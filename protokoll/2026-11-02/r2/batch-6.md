# Vorabeintrag Batch 6 · 02.11.2026 · Revision r2

**Revision r2** (vor allen Anstößen erstellt, ersetzt r1 in `../batch-6.md`; r1 bleibt unverändert erhalten). Für die Auswertung zählt r2 für alle 40 Spiele. Gründe: (1) K.-o.-/Play-off-Runden (alle Spiele mit Spieltag 0) aus Training und Tabellen ausgeschlossen, weil Verlängerung und neutraler Ort für sie nicht ausgeschlossen werden können (Abschnitt 5.2); das API-Feld no_home_away ist saisonweise uneinheitlich gesetzt und wird nicht als Kennzeichnung neutraler Plätze verwendet; (2) der in r1 eigenmächtig eingeführte Grundraten-Maßstab („Markt unbrauchbar“) ist auf Nutzeranweisung gestrichen, der Testbefund steht nur noch im Modellfeld; (3) xG-Werte 0,00 werden als beobachtete 0 übernommen; (4) Datenbasis „eingeschränkt“ nur bei konkreten Datenlücken, Umfang wird immer genannt; (5) Rohdaten-Snapshot liegt als `../rohdaten.tar.xz` bei.

- System: FootyStats-System v1.3 (Fassung v1.3-BTTS-2026-10-26)
- Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte)
- Analysestichtag / Informationsstand (Daten-Snapshot): 2026-11-02 10:09 UTC
- Eintrag erstellt: 2026-11-02 10:42:04 UTC
- Quelle: FootyStats API (api.football-data-api.com), Endpunkte `todays-matches`, `league-list`, `league-matches`; Abrufliste mit `key=[REDACTED]` in `abrufe.txt`.
- Nicht geprüft: Ausfälle, Aufstellungen, Belastung, Wetter, Trainerwechsel. AVG_2hg: fehlt (API-Definition nicht geprüft).
- Saisonwerte und letzte 6 sind aus den Einzelspielen der jeweiligen Ligasaison berechnet (nur Status `complete`, Anstoß vor dem Stichtag); letzte 6 = letzte sechs Ligaspiele dieser Saison, Wettbewerb identifiziert. xG zählen, wenn beide Werte vorhanden und ≥ 0 sind; ein API-Wert 0,00 bleibt als beobachtete 0 erhalten. K.-o.-/Play-off-Spiele (Spieltag 0) sind ausgeschlossen.

## 6.1 Zagłębie Lubin – Korona Kielce | 2026-11-02 17:00 UTC | Polen Ekstraklasa 2026/2027, Spieltag 13 | Match-ID 8550448

Analyse-ID: A-20261102-8550448-r2 · Team-IDs: 1149 / 1221 · Saison-ID: 17112 · Status beim Abruf: incomplete · Ort: Stadion Zagłębia Lubin

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-07-27 bis 2026-10-23, Gast 2026-07-25 bis 2026-10-24; letzte 6: Heim 2026-09-12–2026-10-23, Gast 2026-09-12–2026-10-24.

