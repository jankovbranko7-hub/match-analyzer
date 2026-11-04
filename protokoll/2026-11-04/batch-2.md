# Vorabeintrag Batch 2 · 04.11.2026

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-04 16:19 UTC
- Eintrag erstellt: 2026-11-04 16:22:05 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen des jeweiligen Wettbewerbs berechnet (bei der Champions League: nur Ligaphase dieser Saison, letzte 6 = vorhandene Spiele; Landesliga-Tabellen getrennt) (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 2.1 Cardiff City – West Ham United | 2026-11-04 19:45 UTC | England Championship 2026/2027, Spieltag 14 | Match-ID 8566637

Analyse-ID: A-20261104-8566637-r1 · Team-IDs: 161 / 153 · Saison-ID: 17184 · Status beim Abruf: incomplete · Ort: Cardiff City Stadium

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 13 bzw. 13 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-17 bis 2026-10-31, Gast 2026-08-16 bis 2026-10-31; letzte 6: Heim 2026-09-19–2026-10-31, Gast 2026-09-19–2026-10-31.

**Cardiff City (Heim, ID 161)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 6 | 7 | 6
Tore | 19 | 13 | 6 | 12
Gegentore | 20 | 6 | 14 | 9
Tore/Spiel | 1.46 | 2.17 | 0.86 | 2.00
Gegentore/Spiel | 1.54 | 1.00 | 2.00 | 1.50
xG für/Spiel | 1.92 | 2.34 | 1.56 | 1.79
xG gegen/Spiel | 1.54 | 1.16 | 1.87 | 1.63
Spiele mit xG | 13 | 6 | 7 | 6
S/U/N | 3/5/5 | 3/3/0 | 0/2/5 | 3/1/2
Punkte/Spiel | 1.08 | 2.00 | 0.29 | 1.67
BTTS % | 69 % | 83 % | 57 % | 67 %
Over 2,5 % | 62 % | 50 % | 71 % | 83 %
Under 2,5 % | 38 % | 50 % | 29 % | 17 %
Clean Sheets % | 8 % | 17 % | 0 % | 17 %
Failed to Score % | 23 % | 0 % | 43 % | 17 %
BTTS-and-lose % | 15 % | 0 % | 29 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**West Ham United (Gast, ID 153)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 13 | 7 | 6 | 6
Tore | 33 | 18 | 15 | 13
Gegentore | 18 | 11 | 7 | 9
Tore/Spiel | 2.54 | 2.57 | 2.50 | 2.17
Gegentore/Spiel | 1.38 | 1.57 | 1.17 | 1.50
xG für/Spiel | 1.94 | 2.10 | 1.74 | 2.13
xG gegen/Spiel | 1.27 | 1.11 | 1.45 | 1.22
Spiele mit xG | 13 | 7 | 6 | 6
S/U/N | 6/4/3 | 3/1/3 | 3/3/0 | 2/2/2
Punkte/Spiel | 1.69 | 1.43 | 2.00 | 1.33
BTTS % | 69 % | 71 % | 67 % | 67 %
Over 2,5 % | 77 % | 86 % | 67 % | 67 %
Under 2,5 % | 23 % | 14 % | 33 % | 33 %
Clean Sheets % | 31 % | 29 % | 33 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 23 % | 43 % | 0 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Cardiff City: 19.09. H Charlton Athletic (1.00 PPG) 3:1 · 10.10. A Blackburn Rovers (1.29 PPG) 1:2 · 13.10. H Watford (1.00 PPG) 5:1 · 17.10. A Middlesbrough (2.15 PPG) 2:2 · 24.10. H Birmingham City (1.86 PPG) 1:0 · 31.10. A Wolverhampton Wanderers (1.85 PPG) 0:3

Letzte 6 West Ham United: 19.09. A Millwall (1.29 PPG) 2:2 · 09.10. H Queens Park Rangers (1.50 PPG) 1:1 · 14.10. A Lincoln City (1.07 PPG) 6:0 · 17.10. A Swansea City (1.86 PPG) 1:0 · 24.10. H Southampton (2.00 PPG) 2:3 · 31.10. H West Bromwich Albion (1.79 PPG) 1:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Cardiff City [1, 2, 2, 1, 0, 1, 0, 3, 1, 5, 2, 1, 0]; West Ham United [2, 1, 1, 4, 3, 3, 6, 2, 1, 6, 1, 2, 1]

**Bild:** Saison 2026/27 mit je 13 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Cardiff mit 1,46 Toren pro Spiel, das aber in allen 6 Heimspielen traf (2,34 xG daheim) gegen West Ham, während West Ham in allen 13 Saisonspielen traf gegen Cardiffs Heimabwehr mit nur 17 % Clean Sheets; der Weg zu drei Toren ist mit 50 % bzw. 67 % Over beider Kontexte schwächer belegt als BTTS (Modell 56 %); stärkstes Gegenargument sind West Hams 2 Zu-null-Spiele in 6 Auswärtsspielen, die gegen Cardiffs Heimchancen keine wesentliche Gefahr für den Heimtreffer begründen.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1821 Spiele, Saisons [9663, 12451, 14930, 17184]; Schätzung λ Heim 1.395, λ Gast 1.339. Prüfstand (unberührter Test, 183 Spiele ab 2026-04-25): Heimsieg besser als Grundrate (Brier 0.2422 gegen 0.2447); Auswärtssieg besser als Grundrate (Brier 0.2165 gegen 0.219); BTTS Ja nicht besser als Grundrate (Brier 0.2467 gegen 0.2433); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2592 gegen 0.2533). Grenzen: 15 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 38 % · Remis 26 % · Auswärtssieg 36 % · BTTS Ja 56 % · Over 2,5 51 % · Under 2,5 49 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.83 · X 3.85 · 2 1.96 · BTTS Ja 1.34 · Over 2,5 1.36 · Under 2,5 3.2.

