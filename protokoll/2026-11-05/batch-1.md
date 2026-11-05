# Vorabeintrag Batch 1 · 05.11.2026

- System: FootyStats-System v1.4 (Fassung v1.4-2026-11-05)
- Modell: Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-05 09:51 UTC
- Eintrag erstellt: 2026-11-05 09:56:12 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei Europapokal-Wettbewerben: nur Liga- bzw. Gruppenphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 1.1 Aldosivi – River Plate | 2026-11-05 18:00 UTC | Argentinien Primera División 2026, Spieltag 16 | Match-ID 8419139

Analyse-ID: A-20261105-8419139-r1 · Team-IDs: 696 / 718 · Saison-ID: 16571 · Status beim Abruf: incomplete · Ort: Estadio José María Minella · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026: 31 bzw. 31 Ligaspiele; xG für alle Spiele; 15 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-01-22 bis 2026-10-31, Gast 2026-01-24 bis 2026-11-01; letzte 6: Heim 2026-09-21–2026-10-31, Gast 2026-09-19–2026-11-01.

**Aldosivi (Heim, ID 696)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 31 | 15 | 16 | 6
Tore | 22 | 11 | 11 | 5
Gegentore | 43 | 14 | 29 | 8
Tore/Spiel | 0.71 | 0.73 | 0.69 | 0.83
Gegentore/Spiel | 1.39 | 0.93 | 1.81 | 1.33
xG für/Spiel | 1.37 | 1.54 | 1.22 | 1.46
xG gegen/Spiel | 1.69 | 1.46 | 1.89 | 1.76
Spiele mit xG | 31 | 15 | 16 | 6
S/U/N | 3/10/18 | 3/8/4 | 0/2/14 | 2/0/4
Punkte/Spiel | 0.61 | 1.13 | 0.12 | 1.00
BTTS % | 52 % | 47 % | 56 % | 50 %
Over 2,5 % | 35 % | 27 % | 44 % | 50 %
Under 2,5 % | 65 % | 73 % | 56 % | 50 %
Clean Sheets % | 23 % | 47 % | 0 % | 33 %
Failed to Score % | 42 % | 40 % | 44 % | 17 %
BTTS-and-lose % | 32 % | 20 % | 44 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**River Plate (Gast, ID 718)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 31 | 16 | 15 | 6
Tore | 41 | 24 | 17 | 7
Gegentore | 26 | 15 | 11 | 4
Tore/Spiel | 1.32 | 1.50 | 1.13 | 1.17
Gegentore/Spiel | 0.84 | 0.94 | 0.73 | 0.67
xG für/Spiel | 1.77 | 2.01 | 1.51 | 1.80
xG gegen/Spiel | 1.05 | 0.85 | 1.27 | 1.08
Spiele mit xG | 31 | 16 | 15 | 6
S/U/N | 16/4/11 | 9/1/6 | 7/3/5 | 3/1/2
Punkte/Spiel | 1.68 | 1.75 | 1.60 | 1.67
BTTS % | 35 % | 38 % | 33 % | 33 %
Over 2,5 % | 35 % | 44 % | 27 % | 33 %
Under 2,5 % | 65 % | 56 % | 73 % | 67 %
Clean Sheets % | 35 % | 38 % | 33 % | 50 %
Failed to Score % | 32 % | 25 % | 40 % | 17 %
BTTS-and-lose % | 6 % | 12 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Aldosivi: 21.09. H Atlético Tucumán (1.00 PPG) 1:0 · 04.10. A Huracán (1.32 PPG) 0:1 · 09.10. H Sarmiento (1.29 PPG) 1:3 · 18.10. A Estudiantes Río Cuarto (0.45 PPG) 1:2 · 25.10. H Belgrano (1.58 PPG) 1:0 · 31.10. A Racing Club (1.16 PPG) 1:2

Letzte 6 River Plate: 19.09. H Huracán (1.32 PPG) 1:2 · 11.10. H Estudiantes Río Cuarto (0.45 PPG) 1:0 · 14.10. A Sarmiento (1.29 PPG) 1:1 · 18.10. A Belgrano (1.58 PPG) 3:0 · 25.10. H Racing Club (1.16 PPG) 1:0 · 01.11. A Boca Juniors (1.94 PPG) 0:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Aldosivi [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 3, 3, 1, 0, 1, 1, 1, 1]; River Plate [1, 2, 0, 1, 0, 0, 3, 1, 2, 2, 2, 3, 2, 0, 3, 0, 0, 0, 0, 0, 2, 2, 3, 3, 2, 1, 1, 1, 3, 1, 0]

