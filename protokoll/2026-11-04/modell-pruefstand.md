# Modell-Prüfstand 04.11.2026 · Stichtag 2026-11-04 16:19 UTC

Modell: Poisson-v1.3-reg (reguliertes unabhängiges Poisson nach Abschnitt 5.3, Tore, 4 Saisons, gleiche Gewichte). alpha aus {0.1, 1, 10, 100}: Training auf den ersten 50 % der chronologisch sortierten Spiele, Bewertung auf vier folgenden Blöcken bis 90 % (wachsendes Trainingsfenster), mittlerer negativer Poisson-Log-Score der Torpaare; bei Gleichstand größeres alpha. Unberührter Test: letzte 10 %, trainiert auf den ersten 90 % mit gewähltem alpha. Endmodell auf allen Vorabspielen. Grundrate = Trefferanteil im Trainingsteil. K.-o.-/Play-off-Runden (Spieltag 0) sind ausgeschlossen. Der Vergleich mit der Grundrate beschreibt Stärken und Schwächen, er ist keine Freigabehürde.

## UEFA Champions League (Saison-ID 17128)

Saisons [9543, 12321, 14924, 17128]; 447 Spiele (2023-09-19 bis 2026-11-03); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.3043; Heimvorteil 0.2986.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [3.52689, 179, True], '1': [3.34498, 179, True], '10': [3.25994, 179, True], '100': [3.34232, 179, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 45 | 0.195 (±0.0154) | 0.2492 | 0.5769 | 0.6916 | [[0.2, 0.4, 16, 0.335, 0.188, 0.098], [0.4, 0.6, 20, 0.517, 0.75, 0.097], [0.6, 0.8, 9, 0.675, 0.778, 0.139]]
Auswärtssieg | 45 | 0.1878 (±0.0271) | 0.2222 | 0.5565 | 0.6365 | [[0, 0.2, 11, 0.155, 0.182, 0.116], [0.2, 0.4, 23, 0.297, 0.217, 0.086], [0.4, 0.6, 11, 0.467, 0.727, 0.134]]
BTTS Ja | 45 | 0.2656 (±0.0221) | 0.2495 | 0.727 | 0.6921 | [[0.4, 0.6, 15, 0.559, 0.733, 0.114], [0.6, 0.8, 30, 0.667, 0.433, 0.09]]
Over 2,5 / Under 2,5 | 45 | 0.2223 (±0.0238) | 0.211 | 0.6387 | 0.6135 | [[0.4, 0.6, 8, 0.538, 0.875, 0.117], [0.6, 0.8, 37, 0.675, 0.676, 0.077]]

## England Championship (Saison-ID 17184)

Saisons [9663, 12451, 14930, 17184]; 1821 Spiele (2023-08-04 bis 2026-11-03); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.1435; Heimvorteil 0.2336.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.82851, 728, True], '1': [2.82503, 728, True], '10': [2.81112, 728, True], '100': [2.80911, 728, True]} → gewählt 100.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 183 | 0.2422 (±0.0053) | 0.2447 | 0.6774 | 0.6826 | [[0.2, 0.4, 28, 0.381, 0.357, 0.091], [0.4, 0.6, 155, 0.447, 0.439, 0.04]]
Auswärtssieg | 183 | 0.2165 (±0.0138) | 0.219 | 0.6238 | 0.6299 | [[0.2, 0.4, 183, 0.3, 0.322, 0.035]]
BTTS Ja | 183 | 0.2467 (±0.0018) | 0.2433 | 0.6864 | 0.6798 | [[0.4, 0.6, 183, 0.509, 0.628, 0.036]]
Over 2,5 / Under 2,5 | 183 | 0.2592 (±0.0034) | 0.2533 | 0.7116 | 0.6997 | [[0.4, 0.6, 183, 0.466, 0.628, 0.036]]

## Belgien Pro League (Saison-ID 17171)

