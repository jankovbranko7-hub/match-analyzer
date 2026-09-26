"""Match-Analyzer: Prognose für einzelne Spiele aus FootyStats-Daten.

Aufruf:
    python3 analyse/modell.py --liste 2026-09-26          # Spiele eines Tages mit ID anzeigen
    python3 analyse/modell.py 8548331 8548255 8408933     # diese Spiele berechnen

Optionen:
    --markt 0.3   Anteil der margenbereinigten Vorab-Quoten an den erwarteten Toren
                  (Standard 0 = reines Datenmodell, laut CLAUDE.md kein Markt-Mix)
    --neu         API-Daten neu laden statt zwischengespeicherte Dateien zu nutzen
    --daten DIR   Ordner für die API-Antworten (Standard: analyse/daten, nicht im Git)

Der API-Key wird aus FOOTYSTATS_API_KEY gelesen (ersatzweise APIKEY) und nie ausgegeben.
"""
import argparse, json, math, os, sys, time, urllib.parse, urllib.request
import numpy as np
from scipy.optimize import minimize

BASE = "https://api.football-data-api.com"

# ---------------------------------------------------------------- API-Zugriff

def api_key():
    key = os.environ.get("FOOTYSTATS_API_KEY") or os.environ.get("APIKEY")
    if not key:
        sys.exit("FOOTYSTATS_API_KEY fehlt: in den Umgebungseinstellungen hinterlegen "
                 "(Titelleiste → Cloud-Umgebung → Edit) und eine neue Session starten.")
    return key

def hole(endpoint, params, datei, args):
    """Holt eine API-Antwort und speichert sie; vorhandene Dateien werden wiederverwendet."""
    pfad = os.path.join(args.daten, datei)
    if os.path.exists(pfad) and not args.neu:
        return json.load(open(pfad))
    url = f"{BASE}/{endpoint}?" + urllib.parse.urlencode({**params, "key": api_key()})
    with urllib.request.urlopen(url, timeout=60) as r:
        daten = json.load(r)
    if not daten.get("success", True):
        sys.exit(f"API-Fehler bei {endpoint}: {daten.get('message')}")
    os.makedirs(args.daten, exist_ok=True)
    json.dump(daten, open(pfad, "w"))
    return daten

# ---------------------------------------------------------------- Modell

def pois(l, n=11): return np.array([math.exp(-l)*l**k/math.factorial(k) for k in range(n)])

def matrix(lh, la, rho=-0.07):
    """Ergebnis-Matrix 0:0 bis 10:10 (Poisson mit Dixon-Coles-Korrektur)."""
    M=np.outer(pois(lh),pois(la))
    M[0,0]*=1-lh*la*rho; M[0,1]*=1+lh*rho; M[1,0]*=1+la*rho; M[1,1]*=1-rho
    return M/M.sum()

def probs(M):
    i,j=np.indices(M.shape)
    return dict(H=M[i>j].sum(),D=M[i==j].sum(),A=M[i<j].sum(),O25=M[i+j>=3].sum(),U25=M[i+j<=2].sum(),BTTS=M[(i>0)&(j>0)].sum())

def shrink(x,n,k=5):
    """Zieht Werte aus kleinen Stichproben Richtung Liga-Durchschnitt (1,0)."""
    return (n*x+k*1.0)/(n+k)

