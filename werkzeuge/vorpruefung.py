#!/usr/bin/env python3
"""Vorprüfung (Ergänzung zu Sports-Mole-Check 1.4.1, Wunsch des Nutzers vom 28.11.2026).

Zählt für alle Spiele einer Liga an einem Tag, die eine Sports-Mole-Vorschau haben, nur die **Zahlenseite**
(FootyStats + SM-Formdaten): die vier Bausteine des Kräfteverhältnisses (Schritt 4b), den Spielort und die
Tor-Zahlen der letzten 6. Ohne Agenten, ohne Teamnews, ohne Lage – **kein Tipp**. Das Werkzeug bewertet nichts;
den Satz „Zahlen zeigen zu: …“ schreibt Claude, die 5 Spiele wählt der Nutzer.

Aufruf (aus dem Repo-Wurzelordner):
  python3 -I werkzeuge/vorpruefung.py "<Liga-Teilname wie in der SM-Übersicht>" [Wochentag] [--saison <FS-Saison>]
Beispiele:
  python3 -I werkzeuge/vorpruefung.py "Premier League" Saturday
  python3 -I werkzeuge/vorpruefung.py "Turkish Super Lig" --saison 17265
Ohne Wochentag: der erste Tag der SM-Übersicht (heute). --saison nur nötig, wenn das Werkzeug die Liga nicht kennt.
Keine Quoten, keine Vorab-Werte, keine Direktvergleiche, kein „We say“.
"""
import datetime
import os
import re
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
import datenblatt as db  # noqa: E402
import sm_spiel as sm  # noqa: E402

# Liga-Name der SM-Übersicht → FS-Saison 2026/27 (FOOTYSTATS-API.md)
LIGA = {"premier league": 17146, "championship": 17184, "league one": 17180, "scottish premiership": 17148,
        "la liga": 17199, "serie a": 17084, "bundesliga": 17210, "2. bundesliga": 17212, "ligue 1": 17102,
        "ligue 2": 17117, "eredivisie": 17097, "primeira liga": 17217, "turkish super lig": 17265,
        "serie b": 17404, "champions league": 17128, "europa league": 17127, "conference league": 17130}


def kennz(zs):
    n = len(zs)
    w = sum(e > g for *_, e, g, _ in zs)
    d = sum(e == g for *_, e, g, _ in zs)
    return dict(n=n, sun=f"{w}-{d}-{n - w - d}", tore=f"{sum(e for *_, e, g, _ in zs)}:{sum(g for *_, e, g, _ in zs)}",
                ue=sum(e + g > 2 for *_, e, g, _ in zs), bt=sum(e > 0 and g > 0 for *_, e, g, _ in zs),
                ohne=sum(e == 0 for *_, e, g, _ in zs), zn=sum(g == 0 for *_, e, g, _ in zs),
                drei=[f"{e}:{g}" for *_, e, g, _ in zs if e >= 3])


def form(k):
    return f"{k['sun']}, {k['tore']}" if k["n"] else "keine Spiele"


def tore(name, liga, alle):
    def t(k):
        return (f"über 2,5 {k['ue']}/{k['n']}, beide treffen {k['bt']}/{k['n']}, ohne Tor {k['ohne']}/{k['n']}, "
                f"zu null {k['zn']}/{k['n']}, 3+ eigene Tore {len(k['drei'])}-mal{' (' + ', '.join(k['drei']) + ')' if k['drei'] else ''}")
    return f"{name}: Liga {t(liga)}" + (f" · alle Wb. {t(alle)}" if alle else " · alle Wb.: SM-Formdaten fehlen")


