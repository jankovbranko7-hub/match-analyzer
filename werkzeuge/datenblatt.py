#!/usr/bin/env python3
"""Datenblatt-Werkzeug (Sports-Mole-Check 1.4, Hebel 1 – Wunsch des Nutzers vom 27.11.2026).

Ein Aufruf liefert für eine Paarung alle gezählten Fakten für Schritt 2, 3 und 4b – das Werkzeug zählt,
der Agent bewertet. Nur Sports Mole und FootyStats; keine Quoten, keine Vorab-Werte, keine Direktvergleiche.

Aufruf (aus dem Repo-Wurzelordner):
  python3 -I werkzeuge/datenblatt.py <saison> "<FS-Heim>" "<FS-Gast>" [Optionen]
Optionen:
  --sm "<SM-Heim>" "<SM-Gast>"   SM-Teilnamen wie bei sm_spiel.py (für Formdaten aller Wettbewerbe = Rang-2-Block)
  --sm-seite <URL>               stattdessen direkt die SM-Spielseite (…_game_N.html), z. B. wenn die Vorschau nicht mehr
                                 in der Übersicht steht
  --spieler-heim "A,B,C"         Spieler aus den Teamnews des Heimteams (Regel 7b/7c)
  --spieler-gast "D,E"           dito Gastteam
  --ep <saison>                  Europapokal-Saison (CL 17128, EL 17127, ECL 17130): zusätzlicher Block Ligaphase
Ausgabe: Markdown auf stdout (zum Einfügen in die Tagesliste, Datenblatt-Felder 1–4 und 7, Spieler für Feld 5).

Grenzen (immer selbst prüfen): Teamnews-Status nach Originalwort liest weiter der Agent aus dem SM-Artikel; Pokalspiele
und ihre Aufstellungen führt FS meist nicht (nur SM-Formdaten); SM zeigt nicht ausgetragene Spiele teils als 0:0
(das Werkzeug meldet Abweichungen SM ↔ FS); die Gegner-Zuordnung SM → FS-Tabelle geht über Namensähnlichkeit.
"""
import datetime
import functools
import json
import os
import re
import subprocess
import sys
import unicodedata

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
BER = datetime.timezone(datetime.timedelta(hours=1))
# erster Abstiegsplatz, Relegationsplatz je FS-Saison (sonst „nicht in der Quelle“)
ABSTIEG = {17146: (18, None), 17199: (18, None), 17084: (18, None), 17210: (17, 16), 17212: (17, 16),
           17102: (17, 16), 17184: (22, None), 17180: (21, None), 17097: (17, 16), 17148: (12, 11)}


@functools.lru_cache(None)
def get(path, **q):
    out = subprocess.run([S + "/fs.sh", path] + [f"{k}={v}" for k, v in sorted(q.items())],
                         capture_output=True, text=True).stdout
    body, code = out.rsplit("\n__HTTP", 1)
    if code.strip() != "200":
        sys.exit(f"FootyStats HTTP {code.strip()} bei {path} – Zugriff prüfen und dem Nutzer melden.")
    return json.loads(body)


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s)


def toks(s):
    stop = {"fc", "cf", "sc", "cd", "cs", "ud", "ac", "afc", "sk", "fk", "the", "de", "club", "sv", "vfb", "vfl", "us"}
    return {t for t in norm(s).split() if t not in stop and len(t) > 1}


def dt(m):
    return datetime.datetime.fromtimestamp(m["date_unix"], BER)


def tabelle(ms):
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
    return order, pts, gd, gf, nm, pl


def finde_team(ms, teil):
    namen = {}
    for m in ms:
        namen[m["homeID"]] = m["home_name"]
        namen[m["awayID"]] = m["away_name"]
    exakt = [t for t, n in namen.items() if norm(n).strip() == norm(teil).strip()]
    if exakt:
        return exakt[0], namen[exakt[0]]
    treffer = [t for t, n in namen.items() if norm(teil).strip() in norm(n)]
    if len(treffer) != 1:
        sys.exit(f"Team „{teil}“ nicht eindeutig in FS gefunden: {[namen[t] for t in treffer] or 'keins'}")
    return treffer[0], namen[treffer[0]]


