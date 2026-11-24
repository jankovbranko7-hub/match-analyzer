# Sports-Mole-Check (System B) · Version 1.3

Vom Nutzer festgelegt am 20.11.2026. Ersetzt **alle** früheren Versionen des Forebet-Checks
(1 bis 3.1, archiviert in `archiv/`); von ihnen wird nichts mehr verwendet.
Version 1.0 am 20.11.2026; **Version 1.1** am selben Tag auf Wunsch des Nutzers: **Sports Mole und
FootyStats entscheiden gemeinsam.** Sports Mole liefert, was in keiner Statistik steht (Teamnews,
Trainer, Ausgangslage), FootyStats die harten Zahlen; beide kontrollieren sich gegenseitig. Jeder
Tipp wird gekennzeichnet: „beide einig“ oder „geteilt“. **Version 1.2** (20.11.2026, Wunsch des
Nutzers): fester **Lage-Check je Team** – worum es geht, wie dringend die Punkte sind, Serien
(letzter Sieg, letztes Tor), Schwächung, Besonderheiten; die Lage steht über den Saisonzahlen.
**Version 1.3** (21.11.2026, Wunsch des Nutzers): **Vorschau und Daten richtig lesen** – Pflicht-
**Datenblatt je Team** (neuer Schritt 3), jede Zahl mit Bezug, Teamnews nach dem Originalwort,
**automatischer Abgleich** Sports Mole ↔ FootyStats (`werkzeuge/abgleich.py`); **„We say“ wird
überhaupt nicht mehr verwendet** – weder als Grund noch zum Vergleich; **Fehlerprotokoll**
(`FEHLERPROTOKOLL.md`): jeder gefundene Fehler wird eingetragen, vor jeder Analyse gelesen und in
jeder Kontrolle Fehlerart für Fehlerart geprüft. Version 1.2 liegt in `archiv/SPORTSMOLE-CHECK-1.2.md`.
**Ergänzungen zu 1.3** (Wünsche des Nutzers): Regel 7b – Ausfälle nur mit belegter Position als Richtung
(22.11.); Platzverweise in der Auswertung gesondert mitzählen (24.11.); Abschnitt **Europapokal** (24.11.).
Je Paarung gibt es **immer genau einen Tipp**
aus sechs Märkten, den Claude **selbst** aus dem Gesamtbild bestimmt – ohne Rechenmodell, ohne
Schwellen, ohne Punkte (Wunsch des Nutzers vom 20.11.2026). Eigener Branch (`forebet-system`); getrennt von allen anderen Systemen.

## Verbindlichkeit (Wunsch des Nutzers vom 21.11.2026)

Dieses System und **alle seine Punkte** gelten **immer** und dürfen **nicht umgangen** werden:
Ablauf, Prüfliste „Sorgfalt“, Grundsätze, Rangfolge, Entscheidungsweg Schritt 1–8 in seiner
Reihenfolge, Regeln für den Tipp, Antwortaufbau, Tagesliste und Kontrollstufen.

- Für **jede** Paarung, ohne Ausnahme – auch bei vielen Spielen, Zeitdruck oder kurz vor Anpfiff.
- Kein Schritt wird ausgelassen, abgekürzt, zusammengelegt oder durch etwas anderes ersetzt.
- Nichts außerhalb des Systems fließt ein (keine Quoten, kein Rechenmodell, keine Direktvergleiche,
  keine Schwellen oder Punkte, kein „We say“, keine Vermutung ohne Quelle).
- Kann ein Schritt nicht vollständig erledigt werden (Quelle fehlt, Seite nicht erreichbar), sagt
  Claude das dem Nutzer offen und vermerkt es in der Tagesliste – nie stillschweigend übergehen.
- Erst wenn die Prüfliste für alle Paarungen einer Gruppe (gleiche Anstoßzeit) erfüllt ist, gehen
  deren Tipps an den Nutzer. Ein
  Verstoß, der vorher auffällt, wird vor der Antwort behoben.
- Ausnahmen oder Änderungen nur auf ausdrücklichen Wunsch des Nutzers; Claude macht keine eigenen.

**Arbeitsweise je Paarung** (Wunsch des Nutzers vom 21.11.2026):

