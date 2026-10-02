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
   **Taugt das xG einer ganzen Liga nicht** – Gesamt-xG geteilt durch Gesamt-Tore unter
   `LIGA_XG_MIN` (0,65) –, entfallen `XG_ANTEIL` und `LIGA_BASIS_XG` **für diese Liga**: Es
   wird nur mit Toren gerechnet, für jedes Team, auch für die mit gefüllt aussehendem Feld.
   Der Defekt sitzt in der Erhebung der Liga, nicht im einzelnen Team. Zwischen 0,65 und 0,85
   wird nicht eingegriffen, die Ausgabe weist nur darauf hin. Eingebaut am 02.10.2026.
   **Fehlt das xG-Feld eines Teams** (0,00 bei erzielten Toren – FootyStats erhebt xG nicht in
   jeder Liga und füllt es teils erst nachträglich), zählen für diesen Term nur die Tore, und
   das Team wird beim Liga-xG-Mittel ausgelassen. Ohne das las das Modell ein leeres Feld als
   „erspielt keine Chancen": Ein Team mit Liga-Durchschnitt bekam Angriffsstärke 0,30 statt
   1,01, und die Nullen zogen zusätzlich den Liga-Nenner um 15 % nach unten, was die Stärke
   **aller** Teams derselben Liga um 17 % aufblähte. Eingebaut am 30.09.2026.
4. **Direkte Duelle** verschieben die Gesamttore um 10 %, wenn das letzte Duell höchstens 3 Jahre alt ist.
5. **Vorab-Quoten** (optional, `--markt 0.3`): margenbereinigt in erwartete Tore umgerechnet und beigemischt.
   Standard ist 0 – reines Datenmodell.
6. **Poisson mit Dixon-Coles-Korrektur** (rho = −0,07) ergibt die Ergebnis-Matrix 0:0 bis 10:10;
   daraus Heim/Remis/Auswärts, Über/Unter 2,5, Beide treffen und die Top-3-Ergebnisse.
7. **Faire Quote** = 1 / Wahrscheinlichkeit.
8. **Bester Tipp** = die wahrscheinlichste der fünf Wetten. Liegen mehrere weniger als
   `GLEICHSTAND_PUNKTE` (2,0) auseinander, entscheidet unter diesen die **kleinste
   Empfindlichkeit**: um wie viele Punkte sich die Wette verschiebt, wenn beide erwarteten
   Tore um `EMPF_STOERUNG` (10 %) falsch sind. Der Preis entscheidet weiterhin nicht mit.
   Eingebaut am 02.10.2026 – verändert keine Wahrscheinlichkeit, nur die Auswahl.

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

### Gleichstand-Entscheid bei der Tipp-Auswahl

Die fünf Wetten reagieren sehr unterschiedlich auf einen Fehler in den erwarteten Toren.
Gemessen an 32 Spielen aus fünf Ligen, 10 % Fehler auf beide λ:

| Wette | Bewegung |
|---|---|
| Über 2,5 / Unter 2,5 | **6,22 Punkte** |
| Beide treffen | **4,73 Punkte** |
| Sieg Heim | 1,01 Punkte |
| Sieg Auswärts | 0,54 Punkte |

Über/Unter 2,5 liest die **Summe** der erwarteten Tore direkt ab, Sieg Heim und Sieg Auswärts
hängen an der **Differenz** und kaum am Niveau. Die Regel „höchste Wahrscheinlichkeit" wählte
deshalb 30 von 32 Tipps aus den drei empfindlichsten Zeilen.

Seit 02.10.2026 gilt: Liegen mehrere Wetten unter 2 Punkten auseinander, gewinnt die
unempfindlichste. Darüber bleibt es bei der höchsten Wahrscheinlichkeit, und der Preis
entscheidet in keinem Fall mit.

| | Wahrscheinlichkeit | Abstand zum Markt |
|---|---|---|
| vorher | 61,07 % | 4,14 Punkte |
| **jetzt** | **60,93 %** | **4,01 Punkte** |

