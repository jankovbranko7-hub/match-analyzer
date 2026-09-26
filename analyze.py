#!/usr/bin/env python3
"""Match Analyzer – feste Rechenmethode für ein Spiel.

Nutzung:
    python3 analyze.py "Heimteam" "Auswärtsteam" 26.09.2026
    python3 analyze.py "Heimteam" "Auswärtsteam" 2026-09-26 --json

Holt alle Daten frisch aus der FootyStats-API (Key aus FOOTYSTATS_API_KEY),
berechnet erwartete Tore, Ergebnis-Matrix (Poisson mit Dixon-Coles-Korrektur),
die Wahrscheinlichkeiten der erlaubten Wetten und den besten Tipp nach
Datenklarheit. Jeder Aufruf rechnet genau ein Spiel – nichts wird zwischen
Spielen geteilt außer dem API-Cache (gleiche Anfrage innerhalb von 30 Minuten).
"""
import datetime as dt
import hashlib
import json
import math
import os
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.football-data-api.com"
CACHE_DIR = os.path.join(os.environ.get("TMPDIR", "/tmp"), "match-analyzer-cache")
CACHE_TTL = 30 * 60
TIMEZONE = "Europe/Berlin"

# ---------------------------------------------------------------- Gewichte
# Erwartete Tore: Anteile der Kennzahlen am Angriffs- bzw. Abwehrwert
ATT_WEIGHTS = {"xg": 0.60, "goals": 0.25, "sot": 0.15}
DEF_WEIGHTS = {"xg": 0.65, "goals": 0.35}
VENUE_SHRINK = 6        # Heim/Auswärts-Wert zählt n/(n+6), Rest Gesamtsaison
FORM_WEIGHT = 0.20      # Anteil Form der letzten 10 Spiele
DC_RHO = -0.08          # Dixon-Coles-Korrektur für 0:0, 1:0, 0:1, 1:1
MARKET_WEIGHT = 0.20    # Anteil margenbereinigter Vorab-Quoten
MIN_TIP_PROB = 0.40     # bester Tipp braucht mindestens 40 % Wahrscheinlichkeit


# ---------------------------------------------------------------- API
def api(endpoint, **params):
    key = os.environ.get("FOOTYSTATS_API_KEY")
    if not key:
        sys.exit("FOOTYSTATS_API_KEY fehlt – in den Umgebungseinstellungen hinterlegen "
                 "(Titelleiste → Cloud-Umgebung → Edit) und eine neue Session starten.")
    os.makedirs(CACHE_DIR, exist_ok=True)
    tag = hashlib.sha1(json.dumps([endpoint, params], sort_keys=True).encode()).hexdigest()
    path = os.path.join(CACHE_DIR, tag + ".json")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < CACHE_TTL:
        with open(path) as f:
            return json.load(f)
    url = f"{BASE}/{endpoint}?" + urllib.parse.urlencode({**params, "key": key})
    last = None
    for wait in (0, 2, 4, 8):
        time.sleep(wait)
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = json.load(r)
            break
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            last = str(e).replace(key, "***")
    else:
        sys.exit(f"API-Fehler bei {endpoint}: {last}")
    if not data.get("success", True) and not data.get("data"):
        sys.exit(f"API meldet Fehler bei {endpoint}: {data.get('message')}")
    with open(path, "w") as f:
        json.dump(data, f)
    return data


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    for junk in ("club ", "cf ", "fc ", "cd ", "ca ", "sc "):
        s = s.replace(junk, "")
    return " ".join(s.replace("-", " ").replace(".", " ").split())


def name_hit(query, match_name):
    q, m = norm(query), norm(match_name)
    return q == m or q in m or m in q


def find_match(home, away, date):
    days = [date, date + dt.timedelta(days=1), date - dt.timedelta(days=1)]
    for day in days:
        page, max_page = 1, 1
        while page <= max_page:
            res = api("todays-matches", date=day.isoformat(), timezone=TIMEZONE, page=page)
            max_page = (res.get("pager") or {}).get("max_page", 1)
            for m in res.get("data", []):
                if name_hit(home, m["home_name"]) and name_hit(away, m["away_name"]):
                    return m, False
                if name_hit(home, m["away_name"]) and name_hit(away, m["home_name"]):
                    return m, True
            page += 1
    sys.exit(f"Spiel {home} – {away} um den {date:%d.%m.%Y} nicht gefunden.")


