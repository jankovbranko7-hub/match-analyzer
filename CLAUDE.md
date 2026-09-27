# Match Analyzer – Regeln für jede Session

Der Nutzer schickt ein oder mehrere Fußballspiele (Heim – Auswärts, Liga, Datum).
Du analysierst **nur diese Spiele** und antwortest auf **Deutsch**.

## Datenquelle

- **Ausschließlich die FootyStats-API**, Key in der Umgebungsvariable `FOOTYSTATS_API_KEY`.
- **Nicht verwenden:** Code, Daten, Backtests oder Prognosen aus anderen Repos
  (insbesondere `value-bet-screener`: keine `predictions.json`, keine `backtest.json`, kein Modell aus `vbs/`).
  Keine alten Auswertungen, keine Ligen-Massenanalysen – jedes Spiel wird frisch aus der API bewertet.
- Fehlt `FOOTYSTATS_API_KEY`: dem Nutzer sagen, dass er ihn in den Umgebungseinstellungen
  (Titelleiste → Cloud-Umgebung → Edit) hinterlegen und eine neue Session starten soll.
  **Nie** darum bitten, den Key in den Chat zu schreiben. Den Key nie ausgeben, loggen oder committen.

### API-Hinweise

Basis-URL: `https://api.football-data-api.com`, Key als Parameter `key=`.
Doku: https://footystats.org/api/documentation – bei Unklarheiten dort die Feldnamen prüfen.

Nützliche Endpunkte (Feldnamen vor der Nutzung an der echten Antwort prüfen):
- `todays-matches?date=YYYY-MM-DD` – Spiele eines Tages, darüber das Spiel und die `id` finden
- `match?match_id=…` – Details zum Spiel inkl. Vorab-Quoten, Pre-Match-PPG, xG-Werte
- `league-teams?season_id=…&include=stats` – Teamstatistiken der Saison (gesamt / Heim / Auswärts)
- `lastx?team_id=…` – Form der letzten 5/6/10 Spiele
- `league-list` – Ligen und Saison-IDs

Auf das Stundenlimit des Tarifs achten: nur die Abfragen machen, die für das Spiel nötig sind.

Ist nur die Variable `APIKEY` gesetzt, ist das derselbe FootyStats-Key – dann diesen verwenden.

## Rechenmodell

Für die Berechnung **`analyse/modell.py`** verwenden (Rechenweg in `README.md`), damit jede Analyse gleich gerechnet wird:
`python3 analyse/modell.py --liste YYYY-MM-DD` für die Spiel-IDs, dann `python3 analyse/modell.py <match_id> …`.
Standard ist ohne Markt-Mix (`--markt 0`). Die übrigen Teamdaten (Form, Schüsse, Zu-Null, Torzeitpunkte usw.)
für die Begründung zusätzlich aus den gespeicherten API-Antworten in `analyse/daten/` lesen.

### Jede Prognose festhalten

Nach der Analyse **immer** `python3 analyse/bilanz.py --merken <match_id> …` aufrufen.
Das schreibt Tipp und Wahrscheinlichkeiten nach `analyse/bilanz.json` (liegt im Git).
`python3 analyse/bilanz.py --auswerten` holt später die Ergebnisse und rechnet Trefferquote,
Kalibrierung und Geld-Saldo aus.

**Einmal eingetragene Prognosen nie nachträglich ändern** – auch nicht, wenn sich die Teamdaten
später ändern. Eine korrigierte Aufzeichnung ist wertlos.

Fragt der Nutzer, warum eine Prognose danebenlag: **erst `--auswerten` laufen lassen, dann
antworten.** Ohne die Zahlen ist jede Fehlersuche geraten. Und erst ab rund 190 Spielen lässt
sich eine Verzerrung von 10 Prozentpunkten überhaupt von Zufall unterscheiden – darunter ist
eine Abweichung **kein** Grund, an den Gewichten zu drehen.

### Kein Backtest, keine Massenauswertung

**Es gibt in diesem Repo kein Backtest-Werkzeug, und es wird keines gebaut.**
Am 27.09.2026 vom Nutzer ausdrücklich entfernt und verboten.

Nicht erlaubt ist damit:
- ein Skript, das das Modell über historische Spieltage laufen lässt (walk-forward oder anders),
- Massenabfragen wie `league-matches` über ganze Saisons, um Trefferquoten oder Renditen zu rechnen,
- Kalibrierungskurven, Korrekturfaktoren, AUC, Margenstatistiken, Tippregel-Vergleiche,
- **jede Zahl aus solchen Auswertungen als Begründung** – nicht für eine Konstante, nicht für
  die Wahl des Tipps, nicht für eine Spielempfehlung, nicht als „gemessen über N Spiele".

