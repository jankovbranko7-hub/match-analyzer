# Vorabeintrag Batch 8 · 02.11.2026 · Revision r2

**Revision r2** (vor allen Anstößen erstellt, ersetzt r1 in `../batch-8.md`; r1 bleibt unverändert erhalten). Für die Auswertung zählt r2 für alle 40 Spiele. Gründe: (1) K.-o.-/Play-off-Runden (alle Spiele mit Spieltag 0) aus Training und Tabellen ausgeschlossen, weil Verlängerung und neutraler Ort für sie nicht ausgeschlossen werden können (Abschnitt 5.2); das API-Feld no_home_away ist saisonweise uneinheitlich gesetzt und wird nicht als Kennzeichnung neutraler Plätze verwendet; (2) der in r1 eigenmächtig eingeführte Grundraten-Maßstab („Markt unbrauchbar“) ist auf Nutzeranweisung gestrichen, der Testbefund steht nur noch im Modellfeld; (3) xG-Werte 0,00 werden als beobachtete 0 übernommen; (4) Datenbasis „eingeschränkt“ nur bei konkreten Datenlücken, Umfang wird immer genannt; (5) Rohdaten-Snapshot liegt als `../rohdaten.tar.xz` bei.

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-02 10:09 UTC
- Eintrag erstellt: 2026-11-02 10:42:04 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen der jeweiligen Ligasaison berechnet (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 8.1 RCD Mallorca – Cádiz | 2026-11-02 20:00 UTC | Spanien Segunda División 2026/2027, Spieltag 12 | Match-ID 8584339

Analyse-ID: A-20261102-8584339-r2 · Team-IDs: 298 / 310 · Saison-ID: 17269 · Status beim Abruf: incomplete · Ort: Estadio Iberoamericano 2010

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 11 bzw. 11 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-24, Gast 2026-08-15 bis 2026-10-25; letzte 6: Heim 2026-09-19–2026-10-24, Gast 2026-09-19–2026-10-25.

**RCD Mallorca (Heim, ID 298)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 13 | 10 | 3 | 6
Gegentore | 6 | 2 | 4 | 4
Tore/Spiel | 1.18 | 2.00 | 0.50 | 1.00
Gegentore/Spiel | 0.55 | 0.40 | 0.67 | 0.67
xG für/Spiel | 1.35 | 1.45 | 1.26 | 1.30
xG gegen/Spiel | 1.19 | 1.00 | 1.35 | 1.22
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 5/4/2 | 4/0/1 | 1/4/1 | 2/3/1
Punkte/Spiel | 1.73 | 2.40 | 1.17 | 1.50
BTTS % | 27 % | 20 % | 33 % | 50 %
Over 2,5 % | 18 % | 40 % | 0 % | 17 %
Under 2,5 % | 82 % | 60 % | 100 % | 83 %
Clean Sheets % | 55 % | 60 % | 50 % | 33 %
Failed to Score % | 36 % | 20 % | 50 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Cádiz (Gast, ID 310)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 7 | 4 | 6
Tore | 14 | 9 | 5 | 9
Gegentore | 14 | 6 | 8 | 7
Tore/Spiel | 1.27 | 1.29 | 1.25 | 1.50
Gegentore/Spiel | 1.27 | 0.86 | 2.00 | 1.17
xG für/Spiel | 1.24 | 1.37 | 1.00 | 1.39
xG gegen/Spiel | 1.49 | 1.52 | 1.44 | 1.44
Spiele mit xG | 11 | 7 | 4 | 6
S/U/N | 2/4/5 | 2/2/3 | 0/2/2 | 2/1/3
Punkte/Spiel | 0.91 | 1.14 | 0.50 | 1.17
BTTS % | 55 % | 43 % | 75 % | 50 %
Over 2,5 % | 45 % | 43 % | 50 % | 50 %
Under 2,5 % | 55 % | 57 % | 50 % | 50 %
Clean Sheets % | 18 % | 29 % | 0 % | 17 %
Failed to Score % | 36 % | 43 % | 25 % | 33 %
BTTS-and-lose % | 18 % | 14 % | 25 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 RCD Mallorca: 19.09. A Real Sociedad II (0.92 PPG) 1:0 · 27.09. H Almería (2.17 PPG) 0:1 · 04.10. A Girona FC (1.75 PPG) 0:0 · 11.10. H UD Las Palmas (1.27 PPG) 3:1 · 17.10. A SD Eibar (1.92 PPG) 1:1 · 24.10. A Leganés (1.09 PPG) 1:1

Letzte 6 Cádiz: 19.09. H Girona FC (1.75 PPG) 1:2 · 26.09. A CD Tenerife (1.27 PPG) 1:1 · 03.10. H Leganés (1.09 PPG) 4:0 · 11.10. H Sporting Gijón (1.83 PPG) 0:1 · 18.10. A Granada CF (1.92 PPG) 0:2 · 25.10. H Ceuta (0.42 PPG) 3:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): RCD Mallorca [2, 0, 3, 0, 2, 1, 0, 0, 3, 1, 1]; Cádiz [0, 2, 1, 2, 0, 1, 1, 4, 0, 0, 3]

