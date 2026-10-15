#!/usr/bin/env python3
"""Liest Spiele aus der FootyStats-API und gibt die Tabellen je Team aus, wie SYSTEM.md sie verlangt.

    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py --liste 2026-10-10
    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py 8408402 8551445

Je Spiel: match, team und lastx beider Teams sowie league-teams der Saison, jeweils zweimal
abgefragt und Wert fuer Wert verglichen.

Saisonspalten (gesamt/zu Hause/auswaerts): bei Ligaspielen die Saison des Spiels. Bei Pokal- und
Europapokalspielen die aktuelle Saison der heimischen Liga des Teams (aus /team, Eintrag mit
season_format "Domestic League"), weil der Wettbewerb selbst oft erst 0 bis 3 Spiele hat. Die
Quelle steht je Team unter der Ueberschrift. Gibt es keine Ligadaten, bleibt es beim Wettbewerb.

Ausgabe als Markdown: Tabelle je Team (Heim, dann Gast), Kontextzeile, Gegenprobe. Bild und Wette schreibt das Skript NICHT - die kommen aus dem
Lesen der Tabellen nach SYSTEM.md und CLAUDE.md.

Zeilen wie in SYSTEM.md: Spiele, Tore, Gegentore, xG fuer, xG dagegen und die Varianz-Felder
(seasonScoredAVG, seasonConcededAVG, BTTS_and_lose_percentage, BTTS_and_win_percentage, AVG_2hg),
Haeufigkeiten und Ergebnisse (seasonCSPercentage, seasonFTSPercentage, seasonOver25Percentage,
seasonBTTSPercentage, winPercentage, drawPercentage, seasonPPG, shotsOnTargetAVG) -
die Felder und Bezeichnungen genau wie in SYSTEM.md,
so wie die API sie liefert. Liefert die API bei Tore/Gegentore eine Liste (eine Torminute je
Tor), zaehlt die Anzahl der Eintraege. Fehlt ein Feld, steht "fehlt".

Der Key kommt aus FOOTYSTATS_KEY und wird nie ausgegeben.
"""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request

BASE = "https://api.football-data-api.com/"
SPALTEN = ['overall', 'home', 'away']
FELDER = [('Spiele', 'seasonMatchesPlayed_{}'), ('Tore', 'seasonGoals_{}'),
          ('Gegentore', 'seasonConceded_{}'), ('xG für', 'xg_for_avg_{}'),
          ('xG dagegen', 'xg_against_avg_{}'), ('seasonScoredAVG', 'seasonScoredAVG_{}'),
          ('seasonConcededAVG', 'seasonConcededAVG_{}'), ('BTTS_and_lose_percentage', 'BTTS_and_lose_percentage_{}'),
          ('BTTS_and_win_percentage', 'BTTS_and_win_percentage_{}'), ('AVG_2hg', 'AVG_2hg_{}'),
          ('seasonCSPercentage', 'seasonCSPercentage_{}'), ('seasonFTSPercentage', 'seasonFTSPercentage_{}'),
          ('seasonOver25Percentage', 'seasonOver25Percentage_{}'), ('seasonBTTSPercentage', 'seasonBTTSPercentage_{}'),
          ('winPercentage', 'winPercentage_{}'), ('drawPercentage', 'drawPercentage_{}'),
          ('seasonPPG', 'seasonPPG_{}'), ('shotsOnTargetAVG', 'shotsOnTargetAVG_{}')]
# /team liefert Tore/Gegentore zu Hause/auswaerts nur unter diesen Namen (gleiche Zahlen wie league-teams)
ERSATZ = {'seasonGoals_{}': 'seasonScoredNum_{}', 'seasonConceded_{}': 'seasonConcededNum_{}'}
KONTEXT = ['team_a_xg_prematch', 'team_b_xg_prematch', 'btts_potential', 'o25_potential', 'u25_potential']
KOPF_FELDER = ['id', 'homeID', 'awayID', 'home_name', 'away_name', 'competition_id', 'date_unix']


def hole(endpoint, pflicht=True, **params):
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
        if not pflicht:
            return None
        sys.exit(f"API-Fehler bei {endpoint}: HTTP {e.code}")
    if not daten.get('success', True):
        if not pflicht:
            return None
        sys.exit(f"API-Fehler bei {endpoint}: {daten.get('message')}")
    return daten['data']


def zahl(d, k):
    v = (d or {}).get(k)
    if isinstance(v, list):  # seasonGoals_home/away usw.: ein Eintrag (Torminute) je Tor
        return len(v)
    return v if isinstance(v, (int, float)) else None


def f(v):
    if v is None:
        return 'fehlt'
    return str(v).replace('.', ',')


