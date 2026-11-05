# Ergebnisabruf (Abschnitt 10): python3 -I results14.py <protokoll/TAG-Ordner> <TAG>
import sys,json; sys.path.insert(0,'.')
import fs
V=json.load(open(sys.argv[1]+'/vorab.json'))['matches']; TAG=sys.argv[2]; out={}
for k,v in V.items():
    if not v.get('match_id'): continue
    d=fs.get('match',nocache=True,match_id=v['match_id'])['data']; d=d[0] if isinstance(d,list) else d
    out[k]=dict(match_id=d['id'],home=d['home_name'],away=d['away_name'],status=d['status'],date_unix=d['date_unix'],hg=d['homeGoalCount'],ag=d['awayGoalCount'],
                ht=(d.get('ht_goals_team_a'),d.get('ht_goals_team_b')),homeID=d['homeID'],awayID=d['awayID'])
    print(k,out[k]['status'],out[k]['home'],out[k]['hg'],':',out[k]['ag'],out[k]['away'],d['homeID']==v['home_id'] and d['awayID']==v['away_id'])
json.dump(out,open(f'../results_{TAG}.json','w'),ensure_ascii=False,indent=1)