def strengths(t, side, L, last6):
    """Angriffs- und Abwehrstärke relativ zum Liga-Durchschnitt (70 % xG, 30 % Tore)."""
    s=t['stats']; n_v=s[f'seasonMatchesPlayed_{side}']; n_o=s['seasonMatchesPlayed_overall']
    Lg_v = L[side]; Lx_v = L['x'+side]; Lg_o=(L['home']+L['away'])/2; Lx_o=(L['xhome']+L['xaway'])/2
    opp = 'away' if side=='home' else 'home'
    # Heim- bzw. Auswärtswerte und Gesamtwerte
    att_v = 0.7*s[f'xg_for_avg_{side}']/Lx_v + 0.3*s[f'seasonScoredAVG_{side}']/Lg_v
    att_o = 0.7*s['xg_for_avg_overall']/Lx_o + 0.3*s['seasonScoredAVG_overall']/Lg_o
    dfn_v = 0.7*s[f'xg_against_avg_{side}']/L['x'+opp] + 0.3*s[f'seasonConcededAVG_{side}']/L[opp]
    dfn_o = 0.7*s['xg_against_avg_overall']/Lx_o + 0.3*s['seasonConcededAVG_overall']/Lg_o
    wv = n_v/(n_v+6)
    att = shrink(wv*att_v+(1-wv)*att_o, n_o); dfn = shrink(wv*dfn_v+(1-wv)*dfn_o, n_o)
    # Form der letzten 6 Spiele mit 25 %
    f=last6['stats']
    att_f = 0.7*f['xg_for_avg_overall']/Lx_o + 0.3*f['seasonScoredAVG_overall']/Lg_o
    dfn_f = 0.7*f['xg_against_avg_overall']/Lx_o + 0.3*f['seasonConcededAVG_overall']/Lg_o
    att = 0.75*att + 0.25*shrink(att_f,6,3); dfn = 0.75*dfn + 0.25*shrink(dfn_f,6,3)
    return att, dfn

def market_lambdas(m):
    """Erwartete Tore, die zu den margenbereinigten Vorab-Quoten passen."""
    o=[m['odds_ft_1'],m['odds_ft_x'],m['odds_ft_2']]; ip=np.array([1/x for x in o]); ip/=ip.sum()
    ou=np.array([1/m['odds_ft_over25'],1/m['odds_ft_under25']]); ou/=ou.sum()
    bt=np.array([1/m['odds_btts_yes'],1/m['odds_btts_no']]); bt/=bt.sum()
    def loss(v):
        p=probs(matrix(*np.exp(v)))
        return (p['H']-ip[0])**2+(p['D']-ip[1])**2+(p['A']-ip[2])**2+(p['O25']-ou[0])**2+0.5*(p['BTTS']-bt[0])**2
    r=minimize(loss,[0.3,0.2],method='Nelder-Mead')
    return np.exp(r.x), dict(H=ip[0],D=ip[1],A=ip[2],O25=ou[0],BTTS=bt[0])

def quoten_da(m):
    return all(m.get(k, 0) and m[k] > 1 for k in
               ['odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over25','odds_ft_under25','odds_btts_yes','odds_btts_no'])

def league(T):
    def avg(k,w): return sum(t['stats'][k]*t['stats'][w] for t in T)/sum(t['stats'][w] for t in T)
    return dict(home=avg('seasonScoredAVG_home','seasonMatchesPlayed_home'),away=avg('seasonScoredAVG_away','seasonMatchesPlayed_away'),
                xhome=avg('xg_for_avg_home','seasonMatchesPlayed_home'),xaway=avg('xg_for_avg_away','seasonMatchesPlayed_away'))

def h2h_gewicht(m, jahre=3):
    """Direkte Duelle zählen 10 %, aber nur wenn das letzte Duell höchstens 3 Jahre zurückliegt."""
    spiele = m.get('h2h', {}).get('previous_matches_ids') or []
    if not spiele: return 0.0
    letztes = max(s['date_unix'] for s in spiele)
    return 0.10 if m['date_unix'] - letztes <= jahre*365*86400 else 0.0

# ---------------------------------------------------------------- Ablauf

