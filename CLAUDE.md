# Regeln

## Das System ist `SYSTEM.md`

**Ab 06.10.2026 gilt `SYSTEM.md` im Hauptordner – genau so, wie es dort steht.** Vom
Nutzer so entschieden. Lesen, Ausgabe und Wette folgen allein dieser Datei. Alles hier
unten regelt nur den Rahmen. Steht etwas hier im Widerspruch zu `SYSTEM.md`, gilt
`SYSTEM.md` – und das ist zu melden, nicht stillschweigend aufzulösen.

**So ist es gemeint – Erläuterung des Nutzers vom 06.10.2026, wörtlich:**

> Jedes Team bringt seine eigenen Felder mit: Tore, Gegentore, xG für, xG dagegen,
> Spiele, letzte 6, jeweils gesamt, zu Hause und auswärts. Diese Felder werden
> zusammengeführt. Daraus entsteht das Bild, und nur daraus der Tipp.
> Die gemeinsamen Zahlen, Pre-Match-xG, BTTS, Over und Under, führen die Entscheidung
> nicht. Sie stehen daneben. Tragen die Teamfelder keinen gemeinsamen Satz, gibt es
> keinen Tipp. Das ist der skeptische Teil: nicht jedes Spiel bekommt eine Wette, nur
> weil eine Zahl größer ist.

Zu jeder Wette steht im Chat, welche Teamfelder sie tragen, damit der Nutzer sie
nachprüfen kann.

**Vorgehen, vom Nutzer am 06.10.2026 bestätigt („Das passt so"):**

- **Zusammenführen.** Vier Spaltenpaare: gesamt / gesamt · Heim zu Hause / Gast
  auswärts · letzte 6 gesamt / letzte 6 gesamt · letzte 6 Heim zu Hause / letzte 6 Gast
  auswärts. Je Paar und Seite: (eigene Tore pro Spiel + Gegentore des Gegners pro Spiel)
  / 2, ebenso (eigenes xG für + xG dagegen des Gegners) / 2. Das ergibt acht Sichten
  (vier Paare, je Tore und xG). Diese Tabelle steht im Chat.
- **Eine Wette ist getragen, wenn alle acht Sichten dasselbe sagen:** Heimsieg bzw.
  Auswärtssieg – die Seite liegt überall vorn. Over 2,5 bzw. Under 2,5 – die Summe liegt
  überall über bzw. unter 2,5. BTTS Ja – jede Seite kommt überall auf mindestens 1.
  Sagt eine Sicht etwas anderes: keine Wette.
- **Tragen zwei Wetten, werden beide genannt.** Es wird keine ausgewählt.
- Die Daten werden zweimal abgefragt (Spiel, `league-teams`, `lastx` je Team) und Wert
  für Wert verglichen. Weicht einer ab: keine Wette.

Der Nutzer schickt ein Datum und Paarungen. Du analysierst **nur diese Spiele** und
antwortest auf **Deutsch**.

**Nicht mehr benutzt:** `analyse/modell.py` (Poisson-Modell) und `skills/api-bild/`
(Tipp aus dem höchsten Potential). Beide bleiben im Repo liegen, liefern aber keine Wette.

## Key

`SYSTEM.md` nennt `FOOTYSTATS_KEY`. In dieser Umgebung ist der Key als `APIKEY`
hinterlegt; beim Aufruf unter dem Namen `FOOTYSTATS_KEY` mitgeben
(`FOOTYSTATS_KEY="$APIKEY" python3 ...`), Dateien dafür nicht ändern.

Fehlt der Key: dem Nutzer sagen, dass er ihn in den Umgebungseinstellungen hinterlegen
und eine neue Session starten soll. **Nie** darum bitten, den Key in den Chat zu
schreiben. Den Key **nie** ausgeben, loggen, in eine Datei schreiben oder committen –
auch nicht in `api_bild.py`.

## Stundenlimit

Nur die Abfragen machen, die für die geschickten Spiele nötig sind. Ein `HTTP 417` ist
das Limit – dann warten, nicht sofort erneut abfragen.

## Nichts Altes

Keine Datei des alten Systems (die „70/30-Datei" mit den 14 Konstanten, `modell2.py`,
`bilanz.py`, `bilanz.json`, `rueckschau.py`, `pruefung.py`, `pruefung2.py`, `bild.py`,
`SOLLBRUCHSTELLEN.md`), kein fremdes Repo, insbesondere `value-bet-screener`, nicht
dessen Zwischenspeicher. Kein Backtesting in jeder Form.

## Nichts dazuerfinden

Keine zusätzliche Schwelle, kein Filter, keine Obergrenze, kein Ausschlusskriterium,
keine Rechnung, die `SYSTEM.md` nicht verlangt – auch nicht als gut gemeinter Hinweis,
auch nicht in Prosa. Fehlt eine Regel, wird gefragt, nicht ergänzt.
