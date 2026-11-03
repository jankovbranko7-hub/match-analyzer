# Vorabeintrag Batch 5 · 03.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-03 14:33 UTC
- Eintrag erstellt: 2026-11-03 14:37:48 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 5.1 FK Bodo - Glimt – Lille | 2026-11-03 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 4 | Match-ID 8700812

Analyse-ID: A-20261103-8700812-r1 · Team-IDs: 332 / 441 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Aspmyra Stadion · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-10 bis 2026-10-20, Gast 2026-09-08 bis 2026-10-21; letzte 6: Heim 2026-09-10–2026-10-20, Gast 2026-09-08–2026-10-21.

**FK Bodo - Glimt (Heim, ID 332)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 4 | 1 | 3 | 4
Gegentore | 9 | 0 | 9 | 9
Tore/Spiel | 1.33 | 1.00 | 1.50 | 1.33
Gegentore/Spiel | 3.00 | 0.00 | 4.50 | 3.00
xG für/Spiel | 1.18 | 1.32 | 1.11 | 1.18
xG gegen/Spiel | 2.08 | 1.29 | 2.48 | 2.08
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 1/0/0 | 0/0/2 | 1/0/2
Punkte/Spiel | 1.00 | 3.00 | 0.00 | 1.00
BTTS % | 33 % | 0 % | 50 % | 33 %
Over 2,5 % | 67 % | 0 % | 100 % | 67 %
Under 2,5 % | 33 % | 100 % | 0 % | 33 %
Clean Sheets % | 33 % | 100 % | 0 % | 33 %
Failed to Score % | 33 % | 0 % | 50 % | 33 %
BTTS-and-lose % | 33 % | 0 % | 50 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Lille (Gast, ID 441)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 4 | 4 | 0 | 4
Gegentore | 10 | 7 | 3 | 10
Tore/Spiel | 1.33 | 2.00 | 0.00 | 1.33
Gegentore/Spiel | 3.33 | 3.50 | 3.00 | 3.33
xG für/Spiel | 0.92 | 1.23 | 0.30 | 0.92
xG gegen/Spiel | 1.80 | 1.56 | 2.28 | 1.80
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 0/0/3 | 0/0/2 | 0/0/1 | 0/0/3
Punkte/Spiel | 0.00 | 0.00 | 0.00 | 0.00
BTTS % | 67 % | 100 % | 0 % | 67 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 100 % | 33 %
BTTS-and-lose % | 67 % | 100 % | 0 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**FK Bodo - Glimt – Landesliga (Saison-ID 16558, 2026-04-06 bis 2026-10-30)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 25 | 13 | 12 | 6
Tore | 61 | 37 | 24 | 12
Gegentore | 23 | 10 | 13 | 8
Tore/Spiel | 2.44 | 2.85 | 2.00 | 2.00
Gegentore/Spiel | 0.92 | 0.77 | 1.08 | 1.33
xG für/Spiel | 2.29 | 2.63 | 1.91 | 2.51
xG gegen/Spiel | 1.01 | 0.89 | 1.14 | 1.16
Spiele mit xG | 25 | 13 | 12 | 6
S/U/N | 19/2/4 | 11/0/2 | 8/2/2 | 4/0/2
Punkte/Spiel | 2.36 | 2.54 | 2.17 | 2.00
BTTS % | 44 % | 38 % | 50 % | 67 %
Over 2,5 % | 72 % | 77 % | 67 % | 67 %
Under 2,5 % | 28 % | 23 % | 33 % | 33 %
Clean Sheets % | 44 % | 46 % | 42 % | 17 %
Failed to Score % | 12 % | 15 % | 8 % | 17 %
BTTS-and-lose % | 4 % | 0 % | 8 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Lille – Landesliga (Saison-ID 17102, 2026-08-23 bis 2026-10-30)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 12 | 7 | 5 | 7
Gegentore | 6 | 3 | 3 | 4
Tore/Spiel | 1.33 | 1.40 | 1.25 | 1.17
Gegentore/Spiel | 0.67 | 0.60 | 0.75 | 0.67
xG für/Spiel | 1.41 | 1.42 | 1.39 | 1.47
xG gegen/Spiel | 1.58 | 1.22 | 2.04 | 1.26
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 5/3/1 | 3/2/0 | 2/1/1 | 3/2/1
Punkte/Spiel | 2.00 | 2.20 | 1.75 | 1.83
BTTS % | 44 % | 40 % | 50 % | 50 %
Over 2,5 % | 22 % | 20 % | 25 % | 17 %
Under 2,5 % | 78 % | 80 % | 75 % | 83 %
Clean Sheets % | 56 % | 60 % | 50 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 11 % | 0 % | 25 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 FK Bodo - Glimt: 10.09. A Bayern München (1.67 PPG) 0:5 · 14.10. H Borussia Dortmund (2.00 PPG) 1:0 · 20.10. A Napoli (1.00 PPG) 3:4

