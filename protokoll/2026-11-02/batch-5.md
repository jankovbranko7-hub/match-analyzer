# Vorabeintrag Batch 5 · 02.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-02 10:09 UTC
- Eintrag erstellt: 2026-11-02 10:17:29 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen der jeweiligen Ligasaison berechnet (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählt nur, wenn für das Spiel beide Werte ≥ 0 und nicht beide 0 sind.

## 5.1 Atalanta – Parma | 2026-11-02 19:45 UTC | Italien Serie A 2026/2027, Spieltag 10 | Match-ID 8545047

Analyse-ID: A-20261102-8545047-r1 · Team-IDs: 464 / 476 · Saison-ID: 17084 · Status beim Abruf: incomplete · Ort: Gewiss Stadium

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 9 bzw. 9 Ligaspiele; xG für alle Spiele; kleine Saisonstichprobe).

Zeitraum Saison: Heim 2026-08-23 bis 2026-10-29, Gast 2026-08-22 bis 2026-10-28; letzte 6: Heim 2026-09-12–2026-10-29, Gast 2026-09-14–2026-10-28.

**Atalanta (Heim, ID 464)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 16 | 11 | 5 | 12
Gegentore | 17 | 8 | 9 | 14
Tore/Spiel | 1.78 | 2.20 | 1.25 | 2.00
Gegentore/Spiel | 1.89 | 1.60 | 2.25 | 2.33
xG für/Spiel | 1.53 | 1.86 | 1.12 | 1.79
xG gegen/Spiel | 2.07 | 1.85 | 2.34 | 1.83
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 3/2/4 | 3/1/1 | 0/1/3 | 1/2/3
Punkte/Spiel | 1.22 | 2.00 | 0.25 | 0.83
BTTS % | 78 % | 80 % | 75 % | 83 %
Over 2,5 % | 78 % | 80 % | 75 % | 83 %
Under 2,5 % | 22 % | 20 % | 25 % | 17 %
Clean Sheets % | 11 % | 20 % | 0 % | 0 %
Failed to Score % | 11 % | 0 % | 25 % | 17 %
BTTS-and-lose % | 33 % | 20 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Parma (Gast, ID 476)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 5 | 3 | 2 | 4
Gegentore | 15 | 6 | 9 | 11
Tore/Spiel | 0.56 | 0.60 | 0.50 | 0.67
Gegentore/Spiel | 1.67 | 1.20 | 2.25 | 1.83
xG für/Spiel | 1.13 | 1.25 | 0.97 | 1.25
xG gegen/Spiel | 1.87 | 1.52 | 2.32 | 1.96
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 1/2/6 | 1/2/2 | 0/0/4 | 1/1/4
Punkte/Spiel | 0.56 | 1.00 | 0.00 | 0.67
BTTS % | 44 % | 40 % | 50 % | 50 %
Over 2,5 % | 56 % | 40 % | 75 % | 83 %
Under 2,5 % | 44 % | 60 % | 25 % | 17 %
Clean Sheets % | 11 % | 20 % | 0 % | 17 %
Failed to Score % | 56 % | 60 % | 50 % | 50 %
BTTS-and-lose % | 22 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Atalanta: 12.09. H Cagliari (1.30 PPG) 1:2 · 20.09. A Juventus (1.70 PPG) 0:2 · 12.10. H Venezia (0.30 PPG) 3:1 · 18.10. A AC Milan (2.10 PPG) 2:3 · 25.10. H Frosinone (2.00 PPG) 4:4 · 29.10. A Fiorentina (0.56 PPG) 2:2

Letzte 6 Parma: 14.09. A Como (2.30 PPG) 1:2 · 20.09. H Genoa (1.30 PPG) 2:1 · 10.10. A Inter Milan (2.50 PPG) 0:3 · 19.10. H Torino (1.30 PPG) 0:3 · 24.10. A Lazio (2.80 PPG) 1:2 · 28.10. H Udinese (0.50 PPG) 0:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Atalanta [2, 1, 1, 1, 0, 3, 2, 4, 2]; Parma [0, 0, 1, 1, 2, 0, 0, 1, 0]