**Zagłębie Lubin (Heim, ID 1149)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 15 | 7 | 8 | 9
Gegentore | 15 | 4 | 11 | 10
Tore/Spiel | 1.25 | 1.17 | 1.33 | 1.50
Gegentore/Spiel | 1.25 | 0.67 | 1.83 | 1.67
xG für/Spiel | 1.50 | 1.71 | 1.28 | 1.58
xG gegen/Spiel | 1.82 | 1.41 | 2.23 | 1.90
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 5/4/3 | 4/1/1 | 1/3/2 | 3/1/2
Punkte/Spiel | 1.58 | 2.17 | 1.00 | 1.67
BTTS % | 58 % | 33 % | 83 % | 67 %
Over 2,5 % | 50 % | 33 % | 67 % | 67 %
Under 2,5 % | 50 % | 67 % | 33 % | 33 %
Clean Sheets % | 33 % | 50 % | 17 % | 17 %
Failed to Score % | 25 % | 33 % | 17 % | 17 %
BTTS-and-lose % | 17 % | 0 % | 33 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Korona Kielce (Gast, ID 1221)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 14 | 7 | 7 | 7
Gegentore | 18 | 7 | 11 | 13
Tore/Spiel | 1.17 | 1.17 | 1.17 | 1.17
Gegentore/Spiel | 1.50 | 1.17 | 1.83 | 2.17
xG für/Spiel | 1.66 | 1.67 | 1.66 | 1.80
xG gegen/Spiel | 1.49 | 1.44 | 1.54 | 1.48
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 5/3/4 | 2/3/1 | 3/0/3 | 3/0/3
Punkte/Spiel | 1.50 | 1.50 | 1.50 | 1.50
BTTS % | 58 % | 67 % | 50 % | 50 %
Over 2,5 % | 33 % | 17 % | 50 % | 50 %
Under 2,5 % | 67 % | 83 % | 50 % | 50 %
Clean Sheets % | 17 % | 17 % | 17 % | 17 %
Failed to Score % | 25 % | 17 % | 33 % | 33 %
BTTS-and-lose % | 8 % | 0 % | 17 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Zagłębie Lubin: 12.09. H GKS Katowice (1.62 PPG) 2:1 · 15.09. A Raków Częstochowa (0.50 PPG) 3:2 · 20.09. H Wisła Płock (1.25 PPG) 0:2 · 10.10. A Cracovia Kraków (0.92 PPG) 1:3 · 18.10. H Jagiellonia Białystok (1.50 PPG) 1:0 · 23.10. A Motor Lublin (1.23 PPG) 2:2

Letzte 6 Korona Kielce: 12.09. A Śląsk Wrocław (0.75 PPG) 2:1 · 15.09. H Górnik Zabrze (2.15 PPG) 0:2 · 19.09. H Raków Częstochowa (0.50 PPG) 3:2 · 11.10. A Pogoń Szczecin (2.18 PPG) 0:2 · 18.10. A Lech Poznań (2.58 PPG) 1:6 · 24.10. H GKS Katowice (1.62 PPG) 1:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Zagłębie Lubin [2, 1, 2, 0, 0, 1, 2, 3, 0, 1, 1, 2]; Korona Kielce [0, 1, 2, 1, 2, 1, 2, 0, 3, 0, 1, 1]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Zagłębie mit 1,25 Toren/Spiel, gegen Korona mit 1,49 xG gegen; ein Weg zu drei Toren ist mit 50 % bzw. 33 % Over beider Teams unklar; stärkstes Gegenargument gegen den Heimsieg (Modell 45 %) ist Koronas Auswärtsoffensive mit 1,66 xG und 3-0-3, sodass Zagłębies Heimstärke (2,17 Punkte/Spiel) nicht für eine klare Auswahl reicht.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1030 Spiele, Saisons [9553, 12120, 15031, 17112]; Schätzung λ Heim 1.431, λ Gast 1.094. Prüfstand (unberührter Test, 103 Spiele ab 2026-07-31): Heimsieg besser als Grundrate (Brier 0.2415 gegen 0.2493); Auswärtssieg besser als Grundrate (Brier 0.2054 gegen 0.211); BTTS Ja nicht besser als Grundrate (Brier 0.2396 gegen 0.2337); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2462 gegen 0.2496). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 45 % · Remis 26 % · Auswärtssieg 29 % · BTTS Ja 51 % · Over 2,5 46 % · Under 2,5 54 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.55 · X 3.35 · 2 2.75 · BTTS Ja 1.7 · Over 2,5 1.97 · Under 2,5 1.85.

**Auswahl:** keine – Grund siehe Bild.

---

## 6.2 Radomiak Radom – Śląsk Wrocław | 2026-11-02 17:00 UTC | Polen Ekstraklasa 2026/2027, Spieltag 13 | Match-ID 8550586