**Auswahl:** BTTS Ja

---

## 2.2 Oxford United – Reading

**Bild:** Spielidentität ungeklärt: Oxford United – Reading ist im Tagesplan der API für den 04.11.2026 nicht vorhanden, in der Championship-Saison nicht enthalten, und die League One ist im API-Abo nicht abrufbar (HTTP 417 ohne Abfragelimit); nach Abschnitt 2 wird die Begegnung nicht geraten, deshalb keine Analyse und keine Auswahl.

**Auswahl:** keine

---

## 2.3 Fenerbahçe – Liverpool | 2026-11-04 17:45 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700181

Analyse-ID: A-20261104-8700181-r1 · Team-IDs: 105 / 151 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Şükrü Saracoğlu Stadium · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-10 bis 2026-10-20, Gast 2026-09-09 bis 2026-10-20; letzte 6: Heim 2026-09-10–2026-10-20, Gast 2026-09-09–2026-10-20.

**Fenerbahçe (Heim, ID 105)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 3 | 3 | 0 | 3
Gegentore | 9 | 3 | 6 | 9
Tore/Spiel | 1.00 | 1.50 | 0.00 | 1.00
Gegentore/Spiel | 3.00 | 1.50 | 6.00 | 3.00
xG für/Spiel | 1.44 | 1.36 | 1.60 | 1.44
xG gegen/Spiel | 1.72 | 1.40 | 2.35 | 1.72
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 0/2/1 | 0/2/0 | 0/0/1 | 0/2/1
Punkte/Spiel | 0.67 | 1.00 | 0.00 | 0.67
BTTS % | 67 % | 100 % | 0 % | 67 %
Over 2,5 % | 67 % | 50 % | 100 % | 67 %
Under 2,5 % | 33 % | 50 % | 0 % | 33 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 33 % | 0 % | 100 % | 33 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Liverpool (Gast, ID 151)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 12 | 6 | 6 | 12
Gegentore | 7 | 4 | 3 | 7
Tore/Spiel | 4.00 | 3.00 | 6.00 | 4.00
Gegentore/Spiel | 2.33 | 2.00 | 3.00 | 2.33
xG für/Spiel | 2.23 | 1.98 | 2.72 | 2.23
xG gegen/Spiel | 1.33 | 1.33 | 1.32 | 1.33
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 3/0/0 | 2/0/0 | 1/0/0 | 3/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**Fenerbahçe – Landesliga (Saison-ID 17265, 2026-08-15 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 10 | 5 | 5 | 6
Tore | 24 | 17 | 7 | 16
Gegentore | 10 | 6 | 4 | 4
Tore/Spiel | 2.40 | 3.40 | 1.40 | 2.67
Gegentore/Spiel | 1.00 | 1.20 | 0.80 | 0.67
xG für/Spiel | 1.89 | 2.07 | 1.71 | 1.82
xG gegen/Spiel | 1.53 | 1.65 | 1.41 | 1.66
Spiele mit xG | 10 | 5 | 5 | 6
S/U/N | 5/1/4 | 3/0/2 | 2/1/2 | 3/1/2
Punkte/Spiel | 1.60 | 1.80 | 1.40 | 1.67
BTTS % | 50 % | 60 % | 40 % | 33 %
Over 2,5 % | 80 % | 100 % | 60 % | 83 %
Under 2,5 % | 20 % | 0 % | 40 % | 17 %
Clean Sheets % | 50 % | 40 % | 60 % | 67 %
Failed to Score % | 10 % | 0 % | 20 % | 17 %
BTTS-and-lose % | 40 % | 40 % | 40 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Liverpool – Landesliga (Saison-ID 17146, 2026-08-23 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 11 | 4 | 7 | 5
Gegentore | 9 | 6 | 3 | 5
Tore/Spiel | 1.22 | 0.80 | 1.75 | 0.83
Gegentore/Spiel | 1.00 | 1.20 | 0.75 | 0.83
xG für/Spiel | 1.69 | 1.54 | 1.88 | 1.57
xG gegen/Spiel | 1.31 | 1.35 | 1.26 | 1.31
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 4/3/2 | 1/2/2 | 3/1/0 | 3/1/2
Punkte/Spiel | 1.67 | 1.00 | 2.50 | 1.67
BTTS % | 33 % | 20 % | 50 % | 17 %
Over 2,5 % | 44 % | 40 % | 50 % | 33 %
Under 2,5 % | 56 % | 60 % | 50 % | 67 %
Clean Sheets % | 44 % | 40 % | 50 % | 50 %
Failed to Score % | 33 % | 60 % | 0 % | 50 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Fenerbahçe: 10.09. H Roma (1.00 PPG) 1:1 · 14.10. A Aston Villa (2.25 PPG) 0:6 · 20.10. H Slavia Praha (0.33 PPG) 2:2

Letzte 6 Liverpool: 09.09. H Atlético Madrid (1.00 PPG) 2:1 · 14.10. A LASK Linz (1.50 PPG) 6:3 · 20.10. H Villarreal (0.75 PPG) 4:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Fenerbahçe [1, 0, 2]; Liverpool [2, 6, 4]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Fenerbahçe mit 3 Toren in 3 Champions-League-Spielen, gegen Liverpool, während Liverpool alle 3 Champions-League-Spiele gewann (12 Tore) und in der Premier League auswärts 3-1-0 steht; der Weg zu drei Toren ist mit Liverpools Champions-League-Spielen (3, 9 und 7 Tore) plausibel, widerspricht aber Liverpools Premier-League-Bild der letzten sechs mit nur 33 % Over, weshalb der Auswärtssieg (Modell 59 %) besser belegt ist; stärkstes Gegenargument ist Fenerbahçes Heimstärke mit beiden Champions-League-Heimspielen remis (1:1 Roma, 2:2 Slavia) und 17 Ligatoren in 5 Heimspielen, was das Remisrisiko erhöht und als wesentliche Gefahr gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 447 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.316, λ Gast 2.270. Prüfstand (unberührter Test, 45 Spiele ab 2026-10-13): Heimsieg besser als Grundrate (Brier 0.195 gegen 0.2492); Auswärtssieg besser als Grundrate (Brier 0.1878 gegen 0.2222); BTTS Ja nicht besser als Grundrate (Brier 0.2656 gegen 0.2495); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2223 gegen 0.211). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 21 % · Remis 20 % · Auswärtssieg 59 % · BTTS Ja 66 % · Over 2,5 69 % · Under 2,5 31 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 5.75 · X 4.9 · 2 1.5 · BTTS Ja 1.47 · Over 2,5 1.36 · Under 2,5 3.14.

**Auswahl:** Auswärtssieg

⚠️ Fenerbahçe spielte beide Champions-League-Heimspiele remis – Remisrisiko.

---

## 2.4 AEK Athens – Real Madrid | 2026-11-04 17:45 UTC | UEFA Champions League 2026/2027, Spieltag 4 | Match-ID 8700785

Analyse-ID: A-20261104-8700785-r1 · Team-IDs: 1101 / 84 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: OPAP Arena · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-08 bis 2026-10-20, Gast 2026-09-08 bis 2026-10-21; letzte 6: Heim 2026-09-08–2026-10-20, Gast 2026-09-08–2026-10-21.

**AEK Athens (Heim, ID 1101)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 3 | 1 | 2 | 3
Gegentore | 8 | 0 | 8 | 8
Tore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
Gegentore/Spiel | 2.67 | 0.00 | 4.00 | 2.67
xG für/Spiel | 1.37 | 1.77 | 1.17 | 1.37
xG gegen/Spiel | 1.49 | 1.15 | 1.66 | 1.49
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 1/0/0 | 0/0/2 | 1/0/2
Punkte/Spiel | 1.00 | 3.00 | 0.00 | 1.00
BTTS % | 67 % | 0 % | 100 % | 67 %
Over 2,5 % | 67 % | 0 % | 100 % | 67 %
Under 2,5 % | 33 % | 100 % | 0 % | 33 %
Clean Sheets % | 33 % | 100 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 67 % | 0 % | 100 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Real Madrid (Gast, ID 84)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 10 | 6 | 4 | 10
Gegentore | 5 | 2 | 3 | 5
Tore/Spiel | 3.33 | 3.00 | 4.00 | 3.33
Gegentore/Spiel | 1.67 | 1.00 | 3.00 | 1.67
xG für/Spiel | 2.03 | 2.09 | 1.91 | 2.03
xG gegen/Spiel | 1.84 | 1.94 | 1.64 | 1.84
Spiele mit xG | 3 | 2 | 1 | 3
S/U/N | 3/0/0 | 2/0/0 | 1/0/0 | 3/0/0
Punkte/Spiel | 3.00 | 3.00 | 3.00 | 3.00
BTTS % | 100 % | 100 % | 100 % | 100 %
Over 2,5 % | 100 % | 100 % | 100 % | 100 %
Under 2,5 % | 0 % | 0 % | 0 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Landesliga-Daten (getrennt von der Champions League, andere Skala):**

**AEK Athens – Landesliga (Saison-ID 17356, 2026-08-22 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 21 | 17 | 4 | 16
Gegentore | 5 | 0 | 5 | 4
Tore/Spiel | 2.62 | 4.25 | 1.00 | 2.67
Gegentore/Spiel | 0.62 | 0.00 | 1.25 | 0.67
xG für/Spiel | 1.97 | 2.49 | 1.44 | 1.96
xG gegen/Spiel | 1.06 | 0.75 | 1.37 | 1.06
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 5/2/1 | 4/0/0 | 1/2/1 | 4/1/1
Punkte/Spiel | 2.12 | 3.00 | 1.25 | 2.17
BTTS % | 38 % | 0 % | 75 % | 33 %
Over 2,5 % | 62 % | 100 % | 25 % | 67 %
Under 2,5 % | 38 % | 0 % | 75 % | 33 %
Clean Sheets % | 50 % | 100 % | 0 % | 50 %
Failed to Score % | 12 % | 0 % | 25 % | 17 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Real Madrid – Landesliga (Saison-ID 17199, 2026-08-22 bis 2026-11-01)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 5 | 6 | 6
Tore | 28 | 17 | 11 | 14
Gegentore | 10 | 3 | 7 | 6
Tore/Spiel | 2.55 | 3.40 | 1.83 | 2.33
Gegentore/Spiel | 0.91 | 0.60 | 1.17 | 1.00
xG für/Spiel | 1.98 | 2.11 | 1.87 | 1.61
xG gegen/Spiel | 1.46 | 1.45 | 1.46 | 1.58
Spiele mit xG | 11 | 5 | 6 | 6
S/U/N | 9/0/2 | 5/0/0 | 4/0/2 | 5/0/1
Punkte/Spiel | 2.45 | 3.00 | 2.00 | 2.50
BTTS % | 64 % | 60 % | 67 % | 67 %
Over 2,5 % | 82 % | 80 % | 83 % | 83 %
Under 2,5 % | 18 % | 20 % | 17 % | 17 %
Clean Sheets % | 27 % | 40 % | 17 % | 33 %
Failed to Score % | 9 % | 0 % | 17 % | 0 %
BTTS-and-lose % | 9 % | 0 % | 17 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 AEK Athens: 08.09. H LASK Linz (1.50 PPG) 1:0 · 14.10. A Shakhtar Donetsk (1.00 PPG) 1:3 · 20.10. A Manchester City (2.00 PPG) 1:5

Letzte 6 Real Madrid: 08.09. H Inter Milan (1.50 PPG) 2:1 · 14.10. A Roma (1.00 PPG) 4:3 · 21.10. H RB Leipzig (1.00 PPG) 4:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): AEK Athens [1, 1, 1]; Real Madrid [2, 4, 4]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist AEK mit 3 Toren in 3 Champions-League-Spielen, gegen Real Madrid mit 5 Champions-League-Gegentoren in 3; der Weg zu drei Toren ist stark, weil Reals Champions-League-Spiele 3, 7 und 5 Tore brachten, Real in La Liga auswärts zu 83 % Over spielte und mit 10 Champions-League-Toren auch allein drei Tore liefern kann, und das Modell schätzt 74 %; stärkstes Gegenargument ist AEKs Heimabwehr (Liga 17:0 Tore in 4 Heimspielen, Champions League 1:0 gegen LASK), die aber auf griechischem Niveau und gegen LASK entstand und keine wesentliche Gefahr begründet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 447 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.599, λ Gast 2.270. Prüfstand (unberührter Test, 45 Spiele ab 2026-10-13): Heimsieg besser als Grundrate (Brier 0.195 gegen 0.2492); Auswärtssieg besser als Grundrate (Brier 0.1878 gegen 0.2222); BTTS Ja nicht besser als Grundrate (Brier 0.2656 gegen 0.2495); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2223 gegen 0.211). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 27 % · Remis 20 % · Auswärtssieg 53 % · BTTS Ja 72 % · Over 2,5 74 % · Under 2,5 26 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 10.5 · X 6.75 · 2 1.25 · BTTS Ja 1.67 · Over 2,5 1.28 · Under 2,5 3.7.

