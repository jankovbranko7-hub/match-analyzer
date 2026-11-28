# Vorlage · Abschnitt einer Paarung in der Tagesliste (Sports-Mole-Check 1.5)

Eingerichtet am 28.11.2026. Jeder Bearbeiter schreibt seinen Abschnitt **genau in diesem Aufbau** (Reihenfolge = Entscheidungsweg
1–8 in `SPORTSMOLE-CHECK.md`). Die Ausführlichkeit richtet sich nach den Abschnitten der letzten Tagesliste; die Punkte 4b, 8 und
die Merkmale 10–12 stehen so da wie hier. In `<…>` steht, was einzutragen ist. Musterfälle für die festen Sätze: `MUSTERFAELLE.md`.

```
## <Nr.> · <Anstoß> · <Heim> – <Gast>            (bei Grenzfall: „(Grenzfall)“ auch in der Überschrift)

- **Schritt 1 – Abrufen:** <SM-Vorschau mit Stand, gehört zu diesem Termin; vier SM-Teile vorhanden; Anstoß SM = FS, match_id;
  welche Werkzeuge mit Uhrzeit (`TZ=Europe/Berlin date`); was nicht verwendet wurde (H2H-Sätze, Datenanalyse, Quoten, „We say“)>
- **Zweitquelle Teamnews (`teamnews2.py`, Uhrzeit):** <welche Länderquelle, Team dort gefunden; je Team: bestätigt / nur Sports Mole /
  nur Länderquelle; oder „nicht verfügbar“ mit Grund>
- **Schritt 2 – Abgleich:** <Ergebnis `abgleich.py`; aus `datenblatt.py` jede Zeile „Abweichungen SM ↔ FS“ und „Hinweise zur
  Zuordnung“ – geklärt oder „nicht klärbar“>
- **Schritt 3 – Datenblatt <Heim>**
  1. Tabelle: <aus dem Werkzeug wörtlich; mit SM-Tabelle abgeglichen; Abstände>
  2. Letzte Spiele: <SM-Formdaten mit Wettbewerb; FS letzte 6 Liga mit Datum>
  3. Letzter Sieg, letztes Tor, Serien: <aus dem Werkzeug, mit Bezug Liga / alle Wb.>
  4. Zahlen mit Bezug: <Blöcke aus dem Werkzeug wörtlich: letzte 6 alle Wb., letzte 6 Liga, daheim/auswärts Saison; Europapokal:
     alle drei Rang-2-Blöcke>
  5. Teamnews nach Originalwort: <fehlt / fraglich / gesperrt / zurück, je Spieler mit englischem Wortlaut, Position mit Quelle
     oder „Position nicht in der Quelle“, Einsatz im letzten Pflichtspiel und „neu“ / „nicht neu – keine Richtung“ (Regel 7c),
     Zweitquelle: „bestätigt (<Länderquelle>: Statuswort im Original, seit wann)“ / „nicht bestätigt – nur Sports Mole“ (Regel 7e);
     eigene Liste „nur <Länderquelle>“ mit Statuswort, seit wann, Position, Einsatz im letzten Pflichtspiel; oder „Zweitquelle
     nicht verfügbar – nur Sports Mole“>
  6. Abweichungen: <aus Schritt 2>
  7. Weitere Fakten: <Trainer, Spiele davor/danach mit Datum, Besonderheit – je mit Quelle oder „nicht in der Quelle“>
- **Schritt 3 – Datenblatt <Gast>** <wie oben>
- **Schritt 4 – Lage <Heim>:** (1) <worum es geht> (2) <Dringlichkeit> (3) <Serien> (4) <Schwächung> (5) <Besonderheit>
- **Schritt 4 – Lage <Gast>:** (1) … (5)
- **Schritt 4b – Kräfteverhältnis:**
  - (a) Tabelle zeigt zu: <Heim / Gast / keinem> – weil <Platz, Punkte je Spiel, Abstand>
  - (b) Letzte 6 alle Wb. zeigt zu: <Heim / Gast / keinem> – weil <S-U-N, Tore beider>
  - (c) Letzte 6 Liga zeigt zu: <Heim / Gast / keinem> – weil <S-U-N, Tore beider>
  - (d) Gegnerstärke zeigt zu: <Heim / Gast / keinem> – weil <Ergebnisse gegen obere/untere Hälfte beider>
  - Spielort zeigt zu: <Heim / Gast / keinem> – weil <Heim daheim, Gast auswärts>
  - **Einstufung: <klarer Favorit: Team / ausgeglichen / nicht eindeutig>** <bei klarem Favoriten: 3+ eigene Tore des Favoriten
    mit Spielständen; Spiele gegen unterklassige Pokalgegner: „zählt hier nicht“>
- **Schritt 5 – Spielbild <Heim>:** trifft es? <…> · kassiert es? <…> · gewinnt es? <…>
- **Schritt 5 – Spielbild <Gast>:** trifft es? <…> · kassiert es? <…> · gewinnt es? <…>
- **Spielbild gesamt:** <…>
- **Schritt 6 – Die sechs Märkte** (je Rang 1–2 dafür/dagegen, dann Rang 3; bei klarem Favoriten „nicht erlaubt (4b)“ dazuschreiben):
  - Heimsieg: <…>
  - Auswärtssieg: <…>
  - Beide treffen – Ja: <…>
  - Beide treffen – Nein: <…>
  - Über 2,5: <…>
  - Unter 2,5: <… mit fester Gegenangabe „mehrfach 3+ eigene Tore“ und Spielständen>
- ✅ **Schritt 7 – Tipp: <Markt>.** <Vorrang Sieg-Markt geprüft: ja/nein, weil …> Gründe: <…> Warum nicht die anderen: <…>
  Gegenangaben (Rang 1–2) mit Gegenangaben-Prüfung:
  - <Gegenangabe> → **dreht den Tipp: ja/nein**, weil <…>
- **Schritt 8 – Kennzeichnung: <beide einig / geteilt>.**
  - Teamnews-Seite (Rang 1 – Lage, Teamnews aus Sports Mole + Länderquelle) zeigt: <zum Tipp / woandershin (wohin) / nicht
    eindeutig> – weil <… nur bestätigte Angaben; nicht bestätigte Angabe gegen den Tipp → „nicht eindeutig“>
  - FS-Seite (Rang 2–3 – Form, Spielort, Saison) zeigt: <zum Tipp / woandershin (wohin) / nicht eindeutig> – weil <…>
  - **Spielen: <ja / nein – nur Beobachtung / nein – Teamnews nicht bestätigt>**
- **Merkmale:** (1) <Wettart> · (2) <beide einig / geteilt>, <geändert / nicht geändert> · (3) Grenzfall: <ja (welcher Markt
  fast gleich stark) / nein> · (4) Tipp geändert: <ja (ursprünglicher Markt) / nein> · (5) neue Rang-1-Gegenangabe: <ja (wer) / nein> ·
  (6) Rang-2-Blöcke einig: <ja / nein (welcher nicht)> · (7) gegensätzliche Profile: <ja / nein> · (8) Datenlage vollständig:
  <ja / nein (was fehlt)> · (9) zweitbester Markt: <Markt> · (10) Kräfteverhältnis: <klarer Favorit (Team) / ausgeglichen / nicht
  eindeutig>; Tabellenhöher: <Heim / Gast> · (11) Spielen: <ja / nein> · (12) Schattentipp: <Markt> – <gleich / anders wegen
  4b-Ausschluss / anders wegen Vorrang Sieg-Markt> · (14) Zweitquelle: <bestätigt / weicht ab (wer, was) – Rang 1 betroffen:
  ja/nein / nicht verfügbar> · (15) Ohne Zweitquelle: Tipp <Markt>, Spielen <ja/nein> – <gleich / anders>
- Kontrolldurchgang (Bearbeiter, <Uhrzeit> `date`): <was gegen welche Quelle geprüft wurde, Fehlerarten A–N, korrigierte Fehler>
```

Tabellenzeile im Kopf der Tagesliste (Spalten seit 1.4.1):

```
| Nr. | Anstoß | Spiel | Liga | match_id | Tipp | Kennzeichnung | Spielen | Ergebnis |
|---|---|---|---|---|---|---|---|---|
| 1a | 20:30 | <Heim> – <Gast> | <Liga> (<FS-Saison>) | <match_id> | **<Markt>** (Grenzfall; bis <Uhrzeit> <ursprünglicher Markt>) | beide einig | ja | |
```

Merkmal **(13) Vorprüfung** trägt nicht der Bearbeiter ein, sondern Claude nach der Kontrolle (vor Merkmal 14 einfügen):
„· (13) Vorprüfung: ja – Zahlen zeigten zu: <Heimsieg / Auswärtssieg / Tor-Markt / keinem>“ oder „· (13) Vorprüfung: nein“.

Märkte immer mit ihren festen Namen: Heimsieg, Auswärtssieg, Beide treffen – Ja, Beide treffen – Nein, Über 2,5, Unter 2,5
(`werkzeuge/tippanalyse.py` liest genau diese Wörter).