**Bild:** Saison 2026/27 mit 11 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Cádiz auswärts mit 5 Toren in 4 Spielen und 1,00 xG, gegen Mallorcas Heimabwehr mit 2 Gegentoren in 5 und 60 % Clean Sheets; der Weg zu drei Toren ist schwach und wird nicht gewählt; stärkstes Gegenargument ist Mallorcas Remisneigung mit drei Remis in den letzten sechs Spielen, die aber auswärts entstanden, während Mallorca daheim 4-0-1 steht und Cádiz auswärts sieglos ist, sodass der Heimsieg (Modell 53 %) getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1514 Spiele, Saisons [9675, 12467, 15066, 17269]; Schätzung λ Heim 1.443, λ Gast 0.771. Prüfstand (unberührter Test, 152 Spiele ab 2026-05-17): Heimsieg besser als Grundrate (Brier 0.2375 gegen 0.2479); Auswärtssieg besser als Grundrate (Brier 0.2036 gegen 0.2221); BTTS Ja nicht besser als Grundrate (Brier 0.2505 gegen 0.2499); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2451 gegen 0.2491). Grenzen: 18 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 53 % · Remis 27 % · Auswärtssieg 20 % · BTTS Ja 41 % · Over 2,5 38 % · Under 2,5 62 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.47 · X 3.9 · 2 6 · BTTS Ja 1.95 · Over 2,5 1.87 · Under 2,5 1.97.

**Auswahl:** Heimsieg

---

## 8.2 GAIS – AIK | 2026-11-02 18:00 UTC | Schweden Allsvenskan 2026, Spieltag 27 | Match-ID 8420248

Analyse-ID: A-20261102-8420248-r2 · Team-IDs: 679 / 661 · Saison-ID: 16576 · Status beim Abruf: incomplete · Ort: Gamla Ullevi

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026: 26 bzw. 26 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-04-06 bis 2026-10-29, Gast 2026-04-05 bis 2026-10-27; letzte 6: Heim 2026-09-14–2026-10-29, Gast 2026-09-16–2026-10-27.

