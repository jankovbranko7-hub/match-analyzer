#!/usr/bin/env python3
"""Auswertung aller ausgewerteten Tipps in tipps/sportsmole/ (Sports-Mole-Check, überarbeitet am 28.11.2026 für 1.4.1).

Aufruf aus dem Repo-Wurzelordner:  python3 -I werkzeuge/tippanalyse.py

Liest alle Tageslisten `tipps/sportsmole/JJJJ-MM-TT*.md` (alle Monate), je Tipp die Tabellenzeile (Tipp, Kennzeichnung,
Ergebnis) und die Merkmale-Zeile des Abschnitts. Gibt aus:
  1. alle Tipps (Trefferquote, zweitbester Markt, Kennzeichnung × Grenzfall, geänderte Tipps, Wettart, Liga, verfehlte Tor-Tipps),
  2. getrennt „vor 1.4“ und „seit 1.4“,
  3. seit 1.4: „Spielen: ja/nein“, Zahl der gespielten Tipps (Auswertung an den Nutzer ab 50 gespielten),
     Kräfteverhältnis, Schattentipp (was ohne 4b-Ausschluss und ohne Vorrang Sieg-Markt getippt worden wäre),
     Vergleichswert „der Tabellenhöhere gewinnt“, Vorprüfung (Merkmal 13: aus Vorprüfung gewählt ja/nein),
     Zweitquelle Teamnews (Merkmal 14: bestätigt / weicht ab / nicht verfügbar; Rang 1 betroffen ja/nein),
     Merkmal 15: Tipp und „Spielen“ ohne Zweitquelle (Vergleich Version 1.5 mit dem Stand davor an denselben Spielen).
Ein Tipp zählt als „seit 1.4“, wenn seine Merkmale-Zeile Punkt (11) „Spielen“ enthält oder die Liste ab dem 28.11.2026 datiert.
Keine Quoten, kein Rechenmodell – nur Ergebnisse der eigenen Tipps.
"""
import glob
import re
import unicodedata

MK = [("Heimsieg", "H"), ("Auswärtssieg", "A"), ("Beide treffen – Ja", "BJ"), ("Beide treffen – Nein", "BN"),
      ("Über 2,5", "O"), ("Unter 2,5", "U")]
MK_NAME = {k: n for n, k in MK}
START_14 = "2026-11-28"


def mk(s):
    """Erster genannter Markt in einem Text (oder None). „Sieg <Team>“ ohne Heim/Auswärts wird nicht geraten."""
    if not s:
        return None
    best = None
    for n, k in MK:
        i = s.find(n)
        if i >= 0 and (best is None or i < best[0]):
            best = (i, k)
    return best[1] if best else None


def out(h, a):
    return {"H": h > a, "A": a > h, "BJ": h > 0 < a, "BN": not (h > 0 < a), "O": h + a > 2, "U": h + a < 3}


