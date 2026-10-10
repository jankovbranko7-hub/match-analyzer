# Regeln

**Das System ist `SYSTEM.md` – genau so, wie es dort steht, und nichts sonst.** Seit
10.10.2026 ist das das Paket „footystats-bild-wette" des Nutzers (`SYSTEM.md` = dessen
`SKILL.md`, dazu `references/`, `scripts/`, `evals/`, `CHANGELOG.md`), vom Nutzer als
„komplettes neues System" eingesetzt, „so ausführen ohne Widerrede". Es verlangt die
freiere, qualitative Gewichtung von Bild und Verlauf ohne Schwellen – genau so anwenden.
Die früheren Lesarten 1–5 gelten nicht mehr.

**Spiele kommen als Batch:** Der Nutzer schickt künftig immer 5 Spiele, nummeriert.
Geantwortet wird in derselben Nummerierung – jede Nummer genau ihr Spiel, nichts vertauschen.

## Technik (nicht Teil des Systems)

`SYSTEM.md` nennt `FOOTYSTATS_KEY`. In dieser Umgebung ist der Key als `APIKEY`
hinterlegt; beim Aufruf als `FOOTYSTATS_KEY="$APIKEY"` mitgeben. Fehlt er: dem Nutzer
sagen, dass er ihn in den Umgebungseinstellungen hinterlegen soll. Den Key **nie** im
Chat erfragen, ausgeben, loggen, in eine Datei schreiben oder committen.

Ein `HTTP 417` ist das Stundenlimit der API – dann warten.

Tabellen kommen aus `system/tabellen.py` mit den Feldern aus `SYSTEM.md`. Liefert die API
bei `seasonGoals_*`/`seasonConceded_*` eine Liste (eine Torminute je Tor), ist die Anzahl
der Einträge die Torzahl. Fehlt das Feld (z. B. letzte 6 zu Hause/auswärts), steht „fehlt".

Antworten auf Deutsch.
