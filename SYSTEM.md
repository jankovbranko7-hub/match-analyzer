---
name: footystats-bild-wette
description: "Analysiere Fußballspiele mit der FootyStats-API: lies je Team alle Felder (gesamt/zu Hause/auswärts + letzte 6), baue daraus mit offenem Kopf die Geschichte des Spiels – wer hat es in der Hand, wie beginnt es, was passiert nach dem ersten Tor, trifft der Schwächere, wie nah ist ein Remis, wie belastbar sind die Zahlen – und schlage eine Wette daraus vor (Heimsieg, Auswärtssieg, BTTS Ja, Over 2.5, Under 2.5) oder keine. Nutze wenn der Nutzer Spiele für Bild und Wette schickt."
type: workflow
lifecycle: active
---

# FootyStats Spielbild und Wette

Lies je Team **alle Felder**, die die API liefert, baue daraus die **Geschichte des Spiels** und schlage
eine Wette nur aus dieser Geschichte vor. Nicht starr Zahlen ablesen: Die Zahlen sind das Material,
das Spielbild entsteht aus ihrem Zusammenspiel und aus Erfahrung. Gemeinsame Felder sind nur Kontext.

**API Key:** aus der Umgebungsvariable `FOOTYSTATS_KEY` (nicht in Dateien)  
**Base:** `https://api.football-data-api.com`  
Kein Schätzen fehlender Felder — schreibe „fehlt“.

## Workflow (immer in dieser Reihenfolge)

1. **Spiel exakt zuordnen.**  
   Über `/league-matches?season_id=…` oder `/match?match_id=`. Ein ähnlicher Name ist das falsche Spiel.
   Nur exakte Zuordnung (Name + Datum/Liga). Sonst keine Analyse.

2. **Heimteam komplett, dann Gastteam komplett – alle Felder.**  
   `/league-teams?season_id=...&include=stats`: je Team über 1.000 Felder, jeweils in den Spalten
   **gesamt / zu Hause / auswärts**. Alle werden gelesen. Ecken, Karten, Abseits, Fouls, Teamnamen in
   anderen Sprachen und Verwaltungsfelder betreffen keine der fünf Wetten; sie werden mitgelesen, aber
   nicht für das Bild verwendet.

3. **Letzte 6.**  
   `/lastx?team_id=...`, Eintrag `last_x_match_num=6`, dieselben Felder. Die API zählt dabei alle
   Wettbewerbe (auch Pokal und Europapokal) – das beim Lesen berücksichtigen.

4. **Gemeinsam, nur als Kontext.**  
   Aus `/match?match_id=`: Pre-Match-xG, `btts_potential`, `o25_potential`, `u25_potential`, Quoten.
   Der direkte Vergleich (`h2h`) ist Hintergrund. Diese Felder entscheiden die Wette **nicht**.

5. **Dieselbe Antwort ein zweites Mal lesen.** Weicht ein Wert ab, keine Wette.

## Die Philosophie: erst die Geschichte des Spiels, dann die Wette

Für jedes Spiel werden sechs Fragen beantwortet, jede aus den passenden Feldern beider Teams
(Heimteam vor allem zu Hause, Gastteam vor allem auswärts, gesamt und letzte 6 dazu):

1. **Wer hat das Spiel in der Hand?** – Stärke, Kontrolle, Form: xG für/dagegen, Tore, Gegentore,
   Schüsse und Schüsse aufs Tor, Ballbesitz, (gefährliche) Angriffe, Punkte pro Spiel, Siege/Niederlagen,
   Tabellenplatz, Heimvorteil.
2. **Wie beginnt das Spiel?** – Wer schießt das erste Tor, wer führt oder liegt zur Pause hinten,
   Tore der 1. Halbzeit, in welchen Minuten die Tore fallen.
3. **Was passiert nach dem ersten Tor?** – Verwaltet der Führende oder öffnet sich das Spiel:
   2. Halbzeit (Tore, Siege, Punkte, zu Null), BTTS_and_win/lose, Tore in beiden Halbzeiten.
