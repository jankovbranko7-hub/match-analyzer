# Fehlerprotokoll · Sports-Mole-Check

Eingerichtet am 21.11.2026 auf Wunsch des Nutzers: **aus jedem Fehler lernen.** Hier steht jeder
gefundene Fehler mit Datum, Spiel, Fehlerart und Gegenmaßnahme.

**So wird es verwendet (Pflicht, Teil von Version 1.3):**
1. **Vor jeder Analyse** liest Claude dieses Protokoll und prüft beim Schreiben jede Fehlerart
   gezielt mit.
2. Der **Kontrolldurchgang** (Stufe 1), die **„Kontrolle“** (Stufe 2) und die **unabhängige
   Kontrolle** (Stufe 3) gehen jede Fehlerart einzeln durch; der unabhängige Prüfer bekommt
   dieses Protokoll mit.
3. **Jeder neu gefundene Fehler** – egal von wem gefunden (Claude, Prüfer, Nutzer) – wird sofort
   hier eingetragen: Datum, Spiel, was falsch war, Fehlerart, ob ein Tipp betroffen war.
4. Passt ein Fehler zu **keiner** Fehlerart, wird eine neue angelegt und dem Nutzer eine
   Gegenmaßnahme vorgeschlagen (Regeländerung nur auf seinen ausdrücklichen Wunsch).
5. Häuft sich eine Fehlerart trotz Gegenmaßnahme, sagt Claude das dem Nutzer offen.

---

## Fehlerarten mit Gegenmaßnahme (Stand 21.11.2026)

Häufigkeit = Zahl der gefundenen Fälle am 20. und 21.11.2026.

**A · Liga und alle Wettbewerbe verwechselt** – häufigste Fehlerart (über 20 Fälle)
- Typisch: FootyStats-Trends („seit X Spielen …“) zählen nur die Liga; „letzte 6“ ohne Angabe;
  Heimserie, die einen Pokal- oder Europapokalspiel übersieht.
- Gegenmaßnahme: Prüfliste 6a; Datenblatt „jede Zahl mit Bezug“ (1.3); `sm_spiel.py` beschriftet
  jedes Formspiel mit Wettbewerb (1.3).
- Wichtig: Der Kontrolldurchgang (Stufe 1) hat diese Fehler am 20.11. nicht erkannt – jede Serie
  muss aus den Ergebnislisten **nachgezählt** werden, nicht aus dem Trendsatz übernommen.

**B · Gegenangaben unvollständig** (über 15 Fälle, 1 Tipp geändert)
- Typisch: fehlende oder fragliche **Angreifer** beim Team, das für den Tipp treffen soll, nicht
  genannt; Form-Gegenangaben aus Rang 2 vergessen.
- Gegenmaßnahme: Prüfliste 9 („alle Rang-1–2-Gegenangaben“); Datenblatt-Teamnews in vier Listen
  (1.3) – vor dem Tipp jede Liste gegen den Tipp lesen.

**C · Sicherster Markt falsch abgewogen** (10 Fälle + 2 Grenzfälle: 5 vor Anpfiff gefunden und Tipp geändert, 5 erst nach der Auswertung gefunden – alle 5 Fehltipps)
- Typisch: Tipp ruhte auf Saisonwerten (Rang 3), obwohl Form oder Lage (Rang 1–2) dagegen
  sprachen; Spielbild je Team passte nicht zum Tipp.
- Gegenmaßnahme: Regel „Rang 3 dreht Rang 1–2 nicht um“; bei jedem Markt den Rang des Grundes
  nennen; Spielbild je Team vor dem Tipp gegen den Tipp lesen. **Seit 21.11. (nach der Auswertung):
  Gegenangaben-Prüfung „dreht den Tipp: ja/nein, weil …“ bei jeder Rang-1–2-Gegenangabe; neue
  Gegenangabe aus einer Kontrolle → Tipp immer neu abwägen.**

**D · „We say“ als Tatsache verwendet** (3 Fälle)
- Gegenmaßnahme: „We say“ seit 1.3 komplett gestrichen; `sm_spiel.py` gibt den Absatz nicht mehr aus.

