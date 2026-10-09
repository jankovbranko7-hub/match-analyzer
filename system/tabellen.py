#!/usr/bin/env python3
"""Liest Spiele aus der FootyStats-API und gibt die Tabellen je Team aus, wie SYSTEM.md sie verlangt.

    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py --liste 2026-10-10
    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py 8408402 8551445

Je Spiel: match, league-teams der Saison und lastx beider Teams, jeweils zweimal abgefragt
und Wert fuer Wert verglichen. Ausgabe als Markdown: Tabelle je Team (Heim, dann Gast),
Kontextzeile, Gegenprobe. Bild und Wette schreibt das Skript NICHT - die kommen aus dem
Lesen der Tabellen nach SYSTEM.md und CLAUDE.md.

Zeilen: Spiele, Tore, Gegentore (Summen der API), Tore pro Spiel, Gegentore pro Spiel
(Summe geteilt durch Spiele, damit sie dieselbe Einheit haben wie xG), xG fuer, xG dagegen
(Schnitt pro Spiel laut API). Fehlt ein Feld, steht "fehlt". Bei 0 Spielen laesst sich
"pro Spiel" nicht bilden, dort steht ebenfalls "fehlt".

Der Key kommt aus FOOTYSTATS_KEY und wird nie ausgegeben.
"""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request

BASE = "https://api.football-data-api.com/"
SPALTEN = ['overall', 'home', 'away']
FELDER = [('Spiele', 'seasonMatchesPlayed_{}'), ('Tore', 'seasonScoredNum_{}'),
          ('Gegentore', 'seasonConcededNum_{}'), ('xG für', 'xg_for_avg_{}'),
          ('xG dagegen', 'xg_against_avg_{}')]
KONTEXT = ['team_a_xg_prematch', 'team_b_xg_prematch', 'btts_potential', 'o25_potential', 'u25_potential']
KOPF_FELDER = ['id', 'homeID', 'awayID', 'home_name', 'away_name', 'competition_id', 'date_unix']


def hole(endpoint, **params):
    key = os.environ.get('FOOTYSTATS_KEY')
    if not key:
        sys.exit("FOOTYSTATS_KEY fehlt: beim Aufruf FOOTYSTATS_KEY=\"$APIKEY\" mitgeben.")
    url = BASE + endpoint + "?" + urllib.parse.urlencode({**params, 'key': key})
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            daten = json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 417:
            sys.exit("HTTP 417: Stundenlimit der API erreicht. Warten, nicht sofort erneut abfragen.")
        sys.exit(f"API-Fehler bei {endpoint}: HTTP {e.code}")
    if not daten.get('success', True):
        sys.exit(f"API-Fehler bei {endpoint}: {daten.get('message')}")
    return daten['data']


def zahl(d, k):
    v = (d or {}).get(k)
    return v if isinstance(v, (int, float)) else None


def f(v, stellen=None):
    if v is None:
        return 'fehlt'
    if stellen is not None:
        return f"{v:.{stellen}f}".replace('.', ',')
    return str(v).replace('.', ',')


def teamwerte(teams, lastx, tid):
    t = next((x for x in teams if x.get('id') == tid), None)
    l6 = next((x for x in lastx if x.get('last_x_match_num') == 6 and x.get('id') == tid), None)
    w = {}
    for name, muster in FELDER:
        for sp in SPALTEN:
            w[(name, sp)] = zahl(t and t.get('stats'), muster.format(sp))
            w[(name, 'L6' + sp)] = zahl(l6 and l6.get('stats'), muster.format(sp))
    w['L6 letztes Spiel'] = zahl(l6, 'last_updated_match_timestamp')
    w['L6 competition_id'] = zahl(l6, 'competition_id')
    return (t or {}).get('name'), w