def sicht(spiel, team_ist_heim):
    """spiel = (heim, gast, th, ta, wb, quelle, datum) → (eigene, gegner, Gegnername, H/A)."""
    h, g, th, ta = spiel[:4]
    return (th, ta, g, "H") if team_ist_heim else (ta, th, h, "A")


def block(zeilen, titel):
    """zeilen: [(datum, H/A, Gegner, eigene, gegen, wb)] neuestes zuerst."""
    n = len(zeilen)
    if not n:
        return [f"- {titel}: keine Spiele"]
    w = sum(e > g for _, _, _, e, g, _ in zeilen)
    d = sum(e == g for _, _, _, e, g, _ in zeilen)
    l = n - w - d
    tf = sum(e for *_, e, g, _ in zeilen)
    ta = sum(g for *_, e, g, _ in zeilen)
    def liste(bed):
        return [f"{e}:{g}" for _, _, _, e, g, _ in zeilen if bed(e, g)]
    ov, bt = liste(lambda e, g: e + g > 2), liste(lambda e, g: e > 0 and g > 0)
    tor, ohne = liste(lambda e, g: e > 0), liste(lambda e, g: e == 0)
    gt, zn = liste(lambda e, g: g > 0), liste(lambda e, g: g == 0)
    drei = liste(lambda e, g: e >= 3)
    sp = " · ".join(f"{d_} {ha} {o} {e}:{g}{'' if wb == 'Liga' else ' (' + wb + ')'}" for d_, ha, o, e, g, wb in zeilen)
    return [f"- **{titel}** ({n} Sp.): {w}-{d}-{l}, {tf}:{ta} · über 2,5 {len(ov)}/{n} ({', '.join(ov) or '–'}) · "
            f"beide treffen {len(bt)}/{n} (Spiel) · Tor {len(tor)}/{n}, ohne Tor {len(ohne)}/{n} ({', '.join(ohne) or '–'}) · "
            f"Gegentor {len(gt)}/{n}, zu null {len(zn)}/{n} ({', '.join(zn) or '–'}) (Team) · 3+ eigene Tore "
            f"{len(drei)}-mal ({', '.join(drei) or '–'})",
            f"  - Spiele (Sicht des Teams, eigene:gegen, neuestes zuerst): {sp}"]


def serien(zeilen, titel):
    """Serien vom neuesten Spiel aus."""
    def lauf(bed):
        k = 0
        for z in zeilen:
            if bed(z[3], z[4]):
                k += 1
            else:
                break
        return k
    def letzt(bed):
        for z in zeilen:
            if bed(z[3], z[4]):
                return f"{z[0]} {z[1]} {z[2]} {z[3]}:{z[4]}"
        return f"nicht in den {len(zeilen)} Spielen"
    return (f"- **Serien {titel}** (vom letzten Spiel an): Tor in Folge {lauf(lambda e, g: e > 0)} · ohne Tor in Folge "
            f"{lauf(lambda e, g: e == 0)} · zu null in Folge {lauf(lambda e, g: g == 0)} · Gegentor in Folge "
            f"{lauf(lambda e, g: g > 0)} · ungeschlagen {lauf(lambda e, g: e >= g)} · sieglos {lauf(lambda e, g: e <= g)} · "
            f"letzter Sieg: {letzt(lambda e, g: e > g)} · letztes Tor: {letzt(lambda e, g: e > 0)}")


def spieler_index(sid):
    idx, page = {}, 1
    while True:
        r = get("league-players", season_id=sid, page=page)
        for p in r["data"]:
            idx[p["id"]] = p
        if page >= r.get("pager", {}).get("max_page", 1):
            return idx
        page += 1


