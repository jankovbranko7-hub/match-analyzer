"""Bilanz: Prognosen festhalten und gegen die Ergebnisse auswerten.

    python3 analyse/bilanz.py --merken 8549906 8549907   # Prognosen speichern (nach der Analyse)
    python3 analyse/bilanz.py --auswerten                # Ergebnisse holen und Bilanz ziehen
    python3 analyse/bilanz.py --auswerten --liga 17269   # nur eine Liga

Warum das nötig ist: Ohne Aufzeichnung lässt sich nie unterscheiden, ob das Modell
verzerrt ist oder ob es einfach Pech hatte. Am 26.09.2026 waren 15 Spiele ausgewertet –
damit wäre erst eine Verzerrung von 35 Prozentpunkten nachweisbar gewesen. Für
10 Prozentpunkte braucht es rund 190 Spiele, für 5 Prozentpunkte rund 750.

`analyse/bilanz.json` liegt im Git und wächst mit jeder Analyse. Einmal eingetragene
Prognosen werden **nie** nachträglich geändert – auch nicht, wenn sich die Teamdaten
später ändern. Sonst wäre die Auswertung wertlos.
"""
import argparse, json, math, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modell as M

BILANZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bilanz.json")

# Die fünf Wetten aus CLAUDE.md. Unentschieden ist bewusst nicht dabei.
WETTEN = {'H': 'Sieg Heim', 'A': 'Sieg Auswärts', 'O25': 'Über 2,5',
          'U25': 'Unter 2,5', 'BTTS': 'Beide treffen'}
QUOTENFELD = {'H': 'odds_ft_1', 'A': 'odds_ft_2', 'O25': 'odds_ft_over25',
              'U25': 'odds_ft_under25', 'BTTS': 'odds_btts_yes'}

# Spiele mit diesen Status wurden nie gespielt. Sie zaehlen weder als Treffer noch als
# Fehltipp und duerfen nicht ewig als "offen" stehen bleiben.
ABGESAGT = ('suspended', 'canceled', 'cancelled', 'postponed', 'abandoned')


def laden():
    if not os.path.exists(BILANZ):
        return []
    with open(BILANZ) as f:
        return json.load(f)


def speichern(eintraege):
    with open(BILANZ, 'w') as f:
        json.dump(eintraege, f, indent=1, ensure_ascii=False)


def bester_tipp(p):
    """Variante A: die Wette mit der höchsten Wahrscheinlichkeit, ohne Rücksicht auf den Preis."""
    k = max(WETTEN, key=lambda k: p[k])
    return k, p[k]


def getroffen(tipp, h, a):
    return {'H': h > a, 'A': h < a, 'O25': h + a >= 3,
            'U25': h + a <= 2, 'BTTS': h > 0 and a > 0}[tipp]


# ---------------------------------------------------------------- Merken

def merken(mid, args):
    eintraege = laden()
    if any(e['id'] == mid for e in eintraege):
        print(f"  {mid} steht schon in der Bilanz, unverändert gelassen.")
        return
    r = M.berechne(mid, args)
    m = r['match']
    if r['gesperrt']:
        print(f"  {m['home_name']} - {m['away_name']}: gesperrt, nicht aufgenommen.")
        return
    p = {k: float(v) for k, v in r['p'].items()}
    tipp, pt = bester_tipp(p)
    eintraege.append(dict(
        id=mid, liga=r['sid'], datum_unix=m['date_unix'],
        heim=m['home_name'], ausw=m['away_name'],
        lh=round(r['lh'], 3), la=round(r['la'], 3),
        p={k: round(v, 4) for k, v in p.items()},
        tipp=tipp, p_tipp=round(pt, 4), faire_quote=round(1 / pt, 2),
        quote=m.get(QUOTENFELD[tipp]) or None,
        ergebnis=None))
    print(f"  gemerkt: {m['home_name']} - {m['away_name']} | {WETTEN[tipp]} {pt*100:.1f} %")
    speichern(eintraege)


# ---------------------------------------------------------------- Auswerten

def z_wert(ps, treffer):
    e = sum(ps)
    sd = math.sqrt(sum(p * (1 - p) for p in ps)) or 1e-9
    return e, sd, (treffer - e) / sd


def zeile(name, ps, treffer):
    e, sd, z = z_wert(ps, treffer)
    urteil = "SIGNIFIKANT" if abs(z) > 1.96 else "im Zufallsbereich"
    print(f"  {name:20s} erwartet {e:6.1f}   tatsächlich {treffer:4.0f}   ±{sd:.1f}   z={z:+.2f}   {urteil}")


