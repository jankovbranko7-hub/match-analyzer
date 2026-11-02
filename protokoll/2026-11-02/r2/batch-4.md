# Vorabeintrag Batch 4 · 02.11.2026 · Revision r2

**Revision r2** (vor allen Anstößen erstellt, ersetzt r1 in `../batch-4.md`; r1 bleibt unverändert erhalten). Für die Auswertung zählt r2 für alle 40 Spiele. Gründe: (1) K.-o.-/Play-off-Runden (alle Spiele mit Spieltag 0) aus Training und Tabellen ausgeschlossen, weil Verlängerung und neutraler Ort für sie nicht ausgeschlossen werden können (Abschnitt 5.2); das API-Feld no_home_away ist saisonweise uneinheitlich gesetzt und wird nicht als Kennzeichnung neutraler Plätze verwendet; (2) der in r1 eigenmächtig eingeführte Grundraten-Maßstab („Markt unbrauchbar“) ist auf Nutzeranweisung gestrichen, der Testbefund steht nur noch im Modellfeld; (3) xG-Werte 0,00 werden als beobachtete 0 übernommen; (4) Datenbasis „eingeschränkt“ nur bei konkreten Datenlücken, Umfang wird immer genannt; (5) Rohdaten-Snapshot liegt als `../rohdaten.tar.xz` bei.

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-02 10:09 UTC
- Eintrag erstellt: 2026-11-02 10:42:04 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen der jeweiligen Ligasaison berechnet (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 4.1 Reims – Sochaux | 2026-11-02 19:45 UTC | Frankreich Ligue 2 2026/2027, Spieltag 11 | Match-ID 8551239

Analyse-ID: A-20261102-8551239-r2 · Team-IDs: 451 / 454 · Saison-ID: 17117 · Status beim Abruf: incomplete · Ort: Stade Auguste-Delaune II

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 10 bzw. 10 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-08 bis 2026-10-26, Gast 2026-08-08 bis 2026-10-23; letzte 6: Heim 2026-09-05–2026-10-26, Gast 2026-09-04–2026-10-23.

**Reims (Heim, ID 451)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 20 | 13 | 7 | 10
Gegentore | 12 | 9 | 3 | 7
Tore/Spiel | 2.00 | 2.60 | 1.40 | 1.67
Gegentore/Spiel | 1.20 | 1.80 | 0.60 | 1.17
xG für/Spiel | 1.36 | 1.61 | 1.10 | 1.26
xG gegen/Spiel | 1.47 | 1.46 | 1.48 | 1.64
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 4/6/0 | 2/3/0 | 2/3/0 | 2/4/0
Punkte/Spiel | 1.80 | 1.80 | 1.80 | 1.67
BTTS % | 80 % | 100 % | 60 % | 83 %
Over 2,5 % | 60 % | 80 % | 40 % | 50 %
Under 2,5 % | 40 % | 20 % | 60 % | 50 %
Clean Sheets % | 20 % | 0 % | 40 % | 17 %
Failed to Score % | 20 % | 0 % | 40 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Sochaux (Gast, ID 454)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 8 | 4 | 4 | 7
Gegentore | 12 | 7 | 5 | 9
Tore/Spiel | 0.80 | 0.80 | 0.80 | 1.17
Gegentore/Spiel | 1.20 | 1.40 | 1.00 | 1.50
xG für/Spiel | 1.14 | 1.25 | 1.02 | 1.29
xG gegen/Spiel | 1.60 | 1.49 | 1.72 | 1.61
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 2/5/3 | 2/1/2 | 0/4/1 | 1/3/2
Punkte/Spiel | 1.10 | 1.40 | 0.80 | 1.00
BTTS % | 50 % | 40 % | 60 % | 83 %
Over 2,5 % | 30 % | 40 % | 20 % | 33 %
Under 2,5 % | 70 % | 60 % | 80 % | 67 %
Clean Sheets % | 40 % | 40 % | 40 % | 17 %
Failed to Score % | 30 % | 20 % | 40 % | 0 %
BTTS-and-lose % | 20 % | 20 % | 20 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Reims: 05.09. H Guingamp (1.27 PPG) 2:2 · 11.09. A Nancy (1.90 PPG) 2:1 · 18.09. H Montpellier (2.18 PPG) 1:1 · 10.10. A Nantes (0.82 PPG) 0:0 · 16.10. H Dijon (1.36 PPG) 4:2 · 26.10. A Boulogne (0.91 PPG) 1:1

Letzte 6 Sochaux: 04.09. A Pau (1.82 PPG) 1:1 · 12.09. H Nantes (0.82 PPG) 1:0 · 18.09. A Laval (0.82 PPG) 1:1 · 09.10. H Boulogne (0.91 PPG) 1:1 · 17.10. A Metz (1.27 PPG) 2:3 · 23.10. H Annecy (1.45 PPG) 1:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Reims [0, 3, 3, 4, 2, 2, 1, 0, 4, 1]; Sochaux [0, 0, 1, 0, 1, 1, 1, 1, 2, 1]

**Bild:** Saison 2026/27 mit je 10 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Sochaux mit 0,80 Toren/Spiel und 1,14 xG, das aber in allen letzten sechs Spielen traf (gleichmäßig je 1–2 Tore, keine Häufung) gegen eine Reims-Heimabwehr, die in allen 5 Heimspielen kassierte, während Reims daheim 13 Tore in 5 Spielen ohne torloses Spiel erzielte; der Weg zu drei Toren ist über Reims' 80 % Over daheim möglich, aber Sochaux-Spiele gingen nur zu 30 % Over; stärkstes Gegenargument ist Sochaux' geringe Torquote mit 40 % torlosen Auswärtsspielen, die als Gefahr für den Gästetreffer gewichtet wird, BTTS aber nicht entkräftet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1089 Spiele, Saisons [9621, 12338, 14954, 17117]; Schätzung λ Heim 1.657, λ Gast 0.888. Prüfstand (unberührter Test, 109 Spiele ab 2026-05-02): Heimsieg besser als Grundrate (Brier 0.2313 gegen 0.2379); Auswärtssieg besser als Grundrate (Brier 0.2185 gegen 0.222); BTTS Ja besser als Grundrate (Brier 0.2465 gegen 0.2513); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2441 gegen 0.2505). Grenzen: 4 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 56 % · Remis 24 % · Auswärtssieg 20 % · BTTS Ja 48 % · Over 2,5 47 % · Under 2,5 53 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.7 · X 3.55 · 2 4.4 · BTTS Ja 1.65 · Over 2,5 1.67 · Under 2,5 2.07.

