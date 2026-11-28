# Sports-Mole-Check (System B) · Version 1.4.1

## ‼️ OBERSTE PRIORITÄT (Wunsch des Nutzers vom 26.11.2026)

1. **Claude hält sich immer und ohne Ausnahme an dieses System** – egal ob alter oder neuer Chat, alte oder
   neue Sitzung. Keine eigenen Abweichungen, Abkürzungen oder „Auslegungen“; eine mehrdeutige Antwort des
   Nutzers ist keine Erlaubnis für eine Abweichung – dann wird nachgefragt.
2. **Der Nutzer schickt die Spiele in Schritten zu je 5 Spielen.** Claude bearbeitet jeden Schritt vollständig
   nach dem System (jede Paarung einzeln, Prüfliste, Kontrollstufen 1–3) und schickt die Tipps mit dem
   Kontrollergebnis; erst danach kommt der nächste Schritt. **Alle 5 Tipps eines Schritts kommen zusammen**, fertig
   und geprüft vor dem **ersten Anstoß** dieser 5 Spiele (Wahl des Nutzers vom 27.11.2026, Variante a). Auf Wunsch des Nutzers
   läuft davor eine **Vorprüfung** (Abschnitt „Vorprüfung“, seit 28.11.2026) – die 5 Spiele wählt weiter der Nutzer.
3. **Prüfer: genau einer.** Für die unabhängige Kontrolle (Stufe 3) gibt es **einen** Prüfer; jeder weitere
   5er-Schritt geht per Weiterführung an **denselben** Prüfer (nur wenn das nicht geht, z. B. im neuen Chat, startet ein
   neuer). Zusätzlich nur: bei einem Grenzfall mit „Spielen: ja“ (seit 27.11.2026) **ein** neuer Prüfer für die kurze
   Grenzfall-Runde und eine weitere Runde, wenn der Nutzer „unabhängige Kontrolle“ schreibt. **Nie mehrere Prüfer gleichzeitig.**
4. **Variante B „drei Augenpaare“** (Wahl des Nutzers vom 27.11.2026): Je 5er-Schritt bearbeitet je Spiel **ein**
   Agent (`bearbeiter`, `.claude/agents/bearbeiter.md`) genau diese eine Paarung vollständig nach dem
   Entscheidungsweg 1–8. Die Agenten werden **frisch gestartet** – nur mit dem kurzen Auftrag und den Regel-Dateien,
   **ohne Kopie des Chats**; höchstens 5 gleichzeitig (ein Schritt). Danach liest **Claude selbst** jede Aussage gegen die
   Quellen (Stufe 1), dann prüft **ein** Prüfer alle 5 (Punkt 3); erst danach gehen die Tipps an den Nutzer. Für die
   Bearbeitung ersetzt das „erst eine Paarung, dann die nächste“: Jeder Agent bearbeitet genau eine Paarung einzeln.

(Anlass: 26.11.2026 – parallele Agenten und 5 Prüfer statt Ablauf nach System, Nutzungslimit erreicht, kein
Tipp vor Anpfiff.)

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
(22.11.); Platzverweise in der Auswertung gesondert mitzählen (24.11.); Abschnitt **Europapokal** (24.11.);
Merkmale-Zeile je Tipp (25.11.) mit zweitbestem Markt (26.11.); Regel 7c – nur neue Ausfälle/sichere Rückkehrer als
Rang-1-Grund (26.11.); **Oberste Priorität** mit 5er-Schritten, einem Prüfer und Variante B „drei Augenpaare“ (26./27.11.).
**Version 1.4** (27.11.2026, Wunsch des Nutzers nach der Auswertung aller Tipps vom 20.–26.11.): (1) Pflicht-Schritt
**Kräfteverhältnis** (Schritt 4b) mit Ausschlussregeln für Tor-Märkte bei klarem Favoriten; (2) **gespielt wird nur „beide
einig“** – „geteilt“ ist nur Beobachtung (Schritt 8); (3) **Vorrang Sieg-Markt**, wenn Lage und Kräfteverhältnis klar zum selben
Team zeigen (Schritt 7). Anlass und Zahlen: `tipps/sportsmole/analyse-2026-11-27.md`.
**Sparplan (27.11.2026, Wunsch des Nutzers – „mehr Spiele bei höchster Qualität“):** (1) **Datenblatt-Werkzeug**
`werkzeuge/datenblatt.py` ist Pflicht für die Zahlen (Schritt 2–4b); (2) Bearbeiter lesen `FEHLERPROTOKOLL-KURZ.md` statt der
Vollfassung; (3) **Grenzfall-Runde nur für Paarungen mit „Spielen: ja“**; (4) der Prüfer gleicht die Zahlen mit dem Werkzeug ab
und prüft vor allem Teamnews-Wortlaut, Regel 7c, Gegenangaben, Kräfteverhältnis und Abwägung.
**Version 1.4.1** (28.11.2026, Wunsch des Nutzers nach der Systemprüfung – „1–3 umsetzen“): Die Tippregeln von 1.4 bleiben; sie
werden eindeutiger und messbar. (1) **Feste Sätze** im Kräfteverhältnis (Schritt 4b: je Baustein „zeigt zu: Heim / Gast / keinem“)
und bei der Kennzeichnung (Schritt 8: je Seite „zeigt: zum Tipp / woandershin / nicht eindeutig“); (2) **Spielort** als Gegenprobe
in 4b; (3) **Spiele gegen unterklassige Pokalgegner** zählen nicht für die 3+-Tore-Regeln (4b und feste Unter-2,5-Gegenangabe);
(4) **Musterfälle** (`MUSTERFAELLE.md`) und **Vorlage** für den Abschnitt (`VORLAGE-ABSCHNITT.md`); (5) **Stichprobe von Hand** durch
den Prüfer (eine Paarung je Schritt); (6) **Schattentipp** und „Tabellenhöher“ in der Merkmale-Zeile, **Auswertung erst nach 50
gespielten Tipps**, Abschnitt „Änderungen am System“; (7) Werkzeuge: `datenblatt.py` prüft Regel 7c am letzten Pflichtspiel
(auch Europapokal) und gleicht SM ↔ FS in beide Richtungen ab; `tippanalyse.py` wertet 1.4 getrennt aus. Version 1.4 liegt in
`archiv/SPORTSMOLE-CHECK-1.4.md`.
**Ergänzung zu 1.4.1 – Vorprüfung** (28.11.2026, Wunsch des Nutzers: „Ja einbauen“): Vor der Spielauswahl zählt
`werkzeuge/vorpruefung.py` für alle Spiele einer Liga mit Vorschau die Zahlenseite; Claude nennt je Spiel, wohin die Zahlen zeigen;
der Nutzer wählt seine 5; Merkmal 13 hält fest, ob ein Spiel aus der Vorprüfung gewählt wurde (Abschnitt „Vorprüfung“).
**Ergänzung zu 1.4.1 – Zweitquelle Teamnews, Probelauf** (28.11.2026, Wunsch des Nutzers: frei zugängliche Quellen der jeweiligen
Länder): `werkzeuge/teamnews2.py` stellt die Ausfall- und Sperrenlisten der Länderquellen neben die Sports-Mole-Teamnews – **nur als
Abgleich, ohne Einfluss auf den Tipp**; Merkmal 14 hält das Ergebnis fest (Abschnitt „Zweitquelle Teamnews – Probelauf“).
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
- Erst wenn die Prüfliste für alle 5 Paarungen eines Schritts erfüllt ist, gehen deren Tipps an den Nutzer.
  Ein Verstoß, der vorher auffällt, wird vor der Antwort behoben.
