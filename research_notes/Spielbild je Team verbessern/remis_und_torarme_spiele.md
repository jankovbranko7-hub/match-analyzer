# Remis, torarme Spiele, Siege zu Null und BTTS – was sie wahrscheinlicher macht (Evidenz)

Hinweis zur Methode (gilt für alle Abschnitte): Viele Zahlen unten stammen aus einer **eigenen Auswertung (EA)** der Rohdaten von [football-data.co.uk](https://www.football-data.co.uk/data.php) (Spaltenbeschreibung: [notes.txt](https://www.football-data.co.uk/notes.txt)): 35.459 Ligaspiele, 12 Ligen (Premier League, Championship, Bundesliga, 2. Bundesliga, La Liga, Segunda, Serie A, Serie B, Ligue 1, Ligue 2, Eredivisie, Primeira Liga), Saisons 2018/19–2025/26, nur reguläre Spielzeit. Für Vorhersagetests wurden die Corona-Saisons 2019/20 und 2020/21 ausgeschlossen (26.677 Spiele) und nur Spiele genutzt, in denen beide Teams schon ≥ 6 Saisonspiele hatten (22.397 Spiele). Teamwerte vor dem Spiel = Saisonschnitt **nur aus früheren Spielen** (kein Blick in die Zukunft). xG ist in diesen Daten nicht enthalten; als xG-Ersatz dienen **Torschüsse aufs Tor (SOT)**. Wettquoten (Pinnacle-Schlussquoten, sonst Marktdurchschnitt) wurden **nur als Messlatte für Teamstärke/erwartete Tore** genutzt, nicht als Wettmodell. „AUC“ = Trennschärfe eines Merkmals (0,50 = Zufall, 1,00 = perfekt; im Fußball sind 0,60–0,70 schon gut). Skripte liegen nur im Session-Scratchpad.

## 1. Basisraten je Liga (Remis %, Over 2.5 %, BTTS %, Zu-Null-Quoten), Top- und 2. Ligen

### Takeaway
Über 12 europäische Ligen (2018/19–2025/26) enden 26,7 % der Spiele remis, 50,1 % mit Over 2.5, 52,6 % mit BTTS; ein Team spielt in 27,4 % seiner Spiele zu Null, und 54,5 % aller Siege sind Siege zu Null. Die Ligaunterschiede sind groß und stabiler als Teamquoten: Bundesliga/Eredivisie/2. Bundesliga sind torreich (O2.5 ≈ 58–61 %, BTTS ≈ 56–60 %, Remis ≈ 23–26 %), Serie B, Segunda und Ligue 2 sind remis- und torarm (Remis ≈ 29–32 %, O2.5 ≈ 40–45 %, 0:0 ≈ 9–11 %).

### Cited Findings
- **Basisraten 2018/19–2025/26 (EA, alle 8 Saisons inkl. Corona-Jahre)** — [football-data.co.uk](https://www.football-data.co.uk/data.php):

| Liga | Spiele | Tore/Sp | Heim % | Remis % | Ausw. % | O2.5 % | BTTS % | 0:0 % | 1:1 % | Zu Null je Team-Spiel % | Heim zu Null % | Ausw. zu Null % | Sieg zu Null (Anteil aller Spiele) % | Anteil Siege, die zu Null sind % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ENG Premier League | 3040 | 2,86 | 43,9 | 23,0 | 33,0 | 54,8 | 53,5 | 5,7 | 10,9 | 26,1 | 29,0 | 23,1 | 40,9 | 53,1 |
| ENG Championship | 4416 | 2,54 | 43,0 | 26,5 | 30,5 | 47,3 | 51,1 | 7,5 | 12,9 | 28,2 | 32,1 | 24,3 | 41,5 | 56,4 |
| GER Bundesliga | 2448 | 3,16 | 43,5 | 24,6 | 31,9 | 61,4 | 59,8 | 5,1 | 11,9 | 22,7 | 25,8 | 19,6 | 35,1 | 46,6 |
| GER 2. Bundesliga | 2448 | 2,96 | 43,3 | 26,5 | 30,2 | 58,3 | 58,4 | 6,0 | 11,7 | 23,8 | 27,9 | 19,7 | 35,6 | 48,4 |
| ESP La Liga | 3040 | 2,57 | 45,0 | 27,0 | 28,0 | 46,7 | 51,6 | 7,5 | 13,6 | 27,9 | 33,0 | 22,9 | 41,0 | 56,1 |
| ESP Segunda | 3696 | 2,30 | 44,3 | 30,0 | 25,7 | 40,5 | 48,1 | 10,6 | 14,0 | 31,2 | 37,3 | 25,1 | 41,3 | 59,0 |
| ITA Serie A | 3040 | 2,72 | 41,0 | 26,5 | 32,5 | 52,0 | 54,0 | 6,9 | 12,1 | 26,5 | 29,2 | 23,7 | 39,0 | 53,2 |
| ITA Serie B | 3002 | 2,48 | 41,2 | 31,7 | 27,0 | 45,0 | 53,3 | 8,7 | 15,9 | 27,7 | 32,4 | 23,0 | 38,1 | 55,8 |
| FRA Ligue 1 | 2717 | 2,75 | 43,0 | 25,3 | 31,7 | 52,2 | 53,6 | 7,1 | 11,9 | 26,8 | 30,1 | 23,5 | 39,3 | 52,6 |
| FRA Ligue 2 | 2790 | 2,38 | 41,5 | 28,8 | 29,6 | 43,1 | 46,9 | 10,5 | 12,4 | 31,8 | 35,7 | 27,8 | 42,6 | 59,9 |
| NED Eredivisie | 2374 | 3,11 | 45,3 | 23,5 | 31,2 | 59,8 | 56,2 | 5,0 | 11,2 | 24,4 | 28,9 | 19,8 | 38,8 | 50,6 |
| POR Primeira Liga | 2448 | 2,61 | 43,2 | 24,4 | 32,4 | 49,0 | 48,5 | 6,9 | 10,9 | 29,2 | 33,1 | 25,4 | 44,6 | 58,9 |
| **Alle 12** | **35459** | **2,67** | **43,2** | **26,7** | **30,2** | **50,1** | **52,6** | **7,4** | **12,6** | **27,4** | **31,5** | **23,3** | **40,0** | **54,5** |

- **Jüngste drei Saisons 2023/24–2025/26 (EA, 13.182 Spiele)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): alle 12 Ligen: 2,73 Tore/Sp, Remis 26,6 %, O2.5 52,1 %, BTTS 54,1 %, 0:0 7,0 %, zu Null je Team-Spiel 26,4 %. Je Liga (Remis / O2.5 / BTTS / 0:0): Premier League 24,5 / 58,8 / 58,3 / 4,7; Championship 26,0 / 49,1 / 53,1 / 6,8; Bundesliga 25,4 / 62,0 / 60,1 / 5,1; 2. Bundesliga 25,2 / 59,4 / 59,6 / 5,6; La Liga 26,1 / 48,2 / 53,4 / 5,9; Segunda 27,7 / 45,4 / 50,8 / 9,5; Serie A 28,0 / 47,7 / 49,7 / 8,2; Serie B 32,4 / 47,6 / 54,8 / 9,2; Ligue 1 23,7 / 53,7 / 53,8 / 7,1; Ligue 2 27,7 / 47,5 / 49,5 / 9,7; Eredivisie 25,4 / 60,2 / 58,3 / 4,0; Primeira Liga 25,8 / 52,7 / 50,1 / 6,3.
- **Schwankung von Saison zu Saison (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Remisquote Premier League zwischen 18,7 % (2018/19) und 27,4 % (2025/26); Primeira Liga 18,0 % (2022/23) bis 28,4 % (2021/22); Serie B 26,8 % bis 34,5 %; Bundesliga nur 22,2 % bis 26,5 %. O2.5 Premier League 50,0 % (2020/21) bis 64,7 % (2023/24); Serie A fällt von 62,9 % (2019/20) auf 45,8 % (2025/26), BTTS Serie A von 62,1 % auf 45,3 %; Segunda steigt von 34,2 % O2.5 (2020/21) auf 50,4 % (2025/26). Ligaraten können also innerhalb weniger Jahre um 10–15 Prozentpunkte driften.
- **Zusammensetzung der Remis (EA, alle Spiele)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): 47,1 % aller Remis sind 1:1, 27,9 % 0:0, 20,6 % 2:2, 3,9 % 3:3, 0,4 % 4:4. Nur gut ein Viertel der Remis ist torlos – ein Remis-Tipp ist also mehrheitlich ein Tipp auf ein Spiel mit Toren auf beiden Seiten.
- **Externe Gegenprobe BTTS (Zeitraum nicht angegeben, Datenbankstand 12.10.2026)**: BTTS 52,1 % über 81.113 Spiele; Bundesliga 60,2 % (968 Sp.), Eredivisie 59,3 %, Premier League 58,1 %, Ligue 1 54,4 %, La Liga 53,7 %, Championship 53,0 %, Serie A 50,2 %, Primeira Liga 50,1 %; 0:0-Quote z. B. Serie A 7,9 %, Championship 7,3 %, Bundesliga 5,3 % — [Daily Sport Pick](https://dailysportpick.com/learn/both-teams-to-score-explained/). Das deckt sich größenordnungsmäßig mit der EA für die jüngsten Saisons.
- FootyStats-Ligaseiten zeigen nur die aktuelle Saison (2026/27, wenige Spieltage) – z. B. Premier League O2.5 56 %, Bundesliga O2.5 78 % – und sind daher als Basisrate ungeeignet — [FootyStats Premier League](https://footystats.org/england/premier-league), [FootyStats Bundesliga](https://footystats.org/germany/bundesliga).

### Inferences
- Die Liga ist der stärkste und stabilste einzelne „Prior“: Zwischen Bundesliga (O2.5 61 %) und Segunda (40 %) liegen über 20 Prozentpunkte – mehr als die meisten Team-Merkmale innerhalb einer Liga trennen (siehe Abschnitte 3–4).
- Zweite Ligen sind nicht einheitlich: Serie B, Segunda, Ligue 2 = remis-/torarm; 2. Bundesliga = fast so torreich wie die Bundesliga. Eine pauschale Regel „2. Liga = torarm“ wäre falsch.
- Wegen der Drift sollten Ligaraten aus den letzten 2–3 Saisons statt aus langen Zeiträumen genommen werden (Serie A ist heute klar torärmer als 2019–2022).
- Siege zu Null sind kein Sonderfall: Über die Hälfte aller Siege (in torarmen Ligen fast 60 %) sind Siege zu Null; in Bundesliga/2. Bundesliga sind es weniger als die Hälfte.

### Gaps
- Keine Daten für weitere zweite Ligen (z. B. 3. Liga, League One) und keinen Europapokal ausgewertet.
- FootyStats-Ligaseiten für frühere Saisons (z. B. 2024/25) konnten nicht direkt abgerufen werden; die Basisraten stammen daher aus der eigenen Auswertung.
- Die Corona-Saisons (Geisterspiele, weniger Heimvorteil) sind in der 8-Saisons-Tabelle enthalten; die 3-Saisons-Zahlen sind davon frei.

## 2. Was sagt Remis voraus – und wie schlecht sind Remis vorhersagbar?

### Takeaway
Remis sind messbar der am schlechtesten vorhersagbare 1X2-Ausgang: Selbst der Markt erreicht für Remis nur AUC 0,58 (Heimsieg 0,70, Auswärtssieg 0,71), die Remis-Wahrscheinlichkeit liegt in 95 % der Spiele zwischen 16 % und 33 % und überschreitet praktisch nie 35–40 %. Die zwei echten Treiber sind **ausgeglichene Stärke** und **niedrige erwartete Gesamttore** (plus Liga); kombiniert heben sie die Remisquote auf rund 32–35 %, unausgeglichene Spiele fallen auf 12–18 %. Die Remisquote eines Teams („zieht oft remis“) ist dagegen fast reines Rauschen.

### Cited Findings
- **Spannweite der Remis-Wahrscheinlichkeit (EA, Markt-Schlussquoten, 26.677 Spiele ohne Corona-Saisons)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): implizite Remis-Wahrscheinlichkeit Median 27,4 %, 5. Perzentil 15,6 %, 95. Perzentil 32,7 %, Maximum 40,8 %. Zum Vergleich Heimsieg: Median 42,5 %, Maximum 93,9 %; Auswärtssieg Maximum 93,6 %. Das Remis war nur in 161 von 26.677 Spielen (0,6 %) der wahrscheinlichste Ausgang. Wer immer den wahrscheinlichsten Ausgang tippt, liegt in 51,1 % der Spiele richtig – und tippt dabei fast nie Remis.
- **Trennschärfe (AUC) der Marktwahrscheinlichkeit je Ausgang (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Heimsieg 0,699; Auswärtssieg 0,707; **Remis 0,579**; Over 2.5 0,616.
- **Kalibrierung Remis (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Spiele mit impliziter Remis-W. ≤ 15 % endeten zu 9,8 % remis (n = 1.154); 20–22,5 % → 21,0 %; 25–27,5 % → 26,9 % (n = 5.673); 27,5–30 % → 29,0 % (n = 6.924); 30–32,5 % → 32,4 % (n = 4.646); 32,5–35 % → 33,9 % (n = 1.394); > 35 % → 31,0 % (n = 145). Es gibt also eine echte, aber schmale Spannweite (~10 % bis ~34 %).
- **Remisquote nach Ausgeglichenheit × erwarteten Gesamttoren (EA, Markt als Messlatte, 22.397 Spiele)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Ausgeglichenheit = |P(Heim) − P(Ausw.)|, erwartete Tore aus den Quoten.
  - Sehr ausgeglichen (≤ 0,10) und ≤ 2,2 erwartete Tore: **34,6 %** Remis (n = 968); ausgeglichen und 2,2–2,5 Tore: 31,1 %; ausgeglichen und > 3,1 Tore: 26,8 %.
  - Mäßig unausgeglichen (0,20–0,35) und ≤ 2,2 Tore: 33,5 %; bei > 3,1 Tore: 22,5 %.
  - Klarer Favorit (Differenz > 0,50): 12,5–21,4 % Remis, bei > 3,1 erwarteten Toren 13,1 % (n = 1.807).
- **Dasselbe nur mit Teamfeldern (EA, ohne Quoten)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Differenz Punkte/Spiel (PPG) ≤ 0,25 und niedrige Torrate beider Teams (unterstes Viertel von (Tore+Gegentore beider Teams)/2 ≤ 2,39): **31,8 %** Remis; gleiche PPG aber torreiche Teams (oberstes Viertel ≥ 2,94): 26,4 %; PPG-Differenz > 1,2: 15,8–21,6 %. AUC für Remis: kleine PPG-Differenz 0,538; niedrige Torrate 0,530; durchschnittliche Remisquote beider Teams 0,520; Markt 0,581.
- **Persistenz der Team-Remisquote (EA, 1.417 Team-Saisons)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Korrelation gerade/ungerade Spiele r = 0,05 (hochgerechnete Zuverlässigkeit für eine ganze Saison nur 0,10); Hinrunde → Rückrunde r = 0,08; Saison → nächste Saison r = 0,16 (743 Paare). Teams mit ≥ 40 % Remis in der ersten Saisonhälfte (Schnitt 45,0 %, n = 180) hatten in der zweiten Hälfte 27,1 % – exakt Ligadurchschnitt (26,6 %). Teams mit ≤ 15 % (Schnitt 9,5 %) → 23,7 %. „Letzte 6“: 0 Remis in den letzten 6 → nächstes Spiel 26,0 % Remis; 4 Remis in den letzten 6 → 27,7 % (n = 1.981) – praktisch kein Signal.
- **Saisonphase (EA, ohne Corona-Saisons)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): letzte 2 Spieltage 23,4 % Remis, 2,97 Tore/Sp, O2.5 57,7 % (n = 1.432); 3–4 Spieltage vor Ende 26,9 %; bis 10 Spieltage vor Ende 25,4–25,9 %; davor 27,0 % Remis, 2,66 Tore. Der Markt hatte die niedrigere Remisrate am Saisonende bereits eingepreist (implizit 23,9 % in den letzten 2 Spieltagen).
- **Spielverlauf (EA, alle Spiele)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): 30,4 % der Spiele stehen zur Pause 0:0; davon enden 38,5 % remis, 24,5 % 0:0, 16,6 % Over 2.5, 25,1 % BTTS.
- **Punkteregel als Anreiz**: Eine Studie über 35 Länder fand nach Einführung der 3-Punkte-Regel +8,5 % erwartete Tore und −16,2 % Remisanteil; eine bayesianische Change-Point-Analyse über sieben Ligen fand keinen Effekt auf die mittlere Torzahl, aber mehr entschiedene Spiele in den meisten Ligen — [Bayesian change-point modelling of the effects of 3-points-for-a-win rule (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9041734/). Dilger & Geyer finden im Vergleich deutscher Liga- und Pokalspiele (Differenz-in-Differenzen) weniger Remis und mehr Siege durch die 3-Punkte-Regel — [Are Three Points for a Win Really Better Than Two? (ResearchGate)](https://www.researchgate.net/publication/247739573_Are_Three_Points_for_a_Win_Really_Better_Than_Two_A_Comparison_of_German_Soccer_League_and_Cup_Games).
- **ML-Studien bestätigen**: XGBoost für die Frauen-WM 2023 – Siege/Niederlagen je ca. 0,67 Treffergenauigkeit, Remis 0,32 — [PMC12360935](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12360935/) (Länderspiele, kleiner Datensatz).
- **Wetter (Regen) und Remis**: 7.528 englische Spiele (Premier League + Championship, seit 2002): Odds Ratio für Remis je mm Regen 0,952, nicht signifikant (p = 0,165) — [opisthokonta.net](https://opisthokonta.net/?p=1066).

### Inferences
- „Remis ist am schwersten vorherzusagen“ lässt sich quantifizieren: Ein Remis ist auch im günstigsten Fall nur ca. 1:2 gegen sich (≈ 33–35 %), ein Heim- oder Auswärtssieg kann 70–90 % erreichen. Ein qualitatives Bild kann ein Remis nie „wahrscheinlichster Ausgang mit Abstand“ machen, sondern nur zwischen ~15 % und ~35 % verschieben.
- Für das Spielbild zählen zwei Fragen: (1) Sind die Teams wirklich gleich stark (PPG, Tordifferenz, SOT/xG-Differenz)? (2) Ist wenig Tore zu erwarten (beide Teams mit niedrigen Tor- und Gegentorraten, torarme Liga)? Beides zusammen ist das beste Remis-Bild; ein ausgeglichenes, aber torreiches Spiel ist deutlich weniger remisverdächtig.
- Die Teamstatistik „Remisquote“ sollte ignoriert werden – sie wiederholt sich nicht. Ebenso die Anzahl Remis in den letzten 6.
- Am letzten oder vorletzten Spieltag gibt es weniger Remis und mehr Tore (offenere Spiele); dass Teams „sich auf ein Remis einigen“, zeigt sich in den Gesamtdaten nicht.
- Ein Remis-Tipp ist mehrheitlich ein Tipp auf 1:1/2:2 – „ausgeglichen“ und „BTTS“ widersprechen sich also nicht (siehe Abschnitt 5).

### Gaps
- Keine belastbare Literatur zu Anreizen am Saisonende („nichts mehr zu spielen“, gegenseitig nützliches Remis) gefunden; nur die eigene Gesamtauswertung nach Spieltag, ohne Tabellensituation.
- Eine oft zitierte Angabe, dass auch beste Modelle/Buchmacher nur ~55 % Trefferquote erreichen, konnte keiner eindeutigen Quelle zugeordnet werden (eigene EA: 51,1 % beim Tipp auf den Markt-Favoriten).
- Stil-Paarungen (z. B. zwei tief stehende Teams) als Remis-Treiber: keine quantitative Quelle gefunden.

## 3. Was sagt torarme Spiele (Under 2.5) und Zu-Null-Spiele voraus – und wie beständig sind Zu-Null- und Ohne-Tor-Quoten?

### Takeaway
Under 2.5 und Zu-Null hängen vor allem an den **erwarteten Gesamttoren** (Tor-/Gegentorraten bzw. SOT/xG beider Teams) und an der **Angriffsschwäche des Gegners**. Wer zu Null spielt, wird besser über die Angriffsdaten des Gegners (Ohne-Tor-Quote, Tore/Schüsse aufs Tor) vorhergesagt als über die eigene Zu-Null-Quote. Zu-Null-Quoten sind nur mäßig beständig (Rückrunde regrediert etwa zur Hälfte bis zwei Dritteln zum Mittelwert); Torraten und vor allem Schüsse aufs Tor sind deutlich beständiger und sagen künftige Zu-Null-Spiele besser voraus. Regen hat keinen nachweisbaren Effekt.

### Cited Findings
- **Under 2.5 nach erwarteten Gesamttoren (EA, 22.397 Spiele, Quintile)** — [football-data.co.uk](https://www.football-data.co.uk/data.php):
  - Erwartete Tore aus Teamfeldern ((Tore Heim + Gegentore Gast)/2 + (Tore Gast + Gegentore Heim)/2, mit Heimfaktor): unterstes Fünftel (≤ 2,34) → Under 2.5 58,1 %, 0:0 10,2 %, BTTS 47,7 %, Remis 29,3 %; oberstes Fünftel (> 3,04) → Under 2.5 39,6 %, 0:0 4,9 %, BTTS 58,1 %, Remis 23,1 %.
  - Erwartete Tore aus Quoten: unterstes Fünftel (≤ 2,35) → Under 2.5 61,4 %, 0:0 11,5 %, Remis 32,2 %; oberstes (> 3,0) → Under 2.5 33,9 %, 0:0 3,2 %, Remis 19,0 %.
- **Trennschärfe für Over/Under 2.5 (EA, AUC)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Ø Over-2.5-Quote beider Teams 0,569; dieselbe nur Heimteam-zu-Hause/Gast-auswärts 0,561; Poisson aus Tor-/Gegentorraten 0,578; Poisson aus Schüssen aufs Tor (xG-Ersatz) 0,582; Markt 0,617.
- **Trennschärfe für „Heimteam spielt zu Null“ (EA, AUC)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Zu-Null-Quote des Heimteams allein 0,555; Ohne-Tor-Quote des Gastes allein 0,573; Mittel aus beiden 0,590; Poisson aus Tor-/Gegentorraten 0,607; aus SOT 0,612; Markt 0,640. Für „Gast spielt zu Null“: Zu-Null-Quote Gast 0,567; Ohne-Tor-Quote Heim 0,586; Mittel 0,606; Torraten 0,622; SOT 0,622; Markt 0,662.
- **Beständigkeit der Team-Kennzahlen (EA, 1.417 Team-Saisons, um Liga-Saison-Mittel bereinigt)** — [football-data.co.uk](https://www.football-data.co.uk/data.php):

| Kennzahl | r gerade/ungerade Spiele | hochgerechnete Zuverlässigkeit ganze Saison | r Hinrunde → Rückrunde | r Saison → nächste Saison |
|---|---|---|---|---|
| BTTS-Quote | 0,10 | 0,17 | 0,14 | 0,09 |
| Over-2.5-Quote | 0,17 | 0,29 | 0,23 | 0,29 |
| Zu-Null-Quote | 0,30 | 0,46 | 0,32 | 0,33 |
| Ohne-Tor-Quote (FTS) | 0,38 | 0,55 | 0,44 | 0,46 |
| Remisquote | 0,05 | 0,10 | 0,08 | 0,16 |
| Siegquote | 0,56 | 0,72 | 0,63 | 0,66 |
| Punkte/Spiel | 0,59 | 0,74 | 0,66 | 0,67 |
| Tore/Spiel | 0,63 | 0,78 | 0,67 | 0,70 |
| Gegentore/Spiel | 0,42 | 0,60 | 0,49 | 0,50 |
| Tordifferenz/Spiel | 0,66 | 0,80 | 0,71 | 0,72 |
| Schüsse aufs Tor für | 0,67 | 0,81 | – | 0,72 |
| Schüsse aufs Tor gegen | 0,54 | 0,70 | – | 0,59 |

- **Regression zur Mitte bei Zu-Null/Ohne-Tor (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Teams mit ≥ 45 % Zu-Null in der ersten Saisonhälfte (Schnitt 52,8 %, n = 130) → 36,4 % in der zweiten Hälfte (Gesamtschnitt 27,3 %); ≤ 15 % (Schnitt 8,8 %, n = 211) → 21,7 %. Ohne-Tor ≥ 40 % (Schnitt 46,6 %, n = 251) → 36,2 %; ≤ 15 % (8,1 %) → 17,2 %.
- **„Letzte 6“ → nächstes Spiel (EA, Teamsicht)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Zu Null in 0 der letzten 6 → nächstes Spiel 23,7 % zu Null; 3 von 6 → 29,9 %; 4 von 6 → 34,8 % (n = 2.353); 5 von 6 → 39,7 % (n = 524); Basis 27,3 %. Ohne Tor in 0 der letzten 6 → 20,8 %; 3 von 6 → 31,1 %; 5 von 6 → 33,1 % (n = 502).
- **Was sagt die Rückrunden-Quote besser voraus? (EA, Team-Saisons, nicht ligabereinigt)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Zu-Null-Quote Rückrunde: Hinrunden-Zu-Null-Quote r = 0,35; aus Hinrunden-Gegentoren abgeleitet r = 0,44; aus Hinrunden-Schüssen-aufs-Tor-gegen r = 0,45. Ohne-Tor-Quote Rückrunde: Hinrunden-Quote r = 0,46; aus Toren 0,52; aus SOT 0,54.
- **Weniger torlose Spiele als ein unabhängiges Poisson-Modell erwartet (EA)**: 0:0 beobachtet 7,44 % gegenüber 8,01 % im unabhängigen Poisson-Modell (Details Abschnitt 5) — [football-data.co.uk](https://www.football-data.co.uk/data.php).
- **Regen**: Je mm Regen +0,16 % Tore, nicht signifikant (p = 0,856), 4.826 Championship- + 2.702 Premier-League-Spiele seit 2002; der Autor findet keinen Beleg, dass Regen Tore senkt oder Remis fördert — [opisthokonta.net](https://opisthokonta.net/?p=1066).
- **Temperatur**: Eine Studie mit Spieldaten aus 10 Ländern (Kyklos, 2026) findet laut Zusammenfassung höhere Torproduktivität und bessere Schussverwertung bei wärmeren Bedingungen und schwächere Defensivleistung bei Hitze, mit Unterschieden je Liga/Klima — [Mišák, Temperature and Productivity in Soccer, Kyklos 2026](https://onlinelibrary.wiley.com/doi/10.1111/kykl.70029) (nur Abstract über Suchzusammenfassung gesehen, Volltext nicht abrufbar). Eine Studie mit UEFA-Daten 2016–2021 fand laut Suchzusammenfassung signifikante Einflüsse meteorologischer Faktoren auf offensive Leistungsvariablen, ohne einfache Tore-pro-Grad-Angabe — [PMC11474995](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11474995/) (Volltext nicht geprüft).
- Wettseiten behaupten z. B. −0,3 Tore pro Spiel bei starkem Regen oder +0,48 Tore je 10 °C, ohne nachvollziehbare Studie — [Forebet](https://www.forebet.com/en/insight/24315-how-weather-affects-football-and-match-predictions), [TopFootballTips](https://topfootballtips.com/mastering-weathers-hidden-role-in-football-predictions/) (nicht belastbar).

### Inferences
- Für „wird das torarm?“ und „spielt X zu Null?“ ist die **Angriffsstärke des Gegners** (Tore/Spiel, xG/SOT für, Ohne-Tor-Quote) das verlässlichere Signal als die eigene Zu-Null-Quote. Angriffswerte sind über die Saison stabiler (Tore/Spiel r ≈ 0,63–0,70) als Abwehrwerte (Gegentore r ≈ 0,42–0,50).
- Eine Zu-Null-Quote von über 50 % nach einer Halbserie ist im Mittel eher ~35–37 % wert; eine sehr niedrige Zu-Null-Quote ist ~20 % wert. Gegentore- bzw. xG-gegen-Werte sind die bessere Grundlage als die rohe Zu-Null-Quote.
- 4–5 Zu-Null-Spiele in den letzten 6 sind ein echtes, aber begrenztes Signal (35–40 % statt 27 %); 6 von 6 hat zu wenig Fälle, um mehr zu bedeuten.
- Heim-/Auswärts-getrennte Quoten halbieren die Stichprobe und waren in der EA etwas schlechter als die Gesamtquoten (Over 2.5: 0,561 vs. 0,569; BTTS: 0,535 vs. 0,538). Heim-/Auswärtsfelder eher ergänzend lesen, nicht als Hauptsignal.
- Wetter (Regen) ist für das Spielbild vernachlässigbar; Temperatur allenfalls ein schwacher Zusatz.

### Gaps
- Echte xG-Werte (z. B. FootyStats/Opta) konnten nicht getestet werden; SOT ist nur ein Ersatz. Erfahrungsgemäß ist xG mindestens so aussagekräftig wie SOT, aber hier nicht belegt.
- Keine quantitative Quelle zu Stil-Paarungen (Ballbesitz gegen tiefen Block, Pressingintensität) und torarmen Spielen gefunden.
- Effektgrößen der Temperatur-Studie (Kyklos 2026) nicht verfügbar. Eine in der Suche erwähnte Studie mit 64 Spielen unter Hitze-/Feuchtebelastung (Spanien), die keinen Unterschied in der Torzahl fand, konnte keiner eindeutigen Quelle zugeordnet werden.

## 4. Sind Team-Quoten wie „BTTS in 80 % der Spiele“ oder Over-2.5-% beständig – und wie schlagen sie sich gegen torbasierte/xG-basierte Erwartungen?

### Takeaway
BTTS-Quoten von Teams sind überwiegend Rauschen (Zuverlässigkeit über eine ganze Saison ≈ 0,17; Saison-zu-Saison-Korrelation 0,09); Over-2.5-Quoten sind etwas besser (≈ 0,29), aber ebenfalls schwach. Extreme Werte fallen in der nächsten Halbserie stark zum Ligamittel zurück (BTTS 76 % → 59 %; Over 2.5 75 % → 61 %). Erwartungen aus Tor- und Gegentorraten bzw. Schüssen aufs Tor sagen künftige BTTS-/Over-Quoten und einzelne Spiele besser voraus als die Prozentwerte selbst; BTTS bleibt dabei der am wenigsten vorhersagbare der untersuchten Märkte.

### Cited Findings
- **Beständigkeit (EA, 1.417 Team-Saisons)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): BTTS-Quote r gerade/ungerade 0,10, Hinrunde → Rückrunde 0,14, Saison → nächste Saison 0,09; Over-2.5-Quote 0,17 / 0,23 / 0,29 (zum Vergleich Tore/Spiel 0,63 / 0,67 / 0,70; Tabelle in Abschnitt 3).
- **Regression zur Mitte (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Teams mit BTTS ≥ 70 % in der ersten Saisonhälfte (Schnitt 75,8 %, n = 132) → 59,2 % in der zweiten Hälfte (Gesamtschnitt 52,8 %); BTTS ≤ 35 % (Schnitt 28,3 %, n = 102) → 46,3 %. Over 2.5 ≥ 70 % (Schnitt 75,2 %, n = 138) → 61,2 % (Schnitt 50,6 %); Over 2.5 ≤ 30 % (Schnitt 25,0 %, n = 101) → 42,5 %.
- **„Letzte 6“ (EA, nächstes Spiel des Teams)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): BTTS in 6 von 6 → 56,4 % BTTS im nächsten Spiel (n = 1.085); 5 von 6 → 55,9 %; 3 von 6 → 52,8 %; 0 von 6 → 47,7 % (Basis 52,8 %). Over 2.5 in 6 von 6 → 58,5 % (n = 1.016); 5 von 6 → 55,7 %; 0 von 6 → 43,6 % (Basis 50,6 %).
- **Prozentwert vs. torbasierte Erwartung für die Rückrunde (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Rückrunden-BTTS-Quote korreliert mit Hinrunden-BTTS-Quote r = 0,23, mit Poisson-Erwartung aus Hinrunden-Toren/Gegentoren r = 0,29, aus SOT r = 0,31. Rückrunden-Over-2.5: Hinrunden-Quote 0,39, aus Toren 0,42, aus SOT 0,44.
- **Einzelspiel-Vorhersage (EA, AUC, 22.397 Spiele)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): BTTS: Ø BTTS-Quote beider Teams 0,538; nur Heim-zu-Hause/Gast-auswärts 0,535; Poisson aus Tor-/Gegentorraten 0,550; aus SOT 0,554; aus Marktquoten (1X2 + O/U) abgeleitet 0,573. Over 2.5: 0,569 / 0,561 / 0,578 / 0,582 / Markt 0,617.
- **BTTS bleibt nahe 50 % (externe Daten)**: BTTS nach modellierten erwarteten Toren: < 2,0 → 47,5 % (n = 5.678); 2,0–2,5 → 50,7 %; 2,5–3,0 → 53,2 %; 3,0–3,5 → 54,9 %; ≥ 3,5 → 57,0 % (n = 10.520). Ein Poisson-Modell der Seite war stark übertrieben sicher: Prognosen von 20–25 % trafen zu 46,1 % ein (n = 1.891), Prognosen von 75–80 % zu 62,2 % (n = 1.248) — [Daily Sport Pick](https://dailysportpick.com/learn/both-teams-to-score-explained/) (Eigenangaben, Zeitraum und Ligen der Kalibrierung nicht vollständig dokumentiert; Zeilensummen inkonsistent mit genannter Gesamtzahl).
- **Kleine Stichproben**: Ein Team mit drei torreichen Spielen zeigt „100 % Over 2.5“ rein zufällig; BTTS/Over-Quoten haben mittleres Kleinstichproben-Risiko — [Performance Odds](https://www.performanceodds.com/football-stats-trends/small-sample-size-in-football-stats-when-can-you-trust-the-data/) (Ratgeberseite, qualitativ).
- **BTTS und Over 2.5 sind verschiedene Ereignisse**: 3:0 ist Over, aber kein BTTS; 1:1 ist BTTS, aber Under — [Daily Sport Pick](https://dailysportpick.com/learn/both-teams-to-score-explained/). In der EA sind 47,1 % aller Remis 1:1 (BTTS + Under) — [football-data.co.uk](https://www.football-data.co.uk/data.php).

### Inferences
- Eine Angabe wie „BTTS in 80 % der Spiele“ nach 10–15 Spielen ist realistisch eher ~58–60 % wert (etwa zwei Drittel des Abstands zum Ligamittel verschwinden). Für Over 2.5 verschwindet rund die Hälfte des Abstands.
- BTTS ist ein „Produkt“ zweier Ereignisse (Heim trifft UND Gast trifft); die Quote eines Teams mischt eigenen Angriff, eigene Abwehr und Gegnerqualität. Besser ist, beide Teilfragen getrennt zu beurteilen: trifft der Gast gegen diese Abwehr? trifft das Heimteam gegen jene Abwehr? – mit Tor-/xG-Raten und Ohne-Tor-/Zu-Null-Quoten (diese sind beständiger).
- Selbst in den klarsten Konstellationen liegt BTTS selten außerhalb von ~45–60 %. Ein qualitatives Bild sollte BTTS-Aussagen deshalb zurückhaltend formulieren.
- Heim-/Auswärts-getrennte Prozentwerte (z. B. „BTTS zu Hause 90 %“) sind wegen noch kleinerer Stichproben noch verrauschter.

### Gaps
- Kein direkter Test mit echten xG-Werten; SOT-Poisson diente als Ersatz.
- Keine wissenschaftliche Studie gefunden, die die Beständigkeit von BTTS-/Over-Quoten untersucht; die Zahlen stammen aus der eigenen Auswertung.

## 5. Poisson / Dixon-Coles: Abhängigkeit zwischen Heim- und Auswärtstoren, Häufung von 0:0 und 1:1

### Takeaway
Ein Modell mit zwei unabhängigen Poisson-Torzahlen unterschätzt Remis leicht (EA: 24,2 % statt beobachteter 26,7 %) und BTTS deutlich (48,8 % statt 52,6 %), überschätzt dagegen knappe Siege zu Null (0:1, 0:2, 2:0). Die klassische Dixon-Coles-Korrektur (negatives ρ) bildet das teilweise ab; in den aktuellen Daten ist der Effekt klein (ρ ≈ −0,05) und kommt vor allem von 1:1 und 2:2, **nicht** von zusätzlichen 0:0. Qualitativ heißt das: Spiele, in denen ein Tor fällt, ziehen oft ein Gegentor nach (Spielstand-Effekte), daher mehr „Remis mit Toren“ und mehr BTTS als eine reine Stärke-Rechnung nahelegt.

### Cited Findings
- **Beobachtet vs. unabhängiges Poisson (EA, Maher-artiges Stärkemodell je Liga-Saison, 35.459 Spiele)** — [football-data.co.uk](https://www.football-data.co.uk/data.php):

| Ergebnis | beobachtet % | unabh. Poisson % |
|---|---|---|
| 0:0 | 7,44 | 8,01 |
| 1:1 | 12,57 | 10,91 |
| 2:2 | 5,49 | 4,32 |
| 1:0 | 10,29 | 10,43 |
| 0:1 | 7,71 | 8,73 |
| 2:0 | 7,18 | 7,59 |
| 0:2 | 4,70 | 5,36 |
| 2:1 | 8,66 | 7,64 |
| 1:2 | 7,03 | 6,43 |
| Remis gesamt | 26,66 | 24,24 |
| BTTS | 52,59 | 48,78 |
| Over 2.5 | 50,12 | 48,97 |

- **Je Liga (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Remis beobachtet vs. Poisson z. B. Serie B 31,7 vs. 25,8 %; Bundesliga 24,6 vs. 21,1 %; Eredivisie 23,5 vs. 20,7 %; Premier League 23,0 vs. 22,4 %; Primeira Liga 24,4 vs. 23,6 %. 1:1 ist in allen 12 Ligen häufiger als erwartet (z. B. Serie B 15,9 vs. 11,8 %, Bundesliga 11,9 vs. 9,5 %); 0:0 ist in 9 von 12 Ligen seltener als erwartet.
- **Korrelation und ρ (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): rohe Korrelation Heimtore/Auswärtstore −0,050 (Stärkeunterschiede: Ein starkes Team schießt viel und kassiert wenig); nach Herausrechnen der Teamstärken +0,026. Dixon-Coles-ρ (Profil-Likelihood) über alle Ligen −0,05; je Liga von −0,14 (Bundesliga), −0,11 (Serie B), −0,09 (Eredivisie, 2. Bundesliga) bis +0,03 (Primeira Liga).
- **Literatur**: Maher (1982) ergänzte eine bivariate Poisson-Variante, weil das unabhängige Modell „tends to underestimate the proportion of draws“; Dixon & Coles (1997) führten ρ ein, das nur die Felder 0:0, 1:0, 0:1, 1:1 verändert — [Petretta et al., On the dependence in football match outcomes (arXiv 2103.07272)](https://arxiv.org/html/2103.07272v2).
- **Neuere Prüfung (Petretta et al.)**: 9.130 Spiele der Top-5-Ligen 2014/15–2018/19: Pearson-Korrelation Heim-/Auswärtstore −0,085 (p < 0,001); Poisson-Randverteilungen werden wegen Überdispersion verworfen (p < 0,001); beobachtet/unabhängig-Verhältnisse für Remis-Ergebnisse 99,5 % (0:0), 102,1 % (1:1), 102,7 % (2:2); die Autoren schreiben, die Abhängigkeit sei anders als „observed by Dixon and Coles at the time“ — [arXiv 2103.07272](https://arxiv.org/html/2103.07272v2).
- **Wirkrichtung von ρ**: negatives ρ erhöht 0:0 und 1:1 und senkt 1:0/0:1; alles, was an diesen vier Feldern hängt (Remis, Under 2.5, BTTS Nein), erbt den Fehler eines unabhängigen Modells — [StatsUltra](https://statsultra.com/dixon-coles-model/), [pena.lt](http://www.pena.lt/y/2021/06/24/predicting-football-results-using-python-and-dixon-and-coles/). Typischer Bereich in Top-Ligen laut Rechner-Doku ρ ≈ −0,15 bis −0,05 — [MetricGate](https://metricgate.com/docs/dixon-coles-soccer-model/) (Sekundärquelle).
- **ρ kann auch positiv sein**: Michels et al. (2025) zeigen, dass das Modell Wahrscheinlichkeit auch in die Gegenrichtung (weniger Remis) verschieben kann, wie in jüngeren Champions-League-Saisons — [arXiv 2508.20075](https://arxiv.org/pdf/2508.20075).
- **Karlis & Ntzoufras (2003)**: bivariates Poisson-Modell mit Diagonal-Inflation, damit Remis-Ergebnisse besser kalibriert sind als im unabhängigen Modell — [Analysis of sports data using bivariate Poisson models (ResearchGate)](https://www.researchgate.net/publication/227719079_Analysis_of_sports_data_using_bivariate_Poisson_models); Karlis & Ntzoufras (2000) fanden Überdispersion über 456 Teams in 24 Ligen — [arXiv 2103.07272](https://arxiv.org/html/2103.07272v2).
- **Spielstand-Effekte als Mechanismus**: Premier League 2013/14 – zurückliegendes Team (−1) hat 53,4 % Schussanteil, führendes (+1) 46,6 %; das führende Team erzielt in diesem Zustand trotzdem 52,9 % der Tore (Konter, „defensive shell“) — [StatsBomb, Score Effects](https://blogarchive.statsbomb.com/articles/soccer/score-effects/) (eine Saison, ca. 3.500 Schüsse). Skripnikov et al. (2026) finden einen überwiegend monoton negativen Effekt von Tor- und Rote-Karten-Differenz auf xG/SOT pro Minute (Führung → weniger eigene Chancen) — [SAGE, Adjusting xG and SOT for game context](https://journals.sagepub.com/doi/10.1177/22150218261454824) (nur Abstract/Snippet gesehen).

### Inferences
- Wer das Spielbild aus „Tore Heim erwartet × Tore Gast erwartet“ (Poisson-Logik) ableitet, sollte qualitativ nachjustieren: etwas mehr Remis (v. a. 1:1/2:2), mehr BTTS, weniger knappe Siege zu Null des Außenseiters bzw. Auswärtsteams (0:1/0:2 sind am stärksten überschätzt).
- Der Mechanismus ist plausibel der Spielstand: Nach einem Tor drängt das zurückliegende Team (mehr Schüsse), das führende kontert – beide Seiten treffen öfter. Ein 0:0 ist nicht „extra wahrscheinlich“; die alte Dixon-Coles-Geschichte (mehr 0:0) gilt in aktuellen Daten kaum.
- Die Unterschätzung ist ligaabhängig: groß in Serie B, Bundesliga, Eredivisie, 2. Bundesliga; klein in Premier League und Portugal.

### Gaps
- Der Originalwert von ρ aus Dixon & Coles (1997) und die Inflationsparameter aus Karlis & Ntzoufras (2003) konnten nicht im Original eingesehen werden.
- Das eigene Stärkemodell wurde in-sample je Saison geschätzt; Überanpassung macht die Stärkeunterschiede etwas zu groß und könnte die Remis-Unterschätzung leicht übertreiben (die 0:0-Überschätzung spricht aber gegen eine reine Artefakt-Erklärung). Petretta et al. finden mit einer anderen Methode nur ~2–3 % mehr 1:1/2:2 als unabhängig erwartet.

## 6. Favorit gegen Außenseiter: Wie oft gewinnt ein klarer Favorit zu Null – und was unterscheidet ein kontrolliertes von einem offenen Spiel?

### Takeaway
Ein klarer Favorit (≥ 60 % Siegwahrscheinlichkeit) gewinnt in ~73 % der Spiele, aber nur in ~41 % zu Null; der Außenseiter trifft in ~55 % dieser Spiele. Erst bei ≥ 80 % Favoritenstellung sinkt die Trefferquote des Außenseiters unter 50 %. Ob der Favorit „kontrolliert“ (zu Null) gewinnt, hängt an **Angriffsschwäche des Außenseiters** und **Abwehrstärke des Favoriten** – nicht am Angriff des Favoriten. Hohe erwartete Gesamttore bedeuten: Favorit gewinnt öfter, kassiert aber öfter (offenes Spiel).

### Cited Findings
- **Favoritenausgänge nach Siegwahrscheinlichkeit (EA, Markt als Stärkemaß, 35.459 Spiele, Quotenabdeckung 99,9 %)** — [football-data.co.uk](https://www.football-data.co.uk/data.php):

| Favoriten-Siegwahrsch. | n | Sieg % | Remis % | Niederlage % | Sieg zu Null % | Sieg mit Gegentor % | Außenseiter trifft % | Anteil Siege zu Null % |
|---|---|---|---|---|---|---|---|---|
| ≤ 45 % | 15150 | 40,0 | 30,5 | 29,5 | 21,9 | 18,1 | 69,0 | 54,7 |
| 45–50 % | 5622 | 47,3 | 29,5 | 23,2 | 26,0 | 21,3 | 65,2 | 54,9 |
| 50–55 % | 4238 | 52,1 | 27,2 | 20,6 | 29,6 | 22,5 | 63,3 | 56,8 |
| 55–60 % | 3409 | 57,7 | 24,8 | 17,5 | 31,8 | 25,9 | 62,1 | 55,1 |
| 60–65 % | 2254 | 64,4 | 21,2 | 14,4 | 35,8 | 28,7 | 59,5 | 55,5 |
| 65–70 % | 1669 | 70,5 | 17,5 | 12,0 | 41,6 | 28,9 | 54,8 | 59,0 |
| 70–75 % | 1279 | 75,1 | 16,7 | 8,1 | 41,1 | 34,0 | 55,0 | 54,7 |
| 75–80 % | 886 | 79,8 | 13,2 | 7,0 | 43,8 | 36,0 | 54,5 | 54,9 |
| > 80 % | 928 | 86,3 | 8,6 | 5,1 | 50,4 | 35,9 | 48,0 | 58,4 |

- **Heim- vs. Auswärtsfavorit (≥ 60 %, EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Heimfavorit (n = 5.304): Sieg 72,8 %, Sieg zu Null 41,6 %, Sieg mit Gegentor 31,2 %, Außenseiter trifft 54,6 %. Auswärtsfavorit (n = 1.712): Sieg 72,2 %, zu Null 39,4 %, mit Gegentor 32,8 %, Außenseiter trifft 57,8 %.
- **Signale innerhalb klarer Favoriten (≥ 60 %, beide Teams ≥ 6 Spiele, n = 4.535; Sieg zu Null 41,0 %) – AUC für „Favorit gewinnt zu Null“ (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): aus Quoten abgeleitete erwartete Tore des Außenseiters (niedrig) 0,584; Gegentore/Spiel des Favoriten (niedrig) 0,550; SOT für des Außenseiters (niedrig) 0,549; SOT gegen des Favoriten (niedrig) 0,546; Zu-Null-Quote Favorit 0,545; Siegwahrscheinlichkeit Favorit 0,544; Tore/Spiel Außenseiter (niedrig) 0,541; BTTS-Quote Favorit bzw. Außenseiter (niedrig) je 0,535; Ohne-Tor-Quote Außenseiter 0,533; erwartete Gesamttore (niedrig) 0,524; **Tore/Spiel des Favoriten 0,504 und Gegentore/Spiel des Außenseiters 0,500 = kein Signal**.
- **Drittel-Vergleiche (EA, je ~1.510 Spiele)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): Außenseiter mit wenig SOT (Ø 3,0/Spiel) → Favorit gewinnt zu Null 45,8 %, Außenseiter trifft 49,9 %; viel SOT (Ø 4,7) → 36,0 %, trifft 60,9 %. Favorit mit hoher Zu-Null-Quote (Ø 52,7 %) → 45,0 %; niedriger (Ø 22,1 %) → 36,9 %. Favorit lässt wenig SOT zu (Ø 2,7) → 45,6 %; viel (Ø 4,5) → 36,2 %. Außenseiter mit hoher Ohne-Tor-Quote (Ø 47,5 %) → 44,4 %; niedriger (Ø 19,4 %) → 38,1 %. Niedrige erwartete Gesamttore (Ø 2,69) → zu Null 44,2 %, Sieg 69,4 %; hohe (Ø 3,59) → zu Null 39,1 %, Sieg 76,3 %, Außenseiter trifft 59,2 %.
- **Kombination (EA)** — [football-data.co.uk](https://www.football-data.co.uk/data.php): schwacher Außenseiter-Angriff (SOT unterstes Drittel) + starke Favoriten-Abwehr (SOT gegen unterstes Drittel): **49,7 %** Sieg zu Null (n = 467); starker Außenseiter-Angriff + schwache Favoriten-Abwehr: **30,6 %** (n = 474); dazwischen 36–48 %.
- **Spielstand-Mechanismus**: Führende Teams geben Schussanteile ab (46,6 % bei +1) — [StatsBomb, Score Effects](https://blogarchive.statsbomb.com/articles/soccer/score-effects/). Das erklärt, warum auch dominante Favoriten oft noch ein Gegentor kassieren.

### Inferences
- „Favorit gewinnt“ und „Favorit gewinnt zu Null“ sind sehr verschiedene Aussagen: Bei 60–75 % Favoritenstellung trifft der Außenseiter trotzdem in 55–60 % der Spiele. Ein Sieg zu Null ist selbst bei klaren Favoriten meist < 50 %.
- Ein **kontrolliertes Spiel** erkennt man am Profil: Außenseiter mit wenig Torschüssen/xG und vielen Spielen ohne Tor + Favorit mit wenig zugelassenen Schüssen/xG gegen. Ein **offenes Spiel**: torreiche Teams, Außenseiter mit ordentlichem Angriff, Favorit mit durchlässiger Abwehr – der Favorit gewinnt dann sogar etwas öfter, aber häufiger mit Gegentor.
- Die Offensivstärke des Favoriten sagt etwas über „Sieg ja/nein“, aber nichts über „zu Null“; für Zu-Null-Fragen zählt die Gegenseite (Angriff des Außenseiters) und die eigene Abwehr.
- Auswärtsfavoriten kassieren etwas häufiger als gleich starke Heimfavoriten (Außenseiter trifft 57,8 % vs. 54,6 %) – passend zur bekannten Heim-Anfälligkeit-Frage: auch ein schwaches Heimteam trifft zu Hause relativ oft.

### Gaps
- Keine Literatur gefunden, die „Spielkontrolle“ von Favoriten (z. B. Ballbesitz, Feldneigung) direkt mit Siegen zu Null verknüpft; die Aussagen stammen aus der eigenen Auswertung mit SOT als Ersatz für xG.
- Favoritenstellung wurde über Quoten gemessen (als bestes verfügbares Stärkemaß); mit reinen Teamfeldern (PPG, xG-Differenz) dürften die Muster ähnlich, aber etwas schwächer ausfallen – nicht separat getestet.
