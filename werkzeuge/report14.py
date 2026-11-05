import sys,json,datetime,os,shutil; sys.path.insert(0,'.'); sys.path.insert(0,'..')
import importlib
DAY,TAG,OUT0=sys.argv[1],sys.argv[2],sys.argv[3]
D=importlib.import_module(f'decisions_{TAG}').D
CFG=json.load(open(f'../batches_{TAG}.json'))
M=json.load(open(f'../matches_{TAG}.json')); MOD=json.load(open(f'../models_{TAG}.json')); T=int(open(f'../tdec_{TAG}').read())
OUT=OUT0; os.makedirs(OUT,exist_ok=True)
NOW=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
U=lambda t: datetime.datetime.fromtimestamp(t,datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
LN={'17171':'Belgien Pro League','17128':'UEFA Champions League','17184':'England Championship','16714':'Ecuador Serie A','16533':'Paraguay División Profesional','17301':'Polen 1. Liga','16571':'Argentinien Primera División','16927':'Bolivien LFPB','16544':'Brasilien Série A','16783':'Brasilien Série B','16615':'Chile Primera División','16614':'Kolumbien Primera A','17088':'Bulgarien First League','17091':'Dänemark Superliga','17146':'England Premier League','17102':'Frankreich Ligue 1','17117':'Frankreich Ligue 2','17356':'Griechenland Super League','17084':'Italien Serie A','17110':'Niederlande Eerste Divisie','17112':'Polen Ekstraklasa','17217':'Portugal Liga Portugal','17215':'Portugal Liga Portugal 2','17119':'Serbien SuperLiga','17199':'Spanien La Liga','17269':'Spanien Segunda División','16576':'Schweden Allsvenskan','17265':'Türkei Süper Lig','17290':'Türkei 1. Lig'}
MK={'H':'Heimsieg','A':'Auswärtssieg','BTTS':'BTTS Ja','O25':'Over 2,5 / Under 2,5'}
def usable(c):
    t=MOD[c]['test']; r={}
    for k,x in t.items(): r[k]=not (x['brier']>x['brier_base'] and x['logloss']>x['logloss_base'])
    return r
def pct(x): return f'{100*x:.0f} %'
def q(v): return 'fehlt' if (v in (None,0,'0') or (isinstance(v,(int,float)) and v<=1)) else f'{v}'
DDE=f"{DAY[8:10]}.{DAY[5:7]}.{DAY[:4]}"
SYS='FootyStats-System v1.4 (Fassung v1.4-2026-11-05)'; MV='Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte)'
allj={}
for b in range(1,len(CFG['batches'])+1):
    L=[f'# Vorabeintrag Batch {b} · {DDE}','',f'- System: {SYS}',f'- Modell: {MV}',
       f'- Analysestichtag / Informationsstand (Daten-Snapshot): {U(T)}',f'- Eintrag erstellt: {NOW}',
       '- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.',
       '- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).',
       '- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.','']
    for n in range(1,6):
        k=f'{b}.{n}'
        if k not in M:
            sel,bild,warn=D[k]; hm,aw=CFG['missing'][k]; L+=[f'## {k} {hm} – {aw}','',f'**Bild:** {bild}','',f'**Auswahl:** {sel}','','---','']
            allj[k]=dict(home=hm,away=aw,match_id=None,selection=sel,warning=None,bild=bild,note='Spielidentität ungeklärt')
            continue
        m=M[k]; c=m['comp']; mo=MOD[c]; sel,bild,warn=D[k]; us=usable(c)
        aid=f"A-{DAY.replace('-','')}-{m['mid']}-r1"
        I=m['info']; nh=I['Heim']['cols']['Gesamt']['n']; na=I['Gast']['cols']['Gesamt']['n']
        xgmiss=[I[s]['name'] for s in ('Heim','Gast') if I[s]['cols']['Gesamt']['nx']<I[s]['cols']['Gesamt']['n']]
        natmiss=[I[sd]['name'] for sd in ('Heim','Gast') if m.get('nat') and not m['nat'].get(sd)]
        dstat='eingeschränkt' if (xgmiss or natmiss) else 'verwendbar'
        dgr=f"Saison {m['season']}: {nh} bzw. {na} Ligaspiele"+(f"; xG fehlt teilweise bei {', '.join(xgmiss)}" if xgmiss else '; xG für alle Spiele')+(f"; {m['nko']} K.-o.-/Play-off-Spiele der Saison ausgeschlossen" if m['nko'] else '')+(f"; Landesliga-Daten fehlen für {', '.join(natmiss)} (Liga nicht im API-Abo)" if natmiss else '')
        L+=[f"## {b}.{n} {m['home']} – {m['away']} | {m['kick']} | {LN[c]} {m['season']}, Spieltag {m['gw']} | Match-ID {m['mid']}",'',
            f"Analyse-ID: {aid} · Team-IDs: {m['hid']} / {m['aid']} · Saison-ID: {c} · Status beim Abruf: {m['status']} · Ort: {m['stadium'] or 'fehlt'}"+(' · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)' if m['nha'] else ''),'',
            f"Datenstand: {U(T)}; Datenbasis: {dstat} ({dgr}).",'',
            f"Zeitraum Saison: Heim {I['Heim']['period'][0]} bis {I['Heim']['period'][1]}, Gast {I['Gast']['period'][0]} bis {I['Gast']['period'][1]}; letzte 6: Heim {I['Heim']['l6period'][0]}–{I['Heim']['l6period'][1]}, Gast {I['Gast']['l6period'][0]}–{I['Gast']['l6period'][1]}.",'',
            m['tables'],'',*( ['**Landesliga-Daten (getrennt von der Champions League, andere Skala):**','']+[ (m['nat'][sd]['table'] if m['nat'].get(sd) else f"**{I[sd]['name']} – Landesliga:** fehlt (Liga nicht im API-Abo)") +'\n' for sd in ('Heim','Gast')] if m.get('nat') else []),
            f"Letzte 6 {m['home']}: "+' · '.join(I['Heim']['l6']),'',
            f"Letzte 6 {m['away']}: "+' · '.join(I['Gast']['l6']),'',
            f"Torverteilung Saison (eigene Tore je Spiel, chronologisch): {m['home']} {I['Heim']['dist']}; {m['away']} {I['Gast']['dist']}",'',
            f"**Bild:** {bild}",'']
        mk=m['mk']
        L+=[f"**Modell:** {MV}; alpha = {mo['alpha']} (zeitlich vorwärts gewählt); Training {mo['n_train']} Spiele, Saisons {mo['seasons']}; Schätzung Tormodell λ Heim {m['lh']:.3f}, λ Gast {m['la']:.3f}; xG-Variante λ Heim {m['lhx']:.3f}, λ Gast {m['lax']:.3f} (xG-Anteil im Training {(f"{100*m['xg_cov']:.0f} %") if m['xg_cov'] is not None else 'fehlt'}). "
            f"Prüfstand (unberührter Test, {mo['test']['H']['n']} Spiele ab {U(mo['split']['test_from'])[:10]}): "+'; '.join(f"{MK[x]} {'besser als Grundrate' if us[x] else 'nicht besser als Grundrate'} (Brier {mo['test'][x]['brier']} gegen {mo['test'][x]['brier_base']}{' – xG-Variante' if x in ('BTTS','O25') else ''})" for x in ['H','A','BTTS','O25'])+
            '. Grenzen: '+(f"{mo['excluded_ko']} K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; " if mo['excluded_ko'] else '')+'unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.',
            '',f"Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg {pct(mk['H'])} · Remis {pct(mk['D'])} · Auswärtssieg {pct(mk['A'])} · BTTS Ja {pct(mk['BTTS'])} · Over 2,5 {pct(mk['O25'])} · Under 2,5 {pct(mk['U25'])} (nur Tormodell: BTTS {pct(m['mk_tor']['BTTS'])}, Over 2,5 {pct(m['mk_tor']['O25'])})",'']
        o=m['odds']
        L+=[f"**Quote:** FootyStats `todays-matches`, Abruf {m['odds_fetch'][:16].replace('T',' ')} UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 {q(o['odds_ft_1'])} · X {q(o['odds_ft_x'])} · 2 {q(o['odds_ft_2'])} · BTTS Ja {q(o['odds_btts_yes'])} · Over 2,5 {q(o['odds_ft_over25'])} · Under 2,5 {q(o['odds_ft_under25'])}.",'',
            ]
        SK={'Heimsieg':'H','Auswärtssieg':'A','BTTS Ja':'BTTS','Over 2,5':'O25','Under 2,5':'U25'}.get(sel)
        mt=m['mkt']; dev=None
        if SK and SK in mt:
            dev=mk[SK]-mt[SK]; L+=[f"**Markt:** margenbereinigt {pct(mt[SK])} für {sel}; Modell {pct(mk[SK])}; Abweichung Modell − Markt {100*dev:+.0f} Prozentpunkte"+(' – **Modell über Markt** (Kennzeichnung, keine Sperre)' if dev>0.05 else '')+'.','']
        elif SK: L+=['**Markt:** fehlt (Quote unvollständig).','']
        else: L+=['**Markt:** '+(' · '.join(f"{n} {pct(mt[x])}" for n,x in [('Heim','H'),('Remis','D'),('Auswärts','A'),('BTTS','BTTS'),('Over','O25')] if x in mt) or 'fehlt')+' (margenbereinigt, informativ).','']
        L+=[f"**Auswahl:** {sel}"+('' if sel!='keine' else ' – Grund siehe Bild.'),'']
        if warn: L+=[f"⚠️ {warn}",'']
        L+=['---','']
        allj[k]=dict(analysis_id=aid,match_id=m['mid'],home=m['home'],away=m['away'],home_id=m['hid'],away_id=m['aid'],season_id=c,league=LN[c],kickoff_utc=m['kick'],
                     data_status=dstat,selection=sel,warning=warn,bild=bild,lambda_home=m['lh'],lambda_away=m['la'],probs={x:mk[x] for x in ['H','D','A','BTTS','O25','U25']},probs_tormodell={x:m['mk_tor'][x] for x in ['H','D','A','BTTS','O25','U25']},probs_xg={x:m['mk_xg'][x] for x in ['H','D','A','BTTS','O25','U25']},markt=mt,abweichung_modell_markt=dev,modell_ueber_markt=(dev is not None and dev>0.05),lambda_xg=(m['lhx'],m['lax']),
                     odds=o,odds_fetch_utc=m['odds_fetch'],model_alpha=mo['alpha'],market_usable=us)
    open(f'{OUT}/batch-{b}.md','w').write('\n'.join(L))
# Modellprüfstand
P=[f'# Modell-Prüfstand {DDE} · Stichtag {U(T)}','',f'Modell: {MV}. alpha aus {{0.1, 1, 10, 100}}: Training auf den ersten 50 % der chronologisch sortierten Spiele, Bewertung auf vier folgenden Blöcken bis 90 % (wachsendes Trainingsfenster), mittlerer negativer Poisson-Log-Score der Torpaare; bei Gleichstand größeres alpha. Unberührter Test: letzte 10 %, trainiert auf den ersten 90 % mit gewähltem alpha. Endmodell auf allen Vorabspielen. Grundrate = Trefferanteil im Trainingsteil. K.-o.-/Play-off-Runden (Spieltag 0) sind ausgeschlossen. Der Vergleich mit der Grundrate beschreibt Stärken und Schwächen, er ist keine Freigabehürde.','']
for c,mo in MOD.items():
    P+=[f"## {LN[c]} (Saison-ID {c})",'',f"Saisons {mo['seasons']}; {mo['n_train']} Spiele ({U(mo['first'])[:10]} bis {U(mo['last'])[:10]}); Duplikate {mo['dup']}; ungültige Werte {len(mo['issues'])}; Fit erfolgreich: {mo['final']['success']}; mu {mo['final']['mu']:.4f}; Heimvorteil {mo['final']['home']:.4f}.",
        f"alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {mo['alpha_scores']} → gewählt {mo['alpha']}.",'',
        'Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]','---|---|---|---|---|---|---']
    for x in ['H','A','BTTS','O25']:
        t=mo['test'][x]; P.append(f"{MK[x]} | {t['n']} | {t['brier']} (±{t['brier_se']}) | {t['brier_base']} | {t['logloss']} | {t['logloss_base']} | {t['groups']}")
    P.append('')
open(f'{OUT}/modell-pruefstand.md','w').write('\n'.join(P))
json.dump(dict(system=SYS,model=MV,snapshot_utc=U(T),created_utc=NOW,matches=allj),open(f'{OUT}/vorab.json','w'),ensure_ascii=False,indent=1,default=float)
open(f'{OUT}/abrufe.txt','w').write(''.join(l for l in open('../cache/_requests.log') if l>=open(f'../tdec_{TAG}_startiso').read().strip()))

print('ok')
