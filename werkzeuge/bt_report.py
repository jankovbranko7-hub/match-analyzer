import json,math,numpy as np
R=json.load(open('../backtest.json'))
V=['base','decay','dc','both','market']; MK=['H','A','BTTS','O25']
rows=[x for r in R.values() for x in r['test'] if x['market']]
print('Ligen',len(R),'Testspiele gesamt',sum(len(r['test']) for r in R.values()),'mit Quoten',len(rows))
print('xi gewählt:',{k:v['xi'] for k,v in R.items()})
print('rho Mittel',np.mean([v['rho_base'] for v in R.values()]))
for m in MK:
    y=np.array([x['y'][m] for x in rows],float); base=y.mean()
    out=[]
    for v in V:
        p=np.clip(np.array([x[v][m] for x in rows]),1e-9,1-1e-9)
        out.append(f"{v} {np.mean((p-y)**2):.4f}/{np.mean(-(y*np.log(p)+(1-y)*np.log(1-p))):.4f}")
    print(m,'|','  '.join(out))
def oddsfor(x,k):
    o=x['odds']; return {'H':o['h'],'A':o['a'],'BTTS':o['by'],'O25':o['o'],'U25':o['u']}[k]
def probs(x,v):
    p=dict(x[v]); p['U25']=1-p['O25']; return p
def sim(v,rule,thr):
    n=k=0; g=0.0
    for x in rows:
        p=probs(x,v); cand=[]
        for m in ['H','A','BTTS','O25','U25']:
            q=oddsfor(x,m)
            if not q: continue
            if rule=='prob' and p[m]>=thr: cand.append((p[m],m,q))
            if rule=='value' and p[m]*q>=thr: cand.append((p[m]*q,m,q))
        if not cand: continue
        _,m,q=max(cand); hit={'H':x['y']['H'],'A':x['y']['A'],'BTTS':x['y']['BTTS'],'O25':x['y']['O25'],'U25':not x['y']['O25']}[m]
        n+=1; k+=hit; g+=(q-1) if hit else -1
    return n,k,g
print('\nAuswahlregel | Tipps | Trefferquote | ROI (vor Kosten)')
for v in ['base','both','market']:
    for t in [0.55,0.6,0.65,0.7,0.75]:
        n,k,g=sim(v,'prob',t); print(f'{v} p>={t}: {n} | {100*k/max(n,1):.1f} % | {100*g/max(n,1):+.1f} %')
for v in ['base','both']:
    for t in [1.0,1.05,1.10,1.20]:
        n,k,g=sim(v,'value',t); print(f'{v} p*q>={t}: {n} | {100*k/max(n,1):.1f} % | {100*g/max(n,1):+.1f} %')
