# Regeln

**Das System ist `SYSTEM.md` – genau so, wie es dort steht, und nichts sonst.** Seit
10.10.2026 ist das das Paket „footystats-bild-wette" des Nutzers (`SYSTEM.md` = dessen
`SKILL.md`, dazu `references/`, `scripts/`, `evals/`, `CHANGELOG.md`), vom Nutzer als
„komplettes neues System" eingesetzt, „so ausführen ohne Widerrede". Es verlangt die
freiere, qualitative Gewichtung von Bild und Verlauf ohne Schwellen – genau so anwenden.
Die früheren Lesarten 1–5 gelten nicht mehr.

**Spiele kommen als Batch:** Der Nutzer schickt künftig immer 5 Spiele, nummeriert.
Geantwortet wird in derselben Nummerierung – jede Nummer genau ihr Spiel, nichts vertauschen.

**Gefahr nur, wo sie sicher da ist** (Nutzer 11.10.: erst „immer markiert, weil man den
Überblick schnell verliert", dann „nur pro Spiel, wo es auch zu 100 % eine Gefahr gibt"):
Ganz oben steht eine Übersicht je Nummer: Spiel | Wette | ⚠️ Gefahr. Die Zeile
`⚠️ **Gefahr:** …` (direkt unter der Wette, mit Feld und Zahl) gibt es **nur**, wenn ein
Teamfeld direkt das Gegenteil der Wette zeigt – in den Spalten, die für das Spiel zählen:
Heimteam gesamt / zu Hause / L6 gesamt, Gast gesamt / auswärts / L6 gesamt.
- Heimsieg / Auswärtssieg: Der Gegner hat in einer dieser Spalten die bessere Tor- oder
  xG-Bilanz (für minus gegen pro Spiel), oder das gewettete Team ist dort im Minus.
- Over 2.5: In einer dieser Spalten fallen im Schnitt weniger als 2,5 Tore pro Spiel
  (Tore + Gegentore). Under 2.5: mehr als 2,5.
- BTTS Ja: Ein Team trifft in einer dieser Spalten im Schnitt unter 1 Tor pro Spiel, oder
  der Gegner kassiert dort im Schnitt unter 1.
Sonst keine ⚠️-Zeile, in der Übersicht „–“. Schwächen, die nicht direkt dagegen sprechen,
gehören in die Begründung, nicht in die Gefahr-Zeile. Bei „keine“ steht in der Übersicht der
Grund. Das ist nur die Darstellung – an der Wahl der Wette ändert es nichts.

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