- Ausnahmen oder Änderungen nur auf ausdrücklichen Wunsch des Nutzers; Claude macht keine eigenen.

**Arbeitsweise je Paarung** (Wunsch des Nutzers vom 21.11.2026):

- **Jede Paarung einzeln, Schritt für Schritt** (Entscheidungsweg 1–8: Abrufen, Abgleich,
  Datenblatt, Lage, Kräfteverhältnis (4b, seit 1.4), Spielbild, Märkte, Tipp, Kennzeichnung): Je Paarung arbeitet **ein eigener Agent**
  (Oberste Priorität, Punkt 4) und geht den Entscheidungsweg für genau diese Paarung vollständig durch; ein
  Agent bearbeitet nie mehrere Paarungen (angeglichen am 27.11.2026).
- **5er-Schritte** (Wahl des Nutzers vom 27.11.2026, ersetzt die „Gruppen nach Anstoßzeit“ vom 21.11.2026):
  **Die 5 Tipps eines Schritts gehen erst zusammen an den Nutzer, wenn jede der 5 Paarungen fertig und geprüft ist**
  (Prüfliste, Kontrolldurchgang durch Claude, **automatische unabhängige Kontrolle** mit Korrekturen) – vor dem
  ersten Anstoß dieser 5 Spiele. Dann folgt der nächste Schritt.
- **Reicht die Zeit bis zum ersten Anstoß nicht**, sagt Claude das dem Nutzer gleich zu Beginn offen,
  statt abzukürzen (welche Spiele nicht mehr vollständig geschafft werden).

**Alles im Chat** (Wunsch des Nutzers vom 21.11.2026): Der Nutzer liest die Dateien nicht. Alles,
was er wissen muss, steht **vollständig im Chat**, handytauglich als Liste:

- je Paarung (Variante 1, Wahl des Nutzers vom 21.11.2026): **Anstoß, Paarung, Tipp mit
  Kennzeichnung, „Spielen: ja/nein“ (seit 1.4), das Kräfteverhältnis in einem Satz (seit 1.4), die Gründe und alle Gegenangaben – jede aus Rang 1–2 mit „dreht den Tipp: ja/nein,
  weil …“**. Datenblatt, Lage-Check und Spielbild stehen vollständig in der Tagesliste, nicht im Chat;
- Ergebnisse jeder Kontrolle mit jedem gefundenen Fehler und jeder Korrektur;
- jeder neue Eintrag ins Fehlerprotokoll und was daraus folgt;
- die Auswertung.

Ein PDF nur auf ausdrücklichen Wunsch. Tagesliste und Fehlerprotokoll bleiben als Ablage.

## Vorprüfung (Ergänzung zu 1.4.1, Wunsch des Nutzers vom 28.11.2026)

Zweck: mehr **gespielte** Tipps je Aufwand. Am 27.11. waren 9 von 10 Tipps „geteilt“ (nur Beobachtung); die Vorprüfung zeigt vor
der Auswahl, bei welchen Spielen wenigstens die Zahlenseite klar in eine Richtung zeigt.

- **Auslöser:** Der Nutzer schreibt „Vorprüfung <Liga oder Ligen> [Tag]“. Ohne diesen Wunsch gibt es keine Vorprüfung.
- **Ablauf:** Claude lässt `werkzeuge/vorpruefung.py "<Liga>" [Wochentag]` laufen – **ohne Agenten** – für alle Spiele der Liga mit
  Sports-Mole-Vorschau. Das Werkzeug zählt nur: die vier Bausteine aus Schritt 4b (Tabelle, letzte 6 alle Wb., letzte 6 Liga,
  Gegnerstärke), den Spielort und die Tor-Zahlen der letzten 6 beider Teams.
- **Im Chat je Spiel** (Liste, erst die Spiele mit Richtung): Anstoß, Paarung und **ein fester Satz „Zahlen zeigen zu: Heimsieg /
  Auswärtssieg / <Tor-Markt> / keinem – weil …“**. „Heimsieg/Auswärtssieg“ nur, wenn alle vier Bausteine zum selben Team zeigen
  und der Spielort nicht zum anderen (wie Schritt 4b). Ein Tor-Markt nur, wenn **alle** Rang-2-Blöcke **beider** Teams (letzte 6
  Liga und letzte 6 alle Wb.) deutlich zu diesem Markt zeigen. **Im Zweifel „keinem“.** Keine Schwellen, keine Punkte – der
  Halbsatz nennt die Zahlen. Jede Abweichung und jeder Hinweis des Werkzeugs wird mitgenannt.
- **Was die Vorprüfung nicht ist:** kein Tipp und keine Empfehlung zu spielen. Sie sieht **nur die Zahlenseite** – keine Teamnews,
  keine Lage, keine Regel 7c, keine Gegenangaben-Prüfung, keine Kontrolle. Ob auch die Sports-Mole-Seite passt („beide einig“),
  zeigt erst die volle Analyse; der Tipp dort kann ein anderer Markt sein als die Richtung der Vorprüfung. Claude sagt das bei
  jeder Vorprüfung dazu.
- **Auswahl:** Die 5 Spiele wählt der Nutzer – auch Spiele mit „keinem“ oder Spiele außerhalb der Vorprüfung. Danach läuft der
  Ablauf unten **unverändert und vollständig**.
- **Kein Anker:** Bearbeiter und Prüfer bekommen das Ergebnis der Vorprüfung **nicht** (weder im Auftrag noch in der Tagesliste, bis
  die Tipps fertig und geprüft sind). Erst danach trägt Claude Merkmal 13 ein.
- **Messen:** Merkmal 13 je Tipp („Vorprüfung: ja – Zahlen zeigten zu: … / nein“); `werkzeuge/tippanalyse.py` zählt getrennt,
  wie oft daraus „Spielen: ja“ wurde und wie die Tipps ausgingen. Die Vorprüfung ändert keine Tippregel.

## Zweitquelle Teamnews – Probelauf (Ergänzung zu 1.4.1, Wunsch des Nutzers vom 28.11.2026)

Zweck: Für die Zahlen gibt es zwei Quellen, für Teamnews und Lage nur Sports Mole. Der Probelauf misst, wie oft frei zugängliche
Listen der jeweiligen Länder von Sports Mole abweichen und ob das einen Tipp betroffen hätte. Test am 28.11. (Mainz – Union
Berlin): 7 Ausfälle in allen Quellen gleich; die deutsche Liste führte einen Spieler „seit gestern“, der bei Sports Mole fehlte;
die englische Sammelseite führte einen Spieler als gesperrt, den Sports Mole in der möglichen Startelf nennt.

