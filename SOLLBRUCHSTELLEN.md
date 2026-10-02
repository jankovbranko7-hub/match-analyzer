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

## 15. Kaputtes xG wird nur bei glatter Null erkannt — BEHOBEN am 02.10.2026

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

**Eingebaut am 02.10.2026 auf ausdrückliche Anweisung des Nutzers** als `LIGA_XG_MIN = 0,65`
(Grenze in der Mitte der Lücke zwischen 0,54 und 0,76) und `LIGA_XG_WARN = 0,85` (nur
Hinweis, kein Eingriff). Liegt eine Liga unter 0,65, entfallen `XG_ANTEIL` und
`LIGA_BASIS_XG` **für die ganze Liga** – auch für Teams mit gefüllt aussehendem Feld.

**Gegenprobe an 114 zwischengespeicherten Spielen, beide Fassungen mit denselben
Eingangsdaten gerechnet:**

| | |
|---|---|
| völlig unverändert | **113** (99,1 %) |
| verändert | 1 – Wohlen – Schötz, Saison 17308 |
| Tipp gewechselt | 1 – Beide treffen → Über 2,5 |
| Sperre gewechselt | keine |

Der Eingriff trifft also genau die Liga, für die er gebaut ist, und keine andere.

**Was die Gegenprobe NICHT zeigt:** ob der Tipp vor dem Spiel anders ausgefallen wäre. Die
zwischengespeicherte Teamstatistik wurde am 30.09. um 22:42 UTC geholt, Anstoß war 18:15 –
sie enthält das 1:5 also schon. Das λ von Schötz steigt in dieser Gegenprobe von 1,62 auf
2,62, aber ein Teil davon ist das Spiel selbst. Der Schnappschuss von vorher existiert nicht
mehr, also ist es nicht messbar. Die Aufzeichnung in `bilanz.json` bleibt unverändert.

**Nebenbei behoben:** `term()` in `strengths()` teilte auch dann durch das Liga-xG, wenn das
xG-Gewicht null war (`0 * (xg/0)`). Bei einer Liga ganz ohne xG-Felder wäre das ein
`ZeroDivisionError` gewesen. Jetzt wird der Term bei Gewicht null gar nicht erst gebildet.
Dieselbe Stelle ist der Grund, warum die Sperre jetzt `L['xhome']` nur noch prüft, wenn das
Liga-xG überhaupt verwendet wird.

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

## 19. `--auswerten` verwarf geholte Ergebnisse bei einem API-Fehler — BEHOBEN am 02.10.2026

Dieselbe Familie wie Punkt 13 und 14, dritte Stelle. Die Schleife in `bilanz.py`, die die
fehlenden Ergebnisse nachholt, hatte **kein** `try/except`, und `speichern(eintraege)` steht
**hinter** der Schleife:

```
for e in eintraege:
    if e['ergebnis'] is None:
        m = M.hole("match", ...)     # hier bricht es ab
        ...
speichern(eintraege)                 # wird nie erreicht
```

**Wirkung:** Bei 30 offenen Spielen und dem Stundenlimit beim zehnten waren die neun bereits
geholten Ergebnisse weg und mussten beim nächsten Lauf erneut abgefragt werden — in derselben
Stunde also gar nicht. Weil `--auswerten` mit `neu=True` arbeitet, zählt jeder offene Eintrag
bei jedem Lauf gegen das Limit.

**Behoben:** je Eintrag abfangen, das Spiel bleibt offen, die übrigen werden weiter geholt, und
`speichern()` wird erreicht. Nicht abrufbare Spiele werden am Anfang der Auswertung aufgelistet.
Nachgestellt mit einer Testbilanz und einer API, die nur `success: false` antwortet: alle drei
Spiele gemeldet, Bilanz danach unbeschädigt. Keine Zahl verändert.

## 20. Die Begründung der Saisonspiel-Sperre beschrieb einen Lauf ohne Datenfenster — KORRIGIERT am 02.10.2026

