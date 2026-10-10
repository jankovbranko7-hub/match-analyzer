# Regeln

**Das System ist `SYSTEM.md` – genau so, wie es dort steht, und nichts sonst.** Keine
zusätzliche Regel, Lesart, Schwelle, Linie, Rechnung oder Spaltenauswahl, die nicht in
`SYSTEM.md` steht. Alle früheren Zusatzregeln in dieser Datei hat der Nutzer am
10.10.2026 gestrichen („alles raus was nicht im System steht").

**Vom Nutzer danach festgelegt:**
- 10.10.2026: Tragen die Teamfelder zwei Wetten, wird die stärkere getippt („soll die
  stärke getippt werden ganz einfach"). Stärker ist die Wette, deren schwächste Spalte
  weiter über bzw. unter ihrer Linie liegt.

## Technik (nicht Teil des Systems)

`SYSTEM.md` nennt `FOOTYSTATS_KEY`. In dieser Umgebung ist der Key als `APIKEY`
hinterlegt; beim Aufruf als `FOOTYSTATS_KEY="$APIKEY"` mitgeben. Fehlt er: dem Nutzer
sagen, dass er ihn in den Umgebungseinstellungen hinterlegen soll. Den Key **nie** im
Chat erfragen, ausgeben, loggen, in eine Datei schreiben oder committen.

Ein `HTTP 417` ist das Stundenlimit der API – dann warten.

Antworten auf Deutsch.
