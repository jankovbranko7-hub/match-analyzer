# Vorabeintrag Batch 2 · 03.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-03 14:33 UTC
- Eintrag erstellt: 2026-11-03 14:37:48 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 2.1 Watford – Lincoln City | 2026-11-03 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566312

Analyse-ID: A-20261103-8566312-r1 · Team-IDs: 155 / 1021 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: Vicarage Road

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-16 bis 2026-10-31, Gast 2026-08-15 bis 2026-10-31; letzte 6: Heim 2026-09-18–2026-10-31, Gast 2026-09-19–2026-10-31.

**Watford (Heim, ID 155)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 12 | 8 | 4 | 5
Gegentore | 23 | 9 | 14 | 14
Tore/Spiel | 0.92 | 1.33 | 0.57 | 0.83
Gegentore/Spiel | 1.77 | 1.50 | 2.00 | 2.33
xG für/Spiel | 1.30 | 1.59 | 1.05 | 1.30
xG gegen/Spiel | 1.77 | 1.69 | 1.83 | 1.95
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 3/2/8 | 3/1/2 | 0/1/6 | 1/0/5
Punkte/Spiel | 0.85 | 1.67 | 0.14 | 0.50
BTTS % | 54 % | 67 % | 43 % | 33 %
Over 2,5 % | 46 % | 67 % | 29 % | 50 %
Under 2,5 % | 54 % | 33 % | 71 % | 50 %
Clean Sheets % | 8 % | 17 % | 0 % | 17 %
Failed to Score % | 38 % | 17 % | 57 % | 50 %
BTTS-and-lose % | 23 % | 17 % | 29 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Lincoln City (Gast, ID 1021)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 14 | 8 | 6 | 8
Gegentore | 23 | 16 | 7 | 17
Tore/Spiel | 1.08 | 1.14 | 1.00 | 1.33
Gegentore/Spiel | 1.77 | 2.29 | 1.17 | 2.83
xG für/Spiel | 1.32 | 1.54 | 1.06 | 1.33
xG gegen/Spiel | 1.78 | 1.73 | 1.84 | 1.82
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 4/3/6 | 1/2/4 | 3/1/2 | 1/1/4
Punkte/Spiel | 1.15 | 0.71 | 1.67 | 0.67
BTTS % | 54 % | 71 % | 33 % | 67 %
Over 2,5 % | 62 % | 71 % | 50 % | 100 %
Under 2,5 % | 38 % | 29 % | 50 % | 0 %
Clean Sheets % | 31 % | 14 % | 50 % | 0 %
Failed to Score % | 23 % | 29 % | 17 % | 33 %
BTTS-and-lose % | 31 % | 43 % | 17 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Watford: 18.09. A Bristol City (1.38 PPG) 0:1 · 10.10. H Burnley (0.69 PPG) 0:4 · 13.10. A Cardiff City (1.08 PPG) 1:5 · 17.10. H Charlton Athletic (1.08 PPG) 2:0 · 24.10. A Wolverhampton Wanderers (1.85 PPG) 0:1 · 31.10. A Norwich City (1.15 PPG) 2:3

Letzte 6 Lincoln City: 19.09. H Swansea City (2.00 PPG) 1:2 · 10.10. A Sheffield United (1.46 PPG) 0:3 · 14.10. H West Ham United (1.69 PPG) 0:6 · 17.10. A Millwall (1.38 PPG) 2:2 · 24.10. H Burnley (0.69 PPG) 4:1 · 31.10. H Birmingham City (1.77 PPG) 1:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Watford [2, 1, 1, 0, 0, 2, 1, 0, 0, 1, 2, 0, 2]; Lincoln City [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 2, 4, 1]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Lincoln auswärts mit 6 Toren in 6 und 1,06 xG, gegen Watfords Heimabwehr mit 1,69 xG gegen; ein Weg zu drei Toren ist mit 67 % Over in Watford-Heimspielen gegen 50 % in Lincoln-Auswärtsspielen unklar; stärkstes Gegenargument gegen den Modell-Heimsieg (47 %) ist Watfords Form mit 1-0-5 in den letzten sechs, während auch Lincoln dort 1-1-4 steht, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.548, λ Gast 1.126. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 47 % · Remis 25 % · Auswärtssieg 28 % · BTTS Ja 53 % · Over 2,5 50 % · Under 2,5 50 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.45 · X 3.4 · 2 2.65 · BTTS Ja 1.7 · Over 2,5 1.77 · Under 2,5 1.95.

**Auswahl:** keine – Grund siehe Bild.

---

