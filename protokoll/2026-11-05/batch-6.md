# Vorabeintrag Batch 6 · 05.11.2026

- System: FootyStats-System v1.4 (Fassung v1.4-2026-11-05)
- Modell: Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-05 09:51 UTC
- Eintrag erstellt: 2026-11-05 09:56:12 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei Europapokal-Wettbewerben: nur Liga- bzw. Gruppenphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 6.1 Panathinaikos – CSKA Sofia | 2026-11-05 20:00 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701014

Analyse-ID: A-20261105-8701014-r1 · Team-IDs: 960 / 3604 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: Olympiako Stadio Spyros Louis · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Panathinaikos (Heim, ID 960)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 7 | 2 | 5 | 7
Gegentore | 2 | 1 | 1 | 2
Tore/Spiel | 3.50 | 2.00 | 5.00 | 3.50
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 2.27 | 3.19 | 1.35 | 2.27
xG gegen/Spiel | 0.83 | 0.53 | 1.14 | 0.83
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 2/0/0 | 1/0/0 | 1/0/0 | 2/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**CSKA Sofia (Gast, ID 3604)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 3 | 1 | 2 | 3
Gegentore | 4 | 2 | 2 | 4
Tore/Spiel | 1.50 | 1.00 | 2.00 | 1.50
Gegentore/Spiel | 2.00 | 2.00 | 2.00 | 2.00
xG für/Spiel | 1.93 | 2.00 | 1.86 | 1.93
xG gegen/Spiel | 1.36 | 1.12 | 1.60 | 1.36
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/1/1 | 0/0/1 | 0/1/0 | 0/1/1
Punkte/Spiel | 0.50 | 0.00 | 1.00 | 0.50
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 50 % | 100 % | 0 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Panathinaikos – Landesliga (Saison-ID 17356, 2026-08-31 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 20 | 16 | 4 | 12
Gegentore | 4 | 3 | 1 | 2
Tore/Spiel | 2.22 | 3.20 | 1.00 | 2.00
Gegentore/Spiel | 0.44 | 0.60 | 0.25 | 0.33
xG für/Spiel | 2.14 | 2.45 | 1.76 | 2.09
xG gegen/Spiel | 0.86 | 0.80 | 0.93 | 0.89
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 8/0/1 | 5/0/0 | 3/0/1 | 5/0/1
Punkte/Spiel | 2.67 | 3.00 | 2.25 | 2.50
BTTS % | 33 % | 60 % | 0 % | 17 %
Over 2,5 % | 44 % | 80 % | 0 % | 33 %
Under 2,5 % | 56 % | 20 % | 100 % | 67 %
Clean Sheets % | 56 % | 40 % | 75 % | 67 %
Failed to Score % | 11 % | 0 % | 25 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**CSKA Sofia – Landesliga (Saison-ID 17088, 2026-07-20 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 29 | 19 | 10 | 12
Gegentore | 9 | 5 | 4 | 4
Tore/Spiel | 2.23 | 2.71 | 1.67 | 2.00
Gegentore/Spiel | 0.69 | 0.71 | 0.67 | 0.67
xG für/Spiel | 2.34 | 2.44 | 2.22 | 2.48
xG gegen/Spiel | 1.24 | 1.26 | 1.22 | 1.39
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 9/4/0 | 6/1/0 | 3/3/0 | 4/2/0
Punkte/Spiel | 2.38 | 2.71 | 2.00 | 2.33
BTTS % | 54 % | 57 % | 50 % | 50 %
Over 2,5 % | 54 % | 71 % | 33 % | 33 %
Under 2,5 % | 46 % | 29 % | 67 % | 67 %
Clean Sheets % | 46 % | 43 % | 50 % | 50 %
Failed to Score % | 15 % | 14 % | 17 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Panathinaikos: 15.10. H Borac Banja Luka (1.50 PPG) 2:1 · 22.10. A Kairat (0.50 PPG) 5:1

Letzte 6 CSKA Sofia: 15.10. H Monaco (3.00 PPG) 1:2 · 22.10. A Nordsjælland (1.00 PPG) 2:2

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Panathinaikos [2, 5]; CSKA Sofia [1, 2]

**Bild:** Conference League 2026/27 mit je 2 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist CSKA Sofia mit 3 Toren in 2 Conference-League-Spielen, gegen Panathinaikos, das in der Liga daheim 5-0-0 bei 16:3 Toren steht und in der Conference League beide Spiele gewann (7:2); der Weg zu drei Toren hängt vor allem an Panathinaikos und wird nicht gewählt; stärkstes Gegenargument ist CSKAs ungeschlagene Ligabilanz (9-4-0, auswärts 3-3-0), die als wesentliche Gefahr für den Heimsieg (Modell 61 %) gewichtet wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 2.052, λ Gast 1.009; xG-Variante λ Heim 1.635, λ Gast 1.138 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 61 % · Remis 21 % · Auswärtssieg 18 % · BTTS Ja 55 % · Over 2,5 52 % · Under 2,5 48 % (nur Tormodell: BTTS 55 %, Over 2,5 59 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.44 · X 4.6 · 2 6 · BTTS Ja 1.87 · Over 2,5 1.72 · Under 2,5 2.1.

**Markt:** margenbereinigt 64 % für Heimsieg; Modell 61 %; Abweichung Modell − Markt -3 Prozentpunkte.

**Auswahl:** Heimsieg

⚠️ CSKA Sofia ist in der Liga ungeschlagen (auswärts 3-3-0) – Remisrisiko.

---

## 6.2 Getafe CF – Brighton & Hove Albion | 2026-11-05 20:00 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701029

Analyse-ID: A-20261105-8701029-r1 · Team-IDs: 293 / 209 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: Coliseum Alfonso Pérez · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Getafe CF (Heim, ID 293)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 3 | 2 | 1 | 3
Gegentore | 6 | 5 | 1 | 6
Tore/Spiel | 1.50 | 2.00 | 1.00 | 1.50
Gegentore/Spiel | 3.00 | 5.00 | 1.00 | 3.00
xG für/Spiel | 2.03 | 2.66 | 1.40 | 2.03
xG gegen/Spiel | 1.24 | 1.26 | 1.22 | 1.24
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/1/1 | 0/0/1 | 0/1/0 | 0/1/1
Punkte/Spiel | 0.50 | 0.00 | 1.00 | 0.50
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 50 % | 100 % | 0 % | 50 %
Under 2,5 % | 50 % | 0 % | 100 % | 50 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 50 % | 100 % | 0 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Brighton & Hove Albion (Gast, ID 209)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 4 | 4 | 0 | 4
Gegentore | 0 | 0 | 0 | 0
Tore/Spiel | 2.00 | 4.00 | 0.00 | 2.00
Gegentore/Spiel | 0.00 | 0.00 | 0.00 | 0.00
xG für/Spiel | 3.20 | 3.77 | 2.63 | 3.20
xG gegen/Spiel | 0.68 | 0.38 | 0.98 | 0.68
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 1/1/0 | 1/0/0 | 0/1/0 | 1/1/0
Punkte/Spiel | 2.00 | 3.00 | 1.00 | 2.00
BTTS % | 0 % | 0 % | 0 % | 0 %
Over 2,5 % | 50 % | 100 % | 0 % | 50 %
Under 2,5 % | 50 % | 0 % | 100 % | 50 %
Clean Sheets % | 100 % | 100 % | 100 % | 100 %
Failed to Score % | 50 % | 0 % | 100 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Getafe CF – Landesliga (Saison-ID 17199, 2026-08-15 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 6 | 5 | 6
Tore | 8 | 8 | 0 | 5
Gegentore | 16 | 4 | 12 | 10
Tore/Spiel | 0.73 | 1.33 | 0.00 | 0.83
Gegentore/Spiel | 1.45 | 0.67 | 2.40 | 1.67
xG für/Spiel | 1.14 | 1.39 | 0.84 | 1.17
xG gegen/Spiel | 1.60 | 1.39 | 1.85 | 1.83
Spiele mit xG | 11 | 6 | 5 | 6
S/U/N | 3/3/5 | 3/3/0 | 0/0/5 | 2/1/3
Punkte/Spiel | 1.09 | 2.00 | 0.00 | 1.17
BTTS % | 36 % | 67 % | 0 % | 33 %
Over 2,5 % | 36 % | 17 % | 60 % | 50 %
Under 2,5 % | 64 % | 83 % | 40 % | 50 %
Clean Sheets % | 18 % | 33 % | 0 % | 17 %
Failed to Score % | 45 % | 0 % | 100 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Brighton & Hove Albion – Landesliga (Saison-ID 17146, 2026-08-23 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 24 | 13 | 11 | 16
Gegentore | 7 | 1 | 6 | 2
Tore/Spiel | 2.67 | 3.25 | 2.20 | 2.67
Gegentore/Spiel | 0.78 | 0.25 | 1.20 | 0.33
xG für/Spiel | 1.77 | 2.03 | 1.56 | 1.61
xG gegen/Spiel | 1.31 | 0.85 | 1.68 | 1.40
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 6/1/2 | 3/1/0 | 3/0/2 | 5/0/1
Punkte/Spiel | 2.11 | 2.50 | 1.80 | 2.50
BTTS % | 22 % | 25 % | 20 % | 0 %
Over 2,5 % | 56 % | 75 % | 40 % | 50 %
Under 2,5 % | 44 % | 25 % | 60 % | 50 %
Clean Sheets % | 67 % | 75 % | 60 % | 83 %
Failed to Score % | 11 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 11 % | 0 % | 20 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Getafe CF: 15.10. A CS U Craiova (2.00 PPG) 1:1 · 22.10. H Lugano (3.00 PPG) 2:5

Letzte 6 Brighton & Hove Albion: 15.10. H Kauno Žalgiris (0.00 PPG) 4:0 · 22.10. A Jablonec (0.50 PPG) 0:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Getafe CF [1, 2]; Brighton & Hove Albion [4, 0]

**Bild:** Conference League 2026/27 mit je 2 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Getafe mit 8 Toren in 11 La-Liga-Spielen, gegen Brighton mit 83 % Clean Sheets in den letzten sechs Premier-League-Spielen; der Weg zu drei Toren ist widersprüchlich, weil Getafes Liga-Heimspiele nur zu 17 % Over endeten, die xG-Variante aber 54 % Over schätzt; stärkstes Gegenargument gegen den Auswärtssieg ist das Modell mit nur 32 %, sodass weder Sieg- noch Torlinienmarkt widerspruchsfrei getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 1.499, λ Gast 1.257; xG-Variante λ Heim 1.524, λ Gast 1.327 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 43 % · Remis 25 % · Auswärtssieg 32 % · BTTS Ja 57 % · Over 2,5 54 % · Under 2,5 46 % (nur Tormodell: BTTS 56 %, Over 2,5 52 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 6 · X 3.9 · 2 1.6 · BTTS Ja 1.91 · Over 2,5 1.93 · Under 2,5 1.87.

**Markt:** Heim 16 % · Remis 24 % · Auswärts 60 % · BTTS 50 % · Over 49 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 6.3 Twente – Paphos | 2026-11-05 20:00 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701033

Analyse-ID: A-20261105-8701033-r1 · Team-IDs: 375 / 3743 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: De Grolsch Veste · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: eingeschränkt (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen; Landesliga-Daten fehlen für Paphos (Liga nicht im API-Abo)).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Twente (Heim, ID 375)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 5 | 1 | 4 | 5
Gegentore | 1 | 0 | 1 | 1
Tore/Spiel | 2.50 | 1.00 | 4.00 | 2.50
Gegentore/Spiel | 0.50 | 0.00 | 1.00 | 0.50
xG für/Spiel | 2.65 | 2.39 | 2.90 | 2.65
xG gegen/Spiel | 0.54 | 0.50 | 0.58 | 0.54
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 2/0/0 | 1/0/0 | 1/0/0 | 2/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 50 % | 0 % | 100 % | 50 %
Over 2,5 % | 50 % | 0 % | 100 % | 50 %
Under 2,5 % | 50 % | 100 % | 0 % | 50 %
Clean Sheets % | 50 % | 100 % | 0 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Paphos (Gast, ID 3743)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 2 | 1 | 1 | 2
Gegentore | 4 | 1 | 3 | 4
Tore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
Gegentore/Spiel | 2.00 | 1.00 | 3.00 | 2.00
xG für/Spiel | 1.39 | 1.71 | 1.07 | 1.39
xG gegen/Spiel | 1.90 | 1.53 | 2.28 | 1.90
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/1/1 | 0/1/0 | 0/0/1 | 0/1/1
Punkte/Spiel | 0.50 | 1.00 | 0.00 | 0.50
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 50 % | 0 % | 100 % | 50 %
Under 2,5 % | 50 % | 100 % | 0 % | 50 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 50 % | 0 % | 100 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Twente – Landesliga (Saison-ID 17097, 2026-08-09 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 28 | 10 | 18 | 18
Gegentore | 10 | 5 | 5 | 5
Tore/Spiel | 2.55 | 2.00 | 3.00 | 3.00
Gegentore/Spiel | 0.91 | 1.00 | 0.83 | 0.83
xG für/Spiel | 2.33 | 2.59 | 2.11 | 2.31
xG gegen/Spiel | 1.15 | 1.15 | 1.15 | 1.22
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 7/2/2 | 4/0/1 | 3/2/1 | 4/1/1
Punkte/Spiel | 2.09 | 2.40 | 1.83 | 2.17
BTTS % | 55 % | 60 % | 50 % | 50 %
Over 2,5 % | 55 % | 60 % | 50 % | 50 %
Under 2,5 % | 45 % | 40 % | 50 % | 50 %
Clean Sheets % | 36 % | 40 % | 33 % | 50 %
Failed to Score % | 9 % | 0 % | 17 % | 0 %
BTTS-and-lose % | 9 % | 20 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Paphos – Landesliga:** fehlt (Liga nicht im API-Abo)

Letzte 6 Twente: 15.10. H Thun (0.00 PPG) 1:0 · 22.10. A Lincoln Red Imps (0.00 PPG) 4:1

Letzte 6 Paphos: 15.10. A Atalanta (1.50 PPG) 1:3 · 22.10. H Riga (1.00 PPG) 1:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Twente [1, 4]; Paphos [1, 1]

**Bild:** Die Datenbasis ist eingeschränkt, weil die Landesliga von Pafos im API-Abo fehlt; schwächere Offensive ist Pafos mit 2 Toren in 2 Conference-League-Spielen und 1,90 xG gegen, gegen Twente, das in der Eredivisie daheim 4-0-1 bei 2,59 xG steht und beide Conference-League-Spiele gewann (5:1); der Weg zu drei Toren hängt vor allem an Twente und wird nicht gewählt; stärkstes Gegenargument sind Pafos' Treffer in beiden Conference-League-Spielen bei fehlender Ligabasis, die gegen Twentes Heimbilanz aber keine wesentliche Gefahr für den Heimsieg (Modell 55 %) begründen.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 1.801, λ Gast 1.040; xG-Variante λ Heim 1.583, λ Gast 1.149 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 55 % · Remis 23 % · Auswärtssieg 22 % · BTTS Ja 54 % · Over 2,5 51 % · Under 2,5 49 % (nur Tormodell: BTTS 54 %, Over 2,5 54 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.23 · X 5.25 · 2 8 · BTTS Ja 1.73 · Over 2,5 1.43 · Under 2,5 2.7.

**Markt:** margenbereinigt 72 % für Heimsieg; Modell 55 %; Abweichung Modell − Markt -17 Prozentpunkte.

**Auswahl:** Heimsieg

---

## 6.4 Sint-Truiden – Brann | 2026-11-05 20:00 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701040

Analyse-ID: A-20261105-8701040-r1 · Team-IDs: 532 / 336 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: Stayen Stadion · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Sint-Truiden (Heim, ID 532)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 3 | 2 | 1 | 3
Gegentore | 0 | 0 | 0 | 0
Tore/Spiel | 1.50 | 2.00 | 1.00 | 1.50
Gegentore/Spiel | 0.00 | 0.00 | 0.00 | 0.00
xG für/Spiel | 2.20 | 2.29 | 2.10 | 2.20
xG gegen/Spiel | 1.09 | 0.37 | 1.81 | 1.09
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 2/0/0 | 1/0/0 | 1/0/0 | 2/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 0 % | 0 % | 0 % | 0 %
Over 2,5 % | 0 % | 0 % | 0 % | 0 %
Under 2,5 % | 100 % | 100 % | 100 % | 100 %
Clean Sheets % | 100 % | 100 % | 100 % | 100 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Brann (Gast, ID 336)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 6 | 2 | 4 | 6
Gegentore | 2 | 1 | 1 | 2
Tore/Spiel | 3.00 | 2.00 | 4.00 | 3.00
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
xG für/Spiel | 2.51 | 2.72 | 2.30 | 2.51
xG gegen/Spiel | 0.94 | 0.74 | 1.15 | 0.94
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 2/0/0 | 1/0/0 | 1/0/0 | 2/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Sint-Truiden – Landesliga (Saison-ID 17171, 2026-08-08 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 18 | 6 | 12 | 10
Gegentore | 21 | 8 | 13 | 13
Tore/Spiel | 1.80 | 1.20 | 2.40 | 1.67
Gegentore/Spiel | 2.10 | 1.60 | 2.60 | 2.17
xG für/Spiel | 1.79 | 2.07 | 1.51 | 1.77
xG gegen/Spiel | 1.59 | 1.41 | 1.78 | 1.45
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 2/2/6 | 1/1/3 | 1/1/3 | 1/0/5
Punkte/Spiel | 0.80 | 0.80 | 0.80 | 0.50
BTTS % | 60 % | 40 % | 80 % | 50 %
Over 2,5 % | 70 % | 60 % | 80 % | 67 %
Under 2,5 % | 30 % | 40 % | 20 % | 33 %
Clean Sheets % | 10 % | 20 % | 0 % | 17 %
Failed to Score % | 30 % | 40 % | 20 % | 33 %
BTTS-and-lose % | 30 % | 20 % | 40 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Brann – Landesliga (Saison-ID 16558, 2026-03-15 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 25 | 13 | 12 | 6
Tore | 45 | 23 | 22 | 8
Gegentore | 42 | 20 | 22 | 13
Tore/Spiel | 1.80 | 1.77 | 1.83 | 1.33
Gegentore/Spiel | 1.68 | 1.54 | 1.83 | 2.17
xG für/Spiel | 1.80 | 2.04 | 1.54 | 1.93
xG gegen/Spiel | 1.61 | 1.41 | 1.82 | 1.92
Spiele mit xG | 25 | 13 | 12 | 6
S/U/N | 10/2/13 | 7/0/6 | 3/2/7 | 2/0/4
Punkte/Spiel | 1.28 | 1.62 | 0.92 | 1.00
BTTS % | 76 % | 77 % | 75 % | 67 %
Over 2,5 % | 80 % | 85 % | 75 % | 67 %
Under 2,5 % | 20 % | 15 % | 25 % | 33 %
Clean Sheets % | 12 % | 8 % | 17 % | 0 %
Failed to Score % | 16 % | 15 % | 17 % | 33 %
BTTS-and-lose % | 40 % | 31 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Sint-Truiden: 15.10. H Saburtalo (0.50 PPG) 2:0 · 22.10. A Midtjylland (0.50 PPG) 1:0

Letzte 6 Brann: 15.10. H Lincoln Red Imps (0.00 PPG) 2:1 · 22.10. A Kauno Žalgiris (0.00 PPG) 4:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Sint-Truiden [2, 1]; Brann [2, 4]

**Bild:** Conference League 2026/27 mit je 2 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Sint-Truiden mit 3 Toren in 2 Conference-League-Spielen, aber nur 6 Toren in 5 Liga-Heimspielen, gegen Brann mit 17 % Clean Sheets; ein Weg zu drei Toren ist mit 70 % bzw. 80 % Over beider Ligen sichtbar, widerspricht aber Sint-Truidens Conference-League-Spielen ohne Over; stärkstes Gegenargument gegen den Heimsieg (Modell 52 %) ist Sint-Truidens Ligaform mit 1-0-5 in den letzten sechs, sodass kein Markt widerspruchsfrei getragen wird.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 1.656, λ Gast 1.043; xG-Variante λ Heim 1.585, λ Gast 1.214 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 52 % · Remis 24 % · Auswärtssieg 24 % · BTTS Ja 56 % · Over 2,5 53 % · Under 2,5 47 % (nur Tormodell: BTTS 52 %, Over 2,5 51 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.73 · X 4.1 · 2 4.4 · BTTS Ja 1.53 · Over 2,5 1.54 · Under 2,5 2.45.

**Markt:** Heim 55 % · Remis 23 % · Auswärts 22 % · BTTS 62 % · Over 61 % (margenbereinigt, informativ).

**Auswahl:** keine – Grund siehe Bild.

---

## 6.5 Lugano – Kauno Žalgiris | 2026-11-05 20:00 UTC | UEFA Conference League 2026/2027, Spieltag 3 | Match-ID 8701055

Analyse-ID: A-20261105-8701055-r1 · Team-IDs: 894 / 1231 · Saison-ID: 17130 · Status beim Abruf: incomplete · Ort: fehlt · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-05 09:51 UTC; Datenbasis: verwendbar (Saison 2026/2027: 2 bzw. 2 Ligaspiele; xG für alle Spiele; 258 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-10-15 bis 2026-10-22, Gast 2026-10-15 bis 2026-10-22; letzte 6: Heim 2026-10-15–2026-10-22, Gast 2026-10-15–2026-10-22.

**Lugano (Heim, ID 894)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 8 | 3 | 5 | 8
Gegentore | 4 | 2 | 2 | 4
Tore/Spiel | 4.00 | 3.00 | 5.00 | 4.00
Gegentore/Spiel | 2.00 | 2.00 | 2.00 | 2.00
xG für/Spiel | 1.50 | 1.74 | 1.26 | 1.50
xG gegen/Spiel | 2.27 | 1.88 | 2.66 | 2.27
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 2/0/0 | 1/0/0 | 1/0/0 | 2/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Kauno Žalgiris (Gast, ID 1231)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 2 | 1 | 1 | 2
Tore | 1 | 1 | 0 | 1
Gegentore | 8 | 4 | 4 | 8
Tore/Spiel | 0.50 | 1.00 | 0.00 | 0.50
Gegentore/Spiel | 4.00 | 4.00 | 4.00 | 4.00
xG für/Spiel | 0.76 | 1.15 | 0.38 | 0.76
xG gegen/Spiel | 3.04 | 2.30 | 3.77 | 3.04
Spiele mit xG | 2 | 1 | 1 | 2
S/U/N | 0/0/2 | 0/0/1 | 0/0/1 | 0/0/2
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 50 % | 100 % | 0 % | 50 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 50 % | 0 % | 100 % | 50 %
BTTS-and-lose % | 50 % | 100 % | 0 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt vom Europapokal, andere Skala):**

**Lugano – Landesliga (Saison-ID 17129, 2026-07-26 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 7 | 5 | 6
Tore | 36 | 20 | 16 | 19
Gegentore | 10 | 5 | 5 | 6
Tore/Spiel | 3.00 | 2.86 | 3.20 | 3.17
Gegentore/Spiel | 0.83 | 0.71 | 1.00 | 1.00
xG für/Spiel | 1.83 | 1.87 | 1.76 | 1.79
xG gegen/Spiel | 1.46 | 1.49 | 1.43 | 1.72
Spiele mit xG | 12 | 7 | 5 | 6
S/U/N | 11/1/0 | 6/1/0 | 5/0/0 | 5/1/0
Punkte/Spiel | 2.83 | 2.71 | 3.00 | 2.67
BTTS % | 67 % | 57 % | 80 % | 67 %
Over 2,5 % | 92 % | 86 % | 100 % | 100 %
Under 2,5 % | 8 % | 14 % | 0 % | 0 %
Clean Sheets % | 33 % | 43 % | 20 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Kauno Žalgiris – Landesliga (Saison-ID 16799, 2026-02-23 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 33 | 17 | 16 | 6
Tore | 67 | 38 | 29 | 10
Gegentore | 22 | 9 | 13 | 4
Tore/Spiel | 2.03 | 2.24 | 1.81 | 1.67
Gegentore/Spiel | 0.67 | 0.53 | 0.81 | 0.67
xG für/Spiel | 1.76 | 1.67 | 1.86 | 2.32
xG gegen/Spiel | 1.13 | 1.10 | 1.17 | 1.33
Spiele mit xG | 33 | 17 | 16 | 6
S/U/N | 18/10/5 | 9/5/3 | 9/5/2 | 4/1/1
Punkte/Spiel | 1.94 | 1.88 | 2.00 | 2.17
BTTS % | 42 % | 29 % | 56 % | 33 %
Over 2,5 % | 55 % | 53 % | 56 % | 33 %
Under 2,5 % | 45 % | 47 % | 44 % | 67 %
Clean Sheets % | 52 % | 59 % | 44 % | 67 %
Failed to Score % | 18 % | 24 % | 12 % | 17 %
BTTS-and-lose % | 9 % | 6 % | 12 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Lugano: 15.10. H Red Star Belgrade (0.50 PPG) 3:2 · 22.10. A Getafe CF (0.50 PPG) 5:2

Letzte 6 Kauno Žalgiris: 15.10. A Brighton & Hove Albion (2.00 PPG) 0:4 · 22.10. H Brann (3.00 PPG) 1:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Lugano [3, 5]; Kauno Žalgiris [0, 1]

**Bild:** Conference League 2026/27 mit je 2 Spielen und Landesliga-Daten ist verwendbar, die Europapokal-Daten (2–3 Spiele je Team, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Žalgiris mit 1 Tor in 2 Conference-League-Spielen und 0,76 xG, gegen Lugano, das in der Liga 11-1-0 bei 36:10 Toren steht und beide Conference-League-Spiele gewann (8:4); der Weg zu drei Toren ist mit Luganos 92 % Over in der Liga plausibel, hängt aber vor allem an Lugano, weshalb der Heimsieg (Modell 66 %) besser belegt ist; stärkstes Gegenargument ist Luganos Abwehr mit 4 Gegentoren in 2 Conference-League-Spielen, die gegen Žalgiris' schwache Offensive keine wesentliche Gefahr begründet.

**Modell:** Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 348 Spiele, Saisons [9600, 12278, 14904, 17130]; Schätzung Tormodell λ Heim 2.379, λ Gast 1.107; xG-Variante λ Heim 1.710, λ Gast 1.156 (xG-Anteil im Training 100 %). Prüfstand (unberührter Test, 35 Spiele ab 2026-10-15): Heimsieg besser als Grundrate (Brier 0.2492 gegen 0.2508); Auswärtssieg besser als Grundrate (Brier 0.174 gegen 0.1791); BTTS Ja besser als Grundrate (Brier 0.2441 gegen 0.2479 – xG-Variante); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2472 gegen 0.2518 – xG-Variante). Grenzen: 1181 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten v1.4 (Schätzung): Heimsieg 66 % · Remis 18 % · Auswärtssieg 16 % · BTTS Ja 56 % · Over 2,5 55 % · Under 2,5 45 % (nur Tormodell: BTTS 61 %, Over 2,5 68 %)

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-05 09:50 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.08 · X 7.6 · 2 12 · BTTS Ja 1.75 · Over 2,5 1.36 · Under 2,5 3.1.

**Markt:** margenbereinigt 81 % für Heimsieg; Modell 66 %; Abweichung Modell − Markt -16 Prozentpunkte.

**Auswahl:** Heimsieg

---