- **Jede Paarung einzeln, Schritt für Schritt** (Entscheidungsweg 1–8: Abrufen, Abgleich,
  Datenblatt, Lage, Spielbild, Märkte, Tipp, Kennzeichnung) – erst wenn eine Paarung vollständig
  fertig ist, kommt die nächste. Keine Paarungen im Block nebeneinander bearbeiten.
- **Gruppen nach Anstoßzeit** (Wahl des Nutzers vom 21.11.2026): Die Paarungen werden in der
  Reihenfolge ihres Anstoßes bearbeitet und zu Gruppen mit derselben Anstoßzeit zusammengefasst.
  **Eine Gruppe geht erst an den Nutzer, wenn jede ihrer Paarungen fertig und geprüft ist**
  (Prüfliste, Kontrolldurchgang, **automatische unabhängige Kontrolle** mit Korrekturen) – auch wenn
  es länger dauert. Dann folgt die nächste Gruppe.
- **Reicht die Zeit bis zum Anpfiff nicht für alle Spiele**, sagt Claude das dem Nutzer offen,
  statt abzukürzen (welche Spiele nicht mehr vollständig geschafft werden).

**Alles im Chat** (Wunsch des Nutzers vom 21.11.2026): Der Nutzer liest die Dateien nicht. Alles,
was er wissen muss, steht **vollständig im Chat**, handytauglich als Liste:

- je Paarung (Variante 1, Wahl des Nutzers vom 21.11.2026): **Anstoß, Paarung, Tipp mit
  Kennzeichnung, die Gründe und alle Gegenangaben – jede aus Rang 1–2 mit „dreht den Tipp: ja/nein,
  weil …“**. Datenblatt, Lage-Check und Spielbild stehen vollständig in der Tagesliste, nicht im Chat;
- Ergebnisse jeder Kontrolle mit jedem gefundenen Fehler und jeder Korrektur;
- jeder neue Eintrag ins Fehlerprotokoll und was daraus folgt;
- die Auswertung.

Ein PDF nur auf ausdrücklichen Wunsch. Tagesliste und Fehlerprotokoll bleiben als Ablage.

## Ablauf eines Auftrags

Der Nutzer schreibt z. B. **„Analyse der heutigen Spiele aus der League One“** (Liga und Tag). Dann:

0. Claude liest zuerst das **Fehlerprotokoll** (`FEHLERPROTOKOLL.md`) und achtet beim Schreiben auf
   jede Fehlerart (seit 1.3, Wunsch des Nutzers vom 21.11.2026).
1. Claude holt aus der Sports-Mole-Vorschau-Übersicht alle Paarungen dieser Liga an diesem Tag
   (`werkzeuge/sm_spiel.py tag "<Liga>" [Wochentag]`, Anstoß in deutscher Zeit).
2. Claude gleicht mit FootyStats ab, welche Spiele der Liga an dem Tag angesetzt sind; Spiele ohne
   Sports-Mole-Vorschau werden als „nicht bewertet (keine Vorschau)“ aufgeführt.
3. Für jede Paarung holt Claude die vier Sports-Mole-Teile (`werkzeuge/sm_spiel.py "<Heim>" "<Gast>"`)
   und die FootyStats-Zahlen (`werkzeuge/fs_spiel.py <season_id> "<Heim>" "<Gast>"`), lässt den
   automatischen Abgleich laufen (`werkzeuge/abgleich.py <season_id> "<Heim>" "<Gast>"`), legt das
   Datenblatt je Team an und geht den Entscheidungsweg unten durch – je Paarung genau ein Tipp.
4. Alle Tipps kommen mit dem vollständigen Antwortaufbau in die Tagesliste; im Chat steht je Paarung,
   was unter „Alles im Chat“ festgelegt ist (Variante 1), handytauglich als Liste statt breiter
   Tabellen.

## Sorgfalt – keine Fehler, nichts vergessen (Pflicht, Wunsch des Nutzers vom 20.11.2026)

