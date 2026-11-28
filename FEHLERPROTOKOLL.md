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

**N · Ablauf nicht nach System / Abweichung ohne ausdrückliches Ja** (seit 26.11.2026)
- Typisch: parallele Bearbeiter und mehrere Prüfer ohne Auftrag; mehrdeutige Antwort des Nutzers als Erlaubnis gedeutet;
  Nutzungslimit nicht bedacht – kein Tipp vor Anpfiff.
- Gegenmaßnahme: „Oberste Priorität“ ganz oben im System (immer nach System, 5er-Schritte, genau ein Prüfer, Variante B);
  bei Mehrdeutigkeit nachfragen.

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
  genommen (Hull/Brighton, Osasuna/Málaga, Getafe/Atlético) – E. Gegenmaßnahme (vom Nutzer am 22.11. ins
  System übernommen, Schritt 3 Feld 5, Schritt 5, Prüfliste 7b): Ausfälle nur mit Position aus der
  Quelle als Richtung verwenden; sonst „Position nicht in der Quelle – keine Richtung“.
- Osasuna/Málaga (zweite Kontrolle): „je ein Spiel“ falsch gezählt (0:2 Sevilla fehlte); „Positionen nicht
  in der Quelle“, obwohl die FS-Spielerdaten sie nennen; Status „spielt“ zu stark; Niño SM 4 / FS 5
  nicht vermerkt – H/B/F/G – UK2. Lehre: Bei Regel 7b immer auch `fs.sh league-players` abrufen.
- Zweite Kontrolle 22.11. (Gruppen 1, 3, 4): Positionen als „nicht in der Quelle“ geführt, obwohl FS-
  Spielerdaten sie nennen (Roberts, Jørgensen, Morishita, Mantilla, Andrés Martín, Barrenetxea, Yohanna,
  Targett, Morita); Korrekturen der ersten Kontrolle nur teilweise umgesetzt (Racing „letzte 5“,
  Hughes); SM-Artikelaussage „schlechteste Abwehr“ durch Tabelle überholt; Vorschau-Aktualisierung nicht
  vermerkt; fehlende Gegenangabe McBurnie – B/H/E/G/A/J – UK2. Lehre: Korrekturen immer im ganzen
  Abschnitt suchen und ersetzen, nicht nur an einer Stelle.
- Getafe/Atlético (zweite Kontrolle): Formleiste falsch gelesen – „letzte 5 Spiele alle unter 2,5“, das letzte
  (1:2 Barcelona) lag darüber; der Fehler entstand bei der Selbstkorrektur „letzte 4 → letzte 5“ und
  wurde von der ersten Kontrolle nicht erkannt – H/C – UK2 (Tipp neu abgewogen, bleibt).
- Barcelona/Villarreal und Liverpool/United (zweite Kontrolle): Positionen aus FS nicht genutzt,
  Champions-League-Termine 25.11. als „nicht in der Quelle“, Villarreal „letzte 5“ statt 6 – E/J/H – UK2.
- **Zeit:** Die zweite Kontrolle aller 7 Spiele dauerte bis ca. 17:20; die Berichte zu Gruppe 1–4 kamen
  nach Anpfiff (Tipps blieben laut Regel). Lehre: zusätzliche Runden früh starten.
- Marseille/Le Mans: Gegenangabe mit falscher Annahme widerlegt („spielte schon ohne Palmieri“ – laut FS 9
  von 10 Spielen dabei); „Tor in den letzten 8“ statt 6; EL-Termin übersehen; „formstärkstes Team“ –
  E/H/J/C – UK. Lehre: SM-„still without“ heißt nicht „fehlte schon in den letzten Spielen“ – Einsätze in
  FS-Spielerdaten prüfen.
- Atalanta/Inter: Europapokal-Termine als „nicht in der Quelle“ (FS hat sie); Rückkehrer ohne Startelf als
  Grund; Vermutung „fehlten in Monza noch nicht“; Märkte ohne „dafür“ – J/E/F/C – UK. Lehre: Europapokal-
  Spielpläne (FS-Saisons 17127, 17128, 17130) immer mit abrufen.
- Chicago/Charlotte: falsche SM-Artikelaussage („2 Heimniederlagen in Folge“) übernommen statt Spielseite;
  fragliche Abwehrspieler außerhalb der möglichen Startelf als Grund – G/H/E/F – UK.