Die Tabelle in `CLAUDE.md` zur Trennschärfe bei `MIN_SAISONSPIELE` (13,0 Punkte bei einem
Spiel, 28,2 bei drei, 49,6 bei zwölf) steigt mit der Spielzahl — so wirkt die Dämpfung,
**wenn kein Datenfenster läuft**. Im echten Lauf liegt immer ein `lastx`-10er-Block vor,
`saisonfenster()` hebt die Stichprobe auf 10, und `DAEMPFUNG_K = 5` greift dann fast nicht
mehr. Gemessen an zwei synthetischen Heimteams (2,6 gegen 0,7 Tore), Form abgeschaltet:

| Saisonspiele | ohne Fenster | Fenster bestätigt die Saison | Fenster zeigt Liga-Schnitt |
|---|---|---|---|
| 1 | 5,0 Punkte | **24,1** | 2,5 |
| **3 (Grenze)** | 11,2 Punkte | **24,1** | 7,4 |
| 8 | 21,6 Punkte | **24,1** | 19,4 |
| 12 | 26,1 Punkte | 26,1 | 26,1 |

Die mittlere Spalte ist **flach** — 24,1 Punkte von einem bis acht Saisonspielen, 92 % der
Trennschärfe von zwölf Spielen. Die absoluten Werte sind nicht mit der Tabelle vom 01.10.
vergleichbar (anderer synthetischer Aufbau), der Verlauf schon.

**Folge:** Unter drei Saisonspielen ist nicht die Dämpfung das Problem, sondern die Herkunft
der Zahlen. Bei 3 Saisonspielen liegt die Trennschärfe je nach Fensterinhalt zwischen 7,4 und
24,1 Punkten. Die Sperre ist weiter sinnvoll — sie schützt vor einer Prognose, die zu 70 % auf
Spielen außerhalb der Saison steht —, aber aus einem anderen Grund als dokumentiert. Grenze
unverändert bei 3, Begründung in `CLAUDE.md` richtiggestellt. Hängt mit Punkt 17 zusammen.

## 21. Zwei Dinge, die bleiben wie sie sind — OFFEN, bewusst

**Ein Spiel kann in zwei Tageslisten stehen.** `todays-matches?date=` folgt nicht dem
UTC-Tag. Am 02.10.2026 geprüft: `date=2026-10-03` liefert 82 Spiele, zwei davon stoßen am
**04.10. um 00:00 UTC** an (Tulsa – Sacramento, Aragua – Marítimo). Dieselben zwei stehen
auch in `date=2026-10-04`. Es geht also nichts verloren, aber **ein Spiel kann doppelt in
die Liste geraten**, wenn zwei aufeinanderfolgende Tage abgefragt werden. `bilanz.py --merken`
fängt den Doppeleintrag ab (`if any(e['id'] == mid …)`), die Antwort an den Nutzer nicht —
dafür gibt es Durchgang 4, erster Punkt. **Spiel-IDs vor der Analyse über die `id` entdoppeln.**

**`p_tipp` ist nach oben verzerrt.** Der beste Tipp ist das Maximum aus fünf Wetten
(Variante A). Das Maximum mehrerer verrauschter Schätzungen liegt systematisch über dem
wahren Wert — je mehr Rauschen, desto mehr. Die erwartete Trefferzahl in `--auswerten`
(aktuell 47,6 bei 78 Spielen) ist deshalb eher zu hoch angesetzt, und ein Rückstand darauf
wäre **teils Auswahl und nicht Fehlkalibrierung**. Nicht korrigierbar ohne die wahren
Wahrscheinlichkeiten, also nicht korrigiert. Praktisch derzeit ohne Belang: die tatsächliche
Zahl liegt mit 49 **über** der erwarteten, der Verzerrung also entgegen.

## 22. Die fünf Wetten standen nicht auf derselben Skala — TEILS BEHOBEN am 02.10.2026

Von 78 aufgezeichneten Tipps waren **45 „Beide treffen" (58 %)** und **kein einziger
„Sieg Auswärts"**. Das ist keine Aussage über Spiele, sondern Arithmetik: Die fünf Wetten
starten auf völlig verschiedenen Basisraten. Bei einem Durchschnittsspiel der fünf geprüften
Ligen:

| Wette | Basisrate |
|---|---|
| Sieg Auswärts | 29,6 – 30,8 % |
| Sieg Heim | 42,4 – 46,5 % |
| Unter 2,5 | 31,6 – 51,2 % |
| Über 2,5 | 48,8 – 68,4 % |
| **Beide treffen** | **53,8 – 68,6 %** |

Über 32 Spiele lag der **höchste** Wert von Sieg Auswärts bei 49,8 %, der **niedrigste** von
Beide treffen bei 43,4 %. Sieg Auswärts kann das argmax also praktisch nie gewinnen.

**Der schwerere Teil: die gewählten Wetten sind die zerbrechlichsten.** Bei 10 % Fehler auf
beide λ bewegt sich Über/Unter 2,5 um **6,22** Punkte, Beide treffen um **4,73**, Sieg Heim um
**1,01**, Sieg Auswärts um **0,54**. Die alte Regel wählte 30 von 32 Tipps aus den drei
oberen Zeilen — also systematisch dort, wo ein Modellfehler am stärksten durchschlägt.

**Was dagegen NICHT hilft** (beides gemessen, beides verworfen):

| Regel | Wahrsch. | Abstand Markt |
|---|---|---|
| höchste Wahrscheinlichkeit | 61,07 % | 4,14 |
| Abweichung vom Liga-Schnitt | 49,7 % | 5,04 |
| Abweichung je Punkt Empfindlichkeit | 44,3 % | 4,92 |

Beide kosten 11 bis 17 Punkte Wahrscheinlichkeit und entfernen sich dabei **weiter** vom
Markt. Die hohe Basisrate von Beide treffen ist kein Fehler, sondern der Grund, warum es
öfter eintritt; sie herauszurechnen heißt, absichtlich die unwahrscheinlichere Wette zu
nehmen (Sieg Auswärts in 13 bzw. 18 von 32 Spielen, bei Wahrscheinlichkeiten um 35 %).

**Eingebaut wurde deshalb nur der Gleichstand-Entscheid** (`GLEICHSTAND_PUNKTE = 2.0`):
Liegen mehrere Wetten unter 2 Punkten auseinander, gewinnt die unempfindlichste. Kosten
0,14 Punkte Wahrscheinlichkeit, Marktabstand 4,14 → 4,01 (**t = −0,86, im Zufallsbereich** —
der Gewinn ist nicht belegt). An 114 Spielen: Wahrscheinlichkeiten überall identisch, 31
Gleichstände, 10 Tipps gewechselt, alle von Über/Unter 2,5 zu Beide treffen oder Sieg Heim.

**OFFEN bleibt die Schieflage selbst.** Außerhalb des Gleichstands wählt das Modell weiter
nach Wahrscheinlichkeit und landet damit weiter überwiegend bei Beide treffen. Die Bilanz
misst also auch künftig überwiegend, wie gut das Modell „Beide treffen" vorhersagt (dort
41 getroffene gegen 44,0 erwartete). Das ist die Folge von Variante A und keine Schwäche der
Rechnung — aber man muss es wissen, wenn man die Trefferquote liest.

## 23. Das Modell streute zu weit — BEHOBEN am 02.10.2026

Der erste Fund dieser Session, der die **Genauigkeit** betrifft und nicht die Verlässlichkeit.
Gemessen an 108 zwischengespeicherten Spielen mit vollständigen Vorab-Quoten, Modell-λ gegen
margenbereinigtes Markt-λ:

| | Bias | Steigung | t gegen 1 |
|---|---|---|---|
| Heimtore | −0,013 | 0,842 | **−3,15** |
| Auswärtstore | −0,014 | 0,857 | −2,27 |
| Tore gesamt | −0,027 | **0,809** | **−3,54** |
| Differenz (Ausgang) | +0,001 | 0,879 | −2,13 |

**Das Niveau war richtig:** Bias praktisch null, Heimvorteil 1,304 gegen 1,307, Gesamttore
2,889 gegen 2,916. Falsch war die **Spreizung** – bei hohen Modellwerten sagte der Markt
niedrigere und umgekehrt. Drei bis dreieinhalb Standardfehler.

