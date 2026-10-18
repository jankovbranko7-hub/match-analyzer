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

   Gesamt, zu Hause und auswärts sind **Spalten**, keine eigene Regel. Eine Spalte wird nicht gewählt, nur weil dort eine Zahl steht.

3. **Letzte 6.**  
   Die letzten 6 **Ligaspiele** vor dem Anpfiff, gezählt aus `/league-matches?season_id=...` (`/lastx` mischt Pokal und Europapokal hinein). Dieselben Zeilen (Spiele, Tore, Gegentore, xG für, xG dagegen + Varianz-Felder, gesamt/home/away). Oder Form fehlt.

3a. **Vorsaison und Liga-Grundwerte.**  
   - Je Team die abgeschlossene Vorsaison aus `/team?team_id=...&include=stats` (Wettbewerb mit den meisten Spielen der Vorsaison): Spiele, xG für, xG dagegen, Tore und Gegentore pro Spiel – mit Vermerk, ob gleiche oder andere Liga.  
   - Je Spiel die Liga-Grundwerte der Vorsaison aus `/league-matches` der Vorsaison: Ø Tore, Over 2.5 %, BTTS %, Remis %, Heimsieg %.

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

Mögliche Ausgänge bleiben:
- Heimsieg oder Auswärtssieg (wenn Stärke und Verlauf zusammen klar darauf hindeuten).
- Over 2.5 oder BTTS Ja (wenn der Verlauf/Varianz dominiert oder beide Seiten offensiv).
- Under 2.5 (wenn beide Seiten niedrig treffen und kassieren).
- **keine**, wenn nichts klar dominiert oder die Signale zu widersprüchlich sind.

Es wird immer nur die **eine stärkste** Wette ausgegeben, die aus der freieren Gewichtung von Bild + Verlauf hervorgeht.

## Gewichtung nach Belastbarkeit

Weiter qualitativ und ohne Schwellen – aber mit dieser Reihenfolge des Vertrauens, weil sich manche Zahlen
von Spiel zu Spiel wiederholen und andere überwiegend Zufall sind:

1. **xG für / xG dagegen tragen mehr als Tore und Gegentore.** Gegentore schwanken am stärksten; eine Abwehr
   wird zuerst an xG dagegen gemessen, erst dann an den Gegentoren.
2. **Die Gesamtspalte ist die Basis, zu Hause / auswärts nur die Korrektur.** Aus 3–5 Heim- oder
   Auswärtsspielen sind die Werte meist Zufall. Der Heimvorteil kommt aus der Liga (Liga-Grundwerte), nicht
   aus der Heimtabelle eines einzelnen Teams.
3. **Früh in der Saison wiegt die Vorsaison mit** – je weniger Saisonspiele, desto mehr. Kommt die Vorsaison
   aus einer anderen (tieferen) Liga, wird sie entsprechend abgewertet.
4. **Letzte 6 sind ein Hinweis auf Veränderung, kein eigenes Signal.**
5. **Die Varianz-Felder (BTTS_and_lose/win, AVG_2hg) sind aus Ergebnissen gezählt und schwanken stark.** Sie
   färben den Verlauf, tragen eine Wette aber nur, wenn Tore und xG beider Seiten in dieselbe Richtung zeigen.
6. **Torzahl und BTTS: Ausgangspunkt sind die Liga-Grundwerte.** Davon weicht das Bild ab, wenn Angriff gegen
   Abwehr beider Seiten (eigene xG für gegen xG dagegen des Gegners, und umgekehrt) klar höher oder niedriger liegen.
7. **Sieg zu Null und Under:** Entscheidend ist, wie harmlos der Angriff des Gegners ist (xG für, Tore pro
   Spiel), mehr als die eigene Abwehr. Auch klare Favoriten kassieren oft ein Tor.
8. **Ein Remis ist nie der klare Ausgang**, aber bei gleich starken, torarmen Teams spricht es gegen eine
   Siegwette (dann eher Under oder keine).
9. **Ein sauberer Heimsieg hat fünf Merkmale:** angriffsstarkes Heimteam (xG für), klarer xG-Abstand gesamt,
   klarer Punkteabstand, wenig erwartete Tore für den Gast (Gast xG für gegen Heim xG dagegen) und ein Heimteam,
   das mindestens seine xG trifft. Jedes fehlende Merkmal macht ein Remis wahrscheinlicher.
10. **Jede Wettart hat ihr sauberes Profil** (Auswärtssieg: klarer xG- und Punkteabstand für den Gast, Gast trifft
    mindestens seine xG; Over: viele erwartete Tore, torreiche Teams und Liga; Under: das Gegenteil; BTTS: auch die
    schwächere Seite hat Tore zu erwarten, keins der Teams bleibt oft ohne Tor, Liga mit vielen Over-Spielen).
    Torwetten erreichen auch mit sauberem Profil selten mehr als 60–65 %, der saubere Heimsieg am meisten.

## Ausgabe

- Tabelle je Team (Heim zuerst, dann Gast). Spalten: Gesamt | zu Hause | auswärts. Zeilen: Spiele, Tore, Gegentore, xG für, xG dagegen + die Varianz-Felder. Danach letzte 6 analog. Unter jeder Tabelle die Vorsaison-Zeile, nach beiden Tabellen die Liga-Grundwerte.
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

# Ligaspiele der Saison (letzte 6) bzw. der Vorsaison (Liga-Grundwerte)
curl "https://api.football-data-api.com/league-matches?key=$FOOTYSTATS_KEY&season_id=SEASON_ID&max_per_page=1000"

# Team mit allen Saisons (Vorsaison)
curl "https://api.football-data-api.com/team?key=$FOOTYSTATS_KEY&team_id=TEAM_ID&include=stats"
```

Nutze `bash` mit `curl` oder `browser_execute` zum Abrufen. Parsen mit Python in `/tmp` falls nötig. Speichere Zwischenergebnisse nicht dauerhaft.

## Regeln (strikt)

- Exakte Spielzuordnung. Ähnlicher Name = falsches Spiel.
- Heim komplett, dann Gast komplett.
- Keine Schätzung. Fehlt = „fehlt“.
- Gesamt/zu Hause/auswärts = Spalten.
- Wette **nur** aus Teamfeldern (Spiele/Tore/Gegentore/xG + Varianz-Felder + letzte 6 + Vorsaison), mit freierer Gewichtung und Interpretation der Zahlen (keine Schwellen) nach der Gewichtung nach Belastbarkeit; die Liga-Grundwerte sind der Ausgangspunkt für Torzahl und BTTS.
- Gemeinsame Felder (Pre-Match-xG, BTTS, Over/Under) = Kontext only.
- Zweimal lesen. Abweichung → keine Wette.
- Ausgabe: Tabellen → Bild-Satz (mit freierer Begründung) → eine Wette oder „keine“.

Siehe `references/field_mapping.md` für exakte Feldnamen.
