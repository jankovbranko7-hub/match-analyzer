#!/usr/bin/env python3
"""Das Modell. Eingabe sind NUR fuenf Groessen aus der FootyStats-API.

ES GIBT IN DIESER DATEI KEINE GESETZTE ZAHL. Keine Gewichte, keine Daempfung, keine
Schwelle, keine Sperre, kein Erfahrungswert. Was gerechnet wird, steht unten, und jede
Verknuepfung ist ein ungewichtetes Mittel gleichwertiger Schaetzungen in derselben
Einheit.

DIE FUENF EINGABEN
  match-Endpunkt:        team_a_xg_prematch, team_b_xg_prematch
                         btts_potential, o25_potential, u25_potential
  league-teams-Endpunkt: xg_for_avg_home/away, xg_against_avg_home/away

DER RECHENWEG, in zwei Schritten, beide ohne Gewicht

  1. Aus der Tor-Skala. Zwei gleichwertige Schaetzungen je Seite, Mittel daraus:
       a) das Pre-Match-xG der API
       b) Angriff gegen Abwehr: (xG_fuer der einen Seite + xG_gegen der anderen) / 2
     lam_xg = Mittel(a, b)

  2. Aus der Wahrscheinlichkeits-Skala. Gesucht sind die beiden Lambda, deren
     Poisson-Verteilung die drei Potentiale am besten trifft:
       minimiere (P_BTTS - btts)^2 + (P_Over - o25)^2 + (P_Under - u25)^2
     Drei Gleichungen, zwei Unbekannte, kleinste Quadrate. Alle drei Residuen stehen
     auf derselben Skala (0 bis 1), deshalb braucht es keine Gewichtung.
     lam_pot = Ergebnis des Fits

  3. lam = Mittel(lam_xg, lam_pot)

  Beide Schritte liefern dieselbe Groesse in derselben Einheit, also ist das Mittel
  eine Zusammenfassung und keine Abwaegung.

  WICHTIG, an echten Spielen beobachtet: der Fit aus Schritt 2 liefert IMMER
  lam_heim = lam_ausw. BTTS, Over und Under sagen nur etwas ueber die SUMME der Tore,
  nichts darueber, wer sie schiesst. Die Seitenverteilung - und damit Heimsieg gegen
  Auswaertssieg - stammt deshalb vollstaendig aus Schritt 1. Schritt 2 wirkt allein auf
  das Torniveau. Das ist keine Schwaeche des Fits, sondern der Informationsgehalt der
  drei Potentiale. Fehlt eine Seite, wird die andere allein
  genommen und das in der Ausgabe gesagt - nichts wird ersetzt oder geschaetzt.

  Verteilung: reine, unabhaengige Poisson. Keine Dixon-Coles-Korrektur - rho waere
  eine aus der alten Datei geliehene Zahl.

DER TIPP
  Die wahrscheinlichste der fuenf Wetten: Heimsieg, Auswaertssieg, BTTS Ja,
  Ueber 2,5, Unter 2,5. Keine Schwelle, kein Vorrang, kein Gleichstand-Entscheid.

DIE PRUEFUNG, bevor ueberhaupt ein Tipp erscheint
  1. Spiel und Teams werden ueber die id gefuehrt und mit Namen, Team-ids, Liga und
     Anstosszeit ausgeschrieben.
  2. Jedes benutzte Feld wird mit seinem Rohwert gezeigt. Fehlt es, steht FEHLT.
  3. Gegenprobe: eine ZWEITE, UNABHAENGIGE Abfrage derselben Endpunkte (hole_direkt),
     am Zwischenspeicher vorbei, Feld fuer Feld gegen die erste Lesung gehalten.
     Das prueft, ob die Zahl richtig angekommen ist - nicht nur, ob sie richtig
     gelesen wurde. Kostet eine zusaetzliche Abfrage je Endpunkt und Spiel.
  4. Nur wenn beide Abfragen identisch sind, wird der Tipp ausgegeben. Weicht ein
     Wert ab oder schlaegt die zweite Abfrage fehl (Stundenlimit): kein Tipp.

    python3 analyse/modell.py --liste 2026-10-05        Spiele des Tages mit id
    python3 analyse/modell.py 8419375 8469639           diese Spiele rechnen
"""
import argparse, json, math, os, sys

