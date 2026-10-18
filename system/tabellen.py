#!/usr/bin/env python3
"""Liest Spiele aus der FootyStats-API und gibt die Tabellen je Team aus, wie SYSTEM.md sie verlangt.

    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py --liste 2026-10-10
    FOOTYSTATS_KEY="$APIKEY" python3 system/tabellen.py 8408402 8551445

Je Spiel: match, league-teams der Saison, league-matches der Saison (fuer die letzten 6
Ligaspiele), team beider Teams (fuer die abgeschlossene Vorsaison) und league-matches der
Vorsaison der Liga (fuer die Liga-Grundwerte) - alles zweimal abgefragt und Wert fuer Wert
verglichen. Ausgabe als Markdown: Tabelle je Team (Heim, dann Gast) mit Vorsaison-Zeile,
dann Liga-Grundwerte, Kontextzeile, Gegenprobe. Bild und Wette schreibt das Skript NICHT -
die kommen aus dem Lesen der Tabellen nach SYSTEM.md und CLAUDE.md.

Zeilen wie in SYSTEM.md: Spiele, Tore, Gegentore, xG fuer, xG dagegen und die Varianz-Felder
(seasonScoredAVG, seasonConcededAVG, BTTS_and_lose_percentage, BTTS_and_win_percentage, AVG_2hg).
Saisonspalten kommen aus league-teams, so wie die API sie liefert. Die letzten 6 sind die
letzten 6 Ligaspiele aus league-matches (lastx zaehlt auch Pokal und Europapokal). Liefert die
API bei Tore/Gegentore eine Liste (eine Torminute je Tor), zaehlt die Anzahl der Eintraege.
Fehlt ein Feld, steht "fehlt".

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


def schnitt(werte):
    werte = [v for v in werte if isinstance(v, (int, float))]
    return round(sum(werte) / len(werte), 2) if werte else None


def l6_werte(spiele, tid, vor):
    """Die 10 Zeilen aus den letzten 6 Ligaspielen des Teams vor dem Anpfiff (gesamt, davon zu Hause, davon auswaerts)."""
    eigene = sorted([m for m in spiele if m.get('status') == 'complete' and m['date_unix'] < vor
                     and tid in (m['homeID'], m['awayID'])], key=lambda m: m['date_unix'])[-6:]
    sicht = []
    for m in eigene:
        heim = m['homeID'] == tid
        gf, ga = (m['homeGoalCount'], m['awayGoalCount']) if heim else (m['awayGoalCount'], m['homeGoalCount'])
        xf, xa = (m.get('team_a_xg'), m.get('team_b_xg')) if heim else (m.get('team_b_xg'), m.get('team_a_xg'))
        h2 = m['homeGoalCount'] + m['awayGoalCount'] - m.get('ht_goals_team_a', 0) - m.get('ht_goals_team_b', 0)
        sicht.append((heim, gf, ga, xf, xa, h2))
    w = {}
    for sp, teil in (('overall', sicht), ('home', [s for s in sicht if s[0]]), ('away', [s for s in sicht if not s[0]])):
        n = len(teil)
        werte = [n, sum(s[1] for s in teil), sum(s[2] for s in teil), schnitt([s[3] for s in teil]), schnitt([s[4] for s in teil]),
                 schnitt([s[1] for s in teil]), schnitt([s[2] for s in teil]),
                 round(100 * sum(1 for s in teil if s[1] and s[2] and s[1] < s[2]) / n) if n else None,
                 round(100 * sum(1 for s in teil if s[1] and s[2] and s[1] > s[2]) / n) if n else None,
                 schnitt([s[5] for s in teil])] if n else [0] + [None] * 9
        for (name, _), v in zip(FELDER, werte):
            w[(name, 'L6' + sp)] = v
    return w


def teamwerte(teams, spiele, tid, vor):
    t = next((x for x in teams if x.get('id') == tid), None)
    w = {}
    for name, muster in FELDER:
        for sp in SPALTEN:
            w[(name, sp)] = zahl(t and t.get('stats'), muster.format(sp))
    w.update(l6_werte(spiele, tid, vor))
    return (t or {}).get('name'), w


def vorsaison(eintraege, sid, ligen, vorsaison_id):
    """Abgeschlossene Vorsaison des Teams: der Wettbewerb mit den meisten Spielen in der Saison davor."""
    jetzt = next((e for e in eintraege if e.get('competition_id') == sid), None)
    if not jetzt:
        return None
    lab = str(jetzt.get('season'))
    davor = f"{int(lab.split('/')[0]) - 1}/{int(lab.split('/')[1]) - 1}" if '/' in lab else str(int(lab) - 1)
    kand = [e for e in eintraege if str(e.get('season')) == davor and zahl(e.get('stats'), 'seasonMatchesPlayed_overall')]
    if not kand:
        return None
    e = max(kand, key=lambda e: e['stats']['seasonMatchesPlayed_overall'])
    s = e['stats']
    liga = ligen.get(e.get('competition_id'), f"Wettbewerb {e.get('competition_id')}")
    art = 'gleiche Liga' if e.get('competition_id') == vorsaison_id.get(sid) else 'andere Liga'
    return (davor, liga, art, zahl(s, 'seasonMatchesPlayed_overall'), zahl(s, 'xg_for_avg_overall'),
            zahl(s, 'xg_against_avg_overall'), zahl(s, 'seasonScoredAVG_overall'), zahl(s, 'seasonConcededAVG_overall'))


def ligagrund(spiele):
    fertig = [m for m in spiele if m.get('status') == 'complete']
    n = len(fertig)
    if not n:
        return None
    tore = [m['homeGoalCount'] + m['awayGoalCount'] for m in fertig]
    return (n, round(sum(tore) / n, 2), round(100 * sum(t >= 3 for t in tore) / n),
            round(100 * sum(1 for m in fertig if m['homeGoalCount'] and m['awayGoalCount']) / n),
            round(100 * sum(1 for m in fertig if m['homeGoalCount'] == m['awayGoalCount']) / n),
            round(100 * sum(1 for m in fertig if m['homeGoalCount'] > m['awayGoalCount']) / n))


def tabelle(name, w, vs):
    sp6 = SPALTEN + ['L6' + s for s in SPALTEN]
    z = [f"**{name}**",
         "| | gesamt | zu Hause | auswärts | L6 gesamt | L6 zu Hause | L6 auswärts |",
         "|---|---|---|---|---|---|---|"]
    z += [f"| {n} | " + ' | '.join(f(w[(n, s)]) for s in sp6) + ' |' for n, _ in FELDER]
    if vs:
        z.append(f"Vorsaison {vs[0]}, {vs[1]} ({vs[2]}): {f(vs[3])} Spiele · xG für {f(vs[4])} · xG dagegen {f(vs[5])} · "
                 f"Tore pro Spiel {f(vs[6])} · Gegentore pro Spiel {f(vs[7])}")
    else:
        z.append("Vorsaison: fehlt")
    return '\n'.join(z)


def liste(datum):
    for m in hole('todays-matches', date=datum):
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"{m['id']}  {zeit}  {m.get('status')}  {m['home_name']} – {m['away_name']}  (Saison {m['competition_id']})")


def spiele(ids):
    ligen, vorsaison_id = {}, {}
    for l in hole('league-list', chosen_leagues_only='true'):
        s = sorted(l['season'], key=lambda x: str(x['year']))
        for i, x in enumerate(s):
            ligen[x['id']] = l['name']
            if i:
                vorsaison_id[x['id']] = s[i - 1]['id']
    cache = {}

    def einmal(schluessel, abruf):  # je Lesung genau einmal frisch von der API
        if schluessel not in cache:
            cache[schluessel] = abruf()
        return cache[schluessel]

    for mid in ids:
        lesung = []
        for n in range(2):  # erste Lesung und Gegenprobe, beide frisch von der API
            m = hole('match', match_id=mid)
            m = m[0] if isinstance(m, list) else m
            sid, vor = m['competition_id'], m['date_unix']
            T = einmal(('teams', sid, n), lambda: hole('league-teams', season_id=sid, include='stats'))
            L = einmal(('spiele', sid, n), lambda: hole('league-matches', season_id=sid, max_per_page=1000))
            vid = vorsaison_id.get(sid)
            LV = einmal(('spiele', vid, n), lambda: hole('league-matches', season_id=vid, max_per_page=1000)) if vid else []
            teile = [m, ligagrund(LV)]
            for tid in (m['homeID'], m['awayID']):
                E = einmal(('team', tid, n), lambda: hole('team', team_id=tid, include='stats') or [])
                teile.append((teamwerte(T, L, tid, vor), vorsaison(E, sid, ligen, vorsaison_id)))
            lesung.append(teile)
        (m, lg, (h, hv), (a, av)), (m2, lg2, (h2, hv2), (a2, av2)) = lesung
        abw = [k for k in KOPF_FELDER + KONTEXT if m.get(k) != m2.get(k)]
        abw += [f"Heim {k}" for k in h[1] if h[1][k] != h2[1][k]] + [f"Gast {k}" for k in a[1] if a[1][k] != a2[1][k]]
        abw += [x for x, y, z in (('Heim Vorsaison', hv, hv2), ('Gast Vorsaison', av, av2), ('Liga-Grundwerte', lg, lg2)) if y != z]
        anzahl = len(KOPF_FELDER) + len(KONTEXT) + len(h[1]) + len(a[1]) + len(hv or ()) + len(av or ()) + len(lg or ())
        zeit = time.strftime('%d.%m. %H:%M UTC', time.gmtime(m['date_unix']))
        print(f"## {m['home_name']} – {m['away_name']} · {zeit}")
        print(f"Spiel-id {mid} · Heim-id {m['homeID']} · Ausw-id {m['awayID']} · Saison {m['competition_id']} · status {m.get('status')}")
        print(f"API-Teamnamen: {h[0] or 'fehlt'} / {a[0] or 'fehlt'}")
        print("L6 = letzte 6 Ligaspiele vor dem Anpfiff.\n")
        print(tabelle(m['home_name'], h[1], hv) + "\n")
        print(tabelle(m['away_name'], a[1], av) + "\n")
        if lg:
            print(f"Liga-Grundwerte Vorsaison ({ligen.get(m['competition_id'], 'fehlt')}, {lg[0]} Spiele): Ø Tore {f(lg[1])} · "
                  f"Over 2.5 {lg[2]} % · BTTS {lg[3]} % · Remis {lg[4]} % · Heimsieg {lg[5]} %")
        else:
            print("Liga-Grundwerte Vorsaison: fehlt")
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
