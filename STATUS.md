# Stand

Zuletzt aktualisiert: 28.09.2026. Diese Datei ist die Übergabe an die nächste Session –
sie sagt, wo alles steht. Die Regeln stehen in `CLAUDE.md`, der Rechenweg in `README.md`,
die Schwachstellen in `SOLLBRUCHSTELLEN.md`.

## Als Erstes in einer neuen Session

```
python3 analyse/bilanz.py --auswerten
```

Das holt die Ergebnisse der offenen Spiele und zieht die Bilanz. **Vor jeder Antwort auf
die Frage „warum lag die Prognose daneben" zwingend zuerst ausführen.**

## Modellstand

**Eingefroren.** Letzte Änderung am Rechenweg: Datenfenster (`FENSTER_MIN_SPIELE = 10`)
am 27.09.2026. Keine Schuss-Komponente – besprochen, gemessen, **nicht eingebaut**.

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
| Prognosen gesamt | 61 |
| ausgewertet | 49 |
| **offen** | **11** |
| Treffer | 33 gegen 30.1 erwartete |
| Trefferquote | 67.3 % (Modell sagte 61.5 %) |
| Geld, alle Tipps zu 10 € | +8 € auf 480 € Einsatz (+1.8 %) |

Aussagekraft: Bei 49 Spielen wäre erst eine Verzerrung ab rund 20 Prozentpunkten
nachweisbar. Für 10 Punkte braucht es rund 190 Spiele. **Bis dahin ist keine Abweichung ein
Grund, an den Gewichten zu drehen.**

## Offene Prognosen (11)

| Spiel | Tipp | Wahrsch. | Faire Quote | Anstoß UTC |
|---|---|---|---|---|
| Žilina II – Futura Humenné | Sieg Heim | 55.7 % | 1.79 | 15:00 |
| Naftagas – Jedinstvo Ub | Beide treffen | 52.2 % | 1.91 | 16:00 |
| Bor – Metalac GM | Unter 2,5 | 57.7 % | 1.73 | 16:00 |
| Dubočica – Javor Ivanjica | Beide treffen | 58.0 % | 1.72 | 16:00 |
| Hapoel Kfar Shalem – Maccabi Kabilio Jaffa | Beide treffen | 67.6 % | 1.48 | 16:00 |
| Hapoel Kfar Saba – Bnei Yehuda | Über 2,5 | 70.0 % | 1.43 | 16:00 |
| Maccabi Kiryat Gat – Kafr Qasim | Beide treffen | 59.7 % | 1.68 | 16:00 |
| Maccabi Bnei Raina – Hapoel Ra'anana | Beide treffen | 66.4 % | 1.51 | 16:45 |
| Rudar – Dravinja | Über 2,5 | 65.5 % | 1.53 | 17:00 |
| Loznica – Spartak Subotica | Beide treffen | 61.5 % | 1.63 | 18:00 |
| Leganés – CD Castellón | Unter 2,5 | 53.4 % | 1.87 | 18:30 |

## Laufender Wettschein des Nutzers

4er-Kombi vom 28.09., Einsatz 20 €, Kombiquote 7,26, möglicher Gewinn 145,11 €.
Legs: Kiryat Gat BTTS 1,55 · Bor Unter 2,5 1,65 · Bney Reine BTTS 1,47 · Leganés Unter 2,5 1,93.
Trefferchance 12,2 %, Erwartungswert 17,72 € – drei der vier Quoten lagen unter der fairen.

## Was in dieser Session gelernt wurde

1. **Die Tabelle entscheidet, nicht die Prosa.** Warnungen im Fließtext werden überlesen.
   Alles Entscheidungsrelevante gehört in eine Spalte.
2. **`gegen fair` misst bei dünner Datenlage das eigene Rauschen**, nicht Value. Deshalb hat
   die Rangliste zwei Blöcke.
3. **FootyStats-Quoten sind nicht die Quoten des Nutzers** – im Median 6,1 % darüber,
   im Extremfall 17,5 %.
4. **Die Marge multipliziert sich je Leg.** Sieben Legs, sechs gewonnen, Schein verloren.
5. **Der Backtest ist verboten.** Die einzige erlaubte Rückschau ist `bilanz.py --auswerten`.