Analyse-ID: A-20261102-8550586-r2 · Team-IDs: 805 / 1220 · Saison-ID: 17112 · Status beim Abruf: incomplete · Ort: Stadion MOSiR ul. Narutowicza

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 12 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-07-24 bis 2026-10-24, Gast 2026-07-25 bis 2026-10-25; letzte 6: Heim 2026-09-05–2026-10-24, Gast 2026-09-06–2026-10-25.

**Radomiak Radom (Heim, ID 805)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 12 | 7 | 5 | 6
Gegentore | 28 | 10 | 18 | 15
Tore/Spiel | 1.00 | 1.17 | 0.83 | 1.00
Gegentore/Spiel | 2.33 | 1.67 | 3.00 | 2.50
xG für/Spiel | 1.54 | 1.70 | 1.38 | 1.65
xG gegen/Spiel | 1.85 | 1.83 | 1.87 | 1.81
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 2/2/8 | 2/1/3 | 0/1/5 | 0/1/5
Punkte/Spiel | 0.67 | 1.17 | 0.17 | 0.17
BTTS % | 58 % | 67 % | 50 % | 50 %
Over 2,5 % | 67 % | 67 % | 67 % | 50 %
Under 2,5 % | 33 % | 33 % | 33 % | 50 %
Clean Sheets % | 17 % | 17 % | 17 % | 17 %
Failed to Score % | 42 % | 33 % | 50 % | 50 %
BTTS-and-lose % | 42 % | 33 % | 50 % | 50 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Śląsk Wrocław (Gast, ID 1220)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 16 | 9 | 7 | 8
Gegentore | 22 | 10 | 12 | 13
Tore/Spiel | 1.33 | 1.50 | 1.17 | 1.33
Gegentore/Spiel | 1.83 | 1.67 | 2.00 | 2.17
xG für/Spiel | 1.41 | 1.54 | 1.27 | 1.30
xG gegen/Spiel | 1.98 | 1.84 | 2.12 | 2.15
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 2/3/7 | 2/2/2 | 0/1/5 | 1/0/5
Punkte/Spiel | 0.75 | 1.33 | 0.17 | 0.50
BTTS % | 83 % | 67 % | 100 % | 83 %
Over 2,5 % | 75 % | 67 % | 83 % | 83 %
Under 2,5 % | 25 % | 33 % | 17 % | 17 %
Clean Sheets % | 17 % | 33 % | 0 % | 17 %
Failed to Score % | 8 % | 17 % | 0 % | 0 %
BTTS-and-lose % | 58 % | 33 % | 83 % | 83 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Radomiak Radom: 05.09. A Widzew Łódź (0.85 PPG) 0:0 · 14.09. H Piast Gliwice (1.62 PPG) 0:2 · 20.09. A Lech Poznań (2.58 PPG) 1:5 · 12.10. H Motor Lublin (1.23 PPG) 2:3 · 19.10. A Wisła Płock (1.25 PPG) 0:1 · 24.10. A Pogoń Szczecin (2.18 PPG) 3:4

Letzte 6 Śląsk Wrocław: 06.09. A Jagiellonia Białystok (1.50 PPG) 1:2 · 12.09. H Korona Kielce (1.50 PPG) 1:2 · 18.09. A Wisła Kraków (1.62 PPG) 1:2 · 10.10. H Lech Poznań (2.58 PPG) 1:4 · 17.10. A Motor Lublin (1.23 PPG) 2:3 · 25.10. H Wieczysta Kraków (0.62 PPG) 2:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Radomiak Radom [2, 1, 1, 0, 0, 2, 0, 0, 1, 2, 0, 3]; Śląsk Wrocław [1, 2, 0, 1, 3, 1, 1, 1, 1, 1, 2, 2]

