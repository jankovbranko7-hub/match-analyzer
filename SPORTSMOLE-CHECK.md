# Sports-Mole-Check (System B) · Version 1.0

Vom Nutzer festgelegt am 20.11.2026. Ersetzt **alle** früheren Versionen des Forebet-Checks
(1 bis 3.1, archiviert in `archiv/`); von ihnen wird nichts mehr verwendet.
Grundlage je Paarung ist **Sports Mole**, das Claude selbst abruft. **FootyStats dient nur dem
Abgleich** der Daten, nicht als Grund für den Tipp. Je Paarung gibt es **immer genau einen Tipp**
aus sechs Märkten. Eigener Branch (`forebet-system`); getrennt von allen anderen Systemen.

## Ablauf eines Auftrags

Der Nutzer schreibt z. B. **„Analyse der heutigen Spiele aus der League One“** (Liga und Tag). Dann:
1. Claude holt aus der Sports-Mole-Vorschau-Übersicht alle Paarungen dieser Liga an diesem Tag
   (`werkzeuge/sm_spiel.py tag "<Liga>" [Wochentag]`, Anstoß in deutscher Zeit).
2. Claude gleicht mit FootyStats ab, welche Spiele der Liga an dem Tag angesetzt sind; Spiele ohne
   Sports-Mole-Vorschau werden als „nicht bewertet (keine Vorschau)“ aufgeführt.
3. Für jede Paarung holt Claude die vier Sports-Mole-Teile (`werkzeuge/sm_spiel.py "<Heim>" "<Gast>"`)
   und geht den Entscheidungsweg unten durch – je Paarung genau ein Tipp.
4. Alle Tipps kommen in die Tagesliste; Antwort an den Nutzer kurz und handytauglich (Listen statt
   breiter Tabellen).

## Grundsätze

1. **Keine Quoten.** Quoten (auch der Quotenbereich der Sports-Mole-Spielseite), Buchmacher und
   Vorteil/fair werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Grundbasis ist Sports Mole** – vier Teile, je Paarung von Claude selbst abgerufen
   (`werkzeuge/sm_spiel.py`):
   1. **Vorschau-Übersicht** (`sportsmole.co.uk/football/preview/`): Paarung finden.
   2. **Vorschau-Artikel:** Ausgangslage, Formleisten (Liga und alle Wettbewerbe), Teamnews
      (Ausfälle, Sperren, Rückkehrer, Wackelkandidaten), mögliche Aufstellungen, „We say“, Stand.
   3. **Spielseite „Match Guide, Data Analysis“:** Formleisten, letztes Spiel, Tore und
      Top-Torschütze je Team, Datenanalyse (Wahrscheinlichkeiten für Sieg/Remis/Niederlage, beide
      treffen, über/unter 1,5–4,5, Tore je Team, erstes Tor, Halbzeit), Direktvergleiche,
      letzte 6 Ergebnisse je Team mit Spielstand.
   4. **Tabelle und Torschützenliste** der Liga.
3. **FootyStats nur zum Abgleich** (`werkzeuge/fs_spiel.py`): Anstoß, letzte Ergebnisse,
   Tabellenplatz, Direktvergleiche. FootyStats liefert **keinen** eigenen Grund für den Tipp.
   Weicht eine Sports-Mole-Angabe von FootyStats ab, wird das vermerkt und diese Angabe wird
   nicht als Grund verwendet. Nach Abpfiff liefert FootyStats die Ergebnisse für die Auswertung.
4. **Nur Spiele mit Sports-Mole-Vorschau** werden bewertet. Die Vorschau muss zu diesem Termin
   gehören (Datum, Spieltag); eine veraltete Vorschau (z. B. zu einem verlegten Termin) zählt nicht.

## Rangfolge (alles aus Sports Mole)

| Rang | Information | Teil |
|---|---|---|
| 1 | Teamnews: Ausfälle, Sperren, Rückkehrer, Aufstellungen, Trainer, Ausgangslage | Artikel |
| 2 | Form: Formleisten (Liga, alle Wettbewerbe), letzte 6 Ergebnisse mit Spielstand, Serien | Artikel + Spielseite |
| 3 | Datenanalyse (Wahrscheinlichkeiten), Tabelle, Tore, Torschützen | Spielseite + Tabelle |
| 4 | Direktvergleiche | Spielseite |
| – | „We say“ | nur zum Vergleich in der Tagesliste |

