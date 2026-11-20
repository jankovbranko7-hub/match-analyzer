# Forebet-Check (System B) · Version 3.1 – Spielbild

> Archiv: Version 3.1 (20.11.2026). Gilt nicht mehr – abgelöst durch den Sports-Mole-Check (`SPORTSMOLE-CHECK.md`).

Vom Nutzer festgelegt am 20.11.2026 als Hauptanalyse. Baut auf Version 2.10 auf (archiviert in
`archiv/FOREBET-CHECK-2.10.md`): Aus der **Sports-Mole-Vorschau** und **FootyStats** entsteht je Spiel
ein eigenes **Spielbild**; daraus **immer genau ein Tipp** je Spiel: der klare Markt (Einstufung
**klar**) oder, wenn keiner klar ist, der nächstbeste Markt (Einstufung **knapp**).
Version 3.0 (20.11.2026: kein Tipp ohne klaren Markt) am selben Tag auf Wunsch des Nutzers zu
Version 3.1 geändert: Gegenangabe aus Rang 1–2 → nächster Markt wird getippt, immer ein Tipp
(wie in Version 2.3/2.10). Forebet wird nicht mehr verwendet (Wunsch des Nutzers vom
20.11.2026); der Name „Forebet-Check“ bleibt nur als Name des Systems.
Versionsgeschichte bis 2.10 siehe Archiv. Eigener Branch; getrennt vom OddAlerts-System v1.3-OA und
vom Spielcheck (System A).

## Grundsätze

1. **Keine Quoten.** Quoten, Quotenbewegungen, nötige Trefferquote, Vorteil/fair und
   Buchmacher werden weder abgerufen noch genannt noch als Begründung verwendet.
2. **Datenquellen – nur diese zwei:** Vorschau von **Sports Mole** und Zahlen aus **FootyStats**
   (`https://api.football-data-api.com/`). Forebet und Odd Alerts werden nicht verwendet – weder
   Vorschau noch Prognose noch Statistikseite. Keine Quotenfelder.
3. Die Fakten aus der Vorschau und die Daten aus FootyStats werden nach der **Rangfolge** unten
   gewichtet; daraus macht Claude ein **eigenes Spielbild** und daraus höchstens **einen Tipp**.
4. **Prognosen** – „We say“ von Sports Mole – fließen **nicht** in Spielbild und Tipp ein. Sie werden erst
   danach **zum Vergleich** genannt und in der Tagesliste mitgeführt.

## Eingang je Spiel

Der Nutzer schickt je Spiel die **Sports-Mole-Vorschau** (PDF, Text oder Screenshot). Verwendet wird
alles, was vorhanden ist: Team News (Ausfälle, Sperren, Rückkehrer), mögliche Aufstellungen,
Formleiste, Trainer, Ausgangslage. Ausfälle, Sperren, Trainerwechsel und Aufstellungen aus der
Vorschau gelten als gesetzt.

Der Nutzer schickt nur Spiele, für die es eine Sports-Mole-Vorschau gibt. Ohne Sports-Mole-Vorschau
wird kein Spiel bewertet; es gibt keinen Ersatz.

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
| 1 | Konkrete Spielinformationen: Ausfälle, Sperren, Aufstellung, Trainer, Torwart, Belastung (Europapokal), Ausgangslage | Sports-Mole-Vorschau |
| 2 | **Aktuelle Form:** letzte 6 Spiele, letzte 3 Heim- bzw. Auswärtsspiele, laufende Serien (Tore, ohne Tor, zu null) | FootyStats (letzte 6 aller Wettbewerbe, letzte 6 Ligaspiele, Trends) + Formleiste der Vorschau |
| 3 | Saisonwerte: Heim/Auswärts-Bilanz, Tore, xG, Tabelle, Vorab-xG und Torpotenzial | FootyStats |
| 4 | Direktvergleiche und lange Trends | FootyStats + Vorschau |
| – | Prognose: „We say“ von Sports Mole | nur Vergleich, kein Einfluss |

## Entscheidungsweg je Spiel (Schritt 1–4, immer in dieser Reihenfolge)

1. **Wer bekommt keinen Sieg-Tipp?** Jedes Team mit **höchstens 1 Sieg aus den letzten 6** Spielen
   aller Wettbewerbe scheidet für einen Sieg-Tipp aus (Regel 3) – auch wenn das Spielbild anders
   aussieht.
2. **Spielbild:** In 3–4 Sätzen, wie das Spiel voraussichtlich läuft:
   - Wer bestimmt das Spiel, wer kommt zu Chancen?
   - Trifft jedes der beiden Teams – oder kaum?
   - Wird es offen (viele Tore) oder zäh (wenige Tore)?
   - Was ändern Ausfälle, Sperren, Trainerwechsel, Ausgangslage?
   Jeder Satz wird mit konkreten Angaben aus Rang 1–2 belegt; Rang 3–4 ergänzen nur.