**Bild:** Saison 2026/27 mit je 12 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Radomiak mit 1,00 Toren/Spiel und 42 % torlosen Spielen, gegen Śląsk mit 1,98 xG gegen und auswärts 12 Gegentoren in 6; der Weg zu drei Toren läuft über beide schwachen Abwehrreihen (Radomiak 28, Śląsk 22 Gegentore) und notfalls einseitig, mit 83 % Over in Śląsks Auswärtsspielen und 67 % in Radomiaks Heimspielen, und das Modell schätzt 53 %; stärkstes Gegenargument ist Radomiaks Torlosigkeit in 3 der letzten 6 Spiele, die den beidseitigen Weg erschwert, Over aber nicht entkräftet.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1030 Spiele, Saisons [9553, 12120, 15031, 17112]; Schätzung λ Heim 1.534, λ Gast 1.279. Prüfstand (unberührter Test, 103 Spiele ab 2026-07-31): Heimsieg besser als Grundrate (Brier 0.2415 gegen 0.2493); Auswärtssieg besser als Grundrate (Brier 0.2054 gegen 0.211); BTTS Ja nicht besser als Grundrate (Brier 0.2396 gegen 0.2337); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2462 gegen 0.2496). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 43 % · Remis 25 % · Auswärtssieg 32 % · BTTS Ja 57 % · Over 2,5 53 % · Under 2,5 47 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.15 · X 3.4 · 2 2.82 · BTTS Ja 1.5 · Over 2,5 1.57 · Under 2,5 2.21.

**Auswahl:** Over 2,5

⚠️ Radomiak in 3 der letzten 6 Spiele torlos – dann muss Śląsk allein für Over sorgen.

---

## 6.3 Raków Częstochowa – Pogoń Szczecin | 2026-11-02 19:30 UTC | Polen Ekstraklasa 2026/2027, Spieltag 13 | Match-ID 8550577

Analyse-ID: A-20261102-8550577-r2 · Team-IDs: 802 / 1225 · Saison-ID: 17112 · Status beim Abruf: incomplete · Ort: Stadion Raków

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 12 bzw. 11 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-07-26 bis 2026-10-24, Gast 2026-07-24 bis 2026-10-24; letzte 6: Heim 2026-09-11–2026-10-24, Gast 2026-09-07–2026-10-24.

**Raków Częstochowa (Heim, ID 802)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 12 | 6 | 6 | 6
Tore | 16 | 9 | 7 | 10
Gegentore | 28 | 17 | 11 | 14
Tore/Spiel | 1.33 | 1.50 | 1.17 | 1.67
Gegentore/Spiel | 2.33 | 2.83 | 1.83 | 2.33
xG für/Spiel | 1.80 | 1.86 | 1.73 | 2.07
xG gegen/Spiel | 1.84 | 1.60 | 2.07 | 1.88
Spiele mit xG | 12 | 6 | 6 | 6
S/U/N | 2/0/10 | 1/0/5 | 1/0/5 | 2/0/4
Punkte/Spiel | 0.50 | 0.50 | 0.50 | 1.00
BTTS % | 92 % | 100 % | 83 % | 100 %
Over 2,5 % | 92 % | 100 % | 83 % | 100 %
Under 2,5 % | 8 % | 0 % | 17 % | 0 %
Clean Sheets % | 0 % | 0 % | 0 % | 0 %
Failed to Score % | 8 % | 0 % | 17 % | 0 %
BTTS-and-lose % | 75 % | 83 % | 67 % | 67 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Pogoń Szczecin (Gast, ID 1225)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 11 | 7 | 4 | 6
Tore | 19 | 14 | 5 | 12
Gegentore | 9 | 8 | 1 | 5
Tore/Spiel | 1.73 | 2.00 | 1.25 | 2.00
Gegentore/Spiel | 0.82 | 1.14 | 0.25 | 0.83
xG für/Spiel | 1.49 | 1.60 | 1.30 | 1.55
xG gegen/Spiel | 1.81 | 1.75 | 1.91 | 1.69
Spiele mit xG | 11 | 7 | 4 | 6
S/U/N | 7/3/1 | 4/2/1 | 3/1/0 | 5/1/0
Punkte/Spiel | 2.18 | 2.00 | 2.50 | 2.67
BTTS % | 45 % | 57 % | 25 % | 50 %
Over 2,5 % | 36 % | 43 % | 25 % | 33 %
Under 2,5 % | 64 % | 57 % | 75 % | 67 %
Clean Sheets % | 45 % | 29 % | 75 % | 50 %
Failed to Score % | 18 % | 14 % | 25 % | 0 %
BTTS-and-lose % | 0 % | 0 % | 0 % | 0 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Raków Częstochowa: 11.09. H Motor Lublin (1.23 PPG) 2:1 · 15.09. H Zagłębie Lubin (1.58 PPG) 2:3 · 19.09. A Korona Kielce (1.50 PPG) 2:3 · 09.10. H GKS Katowice (1.62 PPG) 1:4 · 16.10. A Wieczysta Kraków (0.62 PPG) 2:1 · 24.10. A Wisła Kraków (1.62 PPG) 1:2