**Bild:** Saison 2026/27 mit je 9 Spielen und voller xG-Abdeckung ist eingeschränkt verwendbar; schwächere Offensive ist Parma mit 5 Toren in 9 Spielen und 56 % torlosen Spielen, auswärts 2 Tore in 4, gegen Atalantas Heimabwehr; der Weg zu drei Toren hängt vor allem an Atalanta (11 Heimtore in 5) und wird nicht gewählt; stärkstes Gegenargument ist Atalantas schwache Defensive (2,07 xG gegen) und Form (0,83 Punkte/Spiel in den letzten sechs), die gegen Parmas torarmen Angriff aber weniger wiegt, sodass der Heimsieg (Modell 64 %) getragen bleibt.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1238 Spiele, Saisons [9697, 12530, 15068, 17084]; Schätzung λ Heim 1.918, λ Gast 0.790. Prüfstand (unberührter Test, 124 Spiele ab 2026-05-10): Heimsieg brauchbar (Brier 0.2082 gegen 0.2484); Auswärtssieg brauchbar (Brier 0.2055 gegen 0.2426); BTTS Ja brauchbar (Brier 0.2433 gegen 0.2504); Over 2,5 / Under 2,5 brauchbar (Brier 0.2529 gegen 0.2543). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 64 % · Remis 21 % · Auswärtssieg 15 % · BTTS Ja 47 % · Over 2,5 51 % · Under 2,5 49 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.53 · X 4.5 · 2 5.75 · BTTS Ja 1.7 · Over 2,5 1.56 · Under 2,5 2.22.

**Auswahl:** Heimsieg

⚠️ Atalanta: 2,07 xG gegen pro Spiel und 1-2-3 in den letzten sechs Spielen – Widerspruch zwischen Saison-Heimbild und Form.

---

## 5.2 Heracles – Oss | 2026-11-02 19:00 UTC | Niederlande Eerste Divisie 2026/2027, Spieltag 13 | Match-ID 8549998

Analyse-ID: A-20261102-8549998-r1 · Team-IDs: 370 / 391 · Saison-ID: 17110 · Status beim Abruf: incomplete · Ort: Asito Stadion

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-07 bis 2026-10-23, Gast 2026-08-07 bis 2026-10-23; letzte 6: Heim 2026-09-18–2026-10-23, Gast 2026-09-18–2026-10-23.

**Heracles (Heim, ID 370)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 5 | 7 | 6
Tore | 37 | 16 | 21 | 13
Gegentore | 14 | 4 | 10 | 5
Tore/Spiel | 3.08 | 3.20 | 3.00 | 2.17
Gegentore/Spiel | 1.17 | 0.80 | 1.43 | 0.83
xG für/Spiel | 2.36 | 2.55 | 2.23 | 2.33
xG gegen/Spiel | 1.04 | 0.93 | 1.11 | 0.91
Spiele mit xG | 12 | 5 | 7 | 6
S/U/N | 9/2/1 | 5/0/0 | 4/2/1 | 3/2/1
Punkte/Spiel | 2.42 | 3.00 | 2.00 | 1.83
BTTS % | 67 % | 40 % | 86 % | 50 %
Over 2,5 % | 75 % | 80 % | 71 % | 50 %
Under 2,5 % | 25 % | 20 % | 29 % | 50 %
Clean Sheets % | 25 % | 60 % | 0 % | 33 %
Failed to Score % | 8 % | 0 % | 14 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Oss (Gast, ID 391)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 19 | 16 | 3 | 14
Gegentore | 20 | 8 | 12 | 8
Tore/Spiel | 1.58 | 2.67 | 0.50 | 2.33
Gegentore/Spiel | 1.67 | 1.33 | 2.00 | 1.33
xG für/Spiel | 1.30 | 1.34 | 1.26 | 1.40
xG gegen/Spiel | 1.95 | 2.12 | 1.79 | 1.99
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 4/1/7 | 4/1/1 | 0/0/6 | 3/1/2
Punkte/Spiel | 1.08 | 2.17 | 0.00 | 1.67
BTTS % | 67 % | 83 % | 50 % | 67 %
Over 2,5 % | 83 % | 100 % | 67 % | 83 %
Under 2,5 % | 17 % | 0 % | 33 % | 17 %
Clean Sheets % | 8 % | 17 % | 0 % | 17 %
Failed to Score % | 25 % | 0 % | 50 % | 17 %
BTTS-and-lose % | 33 % | 17 % | 50 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Heracles: 18.09. A Almere City (1.92 PPG) 0:1 · 26.09. H Vitesse (1.42 PPG) 2:0 · 02.10. A Helmond Sport (0.92 PPG) 2:2 · 09.10. H RKC Waalwijk (1.23 PPG) 3:0 · 18.10. A MVV (1.31 PPG) 5:1 · 23.10. A NAC Breda (1.75 PPG) 1:1

