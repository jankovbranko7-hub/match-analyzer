#!/usr/bin/env python3
"""Kontext eines Teams aus FootyStats (Sports-Mole-Check 1.3, Datenblatt und Prüfer).

Aufruf:
  python3 -I werkzeuge/kontext.py <team_id> <liga_saison> ["Name1,Name2"] [<europapokal_saison>]

Ohne 4. Argument (oder wenn es gleich der Liga-Saison ist) nur die Liga; sonst zusätzlich der
Europapokal (Ligaphase ab 01.09., z. B. CL 17128, EL 17127, ECL 17130).

Ausgabe je Wettbewerb: Tabelle selbst aus den FS-Spielen (Punkte, Tordifferenz, Tore – die offizielle
Reihenfolge kann abweichen) mit Nachbarn, die letzten 8 Spiele, Kennzahlen (letzte 6, daheim/auswärts
Saison, letzte 5 daheim/auswärts; über 2,5 / beide treffen je Spiel, zu null / ohne Tor je Team) und die
nächsten Spiele. Nicht ausgetragene Spiele (Status „suspended“ u. ä.) zählen nicht.
Mit Namen: Spieler des Teams (club_team_id) mit Position, Einsätzen, Minuten, Toren und letztem Einsatz.
Achtung: Das FS-Feld „letzter Einsatz“ ist teils veraltet – im Zweifel die Aufstellung im FS-`match` prüfen;
bei „nicht gefunden“ andere Schreibweisen versuchen.
Keine Quoten, keine Vorab-Werte, keine Direktvergleiche.
"""
import datetime
import functools
import json
import os
import subprocess
import sys

S = os.path.dirname(os.path.abspath(__file__))
BER = datetime.timezone(datetime.timedelta(hours=1))


@functools.lru_cache(None)
def get(path, **q):
    out = subprocess.run([S + "/fs.sh", path] + [f"{k}={v}" for k, v in sorted(q.items())],
                         capture_output=True, text=True).stdout
    body, code = out.rsplit("\n__HTTP", 1)
    if code.strip() != "200":
        sys.exit(f"HTTP {code.strip()} bei {path}")
    return json.loads(body)


