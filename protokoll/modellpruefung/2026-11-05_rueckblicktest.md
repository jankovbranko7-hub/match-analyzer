# Rückblick-Test Modellversion 2 (Zeitgewichtung), 05.11.2026

Zweck: zeitliche Prüfung der neuen Modellversion nach Abschnitt 5.3/5.5 vor der Übernahme in Fassung v1.3-OA-2026-11-05.

## Verfahren

- Daten: abgeschlossene Spiele (Status FT, ohne Freundschaftsspiele) aus Odd Alerts `fixtures/between`, abgerufen am 02. und 03.11.2026; 28 Wettbewerbe mit mindestens 600 Spielen.
- Testzeitraum je Wettbewerb: die letzten 365 Tage vor dem jüngsten Spiel; Parameterwahl (alpha, xi) ausschließlich auf den 365 Tagen davor.
- Rollend vorwärts: Neuschätzung alle 28 Tage nur mit Spielen vor dem Blockbeginn (Trainingsfenster 1.100 Tage); Teams ohne Parameter werden nicht bewertet.
- Variante A: gleichgewichtet (xi = 0), alpha aus {0.1, 1, 10, 100}. Variante B: zusätzlich xi aus {0, 0.002, 0.004, 0.008} pro Tag. Auswahl nach mittlerem negativem Log-Score der Torpaare, bei Gleichstand größeres alpha.
- Grundrate: Anteil im Testjahr selbst (begünstigt die Grundrate leicht). Markt: Pinnacle-Schlussquote aus `odds/history`, Buchmacheraufschlag proportional entfernt, nur 6 Wettbewerbe (Premier League, Championship, La Liga, Serie A, Eerste Divisie, Ekstraklasa).

## Ergebnis

- Bewertete Testspiele: 9122 in 28 Wettbewerben.
- Mittlerer negativer Log-Score: A 2,8979, B 2,8916; Differenz 0,0063, Standardfehler 0,0015 (z = 4,1); B besser in 17 von 28 Wettbewerben.

| Markt | Brier Grundrate | Brier A | Brier B | Log-Loss A | Log-Loss B |
|---|---|---|---|---|---|
| Heimsieg | 0,2454 | 0,2275 | 0,2271 | 0,6459 | 0,6448 |
| Auswärtssieg | 0,2108 | 0,1954 | 0,1954 | 0,5752 | 0,5749 |
| BTTS Ja | 0,2460 | 0,2495 | 0,2488 | 0,6924 | 0,6908 |
| Over 2,5 | 0,2455 | 0,2462 | 0,2457 | 0,6857 | 0,6844 |

Vergleich mit dem Markt (6 Wettbewerbe, gleiche Spiele):

| Markt | n | Brier A | Brier B | Brier Pinnacle |
|---|---|---|---|---|
| Heimsieg | 2355 | 0,2287 | 0,2275 | 0,2192 |
| Auswärtssieg | 2355 | 0,2024 | 0,2019 | 0,1969 |
| BTTS Ja | 1247 | 0,2467 | 0,2458 | 0,2429 |
| Over 2,5 | 2341 | 0,2503 | 0,2486 | 0,2432 |

Trefferanteil, wenn die Modellwahrscheinlichkeit mindestens 60 % betrug (nur Beschreibung, keine Auswahlregel):

| Markt | A | B |
|---|---|---|
| Heimsieg | 701 von 995 (70,5 %) | 600 von 822 (73,0 %) |
| Auswärtssieg | 133 von 190 (70,0 %) | 103 von 147 (70,1 %) |
| BTTS Ja | 598 von 959 (62,4 %) | 644 von 1049 (61,4 %) |
| Over 2,5 | 823 von 1232 (66,8 %) | 809 von 1248 (64,8 %) |

## Je Wettbewerb

