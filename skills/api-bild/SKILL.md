---
name: api-bild
description: "Read a FootyStats match twice and name one tip from pre-match xG and BTTS, over, under potentials. Use when the user sends football fixtures and wants an API picture tip, not the 70/30 model."
type: tool
lifecycle: active
---

# API-Bild — ein Tipp aus den FootyStats-Feldern

Kein 70/30, kein Dixon-Coles, keine Schwelle. Der Tipp benennt das höchste gelesene Potential.

## Ablauf

1. Key aus `FOOTYSTATS_KEY` lesen. Fehlt er, stoppen.
2. Paarung über `todays-matches` der genannten Datumszahl finden. Der API-Name muss der angefragte Name sein. Ein ähnlicher Verein ist das falsche Spiel.
3. `python3 scripts/api_bild.py MATCH_ID` ausführen. Das Skript liest `/match` zweimal.
4. Stimmen die zwei Antworten nicht überein, keinen Tipp ausgeben. Den Fehler hinschreiben.
5. Jedes Feld im Chat zeigen. Ein fehlendes Feld heißt `fehlt` und wird nie geschätzt.
6. Der Tipp des Skripts ist der Tipp. Nicht daneben rechnen.

## Felder

`team_a_xg_prematch`, `team_b_xg_prematch`, `btts_potential`, `o25_potential`, `u25_potential`.

Sind BTTS, Over und Under gleich hoch, benennt das höhere Pre-Match-xG Heimsieg oder Auswärtssieg. Sonst benennt das höchste Potential BTTS Ja, Over 2.5 oder Under 2.5.

## Ausgabe

```
Team – Team, Liga
API: xG Heim, xG Gast, BTTS, Over, Under
Prüfung: übereinstimmend oder kein Tipp
Tipp: ein Markt
```

## Nicht tun

Die Datei match-analyzer-modell-v2 nicht laden. Keine Quote in den Tipp mischen. Keinen zweiten Markt nennen.