Letzte 6 Oss: 18.09. H Dordrecht (0.92 PPG) 3:0 · 26.09. A Emmen (1.92 PPG) 0:1 · 03.10. H MVV (1.31 PPG) 4:1 · 09.10. H Helmond Sport (0.92 PPG) 3:1 · 16.10. A Den Bosch (1.38 PPG) 1:2 · 23.10. H Ajax II (1.00 PPG) 3:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Heracles [4, 3, 6, 3, 5, 3, 0, 2, 2, 3, 5, 1]; Oss [1, 0, 0, 2, 1, 1, 3, 0, 4, 3, 1, 3]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Oss auswärts mit 3 Toren in 6 Spielen und 50 % torlosen Spielen, gegen eine Heracles-Heimabwehr mit 4 Gegentoren in 5; der Weg zu drei Toren hängt fast allein an Heracles und wird nicht gewählt, weil Over in dieser Liga im Test schlechter als die Grundrate war; stärkstes Gegenargument ist Oss' verbesserte Form (1,67 Punkte/Spiel in den letzten sechs), die aber auf Heimspielen beruht, während Oss auswärts 0-0-6 steht, sodass der Heimsieg (Modell 77 %) klar getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1266 Spiele, Saisons [9654, 12317, 14987, 17110]; Schätzung λ Heim 2.777, λ Gast 0.868. Prüfstand (unberührter Test, 127 Spiele ab 2026-04-24): Heimsieg brauchbar (Brier 0.2404 gegen 0.2532); Auswärtssieg schlechter als Grundrate (für diesen Markt unbrauchbar) (Brier 0.2142 gegen 0.213); BTTS Ja brauchbar (Brier 0.2221 gegen 0.2243); Over 2,5 / Under 2,5 schlechter als Grundrate (für diesen Markt unbrauchbar) (Brier 0.2343 gegen 0.2229). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 77 % · Remis 14 % · Auswärtssieg 9 % · BTTS Ja 54 % · Over 2,5 70 % · Under 2,5 30 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.18 · X 7 · 2 9.3 · BTTS Ja 1.73 · Over 2,5 1.25 · Under 2,5 3.5.

**Auswahl:** Heimsieg

---

## 5.3 PSV II – NAC Breda | 2026-11-02 19:00 UTC | Niederlande Eerste Divisie 2026/2027, Spieltag 13 | Match-ID 8550180

Analyse-ID: A-20261102-8550180-r1 · Team-IDs: 392 / 385 · Saison-ID: 17110 · Status beim Abruf: incomplete · Ort: Sportcomplex De Herdgang

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-10 bis 2026-10-23, Gast 2026-08-07 bis 2026-10-23; letzte 6: Heim 2026-09-11–2026-10-23, Gast 2026-09-20–2026-10-23.

