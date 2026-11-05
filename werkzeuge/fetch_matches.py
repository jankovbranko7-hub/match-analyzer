import sys,json; sys.path.insert(0,'.')
import fs
S=json.load(open('../seasons.json'))
out={}
for cur,lst in S.items():
    ids=[sid for sid,yr in lst]
    i=ids.index(int(cur)); use=ids[max(0,i-3):i+1]
    for sid in use:
        rows=[]; p=1
        while True:
            r=fs.get('league-matches',season_id=sid,max_per_page=1000,page=p)
            if not r.get('success'): print('FEHLER',sid,r.get('message')); break
            rows+=r['data']; mp=r['pager']['max_page']
            if p>=mp: break
            p+=1
        out[str(sid)]={'league_current':cur,'n':len(rows),'pages':p}
        print(cur,sid,len(rows),'pages',p, r['metadata'].get('request_remaining') if 'metadata' in r else '')
json.dump(out,open('../matches_index.json','w'))
