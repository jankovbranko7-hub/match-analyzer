"""API-Bild. Kein 70/30, keine Schwelle. Zweimal lesen, dann ein Tipp."""

from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request

BASE = "https://api.football-data-api.com"
FELDER = (
    "team_a_xg_prematch",
    "team_b_xg_prematch",
    "btts_potential",
    "o25_potential",
    "u25_potential",
)


def key() -> str:
    wert = os.environ.get("FOOTYSTATS_KEY") or os.environ.get("FOOTYSTATS_API_KEY")
    if not wert:
        raise SystemExit("FOOTYSTATS_KEY fehlt")
    return wert


def hole(endpoint: str, params: dict) -> dict:
    url = f"{BASE}/{endpoint}?" + urllib.parse.urlencode({**params, "key": key()})
    with urllib.request.urlopen(url, timeout=60) as r:
        daten = json.load(r)
    if not daten.get("success", True):
        raise SystemExit(f"API-Fehler {endpoint}: {daten.get('message')}")
    return daten


def zweimal(endpoint: str, params: dict) -> tuple[dict, dict]:
    erst = hole(endpoint, params)
    time.sleep(0.3)
    zweit = hole(endpoint, params)
    return erst, zweit


def feld(daten: dict, name: str):
    wert = daten.get(name)
    if wert in (None, "", 0) and name.endswith("_yes"):
        return "fehlt"
    if wert is None or wert == "":
        return "fehlt"
    return wert


def tipp(bild: dict) -> str:
    """Das höchste Potential benennt den Markt. xG benennt die Seite, wenn die Potentiale gleich sind."""
    werte = {
        "BTTS Ja": bild["btts_potential"],
        "Over 2.5": bild["o25_potential"],
        "Under 2.5": bild["u25_potential"],
    }
    if any(v == "fehlt" for v in werte.values()):
        return "kein Tipp, Potential fehlt"
    hoechster = max(werte.values())
    namen = [n for n, v in werte.items() if v == hoechster]
    if len(namen) == 1:
        return namen[0]
    hx, ax = bild["team_a_xg_prematch"], bild["team_b_xg_prematch"]
    if hx == "fehlt" or ax == "fehlt" or hx == ax:
        return "kein Tipp, Felder gleich hoch"
    return "Heimsieg" if hx > ax else "Auswärtssieg"


def spiel(match_id: int) -> dict:
    a, b = zweimal("match", {"match_id": match_id})
    da, db = a["data"], b["data"]
    if da.get("id") != db.get("id") or da.get("home_name") != db.get("home_name"):
        return {"frei": False, "fehler": "die zwei Abrufe sind nicht dasselbe Spiel"}
    bild = {name: feld(da, name) for name in FELDER}
    zweit = {name: feld(db, name) for name in FELDER}
    if bild != zweit:
        return {"frei": False, "fehler": "zweite Antwort weicht ab", "erst": bild, "zweit": zweit}
    return {
        "frei": True,
        "id": da.get("id"),
        "liga": da.get("competition_id"),
        "heim": da.get("home_name"),
        "gast": da.get("away_name"),
        "bild": bild,
        "tipp": tipp(bild),
    }


if __name__ == "__main__":
    import sys
    for mid in sys.argv[1:]:
        r = spiel(int(mid))
        print(json.dumps(r, ensure_ascii=False))
