# Regeln (Branch `forebet-system`)

Dieser Branch enthält **nur den Forebet-Check (System B)** des Nutzers, eingerichtet am
07.11.2026 (abgezweigt von `tipps-system-a-b`). Regeln: `FOREBET-CHECK.md`. Das
OddAlerts-System v1.3-OA, der Spielcheck (System A) und alle anderen Systeme gelten hier nicht
und werden nicht vermischt; sie liegen auf ihren eigenen Branches. Änderungen nur auf
ausdrücklichen Wunsch des Nutzers.

## Arbeitsweise

- Der Nutzer fügt eine Forebet-Vorschau ein (Text oder Screenshot) → Forebet-Check nach
  `FOREBET-CHECK.md`. Forebet selbst ist für Claude nicht erreichbar.
- Keine Spielcheck-Zählung („x von 10“), keine Schwellen.
- Alle Tipps eines Tages in `tipps/forebet/JJJJ-MM-TT.md`, nach Abpfiff dort auswerten;
  committen und pushen.

## Technik

Der Odd-Alerts-Schlüssel liegt in der Umgebung als `ODDALERTS_KEY` und wird als
Query-Parameter `api_token` an `https://data.oddalerts.com/api/` gesendet. Fehlt er: dem
Nutzer sagen, dass er ihn in den Umgebungseinstellungen hinterlegen soll. Den Schlüssel
**nie** im Chat erfragen, ausgeben, loggen, in eine Datei schreiben oder committen; in
gespeicherten URLs `[REDACTED]` (auch in `next_page_url` der API-Antworten).

Endpunkte und Felder: `ODDALERTS-API.md`. Hilfsskripte: `werkzeuge/` (siehe README dort).
Bei HTTP 429 oder ähnlichem warten.

Antworten auf Deutsch.
