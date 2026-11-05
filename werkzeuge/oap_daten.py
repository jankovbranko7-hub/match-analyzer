"""Datenspeicher für das eigene Modell (OAP-2.0): Ligaspiele je Wettbewerb.

Speichert je Wettbewerb kompakt alle Spiele der laufenden und der vorherigen Saison
(Ergebnis, Status, xG falls vorhanden) in .cache/oap/comp_<id>.json (nicht im Git).
Aktualisierung lädt nur neue Seiten, bis bekannte abgeschlossene Spiele erreicht sind.

Aufruf:
  python3 werkzeuge/oap_daten.py 68 859 750        # bestimmte Wettbewerbe
  python3 werkzeuge/oap_daten.py --datei ids.txt    # IDs aus Datei (eine pro Zeile)
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache", "oap")
SAISONS = 2  # laufende + vorherige


def kompakt(f):
    st = f.get("stats") or {}
    return {"id": f["id"], "u": f["unix"], "s": f.get("season_id"), "st": f.get("status"),
            "h": f["home_id"], "a": f["away_id"], "hg": f.get("home_goals"), "ag": f.get("away_goals"),
            "hx": st.get("home_xg"), "ax": st.get("away_xg"), "fr": bool(f.get("is_friendly")),
            "ht": f.get("ht_score")}


def pfad(cid):
    return os.path.join(CACHE, f"comp_{cid}.json")


def laden(cid):
    try:
        with open(pfad(cid), encoding="utf8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def aktualisieren(cid):
    alt = laden(cid)
    bekannt = {s["id"]: s for s in (alt or {}).get("spiele", [])}
    fertig_bekannt = {i for i, s in bekannt.items() if s["st"] == "FT"}
    saisons, neu, page = [], {}, 1
    while True:
        d = oa.get("fixtures/competition/" + str(cid),
                   {"per_page": 250, "page": page, "order": "desc", "include": "stats"})
        rows = d.get("data") or []
        stop = False
        treffer_bekannt = 0
        for f in rows:
            s = f.get("season_id")
            if s not in saisons:
                if len(saisons) == SAISONS:
                    stop = True
                    break
                saisons.append(s)
            neu[f["id"]] = kompakt(f)
            if f["id"] in fertig_bekannt:
                treffer_bekannt += 1
        # Wenn eine ganze Seite nur aus bereits abgeschlossenen bekannten Spielen besteht: Rest aus Cache
        if alt and rows and treffer_bekannt == len(rows):
            for i, s in bekannt.items():
                if i not in neu and s["s"] in saisons:
                    neu[i] = s
            break
        if stop or not rows or not (d.get("info") or {}).get("next_page_url"):
            break
        page += 1
    spiele = sorted(neu.values(), key=lambda s: (s["u"], s["id"]))
    os.makedirs(CACHE, exist_ok=True)
    with open(pfad(cid), "w", encoding="utf8") as fh:
        json.dump({"wettbewerb_id": cid, "saisons": saisons, "abruf_utc": oa.jetzt_utc().strftime("%Y-%m-%dT%H:%M:%SZ"),
                   "spiele": spiele}, fh, separators=(",", ":"))
    return len(spiele)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", type=int)
    ap.add_argument("--datei")
    a = ap.parse_args()
    ids = list(a.ids)
    if a.datei:
        ids += [int(z) for z in open(a.datei) if z.strip()]
    for n, cid in enumerate(ids, 1):
        try:
            k = aktualisieren(cid)
            print(f"[{n}/{len(ids)}] {cid}: {k} Spiele", flush=True)
        except oa.OAError as e:
            print(f"[{n}/{len(ids)}] {cid}: Fehler {e}", flush=True)


if __name__ == "__main__":
    main()
