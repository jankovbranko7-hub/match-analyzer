# Sports-Mole-Check (System B) · Version 1.1

Vom Nutzer festgelegt am 20.11.2026. Ersetzt **alle** früheren Versionen des Forebet-Checks
(1 bis 3.1, archiviert in `archiv/`); von ihnen wird nichts mehr verwendet.
Version 1.0 am 20.11.2026; **Version 1.1** am selben Tag auf Wunsch des Nutzers: **Sports Mole und
FootyStats entscheiden gemeinsam.** Sports Mole liefert, was in keiner Statistik steht (Teamnews,
Trainer, Ausgangslage), FootyStats die harten Zahlen; beide kontrollieren sich gegenseitig. Jeder
Tipp wird gekennzeichnet: „beide einig“ oder „geteilt“. Je Paarung gibt es **immer genau einen Tipp**
aus sechs Märkten, den Claude **selbst** aus dem Gesamtbild bestimmt – ohne Rechenmodell, ohne
Schwellen, ohne Punkte (Wunsch des Nutzers vom 20.11.2026). Eigener Branch (`forebet-system`); getrennt von allen anderen Systemen.

## Ablauf eines Auftrags

Der Nutzer schreibt z. B. **„Analyse der heutigen Spiele aus der League One“** (Liga und Tag). Dann:
1. Claude holt aus der Sports-Mole-Vorschau-Übersicht alle Paarungen dieser Liga an diesem Tag
   (`werkzeuge/sm_spiel.py tag "<Liga>" [Wochentag]`, Anstoß in deutscher Zeit).
2. Claude gleicht mit FootyStats ab, welche Spiele der Liga an dem Tag angesetzt sind; Spiele ohne
   Sports-Mole-Vorschau werden als „nicht bewertet (keine Vorschau)“ aufgeführt.
3. Für jede Paarung holt Claude die vier Sports-Mole-Teile (`werkzeuge/sm_spiel.py "<Heim>" "<Gast>"`)
   und die FootyStats-Zahlen (`werkzeuge/fs_spiel.py <season_id> "<Heim>" "<Gast>"`) und geht den
   Entscheidungsweg unten durch – je Paarung genau ein Tipp.
4. Alle Tipps kommen in die Tagesliste; Antwort an den Nutzer kurz und handytauglich (Listen statt
   breiter Tabellen).

## Sorgfalt – keine Fehler, nichts vergessen (Pflicht, Wunsch des Nutzers vom 20.11.2026)

Vor jeder Antwort mit Tipps geht Claude diese Prüfliste **vollständig** durch und schreibt am Ende
der Tagesliste eine Zeile „Prüfliste erledigt“ mit den gefundenen und korrigierten Fehlern.

**Vollständigkeit**

1. Alle Paarungen der genannten Liga an dem Tag erfasst – Sports-Mole-Übersicht **und**
   FootyStats-Spielplan verglichen; jedes Spiel ohne Vorschau steht als „nicht bewertet“ in der Liste.
2. Je Paarung alle vier Sports-Mole-Teile (Übersicht, Artikel, Spielseite, Tabelle und Torschützen)
   und die FootyStats-Zahlen abgerufen; fehlt ein Teil, wird das genannt.
3. Je Paarung genau ein Tipp aus den sechs erlaubten Märkten; alle sechs Märkte geprüft.

**Richtigkeit**

4. Vorschau gehört zu diesem Termin (Datum, Spieltag, Stand der Aktualisierung geprüft).
5. Anstoß in deutscher Zeit, mit FootyStats abgeglichen.
6. Jede Zahl und jedes Ergebnis im Spielbild gegen die Quelle geprüft (Wortlaut der Vorschau,
   Spielseite, Tabelle, FootyStats); Formleisten in der richtigen Richtung gelesen (Artikel: alt → neu,
   Spielseite: neu → alt).
   - **6a:** Bei jeder Serie, jedem Trend und jeder Bilanz steht, ob sie **Liga oder alle
     Wettbewerbe** meint. FootyStats-Trends („seit X Spielen …“) zählen oft nur die Liga – vor
     Verwendung mit den Ergebnislisten beider Quellen nachzählen (ergänzt am 20.11.2026).