**Auswahl:** BTTS Ja

⚠️ Sochaux: nur 0,80 Tore pro Spiel und auswärts in 2 von 5 Spielen torlos – Gefahr für den benötigten Gästetreffer.

---

## 4.2 Red Star – Nancy | 2026-11-02 19:45 UTC | Frankreich Ligue 2 2026/2027, Spieltag 11 | Match-ID 8551442

Analyse-ID: A-20261102-8551442-r2 · Team-IDs: 485 / 447 · Saison-ID: 17117 · Status beim Abruf: incomplete · Ort: Stade de Paris

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 10 bzw. 10 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-08 bis 2026-10-26, Gast 2026-08-08 bis 2026-10-23; letzte 6: Heim 2026-09-04–2026-10-26, Gast 2026-09-07–2026-10-23.

**Red Star (Heim, ID 485)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 4 | 6 | 6
Tore | 13 | 2 | 11 | 10
Gegentore | 12 | 5 | 7 | 7
Tore/Spiel | 1.30 | 0.50 | 1.83 | 1.67
Gegentore/Spiel | 1.20 | 1.25 | 1.17 | 1.17
xG für/Spiel | 1.62 | 1.65 | 1.60 | 1.71
xG gegen/Spiel | 1.20 | 1.01 | 1.33 | 1.11
Spiele mit xG | 10 | 4 | 6 | 6
S/U/N | 5/2/3 | 1/1/2 | 4/1/1 | 4/0/2
Punkte/Spiel | 1.70 | 1.00 | 2.17 | 2.00
BTTS % | 60 % | 25 % | 83 % | 67 %
Over 2,5 % | 50 % | 25 % | 67 % | 67 %
Under 2,5 % | 50 % | 75 % | 33 % | 33 %
Clean Sheets % | 30 % | 50 % | 17 % | 17 %
Failed to Score % | 20 % | 50 % | 0 % | 17 %
BTTS-and-lose % | 20 % | 25 % | 17 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Nancy (Gast, ID 447)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 12 | 5 | 7 | 9
Gegentore | 8 | 3 | 5 | 7
Tore/Spiel | 1.20 | 1.00 | 1.40 | 1.50
Gegentore/Spiel | 0.80 | 0.60 | 1.00 | 1.17
xG für/Spiel | 1.58 | 1.74 | 1.41 | 1.64
xG gegen/Spiel | 1.03 | 1.01 | 1.06 | 1.05
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 6/1/3 | 3/0/2 | 3/1/1 | 4/0/2
Punkte/Spiel | 1.90 | 1.80 | 2.00 | 2.00
BTTS % | 30 % | 20 % | 40 % | 50 %
Over 2,5 % | 30 % | 20 % | 40 % | 50 %
Under 2,5 % | 70 % | 80 % | 60 % | 50 %
Clean Sheets % | 50 % | 60 % | 40 % | 33 %
Failed to Score % | 30 % | 20 % | 40 % | 17 %
BTTS-and-lose % | 10 % | 20 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Red Star: 04.09. A Laval (0.82 PPG) 2:1 · 14.09. H Metz (1.27 PPG) 1:0 · 19.09. A Guingamp (1.27 PPG) 3:1 · 10.10. A Clermont (0.73 PPG) 3:2 · 17.10. H Saint-Étienne (2.27 PPG) 0:1 · 26.10. A Montpellier (2.18 PPG) 1:2

