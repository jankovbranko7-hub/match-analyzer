"""Spiel-IDs aus Paarungen finden - ohne Liga, nur Namen und Datum.

    python3 analyse/finde.py 2026-10-02 "CD Eldense - Real Oviedo" "Helmond - Heracles"
    python3 analyse/finde.py 2026-10-02 --liste          # alle Spiele des Tages zeigen

Der Nutzer schickt Paarung und Datum, keine Liga - die steht in den Spieldaten selbst
(`competition_id`). Dieses Skript loest die Namen auf und erledigt dabei Durchgang 0 aus
CLAUDE.md, Punkte 1, 3 und 4.

WARUM ES DAS GIBT: Ein Namensvergleich greift daneben. Am 30.09.2026 landete
"Atletico El Vigia" auf "Atletico Avila" (CLAUDE.md, "Keine Zahl von Hand in die Rangliste").
Dieses Skript macht drei Dinge dagegen:

  1. BEIDE Namen muessen passen, nicht einer. Ein Treffer auf nur einer Seite zaehlt nicht.
  2. Bleiben mehrere Spiele uebrig, wird NICHT gewaehlt, sondern "MEHRDEUTIG" gemeldet.
  3. Wird nichts gefunden, steht da "NICHT GEFUNDEN" - nie ein geratenes Spiel.

Dazu, weil es sonst jedes Mal von Hand passieren muss:
  - Anstoss gegen die Uhr (Durchgang 0, Punkt 1): angepfiffene Spiele werden markiert.
  - Abgleich mit bilanz.json (Punkt 3): schon festgehaltene Spiele werden markiert.
  - Der Tag ist nicht UTC-genau (Sollbruchstelle 21): findet sich eine Paarung am
    genannten Tag nicht, wird der Vor- und der Folgetag mitgesucht.
"""
import argparse, json, os, sys, time, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modell as M

# Vereinszusaetze, die beim Vergleich wegfallen. Keine Namensbestandteile, die ein Team
# von einem anderen unterscheiden - "II", "B", "Women" bleiben drin, die trennen Mannschaften.
RAUSCH = {'fc', 'cf', 'sc', 'afc', 'ac', 'sv', 'tsv', 'vfl', 'vfb', 'cd', 'ca', 'cs', 'as',
          'ss', 'ssc', 'us', 'club', 'calcio', 'athletic', 'atletico', 'deportivo', 'real',
          'city', 'town', 'united', 'fk', 'nk', 'hk', 'if', 'if,', 'bk', 'ik', 'sk', 'mfk',
          'ofk', 'rc', 'rcd', 'ud', 'sd', 'ce', 'ec', 'se', 'sf', 'spvgg', 'bsc', 'msv'}


def norm(s):
    """Kleinschreibung, ohne Akzente, ohne Satzzeichen."""
    s = unicodedata.normalize('NFKD', s or '')
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return ' '.join(''.join(c if c.isalnum() or c.isspace() else ' ' for c in s).split())


def kern(s):
    """Normiert und ohne Vereinszusaetze - aber nie leer."""
    t = [w for w in norm(s).split() if w not in RAUSCH]
    return ' '.join(t) if t else norm(s)


def passt(frage, name):
    """Passt der gesuchte Name auf diesen Teamnamen?"""
    f, n = kern(frage), kern(name)
    if not f or not n:
        return False
    if f == n:
        return True
    fs, ns = set(f.split()), set(n.split())
    # Alle Woerter der Frage kommen im Namen vor (oder umgekehrt) - "Helmond" auf
    # "Helmond Sport", aber nicht "Atletico El Vigia" auf "Atletico Avila", weil dort
    # "el" und "vigia" fehlen.
    return fs <= ns or ns <= fs


def trenne(paarung):
    for t in (' - ', ' – ', ' — ', ' vs ', ' vs. ', ' gegen ', ' : ', '-'):
        if t in paarung:
            a, _, b = paarung.partition(t)
            if a.strip() and b.strip():
                return a.strip(), b.strip()
    return None


def tag(datum, args):
    return M.hole("todays-matches", {"date": datum}, f"tag_{datum}.json", args)['data']


def nachbartage(datum):
    import datetime
    d = datetime.date.fromisoformat(datum)
    return [(d - datetime.timedelta(days=1)).isoformat(), (d + datetime.timedelta(days=1)).isoformat()]


def bilanz_ids():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bilanz.json')
    if not os.path.exists(p):
        return set()
    with open(p) as f:
        return {e['id'] for e in json.load(f)}


