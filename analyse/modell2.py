#!/usr/bin/env python3
"""Neuer Rechenkern: Maximum-Likelihood-Poisson auf Spielebene.

WARUM NEU. Der Kern in modell.py schaetzt die Teamstaerke als Verhaeltnis von
Saisonmitteln (Team-Tore / Liga-Tore) und zieht sie dann mit acht handgesetzten
Konstanten zum Liga-Durchschnitt. Zwei Schwaechen, beide gemessen:

  1. Das Verhaeltnis ignoriert, GEGEN WEN gespielt wurde. Bei 10-14 Vorspielen liegen
     die Spielplaene der beiden Teams im 90. Perzentil 11,1 % auseinander. Eine
     Korrektur daraufzurechnen hat nichts gebracht (pruefung.py --gegner).
  2. Die acht Konstanten sind nicht verbesserbar: acht von acht haben in zwei
     unabhaengigen Ligen-Haelften verschiedene Optima (CLAUDE.md). Sie liegen also
     im Rauschen - jede davon koennte man ebenso gut anders setzen.

WAS STATTDESSEN. Alle Spiele einer Saison gehen gemeinsam in eine gewichtete
Poisson-Regression:

    log E[Tore Heim] = mu + heim + angriff[Heim] - abwehr[Ausw]
    log E[Tore Ausw] = mu        + angriff[Ausw] - abwehr[Heim]

Angriff und Abwehr aller Teams werden SIMULTAN geschaetzt. Dadurch ist die
Gegnerstaerke automatisch herausgerechnet: Wer gegen starke Abwehren spielte, bekommt
fuer dieselben Tore einen hoeheren Angriffswert. Das ist der Unterschied zwischen
"Mittelwert teilen" und "Modell schaetzen", und er ist nicht nachtraeglich zu
korrigieren.

Die Zielfunktion ist in diesen Parametern KONVEX - es gibt genau ein Optimum, und
L-BFGS findet es verlaesslich. Keine Startwertabhaengigkeit, kein lokales Minimum.

VIER GROESSEN statt acht Konstanten, und jede wird gegen echte Ergebnisse bestimmt:

    HALBWERT   Zeitabklingen in Tagen. Ein Spiel vor HALBWERT Tagen zaehlt halb.
               Ersetzt FORM_ANTEIL, FORM_DAEMPFUNG_K und das Formfenster - Form ist
               hier keine zweite Komponente, sondern dasselbe Modell mit Gewichten.
    RIDGE      Strafterm auf angriff und abwehr. Zieht Teams mit wenigen Spielen zum
               Liga-Durchschnitt. Ersetzt SEITE_K, DAEMPFUNG_K und MIN_SAISONSPIELE
               als Daempfung - und zwar mit einer Zahl statt dreien.
    XG_K       Gewicht des xG neben den Toren. Beobachtet wird (Tore + XG_K*xG)/(1+XG_K).
               Ersetzt XG_ANTEIL und LIGA_BASIS_XG.
    RHO        Dixon-Coles-Korrektur fuer 0:0, 1:0, 0:1, 1:1. Wird nach der Schaetzung
               aufgesetzt, damit die Zielfunktion konvex bleibt.

WAS BLEIBT. Die Liga-xG-Schranken (LIGA_XG_MIN/MAX) gelten unveraendert weiter - sie
sind eine Datenqualitaetspruefung, kein Gewicht. Ohne sie sieht jede Idee gut aus, die
ein kaputtes xG ausgleicht (am 03.10.2026 zweimal passiert).

WAS DIESE DATEI NICHT TUT. Sie rechnet keine Tipps und schreibt nichts in bilanz.json.
Sie ist der Kern; die Anbindung kommt erst, wenn der Walk-forward sie als besser
ausweist. Bis dahin bleibt modell.py der Rechenweg.
"""
import math
import numpy as np
from scipy.optimize import minimize

