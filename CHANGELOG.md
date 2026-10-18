## 2026-10-10
- Initial skill creation for FootyStats Bild und Wette analysis.
- Added workflow, API key, field mapping reference, and basic fetch script.

## 2026-10-11
- Regeln für Bild + Verlauf gelockert: freiere Gewichtung und Interpretation der Teamfelder (Last 6 vs. Saison, Home/Away, Varianz-Zusammenspiel).
- Keine festen Schwellen oder Grenzwerte mehr.
- Begründung darf qualitativer und ausführlicher sein.
- Eine stärkste Wette oder „keine“ bleibt unverändert.

## 2026-10-10 (Update 3)
- Varianz-Felder hinzugefügt: `BTTS_and_lose_percentage`, `BTTS_and_win_percentage`, `AVG_2hg`, `seasonScoredAVG`, `seasonConcededAVG`.
- Diese Felder fließen ins Bild ein, um den Spielverlauf besser abzubilden.
- Bei hoher BTTS_and_lose trotz guter xG-Bilanz wird Over/BTTS der reinen Sieg-Wette vorgezogen.
- Nur noch **eine Wette** pro Spiel: die stärkste aus dem Bild.
- Keine Kombinationen mehr (z. B. Sieg + BTTS).
- Wenn der Verlauf stärker ist als die reine Stärke, wird Over/BTTS/Under gewählt.
- Bild-Interpretation erweitert: Spielverlauf stärker gewichten.
- Regeln für Over 2.5 / BTTS / Under 2.5 aus Teamfeldern ergänzt (beide Seiten offensiv/defensiv, eine Seite stärker + Gegner trifft, beide defensiv, Home/Away-Unterschiede, Last-6-Gewichtung).
- Ziel: Nicht mehr automatisch nur Sieg-Wetten, sondern Verlauf aus den Zahlen ableiten.

## 2026-10-10
- Initial skill creation for FootyStats Bild und Wette analysis.
- Added workflow, API key, field mapping reference, and basic fetch script.

## 2026-10-11 (Update 4)
- Spiele kommen als nummerierter Batch; Antwort in derselben Nummerierung.
- Übersicht ganz oben: Nr. | Anpfiff | Spiel | Wette | ⚠️ Gefahr, darunter die freigegebenen Wetten.
- Warnsignal ⚠️ nach Vorgabe des Nutzers: qualitativ, ohne Grenzwerte, Schwerpunkt Heim-Anfälligkeit; Kriterien je Wette (Heimsieg, Auswärtssieg, BTTS/Over, Under) und seltenere Signale. Nur Darstellung, ändert die Wette nicht.

## 2026-10-14
- „Auswerten“ heißt: nur die freigegebenen Wetten (ohne ⚠️, nicht „keine“) aus dem genannten Zeitraum.

## 2026-10-15
- Freigabe-Check in drei Durchgängen vor jeder Wette ohne ⚠️: Spalte für Spalte (auch L6 zu Hause/auswärts), gleiche Signale gleich behandeln, jede Zahl gegen die Tabelle prüfen. Anlass: Bodø/Glimt – Dortmund (1:0), wo Dortmunds stabile Auswärtsabwehr (0,67 Gegentore) nicht wie bei Feyenoord markiert wurde.
- Ohne Saisondaten (v. a. Conference League) keine Freigabe.
- `scripts/tabellen.py`: Tabellen je Spiel mit doppelter Lesung und Gegenprobe.
- `references/api_hinweise.md`: Spiele finden über `/league-matches`, Saison-IDs, Namensvarianten, Europapokal-Besonderheiten.
- Häufigkeiten und Ergebnisse als Teamfelder aufgenommen (Nutzer 15.10., „ohne irgendwelche Schwellen“): `seasonCSPercentage`, `seasonFTSPercentage`, `seasonOver25Percentage`, `seasonBTTSPercentage`, `winPercentage`, `drawPercentage`, `seasonPPG`, `shotsOnTargetAVG` – je gesamt/zu Hause/auswärts und für die letzten 6. Sie fließen qualitativ ins Bild und in die Wette ein, ohne Grenzwerte. `tabellen.py` zeigt sie als zusätzliche Zeilen (Gegenprobe jetzt 228 Werte je Spiel).
- Europapokal und Pokal: Die Saisonspalten kommen aus der aktuellen Saison der heimischen Liga des Teams (`/team`), nicht mehr aus dem Wettbewerb mit oft 0 bis 3 Spielen (Nutzer 15.10.: „nur weil sie erst 1 Spiel oder 0 Spiel in der Conference League haben, heißt es nicht, dass die Daten weggeschmissen werden sollten“). Die Quelle steht je Team über der Tabelle. Tore/Gegentore zu Hause/auswärts kommen dort aus `seasonScoredNum_*`/`seasonConcededNum_*`; damit sind auch die Tore der letzten 6 zu Hause/auswärts vorhanden.

