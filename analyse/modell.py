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
    """Holt eine API-Antwort und speichert sie.

    Zwischengespeicherte Dateien werden bis CACHE_STUNDEN wiederverwendet, danach neu geladen.
    """
    pfad = os.path.join(args.daten, datei)
    if os.path.exists(pfad) and not args.neu:
        alter_h = (time.time() - os.path.getmtime(pfad)) / 3600
        if alter_h < CACHE_STUNDEN:
            return json.load(open(pfad))
        print(f"  (aktualisiere {datei}, war {alter_h:.1f} h alt)")
    url = f"{BASE}/{endpoint}?" + urllib.parse.urlencode({**params, "key": api_key()})
    with urllib.request.urlopen(url, timeout=60) as r:
        daten = json.load(r)
    if not daten.get("success", True):
        sys.exit(f"API-Fehler bei {endpoint}: {daten.get('message')}")
    os.makedirs(args.daten, exist_ok=True)
    json.dump(daten, open(pfad, "w"))
    return daten

# ---------------------------------------------------------------- Gewichte
#
# NACH ERFAHRUNG GESETZT, NICHT AN VERGANGENEN SPIELEN OPTIMIERT.
# So gewollt. Die Werte bleiben fest, damit jede Analyse vergleichbar ist und
# nicht jede Session anders rechnet.
#
# NUR ÄNDERN, WENN DER NUTZER ES AUSDRÜCKLICH VERLANGT.
# Dann hier ändern, die Begründung danebenschreiben und im README nachziehen.
# Nicht "weil es für dieses eine Spiel besser passt" – das ist Ergebnis-Anpassung
# im Nachhinein und macht alle früheren Prognosen unvergleichbar.

XG_ANTEIL           = 0.70   # xG gegen echte Tore bei der Teamstärke.
                             # xG ist stabiler: Tore schwanken bei 5-10 Spielen stark.
LIGA_BASIS_XG       = 0.40   # Liga-Basis: 60 % echte Tore, 40 % Liga-xG.
                             # Tore zählen hier mehr, weil der Liga-Schnitt über
                             # hunderte Spiele läuft und dadurch schon stabil ist.
SEITE_K             = 6      # Heim-/Auswärtswerte gegen Gesamtwerte: n / (n + 6).
                             # Bei 6 Heimspielen zählt die Heimbilanz zur Hälfte.
DAEMPFUNG_K         = 5      # Saisonstärke Richtung 1,00 ziehen, Wirkung wie
                             # 5 zusätzliche Spiele auf Liga-Niveau. Fängt
                             # Ausreißer am Saisonstart ab.
FORM_ANTEIL         = 0.25   # Form der letzten 6 Spiele. Genug für eine echte
                             # Formkurve, zu wenig, damit eine Glückssträhne
                             # durchschlägt.
FORM_DAEMPFUNG_K    = 3      # Form stärker dämpfen: nur 6 Spiele Grundlage.
H2H_ANTEIL          = 0.10   # Direkte Duelle auf die Gesamttore. Klein, weil
                             # Kader und Trainer wechseln.
H2H_MAX_JAHRE       = 3      # Duelle älter als 3 Jahre zählen gar nicht.
H2H_DAEMPFUNG_K     = 3      # Direkte Duelle daempfen: Gewicht = H2H_ANTEIL * n/(n+3), wobei n
                             # die Zahl der jungen Duelle ist. Ein einzelnes Duell zaehlt damit
                             # 2,5 %, sechs Duelle 6,7 %. Gleicher Wert wie FORM_DAEMPFUNG_K,
                             # dieselbe Ueberlegung - nicht an Ergebnissen angepasst.
DIXON_COLES_RHO     = -0.07  # Korrektur für 0:0/1:0/0:1/1:1. Übliche Größe aus der
                             # Literatur; reine Poisson unterschätzt enge Ergebnisse.
MARKT_ANTEIL        = 0.0    # Vorab-Quoten fließen standardmäßig NICHT ein
MIN_SAISONSPIELE    = 3      # Sperre: unter so vielen Saisonspielen eines Teams gibt das
CACHE_STUNDEN       = 6      # Zwischengespeicherte API-Antworten gelten so lange. Danach laedt
                             # das Skript neu. Schuetzt vor veralteten Quoten im Tagesverlauf und
                             # vor veralteter Teamstatistik am naechsten Tag. --neu erzwingt sofort.
                             # Modell KEINE Prognose aus. Darunter ersetzt die Daempfung die
                             # Teamstaerke praktisch komplett durch den Liga-Durchschnitt, und
                             # das Ergebnis ist fuer jedes Spiel fast dasselbe (Remis ~29 %).
                             # (Regel in CLAUDE.md). Über --markt zuschaltbar.

# ---------------------------------------------------------------- Modell

def pois(l, n=11): return np.array([math.exp(-l)*l**k/math.factorial(k) for k in range(n)])

