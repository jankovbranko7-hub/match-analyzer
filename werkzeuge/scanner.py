"""Spiele-Scanner: listet ALLE kommenden Spiele mit Odd-Alerts-Wahrscheinlichkeiten
und Quoten – ohne Grenzen und ohne Vorauswahl. Die Entscheidung trifft das
System v1.3-OA.

Aufruf:
  python3 werkzeuge/scanner.py                 # nächste 24 Stunden
  python3 werkzeuge/scanner.py --stunden 48
  python3 werkzeuge/scanner.py --datum 2026-11-07   # ein Kalendertag (UTC)

Ergebnis: scans/scan_<Zeit>.json (Rohdaten-Snapshot) und scans/scan_<Zeit>.md (Liste).
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def zeitraum(args):
    if args.datum:
        start = datetime.strptime(args.datum, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return int(start.timestamp()), int((start + timedelta(days=1)).timestamp()) - 1
    now = oa.jetzt_utc()
    return int(now.timestamp()), int((now + timedelta(hours=args.stunden)).timestamp())


def scan(von, bis):
    basis = {"from": von, "to": bis, "per_page": 250, "bookmakers": "1,2",
             "markets": oa.MARKT_IDS}
    eroeffnung = oa.get_all("fixtures/upcoming",
                            {**basis, "include": "probability,odds", "odds_type": "opening"})
    aktuell = {f["id"]: f for f in oa.get_all(
        "fixtures/upcoming", {**basis, "include": "odds", "odds_type": "closing"})}
    spiele, gesehen = [], set()
    for f in eroeffnung:
        if f["id"] in gesehen:
            continue
        gesehen.add(f["id"])
        q_er = oa.quoten_aus_fixture(f.get("odds"))
        q_ak = oa.quoten_aus_fixture((aktuell.get(f["id"]) or {}).get("odds"))
        spiele.append({
            "match_id": f["id"],
            "anstoss_utc": oa.iso(f["unix"]),
            "unix": f["unix"],
            "status": f.get("status"),
            "wettbewerb": f.get("competition_name"),
            "wettbewerb_id": f.get("competition_id"),
            "land": f.get("competition_country"),
            "wettbewerbstyp": f.get("competition_type"),
            "saison_id": f.get("season_id"),
            "saison": f.get("season"),
            "heim": f.get("home_name"), "heim_id": f.get("home_id"),
            "gast": f.get("away_name"), "gast_id": f.get("away_id"),
            "heim_spiele": f.get("home_played"), "gast_spiele": f.get("away_played"),
            "pokal": f.get("is_cup"), "freundschaftsspiel": f.get("is_friendly"),
            "oa_vorhersagbarkeit": f.get("competition_predictability"),
            "oa_wahrscheinlichkeit": oa.wahrscheinlichkeiten(f.get("probability")),
            "quoten": {
                "bet365": {"eroeffnung": q_er["bet365"], "aktuell": q_ak["bet365"]},
                "pinnacle": {"eroeffnung": q_er["pinnacle"], "aktuell": q_ak["pinnacle"]},
            },
        })
    spiele.sort(key=lambda s: (s["unix"], s["wettbewerb"] or "", s["match_id"]))
    return spiele


def fmt_p(p, k):
    if not p or p.get(k) is None:
        return "–"
    return f"{p[k]:.0f}"


def fmt_q(q, k):
    v = (q or {}).get(k)
    return "–" if v is None else f"{v:.2f}"


def markdown(meta, spiele):
    z = [f"# Spiele-Scanner {meta['abruf_utc']}", "",
         f"Zeitraum (UTC): {meta['von_utc']} bis {meta['bis_utc']} · {len(spiele)} Spiele · "
         "Quelle: Odd Alerts API.",
         "",
         "**Keine Filter, keine Grenzen, keine Empfehlung.** Die Liste zeigt nur, was "
         "Odd Alerts liefert. Ob und welcher Tipp gespielt wird, entscheidet allein das "
         "System v1.3-OA nach vollständiger Analyse.",
         "",
         "OA % = Odd-Alerts-Wahrscheinlichkeit (Kontext, kein Modell im Sinne von "
         "Abschnitt 5). Quoten: Bet365 Eröffnung / aktuell. „–“ = fehlt.",
         "",
         "| Nr | Anstoß UTC | Wettbewerb | Spiel | Match-ID | OA % H/X/A | OA % BTTS | "
         "OA % O/U 2,5 | Bet365 H/X/A (Eröff.) | Bet365 BTTS | Bet365 O/U 2,5 | "
         "Bet365 H/X/A (aktuell) |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, s in enumerate(spiele, 1):
        p = s["oa_wahrscheinlichkeit"]
        e = s["quoten"]["bet365"]["eroeffnung"]
        a = s["quoten"]["bet365"]["aktuell"]
        wb = f"{s['land'] or ''} · {s['wettbewerb'] or ''}".strip(" ·")
        z.append(
            f"| {i} | {s['anstoss_utc'][:16].replace('T', ' ')} | {wb} | "
            f"{s['heim']} – {s['gast']} | {s['match_id']} | "
            f"{fmt_p(p, 'heim')}/{fmt_p(p, 'remis')}/{fmt_p(p, 'auswaerts')} | "
            f"{fmt_p(p, 'btts')} | {fmt_p(p, 'over25')}/{fmt_p(p, 'under25')} | "
            f"{fmt_q(e, 'heim')}/{fmt_q(e, 'remis')}/{fmt_q(e, 'auswaerts')} | "
            f"{fmt_q(e, 'btts')} | {fmt_q(e, 'over25')}/{fmt_q(e, 'under25')} | "
            f"{fmt_q(a, 'heim')}/{fmt_q(a, 'remis')}/{fmt_q(a, 'auswaerts')} |")
    return "\n".join(z) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stunden", type=int, default=24)
    ap.add_argument("--datum", help="Kalendertag JJJJ-MM-TT (UTC)")
    args = ap.parse_args()
    von, bis = zeitraum(args)
    abruf = oa.jetzt_utc()
    try:
        spiele = scan(von, bis)
    except oa.OAError as e:
        sys.exit(f"Fehler: {e}")
    meta = {
        "werkzeug": "scanner", "system": "v1.3-OA",
        "abruf_utc": abruf.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "von_utc": oa.iso(von), "bis_utc": oa.iso(bis),
        "quelle": "Odd Alerts API, fixtures/upcoming",
        "abfrageparameter": {"from": von, "to": bis, "include": "probability,odds",
                             "bookmakers": "1,2", "markets": oa.MARKT_IDS,
                             "odds_type": "opening + closing", "api_token": "[REDACTED]"},
        "filter": "keine",
        "anzahl": len(spiele),
    }
    os.makedirs(os.path.join(ROOT, "scans"), exist_ok=True)
    stamp = abruf.strftime("%Y-%m-%dT%H%MZ")
    pj = os.path.join(ROOT, "scans", f"scan_{stamp}.json")
    pm = os.path.join(ROOT, "scans", f"scan_{stamp}.md")
    with open(pj, "w", encoding="utf8") as f:
        json.dump({"meta": meta, "spiele": spiele}, f, ensure_ascii=False, separators=(",", ":"))
    with open(pm, "w", encoding="utf8") as f:
        f.write(markdown(meta, spiele))
    print(f"{len(spiele)} Spiele gespeichert:\n  {os.path.relpath(pm, ROOT)}\n  {os.path.relpath(pj, ROOT)}")


if __name__ == "__main__":
    main()
