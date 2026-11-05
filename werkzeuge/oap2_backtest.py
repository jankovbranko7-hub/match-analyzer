"""Entwicklung und Test für OAP-2.0 (eigenes Modell + Odd-Alerts-Leitschiene).

Benötigt im Arbeitsordner fx.json und odds.json (von oap_backtest_holen.py) und den
Datenspeicher .cache/oap/ (von oap_daten.py). Strikt zeitlich: Für Spiele eines Tages
werden nur Ligaspiele verwendet, die vor 00:00 UTC dieses Tages beendet waren.
Entwicklung 06.–23.10.2026, unberührter Test ab 24.10.2026.

Aufruf (im Arbeitsordner): python3 /pfad/werkzeuge/oap2_backtest.py [schritt]
  schritt = modell  → Modellwahl (Log-Loss, nur Entwicklung)
  schritt = regel   → Regelwahl auf Entwicklung, dann einmaliger Test
"""

import collections
import itertools
import json
import math
import os
import sys
from datetime import datetime, timezone
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402
import oap_modell as om  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache", "oap")
GRENZE = datetime(2026, 10, 24, tzinfo=timezone.utc).timestamp()
MK = list(oa.MAERKTE)
GRID = [{"w_xg": w, "halbwertszeit": hl, "alpha": 2.0, "min_spiele": 6}
        for w, hl in itertools.product((0.0, 0.5, 1.0), (120.0, 365.0))]


