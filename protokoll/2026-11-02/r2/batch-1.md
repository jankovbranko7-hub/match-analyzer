# Vorabeintrag Batch 1 · 02.11.2026 · Revision r2

**Revision r2** (vor allen Anstößen erstellt, ersetzt r1 in `../batch-1.md`; r1 bleibt unverändert erhalten). Für die Auswertung zählt r2 für alle 40 Spiele. Gründe: (1) K.-o.-/Play-off-Runden (alle Spiele mit Spieltag 0) aus Training und Tabellen ausgeschlossen, weil Verlängerung und neutraler Ort für sie nicht ausgeschlossen werden können (Abschnitt 5.2); das API-Feld no_home_away ist saisonweise uneinheitlich gesetzt und wird nicht als Kennzeichnung neutraler Plätze verwendet; (2) der in r1 eigenmächtig eingeführte Grundraten-Maßstab („Markt unbrauchbar“) ist auf Nutzeranweisung gestrichen, der Testbefund steht nur noch im Modellfeld; (3) xG-Werte 0,00 werden als beobachtete 0 übernommen; (4) Datenbasis „eingeschränkt“ nur bei konkreten Datenlücken, Umfang wird immer genannt; (5) Rohdaten-Snapshot liegt als `../rohdaten.tar.xz` bei.

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-02 10:09 UTC
- Eintrag erstellt: 2026-11-02 10:42:04 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen der jeweiligen Ligasaison berechnet (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 1.1 Defensa y Justicia – Independiente | 2026-11-02 22:00 UTC | Argentinien Primera División 2026, Spieltag 15 | Match-ID 8419182

Analyse-ID: A-20261102-8419182-r2 · Team-IDs: 701 / 702 · Saison-ID: 16571 · Status beim Abruf: incomplete · Ort: Estadio Norberto Tito Tomaghello · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026: 30 bzw. 30 Ligaspiele; xG für alle Spiele; 15 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-01-22 bis 2026-10-24, Gast 2026-01-23 bis 2026-10-25; letzte 6: Heim 2026-09-11–2026-10-24, Gast 2026-09-13–2026-10-25.

**Defensa y Justicia (Heim, ID 701)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 30 | 15 | 15 | 6
Tore | 38 | 18 | 20 | 11
Gegentore | 34 | 14 | 20 | 4
Tore/Spiel | 1.27 | 1.20 | 1.33 | 1.83
Gegentore/Spiel | 1.13 | 0.93 | 1.33 | 0.67
xG für/Spiel | 1.46 | 1.52 | 1.40 | 1.81
xG gegen/Spiel | 1.57 | 1.39 | 1.76 | 1.89
Spiele mit xG | 30 | 15 | 15 | 6
S/U/N | 12/10/8 | 6/6/3 | 6/4/5 | 4/1/1
Punkte/Spiel | 1.53 | 1.60 | 1.47 | 2.17
BTTS % | 53 % | 53 % | 53 % | 33 %
Over 2,5 % | 43 % | 33 % | 53 % | 50 %
Under 2,5 % | 57 % | 67 % | 47 % | 50 %
Clean Sheets % | 30 % | 33 % | 27 % | 50 %
Failed to Score % | 27 % | 20 % | 33 % | 17 %
BTTS-and-lose % | 10 % | 7 % | 13 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Independiente (Gast, ID 702)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 30 | 15 | 15 | 6
Tore | 37 | 18 | 19 | 6
Gegentore | 34 | 19 | 15 | 8
Tore/Spiel | 1.23 | 1.20 | 1.27 | 1.00
Gegentore/Spiel | 1.13 | 1.27 | 1.00 | 1.33
xG für/Spiel | 1.50 | 1.66 | 1.33 | 1.47
xG gegen/Spiel | 1.31 | 1.03 | 1.59 | 1.32
Spiele mit xG | 30 | 15 | 15 | 6
S/U/N | 12/9/9 | 5/5/5 | 7/4/4 | 2/2/2
Punkte/Spiel | 1.50 | 1.33 | 1.67 | 1.33
BTTS % | 53 % | 47 % | 60 % | 67 %
Over 2,5 % | 33 % | 33 % | 33 % | 33 %
Under 2,5 % | 67 % | 67 % | 67 % | 67 %
Clean Sheets % | 30 % | 33 % | 27 % | 17 %
Failed to Score % | 20 % | 27 % | 13 % | 17 %
BTTS-and-lose % | 13 % | 13 % | 13 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Defensa y Justicia: 11.09. H Gimnasia Mendoza (1.29 PPG) 2:0 · 18.09. A Central Córdoba SdE (0.87 PPG) 2:2 · 03.10. H San Lorenzo (1.32 PPG) 3:0 · 10.10. A Unión Santa Fe (1.26 PPG) 2:0 · 16.10. H Instituto (1.74 PPG) 0:1 · 24.10. A Talleres Córdoba (1.19 PPG) 2:1

Letzte 6 Independiente: 13.09. H San Lorenzo (1.32 PPG) 1:1 · 19.09. A Unión Santa Fe (1.26 PPG) 2:1 · 02.10. H Instituto (1.74 PPG) 1:4 · 12.10. A Talleres Córdoba (1.19 PPG) 1:0 · 18.10. A Racing Club (1.16 PPG) 1:1 · 25.10. H Boca Juniors (1.94 PPG) 0:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Defensa y Justicia [0, 1, 0, 3, 1, 1, 0, 1, 1, 5, 2, 0, 1, 1, 0, 1, 1, 2, 0, 2, 1, 2, 1, 0, 2, 2, 3, 2, 0, 2]; Independiente [1, 1, 1, 1, 2, 2, 1, 2, 4, 1, 1, 1, 1, 3, 0, 2, 2, 1, 0, 0, 3, 0, 0, 1, 1, 2, 1, 1, 1, 0]

**Bild:** Saison 2026 mit je 30 Ligaspielen (K.-o.-Spiele ausgeschlossen) und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Independiente mit 1,23 Toren/Spiel und Auswärts-xG 1,33, das gegen eine Defensa-Heimabwehr (14 Gegentore in 15) nur moderat trifft; der Weg zu drei Toren ist schwach, weil Defensa daheim nur 33 % Over hat, Independiente auswärts 33 % und das Modell nur 35 % Over schätzt; stärkstes Gegenargument sind Defensas letzte sechs Spiele mit 50 % Over und zusammen 3,7 xG pro Spiel, das als echte Gefahr gewichtet wird, die Auswahl aber nicht kippt.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1893 Spiele, Saisons [8595, 11212, 15746, 16571]; Schätzung λ Heim 1.164, λ Gast 0.918. Prüfstand (unberührter Test, 190 Spiele ab 2026-08-01): Heimsieg besser als Grundrate (Brier 0.2351 gegen 0.2406); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2221); BTTS Ja nicht besser als Grundrate (Brier 0.2667 gegen 0.2647); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2593 gegen 0.2631). Grenzen: 53 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 41 % · Remis 30 % · Auswärtssieg 29 % · BTTS Ja 41 % · Over 2,5 35 % · Under 2,5 65 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.25 · X 3.15 · 2 3.35 · BTTS Ja 1.83 · Over 2,5 2.1 · Under 2,5 1.68.

