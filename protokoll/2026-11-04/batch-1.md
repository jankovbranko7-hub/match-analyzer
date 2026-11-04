# Vorabeintrag Batch 1 · 04.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-04 16:19 UTC
- Eintrag erstellt: 2026-11-04 16:21:29 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 1.1 KV Kortrijk – KV Mechelen | 2026-11-04 19:30 UTC | Belgien Pro League 2026/2027, Spieltag 9 | Match-ID 8562287

Analyse-ID: A-20261104-8562287-r1 · Team-IDs: 536 / 537 · Saison-ID: 17171 · Status beim Abruf: incomplete · Ort: Guldensporenstadion

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 9 bzw. 9 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-07 bis 2026-10-31, Gast 2026-08-09 bis 2026-10-31; letzte 6: Heim 2026-09-03–2026-10-31, Gast 2026-08-29–2026-10-31.

**KV Kortrijk (Heim, ID 536)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 3 | 2 | 1 | 2
Gegentore | 19 | 8 | 11 | 10
Tore/Spiel | 0.33 | 0.50 | 0.20 | 0.33
Gegentore/Spiel | 2.11 | 2.00 | 2.20 | 1.67
xG für/Spiel | 1.17 | 1.41 | 0.97 | 1.16
xG gegen/Spiel | 1.71 | 1.56 | 1.82 | 1.58
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 1/1/7 | 1/0/3 | 0/1/4 | 1/1/4
Punkte/Spiel | 0.44 | 0.75 | 0.20 | 0.67
BTTS % | 22 % | 25 % | 20 % | 17 %
Over 2,5 % | 56 % | 50 % | 60 % | 33 %
Under 2,5 % | 44 % | 50 % | 40 % | 67 %
Clean Sheets % | 11 % | 25 % | 0 % | 17 %
Failed to Score % | 67 % | 50 % | 80 % | 67 %
BTTS-and-lose % | 11 % | 25 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**KV Mechelen (Gast, ID 537)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 10 | 8 | 2 | 7
Gegentore | 17 | 11 | 6 | 10
Tore/Spiel | 1.11 | 1.60 | 0.50 | 1.17
Gegentore/Spiel | 1.89 | 2.20 | 1.50 | 1.67
xG für/Spiel | 1.29 | 1.30 | 1.28 | 1.39
xG gegen/Spiel | 1.62 | 1.80 | 1.40 | 1.60
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 2/3/4 | 2/1/2 | 0/2/2 | 2/2/2
Punkte/Spiel | 1.00 | 1.40 | 0.50 | 1.33
BTTS % | 33 % | 40 % | 25 % | 33 %
Over 2,5 % | 44 % | 60 % | 25 % | 50 %
Under 2,5 % | 56 % | 40 % | 75 % | 50 %
Clean Sheets % | 22 % | 20 % | 25 % | 33 %
Failed to Score % | 56 % | 40 % | 75 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 KV Kortrijk: 03.09. A RSC Anderlecht (1.90 PPG) 0:1 · 06.09. H Zulte-Waregem (1.10 PPG) 0:2 · 13.09. A RAAL La Louvière (0.70 PPG) 0:3 · 20.09. H Waasland-Beveren (1.00 PPG) 1:0 · 10.10. A KRC Genk (1.50 PPG) 0:3 · 31.10. A Standard Liège (1.20 PPG) 1:1

Letzte 6 KV Mechelen: 29.08. A RAAL La Louvière (0.70 PPG) 2:2 · 05.09. H KVC Westerlo (1.40 PPG) 0:4 · 11.09. H RSC Anderlecht (1.90 PPG) 0:1 · 19.09. A Lommel United (1.50 PPG) 0:0 · 11.10. H Sint-Truiden (0.80 PPG) 4:3 · 31.10. H KRC Genk (1.50 PPG) 1:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): KV Kortrijk [0, 0, 1, 0, 0, 0, 1, 0, 1]; KV Mechelen [0, 3, 0, 2, 0, 0, 0, 4, 1]

