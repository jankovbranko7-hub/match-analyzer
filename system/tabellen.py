#!/usr/bin/env python3
"""Liest Spiele aus der FootyStats-API und gibt die Tabellen je Team aus, wie SYSTEM.md sie verlangt.

    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py --liste 2026-10-10
    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py 8408402 8551445
    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py --roh rohdaten.json 8408402

Je Spiel: match, league-teams der Saison und lastx beider Teams, jeweils zweimal abgefragt
und Wert fuer Wert verglichen. Ausgabe als Markdown: je Team (Heim, dann Gast) ALLE Felder,
die die API liefert, gegliedert nach den sechs Fragen des Spielbilds aus SYSTEM.md; dazu
Kontext, direkter Vergleich und Gegenprobe. Bild und Wette schreibt das Skript NICHT - die
kommen aus dem Lesen der Tabellen nach SYSTEM.md und CLAUDE.md.

Felder zu Ecken, Karten, Abseits, Fouls, Teamnamen in anderen Sprachen und Verwaltung
(Zuschauer, Gehalt, Stadion, Links) werden mitgelesen und mitverglichen, aber nicht als
Tabelle gezeigt, weil sie keine der fuenf Wetten betreffen. Mit --roh landen alle Felder
beider Lesungen ungekuerzt in einer JSON-Datei.

Liefert die API bei einem Feld eine Liste (z. B. eine Torminute je Tor), zaehlt die Anzahl
der Eintraege. Fehlt ein Feld, steht "fehlt". Der Key kommt aus FOOTYSTATS_KEY und wird nie
ausgegeben.
"""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

BASE = "https://api.football-data-api.com/"
SPALTEN = ['overall', 'home', 'away']
# Reihenfolge der Pruefung zaehlt: das erste passende Muster bestimmt den Abschnitt.
ABSCHNITTE = [
    ('5 · Wie nah ist ein Remis?', r'(?i)draw'),
    ('2 · Wie beginnt das Spiel? (erstes Tor, Halbzeit, Torminuten)', r'HT|firstGoal|_min_|Min$|_fhg'),
    ('3 · Was passiert nach dem ersten Tor? (2. Halbzeit, Verlauf)', r'BTTS_and_|BTTS_both|_2hg|BothHalves'),
    ('4 · Trifft der Schwächere, hält der Starke die Null? (Null, ohne Tor, Torhäufigkeit)', r'^season(CS|FTS|BTTS|Over|Under)'),
    ('1 · Wer hat das Spiel in der Hand? (Stärke, Kontrolle, Form)', r'^(season|xg_|shots|possession|attacks|dangerous|home(Attack|Defence|Overall)|leaguePosition|currentForm|winPercentage|losePercentage)'),
    ('6 · Wie belastbar sind die Zahlen? (erfasste Spiele)', r'(?i)recorded|recoded'),
]
NICHT_GEZEIGT = r'(?i)^name_|corner|card|offside|foul|attendance|salar|venue|url|^women|additional_info|previous_seasons|suspended|prediction_risk'
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


def wert(v):
    if isinstance(v, list):  # z. B. seasonGoals_home: ein Eintrag (Torminute) je Tor
        return len(v)
    if isinstance(v, (int, float)) or (isinstance(v, str) and v != ''):
        return v
    return None


def f(v):
    if v is None:
        return 'fehlt'
    return str(v).replace('.', ',') if isinstance(v, (int, float)) else str(v)


def basis(k):
    """Feldname ohne _overall/_home/_away und die Spalte dazu (ohne Endung = gesamt)."""
    m = re.match(r'^(.*)_(overall|home|away)$', k)
    return (m.group(1), m.group(2)) if m else (k, 'overall')


def teamfelder(teams, lastx, tid):
    t = next((x for x in teams if x.get('id') == tid), None)
    l6 = next((x for x in lastx if x.get('last_x_match_num') == 6 and x.get('id') == tid), None)
    return (t or {}).get('name'), (t or {}).get('stats') or {}, (l6 or {}).get('stats') or {}


def abschnitt(b):
    for titel, muster in ABSCHNITTE:
        if re.search(muster, b):
            return titel
    return '7 · Weitere spielbezogene Felder'


def tabellen(name, saison, l6):
    zeilen, nicht = {}, 0
    for k in list(saison) + [k for k in l6 if k not in saison]:
        if re.search(NICHT_GEZEIGT, k):
            nicht += 1
            continue
        b, sp = basis(k)
        zeilen.setdefault(b, {})
        zeilen[b][sp] = wert(saison.get(k))
        zeilen[b]['L6' + sp] = wert(l6.get(k))
    gruppen = {}
    for b in zeilen:
        gruppen.setdefault(abschnitt(b), []).append(b)
    out = [f"**{name}** – {sum(len(v) for v in gruppen.values())} Felder in Tabellen, {nicht} weitere gelesen (Ecken, Karten, Abseits, Fouls, Namen, Verwaltung)"]
    sp6 = SPALTEN + ['L6' + s for s in SPALTEN]
    for titel in sorted(gruppen):
        out += ['', f"*{titel}*", "| | gesamt | zu Hause | auswärts | L6 gesamt | L6 zu Hause | L6 auswärts |",
                "|---|---|---|---|---|---|---|"]
        out += [f"| {b} | " + ' | '.join(f(zeilen[b].get(s)) for s in sp6) + ' |' for b in gruppen[titel]]
    return '\n'.join(out)


