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


# ---------------------------------------------------------------- OAP-M3: Liga-Ebene + Team-Abweichung
def wettbewerbstypen():
    try:
        with open(os.path.join(CACHE, "wettbewerbe.json")) as fh:
            return {int(k): v.get("typ") for k, v in json.load(fh).items()}
    except (OSError, ValueError):
        return {}


def liga_zuordnung(d, typen):
    """Jedes Team → Wettbewerb seines letzten Ligaspiels im Datenbestand (sonst Gruppe -1)."""
    letzte = {}
    for s in d:
        if typen.get(s["c"]) != "League":
            continue
        for t in (s["h"], s["a"]):
            if t not in letzte or s["u"] > letzte[t][0]:
                letzte[t] = (s["u"], s["c"])
    return {t: v[1] for t, v in letzte.items()}


def fit_h(spiele, stichtag, w_xg=1.0, halbwertszeit=120.0, alpha_team=5.0, alpha_liga=0.2,
          iterationen=600, typen=None, fenster_tage=400, toleranz=1e-5):
    """Stärke = Ligastärke + Teamabweichung; Ridge stark auf Team, schwach auf Liga."""
    typen = typen if typen is not None else wettbewerbstypen()
    d = [s for s in spiele if s["st"] == "FT" and not s["fr"] and s["u"] < stichtag
         and s["u"] > stichtag - fenster_tage * 86400 and s["hg"] is not None and s["ag"] is not None]
    if not d:
        return None
    teams = sorted({s["h"] for s in d} | {s["a"] for s in d})
    ix = {t: i for i, t in enumerate(teams)}
    zu = liga_zuordnung(d, typen)
    ligen = sorted(set(zu.values())) + [-1]
    lx = {l: i for i, l in enumerate(ligen)}
    team_liga = np.array([lx[zu.get(t, -1)] for t in teams])
    T, L, n = len(teams), len(ligen), len(d)
    hi = np.fromiter((ix[s["h"]] for s in d), int, n)
    ai = np.fromiter((ix[s["a"]] for s in d), int, n)

    def ziel(s, tore, xg):
        return w_xg * float(s[xg]) + (1 - w_xg) * s[tore] if (s["hx"] is not None and s["ax"] is not None and w_xg > 0) else s[tore]

    yh = np.fromiter((ziel(s, "hg", "hx") for s in d), float, n)
    ya = np.fromiter((ziel(s, "ag", "ax") for s in d), float, n)
    w = np.fromiter((0.5 ** (((stichtag - s["u"]) / 86400.0) / halbwertszeit) for s in d), float, n)
    att_i = np.concatenate([hi, ai]); def_i = np.concatenate([ai, hi])
    att_l, def_l = team_liga[att_i], team_liga[def_i]
    heim = np.concatenate([np.ones(n), np.zeros(n)])
    y = np.concatenate([yh, ya]); ww = np.concatenate([w, w])
    a = np.zeros(T); dd = np.zeros(T); La = np.zeros(L); Ld = np.zeros(L)
    mu = math.log(max(np.average(y, weights=ww), 0.05)); hv = 0.25

    def eta():
        return mu + hv * heim + La[att_l] + a[att_i] - Ld[def_l] - dd[def_i]

    def schritt(idx, groesse, vorz, par, alpha):
        lam = np.exp(np.clip(eta(), -10, 10))
        g = vorz * np.bincount(idx, ww * (lam - y), groesse) + 2 * alpha * par
        H = np.bincount(idx, ww * lam, groesse) + 2 * alpha + 1e-9
        return np.clip(g / H, -1, 1)

    diff = 1.0
    for it in range(iterationen):
        alt = np.concatenate([a, dd, La, Ld, [mu, hv]])
        La -= schritt(att_l, L, 1, La, alpha_liga)
        Ld -= schritt(def_l, L, -1, Ld, alpha_liga)
        a -= schritt(att_i, T, 1, a, alpha_team)
        dd -= schritt(def_i, T, -1, dd, alpha_team)
        # Beschleunigung: mittlere Teamabweichung je Liga in die Ligastärke verschieben
        ma = np.bincount(team_liga, a, L) / np.maximum(np.bincount(team_liga, minlength=L), 1)
        md = np.bincount(team_liga, dd, L) / np.maximum(np.bincount(team_liga, minlength=L), 1)
        La += ma; a -= ma[team_liga]; Ld += md; dd -= md[team_liga]
        lam = np.exp(np.clip(eta(), -10, 10))
        mu -= float(np.sum(ww * (lam - y)) / np.sum(ww * lam))
        lam = np.exp(np.clip(eta(), -10, 10)); m = heim == 1
        hv -= float(np.sum((ww * (lam - y))[m]) / np.sum((ww * lam)[m]))
        diff = float(np.max(np.abs(np.concatenate([a, dd, La, Ld, [mu, hv]]) - alt)))
        if diff < toleranz:
            break
    att = La[team_liga] + a
    dfn = Ld[team_liga] + dd
    if not (np.all(np.isfinite(att)) and np.all(np.isfinite(dfn))):
        return None
    anzahl = np.bincount(hi, minlength=T) + np.bincount(ai, minlength=T)
    return {"ix": ix, "att": att, "dfn": dfn, "mu": mu, "hv": hv, "anzahl": anzahl, "n": n,
            "iterationen": it + 1, "konvergenz": diff, "ligen": L,
            "liga_staerke": {ligen[i]: (float(La[i]), float(Ld[i])) for i in range(L)}}


