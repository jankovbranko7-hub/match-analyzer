"""Rueckschau: das Modell gegen echte Ergebnisse vergangener Spieltage pruefen.

    python3 analyse/rueckschau.py --ligen 16540 15066 16504     # Ligen holen und bewerten
    python3 analyse/rueckschau.py                               # alles aus dem Zwischenspeicher
    python3 analyse/rueckschau.py --konstante XG_ANTEIL --werte 0.4 0.5 0.6 0.7 0.8
    python3 analyse/rueckschau.py --konstante DAEMPFUNG_K --werte 2 3 5 8 12 --haelften

WOZU DAS DA IST
---------------
Der Nutzer hat dieses Werkzeug am 02.10.2026 ausdruecklich verlangt, nachdem zwei
Entscheidungen desselben Tages nur damit zu treffen waren:

  - LAMBDA_DAEMPFUNG = 0,85 sah gegen die Vorab-Quoten stark aus (Steigung 0,81,
    t = -3,5) und fiel gegen echte Ergebnisse durch -> zurueck auf 1,00.
  - LIGA_XG_MIN = 0,65 liess eine Liga mit kaputtem xG durch; 0,85 brachte
    +21,68 Log-Likelihood bei t = +2,91 -> geaendert.

Ohne dieses Werkzeug waere beides Meinung geblieben. ES IST EIN PRUEFGERAET FUER EINEN
VORSCHLAG, KEINE SUCHMASCHINE FUER GEWICHTE. Was damit erlaubt und was verboten ist,
steht in CLAUDE.md, Abschnitt "Rueckschau".

WAS ES MISST
------------
Strikt vorwaerts: Fuer jedes Spiel werden die Teamdaten NUR aus Spielen gerechnet, deren
date_unix kleiner ist. Kein Blick in die Zukunft, kein Spiel bewertet sich selbst. Tore
und Per-Spiel-xG kommen aus `league-matches` (ein Aufruf je Liga).

Maszstab ist die Log-Likelihood des echten Ergebnisses unter der Dixon-Coles-Matrix -
die misst die ganze Verteilung, nicht nur den Tipp. Dazu Trefferquote und Brier.

WAS ES NICHT NACHBAUT, und das ist wichtig
------------------------------------------
  - H2H (hoechstens 10 % und nur auf die Summe; die FootyStats-Duelle reichen Jahre
    zurueck und liegen hier nicht vor).
  - Das Datenfenster: bewertet werden nur Spiele, bei denen beide Teams schon
    MIN_VOR Vorspiele haben - dann ist das Fenster ohnehin aus.
  - Den Gleichstand-Entscheid bei der Tipp-Auswahl nur, wenn --gleichstand gesetzt ist.
  - Die LIGA-SCHRANKEN fuer das xG (LIGA_XG_MIN / LIGA_XG_MAX). Das Werkzeug rechnet mit
    XG_ANTEIL und LIGA_BASIS_XG fuer jede Liga gleich und faengt nur das fehlende xG je Team
    ab. Wer eine Schranke pruefen will, setzt --konstante XG_ANTEIL bzw. LIGA_BASIS_XG je
    Liga von Hand - so sind beide Schranken am 02.10.2026 gemessen worden.

Eine Zahl aus diesem Werkzeug gilt also fuer den Kern des Modells, nicht fuer jede Zeile
von modell.py. Wer sie zitiert, sagt das dazu.
"""
import argparse, collections, json, math, os, pickle, sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modell as M

MIN_VOR = 10                      # beide Teams brauchen so viele Vorspiele
FORM_FENSTER = (4, 6, 8, 10)      # Formfenster, die vorberechnet werden