**Auswahl:** Under 2,5

⚠️ Defensa y Justicia: letzte sechs Spiele mit 1,81 xG für und 1,89 xG gegen (zusammen 3,7 pro Spiel) und 50 % Over 2,5 – der Saison-Under-Trend kann bei dieser Form brechen.

---

## 1.2 Platense – Central Córdoba SdE | 2026-11-02 22:00 UTC | Argentinien Primera División 2026, Spieltag 15 | Match-ID 8419323

Analyse-ID: A-20261102-8419323-r2 · Team-IDs: 749 / 738 · Saison-ID: 16571 · Status beim Abruf: incomplete · Ort: Estadio Ciudad de Vicente López · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026: 30 bzw. 30 Ligaspiele; xG für alle Spiele; 15 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-01-22 bis 2026-10-23, Gast 2026-01-23 bis 2026-10-26; letzte 6: Heim 2026-09-12–2026-10-23, Gast 2026-09-12–2026-10-26.

**Platense (Heim, ID 749)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 30 | 15 | 15 | 6
Tore | 24 | 9 | 15 | 6
Gegentore | 35 | 19 | 16 | 8
Tore/Spiel | 0.80 | 0.60 | 1.00 | 1.00
Gegentore/Spiel | 1.17 | 1.27 | 1.07 | 1.33
xG für/Spiel | 1.50 | 1.57 | 1.43 | 1.62
xG gegen/Spiel | 1.34 | 1.25 | 1.44 | 1.25
Spiele mit xG | 30 | 15 | 15 | 6
S/U/N | 6/12/12 | 2/6/7 | 4/6/5 | 1/2/3
Punkte/Spiel | 1.00 | 0.80 | 1.20 | 0.83
BTTS % | 47 % | 40 % | 53 % | 67 %
Over 2,5 % | 33 % | 20 % | 47 % | 50 %
Under 2,5 % | 67 % | 80 % | 53 % | 50 %
Clean Sheets % | 23 % | 13 % | 33 % | 0 %
Failed to Score % | 47 % | 53 % | 40 % | 33 %
BTTS-and-lose % | 10 % | 0 % | 20 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Central Córdoba SdE (Gast, ID 738)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 30 | 15 | 15 | 6
Tore | 22 | 15 | 7 | 7
Gegentore | 44 | 22 | 22 | 15
Tore/Spiel | 0.73 | 1.00 | 0.47 | 1.17
Gegentore/Spiel | 1.47 | 1.47 | 1.47 | 2.50
xG für/Spiel | 1.24 | 1.43 | 1.06 | 1.51
xG gegen/Spiel | 1.78 | 1.60 | 1.96 | 1.74
Spiele mit xG | 30 | 15 | 15 | 6
S/U/N | 6/8/16 | 5/3/7 | 1/5/9 | 0/3/3
Punkte/Spiel | 0.87 | 1.20 | 0.53 | 0.50
BTTS % | 37 % | 33 % | 40 % | 83 %
Over 2,5 % | 37 % | 40 % | 33 % | 83 %
Under 2,5 % | 63 % | 60 % | 67 % | 17 %
Clean Sheets % | 27 % | 33 % | 20 % | 0 %
Failed to Score % | 50 % | 40 % | 60 % | 17 %
BTTS-and-lose % | 17 % | 13 % | 20 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Platense: 12.09. A Estudiantes (1.48 PPG) 1:2 · 20.09. H Newell's Old Boys (1.19 PPG) 0:1 · 05.10. A Vélez Sarsfield (1.81 PPG) 2:2 · 11.10. H Argentinos Juniors (1.90 PPG) 1:1 · 17.10. H Lanús (1.58 PPG) 0:1 · 23.10. A Gimnasia Mendoza (1.29 PPG) 2:1