Letzte 6 Nancy: 07.09. A Nantes (0.82 PPG) 0:1 · 11.09. H Reims (1.80 PPG) 1:2 · 18.09. A Rodez (1.18 PPG) 4:3 · 09.10. H Guingamp (1.27 PPG) 1:0 · 16.10. A Annecy (1.45 PPG) 2:1 · 23.10. H Laval (0.82 PPG) 1:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Red Star [1, 0, 1, 1, 2, 1, 3, 3, 0, 1]; Nancy [0, 0, 1, 2, 0, 1, 4, 1, 2, 1]

**Bild:** Saison 2026/27 mit je 10 Spielen ist verwendbar; schwächere Offensive ist Red Star daheim mit 2 Toren in 4 Spielen trotz 1,65 xG, gegen Nancys Abwehr mit 50 % Clean Sheets; ein Weg zu drei Toren ist mit 50 % Over in Red-Star-Spielen gegen 30 % in Nancy-Spielen unsicher; stärkstes Gegenargument gegen jede Siegauswahl ist das ausgeglichene Modell (Heim 45 %, Auswärts 28 %) gegen Nancys bessere Tabellenbilanz (1,90 Punkte/Spiel), sodass kein Markt tragfähig ist.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1089 Spiele, Saisons [9621, 12338, 14954, 17117]; Schätzung λ Heim 1.411, λ Gast 1.043. Prüfstand (unberührter Test, 109 Spiele ab 2026-05-02): Heimsieg besser als Grundrate (Brier 0.2313 gegen 0.2379); Auswärtssieg besser als Grundrate (Brier 0.2185 gegen 0.222); BTTS Ja besser als Grundrate (Brier 0.2465 gegen 0.2513); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2441 gegen 0.2505). Grenzen: 4 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 45 % · Remis 27 % · Auswärtssieg 28 % · BTTS Ja 49 % · Over 2,5 44 % · Under 2,5 56 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.29 · X 3.3 · 2 2.85 · BTTS Ja 1.68 · Over 2,5 1.99 · Under 2,5 1.8.

**Auswahl:** keine – Grund siehe Bild.