# ---------------------------------------------------------------- Helfer
def num(v):
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    return v


def ratio(a, b):
    return a / b if a is not None and b else None


def blend(parts):
    """Gewichtetes Mittel, fehlende Teile werden herausgerechnet."""
    parts = [(w, v) for w, v in parts if v is not None]
    tw = sum(w for w, _ in parts)
    return sum(w * v for w, v in parts) / tw if tw else 1.0


def rating(venue, venue_lg, overall, overall_lg, form, n_venue):
    wv = n_venue / (n_venue + VENUE_SHRINK) if n_venue else 0
    base = blend([(wv, ratio(venue, venue_lg)), (1 - wv, ratio(overall, overall_lg))])
    f = ratio(form, overall_lg)
    return base if f is None else (1 - FORM_WEIGHT) * base + FORM_WEIGHT * f


def league_avg(teams, key_home, key_away):
    nh = na = h = a = 0.0
    for s in teams:
        mh, ma = s.get("seasonMatchesPlayed_home") or 0, s.get("seasonMatchesPlayed_away") or 0
        vh, va = num(s.get(key_home)), num(s.get(key_away))
        if vh is not None:
            h += vh * mh; nh += mh
        if va is not None:
            a += va * ma; na += ma
    lh, la = (h / nh if nh else None), (a / na if na else None)
    lh, la = (lh or None), (la or None)   # 0 = Liga ohne diese Daten
    lo = (lh + la) / 2 if lh and la else None
    return lh, la, lo


def dc_matrix(lam, mu, rho=DC_RHO, n=11):
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            p = (math.exp(-lam) * lam ** i / math.factorial(i)
                 * math.exp(-mu) * mu ** j / math.factorial(j))
            if i == 0 and j == 0:
                p *= 1 - lam * mu * rho
            elif i == 0 and j == 1:
                p *= 1 + lam * rho
            elif i == 1 and j == 0:
                p *= 1 + mu * rho
            elif i == 1 and j == 1:
                p *= 1 - rho
            P[i][j] = p
    s = sum(map(sum, P))
    return [[p / s for p in row] for row in P]


def market(match):
    """Margenbereinigte Wahrscheinlichkeiten aus den FootyStats-Quoten (Mittel über Buchmacher)."""
    oc = match.get("odds_comparison") or {}

    def avg_odds(market_name, sel, fallback):
        books = (oc.get(market_name) or {}).get(sel) or {}
        vals = [num(v) for v in books.values() if num(v) and num(v) > 1]
        if vals:
            return sum(vals) / len(vals)
        v = num(match.get(fallback))
        return v if v and v > 1 else None

    def devig(odds):
        if any(o is None for o in odds):
            return None
        inv = [1 / o for o in odds]
        return [x / sum(inv) for x in inv]

    return {
        "1x2": devig([avg_odds("FT Result", "Home", "odds_ft_1"),
                      avg_odds("FT Result", "Draw", "odds_ft_x"),
                      avg_odds("FT Result", "Away", "odds_ft_2")]),
        "ou25": devig([avg_odds("Goals Over/Under", "Over 2.5", "odds_ft_over25"),
                       avg_odds("Goals Over/Under", "Under 2.5", "odds_ft_under25")]),
        "btts": devig([avg_odds("Both Teams To Score", "Yes", "odds_btts_yes"),
                       avg_odds("Both Teams To Score", "No", "odds_btts_no")]),
        "best_odds": {
            "Sieg Heim": max_odds(oc, "FT Result", "Home", match.get("odds_ft_1")),
            "Sieg Auswärts": max_odds(oc, "FT Result", "Away", match.get("odds_ft_2")),
            "Über 2,5": max_odds(oc, "Goals Over/Under", "Over 2.5", match.get("odds_ft_over25")),
            "Unter 2,5": max_odds(oc, "Goals Over/Under", "Under 2.5", match.get("odds_ft_under25")),
            "Beide treffen – Ja": max_odds(oc, "Both Teams To Score", "Yes", match.get("odds_btts_yes")),
        },
    }


