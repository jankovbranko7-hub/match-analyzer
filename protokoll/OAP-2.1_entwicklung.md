# OA-Prognose-System v2.1 – Pokal- und Europapokalspiele: Entwicklung und Test

Erstellt 05.11.2026. Werkzeuge: `werkzeuge/oap_global.py` (Modelle M2, M3),
`werkzeuge/oap21_backtest.py`. Daten: Odd Alerts (149 Pokalwettbewerbe zusätzlich im
Datenspeicher, Wettbewerbsarten aus `competitions`), `api_token=[REDACTED]`.

Grundgesamtheit: 1.525 Nicht-Ligaspiele (keine Freundschaftsspiele) mit Odd-Alerts-Prognose,
Ergebnis nach regulärer Spielzeit und Bet365-Quote, 06.10.–03.11.2026; Entwicklung 06.–23.10.,
unberührter Test 24.10.–03.11.; je Spieltag nur vorher beendete Spiele im Modell.

## Erster Versuch – M2 (ein Modell, alle Teams zum Gesamtmittel gezogen)

Log-Loss Spielausgang Entwicklung 1,013 / Test 1,029 gegen Odd Alerts 0,985 / 0,986;
Regel v2.0: 225 Tipps −9,0 % (Eröffnung) / −15,0 % (Schluss). Verworfen.

## Modellwahl (nur Entwicklung, 744 gemeinsame Spiele, Log-Loss)

| Variante | 1X2 | Over/Under | BTTS | Summe |
|---|---|---|---|---|
| A M2 (bisher) | 1,0165 | 0,6881 | 0,7131 | 2,4177 |
| B M3 Tore, Teamstrafe 5 | 0,9552 | 0,6902 | 0,7120 | 2,3574 |
| **C M3 xG, Teamstrafe 5** | **0,9540** | **0,6879** | **0,7104** | **2,3523** |
| D M3 Tore, Teamstrafe 20 | 0,9697 | 0,6849 | 0,7059 | 2,3605 |
| Odd Alerts | 0,9877 | 0,6677 | 0,6901 | – |

Gewählt: C (M3: Ligastärke + Teamabweichung, xG, Ligastrafe 0,2, Teamstrafe 5, 400 Tage).

## Einmaliger Test (Regel unverändert aus v2.0)

Log-Loss Test (636 Spiele): M3 1X2 0,9666 / OU 0,6765 / BTTS 0,6964 – Odd Alerts 0,9872 /
0,6672 / 0,6926.

| | Tipps | Treffer | ROI Eröffnung | ROI Schluss | CLV vs. Pinnacle |
|---|---|---|---|---|---|
| Entwicklung | 122 | 50,8 % | +6,4 % | −0,3 % | +7,3 % |
| **Test** | **80** | **57,5 %** | **+20,8 % (z = 1,7)** | **+11,6 %** | +8,6 % |
| Gesamt | 202 | 53,5 % | +12,1 % | +4,4 % | +7,8 % |

## Bewertung

Das Pokalmodell M3 schätzt den Spielausgang in Entwicklung und Test genauer als Odd Alerts.
Die Regel war im Test positiv, die Stichprobe (80 Tipps) ist aber zu klein für einen Beleg.
Over/Under und BTTS schätzt Odd Alerts weiterhin genauer. Bewertung im Testbetrieb nach
Regelwerk Abschnitt 8.
