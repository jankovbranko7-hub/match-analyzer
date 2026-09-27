"""Backtest: das bestehende Modell an historischen Spielen messen.

    python3 analyse/backtest.py --saison 16540              # eine Saison
    python3 analyse/backtest.py --liga "USL Championship"   # alle Saisons einer Liga
    python3 analyse/backtest.py --xg-aera --ligen 10        # zehn Ligen ab 2019/20

**Dieses Skript ändert das Modell nicht und darf es nie tun.**

Es ruft dieselben Funktionen auf, die auch `modell.py` für eine echte Prognose verwendet
(`strengths`, `matrix`, `probs`) und liest dieselben Konstanten. Neu ist nur die
Daten-Beschaffung: Statt den aktuellen Saisonstand von FootyStats zu holen, baut es den
Stand **vor jedem einzelnen Spiel** aus den vorherigen Spieltagen nach (walk-forward).
So sieht das Modell nie etwas, das zum Zeitpunkt der Prognose noch nicht bekannt war.

Warum es nichts ändern darf: Über tausende Spiele lassen sich immer Gewichte finden, die
rückwärts besser aussehen und vorwärts schlechter sind. Der Backtest sagt, **wie gut das
jetzige Modell ist** – er entscheidet nicht, wie es auszusehen hat. Eine Änderung der
Gewichte verlangt weiterhin die ausdrückliche Zustimmung des Nutzers (siehe CLAUDE.md).

Einschränkungen, die man beim Lesen der Zahlen kennen muss:
- Die Form der letzten 6 Spiele stammt hier nur aus Ligaspielen, live aus `lastx`
  (alle Wettbewerbe). Die Werte sind nah, aber nicht identisch.
- xG liefert FootyStats erst ab der Saison 2019/20. Ältere Spiele sind unbrauchbar,
  weil das Modell xG mit 70 % gewichtet.
"""
import argparse, json, math, os, sys, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modell as M

WETTEN = ['H', 'A', 'O25', 'U25', 'BTTS']


# ---------------------------------------------------------------- Daten

def saison_holen(sid, args):
    """Alle Spiele einer Saison. Eine Abfrage pro Saison, danach aus dem Cache."""
    pfad = os.path.join(args.daten, f"saison_{sid}.json")
    if os.path.exists(pfad) and not args.neu:
        return json.load(open(pfad))
    url = "https://api.football-data-api.com/league-matches?" + urllib.parse.urlencode(
        {"season_id": sid, "key": M.api_key()})
    with urllib.request.urlopen(url, timeout=120) as r:
        d = json.load(r)
    if not d.get('success'):
        return []
    spiele = [m for m in (d.get('data') or []) if m.get('status') == 'complete']
    os.makedirs(args.daten, exist_ok=True)
    json.dump(spiele, open(pfad, 'w'))
    return spiele


# ---------------------------------------------------------------- Stand vor dem Spiel