## 2.2 Blackburn Rovers – Stoke City | 2026-11-03 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566349

Analyse-ID: A-20261103-8566349-r1 · Team-IDs: 216 / 141 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: Ewood Park

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-14 bis 2026-10-31, Gast 2026-08-15 bis 2026-10-31; letzte 6: Heim 2026-09-19–2026-10-31, Gast 2026-09-19–2026-10-31.

**Blackburn Rovers (Heim, ID 216)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 19 | 11 | 8 | 9
Gegentore | 20 | 7 | 13 | 10
Tore/Spiel | 1.46 | 1.83 | 1.14 | 1.50
Gegentore/Spiel | 1.54 | 1.17 | 1.86 | 1.67
xG für/Spiel | 1.25 | 1.60 | 0.95 | 1.11
xG gegen/Spiel | 1.77 | 1.59 | 1.91 | 2.01
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 5/3/5 | 4/0/2 | 1/3/3 | 3/1/2
Punkte/Spiel | 1.38 | 2.00 | 0.86 | 1.67
BTTS % | 69 % | 83 % | 57 % | 50 %
Over 2,5 % | 77 % | 83 % | 71 % | 67 %
Under 2,5 % | 23 % | 17 % | 29 % | 33 %
Clean Sheets % | 23 % | 17 % | 29 % | 33 %
Failed to Score % | 15 % | 0 % | 29 % | 17 %
BTTS-and-lose % | 31 % | 33 % | 29 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Stoke City (Gast, ID 141)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 20 | 12 | 8 | 9
Gegentore | 16 | 6 | 10 | 5
Tore/Spiel | 1.54 | 1.71 | 1.33 | 1.50
Gegentore/Spiel | 1.23 | 0.86 | 1.67 | 0.83
xG für/Spiel | 1.28 | 1.22 | 1.34 | 1.26
xG gegen/Spiel | 1.56 | 1.21 | 1.97 | 1.49
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 7/2/4 | 4/1/2 | 3/1/2 | 4/1/1
Punkte/Spiel | 1.77 | 1.86 | 1.67 | 2.17
BTTS % | 62 % | 43 % | 83 % | 50 %
Over 2,5 % | 62 % | 57 % | 67 % | 50 %
Under 2,5 % | 38 % | 43 % | 33 % | 50 %
Clean Sheets % | 38 % | 57 % | 17 % | 50 %
Failed to Score % | 8 % | 14 % | 0 % | 17 %
BTTS-and-lose % | 31 % | 29 % | 33 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Blackburn Rovers: 19.09. A Portsmouth (1.46 PPG) 2:2 · 10.10. H Cardiff City (1.08 PPG) 2:1 · 13.10. A Bristol City (1.38 PPG) 1:0 · 17.10. A West Bromwich Albion (1.85 PPG) 2:3 · 24.10. H Wrexham (1.08 PPG) 2:0 · 31.10. A Swansea City (2.00 PPG) 0:4

Letzte 6 Stoke City: 19.09. H Sheffield United (1.46 PPG) 2:1 · 10.10. A Bolton Wanderers (1.08 PPG) 2:1 · 13.10. H Middlesbrough (2.15 PPG) 2:3 · 17.10. A Derby County (0.54 PPG) 1:0 · 24.10. H Bristol City (1.38 PPG) 0:0 · 31.10. H Preston North End (0.38 PPG) 2:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Blackburn Rovers [2, 2, 1, 0, 1, 1, 3, 2, 2, 1, 2, 2, 0]; Stoke City [1, 1, 1, 1, 4, 1, 2, 2, 2, 2, 1, 0, 2]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Blackburn mit 1,25 xG (letzte sechs 1,11), das aber in allen 6 Heimspielen traf (11 Tore) gegen Stoke mit nur 17 % Auswärts-Clean-Sheets, während Stoke in allen 6 Auswärtsspielen traf gegen Blackburns Heimabwehr mit 17 % Clean Sheets; der Weg zu drei Toren ist mit 83 % bzw. 67 % Over ebenfalls plausibel, BTTS ist durch beide eigenen Torserien aber direkter belegt, obwohl das Modell nur 45 % schätzt; stärkstes Gegenargument sind Stokes 50 % Clean Sheets in den letzten sechs und Blackburns niedrige Chancenwerte zuletzt, was als wesentliche Gefahr für den Heimtreffer gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.279, λ Gast 0.984. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 43 % · Remis 28 % · Auswärtssieg 29 % · BTTS Ja 45 % · Over 2,5 39 % · Under 2,5 61 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.45 · X 3.25 · 2 2.4 · BTTS Ja 1.75 · Over 2,5 2.06 · Under 2,5 1.8.