**Die Ursache ist nicht trennbar, die Antwort schon.** Eine Steigung unter 1 entsteht sowohl,
wenn das Modell wirklich übertreibt, als auch, wenn es nur verrauschter ist als der Markt
(Regressionsverdünnung). In beiden Fällen gilt derselbe Satz aus der Statistik: eine
verrauschte Schätzung gehört zum Mittel gezogen, sonst ist ihr Fehler größer als nötig.

**Eingebaut:** `LAMBDA_DAEMPFUNG = 0.85`, angewandt nach dem H2H-Faktor und vor dem Markt-Mix.
Gedämpft wird nur das Modell-λ, nie das Markt-λ.

| | vorher | jetzt |
|---|---|---|
| λ-Fehler gegen Markt | 0,303 Tore | **0,291** |
| Abstand zum Markt beim Tipp | 4,18 | **3,63** (paarweise t = **−3,34**) |
| Wahrscheinlichkeit des Tipps | 61,24 % | 60,89 % (−0,35 Punkte) |
| größter Marktabstand | 24,0 | **18,7** |
| Spiele über der 8-Punkte-Grenze | 11 von 108 | **9** |
| Tipp gewechselt | – | 7 von 114 |
| Sperren gewechselt | – | 0 |

Praktisch heißt das: weniger Spiele landen wegen „Markt widerspricht stark" im unteren Block
der Rangliste, und die Extremfälle verschwinden. Boreham Wood – Altrincham stand vorher bei
Sieg Heim mit **−13,8** Punkten Marktabstand und steht jetzt bei Beide treffen mit **−2,4**.

**Warum 0,85 und nicht 0,77:** Der kleinste λ-Fehler liegt bei 0,77, die gemessenen Steigungen
bei 0,81 bis 0,88. 0,85 liegt am oberen Rand, holt vier Fünftel des Gewinns (4,18 → 3,63 von
3,41 möglich) und greift so wenig ein wie möglich.

**OFFEN: was die Messung nicht zeigt.** Ob die Trefferquote steigt, ist damit nicht belegt —
dafür bräuchte es den Vergleich gegen echte Ergebnisse über vergangene Spieltage, also den
Backtest, den dieses Repo verbietet. Und der Marktabstand verbessert sich zum Teil deshalb,
weil auf den Markt hin gedämpft wird; diese Zahl ist also teilweise zirkulär. **Nicht**
zirkulär ist der Befund selbst: eine Steigung von 0,81 bei t = −3,5 ist unabhängig davon, was
man danach damit macht.

Die Aufzeichnungen in `bilanz.json` bleiben unverändert — alle 79 sind vor dieser Änderung
entstanden und mit der alten Spreizung gerechnet. Ab der nächsten Prognose ist die Bilanz
deshalb **nicht mehr mit den 79 alten vergleichbar**, was die λ betrifft.

## 24. Die λ-Dämpfung: Befund richtig, Schlussfolgerung falsch — ZURÜCKGENOMMEN am 02.10.2026

Am 02.10.2026 eingebaut (Punkt 23) und am selben Tag zurückgenommen, nachdem der Nutzer die
Rückschau auf echte Ergebnisse erlaubt hat. **Die Episode ist der Grund, warum der Marktabstand
ein Warnsignal bleibt und nie eine Zielfunktion wird.**

**Der Befund war echt.** Modell-λ gegen Markt-λ an 108 Spielen: Steigung 0,809 für die
Gesamttore bei t = −3,54. Das Modell streut messbar weiter als der Markt, bei korrektem Niveau.

**Die Schlussfolgerung war falsch.** Walk-forward über **2136 Spiele aus 12 reifen Ligen**,
Teamdaten je Spiel ausschließlich aus Spielen davor gerechnet (Tore und Per-Spiel-xG aus
`league-matches`), bewertet nur Spiele mit mindestens 10 Vorspielen je Team, damit das
Datenfenster aus ist und kein Spiel sich selbst bewertet:

| k | LogLik je Spiel | Trefferquote | Brier |
|---|---|---|---|
| 0,65 | −2,91952 | 59,1 % | 0,23316 |
| 0,75 | −2,91621 | 60,1 % | 0,23278 |
| 0,85 | −2,91396 | 60,0 % | 0,23253 |
| **1,00** | **−2,91260** | 60,0 % | **0,23240** |
| 1,05 | −2,91270 | 59,9 % | 0,23242 |