Vor jeder Antwort mit Tipps geht Claude diese Prüfliste **vollständig** durch (Punkt 12 gehört
zur Auswertung nach Abpfiff und wird dort erledigt) und schreibt am Ende
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
     Wettbewerbe** meint (seit 1.3 zusätzlich: gesamt / daheim / auswärts und Team oder Spiel). FootyStats-Trends („seit X Spielen …“) zählen oft nur die Liga – vor
     Verwendung mit den Ergebnislisten beider Quellen nachzählen (ergänzt am 20.11.2026).
   - **6b (seit 1.3):** Datenblatt je Team vollständig angelegt; **jede Angabe darin einmal gegen den
     Wortlaut der Quelle gelesen**; `abgleich.py` gelaufen, jede „ABWEICHUNG“ geklärt und vermerkt;
     im Spielbild, in den Märkten und im Tipp steht nichts, was nicht im Datenblatt steht.
7. Jeder Ausfall, jede Sperre, jeder Rückkehrer dem **richtigen Team** zugeordnet – mit Status nach
   dem **Originalwort** der Vorschau (fehlt / fraglich / gesperrt / zurück, siehe Schritt 3).
   - **7b (seit 22.11.2026):** Kein Ausfall ohne belegte Position ist als Grund oder Gegenangabe für
     mehr/weniger Tore oder Sieg/Niederlage verwendet; sonst steht „Position nicht in der Quelle –
     keine Richtung“.
   - **7a:** Lage-Check für **beide** Teams mit allen fünf Fragen gemacht (worum es geht,
     Dringlichkeit, Serien mit Datum des letzten Siegs und Tors, Schwächung, Besonderheit).
8. Gegenseitiger Abgleich gemacht (letzte Ergebnisse, Tabellenplatz);
   Abweichungen vermerkt, nur übereinstimmende Angaben als Grund verwendet.
   - **8a:** Kennzeichnung „beide einig“ oder „geteilt“ gesetzt und bei „geteilt“ begründet.
9. Tipp ist der sicherste der sechs Märkte (gegen ihn spricht am wenigsten; bei den anderen
   Märkten kurz gesagt, warum mehr dagegen spricht). Tipp passt zur Begründung: Die genannten Gründe tragen genau diesen Markt; **alle**
   Angaben aus Rang 1–2, die gegen den Tipp sprechen, sind genannt (auch Ausfälle beim Gegner und
   Ergebnisse unter einem neuen Trainer, Lage beider Teams); Richtung aus Rang 1–2, Rang 3 dreht sie
   nicht um. **Bei jeder Rang-1–2-Gegenangabe steht „dreht den Tipp: ja/nein, weil …“; bei „ja“
   ist der Markt neu gewählt** (seit 21.11.2026).
10. Keine Quoten, kein Rechenmodell (weder Sports-Mole-Datenanalyse noch FootyStats-Vorab-Werte),
    **keine Direktvergleiche (H2H)**, keine Schwellen, keine Punkte, **kein „We say“** verwendet –
    auch nicht nebenbei in Datenblatt, Spielbild oder Gegenangaben.

**Abschluss**

11. Tagesliste vollständig (alle Spalten, Gründe je Paarung), committet und auf den Arbeitsbranch
    **und** `forebet-system` gepusht.
12. **Nur bei der Auswertung:** nach Abpfiff alle Ergebnisse aus FootyStats eingetragen und ausgewertet – kein Spiel vergessen.
    Je Spiel auch Platzverweise aus FootyStats (`card_details`: Team, Minute, Spielstand) vermerken und
    gesondert mitzählen (Wunsch des Nutzers vom 24.11.2026) – nur zur Beobachtung, die Wertung bleibt.
13. Verbindlichkeit eingehalten: jeder Punkt des Systems für jede Paarung erfüllt, nichts
    umgangen; was nicht erledigt werden konnte, ist offen genannt (ergänzt am 21.11.2026).
14. **Fehlerprotokoll:** vor der Analyse gelesen; jede Fehlerart gezielt geprüft; jeder in
    dieser Runde gefundene Fehler dort eingetragen (seit 1.3).

**Drei Kontrollstufen** (keine Garantie möglich, darum mehrfach geprüft):

- **Stufe 1 – Kontrolldurchgang (automatisch):** Nach der Analyse und vor der Antwort liest Claude
  jede Aussage der Tagesliste noch einmal gegen die Quelle (Vorschau, Spielseite, Tabelle,
  FootyStats) und geht die Prüfliste und jede Fehlerart des Fehlerprotokolls durch. Erst danach gehen die Tipps an den Nutzer.
