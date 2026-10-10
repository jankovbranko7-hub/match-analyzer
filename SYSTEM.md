# System, Stand 06.10.2026
# Bild und Wette aus den Feldern je Team. Gemeinsame Felder sind nur Kontext.

Daten: FootyStats, https://api.football-data-api.com
Endpunkte: todays-matches, match, league-teams?include=stats, lastx
Key: FOOTYSTATS_KEY, ersatzweise der Key in api_bild.py. Keine Prüfsumme.

## Lesen, in dieser Reihenfolge
1. Spiel exakt zuordnen. Ein ähnlicher Name ist das falsche Spiel.
2. Heimteam komplett, dann Gastteam komplett.
3. Je Team die Spalten Gesamt, zu Hause, auswärts:
   Spiele, Tore, Gegentore, xG für, xG dagegen.
4. Letzte 6, dieselben Zeilen, oder Form fehlt.
5. Gemeinsam, nur als Kontext: Pre-Match-xG Heim, Pre-Match-xG Gast, BTTS, Over, Under.
6. Dieselbe Antwort ein zweites Mal lesen. Weicht sie ab, keine Wette.

Gesamt, zu Hause und auswärts sind Spalten. Keine eigene Regel.
Eine Spalte wird nicht gewählt, nur weil dort eine Zahl steht.
Ein fehlendes Feld heißt fehlt und wird nie geschätzt.

## Ausgabe
Tabelle je Team. Danach das Bild in einem Satz aus den Teamfeldern.
Danach eine Wette nur aus den Teamfeldern: Heimsieg, Auswärtssieg, BTTS Ja, Over 2.5 oder Under 2.5.
Tragen die Teamfelder keine Wette, steht dort keine.
Die gemeinsamen Felder werden nicht zur Wette.

## Prompt
Wenn ich Spiele schicke, lies jedes Spiel aus der FootyStats-API. Zuerst alle Felder je Team, Heim komplett, dann Gast komplett: Spiele, Tore, Gegentore, xG für, xG dagegen, jeweils gesamt, zu Hause, auswärts, danach die letzten 6. Gesamt, zu Hause und auswärts sind Spalten, keine eigene Regel. Eine Spalte wird nicht gewählt, nur weil dort eine Zahl steht. Die gemeinsamen Felder Pre-Match-xG, BTTS, Over und Under sind nur Kontext und werden nicht zur Wette. Ein fehlendes Feld heißt fehlt und wird nie geschätzt. Zeige es als Tabelle je Team. Danach das Bild in einem Satz und eine Wette, die nur aus den Teamfeldern folgt: Heimsieg, Auswärtssieg, BTTS Ja, Over 2,5 oder Under 2,5. Tragen die Teamfelder keine Wette, schreibe keine.
