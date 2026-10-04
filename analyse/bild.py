#!/usr/bin/env python3
"""Maximales Spielbild: alles, was die API zu einer Partie hergibt, auf einer Seite.

VOM NUTZER AM 04.10.2026 VERLANGT: "Es sollte ein maximales Spiel Bild entstehen. Und
keine Sperre wieviel Spiele sie hatten."

Die Sperre ist in modell.py entfernt. Diese Datei liefert das Bild: sie rechnet nichts
Neues und aendert keinen Tipp, sondern stellt die Rohdaten beider Teams nebeneinander,
dazu die Modellzahlen aus berechne(). Grundlage sind die Felder, die in den
zwischengespeicherten Antworten WIRKLICH stehen - jedes hier gezeigte Feld ist an echten
Daten geprueft, nichts ist geraten. FootyStats liefert 1065 Felder je Team; das Modell
rechnet mit 11, dieses Bild zeigt rund 40.

Spalte 'Liga' ist das mit der Spielzahl gewichtete Mittel aller Teams der Liga - damit
sieht man auf einen Blick, ob ein Wert hoch ist oder nur hoch aussieht.

    python3 analyse/bild.py 8419375 8469639
    python3 analyse/bild.py --liste 2026-10-04
"""
import argparse, os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analyse.modell as M

# (Beschriftung, Feld-overall, Feld-home, Feld-away, Format)  - alle Namen an echten
# Daten geprueft. None heisst: die Seite gibt es nicht, dann bleibt die Spalte leer.
ZEILEN = [
    ('Spiele',            'seasonMatchesPlayed_overall', 'seasonMatchesPlayed_home', 'seasonMatchesPlayed_away', '{:.0f}'),
    ('Punkte/Spiel',      'seasonPPG_overall',           'seasonPPG_home',           'seasonPPG_away',           '{:.2f}'),
    ('S-U-N',             None, None, None, None),
    ('Tore',              'seasonScoredAVG_overall',     'seasonScoredAVG_home',     'seasonScoredAVG_away',     '{:.2f}'),
    ('Gegentore',         'seasonConcededAVG_overall',   'seasonConcededAVG_home',   'seasonConcededAVG_away',   '{:.2f}'),
    ('xG',                'xg_for_avg_overall',          'xg_for_avg_home',          'xg_for_avg_away',          '{:.2f}'),
    ('xGA',               'xg_against_avg_overall',      'xg_against_avg_home',      'xg_against_avg_away',      '{:.2f}'),
    ('Tore 1. Halbzeit',  'scoredAVGHT_overall',         None, None,                                             '{:.2f}'),
    ('Gegent. 1. HZ',     'concededAVGHT_overall',       None, None,                                             '{:.2f}'),
    ('Schuesse',          'shotsAVG_overall',            'shotsAVG_home',            'shotsAVG_away',            '{:.1f}'),
    ('davon aufs Tor',    'shotsOnTargetAVG_overall',    'shotsOnTargetAVG_home',    'shotsOnTargetAVG_away',    '{:.1f}'),
    ('Ballbesitz %',      'possessionAVG_overall',       'possessionAVG_home',       'possessionAVG_away',       '{:.0f}'),
    ('Angriffe',          'attacks_avg_overall',         'attacks_avg_home',         'attacks_avg_away',         '{:.0f}'),
    ('gefaehrliche',      'dangerous_attacks_avg_overall','dangerous_attacks_avg_home','dangerous_attacks_avg_away','{:.0f}'),
    ('Ecken',             'cornersAVG_overall',          None, None,                                             '{:.1f}'),
    ('Karten',            'cardsAVG_overall',            None, None,                                             '{:.1f}'),
    ('Zu Null %',         'seasonCSPercentage_overall',  'seasonCSPercentage_home',  'seasonCSPercentage_away',  '{:.0f}'),
    ('ohne eig. Tor %',   'seasonFTSPercentage_overall', 'seasonFTSPercentage_home', 'seasonFTSPercentage_away', '{:.0f}'),
    ('Ueber 2,5 %',       'seasonOver25Percentage_overall','seasonOver25Percentage_home','seasonOver25Percentage_away','{:.0f}'),
    ('Beide treffen %',   'seasonBTTSPercentage_overall','seasonBTTSPercentage_home','seasonBTTSPercentage_away','{:.0f}'),
    ('Tordifferenz',      'seasonGoalDifference_overall', None, None,                                            '{:+.0f}'),
]


