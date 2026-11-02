# Odd Alerts API – geprüfte Endpunkte (Stand 02.11.2026)

Basis: `https://data.oddalerts.com/api/`, Schlüssel als Query-Parameter `api_token`
(aus der Umgebung `ODDALERTS_KEY`, nie speichern; in gespeicherten URLs `[REDACTED]`).
Antworten meist `{"info": {...}, "data": [...]}`; Pagination über `info.next_page_url`
(enthält den Schlüssel – vor dem Speichern ersetzen), 250 Einträge pro Seite.
Unbekannte Pfade liefern HTTP 200 mit HTML statt JSON – Antwort immer als JSON prüfen.

Zugang beim Test: Pro-Abo, API freigeschaltet. Stundenlimit nicht geprüft.

| Endpunkt | Inhalt | System |
|---|---|---|
| `fixtures/upcoming` | kommende Spiele (ca. 14 Tage): `id`, `home_id`/`away_id`, Namen, `competition_id`, `season_id`, `season`, `date` (UTC), `unix`, `status`, `is_friendly`, `is_cup`, `has_odds` | 2 |
| `fixtures/{id}` | ein Spiel, gleiche Felder; nach dem Spiel `home_goals`, `away_goals`, `ht_score`, `status` (z. B. `FT`, `CANCELLED`) | 2, 10 |
| `fixtures/between?from=&to=&competitions=` | Spiele im Zeitraum (Unix-Sekunden), optional je Wettbewerb; abgeschlossene mit Ergebnis | 3.1, 5.2, 10 |
| `stats/fixture/{id}` | Saisonstatistik beider Teams des Spiels | 4 |
| `stats/season/{season_id}` | Saisonstatistik aller Teams einer Saison | 4 |
| `stats/fixture/{id}?last_x=6_overall` | letzte 6 (auch `6_home`, `6_away`); `info.all_comps: true` = wettbewerbsübergreifend | 3.1 |
| `odds/history/{id}` | je Buchmacher/Markt/Ausgang `opening`, `closing`, `peak` | 6 (optional) |
| `odds/latest/{id}` | Quotenbewegungen der letzten `since_minutes` (5–60) | 6 (optional) |
| `competitions`, `competitions/{id}` | Wettbewerbe mit `current_season` | 2 |
| `countries`, `bookmakers` | Stammdaten | – |

Statistikfelder (jeweils `total`/`home`/`away`, dazu `_avg` bzw. `_percentage`):
`played`, `won`, `drawn`, `lost`, `points`, `goals_for`, `goals_against`, `goals_total`,
`goals_over` (o0–o3 = über 0,5 … 3,5), `btts`, `failed_to_score`, `clean_sheet`,
`xg_for`, `xg_against`, `xg_total`, `goals_1h`/`goals_2h`, `goals_for_2h`,
`goals_against_2h` u. a.; `coverage.xg` = Zahl/Anteil der Spiele mit xG. Abfrage-Info:
`lookback_days: 730`, Freundschaftsspiele standardmäßig ausgeschlossen.

Quotenmärkte: `ft_result` (home/draw/away), `btts` (yes/no), `total_goals`
(`over_25`/`under_25` u. a.). Buchmacher im Test: Pinnacle, Bet365, Betfair Exchange,
William Hill, 1xBet.

Lücken für das System:
- BTTS-and-lose nicht als Feld → aus Einzelergebnissen auszählen.
- AVG_2hg (FootyStats) gibt es nicht → `goals_2h` u. a.
- `last_x` mischt Wettbewerbe → letzte 6 bevorzugt aus `fixtures/between`.
- xG-Abdeckung je Liga unterschiedlich (Test: usbekische Pro Liga 0/6).
- Historie je Liga unterschiedlich tief (Premier League mindestens bis 2022/23).
- `teams/{id}` lieferte keine Daten; `probability/{id}` antwortete „Invalid type provided“
  und ist ohnehin kein Modell im Sinne von Abschnitt 5.
