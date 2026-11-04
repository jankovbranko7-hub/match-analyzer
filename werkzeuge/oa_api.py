"""Gemeinsame Hilfen für die Odd-Alerts-API (nur Python-Standardbibliothek).

Der Schlüssel kommt ausschließlich aus der Umgebungsvariable ODDALERTS_KEY.
Er wird nie ausgegeben, geloggt oder gespeichert; Fehlermeldungen enthalten
nur den Pfad, nie die URL mit Schlüssel.
"""

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

BASE = "https://data.oddalerts.com/api/"

# Bookmaker-IDs laut API: 1 = Pinnacle, 2 = Bet365
BUCHMACHER = {"pinnacle": "pinnacle", "bet365": "bet365"}
MARKT_IDS = "6,9,13"  # ft_result, btts, total_goals

# Die fünf erlaubten Märkte des Systems v1.3-OA (Abschnitt 1)
MAERKTE = {
    "heim": {"label": "Heimsieg", "prob": "home_win", "odds": ("ft_result", "home")},
    "auswaerts": {"label": "Auswärtssieg", "prob": "away_win", "odds": ("ft_result", "away")},
    "btts": {"label": "BTTS Ja", "prob": "btts", "odds": ("btts", "yes")},
    "over25": {"label": "Over 2,5", "prob": "o25", "odds": ("total_goals", "over_25")},
    "under25": {"label": "Under 2,5", "prob": "u25", "odds": ("total_goals", "under_25")},
}
# Remis nur als Information (kein erlaubter Markt)
REMIS = {"prob": "draw", "odds": ("ft_result", "draw")}

ANNULLIERT = {"POSTPONED", "CANCELLED", "ABANDONED", "AWARDED", "SUSPENDED",
              "INTERRUPTED", "DELETED"}


class OAError(Exception):
    pass


def _key():
    k = os.environ.get("ODDALERTS_KEY", "").strip()
    if not k:
        raise OAError("ODDALERTS_KEY fehlt in der Umgebung – bitte in den "
                      "Umgebungseinstellungen hinterlegen.")
    return k


def _redact(text, key):
    return text.replace(key, "[REDACTED]") if key else text


def get(path, params=None, retries=5):
    key = _key()
    p = dict(params or {})
    p["api_token"] = key
    url = BASE + path.lstrip("/") + "?" + urllib.parse.urlencode(p)
    for versuch in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                body = r.read()
        except urllib.error.HTTPError as e:
            body = e.read()
            if e.code in (417, 429, 500, 502, 503, 504) and versuch < retries - 1:
                time.sleep(min(60, 10 * (versuch + 1)))
                continue
            raise OAError(f"HTTP {e.code} bei /{path}: "
                          f"{_redact(body[:200].decode('utf8', 'replace'), key)}")
        except urllib.error.URLError as e:
            if versuch < retries - 1:
                time.sleep(5 * (versuch + 1))
                continue
            raise OAError(f"Netzwerkfehler bei /{path}: {type(e).__name__}")
        try:
            data = json.loads(body)
        except ValueError:
            raise OAError(f"Keine JSON-Antwort bei /{path} (Endpunkt unbekannt?)")
        if isinstance(data, dict) and isinstance(data.get("original"), dict) \
                and "error" in data["original"]:
            raise OAError(f"API-Fehler bei /{path}: {data['original']['error']}")
        return data
    raise OAError(f"Kein Erfolg bei /{path}")


def get_all(path, params=None):
    """Alle Seiten abrufen (Pagination über info.next_page_url)."""
    p = dict(params or {})
    out, page = [], 1
    while True:
        p["page"] = page
        d = get(path, p)
        rows = d.get("data") or []
        out += rows
        if not rows or not (d.get("info") or {}).get("next_page_url"):
            return out
        page += 1


def fixtures_by_ids(ids, extra=None):
    """Spiele per ID abrufen, 50 pro Aufruf."""
    ids = list(ids)
    out = []
    for i in range(0, len(ids), 50):
        params = {"ids": ",".join(map(str, ids[i:i + 50])), "per_page": 50}
        params.update(extra or {})
        out += get_all("fixtures/multiple", params)
    return out


def jetzt_utc():
    return datetime.now(timezone.utc)


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def quoten_aus_fixture(odds):
    """Verschachtelte include=odds-Antwort in {buchmacher: {markt: quote}} umwandeln."""
    out = {}
    for buch in BUCHMACHER:
        m = (odds or {}).get(buch) or {}
        werte = {}
        for name, info in list(MAERKTE.items()) + [("remis", REMIS)]:
            mk, oc = info["odds"]
            v = (m.get(mk) or {}).get(oc)
            werte[name] = float(v) if v not in (None, "", 0) else None
        out[buch] = werte
    return out


def wahrscheinlichkeiten(prob):
    """Odd-Alerts-Wahrscheinlichkeiten (Prozent) für die Systemmärkte plus Remis."""
    if not prob:
        return None
    out = {}
    for name, info in list(MAERKTE.items()) + [("remis", REMIS)]:
        v = prob.get(info["prob"])
        out[name] = float(v) if v is not None else None
    return out


def regulaere_tore(fx):
    """Tore nach regulärer Spielzeit inkl. Nachspielzeit (Abschnitt 1).

    Rückgabe (heim, gast, herkunft) oder None, wenn nicht sicher bestimmbar.
    """
    st = fx.get("status")
    h, a = fx.get("home_goals"), fx.get("away_goals")
    if st == "FT" and h is not None and a is not None:
        return int(h), int(a), "Endstand (FT)"
    if st in ("AET", "FT_PEN"):
        goals = (fx.get("timings") or {}).get("goals")
        if goals is None or h is None or a is None:
            return None
        if len(goals) != int(h) + int(a):
            return None
        teams = {fx.get("home_id"), fx.get("away_id")}
        if any(g.get("team_id") not in teams for g in goals):
            return None
        rh = sum(1 for g in goals if g["minute"] <= 90 and g["team_id"] == fx["home_id"])
        ra = sum(1 for g in goals if g["minute"] <= 90 and g["team_id"] == fx["away_id"])
        return rh, ra, f"aus Torminuten berechnet ({st}) – bitte prüfen"
    return None


def gewonnen(markt, h, a):
    if markt == "heim":
        return h > a
    if markt == "auswaerts":
        return a > h
    if markt == "btts":
        return h > 0 and a > 0
    if markt == "over25":
        return h + a >= 3
    if markt == "under25":
        return h + a <= 2
    raise ValueError(markt)