**PSV II (Heim, ID 392)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 17 | 9 | 8 | 6
Gegentore | 19 | 6 | 13 | 10
Tore/Spiel | 1.42 | 1.50 | 1.33 | 1.00
Gegentore/Spiel | 1.58 | 1.00 | 2.17 | 1.67
xG für/Spiel | 1.60 | 1.75 | 1.45 | 1.26
xG gegen/Spiel | 1.77 | 1.51 | 2.03 | 2.05
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 4/4/4 | 3/2/1 | 1/2/3 | 1/2/3
Punkte/Spiel | 1.33 | 1.83 | 0.83 | 0.83
BTTS % | 83 % | 67 % | 100 % | 83 %
Over 2,5 % | 58 % | 33 % | 83 % | 50 %
Under 2,5 % | 42 % | 67 % | 17 % | 50 %
Clean Sheets % | 8 % | 17 % | 0 % | 0 %
Failed to Score % | 8 % | 17 % | 0 % | 17 %
BTTS-and-lose % | 25 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**NAC Breda (Gast, ID 385)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 23 | 11 | 12 | 12
Gegentore | 20 | 10 | 10 | 6
Tore/Spiel | 1.92 | 1.83 | 2.00 | 2.00
Gegentore/Spiel | 1.67 | 1.67 | 1.67 | 1.00
xG für/Spiel | 1.97 | 2.04 | 1.91 | 1.76
xG gegen/Spiel | 1.07 | 0.90 | 1.23 | 0.86
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 6/3/3 | 3/1/2 | 3/2/1 | 4/2/0
Punkte/Spiel | 1.75 | 1.67 | 1.83 | 2.33
BTTS % | 75 % | 67 % | 83 % | 67 %
Over 2,5 % | 67 % | 50 % | 83 % | 50 %
Under 2,5 % | 33 % | 50 % | 17 % | 50 %
Clean Sheets % | 17 % | 17 % | 17 % | 33 %
Failed to Score % | 8 % | 17 % | 0 % | 0 %
BTTS-and-lose % | 17 % | 17 % | 17 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 PSV II: 11.09. A Helmond Sport (0.92 PPG) 1:3 · 14.09. H AZ II (1.31 PPG) 1:1 · 19.09. A Vitesse (1.42 PPG) 1:3 · 09.10. A Roda JC (1.92 PPG) 1:1 · 19.10. H Dordrecht (0.92 PPG) 0:1 · 23.10. A Eindhoven (0.85 PPG) 2:1

Letzte 6 NAC Breda: 20.09. A De Graafschap (1.15 PPG) 2:1 · 26.09. H Eindhoven (0.85 PPG) 4:2 · 03.10. A Vitesse (1.42 PPG) 2:2 · 09.10. H MVV (1.31 PPG) 1:0 · 16.10. A Helmond Sport (0.92 PPG) 2:0 · 23.10. H Heracles (2.42 PPG) 1:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): PSV II [3, 1, 1, 2, 1, 3, 1, 1, 1, 1, 0, 2]; NAC Breda [2, 0, 3, 2, 2, 2, 2, 4, 2, 1, 2, 1]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist PSV II mit 1,42 Toren/Spiel, das aber in 11 von 12 Spielen traf (gleichmäßig verteilt) gegen NAC, die nur 17 % Clean Sheets hat, während NAC ebenfalls in 11 von 12 Spielen traf gegen PSV II mit 8 % Clean Sheets; der Weg zu drei Toren ist über beide Teams plausibel (Modell 71 % Over), Over war in dieser Liga im Test aber schlechter als die Grundrate; stärkstes Gegenargument ist NACs starke Abwehr mit 1,07 xG gegen (letzte sechs 0,86) gegen PSV IIs schwächere Form (1,26 xG in den letzten sechs), was den Heimtreffer gefährdet, BTTS (Modell 70 %) aber nicht entkräftet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1266 Spiele, Saisons [9654, 12317, 14987, 17110]; Schätzung λ Heim 1.754, λ Gast 1.896. Prüfstand (unberührter Test, 127 Spiele ab 2026-04-24): Heimsieg brauchbar (Brier 0.2404 gegen 0.2532); Auswärtssieg schlechter als Grundrate (für diesen Markt unbrauchbar) (Brier 0.2142 gegen 0.213); BTTS Ja brauchbar (Brier 0.2221 gegen 0.2243); Over 2,5 / Under 2,5 schlechter als Grundrate (für diesen Markt unbrauchbar) (Brier 0.2343 gegen 0.2229). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 36 % · Remis 22 % · Auswärtssieg 42 % · BTTS Ja 70 % · Over 2,5 71 % · Under 2,5 29 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 4.6 · X 4.3 · 2 1.47 · BTTS Ja 1.4 · Over 2,5 1.28 · Under 2,5 3.05.

