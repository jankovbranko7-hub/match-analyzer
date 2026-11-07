# Forebet-Check (System B) · Version 2

Vom Nutzer festgelegt am 07.11.2026. Ersetzt Version 1 (06.11.2026, Odd Alerts mit Quoten).
Eigener Branch; getrennt vom OddAlerts-System v1.3-OA und vom Spielcheck (System A).

## Grundsätze

1. **Keine Quoten.** Quoten, Quotenbewegungen, nötige Trefferquote, Vorteil/fair und
   Buchmacher werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Datenquelle ist FootyStats** (`https://api.football-data-api.com/`). Odd Alerts wird nicht
   mehr verwendet.
3. **Zwei Säulen, beide stark gewichtet:**
   - **Forebet** (vom Nutzer je Spiel geschickt) – **sehr stark** gewichtet.
   - **FootyStats** (von Claude je Spiel ausgewertet) – **stark** gewichtet.
   Beide werden zu **einem Spielbild** zusammengeführt; daraus folgt **ein Tipp**.

## Eingang je Spiel: Forebet-Vorschau

Der Nutzer schickt je Spiel, was Forebet in der Vorschau angibt. Die Abschnitte unterscheiden sich
von Spiel zu Spiel; verwendet wird alles, was vorhanden ist:
- Teamnews und voraussichtliche Aufstellungen
- Prognose (Wahrscheinlichkeit, erwartetes Ergebnis)
- Haupttrends
- Gesamtbild in der Liga
- Aktuelle Form
- Direkte Duelle
- Wichtigste Fakten

Ausfälle, Sperren, Trainerwechsel und Aufstellungen aus Forebet gelten als gesetzt.

## FootyStats je Spiel (`werkzeuge/fs_spiel.py`)

- Vorab-Werte des Spiels: erwartete Tore (xG) je Team, Torpotenzial (über 1,5 / 2,5 / 3,5,
  beide treffen), Punkte pro Spiel vor dem Spiel
- Saison gesamt und Heim (Heimteam) bzw. auswärts (Gastteam): Tabellenplatz, S-U-N, Tore, Punkte
  pro Spiel, xG für/gegen, über 2,5 %, beide treffen %, zu null %, ohne Tor %
- Letzte 6 über **alle Wettbewerbe** (inkl. Europapokal und Pokal) und letzte 6 Ligaspiele
- Direktvergleiche (Bilanz, Ø Tore, letzte Ergebnisse) und FootyStats-Trends

## Zusammenführung zum Spielbild

1. Aus Forebet: Wer ist stärker, welches Ergebnis wird erwartet, welche konkreten Umstände
   (Ausfälle, Aufstellung, Trainer, Serien) prägen das Spiel?
2. Aus FootyStats: Bestätigen Saison, Heim/Auswärts, Form aller Wettbewerbe, xG und
   Direktvergleiche dieses Bild?
3. **Stimmen beide überein**, liegt der Tipp dort.
4. **Weichen sie ab**, wiegen konkrete Spielinformationen aus Forebet (Ausfälle, Aufstellung,
   Trainer) schwerer als Statistik aus der Vergangenheit. Claude wählt dann den Markt, in dem
   beide Quellen am ehesten zusammenpassen (z. B. Doppelte Chance statt Sieg, Tore statt
   Sieger), und benennt die Abweichung.
5. Zahlen aus Forebet, die FootyStats widersprechen, werden kurz vermerkt; die Forebet-Angabe
   wird dadurch nicht verworfen (Wettbewerbe können unterschiedlich gezählt sein).

## Regeln für den Tipp

- **Ein Tipp je Spiel** aus dem zusammengeführten Spielbild, deutlich als „Tipp“ markiert.
- Märkte: Sieg, Doppelte Chance, Über/Unter, beide treffen, Team trifft u. ä. – je nachdem, was das
  Spielbild am klarsten trägt.
- Keine Schwellen, keine Spielcheck-Zählung („x von 10“).
- **Bedenken nach Stärke:** stark = konkrete Information zu genau diesem Spiel (Ausfall,
  Systemumstellung, Trainerwechsel); schwach = allgemeine Statistik aus der Vergangenheit.
  Spricht eine starke Bedenke klar gegen den Tipp, nimmt Claude den nächststärkeren Markt.

## Antwortaufbau je Spiel

1. Forebet (Kernaussagen der geschickten Abschnitte)
2. FootyStats (Saison, Heim/Auswärts, Form, Direktvergleiche, Vorab-xG)
3. Spielbild (zusammengeführt; Übereinstimmung oder Abweichung)
4. ✅ **Tipp** mit Gründen und Bedenken (stark/schwach)

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/forebet/JJJJ-MM-TT.md` (mit FootyStats-`match_id`) und
werden dort nach Abpfiff ausgewertet (Treffer je Tipp, Trefferquote; keine Einheiten/Quoten).
