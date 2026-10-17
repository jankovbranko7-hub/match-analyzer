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