Beste Log-Likelihood und bester Brier bei **k = 1,00**, Trefferquote flach. Paarweise 0,85
gegen 1,00: −2,90 LL gesamt, **t = −1,26** – im Zufallsbereich, aber mit negativem Vorzeichen,
und **9 von 12 Ligen bevorzugen einzeln 1,00**.

**Näher am Markt heißt nicht näher an der Wirklichkeit.** Der Marktabstand misst, wie weit
Modell und Buchmacher auseinanderliegen – nicht, wer recht hat. Auf ihn hin zu optimieren ist
derselbe Fehler wie der vom 27.09.2026, nur mit dem Markt statt der Vergangenheit als Ziel.

### Was dieselbe Messung über das Modell sagt — und das ist der eigentliche Ertrag

2136 Spiele, strikt vorwärts, k = 1,00:

| | tatsächlich | erwartet | z |
|---|---|---|---|
| Tipps getroffen | 1282 (60,0 %) | 1275,4 (59,7 %) | **+0,29** |
| Sieg Heim | 943 | 911,4 | +1,41 |
| Sieg Auswärts | 621 | 647,9 | −1,29 |
| Über 2,5 | 1079 | 1071,9 | +0,32 |
| Unter 2,5 | 1057 | 1064,1 | −0,32 |
| Beide treffen | 1162 | 1144,5 | +0,77 |
| Tore | 5753 | 5769 | **−0,3 %** |

**Das Modell ist kalibriert.** Keine der fünf Wetten weicht signifikant ab, die Torzahl stimmt
auf 0,3 %, die Trefferquote auf 0,3 Prozentpunkte. Die 78 Spiele in `bilanz.json` deuteten
darauf hin, die 2136 belegen es. Wer die Gewichte anfassen will, hat hier die Messlatte:
**sie sind nicht nachweisbar verzerrt.**

### Der Gleichstand-Entscheid wurde mitgeprüft

Auf den **557** Spielen, in denen er eingriff:

| Auswahl | Treffer | erwartet | z |
|---|---|---|---|
| nur argmax | 356 | 324,8 | +2,70 |
| **mit Gleichstand** | **365** | 323,0 | **+3,63** |

**+9 Treffer** bei 99 Spielen mit verschiedenem Tipp. McNemar: argmax allein richtig 45×,
Gleichstand allein richtig 54×, **z = +0,90 – nicht signifikant.** Er schadet nicht, kostet
0,35 Punkte Wahrscheinlichkeit, und das Vorzeichen stimmt. **Er bleibt**, aber er ist nicht
bewiesen.

### Der Walk-forward liegt nicht im Repo

Die Erlaubnis vom 02.10.2026 galt für **diese Messung**, nicht für ein dauerhaftes
Backtest-Werkzeug. Die Skripte (`walk.py`, `score.py`, `sig.py`) lagen im Arbeitsverzeichnis
der Session und sind mit ihr weg. Wer sie wieder braucht, baut sie neu – oder der Nutzer sagt,
dass sie ins Repo sollen. Der Aufbau steht oben beschrieben: `league-matches` je Liga, nach
`date_unix` sortieren, Teamdaten je Spiel nur aus Spielen davor, mindestens 10 Vorspiele je
Team, dann Log-Likelihood der echten Ergebnisse unter der Dixon-Coles-Matrix.

## 25. Alle acht Gewichte an echten Ergebnissen geprüft — KEINES GEÄNDERT, Grenze korrigiert

Am 02.10.2026, nachdem der Nutzer die Rückschau erlaubt hatte. Walk-forward über **2136 Spiele
aus 12 reifen Ligen**, jede Konstante einzeln durchgefahren, **getrennt auf zwei unabhängigen
Ligen-Hälften** – damit sich Anpassung von echtem Gewinn unterscheiden lässt.

