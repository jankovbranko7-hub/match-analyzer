"""Live-Filter: prüft einen Alarm aus der Live-App, bevor gewettet wird.

    python3 analyse/live.py --spiel "Heim – Auswärts" --minute 62 --stand 1:1 \\
        --druck heim --druck-prozent 68 --sot 6:1 --da 45:24 --schnitt 1.6 --quote 1.55
    python3 analyse/live.py ... --merken                 # Prüfung festhalten
    python3 analyse/live.py --ergebnis 3 ja              # Alarm 3: fiel danach ein Tor?
    python3 analyse/live.py --auswerten                  # Bilanz aller Signale

Die Wette ist immer dieselbe: **noch mindestens ein Tor** (Über aktueller Stand + 0,5).

Warum es das Skript braucht: Die App prüft jede Regel für sich. Druck, Schüsse und
Tore-Schnitt können von drei verschiedenen Teams kommen, und den Spielstand sieht sie
nicht. Am 27.09.2026 waren alle 10 Alarme des alten Filters Fehlsignale. Hier müssen
alle Bedingungen für **dasselbe** Team gelten, und gewettet wird nur über der fairen Quote.

`analyse/live.json` sammelt jede Prüfung. Einträge werden nie nachträglich geändert,
nur das Ergebnis wird nachgetragen.
"""
import argparse, json, math, os, sys
from datetime import datetime

LIVE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "live.json")

# ---------------------------------------------------------------- Schwellen
#
# NACH ERFAHRUNG GESETZT, NICHT AN VERGANGENEN SPIELEN GETESTET.
# Nur auf ausdrückliches Verlangen des Nutzers ändern, Begründung danebenschreiben.
# Nicht nach wenigen Alarmen nachstellen: Erst ab rund 50 Signalen lässt sich eine
# Trefferquote grob beurteilen.

MINUTE_VON        = 55     # Nach der Pause: der Druck ist aktuell, nicht aus der 1. Halbzeit
MINUTE_BIS        = 75     # übrig. Danach bleibt zu wenig Restzeit für eine faire Quote.
DRUCK_MIN         = 65     # Pressure Recent % des Druck-Teams. 60 lässt zu viel Ballgeschiebe durch.
SOT_TEAM_MIN      = 5      # Schüsse aufs Tor des Druck-Teams.
SOT_GEGNER_MAX    = 2      # Schüsse aufs Tor des Gegners: das Spiel muss einseitig sein.
DA_ANTEIL_MIN     = 60     # Anteil des Druck-Teams an allen Dangerous Attacks, in %.
                           # Schüsse sind wenige Ereignisse und schwanken, Dangerous Attacks
                           # zeigen über das ganze Spiel, ob die Überlegenheit echt ist.
SCHNITT_MIN       = 1.4    # Saison-Tore pro Spiel des Druck-Teams. Schüsse ohne Abschluss-
                           # qualität bringen nichts (siehe SOLLBRUCHSTELLEN.md, Punkt 6).
RUECKSTAND_MAX    = 1      # Das Druck-Team darf nicht führen und höchstens 1 Tor zurückliegen.
                           # Wer führt, nimmt Tempo raus. Wer 2 hinten liegt, gibt oft auf.
NACHSPIELZEIT     = 5      # Minuten Nachspielzeit in der 2. Halbzeit.
ANTEIL_2HZ        = 0.55   # Anteil der Tore, die in der 2. Halbzeit fallen.
DRUCK_FAKTOR      = 1.20   # So viel höher als normal liegt die Torrate bei klarem Druck.
                           # Der unsicherste Wert hier. Ist er zu hoch, sind alle fairen
                           # Quoten zu niedrig und jede Wette verliert auf Dauer.
MARGE             = 1.05   # Gewettet wird erst 5 % über der fairen Quote.


