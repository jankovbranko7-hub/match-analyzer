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

**Ausgabe genau wie in `SYSTEM.md`:** Tabelle je Team, das Bild in **genau einem Satz**,
eine Wette oder keine. Keine Zusätze – kein „Warum nicht die anderen", keine Hinweise
zur Datenbasis, keine eigene Herleitung.

**Kein festes Verfahren zum Zusammenführen, keine Schwelle.** Am 06.10.2026 hatte ich
eines erfunden (acht Sichten aus Angriff plus gegnerischer Abwehr geteilt durch zwei,
Wette nur wenn alle acht übereinstimmen, BTTS erst ab 1 je Seite). Der Nutzer hat es
gestrichen. Nicht wieder einbauen.

**Tragen die Teamfelder zwei Wetten, werden beide genannt.** (Vom Nutzer bestätigt.)

**Gegenprobe:** Die Daten werden zweimal abgefragt (Spiel, `league-teams`, `lastx` je
Team) und Wert für Wert verglichen. Weicht einer ab: keine Wette.

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