---

## 4.3 Atromitos – Volos NFC | 2026-11-02 16:00 UTC | Griechenland Super League 2026/2027, Spieltag 9 | Match-ID 8603737

Analyse-ID: A-20261102-8603737-r2 · Team-IDs: 1109 / 5199 · Saison-ID: 17356 · Status beim Abruf: incomplete · Ort: Stadio Peristeriou

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 7 bzw. 8 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-22 bis 2026-10-25, Gast 2026-08-23 bis 2026-10-25; letzte 6: Heim 2026-08-30–2026-10-25, Gast 2026-09-05–2026-10-25.

**Atromitos (Heim, ID 1109)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 7 | 3 | 4 | 6
Tore | 6 | 3 | 3 | 6
Gegentore | 12 | 5 | 7 | 11
Tore/Spiel | 0.86 | 1.00 | 0.75 | 1.00
Gegentore/Spiel | 1.71 | 1.67 | 1.75 | 1.83
xG für/Spiel | 1.01 | 1.45 | 0.69 | 1.05
xG gegen/Spiel | 1.39 | 1.22 | 1.52 | 1.12
Spiele mit xG | 7 | 3 | 4 | 6
S/U/N | 0/2/5 | 0/1/2 | 0/1/3 | 0/2/4
Punkte/Spiel | 0.29 | 0.33 | 0.25 | 0.33
BTTS % | 86 % | 100 % | 75 % | 100 %
Over 2,5 % | 57 % | 67 % | 50 % | 67 %
Under 2,5 % | 43 % | 33 % | 50 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 14 % | 0 % | 25 % | 0 %
BTTS-and-lose % | 57 % | 67 % | 50 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Volos NFC (Gast, ID 5199)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 6 | 3 | 3 | 5
Gegentore | 13 | 5 | 8 | 10
Tore/Spiel | 0.75 | 0.75 | 0.75 | 0.83
Gegentore/Spiel | 1.62 | 1.25 | 2.00 | 1.67
xG für/Spiel | 0.99 | 0.98 | 1.01 | 0.87
xG gegen/Spiel | 1.68 | 1.65 | 1.71 | 1.92
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 0/3/5 | 0/2/2 | 0/1/3 | 0/2/4
Punkte/Spiel | 0.38 | 0.50 | 0.25 | 0.33
BTTS % | 62 % | 75 % | 50 % | 67 %
Over 2,5 % | 38 % | 25 % | 50 % | 50 %
Under 2,5 % | 62 % | 75 % | 50 % | 50 %
Clean Sheets % | 12 % | 0 % | 25 % | 17 %
Failed to Score % | 38 % | 25 % | 50 % | 33 %
BTTS-and-lose % | 38 % | 25 % | 50 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Atromitos: 30.08. H PAOK (2.00 PPG) 1:2 · 06.09. H Kalamata (1.25 PPG) 1:1 · 12.09. A Iraklis Thessaloniki (1.12 PPG) 1:1 · 19.09. H Kifisia (1.22 PPG) 1:2 · 10.10. A Asteras Tripolis (0.67 PPG) 1:2 · 25.10. A Aris (1.78 PPG) 1:3

Letzte 6 Volos NFC: 05.09. H Olympiakos Piraeus (2.44 PPG) 1:1 · 13.09. A Kalamata (1.25 PPG) 1:3 · 20.09. H AEK Athens (2.12 PPG) 1:2 · 11.10. A Aris (1.78 PPG) 2:3 · 17.10. A Levadiakos (0.67 PPG) 0:0 · 25.10. H Panathinaikos (2.67 PPG) 0:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Atromitos [0, 1, 1, 1, 1, 1, 1]; Volos NFC [0, 1, 1, 1, 1, 2, 0, 0]

