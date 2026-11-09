# Werkzeuge (FootyStats und Odd Alerts, ohne Schlüssel)

Alle Skripte lesen die Schlüssel nur aus der Umgebung (`APIKEY` für FootyStats, `ODDALERTS_KEY`
für Odd Alerts) und schwärzen sie als `[REDACTED]`. Keine Quoten.

- `fs.sh <pfad> [k=v ...]` – ein API-Abruf, z. B. `werkzeuge/fs.sh match match_id=8572478`.
  Letzte Zeile: `__HTTP <code>`.
- `fs_spiel.py <season_id> "<Heim-Teilname>" "<Auswärts-Teilname>"` – alle FootyStats-Daten zu
  einem Spiel für den Forebet-Check v2 (Vorab-xG, Saison, Heim/Auswärts, letzte 6 aller
  Wettbewerbe, letzte 6 Ligaspiele, Direktvergleiche, Trends). Keine Quoten.
- `fs_ergebnis.py <match_id> ...` – Endergebnisse für die Auswertung.

Odd Alerts:
- `oa.sh <pfad> [k=v ...]` – ein API-Abruf, z. B. `werkzeuge/oa.sh fixtures/upcoming competitions=477`.
- `oa_spiel.py <competition_id> "<Heim-Teilname>" "<Auswärts-Teilname>"` – Saisonwerte gesamt und
  Heim/Auswärts, Odd-Alerts-Modell (nur zum Vergleich; nur für Spiele der nächsten ~5 Tage).
- `ergebnisse.py <comp_ids> "<Heim>" "<Auswärts>"` – letzte 10 Pflichtspiele inkl. Pokal,
  Heim-/Auswärtsspiele, Direktvergleiche (exakte Teamnamen wie in der API).

Saison-IDs FootyStats: `FOOTYSTATS-API.md`. Wettbewerbs-IDs Odd Alerts (Auswahl): Bundesliga 477,
2. Bundesliga 471, DFB-Pokal 417, Premier League 423, Championship 418, FA Cup 327, Carabao Cup 268,
La Liga 419, Serie A 499, Coppa Italia 531, Serie B 545, Ligue 1 200, Ligue 2 256, Eredivisie 437,
Pro League (BEL) 198, Süper Lig 414, Allsvenskan 255, Admiral Bundesliga (AUT) 411, Champions League 51.