**GAIS (Heim, ID 679)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 26 | 13 | 13 | 6
Tore | 32 | 17 | 15 | 7
Gegentore | 26 | 6 | 20 | 8
Tore/Spiel | 1.23 | 1.31 | 1.15 | 1.17
Gegentore/Spiel | 1.00 | 0.46 | 1.54 | 1.33
xG für/Spiel | 1.67 | 1.78 | 1.56 | 1.51
xG gegen/Spiel | 1.38 | 1.25 | 1.51 | 1.49
Spiele mit xG | 26 | 13 | 13 | 6
S/U/N | 9/7/10 | 5/5/3 | 4/2/7 | 2/1/3
Punkte/Spiel | 1.31 | 1.54 | 1.08 | 1.17
BTTS % | 35 % | 23 % | 46 % | 33 %
Over 2,5 % | 35 % | 23 % | 46 % | 33 %
Under 2,5 % | 65 % | 77 % | 54 % | 67 %
Clean Sheets % | 42 % | 54 % | 31 % | 33 %
Failed to Score % | 31 % | 38 % | 23 % | 33 %
BTTS-and-lose % | 15 % | 0 % | 31 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**AIK (Gast, ID 661)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 26 | 13 | 13 | 6
Tore | 42 | 21 | 21 | 13
Gegentore | 45 | 29 | 16 | 14
Tore/Spiel | 1.62 | 1.62 | 1.62 | 2.17
Gegentore/Spiel | 1.73 | 2.23 | 1.23 | 2.33
xG für/Spiel | 1.52 | 1.77 | 1.28 | 1.72
xG gegen/Spiel | 1.74 | 1.73 | 1.75 | 1.85
Spiele mit xG | 26 | 13 | 13 | 6
S/U/N | 10/8/8 | 4/3/6 | 6/5/2 | 1/3/2
Punkte/Spiel | 1.46 | 1.15 | 1.77 | 1.00
BTTS % | 73 % | 62 % | 85 % | 100 %
Over 2,5 % | 69 % | 69 % | 69 % | 83 %
Under 2,5 % | 31 % | 31 % | 31 % | 17 %
Clean Sheets % | 15 % | 15 % | 15 % | 0 %
Failed to Score % | 19 % | 23 % | 15 % | 0 %
BTTS-and-lose % | 19 % | 23 % | 15 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 GAIS: 14.09. A Djurgården (1.93 PPG) 0:2 · 20.09. A Mjällby (1.00 PPG) 3:0 · 10.10. H Sirius (2.12 PPG) 0:1 · 18.10. A Örgryte (0.70 PPG) 2:4 · 25.10. H IFK Göteborg (1.41 PPG) 1:1 · 29.10. A Kalmar (0.85 PPG) 1:0

Letzte 6 AIK: 16.09. H Mjällby (1.00 PPG) 1:1 · 20.09. A Halmstad (0.65 PPG) 1:2 · 10.10. H Brommapojkarna (1.26 PPG) 5:6 · 17.10. H IFK Göteborg (1.41 PPG) 2:2 · 24.10. A Sirius (2.12 PPG) 2:1 · 27.10. H Elfsborg (1.70 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): GAIS [0, 1, 1, 0, 2, 4, 1, 1, 2, 1, 3, 1, 1, 0, 1, 2, 0, 0, 4, 0, 0, 3, 0, 2, 1, 1]; AIK [2, 2, 1, 1, 0, 1, 2, 1, 2, 0, 2, 2, 2, 0, 0, 4, 3, 3, 0, 1, 1, 1, 5, 2, 2, 2]

**Bild:** Saison 2026 mit je 26 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist AIK auswärts mit 1,28 xG, aber 21 Toren in 13 Spielen, gegen GAIS' Heimabwehr mit 6 Gegentoren in 13; der Weg zu drei Toren ist widersprüchlich, weil GAIS daheim 77 % Under, AIK auswärts aber 69 % Over hat; stärkstes Gegenargument gegen den Modell-Heimsieg (46 %) ist AIKs Auswärtsbilanz von 6-5-2 mit 1,77 Punkten pro Spiel, sodass kein Markt widerspruchsfrei getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 933 Spiele, Saisons [8737, 17350, 16263, 16576]; Schätzung λ Heim 1.379, λ Gast 0.982. Prüfstand (unberührter Test, 94 Spiele ab 2026-08-08): Heimsieg besser als Grundrate (Brier 0.2184 gegen 0.2416); Auswärtssieg besser als Grundrate (Brier 0.2281 gegen 0.244); BTTS Ja nicht besser als Grundrate (Brier 0.2669 gegen 0.2572); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2449 gegen 0.252). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 46 % · Remis 27 % · Auswärtssieg 27 % · BTTS Ja 47 % · Over 2,5 42 % · Under 2,5 58 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.78 · X 3.7 · 2 3.85 · BTTS Ja 1.53 · Over 2,5 1.6 · Under 2,5 2.32.

