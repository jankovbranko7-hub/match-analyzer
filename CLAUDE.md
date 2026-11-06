# Regeln (Branch `system-v1.3-oa`)

**Das System ist `OddAlerts-System-v1.3-OA.txt` – genau so, wie es dort steht, und nichts
sonst.** Dazu gehören `AKTIVES-SYSTEM.txt` und `AKTIVES-SYSTEM.json` (aktive Fassung
v1.3-OA-2026-11-05, Modellversion 2 mit Zeitgewichtung; Vorgänger in `archiv/`). Am 02.11.2026 auf Wunsch des Nutzers aus dem FootyStats-System v1.3
(Branch `system-v1.3`) übertragen: gleiche Regeln, einzige Datenquelle Odd Alerts. Das
FootyStats-System auf `system-v1.3` und das System auf `main` gelten hier nicht und werden
nicht vermischt; Änderungen an einem der Systeme nur auf ausdrücklichen Wunsch des Nutzers.

## Arbeitsweise (nicht Teil des Systems)

- Spiele kommen meist als Batches zu je 5, nummeriert („Batch X · Nr. Y“). Jede Nummer
  genau ihr Spiel, nichts vertauschen.
- Vorabeinträge nach Abschnitt 9 des Systems kommen vor dem Anpfiff als Datei nach
  `protokoll/` und werden committet und gepusht; Ergebnisprüfungen getrennt davon
  (Abschnitt 10).
- Schreibt der Nutzer „Spielcheck: …“, gilt das eigene Prüfverfahren in `SPIELCHECK.md`
  (nicht Teil des Systems; keine Vorabeinträge nötig).

## Technik

Der Odd-Alerts-Schlüssel liegt in der Umgebung als `ODDALERTS_KEY` und wird als
Query-Parameter `api_token` an `https://data.oddalerts.com/api/` gesendet. Fehlt er: dem
Nutzer sagen, dass er ihn in den Umgebungseinstellungen hinterlegen soll. Den Schlüssel
**nie** im Chat erfragen, ausgeben, loggen, in eine Datei schreiben oder committen; in
gespeicherten URLs `[REDACTED]` (auch in `next_page_url` der API-Antworten).

Endpunkte und Felder: `ODDALERTS-API.md`. Ein Stundenlimit der API ist nicht geprüft;
bei HTTP 429 oder ähnlichem warten.

Antworten auf Deutsch.