# Konstanten, die --konstante kennt. Name -> (Schluessel in der Rechnung, Vorgabe)
KONSTANTEN = {
    'XG_ANTEIL':        ('XG',       M.XG_ANTEIL),
    'LIGA_BASIS_XG':    ('BASIS',    M.LIGA_BASIS_XG),
    'SEITE_K':          ('SEITE_K',  M.SEITE_K),
    'DAEMPFUNG_K':      ('DAEMP_K',  M.DAEMPFUNG_K),
    'FORM_ANTEIL':      ('FORM',     M.FORM_ANTEIL),
    'FORM_DAEMPFUNG_K': ('FORM_K',   M.FORM_DAEMPFUNG_K),
    'FORM_FENSTER':     ('FORM_W',   6),
    'DIXON_COLES_RHO':  ('RHO',      M.DIXON_COLES_RHO),
    'LAMBDA_DAEMPFUNG': ('LAM_D',    M.LAMBDA_DAEMPFUNG),
}
STD = {s: v for s, v in KONSTANTEN.values()}


# ---------------------------------------------------------------- Zutaten (Pass 1)

def _mittel(xs):
    return sum(xs) / len(xs) if xs else None


def spiele_der_liga(sid, args):
    d = M.hole("league-matches", {"season_id": sid}, f"lm_{sid}.json", args)['data']
    sp = [dict(t=m['date_unix'], h=m['homeID'], a=m['awayID'],
               hg=m['homeGoalCount'], ag=m['awayGoalCount'],
               hx=m.get('team_a_xg') or 0.0, ax=m.get('team_b_xg') or 0.0)
          for m in d if m['status'] == 'complete' and m.get('homeGoalCount') is not None]
    sp.sort(key=lambda x: x['t'])
    return sp


def zutaten(sid, args):
    """Je bewertbares Spiel die Rohmittelwerte, ausschliesslich aus Spielen davor.

    Die Mittelwerte haengen nicht von den Konstanten ab - nur ihre Verrechnung. Einmal
    vorberechnet, kostet jede Konstanten-Kombination nur noch Sekunden.
    """
    sp = spiele_der_liga(sid, args)
    heim = collections.defaultdict(list); ausw = collections.defaultdict(list)
    chrono = collections.defaultdict(list)
    lh = []; la = []; lxh = []; lxa = []
    out = []
    for m in sp:
        n_h = len(heim[m['h']]) + len(ausw[m['h']])
        n_a = len(heim[m['a']]) + len(ausw[m['a']])
        if n_h >= MIN_VOR and n_a >= MIN_VOR and lh:
            def team(tid, seite):
                sv = heim[tid] if seite == 'home' else ausw[tid]
                ov = heim[tid] + ausw[tid]
                d = dict(n_v=len(sv), n_o=len(ov))
                for nm, v in (('v', sv), ('o', ov)):
                    for i, k in enumerate(('tf', 'xf', 'tg', 'xg')):
                        d[f'{nm}_{k}'] = _mittel([e[i] for e in v])
                for w in FORM_FENSTER:
                    f = chrono[tid][-w:]
                    d[f'f{w}_n'] = len(f)
                    for i, k in enumerate(('tf', 'xf', 'tg', 'xg')):
                        d[f'f{w}_{k}'] = _mittel([e[i] for e in f])
                return d
            out.append(dict(sid=sid, hg=m['hg'], ag=m['ag'],
                            L=dict(h=_mittel(lh), a=_mittel(la),
                                   xh=_mittel(lxh), xa=_mittel(lxa)),
                            H=team(m['h'], 'home'), A=team(m['a'], 'away')))
        heim[m['h']].append((m['hg'], m['hx'], m['ag'], m['ax']))
        ausw[m['a']].append((m['ag'], m['ax'], m['hg'], m['hx']))
        chrono[m['h']].append((m['hg'], m['hx'], m['ag'], m['ax']))
        chrono[m['a']].append((m['ag'], m['ax'], m['hg'], m['hx']))
        lh.append(m['hg']); la.append(m['ag']); lxh.append(m['hx']); lxa.append(m['ax'])
    return out


# ---------------------------------------------------------------- Bewertung (Pass 2)

_I, _J = np.indices((11, 11))
_MH = _I > _J; _MA = _I < _J; _MO = _I + _J >= 3; _MB = (_I > 0) & (_J > 0)


