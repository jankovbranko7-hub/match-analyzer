---
name: footystats-bild-wette
description: "Analysiere Fußballspiele mit der FootyStats-API: extrahiere Teamfelder (Spiele, Tore, Gegentore, xG für/dagegen gesamt/zu Hause/auswärts + letzte 6 + Varianz-Felder), bilde ein Bild in einem Satz aus den Teamfeldern und schlage eine Wette nur daraus vor (Heimsieg, Auswärtssieg, BTTS Ja, Over 2.5, Under 2.5) oder keine. Nutze wenn der Nutzer Spiele für Bild und Wette schickt."
type: workflow
lifecycle: active
---

# FootyStats Bild und Wette

Extrahiere exakte Teamdaten aus der FootyStats-API, zeige Tabellen je Team, bilde ein Bild in einem Satz aus den Teamfeldern und schlage eine Wette nur aus diesen Feldern vor. Gemeinsame Felder sind nur Kontext.

**API Key:** aus der Umgebungsvariable `FOOTYSTATS_KEY` (nicht in Dateien)  
**Base:** `https://api.football-data-api.com`  
Keine Prüfsumme. Kein Schätzen fehlender Felder — schreibe „fehlt“.

## Workflow (immer in dieser Reihenfolge)

1. **Spiel exakt zuordnen.**  
   Nutze `/todays-matches` (mit `date=YYYY-MM-DD` falls gegeben) oder `/match?match_id=`.  
   Ein ähnlicher Name ist das falsche Spiel. Nur exakte Zuordnung (Name + Datum/Liga wenn möglich). Sonst keine Analyse.

2. **Heimteam komplett, dann Gastteam komplett.**  
   Hole Teamdaten mit `/league-teams?season_id=...&include=stats` (season_id aus Match oder Liga).  
   Für jedes Team die Spalten **Gesamt / zu Hause / auswärts**:  
   - Spiele (`seasonMatchesPlayed_overall/home/away`)  
   - Tore (`seasonGoals_overall/home/away`)  
   - Gegentore (`seasonConceded_overall/home/away`)  
   - xG für (`xg_for_avg_overall/home/away` — Avg, da Totals oft leer)  
   - xG dagegen (`xg_against_avg_overall/home/away`)  
   - Zusätzlich für Verlauf:  
     - `seasonScoredAVG_overall` / `seasonConcededAVG_overall`  
     - `BTTS_and_lose_percentage_overall` / `BTTS_and_win_percentage_overall`  
     - `AVG_2hg_overall` (Tore in der 2. Halbzeit)
   - Zusätzlich (Nutzer 18.10.), je gesamt/zu Hause/auswärts:
     - Schüsse aufs Tor pro Spiel für (`shotsOnTargetAVG_*`) und gegen (aus den Ligaspielen der Saison gezählt, `team_a_shotsOnTarget`/`team_b_shotsOnTarget`)
     - Punkte pro Spiel (`seasonPPG_*`) und Tabellenplatz (`leaguePosition_*`)
     - Erstes Tor erzielt % (`firstGoalScoredPercentage_*`) und Führung zur Pause % (`leadingAtHTPercentage_*`)
   - Je Spiel das **Torniveau der Liga**: Ø Tore und Over-2.5-Quote der laufenden Saison (Spiele vor dem Anpfiff) und der Vorsaison (`/league-matches`).

   Gesamt, zu Hause und auswärts sind **Spalten**, keine eigene Regel. Eine Spalte wird nicht gewählt, nur weil dort eine Zahl steht.

3. **Letzte 6.**  
   `/lastx?team_id=...` — bevorzuge `last_x_match_num=6`. Dieselben Zeilen (Spiele, Tore, Gegentore, xG für, xG dagegen gesamt/home/away). Oder Form fehlt.

4. **Gemeinsam, nur als Kontext.**  
   Aus `/match?match_id=`:  
   - Pre-Match-xG Heim, Pre-Match-xG Gast (oder `avg_potential` als Proxy)  
   - BTTS (`btts_potential`)  
   - Over / Under (`o25_potential`, `u25_potential` oder Odds)  
   Diese Felder **nicht zur Wette** verwenden.

5. **Dieselbe Antwort ein zweites Mal lesen.** Weicht sie ab, keine Wette.

Ein fehlendes Feld heißt **fehlt** und wird nie geschätzt.

## Bild und Verlauf bestimmen die Wette

Das **Spiel-Bild** (Stärke aus Tore/xG, Home/Away-Splits, Last 6) und der **Spielverlauf** (Varianz-Felder wie BTTS_and_lose, AVG_2hg, Scored/ConcededAVG und deren Zusammenspiel) bestimmen gemeinsam die eine Wette.