**Auswahl:** BTTS Ja

⚠️ Stoke mit 3 Clean Sheets in den letzten 6 Spielen und Blackburn zuletzt nur 1,11 xG – Gefahr für den Heimtreffer; Modell nur 45 %.

---

## 2.3 Queens Park Rangers – Burnley | 2026-11-03 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566566

Analyse-ID: A-20261103-8566566-r1 · Team-IDs: 160 / 145 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: MATRADE Loftus Road

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-31, Gast 2026-08-16 bis 2026-10-31; letzte 6: Heim 2026-09-19–2026-10-31, Gast 2026-09-19–2026-10-31.

**Queens Park Rangers (Heim, ID 160)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 21 | 13 | 8 | 13
Gegentore | 16 | 5 | 11 | 11
Tore/Spiel | 1.62 | 2.17 | 1.14 | 2.17
Gegentore/Spiel | 1.23 | 0.83 | 1.57 | 1.83
xG für/Spiel | 1.60 | 1.96 | 1.28 | 1.50
xG gegen/Spiel | 1.41 | 1.26 | 1.54 | 1.55
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 5/5/3 | 3/2/1 | 2/3/2 | 2/2/2
Punkte/Spiel | 1.54 | 1.83 | 1.29 | 1.33
BTTS % | 62 % | 50 % | 71 % | 67 %
Over 2,5 % | 62 % | 67 % | 57 % | 83 %
Under 2,5 % | 38 % | 33 % | 43 % | 17 %
Clean Sheets % | 23 % | 33 % | 14 % | 17 %
Failed to Score % | 31 % | 33 % | 29 % | 17 %
BTTS-and-lose % | 8 % | 0 % | 14 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Burnley (Gast, ID 145)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 17 | 8 | 9 | 9
Gegentore | 25 | 10 | 15 | 9
Tore/Spiel | 1.31 | 1.14 | 1.50 | 1.50
Gegentore/Spiel | 1.92 | 1.43 | 2.50 | 1.50
xG für/Spiel | 1.47 | 1.41 | 1.54 | 1.46
xG gegen/Spiel | 1.56 | 1.37 | 1.78 | 1.58
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 1/6/6 | 0/5/2 | 1/1/4 | 1/3/2
Punkte/Spiel | 0.69 | 0.71 | 0.67 | 1.00
BTTS % | 85 % | 86 % | 83 % | 67 %
Over 2,5 % | 69 % | 57 % | 83 % | 67 %
Under 2,5 % | 31 % | 43 % | 17 % | 33 %
Clean Sheets % | 15 % | 14 % | 17 % | 33 %
Failed to Score % | 8 % | 14 % | 0 % | 17 %
BTTS-and-lose % | 46 % | 29 % | 67 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Queens Park Rangers: 19.09. H Preston North End (0.38 PPG) 2:2 · 09.10. A West Ham United (1.69 PPG) 1:1 · 14.10. H Derby County (0.54 PPG) 4:1 · 17.10. A Birmingham City (1.77 PPG) 0:3 · 24.10. H Swansea City (2.00 PPG) 5:0 · 31.10. A Southampton (2.08 PPG) 1:4

Letzte 6 Burnley: 19.09. H Derby County (0.54 PPG) 1:1 · 10.10. A Watford (0.85 PPG) 4:0 · 13.10. H Charlton Athletic (1.08 PPG) 2:2 · 16.10. H Wolverhampton Wanderers (1.85 PPG) 1:2 · 24.10. A Lincoln City (1.15 PPG) 1:4 · 31.10. H Portsmouth (1.46 PPG) 0:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Queens Park Rangers [3, 0, 2, 2, 0, 0, 1, 2, 1, 4, 0, 5, 1]; Burnley [2, 1, 1, 1, 1, 1, 1, 1, 4, 2, 1, 1, 0]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist QPR daheim mit 33 % torlosen Spielen trotz 1,96 xG, gegen Burnleys Abwehr mit 25 Gegentoren; ein Weg zu drei Toren ist mit 67 % bzw. 83 % Over beider Kontexte sichtbar, widerspricht aber dem Modell (38 %); stärkstes Gegenargument ist der ungeklärte Widerspruch zwischen dem Modell-Auswärtssieg (47 %, geprägt von früheren Saisons) und Burnleys Saisonbilanz von 1-6-6 mit 0,69 Punkten pro Spiel, der eine Auswahl verhindert.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 0.888, λ Gast 1.321. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 25 % · Remis 28 % · Auswärtssieg 47 % · BTTS Ja 43 % · Over 2,5 38 % · Under 2,5 62 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.02 · X 3.7 · 2 2.98 · BTTS Ja 1.57 · Over 2,5 1.65 · Under 2,5 2.2.