### 23.11.2026
- Başakşehir/Çorum: fragliche Spieler als neue Schwächung gewertet, obwohl sie laut FS schon in den letzten
  Spielen fehlten – E/F – UK. Lehre (erneut): bei jedem Ausfall den letzten Einsatz in FS prüfen.
- Başakşehir/Çorum: Ränge falsch zugeordnet, Märkte zusammengelegt ohne „dafür“, Abstand nach unten fehlte –
  C/H/J – UK.
- Monza/Fiorentina: SM-Artikelaussage („only Sassuolo conceded more“) durch den Spieltag überholt und als
  Tipp-Grund verwendet; Njies Torbeteiligungen fehlten in der Gegenangabe – G/H/B – UK. Lehre (erneut):
  Tabellenaussagen des Artikels immer gegen die aktuelle Tabelle prüfen.
- Brentford/Everton: Igor Thiago als „Torjäger“ aus dem Artikel („star striker“) übernommen, obwohl laut
  SM-Spielseite und FS Schade bester Torschütze ist (Thiago 2 Ligatore) – Tipp-Grund falsch – G/H/E – UK.
  Gegenangabe nur mit Rang 3 widerlegt, „Heimsiege zu null“ als Rang 1–2 gewertet, Daten aller Wb. fehlten,
  Märkte zusammengelegt, Lage-Abstände – C/B/A/K/J – UK. **Tipp geändert** (Beide treffen – Nein → Unter 2,5;
  beide einig → geteilt).
- Levante/Elche: „auswärts zuletzt 2-mal zu null“ als Grund für Unter 2,5 (das 3:0 war über 2,5) – H/C; Elches 2
  torlose Spiele ohne Bezug „daheim“ als Grund und zur Widerlegung einer Auswärts-Gegenangabe benutzt – A/C/B;
  Kennzeichnung mit Saisonwert/Form auf der SM-Seite begründet – C/K; Boayar/Yago „fehlt“ statt „unklar“ – F –
  UK. Tipp neu abgewogen, bleibt.
- St. Louis/LAFC: Navarro (19 Tore) aus der SM-Torschützenliste als St.-Louis-Torjäger übernommen – laut FS
  spielt er bei Colorado, die SM-Spielseite nennt Becher; der Abgleich prüft Torschützen nicht – G/H – UK, Tipp-
  Grund. Long ohne Position, obwohl FS „Defender“ – 7b – H/B; Gegentor-Zahl falsch (5 statt 4 von 6) – H;
  Ausfälle Shaffelburg/Tillman nicht gegen den letzten Einsatz geprüft – E/F (Lehre vom selben Tag nicht
  angewandt!) – UK. Tipp ohne Navarro neu abgewogen, bleibt.
- **Muster 23.11.:** In 3 von 5 Paarungen stammte ein falscher Tipp-Grund aus einer Spieler-/Tabellenangabe des
  SM-Artikels oder der SM-Torschützenliste, die nicht gegen SM-Spielseite und FS-Spielerdaten geprüft wurde.
  Lehre: **jeden Spieler, der als Grund dient (Torjäger, Ausfall), mit Team, Position, Toren und letztem Einsatz
  in den FS-Spielerdaten belegen**, bevor er in den Tipp geht.

### 24.11.2026 · Champions League
- Galatasaray/Villa: Widerlegung „ohne Osimhen und Leão 4:3 und 2:1“ falsch – Leão spielte beim 4:3 noch
  (FS letzter Einsatz 07.11.) – H/E – UK. Osimhen „unklar“ in Schritt 6/7 zu „fehlt“ verschärft – F – UK.
  Rang-2-Gegenangabe „Villa PL 3 von 6 über 2,5“ fehlte – B – UK. Datenblatt ohne CL-Einzelspiele – K/H – UK.
- Bodø/LASK: Spielstände, die nur FS belegt, als „Artikel und FS stimmen überein“ dargestellt – G – UK;
  „Pokalspiel“ ohne Quelle – E – UK; CL-Spielertore mit Qualifikation gezählt – A – UK; letzte Einsätze von
  Adeniran, Lang, Helmersen nicht geprüft (Lehre vom 23.11. erneut nicht vollständig angewandt!) – F/B – UK;
  Rang-2-Gegenangabe (Bodøs CL-Heimspiele) als Rang 3 geführt – C – UK; Lage unvollständig – J – UK. Tipps
  blieben.
