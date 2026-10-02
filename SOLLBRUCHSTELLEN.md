# Sollbruchstellen

Bekannte Schwachstellen des Modells und des Ablaufs, gefunden am 26.09.2026.
**Vor jeder Analyse überfliegen.** Was hier als `OFFEN` steht, kann eine Prognose verfälschen,
ohne dass man es der Ausgabe ansieht.

---

## 1. Fehlende Saisondaten — GELÖST

**Was passiert:** Hat ein Team null gespielte Saisonspiele, ersetzt die Dämpfung die Teamstärke
vollständig durch den Liga-Durchschnitt. Das Modell gibt dann für jedes Spiel fast dieselben
Zahlen aus.

**Wie es sich zeigte:** Alle zehn Länderspiele am 26.09.2026 bekamen Remis 29 % und Heimsieg
zwischen 32 % und 45 % — San Marino gegen Finnland 35 % Heimsieg, Markt 3 %.

**Gelöst durch:** `MIN_SAISONSPIELE = 3` in `analyse/modell.py`. Darunter keine Prognose.

---

## 2. Länderspiele — GELÖST (durch Verzicht)

**Was passiert:** Das Modell vergleicht rohe Form-Durchschnitte, ohne zu berücksichtigen,
**gegen wen** gespielt wurde. In einer Liga treffen alle Teams auf dieselben Gegner, bei
Nationalmannschaften nicht. Eine 0:2-Niederlage gegen Spanien zählt wie eine gegen Moldau.

**Wie es sich zeigte:** Mittlere Abweichung zum Markt über zehn Länderspiele: 17 Prozentpunkte.

**Gelöst durch:** Regel in `CLAUDE.md` — Länderspiele werden nicht getippt, auch bei
ausreichender Spielzahl. Offen sagen statt schätzen.

---

## 3. Zwischenspeicher läuft nie ab — GELÖST

**Was passiert:** `analyse/daten/` speichert jede API-Antwort und verwendet sie unbegrenzt weiter.
Es gibt keine Verfallszeit.

**Folgen:**
- Quoten bewegen sich im Tagesverlauf. Eine zweite Abfrage am Abend rechnet mit den Quoten vom Morgen.
- **Schwerwiegender:** Am nächsten Tag ist die Teamstatistik veraltet. Hat ein Team
  zwischenzeitlich gespielt, ändern sich Stärke und Form — und damit alle fünf
  Wahrscheinlichkeiten. Der beste Tipp kann kippen.

**Gelöst durch:** `CACHE_STUNDEN = 6` in `analyse/modell.py`. Zwischengespeicherte Antworten
gelten sechs Stunden, danach lädt das Skript von selbst neu und sagt es in einer Zeile.
`--neu` erzwingt weiterhin sofort.

**Geprüft am 26.09.2026:** Innerhalb desselben Tages hatte sich keine einzige von 24 Quoten bewegt.
Das Risiko lag zwischen Tagen, nicht innerhalb eines Tages – sechs Stunden decken beides ab.

---

## 4. Bester Tipp: Wahrscheinlichkeit oder Preis — GELÖST

**Was passiert:** `CLAUDE.md` sagt „Value ist Nebensache", in der Praxis entscheidet der Preis
aber in engen Fällen, welche Wette benannt wird. Beides zugleich geht nicht.

**Wie es sich zeigte:** Am 26.09.2026 wurde vormittags nach Variante A getippt und nachmittags
nach Variante B, ohne dass es auffiel:

| Spiel | höchste Wahrscheinlichkeit | getippt | Variante |
|---|---|---|---|
| Atlante – Monterrey | BTTS 57,2 % | BTTS (kein Value) | A |
| Tijuana – Atlas | BTTS 56,5 % | BTTS (kein Value) | A |
| El Paso – Tulsa | BTTS 55,8 % | BTTS (kein Value) | A |
| Ceuta – Real Sociedad II | BTTS 54,2 % | Sieg Auswärts 39,8 % | B |
| Granada – Andorra | BTTS 57,7 % | Sieg Auswärts 36,5 % | B |
| Celta Fortuna – Sabadell | BTTS 58,8 % | Sieg Auswärts 39,5 % | B |

**Variante A:** Bester Tipp = höchste Wahrscheinlichkeit, Preis nur im Value-Satz.
Immer gleich, ignoriert aber, dass eine 58-%-Wette bei 1,57 auf Dauer Geld verliert.

