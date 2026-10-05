# Regeln

## Der Auftrag, wörtlich

> Rechne ein eigenes Python-Modell, nicht die 70/30-Datei. Eingabe nur Pre-Match-xG,
> xG für und dagegen, BTTS-Potential, Over-Potential, Under-Potential. Die API-Zahlen
> müssen fehlerfrei sein: Spiel und Teams exakt prüfen, jedes Feld hier hinschreiben,
> ein fehlendes Feld als fehlt markieren und nie schätzen, die gelesenen Werte ein
> zweites Mal gegen die API-Antwort halten. Erst wenn beides übereinstimmt, kommt der
> Tipp. Ein Tipp pro Spiel: Heimsieg, Auswärtssieg, BTTS Ja, Over 2,5 oder Under 2,5.
> Keine Schwelle aus einer alten Datei.

Das ist die Vorgabe. Alles Folgende setzt sie nur um. **Steht etwas weiter unten im
Widerspruch dazu, gilt der Auftrag** – und das ist zu melden, nicht stillschweigend
aufzulösen.

Der Nutzer schickt ein Datum und Paarungen. Du analysierst **nur diese Spiele** und
antwortest auf **Deutsch**.

## Nichts Altes. Strikt verboten.

**Vom Nutzer am 05.10.2026 noch einmal ausdrücklich eingeschärft.** Verboten ist jede
Berührung mit dem alten System, in jeder Form:

