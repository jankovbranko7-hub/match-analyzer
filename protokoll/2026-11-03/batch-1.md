# Vorabeintrag Batch 1 · 03.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-03 14:33 UTC
- Eintrag erstellt: 2026-11-03 14:37:48 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 1.1 Aurora – Independiente Petrolero | Bolivien LFPB

**Bild:** Spielidentität ungeklärt: Die API führt Aurora – Independiente Petrolero (Match-ID 8733223) erst am 04.12.2026, für den 03.11.2026 ist die Begegnung im Spielplan nicht vorhanden; nach Abschnitt 2 wird sie nicht geraten, deshalb keine Analyse und keine Auswahl.

**Auswahl:** keine

---

## 1.2 Chapecoense – Mirassol | 2026-11-03 22:30 UTC | Brasilien Série A 2026, Spieltag 34 | Match-ID 8409599

Analyse-ID: A-20261103-8409599-r1 · Team-IDs: 623 / 2721 · Saison-ID: 16544 · Status beim Abruf: incomplete · Ort: Arena Condá

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026: 32 bzw. 33 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-01-28 bis 2026-10-28, Gast 2026-01-29 bis 2026-10-30; letzte 6: Heim 2026-09-19–2026-10-28, Gast 2026-09-19–2026-10-30.

**Chapecoense (Heim, ID 623)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 32 | 15 | 17 | 6
Tore | 32 | 21 | 11 | 4
Gegentore | 66 | 34 | 32 | 14
Tore/Spiel | 1.00 | 1.40 | 0.65 | 0.67
Gegentore/Spiel | 2.06 | 2.27 | 1.88 | 2.33
xG für/Spiel | 1.29 | 1.50 | 1.11 | 1.19
xG gegen/Spiel | 1.90 | 1.58 | 2.18 | 2.23
Spiele mit xG | 32 | 15 | 17 | 6
S/U/N | 4/9/19 | 3/5/7 | 1/4/12 | 1/1/4
Punkte/Spiel | 0.66 | 0.93 | 0.41 | 0.67
BTTS % | 62 % | 73 % | 53 % | 50 %
Over 2,5 % | 59 % | 73 % | 47 % | 67 %
Under 2,5 % | 41 % | 27 % | 53 % | 33 %
Clean Sheets % | 6 % | 13 % | 0 % | 0 %
Failed to Score % | 34 % | 20 % | 47 % | 50 %
BTTS-and-lose % | 28 % | 33 % | 24 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Mirassol (Gast, ID 2721)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 17 | 16 | 6
Tore | 37 | 24 | 13 | 6
Gegentore | 47 | 22 | 25 | 5
Tore/Spiel | 1.12 | 1.41 | 0.81 | 1.00
Gegentore/Spiel | 1.42 | 1.29 | 1.56 | 0.83
xG für/Spiel | 1.47 | 1.79 | 1.13 | 1.30
xG gegen/Spiel | 1.62 | 1.36 | 1.90 | 2.14
Spiele mit xG | 33 | 17 | 16 | 6
S/U/N | 9/10/14 | 7/6/4 | 2/4/10 | 2/2/2
Punkte/Spiel | 1.12 | 1.59 | 0.62 | 1.33
BTTS % | 64 % | 71 % | 56 % | 33 %
Over 2,5 % | 45 % | 53 % | 38 % | 0 %
Under 2,5 % | 55 % | 47 % | 62 % | 100 %
Clean Sheets % | 9 % | 18 % | 0 % | 33 %
Failed to Score % | 27 % | 12 % | 44 % | 33 %
BTTS-and-lose % | 15 % | 12 % | 19 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Chapecoense: 19.09. A Atlético Mineiro (1.52 PPG) 1:1 · 07.10. A Vitória (1.15 PPG) 0:4 · 12.10. H Atlético PR (1.64 PPG) 1:4 · 17.10. A Botafogo (1.18 PPG) 0:1 · 24.10. H Fluminense (1.64 PPG) 2:1 · 28.10. A Bragantino (1.38 PPG) 0:3

