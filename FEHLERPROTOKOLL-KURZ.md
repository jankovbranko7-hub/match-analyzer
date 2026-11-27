# Fehlerprotokoll – Kurzfassung für Bearbeiter-Agenten (Hebel 2, Version 1.4, Wunsch des Nutzers vom 27.11.2026)

Die Bearbeiter-Agenten lesen statt des vollständigen `FEHLERPROTOKOLL.md` diese Kurzfassung (spart Limit). Claude und die
Prüfer lesen weiter die Vollfassung. Neue Fehler werden immer zuerst in `FEHLERPROTOKOLL.md` eingetragen; ergibt sich daraus eine
neue Lehre, kommt sie hier dazu (Stand: 27.11.2026).

## Fehlerarten (A–N) – beim Schreiben jede gezielt vermeiden

- **A · Liga und alle Wettbewerbe verwechselt** (häufigste): jede Zahl mit Bezug Liga/alle Wb. · gesamt/daheim/auswärts ·
  Team/Spiel. FS-Trends („seit X Spielen“) zählen nur die Liga. Zahlen aus `werkzeuge/datenblatt.py` übernehmen, nicht selbst zählen.
- **B · Gegenangaben unvollständig:** jede Teamnews-Liste und jeden Rang-2-Block gegen den Tipp lesen; fehlende/fragliche Angreifer
  beim Team, das treffen soll, immer nennen.
- **C · Sicherster Markt falsch abgewogen:** Rang 3 dreht Rang 1–2 nicht; jede Rang-1–2-Gegenangabe mit „dreht den Tipp: ja/nein,
  weil …“; **erst den ganzen Rang-2-Block gegen den Tipp lesen** – Spielort-Teilmengen der letzten 6 (2–3 Spiele) ersetzen ihn nicht.
- **D · „We say“** wird nicht verwendet.
- **E · Vermutung ohne Quelle:** keine Belastung ohne Spieldatum, kein „Derby“ ohne Quellenwort, keine Spielorte/Städte, die nicht
  in der Quelle stehen, kein „Torproblem“, „formstärkstes Team“, „Trainer stellt um“.
- **F · Teamnews-Status falsch gelesen:** nur nach Originalwort (fehlt/fraglich/gesperrt/zurück, sonst „unklar (Wortlaut: …)“);
  „could“, „may“, „likely“, „in contention“, „must vie“, „welcome back“, „unlikely to feature“ sind nicht sicher.
- **G · Fehler der Quelle übernommen:** SM-Artikelangaben (Tabellenplatz, Torjäger, „schlechteste Abwehr“, Serien) gegen
  SM-Tabelle, Spielseite und FS prüfen; SM-Spielseite zeigt nicht ausgetragene Spiele als 0:0.
- **H · Zahl falsch gelesen/gezählt:** „5 von 6“ statt „alle“; Formleisten-Richtung (Artikel alt → neu, Spielseite neu → alt).
- **I · Anteil Team/Spiel verwechselt:** „Team trifft in 80 %“ ≠ „in den Spielen treffen beide in 80 %“.
- **J · Lage-Check unvollständig:** Abstände nach oben, unten und zum Abstiegs-/Relegationsplatz; Trainer-Spielzahl, wenn nicht in
  der Quelle: „nicht in der Quelle“.
- **K · Entscheidungsweg nicht in der Reihenfolge:** Abschnitt genau in der Reihenfolge Schritt 1–8 (mit 4b); Spielbild je Team.
- **L · Direktvergleich (H2H):** nie – auch nicht in Widerlegungen und nicht über Pokalspiele gegen denselben Gegner.
- **M · Eigene Werkzeug- und Formfehler:** Uhrzeit immer mit `TZ=Europe/Berlin date` ablesen; volle Teamnamen.
- **N · Ablauf nicht nach System:** keine Abweichung ohne ausdrückliches Ja des Nutzers.

## Die wichtigsten Lehren aus den Einzelfällen (20.–27.11.)

1. **Regel 7c:** „neu“ nur, wer im letzten Pflichtspiel spielte (Startelf/eingewechselt) und jetzt fehlt/fraglich/gesperrt ist,
   oder wer fehlte und laut Quelle **klar** startet/spielt. **Ungenutzt auf der Bank ≠ fehlte** (Provod 25.11., Manning 27.11.).
   „Will welcome back from suspension“ + nur mögliche Startelf ≠ sicher (Vaessen/Hateboer 27.11.). Eine **unveränderte Elf** ist
   keine Änderung (Rizespor 27.11.). Letzte Einsätze immer über die Aufstellungen (das Werkzeug macht das), nie über das veraltete
   FS-Feld „letzter Einsatz“.
2. **Regel 7b:** Positionen aus den FS-Spielerdaten suchen – auch normalisiert (Sonderzeichen, andere Schreibweise: Mayor/Major,
   Šturm); erst dann „Position nicht in der Quelle – keine Richtung“.
3. **„Ohne Tor“ nie gegen Über/Unter 2,5 ohne Spielstände** – ein 0:3 liegt über 2,5 (viermal passiert).
4. **Unter 2,5:** feste Gegenangabe „Team mit mehrfach 3+ eigenen Toren in den letzten 6“ mit Spielständen; bei klarem Favoriten
   immer für den Favoriten nennen (Schritt 4b).
5. **Widerlegung mit Spielort-Werten:** Bezug „daheim“/„auswärts“ immer nennen; Heim-Zu-null-Spiele widerlegen keine
   Auswärts-Gegenangabe (Levante 23.11., Marítimo 27.11.).
6. **Tabellenplätze der Gegner sind Rang 3**, nicht Rang 2.
7. **Kennzeichnung:** Die Sports-Mole-Seite ist Rang 1 (Lage-Check, Teamnews) – nie mit Form oder Saisonwerten begründen;
   „beide einig“ nur, wenn auch die FS-Seite (Rang 2–3) zum Tipp zeigt.
8. **Europapokal:** Datenblatt-Feld 4 immer mit allen drei Rang-2-Blöcken (letzte 6 alle Wb., alle Spiele der Ligaphase, letzte 6
   der Heimliga); Spielertore ohne Qualifikation.
9. **Abweichung SM ↔ FS:** genau sagen, was welche Quelle belegt; als Grund nur, was beide gleich zeigen.
10. **Korrekturen immer im ganzen Abschnitt suchen und ersetzen**, nicht nur an der genannten Stelle (dreimal passiert).
11. **Version 1.4:** Kräfteverhältnis (4b) vor dem Spielbild; bei „klarer Favorit“ kein Beide treffen – Ja, Über 2,5 nur, wenn der
    Favorit allein mehrfach 3+ Tore schoss; Vorrang Sieg-Markt; „Spielen: ja“ nur bei „beide einig“.
    „Lage zeigt zu Team X“ = Lage-Fakten von X (Serien, keine neue Schwächung) sprechen für X und die des Gegners
    (Serien, neue Schwächung) gegen ihn; Dringlichkeit allein reicht nicht.