- **Quellen** (frei zugänglich, ohne Schlüssel; Stand 28.11.2026 von hier erreichbar):
  - Deutschland (Bundesliga): **LigaInsider** – Spieler, Art, Grund, „fehlt seit“.
  - Spanien (La Liga), dazu Champions League und Europa League: **FútbolFantasy** – Verletzte mit „desde“ (seit) und Einsatzchance
    (die Sperrenliste dieser Seite ist nicht lesbar – Sperren dort nur über die Sammelseite).
  - Italien (Serie A): **Fantacalcio** – Infortunati (verletzt), Squalificati (gesperrt), Diffidati (Sperre droht, kein Ausfall).
  - England (Premier League): **offizielle Fantasy-Liste der Premier League** – Status, Position, Einsatzchance, Zeitpunkt der Meldung.
  - Alle Ligen als Ergänzung, einzige Quelle für Frankreich, Niederlande, Portugal, Türkei, Schottland, Championship,
    2. Bundesliga: **Sammelseite Sportsgambler** – im Test weniger verlässlich; was nur sie zeigt, ist kein Beleg.
  - Gesperrt für automatischen Abruf und darum nicht verwendet: kicker, L'Équipe, Transfermarkt, UEFA.com. Sperren werden nicht umgangen.
  - Von diesen Seiten werden **nur die Listen** gelesen – keine Quoten, Tipps, Vorhersagen, Direktvergleiche.
- **Ablauf:** Nach Stufe 3 (und der Grenzfall-Runde), vor dem Senden der Tipps, lässt **Claude selbst** je Paarung
  `werkzeuge/teamnews2.py "<Liga>" "<Heim>" "<Gast>" --spieler-heim "…" --spieler-gast "…"` laufen (Namen = die Spieler aus den
  Sports-Mole-Teamnews im Datenblatt). **Bearbeiter und Prüfer verwenden die Zweitquelle nicht.**
- **Kein Einfluss auf den Tipp** (Probelauf): Was nur in der Zweitquelle steht, ist weder Grund noch Gegenangabe und ändert weder
  Tipp noch Kennzeichnung noch „Spielen: ja/nein“.
- **Einstufung durch Claude** (das Werkzeug zählt nur Namen): „**bestätigt**“ – die Länderquelle führt dieselben Ausfälle und Sperren
  mit demselben Status, nichts Zusätzliches; „**weicht ab**“ – ein Spieler fehlt in einer der beiden Quellen oder der Status ist ein
  anderer (wer, was, seit wann); „**nicht verfügbar**“ – keine Quelle für diese Liga, Seite nicht erreichbar oder Team nicht gefunden.
  Abweichungen, die nur die Sammelseite zeigt, werden genannt, zählen aber nicht als „weicht ab“.
  Dazu „**Rang 1 betroffen: ja/nein**“: ja, wenn die Abweichung – wäre sie belegt – nach Regel 7b/7c ein Rang-1-Grund oder eine
  Rang-1-Gegenangabe gewesen wäre (neuer Ausfall oder sichere Rückkehr mit belegter Position, oder Sports Mole führt einen neuen
  Ausfall, den die Länderquelle nicht kennt).
- **Statuswörter der Quellen** bleiben im Original stehen: deutsch „Verletzung“ = fehlt, „angeschlagen“ = fehlt oder fraglich
  (Wortlaut lesen), „Aufbautraining“ = unklar, „5. Gelbe Karte“/„Rote Karte“ = gesperrt; spanisch „baja“ = fehlt, „duda“ = fraglich,
  Einsatzchance 0 % = fehlt; italienisch „infortunato“ = verletzt, „squalificato“ = gesperrt, „diffidato“ = Sperre droht (kein Ausfall),
  „da valutare“/„in dubbio“ = fraglich; englisch „injured“ = fehlt, „doubtful“ = fraglich, „suspended“ = gesperrt.
- **Im Chat** je Paarung eine Zeile „Zweitquelle: bestätigt / weicht ab (wer, was) / nicht verfügbar“. Bei „Rang 1 betroffen: ja“
  deutlich hervorgehoben mit dem Zusatz „im Tipp nicht berücksichtigt (Probelauf)“ – was der Nutzer daraus macht, entscheidet er.
- **Merkmal 14** je Tipp; `werkzeuge/tippanalyse.py` zählt mit. Nach etwa 50 Tipps mit Zweitquelle berichtet Claude, wie oft sie
  abwich und wie oft Rang 1 betroffen war; ob die Zweitquelle dann mitentscheiden soll, entscheidet nur der Nutzer.
- **Fällt eine Quelle aus** (gesperrt, Aufbau geändert), meldet das Werkzeug das; der Ablauf läuft unverändert mit Sports Mole weiter.

## Ablauf eines Auftrags

Der Nutzer schickt die Spiele **in Schritten zu je 5** (Oberste Priorität, Punkt 2), z. B. fünf Paarungen der
League One. Schickt er mehr als 5 Spiele auf einmal, fragt Claude, welche 5 zuerst. Dann:

0. Claude liest zuerst das **Fehlerprotokoll** (`FEHLERPROTOKOLL.md`) und achtet beim Schreiben auf
   jede Fehlerart (seit 1.3, Wunsch des Nutzers vom 21.11.2026).
1. Claude sucht die 5 Paarungen in der Sports-Mole-Vorschau-Übersicht
   (`werkzeuge/sm_spiel.py tag "<Liga>" [Wochentag]`, Anstoß in deutscher Zeit).
2. Claude gleicht mit dem FootyStats-Spielplan ab (Anstoß, match_id); Spiele ohne Sports-Mole-Vorschau werden
   als „nicht bewertet (keine Vorschau)“ aufgeführt. Claude sagt mit Uhrzeit, ob die 5 bis zum ersten Anstoß fertig werden.
3. Claude startet je Paarung **einen frischen Agenten** (`bearbeiter`, ohne Kopie des Chats). Er holt die vier
   Sports-Mole-Teile (`werkzeuge/sm_spiel.py "<Heim>" "<Gast>"`), das **Datenblatt-Werkzeug**
   (`werkzeuge/datenblatt.py <season_id> "<FS-Heim>" "<FS-Gast>" --sm … --spieler-heim … --spieler-gast …`, seit 27.11.2026
   Pflicht; im Europapokal zusätzlich `--liga-heim`/`--liga-gast` mit den Heimliga-Saisons) und bei Bedarf weitere FootyStats-Zahlen (`werkzeuge/fs_spiel.py <season_id> "<Heim>" "<Gast>"`), lässt den automatischen Abgleich laufen
   (`werkzeuge/abgleich.py <season_id> "<Heim>" "<Gast>"`), legt das Datenblatt je Team an und geht den
   Entscheidungsweg unten durch – je Paarung genau ein Tipp. Aufbau des Abschnitts: `VORLAGE-ABSCHNITT.md`; Einstufungen
   (Kräfteverhältnis, Kennzeichnung) nach den festen Sätzen und den Musterfällen in `MUSTERFAELLE.md` (seit 1.4.1).
4. Claude fügt die 5 Abschnitte der Agenten in die Tagesliste ein und liest jeden selbst gegen die Quellen (Stufe 1), danach prüft **ein** Prüfer alle 5 (Stufe 3) –
   bei **einer** von Claude benannten Paarung zählt er die Zahlen von Hand nach (Stichprobe, seit 1.4.1);
   Korrekturen werden eingearbeitet; bei einem Grenzfall mit „Spielen: ja“ folgt danach die kurze Grenzfall-Runde (ein neuer
   Prüfer); Grenzfälle mit „Spielen: nein“ bekommen keine zweite Runde (seit 27.11.2026).