def lambdas(z, c):
    """Erwartete Tore aus den Zutaten, mit den Konstanten in c. Spiegelt modell.py."""
    L = z['L']; Lh, La, Lxh, Lxa = L['h'], L['a'], L['xh'], L['xa']
    if min(Lh, La, Lxh, Lxa) <= 0:
        return None
    Lg_o = (Lh + La) / 2; Lx_o = (Lxh + Lxa) / 2

    def term(tore, x, Lx, Lg):
        if tore is None:
            return None
        if (x or 0) == 0 and tore > 0:        # fehlendes xG, wie modell.xg_fehlt
            return tore / Lg
        return c['XG'] * x / Lx + (1 - c['XG']) * tore / Lg

    def staerke(d, seite):
        Lg_v, Lx_v = (Lh, Lxh) if seite == 'home' else (La, Lxa)
        Lg_g, Lx_g = (La, Lxa) if seite == 'home' else (Lh, Lxh)
        att_o = term(d['o_tf'], d['o_xf'], Lx_o, Lg_o)
        dfn_o = term(d['o_tg'], d['o_xg'], Lx_o, Lg_o)
        if att_o is None:
            return None
        if d['n_v']:
            att_v = term(d['v_tf'], d['v_xf'], Lx_v, Lg_v)
            dfn_v = term(d['v_tg'], d['v_xg'], Lx_g, Lg_g)
        else:
            att_v, dfn_v = att_o, dfn_o
        wv = d['n_v'] / (d['n_v'] + c['SEITE_K'])
        att = M.shrink(wv * att_v + (1 - wv) * att_o, d['n_o'], c['DAEMP_K'])
        dfn = M.shrink(wv * dfn_v + (1 - wv) * dfn_o, d['n_o'], c['DAEMP_K'])
        w = int(c['FORM_W']); n = d[f'f{w}_n']
        if n and c['FORM'] > 0:
            af = term(d[f'f{w}_tf'], d[f'f{w}_xf'], Lx_o, Lg_o)
            df = term(d[f'f{w}_tg'], d[f'f{w}_xg'], Lx_o, Lg_o)
            if af is not None:
                att = (1 - c['FORM']) * att + c['FORM'] * M.shrink(af, n, c['FORM_K'])
                dfn = (1 - c['FORM']) * dfn + c['FORM'] * M.shrink(df, n, c['FORM_K'])
        return att, dfn

    h = staerke(z['H'], 'home'); a = staerke(z['A'], 'away')
    if not h or not a:
        return None
    b = c['BASIS']
    bh = (1 - b) * Lh + b * Lxh; ba = (1 - b) * La + b * Lxa
    lh = bh * h[0] * a[1]; la = ba * a[0] * h[1]
    k = c['LAM_D']
    return bh + k * (lh - bh), ba + k * (la - ba)


def getroffen(w, h, a):
    return {'H': h > a, 'A': h < a, 'O25': h + a >= 3,
            'U25': h + a <= 2, 'BTTS': h > 0 and a > 0}[w]


def bewerte(menge, c, gleichstand=False):
    """Gibt Kennzahlen und die Log-Likelihood je Spiel zurueck (None = nicht rechenbar)."""
    ll = []; n = 0; tref = 0; erw = 0.0; brier = 0.0
    for z in menge:
        r = lambdas(z, c)
        if not r:
            ll.append(None); continue
        Mx = M.matrix(r[0], r[1], c['RHO'])
        p = dict(H=Mx[_MH].sum(), A=Mx[_MA].sum(), O25=Mx[_MO].sum(), BTTS=Mx[_MB].sum())
        p['U25'] = 1 - p['O25']
        p = {k: float(v) for k, v in p.items()}
        if gleichstand:
            t, pt, _, _ = M.bester_tipp(p, r[0], r[1])
        else:
            t = max(M.WETTEN, key=lambda w: p[w]); pt = p[t]
        ll.append(math.log(max(Mx[min(z['hg'], 10), min(z['ag'], 10)], 1e-12)))
        tref += getroffen(t, z['hg'], z['ag']); erw += pt; n += 1
        brier += sum((p[w] - (1 if getroffen(w, z['hg'], z['ag']) else 0)) ** 2
                     for w in M.WETTEN) / 5
    g = [v for v in ll if v is not None]
    return dict(ll=ll, n=n, llm=sum(g) / len(g) if g else 0.0, tref=tref, erw=erw,
                quote=tref / n if n else 0.0, brier=brier / n if n else 0.0)


