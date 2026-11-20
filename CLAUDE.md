# Regeln (Branch `forebet-system`)

Dieser Branch enthält **nur den Forebet-Check (System B)** des Nutzers, eingerichtet am
07.11.2026 (abgezweigt von `tipps-system-a-b`). Regeln: `FOREBET-CHECK.md`. Das
OddAlerts-System v1.3-OA, der Spielcheck (System A) und alle anderen Systeme gelten hier nicht
und werden nicht vermischt; sie liegen auf ihren eigenen Branches. Änderungen nur auf
ausdrücklichen Wunsch des Nutzers.

## Arbeitsweise

- Der Nutzer fügt je Spiel die **Sports-Mole-Vorschau** ein (PDF, Text oder Screenshot) →
  Forebet-Check **Version 3.0 – Spielbild** nach `FOREBET-CHECK.md` (seit 20.11.2026 Hauptanalyse):
  Fakten aus der Vorschau + FootyStats nach fester Rangfolge gewichten (Spielinfos > aktuelle Form >
  Saison > Direktvergleiche), daraus ein eigenes Spielbild; getippt wird nur ein Markt, der danach
  klar ist – nur Sieg, beide treffen Ja/Nein, über/unter 2,5. Kein klarer Markt → kein Tipp.
  Der Nutzer schickt nur Spiele mit Sports-Mole-Vorschau. **Forebet wird überhaupt nicht mehr
  verwendet** (Wunsch des Nutzers vom 20.11.2026). „We say“ nur zum Vergleich. Version 2.10 liegt in `archiv/FOREBET-CHECK-2.10.md`.
- **Keine Quoten** (seit 07.11.2026). Keine Spielcheck-Zählung („x von 10“), keine Schwellen.
- Alle Tipps eines Tages in `tipps/forebet/JJJJ-MM-TT.md`, nach Abpfiff dort auswerten;
  committen und pushen.
- **Branch `forebet-system` immer automatisch mitziehen** (Wunsch des Nutzers vom 09.11.2026):
  Jede Regeländerung und jede Tagesliste nach dem Push auf den Arbeitsbranch auch nach
  `forebet-system` pushen (nur als Vorspulen, nie überschreiben).

## Technik

Einzige Datenquelle (seit 14.11.2026, Version 2.8), ohne Quoten:
- **FootyStats** (`https://api.football-data-api.com/`): Schlüssel in der Umgebung als `APIKEY`,
  Query-Parameter `key`. Endpunkte, Felder, Saison-IDs: `FOOTYSTATS-API.md`. Limit 1800/Stunde.
- Odd Alerts wird überhaupt nicht mehr verwendet, weder API noch Vorschau (Wunsch des Nutzers
  vom 14.11.2026).

Fehlt ein Schlüssel: dem Nutzer sagen, dass er ihn in den Umgebungseinstellungen hinterlegen
soll. Schlüssel **nie** im Chat erfragen, ausgeben, loggen, in eine Datei schreiben oder
committen; in gespeicherten URLs `[REDACTED]` (auch in `next_page_url`).
Hilfsskripte: `werkzeuge/` (README dort). Bei HTTP 429 oder ähnlichem warten.

Antworten auf Deutsch.