**E · Vermutung ohne Quelle** (über 10 Fälle)
- Typisch: „Europapokal-Belastung“ ohne Spiel unter der Woche; „Derby“ als Grund; „Torproblem“,
  „formstärkstes Team“, „neuer Trainer stellt um“ ohne Beleg.
- Gegenmaßnahme: Datenblatt nur mit Fakten und Quelle (1.3); Belastung nur mit Datum des Spiels.

**F · Status der Teamnews falsch gelesen** (3 Fälle)
- Typisch: „may play“ als sicher, „doubt“ als „fehlt“, „möglicherweise in der Startelf“ als sicher.
- Gegenmaßnahme: Teamnews nach dem Originalwort (1.3), bei Unklarheit „unklar (Wortlaut: …)“.

**G · Fehler der Quelle übernommen / Abgleich übersehen** (4 Fälle)
- Typisch: Sports-Mole-Artikel nennt falsche Ergebnisse oder falschen Platz; Abweichung SM ↔ FS
  nicht bemerkt.
- Gegenmaßnahme: `abgleich.py` (1.3) meldet jede Abweichung automatisch; Spielseite und Tabelle
  gehen dem Artikeltext vor.

**H · Zahl falsch gelesen oder gezählt** (über 10 Fälle)
- Typisch: „alle“ statt „5 von 6“; Spiel in einer Serie übersehen; Bilanz 3-1 statt 3-0-1;
  Abstand falsch; Suchfilter verfehlt Spieler.
- Gegenmaßnahme: Datenblatt, jede Angabe einmal gegen den Wortlaut gelesen (Prüfliste 6b);
  Abstände aus `abgleich.py`.

**I · Anteil falsch beschrieben – Team oder Spiel** (1 Fall)
- Typisch: „beide treffen am Spielort zu 80 %“, gemeint war „das Team trifft zu 80 %“.
- Gegenmaßnahme: Datenblatt Bezug „Team oder Spiel“ (1.3).

**J · Lage-Check unvollständig** (über 10 Fälle)
- Typisch: Abstand nur in eine Richtung; „worum es geht“ fehlt; „ohne Druck“ trotz 3 Punkten
  über dem Abstiegsplatz; Spielzahl des neuen Trainers nicht angegeben.
- Gegenmaßnahme: Abstände nach oben, unten und zum Abstiegs-/Relegationsplatz aus `abgleich.py`;
  fehlt eine Angabe in der Quelle, steht „nicht in der Quelle“.

**K · Entscheidungsweg nicht in der Reihenfolge** (3 Listen)
- Typisch: Lage-Check vor FootyStats/Abgleich; Spielbild nicht je Team.
- Gegenmaßnahme: Antwortaufbau = Entscheidungsweg; Stufe 3 prüft die Reihenfolge.

**L · Direktvergleich (H2H) verwendet** (3 Fälle am 20.11., vor dem Verbot)
- Gegenmaßnahme: H2H verboten (20.11.); H2H-Sätze im Artikeltext nie übernehmen (Prüfliste 10).

**M · Eigene Werkzeug- und Formfehler** (6 Fälle)
- Typisch: Zusammenfassung las „Real“ als Real Madrid statt Real Betis; Werkzeug nahm den falschen
  Spielseiten-Link; Uhrzeit in der Liste geschätzt statt abgelesen.
- Gegenmaßnahme: volle Teamnamen; Uhrzeit immer mit `date` ablesen; Werkzeuge nach jeder Änderung
  an einem echten Spiel testen.

---

## Einzelne Fehler (chronologisch)

Abkürzungen: SK = Kontrolldurchgang Stufe 1 · UK = unabhängige Kontrolle · N = vom Nutzer gefunden.
„Tipp!“ = Tipp wurde deshalb vor Anpfiff geändert.