def max_odds(oc, market_name, sel, fallback):
    books = (oc.get(market_name) or {}).get(sel) or {}
    vals = [(num(v), b) for b, v in books.items() if num(v)]
    if vals:
        return max(vals)
    v = num(fallback)
    return (v, "FootyStats") if v and v > 1 else None


# ---------------------------------------------------------------- Datenklarheit
def side(h, a, higher_better=True):
    """1 = spricht fürs Heimteam, 0 = fürs Auswärtsteam, 0.5 = gleich, None = fehlt."""
    if h is None or a is None:
        return None
    if h == a:
        return 0.5
    return 1.0 if (h > a) == higher_better else 0.0


def over(v, thr):
    """1 = spricht für die Wette, 0 = dagegen, 0.5 = genau auf der Schwelle."""
    if v is None:
        return None
    return 0.5 if v == thr else float(v > thr)


def clarity(indicators):
    vals = [v for _, v in indicators if v is not None]
    return sum(vals) / len(vals) if vals else 0.5


# ---------------------------------------------------------------- Analyse
def analyze(home_q, away_q, date):
    m0, swapped = find_match(home_q, away_q, date)
    match = api("match", match_id=m0["id"])["data"]
    if isinstance(match, list):
        match = match[0]
    season_id = match.get("competition_id") or m0.get("competition_id")
    teams_raw = api("league-teams", season_id=season_id, include="stats")["data"]
    T = {t["id"]: t for t in teams_raw}
    hid, aid = match["homeID"], match["awayID"]
    H, A = T[hid]["stats"], T[aid]["stats"]
    teams = [t["stats"] for t in teams_raw]

    def lastx(tid):
        out = {}
        for x in api("lastx", team_id=tid).get("data", []):
            out.setdefault(x["last_x_match_num"], x["stats"])
        return out
    FH, FA = lastx(hid), lastx(aid)
    fh10, fa10 = FH.get(10, {}), FA.get(10, {})
    fh5, fa5 = FH.get(5, {}), FA.get(5, {})

    g = lambda s, k: num(s.get(k))
    LG = league_avg(teams, "seasonScoredAVG_home", "seasonScoredAVG_away")
    LX = league_avg(teams, "xg_for_avg_home", "xg_for_avg_away")
    LS = league_avg(teams, "shotsOnTargetAVG_home", "shotsOnTargetAVG_away")
    nh = H.get("seasonMatchesPlayed_home") or 0
    na = A.get("seasonMatchesPlayed_away") or 0

    # Angriff Heim (zu Hause) gegen Abwehr Auswärts (auswärts) und umgekehrt
    att_h = blend([
        (ATT_WEIGHTS["xg"], rating(g(H, "xg_for_avg_home"), LX[0], g(H, "xg_for_avg_overall"), LX[2], g(fh10, "xg_for_avg_overall"), nh) if LX[2] else None),
        (ATT_WEIGHTS["goals"], rating(g(H, "seasonScoredAVG_home"), LG[0], g(H, "seasonScoredAVG_overall"), LG[2], g(fh10, "seasonScoredAVG_overall"), nh)),
        (ATT_WEIGHTS["sot"], rating(g(H, "shotsOnTargetAVG_home"), LS[0], g(H, "shotsOnTargetAVG_overall"), LS[2], None, nh) if LS[2] else None),
    ])
    def_a = blend([
        (DEF_WEIGHTS["xg"], rating(g(A, "xg_against_avg_away"), LX[0], g(A, "xg_against_avg_overall"), LX[2], g(fa10, "xg_against_avg_overall"), na) if LX[2] else None),
        (DEF_WEIGHTS["goals"], rating(g(A, "seasonConcededAVG_away"), LG[0], g(A, "seasonConcededAVG_overall"), LG[2], g(fa10, "seasonConcededAVG_overall"), na)),
    ])
    att_a = blend([
        (ATT_WEIGHTS["xg"], rating(g(A, "xg_for_avg_away"), LX[1], g(A, "xg_for_avg_overall"), LX[2], g(fa10, "xg_for_avg_overall"), na) if LX[2] else None),
        (ATT_WEIGHTS["goals"], rating(g(A, "seasonScoredAVG_away"), LG[1], g(A, "seasonScoredAVG_overall"), LG[2], g(fa10, "seasonScoredAVG_overall"), na)),
        (ATT_WEIGHTS["sot"], rating(g(A, "shotsOnTargetAVG_away"), LS[1], g(A, "shotsOnTargetAVG_overall"), LS[2], None, na) if LS[2] else None),
    ])
    def_h = blend([
        (DEF_WEIGHTS["xg"], rating(g(H, "xg_against_avg_home"), LX[1], g(H, "xg_against_avg_overall"), LX[2], g(fh10, "xg_against_avg_overall"), nh) if LX[2] else None),
        (DEF_WEIGHTS["goals"], rating(g(H, "seasonConcededAVG_home"), LG[1], g(H, "seasonConcededAVG_overall"), LG[2], g(fh10, "seasonConcededAVG_overall"), nh)),
    ])
    base_h = blend([(0.5, LG[0]), (0.5, LX[0])]) if LG[0] else 1.45
    base_a = blend([(0.5, LG[1]), (0.5, LX[1])]) if LG[1] else 1.15
    lam, mu = base_h * att_h * def_a, base_a * att_a * def_h

    P = dc_matrix(lam, mu)
    n = len(P)
    cells = [(i, j, P[i][j]) for i in range(n) for j in range(n)]
    model = {
        "home": sum(p for i, j, p in cells if i > j),
        "draw": sum(p for i, j, p in cells if i == j),
        "away": sum(p for i, j, p in cells if i < j),
        "over25": sum(p for i, j, p in cells if i + j > 2),
        "btts": sum(p for i, j, p in cells if i > 0 and j > 0),
    }
    mk = market(match)
    w = MARKET_WEIGHT
    mix = lambda mod, mkt: mod if mkt is None else (1 - w) * mod + w * mkt
    final = {
        "home": mix(model["home"], mk["1x2"] and mk["1x2"][0]),
        "draw": mix(model["draw"], mk["1x2"] and mk["1x2"][1]),
        "away": mix(model["away"], mk["1x2"] and mk["1x2"][2]),
        "over25": mix(model["over25"], mk["ou25"] and mk["ou25"][0]),
        "btts": mix(model["btts"], mk["btts"] and mk["btts"][0]),
    }
    final["under25"] = 1 - final["over25"]
    top = sorted(cells, key=lambda c: -c[2])[:3]

    # ---- Datenklarheit: Anteil der Kennzahlen, die für die Wette sprechen
    win_ind = [
        ("Punkte/Spiel gesamt", side(g(H, "seasonPPG_overall"), g(A, "seasonPPG_overall"))),
        ("Punkte/Spiel Heim bzw. Auswärts", side(g(H, "seasonPPG_home"), g(A, "seasonPPG_away")) if nh and na else None),
        ("Form letzte 5 (Punkte/Spiel)", side(g(fh5, "seasonPPG_overall"), g(fa5, "seasonPPG_overall"))),
        ("Form letzte 10 (Punkte/Spiel)", side(g(fh10, "seasonPPG_overall"), g(fa10, "seasonPPG_overall"))),
        ("xG gesamt", side(g(H, "xg_for_avg_overall"), g(A, "xg_for_avg_overall")) if LX[2] else None),
        ("xG gegen gesamt", side(g(H, "xg_against_avg_overall"), g(A, "xg_against_avg_overall"), False) if LX[2] else None),
        ("xG Heim bzw. Auswärts", side(g(H, "xg_for_avg_home"), g(A, "xg_for_avg_away")) if LX[2] and nh and na else None),
        ("xG gegen Heim bzw. Auswärts", side(g(H, "xg_against_avg_home"), g(A, "xg_against_avg_away"), False) if LX[2] and nh and na else None),
        ("Tordifferenz/Spiel", side((g(H, "seasonScoredAVG_overall") or 0) - (g(H, "seasonConcededAVG_overall") or 0),
                                    (g(A, "seasonScoredAVG_overall") or 0) - (g(A, "seasonConcededAVG_overall") or 0))),
        ("Schüsse aufs Tor", side(g(H, "shotsOnTargetAVG_overall"), g(A, "shotsOnTargetAVG_overall")) if LS[2] else None),
        ("Ballbesitz", side(g(H, "possessionAVG_overall") or None, g(A, "possessionAVG_overall") or None)),
        ("Dangerous Attacks", side(g(H, "dangerous_attacks_avg_overall") or None, g(A, "dangerous_attacks_avg_overall") or None)),
        ("Tabellenplatz", side(g(H, "leaguePosition_overall") or None, g(A, "leaguePosition_overall") or None, False)),
        ("Erwartete Tore (Modell)", side(lam, mu)),
    ]
    home_clar = clarity(win_ind)

    exp_total_thr = 2.67  # ab hier liegt Über 2,5 bei Poisson über 50 %
    ou_ind = [
        ("Heim Über-2,5-Quote gesamt", over(g(H, "seasonOver25Percentage_overall"), 50)),
        ("Heim Über-2,5-Quote zu Hause", over(g(H, "seasonOver25Percentage_home"), 50) if nh else None),
        ("Auswärts Über-2,5-Quote gesamt", over(g(A, "seasonOver25Percentage_overall"), 50)),
        ("Auswärts Über-2,5-Quote auswärts", over(g(A, "seasonOver25Percentage_away"), 50) if na else None),
        ("Heim Über 2,5 letzte 10", over(g(fh10, "seasonOver25Percentage_overall"), 50)),
        ("Auswärts Über 2,5 letzte 10", over(g(fa10, "seasonOver25Percentage_overall"), 50)),
        ("Tore/Spiel Heimteam zu Hause", over(g(H, "seasonAVG_home"), 2.5) if nh else None),
        ("Tore/Spiel Auswärtsteam auswärts", over(g(A, "seasonAVG_away"), 2.5) if na else None),
        ("FootyStats Vorab-xG gesamt", over(g(match, "total_xg_prematch") or None, exp_total_thr)),
        ("Modell Über 2,5", over(model["over25"], 0.5)),
    ]
    over_clar = clarity(ou_ind)

    def pct(s, k):
        v = g(s, k)
        return None if v is None else v / 100
    def scores(fts, cs_opp):
        vals = [x for x in ((1 - fts) if fts is not None else None,
                            (1 - cs_opp) if cs_opp is not None else None) if x is not None]
        return sum(vals) / len(vals) if vals else None
    sh_v = scores(pct(H, "seasonFTSPercentage_home"), pct(A, "seasonCSPercentage_away")) if nh and na else None
    sa_v = scores(pct(A, "seasonFTSPercentage_away"), pct(H, "seasonCSPercentage_home")) if nh and na else None
    sh_o = scores(pct(H, "seasonFTSPercentage_overall"), pct(A, "seasonCSPercentage_overall"))
    sa_o = scores(pct(A, "seasonFTSPercentage_overall"), pct(H, "seasonCSPercentage_overall"))
    btts_ind = [
        ("Heim BTTS-Quote gesamt", over(g(H, "seasonBTTSPercentage_overall"), 50)),
        ("Heim BTTS-Quote zu Hause", over(g(H, "seasonBTTSPercentage_home"), 50) if nh else None),
        ("Auswärts BTTS-Quote gesamt", over(g(A, "seasonBTTSPercentage_overall"), 50)),
        ("Auswärts BTTS-Quote auswärts", over(g(A, "seasonBTTSPercentage_away"), 50) if na else None),
        ("Heim BTTS letzte 10", over(g(fh10, "seasonBTTSPercentage_overall"), 50)),
        ("Auswärts BTTS letzte 10", over(g(fa10, "seasonBTTSPercentage_overall"), 50)),
        ("Beide treffen laut Zu-Null/ohne-Tor (Heim/Auswärts)", over(sh_v * sa_v, 0.5) if sh_v is not None and sa_v is not None else None),
        ("Beide treffen laut Zu-Null/ohne-Tor (gesamt)", over(sh_o * sa_o, 0.5) if sh_o is not None and sa_o is not None else None),
        ("FootyStats BTTS-Potenzial", over(g(match, "btts_potential") or None, 50)),
        ("Modell Beide treffen", over(model["btts"], 0.5)),
    ]
    btts_clar = clarity(btts_ind)

    bets = {
        "Sieg Heim": (final["home"], home_clar),
        "Sieg Auswärts": (final["away"], 1 - home_clar),
        "Über 2,5": (final["over25"], over_clar),
        "Unter 2,5": (final["under25"], 1 - over_clar),
        "Beide treffen – Ja": (final["btts"], btts_clar),
    }
    eligible = {k: v for k, v in bets.items() if v[0] >= MIN_TIP_PROB}
    best = max(eligible, key=lambda k: (round(eligible[k][1], 3), eligible[k][0]))

    warnings = []
    for label, st in ((match["home_name"], H), (match["away_name"], A)):
        mp = st.get("seasonMatchesPlayed_overall") or 0
        if mp < 5:
            warnings.append(f"{label} hat erst {mp} Saisonspiele in diesem Wettbewerb – Zahlen unsicher.")
    if not LX[2]:
        warnings.append("Liga ohne xG-Daten – erwartete Tore nur aus Toren/Schüssen.")
    if mk["1x2"] and max(abs(model[k] - mk["1x2"][i]) for i, k in enumerate(("home", "draw", "away"))) > 0.20:
        warnings.append("Modell und Buchmacher liegen beim Spielausgang über 20 Punkte auseinander – "
                        "Datenlage prüfen (z. B. Pokal, Reserveteam, Saisonstart) und das offen sagen.")

    return {
        "warnings": warnings,
        "match": {"id": match["id"], "home": match["home_name"], "away": match["away_name"],
                  "kickoff_utc": dt.datetime.fromtimestamp(match["date_unix"], dt.timezone.utc).strftime("%Y-%m-%d %H:%M"),
                  "season_id": season_id, "game_week": match.get("game_week"),
                  "stadium": match.get("stadium_name"), "swapped_input": swapped},
        "league_avg": {"goals_home": LG[0], "goals_away": LG[1], "xg_home": LX[0], "xg_away": LX[1]},
        "ratings": {"att_home": att_h, "def_away": def_a, "att_away": att_a, "def_home": def_h},
        "expected_goals": {"home": lam, "away": mu,
                           "footystats_prematch_xg": [match.get("team_a_xg_prematch"), match.get("team_b_xg_prematch")]},
        "model": model, "market": {k: mk[k] for k in ("1x2", "ou25", "btts")}, "final": final,
        "top_scores": [(f"{i}:{j}", p) for i, j, p in top],
        "bets": {k: {"prob": p, "fair_odds": 1 / p, "clarity": c, "best_odds": mk["best_odds"].get(k)}
                 for k, (p, c) in bets.items()},
        "best_tip": best,
        "indicators": {"sieg_heim": win_ind, "ueber_2_5": ou_ind, "beide_treffen": btts_ind},
        "team_stats": {"home": team_summary(H, fh5, fh10, "home"), "away": team_summary(A, fa5, fa10, "away")},
        "h2h": (match.get("h2h") or {}).get("previous_matches_results"),
        "h2h_matches": (match.get("h2h") or {}).get("previous_matches_ids"),
        "trends": match.get("trends"),
    }