def aufstellung(mid, tid, idx):
    d = get("match", match_id=mid)["data"]
    seite = "team_a" if d["homeID"] == tid else "team_b"
    nm = lambda i: (idx.get(i) or {}).get("known_as") or (idx.get(i) or {}).get("full_name") or f"ID {i}"
    st = {p["player_id"]: "Startelf" for p in (d.get("lineups") or {}).get(seite, [])}
    for b in (d.get("bench") or {}).get(seite, []):
        if b["player_out_id"] != -1:
            st[b["player_in_id"]] = f"eingewechselt {b['player_out_time']} für {nm(b['player_out_id'])}"
            if b["player_out_id"] in st and st[b["player_out_id"]] == "Startelf":
                st[b["player_out_id"]] = f"Startelf, ausgewechselt {b['player_out_time']}"
        else:
            st[b["player_in_id"]] = "Bank, ungenutzt"
    ev = {}
    for side in ("team_a", "team_b"):
        for p in (d.get("lineups") or {}).get(side, []):
            if side == seite and p.get("player_events"):
                ev[p["player_id"]] = ", ".join(f"{e['event_type']} {e['event_time']}" for e in p["player_events"])
    return st, ev, nm


def team_teil(label, tid, name, ms, order, pts, gd, pl, nm_t, sid, sm_spiele, spieler, idx):
    out = [f"### Datenblatt {name} ({label}, FS-Team-ID {tid})"]
    p = order.index(tid) + 1
    n_teams = len(order)
    pos = {t: i + 1 for i, t in enumerate(order)}
    # 1. Tabelle
    ab, rel = ABSTIEG.get(sid, (None, None))
    nachbarn = " | ".join(f"{i + 1}. {nm_t[t]} {pts[t]} ({pl[t]} Sp, TD {gd[t]:+d})" for i, t in enumerate(order) if abs(i + 1 - p) <= 2)
    z = [f"1. **Tabelle (aus FS-Spielen; mit SM-Tabelle abgleichen, Punktabzüge zählt FS nicht):** Platz {p} von {n_teams}, "
         f"{pts[tid]} Pkt aus {pl[tid]} Sp ({pts[tid] / pl[tid]:.2f} je Spiel), TD {gd[tid]:+d}. Nachbarn: {nachbarn}."]
    abst = [f"Platz 1: {pts[order[0]] - pts[tid]:+d} Pkt" if p > 1 else "selbst Platz 1"]
    if p > 1:
        abst.append(f"Platz {p - 1}: {pts[order[p - 2]] - pts[tid]:+d}")
    if p < n_teams:
        abst.append(f"Platz {p + 1}: {pts[order[p]] - pts[tid]:+d}")
    for lab, pl_ in (("Relegationsplatz", rel), ("erster Abstiegsplatz", ab)):
        if pl_:
            abst.append(f"{lab} {pl_}: {pts[order[pl_ - 1]] - pts[tid]:+d}")
    if not ab:
        abst.append("Abstiegsplätze: nicht in der Quelle (Werkzeug kennt sie für diese Liga nicht)")
    z.append("   Abstände (Punkte des Platzes minus eigene): " + " · ".join(abst))
    out += z
    # Ligaspiele
    mine = sorted([m for m in ms if tid in (m["homeID"], m["awayID"])], key=lambda m: m["date_unix"])
    done = [m for m in mine if m["status"] == "complete"]
    nicht = [m for m in mine if m["status"] not in ("complete", "incomplete")]
    def zl(m):
        h = m["homeID"] == tid
        e, g = (m["homeGoalCount"], m["awayGoalCount"]) if h else (m["awayGoalCount"], m["homeGoalCount"])
        geg = m["awayID"] if h else m["homeID"]
        return (f"{dt(m):%d.%m.}", "H" if h else "A", f"{nm_t.get(geg, '?')} (Pl. {pos.get(geg, '?')})", e, g, "Liga")
    liga = [zl(m) for m in reversed(done)]
    out.append("2./4. **Zahlen mit Bezug** (FS; Spiel = über 2,5 / beide treffen, Team = Tor / Gegentor / zu null):")
    out += block(liga[:6], "letzte 6 Liga")
    if sm_spiele:
        out += block(sm_spiele[:6], "letzte 6 alle Wb. (SM-Formdaten; Ligaspiele mit FS abgeglichen)")
    else:
        out.append("- letzte 6 alle Wb.: ohne --sm nicht erstellt (Pokalspiele nur über SM)")
    heim = [zl(m) for m in reversed(done) if m["homeID"] == tid]
    ausw = [zl(m) for m in reversed(done) if m["awayID"] == tid]
    out += block(heim, "Liga daheim Saison (Rang 3)")
    out += block(ausw, "Liga auswärts Saison (Rang 3)")
    out += block(heim[:5], "Liga letzte 5 daheim")
    out += block(ausw[:5], "Liga letzte 5 auswärts")
    out.append("3. **Letzter Sieg, letztes Tor, Serien:**")
    out.append(serien(liga, "Liga (FS)"))
    if sm_spiele:
        out.append(serien(sm_spiele, "alle Wb. (SM, nur letzte 6)"))
    if nicht:
        out.append("- NICHT AUSGETRAGEN (nicht zählen): " + " | ".join(
            f"{dt(m):%d.%m.} {m['home_name']} – {m['away_name']} ({m['status']})" for m in nicht))
    # 4b Gegnerstärke
    basis = sm_spiele[:6] if sm_spiele else liga[:6]
    oben = [z_ for z_ in basis if re.search(r"Pl\. (\d+)", z_[2]) and int(re.search(r"Pl\. (\d+)", z_[2]).group(1)) <= n_teams // 2]
    unten = [z_ for z_ in basis if re.search(r"Pl\. (\d+)", z_[2]) and int(re.search(r"Pl\. (\d+)", z_[2]).group(1)) > n_teams // 2]
    rest = [z_ for z_ in basis if z_ not in oben and z_ not in unten]
    def kurz(zs):
        if not zs:
            return "keine"
        w = sum(e > g for *_, e, g, _ in zs); d = sum(e == g for *_, e, g, _ in zs)
        return (f"{len(zs)} Sp. {w}-{d}-{len(zs) - w - d}, {sum(e for *_, e, g, _ in zs)}:{sum(g for *_, e, g, _ in zs)} "
                f"(ohne Tor {sum(e == 0 for *_, e, g, _ in zs)}, zu null {sum(g == 0 for *_, e, g, _ in zs)}) – "
                + ", ".join(f"{z_[2]} {z_[3]}:{z_[4]}" for z_ in zs))
    out.append(f"4b. **Gegnerstärke der letzten 6** ({'alle Wb.' if sm_spiele else 'Liga'}; obere Hälfte = Platz 1–{n_teams // 2}):")
    out.append(f"- gegen obere Hälfte: {kurz(oben)}")
    out.append(f"- gegen untere Hälfte: {kurz(unten)}")
    out.append(f"- Gegner ohne Liga-Platz (Pokal/andere Liga): {kurz(rest)}")
    # 7 weitere Fakten
    nx = [m for m in mine if m["status"] == "incomplete"][:2]
    out.append("7. **Spiele davor/danach (Liga, FS):** letztes " + (f"{dt(done[-1]):%d.%m.}" if done else "–") + " · nächste: "
               + " | ".join(f"{dt(m):%d.%m. %H:%M} {m['home_name']} – {m['away_name']}" for m in nx)
               + (" · Pokalspiele: siehe SM-Formdaten (Datum steht dort nicht)" if sm_spiele and any(z_[5] != "Liga" for z_ in sm_spiele[:6]) else ""))
    # 5. Spieler / 7c
    letzte = [m for m in reversed(done)][:2]
    if letzte:
        st0, ev0, nmf = aufstellung(letzte[0]["id"], tid, idx)
        startelf = [nmf(i) for i, s in st0.items() if s.startswith("Startelf")]
        out.append(f"5. **Startelf letztes Ligaspiel** ({dt(letzte[0]):%d.%m.}, match {letzte[0]['id']}): " + ", ".join(startelf))
        if spieler:
            out.append("   **Spieler aus den Teamnews (Regel 7b/7c – Status nach Originalwort trägt der Agent ein):**")
            auf = [(m, aufstellung(m["id"], tid, idx)) for m in letzte]
            kand = [p_ for p_ in idx.values() if p_.get("club_team_id") == tid]
            # Spieler, die in den Aufstellungen stehen, auch ohne club_team_id
            ids_auf = set()
            for _, (st, _, _) in auf:
                ids_auf |= set(st)
            kand += [idx[i] for i in ids_auf if i in idx and idx[i] not in kand]
            for name in spieler:
                hits = [p_ for p_ in kand if norm(name).strip() and all(t in norm(p_.get("full_name", "") + " " + (p_.get("known_as") or "")) for t in norm(name).split())]
                if not hits:
                    out.append(f"   - {name}: in FS nicht gefunden (normalisiert gesucht) – Position nicht in der Quelle (FS); "
                               f"nur SM-Artikel/mögliche Startelf verwenden")
                    continue
                for p_ in hits[:2]:
                    stat = []
                    for m, (st, ev, _) in auf:
                        s_ = st.get(p_["id"], "nicht im Kader")
                        e_ = ev.get(p_["id"])
                        stat.append(f"{dt(m):%d.%m.}: {s_}{' [' + e_ + ']' if e_ else ''}")
                    neu = st0.get(p_["id"], "nicht im Kader")
                    hinweis = ("spielte im letzten Ligaspiel → bei fehlt/fraglich/gesperrt NEU" if neu.startswith(("Startelf", "eingewechselt"))
                               else "spielte im letzten Ligaspiel nicht → bei fehlt/fraglich NICHT NEU; bei „zurück“ nur neu, wenn die Quelle klar „startet/spielt“ sagt")
                    out.append(f"   - {p_.get('known_as') or p_['full_name']}: {p_.get('position')}, {p_.get('appearances_overall')} Eins., "
                               f"{p_.get('goals_overall')} Tore · " + " · ".join(stat) + f" → {hinweis}")
            out.append("   Achtung: Pokal-Aufstellungen führt FS meist nicht – war das letzte Pflichtspiel ein Pokalspiel, 7c dort laut SM prüfen.")
    return out


def sm_formdaten(sm_heim, sm_gast, seite=None):
    import sm_spiel as sm
    if seite:
        pfad = re.sub(r"^https?://[^/]+", "", seite)
        return sm.formdaten(sm.hole(pfad)), pfad.split("/")[2], None
    h_, g_ = (s.lower().replace(" ", "-") for s in (sm_heim, sm_gast))
    treffer = [t[4] for t in sm.liste() if h_ in t[4].lower() and g_ in t[4].lower()]
    if not treffer:
        return None, None, "SM-Vorschau nicht gefunden"
    h = sm.hole(treffer[0])
    m = re.search(r'For data analysis[^<]*<a href="(/football/[^"]*_game_\d+\.html)"', h)
    if not m:
        return None, None, "SM-Spielseite nicht verlinkt"
    liga = m.group(1).split("/")[2]
    fd = sm.formdaten(sm.hole(m.group(1)))
    return fd, liga, None


def sm_zu_zeilen(spiele, liga_slug, fs_done, tid, nm_t, pos, abw):
    """SM-Formdaten (neuestes zuerst) → Zeilen; Ligaspiele werden über Gegner + FS abgeglichen."""
    # Teamname im SM-Format = der Name, der in allen Spielen vorkommt
    namen = None
    for _, _, a, _, _, b in spiele:
        namen = {a, b} if namen is None else namen & {a, b}
    team_sm = sorted(namen)[0] if namen and len(namen) == 1 else None
    fs_liga = sorted(fs_done, key=lambda m: -m["date_unix"])
    zeilen = []
    for wb, sun, a, x, y, b in spiele:
        ist_heim = (a == team_sm) if team_sm else True
        e, g, geg = (x, y, b) if ist_heim else (y, x, a)
        ha = "H" if ist_heim else "A"
        if wb == liga_slug:
            # passenden FS-Spiel suchen: gleicher Ort, Gegner mit größter Namensähnlichkeit
            best = None
            for m in fs_liga:
                h = m["homeID"] == tid
                if (ha == "H") != h:
                    continue
                gname = m["away_name"] if h else m["home_name"]
                sc = len(toks(gname) & toks(geg))
                if sc and (best is None or sc > best[0]):
                    best = (sc, m)
                    if sc:
                        break
            if best:
                m = best[1]
                h = m["homeID"] == tid
                fe, fg = (m["homeGoalCount"], m["awayGoalCount"]) if h else (m["awayGoalCount"], m["homeGoalCount"])
                gid = m["awayID"] if h else m["homeID"]
                if (fe, fg) != (e, g):
                    abw.append(f"{nm_t.get(tid)}: SM {ha} {geg} {e}:{g} ≠ FS {dt(m):%d.%m.} {fe}:{fg} (Status {m['status']}) – "
                               f"SM-Platzhalter? FS-Wert verwendet")
                    e, g = fe, fg
                zeilen.append((f"{dt(m):%d.%m.}", ha, f"{nm_t.get(gid, geg)} (Pl. {pos.get(gid, '?')})", e, g, "Liga"))
                fs_liga.remove(m)
                continue
            abw.append(f"{nm_t.get(tid)}: SM-Ligaspiel {ha} {geg} {e}:{g} in FS nicht zugeordnet")
            zeilen.append(("?", ha, f"{geg} (Pl. ?)", e, g, "Liga"))
        else:
            zeilen.append(("Datum n. i. Q.", ha, f"{geg} (anderer Wb.)", e, g, wb))
    return zeilen


def main():
    a = sys.argv[1:]
    if len(a) < 3:
        sys.exit(__doc__)
    sid, fh, fg = int(a[0]), a[1], a[2]
    opt = {"--sm": None, "--sm-seite": None, "--spieler-heim": "", "--spieler-gast": "", "--ep": None}
    i = 3
    while i < len(a):
        if a[i] == "--sm":
            opt["--sm"] = (a[i + 1], a[i + 2]); i += 3
        elif a[i] in opt:
            opt[a[i]] = a[i + 1]; i += 2
        else:
            sys.exit(f"Unbekannte Option {a[i]}")
    ms = get("league-matches", season_id=sid, max_per_page=1000)["data"]
    th, nh = finde_team(ms, fh)
    tg, ng = finde_team(ms, fg)
    order, pts, gd, gf, nm_t, pl = tabelle(ms)
    pos = {t: k + 1 for k, t in enumerate(order)}
    spiel = [m for m in ms if m["homeID"] == th and m["awayID"] == tg and m["status"] == "incomplete"]
    jetzt = datetime.datetime.now(BER)
    print(f"## Datenblatt-Werkzeug · {nh} – {ng} · FS-Saison {sid} · erstellt {jetzt:%d.%m.%Y %H:%M} (deutsche Zeit)")
    if spiel:
        print(f"- FS-Spiel: match_id {spiel[0]['id']}, Anstoß {dt(spiel[0]):%d.%m.%Y %H:%M} (deutsche Zeit), Spieltag {spiel[0].get('game_week')}")
    else:
        print("- FS-Spiel: kein offenes Spiel dieser Paarung in der Saison gefunden – Termin prüfen")
    abw, sm_z = [], {th: None, tg: None}
    if opt["--sm"] or opt["--sm-seite"]:
        fd, liga_slug, fehler = sm_formdaten(*(opt["--sm"] or (None, None)), seite=opt["--sm-seite"])
        if fehler:
            print(f"- SM: {fehler}")
        elif fd and len(fd) == 2:
            done = {t: [m for m in ms if m["status"] == "complete" and t in (m["homeID"], m["awayID"])] for t in (th, tg)}
            sm_z[th] = sm_zu_zeilen(fd[0][1], liga_slug, done[th], th, nm_t, pos, abw)
            sm_z[tg] = sm_zu_zeilen(fd[1][1], liga_slug, done[tg], tg, nm_t, pos, abw)
            print(f"- SM-Formdaten gelesen (Liga-Slug {liga_slug}); Ligaspiele mit FS abgeglichen.")
    print("- **Abweichungen SM ↔ FS:** " + ("; ".join(abw) if abw else "keine in den Formdaten (Tabellenplatz mit SM-Tabelle selbst abgleichen)"))
    idx = spieler_index(sid)
    sp_h = [s.strip() for s in opt["--spieler-heim"].split(",") if s.strip()]
    sp_g = [s.strip() for s in opt["--spieler-gast"].split(",") if s.strip()]
    for label, t, n, sm_, sp in (("Heim", th, nh, sm_z[th], sp_h), ("Gast", tg, ng, sm_z[tg], sp_g)):
        print()
        print("\n".join(team_teil(label, t, n, ms, order, pts, gd, pl, nm_t, sid, sm_, sp, idx)))
    # 4b Tabellenvergleich
    print("\n### Kräfteverhältnis – Tabellenvergleich (Schritt 4b, Teil 1)")
    print(f"- {nh}: Platz {pos[th]}, {pts[th]} Pkt ({pts[th] / pl[th]:.2f} je Spiel) · {ng}: Platz {pos[tg]}, {pts[tg]} Pkt "
          f"({pts[tg] / pl[tg]:.2f} je Spiel) · Abstand {abs(pos[th] - pos[tg])} Plätze, {abs(pts[th] - pts[tg])} Punkte.")
    print("- Einstufung (klarer Favorit / ausgeglichen / nicht eindeutig) trifft der Agent mit Tabelle, beiden Rang-2-Blöcken "
          "und Gegnerstärke (oben je Team).")
    if opt["--ep"]:
        eu = get("league-matches", season_id=int(opt["--ep"]), max_per_page=1000)["data"]
        eu = [m for m in eu if dt(m) >= datetime.datetime(2026, 9, 1, tzinfo=BER)]
        o2, p2, g2, f2, n2, l2 = tabelle(eu)
        print(f"\n### Europapokal-Ligaphase (Saison {opt['--ep']}; Tabelle aus FS-Spielen, UEFA-Reihenfolge kann abweichen)")
        for nmx in (nh, ng):
            t2 = [t for t, n_ in n2.items() if toks(n_) & toks(nmx)]
            if not t2:
                print(f"- {nmx}: in der Ligaphase nicht gefunden"); continue
            t2 = t2[0]
            mine = sorted([m for m in eu if t2 in (m["homeID"], m["awayID"]) and m["status"] == "complete"], key=lambda m: -m["date_unix"])
            zz = []
            for m in mine:
                h = m["homeID"] == t2
                e, g = (m["homeGoalCount"], m["awayGoalCount"]) if h else (m["awayGoalCount"], m["homeGoalCount"])
                zz.append((f"{dt(m):%d.%m.}", "H" if h else "A", n2[m["awayID"] if h else m["homeID"]], e, g, "Liga"))
            print(f"- {n2[t2]}: Platz {o2.index(t2) + 1} von {len(o2)}, {p2[t2]} Pkt")
            print("\n".join(block(zz, "alle Spiele Ligaphase")))
    print("\n_Werkzeug zählt nur; Teamnews-Status (Originalwort), Lage-Check, Einstufung, Märkte und Tipp trifft der Agent._")


if __name__ == "__main__":
    main()