### 20.11.2026 (Version 1.0/1.1)
- Troyes – Le Havre: „kein Spieler unter den besten 30 Torschützen“ falsch (Suchfilter) – H – SK
- Bayern: „übernimmt die Spitze“ – war schon Erster – H – UK
- Bayern: Kölns torarme Ligaspiele unvollständig (1:2 gegen Leverkusen fehlte) – H – UK
- Bayern: Kane „may play“ als sicher – F – UK
- Barnsley: Über 2,5 „alle“ statt 5 von 6 – H – UK
- Bilbao: Serie ohne das 1:1 gezählt – H – UK
- Bilbao: Sestao Viertligist, nicht Drittligist; Sancet nur möglicherweise in der Startelf – H/F – UK
- Bayern: „letzte 7 alle 3+ Tore“ – FS-Trend zählte nur die Liga – A – SK
- Bilbao: „trifft seit 4 Spielen“ = Liga – A – SK
- Bayern: „seit 9 ungeschlagen“ = Liga; Köln „auswärts sieglos“ = Liga – A – UK
- Barnsley/Wednesday: Serien = Liga – A – UK
- Troyes: „Le Havre kassiert immer“ zu weit – H – UK
- Bilbao: Gegenangaben zu „Beide treffen – Ja“ fehlten – B/C – UK – **Tipp!** (→ Unter 2,5 ✅)
- Uhrzeit der Tipps falsch angegeben (17:50 statt 17:38) – M – selbst
- Direktvergleiche als Grund/Gegenangabe (Bayern, Bilbao, Barnsley) – L – N (danach verboten)

### 21.11.2026 · Premier League / La Liga (Version 1.2)
- Betis „3 ungeschlagen“ = Liga – A – SK
- Forest: letzte Auswärtsspiele aus dem SM-Artikel falsch – G – UK
- Bournemouth: „Forests Auswärtsschwäche“ von FS nicht getragen; „formstärkstes Team“ – E – UK
- Villa: „2:0-Führung“ nicht belegt – E – UK; Gegentor-Serie = alle Wb. – A – UK
- Chelsea: „17 % über 2,5“ = alle Wb. – A – UK
- Coventry: „Nullnummern zu Saisonbeginn“, „trifft daheim sicher“ falsch – H/E – UK – **Tipp!**
- Rayo: „beide treffen am Spielort zu 80 %“ – I – UK; „Kapitän Gayà“ nicht belegt – E – UK – **Tipp!**
- Sevilla: „Torproblem“ nicht belegt – E – UK
- Newcastle: „3 sieglos“ = alle Wb. – A – UK
- Celta/Real: letzter Sieg/Tor fehlten; Platz laut Artikel 11., Tabelle 12. – J/G – UK
- Zusammenfassung las „Real“ als Real Madrid statt Betis – M – selbst
- Reihenfolge Entscheidungsweg falsch, Spielbild nicht je Team – K – N
- Coventry: „Beide treffen – Nein“ ruhte auf Rang 3 – C – UK2 – **Tipp!** (→ Sieg Coventry)
- Rayo: Heimsieg ruhte auf Rang 3, „Valencia gewinnt kaum“ widersprach den Zahlen – C – UK2 – **Tipp!** (→ Über 2,5)
- Sevilla: „Derby“ als Grund, „Betis ohne Cucho“ (nur fraglich) – E/F – UK2 – **Tipp!** (→ Beide treffen – Ja)
- Spurs: fehlende/fragliche Spurs-Angreifer nicht als Gegenangabe – B – UK2
- **Grenzfall nach der Auswertung (ca. 23:10):** Spurs – Ipswich (2:0): „Beide treffen – Ja“ ruhte vor
  allem auf Ipswichs Saisonwerten auswärts (Rang 3); die Rang-1-Gegenangabe (Spurs-Angreifer) wurde
  nicht auf „dreht den Tipp“ geprüft – C (Grenzfall).
- Bournemouth „kassiert selten“ = alle Wb. (Liga 7 in 6) – A – UK2
- Newcastle „erste 4 Heimspiele 2+ Tore“ = alle Wb.; Märkte ohne Grund – A/C – UK2
- Celta „ohne Druck“ trotz 3 Punkten über Platz 18 – J – UK2

