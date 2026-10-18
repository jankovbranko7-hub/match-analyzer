# Sample size, stability and home advantage in football team statistics

Scope: club football, European domestic leagues. Research date: 18 Oct 2026. About 22 searches and fetches. Several key methodology pages could not be retrieved (FiveThirtyEight club-soccer methodology now redirects to abcnews.com, web.archive.org is blocked for the fetch tool, and the Club Elo "System" page did not return its methodology text). Those gaps are listed under each question.

Source-quality legend used below: **[peer-reviewed]**, **[analyst blog]**, **[company/betting blog]** (lower weight, often promotional), **[journalism]**.

---

## 1. How quickly do team xG, shots, goals and points stabilize? (concrete numbers of matches)

### Takeaway
Shot-based measures (shots, shots on target, shot share, and by extension xG) settle much faster than goals and points. Goals conceded is among the noisiest team numbers. After about 7 matches, early shot and shot-on-target numbers correlate about r ≈ 0.6 with the rest of the season, while goals conceded sits around r ≈ 0.4 and barely improves by match 15. No published formal split-half study giving an exact "N games" figure for team xG was found. Informal analyst rules put the point where xG beats goals as a guide at roughly 3–7 matches, with "reliable" needing half a season or more.

### Cited Findings
**Large recent multi-league correlation study (company blog, so treat with caution, but the method is transparent):**
- Sample: 725 team-seasons from 21 European leagues (192 from the big five), seasons 2024/25, 2025/26 and 2026/27 to date. Method: average over the first N matches vs average over all remaining league matches, both relative to the league-season average. Metric is Pearson r. Last updated 11 Oct 2026. No xG was analysed (only shots and shots on target). — [StatPair, "Early-Season Football Stats" [company/betting blog]](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)
- Team correlations, first N matches vs rest of season (after 3 / 5 / 7 / 10 / 15 matches):
  - Shots: 0.52 / 0.58 / 0.63 / 0.66 / 0.70
  - Shots on target: 0.49 / 0.59 / 0.62 / 0.68 / 0.68
  - Goals scored: 0.43 / 0.53 / 0.58 / 0.58 / 0.61
  - Points per game: 0.41 / 0.51 / 0.58 / 0.59 / 0.59
  - Shots conceded: 0.49 / 0.53 / 0.57 / 0.63 / 0.63
  - Shots on target conceded: 0.42 / 0.45 / 0.51 / 0.54 / 0.53
  - Goals conceded: 0.28 / 0.35 / 0.43 / 0.43 / 0.41
  - Corners: 0.39 / 0.42 / 0.49 / 0.51 / 0.48
  - Yellow cards: 0.16 / 0.18 / 0.20 / 0.24 / 0.23
  — [StatPair](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)
- Big five only, after 7 matches: goals scored r = 0.68, shots on target r = 0.71, goals conceded r = 0.41. — [StatPair](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)
- Underlying stats beat results as predictors. Early shots-on-target difference predicts rest-of-season points at r = 0.52 / 0.58 / 0.63 / 0.66 after 3 / 5 / 7 / 10 matches. Early points predict rest-of-season points at only 0.41 / 0.51 / 0.58 / 0.59. Early shots on target predict future goals scored better than early goals do (0.63 vs 0.61 after 7; 0.66 vs 0.61 after 10). — [StatPair](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)
- Teams in the top fifth after 7 matches kept only about 54% of their shot advantage, 42% of their goals-scored advantage and 26% of their (worst-defence) goals-conceded deviation over the rest of the season. That is strong regression to the mean, especially on defence. — [StatPair](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)
- The authors' own summary is that "attack settles faster than defence", and that goals conceded (0.43 after 7, 0.41 after 15) is one of the least reliable team numbers. — [StatPair](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)