**Bild:** Saison 2026/27 mit je 9 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Kortrijk mit 3 Toren in 9 Spielen und 67 % torlosen Spielen, während auch Mechelen auswärts nur 2 Tore in 4 Spielen erzielte (75 % torlos); der Weg zu drei Toren ist schwach, weil beide Offensiven kaum treffen und Mechelens Auswärtsspiele nur zu 25 % Over endeten, das Modell schätzt 50 % Under; stärkstes Gegenargument ist Kortrijks anfällige Abwehr mit 2,11 Gegentoren pro Spiel (56 % Over in Kortrijk-Spielen), über die ein einseitiges Spiel drei Tore hergeben kann, was als wesentliche Gefahr gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1025 Spiele, Saisons [9577, 12137, 14937, 17171]; Schätzung λ Heim 1.101, λ Gast 1.567. Prüfstand (unberührter Test, 103 Spiele ab 2026-05-17): Heimsieg besser als Grundrate (Brier 0.2121 gegen 0.2555); Auswärtssieg besser als Grundrate (Brier 0.1649 gegen 0.2066); BTTS Ja nicht besser als Grundrate (Brier 0.2577 gegen 0.254); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2432 gegen 0.2446). Grenzen: 2 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 27 % · Remis 25 % · Auswärtssieg 48 % · BTTS Ja 53 % · Over 2,5 50 % · Under 2,5 50 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.61 · X 3.35 · 2 2.6 · BTTS Ja 1.6 · Over 2,5 1.78 · Under 2,5 1.95.

**Auswahl:** Under 2,5

⚠️ Kortrijk kassiert 2,11 Tore pro Spiel (56 % Over) – ein einseitiges Spiel kann drei Tore bringen; Modell nur 50 %.

---

## 1.2 Atlético PR – Vasco da Gama | 2026-11-04 22:30 UTC | Brasilien Série A 2026, Spieltag 34 | Match-ID 8409594

Analyse-ID: A-20261104-8409594-r1 · Team-IDs: 622 / 625 · Saison-ID: 16544 · Status beim Abruf: incomplete · Ort: Arena de Baixada

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026: 33 bzw. 32 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-01-28 bis 2026-10-30, Gast 2026-01-29 bis 2026-10-29; letzte 6: Heim 2026-09-20–2026-10-30, Gast 2026-09-19–2026-10-29.

**Atlético PR (Heim, ID 622)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 16 | 17 | 6
Tore | 50 | 27 | 23 | 9
Gegentore | 40 | 15 | 25 | 9
Tore/Spiel | 1.52 | 1.69 | 1.35 | 1.50
Gegentore/Spiel | 1.21 | 0.94 | 1.47 | 1.50
xG für/Spiel | 1.48 | 1.74 | 1.24 | 1.89
xG gegen/Spiel | 1.39 | 1.06 | 1.71 | 1.49
Spiele mit xG | 33 | 16 | 17 | 6
S/U/N | 15/9/9 | 9/5/2 | 6/4/7 | 2/2/2
Punkte/Spiel | 1.64 | 2.00 | 1.29 | 1.33
BTTS % | 58 % | 56 % | 59 % | 67 %
Over 2,5 % | 48 % | 44 % | 53 % | 50 %
Under 2,5 % | 52 % | 56 % | 47 % | 50 %
Clean Sheets % | 24 % | 31 % | 18 % | 0 %
Failed to Score % | 24 % | 19 % | 29 % | 33 %
BTTS-and-lose % | 9 % | 0 % | 18 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Vasco da Gama (Gast, ID 625)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 32 | 17 | 15 | 6
Tore | 40 | 25 | 15 | 11
Gegentore | 49 | 24 | 25 | 8
Tore/Spiel | 1.25 | 1.47 | 1.00 | 1.83
Gegentore/Spiel | 1.53 | 1.41 | 1.67 | 1.33
xG für/Spiel | 1.88 | 2.14 | 1.59 | 2.06
xG gegen/Spiel | 1.27 | 1.22 | 1.33 | 1.05
Spiele mit xG | 32 | 17 | 15 | 6
S/U/N | 10/8/14 | 8/3/6 | 2/5/8 | 3/1/2
Punkte/Spiel | 1.19 | 1.59 | 0.73 | 1.67
BTTS % | 62 % | 59 % | 67 % | 50 %
Over 2,5 % | 59 % | 65 % | 53 % | 67 %
Under 2,5 % | 41 % | 35 % | 47 % | 33 %
Clean Sheets % | 12 % | 18 % | 7 % | 33 %
Failed to Score % | 31 % | 29 % | 33 % | 33 %
BTTS-and-lose % | 19 % | 12 % | 27 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Atlético PR: 20.09. H Bahia (1.61 PPG) 2:1 · 08.10. H Atlético Mineiro (1.52 PPG) 2:2 · 12.10. A Chapecoense (0.64 PPG) 4:1 · 17.10. H Palmeiras (2.12 PPG) 0:2 · 24.10. A Vitória (1.15 PPG) 1:1 · 30.10. A Grêmio (1.12 PPG) 0:2