- **Nach der Auswertung gefunden (ca. 22:20, N):** Villa – Sunderland (0:0): „Beide treffen – Ja“
  ruhte auf Saisonwerten am Spielort (Rang 3: „beide am Spielort nie zu null“); dagegen standen
  Rang 1–2 – Sunderland in 3 der letzten 5 Ligaspiele ohne Tor, 2 der letzten 3 zu null, ohne
  Brobbey und Xhaka – nur als Gegenangabe, ohne den Tipp umzudrehen – C – von UK1 und UK2 nicht
  erkannt.

### 21.11.2026 · Serie A / Bundesliga (Version 1.2)
- Stuttgart „2 der letzten 3 zu null“ = Liga und Pokal – A – SK
- Paderborn Abstand falsch; Elversberg „3-1“ statt 3-0-1; Datum Como-Sieg nicht belegt – H/E – SK
- Union „letzte 6 alle Wb.“ falsch übernommen (SM ≠ FS) – G – UK
- Gegenangaben fehlten: Leverkusen, Napoli, Dortmund, Frankfurt/Hoffenheim – B – UK
- **Nach der Auswertung gefunden (ca. 22:20, N):** Frankfurt – Hoffenheim (1:0) und Elversberg –
  Freiburg (0:1): „Beide treffen – Ja“ ruhte auf Spielort-Saisonwerten (Rang 3: 75 %, „Liga daheim
  immer“); Rang 2 dagegen (Frankfurt 2 der letzten 5 Ligaspiele ohne Tor, letzte 6 nur 50 % beide
  treffen; Elversberg 3 der letzten 6 ohne Tor, Freiburg zweimal zu null) stand nur im „Dagegen“ –
  C – von UK1 und UK2 nicht erkannt.
- Abstände fehlten: Como, Cagliari, Napoli, Torino; Parma Trainer-Spielzahl – J – UK
- Liga/alle Wb. fehlte: Cagliari, Lazio, Lecce, Leverkusen, Elversberg – A – UK
- H2H-Beispiele in der Prüfliste – L – UK
- Reihenfolge Entscheidungsweg – K – N
- Lazio Fan-Boykott nur aus „We say“ – D – UK2
- „Europapokal-Belastung“ ohne Spiel unter der Woche – E – UK2
- Gegenangaben: Dortmund, Elversberg (Pokal 0:2), Parma (3:0 in Bergamo) – B – UK2
- Spielbild je Team ungenau (Paderborn, Leipzig, Dortmund) – C – UK2
- Schalke „5 Spiele ohne Tor“ statt 4 (alle Wb.) / 3 (Liga) – H/A – UK2

- **Grenzfall nach der Auswertung (ca. 23:10):** Napoli – Torino (1:0): „Beide treffen – Ja“; Rang 2
  dagegen (Napoli 2 der letzten 5 Ligaspiele ohne Tor, Torino traf in Frosinone nicht) – C (Grenzfall).

### 21.11.2026 · Regeln und Werkzeuge (selbst gefunden)
- Werkzeug-Beschreibung (`werkzeuge/README.md`) nannte bei `fs_spiel.py` noch „Vorab-xG“ aus einer
  alten Version (das Werkzeug gab den Wert nicht aus) – M – beim Systemtest korrigiert.
- Regel-PDF 1.3: mehrere Aufzählungen erschienen als Fließtext (fehlende Leerzeile vor Listen) – M –
  vor dem Versand korrigiert.
- Lücke in der Regel zur Stufe 3: Ein Tipp wurde nach einer Kontrolle nur neu bestimmt, wenn ein
  Tipp-Grund falsch war – neu gefundene Rang-1–2-Gegenangaben lösten keine Neuabwägung aus (Ursache
  der C-Fehler bei Villa, Frankfurt, Elversberg, Lens, Strasbourg) – C – nach der Auswertung (N),
  Regel am 21.11. geändert.

### 21.11.2026 · Ligue 1 (Version 1.2)
- **Nach der Auswertung gefunden (ca. 23:10, selbst):** Lens – Toulouse (1:1): „Über 2,5“ ruhte auf
  Saisonanteilen (Rang 3: 80 %); Rang 1–2 dagegen (Toulouse 2 der letzten 5 Ligaspiele ohne Tor,
  Messali fehlt, Jørgensen fraglich; bei Lens fehlen Édouard und Sima) nur im „Dagegen“ – C.
