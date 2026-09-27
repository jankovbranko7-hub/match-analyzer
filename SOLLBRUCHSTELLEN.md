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
