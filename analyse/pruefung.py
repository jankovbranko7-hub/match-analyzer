#!/usr/bin/env python3
"""Tiefenpruefung des Modells gegen echte Ergebnisse - Erweiterung von rueckschau.py.

rueckschau.py prueft die Konstanten des Rechenkerns. Diese Datei prueft, ob dem Modell
etwas FEHLT: Gegnerstaerke, Ruhetage, Punkte pro Spiel, die Vorab-Quoten. Dazu braucht
sie mehr Zutaten als rueckschau.py vorberechnet, deshalb eine eigene Datei.

Alles laeuft strikt vorwaerts: Teamdaten je Spiel nur aus Spielen DAVOR, bewertet nur
Spiele, bei denen beide Teams schon MIN_VOR Vorspiele hatten. Quelle sind die
zwischengespeicherten `league-matches`-Antworten - keine zusaetzliche API-Abfrage.

    python3 analyse/pruefung.py --gegner        Gegnerstaerke (Strength of Schedule)
    python3 analyse/pruefung.py --residuen      woran haengt der Modellfehler?
    python3 analyse/pruefung.py --markt         MARKT_ANTEIL gegen echte Ergebnisse
    python3 analyse/pruefung.py --widerspruch   Modell gegen Markt: wer hat recht?

Jeder Durchlauf teilt nach LIGEN in zwei Haelften und sagt EINIG oder UNEINIG - dieselbe
Disziplin wie in rueckschau.py. Eine Zahl hieraus ist eine Aussage ueber das MODELL,
nie ueber ein einzelnes Spiel, und begruendet keinen Tipp (Regel in CLAUDE.md).

Die Grenzen von rueckschau.py gelten hier genauso: H2H und das Datenfenster werden
nicht nachgebaut. Die Liga-xG-Schranken (LIGA_XG_MIN/MAX) SIND nachgebaut - ohne sie
sieht jede Idee besser aus, die ein kaputtes xG ausgleicht (am 03.10.2026 zweimal
passiert, siehe CLAUDE.md).
"""
import argparse, collections, json, math, os, pickle, statistics as st, sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analyse.modell as M
import analyse.rueckschau as R

MIN_VOR = R.MIN_VOR
FORM_FENSTER = R.FORM_FENSTER
SOS_ITER = 3                      # Iterationen des Angriff/Abwehr-Fits je Spiel
TAG = 86400.0
QUOTEN = ['odds_ft_1', 'odds_ft_x', 'odds_ft_2', 'odds_ft_over25',
          'odds_ft_under25', 'odds_btts_yes', 'odds_btts_no']

# Die Zusatz-Anteile. 0 heisst jeweils: heutiges Modell.
STD = {**R.STD, 'GEGNER': 0.0, 'PPG': 0.0, 'SUM_D': 1.0, 'MARKT': 0.0}

_I, _J = np.indices((11, 11))
_MH = _I > _J; _MA = _I < _J; _MO = _I + _J >= 3; _MB = (_I > 0) & (_J > 0)


def _m(xs):
    return st.fmean(xs) if xs else None


# ------------------------------------------------------------------ Rohdaten

def spiele(sid, daten):
    """Liest eine zwischengespeicherte league-matches-Antwort. Keine API-Abfrage."""
    with open(os.path.join(daten, f'lm_{sid}.json')) as f:
        d = json.load(f)['data']
    sp = [dict(t=m['date_unix'], h=m['homeID'], a=m['awayID'],
               hg=m['homeGoalCount'], ag=m['awayGoalCount'],
               hx=m.get('team_a_xg') or 0.0, ax=m.get('team_b_xg') or 0.0,
               q=m if all((m.get(k) or 0) > 1 for k in QUOTEN) else None)
          for m in d if m['status'] == 'complete' and m.get('homeGoalCount') is not None]
    sp.sort(key=lambda x: x['t'])
    return sp


def saisons(daten, min_spiele=120):
    out = []
    for f in sorted(os.listdir(daten)):
        if not f.startswith('lm_'):
            continue
        sid = int(f.split('_')[1].split('.')[0])
        try:
            if len(spiele(sid, daten)) >= min_spiele:
                out.append(sid)
        except Exception:
            pass
    return out