5. Alle Tipps kommen mit dem vollständigen Antwortaufbau in die Tagesliste; im Chat steht je Paarung,
   was unter „Alles im Chat“ festgelegt ist (Variante 1), mit dem Kontrollergebnis, handytauglich als Liste statt
   breiter Tabellen.

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
     Wortlaut der Quelle gelesen** (Zahlen aus `werkzeuge/datenblatt.py` gelten als nachgezählt – seit 27.11.2026; Aussagen
     des SM-Artikels weiter gegen den Wortlaut); `abgleich.py` gelaufen, jede „ABWEICHUNG“ geklärt und vermerkt;
     im Spielbild, in den Märkten und im Tipp steht nichts, was nicht im Datenblatt steht.
7. Jeder Ausfall, jede Sperre, jeder Rückkehrer dem **richtigen Team** zugeordnet – mit Status nach
   dem **Originalwort** der Vorschau (fehlt / fraglich / gesperrt / zurück, siehe Schritt 3).
   - **7a:** Lage-Check für **beide** Teams mit allen fünf Fragen gemacht (worum es geht,
     Dringlichkeit, Serien mit Datum des letzten Siegs und Tors, Schwächung, Besonderheit).
   - **7b (seit 22.11.2026):** Kein Ausfall ohne belegte Position ist als Grund oder Gegenangabe für
     mehr/weniger Tore oder Sieg/Niederlage verwendet; sonst steht „Position nicht in der Quelle –
     keine Richtung“.
   - **7c (seit 26.11.2026):** Als Rang-1-Grund oder -Gegenangabe nur Spieler, die neu fehlen (spielten im letzten
     Pflichtspiel laut FS-Aufstellung) oder sicher zurück sind (fehlten im letzten Spiel, Quelle sagt klar „spielt“);
     sonst im Datenblatt „nicht neu – keine Richtung“ (Schritt 5).
   - **7d (seit 1.4):** Kräfteverhältnis (Schritt 4b) gemacht – Tabellenabstand, Gegnerstärke der letzten 6 je Team,
     Einstufung mit Begründung; die Ausschlussregeln bei „klarer Favorit“ beachtet. **Seit 1.4.1:** die vier Bausteine und der
     Spielort je mit dem festen Satz „zeigt zu: Heim / Gast / keinem – weil …“; „klarer Favorit“ nur, wenn alle vier Bausteine zum
     selben Team zeigen und der Spielort nicht zum anderen; Spiele gegen unterklassige Pokalgegner bei den 3+-Tore-Regeln nicht
     mitgezählt (Schritt 4b).
8. Gegenseitiger Abgleich gemacht (letzte Ergebnisse, Tabellenplatz);
   Abweichungen vermerkt, nur übereinstimmende Angaben als Grund verwendet.
   - **8a:** Kennzeichnung „beide einig“ oder „geteilt“ gesetzt und bei „geteilt“ begründet – seit 1.4.1 mit den zwei festen
     Sätzen (SM-Seite / FS-Seite „zeigt: zum Tipp / woandershin / nicht eindeutig – weil …“); „beide einig“ nur, wenn beide „zum
     Tipp“ lauten (Schritt 8).
   - **8b (seit 1.4):** „Spielen: ja“ nur bei „beide einig“, sonst „Spielen: nein – nur Beobachtung“ (Tagesliste und Chat).
9. Tipp ist der sicherste der sechs Märkte (seit 1.4: unter den nach Schritt 4b erlaubten Märkten; Vorrang Sieg-Markt nach Schritt 7 geht vor) (gegen ihn spricht am wenigsten; bei den anderen
   Märkten kurz gesagt, warum mehr dagegen spricht). Tipp passt zur Begründung: Die genannten Gründe tragen genau diesen Markt; **alle**
   Angaben aus Rang 1–2, die gegen den Tipp sprechen, sind genannt (auch Ausfälle beim Gegner und
   Ergebnisse unter einem neuen Trainer, Lage beider Teams); Richtung aus Rang 1–2, Rang 3 dreht sie
   nicht um. **Bei jeder Rang-1–2-Gegenangabe steht „dreht den Tipp: ja/nein, weil …“; bei „ja“
   ist der Markt neu gewählt** (seit 21.11.2026). **Seit 1.4:** Vorrang Sieg-Markt geprüft (Schritt 7), bei „klarer Favorit“
   kein Beide treffen – Ja und Über 2,5 nur mit der Favoriten-Bedingung (Schritt 4b).
10. Keine Quoten, kein Rechenmodell (weder Sports-Mole-Datenanalyse noch FootyStats-Vorab-Werte),
    **keine Direktvergleiche (H2H)**, keine Schwellen, keine Punkte, **kein „We say“** verwendet –
    auch nicht nebenbei in Datenblatt, Spielbild oder Gegenangaben.

**Abschluss**

11. Tagesliste vollständig (alle Spalten, Gründe je Paarung, **Merkmale-Zeile je Tipp** – seit 25.11.2026; seit 1.4.1 mit den
    Punkten 1–12, also auch „Tabellenhöher“ und Schattentipp; Punkte 13 „Vorprüfung“ und 14 „Zweitquelle“ von Claude nach der Kontrolle ergänzt), committet und auf den Arbeitsbranch
    **und** `forebet-system` gepusht.
12. **Nur bei der Auswertung:** nach Abpfiff alle Ergebnisse aus FootyStats eingetragen und ausgewertet – kein Spiel vergessen.
    Je Spiel auch Platzverweise aus FootyStats (`card_details`: Team, Minute, Spielstand) vermerken und
    gesondert mitzählen (Wunsch des Nutzers vom 24.11.2026) – nur zur Beobachtung, die Wertung bleibt.
13. Verbindlichkeit eingehalten: jeder Punkt des Systems für jede Paarung erfüllt, nichts
    umgangen; was nicht erledigt werden konnte, ist offen genannt (ergänzt am 21.11.2026).
14. **Fehlerprotokoll:** vor der Analyse gelesen (Claude und Prüfer die Vollfassung, Bearbeiter `FEHLERPROTOKOLL-KURZ.md`); jede Fehlerart gezielt geprüft; jeder in
    dieser Runde gefundene Fehler dort eingetragen (seit 1.3).
15. **Stichprobe von Hand (seit 1.4.1):** Im Auftrag an den Prüfer ist eine Paarung des Schritts als Stichprobe benannt (bevorzugt
    eine mit „Spielen: ja“, sonst wechselnd); ihr Ergebnis steht im Kontrollergebnis.

**Drei Kontrollstufen** (keine Garantie möglich, darum mehrfach geprüft):

- **Stufe 1 – Kontrolldurchgang (automatisch):** Nach der Analyse und vor der Antwort liest Claude **selbst**
  (nicht der Agent) jede Aussage der Tagesliste noch einmal gegen die Quelle (Vorschau, Spielseite, Tabelle,
  FootyStats; seit 27.11.2026 die Zahlen durch einen eigenen Lauf von `werkzeuge/datenblatt.py` und den Vergleich mit dem
  Datenblatt der Tagesliste) und geht die Prüfliste und jede Fehlerart des Fehlerprotokolls durch. Erst danach gehen die Tipps an den Nutzer.