Letzte 6 Pogoń Szczecin: 07.09. H Wisła Płock (1.25 PPG) 1:1 · 13.09. H Wieczysta Kraków (0.62 PPG) 2:0 · 20.09. A Piast Gliwice (1.62 PPG) 2:1 · 11.10. H Korona Kielce (1.50 PPG) 2:0 · 17.10. A GKS Katowice (1.62 PPG) 1:0 · 24.10. H Radomiak Radom (0.67 PPG) 4:3

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Raków Częstochowa [1, 1, 1, 2, 1, 0, 2, 2, 2, 1, 2, 1]; Pogoń Szczecin [0, 2, 3, 2, 0, 1, 2, 2, 2, 1, 4]

**Bild:** Saison 2026/27 mit 12 und 11 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Raków mit 1,33 Toren/Spiel, aber 1,80 xG und Tore in 11 von 12 Spielen, gegen Pogoń mit 1,81 xG gegen; der Weg zu drei Toren läuft über Raków-Spiele mit 92 % Over (daheim 100 %, 4,3 Tore/Spiel) und Pogońs Offensive mit 1,73 Toren/Spiel, das Modell schätzt 52 %; stärkstes Gegenargument ist Pogońs Under-Profil mit 36 % Over und nur 1 Auswärtsgegentor in 4 Spielen, was als wesentliche Gefahr gewichtet wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 100 (zeitlich vorwärts gewählt); Training 1030 Spiele, Saisons [9553, 12120, 15031, 17112]; Schätzung λ Heim 1.549, λ Gast 1.189. Prüfstand (unberührter Test, 103 Spiele ab 2026-07-31): Heimsieg besser als Grundrate (Brier 0.2415 gegen 0.2493); Auswärtssieg besser als Grundrate (Brier 0.2054 gegen 0.211); BTTS Ja nicht besser als Grundrate (Brier 0.2396 gegen 0.2337); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2462 gegen 0.2496). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 46 % · Remis 25 % · Auswärtssieg 29 % · BTTS Ja 55 % · Over 2,5 52 % · Under 2,5 48 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 2.1 · X 3.6 · 2 3.25 · BTTS Ja 1.53 · Over 2,5 1.55 · Under 2,5 2.33.

**Auswahl:** Over 2,5

⚠️ Pogoń-Spiele nur 36 % Over und auswärts nur 1 Gegentor in 4 Spielen.

---

## 6.4 Benfica – Alverca | 2026-11-02 20:15 UTC | Portugal Liga Portugal 2026/2027, Spieltag 10 | Match-ID 8574282

Analyse-ID: A-20261102-8574282-r2 · Team-IDs: 78 / 10708 · Saison-ID: 17217 · Status beim Abruf: incomplete · Ort: Estádio do Sport Lisboa e Benfica

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 9 bzw. 9 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-09 bis 2026-10-26, Gast 2026-08-09 bis 2026-10-24; letzte 6: Heim 2026-09-05–2026-10-26, Gast 2026-08-29–2026-10-24.