def tor_chance(minute, liga_schnitt):
    """Wahrscheinlichkeit für mindestens ein weiteres Tor bis zum Abpfiff (Poisson)."""
    rate = liga_schnitt * ANTEIL_2HZ / (45 + NACHSPIELZEIT)       # Tore pro Minute, 2. HZ
    rest = max(0, 90 + NACHSPIELZEIT - minute)
    return 1 - math.exp(-rate * DRUCK_FAKTOR * rest)


def pruefen(a):
    h, g = (int(x) for x in a.stand.split(':'))
    sh, sg = (int(x) for x in a.sot.split(':'))
    dh, dg = (int(x) for x in a.da.split(':'))
    eigen, gegner = (h, g) if a.druck == 'heim' else (g, h)
    sot_e, sot_g = (sh, sg) if a.druck == 'heim' else (sg, sh)
    rueck = gegner - eigen
    da_e = dh if a.druck == 'heim' else dg
    da_anteil = 100 * da_e / max(1, dh + dg)

    p = tor_chance(a.minute, a.liga_schnitt)
    fair = 1 / p
    ab = fair * MARGE
    regeln = [
        (f"Minute {MINUTE_VON}–{MINUTE_BIS}", MINUTE_VON <= a.minute <= MINUTE_BIS, f"{a.minute}."),
        (f"Druck ≥ {DRUCK_MIN} %", a.druck_prozent >= DRUCK_MIN, f"{a.druck_prozent:g} %"),
        (f"Schüsse aufs Tor ≥ {SOT_TEAM_MIN}", sot_e >= SOT_TEAM_MIN, str(sot_e)),
        (f"Gegner Schüsse aufs Tor ≤ {SOT_GEGNER_MAX}", sot_g <= SOT_GEGNER_MAX, str(sot_g)),
        (f"Dangerous Attacks ≥ {DA_ANTEIL_MIN} %", da_anteil >= DA_ANTEIL_MIN,
         f"{da_anteil:.0f} % ({a.da})"),
        (f"Tore-Schnitt ≥ {SCHNITT_MIN}".replace('.', ','), a.schnitt >= SCHNITT_MIN,
         f"{a.schnitt:.2f}".replace('.', ',')),
        (f"führt nicht, max. {RUECKSTAND_MAX} Tor hinten", 0 <= rueck <= RUECKSTAND_MAX,
         f"{eigen}:{gegner} aus Sicht Druck-Team"),
    ]
    if a.quote:
        regeln.append((f"Quote ≥ {ab:.2f}".replace('.', ','), a.quote >= ab, f"{a.quote:.2f}".replace('.', ',')))
    signal = all(ok for _, ok, _ in regeln) and bool(a.quote)
    return dict(regeln=regeln, p=p, fair=fair, ab=ab, signal=signal, tore=h + g)


def ausgeben(a, r):
    wette = f"Über {r['tore']},5 (noch ein Tor)"
    print(f"{a.spiel or 'Spiel'} – Druck-Team: {a.druck}, Stand {a.stand}, {a.minute}. Minute")
    for name, ok, wert in r['regeln']:
        print(f"  {'✓' if ok else '✗'} {name:<34} {wert}")
    print(f"  Wette: {wette}")
    print(f"  Chance noch ein Tor: {r['p']*100:.1f} %, faire Quote {r['fair']:.2f}, "
          f"wetten ab {r['ab']:.2f}".replace('.', ','))
    if not a.quote:
        print("  → Live-Quote fehlt (--quote), ohne sie kein Signal.")
    print("  → SIGNAL: wetten." if r['signal'] else "  → KEIN Signal: nicht wetten.")


# ---------------------------------------------------------------- Bilanz

def laden():
    return json.load(open(LIVE)) if os.path.exists(LIVE) else []


def speichern(e):
    json.dump(e, open(LIVE, 'w'), indent=1, ensure_ascii=False)