- **Stufe 2 – Prüffrage des Nutzers:** Schreibt der Nutzer **„Kontrolle“**, prüft Claude alles
  von vorn: Quellen neu abrufen, jede Zahl, jedes Ergebnis, jede Zuordnung, jeden Tipp gegen die
  Gründe, jede Fehlerart des Fehlerprotokolls, den Entscheidungsweg Schritt 1–8 und bei jeder
  Paarung die Gegenangaben-Prüfung („dreht den Tipp: ja/nein, weil …“). Wird eine neue Gegenangabe
  aus Rang 1–2 gefunden, wird der Tipp **immer neu abgewogen** (vor Anpfiff; angeglichen an Stufe 3
  am 21.11.2026). Antwort: „keine Fehler gefunden“ oder jeder Fehler mit Korrektur; in der Tagesliste wird
  „Kontrolle (Uhrzeit): …“ vermerkt.
- **Stufe 3 – unabhängige Kontrolle (seit 20.11.2026; seit 21.11.2026 automatisch, Wunsch des
  Nutzers):** Nach jeder Analyse – je 5er-Schritt, nach Prüfliste und Kontrolldurchgang – startet Claude
  **von selbst, ohne Aufforderung**, einen zweiten, unabhängigen Prüfer. Der Prüfer ist der Projekt-Agent
  `pruefer` (`.claude/agents/pruefer.md`, fester Prüfauftrag); weitere 5er-Schritte gehen per
  Weiterführung an denselben Prüfer, geht das nicht (z. B. im neuen Chat oder nach einem Neustart), startet ein neuer
  (Wunsch des Nutzers vom 24.11.2026, angeglichen am 27.11.2026). Nie mehrere Prüfer gleichzeitig. **Zweite, kurze Runde für Grenzfälle** (eingeführt am 24.11.2026, Wunsch des
  Nutzers; seit 27.11.2026 nur für „Spielen: ja“): Nach den Korrekturen der ersten Runde prüft ein **neuer** Prüfer (Agent
  `pruefer`) nur die Paarungen mit „Spielen: ja“, die in Schritt 7 als **Grenzfall** vermerkt sind (zwei Märkte fast gleich stark), und dort nur die Tipp-Gründe,
  die Rang-1–2-Gegenangaben und den sichersten Markt. Gibt es in einem Schritt keinen Grenzfall mit „Spielen: ja“, entfällt sie.
  Ihr Ergebnis steht mit im Kontrollergebnis. Sie verbessert die Herleitung, nicht den Spielausgang. Erst nach seinem Bericht
  und den Korrekturen gehen die 5 Tipps des Schritts an den Nutzer, im Chat zusammen mit dem
  Kontrollergebnis (gefundene Fehler, Korrekturen, geänderte Tipps – oder „keine Fehler gefunden“).
  Schreibt der Nutzer zusätzlich **„unabhängige Kontrolle“**, folgt eine weitere Runde. Reicht die
  Zeit bis zum ersten Anstoß dafür nicht, sagt Claude das vorher offen. Je Spieltag wird vermerkt, was die
  Kontrolle gefunden hat (Erprobung von 1.3: findet sie über mehrere Spieltage nichts, was einen
  Tipp betrifft, kann der Nutzer entscheiden, sie seltener zu verlangen). Der Prüfer ist eine eigene Claude-Instanz, die
  die Analyse aus dem Gespräch nicht kennt. Er liest Regeln, Fehlerprotokoll und Tagesliste, ruft alle Quellen selbst neu
  ab (Sports Mole, FootyStats; die Zahlen gleicht er seit 27.11.2026 mit einem eigenen Lauf von `werkzeuge/datenblatt.py` ab, statt
  sie von Hand nachzuzählen – sein Schwerpunkt sind Teamnews-Wortlaut, Regel 7b/7c, Gegenangaben, Kräfteverhältnis und Abwägung;
  **Stichprobe von Hand, seit 1.4.1:** bei **einer** von Claude benannten Paarung je Schritt – bevorzugt eine mit „Spielen: ja“, sonst
  wechselnd – zählt der Prüfer die Zahlen des Datenblatts selbst aus den Rohdaten nach (FS-`league-matches`, SM-Spielseite), ohne das
  Werkzeug, damit ein Fehler des Werkzeugs nicht an Bearbeiter, Claude und Prüfer zugleich vorbeigeht; weicht etwas ab, ist das ein
  Werkzeugfehler: ins Fehlerprotokoll (M), dem Nutzer melden, alle 5 Paarungen des Schritts von Hand nachzählen) und prüft Vollständigkeit, Anstoß, jede Aussage mit Teamzuordnung,
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
- Alle übrigen Regeln (Datenblatt, Lage-Check, Kräfteverhältnis 4b, Gegenangaben-Prüfung, 7b, Kennzeichnung, Spielen) gelten
  unverändert. **Datenblatt-Werkzeug im Europapokal:** `datenblatt.py <Europapokal-Saison> … --sm …` liefert die Ligaphase
  (Tabelle und Spiele ab 01.09., ohne Qualifikation) und die letzten 6 aller Wb.; den Block „letzte 6 der Heimliga“ liefert
  `kontext.py <team_id> <Heimliga-Saison>` je Team. 4b im Europapokal: Tabelle = Ligaphase **und** Heimliga-Platz.

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
      „Position nicht in der Quelle“. **Neu oder nicht** (seit 26.11.2026, Regel 7c): je Ausfall/Rückkehrer der Einsatz im
      letzten Pflichtspiel laut FS-Aufstellung (Startelf / eingewechselt / Bank / nicht im Kader) und „neu“ oder „nicht neu –
      keine Richtung“.
   6. **Abweichungen** aus dem Abgleich (Schritt 2).
   7. **Weitere Fakten für den Lage-Check** (seit 21.11.2026): **Trainer** (seit wann, wie viele
      Spiele – steht die Zahl nicht in der Quelle: „nicht in der Quelle“), **Spiele kurz davor und
      danach** mit Datum und Wettbewerb (Belastung – nur mit Datum, sonst keine Belastung),
      **Besonderheit** (Derby, Kellerduell, Spitzenspiel, letztes Spiel vor einer Pause) – je mit Quelle.
   **Datenblatt-Werkzeug** (Pflicht seit 27.11.2026): Die Zahlen der Felder 1–4, die Gegnerstärke für Schritt 4b, die Startelf des
   letzten Ligaspiels und die Regel-7c-Prüfung der Teamnews-Spieler kommen aus `werkzeuge/datenblatt.py` und werden **wörtlich
   übernommen** (nicht neu gezählt). Der Agent ergänzt den Teamnews-Status nach Originalwort (Feld 5), was das Werkzeug nicht
   kann (Aufstellungen nationaler Pokalspiele, Spieler ohne FS-Eintrag), und klärt jede gemeldete Abweichung. **Seit 1.4.1:** Das
   Werkzeug prüft Regel 7c am **letzten Pflichtspiel, das FS führt** (Liga und Europapokal; im Europapokal mit `--liga-heim`/
   `--liga-gast` auch die Heimliga) und warnt, wenn das neueste Spiel der SM-Formdaten ein nationales Pokalspiel war (dann 7c laut
   SM-Artikel prüfen). Es gleicht SM ↔ FS **in beide Richtungen** ab: Ein FS-Spiel, das in den SM-Formdaten fehlt, wird als
   Abweichung gemeldet und in den Block „letzte 6 alle Wb.“ aufgenommen. Jede Zeile „Abweichungen“ und „Hinweise zur Zuordnung“
   wird geklärt und vermerkt.
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
4b. **Kräfteverhältnis** (Pflicht seit Version 1.4, Wunsch des Nutzers vom 27.11.2026; feste Sätze seit 1.4.1) – nach dem
   Lage-Check, vor dem Spielbild, nur Fakten aus dem Datenblatt (fehlt eine Angabe, wird sie zuerst mit Quelle eingetragen):
   1. **Vier Bausteine, je mit dem festen Satz „zeigt zu: Heim / Gast / keinem – weil …“** (die Fakten in einem Halbsatz):
      - **(a) Tabelle:** Platz, Punkte und Punkte je Spiel beider Teams und der Abstand zwischen ihnen (Liga; im Europapokal
        Ligaphase **und** Heimliga).
      - **(b) Letzte 6 aller Wettbewerbe** beider Teams (S-U-N, Tore).
      - **(c) Letzte 6 Liga** beider Teams (S-U-N, Tore; im Europapokal alle Spiele der Ligaphase **und** die letzten 6 der
        Heimliga – zeigt einer der beiden Blöcke woandershin, lautet der Satz „keinem“).
      - **(d) Gegnerstärke der letzten 6** (alle Wettbewerbe) je Team: zu jedem Formspiel der aktuelle Tabellenplatz des Gegners
        (Pokalgegner aus anderen Ligen: Spielklasse laut Quelle, sonst „nicht in der Quelle“); daraus Ergebnisse, eigene Tore und
        Gegentore gegen Gegner aus der oberen und aus der unteren Tabellenhälfte.
      Ein Baustein zeigt zu dem Team, das darin **deutlich** besser dasteht. Liegen beide nah beieinander oder lässt sich der
      Baustein in beide Richtungen lesen, lautet der Satz „zeigt zu: keinem“ – **im Zweifel „keinem“**. Keine Schwellen, keine
      Punkte: Der Halbsatz nennt die Fakten, der Prüfer liest sie nach (Musterfälle: `MUSTERFAELLE.md`).
   2. **Spielort als Gegenprobe (seit 1.4.1):** Liga-Bilanz des Heimteams daheim und des Gastteams auswärts (Saison, Rang 3, aus
      dem Werkzeug) mit dem Satz „Spielort zeigt zu: Heim / Gast / keinem – weil …“.
   3. **Einstufung:** „**klarer Favorit: <Team>**“ nur, wenn **alle vier Bausteine (a–d) zum selben Team zeigen** und der
      **Spielort nicht zum anderen Team** zeigt; „**ausgeglichen**“, wenn kein Baustein zu einem Team zeigt; sonst „**nicht
      eindeutig**“. In der Tagesliste stehen die fünf Sätze und die Einstufung, im Chat ein Satz.
   **Wirkung bei „klarer Favorit“** (Anlass: Auswertung 20.–26.11. – in 19 von 21 verfehlten Tipps auf Beide treffen – Ja,
   Über 2,5 und Unter 2,5 blieb ein Team ohne Tor bzw. gewann ein Team deutlich):
   - **Beide treffen – Ja ist nicht erlaubt.**
   - **Über 2,5 nur**, wenn der Favorit in seinen letzten 6 (Bezug nennen) mehrfach **allein** 3 oder mehr Tore schoss (mit
     Spielständen) – der Tipp darf nicht davon abhängen, dass der Außenseiter trifft.
   - Bei **Unter 2,5** ist die feste Gegenangabe (3+ eigene Tore) für den Favoriten immer ausdrücklich zu nennen.
   **Unterklassige Pokalgegner (seit 1.4.1, Wunsch des Nutzers vom 28.11.2026):** Ein Spiel gegen einen Gegner, der laut Quelle
   (SM-Artikel, SM-Spielseite, FS) in einer **tieferen Spielklasse** spielt als das Team, zählt **nicht** für „Favorit schoss
   mehrfach allein 3+ Tore“ und **nicht** für die feste Unter-2,5-Gegenangabe (Schritt 6); es wird genannt mit „unterklassiger
   Gegner – zählt hier nicht“. Steht die Spielklasse des Pokalgegners nicht in der Quelle, gilt die vorsichtige Seite: Es zählt
   **nicht** für die Favoriten-Bedingung (Über 2,5), aber **weiter** für die Unter-2,5-Gegenangabe. Europapokal-Gegner sind nicht
   unterklassig. In den Rang-2-Blöcken bleibt das Spiel stehen (mit dem Hinweis), nur für diese zwei Regeln zählt es nicht.
   Die Einstufung selbst ist kein Rang-Grund; sie schließt Märkte aus und gibt den Vorrang aus Schritt 7.