**Bild:** Saison 2026/27 mit 7 und 8 Spielen und voller xG-Abdeckung (die API liefert für Iraklis–Atromitos 1:1 xG 0,00/0,00, als beobachtete 0 übernommen) ist verwendbar; schwächere Offensive ist Volos mit 0,75 Toren/Spiel und 0,99 xG, gegen Atromitos ohne Clean Sheet; ein Weg zu drei Toren ist mit 57 % bzw. 38 % Over beider Teams unklar; stärkstes Gegenargument gegen den Modell-Heimsieg (52 %) ist Atromitos' Saisonbilanz von 0-2-5 ohne Sieg, und dieser ungeklärte Widerspruch zum Modell verhindert eine Auswahl.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 1 (zeitlich vorwärts gewählt); Training 772 Spiele, Saisons [9889, 12734, 15163, 17356]; Schätzung λ Heim 1.557, λ Gast 0.924. Prüfstand (unberührter Test, 78 Spiele ab 2026-05-10): Heimsieg besser als Grundrate (Brier 0.1917 gegen 0.2563); Auswärtssieg besser als Grundrate (Brier 0.1737 gegen 0.2045); BTTS Ja nicht besser als Grundrate (Brier 0.2566 gegen 0.2502); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2464 gegen 0.2489). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 52 % · Remis 25 % · Auswärtssieg 22 % · BTTS Ja 48 % · Over 2,5 45 % · Under 2,5 55 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.95 · X 3.45 · 2 3.7 · BTTS Ja 1.85 · Over 2,5 1.95 · Under 2,5 1.85.

**Auswahl:** keine – Grund siehe Bild.

---

## 4.4 Kalamata – Iraklis Thessaloniki | 2026-11-02 17:30 UTC | Griechenland Super League 2026/2027, Spieltag 9 | Match-ID 8604050

Analyse-ID: A-20261102-8604050-r2 · Team-IDs: 5191 / 1112 · Saison-ID: 17356 · Status beim Abruf: incomplete · Ort: Dimotiko Stadio Paralias

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 8 bzw. 8 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-22 bis 2026-10-25, Gast 2026-08-22 bis 2026-10-24; letzte 6: Heim 2026-09-06–2026-10-25, Gast 2026-09-07–2026-10-24.

**Kalamata (Heim, ID 5191)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 13 | 9 | 4 | 11
Gegentore | 17 | 8 | 9 | 12
Tore/Spiel | 1.62 | 2.25 | 1.00 | 1.83
Gegentore/Spiel | 2.12 | 2.00 | 2.25 | 2.00
xG für/Spiel | 1.22 | 1.38 | 1.06 | 1.32
xG gegen/Spiel | 1.66 | 1.56 | 1.76 | 1.61
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 3/1/4 | 2/0/2 | 1/1/2 | 3/1/2
Punkte/Spiel | 1.25 | 1.50 | 1.00 | 1.67
BTTS % | 62 % | 75 % | 50 % | 67 %
Over 2,5 % | 62 % | 75 % | 50 % | 67 %
Under 2,5 % | 38 % | 25 % | 50 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 38 % | 25 % | 50 % | 33 %
BTTS-and-lose % | 12 % | 25 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Iraklis Thessaloniki (Gast, ID 1112)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 3 | 5 | 6
Tore | 9 | 5 | 4 | 8
Gegentore | 11 | 4 | 7 | 6
Tore/Spiel | 1.12 | 1.67 | 0.80 | 1.33
Gegentore/Spiel | 1.38 | 1.33 | 1.40 | 1.00
xG für/Spiel | 0.77 | 0.64 | 0.84 | 0.73
xG gegen/Spiel | 1.66 | 1.06 | 2.03 | 1.46
Spiele mit xG | 8 | 3 | 5 | 6
S/U/N | 2/3/3 | 1/1/1 | 1/2/2 | 2/2/2
Punkte/Spiel | 1.12 | 1.33 | 1.00 | 1.33
BTTS % | 50 % | 67 % | 40 % | 50 %
Over 2,5 % | 38 % | 33 % | 40 % | 33 %
Under 2,5 % | 62 % | 67 % | 60 % | 67 %
Clean Sheets % | 38 % | 33 % | 40 % | 50 %
Failed to Score % | 25 % | 0 % | 40 % | 17 %
BTTS-and-lose % | 25 % | 33 % | 20 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Kalamata: 06.09. A Atromitos (0.29 PPG) 1:1 · 13.09. H Volos NFC (0.38 PPG) 3:1 · 20.09. H Panathinaikos (2.67 PPG) 0:1 · 12.10. A PAOK (2.00 PPG) 3:1 · 18.10. H OFI (1.78 PPG) 4:3 · 25.10. A Olympiakos Piraeus (2.44 PPG) 0:5