**Variante B:** Bester Tipp = beste Wette aus Wahrscheinlichkeit und Preis.
Näher am Wetten, hängt aber an Quoten, die sich bewegen.

**Entschieden am 26.09.2026: Variante A.** Der beste Tipp ist immer die Wette mit der höchsten
Wahrscheinlichkeit, der Preis entscheidet nicht mit.

Damit trägt der **Value-Satz** die Wettentscheidung: Weil der Tipp den Preis ignoriert, benennt er
nur, was am wahrscheinlichsten ist. Ob sich die Wette zu dieser Quote lohnt, muss der Value-Satz
unmissverständlich sagen. Erst beides zusammen ergibt eine Empfehlung.

**Was Variante A kostet:** Sie benennt regelmäßig Wetten, die zum verfügbaren Preis auf Dauer Geld
verlieren. Die drei Morgentipps vom 26.09.2026 (BTTS bei 1,55 / 1,71 / 1,70 gegen faire
1,75 / 1,77 / 1,79) gingen alle auf, waren rechnerisch aber trotzdem Verlustwetten. Das ist der
bewusst gewählte Preis für eine Ausgabe, die immer gleich funktioniert.

---

## 5. Gewichte sind ungeprüft — IN ARBEIT

Die Gewichte in `analyse/modell.py` sind nach Erfahrung gesetzt, nicht an vergangenen Spielen
optimiert. Sie bleiben fest, damit Analysen vergleichbar sind.

**Seit 26.09.2026 gibt es einen Weg, das zu prüfen:** `analyse/bilanz.py` hält jede Prognose fest
und wertet sie gegen die Ergebnisse aus, mit z-Test gegen den Zufall.

**Erster Stand (15 Spiele, 26.09.2026):**

| | erwartet | tatsächlich | z |
|---|---|---|---|
| Tipps getroffen | 9,4 | 9 | −0,22 |
| Beide treffen | 9,2 | 9 | −0,10 |
| Über 2,5 | 8,9 | 6 | −1,55 |
| Heimsiege | 6,2 | 7 | +0,41 |
| Tore gesamt | 46,7 | 47 | — |

Keine einzige Abweichung ist signifikant. Das Modell lag an diesem Tag **nicht** falsch; die sechs
Fehltipps sind das, was bei 60-Prozent-Wetten normal ist.

**Wichtig für künftige Fehlersuchen:** Mit 15 Spielen wäre erst eine Verzerrung ab 36
Prozentpunkten nachweisbar. Für 10 Prozentpunkte braucht es rund 190 Spiele, für 5 rund 750.
Bis dahin ist jede Anpassung der Gewichte eine Anpassung an Rauschen und macht das Modell
schlechter, nicht besser.

---

## 6. xG misst keine Abschlussqualität — INHÄRENT

**Was passiert:** Das Modell gewichtet xG mit 70 % gegenüber echten Toren. Erspielt ein Team viele
Chancen und trifft nicht, hält das Modell es für stark.

**Wie es sich zeigte:** FC Andorra hatte fünf Niederlagen in Folge bei 1,98 xG für und 1,00 xG
gegen. Das Modell setzte sie auf Augenhöhe mit Granada. Entweder ist es Pech, das sich ausgleicht
— oder die Stürmer sind schlecht, und xG sieht das nicht.

**Umgang:** Bei großer Lücke zwischen xG und Toren in der Begründung benennen, nicht verschweigen.

---

## 7. Direkte Duelle mit winzigen Stichproben — GELÖST

**Was passiert:** Direkte Duelle gehen mit 10 % in die Gesamttore ein, unabhängig davon, ob es
zwei oder dreißig Duelle sind.

**Wie es sich zeigte:** Celta Fortuna gegen Sabadell hat zwei Duelle mit 4,5 Toren im Schnitt.
Das hob die Torerwartung um rund 7 % — auf Grundlage von zwei Spielen.

**Zweiter, schwererer Fehler, gefunden am 26.09.2026:** Die Frische-Prüfung sah nur auf das
**jüngste** Duell, der eingespeiste Tor-Schnitt (`betting_stats.avg_goals`) umfasste dagegen
**alle** Duelle. Bei Emmen – Oss flossen so 24 Duelle zurück bis 2009 mit 3,46 Toren ein,
während die sechs jungen bei 2,33 lagen – eine Verzerrung von 1,13 Toren. Bei MVV – Helmond
waren es 35 Duelle seit 2009.