4. **Trifft der Schwächere, hält der Starke die Null?** – Spiele zu Null, Spiele ohne eigenes Tor,
   BTTS-Anteil, Anteile Over/Under.
5. **Wie nah ist ein Remis?** – Remis-Anteil, Remis zur Pause, Remis mit beiderseitigen Toren.
6. **Wie belastbar sind die Zahlen?** – Wie viele Spiele dahinterstehen, Ausreißer, Saison gegen
   letzte 6, Pokal- und Europaspiele in den letzten 6, direkter Vergleich als Hintergrund.

**Mit offenem Kopf gewichten – ohne Schwellen und feste Grenzwerte.**
- Eine Zahl aus wenigen Spielen oder mit einem Ausreißer wiegt weniger als ein Muster, das sich durch
  viele Felder und Spalten zieht.
- Widersprüche werden abgewogen, nicht mechanisch aufgelöst.
- Erfahrung und Einschätzung, wie solche Spiele typischerweise laufen, gehören ausdrücklich dazu –
  begründet, nicht geraten.

**Die Geschichte in einem Satz bestimmt die Wette.** Zum Beispiel:
- Favorit kontrolliert, trifft früh, der Gegner kommt kaum zu Chancen → **Heimsieg / Auswärtssieg**.
- Beide spielen offen, beide treffen, das Spiel kippt hin und her → **Over 2.5 / BTTS Ja**.
- Zähes Spiel, wenige Chancen, beide oft ohne Tor oder zu Null → **Under 2.5**.
- Die Geschichte passt nicht zusammen → **keine**.

Es wird immer nur die **eine** Wette ausgegeben, die am besten zur Geschichte passt.

## Ausgabe

- Je Team (Heim zuerst, dann Gast) die Tabellen mit allen spielbezogenen Feldern, gegliedert nach den
  sechs Fragen. Spalten: gesamt | zu Hause | auswärts | L6 gesamt | L6 zu Hause | L6 auswärts.
- Danach Kontext und direkter Vergleich (nicht zur Wette).
- Danach die **Geschichte des Spiels in einem Satz** aus den Teamfeldern.
- Danach **eine Wette**: Heimsieg, Auswärtssieg, BTTS Ja, Over 2.5 oder Under 2.5. Trägt die Geschichte
  keine Wette, steht dort **keine**.

## API-Aufrufe (Beispiele)

```bash
# Spiele einer Saison (zum Finden)
curl "https://api.football-data-api.com/league-matches?key=$FOOTYSTATS_KEY&season_id=SEASON_ID&max_per_page=1000"

# Match Details (Kontext, direkter Vergleich)
curl "https://api.football-data-api.com/match?key=$FOOTYSTATS_KEY&match_id=MATCH_ID"

# Team Stats (alle Felder)
curl "https://api.football-data-api.com/league-teams?key=$FOOTYSTATS_KEY&season_id=SEASON_ID&include=stats"

# Letzte 6
curl "https://api.football-data-api.com/lastx?key=$FOOTYSTATS_KEY&team_id=TEAM_ID"
```

Tabellen erzeugt `system/tabellen.py` (doppelte Lesung, Gegenprobe über alle Felder).

## Regeln (strikt)

- Exakte Spielzuordnung. Ähnlicher Name = falsches Spiel.
- Heim komplett, dann Gast komplett – alle Felder.
- Keine Schätzung. Fehlt = „fehlt“.
- Gesamt/zu Hause/auswärts/letzte 6 = Spalten.
- Wette **nur** aus den Teamfeldern, über die Geschichte des Spiels, mit offener Gewichtung (keine Schwellen).
- Gemeinsame Felder (Pre-Match-xG, Potentiale, Quoten, direkter Vergleich) = Kontext/Hintergrund.
- Zweimal lesen. Abweichung → keine Wette.
- Ausgabe: Tabellen → Geschichte in einem Satz → eine Wette oder „keine“.

Siehe `references/field_mapping.md` für Feldnamen und Zuordnung zu den sechs Fragen.
