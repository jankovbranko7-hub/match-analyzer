"""Tipp-Auswahl nach OA-Prognose-System v1.0 (OAP-1.0), Abschnitt 3.

Regel: p ≥ 60 %, Vorteil e = p × q − 1 ≥ 10 %, Bet365-Quote q ≤ 3,00, kein
Freundschaftsspiel, Status NS; pro Spiel höchstens ein Tipp (größter Vorteil).
p = Odd-Alerts-Wahrscheinlichkeit, q = aktuelle Bet365-Quote zum Abrufzeitpunkt.

Aufruf:
  python3 werkzeuge/oap_auswahl.py                  # nächste 24 Stunden, nur anzeigen/speichern
  python3 werkzeuge/oap_auswahl.py --stunden 48
  python3 werkzeuge/oap_auswahl.py --erfassen       # Tipps zusätzlich im Tracker erfassen

Ausgabe: scans/oap_<Zeit>.md und .json
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P_MIN, EDGE_MIN, Q_MAX = 0.60, 0.10, 3.00
VERSION = "OAP-1.0"


def kandidaten(von, bis):
    rows = oa.get_all("fixtures/upcoming", {
        "from": von, "to": bis, "per_page": 250, "include": "probability,odds",
        "bookmakers": "1,2", "markets": oa.MARKT_IDS, "odds_type": "closing"})
    tipps, geprueft, gesehen = [], 0, set()
    jetzt = oa.jetzt_utc().timestamp()
    for f in rows:
        if f["id"] in gesehen:
            continue
        gesehen.add(f["id"])
        if f.get("is_friendly") or f.get("status") != "NS" or f["unix"] <= jetzt:
            continue
        p = oa.wahrscheinlichkeiten(f.get("probability"))
        q = oa.quoten_aus_fixture(f.get("odds"))
        if not p:
            continue
        geprueft += 1
        beste = None
        for m in oa.MAERKTE:
            pm, qm = p.get(m), q["bet365"].get(m)
            if pm is None or qm is None:
                continue
            pm /= 100
            e = pm * qm - 1
            if pm >= P_MIN and e >= EDGE_MIN and qm <= Q_MAX:
                if beste is None or e > beste["vorteil"]:
                    beste = {"markt": m, "p": pm, "quote": qm, "vorteil": e,
                             "pinnacle": q["pinnacle"].get(m)}
        if beste:
            tipps.append({"match_id": f["id"], "anstoss_utc": oa.iso(f["unix"]), "unix": f["unix"],
                          "land": f.get("competition_country"), "wettbewerb": f.get("competition_name"),
                          "heim": f.get("home_name"), "gast": f.get("away_name"), **beste})
    tipps.sort(key=lambda t: (t["unix"], t["match_id"]))
    return tipps, geprueft


def bereits_erfasst():
    pfad = os.path.join(ROOT, "tracker", "vorab.jsonl")
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
        tipps, geprueft = kandidaten(von, bis)
    except oa.OAError as e:
        sys.exit(f"Fehler: {e}")
    stamp = jetzt.strftime("%Y-%m-%dT%H%MZ")
    meta = {"system": VERSION, "abruf_utc": jetzt.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "von_utc": oa.iso(von), "bis_utc": oa.iso(bis), "spiele_geprueft": geprueft,
            "regel": {"p_min": P_MIN, "vorteil_min": EDGE_MIN, "quote_max": Q_MAX},
            "abfrage": {"pfad": "fixtures/upcoming", "include": "probability,odds", "bookmakers": "1,2",
                        "markets": oa.MARKT_IDS, "odds_type": "closing", "api_token": "[REDACTED]"}}
    os.makedirs(os.path.join(ROOT, "scans"), exist_ok=True)
    with open(os.path.join(ROOT, "scans", f"oap_{stamp}.json"), "w", encoding="utf8") as fh:
        json.dump({"meta": meta, "tipps": tipps}, fh, ensure_ascii=False, indent=1)
    z = [f"# OA-Prognose-System v1.0 – Tipps {meta['abruf_utc']}", "",
         f"Zeitraum (UTC) {meta['von_utc']} bis {meta['bis_utc']} · {geprueft} Spiele mit Prognose geprüft · "
         f"**{len(tipps)} Tipps**", "",
         "Regel: Odd-Alerts-Wahrscheinlichkeit ≥ 60 %, Vorteil p×Quote−1 ≥ 10 %, Bet365-Quote ≤ 3,00, "
         "ein Tipp pro Spiel. **Status Testbetrieb – nur auf Papier.**", "",
         "| Nr | Anstoß UTC | Wettbewerb | Spiel | Match-ID | Tipp | OA % | Bet365 | Vorteil | Pinnacle |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for i, t in enumerate(tipps, 1):
        pin = f"{t['pinnacle']:.2f}" if t["pinnacle"] else "–"
        z.append(f"| {i} | {t['anstoss_utc'][:16].replace('T', ' ')} | {t['land']} · {t['wettbewerb']} | "
                 f"{t['heim']} – {t['gast']} | {t['match_id']} | {oa.MAERKTE[t['markt']]['label']} | "
                 f"{t['p'] * 100:.0f} | {t['quote']:.2f} | {t['vorteil'] * 100:+.0f} % | {pin} |")
    with open(os.path.join(ROOT, "scans", f"oap_{stamp}.md"), "w", encoding="utf8") as fh:
        fh.write("\n".join(z) + "\n")
    print(f"{geprueft} Spiele geprüft, {len(tipps)} Tipps → scans/oap_{stamp}.md")
    if a.erfassen:
        schon = bereits_erfasst()
        neu = 0
        for t in tipps:
            if t["match_id"] in schon:
                continue
            r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "werkzeuge", "tracker.py"), "erfassen",
                                "--match-id", str(t["match_id"]), "--markt", t["markt"], "--quelle", "system",
                                "--analyse-id", f"OAP-{stamp}-{t['match_id']}",
                                "--notiz", f"Auswahl: p={t['p']:.4f} q={t['quote']} Vorteil={t['vorteil']:.4f}"],
                               capture_output=True, text=True)
            if r.returncode == 0:
                neu += 1
            else:
                print("  nicht erfasst:", t["match_id"], (r.stdout + r.stderr).strip()[:150])
        print(f"{neu} neue Tipps im Tracker erfasst ({len(tipps) - neu} bereits vorhanden oder abgelehnt).")


if __name__ == "__main__":
    main()
