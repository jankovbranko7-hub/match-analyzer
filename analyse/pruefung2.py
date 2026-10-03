#!/usr/bin/env python3
"""Walk-forward fuer den neuen Kern (modell2.py) - und der direkte Vergleich mit dem alten.

Strikt vorwaerts: zu jedem Spieltag wird die Poisson-Regression NUR aus Spielen davor
geschaetzt, dann werden die Spiele dieses Tages vorhergesagt. Bewertet werden - genau
wie in pruefung.py und rueckschau.py - nur Spiele, bei denen beide Teams schon MIN_VOR
Vorspiele hatten. Dieselbe Menge, dieselben Masse, damit der Vergleich traegt.

    python3 analyse/pruefung2.py --vergleich                 alt gegen neu
    python3 analyse/pruefung2.py --scan HALBWERT 90 180 360 720 0
    python3 analyse/pruefung2.py --scan RIDGE 1 2 4 8 16
    python3 analyse/pruefung2.py --scan XG_K 0 1 2 3 6
    python3 analyse/pruefung2.py --scan RHO -0.12 -0.07 -0.03 0
    python3 analyse/pruefung2.py --ausgabe neu.pkl           Lambdas sichern

Jeder Scan teilt nach LIGEN in zwei Haelften und sagt EINIG oder UNEINIG, und zaehlt
ab, wie viele Ligen besser werden - dieselbe Disziplin wie bisher. Massstab ist die
Log-Likelihood des echten Ergebnisses, nicht die Trefferquote eines Laufs.
"""
import argparse, math, os, pickle, statistics as st, sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analyse.modell as M
import analyse.modell2 as M2
import analyse.pruefung as P
import analyse.rueckschau as R

MIN_VOR = R.MIN_VOR


def lauf(sids, daten, halbwert, ridge, xg_k, fortschritt=False):
    """Vorhersagen des neuen Kerns, strikt vorwaerts. Gibt eine Zeile je Spiel."""
    rows = []
    for sid in sids:
        sp = P.spiele(sid, daten)
        fl = P.liga_flags(sp)
        S = M2.Saison(sp, xg_k=xg_k, xg_ok=fl['xg_ok'],
                      halbwert=halbwert, ridge=ridge)
        n_vor = {}
        fit = None
        for t in sorted({m['t'] for m in sp}):
            tag = [m for m in sp if m['t'] == t]
            offen = [m for m in tag
                     if n_vor.get(m['h'], 0) >= MIN_VOR and n_vor.get(m['a'], 0) >= MIN_VOR]
            if offen:
                fit = S.bis(t)
            if offen and fit:
                for m in offen:
                    lh, la = M2.erwartete_tore(*fit, S.idx.get(m['h']), S.idx.get(m['a']))
                    rows.append(dict(sid=sid, key=(sid, m['h'], m['a'], m['t']),
                                     lh=lh, la=la, hg=m['hg'], ag=m['ag']))
            for m in tag:
                n_vor[m['h']] = n_vor.get(m['h'], 0) + 1
                n_vor[m['a']] = n_vor.get(m['a'], 0) + 1
        if fortschritt:
            print(f"  Saison {sid}: {sum(1 for r in rows if r['sid'] == sid):5d} "
                  f"bewertete Spiele", flush=True)
    return rows


def score(rows, rho, gleichstand=True):
    """Dieselben Masse wie rueckschau.bewerte: LL je Spiel, Trefferquote, Brier."""
    ll = []; tref = 0; erw = 0.0; brier = 0.0; n = 0
    for r in rows:
        Mx = M2.matrix(r['lh'], r['la'], rho)
        p = M2.wetten(Mx)
        if gleichstand:
            t, pt, _, _ = M.bester_tipp(p, r['lh'], r['la'])
        else:
            t = max(M.WETTEN, key=lambda w: p[w]); pt = p[t]
        ll.append(math.log(max(Mx[min(r['hg'], 10), min(r['ag'], 10)], 1e-12)))
        tref += R.getroffen(t, r['hg'], r['ag']); erw += pt; n += 1
        brier += sum((p[w] - (1 if R.getroffen(w, r['hg'], r['ag']) else 0)) ** 2
                     for w in M.WETTEN) / 5
    return dict(ll=ll, n=n, llm=sum(ll) / n if n else 0.0, tref=tref, erw=erw,
                quote=tref / n if n else 0.0, brier=brier / n if n else 0.0)