7. Jeder Ausfall, jede Sperre, jeder Rückkehrer dem **richtigen Team** zugeordnet.
8. Gegenseitiger Abgleich gemacht (letzte Ergebnisse, Tabellenplatz);
   Abweichungen vermerkt, nur übereinstimmende Angaben als Grund verwendet.
   - **8a:** Kennzeichnung „beide einig“ oder „geteilt“ gesetzt und bei „geteilt“ begründet.
9. Tipp ist der sicherste der sechs Märkte (gegen ihn spricht am wenigsten; bei den anderen
   Märkten kurz gesagt, warum mehr dagegen spricht). Tipp passt zur Begründung: Die genannten Gründe tragen genau diesen Markt; **alle**
   Angaben aus Rang 1–2, die gegen den Tipp sprechen, sind genannt (auch Ausfälle beim Gegner und
   Ergebnisse unter einem neuen Trainer); Richtung aus Rang 1–2, Rang 3 dreht sie nicht um.
10. Keine Quoten, kein Rechenmodell (weder Sports-Mole-Datenanalyse noch FootyStats-Vorab-Werte),
    **keine Direktvergleiche (H2H)**, keine Schwellen, keine Punkte verwendet – auch nicht nebenbei
    in Spielbild oder Gegenangaben.

**Abschluss**

11. Tagesliste vollständig (alle Spalten, Gründe je Paarung), committet und auf den Arbeitsbranch
    **und** `forebet-system` gepusht.
12. Nach Abpfiff: alle Ergebnisse aus FootyStats eingetragen und ausgewertet – kein Spiel vergessen.

**Drei Kontrollstufen** (keine Garantie möglich, darum mehrfach geprüft):
- **Stufe 1 – Kontrolldurchgang (automatisch):** Nach der Analyse und vor der Antwort liest Claude
  jede Aussage der Tagesliste noch einmal gegen die Quelle (Vorschau, Spielseite, Tabelle,
  FootyStats) und geht die Prüfliste durch. Erst danach gehen die Tipps an den Nutzer.
- **Stufe 2 – Prüffrage des Nutzers:** Schreibt der Nutzer **„Kontrolle“**, prüft Claude alles
  von vorn: Quellen neu abrufen, jede Zahl, jedes Ergebnis, jede Zuordnung, jeden Tipp gegen die
  Gründe. Antwort: „keine Fehler gefunden“ oder jeder Fehler mit Korrektur; in der Tagesliste wird
  „Kontrolle (Uhrzeit): …“ vermerkt.
- **Stufe 3 – unabhängige Kontrolle (seit 20.11.2026):** Schreibt der Nutzer **„unabhängige
  Kontrolle“**, startet Claude einen zweiten, unabhängigen Prüfer (eigene Claude-Instanz, ohne die
  Analyse aus dem Gespräch zu kennen). Er liest Regeln und Tagesliste, ruft alle Quellen selbst neu
  ab (Sports Mole, FootyStats) und prüft Vollständigkeit, Anstoß, jede Aussage mit Teamzuordnung,
  den FootyStats-Abgleich und ob jeder Tipp regelkonform aus den Gründen folgt. Er ändert nichts;
  Claude trägt jeden gefundenen Fehler korrigiert ein und vermerkt in der Tagesliste
  „Unabhängige Kontrolle (Uhrzeit): …“. Ein Tipp wird nur neu bestimmt, wenn ein Fehler einen
  Tipp-Grund betrifft und das Spiel noch nicht angepfiffen ist.

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
      letzte 6 Ergebnisse je Team mit Spielstand. **Direktvergleiche und die Datenanalyse
      (Wahrscheinlichkeiten des Sports-Mole-Rechenmodells) werden nicht verwendet** – weder als
      Grund noch zum Vergleich.
   4. **Tabelle und Torschützenliste** der Liga.
