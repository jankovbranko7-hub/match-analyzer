"""Erfolgs-Tracker (Vorabeinträge, getrennte Abrechnung, Bericht, Kalibrierung).

Befehle:
  erfassen     Tipp VOR dem Anpfiff speichern (unveränderlich, nur anhängen)
  abrechnen    Ergebnisse und Schlussquoten getrennt abrufen und speichern
  bericht      Auswertung je Quelle, Markt und Warnzeichen
  kalibrierung Prüft die Odd-Alerts-Wahrscheinlichkeiten über alle Scanner-Spiele

Beispiele:
  python3 werkzeuge/tracker.py erfassen --match-id 420673876 --markt btts --quelle system
  python3 werkzeuge/tracker.py erfassen --match-id 420673876 --markt keine --quelle system
  python3 werkzeuge/tracker.py erfassen --match-id 420673876 --markt heim --quelle oddalerts --quote 1.85
  python3 werkzeuge/tracker.py abrechnen
  python3 werkzeuge/tracker.py bericht
  python3 werkzeuge/tracker.py kalibrierung

Dateien:
  tracker/<System>/vorab.jsonl       Vorabeinträge (nie geändert)
  tracker/<System>/ergebnisse.jsonl  Ergebnisprüfungen (getrennt)
  Anderes System: Umgebungsvariable TRACKER_SYSTEM=OAP-1.0
  scans/ergebnisse.jsonl    Ergebnisse der Scanner-Spiele (für die Kalibrierung)
"""

import argparse
import glob
import json
import math
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCAN_ERGEB = os.path.join(ROOT, "scans", "ergebnisse.jsonl")
QUELLEN = ("system", "oddalerts", "andere")
try:
    with open(os.path.join(ROOT, "AKTIVES-SYSTEM.json"), encoding="utf8") as _f:
        SYSTEM = json.load(_f).get("revision", "unbekannt")
except (OSError, ValueError):
    SYSTEM = "unbekannt"
SYSTEM = os.environ.get("TRACKER_SYSTEM", SYSTEM)  # z. B. OAP-1.0 für alte Einträge
VORAB = os.path.join(ROOT, "tracker", SYSTEM, "vorab.jsonl")
ERGEB = os.path.join(ROOT, "tracker", SYSTEM, "ergebnisse.jsonl")


def lesen(pfad):
    if not os.path.exists(pfad):
        return []
    with open(pfad, encoding="utf8") as f:
        return [json.loads(z) for z in f if z.strip()]


def anhaengen(pfad, eintraege):
    os.makedirs(os.path.dirname(pfad), exist_ok=True)
    with open(pfad, "a", encoding="utf8") as f:
        for e in eintraege:
            f.write(json.dumps(e, ensure_ascii=False, separators=(",", ":")) + "\n")


# ---------------------------------------------------------------- erfassen
def erfassen(args):
    jetzt = oa.jetzt_utc()
    fx = oa.get("fixtures/" + str(args.match_id),
                {"include": "probability,odds", "bookmakers": "1,2",
                 "markets": oa.MARKT_IDS, "odds_type": "closing"})
    daten = fx.get("data") or []
    if not daten:
        sys.exit(f"Match-ID {args.match_id} nicht gefunden.")
    f = daten[0]
    if f.get("status") != "NS" or f["unix"] <= jetzt.timestamp():
        sys.exit(f"Nicht erfasst: Spiel hat bereits begonnen oder ist beendet "
                 f"(Status {f.get('status')}, Anstoß {oa.iso(f['unix'])}). "
                 "Nach dem Anpfiff ist es keine Vorhersage mehr.")
    quoten = oa.quoten_aus_fixture(f.get("odds"))
    nr = len(lesen(VORAB)) + 1
    eintrag = {
        "eintrag_id": f"T{nr:05d}-{args.match_id}",
        "system": SYSTEM,
        "erfasst_utc": jetzt.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "quelle": args.quelle,
        "analyse_id": args.analyse_id,
        "match_id": f["id"],
        "anstoss_utc": oa.iso(f["unix"]),
        "wettbewerb": f.get("competition_name"), "land": f.get("competition_country"),
        "saison_id": f.get("season_id"),
        "heim": f.get("home_name"), "heim_id": f.get("home_id"),
        "gast": f.get("away_name"), "gast_id": f.get("away_id"),
        "markt": args.markt,
        "warnung": bool(args.warnung),
        "warnung_text": args.warnung or None,
        "quote_eigen": args.quote,
        "quoten_bei_erfassung": quoten,
        "oa_wahrscheinlichkeit": oa.wahrscheinlichkeiten(f.get("probability")),
        "notiz": args.notiz,
        "abfrage": {"pfad": f"fixtures/{f['id']}", "include": "probability,odds",
                    "bookmakers": "1,2", "markets": oa.MARKT_IDS,
                    "odds_type": "closing", "api_token": "[REDACTED]"},
    }
    anhaengen(VORAB, [eintrag])
    label = "keine Wette" if args.markt == "keine" else oa.MAERKTE[args.markt]["label"]
    q = args.quote or (quoten["bet365"].get(args.markt) if args.markt != "keine" else None)
    print(f"Erfasst {eintrag['eintrag_id']}: {f['home_name']} – {f['away_name']} "
          f"({oa.iso(f['unix'])}) · {label}{' ⚠️' if args.warnung else ''} · "
          f"Quelle {args.quelle} · Quote {q if q else 'fehlt'}")