# Startwerte. Keine Erfahrungswerte - sie werden von pruefung2.py gegen echte
# Ergebnisse bestimmt und hier eingetragen, mit der Messung daneben.
HALBWERT = 180.0      # Tage
RIDGE    = 4.0
XG_K     = 2.0        # entspricht einem xG-Anteil von 2/3
RHO      = -0.07      # uebernommen aus modell.py, wird mitgeprueft

TAG = 86400.0
MAXTOR = 11


# --------------------------------------------------------------------- Schaetzung

def gewichte(t_jetzt, t_spiele, halbwert=HALBWERT):
    """Zeitabklingen: ein Spiel vor `halbwert` Tagen zaehlt halb so viel."""
    if not halbwert or halbwert >= 1e9:
        return np.ones(len(t_spiele))
    d = (t_jetzt - np.asarray(t_spiele, dtype=float)) / TAG
    return np.exp(-np.log(2.0) * np.maximum(d, 0.0) / halbwert)


def schaetze(ih, ia, yh, ya, w, n_teams, ridge=RIDGE, start=None):
    """Gewichtete Poisson-Regression. Gibt (mu, heim, angriff, abwehr) zurueck.

    ih, ia  Teamindex Heim bzw. Ausw je Spiel
    yh, ya  beobachtete Tore (oder Tore/xG gemischt) je Spiel
    w       Spielgewicht (Zeitabklingen)

    Die Zielfunktion ist die gewichtete Poisson-Log-Likelihood minus
    ridge * (|angriff|^2 + |abwehr|^2). Sie ist konvex, der Ridge-Term macht die
    Parameter identifizierbar (ohne ihn waere angriff+c, abwehr+c aequivalent).
    """
    ih = np.asarray(ih); ia = np.asarray(ia)
    yh = np.asarray(yh, dtype=float); ya = np.asarray(ya, dtype=float)
    w = np.asarray(w, dtype=float)
    T = n_teams
    p0 = np.zeros(2 + 2 * T) if start is None else np.array(start, dtype=float)
    if start is None:
        ges = w.sum()
        if ges > 0:
            m = max(1e-6, (w @ (yh + ya)) / (2 * ges))
            p0[0] = math.log(m)
            hm = max(1e-6, (w @ yh) / ges); am = max(1e-6, (w @ ya) / ges)
            p0[1] = math.log(hm / am) if am > 0 else 0.0

    def ziel(p):
        mu, hv = p[0], p[1]
        a = p[2:2+T]; d = p[2+T:]
        eh = mu + hv + a[ih] - d[ia]
        ea = mu + a[ia] - d[ih]
        lh = np.exp(np.clip(eh, -20, 8)); la = np.exp(np.clip(ea, -20, 8))
        # negative Log-Likelihood (die von y unabhaengigen Terme entfallen)
        nll = float(w @ (lh - yh * eh) + w @ (la - ya * ea))
        nll += ridge * float(a @ a + d @ d)
        rh = w * (yh - lh); ra = w * (ya - la)      # Residuen, Gradient der LL
        g = np.zeros_like(p)
        g[0] = -(rh.sum() + ra.sum())
        g[1] = -rh.sum()
        ga = np.bincount(ih, rh, T) + np.bincount(ia, ra, T)
        gd = -(np.bincount(ia, rh, T) + np.bincount(ih, ra, T))
        g[2:2+T] = -ga + 2 * ridge * a
        g[2+T:] = -gd + 2 * ridge * d
        return nll, g

    r = minimize(ziel, p0, jac=True, method='L-BFGS-B',
                 options=dict(maxiter=400, ftol=1e-10, gtol=1e-7))
    p = r.x
    return float(p[0]), float(p[1]), p[2:2+T].copy(), p[2+T:].copy()