Letzte 6 Central Córdoba SdE: 12.09. A Boca Juniors (1.94 PPG) 1:3 · 18.09. H Defensa y Justicia (1.53 PPG) 2:2 · 05.10. A Deportivo Riestra (0.74 PPG) 1:1 · 10.10. H Estudiantes (1.48 PPG) 2:2 · 19.10. A Newell's Old Boys (1.19 PPG) 1:2 · 26.10. H Vélez Sarsfield (1.81 PPG) 0:5

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Platense [0, 2, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 3, 0, 0, 2, 1, 0, 1, 1, 2, 0, 1, 1, 0, 2, 1, 0, 2]; Central Córdoba SdE [0, 0, 0, 1, 0, 0, 2, 0, 1, 1, 0, 1, 0, 4, 0, 1, 0, 0, 1, 2, 0, 1, 0, 0, 1, 2, 1, 2, 1, 0]

**Bild:** Saison 2026 mit je 30 Ligaspielen (K.-o.-Spiele ausgeschlossen) ist verwendbar; schwächere Offensive ist Central Córdoba mit auswärts 7 Toren in 15 Spielen und 60 % Spielen ohne Tor, während auch Platense daheim nur 9 Tore in 15 erzielt (53 % ohne Tor); der Weg zu drei Toren ist schwach, weil Platense-Heimspiele zu 80 % Under endeten und das Modell nur 32 % Over schätzt; stärkstes Gegenargument ist Central Córdobas letzte-sechs-Bild mit 83 % Over und 15 Gegentoren, das aber stark vom 0:5 gegen Vélez geprägt ist und gegen die torarme Platense-Offensive geringer wiegt.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1893 Spiele, Saisons [8595, 11212, 15746, 16571]; Schätzung λ Heim 1.171, λ Gast 0.835. Prüfstand (unberührter Test, 190 Spiele ab 2026-08-01): Heimsieg besser als Grundrate (Brier 0.2351 gegen 0.2406); Auswärtssieg besser als Grundrate (Brier 0.2171 gegen 0.2221); BTTS Ja nicht besser als Grundrate (Brier 0.2667 gegen 0.2647); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2593 gegen 0.2631). Grenzen: 53 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 44 % · Remis 30 % · Auswärtssieg 26 % · BTTS Ja 39 % · Over 2,5 32 % · Under 2,5 68 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.55 · X 3.85 · 2 6.1 · BTTS Ja 2.16 · Over 2,5 2.06 · Under 2,5 1.73.