def liga_flags(sp):
    """Liga-xG-Test wie modell.league(): Gesamt-xG gegen Gesamt-Tore der Saison."""
    tore = sum(m['hg'] + m['ag'] for m in sp)
    xg = sum(m['hx'] + m['ax'] for m in sp)
    r = xg / tore if tore else 0.0
    return dict(xg_rel=r, xg_ok=r >= M.LIGA_XG_MIN,
                basis_ok=M.LIGA_XG_MIN <= r <= M.LIGA_XG_MAX)


class Fit:
    """Iterativer Angriff/Abwehr-Fit ueber die bisherigen Spiele, mit Warmstart.

    Liefert die Gegnerstaerke: att[t] und dfn[t] je Team, aus denen sich das Mittel
    der tatsaechlich bespielten Gegner bilden laesst. Unter dem Modell gilt
        Team-Tore je Spiel ~ Liga-Basis * att_wahr * Mittel(dfn der Gegner)
    die Rohstaerke des Modells ist also att_wahr * sos - und sos ist der Teiler.
    """

    def __init__(self):
        self.sp = []
        self.att = collections.defaultdict(lambda: 1.0)
        self.dfn = collections.defaultdict(lambda: 1.0)
        self.attx = collections.defaultdict(lambda: 1.0)
        self.dfnx = collections.defaultdict(lambda: 1.0)

    def add(self, m):
        self.sp.append((m['h'], m['a'], m['hg'], m['ag'], m['hx'], m['ax']))

    def loese(self):
        n = len(self.sp)
        if n < 8:
            return
        Lh = sum(s[2] for s in self.sp) / n; La = sum(s[3] for s in self.sp) / n
        Lxh = sum(s[4] for s in self.sp) / n; Lxa = sum(s[5] for s in self.sp) / n
        for att, dfn, bh, ba, ih, ia in ((self.att, self.dfn, Lh, La, 2, 3),
                                         (self.attx, self.dfnx, Lxh, Lxa, 4, 5)):
            if bh <= 0 or ba <= 0:
                continue
            for _ in range(SOS_ITER):
                zf = collections.defaultdict(float); nf = collections.defaultdict(float)
                zg = collections.defaultdict(float); ng = collections.defaultdict(float)
                for s in self.sp:
                    h, a = s[0], s[1]
                    zf[h] += s[ih]; nf[h] += bh * dfn[a]
                    zf[a] += s[ia]; nf[a] += ba * dfn[h]
                    zg[h] += s[ia]; ng[h] += ba * att[a]
                    zg[a] += s[ih]; ng[a] += bh * att[h]
                for d, z, nn in ((att, zf, nf), (dfn, zg, ng)):
                    for t in list(nn):
                        if nn[t] > 1e-9:
                            d[t] = max(0.05, min(5.0, z[t] / nn[t]))
                    mu = st.fmean(d.values())
                    if mu > 1e-9:
                        for t in d:
                            d[t] /= mu


