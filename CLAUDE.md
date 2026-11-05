# Regeln (Branch `system-oa-prognose`)

**Das System ist `OA-Prognose-System-v2.1.txt` (Kennung OAP-2.1) – genau so, wie es dort
steht, und nichts sonst.** (v1.0 und v2.0 nur noch Aufzeichnung.) Dazu gehören `AKTIVES-SYSTEM.txt` und `AKTIVES-SYSTEM.json`.
Auf ausdrücklichen Wunsch des Nutzers am 05.11.2026 als eigenes System für das
Prediction-Modul von Odd Alerts entworfen. FootyStats-System v1.3 (`system-v1.3`),
OddAlerts-System v1.3-OA (`system-v1.3-oa`, `system-v1.3-oa-werkzeuge`) und `main`
gelten hier nicht und werden nicht vermischt. Änderungen nur auf ausdrücklichen Wunsch
des Nutzers und nur als neue Version.

## Arbeitsweise (nicht Teil des Systems)

- Auswahl: `python3 werkzeuge/oap21_auswahl.py` (Liste) bzw. mit `--erfassen` (Tipps vor
  Anpfiff in `tracker/OAP-2.1/vorab.jsonl`), danach committen und pushen. Tippliste immer
  mit Datum/Uhrzeit (deutsche Zeit), Land und Wettbewerb ausgeben.
- Nach den Spielen: `python3 werkzeuge/tracker.py abrechnen` und `... bericht` (ältere
  Versionen mit `TRACKER_SYSTEM=OAP-1.0` bzw. `OAP-2.0`).
- Status Testbetrieb: dem Nutzer nicht zu echten Einsätzen raten, solange Abschnitt 8
  nicht erfüllt ist.

## Technik

Odd-Alerts-Schlüssel in der Umgebung als `ODDALERTS_KEY`, als `api_token` an
`https://data.oddalerts.com/api/`. Fehlt er: dem Nutzer sagen, dass er ihn in den
Umgebungseinstellungen hinterlegen soll. Den Schlüssel **nie** im Chat erfragen,
ausgeben, loggen, in eine Datei schreiben oder committen; in gespeicherten URLs
`[REDACTED]`. Endpunkte: `ODDALERTS-API.md`.

Antworten auf Deutsch, einfach und kurz erklärt.