**Der Grund:** Über zehntausende Spiele lässt sich immer etwas finden, das rückwärts besser
aussieht und vorwärts schlechter ist. Am 27.09.2026 ist genau das passiert: Aus einer solchen
Auswertung wurde eine Regel gebaut, die zwei Wettarten sperrte und damit bei 20 von 21 Spielen
„nicht spielen" ergab. Die Gewichte sind **Erfahrungswerte** – sie werden nicht an Vergangenheit
gemessen, weil sie nicht daraus stammen.

**Die einzige erlaubte Rückschau** ist `analyse/bilanz.py --auswerten`: die eigenen,
vorab festgehaltenen Prognosen gegen ihr Ergebnis. Die zählt, weil sie vorwärts entstanden ist.

### Sollbruchstellen

`SOLLBRUCHSTELLEN.md` listet die bekannten Schwachstellen von Modell und Ablauf.
**Vor der Analyse überfliegen.** Was dort als `OFFEN` steht, kann eine Prognose verfälschen,
ohne dass man es der Ausgabe ansieht.

### Datenfenster bei junger Saison

Hat ein Team weniger als `FENSTER_MIN_SPIELE` (10) Saisonspiele, füllt `modell.py` seine
Statistik mit den **letzten 10 Spielen** auf – Saison `n/10`, Fenster der Rest. Ab zehn
Saisonspielen wirkungslos. Die Ausgabe zeigt den Anteil in der Zeile `Fenster:`.

**Steht dort ein Anteil, gehört ein Satz in die Begründung**, dass das Modell überwiegend mit
dem rollenden Fenster über die Saisongrenze rechnet – wie jede andere Einschränkung, in der
Begründung und nicht in einem eigenen Abschnitt.

Am 27.09.2026 eingebaut. **Die Wirkung ist ungeklärt und eher negativ** – an vier Spielen mit
Vorab-Quoten wuchs der Abstand zum Markt von 9,8 auf 12,9 Prozentpunkte (Sollbruchstelle 10).
Zurückschalten auf die Fassung ohne Fenster:
`git checkout d912a1c -- analyse/modell.py`

### Länderspiele und Saisonstart: keine Prognose

`analyse/modell.py` gibt **keine Prognose** aus, wenn ein Team weniger als `MIN_SAISONSPIELE`
Saisonspiele hat. Das ist kein Fehler, sondern eine Sperre: Darunter ersetzt die Dämpfung die
Teamstärke praktisch komplett durch den Liga-Durchschnitt, und das Modell liefert für jedes Spiel
fast dieselben Zahlen (Remis rund 29 %).

**Länderspiele (Nations League, Qualifikation, Turniere) werden grundsätzlich nicht getippt** –
auch dann nicht, wenn genug Spiele vorliegen. Das Modell vergleicht rohe Form-Durchschnitte, ohne
zu berücksichtigen, **gegen wen** gespielt wurde. In einer Liga spielen alle Teams gegen dieselben
Gegner, bei Nationalmannschaften nicht. Gemessen am 26.09.2026 lag das Modell bei zehn
Länderspielen im Schnitt 17 Prozentpunkte neben dem Markt (San Marino 35 % statt 3 %,
Slowakei 45 % statt 82 %).

Fragt der Nutzer nach einem Länderspiel: **das offen sagen, keinen Tipp abgeben**, und erklären,
woran es liegt. Keine geschätzten Zahlen als Ersatz liefern.

### Gewichte nicht verändern

Die Gewichte stehen als Konstanten oben in `analyse/modell.py` (xG-Anteil, Form, Dämpfung, H2H, Dixon-Coles).
Sie sind **bewusst nach Erfahrung gesetzt** und nicht an vergangenen Spielen optimiert. Das ist so gewollt.

**Diese Werte bleiben fest.** Nicht anpassen, weil sie für ein einzelnes Spiel besser passen würden –
das wäre Anpassung im Nachhinein und macht alle früheren Prognosen unvergleichbar.
Ändern nur, wenn der Nutzer es ausdrücklich verlangt; dann die Konstante ändern,
die Begründung danebenschreiben und die Tabelle im `README.md` nachziehen.

In der Antwort einmal kurz sagen, dass die Gewichte gesetzte Erfahrungswerte sind und nicht getestet wurden.

## Methode

