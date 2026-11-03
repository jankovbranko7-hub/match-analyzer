# Vorabeintrag Batch 4 · 03.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-03 14:33 UTC
- Eintrag erstellt: 2026-11-03 14:37:48 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 4.1 Atlético Madrid – Bayern München | 2026-11-03 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 4 | Match-ID 8700136

Analyse-ID: A-20261103-8700136-r1 · Team-IDs: 117 / 38 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Riyadh Air Metropolitano · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-09 bis 2026-10-20, Gast 2026-09-10 bis 2026-10-21; letzte 6: Heim 2026-09-09–2026-10-20, Gast 2026-09-10–2026-10-21.

**Atlético Madrid (Heim, ID 117)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 2 | 2 | 4
Gegentore | 3 | 0 | 3 | 3
Tore/Spiel | 1.33 | 2.00 | 1.00 | 1.33
Gegentore/Spiel | 1.00 | 0.00 | 1.50 | 1.00
xG für/Spiel | 1.20 | 1.38 | 1.11 | 1.20
xG gegen/Spiel | 1.58 | 1.10 | 1.81 | 1.58
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 1/0/0 | 0/1/1 | 1/1/1
Punkte/Spiel | 1.33 | 3.00 | 0.50 | 1.33
BTTS % | 67 % | 0 % | 100 % | 67 %
Over 2,5 % | 33 % | 0 % | 50 % | 33 %
Under 2,5 % | 67 % | 100 % | 50 % | 67 %
Clean Sheets % | 33 % | 100 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Bayern München (Gast, ID 38)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 10 | 7 | 3 | 10
Gegentore | 5 | 2 | 3 | 5
Tore/Spiel | 3.33 | 3.50 | 3.00 | 3.33
Gegentore/Spiel | 1.67 | 1.00 | 3.00 | 1.67
xG für/Spiel | 2.38 | 2.17 | 2.82 | 2.38
xG gegen/Spiel | 0.99 | 0.96 | 1.06 | 0.99
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/2/0 | 1/1/0 | 0/1/0 | 1/2/0
Punkte/Spiel | 1.67 | 2.00 | 1.00 | 1.67
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Atlético Madrid – Landesliga (Saison-ID 17199, 2026-08-19 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 22 | 11 | 11 | 12
Gegentore | 8 | 3 | 5 | 2
Tore/Spiel | 2.00 | 2.20 | 1.83 | 2.00
Gegentore/Spiel | 0.73 | 0.60 | 0.83 | 0.33
xG für/Spiel | 1.91 | 2.14 | 1.71 | 2.11
xG gegen/Spiel | 1.20 | 1.04 | 1.34 | 1.13
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 9/1/1 | 4/1/0 | 5/0/1 | 6/0/0
Punkte/Spiel | 2.55 | 2.60 | 2.50 | 3.00
BTTS % | 36 % | 40 % | 33 % | 33 %
Over 2,5 % | 64 % | 60 % | 67 % | 50 %
Under 2,5 % | 36 % | 40 % | 33 % | 50 %
Clean Sheets % | 55 % | 60 % | 50 % | 67 %
Failed to Score % | 9 % | 0 % | 17 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Bayern München – Landesliga (Saison-ID 17210, 2026-08-28 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 27 | 20 | 7 | 22
Gegentore | 8 | 4 | 4 | 7
Tore/Spiel | 3.38 | 5.00 | 1.75 | 3.67
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.17
xG für/Spiel | 2.73 | 2.84 | 2.62 | 2.86
xG gegen/Spiel | 1.02 | 1.07 | 0.97 | 1.07
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 5/3/0 | 3/1/0 | 2/2/0 | 4/2/0
Punkte/Spiel | 2.25 | 2.50 | 2.00 | 2.33
BTTS % | 75 % | 75 % | 75 % | 83 %
Over 2,5 % | 88 % | 100 % | 75 % | 100 %
Under 2,5 % | 12 % | 0 % | 25 % | 0 %
Clean Sheets % | 25 % | 25 % | 25 % | 17 %
Failed to Score % | 12 % | 0 % | 25 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Atlético Madrid: 09.09. A Liverpool (3.00 PPG) 1:2 · 13.10. H Manchester United (1.00 PPG) 2:0 · 20.10. A Stuttgart (2.33 PPG) 1:1

Letzte 6 Bayern München: 10.09. H FK Bodo - Glimt (1.00 PPG) 5:0 · 13.10. A Viking (0.33 PPG) 3:3 · 21.10. H Arsenal (2.33 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Atlético Madrid [1, 2, 1]; Bayern München [5, 3, 2]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Atlético, das aber in allen 3 Champions-League-Spielen und in jedem La-Liga-Heimspiel traf, gegen Bayern mit 1,02 xG gegen in der Bundesliga, während Bayern in allen 3 Champions-League-Spielen (10 Tore) und in den letzten sechs Ligaspielen jeweils traf gegen Atléticos Abwehr; der Weg zu drei Toren ist plausibel (Modell 71 %), Atléticos Champions-League-Spiele gingen aber nur zu 33 % Over, weshalb BTTS (Modell 70 %) besser belegt ist; stärkstes Gegenargument ist Atléticos Defensive mit 60 % Heim-Clean-Sheets und 4 Zu-null-Spielen in den letzten sechs Ligaspielen, die den Bayern-Treffer gefährdet und als wesentliche Gefahr gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.915, λ Gast 1.737. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 43 % · Remis 22 % · Auswärtssieg 36 % · BTTS Ja 70 % · Over 2,5 71 % · Under 2,5 29 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.72 · X 4 · 2 2.45 · BTTS Ja 1.4 · Over 2,5 1.39 · Under 2,5 2.73.

**Auswahl:** BTTS Ja

⚠️ Atlético hielt in den letzten 6 La-Liga-Spielen viermal die Null und daheim in 60 % der Spiele – Gefahr für den Bayern-Treffer.

---

## 4.2 Manchester United – Roma | 2026-11-03 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700172

Analyse-ID: A-20261103-8700172-r1 · Team-IDs: 149 / 113 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Old Trafford · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-10 bis 2026-10-21, Gast 2026-09-10 bis 2026-10-20; letzte 6: Heim 2026-09-10–2026-10-21, Gast 2026-09-10–2026-10-20.

**Manchester United (Heim, ID 149)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 5 | 4 | 1 | 5
Gegentore | 6 | 0 | 6 | 6
Tore/Spiel | 1.67 | 4.00 | 0.50 | 1.67
Gegentore/Spiel | 2.00 | 0.00 | 3.00 | 2.00
xG für/Spiel | 1.64 | 2.49 | 1.22 | 1.64
xG gegen/Spiel | 1.29 | 0.99 | 1.44 | 1.29
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 1/0/0 | 0/0/2 | 1/0/2
Punkte/Spiel | 1.00 | 3.00 | 0.00 | 1.00
BTTS % | 33 % | 0 % | 50 % | 33 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 33 % | 100 % | 0 % | 33 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Roma (Gast, ID 113)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 8 | 7 | 1 | 8
Gegentore | 5 | 4 | 1 | 5
Tore/Spiel | 2.67 | 3.50 | 1.00 | 2.67
Gegentore/Spiel | 1.67 | 2.00 | 1.00 | 1.67
xG für/Spiel | 1.98 | 2.33 | 1.28 | 1.98
xG gegen/Spiel | 1.09 | 1.05 | 1.16 | 1.09
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/1/1 | 1/0/1 | 0/1/0 | 1/1/1
Punkte/Spiel | 1.33 | 1.50 | 1.00 | 1.33
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 67 % | 100 % | 0 % | 67 %
Under 2,5 % | 33 % | 0 % | 100 % | 33 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 50 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Manchester United – Landesliga (Saison-ID 17146, 2026-08-22 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 10 | 6 | 4 | 3
Gegentore | 15 | 7 | 8 | 9
Tore/Spiel | 1.11 | 1.50 | 0.80 | 0.50
Gegentore/Spiel | 1.67 | 1.75 | 1.60 | 1.50
xG für/Spiel | 1.94 | 2.09 | 1.82 | 1.74
xG gegen/Spiel | 1.43 | 1.17 | 1.64 | 1.47
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 1/4/4 | 1/1/2 | 0/3/2 | 0/3/3
Punkte/Spiel | 0.78 | 1.00 | 0.60 | 0.50
BTTS % | 56 % | 50 % | 60 % | 50 %
Over 2,5 % | 33 % | 50 % | 20 % | 17 %
Under 2,5 % | 67 % | 50 % | 80 % | 83 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 44 % | 50 % | 40 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Roma – Landesliga (Saison-ID 17084, 2026-08-24 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 28 | 14 | 14 | 16
Gegentore | 10 | 5 | 5 | 9
Tore/Spiel | 2.80 | 2.80 | 2.80 | 2.67
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.50
xG für/Spiel | 2.06 | 2.36 | 1.76 | 1.82
xG gegen/Spiel | 1.36 | 1.28 | 1.44 | 1.67
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 7/3/0 | 4/1/0 | 3/2/0 | 3/3/0
Punkte/Spiel | 2.40 | 2.60 | 2.20 | 2.00
BTTS % | 50 % | 60 % | 40 % | 67 %
Over 2,5 % | 70 % | 80 % | 60 % | 67 %
Under 2,5 % | 30 % | 20 % | 40 % | 33 %
Clean Sheets % | 50 % | 40 % | 60 % | 33 %
Failed to Score % | 10 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Manchester United: 10.09. H Sabah (1.00 PPG) 4:0 · 13.10. A Atlético Madrid (1.33 PPG) 0:2 · 21.10. A Como (2.00 PPG) 1:4

Letzte 6 Roma: 10.09. A Fenerbahçe (0.67 PPG) 1:1 · 14.10. H Real Madrid (3.00 PPG) 3:4 · 20.10. H Slovan Bratislava (0.00 PPG) 4:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Manchester United [4, 0, 1]; Roma [1, 3, 4]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Manchester United mit 3 Toren in den letzten sechs Premier-League-Spielen (50 % torlos) trotz 1,74 xG; ein Weg zu drei Toren ist mit 17 % Over in Uniteds letzten sechs Ligaspielen schwach belegt, obwohl das Modell 71 % schätzt; stärkstes Gegenargument gegen den Modell-Heimsieg (47 %) ist Uniteds Ligaform mit 0-3-3 gegen Romas ungeschlagene Serie-A-Bilanz (7-3-0), und gegen BTTS spricht Uniteds wiederholte Torlosigkeit, die nach der BTTS-Präzisierung nicht durch gute xG überdeckt werden darf, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 2.029, λ Gast 1.645. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 47 % · Remis 21 % · Auswärtssieg 32 % · BTTS Ja 70 % · Over 2,5 71 % · Under 2,5 29 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.2 · X 3.95 · 2 2.9 · BTTS Ja 1.44 · Over 2,5 1.44 · Under 2,5 2.61.

**Auswahl:** keine – Grund siehe Bild.

---

## 4.3 Villarreal – PSG | 2026-11-03 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700158

Analyse-ID: A-20261103-8700158-r1 · Team-IDs: 76 / 68 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Estadio de la Cerámica · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-08 bis 2026-10-20, Gast 2026-09-09 bis 2026-10-20; letzte 6: Heim 2026-09-08–2026-10-20, Gast 2026-09-09–2026-10-20.

**Villarreal (Heim, ID 76)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 8 | 3 | 5 | 8
Gegentore | 8 | 1 | 7 | 8
Tore/Spiel | 2.67 | 3.00 | 2.50 | 2.67
Gegentore/Spiel | 2.67 | 1.00 | 3.50 | 2.67
xG für/Spiel | 1.48 | 1.53 | 1.46 | 1.48
xG gegen/Spiel | 1.90 | 1.33 | 2.19 | 1.90
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 1/0/0 | 0/0/2 | 1/0/2
Punkte/Spiel | 1.00 | 3.00 | 0.00 | 1.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 67 % | 0 % | 100 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**PSG (Gast, ID 68)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 14 | 10 | 4 | 14
Gegentore | 5 | 3 | 2 | 5
Tore/Spiel | 4.67 | 5.00 | 4.00 | 4.67
Gegentore/Spiel | 1.67 | 1.50 | 2.00 | 1.67
xG für/Spiel | 2.80 | 3.27 | 1.85 | 2.80
xG gegen/Spiel | 1.86 | 1.38 | 2.83 | 1.86
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 3/0/0 | 2/0/0 | 1/0/0 | 3/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Villarreal – Landesliga (Saison-ID 17199, 2026-08-16 bis 2026-10-30)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 15 | 6 | 9 | 8
Gegentore | 15 | 7 | 8 | 5
Tore/Spiel | 1.36 | 1.20 | 1.50 | 1.33
Gegentore/Spiel | 1.36 | 1.40 | 1.33 | 0.83
xG für/Spiel | 1.93 | 2.03 | 1.85 | 1.95
xG gegen/Spiel | 1.22 | 1.15 | 1.27 | 0.86
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 3/3/5 | 1/1/3 | 2/2/2 | 3/1/2
Punkte/Spiel | 1.09 | 0.80 | 1.33 | 1.67
BTTS % | 64 % | 60 % | 67 % | 50 %
Over 2,5 % | 64 % | 60 % | 67 % | 50 %
Under 2,5 % | 36 % | 40 % | 33 % | 50 %
Clean Sheets % | 9 % | 20 % | 0 % | 17 %
Failed to Score % | 36 % | 40 % | 33 % | 50 %
BTTS-and-lose % | 18 % | 40 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**PSG – Landesliga (Saison-ID 17102, 2026-08-23 bis 2026-10-30)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 3 | 6 | 6
Tore | 21 | 6 | 15 | 16
Gegentore | 10 | 3 | 7 | 4
Tore/Spiel | 2.33 | 2.00 | 2.50 | 2.67
Gegentore/Spiel | 1.11 | 1.00 | 1.17 | 0.67
xG für/Spiel | 2.35 | 2.42 | 2.31 | 2.33
xG gegen/Spiel | 1.20 | 0.88 | 1.36 | 1.38
Spiele mit xG | 9 | 3 | 6 | 6
S/U/N | 6/2/1 | 2/0/1 | 4/2/0 | 6/0/0
Punkte/Spiel | 2.22 | 2.00 | 2.33 | 3.00
BTTS % | 78 % | 67 % | 83 % | 67 %
Over 2,5 % | 78 % | 67 % | 83 % | 67 %
Under 2,5 % | 22 % | 33 % | 17 % | 33 %
Clean Sheets % | 22 % | 33 % | 17 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 11 % | 33 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Villarreal: 08.09. A Borussia Dortmund (2.00 PPG) 2:3 · 13.10. H Napoli (1.00 PPG) 3:1 · 20.10. A Liverpool (3.00 PPG) 3:4

Letzte 6 PSG: 09.09. H Slovan Bratislava (0.00 PPG) 6:1 · 14.10. A Manchester City (2.00 PPG) 4:2 · 20.10. H FC Barcelona (2.00 PPG) 4:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Villarreal [2, 3, 3]; PSG [6, 4, 4]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Villarreal, das aber in allen 3 Champions-League-Spielen traf (8 Tore), gegen PSG ohne Champions-League-Clean-Sheet; der Weg zu drei Toren ist stark, weil Villarreals Champions-League-Spiele 5, 4 und 7 Tore und PSGs 7, 6 und 6 Tore brachten, PSG in der Ligue 1 auswärts zu 83 % Over spielte und auch allein drei Tore liefern kann (14 Champions-League-Tore), und das Modell schätzt 69 %; stärkstes Gegenargument ist Villarreals Liga-Abwehr der letzten sechs mit 0,86 xG gegen und 50 % Over, das gegen das eindeutige Champions-League-Bild aber keine wesentliche Gefahr begründet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.359, λ Gast 2.213. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 23 % · Remis 20 % · Auswärtssieg 57 % · BTTS Ja 66 % · Over 2,5 69 % · Under 2,5 31 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 4.62 · X 4.5 · 2 1.52 · BTTS Ja 1.38 · Over 2,5 1.31 · Under 2,5 3.26.

**Auswahl:** Over 2,5

---

## 4.4 Feyenoord – Inter Milan | 2026-11-03 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700596

Analyse-ID: A-20261103-8700596-r1 · Team-IDs: 367 / 470 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Stadion Feijenoord · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-09 bis 2026-10-21, Gast 2026-09-08 bis 2026-10-21; letzte 6: Heim 2026-09-09–2026-10-21, Gast 2026-09-08–2026-10-21.

**Feyenoord (Heim, ID 367)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 3 | 1 | 4
Gegentore | 8 | 2 | 6 | 8
Tore/Spiel | 1.33 | 3.00 | 0.50 | 1.33
Gegentore/Spiel | 2.67 | 2.00 | 3.00 | 2.67
xG für/Spiel | 1.09 | 1.44 | 0.91 | 1.09
xG gegen/Spiel | 2.15 | 1.28 | 2.58 | 2.15
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 1/0/0 | 0/0/2 | 1/0/2
Punkte/Spiel | 1.00 | 3.00 | 0.00 | 1.00
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Inter Milan (Gast, ID 470)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 5 | 4 | 1 | 5
Gegentore | 6 | 4 | 2 | 6
Tore/Spiel | 1.67 | 2.00 | 1.00 | 1.67
Gegentore/Spiel | 2.00 | 2.00 | 2.00 | 2.00
xG für/Spiel | 2.36 | 2.30 | 2.48 | 2.36
xG gegen/Spiel | 1.78 | 1.75 | 1.85 | 1.78
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/0/2 | 1/0/1 | 0/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 1.50 | 0.00 | 1.00
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 67 % | 50 % | 100 % | 67 %
Under 2,5 % | 33 % | 50 % | 0 % | 33 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 67 % | 50 % | 100 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Feyenoord – Landesliga (Saison-ID 17097, 2026-08-09 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 33 | 12 | 21 | 20
Gegentore | 12 | 5 | 7 | 5
Tore/Spiel | 3.00 | 2.40 | 3.50 | 3.33
Gegentore/Spiel | 1.09 | 1.00 | 1.17 | 0.83
xG für/Spiel | 2.25 | 2.45 | 2.08 | 2.24
xG gegen/Spiel | 1.27 | 1.06 | 1.46 | 1.37
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 7/4/0 | 2/3/0 | 5/1/0 | 4/2/0
Punkte/Spiel | 2.27 | 1.80 | 2.67 | 2.33
BTTS % | 64 % | 60 % | 67 % | 50 %
Over 2,5 % | 64 % | 60 % | 67 % | 50 %
Under 2,5 % | 36 % | 40 % | 33 % | 50 %
Clean Sheets % | 36 % | 40 % | 33 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Inter Milan – Landesliga (Saison-ID 17084, 2026-08-22 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 26 | 17 | 9 | 13
Gegentore | 13 | 7 | 6 | 7
Tore/Spiel | 2.60 | 3.40 | 1.80 | 2.17
Gegentore/Spiel | 1.30 | 1.40 | 1.20 | 1.17
xG für/Spiel | 2.35 | 2.61 | 2.10 | 2.20
xG gegen/Spiel | 1.12 | 1.02 | 1.22 | 1.15
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 8/1/1 | 5/0/0 | 3/1/1 | 4/1/1
Punkte/Spiel | 2.50 | 3.00 | 2.00 | 2.17
BTTS % | 70 % | 80 % | 60 % | 67 %
Over 2,5 % | 80 % | 100 % | 60 % | 83 %
Under 2,5 % | 20 % | 0 % | 40 % | 17 %
Clean Sheets % | 30 % | 20 % | 40 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 10 % | 0 % | 20 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Feyenoord: 09.09. A FC Barcelona (2.00 PPG) 1:5 · 14.10. H Como (2.00 PPG) 3:2 · 21.10. A Real Betis (3.00 PPG) 0:1

Letzte 6 Inter Milan: 08.09. A Real Madrid (3.00 PPG) 1:2 · 13.10. H Club Brugge (2.00 PPG) 3:4 · 21.10. H Shakhtar Donetsk (1.33 PPG) 1:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Feyenoord [1, 3, 0]; Inter Milan [1, 3, 1]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Feyenoord mit 1,09 xG in der Champions League und einem torlosen Spiel bei Betis, gegen Inter mit 1,12 xG gegen in der Serie A; ein Weg zu drei Toren ist mit je 67 % Over in drei Champions-League-Spielen unsicher; stärkstes Gegenargument gegen den Modell-Auswärtssieg (43 %) ist Inters Champions-League-Bilanz von 1-0-2, und gegen BTTS spricht Feyenoords schwacher Chancenwert auf diesem Niveau, der den Heimtreffer wesentlich gefährdet, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.334, λ Gast 1.584. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 32 % · Remis 24 % · Auswärtssieg 43 % · BTTS Ja 59 % · Over 2,5 56 % · Under 2,5 44 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.7 · X 4.2 · 2 1.88 · BTTS Ja 1.4 · Over 2,5 1.41 · Under 2,5 2.7.

**Auswahl:** keine – Grund siehe Bild.

---

## 4.5 LASK Linz – Slovan Bratislava | 2026-11-03 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 4 | Match-ID 8700709

Analyse-ID: A-20261103-8700709-r1 · Team-IDs: 595 / 982 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Raiffeisen Arena · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Slovan Bratislava (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-08 bis 2026-10-21, Gast 2026-09-09 bis 2026-10-20; letzte 6: Heim 2026-09-08–2026-10-21, Gast 2026-09-09–2026-10-20.

**LASK Linz (Heim, ID 595)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 6 | 3 | 3 | 6
Gegentore | 9 | 6 | 3 | 9
Tore/Spiel | 2.00 | 3.00 | 1.50 | 2.00
Gegentore/Spiel | 3.00 | 6.00 | 1.50 | 3.00
xG für/Spiel | 1.30 | 1.32 | 1.29 | 1.30
xG gegen/Spiel | 2.06 | 2.72 | 1.73 | 2.06
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 0/0/1 | 1/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 0.00 | 1.50 | 1.00
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 33 % | 100 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Slovan Bratislava (Gast, ID 982)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 1 | 0 | 1 | 1
Gegentore | 13 | 3 | 10 | 13
Tore/Spiel | 0.33 | 0.00 | 0.50 | 0.33
Gegentore/Spiel | 4.33 | 3.00 | 5.00 | 4.33
xG für/Spiel | 0.82 | 1.29 | 0.59 | 0.82
xG gegen/Spiel | 2.95 | 1.98 | 3.44 | 2.95
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 0/0/3 | 0/0/1 | 0/0/2 | 0/0/3
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 33 % | 0 % | 50 % | 33 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 67 % | 100 % | 50 % | 67 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**LASK Linz – Landesliga (Saison-ID 17181, 2026-07-31 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 26 | 13 | 13 | 11
Gegentore | 13 | 7 | 6 | 11
Tore/Spiel | 2.36 | 2.17 | 2.60 | 1.83
Gegentore/Spiel | 1.18 | 1.17 | 1.20 | 1.83
xG für/Spiel | 2.14 | 1.89 | 2.44 | 1.92
xG gegen/Spiel | 1.00 | 1.05 | 0.95 | 1.22
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 7/1/3 | 4/0/2 | 3/1/1 | 2/1/3
Punkte/Spiel | 2.00 | 2.00 | 2.00 | 1.17
BTTS % | 55 % | 50 % | 60 % | 67 %
Over 2,5 % | 82 % | 83 % | 80 % | 83 %
Under 2,5 % | 18 % | 17 % | 20 % | 17 %
Clean Sheets % | 36 % | 33 % | 40 % | 17 %
Failed to Score % | 9 % | 17 % | 0 % | 17 %
BTTS-and-lose % | 18 % | 17 % | 20 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Slovan Bratislava – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 LASK Linz: 08.09. A AEK Athens (1.00 PPG) 0:1 · 14.10. H Liverpool (3.00 PPG) 3:6 · 21.10. A Sporting CP (2.00 PPG) 3:2

Letzte 6 Slovan Bratislava: 09.09. A PSG (3.00 PPG) 1:6 · 14.10. H Stuttgart (2.33 PPG) 0:3 · 20.10. A Roma (1.33 PPG) 0:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): LASK Linz [0, 3, 3]; Slovan Bratislava [1, 0, 0]

**Bild:** Champions League 2026/27 mit je 3 Spielen ist eingeschränkt, weil die slowakische Liga im API-Abo fehlt und für Slovan keine Landesliga-Daten vorliegen; schwächere Offensive ist Slovan mit 1 Tor in 3 Champions-League-Spielen und 0,82 xG, gegen LASK; der Weg zu drei Toren läuft vor allem einseitig über LASK, weil Slovan in der Champions League 13 Gegentore in 3 Spielen (2,95 xG gegen) kassierte, LASK in der Liga 2,36 Tore pro Spiel bei 82 % Over erzielt und alle 3 Slovan-Spiele Over endeten, das Modell schätzt 80 %; stärkstes Gegenargument ist Slovans geringe Eigenbeteiligung an Toren, sodass LASK fast allein drei Tore erzielen muss, was bei den gezeigten Werten aber keine wesentliche Gefahr ist.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 3.124, λ Gast 1.192. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 76 % · Remis 13 % · Auswärtssieg 11 % · BTTS Ja 67 % · Over 2,5 80 % · Under 2,5 20 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.41 · X 5 · 2 6.85 · BTTS Ja 1.53 · Over 2,5 1.36 · Under 2,5 2.82.

**Auswahl:** Over 2,5

---