**Auswahl:** keine – Grund siehe Bild.

---

## 8.3 Mjällby – Kalmar | 2026-11-02 18:00 UTC | Schweden Allsvenskan 2026, Spieltag 27 | Match-ID 8420303

Analyse-ID: A-20261102-8420303-r2 · Team-IDs: 671 / 666 · Saison-ID: 16576 · Status beim Abruf: incomplete · Ort: Strandvallen

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026: 26 bzw. 26 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-04-04 bis 2026-10-29, Gast 2026-04-05 bis 2026-10-29; letzte 6: Heim 2026-09-16–2026-10-29, Gast 2026-09-13–2026-10-29.

**Mjällby (Heim, ID 671)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 26 | 13 | 13 | 6
Tore | 30 | 12 | 18 | 4
Gegentore | 43 | 21 | 22 | 9
Tore/Spiel | 1.15 | 0.92 | 1.38 | 0.67
Gegentore/Spiel | 1.65 | 1.62 | 1.69 | 1.50
xG für/Spiel | 1.46 | 1.58 | 1.35 | 1.44
xG gegen/Spiel | 1.72 | 1.56 | 1.88 | 1.72
Spiele mit xG | 26 | 13 | 13 | 6
S/U/N | 6/8/12 | 3/2/8 | 3/6/4 | 1/2/3
Punkte/Spiel | 1.00 | 0.85 | 1.15 | 0.83
BTTS % | 50 % | 31 % | 69 % | 50 %
Over 2,5 % | 46 % | 38 % | 54 % | 33 %
Under 2,5 % | 54 % | 62 % | 46 % | 67 %
Clean Sheets % | 15 % | 23 % | 8 % | 0 %
Failed to Score % | 42 % | 54 % | 31 % | 50 %
BTTS-and-lose % | 12 % | 15 % | 8 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Kalmar (Gast, ID 666)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 26 | 13 | 13 | 6
Tore | 23 | 14 | 9 | 2
Gegentore | 42 | 21 | 21 | 12
Tore/Spiel | 0.88 | 1.08 | 0.69 | 0.33
Gegentore/Spiel | 1.62 | 1.62 | 1.62 | 2.00
xG für/Spiel | 1.47 | 1.35 | 1.59 | 1.47
xG gegen/Spiel | 1.50 | 1.43 | 1.56 | 1.52
Spiele mit xG | 26 | 13 | 13 | 6
S/U/N | 6/4/16 | 5/2/6 | 1/2/10 | 1/0/5
Punkte/Spiel | 0.85 | 1.31 | 0.38 | 0.50
BTTS % | 38 % | 38 % | 38 % | 17 %
Over 2,5 % | 50 % | 62 % | 38 % | 50 %
Under 2,5 % | 50 % | 38 % | 62 % | 50 %
Clean Sheets % | 12 % | 15 % | 8 % | 0 %
Failed to Score % | 54 % | 46 % | 62 % | 83 %
BTTS-and-lose % | 12 % | 0 % | 23 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Mjällby: 16.09. A AIK (1.46 PPG) 1:1 · 20.09. H GAIS (1.31 PPG) 0:3 · 10.10. H Degerfors (0.74 PPG) 1:1 · 18.10. A Västerås SK (1.63 PPG) 0:1 · 25.10. H Hammarby (2.04 PPG) 0:2 · 29.10. A Örgryte (0.70 PPG) 2:1

Letzte 6 Kalmar: 13.09. A Elfsborg (1.70 PPG) 0:1 · 20.09. H Häcken (1.81 PPG) 0:5 · 12.10. A Malmö FF (1.48 PPG) 0:1 · 19.10. A Degerfors (0.74 PPG) 2:1 · 24.10. H Brommapojkarna (1.26 PPG) 0:3 · 29.10. H GAIS (1.31 PPG) 0:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Mjällby [0, 0, 3, 0, 2, 3, 4, 0, 1, 1, 4, 1, 0, 1, 0, 4, 0, 0, 1, 1, 1, 0, 1, 0, 0, 2]; Kalmar [0, 2, 0, 1, 2, 2, 2, 0, 2, 0, 3, 0, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0]

