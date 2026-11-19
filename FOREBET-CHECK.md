# Forebet-Check (System B) · Version 2.12

Vom Nutzer festgelegt am 07.11.2026 (Version 2), Rangfolge ergänzt am 08.11.2026 (Version 2.1)
nach der MLS-Auswertung; Forebet-Prognose aus der Tippfindung genommen am 08.11.2026 (Version 2.2); Märkte auf Sieg,
beide treffen und über/unter 2,5 begrenzt am 08.11.2026 (Version 2.3); fester Entscheidungsweg
Schritt 1–4 am 09.11.2026 (Version 2.4); Odd-Alerts-Vorschau als Ersatz für fehlende
Forebet-Vorschauen und Odd-Alerts-API als zweite Datenquelle am 09.11.2026 (Version 2.5); „klare Seite“ in Schritt 2 genau nach
den 6 neu gemachten Tipps vom 08.11. festgelegt am 09.11.2026 (Version 2.6); „stark“ nur noch, wenn wirklich
alles Relevante gegen den Tipp spricht, festgelegt am 14.11.2026 (Version 2.7); FootyStats einzige Datenquelle, Odd-Alerts-API gestrichen am
14.11.2026 (Version 2.8); Odd Alerts ganz gestrichen (auch die Vorschau), Auswertung je Wettart am
14.11.2026 (Version 2.9); Einstufung „klar“/„knapp“ je Tipp am 14.11.2026 (Version 2.10). Die Alternative je Spiel
(Version 2.11 vom 16.11.) am 17.11.2026 auf Wunsch des Nutzers wieder gestrichen: Es gilt Version 2.10
– Forebet-Vorschau + FootyStats, Einstufung klar/knapp so angewendet wie am 14.11.2026.
Version 2.12 am 19.11.2026 auf Wunsch des Nutzers (Rückkehr zur Arbeitsweise vom 08.11.):
Ausfälle bestimmen den Tipp mit, Motivation gehört zu Rang 1 (kein Sieg-Tipp für ein Team, für
das es um nichts mehr geht), „klar“ nur wenn Ausfälle, Form und Saison am Spielort in dieselbe
Richtung zeigen (gestützt durch die Datenanalyse `tipps/forebet/test-klar-datenanalyse.md`),
Prüfprotokoll je Tag. Ersetzt Version 1 (06.11.2026, Odd Alerts mit Quoten).
Eigener Branch; getrennt vom OddAlerts-System v1.3-OA und vom Spielcheck (System A).

## Grundsätze

1. **Keine Quoten.** Quoten, Quotenbewegungen, nötige Trefferquote, Vorteil/fair und
   Buchmacher werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Einzige Datenquelle ist FootyStats** (`https://api.football-data-api.com/`), seit Version 2.8.
   Odd Alerts wird überhaupt nicht mehr verwendet – weder API noch Vorschau (seit Version 2.9).
   Auch andere Seiten (z. B. Sports Mole) werden nicht verwendet.
   Keine Quotenfelder.
3. **Die Fakten aus der Forebet-Vorschau und der Forebet-Statistikseite und die Daten aus
   FootyStats** sind die Grundlage. Sie
   werden **nicht auf Übereinstimmung** geprüft, sondern nach der **Rangfolge** unten
   gewichtet; daraus macht Claude **einen eigenen Tipp**.
4. **Prognosen** – Forebet-Prognose
   (Wahrscheinlichkeit, erwartetes Ergebnis, Tipp wie „über 2,5“) – fließen **nicht** in den
   Tipp ein. Sie wird erst nach dem Tipp **zum Vergleich**
   genannt und in der Tagesliste mitgeführt, damit beide ausgewertet werden können.

## Eingang je Spiel: Forebet-Vorschau und Forebet-Statistikseite

Der Nutzer schickt je Spiel nur die Forebet-Vorschau (als PDF, Text oder Screenshot) – ohne die
Seite „Prediction / Stats / H2H“ (Wunsch des Nutzers vom 15.11.2026); die Zahlen kommen aus
FootyStats. Ohne Forebet-Vorschau wird kein Spiel bewertet. Die Abschnitte unterscheiden sich
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

## Rangfolge der Informationen

| Rang | Information | Quelle |
|---|---|---|
| 1 | Konkrete Spielinformationen: Ausfälle, Sperren, Aufstellung, Trainer, Torwart, Belastung (Europapokal), **Motivation** (geht es für das Team noch um etwas?) | Forebet-Vorschau |
| 2 | **Aktuelle Form:** letzte 6 Spiele, letzte 3 Heim- bzw. Auswärtsspiele, laufende Serien (Tore, ohne Tor, zu null) | Vorschau („Aktuelle Form“, „Haupttrends“) + Forebet-Statistikseite + FootyStats (letzte 6 aller Wettbewerbe, letzte 6 Ligaspiele, Trends) |
| 3 | Saisonwerte: Heim/Auswärts-Bilanz, Tore, xG, Tabelle, Vorab-xG und Torpotenzial | FootyStats + Vorschau („Gesamtbild in der Liga“) |
| 4 | Direktvergleiche und lange Trends (z. B. „16 der letzten 20“) | beide |
| – | Prognose: Forebet | nur Vergleich, kein Einfluss |

## Entscheidungsweg je Spiel (Schritt 1–4, immer in dieser Reihenfolge)