**Auswahl:** keine – Grund siehe Bild.

---

## 2.4 Derby County – Norwich City | 2026-11-03 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566607

Analyse-ID: A-20261103-8566607-r1 · Team-IDs: 213 / 159 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: Pride Park Stadium

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-31, Gast 2026-08-15 bis 2026-10-31; letzte 6: Heim 2026-09-19–2026-10-31, Gast 2026-09-20–2026-10-31.

**Derby County (Heim, ID 213)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 11 | 4 | 7 | 5
Gegentore | 25 | 10 | 15 | 12
Tore/Spiel | 0.85 | 0.67 | 1.00 | 0.83
Gegentore/Spiel | 1.92 | 1.67 | 2.14 | 2.00
xG für/Spiel | 1.45 | 1.59 | 1.33 | 1.50
xG gegen/Spiel | 1.75 | 1.61 | 1.87 | 1.68
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 1/4/8 | 0/2/4 | 1/2/4 | 0/3/3
Punkte/Spiel | 0.54 | 0.33 | 0.71 | 0.50
BTTS % | 62 % | 50 % | 71 % | 83 %
Over 2,5 % | 54 % | 50 % | 57 % | 33 %
Under 2,5 % | 46 % | 50 % | 43 % | 67 %
Clean Sheets % | 8 % | 0 % | 14 % | 0 %
Failed to Score % | 31 % | 50 % | 14 % | 17 %
BTTS-and-lose % | 31 % | 17 % | 43 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Norwich City (Gast, ID 159)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 23 | 13 | 10 | 10
Gegentore | 24 | 12 | 12 | 11
Tore/Spiel | 1.77 | 1.86 | 1.67 | 1.67
Gegentore/Spiel | 1.85 | 1.71 | 2.00 | 1.83
xG für/Spiel | 1.59 | 1.62 | 1.56 | 1.42
xG gegen/Spiel | 1.34 | 1.25 | 1.45 | 1.25
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 5/0/8 | 3/0/4 | 2/0/4 | 2/0/4
Punkte/Spiel | 1.15 | 1.29 | 1.00 | 1.00
BTTS % | 69 % | 71 % | 67 % | 67 %
Over 2,5 % | 77 % | 71 % | 83 % | 67 %
Under 2,5 % | 23 % | 29 % | 17 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 31 % | 29 % | 33 % | 33 %
BTTS-and-lose % | 31 % | 29 % | 33 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Derby County: 19.09. A Burnley (0.69 PPG) 1:1 · 10.10. H Wrexham (1.08 PPG) 1:1 · 14.10. A Queens Park Rangers (1.54 PPG) 1:4 · 17.10. H Stoke City (1.77 PPG) 0:1 · 24.10. A Sheffield United (1.46 PPG) 1:1 · 31.10. A Millwall (1.38 PPG) 1:4

Letzte 6 Norwich City: 20.09. H Bolton Wanderers (1.08 PPG) 3:4 · 10.10. A Swansea City (2.00 PPG) 1:2 · 14.10. H Southampton (2.08 PPG) 0:1 · 17.10. H Portsmouth (1.46 PPG) 0:1 · 24.10. A Charlton Athletic (1.08 PPG) 3:1 · 31.10. H Watford (0.85 PPG) 3:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Derby County [1, 2, 0, 2, 0, 0, 1, 1, 1, 1, 0, 1, 1]; Norwich City [1, 0, 4, 0, 3, 2, 3, 3, 1, 0, 0, 3, 3]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Derby mit 4 Toren in 6 Heimspielen und 50 % torlosen Heimspielen, gegen Norwich ohne Clean Sheet in 13 Spielen; der Weg zu drei Toren läuft über Norwichs Offensive (1,77 Tore/Spiel) gegen Derbys Abwehr (1,92 Gegentore/Spiel) und notfalls einseitig, mit 77 % Over in Norwich-Spielen (auswärts 83 %), das Modell schätzt 55 %; stärkstes Gegenargument ist Derbys schwache Heimoffensive, die den beidseitigen Weg erschwert und als wesentliche Gefahr gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.477, λ Gast 1.401. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 39 % · Remis 25 % · Auswärtssieg 36 % · BTTS Ja 58 % · Over 2,5 55 % · Under 2,5 45 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.3 · X 3.7 · 2 2.05 · BTTS Ja 1.53 · Over 2,5 1.65 · Under 2,5 2.2.