**Auswahl:** BTTS Ja

⚠️ PSV II gegen NACs Abwehr mit nur 0,86 xG gegen in den letzten sechs Spielen – Gefahr für den Heimtreffer.

---

## 5.4 Ajax II – Vitesse | 2026-11-02 19:00 UTC | Niederlande Eerste Divisie 2026/2027, Spieltag 13 | Match-ID 8550267

Analyse-ID: A-20261102-8550267-r1 · Team-IDs: 400 / 369 · Saison-ID: 17110 · Status beim Abruf: incomplete · Ort: Sportpark De Toekomst

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-07 bis 2026-10-23, Gast 2026-08-07 bis 2026-10-23; letzte 6: Heim 2026-09-11–2026-10-23, Gast 2026-09-19–2026-10-23.

**Ajax II (Heim, ID 400)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 18 | 9 | 9 | 6
Gegentore | 29 | 14 | 15 | 15
Tore/Spiel | 1.50 | 1.50 | 1.50 | 1.00
Gegentore/Spiel | 2.42 | 2.33 | 2.50 | 2.50
xG für/Spiel | 1.70 | 1.68 | 1.73 | 1.84
xG gegen/Spiel | 1.82 | 1.72 | 1.92 | 1.65
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 3/3/6 | 2/1/3 | 1/2/3 | 1/2/3
Punkte/Spiel | 1.00 | 1.17 | 0.83 | 0.83
BTTS % | 67 % | 50 % | 83 % | 50 %
Over 2,5 % | 67 % | 67 % | 67 % | 67 %
Under 2,5 % | 33 % | 33 % | 33 % | 33 %
Clean Sheets % | 17 % | 17 % | 17 % | 17 %
Failed to Score % | 25 % | 50 % | 0 % | 50 %
BTTS-and-lose % | 33 % | 17 % | 50 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Vitesse (Gast, ID 369)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 16 | 8 | 8 | 6
Gegentore | 17 | 10 | 7 | 9
Tore/Spiel | 1.33 | 1.33 | 1.33 | 1.00
Gegentore/Spiel | 1.42 | 1.67 | 1.17 | 1.50
xG für/Spiel | 1.57 | 1.73 | 1.40 | 1.40
xG gegen/Spiel | 1.50 | 1.43 | 1.57 | 1.45
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 5/2/5 | 2/2/2 | 3/0/3 | 2/1/3
Punkte/Spiel | 1.42 | 1.33 | 1.50 | 1.17
BTTS % | 50 % | 67 % | 33 % | 33 %
Over 2,5 % | 50 % | 67 % | 33 % | 33 %
Under 2,5 % | 50 % | 33 % | 67 % | 67 %
Clean Sheets % | 8 % | 0 % | 17 % | 17 %
Failed to Score % | 42 % | 33 % | 50 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Ajax II: 11.09. H RKC Waalwijk (1.23 PPG) 0:2 · 14.09. A Utrecht II (0.58 PPG) 1:6 · 18.09. H Roda JC (1.92 PPG) 0:0 · 09.10. H VVV (2.15 PPG) 0:3 · 19.10. H De Graafschap (1.15 PPG) 2:1 · 23.10. A Oss (1.08 PPG) 3:3

