# Stand

Zuletzt aktualisiert: **03.10.2026**. Diese Datei ist die Übergabe an die nächste Session –
sie sagt, wo alles steht. Die Regeln stehen in `CLAUDE.md`, der Rechenweg in `README.md`,
die Schwachstellen in `SOLLBRUCHSTELLEN.md`.

## Als Erstes in einer neuen Session

```
python3 analyse/bilanz.py --auswerten
```

Das holt die Ergebnisse der offenen Spiele und zieht die Bilanz. **Vor jeder Antwort auf
die Frage „warum lag die Prognose daneben" zwingend zuerst ausführen.**

## Modellstand

**Am 03.10.2026 auf den Stand vom 28.09.2026 zurückgesetzt** (Commit `c6d006a`,
Fassung 2), vom Nutzer verlangt. `modell.py` und `bilanz.py` stehen wieder dort.
**Genau 14 Konstanten:**

| Konstante | Wert |
|---|---|
| `XG_ANTEIL` | 0,70 |
| `LIGA_BASIS_XG` | 0,40 |
| `SEITE_K` | 6 |
| `DAEMPFUNG_K` | 5 |
| `FORM_ANTEIL` / `FORM_DAEMPFUNG_K` | 0,25 / 3 |
| `H2H_ANTEIL` / `H2H_MAX_JAHRE` / `H2H_DAEMPFUNG_K` | 0,10 / 3 / 3 |
| `DIXON_COLES_RHO` | −0,07 |
| `MARKT_ANTEIL` | **0,0** |
| `MIN_SAISONSPIELE` | 3 |
| `FENSTER_MIN_SPIELE` | 10 |
| `CACHE_STUNDEN` | 6 |

**Weg mit dem Rücksprung:** die drei xG-Liga-Schranken, `xg_fehlt`, der
Gleichstand-Entscheid, `LAMBDA_DAEMPFUNG`, `MARKT_ANTEIL = 0,5`, und in `bilanz.json`
die Felder `abstand_markt`, `empf_tipp`, `gleichstand`.

**Vier bekannte Fehler sind damit zurück** – `sys.exit` bei API-Fehlern reißt den
ganzen Lauf mit, fehlendes xG wird als „keine Chancen" gelesen, `--auswerten` verwirft
geholte Ergebnisse, `abstand_markt` wird nicht aufgezeichnet. Dem Nutzer gesagt, von ihm
zweimal verlangt. Details in `CLAUDE.md`, Abschnitt „Modellstand eingefroren".

**Kein Gewicht ist je an vergangenen Spielen optimiert worden.** Am 02.10. im
Walk-forward über 2136 Spiele geprüft, getrennt auf zwei Ligen-Hälften: **acht von acht
widersprechen sich.** Am 03.10. zusätzlich geprüft, ob eine Mittelung über die
Erfahrungswerte hilft – nein (t = +0,79, Hälfte A negativ). Das Modell ist gegen seine
eigenen Gewichte unempfindlich.

Frühere Fassungen: `d912a1c` (ohne Datenfenster), `605fab4` (mit), `c6d006a` (**jetzt**),
`853b732` (mit Markt 0,5 und allen xG-Schranken).
Umschalten: `git checkout <commit> -- analyse/modell.py analyse/bilanz.py`

## Wie gut das Modell ist

Gemessen am 02.10.2026 im Walk-forward über **2136 Spiele aus 12 reifen Ligen**, Teamdaten je
Spiel nur aus Spielen davor:

| | tatsächlich | erwartet | z |
|---|---|---|---|
| Tipps getroffen | 1282 (60,0 %) | 1275,4 (59,7 %) | +0,29 |
| Sieg Heim | 943 | 911,4 | +1,41 |
| Sieg Auswärts | 621 | 647,9 | −1,29 |
| Über 2,5 | 1079 | 1071,9 | +0,32 |
| Beide treffen | 1162 | 1144,5 | +0,77 |
| Tore | 5753 | 5769 | −0,3 % |

**Das Modell ist kalibriert.** Keine der fünf Wetten weicht signifikant ab. Was es nicht
kann: den Buchmacher schlagen – der Abstand zum Markt liegt bei rund 4 Punkten, die Marge
bei 7 bis 10 %.

## Bilanz der eigenen Prognosen

Stand 03.10.2026, 01:14 UTC (`python3 analyse/bilanz.py --auswerten`):