| Wettbewerb (ID) | Testspiele | A: alpha | B: alpha, xi | Log-Score A | Log-Score B |
|---|---|---|---|---|---|
| Argentina Liga Profesional de Fútbol (699) | 515 | 10 | 10, 0.002 | 2,6278 | 2,6203 |
| Bolivia Liga De Futbol Prof (758) | 244 | 10 | 10, 0.008 | 3,1285 | 3,1423 |
| Brazil Serie A (115) | 398 | 1 | 1, 0.002 | 2,8577 | 2,8604 |
| Brazil Serie B (206) | 382 | 100 | 10, 0.004 | 2,7254 | 2,7049 |
| Bulgaria First League (161) | 273 | 10 | 10, 0.0 | 2,7856 | 2,7856 |
| Chile Primera Division (306) | 236 | 10 | 10, 0.004 | 3,0229 | 3,0324 |
| Colombia Liga BetPlay (317) | 412 | 10 | 10, 0.002 | 2,7329 | 2,7219 |
| Denmark Superliga (413) | 188 | 10 | 10, 0.0 | 3,1005 | 3,1005 |
| Ecuador Liga Pro (40) | 322 | 10 | 10, 0.002 | 2,7637 | 2,7534 |
| England Championship (418) | 555 | 10 | 10, 0.002 | 2,9125 | 2,9007 |
| England Premier League (423) | 369 | 0.1 | 1, 0.002 | 2,9703 | 2,9385 |
| Europe Champions League (51) | 228 | 10 | 10, 0.0 | 3,2944 | 3,2944 |
| France Ligue 1 (200) | 288 | 10 | 10, 0.002 | 3,0357 | 3,0402 |
| France Ligue 2 (256) | 275 | 10 | 10, 0.002 | 2,8998 | 2,8968 |
| Greece Super League (406) | 235 | 10 | 10, 0.002 | 2,7873 | 2,8054 |
| Italy Serie A (499) | 385 | 10 | 10, 0.002 | 2,8654 | 2,8600 |
| Netherlands Eerste Divisie (175) | 374 | 10 | 10, 0.002 | 3,1871 | 3,1692 |
| Paraguay Division 1 (60) | 243 | 100 | 100, 0.0 | 2,7767 | 2,7767 |
| Poland 1. Liga (158) | 288 | 10 | 10, 0.004 | 2,9141 | 2,9086 |
| Poland Ekstraklasa (165) | 300 | 10 | 10, 0.002 | 2,9253 | 2,9156 |
| Portugal Liga Portugal (475) | 303 | 10 | 1, 0.002 | 2,8046 | 2,8138 |
| Portugal Liga Portugal 2 (397) | 301 | 10 | 10, 0.002 | 2,8666 | 2,8642 |
| Serbia Super Liga (155) | 283 | 10 | 10, 0.002 | 2,8974 | 2,8897 |
| Spain La Liga (419) | 373 | 10 | 10, 0.002 | 2,8604 | 2,8542 |
| Spain La Liga 2 (420) | 458 | 10 | 10, 0.004 | 2,8987 | 2,8880 |
| Sweden Allsvenskan (255) | 228 | 10 | 10, 0.002 | 3,0367 | 3,0250 |
| Turkey 1. Lig (410) | 372 | 1 | 1, 0.002 | 2,9896 | 2,9672 |
| Turkey Super Lig (414) | 294 | 10 | 10, 0.002 | 2,9195 | 2,9201 |

## Bewertung

- Übernommen: Variante B als Modellversion 2 (kleiner, statistisch abgesicherter Vorteil im Log-Score, kein Nachteil in den Märkten).
- Grenze: Bei BTTS und Over/Under ist auch Variante B nicht besser als die Grundrate; Tipps auf diese Märkte stützen sich weiterhin vor allem auf das sportliche Bild.
- Nicht übernommen: die Marktquote als Modellbaustein (im Test besser, wäre aber eine grundlegende Systemänderung und bedarf einer eigenen Entscheidung des Nutzers).
- Ein Rückblick-Test beweist keine künftige Trefferquote oder Profitabilität.