def zutaten(sid, daten):
    """Je bewertbares Spiel alle Zutaten - Rohmittel, Gegnerstaerke, PPG, Markt-Lambda."""
    sp = spiele(sid, daten)
    flags = liga_flags(sp)
    heim = collections.defaultdict(list); ausw = collections.defaultdict(list)
    chrono = collections.defaultdict(list)
    g_heim = collections.defaultdict(list); g_ausw = collections.defaultdict(list)
    n_sp = collections.defaultdict(int); pkt = collections.defaultdict(int)
    letzte = {}; zeiten = collections.defaultdict(list)
    lh = []; la = []; lxh = []; lxa = []
    fit = Fit()
    out = []
    for m in sp:
        n_h, n_a = n_sp[m['h']], n_sp[m['a']]
        if n_h >= MIN_VOR and n_a >= MIN_VOR and lh:
            fit.loese()

            def team(tid, seite):
                sv = heim[tid] if seite == 'home' else ausw[tid]
                ov = heim[tid] + ausw[tid]
                gv = g_heim[tid] if seite == 'home' else g_ausw[tid]
                go = g_heim[tid] + g_ausw[tid]
                d = dict(n_v=len(sv), n_o=len(ov),
                         ppg=pkt[tid] / n_sp[tid],
                         ruhe=(m['t'] - letzte[tid]) / TAG if tid in letzte else None,
                         dichte14=sum(1 for x in zeiten[tid] if m['t'] - x <= 14 * TAG),
                         serie3=sum(chrono[tid][-3:][i][4] for i in range(min(3, len(chrono[tid])))))
                for nm, v in (('v', sv), ('o', ov)):
                    for i, k in enumerate(('tf', 'xf', 'tg', 'xg')):
                        d[f'{nm}_{k}'] = _m([e[i] for e in v])
                for w in FORM_FENSTER:
                    f = chrono[tid][-w:]
                    d[f'f{w}_n'] = len(f)
                    for i, k in enumerate(('tf', 'xf', 'tg', 'xg')):
                        d[f'f{w}_{k}'] = _m([e[i] for e in f])
                for nm, gg in (('v', gv), ('o', go)):
                    d[f'sos_{nm}_att'] = _m([fit.dfn[x] for x in gg]) or 1.0
                    d[f'sos_{nm}_dfn'] = _m([fit.att[x] for x in gg]) or 1.0
                    d[f'sosx_{nm}_att'] = _m([fit.dfnx[x] for x in gg]) or 1.0
                    d[f'sosx_{nm}_dfn'] = _m([fit.attx[x] for x in gg]) or 1.0
                for w in FORM_FENSTER:
                    f = go[-w:]
                    d[f'sos_f{w}_att'] = _m([fit.dfn[x] for x in f]) or 1.0
                    d[f'sos_f{w}_dfn'] = _m([fit.att[x] for x in f]) or 1.0
                    d[f'sosx_f{w}_att'] = _m([fit.dfnx[x] for x in f]) or 1.0
                    d[f'sosx_f{w}_dfn'] = _m([fit.attx[x] for x in f]) or 1.0
                return d

            mlh = mla = None
            if m['q'] is not None:
                try:
                    (a_, b_), _ = M.market_lambdas(m['q'])
                    mlh, mla = float(a_), float(b_)
                except Exception:
                    pass
            out.append(dict(sid=sid, hg=m['hg'], ag=m['ag'], mlh=mlh, mla=mla, **flags,
                            L=dict(h=_m(lh), a=_m(la), xh=_m(lxh), xa=_m(lxa)),
                            H=team(m['h'], 'home'), A=team(m['a'], 'away')))
        for tid, seite, g, gg, gx, gxx in ((m['h'], 'h', m['hg'], m['ag'], m['hx'], m['ax']),
                                           (m['a'], 'a', m['ag'], m['hg'], m['ax'], m['hx'])):
            erg = 1 if g > gg else (0 if g == gg else -1)
            (heim if seite == 'h' else ausw)[tid].append((g, gx, gg, gxx))
            chrono[tid].append((g, gx, gg, gxx, erg))
            (g_heim if seite == 'h' else g_ausw)[tid].append(m['a'] if seite == 'h' else m['h'])
            n_sp[tid] += 1
            pkt[tid] += 3 if erg > 0 else (1 if erg == 0 else 0)
            letzte[tid] = m['t']; zeiten[tid].append(m['t'])
        lh.append(m['hg']); la.append(m['ag']); lxh.append(m['hx']); lxa.append(m['ax'])
        fit.add(m)
    return out


def laden(args):
    pfad = os.path.join(args.daten, 'pruefung_zutaten.pkl')
    sids = args.ligen or saisons(args.daten)
    if not sids:
        sys.exit("Keine league-matches im Zwischenspeicher. Erst rueckschau.py --ligen ... laufen lassen.")
    schluessel = tuple(sids) + (MIN_VOR, SOS_ITER, 'v1')
    if os.path.exists(pfad) and not args.neu:
        g = pickle.load(open(pfad, 'rb'))
        if g.get('schluessel') == schluessel:
            return g['zutaten']
    alle = []
    for sid in sids:
        try:
            z = zutaten(sid, args.daten)
        except Exception as e:
            print(f"  Saison {sid}: uebersprungen ({type(e).__name__}: {e})")
            continue
        print(f"  Saison {sid}: {len(z):5d} bewertbare Spiele", flush=True)
        alle += z
    pickle.dump(dict(schluessel=schluessel, zutaten=alle), open(pfad, 'wb'))
    return alle


# ------------------------------------------------------------------ Rechnung

