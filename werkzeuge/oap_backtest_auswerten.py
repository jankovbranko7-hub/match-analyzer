"""Auswertung der Entwicklungsdaten für OAP-1.0 (im Ordner mit fx.json/odds.json ausführen).
Entwicklung 06.–23.10., unberührter Test ab 24.10.2026."""
import json, math, sys, collections
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa
from datetime import datetime, timezone

GRENZE = datetime(2026, 10, 24, tzinfo=timezone.utc).timestamp()  # ab hier unberührter Test
M = {  # markt: (prob-feld, (odds-markt, outcome))
    "heim": ("home_win", ("ft_result", "home")),
    "remis": ("draw", ("ft_result", "draw")),
    "auswaerts": ("away_win", ("ft_result", "away")),
    "btts_ja": ("btts", ("btts", "yes")),
    "btts_nein": ("btts_no", ("btts", "no")),
    "over25": ("o25", ("total_goals", "over_25")),
    "under25": ("u25", ("total_goals", "under_25")),
}
def win(m, h, a):
    return {"heim": h > a, "remis": h == a, "auswaerts": a > h, "btts_ja": h > 0 and a > 0,
            "btts_nein": h == 0 or a == 0, "over25": h + a >= 3, "under25": h + a <= 2}[m]

fx = json.load(open("fx.json")); od = json.load(open("odds.json"))
Q = collections.defaultdict(dict)
for r in od:
    try: Q[(r["fixture_id"], r["bookmaker_id"])][(r["market_key"], r["outcome"])] = (float(r["opening"]), float(r["closing"]))
    except (TypeError, ValueError): pass
rows, seen = [], set()
for f in fx:
    if f["id"] in seen: continue
    seen.add(f["id"])
    t = oa.regulaere_tore(f)
    if not t: continue
    h, a = t[0], t[1]; p = f["probability"]
    b365, pin = Q.get((f["id"], 2), {}), Q.get((f["id"], 1), {})
    # Pinnacle faire Wahrscheinlichkeit (Eröffnung, Marge proportional entfernt)
    fair = {}
    for grp in (["heim", "remis", "auswaerts"], ["over25", "under25"]):
        qs = [pin.get(M[m][1]) for m in grp]
        if all(qs):
            inv = [1 / q[0] for q in qs]; s = sum(inv)
            for m, v in zip(grp, inv): fair[m] = v / s
    for m, (pk, ok) in M.items():
        if p.get(pk) is None or ok not in b365: continue
        o, c = b365[ok]
        if o <= 1 or c <= 1: continue
        rows.append(dict(fid=f["id"], unix=f["unix"], test=f["unix"] >= GRENZE, m=m, p=float(p[pk]) / 100,
                         o=o, c=c, pc=(pin.get(ok) or (None, None))[1], fair=fair.get(m), won=win(m, h, a),
                         pred=f.get("competition_predictability"), mp=min(f.get("home_played") or 0, f.get("away_played") or 0),
                         friendly=f.get("is_friendly"), cup=f.get("is_cup")))
dev = [r for r in rows if not r["test"]]; test = [r for r in rows if r["test"]]
print(f"Zeilen {len(rows)} (Entwicklung {len(dev)}, Test {len(test)}), Spiele {len({r['fid'] for r in rows})}")

def kal(sel, name):
    print(f"\nKalibrierung {name}")
    for m in M:
        s = [r for r in sel if r["m"] == m]
        if not s: continue
        br = sum((r["p"] - r["won"]) ** 2 for r in s) / len(s)
        gr = []
        for lo in range(0, 100, 20):
            g = [r for r in s if lo / 100 <= r["p"] < (lo + 20) / 100 or (lo == 80 and r["p"] >= 1)]
            if len(g) >= 20: gr.append(f"{lo}-{lo+20}:{sum(r['p'] for r in g)/len(g)*100:.0f}→{sum(r['won'] for r in g)/len(g)*100:.0f}({len(g)})")
        print(f"  {m:10} n={len(s):5} Brier {br:.3f}  " + " ".join(gr))

def ev(sel, quote="c"):
    n = len(sel)
    if n == 0: return None
    pr = sum((r[quote] - 1) if r["won"] else -1 for r in sel)
    sd = math.sqrt(sum((((r[quote] - 1) if r["won"] else -1) - pr / n) ** 2 for r in sel) / n) or 1
    cl = [r["o"] / r["pc"] - 1 for r in sel if r["pc"]]
    return dict(n=n, treffer=sum(r["won"] for r in sel) / n, roi=pr / n, z=pr / (sd * math.sqrt(n)),
                clv=sum(cl) / len(cl) if cl else float("nan"))

def fmt(e):
    if not e: return "n=0"
    return f"n={e['n']:5} Treffer {e['treffer']*100:5.1f}% ROI {e['roi']*100:+6.1f}% z={e['z']:+.1f} CLV {e['clv']*100:+5.1f}%"

def regel(sel, maerkte, edge_min, p_min, q_max, signal="oa", eins_pro_spiel=True):
    out = []
    for r in sel:
        if r["m"] not in maerkte or r["friendly"]: continue
        pp = r["p"] if signal == "oa" else r["fair"]
        if pp is None: continue
        e = pp * r["o"] - 1
        if e >= edge_min and r["p"] >= p_min and r["o"] <= q_max:
            out.append({**r, "edge": e})
    if eins_pro_spiel:
        best = {}
        for r in out:
            if r["fid"] not in best or r["edge"] > best[r["fid"]]["edge"]: best[r["fid"]] = r
        out = list(best.values())
    return out

if __name__ == "__main__":
    kal(dev, "Entwicklung")
    print("\nAlle Tipps je Markt (Entwicklung, Eröffnungsquote o / Schlussquote c):")
    for m in M:
        s = [r for r in dev if r["m"] == m]
        print(f"  {m:10} o: {fmt(ev(s,'o'))} | c: {fmt(ev(s,'c'))}")
    GRUPPEN = {"1X2": ["heim", "remis", "auswaerts"], "Tore": ["over25", "under25"], "BTTS": ["btts_ja", "btts_nein"],
               "alle": list(M)}
    erg = []
    for gname, g in GRUPPEN.items():
        for em in (0.0, 0.05, 0.10, 0.20):
            for pm in (0.0, 0.40, 0.50, 0.60):
                for qm in (3.0, 5.0):
                    s = regel(dev, g, em, pm, qm)
                    e = ev(s, "o")
                    if e and e["n"] >= 150: erg.append((e["roi"], gname, em, pm, qm, e, ev(s, "c")))
    erg.sort(key=lambda x: -x[0])
    print("\nBeste Regeln in der Entwicklung (Eröffnungsquote, mind. 150 Tipps):")
    for x in erg[:12]:
        print(f"  {x[1]:5} Edge≥{x[2]:.2f} p≥{x[3]:.2f} Quote≤{x[4]}  o: {fmt(x[5])} | c: {fmt(x[6])}")
    print(f"  ... von {len(erg)} Regeln, positiv (o): {sum(1 for x in erg if x[0]>0)}")
    json.dump([[x[1], x[2], x[3], x[4]] for x in erg[:12]], open("top_regeln.json", "w"))
