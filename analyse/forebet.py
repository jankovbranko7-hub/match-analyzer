#!/usr/bin/env python3
"""Forebet-Gegenprobe: der Tipp gilt nur, wenn Forebet daneben passt.

VOM NUTZER AM 03.10.2026 VERLANGT, wortwoertlich:
  "Forebet wird daneben gelesen. Der Tipp gilt nur, wenn Forebet denselben Markt als
   haeufigstes Ergebnis hat und die erwarteten Tore hoechstens 0,40 auseinanderliegen."

Zwei Bedingungen, beide muessen stimmen:

  1. MARKT. Das haeufigste Ergebnis von Forebet muss die getippte Wette erfuellen.
     Aus einem Ergebnis h:a folgt eindeutig, welche der fuenf Wetten es traegt:
       H    h > a          A    h < a
       O25  h + a >= 3     U25  h + a <= 2       BTTS  h > 0 und a > 0
     Sagt Forebet 1:1 und das Modell tippt "Unter 2,5", stimmt es (1+1 = 2).
     Sagt Forebet 1:1 und das Modell tippt "Sieg Heim", stimmt es nicht.

  2. TORE. |erwartete Tore Modell - erwartete Tore Forebet| <= GRENZE_TORE (0,40).
     Verglichen wird die SUMME beider Lambda gegen Forebets Torerwartung.

Erfuellt ein Spiel beides, gilt der Tipp. Sonst VERFAELLT er - und das gehoert in den
Bericht, nicht in meinen Kopf.

WARUM DIE ZAHLEN VON HAND KOMMEN. Forebet laeuft hinter einer Cloudflare-Managed-
Challenge (HTTP 403 auf jede Anfrage, auch auf robots.txt, dort noindex/nofollow).
Ein automatischer Abruf waere das Umgehen eines gesetzten Zugangsschutzes und wird
deshalb nicht gebaut. Der Nutzer liest die zwei Werte ab - wie die Quoten beim
Buchmacher - und uebergibt sie hier. Die Modellzahlen holt dieses Skript selbst aus
modell.berechne(), damit nichts abgetippt wird (Regel "Keine Zahl von Hand").

Aufruf:
    python3 analyse/forebet.py 8419375=1:1@2.31 8469639=2:1
    python3 analyse/forebet.py --text        # Block lesen, wie Forebet ihn anzeigt

Format je Spiel:  <match_id>=<Forebet-Ergebnis>[@<Forebet-Torerwartung>]
Fehlt die Torerwartung, wird die Summe des Ergebnisses genommen (1:1 -> 2,0) und das
in der Ausgabe gesagt - Forebets eigene Zahl ist genauer, weil sie nicht gerundet ist.
"""
import argparse, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analyse.modell as M

GRENZE_TORE = 0.40          # vom Nutzer am 03.10.2026 festgelegt
WETTEN = ('H', 'A', 'O25', 'U25', 'BTTS')
NAME = {'H': 'Sieg Heim', 'A': 'Sieg Auswaerts', 'O25': 'Ueber 2,5',
        'U25': 'Unter 2,5', 'BTTS': 'Beide treffen'}


def traegt(wette, h, a):
    """Erfuellt das Ergebnis h:a die Wette? Dieselbe Abgrenzung wie in modell.probs()."""
    return {'H': h > a, 'A': h < a, 'O25': h + a >= 3,
            'U25': h + a <= 2, 'BTTS': h > 0 and a > 0}[wette]


def pruefe(tipp, lam_summe, fb_h, fb_a, fb_tore=None):
    """Gibt (gilt, markt_ok, tore_ok, abstand, fb_tore_benutzt) zurueck."""
    if fb_tore is None:
        fb_tore = float(fb_h + fb_a)
    markt_ok = traegt(tipp, fb_h, fb_a)
    abstand = abs(lam_summe - fb_tore)
    tore_ok = abstand <= GRENZE_TORE + 1e-9
    return (markt_ok and tore_ok), markt_ok, tore_ok, abstand, fb_tore


def zerlege(arg):
    """'8419375=1:1@2.31' -> (8419375, 1, 1, 2.31). Die Torerwartung ist optional."""
    m = re.fullmatch(r'\s*(\d+)\s*=\s*(\d+)\s*[:\-]\s*(\d+)\s*(?:@\s*([\d.,]+)\s*)?', arg)
    if not m:
        sys.exit(f"Unlesbar: {arg!r}. Erwartet <match_id>=<h>:<a>[@<Tore>], "
                 f"z. B. 8419375=1:1@2.31")
    mid, h, a, tore = m.groups()
    return int(mid), int(h), int(a), (float(tore.replace(',', '.')) if tore else None)