def lambdas(z, c):
    """Erwartete Tore. Spiegelt modell.py, plus die vier Zusatz-Anteile aus STD."""
    L = z['L']; Lh, La, Lxh, Lxa = L['h'], L['a'], L['xh'], L['xa']
    xg_ok = z.get('xg_ok', True); basis_ok = z.get('basis_ok', True)
    if min(Lh, La) <= 0 or (xg_ok and min(Lxh, Lxa) <= 0):
        return None
    c = dict(c)
    if not xg_ok:
        c['XG'] = 0.0
    Lg_o = (Lh + La) / 2
    Lx_o = (Lxh + Lxa) / 2 if min(Lxh, Lxa) > 0 else 1.0
    G = c['GEGNER']

    def term(tore, x, Lx, Lg):
        if tore is None:
            return None
        if not c['XG'] or ((x or 0) == 0 and tore > 0):
            return tore / Lg          # nicht durch ein Liga-xG von 0 teilen
        return c['XG'] * x / Lx + (1 - c['XG']) * tore / Lg

    def korr(wert, d, nm, art):
        if not G or wert is None:
            return wert
        s = c['XG'] * d[f'sosx_{nm}_{art}'] + (1 - c['XG']) * d[f'sos_{nm}_{art}']
        return wert / (s ** G) if s > 1e-6 else wert

    def staerke(d, seite):
        Lg_v, Lx_v = (Lh, Lxh) if seite == 'home' else (La, Lxa)
        Lg_g, Lx_g = (La, Lxa) if seite == 'home' else (Lh, Lxh)
        Lx_v = Lx_v or 1.0; Lx_g = Lx_g or 1.0
        att_o = korr(term(d['o_tf'], d['o_xf'], Lx_o, Lg_o), d, 'o', 'att')
        dfn_o = korr(term(d['o_tg'], d['o_xg'], Lx_o, Lg_o), d, 'o', 'dfn')
        if att_o is None:
            return None
        if d['n_v']:
            att_v = korr(term(d['v_tf'], d['v_xf'], Lx_v, Lg_v), d, 'v', 'att')
            dfn_v = korr(term(d['v_tg'], d['v_xg'], Lx_g, Lg_g), d, 'v', 'dfn')
        else:
            att_v, dfn_v = att_o, dfn_o
        wv = d['n_v'] / (d['n_v'] + c['SEITE_K'])
        att = M.shrink(wv * att_v + (1 - wv) * att_o, d['n_o'], c['DAEMP_K'])
        dfn = M.shrink(wv * dfn_v + (1 - wv) * dfn_o, d['n_o'], c['DAEMP_K'])
        w = int(c['FORM_W']); n = d[f'f{w}_n']
        if n and c['FORM'] > 0:
            af = term(d[f'f{w}_tf'], d[f'f{w}_xf'], Lx_o, Lg_o)
            df = term(d[f'f{w}_tg'], d[f'f{w}_xg'], Lx_o, Lg_o)
            if af is not None and G:
                sa = c['XG'] * d[f'sosx_f{w}_att'] + (1 - c['XG']) * d[f'sos_f{w}_att']
                sd = c['XG'] * d[f'sosx_f{w}_dfn'] + (1 - c['XG']) * d[f'sos_f{w}_dfn']
                if sa > 1e-6: af /= sa ** G
                if sd > 1e-6: df /= sd ** G
            if af is not None:
                att = (1 - c['FORM']) * att + c['FORM'] * M.shrink(af, n, c['FORM_K'])
                dfn = (1 - c['FORM']) * dfn + c['FORM'] * M.shrink(df, n, c['FORM_K'])
        return att, dfn

    h = staerke(z['H'], 'home'); a = staerke(z['A'], 'away')
    if not h or not a:
        return None
    b = c['BASIS'] if basis_ok else 0.0
    bh = (1 - b) * Lh + b * Lxh; ba = (1 - b) * La + b * Lxa
    lh = bh * h[0] * a[1]; la = ba * a[0] * h[1]
    lh = bh + c['LAM_D'] * (lh - bh); la = ba + c['LAM_D'] * (la - ba)
    # Summe und Differenz getrennt behandeln: gemessen ist die Summe zu weit gespreizt
    # (Steigung 0,79), die Differenz nicht (1,10). Eine gemeinsame Daempfung traf beides.
    S, D, Sb = lh + la, lh - la, bh + ba
    S = Sb + c['SUM_D'] * (S - Sb)
    D = D + c['PPG'] * (z['H']['ppg'] - z['A']['ppg'])
    lh, la = max(0.05, (S + D) / 2), max(0.05, (S - D) / 2)
    w = c['MARKT']
    if w and z.get('mlh') is not None:
        lh = (1 - w) * lh + w * z['mlh']; la = (1 - w) * la + w * z['mla']
    return lh, la


