# Regeln (Branch `forebet-system`)

Dieser Branch enthält **nur den Forebet-Check (System B)** des Nutzers, eingerichtet am
07.11.2026 (abgezweigt von `tipps-system-a-b`). Regeln: `FOREBET-CHECK.md`. Das
OddAlerts-System v1.3-OA, der Spielcheck (System A) und alle anderen Systeme gelten hier nicht
und werden nicht vermischt; sie liegen auf ihren eigenen Branches. Änderungen nur auf
ausdrücklichen Wunsch des Nutzers.

## Arbeitsweise

- Der Nutzer fügt je Spiel die Forebet-Vorschau ein (Text oder Screenshot) → Forebet-Check
  Version 2.3 nach `FOREBET-CHECK.md`: Fakten aus der Forebet-Vorschau + FootyStats nach fester
  Rangfolge gewichten (Spielinfos > aktuelle Form > Saison > Direktvergleiche), daraus ein eigener
  Tipp – nur Sieg, beide treffen Ja/Nein, über/unter 2,5. Die Forebet-Prognose fließt nicht ein,
  sie wird nur zum Vergleich genannt. Forebet selbst ist für Claude nicht erreichbar.
- **Keine Quoten** (seit 07.11.2026). Keine Spielcheck-Zählung („x von 10“), keine Schwellen.
- Alle Tipps eines Tages in `tipps/forebet/JJJJ-MM-TT.md`, nach Abpfiff dort auswerten;
  committen und pushen.

## Technik

Datenquelle ist **FootyStats** (`https://api.football-data-api.com/`), Odd Alerts wird nicht mehr
verwendet. Der Schlüssel liegt in der Umgebung als `APIKEY` und wird als Query-Parameter `key`
gesendet. Fehlt er: dem Nutzer sagen, dass er ihn in den Umgebungseinstellungen hinterlegen soll.
Den Schlüssel **nie** im Chat erfragen, ausgeben, loggen, in eine Datei schreiben oder committen;
in gespeicherten URLs `[REDACTED]`. Limit laut API: 1800 Abrufe pro Stunde.

Endpunkte, Felder, Saison-IDs: `FOOTYSTATS-API.md`. Hilfsskripte: `werkzeuge/` (README dort).
Bei HTTP 429 oder ähnlichem warten.

Antworten auf Deutsch.
