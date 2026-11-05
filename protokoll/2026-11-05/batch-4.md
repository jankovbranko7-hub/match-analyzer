# Vorabeintrag Batch 4 · 05.11.2026

- System: FootyStats-System v1.4 (Fassung v1.4-2026-11-05)
- Modell: Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-05 09:51 UTC
- Eintrag erstellt: 2026-11-05 09:56:12 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei Europapokal-Wettbewerben: nur Liga- bzw. Gruppenphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 4.1 Celtic – Beşiktaş | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700922

Analyse-ID: A-20261105-8700922-r1 · Team-IDs: 23 / 109 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Celtic Park · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-17 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-17–2026-10-22, Gast 2026-09-17–2026-10-22.

**Celtic (Heim, ID 23)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 3 | 2 | 1 | 3
Gegentore | 9 | 5 | 4 | 9
Tore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
Gegentore/Spiel | 3.00 | 2.50 | 4.00 | 3.00
xG für/Spiel | 1.49 | 1.44 | 1.59 | 1.49
xG gegen/Spiel | 2.13 | 1.89 | 2.61 | 2.13
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 0/0/3 | 0/0/2 | 0/0/1 | 0/0/3
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 100 % | 100 % | 100 % | 100 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Beşiktaş (Gast, ID 109)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 9 | 6 | 3 | 9
Gegentore | 5 | 3 | 2 | 5
Tore/Spiel | 3.00 | 3.00 | 3.00 | 3.00
Gegentore/Spiel | 1.67 | 1.50 | 2.00 | 1.67
xG für/Spiel | 1.49 | 1.31 | 1.85 | 1.49
xG gegen/Spiel | 1.24 | 1.18 | 1.36 | 1.24
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 2/1/0 | 1/1/0 | 1/0/0 | 2/1/0
Punkte/Spiel | 2.33 | 2.00 | 3.00 | 2.33
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Celtic – Landesliga (Saison-ID 17148, 2026-08-03 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 27 | 15 | 12 | 13
Gegentore | 10 | 5 | 5 | 7
Tore/Spiel | 2.25 | 2.50 | 2.00 | 2.17
Gegentore/Spiel | 0.83 | 0.83 | 0.83 | 1.17
xG für/Spiel | 2.44 | 2.21 | 2.68 | 2.28
xG gegen/Spiel | 1.25 | 1.32 | 1.19 | 1.34
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 9/1/2 | 4/1/1 | 5/0/1 | 3/1/2
Punkte/Spiel | 2.33 | 2.17 | 2.50 | 1.67
BTTS % | 50 % | 50 % | 50 % | 50 %
Over 2,5 % | 58 % | 67 % | 50 % | 50 %
Under 2,5 % | 42 % | 33 % | 50 % | 50 %
Clean Sheets % | 33 % | 33 % | 33 % | 17 %
Failed to Score % | 17 % | 17 % | 17 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Beşiktaş – Landesliga (Saison-ID 17265, 2026-08-16 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 20 | 14 | 6 | 11
Gegentore | 12 | 3 | 9 | 8
Tore/Spiel | 2.00 | 2.80 | 1.20 | 1.83
Gegentore/Spiel | 1.20 | 0.60 | 1.80 | 1.33
xG für/Spiel | 1.86 | 1.94 | 1.79 | 1.86
xG gegen/Spiel | 1.11 | 0.94 | 1.28 | 1.26
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 6/1/3 | 5/0/0 | 1/1/3 | 3/1/2
Punkte/Spiel | 1.90 | 3.00 | 0.80 | 1.67
BTTS % | 50 % | 40 % | 60 % | 50 %
Over 2,5 % | 60 % | 60 % | 60 % | 67 %
Under 2,5 % | 40 % | 40 % | 40 % | 33 %
Clean Sheets % | 30 % | 60 % | 0 % | 33 %
Failed to Score % | 20 % | 0 % | 40 % | 17 %
BTTS-and-lose % | 10 % | 0 % | 20 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Celtic: 17.09. H Ferencváros (3.00 PPG) 1:3 · 15.10. A Benfica (3.00 PPG) 1:4 · 22.10. H Celta de Vigo (1.00 PPG) 1:2

Letzte 6 Beşiktaş: 17.09. H Olympique Marseille (0.00 PPG) 4:1 · 15.10. A Hoffenheim (1.00 PPG) 3:2 · 22.10. H Crystal Palace (1.33 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Celtic [1, 1, 1]; Beşiktaş [4, 3, 2]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Celtic in der Europa League mit 3 Toren in 3 Spielen, das aber in jedem Spiel traf und in der Liga nur zu 17 % torlos blieb, gegen Beşiktaş ohne Clean Sheet in der Europa League und in 5 Liga-Auswärtsspielen, während Beşiktaş in allen 3 Europa-League-Spielen traf (9 Tore) gegen Celtic mit 9 Gegentoren in 3 Spielen; der Weg zu drei Toren ist mit 100 % Over in beiden Europa-League-Bilanzen ebenfalls plausibel, BTTS ist durch beide eigenen Torserien aber direkter belegt (Modell 60 %); stärkstes Gegenargument ist Beşiktaş' Torlosigkeit in 2 von 5 Liga-Auswärtsspielen, die als wesentliche Gefahr für den Gästetreffer gewichtet wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.866, λ Gast 1.631; xG-Variante λ Heim 1.582, λ Gast 1.397 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 44 % · Remis 22 % · Auswärtssieg 34 % · BTTS Ja 60 % · Over 2,5 57 % · Under 2,5 43 % (nur Tormodell: BTTS 68 %, Over 2,5 68 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.63 · X 3.74 · 2 2.08 · BTTS Ja 1.47 · Over 2,5 1.64 · Under 2,5 2.27.

**Markt:** margenbereinigt 64 % für BTTS Ja; Modell 60 %; Abweichung Modell − Markt -4 Prozentpunkte.

**Auswahl:** BTTS Ja

⚠️ Beşiktaş blieb in 2 von 5 Liga-Auswärtsspielen torlos – Gefahr für den Gästetreffer.

---

## 4.2 Benfica – Lech Poznań | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700951

Analyse-ID: A-20261105-8700951-r1 · Team-IDs: 78 / 961 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Estádio do Sport Lisboa e Benfica · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-17–2026-10-22.

**Benfica (Heim, ID 78)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 10 | 4 | 6 | 10
Gegentore | 2 | 1 | 1 | 2
Tore/Spiel | 3.33 | 4.00 | 3.00 | 3.33
Gegentore/Spiel | 0.67 | 1.00 | 0.50 | 0.67
xG für/Spiel | 2.14 | 2.61 | 1.90 | 2.14
xG gegen/Spiel | 1.47 | 1.59 | 1.41 | 1.47
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 3/0/0 | 1/0/0 | 2/0/0 | 3/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 33 % | 0 % | 50 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Lech Poznań (Gast, ID 961)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 1 | 1 | 0 | 1
Gegentore | 9 | 5 | 4 | 9
Tore/Spiel | 0.33 | 0.50 | 0.00 | 0.33
Gegentore/Spiel | 3.00 | 2.50 | 4.00 | 3.00
xG für/Spiel | 1.52 | 1.33 | 1.89 | 1.52
xG gegen/Spiel | 2.37 | 2.66 | 1.78 | 2.37
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 0/1/2 | 0/1/1 | 0/0/1 | 0/1/2
Punkte/Spiel | 0.33 | 0.50 | 0.00 | 0.33
BTTS % | 33 % | 50 % | 0 % | 33 %
Over 2,5 % | 67 % | 50 % | 100 % | 67 %
Under 2,5 % | 33 % | 50 % | 0 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 67 % | 50 % | 100 % | 67 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Benfica – Landesliga (Saison-ID 17217, 2026-08-09 bis 2026-11-02)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 27 | 10 | 17 | 13
Gegentore | 8 | 4 | 4 | 5
Tore/Spiel | 2.70 | 2.00 | 3.40 | 2.17
Gegentore/Spiel | 0.80 | 0.80 | 0.80 | 0.83
xG für/Spiel | 2.09 | 2.36 | 1.81 | 1.88
xG gegen/Spiel | 0.89 | 0.72 | 1.06 | 1.06
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 8/1/1 | 4/1/0 | 4/0/1 | 5/0/1
Punkte/Spiel | 2.50 | 2.60 | 2.40 | 2.50
BTTS % | 50 % | 60 % | 40 % | 50 %
Over 2,5 % | 80 % | 60 % | 100 % | 67 %
Under 2,5 % | 20 % | 40 % | 0 % | 33 %
Clean Sheets % | 50 % | 40 % | 60 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 10 % | 0 % | 20 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Lech Poznań – Landesliga (Saison-ID 17112, 2026-07-25 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 7 | 5 | 6
Tore | 32 | 20 | 12 | 21
Gegentore | 11 | 4 | 7 | 7
Tore/Spiel | 2.67 | 2.86 | 2.40 | 3.50
Gegentore/Spiel | 0.92 | 0.57 | 1.40 | 1.17
xG für/Spiel | 1.93 | 2.12 | 1.67 | 1.76
xG gegen/Spiel | 1.33 | 1.17 | 1.56 | 1.52
Spiele mit xG | 12 | 7 | 5 | 6
S/U/N | 10/1/1 | 6/1/0 | 4/0/1 | 5/0/1
Punkte/Spiel | 2.58 | 2.71 | 2.40 | 2.50
BTTS % | 75 % | 57 % | 100 % | 100 %
Over 2,5 % | 83 % | 71 % | 100 % | 100 %
Under 2,5 % | 17 % | 29 % | 0 % | 0 %
Clean Sheets % | 25 % | 43 % | 0 % | 0 %
Failed to Score % | 8 % | 14 % | 0 % | 0 %
BTTS-and-lose % | 8 % | 0 % | 20 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Benfica: 16.09. A AC Milan (1.00 PPG) 2:0 · 15.10. H Celtic (0.00 PPG) 4:1 · 22.10. A Omonia Nicosia (2.00 PPG) 4:1

Letzte 6 Lech Poznań: 17.09. A Crystal Palace (1.33 PPG) 0:4 · 15.10. H Bayer Leverkusen (3.00 PPG) 0:4 · 22.10. H Sunderland (2.33 PPG) 1:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Benfica [2, 4, 4]; Lech Poznań [0, 0, 1]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Lech mit 1 Tor in 3 Europa-League-Spielen, gegen Benfica mit 50 % Liga-Clean-Sheets; der Weg zu drei Toren hängt vor allem an Benfica (10 Europa-League-Tore) und wird nicht gewählt; stärkstes Gegenargument ist Lechs starke Ligaform (10-1-1, auswärts in jedem Spiel getroffen), die gegen Benficas 3-0-0 in der Europa League und 8-1-1 in der Liga den Heimsieg (Modell 69 %) aber nicht entkräftet.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 2.404, λ Gast 0.971; xG-Variante λ Heim 1.859, λ Gast 1.268 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 69 % · Remis 17 % · Auswärtssieg 13 % · BTTS Ja 61 % · Over 2,5 60 % · Under 2,5 40 % (nur Tormodell: BTTS 57 %, Over 2,5 66 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.13 · X 7.8 · 2 13 · BTTS Ja 1.9 · Over 2,5 1.3 · Under 2,5 3.75.

**Markt:** margenbereinigt 81 % für Heimsieg; Modell 69 %; Abweichung Modell − Markt -12 Prozentpunkte.

**Auswahl:** Heimsieg

---

## 4.3 Hapoel Be'er Sheva – OFI | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700868

Analyse-ID: A-20261105-8700868-r1 · Team-IDs: 58 / 5130 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Stadionul Valentin Stănescu · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Hapoel Be'er Sheva (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-17–2026-10-22.

**Hapoel Be'er Sheva (Heim, ID 58)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 1 | 0 | 1 | 1
Gegentore | 6 | 0 | 6 | 6
Tore/Spiel | 0.33 | 0.00 | 0.50 | 0.33
Gegentore/Spiel | 2.00 | 0.00 | 3.00 | 2.00
xG für/Spiel | 1.17 | 1.70 | 0.90 | 1.17
xG gegen/Spiel | 2.04 | 0.76 | 2.69 | 2.04
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 0/1/2 | 0/1/0 | 0/0/2 | 0/1/2
Punkte/Spiel | 0.33 | 1.00 | 0.00 | 0.33
BTTS % | 33 % | 0 % | 50 % | 33 %
Over 2,5 % | 67 % | 0 % | 100 % | 67 %
Under 2,5 % | 33 % | 100 % | 0 % | 33 %
Clean Sheets % | 33 % | 100 % | 0 % | 33 %
Failed to Score % | 67 % | 100 % | 50 % | 67 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**OFI (Gast, ID 5130)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 3 | 2 | 1 | 3
Gegentore | 4 | 2 | 2 | 4
Tore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
Gegentore/Spiel | 1.33 | 1.00 | 2.00 | 1.33
xG für/Spiel | 0.66 | 0.78 | 0.43 | 0.66
xG gegen/Spiel | 2.92 | 2.99 | 2.78 | 2.92
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 1/0/2 | 1/0/1 | 0/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 1.50 | 0.00 | 1.00
BTTS % | 33 % | 0 % | 100 % | 33 %
Over 2,5 % | 33 % | 0 % | 100 % | 33 %
Under 2,5 % | 67 % | 100 % | 0 % | 67 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 33 % | 50 % | 0 % | 33 %
BTTS-and-lose % | 33 % | 0 % | 100 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Hapoel Be'er Sheva – Landesliga:** fehlt (Liga nicht im API-Abo)

**OFI – Landesliga (Saison-ID 17356, 2026-08-23 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 14 | 8 | 6 | 9
Gegentore | 12 | 3 | 9 | 10
Tore/Spiel | 1.56 | 2.00 | 1.20 | 1.50
Gegentore/Spiel | 1.33 | 0.75 | 1.80 | 1.67
xG für/Spiel | 1.14 | 1.25 | 1.05 | 1.25
xG gegen/Spiel | 1.70 | 1.55 | 1.82 | 1.77
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 5/1/3 | 3/1/0 | 2/0/3 | 3/1/2
Punkte/Spiel | 1.78 | 2.50 | 1.20 | 1.67
BTTS % | 44 % | 50 % | 40 % | 50 %
Over 2,5 % | 56 % | 50 % | 60 % | 67 %
Under 2,5 % | 44 % | 50 % | 40 % | 33 %
Clean Sheets % | 44 % | 50 % | 40 % | 33 %
Failed to Score % | 11 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 22 % | 0 % | 40 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Hapoel Be'er Sheva: 16.09. H Dinamo Zagreb (1.33 PPG) 0:0 · 15.10. A AZ (2.00 PPG) 1:2 · 22.10. A Union Saint-Gilloise (2.33 PPG) 0:4

Letzte 6 OFI: 17.09. H Hoffenheim (1.00 PPG) 2:0 · 15.10. A Rennes (1.50 PPG) 1:2 · 22.10. H Bayer Leverkusen (3.00 PPG) 0:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Hapoel Be'er Sheva [0, 1, 0]; OFI [2, 1, 0]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Hapoel Be’er Sheva im API-Abo fehlt; schwächere Offensive ist OFI mit 0,66 xG in der Europa League, aber auch Hapoel erzielte nur 1 Tor in 3 Spielen; ein Weg zu drei Toren ist bei beiden schwachen Offensiven unsicher; stärkstes Gegenargument gegen jede Auswahl ist das ausgeglichene Modell (Heim 40 %, Auswärts 33 %) bei fehlender Ligabasis für Hapoel, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.391, λ Gast 1.242; xG-Variante λ Heim 1.799, λ Gast 1.216 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 40 % · Remis 26 % · Auswärtssieg 33 % · BTTS Ja 59 % · Over 2,5 58 % · Under 2,5 42 % (nur Tormodell: BTTS 53 %, Over 2,5 49 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.02 · X 3.6 · 2 2.83 · BTTS Ja 1.55 · Over 2,5 1.68 · Under 2,5 2.2.

**Markt:** Heim 44 % · Remis 25 % · Auswärts 31 % · BTTS 61 % · Over 57 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 4.4 Celta de Vigo – Union Saint-Gilloise | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700886

Analyse-ID: A-20261105-8700886-r1 · Team-IDs: 281 / 2572 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Estadio de Balaídos · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-17–2026-10-22.

**Celta de Vigo (Heim, ID 281)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 3 | 1 | 2 | 3
Gegentore | 4 | 2 | 2 | 4
Tore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
Gegentore/Spiel | 1.33 | 2.00 | 1.00 | 1.33
xG für/Spiel | 1.65 | 0.97 | 2.00 | 1.65
xG gegen/Spiel | 1.50 | 2.26 | 1.11 | 1.50
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

**Union Saint-Gilloise (Gast, ID 2572)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 8 | 5 | 3 | 8
Gegentore | 1 | 1 | 0 | 1
Tore/Spiel | 2.67 | 2.50 | 3.00 | 2.67
Gegentore/Spiel | 0.33 | 0.50 | 0.00 | 0.33
xG für/Spiel | 2.61 | 2.60 | 2.61 | 2.61
xG gegen/Spiel | 1.09 | 0.85 | 1.56 | 1.09
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 2/1/0 | 1/1/0 | 1/0/0 | 2/1/0
Punkte/Spiel | 2.33 | 2.00 | 3.00 | 2.33
BTTS % | 33 % | 50 % | 0 % | 33 %
Over 2,5 % | 67 % | 50 % | 100 % | 67 %
Under 2,5 % | 33 % | 50 % | 0 % | 33 %
Clean Sheets % | 67 % | 50 % | 100 % | 67 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Celta de Vigo – Landesliga (Saison-ID 17199, 2026-08-22 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 10 | 9 | 1 | 8
Gegentore | 10 | 6 | 4 | 5
Tore/Spiel | 0.91 | 1.50 | 0.20 | 1.33
Gegentore/Spiel | 0.91 | 1.00 | 0.80 | 0.83
xG für/Spiel | 1.15 | 1.22 | 1.08 | 1.22
xG gegen/Spiel | 1.46 | 1.60 | 1.29 | 1.53
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 2/6/3 | 2/2/2 | 0/4/1 | 2/3/1
Punkte/Spiel | 1.09 | 1.33 | 0.80 | 1.50
BTTS % | 36 % | 50 % | 20 % | 33 %
Over 2,5 % | 36 % | 50 % | 20 % | 50 %
Under 2,5 % | 64 % | 50 % | 80 % | 50 %
Clean Sheets % | 45 % | 33 % | 60 % | 50 %
Failed to Score % | 55 % | 33 % | 80 % | 50 %
BTTS-and-lose % | 9 % | 17 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Union Saint-Gilloise – Landesliga (Saison-ID 17171, 2026-08-08 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 29 | 14 | 15 | 18
Gegentore | 7 | 3 | 4 | 6
Tore/Spiel | 2.90 | 2.80 | 3.00 | 3.00
Gegentore/Spiel | 0.70 | 0.60 | 0.80 | 1.00
xG für/Spiel | 1.97 | 2.14 | 1.81 | 2.17
xG gegen/Spiel | 1.14 | 1.07 | 1.21 | 1.09
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 8/2/0 | 3/2/0 | 5/0/0 | 5/1/0
Punkte/Spiel | 2.60 | 2.20 | 3.00 | 2.67
BTTS % | 50 % | 40 % | 60 % | 67 %
Over 2,5 % | 70 % | 60 % | 80 % | 67 %
Under 2,5 % | 30 % | 40 % | 20 % | 33 %
Clean Sheets % | 50 % | 60 % | 40 % | 33 %
Failed to Score % | 10 % | 20 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Celta de Vigo: 16.09. A Omonia Nicosia (2.00 PPG) 0:1 · 15.10. H Juventus (2.33 PPG) 1:2 · 22.10. A Celtic (0.00 PPG) 2:1

Letzte 6 Union Saint-Gilloise: 17.09. A Viktoria Plzeň (0.00 PPG) 3:0 · 15.10. H Real Sociedad (1.33 PPG) 1:1 · 22.10. H Hapoel Be'er Sheva (0.33 PPG) 4:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Celta de Vigo [0, 1, 2]; Union Saint-Gilloise [3, 1, 4]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Celta mit 10 Toren in 11 La-Liga-Spielen und 55 % torlosen Spielen, gegen Union Saint-Gilloise mit 67 % Clean Sheets in der Europa League; ein Weg zu drei Toren ist widersprüchlich (Celta 36 % Over in der Liga, Union auswärts 80 %); stärkstes Gegenargument ist der ungeklärte Widerspruch zwischen dem Modell, das Celta leicht vorn sieht (45 % zu 29 %), und Unions Form (8-2-0 in der Liga, 2-1-0 in der Europa League), sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.460, λ Gast 1.117; xG-Variante λ Heim 1.362, λ Gast 1.394 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 45 % · Remis 26 % · Auswärtssieg 29 % · BTTS Ja 56 % · Over 2,5 52 % · Under 2,5 48 % (nur Tormodell: BTTS 52 %, Over 2,5 48 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.28 · X 3.5 · 2 3 · BTTS Ja 1.6 · Over 2,5 1.85 · Under 2,5 2.03.

**Markt:** Heim 41 % · Remis 27 % · Auswärts 32 % · BTTS 58 % · Over 52 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 4.5 Torreense – FC Avan Academy | 2026-11-05 20:00 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700921

Analyse-ID: A-20261105-8700921-r1 · Team-IDs: 4835 / 1362 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Estádio Dr. Magalhães Pessoa · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für FC Avan Academy (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-17 bis 2026-10-22, Gast 2026-09-16 bis 2026-10-22; letzte 6: Heim 2026-09-17–2026-10-22, Gast 2026-09-16–2026-10-22.

**Torreense (Heim, ID 4835)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 1 | 3 | 4
Gegentore | 7 | 2 | 5 | 7
Tore/Spiel | 1.33 | 1.00 | 1.50 | 1.33
Gegentore/Spiel | 2.33 | 2.00 | 2.50 | 2.33
xG für/Spiel | 0.81 | 0.38 | 1.03 | 0.81
xG gegen/Spiel | 2.17 | 2.30 | 2.10 | 2.17
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 0/0/1 | 1/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 0.00 | 1.50 | 1.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 67 % | 100 % | 50 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**FC Avan Academy (Gast, ID 1362)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 2 | 1 | 1 | 2
Gegentore | 11 | 8 | 3 | 11
Tore/Spiel | 0.67 | 0.50 | 1.00 | 0.67
Gegentore/Spiel | 3.67 | 4.00 | 3.00 | 3.67
xG für/Spiel | 1.22 | 1.04 | 1.59 | 1.22
xG gegen/Spiel | 2.04 | 2.31 | 1.49 | 2.04
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

**Torreense – Landesliga (Saison-ID 17215, 2026-08-09 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 8 | 3 | 5 | 3
Gegentore | 10 | 5 | 5 | 4
Tore/Spiel | 0.89 | 0.75 | 1.00 | 0.50
Gegentore/Spiel | 1.11 | 1.25 | 1.00 | 0.67
xG für/Spiel | 1.29 | 1.42 | 1.19 | 1.33
xG gegen/Spiel | 1.44 | 1.30 | 1.55 | 1.36
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 2/4/3 | 1/2/1 | 1/2/2 | 2/2/2
Punkte/Spiel | 1.11 | 1.25 | 1.00 | 1.33
BTTS % | 33 % | 25 % | 40 % | 0 %
Over 2,5 % | 44 % | 50 % | 40 % | 17 %
Under 2,5 % | 56 % | 50 % | 60 % | 83 %
Clean Sheets % | 44 % | 50 % | 40 % | 67 %
Failed to Score % | 44 % | 50 % | 40 % | 67 %
BTTS-and-lose % | 11 % | 0 % | 20 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**FC Avan Academy – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 Torreense: 17.09. A Lillestrøm (0.33 PPG) 2:1 · 15.10. H Sunderland (2.33 PPG) 1:2 · 22.10. A Ferencváros (3.00 PPG) 1:4

Letzte 6 FC Avan Academy: 16.09. H Sparta Praha (1.33 PPG) 1:4 · 15.10. A Jagiellonia Białystok (1.00 PPG) 1:3 · 22.10. H AZ (2.00 PPG) 0:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Torreense [2, 1, 1]; FC Avan Academy [1, 1, 0]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von FC Avan Academy (laut API; als Ararat-Armenia gemeldet, Alias nicht von der API bestätigt) im API-Abo fehlt; schwächere Offensive ist Torreense mit 0,81 xG in der Europa League und 3 Toren in den letzten sechs Ligaspielen (67 % torlos), während Avan Academy nur 2 Tore in 3 Spielen erzielte; ein Weg zu drei Toren ist durch alle sechs Over-Spiele beider Teams in der Europa League sichtbar, widerspricht aber Torreenses Liga-Bild mit 17 % Over in den letzten sechs; stärkstes Gegenargument gegen den Modell-Heimsieg (58 %) ist Torreenses negative xG-Bilanz (0,81 zu 2,17), sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 2.125, λ Gast 1.218; xG-Variante λ Heim 1.568, λ Gast 1.308 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 58 % · Remis 21 % · Auswärtssieg 21 % · BTTS Ja 58 % · Over 2,5 55 % · Under 2,5 45 % (nur Tormodell: BTTS 62 %, Over 2,5 65 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.8 · X 3.8 · 2 3.92 · BTTS Ja 1.85 · Over 2,5 2.06 · Under 2,5 1.83.

**Markt:** Heim 52 % · Remis 25 % · Auswärts 24 % · BTTS 50 % · Over 47 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---
