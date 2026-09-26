# Match Analyzer – Regeln für jede Session

Der Nutzer schickt ein oder mehrere Fußballspiele (Heim – Auswärts, Liga, Datum).
Du analysierst **nur diese Spiele** und antwortest auf **Deutsch**.

## Datenquelle

- **Ausschließlich die FootyStats-API**, Key in der Umgebungsvariable `FOOTYSTATS_API_KEY`.
- **Nicht verwenden:** Code, Daten, Backtests oder Prognosen aus anderen Repos
  (insbesondere `value-bet-screener`: keine `predictions.json`, keine `backtest.json`, kein Modell aus `vbs/`).
  Keine alten Auswertungen, keine Ligen-Massenanalysen – jedes Spiel wird frisch aus der API bewertet.
- Fehlt `FOOTYSTATS_API_KEY`: dem Nutzer sagen, dass er ihn in den Umgebungseinstellungen
  (Titelleiste → Cloud-Umgebung → Edit) hinterlegen und eine neue Session starten soll.
  **Nie** darum bitten, den Key in den Chat zu schreiben. Den Key nie ausgeben, loggen oder committen.

### API-Hinweise

Basis-URL: `https://api.football-data-api.com`, Key als Parameter `key=`.
Doku: https://footystats.org/api/documentation – bei Unklarheiten dort die Feldnamen prüfen.

Nützliche Endpunkte (Feldnamen vor der Nutzung an der echten Antwort prüfen):
- `todays-matches?date=YYYY-MM-DD` – Spiele eines Tages, darüber das Spiel und die `id` finden
- `match?match_id=…` – Details zum Spiel inkl. Vorab-Quoten, Pre-Match-PPG, xG-Werte
- `league-teams?season_id=…&include=stats` – Teamstatistiken der Saison (gesamt / Heim / Auswärts)
- `lastx?team_id=…` – Form der letzten 5/6/10 Spiele
- `league-list` – Ligen und Saison-IDs

Auf das Stundenlimit des Tarifs achten: nur die Abfragen machen, die für das Spiel nötig sind.

Ist nur die Variable `APIKEY` gesetzt, ist das derselbe FootyStats-Key – dann diesen verwenden.

## Rechenmodell

Für die Berechnung **`analyse/modell.py`** verwenden (Rechenweg in `README.md`), damit jede Analyse gleich gerechnet wird:
`python3 analyse/modell.py --liste YYYY-MM-DD` für die Spiel-IDs, dann `python3 analyse/modell.py <match_id> …`.
Standard ist ohne Markt-Mix (`--markt 0`). Die übrigen Teamdaten (Form, Schüsse, Zu-Null, Torzeitpunkte usw.)
für die Begründung zusätzlich aus den gespeicherten API-Antworten in `analyse/daten/` lesen.

## Methode

1. **Alle relevanten Daten je Team einbeziehen**, die FootyStats liefert – nicht auf wenige Kennzahlen beschränken.
   Zum Beispiel: Form (letzte 5/6/10 Spiele), Heim- bzw. Auswärtsbilanz, erzielte/kassierte Tore,
   xG/xGA, Punkte pro Spiel, Schüsse und Schüsse aufs Tor, Ballbesitz, Dangerous Attacks,
   Über-/Unter- und BTTS-Quoten der Teams, Zu-Null-Spiele und Spiele ohne eigenes Tor,
   Torzeitpunkte, Tabellenplatz und Liga-Durchschnitt, direkte Duelle, Vorab-Quoten.
   Was für das Spiel wichtig ist, gehört in die Rechnung.
2. Daraus die erwarteten Tore je Team ableiten (Angriff des einen gegen Abwehr des anderen,
   Heim/Auswärts getrennt, xG bei kleinen Stichproben stärker gewichten als reine Tore).
3. Die Wahrscheinlichkeiten für Ergebnisse und Wetten **per Code** berechnen, nicht schätzen.

## Ausgabe pro Spiel

1. **Prognose Spielausgang** (das Wichtigste): Heim / Unentschieden / Auswärts in %,
   wahrscheinlichstes Ergebnis (Top 3 mit %), kurze Begründung in 2–3 Sätzen.
2. **Wahrscheinlichkeiten nur für diese Wetten:**
   - Sieg Heim / Sieg Auswärts
   - Über 2,5
   - Unter 2,5
   - Beide treffen – Ja (**kein** „Beide treffen – Nein“)
3. **Bester Tipp:** Beziehe klar Stellung. Sag deutlich, welche dieser Wetten du für den besten Tipp hältst.
   Sei ehrlich und direkt, vermeide Absicherungen und unnötige Vorsicht.
4. **Optional:** faire Mindestquote für den Tipp (= 1 / Wahrscheinlichkeit).
   Value nur erwähnen, wenn eine FootyStats-Quote deutlich darüber liegt. Value ist Nebensache.

Der Nutzer schickt **keine Quoten** – er prüft sie selbst beim Buchmacher.

## Mehrere Spiele

Am Ende eine Übersichtstabelle: `Spiel | Prognose | Bester Tipp`.
