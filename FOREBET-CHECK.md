# Forebet-Check (System B) · Version 2.6

Vom Nutzer festgelegt am 07.11.2026 (Version 2), Rangfolge ergänzt am 08.11.2026 (Version 2.1)
nach der MLS-Auswertung; Forebet-Prognose aus der Tippfindung genommen am 08.11.2026 (Version 2.2); Märkte auf Sieg,
beide treffen und über/unter 2,5 begrenzt am 08.11.2026 (Version 2.3); fester Entscheidungsweg
Schritt 1–4 am 09.11.2026 (Version 2.4); Odd-Alerts-Vorschau als Ersatz für fehlende
Forebet-Vorschauen und Odd-Alerts-API als zweite Datenquelle am 09.11.2026 (Version 2.5); „klare Seite“ in Schritt 2 genau nach
den 6 neu gemachten Tipps vom 08.11. festgelegt am 09.11.2026 (Version 2.6). Ersetzt Version 1 (06.11.2026, Odd Alerts mit Quoten).
Eigener Branch; getrennt vom OddAlerts-System v1.3-OA und vom Spielcheck (System A).

## Grundsätze

1. **Keine Quoten.** Quoten, Quotenbewegungen, nötige Trefferquote, Vorteil/fair und
   Buchmacher werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Datenquellen sind FootyStats** (`https://api.football-data-api.com/`) **und die Odd-Alerts-API**
   (`https://data.oddalerts.com/api/`). Von Odd Alerts werden nur Statistik, Ergebnisse und
   Direktvergleiche genutzt – **keine Quoten-Endpunkte** (`odds/…`).
3. **Die Fakten aus der Vorschau (Forebet oder Odd Alerts) und die Daten aus FootyStats und
   Odd Alerts** sind die Grundlage. Sie
   werden **nicht auf Übereinstimmung** geprüft, sondern nach der **Rangfolge** unten
   gewichtet; daraus macht Claude **einen eigenen Tipp**.
4. **Prognosen** – Forebet-Prognose, Prognose der Odd-Alerts-Vorschau und das Odd-Alerts-Modell
   (Wahrscheinlichkeit, erwartetes Ergebnis, Tipp wie „über 2,5“) – fließen **nicht** in den
   Tipp ein. Sie wird erst nach dem Tipp **zum Vergleich**
   genannt und in der Tagesliste mitgeführt, damit beide ausgewertet werden können.

## Eingang je Spiel: Forebet-Vorschau, sonst Odd-Alerts-Vorschau

Der Nutzer schickt je Spiel, was Forebet in der Vorschau angibt. **Hat Forebet für ein Spiel oder
eine Liga keine Vorschau, schickt er die Odd-Alerts-Vorschau**; sie wird genauso behandelt
(Fakten nach Rangfolge, Prognose nur zum Vergleich). Die Abschnitte unterscheiden sich
von Spiel zu Spiel; verwendet wird alles, was vorhanden ist:
- Teamnews und voraussichtliche Aufstellungen
- Prognose (Wahrscheinlichkeit, erwartetes Ergebnis) – nur zum Vergleich, nicht für den Tipp
- Haupttrends
- Gesamtbild in der Liga
- Aktuelle Form
- Direkte Duelle
- Wichtigste Fakten

Ausfälle, Sperren, Trainerwechsel und Aufstellungen aus der Vorschau gelten als gesetzt.

## FootyStats je Spiel (`werkzeuge/fs_spiel.py`)

- Vorab-Werte des Spiels: erwartete Tore (xG) je Team, Torpotenzial (über 1,5 / 2,5 / 3,5,
  beide treffen), Punkte pro Spiel vor dem Spiel
- Saison gesamt und Heim (Heimteam) bzw. auswärts (Gastteam): Tabellenplatz, S-U-N, Tore, Punkte
  pro Spiel, xG für/gegen, über 2,5 %, beide treffen %, zu null %, ohne Tor %
- Letzte 6 über **alle Wettbewerbe** (inkl. Europapokal und Pokal) und letzte 6 Ligaspiele
- Direktvergleiche (Bilanz, Ø Tore, letzte Ergebnisse) und FootyStats-Trends

## Odd Alerts je Spiel (`werkzeuge/oa_spiel.py`, `werkzeuge/ergebnisse.py`)

- Saisonwerte gesamt und Heim/Auswärts (`stats/fixture`): S-U-N, Tore, über 2,5 %, beide
  treffen %, zu null, ohne Tor, xG
- Letzte 10 Pflichtspiele inkl. Pokal, Heim-/Auswärtsspiele und Direktvergleiche
  (`fixtures/between`); Champions League ID 51
- Odd-Alerts-Modell (`trends/btts` → `probability`): **nur zum Vergleich**
- Zweite Quelle zur Gegenprüfung von FootyStats und Ersatz, wo FootyStats eine Liga nicht hat

