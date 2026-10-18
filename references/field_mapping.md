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

| Schüsse aufs Tor (für) | shotsOnTargetAVG_overall | shotsOnTargetAVG_home | shotsOnTargetAVG_away |
| Punkte pro Spiel   | seasonPPG_overall       | seasonPPG_home         | seasonPPG_away         |
| Tabellenplatz      | leaguePosition_overall  | leaguePosition_home    | leaguePosition_away    |
| Erstes Tor erzielt % | firstGoalScoredPercentage_overall | firstGoalScoredPercentage_home | firstGoalScoredPercentage_away |
| Führung zur Pause % | leadingAtHTPercentage_overall | leadingAtHTPercentage_home | leadingAtHTPercentage_away |

Schüsse aufs Tor (gegen) gibt es nicht als Feld: Sie werden aus `/league-matches` der Saison gezählt
(`team_a_shotsOnTarget`/`team_b_shotsOnTarget` des Gegners, nur Spiele mit Schussdaten). Torniveau der
Liga: Ø Tore und Over-2.5-Quote aus `/league-matches` der laufenden Saison (Spiele vor dem Anpfiff) und
der Vorsaison (Vorsaison-ID über `/league-list?chosen_leagues_only=true`). In `/lastx` ist
`leaguePosition` 0, deshalb steht der Tabellenplatz nur in den Saisonspalten.

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