**Gelöst durch:** `h2h_werte()` rechnet den Schnitt selbst, aus genau den Duellen, die auch die
Frische-Prüfung bestehen. Das Gewicht wächst zusätzlich mit ihrer Zahl
(`H2H_ANTEIL * n/(n+H2H_DAEMPFUNG_K)`): ein einzelnes Duell zählt 2,5 % statt 10 %.

**Gemessen an den 15 Spielen vom 26.09.2026:** Rechnung in 12 von 15 Fällen verändert,
Trefferquote unverändert 9, Log-Likelihood der echten Ergebnisse von −46,28 auf −46,00
verbessert. Der Fix wurde gemacht, weil die alte Rechnung **falsch** war, nicht weil die
Messung ihn belegt – dafür sind 15 Spiele zu wenig.

---

## 8. Modell gegen Markt — LESEHILFE

Weicht das Modell stark vom Markt ab, ist das **kein automatischer Value**. Erst prüfen, woher
die Lücke kommt:

- **Dünne Datenlage?** Dann hat meist der Markt recht (siehe 1 und 2).
- **xG gegen Ergebnisse?** Der Markt bewertet Ergebnisse, das Modell Chancen. Beide können recht
  haben (siehe 6).
- **Markt und Modell einig?** Dann ist die Prognose belastbar, aber es gibt fast nie Value.

Faustregel: unter 10 Prozentpunkten Abweichung normal, darüber die Ursache benennen,
ab etwa 25 Prozentpunkten das Modell hinterfragen statt den Markt.

---

## 9. Formatdrift — GELÖST

**Was passiert war:** Die Ausgabe veränderte sich von Antwort zu Antwort — nummerierte Abschnitte,
zusätzliche Tabellenspalten, eigene Kapitel für Einschränkungen, fehlende Übersichtstabelle.

**Gelöst durch:** feste Vorlage in `CLAUDE.md` mit Regeln zu Tabelle, Überschrift und Zusätzen.

---

## 10. Datenfenster bei junger Saison — EINGEBAUT, WIRKUNG UNKLAR

**Was es löst:** Am Saisonanfang stehen einem Team 3 bis 6 Spiele zur Verfügung. Die FootyStats-
Website zeigt daneben ein rollendes Fenster über 7 bis 10 Spiele – deutlich andere Werte.
Für Manchester United W am 27.09.2026 (4. Spieltag):

| | Website (rollendes Fenster) | API, Saison 17475 |
|---|---|---|
| Tore erzielt | 1,4 (Heim) | 0,00 (Heim), 0,67 gesamt |
| Tore kassiert | 1,6 (Heim) | 5,00 (Heim), 2,67 gesamt |
| Schüsse / Match | 9,71 | 3,33 |
| Zu Null | 10 % | 0 % |
| Spiele | 7 bis 10 | **3** |

**Eingebaut am 27.09.2026 auf Verlangen des Nutzers:** `FENSTER_MIN_SPIELE = 10`. Unter zehn
Saisonspielen bekommt die Saison das Gewicht `n/10`, die letzten 10 Spiele den Rest; die
Spielzahl wird auf die des Fensters gehoben. Ab zehn Saisonspielen wirkungslos, reife Ligen
rechnen unverändert. Kostet keine zusätzliche API-Abfrage (derselbe `lastx`-Aufruf wie die Form).

**Was dabei herauskam – und es spricht gegen die Änderung.** Abstand zwischen Modell und
margenbereinigtem Markt beim Heimsieg, an den vier Spielen des 27.09.2026 mit Vorab-Quoten:

| Spiel | Markt | ohne Fenster | nur Datenmischung | voll (eingebaut) |
|---|---|---|---|---|
| Tottenham W – Villa W | 57,4 % | 67,5 % (10,1) | **58,5 % (1,1)** | 70,9 % (13,5) |
| Birmingham W – Palace W | 54,8 % | 33,7 % (21,1) | 27,7 % (27,1) | 31,6 % (23,2) |
| Chelsea W – Arsenal W | 40,5 % | 33,5 % (7,0) | 28,7 % (11,8) | 28,0 % (12,5) |
| Mallorca – Almería | 44,6 % | 45,6 % (1,0) | 45,5 % (0,9) | 47,1 % (2,5) |
| **Mittlerer Abstand** | | **9,8** | 10,2 | **12,9** |