def analysiere(mid, args):
    m = hole("match", {"match_id": mid}, f"match_{mid}.json", args)['data']
    sid = m['competition_id']
    T = hole("league-teams", {"season_id": sid, "include": "stats"}, f"teams_{sid}.json", args)['data']
    L = league(T); T = {t['id']: t for t in T}
    def last6(tid):
        d = hole("lastx", {"team_id": tid}, f"lastx_{tid}.json", args)['data']
        return [e for e in d if e['last_x_match_num']==6][0]

    ah,dh=strengths(T[m['homeID']],'home',L,last6(m['homeID']))
    aa,da=strengths(T[m['awayID']],'away',L,last6(m['awayID']))
    base_h=0.6*L['home']+0.4*L['xhome']; base_a=0.6*L['away']+0.4*L['xaway']
    lh=base_h*ah*da; la=base_a*aa*dh
    h2h_w = h2h_gewicht(m)
    if h2h_w:
        tot=lh+la; f=(1-h2h_w)+h2h_w*m['h2h']['betting_stats']['avg_goals']/tot; lh*=f; la*=f

    mk = None
    if quoten_da(m):
        (mlh,mla),mk=market_lambdas(m)
    w = args.markt if mk else 0.0
    flh=(1-w)*lh+w*(mlh if mk else 0); fla=(1-w)*la+w*(mla if mk else 0)
    M=matrix(flh,fla); p=probs(M)
    idx=np.dstack(np.unravel_index(np.argsort(-M.ravel()),M.shape))[0][:3]

    pct = lambda d: {k: round(float(v)*100,1) for k,v in d.items()}
    print('='*70); print(m['home_name'],'-',m['away_name'], f"(Spiel {mid}, Saison {sid})")
    print(f" Liga-Schnitt: Heim {L['home']:.2f} Tore / {L['xhome']:.2f} xG, Auswärts {L['away']:.2f} Tore / {L['xaway']:.2f} xG")
    print(f' Stärken: Heim Att {ah:.2f} Def {dh:.2f} | Ausw Att {aa:.2f} Def {da:.2f}')
    print(f' H2H-Gewicht: {h2h_w:.0%}')
    if mk:
        print(f' λ Modell {lh:.2f}-{la:.2f} | λ Markt {mlh:.2f}-{mla:.2f} | Markt-Anteil {w:.0%} | final {flh:.2f}-{fla:.2f}')
        print(' Markt (ohne Marge):', pct(mk))
    else:
        print(f' λ Modell {lh:.2f}-{la:.2f} (keine vollständigen Vorab-Quoten)')
    print(' FINAL:', pct(p))
    print(' Top3:',[(f'{a}:{b}',round(float(M[a,b])*100,1)) for a,b in idx])
    print(' Faire Quoten:',{k:round(1/float(v),2) for k,v in p.items()})
    if mk:
        print(' FootyStats-Quoten: 1',m['odds_ft_1'],'X',m['odds_ft_x'],'2',m['odds_ft_2'],
              'O2.5',m['odds_ft_over25'],'U2.5',m['odds_ft_under25'],'BTTS',m['odds_btts_yes'])

def liste(datum, args):
    d = hole("todays-matches", {"date": datum}, f"tag_{datum}.json", args)['data']
    for m in d:
        print(m['id'], m['competition_id'], time.strftime('%H:%M UTC', time.gmtime(m['date_unix'])),
              m['home_name'], '-', m['away_name'])

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Spielprognose aus FootyStats-Daten")
    ap.add_argument("spiele", nargs="*", type=int, help="FootyStats match_id(s)")
    ap.add_argument("--liste", metavar="DATUM", help="Spiele eines Tages (YYYY-MM-DD) anzeigen")
    ap.add_argument("--markt", type=float, default=0.0, help="Anteil Vorab-Quoten (0 bis 1, Standard 0)")
    ap.add_argument("--neu", action="store_true", help="API-Daten neu laden")
    ap.add_argument("--daten", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "daten"))
    args = ap.parse_args()
    if args.liste: liste(args.liste, args)
    for mid in args.spiele: analysiere(mid, args)
    if not args.liste and not args.spiele: ap.print_help()