def haelften_nach_liga(rows):
    sids = sorted({r['sid'] for r in rows})
    a = [r for r in rows if sids.index(r['sid']) % 2 == 0]
    b = [r for r in rows if sids.index(r['sid']) % 2 == 1]
    return a, b


def zeile(label, r, basis=None):
    t = ''
    if basis is not None:
        _, tt = R.paarweise(r['ll'], basis['ll'])
        t = f"{tt:>+9.2f}"
    print(f"{label:>10s} {r['llm']:10.5f} {r['quote']*100:6.1f}% {r['brier']:9.5f} "
          f"{r['tref']:7d} {r['erw']:9.1f} {t}")


def kopf(label, n, ligen):
    print(f"\n--- {label}: {n} Spiele, {ligen} Ligen")
    print(f"{'':10s} {'LogLik':>10s} {'Quote':>7s} {'Brier':>9s} {'Treffer':>7s} "
          f"{'erwartet':>9s} {'t vs Basis':>9s}")


def scan(sids, args, name, werte):
    """Scannt eine der vier Groessen. RHO braucht keinen neuen Fit."""
    std = dict(HALBWERT=args.halbwert, RIDGE=args.ridge, XG_K=args.xg_k, RHO=args.rho)
    ergebnis = {}
    for v in werte:
        c = dict(std); c[name] = v
        if name == 'RHO':
            rows = ergebnis.get('_rows') or lauf(sids, args.daten, c['HALBWERT'],
                                                 c['RIDGE'], c['XG_K'])
            ergebnis['_rows'] = rows
        else:
            rows = lauf(sids, args.daten, c['HALBWERT'], c['RIDGE'], c['XG_K'])
        ergebnis[v] = (rows, score(rows, c['RHO']))
        print('.', end='', flush=True)
    print()
    basis = ergebnis[werte[0]][1]
    def tab(filt, label):
        sub = {v: score([r for r in ergebnis[v][0] if filt(r)], 
                        v if name == 'RHO' else std['RHO']) for v in werte}
        if name == 'RHO':
            sub = {v: score([r for r in ergebnis[v][0] if filt(r)], v) for v in werte}
        n0 = sub[werte[0]]['n']
        kopf(label, n0, len({r['sid'] for r in ergebnis[werte[0]][0] if filt(r)}))
        best = max(werte, key=lambda v: sub[v]['llm'])
        for v in werte:
            zeile(f'{v:g}', sub[v], sub[werte[0]])
            if v == best:
                print(f"{'':10s}   <== beste")
        return best
    g = tab(lambda r: True, 'ALLE')
    sids_s = sorted({r['sid'] for r in ergebnis[werte[0]][0]})
    ba = tab(lambda r: sids_s.index(r['sid']) % 2 == 0, 'Haelfte A')
    bb = tab(lambda r: sids_s.index(r['sid']) % 2 == 1, 'Haelfte B')
    print(f"\n  Beste gesamt {g:g} | A {ba:g} | B {bb:g}  ->  "
          f"{'EINIG' if ba == bb else 'UNEINIG'}")
    print("  Liga-Abzaehlung gegen die Basis:")
    for v in werte[1:]:
        bei = []
        for sid in sids_s:
            rb = [r for r in ergebnis[werte[0]][0] if r['sid'] == sid]
            rv = [r for r in ergebnis[v][0] if r['sid'] == sid]
            if len(rb) < 20 or len(rb) != len(rv):
                continue
            s, _ = R.paarweise(score(rv, v if name == 'RHO' else std['RHO'])['ll'],
                               score(rb, werte[0] if name == 'RHO' else std['RHO'])['ll'])
            bei.append((s, sid))
        bei.sort(reverse=True)
        ges = sum(x[0] for x in bei)
        pos = sum(1 for s, _ in bei if s > 0)
        anteil = bei[0][0] / ges * 100 if ges else 0.0
        print(f"    {name} {v:g}: {pos} von {len(bei)} Ligen besser, groesste "
              f"{bei[0][1]} mit {bei[0][0]:+.2f} ({anteil:.0f} % des Gewinns)")


