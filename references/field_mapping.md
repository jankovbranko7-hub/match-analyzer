---
description: "Exakte Feldnamen der FootyStats-API für Team-Stats und Last-X."
---

# Feld-Mapping FootyStats

## League Teams (`/league-teams?include=stats`)

Unter `stats` (oder top-level je nach Response):

| Bedeutung          | Gesamt                  | zu Hause               | auswärts               |
|--------------------|-------------------------|------------------------|------------------------|
| Spiele             | seasonMatchesPlayed_overall | seasonMatchesPlayed_home | seasonMatchesPlayed_away |
| Tore               | seasonGoals_overall     | seasonGoals_home       | seasonGoals_away       |
| Gegentore          | seasonConceded_overall  | seasonConceded_home    | seasonConceded_away    |
| xG für (Total)     | xg_for_overall          | xg_for_home            | xg_for_away            |
| xG dagegen (Total) | xg_against_overall      | xg_against_home        | xg_against_away        |

Averages existieren zusätzlich (`xg_for_avg_*`, `seasonScoredAVG_*` etc.), aber nutze die Totals für die Tabelle, wenn vorhanden. Sonst Avg und vermerke.

## Last X (`/lastx`)

Gleiche Feldnamen unter dem Eintrag mit `last_x_match_num: 6`.  
Zusätzlich oft `formRun_overall` (z.B. "wwdlww").

## Match Details (`/match`)

Kontext-Felder (nicht für Wette):

- Pre-Match xG / Potential: `avg_potential`, `btts_potential`, `o25_potential`, `u25_potential`
- Odds: `odds_btts_yes`, `odds_ft_over25` etc.
- PPG: `pre_match_home_ppg`, `pre_match_away_ppg`

Immer „fehlt“ schreiben, wenn Feld nicht vorhanden.
