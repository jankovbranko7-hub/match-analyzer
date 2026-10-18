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
Danach hat er die Verbesserung des Spielbilds je Team in Auftrag gegeben („mach dich auf
die Suche“, Bericht `reports/Spielbild je Team verbessern.md`) und die Auswahl übertragen
(„Du bist hier der Spezialist“). Übernommen wurde, was im Blindtest an allen 65 Spielen
vom 17.10. besser war: System vom 13.10. plus „Gewichtung nach Belastbarkeit“, Vorsaison,
Liga-Grundwerte und letzte 6 nur aus Ligaspielen (freigegeben 12/20 statt 10/24). Die zehn
Zeilen und alles Übrige vom 13.10. bleiben.

**Spiele kommen als Batch:** Der Nutzer schickt Batches zu je 5 Spielen, nummeriert, oft
mehrere Batches auf einmal (bis 20–30 Spiele). Jedes Spiel heißt „Batch X · Nr. Y“ – jede
Nummer genau ihr Spiel, nichts vertauschen. Im Chat: Übersicht aller Spiele und die Liste
der freigegebenen Wetten; die vollständige Analyse je Spiel als Datei.

**Warnsignal ⚠️** (Nutzer 11.10., gilt ab dem Batch nach dieser Änderung; ersetzt die
frühere feste Regel): Ganz oben steht eine Übersicht je Nummer: Spiel | Wette | ⚠️ Gefahr.
Die Zeile `⚠️ **Gefahr:** …` (direkt unter der Wette, mit Feld und Zahl) kommt bei jeder
Wette, aber **nur**, wenn ein echtes Warnsignal in den Teamfeldern steckt – qualitativ
gelesen, ohne feste Grenzwerte. Schwerpunkt ist die Heim-Anfälligkeit.
- Heimsieg → ⚠️, wenn das Gastteam defensiv sehr stabil ist (vor allem niedrige xG
  dagegen) oder der Stärkeunterschied insgesamt nicht klar ist (Gesamtspalte; früh in der
  Saison mit der Vorsaison). Seit 18.10. statt „die Heim-Stärke nicht extrem ist“: Die
  Heimwerte eines Teams aus wenigen Spielen sind meist Zufall.
  **Remis-Gefahr** (Nutzer 18.10.: „wieso und warum … das musst du erkennen“): Heimsieg nur
  ohne ⚠️, wenn das Bild sauber ist – Heimteam angriffsstark (xG für), klarer xG-Abstand
  gesamt, klarer Punkteabstand, der Gast hat gegen diese Abwehr wenig zu erwarten
  (erwartete Gasttore = Gast xG für und Heim xG dagegen gemittelt), das Heimteam trifft
  mindestens seine xG. Fehlt einer dieser Punkte, ⚠️ „Remis-Gefahr: …“ mit Feld und Zahl.
  Die Zeile „Remis-Check“ aus `system/tabellen.py` zeigt die fünf Werte mit Anhaltspunkten
  aus 6.264 Ligaspielen (keine festen Grenzen, knappe Werte qualitativ abwägen). Belegt:
  Heimfavoriten ohne Hinweis gewannen zu 77 % (Remis 14 %), mit einem zu 65 %, mit zwei
  und mehr zu 54 % (Remis 25 %).
- Auswärtssieg → ⚠️, wenn das Heimteam zu Hause klar anfällig ist (hohe Gegentore, hohe
  seasonConcededAVG oder hohe xG dagegen zu Hause). So vom Nutzer bestätigt.
- BTTS Ja / Over 2.5 → ⚠️, wenn eine Seite defensiv zu stabil ist oder die Varianz
  widersprüchlich ist. Under 2.5 sinngemäß: eine Seite offensiv zu stark oder Varianz
  widersprüchlich.
- **Profil-Checks für alle Wettarten** (Nutzer 18.10.: „Und wie sieht es mit den anderen
  Wettarten aus“): Jede Wette braucht ihr sauberes Profil, sonst ⚠️ mit dem fehlenden
  Merkmal. Die Zeilen aus `system/tabellen.py` zeigen Werte und Anhaltspunkte (keine
  festen Grenzen, knappe Werte qualitativ abwägen):
  - Auswärtssieg: klarer xG-Abstand und klarer Punkteabstand zugunsten des Gastes, der Gast
    trifft mindestens seine xG.
  - Over 2.5: viele erwartete Tore (xG beider Seiten gegeneinander), viele Tore in den
    Spielen beider Teams, torreiche Liga.
  - Under 2.5: wenige erwartete Tore, wenige Tore in den Spielen beider Teams, torarme Liga.
  - BTTS Ja: auch die schwächere Seite hat Tore zu erwarten, keins der Teams bleibt oft
    ohne Tor, Liga mit vielen Over-Spielen.
  Belegte Obergrenzen bei sauberem Profil: Heimsieg 76 %, Over 64 %, BTTS 64 %,
  Auswärtssieg 58 %, Under 53 %. Torwetten bleiben auch sauber nahe 60 %, Under ist am
  schwächsten – das in der Übersicht ehrlich so sagen.
- Weitere echte Warnsignale (seltener): sehr enge xG-Differenz trotz leichtem Vorteil; hohe
  Varianz oder widersprüchliche letzte 6 bei sonst klarem Bild; beide Teams sehr stark und
  das Spiel eng (Top-Spiel); ein Wert, der die Wette trägt, beruht nur auf wenigen Spielen
  oder einem Ausreißer.
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

Tabellen kommen aus `system/tabellen.py` mit den Feldern aus `SYSTEM.md`: Saisonspalten aus
`/league-teams`, letzte 6 aus den Ligaspielen (`/league-matches`), Vorsaison aus `/team`,
Liga-Grundwerte aus `/league-matches` der Vorsaison; alles zweimal gelesen. Liefert die API
bei `seasonGoals_*`/`seasonConceded_*` eine Liste (eine Torminute je Tor), ist die Anzahl
der Einträge die Torzahl. Fehlt ein Feld, steht „fehlt".

Antworten auf Deutsch.