class Lauf:
    """Sammelt den Saisonstand jedes Teams, Spiel für Spiel."""

    def __init__(self):
        self.t = {}          # team_id -> laufende Summen
        self.h2h = {}        # (a,b) sortiert -> Liste (zeit, tore)

    def leer(self):
        return dict(sp_h=0, sp_a=0, tore_h=0, tore_a=0, geg_h=0, geg_a=0,
                    xg_h=0.0, xg_a=0.0, xga_h=0.0, xga_a=0.0, letzte=[])

    def stats(self, tid):
        """Baut ein Dict mit denselben Feldnamen, die modell.strengths() erwartet."""
        d = self.t.get(tid) or self.leer()
        nh, na = d['sp_h'], d['sp_a']; n = nh + na
        if n == 0: return None
        q = lambda z, m: (z / m) if m else 0.0
        return {
            'seasonMatchesPlayed_overall': n,
            'seasonMatchesPlayed_home': nh, 'seasonMatchesPlayed_away': na,
            'seasonScoredAVG_home': q(d['tore_h'], nh), 'seasonScoredAVG_away': q(d['tore_a'], na),
            'seasonScoredAVG_overall': q(d['tore_h'] + d['tore_a'], n),
            'seasonConcededAVG_home': q(d['geg_h'], nh), 'seasonConcededAVG_away': q(d['geg_a'], na),
            'seasonConcededAVG_overall': q(d['geg_h'] + d['geg_a'], n),
            'xg_for_avg_home': q(d['xg_h'], nh), 'xg_for_avg_away': q(d['xg_a'], na),
            'xg_for_avg_overall': q(d['xg_h'] + d['xg_a'], n),
            'xg_against_avg_home': q(d['xga_h'], nh), 'xg_against_avg_away': q(d['xga_a'], na),
            'xg_against_avg_overall': q(d['xga_h'] + d['xga_a'], n),
        }

    def form6(self, tid):
        """Die letzten 6 Ligaspiele, im Format, das modell.strengths() erwartet."""
        d = self.t.get(tid)
        if not d or not d['letzte']: return None
        L = d['letzte'][-6:]; n = len(L)
        s = lambda i: sum(x[i] for x in L) / n
        return {'stats': {'seasonScoredAVG_overall': s(0), 'seasonConcededAVG_overall': s(1),
                          'xg_for_avg_overall': s(2), 'xg_against_avg_overall': s(3)}}

    def liga(self):
        """Liga-Durchschnitt aus dem bisherigen Saisonverlauf."""
        th = sum(d['tore_h'] for d in self.t.values()); nh = sum(d['sp_h'] for d in self.t.values())
        ta = sum(d['tore_a'] for d in self.t.values()); na = sum(d['sp_a'] for d in self.t.values())
        xh = sum(d['xg_h'] for d in self.t.values()); xa = sum(d['xg_a'] for d in self.t.values())
        if not nh or not na: return None
        return dict(home=th / nh, away=ta / na, xhome=xh / nh, xaway=xa / na)

    def h2h_werte(self, a, b, zeit):
        """Dieselbe Regel wie im Modell: nur Duelle der letzten H2H_MAX_JAHRE, Gewicht n/(n+k)."""
        paar = self.h2h.get(tuple(sorted((a, b))), [])
        jung = [t for z, t in paar if zeit - z <= M.H2H_MAX_JAHRE * 365 * 86400]
        if not jung: return 0.0, None
        return M.H2H_ANTEIL * len(jung) / (len(jung) + M.H2H_DAEMPFUNG_K), sum(jung) / len(jung)

    def buchen(self, m):
        h, a = m['homeID'], m['awayID']
        gh, ga = m['homeGoalCount'], m['awayGoalCount']
        xh = m.get('team_a_xg') or gh; xa = m.get('team_b_xg') or ga
        for tid in (h, a):
            self.t.setdefault(tid, self.leer())
        d = self.t[h]
        d['sp_h'] += 1; d['tore_h'] += gh; d['geg_h'] += ga; d['xg_h'] += xh; d['xga_h'] += xa
        d['letzte'].append((gh, ga, xh, xa))
        d = self.t[a]
        d['sp_a'] += 1; d['tore_a'] += ga; d['geg_a'] += gh; d['xg_a'] += xa; d['xga_a'] += xh
        d['letzte'].append((ga, gh, xa, xh))
        self.h2h.setdefault(tuple(sorted((h, a))), []).append((m['date_unix'], gh + ga))


# ---------------------------------------------------------------- Walk-forward

def saison_durchlaufen(spiele, ergebnisse):
    """Geht eine Saison chronologisch durch und prognostiziert jedes Spiel aus der Vergangenheit."""
    lauf = Lauf()
    for m in sorted(spiele, key=lambda x: x['date_unix']):
        L = lauf.liga()
        sh, sa = lauf.stats(m['homeID']), lauf.stats(m['awayID'])
        if L and sh and sa and min(sh['seasonMatchesPlayed_overall'],
                                   sa['seasonMatchesPlayed_overall']) >= M.MIN_SAISONSPIELE:
            f6h, f6a = lauf.form6(m['homeID']), lauf.form6(m['awayID'])
            ah, dh = M.strengths({'stats': sh}, 'home', L, f6h)
            aa, da = M.strengths({'stats': sa}, 'away', L, f6a)
            b = M.LIGA_BASIS_XG
            lh = ((1 - b) * L['home'] + b * L['xhome']) * ah * da
            la = ((1 - b) * L['away'] + b * L['xaway']) * aa * dh
            w, tore = lauf.h2h_werte(m['homeID'], m['awayID'], m['date_unix'])
            if w:
                tot = lh + la; k = (1 - w) + w * tore / tot; lh *= k; la *= k
            p = {k: float(v) for k, v in M.probs(M.matrix(lh, la)).items()}
            gh, ga = m['homeGoalCount'], m['awayGoalCount']
            ergebnisse.append(dict(lh=lh, la=la, p=p, gh=gh, ga=ga,
                                   quoten={'H': m.get('odds_ft_1'), 'A': m.get('odds_ft_2'),
                                           'O25': m.get('odds_ft_over25'),
                                           'U25': m.get('odds_ft_under25'),
                                           'BTTS': m.get('odds_btts_yes')}))
        lauf.buchen(m)


