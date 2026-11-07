# FootyStats-Daten zu einem Spiel (Forebet-Check v2).
# Aufruf: python3 -I werkzeuge/fs_spiel.py <season_id> "<Heim-Teilname>" "<Auswärts-Teilname>"
# Gibt aus: Anstoß, Vorab-Werte, Saison (gesamt + Heim/Auswärts), letzte 6 aller Wettbewerbe,
# letzte 6 Ligaspiele, Direktvergleiche, FootyStats-Trends. Keine Quoten.
import json, sys, subprocess, os, datetime
S = os.path.dirname(os.path.abspath(__file__))
SEASON, H, A = sys.argv[1], sys.argv[2].lower(), sys.argv[3].lower()
BER = datetime.timezone(datetime.timedelta(hours=1))  # MEZ (Winterzeit)

def get(path, **q):
    out = subprocess.run([S + '/fs.sh', path] + [f'{k}={v}' for k, v in q.items()],
                         capture_output=True, text=True).stdout
    body, code = out.rsplit('\n__HTTP', 1)
    if code.strip() != '200':
        sys.exit(f'HTTP {code.strip()} bei {path}')
    return json.loads(body)

def t(u): return datetime.datetime.fromtimestamp(u, BER).strftime('%d.%m.%Y %H:%M')
def g(d, k, nd='fehlt'):
    v = d.get(k)
    return nd if v in (None, '', -1) else v

lm = get('league-matches', season_id=SEASON, max_per_page=1000)['data']
cand = [m for m in lm if H in m['home_name'].lower() and A in m['away_name'].lower()]
if not cand:
    sys.exit('Spiel nicht gefunden – Teilnamen prüfen')
cand.sort(key=lambda m: (m['status'] == 'complete', m['date_unix']))
mm = cand[0]
mid, hid, aid = mm['id'], mm['homeID'], mm['awayID']
m = get('match', match_id=mid)['data']
print(f"## {m['home_name']} – {m['away_name']} · Anstoß {t(m['date_unix'])} · match_id {mid} · Status {m['status']}")
print(f"Vorab: xG {g(m,'team_a_xg_prematch')} : {g(m,'team_b_xg_prematch')} (gesamt {g(m,'total_xg_prematch')}) · "
      f"PPG Heim/Ausw. {g(m,'pre_match_home_ppg')} / {g(m,'pre_match_away_ppg')} · Ø Tore {g(m,'avg_potential')}")
print(f"Potenzial %: o1.5 {g(m,'o15_potential')} · o2.5 {g(m,'o25_potential')} · o3.5 {g(m,'o35_potential')} · "
      f"BTTS {g(m,'btts_potential')} · o0.5 HZ {g(m,'o05HT_potential')}")

lt = {x['id']: x for x in get('league-teams', season_id=SEASON, include='stats')['data']}
def saison(tid, side):
    x = lt.get(tid)
    if not x: print('  Saison: fehlt'); return
    s = x['stats']
    def row(sfx, lab):
        p = s.get(f'seasonMatchesPlayed_{sfx}')
        return (f"  {lab:8} Sp {p} · S-U-N {s.get(f'seasonWinsNum_{sfx}')}-{s.get(f'seasonDrawsNum_{sfx}')}-{s.get(f'seasonLossesNum_{sfx}')}"
                f" · Tore {s.get(f'seasonScoredNum_{sfx}')}:{s.get(f'seasonConcededNum_{sfx}')} · PPG {s.get(f'seasonPPG_{sfx}')}"
                f" · xG {s.get(f'xg_for_avg_{sfx}')}:{s.get(f'xg_against_avg_{sfx}')} · o2.5 {s.get(f'seasonOver25Percentage_{sfx}')}%"
                f" · BTTS {s.get(f'seasonBTTSPercentage_{sfx}')}% · zu null {s.get(f'seasonCSPercentage_{sfx}')}%"
                f" · ohne Tor {s.get(f'seasonFTSPercentage_{sfx}')}%")
    print(f"  Tabellenplatz {g(s,'leaguePosition_overall')}")
    print(row('overall', 'gesamt')); print(row(side, 'Heim' if side == 'home' else 'auswärts'))

def letzte6(tid):
    d = get('lastx', team_id=tid)['data']
    e = [x for x in d if x.get('last_x_match_num') == 6]
    if not e: print('  Letzte 6 (alle Wettbewerbe): fehlt'); return
    s = e[0]['stats']
    print(f"  Letzte 6 (alle Wettb.): S-U-N {s.get('seasonWinsNum_overall')}-{s.get('seasonDrawsNum_overall')}-{s.get('seasonLossesNum_overall')}"
          f" · Tore {s.get('seasonScoredNum_overall')}:{s.get('seasonConcededNum_overall')} · PPG {s.get('seasonPPG_overall')}"
          f" · xG {s.get('xg_for_avg_overall')}:{s.get('xg_against_avg_overall')} · o2.5 {s.get('seasonOver25Percentage_overall')}%"
          f" · BTTS {s.get('seasonBTTSPercentage_overall')}%")

def liga6(tid):
    done = sorted([x for x in lm if x['status'] == 'complete' and tid in (x['homeID'], x['awayID'])],
                  key=lambda x: x['date_unix'])[-6:]
    print('  Letzte 6 Ligaspiele: ' + ' | '.join(
        f"{t(x['date_unix'])[:5]} {x['home_name']} {x['homeGoalCount']}-{x['awayGoalCount']} {x['away_name']}" for x in done))

for tid, side, name in ((hid, 'home', m['home_name']), (aid, 'away', m['away_name'])):
    print(f"### {name}")
    saison(tid, side); letzte6(tid); liga6(tid)

h = m.get('h2h') or {}
r, b = h.get('previous_matches_results', {}), h.get('betting_stats', {})
print(f"### Direktvergleiche: {r.get('totalMatches', 0)} Spiele · Siege {m['home_name']} {r.get('team_a_wins')} · "
      f"Remis {r.get('draw')} · Siege {m['away_name']} {r.get('team_b_wins')} · Ø Tore {b.get('avg_goals')} · "
      f"o2.5 {b.get('over25Percentage')}% · BTTS {b.get('bttsPercentage')}%")
names = {hid: m['home_name'], aid: m['away_name']}
for x in sorted(h.get('previous_matches_ids', []), key=lambda x: -x['date_unix'])[:6]:
    print(f"  {t(x['date_unix'])[:10]} {names.get(x['team_a_id'], x['team_a_id'])} {x['team_a_goals']}-{x['team_b_goals']} {names.get(x['team_b_id'], x['team_b_id'])}")
tr = m.get('trends') or {}
for side in ('home', 'away'):
    for kind, text in tr.get(side, []) or []:
        print(f"  Trend {side} [{kind}]: {text}")
