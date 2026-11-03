# Vorabeintrag Batch 3 · 03.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-03 14:33 UTC
- Eintrag erstellt: 2026-11-03 14:37:48 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 3.1 Birmingham City – Millwall | 2026-11-03 20:00 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566291

Analyse-ID: A-20261103-8566291-r1 · Team-IDs: 206 / 229 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: St. Andrew's Stadium

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-31, Gast 2026-08-15 bis 2026-10-31; letzte 6: Heim 2026-09-19–2026-10-31, Gast 2026-09-19–2026-10-31.

**Birmingham City (Heim, ID 206)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 23 | 14 | 9 | 13
Gegentore | 13 | 7 | 6 | 4
Tore/Spiel | 1.77 | 2.33 | 1.29 | 2.17
Gegentore/Spiel | 1.00 | 1.17 | 0.86 | 0.67
xG für/Spiel | 1.55 | 1.62 | 1.48 | 1.63
xG gegen/Spiel | 1.35 | 1.26 | 1.42 | 1.37
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 6/5/2 | 2/4/0 | 4/1/2 | 4/1/1
Punkte/Spiel | 1.77 | 1.67 | 1.86 | 2.17
BTTS % | 62 % | 67 % | 57 % | 33 %
Over 2,5 % | 69 % | 83 % | 57 % | 67 %
Under 2,5 % | 31 % | 17 % | 43 % | 33 %
Clean Sheets % | 31 % | 33 % | 29 % | 50 %
Failed to Score % | 15 % | 0 % | 29 % | 17 %
BTTS-and-lose % | 8 % | 0 % | 14 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Millwall (Gast, ID 229)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 23 | 15 | 8 | 10
Gegentore | 21 | 9 | 12 | 8
Tore/Spiel | 1.77 | 2.14 | 1.33 | 1.67
Gegentore/Spiel | 1.62 | 1.29 | 2.00 | 1.33
xG für/Spiel | 1.57 | 1.66 | 1.45 | 1.66
xG gegen/Spiel | 1.37 | 1.22 | 1.54 | 1.20
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 5/3/5 | 3/2/2 | 2/1/3 | 2/2/2
Punkte/Spiel | 1.38 | 1.57 | 1.17 | 1.33
BTTS % | 54 % | 43 % | 67 % | 67 %
Over 2,5 % | 77 % | 86 % | 67 % | 67 %
Under 2,5 % | 23 % | 14 % | 33 % | 33 %
Clean Sheets % | 31 % | 29 % | 33 % | 17 %
Failed to Score % | 15 % | 29 % | 0 % | 17 %
BTTS-and-lose % | 23 % | 0 % | 50 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Birmingham City: 19.09. H Middlesbrough (2.15 PPG) 2:2 · 10.10. A West Bromwich Albion (1.85 PPG) 1:0 · 13.10. H Preston North End (0.38 PPG) 4:0 · 17.10. H Queens Park Rangers (1.54 PPG) 3:0 · 24.10. A Cardiff City (1.08 PPG) 0:1 · 31.10. A Lincoln City (1.15 PPG) 3:1

Letzte 6 Millwall: 19.09. H West Ham United (1.69 PPG) 2:2 · 10.10. A Preston North End (0.38 PPG) 1:0 · 13.10. H Swansea City (2.00 PPG) 0:1 · 17.10. H Lincoln City (1.15 PPG) 2:2 · 24.10. A Portsmouth (1.46 PPG) 1:2 · 31.10. H Derby County (0.54 PPG) 4:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Birmingham City [0, 2, 2, 1, 2, 1, 2, 2, 1, 4, 3, 0, 3]; Millwall [2, 3, 1, 0, 4, 1, 2, 2, 1, 0, 2, 1, 4]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Millwall auswärts mit 8 Toren in 6, gegen Birminghams Heimabwehr mit 7 Gegentoren in 6; ein Weg zu drei Toren ist mit 83 % bzw. 67 % Over beider Kontexte sichtbar, widerspricht aber dem Modell mit nur 39 % Over und 45 % BTTS; stärkstes Gegenargument gegen den Heimsieg (Modell 41 %) sind Birminghams 4 Remis in 6 Heimspielen, und weil Modell und Kontextwerte sich widersprechen, gibt es keine Auswahl.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.233, λ Gast 1.015. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 41 % · Remis 29 % · Auswärtssieg 30 % · BTTS Ja 45 % · Over 2,5 39 % · Under 2,5 61 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.91 · X 3.6 · 2 3.23 · BTTS Ja 1.65 · Over 2,5 1.8 · Under 2,5 2.