def paarweise(a, b):
    """Paarweiser t-Test auf der Log-Likelihood je Spiel. Gibt (Summe, t) zurueck."""
    d = [x - y for x, y in zip(a, b) if x is not None and y is not None]
    k = len(d)
    if k < 2:
        return 0.0, 0.0
    mu = sum(d) / k
    sd = math.sqrt(sum((v - mu) ** 2 for v in d) / (k - 1))
    se = sd / math.sqrt(k) or 1e-12
    return mu * k, mu / se


# ---------------------------------------------------------------- Ablauf

def laden(args):
    """Zutaten aus dem Zwischenspeicher oder neu berechnen."""
    pfad = os.path.join(args.daten, 'rueckschau_zutaten.pkl')
    if args.ligen:
        sids = args.ligen
    else:
        sids = sorted(int(os.path.basename(p).split('_')[1].split('.')[0])
                      for p in __import__('glob').glob(os.path.join(args.daten, 'lm_*.json')))
        if not sids:
            sys.exit("Keine league-matches im Zwischenspeicher. Mit --ligen <season_id ...> holen.")
    schluessel = tuple(sids) + (MIN_VOR,)
    if os.path.exists(pfad) and not args.neu:
        gespeichert = pickle.load(open(pfad, 'rb'))
        if gespeichert.get('schluessel') == schluessel:
            return gespeichert['zutaten']
    alle = []
    for sid in sids:
        try:
            z = zutaten(sid, args)
        except Exception as e:
            print(f"  Saison {sid}: uebersprungen ({type(e).__name__}: {e})")
            continue
        print(f"  Saison {sid}: {len(z):5d} bewertbare Spiele", flush=True)
        alle += z
    with open(pfad, 'wb') as f:
        pickle.dump(dict(schluessel=schluessel, zutaten=alle), f)
    return alle


def haelften(menge):
    """Teilt nach LIGEN, nicht nach Spielen - sonst sind die Haelften nicht unabhaengig."""
    sids = sorted({z['sid'] for z in menge})
    a = [z for z in menge if sids.index(z['sid']) % 2 == 0]
    b = [z for z in menge if sids.index(z['sid']) % 2 == 1]
    return a, b


def kalibrierung(menge, args):
    r = bewerte(menge, STD, gleichstand=args.gleichstand)
    print(f"=== Kalibrierung ueber {r['n']} Spiele aus "
          f"{len({z['sid'] for z in menge})} Ligen, strikt vorwaerts\n")
    def z_wert(ps, t):
        e = sum(ps); sd = math.sqrt(sum(p * (1 - p) for p in ps)) or 1e-9
        return e, sd, (t - e) / sd
    ptipp = []; pro = {w: [] for w in M.WETTEN}; tref = {w: 0 for w in M.WETTEN}
    tore_e = 0.0; tore_a = 0
    for z in menge:
        lam = lambdas(z, STD)
        if not lam: continue
        Mx = M.matrix(lam[0], lam[1], STD['RHO'])
        p = dict(H=Mx[_MH].sum(), A=Mx[_MA].sum(), O25=Mx[_MO].sum(), BTTS=Mx[_MB].sum())
        p['U25'] = 1 - p['O25']; p = {k: float(v) for k, v in p.items()}
        if args.gleichstand:
            t, pt, _, _ = M.bester_tipp(p, lam[0], lam[1])
        else:
            t = max(M.WETTEN, key=lambda w: p[w]); pt = p[t]
        ptipp.append(pt)
        for w in M.WETTEN:
            pro[w].append(p[w]); tref[w] += getroffen(w, z['hg'], z['ag'])
        tore_e += lam[0] + lam[1]; tore_a += z['hg'] + z['ag']
    e, sd, zz = z_wert(ptipp, r['tref'])
    print(f"  {'Tipps getroffen':18s} {r['tref']:5d}  erwartet {e:7.1f}  +-{sd:.1f}  z={zz:+5.2f}"
          f"   {100*r['quote']:.1f} % gegen {100*e/len(ptipp):.1f} % vorhergesagt")
    for w in M.WETTEN:
        e, sd, zz = z_wert(pro[w], tref[w])
        print(f"  {w:18s} {tref[w]:5d}  erwartet {e:7.1f}  +-{sd:.1f}  z={zz:+5.2f}")
    print(f"\n  Tore erwartet {tore_e:.0f}, tatsaechlich {tore_a}, "
          f"Abweichung {100*(tore_a/tore_e-1):+.1f} %")
    print(f"  Log-Likelihood je Spiel {r['llm']:.5f}   Brier {r['brier']:.5f}")