Saisons [9577, 12137, 14937, 17171]; 1025 Spiele (2023-07-28 bis 2026-11-01); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.1728; Heimvorteil 0.2452.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.98626, 410, True], '1': [2.98019, 410, True], '10': [2.96032, 410, True], '100': [2.96201, 410, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 103 | 0.2121 (±0.0118) | 0.2555 | 0.6119 | 0.7042 | [[0, 0.2, 2, 0.183, 0.0, 0.0], [0.2, 0.4, 35, 0.312, 0.343, 0.08], [0.4, 0.6, 52, 0.483, 0.538, 0.069], [0.6, 0.8, 13, 0.667, 0.846, 0.1], [0.8, 1.0, 1, 0.83, 1.0, 0.0]]
Auswärtssieg | 103 | 0.1649 (±0.0153) | 0.2066 | 0.5038 | 0.6036 | [[0, 0.2, 18, 0.147, 0.0, 0.0], [0.2, 0.4, 63, 0.293, 0.222, 0.052], [0.4, 0.6, 21, 0.488, 0.714, 0.099], [0.6, 0.8, 1, 0.601, 1.0, 0.0]]
BTTS Ja | 103 | 0.2577 (±0.006) | 0.254 | 0.7087 | 0.7011 | [[0.2, 0.4, 1, 0.39, 1.0, 0.0], [0.4, 0.6, 93, 0.513, 0.462, 0.052], [0.6, 0.8, 9, 0.619, 0.556, 0.166]]
Over 2,5 / Under 2,5 | 103 | 0.2432 (±0.0072) | 0.2446 | 0.679 | 0.6824 | [[0.2, 0.4, 9, 0.364, 0.333, 0.157], [0.4, 0.6, 82, 0.504, 0.646, 0.053], [0.6, 0.8, 12, 0.638, 0.833, 0.108]]

## Brasilien Série A (Saison-ID 16544)

Saisons [9035, 11321, 14231, 16544]; 1472 Spiele (2023-04-15 bis 2026-11-04); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.0392; Heimvorteil 0.3323.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.83248, 588, True], '1': [2.82463, 588, True], '10': [2.81347, 588, True], '100': [2.82515, 588, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 148 | 0.2307 (±0.0086) | 0.2494 | 0.6528 | 0.6919 | [[0.2, 0.4, 39, 0.328, 0.256, 0.07], [0.4, 0.6, 86, 0.491, 0.512, 0.054], [0.6, 0.8, 23, 0.632, 0.696, 0.096]]
Auswärtssieg | 148 | 0.1775 (±0.0158) | 0.1875 | 0.537 | 0.5624 | [[0, 0.2, 36, 0.167, 0.167, 0.062], [0.2, 0.4, 90, 0.28, 0.222, 0.044], [0.4, 0.6, 22, 0.445, 0.5, 0.107]]
BTTS Ja | 148 | 0.2533 (±0.0033) | 0.2486 | 0.6997 | 0.6904 | [[0.2, 0.4, 1, 0.4, 0.0, 0.0], [0.4, 0.6, 147, 0.494, 0.592, 0.041]]
Over 2,5 / Under 2,5 | 148 | 0.2543 (±0.0053) | 0.2525 | 0.7022 | 0.6981 | [[0.2, 0.4, 18, 0.376, 0.722, 0.106], [0.4, 0.6, 129, 0.483, 0.496, 0.044], [0.6, 0.8, 1, 0.603, 0.0, 0.0]]

## Kolumbien Primera A (Saison-ID 16614)

Saisons [8936, 10997, 14086, 16614]; 1681 Spiele (2023-01-25 bis 2026-11-03); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu -0.0847; Heimvorteil 0.3766.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.75062, 672, True], '1': [2.74817, 672, True], '10': [2.74764, 672, True], '100': [2.76434, 672, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 169 | 0.2319 (±0.0086) | 0.2476 | 0.6563 | 0.6883 | [[0.2, 0.4, 52, 0.333, 0.269, 0.062], [0.4, 0.6, 90, 0.496, 0.478, 0.053], [0.6, 0.8, 27, 0.644, 0.667, 0.091]]
Auswärtssieg | 169 | 0.1717 (±0.0151) | 0.1869 | 0.5205 | 0.5612 | [[0, 0.2, 47, 0.156, 0.085, 0.041], [0.2, 0.4, 107, 0.283, 0.28, 0.043], [0.4, 0.6, 15, 0.445, 0.533, 0.129]]
BTTS Ja | 169 | 0.2639 (±0.0059) | 0.2541 | 0.7214 | 0.7014 | [[0.2, 0.4, 29, 0.376, 0.552, 0.092], [0.4, 0.6, 140, 0.448, 0.557, 0.042]]
Over 2,5 / Under 2,5 | 169 | 0.2523 (±0.0086) | 0.2525 | 0.6983 | 0.6982 | [[0.2, 0.4, 84, 0.358, 0.44, 0.054], [0.4, 0.6, 85, 0.448, 0.494, 0.054]]
