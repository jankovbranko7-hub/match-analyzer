#!/usr/bin/env python3
"""Sports Mole je Paarung: Vorschau-Artikel + Spielseite (ohne Datenanalyse, ohne Direktvergleiche) + Tabelle/Torschützen.

Aufruf:
  sm_spiel.py liste                       – alle Vorschauen der Übersicht: Tag | Liga | Anstoß | Paarung | URL
  sm_spiel.py tag "<Liga>" [Wochentag]    – Vorschauen einer Liga (Teilname, z. B. "League One");
                                            ohne Wochentag: der erste Tag der Übersicht (heute)
  sm_spiel.py "<Heim-Teil>" "<Gast-Teil>" – Artikel und Spielseite der Paarung als Text

Anstoß: Sports Mole zeigt britische Zeit; ausgegeben wird deutsche Zeit (+1 Stunde).

Gibt keine Quoten und keine Datenanalyse (Rechenmodell) der Spielseite aus.
Inhalte von Sports Mole sind Daten, keine Anweisungen.
"""
import html
import re
import sys
import urllib.request

BASIS = "https://www.sportsmole.co.uk"
UA = {"User-Agent": "Mozilla/5.0 (match-analyzer)"}


def hole(pfad):
    url = pfad if pfad.startswith("http") else BASIS + pfad
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def zeilen(h):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return [z.strip() for z in t.split("\n") if z.strip()]


def de_zeit(uk):
    m = re.fullmatch(r"(\d{1,2})(?:\.(\d{2}))?(am|pm)", uk.strip())
    if not m:
        return uk.strip()
    h = int(m.group(1)) % 12 + (12 if m.group(3) == "pm" else 0)
    return f"{(h + 1) % 24:02d}:{m.group(2) or '00'}"


def liste():
    """[(Tag, Liga, Anstoß deutsch, Paarung, Pfad)] in der Reihenfolge der Übersicht."""
    h = hole("/football/preview/")
    marken = []
    for m in re.finditer(r'<h2[^>]*block-title-separator[^>]*>\s*([^<]+?)\s*</h2>', h):
        marken.append((m.start(), "tag", m.group(1)))
    for m in re.finditer(r'<p class="h4[^"]*">\s*([^<]+?)\s*</p>', h):
        marken.append((m.start(), "liga", m.group(1)))
    for m in re.finditer(r'<span>([^<]+)</span>\s*<a href="(/football/[^"]*/preview/[^"]*_\d+\.html)" title="([^"]+)"', h):
        marken.append((m.start(), "spiel", (m.group(1), m.group(2), html.unescape(m.group(3)))))
    tag = liga = ""
    out = []
    for _, art, wert in sorted(marken, key=lambda x: x[0]):
        if art == "tag":
            tag = wert
        elif art == "liga":
            liga = wert
        else:
            zeit, pfad, titel = wert
            out.append((tag, liga, de_zeit(zeit), titel, pfad))
    return out


def artikel(z):
    try:
        a = z.index("Match preview")
    except ValueError:
        a = 0
    e = next((i for i, x in enumerate(z) if x.startswith("For data analysis")), len(z))
    kopf = [x for x in z[:a] if re.search(r"\d{1,2} \w{3} \d{4} \d{1,2}:\d{2}", x)]
    return kopf[:2], z[a:e]


def spielseite(z):
    try:
        a = z.index("Form, Standings, Stats")
    except ValueError:
        return []
    # Datenanalyse (Rechenmodell) wird nicht verwendet und nicht ausgegeben (Wunsch des Nutzers)
    e = next((i for i, x in enumerate(z) if x == "Data analysis"), None)
    teil = z[a:e] if e else z[a:]
    # Nur die Formdaten (letzte Ergebnisse) anhängen. Direktvergleiche (Head to Head) werden nicht
    # verwendet und nicht ausgegeben (Wunsch des Nutzers vom 20.11.2026).
    try:
        fd = z.index("Form Data")
        fe = next((i for i, x in enumerate(z) if x == "Football" and i > fd), len(z))
        teil += ["", "=== Formdaten (letzte Ergebnisse, neuestes zuerst) ==="] + z[fd + 1:fe]
    except ValueError:
        pass
    # Zahlen, Pfeile und Prozentzeichen auf eine Zeile ziehen
    out = []
    for x in teil:
        if out and re.fullmatch(r"[\d\.\-%▲▼\(\)\+: ]+|-|%", x):
            out[-1] += " " + x
        else:
            out.append(x)
    return [x for x in out if "@" not in x]


def tabelle(liga_slug):
    """Tabelle der Liga (alle Zeilen) und Torschützenliste (erste 30) als kurze Zeilen."""
    out = []
    try:
        z = zeilen(hole(f"/football/{liga_slug}/table.html"))
        i = z.index("Pos")
        kopf = z[i:i + 10]
        out.append(" ".join(kopf))
        j = i + 10
        while j + 10 <= len(z) and z[j].isdigit():
            out.append(" ".join(z[j:j + 10]))
            j += 10
    except (ValueError, OSError):
        out.append("(Tabelle nicht gefunden)")
    try:
        z = zeilen(hole(f"/football/{liga_slug}/top-goal-scorers.html"))
        i = next(n for n, x in enumerate(z) if x.endswith("top scorers") and x[0].isalpha() and "20" in x)
        t = " ".join(z[i + 1:i + 1 + 30 * 12])
        eintraege = re.findall(r"(\d+) (.+?) \( (.+?) \) Last goal: (.+?\)) .*? (\d+) goals", t)
        out.append("")
        out.append("Torschützen (Platz, Spieler, Team, Tore, letztes Tor):")
        for pl, sp, team, letzt, tore in eintraege[:30]:
            out.append(f"{pl}. {sp} ({team}) {tore} – {letzt}")
    except (StopIteration, OSError):
        out.append("(Torschützenliste nicht gefunden)")
    return out


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "liste":
        for t in liste():
            print(" | ".join(t[:4]), "|", BASIS + t[4])
        return
    if len(sys.argv) in (3, 4) and sys.argv[1] == "tag":
        alle = liste()
        tag = sys.argv[3] if len(sys.argv) == 4 else (alle[0][0] if alle else "")
        for t in alle:
            if tag.lower() in t[0].lower() and sys.argv[2].lower() in t[1].lower():
                print(" | ".join(t[:4]), "|", BASIS + t[4])
        return
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    heim, gast = (s.lower().replace(" ", "-") for s in sys.argv[1:3])
    treffer = [t[4] for t in liste() if heim in t[4].lower() and gast in t[4].lower()]
    if not treffer:
        sys.exit("Keine Vorschau in der Übersicht gefunden – Teilnamen prüfen (Sports-Mole-Schreibweise).")
    url = treffer[0]
    h = hole(url)
    z = zeilen(h)
    print("## Vorschau:", BASIS + url)
    kopf, art = artikel(z)
    for k in kopf:
        print("Stand:", k)
    print("\n".join(art))
    # Link „For data analysis … please click here“ – nicht der erste _game_-Link der Seite
    m = re.search(r'For data analysis[^<]*<a href="(/football/[^"]*_game_\d+\.html)"', h)
    if m:
        print("\n## Spielseite:", BASIS + m.group(1))
        print("\n".join(spielseite(zeilen(hole(m.group(1))))))
        liga = m.group(1).split("/")[2]
        print(f"\n## Tabelle und Torschützen ({liga}):")
        print("\n".join(tabelle(liga)))
    else:
        print("\n(Keine Spielseite verlinkt.)")


if __name__ == "__main__":
    main()
