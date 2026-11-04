"""Reguliertes unabhängiges Poisson-Modell nach System v1.3-OA, Abschnitt 5.

Modellversion: OA-Poisson-1 (Abschnitt 5.3 unverändert umgesetzt)
  log(lambda_H) = mu + Heimvorteil + Angriff_h - Abwehr_a
  log(lambda_A) = mu + Angriff_a - Abwehr_h
  Minimiert: negative Poisson-Log-Likelihood + alpha * Summe(Angriff^2 + Abwehr^2)
  (mu und Heimvorteil unbestraft; Summe der Parameter = 0 folgt aus der Strafe und wird
  zusätzlich zentriert). Alle Spiele gleiches Gewicht.

Trainingsdaten (5.2): ein Wettbewerb, laufende Saison + bis zu 3 vorherige Saisons,
nur Status FT (reguläre Spielzeit; Spiele mit Verlängerung/Elfmeterschießen nicht
beigemischt), nur vor dem Entscheidungszeitpunkt, keine Freundschaftsspiele.

Zeitliche Prüfung (5.3/5.5): chronologisch 60 % Training / 20 % Auswahl von alpha
(mittlerer negativer Log-Score der Torpaare, bei Gleichstand größeres alpha) /
20 % unberührter Test (Brier, Log-Loss, Gruppen je Markt; Vergleich mit Grundrate).
Danach Neuschätzung auf allen Spielen.

Aufruf: python3 werkzeuge/modell.py WETTBEWERB_ID --spiele MATCH_ID[,MATCH_ID...] [--ausgabe DIR]
"""

import argparse
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oa_api as oa  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "OA-Poisson-1"
ALPHAS = [0.1, 1.0, 10.0, 100.0]


def trainingsdaten(wettbewerb_id, vor_unix):
    """FT-Spiele der laufenden + bis zu 3 vorherigen Saisons, neueste zuerst geladen."""
    saisons, spiele, page, ausgeschlossen = [], [], 1, {}
    while True:
        d = oa.get("fixtures/competition/" + str(wettbewerb_id),
                   {"per_page": 250, "page": page, "order": "desc"})
        rows = d.get("data") or []
        fertig = False
        for f in rows:
            s = f.get("season_id")
            if s not in saisons:
                if len(saisons) == 4:
                    fertig = True
                    break
                saisons.append(s)
            if f["unix"] >= vor_unix:
                continue
            if f.get("is_friendly"):
                ausgeschlossen["Freundschaftsspiel"] = ausgeschlossen.get("Freundschaftsspiel", 0) + 1
                continue
            if f.get("status") != "FT" or f.get("home_goals") is None:
                st = f.get("status")
                ausgeschlossen[st] = ausgeschlossen.get(st, 0) + 1
                continue
            spiele.append({"id": f["id"], "unix": f["unix"], "saison_id": s,
                           "saison": f.get("season"), "h": f["home_id"], "a": f["away_id"],
                           "hn": f["home_name"], "an": f["away_name"],
                           "hg": int(f["home_goals"]), "ag": int(f["away_goals"])})
        if fertig or not rows or not (d.get("info") or {}).get("next_page_url"):
            break
        page += 1
    # Duplikate entfernen (3.2)
    eind, dup = {}, 0
    for s in spiele:
        if s["id"] in eind:
            dup += 1
        eind[s["id"]] = s
    spiele = sorted(eind.values(), key=lambda s: (s["unix"], s["id"]))
    return spiele, saisons, ausgeschlossen, dup


