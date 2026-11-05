"""Gemeinsames Modell über alle Wettbewerbe (OAP-M2) für Pokal- und Europapokalspiele.

Ein Poisson-Stärkemodell für ALLE Teams im Datenspeicher (.cache/oap/): Ligaspiele,
nationale Pokale und Europapokale zusammen. Spiele zwischen Teams verschiedener Ligen
(Pokale, Europapokal) verbinden die Ligen zu einer gemeinsamen Skala.

  log(λ_Heim) = μ + Heimvorteil + Angriff_Heim − Abwehr_Gast
  log(λ_Gast) = μ + Angriff_Gast − Abwehr_Heim

Gleiche Einstellungen wie OAP-M1 (Zielgröße xG, Halbwertszeit 120 Tage, α = 2,
mindestens 6 Spiele je Team); Schätzung blockweise mit Newton-Schritten
(Angriff, Abwehr, μ, Heimvorteil), da sehr viele Teams.
Nur abgeschlossene Spiele (FT) vor dem Stichtag, keine Freundschaftsspiele.
"""

import glob
import json
import math
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache", "oap")
FENSTER_TAGE = 730


def alle_spiele():
    """Alle Spiele aller Wettbewerbe im Speicher (dedupliziert), mit Wettbewerbs-ID."""
    spiele = {}
    for p in glob.glob(os.path.join(CACHE, "comp_*.json")):
        try:
            with open(p) as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            continue
        cid = d.get("wettbewerb_id")
        for s in d.get("spiele", []):
            spiele[s["id"]] = {**s, "c": cid}
    return list(spiele.values())


def team_wettbewerbe(spiele):
    idx = {}
    for s in spiele:
        idx.setdefault(s["h"], set()).add(s["c"])
        idx.setdefault(s["a"], set()).add(s["c"])
    return idx


def fit(spiele, stichtag, w_xg=1.0, halbwertszeit=120.0, alpha=2.0, iterationen=300):
    d = [s for s in spiele if s["st"] == "FT" and not s["fr"] and s["u"] < stichtag
         and s["u"] > stichtag - FENSTER_TAGE * 86400 and s["hg"] is not None and s["ag"] is not None]
    if not d:
        return None
    teams = sorted({s["h"] for s in d} | {s["a"] for s in d})
    ix = {t: i for i, t in enumerate(teams)}
    T, n = len(teams), len(d)
    hi = np.fromiter((ix[s["h"]] for s in d), int, n)
    ai = np.fromiter((ix[s["a"]] for s in d), int, n)

    def ziel(s, tore, xg):
        return w_xg * float(s[xg]) + (1 - w_xg) * s[tore] if (s["hx"] is not None and s["ax"] is not None and w_xg > 0) else s[tore]

    yh = np.fromiter((ziel(s, "hg", "hx") for s in d), float, n)
    ya = np.fromiter((ziel(s, "ag", "ax") for s in d), float, n)
    w = np.fromiter((0.5 ** (((stichtag - s["u"]) / 86400.0) / halbwertszeit) for s in d), float, n)
    # Beobachtungen: Heimzeilen (Angriff hi, Abwehr ai, heim=1) und Gastzeilen (Angriff ai, Abwehr hi, heim=0)
    att_i = np.concatenate([hi, ai]); def_i = np.concatenate([ai, hi])
    heim = np.concatenate([np.ones(n), np.zeros(n)])
    y = np.concatenate([yh, ya]); ww = np.concatenate([w, w])
    att = np.zeros(T); dfn = np.zeros(T)
    mu = math.log(max(np.average(y, weights=ww), 0.05)); hv = 0.25

    def eta():
        return mu + hv * heim + att[att_i] - dfn[def_i]

    for it in range(iterationen):
        alt = (att.copy(), dfn.copy(), mu, hv)
        lam = np.exp(np.clip(eta(), -10, 10)); r = ww * (lam - y); h = ww * lam
        g = np.bincount(att_i, r, T) + 2 * alpha * att
        H = np.bincount(att_i, h, T) + 2 * alpha
        att -= np.clip(g / H, -1, 1)
        lam = np.exp(np.clip(eta(), -10, 10)); r = ww * (lam - y); h = ww * lam
        g = -np.bincount(def_i, r, T) + 2 * alpha * dfn
        H = np.bincount(def_i, h, T) + 2 * alpha
        dfn -= np.clip(g / H, -1, 1)
        lam = np.exp(np.clip(eta(), -10, 10))
        mu -= float(np.sum(ww * (lam - y)) / np.sum(ww * lam))
        lam = np.exp(np.clip(eta(), -10, 10))
        m = heim == 1
        hv -= float(np.sum((ww * (lam - y))[m]) / np.sum((ww * lam)[m]))
        diff = max(np.max(np.abs(att - alt[0])), np.max(np.abs(dfn - alt[1])), abs(mu - alt[2]), abs(hv - alt[3]))
        if diff < 1e-6:
            break
    if not (np.all(np.isfinite(att)) and np.all(np.isfinite(dfn)) and math.isfinite(mu) and math.isfinite(hv)):
        return None
    anzahl = np.bincount(hi, minlength=T) + np.bincount(ai, minlength=T)
    return {"ix": ix, "att": att, "dfn": dfn, "mu": mu, "hv": hv, "anzahl": anzahl, "n": n,
            "iterationen": it + 1, "konvergenz": float(diff)}


def lambdas(m, h, a, min_spiele=6):
    if m is None or h not in m["ix"] or a not in m["ix"]:
        return None
    i, j = m["ix"][h], m["ix"][a]
    if m["anzahl"][i] < min_spiele or m["anzahl"][j] < min_spiele:
        return None
    return (math.exp(m["mu"] + m["hv"] + m["att"][i] - m["dfn"][j]),
            math.exp(m["mu"] + m["att"][j] - m["dfn"][i]))