Letzte 6 Vitesse: 19.09. H PSV II (1.33 PPG) 3:1 · 26.09. A Heracles (2.42 PPG) 0:2 · 03.10. H NAC Breda (1.75 PPG) 2:2 · 09.10. A Volendam (1.46 PPG) 0:2 · 16.10. A Eindhoven (0.85 PPG) 1:0 · 23.10. H Emmen (1.92 PPG) 0:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Ajax II [1, 4, 2, 3, 1, 1, 0, 1, 0, 0, 2, 3]; Vitesse [1, 3, 0, 4, 2, 0, 3, 0, 2, 0, 1, 0]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Vitesse mit 42 % torlosen Spielen (auswärts 50 %), aber auch Ajax II blieb daheim in 50 % der Spiele torlos; ein Weg zu drei Toren ist über Ajax IIs schwache Abwehr (29 Gegentore) möglich, Over war in dieser Liga im Test aber schlechter als die Grundrate; stärkstes Gegenargument gegen BTTS ist die beidseitige Torlosigkeit (je 50 % ohne Tor im jeweiligen Kontext), die beide benötigten Treffer gefährdet und überwiegt, und beide Siegmärkte sind mit 37 % und 38 % ausgeglichen.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1266 Spiele, Saisons [9654, 12317, 14987, 17110]; Schätzung λ Heim 1.488, λ Gast 1.516. Prüfstand (unberührter Test, 127 Spiele ab 2026-04-24): Heimsieg brauchbar (Brier 0.2404 gegen 0.2532); Auswärtssieg schlechter als Grundrate (für diesen Markt unbrauchbar) (Brier 0.2142 gegen 0.213); BTTS Ja brauchbar (Brier 0.2221 gegen 0.2243); Over 2,5 / Under 2,5 schlechter als Grundrate (für diesen Markt unbrauchbar) (Brier 0.2343 gegen 0.2229). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 37 % · Remis 24 % · Auswärtssieg 38 % · BTTS Ja 60 % · Over 2,5 58 % · Under 2,5 42 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.62 · X 3.98 · 2 1.93 · BTTS Ja 1.3 · Over 2,5 1.33 · Under 2,5 3.1.

**Auswahl:** keine – Grund siehe Bild.

---

## 5.5 Utrecht II – Dordrecht | 2026-11-02 19:00 UTC | Niederlande Eerste Divisie 2026/2027, Spieltag 13 | Match-ID 8550144

Analyse-ID: A-20261102-8550144-r1 · Team-IDs: 399 / 384 · Saison-ID: 17110 · Status beim Abruf: incomplete · Ort: Sportcomplex Zoudenbalch

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-09 bis 2026-10-23, Gast 2026-08-07 bis 2026-10-24; letzte 6: Heim 2026-09-11–2026-10-23, Gast 2026-09-18–2026-10-24.

