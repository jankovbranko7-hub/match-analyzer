# Vorabeintrag Batch 2 · 05.11.2026

- System: FootyStats-System v1.4 (Fassung v1.4-2026-11-05)
- Modell: Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-05 09:51 UTC
- Eintrag erstellt: 2026-11-05 09:56:12 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei Europapokal-Wettbewerben: nur Liga- bzw. Gruppenphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 2.1 Crystal Palace – Hoffenheim | 2026-11-05 17:45 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700955

Analyse-ID: A-20261105-8700955-r1 · Team-IDs: 143 / 49 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Selhurst Park · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-17 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-17–2026-10-22, Gast 2026-09-17–2026-10-22.

**Crystal Palace (Heim, ID 143)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 8 | 4 | 4 | 8
Gegentore | 5 | 0 | 5 | 5
Tore/Spiel | 2.67 | 4.00 | 2.00 | 2.67
Gegentore/Spiel | 1.67 | 0.00 | 2.50 | 1.67
xG für/Spiel | 1.39 | 1.78 | 1.20 | 1.39
xG gegen/Spiel | 1.27 | 1.89 | 0.95 | 1.27
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 1/0/0 | 0/1/1 | 1/1/1
Punkte/Spiel | 1.33 | 3.00 | 0.50 | 1.33
BTTS % | 67 % | 0 % | 100 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 33 % | 100 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Hoffenheim (Gast, ID 49)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 5 | 5 | 0 | 5
Gegentore | 5 | 3 | 2 | 5
Tore/Spiel | 1.67 | 2.50 | 0.00 | 1.67
Gegentore/Spiel | 1.67 | 1.50 | 2.00 | 1.67
xG für/Spiel | 1.99 | 1.81 | 2.35 | 1.99
xG gegen/Spiel | 1.20 | 1.36 | 0.88 | 1.20
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/0/2 | 1/0/1 | 0/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 1.50 | 0.00 | 1.00
BTTS % | 33 % | 50 % | 0 % | 33 %
Over 2,5 % | 67 % | 100 % | 0 % | 67 %
Under 2,5 % | 33 % | 0 % | 100 % | 33 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 33 % | 0 % | 100 % | 33 %
BTTS-and-lose % | 33 % | 50 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Crystal Palace – Landesliga (Saison-ID 17146, 2026-08-22 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 9 | 6 | 3 | 5
Gegentore | 21 | 10 | 11 | 13
Tore/Spiel | 1.00 | 1.50 | 0.60 | 0.83
Gegentore/Spiel | 2.33 | 2.50 | 2.20 | 2.17
xG für/Spiel | 1.13 | 1.38 | 0.93 | 1.14
xG gegen/Spiel | 2.08 | 1.85 | 2.26 | 2.01
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 2/1/6 | 1/0/3 | 1/1/3 | 1/1/4
Punkte/Spiel | 0.78 | 0.75 | 0.80 | 0.67
BTTS % | 44 % | 75 % | 20 % | 33 %
Over 2,5 % | 56 % | 75 % | 40 % | 50 %
Under 2,5 % | 44 % | 25 % | 60 % | 50 %
Clean Sheets % | 11 % | 0 % | 20 % | 17 %
Failed to Score % | 56 % | 25 % | 80 % | 67 %
BTTS-and-lose % | 22 % | 50 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Hoffenheim – Landesliga (Saison-ID 17210, 2026-08-29 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 14 | 9 | 5 | 10
Gegentore | 16 | 7 | 9 | 10
Tore/Spiel | 1.75 | 2.25 | 1.25 | 1.67
Gegentore/Spiel | 2.00 | 1.75 | 2.25 | 1.67
xG für/Spiel | 1.95 | 2.05 | 1.86 | 1.97
xG gegen/Spiel | 1.43 | 1.32 | 1.53 | 1.40
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 3/0/5 | 2/0/2 | 1/0/3 | 3/0/3
Punkte/Spiel | 1.12 | 1.50 | 0.75 | 1.50
BTTS % | 75 % | 75 % | 75 % | 67 %
Over 2,5 % | 88 % | 100 % | 75 % | 83 %
Under 2,5 % | 12 % | 0 % | 25 % | 17 %
Clean Sheets % | 12 % | 25 % | 0 % | 17 %
Failed to Score % | 12 % | 0 % | 25 % | 17 %
BTTS-and-lose % | 50 % | 50 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Crystal Palace: 17.09. H Lech Poznań (0.33 PPG) 4:0 · 15.10. A Olympique Lyonnais (2.00 PPG) 2:3 · 22.10. A Beşiktaş (2.33 PPG) 2:2

Letzte 6 Hoffenheim: 17.09. A OFI (1.00 PPG) 0:2 · 15.10. H Beşiktaş (2.33 PPG) 2:3 · 22.10. H Olympique Lyonnais (2.00 PPG) 3:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Crystal Palace [4, 2, 2]; Hoffenheim [0, 2, 3]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Crystal Palace mit 5 Toren in den letzten sechs Premier-League-Spielen (67 % torlos), das in der Europa League aber 8 Tore in 3 Spielen erzielte; ein Weg zu drei Toren ist mit Hoffenheims 88 % Over in der Bundesliga sichtbar, das Modell schätzt aber nur 51 % Over; stärkstes Gegenargument gegen den Modell-Heimsieg (56 %) ist Palaces Ligaform mit 1-1-4, und weil Liga- und Europa-League-Bild widersprüchlich bleiben, wird kein Markt getragen.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 2.039, λ Gast 1.251; xG-Variante λ Heim 1.455, λ Gast 1.247 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 56 % · Remis 21 % · Auswärtssieg 23 % · BTTS Ja 55 % · Over 2,5 51 % · Under 2,5 49 % (nur Tormodell: BTTS 62 %, Over 2,5 64 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.89 · X 3.96 · 2 3.7 · BTTS Ja 1.45 · Over 2,5 1.53 · Under 2,5 2.36.

**Markt:** Heim 50 % · Remis 24 % · Auswärts 26 % · BTTS 64 % · Over 61 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 2.2 Lillestrøm – Viktoria Plzeň | 2026-11-05 17:45 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700956

Analyse-ID: A-20261105-8700956-r1 · Team-IDs: 339 / 77 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Åråsen Stadion · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Viktoria Plzeň (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-17 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-17–2026-10-22, Gast 2026-09-17–2026-10-22.

**Lillestrøm (Heim, ID 339)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 2 | 1 | 1 | 2
Gegentore | 9 | 8 | 1 | 9
Tore/Spiel | 0.67 | 0.50 | 1.00 | 0.67
Gegentore/Spiel | 3.00 | 4.00 | 1.00 | 3.00
xG für/Spiel | 1.51 | 1.93 | 0.68 | 1.51
xG gegen/Spiel | 1.63 | 1.49 | 1.91 | 1.63
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 0/1/2 | 0/0/2 | 0/1/0 | 0/1/2
Punkte/Spiel | 0.33 | 0.00 | 1.00 | 0.33
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 67 % | 100 % | 0 % | 67 %
Under 2,5 % | 33 % | 0 % | 100 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 50 % | 0 % | 33 %
BTTS-and-lose % | 33 % | 50 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Viktoria Plzeň (Gast, ID 77)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 2 | 1 | 1 | 2
Gegentore | 7 | 5 | 2 | 7
Tore/Spiel | 0.67 | 0.50 | 1.00 | 0.67
Gegentore/Spiel | 2.33 | 2.50 | 2.00 | 2.33
xG für/Spiel | 1.58 | 1.46 | 1.82 | 1.58
xG gegen/Spiel | 1.65 | 1.67 | 1.61 | 1.65
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 0/0/3 | 0/0/2 | 0/0/1 | 0/0/3
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 50 % | 0 % | 33 %
BTTS-and-lose % | 67 % | 50 % | 100 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Lillestrøm – Landesliga (Saison-ID 16558, 2026-03-15 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 25 | 12 | 13 | 6
Tore | 36 | 22 | 14 | 10
Gegentore | 33 | 19 | 14 | 7
Tore/Spiel | 1.44 | 1.83 | 1.08 | 1.67
Gegentore/Spiel | 1.32 | 1.58 | 1.08 | 1.17
xG für/Spiel | 1.46 | 1.43 | 1.48 | 1.53
xG gegen/Spiel | 1.69 | 1.61 | 1.77 | 2.06
Spiele mit xG | 25 | 12 | 13 | 6
S/U/N | 13/3/9 | 6/1/5 | 7/2/4 | 4/1/1
Punkte/Spiel | 1.68 | 1.58 | 1.77 | 2.17
BTTS % | 44 % | 67 % | 23 % | 33 %
Over 2,5 % | 52 % | 75 % | 31 % | 50 %
Under 2,5 % | 48 % | 25 % | 69 % | 50 %
Clean Sheets % | 32 % | 17 % | 46 % | 50 %
Failed to Score % | 28 % | 17 % | 38 % | 17 %
BTTS-and-lose % | 12 % | 25 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Viktoria Plzeň – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 Lillestrøm: 17.09. H Torreense (1.00 PPG) 1:2 · 15.10. A Sparta Praha (1.33 PPG) 1:1 · 22.10. H Real Sociedad (1.33 PPG) 0:6

Letzte 6 Viktoria Plzeň: 17.09. H Union Saint-Gilloise (2.33 PPG) 0:3 · 15.10. A Ferencváros (3.00 PPG) 1:2 · 22.10. H Levski Sofia (1.33 PPG) 1:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Lillestrøm [1, 1, 0]; Viktoria Plzeň [0, 1, 1]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Viktoria Plzeň im API-Abo fehlt; schwächere Offensive ist Lillestrøm mit 2 Toren in 3 Europa-League-Spielen, gegen Plzeň ohne Clean Sheet; ein Weg zu drei Toren ist mit 67 % bzw. 100 % Over in drei Spielen unsicher; stärkstes Gegenargument gegen jede Auswahl ist das ausgeglichene Modell (Heim 35 %, Auswärts 39 %) bei fehlender Ligabasis für Plzeň, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.299, λ Gast 1.377; xG-Variante λ Heim 1.636, λ Gast 1.255 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 35 % · Remis 26 % · Auswärtssieg 39 % · BTTS Ja 58 % · Over 2,5 55 % · Under 2,5 45 % (nur Tormodell: BTTS 54 %, Over 2,5 50 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.05 · X 3.65 · 2 2.2 · BTTS Ja 1.47 · Over 2,5 1.57 · Under 2,5 2.37.

**Markt:** Heim 31 % · Remis 26 % · Auswärts 43 % · BTTS 64 % · Over 60 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 2.3 Real Sociedad – Olympique Lyonnais | 2026-11-05 17:45 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700984

Analyse-ID: A-20261105-8700984-r1 · Team-IDs: 290 / 57 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Anoeta Stadium · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-17 bis 2026-10-22, Gast 2026-09-16 bis 2026-10-22; letzte 6: Heim 2026-09-17–2026-10-22, Gast 2026-09-16–2026-10-22.

**Real Sociedad (Heim, ID 290)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 8 | 1 | 7 | 8
Gegentore | 3 | 2 | 1 | 3
Tore/Spiel | 2.67 | 1.00 | 3.50 | 2.67
Gegentore/Spiel | 1.00 | 2.00 | 0.50 | 1.00
xG für/Spiel | 1.48 | 1.77 | 1.33 | 1.48
xG gegen/Spiel | 1.41 | 1.21 | 1.52 | 1.41
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 0/0/1 | 1/1/0 | 1/1/1
Punkte/Spiel | 1.33 | 0.00 | 2.00 | 1.33
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 33 % | 0 % | 50 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 100 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Olympique Lyonnais (Gast, ID 57)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 5 | 3 | 2 | 5
Gegentore | 6 | 2 | 4 | 6
Tore/Spiel | 1.67 | 3.00 | 1.00 | 1.67
Gegentore/Spiel | 2.00 | 2.00 | 2.00 | 2.00
xG für/Spiel | 1.25 | 1.16 | 1.29 | 1.25
xG gegen/Spiel | 1.77 | 1.36 | 1.97 | 1.77
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 2/0/1 | 1/0/0 | 1/0/1 | 2/0/1
Punkte/Spiel | 2.00 | 3.00 | 1.50 | 2.00
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Real Sociedad – Landesliga (Saison-ID 17199, 2026-08-21 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 20 | 7 | 13 | 14
Gegentore | 20 | 7 | 13 | 12
Tore/Spiel | 1.82 | 1.40 | 2.17 | 2.33
Gegentore/Spiel | 1.82 | 1.40 | 2.17 | 2.00
xG für/Spiel | 1.58 | 1.55 | 1.61 | 1.66
xG gegen/Spiel | 1.72 | 1.32 | 2.05 | 1.65
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 6/1/4 | 3/1/1 | 3/0/3 | 4/0/2
Punkte/Spiel | 1.73 | 2.00 | 1.50 | 2.00
BTTS % | 73 % | 60 % | 83 % | 83 %
Over 2,5 % | 82 % | 80 % | 83 % | 100 %
Under 2,5 % | 18 % | 20 % | 17 % | 0 %
Clean Sheets % | 9 % | 20 % | 0 % | 0 %
Failed to Score % | 27 % | 40 % | 17 % | 17 %
BTTS-and-lose % | 18 % | 0 % | 33 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Olympique Lyonnais – Landesliga (Saison-ID 17102, 2026-08-22 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 15 | 12 | 3 | 9
Gegentore | 7 | 3 | 4 | 5
Tore/Spiel | 1.67 | 2.40 | 0.75 | 1.50
Gegentore/Spiel | 0.78 | 0.60 | 1.00 | 0.83
xG für/Spiel | 1.47 | 1.78 | 1.09 | 1.39
xG gegen/Spiel | 1.39 | 1.21 | 1.62 | 1.46
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 5/2/2 | 4/1/0 | 1/1/2 | 3/1/2
Punkte/Spiel | 1.89 | 2.60 | 1.00 | 1.67
BTTS % | 44 % | 60 % | 25 % | 33 %
Over 2,5 % | 44 % | 60 % | 25 % | 50 %
Under 2,5 % | 56 % | 40 % | 75 % | 50 %
Clean Sheets % | 44 % | 40 % | 50 % | 50 %
Failed to Score % | 22 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 11 % | 0 % | 25 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Real Sociedad: 17.09. H AFC Bournemouth (3.00 PPG) 1:2 · 15.10. A Union Saint-Gilloise (2.33 PPG) 1:1 · 22.10. A Lillestrøm (0.33 PPG) 6:0

Letzte 6 Olympique Lyonnais: 16.09. A RSC Anderlecht (1.00 PPG) 2:1 · 15.10. H Crystal Palace (1.33 PPG) 3:2 · 22.10. A Hoffenheim (1.00 PPG) 0:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Real Sociedad [1, 1, 6]; Olympique Lyonnais [2, 3, 0]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Lyon in der Ligue 1 auswärts mit 3 Toren in 4 Spielen (50 % torlos), gegen Real Sociedad mit nur 9 % Liga-Clean-Sheets; der Weg zu drei Toren ist widersprüchlich, weil Real Sociedads letzte sechs Ligaspiele alle Over endeten, Lyons Liga-Auswärtsspiele aber nur zu 25 %; stärkstes Gegenargument gegen den Heimsieg (Modell 42 %) ist Lyons Europa-League-Bilanz von 2-0-1, sodass kein Markt widerspruchsfrei getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.580, λ Gast 1.369; xG-Variante λ Heim 1.485, λ Gast 1.287 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 42 % · Remis 24 % · Auswärtssieg 33 % · BTTS Ja 56 % · Over 2,5 52 % · Under 2,5 48 % (nur Tormodell: BTTS 59 %, Over 2,5 57 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.75 · X 4.1 · 2 4.4 · BTTS Ja 1.53 · Over 2,5 1.57 · Under 2,5 2.42.

**Markt:** Heim 55 % · Remis 23 % · Auswärts 22 % · BTTS 61 % · Over 61 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 2.4 Levski Sofia – Jagiellonia Białystok | 2026-11-05 17:45 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700958

Analyse-ID: A-20261105-8700958-r1 · Team-IDs: 3605 / 1224 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Vivacom Arena - Georgi Asparuhov · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-17 bis 2026-10-22, Gast 2026-09-16 bis 2026-10-22; letzte 6: Heim 2026-09-17–2026-10-22, Gast 2026-09-16–2026-10-22.

**Levski Sofia (Heim, ID 3605)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 3 | 0 | 3 | 3
Gegentore | 3 | 1 | 2 | 3
Tore/Spiel | 1.00 | 0.00 | 1.50 | 1.00
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 0.89 | 1.17 | 0.75 | 0.89
xG gegen/Spiel | 1.72 | 1.53 | 1.81 | 1.72
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 0/0/1 | 1/1/0 | 1/1/1
Punkte/Spiel | 1.33 | 0.00 | 2.00 | 1.33
BTTS % | 67 % | 0 % | 100 % | 67 %
Over 2,5 % | 33 % | 0 % | 50 % | 33 %
Under 2,5 % | 67 % | 100 % | 50 % | 67 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 100 % | 0 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Jagiellonia Białystok (Gast, ID 1224)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 4 | 3 | 1 | 4
Gegentore | 6 | 4 | 2 | 6
Tore/Spiel | 1.33 | 1.50 | 1.00 | 1.33
Gegentore/Spiel | 2.00 | 2.00 | 2.00 | 2.00
xG für/Spiel | 0.89 | 1.03 | 0.60 | 0.89
xG gegen/Spiel | 2.04 | 1.77 | 2.57 | 2.04
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/0/2 | 1/0/1 | 0/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 1.50 | 0.00 | 1.00
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 50 % | 0 % | 33 %
BTTS-and-lose % | 33 % | 0 % | 100 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Levski Sofia – Landesliga (Saison-ID 17088, 2026-07-17 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 5 | 7 | 6
Tore | 25 | 14 | 11 | 7
Gegentore | 5 | 1 | 4 | 2
Tore/Spiel | 2.08 | 2.80 | 1.57 | 1.17
Gegentore/Spiel | 0.42 | 0.20 | 0.57 | 0.33
xG für/Spiel | 1.99 | 2.15 | 1.89 | 1.93
xG gegen/Spiel | 0.81 | 0.76 | 0.84 | 0.82
Spiele mit xG | 12 | 5 | 7 | 6
S/U/N | 10/2/0 | 5/0/0 | 5/2/0 | 4/2/0
Punkte/Spiel | 2.67 | 3.00 | 2.43 | 2.33
BTTS % | 42 % | 20 % | 57 % | 33 %
Over 2,5 % | 50 % | 60 % | 43 % | 17 %
Under 2,5 % | 50 % | 40 % | 57 % | 83 %
Clean Sheets % | 58 % | 80 % | 43 % | 67 %
Failed to Score % | 8 % | 0 % | 14 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Jagiellonia Białystok – Landesliga (Saison-ID 17112, 2026-07-25 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 17 | 6 | 11 | 6
Gegentore | 18 | 9 | 9 | 10
Tore/Spiel | 1.42 | 1.00 | 1.83 | 1.00
Gegentore/Spiel | 1.50 | 1.50 | 1.50 | 1.67
xG für/Spiel | 1.70 | 1.76 | 1.64 | 1.74
xG gegen/Spiel | 1.79 | 1.55 | 2.03 | 1.76
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 6/0/6 | 3/0/3 | 3/0/3 | 2/0/4
Punkte/Spiel | 1.50 | 1.50 | 1.50 | 1.00
BTTS % | 58 % | 50 % | 67 % | 50 %
Over 2,5 % | 58 % | 50 % | 67 % | 50 %
Under 2,5 % | 42 % | 50 % | 33 % | 50 %
Clean Sheets % | 17 % | 33 % | 0 % | 17 %
Failed to Score % | 25 % | 17 % | 33 % | 33 %
BTTS-and-lose % | 25 % | 33 % | 17 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Levski Sofia: 17.09. H Salzburg (1.33 PPG) 0:1 · 15.10. A NEC (1.33 PPG) 1:1 · 22.10. A Viktoria Plzeň (0.00 PPG) 2:1

Letzte 6 Jagiellonia Białystok: 16.09. A Olympiakos Piraeus (2.50 PPG) 1:2 · 15.10. H FC Avan Academy (0.00 PPG) 3:1 · 22.10. H RSC Anderlecht (1.00 PPG) 0:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Levski Sofia [0, 1, 2]; Jagiellonia Białystok [1, 3, 0]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Jagiellonia mit 0,89 xG in der Europa League (0:3 daheim gegen Anderlecht), gegen Levski, das in der Liga daheim 5-0-0 bei 14:1 Toren steht, während Jagiellonia in der Liga auswärts ohne Clean Sheet ist; der Weg zu drei Toren ist mit Levskis 17 % Over in den letzten sechs Ligaspielen schwach und wird nicht gewählt; stärkstes Gegenargument ist Levskis schwacher Chancenwert in der Europa League (0,89 xG) und die Heimniederlage gegen Salzburg, was als wesentliche Gefahr für den Heimsieg (Modell 50 %) gewichtet wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.679, λ Gast 1.120; xG-Variante λ Heim 1.563, λ Gast 1.191 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 50 % · Remis 24 % · Auswärtssieg 25 % · BTTS Ja 55 % · Over 2,5 52 % · Under 2,5 48 % (nur Tormodell: BTTS 55 %, Over 2,5 53 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.94 · X 3.65 · 2 3.7 · BTTS Ja 1.66 · Over 2,5 1.8 · Under 2,5 2.

**Markt:** margenbereinigt 49 % für Heimsieg; Modell 50 %; Abweichung Modell − Markt +2 Prozentpunkte.

**Auswahl:** Heimsieg

⚠️ Levski in der Europa League nur 0,89 xG pro Spiel und daheim 0:1 gegen Salzburg.

---

## 2.5 AC Milan – Ferencváros | 2026-11-05 17:45 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700990

Analyse-ID: A-20261105-8700990-r1 · Team-IDs: 461 / 119 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Stadio Giuseppe Meazza · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Ferencváros (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-17–2026-10-22.

**AC Milan (Heim, ID 461)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 0 | 4 | 4
Gegentore | 5 | 2 | 3 | 5
Tore/Spiel | 1.33 | 0.00 | 2.00 | 1.33
Gegentore/Spiel | 1.67 | 2.00 | 1.50 | 1.67
xG für/Spiel | 1.35 | 1.85 | 1.09 | 1.35
xG gegen/Spiel | 1.57 | 1.14 | 1.78 | 1.57
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 0/0/1 | 1/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 0.00 | 1.50 | 1.00
BTTS % | 0 % | 0 % | 0 % | 0 %
Over 2,5 % | 67 % | 0 % | 100 % | 67 %
Under 2,5 % | 33 % | 100 % | 0 % | 33 %
Clean Sheets % | 33 % | 0 % | 50 % | 33 %
Failed to Score % | 67 % | 100 % | 50 % | 67 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Ferencváros (Gast, ID 119)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 9 | 6 | 3 | 9
Gegentore | 3 | 2 | 1 | 3
Tore/Spiel | 3.00 | 3.00 | 3.00 | 3.00
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 1.67 | 1.66 | 1.69 | 1.67
xG gegen/Spiel | 1.52 | 1.39 | 1.78 | 1.52
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

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**AC Milan – Landesliga (Saison-ID 17084, 2026-08-23 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 21 | 13 | 8 | 14
Gegentore | 12 | 7 | 5 | 8
Tore/Spiel | 2.10 | 2.60 | 1.60 | 2.33
Gegentore/Spiel | 1.20 | 1.40 | 1.00 | 1.33
xG für/Spiel | 1.39 | 1.24 | 1.54 | 1.33
xG gegen/Spiel | 1.26 | 1.30 | 1.23 | 1.35
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 6/3/1 | 4/0/1 | 2/3/0 | 4/1/1
Punkte/Spiel | 2.10 | 2.40 | 1.80 | 2.17
BTTS % | 70 % | 60 % | 80 % | 67 %
Over 2,5 % | 60 % | 80 % | 40 % | 67 %
Under 2,5 % | 40 % | 20 % | 60 % | 33 %
Clean Sheets % | 30 % | 40 % | 20 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 10 % | 20 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Ferencváros – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 AC Milan: 16.09. H Benfica (3.00 PPG) 0:2 · 15.10. A Salzburg (1.33 PPG) 4:0 · 22.10. A AFC Bournemouth (3.00 PPG) 0:3

Letzte 6 Ferencváros: 17.09. A Celtic (0.00 PPG) 3:1 · 15.10. H Viktoria Plzeň (0.00 PPG) 2:1 · 22.10. H Torreense (1.00 PPG) 4:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): AC Milan [0, 4, 0]; Ferencváros [3, 2, 4]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Ferencváros im API-Abo fehlt; schwächere Offensive ist Milan in der Europa League mit 4 Toren in 3 Spielen und zwei torlosen Spielen, gegen Ferencváros ohne Clean Sheet; ein Weg zu drei Toren ist mit Ferencváros' 3 Over-Spielen sichtbar, aber unsicher; stärkstes Gegenargument gegen den Heimsieg (Modell 44 %) ist Ferencváros' Europa-League-Bilanz von 3-0-0 bei fehlender Ligabasis, und Milans wiederholte Torlosigkeit in diesem Wettbewerb, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.719, λ Gast 1.443; xG-Variante λ Heim 1.580, λ Gast 1.177 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 44 % · Remis 23 % · Auswärtssieg 32 % · BTTS Ja 55 % · Over 2,5 52 % · Under 2,5 48 % (nur Tormodell: BTTS 63 %, Over 2,5 61 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.34 · X 5.2 · 2 7.5 · BTTS Ja 1.79 · Over 2,5 1.53 · Under 2,5 2.45.

**Markt:** Heim 70 % · Remis 18 % · Auswärts 12 % · BTTS 52 % · Over 62 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---
