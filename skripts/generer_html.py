#!/usr/bin/env python3
"""Regenererer HTML-versjonen av utredningen i rapporter/html/.

Konverterer hver delrapport fra markdown til HTML med pandoc og
setter innholdet inn i rapporter/html/template.html med identisk
navigasjonsbar på alle sider. Spesialsidene index.html,
ledersammendrag.html og visualiseringer.html regenereres ikke fra
markdown, men får navigasjonsbaren oppdatert på plass, slik at nye
delrapporter dukker opp i menyen overalt.

Kjøres fra prosjektroten:  python3 skripts/generer_html.py
Krever pandoc på PATH.
"""

import re
import subprocess
import sys
from pathlib import Path

ROT = Path(__file__).resolve().parent.parent
RAPPORTER = ROT / "rapporter"
HTML = RAPPORTER / "html"
TEMPLATE = HTML / "template.html"

STANDARD_UNDERTITTEL = (
    "Del av utredning om ny verdikjede for "
    "kunnskapsforvaltning i helsesektoren"
)

# Rekkefølgen her er rekkefølgen i navigasjonsbaren.
# md=None betyr spesialside som bare får ny nav-blokk.
SIDER = [
    ("index.html", "Forside", None),
    ("ledersammendrag.html", "Ledersammendrag", None),
    ("aktoeranalyse.html", "Aktøranalyse", "aktoeranalyse.md"),
    ("arkitektur-og-komponenter.html", "Arkitektur",
     "arkitektur-og-komponenter.md"),
    ("casestudier-forsinkelser.html", "Casestudier",
     "casestudier-forsinkelser.md"),
    ("dagens-verdikjede.html", "Dagens verdikjede",
     "dagens-verdikjede.md"),
    ("fremtidsscenarioer.html", "Fremtidsscenarioer",
     "fremtidsscenarioer.md"),
    ("helsepersonellplan-2040.html", "Helsepersonellplan 2040",
     "helsepersonellplan-2040.md"),
    ("internasjonale-erfaringer.html", "Internasjonal erfaring",
     "internasjonale-erfaringer.md"),
    ("kildeforankring-slide3.html", "Kildeforankring",
     "kildeforankring-slide3.md"),
    ("llm-muligheter-og-risikoer.html", "LLM muligheter",
     "llm-muligheter-og-risikoer.md"),
    ("ny-verdikjede.html", "Ny verdikjede", "ny-verdikjede.md"),
    ("regulatorisk-etterslep.html", "Regulatorisk etterslep",
     "regulatorisk-etterslep.md"),
    ("rolledeling-sentral-helseforvaltning.html", "Rolledeling",
     "rolledeling-sentral-helseforvaltning.md"),
    ("rottingen-utfordringsbildet.html", "Røttingen-rapporten",
     "rottingen-utfordringsbildet.md"),
    ("samlet-vurdering.html", "Samlet vurdering",
     "samlet-vurdering-kunnskapsforvaltning.md"),
    ("talepunkter-akser.html", "Talepunkter (akser)",
     "talepunkter-akser.md"),
    ("utfordringer-og-flaskehalser.html", "Utfordringer",
     "utfordringer-og-flaskehalser.md"),
    ("verdikjede-som-okosystem.html", "Verdikjede som økosystem",
     "verdikjede-som-okosystem.md"),
    ("visualiseringer.html", "Visualiseringer", None),
]

MD_TIL_HTML = {md: html for html, _, md in SIDER if md}
MD_TIL_HTML["index.md"] = "index.html"


def bygg_nav(aktiv_html):
    linjer = ["<nav>", "  <ul>"]
    for html, etikett, _ in SIDER:
        aktiv = ' class="active"' if html == aktiv_html else ""
        linjer.append(
            f'    <li><a href="{html}"{aktiv}>{etikett}</a></li>'
        )
    linjer += ["  </ul>", "</nav>"]
    return "\n".join(linjer)


def hent_tittel_og_undertittel(md_tekst):
    tittel = None
    undertittel = None
    for linje in md_tekst.splitlines()[:12]:
        if tittel is None and linje.startswith("# "):
            tittel = linje[2:].strip()
        elif undertittel is None and linje.startswith("## "):
            undertittel = linje[3:].strip()
    return tittel or "Uten tittel", undertittel or STANDARD_UNDERTITTEL


def fjern_h1(md_tekst):
    linjer = md_tekst.splitlines()
    for i, linje in enumerate(linjer):
        if linje.startswith("# "):
            return "\n".join(linjer[:i] + linjer[i + 1:])
    return md_tekst


def pandoc(md_tekst):
    resultat = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html"],
        input=md_tekst, capture_output=True, text=True, check=True,
    )
    return resultat.stdout


def skriv_om_md_lenker(html_tekst):
    def erstatt(m):
        md_navn, fragment = m.group(1), m.group(2) or ""
        html_navn = MD_TIL_HTML.get(md_navn)
        if html_navn:
            return f'href="{html_navn}{fragment}"'
        return m.group(0)

    return re.sub(r'href="([\w.-]+\.md)(#[^"]*)?"', erstatt, html_tekst)


def pakk_inn_tabeller(html_tekst):
    html_tekst = html_tekst.replace(
        "<table>", '<div class="table-wrapper">\n<table>'
    )
    return html_tekst.replace("</table>", "</table>\n</div>")


def generer_rapportside(html_navn, md_navn, mal):
    md_tekst = (RAPPORTER / md_navn).read_text(encoding="utf-8")
    tittel, undertittel = hent_tittel_og_undertittel(md_tekst)
    kropp = pandoc(fjern_h1(md_tekst))
    kropp = pakk_inn_tabeller(skriv_om_md_lenker(kropp))
    side = (
        mal.replace("$title$", tittel)
        .replace("$subtitle$", undertittel)
        .replace("$nav$", bygg_nav(html_navn))
        .replace("$body$", kropp)
    )
    (HTML / html_navn).write_text(side, encoding="utf-8")
    print(f"  genererte {html_navn}")


def oppdater_nav(html_navn):
    sti = HTML / html_navn
    innhold = sti.read_text(encoding="utf-8")
    nytt, antall = re.subn(
        r"<nav>.*?</nav>", bygg_nav(html_navn), innhold,
        count=1, flags=re.DOTALL,
    )
    if antall != 1:
        sys.exit(f"FEIL: fant ingen <nav>-blokk i {html_navn}")
    sti.write_text(nytt, encoding="utf-8")
    print(f"  oppdaterte nav i {html_navn}")


def main():
    mal = TEMPLATE.read_text(encoding="utf-8")
    for html_navn, _, md_navn in SIDER:
        if md_navn:
            generer_rapportside(html_navn, md_navn, mal)
        else:
            oppdater_nav(html_navn)
    print("Ferdig.")


if __name__ == "__main__":
    main()