Letzte 6 Lille: 08.09. H Real Betis (3.00 PPG) 2:3 · 13.10. A Arsenal (2.33 PPG) 0:3 · 21.10. H Galatasaray (1.00 PPG) 2:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): FK Bodo - Glimt [0, 1, 3]; Lille [2, 0, 2]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Lille mit 0,92 xG und 4 Toren in 3 Champions-League-Spielen (alle verloren), gegen Bodø/Glimt, das in der Eliteserien daheim 11-0-2 steht und in der Champions League Dortmund 1:0 schlug; der Weg zu drei Toren ist mit Lilles 22 % Over in der Ligue 1 unsicher und wird nicht gewählt; stärkstes Gegenargument ist Lilles Liga-Abwehr mit 56 % Clean Sheets, die ein enges Spiel und Remisrisiko nahelegt und als wesentliche Gefahr für den Heimsieg (Modell 44 %) gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 438 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.949, λ Gast 1.701. Prüfstand (unberührter Test, 44 Spiele ab 2026-09-09): Heimsieg besser als Grundrate (Brier 0.2056 gegen 0.2491); Auswärtssieg besser als Grundrate (Brier 0.1729 gegen 0.2022); BTTS Ja besser als Grundrate (Brier 0.2335 gegen 0.2359); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2114 gegen 0.2008). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 44 % · Remis 22 % · Auswärtssieg 34 % · BTTS Ja 70 % · Over 2,5 71 % · Under 2,5 29 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.84 · X 4.15 · 2 3.8 · BTTS Ja 1.44 · Over 2,5 1.5 · Under 2,5 2.62.

**Auswahl:** Heimsieg

⚠️ Lille hielt in der Ligue 1 in 56 % der Spiele die Null – enges Spiel und Remisrisiko.

---

## 5.2 Pogoń Siedlce – Ruch Chorzów | 2026-11-03 17:00 UTC | Polen 1. Liga 2026/2027, Spieltag 13 | Match-ID 8592513

Analyse-ID: A-20261103-8592513-r1 · Team-IDs: 776 / 1064 · Saison-ID: 17301 · Status beim Abruf: incomplete · Ort: Stadion ROSRRiT

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-07-25 bis 2026-10-25, Gast 2026-07-26 bis 2026-10-25; letzte 6: Heim 2026-09-12–2026-10-25, Gast 2026-09-07–2026-10-25.

