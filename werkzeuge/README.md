# Werkzeuge (FootyStats-System v1.4)

Das sind die Rechenwerkzeuge, mit denen die Vorabeinträge und Auswertungen in `protokoll/` erstellt werden. Sie gehören nicht zum Regelwerk: maßgeblich ist `FootyStats-System-v1.4.txt`. Den API-Schlüssel enthalten sie nicht. Er kommt aus der Umgebung (`FOOTYSTATS_KEY="$APIKEY"`).

## Arbeitsordner

Die Skripte arbeiten relativ zu einem Arbeitsordner außerhalb des Repositorys. Cache, Modelle und Zwischenstände dürfen nicht ins Repository.

```
W=<Arbeitsordner>; mkdir -p $W/tools $W/cache
cp werkzeuge/*.py $W/tools/; cp werkzeuge/seasons.json $W/
cd $W/tools
```

Python mit `numpy` und `scipy`. Aufrufe immer mit `python3 -I`.

## Ablauf pro Spieltag (TAG z. B. `1106`, DAY z. B. `2026-11-06`)

1. **Spielplan:** `fs.get('todays-matches', nocache=True, date=DAY, timezone='UTC')` aufrufen und die Match-IDs der Batches zuordnen. Begegnungen, die dort fehlen, gelten als Identität ungeklärt (Abschnitt 2).
2. **`../batches_TAG.json`** anlegen: `{"batches": [[match_id oder null, ...], ...], "nat": [Saison-IDs der Landesligen für Europapokal-Teams], "missing": {"2.2": ["Heim", "Gast"]}}`.
3. **Ligadaten:** `league-matches` für die laufende Saison mit `nocache=True` und bis zu drei Vorsaisons laden (siehe `fetch_matches.py`). Den Stichtag als Unix-Zeit nach `../tdec_TAG` schreiben, die Startzeit als ISO-Präfix nach `../tdec_TAG_startiso`.
4. **Modelle:** `python3 -I model14.py <tdec> <Saison-IDs …>` schreibt `../models.json`. Dann `cp ../models.json ../models_TAG.json`.
5. **Tabellen:** `python3 -I build14.py DAY TAG` erzeugt `../matches_TAG.json` und gibt eine Übersicht aus.
6. **Bewertung:** Das Bild, die Auswahl und ⚠️ je Spiel kommen in `../decisions_TAG.py` als `D = {"1.1": (Auswahl, Bild-Satz, Warnung oder None), …}`. Das ist die sportliche Entscheidung nach den Abschnitten 4, 6 und 7 und wird nicht automatisch erzeugt.
7. **Vorabeintrag:** `python3 -I -c "import sys; sys.path.insert(0,'..'); sys.argv=['x',DAY,TAG,'<repo>/protokoll/DAY']; exec(open('report14.py').read())"`. Anschließend den Rohdaten-Snapshot als `rohdaten.tar.xz` beilegen, committen und pushen, und zwar vor dem Anstoß.
8. **Ergebnisprüfung** am Folgetag:
   - `python3 -I results14.py <repo>/protokoll/DAY TAG`
   - `python3 -I evaluate14.py <repo>/protokoll/DAY TAG`
   - `python3 -I write_eval.py DAY TAG <ISO-Präfix des Abrufs> <frühere Tage, kommagetrennt>`

## Rückblick-Test

`backtest.py`, `backtest_xg.py` und `bt_report.py` erzeugen den Prüfstand aus `protokoll/analysen/2026-11-05-rueckblicktest.md`.

## Hinweise

- Ein HTTP 417 mit `request_limit: null` bedeutet, dass die Liga nicht im Abo ist (`LookupError`). Ein anderer 417 ist das Stundenlimit.
- K.-o.- und Play-off-Runden, also Runden, in denen alle Spiele Spieltag 0 haben, werden in Training und Tabellen ausgeschlossen.