Letzte 6 Mirassol: 19.09. H Botafogo (1.18 PPG) 2:0 · 07.10. A Bragantino (1.38 PPG) 1:1 · 11.10. A Bahia (1.61 PPG) 0:1 · 16.10. H Internacional (1.06 PPG) 2:0 · 24.10. H São Paulo (1.30 PPG) 1:1 · 30.10. A Corinthians (1.09 PPG) 0:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Chapecoense [4, 1, 3, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 2, 1, 3, 1, 1, 2, 1, 1, 0, 1, 0, 2, 0]; Mirassol [2, 2, 2, 2, 0, 0, 0, 2, 0, 1, 2, 0, 2, 1, 1, 1, 0, 2, 1, 2, 1, 1, 1, 1, 0, 2, 2, 2, 1, 0, 2, 1, 0]

**Bild:** Saison 2026 mit 32 bzw. 33 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Mirassol auswärts mit 13 Toren in 16 und 1,13 xG, gegen eine Chapecoense-Heimabwehr mit 34 Gegentoren in 15 und nur 13 % Clean Sheets, während Chapecoense daheim in 12 von 15 Spielen traf (21 Tore) gegen Mirassols Auswärtsabwehr ohne Clean Sheet; der Weg zu drei Toren ist mit 73 % Over in Chapecoense-Heimspielen möglich, aber Mirassol hatte in den letzten sechs kein Over-Spiel, weshalb BTTS besser belegt ist (Modell 57 %); stärkstes Gegenargument ist Mirassols Torlosigkeit in 44 % der Auswärtsspiele, die den Gästetreffer unmittelbar gefährdet, gegen die schwächste Heimabwehr der Paarung aber nicht überwiegt.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1470 Spiele, Saisons [9035, 11321, 14231, 16544]; Schätzung λ Heim 1.222, λ Gast 1.649. Prüfstand (unberührter Test, 147 Spiele ab 2026-07-22): Heimsieg besser als Grundrate (Brier 0.231 gegen 0.2493); Auswärtssieg besser als Grundrate (Brier 0.1778 gegen 0.1884); BTTS Ja nicht besser als Grundrate (Brier 0.2532 gegen 0.2486); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2539 gegen 0.2527). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 28 % · Remis 24 % · Auswärtssieg 47 % · BTTS Ja 57 % · Over 2,5 55 % · Under 2,5 45 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.4 · X 3.35 · 2 2.15 · BTTS Ja 1.67 · Over 2,5 1.85 · Under 2,5 1.94.

**Auswahl:** BTTS Ja

⚠️ Mirassol blieb in 7 von 16 Auswärtsspielen torlos – Gefahr für den benötigten Gästetreffer.

---

## 1.3 Mushuc Runa SC – Manta FC | 2026-11-03 20:30 UTC | Ecuador Serie A 2026, Spieltag 5 | Match-ID 8714468

Analyse-ID: A-20261103-8714468-r1 · Team-IDs: 4330 / 4334 · Saison-ID: 16714 · Status beim Abruf: incomplete · Ort: fehlt · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026: 34 bzw. 34 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-02-21 bis 2026-10-26, Gast 2026-02-24 bis 2026-10-24; letzte 6: Heim 2026-09-08–2026-10-26, Gast 2026-09-08–2026-10-24.

**Mushuc Runa SC (Heim, ID 4330)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 34 | 16 | 18 | 6
Tore | 39 | 17 | 22 | 6
Gegentore | 46 | 15 | 31 | 12
Tore/Spiel | 1.15 | 1.06 | 1.22 | 1.00
Gegentore/Spiel | 1.35 | 0.94 | 1.72 | 2.00
xG für/Spiel | 1.39 | 1.53 | 1.26 | 1.39
xG gegen/Spiel | 1.25 | 1.15 | 1.34 | 1.54
Spiele mit xG | 34 | 16 | 18 | 6
S/U/N | 9/13/12 | 6/7/3 | 3/6/9 | 0/3/3
Punkte/Spiel | 1.18 | 1.56 | 0.83 | 0.50
BTTS % | 59 % | 44 % | 72 % | 83 %
Over 2,5 % | 50 % | 31 % | 67 % | 50 %
Under 2,5 % | 50 % | 69 % | 33 % | 50 %
Clean Sheets % | 32 % | 50 % | 17 % | 0 %
Failed to Score % | 26 % | 31 % | 22 % | 17 %
BTTS-and-lose % | 26 % | 12 % | 39 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Manta FC (Gast, ID 4334)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 34 | 18 | 16 | 6
Tore | 22 | 10 | 12 | 5
Gegentore | 49 | 17 | 32 | 8
Tore/Spiel | 0.65 | 0.56 | 0.75 | 0.83
Gegentore/Spiel | 1.44 | 0.94 | 2.00 | 1.33
xG für/Spiel | 1.16 | 1.37 | 0.92 | 1.42
xG gegen/Spiel | 1.44 | 1.11 | 1.81 | 1.26
Spiele mit xG | 34 | 18 | 16 | 6
S/U/N | 7/6/21 | 5/4/9 | 2/2/12 | 2/1/3
Punkte/Spiel | 0.79 | 1.06 | 0.50 | 1.17
BTTS % | 32 % | 22 % | 44 % | 33 %
Over 2,5 % | 29 % | 17 % | 44 % | 33 %
Under 2,5 % | 71 % | 83 % | 56 % | 67 %
Clean Sheets % | 21 % | 33 % | 6 % | 33 %
Failed to Score % | 56 % | 61 % | 50 % | 50 %
BTTS-and-lose % | 15 % | 6 % | 25 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Mushuc Runa SC: 08.09. H Leones del Norte (1.31 PPG) 1:1 · 12.09. A Guayaquil City FC (1.34 PPG) 1:3 · 20.09. A Deportivo Cuenca (1.26 PPG) 1:1 · 09.10. A Delfin SC (1.09 PPG) 2:3 · 19.10. H Orense SC (1.11 PPG) 1:1 · 26.10. A Técnico Universitario (1.06 PPG) 0:3

