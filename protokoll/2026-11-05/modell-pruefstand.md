# Modell-Prüfstand 05.11.2026 · Stichtag 2026-11-05 09:51 UTC

Modell: Poisson-v1.4 (reguliertes unabhängiges Poisson nach 5.3; 1X2 aus Tormodell, BTTS/Over/Under aus xG-Variante 5.6; 4 Saisons, gleiche Gewichte). alpha aus {0.1, 1, 10, 100}: Training auf den ersten 50 % der chronologisch sortierten Spiele, Bewertung auf vier folgenden Blöcken bis 90 % (wachsendes Trainingsfenster), mittlerer negativer Poisson-Log-Score der Torpaare; bei Gleichstand größeres alpha. Unberührter Test: letzte 10 %, trainiert auf den ersten 90 % mit gewähltem alpha. Endmodell auf allen Vorabspielen. Grundrate = Trefferanteil im Trainingsteil. K.-o.-/Play-off-Runden (Spieltag 0) sind ausgeschlossen. Der Vergleich mit der Grundrate beschreibt Stärken und Schwächen, er ist keine Freigabehürde.

## UEFA Europa League (Saison-ID 17127)

Saisons [10210, 12327, 15002, 17127]; 439 Spiele (2023-09-21 bis 2026-11-04); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.1995; Heimvorteil 0.2895.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [3.23321, 176, True], '1': [2.97598, 176, True], '10': [2.89986, 176, True], '100': [2.92914, 176, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 44 | 0.2448 (±0.0109) | 0.2515 | 0.6833 | 0.6961 | [[0.2, 0.4, 5, 0.341, 0.6, 0.219], [0.4, 0.6, 38, 0.48, 0.342, 0.077], [0.6, 0.8, 1, 0.632, 1.0, 0.0]]
Auswärtssieg | 44 | 0.2665 (±0.033) | 0.2637 | 0.7323 | 0.725 | [[0, 0.2, 1, 0.163, 0.0, 0.0], [0.2, 0.4, 40, 0.279, 0.425, 0.078], [0.4, 0.6, 3, 0.425, 0.667, 0.272]]
BTTS Ja | 44 | 0.2431 (±0.007) | 0.2471 | 0.6794 | 0.6873 | [[0.4, 0.6, 44, 0.545, 0.568, 0.075]]
Over 2,5 / Under 2,5 | 44 | 0.2387 (±0.0024) | 0.2266 | 0.6705 | 0.6463 | [[0.4, 0.6, 44, 0.511, 0.773, 0.063]]

## UEFA Conference League (Saison-ID 17130)

Saisons [9600, 12278, 14904, 17130]; 348 Spiele (2023-09-20 bis 2026-10-22); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.0549; Heimvorteil 0.4626.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [3.18134, 139, True], '1': [2.94741, 139, True], '10': [2.88305, 139, True], '100': [2.91559, 139, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 35 | 0.2492 (±0.0095) | 0.2508 | 0.6915 | 0.6948 | [[0.2, 0.4, 1, 0.394, 0.0, 0.0], [0.4, 0.6, 30, 0.521, 0.467, 0.091], [0.6, 0.8, 4, 0.626, 0.75, 0.217]]
Auswärtssieg | 35 | 0.174 (±0.0379) | 0.1791 | 0.5297 | 0.5447 | [[0, 0.2, 6, 0.178, 0.0, 0.0], [0.2, 0.4, 29, 0.244, 0.276, 0.083]]
BTTS Ja | 35 | 0.2441 (±0.0039) | 0.2479 | 0.6813 | 0.6889 | [[0.4, 0.6, 35, 0.521, 0.6, 0.083]]
Over 2,5 / Under 2,5 | 35 | 0.2472 (±0.0041) | 0.2518 | 0.6876 | 0.6967 | [[0.4, 0.6, 35, 0.483, 0.486, 0.084]]

## Argentinien Primera División (Saison-ID 16571)

Saisons [8595, 11212, 15746, 16571]; 1897 Spiele (2023-01-27 bis 2026-11-03); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu -0.1432; Heimvorteil 0.3040.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.6099, 759, True], '1': [2.60421, 759, True], '10': [2.59368, 759, True], '100': [2.59144, 759, True]} → gewählt 100.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 190 | 0.2358 (±0.0051) | 0.2419 | 0.6643 | 0.6769 | [[0.2, 0.4, 34, 0.383, 0.206, 0.069], [0.4, 0.6, 156, 0.446, 0.449, 0.04]]
Auswärtssieg | 190 | 0.2111 (±0.0157) | 0.2164 | 0.613 | 0.6265 | [[0, 0.2, 1, 0.191, 0.0, 0.0], [0.2, 0.4, 189, 0.265, 0.307, 0.034]]
BTTS Ja | 190 | 0.2479 (±0.0012) | 0.2645 | 0.689 | 0.7226 | [[0.4, 0.6, 190, 0.51, 0.532, 0.036]]
Over 2,5 / Under 2,5 | 190 | 0.2448 (±0.0026) | 0.261 | 0.6826 | 0.7174 | [[0.4, 0.6, 190, 0.468, 0.447, 0.036]]