- Lehre: Bei jedem Spieler – auch in Widerlegungen und bei Ersatzleuten – den letzten Einsatz in FS prüfen; bei
  Abweichungen SM-Spielseite/FS genau sagen, was welche Quelle belegt (Ausgang oder Spielstand).
- Arsenal/Dortmund: Rückkehrer Guirassy ohne Startelf als Rang-1-Grund (wie Atalanta 22.11.) – E/F – UK;
  Widerlegung „seither traf Dortmund immer“ falsch (0:0 Union) – H – UK; Gegenangabe Saka fehlte – B – UK.
- Como/AEK: CL-Spielertore mit Qualifikation – A – UK; AEKs Lage als Gegenangabe fehlte – B – UK.
- Leipzig/Lens: Édouard „Position nicht in der Quelle“, FS hat sie (7b – **dritte Wiederholung** der Lehre vom
  22.11.) – B – UK; „Angriff komplett“ falsch – E/H – UK; „unklar“ als Grund – F – UK; „5 von 6“ statt 6 von 6 – H.
- Feyenoord/Porto: „remains uncertain“ als unklar statt fraglich – F; Belastung Porto fehlte – J – UK.
- Hilfsskript: Tabellen-Sortierung nur nach Tordifferenz, nicht nach Toren – Plätze Dortmund/Betis/AEK/Leipzig
  falsch – M – UK.
- Real/PSV: PSV-Abstand, Heimliga-letzte-6 fehlten, Asencio-Position (7b), Kapitän ohne Richtung in der
  Kennzeichnung, Rotation ungenau widerlegt – H/J/K/7b/E/F – UK.
- **Slovan/Betis: Gegenangabe gegen Über 2,5 falsch gelesen – „3-mal ohne Tor“, aber alle drei Spiele 0:3, 0:4, 0:4
  über 2,5 (H/C – dasselbe Muster wie Levante 23.11.) – Tipp! (Auswärtssieg Betis → Über 2,5, beide einig →
  geteilt).** Dazu Ligaserie falsch (A/H), Heimserie fehlte (J/B), Ceballos-Status (F), Artikel ungenau
  wiedergegeben (E).
- City/Napoli: Rang-2-Gegenangabe (Napoli SA letzte 6) als Rang 3 abgetan – C/B/K (Bodø-Muster); Artikelabweichung
  nicht vermerkt – G; Nunes-Status – F – UK. Tipp neu geprüft, blieb.
- **Muster 24.11.:** Die eigene CL-Anwendung (Heimliga-letzte-6 als Rang 2, CL-Spielorte als Rang 2) wurde nicht
  einheitlich umgesetzt (Bodø, PSV, Betis, Napoli). Lehre: Datenblatt-Feld 4 je Team immer mit allen drei
  Rang-2-Blöcken (alle Wb., CL, Heimliga) füllen; „ohne Tor“ nie als Gegenangabe gegen Über 2,5 ohne die
  Spielstände.
- Tipps blieben in 2a–2d alle. **Offen an den Nutzer:** Häufung bei B/F/7b (Spieler-Angaben) trotz Lehre – Spielerdaten
  werden jetzt für jeden genannten Spieler mit dem Hilfsskript abgerufen, die Prüfung fand aber erst die Kontrolle.

### 24.11.2026 · League One
- **Werkzeugbefund (M):** Das FS-Feld `last_match_timestamp` (league-players) ist teils veraltet (Barry, Magennis,
  Adeboyejo, Page, Leahy, Cook spielten später). Lehre: letzte Einsätze über die Aufstellungen im FS-`match`
  prüfen.
- Bradford/Barnsley: „letzte 6“ nur 5 Spiele, FS-Letzte-6 falsch beschrieben – H/G; „ohne Tor“ gegen Über 2,5 in
  der Marktliste (0:3 lag darüber – **drittes Mal dieses Muster**) – H/C; Gegenangabe McGeehan fehlte – B – UK.
- Stevenage/Sheffield: Widerlegung „2 davon Pokalspiele“ falsch – H; Rückkehrer als neu, obwohl sie schon spielten
  (Werkzeugfeld) – E/F; Gegenangabe Magennis fehlte – B – UK. Tipp neu abgewogen, blieb.
- Blackpool/Leicester: „unterklassig“ ohne Quelle – E; Märkte zusammengelegt – C/K; Lage als Gegenangabe fehlte – B
  – UK.
