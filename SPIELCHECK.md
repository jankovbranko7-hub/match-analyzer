# Spielcheck (System A · Arbeitsweise, nicht Teil des Systems)

Eigenes Prüfverfahren des Nutzers, getrennt vom OddAlerts-System v1.3-OA und vom
Forebet-Check (System B, `FOREBET-CHECK.md`); beide werden nicht vermischt. Vereinbart am
06.11.2026. Ändert nichts am System, an Vorabeinträgen oder Auswertungen.

## Auslöser

Der Nutzer schreibt:

> **Spielcheck: [Heimteam] – [Auswärtsteam]** (auch mehrere Paarungen auf einmal)

## Was der Nutzer schickt

Der Nutzer schickt je Spiel nur:

1. die **Paarung** (gern mit Datum und Liga),
2. **„How to play it“** von der Odd-Alerts-Seite (Screenshot oder Text; nicht per API erreichbar).

Alles andere holt Claude selbst. Die Copilot-Fragen unten sind nur ein Zusatz, falls der
Nutzer sie doch einmal stellt.

## Was Claude selbst per API holt (Schlüssel `ODDALERTS_KEY`, nie ausgeben)

| Bereich | Endpunkt | Inhalt |
|---|---|---|
| Spiel finden | `fixtures/upcoming?competitions=<id>` | Match-ID, Anstoß (UTC), Tabellenplatz beider Teams |
| Letzte Spiele / Results | `fixtures/between?competitions=<ids>&from=&to=` (max. 365 Tage, paginiert) | Gegner, Ergebnis, Halbzeit, Heim/Auswärts, Wettbewerb |
| Stats letzte 5/10 | `stats/fixture/<id>?last_x=10_overall` (auch `_home`, `_away`, `5_…`) | Tore, Gegentore, BTTS, Over-Linien, Clean Sheets, ohne Tor; wettbewerbsübergreifend (`all_comps: true`) |
| Saison-Stats | `stats/fixture/<id>`, `stats/season/<season_id>` | wie oben, nur Liga der Saison |
| Cards | in `stats/fixture` (`yellow_cards_*`, `red_cards_*`, `cards_over`, je Halbzeit) | Karten für/gegen/gesamt |
| Trends + Odd-Alerts-Modell | `trends/btts`, `trends/over15`, `trends/over25`, `trends/over35`, `trends/under25`, `trends/draw` | alle Spiele der nächsten 5 Tage mit Team-Quoten und Modell: Heim/Remis/Auswärts, BTTS, Over/Under 1,5/2,5/3,5/4,5, Tore je Team |
| Wahrscheinlichster Ausgang | `probability/ft_result`, `probability/btts`, `probability/double_chance`, `probability/ht_result` | nur der jeweils wahrscheinlichste Ausgang pro Spiel |
| Quoten | `odds/history/<id>` | 8 Buchmacher (u. a. Pinnacle, Bet365, Betfair Exchange), Öffnung und aktueller Stand |

Nicht erreichbar: Predictions (Verdict, How to play it, Bet Builder, Avoid), Tabellen
(`standings` → 403), Simulationen, Aufstellungen und Verletzungen.

## Auswertung

1. **Grundlage:** letzte 5 Spiele je Team, alle Pflichtwettbewerbe (Wunsch des Nutzers),
   **ohne Testspiele** („Club Friendlies“, `is_friendly`; vereinbart am 06.11.2026). Zusätzlich
   zur Kontrolle die letzten 10 je Team und die Liga ohne Pokalspiele gegen unterklassige Gegner.
   Copilot zählt Testspiele oft mit und nennt sie „Liga“ — solche Spiele sind echt, aber werden
   ersetzt. Ein Spiel erst „erfunden“ nennen, wenn es auch unter allen Spielen des Zeitraums
   (`fixtures/between` ohne Wettbewerbsfilter) nicht zu finden ist.
2. **Zählen (von 10 Spielen):**
   - Over 2,5 · Under 2,5 · BTTS Ja · BTTS Nein
   - Heimsieg = Siege Heimteam + Niederlagen Auswärtsteam
   - Auswärtssieg = Siege Auswärtsteam + Niederlagen Heimteam
   - Remis = Remis beider Teams
3. **Grenze des Nutzers:** **mindestens 7 von 10** → kommt in Frage; 6 oder weniger → auslassen.
4. **Gegen die Quote prüfen:** nötige Trefferquote = 1 / Quote (1,25 → 80 %, 1,40 → 71 %,
   1,60 → 63 %, 1,80 → 56 %, 2,00 → 50 %). Die Zählung sollte klar darüber liegen.
   Quotenbewegung seit Öffnung erwähnen.
5. **Gegenprobe:** Copilot-Angaben und „How to play it“ gegen die API prüfen
   (häufige Fehler: Heim/Auswärts vertauscht, Pokal als Liga bezeichnet, erfundene oder
   doppelte Spiele, nur „Ja“-Märkte gezählt). „How to play it“ ändert sich beim Neuladen.
6. **Ergebnis je Spiel:** Tipp mit Zählung, Quote, nötiger Trefferquote und Bedenken —
   oder „auslassen“. Keine Kombiwetten. Keine Garantie.

## Fragen für Odd Alerts Copilot (Stand 06.11.2026, falls der Nutzer sie stellt)

1. „Liste die letzten 5 Spiele beider Teams: Gegner, Ergebnis, Heim oder Auswärts, Wettbewerb.“
2. „Zähle in diesen 10 Spielen: Heimsiege des Heimteams, Auswärtssiege des Auswärtsteams, Remis, Over 2,5, BTTS, Spiele ohne eigenes Tor.“
3. „Welcher einzelne Markt wäre in diesen 10 Spielen am häufigsten aufgegangen? Nenne die Anzahl.“
4. „Welche Tatsache im kommenden Spiel könnte dieses Muster brechen? Gegnerstärke, Ausfälle, Wettbewerb?“

Erkenntnisse aus den Tests: Copilot sieht nur 5 Spiele je Team, wiederholt sonst oft
„How to play it“, gibt bei „niedrig/mittel/hoch“ fast immer „mittel“ und liefert bei einer
reinen Rangfolge-Frage im neuen Chat eine fast gleiche Schablone (BTTS, Over, …) — diese
Fragen sind deshalb entfallen.

## Tagesliste

Freigegebene Spiele (ab 7 von 10) kommen je Tag nach `tipps/spielcheck/JJJJ-MM-TT.md`
(Spiel, Markt, Zählung, Quote) und werden dort nach Abpfiff ausgewertet. Getrennt von
`tipps/forebet/` (System B).
