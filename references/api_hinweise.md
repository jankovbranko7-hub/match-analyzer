---
description: "Praktische Hinweise zur FootyStats-API: Spiele finden, Saison-IDs, Namensvarianten, Besonderheiten."
---

# API-Hinweise

## Spiele finden

`/todays-matches?date=YYYY-MM-DD` ist **unvollständig**. Zuverlässiger ist `/league-matches?season_id=...&max_per_page=1000`: Die Saison der Liga laden und nach Teilstücken beider Teamnamen suchen (z. B. „truid“ + „iberia“). Danach Datum und Wettbewerb prüfen. Ein ähnlicher Name ist weiterhin das falsche Spiel; eine Namensvariante desselben Klubs (siehe unten) ist dasselbe Spiel.

Anpfiffzeit aus `date_unix` (UTC). Spiele am späten Abend in Südamerika liegen nach deutscher Zeit oft schon am Folgetag.

## Saison-IDs (Saison 2026/27 bzw. 2026, Stand 15.10.2026)

| Wettbewerb | season_id |
|---|---|
| Champions League | 17128 |
| Europa League | 17127 |
| Conference League | 17130 |
| Premier League | 17146 |
| Championship | 17184 |
| Bundesliga | 17210 |
| 2. Bundesliga | 17212 |
| 3. Liga | 17267 |
| La Liga | 17199 |
| Segunda División | 17269 |
| Serie A | 17084 |
| Serie B | 17404 |
| Ligue 1 | 17102 |
| Ligue 2 | 17117 |
| Süper Lig | 17265 |
| TFF 1. Lig | 17290 |
| Österreich Bundesliga | 17181 |
| Belgien Pro League | 17171 |
| Polen Ekstraklasa | 17112 |
| Griechenland Super League | 17356 |
| Bulgarien | 17088 |
| Serbien | 17119 |
| Irland | 16537 |
| Saudi Pro League | 17426 |
| MLS | 16504 |
| Argentinien | 16571 |
| Brasilien Série A | 16544 |
| Brasilien Série B | 16783 |
| Kolumbien | 16614 |
| Bolivien | 16927 |
| Liga MX | 17099 |

Welche Ligen verfügbar sind, zeigt `/league-list?chosen_leagues_only=true` (hängt vom Abo ab).

## Namensvarianten (Nutzer → API)

| Nutzer | API |
|---|---|
| Iğdır FK | 76 Iğdır Belediyespor |
| Manisa FK | Manisa BBSK |
| Esenler Erokspor | Erokspor |
| Al-Fayha | Al Feiha |
| Al Taawoun | Al Taawon |
| Ararat-Armenia | FC Avan Academy |
| Red Star / Crvena Zvezda | Red Star Belgrade |
| Olympiacos | Olympiakos Piraeus |
| FC Iberia 1999 | Saburtalo |
| Pafos FC | Paphos |

## Europapokal

- Die Saisonspalten enthalten nur die Spiele des Wettbewerbs (mit Qualifikation), oft nur 1–6. Spalten mit 0 Spielen gelten als „fehlt“.
- Bei Teams mit nur 1 Spiel passen die gesamt-xG oft nicht zu den Heim-/Auswärtswerten; dann tragen vor allem die letzten 6.
- **Conference League:** Für die meisten Teams liefert die API gar keine Saisondaten (alles „fehlt“), nur die letzten 6 – und die stammen aus verschiedenen Ligen. Siehe Freigabe-Check in `SKILL.md`.