- Bromley/Wycombe: „startet“ statt „could hand a start“ – F/E (Tipp-Grund); Widerlegung mit Casey als Stammspieler
  falsch – E/H (Tipp-Grund) – UK. Tipp neu abgewogen, blieb.
- Alle 4: Teamnews ohne englischen Wortlaut, eigene Kategorie „voraussichtlich“ – F/6b.

### 24.11.2026 · Scottish Premiership
- Hibernian/Dundee: Mayor „Position nicht in der Quelle“ – FS schreibt „Major“ (Suchfilter verfehlt Spieler) –
  H/B/7b – UK (**Lehre:** bei „nicht gefunden“ auch andere Schreibweisen suchen); Teamnews-Listen vermischt – F/6b;
  Passlack „schon länger“ – H/E; Abstände/Trainer-Spielzahl – J; Kennzeichnung mit Form statt Lage/Teamnews – C/K
  (Muster Levante 23.11.); fehlende Angreifer-Gegenangaben (Lowe, Murray, Wales) – B – UK. Tipp blieb.
- Rangers/Aberdeen: **Direktvergleich in einer Widerlegung** („Aberdeen verlor den Ligapokal gegen Rangers“) –
  L/C/E – UK (erster H2H-Fall seit dem Verbot; Lehre: auch Pokalspiele gegen denselben Gegner sind Direktvergleich,
  nur als Formspiel zählen); Gegenangabe nur mit Rang 3 widerlegt – C/B (Muster Brentford); Bezug alle Wb./Liga – A;
  Märkte unvollständig – K/C; Lage-Gegenangabe fehlte – B; Kennzeichnung beide einig → geteilt – C/K – UK. Tipp blieb.

### 25.11.2026 · Championship
- Burnley/Birmingham: Saison-Heimwerte (BTTS 7/8, 88 %) und Rang 1 (Klarer gesperrt) in Schritt 6 als „Rang 2“
  etikettiert; echter Rang 2 (letzte 6) ist gemischt (Birmingham BTTS 2/6 dagegen) – C/K – UK. Tipp bleibt (Grenzfall).
- Watford/Blackburn: „Letztes Tor 31.10.“ falsch, Watford traf 03.11. – H/J – UK; Gegenangabe Atcheson (Abwehr,
  fällt aus) gegen Unter fehlte – B/7b – UK. Tipp bleibt.
- Bolton/West Brom: „Letzter Sieg 12.09.“ war nur der letzte Heimsieg (letzter Sieg 03.11.) – J/H – UK.
- Stoke/Millwall: „Millwall 3-mal ohne Tor“ als Rang-2-Grund für Unter, obwohl 2 der 3 über 2,5 lagen – H/C
  (**erneut dasselbe Muster** wie Levante 23.11., Slovan 24.11., Bradford 24.11.) – UK; Saisonwerte als Rang 2 (K);
  Lage-Abstand nach unten und Top-Torschützen Dykes/McGlynn fehlten – J/B – UK. Tipp (Heimsieg) nicht betroffen.
- **Muster 25.11.:** „ohne Tor“ ohne Spielstände gegen Über/Unter ist zum vierten Mal aufgetreten (diesmal in der
  Marktliste, ohne Tippwirkung). Lehre erneut: bei „ohne Tor“ immer die Spielstände prüfen, ein 0:3 ist über 2,5.
- Burnley/Birmingham (zweite Grenzfall-Runde): Gegenangabe „letzte 2 Auswärtsspiele je ohne Tor“ falsch gezählt –
  zuletzt 1:3 in Lincoln (3 Tore) – H – UK2. Kein Tipp-Grund, Tipp bleibt.

### 25.11.2026 · Champions League
- Slavia/Villarreal: Šturm (FS „Danijel Šturm“, Angriff, 2 CL-Tore, Startelf 04.11.) und Piták (FS Abwehr) als „Position nicht
  in der Quelle“ geführt – Schreibweise mit Sonderzeichen nicht gesucht (wie Mayor/Major 24.11.); Šturm fehlte als neue
  Rang-1-Gegenangabe – B/H/7b – UK. Tipp neu abgewogen (bleibt), Grenzfall.
- Slavia/Villarreal: Chaloupek „letzter CL-Einsatz 10.09.“ aus dem veralteten FS-Feld (eingewechselt 04.11.) und als
  Einwechselspieler als „Rang 1 dafür“ gewertet – H/E – UK.