3. **FootyStats entscheidet mit** (`werkzeuge/fs_spiel.py`) – die harten Zahlen: letzte 6 Spiele
   aller Wettbewerbe und letzte 6 Ligaspiele; Bilanz des Heimteams daheim und des Gastteams
   auswärts; Tore, Punkte pro Spiel, xG der bisherigen Spiele; Anteile über 2,5, beide treffen,
   zu null, ohne Tor; Trends (Serien). **Nicht verwendet** werden die Vorab-Werte
   (Vorab-xG, Torpotenzial) – das sind Modellwerte. Außerdem: Spielplan (Vollständigkeit),
   Anstoß, match_id und nach Abpfiff die Ergebnisse für die Auswertung.
4. **Gegenseitige Kontrolle:** Wo beide dieselben Daten haben (Ergebnisse, Tabelle), müssen sie
   übereinstimmen. Abweichungen werden vermerkt; als Grund wird nur
   verwendet, was beide gleich zeigen.
5. **Nur Spiele mit Sports-Mole-Vorschau** werden bewertet. Die Vorschau muss zu diesem Termin
   gehören (Datum, Spieltag); eine veraltete Vorschau (z. B. zu einem verlegten Termin) zählt nicht.

## Rangfolge

| Rang | Information | Quelle |
|---|---|---|
| 1 | Teamnews: Ausfälle, Sperren, Rückkehrer, Aufstellungen, Trainer, Ausgangslage | Sports Mole (Artikel) |
| 2 | Form: letzte 6 aller Wettbewerbe und letzte 6 Ligaspiele mit Ergebnissen, Serien (trifft seit …, ohne Tor seit …, zu null) | FootyStats + Sports Mole (Formleisten, Spielseite) |
| 3 | Saison: Tabelle, Bilanz daheim bzw. auswärts, Tore, xG, Anteile über 2,5 / beide treffen / zu null / ohne Tor; Torschützen | FootyStats + Sports Mole (Tabelle, Torschützen) |
| – | „We say“ | nur zum Vergleich in der Tagesliste |
| – | Sports-Mole-Datenanalyse, FootyStats-Vorab-Werte | nicht verwendet (Rechenmodelle) |
| – | **Direktvergleiche (H2H)** – Bilanz, Ergebnisse, Ø Tore, Serien gegen diesen Gegner | **nicht verwendet** (Wunsch des Nutzers vom 20.11.2026) – weder als Grund noch als Gegenangabe |

Hinweis: Im Artikel stehen die Formleisten vom ältesten zum neuesten Spiel, auf der Spielseite
vom neuesten zum ältesten (letztes Spiel zuerst).

## Entscheidungsweg je Paarung (immer in dieser Reihenfolge)

1. **Abrufen und prüfen:** Artikel, Spielseite, Tabelle holen; prüfen, dass die Vorschau zu diesem
   Termin gehört und wann sie zuletzt aktualisiert wurde.
2. **FootyStats holen und gegenseitig abgleichen:** Anstoß, letzte Ergebnisse, Tabellenplatz;
   Abweichungen vermerken (Grundsatz 4).
3. **Spielbild je Team** – drei Fragen: **Trifft es? Kassiert es? Gewinnt es?** Die Zahlen dazu
   kommen aus FootyStats (Rang 2–3), Sports Mole korrigiert mit den Teamnews (Rang 1): fehlt z. B.
   der Torjäger, zählt sein bisheriger Torschnitt weniger; fehlen Innenverteidiger, zählen die Gegentore mehr.
   Bei einem Widerspruch geht eine **konkrete Nachricht aus Sports Mole** einer Zahl aus FootyStats
   vor (ein gesperrter Kapitän wiegt mehr als ein Saisonwert).
