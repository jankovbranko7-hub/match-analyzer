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
8. **Bester Tipp** = höchste Wahrscheinlichkeit der fünf Wetten. Liegen mehrere innerhalb von
   zwei Prozentpunkten, entscheidet die **Robustheit**: Für jede Wette wird gemessen, um wie
   viele Punkte ihre Wahrscheinlichkeit schwankt, wenn beide erwarteten Tore um 10 % daneben
   liegen (vier Ecken: je 10 % hoch und runter). Die kleinste Schwankung gewinnt. Zahlen in
   der Ausgabezeile `Schwankung bei 10 % Fehler`.

   Hintergrund: „Beide treffen" ist das Produkt zweier abgeflachter Kurven und schwankt um
   rund 10 Punkte, „Über/Unter 2,5" sitzt am steilsten Punkt der Verteilung und schwankt um
   13. Eine fehlertolerante Wette hat damit auch die verlässlichere faire Quote. Nur im
   Zwei-Punkte-Fenster, weil Robustheit sonst die unwahrscheinlichsten Wetten belohnt – als
   alleiniges Kriterium hätte sie an 76 Spielen 28,9 Prozentpunkte Wahrscheinlichkeit
   gekostet. Im Fenster ändert sie den Tipp bei 8 % der Spiele: −0,97 Punkte
   Wahrscheinlichkeit, +2,51 Punkte weniger Schwankung. Eingebaut am 30.09.2026.

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

### Modellstände zum Zurückgreifen

Jede Fassung des Rechenwegs bleibt dauerhaft abrufbar. Tags lassen sich aus der
Cloud-Sitzung nicht auf den Server schieben, deshalb stehen hier die Commit-Kennungen –
die gelten unbegrenzt.

| Stand | Commit | Was drin ist |
|---|---|---|
| **v1 – reine Erfahrungswerte** | `d912a1c` | xG 0,70 / Tore 0,30, ohne Datenfenster. Die 25 Prognosen in `bilanz.json` sind damit entstanden. |
| **v2 – mit Datenfenster** | `605fab4` | wie v1, plus `FENSTER_MIN_SPIELE = 10`. Ab zehn Saisonspielen identisch mit v1. |

```
git checkout d912a1c -- analyse/modell.py     # zurück auf v1
git checkout 605fab4 -- analyse/modell.py     # zurück auf v2
git diff d912a1c 605fab4 -- analyse/modell.py    # Unterschied ansehen
```

Die Gewichte selbst sind in beiden Fassungen dieselben. v2 ändert nur, **aus welchem
Zeitraum** die Teamzahlen stammen, wenn die Saison jünger als zehn Spiele ist.

### Datenfenster bei junger Saison

Hat ein Team weniger als `FENSTER_MIN_SPIELE` Saisonspiele, wird seine Statistik mit den
**letzten 10 Spielen** aufgefüllt. Die laufende Saison bekommt das Gewicht `n / 10`, das
rollende Fenster den Rest – bei 3 Saisonspielen also 30 % Saison und 70 % Fenster.
Die Spielzahl wird dabei auf die des Fensters gehoben, weil die Werte danach auf 10 Spielen
stehen und die Dämpfung sonst weiter so glätten würde, als lägen nur drei vor.

Die Daten kommen aus dem `lastx`-Block, den das Skript für die Form ohnehin holt – das
**kostet keine zusätzliche API-Abfrage**. Ab 10 Saisonspielen passiert nichts mehr, reife
Ligen rechnen unverändert wie vorher.

Das Fenster läuft über die Saisongrenze und über Pokalspiele. Es ist die dreifache
Datenmenge, aber nicht dieselbe Grundgesamtheit wie die Liga-Werte, gegen die normiert wird.
Gemessen an vier Spielen mit Vorab-Quoten hat es den Abstand zum Markt **nicht verkleinert**
(siehe `SOLLBRUCHSTELLEN.md`, Punkt 10).

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
| `FENSTER_MIN_SPIELE` | 10 | darunter wird die Saison mit den letzten 10 Spielen aufgefüllt |
| `CACHE_STUNDEN` | 6 | danach werden API-Daten neu geladen |

Diese Werte sind **nach Erfahrung gesetzt und nicht an vergangenen Spielen optimiert** – so gewollt.
Sie bleiben fest, damit jede Analyse vergleichbar ist. Nur auf ausdrücklichen Wunsch ändern,
Begründung im Code danebenschreiben und diese Tabelle nachziehen.
Nicht nachträglich an einzelne Spielausgänge anpassen.
