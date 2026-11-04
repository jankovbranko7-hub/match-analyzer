"""Daten-Dossier für ein Spiel nach System v1.3-OA (Abschnitte 2–4).

Berechnet die Mannschaftstabellen (Gesamt | Heim | Auswärts | letzte 6) direkt aus den
Einzelspielen der Odd-Alerts-API (Rohdaten, nichts geschätzt) und vergleicht Spielzahl
und Tore mit der API-Saisonstatistik. Verwendet nur Spiele vor dem Abrufzeitpunkt.

Aufruf:  python3 werkzeuge/dossier.py MATCH_ID [MATCH_ID ...] --ausgabe protokoll/daten
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def team_spiele(team_id, vor_unix):
    rows = oa.get("fixtures/team/" + str(team_id),
                  {"per_page": 250, "include": "stats"}).get("data") or []
    out = []
    for f in rows:
        if f["unix"] >= vor_unix or f.get("is_friendly"):
            continue
        out.append(f)
    out.sort(key=lambda f: f["unix"])
    return out


def einzel(f, team_id):
    """Ein Spiel aus Sicht der Mannschaft. None, wenn nicht als reguläres Ergebnis verwendbar."""
    if f.get("status") != "FT" or f.get("home_goals") is None:
        return None
    heim = f["home_id"] == team_id
    tf, tg = (f["home_goals"], f["away_goals"]) if heim else (f["away_goals"], f["home_goals"])
    st = f.get("stats") or {}
    xf, xg_ = (st.get("home_xg"), st.get("away_xg")) if heim else (st.get("away_xg"), st.get("home_xg"))
    ht = f.get("ht_score")
    tore_2hz = None
    if isinstance(ht, str) and "-" in ht:
        try:
            a, b = (int(v) for v in ht.split("-"))
            tore_2hz = f["home_goals"] + f["away_goals"] - a - b
        except ValueError:
            pass
    return {
        "match_id": f["id"], "datum": oa.iso(f["unix"])[:10], "unix": f["unix"],
        "wettbewerb": f.get("competition_name"), "wettbewerb_id": f.get("competition_id"),
        "wettbewerbstyp": f.get("competition_type"), "saison_id": f.get("season_id"),
        "ort": "H" if heim else "A",
        "gegner": f["away_name"] if heim else f["home_name"],
        "gegner_id": f["away_id"] if heim else f["home_id"],
        "tore": tf, "gegentore": tg,
        "xg": float(xf) if xf is not None else None,
        "xg_gegen": float(xg_) if xg_ is not None else None,
        "tore_2hz": tore_2hz,
    }


def kennzahlen(sp):
    n = len(sp)
    if n == 0:
        return {"Spiele": 0}
    s = lambda k: sum(x[k] for x in sp)  # noqa: E731
    pct = lambda c: round(100 * sum(1 for x in sp if c(x)) / n, 1)  # noqa: E731
    w = sum(1 for x in sp if x["tore"] > x["gegentore"])
    d = sum(1 for x in sp if x["tore"] == x["gegentore"])
    xgs = [x for x in sp if x["xg"] is not None and x["xg_gegen"] is not None]
    hz2 = [x for x in sp if x["tore_2hz"] is not None]
    return {
        "Spiele": n,
        "Tore": s("tore"), "Gegentore": s("gegentore"),
        "Tore/Spiel": round(s("tore") / n, 2), "Gegentore/Spiel": round(s("gegentore") / n, 2),
        "xG für/Spiel": round(sum(x["xg"] for x in xgs) / len(xgs), 2) if xgs else "fehlt",
        "xG gegen/Spiel": round(sum(x["xg_gegen"] for x in xgs) / len(xgs), 2) if xgs else "fehlt",
        "Spiele mit xG": len(xgs),
        "S/U/N": f"{w}/{d}/{n - w - d}",
        "Punkte/Spiel": round((3 * w + d) / n, 2),
        "BTTS %": pct(lambda x: x["tore"] > 0 and x["gegentore"] > 0),
        "Over 2,5 %": pct(lambda x: x["tore"] + x["gegentore"] >= 3),
        "Under 2,5 %": pct(lambda x: x["tore"] + x["gegentore"] <= 2),
        "Clean Sheets %": pct(lambda x: x["gegentore"] == 0),
        "Failed to Score %": pct(lambda x: x["tore"] == 0),
        "BTTS-and-lose %": pct(lambda x: x["tore"] > 0 and x["gegentore"] > 0 and x["tore"] < x["gegentore"]),
        "Tore 2. HZ/Spiel": round(sum(x["tore_2hz"] for x in hz2) / len(hz2), 2) if hz2 else "fehlt",
    }


def tabelle(spiele, saison_id, wettbewerb_id):
    sp = [x for x in spiele if x and x["saison_id"] == saison_id and x["wettbewerb_id"] == wettbewerb_id]
    l6 = sp[-6:]
    zeitraum = lambda L: f"{L[0]['datum']} bis {L[-1]['datum']}" if L else "–"  # noqa: E731
    return {
        "wettbewerb": sp[0]["wettbewerb"] if sp else None,
        "saison_id": saison_id,
        "spalten": {
            "Gesamt": kennzahlen(sp),
            "Heim": kennzahlen([x for x in sp if x["ort"] == "H"]),
            "Auswärts": kennzahlen([x for x in sp if x["ort"] == "A"]),
            "letzte 6": kennzahlen(l6),
        },
        "zeitraum": {"Saison": zeitraum(sp), "letzte 6": zeitraum(l6)},
        "einzelspiele": sp,
    }


def api_abgleich(saison_id, team_id):
    try:
        d = oa.get("stats/season/" + str(saison_id), {"teams": team_id}).get("data") or []
    except oa.OAError as e:
        return {"fehler": str(e)}
    for t in d:
        if t.get("team_id") == team_id:
            return {"Spiele": t["played"]["total"], "Tore": t["goals_for"]["total"],
                    "Gegentore": t["goals_against"]["total"],
                    "xG-Abdeckung": (t.get("coverage") or {}).get("xg")}
    return {"fehler": "Team nicht in Saisonstatistik"}


def liga_saison(spiele, wettbewerb_id):
    """Aktuelle nationale Liga-Saison (letztes Ligaspiel außerhalb des betrachteten Wettbewerbs)."""
    for x in reversed(spiele):
        if x and x["wettbewerbstyp"] == "League" and x["wettbewerb_id"] != wettbewerb_id:
            return x["saison_id"], x["wettbewerb_id"]
    return None, None


def dossier(match_id):
    abruf = oa.jetzt_utc()
    f = oa.get("fixtures/" + str(match_id), {"include": "probability,odds", "bookmakers": "1,2",
                                              "markets": oa.MARKT_IDS, "odds_type": "closing"})["data"][0]
    out = {
        "abruf_utc": abruf.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "identitaet": {k: f.get(k) for k in (
            "id", "home_id", "home_name", "away_id", "away_name", "competition_id",
            "competition_name", "competition_country", "competition_type", "season_id",
            "season", "status", "venue", "is_cup", "is_friendly", "home_position",
            "away_position", "season_progress")},
        "anstoss_utc": oa.iso(f["unix"]),
        "quoten_aktuell": oa.quoten_aus_fixture(f.get("odds")),
        "oa_wahrscheinlichkeit": oa.wahrscheinlichkeiten(f.get("probability")),
        "teams": {},
    }
    for seite, tid in (("heim", f["home_id"]), ("gast", f["away_id"])):
        roh = team_spiele(tid, abruf.timestamp())
        ein = [einzel(x, tid) for x in roh]
        nicht_ft = [{"datum": oa.iso(x["unix"])[:10], "wettbewerb": x.get("competition_name"),
                     "status": x.get("status")} for x in roh
                    if x.get("status") != "FT" and x["unix"] > abruf.timestamp() - 400 * 86400]
        team = {"id": tid, "name": f["home_name"] if seite == "heim" else f["away_name"],
                "wettbewerb": tabelle(ein, f["season_id"], f["competition_id"]),
                "api_abgleich_wettbewerb": api_abgleich(f["season_id"], tid),
                "letzte_6_alle": [x for x in ein if x][-6:],
                "nicht_gewertet_letzte_400_tage": nicht_ft[-10:]}
        if f.get("competition_type") != "League" or f.get("is_cup"):
            ls, lw = liga_saison(ein, f["competition_id"])
            if ls:
                team["liga"] = tabelle(ein, ls, lw)
                team["api_abgleich_liga"] = api_abgleich(ls, tid)
        out["teams"][seite] = team
    return out


ZEILEN = ["Spiele", "Tore", "Gegentore", "Tore/Spiel", "Gegentore/Spiel", "xG für/Spiel",
          "xG gegen/Spiel", "Spiele mit xG", "S/U/N", "Punkte/Spiel", "BTTS %", "Over 2,5 %",
          "Under 2,5 %", "Clean Sheets %", "Failed to Score %", "BTTS-and-lose %", "Tore 2. HZ/Spiel"]


def md_tabelle(name, tab, abgleich):
    sp = tab["spalten"]
    z = [f"**{name} – {tab['wettbewerb']}** (Saison-ID {tab['saison_id']}; Saison "
         f"{tab['zeitraum']['Saison']}; letzte 6: {tab['zeitraum']['letzte 6']}; "
         f"API-Abgleich: {abgleich})", "",
         "| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |", "|---|---|---|---|---|"]
    for r in ZEILEN:
        z.append(f"| {r} | " + " | ".join(str(sp[c].get(r, 'fehlt')) for c in
                                         ("Gesamt", "Heim", "Auswärts", "letzte 6")) + " |")
    z += ["", "Einzelspiele (Saison, chronologisch): " + "; ".join(
        f"{x['datum'][5:]} {x['ort']} {x['gegner']} {x['tore']}:{x['gegentore']}"
        + (f" (xG {x['xg']:.1f}:{x['xg_gegen']:.1f})" if x['xg'] is not None else "")
        for x in tab["einzelspiele"]), ""]
    return "\n".join(z)


def markdown(d):
    i = d["identitaet"]
    z = [f"### {i['home_name']} – {i['away_name']} | {d['anstoss_utc']} | "
         f"{i['competition_country']} · {i['competition_name']} | Match-ID {i['id']}", "",
         f"Abruf: {d['abruf_utc']} · Saison {i['season']} (ID {i['season_id']}) · Status {i['status']} · "
         f"Teams {i['home_id']} / {i['away_id']} · Tabellenplatz {i['home_position']} / {i['away_position']}", ""]
    for seite in ("heim", "gast"):
        t = d["teams"][seite]
        z.append(md_tabelle(t["name"], t["wettbewerb"], t["api_abgleich_wettbewerb"]))
        if "liga" in t:
            z.append(md_tabelle(t["name"], t["liga"], t.get("api_abgleich_liga")))
        z.append(f"Letzte 6 alle Wettbewerbe {t['name']}: " + "; ".join(
            f"{x['datum'][5:]} {x['wettbewerb']} {x['ort']} {x['gegner']} {x['tore']}:{x['gegentore']}"
            for x in t["letzte_6_alle"]))
        if t["nicht_gewertet_letzte_400_tage"]:
            z.append(f"Nicht als reguläres Ergebnis gewertet: {t['nicht_gewertet_letzte_400_tage']}")
        z.append("")
    p, q = d["oa_wahrscheinlichkeit"], d["quoten_aktuell"]
    z.append(f"Odd-Alerts-% (Kontext): {p}")
    z.append(f"Quoten aktuell: Bet365 {q['bet365']}; Pinnacle {q['pinnacle']}")
    return "\n".join(z) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+", type=int)
    ap.add_argument("--ausgabe", default=os.path.join(ROOT, "protokoll", "daten"))
    a = ap.parse_args()
    os.makedirs(a.ausgabe, exist_ok=True)
    for mid in a.ids:
        try:
            d = dossier(mid)
        except oa.OAError as e:
            print(f"{mid}: Fehler {e}")
            continue
        base = os.path.join(a.ausgabe, f"dossier_{mid}")
        with open(base + ".json", "w", encoding="utf8") as fh:
            json.dump(d, fh, ensure_ascii=False, separators=(",", ":"))
        with open(base + ".md", "w", encoding="utf8") as fh:
            fh.write(markdown(d))
        print(f"{mid}: {d['identitaet']['home_name']} – {d['identitaet']['away_name']} → {base}.md")


if __name__ == "__main__":
    main()