**Pogoń Siedlce (Heim, ID 776)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 7 | 5 | 6
Tore | 14 | 11 | 3 | 7
Gegentore | 15 | 11 | 4 | 9
Tore/Spiel | 1.17 | 1.57 | 0.60 | 1.17
Gegentore/Spiel | 1.25 | 1.57 | 0.80 | 1.50
xG für/Spiel | 1.25 | 1.23 | 1.27 | 1.51
xG gegen/Spiel | 1.84 | 1.69 | 2.04 | 1.74
Spiele mit xG | 12 | 7 | 5 | 6
S/U/N | 4/3/5 | 3/1/3 | 1/2/2 | 2/1/3
Punkte/Spiel | 1.25 | 1.43 | 1.00 | 1.17
BTTS % | 50 % | 71 % | 20 % | 50 %
Over 2,5 % | 42 % | 57 % | 20 % | 50 %
Under 2,5 % | 58 % | 43 % | 80 % | 50 %
Clean Sheets % | 33 % | 29 % | 40 % | 33 %
Failed to Score % | 25 % | 0 % | 60 % | 33 %
BTTS-and-lose % | 25 % | 43 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Ruch Chorzów (Gast, ID 1064)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 16 | 12 | 4 | 13
Gegentore | 11 | 6 | 5 | 4
Tore/Spiel | 1.33 | 2.00 | 0.67 | 2.17
Gegentore/Spiel | 0.92 | 1.00 | 0.83 | 0.67
xG für/Spiel | 2.04 | 2.46 | 1.62 | 2.35
xG gegen/Spiel | 1.28 | 1.16 | 1.39 | 1.13
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 6/3/3 | 4/1/1 | 2/2/2 | 4/2/0
Punkte/Spiel | 1.75 | 2.17 | 1.33 | 2.33
BTTS % | 25 % | 33 % | 17 % | 33 %
Over 2,5 % | 25 % | 50 % | 0 % | 50 %
Under 2,5 % | 75 % | 50 % | 100 % | 50 %
Clean Sheets % | 50 % | 50 % | 50 % | 67 %
Failed to Score % | 33 % | 17 % | 50 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Pogoń Siedlce: 12.09. A Chrobry Głogów (1.08 PPG) 0:0 · 20.09. H Arka Gdynia (1.17 PPG) 2:1 · 09.10. A Podbeskidzie (1.15 PPG) 0:1 · 15.10. H Puszcza Niepołomice (1.00 PPG) 1:3 · 18.10. H Stal Rzeszów (1.38 PPG) 3:4 · 25.10. A Odra Opole (0.92 PPG) 1:0

Letzte 6 Ruch Chorzów: 07.09. H Unia Skierniewice (0.85 PPG) 3:1 · 12.09. H Podbeskidzie (1.15 PPG) 3:3 · 18.09. A Polonia Bytom (1.62 PPG) 0:0 · 11.10. A ŁKS Łódź (1.69 PPG) 2:0 · 16.10. H Odra Opole (0.92 PPG) 3:0 · 25.10. H Pogoń Grod. Mazowiecki (1.62 PPG) 2:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Pogoń Siedlce [1, 1, 2, 1, 0, 2, 0, 2, 0, 1, 3, 1]; Ruch Chorzów [0, 0, 1, 1, 1, 0, 3, 3, 0, 2, 3, 2]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Ruch Chorzów auswärts mit 4 Toren in 6 Spielen und 50 % torlosen Spielen trotz 1,62 xG, gegen Pogoń Siedlces Heimabwehr mit 11 Gegentoren in 7; der Weg zu drei Toren ist unsicher, weil keines der 6 Ruch-Auswärtsspiele Over endete und Ruch nur 25 % BTTS hat, das Modell schätzt 55 % Under; stärkstes Gegenargument sind Pogońs Heimspiele mit 22 Toren in 7 (57 % Over), die als wesentliche Gefahr gewichtet werden.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1033 Spiele, Saisons [9596, 12156, 14877, 17301]; Schätzung λ Heim 1.125, λ Gast 1.346. Prüfstand (unberührter Test, 104 Spiele ab 2026-08-01): Heimsieg nicht besser als Grundrate (Brier 0.2555 gegen 0.25); Auswärtssieg nicht besser als Grundrate (Brier 0.2062 gegen 0.2038); BTTS Ja besser als Grundrate (Brier 0.2425 gegen 0.248); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2429 gegen 0.2518). Grenzen: 9 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 31 % · Remis 27 % · Auswärtssieg 42 % · BTTS Ja 50 % · Over 2,5 45 % · Under 2,5 55 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.5 · X 3.4 · 2 1.75 · BTTS Ja 1.74 · Over 2,5 1.85 · Under 2,5 1.95.

**Auswahl:** Under 2,5

⚠️ Pogoń Siedlces Heimspiele brachten 3,1 Tore pro Spiel (57 % Over).

---

## 5.3 Chrobry Głogów – Arka Gdynia | 2026-11-03 17:00 UTC | Polen 1. Liga 2026/2027, Spieltag 13 | Match-ID 8592692

Analyse-ID: A-20261103-8592692-r1 · Team-IDs: 780 / 795 · Saison-ID: 17301 · Status beim Abruf: incomplete · Ort: Stadion GOS

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-07-25 bis 2026-10-24, Gast 2026-07-24 bis 2026-10-24; letzte 6: Heim 2026-09-05–2026-10-24, Gast 2026-09-06–2026-10-24.