**Auswahl:** Under 2,5

⚠️ Central Córdoba: 5 der letzten 6 Spiele Over 2,5 (15 Gegentore) – Widerspruch zum Saisonbild.

---

## 1.3 Real Tomayapo – Blooming | 2026-11-02 21:15 UTC | Bolivien LFPB 2026, Spieltag 24 | Match-ID 8733190

Analyse-ID: A-20261102-8733190-r2 · Team-IDs: 668933 / 2262 · Saison-ID: 16927 · Status beim Abruf: incomplete · Ort: fehlt

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026: 23 bzw. 23 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-04-04 bis 2026-10-25, Gast 2026-04-03 bis 2026-10-24; letzte 6: Heim 2026-09-06–2026-10-25, Gast 2026-09-07–2026-10-24.

**Real Tomayapo (Heim, ID 668933)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 23 | 11 | 12 | 6
Tore | 16 | 9 | 7 | 3
Gegentore | 40 | 12 | 28 | 8
Tore/Spiel | 0.70 | 0.82 | 0.58 | 0.50
Gegentore/Spiel | 1.74 | 1.09 | 2.33 | 1.33
xG für/Spiel | 1.22 | 1.38 | 1.08 | 1.46
xG gegen/Spiel | 1.66 | 1.37 | 1.93 | 1.62
Spiele mit xG | 23 | 11 | 12 | 6
S/U/N | 5/5/13 | 3/4/4 | 2/1/9 | 1/1/4
Punkte/Spiel | 0.87 | 1.18 | 0.58 | 0.67
BTTS % | 43 % | 55 % | 33 % | 33 %
Over 2,5 % | 43 % | 27 % | 58 % | 33 %
Under 2,5 % | 57 % | 73 % | 42 % | 67 %
Clean Sheets % | 26 % | 27 % | 25 % | 33 %
Failed to Score % | 39 % | 27 % | 50 % | 50 %
BTTS-and-lose % | 26 % | 18 % | 33 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Blooming (Gast, ID 2262)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 23 | 12 | 11 | 6
Tore | 31 | 21 | 10 | 9
Gegentore | 25 | 6 | 19 | 7
Tore/Spiel | 1.35 | 1.75 | 0.91 | 1.50
Gegentore/Spiel | 1.09 | 0.50 | 1.73 | 1.17
xG für/Spiel | 1.58 | 1.78 | 1.36 | 1.91
xG gegen/Spiel | 1.52 | 1.20 | 1.86 | 1.44
Spiele mit xG | 23 | 12 | 11 | 6
S/U/N | 6/10/7 | 5/7/0 | 1/3/7 | 1/2/3
Punkte/Spiel | 1.22 | 1.83 | 0.55 | 0.83
BTTS % | 57 % | 50 % | 64 % | 67 %
Over 2,5 % | 39 % | 33 % | 45 % | 50 %
Under 2,5 % | 61 % | 67 % | 55 % | 50 %
Clean Sheets % | 30 % | 50 % | 9 % | 17 %
Failed to Score % | 26 % | 25 % | 27 % | 33 %
BTTS-and-lose % | 17 % | 0 % | 36 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Real Tomayapo: 06.09. A The Strongest (2.00 PPG) 1:3 · 14.09. H Bolívar (2.38 PPG) 1:2 · 17.09. H Oriente Petrolero (1.58 PPG) 0:2 · 09.10. A San Antonio Bulo Bulo (1.12 PPG) 0:0 · 17.10. H Gualberto Villarroel SJ (0.83 PPG) 1:0 · 25.10. A Aurora (1.46 PPG) 0:1

