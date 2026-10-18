# Team-Kennzahlen jenseits von Saison-xG, Toren und Gegentoren – was verbessert das Spielbild?

Hinweis zur Quellenlage (Stand 18.10.2026): Die belastbarsten Zahlen gibt es zu (a) xG vs. Tore/Schüsse/Torschüsse als Prognose künftiger Punkte/Tore, (b) Persistenz von Abschluss- und Torwart-Über-/Unterperformance. Zu PPDA, Field Tilt, „gefährlichen Angriffen" und zu Spielständen gibt es fast nur beschreibende oder gleichzeitige (nicht prognostische) Korrelationen. Zu BTTS/Over 2.5 speziell habe ich keine Studie gefunden, die einzelne Team-Kennzahlen auf ihren Prognosewert testet.

## 1. npxG vs. xG, xG pro Schuss, Schüsse und Torschüsse vs. Tore und xG – was sagt künftige Tore/Ergebnisse am besten voraus?

### Takeaway
xG-Verhältnis (xG / (xG + xGA)) ist in Europas Top-5-Ligen über die ganze Saison der beste Einzelprädiktor für künftige Punkte und Tore; danach kommen Tor-Verhältnis und Torschuss-Verhältnis, das reine Schuss-Verhältnis (TSR) ist am schwächsten. Der Vorsprung von xG ist in neueren Daten aber kleiner geworden (≈ 8 Spiele bis xG klar besser ist als Punkte), und xGOT (Post-Shot-xG) prognostiziert schlechter als normales xG.