**Utrecht II (Heim, ID 399)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 19 | 10 | 9 | 14
Gegentore | 31 | 15 | 16 | 16
Tore/Spiel | 1.58 | 1.67 | 1.50 | 2.33
Gegentore/Spiel | 2.58 | 2.50 | 2.67 | 2.67
xG für/Spiel | 1.62 | 1.50 | 1.74 | 1.72
xG gegen/Spiel | 1.87 | 1.79 | 1.94 | 1.90
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 2/1/9 | 1/1/4 | 1/0/5 | 2/0/4
Punkte/Spiel | 0.58 | 0.67 | 0.50 | 1.00
BTTS % | 92 % | 83 % | 100 % | 100 %
Over 2,5 % | 92 % | 83 % | 100 % | 100 %
Under 2,5 % | 8 % | 17 % | 0 % | 0 %
Clean Sheets % | 8 % | 17 % | 0 % | 0 %
Failed to Score % | 8 % | 17 % | 0 % | 0 %
BTTS-and-lose % | 75 % | 67 % | 83 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Dordrecht (Gast, ID 384)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 16 | 10 | 6 | 7
Gegentore | 31 | 17 | 14 | 13
Tore/Spiel | 1.33 | 1.67 | 1.00 | 1.17
Gegentore/Spiel | 2.58 | 2.83 | 2.33 | 2.17
xG für/Spiel | 1.46 | 1.38 | 1.54 | 1.45
xG gegen/Spiel | 1.52 | 1.60 | 1.44 | 1.27
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 3/2/7 | 2/0/4 | 1/2/3 | 2/1/3
Punkte/Spiel | 0.92 | 1.00 | 0.83 | 1.17
BTTS % | 67 % | 67 % | 67 % | 50 %
Over 2,5 % | 75 % | 83 % | 67 % | 67 %
Under 2,5 % | 25 % | 17 % | 33 % | 33 %
Clean Sheets % | 8 % | 0 % | 17 % | 17 %
Failed to Score % | 25 % | 33 % | 17 % | 33 %
BTTS-and-lose % | 33 % | 33 % | 33 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Utrecht II: 11.09. A NAC Breda (1.75 PPG) 3:2 · 14.09. H Ajax II (1.00 PPG) 6:1 · 18.09. H VVV (2.15 PPG) 1:3 · 09.10. A De Graafschap (1.15 PPG) 1:2 · 19.10. H Roda JC (1.92 PPG) 1:2 · 23.10. A Volendam (1.46 PPG) 2:6

Letzte 6 Dordrecht: 18.09. A Oss (1.08 PPG) 0:3 · 25.09. H Almere City (1.92 PPG) 3:2 · 03.10. A Den Bosch (1.38 PPG) 1:1 · 09.10. H Emmen (1.92 PPG) 0:3 · 19.10. A PSV II (1.33 PPG) 1:0 · 24.10. H VVV (2.15 PPG) 2:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Utrecht II [1, 1, 1, 1, 1, 0, 3, 6, 1, 1, 1, 2]; Dordrecht [2, 2, 0, 1, 3, 1, 0, 3, 1, 0, 1, 2]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Dordrecht mit 1,33 Toren/Spiel, das auswärts in 5 von 6 Spielen traf, gegen Utrecht II mit 2,58 Gegentoren/Spiel und 8 % Clean Sheets, während Utrecht II in 11 von 12 Spielen traf (das 6:1 ist eine Häufung, die Trefferserie aber gleichmäßig) gegen Dordrecht mit 8 % Clean Sheets; der Weg zu drei Toren ist mit 92 % Over in Utrecht-II-Spielen stark, Over war in dieser Liga im Test aber schlechter als die Grundrate; stärkstes Gegenargument sind Dordrechts 33 % torlose Spiele in den letzten sechs, die gegen die schwächste Abwehr der Paarung aber keine wesentliche Gefahr begründen.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1266 Spiele, Saisons [9654, 12317, 14987, 17110]; Schätzung λ Heim 1.214, λ Gast 1.791. Prüfstand (unberührter Test, 127 Spiele ab 2026-04-24): Heimsieg brauchbar (Brier 0.2404 gegen 0.2532); Auswärtssieg schlechter als Grundrate (für diesen Markt unbrauchbar) (Brier 0.2142 gegen 0.213); BTTS Ja brauchbar (Brier 0.2221 gegen 0.2243); Over 2,5 / Under 2,5 schlechter als Grundrate (für diesen Markt unbrauchbar) (Brier 0.2343 gegen 0.2229). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 26 % · Remis 23 % · Auswärtssieg 51 % · BTTS Ja 59 % · Over 2,5 58 % · Under 2,5 42 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.25 · X 3.6 · 2 2.7 · BTTS Ja 1.4 · Over 2,5 1.47 · Under 2,5 2.63.

**Auswahl:** BTTS Ja

---