def auswerten(args):
    eintraege = laden()
    if not eintraege:
        print("Bilanz ist leer. Erst mit --merken Prognosen aufnehmen.")
        return

    # Fehlende Ergebnisse nachholen
    for e in eintraege:
        if e['ergebnis'] is None:
            m = M.hole("match", {"match_id": e['id']}, f"erg_{e['id']}.json",
                       argparse.Namespace(daten=args.daten, neu=True))['data']
            if m['status'] == 'complete':
                e['ergebnis'] = {'h': m['homeGoalCount'], 'a': m['awayGoalCount']}
            elif m['status'] in ABGESAGT:
                e['ergebnis'] = {'abgesagt': m['status']}
    speichern(eintraege)

    fertig = [e for e in eintraege if e['ergebnis'] and not e['ergebnis'].get('abgesagt')]
    abgesagt = [e for e in eintraege if e['ergebnis'] and e['ergebnis'].get('abgesagt')]
    if args.liga:
        fertig = [e for e in fertig if e['liga'] == args.liga]
    offen = len([e for e in eintraege if e['ergebnis'] is None])
    if not fertig:
        print(f"Noch kein Spiel beendet ({offen} offen).")
        return

    zusatz = f", {len(abgesagt)} abgesagt" if abgesagt else ""
    print(f"=== Bilanz über {len(fertig)} beendete Spiele ({offen} noch offen{zusatz}) ===\n")
    treffer = sum(getroffen(e['tipp'], e['ergebnis']['h'], e['ergebnis']['a']) for e in fertig)
    zeile("Tipps getroffen", [e['p_tipp'] for e in fertig], treffer)
    for k in ('BTTS', 'O25', 'H', 'A'):
        zeile(WETTEN[k], [e['p'][k] for e in fertig],
              sum(getroffen(k, e['ergebnis']['h'], e['ergebnis']['a']) for e in fertig))

    # Tore: Menge stimmt? (kein z-Test, sondern direkter Vergleich)
    pt = sum(e['lh'] + e['la'] for e in fertig)
    at = sum(e['ergebnis']['h'] + e['ergebnis']['a'] for e in fertig)
    print(f"\n  Tore erwartet {pt:.1f}, tatsächlich {at}, Abweichung {at-pt:+.1f}"
          f" ({(at/pt-1)*100:+.1f} %)")

    # Geld: nur dort, wo eine Quote vorlag
    mitq = [e for e in fertig if e.get('quote') and e['quote'] > 1]
    if mitq:
        ein = 10 * len(mitq)
        aus = sum(10 * e['quote'] for e in mitq
                  if getroffen(e['tipp'], e['ergebnis']['h'], e['ergebnis']['a']))
        val = [e for e in mitq if e['quote'] > e['faire_quote']]
        vaus = sum(10 * e['quote'] for e in val
                   if getroffen(e['tipp'], e['ergebnis']['h'], e['ergebnis']['a']))
        print(f"\n  Alle {len(mitq)} Tipps zu 10 €: Einsatz {ein} €, zurück {aus:.0f} €,"
              f" Saldo {aus-ein:+.0f} € ({(aus/ein-1)*100:+.1f} %)")
        if val:
            print(f"  Nur die {len(val)} mit Value:  Einsatz {10*len(val)} €, zurück {vaus:.0f} €,"
                  f" Saldo {vaus-10*len(val):+.0f} €")

    # Aussagekraft
    n = len(fertig)
    d = (1.96 + 0.84) * math.sqrt(0.25 / n) * 100
    print(f"\n  Aussagekraft: Mit {n} Spielen wäre erst eine Verzerrung ab rund"
          f" {d:.0f} Prozentpunkten nachweisbar.")
    for e in abgesagt:
        print(f"  Nicht gespielt ({e['ergebnis']['abgesagt']}): {e['heim']} – {e['ausw']}"
              f" – zählt weder als Treffer noch als Fehltipp.")
    if n < 190:
        print(f"  Für 10 Prozentpunkte braucht es rund 190 Spiele, für 5 rund 750."
              f" Bis dahin sind Abweichungen kein Grund, die Gewichte anzufassen.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Prognosen merken und auswerten")
    ap.add_argument("--merken", nargs="+", type=int, metavar="ID", help="Prognosen dieser Spiele speichern")
    ap.add_argument("--auswerten", action="store_true", help="Ergebnisse holen und Bilanz ziehen")
    ap.add_argument("--liga", type=int, help="nur diese Saison-ID auswerten")
    ap.add_argument("--markt", type=float, default=M.MARKT_ANTEIL)
    ap.add_argument("--neu", action="store_true")
    ap.add_argument("--trotzdem", action="store_true")
    ap.add_argument("--daten", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "daten"))
    args = ap.parse_args()
    if args.merken:
        for mid in args.merken:
            merken(mid, args)
    if args.auswerten:
        auswerten(args)
    if not args.merken and not args.auswerten:
        ap.print_help()