Letzte 6 Blooming: 07.09. A Nacional Potosí (1.33 PPG) 1:2 · 13.09. H ABB (0.83 PPG) 6:1 · 17.09. H Universitario de Vinto (0.88 PPG) 1:1 · 11.10. A Bolívar (2.38 PPG) 0:1 · 17.10. H Independiente Petrolero (1.25 PPG) 0:0 · 24.10. A Gualberto Villarroel SJ (0.83 PPG) 1:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Real Tomayapo [0, 1, 0, 0, 1, 1, 0, 2, 2, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0]; Blooming [5, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 3, 1, 1, 1, 6, 1, 0, 0, 1]

**Bild:** Saison 2026 mit je 23 Spielen ist verwendbar; schwächere Offensive ist Real Tomayapo mit 16 Toren in 23 und nur 3 Toren in den letzten sechs Spielen (50 % ohne Tor); ein Weg zu drei Toren besteht über Bloomings anfällige Auswärtsabwehr (19 Gegentore in 11), steht aber gegen 73 % Under in Tomayapos Heimspielen; stärkstes Gegenargument gegen den vom Modell bevorzugten Heimsieg (48 %) ist Tomayapos Form mit 1-1-4 und 0,67 Punkten pro Spiel, und weil weder Sieg noch Torlinie klar getragen werden, bleibt der Widerspruch ungeklärt.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1007 Spiele, Saisons [8926, 11072, 16307, 16927]; Schätzung λ Heim 1.480, λ Gast 0.995. Prüfstand (unberührter Test, 101 Spiele ab 2026-07-31): Heimsieg besser als Grundrate (Brier 0.2095 gegen 0.2518); Auswärtssieg besser als Grundrate (Brier 0.171 gegen 0.2074); BTTS Ja nicht besser als Grundrate (Brier 0.2481 gegen 0.2477); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2242 gegen 0.2446). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 48 % · Remis 26 % · Auswärtssieg 25 % · BTTS Ja 49 % · Over 2,5 45 % · Under 2,5 55 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.15 · X 3.4 · 2 2.8 · BTTS Ja 1.55 · Over 2,5 1.65 · Under 2,5 2.1.

**Auswahl:** keine – Grund siehe Bild.

---

## 1.4 Bragantino – Santos | 2026-11-02 23:00 UTC | Brasilien Série A 2026, Spieltag 34 | Match-ID 8409547