**Chrobry Głogów (Heim, ID 780)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 13 | 3 | 10 | 3
Gegentore | 15 | 7 | 8 | 10
Tore/Spiel | 1.08 | 0.50 | 1.67 | 0.50
Gegentore/Spiel | 1.25 | 1.17 | 1.33 | 1.67
xG für/Spiel | 1.48 | 1.55 | 1.41 | 1.58
xG gegen/Spiel | 1.64 | 1.43 | 1.86 | 1.68
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 3/4/5 | 1/2/3 | 2/2/2 | 0/3/3
Punkte/Spiel | 1.08 | 0.83 | 1.33 | 0.50
BTTS % | 42 % | 17 % | 67 % | 33 %
Over 2,5 % | 33 % | 17 % | 50 % | 33 %
Under 2,5 % | 67 % | 83 % | 50 % | 67 %
Clean Sheets % | 25 % | 33 % | 17 % | 33 %
Failed to Score % | 50 % | 67 % | 33 % | 67 %
BTTS-and-lose % | 8 % | 0 % | 17 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Arka Gdynia (Gast, ID 795)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 16 | 13 | 3 | 7
Gegentore | 16 | 5 | 11 | 11
Tore/Spiel | 1.33 | 2.17 | 0.50 | 1.17
Gegentore/Spiel | 1.33 | 0.83 | 1.83 | 1.83
xG für/Spiel | 1.33 | 1.49 | 1.18 | 1.30
xG gegen/Spiel | 1.53 | 1.49 | 1.58 | 1.62
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 4/2/6 | 3/2/1 | 1/0/5 | 1/1/4
Punkte/Spiel | 1.17 | 1.83 | 0.50 | 0.67
BTTS % | 50 % | 67 % | 33 % | 83 %
Over 2,5 % | 58 % | 67 % | 50 % | 83 %
Under 2,5 % | 42 % | 33 % | 50 % | 17 %
Clean Sheets % | 25 % | 33 % | 17 % | 0 %
Failed to Score % | 25 % | 0 % | 50 % | 17 %
BTTS-and-lose % | 25 % | 17 % | 33 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Chrobry Głogów: 05.09. A Miedź Legnica (1.46 PPG) 1:1 · 12.09. H Pogoń Siedlce (1.25 PPG) 0:0 · 19.09. A Polonia Warszawa (1.69 PPG) 0:2 · 10.10. H Pogoń Grod. Mazowiecki (1.62 PPG) 0:4 · 17.10. A Polonia Bytom (1.62 PPG) 2:3 · 24.10. A Stal Mielec (1.23 PPG) 0:0

Letzte 6 Arka Gdynia: 06.09. H ŁKS Łódź (1.69 PPG) 1:1 · 12.09. A Warta Poznań (1.46 PPG) 0:3 · 20.09. A Pogoń Siedlce (1.25 PPG) 1:2 · 10.10. H Polonia Warszawa (1.69 PPG) 1:2 · 18.10. A Lechia Gdańsk (1.69 PPG) 1:2 · 24.10. H Nieciecza (1.62 PPG) 3:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Chrobry Głogów [5, 0, 2, 1, 0, 2, 1, 0, 0, 0, 2, 0]; Arka Gdynia [1, 4, 0, 3, 0, 1, 1, 0, 1, 1, 1, 3]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Chrobry daheim mit 3 Toren in 6 Spielen und 67 % torlosen Heimspielen, während auch Arka auswärts nur 3 Tore in 6 erzielte (50 % torlos); der Weg zu drei Toren ist schwach, weil Chrobry-Heimspiele zu 83 % Under endeten und das Modell 57 % Under schätzt; stärkstes Gegenargument ist Arkas letzte-sechs-Bild mit 83 % Over und Chrobrys 0:4 daheim gegen Grodzisk, das zeigt, dass ein einseitiges Spiel drei Tore hergeben kann, und als wesentliche Gefahr gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1033 Spiele, Saisons [9596, 12156, 14877, 17301]; Schätzung λ Heim 0.945, λ Gast 1.463. Prüfstand (unberührter Test, 104 Spiele ab 2026-08-01): Heimsieg nicht besser als Grundrate (Brier 0.2555 gegen 0.25); Auswärtssieg nicht besser als Grundrate (Brier 0.2062 gegen 0.2038); BTTS Ja besser als Grundrate (Brier 0.2425 gegen 0.248); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2429 gegen 0.2518). Grenzen: 9 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 24 % · Remis 26 % · Auswärtssieg 49 % · BTTS Ja 47 % · Over 2,5 43 % · Under 2,5 57 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.5 · X 3.2 · 2 2.55 · BTTS Ja 1.77 · Over 2,5 2.12 · Under 2,5 1.68.

