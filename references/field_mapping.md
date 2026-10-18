---
description: "Feldnamen der FootyStats-API für Team-Stats und Last-X, zugeordnet zu den sechs Fragen des Spielbilds."
---

# Feld-Mapping FootyStats

## League Teams (`/league-teams?include=stats`)

Unter `stats` liefert die API je Team über 1.000 Felder. Die meisten gibt es dreifach mit der Endung
`_overall`, `_home`, `_away` (Spalten gesamt / zu Hause / auswärts). Felder ohne Endung gelten für gesamt.
`system/tabellen.py` liest alle und ordnet die spielbezogenen so zu (erstes passendes Muster gilt):

| Frage | Beispiele für Felder |
|---|---|
| 5 · Wie nah ist ein Remis? | `drawPercentage`, `seasonDrawsNum`, `drawingAtHT(Percentage)`, `BTTS_and_draw(_percentage)`, `draws_2hg` |
| 2 · Wie beginnt das Spiel? | `firstGoalScored(Percentage)`, `leadingAtHT`, `trailingAtHT`, `GoalsHT`, `scoredAVGHT`, `concededAVGHT`, `HTPPG`, `season…HT`, `goals_scored_min_*`, `goals_conceded_min_*`, `seasonScoredMin`, `btts_fhg` |
| 3 · Was passiert nach dem ersten Tor? | `BTTS_and_win/lose(_percentage)`, `BTTS_both_halves`, `AVG_2hg`, `scored_2hg`, `conceded_2hg`, `wins_2hg`, `losses_2hg`, `cs_2hg`, `fts_2hg`, `ppg_2hg`, `scoredBothHalves` |
| 4 · Trifft der Schwächere, hält der Starke die Null? | `seasonCS(Percentage)`, `seasonFTS(Percentage)`, `seasonBTTS(Percentage)`, `seasonOver*/Under*` |
| 1 · Wer hat das Spiel in der Hand? | `seasonMatchesPlayed`, `seasonGoals`, `seasonConceded`, `seasonScoredNum/AVG`, `seasonConcededNum/AVG`, `xg_for_avg`, `xg_against_avg`, `shotsAVG`, `shotsOnTargetAVG`, `possessionAVG`, `attacks_avg`, `dangerous_attacks_avg`, `seasonPPG`, `winPercentage`, `losePercentage`, `leaguePosition`, `homeAttackAdvantage` |
| 6 · Wie belastbar sind die Zahlen? | `attack_num_recoded_matches` und andere „recorded“-Zähler |

Nicht als Tabelle gezeigt, aber gelesen und verglichen: Ecken (`corners…`), Karten (`cards…`),
Abseits (`offsides…`), Fouls, `name_*` (Teamnamen in anderen Sprachen), Verwaltung (Zuschauer,
Gehalt, Stadion, Links, `previous_seasons`).

Liefert die API bei einem Feld eine Liste (z. B. `seasonGoals_home`: eine Torminute je Tor), ist die
Anzahl der Einträge der Wert.

## Last X (`/lastx`)

Gleiche Feldnamen unter dem Eintrag mit `last_x_match_num: 6`. Die API zählt alle Wettbewerbe
(Liga, Pokal, Europapokal). `seasonGoals_home/away` fehlen dort; die Tore zu Hause/auswärts stehen in
`seasonScoredNum_*` und `seasonConcededNum_*`.

## Match Details (`/match`)

Kontext-Felder (nicht für Wette):

- Pre-Match xG / Potential: `team_a_xg_prematch`, `team_b_xg_prematch`, `btts_potential`, `o25_potential`, `u25_potential`
- Odds: `odds_ft_1`, `odds_ft_x`, `odds_ft_2`, `odds_btts_yes`, `odds_ft_over25` etc.
- Direkter Vergleich: `h2h.previous_matches_results`, `h2h.betting_stats` (Hintergrund)

Immer „fehlt“ schreiben, wenn Feld nicht vorhanden.
