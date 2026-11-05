import sys,json,math; sys.path.insert(0,'.')
import numpy as np, fs
from model import ko_rounds
import backtest as B
R=json.load(open('../backtest.json')); S=B.S; T=B.T
out={}
for cur,r in R.items():
    ids=[s for s,y in S[cur]]; i=ids.index(int(cur)); rows={}
    for sid in ids[max(0,i-3):i+1]:
        d=fs.get('league-matches',season_id=sid,max_per_page=1000,page=1)['data']; KO=ko_rounds(d)
        for m in d:
            if m['status']!='complete' or m['date_unix']>=T or m['roundID'] in KO: continue
            if not(isinstance(m['homeGoalCount'],int) and isinstance(m['awayGoalCount'],int)): continue
            xa,xb=m.get('team_a_xg'),m.get('team_b_xg')
            rows[m['id']]=(m['date_unix'],m['homeID'],m['awayID'],m['homeGoalCount'],m['awayGoalCount'],xa if isinstance(xa,(int,float)) else -1,xb if isinstance(xb,(int,float)) else -1)
    data=sorted(rows.values()); N=len(data); t0=int(N*.9); tr=data[:t0]; te=data[t0:]
    # xG-Ziel: xG wenn vorhanden (beide >=0, nicht beide 0), sonst Tore
    trx=[(a,b,c,(x if (x>=0 and y>=0 and x+y>0) else g1),(y if (x>=0 and y>=0 and x+y>0) else g2)) for a,b,c,g1,g2,x,y in tr]
    cov=np.mean([(x>=0 and y>=0 and x+y>0) for a,b,c,g1,g2,x,y in tr])
    lamx=B.fit(trx,r['alpha'],0)
    assert len(te)==len(r['test'])
    for k,(row,x) in enumerate(zip(te,r['test'])): x['xg']=B.mkts(*lamx(row[1],row[2]))
    out[cur]=cov; print(cur,'xG-Abdeckung Training',round(cov,2),flush=True)
json.dump(R,open('../backtest.json','w'),default=float)