def bewerte(menge, c, gleichstand=True):
    alt = R.lambdas; R.lambdas = lambdas
    try:
        return R.bewerte(menge, c, gleichstand)
    finally:
        R.lambdas = alt


def fuenf(lh, la, rho):
    X = M.matrix(lh, la, rho)
    p = dict(H=float(X[_MH].sum()), A=float(X[_MA].sum()),
             O25=float(X[_MO].sum()), BTTS=float(X[_MB].sum()))
    p['U25'] = 1 - p['O25']
    return p


# ------------------------------------------------------------------ Durchlaeufe

def durchlauf(menge, name, werte, label='ALLE'):
    """Scannt einen Anteil und gibt die beste Stufe zurueck."""
    res = {v: bewerte(menge, {**STD, name: v}) for v in werte}
    basis = res[werte[0]]
    best = max(werte, key=lambda v: res[v]['llm'])
    print(f"\n--- {label}: {basis['n']} Spiele, {len({x['sid'] for x in menge})} Ligen")
    print(f"{name:>8s} {'LogLik':>10s} {'Quote':>7s} {'Brier':>9s} "
          f"{'Treffer':>8s} {'erwartet':>9s} {'t vs Basis':>11s}")
    for v in werte:
        r = res[v]; _, t = R.paarweise(r['ll'], basis['ll'])
        print(f"{v:8.2f} {r['llm']:10.5f} {r['quote']*100:6.1f}% {r['brier']:9.5f} "
              f"{r['tref']:8d} {r['erw']:9.1f} {t:>+11.2f}"
              + ('  <==' if v == best else ''))
    return best


def mit_haelften(menge, name, werte):
    g = durchlauf(menge, name, werte, 'ALLE')
    A, B = R.haelften(menge)
    ba = durchlauf(A, name, werte, 'Haelfte A')
    bb = durchlauf(B, name, werte, 'Haelfte B')
    print(f"\n  Beste gesamt {g} | A {ba} | B {bb}  ->  "
          f"{'EINIG' if ba == bb else 'UNEINIG'}")
    if ba != bb:
        print("  UNEINIG heisst laut CLAUDE.md: Anpassung an Rauschen, Konstante bleibt.")
    print("\n  Liga-Abzaehlung (gegen die Basis), damit nicht eine Liga den Gewinn traegt:")
    for v in werte[1:]:
        bei = []
        for sid in sorted({x['sid'] for x in menge}):
            m = [x for x in menge if x['sid'] == sid]
            if len(m) < 20:
                continue
            s, _ = R.paarweise(bewerte(m, {**STD, name: v})['ll'], bewerte(m, STD)['ll'])
            bei.append((s, sid))
        bei.sort(reverse=True)
        ges = sum(x[0] for x in bei)
        pos = sum(1 for s, _ in bei if s > 0)
        anteil = bei[0][0] / ges * 100 if ges else 0
        print(f"    {name} {v:5.2f}: {pos} von {len(bei)} Ligen besser, groesste Liga "
              f"{bei[0][1]} mit {bei[0][0]:+.2f} ({anteil:.0f} % des Gewinns)")


