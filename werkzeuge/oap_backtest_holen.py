"""Entwicklungsdaten für OAP-1.0 holen (06.10.–03.11.2026). Im Arbeitsordner ausführen;
schreibt fx.json und odds.json. Schlüssel aus ODDALERTS_KEY."""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa
from datetime import datetime,timezone,timedelta
start=datetime(2026,10,6,tzinfo=timezone.utc); ende=datetime(2026,11,4,tzinfo=timezone.utc)
fx=[]
d=start
while d<ende:
    a=int(d.timestamp()); b=int((d+timedelta(days=1)).timestamp())-1
    rows=oa.get_all("fixtures/between",{"from":a,"to":b,"include":"probability,timings","per_page":250})
    keep=[r for r in rows if r.get("probability")]
    fx+=keep; print(d.date(),len(rows),len(keep),file=sys.stderr,flush=True)
    d+=timedelta(days=1)
json.dump(fx,open("fx.json","w"))
ids=sorted({r["id"] for r in fx if r.get("status") in ("FT","AET","FT_PEN")})
print("Spiele mit Prognose und Ergebnis",len(ids),file=sys.stderr,flush=True)
od=[]
for i in range(0,len(ids),50):
    od+=oa.get("odds/history/multiple",{"ids":",".join(map(str,ids[i:i+50])),"markets":"6,9,13","bookmakers":"1,2"}).get("data") or []
    if i%2500==0: print("Quoten",i,len(od),file=sys.stderr,flush=True)
json.dump(od,open("odds.json","w")); print("fertig",len(fx),len(od))