Analyse-ID: A-20261102-8409547-r2 · Team-IDs: 635 / 611 · Saison-ID: 16544 · Status beim Abruf: incomplete · Ort: Estádio Nabi Abi Chedid

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026: 33 bzw. 33 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-01-28 bis 2026-10-28, Gast 2026-01-28 bis 2026-10-28; letzte 6: Heim 2026-10-03–2026-10-28, Gast 2026-10-02–2026-10-28.

**Bragantino (Heim, ID 635)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 16 | 17 | 6
Tore | 42 | 27 | 15 | 9
Gegentore | 38 | 17 | 21 | 7
Tore/Spiel | 1.27 | 1.69 | 0.88 | 1.50
Gegentore/Spiel | 1.15 | 1.06 | 1.24 | 1.17
xG für/Spiel | 1.81 | 2.05 | 1.58 | 2.28
xG gegen/Spiel | 1.44 | 1.15 | 1.72 | 1.85
Spiele mit xG | 33 | 16 | 17 | 6
S/U/N | 12/8/13 | 8/3/5 | 4/5/8 | 2/2/2
Punkte/Spiel | 1.33 | 1.69 | 1.00 | 1.33
BTTS % | 52 % | 50 % | 53 % | 50 %
Over 2,5 % | 39 % | 50 % | 29 % | 33 %
Under 2,5 % | 61 % | 50 % | 71 % | 67 %
Clean Sheets % | 27 % | 38 % | 18 % | 17 %
Failed to Score % | 24 % | 19 % | 29 % | 33 %
BTTS-and-lose % | 18 % | 19 % | 18 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Santos (Gast, ID 611)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 17 | 16 | 6
Tore | 49 | 23 | 26 | 8
Gegentore | 47 | 21 | 26 | 7
Tore/Spiel | 1.48 | 1.35 | 1.62 | 1.33
Gegentore/Spiel | 1.42 | 1.24 | 1.62 | 1.17
xG für/Spiel | 1.49 | 1.61 | 1.36 | 1.66
xG gegen/Spiel | 1.46 | 1.26 | 1.68 | 1.62
Spiele mit xG | 33 | 17 | 16 | 6
S/U/N | 12/11/10 | 6/7/4 | 6/4/6 | 2/3/1
Punkte/Spiel | 1.42 | 1.47 | 1.38 | 1.50
BTTS % | 73 % | 65 % | 81 % | 83 %
Over 2,5 % | 64 % | 47 % | 81 % | 67 %
Under 2,5 % | 36 % | 53 % | 19 % | 33 %
Clean Sheets % | 21 % | 24 % | 19 % | 17 %
Failed to Score % | 12 % | 18 % | 6 % | 17 %
BTTS-and-lose % | 24 % | 12 % | 38 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Bragantino: 03.10. A Atlético Mineiro (1.52 PPG) 0:1 · 07.10. H Mirassol (1.12 PPG) 1:1 · 13.10. H Cruzeiro (1.73 PPG) 4:2 · 18.10. A Remo (0.88 PPG) 1:1 · 24.10. A Palmeiras (2.12 PPG) 0:2 · 28.10. H Chapecoense (0.66 PPG) 3:0

Letzte 6 Santos: 02.10. A São Paulo (1.30 PPG) 2:1 · 08.10. H Flamengo (2.21 PPG) 2:2 · 11.10. A Atlético Mineiro (1.52 PPG) 1:2 · 18.10. A Fluminense (1.64 PPG) 2:1 · 25.10. H Bahia (1.61 PPG) 1:1 · 28.10. H Palmeiras (2.12 PPG) 0:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Bragantino [1, 1, 0, 1, 1, 1, 0, 1, 3, 1, 1, 4, 0, 2, 0, 2, 3, 3, 1, 0, 0, 1, 1, 1, 2, 1, 1, 0, 1, 4, 1, 0, 3]; Santos [2, 1, 1, 2, 2, 1, 1, 0, 2, 1, 1, 2, 2, 1, 2, 0, 2, 3, 1, 2, 0, 3, 1, 1, 3, 2, 2, 2, 2, 1, 2, 1, 0]