Letzte 6 Vasco da Gama: 19.09. H Coritiba (1.24 PPG) 5:0 · 07.10. A Botafogo (1.18 PPG) 2:1 · 10.10. H Remo (0.88 PPG) 0:0 · 18.10. A São Paulo (1.30 PPG) 0:1 · 24.10. H Corinthians (1.09 PPG) 3:2 · 29.10. H Flamengo (2.21 PPG) 1:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Atlético PR [1, 2, 0, 1, 2, 2, 2, 4, 0, 1, 2, 0, 3, 0, 0, 1, 2, 1, 2, 2, 0, 2, 1, 3, 3, 1, 3, 2, 2, 4, 0, 1, 0]; Vasco da Gama [1, 1, 0, 1, 2, 3, 3, 2, 1, 1, 1, 2, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 1, 3, 0, 2, 5, 2, 0, 0, 3, 1]

**Bild:** Saison 2026 mit 33 bzw. 32 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Vasco auswärts mit 15 Toren in 15 Spielen, gegen Athleticos Heimabwehr mit 1,06 xG gegen; der Weg zu drei Toren ist mit 44 % Over in Athletico-Heimspielen unsicher und wird nicht gewählt; stärkstes Gegenargument sind Vascos hohe Chancenwerte (1,88 xG pro Spiel, in den letzten sechs 2,06) und Athleticos Form von 2-2-2 in den letzten sechs, die gegen Athleticos 9-5-2 daheim und Vascos 2-5-8 auswärts den Heimsieg (Modell 55 %) gefährden, aber nicht entkräften.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1472 Spiele, Saisons [9035, 11321, 14231, 16544]; Schätzung λ Heim 1.726, λ Gast 0.980. Prüfstand (unberührter Test, 148 Spiele ab 2026-07-23): Heimsieg besser als Grundrate (Brier 0.2307 gegen 0.2494); Auswärtssieg besser als Grundrate (Brier 0.1775 gegen 0.1875); BTTS Ja nicht besser als Grundrate (Brier 0.2533 gegen 0.2486); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2543 gegen 0.2525). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 55 % · Remis 24 % · Auswärtssieg 21 % · BTTS Ja 51 % · Over 2,5 51 % · Under 2,5 49 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.1 · X 3.39 · 2 3.4 · BTTS Ja 1.62 · Over 2,5 1.8 · Under 2,5 2.

**Auswahl:** Heimsieg

⚠️ Vasco mit 1,88 xG pro Spiel (zuletzt 2,06) – trotz schwacher Auswärtsbilanz reale Torgefahr.

---

## 1.3 Flamengo – Grêmio | 2026-11-04 22:30 UTC | Brasilien Série A 2026, Spieltag 34 | Match-ID 8409608

Analyse-ID: A-20261104-8409608-r1 · Team-IDs: 612 / 616 · Saison-ID: 16544 · Status beim Abruf: incomplete · Ort: Estadio Jornalista Mário Filho

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026: 33 bzw. 33 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-01-29 bis 2026-10-29, Gast 2026-01-28 bis 2026-10-30; letzte 6: Heim 2026-09-20–2026-10-29, Gast 2026-09-20–2026-10-30.