- **Stufe 2 – Prüffrage des Nutzers:** Schreibt der Nutzer **„Kontrolle“**, prüft Claude alles
  von vorn: Quellen neu abrufen, jede Zahl, jedes Ergebnis, jede Zuordnung, jeden Tipp gegen die
  Gründe, jede Fehlerart des Fehlerprotokolls, den Entscheidungsweg Schritt 1–8 und bei jeder
  Paarung die Gegenangaben-Prüfung („dreht den Tipp: ja/nein, weil …“). Wird eine neue Gegenangabe
  aus Rang 1–2 gefunden, wird der Tipp **immer neu abgewogen** (vor Anpfiff; angeglichen an Stufe 3
  am 21.11.2026). Antwort: „keine Fehler gefunden“ oder jeder Fehler mit Korrektur; in der Tagesliste wird
  „Kontrolle (Uhrzeit): …“ vermerkt.
- **Stufe 3 – unabhängige Kontrolle (seit 20.11.2026; seit 21.11.2026 automatisch, Wunsch des
  Nutzers):** Nach jeder Analyse – je Gruppe, nach Prüfliste und Kontrolldurchgang – startet Claude
  **von selbst, ohne Aufforderung**, einen zweiten, unabhängigen Prüfer – **genau einen Prüfer je Gruppe**,
  auch bei vielen Spielen (Wunsch des Nutzers vom 24.11.2026, spart Nutzungslimit; dauert dafür länger, also früh
  starten). Erst nach seinem Bericht
  und den Korrekturen gehen die Tipps der Gruppe an den Nutzer, im Chat zusammen mit dem
  Kontrollergebnis (gefundene Fehler, Korrekturen, geänderte Tipps – oder „keine Fehler gefunden“).
  Schreibt der Nutzer zusätzlich **„unabhängige Kontrolle“**, folgt eine weitere Runde. Reicht die
  Zeit bis zum Anpfiff dafür nicht, sagt Claude das vorher offen. Je Spieltag wird vermerkt, was die
  Kontrolle gefunden hat (Erprobung von 1.3: findet sie über mehrere Spieltage nichts, was einen
  Tipp betrifft, kann der Nutzer entscheiden, sie seltener zu verlangen). Der Prüfer ist eine eigene Claude-Instanz, die
  die Analyse aus dem Gespräch nicht kennt. Er liest Regeln, Fehlerprotokoll und Tagesliste, ruft alle Quellen selbst neu
  ab (Sports Mole, FootyStats) und prüft Vollständigkeit, Anstoß, jede Aussage mit Teamzuordnung,
  den FootyStats-Abgleich und ob jeder Tipp regelkonform aus den Gründen folgt – **und ob der
  Entscheidungsweg je Paarung vollständig und in der vorgeschriebenen Reihenfolge eingehalten ist**
  (Schritt 1–8, Datenblatt je Team gegen die Quellen, Lage-Check mit fünf Fragen für beide Teams, Spielbild je Team mit „trifft es?
  kassiert es? gewinnt es?“, alle sechs Märkte mit Grund, Tipp, Kennzeichnung; ergänzt am 21.11.2026). Er ändert nichts;
  Claude trägt jeden gefundenen Fehler korrigiert ein und vermerkt in der Tagesliste
  „Unabhängige Kontrolle (Uhrzeit): …“. Ein Tipp wird neu bestimmt, wenn ein Fehler einen
  Tipp-Grund betrifft **oder eine neue Gegenangabe aus Rang 1–2 gefunden wird** – dann wird der
  Tipp **immer neu abgewogen** („dreht den Tipp: ja/nein, weil …“), solange das Spiel noch nicht
  angepfiffen ist (seit 21.11.2026). Der Prüfer prüft bei jeder Paarung gesondert, ob eine
  Rang-1–2-Gegenangabe den Tipp dreht.

Findet Claude später einen Fehler, wird er sofort offen benannt und in der Tagesliste mit Uhrzeit
korrigiert (vor Anpfiff: Tipp darf neu bestimmt werden, bei einer neuen Rang-1–2-Gegenangabe wird
er immer neu abgewogen; nach Anpfiff: Tipp bleibt, Fehler wird
vermerkt).

## Grundsätze

