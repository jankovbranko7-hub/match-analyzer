# Rückblick-Test 05.11.2026 – Prüfstand für v1.4

**Zweck:** Modellvarianten zeitlich vorwärts auf unberührten Spielen prüfen (Abschnitte 5.3, 5.5, 5.6), bevor v1.4 aktiviert wird. Das ist eine historische Simulation, keine Vorhersage.

**Datensatz:** 29 Wettbewerbe (alle bisher genutzten Ligen und die Champions League), je laufende plus bis zu drei vorherige Saisons, Daten-Snapshot 04.11.2026 16:19 UTC. Nur Spiele mit Status `complete`, K.-o.-/Play-off-Runden (Spieltag 0) ausgeschlossen. Pro Liga:
- Die ersten 50 % der Spiele, chronologisch sortiert, dienen zum Training.
- Vier Blöcke bis 90 % dienen zur Wahl von alpha (und für die Zeitgewichtung xi).
- Die letzten 10 % sind der unberührte Test, trainiert auf den ersten 90 %.

Getestet wurden 3.325 Spiele, davon 3.247 mit vollständigen Quoten.

**Varianten:**
- **base:** Tormodell v1.3.
- **decay:** Zeitgewichtung exp(−xi·Alter in Tagen), xi aus {0, 0,0005, 0,001, 0,002, 0,004} vorwärts gewählt.
- **dc:** Dixon-Coles-Korrektur, rho auf dem Training geschätzt.
- **both:** decay und dc zusammen.
- **xg:** Poisson-Modell mit Spiel-xG als Zielgröße, Tore wenn xG fehlen; die xG-Abdeckung im Training lag bei 88–100 %.
- **market:** margenbereinigte Wahrscheinlichkeiten aus den FootyStats-Quoten. Ob es Eröffnungs- oder Schlussquoten sind, wurde nicht geprüft.

**Brier-Score im unberührten Test (3.247 Spiele; kleiner ist besser):**

Markt | base | decay | dc | both | xg | market
---|---|---|---|---|---|---
Heimsieg | 0,2283 | 0,2293 | 0,2284 | 0,2294 | 0,2346 | 0,2173
Auswärtssieg | 0,1992 | 0,1995 | 0,1993 | 0,1996 | 0,2049 | 0,1905
BTTS Ja | 0,2513 | 0,2508 | 0,2509 | 0,2504 | 0,2478 | 0,2460
Over 2,5 | 0,2488 | 0,2490 | 0,2488 | 0,2490 | 0,2483 | 0,2419

**Mischung Markt + xG:** Das Gewicht wurde auf einer Hälfte der Ligen gewählt und auf der anderen geprüft. Gegenüber der reinen Marktquote gab es keinen relevanten Gewinn.

**Mechanische Auswahlregeln** (nur zur Einordnung, keine Regel des Systems):

Regel | Ergebnis
---|---
Modell-p ≥ 0,55 | 58 % Treffer, ROI −7 % vor Kosten
Modell-p ≥ 0,70 | 73 % Treffer, ROI −2 %
Marktfavorit ≥ 0,75 | 87 % Treffer, ROI +1 %
Modell-p · Quote ≥ 1,0 | ROI −12 %
Modell-p · Quote ≥ 1,2 | ROI −17 %

**Abweichung Modell − Markt** (6.961 mögliche Tipps mit Modell-p ≥ 0,5; v1.4-Wahrscheinlichkeiten):

Abweichung | n | Ø Modell | Ø Markt | beobachtet
---|---|---|---|---
0 bis +5 Pkt. | 1.948 | 55 % | 53 % | 54 %
+5 bis +10 Pkt. | 1.219 | 55 % | 48 % | 48 %
+10 bis +15 Pkt. | 400 | 55 % | 43 % | 43 %

Dagegen die echten v1.3-Tipps vom 02. bis 04.11.: Bei mehr als 5 Punkten Abweichung trafen 9 von 11 Tipps. Das ist eine sehr kleine Stichprobe.

**Entscheidung v1.4:**
- **xg** für BTTS und Over/Under übernommen.
- **decay** und **dc** nicht übernommen.
- **Marktgegenprobe** als Transparenzangabe (Variante B), ohne Sperrwirkung.

Die Wahl der Variante hat der Nutzer an Claude übertragen.
