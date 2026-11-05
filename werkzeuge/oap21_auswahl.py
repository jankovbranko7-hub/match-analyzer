"""Tipp-Auswahl nach OA-Prognose-System v2.1 (OAP-2.1).

Alle Ligaspiele (Modell OAP-M1 je Liga) sowie alle Pokal-, Europapokal- und anderen
Wettbewerbsspiele (gemeinsames Modell OAP-M3: Ligastärke + Teamabweichung).
Regel und Odd-Alerts-Leitschiene unverändert aus v2.0:
  p_M ≥ 40 %, Vorteil p_M × q − 1 ≥ 10 %, q ≤ 3,00 (Bet365 aktuell),
  |p_M − p_OA| ≤ 5 Prozentpunkte UND p_OA × q − 1 ≥ 0;
  kein Freundschaftsspiel, Status NS, pro Spiel ein Tipp (größter Vorteil).

Aufruf:  python3 werkzeuge/oap21_auswahl.py [--stunden 24] [--erfassen]
Ausgabe: scans/oap21_<Zeit>.md und .json
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402
import oap_daten as od  # noqa: E402
import oap_global as G  # noqa: E402
import oap_modell as om  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "OAP-2.1"
M1 = {"w_xg": 1.0, "halbwertszeit": 120.0, "alpha": 2.0, "min_spiele": 6}
M3 = {"w_xg": 1.0, "halbwertszeit": 120.0, "alpha_team": 5.0, "alpha_liga": 0.2, "fenster_tage": 400,
      "min_spiele": 6}
P_MIN, EDGE_MIN, Q_MAX, ABW_MAX = 0.40, 0.10, 3.00, 0.05
TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]


def mez(unix):
    d = datetime.fromtimestamp(unix, ZoneInfo("Europe/Berlin"))
    return f"{TAGE[d.weekday()]} {d:%d.%m. %H:%M}"


def regel(pm, po, q):
    beste = None
    for m in oa.MAERKTE:
        qm, pom = q["bet365"].get(m), po.get(m)
        if qm is None or pom is None:
            continue
        pom /= 100
        e = pm[m] * qm - 1
        if pm[m] >= P_MIN and e >= EDGE_MIN and qm <= Q_MAX and abs(pm[m] - pom) <= ABW_MAX and pom * qm - 1 >= 0:
            if beste is None or e > beste["vorteil"]:
                beste = {"markt": m, "p_modell": pm[m], "p_oa": pom, "quote": qm, "vorteil": e,
                         "pinnacle": q["pinnacle"].get(m)}
    return beste


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
        if f.get("is_friendly") or f.get("status") != "NS" or f["unix"] <= jetzt or not f.get("probability"):
            continue
        spiele.append(f)
    liga = [f for f in spiele if f.get("competition_type") == "League"]
    pokal = [f for f in spiele if f.get("competition_type") != "League"]
    stat = {"spiele_mit_prognose": len(spiele), "ligaspiele": len(liga), "pokalspiele": len(pokal),
            "ohne_modell": 0}
    # Ligen: Datenspeicher je Liga aktualisieren, M1 je Liga
    m1 = {}
    for cid in sorted({f["competition_id"] for f in liga}):
        try:
            od.aktualisieren(cid)
            m1[cid] = om.fit(od.laden(cid)["spiele"], jetzt, M1["w_xg"], M1["halbwertszeit"], M1["alpha"])
        except (oa.OAError, TypeError, KeyError):
            m1[cid] = None
    # Pokale: Pokalwettbewerb + Ligen beider Teams aktualisieren, dann ein gemeinsames M3
    m3 = None
    if pokal:
        index = G.team_wettbewerbe(G.alle_spiele())
        zu_laden = {f["competition_id"] for f in pokal}
        for f in pokal:
            zu_laden |= index.get(f["home_id"], set()) | index.get(f["away_id"], set())
        zu_laden -= set(m1)  # heute schon aktualisiert
        for cid in sorted(zu_laden):
            try:
                od.aktualisieren(cid)
            except oa.OAError:
                pass
        m3 = G.fit_h2(G.alle_spiele(), jetzt, w_xg=M3["w_xg"], halbwertszeit=M3["halbwertszeit"],
                      alpha_team=M3["alpha_team"], alpha_liga=M3["alpha_liga"], fenster_tage=M3["fenster_tage"])
    tipps, alle = [], []
    for f in spiele:
        ist_liga = f.get("competition_type") == "League"
        lam = (om.lambdas(m1.get(f["competition_id"]), f["home_id"], f["away_id"], M1["min_spiele"]) if ist_liga
               else G.lambdas(m3, f["home_id"], f["away_id"], M3["min_spiele"]))
        if not lam:
            stat["ohne_modell"] += 1
            continue
        pm = om.maerkte(*lam)
        info = {"match_id": f["id"], "anstoss_utc": oa.iso(f["unix"]), "unix": f["unix"],
                "land": f.get("competition_country"), "wettbewerb": f.get("competition_name"),
                "art": "Liga" if ist_liga else "Pokal/Europapokal", "modell_name": "OAP-M1" if ist_liga else "OAP-M3",
                "heim": f.get("home_name"), "gast": f.get("away_name"),
                "lambda": [round(lam[0], 3), round(lam[1], 3)],
                "modell": {k: round(v, 4) for k, v in pm.items() if k in oa.MAERKTE}}
        alle.append(info)
        beste = regel(pm, oa.wahrscheinlichkeiten(f["probability"]), oa.quoten_aus_fixture(f.get("odds")))
        if beste:
            tipps.append({**info, **beste})
    tipps.sort(key=lambda t: (t["unix"], t["match_id"]))
    return tipps, alle, stat


def bereits_erfasst():
    pfad = os.path.join(ROOT, "tracker", VERSION, "vorab.jsonl")
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
            "bis_utc": oa.iso(bis), **stat, "mit_modell": len(alle), "modell_liga": M1, "modell_pokal": M3,
            "regel": {"p_min": P_MIN, "vorteil_min": EDGE_MIN, "quote_max": Q_MAX, "abweichung_oa_max": ABW_MAX,
                      "oa_vorteil_min": 0.0},
            "abfrage": {"pfad": "fixtures/upcoming", "include": "probability,odds", "bookmakers": "1,2",
                        "markets": oa.MARKT_IDS, "odds_type": "closing", "api_token": "[REDACTED]"}}
    os.makedirs(os.path.join(ROOT, "scans"), exist_ok=True)
    with open(os.path.join(ROOT, "scans", f"oap21_{stamp}.json"), "w", encoding="utf8") as fh:
        json.dump({"meta": meta, "tipps": tipps, "alle_modellwerte": alle}, fh, ensure_ascii=False)
    z = [f"# OA-Prognose-System v2.1 – Tipps {meta['abruf_utc']}", "",
         f"Zeitraum (UTC) {meta['von_utc']} bis {meta['bis_utc']} · {stat['spiele_mit_prognose']} Spiele mit "
         f"Odd-Alerts-Prognose ({stat['ligaspiele']} Liga, {stat['pokalspiele']} Pokal/Europapokal), "
         f"{len(alle)} mit eigenem Modellwert · **{len(tipps)} Tipps**", "",
         "Eigenes Modell entscheidet (p ≥ 40 %, Vorteil ≥ 10 %, Bet365 ≤ 3,00); Odd Alerts als Leitschiene "
         "(höchstens 5 Punkte Abweichung, OA sieht keinen Nachteil). **Status Testbetrieb – nur auf Papier.**", "",
         "| Nr | Datum/Zeit (dt. Zeit) | Land | Wettbewerb | Art | Spiel | Tipp | Modell % | OA % | Bet365 | Vorteil | Match-ID |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, t in enumerate(tipps, 1):
        z.append(f"| {i} | {mez(t['unix'])} | {t['land']} | {t['wettbewerb']} | {t['art']} | {t['heim']} – {t['gast']} | "
                 f"{oa.MAERKTE[t['markt']]['label']} | {t['p_modell'] * 100:.0f} | {t['p_oa'] * 100:.0f} | "
                 f"{t['quote']:.2f} | {t['vorteil'] * 100:+.0f} % | {t['match_id']} |")
    with open(os.path.join(ROOT, "scans", f"oap21_{stamp}.md"), "w", encoding="utf8") as fh:
        fh.write("\n".join(z) + "\n")
    print(f"{stat['spiele_mit_prognose']} Spiele ({stat['ligaspiele']} Liga, {stat['pokalspiele']} Pokal), "
          f"{len(alle)} mit Modellwert, {len(tipps)} Tipps → scans/oap21_{stamp}.md")
    if a.erfassen:
        schon = bereits_erfasst()
        neu = 0
        for t in tipps:
            if t["match_id"] in schon:
                continue
            r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "werkzeuge", "tracker.py"), "erfassen",
                                "--match-id", str(t["match_id"]), "--markt", t["markt"], "--quelle", "system",
                                "--analyse-id", f"OAP21-{stamp}-{t['match_id']}",
                                "--notiz", f"{t['art']} {t['modell_name']} p={t['p_modell']:.4f} OA p={t['p_oa']:.4f} "
                                           f"q={t['quote']} Vorteil={t['vorteil']:.4f} lambda={t['lambda']}"],
                               capture_output=True, text=True, env={**os.environ, "TRACKER_SYSTEM": VERSION})
            if r.returncode == 0:
                neu += 1
            else:
                print("  nicht erfasst:", t["match_id"], (r.stdout + r.stderr).strip()[:150])
        print(f"{neu} neue Tipps im Tracker erfasst.")


if __name__ == "__main__":
    main()
