# Häkchen für Forebet-Check Version 2.12 (Einstufung klar/knapp), berechnet aus FootyStats.
# Aufruf: python3 -I werkzeuge/fs_haekchen.py <season_id> "<Heim-Teilname>" "<Auswärts-Teilname>" [tipp]
#   tipp: heim | ausw | ja | nein | ueber | unter   (ohne tipp: Tabelle für alle sechs Märkte)
# Gibt aus: Schritt 1/2 (Siege aus 6, sieglos am Spielort, klare Seite), Häkchen „Form“ und
# „Saison am Spielort“ mit allen Zahlen, Direktvergleiche (nur Anzeige). Das Häkchen
# „Ausfälle/Motivation“ (Rang 1) setzt Claude aus der Vorschau. Keine Quoten.
#
# Regeln für die Häkchen (fest, jeden Tag gleich):
#   Form = letzte 6 aller Wettbewerbe (FootyStats lastx), Saison = Heimteam daheim, Gastteam auswärts.
#   „zeigt zum Tipp“ = mindestens die Hälfte der Spiele in Richtung des Tipps:
#   heim  – Form: Heim ≥ 3 Siege, Gast ≤ 3 Siege · Saison: Heim gewinnt daheim ≥ 50 %, Gast verliert auswärts ≥ 50 %
#   ausw  – spiegelbildlich
#   ja/nein   – beide Teams beide treffen ≥ 50 % bzw. ≤ 50 %
#   ueber/unter – beide Teams über 2,5 ≥ 50 % bzw. ≤ 50 %
#   Saison zählt erst ab 4 Spielen am Spielort, sonst „–“ (dann entscheiden Rang 1–2 allein).
import json, sys, subprocess, os
S = os.path.dirname(os.path.abspath(__file__))
SEASON, H, A = sys.argv[1], sys.argv[2].lower(), sys.argv[3].lower()
TIPP = sys.argv[4].lower() if len(sys.argv) > 4 else None
MK = {'heim': 'Heimsieg', 'ausw': 'Auswärtssieg', 'ja': 'Beide treffen – Ja', 'nein': 'Beide treffen – Nein',
      'ueber': 'Über 2,5', 'unter': 'Unter 2,5'}
if TIPP and TIPP not in MK:
    sys.exit('tipp muss heim, ausw, ja, nein, ueber oder unter sein')

def get(path, **q):
    out = subprocess.run([S + '/fs.sh', path] + [f'{k}={v}' for k, v in q.items()],
                         capture_output=True, text=True).stdout
    body, code = out.rsplit('\n__HTTP', 1)
    if code.strip() != '200':
        sys.exit(f'HTTP {code.strip()} bei {path}')
    return json.loads(body)

lm = get('league-matches', season_id=SEASON, max_per_page=1000)['data']
cand = [m for m in lm if H in m['home_name'].lower() and A in m['away_name'].lower()]
if not cand:
    sys.exit('Spiel nicht gefunden – Teilnamen prüfen')
cand.sort(key=lambda m: (m['status'] == 'complete', m['date_unix']))
mm = cand[0]
hid, aid = mm['homeID'], mm['awayID']
m = get('match', match_id=mm['id'])['data']
lt = {x['id']: x['stats'] for x in get('league-teams', season_id=SEASON, include='stats')['data']}

def l6(tid):
    e = [x for x in get('lastx', team_id=tid)['data'] if x.get('last_x_match_num') == 6]
    if not e:
        return None
    s = e[0]['stats']
    n = (s.get('seasonWinsNum_overall') or 0) + (s.get('seasonDrawsNum_overall') or 0) + (s.get('seasonLossesNum_overall') or 0)
    return dict(n=n, w=s.get('seasonWinsNum_overall') or 0, d=s.get('seasonDrawsNum_overall') or 0,
                l=s.get('seasonLossesNum_overall') or 0, bt=s.get('seasonBTTSPercentage_overall') or 0,
                o=s.get('seasonOver25Percentage_overall') or 0)

def venue(tid, sfx):
    s = lt.get(tid) or {}
    n = s.get(f'seasonMatchesPlayed_{sfx}') or 0
    if not n:
        return dict(n=0)
    return dict(n=n, w=s.get(f'seasonWinsNum_{sfx}') or 0, d=s.get(f'seasonDrawsNum_{sfx}') or 0,
                l=s.get(f'seasonLossesNum_{sfx}') or 0, bt=s.get(f'seasonBTTSPercentage_{sfx}') or 0,
                o=s.get(f'seasonOver25Percentage_{sfx}') or 0)

fh, fa = l6(hid), l6(aid)
vh, va = venue(hid, 'home'), venue(aid, 'away')
hn, an = m['home_name'], m['away_name']
pc = lambda a, b: round(100 * a / b) if b else 0
sg = lambda n: f"{n} Sieg" if n == 1 else f"{n} Siege"