**Bild:** Saison 2026 mit je 33 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Santos auswärts mit 1,36 xG, das aber in 15 von 16 Auswärtsspielen traf (Tore gleichmäßig je 1–3) gegen eine Bragantino-Heimabwehr mit nur 38 % Clean Sheets, während Bragantino daheim 27 Tore in 16 Spielen und 2,05 xG erzielte (in 81 % der Heimspiele, in den letzten drei Heimspielen 1, 4 und 3 Tore) gegen Santos' Auswärtsabwehr mit 26 Gegentoren in 16; der Weg zu drei Toren ist mit 81 % Over in Santos-Auswärtsspielen ebenfalls plausibel, BTTS ist aber durch beide eigenen Torargumente besser belegt als Over (Bragantino daheim 50 %) und als der Heimsieg mit seinem Remisrisiko; stärkstes Gegenargument sind Bragantinos zwei torlose Auswärtsspiele in den letzten sechs und Santos' 0:0 gegen Palmeiras, die aber nicht den Heimkontext betreffen und keine wesentliche Gefahr für einen der beiden Treffer begründen.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1469 Spiele, Saisons [9035, 11321, 14231, 16544]; Schätzung λ Heim 1.637, λ Gast 0.983. Prüfstand (unberührter Test, 147 Spiele ab 2026-07-21): Heimsieg besser als Grundrate (Brier 0.2312 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.178 gegen 0.1884); BTTS Ja nicht besser als Grundrate (Brier 0.2532 gegen 0.2487); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2536 gegen 0.2522). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 53 % · Remis 25 % · Auswärtssieg 23 % · BTTS Ja 50 % · Over 2,5 49 % · Under 2,5 51 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.05 · X 3.65 · 2 2.9 · BTTS Ja 1.53 · Over 2,5 1.53 · Under 2,5 2.45.

**Auswahl:** BTTS Ja

---

## 1.5 Fortaleza – Atlético GO | 2026-11-02 19:00 UTC | Brasilien Série B 2026, Spieltag 36 | Match-ID 8469497

Analyse-ID: A-20261102-8469497-r2 · Team-IDs: 2601 / 629 · Saison-ID: 16783 · Status beim Abruf: incomplete · Ort: Estádio Governador Plácido Aderaldo Castelo

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026: 35 bzw. 35 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-03-21 bis 2026-10-24, Gast 2026-03-21 bis 2026-10-24; letzte 6: Heim 2026-09-27–2026-10-24, Gast 2026-09-26–2026-10-24.