## Brasilien Série A (Saison-ID 16544)

Saisons [9035, 11321, 14231, 16544]; 1476 Spiele (2023-04-15 bis 2026-11-05); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu 0.0396; Heimvorteil 0.3312.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.83798, 590, True], '1': [2.82954, 590, True], '10': [2.81751, 590, True], '100': [2.82956, 590, True]} → gewählt 10.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 148 | 0.2303 (±0.0087) | 0.2498 | 0.6519 | 0.6928 | [[0.2, 0.4, 40, 0.329, 0.25, 0.068], [0.4, 0.6, 85, 0.495, 0.529, 0.054], [0.6, 0.8, 23, 0.637, 0.739, 0.092]]
Auswärtssieg | 148 | 0.1736 (±0.0157) | 0.1809 | 0.5287 | 0.548 | [[0, 0.2, 35, 0.164, 0.143, 0.059], [0.2, 0.4, 92, 0.279, 0.217, 0.043], [0.4, 0.6, 21, 0.448, 0.476, 0.109]]
BTTS Ja | 148 | 0.2422 (±0.0044) | 0.2486 | 0.6774 | 0.6904 | [[0.4, 0.6, 146, 0.549, 0.582, 0.041], [0.6, 0.8, 2, 0.614, 1.0, 0.0]]
Over 2,5 / Under 2,5 | 148 | 0.2494 (±0.0033) | 0.2519 | 0.692 | 0.697 | [[0.4, 0.6, 146, 0.523, 0.507, 0.041], [0.6, 0.8, 2, 0.604, 1.0, 0.0]]

## Brasilien Série B (Saison-ID 16783)

Saisons [9042, 11351, 14305, 16783]; 1500 Spiele (2023-04-14 bis 2026-11-02); Duplikate 0; ungültige Werte 0; Fit erfolgreich: True; mu -0.1002; Heimvorteil 0.3581.
alpha-Kandidaten (mittlerer neg. Log-Score, Anzahl Spiele): {'0.1': [2.68615, 600, True], '1': [2.68018, 600, True], '10': [2.66207, 600, True], '100': [2.65215, 600, True]} → gewählt 100.

Markt | n | Brier (±SE) | Brier Grundrate | Log-Loss | Log-Loss Grundrate | Kalibrierung [von, bis, n, Ø p, beobachtet, SE]
---|---|---|---|---|---|---
Heimsieg | 150 | 0.2375 (±0.0043) | 0.2493 | 0.6678 | 0.6917 | [[0.2, 0.4, 10, 0.386, 0.0, 0.0], [0.4, 0.6, 140, 0.461, 0.507, 0.042]]
Auswärtssieg | 150 | 0.2035 (±0.0175) | 0.2099 | 0.5955 | 0.6119 | [[0, 0.2, 3, 0.19, 0.0, 0.0], [0.2, 0.4, 147, 0.262, 0.299, 0.038]]
BTTS Ja | 150 | 0.2528 (±0.0024) | 0.2485 | 0.6987 | 0.6901 | [[0.4, 0.6, 150, 0.528, 0.46, 0.041]]
Over 2,5 / Under 2,5 | 150 | 0.2487 (±0.0013) | 0.2558 | 0.6906 | 0.7052 | [[0.4, 0.6, 150, 0.491, 0.467, 0.041]]