- **Nach der Auswertung gefunden (ca. 23:10, selbst):** Strasbourg – Brest (0:1): „Beide treffen –
  Ja“ auf Saisonwerten (Rang 3); Rang 2 dagegen (Brest letzte 2 Ligaspiele zu null, Strasbourg 0:3
  in Rennes, Reyna und Balde fraglich) nur im „Dagegen“ – C.
- Nice „Ausfälle vor allem Abwehr“ nur aus „We say“ – D – SK
- PSG „Champions-League-Belastung“ nicht belegt – E – UK
- Strasbourg „zwei Tage Training“ nur aus „We say“ – D – UK
- Lens „gut zwei Monate“ statt „kaum zwei“; Toulouse „2 Spiele ohne Tor“ = 2 der letzten 5 – H – UK
- Vermutung „neuer Trainer stellt die Abwehr um“ – E – UK
- Liga/alle Wb. fehlte: Lille, Monaco, Strasbourg, Tengstedt – A – UK
- Gegenangaben fehlten: PSG-Angreifer, Toulouse/Lens vorn, Lyon/Lille, Namaso, Golovin, Reyna,
  Balde, Strasbourgs 0:3 – B – UK
- Reihenfolge Entscheidungsweg – K – N
- Spielbild je Team ohne Quelle/Teamnews; Abstände fehlten; Lyon „EL-Belastung“ – K/J/E – UK2

### 22.11.2026 (Version 1.3, erste Anwendung)
- Uhrzeiten der Abrufe geschätzt statt mit `date` abgelesen („11:50“, „12:05“ – tatsächlich ca. 11:35,
  11:37) – M – UK.
- Burnley/Blackburn: nächstes Spiel (25.11.) als „nicht in der Quelle“ geführt, steht im FS-Spielplan;
  Abstände zu den Nachbarn fehlten – J – UK.
- Burnley/Blackburn: „Lancashire-Derby“/„Derby“ – Quelle sagt nur „fierce rivals“; Roberts' Position
  angenommen – E – UK.
- Burnley/Blackburn: Markt Über 2,5 falsch gelesen („2:2/1:2“ als Gegenangabe für Unter); Märkte ohne
  „dafür“/Rang 3 – H/C – UK.
- Burnley/Blackburn: „if … overcome injuries … bench at best“ als „fraglich“ statt „unklar“ – F – UK.
- Barcelona: „ohne Sieg wäre Platz 1 weg“ falsch (Remis hält Platz 1) – Tipp-Grund – H/E – UK; Tipp
  neu abgewogen, bleibt.
- Barcelona/Villarreal: Vorschau heute aktualisiert, nicht vermerkt – H/G – UK.
- Villarreal: „Torprobleme“ ohne „Liga“ (alle Wb. Tor in 4 der letzten 6) – A – UK.
- Villarreal: Gegenangabe mit einem Spiel außerhalb der letzten 6 begründet, 3:4 Liverpool fehlte – H/B – UK.
- Barcelona/Villarreal: „Ausfälle vorn“, „Stürmer Moreno“, „Innenverteidiger Koundé/Cubarsí“ nicht
  belegt – F/E – UK.
- Barcelona: Gegenangabe „19 Tore, 4 Siege“ falsch gezählt (richtig 16 Tore, 3 Siege) – H – SK.
- Hull/Brighton: zwei Begründungen mit Vermutung („vor den Ausfällen“, „Gegner mit schwächerer
  Abwehr“) – E – SK.
- Hull/Brighton: Brightons 3+-Tore-Spiele falsch gezählt (3 statt 5); Gegenangabe „über 2,5 bräuchte
  zwei Brighton-Gegentore“ falsch (ein 1:2 reicht; 0:2 in Liverpool übersehen) – H/C – UK – **Tipp!**
  (Unter 2,5 → Beide treffen – Nein, Kennzeichnung geteilt).