## 2026-10-16
- Warnsignal bei Siegwetten erweitert (Nutzer 16.10., „ohne Schwellen“): ⚠️ auch, wenn eines der Teams in den passenden Spalten auffällig oft unentschieden spielt, oder wenn das Team, gegen das gewettet wird, klar bessere Ergebnisse holt, als seine xG erwarten lassen (bei Heimsieg das Gastteam auswärts, bei Auswärtssieg sinngemäß das Heimteam zu Hause). Anlass: Sparta Praha – Lillestrøm und Hearts – Nordsjælland, beide freigegebene Heimsiege, beide 1:1.

## 2026-10-17
- Zurück auf den Stand vom 14.10. (Nutzer 17.10.: „zum System zurück, wo 100 % Trefferquote war“). `SYSTEM.md`, `CLAUDE.md`, `system/tabellen.py` und `references/field_mapping.md` sind wieder wie am 14.10.: Warnregel vom 11.10., kein Freigabe-Check, keine Häufigkeits- und Ergebnisfelder, im Europapokal die Saisondaten aus dem Wettbewerb selbst, keine Zusatzregel für Siegwetten. Die Einträge vom 15. und 16.10. oben bleiben als Verlauf stehen. `references/api_hinweise.md` bleibt (Saison-IDs, Namensvarianten; ändert keine Wette).
- Präzisiert (Nutzer 17.10.: „das System laut den Spielen vom 13.10. zurück“): Maßgeblich ist der Stand vom 13.10. (Commit 4cc8953). `SYSTEM.md`, `system/tabellen.py` und `references/field_mapping.md` sind damit identisch. In `CLAUDE.md` kam bis heute nur die Auswerten-Regel vom 14.10. dazu; sie legt fest, was „auswerten“ heißt, und ändert keine Wette.

