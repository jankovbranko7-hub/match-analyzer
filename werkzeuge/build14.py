import sys,json,math,datetime; sys.path.insert(0,'.')
import numpy as np, fs
from model import markets, ko_rounds
DAY,TAG=sys.argv[1],sys.argv[2]
CFG=json.load(open(f'../batches_{TAG}.json'))
M=json.load(open(f'../models_{TAG}.json'))
T_DEC=int(open(f'../tdec_{TAG}').read())
BATCH=CFG['batches']
NAT=CFG.get('nat',[])
tm=fs.get('todays-matches',date=DAY,timezone='UTC')
tmfetch=json.load(open([f for f in __import__('glob').glob('../cache/todays-matches__*.json') if json.load(open(f))['params_redacted'].startswith('date='+DAY)][0]))['fetched_utc']
TM={m['id']:m for m in tm['data']}
def U(t): return datetime.datetime.fromtimestamp(t,datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
def f2(x): return 'fehlt' if x is None else f'{x:.2f}'
def pc(a,n): return 'fehlt' if n==0 else f'{100*a/n:.0f} %'
def stats(rows,tid):
    n=len(rows); g=c=w=d=l=bt=o=un=cs=fts=btl=0; xf=xa=0.0; nx=0
    for m in rows:
        h=m['homeID']==tid; gf=m['homeGoalCount'] if h else m['awayGoalCount']; ga=m['awayGoalCount'] if h else m['homeGoalCount']
        g+=gf;c+=ga; w+=gf>ga; d+=gf==ga; l+=gf<ga; b=gf>0 and ga>0; bt+=b; o+=gf+ga>2; un+=gf+ga<3; cs+=ga==0; fts+=gf==0; btl+=b and gf<ga
        xa_,xb_=m.get('team_a_xg'),m.get('team_b_xg')
        if isinstance(xa_,(int,float)) and isinstance(xb_,(int,float)) and xa_>=0 and xb_>=0:
            nx+=1; xf+=xa_ if h else xb_; xa+=xb_ if h else xa_
    return dict(n=n,g=g,c=c,gpm=g/n if n else None,cpm=c/n if n else None,xf=xf/nx if nx else None,xa=xa/nx if nx else None,nx=nx,
                w=w,d=d,l=l,ppg=(3*w+d)/n if n else None,bt=pc(bt,n),o=pc(o,n),u=pc(un,n),cs=pc(cs,n),fts=pc(fts,n),btl=pc(btl,n))
def table(name,cols):
    keys=['Gesamt','Heim','Auswärts','letzte 6']
    L=[f'**{name}**','',' | '.join(['Kennzahl']+keys),' | '.join(['---']*5)]
    R=[('Spiele','n'),('Tore','g'),('Gegentore','c'),('Tore/Spiel','gpm'),('Gegentore/Spiel','cpm'),('xG für/Spiel','xf'),('xG gegen/Spiel','xa'),('Spiele mit xG','nx'),
       ('S/U/N',None),('Punkte/Spiel','ppg'),('BTTS %','bt'),('Over 2,5 %','o'),('Under 2,5 %','u'),('Clean Sheets %','cs'),('Failed to Score %','fts'),('BTTS-and-lose %','btl'),('AVG_2hg',None)]
    for lab,k in R:
        vals=[]
        for c in keys:
            s=cols[c]
            if lab=='S/U/N': v=f"{s['w']}/{s['d']}/{s['l']}"
            elif lab=='AVG_2hg': v='fehlt'
            else:
                v=s[k]; v=f2(v) if isinstance(v,float) or v is None else str(v)
            vals.append(v)
        L.append(' | '.join([lab]+vals))
    return '\n'.join(L)
out={}
for bi,b in enumerate(BATCH,1):
  for ni,mid in enumerate(b,1):
    if mid is None: continue
    m=TM[mid]; cur=str(m['competition_id']); mod=M[cur]
    r=fs.get('league-matches',season_id=int(cur),max_per_page=1000,page=1)
    KO=ko_rounds(r['data'])
    done=[x for x in r['data'] if x['status']=='complete' and x['date_unix']<T_DEC and x['roundID'] not in KO]
    nko=sum(1 for x in r['data'] if x['status']=='complete' and x['date_unix']<T_DEC and x['roundID'] in KO)
    tgt=[x for x in r['data'] if x['id']==mid][0]
    ppg={}
    for x in done:
        for t in (x['homeID'],x['awayID']): ppg.setdefault(t,[])
    teamrows={t:[x for x in done if t in (x['homeID'],x['awayID'])] for t in ppg}
    PPG={t:stats(v,t)['ppg'] for t,v in teamrows.items()}
    names={}
    for x in r['data']: names[x['homeID']]=x['home_name']; names[x['awayID']]=x['away_name']
    sec=[]; info={}
    for side,tid in (('Heim',m['homeID']),('Gast',m['awayID'])):
        rows=sorted(teamrows.get(tid,[]),key=lambda x:x['date_unix'])
        hr=[x for x in rows if x['homeID']==tid]; ar=[x for x in rows if x['awayID']==tid]; l6=rows[-6:]
        cols={'Gesamt':stats(rows,tid),'Heim':stats(hr,tid),'Auswärts':stats(ar,tid),'letzte 6':stats(l6,tid)}
        L6=[]
        for x in l6:
            h=x['homeID']==tid; opp=x['awayID'] if h else x['homeID']
            gf=x['homeGoalCount'] if h else x['awayGoalCount']; ga=x['awayGoalCount'] if h else x['homeGoalCount']
            L6.append(f"{datetime.datetime.utcfromtimestamp(x['date_unix']).strftime('%d.%m.')} {'H' if h else 'A'} {names.get(opp,opp)} ({f2(PPG.get(opp))} PPG) {gf}:{ga}")
        dist=[ (x['homeGoalCount'] if x['homeID']==tid else x['awayGoalCount']) for x in rows]
        info[side]=dict(id=tid,name=m['home_name'] if side=='Heim' else m['away_name'],cols=cols,l6=L6,dist=dist,
                        period=(U(rows[0]['date_unix'])[:10],U(rows[-1]['date_unix'])[:10]) if rows else None,
                        l6period=(U(l6[0]['date_unix'])[:10],U(l6[-1]['date_unix'])[:10]) if l6 else None)
    nat={}
    if cur=='17128':
        for side,tid in (('Heim',m['homeID']),('Gast',m['awayID'])):
            nat[side]=None
            for sid in NAT:
                rr=fs.get('league-matches',season_id=sid,max_per_page=1000,page=1)['data']
                KO2=ko_rounds(rr)
                rows=sorted([x for x in rr if x['status']=='complete' and x['date_unix']<T_DEC and x['roundID'] not in KO2 and tid in (x['homeID'],x['awayID'])],key=lambda x:x['date_unix'])
                if rows:
                    hr=[x for x in rows if x['homeID']==tid]; ar=[x for x in rows if x['awayID']==tid]
                    nm=m['home_name'] if side=='Heim' else m['away_name']
                    nat[side]=dict(sid=sid,period=(U(rows[0]['date_unix'])[:10],U(rows[-1]['date_unix'])[:10]),
                        table=table(f"{nm} – Landesliga (Saison-ID {sid}, {U(rows[0]['date_unix'])[:10]} bis {U(rows[-1]['date_unix'])[:10]})",{'Gesamt':stats(rows,tid),'Heim':stats(hr,tid),'Auswärts':stats(ar,tid),'letzte 6':stats(rows[-6:],tid)}),
                        cols={'Gesamt':stats(rows,tid),'Heim':stats(hr,tid),'Auswärts':stats(ar,tid),'letzte 6':stats(rows[-6:],tid)})
                    break
    p=np.array(mod['params']['p']); teams=mod['params']['teams']; n=len(teams); idx={t:i for i,t in enumerate(teams)}
    att=p[2:2+n]-p[2:2+n].mean(); de=p[2+n:]-p[2+n:].mean(); mu=p[0]+p[2:2+n].mean()-p[2+n:].mean(); ha=p[1]
    h,a=m['homeID'],m['awayID']
    px=np.array(mod['params_xg']['p']); attx=px[2:2+n]-px[2:2+n].mean(); dex=px[2+n:]-px[2+n:].mean(); mux=px[0]+px[2:2+n].mean()-px[2+n:].mean(); hax=px[1]
    if h in idx and a in idx:
        lh=math.exp(mu+ha+att[idx[h]]-de[idx[a]]); la=math.exp(mu+att[idx[a]]-de[idx[h]]); mk=markets(lh,la)
        lhx=math.exp(mux+hax+attx[idx[h]]-dex[idx[a]]); lax=math.exp(mux+attx[idx[a]]-dex[idx[h]]); mkx=markets(lhx,lax)
        mk_tor=dict(mk); mk=dict(H=mk_tor['H'],D=mk_tor['D'],A=mk_tor['A'],BTTS=mkx['BTTS'],O25=mkx['O25'],U25=mkx['U25'],sum1x2=mk_tor['sum1x2'],tail=max(mk_tor['tail'],mkx['tail']))
    else: lh=la=lhx=lax=None; mk=mk_tor=mkx=None
    odds={k:m.get(k) for k in ['odds_ft_1','odds_ft_x','odds_ft_2','odds_btts_yes','odds_btts_no','odds_ft_over25','odds_ft_under25']}
    ok=lambda v: isinstance(v,(int,float)) and v>1
    mkt={}
    if all(ok(odds[k]) for k in ['odds_ft_1','odds_ft_x','odds_ft_2']):
        t=sum(1/odds[k] for k in ['odds_ft_1','odds_ft_x','odds_ft_2']); mkt.update(H=(1/odds['odds_ft_1'])/t,D=(1/odds['odds_ft_x'])/t,A=(1/odds['odds_ft_2'])/t)
    if ok(odds['odds_btts_yes']) and ok(odds['odds_btts_no']):
        mkt['BTTS']=(1/odds['odds_btts_yes'])/(1/odds['odds_btts_yes']+1/odds['odds_btts_no'])
    if ok(odds['odds_ft_over25']) and ok(odds['odds_ft_under25']):
        po=(1/odds['odds_ft_over25'])/(1/odds['odds_ft_over25']+1/odds['odds_ft_under25']); mkt['O25']=po; mkt['U25']=1-po
    out[f'{bi}.{ni}']=dict(mid=mid,comp=cur,season=m['season'],gw=m.get('game_week'),kick=U(m['date_unix']),status=m['status'],
        home=m['home_name'],away=m['away_name'],hid=h,aid=a,lh=lh,la=la,lhx=lhx,lax=lax,mk=mk,mk_tor=mk_tor,mk_xg=mkx,mkt=mkt,xg_cov=mod.get('xg_coverage'),odds=odds,odds_fetch=tmfetch,info=info,
        tables=table(f"{m['home_name']} (Heim, ID {h})",info['Heim']['cols'])+'\n\n'+table(f"{m['away_name']} (Gast, ID {a})",info['Gast']['cols']),
        stadium=m.get('stadium_name'),nha=m.get('no_home_away'),nko=nko,nat=nat)
json.dump(out,open(f'../matches_{TAG}.json','w'),default=float)
for k,v in out.items():
    I=v['info']
    print(f"\n### {k} {v['home']} – {v['away']} | {v['kick']} | {v['comp']} | GW {v['gw']} | lam {f2(v['lh'])}/{f2(v['la'])}")
    if v['mk']: print('  P(v1.4): H %.2f D %.2f A %.2f BTTS %.2f O25 %.2f'%(v['mk']['H'],v['mk']['D'],v['mk']['A'],v['mk']['BTTS'],v['mk']['O25']),'| Markt',{k:round(x,2) for k,x in v['mkt'].items()},'| odds',[v['odds'][x] for x in v['odds']])
    for s in ('Heim','Gast'):
        c=I[s]['cols']
        for col in ('Gesamt','Heim' if s=='Heim' else 'Auswärts','letzte 6'):
            x=c[col]; print(f"  {s[0]} {col[:4]}: n{x['n']} {x['g']}:{x['c']} xG {f2(x['xf'])}/{f2(x['xa'])}({x['nx']}) {x['w']}-{x['d']}-{x['l']} ppg {f2(x['ppg'])} btts {x['bt']} o25 {x['o']} cs {x['cs']} fts {x['fts']} btl {x['btl']}")
        print('   L6:',' ; '.join(I[s]['l6'])); print('   Torverteilung:',I[s]['dist'])
        nt=v['nat'].get(s) if v['nat'] else None
        if v['nat']:
            if nt:
                for col in ('Gesamt','Heim' if s=='Heim' else 'Auswärts','letzte 6'):
                    x=nt['cols'][col]; print(f"   LIGA {nt['sid']} {col[:4]}: n{x['n']} {x['g']}:{x['c']} xG {f2(x['xf'])}/{f2(x['xa'])} {x['w']}-{x['d']}-{x['l']} ppg {f2(x['ppg'])} btts {x['bt']} o25 {x['o']} cs {x['cs']} fts {x['fts']}")
            else: print('   LIGA: fehlt (Landesliga nicht im Abo)')
