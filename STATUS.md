# Stand

Zuletzt aktualisiert: **02.10.2026**. Diese Datei ist die Übergabe an die nächste Session –
sie sagt, wo alles steht. Die Regeln stehen in `CLAUDE.md`, der Rechenweg in `README.md`,
die Schwachstellen in `SOLLBRUCHSTELLEN.md`.

## Als Erstes in einer neuen Session

```
python3 analyse/bilanz.py --auswerten
```

Das holt die Ergebnisse der offenen Spiele und zieht die Bilanz. **Vor jeder Antwort auf
die Frage „warum lag die Prognose daneben" zwingend zuerst ausführen.**

## Modellstand

| Konstante | Wert | |
|---|---|---|
| `XG_ANTEIL` | 0,70 | |
| `LIGA_BASIS_XG` | 0,40 | |
| `SEITE_K` | 6 | |
| `DAEMPFUNG_K` | 5 | |
| `FORM_ANTEIL` / `FORM_DAEMPFUNG_K` | 0,25 / 3 | |
| `H2H_ANTEIL` / `H2H_MAX_JAHRE` / `H2H_DAEMPFUNG_K` | 0,10 / 3 / 3 | |
| `DIXON_COLES_RHO` | −0,07 | |
| `LAMBDA_DAEMPFUNG` | **1,00** | aus – am 02.10. geprüft und verworfen |
| `GLEICHSTAND_PUNKTE` / `EMPF_STOERUNG` | **2,0 / 0,10** | neu am 02.10. |
| `LIGA_XG_MIN` / `LIGA_XG_WARN` | **0,85 / 0,95** | neu am 02.10. |
| `MARKT_ANTEIL` | 0,0 (aus) | |
| `MIN_SAISONSPIELE` | 3 | |
| `FENSTER_MIN_SPIELE` | 10 | |
| `CACHE_STUNDEN` | 6 | |

**Kein Gewicht ist je an vergangenen Spielen optimiert worden**, und am 02.10. wurde geprüft,
dass das richtig ist: alle acht Gewichte im Walk-forward über 2136 Spiele durchgefahren,
getrennt auf zwei Ligen-Hälften – **acht von acht widersprechen sich**. Details in
`SOLLBRUCHSTELLEN.md` Punkt 25.

Frühere Fassungen: `d912a1c` (ohne Datenfenster), `605fab4` (mit).
Zurückschalten: `git checkout <commit> -- analyse/modell.py`

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

| | |
|---|---|
| Prognosen gesamt | 79 |
| ausgewertet | 78 |
| **offen** | **0** |
| abgesagt | 1 (New York RB – St. Louis City) |
| Treffer | 49 gegen 47,6 erwartete (z = +0,33) |
| Trefferquote | 62,8 % (Modell sagte 61,0 %) |
| Tore | 222 gegen 223,0 erwartete (−0,4 %) |
| Geld, alle Tipps zu 10 € | −32 € auf 760 € (−4,2 %) |
| Geld, nur die 16 mit Value | +7 € auf 160 € |

**`abstand_markt` steht bei 0 von 78 Einträgen** – seit das Feld am 30.09. dazukam, ist keine
Prognose mehr aufgezeichnet worden. Die Frage, ob Tipps mit großem Marktabstand schlechter
liefen, ist weiter unbeantwortet. Ab der nächsten Prognose kommen `abstand_markt`,
`empf_tipp` und `gleichstand` mit.

**58 % der 78 Tipps waren „Beide treffen", Sieg Auswärts kein einziger.** Das ist Arithmetik
(Basisraten 54–69 % gegen 30 %), kein Fehler – aber es heißt, die Bilanz misst überwiegend,
wie gut „Beide treffen" vorhergesagt wird.

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

## Der Walk-forward liegt nicht im Repo

Der Nutzer hat die Rückschau auf echte Ergebnisse am 02.10.2026 erlaubt – **für diese
Messung**, nicht als dauerhaftes Werkzeug. Die Skripte lagen im Arbeitsverzeichnis der
Session. Der Aufbau steht in `SOLLBRUCHSTELLEN.md` Punkt 24 beschrieben: `league-matches` je
Liga, nach `date_unix` sortieren, Teamdaten je Spiel nur aus Spielen davor, mindestens 10
Vorspiele je Team, dann Log-Likelihood der echten Ergebnisse unter der Dixon-Coles-Matrix.

**Der Nutzer wurde gefragt, ob es ins Repo soll – noch keine Antwort.** Mit dem Werkzeug
ließe sich jede künftige Idee gegen 2000 echte Spiele prüfen statt gegen 78.

## Wettscheine des Nutzers

| Datum | Schein | Ergebnis |
|---|---|---|
| 27.09. | 7 Legs, 10 € | **verloren** – 6 von 7 getroffen. Einzeln: 16,64 € (+66 %) |
| 28.09. | 4 Legs, 20 €, Kombiquote 7,26 | **verloren** – 3 von 4 getroffen. Einzeln: rund 25 € |
| 30.09. | 6 Legs (Tipico) | – |

**Dreimal dieselbe Rechnung:** Die Marge multipliziert sich je Leg. Fünf Legs à 7 % sind
30,4 %, sechs 34,9 %.

## Was als Nächstes ansteht

Der Nutzer spielt **ab dem 10.10.2026 Topligen**. Dort ist die Saison reif, `Fenster` 0 %,
das xG sauber – die beste Datenlage, die das Modell bekommen kann. Jede Prognose von da an
landet mit `abstand_markt`, `empf_tipp` und `gleichstand` in `bilanz.json`. **Nach rund
hundert solchen Spielen** lässt sich erstmals beantworten, ob die 8-Punkte-Grenze stimmt und
ob der Gleichstand-Entscheid trägt.