def staerke(zs, n_teams):
    def pl(z):
        m = re.search(r"Pl\. (\d+)", z[2])
        return int(m.group(1)) if m else None
    teile = []
    for lab, sub in (("oben", [z for z in zs if pl(z) and pl(z) <= n_teams // 2]),
                     ("unten", [z for z in zs if pl(z) and pl(z) > n_teams // 2]),
                     ("ohne Liga-Platz", [z for z in zs if not pl(z)])):
        teile.append(f"{lab} {form(kennz(sub))}" if sub else f"{lab} –")
    return ", ".join(teile)


def finde_fs_spiel(ms, sm_heim, sm_gast):
    """Offenes FS-Spiel zur SM-Paarung: beide Namen müssen passen (ganzer Name oder starker Treffer)."""
    best = []
    for m in ms:
        if m["status"] != "incomplete":
            continue
        h, g = db.name_wert(sm_heim, m["home_name"]), db.name_wert(sm_gast, m["away_name"])
        if h[0] >= 1 and g[0] >= 1:
            best.append(((h[0] + g[0], -(h[2] + g[2]), -(h[3] + g[3]), -m["date_unix"]), m))
    best.sort(key=lambda t: t[0], reverse=True)
    return best[0][1] if best else None


def main():
    a = sys.argv[1:]
    saison = None
    if "--saison" in a:
        i = a.index("--saison")
        saison = int(a[i + 1])
        a = a[:i] + a[i + 2:]
    if not a:
        sys.exit(__doc__)
    liga_teil = a[0].lower()
    alle = sm.liste()
    tag = a[1] if len(a) > 1 else (alle[0][0] if alle else "")
    spiele = [t for t in alle if tag.lower() in t[0].lower() and liga_teil in t[1].lower()]
    if not spiele:
        sys.exit(f"Keine SM-Vorschau für „{a[0]}“ am Tag „{tag}“ in der Übersicht.")
    ligen = sorted({t[1] for t in spiele})
    if len(ligen) > 1:
        sys.exit(f"Liga-Teilname nicht eindeutig: {ligen} – genauer angeben.")
    sid = saison or LIGA.get(ligen[0].lower())
    if not sid:
        sys.exit(f"Liga „{ligen[0]}“ kennt das Werkzeug nicht – mit --saison <FS-Saison> aufrufen (FOOTYSTATS-API.md).")
    start = datetime.datetime(2026, 9, 1, tzinfo=db.BER)
    ms = db.get("league-matches", season_id=sid, max_per_page=1000)["data"]
    if sid in db.EUROPAPOKAL:
        ms = [m for m in ms if db.dt(m) >= start]
    weitere = {s: (db.EP_NAME[s], [m for m in db.get("league-matches", season_id=s, max_per_page=1000)["data"] if db.dt(m) >= start])
               for s in sorted(db.EUROPAPOKAL - {sid})}
    order, pts, gd, gf, nm_t, pl = db.tabelle(ms)
    pos = {t: k + 1 for k, t in enumerate(order)}
    n_teams = len(order)
    done = [m for m in ms if m["status"] == "complete"]
    jetzt = datetime.datetime.now(db.BER)
    print(f"## Vorprüfung · {ligen[0]} · {spiele[0][0]} · FS-Saison {sid} · erstellt {jetzt:%d.%m.%Y %H:%M} (deutsche Zeit)")
    print("_Nur die Zahlenseite (FootyStats + SM-Formdaten). Keine Teamnews, keine Lage, kein Tipp. Das Werkzeug zählt nur._")
    if sid in db.EUROPAPOKAL:
        print("_Europapokal: Heimliga-Blöcke fehlen hier (nur Ligaphase und letzte 6 aller Wb.)._")
    for _, _, zeit, titel, pfad in spiele:
        try:
            sm_heim, sm_gast = [x.strip() for x in re.split(r"\s+vs\.?\s+", titel, maxsplit=1)]
        except ValueError:
            print(f"\n### {zeit} · {titel}\n- Titel nicht lesbar – von Hand prüfen")
            continue
        print(f"\n### {zeit} · {sm_heim} – {sm_gast}")
        m = finde_fs_spiel(ms, sm_heim, sm_gast)
        if not m:
            print("- FS-Spiel nicht gefunden (Namen anders geschrieben oder Spiel nicht im FS-Spielplan) – von Hand prüfen")
            continue
        th, tg = m["homeID"], m["awayID"]
        nh, ng = m["home_name"], m["away_name"]
        print(f"- FS: {nh} – {ng}, match_id {m['id']}, Anstoß {db.dt(m):%d.%m.%Y %H:%M} (deutsche Zeit)")
        if th not in pos or tg not in pos:
            print("- Ein Team hat noch kein ausgetragenes Spiel in dieser Saison – von Hand prüfen")
            continue
        abw, hinw, smz = [], [], {th: None, tg: None}
        try:
            h = sm.hole(pfad)
            ml = re.search(r'For data analysis[^<]*<a href="(/football/[^"]*_game_\d+\.html)"', h)
            fd = sm.formdaten(sm.hole(ml.group(1))) if ml else []
            if len(fd) == 2:
                slug = ml.group(1).split("/")[2]
                smz[th] = db.sm_zu_zeilen(fd[0][1], slug, sid, th, ms, weitere, nm_t, pos, abw, hinw)
                smz[tg] = db.sm_zu_zeilen(fd[1][1], slug, sid, tg, ms, weitere, nm_t, pos, abw, hinw)
            else:
                hinw.append("SM-Formdaten nicht gefunden – Block „alle Wb.“ fehlt")
        except OSError as e:
            hinw.append(f"SM nicht erreichbar ({e}) – Block „alle Wb.“ fehlt")
        def liga_zeilen(tid, nur=None):
            out = []
            for x in sorted(done, key=lambda x: -x["date_unix"]):
                if tid not in (x["homeID"], x["awayID"]):
                    continue
                hh, e, g, gid, gname = db.sp_sicht(x, tid)
                if nur is not None and hh != nur:
                    continue
                out.append((f"{db.dt(x):%d.%m.}", "H" if hh else "A", f"{gname} (Pl. {pos.get(gid, '?')})", e, g, "Liga"))
            return out
        lh, lg = liga_zeilen(th), liga_zeilen(tg)
        kh, kg = kennz(lh[:6]), kennz(lg[:6])
        ah = kennz(smz[th][:6]) if smz[th] else None
        ag = kennz(smz[tg][:6]) if smz[tg] else None
        print(f"- (a) Tabelle: Heim Platz {pos[th]}, {pts[th] / pl[th]:.2f} Pkt je Spiel ({pts[th]} aus {pl[th]}) · Gast Platz {pos[tg]}, "
              f"{pts[tg] / pl[tg]:.2f} ({pts[tg]} aus {pl[tg]}) · Abstand {abs(pos[th] - pos[tg])} Plätze, {abs(pts[th] - pts[tg])} Punkte")
        print(f"- (b) Letzte 6 alle Wb.: Heim {form(ah) if ah else 'fehlt'} · Gast {form(ag) if ag else 'fehlt'}")
        print(f"- (c) Letzte 6 Liga: Heim {form(kh)} · Gast {form(kg)}")
        print(f"- (d) Gegnerstärke der letzten 6 ({'alle Wb.' if smz[th] and smz[tg] else 'Liga'}; obere Hälfte = Platz 1–{n_teams // 2}): "
              f"Heim {staerke((smz[th] or lh)[:6], n_teams)} · Gast {staerke((smz[tg] or lg)[:6], n_teams)}")
        print(f"- Spielort (Liga, Saison): Heim daheim {form(kennz(liga_zeilen(th, True)))} · Gast auswärts {form(kennz(liga_zeilen(tg, False)))}")
        print(f"- Tore letzte 6 – {tore('Heim', kh, ah)}")
        print(f"- Tore letzte 6 – {tore('Gast', kg, ag)}")
        if abw:
            print("- Abweichungen SM ↔ FS: " + "; ".join(abw))
        if hinw:
            print("- Hinweise: " + "; ".join(hinw))
    print("\n_Den Satz „Zahlen zeigen zu: Heimsieg / Auswärtssieg / <Tor-Markt> / keinem – weil …“ schreibt Claude (im Zweifel „keinem“); "
          "die 5 Spiele wählt der Nutzer; danach läuft das volle System unverändert._")


if __name__ == "__main__":
    main()
