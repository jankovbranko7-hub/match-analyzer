# OA-Prognose-System v2.0 – Entwicklung und Test

Erstellt 05.11.2026. Werkzeuge: `werkzeuge/oap_daten.py` (Datenspeicher, 627 Ligen),
`werkzeuge/oap_modell.py` (Modell OAP-M1), `werkzeuge/oap2_backtest.py` (Entwicklung/Test).
Daten: Odd Alerts (`fixtures/competition/{id}?include=stats`, `fixtures/between?include=probability`,
`odds/history/multiple`), `api_token=[REDACTED]`.

Grundgesamtheit: 11.110 Ligaspiele mit Odd-Alerts-Prognose, Ergebnis nach regulärer Spielzeit
und Bet365-Quote (06.10.–03.11.2026); Entwicklung 06.–23.10. (6.011 Spiele), unberührter Test
24.10.–03.11. Für jedes Spiel nur Ligaspiele im Modell, die vor 00:00 UTC des Spieltags
beendet waren.

## Schritt 1 – Modellwahl (nur Entwicklung, Log-Loss, 5.547 gemeinsame Spiele)

| xG-Anteil | Halbwertszeit | 1X2 | Over/Under | BTTS | Summe |
|---|---|---|---|---|---|
| 0 | 120 | 0,9935 | 0,6685 | 0,6914 | 2,3534 |
| 0 | 365 | 0,9948 | 0,6706 | 0,6911 | 2,3565 |
| 0,5 | 120 | 0,9926 | 0,6672 | 0,6907 | 2,3505 |
| 0,5 | 365 | 0,9940 | 0,6694 | 0,6905 | 2,3539 |
| **1,0** | **120** | **0,9928** | **0,6667** | **0,6906** | **2,3501** |
| 1,0 | 365 | 0,9942 | 0,6689 | 0,6905 | 2,3536 |
| Odd Alerts | – | 0,9991 | 0,6623 | 0,6816 | – |

Gewählt: xG-Anteil 1,0, Halbwertszeit 120 Tage (α = 2, mindestens 6 Spiele je Team).

Test (4.935 Spiele): eigenes Modell 1X2 0,9914 / OU 0,6778 / BTTS 0,6914 – Odd Alerts
1,0007 / 0,6654 / 0,6835. Beim Spielausgang ist das eigene Modell in beiden Zeiträumen
genauer, bei Toren und BTTS nicht.

## Schritt 2 – Regelwahl (16 Regeln, nur Entwicklung, mindestens 150 Tipps)

Raster: Vorteil ≥ 5/10 %, p_M ≥ 40/50 %, Abweichung zu Odd Alerts ≤ 5/10 Punkte,
Odd-Alerts-Vorteil ≥ 0 ja/nein, Quote ≤ 3,00, ein Tipp pro Spiel. Auswahlkriterium vorab:
höchster ROI zur Eröffnungsquote. Gewählt: **Vorteil ≥ 10 %, p_M ≥ 40 %, Abweichung ≤ 5,
Odd-Alerts-Vorteil ≥ 0** (Entwicklung: 499 Tipps, 54,1 % Treffer, ROI +13,0 % Eröffnung,
+8,3 % Schluss, z = 2,7). Alle 16 Regeln waren in der Entwicklung zur Eröffnungsquote ≥ 0 %.

## Schritt 3 – einmaliger Test 24.10.–03.11.

| | Tipps | Treffer | ROI Eröffnung | ROI Schluss | CLV vs. Pinnacle |
|---|---|---|---|---|---|
| Gewählte Regel | 450 | 46,9 % | −1,0 % (z = −0,2) | −4,7 % | +3,8 % |

Je Markt (Eröffnung): Heim −1,0 % (131), Auswärts +21,5 % (38), BTTS Ja +16,8 % (14),
BTTS Nein −38,2 % (16), Over 2,5 −16,3 % (82), Under 2,5 +2,4 % (168), Remis (1).
Die Regel wird wegen dieser Testzahlen nicht verändert.

## Bewertung

Der Vorteil aus der Entwicklung hat sich im Test nicht bestätigt. Belegt ist nur, dass das
eigene Modell den Spielausgang etwas genauer schätzt als Odd Alerts. Ob daraus Gewinn
entsteht, zeigt nur der Testbetrieb mit vor Anpfiff gespeicherten Tipps (Regelwerk
Abschnitt 8). Mögliche spätere Version (eigener Test nötig): nur Siegmärkte, weil das
Modell dort genauer ist – das ist eine Hypothese, keine belegte Verbesserung.