**Flamengo (Heim, ID 612)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 16 | 17 | 6
Tore | 68 | 32 | 36 | 15
Gegentore | 28 | 12 | 16 | 6
Tore/Spiel | 2.06 | 2.00 | 2.12 | 2.50
Gegentore/Spiel | 0.85 | 0.75 | 0.94 | 1.00
xG für/Spiel | 1.81 | 2.05 | 1.60 | 2.11
xG gegen/Spiel | 1.28 | 1.14 | 1.42 | 1.28
Spiele mit xG | 33 | 16 | 17 | 6
S/U/N | 22/7/4 | 12/3/1 | 10/4/3 | 5/1/0
Punkte/Spiel | 2.21 | 2.44 | 2.00 | 2.67
BTTS % | 52 % | 44 % | 59 % | 67 %
Over 2,5 % | 64 % | 56 % | 71 % | 83 %
Under 2,5 % | 36 % | 44 % | 29 % | 17 %
Clean Sheets % | 42 % | 50 % | 35 % | 33 %
Failed to Score % | 6 % | 6 % | 6 % | 0 %
BTTS-and-lose % | 6 % | 0 % | 12 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Grêmio (Gast, ID 616)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 17 | 16 | 6
Tore | 37 | 27 | 10 | 7
Gegentore | 44 | 21 | 23 | 6
Tore/Spiel | 1.12 | 1.59 | 0.62 | 1.17
Gegentore/Spiel | 1.33 | 1.24 | 1.44 | 1.00
xG für/Spiel | 1.31 | 1.51 | 1.10 | 1.58
xG gegen/Spiel | 1.69 | 1.72 | 1.66 | 1.95
Spiele mit xG | 33 | 17 | 16 | 6
S/U/N | 9/10/14 | 8/5/4 | 1/5/10 | 2/3/1
Punkte/Spiel | 1.12 | 1.71 | 0.50 | 1.50
BTTS % | 58 % | 65 % | 50 % | 50 %
Over 2,5 % | 42 % | 47 % | 38 % | 17 %
Under 2,5 % | 58 % | 53 % | 62 % | 83 %
Clean Sheets % | 24 % | 29 % | 19 % | 50 %
Failed to Score % | 30 % | 18 % | 44 % | 17 %
BTTS-and-lose % | 24 % | 18 % | 31 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Flamengo: 20.09. H Bragantino (1.38 PPG) 2:1 · 08.10. A Santos (1.38 PPG) 2:2 · 11.10. H Fluminense (1.64 PPG) 1:0 · 18.10. A Bahia (1.61 PPG) 3:0 · 26.10. H Atlético Mineiro (1.52 PPG) 3:2 · 29.10. A Vasco da Gama (1.19 PPG) 4:1

Letzte 6 Grêmio: 20.09. H Palmeiras (2.12 PPG) 0:0 · 07.10. A Remo (0.88 PPG) 1:1 · 11.10. H Internacional (1.12 PPG) 1:1 · 18.10. H Cruzeiro (1.73 PPG) 2:4 · 26.10. A Coritiba (1.24 PPG) 1:0 · 30.10. H Atlético PR (1.64 PPG) 2:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Flamengo [1, 1, 2, 2, 3, 3, 1, 0, 3, 2, 2, 4, 2, 1, 1, 0, 3, 4, 1, 1, 2, 5, 1, 3, 2, 1, 2, 2, 2, 1, 3, 3, 4]; Grêmio [1, 5, 0, 2, 1, 1, 2, 1, 1, 0, 0, 0, 1, 0, 0, 1, 3, 1, 1, 1, 2, 0, 0, 3, 0, 1, 2, 0, 1, 1, 2, 1, 2]