1. **Keine Quoten.** Quoten (auch der Quotenbereich der Sports-Mole-Spielseite), Buchmacher und
   Vorteil/fair werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Grundbasis ist Sports Mole** – vier Teile, je Paarung von Claude selbst abgerufen
   (`werkzeuge/sm_spiel.py`):
   1. **Vorschau-Übersicht** (`sportsmole.co.uk/football/preview/`): Paarung finden.
   2. **Vorschau-Artikel:** Ausgangslage, Formleisten (Liga und alle Wettbewerbe), Teamnews
      (Ausfälle, Sperren, Rückkehrer, Wackelkandidaten), mögliche Aufstellungen, Stand. Der Absatz
      „We say“ wird nicht verwendet (seit 1.3; `sm_spiel.py` gibt ihn nicht mehr aus).
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
   übereinstimmen – seit 1.3 automatisch geprüft mit `werkzeuge/abgleich.py` (Tabellenplatz,
   Ligaspiele mit Heim/Auswärts und Spielstand, S-U-N und Tore der letzten 6 aller Wettbewerbe). Abweichungen werden vermerkt; als Grund wird nur
   verwendet, was beide gleich zeigen.
5. **Nur Spiele mit Sports-Mole-Vorschau** werden bewertet. Die Vorschau muss zu diesem Termin
   gehören (Datum, Spieltag); eine veraltete Vorschau (z. B. zu einem verlegten Termin) zählt nicht.

## Rangfolge

| Rang | Information | Quelle |
|---|---|---|
| 1 | **Lage** (Lage-Check, Schritt 4): worum es geht, Dringlichkeit der Punkte, Serien (letzter Sieg, letztes Tor), Schwächung (Ausfälle, Sperren, Trainerwechsel, Belastung), Besonderheiten – dazu Teamnews und Aufstellungen | Sports Mole (Artikel, Tabelle) + Ergebnislisten beider Quellen |
| 2 | Form: letzte 6 aller Wettbewerbe und letzte 6 Ligaspiele mit Ergebnissen, Serien (trifft seit …, ohne Tor seit …, zu null) | FootyStats + Sports Mole (Formleisten, Spielseite) |
| 3 | Saison: Tabelle, Bilanz daheim bzw. auswärts, Tore, xG, Anteile über 2,5 / beide treffen / zu null / ohne Tor; Torschützen | FootyStats + Sports Mole (Tabelle, Torschützen) |
| – | „We say“ | **nicht verwendet** (seit Version 1.3, Wunsch des Nutzers vom 21.11.2026) – weder als Grund noch zum Vergleich |
| – | Sports-Mole-Datenanalyse, FootyStats-Vorab-Werte | nicht verwendet (Rechenmodelle) |
| – | **Direktvergleiche (H2H)** – Bilanz, Ergebnisse, Ø Tore, Serien gegen diesen Gegner | **nicht verwendet** (Wunsch des Nutzers vom 20.11.2026) – weder als Grund noch als Gegenangabe |

Hinweis: Im Artikel stehen die Formleisten vom ältesten zum neuesten Spiel, auf der Spielseite
vom neuesten zum ältesten (letztes Spiel zuerst).

### Europapokal (Champions League, Europa League, Conference League) – Wunsch des Nutzers vom 24.11.2026

- **„Liga“** meint den Wettbewerb des Spiels (Ligaphase des Europapokals); daneben stehen die **Heimliga**
  (eigene FS-Saison) und die **letzten 6 aller Wettbewerbe**.
- **Rang 2** = letzte 6 aller Wettbewerbe **+** alle Europapokal-Spiele der Ligaphase (auch Heim- und
  Auswärtswerte darin) **+** letzte 6 der Heimliga – im Datenblatt (Feld 4) **immer alle drei Blöcke** je Team.
- **Rang 3** = Saisonwerte der Heimliga am Spielort (daheim/auswärts).
- **Tabelle:** Ist die SM-Tabelle der Ligaphase nicht abrufbar, wird sie aus allen FS-Spielen der Ligaphase
  berechnet (Punkte, dann Tordifferenz, dann Tore; Hinweis, dass die UEFA-Reihenfolge abweichen kann).
  Grenzen: Platz 1–8 Achtelfinale, 9–24 Play-offs, ab 25 ausgeschieden; dazu der Heimliga-Platz.
