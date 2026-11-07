# Forebet-Check (System B · Arbeitsweise, nicht Teil des Systems)

Eigenes Prüfverfahren des Nutzers, vereinbart am 06.11.2026. Getrennt vom OddAlerts-System
v1.3-OA und vom Spielcheck (System A, `SPIELCHECK.md`); die Verfahren werden nicht vermischt.

## Auslöser

Der Nutzer fügt eine **Forebet-Vorschau** zu einem Spiel ein (Text oder Screenshot). Forebet ist
für Claude nicht erreichbar (Cloudflare, HTTP 403), deshalb kommt die Vorschau immer vom Nutzer.

## Was Claude selbst per API holt (Schlüssel `ODDALERTS_KEY`, nie ausgeben)

- Spiel finden: `fixtures/upcoming?competitions=<id>` (Anstoß, Tabellenplatz)
- Saison- und Formdaten: `fixtures/between` (Liga + Pokal, ohne Testspiele), Heim-/Auswärtsbilanz,
  Direktvergleiche
- Odd-Alerts-Modell: `trends/btts` (paginiert, Feld `probability`)
- Quoten: `odds/history/<id>` (Öffnung → aktuell, Pinnacle und Bet365, beste Quote)

## Regeln

1. **Stärkstes Signal:** Claude nennt **einen** Tipp — das stärkste Signal aus Daten, Spielbild
   und Form — deutlich als „Tipp“ markiert, mit Quote und nötiger Trefferquote (1 / Quote).
2. **Keine Schwellen:** keine 7-von-10-Grenze, keine Value-Mindestgrenze, keine Pflicht zur
   Übereinstimmung der Quellen.
3. **Keine Spielcheck-Zählung** (letzte 5 je Team, „x von 10“): wird weder gezeigt noch als
   Begründung verwendet.
4. Forebet und das Odd-Alerts-Modell müssen nicht übereinstimmen. Weichen sie ab, wägt Claude
   selbst ab, welche Seite die Daten (Saison, Heim/Auswärts, Form, Direktvergleiche), das
   Spielbild und die Form besser stützen. Der Tipp ist Claudes begründete Einschätzung.
5. **Ausfälle, Sperren, Aufstellungen** aus der Vorschau gelten als gesetzt (API hat sie nicht).
6. Angaben der Vorschau werden gegen die API geprüft; falsche Angaben werden benannt.
7. Quote und Quotenbewegung (inkl. Pinnacle ohne Marge) werden genannt.
8. **Warnungen nach Stärke ordnen** (vereinbart am 07.11.2026 nach der Auswertung vom 06.11.):
   - **Stark** = konkrete Information zu genau diesem Spiel: Systemumstellung, Trainerwechsel,
     Ausfälle, eine deutliche Quotenbewegung gegen den Tipp.
   - **Schwach** = allgemeine Statistik aus der Vergangenheit (Saisonquote, Direktvergleiche).
   - Spricht eine **starke** Warnung klar gegen den Tipp, nimmt Claude den nächststärkeren Markt,
     gegen den keine starke Warnung spricht. Statistik aus der Vergangenheit überstimmt keine
     konkrete Spielinformation.
   - Bedenken werden als „stark“ oder „schwach“ gekennzeichnet.
9. **Preis offen benennen:** Bei jedem Tipp steht, ob die Quote einen **Vorteil** bietet (Modell
   **und** Pinnacle ohne Marge über der nötigen Trefferquote) oder nur **fair** ist. Keine Schwelle:
   die Entscheidung, ob gespielt wird, bleibt beim Nutzer.

## Antwortaufbau je Spiel

1. Forebet-Vorschau gegen die API (stimmt / falsch / nicht prüfbar)
2. Daten (Saison, Heim/Auswärts, Direktvergleiche)
3. Modell und Markt (Forebet · Odd-Alerts-Modell · Pinnacle ohne Marge, Quotenbewegung)
4. ✅ **Tipp** mit Quote, Preis (Vorteil oder fair), Gründen und Bedenken (stark/schwach) —
   Einzelwette, keine Kombi, keine Garantie

## Tagesliste

Alle Tipps eines Tages kommen nach `tipps/forebet/JJJJ-MM-TT.md` und werden dort nach Abpfiff
ausgewertet. Getrennt von `tipps/spielcheck/` (System A).