Die Datenmischung allein ist etwa neutral. Das **Anheben der Spielzahl** ist der schädliche
Teil: Es nimmt der Dämpfung ihre Wirkung, und ohne diese Glättung schlägt ein anderer Fehler
voll durch – der Liga-Durchschnitt selbst. In der WSL lautet er am 4. Spieltag Heim 1,22 Tore
gegen **Auswärts 1,70**, das Verhältnis ist also verdreht. Weniger Dämpfung heißt: Dieser
verdrehte Maßstab wirkt stärker. Das erklärt, warum in drei von vier Spielen die
Auswärtsmannschaft noch weiter nach oben rutscht.

**Vier Spiele beweisen nichts.** Das ist keine Auswertung über viele Spiele (die ist in diesem
Repo verboten), sondern der Markt-Vergleich nach Sollbruchstelle 8 an den Spielen eines Tages.
Die Richtung ist einheitlich, die Grundlage winzig.

**Offen und wichtiger als das Fenster:** Der Liga-Durchschnitt wird aus derselben jungen Saison
gebildet wie alles andere. Solange er verdreht sein kann, bringt eine bessere Teamstatistik
nichts – sie wird an einem falschen Maßstab gemessen. Wer hier weitermacht, repariert zuerst
den Maßstab, nicht die Teamwerte.

**Zurückschalten auf die Fassung ohne Fenster:**
`git checkout d912a1c -- analyse/modell.py`

---

## 11. Externe Prüfung vom 28.09.2026 — ein Fehler behoben, ein Vorschlag verworfen

Der Nutzer hat die Modellbeschreibung von einem anderen Modell prüfen lassen. Acht Punkte,
davon sieben zutreffend. Was daraus folgte:

**BEHOBEN — `strengths()` stürzte ohne den lastx-6er-Block ab.** Fehlte der Block, warf die
Funktion einen `TypeError`. Der 10er-Block war über `saisonfenster()` abgesichert, der 6er
nicht. Jetzt entfällt bei fehlendem Block der Formanteil und es wird mit dem Rest gerechnet.
**An fünf echten Spielen geprüft: kein einziger Wert hat sich geändert** – die Korrektur
greift nur in dem Fall, in dem vorher gar nichts herauskam.

**VERWORFEN — den Liga-Maßstab gegen die Vorsaison schrumpfen.** Der Gedanke war richtig:
Der Maßstab stammt aus derselben dünnen Saison wie die Teams, und ein verdrehtes
Heim-Auswärts-Verhältnis macht jedes Spiel der Liga gleichzeitig falsch. Gemessen an den
14 Spielen vom 28.09.2026 mit `Liga = w·Saison + (1−w)·Vorsaison`, `w = n/(n+k)`:

| k | Tipp geändert | Abstand zum Markt vorher | nachher |
|---|---|---|---|
| 25 | 1 von 14 | 6,1 | **6,5** |
| 50 | 2 von 14 | 6,1 | **7,1** |
| 100 | 3 von 14 | 5,9 | **7,5** |

In allen drei Varianten **schlechter**, und je stärker die Schrumpfung, desto schlechter.
Nur in Griechenland wirkte sie richtig (1,76 → 1,48, Kallithea von 4,5 auf 1,6 Punkte an den
Markt heran), in Serbien und Israel dagegen falsch. Die Vorsaison ist offenbar kein guter
Anker: Auf- und Absteiger machen die Liga zu einer anderen.

**Die Schwachstelle bleibt damit OFFEN.** Der verdrehte Liga-Maßstab am Saisonanfang ist real
und unbehoben – die naheliegende Reparatur ist geprüft und taugt nicht.

**Nicht umgesetzt, weil nicht baubar:** ein seitengetrennter H2H-Faktor. Die H2H-Einträge
führen `team_a_id`, `team_b_id` und die Tore, aber **kein Feld für Heim oder Auswärts** –
ein Split würde Heim- und Auswärtspartien vermischen.

