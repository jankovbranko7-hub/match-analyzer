# Werkzeuge

Sports-Mole-Check (seit 20.11.2026):
- `datenblatt.py <saison> "<FS-Heim>" "<FS-Gast>" [--sm "<sm-heim>" "<sm-gast>" | --sm-seite <URL>] [--spieler-heim "A,B"]
  [--spieler-gast "C,D"] [--ep <saison>]` (seit 27.11.2026, Pflicht) – ein Aufruf liefert das gezählte Datenblatt beider Teams:
  Tabelle mit Abständen, letzte 6 Liga und alle Wb. (SM-Formdaten, mit FS abgeglichen, Abweichungen gemeldet), Heim/Auswärts,
  Serien, Gegnerstärke (Schritt 4b), Startelf des letzten Ligaspiels und Regel-7c-Status der Teamnews-Spieler.
- `tippanalyse.py` – Auswertung aller Tipps (Wettart, Kennzeichnung, Grenzfall, zweitbester Markt, Liga, verfehlte Tor-Tipps).
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