## 2026-10-18
- Neues Spielbild (Nutzer 18.10.: „je Team alle über 1000 Felder lesen“, „nicht starr nur Daten ablesen“, „offenes Hirn sowie eine starke Philosophie, um ein perfektes Spielbild je Spiel zu erstellen“). `SYSTEM.md`: Philosophie „erst die Geschichte des Spiels, dann die Wette“ mit sechs Fragen (wer hat das Spiel in der Hand, wie beginnt es, was passiert nach dem ersten Tor, trifft der Schwächere/hält der Starke die Null, wie nah ist ein Remis, wie belastbar sind die Zahlen). Gewichtung offen, ohne Schwellen; Erfahrung und Einschätzung gehören dazu. Gemeinsame Felder, Quoten und direkter Vergleich bleiben Kontext.
- `system/tabellen.py` liest je Team alle Felder aus `/league-teams` und `/lastx` (gut 1.000), zeigt die spielbezogenen (rund 190 Zeilen je Team, je mit gesamt/zu Hause/auswärts/L6) gegliedert nach den sechs Fragen und vergleicht in der Gegenprobe alle Felder beider Lesungen. Ecken, Karten, Abseits, Fouls, Namen und Verwaltung werden mitgelesen, aber nicht gezeigt. `--roh` schreibt alles ungekürzt in eine JSON-Datei. Hinweis in jeder Tabelle: L6 zählt alle Wettbewerbe.
- `CLAUDE.md`: Beim Heimsieg entfällt die ⚠️-Bedingung „Heim-Stärke nicht extrem“ (das „Hindernis im System“, am 17.10. bei 18 von 19 Heimsiegen). Neu: ⚠️ bei jeder Wette, wenn die Geschichte des Spiels einen echten Bruch hat. Batch-Format mit „Batch X · Nr. Y“ und Analyse als Datei festgehalten.
- `references/field_mapping.md`: Zuordnung der Felder zu den sechs Fragen.
- Zurückgenommen (Nutzer 18.10.: „wir lassen alles beim Alten“). Blindtest an den 13 freigegebenen Spielen vom 17.10. mit Datenstand vor dem Anpfiff: altes System mit 10 Zeilen 7/13; neues Spielbild 6/12 (frei 4/7); altes System mit allen Daten 6/12 (frei 4/7), dieselben Wetten wie das neue Spielbild. `SYSTEM.md`, `system/tabellen.py`, `references/field_mapping.md` wieder wie am 13.10. (Commit 4cc8953), auch die ⚠️-Regel vom 11.10. mit „Heim-Stärke nicht extrem“. In `CLAUDE.md` bleiben nur das Batch-Format (mehrere Batches, Analyse als Datei) und ein Hinweis auf diese Entscheidung; beides ändert keine Wette.
- Spielbild je Team verbessert (Nutzer 18.10.: „mach dich auf die Suche“, dann „Du bist hier der Spezialist“). Grundlage: Recherche `reports/Spielbild je Team verbessern.md` und ein Blindtest an allen 65 Spielen vom 17.10. mit Datenstand vor dem Anpfiff, je zwei unabhängige Analysen pro Fassung. A = System 13.10.: freigegeben 10/24 (42 %), mit ⚠️ 15/34 (44 %), alle 25/58. B = 13.10. + Gewichtung nach Belastbarkeit + Vorsaison + Liga-Grundwerte + letzte 6 nur Liga: freigegeben 12/20 (60 %), mit ⚠️ 10/25 (40 %), alle 22/45. Übernommen wird B:
  - `SYSTEM.md`: letzte 6 aus den Ligaspielen (`/league-matches`) statt `/lastx`; neu Schritt 3a (Vorsaison je Team aus `/team`, Liga-Grundwerte der Vorsaison); neuer Abschnitt „Gewichtung nach Belastbarkeit“ (xG vor Toren, Gesamtspalte vor Heim/Auswärts, Vorsaison früh in der Saison, letzte 6 nur Hinweis, Varianz-Felder färben, Liga-Grundwerte als Ausgangspunkt für Torzahl/BTTS, Under/Zu-Null über den Angriff des Gegners, Remis spricht gegen Siegwette). Die zehn Zeilen bleiben.
  - `CLAUDE.md`: ⚠️ beim Heimsieg jetzt „Gastteam defensiv sehr stabil (vor allem xG dagegen) oder Stärkeunterschied insgesamt nicht klar“ statt „Heim-Stärke nicht extrem“; zusätzliches seltenes Warnsignal: tragender Wert aus wenigen Spielen oder einem Ausreißer.
  - `system/tabellen.py`: letzte 6 aus `/league-matches` (L6 zu Hause/auswärts jetzt mit Toren), Vorsaison-Zeile je Team, Liga-Grundwerte je Spiel; Gegenprobe über alles.
  - `references/field_mapping.md` entsprechend.
- Remis-Gefahr beim Heimsieg (Nutzer 18.10.: „Daran musst du arbeiten, wieso und warum … das musst du erkennen“, nach drei freigegebenen Heimsiegen mit Remis im Blindtest). Analyse von 6.264 Ligaspielen (19 Ligen, nur Daten vor dem Anpfiff), 1.879 Heimfavoriten: Remis lassen sich nicht sicher vorhersagen, aber der saubere Heimsieg lässt sich erkennen. Fünf Merkmale: Heim xG für, xG-Abstand gesamt, Punkteabstand, erwartete Gasttore, Heim-Tore gegenüber xG. Ohne Hinweis 77 % Heimsieg (14 % Remis, n = 317), mit einem Hinweis 65 %, mit zwei und mehr 54 % (25 % Remis); stabil in Vorsaison/laufender Saison und Ligatypen. Am 17.10.: ohne Hinweis 3/3 Heimsiege (City, Roma, Amed), mit einem 3/5, mit zwei und mehr 5/13. `CLAUDE.md`: ⚠️ „Remis-Gefahr“ beim Heimsieg, wenn ein Merkmal fehlt. `SYSTEM.md`: Gewichtung Punkt 9. `system/tabellen.py`: Zeile „Remis-Check“ mit den fünf Werten und Anhaltspunkten (keine festen Grenzen).