- **Spielertore im Europapokal** nur aus der Ligaphase (FS-Zahlen enthalten die Qualifikation – kennzeichnen).
- Alle übrigen Regeln (Datenblatt, Lage-Check, Gegenangaben-Prüfung, 7b, Kennzeichnung) gelten unverändert.

## Entscheidungsweg je Paarung (immer in dieser Reihenfolge)

1. **Abrufen und prüfen:** Artikel, Spielseite, Tabelle und Torschützenliste holen; prüfen, dass die Vorschau zu diesem
   Termin gehört und wann sie zuletzt aktualisiert wurde.
2. **FootyStats holen und gegenseitig abgleichen:** Anstoß, letzte Ergebnisse, Tabellenplatz –
   mit `werkzeuge/abgleich.py` (seit 1.3); jede „ABWEICHUNG“ von Hand klären und vermerken; als
   Grund wird nur verwendet, was beide gleich zeigen (Grundsatz 4).
3. **Datenblatt je Team** (seit 1.3, Pflicht; Wunsch des Nutzers vom 21.11.2026: „Vorschau und
   Daten müssen richtig gelesen werden“). Vor jeder Bewertung werden die Fakten je Team in eine
   feste Form übertragen – **nur Fakten mit Quelle, noch keine Bewertung:**
   1. **Tabelle:** Platz, Punkte, Spiele; Abstand nach oben und unten, zum ersten Abstiegs- bzw.
      Relegationsplatz (aus `abgleich.py`, SM-Tabelle).
   2. **Letzte Spiele:** Sports-Mole-Formdaten, neuestes zuerst, je Spiel Wettbewerb und S/U/N
      (aus `sm_spiel.py`); FootyStats letzte 6 Ligaspiele mit Datum.
   3. **Letzter Sieg, letztes Tor:** Datum, Gegner, Ergebnis, Wettbewerb – mit Quelle.
   4. **Zahlen mit Bezug:** jede Zahl mit (a) Liga oder alle Wettbewerbe, (b) gesamt, daheim oder
      auswärts, (c) **Team oder Spiel** – z. B. „Rayo trifft daheim in 80 % seiner Spiele (Team)“
      ist etwas anderes als „in Rayo-Heimspielen treffen beide in 60 % (Spiel)“.
      **Europapokal:** je Team immer alle drei Rang-2-Blöcke – letzte 6 aller Wb., alle Europapokal-Spiele,
      letzte 6 der Heimliga (Abschnitt „Europapokal“ unter „Rangfolge“).
   5. **Teamnews nach dem Originalwort** der Vorschau, getrennt in vier Listen, je Spieler mit dem
      englischen Wortlaut in Klammern:
      - **fehlt:** „ruled out“, „out“, „sidelined“, „will miss“, „injured“ (ohne Einschränkung)
      - **fraglich:** „doubt“, „doubtful“, „fitness test“, „touch and go“, „concern“, „assessed“,
        „could miss“, „uncertain“
      - **gesperrt:** „suspended“, „banned“, „serving a ban“
      - **zurück:** „back“, „returns“, „available again“, „back in training“
      Passt kein Wort eindeutig: „unklar (Wortlaut: …)“ – nie zu „fehlt“ verschärfen.
      **Position je Ausfall** (seit 22.11.2026, Wunsch des Nutzers): Die Position steht nur dabei, wenn
      sie in der Quelle steht – SM-Artikel (z. B. „defensive duo“, „striker“), mögliche Startelf der
      SM-Vorschau oder FootyStats-Spielerdaten (`fs.sh league-players season_id=…`). Sonst:
      „Position nicht in der Quelle“.
   6. **Abweichungen** aus dem Abgleich (Schritt 2).
   7. **Weitere Fakten für den Lage-Check** (seit 21.11.2026): **Trainer** (seit wann, wie viele
      Spiele – steht die Zahl nicht in der Quelle: „nicht in der Quelle“), **Spiele kurz davor und
      danach** mit Datum und Wettbewerb (Belastung – nur mit Datum, sonst keine Belastung),
      **Besonderheit** (Derby, Kellerduell, Spitzenspiel, letztes Spiel vor einer Pause) – je mit Quelle.
   **Wirkung:** Lage-Check, Spielbild, Märkte und Tipp (Schritt 4–8) verwenden **nur Angaben aus dem
   Datenblatt**; fehlt eine Angabe, wird sie zuerst mit Quelle ins Datenblatt eingetragen. Jede
   Angabe im Datenblatt wird einmal gegen den Wortlaut der Quelle gelesen (Prüfliste 6b). „We say“
   und Direktvergleiche kommen nie ins Datenblatt.