Letzte 6 Iraklis Thessaloniki: 07.09. A Asteras Tripolis (0.67 PPG) 2:0 · 12.09. H Atromitos (0.29 PPG) 1:1 · 19.09. A Aris (1.78 PPG) 0:0 · 11.10. H Levadiakos (0.67 PPG) 2:0 · 18.10. A PAOK (2.00 PPG) 1:2 · 24.10. H Kifisia (1.22 PPG) 2:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Kalamata [2, 0, 1, 3, 0, 3, 4, 0]; Iraklis Thessaloniki [0, 1, 2, 1, 0, 2, 1, 2]

**Bild:** Saison 2026/27 mit je 8 Spielen und voller xG-Abdeckung (die API liefert für Iraklis–Atromitos 1:1 xG 0,00/0,00, als beobachtete 0 übernommen) ist verwendbar; schwächere Offensive ist Iraklis mit 0,77 xG/Spiel, gegen eine Kalamata-Abwehr ohne Clean Sheet in 8 Spielen; der Weg zu drei Toren läuft über Kalamatas Heimspiele (9:8 Tore in 4, 75 % Over) und Iraklis' hohe xG gegen (1,66, auswärts 2,03), notfalls auch einseitig über Kalamata, und das Modell schätzt 64 % Over; stärkstes Gegenargument sind nur 38 % Over in Iraklis-Spielen und Kalamatas auf wenige Spiele konzentrierte Tore (3, 3, 4 bei drei torlosen Spielen), was als wesentliche Gefahr gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 1 (zeitlich vorwärts gewählt); Training 772 Spiele, Saisons [9889, 12734, 15163, 17356]; Schätzung λ Heim 1.818, λ Gast 1.488. Prüfstand (unberührter Test, 78 Spiele ab 2026-05-10): Heimsieg besser als Grundrate (Brier 0.1917 gegen 0.2563); Auswärtssieg besser als Grundrate (Brier 0.1737 gegen 0.2045); BTTS Ja nicht besser als Grundrate (Brier 0.2566 gegen 0.2502); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2464 gegen 0.2489). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 46 % · Remis 23 % · Auswärtssieg 32 % · BTTS Ja 65 % · Over 2,5 64 % · Under 2,5 36 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.15 · X 3.1 · 2 3.39 · BTTS Ja 1.83 · Over 2,5 2.15 · Under 2,5 1.69.

**Auswahl:** Over 2,5

⚠️ Iraklis-Spiele nur 38 % Over und Iraklis-Offensive mit 0,88 xG; Kalamatas Tore sind auf wenige Spiele konzentriert.

---

## 4.5 Sassuolo – Fiorentina | 2026-11-02 17:30 UTC | Italien Serie A 2026/2027, Spieltag 10 | Match-ID 8545052

Analyse-ID: A-20261102-8545052-r2 · Team-IDs: 469 / 471 · Saison-ID: 17084 · Status beim Abruf: incomplete · Ort: MAPEI Stadium - Città del Tricolore

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 9 bzw. 9 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-23 bis 2026-10-27, Gast 2026-08-24 bis 2026-10-29; letzte 6: Heim 2026-09-13–2026-10-27, Gast 2026-09-11–2026-10-29.