import numpy as np
from scipy.optimize import minimize

import time, urllib.parse, urllib.request

BASE = "https://api.football-data-api.com"
CACHE_STUNDEN = 6


def api_key():
    key = os.environ.get("FOOTYSTATS_API_KEY") or os.environ.get("APIKEY")
    if not key:
        sys.exit("FOOTYSTATS_API_KEY fehlt: in den Umgebungseinstellungen hinterlegen "
                 "(Titelleiste -> Cloud-Umgebung -> Edit) und eine neue Session starten.")
    return key


def hole(endpoint, params, datei, args):
    """Holt eine API-Antwort und speichert sie. Ein Fehler wirft - er beendet nie den Lauf."""
    pfad = os.path.join(args.daten, datei)
    if os.path.exists(pfad) and not args.neu:
        alter_h = (time.time() - os.path.getmtime(pfad)) / 3600
        if alter_h < CACHE_STUNDEN:
            with open(pfad) as f:
                return json.load(f)
        print(f"  (aktualisiere {datei}, war {alter_h:.1f} h alt)")
    url = f"{BASE}/{endpoint}?" + urllib.parse.urlencode({**params, "key": api_key()})
    with urllib.request.urlopen(url, timeout=60) as r:
        daten = json.load(r)
    if not daten.get("success", True):
        raise RuntimeError(f"API-Fehler bei {endpoint}: {daten.get('message')}")
    os.makedirs(args.daten, exist_ok=True)
    with open(pfad, "w") as f:
        json.dump(daten, f)
    return daten


def hole_direkt(endpoint, params):
    """Zweite, unabhaengige Abfrage - geht IMMER zur API, nie an den Zwischenspeicher.

    Nur fuer die Gegenprobe. Sie prueft, ob die Zahl richtig angekommen ist, nicht nur,
    ob sie richtig gelesen wurde. Kostet eine zusaetzliche Abfrage je Endpunkt.
    """
    url = f"{BASE}/{endpoint}?" + urllib.parse.urlencode({**params, "key": api_key()})
    with urllib.request.urlopen(url, timeout=60) as r:
        daten = json.load(r)
    if not daten.get("success", True):
        raise RuntimeError(f"API-Fehler bei {endpoint}: {daten.get('message')}")
    return daten


def liste(datum, args):
    for m in hole("todays-matches", {"date": datum}, f"tag_{datum}.json", args)['data']:
        print(m['id'], m['competition_id'],
              time.strftime('%H:%M UTC', time.gmtime(m['date_unix'])),
              m['home_name'], '-', m['away_name'])

MAXTOR = 12
WETTEN = ('H', 'A', 'BTTS', 'O25', 'U25')
NAME = {'H': 'Heimsieg', 'A': 'Auswaertssieg', 'BTTS': 'BTTS Ja',
        'O25': 'Ueber 2,5', 'U25': 'Unter 2,5'}

MATCHFELDER = ['team_a_xg_prematch', 'team_b_xg_prematch',
               'btts_potential', 'o25_potential', 'u25_potential']
TEAMFELDER = ['xg_for_avg_home', 'xg_for_avg_away',
              'xg_against_avg_home', 'xg_against_avg_away']

_I, _J = np.indices((MAXTOR, MAXTOR))
_FAK = np.array([math.factorial(k) for k in range(MAXTOR)], dtype=float)


def wetten(lh, la):
    """Reine Poisson, keine Korrektur. Gibt die fuenf Wetten plus Remis zurueck."""
    ph = np.exp(-lh) * lh ** np.arange(MAXTOR) / _FAK
    pa = np.exp(-la) * la ** np.arange(MAXTOR) / _FAK
    Mx = np.outer(ph, pa); Mx = Mx / Mx.sum()
    p = dict(H=float(Mx[_I > _J].sum()), A=float(Mx[_I < _J].sum()),
             D=float(np.trace(Mx)), O25=float(Mx[_I + _J >= 3].sum()),
             BTTS=float(Mx[(_I > 0) & (_J > 0)].sum()))
    p['U25'] = 1 - p['O25']
    return p, Mx


