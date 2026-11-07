# Ergebnisse von Paarungen zwischen 05.11. und 10.11.2026 (Datum im Skript anpassen).
# Aufruf: python3 -I werkzeuge/auswertung.py <comp_ids> "Heim|Auswärts" ...
import json,sys,subprocess,time,calendar,os
S=os.path.dirname(os.path.abspath(__file__))
def get(path,**q):
    out=subprocess.run([S+'/oa.sh',path]+[f'{k}={v}' for k,v in q.items()],capture_output=True,text=True).stdout
    return json.loads(out.rsplit('\n__HTTP',1)[0])
comps=sys.argv[1]; pairs=[p.split('|') for p in sys.argv[2:]]
frm=calendar.timegm((2026,11,5,0,0,0)); to=calendar.timegm((2026,11,10,0,0,0))
rows=[]
for c in comps.split(','):
    p=1
    while True:
        d=get('fixtures/between',competitions=c,page=p,**{'from':frm,'to':to})
        rows+=d.get('data',[])
        if not d.get('info',{}).get('next_page_url'): break
        p+=1
for h,a in pairs:
    m=[r for r in rows if h.lower() in r['home_name'].lower() and a.lower() in r['away_name'].lower()]
    for r in m: print(f"{r['id']} | {r['date'][:16]} | {r['home_name']} {r['home_goals']}-{r['away_goals']} {r['away_name']} | HZ {r.get('ht_score')} | {r['status']} | {r['competition_name']}")
    if not m: print('NICHT GEFUNDEN',h,a)
