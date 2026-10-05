# Rechenweg

Ein Tipp je Spiel, aus fünf Zahlen der FootyStats-API. Keine gesetzte Konstante.

**Nichts Altes.** Keine Datei des alten Systems, kein Backtesting, keine Rückschau,
keine gesetzte oder angepasste Zahl, kein fremdes Repo, nicht dessen Zwischenspeicher.
Jede Zahl hier muss aus einer frischen API-Antwort kommen. Siehe `CLAUDE.md`.

## Eingaben

| Größe | Feld | Endpunkt |
|---|---|---|
| Pre-Match-xG Heim | `team_a_xg_prematch` | `match` |
| Pre-Match-xG Auswärts | `team_b_xg_prematch` | `match` |
| BTTS-Potential | `btts_potential` | `match` |
| Over-Potential | `o25_potential` | `match` |
| Under-Potential | `u25_potential` | `match` |
| xG für / gegen, Heim und Auswärts | `xg_for_avg_*`, `xg_against_avg_*` | `league-teams` |

## Schritt 1 – Tor-Skala

Zwei gleichwertige Schätzungen je Seite:

```
a) Pre-Match-xG der API
b) (xG_für der einen Seite + xG_gegen der anderen) / 2

lam_xg = Mittel(a, b)
```

## Schritt 2 – Wahrscheinlichkeits-Skala

Gesucht sind die beiden λ, deren Poisson die drei Potentiale am besten trifft:

```
minimiere (P_BTTS − btts)² + (P_Over − o25)² + (P_Under − u25)²
```

Drei Gleichungen, zwei Unbekannte, kleinste Quadrate. Alle drei Residuen stehen auf
derselben Skala (0 bis 1) – deshalb braucht es **keine** Gewichtung.

**Die Potentiale kennen die Seite nicht.** Der Fit liefert oft zwei verschiedene Werte,
aber die vertauschte Zuordnung trifft die Potentiale genauso gut – welche Seite den
größeren bekäme, hinge nur vom Startpunkt der Suche ab. Beide Zuordnungen werden
deshalb gleich behandelt:

```
lam_pot = (Fit_heim + Fit_ausw) / 2, für beide Seiten
```

Die Torsumme bleibt dabei unverändert. **λ_pot ist damit immer für beide Seiten gleich.**

## Schritt 3

```
lam = Mittel(lam_xg, lam_pot)
```

Beide Schritte liefern dieselbe Größe in derselben Einheit. Das Mittel ist eine
Zusammenfassung, keine Abwägung. Fehlt eines der benutzten Felder, gibt es keinen Tipp –
es wird nicht mit den übrigen weitergerechnet.

## Verteilung

Reine unabhängige Poisson über eine 12×12-Ergebnismatrix, auf Summe 1 normiert.
Keine Dixon-Coles-Korrektur: ρ wäre eine gesetzte Zahl.

```
Heimsieg      Summe über i > j
Auswärtssieg  Summe über i < j
Über 2,5      Summe über i + j >= 3
Unter 2,5     1 − Über 2,5
BTTS Ja       Summe über i > 0 und j > 0

faire Quote = 1 / Wahrscheinlichkeit
```

## Prüfung vor jedem Tipp

1. Spiel und Teams über die `id`, mit Namen, Team-`id`s, Liga, Anstoß und `status`.
2. Jedes benutzte Feld mit Rohwert; fehlt eines, steht `FEHLT` und es gibt keinen Tipp.
   Nie ersetzt, nie geschätzt, nie mit den übrigen Feldern weitergerechnet.
3. Eine **zweite, unabhängige Abfrage** derselben Endpunkte, am Zwischenspeicher vorbei,
   Feld für Feld gegen die erste Lesung gehalten (20 Werte). Weicht einer ab: kein Tipp.
   Schlägt die zweite Abfrage fehl (Stundenlimit): kein Tipp. Das kostet eine
   zusätzliche Abfrage je Endpunkt und Spiel.
4. **Jeder Wert, den die API liefert, geht unverändert in den Fit.** Es gibt keine
   Platzhalter-Erkennung und keine Prüfung, ob eine Zahl plausibel aussieht. `FEHLT`
   heißt: das Feld ist nicht da. Eine Null ist eine Zahl.

## Tipp

Die wahrscheinlichste der fünf Wetten. Keine Schwelle.
