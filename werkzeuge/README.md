# Werkzeuge

Sports-Mole-Check (seit 20.11.2026):
- `datenblatt.py <saison> "<FS-Heim>" "<FS-Gast>" [--sm "<sm-heim>" "<sm-gast>" | --sm-seite <URL>] [--spieler-heim "A,B"]
  [--spieler-gast "C,D"] [--ep <saison>] [--liga-heim <saison>] [--liga-gast <saison>]` (seit 27.11.2026, Pflicht) – ein Aufruf
  liefert das gezählte Datenblatt beider Teams: Tabelle mit Abständen, letzte 6 Liga und alle Wb., Heim/Auswärts, Serien,
  Gegnerstärke, Tabellen- und Spielort-Vergleich (Schritt 4b), „Tabellenhöher“ (Merkmal 10). Seit 28.11.2026 (1.4.1):
  Startelf und Regel-7c-Status am **letzten Pflichtspiel laut FS** (Liga und Europapokal; im Europapokal mit `--liga-heim`/
  `--liga-gast` auch die Heimliga) mit Warnung, wenn das neueste SM-Spiel ein nationales Pokalspiel war; Abgleich SM ↔ FS **in
  beide Richtungen** (fehlt ein FS-Spiel in den SM-Formdaten, wird es gemeldet und in den Block aufgenommen; Zuordnung über
  Spielort, ganzen Gegnernamen und Ergebnis; „Hinweise zur Zuordnung“ bei anders geschriebenen Namen); bei „3+ eigene Tore“ sind
  nationale Pokalspiele einzeln genannt (unterklassige Gegner zählen nach 1.4.1 nicht). Seit 28.11.2026 (nach Schritt 1): Trifft ein
  Suchname aus nur einem Wort nicht den Nachnamen des FS-Eintrags, steht „ZUORDNUNG PRÜFEN“ dabei – Spieler mit vollem Namen übergeben.
- `vorpruefung.py "<Liga wie in der SM-Übersicht>" [Wochentag] [--saison <FS-Saison>]` (seit 28.11.2026) – Vorprüfung vor der
  Spielauswahl: für alle Spiele der Liga mit SM-Vorschau nur die Zahlenseite (vier Bausteine aus Schritt 4b, Spielort, Tor-Zahlen
  der letzten 6), ohne Agenten, ohne Teamnews – kein Tipp. Den Satz „Zahlen zeigen zu: …“ schreibt Claude, die 5 Spiele wählt der
  Nutzer (Abschnitt „Vorprüfung“ in `SPORTSMOLE-CHECK.md`).
- `teamnews2.py "<Liga>" "<Heim>" "<Gast>" [--spieler-heim "A,B"] [--spieler-gast "C,D"]` (seit 28.11.2026, Version 1.5, Regel 7e) –
  Zweitquelle Teamnews: holt die frei zugänglichen Ausfall- und Sperrenlisten des Landes (LigaInsider, FútbolFantasy, Fantacalcio,
  offizielle Premier-League-Fantasy-Liste; für alle Ligen zusätzlich die Sammelseite Sportsgambler) und stellt sie neben die
  Spielernamen aus den Sports-Mole-Teamnews: bestätigt / nur Sports Mole / nur Zweitquelle. Seit Version 1.5 Teil der
  Entscheidung: Nur was Sports Mole und die Länderquelle beide führen, gibt eine Richtung; der Bearbeiter ruft es je Paarung auf,
  Claude und der Prüfer rufen es selbst neu ab. Die Sammelseite ist kein Beleg. Findet es ein Team nicht eindeutig, nennt es die
  Teamnamen der Quelle – dann mit diesem Namen erneut aufrufen.
- `tippanalyse.py` – Auswertung aller Tipps aller Monate (Wettart, Kennzeichnung, Grenzfall, zweitbester Markt, geänderte Tipps,
  Liga, verfehlte Tor-Tipps), getrennt vor/seit 1.4; seit 1.4: „Spielen: ja/nein“ mit Zählerstand der gespielten Tipps (Bericht an
  den Nutzer ab 50), Kräfteverhältnis, Schattentipp, Vergleichswert „der Tabellenhöhere gewinnt“, Vorprüfung (Merkmal 13), Zweitquelle Teamnews (Merkmal 14), Tipp und „Spielen“ ohne Zweitquelle (Merkmal 15).
