# Werkzeuge (Hilfsskripte, ohne Schlüssel)

Alle Skripte lesen den Schlüssel nur aus der Umgebungsvariable `ODDALERTS_KEY` und schwärzen
ihn in jeder Ausgabe als `[REDACTED]`.

- `oa.sh <pfad> [k=v ...]` – ein API-Abruf, z. B. `werkzeuge/oa.sh odds/history/420643055`.
  Letzte Zeile: `__HTTP <code>`.
- `ergebnisse.py <comp_ids> "<Heim>" "<Auswärts>" [cache.json]` – letzte 10 Pflichtspiele,
  Heim-/Auswärtsspiele und Direktvergleiche (Liga + Pokal-IDs angeben).
- `auswertung.py <comp_ids> "Heim|Auswärts" ...` – Endergebnisse für die Auswertung
  (Zeitraum im Skript).

Wettbewerbs-IDs (Auswahl): Bundesliga 477, 2. Bundesliga 471, DFB-Pokal 417,
Championship 418, FA Cup 327, Carabao Cup 268, La Liga 419, Serie A 499, Coppa Italia 531,
Serie B 545, Ligue 1 200, Ligue 2 256, Eredivisie 437, KNVB Beker 251, Pro League (BEL) 198,
Belgian Cup 258, Süper Lig 414, Turkish Cup 626, Allsvenskan 255, Svenska Cupen 34,
Admiral Bundesliga (AUT) 411.

Modell eines Spiels: `trends/btts?page=N` durchblättern, Eintrag mit `id` = Fixture-ID, Feld
`probability`.
