# Endergebnisse für die Auswertung: python3 -I werkzeuge/fs_ergebnis.py <match_id> [<match_id> ...]
import json, sys, subprocess, os
S = os.path.dirname(os.path.abspath(__file__))
for mid in sys.argv[1:]:
    out = subprocess.run([S + '/fs.sh', 'match', f'match_id={mid}'], capture_output=True, text=True).stdout
    m = json.loads(out.rsplit('\n__HTTP', 1)[0])['data']
    print(f"{mid} {m['home_name']} {m['homeGoalCount']}:{m['awayGoalCount']} {m['away_name']} "
          f"(HZ {m.get('ht_goals_team_a')}:{m.get('ht_goals_team_b')}) Status {m['status']}")