**Benfica (Heim, ID 78)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 4 | 5 | 6
Tore | 26 | 9 | 17 | 15
Gegentore | 8 | 4 | 4 | 5
Tore/Spiel | 2.89 | 2.25 | 3.40 | 2.50
Gegentore/Spiel | 0.89 | 1.00 | 0.80 | 0.83
xG für/Spiel | 2.14 | 2.55 | 1.81 | 1.84
xG gegen/Spiel | 0.88 | 0.65 | 1.06 | 1.01
Spiele mit xG | 9 | 4 | 5 | 6
S/U/N | 7/1/1 | 3/1/0 | 4/0/1 | 5/0/1
Punkte/Spiel | 2.44 | 2.50 | 2.40 | 2.50
BTTS % | 56 % | 75 % | 40 % | 50 %
Over 2,5 % | 89 % | 75 % | 100 % | 83 %
Under 2,5 % | 11 % | 25 % | 0 % | 17 %
Clean Sheets % | 44 % | 25 % | 60 % | 50 %
Failed to Score % | 0 % | 0 % | 0 % | 0 %
BTTS-and-lose % | 11 % | 0 % | 20 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**Alverca (Gast, ID 10708)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 9 | 5 | 4 | 6
Tore | 13 | 5 | 8 | 10
Gegentore | 13 | 6 | 7 | 6
Tore/Spiel | 1.44 | 1.00 | 2.00 | 1.67
Gegentore/Spiel | 1.44 | 1.20 | 1.75 | 1.00
xG für/Spiel | 1.25 | 1.19 | 1.32 | 1.21
xG gegen/Spiel | 1.41 | 1.44 | 1.39 | 1.41
Spiele mit xG | 9 | 5 | 4 | 6
S/U/N | 3/2/4 | 1/2/2 | 2/0/2 | 3/1/2
Punkte/Spiel | 1.22 | 1.00 | 1.50 | 1.67
BTTS % | 67 % | 60 % | 75 % | 67 %
Over 2,5 % | 56 % | 40 % | 75 % | 50 %
Under 2,5 % | 44 % | 60 % | 25 % | 50 %
Clean Sheets % | 11 % | 20 % | 0 % | 17 %
Failed to Score % | 22 % | 20 % | 25 % | 17 %
BTTS-and-lose % | 22 % | 20 % | 25 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 Benfica: 05.09. A CS Marítimo (0.80 PPG) 3:0 · 09.09. A Moreirense FC (1.40 PPG) 4:0 · 13.09. H Gil Vicente (1.56 PPG) 3:1 · 20.09. A Porto (3.00 PPG) 1:3 · 11.10. H Vitória Guimarães (0.89 PPG) 2:0 · 26.10. A Santa Clara (2.10 PPG) 2:1

Letzte 6 Alverca: 29.08. H Santa Clara (2.10 PPG) 1:1 · 05.09. H Sporting Braga (1.40 PPG) 1:2 · 12.09. A CD Nacional (0.70 PPG) 3:1 · 19.09. H Rio Ave FC (0.70 PPG) 1:0 · 12.10. A Famalicão (1.00 PPG) 4:1 · 24.10. H FC Arouca (2.00 PPG) 0:1

Torverteilung Saison (eigene Tore je Spiel, chronologisch): Benfica [2, 7, 2, 3, 4, 3, 1, 2, 2]; Alverca [0, 2, 1, 1, 1, 3, 1, 4, 0]