def merken(a, r):
    e = laden()
    nr = max((x['nr'] for x in e), default=0) + 1
    e.append(dict(nr=nr, zeit=datetime.now().isoformat(timespec='minutes'), spiel=a.spiel,
                  minute=a.minute, stand=a.stand, druck=a.druck, druck_prozent=a.druck_prozent,
                  sot=a.sot, da=a.da, schnitt=a.schnitt, liga_schnitt=a.liga_schnitt, quote=a.quote,
                  p=round(r['p'], 4), fair=round(r['fair'], 2), signal=r['signal'],
                  ergebnis=None))
    speichern(e)
    print(f"  Als Nr. {nr} festgehalten. Nach dem Spiel: --ergebnis {nr} ja|nein")


def ergebnis(nr, wert):
    e = laden()
    x = next((x for x in e if x['nr'] == nr), None)
    if not x:
        sys.exit(f"Nr. {nr} gibt es nicht.")
    if x['ergebnis'] is not None:
        sys.exit(f"Nr. {nr} hat schon ein Ergebnis, unverändert gelassen.")
    x['ergebnis'] = wert == 'ja'
    speichern(e)
    print(f"Nr. {nr}: {'Tor gefallen' if x['ergebnis'] else 'kein Tor mehr'}.")


def auswerten():
    e = laden()
    s = [x for x in e if x['signal'] and x['ergebnis'] is not None]
    offen = sum(1 for x in e if x['signal'] and x['ergebnis'] is None)
    print(f"{len(e)} Prüfungen, {sum(x['signal'] for x in e)} Signale, "
          f"{len(s)} ausgewertet, {offen} offen.")
    if not s:
        return
    treffer = sum(x['ergebnis'] for x in s)
    erwartet = sum(x['p'] for x in s)
    sd = math.sqrt(sum(x['p'] * (1 - x['p']) for x in s))
    saldo = sum((x['quote'] - 1) if x['ergebnis'] else -1 for x in s)
    print(f"  Treffer {treffer} von {len(s)}, erwartet {erwartet:.1f}, "
          f"z = {(treffer - erwartet) / sd:+.2f}".replace('.', ','))
    print(f"  Saldo bei 1 Einheit Einsatz: {saldo:+.2f} Einheiten".replace('.', ','))
    if len(s) < 50:
        print("  Unter 50 Signalen ist das kein Urteil über den Filter.")
    nicht = [x for x in e if not x['signal'] and x['ergebnis'] is not None]
    if nicht:
        print(f"  Aussortierte Alarme mit Ergebnis: {sum(x['ergebnis'] for x in nicht)} "
              f"von {len(nicht)} mit Tor.")


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--spiel', default='')
    ap.add_argument('--minute', type=int)
    ap.add_argument('--stand', help='Spielstand Heim:Auswärts, z. B. 1:1')
    ap.add_argument('--druck', choices=['heim', 'auswaerts'], help='Team mit dem Druck')
    ap.add_argument('--druck-prozent', type=float, help='Pressure Recent %% dieses Teams')
    ap.add_argument('--sot', help='Schüsse aufs Tor Heim:Auswärts, z. B. 6:1')
    ap.add_argument('--da', help='Dangerous Attacks Heim:Auswärts, z. B. 24:45')
    ap.add_argument('--schnitt', type=float, help='Saison-Tore pro Spiel des Druck-Teams')
    ap.add_argument('--liga-schnitt', type=float, default=2.7, help='Tore pro Spiel der Liga')
    ap.add_argument('--quote', type=float, help='Live-Quote für Über (Stand + 0,5)')
    ap.add_argument('--merken', action='store_true')
    ap.add_argument('--ergebnis', nargs=2, metavar=('NR', 'ja|nein'))
    ap.add_argument('--auswerten', action='store_true')
    a = ap.parse_args()

    if a.auswerten:
        auswerten()
    elif a.ergebnis:
        ergebnis(int(a.ergebnis[0]), a.ergebnis[1])
    else:
        fehlt = [n for n in ('minute', 'stand', 'druck', 'druck_prozent', 'sot', 'da', 'schnitt')
                 if getattr(a, n) is None]
        if fehlt:
            ap.error("es fehlt: " + ", ".join('--' + n.replace('_', '-') for n in fehlt))
        r = pruefen(a)
        ausgeben(a, r)
        if a.merken:
            merken(a, r)