**Bild:** Saison 2026 mit je 26 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Kalmar mit 0,88 Toren/Spiel und auswärts 62 % torlosen Spielen (83 % in den letzten sechs), aber auch Mjällby blieb daheim in 54 % der Spiele torlos; der Weg zu drei Toren ist schwach, weil Mjällby daheim nur 12 Tore in 13 erzielte, beide im jeweiligen Kontext 62 % Under haben und das Modell 47 % Over schätzt; stärkstes Gegenargument sind beide anfälligen Abwehrreihen (je über 1,6 Gegentore/Spiel), über die ein einseitiges 3:0 möglich bleibt, was gegen die beidseitige Torarmut aber geringer wiegt.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 933 Spiele, Saisons [8737, 17350, 16263, 16576]; Schätzung λ Heim 1.696, λ Gast 0.867. Prüfstand (unberührter Test, 94 Spiele ab 2026-08-08): Heimsieg besser als Grundrate (Brier 0.2184 gegen 0.2416); Auswärtssieg besser als Grundrate (Brier 0.2281 gegen 0.244); BTTS Ja nicht besser als Grundrate (Brier 0.2669 gegen 0.2572); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2449 gegen 0.252). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 57 % · Remis 24 % · Auswärtssieg 19 % · BTTS Ja 47 % · Over 2,5 47 % · Under 2,5 53 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.42 · X 3.4 · 2 2.72 · BTTS Ja 1.68 · Over 2,5 1.95 · Under 2,5 1.86.

**Auswahl:** Under 2,5

---

## 8.4 Gençlerbirliği – Alanyaspor | 2026-11-02 17:00 UTC | Türkei Süper Lig 2026/2027, Spieltag 10 | Match-ID 8583480

Analyse-ID: A-20261102-8583480-r2 · Team-IDs: 199 / 189 · Saison-ID: 17265 · Status beim Abruf: incomplete · Ort: Eryaman Stadyumu

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 9 bzw. 9 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-15 bis 2026-10-25, Gast 2026-08-15 bis 2026-10-23; letzte 6: Heim 2026-09-06–2026-10-25, Gast 2026-09-07–2026-10-23.

**Gençlerbirliği (Heim, ID 199)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 7 | 6 | 1 | 3
Gegentore | 18 | 7 | 11 | 16
Tore/Spiel | 0.78 | 1.20 | 0.25 | 0.50
Gegentore/Spiel | 2.00 | 1.40 | 2.75 | 2.67
xG für/Spiel | 1.27 | 1.48 | 1.00 | 1.28
xG gegen/Spiel | 2.01 | 1.88 | 2.16 | 1.98
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 2/2/5 | 1/2/2 | 1/0/3 | 0/1/5
Punkte/Spiel | 0.89 | 1.00 | 0.75 | 0.17
BTTS % | 44 % | 80 % | 0 % | 33 %
Over 2,5 % | 56 % | 60 % | 50 % | 67 %
Under 2,5 % | 44 % | 40 % | 50 % | 33 %
Clean Sheets % | 11 % | 0 % | 25 % | 0 %
Failed to Score % | 44 % | 20 % | 75 % | 67 %
BTTS-and-lose % | 11 % | 20 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Alanyaspor (Gast, ID 189)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 9 | 4 | 5 | 6
Gegentore | 11 | 4 | 7 | 8
Tore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
Gegentore/Spiel | 1.22 | 1.00 | 1.40 | 1.33
xG für/Spiel | 1.22 | 1.46 | 1.03 | 1.37
xG gegen/Spiel | 1.68 | 1.62 | 1.73 | 1.78
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 3/3/3 | 1/2/1 | 2/1/2 | 2/2/2
Punkte/Spiel | 1.33 | 1.25 | 1.40 | 1.33
BTTS % | 56 % | 50 % | 60 % | 50 %
Over 2,5 % | 56 % | 50 % | 60 % | 67 %
Under 2,5 % | 44 % | 50 % | 40 % | 33 %
Clean Sheets % | 33 % | 50 % | 20 % | 33 %
Failed to Score % | 22 % | 25 % | 20 % | 33 %
BTTS-and-lose % | 22 % | 25 % | 20 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Gençlerbirliği: 06.09. A Trabzonspor (2.20 PPG) 0:5 · 13.09. H Kasımpaşa (1.70 PPG) 1:2 · 19.09. A İstanbul Başakşehir (1.40 PPG) 0:4 · 10.10. H Amed (2.30 PPG) 2:2 · 17.10. H Galatasaray (2.50 PPG) 0:1 · 25.10. A Konyaspor (0.80 PPG) 0:2