def wert(stats, muster, sp):
    v = zahl(stats, muster.format(sp))
    if v is None and muster in ERSATZ:
        v = zahl(stats, ERSATZ[muster].format(sp))
    return v


def heimliga(eintraege, sid):
    """Bei Pokal- und Europapokalspielen die aktuelle Saison der heimischen Liga, sonst None."""
    spiel = next((e for e in eintraege or [] if e.get('competition_id') == sid), None)
    if spiel is None or spiel.get('season_format') == 'Domestic League':
        return None
    def start(e):
        try:
            return int(str(e.get('season'))[:4])
        except ValueError:
            return 0
    ligen = [e for e in eintraege if e.get('season_format') == 'Domestic League'
             and ((e.get('stats') or {}).get('seasonMatchesPlayed_overall') or 0) > 0]
    return max(ligen, key=lambda e: (start(e), e['stats']['seasonMatchesPlayed_overall'])) if ligen else None


def teamwerte(saison, lastx, tid):
    l6 = next((x for x in lastx if x.get('last_x_match_num') == 6 and x.get('id') == tid), None)
    w = {}
    for name, muster in FELDER:
        for sp in SPALTEN:
            w[(name, sp)] = wert(saison, muster, sp)
            w[(name, 'L6' + sp)] = wert(l6 and l6.get('stats'), muster, sp)
    return w


def tabelle(name, w):
    sp6 = SPALTEN + ['L6' + s for s in SPALTEN]
    z = [f"**{name}**",
         "| | gesamt | zu Hause | auswärts | L6 gesamt | L6 zu Hause | L6 auswärts |",
         "|---|---|---|---|---|---|---|"]
    z += [f"| {n} | " + ' | '.join(f(w[(n, s)]) for s in sp6) + ' |' for n, _ in FELDER]
    return '\n'.join(z)


def liste(datum):
    for m in hole('todays-matches', date=datum):
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"{m['id']}  {zeit}  {m.get('status')}  {m['home_name']} – {m['away_name']}  (Saison {m['competition_id']})")


def spiele(ids):
    teams_cache, team_cache, lastx_cache = {}, {}, {}
    for mid in ids:
        lesung = []
        for r in range(2):  # erste Lesung und Gegenprobe, beide frisch von der API
            m = hole('match', match_id=mid)
            m = m[0] if isinstance(m, list) else m
            sid = m['competition_id']
            werte = []
            for tid in (m['homeID'], m['awayID']):
                if (tid, r) not in team_cache:
                    team_cache[(tid, r)] = hole('team', pflicht=False, team_id=tid, include='stats')
                if (tid, r) not in lastx_cache:
                    lastx_cache[(tid, r)] = hole('lastx', team_id=tid)
                liga = heimliga(team_cache[(tid, r)], sid)
                if liga:
                    saison, name = liga.get('stats'), liga.get('name')
                    quelle = (f"heimische Liga ({liga.get('country')}, Saison {liga.get('season')}, "
                              f"Wettbewerb {liga.get('competition_id')}) statt Wettbewerb {sid}")
                else:
                    if (sid, r) not in teams_cache:
                        teams_cache[(sid, r)] = hole('league-teams', season_id=sid, include='stats')
                    t = next((x for x in teams_cache[(sid, r)] if x.get('id') == tid), None)
                    saison, name, quelle = t and t.get('stats'), t and t.get('name'), f"Wettbewerb des Spiels ({sid})"
                werte.append((name, quelle, teamwerte(saison, lastx_cache[(tid, r)], tid)))
            lesung.append((m, werte))
        (m, [(hn, hq, hw), (an, aq, aw)]), (m2, [(_, hq2, hw2), (_, aq2, aw2)]) = lesung
        abw = [k for k in KOPF_FELDER + KONTEXT if m.get(k) != m2.get(k)]
        abw += [q for q, a, b in (('Quelle Heim', hq, hq2), ('Quelle Gast', aq, aq2)) if a != b]
        abw += [f"Heim {k}" for k in hw if hw[k] != hw2[k]] + [f"Gast {k}" for k in aw if aw[k] != aw2[k]]
        anzahl = len(KOPF_FELDER) + len(KONTEXT) + 2 + len(hw) + len(aw)
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"## {m['home_name']} – {m['away_name']} · {zeit}")
        print(f"Spiel-id {mid} · Heim-id {m['homeID']} · Ausw-id {m['awayID']} · Saison {m['competition_id']} · status {m.get('status')}")
        print(f"API-Teamnamen: {hn or 'fehlt'} / {an or 'fehlt'}")
        print(f"Saisonspalten Heim: {hq}")
        print(f"Saisonspalten Gast: {aq}\n")
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
