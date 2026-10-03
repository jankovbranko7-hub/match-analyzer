# match-analyzer

Prognosen für einzelne Fußballspiele aus FootyStats-Daten. Regeln für die Analyse stehen in `CLAUDE.md`.

## Rechenmodell: `analyse/modell.py`

```bash
pip install -r requirements.txt
python3 analyse/modell.py --liste 2026-09-26        # Spiele des Tages mit ID
python3 analyse/modell.py 8548331 8548255 8408933   # Prognose für diese Spiele
python3 analyse/rueckschau.py                       # Modell gegen echte Ergebnisse prüfen
python3 analyse/finde.py 2026-10-02 "Eldense - Oviedo" "Helmond - Heracles"   # IDs aus Paarungen
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
   `LIGA_XG_MIN` (0,85) –, entfallen `XG_ANTEIL` und `LIGA_BASIS_XG` **für diese Liga**: Es
   wird nur mit Toren gerechnet, für jedes Team, auch für die mit gefüllt aussehendem Feld.
   Der Defekt sitzt in der Erhebung der Liga, nicht im einzelnen Team. Zwischen 0,85 und 0,95
   wird nicht eingegriffen, die Ausgabe weist nur darauf hin. Eingebaut am 02.10.2026,
   Grenze am selben Tag an echten Ergebnissen von 0,65 auf 0,85 korrigiert.
   **Liegt das Liga-xG mehr als 15 % ÜBER den Liga-Toren** (`LIGA_XG_MAX` = 1,15), fällt nur
   `LIGA_BASIS_XG` weg – die Teamstärken sind Verhältnisse und gegen eine gleichmäßige
   Verzerrung immun, die Torbasis nicht.
   **Fehlt das xG-Feld eines Teams** (0,00 bei erzielten Toren – FootyStats erhebt xG nicht in
   jeder Liga und füllt es teils erst nachträglich), zählen für diesen Term nur die Tore, und
   das Team wird beim Liga-xG-Mittel ausgelassen. Ohne das las das Modell ein leeres Feld als
   „erspielt keine Chancen": Ein Team mit Liga-Durchschnitt bekam Angriffsstärke 0,30 statt
   1,01, und die Nullen zogen zusätzlich den Liga-Nenner um 15 % nach unten, was die Stärke
   **aller** Teams derselben Liga um 17 % aufblähte. Eingebaut am 30.09.2026.
4. **Direkte Duelle** verschieben die Gesamttore um 10 %, wenn das letzte Duell höchstens 3 Jahre alt ist.
4b. **Spreizung dämpfen:** `λ' = Liga-Basis + LAMBDA_DAEMPFUNG · (λ − Liga-Basis)`.
   Steht auf **1,00, also aus.** Am 02.10.2026 mit 0,85 eingebaut (die Spreizung lag gegen
   den Markt bei 0,81 bis 0,88, t bis −3,5) und am selben Tag zurückgenommen: der
   Walk-forward über 2136 Spiele gegen echte Ergebnisse bevorzugt 1,00.
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

### Spiel-IDs aus Paarungen: `analyse/finde.py`

```bash
python3 analyse/finde.py 2026-10-02 "CD Eldense - Real Oviedo" "Helmond - Heracles"
python3 analyse/finde.py 2026-10-02 --liste          # alle Spiele des Tages

python3 analyse/finde.py --text <<'ENDE'             # so, wie der Nutzer schreibt
02.10.
1. Eldense - Oviedo
2. Helmond - Heracles
- Dundalk – Bohemians
ENDE
```

`--text` liest den Block, wie er in der Nachricht steht: **Datum oben, darunter je Zeile ein
Spiel.** Erkannt werden `2026-10-02`, `02.10.2026`, `02.10.` und `02/10/2026` – ohne Jahr das
laufende. Nummerierung (`1.`, `2)`), Aufzählungszeichen (`-`, `*`, `•`) und Leerzeilen fallen
weg. Fehlt das Datum oder fehlen die Paarungen, bricht es ab statt zu raten.

Der Nutzer schickt Paarung und Datum, **keine Liga** – die steht in den Spieldaten selbst.
Das Skript löst die Namen auf und erledigt dabei Durchgang 0 aus `CLAUDE.md`:

- **Beide Namen müssen passen**, nicht einer. Bleiben mehrere Spiele übrig, meldet es
  `MEHRDEUTIG` und wählt nicht; findet es nichts, steht `NICHT GEFUNDEN` – nie ein geratenes
  Spiel. Der Fehler vom 30.09.2026 („Atlético El Vigía" auf „Atlético Ávila") wird damit
  abgewiesen statt falsch zugeordnet.
- Toleriert Schreibweisen: „Helmond" findet „Helmond Sport", Akzente und Vereinszusätze
  (FC, CD, SV …) fallen weg, Trennzeichen `-`, `–`, `vs`, `gegen` werden erkannt. „II", „B"
  und „Women" bleiben stehen, weil sie Mannschaften unterscheiden.
- Markiert **schon angepfiffen** (Durchgang 0, Punkt 1), **steht schon in `bilanz.json`**
  (Punkt 3) und **Länderspiel** – und nimmt diese Spiele aus der Vorschlagszeile heraus,
  benennt sie aber, damit nichts stillschweigend wegfällt (Punkt 4).
- Findet sich eine Paarung am genannten Tag nicht, werden Vor- und Folgetag mitgesucht –
  der Tag der API ist nicht UTC-genau (`SOLLBRUCHSTELLEN.md`, Punkt 21).

### Rückschau gegen echte Ergebnisse: `analyse/rueckschau.py`

```bash
python3 analyse/rueckschau.py                                  # Kalibrierung über alle Ligen
python3 analyse/rueckschau.py --konstante XG_ANTEIL --werte 0.5 0.6 0.7 0.8 --haelften
python3 analyse/rueckschau.py --ligen 16540 15066               # weitere Ligen dazuholen
```

Walk-forward: Für jedes Spiel werden die Teamdaten **ausschließlich aus Spielen davor**
gerechnet (Tore und Per-Spiel-xG aus `league-matches`, ein Aufruf je Liga). Bewertet werden
nur Spiele, bei denen beide Teams schon 10 Vorspiele haben – damit ist das Datenfenster aus
und kein Spiel bewertet sich selbst. Maßstab ist die **Log-Likelihood** des echten Ergebnisses
unter der Dixon-Coles-Matrix, dazu Trefferquote und Brier.

`--haelften` teilt nach **Ligen** in zwei unabhängige Hälften und meldet selbst „EINIG" oder
„UNEINIG". Das ist der Schutz gegen Anpassung: Nur was in beiden Hälften dasselbe Optimum hat,
ist überhaupt ein Kandidat. Am 02.10.2026 waren **acht von acht Konstanten uneinig**.

Das Werkzeug baut H2H und das Datenfenster nicht nach – eine Zahl daraus gilt für den **Kern**
des Modells. Was damit erlaubt und was verboten ist, steht in `CLAUDE.md` unter „Rückschau".

Stand am 02.10.2026 über 2136 Spiele aus 12 reifen Ligen: **1282 Treffer gegen 1275,4
erwartete (60,0 gegen 59,7 %, z = +0,29)**, Tore −0,3 %, Log-Likelihood je Spiel −2,91260,
Brier 0,23240. Das Modell ist kalibriert.

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

### Spreizung der erwarteten Tore

Das Modell traf das **Niveau** der erwarteten Tore gut, aber nicht die **Spreizung**. Gemessen
an 108 zwischengespeicherten Spielen mit vollständigen Vorab-Quoten, Modell-λ gegen Markt-λ:

| | Bias | Steigung | t gegen 1 |
|---|---|---|---|
| Heimtore | −0,013 | 0,842 | −3,15 |
| Auswärtstore | −0,014 | 0,857 | −2,27 |
| Tore gesamt | −0,027 | **0,809** | **−3,54** |
| Differenz | +0,001 | 0,879 | −2,13 |

Heimvorteil 1,304 gegen 1,307 beim Markt, Gesamttore 2,889 gegen 2,916 – das Niveau passt.
Aber eine Steigung unter 1 heißt: sagt das Modell einen hohen Wert, sagt der Markt einen
weniger hohen. Ob das Modell übertreibt oder nur verrauschter ist als der Markt, lässt sich
nicht trennen (Regressionsverdünnung); die Antwort ist in beiden Fällen dieselbe und folgt aus
der Statistik: eine verrauschte Schätzung gehört zum Mittel gezogen.

