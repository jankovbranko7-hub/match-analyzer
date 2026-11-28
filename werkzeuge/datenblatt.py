#!/usr/bin/env python3
"""Datenblatt-Werkzeug (Sports-Mole-Check 1.4.1, Hebel 1 – Wunsch des Nutzers vom 27.11.2026, überarbeitet am 28.11.2026).

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
  --liga-heim <saison>           Heimliga-Saison des Heimteams (nur nötig, wenn <saison> ein Europapokal ist): ihre Spiele
  --liga-gast <saison>           zählen dann für „letztes Pflichtspiel“ (Regel 7c) und den Abgleich der SM-Formdaten
Ausgabe: Markdown auf stdout (zum Einfügen in die Tagesliste, Datenblatt-Felder 1–4 und 7, Spieler für Feld 5).

Seit 28.11.2026 (Version 1.4.1):
  - Regel 7c wird am **letzten Pflichtspiel laut FS** geprüft (Liga und Europapokal; bei Europapokal-Spielen mit
    --liga-heim/--liga-gast auch die Heimliga), nicht mehr nur am letzten Ligaspiel.
  - Abgleich SM ↔ FS **in beide Richtungen**: ein FS-Spiel, das in den SM-Formdaten fehlt, wird gemeldet und in den
    Block „letzte 6 alle Wb.“ aufgenommen; die Zuordnung prüft den ganzen Gegnernamen, Spielort und Ergebnis
    (kein Treffer mehr über ein einzelnes Namenswort wie „City“ oder „Real“).
  - „3+ eigene Tore“: Spiele außerhalb der Liga sind einzeln genannt (unterklassige Pokalgegner zählen nach 1.4.1 nicht).
  - Kräfteverhältnis: Spielort-Vergleich (Heimteam daheim / Gastteam auswärts) und „Tabellenhöher“.

Grenzen (immer selbst prüfen): Teamnews-Status nach Originalwort liest weiter der Agent aus dem SM-Artikel; nationale
Pokalspiele und ihre Aufstellungen führt FS nicht (nur SM-Formdaten, ohne Datum); SM zeigt nicht ausgetragene Spiele
teils als 0:0 (das Werkzeug meldet Abweichungen SM ↔ FS).
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
EUROPAPOKAL = {17127, 17128, 17130}  # EL, CL, ECL: Ligaphase ab 01.09. (Qualifikation nicht zählen)
EP_NAME = {17128: "Champions League", 17127: "Europa League", 17130: "Conference League"}
EP_SLUG = {"champions-league": 17128, "europa-league": 17127, "europa-conference-league": 17130,
           "conference-league": 17130}
# erster Abstiegsplatz, Relegationsplatz je FS-Saison (sonst „nicht in der Quelle“) – nur Ligen, deren Regelung feststeht
ABSTIEG = {17146: (18, None), 17199: (18, None), 17084: (18, None), 17210: (17, 16), 17212: (17, 16),
           17102: (17, 16), 17184: (22, None), 17180: (21, None), 17097: (17, 16), 17148: (12, 11),
           17217: (17, 16), 17267: (17, None), 17117: (17, 16), 17269: (19, None), 17129: (12, 11)}
UNDATIERT = "Datum n. i. Q."


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


STOP = {"fc", "cf", "sc", "cd", "cs", "ud", "ac", "afc", "sk", "fk", "the", "de", "club", "sv", "vfb", "vfl", "us"}
# SM-Kurzformen → Wörter des vollen Namens
ALIAS = {"utd": ["united"], "man": ["manchester"], "spurs": ["tottenham"], "wolves": ["wolverhampton"],
         "sheff": ["sheffield"], "weds": ["wednesday"], "nottm": ["nottingham"], "psg": ["paris", "saint", "germain"],
         "qpr": ["queens", "park", "rangers"], "boro": ["middlesbrough"]}
# Wörter, die viele Vereine teilen – allein kein Beleg für denselben Gegner
GENERISCH = {"city", "united", "real", "town", "rovers", "county", "albion", "wanderers", "athletic", "sporting",
             "borussia", "racing", "deportivo", "olympique", "inter", "st", "saint", "west", "east", "north", "south",
             "new", "la", "le", "los", "las", "union", "dynamo", "dinamo", "rangers", "park"}


def toks(s):
    return {t for t in norm(s).split() if t not in STOP and len(t) > 1}


def wort_gleich(x, y):
    k = min(len(x), len(y))
    return x == y or (k >= 3 and (x.startswith(y) or y.startswith(x))) or (k >= 5 and (x in y or y in x))


def name_wert(sm_name, fs_name):
    """Vergleich SM-Gegnername ↔ FS-Teamname → (starke Treffer, schwache Treffer, offene SM-Wörter, offene FS-Wörter)."""
    a = []
    for t in sorted(toks(sm_name)):
        a += ALIAS.get(t, [t])
    b = sorted(toks(fs_name))
    used, stark, schwach, offen = set(), 0, 0, 0
    for x in a:
        hit = next((j for j, y in enumerate(b) if j not in used and wort_gleich(x, y)), None)
        if hit is None:
            offen += 1
            continue
        used.add(hit)
        if x in GENERISCH or b[hit] in GENERISCH:
            schwach += 1
        else:
            stark += 1
    return stark, schwach, offen, len(b) - len(used)


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
    kein_pokal = {"Liga"} | set(EP_SLUG) | set(EP_NAME.values())
    drei_wb = [f"{e}:{g} {o} [{wb}]" for _, _, o, e, g, wb in zeilen if e >= 3 and wb not in kein_pokal]
    zusatz = (f"; davon nationaler Pokal/anderer Wb.: {', '.join(drei_wb)} – Spielklasse des Gegners laut Quelle prüfen, "
              f"Spiele gegen unterklassige Gegner zählen für die 3+-Regeln nicht (1.4.1)") if drei_wb else ""
    sp = " · ".join(f"{d_} {ha} {o} {e}:{g}{'' if wb == 'Liga' else ' (' + wb + ')'}" for d_, ha, o, e, g, wb in zeilen)
    return [f"- **{titel}** ({n} Sp.): {w}-{d}-{l}, {tf}:{ta} · über 2,5 {len(ov)}/{n} ({', '.join(ov) or '–'}) · "
            f"beide treffen {len(bt)}/{n} (Spiel) · Tor {len(tor)}/{n}, ohne Tor {len(ohne)}/{n} ({', '.join(ohne) or '–'}) · "
            f"Gegentor {len(gt)}/{n}, zu null {len(zn)}/{n} ({', '.join(zn) or '–'}) (Team) · 3+ eigene Tore "
            f"{len(drei)}-mal ({', '.join(drei) or '–'}{zusatz})",
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
    for p in (d.get("lineups") or {}).get(seite, []):
        if p.get("player_events"):
            ev[p["player_id"]] = ", ".join(f"{e['event_type']} {e['event_time']}" for e in p["player_events"])
    return st, ev, nm


def sp_sicht(m, tid):
    """FS-Spiel aus Sicht des Teams → (ist_heim, eigene, gegen, Gegner-ID, Gegnername)."""
    h = m["homeID"] == tid
    e, g = (m["homeGoalCount"], m["awayGoalCount"]) if h else (m["awayGoalCount"], m["homeGoalCount"])
    return h, e, g, (m["awayID"] if h else m["homeID"]), (m["away_name"] if h else m["home_name"])


def pflichtspiele(tid, ms, weitere, liga_label):
    """Alle ausgetragenen Spiele des Teams, die FS führt (Liga + weitere Wettbewerbe), neuestes zuerst: [(match, Wb.)]."""
    out = [(m, liga_label) for m in ms if m["status"] == "complete" and tid in (m["homeID"], m["awayID"])]
    for s, (label, mm) in weitere.items():
        out += [(m, label) for m in mm if m["status"] == "complete" and tid in (m["homeID"], m["awayID"])]
    return sorted(out, key=lambda x: -x[0]["date_unix"])


def team_teil(label, tid, name, ms, order, pts, gd, pl, nm_t, sid, sm_spiele, spieler, idx, pfl, liga_label):
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
        if pl_ and pl_ <= n_teams:
            abst.append(f"{lab} {pl_}: {pts[order[pl_ - 1]] - pts[tid]:+d}")
    if sid in EUROPAPOKAL and n_teams >= 25:
        abst += [f"Platz 8 (letzter Achtelfinal-Platz): {pts[order[7]] - pts[tid]:+d}",
                 f"Platz 24 (letzter Play-off-Platz): {pts[order[23]] - pts[tid]:+d}",
                 f"Platz 25: {pts[order[24]] - pts[tid]:+d} · Heimliga-Platz mit kontext.py ergänzen"]
    elif not ab:
        abst.append("Abstiegsplätze: nicht in der Quelle (Werkzeug kennt sie für diese Liga nicht – aus SM-Tabelle/Artikel belegen)")
    z.append("   Abstände (Punkte des Platzes minus eigene): " + " · ".join(abst))
    out += z
    # Ligaspiele
    mine = sorted([m for m in ms if tid in (m["homeID"], m["awayID"])], key=lambda m: m["date_unix"])
    done = [m for m in mine if m["status"] == "complete"]
    nicht = [m for m in mine if m["status"] not in ("complete", "incomplete")]
    def zl(m):
        h, e, g, geg, _ = sp_sicht(m, tid)
        return (f"{dt(m):%d.%m.}", "H" if h else "A", f"{nm_t.get(geg, '?')} (Pl. {pos.get(geg, '?')})", e, g, "Liga")
    liga = [zl(m) for m in reversed(done)]
    out.append("2./4. **Zahlen mit Bezug** (FS; Spiel = über 2,5 / beide treffen, Team = Tor / Gegentor / zu null):")
    out += block(liga[:6], "letzte 6 Liga")
    if sm_spiele:
        out += block(sm_spiele[:6], "letzte 6 alle Wb. (SM-Formdaten; mit FS abgeglichen, FS-Spiele die in SM fehlen ergänzt)")
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
        out.append(serien(sm_spiele[:6], "alle Wb. (nur letzte 6)"))
    if nicht:
        out.append("- NICHT AUSGETRAGEN (nicht zählen): " + " | ".join(
            f"{dt(m):%d.%m.} {m['home_name']} – {m['away_name']} ({m['status']})" for m in nicht))
    # 4b Gegnerstärke
    basis = sm_spiele[:6] if sm_spiele else liga[:6]
    def platz(z_):
        m_ = re.search(r"Pl\. (\d+)", z_[2])
        return int(m_.group(1)) if m_ else None
    oben = [z_ for z_ in basis if platz(z_) and platz(z_) <= n_teams // 2]
    unten = [z_ for z_ in basis if platz(z_) and platz(z_) > n_teams // 2]
    rest = [z_ for z_ in basis if not platz(z_)]
    def kurz(zs):
        if not zs:
            return "keine"
        w = sum(e > g for *_, e, g, _ in zs); d = sum(e == g for *_, e, g, _ in zs)
        return (f"{len(zs)} Sp. {w}-{d}-{len(zs) - w - d}, {sum(e for *_, e, g, _ in zs)}:{sum(g for *_, e, g, _ in zs)} "
                f"(ohne Tor {sum(e == 0 for *_, e, g, _ in zs)}, zu null {sum(g == 0 for *_, e, g, _ in zs)}) – "
                + ", ".join(f"{z_[2]} {z_[3]}:{z_[4]}" for z_ in zs))
    out.append(f"4b. **Gegnerstärke der letzten 6** ({'alle Wb.' if sm_spiele else 'Liga'}; obere Hälfte = Platz 1–{n_teams // 2}; "
               f"Tabellenplätze der Gegner sind Rang 3):")
    out.append(f"- gegen obere Hälfte: {kurz(oben)}")
    out.append(f"- gegen untere Hälfte: {kurz(unten)}")
    out.append(f"- Gegner ohne Liga-Platz (Pokal/andere Liga – Spielklasse laut Quelle ergänzen): {kurz(rest)}")
    # 7 weitere Fakten
    nx = [m for m in mine if m["status"] == "incomplete"][:2]
    out.append("7. **Spiele davor/danach (FS):** letztes Pflichtspiel in FS "
               + (f"{dt(pfl[0][0]):%d.%m.} ({pfl[0][1]})" if pfl else "–") + " · letztes Ligaspiel "
               + (f"{dt(done[-1]):%d.%m.}" if done else "–") + " · nächste Liga: "
               + " | ".join(f"{dt(m):%d.%m. %H:%M} {m['home_name']} – {m['away_name']}" for m in nx)
               + (" · nationale Pokalspiele: siehe SM-Formdaten (Datum steht dort nicht)"
                  if sm_spiele and any(z_[0] == UNDATIERT for z_ in sm_spiele[:6]) else ""))
    # 5. Spieler / 7c – am letzten Pflichtspiel, das FS führt (Liga, Europapokal, ggf. Heimliga)
    letzte = pfl[:2]
    if not letzte:
        out.append("5. **Startelf letztes Pflichtspiel:** kein ausgetragenes Spiel in FS gefunden – Regel 7c von Hand prüfen.")
        return out
    m0, wb0 = letzte[0]
    st0, ev0, nmf = aufstellung(m0["id"], tid, idx)
    startelf = [nmf(i) for i, s in st0.items() if s.startswith("Startelf")]
    out.append(f"5. **Startelf letztes Pflichtspiel laut FS** ({dt(m0):%d.%m.}, {wb0}, {m0['home_name']} – {m0['away_name']}, "
               f"match {m0['id']}): " + (", ".join(startelf) or "keine Aufstellung in FS – Regel 7c von Hand prüfen"))
    if sm_spiele and sm_spiele[0][0] == UNDATIERT:
        out.append(f"   **ACHTUNG Regel 7c:** Das neueste Spiel der SM-Formdaten ({sm_spiele[0][1]} {sm_spiele[0][2]} "
                   f"{sm_spiele[0][3]}:{sm_spiele[0][4]}, {sm_spiele[0][5]}) führt FS nicht – war das das letzte Pflichtspiel, "
                   f"„neu oder nicht“ dort laut SM-Artikel prüfen; die Angaben unten gelten für das letzte Spiel in FS.")
    if spieler:
        out.append("   **Spieler aus den Teamnews (Regel 7b/7c – Status nach Originalwort trägt der Agent ein):**")
        auf = [(m, wb, aufstellung(m["id"], tid, idx)) for m, wb in letzte]
        kand = [p_ for p_ in idx.values() if p_.get("club_team_id") == tid]
        ids_auf = set()
        for _, _, (st, _, _) in auf:
            ids_auf |= set(st)
        kand += [idx[i] for i in ids_auf if i in idx and idx[i] not in kand]
        for sp_name in spieler:
            hits = [p_ for p_ in kand if norm(sp_name).strip() and all(
                t in norm(p_.get("full_name", "") + " " + (p_.get("known_as") or "")) for t in norm(sp_name).split())]
            if not hits:
                out.append(f"   - {sp_name}: in FS nicht gefunden (normalisiert gesucht) – Position nicht in der Quelle (FS); "
                           f"nur SM-Artikel/mögliche Startelf verwenden")
                continue
            for p_ in hits[:2]:
                stat = []
                for m, wb, (st, ev, _) in auf:
                    s_ = st.get(p_["id"], "nicht im Kader")
                    e_ = ev.get(p_["id"])
                    stat.append(f"{dt(m):%d.%m.} ({wb}): {s_}{' [' + e_ + ']' if e_ else ''}")
                neu = st0.get(p_["id"], "nicht im Kader")
                hinweis = ("spielte im letzten Pflichtspiel laut FS → bei fehlt/fraglich/gesperrt NEU"
                           if neu.startswith(("Startelf", "eingewechselt"))
                           else "spielte im letzten Pflichtspiel laut FS nicht → bei fehlt/fraglich NICHT NEU; bei „zurück“ nur "
                                "neu, wenn die Quelle klar „startet/spielt“ sagt (ungenutzt auf der Bank ≠ fehlte)")
                # seit 28.11.2026: Ein Suchname aus nur einem Wort muss den Nachnamen treffen – sonst Warnung (Anlass:
                # Suchname „Joseph“ traf den Vornamen von „Joseph Peter Rodon“, Leeds – Coventry 28.11.)
                nach = {(norm(p_.get(k_) or "").split() or [""])[-1] for k_ in ("full_name", "known_as")} - {""}
                q_ = set(norm(sp_name).split())
                warn = ("" if len(q_) >= 2 or q_ & nach else
                        f" · **ZUORDNUNG PRÜFEN:** Suchname „{sp_name}“ trifft nicht den Nachnamen dieses FS-Eintrags "
                        f"(„{p_.get('full_name')}“) – evtl. anderer Spieler; mit vollem Namen erneut suchen")
                out.append(f"   - {p_.get('known_as') or p_['full_name']}: {p_.get('position')}, {p_.get('appearances_overall')} Eins., "
                           f"{p_.get('goals_overall')} Tore ({liga_label}) · " + " · ".join(stat) + f" → {hinweis}{warn}")
        out.append("   Achtung: Nationale Pokalspiele und ihre Aufstellungen führt FS nicht – war das letzte Pflichtspiel ein "
                   "Pokalspiel, 7c dort laut SM prüfen.")
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


def sm_zu_zeilen(spiele, liga_slug, sid, tid, ms, weitere, nm_t, pos, abw, hinw):
    """SM-Formdaten (neuestes zuerst) → Zeilen, in beide Richtungen mit FS abgeglichen.

    Jedes SM-Spiel wird über Spielort, Gegnername (ganzer Name) und Ergebnis einem FS-Spiel zugeordnet.
    FS-Spiele, die im Zeitraum der SM-Formdaten liegen und dort fehlen, werden gemeldet und ergänzt.
    """
    name = nm_t.get(tid, "?")
    # Teamname im SM-Format = der Name, der in allen Spielen vorkommt
    namen = None
    for _, _, a, _, _, b in spiele:
        namen = {a, b} if namen is None else namen & {a, b}
    team_sm = sorted(namen)[0] if namen and len(namen) == 1 else None
    if spiele and not team_sm:
        hinw.append(f"{name}: SM-Teamname in den Formdaten nicht eindeutig – Heim/Auswärts der SM-Spiele von Hand prüfen")
    # FS-Pools je Wettbewerb: {Schlüssel: [Spiele des Teams, alle Status]}
    pools = {"liga": [m for m in ms if tid in (m["homeID"], m["awayID"])]}
    for s, (label, mm) in weitere.items():
        pools[s] = [m for m in mm if tid in (m["homeID"], m["awayID"])]
    heimliga = [s for s in weitere if s not in EUROPAPOKAL]
    def pool_von(wb):
        if wb == liga_slug:
            return "liga"
        if wb in EP_SLUG:
            s = EP_SLUG[wb]
            return "liga" if s == sid else (s if s in pools else None)
        return heimliga[0] if heimliga and pools.get(heimliga[0]) else None
    def label_von(key, wb):
        return "Liga" if key == "liga" else wb
    benutzt = set()
    def kandidaten(key, ist_heim, status_ok=True):
        return sorted([m for m in pools.get(key, []) if m["id"] not in benutzt and (m["homeID"] == tid) == ist_heim
                       and ((m["status"] == "complete") if status_ok else (m["status"] not in ("complete", "incomplete")))],
                      key=lambda m: -m["date_unix"])
    def zeile(m, key, wb):
        h, e, g, gid, gname = sp_sicht(m, tid)
        if key == "liga":
            geg = f"{nm_t.get(gid, gname)} (Pl. {pos.get(gid, '?')})"
        else:
            geg = f"{gname} (anderer Wb.)"
        return (f"{dt(m):%d.%m.}", "H" if h else "A", geg, e, g, label_von(key, wb))
    zeilen = []  # [(Zeile, date_unix oder None)]
    offen = []   # Indizes der SM-Spiele ohne FS-Zuordnung
    for wb, sun, a, x, y, b in spiele:
        ist_heim = (a == team_sm) if team_sm else True
        e, g, geg = (x, y, b) if ist_heim else (y, x, a)
        ha = "H" if ist_heim else "A"
        key = pool_von(wb)
        treffer = None
        if key is not None:
            kand = kandidaten(key, ist_heim)
            bew = []
            for m in kand:
                _, fe, fg, _, gname = sp_sicht(m, tid)
                st, sw, off_sm, off_fs = name_wert(geg, gname)
                bew.append(((st, sw, -off_sm, -off_fs, (fe, fg) == (e, g), m["date_unix"]), m, st, off_sm, (fe, fg)))
            bew.sort(key=lambda t: t[0], reverse=True)
            if bew and bew[0][2] >= 1:
                _, m, st, off_sm, erg = bew[0]
                if erg == (e, g):
                    treffer = m
                elif off_sm == 0:
                    # ganzer Name passt, Ergebnis nicht → echte Abweichung
                    abw.append(f"{name}: SM {ha} {geg} {e}:{g} ≠ FS {dt(m):%d.%m.} {erg[0]}:{erg[1]} (Status {m['status']}) – "
                               f"FS-Wert im Block verwendet, von Hand klären")
                    treffer = m
            if treffer is None:
                # kein Namensbeleg: neuestes offenes FS-Spiel am selben Ort mit demselben Ergebnis
                gleich = [m for m in kand if sp_sicht(m, tid)[1:3] == (e, g)]
                if gleich and kand and gleich[0]["id"] == kand[0]["id"]:
                    treffer = gleich[0]
                    hinw.append(f"{name}: SM {ha} „{geg}“ {e}:{g} über Spielort, Reihenfolge und Ergebnis dem FS-Spiel "
                                f"{dt(treffer):%d.%m.} gegen „{sp_sicht(treffer, tid)[4]}“ zugeordnet (Name anders geschrieben) – Gegner prüfen")
            if treffer is None and (e, g) == (0, 0):
                # SM-Platzhalter für ein nicht ausgetragenes Spiel?
                na = [m for m in kandidaten(key, ist_heim, status_ok=False) if name_wert(geg, sp_sicht(m, tid)[4])[0] >= 1]
                if na:
                    benutzt.add(na[0]["id"])
                    abw.append(f"{name}: SM zeigt {ha} {geg} 0:0, FS führt das Spiel vom {dt(na[0]):%d.%m.} als "
                               f"„{na[0]['status']}“ (nicht ausgetragen) – nicht gezählt")
                    continue
        if treffer is not None:
            benutzt.add(treffer["id"])
            zeilen.append((zeile(treffer, key, wb), treffer["date_unix"]))
        else:
            if key is not None:
                abw.append(f"{name}: SM-Spiel {ha} {geg} {e}:{g} ({wb}) in FS nicht zugeordnet – SM-Wert im Block, von Hand klären")
            offen.append(len(zeilen))
            zeilen.append(((UNDATIERT, ha, f"{geg} (anderer Wb.)" if wb != liga_slug else f"{geg} (Pl. ?)", e, g,
                            "Liga" if wb == liga_slug else wb), None))
    # Gegenrichtung: FS-Spiele, die neuer sind als das älteste zugeordnete Spiel, aber keinem SM-Spiel zugeordnet wurden
    datiert = [d for _, d in zeilen if d]
    if datiert:
        alt, neu = min(datiert), max(datiert)
        fehlend = []
        for key, mm in pools.items():
            wbl = "Liga" if key == "liga" else weitere[key][0]
            fehlend += [(m, key, wbl) for m in mm if m["status"] == "complete" and m["id"] not in benutzt and m["date_unix"] > alt]
        # zuerst: gehört ein solches FS-Spiel zu einem undatierten SM-Spiel (z. B. unbekannter Wettbewerbs-Link, anderer Name)?
        for i in offen:
            z_ = zeilen[i][0]
            sm_geg = z_[2].rsplit(" (", 1)[0]
            pass_ = [(m, key, wbl) for m, key, wbl in fehlend if m["id"] not in benutzt
                     and (m["homeID"] == tid) == (z_[1] == "H") and sp_sicht(m, tid)[1:3] == (z_[3], z_[4])]
            sicher = [t for t in pass_ if (lambda w: w[0] >= 1 and w[2] == 0)(name_wert(sm_geg, sp_sicht(t[0], tid)[4]))]
            wahl = sicher[0] if sicher else (pass_[0] if len(pass_) == 1 else None)
            if wahl:
                m, key, wbl = wahl
                benutzt.add(m["id"])
                zeilen[i] = (zeile(m, key, "Liga" if key == "liga" else z_[5]), m["date_unix"])
                if not sicher:
                    hinw.append(f"{name}: SM {z_[1]} „{sm_geg}“ {z_[3]}:{z_[4]} ({z_[5]}) über Spielort und Ergebnis dem FS-Spiel "
                                f"{dt(m):%d.%m.} gegen „{sp_sicht(m, tid)[4]}“ ({wbl}) zugeordnet – Gegner prüfen")
        for m, key, wbl in sorted(fehlend, key=lambda t: t[0]["date_unix"]):
            if m["id"] in benutzt:
                continue
            h, e, g, _, gname = sp_sicht(m, tid)
            abw.append(f"{name}: FS-Spiel {dt(m):%d.%m.} {'H' if h else 'A'} {gname} {e}:{g} ({wbl}) fehlt in den SM-Formdaten"
                       + (" – SM-Formdaten veraltet? Spiel oben in den Block aufgenommen" if m["date_unix"] > neu
                          else " – nach Datum in den Block eingefügt") + ", von Hand klären")
            ziel = next((i for i, (_, d) in enumerate(zeilen) if d and d < m["date_unix"]), len(zeilen))
            zeilen.insert(ziel, (zeile(m, key, wbl), m["date_unix"]))
    elif spiele:
        hinw.append(f"{name}: kein SM-Formspiel einem FS-Spiel zugeordnet – Gegenrichtung (fehlt ein FS-Spiel in SM?) von Hand prüfen")
    return [z_ for z_, _ in zeilen]


def spielort_zeile(name, zs, wo):
    if not zs:
        return f"{name} {wo}: keine Ligaspiele"
    w = sum(e > g for *_, e, g, _ in zs); d = sum(e == g for *_, e, g, _ in zs)
    return (f"{name} {wo} (Liga, Saison): {len(zs)} Sp. {w}-{d}-{len(zs) - w - d}, "
            f"{sum(e for *_, e, g, _ in zs)}:{sum(g for *_, e, g, _ in zs)}, {(3 * w + d) / len(zs):.2f} Pkt je Spiel")


def main():
    a = sys.argv[1:]
    if len(a) < 3:
        sys.exit(__doc__)
    sid, fh, fg = int(a[0]), a[1], a[2]
    opt = {"--sm": None, "--sm-seite": None, "--spieler-heim": "", "--spieler-gast": "", "--ep": None,
           "--liga-heim": None, "--liga-gast": None}
    i = 3
    while i < len(a):
        if a[i] == "--sm":
            opt["--sm"] = (a[i + 1], a[i + 2]); i += 3
        elif a[i] in opt:
            opt[a[i]] = a[i + 1]; i += 2
        else:
            sys.exit(f"Unbekannte Option {a[i]}")
    start = datetime.datetime(2026, 9, 1, tzinfo=BER)
    ms = get("league-matches", season_id=sid, max_per_page=1000)["data"]
    if sid in EUROPAPOKAL:
        ms = [m for m in ms if dt(m) >= start]
    liga_label = EP_NAME.get(sid, "Liga")
    # weitere Wettbewerbe, die FS führt (für „letztes Pflichtspiel“ und den Abgleich): Europapokale, ggf. Heimligen
    weitere = {}
    for s in sorted(EUROPAPOKAL - {sid}):
        weitere[s] = (EP_NAME[s], [m for m in get("league-matches", season_id=s, max_per_page=1000)["data"] if dt(m) >= start])
    for o in ("--liga-heim", "--liga-gast"):
        if opt[o] and int(opt[o]) not in weitere and int(opt[o]) != sid:
            weitere[int(opt[o])] = ("Heimliga", get("league-matches", season_id=int(opt[o]), max_per_page=1000)["data"])
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
    abw, hinw, sm_z = [], [], {th: None, tg: None}
    if opt["--sm"] or opt["--sm-seite"]:
        fd, liga_slug, fehler = sm_formdaten(*(opt["--sm"] or (None, None)), seite=opt["--sm-seite"])
        if fehler:
            print(f"- SM: {fehler}")
        elif fd and len(fd) == 2:
            sm_z[th] = sm_zu_zeilen(fd[0][1], liga_slug, sid, th, ms, weitere, nm_t, pos, abw, hinw)
            sm_z[tg] = sm_zu_zeilen(fd[1][1], liga_slug, sid, tg, ms, weitere, nm_t, pos, abw, hinw)
            print(f"- SM-Formdaten gelesen (Liga-Slug {liga_slug}); Liga- und Europapokal-Spiele in beide Richtungen mit FS abgeglichen.")
        else:
            print("- SM: Formdaten auf der Spielseite nicht gefunden – Block „letzte 6 alle Wb.“ von Hand erstellen")
    print("- **Abweichungen SM ↔ FS:** " + ("; ".join(abw) if abw else "keine in den Formdaten (Tabellenplatz mit SM-Tabelle selbst abgleichen)"))
    if hinw:
        print("- **Hinweise zur Zuordnung (prüfen):** " + "; ".join(hinw))
    idx = spieler_index(sid)
    sp_h = [s.strip() for s in opt["--spieler-heim"].split(",") if s.strip()]
    sp_g = [s.strip() for s in opt["--spieler-gast"].split(",") if s.strip()]
    for label, t, n, sm_, sp in (("Heim", th, nh, sm_z[th], sp_h), ("Gast", tg, ng, sm_z[tg], sp_g)):
        print()
        pfl = pflichtspiele(t, ms, weitere, liga_label)
        print("\n".join(team_teil(label, t, n, ms, order, pts, gd, pl, nm_t, sid, sm_, sp, idx, pfl, liga_label)))
    # 4b Tabellenvergleich und Spielort
    print("\n### Kräfteverhältnis – Tabelle und Spielort (Schritt 4b; die Bausteine „letzte 6“ und Gegnerstärke stehen oben je Team)")
    print(f"- Tabelle: {nh}: Platz {pos[th]}, {pts[th]} Pkt ({pts[th] / pl[th]:.2f} je Spiel) · {ng}: Platz {pos[tg]}, {pts[tg]} Pkt "
          f"({pts[tg] / pl[tg]:.2f} je Spiel) · Abstand {abs(pos[th] - pos[tg])} Plätze, {abs(pts[th] - pts[tg])} Punkte.")
    hoch = "Heim" if pos[th] < pos[tg] else "Gast"
    print(f"- Tabellenhöher (für die Merkmale-Zeile, Punkt 10): {hoch} ({nh if hoch == 'Heim' else ng}).")
    done = [m for m in ms if m["status"] == "complete"]
    def ort(tid, heim):
        return [(None, None, None) + sp_sicht(m, tid)[1:3] + (None,) for m in done if (m["homeID"] if heim else m["awayID"]) == tid]
    print(f"- Spielort (Rang 3): {spielort_zeile(nh, ort(th, True), 'daheim')} · {spielort_zeile(ng, ort(tg, False), 'auswärts')}.")
    print("- Einstufung (klarer Favorit / ausgeglichen / nicht eindeutig) trifft der Agent: je Baustein „zeigt zu: Heim / Gast / "
          "keinem“ (Tabelle, letzte 6 alle Wb., letzte 6 Liga, Gegnerstärke) und der Spielort als Gegenprobe (Schritt 4b).")
    if opt["--ep"]:
        eu = get("league-matches", season_id=int(opt["--ep"]), max_per_page=1000)["data"]
        eu = [m for m in eu if dt(m) >= start]
        o2, p2, g2, f2, n2, l2 = tabelle(eu)
        print(f"\n### Europapokal-Ligaphase (Saison {opt['--ep']}; Tabelle aus FS-Spielen, UEFA-Reihenfolge kann abweichen)")
        for tid_, nmx in ((th, nh), (tg, ng)):
            if tid_ not in n2:
                print(f"- {nmx}: in der Ligaphase nicht gefunden"); continue
            mine = sorted([m for m in eu if tid_ in (m["homeID"], m["awayID"]) and m["status"] == "complete"], key=lambda m: -m["date_unix"])
            zz = []
            for m in mine:
                h, e, g, gid, gname = sp_sicht(m, tid_)
                zz.append((f"{dt(m):%d.%m.}", "H" if h else "A", gname, e, g, "Liga"))
            print(f"- {n2[tid_]}: Platz {o2.index(tid_) + 1} von {len(o2)}, {p2[tid_]} Pkt")
            print("\n".join(block(zz, "alle Spiele Ligaphase")))
    print("\n_Werkzeug zählt nur; Teamnews-Status (Originalwort), Lage-Check, Einstufung, Märkte und Tipp trifft der Agent._")


if __name__ == "__main__":
    main()