**Bild:** Saison 2026 mit je 33 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Grêmio auswärts mit 10 Toren in 16 Spielen und 44 % torlosen Spielen, gegen Flamengos Heimabwehr mit 50 % Clean Sheets; der Weg zu drei Toren hängt vor allem an Flamengo und wird nicht gewählt; stärkstes Gegenargument ist Grêmios verbesserte Form mit 2-3-1 und 50 % Clean Sheets in den letzten sechs, die gegen Flamengos 12-3-1 daheim und 5-1-0 in den letzten sechs sowie Grêmios 1-5-10 auswärts den Heimsieg (Modell 67 %) aber nicht entkräftet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1472 Spiele, Saisons [9035, 11321, 14231, 16544]; Schätzung λ Heim 2.174, λ Gast 0.857. Prüfstand (unberührter Test, 148 Spiele ab 2026-07-23): Heimsieg besser als Grundrate (Brier 0.2307 gegen 0.2494); Auswärtssieg besser als Grundrate (Brier 0.1775 gegen 0.1875); BTTS Ja nicht besser als Grundrate (Brier 0.2533 gegen 0.2486); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2543 gegen 0.2525). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 67 % · Remis 19 % · Auswärtssieg 14 % · BTTS Ja 51 % · Over 2,5 58 % · Under 2,5 42 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.17 · X 8 · 2 13 · BTTS Ja 1.88 · Over 2,5 1.29 · Under 2,5 3.4.

**Auswahl:** Heimsieg

---

## 1.4 Cúcuta Deportivo – Santa Fe | 2026-11-04 23:30 UTC | Kolumbien Primera A 2026, Spieltag 17 | Match-ID 8544015

Analyse-ID: A-20261104-8544015-r1 · Team-IDs: 2153 / 2133 · Saison-ID: 16614 · Status beim Abruf: incomplete · Ort: Estadio General Santander · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026: 35 bzw. 35 Ligaspiele; xG für alle Spiele; 14 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-01-19 bis 2026-10-27, Gast 2026-01-19 bis 2026-10-30; letzte 6: Heim 2026-09-26–2026-10-27, Gast 2026-09-29–2026-10-30.

**Cúcuta Deportivo (Heim, ID 2153)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 35 | 17 | 18 | 6
Tore | 40 | 24 | 16 | 9
Gegentore | 59 | 21 | 38 | 6
Tore/Spiel | 1.14 | 1.41 | 0.89 | 1.50
Gegentore/Spiel | 1.69 | 1.24 | 2.11 | 1.00
xG für/Spiel | 1.14 | 1.16 | 1.13 | 1.24
xG gegen/Spiel | 1.69 | 1.58 | 1.81 | 1.60
Spiele mit xG | 35 | 17 | 18 | 6
S/U/N | 9/10/16 | 7/5/5 | 2/5/11 | 4/0/2
Punkte/Spiel | 1.06 | 1.53 | 0.61 | 2.00
BTTS % | 57 % | 59 % | 56 % | 33 %
Over 2,5 % | 51 % | 47 % | 56 % | 50 %
Under 2,5 % | 49 % | 53 % | 44 % | 50 %
Clean Sheets % | 23 % | 29 % | 17 % | 50 %
Failed to Score % | 23 % | 12 % | 33 % | 17 %
BTTS-and-lose % | 26 % | 18 % | 33 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Santa Fe (Gast, ID 2133)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 35 | 18 | 17 | 6
Tore | 52 | 31 | 21 | 7
Gegentore | 39 | 19 | 20 | 6
Tore/Spiel | 1.49 | 1.72 | 1.24 | 1.17
Gegentore/Spiel | 1.11 | 1.06 | 1.18 | 1.00
xG für/Spiel | 1.46 | 1.58 | 1.33 | 1.43
xG gegen/Spiel | 1.42 | 1.26 | 1.58 | 1.50
Spiele mit xG | 35 | 18 | 17 | 6
S/U/N | 15/12/8 | 9/6/3 | 6/6/5 | 4/0/2
Punkte/Spiel | 1.63 | 1.83 | 1.41 | 2.00
BTTS % | 69 % | 67 % | 71 % | 50 %
Over 2,5 % | 51 % | 61 % | 41 % | 50 %
Under 2,5 % | 49 % | 39 % | 59 % | 50 %
Clean Sheets % | 17 % | 22 % | 12 % | 17 %
Failed to Score % | 17 % | 17 % | 18 % | 33 %
BTTS-and-lose % | 9 % | 6 % | 12 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Cúcuta Deportivo: 26.09. H Llaneros (1.17 PPG) 2:1 · 04.10. H Deportivo Pereira (0.75 PPG) 4:0 · 11.10. A Boyacá Chicó (0.92 PPG) 1:0 · 20.10. H Atlético Nacional (2.11 PPG) 1:0 · 24.10. A América de Cali (1.91 PPG) 1:3 · 27.10. H Rionegro Águilas (1.42 PPG) 0:2