- Slavia/Villarreal: Provod „fehlte beim 1:2 gegen Arsenal“ – war ungenutzt auf der Bank – H/E – UK.
- Slavia/Villarreal: Spielbild „trifft ja“ ohne die fehlenden/fraglichen Torschützen (3 von 5 CL-Toren) – B/C – UK.
- Sabah/Barcelona: Christensen „19.09.“ (eingewechselt 08.11.), Rodri „31.10.“ (Startelf 03.11.) aus veralteten FS-Feldern –
  H – UK. Kein Tipp betroffen.
- Slavia/Villarreal (zweite Grenzfall-Runde): Widerlegung „zuletzt 2:0 und davor 1:1“ – davor lag ein 4:1 – H – UK2;
  „seither 0:6, 2:0, 2:3“ galt nur für Moreno, nicht für Akhomach – H – UK2; Rang-2-Gegenangabe „Slavia letzte 6 alle Wb.
  2-mal zu null“ fehlte unter Schritt 6/7 – B – UK2. Kein Tipp-Grund, Tipp bleibt.
- Atlético/Viking: Kennzeichnung „beide einig“ mit nicht neuen Viking-Ausfällen und einseitiger Lage begründet (beide punktgleich
  unter Druck) → geteilt – C/K – UK; Vikings Lage fehlte als Rang-1-Gegenangabe (dreht nein) – B/J – UK.
- Brügge/Liverpool: Ordóñez „ob neu offen“ und als Tipp-Grund – laut FS-Aufstellungen seit 04.11. nicht im Kader – E/B – UK. Lehre:
  auch Spieler, die FS nicht führt, über die Aufstellungen prüfen.
- Inter/Stuttgart: „Lautaro und Bastoni zurück“ als Rang-1-Tipp-Grund (Bastoni spielte alle Ligaspiele, Lautaro nur eingewechselt,
  „must vie“) – E/F – UK (Muster Atalanta 22.11., Guirassy 24.11.); als Grenzfall nachgetragen.
- Lille/Bayern: Neuer und Davies „nicht neu“, aber als Rang-1- und Tipp-Grund – E – UK.
- Atlético/Viking: SM „0:0“ in Tromsø gegen FS „3:2“ mit Aufstellungen und Torschützen – G (Hinweis; SM-Platzhalter).
- **Muster 25.11. (vom Nutzer am 26.11. als Regel 7c übernommen):** Ausfälle oder Rückkehrer ohne Wirkung auf die letzten Spiele wurden in 4 Paarungen als
  Rang-1-Grund gewertet (Chaloupek, Ordóñez, Neuer/Davies, Bastoni). Gegenmaßnahme: Als Rang-1-Grund zählt nur, wer im letzten Spiel
  noch spielte (fehlt neu) bzw. im letzten Spiel fehlte und jetzt sicher zurück ist.
- Schachtar/Fenerbahçe (zweite Runde): Abweichung SM ↔ FS mit falscher Erklärung zugunsten SM entschieden („6 von 6 unter“ nur SM,
  aber Tipp-Grund) – G/H – UK2; Widerlegung „erst durch 2 Gegentore“ für 3:2/2:2 falsch – H/C – UK2; Pedrinho (nicht neu) als Grund –
  E – UK2; feste Unter-Gegenangabe ohne Heimliga-Block (Süper Lig 3-mal 3+) – B/A – UK2. Tipp neu abgewogen, bleibt.
- Atlético/Viking (zweite Runde): Tipp-Grund mit dem strittigen Tromsø-Spiel – G – UK2; Vikings 2:0 in Brann fehlte – B – UK2.
- Inter/Stuttgart (zweite Runde): Lautaro weiter in Widerlegung/Spielbild – E – UK2; Stuttgarts Auswärtsbilanz nur teilweise – B – UK2.
- Lille/Bayern (zweite Runde): Ueda/E. Mbappé (spielten am 21.11.) als Rang-1-Grund und in der Kennzeichnung – E/F – UK2; „Karl
  startet“ statt mögliche Startelf – F – UK2; Lilles Zu-null-Spiele fehlten als Gegenangabe – B – UK2. Tipp bleibt.
- Selbst gefunden: Suárez (2a) und Dembélé (2e) als Verstärkung, obwohl schon zuletzt dabei – E. Lehre (erneut, wie 22.11.): eine
  Korrektur immer in allen Abschnitten suchen, nicht nur an der genannten Stelle.
