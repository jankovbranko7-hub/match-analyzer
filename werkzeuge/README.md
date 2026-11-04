# Werkzeuge für System v1.3-OA

Zwei Hilfsprogramme, **nicht Teil des Systems**. Sie ändern keine Regel und treffen keine
Auswahl. Die Entscheidung trifft allein `OddAlerts-System-v1.3-OA.txt`.

Voraussetzung: Schlüssel als `ODDALERTS_KEY` in der Umgebung. Nur Python 3, keine
Zusatzpakete. Der Schlüssel wird nirgends gespeichert; in Dateien steht `[REDACTED]`.

## 1. Spiele-Scanner – `scanner.py`

Listet **alle** kommenden Spiele **ohne Filter und ohne Grenzen**: Odd-Alerts-Wahrscheinlichkeiten
(Heim/Remis/Auswärts, BTTS, Over/Under 2,5) und Bet365-Quoten (Eröffnung und aktuell),
dazu im JSON auch Pinnacle.

```
python3 werkzeuge/scanner.py                  # nächste 24 Stunden
python3 werkzeuge/scanner.py --stunden 48
python3 werkzeuge/scanner.py --datum 2026-11-07
```

Ergebnis in `scans/`: `scan_<Zeit>.md` (Liste mit Nummern) und `scan_<Zeit>.json`
(Snapshot mit Abrufzeit für spätere Prüfung). „–“ heißt fehlt; Pinnacle bietet kein BTTS an,
Bet365 nicht bei jedem Spiel.

Die Odd-Alerts-Prozente sind nur Kontext – kein Modell im Sinne von Abschnitt 5.

## 2. Erfolgs-Tracker – `tracker.py`

| Befehl | Was passiert |
|---|---|
| `erfassen --match-id ID --markt heim\|auswaerts\|btts\|over25\|under25\|keine --quelle system\|oddalerts\|andere` | Speichert den Tipp **vor dem Anpfiff** mit Zeitstempel, Quoten und Odd-Alerts-Prozenten in `tracker/vorab.jsonl`. Nach dem Anpfiff wird abgelehnt. Optional: `--warnung "Text"` (⚠️), `--quote 1.85` (tatsächlich erhaltene Quote), `--analyse-id`, `--notiz`. |
| `abrechnen` | Holt Ergebnisse (reguläre Spielzeit inkl. Nachspielzeit) und Eröffnungs-/Schlussquoten, getrennt in `tracker/ergebnisse.jsonl`. Verlängerung zählt nicht; wenn nicht sicher bestimmbar: „manuell“. Verschobene/abgebrochene Spiele: „annulliert“. |
| `bericht` | Je Quelle, Markt und ⚠️: Tipps, „keine“, Trefferquote ± Unsicherheit, Gewinn bei 1 Einheit, ROI, CLV gegenüber Pinnacle-Schlussquote, Brier-Score der Odd-Alerts-Prozente. |
| `kalibrierung` | Prüft über alle gescannten Spiele, ob die Odd-Alerts-Prozente stimmen (z. B. „sagt 60 %, trifft 58 %“). |

Regeln nach Abschnitt 9/10: Vorabeinträge werden nie geändert, nur angehängt. Ergebnisse
stehen getrennt. „keine“ zählt weder als Treffer noch als Verlust. Ohne eigene Quote wird
mit Bet365 zum Erfassungszeitpunkt gerechnet und das als hypothetisch ausgewiesen.

## Ablauf

1. `scanner.py` → Kandidatenliste in `scans/`.
2. Nutzer wählt Spiele (Batch) → Analyse nach System v1.3-OA → Vorabeintrag in `protokoll/`.
3. Für jedes analysierte Spiel `tracker.py erfassen … --quelle system` (auch bei „keine“).
4. Nach den Spielen `tracker.py abrechnen`, dann `tracker.py bericht`.