def fit_potentiale(btts, o25, u25, start):
    """Die beiden Lambda, deren Poisson die drei Potentiale am besten trifft."""
    ziel = {}
    if btts is not None: ziel['BTTS'] = btts / 100
    if o25 is not None: ziel['O25'] = o25 / 100
    if u25 is not None: ziel['U25'] = u25 / 100
    if not ziel:
        return None, None
    def loss(v):
        p, _ = wetten(*np.exp(v))
        return sum((p[k] - z) ** 2 for k, z in ziel.items())
    r = minimize(loss, np.log(np.maximum(start, 0.05)), method='Nelder-Mead',
                 options=dict(xatol=1e-8, fatol=1e-12, maxiter=4000))
    return tuple(float(x) for x in np.exp(r.x)), float(r.fun)


def feld(d, k):
    """Rohwert oder None. Es wird nichts ersetzt und nichts geschaetzt.

    EINE EXAKTE NULL GILT ALS FEHLEND, nicht als Messung. Keines dieser fuenf Felder
    kann fuer ein angesetztes Spiel echt null sein: ein Pre-Match-xG von 0,00 oder eine
    Over-Chance von 0 % gibt es nicht. An 143 zwischengespeicherten Spielen gemessen:
    10 Spiele fuehren btts = o25 = u25 = 0 UND xG = 0:0, alles Laenderspiele, zu denen
    FootyStats nichts hat. Vorher ging diese Null als echter Wert in die Rechnung -
    fit_potentiale(0, 0, 0) liefert lam 0,000 : 2,674, also Unsinn bis in den Tipp.
    Gefunden am 05.10.2026.
    """
    v = d.get(k, None)
    if not isinstance(v, (int, float)) or v == 0:
        return None
    return v


def zeig(k, v, quelle):
    print(f"    {k:24s} {('FEHLT' if v is None else v):>10}   ({quelle})")


