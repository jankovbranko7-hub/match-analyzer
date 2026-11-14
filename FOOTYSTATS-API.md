# FootyStats-API – genutzte Endpunkte (Stand 07.11.2026)

Basis `https://api.football-data-api.com/`, Schlüssel als Query-Parameter `key` (Umgebung `APIKEY`,
nie speichern). Antwort `{"success", "pager", "metadata", "data"}`; `metadata.request_remaining`
zeigt das Stundenkontingent (1800).

| Endpunkt | Inhalt |
|---|---|
| `league-list?chosen_leagues_only=true` | Ligen des Abos mit Saison-IDs |
| `league-matches?season_id=&max_per_page=1000` | alle Spiele einer Saison (`id`, `homeID`, `awayID`, `date_unix`, `status`, `homeGoalCount`, `awayGoalCount`) |
| `match?match_id=` | ein Spiel: Vorab-xG (`team_a_xg_prematch`), Potenziale (`o25_potential`, `btts_potential`, `avg_potential`), `pre_match_home_ppg`, `h2h`, `trends`, `lineups`; nach dem Spiel Ergebnis |
| `league-teams?season_id=&include=stats` | Saisonwerte je Team (`…_overall/_home/_away`): `seasonScoredNum`, `seasonConcededNum`, `seasonPPG`, `xg_for_avg`, `xg_against_avg`, `seasonOver25Percentage`, `seasonBTTSPercentage`, `seasonCSPercentage`, `seasonFTSPercentage`, `leaguePosition` |
| `lastx?team_id=` | letzte 5/6/10 über alle Wettbewerbe (`last_x_match_num`), gleiche Felder |

Hinweise: `seasonGoals_*` enthält Torminuten (Liste), Torzahlen stehen in `seasonScoredNum_*`.
`todays-matches` ist unvollständig; Spiele über `league-matches` suchen. Quotenfelder (`odds_*`)
werden im Forebet-Check v2 nicht verwendet.

## Saison-IDs 2026/27 (Auswahl)

| Liga | ID | Liga | ID |
|---|---|---|---|
| Bundesliga | 17210 | Premier League | 17146 |
| 2. Bundesliga | 17212 | Championship | 17184 |
| 3. Liga | 17267 | League One | 17180 |
| La Liga | 17199 | Serie A | 17084 |
| Segunda División | 17269 | Serie B | 17404 |
| Ligue 1 | 17102 | Ligue 2 | 17117 |
| Eredivisie | 17097 | Pro League (BEL) | 17171 |
| Österreich Bundesliga | 17181 | Süper Lig | 17265 |
| Liga Portugal | 17217 | Schottland Premiership | 17148 |
| Schweiz Super League | 17129 | Dänemark Superliga | 17091 |
| Allsvenskan (2026) | 16576 | Eliteserien (2026) | 16558 |
| Champions League | 17128 | Europa League | 17127 |
| Conference League | 17130 | Griechenland | 17356 |
| Nations League 2026/27 | 16808 | WM-Quali Europa (2026) | 13964 |