**Shot ratio (TSR) repeatability, older Premier League work:**
- Total Shots Ratio (shots for / (shots for + against)) is "staggeringly consistent" across a season, while PDO (shooting % + save %) is "largely luck driven". Points are "pretty randomly distributed throughout a season." In split-season tests (first 9 vs final 29, first 14 vs final 24, first 19 vs final 19 matches), "shots were far and away the most useful metric" for predicting future points. — [James Grayson, first 19 vs final 19 [analyst blog, ~2013]](https://jameswgrayson.wordpress.com/2013/12/30/which-metrics-are-the-most-repeatable-between-the-first-19-and-final-19-games-of-the-season/)
- TSR shows only about 14% regression toward the mean season to season (roughly an "86% skill / 14% luck" split in Premier League seasons, the same as the shots-on-target ratio). Shot metrics have a "head start" over goals early in the season. — [James Grayson blog (via search results)](https://jameswgrayson.wordpress.com/2013/11/07/how-repeatable-are-shots-on-target/); [Grayson, first 14 vs final 24](https://jameswgrayson.wordpress.com/2013/12/11/which-metrics-are-the-most-repeatable-between-the-first-14-and-final-24-games-of-the-season/)
- Caveat: TSR treats all shots as equal and ignores shot location. — [The Stat Attack, "The Curious Case of Expected Goal Ratio"](https://thestatattackblog.wordpress.com/2014/01/10/the-curious-case-of-expected-goal-ratio/)

**xG specifically:**
- American Soccer Analysis says xG takes "about seven games before it unveils its magical powers", and single-match xG is of limited use for judging who "deserved" to win. This is a rule of thumb, not a formal reliability test. — [American Soccer Analysis, "Single Game xG is here to stay – is it useful?" (2 Mar 2020) [analyst blog]](https://www.americansocceranalysis.com/home/2020/3/2/single-game-xg-is-here-to-stay-is-it-useful)
- Journalistic claim: "somewhere around the three- to five-game mark, a team's xG difference reliably gives more information about a team's future performance than their goal difference." — [CBS Sports guide [journalism]](https://www.cbssports.com/soccer/news/fifa-2026-world-cup-expected-goals-analytics-soccer-nerd/)
- A peer-reviewed comparison of xG, shots and goals across the top five European leagues found xG was the stronger indicator of team performance in nearly every league and measure (exception: precision in Serie A). Future performance was defined over the subsequent six matches. — [PLOS ONE 2023, "Expected goals in football: Improving model performance and demonstrating value" [peer-reviewed]](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0282295)
- Before kickoff, xG from the last three matches gave 0.556 outcome-prediction accuracy in the Bundesliga, versus 0.583 for expected possession value (EPV). So short-window xG is only modestly predictive. — [PMC12640942, Bundesliga EPV vs xG (2025) [peer-reviewed]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12640942/)
- One forecasting paper found predicted xG "would not necessarily outperform" predictions based on other statistics. — [arXiv 2001.09097, "Forecasting football matches by predicting match statistics"](https://arxiv.org/pdf/2001.09097)

**Luck vs skill in season-level points:**
- A preregistered study of the top seven European leagues over three seasons attributes about 40% of the variation in over- or underperformance against expected points (xPts) to skill and about 60% to luck. Over 38 matches that is a points SD of about 6 (skill) vs about 7 (luck). — [Holzmeister & Johannesson 2025, Journal of Sports Economics, "Skills vs. Luck: Decomposing Deviations from Expected Performance in European Football Leagues" [peer-reviewed]](https://journals.sagepub.com/doi/10.1177/15270025251374620)
- Older estimates (Mauboussin, relayed secondhand) put luck's share of Premier League standings variance at about 27–31%, or "around half the spread of points". These are secondhand blog figures. — [Rob Fielder Substack](https://robfielder.substack.com/p/the-table-never-lies-the-importance); [Optimum Sports Performance blog](https://optimumsportsperformance.com/blog/the-role-of-skill-vs-luck-in-team-sport-winning/)
- First-half vs second-half over- or underperformance (Premier League and Football League) showed "virtually no correlation" and "an almost perfect regression to the mean". — [Pinnacle, "Regression to the mean in sports betting" [company/betting blog]](https://www.pinnacle.com/betting-resources/en/betting-strategy/regression-to-the-mean-in-sports-betting/ewp2a8kl7mmhuqcm)

### Inferences
- Rough stability ranking for team stats, from fastest to slowest: passes/possession > shots ≈ shots on target (and xG, which is shot-based) > goals scored ≈ points > shots conceded > shots on target conceded > goals conceded > cards.
- After 3 matches, every results-based team number (goals for and against, points) has r ≤ 0.43 with the rest of the season. Most of the variation is still noise, and goals conceded is close to "mostly noise" (r = 0.28).
- Practical thresholds from the numbers above: about 5–7 matches before shots/xG are "partly signal" (r ≈ 0.6); about 10–15 matches before shot numbers reach about 0.65–0.70. Goals conceded never gets clearly above 0.45 within 15 matches, so defensive solidity judged from goals conceded should be treated as weak evidence all season. Shots or xG against are better.
- Overperformance against xG or xPts largely does not persist (the 60% luck share, plus the near-zero half-season correlation of overperformance).

### Gaps
- No published formal split-half reliability study with an exact "N matches" number for team xG for/against was found. The StatPair study did not include xG. Its shot-based numbers are the closest proxy.
- No league-specific stabilization figures for second tiers (Championship, 2. Bundesliga, Segunda, Serie B, Ligue 2) were found.
- Grayson's exact R values could not be read (they sit in image tables).

---

## 2. Blending early-season data with previous-season data (priors, regression, promoted teams, squad changes)

### Takeaway
At matchday 7, last season's numbers alone still predicted the rest of the season better than the first 7 matches for every team stat tested. A blend of roughly 70% last season / 30% current season was best or joint-best (company-blog study, same-league teams only). Professional rating systems (FiveThirtyEight SPI, Club Elo, Caley's Expecting Goals ratings) all carry a prior from the previous season and/or squad value into the new season rather than resetting. Their exact weights could not be retrieved. No quantitative evidence on promoted teams or summer squad changes was found.

### Cited Findings
- 280 teams that stayed in the same league (promoted and relegated teams excluded), predicting the rest of 2025/26. Each figure is the correlation with the rest of the season, given as last season only / first 7 matches only / 50/50 blend / 70/30 (last season / first 7):
  - Goals scored: 0.67 / 0.59 / 0.70 / 0.72
  - Goals conceded: 0.47 / 0.41 / 0.51 / 0.54
  - Shots: 0.68 / 0.64 / 0.73 / 0.73
  - Corners: 0.60 / 0.47 / 0.62 / 0.65
  - Yellow cards: 0.39 / 0.22 / 0.35 / 0.40
  - Blend weights at other matchdays were not tested; only matchday 7 was. — [StatPair [company/betting blog]](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)
- The same source recommends blending in last season until at least about matchday 10–15, "unless the squad or manager has changed significantly". It also recommends shrinking early numbers toward the league average. Neither recommendation is quantified. — [StatPair](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study) (as summarised in search results)
- Michael Caley's Expecting Goals team ratings are "a weighted average of team performance combining goals and xG, regressed to estimated team value". Performance is adjusted for red cards (10 v 11 periods scaled by 1.4) and opposition quality. For promoted sides, "past performance is adjusted for league difficulty". Weights and fade rates are behind a paywall. — [Expecting Goals, Premier League Team Ratings (Michael Caley, 28 Oct 2025) [analyst blog]](https://www.expectinggoals.com/p/expecting-goals-premier-league-team)
- FiveThirtyEight's club SPI (a revised version of ESPN's Soccer Power Index) gives each team offensive and defensive ratings. "Before a season begins, a team's SPI ratings are based on two f[actors]…" (the snippet was truncated, and the full page now redirects to abcnews.com). — [FiveThirtyEight, "How our club soccer predictions work"](https://fivethirtyeight.com/features/how-our-club-soccer-predictions-work/) (only the search snippet was visible)
- Club Elo carries ratings over continuously, with no seasonal reset visible on the site. Ratings are shown with an uncertainty band (e.g. "±81"). It uses a logistic expectancy W_e = 1/(1+10^(−d/400)), and secondary sources cite k = 20. — [clubelo.com](http://clubelo.com/System); [arXiv 2007.03412](https://arxiv.org/pdf/2007.03412); [arXiv 1912.02076](https://arxiv.org/pdf/1912.02076)
- TSR regresses only about 14% toward the mean from one season to the next, so last season's shot dominance is a strong prior. — [James Grayson blog](https://jameswgrayson.wordpress.com/2013/11/07/how-repeatable-are-shots-on-target/)

### Inferences
- For a qualitative picture around matchdays 1–7, last season's underlying numbers (shots/xG for and against) should dominate. Current-season data should mainly confirm or flag changes. Around matchday 10–15 the weights plausibly approach parity, although the source only tested matchday 7.
- The larger the squad or manager change, the less weight last season should get. Defensive numbers (goals conceded) need the most regression in both directions.
- Promoted teams have no same-league prior. Rating systems handle this with a league-difficulty adjustment (Caley) or squad value (likely FiveThirtyEight, unverified). In practice their second-tier numbers overstate their top-flight level.

### Gaps
- The exact FiveThirtyEight SPI preseason formula (previous-season weight, market-value weight, reversion, and how fast preseason ratings fade during the season) could not be retrieved: the page redirects and archive.org is blocked.
- The Club Elo methodology page (promoted-team handling, home-advantage update rule) was not readable.
- No quantitative study was found on summer squad turnover or manager changes and how much they reduce the value of last season's data.
- No study was found comparing promoted teams' second-tier xG with their top-flight xG, or giving a recommended discount.
- Only one source (a company blog, not peer-reviewed) tests blend weights at all.

---

## 3. Recent form (last 5/6 matches) vs season-long performance; is there a hot hand or momentum effect?

### Takeaway
"Form", measured as recent results, is a weak predictor once longer-term strength is known. Over 3–7 matches, results-based numbers (points, goals) carry less signal than shot-based numbers. Peer-reviewed Premier League evidence shows no positive momentum, and even some reversal after winning streaks. Recent-trend features add at most small, interval-specific value in ML models.

### Cited Findings
- Premier League fixed-effects study: performance reversal follows winning streaks, with no comparable pattern for streaks of draws or losses, or for in-game goal-scoring. The authors conclude momentum is "better suited as a post hoc label of performance than a robust causal phenomenon." — [Applied Economics 47(4), 2015, "The hot hand fallacy re-examined: new evidence from the English Premier League" [peer-reviewed]](https://www.tandfonline.com/doi/abs/10.1080/00036846.2014.969830) (abstract via search results)
- In-game: no evidence that goal sequences change winning chances, but bettors strongly tend to back the team that has "gained momentum". — [Ötting & Deutscher, "Gambling on Momentum", arXiv 2211.06052](https://arxiv.org/pdf/2211.06052)
- An ML pipeline found recent-trend ("momentum") features predicted soccer outcomes better than short-window averages only for some intervals (best at windows of 6–7 games, with value mainly over short spans of 3–4). — [MDPI Data 9(2):29, 2024 [peer-reviewed, small effect]](https://www.mdpi.com/2306-5729/9/2/29)
- Early points (3 / 5 / 7 matches) correlate only 0.41 / 0.51 / 0.58 with rest-of-season points. The shots-on-target difference over the same window does better (0.52 / 0.58 / 0.63). — [StatPair [company/betting blog]](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)
- Over- or underperformance in the first half of a season shows "virtually no correlation" with the second half. — [Pinnacle [company/betting blog]](https://www.pinnacle.com/betting-resources/en/betting-strategy/regression-to-the-mean-in-sports-betting/ewp2a8kl7mmhuqcm)
- Points are "pretty randomly distributed throughout a season" (Premier League). — [James Grayson [analyst blog]](https://jameswgrayson.wordpress.com/2013/12/30/which-metrics-are-the-most-repeatable-between-the-first-19-and-final-19-games-of-the-season/)
- Pre-match prediction from last-three-match xG: about 55.6% accuracy (Bundesliga). — [PMC12640942 [peer-reviewed]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12640942/)

### Inferences
- A last-6 results line (W/D/L) is about as informative as a 6-match sample of points (r ≈ 0.5 with the future), and it adds little once season-long and previous-season underlying numbers are known. "Form" read from last-6 xG or shots is more useful than form read from results.
- A hot streak of wins with weak underlying numbers should be read as likely to regress, not as momentum.
- Genuine changes (new manager, key injuries or returns, tactical switch) are the legitimate reason to weight recent matches more. The evidence above does not quantify this.

### Gaps
- A cited "2018 PLOS ONE study of 45,000+ matches" on form (mentioned by a betting site) could not be verified.
- No study was found that quantifies the extra predictive value of last-5/6 xG over season xG, controlling for team strength.
- No evidence was found on post-manager-change form persistence (beyond general regression to the mean).

---

## 4. Home/away splits per team: persistent or noise? How many matches are needed?

### Takeaway
Team-specific home advantage beyond the league average is hard to tell apart from noise. Even with about 20+ home matches per team (Champions League, ability-controlled), studies disagree on whether teams differ significantly. In subsets of strong teams, and against weak opponents, no between-team differences were found. With 3–8 home games in a domestic season, a team's home/away split is overwhelmingly noise. The league-level home advantage is the better baseline.

### Cited Findings
- Kuvvetli & Çilengiroğlu (2024): 2,344 Champions League matches, 2003/04–2021/22. 42 teams had at least 40 matches (about 20 home, 20 away). Goal-based HA was estimated with a Poisson GEE controlling for team ability (UEFA ranking):
  - Adjusted HA ranged from 32.1% (Lille) to 79.5% (Sevilla), and 37 of 42 teams had significant HA. Between-team variation was significant (χ² = 88.4 including Lille; χ² = 60.1, p = 0.03 excluding Lille).
  - In a subset of 20 teams, HA ranged from 64.3% to 77.7% with no significant between-team difference.
  - Against weak opponents, there was no significant between-team HA difference (χ² = 8.2, p = 0.94).
  - Away disadvantage varied more (45.1–71.9%; χ² = 179.8, p < 0.001), but only 12 of 42 teams had significant AD.
  - Team HA did not differ between group and knockout stages (p = 0.740).
  — [Journal of Human Kinetics 92 (2024):161–179 [peer-reviewed]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11079936/)
- Goumas: in 13 Champions League teams, once team ability was controlled for, HA did not vary significantly between teams. There was weak evidence of between-team variation in away disadvantage, and significant differences between countries. — [Goumas, "Modelling home advantage for individual teams in UEFA Champions League football", Journal of Sport and Health Science [peer-reviewed]](https://www.sciencedirect.com/science/article/pii/S2095254615001325)
- Long-run domestic team ranges (points-share HA): France 59.2–74.4%, Italy 61.0–71.8%, Portugal 61.0–71.3%, Spain 67.1–72.0% (Pollard & Gómez 2009). Greece 49.6–80.5% (Armatas & Pollard 2014). Brazil 57.5–74.9% (Pollard et al. 2008). — cited in [Kuvvetli & Çilengiroğlu 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11079936/); original [Pollard & Gómez, "Home advantage in football in South-West Europe: long-term trends, regional variation, and team differences"](https://www.researchgate.net/publication/246474757_Home_advantage_in_football_in_South-West_Europe_Long-term_trends_regional_variation_and_team_differences)
- Better teams show home advantage more often, so team ability confounds raw home/away splits. — [search summary of the South-West Europe literature](https://www.researchgate.net/publication/246474757_Home_advantage_in_football_in_South-West_Europe_Long-term_trends_regional_variation_and_team_differences)
- Points-share HA can mislead as a team metric: a team that earns equal points at home and away scores 50%, and the measure mixes ability with venue effects. — [PMC4415821, "Validity of the Established Method of Quantifying Home Advantage in Soccer" [peer-reviewed]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4415821/)
- Supporting evidence on single-season stability: within one season, goals-conceded averages reach only r ≈ 0.41–0.43 even after 7–15 total matches (of which only about half are at home). — [StatPair](https://statpair.com/blog/early-season-football-stats-signal-vs-noise-data-study)

### Inferences
- If even the full-season goals-conceded rank is weak (r ≈ 0.4 after 15 matches), then "goals conceded at home over 3 home matches" (or "seasonConcededAVG_home" early in a season) is close to pure noise. A home/away split over the last 6 venue-specific matches (which spans many months) is also very noisy.
- Unless there is a structural reason (altitude, extreme travel, artificial pitch, a very different stadium), the most defensible prior is: the team's overall strength plus the league's average home advantage. Team-specific deviations should be heavily shrunk.
- Home splits are better read through shots or xG at home vs away than through goals or points.

### Gaps
- No domestic-league study was found giving a split-half or year-to-year correlation for team-specific home advantage, or a "number of home matches needed".
- No study was found isolating artificial-pitch effects in European leagues.

---

## 5. Home advantage: size by league, trend, the COVID natural experiment, causes, team and stadium effects

### Takeaway
Men's domestic home advantage, measured as the share of points won at home, typically runs about 53–65% across countries. Southern and Eastern European leagues (Spain, Turkey, Greece) tend to be higher than England, Germany and France. Home advantage has declined over decades, with English home win rates falling from above 60% historically to about 40–41% recently. COVID ghost games roughly halved it (home edge +0.39 → +0.22 points per game; +0.29 → +0.15 goals per game), pointing to crowd influence, partly through referee decisions (fewer away yellow cards) and partly through home attacking output. Cross-league differences are partly explained by travel distance, altitude and governance factors (43% of variance explained across 157 leagues).

### Cited Findings
**COVID ghost games:**
- McCarrick (Univ. of Leeds), Wolfson (Northumbria) et al. (2021): about 4,844–5,000 matches, 15 leagues in 11 countries, including Premier League, Championship, Bundesliga, 2. Bundesliga, La Liga, Segunda, Serie A, Serie B, plus Portugal, Greece, Turkey, Austria, Denmark, Russia and Switzerland. Data from Football-Data.co.uk and FiveThirtyEight.
  - Home minus away points per game: +0.39 with fans vs +0.22 without.
  - Home minus away goals per game: +0.29 vs +0.15.
  - Without fans, home teams had 0.7 fewer corners, 1.3 fewer shot attempts and 0.4 fewer shots on target per game, while away teams gained 0.10 corners, 0.17 shots and 0.20 shots on target.
  - Away teams got far fewer yellow cards. After adjusting for dominance, the referee associations weakened, and for red cards they became non-significant.
  - No per-league breakdown in the press release. — [Northumbria University press release, 17 Aug 2021](https://newsroom.northumbria.ac.uk/pressreleases/football-without-the-fans-new-study-reveals-effect-of-empty-stadiums-during-pandemic-3121743); [Psychology of Sport and Exercise 2021 abstract [peer-reviewed]](https://www.sciencedirect.com/science/article/abs/pii/S146902922100131X); [New Atlas summary](https://newatlas.com/sports/empty-stadiums-football-sport-home-ground-advantage-covid)
- Bryson, Dolton, Reade, Schreyer & Singleton (2021) used matches behind closed doors in several countries in 2019/20 as a natural experiment. They found large, significant effects on yellow cards: without a crowd, away teams received fewer cards, which reduced home advantage. — [Economics Letters 198 (2021) 109664 [peer-reviewed]](https://discovery-pp.ucl.ac.uk/id/eprint/10115454/1/Bryson%20et%20al%202020%20Econ%20Letters.pdf); [IZA DP 13578](https://www.iza.org/publications/dp/13578)
- Other COVID analyses: a Bayesian prediction study of the changed home advantage in spectator-free matches ([PMC8947042](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8947042/)), "Home advantage of European major football leagues under COVID-19 pandemic" ([arXiv 2101.00457](https://arxiv.org/pdf/2101.00457)), and a Bundesliga before/during/after analysis ([Pith summary of arXiv 2411.12509](https://pith.science/paper/2411.12509)). Their exact figures were not retrieved; see Gaps.

**Size by league / country:**
- Pollard & Gómez (2009), South-West Europe, points-share HA: Spain 69.9%, France 66.9%, Portugal 65.8%, Italy 65.2% (long-term averages). — cited in [Kuvvetli & Çilengiroğlu 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11079936/)
- Pollard & Gómez (2014a): men's league HA ranged from 52.8% to 65.2% across the countries studied (women's leagues averaged 54.2% vs 60% for men). Pollard & Gómez (2014b), 157 national leagues: the highest was Nigeria at 86.8%. FIFA ranking, maximum travel distance, high altitude, civil conflict and a corruption index together explained 43% of cross-league variation. Ramchandani et al. (2021): English leagues 58–61%. — cited in [Kuvvetli & Çilengiroğlu 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11079936/)
- Club Elo per-country home-field-advantage values seen on clubelo.com in Oct 2026, in Elo points: Spain 65, Turkey 65, Norway 59, Czech Republic 54, Netherlands 51, Russia 47, Germany 46, Italy 45, England 39, France 36 (South America higher: Colombia 85, Brazil 76). The values look per-country and dynamic; the page does not explain them. — [clubelo.com](http://clubelo.com/System)
- Recent points-share figures, 2025/26 (betting-adjacent source, lower weight): La Liga ~62.7%, Ligue 1 >60%, Eredivisie ~60%, Bundesliga 57.08%, Serie A ~53%. — [Win Sports Online [company/betting blog]](https://www.winsportsonline.com/research/football/home-as-a-fortress-how-much-does-home-advantage-still-matter-in-europes-top-7-leagues/)
- Süper Lig 2015–16: about 61% of points won at home. — [Leite, Athens Journal of Sports 2017](https://www.athensjournals.gr/sports/2017-4-1-4-Leite.pdf)
- Bundesliga points share 58.35% (older analysis). — [Barça Innovation Hub](https://barcainnovationhub.fcbarcelona.com/blog/the-advantage-of-playing-at-home/)
- Home win rate by league (season not stated): Eredivisie ~46.7%, Süper Lig ~46.3%, Bundesliga ~41%. — [TheDatabetics [company/betting blog]](https://thedatabetics.com/insights/football-leagues-home-advantage/)

**Trend over time:**
- English professional football, 1974–2018: home advantage declined significantly in all leagues. The decline is secular and does not appear tied to technology such as referee monitoring. — [De Economist, "Seasonal Home Advantage in English Professional Football; 1974–2018" [peer-reviewed]](https://link.springer.com/article/10.1007/s10645-020-09372-z)
- Across all four English tiers, home teams won 64.6% of matches at the 1895/96 peak, and 2015/16 set a record low of 41.0%. — [Sky Sports [journalism]](https://www.skysports.com/football/news/11096/10955089/sky-sports-bust-common-football-myths-home-advantage); [Sky Sports, "Home advantage is on the wane in the Premier League"](https://www.skysports.com/football/news/11095/13511444/home-advantage-is-on-the-wane-in-the-premier-league-between-the-lines)
- All four English tiers started with home win rates above 50% and now sit close to 40%. Away win rates are consistently above 30% and trending upward. Suggested (untested) causes: standardised pitches, better travel and accommodation, tactical and data analysis, fitness. — [Sean Elvidge, "Waning Home Advantage in English League Football" (2025) [analyst blog]](https://seanelvidge.com/articles/2025/Home_advantage_in_English_football/)
- Press release: "Covid-19 and VAR decimate 'home advantage' in football leagues across Europe" (figures not retrieved). — [LCP press release](https://www.lcp.com/en/media-centre/press-releases/covid-19-and-var-decimate-home-advantage-in-football-leagues-across-europe)

**Causes and team/stadium effects:**
- Crowd: ghost-game evidence (above) shows the home edge roughly halved. The mechanisms are fewer home attacking actions (shots −1.3 per game) and less referee bias against away teams (yellow cards), with part of the referee effect explained by dominance. — [McCarrick et al. 2021](https://newsroom.northumbria.ac.uk/pressreleases/football-without-the-fans-new-study-reveals-effect-of-empty-stadiums-during-pandemic-3121743); [Bryson et al. 2021](https://discovery-pp.ucl.ac.uk/id/eprint/10115454/1/Bryson%20et%20al%202020%20Econ%20Letters.pdf)
- Travel distance and altitude are significant cross-league predictors (Pollard & Gómez 2014b). Champions League matches 2008–2016: home advantage increased at higher altitude (Van Damme & Stijn 2019). — cited in [Kuvvetli & Çilengiroğlu 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11079936/)
- Team-specific persistence: see Q4. The evidence is mixed and ability-confounded.

### Inferences
- Converting the Club Elo HFA values with the logistic formula (W_e = 1/(1+10^(−d/400))) gives an expected score for an equal-strength home team of about 55% (England, d = 39; France, d = 36), about 57% (Germany, d = 46) and about 59% (Spain or Turkey, d = 65). This is my calculation, not a source figure.
- Pre-COVID, a typical home edge was about +0.4 points and +0.3 goals per game for evenly matched teams (pooled across the McCarrick leagues). That is meaningful but much smaller than the difference between a strong and a weak team. A home win is therefore not a default for evenly matched teams.
- Because home advantage has declined over decades and differs by league, use a recent league-specific baseline (e.g. the last 2–3 seasons) rather than old textbook values.
- Team-specific "fortress" narratives should require structural support (altitude, unusual travel, artificial pitch) and large multi-season samples.

### Gaps
- No consistent, single-method league-by-league table was found for the second tiers listed (Championship, 2. Bundesliga, Segunda, Serie B, Ligue 2) or for the Süper Lig in recent seasons. McCarrick et al. included several of these leagues but the per-league numbers were not retrieved.
- Two figures appeared in search summaries without a clearly attributable source and are left out of the findings:
  - Points edge falling from 0.48 to 0.10 per game, with away goals rising from 1.19 to 1.38, in a "five-league analysis".
  - The Bundesliga's first ghost-game period cutting home win probability by 13 percentage points.
- A reported 23-league study finding "no effect of closed doors on final match outcomes" could not be traced. Wunderlich et al. (PLOS ONE 2021, "home advantage remains…") was not fetched. Not all COVID studies agree on the size of the drop.
- No effect-size numbers were found for artificial turf, stadium relocation or familiarity in European leagues.
- The Club Elo HFA values come from a results page snapshot. The update rule for these values was not documented in what was retrieved.
