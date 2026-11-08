# Forebet-Check (System B) · Version 2.1

Vom Nutzer festgelegt am 07.11.2026 (Version 2), Rangfolge ergänzt am 08.11.2026 (Version 2.1)
nach der MLS-Auswertung. Ersetzt Version 1 (06.11.2026, Odd Alerts mit Quoten).
Eigener Branch; getrennt vom OddAlerts-System v1.3-OA und vom Spielcheck (System A).

## Grundsätze

1. **Keine Quoten.** Quoten, Quotenbewegungen, nötige Trefferquote, Vorteil/fair und
   Buchmacher werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Datenquelle ist FootyStats** (`https://api.football-data-api.com/`). Odd Alerts wird nicht
   mehr verwendet.
3. **Forebet-Vorschau und FootyStats-Daten** sind die Grundlage. Sie werden **nicht auf
   Übereinstimmung** geprüft, sondern nach der **Rangfolge** unten gewichtet; daraus folgt
   **ein Tipp**.

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

## Rangfolge der Informationen

| Rang | Information | Quelle |
|---|---|---|
| 1 | Konkrete Spielinformationen: Ausfälle, Aufstellung, Trainer, Torwart | Forebet |
| 2 | **Aktuelle Form:** letzte 6 Spiele, letzte 3 Heim- bzw. Auswärtsspiele, laufende Serien | Forebet („Aktuelle Form“, „Haupttrends“) + FootyStats (letzte 6 aller Wettbewerbe, letzte 6 Ligaspiele) |
| 3 | Forebet-Prognose: Wahrscheinlichkeit, erwartetes Ergebnis, erwartete Tore | Forebet |
| 4 | Saisonwerte: Heim/Auswärts-Bilanz, Tore, xG, Tabelle, Vorab-xG | FootyStats + Forebet („Gesamtbild in der Liga“) |
| 5 | Direktvergleiche und lange Trends (z. B. „16 der letzten 20“) | beide |

## Regeln für den Tipp

1. **Ein Tipp je Spiel**, deutlich als „Tipp“ markiert.
2. **Richtung des Tipps aus Rang 1–3.** Rang 4 und 5 helfen nur bei der Wahl des Markts (z. B.
   Sieger oder Tore) und drehen die Richtung nicht um.
3. **Form vor Saison:** Ein Team mit **höchstens 1 Sieg aus den letzten 6** bekommt **keinen
   Sieg-Tipp**, auch als Heimteam oder Tabellenfavorit.
4. **Kein Kompromiss-Markt** nur weil Informationen sich widersprechen; gewählt wird der Markt,
   den die oberen Ränge am klarsten tragen.
5. Märkte: Sieg, Doppelte Chance, Über/Unter, beide treffen, Team trifft u. ä.
6. Keine Schwellen, keine Spielcheck-Zählung („x von 10“).
7. **Bedenken nach Stärke:** stark = Information aus Rang 1 oder 2 (Ausfall, Trainer, aktuelle
   Form); schwach = Rang 4 und 5 (Saisonstatistik, Direktvergleiche, lange Trends). Spricht
   eine starke Bedenke klar gegen den Tipp, nimmt Claude den nächststärkeren Markt.
8. Zahlen aus Forebet, die FootyStats widersprechen, werden kurz vermerkt; die Forebet-Angabe
   wird dadurch nicht verworfen (Wettbewerbe können unterschiedlich gezählt sein).

## Antwortaufbau je Spiel

1. Rang 1–3: Spielinformationen, aktuelle Form, Forebet-Prognose
2. Rang 4–5: Saison, Heim/Auswärts, Direktvergleiche (FootyStats und Forebet)
3. Spielbild nach Rangfolge
4. ✅ **Tipp** mit Gründen und Bedenken (stark/schwach)

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/forebet/JJJJ-MM-TT.md` (mit FootyStats-`match_id`) und
werden dort nach Abpfiff ausgewertet (Treffer je Tipp, Trefferquote; keine Einheiten/Quoten).
Vorschauen möglichst vor Anpfiff; Tipps nach Anpfiff werden in der Liste vermerkt.