def liga_mittel(T, feld):
    """Mit der Spielzahl gewichtetes Ligamittel. 0, wenn die Liga noch nichts gespielt hat."""
    n = sum((t['stats'].get('seasonMatchesPlayed_overall') or 0) for t in T)
    if not n:
        return None
    su = 0.0
    for t in T:
        v = t['stats'].get(feld)
        w = t['stats'].get('seasonMatchesPlayed_overall') or 0
        if v is None:
            return None
        su += v * w
    return su / n


def zahl(v, fmt):
    return fmt.format(v) if isinstance(v, (int, float)) else '-'


def bild(mid, args):
    r = M.berechne(mid, args)
    m = r['match']
    print('=' * 78)
    print(f"{m['home_name']} - {m['away_name']}   (Spiel {mid}, Saison {r['sid']})")
    if r['gesperrt']:
        print(f"  KEINE PROGNOSE. {r.get('grund', '')}")
        return
    T = M.hole("league-teams", {"season_id": r['sid'], "include": "stats"},
               f"teams_{r['sid']}.json", args)['data']
    sh = next(t for t in T if t['id'] == m['homeID'])
    sa = next(t for t in T if t['id'] == m['awayID'])

    # --- Modellzahlen
    p = {k: float(v) * 100 for k, v in r['p'].items()}
    print(f"  Erwartete Tore {r['flh']:.2f} : {r['fla']:.2f}"
          f"   |   Heim {p['H']:.1f} %  Remis {p['D']:.1f} %  Ausw {p['A']:.1f} %")
    print(f"  Ueber 2,5 {p['O25']:.1f} %   Unter 2,5 {p['U25']:.1f} %   "
          f"Beide treffen {p['BTTS']:.1f} %")
    print(f"  Haeufigste Ergebnisse: " +
          ', '.join(f"{e} {v*100:.1f} %" for e, v in r['top3']))
    print(f"  Staerken: Heim Att {r['ah']:.2f} Def {r['dh']:.2f} | "
          f"Ausw Att {r['aa']:.2f} Def {r['da']:.2f}   (1,00 = Liga-Durchschnitt)")

    # --- Datengrundlage, ohne Sperre, aber benannt
    duenn = []
    if r['nh'] < M.MIN_SAISONSPIELE: duenn.append(f"Heim nur {r['nh']}")
    if r['na'] < M.MIN_SAISONSPIELE: duenn.append(f"Ausw nur {r['na']}")
    print(f"  Datengrundlage: Heim {r['nh']} Saisonspiele, Ausw {r['na']}"
          + (f"  <-- duenn ({', '.join(duenn)})" if duenn else ''))
    if r['fen_h'] or r['fen_a']:
        print(f"  Fenster: Heim {r['fen_h']:.0%} aus den letzten 10 Spielen | "
              f"Ausw {r['fen_a']:.0%}")
    print(f"  H2H-Gewicht {r['h2h_w']:.0%}" +
          (f"   |   Markt-Anteil {r['w']:.0%}" if r['mk'] else "   |   keine vollstaendigen Vorab-Quoten"))

    # --- die Tabelle
    print()
    print(f"  {'':18s} {'HEIM ges':>9s} {'heim':>7s} | {'AUSW ges':>9s} {'ausw':>7s} | {'Liga':>7s}")
    print('  ' + '-' * 74)
    for name, f_o, f_h, f_a, fmt in ZEILEN:
        if f_o is None:                      # Sonderzeile S-U-N
            def sun(st):
                g = lambda k: st['stats'].get(k)
                return f"{g('seasonWinsNum_overall')}-{g('seasonDrawsNum_overall')}-{g('seasonLossesNum_overall')}"
            print(f"  {name:18s} {sun(sh):>9s} {'':>7s} | {sun(sa):>9s} {'':>7s} | {'':>7s}")
            continue
        lm = liga_mittel(T, f_o)
        print(f"  {name:18s} {zahl(sh['stats'].get(f_o), fmt):>9s} "
              f"{zahl(sh['stats'].get(f_h), fmt) if f_h else '':>7s} | "
              f"{zahl(sa['stats'].get(f_o), fmt):>9s} "
              f"{zahl(sa['stats'].get(f_a), fmt) if f_a else '':>7s} | "
              f"{zahl(lm, fmt):>7s}")

    # --- Form aus lastx, alle drei Bloecke
    print()
    for tid, lab in ((m['homeID'], 'Heim'), (m['awayID'], 'Ausw')):
        d = M.hole("lastx", {"team_id": tid}, f"lastx_{tid}.json", args)['data']
        teile = []
        for num in (5, 6, 10):
            b = next((e for e in d if e['last_x_match_num'] == num), None)
            if not b:
                continue
            st = b['stats']
            teile.append(f"{num}: {st.get('seasonScoredAVG_overall')}-"
                         f"{st.get('seasonConcededAVG_overall')} Tore, "
                         f"xG {st.get('xg_for_avg_overall')}, PPG {st.get('seasonPPG_overall')}")
        print(f"  Form {lab}: " + ('  |  '.join(teile) if teile else 'kein lastx-Block'))

    # --- H2H und Quoten
    h2h = (m.get('h2h') or {}).get('previous_matches_ids') or []
    jung = [x for x in h2h if m['date_unix'] - x['date_unix'] <= M.H2H_MAX_JAHRE*365*86400]
    if jung:
        erg = ', '.join(f"{x['team_a_goals']}:{x['team_b_goals']}" for x in jung[:6])
        schnitt = sum(x['team_a_goals']+x['team_b_goals'] for x in jung)/len(jung)
        print(f"  Direkte Duelle (max {M.H2H_MAX_JAHRE} Jahre): {len(jung)} Stueck, "
              f"{schnitt:.2f} Tore im Schnitt  [{erg}]")
    else:
        print(f"  Direkte Duelle: keine in den letzten {M.H2H_MAX_JAHRE} Jahren")
    if r['mk']:
        print(f"  FootyStats-Quoten: 1 {m['odds_ft_1']}  X {m['odds_ft_x']}  2 {m['odds_ft_2']}"
              f"   O2.5 {m['odds_ft_over25']}  U2.5 {m['odds_ft_under25']}  "
              f"BTTS {m['odds_btts_yes']}")
        print(f"  Markt ohne Marge: " +
              '  '.join(f"{k} {float(v)*100:.1f} %" for k, v in r['mk'].items()))
    print(f"  Faire Quoten: " +
          '  '.join(f"{k} {1/float(v):.2f}" for k, v in r['p'].items()))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('spiele', nargs='*', type=int)
    ap.add_argument('--liste', metavar='DATUM')
    ap.add_argument('--markt', type=float, default=M.MARKT_ANTEIL)
    ap.add_argument('--neu', action='store_true')
    ap.add_argument('--trotzdem', action='store_true', help='ohne Wirkung, die Sperre ist weg')
    ap.add_argument('--daten', default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'daten'))
    args = ap.parse_args()
    if args.liste:
        M.liste(args.liste, args)
    for mid in args.spiele:
        try:
            bild(mid, args)
        except Exception as e:
            print(f"  Spiel {mid}: {type(e).__name__}: {e}")
    if not args.liste and not args.spiele:
        ap.print_help()