Seit 02.10.2026 gilt `λ' = Liga-Basis + 0,85 · (λ − Liga-Basis)`. Gemessen an denselben
108 Spielen:

| | vorher | jetzt |
|---|---|---|
| λ-Fehler gegen Markt | 0,303 Tore | **0,291** |
| Abstand zum Markt beim Tipp | 4,18 Punkte | **3,63** (t = −3,34) |
| Wahrscheinlichkeit des Tipps | 61,24 % | 60,89 % |
| größter Marktabstand | 24,0 Punkte | **18,7** |
| Spiele über der 8-Punkte-Grenze | 11 | **9** |
| Tipp gewechselt | – | 7 von 114 |

**Am 02.10.2026 zurückgenommen – `LAMBDA_DAEMPFUNG` steht auf 1,00.** Der Nutzer hat die
Rückschau auf echte Ergebnisse erlaubt, und die sagt das Gegenteil: Walk-forward über
**2136 Spiele aus 12 reifen Ligen**, Teamdaten je Spiel nur aus Spielen davor, bewertet nur
mit mindestens 10 Vorspielen je Team.

| k | LogLik je Spiel | Trefferquote | Brier |
|---|---|---|---|
| 0,80 | −2,91495 | 60,1 % | 0,23264 |
| 0,85 | −2,91396 | 60,0 % | 0,23253 |
| **1,00** | **−2,91260** | 60,0 % | **0,23240** |

Beste Log-Likelihood und bester Brier bei 1,00; paarweise 0,85 gegen 1,00 t = −1,26 (im
Zufallsbereich, Richtung negativ); 9 von 12 Ligen bevorzugen einzeln 1,00.

**Näher am Markt heißt nicht näher an der Wirklichkeit.** Der Marktabstand ist ein
Warnsignal, keine Zielfunktion. Der Befund selbst (Steigung 0,81 bei t = −3,5) bleibt richtig,
die Schlussfolgerung war falsch.

**Was dieselbe Messung über das Modell sagt:** Über die 2136 Spiele trifft es **60,0 % bei
59,7 % vorhergesagten (z = +0,29)**, keine der fünf Wetten weicht signifikant ab, und die
Torzahl stimmt auf **−0,3 %** (5753 gegen 5769 erwartete). Das Modell ist kalibriert.

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

**Die Grenze lag zunächst bei 0,65 und ist am 02.10.2026 auf 0,85 korrigiert worden**, gemessen
an echten Ergebnissen. Im Walk-forward über 2136 Spiele rutschte Saison 16015 mit einem
Verhältnis von **0,66** knapp durch – und genau diese Liga verdarb das xG-Gewicht:

| Saison 16015 allein, 161 Spiele | LogLik je Spiel | Trefferquote | Brier |
|---|---|---|---|
| xG mit 0,70 (Grenze 0,65) | −2,69346 | 64,0 % | 0,22492 |
| **xG aus (Grenze 0,85)** | **−2,55881** | **65,8 %** | **0,21080** |

Über alle 2136 Spiele: LogLik je Spiel −2,91260 → **−2,90246**, Brier 0,23240 → **0,23134**,
paarweise **+21,68 LL bei t = +2,91**. Weiter hinauf geht nicht: eine Grenze von 0,95 fasst
vier Ligen und wird wieder schlechter (+1,75 LL, t = +0,18, Trefferquote 58,1 statt 59,3 %).
Die Verhältnisse der zwölf geprüften Ligen lagen bei 0,66 und dann erst wieder bei 0,91 bis
1,12 – 0,85 liegt in dieser Lücke. `LIGA_XG_WARN` steht deshalb jetzt bei 0,95.

**Und er gilt in beide Richtungen, seit dem 02.10.2026.** Liegt das Liga-xG über
`LIGA_XG_MAX` = 1,15, ist die Torbasis `(1−b)·Tore + b·xG` um `b·(q−1)` zu hoch – bei
q = 1,34 also um 13,6 %, was systematisch Richtung Über 2,5 und Beide treffen drückt. Die
**Teamstärken** sind Verhältnisse (Team-xG / Liga-xG) und kürzen eine gleichmäßige Verzerrung
heraus, deshalb bleibt `XG_ANTEIL` dort stehen. Gemessen im Walk-forward:

| Variante | t gegen die Fassung mit nur der Untergrenze |
|---|---|
| unter 0,85 nur `XG_ANTEIL` aus | −1,63 |
| unter 0,85 nur `LIGA_BASIS` aus | **−3,04** |
| über 1,10 nur `LIGA_BASIS` aus | **+2,00** |
| über 1,10 beides aus | −0,63 |

Unten trägt das Teamgewicht den Gewinn, oben die Basis – beide „beides aus"-Varianten sind
schlechter. **Die Grenze 1,15 ist das Spiegelbild von 0,85, nicht das gemessene Optimum:**
die +2,00 hängen an einer Liga mit Verhältnis 1,12, und 1,12 ist der oberste Wert des
beobachteten Normalbereichs (0,91 bis 1,12). Eine Grenze mitten hinein wäre Anpassung an eine
Liga. Mit 1,15 ist die einzige messbare Liga 17387 (1,21, nur 12 bewertbare Spiele):
LogLik −2,60403 → −2,57766, Brier 0,22599 → 0,22380, **t = +0,78 – Richtung stimmt,
Stichprobe reicht nicht.**

Der Test **kostet keine zusätzliche API-Abfrage** – die Werte stehen in der
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
> **Am 03.10.2026 auf den Stand vom 28.09.2026 zurückgesetzt** (Commit `c6d006a`),
> vom Nutzer verlangt. Der laufende Rechenweg hat **genau 14 Konstanten**:
> `MARKT_ANTEIL` steht wieder auf **0,0**, und `LAMBDA_DAEMPFUNG`,
> `GLEICHSTAND_PUNKTE`, `EMPF_STOERUNG`, `LIGA_XG_MIN`, `LIGA_XG_MAX` und
> `LIGA_XG_WARN` **gibt es nicht mehr**. Die Zeilen dazu in der Tabelle und die
> Abschnitte weiter unten beschreiben Messungen, nicht den laufenden Code.
> Neu daneben: die Forebet-Gegenprobe in `analyse/forebet.py`.

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
| `LAMBDA_DAEMPFUNG` | 1,00 | aus – geprüft und verworfen, siehe unten |
| `GLEICHSTAND_PUNKTE` | 2,0 | darunter entscheidet die Empfindlichkeit, nicht die Wahrscheinlichkeit |
| `EMPF_STOERUNG` | 0,10 | λ-Fehler, an dem die Empfindlichkeit gemessen wird |
| `LIGA_XG_MIN` | 0,85 | darunter rechnet die ganze Liga nur mit Toren |
| `LIGA_XG_MAX` | 1,15 | darüber fällt nur `LIGA_BASIS_XG` weg, Teamstärken bleiben |
| `LIGA_XG_WARN` | 0,95 | darunter nur ein Hinweis in der Ausgabe |
| `MARKT_ANTEIL` | **0,5** | halber Markt in den erwarteten Toren – gemessen, siehe unten |
| `MIN_SAISONSPIELE` | 3 | darunter keine Prognose (Sperre) |
| `FENSTER_MIN_SPIELE` | 10 | darunter wird die Saison mit den letzten 10 Spielen aufgefüllt |
| `CACHE_STUNDEN` | 6 | danach werden API-Daten neu geladen |

### Die Gewichte wurden am 02.10.2026 einmal gegen echte Ergebnisse geprüft

Der Nutzer hat die Rückschau erlaubt. Alle acht Konstanten wurden im Walk-forward über
2136 Spiele durchgefahren, und zwar **auf zwei unabhängigen Ligen-Hälften getrennt**, um
Anpassung von echtem Gewinn zu unterscheiden:

| Konstante | jetzt | beste in Hälfte A | beste in Hälfte B | |
|---|---|---|---|---|
| `XG_ANTEIL` | 0,70 | 0,4 | 0,6 | uneinig |
| `LIGA_BASIS_XG` | 0,40 | 0,2 | 0,6 | uneinig |
| `SEITE_K` | 6 | 2 | 20 | uneinig |
| `DAEMPFUNG_K` | 5 | 12 | 3 | uneinig |
| `FORM_ANTEIL` | 0,25 | 0,4 | 0,25 | uneinig |
| `FORM_DAEMPFUNG_K` | 3 | 3 | 1 | uneinig |
| Formfenster | 6 | 4 | 8 | uneinig |
| `DIXON_COLES_RHO` | −0,07 | −0,025 | −0,07 | uneinig |

