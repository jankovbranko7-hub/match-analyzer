# Regeln

**Das System ist `SYSTEM.md` – genau so, wie es dort steht, und nichts sonst.** Seit
10.10.2026 ist das das Paket „footystats-bild-wette" des Nutzers (`SYSTEM.md` = dessen
`SKILL.md`, dazu `references/`, `scripts/`, `evals/`, `CHANGELOG.md`), vom Nutzer als
„komplettes neues System" eingesetzt, „so ausführen ohne Widerrede". Es verlangt die
freiere, qualitative Gewichtung von Bild und Verlauf ohne Schwellen – genau so anwenden.
Die früheren Lesarten 1–5 gelten nicht mehr. Am 17.10. hat der Nutzer das System auf
den Stand vom 13.10. zurückgesetzt („zum System zurück, wo 100 % Trefferquote war“, „laut
den Spielen vom 13.10.“; bis 14.10. kam nur die Auswerten-Regel dazu, die keine Wette ändert): ohne
Freigabe-Check, ohne die Häufigkeits- und Ergebnisfelder, ohne Ligadaten im Europapokal und
ohne die Zusatzregel für Siegwetten vom 16.10.

Am 18.10. (nach den 65 Spielen vom 17.10.) hat der Nutzer das Spielbild neu ausgerichtet:
„je Team alle über 1000 Felder lesen“, „nicht starr nur Daten ablesen“, „offenes Hirn sowie
eine starke Philosophie, um ein perfektes Spielbild je Spiel zu erstellen“, Erfahrung und
Bauchgefühl dürfen einfließen. Seitdem steht in `SYSTEM.md` die Philosophie „erst die
Geschichte des Spiels, dann die Wette“ mit den sechs Fragen; die Tabellen zeigen alle
spielbezogenen Felder. Quoten und Rechenmodelle hat der Nutzer dafür nicht gewollt – sie
bleiben Kontext.

**Spiele kommen als Batch:** Der Nutzer schickt Batches zu je 5 Spielen, nummeriert, oft
mehrere Batches auf einmal (bis 20–30 Spiele). Jedes Spiel heißt „Batch X · Nr. Y“ – jede
Nummer genau ihr Spiel, nichts vertauschen. Im Chat: Übersicht aller Spiele und die Liste
der freigegebenen Wetten; die vollständige Analyse je Spiel als Datei.

**Warnsignal ⚠️** (Nutzer 11.10., gilt ab dem Batch nach dieser Änderung; ersetzt die
frühere feste Regel): Ganz oben steht eine Übersicht je Nummer: Spiel | Wette | ⚠️ Gefahr.
Die Zeile `⚠️ **Gefahr:** …` (direkt unter der Wette, mit Feld und Zahl) kommt bei jeder
Wette, aber **nur**, wenn ein echtes Warnsignal in den Teamfeldern steckt – qualitativ
gelesen, ohne feste Grenzwerte. Schwerpunkt ist die Heim-Anfälligkeit.
- Heimsieg → ⚠️, wenn das Gastteam defensiv sehr stabil ist. (Die frühere Bedingung „oder
  die Heim-Stärke nicht extrem ist“ ist am 18.10. entfallen – laut Nutzer das „Hindernis im
  System“, das am 17.10. 18 von 19 Heimsiegen gesperrt hat.)
- Jede Wette → ⚠️, wenn die Geschichte des Spiels einen echten Bruch hat, z. B. der Favorit
  kontrolliert, kassiert aber fast in jedem Spiel; oder der Schwächere trifft kaum, hält aber
  oft die Null.
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

**Auswerten** (Nutzer 14.10.): Sagt der Nutzer „auswerten“, sind nur die freigegebenen
Wetten gemeint – die ohne ⚠️ (und nicht „keine“) –, aus dem Zeitraum, den er nennt. Andere
nur, wenn er es ausdrücklich sagt.

## Technik (nicht Teil des Systems)

`SYSTEM.md` nennt `FOOTYSTATS_KEY`. In dieser Umgebung ist der Key als `APIKEY`
hinterlegt; beim Aufruf als `FOOTYSTATS_KEY="$APIKEY"` mitgeben. Fehlt er: dem Nutzer
sagen, dass er ihn in den Umgebungseinstellungen hinterlegen soll. Den Key **nie** im
Chat erfragen, ausgeben, loggen, in eine Datei schreiben oder committen.

Ein `HTTP 417` ist das Stundenlimit der API – dann warten.

Tabellen kommen aus `system/tabellen.py`: alle Felder je Team, gegliedert nach den sechs
Fragen aus `SYSTEM.md`; Ecken, Karten, Abseits, Fouls, Namen und Verwaltung werden nur
mitgelesen und mitverglichen. `--roh datei.json` schreibt alle Felder ungekürzt in eine
Datei (enthält keinen Key). Liefert die API bei einem Feld eine Liste (eine Torminute je
Tor), ist die Anzahl der Einträge der Wert. Fehlt das Feld, steht „fehlt".

Antworten auf Deutsch.
