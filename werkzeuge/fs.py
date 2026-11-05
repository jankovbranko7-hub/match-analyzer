import os, sys, json, time, hashlib, urllib.request, urllib.parse, urllib.error, datetime
BASE="https://api.football-data-api.com/"
CACHE=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"cache")
LOG=os.path.join(CACHE,"_requests.log")
def get(endpoint, nocache=False, **params):
    key=os.environ.get("FOOTYSTATS_KEY")
    if not key: raise SystemExit("FOOTYSTATS_KEY fehlt")
    red="&".join(f"{k}={v}" for k,v in sorted(params.items()))
    fn=os.path.join(CACHE, endpoint.replace("/","_")+"__"+hashlib.md5(red.encode()).hexdigest()[:10]+".json")
    if os.path.exists(fn) and not nocache:
        return json.load(open(fn))["data_raw"]
    q=dict(params); q["key"]=key
    url=BASE+endpoint+"?"+urllib.parse.urlencode(q)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                body=json.load(r)
            break
        except urllib.error.HTTPError as e:
            if e.code==417:
                try: b=json.loads(e.read())
                except Exception: b={}
                if b.get('metadata',{}).get('request_limit') is None and b: raise LookupError('nicht im Abo')
                raise SystemExit("HTTP 417 Stundenlimit")
            if attempt==2: raise SystemExit(f"HTTP {e.code} bei {endpoint}")
            time.sleep(2)
    ts=datetime.datetime.now(datetime.timezone.utc).isoformat()
    json.dump({"endpoint":endpoint,"params_redacted":red+"&key=[REDACTED]","fetched_utc":ts,"data_raw":body},open(fn,"w"))
    open(LOG,"a").write(f"{ts}\t{BASE}{endpoint}?{red}&key=[REDACTED]\n")
    return body