def dt(m):
    return datetime.datetime.fromtimestamp(m["date_unix"], BER)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    tid, dom = int(sys.argv[1]), sys.argv[2]
    names = [n for n in (sys.argv[3] if len(sys.argv) > 3 else "").split(",") if n.strip()]
    eu = sys.argv[4] if len(sys.argv) > 4 else dom

    def fmt(m):
        return f"{dt(m):%d.%m} {m['home_name']} {m['homeGoalCount']}-{m['awayGoalCount']} {m['away_name']}"

    def stats(ms, label):
        w = d = l = gf = ga = bt = ov = cs = fts = 0
        for m in ms:
            h = m["homeID"] == tid
            f, a = (m["homeGoalCount"], m["awayGoalCount"]) if h else (m["awayGoalCount"], m["homeGoalCount"])
            gf += f; ga += a; w += f > a; d += f == a; l += f < a
            bt += f > 0 and a > 0; ov += f + a > 2; cs += a == 0; fts += f == 0
        n = len(ms)
        print(f"  {label}: Sp {n} · {w}-{d}-{l} · {gf}:{ga} · über2,5 {ov}/{n} (Spiel) · beide treffen {bt}/{n} "
              f"(Spiel) · zu null {cs}/{n} (Team) · ohne Tor {fts}/{n} (Team)")

    def table(ms):
        pts, gd, gf, nm, pl = {}, {}, {}, {}, {}
        for m in ms:
            if m["status"] != "complete":
                continue
            for t, f, a, n in ((m["homeID"], m["homeGoalCount"], m["awayGoalCount"], m["home_name"]),
                               (m["awayID"], m["awayGoalCount"], m["homeGoalCount"], m["away_name"])):
                nm[t] = n
                pts[t] = pts.get(t, 0) + (3 if f > a else 1 if f == a else 0)
                gd[t] = gd.get(t, 0) + f - a
                gf[t] = gf.get(t, 0) + f
                pl[t] = pl.get(t, 0) + 1
        order = sorted(pts, key=lambda t: (-pts[t], -gd[t], -gf[t]))
        return order, pts, gd, nm, pl

    now = datetime.datetime.now(BER).timestamp()
    wettb = [(dom, "Liga")] if eu == dom else [(dom, "Heimliga"), (eu, "Europapokal")]
    for sid, label in wettb:
        ms = get("league-matches", season_id=sid, max_per_page=1000)["data"]
        if label == "Europapokal":
            ms = [m for m in ms if dt(m) >= datetime.datetime(2026, 9, 1, tzinfo=BER)]
        mine = sorted([m for m in ms if tid in (m["homeID"], m["awayID"])], key=lambda m: m["date_unix"])
        done = [m for m in mine if m["status"] == "complete"]
        nicht = [m for m in mine if m["status"] not in ("complete", "incomplete")]
        order, pts, gd, nm, pl = table(ms)
        if tid in pts:
            p = order.index(tid)
            nb = [f"{i + 1}. {nm[t]} {pts[t]} ({pl[t]} Sp, TD {gd[t]})" for i, t in enumerate(order) if abs(i - p) <= 2]
            print(f"## {label} (Saison {sid}) – Tabelle aus FS-Spielen: Platz {p + 1} von {len(order)}, "
                  f"{pts[tid]} Pkt; Nachbarn: " + " | ".join(nb))
            if label == "Europapokal" and len(order) >= 25:
                print("   Grenzen: Platz 8 =", pts[order[7]], "Pkt · Platz 24 =", pts[order[23]],
                      "Pkt · Platz 25 =", pts[order[24]], "Pkt")
            elif label != "Europapokal":
                print("   Platz 1 =", pts[order[0]], "· Platz", len(order) - 2, "=", pts[order[-3]],
                      "· Platz", len(order) - 3, "=", pts[order[-4]])
        print("  Spiele:", " | ".join(fmt(m) for m in done[-8:]))
        if nicht:
            print("  NICHT AUSGETRAGEN (nicht zählen):",
                  " | ".join(f"{dt(m):%d.%m} {m['home_name']} – {m['away_name']} ({m['status']})" for m in nicht))
        stats(done[-6:], "letzte 6")
        stats([m for m in done if m["homeID"] == tid], "daheim Saison")
        stats([m for m in done if m["awayID"] == tid], "auswärts Saison")
        stats([m for m in done if m["homeID"] == tid][-5:], "letzte 5 daheim")
        stats([m for m in done if m["awayID"] == tid][-5:], "letzte 5 auswärts")
        nx = [m for m in mine if m["status"] == "incomplete" and m["date_unix"] >= now - 3 * 3600][:2]
        print("  nächste:", " | ".join(f"{dt(m):%d.%m %H:%M} {m['home_name']} – {m['away_name']}" for m in nx))
    if names:
        for sid, _ in wettb:
            page = 1
            while True:
                r = get("league-players", season_id=sid, page=page)
                for p in r["data"]:
                    if p.get("club_team_id") != tid:
                        continue
                    fn = (p.get("full_name", "") + " " + p.get("known_as", "")).lower()
                    if any(n.strip().lower() in fn for n in names):
                        lm = p.get("last_match_timestamp") or 0
                        last = f"{datetime.datetime.fromtimestamp(lm, BER):%d.%m.%Y}" if lm else "keiner"
                        print(f"  P[{sid}] {p.get('known_as') or p['full_name']} · {p.get('position')} · Eins "
                              f"{p.get('appearances_overall')} · Min {p.get('minutes_played_overall')} · Tore "
                              f"{p.get('goals_overall')} · letzter Einsatz {last}")
                if page >= r.get("pager", {}).get("max_page", 1):
                    break
                page += 1


if __name__ == "__main__":
    main()