5. **Spielbild je Team** – drei Fragen: **Trifft es? Kassiert es? Gewinnt es?** Die Zahlen dazu
   kommen aus FootyStats (Rang 2–3), Sports Mole korrigiert mit den Teamnews (Rang 1): fehlt z. B.
   der Torjäger, zählt sein bisheriger Torschnitt weniger; fehlen Innenverteidiger, zählen die Gegentore mehr.
   **Ausfälle geben nur mit belegter Position eine Richtung** (seit 22.11.2026, Wunsch des Nutzers):
   Ein Ausfall darf nur dann als Grund für mehr oder weniger Tore (oder für Sieg/Niederlage) dienen,
   wenn seine Position in der Quelle steht. Steht sie nicht dort, gilt: **„Position nicht in der
   Quelle – keine Richtung“**; der Ausfall wird genannt, aber weder als Grund noch als Gegenangabe
   gewichtet. (Anlass: Hull – Brighton, Osasuna – Málaga, Getafe – Atlético am 22.11.)
   **Nur neue Änderungen sind Rang-1-Gründe** (seit 26.11.2026, Wunsch des Nutzers – Regel 7c): Ein Spieler zählt nur dann
   als Grund oder Gegenangabe aus Rang 1, wenn er (a) im **letzten Pflichtspiel noch spielte** (Startelf oder eingewechselt)
   und jetzt fehlt, gesperrt oder fraglich ist, oder (b) im **letzten Pflichtspiel fehlte** und jetzt **sicher zurück** ist
   (Quelle sagt klar, dass er spielt/startet – nicht „could“, „may“, „in contention“, „must vie“). Geprüft wird das über die
   FS-Aufstellungen des letzten Spiels (beide Wettbewerbe). Alle anderen Ausfälle/Rückkehrer stehen im Datenblatt mit
   „nicht neu – keine Richtung“, weil sie schon in den Zahlen der letzten Spiele stecken. (Anlass: Chaloupek, Ordóñez,
   Neuer/Davies, Bastoni, Pedrinho, Ueda/E. Mbappé am 25.11.)
   Bei einem Widerspruch geht eine **konkrete Nachricht aus Sports Mole** einer Zahl aus FootyStats
   vor (ein gesperrter Kapitän wiegt mehr als ein Saisonwert).
