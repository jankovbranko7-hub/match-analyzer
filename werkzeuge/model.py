import sys,json,math,os; sys.path.insert(0,'.')
import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
import fs
ALPHAS=[0.1,1,10,100]
T_DEC=int(sys.argv[1]) if __name__=="__main__" else None
S=json.load(open('../seasons.json'))

def ko_rounds(rows):
    # Runden, in denen kein Spiel eine Spieltagnummer hat (game_week 0): Play-off/K.-o.-Runden
    R={}
    for m in rows: R.setdefault(m['roundID'],[]).append(m['game_week'])
    return {r for r,g in R.items() if all(x==0 for x in g)}
def load(cur):
    ids=[sid for sid,yr in S[cur]]; i=ids.index(int(cur)); use=ids[max(0,i-3):i+1]
    rows={}; issues=[]; dup=0; allm=[]; excl=[]
    for sid in use:
        r=fs.get('league-matches',season_id=sid,max_per_page=1000,page=1)
        assert r['pager']['max_page']==1
        KO=ko_rounds(r['data'])
        for m in r['data']:
            allm.append((sid,m))
            if m['status']!='complete' or m['date_unix']>=T_DEC: continue
            if m['roundID'] in KO: excl.append(m['id']); continue
            hg,ag=m['homeGoalCount'],m['awayGoalCount']
            if not (isinstance(hg,int) and isinstance(ag,int) and hg>=0 and ag>=0):
                issues.append(('ungueltige Tore',m['id'],hg,ag)); continue
            if m['id'] in rows: dup+=1; continue
            rows[m['id']]=(m['date_unix'],m['homeID'],m['awayID'],hg,ag,sid)
    data=sorted(rows.values())
    return use,data,dup,issues,allm,excl

def nll_fun(p,H,A,X,Y,n,alpha):
    mu,ha=p[0],p[1]; att=p[2:2+n]; de=p[2+n:]
    lh=mu+ha+att[H]-de[A]; la=mu+att[A]-de[H]
    eh,ea=np.exp(lh),np.exp(la)
    f=np.sum(eh-X*lh)+np.sum(ea-Y*la)+alpha*(np.sum(att**2)+np.sum(de**2))
    g=np.zeros_like(p); rh=eh-X; ra=ea-Y
    g[0]=rh.sum()+ra.sum(); g[1]=rh.sum()
    ga=np.zeros(n); gd=np.zeros(n)
    np.add.at(ga,H,rh); np.add.at(ga,A,ra); np.add.at(gd,A,-rh); np.add.at(gd,H,-ra)
    g[2:2+n]=ga+2*alpha*att; g[2+n:]=gd+2*alpha*de
    return f,g

def fit(train,teams,alpha):
    idx={t:i for i,t in enumerate(teams)}; n=len(teams)
    H=np.array([idx[r[1]] for r in train]); A=np.array([idx[r[2]] for r in train])
    X=np.array([r[3] for r in train],float); Y=np.array([r[4] for r in train],float)
    p0=np.zeros(2+2*n); p0[0]=math.log(max((X.mean()+Y.mean())/2,0.1))
    res=minimize(nll_fun,p0,args=(H,A,X,Y,n,alpha),jac=True,method='L-BFGS-B',options={'maxiter':5000,'gtol':1e-9})
    return res,idx

def lam(p,idx,n,h,a):
    mu,ha=p[0],p[1]
    ah=p[2+idx[h]] if h in idx else 0.0; aa=p[2+idx[a]] if a in idx else 0.0
    dh=p[2+n+idx[h]] if h in idx else 0.0; da=p[2+n+idx[a]] if a in idx else 0.0
    return math.exp(mu+ha+ah-da), math.exp(mu+aa-dh)

def logpois(k,l): return k*math.log(l)-l-gammaln(k+1)

def markets(lh,la):
    def pmf(l):
        out=[];k=0;c=0
        while True:
            v=math.exp(logpois(k,l)); out.append(v); c+=v; k+=1
            if 1-c<1e-7 and k>2: break
        return np.array(out)
    ph,pa=pmf(lh),pmf(la); M=np.outer(ph,pa)
    tail=1-M.sum()
    hw=np.tril(M,-1).sum(); aw=np.triu(M,1).sum(); dr=np.trace(M)
    btts=(1-math.exp(-lh))*(1-math.exp(-la)); s=lh+la
    u25=math.exp(-s)*(1+s+s*s/2); o25=1-u25
    return dict(H=hw,D=dr,A=aw,BTTS=btts,O25=o25,U25=u25,tail=tail,sum1x2=hw+dr+aw)