# ---------------------------------------------------------------- Auswertung

def eingetreten(w, gh, ga):
    return {'H': gh > ga, 'A': gh < ga, 'O25': gh + ga >= 3,
            'U25': gh + ga <= 2, 'BTTS': gh > 0 and ga > 0}[w]


def auc(ps_ja, ps_nein):
    if not ps_ja or not ps_nein: return float('nan')
    ja = sorted(ps_ja); treffer = 0
    for y in ps_nein:
        import bisect
        gr = len(ja) - bisect.bisect_right(ja, y)
        gl = bisect.bisect_right(ja, y) - bisect.bisect_left(ja, y)
        treffer += gr + 0.5 * gl
    return treffer / (len(ps_ja) * len(ps_nein))


def bericht(E, titel):
    n = len(E)
    print(f"\n=== {titel}: {n:,} Spiele ===\n".replace(',', '.'))
    if not n: return

    tipps = [max(WETTEN, key=lambda w: e['p'][w]) for e in E]
    ps = [E[i]['p'][t] for i, t in enumerate(tipps)]
    tr = sum(eingetreten(t, E[i]['gh'], E[i]['ga']) for i, t in enumerate(tipps))
    sd = math.sqrt(sum(p * (1 - p) for p in ps))
    print(f"  Tipps getroffen     erwartet {sum(ps):8.1f}   tatsächlich {tr:6d}"
          f"   ±{sd:.1f}   z={(tr-sum(ps))/sd:+.2f}")

    pt = sum(e['lh'] + e['la'] for e in E); at = sum(e['gh'] + e['ga'] for e in E)
    print(f"  Tore                erwartet {pt:8.1f}   tatsächlich {at:6d}"
          f"   Abweichung {(at/pt-1)*100:+.1f} %\n")

    print(f"  {'Wette':16s}{'erwartet':>11s}{'tatsächlich':>13s}{'z':>8s}{'Trennschärfe':>15s}")
    for w in WETTEN:
        p = [e['p'][w] for e in E]
        ja = [e['p'][w] for e in E if eingetreten(w, e['gh'], e['ga'])]
        ne = [e['p'][w] for e in E if not eingetreten(w, e['gh'], e['ga'])]
        s = math.sqrt(sum(x * (1 - x) for x in p)) or 1e-9
        print(f"  {w:16s}{sum(p):11.1f}{len(ja):13d}{(len(ja)-sum(p))/s:+8.2f}"
              f"{auc(ja, ne):15.3f}")
    print(f"\n  Trennschärfe 0,500 = Münzwurf. Darüber erkennt das Modell die richtigen Spiele.")

    # Geld gegen die echten Vorab-Quoten
    print(f"\n  {'Wette':16s}{'Wetten':>9s}{'Rendite':>10s}{'nur mit Value':>16s}")
    for w in WETTEN:
        mit = [e for e in E if (e['quoten'].get(w) or 0) > 1]
        if not mit: continue
        ein = len(mit); aus = sum(e['quoten'][w] for e in mit if eingetreten(w, e['gh'], e['ga']))
        val = [e for e in mit if e['quoten'][w] > 1 / e['p'][w]]
        vein = len(val); vaus = sum(e['quoten'][w] for e in val if eingetreten(w, e['gh'], e['ga']))
        vt = f"{(vaus/vein-1)*100:+.1f} % ({vein})" if vein else "–"
        print(f"  {w:16s}{ein:9d}{(aus/ein-1)*100:+9.1f} %{vt:>16s}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Das bestehende Modell an historischen Spielen messen")
    ap.add_argument("--saison", type=int, nargs="+", help="Saison-IDs")
    ap.add_argument("--neu", action="store_true")
    ap.add_argument("--daten", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "daten"))
    args = ap.parse_args()
    E = []
    for sid in (args.saison or []):
        sp = saison_holen(sid, args)
        mit_xg = sum(1 for m in sp if (m.get('team_a_xg') or 0) > 0)
        if sp and mit_xg / len(sp) < 0.5:
            print(f"  Saison {sid}: nur {mit_xg}/{len(sp)} Spiele mit xG – übersprungen.")
            continue
        vorher = len(E); saison_durchlaufen(sp, E)
        print(f"  Saison {sid}: {len(sp)} Spiele geladen, {len(E)-vorher} prognostiziert")
    bericht(E, "Backtest")