6. **Die sechs Märkte prüfen:** Heimsieg, Auswärtssieg, Beide treffen – Ja, Beide treffen – Nein,
   Über 2,5, Unter 2,5 – je kurz: was spricht dafür, was dagegen (nach Rangfolge gewichtet).
   **Je Markt zuerst Rang 1–2** (Lage, Teamnews, aktuelle Form), **erst danach Rang 3**
   (Saisonwerte); die Gegenangaben-Prüfung aus Schritt 7 gilt schon hier: Ein Markt, gegen den
   Rang 1–2 sprechen, wird nicht durch Saisonwerte zum stärksten (seit 21.11.2026).
   **Unter 2,5 – feste Gegenangabe** (Wunsch des Nutzers vom 24.11.2026): Bei jedem Unter-Markt wird
   ausdrücklich geprüft, ob eines der Teams in seinen letzten 6 Spielen (Bezug nennen) schon mehrfach
   allein 3 oder mehr Tore geschossen hat – mit Spielständen. Trifft das zu, ist es eine Rang-2-Gegenangabe
   mit „dreht den Tipp: ja/nein, weil …“. (Anlass: Auswertung 24.11. – alle 5 Unter-Fehltipps hatten ein
   Team mit 3+ eigenen Toren.) Spiele gegen laut Quelle unterklassige Pokalgegner zählen dabei nicht mit (seit 1.4.1, Schritt 4b).
7. **Tipp:** Claude bestimmt **selbst** den **sichersten der sechs Märkte** (Kriterium siehe unten; seit 1.4 nur unter
   den nach Schritt 4b erlaubten Märkten, und der **Vorrang Sieg-Markt** unten geht vor)
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
   **Vorrang Sieg-Markt** (seit Version 1.4, Wunsch des Nutzers vom 27.11.2026): Zeigen der Lage-Check (Rang 1) und das
   Kräfteverhältnis („klarer Favorit“, Schritt 4b) zum **selben Team** und dreht keine Rang-1–2-Gegenangabe dessen Sieg
   („dreht den Tipp: ja/nein, weil …“), ist **der Sieg dieses Teams der Tipp** – vor jedem Tor-Markt. Dreht eine Gegenangabe den
   Sieg, gilt wieder „sicherster Markt“ unter Beachtung der Ausschlüsse aus Schritt 4b.
   **Wann der Lage-Check zu einem Team zeigt** (festgelegt vom Nutzer am 27.11.2026): Die Lage zeigt zu Team X, wenn die
   Lage-Fakten von X (Serien, keine neue Schwächung) für X sprechen und die des Gegners (Serien, neue Schwächung) gegen den
   Gegner. Die Dringlichkeit der Punkte allein reicht nicht.
8. **Kennzeichnung** (genau festgelegt am 21.11.2026): Die **Sports-Mole-Seite** ist Rang 1 –
   Lage-Check und Teamnews (Artikel, Tabelle); die **FootyStats-Seite** sind die Zahlen aus Rang 2–3
   (Form, Heim/Auswärts, Saisonanteile). „**beide einig**“ – beide Seiten zeigen zum Tipp;
   „**geteilt**“ – eine Seite zeigt woandershin oder nicht eindeutig (welche und warum, in einem
   Satz). Die
   Kennzeichnung ist keine Schwelle, sondern dient der Auswertung.
   **Feste Sätze (seit 1.4.1):** In der Tagesliste steht immer: „**SM-Seite** (Rang 1 – Lage, Teamnews) zeigt: zum Tipp /
   woandershin (wohin) / nicht eindeutig – weil …“ und „**FS-Seite** (Rang 2–3 – Form, Spielort, Saison) zeigt: zum Tipp /
   woandershin (wohin) / nicht eindeutig – weil …“. „beide einig“ nur, wenn **beide Sätze „zum Tipp“** lauten. Gibt Rang 1 für den
   gewählten Markt keine Richtung (keine neue Änderung nach Regel 7c, Lage ohne Bezug zum Markt), lautet der SM-Satz „nicht
   eindeutig“ – das ist „geteilt“. Zeigt ein Rang-2-Block gegen den Tipp, lautet der FS-Satz nicht „zum Tipp“ (Musterfälle:
   `MUSTERFAELLE.md`).
   **Spielen nur bei „beide einig“** (seit Version 1.4, Wunsch des Nutzers vom 27.11.2026): Jede Paarung bekommt weiter genau
   einen Tipp. „beide einig“ → **„Spielen: ja“**; „geteilt“ → **„Spielen: nein – nur Beobachtung“**. Die Auswertung zählt beide
   Gruppen getrennt.

## Regeln für den Tipp

1. **Genau ein Tipp je Paarung**, deutlich als „Tipp“ markiert, mit Gründen, dem, was dagegen
   spricht, und der Kennzeichnung „beide einig“ oder „geteilt“. Der Tipp ist **immer der sicherste
   der sechs Märkte** – der, gegen den am wenigsten spricht (seit 1.4: unter den nach Schritt 4b erlaubten Märkten; Vorrang Sieg-Markt nach Schritt 7 geht vor). Die Kennzeichnung sagt, wie sicher
   er ist (beide einig = sicherer, geteilt = unsicherer); sie entscheidet nicht, ob ein Tipp bestimmt wird (immer genau
   einer), seit Version 1.4 aber, ob er **gespielt** wird (nur „beide einig“, Schritt 8).
2. **Erlaubte Märkte – nur diese sechs:** Heimsieg, Auswärtssieg, Beide treffen – Ja,
   Beide treffen – Nein, Über 2,5 Tore, Unter 2,5 Tore. Keine anderen Wettarten (kein Remis,
   keine Doppelte Chance, keine Ecken, keine anderen Torlinien).
3. Rang 3 dreht eine klare Angabe aus Rang 1–2 nicht um. (Die Ausschlüsse aus Schritt 4b widersprechen dem nicht: „klarer
   Favorit“ setzt voraus, dass auch beide Rang-2-Blöcke zum Favoriten zeigen; die Tabelle allein schließt nichts aus.)
4. Jede Aussage im Spielbild nennt ihre Quelle (Sports Mole: Artikel, Spielseite, Tabelle;
   FootyStats) und steht im Datenblatt (seit 1.3).
5. Kein Rechenmodell, keine Direktvergleiche (H2H), keine Schwellen, keine Punkte. Verboten ist das
   **Zählen von Gründen oder Häkchen als Entscheidungsregel** („7 von 10 Punkten erfüllt“).
   **Erlaubt und im Datenblatt Pflicht** sind Ergebniszählungen aus Formdaten („in 3 der letzten
   5 Ligaspiele ohne Tor“), klargestellt am 21.11.2026.

## Antwortaufbau je Paarung

**In der Tagesliste** genau in der Reihenfolge des Entscheidungswegs (angeglichen am 21.11.2026,
Version 1.3); **im Chat** nur Punkt 7 mit Anstoß und Paarung, dazu seit 1.4 der Satz aus 3b und „Spielen: ja/nein“ (Variante 1, siehe
„Alles im Chat“):

1. Abgleich Sports Mole ↔ FootyStats (Ergebnis von `abgleich.py`, Abweichungen)
2. **Datenblatt je Team** (Tabelle, letzte Spiele, letzter Sieg/Tor, Zahlen mit Bezug, Teamnews
   nach Originalwort)
3. **Lage-Check je Team** (fünf Fragen)
3b. **Kräfteverhältnis** (vier Bausteine und Spielort je mit dem festen Satz „zeigt zu: …“, Einstufung – seit 1.4, feste Sätze
    seit 1.4.1)