def suche(spiele, heim, ausw):
    """Spiele, bei denen BEIDE Namen passen. Auch in getauschter Reihenfolge."""
    treffer = [m for m in spiele if passt(heim, m['home_name']) and passt(ausw, m['away_name'])]
    if treffer:
        return treffer, False
    getauscht = [m for m in spiele if passt(ausw, m['home_name']) and passt(heim, m['away_name'])]
    return getauscht, bool(getauscht)


def huerden(m, jetzt, drin):
    """Gruende, dieses Spiel NICHT zu rechnen. Leer heisst: Prognose moeglich."""
    h = []
    if m['date_unix'] <= jetzt or m['status'] == 'complete':
        h.append('SCHON ANGEPFIFFEN - keine Prognose')
    if m['id'] in drin:
        h.append('steht schon in bilanz.json')
    if m['competition_id'] == 16808 or 'nations' in norm(m.get('competition_name', '')):
        h.append('Laenderspiel - wird nicht getippt')
    return h


def zeige(m, jetzt, drin):
    import datetime
    t = datetime.datetime.utcfromtimestamp(m['date_unix']).strftime('%d.%m. %H:%M UTC')
    h = huerden(m, jetzt, drin)
    return (f"  {m['id']}  {t}  Liga {m['competition_id']}  "
            f"{m['home_name']} - {m['away_name']}" + ("   [" + '; '.join(h) + "]" if h else ""))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Spiel-IDs aus Paarungen finden")
    ap.add_argument("datum", help="YYYY-MM-DD")
    ap.add_argument("paarungen", nargs="*", help='je Spiel "Heim - Auswaerts"')
    ap.add_argument("--liste", action="store_true", help="alle Spiele des Tages zeigen")
    ap.add_argument("--neu", action="store_true")
    ap.add_argument("--daten", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "daten"))
    args = ap.parse_args()

    jetzt = time.time()
    drin = bilanz_ids()
    spiele = tag(args.datum, args)
    print(f"{len(spiele)} Spiele am {args.datum}. Jetzt ist "
          f"{time.strftime('%d.%m. %H:%M UTC', time.gmtime(jetzt))}.\n")

    if args.liste or not args.paarungen:
        for m in sorted(spiele, key=lambda x: x['date_unix']):
            print(zeige(m, jetzt, drin))
        sys.exit()

    ids = []
    for p in args.paarungen:
        tz = trenne(p)
        print(f"{p}")
        if not tz:
            print('  NICHT LESBAR - bitte als "Heim - Auswaerts" schreiben\n'); continue
        heim, ausw = tz
        treffer, getauscht = suche(spiele, heim, ausw)
        quelle = args.datum
        if not treffer:
            for d2 in nachbartage(args.datum):
                try:
                    treffer, getauscht = suche(tag(d2, args), heim, ausw)
                except Exception as e:
                    print(f"  ({d2} nicht abrufbar: {type(e).__name__})"); continue
                if treffer:
                    quelle = d2; break
        if not treffer:
            print("  NICHT GEFUNDEN - Schreibweise pruefen oder anderes Datum\n"); continue
        if len(treffer) > 1:
            print(f"  MEHRDEUTIG, {len(treffer)} Spiele passen - bitte eines nennen:")
            for m in treffer:
                print(zeige(m, jetzt, drin))
            print()
            continue
        m = treffer[0]
        if quelle != args.datum:
            print(f"  (gefunden am {quelle}, nicht am {args.datum} - der Tag der API ist nicht UTC-genau)")
        if getauscht:
            print(f"  (Heim und Auswaerts getauscht: {m['home_name']} hat Heimrecht)")
        print(zeige(m, jetzt, drin)); print()
        ids.append((m, huerden(m, jetzt, drin)))
    frei = [m['id'] for m, h in ids if not h]
    sperr = [(m, h) for m, h in ids if h]
    print(f"{len(ids)} von {len(args.paarungen)} Paarungen aufgeloest.")
    if sperr:
        print(f"\n  {len(sperr)} davon NICHT rechnen:")
        for m, h in sperr:
            print(f"    {m['id']}  {m['home_name']} - {m['away_name']}: {'; '.join(h)}")
        print("  (im Bericht trotzdem benennen, nicht stillschweigend weglassen)")
    if frei:
        print(f"\n  {len(frei)} zu rechnen:\n")
        print(f"  python3 analyse/modell.py {' '.join(str(i) for i in frei)}")
        print(f"  python3 analyse/bilanz.py --merken {' '.join(str(i) for i in frei)}")
    else:
        print("\n  Kein Spiel uebrig, das eine Prognose zulaesst.")
