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