Letzte 6 Manta FC: 08.09. A CS Emelec (1.20 PPG) 0:1 · 12.09. H SD Aucas (1.54 PPG) 0:0 · 21.09. H Orense SC (1.11 PPG) 2:1 · 10.10. H Técnico Universitario (1.06 PPG) 1:0 · 18.10. A Delfin SC (1.09 PPG) 2:4 · 24.10. H Deportivo Cuenca (1.26 PPG) 0:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Mushuc Runa SC [1, 0, 1, 0, 2, 2, 2, 1, 1, 1, 4, 0, 1, 1, 2, 0, 3, 1, 1, 2, 1, 0, 2, 3, 0, 0, 1, 0, 1, 1, 1, 2, 1, 0]; Manta FC [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 0, 2, 1, 2, 0]

**Bild:** Saison 2026 mit je 34 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Manta auswärts mit 12 Toren in 16 Spielen, 0,92 xG und 50 % torlosen Spielen, gegen Mushuc Runas Heimabwehr mit 50 % Clean Sheets; der Weg zu drei Toren ist mit 31 % Over in Mushuc-Heimspielen schwach und wird nicht gewählt; stärkstes Gegenargument ist Mushuc Runas Form ohne Sieg in den letzten sechs Spielen (0-3-3) und 7 Remis in 16 Heimspielen, was das Remisrisiko erhöht, gegen Mantas Auswärtsbilanz von 2-2-12 den Heimsieg (Modell 54 %) aber nicht entkräftet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1069 Spiele, Saisons [8934, 11157, 15842, 16714]; Schätzung λ Heim 1.680, λ Gast 0.980. Prüfstand (unberührter Test, 107 Spiele ab 2026-07-26): Heimsieg besser als Grundrate (Brier 0.2391 gegen 0.249); Auswärtssieg besser als Grundrate (Brier 0.1936 gegen 0.2019); BTTS Ja nicht besser als Grundrate (Brier 0.2607 gegen 0.2508); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2614 gegen 0.2516). Grenzen: 4 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 54 % · Remis 24 % · Auswärtssieg 22 % · BTTS Ja 51 % · Over 2,5 50 % · Under 2,5 50 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.52 · X 3.7 · 2 5.5 · BTTS Ja 1.95 · Over 2,5 1.9 · Under 2,5 1.77.

**Auswahl:** Heimsieg

⚠️ Mushuc Runa ohne Sieg in den letzten 6 Spielen (0-3-3) und 7 Remis in 16 Heimspielen.

---

## 1.4 Portsmouth – Swansea City | 2026-11-03 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566286

Analyse-ID: A-20261103-8566286-r1 · Team-IDs: 272 / 154 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: Fratton Park

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-31, Gast 2026-08-15 bis 2026-10-31; letzte 6: Heim 2026-10-11–2026-10-31, Gast 2026-09-19–2026-10-31.

