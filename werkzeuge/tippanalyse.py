# Auswertung aller ausgewerteten Tipps in tipps/sportsmole/ (Trefferquoten je Wettart, Kennzeichnung, Grenzfall,
# zweitbester Markt, Liga, verfehlte Tor-Tipps). Aufruf aus dem Repo-Wurzelordner: python3 -I werkzeuge/tippanalyse.py

import re,glob,unicodedata,json
MK=[("Heimsieg","H"),("Auswärtssieg","A"),("Beide treffen – Ja","BJ"),("Beide treffen – Nein","BN"),("Über 2,5","O"),("Unter 2,5","U")]
def mk(s):
    if not s: return None
    best=None
    for n,k in MK:
        i=s.find(n)
        if i>=0 and (best is None or i<best[0]): best=(i,k)
    return best[1] if best else None
def out(h,a): return {"H":h>a,"A":a>h,"BJ":h>0<a,"BN":not(h>0<a),"O":h+a>2,"U":h+a<3}
norm=lambda s:unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode().lower()
rows=[]
for f in sorted(glob.glob("tipps/sportsmole/2026-11-*.md")):
    txt=open(f).read(); lines=txt.split("\n")
    hdr=None
    for ln in lines:
        if ln.startswith("|") and re.search(r"\|\s*Tipp\s*\|",ln):
            hdr=[c.strip() for c in ln.strip().strip("|").split("|")]; continue
        if not ln.startswith("|") or hdr is None: continue
        c=[x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c)<len(hdr)-1: continue
        d=dict(zip(hdr,c))
        tipc=d.get("Tipp",""); tip=mk(tipc.split("(")[0]) or mk(tipc)
        erg=d.get("Ergebnis","") or c[-1]
        m=re.search(r"(\d+)\s*:\s*(\d+)",erg+" "+c[-1])
        if not tip or not m: continue
        h,a=int(m.group(1)),int(m.group(2))
        spiel=d.get("Spiel") or d.get("Paarung") or ""
        liga=d.get("Liga","")
        kz=d.get("Kennzeichnung","")
        orig=None
        mo=re.search(r"bis [\d:]+ ([^)]+)\)",tipc) or re.search(r"ursprünglich ([^)·]+)",tipc)
        if mo: orig=mk(mo.group(1))
        rows.append(dict(f=f.split("/")[-1][:-3],spiel=spiel,liga=liga,tip=tip,h=h,a=a,kz="einig" if "einig" in kz else "geteilt" if "geteilt" in kz else "?",gf="Grenzfall" in tipc,orig=orig,txt=txt))
# Merkmale je Spiel
for r in rows:
    home=norm(r["spiel"].split("–")[0].split(" - ")[0]).strip()[:8]
    secs=re.split(r"\n## ",r["txt"])
    sec=[s for s in secs if home and home in norm(s.split("\n")[0])]
    r["mm"]=None
    if sec:
        ms=re.findall(r"\*\*Merkmale[^*]*\*\*(.*?)(?:\n- \*\*|\n\n|$)",sec[-1],re.S)
        gult=[x for x in ms]
        if gult: r["mm"]=" ".join(gult[-1].split())
for r in rows:
    mm=r["mm"] or ""
    m9=re.search(r"\(9\)[^·]*?:\s*([^·(]+)",mm); r["zweit"]=mk(m9.group(1)) if m9 else None
    m6=re.search(r"\(6\)[^·]*?:\s*(ja|nein)",mm); r["r2"]=m6.group(1) if m6 else None
    m7=re.search(r"\(7\)[^·]*?:\s*(ja|nein)",mm); r["prof"]=m7.group(1) if m7 else None
    m5=re.search(r"\(5\)[^·]*?:\s*(ja|nein)",mm); r["neu1"]=m5.group(1) if m5 else None
    r["hit"]=out(r["h"],r["a"])[r["tip"]]
    del r["txt"]

def q(sub,key="hit"):
    t=sum(1 for r in sub if r[key]); return f"{t}/{len(sub)} = {t/len(sub):.0%}" if sub else "–"
print("Tipps:",len(rows),"Treffer",q(rows))
mm=[r for r in rows if r["mm"]]; print("mit Merkmale-Zeile:",len(mm))
z=[r for r in mm if r["zweit"]]
for r in z: r["zhit"]=out(r["h"],r["a"])[r["zweit"]]
print("\nTipp vs. zweitbester Markt (gleiche Spiele):",len(z)); print("  Tipp:",q(z),"  Zweitbester:",q(z,"zhit"))
print("  nur Tipp traf:",sum(r['hit'] and not r['zhit'] for r in z)," nur Zweitbester traf:",sum(r['zhit'] and not r['hit'] for r in z)," beide:",sum(r['hit'] and r['zhit'] for r in z)," keiner:",sum(not r['hit'] and not r['zhit'] for r in z))
for lab,k,v in (("Rang-2-Blöcke einig","r2","ja"),("Rang-2-Blöcke NICHT einig","r2","nein"),("gegensätzliche Profile","prof","ja"),("keine gegens. Profile","prof","nein"),("neue Rang-1-Gegenangabe","neu1","ja"),("keine neue Rang-1-Gegenangabe","neu1","nein")):
    print(f"  {lab}: {q([r for r in mm if r[k]==v])}")
print("\nKombination Kennzeichnung × Grenzfall:")
for kz in ("einig","geteilt"):
    for g in (False,True):
        print(f"  {kz}, Grenzfall={g}: {q([r for r in rows if r['kz']==kz and r['gf']==g])}")
print("\nGeänderte Tipps (vor Anpfiff):")
ch=[r for r in rows if r["orig"]]
for r in ch: r["ohit"]=out(r["h"],r["a"])[r["orig"]]
print("  Anzahl",len(ch)," neuer Tipp:",q(ch)," ursprünglicher hätte:",q(ch,"ohit"))
print("\nWettart × Kennzeichnung:")
for n,k in MK:
    a=[r for r in rows if r['tip']==k]
    if a: print(f"  {n}: einig {q([r for r in a if r['kz']=='einig'])} | geteilt {q([r for r in a if r['kz']=='geteilt'])}")
print("\nEuropapokal vs. Ligen:")
ep=[r for r in rows if re.search(r"Champions|Europa|Conference|ECL|EL\b|CL\b",r['liga']+r['f']) or r['f'] in ('2026-11-24','2026-11-25','2026-11-26') and not r['liga']]
print("  (Zuordnung über Liga-Spalte/Tagesliste)")
bylg={}
for r in rows:
    lg=r['liga'] or {'2026-11-24':'Champions League','2026-11-25':'Champions League','2026-11-26':'EL/ECL'}.get(r['f'],'?')
    lg=re.sub(r"\s*\(\d+\)","",lg)
    bylg.setdefault(lg,[]).append(r)
for lg,s in sorted(bylg.items(),key=lambda x:-len(x[1])): print(f"  {lg}: {q(s)}")
print("\nTor-Tipps: Abstand zur Torgrenze (wie knapp verfehlt):")
for n,k in MK[2:]:
    a=[r for r in rows if r['tip']==k and not r['hit']]
    print(f"  {n} verfehlt: "+", ".join(f"{r['h']}:{r['a']}" for r in a))
