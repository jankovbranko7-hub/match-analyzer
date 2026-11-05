"""Tipp-Auswahl nach OA-Prognose-System v2.0 (OAP-2.0): eigenes Modell + Odd-Alerts-Leitschiene.

Regel (Regelwerk Abschnitt 4), je Markt:
  p_M = eigene Modellwahrscheinlichkeit, p_OA = Odd Alerts, q = aktuelle Bet365-Quote
  p_M ≥ 40 %, Vorteil p_M × q − 1 ≥ 10 %, q ≤ 3,00,
  Leitschiene: |p_M − p_OA| ≤ 5 Prozentpunkte UND p_OA × q − 1 ≥ 0,
  nur Ligaspiele, kein Freundschaftsspiel, Status NS; pro Spiel ein Tipp (größter Vorteil).

Aufruf:
  python3 werkzeuge/oap2_auswahl.py [--stunden 24] [--erfassen]
Ausgabe: scans/oap2_<Zeit>.md und .json
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402
import oap_daten as od  # noqa: E402
import oap_modell as om  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "OAP-2.0"
PARAMS = {"w_xg": 1.0, "halbwertszeit": 120.0, "alpha": 2.0, "min_spiele": 6}
P_MIN, EDGE_MIN, Q_MAX, ABW_MAX = 0.40, 0.10, 3.00, 0.05


def auswahl(von, bis):
    rows = oa.get_all("fixtures/upcoming", {
        "from": von, "to": bis, "per_page": 250, "include": "probability,odds",
        "bookmakers": "1,2", "markets": oa.MARKT_IDS, "odds_type": "closing"})
    jetzt = oa.jetzt_utc().timestamp()
    spiele, gesehen = [], set()
    for f in rows:
        if f["id"] in gesehen:
            continue
        gesehen.add(f["id"])
        if (f.get("competition_type") != "League" or f.get("is_friendly") or f.get("status") != "NS"
                or f["unix"] <= jetzt or not f.get("probability")):
            continue
        spiele.append(f)
    modelle, stat = {}, {"ligaspiele": len(spiele), "ohne_modell": 0, "ohne_quote": 0}
    for cid in sorted({f["competition_id"] for f in spiele}):
        try:
            od.aktualisieren(cid)
            hist = od.laden(cid)["spiele"]
            modelle[cid] = om.fit(hist, jetzt, PARAMS["w_xg"], PARAMS["halbwertszeit"], PARAMS["alpha"])
        except (oa.OAError, TypeError, KeyError):
            modelle[cid] = None
    tipps, alle = [], []
    for f in spiele:
        lam = om.lambdas(modelle.get(f["competition_id"]), f["home_id"], f["away_id"], PARAMS["min_spiele"])
        if not lam:
            stat["ohne_modell"] += 1
            continue
        pm = om.maerkte(*lam)
        po = oa.wahrscheinlichkeiten(f["probability"])
        q = oa.quoten_aus_fixture(f.get("odds"))
        beste = None
        for m in oa.MAERKTE:
            qm, pom = q["bet365"].get(m), po.get(m)
            if qm is None or pom is None:
                continue
            pom /= 100
            e = pm[m] * qm - 1
            if (pm[m] >= P_MIN and e >= EDGE_MIN and qm <= Q_MAX and abs(pm[m] - pom) <= ABW_MAX
                    and pom * qm - 1 >= 0):
                if beste is None or e > beste["vorteil"]:
                    beste = {"markt": m, "p_modell": pm[m], "p_oa": pom, "quote": qm, "vorteil": e,
                             "pinnacle": q["pinnacle"].get(m)}
        info = {"match_id": f["id"], "anstoss_utc": oa.iso(f["unix"]), "unix": f["unix"],
                "land": f.get("competition_country"), "wettbewerb": f.get("competition_name"),
                "heim": f.get("home_name"), "gast": f.get("away_name"),
                "lambda": [round(lam[0], 3), round(lam[1], 3)],
                "modell": {k: round(v, 4) for k, v in pm.items() if k in oa.MAERKTE}}
        alle.append(info)
        if beste:
            tipps.append({**info, **beste})
    tipps.sort(key=lambda t: (t["unix"], t["match_id"]))
    return tipps, alle, stat


def bereits_erfasst(system):
    pfad = os.path.join(ROOT, "tracker", system, "vorab.jsonl")
    if not os.path.exists(pfad):
        return set()
    with open(pfad, encoding="utf8") as fh:
        return {json.loads(z)["match_id"] for z in fh if z.strip()}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stunden", type=int, default=24)
    ap.add_argument("--erfassen", action="store_true")
    a = ap.parse_args()
    jetzt = oa.jetzt_utc()
    von, bis = int(jetzt.timestamp()), int((jetzt + timedelta(hours=a.stunden)).timestamp())
    try:
        tipps, alle, stat = auswahl(von, bis)
    except oa.OAError as e:
        sys.exit(f"Fehler: {e}")
    stamp = jetzt.strftime("%Y-%m-%dT%H%MZ")
    meta = {"system": VERSION, "abruf_utc": jetzt.strftime("%Y-%m-%dT%H:%M:%SZ"), "von_utc": oa.iso(von),
            "bis_utc": oa.iso(bis), **stat, "mit_modell": len(alle), "modell": PARAMS,
            "regel": {"p_min": P_MIN, "vorteil_min": EDGE_MIN, "quote_max": Q_MAX, "abweichung_oa_max": ABW_MAX,
                      "oa_vorteil_min": 0.0},
            "abfrage": {"pfad": "fixtures/upcoming", "include": "probability,odds", "bookmakers": "1,2",
                        "markets": oa.MARKT_IDS, "odds_type": "closing", "api_token": "[REDACTED]"}}
    os.makedirs(os.path.join(ROOT, "scans"), exist_ok=True)
    with open(os.path.join(ROOT, "scans", f"oap2_{stamp}.json"), "w", encoding="utf8") as fh:
        json.dump({"meta": meta, "tipps": tipps, "alle_modellwerte": alle}, fh, ensure_ascii=False)
    z = [f"# OA-Prognose-System v2.0 – Tipps {meta['abruf_utc']}", "",
         f"Zeitraum (UTC) {meta['von_utc']} bis {meta['bis_utc']} · {stat['ligaspiele']} Ligaspiele mit "
         f"Odd-Alerts-Prognose, {len(alle)} mit eigenem Modellwert · **{len(tipps)} Tipps**", "",
         "Eigenes Modell entscheidet (p ≥ 40 %, Vorteil ≥ 10 %, Bet365 ≤ 3,00); Odd Alerts als Leitschiene "
         "(höchstens 5 Punkte Abweichung, OA sieht keinen Nachteil). **Status Testbetrieb – nur auf Papier.**", "",
         "| Nr | Anstoß UTC | Wettbewerb | Spiel | Match-ID | Tipp | Modell % | OA % | Bet365 | Vorteil |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for i, t in enumerate(tipps, 1):
        z.append(f"| {i} | {t['anstoss_utc'][:16].replace('T', ' ')} | {t['land']} · {t['wettbewerb']} | "
                 f"{t['heim']} – {t['gast']} | {t['match_id']} | {oa.MAERKTE[t['markt']]['label']} | "
                 f"{t['p_modell'] * 100:.0f} | {t['p_oa'] * 100:.0f} | {t['quote']:.2f} | {t['vorteil'] * 100:+.0f} % |")
    with open(os.path.join(ROOT, "scans", f"oap2_{stamp}.md"), "w", encoding="utf8") as fh:
        fh.write("\n".join(z) + "\n")
    print(f"{stat['ligaspiele']} Ligaspiele, {len(alle)} mit Modellwert, {len(tipps)} Tipps → scans/oap2_{stamp}.md")
    if a.erfassen:
        schon = bereits_erfasst(VERSION)
        neu = 0
        for t in tipps:
            if t["match_id"] in schon:
                continue
            r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "werkzeuge", "tracker.py"), "erfassen",
                                "--match-id", str(t["match_id"]), "--markt", t["markt"], "--quelle", "system",
                                "--analyse-id", f"OAP2-{stamp}-{t['match_id']}",
                                "--notiz", f"Modell p={t['p_modell']:.4f} OA p={t['p_oa']:.4f} q={t['quote']} "
                                           f"Vorteil={t['vorteil']:.4f} lambda={t['lambda']}"],
                               capture_output=True, text=True, env={**os.environ, "TRACKER_SYSTEM": VERSION})
            if r.returncode == 0:
                neu += 1
            else:
                print("  nicht erfasst:", t["match_id"], (r.stdout + r.stderr).strip()[:150])
        print(f"{neu} neue Tipps im Tracker erfasst.")


if __name__ == "__main__":
    main()