def team_summary(s, f5, f10, venue):
    keys = ["leaguePosition_overall", "seasonMatchesPlayed_overall", f"seasonMatchesPlayed_{venue}",
            "seasonWinsNum_overall", "seasonDrawsNum_overall", "seasonLossesNum_overall",
            f"seasonWinsNum_{venue}", f"seasonDrawsNum_{venue}", f"seasonLossesNum_{venue}",
            "seasonPPG_overall", f"seasonPPG_{venue}",
            "seasonScoredAVG_overall", "seasonConcededAVG_overall",
            f"seasonScoredAVG_{venue}", f"seasonConcededAVG_{venue}",
            "xg_for_avg_overall", "xg_against_avg_overall", f"xg_for_avg_{venue}", f"xg_against_avg_{venue}",
            "shotsAVG_overall", "shotsOnTargetAVG_overall", "possessionAVG_overall", "dangerous_attacks_avg_overall",
            "seasonOver25Percentage_overall", f"seasonOver25Percentage_{venue}",
            "seasonBTTSPercentage_overall", f"seasonBTTSPercentage_{venue}",
            "seasonCSPercentage_overall", f"seasonCSPercentage_{venue}",
            "seasonFTSPercentage_overall", f"seasonFTSPercentage_{venue}"]
    out = {k: s.get(k) for k in keys}
    for tag, f in (("last5", f5), ("last10", f10)):
        out[tag] = {k: f.get(k) for k in ("seasonPPG_overall", "seasonWinsNum_overall", "seasonDrawsNum_overall",
                                           "seasonLossesNum_overall", "seasonScoredNum_overall",
                                           "seasonConcededNum_overall", "xg_for_avg_overall", "xg_against_avg_overall")}
    out["goals_scored_min_0_to_15_75_to_90"] = [s.get("goals_scored_min_0_to_15"), s.get("goals_scored_min_76_to_90")]
    return out