# ---------------------------------------------------------------- abrechnen
def ergebnis_fuer(fx):
    st = fx.get("status")
    if st in oa.ANNULLIERT:
        return {"status": st, "ausgang": "annulliert",
                "hinweis": "nach den Marktregeln des Buchmachers prüfen"}
    tore = oa.regulaere_tore(fx)
    if tore is None:
        if st in ("AET", "FT_PEN"):
            return {"status": st, "ausgang": "manuell",
                    "hinweis": "Ergebnis nach 90 Minuten nicht sicher bestimmbar"}
        return None  # noch offen
    return {"status": st, "tore_regulaer": [tore[0], tore[1]], "herkunft": tore[2],
            "ausgang": "beendet"}


def schlussquoten(ids):
    out = defaultdict(dict)
    ids = list(ids)
    for i in range(0, len(ids), 50):
        rows = oa.get("odds/history/multiple",
                      {"ids": ",".join(map(str, ids[i:i + 50])),
                       "markets": oa.MARKT_IDS, "bookmakers": "1,2"}).get("data") or []
        for r in rows:
            for name, info in oa.MAERKTE.items():
                if (r.get("market_key"), r.get("outcome")) == info["odds"]:
                    buch = {1: "pinnacle", 2: "bet365"}.get(r.get("bookmaker_id"))
                    if buch:
                        try:
                            out[r["fixture_id"]][f"{buch}_{name}"] = {
                                "eroeffnung": float(r["opening"]), "schluss": float(r["closing"])}
                        except (TypeError, ValueError, KeyError):
                            pass
    return out


def abrechnen(args):
    vorab = lesen(VORAB)
    erledigt = {e["eintrag_id"] for e in lesen(ERGEB)}
    offen = [v for v in vorab if v["eintrag_id"] not in erledigt]
    if not offen:
        print("Keine offenen Einträge.")
        return
    ids = sorted({v["match_id"] for v in offen})
    fxs = {f["id"]: f for f in oa.fixtures_by_ids(ids, {"include": "timings"})}
    sq = schlussquoten(ids)
    jetzt = oa.jetzt_utc().strftime("%Y-%m-%dT%H:%M:%SZ")
    neu, noch_offen = [], 0
    for v in offen:
        fx = fxs.get(v["match_id"])
        erg = ergebnis_fuer(fx) if fx else None
        if erg is None:
            noch_offen += 1
            continue
        if erg["ausgang"] == "beendet" and v["markt"] != "keine":
            h, a = erg["tore_regulaer"]
            erg["tipp"] = "Treffer" if oa.gewonnen(v["markt"], h, a) else "Niete"
        elif v["markt"] == "keine" and erg["ausgang"] == "beendet":
            erg["tipp"] = "keine Wette"
        erg.update({"eintrag_id": v["eintrag_id"], "match_id": v["match_id"],
                    "abruf_utc": jetzt, "quoten_historie": sq.get(v["match_id"], {})})
        neu.append(erg)
    anhaengen(ERGEB, neu)
    print(f"{len(neu)} Ergebnisse gespeichert, {noch_offen} noch offen.")
    for e in neu:
        v = next(x for x in offen if x["eintrag_id"] == e["eintrag_id"])
        t = e.get("tore_regulaer")
        print(f"  {v['eintrag_id']}: {v['heim']} – {v['gast']} "
              f"{f'{t[0]}:{t[1]}' if t else e['status']} · {v['markt']} → "
              f"{e.get('tipp', e['ausgang'])}")