def matrix(lh, la, rho=DIXON_COLES_RHO):
    """Ergebnis-Matrix 0:0 bis 10:10 (Poisson mit Dixon-Coles-Korrektur)."""
    M=np.outer(pois(lh),pois(la))
    M[0,0]*=1-lh*la*rho; M[0,1]*=1+lh*rho; M[1,0]*=1+la*rho; M[1,1]*=1-rho
    return M/M.sum()

def probs(M):
    i,j=np.indices(M.shape)
    return dict(H=M[i>j].sum(),D=M[i==j].sum(),A=M[i<j].sum(),O25=M[i+j>=3].sum(),U25=M[i+j<=2].sum(),BTTS=M[(i>0)&(j>0)].sum())

def shrink(x,n,k=DAEMPFUNG_K):
    """Zieht Werte aus kleinen Stichproben Richtung Liga-Durchschnitt (1,0)."""
    return (n*x+k*1.0)/(n+k)

def strengths(t, side, L, last6):
    """Angriffs- und Abwehrstärke relativ zum Liga-Durchschnitt (XG_ANTEIL xG, Rest Tore)."""
    s=t['stats']; n_v=s[f'seasonMatchesPlayed_{side}']; n_o=s['seasonMatchesPlayed_overall']
    Lg_v = L[side]; Lx_v = L['x'+side]; Lg_o=(L['home']+L['away'])/2; Lx_o=(L['xhome']+L['xaway'])/2
    opp = 'away' if side=='home' else 'home'
    x, g = XG_ANTEIL, 1-XG_ANTEIL
    # Heim- bzw. Auswärtswerte und Gesamtwerte
    att_v = x*s[f'xg_for_avg_{side}']/Lx_v + g*s[f'seasonScoredAVG_{side}']/Lg_v
    att_o = x*s['xg_for_avg_overall']/Lx_o + g*s['seasonScoredAVG_overall']/Lg_o
    dfn_v = x*s[f'xg_against_avg_{side}']/L['x'+opp] + g*s[f'seasonConcededAVG_{side}']/L[opp]
    dfn_o = x*s['xg_against_avg_overall']/Lx_o + g*s['seasonConcededAVG_overall']/Lg_o
    wv = n_v/(n_v+SEITE_K)
    att = shrink(wv*att_v+(1-wv)*att_o, n_o); dfn = shrink(wv*dfn_v+(1-wv)*dfn_o, n_o)
    # Form der letzten 6 Spiele
    f=last6['stats']
    att_f = x*f['xg_for_avg_overall']/Lx_o + g*f['seasonScoredAVG_overall']/Lg_o
    dfn_f = x*f['xg_against_avg_overall']/Lx_o + g*f['seasonConcededAVG_overall']/Lg_o
    fa = FORM_ANTEIL
    att = (1-fa)*att + fa*shrink(att_f,6,FORM_DAEMPFUNG_K)
    dfn = (1-fa)*dfn + fa*shrink(dfn_f,6,FORM_DAEMPFUNG_K)
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

def h2h_werte(m, jahre=H2H_MAX_JAHRE, k=H2H_DAEMPFUNG_K):
    """Gewicht und Tor-Schnitt der direkten Duelle, beides nur aus den jungen Duellen.

    Fehler bis 26.09.2026: Die Frische-Prüfung sah nur auf das jüngste Duell, der
    verwendete Tor-Schnitt (`betting_stats.avg_goals`) umfasste dagegen **alle** Duelle,
    teils zurück bis 2009. Bei Emmen – Oss flossen so 24 Duelle mit 3,46 Toren ein,
    während die sechs jungen bei 2,33 lagen. Der Schnitt wird deshalb hier selbst
    gerechnet, aus denselben Duellen, die auch die Frische-Prüfung bestehen.

    Zweiter Fehler: Das Gewicht war fest, egal ob ein Duell vorlag oder zwanzig.
    Jetzt wächst es mit der Zahl der jungen Duelle (n/(n+k)) – dieselbe Dämpfung,
    die das Modell schon bei Teamstärke und Form verwendet.
    """
    spiele = (m.get('h2h') or {}).get('previous_matches_ids') or []
    jung = [s for s in spiele if m['date_unix'] - s['date_unix'] <= jahre*365*86400]
    if not jung: return 0.0, None
    schnitt = sum(s['team_a_goals'] + s['team_b_goals'] for s in jung) / len(jung)
    return H2H_ANTEIL * len(jung) / (len(jung) + k), schnitt

# ---------------------------------------------------------------- Ablauf

