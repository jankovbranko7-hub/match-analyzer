"""Test des gemeinsamen Modells OAP-M2 an Pokal- und Europapokalspielen (für OAP-2.1).

Regel und Leitschiene unverändert aus OAP-2.0 übernommen (keine neue Anpassung).
Strikt zeitlich: je Spieltag ein Modell mit allen vor 00:00 UTC beendeten Spielen.
Im Arbeitsordner mit fx.json/odds.json ausführen.
"""

import collections
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402
import oap_global as G  # noqa: E402
import oap_modell as om  # noqa: E402
import oap2_backtest as B  # noqa: E402


def main():
    fx = json.load(open("fx.json"))
    od = json.load(open("odds.json"))
    Q = collections.defaultdict(dict)
    for r in od:
        try:
            Q[(r["fixture_id"], r["bookmaker_id"])][(r["market_key"], r["outcome"])] = (float(r["opening"]), float(r["closing"]))
        except (TypeError, ValueError):
            pass
    spiele, seen = [], set()
    for f in fx:
        if f["id"] in seen or f.get("competition_type") == "League" or f.get("is_friendly"):
            continue
        seen.add(f["id"])
        t = oa.regulaere_tore(f)
        b = Q.get((f["id"], 2))
        if not t or not b:
            continue
        spiele.append({"id": f["id"], "c": f["competition_id"], "cn": f["competition_name"], "tag": int(f["unix"] // 86400 * 86400),
                       "h": f["home_id"], "a": f["away_id"], "hg": t[0], "ag": t[1], "test": f["unix"] >= B.GRENZE,
                       "oa": oa.wahrscheinlichkeiten(f["probability"]), "b365": b, "pin": Q.get((f["id"], 1), {})})
    print(f"Pokal-/Europapokalspiele mit Prognose, Ergebnis, Bet365: {len(spiele)}", flush=True)
    alle = G.alle_spiele()
    P = {}
    for tag in sorted({s["tag"] for s in spiele}):
        m = G.fit(alle, tag)
        for s in spiele:
            if s["tag"] == tag:
                lam = G.lambdas(m, s["h"], s["a"], 6)
                if lam:
                    P[s["id"]] = om.maerkte(*lam)
    dev = [s for s in spiele if not s["test"]]
    tst = [s for s in spiele if s["test"]]
    print(f"mit Modellwert: {len(P)} von {len(spiele)}")
    for name, sel in (("Entwicklung", dev), ("Test", tst)):
        print(f"Log-Loss {name} – Modell M2: {B.logloss(sel, P, 'modell')} | Odd Alerts: {B.logloss(sel, P, 'oa')}")
    Z = B.zeilen(spiele, P)
    regel = (0.10, 0.40, 0.05, True)  # unverändert aus OAP-2.0
    for name, flag in (("Entwicklung 06.–23.10.", False), ("Test 24.10.–03.11.", True)):
        sel = B.regel([r for r in Z if r["test"] == flag], *regel)
        print(f"{name}: o {B.ev(sel, 'o')} | c {B.ev(sel, 'c')}")
    gesamt = B.regel(Z, *regel)
    print(f"Gesamt: o {B.ev(gesamt, 'o')} | c {B.ev(gesamt, 'c')}")
    nach = collections.defaultdict(list)
    namen = {s["id"]: s["cn"] for s in spiele}
    for r in gesamt:
        nach[namen[r["fid"]]].append(r)
    for k, v in sorted(nach.items(), key=lambda x: -len(x[1]))[:10]:
        print(f"   {k:35} {B.ev(v, 'o')}")


if __name__ == "__main__":
    main()