### Cited Findings
- Original 11tegen11-Studie (Sander IJtsma, Jan. 2015; Top-5-Ligen 2012/13–2013/14 + Eredivisie 2013/14, Spiel-für-Spiel-Korrelation mit künftigen Punkten pro Spiel): xG-Verhältnis hatte die höchste Spitzenkorrelation mit künftigen Punkten; nach 4 Spielen war xG so prädiktiv wie das Tor-Verhältnis an seinem Höchstpunkt; klarer Vorsprung vor TSR und anderen Kennzahlen. Archiv: http://web.archive.org/web/20181112175811/http://www.11tegen11.com/2015/01/05/the-best-predictor-for-future-performance-is-expected-goals/ — zusammengefasst in [ASA Replication Project 2022](https://www.americansocceranalysis.com/home/2022/7/19/the-replication-project-is-xg-the-best-predictor-of-future-results)
- ASA-Replikation (Eliot McKinley, 2022; Top-5-Ligen 14.608 Spiele seit 2017/18 ohne 2020, MLS 2.516 Spiele; 1.000 Bootstrap-Reihenfolgen je Team): xG-Verhältnis bleibt zu jedem Saisonzeitpunkt bester Prädiktor künftiger Punkte; aber der Abstand ist kleiner geworden; die 2015 klare Trennung zwischen „dummen" (Punkte, Tore) und „klügeren" Kennzahlen (TSR, Torschuss-Verhältnis) ist in neueren Daten kaum noch sichtbar; Schuss-Kennzahlen waren nicht klar besser als Ergebnis-Kennzahlen. xG ist in Europa erst nach ≈ 8 Spielen (MLS ≈ 7) besser als Punkte pro Spiel (2015: nach 4). MLS ist für jede Kennzahl deutlich weniger vorhersagbar. Eine argentinische Analyse (Howard Hamilton, 2015–16) fand xG nicht überlegen. — [ASA 2022](https://www.americansocceranalysis.com/home/2022/7/19/the-replication-project-is-xg-the-best-predictor-of-future-results)
- Tony ElHabr (FBref/Opta, Big 5 + MLS, 2018–2024 ohne 2020, 25.416 Team-Spiel-Zeilen; laufendes R² zwischen bisherigen und restlichen Saisonwerten): Erster Spieltag mit R² > 0,5 (Big 5) – xG-Verhältnis: 9 (künftiges Tor-Verhältnis) / 13 (künftige Punkte pro Spiel); Tor-Verhältnis: 11 / 15; Torschuss-Verhältnis: 12 / 16; Punkte pro Spiel: 13 / 16; Schuss-Verhältnis (TSR): nie. xGOT-Verhältnis schneidet „nicht annähernd so gut" ab wie xG-Verhältnis; Torschuss-Verhältnis ist prädiktiver als TSR. xG + xAG erreicht die Schwelle schon an Spieltag 7 / 10 (zählt aber Torbeteiligungen doppelt). Gebootstrapte R² liegen „etwas niedriger", >0,5 meist erst um Spieltag 15–20. Keine Konfidenzintervalle. — [ElHabr: Expected goals, gamestate, and predictiveness](https://tonyelhabr.rbind.io/posts/xg-predictor-future-results/)
- Tiotal Football fand (MLS) „goals added" und erfolgreiche Pässe in den Strafraum prädiktiver für künftige Punkte als xG – ohne Zahlen, nur zitiert. — [ElHabr](https://tonyelhabr.rbind.io/posts/xg-predictor-future-results/)
- PLOS ONE (Mead, O'Hare, McMenemy 2023): eigenes xG-Modell übertraf rohe Schüsse und Tore als Prädiktor in jeder Liga und jedem Maß, mit einer Ausnahme (ein Präzisionswert in der Serie A). — [PLOS ONE 2023](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0282295)
- Brechot & Flepp (2020, Journal of Sports Economics 21(4)): xG-basierte Maße sagen künftige Spielergebnisse in europäischem Klubfußball signifikant besser voraus als reine Ergebnismaße. — zitiert in [Böttger/Vischer 2026, Uni Münster DP 3/2026](https://d-nb.info/1400733782/34)
- Gegenstimme: Wheatcroft (arXiv 2001.09097) – es sei „nicht notwendigerweise" so, dass vorhergesagte xG Prognosen/Ratings auf Basis anderer Statistiken (Schüsse, Torschüsse, Ecken) schlagen. — [arXiv 2001.09097](https://arxiv.org/pdf/2001.09097)
- Hudl/StatsBomb: auf Teamebene sind xG-Modelle prädiktiver als aktuelle Tordifferenz und reine Schusszahl-Kennzahlen wie TSR. — [Hudl: What are xG](https://www.hudl.com/blog/expected-goals-xg-explained)
- Spielerebene: „Shots over expected" (mehr Schüsse als die Spielsituation erwarten lässt) hat Jahr-zu-Jahr-Korrelation ≈ 0,63, „goals over expected" (Tore minus xG) nur ≈ 0,12 – die wiederholbare Fähigkeit liegt eher im Erzeugen von Schüssen/Chancen als im Verwandeln. (Preprint, Premier League) — [arXiv 2512.00203](https://arxiv.org/pdf/2512.00203)
- Marcel-Projektionen (Spielerebene): xG/xA projizieren künftige Tore/Vorlagen besser als Tore/Vorlagen selbst; reine Schusszahlen korrelieren deutlich schlechter mit Nicht-Elfmeter-Toren der Folgesaison. — [Expecting Goals: Building Marcel](https://www.expectinggoals.com/p/building-marcel-part-1-addendum-expected)

### Inferences
- Rangfolge fürs Spielbild (Teamebene, Saison läuft): xG-Differenz/xG-Verhältnis > Tor-Differenz ≈ Torschuss-Verhältnis > Punkte > reine Schusszahl. Vor ≈ Spieltag 8–10 ist jede Kennzahl stark verrauscht; früh in der Saison Vorjahres-/Kaderinfos stärker gewichten.
- xG und Tore sind keine Gegensätze: Nach vielen Spielen konvergieren Tor- und xG-Verhältnis im Prognosewert; Tore enthalten zusätzlich etwas echtes Abschluss-/Torwart-Können (siehe Abschnitt 5). Praktisch: beides lesen, aber bei großer Lücke eher xG trauen.
- Torschüsse sind besser als alle Schüsse, weil sie einen Teil der Schussqualität enthalten; xGOT/Post-Shot-xG enthält dagegen mehr Abschluss-Zufall und ist deshalb schlechter als Prognose (gut zur Beschreibung, schlecht zur Vorhersage).
- Viele Schüsse bei niedriger xG/Schuss (z. B. Distanzschüsse) sind kein Qualitätssignal; ein Team mit wenigen, aber guten Chancen ist eher unterschätzt, wenn man nur auf Schusszahlen schaut.

### Gaps
- Keinen direkten, quantitativen Vergleich npxG vs. xG als Prädiktor auf Teamebene gefunden. (Die Münster-Studie verwendet npxG, ohne Vergleich.) Begründung, warum npxG oft bevorzugt wird (Elfmeter = seltene, hoch bewertete, zufallsbehaftete Ereignisse), ist plausibel, aber hier nicht mit einer Zahl belegt.
- Keine Teamstudie zum eigenständigen Prognosewert von xG pro Schuss (Schussqualität) zusätzlich zu xG gefunden.
- Keine Studie zur Prognose von Over/Under 2.5 oder BTTS mit diesen Kennzahlen; Evidenz bezieht sich auf Punkte/Tor-Verhältnis.
- Exakte R²-Kurven der ASA-Replikation sind nur als Grafik verfügbar.

## 2. Standardsituationen: Anteil an Toren, Stabilität der Team-Standardstärke, Bedeutung für Torprognosen

### Takeaway
Standards (ohne Elfmeter) machen in der Premier League etwa ein Fünftel bis gut ein Viertel aller Tore aus (2024/25: 20,6 %, 2025/26: 27,4 %); die Standard-xG-Differenz hängt stark mit Punkten zusammen (ρ ≈ +0,64 über 96 Teams), aber eine veröffentlichte Saison-zu-Saison-Wiederholbarkeit der Team-Standardstärke habe ich nicht gefunden.

### Cited Findings
- Premier League 2025/26: 27,4 % aller Tore aus Nicht-Elfmeter-Standards – zweithöchster Anteil in 34 PL-Spielzeiten; Vorsaison 20,6 %. (Ein Opta-Text zur Saisonmitte nannte noch 30,0 %.) Arsenal: 25 Nicht-Elfmeter-Standardtore (Ecken, indirekte/direkte Freistöße, Einwürfe), 17 Eckentore = PL-Rekord (vorher 16: Arsenal 2023/24, West Brom 2016/17, Oldham 1992/93). — [Opta Analyst: Arsenal corners record](https://theanalyst.com/articles/arsenal-most-goals-from-corners-premier-league-season-record); [Opta Analyst: set piece/throw-in stats](https://theanalyst.com/articles/premier-league-delays-set-piece-throw-in-stats)
- Häufig zitierte Faustregel „rund 30 % der Tore aus Standards" – vom Autor selbst nicht verifiziert. — [Dreamdataball: Why bother analysing set pieces?](https://dreamdataball.substack.com/p/why-bother-analysing-set-pieces)
- Standard-xG-Differenz pro Spiel vs. Punkte pro Spiel, 96 Teams aus 5 Ligen (PL, Serie A, Bundesliga, 2. Bundesliga, 3. Liga), eine Saison 2025/26: Spearman ρ = +0,64, R² = 0,46, p = 2,7e-12. Je Liga: Serie A +0,83; Bundesliga +0,65; 3. Liga +0,62; PL +0,56; 2. Bundesliga +0,42 (p = 0,09, nicht signifikant). Autor: nur Zusammenhang, keine Kausalität (starke Teams lassen auch weniger Standards zu); keine Jahr-zu-Jahr-Wiederholbarkeit berichtet; Definition der Standard-xG im Text unklar. Beispiele: Inter 29 Standardtore (nächstbestes Team Napoli 18); Arsenal Standard-xG-Differenz +0,385/Spiel vs. +0,114 (Man City, Zweiter). — [Dreamdataball](https://dreamdataball.substack.com/p/why-bother-analysing-set-pieces)
- Künftige Standardtore (Spielerebene) hängen enger mit der bisherigen Standard-Schussproduktion zusammen als mit der Gesamt- oder Open-Play-Schussproduktion; Autor warnt, Korrelationen seien grob und varianzbehaftet. — [Expecting Goals: Predicting Set Piece Goals and Assists](https://www.expectinggoals.com/p/predicting-set-piece-goals-and-assists)
- Paul Power (Sloan 2018, laut ESPN): Open-Play-Ballbesitze führen in 1,1 % der Fälle zu einem Tor, Standards in 1,8 %. — [ESPN: How set pieces are ruining Premier League](https://www.espn.com/soccer/story/_/id/46662849/set-pieces-ruining-premier-league-helping-arsenal-throw-ins)

### Inferences
- Standardstärke ist ein eigener Baustein des Bildes, der in Saison-xG bereits steckt (Standard-xG zählt mit), aber verdeckt sein kann: Ein Team mit mäßiger Open-Play-xG und starker Standard-xG kann gegen tief stehende Gegner trotzdem treffen – relevant für BTTS/Over, wenn der Außenseiter standardstark ist.
- Standard-Tore allein (ohne Standard-xG) sind sehr klein-stichprobig und verrauscht; Standard-xG/-Schüsse sind die verlässlichere Lesart. Plausibel stabil ist Standardstärke dort, wo sie an Personal (Kopfballspieler, Schützen) und Trainerteam hängt – bei Trainer-/Kaderwechsel neu bewerten.
- Der Anteil schwankt zwischen Saisons/Ligen (PL 20,6 % → 27,4 % in einem Jahr) – ligaweite Trends beachten.

### Gaps
- Keine veröffentlichte Saison-zu-Saison-Korrelation der Team-Standard-xG (für/gegen) gefunden – Persistenz der Team-Standardstärke ist daher nicht quantifiziert.
- Keine Studie, die Standard-xG als zusätzlichen Prädiktor künftiger Tore über Gesamt-xG hinaus testet.
- Kaum Daten zu zweiten Ligen jenseits der einen Dreamdataball-Saison.

## 3. Pressing und Territorium: PPDA, Field Tilt, Ballbesitz, (gefährliche) Angriffe – Prognosewert über xG hinaus?

### Takeaway
Es gibt keine Studie, die zeigt, dass PPDA, Field Tilt, Ballbesitz oder „gefährliche Angriffe" künftige Ergebnisse oder Tore über xG hinaus vorhersagen. Vorhandene Zahlen sind gleichzeitige Korrelationen: Bedrohungs-gewichteter Ballbesitz hängt deutlich stärker mit Tordifferenz/xG zusammen als reiner Ballbesitz; Field Tilt korreliert nur schwach mit Punkten.

### Cited Findings
- ASA (2019): bedrohungsgewichtete Ballbesitz-Kennzahl („Chance xPG") korreliert mit der Tordifferenz r ≈ 0,73, reiner ballkontaktbasierter Ballbesitz nur ≈ 0,52 (gleichzeitig, nicht prognostisch; MLS). — [ASA: xPG is Back, Baby!](https://www.americansocceranalysis.com/home/2019/9/11/xpg-is-back-baby-putting-possession-metrics-to-the-correlation-test)
- Preprint 2026 (Broadcast-Daten): bedrohungsgewichteter Ballbesitz folgt xG etwas besser als reiner Ballbesitz (0,56 vs. 0,50); Field Tilt korreliert schwach mit Punkten (0,18); nur gleichzeitige Maße. — [arXiv 2608.09887](https://arxiv.org/pdf/2608.09887)
- Ein aus PPDA abgeleiteter Ballbesitz-Proxy korreliert ≈ 0,77 mit dem xG-Anteil eines Teams – starke Überlappung mit xG. — [Inganci Research](https://inganci.com/research/possession-adjustment)
- Informelle Analyse: Teams mit > 50 % Ballbesitz erzielen mehr Tore, aber mit breiterer Streuung; Ballbesitz korreliert stärker mit xG als mit Toren; keine Kontrolle für xG. — [Medium: Ball possession and points](https://medium.com/@enmlowe/ball-possession-and-points-causality-or-correlation-a-first-analysis-eacc974ad557)
- Erfolgreiche Pässe in den Strafraum (eine Territoriums-/Strafraumpräsenz-Kennzahl) wurden in der MLS als prädiktiver für künftige Punkte als xG beschrieben (Tiotal Football, ohne Zahlen). — [ElHabr](https://tonyelhabr.rbind.io/posts/xg-predictor-future-results/)
- Ballbesitz ist spielstandabhängig (siehe Abschnitt 4): Spielstand verzerrt Ballbesitz, Schusszahlen und xG. — [The Football Analyst: Game State and Stats](https://the-footballanalyst.com/game-state-and-stats-how-the-scoreline-skews-the-numbers/)
- Field-Tilt-Definitionen unterscheiden sich je Anbieter (Anteil Pässe im letzten Drittel vs. Spielanteil in der gegnerischen Hälfte). — [Medium: 12 Football Stats Explained](https://medium.com/@thefootballgazette/12-stats-that-explain-football-and-where-they-fail-413aa28b03a8)

### Inferences
- PPDA und Field Tilt beschreiben den Spielstil (hohes Pressing, Dominanz), nicht direkt die Qualität; da sie stark mit xG überlappen, liefern sie vermutlich wenig zusätzliche Prognose, wenn xG schon vorliegt. Nützlich eher als Kontext: Ein Team mit hohem Field Tilt/niedriger PPDA, aber niedriger xG „dominiert steril"; hoher Ballbesitz ohne Strafraumpräsenz ist kein Stärkesignal.
- Ballbesitz und Territorium sind stark vom Spielstand gefärbt (Führende geben Ball ab) – Saisonwerte von Teams, die oft führen, unterschätzen ihre Dominanz und umgekehrt.
- „Gefährliche Angriffe" (Datenanbieter-Zählung aus Live-Feeds) sind uneinheitlich definiert; ohne Studienbeleg höchstens als grober Druck-Indikator lesen.

### Gaps
- Keine Studie gefunden, die PPDA, Field Tilt, Ballbesitz oder gefährliche Angriffe gegen künftige Punkte/Tore unter Kontrolle von xG testet (zusätzlicher Prognosewert unbekannt).
- Keine Daten zur Saison-zu-Saison-Stabilität von PPDA/Field Tilt gefunden.
- Ein ResearchGate-Paper („Hierarchical and Mediation Analysis of Expected Goals and Pressing Intensity Across Top European Football Leagues") soll laut Suchsnippet xG und Tore als vergleichbar prädiktiv für die Folgesaison finden – nicht verifiziert, PPDA-Ergebnisse unbekannt.

## 4. Spielstandseffekte: Verhalten bei Führung/Rückstand, „Game Management", Favoriten, Bedeutung für Torzahl und BTTS; Lesart von „erstes Tor %", „Punkte nach 0:1", Halbzeitführungen

### Takeaway
Führende Teams schießen seltener, aber mit leicht besserer Chancenqualität und höherer Verwertung (Konter gegen aufgerückte Gegner); zurückliegende Teams schießen mehr, aber aus schlechteren Positionen. Das Team, das zuerst trifft, gewinnt in Europa rund 66–71 % der Spiele, Top-Teams aber rund 87–90 % – „erstes Tor"-Quoten sind daher vor allem ein Stärke-Proxy. xG aus Phasen mit ≥ 2 Toren Abstand hat praktisch keinen Prognosewert.

### Cited Findings
- Teams bei −1/−2 schießen tendenziell mehr als der Gegner; Teams mit 3+ Toren Rückstand werden klar überschossen; bei −2 mehr Schüsse, aber weniger aufs Tor (Distanz, schlechte Winkel); führende Teams verwerten einen höheren Anteil ihrer Schüsse (Gegner rückt auf → Konterräume). Michael Caley: Spielstand beeinflusst die xG regulärer Schüsse signifikant, aber der Effekt ist klein; Führende haben etwas bessere Chancen (vermutlich weniger Druck auf den Schützen). Daten v. a. PL 2015/16, keine Stichprobengrößen. Weiterführende Quellen dort: 11tegen11 „Game states and conversion" (2013, http://11tegen11.net/2013/04/06/game-states-and-conversion/), Ben Pugsley „Score effects" (StatsBomb 2013, http://statsbomb.com/2013/12/score-effects/). — [One Short Corner: Game states and score effects (2016)](https://oneshortcorner.wordpress.com/2016/04/12/football-analytics-part-five-game-states-and-score-effects/)
- Dixon & Robinson (1998, The Statistician 47(3)): Torraten steigen im Spielverlauf und hängen vom aktuellen Spielstand ab (Score-State-Multiplikatoren im Birth-Process-Modell). — [arXiv 2003.10294 (Zusammenfassung)](https://arxiv.org/pdf/2003.10294); [arXiv 2605.16066](https://arxiv.org/pdf/2605.16066)
- Spielstand-gefiltertes xG prognostiziert nicht besser: xG nur bei Unentschieden verringert den Prognosewert für künftige Punkte (wirft > 50 % der Daten weg); xG bei |Tordifferenz| ≤ 1 (83,1 % der Spielminuten) ist etwa so gut wie Gesamt-xG; xG bei |Tordifferenz| > 1 (16,1 % der Minuten) hat R² ≈ 0 über alle Spieltage. — [ElHabr](https://tonyelhabr.rbind.io/posts/xg-predictor-future-results/)
- CIES Football Observatory (92 Ligen, 1.1.2015–31.12.2019): Team mit dem ersten Tor gewinnt im Schnitt knapp 70 %; Premier League 71,1 % (höchster Big-5-Wert), Bundesliga 67,8 % (niedrigster Big-5-Wert), Belgien und Norwegen je 66,3 % (niedrigste in Europa). Klubebene: PSG 124/138 (89,9 %), Barcelona 116/131 (88,5 %), Man City 115/132 (87,1 %); Central Coast Mariners nur 20/53 (38 %); niedrige Big-5-Werte u. a. Toulouse, Augsburg, Udinese, Eibar, Southampton. — [CIES Weekly Post 293](https://football-observatory.com/IMG/sites/b5wp/2019/wp293/en/)
- Vollspiel-Summen mischen Spielstände: Ballbesitz, Schusszahlen und xG können durch den Spielstand aufgebläht oder gedrückt sein; „mehr Schüsse" heißt nicht automatisch „besseres Team". — [The Football Analyst](https://the-footballanalyst.com/game-state-and-stats-how-the-scoreline-skews-the-numbers/)
- Spielstand-xG-Aufteilung (führend/unentschieden/zurück) als Beschreibungsmittel, Fallstudie Malmö; Schussdistanz verschiebt sich mit dem Spielstand. — [Waltzing Analytics: Gamestate xG](https://marclamberts.substack.com/p/gamestate-xg-score)

### Inferences
- Für Torzahl/BTTS: Führt der Favorit früh, sinkt sein Schussvolumen, der Außenseiter muss öffnen – das erhöht die Konterchancen des Favoriten (höhere Verwertung bei Führung) und gibt dem Außenseiter mehr, aber schlechtere Schüsse. BTTS hängt dann stark davon ab, ob der Außenseiter auch aus schlechteren Lagen/Standards trifft. Ein „Game-Management"-Favorit (verwaltet 1:0) drückt die Gesamttore; ein Favorit, der bei Führung weiter angreift, treibt Over. Das ist mechanistisch plausibel, aber nicht mit Teamzahlen zur BTTS-Prognose belegt.
- „Erstes Tor erzielt %"/„Sieg nach Führung %"/„Punkte nach 0:1": Weil der Ligadurchschnitt bei ≈ 70 % liegt und Top-Teams ≈ 88–90 % erreichen, messen diese Felder großteils Teamstärke, nicht eine eigene „Mentalität". Auffällig sind nur deutliche Abweichungen vom für die Stärke erwartbaren Wert – und auch die sind bei 10–20 Ereignissen pro Saison klein-stichprobig. Nicht doppelt zählen, wenn xG-Differenz die Stärke schon zeigt.
- Kantersiege/hohe Niederlagen: xG und Schüsse aus Phasen mit ≥ 2 Toren Abstand sind fast reines Rauschen; ein Team, dessen Saison-xG durch einige Kantersiege aufgebläht ist, ist schwächer als die Summe suggeriert (und umgekehrt).
- Teams, die oft führen, haben „gedrückte" Schuss-/Ballbesitzwerte und oft leicht günstige PDO (bessere Verwertung/Gegner mit schlechteren Schüssen) – das ist teils Spielstandseffekt, nicht nur Glück.

### Gaps
- Keine quantitativen, aktuellen europäischen Zahlen gefunden, wie stark Schuss-/xG-Anteile bei Führung/Rückstand konkret verschoben werden (StatsBomb/Pugsley 2013 nur verlinkt, nicht abgerufen).
- Keine Studie zur Stabilität/Prognosekraft von „Punkte nach 0:1", „Halbzeitführung gehalten" oder „erstes Tor %" auf Teamebene.
- Eine Studie (Big 5, 2014/15) mit Heim-/Auswärts-Aufteilung (Heimteam nach erstem Tor ≈ 85 % der möglichen Punkte, Auswärtsteam ≈ 76 %) tauchte nur in einem Suchsnippet auf; Primärquelle nicht verifiziert.
- Eine Championship-Studie („nach eigenem Tor weniger, aber bessere Schüsse" – „defensive shell") nur aus Suchsnippet, Primärquelle nicht verifiziert.
- Keine Evidenz zur „Favoriten verwalten Führungen"-These mit Effektgrößen gefunden.

## 5. Abschluss- und Torwart-Über-/Unterperformance vs. xG: Wie persistent? Wann Toren, wann xG trauen?

### Takeaway
Über-/Unterperformance gegenüber xG ist überwiegend Zufall, enthält aber einen kleinen echten Fähigkeitsanteil: Auf Teamebene erklären stabile Klubunterschiede ≈ 29–38 % der Varianz der Tor-Überperformance (offensiv ≈ 22–36 %, defensiv ≈ 20–31 %), auf Spielerebene ≈ 21 % (Abschluss) bzw. ≈ 25 % (Torhüter); Jahr-zu-Jahr-Persistenz liegt bei grob 0,1–0,2. Eine einzelne Saison Überperformance ist nur ein schwaches Signal – xG trauen, Tore nur mit kleinem Zuschlag und erst über mehrere Saisons.

### Cited Findings
- Holzmeister & Johannesson (2025, Journal of Sports Economics 26(8), 953–975; Random-Effects-Metaanalyse, 3 Saisons, 7 europäische Ligen): I² (Anteil Skill) ≈ 29–55 % für Überperformance in Punkten, ≈ 29–38 % für Tor-Überperformance; offensiv (Tore − xG) ≈ 22–36 % (Mittel ≈ 27 %), defensiv (xGA − Gegentore) ≈ 20–31 % (Mittel ≈ 24 %) → ein Drittel bis die Hälfte der Teamvarianz systematisch, Rest Glück; Glück verschiebt Tabellenplätze spürbar (10.000 simulierte Saisons je Liga). Gegenbefund: Sarkar & Kamath (2023) finden keinen systematischen Glückseinfluss auf Endtabellen. — zitiert in [Böttger/Vischer 2026](https://d-nb.info/1400733782/34)
- Böttger & Vischer (Uni Münster, DP 3/2026; Big 5, 2017/18–2024/25, 3.202 Feldspieler-Saisons, 932 Torwart-Saisons, npxG-Basis): Skill-Anteil an der Varianz 6,75–29,95 % beim Abschluss (Mittel I² ≈ 21 %), 7,69–34,34 % bei Torhütern (≈ 25 %). Persistenz-Regression Folgesaison: β = 0,110 (Feldspieler), β = 0,185 (Torhüter), beide p < 0,01; daraus ≈ 52 % (Abschluss) bzw. ≈ 74 % (Torhüter) des Skill-Signals bleiben erhalten. „A single season of xG overperformance is too noisy to serve as a reliable indicator." Beste Finisher als Plausibilitätscheck: Messi OP 0,134 (6 Saisons), Kane 0,111 (8 Saisons); Torhüter Samba +0,214, Navas +0,077, Consigli −0,252, Schwolow −0,220. — [Böttger/Vischer 2026](https://d-nb.info/1400733782/34)
- Analytics FC (2025): bei wenigen Schüssen praktisch kein Zusammenhang zwischen Tore/xG in aufeinanderfolgenden Perioden; ab ≈ 60 Schüssen klarer, aber schwacher Zusammenhang, Persistenzfaktor ≈ 0,1. — [Analytics FC: consistently good finishers?](https://analyticsfc.co.uk/blog/2025/02/11/are-some-players-consistently-good-finishers/)
- Spieler-Abschluss: Tore über xG Jahr-zu-Jahr r ≈ 0,12 (Preprint, PL). — [arXiv 2512.00203](https://arxiv.org/pdf/2512.00203)
- Davis & Robberechts (2024): Messi übertraf seine xG über die gesamte Karriere „nur" um ≈ 25 %; Simulationen: in einer Saison überzuperformen ist gut möglich, es dauerhaft zu tun ist schwer. — [arXiv 2401.09940](https://arxiv.org/pdf/2401.09940)
- ASA Replication (2023): Tore − xG (wie Tore/xG) sagt sich selbst von Saison zu Saison schlecht voraus; xG sei auf Teamebene „perhaps the best metric" zur Projektion der Folgesaison. — [ASA: Measuring Shooting Overperformance](https://www.americansocceranalysis.com/home/2023/8/28/the-replication-project-measuring-shooting-overperformance)
- Torhüter (ASA 2023; Keeper mit ≥ 50 Torschüssen gegen in beiden Saisons): Jahr-zu-Jahr-Korrelation 0,21 für Gegentore/PSxG, 0,18 für Gegentore/xG – schwach, aber signifikant; ein durchschnittlicher Keeper kann realistisch 8–10 Tore zwischen zwei Saisons schwanken. — [ASA: Thomas Bayes? Meet Djordje Petrovic](https://www.americansocceranalysis.com/home/2023/8/28/thomas-bayes-meet-djordje-petrovic)
- Torhüter (Analytics FC 2023): PSxG−GA schwankt bei Keepern mit und ohne Vereinswechsel ähnlich (also eher individuell), Leistung ändert sich zwischen Saisons im Schnitt um ≈ 0,2 Tore/90. — [Analytics FC: goalkeeper statistics](https://analyticsfc.co.uk/blog/2023/08/22/do-goalkeeper-statistics-reflect-individual-ability-or-team-performance/)
- Liga MX (2021ff.): Goals-prevented-Metrik Jahr-zu-Jahr r = 0,08. — [Cambio de Juego](https://cambiodejuegoenglish.beehiiv.com/p/goalkeepers-the-hardest-position-to-analyze)
- Bayesianisches Shrinkage (log-odds, kleine Stichproben zum Mittel ziehen) als empfohlene Methode, temporäre Überperformance von echter Fähigkeit zu trennen. — [pena.lt: A better way to measure finishing skill (2025)](https://pena.lt/y/2025/10/01/a-better-way-to-measure-finishing-skill/)
- Spielstand färbt Verwertung/PDO: Leicester 2015/16 PDO > 110, teils durch lange Phasen in günstigem Spielstand erklärt. — [One Short Corner](https://oneshortcorner.wordpress.com/2016/04/12/football-analytics-part-five-game-states-and-score-effects/)

### Inferences
- Faustregel fürs Bild: Tore − xG (offensiv) und xGA − Gegentore (defensiv) einer laufenden Saison größtenteils (grob 2/3 bis 3/4) als Zufall behandeln, der zurückläuft. Ein Team, das klar über xG trifft, ist eher schwächer als die Torbilanz; eines mit klar weniger Gegentoren als xGA eher anfälliger, als es aussieht – und umgekehrt.
- Tore eher trauen (mit Zuschlag), wenn: (a) die Überperformance über mehrere Saisons und viele Schüsse anhält, (b) sie an konkreten Personen hängt, die noch da sind (Elite-Stürmer, nachweislich starker Torhüter – Torhüter-Signal ist etwas stabiler als Abschluss-Signal), (c) sie zum Spielstil passt (oft führend → Konter mit hoher Verwertung, siehe Abschnitt 4). Bei Torhüter- oder Stürmerwechsel/Verletzung den Zuschlag streichen.
- xG eher trauen, wenn: kleine Stichprobe (frühe Saison, < ≈ 10 Spiele), Überperformance aus wenigen Ausreißerspielen, keine Personenkonstanz.
- Für die Defensive: PSxG/xGOT gegen minus Gegentore isoliert Torwartleistung; xGA misst, wie viel die Abwehr zulässt – die Abwehr-Kennzahl (xGA) ist das stabilere Prognosesignal.

### Gaps
- Exakte Team-Jahr-zu-Jahr-Korrelation von (Tore − xG) bzw. (xGA − Gegentore) nicht gefunden (Holzmeister & Johannesson nur sekundär über Böttger/Vischer zugänglich).
- Keine Studie zur Persistenz innerhalb einer Saison (erste vs. zweite Hälfte) auf Teamebene gefunden.

## 6. Vergleichsstudien zum Prognosewert dieser Kennzahlen (Überblick)

### Takeaway
Die direkten Vergleichsstudien (11tegen11 2015, ASA 2022, ElHabr 2024, PLOS ONE 2023, Brechot & Flepp 2020) stimmen überein: xG > Tore ≈ Torschüsse > Punkte > alle Schüsse für künftige Punkte/Tore; Spielstand-Filter, xGOT und Stil-Kennzahlen (PPDA, Ballbesitz, Field Tilt) sind nicht als zusätzliche Prädiktoren belegt. Kompositmaße mit Strafraum-/Chancen-Erzeugung (xG + xAG, Pässe in den Strafraum, goals added) zeigen teils etwas mehr Prognosekraft.

### Cited Findings
- 11tegen11 (2015, Top-5 + Eredivisie): xG-Verhältnis höchste Korrelation mit künftigen Punkten, nach 4 Spielen so gut wie Tor-Verhältnis maximal. — [ASA 2022](https://www.americansocceranalysis.com/home/2022/7/19/the-replication-project-is-xg-the-best-predictor-of-future-results)
- ASA-Replikation (2022, 14.608 Top-5-Spiele): xG weiterhin vorne, Abstand kleiner, ≈ 8 Spiele bis xG Punkte schlägt. — [ASA 2022](https://www.americansocceranalysis.com/home/2022/7/19/the-replication-project-is-xg-the-best-predictor-of-future-results)
- ElHabr (Big 5, 2018–2024): Schwelle R² > 0,5 – xG 9/13, Tore 11/15, Torschüsse 12/16, Punkte 13/16, Schüsse nie; Spielstand-gefiltertes xG nicht besser; xGOT schlechter; xG + xAG 7/10. — [ElHabr](https://tonyelhabr.rbind.io/posts/xg-predictor-future-results/)
- PLOS ONE 2023: xG schlägt Schüsse und Tore in allen Ligen/Maßen bis auf eine Ausnahme. — [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0282295)
- Brechot & Flepp 2020: xG-basierte Maße prognostizieren künftige Ergebnisse signifikant besser als Ergebnismaße. — zitiert in [Böttger/Vischer 2026](https://d-nb.info/1400733782/34)
- Skill-vs-Glück-Zerlegung auf Teamebene: 29–38 % der Tor-Überperformance-Varianz systematisch. — [Böttger/Vischer 2026](https://d-nb.info/1400733782/34)
- Gegenstimmen: Wheatcroft (Ratings aus anderen Statistiken können konkurrenzfähig sein) — [arXiv 2001.09097](https://arxiv.org/pdf/2001.09097); Argentinien (Hamilton 2015–16) und MLS: xG nicht klar überlegen / geringere Vorhersagbarkeit in Ligen mit Parität bzw. unausgeglichenem Spielplan — [ASA 2022](https://www.americansocceranalysis.com/home/2022/7/19/the-replication-project-is-xg-the-best-predictor-of-future-results)
- Neuere Bundesliga-Studie vergleicht Expected Possession Value (EPV) mit xG zur Ergebnisprognose (nicht im Detail abgerufen). — [PMC12640942](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12640942/)
- Unterschiedliche xG-Anbieter haben unterschiedliche Prognosekraft (Vergleich, nicht im Detail abgerufen). — [Beat the Bookie: Comparing xG providers (2024)](https://beatthebookie.blog/2024/01/06/comparing-the-predictive-power-of-different-xg-data-providers/)

### Inferences
- Lesehilfe für ein qualitatives Teambild (aus allen Abschnitten abgeleitet):
  1. Kern: xG-Differenz (für/gegen), möglichst ohne Elfmeter und ohne Phasen mit ≥ 2 Toren Abstand gedacht.
  2. Abgleich Tore vs. xG: Lücke überwiegend als Zufall mit Rücklauf lesen; nur mehrjährige, personengebundene Lücken (Torjäger, Torhüter) teilweise behalten.
  3. Torschüsse > Schüsse; viele Schüsse mit niedriger Qualität nicht als Stärke werten.
  4. Standard-xG für/gegen als Zusatzbaustein, besonders für den Außenseiter (BTTS) und gegen tief stehende Gegner.
  5. Spielstand-Felder („erstes Tor %", „Punkte nach 0:1", „Halbzeitführung gehalten") primär als Stärke-Proxy; nur starke Abweichungen vom Stärke-Erwartungswert sind interessant, und auch die sind klein-stichprobig.
  6. PPDA/Ballbesitz/Field Tilt/gefährliche Angriffe als Stil-Kontext, nicht als eigenständige Stärke- oder Torprognose.
- Datenmenge: Vor ≈ Spieltag 8–10 sind Saisonwerte aller Kennzahlen unsicher; Home/Away-Teilstichproben halbieren die Datenmenge und sind noch verrauschter.

### Gaps
- Keine Vergleichsstudie für zweite Ligen in Europa gefunden.
- Keine Vergleichsstudie mit Zielgröße Over/Under 2.5 oder BTTS (statt Punkte/Tor-Verhältnis) gefunden.
- Keine Studie zur Prognosekraft von Heim- vs. Auswärts-getrennten Teamwerten gefunden.
