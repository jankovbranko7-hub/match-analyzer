# Werkzeuge (FootyStats, ohne Schlüssel)

Alle Skripte lesen den Schlüssel nur aus `APIKEY` und schwärzen ihn als `[REDACTED]`.

- `fs.sh <pfad> [k=v ...]` – ein API-Abruf, z. B. `werkzeuge/fs.sh match match_id=8572478`.
  Letzte Zeile: `__HTTP <code>`.
- `fs_spiel.py <season_id> "<Heim-Teilname>" "<Auswärts-Teilname>"` – alle FootyStats-Daten zu
  einem Spiel für den Forebet-Check v2 (Vorab-xG, Saison, Heim/Auswärts, letzte 6 aller
  Wettbewerbe, letzte 6 Ligaspiele, Direktvergleiche, Trends). Keine Quoten.
- `fs_ergebnis.py <match_id> ...` – Endergebnisse für die Auswertung.

Saison-IDs: `FOOTYSTATS-API.md`.