def bericht(mid, fb_h, fb_a, fb_tore, args):
    r = M.berechne(mid, args)
    m = r['match']
    kopf = f"{m['home_name']} - {m['away_name']} (Spiel {mid})"
    print('=' * 70)
    print(kopf)
    if r['gesperrt']:
        print(f"  KEINE PROGNOSE (Saisonspiele {r['nh']}/{r['na']}, noetig "
              f"{M.MIN_SAISONSPIELE}) - die Gegenprobe entfaellt.")
        return None
    p = r['p']
    tipp = max(WETTEN, key=lambda w: float(p[w]))
    lam = float(r['flh']) + float(r['fla'])
    gilt, markt_ok, tore_ok, abstand, fb_benutzt = pruefe(tipp, lam, fb_h, fb_a, fb_tore)
    print(f"  Modell:  {NAME[tipp]} {float(p[tipp])*100:.1f} %   "
          f"erwartete Tore {r['flh']:.2f} : {r['fla']:.2f}  (Summe {lam:.2f})")
    quelle = '' if fb_tore is not None else '  (aus dem Ergebnis, Forebets eigene Zahl fehlt)'
    print(f"  Forebet: haeufigstes Ergebnis {fb_h}:{fb_a}   "
          f"erwartete Tore {fb_benutzt:.2f}{quelle}")
    print(f"  1) Markt: {fb_h}:{fb_a} traegt {NAME[tipp]}? "
          f"{'JA' if markt_ok else 'NEIN'}")
    print(f"  2) Tore:  Abstand {abstand:.2f} <= {GRENZE_TORE:.2f}? "
          f"{'JA' if tore_ok else 'NEIN'}")
    if gilt:
        print(f"  --> TIPP GILT: {NAME[tipp]}")
    else:
        grund = []
        if not markt_ok:
            grund.append(f"Forebets {fb_h}:{fb_a} traegt {NAME[tipp]} nicht")
        if not tore_ok:
            grund.append(f"Torerwartung {abstand:.2f} auseinander (erlaubt {GRENZE_TORE:.2f})")
        print(f"  --> TIPP VERFAELLT: {' und '.join(grund)}")
    return dict(mid=mid, tipp=tipp, p=float(p[tipp]), lam=lam, fb=(fb_h, fb_a),
                fb_tore=fb_benutzt, gilt=gilt, markt_ok=markt_ok, tore_ok=tore_ok,
                abstand=abstand, heim=m['home_name'], ausw=m['away_name'])


def lies_block(text):
    """Liest einen Block '<match_id> <h>:<a> [<Tore>]' je Zeile, wie man ihn abtippt."""
    out = []
    for zeile in text.splitlines():
        z = zeile.strip()
        if not z or z.startswith('#'):
            continue
        t = re.fullmatch(r'(\d+)\s+(\d+)\s*[:\-]\s*(\d+)(?:\s+([\d.,]+))?', z)
        if not t:
            print(f"  uebersprungen: {z!r}", file=sys.stderr)
            continue
        mid, h, a, tore = t.groups()
        out.append((int(mid), int(h), int(a),
                    float(tore.replace(',', '.')) if tore else None))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('spiele', nargs='*', help='<match_id>=<h>:<a>[@<Tore>]')
    ap.add_argument('--text', action='store_true',
                    help='Block von der Standardeingabe lesen, eine Zeile je Spiel')
    ap.add_argument('--neu', action='store_true', help='API-Daten neu laden')
    ap.add_argument('--trotzdem', action='store_true',
                    help='Sperre bei zu wenigen Saisonspielen umgehen')
    ap.add_argument('--markt', type=float, default=M.MARKT_ANTEIL)
    ap.add_argument('--daten', default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'daten'))
    args = ap.parse_args()

    eingaben = []
    if args.text:
        eingaben = lies_block(sys.stdin.read())
    for s in args.spiele:
        eingaben.append(zerlege(s))
    if not eingaben:
        ap.print_help()
        return

    zeilen = [z for z in (bericht(*e, args) for e in eingaben) if z]
    gueltig = [z for z in zeilen if z['gilt']]
    print('=' * 70)
    print(f"{len(gueltig)} von {len(zeilen)} Tipps bestehen die Forebet-Gegenprobe.")
    if zeilen:
        print(f"\n{'Spiel':40s} {'Tipp':16s} {'Modell':>7s} {'Forebet':>8s} "
              f"{'Abstand':>8s}  Urteil")
        for z in zeilen:
            paar = f"{z['heim']} - {z['ausw']}"[:39]
            print(f"{paar:40s} {NAME[z['tipp']]:16s} {z['lam']:7.2f} "
                  f"{z['fb_tore']:8.2f} {z['abstand']:8.2f}  "
                  f"{'gilt' if z['gilt'] else 'verfaellt'}")
    if len(gueltig) < len(zeilen):
        print("\nVerfallene Tipps werden im Bericht als verfallen ausgewiesen und kommen "
              "in keine Kombi.")


if __name__ == '__main__':
    main()