**Fortaleza (Heim, ID 2601)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 35 | 17 | 18 | 6
Tore | 43 | 27 | 16 | 10
Gegentore | 31 | 16 | 15 | 7
Tore/Spiel | 1.23 | 1.59 | 0.89 | 1.67
Gegentore/Spiel | 0.89 | 0.94 | 0.83 | 1.17
xG für/Spiel | 1.51 | 1.73 | 1.30 | 1.60
xG gegen/Spiel | 1.41 | 1.23 | 1.59 | 1.27
Spiele mit xG | 35 | 17 | 18 | 6
S/U/N | 16/13/6 | 9/7/1 | 7/6/5 | 2/4/0
Punkte/Spiel | 1.74 | 2.00 | 1.50 | 1.67
BTTS % | 46 % | 59 % | 33 % | 67 %
Over 2,5 % | 37 % | 47 % | 28 % | 50 %
Under 2,5 % | 63 % | 53 % | 72 % | 50 %
Clean Sheets % | 43 % | 35 % | 50 % | 33 %
Failed to Score % | 23 % | 12 % | 33 % | 0 %
BTTS-and-lose % | 6 % | 0 % | 11 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Atlético GO (Gast, ID 629)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 35 | 18 | 17 | 6
Tore | 42 | 27 | 15 | 6
Gegentore | 33 | 15 | 18 | 6
Tore/Spiel | 1.20 | 1.50 | 0.88 | 1.00
Gegentore/Spiel | 0.94 | 0.83 | 1.06 | 1.00
xG für/Spiel | 1.66 | 1.81 | 1.52 | 2.17
xG gegen/Spiel | 1.43 | 1.19 | 1.69 | 1.54
Spiele mit xG | 35 | 18 | 17 | 6
S/U/N | 14/12/9 | 9/5/4 | 5/7/5 | 2/2/2
Punkte/Spiel | 1.54 | 1.78 | 1.29 | 1.33
BTTS % | 49 % | 44 % | 53 % | 50 %
Over 2,5 % | 37 % | 44 % | 29 % | 17 %
Under 2,5 % | 63 % | 56 % | 71 % | 83 %
Clean Sheets % | 34 % | 39 % | 29 % | 33 %
Failed to Score % | 26 % | 28 % | 24 % | 17 %
BTTS-and-lose % | 9 % | 6 % | 12 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Fortaleza: 27.09. H Athletic Club (1.26 PPG) 2:2 · 03.10. H Náutico (1.28 PPG) 1:1 · 07.10. A América Mineiro (0.72 PPG) 1:0 · 12.10. H CRB (1.57 PPG) 2:2 · 16.10. A Sport Recife (1.53 PPG) 2:0 · 24.10. A Ponte Preta (0.42 PPG) 2:2

Letzte 6 Atlético GO: 26.09. A Goiás (1.49 PPG) 1:0 · 03.10. H América Mineiro (0.72 PPG) 2:0 · 07.10. A CRB (1.57 PPG) 1:3 · 11.10. H Sport Recife (1.53 PPG) 1:1 · 16.10. A Ponte Preta (0.42 PPG) 1:1 · 24.10. H Novorizontino (1.86 PPG) 0:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Fortaleza [0, 0, 2, 1, 3, 0, 4, 0, 1, 3, 0, 1, 0, 1, 2, 2, 0, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2]; Atlético GO [0, 1, 1, 2, 1, 2, 0, 1, 1, 0, 1, 2, 3, 1, 2, 0, 1, 0, 1, 3, 1, 0, 0, 3, 1, 2, 2, 4, 0, 1, 2, 1, 1, 1, 0]

**Bild:** Saison 2026 mit je 35 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Atlético GO auswärts mit 15 Toren in 17 und nur 29 % Over, gegen Fortalezas Heimabwehr mit 1,23 xG gegen; der Weg zu drei Toren läuft vor allem über Fortaleza (1,59 Heimtore/Spiel), bleibt aber unsicher, weil Atlético GO in den letzten sechs nur 17 % Over hatte und das Modell 38 % Over schätzt; stärkstes Gegenargument sind Fortalezas drei 2:2 in den letzten sechs Spielen und 59 % BTTS daheim, was als Warnung, nicht als Widerlegung gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1497 Spiele, Saisons [9042, 11351, 14305, 16783]; Schätzung λ Heim 1.293, λ Gast 0.916. Prüfstand (unberührter Test, 150 Spiele ab 2026-08-09): Heimsieg besser als Grundrate (Brier 0.2365 gegen 0.2489); Auswärtssieg besser als Grundrate (Brier 0.2065 gegen 0.2134); BTTS Ja besser als Grundrate (Brier 0.2452 gegen 0.2478); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2501 gegen 0.2526). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 45 % · Remis 28 % · Auswärtssieg 26 % · BTTS Ja 44 % · Over 2,5 38 % · Under 2,5 62 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.02 · X 3.3 · 2 3.75 · BTTS Ja 1.8 · Over 2,5 2.05 · Under 2,5 1.75.

**Auswahl:** Under 2,5

⚠️ Fortaleza: drei 2:2 in den letzten sechs Spielen und 59 % BTTS daheim – ein Treffer mehr reicht für Over.

---