**Auswahl:** Over 2,5

⚠️ Derby erzielte daheim nur 4 Tore in 6 Spielen (50 % torlos) – Over hängt dann weitgehend an Norwich.

---

## 2.5 Charlton Athletic – Bolton Wanderers | 2026-11-03 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566634

Analyse-ID: A-20261103-8566634-r1 · Team-IDs: 225 / 226 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: The Valley

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-31, Gast 2026-08-15 bis 2026-10-31; letzte 6: Heim 2026-09-19–2026-10-31, Gast 2026-09-20–2026-10-31.

**Charlton Athletic (Heim, ID 225)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 11 | 5 | 6 | 5
Gegentore | 21 | 5 | 16 | 14
Tore/Spiel | 0.85 | 0.83 | 0.86 | 0.83
Gegentore/Spiel | 1.62 | 0.83 | 2.29 | 2.33
xG für/Spiel | 1.11 | 1.28 | 0.97 | 1.12
xG gegen/Spiel | 1.81 | 1.40 | 2.16 | 1.96
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 3/5/5 | 2/3/1 | 1/2/4 | 0/2/4
Punkte/Spiel | 1.08 | 1.50 | 0.71 | 0.33
BTTS % | 54 % | 50 % | 57 % | 67 %
Over 2,5 % | 54 % | 33 % | 71 % | 67 %
Under 2,5 % | 46 % | 67 % | 29 % | 33 %
Clean Sheets % | 23 % | 50 % | 0 % | 0 %
Failed to Score % | 38 % | 33 % | 43 % | 33 %
BTTS-and-lose % | 15 % | 17 % | 14 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Bolton Wanderers (Gast, ID 226)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 18 | 9 | 9 | 11
Gegentore | 26 | 15 | 11 | 14
Tore/Spiel | 1.38 | 1.29 | 1.50 | 1.83
Gegentore/Spiel | 2.00 | 2.14 | 1.83 | 2.33
xG für/Spiel | 1.54 | 1.82 | 1.21 | 1.63
xG gegen/Spiel | 1.65 | 1.66 | 1.63 | 1.76
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 4/2/7 | 2/0/5 | 2/2/2 | 2/1/3
Punkte/Spiel | 1.08 | 0.86 | 1.33 | 1.17
BTTS % | 62 % | 71 % | 50 % | 83 %
Over 2,5 % | 69 % | 71 % | 67 % | 83 %
Under 2,5 % | 31 % | 29 % | 33 % | 17 %
Clean Sheets % | 23 % | 14 % | 33 % | 17 %
Failed to Score % | 31 % | 14 % | 50 % | 17 %
BTTS-and-lose % | 38 % | 57 % | 17 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Charlton Athletic: 19.09. A Cardiff City (1.08 PPG) 1:3 · 10.10. H Bristol City (1.38 PPG) 1:1 · 13.10. A Burnley (0.69 PPG) 2:2 · 17.10. A Watford (0.85 PPG) 0:2 · 24.10. H Norwich City (1.15 PPG) 1:3 · 31.10. A Middlesbrough (2.15 PPG) 0:3

Letzte 6 Bolton Wanderers: 20.09. A Norwich City (1.15 PPG) 4:3 · 10.10. H Stoke City (1.77 PPG) 1:2 · 13.10. A Wolverhampton Wanderers (1.85 PPG) 3:1 · 17.10. A Southampton (2.08 PPG) 0:0 · 23.10. H Middlesbrough (2.15 PPG) 1:5 · 31.10. H Bristol City (1.38 PPG) 2:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Charlton Athletic [2, 2, 1, 1, 0, 0, 0, 1, 1, 2, 0, 1, 0]; Bolton Wanderers [2, 0, 0, 2, 0, 2, 1, 4, 1, 3, 0, 1, 2]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Charlton mit 0,85 Toren/Spiel und 1,11 xG, gegen Boltons Abwehr mit 1,65 xG gegen; ein Weg zu drei Toren ist mit 33 % Over in Charlton-Heimspielen gegen 67 % in Bolton-Auswärtsspielen widersprüchlich; stärkstes Gegenargument gegen den Modell-Heimsieg (42 %) ist Charltons Form mit 0-2-4 in den letzten sechs, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.400, λ Gast 1.176. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 42 % · Remis 26 % · Auswärtssieg 32 % · BTTS Ja 52 % · Over 2,5 48 % · Under 2,5 52 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.25 · X 3.63 · 2 3 · BTTS Ja 1.57 · Over 2,5 1.78 · Under 2,5 2.

**Auswahl:** keine – Grund siehe Bild.

---