Hinweis: Im Artikel stehen die Formleisten vom ältesten zum neuesten Spiel, auf der Spielseite
vom neuesten zum ältesten (letztes Spiel zuerst).

## Entscheidungsweg je Paarung (immer in dieser Reihenfolge)

1. **Abrufen und prüfen:** Artikel, Spielseite, Tabelle holen; prüfen, dass die Vorschau zu diesem
   Termin gehört und wann sie zuletzt aktualisiert wurde.
2. **Abgleich mit FootyStats:** Anstoß, letzte 6 Ergebnisse, Tabellenplatz, Direktvergleiche.
   Abweichungen vermerken (Grundsatz 3).
3. **Spielbild je Team** aus Rang 1–2, in Worten: Angriff (trifft es?), Abwehr (bleibt es ohne
   Gegentor?), Form (gewinnt es?) – und was Ausfälle, Sperren, Trainer und Ausgangslage ändern.
4. **Sechs Märkte ordnen** nach der Datenanalyse (Rang 3), höchste Wahrscheinlichkeit zuerst:
   Heimsieg, Auswärtssieg, Beide treffen – Ja, Beide treffen – Nein, Über 2,5, Unter 2,5.
5. **Tipp:** Von oben nach unten der **erste Markt, gegen den Rang 1–2 nicht klar sprechen**.
   „Klar dagegen“ heißt: eine konkrete Angabe aus Teamnews oder Form lässt direkt das Gegenteil
   erwarten (z. B. Sieg-Tipp, aber das Team hat in den letzten 6 kaum gewonnen oder seine
   wichtigsten Spieler fehlen; „Beide treffen – Ja“, aber ein Team blieb zuletzt mehrfach ohne Tor;
   „Über 2,5“, aber beide Teams spielten zuletzt fast nur torarm). Kleinigkeiten zählen nicht.
   Sprechen Rang 1–2 gegen alle sechs Märkte, ist der Tipp der Markt mit der höchsten
   Wahrscheinlichkeit. **Es gibt immer genau einen Tipp.**

## Regeln für den Tipp

1. **Genau ein Tipp je Paarung**, deutlich als „Tipp“ markiert, mit dem Platz in der Reihenfolge
   aus Schritt 4 (Platz 1 = höchste Wahrscheinlichkeit).
2. **Erlaubte Märkte – nur diese sechs:** Heimsieg, Auswärtssieg, Beide treffen – Ja,
   Beide treffen – Nein, Über 2,5 Tore, Unter 2,5 Tore. Keine anderen Wettarten (kein Remis,
   keine Doppelte Chance, keine Ecken, keine anderen Torlinien).
3. Rang 3–4 drehen eine klare Angabe aus Rang 1–2 nicht um; Rang 1–2 können einen Markt nur
   überspringen, nicht neu erfinden.
4. Jede Aussage im Spielbild nennt ihre Sports-Mole-Quelle (Artikel, Spielseite, Tabelle).

## Antwortaufbau je Paarung

1. Rang 1: Teamnews und Ausgangslage
2. Rang 2: Form (Formleisten, letzte Ergebnisse)
3. Abgleich FootyStats (übereinstimmend oder Abweichung)
4. Spielbild je Team
5. Die sechs Märkte in der Reihenfolge der Datenanalyse, je „passt“ oder „klar dagegen – weil …“
6. ✅ **Tipp** mit Platz und Gründen
7. Zum Vergleich: „We say“

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/sportsmole/JJJJ-MM-TT.md` (Anstoß, Paarung, Liga,
FootyStats-`match_id`, Tipp, Platz, „We say“) und werden dort nach Abpfiff mit den Ergebnissen aus
FootyStats ausgewertet: Treffer und Trefferquote, Treffer je Wettart und je Platz, dazu „We say“
zum Vergleich (Sieger/Remis); keine Einheiten, keine Quoten. Tipps möglichst vor Anpfiff; Tipps
nach Anpfiff werden vermerkt.