def residuen(menge):
    """Woran haengt der Modellfehler? Korrelationen und Regressionen."""
    rows = []
    for z in menge:
        r = lambdas(z, STD)
        if not r:
            continue
        H, A = z['H'], z['A']
        rows.append(dict(sid=z['sid'], lh=r[0], la=r[1], hg=z['hg'], ag=z['ag'],
                         rest_h=z['hg']-r[0], rest_a=z['ag']-r[1],
                         rest_sum=(z['hg']+z['ag'])-(r[0]+r[1]),
                         rest_diff=(z['hg']-z['ag'])-(r[0]-r[1]),
                         ruhe_h=H['ruhe'], ruhe_a=A['ruhe'],
                         d14=H['dichte14']-A['dichte14'],
                         ppg_d=H['ppg']-A['ppg'], ppg_s=H['ppg']+A['ppg'],
                         serie_d=H['serie3']-A['serie3'], n=min(H['n_o'], A['n_o'])))
    print(f"\n=== Residualanalyse ueber {len(rows)} Spiele aus "
          f"{len({r['sid'] for r in rows})} Ligen ===\n")
    print(f"  Mittlerer Rest: Heim {st.fmean(r['rest_h'] for r in rows):+.4f}, "
          f"Ausw {st.fmean(r['rest_a'] for r in rows):+.4f}, "
          f"Summe {st.fmean(r['rest_sum'] for r in rows):+.4f}\n")

    def korr(xs, ys):
        p = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
        n = len(p)
        if n < 30:
            return None, None, n
        mx = st.fmean(a for a, _ in p); my = st.fmean(b for _, b in p)
        sx = st.stdev(a for a, _ in p); sy = st.stdev(b for _, b in p)
        if sx < 1e-9 or sy < 1e-9:
            return None, None, n
        rr = sum((a-mx)*(b-my) for a, b in p)/((n-1)*sx*sy)
        return rr, rr*math.sqrt((n-2)/max(1e-12, 1-rr*rr)), n

    KAND = [('Ruhetage Heim', 'ruhe_h', 'rest_h'), ('Ruhetage Ausw', 'ruhe_a', 'rest_a'),
            ('Dichteunterschied 14 T', 'd14', 'rest_diff'),
            ('PPG-Abstand', 'ppg_d', 'rest_diff'), ('PPG-Summe', 'ppg_s', 'rest_sum'),
            ('Serienabstand (3)', 'serie_d', 'rest_diff'),
            ('Vorspiele', 'n', 'rest_sum')]
    print(f"{'Groesse':26s} {'Ziel':11s} {'n':>5s} {'r':>8s} {'t':>7s}")
    print('-' * 62)
    for name, k, ziel in KAND:
        rr, tt, n = korr([r[k] for r in rows], [r[ziel] for r in rows])
        if rr is None:
            print(f"{name:26s} {ziel:11s} {n:>5d} {'-':>8s} {'-':>7s}")
        else:
            print(f"{name:26s} {ziel:11s} {n:>5d} {rr:>+8.4f} {tt:>+7.2f}"
                  + ('  **' if abs(tt) >= 2.5 else ''))

    def regress(xs, ys, name):
        p = list(zip(xs, ys)); n = len(p)
        mx = st.fmean(a for a, _ in p); my = st.fmean(b for _, b in p)
        sxx = sum((a-mx)**2 for a, _ in p)
        b1 = sum((a-mx)*(b-my) for a, b in p)/sxx
        res = [b - (my + b1*(a-mx)) for a, b in p]
        se = math.sqrt(sum(v*v for v in res)/(n-2)/sxx)
        print(f"  {name:36s} Steigung {b1:6.3f}   t gegen 1 {(b1-1)/se:+6.2f}")

    print("\n  Echte Werte auf die Modellwerte regressiert. Steigung unter 1 heisst:")
    print("  das Modell spreizt zu weit; ueber 1 heisst: zu wenig.")
    regress([r['lh']+r['la'] for r in rows], [r['hg']+r['ag'] for r in rows], 'Gesamttore')
    regress([r['lh']-r['la'] for r in rows], [r['hg']-r['ag'] for r in rows], 'Tordifferenz')
    regress([r['lh'] for r in rows], [r['hg'] for r in rows], 'Heimtore')
    regress([r['la'] for r in rows], [r['ag'] for r in rows], 'Auswaertstore')


