# Modell-Prüfstand 03.11.2026 · Stichtag 2026-11-03 14:33 UTC

Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte). alpha aus {0.1, 1, 10, 100}: Training auf den ersten 50 % der chronologisch sortierten Spiele, Bewertung auf vier folgenden Blöcken bis 90 % (wachsendes Trainingsfenster), mittlerer negativer Poisson-Log-Score der Torpaare; bei Gleichstand größeres alpha. Unberührter Test: letzte 10 %, trainiert auf den ersten 90 % mit gewähltem alpha. Endmodell auf allen Vorabspielen. Grundrate = Trefferanteil im Trainingsteil. K.-o.-/Play-off-Runden (Spieltag 0) sind ausgeschlossen. Der Vergleich mit der Grundrate beschreibt Stärken und Schwächen, er ist keine Freigabehürde.

## UEFA Champions League (Saison-ID 17128)

Saisons [9543, 12321, 14924, 17128]; 438 Spiele (2023-09-19 bis 2026-10-21); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.3058; Heimvorteil 0.3041.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [3.49391, 175, True], '1': [3.32843, 175, True], '10': [3.25076, 175, True], '100': [3.33644, 175, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 44 | 0.2056 (±0.0151) | 0.2491 | 0.5996 | 0.6914 | [[0.2, 0.4, 12, 0.343, 0.167, 0.108], [0.4, 0.6, 24, 0.521, 0.708, 0.093], [0.6, 0.8, 8, 0.682, 0.875, 0.117]]
Auswärtssieg | 44 | 0.1729 (±0.0275) | 0.2022 | 0.5235 | 0.595 | [[0, 0.2, 11, 0.157, 0.091, 0.087], [0.2, 0.4, 26, 0.292, 0.269, 0.087], [0.4, 0.6, 7, 0.464, 0.571, 0.187]]
BTTS Ja | 44 | 0.2335 (±0.0209) | 0.2359 | 0.661 | 0.6648 | [[0.4, 0.6, 18, 0.567, 0.722, 0.106], [0.6, 0.8, 26, 0.667, 0.615, 0.095]]
Over 2,5 / Under 2,5 | 44 | 0.2114 (±0.0229) | 0.2008 | 0.6165 | 0.5928 | [[0.4, 0.6, 13, 0.562, 0.769, 0.117], [0.6, 0.8, 31, 0.681, 0.742, 0.079]]

## England Championship (Saison-ID 17184)

Saisons [9663, 12451, 14930, 17184]; 1812 Spiele (2023-08-04 bis 2026-10-31); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.1413; Heimvorteil 0.2340.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.8268, 724, True], '1': [2.82339, 724, True], '10': [2.8101, 724, True], '100': [2.81052, 724, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 182 | 0.2492 (±0.0081) | 0.2444 | 0.6933 | 0.6819 | [[0, 0.2, 1, 0.198, 1.0, 0.0], [0.2, 0.4, 58, 0.347, 0.379, 0.064], [0.4, 0.6, 113, 0.469, 0.451, 0.047], [0.6, 0.8, 10, 0.626, 0.3, 0.145]]
Auswärtssieg | 182 | 0.2171 (±0.0144) | 0.2175 | 0.6255 | 0.6268 | [[0, 0.2, 12, 0.149, 0.167, 0.108], [0.2, 0.4, 154, 0.294, 0.331, 0.038], [0.4, 0.6, 16, 0.454, 0.312, 0.116]]
BTTS Ja | 182 | 0.2556 (±0.0046) | 0.2429 | 0.7049 | 0.6789 | [[0.2, 0.4, 11, 0.345, 0.818, 0.116], [0.4, 0.6, 168, 0.496, 0.631, 0.037], [0.6, 0.8, 3, 0.654, 0.667, 0.272]]
Over 2,5 / Under 2,5 | 182 | 0.2682 (±0.0063) | 0.2536 | 0.7308 | 0.7003 | [[0.2, 0.4, 38, 0.365, 0.579, 0.08], [0.4, 0.6, 139, 0.468, 0.647, 0.041], [0.6, 0.8, 5, 0.633, 0.6, 0.219]]

## Ecuador Serie A (Saison-ID 16714)

Saisons [8934, 11157, 15842, 16714]; 1069 Spiele (2023-02-25 bis 2026-11-02); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.0162; Heimvorteil 0.3410.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.82017, 428, True], '1': [2.81048, 428, True], '10': [2.78856, 428, True], '100': [2.79875, 428, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 107 | 0.2391 (±0.011) | 0.249 | 0.6711 | 0.6911 | [[0.2, 0.4, 37, 0.343, 0.378, 0.08], [0.4, 0.6, 58, 0.492, 0.5, 0.066], [0.6, 0.8, 12, 0.663, 0.583, 0.142]]
Auswärtssieg | 107 | 0.1936 (±0.0197) | 0.2019 | 0.5709 | 0.5937 | [[0, 0.2, 22, 0.156, 0.136, 0.073], [0.2, 0.4, 75, 0.284, 0.293, 0.053], [0.4, 0.6, 10, 0.457, 0.5, 0.158]]
BTTS Ja | 107 | 0.2607 (±0.0068) | 0.2508 | 0.7148 | 0.6947 | [[0.2, 0.4, 18, 0.378, 0.556, 0.117], [0.4, 0.6, 89, 0.471, 0.539, 0.053]]
Over 2,5 / Under 2,5 | 107 | 0.2614 (±0.0104) | 0.2516 | 0.7169 | 0.6963 | [[0.2, 0.4, 45, 0.353, 0.489, 0.075], [0.4, 0.6, 62, 0.474, 0.5, 0.064]]

## Paraguay División Profesional (Saison-ID 16533)

Saisons [8783, 11141, 16333, 16533]; 1025 Spiele (2023-01-27 bis 2026-11-01); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.1199; Heimvorteil 0.0999.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.80382, 410, True], '1': [2.8007, 410, True], '10': [2.79561, 410, True], '100': [2.8054, 410, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 103 | 0.2158 (±0.0141) | 0.2399 | 0.6228 | 0.6729 | [[0, 0.2, 4, 0.166, 0.25, 0.217], [0.2, 0.4, 52, 0.313, 0.25, 0.06], [0.4, 0.6, 42, 0.486, 0.571, 0.076], [0.6, 0.8, 5, 0.652, 0.6, 0.219]]
Auswärtssieg | 103 | 0.2112 (±0.0165) | 0.2355 | 0.6084 | 0.6645 | [[0, 0.2, 11, 0.162, 0.091, 0.087], [0.2, 0.4, 60, 0.3, 0.317, 0.06], [0.4, 0.6, 30, 0.464, 0.567, 0.09], [0.6, 0.8, 2, 0.645, 0.5, 0.354]]
BTTS Ja | 103 | 0.2457 (±0.0057) | 0.25 | 0.6846 | 0.6931 | [[0.2, 0.4, 8, 0.387, 0.625, 0.171], [0.4, 0.6, 95, 0.478, 0.505, 0.051]]
Over 2,5 / Under 2,5 | 103 | 0.2482 (±0.0091) | 0.2552 | 0.6897 | 0.7036 | [[0.2, 0.4, 33, 0.362, 0.424, 0.086], [0.4, 0.6, 70, 0.467, 0.529, 0.06]]

## Polen 1. Liga (Saison-ID 17301)

Saisons [9596, 12156, 14877, 17301]; 1033 Spiele (2023-07-21 bis 2026-11-02); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.2297; Heimvorteil 0.1572.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [3.11059, 413, True], '1': [3.03126, 413, True], '10': [2.99886, 413, True], '100': [3.00201, 413, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 104 | 0.2555 (±0.013) | 0.25 | 0.7086 | 0.6933 | [[0, 0.2, 1, 0.154, 1.0, 0.0], [0.2, 0.4, 42, 0.33, 0.476, 0.077], [0.4, 0.6, 56, 0.486, 0.411, 0.066], [0.6, 0.8, 5, 0.631, 0.6, 0.219]]
Auswärtssieg | 104 | 0.2062 (±0.017) | 0.2038 | 0.6016 | 0.5981 | [[0, 0.2, 9, 0.174, 0.111, 0.105], [0.2, 0.4, 71, 0.301, 0.282, 0.053], [0.4, 0.6, 23, 0.451, 0.348, 0.099], [0.6, 0.8, 1, 0.613, 0.0, 0.0]]
BTTS Ja | 104 | 0.2425 (±0.0074) | 0.248 | 0.6779 | 0.6892 | [[0.4, 0.6, 80, 0.517, 0.525, 0.056], [0.6, 0.8, 24, 0.63, 0.625, 0.099]]
Over 2,5 / Under 2,5 | 104 | 0.2429 (±0.0078) | 0.2518 | 0.6789 | 0.6968 | [[0.2, 0.4, 8, 0.375, 0.375, 0.171], [0.4, 0.6, 79, 0.51, 0.494, 0.056], [0.6, 0.8, 17, 0.637, 0.588, 0.119]]

## Brasilien Série A (Saison-ID 16544)

Saisons [9035, 11321, 14231, 16544]; 1470 Spiele (2023-04-15 bis 2026-11-02); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.0396; Heimvorteil 0.3325.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.83489, 588, True], '1': [2.82711, 588, True], '10': [2.81575, 588, True], '100': [2.82618, 588, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 147 | 0.231 (±0.0086) | 0.2493 | 0.6531 | 0.6917 | [[0.2, 0.4, 39, 0.327, 0.256, 0.07], [0.4, 0.6, 86, 0.492, 0.5, 0.054], [0.6, 0.8, 22, 0.633, 0.727, 0.095]]
Auswärtssieg | 147 | 0.1778 (±0.0159) | 0.1884 | 0.538 | 0.5642 | [[0, 0.2, 35, 0.166, 0.171, 0.064], [0.2, 0.4, 91, 0.281, 0.231, 0.044], [0.4, 0.6, 21, 0.45, 0.476, 0.109]]
BTTS Ja | 147 | 0.2532 (±0.0033) | 0.2486 | 0.6996 | 0.6904 | [[0.2, 0.4, 1, 0.4, 0.0, 0.0], [0.4, 0.6, 146, 0.494, 0.596, 0.041]]
Over 2,5 / Under 2,5 | 147 | 0.2539 (±0.0053) | 0.2527 | 0.7013 | 0.6986 | [[0.2, 0.4, 18, 0.376, 0.722, 0.106], [0.4, 0.6, 128, 0.482, 0.5, 0.044], [0.6, 0.8, 1, 0.603, 0.0, 0.0]]