4. **Lage-Check je Team** (Pflicht, nur Fakten, keine Vermutungen) – fünf Fragen:
   1. **Worum geht es?** Titel, Europa, Aufstieg, Abstieg oder nichts mehr – Platz und
      Punkteabstand nach oben und unten (Tabelle, Artikel).
   2. **Wie dringend sind die Punkte?** z. B. „3 Punkte hinter dem rettenden Platz“, „kann die
      Führung ausbauen“, „Mittelfeld ohne Druck“.
   3. **Serien:** letzter Sieg (Datum, wie viele Spiele her), letztes Tor, Spiele ohne Sieg / ohne
      Tor / ohne Gegentor / ohne Niederlage – aus den Ergebnislisten nachgezählt, mit Angabe Liga
      oder alle Wettbewerbe.
   4. **Schwächung:** wer genau fehlt (Torjäger, Stammtorwart, Abwehrkette, Kapitän), Sperren,
      Trainerwechsel (neuer Trainer – wie viele Spiele?), Belastung (Europapokal/Pokal unter der
      Woche, Reise).
   5. **Besonderheit:** Derby, Kellerduell, Spitzenspiel, letztes Spiel vor einer Pause u. Ä.
   **Wirkung:** Die Lage steht **über den Saisonzahlen** (Rang 3) und kann die Richtung aus den
   Zahlen drehen – aber nur mit konkreten Fakten aus Artikel, Tabelle oder Ergebnislisten (z. B.:
   Favorit mit vielen Ausfällen und zwei Remis in Folge gegen ein Team im Abstiegskampf, das tief
   stehen wird → Sieg-Tipp wird zur Gegenangabe, ein Tormarkt kann der sicherere Tipp sein).
5. **Spielbild je Team** – drei Fragen: **Trifft es? Kassiert es? Gewinnt es?** Die Zahlen dazu
   kommen aus FootyStats (Rang 2–3), Sports Mole korrigiert mit den Teamnews (Rang 1): fehlt z. B.
   der Torjäger, zählt sein bisheriger Torschnitt weniger; fehlen Innenverteidiger, zählen die Gegentore mehr.
   **Ausfälle geben nur mit belegter Position eine Richtung** (seit 22.11.2026, Wunsch des Nutzers):
   Ein Ausfall darf nur dann als Grund für mehr oder weniger Tore (oder für Sieg/Niederlage) dienen,
   wenn seine Position in der Quelle steht. Steht sie nicht dort, gilt: **„Position nicht in der
   Quelle – keine Richtung“**; der Ausfall wird genannt, aber weder als Grund noch als Gegenangabe
   gewichtet. (Anlass: Hull – Brighton, Osasuna – Málaga, Getafe – Atlético am 22.11.)
   Bei einem Widerspruch geht eine **konkrete Nachricht aus Sports Mole** einer Zahl aus FootyStats
   vor (ein gesperrter Kapitän wiegt mehr als ein Saisonwert).
6. **Die sechs Märkte prüfen:** Heimsieg, Auswärtssieg, Beide treffen – Ja, Beide treffen – Nein,
   Über 2,5, Unter 2,5 – je kurz: was spricht dafür, was dagegen (nach Rangfolge gewichtet).
   **Je Markt zuerst Rang 1–2** (Lage, Teamnews, aktuelle Form), **erst danach Rang 3**
   (Saisonwerte); die Gegenangaben-Prüfung aus Schritt 7 gilt schon hier: Ein Markt, gegen den
   Rang 1–2 sprechen, wird nicht durch Saisonwerte zum stärksten (seit 21.11.2026).
