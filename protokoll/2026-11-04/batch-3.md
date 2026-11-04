# Vorabeintrag Batch 3 · 04.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-04 16:19 UTC
- Eintrag erstellt: 2026-11-04 16:21:29 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 3.1 Slavia Praha – Arsenal | 2026-11-04 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700185

Analyse-ID: A-20261104-8700185-r1 · Team-IDs: 1213 / 59 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Fortuna Arena · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Slavia Praha (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-10 bis 2026-10-20, Gast 2026-09-09 bis 2026-10-21; letzte 6: Heim 2026-09-10–2026-10-20, Gast 2026-09-09–2026-10-21.

**Slavia Praha (Heim, ID 1213)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 2 | 2 | 4
Gegentore | 7 | 3 | 4 | 7
Tore/Spiel | 1.33 | 2.00 | 1.00 | 1.33
Gegentore/Spiel | 2.33 | 3.00 | 2.00 | 2.33
xG für/Spiel | 1.79 | 1.78 | 1.79 | 1.79
xG gegen/Spiel | 1.89 | 2.68 | 1.50 | 1.89
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 0/1/2 | 0/0/1 | 0/1/1 | 0/1/2
Punkte/Spiel | 0.33 | 0.00 | 0.50 | 0.33
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 33 % | 100 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Arsenal (Gast, ID 59)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 6 | 3 | 3 | 6
Gegentore | 2 | 0 | 2 | 2
Tore/Spiel | 2.00 | 3.00 | 1.50 | 2.00
Gegentore/Spiel | 0.67 | 0.00 | 1.00 | 0.67
xG für/Spiel | 2.26 | 2.28 | 2.25 | 2.26
xG gegen/Spiel | 0.78 | 0.30 | 1.02 | 0.78
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 2/1/0 | 1/0/0 | 1/1/0 | 2/1/0
Punkte/Spiel | 2.33 | 3.00 | 2.00 | 2.33
BTTS % | 33 % | 0 % | 50 % | 33 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 67 % | 100 % | 50 % | 67 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Slavia Praha – Landesliga:** fehlt (Liga nicht im API-Abo)

**Arsenal – Landesliga (Saison-ID 17146, 2026-08-21 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 14 | 9 | 5 | 8
Gegentore | 5 | 2 | 3 | 4
Tore/Spiel | 1.56 | 2.25 | 1.00 | 1.33
Gegentore/Spiel | 0.56 | 0.50 | 0.60 | 0.67
xG für/Spiel | 1.52 | 2.00 | 1.14 | 1.42
xG gegen/Spiel | 1.19 | 1.08 | 1.27 | 1.32
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 8/0/1 | 4/0/0 | 4/0/1 | 5/0/1
Punkte/Spiel | 2.67 | 3.00 | 2.40 | 2.50
BTTS % | 22 % | 50 % | 0 % | 17 %
Over 2,5 % | 44 % | 75 % | 20 % | 33 %
Under 2,5 % | 56 % | 25 % | 80 % | 67 %
Clean Sheets % | 67 % | 50 % | 80 % | 67 %
Failed to Score % | 11 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Slavia Praha: 10.09. H Lens (1.00 PPG) 2:3 · 13.10. A Sabah (1.00 PPG) 0:2 · 20.10. A Fenerbahçe (0.67 PPG) 2:2

Letzte 6 Arsenal: 09.09. A Napoli (1.00 PPG) 1:0 · 13.10. H Lille (0.25 PPG) 3:0 · 21.10. A Bayern München (2.00 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Slavia Praha [2, 0, 2]; Arsenal [1, 3, 2]

**Bild:** Champions League 2026/27 mit je 3 Spielen ist eingeschränkt, weil die tschechische Liga im API-Abo fehlt und für Slavia keine Landesliga-Daten vorliegen; schwächere Offensive ist Slavia mit 4 Toren in 3 Champions-League-Spielen, gegen Arsenal mit 67 % Clean Sheets in der Champions League und 67 % in der Premier League; der Weg zu drei Toren hängt an Arsenal und wird nicht gewählt; stärkstes Gegenargument ist Arsenals geringe Auswärtstorquote in der Premier League (5 Tore in 5 Spielen, 1,14 xG) mit einem Remis in München, was das Remisrisiko erhöht, gegen Slavias 0-1-2 den Auswärtssieg (Modell 70 %) aber nicht entkräftet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 447 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 0.867, λ Gast 2.310. Prüfstand (unberührter Test, 45 Spiele ab 2026-10-13): Heimsieg besser als Grundrate (Brier 0.195 gegen 0.2492); Auswärtssieg besser als Grundrate (Brier 0.1878 gegen 0.2222); BTTS Ja nicht besser als Grundrate (Brier 0.2656 gegen 0.2495); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2223 gegen 0.211). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 12 % · Remis 18 % · Auswärtssieg 70 % · BTTS Ja 52 % · Over 2,5 62 % · Under 2,5 38 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 13 · X 6.4 · 2 1.23 · BTTS Ja 2.25 · Over 2,5 1.7 · Under 2,5 2.23.

**Auswahl:** Auswärtssieg

⚠️ Arsenal erzielte in der Premier League auswärts nur 1,0 Tore pro Spiel – Remisrisiko; Slavias Liga-Daten fehlen.

---

## 3.2 Borussia Dortmund – Real Betis | 2026-11-04 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700594

Analyse-ID: A-20261104-8700594-r1 · Team-IDs: 33 / 284 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Signal Iduna Park · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-08 bis 2026-10-20, Gast 2026-09-08 bis 2026-10-21; letzte 6: Heim 2026-09-08–2026-10-20, Gast 2026-09-08–2026-10-21.

**Borussia Dortmund (Heim, ID 33)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 5 | 3 | 2 | 5
Gegentore | 4 | 2 | 2 | 4
Tore/Spiel | 1.67 | 3.00 | 1.00 | 1.67
Gegentore/Spiel | 1.33 | 2.00 | 1.00 | 1.33
xG für/Spiel | 1.92 | 2.04 | 1.85 | 1.92
xG gegen/Spiel | 1.38 | 1.42 | 1.36 | 1.38
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 2/0/1 | 1/0/0 | 1/0/1 | 2/0/1
Punkte/Spiel | 2.00 | 3.00 | 1.50 | 2.00
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Real Betis (Gast, ID 284)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 7 | 4 | 3 | 7
Gegentore | 4 | 2 | 2 | 4
Tore/Spiel | 2.33 | 2.00 | 3.00 | 2.33
Gegentore/Spiel | 1.33 | 1.00 | 2.00 | 1.33
xG für/Spiel | 2.15 | 2.27 | 1.92 | 2.15
xG gegen/Spiel | 1.12 | 1.25 | 0.84 | 1.12
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 3/0/0 | 2/0/0 | 1/0/0 | 3/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 67 % | 50 % | 100 % | 67 %
Under 2,5 % | 33 % | 50 % | 0 % | 33 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Borussia Dortmund – Landesliga (Saison-ID 17210, 2026-08-29 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 14 | 8 | 6 | 9
Gegentore | 6 | 2 | 4 | 4
Tore/Spiel | 1.75 | 2.00 | 1.50 | 1.50
Gegentore/Spiel | 0.75 | 0.50 | 1.00 | 0.67
xG für/Spiel | 1.72 | 2.19 | 1.25 | 1.73
xG gegen/Spiel | 1.34 | 0.99 | 1.70 | 1.28
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 5/3/0 | 3/1/0 | 2/2/0 | 3/3/0
Punkte/Spiel | 2.25 | 2.50 | 2.00 | 2.00
BTTS % | 38 % | 25 % | 50 % | 33 %
Over 2,5 % | 50 % | 50 % | 50 % | 50 %
Under 2,5 % | 50 % | 50 % | 50 % | 50 %
Clean Sheets % | 62 % | 75 % | 50 % | 67 %
Failed to Score % | 12 % | 0 % | 25 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Real Betis – Landesliga (Saison-ID 17199, 2026-08-21 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 18 | 12 | 6 | 11
Gegentore | 15 | 8 | 7 | 9
Tore/Spiel | 1.64 | 2.00 | 1.20 | 1.83
Gegentore/Spiel | 1.36 | 1.33 | 1.40 | 1.50
xG für/Spiel | 1.83 | 1.83 | 1.83 | 1.75
xG gegen/Spiel | 1.68 | 1.51 | 1.88 | 1.55
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 7/2/2 | 5/0/1 | 2/2/1 | 3/2/1
Punkte/Spiel | 2.09 | 2.50 | 1.60 | 1.83
BTTS % | 55 % | 50 % | 60 % | 67 %
Over 2,5 % | 45 % | 50 % | 40 % | 50 %
Under 2,5 % | 55 % | 50 % | 60 % | 50 %
Clean Sheets % | 45 % | 50 % | 40 % | 33 %
Failed to Score % | 9 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 18 % | 17 % | 20 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Borussia Dortmund: 08.09. H Villarreal (0.75 PPG) 3:2 · 14.10. A FK Bodo - Glimt (1.00 PPG) 0:1 · 20.10. A Sabah (1.00 PPG) 2:1

Letzte 6 Real Betis: 08.09. A Lille (0.25 PPG) 3:2 · 14.10. H Porto (0.00 PPG) 3:2 · 21.10. H Feyenoord (0.75 PPG) 1:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Borussia Dortmund [3, 0, 2]; Real Betis [3, 3, 1]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Betis mit 7 Toren in 3 Champions-League-Spielen, gegen Dortmunds Heimabwehr mit 75 % Bundesliga-Clean-Sheets; ein Weg zu drei Toren ist mit 50 % Over in Dortmunds Ligaspielen unsicher; stärkstes Gegenargument gegen den Modell-Heimsieg (58 %) ist Betis' Champions-League-Bilanz von 3-0-0 und Dortmunds drei Remis in den letzten sechs Ligaspielen, und diese Gegengefahr überwiegt, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 447 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 2.243, λ Gast 1.327. Prüfstand (unberührter Test, 45 Spiele ab 2026-10-13): Heimsieg besser als Grundrate (Brier 0.195 gegen 0.2492); Auswärtssieg besser als Grundrate (Brier 0.1878 gegen 0.2222); BTTS Ja nicht besser als Grundrate (Brier 0.2656 gegen 0.2495); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2223 gegen 0.211). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 58 % · Remis 20 % · Auswärtssieg 22 % · BTTS Ja 66 % · Over 2,5 69 % · Under 2,5 31 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.67 · X 4.2 · 2 4.5 · BTTS Ja 1.47 · Over 2,5 1.5 · Under 2,5 2.62.

**Auswahl:** keine – Grund siehe Bild.

---

## 3.3 Porto – Napoli | 2026-11-04 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700606

Analyse-ID: A-20261104-8700606-r1 · Team-IDs: 82 / 74 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Estádio Do Dragão · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-08 bis 2026-10-20, Gast 2026-09-09 bis 2026-10-20; letzte 6: Heim 2026-09-08–2026-10-20, Gast 2026-09-09–2026-10-20.

**Porto (Heim, ID 82)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 2 | 0 | 2 | 2
Gegentore | 6 | 3 | 3 | 6
Tore/Spiel | 0.67 | 0.00 | 2.00 | 0.67
Gegentore/Spiel | 2.00 | 1.50 | 3.00 | 2.00
xG für/Spiel | 1.08 | 0.96 | 1.31 | 1.08
xG gegen/Spiel | 2.02 | 2.05 | 1.95 | 2.02
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 0/0/3 | 0/0/2 | 0/0/1 | 0/0/3
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 33 % | 0 % | 100 % | 33 %
Over 2,5 % | 33 % | 0 % | 100 % | 33 %
Under 2,5 % | 67 % | 100 % | 0 % | 67 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 67 % | 100 % | 0 % | 67 %
BTTS-and-lose % | 33 % | 0 % | 100 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Napoli (Gast, ID 74)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 5 | 4 | 1 | 5
Gegentore | 7 | 4 | 3 | 7
Tore/Spiel | 1.67 | 2.00 | 1.00 | 1.67
Gegentore/Spiel | 2.33 | 2.00 | 3.00 | 2.33
xG für/Spiel | 1.33 | 1.33 | 1.33 | 1.33
xG gegen/Spiel | 2.12 | 2.42 | 1.53 | 2.12
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/0/2 | 1/0/1 | 0/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 1.50 | 0.00 | 1.00
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 67 % | 50 % | 100 % | 67 %
Under 2,5 % | 33 % | 50 % | 0 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 50 % | 0 % | 33 %
BTTS-and-lose % | 33 % | 0 % | 100 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Porto – Landesliga (Saison-ID 17217, 2026-08-09 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 25 | 13 | 12 | 16
Gegentore | 4 | 2 | 2 | 4
Tore/Spiel | 2.50 | 2.60 | 2.40 | 2.67
Gegentore/Spiel | 0.40 | 0.40 | 0.40 | 0.67
xG für/Spiel | 1.90 | 2.25 | 1.56 | 2.15
xG gegen/Spiel | 0.98 | 0.88 | 1.08 | 0.98
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 10/0/0 | 5/0/0 | 5/0/0 | 6/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 40 % | 40 % | 40 % | 67 %
Over 2,5 % | 60 % | 60 % | 60 % | 83 %
Under 2,5 % | 40 % | 40 % | 40 % | 17 %
Clean Sheets % | 60 % | 60 % | 60 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Napoli – Landesliga (Saison-ID 17084, 2026-08-22 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 4 | 6 | 6
Tore | 17 | 8 | 9 | 11
Gegentore | 13 | 5 | 8 | 8
Tore/Spiel | 1.70 | 2.00 | 1.50 | 1.83
Gegentore/Spiel | 1.30 | 1.25 | 1.33 | 1.33
xG für/Spiel | 1.75 | 1.74 | 1.76 | 1.86
xG gegen/Spiel | 1.68 | 1.70 | 1.67 | 1.64
Spiele mit xG | 10 | 4 | 6 | 6
S/U/N | 4/2/4 | 2/1/1 | 2/1/3 | 2/2/2
Punkte/Spiel | 1.40 | 1.75 | 1.17 | 1.33
BTTS % | 50 % | 50 % | 50 % | 50 %
Over 2,5 % | 50 % | 75 % | 33 % | 50 %
Under 2,5 % | 50 % | 25 % | 67 % | 50 %
Clean Sheets % | 30 % | 50 % | 17 % | 17 %
Failed to Score % | 20 % | 0 % | 33 % | 33 %
BTTS-and-lose % | 20 % | 25 % | 17 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Porto: 08.09. H Manchester City (2.00 PPG) 0:2 · 14.10. A Real Betis (3.00 PPG) 2:3 · 20.10. H PSV (1.33 PPG) 0:1

Letzte 6 Napoli: 09.09. H Arsenal (2.33 PPG) 0:1 · 13.10. A Villarreal (0.75 PPG) 1:3 · 20.10. H FK Bodo - Glimt (1.00 PPG) 4:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Porto [0, 2, 0]; Napoli [0, 1, 4]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Porto in der Champions League mit 2 Toren in 3 Spielen und ohne Heimtor (1,08 xG), obwohl Porto in der Liga 10-0-0 steht; ein Weg zu drei Toren ist mit 33 % Over in Portos Champions-League-Spielen unsicher; stärkstes Gegenargument gegen den Modell-Heimsieg (57 %) ist dieser ungeklärte Widerspruch zwischen Portos Liga- und Champions-League-Bild, der eine Auswahl verhindert.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 447 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 2.035, λ Gast 1.197. Prüfstand (unberührter Test, 45 Spiele ab 2026-10-13): Heimsieg besser als Grundrate (Brier 0.195 gegen 0.2492); Auswärtssieg besser als Grundrate (Brier 0.1878 gegen 0.2222); BTTS Ja nicht besser als Grundrate (Brier 0.2656 gegen 0.2495); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2223 gegen 0.211). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 57 % · Remis 21 % · Auswärtssieg 22 % · BTTS Ja 61 % · Over 2,5 63 % · Under 2,5 37 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.83 · X 3.74 · 2 4.2 · BTTS Ja 1.67 · Over 2,5 1.66 · Under 2,5 2.2.

**Auswahl:** keine – Grund siehe Bild.

---

## 3.4 Lens – Como | 2026-11-04 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 4 | Match-ID 8700706

Analyse-ID: A-20261104-8700706-r1 · Team-IDs: 449 / 518 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Stade Bollaert-Delelis · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-10 bis 2026-10-21, Gast 2026-09-10 bis 2026-10-21; letzte 6: Heim 2026-09-10–2026-10-21, Gast 2026-09-10–2026-10-21.

**Lens (Heim, ID 449)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 3 | 0 | 3 | 3
Gegentore | 7 | 2 | 5 | 7
Tore/Spiel | 1.00 | 0.00 | 1.50 | 1.00
Gegentore/Spiel | 2.33 | 2.00 | 2.50 | 2.33
xG für/Spiel | 2.34 | 2.20 | 2.41 | 2.34
xG gegen/Spiel | 1.51 | 1.34 | 1.59 | 1.51
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 0/0/1 | 1/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 0.00 | 1.50 | 1.00
BTTS % | 33 % | 0 % | 50 % | 33 %
Over 2,5 % | 67 % | 0 % | 100 % | 67 %
Under 2,5 % | 33 % | 100 % | 0 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 67 % | 100 % | 50 % | 67 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Como (Gast, ID 518)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 10 | 8 | 2 | 10
Gegentore | 5 | 2 | 3 | 5
Tore/Spiel | 3.33 | 4.00 | 2.00 | 3.33
Gegentore/Spiel | 1.67 | 1.00 | 3.00 | 1.67
xG für/Spiel | 1.45 | 1.53 | 1.28 | 1.45
xG gegen/Spiel | 1.45 | 1.45 | 1.44 | 1.45
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 2/0/1 | 2/0/0 | 0/0/1 | 2/0/1
Punkte/Spiel | 2.00 | 3.00 | 0.00 | 2.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 0 % | 100 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Lens – Landesliga (Saison-ID 17102, 2026-08-22 bis 2026-10-30)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 16 | 9 | 7 | 10
Gegentore | 13 | 5 | 8 | 8
Tore/Spiel | 1.78 | 2.25 | 1.40 | 1.67
Gegentore/Spiel | 1.44 | 1.25 | 1.60 | 1.33
xG für/Spiel | 1.49 | 1.64 | 1.37 | 1.32
xG gegen/Spiel | 1.33 | 1.02 | 1.57 | 1.31
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 4/1/4 | 3/0/1 | 1/1/3 | 3/1/2
Punkte/Spiel | 1.44 | 2.25 | 0.80 | 1.67
BTTS % | 78 % | 75 % | 80 % | 83 %
Over 2,5 % | 78 % | 75 % | 80 % | 83 %
Under 2,5 % | 22 % | 25 % | 20 % | 17 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 22 % | 25 % | 20 % | 17 %
BTTS-and-lose % | 22 % | 0 % | 40 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Como – Landesliga (Saison-ID 17084, 2026-08-22 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 4 | 6 | 6
Tore | 18 | 5 | 13 | 9
Gegentore | 8 | 1 | 7 | 4
Tore/Spiel | 1.80 | 1.25 | 2.17 | 1.50
Gegentore/Spiel | 0.80 | 0.25 | 1.17 | 0.67
xG für/Spiel | 2.18 | 2.18 | 2.18 | 2.06
xG gegen/Spiel | 1.30 | 0.91 | 1.56 | 1.29
Spiele mit xG | 10 | 4 | 6 | 6
S/U/N | 7/2/1 | 3/1/0 | 4/1/1 | 4/1/1
Punkte/Spiel | 2.30 | 2.50 | 2.17 | 2.17
BTTS % | 60 % | 25 % | 83 % | 33 %
Over 2,5 % | 50 % | 25 % | 67 % | 33 %
Under 2,5 % | 50 % | 75 % | 33 % | 67 %
Clean Sheets % | 30 % | 75 % | 0 % | 50 %
Failed to Score % | 20 % | 25 % | 17 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Lens: 10.09. A Slavia Praha (0.33 PPG) 3:2 · 13.10. H Sporting CP (2.25 PPG) 0:2 · 21.10. A Club Brugge (2.00 PPG) 0:3

Letzte 6 Como: 10.09. H RB Leipzig (1.00 PPG) 4:1 · 14.10. A Feyenoord (0.75 PPG) 2:3 · 21.10. H Manchester United (1.50 PPG) 4:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Lens [3, 0, 0]; Como [4, 2, 4]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Lens mit 3 Toren in 3 Champions-League-Spielen und zwei torlosen Spielen trotz 2,34 xG, das in der Ligue 1 aber in 78 % der Spiele traf, gegen Como ohne Clean Sheet in der Champions League und in 6 Serie-A-Auswärtsspielen, während Como in allen 3 Champions-League-Spielen traf (10 Tore) gegen Lens ohne Clean Sheet in Liga und Champions League; der Weg zu drei Toren ist plausibel (Modell 64 %), BTTS ist durch Comos durchlässige Abwehr und Lens' fehlende Clean Sheets aber direkter belegt (Modell 66 %); stärkstes Gegenargument ist Lens' wiederholte Torlosigkeit in der Champions League, die nach der BTTS-Präzisierung nicht durch gute xG überdeckt werden darf und als wesentliche Gefahr für den Heimtreffer gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 447 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.639, λ Gast 1.680. Prüfstand (unberührter Test, 45 Spiele ab 2026-10-13): Heimsieg besser als Grundrate (Brier 0.195 gegen 0.2492); Auswärtssieg besser als Grundrate (Brier 0.1878 gegen 0.2222); BTTS Ja nicht besser als Grundrate (Brier 0.2656 gegen 0.2495); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2223 gegen 0.211). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 38 % · Remis 23 % · Auswärtssieg 39 % · BTTS Ja 66 % · Over 2,5 64 % · Under 2,5 36 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.5 · X 3.68 · 2 1.95 · BTTS Ja 1.5 · Over 2,5 1.59 · Under 2,5 2.37.

**Auswahl:** BTTS Ja

⚠️ Lens blieb in 2 von 3 Champions-League-Spielen torlos – Gefahr für den Heimtreffer.

---

## 3.5 PSV – Club Brugge | 2026-11-04 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 4 | Match-ID 8700816

Analyse-ID: A-20261104-8700816-r1 · Team-IDs: 121 / 95 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Philips Stadion · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-10 bis 2026-10-20, Gast 2026-09-08 bis 2026-10-21; letzte 6: Heim 2026-09-10–2026-10-20, Gast 2026-09-08–2026-10-21.

**PSV (Heim, ID 121)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 2 | 1 | 1 | 2
Gegentore | 2 | 1 | 1 | 2
Tore/Spiel | 0.67 | 1.00 | 0.50 | 0.67
Gegentore/Spiel | 0.67 | 1.00 | 0.50 | 0.67
xG für/Spiel | 1.40 | 1.06 | 1.57 | 1.40
xG gegen/Spiel | 1.42 | 0.76 | 1.75 | 1.42
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 0/1/0 | 1/0/1 | 1/1/1
Punkte/Spiel | 1.33 | 1.00 | 1.50 | 1.33
BTTS % | 33 % | 100 % | 0 % | 33 %
Over 2,5 % | 0 % | 0 % | 0 % | 0 %
Under 2,5 % | 100 % | 100 % | 100 % | 100 %
Clean Sheets % | 33 % | 0 % | 50 % | 33 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Club Brugge (Gast, ID 95)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 9 | 5 | 4 | 9
Gegentore | 6 | 3 | 3 | 6
Tore/Spiel | 3.00 | 2.50 | 4.00 | 3.00
Gegentore/Spiel | 2.00 | 1.50 | 3.00 | 2.00
xG für/Spiel | 1.80 | 1.65 | 2.10 | 1.80
xG gegen/Spiel | 2.45 | 2.15 | 3.07 | 2.45
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 2/0/1 | 1/0/1 | 1/0/0 | 2/0/1
Punkte/Spiel | 2.00 | 1.50 | 3.00 | 2.00
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 50 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**PSV – Landesliga (Saison-ID 17097, 2026-08-08 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 35 | 21 | 14 | 17
Gegentore | 13 | 5 | 8 | 7
Tore/Spiel | 3.18 | 3.50 | 2.80 | 2.83
Gegentore/Spiel | 1.18 | 0.83 | 1.60 | 1.17
xG für/Spiel | 2.27 | 2.46 | 2.04 | 2.05
xG gegen/Spiel | 1.18 | 1.10 | 1.28 | 1.36
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 7/2/2 | 4/2/0 | 3/0/2 | 3/1/2
Punkte/Spiel | 2.09 | 2.33 | 1.80 | 1.67
BTTS % | 82 % | 67 % | 100 % | 67 %
Over 2,5 % | 82 % | 67 % | 100 % | 67 %
Under 2,5 % | 18 % | 33 % | 0 % | 33 %
Clean Sheets % | 18 % | 33 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 18 % | 0 % | 40 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Club Brugge – Landesliga (Saison-ID 17171, 2026-08-07 bis 2026-10-30)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 26 | 13 | 13 | 18
Gegentore | 8 | 3 | 5 | 6
Tore/Spiel | 2.60 | 2.60 | 2.60 | 3.00
Gegentore/Spiel | 0.80 | 0.60 | 1.00 | 1.00
xG für/Spiel | 2.05 | 2.15 | 1.94 | 2.07
xG gegen/Spiel | 1.25 | 1.27 | 1.23 | 1.26
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 9/0/1 | 5/0/0 | 4/0/1 | 6/0/0
Punkte/Spiel | 2.70 | 3.00 | 2.40 | 3.00
BTTS % | 50 % | 40 % | 60 % | 67 %
Over 2,5 % | 80 % | 80 % | 80 % | 83 %
Under 2,5 % | 20 % | 20 % | 20 % | 17 %
Clean Sheets % | 50 % | 60 % | 40 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 10 % | 0 % | 20 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 PSV: 10.09. H Shakhtar Donetsk (1.00 PPG) 1:1 · 13.10. A RB Leipzig (1.00 PPG) 0:1 · 20.10. A Porto (0.00 PPG) 1:0

Letzte 6 Club Brugge: 08.09. H Aston Villa (2.25 PPG) 2:3 · 13.10. A Inter Milan (1.50 PPG) 4:3 · 21.10. H Lens (1.00 PPG) 3:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): PSV [1, 0, 1]; Club Brugge [2, 4, 3]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist PSV in der Champions League mit 2 Toren in 3 Spielen (1,40 xG), obwohl PSV in der Eredivisie 35 Tore in 11 Spielen erzielte; der Weg zu drei Toren ist widersprüchlich, weil alle Brügge-Spiele Over, alle PSV-Spiele in der Champions League aber Under endeten; stärkstes Gegenargument gegen den Modell-Heimsieg (53 %) ist Brügges Form mit 6-0-0 in der Liga und 2-0-1 in der Champions League, sodass kein Markt widerspruchsfrei getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 447 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 2.050, λ Gast 1.393. Prüfstand (unberührter Test, 45 Spiele ab 2026-10-13): Heimsieg besser als Grundrate (Brier 0.195 gegen 0.2492); Auswärtssieg besser als Grundrate (Brier 0.1878 gegen 0.2222); BTTS Ja nicht besser als Grundrate (Brier 0.2656 gegen 0.2495); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2223 gegen 0.211). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 53 % · Remis 21 % · Auswärtssieg 26 % · BTTS Ja 66 % · Over 2,5 67 % · Under 2,5 33 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.93 · X 4.24 · 2 3.4 · BTTS Ja 1.3 · Over 2,5 1.33 · Under 2,5 3.37.

**Auswahl:** keine – Grund siehe Bild.

---
