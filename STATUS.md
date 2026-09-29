# Stand

Zuletzt aktualisiert: 29.09.2026. Diese Datei ist die Übergabe an die nächste Session –
sie sagt, wo alles steht. Die Regeln stehen in `CLAUDE.md`, der Rechenweg in `README.md`,
die Schwachstellen in `SOLLBRUCHSTELLEN.md`.

## Als Erstes in einer neuen Session

```
python3 analyse/bilanz.py --auswerten
```

Das holt die Ergebnisse der offenen Spiele und zieht die Bilanz. **Vor jeder Antwort auf
die Frage „warum lag die Prognose daneben" zwingend zuerst ausführen.**

## Modellstand

**Eingefroren.** Letzte und einzige Änderung am Rechenweg: Datenfenster
(`FENSTER_MIN_SPIELE = 10`) am 27.09.2026.

**Wie es dazu kam – die Schüsse waren der Auslöser.** Der Nutzer schickte Screenshots seiner
FootyStats-Seite. Dort standen für Manchester United W **9,71 Schüsse pro Spiel**, die API
lieferte für dieselbe Saison **3,33** – fast das Dreifache, dazu 1,4 gegen 0,00 Heimtore und
10 % gegen 0 % Zu-Null. Das war der Beweis, dass Website und API **verschiedene
Grundgesamtheiten** zeigen: die Seite ein rollendes Fenster über 7 bis 10 Spiele, die API nur
die drei Spiele der laufenden Saison. Daraus entstand das Datenfenster (`SOLLBRUCHSTELLEN.md`
Punkt 10).

**Eine Schuss-Komponente selbst wurde geprüft und nicht eingebaut.** Zwei Gründe: FootyStats
liefert 18 Schuss-Felder, alle für das eigene Team – **kein einziges für gegnerische Schüsse**,
also ließe sich nur der Angriff stützen, die Abwehr nicht. Und durchgerechnet änderte
`SCHUSS_ANTEIL` von 0,15 bis 0,80 **bei keinem von 21 Tipps** den besten Tipp. `SCHUSS_ANTEIL`
existiert im Code nicht.

| Konstante | Wert |
|---|---|
| `XG_ANTEIL` | 0,70 |
| `LIGA_BASIS_XG` | 0,40 |
| `SEITE_K` | 6 |
| `DAEMPFUNG_K` | 5 |
| `FORM_ANTEIL` / `FORM_DAEMPFUNG_K` | 0,25 / 3 |
| `H2H_ANTEIL` / `H2H_MAX_JAHRE` / `H2H_DAEMPFUNG_K` | 0,10 / 3 / 3 |
| `DIXON_COLES_RHO` | −0,07 |
| `MARKT_ANTEIL` | 0,0 (aus) |
| `MIN_SAISONSPIELE` | 3 |
| `FENSTER_MIN_SPIELE` | 10 |
| `CACHE_STUNDEN` | 6 |

Frühere Fassungen: `d912a1c` (ohne Datenfenster), `605fab4` (mit).
Zurückschalten: `git checkout <commit> -- analyse/modell.py`

## Bilanz

| | |
|---|---|
| Prognosen gesamt | 71 |
| ausgewertet | 70 |
| **offen** | **0** |
| abgesagt | 1 (New York RB – St. Louis City) |
| Treffer | 46 gegen 42.8 erwartete (z = +0.78, Zufallsbereich) |
| Trefferquote | 66.7 % (Modell sagte 62.0 %) |
| Tore | 196 gegen 199.9 erwartete (−2.0 %) |
| Geld, alle Tipps zu 10 € | +5 € auf 690 € Einsatz (+0.8 %) |
| Geld, nur die 15 mit Value | +17 € auf 150 € Einsatz |

Aussagekraft: Bei 70 Spielen wäre erst eine Verzerrung ab rund 17 Prozentpunkten
nachweisbar. Für 10 Punkte braucht es rund 190 Spiele. **Bis dahin ist keine Abweichung ein
Grund, an den Gewichten zu drehen.**

## Offene Prognosen

Keine. Alles ausgewertet, Stand 29.09.2026 abends. Zuletzt dazugekommen: die zehn Spiele
der National League vom 29.09. (6 von 10 getroffen bei 5,9 erwarteten).

## Wettschein des Nutzers vom 28.09. – verloren

4er-Kombi, Einsatz 20 €, Kombiquote 7,26. **Drei Legs getroffen, eines nicht:**

| Leg | Tipp | Ergebnis | |
|---|---|---|---|
| Bor – Metalac GM | Unter 2,5 | 0:2 | getroffen |
| Leganés – Castellón | Unter 2,5 | 0:2 | getroffen |
| Bnei Raina – Ra'anana | Beide treffen | 1:2 | getroffen |
| Kiryat Gat – Kafr Qasim | Beide treffen | 0:1 | **verloren** |

Damit ist der Schein weg. **Das ist die dritte Bestätigung derselben Rechnung:** am 27.09.
sechs von sieben Legs getroffen und trotzdem 0 €, jetzt drei von vier. Einzeln gespielt
hätten diese vier Tipps aus 20 € Einsatz rund 25 € gemacht.

## Was in dieser Session gelernt wurde

1. **Die Tabelle entscheidet, nicht die Prosa.** Warnungen im Fließtext werden überlesen.
   Alles Entscheidungsrelevante gehört in eine Spalte.
2. **`gegen fair` misst bei dünner Datenlage das eigene Rauschen**, nicht Value. Deshalb hat
   die Rangliste zwei Blöcke.
3. **FootyStats-Quoten sind nicht die Quoten des Nutzers** – im Median 6,1 % darüber,
   im Extremfall 17,5 %.
4. **Die Marge multipliziert sich je Leg.** Sieben Legs, sechs gewonnen, Schein verloren.
5. **Der Backtest ist verboten.** Die einzige erlaubte Rückschau ist `bilanz.py --auswerten`.
6. **Vor dem Rechnen die Uhr prüfen.** Am 29.09. wurden zehn Spiele um 21:26 UTC gerechnet,
   Anstoß war 18:00 und 18:45 – eine Rückschau mit Prognose-Etikett. Dafür gibt es jetzt
   Durchgang 0 in `CLAUDE.md`.
7. **Zwei Sessions können dieselben Spiele eintragen.** Am 29.09. wären die zehn
   National-League-Spiele doppelt in `bilanz.json` gelandet. Vor `--merken` immer `git fetch`
   und die `id` prüfen.

## Regeländerungen vom 29.09.2026

- **Empfehlungen sind Dauerfreigabe.** Fragt der Nutzer, wird empfohlen – ohne Rückfrage.
- **Keine feste Obergrenze von drei Legs mehr.** Die Datenlage entscheidet; bei sehr guter
  Datenlage fünf bis sechs Legs.
- **Ligenregel jetzt nach Wett-Familie statt nach Wettart.** Pro Liga höchstens ein Leg aus
  der Tor-Familie (Über/Unter 2,5, Beide treffen) und eines aus der Ausgangs-Familie
  (Sieg Heim/Auswärts). Grund: Über 2,5 und Beide treffen lesen dieselbe Zahl ab und
  korrelierten an den zehn Spielen vom 29.09. mit +0,96.
- **Durchgang 0 und Durchgang 4** in der Prüfroutine: Uhrzeit, Cache-Alter, Doppeleintrag und
  Vollzähligkeit vorher; Formkontrolle der ganzen Antwort nachher.