def berechne(mid, args):
    """Rechnet ein Spiel durch und gibt alle Werte zurueck.

    Trennt die Rechnung von der Ausgabe, damit modell.py und bilanz.py garantiert
    dieselben Zahlen verwenden. Bei zu wenigen Saisonspielen gesperrt=True.
    """
    m = hole("match", {"match_id": mid}, f"match_{mid}.json", args)['data']
    sid = m['competition_id']
    T = hole("league-teams", {"season_id": sid, "include": "stats"}, f"teams_{sid}.json", args)['data']
    L = league(T); T = {t['id']: t for t in T}

    nh = T[m['homeID']]['stats']['seasonMatchesPlayed_overall']
    na = T[m['awayID']]['stats']['seasonMatchesPlayed_overall']
    if min(nh, na) < MIN_SAISONSPIELE and not args.trotzdem:
        return dict(gesperrt=True, match=m, sid=sid, nh=nh, na=na)

    def last6(tid):
        d = hole("lastx", {"team_id": tid}, f"lastx_{tid}.json", args)['data']
        return [e for e in d if e['last_x_match_num']==6][0]

    ah,dh=strengths(T[m['homeID']],'home',L,last6(m['homeID']))
    aa,da=strengths(T[m['awayID']],'away',L,last6(m['awayID']))
    b = LIGA_BASIS_XG
    base_h=(1-b)*L['home']+b*L['xhome']; base_a=(1-b)*L['away']+b*L['xaway']
    lh=base_h*ah*da; la=base_a*aa*dh
    h2h_w, h2h_tore = h2h_werte(m)
    if h2h_w:
        tot=lh+la; f=(1-h2h_w)+h2h_w*h2h_tore/tot; lh*=f; la*=f

    mk = mlh = mla = None
    if quoten_da(m):
        (mlh,mla),mk=market_lambdas(m)
    w = args.markt if mk else 0.0
    flh=(1-w)*lh+w*(mlh if mk else 0); fla=(1-w)*la+w*(mla if mk else 0)
    M=matrix(flh,fla); p=probs(M)
    idx=np.dstack(np.unravel_index(np.argsort(-M.ravel()),M.shape))[0][:3]
    return dict(gesperrt=False, match=m, sid=sid, L=L, ah=ah, dh=dh, aa=aa, da=da,
                lh=lh, la=la, mlh=mlh, mla=mla, mk=mk, w=w, flh=flh, fla=fla,
                M=M, p=p, h2h_w=h2h_w,
                top3=[(f'{a}:{b}', float(M[a,b])) for a,b in idx])


def analysiere(mid, args):
    r = berechne(mid, args); m = r['match']
    print('='*70); print(m['home_name'],'-',m['away_name'], f"(Spiel {mid}, Saison {r['sid']})")
    if r['gesperrt']:
        print(f"  KEINE PROGNOSE. Saisonspiele: {m['home_name']} {r['nh']}, {m['away_name']} {r['na']}"
              f" (noetig: {MIN_SAISONSPIELE}).")
        print("  Darunter ersetzt das Modell die Teamstaerke durch den Liga-Durchschnitt und")
        print("  liefert fuer jedes Spiel fast dieselben Zahlen. Nicht als Tipp verwendbar.")
        print("  Nur zur Ansicht erzwingbar mit --trotzdem.")
        return
    L=r['L']; p=r['p']
    pct = lambda d: {k: round(float(v)*100,1) for k,v in d.items()}
    print(f" Liga-Schnitt: Heim {L['home']:.2f} Tore / {L['xhome']:.2f} xG, Auswärts {L['away']:.2f} Tore / {L['xaway']:.2f} xG")
    print(f" Stärken: Heim Att {r['ah']:.2f} Def {r['dh']:.2f} | Ausw Att {r['aa']:.2f} Def {r['da']:.2f}")
    print(f" H2H-Gewicht: {r['h2h_w']:.0%}")
    if r['mk']:
        print(f" λ Modell {r['lh']:.2f}-{r['la']:.2f} | λ Markt {r['mlh']:.2f}-{r['mla']:.2f}"
              f" | Markt-Anteil {r['w']:.0%} | final {r['flh']:.2f}-{r['fla']:.2f}")
        print(' Markt (ohne Marge):', pct(r['mk']))
    else:
        print(f" λ Modell {r['lh']:.2f}-{r['la']:.2f} (keine vollständigen Vorab-Quoten)")
    print(' FINAL:', pct(p))
    print(' Top3:',[(e,round(v*100,1)) for e,v in r['top3']])
    print(' Faire Quoten:',{k:round(1/float(v),2) for k,v in p.items()})
    if r['mk']:
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
    ap.add_argument("--markt", type=float, default=MARKT_ANTEIL, help="Anteil Vorab-Quoten (0 bis 1, Standard 0)")
    ap.add_argument("--neu", action="store_true", help="API-Daten neu laden")
    ap.add_argument("--trotzdem", action="store_true",
                    help="Sperre bei zu wenigen Saisonspielen umgehen (Ergebnis ist kein Tipp)")
    ap.add_argument("--daten", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "daten"))
    args = ap.parse_args()
    if args.liste: liste(args.liste, args)
    for mid in args.spiele: analysiere(mid, args)
    if not args.liste and not args.spiele: ap.print_help()