**Auswahl:** keine – Grund siehe Bild.

---

## 3.2 West Bromwich Albion – Southampton | 2026-11-03 20:00 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566645

Analyse-ID: A-20261103-8566645-r1 · Team-IDs: 142 / 146 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: The Hawthorns

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-31, Gast 2026-08-16 bis 2026-10-31; letzte 6: Heim 2026-09-20–2026-10-31, Gast 2026-09-19–2026-10-31.

**West Bromwich Albion (Heim, ID 142)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 19 | 9 | 10 | 9
Gegentore | 14 | 6 | 8 | 7
Tore/Spiel | 1.46 | 1.50 | 1.43 | 1.50
Gegentore/Spiel | 1.08 | 1.00 | 1.14 | 1.17
xG für/Spiel | 1.38 | 1.63 | 1.16 | 1.52
xG gegen/Spiel | 1.41 | 1.05 | 1.71 | 1.51
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 7/3/3 | 3/2/1 | 4/1/2 | 3/1/2
Punkte/Spiel | 1.85 | 1.83 | 1.86 | 1.67
BTTS % | 69 % | 67 % | 71 % | 67 %
Over 2,5 % | 46 % | 33 % | 57 % | 50 %
Under 2,5 % | 54 % | 67 % | 43 % | 50 %
Clean Sheets % | 15 % | 17 % | 14 % | 0 %
Failed to Score % | 15 % | 17 % | 14 % | 33 %
BTTS-and-lose % | 8 % | 0 % | 14 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Southampton (Gast, ID 146)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 28 | 20 | 8 | 10
Gegentore | 13 | 5 | 8 | 5
Tore/Spiel | 2.15 | 2.86 | 1.33 | 1.67
Gegentore/Spiel | 1.00 | 0.71 | 1.33 | 0.83
xG für/Spiel | 1.63 | 1.61 | 1.65 | 1.63
xG gegen/Spiel | 1.58 | 1.46 | 1.71 | 1.58
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 8/3/2 | 6/1/0 | 2/2/2 | 4/1/1
Punkte/Spiel | 2.08 | 2.71 | 1.33 | 2.17
BTTS % | 77 % | 71 % | 83 % | 50 %
Over 2,5 % | 62 % | 71 % | 50 % | 50 %
Under 2,5 % | 38 % | 29 % | 50 % | 50 %
Clean Sheets % | 23 % | 29 % | 17 % | 50 %
Failed to Score % | 8 % | 14 % | 0 % | 17 %
BTTS-and-lose % | 15 % | 0 % | 33 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 West Bromwich Albion: 20.09. A Wolverhampton Wanderers (1.85 PPG) 0:1 · 10.10. H Birmingham City (1.77 PPG) 0:1 · 13.10. A Wrexham (1.08 PPG) 2:1 · 17.10. H Blackburn Rovers (1.38 PPG) 3:2 · 24.10. A Preston North End (0.38 PPG) 1:1 · 31.10. A West Ham United (1.69 PPG) 3:1