**Bild:** Saison 2026 mit je 31 Ligaspielen und voller xG-Abdeckung ist verwendbar, K.-o.-Spiele ausgeschlossen; schwächere Offensive ist Aldosivi mit 0,71 Toren pro Spiel und 42 % torlosen Spielen, gegen River mit 35 % Clean Sheets; der Weg zu drei Toren ist widersprüchlich, weil Aldosivis Heim- und Rivers Auswärtsspiele jeweils zu 73 % Under endeten, die xG-Variante aber 52 % Over schätzt; stärkstes Gegenargument gegen den Auswärtssieg ist Rivers Auswärtstorlosigkeit in 40 % der Spiele bei 8 Remis Aldosivis in 15 Heimspielen, sodass weder Sieg- noch Torlinienmarkt widerspruchsfrei getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1897 Spiele, Saisons [8595, 11212, 15746, 16571]; Schätzung Tormodell λ Heim 1.034, λ Gast 1.131; xG-Variante λ Heim 1.366, λ Gast 1.373 (xG-Anteil im Training 90 %). Prüfstand (unberührter Test, 190 Spiele ab 2026-08-02): Heimsieg besser als Grundrate (Brier 0.2358 gegen 0.2419); Auswärtssieg besser als Grundrate (Brier 0.2111 gegen 0.2164); BTTS Ja besser als Grundrate (Brier 0.2479 gegen 0.2645 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2448 gegen 0.261 – xG-Variante). Grenzen: 53 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 33 % · Remis 29 % · Auswärtssieg 38 % · BTTS Ja 56 % · Over 2,5 52 % · Under 2,5 48 % (nur Tormodell: BTTS 44 %, Over 2,5 37 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 7 · X 4.5 · 2 1.43 · BTTS Ja 2 · Over 2,5 1.91 · Under 2,5 1.93.

**Markt:** Heim 13 % · Remis 21 % · Auswärts 66 % · BTTS 45 % · Over 50 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 1.2 Palmeiras – Remo | 2026-11-05 22:30 UTC | Brasilien Série A 2026, Spieltag 34 | Match-ID 8409606

Analyse-ID: A-20261105-8409606-r1 · Team-IDs: 619 / 2594 · Saison-ID: 16544 · Status beim Abruf: incomplete · Ort: Allianz Parque

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026: 33 bzw. 33 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-01-28 bis 2026-10-28, Gast 2026-01-28 bis 2026-10-29; letzte 6: Heim 2026-09-20–2026-10-28, Gast 2026-09-19–2026-10-29.

**Palmeiras (Heim, ID 619)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 16 | 17 | 6
Tore | 56 | 30 | 26 | 9
Gegentore | 22 | 10 | 12 | 1
Tore/Spiel | 1.70 | 1.88 | 1.53 | 1.50
Gegentore/Spiel | 0.67 | 0.62 | 0.71 | 0.17
xG für/Spiel | 1.67 | 1.85 | 1.49 | 2.15
xG gegen/Spiel | 1.44 | 1.20 | 1.66 | 1.45
Spiele mit xG | 33 | 16 | 17 | 6
S/U/N | 20/10/3 | 12/3/1 | 8/7/2 | 4/2/0
Punkte/Spiel | 2.12 | 2.44 | 1.82 | 2.33
BTTS % | 52 % | 56 % | 47 % | 17 %
Over 2,5 % | 45 % | 44 % | 47 % | 17 %
Under 2,5 % | 55 % | 56 % | 53 % | 83 %
Clean Sheets % | 48 % | 44 % | 53 % | 83 %
Failed to Score % | 15 % | 6 % | 24 % | 33 %
BTTS-and-lose % | 9 % | 6 % | 12 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Remo (Gast, ID 2594)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 17 | 16 | 6
Tore | 36 | 22 | 14 | 5
Gegentore | 51 | 22 | 29 | 6
Tore/Spiel | 1.09 | 1.29 | 0.88 | 0.83
Gegentore/Spiel | 1.55 | 1.29 | 1.81 | 1.00
xG für/Spiel | 1.37 | 1.56 | 1.17 | 1.62
xG gegen/Spiel | 1.60 | 1.56 | 1.65 | 1.53
Spiele mit xG | 33 | 17 | 16 | 6
S/U/N | 6/11/16 | 4/7/6 | 2/4/10 | 1/3/2
Punkte/Spiel | 0.88 | 1.12 | 0.62 | 1.00
BTTS % | 61 % | 71 % | 50 % | 67 %
Over 2,5 % | 48 % | 41 % | 56 % | 33 %
Under 2,5 % | 52 % | 59 % | 44 % | 67 %
Clean Sheets % | 12 % | 12 % | 12 % | 17 %
Failed to Score % | 33 % | 18 % | 50 % | 33 %
BTTS-and-lose % | 21 % | 18 % | 25 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Palmeiras: 20.09. A Grêmio (1.09 PPG) 0:0 · 09.10. H Bahia (1.61 PPG) 1:0 · 11.10. H Corinthians (1.09 PPG) 4:1 · 17.10. A Atlético PR (1.59 PPG) 2:0 · 24.10. H Bragantino (1.38 PPG) 2:0 · 28.10. A Santos (1.38 PPG) 0:0

Letzte 6 Remo: 19.09. H Santos (1.38 PPG) 1:2 · 07.10. H Grêmio (1.09 PPG) 1:1 · 10.10. A Vasco da Gama (1.24 PPG) 0:0 · 18.10. H Bragantino (1.38 PPG) 1:1 · 23.10. A Cruzeiro (1.73 PPG) 0:1 · 29.10. H Botafogo (1.24 PPG) 2:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Palmeiras [2, 5, 3, 2, 1, 1, 2, 1, 2, 2, 0, 1, 1, 1, 1, 1, 3, 1, 3, 1, 4, 0, 2, 4, 1, 0, 2, 0, 1, 4, 2, 2, 0]; Remo [0, 2, 3, 1, 0, 0, 0, 4, 0, 0, 1, 2, 0, 2, 1, 3, 1, 1, 0, 2, 1, 2, 1, 1, 2, 0, 1, 1, 1, 0, 1, 0, 2]

**Bild:** Saison 2026 mit je 33 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Remo auswärts mit 14 Toren in 16 Spielen und 50 % torlosen Spielen, gegen Palmeiras mit 83 % Clean Sheets in den letzten sechs; der Weg zu drei Toren hängt fast allein an Palmeiras und wird nicht gewählt; stärkstes Gegenargument sind Palmeiras' zwei torlose Spiele in den letzten sechs, die aber auswärts entstanden, während Palmeiras daheim 12-3-1 und Remo auswärts 2-4-10 steht, sodass der Heimsieg (Modell 72 %) getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1476 Spiele, Saisons [9035, 11321, 14231, 16544]; Schätzung Tormodell λ Heim 2.178, λ Gast 0.661; xG-Variante λ Heim 2.019, λ Gast 1.059 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 148 Spiele ab 2026-07-23): Heimsieg besser als Grundrate (Brier 0.2303 gegen 0.2498); Auswärtssieg besser als Grundrate (Brier 0.1736 gegen 0.1809); BTTS Ja besser als Grundrate (Brier 0.2422 gegen 0.2486 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2494 gegen 0.2519 – xG-Variante). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 72 % · Remis 18 % · Auswärtssieg 10 % · BTTS Ja 57 % · Over 2,5 59 % · Under 2,5 41 % (nur Tormodell: BTTS 43 %, Over 2,5 54 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.25 · X 6.4 · 2 11.5 · BTTS Ja 2.25 · Over 2,5 1.5 · Under 2,5 2.55.

**Markt:** margenbereinigt 77 % für Heimsieg; Modell 72 %; Abweichung Modell − Markt -4 Prozentpunkte.

**Auswahl:** Heimsieg

---

## 1.3 Botafogo SP – Londrina | 2026-11-05 22:30 UTC | Brasilien Série B 2026, Spieltag 37 | Match-ID 8469644

Analyse-ID: A-20261105-8469644-r1 · Team-IDs: 2598 / 1055 · Saison-ID: 16783 · Status beim Abruf: incomplete · Ort: Estádio Santa Cruz

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026: 36 bzw. 36 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-03-21 bis 2026-10-31, Gast 2026-03-22 bis 2026-11-01; letzte 6: Heim 2026-10-03–2026-10-31, Gast 2026-10-02–2026-11-01.

**Botafogo SP (Heim, ID 2598)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 36 | 18 | 18 | 6
Tore | 41 | 27 | 14 | 7
Gegentore | 39 | 23 | 16 | 3
Tore/Spiel | 1.14 | 1.50 | 0.78 | 1.17
Gegentore/Spiel | 1.08 | 1.28 | 0.89 | 0.50
xG für/Spiel | 1.39 | 1.53 | 1.25 | 1.38
xG gegen/Spiel | 1.40 | 1.13 | 1.66 | 1.44
Spiele mit xG | 36 | 18 | 18 | 6
S/U/N | 13/9/14 | 7/4/7 | 6/5/7 | 4/1/1
Punkte/Spiel | 1.33 | 1.39 | 1.28 | 2.17
BTTS % | 50 % | 72 % | 28 % | 33 %
Over 2,5 % | 39 % | 56 % | 22 % | 17 %
Under 2,5 % | 61 % | 44 % | 78 % | 83 %
Clean Sheets % | 25 % | 17 % | 33 % | 50 %
Failed to Score % | 31 % | 11 % | 50 % | 17 %
BTTS-and-lose % | 14 % | 28 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Londrina (Gast, ID 1055)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 36 | 18 | 18 | 6
Tore | 45 | 25 | 20 | 6
Gegentore | 54 | 23 | 31 | 11
Tore/Spiel | 1.25 | 1.39 | 1.11 | 1.00
Gegentore/Spiel | 1.50 | 1.28 | 1.72 | 1.83
xG für/Spiel | 1.44 | 1.56 | 1.33 | 1.47
xG gegen/Spiel | 1.65 | 1.39 | 1.90 | 2.03
Spiele mit xG | 36 | 18 | 18 | 6
S/U/N | 8/8/20 | 5/5/8 | 3/3/12 | 1/1/4
Punkte/Spiel | 0.89 | 1.11 | 0.67 | 0.67
BTTS % | 56 % | 44 % | 67 % | 67 %
Over 2,5 % | 64 % | 56 % | 72 % | 67 %
Under 2,5 % | 36 % | 44 % | 28 % | 33 %
Clean Sheets % | 22 % | 44 % | 0 % | 17 %
Failed to Score % | 33 % | 33 % | 33 % | 17 %
BTTS-and-lose % | 33 % | 33 % | 33 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Botafogo SP: 03.10. H Vila Nova (1.75 PPG) 0:1 · 07.10. A Operário PR (1.42 PPG) 2:1 · 13.10. H Ceará (1.19 PPG) 1:0 · 18.10. A CRB (1.53 PPG) 1:0 · 24.10. A Avaí (1.03 PPG) 2:0 · 31.10. H Sport Recife (1.53 PPG) 1:1

Letzte 6 Londrina: 02.10. H Criciúma (1.72 PPG) 0:2 · 07.10. A Avaí (1.03 PPG) 1:2 · 13.10. A Athletic Club (1.31 PPG) 2:2 · 20.10. H Cuiabá (1.31 PPG) 1:0 · 24.10. A CRB (1.53 PPG) 1:2 · 01.11. H América Mineiro (0.72 PPG) 1:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Botafogo SP [4, 2, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 2, 1, 0, 3, 3, 0, 4, 0, 2, 1, 1, 0, 1, 0, 1, 1, 1, 2, 0, 2, 1, 1, 2, 1]; Londrina [3, 2, 1, 1, 0, 0, 0, 1, 4, 0, 0, 0, 3, 2, 2, 5, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 2, 6, 1, 0, 0, 1, 2, 1, 1, 1]

**Bild:** Saison 2026 mit je 36 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Londrina mit 1,25 Toren pro Spiel, gegen Botafogo SP mit 50 % Clean Sheets in den letzten sechs, während Londrina auswärts ohne Clean Sheet und mit 3-3-12 dasteht; der Weg zu drei Toren ist mit 56 % Over in Botafogo-Heimspielen möglich, aber Botafogo spielte in den letzten sechs nur zu 17 % Over und wird nicht gewählt; stärkstes Gegenargument sind Botafogos 7 Heimniederlagen in 18 Spielen, die als wesentliche Gefahr gewichtet werden, gegen Botafogos Form von 4-1-1 und Londrinas 1-1-4 den Heimsieg (Modell 46 %) aber nicht entkräften.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1500 Spiele, Saisons [9042, 11351, 14305, 16783]; Schätzung Tormodell λ Heim 1.319, λ Gast 0.932; xG-Variante λ Heim 1.505, λ Gast 1.152 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 150 Spiele ab 2026-08-14): Heimsieg besser als Grundrate (Brier 0.2375 gegen 0.2493); Auswärtssieg besser als Grundrate (Brier 0.2035 gegen 0.2099); BTTS Ja nicht besser als Grundrate (Brier 0.2528 gegen 0.2485 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2487 gegen 0.2558 – xG-Variante). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 46 % · Remis 28 % · Auswärtssieg 26 % · BTTS Ja 53 % · Over 2,5 50 % · Under 2,5 50 % (nur Tormodell: BTTS 44 %, Over 2,5 39 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.75 · X 3.5 · 2 4.3 · BTTS Ja 1.82 · Over 2,5 1.9 · Under 2,5 1.88.

**Markt:** margenbereinigt 52 % für Heimsieg; Modell 46 %; Abweichung Modell − Markt -7 Prozentpunkte.

**Auswahl:** Heimsieg

⚠️ Botafogo SP verlor 7 von 18 Heimspielen.

---

## 1.4 RSC Anderlecht – Salzburg | 2026-11-05 17:45 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700985

Analyse-ID: A-20261105-8700985-r1 · Team-IDs: 61 / 100 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Lotto Park · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-16 bis 2026-10-22, Gast 2026-09-17 bis 2026-10-22; letzte 6: Heim 2026-09-16–2026-10-22, Gast 2026-09-17–2026-10-22.

**RSC Anderlecht (Heim, ID 61)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 1 | 3 | 4
Gegentore | 3 | 2 | 1 | 3
Tore/Spiel | 1.33 | 1.00 | 1.50 | 1.33
Gegentore/Spiel | 1.00 | 2.00 | 0.50 | 1.00
xG für/Spiel | 1.65 | 1.67 | 1.64 | 1.65
xG gegen/Spiel | 1.22 | 1.71 | 0.97 | 1.22
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 0/0/1 | 1/0/1 | 1/0/2
Punkte/Spiel | 1.00 | 0.00 | 1.50 | 1.00
BTTS % | 33 % | 100 % | 0 % | 33 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 33 % | 0 % | 50 % | 33 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 33 % | 100 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Salzburg (Gast, ID 100)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 3 | 0 | 3 | 3
Gegentore | 6 | 4 | 2 | 6
Tore/Spiel | 1.00 | 0.00 | 1.50 | 1.00
Gegentore/Spiel | 2.00 | 4.00 | 1.00 | 2.00
xG für/Spiel | 1.47 | 1.31 | 1.54 | 1.47
xG gegen/Spiel | 1.37 | 1.83 | 1.15 | 1.37
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 0/0/1 | 1/1/0 | 1/1/1
Punkte/Spiel | 1.33 | 0.00 | 2.00 | 1.33
BTTS % | 33 % | 0 % | 50 % | 33 %
Over 2,5 % | 67 % | 100 % | 50 % | 67 %
Under 2,5 % | 33 % | 0 % | 50 % | 33 %
Clean Sheets % | 33 % | 0 % | 50 % | 33 %
Failed to Score % | 33 % | 100 % | 0 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**RSC Anderlecht – Landesliga (Saison-ID 17171, 2026-08-09 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 13 | 10 | 3 | 10
Gegentore | 11 | 2 | 9 | 6
Tore/Spiel | 1.30 | 2.00 | 0.60 | 1.67
Gegentore/Spiel | 1.10 | 0.40 | 1.80 | 1.00
xG für/Spiel | 1.86 | 2.15 | 1.57 | 1.67
xG gegen/Spiel | 1.20 | 0.93 | 1.47 | 1.28
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 6/1/3 | 4/1/0 | 2/0/3 | 4/1/1
Punkte/Spiel | 1.90 | 2.60 | 1.20 | 2.17
BTTS % | 30 % | 40 % | 20 % | 33 %
Over 2,5 % | 60 % | 60 % | 60 % | 67 %
Under 2,5 % | 40 % | 40 % | 40 % | 33 %
Clean Sheets % | 40 % | 60 % | 20 % | 50 %
Failed to Score % | 40 % | 20 % | 60 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Salzburg – Landesliga (Saison-ID 17181, 2026-08-01 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 29 | 21 | 8 | 15
Gegentore | 6 | 3 | 3 | 3
Tore/Spiel | 2.64 | 3.50 | 1.60 | 2.50
Gegentore/Spiel | 0.55 | 0.50 | 0.60 | 0.50
xG für/Spiel | 2.17 | 2.34 | 1.96 | 2.03
xG gegen/Spiel | 1.30 | 1.21 | 1.40 | 1.44
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 8/3/0 | 6/0/0 | 2/3/0 | 4/2/0
Punkte/Spiel | 2.45 | 3.00 | 1.80 | 2.33
BTTS % | 55 % | 50 % | 60 % | 50 %
Over 2,5 % | 64 % | 83 % | 40 % | 67 %
Under 2,5 % | 36 % | 17 % | 60 % | 33 %
Clean Sheets % | 45 % | 50 % | 40 % | 50 %
Failed to Score % | 9 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 RSC Anderlecht: 16.09. H Olympique Lyonnais (2.00 PPG) 1:2 · 15.10. A Dinamo Zagreb (1.33 PPG) 0:1 · 22.10. A Jagiellonia Białystok (1.00 PPG) 3:0

Letzte 6 Salzburg: 17.09. A Levski Sofia (1.33 PPG) 1:0 · 15.10. H AC Milan (1.00 PPG) 0:4 · 22.10. A Celje (0.33 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): RSC Anderlecht [1, 0, 3]; Salzburg [1, 0, 2]

**Bild:** Europa League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Salzburg mit 3 Toren in 3 Europa-League-Spielen, gegen Anderlechts Heimabwehr mit 60 % Liga-Clean-Sheets; ein Weg zu drei Toren ist mit 67 % Over beider Teams in drei Spielen unsicher belegt; stärkstes Gegenargument gegen den Modell-Heimsieg (57 %) ist Salzburgs ungeschlagene Ligabilanz (8-3-0) gegen Anderlechts 1-0-2 in der Europa League, sodass kein Markt getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.980, λ Gast 1.117; xG-Variante λ Heim 1.694, λ Gast 1.209 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 57 % · Remis 22 % · Auswärtssieg 21 % · BTTS Ja 57 % · Over 2,5 55 % · Under 2,5 45 % (nur Tormodell: BTTS 58 %, Over 2,5 60 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.96 · X 3.62 · 2 3.6 · BTTS Ja 1.47 · Over 2,5 1.56 · Under 2,5 2.36.

**Markt:** Heim 48 % · Remis 26 % · Auswärts 26 % · BTTS 62 % · Over 60 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 1.5 NEC – Omonia Nicosia | 2026-11-05 17:45 UTC | UEFA Europa League 2026/2027, Spieltag 4 | Match-ID 8700953

Analyse-ID: A-20261105-8700953-r1 · Team-IDs: 379 / 3741 · Saison-ID: 17127 · Status beim Abruf: incomplete · Ort: Goffertstadion · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 80 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Omonia Nicosia (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-09-17 bis 2026-10-22, Gast 2026-09-16 bis 2026-10-22; letzte 6: Heim 2026-09-17–2026-10-22, Gast 2026-09-16–2026-10-22.

**NEC (Heim, ID 379)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 5 | 1 | 4 | 5
Gegentore | 8 | 1 | 7 | 8
Tore/Spiel | 1.67 | 1.00 | 2.00 | 1.67
Gegentore/Spiel | 2.67 | 1.00 | 3.50 | 2.67
xG für/Spiel | 1.69 | 2.27 | 1.40 | 1.69
xG gegen/Spiel | 1.41 | 0.78 | 1.72 | 1.41
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/1/1 | 0/1/0 | 1/0/1 | 1/1/1
Punkte/Spiel | 1.33 | 1.00 | 1.50 | 1.33
BTTS % | 67 % | 100 % | 50 % | 67 %
Over 2,5 % | 67 % | 0 % | 100 % | 67 %
Under 2,5 % | 33 % | 100 % | 0 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Omonia Nicosia (Gast, ID 3741)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 5 | 2 | 3 | 5
Gegentore | 4 | 4 | 0 | 4
Tore/Spiel | 1.67 | 1.00 | 3.00 | 1.67
Gegentore/Spiel | 1.33 | 2.00 | 0.00 | 1.33
xG für/Spiel | 1.22 | 1.05 | 1.54 | 1.22
xG gegen/Spiel | 1.95 | 2.29 | 1.28 | 1.95
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 2/0/1 | 1/0/1 | 1/0/0 | 2/0/1
Punkte/Spiel | 2.00 | 1.50 | 3.00 | 2.00
BTTS % | 33 % | 50 % | 0 % | 33 %
Over 2,5 % | 67 % | 50 % | 100 % | 67 %
Under 2,5 % | 33 % | 50 % | 0 % | 33 %
Clean Sheets % | 67 % | 50 % | 100 % | 67 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 33 % | 50 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**NEC – Landesliga (Saison-ID 17097, 2026-08-08 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 17 | 9 | 8 | 6
Gegentore | 19 | 12 | 7 | 10
Tore/Spiel | 1.55 | 1.50 | 1.60 | 1.00
Gegentore/Spiel | 1.73 | 2.00 | 1.40 | 1.67
xG für/Spiel | 1.83 | 2.15 | 1.45 | 1.84
xG gegen/Spiel | 1.20 | 1.16 | 1.25 | 1.30
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 2/5/4 | 0/4/2 | 2/1/2 | 0/4/2
Punkte/Spiel | 1.00 | 0.67 | 1.40 | 0.67
BTTS % | 82 % | 100 % | 60 % | 67 %
Over 2,5 % | 73 % | 83 % | 60 % | 50 %
Under 2,5 % | 27 % | 17 % | 40 % | 50 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 18 % | 0 % | 40 % | 33 %
BTTS-and-lose % | 18 % | 33 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Omonia Nicosia – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 NEC: 17.09. A Juventus (2.33 PPG) 0:5 · 15.10. H Levski Sofia (1.33 PPG) 1:1 · 22.10. A Dinamo Zagreb (1.33 PPG) 4:2

Letzte 6 Omonia Nicosia: 16.09. H Celta de Vigo (1.00 PPG) 1:0 · 15.10. A Celje (0.33 PPG) 3:0 · 22.10. H Benfica (3.00 PPG) 1:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): NEC [0, 1, 4]; Omonia Nicosia [1, 3, 1]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Omonia Nikosia im API-Abo fehlt; schwächere Offensive ist Omonia mit 1,22 xG in der Europa League, gegen NEC ohne Clean Sheet in Liga und Europa League; ein Weg zu drei Toren ist mit 67 % Over beider Teams in drei Spielen und NECs 83 % Over daheim sichtbar, aber ohne Ligabasis für Omonia unsicher; stärkstes Gegenargument gegen den Modell-Heimsieg (43 %) ist NECs sieglose Heimbilanz in der Liga (0-4-2), sodass die Datenbasis keinen Markt trägt.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 439 Spiele, Saisons [10210, 12327, 15002, 17127]; Schätzung Tormodell λ Heim 1.671, λ Gast 1.428; xG-Variante λ Heim 1.722, λ Gast 1.196 (xG-Anteil im Training 99 %). Prüfstand (unberührter Test, 44 Spiele ab 2026-09-17): Heimsieg besser als Grundrate (Brier 0.2448 gegen 0.2515); Auswärtssieg nicht besser als Grundrate (Brier 0.2665 gegen 0.2637); BTTS Ja besser als Grundrate (Brier 0.2431 gegen 0.2471 – xG-Variante); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2387 gegen 0.2266 – xG-Variante). Grenzen: 411 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 43 % · Remis 24 % · Auswärtssieg 33 % · BTTS Ja 57 % · Over 2,5 56 % · Under 2,5 44 % (nur Tormodell: BTTS 62 %, Over 2,5 60 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.8 · X 4.06 · 2 4.2 · BTTS Ja 1.55 · Over 2,5 1.57 · Under 2,5 2.37.

**Markt:** Heim 53 % · Remis 24 % · Auswärts 23 % · BTTS 60 % · Over 60 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---