Letzte 6 Alanyaspor: 07.09. A Rizespor (1.10 PPG) 1:0 · 12.09. H Göztepe (1.50 PPG) 2:2 · 19.09. A Çorum Belediyespor (1.60 PPG) 2:1 · 10.10. H BB Erzurumspor (1.40 PPG) 0:0 · 17.10. A Fenerbahçe (1.60 PPG) 0:3 · 23.10. H Kocaelispor (1.60 PPG) 1:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Gençlerbirliği [2, 1, 1, 0, 1, 0, 2, 0, 0]; Alanyaspor [1, 1, 1, 1, 2, 2, 0, 0, 1]

**Bild:** Saison 2026/27 mit je 9 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Gençlerbirliği mit 7 Toren in 9 und nur 3 Toren in den letzten sechs, gegen Alanyaspors Abwehr mit 33 % Clean Sheets; ein Weg zu drei Toren ist mit je 56 % Over beider Teams unklar; stärkstes Gegenargument gegen jede Siegauswahl ist das ausgeglichene Modell (Heim 37 %, Auswärts 35 %), sodass kein Markt getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1117 Spiele, Saisons [9913, 12641, 14972, 17265]; Schätzung λ Heim 1.175, λ Gast 1.127. Prüfstand (unberührter Test, 112 Spiele ab 2026-05-02): Heimsieg besser als Grundrate (Brier 0.2392 gegen 0.2514); Auswärtssieg besser als Grundrate (Brier 0.2087 gegen 0.2195); BTTS Ja besser als Grundrate (Brier 0.247 gegen 0.2539); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2368 gegen 0.2446). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 37 % · Remis 28 % · Auswärtssieg 35 % · BTTS Ja 47 % · Over 2,5 40 % · Under 2,5 60 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.62 · X 3.4 · 2 2.57 · BTTS Ja 1.8 · Over 2,5 2.07 · Under 2,5 1.75.

**Auswahl:** keine – Grund siehe Bild.

---

## 8.5 Kayserispor – Muğlaspor | 2026-11-02 17:00 UTC | Türkei 1. Lig 2026/2027, Spieltag 13 | Match-ID 8589131

Analyse-ID: A-20261102-8589131-r2 · Team-IDs: 193 / 11090 · Saison-ID: 17290 · Status beim Abruf: incomplete · Ort: Kadir Has Şehir Stadı

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-09 bis 2026-10-25, Gast 2026-08-09 bis 2026-10-24; letzte 6: Heim 2026-09-14–2026-10-25, Gast 2026-09-13–2026-10-24.