**Bild:** Saison 2026/27 mit je 9 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Alverca mit 1,44 Toren/Spiel und 1,25 xG, gegen Benficas Abwehr mit 0,88 xG gegen; der Weg zu drei Toren hängt vor allem an Benfica (26 Tore in 9) und wird nicht gewählt; stärkstes Gegenargument ist Alvercas Auswärtsbilanz mit 8 Toren in 4 Spielen, die gegen Benficas Abwehr (Heim 0,65 xG gegen) und Bilanz von 7-1-1 aber wenig wiegt, sodass der Heimsieg (Modell 81 %) getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 1 (zeitlich vorwärts gewählt); Training 1006 Spiele, Saisons [9984, 12931, 15115, 17217]; Schätzung λ Heim 2.751, λ Gast 0.664. Prüfstand (unberührter Test, 101 Spiele ab 2026-05-11): Heimsieg besser als Grundrate (Brier 0.2021 gegen 0.2415); Auswärtssieg besser als Grundrate (Brier 0.1979 gegen 0.2382); BTTS Ja besser als Grundrate (Brier 0.2456 gegen 0.2502); Over 2,5 / Under 2,5 besser als Grundrate (Brier 0.2393 gegen 0.2488). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 81 % · Remis 13 % · Auswärtssieg 6 % · BTTS Ja 45 % · Over 2,5 66 % · Under 2,5 34 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.13 · X 7.4 · 2 12 · BTTS Ja 1.91 · Over 2,5 1.32 · Under 2,5 3.4.

**Auswahl:** Heimsieg

---

## 6.5 FC Penafiel – CD Feirense | 2026-11-02 18:00 UTC | Portugal Liga Portugal 2 2026/2027, Spieltag 9 | Match-ID 8574066

Analyse-ID: A-20261102-8574066-r2 · Team-IDs: 182 / 166 · Saison-ID: 17215 · Status beim Abruf: incomplete · Ort: Estádio Municipal 25 de Abril

Datenstand: 2026-11-02 10:09 UTC; Datenbasis: verwendbar (Saison 2026/2027: 8 bzw. 8 Ligaspiele; xG für alle Spiele).

Zeitraum Saison: Heim 2026-08-08 bis 2026-10-24, Gast 2026-08-09 bis 2026-10-24; letzte 6: Heim 2026-08-23–2026-10-24, Gast 2026-08-24–2026-10-24.

**FC Penafiel (Heim, ID 182)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 18 | 7 | 11 | 16
Gegentore | 8 | 4 | 4 | 5
Tore/Spiel | 2.25 | 1.75 | 2.75 | 2.67
Gegentore/Spiel | 1.00 | 1.00 | 1.00 | 0.83
xG für/Spiel | 1.52 | 1.76 | 1.29 | 1.50
xG gegen/Spiel | 1.39 | 1.28 | 1.49 | 1.44
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 5/1/2 | 2/0/2 | 3/1/0 | 5/0/1
Punkte/Spiel | 2.00 | 1.50 | 2.50 | 2.50
BTTS % | 62 % | 50 % | 75 % | 67 %
Over 2,5 % | 75 % | 50 % | 100 % | 83 %
Under 2,5 % | 25 % | 50 % | 0 % | 17 %
Clean Sheets % | 25 % | 25 % | 25 % | 33 %
Failed to Score % | 12 % | 25 % | 0 % | 0 %
BTTS-and-lose % | 12 % | 25 % | 0 % | 17 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

**CD Feirense (Gast, ID 166)**

Kennzahl | Gesamt | Heim | Auswärts | letzte 6
--- | --- | --- | --- | ---
Spiele | 8 | 4 | 4 | 6
Tore | 2 | 1 | 1 | 2
Gegentore | 10 | 4 | 6 | 9
Tore/Spiel | 0.25 | 0.25 | 0.25 | 0.33
Gegentore/Spiel | 1.25 | 1.00 | 1.50 | 1.50
xG für/Spiel | 1.43 | 1.13 | 1.72 | 1.38
xG gegen/Spiel | 1.42 | 1.18 | 1.67 | 1.59
Spiele mit xG | 8 | 4 | 4 | 6
S/U/N | 0/2/6 | 0/2/2 | 0/0/4 | 0/1/5
Punkte/Spiel | 0.25 | 0.50 | 0.00 | 0.17
BTTS % | 25 % | 25 % | 25 % | 33 %
Over 2,5 % | 25 % | 25 % | 25 % | 33 %
Under 2,5 % | 75 % | 75 % | 75 % | 67 %
Clean Sheets % | 25 % | 50 % | 0 % | 17 %
Failed to Score % | 75 % | 75 % | 75 % | 67 %
BTTS-and-lose % | 25 % | 25 % | 25 % | 33 %
AVG_2hg | fehlt | fehlt | fehlt | fehlt