**Auswahl:** Under 2,5

⚠️ Arka: 5 der letzten 6 Spiele Over 2,5; Chrobry verlor daheim zuletzt 0:4.

---

## 5.4 2 de Mayo – Sportivo Trinidense | 2026-11-03 20:00 UTC | Paraguay División Profesional 2026, Spieltag 18 | Match-ID 8581483

Analyse-ID: A-20261103-8581483-r1 · Team-IDs: 6696 / 6684 · Saison-ID: 16533 · Status beim Abruf: incomplete · Ort: Estadio Monumental Río Parapití · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026: 39 bzw. 39 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-01-23 bis 2026-10-30, Gast 2026-01-23 bis 2026-10-30; letzte 6: Heim 2026-09-26–2026-10-30, Gast 2026-09-26–2026-10-30.

**2 de Mayo (Heim, ID 6696)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 39 | 19 | 20 | 6
Tore | 36 | 17 | 19 | 6
Gegentore | 53 | 18 | 35 | 7
Tore/Spiel | 0.92 | 0.89 | 0.95 | 1.00
Gegentore/Spiel | 1.36 | 0.95 | 1.75 | 1.17
xG für/Spiel | 1.15 | 1.17 | 1.13 | 1.21
xG gegen/Spiel | 1.37 | 1.17 | 1.57 | 1.59
Spiele mit xG | 39 | 19 | 20 | 6
S/U/N | 13/12/14 | 6/7/6 | 7/5/8 | 2/2/2
Punkte/Spiel | 1.31 | 1.32 | 1.30 | 1.33
BTTS % | 44 % | 42 % | 45 % | 33 %
Over 2,5 % | 41 % | 26 % | 55 % | 33 %
Under 2,5 % | 59 % | 74 % | 45 % | 67 %
Clean Sheets % | 31 % | 37 % | 25 % | 33 %
Failed to Score % | 33 % | 32 % | 35 % | 33 %
BTTS-and-lose % | 10 % | 11 % | 10 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Sportivo Trinidense (Gast, ID 6684)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 39 | 20 | 19 | 6
Tore | 58 | 32 | 26 | 10
Gegentore | 42 | 22 | 20 | 8
Tore/Spiel | 1.49 | 1.60 | 1.37 | 1.67
Gegentore/Spiel | 1.08 | 1.10 | 1.05 | 1.33
xG für/Spiel | 1.47 | 1.48 | 1.46 | 1.59
xG gegen/Spiel | 1.38 | 1.38 | 1.38 | 1.53
Spiele mit xG | 39 | 20 | 19 | 6
S/U/N | 17/11/11 | 10/5/5 | 7/6/6 | 4/1/1
Punkte/Spiel | 1.59 | 1.75 | 1.42 | 2.17
BTTS % | 67 % | 65 % | 68 % | 67 %
Over 2,5 % | 54 % | 55 % | 53 % | 50 %
Under 2,5 % | 46 % | 45 % | 47 % | 50 %
Clean Sheets % | 26 % | 25 % | 26 % | 33 %
Failed to Score % | 15 % | 15 % | 16 % | 0 %
BTTS-and-lose % | 21 % | 15 % | 26 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 2 de Mayo: 26.09. A Rubio Ñú (1.00 PPG) 2:2 · 05.10. A Cerro Porteño (1.63 PPG) 2:0 · 12.10. H Sportivo Ameliano (1.33 PPG) 1:0 · 17.10. A Olimpia (2.16 PPG) 0:3 · 24.10. H Deportivo Recoleta (1.10 PPG) 1:1 · 30.10. A Guaraní (1.46 PPG) 0:1