**Portsmouth (Heim, ID 272)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 16 | 10 | 6 | 7
Gegentore | 15 | 10 | 5 | 5
Tore/Spiel | 1.23 | 1.67 | 0.86 | 1.17
Gegentore/Spiel | 1.15 | 1.67 | 0.71 | 0.83
xG für/Spiel | 1.46 | 1.82 | 1.15 | 1.21
xG gegen/Spiel | 1.29 | 1.30 | 1.28 | 1.25
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 5/4/4 | 3/1/2 | 2/3/2 | 3/2/1
Punkte/Spiel | 1.46 | 1.67 | 1.29 | 1.83
BTTS % | 54 % | 67 % | 43 % | 50 %
Over 2,5 % | 46 % | 67 % | 29 % | 33 %
Under 2,5 % | 54 % | 33 % | 71 % | 67 %
Clean Sheets % | 31 % | 17 % | 43 % | 33 %
Failed to Score % | 31 % | 17 % | 43 % | 33 %
BTTS-and-lose % | 15 % | 17 % | 14 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Swansea City (Gast, ID 154)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 20 | 11 | 9 | 9
Gegentore | 13 | 3 | 10 | 8
Tore/Spiel | 1.54 | 1.57 | 1.50 | 1.50
Gegentore/Spiel | 1.00 | 0.43 | 1.67 | 1.33
xG für/Spiel | 1.44 | 1.50 | 1.35 | 1.42
xG gegen/Spiel | 1.16 | 1.15 | 1.17 | 1.17
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 8/2/3 | 4/2/1 | 4/0/2 | 4/0/2
Punkte/Spiel | 2.00 | 2.00 | 2.00 | 2.00
BTTS % | 38 % | 29 % | 50 % | 33 %
Over 2,5 % | 62 % | 43 % | 83 % | 67 %
Under 2,5 % | 38 % | 57 % | 17 % | 33 %
Clean Sheets % | 46 % | 57 % | 33 % | 33 %
Failed to Score % | 31 % | 43 % | 17 % | 33 %
BTTS-and-lose % | 8 % | 0 % | 17 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Portsmouth: 11.10. A Southampton (2.08 PPG) 0:1 · 14.10. H Sheffield United (1.46 PPG) 3:2 · 17.10. A Norwich City (1.15 PPG) 1:0 · 20.10. A Wolverhampton Wanderers (1.85 PPG) 1:1 · 24.10. H Millwall (1.38 PPG) 2:1 · 31.10. A Burnley (0.69 PPG) 0:0

Letzte 6 Swansea City: 19.09. A Lincoln City (1.15 PPG) 2:1 · 10.10. H Norwich City (1.15 PPG) 2:1 · 13.10. A Millwall (1.38 PPG) 1:0 · 17.10. H West Ham United (1.69 PPG) 0:1 · 24.10. A Queens Park Rangers (1.54 PPG) 0:5 · 31.10. H Blackburn Rovers (1.38 PPG) 4:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Portsmouth [1, 3, 1, 0, 2, 0, 2, 0, 3, 1, 1, 2, 0]; Swansea City [2, 0, 3, 2, 0, 1, 3, 2, 2, 1, 0, 0, 4]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Swansea mit 1,44 xG, gegen Portsmouths Heimabwehr mit 1,30 xG gegen; ein Weg zu drei Toren ist mit 67 % Over in Portsmouth-Heimspielen und 83 % in Swansea-Auswärtsspielen sichtbar, widerspricht aber dem Modell (46 % Over) und Portsmouths letzten sechs Spielen mit nur 33 % Over; stärkstes Gegenargument gegen jede Siegauswahl ist das ausgeglichene Modell (Heim 39 %, Auswärts 34 %), sodass kein Markt widerspruchsfrei getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.313, λ Gast 1.193. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 39 % · Remis 27 % · Auswärtssieg 34 % · BTTS Ja 51 % · Over 2,5 46 % · Under 2,5 54 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.63 · X 3.21 · 2 2.6 · BTTS Ja 1.87 · Over 2,5 2.22 · Under 2,5 1.71.

**Auswahl:** keine – Grund siehe Bild.

---

## 1.5 Preston North End – Sheffield United | 2026-11-03 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566287

Analyse-ID: A-20261103-8566287-r1 · Team-IDs: 210 / 251 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: Deepdale

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-31, Gast 2026-08-15 bis 2026-10-30; letzte 6: Heim 2026-09-19–2026-10-31, Gast 2026-09-19–2026-10-30.

