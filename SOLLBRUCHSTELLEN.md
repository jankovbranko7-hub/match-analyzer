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

## 7. Direkte Duelle mit winzigen Stichproben — INHÄRENT

**Was passiert:** Direkte Duelle gehen mit 10 % in die Gesamttore ein, unabhängig davon, ob es
zwei oder dreißig Duelle sind.

**Wie es sich zeigte:** Celta Fortuna gegen Sabadell hat zwei Duelle mit 4,5 Toren im Schnitt.
Das hob die Torerwartung um rund 7 % — auf Grundlage von zwei Spielen.

**Umgang:** Bei weniger als etwa fünf Duellen den H2H-Einfluss in der Begründung erwähnen.

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