def rechne(mid, args):
    # ---------------------------------------------------- 1. Lesung
    roh_m = hole("match", {"match_id": mid}, f"match_{mid}.json", args)
    m = roh_m['data']
    if isinstance(m, list):
        m = m[0]
    sid = m['competition_id']
    roh_t = hole("league-teams", {"season_id": sid, "include": "stats"},
                     f"teams_{sid}.json", args)
    T = roh_t['data']

    print('=' * 78)
    print(f"SPIEL {mid}")
    print(f"  {m.get('home_name')} (id {m.get('homeID')})  -  "
          f"{m.get('away_name')} (id {m.get('awayID')})")
    import time
    print(f"  Liga/Saison {sid}   Anstoss {time.strftime('%d.%m.%Y %H:%M UTC', time.gmtime(m['date_unix']))}"
          f"   status {m.get('status')}")

    # Teams ueber die id, nie ueber den Namen
    th = next((t for t in T if t['id'] == m['homeID']), None)
    ta = next((t for t in T if t['id'] == m['awayID']), None)
    if th is None or ta is None:
        fehlt = [n for n, t in (('Heim', th), ('Ausw', ta)) if t is None]
        print(f"  ABBRUCH: {', '.join(fehlt)}-Team steht nicht in league-teams der "
              f"Saison {sid}. Kein Tipp.")
        return
    print(f"  Zuordnung ueber id bestaetigt: {th['name']} / {ta['name']}")

    print("\n  EINGABEFELDER, Rohwerte")
    werte = {}
    for k in MATCHFELDER:
        werte[k] = feld(m, k)
        zeig(k, werte[k], 'match')
    for k in TEAMFELDER:
        werte['H.' + k] = feld(th['stats'], k)
        zeig('Heim ' + k, werte['H.' + k], 'league-teams')
    for k in TEAMFELDER:
        werte['A.' + k] = feld(ta['stats'], k)
        zeig('Ausw ' + k, werte['A.' + k], 'league-teams')

    # ---------------------------------------------------- 2. Lesung, Gegenprobe
    print("\n  GEGENPROBE: zweite, unabhaengige Abfrage derselben Endpunkte")
    try:
        m2 = hole_direkt("match", {"match_id": mid})['data']
        if isinstance(m2, list):
            m2 = m2[0]
        T2 = hole_direkt("league-teams", {"season_id": sid, "include": "stats"})['data']
    except Exception as e:
        print(f"    Die zweite Abfrage ist fehlgeschlagen: {type(e).__name__}: {e}")
        print("    Ohne Gegenprobe gibt es keinen Tipp.")
        return
    th2 = next((t for t in T2 if t['id'] == m2['homeID']), None)
    ta2 = next((t for t in T2 if t['id'] == m2['awayID']), None)

    abw = []
    for schluessel, nm in [('id', 'match id'), ('homeID', 'homeID'), ('awayID', 'awayID'),
                           ('home_name', 'home_name'), ('away_name', 'away_name'),
                           ('competition_id', 'competition_id'), ('date_unix', 'date_unix')]:
        if m.get(schluessel) != m2.get(schluessel):
            abw.append(f"{nm}: {m.get(schluessel)!r} vs {m2.get(schluessel)!r}")
    for k in MATCHFELDER:
        if werte[k] != feld(m2, k):
            abw.append(f"{k}: {werte[k]!r} vs {feld(m2, k)!r}")
    for praefix, t2 in (('H.', th2), ('A.', ta2)):
        if t2 is None:
            abw.append(f"{praefix}Team in der zweiten Lesung nicht gefunden")
            continue
        for k in TEAMFELDER:
            if werte[praefix + k] != feld(t2['stats'], k):
                abw.append(f"{praefix}{k}: {werte[praefix+k]!r} vs {feld(t2['stats'], k)!r}")
    if abw:
        print("    ABWEICHUNGEN - KEIN TIPP:")
        for a in abw:
            print(f"      {a}")
        return
    anz = 7 + len(MATCHFELDER) + 2 * len(TEAMFELDER)
    print(f"    {anz} Werte geprueft, beide Lesungen identisch.")

    # ---------------------------------------------------- Schritt 1: Tor-Skala
    print("\n  SCHRITT 1 - aus der Tor-Skala")
    pre_h, pre_a = werte['team_a_xg_prematch'], werte['team_b_xg_prematch']
    ff_h, ff_a = werte['H.xg_for_avg_home'], werte['A.xg_for_avg_away']
    gg_h, gg_a = werte['H.xg_against_avg_home'], werte['A.xg_against_avg_away']

    def mittel(xs):
        xs = [x for x in xs if x is not None]
        return sum(xs) / len(xs) if xs else None

    staerke_h = mittel([ff_h, gg_a])          # Heim-Angriff gegen Ausw-Abwehr
    staerke_a = mittel([ff_a, gg_h])          # Ausw-Angriff gegen Heim-Abwehr
    print(f"    Pre-Match-xG                 {pre_h if pre_h is not None else 'FEHLT'} : "
          f"{pre_a if pre_a is not None else 'FEHLT'}")
    print(f"    Angriff gegen Abwehr         "
          f"{'FEHLT' if staerke_h is None else f'{staerke_h:.3f}'} : "
          f"{'FEHLT' if staerke_a is None else f'{staerke_a:.3f}'}"
          f"   (({ff_h} + {gg_a})/2 bzw. ({ff_a} + {gg_h})/2)")
    lam_xg = (mittel([pre_h, staerke_h]), mittel([pre_a, staerke_a]))
    if None in lam_xg:
        print("    ABBRUCH: aus der Tor-Skala laesst sich kein Lambda bilden. Kein Tipp.")
        return
    print(f"    lam_xg                       {lam_xg[0]:.3f} : {lam_xg[1]:.3f}")

    # ---------------------------------------------------- Schritt 2: Potentiale
    print("\n  SCHRITT 2 - aus den Potentialen")
    btts, o25, u25 = werte['btts_potential'], werte['o25_potential'], werte['u25_potential']
    platzhalter = (btts == 50 and o25 == 50 and u25 == 50)
    if platzhalter:
        # Gemessen am 05.10.2026 an 143 zwischengespeicherten Spielen: 8 Spiele fuehren
        # alle drei auf exakt 50. Bei ihnen weicht der Over-Wert, den ihr EIGENES
        # Pre-Match-xG ergibt, im Mittel 15,1 Punkte von den 50 ab, im Extremfall 32,3
        # (Roma W - Barcelona W: xG 1,84:2,63 ergibt 82,3 %, die API sagt 50).
        # Ausserdem sind BTTS und Ueber 2,5 nie derselbe Wert, ausser zufaellig.
        # Eine 50 ALLEIN ist dagegen normal: 9 Spiele haben echte 50/50 bei Over/Under,
        # 12 ein echtes BTTS von 50. Nur alle drei zugleich sind der Standardwert.
        print("    btts/o25/u25 stehen alle drei auf 50 - das ist der Standardwert der API,")
        print("    keine Messung (an 143 Spielen geprueft). Sie gehen NICHT in die Rechnung ein.")
        lam_pot, rest = None, None
    else:
        if o25 is not None and u25 is not None and abs(o25 + u25 - 100) > 1:
            print(f"    HINWEIS: o25 + u25 = {o25 + u25}, nicht 100. Beide Werte gehen "
                  f"trotzdem unveraendert in den Fit.")
        lam_pot, rest = fit_potentiale(btts, o25, u25, np.array(lam_xg))
    if lam_pot is None:
        print("    kein Fit moeglich - die Potentiale fehlen oder sind Platzhalter.")
        lam = lam_xg
        print(f"\n  lam = lam_xg allein           {lam[0]:.3f} : {lam[1]:.3f}")
    else:
        p_fit, _ = wetten(*lam_pot)
        print(f"    Ziel      BTTS {btts} %   Ueber 2,5 {o25} %   Unter 2,5 {u25} %")
        print(f"    erreicht  BTTS {p_fit['BTTS']*100:.1f} %   Ueber 2,5 {p_fit['O25']*100:.1f} %"
              f"   Unter 2,5 {p_fit['U25']*100:.1f} %   (Restfehler {rest:.5f})")
        print(f"    lam_pot                      {lam_pot[0]:.3f} : {lam_pot[1]:.3f}"
              f"   (symmetrisch - die Potentiale kennen nur die Summe, nicht die Seite)")
        lam = ((lam_xg[0] + lam_pot[0]) / 2, (lam_xg[1] + lam_pot[1]) / 2)
        print(f"\n  SCHRITT 3 - Mittel beider      {lam[0]:.3f} : {lam[1]:.3f}")

    # ---------------------------------------------------- Ergebnis
    p, Mx = wetten(*lam)
    print(f"\n  Erwartete Tore {lam[0]:.2f} : {lam[1]:.2f}   (Summe {lam[0]+lam[1]:.2f})")
    print(f"  Heim {p['H']*100:.1f} %   Remis {p['D']*100:.1f} %   Ausw {p['A']*100:.1f} %")
    print(f"\n  {'Wette':16s} {'Wahrsch.':>9s} {'faire Quote':>12s}")
    for w in WETTEN:
        print(f"  {NAME[w]:16s} {p[w]*100:8.1f} % {1/p[w]:12.2f}")
    tipp = max(WETTEN, key=lambda w: p[w])
    print(f"\n  TIPP: {NAME[tipp]}  {p[tipp]*100:.1f} %   faire Mindestquote {1/p[tipp]:.2f}")
    return dict(mid=mid, lam=lam, p=p, tipp=tipp)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('spiele', nargs='*', type=int)
    ap.add_argument('--liste', metavar='DATUM')
    ap.add_argument('--neu', action='store_true')
    ap.add_argument('--daten', default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'daten'))
    args = ap.parse_args()
    if args.liste:
        liste(args.liste, args)
    for mid in args.spiele:
        try:
            rechne(mid, args)
        except Exception as e:
            print(f"  Spiel {mid}: {type(e).__name__}: {e}  -  kein Tipp")
    if not args.liste and not args.spiele:
        ap.print_help()