def haken(t):
    """liefert (Form-Häkchen, Text), (Saison-Häkchen, Text)"""
    if fh is None or fa is None:
        F = ('?', 'letzte 6 fehlen')
    elif t == 'heim':
        F = ('✓' if fh['w'] >= 3 and fa['w'] <= 3 else '✗', f"{hn} {sg(fh['w'])} aus {fh['n']}, {an} {sg(fa['w'])} aus {fa['n']}")
    elif t == 'ausw':
        F = ('✓' if fa['w'] >= 3 and fh['w'] <= 3 else '✗', f"{an} {sg(fa['w'])} aus {fa['n']}, {hn} {sg(fh['w'])} aus {fh['n']}")
    else:
        k = 'bt' if t in ('ja', 'nein') else 'o'
        ok = (fh[k] >= 50 and fa[k] >= 50) if t in ('ja', 'ueber') else (fh[k] <= 50 and fa[k] <= 50)
        lab = 'beide treffen' if k == 'bt' else 'über 2,5'
        F = ('✓' if ok else '✗', f"{lab}: {hn} {fh[k]} %, {an} {fa[k]} % (letzte 6)")
    if vh['n'] < 4 or va['n'] < 4:
        V = ('–', f"zu wenig Spiele am Spielort ({hn} daheim {vh['n']}, {an} auswärts {va['n']}) – zählt nicht")
    elif t == 'heim':
        a, b = pc(vh['w'], vh['n']), pc(va['l'], va['n'])
        V = ('✓' if a >= 50 and b >= 50 else '✗', f"{hn} gewinnt daheim {a} % ({vh['w']}-{vh['d']}-{vh['l']}), {an} verliert auswärts {b} % ({va['w']}-{va['d']}-{va['l']})")
    elif t == 'ausw':
        a, b = pc(va['w'], va['n']), pc(vh['l'], vh['n'])
        V = ('✓' if a >= 50 and b >= 50 else '✗', f"{an} gewinnt auswärts {a} % ({va['w']}-{va['d']}-{va['l']}), {hn} verliert daheim {b} % ({vh['w']}-{vh['d']}-{vh['l']})")
    else:
        k = 'bt' if t in ('ja', 'nein') else 'o'
        ok = (vh[k] >= 50 and va[k] >= 50) if t in ('ja', 'ueber') else (vh[k] <= 50 and va[k] <= 50)
        lab = 'beide treffen' if k == 'bt' else 'über 2,5'
        V = ('✓' if ok else '✗', f"{lab}: {hn} daheim {vh[k]} % ({vh['n']} Sp.), {an} auswärts {va[k]} % ({va['n']} Sp.)")
    return F, V

print(f"## {hn} – {an} · match_id {mm['id']}")
# Schritt 1 und 2 (Entscheidungsweg), mechanisch
if fh and fa:
    aus = [x for x, f in ((hn, fh), (an, fa)) if f['w'] <= 1]
    print(f"Schritt 1: {hn} {fh['w']}-{fh['d']}-{fh['l']}, {an} {fa['w']}-{fa['d']}-{fa['l']} (letzte 6) · "
          f"kein Sieg-Tipp wegen Form: {', '.join(aus) if aus else 'keiner'} · Motivation: aus der Vorschau prüfen")
    hs = vh.get('n', 0) > 0 and vh.get('w', 0) == 0
    as_ = va.get('n', 0) > 0 and va.get('w', 0) == 0
    hc = fh['w'] >= 3 and (fa['w'] <= 1 or as_)
    ac = fa['w'] >= 3 and (fh['w'] <= 1 or hs)
    seite = (hn if hc else an) if hc != ac else None
    print(f"Schritt 2: sieglos am Spielort – {hn} daheim: {'ja' if hs else 'nein'}, {an} auswärts: {'ja' if as_ else 'nein'} · "
          f"klare Seite: {seite or 'keine → Schritt 3'}")

h = m.get('h2h') or {}
r, b = h.get('previous_matches_results', {}), h.get('betting_stats', {})
h2 = (f"Direktvergleiche (nur Anzeige): {r.get('totalMatches', 0)} Spiele · {hn} {r.get('team_a_wins')} Siege · "
      f"Remis {r.get('draw')} · {an} {r.get('team_b_wins')} Siege · beide treffen {b.get('bttsPercentage')} % · "
      f"über 2,5 {b.get('over25Percentage')} %")

if TIPP:
    (f1, ft), (v1, vt) = haken(TIPP)
    print(f"Tipp: {MK[TIPP]}")
    print(f"  Form: {f1}  {ft}")
    print(f"  Saison am Spielort: {v1}  {vt}")
    print(f"  Ausfälle/Motivation: von Claude aus der Vorschau setzen")
    print(f"  → Einstufung aus Zahlen: {'klar möglich (wenn Ausfälle/Motivation ✓)' if f1 == '✓' and v1 in ('✓', '–') else 'knapp'}")
else:
    print(f"{'Markt':22} | Form | Saison | Zahlen")
    for t in MK:
        (f1, ft), (v1, vt) = haken(t)
        print(f"{MK[t]:22} |  {f1}   |   {v1}   | {ft} · {vt}")
print(h2)