Gegengeprüft an 114 zwischengespeicherten Spielen: **Wahrscheinlichkeiten überall auf 1e-12
identisch** (die Rechnung ist unberührt), 31 Spiele mit Gleichstand (27 %), **10 Tipps
gewechselt** (9 %), mittlere Kosten 0,81 Punkte Wahrscheinlichkeit. Zwei Alternativen, die
auch außerhalb des Gleichstands eingreifen, wurden gemessen und verworfen: Normierung auf den
Liga-Schnitt kostet 11,4 Punkte Wahrscheinlichkeit bei 5,04 Marktabstand, Abweichung je Punkt
Empfindlichkeit 16,8 Punkte bei 4,92.

### Liga-Test für das xG

FootyStats erhebt xG nicht in jeder Liga gleich sorgfältig. Punkt 12 in
`SOLLBRUCHSTELLEN.md` fing bisher nur das **einzelne Team** mit glatt null xG ab. Das ist zu
eng: In Saison 17308 hatten 18 von 48 Teams unbrauchbares xG, davon 7 glatt null (erkannt)
und 11 mit Werten wie 0,02 xG bei 1,25 Toren (nicht erkannt) – die Angriffsstärke lag dort
bis zu 182 % zu niedrig.

Der Liga-Test vergleicht **Gesamt-xG gegen Gesamt-Tore** der Saison, über alle Teams, mit
Spielen gewichtet. Ein ehrlich erhobenes xG liegt dicht an den Toren. Gemessen am 02.10.2026
an 29 Ligen:

| Bereich | Ligen | |
|---|---|---|
| 0,89 – 1,34 | 20 | unauffällig |
| 0,89 / 0,76 | 2 | Hinweis, keine Änderung |
| **0,54 / 0,52** | 2 | xG wird verworfen |

Zwischen 0,54 und 0,76 liegt eine deutliche Lücke; die Grenze liegt in ihrer Mitte. Die zwei
verworfenen sind Saison 17308 (die Liga mit den 18 Teams) und 16808 (Nations League, ohnehin
gesperrt). Der Test **kostet keine zusätzliche API-Abfrage** – die Werte stehen in der
`league-teams`-Antwort, die das Modell ohnehin holt.

**Gegengeprüft an 114 zwischengespeicherten Spielen:** 113 völlig unverändert (99,1 %), ein
einziges verändert – Wohlen – Schötz aus Saison 17308, wo der Tipp von „Beide treffen" auf
„Über 2,5" wechselt.

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
| `GLEICHSTAND_PUNKTE` | 2,0 | darunter entscheidet die Empfindlichkeit, nicht die Wahrscheinlichkeit |
| `EMPF_STOERUNG` | 0,10 | λ-Fehler, an dem die Empfindlichkeit gemessen wird |
| `LIGA_XG_MIN` | 0,65 | darunter rechnet die ganze Liga nur mit Toren |
| `LIGA_XG_WARN` | 0,85 | darunter nur ein Hinweis in der Ausgabe |
| `MARKT_ANTEIL` | 0,0 | Vorab-Quoten standardmäßig aus |
| `MIN_SAISONSPIELE` | 3 | darunter keine Prognose (Sperre) |
| `FENSTER_MIN_SPIELE` | 10 | darunter wird die Saison mit den letzten 10 Spielen aufgefüllt |
| `CACHE_STUNDEN` | 6 | danach werden API-Daten neu geladen |

Diese Werte sind **nach Erfahrung gesetzt und nicht an vergangenen Spielen optimiert** – so gewollt.
Sie bleiben fest, damit jede Analyse vergleichbar ist. Nur auf ausdrücklichen Wunsch ändern,
Begründung im Code danebenschreiben und diese Tabelle nachziehen.
Nicht nachträglich an einzelne Spielausgänge anpassen.