def lade_basis():
    fx = json.load(open("fx.json"))
    od = json.load(open("odds.json"))
    Q = collections.defaultdict(dict)
    for r in od:
        try:
            Q[(r["fixture_id"], r["bookmaker_id"])][(r["market_key"], r["outcome"])] = (
                float(r["opening"]), float(r["closing"]))
        except (TypeError, ValueError):
            pass
    spiele, seen = [], set()
    for f in fx:
        if f["id"] in seen or f.get("competition_type") != "League" or f.get("is_friendly"):
            continue
        seen.add(f["id"])
        t = oa.regulaere_tore(f)
        b = Q.get((f["id"], 2))
        if not t or not b or not os.path.exists(os.path.join(CACHE, f"comp_{f['competition_id']}.json")):
            continue
        tag = int(f["unix"] // 86400 * 86400)
        spiele.append({"id": f["id"], "c": f["competition_id"], "tag": tag, "u": f["unix"],
                       "h": f["home_id"], "a": f["away_id"], "hg": t[0], "ag": t[1],
                       "test": f["unix"] >= GRENZE, "oa": oa.wahrscheinlichkeiten(f["probability"]),
                       "b365": b, "pin": Q.get((f["id"], 1), {})})
    return spiele


def _arbeit(args):
    c, tage, spiele_c, params = args
    with open(os.path.join(CACHE, f"comp_{c}.json")) as fh:
        hist = json.load(fh)["spiele"]
    out = {}
    for tag in tage:
        m = om.fit(hist, tag, params["w_xg"], params["halbwertszeit"], params["alpha"])
        for s in spiele_c:
            if s["tag"] != tag:
                continue
            lam = om.lambdas(m, s["h"], s["a"], params["min_spiele"])
            if lam:
                out[s["id"]] = om.maerkte(*lam)
    return out


def vorhersagen(spiele, params, nur=None):
    gruppen = collections.defaultdict(list)
    for s in spiele:
        if nur is None or s["test"] == nur:
            gruppen[s["c"]].append(s)
    jobs = [(c, sorted({s["tag"] for s in L}), [{k: s[k] for k in ("id", "tag", "h", "a")} for s in L], params)
            for c, L in gruppen.items()]
    res = {}
    with Pool(4) as pool:
        for r in pool.imap_unordered(_arbeit, jobs, chunksize=4):
            res.update(r)
    return res


def logloss(spiele, P, quelle):
    """Mittlerer Log-Loss 1X2 (3-Weg), Over/Under, BTTS auf gemeinsamen Spielen."""
    ll = collections.defaultdict(list)
    for s in spiele:
        pm = P.get(s["id"])
        if not pm or not s["oa"] or any(s["oa"].get(k) is None for k in MK):
            continue
        p = pm if quelle == "modell" else {k: s["oa"][k] / 100 for k in MK}
        h, a = s["hg"], s["ag"]
        e = "heim" if h > a else "remis" if h == a else "auswaerts"
        ll["1x2"].append(-math.log(max(p[e] / (p["heim"] + p["remis"] + p["auswaerts"]), 1e-9)))
        o = h + a >= 3
        ll["ou"].append(-math.log(max(p["over25"] if o else p["under25"], 1e-9)))
        bt = h > 0 and a > 0
        ll["btts"].append(-math.log(max(p["btts"] if bt else p["btts_nein"], 1e-9)))
    return {k: (round(sum(v) / len(v), 4), len(v)) for k, v in ll.items()}


def zeilen(spiele, P):
    out = []
    for s in spiele:
        pm = P.get(s["id"])
        if not pm or not s["oa"]:
            continue
        for m in MK:
            ok = oa.MAERKTE[m]["odds"]
            if ok not in s["b365"] or s["oa"].get(m) is None:
                continue
            o, c = s["b365"][ok]
            if o <= 1 or c <= 1:
                continue
            out.append({"fid": s["id"], "test": s["test"], "m": m, "pm": pm[m], "po": s["oa"][m] / 100,
                        "o": o, "c": c, "pc": (s["pin"].get(ok) or (None, None))[1],
                        "won": oa.gewonnen(m, s["hg"], s["ag"])})
    return out


def regel(Z, e_min, p_min, d_max, oa_wert, q_max=3.0):
    best = {}
    for r in Z:
        e = r["pm"] * r["o"] - 1
        if (r["pm"] >= p_min and e >= e_min and r["o"] <= q_max and abs(r["pm"] - r["po"]) <= d_max
                and (not oa_wert or r["po"] * r["o"] - 1 >= 0)):
            if r["fid"] not in best or e > best[r["fid"]][0]:
                best[r["fid"]] = (e, r)
    return [r for _, r in best.values()]


def ev(sel, q):
    n = len(sel)
    if not n:
        return "n=0"
    g = [(r[q] - 1) if r["won"] else -1 for r in sel]
    pr = sum(g)
    sd = math.sqrt(sum((x - pr / n) ** 2 for x in g) / n) or 1
    cl = [r["o"] / r["pc"] - 1 for r in sel if r["pc"]]
    clv = f"{sum(cl) / len(cl) * 100:+.1f}%" if cl else "–"
    return (f"n={n:4} Treffer {sum(r['won'] for r in sel) / n * 100:5.1f}% ROI {pr / n * 100:+6.1f}% "
            f"z={pr / (sd * math.sqrt(n)):+.1f} CLV {clv}")


def main():
    schritt = sys.argv[1] if len(sys.argv) > 1 else "modell"
    spiele = lade_basis()
    dev = [s for s in spiele if not s["test"]]
    print(f"Ligaspiele mit Prognose, Ergebnis, Bet365: {len(spiele)} (Entwicklung {len(dev)})", flush=True)
    if schritt == "modell":
        erg = []
        for params in GRID:
            P = vorhersagen(spiele, params, nur=False)
            L = logloss(dev, P, "modell")
            summe = sum(v[0] for v in L.values())
            erg.append((summe, params, L))
            print(f"{params}: {L} Summe {summe:.4f}", flush=True)
        print("Odd Alerts (gleiche Spiele, letzte Einstellung):", logloss(dev, P, "oa"))
        best = min(erg, key=lambda x: x[0])
        json.dump(best[1], open("oap2_params.json", "w"))
        print("GEWÄHLT:", best[1])
    else:
        params = json.load(open("oap2_params.json"))
        P = vorhersagen(spiele, params)
        print("Log-Loss Test – Modell:", logloss([s for s in spiele if s["test"]], P, "modell"),
              "| Odd Alerts:", logloss([s for s in spiele if s["test"]], P, "oa"))
        Z = zeilen(spiele, P)
        Zd, Zt = [r for r in Z if not r["test"]], [r for r in Z if r["test"]]
        kand = []
        for e_min, p_min, d_max, oa_wert in itertools.product((0.05, 0.10), (0.40, 0.50), (0.05, 0.10), (False, True)):
            sel = regel(Zd, e_min, p_min, d_max, oa_wert)
            if len(sel) >= 150:
                roi = sum((r["o"] - 1) if r["won"] else -1 for r in sel) / len(sel)
                kand.append((roi, (e_min, p_min, d_max, oa_wert), sel))
        kand.sort(key=lambda x: -x[0])
        print("\nRegeln in der Entwicklung (Eröffnungsquote o / Schlussquote c):")
        for roi, k, sel in kand:
            print(f"  Vorteil≥{k[0]} p≥{k[1]} |Modell−OA|≤{k[2]} OA-Wert≥0:{k[3]!s:5}  o {ev(sel, 'o')} | c {ev(sel, 'c')}")
        if not kand:
            print("keine Regel mit ≥150 Tipps")
            return
        roi, k, _ = kand[0]
        json.dump({"params": params, "regel": {"vorteil_min": k[0], "p_min": k[1], "abweichung_max": k[2],
                                               "oa_wert_min_0": k[3], "quote_max": 3.0}},
                  open("oap2_gewaehlt.json", "w"))
        sel = regel(Zt, *k)
        print(f"\nGEWÄHLT (beste Entwicklung): {k}")
        print(f"TEST 24.10.–03.11.: o {ev(sel, 'o')} | c {ev(sel, 'c')}")
        for m in MK:
            x = [r for r in sel if r["m"] == m]
            if x:
                print(f"   {m:10} o {ev(x, 'o')} | c {ev(x, 'c')}")


if __name__ == "__main__":
    main()
