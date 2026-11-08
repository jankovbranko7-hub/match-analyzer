# Forebet-Check (System B) · Version 2.3

Vom Nutzer festgelegt am 07.11.2026 (Version 2), Rangfolge ergänzt am 08.11.2026 (Version 2.1)
nach der MLS-Auswertung; Forebet-Prognose aus der Tippfindung genommen am 08.11.2026 (Version 2.2); Märkte auf Sieg,
beide treffen und über/unter 2,5 begrenzt am 08.11.2026 (Version 2.3). Ersetzt Version 1 (06.11.2026, Odd Alerts mit Quoten).
Eigener Branch; getrennt vom OddAlerts-System v1.3-OA und vom Spielcheck (System A).

## Grundsätze

1. **Keine Quoten.** Quoten, Quotenbewegungen, nötige Trefferquote, Vorteil/fair und
   Buchmacher werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Datenquelle ist FootyStats** (`https://api.football-data-api.com/`). Odd Alerts wird nicht
   mehr verwendet.
3. **Die Fakten aus der Forebet-Vorschau und die FootyStats-Daten** sind die Grundlage. Sie
   werden **nicht auf Übereinstimmung** geprüft, sondern nach der **Rangfolge** unten
   gewichtet; daraus macht Claude **einen eigenen Tipp**.
4. **Die Forebet-Prognose** (Wahrscheinlichkeit, erwartetes Ergebnis, Forebets Tipp wie „über
   2,5“) fließt **nicht** in den Tipp ein. Sie wird erst nach dem Tipp **zum Vergleich**
   genannt und in der Tagesliste mitgeführt, damit beide ausgewertet werden können.

## Eingang je Spiel: Forebet-Vorschau

Der Nutzer schickt je Spiel, was Forebet in der Vorschau angibt. Die Abschnitte unterscheiden sich
von Spiel zu Spiel; verwendet wird alles, was vorhanden ist:
- Teamnews und voraussichtliche Aufstellungen
- Prognose (Wahrscheinlichkeit, erwartetes Ergebnis) – nur zum Vergleich, nicht für den Tipp
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
| 1 | Konkrete Spielinformationen: Ausfälle, Sperren, Aufstellung, Trainer, Torwart, Belastung (Europapokal) | Forebet |
| 2 | **Aktuelle Form:** letzte 6 Spiele, letzte 3 Heim- bzw. Auswärtsspiele, laufende Serien (Tore, ohne Tor, zu null) | Forebet („Aktuelle Form“, „Haupttrends“) + FootyStats (letzte 6 aller Wettbewerbe, letzte 6 Ligaspiele, Trends) |
| 3 | Saisonwerte: Heim/Auswärts-Bilanz, Tore, xG, Tabelle, Vorab-xG und Torpotenzial | FootyStats + Forebet („Gesamtbild in der Liga“) |
| 4 | Direktvergleiche und lange Trends (z. B. „16 der letzten 20“) | beide |
| – | Forebet-Prognose | nur Vergleich, kein Einfluss |

## Regeln für den Tipp

1. **Ein Tipp je Spiel**, deutlich als „Tipp“ markiert, aus Rang 1–4 – ohne Forebet-Prognose.
2. **Richtung aus Rang 1–2.** Rang 3 bestimmt die Richtung nur, wenn Rang 1–2 keine klare
   Richtung zeigen. Rang 3 und 4 helfen bei der Wahl des Markts (Sieger, Tore,
   beide treffen) und drehen eine klare Richtung aus Rang 1–2 nicht um.
3. **Form vor Saison:** Ein Team mit **höchstens 1 Sieg aus den letzten 6** bekommt **keinen
   Sieg-Tipp**, auch als Heimteam oder Tabellenfavorit.
4. **Kein Kompromiss-Markt** nur weil Informationen sich widersprechen; gewählt wird der Markt,
   den die Daten am klarsten tragen.
5. **Erlaubte Märkte – nur diese sechs:** Heimsieg, Auswärtssieg, Beide treffen – Ja,
   Beide treffen – Nein, Über 2,5 Tore, Unter 2,5 Tore. **Keine anderen Wettarten** (keine
   Doppelte Chance, kein Remis, kein „Team trifft“, keine anderen Torlinien wie 1,5 oder 3,5).
6. Keine Schwellen, keine Spielcheck-Zählung („x von 10“).
7. **Bedenken nach Stärke:** stark = Information aus Rang 1 oder 2; schwach = Rang 3 und 4.
   Spricht eine starke Bedenke klar gegen den Tipp, nimmt Claude den nächststärkeren Markt.
8. Zahlen aus Forebet, die FootyStats widersprechen, werden kurz vermerkt; die Forebet-Angabe
   wird dadurch nicht verworfen (Wettbewerbe können unterschiedlich gezählt sein).

## Antwortaufbau je Spiel

1. Rang 1–2: Spielinformationen, aktuelle Form
2. Rang 3–4: Saison, Heim/Auswärts, Vorab-xG, Direktvergleiche (FootyStats und Forebet)
3. ✅ **Tipp** mit Gründen und Bedenken (stark/schwach)
4. Zum Vergleich: Forebet-Prognose (gleich oder abweichend)

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/forebet/JJJJ-MM-TT.md` (mit FootyStats-`match_id` und
Spalte „Forebet-Prognose“) und werden dort nach Abpfiff ausgewertet: Treffer je Tipp und
Trefferquote, getrennt für Claudes Tipp und Forebets Prognose; keine Einheiten/Quoten.
Vorschauen möglichst vor Anpfiff; Tipps nach Anpfiff werden in der Liste vermerkt.