- Rückblick Merkmale (nach der Auswertung): geänderte Tipps „3 von 9“ statt 4 von 9 gezählt (Treffer falsch addiert) – H – selbst,
  vor der Antwort an den Nutzer berichtigt.
- Lehre (erneut): letzte Einsätze immer über die FS-Aufstellungen beider Wettbewerbe prüfen; bei „nicht gefunden“ immer mit
  einer Suche ohne Sonderzeichen (Normalisierung) nachsuchen – Hilfssuche dafür ab Gruppe 2 benutzt.

### 26.11.2026 · Europa League / Conference League (Ablauf)
- **Neue Fehlerart N · Ablauf/Kapazität (selbst, 21:10):** 26 Paarungen an einem Abend, auf Wunsch des Nutzers („Alle Spiele“)
  mit bis zu 20 parallelen Bearbeitern und 5 Prüfern. Das Nutzungslimit (5 Stunden) war zweimal erreicht (14:40, ca. 16:15 bis
  21:00); **kein Tipp ging vor Anpfiff an den Nutzer**, keine unabhängige Kontrolle (Stufe 3) wurde fertig, 6 Paarungen (2i–2n)
  blieben ohne Analyse. Die 20 fertigen Tipps stehen nur zur Auswertung in der Tagesliste. Kein Tipp falsch begründet gefunden –
  der Fehler liegt in der Planung: Claude hat die Rückfrage nur zur Zeit, nicht zum Nutzungslimit gestellt.
  **Vorschlag an den Nutzer (Regeländerung nur auf Wunsch):** Bei mehr als etwa 8–10 Paarungen an einem Abend vorab fragen, welche
  Spiele Vorrang haben; Bearbeiter nicht alle gleichzeitig starten, sondern gruppenweise (erst 18:45 komplett inkl. Prüfer, dann
  21:00); bei einem Limit-Abbruch sofort dem Nutzer Bescheid geben, welche Gruppe wann frühestens kommen kann.
- **Verstoß gegen die Verbindlichkeit (N, vom Nutzer festgestellt, 21:40):** Claude hat sich nicht an das System gehalten:
  (1) Paarungen parallel statt „jede Paarung einzeln, erst dann die nächste“ – die Antwort „Alle Spiele“ wurde als Erlaubnis
  gedeutet, obwohl der Nutzer die Option „Parallel per Agenten“ nicht ausdrücklich gewählt hatte; (2) 5 Prüfer (A–E) in der
  ersten Runde statt eines Prüfers je Tag mit Weiterführung – eigenmächtig, nur in der Tagesliste vermerkt. Beides widerspricht
  „Ausnahmen oder Änderungen nur auf ausdrücklichen Wunsch des Nutzers; Claude macht keine eigenen“. **Gegenmaßnahme:** Keine
  Abweichung vom Ablauf ohne ausdrückliches Ja des Nutzers zu genau dieser Abweichung; ist eine Antwort mehrdeutig, nachfragen
  statt deuten. Reicht die Zeit im System nicht, offen sagen, welche Spiele nicht geschafft werden (Regel „Reicht die Zeit …“).
- Auswertung Gruppe 1: Uhrzeit „23:05“ geschätzt statt mit `date` abgelesen (richtig 23:00) – M – selbst, vor der Antwort berichtigt.
- 27.11.: „A ok“ als Wahl gedeutet und als Punkt 4 ins System eingetragen; der Nutzer hatte nichts gewählt – N (Deutung statt Nachfrage, trotz neuer Regel) – N, rückgängig gemacht.

### 27.11.2026 · Schritt 1 (PL, Championship, La Liga, Serie A, Bundesliga)
- Southampton/Middlesbrough: Manning als „neu zurück“ (Regel 7c) und Rang-1-Grund für den Heimsieg geführt – laut FS-Aufstellung
  24.11. im Kader, ungenutzt auf der Bank, er fehlte nicht (Muster Provod 25.11.: Bank ≠ fehlte) – E/F – SK (Claude, Stufe 1),
  Tipp-Grund. An allen Stellen korrigiert; Tipp neu abgewogen, bleibt (Heimsieg, geteilt, Grenzfall).
- Venezia/Bologna: „Grenzfall“ in Tabelle und Text, nicht in der Abschnittsüberschrift – M – UK. Kein Tipp betroffen.
- Forest/Chelsea: Artikel-„L“ für das 1:1 im EFL Cup als Quellenfehler (G) bezeichnet, obwohl ein Elfmeterschießen es erklären würde
  – richtig „nicht klärbar“ – G/E (Hinweis) – UK. Ohne Tippwirkung.