4. Spielbild je Team: trifft es? kassiert es? gewinnt es? (mit Quelle, Teamnews eingearbeitet)
5. Spielbild gesamt
6. Die sechs Märkte, je kurz dafür/dagegen
7. ✅ **Tipp** mit Gründen, Gegenangaben (jede aus Rang 1–2 mit „dreht den Tipp: ja/nein, weil …“)
   und „beide einig“ / „geteilt“ (mit den zwei festen Sätzen, seit 1.4.1) sowie „Spielen: ja“ / „Spielen: nein – nur
   Beobachtung“ (seit 1.4)
8. **Merkmale-Zeile** (Punkte 1–12)
Vorlage für den ganzen Abschnitt: `VORLAGE-ABSCHNITT.md` (seit 1.4.1).
(Kein „We say“ – seit Version 1.3 nicht mehr verwendet.)

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/sportsmole/JJJJ-MM-TT.md` (Anstoß, Paarung, Liga,
FootyStats-`match_id`, Tipp, „beide einig“/„geteilt“, seit 1.4 „Spielen ja/nein“) und werden dort nach Abpfiff mit
den Ergebnissen aus FootyStats ausgewertet: Treffer und Trefferquote, Treffer je Wettart,
**Treffer „beide einig“ gegenüber „geteilt“**; keine Einheiten, keine Quoten, kein „We say“
(ältere Listen behalten ihre We-say-Spalte als Verlauf, sie wird ab dem 21.11.2026 nicht mehr
ausgewertet). Tipps möglichst vor Anpfiff; Tipps
nach Anpfiff werden vermerkt.

**Merkmale je Tipp** (Wunsch des Nutzers vom 25.11.2026): Zu jedem Tipp steht in der Tagesliste nach Schritt 8 eine
feste Zeile „Merkmale“ – nur zur späteren Auswertung, sie **beeinflusst die Tippwahl nicht** (keine Punkte, keine
Schwellen):
1. Wettart (Heimsieg, Auswärtssieg, Beide treffen – Ja/Nein, Über/Unter 2,5).
2. Kennzeichnung: beide einig / geteilt; ob sie vor Anpfiff geändert wurde.
3. Grenzfall: ja / nein.
4. Tipp vor Anpfiff geändert: ja (ursprünglicher Tipp nennen) / nein.
5. Neue Rang-1-Gegenangabe gegen den Tipp (Spieler, der im letzten Spiel noch spielte und jetzt fehlt/fraglich ist,
   oder neue Lage): ja (wer) / nein.
6. Rang-2-Blöcke einig: zeigen alle Blöcke (letzte 6 alle Wb., letzte 6 Liga; im Europapokal zusätzlich alle CL-Spiele
   und letzte 6 Heimliga) zum Tipp – ja / nein (welcher nicht).
7. Gegensätzliche Profile (ein Team fast immer über, das andere fast immer unter 2,5 bzw. beide treffen): ja / nein.
8. Datenlage vollständig: ja / nein (z. B. Heimliga nicht in FS, ungeklärte Abweichung SM ↔ FS).
9. Zweitbester Markt: der Markt, gegen den nach dem Tipp am wenigsten spricht (ergänzt am 26.11.2026 auf Wunsch
   des Nutzers) – bei der Auswertung wird mitgezählt, ob er getroffen hätte; so lässt sich ohne Rückschau prüfen, ob ein
   Vorrang für Sieg / Beide treffen – Nein bei fast gleich starken Märkten mehr Treffer gebracht hätte.
10. Kräfteverhältnis: klarer Favorit (Team) / ausgeglichen / nicht eindeutig (seit 1.4); dazu seit 1.4.1 „Tabellenhöher: Heim /
    Gast“ (aus dem Werkzeug) – Vergleichswert für die Auswertung („der Tabellenhöhere gewinnt“).
11. Spielen: ja / nein (seit 1.4).
12. **Schattentipp** (seit 1.4.1): der Markt, der **ohne** die Ausschlüsse aus Schritt 4b und **ohne** den Vorrang Sieg-Markt der
    sicherste der sechs gewesen wäre – dazu „gleich“ oder „anders wegen 4b-Ausschluss“ bzw. „anders wegen Vorrang Sieg-Markt“. So
    lassen sich die Regeln von 1.4 an denselben Spielen mit dem Stand davor vergleichen und voneinander trennen.
13. **Vorprüfung** (seit 28.11.2026): „ja – Zahlen zeigten zu: Heimsieg / Auswärtssieg / <Tor-Markt> / keinem“, wenn der Nutzer das
    Spiel nach einer Vorprüfung gewählt hat; sonst „nein“. **Dieses Merkmal trägt Claude ein, nicht der Bearbeiter** – erst wenn die
    Tipps fertig und geprüft sind (Abschnitt „Vorprüfung“).
14. **Zweitquelle Teamnews** (Probelauf seit 28.11.2026): „bestätigt“ / „weicht ab (wer, was) – Rang 1 betroffen: ja/nein“ / „nicht
    verfügbar“. **Auch dieses Merkmal trägt Claude ein**, nach der Kontrolle (Abschnitt „Zweitquelle Teamnews – Probelauf“).
Schreibweise (fest, damit `werkzeuge/tippanalyse.py` sie liest): „(10) Kräfteverhältnis: … ; Tabellenhöher: Heim · (11) Spielen: ja ·
(12) Schattentipp: Über 2,5 – anders wegen Vorrang Sieg-Markt · (13) Vorprüfung: ja – Zahlen zeigten zu: Heimsieg ·
(14) Zweitquelle: weicht ab (Mwene nur in LigaInsider, angeschlagen seit gestern) – Rang 1 betroffen: nein“; die Märkte immer mit ihren festen Namen (Heimsieg, Auswärtssieg,
Beide treffen – Ja, Beide treffen – Nein, Über 2,5, Unter 2,5).
Bei der Auswertung wird je Merkmal mitgezählt (Treffer mit/ohne Merkmal; seit 1.4 immer getrennt nach „Spielen: ja“ und „nein“); bei geänderten Tipps auch, ob der
ursprüngliche Tipp getroffen hätte; immer auch, ob der zweitbeste Markt und der Schattentipp getroffen hätten. **Ausgewertet und dem
Nutzer berichtet wird, sobald 50 gespielte Tipps („Spielen: ja“) seit 1.4 ein Ergebnis haben** (seit 1.4.1; vorher „nach etwa 50
Tipps“ – das wären zu wenige gespielte gewesen); `werkzeuge/tippanalyse.py` zeigt den Zählerstand. Ob ein
Merkmal zum Aussortieren oder Kennzeichnen verwendet wird, entscheidet nur der Nutzer.

## Änderungen am System (seit 1.4.1, Wunsch des Nutzers vom 28.11.2026)

- **Eine Änderung nach der anderen:** Claude schlägt neue Tippregeln einzeln vor, damit sich ihre Wirkung trennen lässt.
- **Nicht aus zu wenigen Fällen:** Claude empfiehlt eine neue Tippregel erst, wenn etwa 50 Fälle dafür vorliegen, und sagt bei
  jeder Zahl dazu, wie viele Fälle dahinterstehen.
- **Messbar von Anfang an:** Jede neue Regel bekommt, wo es geht, eine Merkmale-Zeile, mit der sich an denselben Spielen
  vergleichen lässt, was mit und ohne die Regel getippt worden wäre (wie der Schattentipp).
- Über jede Änderung entscheidet allein der Nutzer; Reparaturen an Werkzeugen (Zählfehler, Abruffehler) werden sofort gemeldet,
  ins Fehlerprotokoll eingetragen und behoben.
