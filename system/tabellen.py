#!/usr/bin/env python3
"""Liest Spiele aus der FootyStats-API und gibt die Tabellen je Team aus, wie SYSTEM.md sie verlangt.

    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py --liste 2026-10-10
    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py 8408402 8551445

Je Spiel: match, league-teams der Saison, lastx beider Teams und league-matches der Saison und
der Vorsaison, jeweils zweimal abgefragt und Wert fuer Wert verglichen. Ausgabe als Markdown:
Tabelle je Team (Heim, dann Gast), Torniveau der Liga, Kontextzeile, Gegenprobe. Bild und Wette schreibt das Skript NICHT - die kommen aus dem
Lesen der Tabellen nach SYSTEM.md und CLAUDE.md.

Zeilen wie in SYSTEM.md: Spiele, Tore, Gegentore, xG fuer, xG dagegen und die Varianz-Felder
(seasonScoredAVG, seasonConcededAVG, BTTS_and_lose_percentage, BTTS_and_win_percentage, AVG_2hg) -
die Felder und Bezeichnungen genau wie in SYSTEM.md,
so wie die API sie liefert. Dazu (Nutzer 18.10.): Schuesse aufs Tor fuer und gegen, Punkte pro
Spiel, Tabellenplatz, erstes Tor erzielt %, Fuehrung zur Pause %. Schuesse aufs Tor gegen gibt
es als Feld nicht; sie werden aus den Ligaspielen der Saison gezaehlt (L6: fehlt). Der
Tabellenplatz steht nur in den Saisonspalten (lastx liefert dort 0). Liefert die API bei Tore/Gegentore eine Liste (eine Torminute je
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
          ('BTTS_and_win_percentage', 'BTTS_and_win_percentage_{}'), ('AVG_2hg', 'AVG_2hg_{}')]
ZUSATZ = [('Schüsse aufs Tor (für)', 'shotsOnTargetAVG_{}'), ('Schüsse aufs Tor (gegen)', None),
          ('Punkte pro Spiel', 'seasonPPG_{}'), ('Tabellenplatz', 'leaguePosition_{}'),
          ('Erstes Tor erzielt %', 'firstGoalScoredPercentage_{}'), ('Führung zur Pause %', 'leadingAtHTPercentage_{}')]
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
    if isinstance(v, list):  # seasonGoals_home/away usw.: ein Eintrag (Torminute) je Tor
        return len(v)
    return v if isinstance(v, (int, float)) else None


def f(v):
    if v is None:
        return 'fehlt'
    return str(v).replace('.', ',')


def schuesse_gegen(spiele, tid, vor):
    """Zugelassene Schuesse aufs Tor pro Spiel aus den Ligaspielen vor dem Anpfiff (gesamt / zu Hause / auswaerts)."""
    werte = {'overall': [], 'home': [], 'away': []}
    for m in spiele:
        if m.get('status') != 'complete' or m['date_unix'] >= vor or tid not in (m['homeID'], m['awayID']):
            continue
        sa, sb = m.get('team_a_shotsOnTarget'), m.get('team_b_shotsOnTarget')
        if not isinstance(sa, (int, float)) or not isinstance(sb, (int, float)) or sa < 0 or sb < 0 or sa + sb == 0:
            continue  # Spiel ohne erfasste Schussdaten
        heim = m['homeID'] == tid
        gegen = sb if heim else sa
        werte['overall'].append(gegen)
        werte['home' if heim else 'away'].append(gegen)
    return {sp: (round(sum(v) / len(v), 2) if v else None) for sp, v in werte.items()}


def teamwerte(teams, lastx, spiele, tid, vor):
    t = next((x for x in teams if x.get('id') == tid), None)
    l6 = next((x for x in lastx if x.get('last_x_match_num') == 6 and x.get('id') == tid), None)
    w = {}
    for name, muster in FELDER:
        for sp in SPALTEN:
            w[(name, sp)] = zahl(t and t.get('stats'), muster.format(sp))
            w[(name, 'L6' + sp)] = zahl(l6 and l6.get('stats'), muster.format(sp))
    gegen = schuesse_gegen(spiele, tid, vor)
    for name, muster in ZUSATZ:
        for sp in SPALTEN:
            if muster is None:
                w[(name, sp)], w[(name, 'L6' + sp)] = gegen[sp], None
            else:
                w[(name, sp)] = zahl(t and t.get('stats'), muster.format(sp))
                w[(name, 'L6' + sp)] = None if name == 'Tabellenplatz' else zahl(l6 and l6.get('stats'), muster.format(sp))
    return (t or {}).get('name'), w


def torniveau(spiele, vor=None):
    fertig = [m for m in spiele if m.get('status') == 'complete' and (vor is None or m['date_unix'] < vor)]
    if not fertig:
        return None
    tore = [m['homeGoalCount'] + m['awayGoalCount'] for m in fertig]
    sot = [x for m in fertig for x in (m.get('team_a_shotsOnTarget'), m.get('team_b_shotsOnTarget'))
           if isinstance(x, (int, float)) and x >= 0]
    return (len(fertig), round(sum(tore) / len(tore), 2), round(100 * sum(x >= 3 for x in tore) / len(tore)),
            round(sum(sot) / len(sot), 2) if sot else None)


def tabelle(name, w):
    sp6 = SPALTEN + ['L6' + s for s in SPALTEN]
    z = [f"**{name}**",
         "| | gesamt | zu Hause | auswärts | L6 gesamt | L6 zu Hause | L6 auswärts |",
         "|---|---|---|---|---|---|---|"]
    z += [f"| {n} | " + ' | '.join(f(w[(n, s)]) for s in sp6) + ' |' for n, _ in FELDER + ZUSATZ]
    return '\n'.join(z)


def liste(datum):
    for m in hole('todays-matches', date=datum):
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"{m['id']}  {zeit}  {m.get('status')}  {m['home_name']} – {m['away_name']}  (Saison {m['competition_id']})")


def spiele(ids):
    teams_cache, lastx_cache, spiele_cache = {}, {}, {}
    vorsaison_id = {}
    for l in hole('league-list', chosen_leagues_only='true'):
        s = sorted(l['season'], key=lambda x: str(x['year']))
        for i, x in enumerate(s[1:], 1):
            vorsaison_id[x['id']] = s[i - 1]['id']
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
            vid = vorsaison_id.get(sid)
            for s_id in (sid, vid):
                if s_id and (s_id, len(lesung)) not in spiele_cache:
                    spiele_cache[(s_id, len(lesung))] = hole('league-matches', season_id=s_id, max_per_page=1000)
            T, L = teams_cache[(sid, len(lesung))], spiele_cache[(sid, len(lesung))]
            h = teamwerte(T, lastx_cache[(m['homeID'], len(lesung))], L, m['homeID'], m['date_unix'])
            a = teamwerte(T, lastx_cache[(m['awayID'], len(lesung))], L, m['awayID'], m['date_unix'])
            liga = (torniveau(L, m['date_unix']), torniveau(spiele_cache[(vid, len(lesung))]) if vid else None)
            lesung.append((m, h, a, liga))
        (m, (hn, hw), (an, aw), liga), (m2, (_, hw2), (_, aw2), liga2) = lesung
        abw = [k for k in KOPF_FELDER + KONTEXT if m.get(k) != m2.get(k)]
        abw += [f"Heim {k}" for k in hw if hw[k] != hw2[k]] + [f"Gast {k}" for k in aw if aw[k] != aw2[k]]
        abw += ['Torniveau der Liga'] if liga != liga2 else []
        anzahl = len(KOPF_FELDER) + len(KONTEXT) + len(hw) + len(aw) + sum(len(x) for x in liga if x)
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"## {m['home_name']} – {m['away_name']} · {zeit}")
        print(f"Spiel-id {mid} · Heim-id {m['homeID']} · Ausw-id {m['awayID']} · Saison {m['competition_id']} · status {m.get('status')}")
        print(f"API-Teamnamen: {hn or 'fehlt'} / {an or 'fehlt'}\n")
        print(tabelle(m['home_name'], hw) + "\n")
        print(tabelle(m['away_name'], aw) + "\n")
        teile = [f"{lab} ({x[0]} Spiele): Ø Tore {f(x[1])} · Over 2.5 {x[2]} % · Ø Schüsse aufs Tor je Team {f(x[3])}" if x else f"{lab}: fehlt"
                 for lab, x in (('laufende Saison', liga[0]), ('Vorsaison', liga[1]))]
        print("Torniveau der Liga: " + " | ".join(teile))
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
