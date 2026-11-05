# OA-Prognose-System v1.0 – Entwicklung und Test

Erstellt 05.11.2026. Daten: Odd Alerts API, `fixtures/between?include=probability,timings`
(06.10.–03.11.2026) und `odds/history/multiple` (Bet365, Pinnacle; Märkte 6, 9, 13),
`api_token=[REDACTED]`. 12.675 Spiele mit Odd-Alerts-Prognose, Ergebnis nach regulärer
Spielzeit und Bet365-Quote; 77.041 Markt-Zeilen. Skripte: `werkzeuge/oap_backtest_holen.py`,
`werkzeuge/oap_backtest_auswerten.py`.

Aufteilung (vorab festgelegt): Entwicklung 06.–23.10. (43.747 Zeilen), unberührter Test
24.10.–03.11. (33.294 Zeilen).

## Kalibrierung der Odd-Alerts-Wahrscheinlichkeiten (Entwicklung)

| Markt | n | Brier | Gruppen (Prognose → beobachtet) |
|---|---|---|---|
| Heimsieg | 6.895 | 0,223 | 20–40: 32→33 · 40–60: 49→49 · 60–80: 67→68 |
| Remis | 6.895 | 0,182 | 0–20: 16→17 · 20–40: 25→26 |
| Auswärtssieg | 6.895 | 0,192 | 20–40: 30→29 · 40–60: 47→47 · 60–80: 67→68 |
| BTTS Ja | 4.758 | 0,245 | 40–60: 52→54 · 60–80: 64→62 |
| BTTS Nein | 4.758 | 0,245 | 40–60: 48→46 · 60–80: 63→58 |
| Over 2,5 | 6.773 | 0,236 | 40–60: 51→52 · 60–80: 67→66 |
| Under 2,5 | 6.773 | 0,236 | 40–60: 49→47 · 60–80: 65→64 |

Ergebnis: gut kalibriert; BTTS Nein im oberen Bereich überschätzt.

## Allen Prognosen folgen (Entwicklung, Bet365-Eröffnungsquote)

Heimsieg −9,2 % · Remis −10,1 % · Auswärtssieg −17,4 % · BTTS Ja −1,0 % · BTTS Nein −12,1 % ·
Over 2,5 −3,4 % · Under 2,5 −9,3 %. Blindes Folgen verliert in jedem Markt.

## Regelsuche (Entwicklung)

Geprüft: 115 Regeln (Marktgruppen × Vorteil ≥ 0/5/10/20 % × p ≥ 0/40/50/60 % × Quote ≤ 3/5,
mind. 150 Tipps); 61 davon positiv zur Eröffnungsquote. Vorab gewählt (größte Tippzahl bei
stabilem Ergebnis, einfache Regel): **alle Märkte, p ≥ 60 %, Vorteil ≥ 10 %, Quote ≤ 3,00,
ein Tipp pro Spiel.**

## Ergebnis der gewählten Regel

| Zeitraum | Tipps | Treffer | ROI Eröffnungsquote | ROI Schlussquote | CLV vs. Pinnacle |
|---|---|---|---|---|---|
| Entwicklung 06.–23.10. | 655 | 62,3 % | +9,5 % (z = 2,8) | +3,5 % | +7,3 % |
| **Test 24.10.–03.11.** | **539** | **57,7 %** | **+1,4 % (z = 0,4)** | **−2,2 %** | +8,1 % |

Im Test je Markt (Eröffnung): Heim +6,6 % (171), Auswärts −13,2 % (84), BTTS Ja +12,8 % (28),
Over 2,5 −2,7 % (198), Under 2,5 +14,1 % (57). Keine Änderung der Regel aus diesen Testzahlen
(sonst wäre der Test nicht mehr unberührt).

## Bewertung

Der Vorteil aus der Entwicklung hat sich im Test nicht bestätigt (ungefähr ausgeglichen).
Der hohe CLV bei kaum positivem ROI ist auffällig und kann bedeuten, dass die historischen
Odd-Alerts-Werte nicht genau dem Stand vor dem Spiel entsprechen. Deshalb: Testbetrieb mit
vor Anpfiff gespeicherten Tipps, Bewertung nach mindestens 300 Tipps (Regelwerk Abschnitt 7).
