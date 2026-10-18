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

Am 18.10. wurden „alle über 1000 Felder“ und eine neue Spielbild-Philosophie getestet
(blind an den 13 freigegebenen Spielen vom 17.10.: keine höhere Trefferquote). Der Nutzer
hat entschieden: „wir lassen alles beim Alten“ – es gilt weiter der Stand vom 13.10.
Die danach am 18.10. eingebauten Änderungen (Gewichtung, Vorsaison, Liga-Grundwerte,
Remis-Check, Profil-Checks) sind wieder entfernt – Nutzer: „Du hast das gesamte System
durcheinander gebracht“. Es gilt der Stand vom 13.10.

**Keine Backtests** (Nutzer 18.10., ausdrücklich): Keine alten Spiele nachrechnen, um daraus
Regeln, Grenzwerte oder Systemänderungen abzuleiten. Auswerten heißt weiter nur: die
freigegebenen Wetten eines genannten Zeitraums gegen die echten Ergebnisse prüfen.

Danach, am 18.10. (Nutzer: „Ja“): Zum Stand vom 13.10. kommen fünf Punkte dazu, die aus
den präzisen Daten am meisten über das nächste Spiel sagen – xG und Schüsse aufs Tor für
und gegen (vor Toren/Gegentoren), Tore pro Spiel, Torniveau der Liga (Ausgangspunkt für
Over/Under), Punkte und Tabellenplatz, erstes Tor erzielt und Führung zur Pause. Weiter
ohne Schwellen, ohne Backtests; die ⚠️-Regel vom 11.10. bleibt unverändert.

**Spiele kommen als Batch:** Der Nutzer schickt Batches zu je 5 Spielen, nummeriert, oft
mehrere Batches auf einmal (bis 20–30 Spiele). Jedes Spiel heißt „Batch X · Nr. Y“ – jede
Nummer genau ihr Spiel, nichts vertauschen. Im Chat: Übersicht aller Spiele und die Liste
der freigegebenen Wetten; die vollständige Analyse je Spiel als Datei.

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
- **Für jede Wettart** (Nutzer 18.10.: „Diese Punkte, die übersehen worden sind, sollen auf
  die ganzen Wettarten einfließen“) ⚠️, wenn:
  - die Stärke eines Teams vor allem aus der anderen Spalte kommt (Gast stark nur zu
    Hause, Heimteam stark nur auswärts) – bei Torwetten sinngemäß: die torreichen bzw.
    torarmen Spiele eines Teams liegen vor allem in der anderen Spalte;
  - die Wette auf der Seite steht, die nur die Tore und nicht die xG tragen (z. B.
    Siegwette gegen ein Team, das deutlich unter seinen xG trifft; Under, obwohl beide
    Teams unter ihren xG treffen; Over/BTTS, obwohl ein Team deutlich über seinen xG trifft).
    Lesart (Nutzer 18.10.: „Bleibt bei der Lesart“): Bei Over/BTTS ⚠️ nur, wenn die Wette
    allein von den Toren getragen wird; tragen die xG-Summen sie auch ohne den
    Torüberschuss, kein ⚠️. Weniger Gegentore als xG dagegen spricht nicht gegen Over/BTTS
    (wie `SYSTEM.md`: ein solches Team kassiert eher wieder);
  - die tragenden Werte nur auf wenigen Spielen stehen.
  Beispiel Carrarese – Modena (17.10., 2:1): Modenas xG 2,95 zu Hause, aber nur 1,49
  auswärts; Carrarese zu Hause 0,33 Tore bei 1,17 xG; nur 3 Spiele je Spalte.
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

Tabellen kommen aus `system/tabellen.py` mit den Feldern aus `SYSTEM.md`. Dazu die Zeilen Schüsse aufs Tor für/gegen (gegen aus `/league-matches` gezählt, L6 „fehlt“), Punkte pro Spiel, Tabellenplatz (nur Saison), erstes Tor %, Führung zur Pause % und die Zeile „Torniveau der Liga“. Liefert die API
bei `seasonGoals_*`/`seasonConceded_*` eine Liste (eine Torminute je Tor), ist die Anzahl
der Einträge die Torzahl. Fehlt das Feld (z. B. letzte 6 zu Hause/auswärts), steht „fehlt".

Antworten auf Deutsch.