- Stufe-1-Vermerke 1a/1b/1c/1e allgemein formuliert (nicht erkennbar, was einzeln geprüft wurde) – M (Hinweis) – UK; präzisiert.
- Werder/Gladbach: Block „letzte 6 alle Wb.“ (Gladbach SM 2-1-3 / FS-lastx 3-1-2, nicht klärbar) als Tipp-Grund und als FS-Seite der
  Kennzeichnung verwendet – gegen Grundsatz 4 – G/H – UK2. Gegenangabe gegen Über 2,5 ohne Spielort (3 der 4 Unter-Spiele Gladbach-
  Heimspiele) – C (Hinweis) – UK2. Tipp bleibt.
- **Southampton/Middlesbrough: Boros Auswärtsbilanz 3-3-2 (nur 2 Niederlagen in 8) als „Rang 3 dafür“ für den Heimsieg; Heimsieg ruhte
  auf Spielort-Teilmengen (2+2 Spiele) und Rang 3, während der ganze Rang-2-Block zu Boro zeigte – C – UK2 – Tipp! (Heimsieg
  Southampton → Beide treffen – Ja, geteilt, Grenzfall).** Dazu B (Hinweis): xG letzte 6 nicht genannt. Lehre: Spielort-Teilmengen der
  letzten 6 (2–3 Spiele) sind kein Ersatz für den ganzen Rang-2-Block – erst den ganzen Block gegen den Tipp lesen.
- Ablauf (M): Die Bearbeiter-Agenten legten Zwischendateien teils im gemeinsamen Scratchpad ab; eine Spielerdatei hatte fremden
  Inhalt (vom Bearbeiter 1c selbst bemerkt und neu abgerufen). Lehre: im Auftrag je Agent einen eigenen Datenordner nennen.

- Schritt 2 · Groningen/Willem II: Vaessen/Hateboer („will welcome back … from suspension“, nur mögliche Startelf) als „neu zurück“ und
  Rang-1-Gegenangabe geführt – Quelle sagt nicht klar „startet“ – Regel 7c – F/E – SK (Claude, Stufe 1). Kein Tipp-Grund; korrigiert.
- Schritt 2 · Ablauf (N): Nutzungslimit um ca. 09:30 erreicht, alle 5 Agenten brachen ab; Fortsetzung um 14:44 per Weiterführung, Vorschauen
  neu abgerufen (unverändert). Kein Tipp nach Anpfiff.
- Schritt 2 · UK1 (Hinweise, ohne Tippwirkung): Rizespor/Kasımpaşa „unveränderte Elf“ als Rang-1-Grund – E/K; Brest/Paris FC Widerlegung
  ohne „Brest hielt nach Lalas Auswechslung (27.) die Null“ – B/H; Marítimo/Nacional FS-lastx „stimmt genau“ trotz anderer Heim/Auswärts-
  Aufteilung – G/H. Alle eingearbeitet.
- Schritt 2 · UK2 (Hinweise, ohne Tippwirkung): Rizespor/Kasımpaşa – UK1-Korrektur „unveränderte Elf“ nur an 2 von 5 Stellen umgesetzt
  (E/K; Lehre 22.11./25.11. erneut: Korrektur im ganzen Abschnitt suchen – Claude hat nur die vom Prüfer genannten Stellen geändert),
  Gegner-Tabellenplätze als Rang 2 (K/C). Brest/Paris FC: xG letzte 6 fehlte als Rang-2-Angabe (B). Marítimo/Nacional: Widerlegung mit
  Nacionals Heim-Zu-null-Spielen ohne „daheim“ gegen eine Auswärts-Gegenangabe (A/C, Muster Levante 23.11.), xG gegen fehlte (B).

### 28.11.2026 · Regeln und Werkzeuge (Systemprüfung auf Wunsch des Nutzers, selbst gefunden – vor dem ersten Einsatz von 1.4)
- `datenblatt.py` prüfte Regel 7c am letzten **Ligaspiel** statt am letzten **Pflichtspiel** – bei Europapokal-Teilnehmern das
  falsche Spiel (Test 28.11.: Manchester United, Real Madrid, Inter spielten am 24./25.11. Champions League, das Werkzeug zeigte
  die Elf vom 22.11.) – M/E – kein Tipp betroffen (Werkzeug noch in keiner Analyse eingesetzt). Behoben: letztes Pflichtspiel laut
  FS (Liga + Europapokal, im Europapokal mit `--liga-heim`/`--liga-gast`), Warnung „ACHTUNG Regel 7c“ bei nationalem Pokalspiel.
