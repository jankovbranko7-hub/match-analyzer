# match-analyzer

Prognosen für einzelne Fußballspiele aus FootyStats-Daten. Regeln für die Analyse stehen in `CLAUDE.md`.

## Rechenmodell: `analyse/modell.py`

```bash
pip install -r requirements.txt
python3 analyse/modell.py --liste 2026-09-26        # Spiele des Tages mit ID
python3 analyse/modell.py 8548331 8548255 8408933   # Prognose für diese Spiele
```

Der API-Key kommt aus der Umgebungsvariable `FOOTYSTATS_API_KEY` (ersatzweise `APIKEY`).
API-Antworten werden in `analyse/daten/` zwischengespeichert (nicht im Git). Sie gelten
`CACHE_STUNDEN` lang und werden danach automatisch neu geladen; `--neu` erzwingt es sofort.

### Rechenweg

1. **Liga-Durchschnitt** der Saison: Tore und xG pro Spiel, getrennt nach Heim und Auswärts.
2. **Angriffs- und Abwehrstärke** je Team relativ zum Liga-Durchschnitt (1,00 = Durchschnitt):
   70 % xG, 30 % Tore; Heim- bzw. Auswärtswerte mit den Gesamtwerten gemischt
   (Gewicht Heim/Auswärts = Spiele / (Spiele + 6)); kleine Stichproben Richtung 1,00 gezogen;
   Form der letzten 6 Spiele mit 25 %.
3. **Erwartete Tore** = Liga-Basis (60 % Tore, 40 % xG) × eigener Angriff × Abwehr des Gegners.
4. **Direkte Duelle** verschieben die Gesamttore um 10 %, wenn das letzte Duell höchstens 3 Jahre alt ist.
5. **Vorab-Quoten** (optional, `--markt 0.3`): margenbereinigt in erwartete Tore umgerechnet und beigemischt.
   Standard ist 0 – reines Datenmodell.
6. **Poisson mit Dixon-Coles-Korrektur** (rho = −0,07) ergibt die Ergebnis-Matrix 0:0 bis 10:10;
   daraus Heim/Remis/Auswärts, Über/Unter 2,5, Beide treffen und die Top-3-Ergebnisse.
7. **Faire Quote** = 1 / Wahrscheinlichkeit.

### Bilanz führen

```bash
python3 analyse/bilanz.py --merken 8549906 8549907   # Prognosen speichern
python3 analyse/bilanz.py --auswerten                # Ergebnisse holen, Bilanz ziehen
```

`analyse/bilanz.json` liegt im Git und sammelt jede Prognose. Die Auswertung vergleicht
Trefferquote, Kalibrierung und Geld-Saldo mit dem, was das Modell vorhergesagt hat, und prüft
per z-Test, ob eine Abweichung echt ist oder Zufall. Erst ab rund 190 Spielen ist eine
Verzerrung von 10 Prozentpunkten überhaupt nachweisbar.

### Grenzen

Die bekannten Schwachstellen stehen vollständig in [`SOLLBRUCHSTELLEN.md`](SOLLBRUCHSTELLEN.md).
Kurzfassung:

Das Modell ist für **Ligen** gebaut, in denen alle Teams gegen dieselben Gegner spielen.
Hat ein Team weniger als `MIN_SAISONSPIELE` Spiele, verweigert das Skript die Prognose,
weil die Dämpfung die Teamstärke dann durch den Liga-Durchschnitt ersetzt (`--trotzdem` erzwingt
die Ausgabe, taugt aber nicht als Tipp).

Für **Länderspiele ist das Modell ungeeignet**, auch bei ausreichender Spielzahl: Es vergleicht
rohe Form-Durchschnitte ohne Korrektur für die Stärke der Gegner. Am 26.09.2026 wich es bei zehn
Länderspielen im Schnitt 17 Prozentpunkte vom Markt ab und gab für San Marino gegen Finnland
35 % Heimsieg aus (Markt: 3 %).

### Gewichte

Alle Gewichte stehen als Konstanten oben in `analyse/modell.py`:

