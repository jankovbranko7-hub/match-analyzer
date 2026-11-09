# Odd-Alerts-Daten zu einem Spiel (Forebet-Check v2.5) – ohne Quoten.
# Aufruf: python3 -I werkzeuge/oa_spiel.py <competition_id> "<Heim-Teilname>" "<Auswärts-Teilname>"
# Gibt aus: Fixture, Saisonwerte gesamt/Heim/Auswärts (stats/fixture) und das Odd-Alerts-Modell
# (trends/btts → probability) – das Modell NUR ZUM VERGLEICH, es fließt nicht in den Tipp ein.
# Letzte Spiele inkl. Pokal und Direktvergleiche: werkzeuge/ergebnisse.py
import json, sys, subprocess, os, datetime
from concurrent.futures import ThreadPoolExecutor
S = os.path.dirname(os.path.abspath(__file__))
COMP, H, A = sys.argv[1], sys.argv[2].lower(), sys.argv[3].lower()
BER = datetime.timezone(datetime.timedelta(hours=1))

def get(path, **q):
    out = subprocess.run([S + '/oa.sh', path] + [f'{k}={v}' for k, v in q.items()],
                         capture_output=True, text=True).stdout
    body, code = out.rsplit('\n__HTTP', 1)
    if code.strip() != '200':
        sys.exit(f'HTTP {code.strip()} bei {path}')
    return json.loads(body)

up = get('fixtures/upcoming', competitions=COMP).get('data', [])
c = [f for f in up if H in f['home_name'].lower() and A in f['away_name'].lower()]
if not c:
    sys.exit('Spiel nicht gefunden – Teilnamen/Wettbewerb prüfen')
f = sorted(c, key=lambda f: f['unix'])[0]
fid = f['id']
print(f"## {f['home_name']} – {f['away_name']} · Anstoß "
      f"{datetime.datetime.fromtimestamp(f['unix'], BER).strftime('%d.%m.%Y %H:%M')} · fixture_id {fid}")

for t in get(f'stats/fixture/{fid}').get('data', []):
    def g(k, s='total'): return t.get(k, {}).get(s)
    def p(k, s): return t.get(k, {}).get(f'{s}_percentage')
    side = 'home' if t['name'] == f['home_name'] else 'away'
    print(f"### {t['name']}")
    for s, lab in (('total', 'gesamt'), (side, 'Heim' if side == 'home' else 'auswärts')):
        o25 = t.get('goals_over', {}).get('o2', {}).get(f'{s}_percentage')
        print(f"  {lab:8} Sp {g('played', s)} · S-U-N {g('won', s)}-{g('drawn', s)}-{g('lost', s)} · "
              f"Tore {g('goals_for', s)}:{g('goals_against', s)} · o2.5 {o25}% · BTTS {p('btts', s)}% · "
              f"zu null {g('clean_sheet', s)} · ohne Tor {g('failed_to_score', s)} · "
              f"xG {t.get('xg_for', {}).get(s + '_avg')}:{t.get('xg_against', {}).get(s + '_avg')}")

def page(n):
    return get('trends/btts', page=n).get('data', [])
first = get('trends/btts', page=1)
pages = first.get('info', {}).get('pages', 1)
rows = first.get('data', [])
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(page, range(2, pages + 1)):
        rows += r
m = [r for r in rows if r.get('id') == fid]
if m:
    pr = m[0]['probability']
    print(f"Odd-Alerts-Modell (nur Vergleich): Heim {pr.get('home_win')} · Remis {pr.get('draw')} · "
          f"Ausw. {pr.get('away_win')} · BTTS {pr.get('btts')} · o2.5 {pr.get('o25')} · u2.5 {pr.get('u25')}")
else:
    print('Odd-Alerts-Modell: fehlt')
