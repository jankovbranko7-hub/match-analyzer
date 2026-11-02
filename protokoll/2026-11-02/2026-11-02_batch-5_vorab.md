# Vorabeinträge 02.11.2026 – Batch 5

System: OddAlerts-System v1.3-OA (Fassung v1.3-OA-2026-11-02). Datenquelle: Odd Alerts Data API. Rechenlauf/Entscheidungszeitpunkt: 2026-11-02 10:15 UTC; Datenabruf 2026-11-02 10:12–10:15 UTC; Eintrag erstellt 2026-11-02 10:20 UTC, vor allen Anstößen. Abfrageparameter ohne API-Schlüssel: `abrufe-2026-11-02.jsonl`; Rohdaten-Snapshot: `rohdaten-2026-11-02.tar.gz`; Modellprüfung je Wettbewerb: `modellpruefung-2026-11-02.json`. Dieser Eintrag wird nicht mehr verändert.

## Batch 5 · Nr. 1 – Analyse-ID OA-20261102-B5-1

**[Atalanta – Parma | 2026-11-02 19:45 UTC | Italy Serie A 2026/2027 (Wettbewerb-ID 499, Saison-ID 2224807, Saisonfortschritt 23 %) | Match-ID 420669107]**

Nutzerangabe: Atalanta vs Parma. Team-IDs: Heim 11513, Gast 10126. Status beim Abruf: NS; Spielort: Gewiss Stadium, Bergamo, Bergamo, Italy; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 13 bzw. 18.

Datenstand: 2026-11-02 10:15 UTC; Datenbasis: verwendbar (je 9 Ligaspiele, xG für alle Spiele).