def tabelle(name, w):
    sp6 = SPALTEN + ['L6' + s for s in SPALTEN]
    z = [f"**{name}**",
         "| | gesamt | zu Hause | auswärts | L6 gesamt | L6 zu Hause | L6 auswärts |",
         "|---|---|---|---|---|---|---|"]
    def pro_spiel(feld, sp):
        n, s = w[('Spiele', sp)], w[(feld, sp)]
        return s / n if n and s is not None else None
    reihen = [('Spiele', [f(w[('Spiele', s)]) for s in sp6]),
              ('Tore', [f(w[('Tore', s)]) for s in sp6]),
              ('Gegentore', [f(w[('Gegentore', s)]) for s in sp6]),
              ('Tore pro Spiel', [f(pro_spiel('Tore', s), 2) for s in sp6]),
              ('Gegentore pro Spiel', [f(pro_spiel('Gegentore', s), 2) for s in sp6]),
              ('xG für', [f(w[('xG für', s)]) for s in sp6]),
              ('xG dagegen', [f(w[('xG dagegen', s)]) for s in sp6])]
    z += [f"| {n} | " + ' | '.join(v) + ' |' for n, v in reihen]
    ts = w['L6 letztes Spiel']
    datum = time.strftime('%d.%m.%Y', time.gmtime(ts)) if ts else 'fehlt'
    quelle = 'alle Wettbewerbe' if w['L6 competition_id'] == -1 else f"Wettbewerb {f(w['L6 competition_id'])}"
    z.append(f"\nLetzte 6: letztes Spiel am **{datum}** ({quelle}, laut API).")
    return '\n'.join(z)


def liste(datum):
    for m in hole('todays-matches', date=datum):
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"{m['id']}  {zeit}  {m.get('status')}  {m['home_name']} – {m['away_name']}  (Saison {m['competition_id']})")


def spiele(ids):
    teams_cache, lastx_cache = {}, {}
    for mid in ids:
        lesung = []
        for _ in range(2):  # erste Lesung und Gegenprobe, beide frisch von der API
            m = hole('match', match_id=mid)
            m = m[0] if isinstance(m, list) else m
            sid = m['competition_id']
            if (sid, len(lesung)) not in teams_cache:
                teams_cache[(sid, len(lesung))] = hole('league-teams', season_id=sid, include='stats')
            for tid in (m['homeID'], m['awayID']):
                if (tid, len(lesung)) not in lastx_cache:
                    lastx_cache[(tid, len(lesung))] = hole('lastx', team_id=tid)
            T = teams_cache[(sid, len(lesung))]
            h = teamwerte(T, lastx_cache[(m['homeID'], len(lesung))], m['homeID'])
            a = teamwerte(T, lastx_cache[(m['awayID'], len(lesung))], m['awayID'])
            lesung.append((m, h, a))
        (m, (hn, hw), (an, aw)), (m2, (_, hw2), (_, aw2)) = lesung
        abw = [k for k in KOPF_FELDER + KONTEXT if m.get(k) != m2.get(k)]
        abw += [f"Heim {k}" for k in hw if hw[k] != hw2[k]] + [f"Gast {k}" for k in aw if aw[k] != aw2[k]]
        anzahl = len(KOPF_FELDER) + len(KONTEXT) + len(hw) + len(aw)
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"## {m['home_name']} – {m['away_name']} · {zeit}")
        print(f"Spiel-id {mid} · Heim-id {m['homeID']} · Ausw-id {m['awayID']} · Saison {m['competition_id']} · status {m.get('status')}")
        print(f"API-Teamnamen: {hn or 'fehlt'} / {an or 'fehlt'}\n")
        print(tabelle(m['home_name'], hw) + "\n")
        print(tabelle(m['away_name'], aw) + "\n")
        print("Kontext: Pre-Match-xG " + f(zahl(m, 'team_a_xg_prematch')) + " : " + f(zahl(m, 'team_b_xg_prematch'))
              + " · BTTS " + f(zahl(m, 'btts_potential')) + " · Over " + f(zahl(m, 'o25_potential'))
              + " · Under " + f(zahl(m, 'u25_potential')))
        print(f"Gegenprobe: {anzahl} Werte verglichen, " + (f"ABWEICHUNG – keine Wette: {abw}" if abw else "beide Lesungen identisch.") + "\n")


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == '--liste':
        liste(a[1])
    else:
        spiele([int(x) for x in a])