Die Zahlen werden **freier gewichtet und interpretiert**:
- Last 6 kann stärker oder schwächer gegenüber der Saison gewichtet werden, je nachdem wie klar und konsistent sie sind.
- Home/Away-Splits werden qualitativ stärker oder schwächer gelesen, ohne feste Grenzen.
- Absolute und relative Differenzen in Tore/xG werden im Zusammenhang mit den Varianz-Feldern beurteilt.
- Widersprüche zwischen Saisonbild und Verlauf werden freier abgewogen (z. B. gute xG-Bilanz + hohe BTTS_and_lose → Verlauf gewinnt; klare Stärke + niedrige Varianz → Sieg).
- Es gibt **keine Schwellen oder festen Grenzwerte**. Die Interpretation bleibt qualitativ und begründet.
- Was die präzisen Daten über das nächste Spiel sagen (Nutzer 18.10.):
  1. **xG und Schüsse aufs Tor, für und gegen**, zeigen, wie viele und wie gute Chancen ein Team herausspielt und zulässt; sie wiederholen sich am stärksten und gehen Toren und Gegentoren vor.
  2. **Tore pro Spiel:** Der Angriff zeigt sich schneller und beständiger als die Abwehr.
  3. **Das Torniveau der Liga** ist der Ausgangspunkt für Over/Under – in einer torarmen Liga fallen weniger Tore, egal welche Teams spielen.
  4. **Punkte und Tabellenplatz** sind ein echter Stärkewert, früh in der Saison aber noch stark vom Glück geprägt.
  5. **Erstes Tor erzielt und Führung zur Pause** messen vor allem Stärke und bestätigen das Bild eher, als dass sie etwas Neues zeigen.

Mögliche Ausgänge bleiben:
- Heimsieg oder Auswärtssieg (wenn Stärke und Verlauf zusammen klar darauf hindeuten).
- Over 2.5 oder BTTS Ja (wenn der Verlauf/Varianz dominiert oder beide Seiten offensiv).
- Under 2.5 (wenn beide Seiten niedrig treffen und kassieren).
- **keine**, wenn nichts klar dominiert oder die Signale zu widersprüchlich sind.

Es wird immer nur die **eine stärkste** Wette ausgegeben, die aus der freieren Gewichtung von Bild + Verlauf hervorgeht.

## Ausgabe

- Tabelle je Team (Heim zuerst, dann Gast). Spalten: Gesamt | zu Hause | auswärts. Zeilen: Spiele, Tore, Gegentore, xG für, xG dagegen + die Varianz-Felder + Schüsse aufs Tor für/gegen, Punkte pro Spiel, Tabellenplatz, erstes Tor erzielt %, Führung zur Pause %. Danach letzte 6 analog. Nach beiden Tabellen das Torniveau der Liga.
- Danach das **Bild in einem Satz** aus den Teamfeldern (nicht aus gemeinsamen Feldern).
- Danach eine **Wette nur aus den Teamfeldern**: Heimsieg, Auswärtssieg, BTTS Ja, Over 2.5 oder Under 2.5.  
  Tragen die Teamfelder keine Wette, steht dort **keine**.  
  Die gemeinsamen Felder werden nicht zur Wette.

## API-Aufrufe (Beispiele)

```bash
# Heutige Spiele
curl "https://api.football-data-api.com/todays-matches?key=$FOOTYSTATS_KEY"

# Match Details
curl "https://api.football-data-api.com/match?key=$FOOTYSTATS_KEY&match_id=MATCH_ID"

# Team Stats
curl "https://api.football-data-api.com/league-teams?key=$FOOTYSTATS_KEY&season_id=SEASON_ID&include=stats"

# Last 6
curl "https://api.football-data-api.com/lastx?key=$FOOTYSTATS_KEY&team_id=TEAM_ID"
```

Nutze `bash` mit `curl` oder `browser_execute` zum Abrufen. Parsen mit Python in `/tmp` falls nötig. Speichere Zwischenergebnisse nicht dauerhaft.

## Regeln (strikt)

- Exakte Spielzuordnung. Ähnlicher Name = falsches Spiel.
- Heim komplett, dann Gast komplett.
- Keine Schätzung. Fehlt = „fehlt“.
- Gesamt/zu Hause/auswärts = Spalten.
- Wette **nur** aus Teamfeldern (Spiele/Tore/Gegentore/xG + Varianz-Felder + Schüsse aufs Tor, Punkte, Tabellenplatz, erstes Tor, Führung zur Pause + letzte 6; das Torniveau der Liga als Ausgangspunkt für Over/Under), mit freierer Gewichtung und Interpretation der Zahlen (keine Schwellen).
- Gemeinsame Felder (Pre-Match-xG, BTTS, Over/Under) = Kontext only.
- Zweimal lesen. Abweichung → keine Wette.
- Ausgabe: Tabellen → Bild-Satz (mit freierer Begründung) → eine Wette oder „keine“.

Siehe `references/field_mapping.md` für exakte Feldnamen.