**Widerlegt:** Der Einwand, die Overall-Abwehr werde gegen die Liga-Angriffs-xG normiert und
dort sitze ein Versatz. In einer geschlossenen Liga ist jedes erzielte xG das kassierte xG
eines anderen. An drei echten Ligatabellen nachgerechnet: Mittel xG-für und Mittel xG-gegen
sind auf drei Nachkommastellen **identisch** (Differenz 0,0 %).


## 12. Fehlendes xG — BEHOBEN am 30.09.2026

**FootyStats erhebt xG nicht in jeder Liga**, und wo es erhoben wird, steht es vor dem Anpfiff
manchmal noch nicht drin. Das Feld zeigt dann 0,00. Das Modell las diese Null als Messung —
also als „dieses Team erspielt sich keine Chancen".

Gemessen an 495 Teams im Zwischenspeicher:

| | |
|---|---|
| Teams mit unbrauchbarem xG | **27 (5,5 %)** |
| davon mit glatter Null | 7 |
| in einer einzigen Liga (17308) | 14 |
| Ligen mit kaputtem xG insgesamt | **5 von 28 (18 %)** |

**Zwei Fehler auf einmal.** Ein Team mit 1,63 Toren bei Liga-Schnitt 1,61 — also exakt
Durchschnitt — bekam mit `XG_ANTEIL = 0,70` die Angriffsstärke **0,30 statt 1,01**. Und weil
die Nullen in den Liga-xG-Durchschnitt einflossen, lag der Nenner 15 % zu niedrig: Alle 41
Teams derselben Liga **mit** funktionierenden Daten bekamen eine 17 % zu hohe Angriffsstärke.

**Der Fix** steht in `xg_fehlt()` und `xg_anteil()`: Fehlt das Feld, zählen für diesen Term nur
die Tore, und das Team wird beim Liga-Mittel ausgelassen. Keine neue Konstante, keine Schwelle —
0,00 bei erzielten Toren ist objektiv eine fehlende Angabe. `XG_ANTEIL` bleibt bei 0,70.

**Geprüft an 76 Spielen mit Vorab-Quoten, ohne ein einziges Ergebnis:** 70 völlig unverändert,
6 betroffen, 2 Tipps gewechselt, Abstand zum Markt 4,17 → 4,09 Punkte.

**Was offen bleibt:** Teams mit *verzerrtem* statt fehlendem xG. Zwanzig Teams liegen beim
Verhältnis xG zu Toren unter 0,45 oder über 2,2 — dort ist das Feld gefüllt, aber unplausibel.
Sie zu erkennen bräuchte eine Schwelle, und die wäre erfunden. Bleibt deshalb unbehandelt.

## 13. Abstürze statt Sperre — BEHOBEN am 01.10.2026

Bei der systematischen Fehlersuche gefunden: `berechne()` konnte mit einer unbehandelten
Ausnahme abbrechen, statt sauber „keine Prognose" zu melden.

| Fall | vorher | jetzt |
|---|---|---|
| Saisonstart, noch kein Spiel gespielt | `ZeroDivisionError` | gesperrt |
| Liga ohne Tore in den bisherigen Spielen | `ZeroDivisionError` in `strengths()` | gesperrt, mit Grund |
| Team nicht in der Ligatabelle (Pokal, Play-off, abweichende `competition_id`) | `KeyError` | gesperrt, mit Grund |

**Die Ursache beim ersten Fall:** `L = league(T)` lief **vor** der `MIN_SAISONSPIELE`-Prüfung —
ausgerechnet in dem Fall, für den die Sperre gebaut wurde. Die Reihenfolge ist jetzt umgedreht:
erst prüfen, dann rechnen.

**Der eigentliche Schaden lag aber in der Schleife.** `for mid in args.spiele: analysiere(...)`
fing nichts ab: Ein einziges kaputtes Spiel brach den ganzen Aufruf ab, und alle folgenden
Spiele wurden nie gerechnet. Bei `bilanz.py --merken` fehlten dadurch Prognosen, ohne dass es
auffiel. Beide Schleifen fangen jetzt je Spiel ab und rechnen weiter.

**Geprüft an 97 zwischengespeicherten Spielen:** 82 gerechnet, **alle identisch zu vorher**,
null Abweichungen. Der Fix ist rein defensiv.

## 14. API-Fehler riss doch den ganzen Lauf mit — BEHOBEN am 02.10.2026

Punkt 13 hat die Schleifen abgesichert, aber nur gegen `Exception`. Der in der Praxis
häufigste Fehler kam trotzdem durch:

```
hole() ->  if not daten.get("success", True): sys.exit(...)
```

`sys.exit` wirft `SystemExit`, und **`SystemExit` erbt von `BaseException`, nicht von
`Exception`** (`issubclass(SystemExit, Exception)` ist `False`). Ein `except Exception`
fängt es also nicht. Betroffen war genau die Antwort, die FootyStats bei erreichtem
Stundenlimit, ungültigem Key oder unbekannter Spiel-ID schickt: `{"success": false}`.

**Wirkung:** Schickt man zwanzig Spiele und das dritte läuft ins Stundenlimit, brechen
Spiel 4 bis 20 ab — **ohne eine Zeile Ausgabe**. Bei `bilanz.py --merken` fehlen dadurch
Prognosen, ohne dass es auffällt. Nachgestellt und bestätigt. Dass HTTP-Fehler (417, 500)
abgefangen wurden, hat das verdeckt: die sind `Exception`.

**Behoben:** `hole()` wirft jetzt `RuntimeError` statt `sys.exit`. Der fehlende API-Key
bleibt bei `sys.exit` — der *soll* alles anhalten. Geprüft: identische Zahlen, nichts
Kaputtes landet im Zwischenspeicher.

Das ist auch der Grund, warum Durchgang 0 Punkt 4 (Vollzähligkeit der Liste) bleibt.

## 15. Kaputtes xG wird nur bei glatter Null erkannt — OFFEN

Punkt 12 fängt `xg == 0 and tore > 0` ab. Der Test ist zu scharf: Er erkennt die glatte
Null, nicht das halb erfasste xG. Gemessen am 02.10.2026 an **519 Teams mit mindestens
fünf Spielen**:

| | Teams | Anteil |
|---|---|---|
| xG glatt null (wird abgefangen) | 7 | 1,3 % |
| xG/Tore unter 0,40 (wird **nicht** abgefangen) | 11 | 2,1 % |
| Median xG/Tore aller Teams | 1,05 | |

**Alle 11 stehen in Saison 17308** (Schweizer Amateurliga), neben den 7 Nullen derselben
Liga: 18 von 48 Teams mit unbrauchbarem xG, 7 davon abgefangen. Beispiele: FC Bassecourt
0,02 xG bei 1,25 Toren, CS Chênois 0,18 bei 1,88, FC Monthey 0,52 bei 1,50.

**Wirkung auf die Angriffsstärke** (Saison 17308, überall sonst keine Änderung):

| Team | jetzt | mit Grenze 0,40 | |
|---|---|---|---|
| FC Coffrane | 0,19 | 0,55 | **+182 %** |
| CS Chênois | 0,44 | 1,17 | **+166 %** |
| FC Monthey | 0,54 | 0,93 | **+73 %** |
| FC Sion II (intakt) | 0,90 | 0,87 | −3 % |

Dazu bleiben die 11 Teams im Liga-xG-Nenner und drücken ihn um **4,5 %**, was alle intakten
Teams derselben Liga entsprechend zu stark macht — dieselbe Mechanik wie in Punkt 12, nur
schwächer.

**Die eine Prognose aus dieser Liga ist die, die am deutlichsten danebenlag:**
Wohlen – Schötz, Unter 2,5 mit 55,2 % bei λ 1,04–1,43 — **Ergebnis 1:5**. Schötz hatte
auswärts 3,40 Tore pro Spiel erzielt, die API nennt dafür 1,69 xG (Verhältnis 0,50).
Mit `XG_ANTEIL = 0,70` hat das Modell 70 % auf die 1,69 gelegt statt auf die 3,40 — der
Angriff war halbiert. Verhältnis 0,50 liegt über jeder Grenze von 0,40, wäre also **auch
mit dem Fix nicht erkannt worden**. Der Eintrag in `bilanz.json` bleibt unverändert.

**Der bessere Test ist der auf Liga-Ebene**, nicht je Team. Gesamt-xG gegen Gesamt-Tore,
über alle 29 zwischengespeicherten Ligen gerechnet, trennt scharf:

