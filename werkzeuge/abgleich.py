#!/usr/bin/env python3
"""Automatischer Abgleich Sports Mole ↔ FootyStats je Paarung (Sports-Mole-Check 1.3, Schritt 2).

Aufruf:
  python3 -I werkzeuge/abgleich.py <season_id> "<SM-Heim-Teil>" "<SM-Gast-Teil>" ["<FS-Heim-Teil>" "<FS-Gast-Teil>"]

SM-Teilnamen wie bei sm_spiel.py (Sports-Mole-Schreibweise, z. B. "real-madrid" "celta");
FS-Teilnamen nur nötig, wenn FootyStats anders schreibt (Standard: dieselben Teilnamen).

Prüft je Team und meldet jede Abweichung mit „ABWEICHUNG“:
  1. Tabellenplatz Sports Mole (Tabelle) gegen FootyStats.
  2. Ligaspiele in den Sports-Mole-Formdaten (neuestes zuerst) gegen die letzten Ligaspiele bei
     FootyStats: Reihenfolge, Heim/Auswärts, Spielstand.
  3. Letzte 6 aller Wettbewerbe: S-U-N und Tore aus den Sports-Mole-Formdaten gegen FootyStats.
Gibt außerdem den Tabellenstand mit Abständen aus (Lage-Check Frage 1 und 2).
Keine Quoten, kein Rechenmodell, keine Direktvergleiche, kein „We say“.
"""
import json
import os
import subprocess
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
import sm_spiel as sm  # noqa: E402

# Erster Platz, der Abstieg bzw. Relegation bedeutet (Ligagröße aus der Tabelle)
ABSTIEG = {
    "premier-league": (18, None), "la-liga": (18, None), "serie-a": (18, None),
    "bundesliga": (17, 16), "ligue-1": (17, 16), "championship": (22, None),
    "league-one": (21, None), "league-two": (23, None), "eredivisie": (17, 16),
    "scottish-premiership": (12, 11),
}


def fs_get(path, **q):
    out = subprocess.run([S + "/fs.sh", path] + [f"{k}={v}" for k, v in q.items()],
                         capture_output=True, text=True).stdout
    body, code = out.rsplit("\n__HTTP", 1)
    if code.strip() != "200":
        sys.exit(f"HTTP {code.strip()} bei {path}")
    return json.loads(body)


def tabelle(liga):
    """[(Platz, Name, Sp, Pkt)] aus der Sports-Mole-Tabelle."""
    rows = []
    for z in sm.tabelle(liga):
        t = z.split()
        if len(t) >= 10 and t[0].isdigit() and all(x.lstrip("-").isdigit() for x in t[-8:]):
            rows.append((int(t[0]), " ".join(t[1:-8]), int(t[-8]), int(t[-1])))
    return rows


def finde(rows, name):
    n = name.lower()
    for r in rows:
        if r[1].lower() == n:
            return r
    for r in rows:
        if n in r[1].lower() or r[1].lower() in n:
            return r
    w = n.split()[0]
    hit = [r for r in rows if w in r[1].lower()]
    return hit[0] if len(hit) == 1 else None