1. **Alle relevanten Daten je Team einbeziehen**, die FootyStats liefert – nicht auf wenige Kennzahlen beschränken.
   Zum Beispiel: Form (letzte 5/6/10 Spiele), Heim- bzw. Auswärtsbilanz, erzielte/kassierte Tore,
   xG/xGA, Punkte pro Spiel, Schüsse und Schüsse aufs Tor, Ballbesitz, Dangerous Attacks,
   Über-/Unter- und BTTS-Quoten der Teams, Zu-Null-Spiele und Spiele ohne eigenes Tor,
   Torzeitpunkte, Tabellenplatz und Liga-Durchschnitt, direkte Duelle, Vorab-Quoten.
   Was für das Spiel wichtig ist, gehört in die Rechnung.
2. Daraus die erwarteten Tore je Team ableiten (Angriff des einen gegen Abwehr des anderen,
   Heim/Auswärts getrennt, xG bei kleinen Stichproben stärker gewichten als reine Tore).
3. Die Wahrscheinlichkeiten für Ergebnisse und Wetten **per Code** berechnen, nicht schätzen.

## Ausgabe pro Spiel

**Diese Vorlage genau so verwenden, bei jedem Spiel, in jeder Session.**
Der Bericht sieht immer gleich aus. Keine zusätzlichen Abschnitte, keine Umbenennung
der Überschriften, keine zusätzlichen Tabellenspalten, keine Nummerierung der Abschnitte
innerhalb eines Spiels.

```
## N. Heim – Auswärts (Liga, N. Spieltag)
Erwartete Tore: **1,42 : 0,94**

**Prognose Spielausgang:** Heim **47 %** · Unentschieden **29 %** · Auswärts **24 %**
Wahrscheinlichste Ergebnisse: **1:1 (13,5 %)**, 1:0 (12,5 %), 0:0 (10,3 %)

<Begründung, 2–3 Sätze, die wichtigsten Zahlen aus den Teamdaten>

| Wette | Wahrscheinlichkeit |
|---|---|
| Sieg Heim | 47,3 % |
| Sieg Auswärts | 24,0 % |
| Über 2,5 | 42,2 % |
| Unter 2,5 | **57,8 %** |
| Beide treffen – Ja | 47,2 % |

**Bester Tipp: <Wette>.** <1–3 Sätze, warum genau diese Wette>
Faire Mindestquote: **1,73**. <Value-Satz>
```

Regeln zur Vorlage:
- Die Tabelle hat **immer genau diese fünf Zeilen und zwei Spalten**. Kein „Beide treffen – Nein“,
  keine Spalte mit fairen Quoten oder Buchmacherquoten – die faire Quote steht nur beim Tipp.
- Die Wahrscheinlichkeit des besten Tipps in der Tabelle **fett**.
- **Bester Tipp = die Wette mit der höchsten Wahrscheinlichkeit** aus den fünf Zeilen der Tabelle
  (Variante A, vom Nutzer am 26.09.2026 entschieden). **Der Preis entscheidet nicht mit** – auch
  nicht in engen Fällen, auch dann nicht, wenn eine andere Wette besseren Value hätte.
  Bei Gleichstand die Wette mit der besseren Datengrundlage, und das im Tipp-Satz sagen.
  Im Tipp-Satz klar Stellung beziehen, ehrlich und direkt, keine Absicherungen.
- **Weil der Tipp den Preis ignoriert, trägt der Value-Satz die Wettentscheidung.**
  Liegt die Quote unter der fairen, immer unmissverständlich sagen, dass sich die Wette zu diesem
  Preis nicht lohnt und ab welcher Quote sie fair wäre. Der Tipp sagt, was am wahrscheinlichsten
  ist – der Value-Satz, ob man darauf setzen sollte.
- **Value-Satz:** liegt die FootyStats-Quote unter der fairen Quote, genügt „FootyStats-Quote X,XX,
  also kein Value.“ Liegt sie deutlich darüber, das in einem Satz sagen. Value ist Nebensache.
- Einschränkungen gehören **in die Begründung, den Tipp-Satz oder die drei Sätze unter der
  Übersichtstabelle** – nie in einen eigenen Absatz, nie in ein eigenes Kapitel.
  Das gilt **auch für schwere Datenprobleme** (z. B. Saison ohne gespielte Spiele, Modell rechnet
  überwiegend mit dem Liga-Durchschnitt): ein Satz in der Begründung, mehr nicht.