| Saison | Tore | xG | xG/Tore | |
|---|---|---|---|---|
| 16808 (Nations League) | 1,06 | 0,56 | **0,52** | schon gesperrt (Länderspiele) |
| 17308 (Schweiz) | 1,61 | 0,87 | **0,54** | die Liga mit den 18 Teams |
| 17139 | 1,87 | 1,41 | 0,76 | auffällig |
| 17110 (Eerste Divisie) | 1,85 | 1,64 | 0,89 | Grenzfall |
| 20 weitere Ligen | | | 0,90 – 1,12 | ok |
| 16580 | 0,97 | 1,29 | **1,34** | Gegenrichtung |

Zwischen 0,54 und 0,76 liegt eine deutliche Lücke. Ein Liga-Test würde also beide bekannten
Problemligen fangen, inklusive der halb erfassten Teams, und nicht nur die Nullen.

**Nicht eingebaut.** Das wäre eine Änderung am Rechenweg und braucht eine ausdrückliche
Anweisung. Vorgelegt am 02.10.2026.

## 16. Gegenrichtung: xG über den Toren — OFFEN, klein

Saison 16580 hat **34 % mehr xG als Tore** (0,97 Tore, 1,29 xG). Weil `LIGA_BASIS_XG = 0,40`
dem xG blind 40 % der Liga-Basis gibt, liegt die Torbasis dort **8,8 % über** dem, was
tatsächlich fiel — das drückt systematisch Richtung Über 2,5 und Beide treffen. Die zehn
Prognosen dieser Liga in `bilanz.json` waren alle Unter 2,5 oder Beide treffen und kamen auf
21 Tore gegen 22,3 erwartete (−6,0 %), 7 von 10 getroffen — zu wenige Spiele, um etwas zu
belegen, aber die Richtung passt zur Rechnung.

## 17. Fenster und Form zählen dieselben Spiele doppelt — OFFEN, bekannt

Bei junger Saison füllt das Fenster (Punkt 10) mit den letzten **10** Spielen auf, danach
mischt `strengths()` noch die Form der letzten **6** dazu. Die sechs jüngsten Spiele stecken
damit in beiden Blöcken:

| Saisonspiele | Gewicht Saison | Gewicht 10er-Fenster | Gewicht 6er-Form |
|---|---|---|---|
| 3 | 0,22 | 0,52 | 0,25 |
| 5 | 0,38 | 0,38 | 0,25 |
| 8 | 0,60 | 0,15 | 0,25 |
| 10 | 0,75 | 0,00 | 0,25 |

Bei drei Saisonspielen hängen also 77 % der Teamstärke an Spielen außerhalb der laufenden
Saison, die sechs jüngsten davon doppelt. Das ist keine Falschrechnung, sondern eine
Überschneidung der beiden Gewichte — sie macht die Form bei junger Saison stärker, als
`FORM_ANTEIL = 0,25` vermuten lässt. Nicht angefasst (Gewichte liegen fest).

## 18. Was geprüft wurde und in Ordnung war (02.10.2026)

Damit nicht zweimal gesucht wird:

| geprüft | Ergebnis |
|---|---|
| Dixon-Coles-Faktoren negativ? | kleinster Faktor 0,72 über λ 0,2–4,0; negativ erst ab λ = 14,3 |
| Massenverlust der 11×11-Matrix | höchstens 5,7 · 10⁻³ bei λ 4,0/4,0 |
| `H + D + A` und `O25 + U25` | Abweichung von 1 höchstens 7 · 10⁻¹⁶ |
| Doppelte Team-IDs in `league-teams` (würde eine still verschlucken) | keine, 29 Ligen |
| Fehlende Felder in den `lastx`-Blöcken | keine, 418 Blöcke |
| H2H-Daten: `date_unix` vorhanden, Fremdpaare | 1287 Duelle, alle mit Datum, keine Fremdpaare |
| Seitenlogik `lh = base_h · att_heim · def_ausw` | richtig zugeordnet, kein doppelter Heimvorteil |
| `abstand_markt` in `bilanz.py` gegen `modell.py` | identische Formel, `U25 = −O25` korrekt |
| Margenbereinigung proportional statt Quotenverhältnis | Unterschied im Mittel 0,71 Punkte (Heimsieg), max 2,87; 2 von 32 Spielen wechseln den Rangliste-Block |

Der `lastx`-10er-Block behauptet **immer** 10 Spiele, auch wenn ein Team weniger gespielt
hat — aus der Antwort nicht prüfbar. `saisonfenster()` hebt die Stichprobe deshalb auch dann
auf 10. Betrifft nur neu gegründete Teams.