class Poisson:
    def __init__(self, alpha):
        self.alpha = alpha

    def fit(self, spiele):
        teams = sorted({s["h"] for s in spiele} | {s["a"] for s in spiele})
        self.idx = {t: i for i, t in enumerate(teams)}
        T = len(teams)
        n = len(spiele)
        P = 2 + 2 * T  # mu, heim, att[T], def[T]
        X = np.zeros((2 * n, P))
        y = np.zeros(2 * n)
        for k, s in enumerate(spiele):
            hi, ai = self.idx[s["h"]], self.idx[s["a"]]
            X[2 * k, 0] = 1; X[2 * k, 1] = 1; X[2 * k, 2 + hi] = 1; X[2 * k, 2 + T + ai] = -1
            X[2 * k + 1, 0] = 1; X[2 * k + 1, 2 + ai] = 1; X[2 * k + 1, 2 + T + hi] = -1
            y[2 * k], y[2 * k + 1] = s["hg"], s["ag"]
        pen = np.full(P, 2 * self.alpha)
        pen[:2] = 0
        beta = np.zeros(P)
        beta[0] = math.log(max(y.mean(), 1e-3))

        def ziel(b):
            eta = X @ b
            return float(np.sum(np.exp(eta) - y * eta) + self.alpha * np.sum(b[2:] ** 2))

        f_alt = ziel(beta)
        for _ in range(100):
            eta = np.clip(X @ beta, -20, 20)
            lam = np.exp(eta)
            grad = X.T @ (lam - y) + pen * beta
            H = X.T @ (X * lam[:, None]) + np.diag(pen) + 1e-9 * np.eye(P)
            schritt = np.linalg.solve(H, grad)
            t = 1.0
            while t > 1e-6:
                neu = beta - t * schritt
                f_neu = ziel(neu)
                if f_neu <= f_alt:
                    break
                t /= 2
            beta = neu
            if abs(f_alt - f_neu) < 1e-10 * max(1, abs(f_alt)):
                f_alt = f_neu
                break
            f_alt = f_neu
        att, dfn = beta[2:2 + T].copy(), beta[2 + T:].copy()
        mu = beta[0] + att.mean() - dfn.mean()
        att -= att.mean(); dfn -= dfn.mean()
        self.mu, self.heim, self.att, self.dfn = mu, beta[1], att, dfn
        self.n_team = {t: 0 for t in teams}
        for s in spiele:
            self.n_team[s["h"]] += 1; self.n_team[s["a"]] += 1
        if not np.all(np.isfinite(beta)):
            raise ValueError("nicht endliche Parameter")
        return self

    def lambdas(self, h, a, neutral=False):
        ah = self.att[self.idx[h]] if h in self.idx else 0.0
        dh = self.dfn[self.idx[h]] if h in self.idx else 0.0
        aa = self.att[self.idx[a]] if a in self.idx else 0.0
        da = self.dfn[self.idx[a]] if a in self.idx else 0.0
        lh = math.exp(self.mu + (0 if neutral else self.heim) + ah - da)
        la = math.exp(self.mu + aa - dh)
        return lh, la


def pois(k, lam):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def maerkte(lh, la):
    """Abschnitt 5.4; Summation bis Restmasse < 1e-6, keine Umnormierung."""
    G = 0
    while True:
        G += 1
        rh = 1 - sum(pois(i, lh) for i in range(G + 1))
        ra = 1 - sum(pois(i, la) for i in range(G + 1))
        if rh + ra < 1e-6 or G > 60:
            break
    ph = [pois(i, lh) for i in range(G + 1)]
    pa = [pois(i, la) for i in range(G + 1)]
    heim = sum(ph[i] * pa[j] for i in range(G + 1) for j in range(G + 1) if i > j)
    ausw = sum(ph[i] * pa[j] for i in range(G + 1) for j in range(G + 1) if i < j)
    remis = sum(ph[i] * pa[i] for i in range(G + 1))
    s = lh + la
    under = math.exp(-s) * (1 + s + s * s / 2)
    btts = (1 - math.exp(-lh)) * (1 - math.exp(-la))
    r = {"heim": heim, "remis": remis, "auswaerts": ausw, "btts": btts,
         "over25": 1 - under, "under25": under, "lambda_heim": lh, "lambda_gast": la,
         "restmasse_1x2": 1 - (heim + ausw + remis)}
    for k in ("heim", "remis", "auswaerts", "btts", "over25", "under25"):
        assert -1e-12 <= r[k] <= 1 + 1e-12
    return r


def logscore(m, spiele):
    tot = 0.0
    for s in spiele:
        lh, la = m.lambdas(s["h"], s["a"])
        tot += -math.log(max(pois(s["hg"], lh) * pois(s["ag"], la), 1e-300))
    return tot / len(spiele)


def ausgang(markt, s):
    return int(oa.gewonnen(markt, s["hg"], s["ag"]))


