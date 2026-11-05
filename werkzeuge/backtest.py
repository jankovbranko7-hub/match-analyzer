import sys,json,math; sys.path.insert(0,'.')
import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy.special import gammaln
import fs
from model import ko_rounds
T=int(open('../tdec_1104').read())
S=json.load(open('../seasons.json'))
ALPHAS=[0.1,1,10,100]; XIS=[0.0,0.0005,0.001,0.002,0.004]
def load(cur):
    ids=[s for s,y in S[cur]]; i=ids.index(int(cur)); rows={}
    for sid in ids[max(0,i-3):i+1]:
        try: d=fs.get('league-matches',season_id=sid,max_per_page=1000,page=1)['data']
        except (LookupError,SystemExit): return None
        KO=ko_rounds(d)
        for m in d:
            if m['status']!='complete' or m['date_unix']>=T or m['roundID'] in KO: continue
            hg,ag=m['homeGoalCount'],m['awayGoalCount']
            if not(isinstance(hg,int) and isinstance(ag,int) and hg>=0 and ag>=0): continue
            od=lambda k: m.get(k) if isinstance(m.get(k),(int,float)) and m.get(k)>1 else None
            rows[m['id']]=(m['date_unix'],m['homeID'],m['awayID'],hg,ag,dict(h=od('odds_ft_1'),d=od('odds_ft_x'),a=od('odds_ft_2'),by=od('odds_btts_yes'),bn=od('odds_btts_no'),o=od('odds_ft_over25'),u=od('odds_ft_under25')))
    return sorted(rows.values(),key=lambda r:r[0])
def fit(tr,alpha,xi):
    teams=sorted({r[1] for r in tr}|{r[2] for r in tr}); idx={t:i for i,t in enumerate(teams)}; n=len(teams)
    H=np.array([idx[r[1]] for r in tr]); A=np.array([idx[r[2]] for r in tr]); X=np.array([r[3] for r in tr],float); Y=np.array([r[4] for r in tr],float)
    tref=tr[-1][0]; W=np.exp(-xi*(tref-np.array([r[0] for r in tr]))/86400.0)
    def f(p):
        mu,ha=p[0],p[1]; att=p[2:2+n]; de=p[2+n:]
        lh=mu+ha+att[H]-de[A]; la=mu+att[A]-de[H]; eh,ea=np.exp(lh),np.exp(la)
        v=np.sum(W*(eh-X*lh))+np.sum(W*(ea-Y*la))+alpha*(np.sum(att**2)+np.sum(de**2))
        g=np.zeros_like(p); rh=W*(eh-X); ra=W*(ea-Y); g[0]=rh.sum()+ra.sum(); g[1]=rh.sum()
        ga=np.zeros(n); gd=np.zeros(n); np.add.at(ga,H,rh); np.add.at(ga,A,ra); np.add.at(gd,A,-rh); np.add.at(gd,H,-ra)
        g[2:2+n]=ga+2*alpha*att; g[2+n:]=gd+2*alpha*de; return v,g
    p0=np.zeros(2+2*n); p0[0]=math.log(max((X.mean()+Y.mean())/2,0.1))
    p=minimize(f,p0,jac=True,method='L-BFGS-B',options={'maxiter':3000}).x
    def lam(h,a):
        ah=p[2+idx[h]] if h in idx else 0; aa=p[2+idx[a]] if a in idx else 0; dh=p[2+n+idx[h]] if h in idx else 0; da=p[2+n+idx[a]] if a in idx else 0
        return math.exp(p[0]+p[1]+ah-da), math.exp(p[0]+aa-dh)
    return lam
def lp(k,l): return k*math.log(l)-l-gammaln(k+1)
def score(lam,te): return np.mean([-(lp(r[3],lam(r[1],r[2])[0])+lp(r[4],lam(r[1],r[2])[1])) for r in te])
def mkts(lh,la,rho=0.0):
    K=12; ph=np.array([math.exp(lp(i,lh)) for i in range(K)]); pa=np.array([math.exp(lp(j,la)) for j in range(K)]); M=np.outer(ph,pa)
    if rho: M[0,0]*=1-lh*la*rho; M[0,1]*=1+lh*rho; M[1,0]*=1+la*rho; M[1,1]*=1-rho
    M=M/M.sum()
    i,j=np.indices(M.shape)
    return dict(H=M[i>j].sum(),A=M[i<j].sum(),BTTS=M[(i>0)&(j>0)].sum(),O25=M[i+j>2].sum())
def fit_rho(lam,tr):
    L=[(lam(r[1],r[2]),r[3],r[4]) for r in tr if r[3]<=1 and r[4]<=1]
    def nl(rho):
        s=0
        for (lh,la),x,y in L:
            t={(0,0):1-lh*la*rho,(0,1):1+lh*rho,(1,0):1+la*rho,(1,1):1-rho}[(x,y)]
            if t<=0: return 1e9
            s-=math.log(t)
        return s
    return minimize_scalar(nl,bounds=(-0.25,0.25),method='bounded').x
def run(cur):
    data=load(cur)
    if not data or len(data)<400: return None
    N=len(data); c0=int(N*.5); t0=int(N*.9); bl=[(c0+int((t0-c0)*k/4),c0+int((t0-c0)*(k+1)/4)) for k in range(4)]
    asc={a:np.mean([score(fit(data[:b0],a,0),data[b0:b1]) for b0,b1 in bl]) for a in ALPHAS}; al=min(ALPHAS,key=lambda a:(round(asc[a],10),-a))
    xsc={x:np.mean([score(fit(data[:b0],al,x),data[b0:b1]) for b0,b1 in bl]) for x in XIS}; xi=min(XIS,key=lambda x:(round(xsc[x],10),x))
    tr=data[:t0]; te=data[t0:]
    lb=fit(tr,al,0); ld=fit(tr,al,xi); rb=fit_rho(lb,tr); rd=fit_rho(ld,tr)
    out=[]
    for r in te:
        h,a=r[3],r[4]; y=dict(H=h>a,A=a>h,BTTS=h>0 and a>0,O25=h+a>2); o=r[5]
        mk=None
        if o['h'] and o['d'] and o['a'] and o['by'] and o['bn'] and o['o'] and o['u']:
            s1=1/o['h']+1/o['d']+1/o['a']; s2=1/o['by']+1/o['bn']; s3=1/o['o']+1/o['u']
            mk=dict(H=(1/o['h'])/s1,A=(1/o['a'])/s1,BTTS=(1/o['by'])/s2,O25=(1/o['o'])/s3)
        out.append(dict(y=y,odds=o,base=mkts(*lb(r[1],r[2])),dc=mkts(*lb(r[1],r[2]),rb),decay=mkts(*ld(r[1],r[2])),both=mkts(*ld(r[1],r[2]),rd),market=mk))
    return dict(league=cur,N=N,alpha=al,xi=xi,rho_base=rb,rho_decay=rd,test=out)
if __name__=='__main__':
    res={}
    for cur in S:
        if cur in ('17180','17157'): continue
        r=run(cur)
        if r: res[cur]=r; print(cur,'N',r['N'],'alpha',r['alpha'],'xi',r['xi'],'rho',round(r['rho_base'],3),flush=True)
    json.dump(res,open('../backtest.json','w'),default=float)