7. **Tipp:** Claude bestimmt **selbst** den **sichersten der sechs Märkte** (Kriterium siehe unten)
   – ohne Rechenmodell, Schwellen oder Punkte. Rang 1–2 geben die Richtung, Rang 3 hilft
   bei der Wahl und dreht eine klare Richtung aus Rang 1–2 nicht um. Was dagegen spricht, wird
   genannt. **Es gibt immer genau einen Tipp.**
   **Immer der sicherste der sechs Märkte** (Wunsch des Nutzers vom 20.11.2026): Claude wählt in
   jedem Spiel – ob „beide einig“ oder „geteilt“ – unter den sechs erlaubten Märkten den
   **sichersten, also den, gegen den am wenigsten spricht** (nach Rangfolge gewichtet). In der
   Begründung steht kurz, warum gegen die anderen Märkte mehr spricht. Es wird nie auf andere,
   „sicherere“ Wettarten ausgewichen (keine Doppelte Chance, kein Über 1,5, kein Unter 3,5 o. Ä.).
   **Gegenangaben-Prüfung** (Pflicht seit 21.11.2026, Wunsch des Nutzers): Erst die Richtung aus
   Rang 1–2 (Lage, Teamnews, aktuelle Form), dann Rang 3 (Saisonwerte). Für **jede** Gegenangabe
   aus Rang 1–2 steht ausdrücklich: **„dreht den Tipp: ja/nein, weil …“**. Bei „ja“ wird der Markt
   neu gewählt. Ein Tipp, der nur auf Rang 3 ruht, während Rang 1–2 dagegen sprechen, ist nicht
   erlaubt. (Anlass: Villa – Sunderland, Frankfurt – Hoffenheim, Elversberg – Freiburg am 21.11.)
8. **Kennzeichnung** (genau festgelegt am 21.11.2026): Die **Sports-Mole-Seite** ist Rang 1 –
   Lage-Check und Teamnews (Artikel, Tabelle); die **FootyStats-Seite** sind die Zahlen aus Rang 2–3
   (Form, Heim/Auswärts, Saisonanteile). „**beide einig**“ – beide Seiten zeigen zum Tipp;
   „**geteilt**“ – eine Seite zeigt woandershin oder nicht eindeutig (welche und warum, in einem
   Satz). Die
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
   FootyStats) und steht im Datenblatt (seit 1.3).
5. Kein Rechenmodell, keine Direktvergleiche (H2H), keine Schwellen, keine Punkte. Verboten ist das
   **Zählen von Gründen oder Häkchen als Entscheidungsregel** („7 von 10 Punkten erfüllt“).
   **Erlaubt und im Datenblatt Pflicht** sind Ergebniszählungen aus Formdaten („in 3 der letzten
   5 Ligaspiele ohne Tor“), klargestellt am 21.11.2026.

## Antwortaufbau je Paarung

**In der Tagesliste** genau in der Reihenfolge des Entscheidungswegs (angeglichen am 21.11.2026,
Version 1.3); **im Chat** nur Punkt 7 mit Anstoß und Paarung (Variante 1, siehe „Alles im Chat“):

1. Abgleich Sports Mole ↔ FootyStats (Ergebnis von `abgleich.py`, Abweichungen)
2. **Datenblatt je Team** (Tabelle, letzte Spiele, letzter Sieg/Tor, Zahlen mit Bezug, Teamnews
   nach Originalwort)
3. **Lage-Check je Team** (fünf Fragen)
4. Spielbild je Team: trifft es? kassiert es? gewinnt es? (mit Quelle, Teamnews eingearbeitet)
5. Spielbild gesamt
6. Die sechs Märkte, je kurz dafür/dagegen
7. ✅ **Tipp** mit Gründen, Gegenangaben (jede aus Rang 1–2 mit „dreht den Tipp: ja/nein, weil …“)
   und „beide einig“ / „geteilt“
(Kein „We say“ – seit Version 1.3 nicht mehr verwendet.)

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/sportsmole/JJJJ-MM-TT.md` (Anstoß, Paarung, Liga,
FootyStats-`match_id`, Tipp, „beide einig“/„geteilt“) und werden dort nach Abpfiff mit
den Ergebnissen aus FootyStats ausgewertet: Treffer und Trefferquote, Treffer je Wettart,
**Treffer „beide einig“ gegenüber „geteilt“**; keine Einheiten, keine Quoten, kein „We say“
(ältere Listen behalten ihre We-say-Spalte als Verlauf, sie wird ab dem 21.11.2026 nicht mehr
ausgewertet). Tipps möglichst vor Anpfiff; Tipps
nach Anpfiff werden vermerkt.