Letzte 6 Santa Fe: 29.09. A Deportivo Pereira (0.75 PPG) 2:1 · 06.10. A Independiente Medellín (1.44 PPG) 1:0 · 18.10. A Llaneros (1.17 PPG) 0:1 · 22.10. H Jaguares de Córdoba (0.86 PPG) 2:1 · 27.10. H Atlético Bucaramanga (1.44 PPG) 2:1 · 30.10. A Atlético Nacional (2.11 PPG) 0:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Cúcuta Deportivo [1, 1, 2, 1, 2, 1, 1, 3, 2, 0, 0, 2, 2, 1, 0, 2, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 2, 1, 0, 2, 4, 1, 1, 1, 0]; Santa Fe [1, 1, 2, 1, 1, 0, 1, 2, 1, 1, 1, 2, 2, 0, 2, 1, 5, 2, 3, 1, 2, 2, 0, 1, 3, 2, 1, 4, 0, 2, 1, 0, 2, 2, 0]

**Bild:** Saison 2026 mit je 35 Spielen und voller xG-Abdeckung ist verwendbar, K.-o.-Spiele ausgeschlossen; schwächere Offensive ist Cúcuta mit 1,16 xG daheim, das aber in 15 von 17 Heimspielen traf gegen Santa Fe mit nur 12 % Auswärts-Clean-Sheets, während Santa Fe in 14 von 17 Auswärtsspielen traf gegen Cúcutas Heimabwehr mit 29 % Clean Sheets; der Weg zu drei Toren ist mit 47 % bzw. 41 % Over beider Kontexte schwächer belegt als BTTS (Modell 52 %); stärkstes Gegenargument sind Cúcutas 3 Zu-null-Spiele in den letzten sechs, die den Gästetreffer gefährden und als wesentliche Gefahr gewichtet werden.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1681 Spiele, Saisons [8936, 10997, 14086, 16614]; Schätzung λ Heim 1.222, λ Gast 1.352. Prüfstand (unberührter Test, 169 Spiele ab 2026-05-03): Heimsieg besser als Grundrate (Brier 0.2319 gegen 0.2476); Auswärtssieg besser als Grundrate (Brier 0.1717 gegen 0.1869); BTTS Ja nicht besser als Grundrate (Brier 0.2639 gegen 0.2541); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2523 gegen 0.2525). Grenzen: 26 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 34 % · Remis 26 % · Auswärtssieg 40 % · BTTS Ja 52 % · Over 2,5 48 % · Under 2,5 52 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.6 · X 3.15 · 2 2.5 · BTTS Ja 1.73 · Over 2,5 2 · Under 2,5 1.8.

**Auswahl:** BTTS Ja

⚠️ Cúcuta hielt in den letzten 6 Spielen dreimal die Null – Gefahr für den Santa-Fe-Treffer.

---

## 1.5 Wrexham – Middlesbrough | 2026-11-04 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566633

Analyse-ID: A-20261104-8566633-r1 · Team-IDs: 1837 / 147 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: Racecourse Ground

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-17 bis 2026-10-30, Gast 2026-08-15 bis 2026-10-31; letzte 6: Heim 2026-09-19–2026-10-30, Gast 2026-09-19–2026-10-31.