| | |
|---|---|
| Prognosen gesamt | 89 |
| ausgewertet | 80 |
| **offen** | **8** (die Spiele vom 03.10. nach 23:30 UTC) |
| abgesagt | 1 (New York RB – St. Louis City) |
| Treffer | 50 gegen 48,8 erwartete (z = +0,28) |
| Tore | 231 gegen 227,6 erwartete (+1,5 %) |
| Geld, alle 78 Tipps mit Quote zu 10 € | **−34 €** auf 780 € (−4,3 %) |
| Geld, nur die 16 mit Value | **+7 €** auf 160 € |

**Das ist die wichtigste Zahl der Datei:** die 16 Tipps mit Value stehen bei +7 €, die 62
ohne bei −41 €. Ein kalibriertes Modell plus 7 bis 10 % Marge ergibt knapp Verlust; der
einzige Hebel, der in 80 Spielen in die richtige Richtung zeigt, ist die Auswahl nach Quote.

**Die ersten zehn Einträge mit `abstand_markt`, `empf_tipp` und `gleichstand`** stammen vom
03.10. (Commit `dd76255`). Die Frage, ob Tipps mit großem Marktabstand schlechter liefen, ist
damit erstmals beantwortbar – aber erst nach rund hundert solchen Spielen.

**Alle 89 Aufzeichnungen sind ohne Markt-Anteil entstanden.** Ab dem 03.10. entstehen sie mit
`MARKT_ANTEIL = 0,5`. Beim Auswerten ist das zu **trennen**, nicht nachzurechnen.

**58 % der ersten 78 Tipps waren „Beide treffen", Sieg Auswärts kein einziger.** Das ist
Arithmetik (Basisraten 54–69 % gegen 30 %), kein Fehler. Am 03.10. nachgemessen: würfelt man
den Tipp statt das Maximum zu nehmen, wird die Mischung gleichmäßig und die Trefferquote
fällt um **10,4 Punkte**. Die Konzentration ist der Preis der Genauigkeit.

## Was am 02.10.2026 passiert ist

Fünf Änderungen, sechs Commits. **Drei betreffen Datenqualität und Verlässlichkeit, eine die
Auswahl, eine wurde zurückgenommen.** Kein Gewicht wurde angefasst.

| Commit | Was | belegt? |
|---|---|---|
| `1dd3616` | API-Fehler riss den ganzen Lauf mit (`SystemExit` statt `Exception`) | Fehler, behoben |
| `6f60d52` | Liga-Test für das xG eingebaut | Datenfehler, behoben |
| `5bbb1ba` | `--auswerten` verwarf geholte Ergebnisse | Fehler, behoben |
| `c717e7a` | Gleichstand-Entscheid unter 2 Punkten | Richtung stimmt, nicht signifikant |
| `eb66b39` → `5f750fa` | λ-Dämpfung 0,85 eingebaut und **zurückgenommen** | an Ergebnissen widerlegt |
| `4419e30` | `LIGA_XG_MIN` 0,65 → 0,85 | **+21,68 LL, t = +2,91, signifikant** |

**Die einzige an echten Ergebnissen belegte Verbesserung ist die letzte** – und sie ist eine
Schranke für Datenqualität, kein Gewicht. Das ist die Lehre des Tages: Treffsicherheit kommt
daraus, kaputte Daten zu erkennen, bevor sie in die Rechnung gehen.

## Was am 03.10.2026 passiert ist

Vom Nutzer verlangt: „es muss besser und präziser werden und nicht immer nur durch Zufall",
dann „erfinde das komplette System komplett neu". **Eine Änderung am Rechenweg, fünf
gemessene Absagen.**

| Commit | Was | belegt? |
|---|---|---|
| `a96bcbb` | `pruefung.py`: misst, was dem Modell fehlt | Werkzeug |
| `6dfb7c1` | `modell2.py`: Rechenkern neu gebaut (Maximum Likelihood) | **gleich gut, t = −0,87** |
| `853b732` | **`MARKT_ANTEIL` 0,0 → 0,5** | **t = +8,68, 13 von 13 Ligen** |
| `d09d8f9` | die vier Größen von `modell2.py` auf die gemessenen Werte | drei EINIG, eine uneinig |
| `5a7814f` | Zufall als Bauprinzip, drei Lesarten | alle drei ohne Gewinn |

**Durchgefallen, damit es nicht wieder versucht wird:** Gegnerstärke (100 % des scheinbaren
Gewinns aus einer Liga mit kaputtem xG), Ruhetage und Spieldichte (gar kein Zusammenhang,
t = −0,82 bis +0,94), Dämpfung nur auf die Summe (70 % aus einer Liga ohne xG), Punkte pro
Spiel (hält die Ligen-Gegenprobe, wirkt aber erst ab 15 Vorspielen – im Oktober nutzlos),
der zweite Rechenkern, die Mischung beider Kerne, Bootstrap-Mittelung (t = −2,99).