Letzte 6 Southampton: 19.09. A Wrexham (1.08 PPG) 1:2 · 11.10. H Portsmouth (1.46 PPG) 1:0 · 14.10. A Norwich City (1.15 PPG) 1:0 · 17.10. H Bolton Wanderers (1.08 PPG) 0:0 · 24.10. A West Ham United (1.69 PPG) 3:2 · 31.10. H Queens Park Rangers (1.54 PPG) 4:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): West Bromwich Albion [2, 3, 1, 1, 1, 1, 1, 0, 0, 2, 3, 1, 3]; Southampton [1, 3, 5, 1, 1, 3, 4, 1, 1, 1, 0, 3, 4]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist West Brom mit 1,46 Toren/Spiel, das in 11 von 13 Spielen traf (daheim 5 von 6) gegen Southampton mit nur 17 % Auswärts-Clean-Sheets, während Southampton in allen 6 Auswärtsspielen traf gegen West Broms Heimabwehr mit 17 % Clean Sheets; der Weg zu drei Toren ist mit 33 % Over in West-Brom-Heimspielen schwach, weshalb BTTS (Modell 56 %) der besser belegte Markt ist; stärkstes Gegenargument sind Southamptons 3 Clean Sheets in den letzten sechs, die den Heimtreffer gefährden und als wesentliche Gefahr gewichtet werden.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.393, λ Gast 1.358. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 38 % · Remis 26 % · Auswärtssieg 36 % · BTTS Ja 56 % · Over 2,5 52 % · Under 2,5 48 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.43 · X 3.5 · 2 3 · BTTS Ja 1.55 · Over 2,5 1.8 · Under 2,5 2.

**Auswahl:** BTTS Ja

⚠️ Southampton mit 3 Clean Sheets in den letzten 6 Spielen – Gefahr für den West-Brom-Treffer.

---

## 3.3 Galatasaray – Stuttgart | 2026-11-03 17:45 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700616

Analyse-ID: A-20261103-8700616-r1 · Team-IDs: 187 / 51 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Rams Global Stadium · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-09 bis 2026-10-21, Gast 2026-09-09 bis 2026-10-20; letzte 6: Heim 2026-09-09–2026-10-21, Gast 2026-09-09–2026-10-20.

**Galatasaray (Heim, ID 187)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 6 | 1 | 5 | 6
Gegentore | 9 | 4 | 5 | 9
Tore/Spiel | 2.00 | 1.00 | 2.50 | 2.00
Gegentore/Spiel | 3.00 | 4.00 | 2.50 | 3.00
xG für/Spiel | 0.96 | 0.62 | 1.12 | 0.96
xG gegen/Spiel | 1.68 | 2.43 | 1.30 | 1.68
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