def vergleich(sids, args):
    """Alter Kern gegen neuen, auf genau derselben Spielmenge."""
    print("Alter Kern (modell.py ueber pruefung.py) ...", flush=True)
    Z = P.laden(argparse.Namespace(daten=args.daten, ligen=sids, neu=False))
    keys_alt = {}
    for sid in sids:
        sp = P.spiele(sid, args.daten)
        n = {}
        for m in sp:
            if n.get(m['h'], 0) >= MIN_VOR and n.get(m['a'], 0) >= MIN_VOR:
                keys_alt.setdefault(sid, []).append((sid, m['h'], m['a'], m['t']))
            n[m['h']] = n.get(m['h'], 0) + 1
            n[m['a']] = n.get(m['a'], 0) + 1
    flach = [k for sid in sids for k in keys_alt.get(sid, [])]
    assert len(flach) == len(Z), f"{len(flach)} != {len(Z)}"
    for z, k in zip(Z, flach):
        z['key'] = k
    print("Neuer Kern (modell2.py) ...", flush=True)
    rows = lauf(sids, args.daten, args.halbwert, args.ridge, args.xg_k, fortschritt=True)
    gem = {r['key'] for r in rows} & {z['key'] for z in Z}
    rows = [r for r in rows if r['key'] in gem]
    Zs = [z for z in Z if z['key'] in gem]
    ordn = {r['key']: r for r in rows}
    rows = [ordn[z['key']] for z in Zs]
    alt = P.bewerte(Zs, P.STD)
    neu = score(rows, args.rho)
    kopf('VERGLEICH', len(gem), len({r['sid'] for r in rows}))
    zeile('alt', alt)
    zeile('neu', neu, alt)
    s, t = R.paarweise(neu['ll'], alt['ll'])
    print(f"\n  Summe der Log-Likelihood-Differenz {s:+.2f} bei t = {t:+.2f}")
    print(f"  Trefferquote {alt['quote']*100:.1f} % -> {neu['quote']*100:.1f} %, "
          f"Brier {alt['brier']:.5f} -> {neu['brier']:.5f}")
    A, B = haelften_nach_liga(rows)
    sids_s = sorted({r['sid'] for r in rows})
    for lab, filt in (('Haelfte A', lambda r: sids_s.index(r['sid']) % 2 == 0),
                      ('Haelfte B', lambda r: sids_s.index(r['sid']) % 2 == 1)):
        rs = [r for r in rows if filt(r)]
        zs = [z for z in Zs if sids_s.index(z['sid']) % 2 == (0 if lab.endswith('A') else 1)]
        s2, t2 = R.paarweise(score(rs, args.rho)['ll'], P.bewerte(zs, P.STD)['ll'])
        print(f"  {lab}: dLL {s2:+.2f}, t = {t2:+.2f}")
    print("\n  Liga-Abzaehlung:")
    bei = []
    for sid in sids_s:
        rs = [r for r in rows if r['sid'] == sid]
        zs = [z for z in Zs if z['sid'] == sid]
        if len(rs) < 20:
            continue
        s2, t2 = R.paarweise(score(rs, args.rho)['ll'], P.bewerte(zs, P.STD)['ll'])
        bei.append((s2, t2, sid, len(rs)))
    bei.sort(reverse=True)
    for s2, t2, sid, n in bei:
        print(f"    Liga {sid}: {n:4d} Spiele, dLL {s2:>+8.2f}, t {t2:>+6.2f}")
    print(f"  {sum(1 for x in bei if x[0] > 0)} von {len(bei)} Ligen besser")
    return rows, Zs


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--daten', default=os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'daten'))
    ap.add_argument('--ligen', type=int, nargs='*', default=None)
    ap.add_argument('--halbwert', type=float, default=M2.HALBWERT)
    ap.add_argument('--ridge', type=float, default=M2.RIDGE)
    ap.add_argument('--xg-k', dest='xg_k', type=float, default=M2.XG_K)
    ap.add_argument('--rho', type=float, default=M2.RHO)
    ap.add_argument('--vergleich', action='store_true')
    ap.add_argument('--scan', nargs='+', metavar=('NAME', 'WERT'))
    ap.add_argument('--ausgabe', default=None)
    args = ap.parse_args()
    sids = args.ligen or P.saisons(args.daten)
    print(f"{len(sids)} Saisons: {sids}")
    print(f"Einstellung: HALBWERT={args.halbwert:g} RIDGE={args.ridge:g} "
          f"XG_K={args.xg_k:g} RHO={args.rho:g}")
    if args.scan:
        name = args.scan[0].upper()
        werte = [float(x) for x in args.scan[1:]]
        if name not in ('HALBWERT', 'RIDGE', 'XG_K', 'RHO'):
            sys.exit(f"Unbekannte Groesse {name}")
        scan(sids, args, name, werte)
    elif args.vergleich:
        rows, _ = vergleich(sids, args)
        if args.ausgabe:
            pickle.dump(rows, open(args.ausgabe, 'wb'))
    else:
        ap.print_help()


if __name__ == '__main__':
    main()