- Hull/Brighton: „vier Offensivspieler fehlen“ nicht belegt (Positionen nicht in der Quelle, wichtigste
  Torbeteiligte verfügbar); Positionen von Rückkehrern und Hughes angenommen – E – UK.
- Hull/Brighton: Bezug Liga/alle Wb. fehlte; Abstände, Trainer, nächstes Spiel fehlten; Märkte ohne
  „dafür“ – A/J/C – UK.
- Racing/Real Sociedad: „trifft immer“/„kassiert immer“ ohne Bezug Liga/alle Wb. – A – UK.
- Racing: Form mit „letzten 5“ statt der letzten 6 Ligaspiele gezählt (0:5 Celta fehlte) – H/B – UK.
- Racing: „mindestens 3 Tore“ ohne Kennzeichnung Spiel/Rang 3 – I – UK.
- Man United: „Tor in 8 von 10 Ligaspielen“ (richtig 6 von 10) – H – SK.
- Liverpool/United: Zahlen der letzten 6 ohne Bezug Liga/alle Wb.; die Liga sah anders aus (Liverpool
  beide treffen 2 von 6, United über 2,5 2 von 6) – A/B – UK – **Tipp!** (Beide treffen – Ja → Unter
  2,5, geteilt).
- Liverpool/United: Remis-Serie und Trainer-Debüt-Fakt fehlten beim Heimsieg; Abstand zu Platz 20;
  „Startelf“ statt „mögliche Startelf“; Bradley/Leoni als Grund überbewertet – B/J/F/E – UK.
- Osasuna/Málaga: Osasuna letzte 6 Liga beide treffen 4 statt 3 von 6 gezählt; Rang-3-Wert als Rang 2;
  Ausfälle ohne Position und „Kellerduell“ als Grund für wenige Tore; Rang-2-Gegenangabe nur mit Rang 3
  widerlegt – H/C/E – UK – **Tipp!** (Unter 2,5 → Beide treffen – Ja, geteilt).
- Getafe/Atlético: Ausfälle und Champions League als Grund für wenige Tore (laut FS Abwehrspieler –
  sprechen eher für Tore); Gegenangabe mit einem selbst über 2,5 liegenden Spiel widerlegt; Bezug alle
  Wb./Liga fehlte; „gemeinsam schwächster Angriff“ veraltet; Status „spielt“ zu stark – E/H/C/A/G/F – UK.
- **Muster am 22.11.:** Ausfälle ohne belegte Position wurden mehrfach als Grund für „wenige Tore“
  genommen (Hull/Brighton, Osasuna/Málaga, Getafe/Atlético) – E. Gegenmaßnahme: Ausfälle nur mit
  Position aus der Quelle als Richtung verwenden; sonst „Position nicht in der Quelle – keine Richtung“.

---

## Lehren bisher

- **Wichtigste Lehre aus der Auswertung 21.11.:** Eine Rang-1–2-Angabe ins „Dagegen“ zu schreiben
  reicht nicht – es muss geprüft werden, ob sie den Tipp **umdreht**. Bei 5 von 10 Fehltipps des
  21.11. stand der richtige Hinweis schon im „Dagegen“ (Villa, Frankfurt, Elversberg, Lens,
  Strasbourg – alle Tormärkte auf Saisonwerten), dazu 2 Grenzfälle (Spurs, Napoli). Die Kontrollen haben Gegenangaben ergänzt, aber die Abwägung nicht neu
  geprüft. (Rückschaufehler beachten: das Ergebnis war bekannt, als es auffiel – der Fehler liegt in
  der Regelanwendung „Rang 3 dreht Rang 1–2 nicht um“, nicht im Ergebnis.)

- Die meisten Fehler fand erst die **unabhängige Kontrolle**, oft erst die **zweite** – eine
  Kontrolle allein reicht nicht immer.
- Am häufigsten: **A (Liga/alle Wb.)**, **B (Gegenangaben)**, **E (Vermutungen)** – darauf beim
  Schreiben zuerst achten.
- **Alle Tippänderungen** kamen aus **B, C, E, F**: Gegenangaben und Abwägung sind die Stellen, an
  denen Fehler den Tipp kosten.