def main():
    if len(sys.argv) not in (4, 6):
        sys.exit(__doc__)
    season = sys.argv[1]
    smh, sma = (x.lower().replace(" ", "-") for x in sys.argv[2:4])
    fsh, fsa = ((sys.argv[4], sys.argv[5]) if len(sys.argv) == 6 else (sys.argv[2], sys.argv[3]))
    fsh, fsa = fsh.lower().replace("-", " "), fsa.lower().replace("-", " ")

    # Sports Mole
    treffer = [t[4] for t in sm.liste() if smh in t[4].lower() and sma in t[4].lower()]
    if not treffer:
        sys.exit("Keine Sports-Mole-Vorschau gefunden – Teilnamen prüfen.")
    h = sm.hole(treffer[0])
    import re
    m = re.search(r'For data analysis[^<]*<a href="(/football/[^"]*_game_\d+\.html)"', h)
    if not m:
        sys.exit("Keine Sports-Mole-Spielseite verlinkt – Abgleich nicht möglich (offen nennen).")
    liga = m.group(1).split("/")[2]
    fd = sm.formdaten(sm.hole(m.group(1)))
    rows = tabelle(liga)

    # FootyStats
    lm = fs_get("league-matches", season_id=season, max_per_page=1000)["data"]
    cand = [x for x in lm if fsh in x["home_name"].lower() and fsa in x["away_name"].lower()]
    if not cand:
        sys.exit("Spiel bei FootyStats nicht gefunden – FS-Teilnamen angeben.")
    cand.sort(key=lambda x: (x["status"] == "complete", x["date_unix"]))
    mm = cand[0]
    lt = {x["id"]: x for x in fs_get("league-teams", season_id=season, include="stats")["data"]}

    fehler = 0
    print(f"## Abgleich {mm['home_name']} – {mm['away_name']} (Sports Mole: {liga}, FootyStats: Saison {season})")
    for (smname, spiele), tid, fsname in zip(fd, (mm["homeID"], mm["awayID"]), (mm["home_name"], mm["away_name"])):
        print(f"\n### {smname} (FS: {fsname})")
        # 1. Tabellenplatz
        r = finde(rows, smname)
        fspos = (lt.get(tid) or {}).get("stats", {}).get("leaguePosition_overall")
        if not r:
            print(f"  ABWEICHUNG? Team in der SM-Tabelle nicht gefunden – von Hand prüfen. FS-Platz {fspos}")
            fehler += 1
        else:
            ok = str(r[0]) == str(fspos)
            fehler += not ok
            gleich_pkt = [p for p, _, _, pts in rows if pts == r[3] and p != r[0]]
            hinweis = "" if ok or not gleich_pkt else (f" (punktgleich mit Platz {', '.join(map(str, gleich_pkt))} – "
                                                       "Reihenfolge oder Stand der Tabelle prüfen)")
            print(f"  {'OK' if ok else 'ABWEICHUNG'} Tabellenplatz: SM {r[0]} · FS {fspos}{hinweis}")
            n = len(rows)
            ab, rel = ABSTIEG.get(liga, (None, None))
            pk = {p: pts for p, _, _, pts in rows}
            teile = [f"Platz {r[0]} von {n}, {r[3]} Punkte nach {r[2]} Spielen",
                     f"Abstand zu Platz 1: {pk[1] - r[3]}"]
            if r[0] > 1:
                teile.append(f"zum Platz darüber ({r[0] - 1}): {pk[r[0] - 1] - r[3]}")
            if r[0] < n:
                teile.append(f"zum Platz darunter ({r[0] + 1}): {r[3] - pk[r[0] + 1]}")
            if rel and rel in pk:
                teile.append(f"steht auf dem Relegationsplatz {rel}" if r[0] == rel
                             else f"über Relegationsplatz {rel}: {r[3] - pk[rel]}")
            if ab and ab in pk:
                if r[0] >= ab:
                    teile.append(f"steht auf einem Abstiegsplatz; Abstand zum rettenden Platz {ab - 1 if not rel else rel - 1}: "
                                 f"{pk[ab - 1 if not rel else rel - 1] - r[3]}")
                else:
                    teile.append(f"über dem ersten Abstiegsplatz {ab}: {r[3] - pk[ab]}")
            print("  Tabelle (SM): " + " · ".join(teile) + " (Punkte; negativ = darunter)")
        # 2. Ligaspiele SM gegen FS
        smliga = [(a, x, y, b) for wb, e, a, x, y, b in spiele if wb == liga]
        fsliga = sorted([x for x in lm if x["status"] == "complete" and tid in (x["homeID"], x["awayID"])],
                        key=lambda x: x["date_unix"], reverse=True)[:len(smliga)]
        for k, ((a, x, y, b), f) in enumerate(zip(smliga, fsliga), 1):
            smheim = a == smname
            fsheim = f["homeID"] == tid
            gleich = smheim == fsheim and (x, y) == (f["homeGoalCount"], f["awayGoalCount"])
            fehler += not gleich
            print(f"  {'OK' if gleich else 'ABWEICHUNG'} Ligaspiel {k} (neuestes zuerst): SM {a} {x}-{y} {b} · "
                  f"FS {f['home_name']} {f['homeGoalCount']}-{f['awayGoalCount']} {f['away_name']}")
        if len(fsliga) < len(smliga):
            print("  ABWEICHUNG: FootyStats hat weniger Ligaspiele als Sports Mole zeigt")
            fehler += 1
        # 3. Letzte 6 aller Wettbewerbe
        su = [e for _, e, *_ in spiele]
        tf = sum((x if a == smname else y) for _, _, a, x, y, _ in spiele)
        tg = sum((y if a == smname else x) for _, _, a, x, y, _ in spiele)
        smb = f"{su.count('S')}-{su.count('U')}-{su.count('N')} · Tore {tf}:{tg}"
        lx = [d for d in fs_get("lastx", team_id=tid)["data"] if d.get("last_x_match_num") == 6]
        if lx and len(spiele) == 6:
            s = lx[0]["stats"]
            fsb = (f"{s.get('seasonWinsNum_overall')}-{s.get('seasonDrawsNum_overall')}-{s.get('seasonLossesNum_overall')}"
                   f" · Tore {s.get('seasonScoredNum_overall')}:{s.get('seasonConcededNum_overall')}")
            ok = smb == fsb
            fehler += not ok
            print(f"  {'OK' if ok else 'ABWEICHUNG'} Letzte 6 alle Wb.: SM {smb} · FS {fsb}"
                  + ("" if ok else " (FootyStats erfasst evtl. nicht jeden Wettbewerb – von Hand prüfen)"))
        else:
            print(f"  Letzte 6 alle Wb.: SM {smb} ({len(spiele)} Spiele) · FS-Vergleich nicht möglich – offen nennen")
    print(f"\nErgebnis: {'keine Abweichung' if not fehler else f'{fehler} ABWEICHUNG(EN) – vermerken, nur Übereinstimmendes als Grund'}")


if __name__ == "__main__":
    main()