**Acht von acht widersprechen sich.** Keine einzige Konstante hat in beiden Hälften dasselbe
Optimum – das ist die Signatur von Anpassung an Rauschen, und damit ist die Regel „nicht an
vergangenen Spielen optimieren" nicht länger nur eine Haltung, sondern gemessen.

Der einzige scheinbare Ausreißer war `XG_ANTEIL`, wo **beide** Hälften etwas unter 0,70
bevorzugten. Das löste sich in der Kontrolle auf: Es kam aus **einer** Liga mit kaputtem xG
(Saison 16015, Verhältnis 0,66), die knapp an der damaligen Grenze von 0,65 vorbeirutschte.
Ohne diese Liga liegt das Optimum in allen drei Mengen bei 0,6 und der Unterschied zu 0,7 ist
nicht mehr signifikant (t = +0,66 über alle, +0,47 und +0,46 je Hälfte). **Geändert wurde
deshalb kein Gewicht, sondern die Datenschranke `LIGA_XG_MIN`.**

Diese Werte sind **nach Erfahrung gesetzt und nicht an vergangenen Spielen optimiert** – so gewollt.
Sie bleiben fest, damit jede Analyse vergleichbar ist. Nur auf ausdrücklichen Wunsch ändern,
Begründung im Code danebenschreiben und diese Tabelle nachziehen.
Nicht nachträglich an einzelne Spielausgänge anpassen.

## Markt-Anteil 0,5 (03.10.2026)

`MARKT_ANTEIL` stand von Anfang an auf **0,0** – die Vorab-Quoten rechneten nicht mit.
Am 03.10.2026 war das **erstmals gegen echte Ergebnisse messbar**: `league-matches`
liefert die Quoten mit, damit stehen 2333 Spiele im Walk-forward zur Verfügung statt
der Momentaufnahmen des jeweiligen Tages.

| `MARKT_ANTEIL` | LogLik je Spiel | Trefferquote | Brier | t gegen 0 | Ligen besser |
|---|---|---|---|---|---|
| **0,0** (vorher) | −2,86028 | 60,7 % | 0,23056 | – | – |
| 0,2 | −2,85092 | 60,9 % | 0,22936 | **+9,81** | **13 von 13** |
| 0,4 | −2,84400 | 61,8 % | 0,22847 | +8,68 | **13 von 13** |
| 0,8 | −2,83710 | 62,3 % | 0,22760 | +6,31 | 11 von 13 |
| 1,0 | −2,83706 | 62,5 % | 0,22762 | +5,08 | 11 von 13 |

Beide Ligen-Hälften sind bei **jedem** Wert positiv, die größte Einzelliga trägt 14 %
des Gewinns. Das ist der größte gemessene Effekt im ganzen Projekt – und der einzige,
der nicht an einer einzelnen Liga hängt. Zum Vergleich: bei `SUM_D` kamen 70 % des
scheinbaren Gewinns aus einer Liga ohne xG, bei der Gegnerstärke 100 % aus einer Liga
mit kaputtem xG.

**0,5 und nicht 1,0.** Zwei unabhängige Gründe zeigen auf dieselbe Zahl:

1. Bei 1,0 ist das Modell rechnerisch der Buchmacher. `gegen fair` wird null, Value
   gibt es nie wieder. Das Modell wäre genauer und als Wettgrundlage wertlos.
2. Gemessen (`pruefung.py --widerspruch`): das Modell **übertreibt seinen Vorsprung
   um etwa das Doppelte**. Bei Abstand ≥ 8 Punkten sagte es 64,4 %, der Markt 52,6 %,
   eingetreten sind **59,1 %** – fast genau die Mitte. Einen halben Marktanteil
   einzurechnen ist mathematisch dasselbe wie den behaupteten Vorsprung zu halbieren.