- **Die alten Dateien.** `modell.py` mit den 14 Konstanten (die „70/30-Datei"),
  `modell2.py`, `bilanz.py`, `bilanz.json`, `rueckschau.py`, `pruefung.py`,
  `pruefung2.py`, `bild.py`, `SOLLBRUCHSTELLEN.md`, das alte `CLAUDE.md` und
  `README.md`. Nicht lesen, nicht kopieren, nicht zitieren, nicht hierher holen.
- **Backtesting in jeder Form.** Kein Walk-forward, keine Rückschau, keine
  Ligen-Hälften, keine Log-Likelihood, kein Brier, keine Trefferquote über vergangene
  Spieltage. Dieses System wird nicht an der Vergangenheit gemessen.
- **Jede gesetzte oder angepasste Zahl.** Keine Gewichte, keine Dämpfung, kein
  xG-Anteil, kein Formanteil, kein H2H, kein Dixon-Coles, kein Markt-Anteil, keine
  Schranke, keine Schwelle, keine Sperre.
- **Fremde Repos**, insbesondere `value-bet-screener`.
- **Der Zwischenspeicher des alten Systems.** Die JSON-Dateien unter dessen
  `analyse/daten/` sind alte Dateien, auch wenn darin API-Antworten stehen. Dieses
  System füllt seinen eigenen Zwischenspeicher aus eigenen Abfragen.

**Der einzige Eingang sind die fünf Felder aus der API, frisch geholt.** Fehlt etwas,
steht `FEHLT` und es gibt keinen Tipp – es wird nichts aus einer alten Datei ergänzt.

**Am 05.10.2026 ist genau das passiert und wurde zurückgenommen:** Die Begründung für
eine selbst erfundene 50er-Regel war mit 143 Spielen aus dem Zwischenspeicher des alten
Repos belegt. Der Nutzer hat die Regel gestrichen und die Zahlen dazu. **Wer eine Zahl
in diese Dateien schreibt, muss sagen können, aus welcher frischen API-Antwort sie
kommt.**

## Datenquelle

**Ausschließlich die FootyStats-API.** Key in der Umgebungsvariablen `FOOTYSTATS_API_KEY`
(ersatzweise `APIKEY`). Fehlt er: dem Nutzer sagen, dass er ihn in den Umgebungs-
einstellungen hinterlegen und eine neue Session starten soll. **Nie** darum bitten, den
Key in den Chat zu schreiben. Den Key nie ausgeben, loggen oder committen.

Basis-URL `https://api.football-data-api.com`, Key als Parameter `key=`.
Doku: https://footystats.org/api/documentation

Auf das Stundenlimit achten: nur die Abfragen machen, die für das Spiel nötig sind.
Ein `HTTP 417` ist das Limit – dann warten, nicht sofort erneut abfragen.

## Das Modell

```
python3 analyse/modell.py --liste 2026-10-05     Spiele des Tages mit id
python3 analyse/modell.py 8419375 8469639        diese Spiele rechnen
```

**Fünf Eingaben, mehr nicht:**

| Feld | Endpunkt |
|---|---|
| `team_a_xg_prematch`, `team_b_xg_prematch` | `match` |
| `btts_potential` | `match` |
| `o25_potential` | `match` |
| `u25_potential` | `match` |
| `xg_for_avg_home/away`, `xg_against_avg_home/away` | `league-teams` |

**Rechenweg, zwei Schritte, beide ohne Gewicht:**

1. **Tor-Skala.** Mittel aus dem Pre-Match-xG und „Angriff gegen Abwehr"
   (`xG_für` der einen Seite plus `xG_gegen` der anderen, geteilt durch zwei).
2. **Wahrscheinlichkeits-Skala.** Die beiden λ, deren Poisson die drei Potentiale am
   besten trifft – drei Gleichungen, zwei Unbekannte, kleinste Quadrate. Alle Residuen
   stehen auf derselben 0-bis-1-Skala, deshalb braucht es keine Gewichtung.
3. λ = Mittel aus beiden.

Reine unabhängige Poisson. **Keine gesetzte Zahl im ganzen Rechenweg** – keine Gewichte,
keine Dämpfung, keine Schwelle, keine Sperre, kein Dixon-Coles, kein Liga-Mittel, keine
Form, kein H2H.

**Der Fit aus Schritt 2 liefert immer λ_heim = λ_ausw.** Die drei Potentiale kennen nur
die Summe der Tore, nicht die Seite. Heimsieg gegen Auswärtssieg stammt deshalb
vollständig aus Schritt 1, Schritt 2 wirkt allein auf das Torniveau. Das gehört in die
Begründung, wenn der Tipp Heimsieg oder Auswärtssieg ist.

## Die Prüfung, vor jedem Tipp

`modell.py` macht das selbst und gibt es aus. **Erscheint eine dieser Meldungen, gibt es
keinen Tipp** – auch keinen geschätzten:

1. **Spiel und Teams über die `id`**, nie über den Namen. Namen, Team-`id`s, Liga,
   Anstoß und `status` stehen in der Ausgabe.
2. **Jedes benutzte Feld mit Rohwert.** Fehlt eines, steht `FEHLT`. Es wird **nie**
   ersetzt und **nie** geschätzt. `FEHLT` heißt: **das Feld ist nicht da oder keine
   Zahl.** Eine Null ist eine Zahl und geht als Null weiter. Es wird **nicht** bewertet,
   ob ein Wert plausibel aussieht – dafür bräuchte es eine Regel, und Regeln werden hier
   nicht erfunden.
3. **Gegenprobe: eine zweite, unabhängige Abfrage** derselben Endpunkte, am
   Zwischenspeicher vorbei, Feld für Feld gegen die erste Lesung gehalten. Weicht ein
   Wert ab: **kein Tipp**. Schlägt die zweite Abfrage fehl (Stundenlimit): **kein Tipp**.
   Das kostet eine zusätzliche Abfrage je Endpunkt und Spiel – das ist der Preis dafür,
   dass die Zahl geprüft ist und nicht nur richtig abgeschrieben.
4. **Keine Platzhalter-Erkennung, keine Plausibilitätsprüfung.** Jeder Wert, den die
   API liefert, geht unverändert in den Fit.

   **Am 05.10.2026 hatte ich hier eine Regel eingebaut**, die ich nicht einbauen
   durfte: stehen `btts_potential`, `o25_potential` und `u25_potential` alle drei auf
   exakt 50, galt das als ungesetzter Standard und ging nicht in den Fit. Dazu eine
   zweite: eine exakte Null galt als fehlendes Feld. **Beide waren von mir erfunden und
   nicht verlangt.** Der Nutzer hat sie gestrichen. Nicht wieder einbauen – auch nicht
   gemessen, auch nicht gut gemeint, auch nicht in Prosa.

**Anstoßzeit gegen die Uhr halten.** `date -u` laufen lassen. Ist ein Spiel schon
angepfiffen, ist es keine Prognose – das offen sagen.

## Der Tipp

**Ein Tipp pro Spiel: die wahrscheinlichste dieser fünf Wetten.**

Heimsieg · Auswärtssieg · BTTS Ja · Über 2,5 · Unter 2,5

Keine Schwelle, kein Vorrang, keine Ausnahme. Der Preis entscheidet nicht mit.

## Ausgabe pro Spiel

**Jedes gelesene Feld steht im Chat**, nicht nur im Terminal. Die Tabelle der Eingaben
wird aus der Ausgabe von `modell.py` übernommen, Wert für Wert, inklusive `FEHLT`.

```
## N. Heim – Auswärts
Spiel-id 8419375 · Heim-id 702 · Ausw-id 743 · Saison 16571 · Anstoß 02.10. 22:15 UTC

| Eingabe | Wert |
|---|---|
| team_a_xg_prematch | 1,36 |
| team_b_xg_prematch | 1,66 |
| btts_potential | 50 |
| o25_potential | 43 |
| u25_potential | 57 |
| Heim xg_for_avg_home | 1,36 |
| Heim xg_against_avg_home | 1,46 |
| Ausw xg_for_avg_away | 1,66 |
| Ausw xg_against_avg_away | 1,64 |

Gegenprobe: zweite Abfrage, 20 Werte, identisch.

Erwartete Tore: **1,64 : 1,56**

| Wette | Wahrscheinlichkeit |
|---|---|
| Heimsieg | 40,1 % |
| Auswärtssieg | 36,5 % |
| BTTS Ja | **63,7 %** |
| Über 2,5 | 62,1 % |
| Unter 2,5 | 37,9 % |

**Tipp: BTTS Ja.** <ein bis zwei Sätze aus den fünf Eingabewerten>
Faire Mindestquote: **1,57**.
```

Die Wahrscheinlichkeit des Tipps **fett**. Genau diese fünf Zeilen. Einschränkungen
(fehlendes Feld, angepfiffenes Spiel) gehören in den Tipp-Satz, nie in
einen eigenen Abschnitt.

**Keine Zahl, die nicht aus der Ausgabe von `modell.py` stammt.** Im Zweifel nachsehen
statt schätzen.

## Nichts dazuerfinden

Keine zusätzliche Schwelle, kein Filter, keine Obergrenze, kein Ausschlusskriterium –
auch nicht als gut gemeinter Hinweis, auch nicht in Prosa. Fehlt eine Regel, wird
gefragt, nicht ergänzt.