- `sm_spiel.py liste` – alle Vorschauen der Übersicht: Tag | Liga | Anstoß (deutsche Zeit) | Paarung | URL.
- `sm_spiel.py tag "<Liga>" [Wochentag]` – nur eine Liga, ohne Wochentag der erste Tag (heute).
- `sm_spiel.py "<Heim-Teil>" "<Gast-Teil>"` – Vorschau-Artikel und Spielseite (ohne Datenanalyse:
  Formleisten, Formdaten; ohne Direktvergleiche), Tabelle und Torschützenliste einer Paarung als Text, Teilnamen in Sports-Mole-Schreibweise
  (z. B. `barnsley sheff`). Ohne Quoten, ohne „We say“ (seit Version 1.3). Formdaten je Team
  neuestes zuerst, je Spiel mit Wettbewerb (Liga / anderer Wb.) und S/U/N aus Sicht des Teams.
- `abgleich.py <season_id> "<SM-Heim>" "<SM-Gast>" ["<FS-Heim>" "<FS-Gast>"]` (seit Version 1.3) –
  automatischer Abgleich Sports Mole ↔ FootyStats: Tabellenplatz, Ligaspiele (Heim/Auswärts,
  Spielstand), S-U-N und Tore der letzten 6 aller Wettbewerbe; meldet jede „ABWEICHUNG“. Dazu
  Tabellenstand mit Abständen nach oben/unten und zum Abstiegs-/Relegationsplatz (Datenblatt).
- `kontext.py <team_id> <liga_saison> ["Name1,Name2"] [<europapokal_saison>]` (seit 24.11.2026) – Kontext
  eines Teams aus FootyStats: Tabelle aus den FS-Spielen mit Nachbarn, letzte Spiele, nicht ausgetragene
  Spiele (nicht zählen), Kennzahlen (letzte 6, daheim/auswärts), nächste Spiele und Spieler mit Position,
  Toren und letztem Einsatz (FS-Feld teils veraltet – im Zweifel Aufstellung im FS-`match` prüfen).
  Wird auch vom Prüfer-Agenten `pruefer` (`.claude/agents/pruefer.md`) genutzt.

FootyStats (Zahlen, Abgleich und Ergebnisse; ohne Vorab-Werte); Odd-Alerts-Skripte werden nicht mehr verwendet:

Alle Skripte lesen die Schlüssel nur aus der Umgebung (`APIKEY` für FootyStats, `ODDALERTS_KEY`
für Odd Alerts) und schwärzen sie als `[REDACTED]`. Keine Quoten.

- `fs.sh <pfad> [k=v ...]` – ein API-Abruf, z. B. `werkzeuge/fs.sh match match_id=8572478`.
  Letzte Zeile: `__HTTP <code>`.
- `fs_spiel.py <season_id> "<Heim-Teilname>" "<Auswärts-Teilname>"` – alle FootyStats-Daten zu
  einem Spiel für den Sports-Mole-Check 1.2 (Saison, Heim/Auswärts, letzte 6 aller
  Wettbewerbe, letzte 6 Ligaspiele, Trends). Keine Quoten, keine Vorab-Werte, keine Direktvergleiche.
- `fs_ergebnis.py <match_id> ...` – Endergebnisse für die Auswertung.
- (Gehört zu Version 2.12, seit dem 20.11.2026 nicht mehr Teil des Systems:) `fs_haekchen.py <season_id> "<Heim>" "<Auswärts>" [heim|ausw|ja|nein|ueber|unter]` – Forebet-Check
  v2.12: Schritt 1/2 mechanisch und die Häkchen „Form“ und „Saison am Spielort“ für die Einstufung
  klar/knapp, nach festen Regeln (im Kopf des Skripts); ohne Tipp eine Tabelle für alle sechs
  Märkte. Das Häkchen „Ausfälle/Motivation“ setzt Claude aus der Vorschau.

Odd Alerts:
- `oa.sh <pfad> [k=v ...]` – ein API-Abruf, z. B. `werkzeuge/oa.sh fixtures/upcoming competitions=477`.
- `oa_spiel.py <competition_id> "<Heim-Teilname>" "<Auswärts-Teilname>"` – Saisonwerte gesamt und
  Heim/Auswärts, Odd-Alerts-Modell (nur zum Vergleich; nur für Spiele der nächsten ~5 Tage).
- `ergebnisse.py <comp_ids> "<Heim>" "<Auswärts>"` – letzte 10 Pflichtspiele inkl. Pokal,
  Heim-/Auswärtsspiele, Direktvergleiche (exakte Teamnamen wie in der API).

Saison-IDs FootyStats: `FOOTYSTATS-API.md`. Wettbewerbs-IDs Odd Alerts (Auswahl): Bundesliga 477,
2. Bundesliga 471, DFB-Pokal 417, Premier League 423, Championship 418, FA Cup 327, Carabao Cup 268,
La Liga 419, Serie A 499, Coppa Italia 531, Serie B 545, Ligue 1 200, Ligue 2 256, Eredivisie 437,
Pro League (BEL) 198, Süper Lig 414, Allsvenskan 255, Admiral Bundesliga (AUT) 411, Champions League 51.