# ---------------------------------------------------------------- bericht
def einsatzquote(v):
    """Quote, zu der abgerechnet wird: eigene Quote, sonst Bet365 bei Erfassung."""
    if v.get("quote_eigen"):
        return v["quote_eigen"], "eigene Quote"
    q = ((v.get("quoten_bei_erfassung") or {}).get("bet365") or {}).get(v["markt"])
    return (q, "Bet365 bei Erfassung (hypothetisch)") if q else (None, "Quote fehlt")


def bericht(args):
    vorab = {v["eintrag_id"]: v for v in lesen(VORAB)}
    ergeb = {e["eintrag_id"]: e for e in lesen(ERGEB)}
    if not vorab:
        print("Noch keine Einträge.")
        return
    gruppen = defaultdict(list)
    for eid, v in vorab.items():
        e = ergeb.get(eid)
        for schluessel in (("alle", v["quelle"]), (v["markt"], v["quelle"]),
                           ("mit ⚠️" if v["warnung"] else "ohne ⚠️", v["quelle"])):
            gruppen[schluessel].append((v, e))
    print(f"Bericht System {SYSTEM} · {len(vorab)} Einträge, {len(ergeb)} abgerechnet\n")
    print("Gruppe | Quelle | erfasst | keine | Tipps abgerechnet | Treffer | Trefferquote ± SE "
          "| Gewinn (1 E.) | ROI | CLV vs. Pinnacle-Schluss | Ø OA-% | Brier OA | offen/annull./manuell")
    print("---|---|---|---|---|---|---|---|---|---|---|---|---")
    reihen = ["alle", "heim", "remis", "auswaerts", "btts", "btts_nein", "over25", "under25", "keine",
              "mit ⚠️", "ohne ⚠️"]
    for g in reihen:
        for q in QUELLEN:
            liste = gruppen.get((g, q))
            if not liste:
                continue
            keine = sum(1 for v, _ in liste if v["markt"] == "keine")
            tipps = [(v, e) for v, e in liste if v["markt"] != "keine"
                     and e and e.get("tipp") in ("Treffer", "Niete")]
            rest = sum(1 for v, e in liste if v["markt"] != "keine"
                       and not (e and e.get("tipp") in ("Treffer", "Niete")))
            n = len(tipps)
            treffer = sum(1 for _, e in tipps if e["tipp"] == "Treffer")
            if n:
                p = treffer / n
                se = math.sqrt(p * (1 - p) / n)
                quote_n, gewinn = 0, 0.0
                clv = []
                briers, ps = [], []
                for v, e in tipps:
                    qv, _ = einsatzquote(v)
                    if qv:
                        quote_n += 1
                        gewinn += (qv - 1) if e["tipp"] == "Treffer" else -1
                        pin = (e.get("quoten_historie") or {}).get(f"pinnacle_{v['markt']}")
                        if pin and pin.get("schluss"):
                            clv.append(qv / pin["schluss"] - 1)
                    op = (v.get("oa_wahrscheinlichkeit") or {}).get(v["markt"])
                    if op is not None:
                        ps.append(op)
                        briers.append((op / 100 - (1 if e["tipp"] == "Treffer" else 0)) ** 2)
                roi = f"{gewinn / quote_n * 100:+.1f} % (n={quote_n})" if quote_n else "fehlt"
                g_txt = f"{gewinn:+.2f}" if quote_n else "fehlt"
                clv_txt = f"{sum(clv) / len(clv) * 100:+.1f} % (n={len(clv)})" if clv else "fehlt"
                ps_txt = f"{sum(ps) / len(ps):.0f} %" if ps else "fehlt"
                br_txt = f"{sum(briers) / len(briers):.3f}" if briers else "fehlt"
                tq = f"{p * 100:.1f} % ± {se * 100:.1f}"
            else:
                tq = g_txt = roi = clv_txt = ps_txt = br_txt = "–"
            print(f"{g} | {q} | {len(liste)} | {keine} | {n} | {treffer} | {tq} | {g_txt} | "
                  f"{roi} | {clv_txt} | {ps_txt} | {br_txt} | {rest}")
    print("\nHinweise: „keine“ zählt weder als Treffer noch als Verlust. Gewinn bei 1 Einheit "
          "pro Tipp; ohne eigene Quote mit Bet365 zum Erfassungszeitpunkt gerechnet "
          "(hypothetisch, Steuern/Gebühren nicht berücksichtigt). CLV > 0 heißt: Quote "
          "besser als Pinnacle-Schlussquote. Kleine Stichproben sind kein Nachweis.")