def widerspruch(menge):
    """Modell gegen Markt: wenn beide sich widersprechen, wer hat recht?"""
    rows = []
    for z in menge:
        if z.get('mlh') is None:
            continue
        r = lambdas(z, STD)
        if not r:
            continue
        pmod = fuenf(r[0], r[1], STD['RHO'])
        pmk = fuenf(z['mlh'], z['mla'], STD['RHO'])
        t, pt, _, _ = M.bester_tipp(pmod, r[0], r[1])
        rows.append(dict(tipp=t, p_mod=pmod[t], p_markt=pmk[t],
                         ab=(pmod[t]-pmk[t])*100,
                         ein=R.getroffen(t, z['hg'], z['ag'])))
    print(f"\n=== {len(rows)} Spiele mit Tipp und Marktpreis ===\n")
    print("Gruppiert nach Abstand zum Markt beim getippten Ausgang.\n")
    print(f"{'Abstand':>16s} {'n':>5s} {'Modell':>8s} {'Markt':>8s} {'echt':>8s} "
          f"{'Fehler Mod':>11s} {'Fehler Mkt':>11s}")
    print('-' * 72)
    for lo, hi in [(-99, -8), (-8, -4), (-4, 0), (0, 4), (4, 8), (8, 99)]:
        g = [r for r in rows if lo <= r['ab'] < hi]
        if len(g) < 25:
            continue
        pm = st.fmean(r['p_mod'] for r in g)*100
        pk = st.fmean(r['p_markt'] for r in g)*100
        ec = st.fmean(r['ein'] for r in g)*100
        print(f"{lo:>+7d} bis {hi:>+5d} {len(g):>5d} {pm:>7.1f}% {pk:>7.1f}% {ec:>7.1f}% "
              f"{pm-ec:>+11.1f} {pk-ec:>+11.1f}")
    pm = st.fmean(r['p_mod'] for r in rows)*100
    pk = st.fmean(r['p_markt'] for r in rows)*100
    ec = st.fmean(r['ein'] for r in rows)*100
    print('-' * 72)
    print(f"{'alle':>16s} {len(rows):>5d} {pm:>7.1f}% {pk:>7.1f}% {ec:>7.1f}% "
          f"{pm-ec:>+11.1f} {pk-ec:>+11.1f}")
    bm = st.fmean((r['p_mod']-r['ein'])**2 for r in rows)
    bk = st.fmean((r['p_markt']-r['ein'])**2 for r in rows)
    d = [(r['p_mod']-r['ein'])**2 - (r['p_markt']-r['ein'])**2 for r in rows]
    tt = st.fmean(d)/(st.stdev(d)/math.sqrt(len(d)))
    print(f"\nBrier auf der getippten Wette: Modell {bm:.5f}, Markt {bk:.5f} "
          f"(t = {tt:+.2f}; positiv = Modell schlechter)")
    print("\nNur Spiele, in denen das Modell optimistischer ist als der Markt:")
    for grenze in (4, 6, 8, 10, 12):
        g = [r for r in rows if r['ab'] >= grenze]
        if len(g) < 25:
            continue
        pm = st.fmean(r['p_mod'] for r in g)*100
        pk = st.fmean(r['p_markt'] for r in g)*100
        ec = st.fmean(r['ein'] for r in g)*100
        sd = math.sqrt(sum(r['p_markt']*(1-r['p_markt']) for r in g))/len(g)*100
        print(f"  Abstand >= {grenze:2d} Pkt: {len(g):4d} Spiele, Modell {pm:5.1f} %, "
              f"Markt {pk:5.1f} %, echt {ec:5.1f} %  (z gegen Markt {(ec-pk)/sd:+.2f})")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--daten', default=os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'daten'))
    ap.add_argument('--ligen', type=int, nargs='*', default=None)
    ap.add_argument('--neu', action='store_true', help='Zutaten neu berechnen')
    ap.add_argument('--gegner', action='store_true', help='Gegnerstaerke scannen')
    ap.add_argument('--ppg', action='store_true', help='Punkte-pro-Spiel-Term scannen')
    ap.add_argument('--summe', action='store_true', help='Daempfung nur auf die Summe')
    ap.add_argument('--markt', action='store_true', help='MARKT_ANTEIL scannen')
    ap.add_argument('--residuen', action='store_true', help='Residualanalyse')
    ap.add_argument('--widerspruch', action='store_true', help='Modell gegen Markt')
    args = ap.parse_args()
    Z = laden(args)
    print(f"\n{len(Z)} bewertbare Spiele aus {len({z['sid'] for z in Z})} Ligen, "
          f"{sum(1 for z in Z if z['mlh'] is not None)} davon mit Vorab-Quoten.")
    getan = False
    if args.gegner:
        mit_haelften(Z, 'GEGNER', [0.0, 0.25, 0.5, 0.75, 1.0]); getan = True
    if args.ppg:
        mit_haelften(Z, 'PPG', [0.0, 0.05, 0.10, 0.15, 0.20, 0.30]); getan = True
    if args.summe:
        mit_haelften(Z, 'SUM_D', [1.0, 0.95, 0.90, 0.85, 0.80]); getan = True
    if args.markt:
        # Nur Spiele mit Quoten, sonst vergleicht man zwei verschiedene Mengen
        mit_haelften([z for z in Z if z['mlh'] is not None], 'MARKT',
                     [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]); getan = True
    if args.residuen:
        residuen(Z); getan = True
    if args.widerspruch:
        widerspruch(Z); getan = True
    if not getan:
        ap.print_help()


if __name__ == '__main__':
    main()