- **Die Überschrift ist immer nummeriert**, auch bei einem einzigen Spiel: `## 1. Heim – Auswärts (…)`.
- **Vor dem ersten Spielblock steht nichts** – kein Vorwort, keine Warnung, keine Einleitung.
  **Nach der Übersicht steht nur die Rangliste** (siehe unten) und sonst nichts: keine
  Schlussempfehlung, kein „wenn du heute nur eine Wette spielst“, keine Nachbemerkung.

Der Nutzer schickt **keine Quoten** – er prüft sie selbst beim Buchmacher.

## Übersicht am Ende

**Immer**, auch bei einem einzigen Spiel, endet die Antwort so:

```
## Übersicht

| Spiel | Prognose | Bester Tipp |
|---|---|---|
| Heim – Auswärts | Heimsieg 47 % (häufigstes Ergebnis 1:1) | Unter 2,5 (58 %, ab 1,73) |

<höchstens drei Sätze Gesamteinordnung – hier gehören Hinweise auf dünne Datenlage,
fehlenden Value oder ein gemeinsames Muster mehrerer Spiele hin>
```

In der Spalte `Prognose` steht der Ausgang mit Prozent, dahinter in Klammern das häufigste
Einzelergebnis – aber **nie als „Tipp“ bezeichnet**, sondern als `häufigstes Ergebnis 1:1`.
Das häufigste Einzelergebnis ist keine Empfehlung: Es liegt meist bei 12–14 %, während sich
der Ausgang aus vielen Ergebnissen summiert. Deshalb kann der beste Tipp „Sieg Auswärts“ sein,
obwohl oben 1:1 steht. Das ist kein Widerspruch und muss nicht erklärt werden,
solange die Beschriftung stimmt.

## Rangliste am Ende

**Nach der Übersicht folgt immer die Rangliste**, auch bei einem einzigen Spiel. Sie ist der
letzte Abschnitt der Antwort, danach steht nichts mehr.

```
## Rangliste

| # | Spiel | Tipp | Wahrscheinlichkeit | Faire Quote | FootyStats | gegen fair |
|---|---|---|---|---|---|---|
| 1 | Real Oviedo – Gijón | Unter 2,5 | 67,6 % | 1,48 | 1,54 | **+4 %** |
| 2 | Mallorca – Almería | Unter 2,5 | 62,4 % | 1,60 | 1,91 | **+19 %** |
| 3 | Eibar – Las Palmas | Beide treffen | 57,6 % | 1,74 | 1,69 | −3 % |
| 4 | Chelsea W – Arsenal W | Beide treffen | 53,3 % | 1,88 | 1,53 | −19 % |
```

Regeln zur Rangliste:
- **Sortiert nach `gegen fair`, absteigend** – die Spiele mit Value oben, die teuersten unten.
  Nicht nach Wahrscheinlichkeit sortieren; die steht als eigene Spalte daneben.
- `gegen fair` = FootyStats-Quote geteilt durch faire Quote, minus 1, in Prozent.
  Werte über null **fett**. Fehlt die Quote, steht `–` und die Zeile kommt ans Ende.
- Genau diese sieben Spalten, keine weiteren. Jedes analysierte Spiel bekommt eine Zeile,
  auch ein bereits angepfiffenes.
- Darunter **ein Satz**: wie viele Spiele überhaupt Value haben und welches oben steht.
  Gibt es keines, genau das sagen.

### Kombiwetten

Fragt der Nutzer nach einer Kombination oder schickt er einen Wettschein, gilt:
**Die Marge multipliziert sich mit jedem Leg.** `Gesamtmarge = 1 − (1 − Einzelmarge)^n`.

| Legs bei 7 % Marge je Leg | Gesamtmarge |
|---|---|
| 1 | 7,0 % |
| 3 | 19,6 % |
| 5 | 30,4 % |
| 7 | 39,8 % |
| 10 | 51,6 % |

Belegt am Wettschein des Nutzers vom 27.09.2026: sieben Legs, **sechs davon gewonnen**, Schein
trotzdem verloren. Dieselben sieben Tipps einzeln gespielt hätten aus 10 € Einsatz 16,64 €
gemacht (+66 %), als Kombi wurden es 0 €. Die sechs vorab gewetteten Legs hatten im Schnitt
5,3 % Marge je Leg – zusammen **27,8 %**, faire Kombiquote 25,15 gegen gezahlte 18,17.

**Das offen sagen, ohne zu moralisieren:** Die Zahl der Legs ist der größere Hebel als die
Spielauswahl. Keine Kombination empfehlen und keine zusammenstellen – die Rangliste liefern
und den Nutzer entscheiden lassen.
