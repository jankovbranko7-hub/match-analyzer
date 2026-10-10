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
Wette nur wenn alle acht übereinstimmen). Der Nutzer hat es gestrichen. Nicht wieder
einbauen.

**BTTS Ja ist eine der fünf Wetten wie jede andere** (so steht es in `SYSTEM.md`). Sie
wird an der Linie gelesen, die die Wette selbst vorgibt – wie Over/Under an 2,5:
„beide treffen" heißt, in **jeder** Spalte schießt jedes Team mindestens 1 Tor pro Spiel
und der Gegner kassiert mindestens 1, bei Toren und bei xG (xG für und xG dagegen
jeweils mindestens 1). Bis 09.10.2026 hatte ich BTTS ohne Lesart faktisch
ausgeschlossen – mein Fehler, vom Nutzer so festgestellt.

**Over 2,5 heißt mehr als 2,5, Under 2,5 heißt weniger als 2,5** – wörtlich wie die Wette.
Liegt eine Spalte genau auf 2,50, trägt sie weder Over noch Under. Nicht nachfragen, nicht
auslegen (Nutzer am 10.10.2026: „halte dich an das System").

**Welche Spalten in die Wette eingehen – für alle fünf Wetten gleich** (Nutzer am
10.10.2026, „Dann nehmen wir 2"): beim **Heimteam** gesamt, zu Hause, L6 gesamt,
L6 zu Hause; beim **Gastteam** gesamt, auswärts, L6 gesamt, L6 auswärts. Das gilt für
Heimsieg und Auswärtssieg genauso wie für BTTS Ja, Over 2,5 und Under 2,5. Heimteam
auswärts und Gastteam zu Hause stehen weiter in der Tabelle (`SYSTEM.md` verlangt alle
drei Spalten je Team), gehen aber in keine Wette ein. Bis 10.10.2026 hatte ich BTTS und
Over/Under in allen sechs Spalten beider Teams gelesen, Heim-/Auswärtssieg nur in den
passenden – das war uneinheitlich, vom Nutzer so entschieden.

**Tragen die Teamfelder mehrere Wetten, gilt die mit den stärksten Daten** – Nutzer am
09.10.2026: „du sollst immer die stärksten Daten aus den APIs, so wie es im System
steht, wählen und daraus soll dann die Wette entstehen, falls alles dafür spricht."
Stärker ist die Wette, deren schwächste Spalte weiter von ihrer Linie bzw. vom Gegner
entfernt ist.

**Genau eine Wette oder keine.** Nie zwei. (Vom Nutzer am 06.10.2026 so festgelegt.)

**Widerspricht eine Spalte – auch Tore gegen xG –, gibt es keine Wette.** Alle Spalten
beider Teams (gesamt, zu Hause bzw. auswärts, letzte 6) müssen in dieselbe Richtung
zeigen, bei Toren und bei xG. Vom Nutzer am 07.10.2026 so bestätigt („das passt alles so"),
auch wenn dadurch nur wenige Spiele eine Wette bekommen.

**Tabellen kommen aus `system/tabellen.py`** (`FOOTYSTATS_KEY="$APIKEY" python3
system/tabellen.py <Spiel-ids>`, Spielliste mit `--liste <Datum>`). Nichts per Auge
umrechnen. Die Tabelle hat sieben Zeilen: Spiele, Tore, Gegentore (Summen der API),
**Tore pro Spiel, Gegentore pro Spiel** (Summe geteilt durch Spiele – dieselbe Einheit wie
xG; vom Nutzer am 09.10.2026 so beschlossen, weil Summen und Schnitte nebeneinander zu
falschen Vergleichen führten), xG für, xG dagegen (Schnitt pro Spiel laut API). Verglichen
wird immer pro Spiel. Bei 0 Spielen steht in „pro Spiel" fehlt.
Unter jeder Teamtabelle steht das **Datum des letzten Spiels der „letzten 6"** (Feld
`last_updated_match_timestamp` aus `lastx`) und dass sie laut API aus allen Wettbewerben
stammen (`competition_id: -1`). Vom Nutzer am 09.10.2026 so beschlossen. Die „letzten 6"
gehen **wie bisher** in die Wette ein, es gibt **kein** Kriterium „veraltet" – das Datum
steht nur zur Information da (Nutzer am 09.10.2026: „bleiben gleich").

**Gegenprobe:** Die Daten werden zweimal abgefragt (Spiel, `league-teams`, `lastx` je
Team) und Wert für Wert verglichen. Weicht einer ab: keine Wette.

**Nichts selbst entscheiden.** Nutzer am 09.10.2026: „Ich möchte, dass du nichts selbst
entscheidest … und dich an das System hältst!" Das heißt:
- **Keine persönlichen Empfehlungen**, keine eigene Auswahl oder Rangfolge unter den
  Tipps, kein „würde ich auslassen". Es gibt nur das, was das System ausgibt.
- **Namen exakt wie in der API.** Weicht ein Name ab – auch nur in der Schreibweise
  oder um einen Zusatz wie „FC" –, wird das Spiel nicht ausgewertet; die API-Schreibweise
  und die Spiel-id werden genannt, und der Nutzer entscheidet.
- **Fehlt eine Regel, wird gefragt** – nicht selbst ausgelegt, nicht selbst gewählt.

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