## Rangfolge der Informationen

| Rang | Information | Quelle |
|---|---|---|
| 1 | Konkrete Spielinformationen: Ausfälle, Sperren, Aufstellung, Trainer, Torwart, Belastung (Europapokal) | Vorschau (Forebet oder Odd Alerts) |
| 2 | **Aktuelle Form:** letzte 6 Spiele, letzte 3 Heim- bzw. Auswärtsspiele, laufende Serien (Tore, ohne Tor, zu null) | Vorschau („Aktuelle Form“, „Haupttrends“) + FootyStats (letzte 6 aller Wettbewerbe, letzte 6 Ligaspiele, Trends) + Odd Alerts (letzte 10 inkl. Pokal) |
| 3 | Saisonwerte: Heim/Auswärts-Bilanz, Tore, xG, Tabelle, Vorab-xG und Torpotenzial | FootyStats + Odd Alerts + Vorschau („Gesamtbild in der Liga“) |
| 4 | Direktvergleiche und lange Trends (z. B. „16 der letzten 20“) | beide |
| – | Prognosen: Forebet, Odd-Alerts-Vorschau, Odd-Alerts-Modell | nur Vergleich, kein Einfluss |

## Entscheidungsweg je Spiel (Schritt 1–4, immer in dieser Reihenfolge)

1. **Wer bekommt keinen Sieg-Tipp?** Jedes Team mit höchstens 1 Sieg aus den letzten 6
   Spielen aller Wettbewerbe scheidet für einen Sieg-Tipp aus (Regel 3).
2. **Gibt es eine klare Seite?** Ein Team ist die klare Seite, wenn **beides** gilt:
   a) es hat **mindestens 3 Siege aus den letzten 6** Spielen aller Wettbewerbe, und
   b) der **Gegner** ist nach Schritt 1 ausgeschieden (höchstens 1 Sieg in 6) **oder** in dieser
      Saison auf diesem Platz sieglos (als Heimteam daheim bzw. als Gastteam auswärts).
   Trifft das auf genau ein Team zu → **Heimsieg** bzw. **Auswärtssieg** dieses Teams.
   Trifft es auf keines oder auf beide zu → weiter mit Schritt 3.
   (So entstanden am 08.11. Sieg Brighton, Lorient, Nice, Villa, Freiburg, Hoffenheim.)
3. **Keine klare Seite →** das klarste **Tor-Signal** aus Rang 1–3:
   - ein Team trifft kaum (Sturm fehlt, seit Spielen ohne Tor, hoher Anteil ohne Tor) →
     **Beide treffen – Nein**
   - beide Teams treffen seit Wochen regelmäßig, Gegner selten zu null →
     **Beide treffen – Ja**
   - lange Serien mit vielen bzw. wenigen Toren, Torpotenzial →
     **Über 2,5** bzw. **Unter 2,5**
4. **Bedenken prüfen (Regel 7):** Spricht eine starke Bedenke (Rang 1–2) klar gegen den Tipp,
   geht es mit dem nächsten Schritt bzw. dem nächstklaren Markt weiter.

Am Ende steht genau einer der sechs erlaubten Märkte (Regel 5). In der Antwort wird genannt,
in welchem Schritt der Tipp entstanden ist.

## Regeln für den Tipp

1. **Ein Tipp je Spiel**, deutlich als „Tipp“ markiert, aus Rang 1–4 – ohne Prognosen.
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
8. Zahlen aus der Vorschau, die FootyStats oder Odd Alerts widersprechen, werden kurz vermerkt;
   widersprechen sich die Quellen, gilt die Zählung mit vollständigen Wettbewerben. Steht eine
   Vorschau-Angabe im Widerspruch zu sich selbst oder zu beiden APIs, wird sie nicht verwendet.

## Antwortaufbau je Spiel

1. Rang 1–2: Spielinformationen, aktuelle Form
2. Rang 3–4: Saison, Heim/Auswärts, Vorab-xG, Direktvergleiche (FootyStats, Odd Alerts, Vorschau)
3. ✅ **Tipp** mit Schritt (1–4), Gründen und Bedenken (stark/schwach)
4. Zum Vergleich: Prognose der Vorschau und Odd-Alerts-Modell (gleich oder abweichend)

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/forebet/JJJJ-MM-TT.md` (mit FootyStats-`match_id`,
Spalte „Vorschau“ = Forebet oder Odd Alerts, Spalte „Prognose (Vergleich)“) und werden dort nach
Abpfiff ausgewertet: Treffer je Tipp und Trefferquote, getrennt für Claudes Tipp und die
Prognose; keine Einheiten/Quoten.
Vorschauen möglichst vor Anpfiff; Tipps nach Anpfiff werden in der Liste vermerkt.
