# Vorabeintrag Batch 5 · 05.11.2026

- System: FootyStats-System v1.4 (Fassung v1.4-2026-11-05)
- Modell: Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-05 09:51 UTC
- Eintrag erstellt: 2026-11-05 09:56:12 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei Europapokal-Wettbewerben: nur Liga- bzw. Gruppenphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 5.1 Trabzonspor – Freiburg | 2026-11-05 17:45 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701007

Analyse-ID: A-20261105-8701007-r1 · Team-IDs: 185 / 42 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: Medical Park Stadyumu · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Trabzonspor (Heim, ID 185)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 6 | 2 | 4 | 6
Gegentore | 2 | 0 | 2 | 2
Tore/Spiel | 3.00 | 2.00 | 4.00 | 3.00
Gegentore/Spiel | 1.00 | 0.00 | 2.00 | 1.00
xG für/Spiel | 1.79 | 1.40 | 2.18 | 1.79
xG gegen/Spiel | 1.37 | 0.90 | 1.84 | 1.37
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 2/0/0 | 1/0/0 | 1/0/0 | 2/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 50 % | 0 % | 100 % | 50 %
Over 2,5 % | 50 % | 0 % | 100 % | 50 %
Under 2,5 % | 50 % | 100 % | 0 % | 50 %
Clean Sheets % | 50 % | 100 % | 0 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Freiburg (Gast, ID 42)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 3 | 3 | 0 | 3
Gegentore | 5 | 2 | 3 | 5
Tore/Spiel | 1.50 | 3.00 | 0.00 | 1.50
Gegentore/Spiel | 2.50 | 2.00 | 3.00 | 2.50
xG für/Spiel | 1.88 | 2.55 | 1.20 | 1.88
xG gegen/Spiel | 1.25 | 1.02 | 1.49 | 1.25
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 1/0/1 | 1/0/0 | 0/0/1 | 1/0/1
Punkte/Spiel | 1.50 | 3.00 | 0.00 | 1.50
BTTS % | 50 % | 100 % | 0 % | 50 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 50 % | 0 % | 100 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Trabzonspor – Landesliga (Saison-ID 17265, 2026-08-15 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 24 | 15 | 9 | 15
Gegentore | 8 | 1 | 7 | 4
Tore/Spiel | 2.40 | 3.00 | 1.80 | 2.50
Gegentore/Spiel | 0.80 | 0.20 | 1.40 | 0.67
xG für/Spiel | 1.66 | 1.80 | 1.51 | 1.53
xG gegen/Spiel | 1.58 | 1.60 | 1.56 | 1.67
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 7/1/2 | 5/0/0 | 2/1/2 | 5/0/1
Punkte/Spiel | 2.20 | 3.00 | 1.40 | 2.50
BTTS % | 40 % | 20 % | 60 % | 17 %
Over 2,5 % | 60 % | 60 % | 60 % | 50 %
Under 2,5 % | 40 % | 40 % | 40 % | 50 %
Clean Sheets % | 50 % | 80 % | 20 % | 67 %
Failed to Score % | 10 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 10 % | 0 % | 20 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Freiburg – Landesliga (Saison-ID 17210, 2026-08-30 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 18 | 12 | 6 | 13
Gegentore | 10 | 5 | 5 | 9
Tore/Spiel | 2.25 | 3.00 | 1.50 | 2.17
Gegentore/Spiel | 1.25 | 1.25 | 1.25 | 1.50
xG für/Spiel | 1.58 | 1.68 | 1.48 | 1.52
xG gegen/Spiel | 1.21 | 1.06 | 1.36 | 1.19
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 5/1/2 | 3/0/1 | 2/1/1 | 3/1/2
Punkte/Spiel | 2.00 | 2.25 | 1.75 | 1.67
BTTS % | 75 % | 75 % | 75 % | 83 %
Over 2,5 % | 88 % | 100 % | 75 % | 100 %
Under 2,5 % | 12 % | 0 % | 25 % | 0 %
Clean Sheets % | 25 % | 25 % | 25 % | 17 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 25 % | 25 % | 25 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Trabzonspor: 15.10. A KuPS (0.00 PPG) 4:2 · 22.10. H Hearts (0.50 PPG) 2:0

Letzte 6 Freiburg: 15.10. H Jablonec (0.50 PPG) 3:2 · 22.10. A Monaco (3.00 PPG) 0:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Trabzonspor [4, 2]; Freiburg [3, 0]

**Bild:** Conference League 2026/27 mit je 2 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Freiburg mit 3 Toren in 2 Conference-League-Spielen, das in der Bundesliga aber in jedem Spiel traf, gegen Trabzonspor mit 80 % Clean Sheets in der Liga daheim; ein Weg zu drei Toren ist widersprüchlich (Freiburg 88 % Over in der Bundesliga, Trabzonspor daheim 60 %); stärkstes Gegenargument ist der ungeklärte Widerspruch zwischen Trabzonspors Heimstärke und Freiburgs Ligaform (5-1-2), bei dem auch das Modell stark vom Markt abweicht (Heimsieg 62 % zu 40 %), sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 2.117, λ Gast 1.050; xG-Variante λ Heim 1.568, λ Gast 1.208 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 62 % · Remis 20 % · Auswärtssieg 18 % · BTTS Ja 56 % · Over 2,5 52 % · Under 2,5 48 % (nur Tormodell: BTTS 57 %, Over 2,5 61 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.26 · X 3.6 · 2 2.66 · BTTS Ja 1.4 · Over 2,5 1.5 · Under 2,5 2.5.

**Markt:** Heim 40 % · Remis 25 % · Auswärts 34 % · BTTS 65 % · Over 62 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 5.2 Lincoln Red Imps – Hajduk Split | 2026-11-05 17:45 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701030

Analyse-ID: A-20261105-8701030-r1 · Team-IDs: 103 / 1863 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: Victoria Stadium · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Lincoln Red Imps, Hajduk Split (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Lincoln Red Imps (Heim, ID 103)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 2 | 1 | 1 | 2
Gegentore | 6 | 4 | 2 | 6
Tore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
Gegentore/Spiel | 3.00 | 4.00 | 2.00 | 3.00
xG für/Spiel | 0.66 | 0.58 | 0.74 | 0.66
xG gegen/Spiel | 2.81 | 2.90 | 2.72 | 2.81
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/0/2 | 0/0/1 | 0/0/1 | 0/0/2
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 100 % | 100 % | 100 % | 100 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Hajduk Split (Gast, ID 1863)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 3 | 2 | 1 | 3
Gegentore | 1 | 1 | 0 | 1
Tore/Spiel | 1.50 | 2.00 | 1.00 | 1.50
Gegentore/Spiel | 0.50 | 1.00 | 0.00 | 0.50
xG für/Spiel | 1.47 | 1.75 | 1.19 | 1.47
xG gegen/Spiel | 1.46 | 1.47 | 1.45 | 1.46
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 2/0/0 | 1/0/0 | 1/0/0 | 2/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 50 % | 100 % | 0 % | 50 %
Over 2,5 % | 50 % | 100 % | 0 % | 50 %
Under 2,5 % | 50 % | 0 % | 100 % | 50 %
Clean Sheets % | 50 % | 0 % | 100 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Lincoln Red Imps – Landesliga:** fehlt (Liga nicht im API-Abo)

**Hajduk Split – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 Lincoln Red Imps: 15.10. A Brann (3.00 PPG) 1:2 · 22.10. H Twente (3.00 PPG) 1:4

Letzte 6 Hajduk Split: 15.10. H Ajax (1.50 PPG) 2:1 · 22.10. A Thun (0.00 PPG) 1:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Lincoln Red Imps [1, 1]; Hajduk Split [2, 1]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesligen von Lincoln Red Imps und Hajduk Split im API-Abo fehlen und jedes Team nur 2 Conference-League-Spiele hat; schwächere Offensive ist Lincoln mit 0,66 xG und 2 Toren in 2 Spielen, gegen Hajduk mit einem Clean Sheet; ein Weg zu drei Toren ist mit Lincolns zwei Over-Spielen sichtbar, aber nicht belastbar; stärkstes Gegenargument gegen den naheliegenden Auswärtssieg ist das Modell mit nur 37 % bei fehlender Ligabasis beider Teams, sodass die Datenbasis keinen Markt trägt.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 1.488, λ Gast 1.452; xG-Variante λ Heim 1.417, λ Gast 1.527 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 39 % · Remis 25 % · Auswärtssieg 37 % · BTTS Ja 59 % · Over 2,5 56 % · Under 2,5 44 % (nur Tormodell: BTTS 59 %, Over 2,5 56 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 6.5 · X 5 · 2 1.28 · BTTS Ja 2.1 · Over 2,5 1.72 · Under 2,5 2.14.

**Markt:** Heim 14 % · Remis 18 % · Auswärts 69 % · BTTS 45 % · Over 55 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 5.3 Thun – Hearts | 2026-11-05 17:45 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701047

Analyse-ID: A-20261105-8701047-r1 · Team-IDs: 888 / 32 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: Stockhorn Arena · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Thun (Heim, ID 888)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 0 | 0 | 0 | 0
Gegentore | 2 | 1 | 1 | 2
Tore/Spiel | 0.00 | 0.00 | 0.00 | 0.00
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 0.97 | 1.45 | 0.50 | 0.97
xG gegen/Spiel | 1.79 | 1.19 | 2.39 | 1.79
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/0/2 | 0/0/1 | 0/0/1 | 0/0/2
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 0 % | 0 % | 0 % | 0 %
Over 2,5 % | 0 % | 0 % | 0 % | 0 %
Under 2,5 % | 100 % | 100 % | 100 % | 100 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 100 % | 100 % | 100 % | 100 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Hearts (Gast, ID 32)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 1 | 1 | 0 | 1
Gegentore | 3 | 1 | 2 | 3
Tore/Spiel | 0.50 | 1.00 | 0.00 | 0.50
Gegentore/Spiel | 1.50 | 1.00 | 2.00 | 1.50
xG für/Spiel | 1.51 | 2.12 | 0.90 | 1.51
xG gegen/Spiel | 1.31 | 1.22 | 1.40 | 1.31
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/1/1 | 0/1/0 | 0/0/1 | 0/1/1
Punkte/Spiel | 0.50 | 1.00 | 0.00 | 0.50
BTTS % | 50 % | 100 % | 0 % | 50 %
Over 2,5 % | 0 % | 0 % | 0 % | 0 %
Under 2,5 % | 100 % | 100 % | 100 % | 100 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 50 % | 0 % | 100 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Thun – Landesliga (Saison-ID 17129, 2026-07-25 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 5 | 7 | 6
Tore | 24 | 4 | 20 | 13
Gegentore | 34 | 14 | 20 | 17
Tore/Spiel | 2.00 | 0.80 | 2.86 | 2.17
Gegentore/Spiel | 2.83 | 2.80 | 2.86 | 2.83
xG für/Spiel | 1.70 | 1.80 | 1.63 | 1.80
xG gegen/Spiel | 1.77 | 1.79 | 1.76 | 1.64
Spiele mit xG | 12 | 5 | 7 | 6
S/U/N | 4/1/7 | 0/1/4 | 4/0/3 | 2/0/4
Punkte/Spiel | 1.08 | 0.20 | 1.71 | 1.00
BTTS % | 75 % | 40 % | 100 % | 83 %
Over 2,5 % | 83 % | 60 % | 100 % | 83 %
Under 2,5 % | 17 % | 40 % | 0 % | 17 %
Clean Sheets % | 8 % | 20 % | 0 % | 0 %
Failed to Score % | 25 % | 60 % | 0 % | 17 %
BTTS-and-lose % | 42 % | 40 % | 43 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Hearts – Landesliga (Saison-ID 17148, 2026-08-01 bis 2026-10-28)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 24 | 15 | 9 | 12
Gegentore | 17 | 4 | 13 | 12
Tore/Spiel | 2.18 | 3.00 | 1.50 | 2.00
Gegentore/Spiel | 1.55 | 0.80 | 2.17 | 2.00
xG für/Spiel | 1.75 | 1.96 | 1.57 | 1.67
xG gegen/Spiel | 1.24 | 1.02 | 1.43 | 1.33
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 6/2/3 | 4/1/0 | 2/1/3 | 2/2/2
Punkte/Spiel | 1.82 | 2.60 | 1.17 | 1.33
BTTS % | 73 % | 60 % | 83 % | 67 %
Over 2,5 % | 82 % | 100 % | 67 % | 67 %
Under 2,5 % | 18 % | 0 % | 33 % | 33 %
Clean Sheets % | 27 % | 40 % | 17 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 27 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Thun: 15.10. A Twente (3.00 PPG) 0:1 · 22.10. H Hajduk Split (3.00 PPG) 0:1

Letzte 6 Hearts: 15.10. H Nordsjælland (1.00 PPG) 1:1 · 22.10. A Trabzonspor (3.00 PPG) 0:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Thun [0, 0]; Hearts [1, 0]

**Bild:** Conference League 2026/27 mit je 2 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Thun ohne Tor in 2 Conference-League-Spielen und mit 4 Toren in 5 Liga-Heimspielen (60 % torlos); ein Weg zu drei Toren ist mit 83 % bzw. 82 % Over in beiden Ligen sichtbar, widerspricht aber den torarmen Conference-League-Spielen beider Teams; stärkstes Gegenargument ist der ungeklärte Widerspruch zwischen dem Modell-Heimsieg (52 %) und Thuns Liga-Heimbilanz von 0-1-4, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 1.531, λ Gast 0.888; xG-Variante λ Heim 1.458, λ Gast 1.162 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 52 % · Remis 26 % · Auswärtssieg 22 % · BTTS Ja 53 % · Over 2,5 49 % · Under 2,5 51 % (nur Tormodell: BTTS 46 %, Over 2,5 44 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.32 · X 3.65 · 2 2.75 · BTTS Ja 1.44 · Over 2,5 1.53 · Under 2,5 2.4.

**Markt:** Heim 40 % · Remis 26 % · Auswärts 34 % · BTTS 65 % · Over 61 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 5.4 Midtjylland – Ajax | 2026-11-05 17:45 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701050

Analyse-ID: A-20261105-8701050-r1 · Team-IDs: 955 / 120 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: MCH Arena · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Midtjylland (Heim, ID 955)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 1 | 0 | 1 | 1
Gegentore | 2 | 1 | 1 | 2
Tore/Spiel | 0.50 | 0.00 | 1.00 | 0.50
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 1.72 | 1.81 | 1.63 | 1.72
xG gegen/Spiel | 1.70 | 2.10 | 1.30 | 1.70
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/1/1 | 0/0/1 | 0/1/0 | 0/1/1
Punkte/Spiel | 0.50 | 0.00 | 1.00 | 0.50
BTTS % | 50 % | 0 % | 100 % | 50 %
Over 2,5 % | 0 % | 0 % | 0 % | 0 %
Under 2,5 % | 100 % | 100 % | 100 % | 100 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 50 % | 100 % | 0 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Ajax (Gast, ID 120)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 3 | 2 | 1 | 3
Gegentore | 2 | 0 | 2 | 2
Tore/Spiel | 1.50 | 2.00 | 1.00 | 1.50
Gegentore/Spiel | 1.00 | 0.00 | 2.00 | 1.00
xG für/Spiel | 1.88 | 2.30 | 1.47 | 1.88
xG gegen/Spiel | 1.58 | 1.42 | 1.75 | 1.58
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 1/0/1 | 1/0/0 | 0/0/1 | 1/0/1
Punkte/Spiel | 1.50 | 3.00 | 0.00 | 1.50
BTTS % | 50 % | 0 % | 100 % | 50 %
Over 2,5 % | 50 % | 0 % | 100 % | 50 %
Under 2,5 % | 50 % | 100 % | 0 % | 50 %
Clean Sheets % | 50 % | 100 % | 0 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 50 % | 0 % | 100 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Midtjylland – Landesliga (Saison-ID 17091, 2026-07-26 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 27 | 14 | 13 | 15
Gegentore | 15 | 7 | 8 | 8
Tore/Spiel | 2.08 | 2.33 | 1.86 | 2.50
Gegentore/Spiel | 1.15 | 1.17 | 1.14 | 1.33
xG für/Spiel | 1.56 | 1.81 | 1.35 | 1.39
xG gegen/Spiel | 1.49 | 1.17 | 1.77 | 1.79
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 9/4/0 | 5/1/0 | 4/3/0 | 5/1/0
Punkte/Spiel | 2.38 | 2.67 | 2.14 | 2.67
BTTS % | 85 % | 83 % | 86 % | 100 %
Over 2,5 % | 62 % | 83 % | 43 % | 83 %
Under 2,5 % | 38 % | 17 % | 57 % | 17 %
Clean Sheets % | 15 % | 17 % | 14 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Ajax – Landesliga (Saison-ID 17097, 2026-08-09 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 30 | 12 | 18 | 16
Gegentore | 13 | 9 | 4 | 7
Tore/Spiel | 2.73 | 2.00 | 3.60 | 2.67
Gegentore/Spiel | 1.18 | 1.50 | 0.80 | 1.17
xG für/Spiel | 2.26 | 2.35 | 2.17 | 2.26
xG gegen/Spiel | 1.27 | 1.29 | 1.24 | 1.28
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 7/3/1 | 2/3/1 | 5/0/0 | 4/2/0
Punkte/Spiel | 2.18 | 1.50 | 3.00 | 2.33
BTTS % | 73 % | 83 % | 60 % | 83 %
Over 2,5 % | 73 % | 67 % | 80 % | 67 %
Under 2,5 % | 27 % | 33 % | 20 % | 33 %
Clean Sheets % | 27 % | 17 % | 40 % | 17 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 9 % | 17 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Midtjylland: 15.10. A Egnatia Rrogozhinë (1.00 PPG) 1:1 · 22.10. H Sint-Truiden (3.00 PPG) 0:1

Letzte 6 Ajax: 15.10. A Hajduk Split (3.00 PPG) 1:2 · 22.10. H Atalanta (1.50 PPG) 2:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Midtjylland [1, 0]; Ajax [1, 2]

**Bild:** Conference League 2026/27 mit je 2 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Midtjylland mit 1 Tor in 2 Conference-League-Spielen, das in der Superliga aber in allen 13 Spielen traf (daheim 14 Tore in 6) gegen Ajax mit 40 % Clean Sheets in Liga-Auswärtsspielen, während Ajax in allen Ligaspielen und in beiden Conference-League-Spielen traf (auswärts 18 Ligatore in 5) gegen Midtjylland mit nur 15 % Liga-Clean-Sheets; der Weg zu drei Toren ist mit 83 % Over in Midtjyllands Liga-Heimspielen ebenfalls plausibel, BTTS ist durch beide eigenen Torserien aber direkter belegt (Modell 57 %); stärkstes Gegenargument ist Midtjyllands torloses Conference-League-Heimspiel gegen Sint-Truiden, das als wesentliche Gefahr für den Heimtreffer gewichtet wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 1.515, λ Gast 1.039; xG-Variante λ Heim 1.606, λ Gast 1.241 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 48 % · Remis 26 % · Auswärtssieg 26 % · BTTS Ja 57 % · Over 2,5 54 % · Under 2,5 46 % (nur Tormodell: BTTS 50 %, Over 2,5 47 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.75 · X 3.6 · 2 2.4 · BTTS Ja 1.4 · Over 2,5 1.49 · Under 2,5 2.56.

**Markt:** margenbereinigt 66 % für BTTS Ja; Modell 57 %; Abweichung Modell − Markt -9 Prozentpunkte.

**Auswahl:** BTTS Ja

⚠️ Midtjylland blieb im einzigen Conference-League-Heimspiel torlos (0:1 gegen Sint-Truiden).

---

## 5.5 Red Star Belgrade – Inter Club d'Escaldes | 2026-11-05 17:45 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701095

Analyse-ID: A-20261105-8701095-r1 · Team-IDs: 70 / 3289 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: Stadion Rajko Mitić · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Inter Club d'Escaldes (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Red Star Belgrade (Heim, ID 70)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 4 | 2 | 2 | 4
Gegentore | 5 | 2 | 3 | 5
Tore/Spiel | 2.00 | 2.00 | 2.00 | 2.00
Gegentore/Spiel | 2.50 | 2.00 | 3.00 | 2.50
xG für/Spiel | 1.64 | 1.40 | 1.88 | 1.64
xG gegen/Spiel | 1.32 | 0.91 | 1.74 | 1.32
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/1/1 | 0/1/0 | 0/0/1 | 0/1/1
Punkte/Spiel | 0.50 | 1.00 | 0.00 | 0.50
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 50 % | 0 % | 100 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Inter Club d'Escaldes (Gast, ID 3289)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 1 | 1 | 0 | 1
Gegentore | 5 | 3 | 2 | 5
Tore/Spiel | 0.50 | 1.00 | 0.00 | 0.50
Gegentore/Spiel | 2.50 | 3.00 | 2.00 | 2.50
xG für/Spiel | 0.90 | 1.01 | 0.79 | 0.90
xG gegen/Spiel | 1.70 | 1.83 | 1.56 | 1.70
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/0/2 | 0/0/1 | 0/0/1 | 0/0/2
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 50 % | 100 % | 0 % | 50 %
Over 2,5 % | 50 % | 100 % | 0 % | 50 %
Under 2,5 % | 50 % | 0 % | 100 % | 50 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 50 % | 0 % | 100 % | 50 %
BTTS-and-lose % | 50 % | 100 % | 0 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Red Star Belgrade – Landesliga (Saison-ID 17119, 2026-07-17 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 14 | 7 | 7 | 6
Tore | 37 | 24 | 13 | 18
Gegentore | 6 | 3 | 3 | 4
Tore/Spiel | 2.64 | 3.43 | 1.86 | 3.00
Gegentore/Spiel | 0.43 | 0.43 | 0.43 | 0.67
xG für/Spiel | 2.18 | 2.48 | 1.89 | 2.19
xG gegen/Spiel | 1.07 | 0.97 | 1.17 | 1.10
Spiele mit xG | 14 | 7 | 7 | 6
S/U/N | 13/1/0 | 7/0/0 | 6/1/0 | 6/0/0
Punkte/Spiel | 2.86 | 3.00 | 2.71 | 3.00
BTTS % | 36 % | 43 % | 29 % | 50 %
Over 2,5 % | 64 % | 86 % | 43 % | 83 %
Under 2,5 % | 36 % | 14 % | 57 % | 17 %
Clean Sheets % | 64 % | 57 % | 71 % | 50 %
Failed to Score % | 7 % | 0 % | 14 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Inter Club d'Escaldes – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 Red Star Belgrade: 15.10. A Lugano (3.00 PPG) 2:3 · 22.10. H København (2.00 PPG) 2:2

Letzte 6 Inter Club d'Escaldes: 15.10. A Mjällby (2.00 PPG) 0:2 · 22.10. H CS U Craiova (2.00 PPG) 1:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Red Star Belgrade [2, 2]; Inter Club d'Escaldes [0, 1]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Inter Club d’Escaldes im API-Abo fehlt; schwächere Offensive ist Inter d’Escaldes mit 1 Tor in 2 Conference-League-Spielen und 0,90 xG, gegen Roter Stern, das in der Liga daheim 7-0-0 bei 24:3 Toren steht; der Weg zu drei Toren hängt allein an Roter Stern und wird nicht gewählt; stärkstes Gegenargument sind Roter Sterns 5 Gegentore in 2 Conference-League-Spielen, die gegen Escaldes' schwache Offensive (0:2 bei Mjällby, 1:3 gegen Craiova) aber keine wesentliche Gefahr für den Heimsieg (Modell 58 %) begründen.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 1.945, λ Gast 1.071; xG-Variante λ Heim 1.617, λ Gast 1.110 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 58 % · Remis 22 % · Auswärtssieg 20 % · BTTS Ja 54 % · Over 2,5 51 % · Under 2,5 49 % (nur Tormodell: BTTS 56 %, Over 2,5 58 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.04 · X 12 · 2 22 · BTTS Ja 2.45 · Over 2,5 1.28 · Under 2,5 3.6.

**Markt:** margenbereinigt 88 % für Heimsieg; Modell 58 %; Abweichung Modell − Markt -30 Prozentpunkte.

**Auswahl:** Heimsieg

---