| Konstante | Wert | Bedeutung |
|---|---|---|
| `XG_ANTEIL` | 0,70 | xG gegen echte Tore bei der Teamstärke |
| `LIGA_BASIS_XG` | 0,40 | Liga-Basis: 60 % Tore, 40 % xG |
| `SEITE_K` | 6 | Heim-/Auswärtsbilanz gegen Gesamtwerte: n / (n + 6) |
| `DAEMPFUNG_K` | 5 | Saisonstärke Richtung 1,00, wie 5 Spiele auf Liga-Niveau |
| `FORM_ANTEIL` | 0,25 | Anteil der letzten 6 Spiele |
| `FORM_DAEMPFUNG_K` | 3 | Dämpfung der Formwerte |
| `H2H_ANTEIL` | 0,10 | Direkte Duelle auf die Gesamttore |
| `H2H_MAX_JAHRE` | 3 | Ältere Duelle zählen gar nicht |
| `H2H_DAEMPFUNG_K` | 3 | Gewicht der Duelle wächst mit ihrer Zahl: n/(n+3) |
| `DIXON_COLES_RHO` | −0,07 | Korrektur für 0:0/1:0/0:1/1:1 |
| `MARKT_ANTEIL` | 0,0 | Vorab-Quoten standardmäßig aus |
| `MIN_SAISONSPIELE` | 3 | darunter keine Prognose (Sperre) |
| `CACHE_STUNDEN` | 6 | danach werden API-Daten neu geladen |

Diese Werte sind **nach Erfahrung gesetzt und nicht an vergangenen Spielen optimiert** – so gewollt.
Sie bleiben fest, damit jede Analyse vergleichbar ist. Nur auf ausdrücklichen Wunsch ändern,
Begründung im Code danebenschreiben und diese Tabelle nachziehen.
Nicht nachträglich an einzelne Spielausgänge anpassen.

## Live-Filter: `analyse/live.py`

Prüft einen Alarm aus der Live-App, bevor gewettet wird. Die Wette ist immer „noch ein Tor“
(Über aktueller Stand + 0,5). Alle Bedingungen müssen für **dasselbe** Team gelten:

| Regel | Schwelle |
|---|---|
| Minute | 55–75 |
| Pressure Recent % des Druck-Teams | ≥ 65 |
| Schüsse aufs Tor Druck-Team / Gegner | ≥ 5 / ≤ 2 |
| Anteil an den Dangerous Attacks | ≥ 60 % |
| Saison-Tore pro Spiel des Druck-Teams | ≥ 1,4 |
| Rote Karte Druck-Team | keine |
| Spielstand aus Sicht des Druck-Teams | führt nicht |
| Live-Quote | ≥ faire Quote × 1,05 |

Faire Quote: Poisson mit der Torrate der 2. Halbzeit (Liga-Schnitt × 0,55 über 50 Minuten),
über die Restzeit bis zur 95. Minute, **ohne Aufschlag für Druck** – laufende Schussdaten
verbessern die Prognose über die Marktquote hinaus kaum (arXiv 2605.16066).

Mit Studien belegt: Spielstand-Regel, Rote Karte, fehlender Druck-Aufschlag, 55 % der Tore in
der 2. Halbzeit (Quellen als Kommentar in `analyse/live.py`). **Nicht belegt**, weil GoalSpy die
Berechnung von „Recent Pressure“ nicht veröffentlicht und es zu Dangerous Attacks keine Studien
gibt: Minute, Druck ≥ 65 %, Schüsse aufs Tor, Dangerous Attacks, Tore-Schnitt. Diese Schwellen
sind Erfahrungswerte und lassen sich nur über die festgehaltenen Alarme messen.

```bash
python3 analyse/live.py --spiel "A – B" --minute 62 --stand 1:1 --druck heim \
    --druck-prozent 68 --sot 6:1 --da 45:24 --schnitt 1.6 --quote 1.55 --merken
python3 analyse/live.py --ergebnis 1 ja     # nach dem Spiel
python3 analyse/live.py --auswerten
```

### Einstellung in GoalSpy (Alerts → Signals)

Drei Signale, gleiche Regeln, nur Zeitfenster und Mindestquote verschieden. Die Mindestquote gilt
für das **Ende** des Fensters (dort ist sie am höchsten) – so ist sie im ganzen Fenster fair.

| Regel | Wert | Team |
|---|---|---|
| Match Time | 55–61 / 62–68 / 69–75 | – |
| Recent Pressure % | ≥ 65 | Any team |
| Shots on Target | ≥ 5 | Any team |
| Shots on Target | ≤ 7 | Combined |
| Dangerous Attacks | ≥ 40 | Any team |
| Red Cards | ≤ 0 | Combined |
| Trends: Goals scored (avg) | ≥ 1.4 | Any team |
| Trends: Total goals (avg) | ≥ 2.7 | Both teams |
| Live Odds: Over, 1 more goal, Full match | ≥ 1.65 / 1.90 / 2.34 | – |

Die App kann nicht prüfen, ob Druck, Schüsse und Tore-Schnitt vom selben Team kommen, und
nicht, wer führt. Das bleibt der Blick aufs Spiel (oder `analyse/live.py`).