**Was `MARKT_ANTEIL = 0,5` bringt:** Trefferquote 60,7 → **61,8 %**, Brier 0,23056 →
0,22814. Wichtiger für das Geld: die Überzeichnung des Value fällt von **+2,8 auf +0,4
Punkte**. Vorher versprach das Modell bei 2 Punkten Marktabstand 61,4 % und lieferte 58,6 %.

## Die drei wichtigsten Lehren vom 03.10.2026

1. **Die Grenze sitzt in den Daten, nicht im Rechenweg.** Zwei strukturell verschiedene
   Schätzer sind gleich gut, und gemischt bringen sie nichts. Eine weitere Komponente im
   Kern wird die Trefferquote nicht heben.
2. **Das Einzige, was gewirkt hat, war Information von außen** – die Vorab-Quoten. Jede
   künftige Idee sollte sich fragen, welche *neue* Information sie bringt, nicht welche
   Verrechnung sie ändert.
3. **Das Zufallsprinzip ist schon eingebaut und heißt Dämpfung.** `DAEMPFUNG_K`, `SEITE_K`,
   `RIDGE` – explizit Zufall darüber zu mitteln zählt dieselbe Unsicherheit zweimal und
   verschlechtert die Likelihood.

## Die drei wichtigsten Lehren vom 02.10.2026

1. **Näher am Markt heißt nicht näher an der Wirklichkeit.** Die λ-Dämpfung war auf den
   Marktabstand hin gebaut (Steigung 0,81, t = −3,5) und fiel gegen echte Ergebnisse durch.
   Der Marktabstand ist ein Warnsignal, keine Zielfunktion.
2. **Sieht eine Konstante schlecht aus, erst nach der kaputten Liga suchen.** Eine von zwölf
   Ligen hat gereicht, um `XG_ANTEIL` um 0,2 bis 0,3 falsch aussehen zu lassen.
3. **Die Fehler sitzen nicht in der Rechnung, sondern davor und danebe**n: drei von fünf
   Änderungen waren Abbrüche und Datenfehler, die man der Ausgabe nicht ansieht.

## Offene Punkte

| Punkt | Was | warum offen |
|---|---|---|
| 10 | Wirkung des Datenfensters ungeklärt, eher negativ | nie an Ergebnissen geprüft |
| 16 | Saison 16580: xG 34 % über den Toren, Torbasis 8,8 % zu hoch | verändert Zahlen |
| 17 | Fenster (10 Spiele) und Form (6) zählen dieselben Spiele doppelt | Gewichte liegen fest |
| 20 | Begründung der Saisonspiel-Sperre korrigiert, Grenze bleibt bei 3 | erledigt, nur Doku |
| 21 | Ein Spiel kann in zwei Tageslisten stehen – IDs entdoppeln | Ablauf, nicht Code |
| 21 | `p_tipp` ist als Maximum aus fünf Wetten nach oben verzerrt | nicht korrigierbar |
| – | Margenbereinigung proportional statt Quotenverhältnis | 2 von 32 Spielen wechseln den Block |

## Der Walk-forward liegt im Repo

Die Frage aus der letzten Fassung ist beantwortet: **drei Werkzeuge liegen drin**, alle lesen
nur `analyse/daten/` – keine API-Abfrage, kein Stundenlimit.

```
python3 analyse/rueckschau.py                      Konstanten des laufenden Kerns
python3 analyse/pruefung.py --markt                MARKT_ANTEIL gegen echte Ergebnisse
python3 analyse/pruefung.py --widerspruch          Modell gegen Markt: wer hat recht?
python3 analyse/pruefung.py --residuen             woran haengt der Modellfehler?
python3 analyse/pruefung2.py --vergleich           alter gegen neuen Kern
python3 analyse/pruefung2.py --scan RIDGE 2 4 8    eine der vier Groessen von modell2.py
```

**Wichtig:** `pruefung.py` baut die Liga-xG-Schranken nach, `rueckschau.py` nicht. Ohne sie
sah die Gegnerstaerke nach t = +3,27 aus, mit ihnen nach t = −1,14. Jede Idee, die mit xG zu
tun hat, muss in `pruefung.py` gegengeprueft werden.

`analyse/modell2.py` ist der **Rechenkern neu gebaut** (Maximum-Likelihood-Poisson auf
Spielebene, Gegnerstaerke per Konstruktion herausgerechnet, vier gemessene Groessen statt
acht gesetzter). Er ist **gleich gut** wie `modell.py` (t = −0,87), die Mischung beider
bringt auch nichts (t = +0,55, uneinig). **Die Grenze sitzt in den Daten, nicht im
Rechenweg.** Er rechnet keine Tipps; `modell.py` bleibt der Rechenweg.