Letzte 6 FC Penafiel: 23.08. H Sporting CP II (2.33 PPG) 2:0 · 30.08. A Porto II (0.89 PPG) 3:0 · 05.09. H Associação Académica de Coimbra OAF (1.67 PPG) 4:1 · 12.09. A Felgueiras 1932 (0.78 PPG) 2:1 · 09.10. H AVS (1.33 PPG) 1:2 · 24.10. A Farense (1.67 PPG) 4:1

Letzte 6 CD Feirense: 24.08. H Porto II (0.89 PPG) 0:1 · 30.08. A AVS (1.33 PPG) 0:2 · 05.09. H Sporting CP II (2.33 PPG) 1:3 · 13.09. A GD Chaves (0.89 PPG) 0:1 · 11.10. A Farense (1.67 PPG) 1:2 · 24.10. H Benfica II (1.89 PPG) 0:0

Torverteilung Saison (eigene Tore je Spiel, chronologisch): FC Penafiel [0, 2, 2, 3, 4, 2, 1, 4]; CD Feirense [0, 0, 0, 0, 1, 0, 1, 0]

**Bild:** Saison 2026/27 mit je 8 Spielen und voller xG-Abdeckung ist verwendbar; schwächere Offensive ist Feirense mit 2 Toren in 8 Spielen trotz 1,43 xG und 75 % torlosen Spielen (auswärts 1 Tor in 4), gegen Penafiel mit 18 Toren in 8; der Weg zu drei Toren hängt allein an Penafiel und ist mit 50 % Over daheim unsicher; stärkstes Gegenargument ist das niedrige Modell-Heimsieg-Ergebnis von 43 % (geprägt von früheren Saisons, in denen Feirense stärker war) und Penafiels Heimbilanz von nur 2-0-2, während Feirense mit 0-2-6 und auswärts 0-0-4 kaum Gegengewicht hat, sodass der Heimsieg sportlich getragen wird.

**Modell:** Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte); alpha = 10 (zeitlich vorwärts gewählt); Training 998 Spiele, Saisons [9704, 12585, 15717, 17215]; Schätzung λ Heim 1.227, λ Gast 0.920. Prüfstand (unberührter Test, 100 Spiele ab 2026-05-04): Heimsieg nicht besser als Grundrate (Brier 0.2508 gegen 0.2498); Auswärtssieg nicht besser als Grundrate (Brier 0.2227 gegen 0.2211); BTTS Ja nicht besser als Grundrate (Brier 0.2589 gegen 0.2501); Over 2,5 / Under 2,5 nicht besser als Grundrate (Brier 0.2661 gegen 0.2518). Grenzen: unabhängige Poisson-Tore, keine Formgewichtung, Teams ohne Vorsaisondaten in dieser Liga werden zur Ligamitte gezogen; Modellwerte sind Schätzungen.

Modellwahrscheinlichkeiten (Schätzung): Heimsieg 43 % · Remis 29 % · Auswärtssieg 28 % · BTTS Ja 43 % · Over 2,5 36 % · Under 2,5 64 %

**Quote:** FootyStats `todays-matches`, Abruf 2026-11-02 10:07 UTC, Buchmacher nicht ausgewiesen, Aktualität nicht geprüft: 1 1.95 · X 3.25 · 2 3.85 · BTTS Ja 1.89 · Over 2,5 2.09 · Under 2,5 1.68.

**Auswahl:** Heimsieg

⚠️ Modell nur 43 % Heimsieg; Penafiel verlor 2 von 4 Heimspielen.

---