**Preston North End (Heim, ID 210)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 10 | 5 | 5 | 4
Gegentore | 27 | 10 | 17 | 14
Tore/Spiel | 0.77 | 0.83 | 0.71 | 0.67
Gegentore/Spiel | 2.08 | 1.67 | 2.43 | 2.33
xG für/Spiel | 1.23 | 1.41 | 1.08 | 1.08
xG gegen/Spiel | 1.75 | 1.47 | 1.99 | 2.08
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 1/2/10 | 1/1/4 | 0/1/6 | 0/2/4
Punkte/Spiel | 0.38 | 0.67 | 0.14 | 0.33
BTTS % | 62 % | 67 % | 57 % | 50 %
Over 2,5 % | 62 % | 50 % | 71 % | 50 %
Under 2,5 % | 38 % | 50 % | 29 % | 50 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 38 % | 33 % | 43 % | 50 %
BTTS-and-lose % | 38 % | 33 % | 43 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Sheffield United (Gast, ID 251)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 17 | 9 | 8 | 9
Gegentore | 15 | 7 | 8 | 6
Tore/Spiel | 1.31 | 1.29 | 1.33 | 1.50
Gegentore/Spiel | 1.15 | 1.00 | 1.33 | 1.00
xG für/Spiel | 1.27 | 1.39 | 1.13 | 1.55
xG gegen/Spiel | 1.60 | 1.47 | 1.76 | 1.35
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 5/4/4 | 3/2/2 | 2/2/2 | 3/1/2
Punkte/Spiel | 1.46 | 1.57 | 1.33 | 1.67
BTTS % | 54 % | 43 % | 67 % | 50 %
Over 2,5 % | 54 % | 43 % | 67 % | 50 %
Under 2,5 % | 46 % | 57 % | 33 % | 50 %
Clean Sheets % | 38 % | 43 % | 33 % | 50 %
Failed to Score % | 23 % | 29 % | 17 % | 0 %
BTTS-and-lose % | 23 % | 14 % | 33 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Preston North End: 19.09. A Queens Park Rangers (1.54 PPG) 2:2 · 10.10. H Millwall (1.38 PPG) 0:1 · 13.10. A Birmingham City (1.77 PPG) 0:4 · 17.10. A Wrexham (1.08 PPG) 1:4 · 24.10. H West Bromwich Albion (1.85 PPG) 1:1 · 31.10. A Stoke City (1.77 PPG) 0:2

Letzte 6 Sheffield United: 19.09. A Stoke City (1.77 PPG) 1:2 · 10.10. H Lincoln City (1.15 PPG) 3:0 · 14.10. A Portsmouth (1.46 PPG) 2:3 · 17.10. A Bristol City (1.38 PPG) 1:0 · 24.10. H Derby County (0.54 PPG) 1:1 · 30.10. H Wrexham (1.08 PPG) 1:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Preston North End [1, 1, 0, 1, 2, 1, 0, 2, 0, 0, 1, 1, 0]; Sheffield United [0, 0, 2, 3, 1, 2, 0, 1, 3, 2, 1, 1, 1]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Preston mit 10 Toren in 13 und 4 Toren in den letzten sechs, gegen Sheffield Uniteds Abwehr mit 38 % Clean Sheets; der Weg zu drei Toren hängt vor allem an Sheffield und wird nicht gewählt; stärkstes Gegenargument ist Sheffields negative Auswärts-xG-Bilanz (1,13 für, 1,76 gegen) bei nur 2-2-2 auswärts, die gegen Prestons 1-2-10 ohne Clean Sheet und 14 Gegentore in den letzten sechs den Auswärtssieg (Modell 41 %) aber nicht entkräftet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1812 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.127, λ Gast 1.314. Prüfstand (unberührter Test, 182 Spiele ab 2026-04-22): Heimsieg nicht besser als Grundrate (Brier 0.2492 gegen 0.2444); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2175); BTTS Ja nicht besser als Grundrate (Brier 0.2556 gegen 0.2429); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2682 gegen 0.2536). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 32 % · Remis 27 % · Auswärtssieg 41 % · BTTS Ja 49 % · Over 2,5 44 % · Under 2,5 56 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.15 · X 3.43 · 2 1.93 · BTTS Ja 1.65 · Over 2,5 1.78 · Under 2,5 2.

**Auswahl:** Auswärtssieg

⚠️ Sheffield United auswärts nur 2-2-2 bei 1,13 xG für und 1,76 xG gegen – Remisrisiko.

---