Letzte 6 Sportivo Trinidense: 26.09. H Cerro Porteño (1.63 PPG) 2:1 · 05.10. H Sportivo Luqueño (0.92 PPG) 3:2 · 10.10. A Sportivo San Lorenzo (0.56 PPG) 1:1 · 18.10. H Libertad (1.56 PPG) 1:0 · 24.10. A Nacional Asunción (1.82 PPG) 1:0 · 30.10. H Rubio Ñú (1.00 PPG) 2:4

Torverteilung Saison (eigene Tore je Spiel, chronologisch): 2 de Mayo [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 2, 1, 1, 1, 0, 1, 0, 2, 2, 2, 0, 0, 1, 2, 1, 1, 2, 0, 1, 2, 2, 0, 0, 2, 2, 1, 0, 1, 0]; Sportivo Trinidense [1, 0, 2, 1, 1, 1, 1, 0, 1, 1, 1, 3, 0, 2, 4, 1, 2, 1, 1, 1, 3, 2, 2, 4, 3, 1, 1, 0, 0, 3, 1, 3, 0, 2, 3, 1, 1, 1, 2]

**Bild:** Saison 2026 mit je 39 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist 2 de Mayo mit 0,92 Toren/Spiel und 1,15 xG, gegen Trinidenses Abwehr mit 26 % Clean Sheets; der Weg zu drei Toren ist schwach, weil 2-de-Mayo-Heimspiele nur zu 26 % Over endeten (1,84 Tore/Spiel) und das Modell 59 % Under schätzt; stärkstes Gegenargument ist Trinidenses Auswärtsprofil mit 53 % Over und 68 % BTTS, das als wesentliche Gefahr gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1025 Spiele, Saisons [8783, 11141, 16333, 16533]; Schätzung λ Heim 1.088, λ Gast 1.227. Prüfstand (unberührter Test, 103 Spiele ab 2026-05-24): Heimsieg besser als Grundrate (Brier 0.2158 gegen 0.2399); Auswärtssieg besser als Grundrate (Brier 0.2112 gegen 0.2355); BTTS Ja besser als Grundrate (Brier 0.2457 gegen 0.25); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2482 gegen 0.2552). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 33 % · Remis 28 % · Auswärtssieg 39 % · BTTS Ja 47 % · Over 2,5 41 % · Under 2,5 59 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 3.1 · X 3.1 · 2 2.05 · BTTS Ja 1.9 · Over 2,5 2.08 · Under 2,5 1.64.

**Auswahl:** Under 2,5

⚠️ Trinidense auswärts mit 53 % Over und 68 % BTTS.

---

## 5.5 Nacional Asunción – Sportivo San Lorenzo | 2026-11-03 22:30 UTC | Paraguay División Profesional 2026, Spieltag 18 | Match-ID 8581468