def run(cur):
    use,data,dup,issues,allm,excl=load(cur)
    N=len(data); teams_all=sorted({r[1] for r in data}|{r[2] for r in data})
    cut0=int(N*0.5); test0=int(N*0.9)
    blocks=[(cut0+int((test0-cut0)*k/4), cut0+int((test0-cut0)*(k+1)/4)) for k in range(4)]
    sel={}
    for al in ALPHAS:
        tot=0;cnt=0;ok=True
        for b0,b1 in blocks:
            tr=data[:b0]; te=data[b0:b1]
            teams=sorted({r[1] for r in tr}|{r[2] for r in tr})
            res,idx=fit(tr,teams,al)
            if not res.success and 'ABNORMAL' in str(res.message): ok=False
            for r in te:
                lh,la=lam(res.x,idx,len(teams),r[1],r[2])
                tot+=-(logpois(r[3],lh)+logpois(r[4],la)); cnt+=1
        sel[al]=(tot/cnt,cnt,ok)
    best=min(ALPHAS,key=lambda a:(round(sel[a][0],10),-a))
    # unberuehrter Test: auf ersten 90 % mit gewaehltem alpha trainieren
    tr=data[:test0]; te=data[test0:]
    teams=sorted({r[1] for r in tr}|{r[2] for r in tr}); res,idx=fit(tr,teams,best)
    base={'H':np.mean([r[3]>r[4] for r in tr]),'A':np.mean([r[3]<r[4] for r in tr]),
          'BTTS':np.mean([r[3]>0 and r[4]>0 for r in tr]),'O25':np.mean([r[3]+r[4]>2 for r in tr])}
    ev={k:[] for k in base}
    for r in te:
        lh,la=lam(res.x,idx,len(teams),r[1],r[2]); m=markets(lh,la)
        obs={'H':r[3]>r[4],'A':r[3]<r[4],'BTTS':r[3]>0 and r[4]>0,'O25':r[3]+r[4]>2}
        for k in ev: ev[k].append((m[k],float(obs[k])))
    test={}
    for k,v in ev.items():
        p=np.array([a for a,b in v]); y=np.array([b for a,b in v]); pc=np.clip(p,1e-12,1-1e-12)
        bri=(p-y)**2; ll=-(y*np.log(pc)+(1-y)*np.log(1-pc))
        bb=base[k]; bri0=np.mean((bb-y)**2); ll0=np.mean(-(y*math.log(bb)+(1-y)*math.log(1-bb)))
        groups=[]
        for lo,hi in [(0,.2),(.2,.4),(.4,.6),(.6,.8),(.8,1.0001)]:
            mk=(p>=lo)&(p<hi)
            if mk.sum(): 
                fr=y[mk].mean(); se=math.sqrt(fr*(1-fr)/mk.sum())
                groups.append([lo,round(hi,1),int(mk.sum()),round(float(p[mk].mean()),3),round(float(fr),3),round(se,3)])
        test[k]=dict(n=len(v),brier=round(float(bri.mean()),4),brier_se=round(float(bri.std(ddof=1)/math.sqrt(len(v))),4),
                     logloss=round(float(ll.mean()),4),brier_base=round(float(bri0),4),logloss_base=round(float(ll0),4),groups=groups)
    # Endmodell auf allen Vorabspielen
    resF,idxF=fit(data,teams_all,best)
    n=len(teams_all); p=resF.x
    final=dict(success=bool(resF.success),msg=str(resF.message),mu=p[0],home=p[1],
               sum_att=float(p[2:2+n].sum()),sum_def=float(p[2+n:].sum()))
    return dict(league=cur,seasons=use,n_train=N,dup=dup,excluded_ko=len(excl),issues=issues,first=data[0][0],last=data[-1][0],
                split=dict(fit_start_n=cut0,blocks=blocks,test_start=test0,test_from=data[test0][0]),
                alpha_scores={str(a):[round(sel[a][0],5),sel[a][1],sel[a][2]] for a in ALPHAS},alpha=best,
                test=test,final=final,params=dict(p=p.tolist(),teams=teams_all))
if __name__=='__main__':
    out={}
    for cur in [c for c in sys.argv[2:]] or list(S):
        r=run(cur); out[cur]=r
        print(cur,'N',r['n_train'],'dup',r['dup'],'iss',len(r['issues']),'alpha',r['alpha'],{k:v[0] for k,v in r['alpha_scores'].items()},
              'fit',r['final']['success'],'sum',round(r['final']['sum_att'],6),round(r['final']['sum_def'],6),
              'test',{k:(v['brier'],v['brier_base']) for k,v in r['test'].items()},flush=True)
    json.dump(out,open('../models.json','w'),default=float)
