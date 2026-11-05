"""Eigenes Modell für OAP-2.0: gewichtetes Poisson-Stärkemodell je Liga.

  log(lambda_heim) = mu + heimvorteil + angriff_h - abwehr_a
  log(lambda_gast) = mu + angriff_a - abwehr_h

Zielgröße je Team und Spiel: y = w * xG + (1 - w) * Tore (ohne xG: nur Tore).
Gewicht je Spiel: 0,5 ^ (Alter in Tagen / Halbwertszeit). Ridge-Strafe alpha auf
Angriff/Abwehr. Nur abgeschlossene Ligaspiele (Status FT) vor dem Stichtag, keine
Freundschaftsspiele. Märkte aus unabhängigen Poisson-Verteilungen.
"""

import math

import numpy as np

STANDARD = {"w_xg": 0.5, "halbwertszeit": 180.0, "alpha": 2.0, "min_spiele": 6}


def fit(spiele, stichtag, w_xg, halbwertszeit, alpha):
    daten = [s for s in spiele if s["st"] == "FT" and not s["fr"] and s["u"] < stichtag
             and s["hg"] is not None and s["ag"] is not None]
    if len(daten) < 30:
        return None
    teams = sorted({s["h"] for s in daten} | {s["a"] for s in daten})
    idx = {t: i for i, t in enumerate(teams)}
    T, n = len(teams), len(daten)
    P = 2 + 2 * T
    rows_i, cols, vals = [], [], []
    y = np.zeros(2 * n)
    wt = np.zeros(2 * n)
    X = np.zeros((2 * n, P))
    anzahl = np.zeros(T)
    for k, s in enumerate(daten):
        hi, ai = idx[s["h"]], idx[s["a"]]
        X[2 * k, [0, 1, 2 + hi, 2 + T + ai]] = [1, 1, 1, -1]
        X[2 * k + 1, [0, 2 + ai, 2 + T + hi]] = [1, 1, -1]
        if s["hx"] is not None and s["ax"] is not None and w_xg > 0:
            y[2 * k] = w_xg * float(s["hx"]) + (1 - w_xg) * s["hg"]
            y[2 * k + 1] = w_xg * float(s["ax"]) + (1 - w_xg) * s["ag"]
        else:
            y[2 * k], y[2 * k + 1] = s["hg"], s["ag"]
        g = 0.5 ** (((stichtag - s["u"]) / 86400.0) / halbwertszeit)
        wt[2 * k] = wt[2 * k + 1] = g
        anzahl[hi] += 1
        anzahl[ai] += 1
    pen = np.full(P, 2 * alpha)
    pen[:2] = 0
    beta = np.zeros(P)
    beta[0] = math.log(max(np.average(y, weights=wt), 0.05))

    def ziel(b):
        eta = X @ b
        return float(np.sum(wt * (np.exp(eta) - y * eta)) + alpha * np.sum(b[2:] ** 2))

    f_alt = ziel(beta)
    for _ in range(50):
        eta = np.clip(X @ beta, -10, 10)
        lam = np.exp(eta)
        grad = X.T @ (wt * (lam - y)) + pen * beta
        H = X.T @ (X * (wt * lam)[:, None]) + np.diag(pen) + 1e-8 * np.eye(P)
        schritt = np.linalg.solve(H, grad)
        t = 1.0
        while t > 1e-6:
            neu = beta - t * schritt
            f_neu = ziel(neu)
            if f_neu <= f_alt:
                break
            t /= 2
        beta = neu
        if abs(f_alt - f_neu) < 1e-9 * max(1.0, abs(f_alt)):
            break
        f_alt = f_neu
    if not np.all(np.isfinite(beta)):
        return None
    return {"idx": idx, "beta": beta, "T": T, "anzahl": anzahl, "n": n}


def lambdas(m, h, a, min_spiele):
    if m is None or h not in m["idx"] or a not in m["idx"]:
        return None
    hi, ai, T, b = m["idx"][h], m["idx"][a], m["T"], m["beta"]
    if m["anzahl"][hi] < min_spiele or m["anzahl"][ai] < min_spiele:
        return None
    lh = math.exp(b[0] + b[1] + b[2 + hi] - b[2 + T + ai])
    la = math.exp(b[0] + b[2 + ai] - b[2 + T + hi])
    return lh, la


def _pois(k, lam):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def maerkte(lh, la):
    G = 15
    while 1 - sum(_pois(i, lh) for i in range(G + 1)) + 1 - sum(_pois(i, la) for i in range(G + 1)) > 1e-7 and G < 40:
        G += 5
    ph = [_pois(i, lh) for i in range(G + 1)]
    pa = [_pois(i, la) for i in range(G + 1)]
    heim = sum(ph[i] * sum(pa[:i]) for i in range(G + 1))
    remis = sum(ph[i] * pa[i] for i in range(G + 1))
    ausw = sum(pa[j] * sum(ph[:j]) for j in range(G + 1))
    s = lh + la
    under = math.exp(-s) * (1 + s + s * s / 2)
    btts = (1 - math.exp(-lh)) * (1 - math.exp(-la))
    return {"heim": heim, "remis": remis, "auswaerts": ausw, "btts": btts, "btts_nein": 1 - btts,
            "over25": 1 - under, "under25": under, "lambda_heim": lh, "lambda_gast": la}
