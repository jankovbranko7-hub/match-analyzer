# Vorabeintrag Batch 3 · 05.11.2026

- System: FootyStats-System v1.4 (Fassung v1.4-2026-11-05)
- Modell: Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-05 09:51 UTC
- Eintrag erstellt: 2026-11-05 09:56:12 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei Europapokal-Wettbewerben: nur Liga- bzw. Gruppenphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 3.1 Sparta Praha – AFC Bournemouth | 2026-11-05 17:45 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700999

Analyse-ID: A-20261105-8700999-r1 · Team-IDs: 86 / 148 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: TC Strahov · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Sparta Praha (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-17–2026-10-22.

**Sparta Praha (Heim, ID 86)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 5 | 1 | 4 | 5
Gegentore | 3 | 1 | 2 | 3
Tore/Spiel | 1.67 | 1.00 | 2.00 | 1.67
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 1.87 | 1.91 | 1.85 | 1.87
xG gegen/Spiel | 1.28 | 0.68 | 1.57 | 1.28
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 0/1/0 | 1/0/1 | 1/1/1
Punkte/Spiel | 1.33 | 1.00 | 1.50 | 1.33
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 33 % | 0 % | 50 % | 33 %
Under 2,5 % | 67 % | 100 % | 50 % | 67 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**AFC Bournemouth (Gast, ID 148)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 8 | 6 | 2 | 8
Gegentore | 1 | 0 | 1 | 1
Tore/Spiel | 2.67 | 3.00 | 2.00 | 2.67
Gegentore/Spiel | 0.33 | 0.00 | 1.00 | 0.33
xG für/Spiel | 1.93 | 2.29 | 1.21 | 1.93
xG gegen/Spiel | 0.95 | 0.54 | 1.77 | 0.95
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 3/0/0 | 2/0/0 | 1/0/0 | 3/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 33 % | 0 % | 100 % | 33 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 67 % | 100 % | 0 % | 67 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Sparta Praha – Landesliga:** fehlt (Liga nicht im API-Abo)

**AFC Bournemouth – Landesliga (Saison-ID 17146, 2026-08-23 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 14 | 7 | 7 | 10
Gegentore | 13 | 4 | 9 | 8
Tore/Spiel | 1.56 | 1.40 | 1.75 | 1.67
Gegentore/Spiel | 1.44 | 0.80 | 2.25 | 1.33
xG für/Spiel | 1.57 | 1.84 | 1.23 | 1.67
xG gegen/Spiel | 1.24 | 1.07 | 1.46 | 1.14
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 3/3/3 | 2/2/1 | 1/1/2 | 3/1/2
Punkte/Spiel | 1.33 | 1.60 | 1.00 | 1.67
BTTS % | 56 % | 40 % | 75 % | 33 %
Over 2,5 % | 56 % | 20 % | 100 % | 50 %
Under 2,5 % | 44 % | 80 % | 0 % | 50 %
Clean Sheets % | 33 % | 40 % | 25 % | 50 %
Failed to Score % | 11 % | 20 % | 0 % | 17 %
BTTS-and-lose % | 22 % | 0 % | 50 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Sparta Praha: 16.09. A FC Avan Academy (0.00 PPG) 4:1 · 15.10. H Lillestrøm (0.33 PPG) 1:1 · 22.10. A Olympiakos Piraeus (2.50 PPG) 0:1

Letzte 6 AFC Bournemouth: 17.09. A Real Sociedad (1.33 PPG) 2:1 · 15.10. H Sturm Graz (1.33 PPG) 3:0 · 22.10. H AC Milan (1.00 PPG) 3:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Sparta Praha [4, 1, 0]; AFC Bournemouth [2, 3, 3]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Sparta Prag im API-Abo fehlt; schwächere Offensive ist Sparta mit 5 Toren in 3 Europa-League-Spielen, gegen Bournemouth mit 67 % Clean Sheets in diesem Wettbewerb; ein Weg zu drei Toren ist mit Bournemouths 3 Over-Spielen sichtbar, aber gegen Spartas 33 % Over unsicher; stärkstes Gegenargument gegen den Auswärtssieg ist das Modell mit nur 33 % bei fehlender Ligabasis für Sparta und Bournemouths Premier-League-Auswärtsbilanz von 1-1-2, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.478, λ Gast 1.304; xG-Variante λ Heim 1.507, λ Gast 1.264 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 41 % · Remis 25 % · Auswärtssieg 33 % · BTTS Ja 56 % · Over 2,5 52 % · Under 2,5 48 % (nur Tormodell: BTTS 56 %, Over 2,5 53 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 6.25 · X 4.5 · 2 1.53 · BTTS Ja 1.65 · Over 2,5 1.57 · Under 2,5 2.37.

**Markt:** Heim 15 % · Remis 21 % · Auswärts 63 % · BTTS 57 % · Over 60 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 3.2 Sturm Graz – Celje | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700883

Analyse-ID: A-20261105-8700883-r1 · Team-IDs: 582 / 1970 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Merkur Arena · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Celje (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-16 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-16–2026-10-22.

**Sturm Graz (Heim, ID 582)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 1 | 1 | 0 | 1
Gegentore | 3 | 0 | 3 | 3
Tore/Spiel | 0.33 | 0.50 | 0.00 | 0.33
Gegentore/Spiel | 1.00 | 0.00 | 3.00 | 1.00
xG für/Spiel | 1.18 | 1.41 | 0.73 | 1.18
xG gegen/Spiel | 1.95 | 1.77 | 2.31 | 1.95
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/1/1 | 1/1/0 | 0/0/1 | 1/1/1
Punkte/Spiel | 1.33 | 2.00 | 0.00 | 1.33
BTTS % | 0 % | 0 % | 0 % | 0 %
Over 2,5 % | 33 % | 0 % | 100 % | 33 %
Under 2,5 % | 67 % | 100 % | 0 % | 67 %
Clean Sheets % | 67 % | 100 % | 0 % | 67 %
Failed to Score % | 67 % | 50 % | 100 % | 67 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Celje (Gast, ID 1970)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 2 | 2 | 0 | 2
Gegentore | 7 | 5 | 2 | 7
Tore/Spiel | 0.67 | 1.00 | 0.00 | 0.67
Gegentore/Spiel | 2.33 | 2.50 | 2.00 | 2.33
xG für/Spiel | 1.05 | 1.20 | 0.74 | 1.05
xG gegen/Spiel | 1.73 | 1.55 | 2.09 | 1.73
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 0/1/2 | 0/1/1 | 0/0/1 | 0/1/2
Punkte/Spiel | 0.33 | 0.50 | 0.00 | 0.33
BTTS % | 33 % | 50 % | 0 % | 33 %
Over 2,5 % | 67 % | 100 % | 0 % | 67 %
Under 2,5 % | 33 % | 0 % | 100 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 67 % | 50 % | 100 % | 67 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Sturm Graz – Landesliga (Saison-ID 17181, 2026-08-01 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 19 | 12 | 7 | 13
Gegentore | 13 | 5 | 8 | 8
Tore/Spiel | 1.73 | 2.40 | 1.17 | 2.17
Gegentore/Spiel | 1.18 | 1.00 | 1.33 | 1.33
xG für/Spiel | 1.87 | 2.02 | 1.74 | 1.89
xG gegen/Spiel | 1.38 | 1.56 | 1.22 | 1.47
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 5/4/2 | 3/2/0 | 2/2/2 | 3/2/1
Punkte/Spiel | 1.73 | 2.20 | 1.33 | 1.83
BTTS % | 64 % | 80 % | 50 % | 67 %
Over 2,5 % | 45 % | 60 % | 33 % | 67 %
Under 2,5 % | 55 % | 40 % | 67 % | 33 %
Clean Sheets % | 27 % | 20 % | 33 % | 17 %
Failed to Score % | 9 % | 0 % | 17 % | 17 %
BTTS-and-lose % | 9 % | 0 % | 17 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Celje – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 Sturm Graz: 16.09. H Rennes (1.50 PPG) 0:0 · 15.10. A AFC Bournemouth (3.00 PPG) 0:3 · 22.10. H Olympique Marseille (0.00 PPG) 1:0

Letzte 6 Celje: 16.09. A Bayer Leverkusen (3.00 PPG) 0:2 · 15.10. H Omonia Nicosia (2.00 PPG) 0:3 · 22.10. H Salzburg (1.33 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Sturm Graz [0, 0, 1]; Celje [0, 0, 2]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Celje im API-Abo fehlt; schwächere Offensive ist Sturm in der Europa League mit 1 Tor in 3 Spielen trotz Liga-Heimstärke (3-2-0), gegen Celje ohne Clean Sheet; ein Weg zu drei Toren ist mit Sturms Europa-League-Spielen (0, 3 und 1 Tor) unsicher; stärkstes Gegenargument gegen den Heimsieg ist das Modell mit nur 41 % bei Sturms Torarmut in diesem Wettbewerb und fehlender Ligabasis für Celje, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.270, λ Gast 1.068; xG-Variante λ Heim 1.420, λ Gast 1.268 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 41 % · Remis 28 % · Auswärtssieg 31 % · BTTS Ja 54 % · Over 2,5 50 % · Under 2,5 50 % (nur Tormodell: BTTS 47 %, Over 2,5 41 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.53 · X 4.4 · 2 5.45 · BTTS Ja 1.67 · Over 2,5 1.53 · Under 2,5 2.37.

**Markt:** Heim 61 % · Remis 21 % · Auswärts 17 % · BTTS 57 % · Over 61 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 3.3 AZ – Juventus | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700948

Analyse-ID: A-20261105-8700948-r1 · Team-IDs: 378 / 90 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: AFAS Stadion · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-17–2026-10-22.

**AZ (Heim, ID 378)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 6 | 2 | 4 | 6
Gegentore | 2 | 1 | 1 | 2
Tore/Spiel | 2.00 | 2.00 | 2.00 | 2.00
Gegentore/Spiel | 0.67 | 1.00 | 0.50 | 0.67
xG für/Spiel | 1.70 | 1.84 | 1.63 | 1.70
xG gegen/Spiel | 1.27 | 0.88 | 1.46 | 1.27
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 2/0/1 | 1/0/0 | 1/0/1 | 2/0/1
Punkte/Spiel | 2.00 | 3.00 | 1.50 | 2.00
BTTS % | 33 % | 100 % | 0 % | 33 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 33 % | 0 % | 50 % | 33 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Juventus (Gast, ID 90)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 9 | 7 | 2 | 9
Gegentore | 3 | 2 | 1 | 3
Tore/Spiel | 3.00 | 3.50 | 2.00 | 3.00
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 1.71 | 1.44 | 2.26 | 1.71
xG gegen/Spiel | 1.22 | 1.34 | 0.97 | 1.22
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 2/1/0 | 1/1/0 | 1/0/0 | 2/1/0
Punkte/Spiel | 2.33 | 2.00 | 3.00 | 2.33
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**AZ – Landesliga (Saison-ID 17097, 2026-08-08 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 20 | 9 | 11 | 4
Gegentore | 13 | 5 | 8 | 8
Tore/Spiel | 1.82 | 1.80 | 1.83 | 0.67
Gegentore/Spiel | 1.18 | 1.00 | 1.33 | 1.33
xG für/Spiel | 2.01 | 1.95 | 2.06 | 1.76
xG gegen/Spiel | 1.07 | 1.01 | 1.12 | 1.13
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 6/2/3 | 3/1/1 | 3/1/2 | 1/2/3
Punkte/Spiel | 1.82 | 2.00 | 1.67 | 0.83
BTTS % | 45 % | 40 % | 50 % | 33 %
Over 2,5 % | 36 % | 20 % | 50 % | 17 %
Under 2,5 % | 64 % | 80 % | 50 % | 83 %
Clean Sheets % | 27 % | 40 % | 17 % | 17 %
Failed to Score % | 27 % | 20 % | 33 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Juventus – Landesliga (Saison-ID 17084, 2026-08-23 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 13 | 7 | 6 | 7
Gegentore | 10 | 4 | 6 | 6
Tore/Spiel | 1.30 | 1.40 | 1.20 | 1.17
Gegentore/Spiel | 1.00 | 0.80 | 1.20 | 1.00
xG für/Spiel | 1.81 | 1.63 | 1.99 | 1.73
xG gegen/Spiel | 0.99 | 0.82 | 1.16 | 1.08
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 5/2/3 | 3/1/1 | 2/1/2 | 3/1/2
Punkte/Spiel | 1.70 | 2.00 | 1.40 | 1.67
BTTS % | 30 % | 20 % | 40 % | 17 %
Over 2,5 % | 20 % | 20 % | 20 % | 17 %
Under 2,5 % | 80 % | 80 % | 80 % | 83 %
Clean Sheets % | 50 % | 60 % | 40 % | 50 %
Failed to Score % | 20 % | 20 % | 20 % | 33 %
BTTS-and-lose % | 10 % | 0 % | 20 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 AZ: 16.09. A Sunderland (2.33 PPG) 0:1 · 15.10. H Hapoel Be'er Sheva (0.33 PPG) 2:1 · 22.10. A FC Avan Academy (0.00 PPG) 4:0

Letzte 6 Juventus: 17.09. H NEC (1.33 PPG) 5:0 · 15.10. A Celta de Vigo (1.00 PPG) 2:1 · 22.10. H Rennes (1.50 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): AZ [0, 2, 4]; Juventus [5, 2, 2]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist AZ mit 4 Toren in den letzten sechs Eredivisie-Spielen, gegen Juventus mit 50 % Serie-A-Clean-Sheets; der Weg zu drei Toren ist widersprüchlich, weil die Ligaspiele beider Teams überwiegend Under (AZ daheim 20 %, Juventus auswärts 20 % Over), alle drei Juventus-Spiele in der Europa League aber Over endeten; stärkstes Gegenargument gegen den Auswärtssieg ist das Modell mit nur 32 % bei Juventus' Liga-Auswärtsbilanz von 2-1-2, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.704, λ Gast 1.410; xG-Variante λ Heim 1.478, λ Gast 1.230 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 45 % · Remis 24 % · Auswärtssieg 32 % · BTTS Ja 55 % · Over 2,5 51 % · Under 2,5 49 % (nur Tormodell: BTTS 62 %, Over 2,5 60 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.4 · X 3.6 · 2 2.05 · BTTS Ja 1.73 · Over 2,5 1.81 · Under 2,5 2.

**Markt:** Heim 28 % · Remis 26 % · Auswärts 46 % · BTTS 55 % · Over 52 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 3.4 Sunderland – Dinamo Zagreb | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700881

Analyse-ID: A-20261105-8700881-r1 · Team-IDs: 156 / 122 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Stadium of Light · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Dinamo Zagreb (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-16 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-16–2026-10-22.

**Sunderland (Heim, ID 156)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 1 | 3 | 4
Gegentore | 2 | 0 | 2 | 2
Tore/Spiel | 1.33 | 1.00 | 1.50 | 1.33
Gegentore/Spiel | 0.67 | 0.00 | 1.00 | 0.67
xG für/Spiel | 2.38 | 1.95 | 2.59 | 2.38
xG gegen/Spiel | 1.05 | 1.19 | 0.99 | 1.05
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 2/1/0 | 1/0/0 | 1/1/0 | 2/1/0
Punkte/Spiel | 2.33 | 3.00 | 2.00 | 2.33
BTTS % | 67 % | 0 % | 100 % | 67 %
Over 2,5 % | 33 % | 0 % | 50 % | 33 %
Under 2,5 % | 67 % | 100 % | 50 % | 67 %
Clean Sheets % | 33 % | 100 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Dinamo Zagreb (Gast, ID 122)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 3 | 3 | 0 | 3
Gegentore | 4 | 4 | 0 | 4
Tore/Spiel | 1.00 | 1.50 | 0.00 | 1.00
Gegentore/Spiel | 1.33 | 2.00 | 0.00 | 1.33
xG für/Spiel | 1.42 | 1.75 | 0.76 | 1.42
xG gegen/Spiel | 1.57 | 1.50 | 1.70 | 1.57
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/1/1 | 1/0/1 | 0/1/0 | 1/1/1
Punkte/Spiel | 1.33 | 1.50 | 1.00 | 1.33
BTTS % | 33 % | 50 % | 0 % | 33 %
Over 2,5 % | 33 % | 50 % | 0 % | 33 %
Under 2,5 % | 67 % | 50 % | 100 % | 67 %
Clean Sheets % | 67 % | 50 % | 100 % | 67 %
Failed to Score % | 33 % | 0 % | 100 % | 33 %
BTTS-and-lose % | 33 % | 50 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Sunderland – Landesliga (Saison-ID 17146, 2026-08-22 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 7 | 1 | 6 | 4
Gegentore | 17 | 4 | 13 | 14
Tore/Spiel | 0.78 | 0.25 | 1.20 | 0.67
Gegentore/Spiel | 1.89 | 1.00 | 2.60 | 2.33
xG für/Spiel | 1.40 | 1.41 | 1.39 | 1.39
xG gegen/Spiel | 1.49 | 1.29 | 1.65 | 1.64
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 1/2/6 | 1/1/2 | 0/1/4 | 0/1/5
Punkte/Spiel | 0.56 | 1.00 | 0.20 | 0.17
BTTS % | 44 % | 0 % | 80 % | 33 %
Over 2,5 % | 33 % | 0 % | 60 % | 33 %
Under 2,5 % | 67 % | 100 % | 40 % | 67 %
Clean Sheets % | 22 % | 50 % | 0 % | 17 %
Failed to Score % | 44 % | 75 % | 20 % | 67 %
BTTS-and-lose % | 33 % | 0 % | 60 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Dinamo Zagreb – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 Sunderland: 16.09. H AZ (2.00 PPG) 1:0 · 15.10. A Torreense (1.00 PPG) 2:1 · 22.10. A Lech Poznań (0.33 PPG) 1:1

Letzte 6 Dinamo Zagreb: 16.09. A Hapoel Be'er Sheva (0.33 PPG) 0:0 · 15.10. H RSC Anderlecht (1.00 PPG) 1:0 · 22.10. H NEC (1.33 PPG) 2:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Sunderland [1, 2, 1]; Dinamo Zagreb [0, 1, 2]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Dinamo Zagreb im API-Abo fehlt; schwächere Offensive ist Sunderland mit 1 Tor in 4 Premier-League-Heimspielen, das in der Europa League aber 4 Tore in 3 Spielen erzielte; ein Weg zu drei Toren ist mit Sunderlands 0 % Over daheim in der Liga schwach, aber Dinamos 2:4 gegen NEC zeigt Gegenbeispiele; stärkstes Gegenargument gegen den Heimsieg (Modell 56 %) ist Sunderlands Ligaform mit 0-1-5 bei fehlender Ligabasis für Dinamo, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.855, λ Gast 1.068; xG-Variante λ Heim 1.724, λ Gast 1.132 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 56 % · Remis 23 % · Auswärtssieg 22 % · BTTS Ja 56 % · Over 2,5 54 % · Under 2,5 46 % (nur Tormodell: BTTS 55 %, Over 2,5 56 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.46 · X 4.7 · 2 6.8 · BTTS Ja 1.75 · Over 2,5 1.68 · Under 2,5 2.2.

**Markt:** Heim 66 % · Remis 20 % · Auswärts 14 % · BTTS 53 % · Over 57 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 3.5 Bayer Leverkusen – Olympique Marseille | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700977

Analyse-ID: A-20261105-8700977-r1 · Team-IDs: 40 / 443 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: BayArena · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-17–2026-10-22.

**Bayer Leverkusen (Heim, ID 40)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 8 | 2 | 6 | 8
Gegentore | 0 | 0 | 0 | 0
Tore/Spiel | 2.67 | 2.00 | 3.00 | 2.67
Gegentore/Spiel | 0.00 | 0.00 | 0.00 | 0.00
xG für/Spiel | 2.71 | 2.09 | 3.03 | 2.71
xG gegen/Spiel | 0.83 | 0.74 | 0.88 | 0.83
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 3/0/0 | 1/0/0 | 2/0/0 | 3/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 0 % | 0 % | 0 % | 0 %
Over 2,5 % | 33 % | 0 % | 50 % | 33 %
Under 2,5 % | 67 % | 100 % | 50 % | 67 %
Clean Sheets % | 100 % | 100 % | 100 % | 100 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Olympique Marseille (Gast, ID 443)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 1 | 0 | 1 | 1
Gegentore | 6 | 1 | 5 | 6
Tore/Spiel | 0.33 | 0.00 | 0.50 | 0.33
Gegentore/Spiel | 2.00 | 1.00 | 2.50 | 2.00
xG für/Spiel | 1.40 | 1.48 | 1.36 | 1.40
xG gegen/Spiel | 1.45 | 1.02 | 1.67 | 1.45
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 0/0/3 | 0/0/1 | 0/0/2 | 0/0/3
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 33 % | 0 % | 50 % | 33 %
Over 2,5 % | 33 % | 0 % | 50 % | 33 %
Under 2,5 % | 67 % | 100 % | 50 % | 67 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 67 % | 100 % | 50 % | 67 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Bayer Leverkusen – Landesliga (Saison-ID 17210, 2026-08-29 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 18 | 10 | 8 | 12
Gegentore | 16 | 5 | 11 | 13
Tore/Spiel | 2.25 | 2.50 | 2.00 | 2.00
Gegentore/Spiel | 2.00 | 1.25 | 2.75 | 2.17
xG für/Spiel | 2.01 | 2.09 | 1.92 | 1.91
xG gegen/Spiel | 1.42 | 1.18 | 1.65 | 1.56
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 4/1/3 | 3/0/1 | 1/1/2 | 3/1/2
Punkte/Spiel | 1.62 | 2.25 | 1.00 | 1.67
BTTS % | 62 % | 50 % | 75 % | 67 %
Over 2,5 % | 88 % | 75 % | 100 % | 83 %
Under 2,5 % | 12 % | 25 % | 0 % | 17 %
Clean Sheets % | 25 % | 50 % | 0 % | 17 %
Failed to Score % | 12 % | 0 % | 25 % | 17 %
BTTS-and-lose % | 25 % | 25 % | 25 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Olympique Marseille – Landesliga (Saison-ID 17102, 2026-08-21 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 20 | 13 | 7 | 14
Gegentore | 13 | 8 | 5 | 8
Tore/Spiel | 2.22 | 2.60 | 1.75 | 2.33
Gegentore/Spiel | 1.44 | 1.60 | 1.25 | 1.33
xG für/Spiel | 1.55 | 1.55 | 1.56 | 1.49
xG gegen/Spiel | 1.79 | 2.00 | 1.54 | 2.06
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 5/0/4 | 3/0/2 | 2/0/2 | 4/0/2
Punkte/Spiel | 1.67 | 1.80 | 1.50 | 2.00
BTTS % | 44 % | 60 % | 25 % | 50 %
Over 2,5 % | 56 % | 80 % | 25 % | 50 %
Under 2,5 % | 44 % | 20 % | 75 % | 50 %
Clean Sheets % | 33 % | 40 % | 25 % | 33 %
Failed to Score % | 22 % | 0 % | 50 % | 17 %
BTTS-and-lose % | 22 % | 40 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Bayer Leverkusen: 16.09. H Celje (0.33 PPG) 2:0 · 15.10. A Lech Poznań (0.33 PPG) 4:0 · 22.10. A OFI (1.00 PPG) 2:0

Letzte 6 Olympique Marseille: 17.09. A Beşiktaş (2.33 PPG) 1:4 · 15.10. H Olympiakos Piraeus (2.50 PPG) 0:1 · 22.10. A Sturm Graz (1.33 PPG) 0:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Bayer Leverkusen [2, 4, 2]; Olympique Marseille [1, 0, 0]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Marseille mit 1 Tor in 3 Europa-League-Spielen und 50 % torlosen Liga-Auswärtsspielen, gegen Leverkusen ohne Gegentor in der Europa League; der Weg zu drei Toren hängt vor allem an Leverkusen (8 Europa-League-Tore) und wird nicht gewählt; stärkstes Gegenargument ist Leverkusens Liga-Abwehr mit 16 Gegentoren in 8 Spielen, die gegen Marseilles 0-0-3 in der Europa League den Heimsieg (Modell 70 %) aber nicht entkräftet.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 2.492, λ Gast 0.984; xG-Variante λ Heim 1.763, λ Gast 1.129 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 70 % · Remis 17 % · Auswärtssieg 13 % · BTTS Ja 56 % · Over 2,5 55 % · Under 2,5 45 % (nur Tormodell: BTTS 57 %, Over 2,5 67 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.25 · X 5.4 · 2 7.7 · BTTS Ja 1.63 · Over 2,5 1.4 · Under 2,5 2.77.

**Markt:** margenbereinigt 72 % für Heimsieg; Modell 70 %; Abweichung Modell − Markt -1 Prozentpunkte.

**Auswahl:** Heimsieg

---