1. **Wer bekommt keinen Sieg-Tipp?** Jedes Team mit höchstens 1 Sieg aus den letzten 6
   Spielen aller Wettbewerbe scheidet für einen Sieg-Tipp aus (Regel 3). Ebenso jedes Team, für
   das es um nichts mehr geht – schon weiter, Gruppensieger, Meister oder abgestiegen
   (Regel 9, seit Version 2.12).
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
4. **Bedenken prüfen (Regel 7):** Gibt es eine starke Bedenke – spricht also wirklich alles
   Relevante gegen den Tipp –, geht es mit dem nächsten Schritt bzw. dem nächstklaren Markt weiter.

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
7. **Bedenken nach Stärke (seit Version 2.7):** **stark** nur, wenn wirklich alles Relevante gegen
   den Tipp spricht – Vorschau und FootyStats zeigen in dieselbe Richtung und es gibt
   keine gewichtige Gegenangabe aus Rang 1–2. Eine starke Bedenke spricht damit immer klar gegen
   den Tipp: Claude nimmt den nächststärkeren Markt (Schritt 4). Alles andere ist **schwach** und
   wird nur genannt. „Stark, aber nicht klar dagegen“ gibt es nicht mehr.
8. Zahlen aus der Vorschau, die FootyStats widersprechen, werden kurz vermerkt; es gilt die Zählung
   mit vollständigen Wettbewerben (FootyStats „letzte 6 aller Wettbewerbe“). Steht eine
   Vorschau-Angabe im Widerspruch zu sich selbst oder zu FootyStats, wird sie nicht verwendet.
9. **Ausfälle und Motivation bestimmen mit (seit Version 2.12, wie am 08.11.).** Ausfälle aus
   der Vorschau sind nicht nur Bedenken, sie geben die Richtung mit vor:
   - fehlt einem Team der Stürmer oder fehlen mehrere Angreifer → spricht für „Beide treffen –
     Nein“ und gegen einen Sieg-Tipp dieses Teams, für den Gegner;
   - fehlt einem Team die halbe Abwehr oder der Stammtorwart → spricht für Tore des Gegners und
     für dessen Sieg;
   - geht es für ein Team um nichts mehr → kein Sieg-Tipp für dieses Team (Schritt 1).
   Beispiele 08.11.: Angers ohne Stürmer → Sieg Nice; Celta ohne Stürmer → beide treffen – Nein;
   Le Havre ohne halbe Abwehr → Sieg Lorient.

## Antwortaufbau je Spiel

1. Rang 1–2: Spielinformationen, aktuelle Form
2. Rang 3–4: Saison, Heim/Auswärts, Vorab-xG, Direktvergleiche (FootyStats, Vorschau)
3. ✅ **Tipp** mit Schritt (1–4), Gründen und Bedenken (stark/schwach) und einer klaren
   **Einstufung (seit Version 2.12): klar**, wenn **Ausfälle/Motivation (Rang 1), Form (Rang 2)
   und Saison am Spielort (Rang 3: Heimteam daheim, Gastteam auswärts)** in Richtung des Tipps
   zeigen; **knapp**, wenn eine **gewichtige** Angabe aus einem dieser drei in die andere Richtung
   zeigt – mit einem Satz, warum. Saisonwerte am Spielort zählen ab 4 Spielen am Spielort; bei
   weniger (z. B. Nationalteams) entscheiden Rang 1–2 allein. Direktvergleiche (Rang 4) machen
   einen Tipp nicht knapp, werden aber immer genannt.
   Gewichtig ist eine Angabe, die den Kern des Tipps trifft – z. B. das Team, das laut Tipp nicht
   treffen soll, traf zuletzt regelmäßig; dem Favoriten fehlen mehrere Stammspieler oder der Grund
   zu gewinnen; ein Team, auf dessen Toren der Über-Tipp beruht, ist ohne seinen Stürmer.
   **Nicht gewichtig** (nur als schwache Bedenke nennen, Einstufung bleibt klar): fragliche
   Spieler, ein einzelnes Gegenbeispiel, Serien gegen andere, stärkere Gegner, die der Gegner im
   Spiel gar nicht nachmachen kann (Maßstab: Tagesliste 14.11.2026).
   Beim Saisonwert am Spielort ist gewichtig, was dem Tipp klar widerspricht (z. B. Unter 2,5,
   aber das Gastteam spielt auswärts meist über 2,5).
4. Zum Vergleich: Prognose der Vorschau (gleich oder abweichend)

**Darstellung der Tagesübersicht** (Wunsch des Nutzers): Tabelle mit Anstoß, Spiel und Tipp;
die Einstufung steht unter der Wettart (✅ klar, ⚠️ knapp); darunter je Spiel eine
Zeile mit der kurzen Begründung – auch bei klaren Tipps mit „schwach dagegen: …“, wenn etwas
dagegen spricht (auch Direktvergleiche). In der Auswertung steht richtig/falsch in eigenen Spalten.

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/forebet/JJJJ-MM-TT.md` (mit FootyStats-`match_id`,
Spalte „Prognose (Vergleich)“) und werden dort nach
Abpfiff ausgewertet: Treffer je Tipp und Trefferquote, getrennt für Claudes Tipp und die
Prognose, getrennt für klare/knappe Tipps, dazu **Treffer je Wettart** (Sieg, beide treffen Ja/Nein, über/unter 2,5) für den
Tag und seit Version 2.3 gesamt; keine Einheiten/Quoten. Bleibt „Beide treffen – Ja“ die
schwächste Wettart, schlägt Claude dem Nutzer vor, sie zu streichen.
Vorschauen möglichst vor Anpfiff; Tipps nach Anpfiff werden in der Liste vermerkt.

**Prüfprotokoll (seit Version 2.12, wie am 08.11.):** Vor dem Abschicken wird jeder Tipp in der
Tagesliste geprüft: erlaubter Markt (Regel 5) · Schritt 1 (Siege aus 6, Motivation) · Richtung
aus Rang 1–2 inkl. Ausfälle (Regel 2, 9) · Saison am Spielort · Forebet-Prognose nicht verwendet ·
starke Bedenken (Regel 7) · jede genannte Zahl gegen FootyStats.