**Kayserispor (Heim, ID 193)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 5 | 7 | 6
Tore | 26 | 12 | 14 | 16
Gegentore | 9 | 6 | 3 | 6
Tore/Spiel | 2.17 | 2.40 | 2.00 | 2.67
Gegentore/Spiel | 0.75 | 1.20 | 0.43 | 1.00
xG für/Spiel | 1.72 | 1.83 | 1.65 | 2.08
xG gegen/Spiel | 1.10 | 1.02 | 1.15 | 0.96
Spiele mit xG | 12 | 5 | 7 | 6
S/U/N | 8/3/1 | 3/1/1 | 5/2/0 | 4/2/0
Punkte/Spiel | 2.25 | 2.00 | 2.43 | 2.33
BTTS % | 42 % | 60 % | 29 % | 50 %
Over 2,5 % | 58 % | 80 % | 43 % | 83 %
Under 2,5 % | 42 % | 20 % | 57 % | 17 %
Clean Sheets % | 58 % | 40 % | 71 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 8 % | 20 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Muğlaspor (Gast, ID 11090)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 18 | 11 | 7 | 13
Gegentore | 14 | 7 | 7 | 10
Tore/Spiel | 1.50 | 1.83 | 1.17 | 2.17
Gegentore/Spiel | 1.17 | 1.17 | 1.17 | 1.67
xG für/Spiel | 1.39 | 1.45 | 1.33 | 1.65
xG gegen/Spiel | 1.37 | 1.30 | 1.43 | 1.41
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 4/6/2 | 2/3/1 | 2/3/1 | 2/3/1
Punkte/Spiel | 1.50 | 1.50 | 1.50 | 1.50
BTTS % | 42 % | 33 % | 50 % | 67 %
Over 2,5 % | 42 % | 67 % | 17 % | 67 %
Under 2,5 % | 58 % | 33 % | 83 % | 33 %
Clean Sheets % | 42 % | 50 % | 33 % | 17 %
Failed to Score % | 33 % | 33 % | 33 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Kayserispor: 14.09. H İstanbulspor (0.38 PPG) 4:0 · 20.09. A Mardin BB (1.85 PPG) 1:0 · 10.10. H Manisa BBSK (1.00 PPG) 3:2 · 14.10. A Antalyaspor (1.46 PPG) 4:0 · 18.10. H Batman Petrolspor (1.77 PPG) 2:2 · 25.10. A Pendikspor (1.08 PPG) 2:2

Letzte 6 Muğlaspor: 13.09. A Sivasspor (1.00 PPG) 1:1 · 18.09. H 76 Iğdır Belediyespor (2.08 PPG) 2:2 · 11.10. A Fatih Karagümrük (1.23 PPG) 1:1 · 15.10. H Bursaspor (2.38 PPG) 0:3 · 19.10. A Manisa BBSK (1.00 PPG) 4:3 · 24.10. H İstanbulspor (0.38 PPG) 5:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Kayserispor [2, 2, 1, 1, 1, 3, 4, 1, 3, 4, 2, 2]; Muğlaspor [0, 0, 0, 2, 1, 2, 1, 2, 1, 0, 4, 5]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Muğlaspor mit 1,50 Toren/Spiel, auswärts 7 in 6, gegen Kayserispor mit 58 % Clean Sheets; der Weg zu drei Toren läuft vor allem über Kayserispor (2,17 Tore/Spiel, nie torlos) und wird nicht gewählt; stärkstes Gegenargument ist Muğlaspors stabile Auswärtsbilanz von 2-3-1 mit nur einer Niederlage, die das Remisrisiko erhöht, gegen Kayserispors 8-3-1 und Modell-Heimsieg von 70 % aber nicht überwiegt.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 1 (zeitlich vorwärts gewählt); Training 1194 Spiele, Saisons [9914, 12928, 15199, 17290]; Schätzung λ Heim 2.218, λ Gast 0.794. Prüfstand (unberührter Test, 120 Spiele ab 2026-08-09): Heimsieg nicht besser als Grundrate (Brier 0.2518 gegen 0.2354); Auswärtssieg nicht besser als Grundrate (Brier 0.2379 gegen 0.2323); BTTS Ja nicht besser als Grundrate (Brier 0.2696 gegen 0.2572); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2604 gegen 0.2505). Grenzen: 14 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 70 % · Remis 18 % · Auswärtssieg 12 % · BTTS Ja 49 % · Over 2,5 58 % · Under 2,5 42 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.44 · X 4.3 · 2 5.5 · BTTS Ja 1.85 · Over 2,5 1.66 · Under 2,5 2.15.

**Auswahl:** Heimsieg

⚠️ Muğlaspor verlor nur 1 von 6 Auswärtsspielen (3 Remis) – Remisrisiko.

---
