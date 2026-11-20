# Sports-Mole-Check (System B) · Version 1.0

Vom Nutzer festgelegt am 20.11.2026. Ersetzt **alle** früheren Versionen des Forebet-Checks
(1 bis 3.1, archiviert in `archiv/`); von ihnen wird nichts mehr verwendet.
Grundlage je Paarung ist **Sports Mole**, das Claude selbst abruft. **FootyStats dient nur dem
Abgleich** der Daten, nicht als Grund für den Tipp. Je Paarung gibt es **immer genau einen Tipp**
aus sechs Märkten, den Claude **selbst** aus dem Gesamtbild bestimmt – ohne Rechenmodell, ohne
Schwellen, ohne Punkte (Wunsch des Nutzers vom 20.11.2026). Eigener Branch (`forebet-system`); getrennt von allen anderen Systemen.

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

## Sorgfalt – keine Fehler, nichts vergessen (Pflicht, Wunsch des Nutzers vom 20.11.2026)

Vor jeder Antwort mit Tipps geht Claude diese Prüfliste **vollständig** durch und schreibt am Ende
der Tagesliste eine Zeile „Prüfliste erledigt“ mit den gefundenen und korrigierten Fehlern.

**Vollständigkeit**
1. Alle Paarungen der genannten Liga an dem Tag erfasst – Sports-Mole-Übersicht **und**
   FootyStats-Spielplan verglichen; jedes Spiel ohne Vorschau steht als „nicht bewertet“ in der Liste.
2. Je Paarung alle vier Sports-Mole-Teile abgerufen (Übersicht, Artikel, Spielseite, Tabelle und
   Torschützen); fehlt ein Teil, wird das genannt.
3. Je Paarung genau ein Tipp aus den sechs erlaubten Märkten; alle sechs Märkte geprüft.

**Richtigkeit**
4. Vorschau gehört zu diesem Termin (Datum, Spieltag, Stand der Aktualisierung geprüft).
5. Anstoß in deutscher Zeit, mit FootyStats abgeglichen.
6. Jede Zahl und jedes Ergebnis im Spielbild gegen die Quelle geprüft (Wortlaut der Vorschau,
   Spielseite, Tabelle); Formleisten in der richtigen Richtung gelesen (Artikel: alt → neu,
   Spielseite: neu → alt).
7. Jeder Ausfall, jede Sperre, jeder Rückkehrer dem **richtigen Team** zugeordnet.
8. Abgleich mit FootyStats gemacht (letzte Ergebnisse, Tabellenplatz, Direktvergleiche);
   Abweichungen vermerkt und die betroffene Angabe nicht als Grund verwendet.
9. Tipp passt zur Begründung: Die genannten Gründe tragen genau diesen Markt; was dagegen spricht,
   ist genannt; Richtung aus Rang 1–2, Rang 3–4 drehen sie nicht um.
10. Keine Quoten, kein Rechenmodell, keine Schwellen, keine Punkte verwendet.

**Abschluss**
11. Tagesliste vollständig (alle Spalten, Gründe je Paarung), committet und auf den Arbeitsbranch
    **und** `forebet-system` gepusht.
12. Nach Abpfiff: alle Ergebnisse aus FootyStats eingetragen und ausgewertet – kein Spiel vergessen.

Findet Claude später einen Fehler, wird er sofort offen benannt und in der Tagesliste mit Uhrzeit
korrigiert (vor Anpfiff: Tipp darf neu bestimmt werden; nach Anpfiff: Tipp bleibt, Fehler wird
vermerkt).

## Grundsätze

1. **Keine Quoten.** Quoten (auch der Quotenbereich der Sports-Mole-Spielseite), Buchmacher und
   Vorteil/fair werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Grundbasis ist Sports Mole** – vier Teile, je Paarung von Claude selbst abgerufen
   (`werkzeuge/sm_spiel.py`):
   1. **Vorschau-Übersicht** (`sportsmole.co.uk/football/preview/`): Paarung finden.
   2. **Vorschau-Artikel:** Ausgangslage, Formleisten (Liga und alle Wettbewerbe), Teamnews
      (Ausfälle, Sperren, Rückkehrer, Wackelkandidaten), mögliche Aufstellungen, „We say“, Stand.
   3. **Spielseite „Match Guide“:** Formleisten, letztes Spiel, Tore und Top-Torschütze je Team,
      Direktvergleiche, letzte 6 Ergebnisse je Team mit Spielstand. **Die Datenanalyse
      (Wahrscheinlichkeiten des Sports-Mole-Rechenmodells) wird nicht verwendet** – weder als
      Grund noch zum Vergleich.
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
| 3 | Tabelle (Platz, Bilanz, Tore), Torschützen, Tore je Team | Tabelle + Spielseite |
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
4. **Die sechs Märkte prüfen:** Heimsieg, Auswärtssieg, Beide treffen – Ja, Beide treffen – Nein,
   Über 2,5, Unter 2,5 – je kurz: was spricht dafür, was dagegen (nach Rangfolge gewichtet).
5. **Tipp:** Claude bestimmt **selbst** den Markt, der am besten zum Spielbild passt – ohne
   Rechenmodell, Schwellen oder Punkte. Rang 1–2 geben die Richtung, Rang 3–4 helfen bei der Wahl
   und drehen eine klare Richtung aus Rang 1–2 nicht um. Widersprechen sich die Angaben, wählt
   Claude den Markt, den das Gesamtbild am stärksten trägt, und nennt, was dagegen spricht.
   **Es gibt immer genau einen Tipp.**

## Regeln für den Tipp

1. **Genau ein Tipp je Paarung**, deutlich als „Tipp“ markiert, mit Gründen und dem, was dagegen
   spricht.
2. **Erlaubte Märkte – nur diese sechs:** Heimsieg, Auswärtssieg, Beide treffen – Ja,
   Beide treffen – Nein, Über 2,5 Tore, Unter 2,5 Tore. Keine anderen Wettarten (kein Remis,
   keine Doppelte Chance, keine Ecken, keine anderen Torlinien).
3. Rang 3–4 drehen eine klare Angabe aus Rang 1–2 nicht um.
4. Jede Aussage im Spielbild nennt ihre Sports-Mole-Quelle (Artikel, Spielseite, Tabelle).
5. Kein Rechenmodell, keine Schwellen, keine Punkte, keine Zählung („x von 10“).

## Antwortaufbau je Paarung

1. Rang 1: Teamnews und Ausgangslage
2. Rang 2: Form (Formleisten, letzte Ergebnisse)
3. Abgleich FootyStats (übereinstimmend oder Abweichung)
4. Spielbild je Team
5. Die sechs Märkte, je kurz dafür/dagegen
6. ✅ **Tipp** mit Gründen und Gegenangaben
7. Zum Vergleich: „We say“

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/sportsmole/JJJJ-MM-TT.md` (Anstoß, Paarung, Liga,
FootyStats-`match_id`, Tipp, „We say“) und werden dort nach Abpfiff mit den Ergebnissen aus
FootyStats ausgewertet: Treffer und Trefferquote, Treffer je Wettart, dazu „We say“
zum Vergleich (Sieger/Remis); keine Einheiten, keine Quoten. Tipps möglichst vor Anpfiff; Tipps
nach Anpfiff werden vermerkt.
