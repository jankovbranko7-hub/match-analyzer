# Regeln (Branch `system-v1.3`)

**Das System ist `FootyStats-System-v1.4.txt` – genau so, wie es dort steht, und nichts
sonst.** Dazu gehören `AKTIVES-SYSTEM.txt` und `AKTIVES-SYSTEM.json` (aktive Fassung
v1.4-2026-11-05). v1.3 wurde vom Nutzer am 01.11.2026 aus `FootyStats-System-v1.3.zip`
auf diesem Branch eingesetzt; auf seinen ausdrücklichen Wunsch vom 05.11.2026 entstand
daraus v1.4 (xG-Variante, Marktgegenprobe). v1.3 liegt unverändert in `archiv/`; Analysen
bis 04.11.2026 bleiben v1.3. Das System auf `main` (`SYSTEM.md`) gilt hier nicht
und wird nicht vermischt; Änderungen an einem der beiden Systeme nur auf ausdrücklichen
Wunsch des Nutzers.

Der API-Schlüssel steht nicht im Regelwerk, sondern in der Umgebung (siehe Technik).

## Arbeitsweise (nicht Teil des Systems)

- **Das System strikt befolgen** (Nutzeranweisung vom 02.11.2026): genau nach Wortlaut, keine
  eigenen Maßstäbe, Schwellen, Hürden oder Ersatzregeln einführen. Lässt das System eine Frage
  offen, sie dem Nutzer vorlegen statt selbst zu entscheiden. Scheitert ein Pflichtcheck
  (Abschnitt 11): beheben oder auf den Tipp verzichten – nie nur vermerken und trotzdem tippen.
  Einschränkungen von Anfang an offen nennen.

- Spiele kommen meist als Batches zu je 5, nummeriert („Batch X · Nr. Y“). Jede Nummer
  genau ihr Spiel, nichts vertauschen.
- Vorabeinträge nach Abschnitt 9 des Systems kommen vor dem Anpfiff als Datei nach
  `protokoll/` und werden committet und gepusht; Ergebnisprüfungen getrennt davon
  (Abschnitt 10).

## Technik

Der FootyStats-Schlüssel liegt in der Umgebung als `APIKEY`; beim Aufruf als
`FOOTYSTATS_KEY="$APIKEY"` mitgeben. Fehlt er: dem Nutzer sagen, dass er ihn in den
Umgebungseinstellungen hinterlegen soll. Den Schlüssel **nie** im Chat erfragen, ausgeben,
loggen, in eine Datei schreiben oder committen; in gespeicherten URLs `[REDACTED]`.

Ein `HTTP 417` ist das Stundenlimit der API – dann warten. Ausnahme: Meldet die Antwort
`request_limit: null`, ist die Liga nicht im API-Abo (andere Abrufe laufen weiter).

Antworten auf Deutsch.
