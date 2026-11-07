# Letzte Pflichtspiele, Heim-/Auswärtsspiele und Direktvergleiche zweier Teams (3 Jahre).
# Aufruf: python3 -I werkzeuge/ergebnisse.py <comp_ids,kommagetrennt> "<Heimteam>" "<Auswärtsteam>" [<cache.json>]
import json,sys,subprocess,time,os
S=os.path.dirname(os.path.abspath(__file__)); now=int(time.time())
COMPS=[int(x) for x in sys.argv[1].split(',')]; HOME=sys.argv[2]; AWAY=sys.argv[3]
CACHE=sys.argv[4] if len(sys.argv)>4 else None
def get(path,**q):
    out=subprocess.run([S+'/oa.sh',path]+[f'{k}={v}' for k,v in q.items()],capture_output=True,text=True).stdout
    b,code=out.rsplit('\n__HTTP',1)
    return json.loads(b)
rows={}
for c in COMPS:
  for frm,to in ((now-364*86400,now),(now-728*86400,now-364*86400),(now-1092*86400,now-728*86400)):
    p=1
    while True:
        d=get('fixtures/between',competitions=c,page=p,**{'from':frm,'to':to})
        for r in d.get('data',[]): rows[r['id']]=r
        if not d.get('info',{}).get('next_page_url'): break
        p+=1
if CACHE: json.dump(list(rows.values()),open(CACHE,'w'))
def ln(r): return f"{r['date'][:10]} {r['home_name'][:16]:16} {r['home_goals']}-{r['away_goals']} (HZ {r.get('ht_score')}) {r['away_name'][:16]:16} [{r['competition_name']}]"
done=[r for r in rows.values() if r.get('home_goals') is not None]
done.sort(key=lambda r:r['unix'])
for t in (HOME,AWAY):
    ms=[r for r in done if t in (r['home_name'],r['away_name'])]
    print('###',t,'letzte 10 Pflichtspiele')
    for r in ms[-10:]: print('  ',ln(r))
    hm=[r for r in ms if (r['home_name']==t if t==HOME else r['away_name']==t) and r['unix']>now-200*86400]
    print('  --', 'Heimspiele' if t==HOME else 'Auswärtsspiele','(letzte 8):')
    for r in hm[-8:]: print('    ',ln(r))
print('### Direktvergleiche')
for r in done:
    if {r['home_name'],r['away_name']}=={HOME,AWAY}: print('  ',ln(r))