**Atalanta** (Team-ID 11513) – Saison 2026/2027, nur Serie A (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 9 | 5 | 4 | 6 |
| Tore | 16 | 11 | 5 | 14 |
| Gegentore | 17 | 8 | 9 | 13 |
| Tore/Spiel | 1,78 | 2,20 | 1,25 | 2,33 |
| Gegentore/Spiel | 1,89 | 1,60 | 2,25 | 2,17 |
| xG für/Spiel | 1,46 | 1,82 | 1,02 | 2,22¹ |
| xG gegen/Spiel | 2,01 | 1,75 | 2,33 | 1,92¹ |
| Spiele mit xG | 9 von 9 | 5 von 5 | 4 von 4 | 6 von 6¹ |
| S/U/N | 3/2/4 | 3/1/1 | 0/1/3 | 2/2/2 |
| Punkte/Spiel | 1,22 | 2,00 | 0,25 | 1,33 |
| BTTS % | 77,8 % | 80,0 % | 75,0 % | 83,3 % |
| Over 2,5 % | 77,8 % | 80,0 % | 75,0 % | 83,3 % |
| Under 2,5 % | 22,2 % | 20,0 % | 25,0 % | 16,7 % |
| Clean Sheets % | 11,1 % | 20,0 % | 0,0 % | 0,0 % |
| Failed to Score % | 11,1 % | 0,0 % | 25,0 % | 16,7 % |
| BTTS-and-lose | 3 von 9 (33,3 %)² | 1 von 5 (20,0 %)² | 2 von 4 (50,0 %)² | 1 von 6 (16,7 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,89 | 1,40 | 2,50 | 2,00³ (6 Sp.) |
| goals_for_2h/Spiel | 0,78 | 0,60 | 1,00 | fehlt |
| goals_against_2h/Spiel | 1,11 | 0,80 | 1,50 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-10-12 H Venezia 3-1 [Serie A]; 2026-10-15 H Pafos FC 3-1 [Europa Conference League]; 2026-10-18 A AC Milan 3-2 [Serie A]; 2026-10-22 A Ajax 2-0 [Europa Conference League]; 2026-10-25 H Frosinone 4-4 [Serie A]; 2026-10-29 A Fiorentina 2-2 [Serie A]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**Parma** (Team-ID 10126) – Saison 2026/2027, nur Serie A (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 9 | 5 | 4 | 6 |
| Tore | 5 | 3 | 2 | 4 |
| Gegentore | 15 | 6 | 9 | 11 |
| Tore/Spiel | 0,56 | 0,60 | 0,50 | 0,67 |
| Gegentore/Spiel | 1,67 | 1,20 | 2,25 | 1,83 |
| xG für/Spiel | 0,95 | 1,12 | 0,74 | 1,06¹ |
| xG gegen/Spiel | 1,64 | 1,19 | 2,22 | 1,76¹ |
| Spiele mit xG | 9 von 9 | 5 von 5 | 4 von 4 | 6 von 6¹ |
| S/U/N | 1/2/6 | 1/2/2 | 0/0/4 | 1/1/4 |
| Punkte/Spiel | 0,56 | 1,00 | 0,00 | 0,67 |
| BTTS % | 44,4 % | 40,0 % | 50,0 % | 50,0 % |
| Over 2,5 % | 55,6 % | 40,0 % | 75,0 % | 83,3 % |
| Under 2,5 % | 44,4 % | 60,0 % | 25,0 % | 16,7 % |
| Clean Sheets % | 11,1 % | 20,0 % | 0,0 % | 16,7 % |
| Failed to Score % | 55,6 % | 60,0 % | 50,0 % | 50,0 % |
| BTTS-and-lose | 2 von 9 (22,2 %)² | 0 von 5 (0,0 %)² | 2 von 4 (50,0 %)² | 2 von 6 (33,3 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,33 | 1,00 | 1,75 | 1,33³ (6 Sp.) |
| goals_for_2h/Spiel | 0,44 | 0,40 | 0,50 | fehlt |
| goals_against_2h/Spiel | 0,89 | 0,60 | 1,25 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-14 A Como 2-1 [Serie A]; 2026-09-20 H Genoa 2-1 [Serie A]; 2026-10-10 A Inter 3-0 [Serie A]; 2026-10-19 H Torino 0-3 [Serie A]; 2026-10-24 A Lazio 2-1 [Serie A]; 2026-10-28 H Udinese 0-0 [Serie A]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

Bild: Datenbasis verwendbar mit vollständiger xG-Abdeckung bei 9 Ligaspielen, die letzten 6 von Atalanta enthalten Europapokalspiele; schwächere Offensive ist Parma mit 0,50 Toren pro Auswärtsspiel, 0,74 xG und null Auswärtspunkten; ein Weg zu drei Toren besteht über Atalantas offensive Heimspiele (2,20 Tore, 80 % Over), ist für den Heimsieg aber nicht nötig; stärkstes Gegenargument ist Atalantas Abwehr mit 1,89 Gegentoren und 2,01 xG gegen pro Spiel sowie zwei Remis in den letzten 6 (4:4, 2:2), was gegen Parmas schwächste Offensive aber geringer wiegt als Atalantas Heimstärke (Modell 64 %).

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Serie A (Italy), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 1238 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-02 10:15 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 10 zeitlich vorwärts gewählt (Training 742 Spiele bis 2025-05-18, Auswahl auf 248 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 248 jüngsten Spielen (2026-02-06 bis 2026-11-01, 248 bewertbar): Heimsieg Brier 0,212 gegen Grundrate 0,246 (besser), Log-Loss 0,612; Auswärtssieg Brier 0,198 gegen Grundrate 0,236 (besser), Log-Loss 0,579; BTTS Ja Brier 0,246 gegen Grundrate 0,250 (besser), Log-Loss 0,686; Over 2,5 Brier 0,255 gegen Grundrate 0,252 (nicht besser), Log-Loss 0,703. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,92, λ Gast 0,79; Heimsieg 64 %, Remis 21 %, Auswärtssieg 15 %, BTTS Ja 47 %, Over 2,5 51 %, Under 2,5 49 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-02 10:12 UTC): Heimsieg 1.54; Auswärtssieg 5.99; BTTS Ja fehlt; Over 2,5 1.60; Under 2,5 2.45. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: Heimsieg**

---

## Batch 5 · Nr. 2 – Analyse-ID OA-20261102-B5-2

**[Heracles Almelo – TOP Oss | 2026-11-02 19:00 UTC | Netherlands Eerste Divisie 2026/2027 (Wettbewerb-ID 175, Saison-ID 2254098, Saisonfortschritt 33 %) | Match-ID 420609314]**

Nutzerangabe: Heracles Almelo vs TOP Oss. Team-IDs: Heim 3993, Gast 7492. Status beim Abruf: NS; Spielort: Asito Stadion, Stadionlaan 1, Almelo, Netherlands; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 1 bzw. 15.

Datenstand: 2026-11-02 10:15 UTC; Datenbasis: verwendbar (je 12 Ligaspiele, xG für alle Spiele).

**Heracles Almelo** (Team-ID 3993) – Saison 2026/2027, nur Eerste Divisie (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 12 | 5 | 7 | 6 |
| Tore | 37 | 16 | 21 | 13 |
| Gegentore | 14 | 4 | 10 | 5 |
| Tore/Spiel | 3,08 | 3,20 | 3,00 | 2,17 |
| Gegentore/Spiel | 1,17 | 0,80 | 1,43 | 0,83 |
| xG für/Spiel | 2,64 | 2,69 | 2,60 | 2,22¹ |
| xG gegen/Spiel | 1,01 | 0,85 | 1,13 | 1,12¹ |
| Spiele mit xG | 12 von 12 | 5 von 5 | 7 von 7 | 5 von 6¹ |
| S/U/N | 9/2/1 | 5/0/0 | 4/2/1 | 3/2/1 |
| Punkte/Spiel | 2,42 | 3,00 | 2,00 | 1,83 |
| BTTS % | 66,7 % | 40,0 % | 85,7 % | 50,0 % |
| Over 2,5 % | 75,0 % | 80,0 % | 71,4 % | 50,0 % |
| Under 2,5 % | 25,0 % | 20,0 % | 28,6 % | 50,0 % |
| Clean Sheets % | 25,0 % | 60,0 % | 0,0 % | 33,3 % |
| Failed to Score % | 8,3 % | 0,0 % | 14,3 % | 16,7 % |
| BTTS-and-lose | 0 von 12 (0,0 %)² | 0 von 5 (0,0 %)² | 0 von 7 (0,0 %)² | 0 von 6 (0,0 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 2,25 | 2,40 | 2,14 | 1,33³ (6 Sp.) |
| goals_for_2h/Spiel | 1,50 | 2,00 | 1,14 | fehlt |
| goals_against_2h/Spiel | 0,75 | 0,40 | 1,00 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-26 H Vitesse 2-0 [Eerste Divisie]; 2026-10-02 A Helmond Sport 2-2 [Eerste Divisie]; 2026-10-09 H RKC Waalwijk 3-0 [Eerste Divisie]; 2026-10-18 A MVV Maastricht 1-5 [Eerste Divisie]; 2026-10-23 A NAC Breda 1-1 [Eerste Divisie]; 2026-10-29 A De Treffers 1-0 [KNVB Beker]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**TOP Oss** (Team-ID 7492) – Saison 2026/2027, nur Eerste Divisie (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 12 | 6 | 6 | 6 |
| Tore | 19 | 16 | 3 | 13 |
| Gegentore | 20 | 8 | 12 | 9 |
| Tore/Spiel | 1,58 | 2,67 | 0,50 | 2,17 |
| Gegentore/Spiel | 1,67 | 1,33 | 2,00 | 1,50 |
| xG für/Spiel | 1,62 | 1,89 | 1,34 | 1,86¹ |
| xG gegen/Spiel | 1,82 | 1,73 | 1,92 | 1,65¹ |
| Spiele mit xG | 12 von 12 | 6 von 6 | 6 von 6 | 5 von 6¹ |
| S/U/N | 4/1/7 | 4/1/1 | 0/0/6 | 3/1/2 |
| Punkte/Spiel | 1,08 | 2,17 | 0,00 | 1,67 |
| BTTS % | 66,7 % | 83,3 % | 50,0 % | 83,3 % |
| Over 2,5 % | 83,3 % | 100,0 % | 66,7 % | 83,3 % |
| Under 2,5 % | 16,7 % | 0,0 % | 33,3 % | 16,7 % |
| Clean Sheets % | 8,3 % | 16,7 % | 0,0 % | 0,0 % |
| Failed to Score % | 25,0 % | 0,0 % | 50,0 % | 16,7 % |
| BTTS-and-lose | 4 von 12 (33,3 %)² | 1 von 6 (16,7 %)² | 3 von 6 (50,0 %)² | 1 von 6 (16,7 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,67 | 2,17 | 1,17 | 1,67³ (6 Sp.) |
| goals_for_2h/Spiel | 0,92 | 1,50 | 0,33 | fehlt |
| goals_against_2h/Spiel | 0,75 | 0,67 | 0,83 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-26 A FC Emmen 1-0 [Eerste Divisie]; 2026-10-03 H MVV Maastricht 4-1 [Eerste Divisie]; 2026-10-09 H Helmond Sport 3-1 [Eerste Divisie]; 2026-10-16 A FC Den Bosch 2-1 [Eerste Divisie]; 2026-10-23 H Jong Ajax 3-3 [Eerste Divisie]; 2026-10-28 A PEC Zwolle 1-2 [KNVB Beker]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

Bild: Datenbasis verwendbar mit je 12 Ligaspielen und vollständiger xG-Abdeckung; schwächere Offensive ist TOP Oss mit 0,50 Toren pro Auswärtsspiel, 50 % torlosen Auswärtsspielen und null Auswärtspunkten gegen Heracles' Heimabwehr mit 0,80 Gegentoren und 0,85 xG gegen; ein Weg zu drei Toren besteht über Heracles allein (3,20 Tore pro Heimspiel), ist für den Heimsieg aber nicht nötig; stärkstes Gegenargument ist TOP Oss' Form mit 13 Toren in den letzten 6, die aber überwiegend zu Hause fielen und gegen Heracles' 5 Heimsiege aus 5 gering gewichtet wird.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Eerste Divisie (Netherlands), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 1265 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-02 10:15 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 100 zeitlich vorwärts gewählt (Training 759 Spiele bis 2025-05-09, Auswahl auf 253 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 253 jüngsten Spielen (2026-02-09 bis 2026-11-01, 241 bewertbar): Heimsieg Brier 0,238 gegen Grundrate 0,249 (besser), Log-Loss 0,670; Auswärtssieg Brier 0,217 gegen Grundrate 0,222 (besser), Log-Loss 0,624; BTTS Ja Brier 0,232 gegen Grundrate 0,234 (besser), Log-Loss 0,656; Over 2,5 Brier 0,237 gegen Grundrate 0,233 (nicht besser), Log-Loss 0,667. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,95, λ Gast 1,16; Heimsieg 56 %, Remis 22 %, Auswärtssieg 22 %, BTTS Ja 59 %, Over 2,5 60 %, Under 2,5 40 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-02 10:12 UTC): Heimsieg 1.17; Auswärtssieg 12.12; BTTS Ja fehlt; Over 2,5 1.26; Under 2,5 3.73. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: Heimsieg**

---

## Batch 5 · Nr. 3 – Analyse-ID OA-20261102-B5-3

**[Jong PSV – NAC Breda | 2026-11-02 19:00 UTC | Netherlands Eerste Divisie 2026/2027 (Wettbewerb-ID 175, Saison-ID 2254098, Saisonfortschritt 33 %) | Match-ID 420609416]**

Nutzerangabe: Jong PSV vs NAC Breda. Team-IDs: Heim 6917, Gast 5111. Status beim Abruf: NS; Spielort: Sportcomplex De Herdgang, Oirschotsedijk 12, Eindhoven, Netherlands; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 13 bzw. 6.

Datenstand: 2026-11-02 10:15 UTC; Datenbasis: verwendbar (je 12 Ligaspiele, xG für alle Spiele).

**Jong PSV** (Team-ID 6917) – Saison 2026/2027, nur Eerste Divisie (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 12 | 6 | 6 | 6 |
| Tore | 17 | 9 | 8 | 6 |
| Gegentore | 19 | 6 | 13 | 10 |
| Tore/Spiel | 1,42 | 1,50 | 1,33 | 1,00 |
| Gegentore/Spiel | 1,58 | 1,00 | 2,17 | 1,67 |
| xG für/Spiel | 1,52 | 1,57 | 1,48 | 1,18¹ |
| xG gegen/Spiel | 1,65 | 1,54 | 1,75 | 2,03¹ |
| Spiele mit xG | 12 von 12 | 6 von 6 | 6 von 6 | 6 von 6¹ |
| S/U/N | 4/4/4 | 3/2/1 | 1/2/3 | 1/2/3 |
| Punkte/Spiel | 1,33 | 1,83 | 0,83 | 0,83 |
| BTTS % | 83,3 % | 66,7 % | 100,0 % | 83,3 % |
| Over 2,5 % | 58,3 % | 33,3 % | 83,3 % | 50,0 % |
| Under 2,5 % | 41,7 % | 66,7 % | 16,7 % | 50,0 % |
| Clean Sheets % | 8,3 % | 16,7 % | 0,0 % | 0,0 % |
| Failed to Score % | 8,3 % | 16,7 % | 0,0 % | 16,7 % |
| BTTS-and-lose | 3 von 12 (25,0 %)² | 0 von 6 (0,0 %)² | 3 von 6 (50,0 %)² | 2 von 6 (33,3 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,58 | 1,50 | 1,67 | 1,33³ (6 Sp.) |
| goals_for_2h/Spiel | 0,75 | 1,00 | 0,50 | fehlt |
| goals_against_2h/Spiel | 0,83 | 0,50 | 1,17 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-11 A Helmond Sport 3-1 [Eerste Divisie]; 2026-09-14 H Jong AZ 1-1 [Eerste Divisie]; 2026-09-19 A Vitesse 3-1 [Eerste Divisie]; 2026-10-09 A Roda JC Kerkrade 1-1 [Eerste Divisie]; 2026-10-19 H FC Dordrecht 0-1 [Eerste Divisie]; 2026-10-23 A FC Eindhoven 1-2 [Eerste Divisie]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**NAC Breda** (Team-ID 5111) – Saison 2026/2027, nur Eerste Divisie (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 12 | 6 | 6 | 6 |
| Tore | 23 | 11 | 12 | 13 |
| Gegentore | 20 | 10 | 10 | 6 |
| Tore/Spiel | 1,92 | 1,83 | 2,00 | 2,17 |
| Gegentore/Spiel | 1,67 | 1,67 | 1,67 | 1,00 |
| xG für/Spiel | 1,85 | 1,76 | 1,94 | 1,59¹ |
| xG gegen/Spiel | 1,22 | 0,80 | 1,65 | 0,84¹ |
| Spiele mit xG | 12 von 12 | 6 von 6 | 6 von 6 | 5 von 6¹ |
| S/U/N | 6/3/3 | 3/1/2 | 3/2/1 | 4/2/0 |
| Punkte/Spiel | 1,75 | 1,67 | 1,83 | 2,33 |
| BTTS % | 75,0 % | 66,7 % | 83,3 % | 66,7 % |
| Over 2,5 % | 66,7 % | 50,0 % | 83,3 % | 50,0 % |
| Under 2,5 % | 33,3 % | 50,0 % | 16,7 % | 50,0 % |
| Clean Sheets % | 16,7 % | 16,7 % | 16,7 % | 33,3 % |
| Failed to Score % | 8,3 % | 16,7 % | 0,0 % | 0,0 % |
| BTTS-and-lose | 2 von 12 (16,7 %)² | 1 von 6 (16,7 %)² | 1 von 6 (16,7 %)² | 0 von 6 (0,0 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,92 | 2,00 | 1,83 | 1,33³ (6 Sp.) |
| goals_for_2h/Spiel | 0,92 | 0,83 | 1,00 | fehlt |
| goals_against_2h/Spiel | 1,00 | 1,17 | 0,83 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-26 H FC Eindhoven 4-2 [Eerste Divisie]; 2026-10-03 A Vitesse 2-2 [Eerste Divisie]; 2026-10-09 H MVV Maastricht 1-0 [Eerste Divisie]; 2026-10-16 A Helmond Sport 0-2 [Eerste Divisie]; 2026-10-23 H Heracles Almelo 1-1 [Eerste Divisie]; 2026-10-28 A JOS Watergraafsmeer 1-3 [KNVB Beker]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

Bild: Datenbasis verwendbar mit je 12 Ligaspielen und vollständiger xG-Abdeckung; schwächere Offensive ist Jong PSV mit 1,50 Toren pro Heimspiel bei 1,57 xG und nur einem torlosen Heimspiel von 6 (17 %), NAC trifft auswärts 2,00-mal bei 1,94 xG und blieb auswärts nie ohne Tor, beide Torargumente sind also eigenständig, und auch die Verteilung zeigt keine Abhängigkeit von einzelnen hohen Siegen; ein Weg zu drei Toren ist über beide Teams plausibel (NAC auswärts 83 % Over), für BTTS aber nicht nötig; stärkstes Gegenargument ist NACs Defensivform mit nur 0,84 xG gegen in den letzten 6 und 2 Spielen ohne Gegentor, die Jong PSVs benötigten Treffer konkret gefährdet und mit Warnung gewichtet wird.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Eerste Divisie (Netherlands), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 1265 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-02 10:15 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 100 zeitlich vorwärts gewählt (Training 759 Spiele bis 2025-05-09, Auswahl auf 253 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 253 jüngsten Spielen (2026-02-09 bis 2026-11-01, 241 bewertbar): Heimsieg Brier 0,238 gegen Grundrate 0,249 (besser), Log-Loss 0,670; Auswärtssieg Brier 0,217 gegen Grundrate 0,222 (besser), Log-Loss 0,624; BTTS Ja Brier 0,232 gegen Grundrate 0,234 (besser), Log-Loss 0,656; Over 2,5 Brier 0,237 gegen Grundrate 0,233 (nicht besser), Log-Loss 0,667. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,74, λ Gast 1,64; Heimsieg 41 %, Remis 23 %, Auswärtssieg 37 %, BTTS Ja 66 %, Over 2,5 66 %, Under 2,5 34 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-02 10:12 UTC): Heimsieg 4.94; Auswärtssieg 1.57; BTTS Ja fehlt; Over 2,5 1.37; Under 2,5 3.07. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: BTTS Ja**

⚠️ NAC Breda ließ in den letzten 6 Spielen nur 0,84 xG pro Spiel zu und spielte zweimal zu null; das gefährdet unmittelbar den benötigten Treffer von Jong PSV.

---

## Batch 5 · Nr. 4 – Analyse-ID OA-20261102-B5-4

**[Jong Ajax – Vitesse | 2026-11-02 19:00 UTC | Netherlands Eerste Divisie 2026/2027 (Wettbewerb-ID 175, Saison-ID 2254098, Saisonfortschritt 33 %) | Match-ID 420609598]**

Nutzerangabe: Jong Ajax vs Vitesse. Team-IDs: Heim 8118, Gast 5577. Status beim Abruf: NS; Spielort: Sportpark De Toekomst, Borchlandweg 16-18, Zuidoost, Amsterdam, Netherlands; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 17 bzw. 10.

Datenstand: 2026-11-02 10:15 UTC; Datenbasis: verwendbar (je 12 Ligaspiele, xG für alle Spiele).

**Jong Ajax** (Team-ID 8118) – Saison 2026/2027, nur Eerste Divisie (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 12 | 6 | 6 | 6 |
| Tore | 18 | 9 | 9 | 6 |
| Gegentore | 29 | 14 | 15 | 15 |
| Tore/Spiel | 1,50 | 1,50 | 1,50 | 1,00 |
| Gegentore/Spiel | 2,42 | 2,33 | 2,50 | 2,50 |
| xG für/Spiel | 1,62 | 1,55 | 1,70 | 1,83¹ |
| xG gegen/Spiel | 1,79 | 1,61 | 1,96 | 1,47¹ |
| Spiele mit xG | 12 von 12 | 6 von 6 | 6 von 6 | 6 von 6¹ |
| S/U/N | 3/3/6 | 2/1/3 | 1/2/3 | 1/2/3 |
| Punkte/Spiel | 1,00 | 1,17 | 0,83 | 0,83 |
| BTTS % | 66,7 % | 50,0 % | 83,3 % | 50,0 % |
| Over 2,5 % | 66,7 % | 66,7 % | 66,7 % | 66,7 % |
| Under 2,5 % | 33,3 % | 33,3 % | 33,3 % | 33,3 % |
| Clean Sheets % | 16,7 % | 16,7 % | 16,7 % | 16,7 % |
| Failed to Score % | 25,0 % | 50,0 % | 0,0 % | 50,0 % |
| BTTS-and-lose | 4 von 12 (33,3 %)² | 1 von 6 (16,7 %)² | 3 von 6 (50,0 %)² | 1 von 6 (16,7 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 2,08 | 1,83 | 2,33 | 2,17³ (6 Sp.) |
| goals_for_2h/Spiel | 0,67 | 0,50 | 0,83 | fehlt |
| goals_against_2h/Spiel | 1,42 | 1,33 | 1,50 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-11 H RKC Waalwijk 0-2 [Eerste Divisie]; 2026-09-14 A Jong FC Utrecht 6-1 [Eerste Divisie]; 2026-09-18 H Roda JC Kerkrade 0-0 [Eerste Divisie]; 2026-10-09 H VVV-Venlo 0-3 [Eerste Divisie]; 2026-10-19 H De Graafschap 2-1 [Eerste Divisie]; 2026-10-23 A TOP Oss 3-3 [Eerste Divisie]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**Vitesse** (Team-ID 5577) – Saison 2026/2027, nur Eerste Divisie (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 12 | 6 | 6 | 6 |
| Tore | 16 | 8 | 8 | 5 |
| Gegentore | 17 | 10 | 7 | 8 |
| Tore/Spiel | 1,33 | 1,33 | 1,33 | 0,83 |
| Gegentore/Spiel | 1,42 | 1,67 | 1,17 | 1,33 |
| xG für/Spiel | 1,78 | 2,02 | 1,54 | 1,03¹ |
| xG gegen/Spiel | 1,52 | 1,43 | 1,62 | 1,86¹ |
| Spiele mit xG | 12 von 12 | 6 von 6 | 6 von 6 | 5 von 6¹ |
| S/U/N | 5/2/5 | 2/2/2 | 3/0/3 | 2/1/3 |
| Punkte/Spiel | 1,42 | 1,33 | 1,50 | 1,17 |
| BTTS % | 50,0 % | 66,7 % | 33,3 % | 16,7 % |
| Over 2,5 % | 50,0 % | 66,7 % | 33,3 % | 16,7 % |
| Under 2,5 % | 50,0 % | 33,3 % | 66,7 % | 83,3 % |
| Clean Sheets % | 8,3 % | 0,0 % | 16,7 % | 33,3 % |
| Failed to Score % | 41,7 % | 33,3 % | 50,0 % | 50,0 % |
| BTTS-and-lose | 0 von 12 (0,0 %)² | 0 von 6 (0,0 %)² | 0 von 6 (0,0 %)² | 0 von 6 (0,0 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,42 | 2,00 | 0,83 | 0,67³ (6 Sp.) |
| goals_for_2h/Spiel | 0,67 | 0,83 | 0,50 | fehlt |
| goals_against_2h/Spiel | 0,75 | 1,17 | 0,33 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-26 A Heracles Almelo 2-0 [Eerste Divisie]; 2026-10-03 H NAC Breda 2-2 [Eerste Divisie]; 2026-10-09 A FC Volendam 2-0 [Eerste Divisie]; 2026-10-16 A FC Eindhoven 0-1 [Eerste Divisie]; 2026-10-23 H FC Emmen 0-2 [Eerste Divisie]; 2026-10-28 A VVV-Venlo 0-2 [KNVB Beker]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

Bild: Datenbasis verwendbar mit je 12 Ligaspielen und vollständiger xG-Abdeckung; schwächere Offensive ist Vitesse mit 1,33 Toren pro Auswärtsspiel, aber 50 % torlosen Auswärtsspielen und nur 17 % BTTS in den letzten 6 (1,03 xG); ein Weg zu drei Toren besteht über Jong Ajax' offene Heimspiele (2,33 Gegentore, 67 % Over), Vitesse-Auswärtsspiele hatten aber nur zu 33 % Over; stärkstes Gegenargument gegen die hohen Modellwerte für BTTS und Over (62 % bzw 59 %) sind die wechselnde Torausbeute beider Teams (beide 50 % ohne Tor an ihrem Spielort), sodass kein Markt klar getragen wird.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Eerste Divisie (Netherlands), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 1265 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-02 10:15 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 100 zeitlich vorwärts gewählt (Training 759 Spiele bis 2025-05-09, Auswahl auf 253 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 253 jüngsten Spielen (2026-02-09 bis 2026-11-01, 241 bewertbar): Heimsieg Brier 0,238 gegen Grundrate 0,249 (besser), Log-Loss 0,670; Auswärtssieg Brier 0,217 gegen Grundrate 0,222 (besser), Log-Loss 0,624; BTTS Ja Brier 0,232 gegen Grundrate 0,234 (besser), Log-Loss 0,656; Over 2,5 Brier 0,237 gegen Grundrate 0,233 (nicht besser), Log-Loss 0,667. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,60, λ Gast 1,47; Heimsieg 41 %, Remis 24 %, Auswärtssieg 35 %, BTTS Ja 62 %, Over 2,5 59 %, Under 2,5 41 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-02 10:12 UTC): Heimsieg 2.84; Auswärtssieg 2.23; BTTS Ja fehlt; Over 2,5 1.37; Under 2,5 3.08. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: keine – beide Teams blieben an ihrem Spielort in 50 % der Spiele ohne Tor, kein Markt klar getragen**

---

## Batch 5 · Nr. 5 – Analyse-ID OA-20261102-B5-5

**[Jong FC Utrecht – FC Dordrecht | 2026-11-02 19:00 UTC | Netherlands Eerste Divisie 2026/2027 (Wettbewerb-ID 175, Saison-ID 2254098, Saisonfortschritt 33 %) | Match-ID 420609600]**

Nutzerangabe: Jong FC Utrecht vs FC Dordrecht. Team-IDs: Heim 5601, Gast 8441. Status beim Abruf: NS; Spielort: Sportcomplex Zoudenbalch, Utrecht, Netherlands; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 20 bzw. 19.

Datenstand: 2026-11-02 10:15 UTC; Datenbasis: verwendbar (je 12 Ligaspiele, xG für alle Spiele).

**Jong FC Utrecht** (Team-ID 5601) – Saison 2026/2027, nur Eerste Divisie (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 12 | 6 | 6 | 6 |
| Tore | 19 | 10 | 9 | 14 |
| Gegentore | 31 | 15 | 16 | 16 |
| Tore/Spiel | 1,58 | 1,67 | 1,50 | 2,33 |
| Gegentore/Spiel | 2,58 | 2,50 | 2,67 | 2,67 |
| xG für/Spiel | 1,36 | 1,26 | 1,45 | 1,54¹ |
| xG gegen/Spiel | 2,02 | 2,01 | 2,04 | 2,17¹ |
| Spiele mit xG | 12 von 12 | 6 von 6 | 6 von 6 | 6 von 6¹ |
| S/U/N | 2/1/9 | 1/1/4 | 1/0/5 | 2/0/4 |
| Punkte/Spiel | 0,58 | 0,67 | 0,50 | 1,00 |
| BTTS % | 91,7 % | 83,3 % | 100,0 % | 100,0 % |
| Over 2,5 % | 91,7 % | 83,3 % | 100,0 % | 100,0 % |
| Under 2,5 % | 8,3 % | 16,7 % | 0,0 % | 0,0 % |
| Clean Sheets % | 8,3 % | 16,7 % | 0,0 % | 0,0 % |
| Failed to Score % | 8,3 % | 16,7 % | 0,0 % | 0,0 % |
| BTTS-and-lose | 9 von 12 (75,0 %)² | 4 von 6 (66,7 %)² | 5 von 6 (83,3 %)² | 4 von 6 (66,7 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,92 | 1,83 | 2,00 | 2,50³ (6 Sp.) |
| goals_for_2h/Spiel | 0,67 | 0,67 | 0,67 | fehlt |
| goals_against_2h/Spiel | 1,25 | 1,17 | 1,33 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-11 A NAC Breda 2-3 [Eerste Divisie]; 2026-09-14 H Jong Ajax 6-1 [Eerste Divisie]; 2026-09-18 H VVV-Venlo 1-3 [Eerste Divisie]; 2026-10-09 A De Graafschap 2-1 [Eerste Divisie]; 2026-10-19 H Roda JC Kerkrade 1-2 [Eerste Divisie]; 2026-10-23 A FC Volendam 6-2 [Eerste Divisie]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**FC Dordrecht** (Team-ID 8441) – Saison 2026/2027, nur Eerste Divisie (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 12 | 6 | 6 | 6 |
| Tore | 16 | 10 | 6 | 9 |
| Gegentore | 31 | 17 | 14 | 13 |
| Tore/Spiel | 1,33 | 1,67 | 1,00 | 1,50 |
| Gegentore/Spiel | 2,58 | 2,83 | 2,33 | 2,17 |
| xG für/Spiel | 1,19 | 1,04 | 1,35 | 1,12¹ |
| xG gegen/Spiel | 1,69 | 1,50 | 1,88 | 1,28¹ |
| Spiele mit xG | 12 von 12 | 6 von 6 | 6 von 6 | 5 von 6¹ |
| S/U/N | 3/2/7 | 2/0/4 | 1/2/3 | 2/1/3 |
| Punkte/Spiel | 0,92 | 1,00 | 0,83 | 1,17 |
| BTTS % | 66,7 % | 66,7 % | 66,7 % | 66,7 % |
| Over 2,5 % | 75,0 % | 83,3 % | 66,7 % | 66,7 % |
| Under 2,5 % | 25,0 % | 16,7 % | 33,3 % | 33,3 % |
| Clean Sheets % | 8,3 % | 0,0 % | 16,7 % | 16,7 % |
| Failed to Score % | 25,0 % | 33,3 % | 16,7 % | 16,7 % |
| BTTS-and-lose | 4 von 12 (33,3 %)² | 2 von 6 (33,3 %)² | 2 von 6 (33,3 %)² | 2 von 6 (33,3 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,75 | 1,83 | 1,67 | 2,00³ (6 Sp.) |
| goals_for_2h/Spiel | 0,58 | 0,83 | 0,33 | fehlt |
| goals_against_2h/Spiel | 1,17 | 1,00 | 1,33 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-25 H Almere City 3-2 [Eerste Divisie]; 2026-10-03 A FC Den Bosch 1-1 [Eerste Divisie]; 2026-10-09 H FC Emmen 0-3 [Eerste Divisie]; 2026-10-19 A Jong PSV 0-1 [Eerste Divisie]; 2026-10-24 H VVV-Venlo 2-4 [Eerste Divisie]; 2026-10-28 A Genemuiden 3-2 [KNVB Beker]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

Bild: Datenbasis verwendbar mit je 12 Ligaspielen und vollständiger xG-Abdeckung; schwächere Offensive ist Dordrecht mit 1,00 Tor pro Auswärtsspiel bei 1,35 xG gegen Jong Utrechts Heimabwehr mit 2,50 Gegentoren und 2,01 xG gegen; der Weg zu drei Toren ist doppelt begründet, weil beide Abwehren mehr als 2,3 Gegentore an ihrem Spielort zulassen und Jong-Utrecht-Spiele zu 92 %, Dordrecht-Spiele zu 75 % drei oder mehr Tore hatten, notfalls auch einseitig über Jong Utrecht; stärkstes Gegenargument ist Dordrechts mäßige Auswärtsoffensive und Jong Utrechts niedrige Heim-xG von 1,26, die aber gegen zwei sehr anfällige Abwehren (beide 2,58 Gegentore pro Spiel) gering gewichtet werden.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Eerste Divisie (Netherlands), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 1265 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-02 10:15 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 100 zeitlich vorwärts gewählt (Training 759 Spiele bis 2025-05-09, Auswahl auf 253 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 253 jüngsten Spielen (2026-02-09 bis 2026-11-01, 241 bewertbar): Heimsieg Brier 0,238 gegen Grundrate 0,249 (besser), Log-Loss 0,670; Auswärtssieg Brier 0,217 gegen Grundrate 0,222 (besser), Log-Loss 0,624; BTTS Ja Brier 0,232 gegen Grundrate 0,234 (besser), Log-Loss 0,656; Over 2,5 Brier 0,237 gegen Grundrate 0,233 (nicht besser), Log-Loss 0,667. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,45, λ Gast 1,61; Heimsieg 34 %, Remis 24 %, Auswärtssieg 42 %, BTTS Ja 61 %, Over 2,5 59 %, Under 2,5 41 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-02 10:12 UTC): Heimsieg 2.27; Auswärtssieg 2.97; BTTS Ja fehlt; Over 2,5 1.49; Under 2,5 2.62. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: Over 2,5**

---
