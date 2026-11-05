# Auswertung (Abschnitt 10, v1.4): python3 -I evaluate14.py <protokoll/TAG-Ordner> <TAG>
import sys,json,math
V=json.load(open(sys.argv[1]+'/vorab.json'))['matches']; TAG=sys.argv[2]
R=json.load(open(f'../results_{TAG}.json'))
OK={'Heimsieg':('H','odds_ft_1',lambda h,a:h>a),'Auswärtssieg':('A','odds_ft_2',lambda h,a:a>h),'BTTS Ja':('BTTS','odds_btts_yes',lambda h,a:h>0 and a>0),
    'Over 2,5':('O25','odds_ft_over25',lambda h,a:h+a>2),'Under 2,5':('U25','odds_ft_under25',lambda h,a:h+a<3)}
def wilson(k,n,z=1.96):
    if n==0: return None
    p=k/n; c=(p+z*z/(2*n))/(1+z*z/n); w=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n); return (c-w,c+w)
rows=[]
for k,v in V.items():
    s=v['selection']
    if not v.get('match_id'):
        rows.append(dict(nr=k,spiel=f"{v['home']} – {v['away']}",match_id=None,ergebnis='–',status='Identität ungeklärt',auswahl='keine',warn=False,p=None,quote=None,p_markt=None,ueber_markt=False,res='keine (nicht gezählt)')); continue
    r=R[k]; st=r['status']
    if s=='keine': res='keine (nicht gezählt)'
    elif st!='complete': res=f'nicht abgerechnet (Status {st}; Marktregeln nicht erfasst)'
    else: res='Treffer' if OK[s][2](r['hg'],r['ag']) else 'Niete'
    p=v['probs'][OK[s][0]] if s in OK else None; q=v['odds'][OK[s][1]] if s in OK else None
    pm=(v.get('markt') or {}).get(OK[s][0]) if s in OK else None
    rows.append(dict(nr=k,spiel=f"{v['home']} – {v['away']}",match_id=v['match_id'],ergebnis=f"{r['hg']}:{r['ag']}",status=st,auswahl=s,warn=bool(v['warning']),p=p,quote=q,p_markt=pm,ueber_markt=bool(v.get('modell_ueber_markt')),res=res))
def summary(sel):
    S=[x for x in sel if x['res'] in ('Treffer','Niete')]; n=len(S); k=sum(x['res']=='Treffer' for x in S)
    prof=sum((x['quote']-1) if x['res']=='Treffer' else -1 for x in S if x['quote'] and x['quote']>1); nq=sum(1 for x in S if x['quote'] and x['quote']>1)
    br=sum((x['p']-(x['res']=='Treffer'))**2 for x in S)/n if n else None
    ll=-sum(math.log(x['p'] if x['res']=='Treffer' else 1-x['p']) for x in S)/n if n else None
    M=[x['p_markt'] for x in S if x['p_markt'] is not None]
    return dict(n=n,treffer=k,quote=k/n if n else None,wilson=wilson(k,n),gewinn=prof,roi=prof/nq if nq else None,n_quote=nq,brier=br,logloss=ll,
                markt_erwartung=(sum(M)/len(M)) if M else None,n_markt=len(M),modell_mittel=(sum(x['p'] for x in S)/n) if n else None)
tips=[x for x in rows if x['auswahl']!='keine']
out=dict(ohne_warn=summary([x for x in tips if not x['warn']]),mit_warn=summary([x for x in tips if x['warn']]),alle_tipps=summary(tips),
         modell_ueber_markt=summary([x for x in tips if x['ueber_markt']]),uebrige=summary([x for x in tips if not x['ueber_markt']]),
         keine=sum(x['auswahl']=='keine' for x in rows),rows=rows)
cal={}
for mk,f in [('H',lambda h,a:h>a),('A',lambda h,a:a>h),('BTTS',lambda h,a:h>0 and a>0),('O25',lambda h,a:h+a>2)]:
    P=[(V[k]['probs'][mk],float(f(R[k]['hg'],R[k]['ag']))) for k in V if k in R and R[k]['status']=='complete']
    if P: cal[mk]=dict(n=len(P),brier=sum((p-y)**2 for p,y in P)/len(P),logloss=-sum(math.log(p if y else 1-p) for p,y in P)/len(P),beobachtet=sum(y for p,y in P)/len(P),mittel_p=sum(p for p,y in P)/len(P))
out['alle_prognosen']=cal
json.dump(out,open(f'../evaluation_{TAG}.json','w'),ensure_ascii=False,indent=1)
for x in rows: print(x['nr'],x['spiel'],x['ergebnis'],x['auswahl'],'⚠️' if x['warn'] else '','MüM' if x['ueber_markt'] else '',x['quote'],x['res'])
for k in ['ohne_warn','mit_warn','alle_tipps','modell_ueber_markt','uebrige']: print(k,{a:b for a,b in out[k].items() if a in ('n','treffer','gewinn','markt_erwartung')})