3. **Die sechs Märkte prüfen:** Für jeden der sechs erlaubten Märkte (Regel 5) kurz: passt er zum
   Spielbild? Ein Markt ist **klar**, wenn alle Angaben aus Rang 1–2 zu ihm passen und es keine
   gewichtige Gegenangabe aus Rang 1–2 gibt (Maßstab: die Tagesliste vom 14.11.2026 – Kleinigkeiten
   machen einen Markt nicht unklar, sie werden als schwache Bedenke genannt). Ein Sieg-Markt kann nur
   klar sein, wenn das Team nach Schritt 1 nicht ausgeschieden ist.
4. **Tipp:**
   - genau ein klarer Markt → das ist der **Tipp**;
   - mehrere klare Märkte → der Markt, den die Daten am stärksten tragen (mit einem Satz, warum);
   - **kein klarer Markt → der nächstbeste Markt** wird getippt: der Markt, gegen den am wenigsten
     spricht (nach Rangfolge gewichtet), mit Einstufung **knapp** und einem Satz, welche
     gewichtige Gegenangabe aus Rang 1–2 dagegen spricht. Es gibt immer genau einen Tipp.

## Regeln für den Tipp

1. **Genau ein Tipp je Spiel**, deutlich als „Tipp“ markiert, aus Rang 1–4 – ohne Prognosen.
2. **Richtung aus Rang 1–2.** Rang 3 und 4 ergänzen das Spielbild und drehen eine klare Richtung
   aus Rang 1–2 nicht um.
3. **Form vor Saison:** Ein Team mit **höchstens 1 Sieg aus den letzten 6** bekommt **keinen
   Sieg-Tipp**, auch als Heimteam oder Tabellenfavorit.
4. **Kein Kompromiss-Markt** nur weil Informationen sich widersprechen; gewählt wird der Markt,
   den die Daten am klarsten tragen (auch beim knappen Tipp).
5. **Erlaubte Märkte – nur diese sechs:** Heimsieg, Auswärtssieg, Beide treffen – Ja,
   Beide treffen – Nein, Über 2,5 Tore, Unter 2,5 Tore. **Keine anderen Wettarten** (keine
   Doppelte Chance, kein Remis, kein „Team trifft“, keine anderen Torlinien wie 1,5 oder 3,5).
6. Keine Schwellen, keine Spielcheck-Zählung („x von 10“).
7. **Bedenken und Einstufung:** Eine gewichtige Gegenangabe aus Rang 1–2 macht einen Markt unklar
   (Schritt 3); wird er trotzdem als nächstbester Markt getippt, ist der Tipp **knapp** und die
   Gegenangabe wird genannt. Kleinigkeiten sind schwache Bedenken und ändern die Einstufung nicht.
8. Zahlen aus der Vorschau, die FootyStats widersprechen, werden kurz vermerkt; es gilt die Zählung
   mit vollständigen Wettbewerben (FootyStats „letzte 6 aller Wettbewerbe“). Steht eine
   Vorschau-Angabe im Widerspruch zu sich selbst oder zu FootyStats, wird sie nicht verwendet.

## Antwortaufbau je Spiel

1. Rang 1–2: Spielinformationen (Sports Mole), aktuelle Form (FootyStats)
2. Rang 3–4: Saison, Heim/Auswärts, Vorab-xG, Direktvergleiche
3. **Spielbild** (3–4 Sätze mit Belegen)
4. Die sechs Märkte: je eine Zeile „klar“ oder „nicht klar – weil …“
5. ✅ **Tipp** mit Gründen, Bedenken und Einstufung **klar** oder **knapp** (bei knapp: welche
   Gegenangabe aus Rang 1–2 dagegen spricht)
6. Zum Vergleich: „We say“ von Sports Mole (gleich oder abweichend)

## Tagesliste

Alle Spiele eines Tages kommen nach `tipps/forebet/JJJJ-MM-TT.md` (mit FootyStats-`match_id`,
Tipp, Einstufung klar/knapp, Spalte „Prognose (Vergleich)“)
und werden dort nach Abpfiff ausgewertet: Treffer je Tipp und Trefferquote, **getrennt nach klar und knapp**,
getrennt für Claudes Tipp und die Prognose, dazu **Treffer je Wettart** (Sieg, beide treffen Ja/Nein,
über/unter 2,5) für den Tag und gesamt seit Version 3.0 (die Tipps nach 3.0 zählen als „klar“); keine Einheiten/Quoten.
Vorschauen möglichst vor Anpfiff; Tipps nach Anpfiff werden in der Liste vermerkt.
