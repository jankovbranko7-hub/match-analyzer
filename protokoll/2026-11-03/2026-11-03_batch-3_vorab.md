# Vorabeinträge 03.11.2026 – Batch 3

System: OddAlerts-System v1.3-OA (Fassung v1.3-OA-2026-11-02). Datenquelle: Odd Alerts Data API. Rechenlauf/Entscheidungszeitpunkt: 2026-11-03 14:00 UTC; Datenabruf 2026-11-03 13:58–14:00 UTC; Eintrag erstellt 2026-11-03 14:03 UTC, vor allen Anstößen. Abfrageparameter ohne API-Schlüssel: `abrufe-2026-11-03.jsonl`; Rohdaten-Snapshot: `rohdaten-2026-11-03.tar.gz`; Modellprüfung je Wettbewerb: `modellpruefung-2026-11-03.json`. Dieser Eintrag wird nicht mehr verändert.

## Batch 3 · Nr. 1 – Analyse-ID OA-20261103-B3-1

**[Birmingham City – Millwall | 2026-11-03 20:00 UTC | England Championship 2026/2027 (Wettbewerb-ID 418, Saison-ID 2234527, Saisonfortschritt 28 %) | Match-ID 420643749]**

Nutzerangabe: Birmingham City vs Millwall. Team-IDs: Heim 4356, Gast 8902. Status beim Abruf: NS; Spielort: St. Andrew's Stadium, St. Andrew's Road, Birmingham, England; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 6 bzw. 12.

Datenstand: 2026-11-03 14:00 UTC; Datenbasis: verwendbar (je 13 Ligaspiele, xG für alle).