**Wrexham (Heim, ID 1837)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 15 | 10 | 5 | 8
Gegentore | 19 | 8 | 11 | 8
Tore/Spiel | 1.15 | 1.67 | 0.71 | 1.33
Gegentore/Spiel | 1.46 | 1.33 | 1.57 | 1.33
xG für/Spiel | 1.32 | 1.39 | 1.26 | 1.38
xG gegen/Spiel | 1.38 | 1.41 | 1.36 | 1.47
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 3/5/5 | 2/2/2 | 1/3/3 | 2/1/3
Punkte/Spiel | 1.08 | 1.33 | 0.86 | 1.17
BTTS % | 62 % | 100 % | 29 % | 67 %
Over 2,5 % | 46 % | 67 % | 29 % | 50 %
Under 2,5 % | 54 % | 33 % | 71 % | 50 %
Clean Sheets % | 15 % | 0 % | 29 % | 0 %
Failed to Score % | 31 % | 0 % | 57 % | 33 %
BTTS-and-lose % | 15 % | 33 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Middlesbrough (Gast, ID 147)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 30 | 17 | 13 | 16
Gegentore | 17 | 9 | 8 | 7
Tore/Spiel | 2.31 | 2.43 | 2.17 | 2.67
Gegentore/Spiel | 1.31 | 1.29 | 1.33 | 1.17
xG für/Spiel | 2.14 | 2.22 | 2.06 | 2.38
xG gegen/Spiel | 1.22 | 1.17 | 1.28 | 1.11
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 8/4/1 | 5/2/0 | 3/2/1 | 4/2/0
Punkte/Spiel | 2.15 | 2.43 | 1.83 | 2.33
BTTS % | 77 % | 71 % | 83 % | 67 %
Over 2,5 % | 77 % | 86 % | 67 % | 83 %
Under 2,5 % | 23 % | 14 % | 33 % | 17 %
Clean Sheets % | 23 % | 29 % | 17 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 8 % | 0 % | 17 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Wrexham: 19.09. H Southampton (2.00 PPG) 2:1 · 10.10. A Derby County (0.50 PPG) 1:1 · 13.10. H West Bromwich Albion (1.79 PPG) 1:2 · 17.10. H Preston North End (0.36 PPG) 4:1 · 24.10. A Blackburn Rovers (1.29 PPG) 0:2 · 30.10. A Sheffield United (1.57 PPG) 0:1

Letzte 6 Middlesbrough: 19.09. A Birmingham City (1.86 PPG) 2:2 · 10.10. H Wolverhampton Wanderers (1.85 PPG) 1:0 · 13.10. A Stoke City (1.86 PPG) 3:2 · 17.10. H Cardiff City (1.08 PPG) 2:2 · 23.10. A Bolton Wanderers (1.21 PPG) 5:1 · 31.10. H Charlton Athletic (1.00 PPG) 3:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Wrexham [1, 1, 1, 3, 0, 1, 0, 2, 1, 1, 4, 0, 0]; Middlesbrough [2, 1, 3, 1, 1, 4, 2, 2, 1, 3, 2, 5, 3]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Wrexham mit 1,32 xG, das aber in allen 6 Heimspielen traf gegen Middlesbrough mit nur 17 % Auswärts-Clean-Sheets, während Middlesbrough in allen 13 Saisonspielen traf (2,14 xG) gegen Wrexhams Heimabwehr ohne Clean Sheet; der Weg zu drei Toren ist mit 67 % Over in beiden Kontexten ebenfalls plausibel, BTTS ist durch beide eigenen Torserien aber direkter belegt (Modell 56 %); stärkstes Gegenargument sind Wrexhams zwei torlose Spiele in den letzten sechs, die aber auswärts entstanden und keine wesentliche Gefahr für den Heimtreffer begründen.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1821 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.445, λ Gast 1.304. Prüfstand (unberührter Test, 183 Spiele ab 2026-04-25): Heimsieg besser als Grundrate (Brier 0.2422 gegen 0.2447); Auswärtssieg besser als Grundrate (Brier 0.2165 gegen 0.219); BTTS Ja nicht besser als Grundrate (Brier 0.2467 gegen 0.2433); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2592 gegen 0.2533). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 41 % · Remis 25 % · Auswärtssieg 34 % · BTTS Ja 56 % · Over 2,5 52 % · Under 2,5 48 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 4.21 · X 3.9 · 2 1.72 · BTTS Ja 1.6 · Over 2,5 1.58 · Under 2,5 2.3.

**Auswahl:** BTTS Ja

---