def durchlauf(menge, name, werte, args):
    schl = KONSTANTEN[name][0]
    mengen = [('alle', menge)]
    if args.haelften:
        a, b = haelften(menge)
        mengen = [('Haelfte A', a), ('Haelfte B', b)]
        print(f"Haelften nach Ligen getrennt: A {len(a)} Spiele aus "
              f"{len({z['sid'] for z in a})} Ligen, B {len(b)} aus "
              f"{len({z['sid'] for z in b})} Ligen\n")
    basis = {lab: bewerte(m, STD, args.gleichstand) for lab, m in mengen}
    print(f"{name} - jetzt {KONSTANTEN[name][1]}\n")
    kopf = f"  {'Wert':>8s}"
    for lab, _ in mengen:
        kopf += f" | {lab+' LogLik':>18s} {'Quote':>7s} {'t gegen jetzt':>14s}"
    print(kopf); print('  ' + '-' * (len(kopf) - 2))
    beste = {}
    for v in werte:
        c = dict(STD); c[schl] = v
        zeile = f"  {v:>8}"
        for lab, m in mengen:
            r = bewerte(m, c, args.gleichstand)
            _, t = paarweise(r['ll'], basis[lab]['ll'])
            beste.setdefault(lab, []).append((r['llm'], v))
            zeile += f" | {r['llm']:18.5f} {100*r['quote']:6.1f}% {t:+14.2f}"
        mark = '   <- jetzt' if v == KONSTANTEN[name][1] else ''
        print(zeile + mark, flush=True)
    print()
    for lab, _ in mengen:
        print(f"  beste in {lab}: {max(beste[lab])[1]}")
    if args.haelften:
        ba = max(beste['Haelfte A'])[1]; bb = max(beste['Haelfte B'])[1]
        if ba == bb:
            print(f"\n  BEIDE HAELFTEN EINIG bei {ba}. Erst damit lohnt ein Blick -"
                  f" und auch dann gilt: nur aendern, wenn der Nutzer es verlangt.")
        else:
            print(f"\n  UNEINIG ({ba} gegen {bb}). Das ist Anpassung an Rauschen,"
                  f" keine Verbesserung. Konstante bleibt.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Modell gegen echte Ergebnisse pruefen")
    ap.add_argument("--ligen", nargs="+", type=int, metavar="SID",
                    help="Saison-IDs holen und bewerten (Standard: alles im Zwischenspeicher)")
    ap.add_argument("--konstante", choices=sorted(KONSTANTEN),
                    help="diese Konstante durchfahren")
    ap.add_argument("--werte", nargs="+", type=float, help="Werte dafuer")
    ap.add_argument("--haelften", action="store_true",
                    help="nach Ligen in zwei Haelften teilen (gegen Anpassung)")
    ap.add_argument("--gleichstand", action="store_true",
                    help="Tipp mit dem Gleichstand-Entscheid waehlen statt mit argmax")
    ap.add_argument("--neu", action="store_true", help="Zutaten neu berechnen")
    ap.add_argument("--daten", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "daten"))
    args = ap.parse_args()
    Z = laden(args)
    if not Z:
        sys.exit("Keine bewertbaren Spiele.")
    print()
    if args.konstante:
        if not args.werte:
            sys.exit("--konstante braucht --werte")
        w = [int(v) if float(v).is_integer() and args.konstante != 'DIXON_COLES_RHO' else v
             for v in args.werte]
        durchlauf(Z, args.konstante, w, args)
    else:
        kalibrierung(Z, args)