# ---------------------------------------------------------------- kalibrierung
def kalibrierung(args):
    snapshot = {}
    for pfad in sorted(glob.glob(os.path.join(ROOT, "scans", "scan_*.json"))):
        with open(pfad, encoding="utf8") as f:
            d = json.load(f)
        abruf = d["meta"]["abruf_utc"]
        for s in d["spiele"]:
            if s.get("oa_wahrscheinlichkeit") and abruf < s["anstoss_utc"]:
                alt = snapshot.get(s["match_id"])
                if not alt or alt[0] < abruf:  # letzter Stand vor Anpfiff
                    snapshot[s["match_id"]] = (abruf, s)
    if not snapshot:
        print("Keine Scans vorhanden.")
        return
    bekannt = {e["match_id"]: e for e in lesen(SCAN_ERGEB)}
    jetzt = oa.jetzt_utc().strftime("%Y-%m-%dT%H:%M:%SZ")
    fehlend = [m for m, (_, s) in snapshot.items()
               if m not in bekannt and s["anstoss_utc"] < jetzt]
    if fehlend:
        neu = []
        for fx in oa.fixtures_by_ids(sorted(fehlend), {"include": "timings"}):
            erg = ergebnis_fuer(fx)
            if erg:
                erg.update({"match_id": fx["id"], "abruf_utc": jetzt})
                neu.append(erg)
        anhaengen(SCAN_ERGEB, neu)
        for e in neu:
            bekannt[e["match_id"]] = e
    print(f"Kalibrierung der Odd-Alerts-Wahrscheinlichkeiten · {len(snapshot)} gescannte Spiele, "
          f"{sum(1 for m in snapshot if bekannt.get(m, {}).get('ausgang') == 'beendet')} beendet\n")
    print("Markt | Spiele | Brier | Log-Loss | Gruppen (OA-% → tatsächlich, n)")
    print("---|---|---|---|---")
    for markt, info in oa.MAERKTE.items():
        paare = []
        for m, (_, s) in snapshot.items():
            e = bekannt.get(m)
            p = (s["oa_wahrscheinlichkeit"] or {}).get(markt)
            if e and e.get("ausgang") == "beendet" and p is not None:
                h, a = e["tore_regulaer"]
                paare.append((p / 100, 1 if oa.gewonnen(markt, h, a) else 0))
        if not paare:
            print(f"{info['label']} | 0 | – | – | –")
            continue
        brier = sum((p - y) ** 2 for p, y in paare) / len(paare)
        eps = 1e-6
        ll = -sum(y * math.log(max(p, eps)) + (1 - y) * math.log(max(1 - p, eps))
                  for p, y in paare) / len(paare)
        gr = []
        for lo in range(0, 100, 10):
            b = [(p, y) for p, y in paare if lo / 100 <= p < (lo + 10) / 100 or (lo == 90 and p == 1)]
            if b:
                gr.append(f"{lo}–{lo + 10}: {sum(p for p, _ in b) / len(b) * 100:.0f}→"
                          f"{sum(y for _, y in b) / len(b) * 100:.0f} % (n={len(b)})")
        print(f"{info['label']} | {len(paare)} | {brier:.3f} | {ll:.3f} | {'; '.join(gr)}")
    print("\nHinweis: Gute Kalibrierung heißt nicht Gewinn – dafür zählt der Vergleich mit der Quote.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="befehl", required=True)
    e = sub.add_parser("erfassen", help="Tipp vor dem Anpfiff speichern")
    e.add_argument("--match-id", type=int, required=True)
    e.add_argument("--markt", required=True, choices=list(oa.MAERKTE) + ["keine"])
    e.add_argument("--quelle", required=True, choices=QUELLEN)
    e.add_argument("--warnung", metavar="TEXT", help="⚠️ mit konkreter Gefahr")
    e.add_argument("--quote", type=float, help="tatsächlich erhaltene Quote (optional)")
    e.add_argument("--analyse-id", help="Verweis auf den Vorabeintrag in protokoll/")
    e.add_argument("--notiz")
    sub.add_parser("abrechnen", help="Ergebnisse abrufen")
    sub.add_parser("bericht", help="Auswertung anzeigen")
    sub.add_parser("kalibrierung", help="Odd-Alerts-Wahrscheinlichkeiten prüfen")
    args = ap.parse_args()
    try:
        {"erfassen": erfassen, "abrechnen": abrechnen, "bericht": bericht,
         "kalibrierung": kalibrierung}[args.befehl](args)
    except oa.OAError as err:
        sys.exit(f"Fehler: {err}")


if __name__ == "__main__":
    main()