**Auswahl:** Over 2,5

---

## 2.5 RB Leipzig – Manchester City | 2026-11-04 20:00 UTC | UEFA Champions League 2026/2027, Spieltag 1 | Match-ID 8700165

Analyse-ID: A-20261104-8700165-r1 · Team-IDs: 46 / 93 · Saison-ID: 17128 · Status beim Abruf: incomplete · Ort: Red Bull Arena · API-Feld no_home_away=1 (ligaweit gesetzt, Bedeutung nicht geprüft; nicht als neutraler Platz gewertet)

Datenstand: 2026-11-04 16:19 UTC; Datenbasis: verwendbar (Saison 2026/2027: 3 bzw. 3 Ligaspiele; xG für alle Spiele; 90 K.-o.-/Play-off-Spiele der Saison ausgeschlossen).

Zeitraum Saison: Heim 2026-09-10 bis 2026-10-21, Gast 2026-09-08 bis 2026-10-20; letzte 6: Heim 2026-09-10–2026-10-21, Gast 2026-09-08–2026-10-20.

**RB Leipzig (Heim, ID 46)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 1 | 2 | 3
Tore | 3 | 1 | 2 | 3
Gegentore | 8 | 0 | 8 | 8
Tore/Spiel | 1.00 | 1.00 | 1.00 | 1.00
Gegentore/Spiel | 2.67 | 0.00 | 4.00 | 2.67
xG für/Spiel | 1.68 | 2.08 | 1.48 | 1.68
xG gegen/Spiel | 1.77 | 1.40 | 1.95 | 1.77
Spiele mit xG | 3 | 1 | 2 | 3
S/U/N | 1/0/2 | 1/0/0 | 0/0/2 | 1/0/2
Punkte/Spiel | 1.00 | 3.00 | 0.00 | 1.00
BTTS % | 67 % | 0 % | 100 % | 67 %
Over 2,5 % | 67 % | 0 % | 100 % | 67 %
Under 2,5 % | 33 % | 100 % | 0 % | 33 %
Clean Sheets % | 33 % | 100 % | 0 % | 33 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 67 % | 0 % | 100 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Manchester City (Gast, ID 93)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 3 | 2 | 1 | 3
Tore | 9 | 7 | 2 | 9
Gegentore | 5 | 5 | 0 | 5
Tore/Spiel | 3.00 | 3.50 | 2.00 | 3.00
Gegentore/Spiel | 1.67 | 2.50 | 0.00 | 1.67
xG für/Spiel | 2.41 | 2.44 | 2.36 | 2.41
xG gegen/Spiel | 1.13 | 1.45 | 0.50 | 1.13
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