def pruefung(spiele):
    n = len(spiele)
    i1, i2 = int(n * 0.6), int(n * 0.8)
    train, val, test = spiele[:i1], spiele[i1:i2], spiele[i2:]
    kand = {}
    for a in ALPHAS:
        kand[a] = logscore(Poisson(a).fit(train), val)
    best = min(kand.values())
    alpha = max(a for a, v in kand.items() if abs(v - best) < 1e-9)
    m = Poisson(alpha).fit(spiele[:i2])
    erg = {}
    for markt in oa.MAERKTE:
        ps, ys = [], []
        for s in test:
            p = maerkte(*m.lambdas(s["h"], s["a"]))[markt]
            ps.append(p); ys.append(ausgang(markt, s))
        base = sum(ausgang(markt, s) for s in spiele[:i2]) / i2
        brier = sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ps)
        brier_b = sum((base - y) ** 2 for y in ys) / len(ys)
        ll = -sum(y * math.log(max(p, 1e-12)) + (1 - y) * math.log(max(1 - p, 1e-12)) for p, y in zip(ps, ys)) / len(ps)
        ll_b = -sum(y * math.log(base) + (1 - y) * math.log(1 - base) for y in ys) / len(ys)
        gruppen = []
        for lo in range(0, 100, 20):
            g = [(p, y) for p, y in zip(ps, ys) if lo / 100 <= p < (lo + 20) / 100 or (lo == 80 and p >= 1)]
            if g:
                gruppen.append({"bereich": f"{lo}-{lo + 20}", "n": len(g),
                                "prognose": round(sum(p for p, _ in g) / len(g) * 100, 1),
                                "beobachtet": round(sum(y for _, y in g) / len(g) * 100, 1)})
        erg[markt] = {"n": len(ys), "brier": round(brier, 4), "brier_grundrate": round(brier_b, 4),
                      "logloss": round(ll, 4), "logloss_grundrate": round(ll_b, 4),
                      "trefferanteil_test": round(sum(ys) / len(ys) * 100, 1),
                      "se_brier": round(np.std([(p - y) ** 2 for p, y in zip(ps, ys)]) / math.sqrt(len(ys)), 4),
                      "gruppen": gruppen}
    return {
        "aufteilung": {"training": [train[0]["unix"], train[-1]["unix"], len(train)],
                       "auswahl": [val[0]["unix"], val[-1]["unix"], len(val)],
                       "test": [test[0]["unix"], test[-1]["unix"], len(test)]},
        "alpha_kandidaten_logscore": {str(a): round(v, 4) for a, v in kand.items()},
        "alpha": alpha, "test_je_markt": erg}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("wettbewerb", type=int)
    ap.add_argument("--spiele", required=True)
    ap.add_argument("--ausgabe", default=os.path.join(ROOT, "protokoll", "daten"))
    a = ap.parse_args()
    jetzt = oa.jetzt_utc()
    spiele, saisons, ausgeschl, dup = trainingsdaten(a.wettbewerb, jetzt.timestamp())
    if len(spiele) < 100:
        sys.exit(f"Zu wenige Trainingsspiele ({len(spiele)}) – keine brauchbare zeitliche Prüfung.")
    pr = pruefung(spiele)
    m = Poisson(pr["alpha"]).fit(spiele)
    ziel = {}
    for mid in a.spiele.split(","):
        f = oa.get("fixtures/" + mid)["data"][0]
        h, g = f["home_id"], f["away_id"]
        eintrag = {"heim": f["home_name"], "gast": f["away_name"],
                   "spiele_im_training": {"heim": m.n_team.get(h, 0), "gast": m.n_team.get(g, 0)}}
        if h not in m.idx or g not in m.idx:
            eintrag["modell"] = "fehlt (Mannschaft ohne Trainingsspiele in diesem Wettbewerb)"
        else:
            r = maerkte(*m.lambdas(h, g))
            eintrag["modell"] = {k: round(v, 6) for k, v in r.items()}
            eintrag["parameter"] = {"angriff_heim": round(float(m.att[m.idx[h]]), 4),
                                    "abwehr_heim": round(float(m.dfn[m.idx[h]]), 4),
                                    "angriff_gast": round(float(m.att[m.idx[g]]), 4),
                                    "abwehr_gast": round(float(m.dfn[m.idx[g]]), 4)}
        ziel[mid] = eintrag
    out = {"modellversion": VERSION, "rechenlauf_utc": jetzt.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "trainingsstichtag_utc": oa.iso(spiele[-1]["unix"]),
           "wettbewerb_id": a.wettbewerb, "saison_ids": saisons,
           "saisons": sorted({s["saison"] for s in spiele}),
           "trainingsspiele": len(spiele), "teams": len(m.idx),
           "ausgeschlossen": ausgeschl, "duplikate_entfernt": dup,
           "erstes_spiel": oa.iso(spiele[0]["unix"]), "letztes_spiel": oa.iso(spiele[-1]["unix"]),
           "zeitliche_pruefung": pr, "alpha_final": pr["alpha"],
           "mu": round(float(m.mu), 4), "heimvorteil": round(float(m.heim), 4),
           "neutraler_platz": "Kennzeichnung in der API fehlt; alle Spiele mit Heimvorteil gerechnet",
           "vorhersagen": ziel}
    os.makedirs(a.ausgabe, exist_ok=True)
    p = os.path.join(a.ausgabe, f"modell_{a.wettbewerb}_{jetzt.strftime('%Y%m%dT%H%MZ')}.json")
    with open(p, "w", encoding="utf8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(json.dumps({k: out[k] for k in ("modellversion", "trainingsspiele", "teams", "saisons",
                                          "ausgeschlossen", "alpha_final", "heimvorteil")}, ensure_ascii=False))
    print(json.dumps(pr, ensure_ascii=False, indent=1))
    print(json.dumps(ziel, ensure_ascii=False, indent=1))
    print("gespeichert:", os.path.relpath(p, ROOT))


if __name__ == "__main__":
    main()