**Birmingham City** (Team-ID 4356) – Saison 2026/2027, nur England Championship (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 13 | 6 | 7 | 6 |
| Tore | 23 | 14 | 9 | 13 |
| Gegentore | 13 | 7 | 6 | 4 |
| Tore/Spiel | 1,77 | 2,33 | 1,29 | 2,17 |
| Gegentore/Spiel | 1,00 | 1,17 | 0,86 | 0,67 |
| xG für/Spiel | 1,78 | 1,65 | 1,90 | 1,84¹ |
| xG gegen/Spiel | 1,36 | 1,41 | 1,31 | 1,46¹ |
| Spiele mit xG | 13 von 13 | 6 von 6 | 7 von 7 | 6 von 6¹ |
| S/U/N | 6/5/2 | 2/4/0 | 4/1/2 | 4/1/1 |
| Punkte/Spiel | 1,77 | 1,67 | 1,86 | 2,17 |
| BTTS % | 61,5 % | 66,7 % | 57,1 % | 33,3 % |
| Over 2,5 % | 69,2 % | 83,3 % | 57,1 % | 66,7 % |
| Under 2,5 % | 30,8 % | 16,7 % | 42,9 % | 33,3 % |
| Clean Sheets % | 30,8 % | 33,3 % | 28,6 % | 50,0 % |
| Failed to Score % | 15,4 % | 0,0 % | 28,6 % | 16,7 % |
| BTTS-and-lose | 1 von 13 (7,7 %)² | 0 von 6 (0,0 %)² | 1 von 7 (14,3 %)² | 0 von 6 (0,0 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,23 | 1,50 | 1,00 | 1,50³ (6 Sp.) |
| goals_for_2h/Spiel | 0,92 | 1,17 | 0,71 | fehlt |
| goals_against_2h/Spiel | 0,31 | 0,33 | 0,29 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-19 H Middlesbrough 2-2 [Championship]; 2026-10-10 A West Bromwich Albion 0-1 [Championship]; 2026-10-13 H Preston North End 4-0 [Championship]; 2026-10-17 H Queens Park Rangers 3-0 [Championship]; 2026-10-24 A Cardiff City 1-0 [Championship]; 2026-10-31 A Lincoln City 1-3 [Championship]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**Millwall** (Team-ID 8902) – Saison 2026/2027, nur England Championship (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 13 | 7 | 6 | 6 |
| Tore | 23 | 15 | 8 | 10 |
| Gegentore | 21 | 9 | 12 | 8 |
| Tore/Spiel | 1,77 | 2,14 | 1,33 | 1,67 |
| Gegentore/Spiel | 1,62 | 1,29 | 2,00 | 1,33 |
| xG für/Spiel | 1,94 | 2,19 | 1,65 | 1,87¹ |
| xG gegen/Spiel | 1,32 | 1,26 | 1,37 | 1,24¹ |
| Spiele mit xG | 13 von 13 | 7 von 7 | 6 von 6 | 6 von 6¹ |
| S/U/N | 5/3/5 | 3/2/2 | 2/1/3 | 2/2/2 |
| Punkte/Spiel | 1,38 | 1,57 | 1,17 | 1,33 |
| BTTS % | 53,9 % | 42,9 % | 66,7 % | 66,7 % |
| Over 2,5 % | 76,9 % | 85,7 % | 66,7 % | 66,7 % |
| Under 2,5 % | 23,1 % | 14,3 % | 33,3 % | 33,3 % |
| Clean Sheets % | 30,8 % | 28,6 % | 33,3 % | 16,7 % |
| Failed to Score % | 15,4 % | 28,6 % | 0,0 % | 16,7 % |
| BTTS-and-lose | 3 von 13 (23,1 %)² | 0 von 7 (0,0 %)² | 3 von 6 (50,0 %)² | 1 von 6 (16,7 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,92 | 2,00 | 1,83 | 1,50³ (6 Sp.) |
| goals_for_2h/Spiel | 0,85 | 1,14 | 0,50 | fehlt |
| goals_against_2h/Spiel | 1,08 | 0,86 | 1,33 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-19 H West Ham United 2-2 [Championship]; 2026-10-10 A Preston North End 0-1 [Championship]; 2026-10-13 H Swansea City 0-1 [Championship]; 2026-10-17 H Lincoln City 2-2 [Championship]; 2026-10-24 A Portsmouth 2-1 [Championship]; 2026-10-31 H Derby County 4-1 [Championship]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

Bild: Datenbasis verwendbar mit je 13 Ligaspielen und vollständiger xG-Abdeckung; schwächere Offensive ist Millwall auswärts mit 1,33 Toren, das aber in allen 6 Auswärtsspielen traf (1,65 xG) gegen Birminghams Heimabwehr mit 1,17 Gegentoren; der Weg zu drei Toren ist über beide Teams begründet, Birmingham erzielte zu Hause 2,33 Tore, traf in jedem Heimspiel und hatte zu 83 % Over, Millwall-Auswärtsspiele hatten zu 67 % Over bei 2,00 Gegentoren; stärkstes Gegenargument sind Birminghams 3 Spiele ohne Gegentor in den letzten 6 und der Modellwert von nur 44 % für Over, die aber gegen die Torbilanz beider Teams am jeweiligen Spielort geringer wiegen.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Championship (England), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 1824 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-03 14:00 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 100 zeitlich vorwärts gewählt (Training 1094 Spiele bis 2025-04-26, Auswahl auf 365 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 365 jüngsten Spielen (2026-01-31 bis 2026-10-31, 318 bewertbar): Heimsieg Brier 0,239 gegen Grundrate 0,244 (besser), Log-Loss 0,670; Auswärtssieg Brier 0,210 gegen Grundrate 0,215 (besser), Log-Loss 0,609; BTTS Ja Brier 0,248 gegen Grundrate 0,247 (nicht besser), Log-Loss 0,689; Over 2,5 Brier 0,251 gegen Grundrate 0,251 (nicht besser), Log-Loss 0,696. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,34, λ Gast 1,08; Heimsieg 43 %, Remis 27 %, Auswärtssieg 30 %, BTTS Ja 49 %, Over 2,5 44 %, Under 2,5 56 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-03 13:58 UTC): Heimsieg 1.94; Auswärtssieg 3.90; BTTS Ja fehlt; Over 2,5 1.79; Under 2,5 2.11. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: Over 2,5**

---

## Batch 3 · Nr. 2 – Analyse-ID OA-20261103-B3-2

**[West Bromwich Albion – Southampton | 2026-11-03 20:00 UTC | England Championship 2026/2027 (Wettbewerb-ID 418, Saison-ID 2234527, Saisonfortschritt 28 %) | Match-ID 420644011]**

Nutzerangabe: West Bromwich Albion vs Southampton. Team-IDs: Heim 10207, Gast 10784. Status beim Abruf: NS; Spielort: The Hawthorns, Halfords Lane, West Bromwich, England; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 4 bzw. 5.

Datenstand: 2026-11-03 14:00 UTC; Datenbasis: verwendbar (je 13 Ligaspiele, xG für alle).

**West Bromwich Albion** (Team-ID 10207) – Saison 2026/2027, nur England Championship (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 13 | 6 | 7 | 6 |
| Tore | 19 | 9 | 10 | 9 |
| Gegentore | 14 | 6 | 8 | 7 |
| Tore/Spiel | 1,46 | 1,50 | 1,43 | 1,50 |
| Gegentore/Spiel | 1,08 | 1,00 | 1,14 | 1,17 |
| xG für/Spiel | 1,57 | 1,82 | 1,35 | 1,78¹ |
| xG gegen/Spiel | 1,42 | 1,11 | 1,68 | 1,52¹ |
| Spiele mit xG | 13 von 13 | 6 von 6 | 7 von 7 | 6 von 6¹ |
| S/U/N | 7/3/3 | 3/2/1 | 4/1/2 | 3/1/2 |
| Punkte/Spiel | 1,85 | 1,83 | 1,86 | 1,67 |
| BTTS % | 69,2 % | 66,7 % | 71,4 % | 66,7 % |
| Over 2,5 % | 46,1 % | 33,3 % | 57,1 % | 50,0 % |
| Under 2,5 % | 53,9 % | 66,7 % | 42,9 % | 50,0 % |
| Clean Sheets % | 15,4 % | 16,7 % | 14,3 % | 0,0 % |
| Failed to Score % | 15,4 % | 16,7 % | 14,3 % | 33,3 % |
| BTTS-and-lose | 1 von 13 (7,7 %)² | 0 von 6 (0,0 %)² | 1 von 7 (14,3 %)² | 0 von 6 (0,0 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,62 | 1,00 | 2,14 | 1,67³ (6 Sp.) |
| goals_for_2h/Spiel | 1,00 | 0,83 | 1,14 | fehlt |
| goals_against_2h/Spiel | 0,62 | 0,17 | 1,00 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-20 A Wolverhampton Wanderers 1-0 [Championship]; 2026-10-10 H Birmingham City 0-1 [Championship]; 2026-10-13 A Wrexham 1-2 [Championship]; 2026-10-17 H Blackburn Rovers 3-2 [Championship]; 2026-10-24 A Preston North End 1-1 [Championship]; 2026-10-31 A West Ham United 1-3 [Championship]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**Southampton** (Team-ID 10784) – Saison 2026/2027, nur England Championship (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 13 | 7 | 6 | 6 |
| Tore | 28 | 20 | 8 | 10 |
| Gegentore | 13 | 5 | 8 | 5 |
| Tore/Spiel | 2,15 | 2,86 | 1,33 | 1,67 |
| Gegentore/Spiel | 1,00 | 0,71 | 1,33 | 0,83 |
| xG für/Spiel | 1,73 | 1,94 | 1,49 | 1,65¹ |
| xG gegen/Spiel | 1,42 | 1,33 | 1,52 | 1,13¹ |
| Spiele mit xG | 13 von 13 | 7 von 7 | 6 von 6 | 6 von 6¹ |
| S/U/N | 8/3/2 | 6/1/0 | 2/2/2 | 4/1/1 |
| Punkte/Spiel | 2,08 | 2,71 | 1,33 | 2,17 |
| BTTS % | 76,9 % | 71,4 % | 83,3 % | 50,0 % |
| Over 2,5 % | 61,5 % | 71,4 % | 50,0 % | 50,0 % |
| Under 2,5 % | 38,5 % | 28,6 % | 50,0 % | 50,0 % |
| Clean Sheets % | 23,1 % | 28,6 % | 16,7 % | 50,0 % |
| Failed to Score % | 7,7 % | 14,3 % | 0,0 % | 16,7 % |
| BTTS-and-lose | 2 von 13 (15,4 %)² | 0 von 7 (0,0 %)² | 2 von 6 (33,3 %)² | 1 von 6 (16,7 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,69 | 2,14 | 1,17 | 1,33³ (6 Sp.) |
| goals_for_2h/Spiel | 1,15 | 1,71 | 0,50 | fehlt |
| goals_against_2h/Spiel | 0,54 | 0,43 | 0,67 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-09-19 A Wrexham 2-1 [Championship]; 2026-10-11 H Portsmouth 1-0 [Championship]; 2026-10-14 A Norwich City 0-1 [Championship]; 2026-10-17 H Bolton Wanderers 0-0 [Championship]; 2026-10-24 A West Ham United 2-3 [Championship]; 2026-10-31 H Queens Park Rangers 4-1 [Championship]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

Bild: Datenbasis verwendbar mit je 13 Ligaspielen und vollständiger xG-Abdeckung; schwächere Offensive ist Southampton auswärts mit 1,33 Toren gegen West Broms Heimabwehr mit 1,00 Gegentoren; ein Weg zu drei Toren ist unsicher, West-Brom-Heimspiele hatten nur zu 33 % Over; stärkstes Gegenargument ist das ausgeglichene Modell (40 % zu 34 %) zwischen zwei Teams der oberen Tabellenhälfte, sodass kein Markt klar getragen wird.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Championship (England), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 1824 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-03 14:00 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 100 zeitlich vorwärts gewählt (Training 1094 Spiele bis 2025-04-26, Auswahl auf 365 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 365 jüngsten Spielen (2026-01-31 bis 2026-10-31, 318 bewertbar): Heimsieg Brier 0,239 gegen Grundrate 0,244 (besser), Log-Loss 0,670; Auswärtssieg Brier 0,210 gegen Grundrate 0,215 (besser), Log-Loss 0,609; BTTS Ja Brier 0,248 gegen Grundrate 0,247 (nicht besser), Log-Loss 0,689; Over 2,5 Brier 0,251 gegen Grundrate 0,251 (nicht besser), Log-Loss 0,696. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,40, λ Gast 1,26; Heimsieg 40 %, Remis 26 %, Auswärtssieg 34 %, BTTS Ja 54 %, Over 2,5 50 %, Under 2,5 50 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-03 13:58 UTC): Heimsieg 2.43; Auswärtssieg 3.03; BTTS Ja fehlt; Over 2,5 1.91; Under 2,5 1.98. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: keine – ausgeglichenes Spitzenspiel, kein Markt klar getragen**

---

## Batch 3 · Nr. 3 – Analyse-ID OA-20261103-B3-3

**[Galatasaray – VfB Stuttgart | 2026-11-03 17:45 UTC | Europe Champions League 2026/2027 (Wettbewerb-ID 51, Saison-ID 2264045, Saisonfortschritt 62 %) | Match-ID 420676188]**

Nutzerangabe: Galatasaray vs VfB Stuttgart. Team-IDs: Heim 5491, Gast 4397. Status beim Abruf: NS; Spielort: Rams Park, İstanbul Çevre Yolu, Aslantepe, İstanbul, Turkey; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 23 bzw. 6.

Datenstand: 2026-11-03 14:00 UTC; Datenbasis: eingeschränkt (Champions League nur 3 Spiele je Team; heimische Ligen mit xG getrennt ausgewiesen).

**Galatasaray** (Team-ID 5491) – Saison 2026/2027, nur Europe Champions League (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 3 | 1 | 2 | 6 |
| Tore | 6 | 1 | 5 | 15 |
| Gegentore | 9 | 4 | 5 | 8 |
| Tore/Spiel | 2,00 | 1,00 | 2,50 | 2,50 |
| Gegentore/Spiel | 3,00 | 4,00 | 2,50 | 1,33 |
| xG für/Spiel | 1,10 | 0,49 | 1,41 | 1,79¹ |
| xG gegen/Spiel | 1,83 | 2,54 | 1,47 | 1,35¹ |
| Spiele mit xG | 3 von 3 | 1 von 1 | 2 von 2 | 6 von 6¹ |
| S/U/N | 1/0/2 | 0/0/1 | 1/0/1 | 5/0/1 |
| Punkte/Spiel | 1,00 | 0,00 | 1,50 | 2,50 |
| BTTS % | 100,0 % | 100,0 % | 100,0 % | 66,7 % |
| Over 2,5 % | 100,0 % | 100,0 % | 100,0 % | 83,3 % |
| Under 2,5 % | 0,0 % | 0,0 % | 0,0 % | 16,7 % |
| Clean Sheets % | 0,0 % | 0,0 % | 0,0 % | 33,3 % |
| Failed to Score % | 0,0 % | 0,0 % | 0,0 % | 0,0 % |
| BTTS-and-lose | 2 von 3 (66,7 %)² | 1 von 1 (100,0 %)² | 1 von 2 (50,0 %)² | 1 von 6 (16,7 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 2,33 | 3,00 | 2,00 | 2,00³ (6 Sp.) |
| goals_for_2h/Spiel | 0,67 | 0,00 | 1,00 | fehlt |
| goals_against_2h/Spiel | 1,67 | 3,00 | 1,00 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-10-09 H Kasımpaşa 3-1 [Super Lig]; 2026-10-13 H FC Barcelona 1-4 [Champions League]; 2026-10-17 A Gençlerbirliği 0-1 [Super Lig]; 2026-10-21 A LOSC Lille 2-4 [Champions League]; 2026-10-26 H Fenerbahçe 2-1 [Super Lig]; 2026-10-30 A Konyaspor 0-4 [Super Lig]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**VfB Stuttgart** (Team-ID 4397) – Saison 2026/2027, nur Europe Champions League (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 3 | 2 | 1 | 6 |
| Tore | 7 | 4 | 3 | 11 |
| Gegentore | 2 | 2 | 0 | 7 |
| Tore/Spiel | 2,33 | 2,00 | 3,00 | 1,83 |
| Gegentore/Spiel | 0,67 | 1,00 | 0,00 | 1,17 |
| xG für/Spiel | 1,95 | 1,80 | 2,25 | 2,17¹ |
| xG gegen/Spiel | 0,86 | 0,83 | 0,92 | 1,47¹ |
| Spiele mit xG | 3 von 3 | 2 von 2 | 1 von 1 | 6 von 6¹ |
| S/U/N | 2/1/0 | 1/1/0 | 1/0/0 | 3/1/2 |
| Punkte/Spiel | 2,33 | 2,00 | 3,00 | 1,67 |
| BTTS % | 66,7 % | 100,0 % | 0,0 % | 50,0 % |
| Over 2,5 % | 66,7 % | 50,0 % | 100,0 % | 50,0 % |
| Under 2,5 % | 33,3 % | 50,0 % | 0,0 % | 50,0 % |
| Clean Sheets % | 33,3 % | 0,0 % | 100,0 % | 33,3 % |
| Failed to Score % | 0,0 % | 0,0 % | 0,0 % | 16,7 % |
| BTTS-and-lose | 0 von 3 (0,0 %)² | 0 von 2 (0,0 %)² | 0 von 1 (0,0 %)² | 1 von 6 (16,7 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,00 | 0,50 | 2,00 | 1,83³ (6 Sp.) |
| goals_for_2h/Spiel | 0,67 | 0,00 | 2,00 | fehlt |
| goals_against_2h/Spiel | 0,33 | 0,50 | 0,00 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-10-14 A Slovan Bratislava 0-3 [Champions League]; 2026-10-17 A Hamburger SV 1-0 [Bundesliga]; 2026-10-20 H Atlético de Madrid 1-1 [Champions League]; 2026-10-23 H Borussia Mönchengladbach 2-3 [Bundesliga]; 2026-10-28 A Paderborn 0-1 [DFB Pokal]; 2026-10-31 A Bayer 04 Leverkusen 2-4 [Bundesliga]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**Galatasaray** – heimische Liga getrennt (Abschnitt 3.1): Turkey Super Lig 2026/2027, Saison-ID 2293981, stats/fixture über Ligaspiel 420643200

| Kennzahl | Gesamt | Heim | Auswärts |
|---|---|---|---|
| Spiele | 10 | 5 | 5 |
| Tore | 23 | 11 | 12 |
| Gegentore | 12 | 6 | 6 |
| Tore/Spiel | 2,30 | 2,20 | 2,40 |
| Gegentore/Spiel | 1,20 | 1,20 | 1,20 |
| xG für/Spiel | 2,19 | 2,82 | 1,56 |
| xG gegen/Spiel | 0,98 | 0,62 | 1,34 |
| Spiele mit xG | 10 von 10 | 5 von 5 | 5 von 5 |
| S/U/N | 8/1/1 | 4/1/0 | 4/0/1 |
| Punkte/Spiel | 2,50 | 2,60 | 2,40 |
| BTTS % | 50,0 % | 80,0 % | 20,0 % |
| Over 2,5 % | 80,0 % | 80,0 % | 80,0 % |
| Under 2,5 % | 20,0 % | 20,0 % | 20,0 % |
| Clean Sheets % | 40,0 % | 20,0 % | 60,0 % |
| Failed to Score % | 10,0 % | 0,0 % | 20,0 % |
| BTTS-and-lose | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) |
| Tore 2. HZ/Spiel (goals_2h) | 2,10 | 2,40 | 1,80 |
| goals_for_2h/Spiel | 1,30 | 1,40 | 1,20 |
| goals_against_2h/Spiel | 0,80 | 1,00 | 0,60 |

**VfB Stuttgart** – heimische Liga getrennt (Abschnitt 3.1): Germany Bundesliga 2026/2027, Saison-ID 2305071, stats/fixture über Ligaspiel 420679088

| Kennzahl | Gesamt | Heim | Auswärts |
|---|---|---|---|
| Spiele | 8 | 3 | 5 |
| Tore | 14 | 6 | 8 |
| Gegentore | 15 | 5 | 10 |
| Tore/Spiel | 1,75 | 2,00 | 1,60 |
| Gegentore/Spiel | 1,88 | 1,67 | 2,00 |
| xG für/Spiel | 2,06 | 2,33 | 1,90 |
| xG gegen/Spiel | 2,02 | 2,05 | 2,01 |
| Spiele mit xG | 8 von 8 | 3 von 3 | 5 von 5 |
| S/U/N | 3/0/5 | 1/0/2 | 2/0/3 |
| Punkte/Spiel | 1,12 | 1,00 | 1,20 |
| BTTS % | 62,5 % | 66,7 % | 60,0 % |
| Over 2,5 % | 62,5 % | 66,7 % | 60,0 % |
| Under 2,5 % | 37,5 % | 33,3 % | 40,0 % |
| Clean Sheets % | 12,5 % | 0,0 % | 20,0 % |
| Failed to Score % | 25,0 % | 33,3 % | 20,0 % |
| BTTS-and-lose | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) |
| Tore 2. HZ/Spiel (goals_2h) | 2,50 | 2,67 | 2,40 |
| goals_for_2h/Spiel | 1,12 | 1,33 | 1,00 |
| goals_against_2h/Spiel | 1,38 | 1,33 | 1,40 |

Hinweis Europapokal/Pokal: Wettbewerbstabellen oben nur dieser Wettbewerb (wenige Spiele, inklusive Qualifikation), heimische Liga getrennt (Abschnitt 3.1); Ausfälle, Aufstellungen und Belastung: nicht geprüft.

Bild: Datenbasis eingeschränkt, weil die Champions League nur 3 Spiele je Team umfasst, die getrennt ausgewiesenen Ligadaten mit xG das Bild aber stützen; schwächere Offensive ist Stuttgart auswärts, das aber in der Bundesliga 1,60 Tore pro Auswärtsspiel bei 2,06 xG pro Spiel erzielt und in 5 der letzten 6 traf, während Galatasaray in der Liga in jedem Heimspiel traf (2,20 Tore, 2,82 xG), beide Torargumente sind also eigenständig; ein Weg zu drei Toren ist über beide Teams plausibel (Galatasaray in der Liga 80 % Over), für BTTS aber nicht nötig; stärkstes Gegenargument sind Galatasarays 60 % Auswärts-Clean-Sheets in der Liga, die aber für dieses Heimspiel nicht gelten, wo Galatasaray zu Hause nur 20 % Clean Sheets hat und Stuttgart in der Liga 2,02 xG gegen zulässt, daher gering gewichtet.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Champions League (Europe), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 877 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-03 14:00 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 10 zeitlich vorwärts gewählt (Training 526 Spiele bis 2025-08-05, Auswahl auf 175 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 176 jüngsten Spielen (2026-02-17 bis 2026-10-21, 93 bewertbar): Heimsieg Brier 0,209 gegen Grundrate 0,250 (besser), Log-Loss 0,608; Auswärtssieg Brier 0,179 gegen Grundrate 0,211 (besser), Log-Loss 0,532; BTTS Ja Brier 0,233 gegen Grundrate 0,244 (besser), Log-Loss 0,660; Over 2,5 Brier 0,231 gegen Grundrate 0,232 (besser), Log-Loss 0,654. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,85, λ Gast 1,39; Heimsieg 48 %, Remis 23 %, Auswärtssieg 29 %, BTTS Ja 63 %, Over 2,5 63 %, Under 2,5 37 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-03 13:58 UTC): Heimsieg 2.08; Auswärtssieg 3.25; BTTS Ja fehlt; Over 2,5 1.33; Under 2,5 3.46. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: BTTS Ja**

---

## Batch 3 · Nr. 4 – Analyse-ID OA-20261103-B3-4

**[Shakhtar Donetsk – Sporting CP | 2026-11-03 17:45 UTC | Europe Champions League 2026/2027 (Wettbewerb-ID 51, Saison-ID 2264045, Saisonfortschritt 62 %) | Match-ID 420684491]**

Nutzerangabe: Shakhtar Donetsk vs Sporting CP. Team-IDs: Heim 4148, Gast 5095. Status beim Abruf: NS; Spielort: Stamford Bridge, Fulham Road, London, England; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 17 bzw. 12.

Datenstand: 2026-11-03 14:00 UTC; Datenbasis: eingeschränkt (Champions League nur 3 Spiele je Team; Shakhtar ohne xG in der Liga).

**Shakhtar Donetsk** (Team-ID 4148) – Saison 2026/2027, nur Europe Champions League (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 3 | 1 | 2 | 6 |
| Tore | 4 | 3 | 1 | 10 |
| Gegentore | 3 | 1 | 2 | 3 |
| Tore/Spiel | 1,33 | 3,00 | 0,50 | 1,67 |
| Gegentore/Spiel | 1,00 | 1,00 | 1,00 | 0,50 |
| xG für/Spiel | 0,90 | 1,32 | 0,68 | 1,08¹ |
| xG gegen/Spiel | 0,89 | 1,15 | 0,76 | 1,08¹ |
| Spiele mit xG | 3 von 3 | 1 von 1 | 2 von 2 | 2 von 6¹ |
| S/U/N | 1/1/1 | 1/0/0 | 0/1/1 | 4/1/1 |
| Punkte/Spiel | 1,33 | 3,00 | 0,50 | 2,17 |
| BTTS % | 66,7 % | 100,0 % | 50,0 % | 33,3 % |
| Over 2,5 % | 33,3 % | 100,0 % | 0,0 % | 50,0 % |
| Under 2,5 % | 66,7 % | 0,0 % | 100,0 % | 50,0 % |
| Clean Sheets % | 0,0 % | 0,0 % | 0,0 % | 50,0 % |
| Failed to Score % | 33,3 % | 0,0 % | 50,0 % | 33,3 % |
| BTTS-and-lose | 0 von 3 (0,0 %)² | 0 von 1 (0,0 %)² | 0 von 2 (0,0 %)² | 0 von 6 (0,0 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 1,33 | 2,00 | 1,00 | 1,33³ (6 Sp.) |
| goals_for_2h/Spiel | 0,67 | 2,00 | 0,00 | fehlt |
| goals_against_2h/Spiel | 0,67 | 0,00 | 1,00 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-10-14 H AEK Athens 3-1 [Champions League]; 2026-10-17 H Kolos Kovalivka 2-1 [Premier League]; 2026-10-21 A Inter 1-0 [Champions League]; 2026-10-24 H Zorya Luhansk 0-0 [Premier League]; 2026-10-27 H Dynamo Kyiv 3-0 [Ukrainian Cup]; 2026-10-30 H Obolon'-Brovar 2-0 [Premier League]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**Sporting CP** (Team-ID 5095) – Saison 2026/2027, nur Europe Champions League (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 3 | 2 | 1 | 6 |
| Tore | 7 | 5 | 2 | 12 |
| Gegentore | 4 | 4 | 0 | 7 |
| Tore/Spiel | 2,33 | 2,50 | 2,00 | 2,00 |
| Gegentore/Spiel | 1,33 | 2,00 | 0,00 | 1,17 |
| xG für/Spiel | 1,99 | 2,27 | 1,42 | 2,07¹ |
| xG gegen/Spiel | 1,42 | 1,28 | 1,72 | 1,14¹ |
| Spiele mit xG | 3 von 3 | 2 von 2 | 1 von 1 | 5 von 6¹ |
| S/U/N | 2/0/1 | 1/0/1 | 1/0/0 | 4/0/2 |
| Punkte/Spiel | 2,00 | 1,50 | 3,00 | 2,00 |
| BTTS % | 66,7 % | 100,0 % | 0,0 % | 66,7 % |
| Over 2,5 % | 66,7 % | 100,0 % | 0,0 % | 66,7 % |
| Under 2,5 % | 33,3 % | 0,0 % | 100,0 % | 33,3 % |
| Clean Sheets % | 33,3 % | 0,0 % | 100,0 % | 33,3 % |
| Failed to Score % | 0,0 % | 0,0 % | 0,0 % | 0,0 % |
| BTTS-and-lose | 1 von 3 (33,3 %)² | 1 von 2 (50,0 %)² | 0 von 1 (0,0 %)² | 2 von 6 (33,3 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 2,00 | 2,50 | 1,00 | 2,00³ (6 Sp.) |
| goals_for_2h/Spiel | 1,33 | 1,50 | 1,00 | fehlt |
| goals_against_2h/Spiel | 0,67 | 1,00 | 0,00 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-10-09 A Sporting Braga 1-3 [Liga Portugal]; 2026-10-13 A Lens 0-2 [Champions League]; 2026-10-21 H LASK 2-3 [Champions League]; 2026-10-25 H Academico Viseu 1-2 [Liga Portugal]; 2026-10-27 H Marítimo 2-1 [Taça da Liga]; 2026-10-30 A Casa Pia 0-2 [Liga Portugal]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**Shakhtar Donetsk** – heimische Liga getrennt (Abschnitt 3.1): Ukraine Premier League 2026/2027, Saison-ID 2304058, stats/fixture über Ligaspiel 420594548

| Kennzahl | Gesamt | Heim | Auswärts |
|---|---|---|---|
| Spiele | 11 | 7 | 4 |
| Tore | 22 | 14 | 8 |
| Gegentore | 5 | 4 | 1 |
| Tore/Spiel | 2,00 | 2,00 | 2,00 |
| Gegentore/Spiel | 0,45 | 0,57 | 0,25 |
| xG für/Spiel | fehlt | fehlt | fehlt |
| xG gegen/Spiel | fehlt | fehlt | fehlt |
| Spiele mit xG | 0 von 11 | 0 von 7 | 0 von 4 |
| S/U/N | 9/1/1 | 5/1/1 | 4/0/0 |
| Punkte/Spiel | 2,55 | 2,29 | 3,00 |
| BTTS % | 27,3 % | 28,6 % | 25,0 % |
| Over 2,5 % | 45,5 % | 42,9 % | 50,0 % |
| Under 2,5 % | 54,5 % | 57,1 % | 50,0 % |
| Clean Sheets % | 63,6 % | 57,1 % | 75,0 % |
| Failed to Score % | 18,2 % | 28,6 % | 0,0 % |
| BTTS-and-lose | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) |
| Tore 2. HZ/Spiel (goals_2h) | 1,45 | 1,57 | 1,25 |
| goals_for_2h/Spiel | 1,27 | 1,29 | 1,25 |
| goals_against_2h/Spiel | 0,18 | 0,29 | 0,00 |

**Sporting CP** – heimische Liga getrennt (Abschnitt 3.1): Portugal Liga Portugal 2026/2027, Saison-ID 2244284, stats/fixture über Ligaspiel 420611773

| Kennzahl | Gesamt | Heim | Auswärts |
|---|---|---|---|
| Spiele | 10 | 5 | 5 |
| Tore | 23 | 11 | 12 |
| Gegentore | 11 | 7 | 4 |
| Tore/Spiel | 2,30 | 2,20 | 2,40 |
| Gegentore/Spiel | 1,10 | 1,40 | 0,80 |
| xG für/Spiel | 1,84 | 1,87 | 1,81 |
| xG gegen/Spiel | 0,82 | 0,89 | 0,76 |
| Spiele mit xG | 10 von 10 | 5 von 5 | 5 von 5 |
| S/U/N | 6/3/1 | 3/1/1 | 3/2/0 |
| Punkte/Spiel | 2,10 | 2,00 | 2,20 |
| BTTS % | 70,0 % | 80,0 % | 60,0 % |
| Over 2,5 % | 70,0 % | 80,0 % | 60,0 % |
| Under 2,5 % | 30,0 % | 20,0 % | 40,0 % |
| Clean Sheets % | 30,0 % | 20,0 % | 40,0 % |
| Failed to Score % | 0,0 % | 0,0 % | 0,0 % |
| BTTS-and-lose | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) |
| Tore 2. HZ/Spiel (goals_2h) | 2,00 | 2,00 | 2,00 |
| goals_for_2h/Spiel | 1,10 | 0,80 | 1,40 |
| goals_against_2h/Spiel | 0,90 | 1,20 | 0,60 |

Hinweis Europapokal/Pokal: Wettbewerbstabellen oben nur dieser Wettbewerb (wenige Spiele, inklusive Qualifikation), heimische Liga getrennt (Abschnitt 3.1); Ausfälle, Aufstellungen und Belastung: nicht geprüft.

Bild: Datenbasis eingeschränkt, weil die Champions League nur 3 Spiele je Team umfasst und für Shakhtars Liga keine xG vorliegen; schwächere Offensive ist Shakhtar mit 0,90 xG pro Champions-League-Spiel gegen Sporting, das in der Liga nur 0,82 xG gegen zulässt; ein Weg zu drei Toren ist unsicher, Shakhtar-Ligaspiele hatten nur zu 45 % Over bei 64 % Clean Sheets; stärkstes Gegenargument ist das ausgeglichene Modell (38 % zu 37 %), sodass kein Markt klar getragen wird.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Champions League (Europe), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 877 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-03 14:00 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 10 zeitlich vorwärts gewählt (Training 526 Spiele bis 2025-08-05, Auswahl auf 175 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 176 jüngsten Spielen (2026-02-17 bis 2026-10-21, 93 bewertbar): Heimsieg Brier 0,209 gegen Grundrate 0,250 (besser), Log-Loss 0,608; Auswärtssieg Brier 0,179 gegen Grundrate 0,211 (besser), Log-Loss 0,532; BTTS Ja Brier 0,233 gegen Grundrate 0,244 (besser), Log-Loss 0,660; Over 2,5 Brier 0,231 gegen Grundrate 0,232 (besser), Log-Loss 0,654. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 1,43, λ Gast 1,40; Heimsieg 38 %, Remis 25 %, Auswärtssieg 37 %, BTTS Ja 57 %, Over 2,5 54 %, Under 2,5 46 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-03 13:58 UTC): Heimsieg 3.57; Auswärtssieg 2.07; BTTS Ja fehlt; Over 2,5 1.71; Under 2,5 2.23. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: keine – ausgeglichenes Bild, kein Markt klar getragen**

---

## Batch 3 · Nr. 5 – Analyse-ID OA-20261103-B3-5

**[FC Barcelona – Aston Villa | 2026-11-03 20:00 UTC | Europe Champions League 2026/2027 (Wettbewerb-ID 51, Saison-ID 2264045, Saisonfortschritt 62 %) | Match-ID 420673876]**

Nutzerangabe: FC Barcelona vs Aston Villa. Team-IDs: Heim 10963, Gast 10661. Status beim Abruf: NS; Spielort: Spotify Camp Nou, Barcelona, Catalonia, Barcelona, Spain; neutraler Platz: nicht gekennzeichnet; Tabellenplatz laut Odd Alerts 8 bzw. 2.

Datenstand: 2026-11-03 14:00 UTC; Datenbasis: eingeschränkt (Champions League nur 3 Spiele je Team; heimische Ligen mit xG getrennt ausgewiesen).

**FC Barcelona** (Team-ID 10963) – Saison 2026/2027, nur Europe Champions League (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 3 | 1 | 2 | 6 |
| Tore | 11 | 5 | 6 | 21 |
| Gegentore | 6 | 1 | 5 | 10 |
| Tore/Spiel | 3,67 | 5,00 | 3,00 | 3,50 |
| Gegentore/Spiel | 2,00 | 1,00 | 2,50 | 1,67 |
| xG für/Spiel | 2,29 | 2,10 | 2,39 | 2,19¹ |
| xG gegen/Spiel | 1,28 | 0,61 | 1,61 | 1,13¹ |
| Spiele mit xG | 3 von 3 | 1 von 1 | 2 von 2 | 6 von 6¹ |
| S/U/N | 2/0/1 | 1/0/0 | 1/0/1 | 4/0/2 |
| Punkte/Spiel | 2,00 | 3,00 | 1,50 | 2,00 |
| BTTS % | 100,0 % | 100,0 % | 100,0 % | 83,3 % |
| Over 2,5 % | 100,0 % | 100,0 % | 100,0 % | 100,0 % |
| Under 2,5 % | 0,0 % | 0,0 % | 0,0 % | 0,0 % |
| Clean Sheets % | 0,0 % | 0,0 % | 0,0 % | 16,7 % |
| Failed to Score % | 0,0 % | 0,0 % | 0,0 % | 0,0 % |
| BTTS-and-lose | 1 von 3 (33,3 %)² | 0 von 1 (0,0 %)² | 1 von 2 (50,0 %)² | 2 von 6 (33,3 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 4,00 | 4,00 | 4,00 | 3,00³ (6 Sp.) |
| goals_for_2h/Spiel | 2,67 | 3,00 | 2,50 | fehlt |
| goals_against_2h/Spiel | 1,33 | 1,00 | 1,50 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-10-10 H Getafe 3-0 [La Liga]; 2026-10-13 A Galatasaray 1-4 [Champions League]; 2026-10-17 A Real Betis 2-5 [La Liga]; 2026-10-20 A Paris Saint Germain 4-2 [Champions League]; 2026-10-25 H Real Madrid 1-2 [La Liga]; 2026-10-31 H Deportivo Alavés 6-1 [La Liga]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**Aston Villa** (Team-ID 10661) – Saison 2026/2027, nur Europe Champions League (stats/fixture, Odd Alerts; Freundschaftsspiele ausgeschlossen)

| Kennzahl | Gesamt | Heim | Auswärts | letzte 6 |
|---|---|---|---|---|
| Spiele | 3 | 2 | 1 | 6 |
| Tore | 12 | 9 | 3 | 13 |
| Gegentore | 3 | 1 | 2 | 6 |
| Tore/Spiel | 4,00 | 4,50 | 3,00 | 2,17 |
| Gegentore/Spiel | 1,00 | 0,50 | 2,00 | 1,00 |
| xG für/Spiel | 2,75 | 3,01 | 2,23 | 2,02¹ |
| xG gegen/Spiel | 1,30 | 1,14 | 1,61 | 1,85¹ |
| Spiele mit xG | 3 von 3 | 2 von 2 | 1 von 1 | 6 von 6¹ |
| S/U/N | 3/0/0 | 2/0/0 | 1/0/0 | 4/1/1 |
| Punkte/Spiel | 3,00 | 3,00 | 3,00 | 2,17 |
| BTTS % | 66,7 % | 50,0 % | 100,0 % | 50,0 % |
| Over 2,5 % | 100,0 % | 100,0 % | 100,0 % | 66,7 % |
| Under 2,5 % | 0,0 % | 0,0 % | 0,0 % | 33,3 % |
| Clean Sheets % | 33,3 % | 50,0 % | 0,0 % | 33,3 % |
| Failed to Score % | 0,0 % | 0,0 % | 0,0 % | 16,7 % |
| BTTS-and-lose | 0 von 3 (0,0 %)² | 0 von 2 (0,0 %)² | 0 von 1 (0,0 %)² | 0 von 6 (0,0 %) |
| Tore 2. HZ/Spiel (goals_2h, beide Teams) | 2,00 | 2,50 | 1,00 | 1,67³ (6 Sp.) |
| goals_for_2h/Spiel | 1,33 | 2,00 | 0,00 | fehlt |
| goals_against_2h/Spiel | 0,67 | 0,50 | 1,00 | fehlt |

Letzte 6 (Spielliste fixtures/between, alle Pflichtwettbewerbe, ohne Freundschaftsspiele; Wettbewerb je Spiel angegeben): 2026-10-14 H Fenerbahçe 6-0 [Champions League]; 2026-10-17 A Newcastle United 0-1 [Premier League]; 2026-10-21 H Viking 3-1 [Champions League]; 2026-10-24 H Manchester City 2-1 [Premier League]; 2026-10-28 A AFC Bournemouth 3-0 [Carabao Cup]; 2026-10-31 H Fulham 1-1 [Premier League]. ¹ xG letzte 6 aus stats/fixture?last_x=6_overall (all_comps: true, wettbewerbsübergreifend; Spielmenge nach Toren/Spielzahl deckungsgleich mit der Liste). ² BTTS-and-lose Saisonspalten aus den abgerufenen Einzelergebnissen dieser Liga-Saison ausgezählt. ³ 2. HZ letzte 6 aus Endstand minus Halbzeitstand.

**FC Barcelona** – heimische Liga getrennt (Abschnitt 3.1): Spain La Liga 2026/2027, Saison-ID 2244302, stats/fixture über Ligaspiel 420654545

| Kennzahl | Gesamt | Heim | Auswärts |
|---|---|---|---|
| Spiele | 11 | 6 | 5 |
| Tore | 46 | 24 | 22 |
| Gegentore | 12 | 7 | 5 |
| Tore/Spiel | 4,18 | 4,00 | 4,40 |
| Gegentore/Spiel | 1,09 | 1,17 | 1,00 |
| xG für/Spiel | 3,03 | 3,07 | 2,98 |
| xG gegen/Spiel | 0,97 | 0,98 | 0,95 |
| Spiele mit xG | 11 von 11 | 6 von 6 | 5 von 5 |
| S/U/N | 10/0/1 | 5/0/1 | 5/0/0 |
| Punkte/Spiel | 2,73 | 2,50 | 3,00 |
| BTTS % | 63,6 % | 66,7 % | 60,0 % |
| Over 2,5 % | 90,9 % | 83,3 % | 100,0 % |
| Under 2,5 % | 9,1 % | 16,7 % | 0,0 % |
| Clean Sheets % | 36,4 % | 33,3 % | 40,0 % |
| Failed to Score % | 0,0 % | 0,0 % | 0,0 % |
| BTTS-and-lose | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) |
| Tore 2. HZ/Spiel (goals_2h) | 2,82 | 2,50 | 3,20 |
| goals_for_2h/Spiel | 2,18 | 1,83 | 2,60 |
| goals_against_2h/Spiel | 0,64 | 0,67 | 0,60 |

**Aston Villa** – heimische Liga getrennt (Abschnitt 3.1): England Premier League 2026/2027, Saison-ID 2263973, stats/fixture über Ligaspiel 420665669

| Kennzahl | Gesamt | Heim | Auswärts |
|---|---|---|---|
| Spiele | 9 | 5 | 4 |
| Tore | 10 | 6 | 4 |
| Gegentore | 13 | 7 | 6 |
| Tore/Spiel | 1,11 | 1,20 | 1,00 |
| Gegentore/Spiel | 1,44 | 1,40 | 1,50 |
| xG für/Spiel | 1,18 | 1,13 | 1,24 |
| xG gegen/Spiel | 1,82 | 1,94 | 1,67 |
| Spiele mit xG | 9 von 9 | 5 von 5 | 4 von 4 |
| S/U/N | 3/3/3 | 1/2/2 | 2/1/1 |
| Punkte/Spiel | 1,33 | 1,00 | 1,75 |
| BTTS % | 55,6 % | 80,0 % | 25,0 % |
| Over 2,5 % | 55,6 % | 60,0 % | 50,0 % |
| Under 2,5 % | 44,4 % | 40,0 % | 50,0 % |
| Clean Sheets % | 22,2 % | 0,0 % | 50,0 % |
| Failed to Score % | 33,3 % | 20,0 % | 50,0 % |
| BTTS-and-lose | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) | fehlt (Einzelergebnisse der Ligasaison nicht abgerufen) |
| Tore 2. HZ/Spiel (goals_2h) | 1,44 | 1,80 | 1,00 |
| goals_for_2h/Spiel | 0,56 | 0,60 | 0,50 |
| goals_against_2h/Spiel | 0,89 | 1,20 | 0,50 |

Hinweis Europapokal/Pokal: Wettbewerbstabellen oben nur dieser Wettbewerb (wenige Spiele, inklusive Qualifikation), heimische Liga getrennt (Abschnitt 3.1); Ausfälle, Aufstellungen und Belastung: nicht geprüft.

Bild: Datenbasis eingeschränkt, weil die Champions League nur 3 Spiele je Team umfasst, die getrennt ausgewiesenen Ligadaten mit xG das Bild aber stützen; schwächere Offensive ist Aston Villa mit 1,00 Tor pro Liga-Auswärtsspiel und 1,24 xG gegen Barcelonas Abwehr mit 0,97 xG gegen; der Weg zu drei Toren ist über Barcelona allein begründet (4,18 Tore und 3,03 xG pro Ligaspiel, 91 % Over in der Liga, alle letzten 6 mit drei oder mehr Toren) und wird durch Villas Champions-League-Torform zusätzlich gestützt, das Modell schätzt Over auf 74 %; stärkstes Gegenargument sind Villas 50 % Clean Sheets in Liga-Auswärtsspielen, die gegen Barcelonas Offensive aber gering gewichtet werden.

Modell: OA-Poisson-L2 v1.3-OA-2026-11-02 (Abschnitt 5.3); Training: Champions League (Europe), Saisons 2023/2024, 2024/2025, 2025/2026, 2026/2027, 877 abgeschlossene Spiele (Status FT) vor dem Rechenlauf 2026-11-03 14:00 UTC, neutraler Platz in Odd Alerts nicht gekennzeichnet (alle als Heimspiele behandelt); alpha = 10 zeitlich vorwärts gewählt (Training 526 Spiele bis 2025-08-05, Auswahl auf 175 späteren Spielen nach mittlerem negativem Log-Score); unberührter Test auf den 176 jüngsten Spielen (2026-02-17 bis 2026-10-21, 93 bewertbar): Heimsieg Brier 0,209 gegen Grundrate 0,250 (besser), Log-Loss 0,608; Auswärtssieg Brier 0,179 gegen Grundrate 0,211 (besser), Log-Loss 0,532; BTTS Ja Brier 0,233 gegen Grundrate 0,244 (besser), Log-Loss 0,660; Over 2,5 Brier 0,231 gegen Grundrate 0,232 (besser), Log-Loss 0,654. Stärke: Siegmärkte im Test meist besser als die Grundrate; Grenze: unabhängige Poisson-Tore, gleiche Gewichtung aller Saisons (Kaderwechsel und Aufsteiger schlecht abgebildet), Torlinien- und BTTS-Märkte nur soweit oben ausgewiesen; Status experimentell. Rechenwerte (Schätzung): λ Heim 2,29, λ Gast 1,59; Heimsieg 54 %, Remis 20 %, Auswärtssieg 26 %, BTTS Ja 72 %, Over 2,5 74 %, Under 2,5 26 %.

Quote: Pinnacle über Odd Alerts odds/history (Feld closing = letzter Stand beim Abruf 2026-11-03 13:58 UTC): Heimsieg 1.28; Auswärtssieg 8.63; BTTS Ja fehlt; Over 2,5 fehlt; Under 2,5 fehlt. Nur Zusatzinformation, keine Freigabebedingung.

**Auswahl: Over 2,5**

---