- `datenblatt.py` glich nur SM → FS ab: Fehlte in den SM-Formdaten das neueste Spiel, kam keine Meldung; die Zuordnung nahm das
  erste FS-Spiel mit einem gemeinsamen Namenswort („City“, „United“, „Real“) und konnte bei auseinanderlaufenden Quellen das
  falsche Spiel treffen und dessen Ergebnis als „FS-Wert“ einsetzen – M/G – kein Tipp betroffen. Behoben: Abgleich in beide
  Richtungen, Zuordnung über Spielort, ganzen Gegnernamen und Ergebnis; getestet mit nachgestellten Fällen (SM veraltet um 1 und 2
  Spiele, Platzhalter 0:0, falsches SM-Ergebnis, anderer Kurzname, unbekannter Wettbewerbs-Link) und 37 Namenspaaren.
- `tippanalyse.py` las nur Listen `2026-11-*` (ab 01.12. nichts Neues), wertete Kräfteverhältnis und „Spielen“ nicht aus, trennte
  nicht vor/seit 1.4 und fand 0 geänderte Tipps, obwohl 3 in den Listen stehen (Schreibweise „zuvor: …“) – M/H – behoben. Die
  Zahlen der Analyse vom 27.11. (80 Tipps, 47 Treffer, Wettarten, Kennzeichnung × Grenzfall) sind unverändert.
- Alle drei Kontrollen (Bearbeiter, Stufe 1, Prüfer) stützen sich seit dem Sparplan auf dasselbe Werkzeug – ein Zählfehler dort
  fiele keiner auf – M (Lücke im Ablauf). Gegenmaßnahme seit 1.4.1: Stichprobe von Hand durch den Prüfer (eine Paarung je Schritt).
- Agenten-Aufträge `bearbeiter.md`/`pruefer.md` und der Absatz „Verbindlich“ in `CLAUDE.md` nannten noch „Version 1.3“; `CLAUDE.md`
  Punkt 3 nannte die Grenzfall-Runde ohne „mit Spielen: ja“ – M – berichtigt. Als Vorlage lasen die Bearbeiter einen 1.3-Abschnitt
  ohne 4b – jetzt `VORLAGE-ABSCHNITT.md` und `MUSTERFAELLE.md`.
- Analyse vom 27.11. (Grundlage von 1.4), Hinweise zur Aussagekraft – E/H (Hinweis, keine Regel deshalb geändert): (a) „in 19 von 21
  verfehlten Tor-Tipps blieb ein Team ohne Tor bzw. gewann deutlich“ folgt zum Teil aus der Definition (ein verfehltes Beide treffen
  – Ja hat immer ein Team ohne Tor) und belegt nicht, dass Schritt 4b diese Spiele vorher als „klarer Favorit“ erkannt hätte;
  (b) der Abstand „beide einig“ 20 von 29 gegen „geteilt“ 26 von 49 kann bei so wenigen Tipps Zufall sein und liegt fast ganz bei
  Über 2,5 (7 von 8 gegen 3 von 10; ohne Über 13 von 21 gegen 23 von 39). Gegenmaßnahme seit 1.4.1: Schattentipp (Merkmal 12),
  Bericht erst nach 50 gespielten Tipps, Abschnitt „Änderungen am System“.

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
- **Werkzeuge sind eine gemeinsame Fehlerquelle** (28.11.): Was das Werkzeug falsch zählt, sehen Bearbeiter, Claude und Prüfer
  gleich falsch – darum je Schritt eine Stichprobe von Hand; neue oder geänderte Werkzeuge an echten Spielen **und** an
  nachgestellten Fehlerfällen testen, bevor sie in einer Analyse laufen.
- **Zahlen aus der Auswertung immer mit Fallzahl** (28.11.): Ein Muster aus wenigen Dutzend Tipps ist eine Richtung, kein Beleg;
  was aus der Definition des Marktes folgt, ist gar kein Muster.
- **Alle Tippänderungen** kamen aus **B, C, E, F**: Gegenangaben und Abwägung sind die Stellen, an
  denen Fehler den Tipp kosten.
