# Rechenweg

Ein Tipp je Spiel, aus fünf Zahlen der FootyStats-API. Keine gesetzte Konstante.

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

**Dieser Fit liefert immer λ_heim = λ_ausw.** Die Potentiale kennen nur die Summe der
Tore, nicht die Seite.

## Schritt 3

```
lam = Mittel(lam_xg, lam_pot)
```

Beide Schritte liefern dieselbe Größe in derselben Einheit. Das Mittel ist eine
Zusammenfassung, keine Abwägung. Fehlt eine Seite, wird die andere allein genommen –
und das steht in der Ausgabe.

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
2. Jedes benutzte Feld mit Rohwert; fehlt eines, steht `FEHLT`. Nie ersetzt, nie geschätzt.
3. Eine **zweite, unabhängige Abfrage** derselben Endpunkte, am Zwischenspeicher vorbei,
   Feld für Feld gegen die erste Lesung gehalten (20 Werte). Weicht einer ab: kein Tipp.
   Schlägt die zweite Abfrage fehl (Stundenlimit): kein Tipp. Das kostet eine
   zusätzliche Abfrage je Endpunkt und Spiel.
4. `btts/o25/u25` alle drei auf 50 ist der Platzhalter der API, keine Messung – die Werte
   gehen dann nicht in den Fit.

## Tipp

Die wahrscheinlichste der fünf Wetten. Keine Schwelle.