def fit_h2(spiele, stichtag, w_xg=0.0, halbwertszeit=120.0, alpha_team=5.0, alpha_liga=0.2,
           typen=None, fenster_tage=400, newton_schritte=25, cg_schritte=150):
    """Wie fit_h, aber gemeinsames Newton-Verfahren mit konjugierten Gradienten (matrixfrei)."""
    typen = typen if typen is not None else wettbewerbstypen()
    d = [s for s in spiele if s["st"] == "FT" and not s["fr"] and s["u"] < stichtag
         and s["u"] > stichtag - fenster_tage * 86400 and s["hg"] is not None and s["ag"] is not None]
    if not d:
        return None
    teams = sorted({s["h"] for s in d} | {s["a"] for s in d})
    ix = {t: i for i, t in enumerate(teams)}
    zu = liga_zuordnung(d, typen)
    ligen = sorted(set(zu.values())) + [-1]
    lx = {l: i for i, l in enumerate(ligen)}
    team_liga = np.array([lx[zu.get(t, -1)] for t in teams])
    T, L, n = len(teams), len(ligen), len(d)
    hi = np.fromiter((ix[s["h"]] for s in d), int, n)
    ai = np.fromiter((ix[s["a"]] for s in d), int, n)

    def ziel(s, tore, xg):
        return w_xg * float(s[xg]) + (1 - w_xg) * s[tore] if (s["hx"] is not None and s["ax"] is not None and w_xg > 0) else s[tore]

    y = np.concatenate([np.fromiter((ziel(s, "hg", "hx") for s in d), float, n),
                        np.fromiter((ziel(s, "ag", "ax") for s in d), float, n)])
    w = np.fromiter((0.5 ** (((stichtag - s["u"]) / 86400.0) / halbwertszeit) for s in d), float, n)
    ww = np.concatenate([w, w])
    att_i = np.concatenate([hi, ai]); def_i = np.concatenate([ai, hi])
    att_l, def_l = team_liga[att_i], team_liga[def_i]
    heim = np.concatenate([np.ones(n), np.zeros(n)])
    o = [0, T, 2 * T, 2 * T + L, 2 * T + 2 * L, 2 * T + 2 * L + 1, 2 * T + 2 * L + 2]
    P = o[-1]
    pen = np.zeros(P)
    pen[o[0]:o[2]] = 2 * alpha_team
    pen[o[2]:o[4]] = 2 * alpha_liga
    pen += 1e-8

    def Xv(v):
        return (v[o[4]] + v[o[5]] * heim + v[o[2]:o[3]][att_l] + v[o[0]:o[1]][att_i]
                - v[o[3]:o[4]][def_l] - v[o[1]:o[2]][def_i])

    def XTu(u):
        return np.concatenate([np.bincount(att_i, u, T), -np.bincount(def_i, u, T),
                               np.bincount(att_l, u, L), -np.bincount(def_l, u, L),
                               [u.sum()], [(u * heim).sum()]])

    def ziel_f(b):
        e = np.clip(Xv(b), -10, 10)
        return float(np.sum(ww * (np.exp(e) - y * e)) + 0.5 * np.sum(pen * b * b))

    b = np.zeros(P)
    b[o[4]] = math.log(max(np.average(y, weights=ww), 0.05)); b[o[5]] = 0.25
    f = ziel_f(b)
    for k in range(newton_schritte):
        lam = np.exp(np.clip(Xv(b), -10, 10))
        g = XTu(ww * (lam - y)) + pen * b
        wl = ww * lam
        diag = np.concatenate([np.bincount(att_i, wl, T), np.bincount(def_i, wl, T),
                               np.bincount(att_l, wl, L), np.bincount(def_l, wl, L),
                               [wl.sum()], [(wl * heim).sum()]]) + pen
        # CG für H s = g, Vorkonditionierung mit diag(H)
        s = np.zeros(P); r = g.copy(); z = r / diag; p = z.copy(); rz = r @ z
        for _ in range(cg_schritte):
            Hp = XTu(wl * Xv(p)) + pen * p
            al = rz / (p @ Hp)
            s += al * p; r -= al * Hp
            if np.sqrt(r @ r) < 1e-6 * np.sqrt(g @ g):
                break
            z = r / diag; rz_neu = r @ z; p = z + (rz_neu / rz) * p; rz = rz_neu
        t = 1.0
        while t > 1e-4:
            neu = b - t * s; f_neu = ziel_f(neu)
            if f_neu <= f:
                break
            t /= 2
        b = neu
        if f - f_neu < 1e-7 * max(1.0, abs(f)):
            f = f_neu
            break
        f = f_neu
    La, Ld = b[o[2]:o[3]], b[o[3]:o[4]]
    att = La[team_liga] + b[o[0]:o[1]]
    dfn = Ld[team_liga] + b[o[1]:o[2]]
    anzahl = np.bincount(hi, minlength=T) + np.bincount(ai, minlength=T)
    return {"ix": ix, "att": att, "dfn": dfn, "mu": float(b[o[4]]), "hv": float(b[o[5]]), "anzahl": anzahl,
            "n": n, "newton": k + 1, "gradnorm": float(np.sqrt(g @ g)), "ligen": L,
            "liga_staerke": {ligen[i]: (float(La[i]), float(Ld[i])) for i in range(L)}}
