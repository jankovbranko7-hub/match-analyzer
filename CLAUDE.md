# Regeln

**Das System ist `SYSTEM.md` – genau so, wie es dort steht, und nichts sonst.** Seit
10.10.2026 ist das das Paket „footystats-bild-wette" des Nutzers (`SYSTEM.md` = dessen
`SKILL.md`, dazu `references/`, `scripts/`, `evals/`, `CHANGELOG.md`), vom Nutzer als
„komplettes neues System" eingesetzt, „so ausführen ohne Widerrede". Es verlangt die
freiere, qualitative Gewichtung von Bild und Verlauf ohne Schwellen – genau so anwenden.
Die früheren Lesarten 1–5 gelten nicht mehr.

**Spiele kommen als Batch:** Der Nutzer schickt künftig immer 5 Spiele, nummeriert.
Geantwortet wird in derselben Nummerierung – jede Nummer genau ihr Spiel, nichts vertauschen.

**Warnsignal ⚠️** (Nutzer 11.10., gilt ab dem Batch nach dieser Änderung; ersetzt die
frühere feste Regel): Ganz oben steht eine Übersicht je Nummer: Spiel | Wette | ⚠️ Gefahr.
Die Zeile `⚠️ **Gefahr:** …` (direkt unter der Wette, mit Feld und Zahl) kommt bei jeder
Wette, aber **nur**, wenn ein echtes Warnsignal in den Teamfeldern steckt – qualitativ
gelesen, ohne feste Grenzwerte. Schwerpunkt ist die Heim-Anfälligkeit.
- Heimsieg → ⚠️, wenn das Gastteam defensiv sehr stabil ist oder die Heim-Stärke nicht
  extrem ist.
- Auswärtssieg → ⚠️, wenn das Heimteam zu Hause klar anfällig ist (hohe Gegentore, hohe
  seasonConcededAVG oder hohe xG dagegen zu Hause). So vom Nutzer bestätigt.
- BTTS Ja / Over 2.5 → ⚠️, wenn eine Seite defensiv zu stabil ist oder die Varianz
  widersprüchlich ist. Under 2.5 sinngemäß: eine Seite offensiv zu stark oder Varianz
  widersprüchlich.
- Weitere echte Warnsignale (seltener): sehr enge xG-Differenz trotz leichtem Vorteil; hohe
  Varianz oder widersprüchliche letzte 6 bei sonst klarem Bild; beide Teams sehr stark und
  das Spiel eng (Top-Spiel).
Kein ⚠️ bei klarer, sauberer Stärke-Differenz ohne Heim-Anfälligkeit, bei solider
Heim-Abwehr des Gegners und wenn in den Teamfeldern kein Risiko erkennbar ist; dann in der
Übersicht „–“. Bei „keine“ steht in der Übersicht der Grund. Das ist nur die Darstellung –
an der Wahl der Wette ändert es nichts.

**Freigabe-Check** (Nutzer 15.10.: „bevor die Freigabe erteilt wird, doppelt und dreifach
prüfen"): Bevor eine Wette ohne ⚠️ rausgeht, drei Durchgänge:
1. Jedes ⚠️-Kriterium oben Spalte für Spalte prüfen – gesamt, zu Hause/auswärts, L6 gesamt
   **und** L6 zu Hause/auswärts.
2. Gleiche Signale gleich behandeln: Was im selben Batch oder am selben Tag bei einem Spiel
   ein ⚠️ bekommt (z. B. eine Abwehr mit wenig Gegentoren bei Over/BTTS), bekommt es bei
   jedem anderen Spiel mit demselben Signal auch.
3. Jede Zahl im Text gegen die Tabelle prüfen.
Auch das ist nur Darstellung – an der Wahl der Wette ändert es nichts.

**Auswerten** (Nutzer 14.10.): Sagt der Nutzer „auswerten“, sind nur die freigegebenen
Wetten gemeint – die ohne ⚠️ (und nicht „keine“) –, aus dem Zeitraum, den er nennt. Andere
nur, wenn er es ausdrücklich sagt.

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