**Sassuolo (Heim, ID 469)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 14 | 8 | 6 | 9
Gegentore | 22 | 10 | 12 | 17
Tore/Spiel | 1.56 | 2.00 | 1.20 | 1.50
Gegentore/Spiel | 2.44 | 2.50 | 2.40 | 2.83
xG für/Spiel | 1.54 | 1.34 | 1.70 | 1.30
xG gegen/Spiel | 1.80 | 1.68 | 1.90 | 1.88
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 2/2/5 | 2/1/1 | 0/1/4 | 1/1/4
Punkte/Spiel | 0.89 | 1.75 | 0.20 | 0.67
BTTS % | 89 % | 100 % | 80 % | 83 %
Over 2,5 % | 78 % | 75 % | 80 % | 67 %
Under 2,5 % | 22 % | 25 % | 20 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 11 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 44 % | 25 % | 60 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Fiorentina (Gast, ID 471)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 11 | 5 | 6 | 10
Gegentore | 21 | 11 | 10 | 12
Tore/Spiel | 1.22 | 1.00 | 1.50 | 1.67
Gegentore/Spiel | 2.33 | 2.20 | 2.50 | 2.00
xG für/Spiel | 1.76 | 2.03 | 1.42 | 1.80
xG gegen/Spiel | 1.69 | 1.44 | 2.00 | 1.75
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 1/2/6 | 0/2/3 | 1/0/3 | 1/2/3
Punkte/Spiel | 0.56 | 0.40 | 0.75 | 0.83
BTTS % | 78 % | 80 % | 75 % | 100 %
Over 2,5 % | 89 % | 80 % | 100 % | 83 %
Under 2,5 % | 11 % | 20 % | 0 % | 17 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 22 % | 20 % | 25 % | 0 %
BTTS-and-lose % | 44 % | 40 % | 50 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Sassuolo: 13.09. H Juventus (1.70 PPG) 3:2 · 18.09. A Monza (0.70 PPG) 1:2 · 11.10. H AC Milan (2.10 PPG) 1:1 · 16.10. A Frosinone (2.00 PPG) 2:4 · 24.10. A Como (2.30 PPG) 0:2 · 27.10. H Lazio (2.80 PPG) 2:6

Letzte 6 Fiorentina: 11.09. A Venezia (0.30 PPG) 4:2 · 20.09. H Napoli (1.40 PPG) 1:1 · 10.10. A Genoa (1.30 PPG) 1:2 · 18.10. H Como (2.30 PPG) 1:3 · 25.10. A Inter Milan (2.50 PPG) 1:2 · 29.10. H Atalanta (1.22 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Sassuolo [1, 2, 2, 3, 1, 1, 2, 0, 2]; Fiorentina [0, 0, 1, 4, 1, 1, 1, 1, 2]

**Bild:** Saison 2026/27 mit je 9 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Fiorentina mit 11 Toren in 9 Spielen, die aber in den letzten sieben Spielen jeweils traf (1,80 xG in den letzten sechs) gegen eine Sassuolo-Abwehr ohne Clean Sheet, während Sassuolo in 8 von 9 Spielen und in allen Heimspielen traf (Tore gleichmäßig verteilt) gegen eine Fiorentina-Abwehr ohne Clean Sheet; der Weg zu drei Toren ist mit 78 % bzw. 89 % Over beider Teams ebenfalls stark; stärkstes Gegenargument ist das 4:2 in Fiorentinas Torzahl, das Ausgangspunkt einer Torhäufung ist, aber angesichts der Trefferserie keine wesentliche Gefahr begründet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1238 Spiele, Saisons [9697, 12530, 15068, 17084]; Schätzung λ Heim 1.294, λ Gast 1.672. Prüfstand (unberührter Test, 124 Spiele ab 2026-05-10): Heimsieg besser als Grundrate (Brier 0.2082 gegen 0.2484); Auswärtssieg besser als Grundrate (Brier 0.2055 gegen 0.2426); BTTS Ja besser als Grundrate (Brier 0.2433 gegen 0.2504); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2529 gegen 0.2543). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 30 % · Remis 24 % · Auswärtssieg 46 % · BTTS Ja 59 % · Over 2,5 57 % · Under 2,5 43 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.75 · X 3.78 · 2 2.37 · BTTS Ja 1.4 · Over 2,5 1.57 · Under 2,5 2.51.

**Auswahl:** BTTS Ja

---