**RB Leipzig – Landesliga (Saison-ID 17210, 2026-08-29 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 22 | 18 | 4 | 18
Gegentore | 11 | 0 | 11 | 8
Tore/Spiel | 2.75 | 4.50 | 1.00 | 3.00
Gegentore/Spiel | 1.38 | 0.00 | 2.75 | 1.33
xG für/Spiel | 1.91 | 2.08 | 1.73 | 1.73
xG gegen/Spiel | 1.63 | 1.40 | 1.86 | 1.68
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 5/0/3 | 4/0/0 | 1/0/3 | 4/0/2
Punkte/Spiel | 1.88 | 3.00 | 0.75 | 2.00
BTTS % | 25 % | 0 % | 50 % | 17 %
Over 2,5 % | 75 % | 100 % | 50 % | 67 %
Under 2,5 % | 25 % | 0 % | 50 % | 33 %
Clean Sheets % | 62 % | 100 % | 25 % | 67 %
Failed to Score % | 12 % | 0 % | 25 % | 17 %
BTTS-and-lose % | 25 % | 0 % | 50 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Manchester City – Landesliga (Saison-ID 17146, 2026-08-23 bis 2026-10-31)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 20 | 11 | 9 | 13
Gegentore | 10 | 7 | 3 | 8
Tore/Spiel | 2.22 | 2.20 | 2.25 | 2.17
Gegentore/Spiel | 1.11 | 1.40 | 0.75 | 1.33
xG für/Spiel | 1.80 | 1.91 | 1.67 | 1.76
xG gegen/Spiel | 1.14 | 1.10 | 1.20 | 1.27
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 7/0/2 | 4/0/1 | 3/0/1 | 4/0/2
Punkte/Spiel | 2.33 | 2.40 | 2.25 | 2.00
BTTS % | 56 % | 60 % | 50 % | 50 %
Over 2,5 % | 67 % | 60 % | 75 % | 67 %
Under 2,5 % | 33 % | 40 % | 25 % | 33 %
Clean Sheets % | 33 % | 20 % | 50 % | 33 %
Failed to Score % | 11 % | 20 % | 0 % | 17 %
BTTS-and-lose % | 11 % | 0 % | 25 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 RB Leipzig: 10.09. A Como (2.00 PPG) 1:4 · 13.10. H PSV (1.33 PPG) 1:0 · 21.10. A Real Madrid (3.00 PPG) 1:4

Letzte 6 Manchester City: 08.09. A Porto (0.00 PPG) 2:0 · 14.10. H PSG (3.00 PPG) 2:4 · 20.10. H AEK Athens (1.00 PPG) 5:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): RB Leipzig [1, 1, 1]; Manchester City [2, 2, 5]