**Stuttgart (Gast, ID 51)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 7 | 4 | 3 | 7
Gegentore | 2 | 2 | 0 | 2
Tore/Spiel | 2.33 | 2.00 | 3.00 | 2.33
Gegentore/Spiel | 0.67 | 1.00 | 0.00 | 0.67
xG für/Spiel | 1.88 | 1.83 | 1.98 | 1.88
xG gegen/Spiel | 1.15 | 1.08 | 1.29 | 1.15
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 2/1/0 | 1/1/0 | 1/0/0 | 2/1/0
Punkte/Spiel | 2.33 | 2.00 | 3.00 | 2.33
BTTS % | 67 % | 100 % | 0 % | 67 %
Over 2,5 % | 67 % | 50 % | 100 % | 67 %
Under 2,5 % | 33 % | 50 % | 0 % | 33 %
Clean Sheets % | 33 % | 0 % | 100 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Galatasaray – Landesliga (Saison-ID 17265, 2026-08-14 bis 2026-10-30)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 23 | 11 | 12 | 11
Gegentore | 12 | 6 | 6 | 6
Tore/Spiel | 2.30 | 2.20 | 2.40 | 1.83
Gegentore/Spiel | 1.20 | 1.20 | 1.20 | 1.00
xG für/Spiel | 2.26 | 2.98 | 1.54 | 2.18
xG gegen/Spiel | 1.08 | 0.90 | 1.26 | 1.07
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 8/1/1 | 4/1/0 | 4/0/1 | 5/0/1
Punkte/Spiel | 2.50 | 2.60 | 2.40 | 2.50
BTTS % | 50 % | 80 % | 20 % | 33 %
Over 2,5 % | 80 % | 80 % | 80 % | 67 %
Under 2,5 % | 20 % | 20 % | 20 % | 33 %
Clean Sheets % | 40 % | 20 % | 60 % | 50 %
Failed to Score % | 10 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Stuttgart – Landesliga (Saison-ID 17210, 2026-08-28 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 3 | 5 | 6
Tore | 14 | 6 | 8 | 9
Gegentore | 15 | 5 | 10 | 9
Tore/Spiel | 1.75 | 2.00 | 1.60 | 1.50
Gegentore/Spiel | 1.88 | 1.67 | 2.00 | 1.50
xG für/Spiel | 1.82 | 1.87 | 1.79 | 1.82
xG gegen/Spiel | 1.96 | 1.52 | 2.22 | 1.94
Spiele mit xG | 8 | 3 | 5 | 6
S/U/N | 3/0/5 | 1/0/2 | 2/0/3 | 2/0/4
Punkte/Spiel | 1.12 | 1.00 | 1.20 | 1.00
BTTS % | 62 % | 67 % | 60 % | 50 %
Over 2,5 % | 62 % | 67 % | 60 % | 50 %
Under 2,5 % | 38 % | 33 % | 40 % | 50 %
Clean Sheets % | 12 % | 0 % | 20 % | 17 %
Failed to Score % | 25 % | 33 % | 20 % | 33 %
BTTS-and-lose % | 38 % | 33 % | 40 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Galatasaray: 09.09. A Sporting CP (2.00 PPG) 1:3 · 13.10. H FC Barcelona (2.00 PPG) 1:4 · 21.10. A Lille (0.00 PPG) 4:2

Letzte 6 Stuttgart: 09.09. H Viking (0.33 PPG) 3:1 · 14.10. A Slovan Bratislava (0.00 PPG) 3:0 · 20.10. H Atlético Madrid (1.33 PPG) 1:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Galatasaray [1, 1, 4]; Stuttgart [3, 3, 1]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Galatasaray in der Champions League mit 0,96 xG, das aber in allen 3 Spielen traf (6 Tore) und in der Süper Lig daheim in jedem Spiel traf, gegen Stuttgart mit 1,96 xG gegen in der Bundesliga, während Stuttgart in allen 3 Champions-League-Spielen und in 80 % seiner Bundesliga-Auswärtsspiele traf gegen Galatasaray mit 9 Champions-League-Gegentoren in 3 Spielen; der Weg zu drei Toren ist ebenfalls plausibel (Modell 63 %), BTTS ist durch beide eigenen Torserien aber direkter belegt (Modell 63 %); stärkstes Gegenargument ist die kleine Champions-League-Stichprobe mit Stuttgarter Treffern gegen schwächere Gegner (Viking, Slovan), was die Aussagekraft mindert, aber keine konkrete Gefahr für einen der Treffer begründet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.816, λ Gast 1.414. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 47 % · Remis 23 % · Auswärtssieg 30 % · BTTS Ja 63 % · Over 2,5 63 % · Under 2,5 37 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.19 · X 4.1 · 2 2.85 · BTTS Ja 1.36 · Over 2,5 1.37 · Under 2,5 3.18.

**Auswahl:** BTTS Ja

---

## 3.4 Shakhtar Donetsk – Sporting CP | 2026-11-03 17:45 UTC | UEFA Champions League 2026/2027, Spieltag 4 | Match-ID 8700784

Analyse-ID: A-20261103-8700784-r1 · Team-IDs: 80 / 114 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Stamford Bridge · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Shakhtar Donetsk (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-10 bis 2026-10-21, Gast 2026-09-09 bis 2026-10-21; letzte 6: Heim 2026-09-10–2026-10-21, Gast 2026-09-09–2026-10-21.

**Shakhtar Donetsk (Heim, ID 80)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 3 | 1 | 4
Gegentore | 3 | 1 | 2 | 3
Tore/Spiel | 1.33 | 3.00 | 0.50 | 1.33
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 1.14 | 1.27 | 1.07 | 1.14
xG gegen/Spiel | 1.30 | 1.29 | 1.30 | 1.30
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 1/0/0 | 0/1/1 | 1/1/1
Punkte/Spiel | 1.33 | 3.00 | 0.50 | 1.33
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 33 % | 100 % | 0 % | 33 %
Under 2,5 % | 67 % | 0 % | 100 % | 67 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Sporting CP (Gast, ID 114)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 7 | 5 | 2 | 7
Gegentore | 4 | 4 | 0 | 4
Tore/Spiel | 2.33 | 2.50 | 2.00 | 2.33
Gegentore/Spiel | 1.33 | 2.00 | 0.00 | 1.33
xG für/Spiel | 1.33 | 1.32 | 1.34 | 1.33
xG gegen/Spiel | 1.56 | 1.23 | 2.20 | 1.56
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 2/0/1 | 1/0/1 | 1/0/0 | 2/0/1
Punkte/Spiel | 2.00 | 1.50 | 3.00 | 2.00
BTTS % | 67 % | 100 % | 0 % | 67 %
Over 2,5 % | 67 % | 100 % | 0 % | 67 %
Under 2,5 % | 33 % | 0 % | 100 % | 33 %
Clean Sheets % | 33 % | 0 % | 100 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 50 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Shakhtar Donetsk – Landesliga:** fehlt (Liga nicht im API-Abo)

**Sporting CP – Landesliga (Saison-ID 17217, 2026-08-08 bis 2026-10-30)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 23 | 11 | 12 | 11
Gegentore | 11 | 7 | 4 | 6
Tore/Spiel | 2.30 | 2.20 | 2.40 | 1.83
Gegentore/Spiel | 1.10 | 1.40 | 0.80 | 1.00
xG für/Spiel | 1.78 | 1.74 | 1.81 | 1.95
xG gegen/Spiel | 1.05 | 1.05 | 1.05 | 1.10
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 6/3/1 | 3/1/1 | 3/2/0 | 3/2/1
Punkte/Spiel | 2.10 | 2.00 | 2.20 | 1.83
BTTS % | 70 % | 80 % | 60 % | 67 %
Over 2,5 % | 70 % | 80 % | 60 % | 50 %
Under 2,5 % | 30 % | 20 % | 40 % | 50 %
Clean Sheets % | 30 % | 20 % | 40 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 10 % | 20 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Shakhtar Donetsk: 10.09. A PSV (1.33 PPG) 1:1 · 14.10. H AEK Athens (1.00 PPG) 3:1 · 21.10. A Inter Milan (1.00 PPG) 0:1

Letzte 6 Sporting CP: 09.09. H Galatasaray (1.00 PPG) 3:1 · 13.10. A Lens (1.00 PPG) 2:0 · 21.10. H LASK Linz (1.00 PPG) 2:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Shakhtar Donetsk [1, 3, 0]; Sporting CP [3, 2, 2]

**Bild:** Champions League 2026/27 mit je 3 Spielen ist eingeschränkt, weil die ukrainische Liga im API-Abo fehlt und für Shakhtar keine Landesliga-Daten vorliegen; schwächere Offensive ist Shakhtar mit 1,14 xG in der Champions League; ein Weg zu drei Toren ist mit 33 % bzw. 67 % Over in drei Spielen nicht belastbar; stärkstes Gegenargument gegen jede Auswahl ist das ausgeglichene Modell (Heim 37 %, Auswärts 39 %) bei fehlender Ligabasis für Shakhtar, sodass die Datenbasis keinen Markt trägt.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.554, λ Gast 1.591. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 37 % · Remis 24 % · Auswärtssieg 39 % · BTTS Ja 63 % · Over 2,5 61 % · Under 2,5 39 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.6 · X 3.6 · 2 1.91 · BTTS Ja 1.57 · Over 2,5 1.72 · Under 2,5 2.2.

**Auswahl:** keine – Grund siehe Bild.

---

## 3.5 FC Barcelona – Aston Villa | 2026-11-03 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700183

Analyse-ID: A-20261103-8700183-r1 · Team-IDs: 83 / 158 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Camp Nou · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-09 bis 2026-10-20, Gast 2026-09-08 bis 2026-10-21; letzte 6: Heim 2026-09-09–2026-10-20, Gast 2026-09-08–2026-10-21.

**FC Barcelona (Heim, ID 83)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 11 | 5 | 6 | 11
Gegentore | 6 | 1 | 5 | 6
Tore/Spiel | 3.67 | 5.00 | 3.00 | 3.67
Gegentore/Spiel | 2.00 | 1.00 | 2.50 | 2.00
xG für/Spiel | 2.26 | 2.58 | 2.10 | 2.26
xG gegen/Spiel | 1.31 | 0.62 | 1.65 | 1.31
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 2/0/1 | 1/0/0 | 1/0/1 | 2/0/1
Punkte/Spiel | 2.00 | 3.00 | 1.50 | 2.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Aston Villa (Gast, ID 158)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 12 | 9 | 3 | 12
Gegentore | 3 | 1 | 2 | 3
Tore/Spiel | 4.00 | 4.50 | 3.00 | 4.00
Gegentore/Spiel | 1.00 | 0.50 | 2.00 | 1.00
xG für/Spiel | 2.31 | 2.38 | 2.16 | 2.31
xG gegen/Spiel | 1.55 | 1.38 | 1.90 | 1.55
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 3/0/0 | 2/0/0 | 1/0/0 | 3/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 67 % | 50 % | 100 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 33 % | 50 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**FC Barcelona – Landesliga (Saison-ID 17199, 2026-08-23 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 46 | 24 | 22 | 25
Gegentore | 12 | 7 | 5 | 8
Tore/Spiel | 4.18 | 4.00 | 4.40 | 4.17
Gegentore/Spiel | 1.09 | 1.17 | 1.00 | 1.33
xG für/Spiel | 2.30 | 2.47 | 2.09 | 2.36
xG gegen/Spiel | 0.89 | 0.83 | 0.97 | 0.81
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 10/0/1 | 5/0/1 | 5/0/0 | 5/0/1
Punkte/Spiel | 2.73 | 2.50 | 3.00 | 2.50
BTTS % | 64 % | 67 % | 60 % | 83 %
Over 2,5 % | 91 % | 83 % | 100 % | 100 %
Under 2,5 % | 9 % | 17 % | 0 % | 0 %
Clean Sheets % | 36 % | 33 % | 40 % | 17 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 9 % | 17 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Aston Villa – Landesliga (Saison-ID 17146, 2026-08-23 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 10 | 6 | 4 | 10
Gegentore | 13 | 7 | 6 | 8
Tore/Spiel | 1.11 | 1.20 | 1.00 | 1.67
Gegentore/Spiel | 1.44 | 1.40 | 1.50 | 1.33
xG für/Spiel | 1.24 | 1.26 | 1.22 | 1.43
xG gegen/Spiel | 1.76 | 1.66 | 1.87 | 1.88
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 3/3/3 | 1/2/2 | 2/1/1 | 3/2/1
Punkte/Spiel | 1.33 | 1.00 | 1.75 | 1.83
BTTS % | 56 % | 80 % | 25 % | 83 %
Over 2,5 % | 56 % | 60 % | 50 % | 67 %
Under 2,5 % | 44 % | 40 % | 50 % | 33 %
Clean Sheets % | 22 % | 0 % | 50 % | 17 %
Failed to Score % | 33 % | 20 % | 50 % | 0 %
BTTS-and-lose % | 11 % | 20 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 FC Barcelona: 09.09. H Feyenoord (1.00 PPG) 5:1 · 13.10. A Galatasaray (1.00 PPG) 4:1 · 20.10. A PSG (3.00 PPG) 2:4

Letzte 6 Aston Villa: 08.09. A Club Brugge (2.00 PPG) 3:2 · 14.10. H Fenerbahçe (0.67 PPG) 6:0 · 21.10. H Viking (0.33 PPG) 3:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): FC Barcelona [5, 4, 2]; Aston Villa [3, 6, 3]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Aston Villa mit 1,24 xG in der Premier League, aber 12 Toren in 3 Champions-League-Spielen, gegen Barcelona mit 6 Champions-League-Gegentoren in 3; der Weg zu drei Toren ist stark, weil alle 3 Champions-League-Spiele beider Teams Over endeten, Barcelona in der Liga 46 Tore in 11 Spielen (91 % Over) erzielte und auch allein drei Tore liefern kann, und das Modell schätzt 74 %; stärkstes Gegenargument ist Villas defensives Auswärtsprofil in der Premier League (50 % Clean Sheets, 50 % Over), das gegen Barcelonas Torquote aber keine wesentliche Gefahr begründet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 2.331, λ Gast 1.549. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 55 % · Remis 20 % · Auswärtssieg 25 % · BTTS Ja 71 % · Over 2,5 74 % · Under 2,5 26 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.16 · X 7.1 · 2 8.5 · BTTS Ja 1.5 · Over 2,5 1.18 · Under 2,5 4.4.

**Auswahl:** Over 2,5

---