def h2h_zeile(m):
    h = m.get('h2h') or {}
    e, w = h.get('previous_matches_results') or {}, h.get('betting_stats') or {}
    if not e.get('totalMatches'):
        return "Direkter Vergleich (Hintergrund): fehlt"
    return (f"Direkter Vergleich (Hintergrund): {e['totalMatches']} Spiele – Heimteam {f(e.get('team_a_wins'))} Siege, "
            f"Gastteam {f(e.get('team_b_wins'))}, Remis {f(e.get('draw'))} · Over 2.5 {f(w.get('over25Percentage'))} % · "
            f"BTTS {f(w.get('bttsPercentage'))} % · zu Null Heimteam {f(w.get('clubACSPercentage'))} %, Gastteam {f(w.get('clubBCSPercentage'))} %")


def vergleich(a, b, vorsilbe):
    return [f"{vorsilbe} {k}" for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)]


def liste(datum):
    for m in hole('todays-matches', date=datum):
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"{m['id']}  {zeit}  {m.get('status')}  {m['home_name']} – {m['away_name']}  (Saison {m['competition_id']})")


def spiele(ids, roh=None):
    teams_cache, lastx_cache, rohdaten = {}, {}, {}
    for mid in ids:
        lesung = []
        for _ in range(2):  # erste Lesung und Gegenprobe, beide frisch von der API
            m = hole('match', match_id=mid)
            m = m[0] if isinstance(m, list) else m
            sid, n = m['competition_id'], len(lesung)
            if (sid, n) not in teams_cache:
                teams_cache[(sid, n)] = hole('league-teams', season_id=sid, include='stats')
            for tid in (m['homeID'], m['awayID']):
                if (tid, n) not in lastx_cache:
                    lastx_cache[(tid, n)] = hole('lastx', team_id=tid)
            T = teams_cache[(sid, n)]
            lesung.append((m, teamfelder(T, lastx_cache[(m['homeID'], n)], m['homeID']),
                           teamfelder(T, lastx_cache[(m['awayID'], n)], m['awayID'])))
        (m, h, a), (m2, h2, a2) = lesung
        abw = [k for k in KOPF_FELDER + KONTEXT + ['h2h'] if m.get(k) != m2.get(k)]
        abw += vergleich(h[1], h2[1], 'Heim') + vergleich(h[2], h2[2], 'Heim L6') + vergleich(a[1], a2[1], 'Gast') + vergleich(a[2], a2[2], 'Gast L6')
        anzahl = len(KOPF_FELDER) + len(KONTEXT) + 1 + sum(len(set(x) | set(y)) for x, y in ((h[1], h2[1]), (h[2], h2[2]), (a[1], a2[1]), (a[2], a2[2])))
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"## {m['home_name']} – {m['away_name']} · {zeit}")
        print(f"Spiel-id {mid} · Heim-id {m['homeID']} · Ausw-id {m['awayID']} · Saison {m['competition_id']} · status {m.get('status')}")
        print(f"API-Teamnamen: {h[0] or 'fehlt'} / {a[0] or 'fehlt'}")
        print("L6 = letzte 6 Pflichtspiele laut API, alle Wettbewerbe (auch Pokal und Europapokal).\n")
        print(tabellen(m['home_name'], h[1], h[2]) + "\n")
        print(tabellen(m['away_name'], a[1], a[2]) + "\n")
        print("Kontext: Pre-Match-xG " + f(wert(m.get('team_a_xg_prematch'))) + " : " + f(wert(m.get('team_b_xg_prematch')))
              + " · BTTS " + f(wert(m.get('btts_potential'))) + " · Over " + f(wert(m.get('o25_potential')))
              + " · Under " + f(wert(m.get('u25_potential'))))
        print(h2h_zeile(m))
        print(f"Gegenprobe: {anzahl} Werte verglichen, " + (f"ABWEICHUNG – keine Wette: {abw[:20]}" if abw else "beide Lesungen identisch.") + "\n")
        rohdaten[mid] = {'match': m, 'heim': {'saison': h[1], 'L6': h[2]}, 'gast': {'saison': a[1], 'L6': a[2]},
                         'gegenprobe_abweichungen': abw}
    if roh:
        with open(roh, 'w', encoding='utf-8') as d:
            json.dump(rohdaten, d, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == '--liste':
        liste(a[1])
    else:
        roh = None
        if a[0] == '--roh':
            roh, a = a[1], a[2:]
        spiele([int(x) for x in a], roh)