## Wettscheine des Nutzers

| Datum | Schein | Ergebnis |
|---|---|---|
| 27.09. | 7 Legs, 10 € | **verloren** – 6 von 7 getroffen. Einzeln: 16,64 € (+66 %) |
| 28.09. | 4 Legs, 20 €, Kombiquote 7,26 | **verloren** – 3 von 4 getroffen. Einzeln: rund 25 € |
| 30.09. | 6 Legs (Tipico) | – |

**Dreimal dieselbe Rechnung:** Die Marge multipliziert sich je Leg. Fünf Legs à 7 % sind
30,4 %, sechs 34,9 %.

## Was als Nächstes ansteht

Der Nutzer spielt **ab dem 10.10.2026 Topligen**.

**Die Zusage der letzten Fassung war falsch und ist am 03.10.2026 nachgemessen.** Hier stand
„Dort ist die Saison reif, `Fenster` 0 %, das xG sauber – die beste Datenlage, die das Modell
bekommen kann". Das trifft am 10.10. fuer **keine einzige** dieser Ligen zu. Grund: die
Saisons 2026/27 starteten erst zwischen dem 07. und 28.08.2026, und bis zum 10.10. liegen
Laenderspielpausen dazwischen.

Stand am 10.10.2026, Spiele je Team einschliesslich der angesetzten:

| Liga | Saison-ID | Sp./Team | `Fenster` | Rangliste | `Fenster` 0 % ab | xG/Tore |
|---|---|---|---|---|---|---|
| Niederlande Eredivisie | 17097 | 7,1 | 29 % | oben | 25.10.2026 | 0,874 (Hinweis) |
| Spanien La Liga | 17199 | 7,0 | 30 % | oben | 26.10.2026 | 0,986 (ok) |
| Frankreich Ligue 1 | 17102 | 5,1 | 49 % | oben, knapp | 08.11.2026 | 1,085 (ok) |
| Italien Serie A | 17084 | 5,0 | 50 % | oben, Grenze | 02.11.2026 | 1,087 (ok) |
| Deutschland Bundesliga | 17210 | 4,1 | **59 %** | **UNTEN** | 22.11.2026 | 0,898 (Hinweis) |

**Was daraus folgt, und es gilt ab dem ersten Spiel:**

- **Bundesliga-Spiele landen am 10.10. im unteren Block der Rangliste** (`Fenster` 59 % ueber
  der 50-%-Regel). Damit kommen sie **in keine Kombi** und sind nur mit ausdruecklicher
  Begruendung empfehlbar. Nicht vergessen, das dem Nutzer zu sagen – er erwartet das Gegenteil.
- **Serie A liegt mit 50,0 % genau auf der Grenze.** Ein verlegtes Spiel kann sie kippen; vor
  der Antwort die Zeile `Fenster:` lesen, nicht diese Tabelle.
- **Eredivisie und Bundesliga brauchen einen Satz zum xG** (0,874 und 0,898, unter
  `LIGA_XG_WARN` = 0,95). Die Ausgabe schreibt `xG auffaellig`.
- **Die Quoten sind da:** 98 bis 100 % der Spiele haben den vollen Satz. `MARKT_ANTEIL = 0,5`
  greift also fast immer – anders als bei den suedamerikanischen Ligen, wo am 03.10. nur
  8 von 11 Spielen Quoten hatten.
- **Die beste Datenlage kommt erst ab Ende Oktober**, Liga fuer Liga: Eredivisie 25.10.,
  La Liga 26.10., Serie A 02.11., Ligue 1 08.11., Bundesliga 22.11.

**Premier League (17146) und Championship (17184) fehlen** – beide liefen am 03.10. ins
Stundenlimit (HTTP 417). Vor dem 10.10. nachholen:
`python3 -c "import analyse.modell as M, argparse; M.hole('league-matches', {'season_id':17146}, 'lm_17146.json', argparse.Namespace(daten='analyse/daten', neu=False))"`

Jede Prognose ab jetzt landet mit `abstand_markt`, `empf_tipp` und `gleichstand` in
`bilanz.json`. **Nach rund hundert solchen Spielen** laesst sich erstmals beantworten, ob die
8-Punkte-Grenze stimmt und ob der Gleichstand-Entscheid traegt. Zu beachten: die 8-Punkte-
Grenze bezieht sich jetzt auf einen **halbierten** Marktabstand (siehe `MARKT_ANTEIL`), sie
wurde absichtlich nicht angepasst.
