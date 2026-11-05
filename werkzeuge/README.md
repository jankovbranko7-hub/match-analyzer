# Werkzeuge für OA-Prognose-System v2.1

Voraussetzung: `ODDALERTS_KEY` in der Umgebung. Nur Python 3 (Backtest-Auswertung ohne Zusatzpakete).

| Werkzeug | Zweck |
|---|---|
| `oap21_auswahl.py [--stunden 24] [--erfassen]` | **v2.1 (aktiv):** alle Ligen (M1) und Pokale/Europapokal (M3) → `scans/oap21_<Zeit>.md`; mit `--erfassen` in `tracker/OAP-2.1/`. |
| `oap_global.py`, `oap21_backtest.py` | gemeinsames Pokalmodell (M2 verworfen, M3 aktiv), Entwicklung/Test v2.1. |
| `oap2_auswahl.py [--stunden 24] [--erfassen]` | v2.0 (nur Aufzeichnung): Ligadaten aktualisieren, eigenes Modell rechnen, Regel mit Odd-Alerts-Leitschiene → `scans/oap2_<Zeit>.md`; mit `--erfassen` in `tracker/OAP-2.0/`. |
| `oap_daten.py`, `oap_modell.py`, `oap2_backtest.py` | Datenspeicher (`.cache/oap/`), Modell OAP-M1, Entwicklung/Test v2.0. |
| `oap_auswahl.py [--stunden 24] [--erfassen]` | v1.0 (nur Aufzeichnung): Tipps nach Regelwerk Abschnitt 3 → `scans/oap_<Zeit>.md/.json`; mit `--erfassen` vor Anpfiff in `tracker/vorab.jsonl` (kein Doppel-Eintrag pro Spiel). |
| `tracker.py abrechnen` / `bericht` / `kalibrierung` | Ergebnisse getrennt abrufen, Auswertung (Treffer, ROI, CLV gegen Pinnacle-Schluss), Kalibrierung über Scans. |
| `scanner.py` | Übersicht aller Spiele mit Odd-Alerts-Prozenten und Quoten, ohne Filter. |
| `oap_backtest_holen.py`, `oap_backtest_auswerten.py` | Entwicklungsgrundlage (Protokoll: `protokoll/OAP-1.0_entwicklung.md`). |
| `oa_api.py` | gemeinsame API-Hilfen (Schlüssel nie gespeichert). |

Ablauf: täglich `oap21_auswahl.py --erfassen` → commit/push → nach den Spielen `tracker.py abrechnen` und `bericht`.