Analyse-ID: A-20261103-8581468-r1 · Team-IDs: 6676 / 6691 · Saison-ID: 16533 · Status beim Abruf: incomplete · Ort: Estadio Arsenio Erico · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-03 14:33 UTC; Datenbasis: verwendbar (Saison 2026: 39 bzw. 39 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-01-24 bis 2026-10-31, Gast 2026-01-24 bis 2026-10-31; letzte 6: Heim 2026-09-25–2026-10-31, Gast 2026-09-28–2026-10-31.

**Nacional Asunción (Heim, ID 6676)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 39 | 19 | 20 | 6
Tore | 57 | 31 | 26 | 8
Gegentore | 31 | 12 | 19 | 3
Tore/Spiel | 1.46 | 1.63 | 1.30 | 1.33
Gegentore/Spiel | 0.79 | 0.63 | 0.95 | 0.50
xG für/Spiel | 1.37 | 1.43 | 1.32 | 1.47
xG gegen/Spiel | 1.29 | 1.27 | 1.30 | 1.66
Spiele mit xG | 39 | 19 | 20 | 6
S/U/N | 19/14/6 | 12/5/2 | 7/9/4 | 3/2/1
Punkte/Spiel | 1.82 | 2.16 | 1.50 | 1.83
BTTS % | 51 % | 47 % | 55 % | 33 %
Over 2,5 % | 38 % | 42 % | 35 % | 17 %
Under 2,5 % | 62 % | 58 % | 65 % | 83 %
Clean Sheets % | 41 % | 47 % | 35 % | 50 %
Failed to Score % | 15 % | 16 % | 15 % | 17 %
BTTS-and-lose % | 8 % | 5 % | 10 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Sportivo San Lorenzo (Gast, ID 6691)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 39 | 20 | 19 | 6
Tore | 24 | 12 | 12 | 7
Gegentore | 71 | 35 | 36 | 9
Tore/Spiel | 0.62 | 0.60 | 0.63 | 1.17
Gegentore/Spiel | 1.82 | 1.75 | 1.89 | 1.50
xG für/Spiel | 1.19 | 1.23 | 1.16 | 1.47
xG gegen/Spiel | 1.71 | 1.62 | 1.82 | 1.89
Spiele mit xG | 39 | 20 | 19 | 6
S/U/N | 4/10/25 | 3/6/11 | 1/4/14 | 1/3/2
Punkte/Spiel | 0.56 | 0.75 | 0.37 | 1.00
BTTS % | 44 % | 40 % | 47 % | 83 %
Over 2,5 % | 41 % | 45 % | 37 % | 50 %
Under 2,5 % | 59 % | 55 % | 63 % | 50 %
Clean Sheets % | 15 % | 25 % | 5 % | 17 %
Failed to Score % | 49 % | 50 % | 47 % | 17 %
BTTS-and-lose % | 23 % | 20 % | 26 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Nacional Asunción: 25.09. H Sportivo Ameliano (1.33 PPG) 1:1 · 06.10. A Olimpia (2.16 PPG) 1:1 · 12.10. H Deportivo Recoleta (1.10 PPG) 1:0 · 17.10. A Guaraní (1.46 PPG) 2:0 · 24.10. H Sportivo Trinidense (1.59 PPG) 0:1 · 31.10. A Sportivo Luqueño (0.92 PPG) 3:0

Letzte 6 Sportivo San Lorenzo: 28.09. H Deportivo Recoleta (1.10 PPG) 0:0 · 03.10. A Guaraní (1.46 PPG) 1:1 · 10.10. H Sportivo Trinidense (1.59 PPG) 1:1 · 18.10. A Sportivo Luqueño (0.92 PPG) 2:3 · 25.10. H Cerro Porteño (1.63 PPG) 1:3 · 31.10. H Libertad (1.56 PPG) 2:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Nacional Asunción [1, 2, 5, 1, 2, 1, 2, 1, 1, 1, 1, 0, 3, 1, 0, 0, 1, 2, 1, 2, 1, 2, 1, 2, 2, 0, 1, 2, 3, 3, 0, 1, 3, 1, 1, 1, 2, 0, 3]; Sportivo San Lorenzo [0, 2, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 2, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1, 2]

**Bild:** Saison 2026 mit je 39 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist San Lorenzo auswärts mit 12 Toren in 19 Spielen und 47 % torlosen Spielen, gegen Nacionals Heimabwehr mit 12 Gegentoren in 19; der Weg zu drei Toren ist mit 42 % Over in Nacional-Heimspielen unsicher und wird nicht gewählt; stärkstes Gegenargument ist San Lorenzos verbesserte Form (1,00 Punkte/Spiel in den letzten sechs, 2:1 gegen Libertad) und Nacionals negative xG-Bilanz der letzten sechs (1,47 zu 1,66), die gegen Nacionals 12-5-2 daheim und San Lorenzos 1-4-14 auswärts den Heimsieg (Modell 62 %) aber nicht entkräften.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 1025 Spiele, Saisons [8783, 11141, 16333, 16533]; Schätzung λ Heim 1.682, λ Gast 0.649. Prüfstand (unberührter Test, 103 Spiele ab 2026-05-24): Heimsieg besser als Grundrate (Brier 0.2158 gegen 0.2399); Auswärtssieg besser als Grundrate (Brier 0.2112 gegen 0.2355); BTTS Ja besser als Grundrate (Brier 0.2457 gegen 0.25); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2482 gegen 0.2552). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 62 % · Remis 24 % · Auswärtssieg 14 % · BTTS Ja 39 % · Over 2,5 41 % · Under 2,5 59 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-03 14:32 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.28 · X 4.9 · 2 9 · BTTS Ja 2.2 · Over 2,5 1.67 · Under 2,5 2.04.

**Auswahl:** Heimsieg

---