def erwartete_tore(mu, hv, a, d, i_h, i_a):
    """Erwartete Tore fuer eine Paarung. Unbekanntes Team -> Liga-Durchschnitt."""
    ah = a[i_h] if i_h is not None else 0.0
    dh = d[i_h] if i_h is not None else 0.0
    aa = a[i_a] if i_a is not None else 0.0
    da = d[i_a] if i_a is not None else 0.0
    return math.exp(mu + hv + ah - da), math.exp(mu + aa - dh)


# --------------------------------------------------------------------- Vorhersage

_I, _J = np.indices((MAXTOR, MAXTOR))
_MH = _I > _J; _MA = _I < _J; _MO = _I + _J >= 3; _MB = (_I > 0) & (_J > 0)
_FAK = np.array([math.factorial(k) for k in range(MAXTOR)], dtype=float)


def matrix(lh, la, rho=RHO):
    """Ergebnis-Matrix mit Dixon-Coles-Korrektur, auf Summe 1 normiert."""
    ph = np.exp(-lh) * lh ** np.arange(MAXTOR) / _FAK
    pa = np.exp(-la) * la ** np.arange(MAXTOR) / _FAK
    Mx = np.outer(ph, pa)
    if rho:
        Mx[0, 0] *= 1 - lh * la * rho
        Mx[0, 1] *= 1 + lh * rho
        Mx[1, 0] *= 1 + la * rho
        Mx[1, 1] *= 1 - rho
        Mx = np.maximum(Mx, 1e-15)
    return Mx / Mx.sum()


def wetten(Mx):
    p = dict(H=float(Mx[_MH].sum()), A=float(Mx[_MA].sum()),
             D=float(np.trace(Mx)), O25=float(Mx[_MO].sum()),
             BTTS=float(Mx[_MB].sum()))
    p['U25'] = 1 - p['O25']
    return p


# --------------------------------------------------------------------- Saisonfit

class Saison:
    """Haelt die Spiele einer Saison und schaetzt zu jedem Zeitpunkt neu.

    `bis(t)` schaetzt aus allen Spielen mit date_unix < t. Der vorige Fit dient als
    Startwert, was den Durchlauf ueber eine ganze Saison um ein Vielfaches
    beschleunigt, ohne das Ergebnis zu aendern (die Zielfunktion ist konvex).
    """

    def __init__(self, spiele, xg_k=XG_K, xg_ok=True, halbwert=HALBWERT, ridge=RIDGE):
        self.sp = sorted(spiele, key=lambda m: m['t'])
        self.xg_k = xg_k if xg_ok else 0.0
        self.halbwert = halbwert
        self.ridge = ridge
        ids = sorted({m['h'] for m in self.sp} | {m['a'] for m in self.sp})
        self.idx = {tid: i for i, tid in enumerate(ids)}
        self.T = len(ids)
        self.t = np.array([m['t'] for m in self.sp], dtype=float)
        self.ih = np.array([self.idx[m['h']] for m in self.sp])
        self.ia = np.array([self.idx[m['a']] for m in self.sp])
        k = self.xg_k
        self.yh = np.array([(m['hg'] + k * m['hx']) / (1 + k) for m in self.sp])
        self.ya = np.array([(m['ag'] + k * m['ax']) / (1 + k) for m in self.sp])
        self._start = None

    def bis(self, t):
        n = int(np.searchsorted(self.t, t, side='left'))
        if n < 6:
            return None
        w = gewichte(t, self.t[:n], self.halbwert)
        mu, hv, a, d = schaetze(self.ih[:n], self.ia[:n], self.yh[:n], self.ya[:n],
                                w, self.T, self.ridge, self._start)
        self._start = np.concatenate(([mu, hv], a, d))
        return mu, hv, a, d

    def prognose(self, fit, heim_id, ausw_id, rho=RHO):
        mu, hv, a, d = fit
        lh, la = erwartete_tore(mu, hv, a, d,
                                self.idx.get(heim_id), self.idx.get(ausw_id))
        return lh, la, matrix(lh, la, rho)