**Das Value-Signal bleibt erhalten**, gemessen an denselben Spielen (Abstand ≥ 2
Punkte, „Fehler" = Versprechen minus Eintritt):

| | verspricht | trifft | Fehler | z gegen Markt |
|---|---|---|---|---|
| ohne Markt | 61,4 % | 58,6 % | **+2,8** | +2,12 |
| Markt 0,5 | 60,3 % | 59,8 % | **+0,4** | +1,51 |

Die Übertreibung ist weg, und die Wirklichkeit liegt weiter **über** dem Marktpreis.
Damit ist auch die Aussage in `CLAUDE.md`, der Value-Abstand messe „das eigene
Rauschen", als zu pessimistisch widerlegt: er trägt Signal, war aber doppelt zu groß
angeschrieben.

**Folge, die man kennen muss:** der `Abstand zum Markt` halbiert sich, weil der Markt
jetzt in beiden Zahlen steckt. Spiele über 8 Punkten gingen von 232 auf 19 zurück.
Die 8-Punkte-Grenze der Rangliste ist deshalb **nicht** angepasst – eine neue Schwelle
aus der Rückschau abzuleiten ist verboten. Wer sie ändern will, muss es anweisen.

Fehlen die Quoten, rechnet das Modell wie bisher ohne Markt. Über `--markt 0`
jederzeit abschaltbar.

## Zweiter Rechenkern: Maximum Likelihood (03.10.2026)

`analyse/modell2.py` ist der Rechenweg **neu gebaut**, nicht erweitert. Statt
Teamstärke = Saisonmittel ÷ Ligamittel plus acht handgesetzte Dämpfungskonstanten
steht dort eine gewichtete Poisson-Regression auf Spielebene:

```
log E[Tore Heim] = mu + heim + angriff[Heim] − abwehr[Ausw]
log E[Tore Ausw] = mu        + angriff[Ausw] − abwehr[Heim]
```

Angriff und Abwehr **aller** Teams werden simultan geschätzt. Damit ist die
Gegnerstärke per Konstruktion herausgerechnet, statt nachträglich korrigiert zu
werden. Die Zielfunktion ist konvex – L-BFGS mit analytischem Gradienten findet das
eine Optimum; mit Warmstart laufen 373 Zeitpunkte einer Saison in 0,5 Sekunden.

Vier Größen statt acht Konstanten, jede im Walk-forward über 2971 Spiele aus 16 Ligen
bestimmt und mit Ligen-Hälften geprüft:

| Größe | Wert | Verdikt | ersetzt |
|---|---|---|---|
| `HALBWERT` | 180 Tage | EINIG | `FORM_ANTEIL`, `FORM_DAEMPFUNG_K`, Formfenster |
| `RIDGE` | 4,0 | EINIG | `SEITE_K`, `DAEMPFUNG_K`, `MIN_SAISONSPIELE` |
| `XG_K` | 1,0 (xG-Anteil 0,50) | EINIG | `XG_ANTEIL`, `LIGA_BASIS_XG` |
| `RHO` | −0,07 | UNEINIG → unverändert | `DIXON_COLES_RHO` |

**Das Ergebnis ist der eigentliche Befund:**

| | LogLik je Spiel | Trefferquote | Brier | Treffer | erwartet |
|---|---|---|---|---|---|
| alt | −2,86649 | 59,4 % | 0,23258 | 1766 | 1802,6 |
| neu | −2,86898 | 59,6 % | 0,23278 | 1770 | 1768,6 |

**t = −0,87.** Ein völlig anderes Verfahren landet an derselben Stelle. Die Mischung
beider Kerne bringt ebenfalls nichts (beste Stufe t = +0,55, UNEINIG, 63 % aus einer
Liga) – beide ziehen also dieselbe Information aus denselben Daten. **Die Grenze
sitzt in den Daten, nicht im Rechenweg.** Das ist gemessen, nicht vermutet, und es
ist der Grund, warum weitere Zusatzkomponenten nichts bringen werden.

Einen Unterschied gibt es: **Kalibrierung.** Alt verspricht 1802,6 Treffer und
liefert 1766 (z = −1,37), neu verspricht 1768,6 und liefert 1770 (z = +0,05). Das
alte Modell überschätzt seine Wahrscheinlichkeiten – und damit jede Value-Zahl. Mit
`MARKT_ANTEIL = 0,5` ist dieser Fehler behoben (+0,4 statt +2,8 Punkte), deshalb
bleibt `modell.py` der laufende Rechenweg und `modell2.py` ist der geprüfte
Gegenentwurf.
