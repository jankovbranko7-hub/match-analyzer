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

Für die Profil-Checks zusätzlich `seasonPPG_overall` (Punkte pro Spiel) und `seasonFTSPercentage_overall` (ohne eigenes Tor, %).

## Letzte 6 (`/league-matches`)

Die letzten 6 Ligaspiele vor dem Anpfiff, je Spiel aus `homeGoalCount`/`awayGoalCount`,
`team_a_xg`/`team_b_xg` und `ht_goals_team_a`/`ht_goals_team_b` gezählt (dieselben 10 Zeilen;
AVG_2hg = Tore beider Teams in der 2. Halbzeit im Schnitt). `/lastx` wird nicht mehr genutzt,
weil es Pokal- und Europapokalspiele mitzählt (geprüft am 18.10.2026).

## Vorsaison (`/team?team_id=…&include=stats`)

Liste aller Saisons des Teams. Genommen wird in der Saison vor der laufenden der Eintrag mit
den meisten `seasonMatchesPlayed_overall` (die Liga): `xg_for_avg_overall`,
`xg_against_avg_overall`, `seasonScoredAVG_overall`, `seasonConcededAVG_overall`.

## Liga-Grundwerte (`/league-matches` der Vorsaison)

Vorsaison-ID über `/league-list?chosen_leagues_only=true`; gezählt werden Ø Tore, Over 2.5 %,
BTTS %, Remis %, Heimsieg % aller beendeten Spiele.

## Match Details (`/match`)

Kontext-Felder (nicht für Wette):

- Pre-Match xG / Potential: `avg_potential`, `btts_potential`, `o25_potential`, `u25_potential`
- Odds: `odds_btts_yes`, `odds_ft_over25` etc.
- PPG: `pre_match_home_ppg`, `pre_match_away_ppg`

Immer „fehlt“ schreiben, wenn Feld nicht vorhanden.
