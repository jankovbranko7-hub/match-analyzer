---
name: footystats-bild-wette
description: "Analysiere Fußballspiele mit der FootyStats-API: extrahiere Teamfelder (Spiele, Tore, Gegentore, xG für/dagegen gesamt/zu Hause/auswärts + letzte 6), bilde ein Bild in einem Satz aus den Teamfeldern und schlage eine Wette nur daraus vor (Heimsieg, Auswärtssieg, BTTS Ja, Over 2.5, Under 2.5) oder keine. Nutze wenn der Nutzer Spiele für Bild und Wette schickt."
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
   - xG für (`xg_for_overall/home/away` — Total, nicht Avg)  
   - xG dagegen (`xg_against_overall/home/away`)  

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

## Bild-Interpretation (Spielverlauf stärker gewichten)

Das Bild beschreibt nicht nur die reine Stärke, sondern den **möglichen Spielverlauf** aus den Teamfeldern:

1. **Beide Seiten offensiv + defensiv schwach**  
   Beide Teams hohe Tore **und** hohe Gegentore (bzw. hohe xG für **und** hohe xG dagegen):  
   → Bild: „Beide Teams treffen und kassieren regelmäßig.“  
   → Wette bevorzugt **Over 2.5** oder **BTTS Ja**.

2. **Eine Seite klar stärker, Gegner trifft aber auch**  
   Team A deutlich bessere xG-Bilanz, Team B zeigt trotzdem solide Tore/xG für:  
   → Bild: „A ist klar stärker, B trifft aber regelmäßig.“  
   → Sieg möglich, zusätzlich **BTTS Ja** in Betracht ziehen.

3. **Beide Seiten sehr defensiv**  
   Beide Teams niedrige Tore **und** niedrige Gegentore:  
   → Bild: „Beide Teams treffen und kassieren wenig.“  
   → Wette bevorzugt **Under 2.5**.

4. **Home/Away-Unterschiede**  
   Starke Unterschiede zwischen zu Hause und auswärts im Bild erwähnen und gewichten.

5. **Last 6 gewichten**  
   Wenn die letzten 6 Spiele ein anderes Bild zeigen als die Saison, das im Bild erwähnen.

Die Wette folgt weiterhin **nur** den Teamfeldern. Die zusätzlichen Regeln dienen nur dazu, den Verlauf besser abzubilden und nicht automatisch nur Sieg-Wetten zu erzeugen.

## Wie die Wette aus dem Bild entsteht

Nach dem Bild in einem Satz wird die Wette **ausschließlich** aus den Teamfeldern abgeleitet:

- **Heimsieg / Auswärtssieg**: Wenn ein Team klar höhere Tore/xG für **und** niedrigere Tore/xG dagegen hat (Saison + Last 6 + Home/Away-Spalten).
- **BTTS Ja**: Wenn beide Teams regelmäßig Tore schießen (hohe Tore + hohe xG für) **und** beide kassieren (hohe Gegentore + hohe xG dagegen).
- **Over 2.5**: Wenn beide Teams hohe Tore **und** hohe Gegentore zeigen (oder hohe xG für **und** hohe xG dagegen auf beiden Seiten).
- **Under 2.5**: Wenn beide Teams niedrige Tore **und** niedrige Gegentore zeigen.
- **Keine**: Wenn die Zahlen widersprüchlich sind, die Differenz zu klein ist oder die Felder keine klare Richtung tragen.

Die Bild-Interpretationsregeln (oben) helfen dabei, den Verlauf zu erkennen und die passende Wette zu wählen. Die Wette selbst kommt immer nur aus den abgelesenen Teamfeldern.

## Ausgabe

- Tabelle je Team (Heim zuerst, dann Gast). Spalten: Gesamt | zu Hause | auswärts. Zeilen: Spiele, Tore, Gegentore, xG für, xG dagegen. Danach letzte 6 analog.
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
- Wette **nur** aus Teamfeldern (Spiele/Tore/Gegentore/xG gesamt+home+away + letzte 6).
- Gemeinsame Felder (Pre-Match-xG, BTTS, Over/Under) = Kontext only.
- Zweimal lesen. Abweichung → keine Wette.
- Ausgabe: Tabellen → Bild-Satz → Wette oder „keine“.

Siehe `references/field_mapping.md` für exakte Feldnamen.