| Konstante | jetzt | beste in A | beste in B | |
|---|---|---|---|---|
| `XG_ANTEIL` | 0,70 | 0,4 | 0,6 | uneinig |
| `LIGA_BASIS_XG` | 0,40 | 0,2 | 0,6 | uneinig |
| `SEITE_K` | 6 | 2 | 20 | uneinig |
| `DAEMPFUNG_K` | 5 | 12 | 3 | uneinig |
| `FORM_ANTEIL` | 0,25 | 0,4 | 0,25 | uneinig |
| `FORM_DAEMPFUNG_K` | 3 | 3 | 1 | uneinig |
| Formfenster | 6 | 4 | 8 | uneinig |
| `DIXON_COLES_RHO` | −0,07 | −0,025 | −0,07 | uneinig |

**Acht von acht widersprechen sich.** Das ist die Signatur von Anpassung an Rauschen. Die
Regel „nicht an vergangenen Spielen optimieren" ist damit nicht länger nur eine Haltung,
sondern gemessen. **Kein Gewicht wurde geändert.**

### Der scheinbare Ausreißer und was er wirklich war

`XG_ANTEIL` war die einzige Konstante, bei der **beide** Hälften in dieselbe Richtung zeigten
(0,4 und 0,6, beide unter 0,70). Auf alle 12 Ligen gerechnet war 0,55 gegen 0,70 sogar
**+12,10 LL bei t = +3,60**, also klar signifikant. Das sah nach einem echten Fund aus.

Die Kontrolle war, das xG je Liga gegen die Tore zu halten. Ergebnis: **eine** Liga fiel
heraus – Saison 16015 mit einem Verhältnis von **0,66**, also knapp über der damaligen Grenze
`LIGA_XG_MIN = 0,65`. Ohne diese Liga:

| Menge | Optimum | 0,55 gegen 0,70 |
|---|---|---|
| alle 11 guten Ligen | 0,6 | +1,81 LL, t = +0,66 |
| gute Ligen, Hälfte A | 0,6 | +0,92 LL, t = +0,47 |
| gute Ligen, Hälfte B | 0,6 | +0,90 LL, t = +0,46 |

Das Optimum ist zum ersten Mal in allen Mengen **gleich**, und der Unterschied zu 0,70 ist
nicht mehr signifikant. **Eine von zwölf Ligen hat gereicht, um ein Gewicht um 0,2 bis 0,3
falsch aussehen zu lassen.**

**Die Lehre:** Sieht eine Konstante schlecht aus, erst nach der kaputten Liga suchen, nicht
am Gewicht drehen.

### Was geändert wurde: `LIGA_XG_MIN` 0,65 → 0,85

Die 0,65 stammten aus einer Lücke in 29 Ligen-Momentaufnahmen (0,54 / 0,76), waren also nie
an Ergebnissen geprüft. Jetzt sind sie es:

| Saison 16015 allein, 161 Spiele | LogLik je Spiel | Trefferquote | Brier |
|---|---|---|---|
| xG mit 0,70 (Grenze 0,65) | −2,69346 | 64,0 % | 0,22492 |
| **xG aus (Grenze 0,85)** | **−2,55881** | **65,8 %** | **0,21080** |

Über alle 2136 Spiele: LogLik je Spiel −2,91260 → **−2,90246**, Brier 0,23240 → **0,23134**,
paarweise **+21,68 LL bei t = +2,91 – signifikant.**

**Grenze 0,95 wäre zu weit:** fasst vier Ligen, +1,75 LL bei t = +0,18, Trefferquote fällt von
59,3 auf 58,1 %. Die Verhältnisse der zwölf Ligen lagen bei 0,66 und dann erst wieder bei
0,91 bis 1,12 – 0,85 liegt in der Lücke, 0,95 schon im guten Bereich. `LIGA_XG_WARN` deshalb
jetzt 0,95.

An den 114 zwischengespeicherten Spielen: **alle 114 völlig unverändert**, 0 Tippwechsel,
0 Sperrenwechsel – die betroffenen Ligen kommen dort nicht vor. Von den 29
Ligen-Momentaufnahmen wird zusätzlich Saison 17139 (0,76) verworfen; 16504, 17110, 17227 und
17279 (0,89 bis 0,93) bekommen nur den Hinweis.
