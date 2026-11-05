import json,glob,math,sys
DAY,TAG,FETCHDAY,PREV=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4].split(',')
D=f'/home/user/match-analyzer/protokoll/{DAY}/ergebnis'
import os; os.makedirs(D,exist_ok=True)
E=json.load(open(f'../evaluation_{TAG}.json')); R=json.load(open(f'../results_{TAG}.json'))
fetch=sorted(json.load(open(f))['fetched_utc'] for f in glob.glob('../cache/match__*.json') if json.load(open(f))['fetched_utc']>=FETCHDAY)
open(f'{D}/abrufe.txt','w').write(''.join(l for l in open('../cache/_requests.log') if '/match?' in l and l>=FETCHDAY))
json.dump(dict(abruf_utc_von=fetch[0],abruf_utc_bis=fetch[-1],quelle='FootyStats API, Endpunkt match',ergebnisse=R),open(f'{D}/ergebnisse.json','w'),ensure_ascii=False,indent=1)
json.dump(E,open(f'{D}/auswertung.json','w'),ensure_ascii=False,indent=1)
pc=lambda x:f'{100*x:.0f} %'
def wilson(k,n,z=1.96):
    p=k/n; c=(p+z*z/(2*n))/(1+z*z/n); w=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n); return (c-w,c+w)
def blk(t,s):
    w=s['wilson']
    if not s['n']: return [f'**{t}:** keine abgerechneten Tipps.','']
    return [f'**{t}:** {s["n"]} abgerechnete Tipps, {s["treffer"]} Treffer, {s["n"]-s["treffer"]} Nieten, Trefferanteil {pc(s["quote"])} (95-%-Wilson-Intervall {pc(w[0])}–{pc(w[1])}); hypothetisch 1 Einheit je Tipp zu den Vorab-Quoten: Gewinn {s["gewinn"]:+.2f} Einheiten, ROI {pc(s["roi"])} vor Kosten (Netto-Rendite: fehlt); Brier {s["brier"]:.3f}, Log-Loss {s["logloss"]:.3f}'+(f'; Markterwartung (margenbereinigt) {pc(s["markt_erwartung"])} bei {s["n_markt"]} Tipps, Treffer über Markterwartung {100*(s["quote"]-s["markt_erwartung"]):+.0f} Prozentpunkte' if s.get('markt_erwartung') is not None else '')+'.','']
d=DAY.split('-'); dd=f'{d[2]}.{d[1]}.{d[0]}'
L=[f'# Ergebnisprüfung {dd} (Abschnitt 10)','',f'- Gewertete Revision: r1. Ergebnisabruf: FootyStats `match`, {fetch[0][:16].replace("T"," ")}–{fetch[-1][11:16]} UTC, getrennt vom Vorabeintrag gespeichert.',
   '- Abrechnung: reguläre Spielzeit einschließlich Nachspielzeit (keine Verlängerung). „keine“ zählt weder als Treffer noch als Verlust. Einsätze hypothetisch.','',
   '## Bericht Tipps ohne ⚠️','','Nr. | Spiel | Ergebnis | Auswahl | Modell | Quote | Ergebnis','---|---|---|---|---|---|---']
rows=E['rows']
for x in rows:
    if x['auswahl']!='keine' and not x['warn']: L.append(f"{x['nr']} | {x['spiel']} | {x['ergebnis']} | {x['auswahl']} | {pc(x['p'])} | {x['quote']} | {x['res']}")
L+=['']+blk('Ohne ⚠️',E['ohne_warn'])
n=k=0; g=0.0
for p in PREV+[f'{DAY}']:
    a=json.load(open(f'/home/user/match-analyzer/protokoll/{p}/ergebnis/auswertung.json'))['ohne_warn'] if p!=DAY else E['ohne_warn']
    n+=a['n']; k+=a['treffer']; g+=a['gewinn']
w=wilson(k,n)
L+=[f'**Kumuliert ohne ⚠️ ({", ".join(PREV+[DAY])}):** {k}/{n} Treffer ({pc(k/n)}, 95-%-Intervall {pc(w[0])}–{pc(w[1])}); hypothetisch {g:+.2f} Einheiten, ROI {pc(g/n)} vor Kosten.','']
L+=['## Vollständiges Auswahlprotokoll','','Nr. | Spiel | Ergebnis | Auswahl | ⚠️ | Modell | Quote | Ergebnis','---|---|---|---|---|---|---|---']
for x in rows: L.append(f"{x['nr']} | {x['spiel']} | {x['ergebnis']} | {x['auswahl']} | {'⚠️' if x['warn'] else ''} | {pc(x['p']) if x['p'] else '–'} | {x['quote'] or '–'} | {x['res']}")
L+=['']+blk('Mit ⚠️',E['mit_warn'])+blk('Alle Tipps',E['alle_tipps'])+(blk('Gruppe „Modell über Markt“ (> 5 Prozentpunkte)',E['modell_ueber_markt'])+blk('Übrige Tipps',E['uebrige']) if E.get('modell_ueber_markt',{}).get('n') else [])+[f"**„keine“:** {E['keine']} Spiele.",'','## Prognosegüte aller vorab berechneten Wahrscheinlichkeiten','','Markt | n | Brier | Log-Loss | Ø Prognose | beobachtet','---|---|---|---|---|---']
names={'H':'Heimsieg','A':'Auswärtssieg','BTTS':'BTTS Ja','O25':'Over 2,5'}
for kk,c in E['alle_prognosen'].items(): L.append(f"{names[kk]} | {c['n']} | {c['brier']:.3f} | {c['logloss']:.3f} | {pc(c['mittel_p'])} | {pc(c['beobachtet'])}")
L+=['','Hinweis: Sehr kleine Stichprobe; aus diesen Ergebnissen werden keine neuen Regeln abgeleitet.']
open(f'{D}/auswertung.md','w').write('\n'.join(L)+'\n')
print(f'kumuliert {k}/{n} {g:+.2f}')
