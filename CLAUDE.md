# Regeln (Branch `system-oa-prognose`)

**Das System ist `OA-Prognose-System-v1.0.txt` (Kennung OAP-1.0) – genau so, wie es dort
steht, und nichts sonst.** Dazu gehören `AKTIVES-SYSTEM.txt` und `AKTIVES-SYSTEM.json`.
Auf ausdrücklichen Wunsch des Nutzers am 05.11.2026 als eigenes System für das
Prediction-Modul von Odd Alerts entworfen. FootyStats-System v1.3 (`system-v1.3`),
OddAlerts-System v1.3-OA (`system-v1.3-oa`, `system-v1.3-oa-werkzeuge`) und `main`
gelten hier nicht und werden nicht vermischt. Änderungen nur auf ausdrücklichen Wunsch
des Nutzers und nur als neue Version.

## Arbeitsweise (nicht Teil des Systems)

- Auswahl: `python3 werkzeuge/oap_auswahl.py` (Liste) bzw. mit `--erfassen` (Tipps vor
  Anpfiff in `tracker/vorab.jsonl`), danach committen und pushen.
- Nach den Spielen: `python3 werkzeuge/tracker.py abrechnen` und `... bericht`.
- Status Testbetrieb: dem Nutzer nicht zu echten Einsätzen raten, solange Abschnitt 7
  nicht erfüllt ist.

## Technik

Odd-Alerts-Schlüssel in der Umgebung als `ODDALERTS_KEY`, als `api_token` an
`https://data.oddalerts.com/api/`. Fehlt er: dem Nutzer sagen, dass er ihn in den
Umgebungseinstellungen hinterlegen soll. Den Schlüssel **nie** im Chat erfragen,
ausgeben, loggen, in eine Datei schreiben oder committen; in gespeicherten URLs
`[REDACTED]`. Endpunkte: `ODDALERTS-API.md`.

Antworten auf Deutsch, einfach und kurz erklärt.