# ---------------------------------------------------------------- Ausgabe
def de(x, d=1):
    return f"{x:.{d}f}".replace(".", ",")


def report(r):
    m = r["match"]
    out = [f"=== {m['home']} – {m['away']} | Anstoß {m['kickoff_utc']} UTC | Spieltag {m['game_week']} | Match-ID {m['id']} ==="]
    if m["swapped_input"]:
        out.append("ACHTUNG: Heim/Auswärts in der Anfrage waren vertauscht – maßgeblich ist die API.")
    out += [f"WARNUNG: {w}" for w in r["warnings"]]
    eg = r["expected_goals"]
    out.append(f"Erwartete Tore: {m['home']} {de(eg['home'], 2)} – {m['away']} {de(eg['away'], 2)}"
               f" (FootyStats Vorab-xG {eg['footystats_prematch_xg'][0]} / {eg['footystats_prematch_xg'][1]})")
    f = r["final"]
    out.append(f"Spielausgang: Heim {de(f['home']*100)} % | Unentschieden {de(f['draw']*100)} % | Auswärts {de(f['away']*100)} %")
    out.append("Top 3 Ergebnisse: " + ", ".join(f"{s} ({de(p*100)} %)" for s, p in r["top_scores"]))
    mk = r["market"]
    out.append(f"Nur Modell: H {de(r['model']['home']*100)} / X {de(r['model']['draw']*100)} / A {de(r['model']['away']*100)} | "
               f"Markt: " + ("/".join(de(x*100) for x in mk["1x2"]) if mk["1x2"] else "keine Quoten")
               + f" | Marktanteil {int(MARKET_WEIGHT*100)} %")
    out.append("")
    out.append(f"{'Wette':22s} {'Wahrsch.':>9s} {'faire Quote':>12s} {'Datenklarheit':>14s}  beste Quote")
    for k, b in r["bets"].items():
        bo = f"{b['best_odds'][0]:.2f} ({b['best_odds'][1]})" if b["best_odds"] else "–"
        out.append(f"{k:22s} {de(b['prob']*100):>7s} % {b['fair_odds']:>12.2f} {de(b['clarity']*100, 0):>12s} %  {bo}")
    best = r["bets"][r["best_tip"]]
    out.append(f"\nBESTER TIPP: {r['best_tip']} – {de(best['prob']*100)} %, faire Mindestquote {best['fair_odds']:.2f}, "
               f"Datenklarheit {de(best['clarity']*100, 0)} %")
    if best["best_odds"] and best["best_odds"][0] >= best["fair_odds"] * 1.05:
        out.append(f"Value: {best['best_odds'][1]} {best['best_odds'][0]:.2f} liegt über der fairen Quote.")
    for name, ind in r["indicators"].items():
        out.append(f"\nKennzahlen {name} (1 = dafür bzw. pro Heim, 0 = dagegen bzw. pro Auswärts):")
        out.append("  " + "; ".join(f"{n}: {'–' if v is None else de(v, 1)}" for n, v in ind))
    for side_name, t in (("Heim", r["team_stats"]["home"]), ("Auswärts", r["team_stats"]["away"])):
        out.append(f"\nTeamdaten {side_name}: " + json.dumps(t, ensure_ascii=False))
    out.append("\nDirekte Duelle: " + json.dumps(r["h2h"], ensure_ascii=False))
    if r["h2h_matches"]:
        years = sorted({dt.datetime.fromtimestamp(x["date_unix"], dt.timezone.utc).year for x in r["h2h_matches"]})
        out.append(f"  Jahre: {years}")
    out.append("Trends: " + json.dumps(r["trends"], ensure_ascii=False))
    return "\n".join(out)


def parse_date(s):
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    sys.exit(f"Datum nicht erkannt: {s} (erwartet TT.MM.JJJJ oder JJJJ-MM-TT)")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 3:
        sys.exit(__doc__)
    result = analyze(args[0], args[1], parse_date(args[2]))
    print(json.dumps(result, ensure_ascii=False, indent=1) if "--json" in sys.argv else report(result))