def norm(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def q(sub, key="hit"):
    t = sum(1 for r in sub if r[key])
    return f"{t}/{len(sub)} = {t / len(sub):.0%}" if sub else "–"


def seg(mm, n):
    """Text des Merkmals (n): von „(n)“ bis „(n+1)“ oder zum Ende."""
    i = mm.find(f"({n})")
    if i < 0:
        return None
    # Ende = der nächste höhere Marker (ein Merkmal kann fehlen, z. B. 13, das Claude erst später einträgt)
    enden = [mm.find(f"({m})", i) for m in range(n + 1, 20)]
    enden = [j for j in enden if j > 0]
    return mm[i + len(f"({n})"):min(enden) if enden else len(mm)].strip(" ·")


def lies():
    rows = []
    for f in sorted(glob.glob("tipps/sportsmole/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]*.md")):
        txt = open(f).read()
        datei = f.split("/")[-1][:-3]
        hdr = None
        for ln in txt.split("\n"):
            if ln.startswith("|") and re.search(r"\|\s*Tipp\s*\|", ln):
                hdr = [c.strip() for c in ln.strip().strip("|").split("|")]
                continue
            if not ln.startswith("|") or hdr is None:
                continue
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            if len(c) < len(hdr) - 1:
                continue
            d = dict(zip(hdr, c))
            tipc = d.get("Tipp", "")
            tip = mk(tipc.split("(")[0]) or mk(tipc)
            erg = d.get("Ergebnis", "") or c[-1]
            m = re.search(r"(\d+)\s*:\s*(\d+)", erg + " " + c[-1])
            if not tip or not m:
                continue
            h, a = int(m.group(1)), int(m.group(2))
            kz = d.get("Kennzeichnung", "")
            # ursprünglicher Tipp bei Änderung vor Anpfiff: „bis 09:15 Heimsieg …)“, „ursprünglich …“, „zuvor: X → Y“
            geaendert = bool(re.search(r"bis [\d:]+ |ursprünglich|zuvor:", tipc))
            mo = (re.search(r"bis [\d:]+ ([^)]+)\)", tipc) or re.search(r"ursprünglich ([^)·]+)", tipc)
                  or re.search(r"zuvor:\s*([^)→]+)", tipc))
            rows.append(dict(f=datei, spiel=d.get("Spiel") or d.get("Paarung") or "", liga=d.get("Liga", ""), tip=tip, h=h, a=a,
                             kz="einig" if "einig" in kz else "geteilt" if "geteilt" in kz else "?",
                             gf="Grenzfall" in tipc, geaendert=geaendert, orig=mk(mo.group(1)) if mo else None,
                             spielen_spalte=d.get("Spielen", ""), txt=txt))
    for r in rows:
        home = norm(r["spiel"].split("–")[0].split(" - ")[0]).strip()[:8]
        sec = [s for s in re.split(r"\n## ", r["txt"]) if home and home in norm(s.split("\n")[0])]
        mm = ""
        if sec:
            ms = re.findall(r"\*\*Merkmale[^*]*\*\*(.*?)(?:\n- |\n\n|$)", sec[-1], re.S)
            if ms:
                mm = " ".join(ms[-1].split())
        r["mm"] = mm or None
        m9 = re.search(r"\(9\)[^·]*?:\s*([^·(]+)", mm)
        r["zweit"] = mk(m9.group(1)) if m9 else None
        for key, n in (("neu1", 5), ("r2", 6), ("prof", 7)):
            mx = re.search(rf"\({n}\)[^·]*?:\s*(ja|nein)", mm)
            r[key] = mx.group(1) if mx else None
        # seit 1.4 / 1.4.1
        s10, s11, s12 = seg(mm, 10), seg(mm, 11), seg(mm, 12)
        r["kv"] = ("klarer Favorit" if s10 and "klarer Favorit" in s10 else "ausgeglichen" if s10 and "ausgeglichen" in s10
                   else "nicht eindeutig" if s10 and "nicht eindeutig" in s10 else None)
        th = re.search(r"Tabellenhöher:\s*(Heim|Gast)", s10 or "")
        r["hoeher"] = th.group(1) if th else None
        sp = re.search(r"Spielen:\s*(ja|nein)", s11 or "") or re.search(r"(ja|nein)", r["spielen_spalte"])
        r["v14"] = bool(s11) or r["f"][:10] >= START_14
        r["spielen"] = sp.group(1) if sp else (("ja" if r["kz"] == "einig" else "nein") if r["v14"] else None)
        r["schatten"] = mk(s12) if s12 else None
        r["schatten_grund"] = ("4b-Ausschluss" if s12 and "4b" in s12 else "Vorrang Sieg-Markt" if s12 and "Vorrang" in s12
                               else None)
        s13 = seg(mm, 13)
        vp = re.search(r"Vorprüfung:\s*(ja|nein)", s13 or "")
        r["vp"] = vp.group(1) if vp else None
        r["vp_markt"] = (mk(s13) if s13 and "keinem" not in s13 else None) if r["vp"] == "ja" else None
        s14 = seg(mm, 14) or ""
        r["zq"] = ("nicht verfügbar" if "nicht verfügbar" in s14 else "weicht ab" if "weicht ab" in s14
                   else "bestätigt" if "bestätigt" in s14 else None)
        r1 = re.search(r"Rang 1 betroffen:\s*(ja|nein)", s14)
        r["zq_rang1"] = r1.group(1) if r1 else None
        s15 = seg(mm, 15) or ""
        r["ohne_tip"] = mk(s15)
        o = re.search(r"Spielen\s*(ja|nein)", s15)
        r["ohne_spielen"] = o.group(1) if o else None
        r["hit"] = out(r["h"], r["a"])[r["tip"]]
        del r["txt"]
    return rows


def grundauswertung(rows, titel):
    print(f"\n===== {titel}: {len(rows)} Tipps, Treffer {q(rows)} =====")
    if not rows:
        return
    mm = [r for r in rows if r["mm"]]
    print("mit Merkmale-Zeile:", len(mm))
    z = [r for r in mm if r["zweit"]]
    for r in z:
        r["zhit"] = out(r["h"], r["a"])[r["zweit"]]
    print("\nTipp vs. zweitbester Markt (gleiche Spiele):", len(z))
    if z:
        print("  Tipp:", q(z), "  Zweitbester:", q(z, "zhit"))
        print("  nur Tipp traf:", sum(r["hit"] and not r["zhit"] for r in z), " nur Zweitbester traf:",
              sum(r["zhit"] and not r["hit"] for r in z), " beide:", sum(r["hit"] and r["zhit"] for r in z),
              " keiner:", sum(not r["hit"] and not r["zhit"] for r in z))
    for lab, k, v in (("Rang-2-Blöcke einig", "r2", "ja"), ("Rang-2-Blöcke NICHT einig", "r2", "nein"),
                      ("gegensätzliche Profile", "prof", "ja"), ("keine gegens. Profile", "prof", "nein"),
                      ("neue Rang-1-Gegenangabe", "neu1", "ja"), ("keine neue Rang-1-Gegenangabe", "neu1", "nein")):
        print(f"  {lab}: {q([r for r in mm if r[k] == v])}")
    print("\nKombination Kennzeichnung × Grenzfall:")
    for kz in ("einig", "geteilt"):
        for g in (False, True):
            print(f"  {kz}, Grenzfall={g}: {q([r for r in rows if r['kz'] == kz and r['gf'] == g])}")
    ch = [r for r in rows if r["geaendert"]]
    mit = [r for r in ch if r["orig"]]
    for r in mit:
        r["ohit"] = out(r["h"], r["a"])[r["orig"]]
    print(f"\nGeänderte Tipps (vor Anpfiff): {len(ch)}  neuer Tipp: {q(ch)}")
    print(f"  davon ursprünglicher Markt lesbar: {len(mit)}  neuer Tipp: {q(mit)}  ursprünglicher hätte: {q(mit, 'ohit')}")
    print("\nWettart × Kennzeichnung:")
    for n, k in MK:
        a = [r for r in rows if r["tip"] == k]
        if a:
            print(f"  {n}: gesamt {q(a)} | einig {q([r for r in a if r['kz'] == 'einig'])} | geteilt {q([r for r in a if r['kz'] == 'geteilt'])}")
    print("\nNach Liga (Zuordnung über Liga-Spalte/Tagesliste):")
    bylg = {}
    for r in rows:
        lg = r["liga"] or {"2026-11-24": "Champions League", "2026-11-25": "Champions League", "2026-11-26": "EL/ECL"}.get(r["f"], "?")
        bylg.setdefault(re.sub(r"\s*\(\d+\)", "", lg), []).append(r)
    for lg, s in sorted(bylg.items(), key=lambda x: -len(x[1])):
        print(f"  {lg}: {q(s)}")
    print("\nVerfehlte Tor-Tipps (Ergebnisse):")
    for n, k in MK[2:]:
        a = [r for r in rows if r["tip"] == k and not r["hit"]]
        print(f"  {n} verfehlt: " + (", ".join(f"{r['h']}:{r['a']}" for r in a) or "–"))


def auswertung_14(rows):
    print(f"\n===== Seit Version 1.4 im Einzelnen ({len(rows)} Tipps mit Ergebnis) =====")
    if not rows:
        print("noch keine ausgewerteten Tipps seit 1.4")
        return
    ja = [r for r in rows if r["spielen"] == "ja"]
    nein = [r for r in rows if r["spielen"] == "nein"]
    print(f"Spielen: ja   {q(ja)}")
    print(f"Spielen: nein {q(nein)} (nur Beobachtung)")
    print(f"→ gespielte Tipps mit Ergebnis: {len(ja)} von 50 (Auswertung an den Nutzer ab 50 gespielten Tipps)")
    print("\nKräfteverhältnis (Merkmal 10):")
    for kv in ("klarer Favorit", "ausgeglichen", "nicht eindeutig", None):
        a = [r for r in rows if r["kv"] == kv]
        if a:
            print(f"  {kv or 'nicht angegeben'}: {q(a)} | davon Spielen: ja {q([r for r in a if r['spielen'] == 'ja'])}"
                  f" | Sieg-Tipps {q([r for r in a if r['tip'] in 'HA'])} | Tor-Tipps {q([r for r in a if r['tip'] not in 'HA'])}")
    s = [r for r in rows if r["schatten"]]
    for r in s:
        r["shit"] = out(r["h"], r["a"])[r["schatten"]]
    print(f"\nSchattentipp (Merkmal 12 – Tipp ohne 4b-Ausschluss und ohne Vorrang Sieg-Markt): {len(s)} Tipps")
    if s:
        gleich = [r for r in s if r["schatten"] == r["tip"]]
        anders = [r for r in s if r["schatten"] != r["tip"]]
        print(f"  gleich wie der Tipp: {len(gleich)} ({q(gleich)})")
        print(f"  anders: {len(anders)} – Tipp nach 1.4 {q(anders)} | Schattentipp (ohne 1.4) hätte {q(anders, 'shit')}")
        for grund in ("4b-Ausschluss", "Vorrang Sieg-Markt", None):
            a = [r for r in anders if r["schatten_grund"] == grund]
            if a:
                print(f"    wegen {grund or 'nicht angegeben'}: {len(a)} – Tipp {q(a)} | Schattentipp {q(a, 'shit')}")
                for r in a:
                    print(f"      {r['f']} {r['spiel']} {r['h']}:{r['a']} – Tipp {MK_NAME[r['tip']]} {'✅' if r['hit'] else '❌'} · "
                          f"Schattentipp {MK_NAME[r['schatten']]} {'✅' if r['shit'] else '❌'}")
    t = [r for r in rows if r["hoeher"]]
    for r in t:
        r["thit"] = (r["h"] > r["a"]) if r["hoeher"] == "Heim" else (r["a"] > r["h"])
    sieg = [r for r in t if r["tip"] in "HA"]
    print(f"\nVergleichswert „der Tabellenhöhere gewinnt“ (Merkmal 10): {len(t)} Tipps mit Angabe")
    if t:
        print(f"  alle Spiele: Tabellenhöherer gewinnt {q(t, 'thit')}")
        print(f"  nur Spiele mit Sieg-Tipp: Tipp {q(sieg)} | Tabellenhöherer gewinnt {q(sieg, 'thit')}")
        sj = [r for r in sieg if r["spielen"] == "ja"]
        print(f"  nur gespielte Sieg-Tipps: Tipp {q(sj)} | Tabellenhöherer gewinnt {q(sj, 'thit')}")
    v = [r for r in rows if r["vp"]]
    print(f"\nVorprüfung (Merkmal 13): {len(v)} Tipps mit Angabe")
    if v:
        def anteil(sub):
            j = sum(r["spielen"] == "ja" for r in sub)
            return f"{j}/{len(sub)} = {j / len(sub):.0%}" if sub else "–"
        gruppen = (("aus Vorprüfung, Zahlen zeigten zu einem Markt", [r for r in v if r["vp"] == "ja" and r["vp_markt"]]),
                   ("aus Vorprüfung, Zahlen zeigten zu keinem", [r for r in v if r["vp"] == "ja" and not r["vp_markt"]]),
                   ("ohne Vorprüfung", [r for r in v if r["vp"] == "nein"]))
        for lab, sub in gruppen:
            print(f"  {lab}: {len(sub)} Tipps – davon „Spielen: ja“ {anteil(sub)} · Treffer alle {q(sub)} · "
                  f"Treffer gespielte {q([r for r in sub if r['spielen'] == 'ja'])}")
        m = gruppen[0][1]
        if m:
            g = [r for r in m if r["vp_markt"] == r["tip"]]
            print(f"  Tipp = Richtung der Vorprüfung: {len(g)} von {len(m)} (Treffer {q(g)}); Tipp anders: {len(m) - len(g)} "
                  f"(Treffer {q([r for r in m if r['vp_markt'] != r['tip']])})")
    z = [r for r in rows if r["zq"]]
    print(f"\nZweitquelle Teamnews (Merkmal 14): {len(z)} Tipps mit Angabe – Bericht an den Nutzer ab etwa 50 Tipps mit Länderquelle")
    if z:
        for lab in ("bestätigt", "weicht ab", "nicht verfügbar"):
            sub = [r for r in z if r["zq"] == lab]
            print(f"  {lab}: {len(sub)} Tipps · Treffer {q(sub)} · gespielte {q([r for r in sub if r['spielen'] == 'ja'])}")
        ab = [r for r in z if r["zq"] == "weicht ab"]
        for lab in ("ja", "nein"):
            sub = [r for r in ab if r["zq_rang1"] == lab]
            print(f"  weicht ab, Rang 1 betroffen: {lab} – {len(sub)} Tipps · Treffer {q(sub)}")
            for r in sub if lab == "ja" else []:
                print(f"      {r['f']} {r['spiel']} {r['h']}:{r['a']} – Tipp {MK_NAME[r['tip']]} {'✅' if r['hit'] else '❌'}")
    o = [r for r in rows if r["ohne_tip"] and r["ohne_spielen"]]
    for r in o:
        r["o_hit"] = out(r["h"], r["a"])[r["ohne_tip"]]
    print(f"\nOhne Zweitquelle (Merkmal 15 – Tipp und „Spielen“ nach den Regeln vor 1.5): {len(o)} Tipps mit Angabe")
    if o:
        gleich = [r for r in o if r["ohne_tip"] == r["tip"] and r["ohne_spielen"] == r["spielen"]]
        anders = [r for r in o if r not in gleich]
        print(f"  gleich: {len(gleich)} · anders: {len(anders)}")
        mit = [r for r in o if r["spielen"] == "ja"]
        ohne = [r for r in o if r["ohne_spielen"] == "ja"]
        print(f"  gespielt mit Zweitquelle (1.5): {q(mit)} | gespielt worden wären ohne Zweitquelle: {q(ohne, 'o_hit')}")
        for r in anders:
            print(f"      {r['f']} {r['spiel']} {r['h']}:{r['a']} – 1.5: {MK_NAME[r['tip']]}, Spielen {r['spielen']} {'✅' if r['hit'] else '❌'} · "
                  f"ohne Zweitquelle: {MK_NAME[r['ohne_tip']]}, Spielen {r['ohne_spielen']} {'✅' if r['o_hit'] else '❌'}")


def main():
    rows = lies()
    grundauswertung(rows, "Alle Tipps")
    vor = [r for r in rows if not r["v14"]]
    seit = [r for r in rows if r["v14"]]
    print(f"\n===== Vor 1.4 / seit 1.4 =====\nvor 1.4:  {q(vor)}\nseit 1.4: {q(seit)}")
    if seit:
        grundauswertung(seit, "Seit 1.4")
    auswertung_14(seit)


if __name__ == "__main__":
    main()