**Bild:** Champions League 2026/27 mit je 3 Spielen und Landesliga-Daten ist verwendbar, die Champions-League-Daten (je 3 Spiele, Gegner unterschiedlich stark) sind klein und die Landesliga-Tabellen stammen aus verschiedenen Ligen ohne gemeinsame Skala; schwächere Offensive ist Leipzig mit 3 Toren in 3 Champions-League-Spielen, gegen Manchester City mit 1,13 xG gegen; der Weg zu drei Toren läuft über beide Teams und notfalls einseitig, weil Leipzigs Champions-League-Spiele 5, 1 und 5 Tore, Citys 2, 6 und 6 Tore brachten, Leipzig daheim in der Bundesliga 18 Tore in 4 Spielen erzielte und City in der Premier League auswärts zu 75 % Over spielte, das Modell schätzt 67 %; stärkstes Gegenargument ist Leipzigs Champions-League-Heimspiel gegen PSV mit nur einem Tor, das als Einzelspiel keine wesentliche Gefahr begründet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 447 Spiele, Saisons [9543, 12321, 14924, 17128]; Schätzung λ Heim 1.562, λ Gast 1.879. Prüfstand (unberührter Test, 45 Spiele ab 2026-10-13): Heimsieg besser als Grundrate (Brier 0.195 gegen 0.2492); Auswärtssieg besser als Grundrate (Brier 0.1878 gegen 0.2222); BTTS Ja nicht besser als Grundrate (Brier 0.2656 gegen 0.2495); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2223 gegen 0.211). Grenzen: 480 K.-o.-/Play-off-Spiele aus dem Training ausgeschlossen; unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 32 % · Remis 22 % · Auswärtssieg 45 % · BTTS Ja 67 % · Over 2,5 67 % · Under 2,5 33 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-04 16:18 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 4.65 · X 4.6 · 2 1.53 · BTTS Ja 1.33 · Over 2,5 1.27 · Under 2,5 3.56.

**Auswahl:** Over 2,5

---