4. **Die sechs Märkte prüfen:** Heimsieg, Auswärtssieg, Beide treffen – Ja, Beide treffen – Nein,
   Über 2,5, Unter 2,5 – je kurz: was spricht dafür, was dagegen (nach Rangfolge gewichtet).
5. **Tipp:** Claude bestimmt **selbst** den Markt, den **beide Quellen gemeinsam** am stärksten
   tragen – ohne Rechenmodell, Schwellen oder Punkte. Rang 1–2 geben die Richtung, Rang 3 hilft
   bei der Wahl und drehen eine klare Richtung aus Rang 1–2 nicht um. Was dagegen spricht, wird
   genannt. **Es gibt immer genau einen Tipp.**
   **Immer der sicherste der sechs Märkte** (Wunsch des Nutzers vom 20.11.2026): Claude wählt in
   jedem Spiel – ob „beide einig“ oder „geteilt“ – unter den sechs erlaubten Märkten den
   **sichersten, also den, gegen den am wenigsten spricht** (nach Rangfolge gewichtet). In der
   Begründung steht kurz, warum gegen die anderen Märkte mehr spricht. Es wird nie auf andere,
   „sicherere“ Wettarten ausgewichen (keine Doppelte Chance, kein Über 1,5, kein Unter 3,5 o. Ä.).
6. **Kennzeichnung:** „**beide einig**“ – Sports Mole und FootyStats zeigen beide zum Tipp;
   „**geteilt**“ – eine Quelle zeigt woandershin (welche und warum, in einem Satz). Die
   Kennzeichnung ist keine Schwelle, sondern dient der Auswertung.

## Regeln für den Tipp

1. **Genau ein Tipp je Paarung**, deutlich als „Tipp“ markiert, mit Gründen, dem, was dagegen
   spricht, und der Kennzeichnung „beide einig“ oder „geteilt“. Der Tipp ist **immer der sicherste
   der sechs Märkte** – der, gegen den am wenigsten spricht. Die Kennzeichnung sagt nur, wie sicher
   er ist (beide einig = sicherer, geteilt = unsicherer); sie entscheidet nie, ob getippt wird.
2. **Erlaubte Märkte – nur diese sechs:** Heimsieg, Auswärtssieg, Beide treffen – Ja,
   Beide treffen – Nein, Über 2,5 Tore, Unter 2,5 Tore. Keine anderen Wettarten (kein Remis,
   keine Doppelte Chance, keine Ecken, keine anderen Torlinien).
3. Rang 3 dreht eine klare Angabe aus Rang 1–2 nicht um.
4. Jede Aussage im Spielbild nennt ihre Quelle (Sports Mole: Artikel, Spielseite, Tabelle;
   FootyStats).
5. Kein Rechenmodell, keine Direktvergleiche (H2H), keine Schwellen, keine Punkte, keine Zählung
   („x von 10“).

## Antwortaufbau je Paarung

1. Rang 1: Teamnews und Ausgangslage (Sports Mole)
2. Rang 2–3: Form, Saison (FootyStats + Sports Mole)
3. Gegenseitiger Abgleich (übereinstimmend oder Abweichung)
4. Spielbild je Team: trifft es? kassiert es? gewinnt es?
5. Die sechs Märkte, je kurz dafür/dagegen
6. ✅ **Tipp** mit Gründen, Gegenangaben und „beide einig“ / „geteilt“
7. Zum Vergleich: „We say“

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/sportsmole/JJJJ-MM-TT.md` (Anstoß, Paarung, Liga,
FootyStats-`match_id`, Tipp, „beide einig“/„geteilt“, „We say“) und werden dort nach Abpfiff mit
den Ergebnissen aus FootyStats ausgewertet: Treffer und Trefferquote, Treffer je Wettart,
**Treffer „beide einig“ gegenüber „geteilt“**, dazu „We say“
zum Vergleich (Sieger/Remis); keine Einheiten, keine Quoten. Tipps möglichst vor Anpfiff; Tipps
nach Anpfiff werden vermerkt.
