#!/usr/bin/env python3
"""Genererer PDF-versjoner av utredningens rapporter.

Designet er inspirert av Helsedirektoratets rapportmal
(referanse: IS-1870): petrolfarget tittelbånd på forsiden,
kolofonside på hel petrolbakgrunn, overskrifter i mørk petrol,
sidetall nede til høyre. Offisiell logo og forsidefoto inngår
ikke — logoposisjonen bruker ordmerke i tekst. Farger og
metadata konfigureres under.

Krav: pandoc og weasyprint på PATH.

Bruk:
    python3 skripts/generer_pdf.py            # alt
    python3 skripts/generer_pdf.py --samlet   # kun samle-PDF-en
"""

import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

ROT = Path(__file__).resolve().parent.parent
RAPPORTER = ROT / "rapporter"
UT = RAPPORTER / "pdf"

# ---------------------------------------------------------------
# Konfigurasjon
# ---------------------------------------------------------------

PETROL = "#0093A8"        # primærfarge (tilnærmet Hdir-petrol)
PETROL_MORK = "#0F4C5C"   # overskrifter
PETROL_LYS = "#E5F4F6"    # tabellstriper/bokser
TEKST = "#222222"
FONT = '"Helvetica Neue", Helvetica, Arial, sans-serif'

UTGIVER = "Helsedirektoratet"
PROSJEKT = ("Utredning om ny verdikjede for "
            "kunnskapsforvaltning i helsesektoren")

# Delrapportene samles i én PDF, i denne rekkefølgen.
DELRAPPORTER = [
    "dagens-verdikjede.md",
    "utfordringer-og-flaskehalser.md",
    "llm-muligheter-og-risikoer.md",
    "ny-verdikjede.md",
    "arkitektur-og-komponenter.md",
    "internasjonale-erfaringer.md",
    "samlet-vurdering-kunnskapsforvaltning.md",
    "aktoeranalyse.md",
    "fremtidsscenarioer.md",
]

# Øvrige rapporter får hver sin PDF (samme utvalg som
# HTML-versjonen, jf. skripts/generer_html.py).
ENKELTRAPPORTER = [
    "casestudier-forsinkelser.md",
    "helsepersonellplan-2040.md",
    "kildeforankring-slide3.md",
    "profesjonsforeninger-normering.md",
    "regulatorisk-etterslep.md",
    "rolledeling-sentral-helseforvaltning.md",
    "rottingen-utfordringsbildet.md",
    "talepunkter-akser.md",
    "verdikjede-som-okosystem.md",
]

SAMLET_TITTEL = ("Ny verdikjede for kunnskapsforvaltning "
                 "i helsesektoren")
SAMLET_FIL = "utredning-samlet.pdf"

# ---------------------------------------------------------------
# CSS (Hdir-inspirert rapportmal)
# ---------------------------------------------------------------

CSS = f"""
@page {{
  size: A4;
  margin: 25mm 22mm 22mm 22mm;
  @bottom-right {{
    content: counter(page);
    font-family: {FONT};
    font-size: 9pt;
    color: {PETROL_MORK};
  }}
  @top-left {{
    content: string(rapporttittel);
    font-family: {FONT};
    font-size: 8pt;
    color: #777777;
  }}
}}
@page forside {{ margin: 0; @bottom-right {{ content: none; }}
  @top-left {{ content: none; }} }}
@page kolofon {{ margin: 0; @bottom-right {{ content: none; }}
  @top-left {{ content: none; }} }}

html {{ font-family: {FONT}; font-size: 10.5pt;
  line-height: 1.5; color: {TEKST}; }}
body {{ margin: 0; }}

/* Forside */
.forside, .forside * {{ box-sizing: border-box; }}
.forside {{ page: forside; width: 210mm; height: 296mm;
  position: relative; page-break-after: always; }}
.forside .topp {{ height: 192mm; background: #ffffff;
  position: relative; }}
.forside .ordmerke {{ position: absolute; right: 14mm;
  bottom: 6mm; font-size: 13pt; font-weight: bold;
  color: {PETROL_MORK}; }}
.forside .kategoristripe {{ position: absolute; left: 0;
  bottom: 0; width: 9mm; height: 150mm; background: {PETROL};
  color: #ffffff; }}
.forside .kategoristripe span {{ display: block;
  transform: rotate(-90deg) translateX(-60mm);
  transform-origin: top left; margin-left: 2.6mm;
  font-size: 9pt; letter-spacing: 0.5pt; white-space: nowrap; }}
.forside .tittelband {{ height: 104mm; background: {PETROL};
  padding: 12mm 20mm 0 24mm; }}
.forside .tittelband h1 {{ color: #ffffff; font-size: 24pt;
  line-height: 1.25; margin: 0 0 6mm 0; border: none; }}
.forside .tittelband .undertittel {{ color: #ffffff;
  font-size: 12pt; opacity: 0.92; }}
.forside .tittelband .dato {{ color: #ffffff; font-size: 10pt;
  margin-top: 8mm; opacity: 0.85; }}

/* Kolofon */
.kolofon {{ page: kolofon; width: 210mm; height: 296mm;
  background: {PETROL}; color: #ffffff;
  padding: 40mm 0 0 24mm; box-sizing: border-box;
  page-break-after: always; }}
.kolofon table {{ border: none; font-size: 10pt; }}
.kolofon td {{ border: none; padding: 1.2mm 8mm 1.2mm 0;
  vertical-align: top; color: #ffffff; }}
.kolofon td:first-child {{ width: 42mm; }}

/* Innholdsfortegnelse */
.innhold {{ page-break-after: always; }}
.innhold h1 {{ color: {PETROL}; font-size: 20pt;
  border: none; }}
.innhold ol {{ list-style: none; padding: 0; margin: 0; }}
.innhold li {{ margin: 1.2mm 0; }}
.innhold li.niv2 {{ margin-left: 8mm; font-size: 9.5pt; }}
.innhold a {{ color: {TEKST}; text-decoration: none; }}
.innhold a::after {{ content: leader('.') " "
  target-counter(attr(href), page); }}

/* Delrapport-skilleside */
.delskille {{ page-break-before: always; }}

/* Overskrifter */
h1 {{ color: {PETROL_MORK}; font-size: 22pt; font-weight: bold;
  margin: 0 0 8mm 0; line-height: 1.2;
  string-set: rapporttittel content(); }}
h2 {{ color: {PETROL_MORK}; font-size: 14pt; margin: 8mm 0 3mm 0;
  page-break-after: avoid; }}
h3 {{ color: {PETROL_MORK}; font-size: 12pt; margin: 6mm 0 2mm 0;
  page-break-after: avoid; }}
h4 {{ color: {PETROL_MORK}; font-size: 10.5pt;
  margin: 5mm 0 2mm 0; page-break-after: avoid; }}

p {{ margin: 0 0 3mm 0; }}
li {{ margin-bottom: 1mm; }}

/* Tabeller */
table {{ border-collapse: collapse; width: 100%;
  font-size: 8.5pt; margin: 3mm 0 5mm 0; }}
th {{ background: {PETROL}; color: #ffffff; text-align: left;
  padding: 1.6mm 2mm; }}
td {{ border-bottom: 0.3pt solid #bbbbbb; padding: 1.4mm 2mm;
  vertical-align: top; }}
tr:nth-child(even) td {{ background: {PETROL_LYS}; }}

blockquote {{ border-left: 1.2mm solid {PETROL};
  margin: 3mm 0; padding: 1mm 0 1mm 5mm; color: #444444; }}
code {{ font-family: Menlo, monospace; font-size: 8.5pt;
  background: #f2f2f2; padding: 0 1mm; }}
pre {{ background: #f2f2f2; padding: 3mm; font-size: 8pt;
  white-space: pre-wrap; }}
hr {{ border: none; border-top: 0.4pt solid #bbbbbb;
  margin: 6mm 0; }}
a {{ color: {PETROL_MORK}; }}
img {{ max-width: 100%; }}

/* Kolofon-overstyringer (etter generelle tabellregler) */
.kolofon {{ box-sizing: border-box; }}
.kolofon table {{ font-size: 10pt; }}
.kolofon tr td {{ background: transparent !important;
  border: none !important; color: #ffffff; }}
"""

# ---------------------------------------------------------------
# Hjelpefunksjoner
# ---------------------------------------------------------------


def sjekk_verktoy():
    for verktoy in ("pandoc", "weasyprint"):
        try:
            subprocess.run([verktoy, "--version"],
                           capture_output=True, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError):
            sys.exit(f"FEIL: {verktoy} er ikke tilgjengelig. "
                     "Installer med Homebrew.")


def hent_tittel(md_tekst):
    m = re.search(r"^#\s+(.+)$", md_tekst, re.MULTILINE)
    return m.group(1).strip() if m else "Uten tittel"


def md_til_html(sti, id_prefix):
    """Konverterer én markdownfil til et HTML-fragment."""
    resultat = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html",
         "--id-prefix", id_prefix, str(sti)],
        capture_output=True, text=True, check=True)
    html = resultat.stdout
    # Interne .md-lenker gir ikke mening i PDF: gjør dem om
    # til ren tekst. (Pandoc kan bryte attributter over flere
    # linjer, derfor \s-toleranse.)
    html = re.sub(
        r'<a\s[^>]*href="[^"]*\.md[^"]*"[^>]*>(.*?)</a>',
        r"\1", html, flags=re.DOTALL)
    return html


def bygg_innhold(html_deler):
    """Innholdsfortegnelse (h1 + h2) med sidetall via CSS."""
    rader = []
    for del_html in html_deler:
        for m in re.finditer(
                r'<h([12])\s+id="([^"]+)"[^>]*>(.*?)</h\1>',
                del_html, re.DOTALL):
            niva, hid, tekst = m.groups()
            ren = re.sub(r"<[^>]+>", "", tekst).strip()
            if ren.startswith("Del av utredning"):
                continue
            klasse = ' class="niv2"' if niva == "2" else ""
            rader.append(
                f'<li{klasse}><a href="#{hid}">{ren}</a></li>')
    return ('<section class="innhold"><h1>Innhold</h1><ol>'
            + "\n".join(rader) + "</ol></section>")


def forside(tittel, undertittel, kategori, dato_str):
    return f"""
<div class="forside">
  <div class="topp">
    <div class="kategoristripe"><span>{kategori}</span></div>
    <div class="ordmerke">{UTGIVER}</div>
  </div>
  <div class="tittelband">
    <h1 style="string-set: none;">{tittel}</h1>
    <div class="undertittel">{undertittel}</div>
    <div class="dato">{dato_str}</div>
  </div>
</div>"""


def kolofon(tittel, dato_str):
    return f"""
<div class="kolofon">
  <table>
    <tr><td>Rapportens tittel:</td><td>{tittel}</td></tr>
    <tr><td>Utgitt:</td><td>{dato_str}</td></tr>
    <tr><td>Utgitt av:</td><td>{UTGIVER}</td></tr>
    <tr><td>Prosjekt:</td><td>{PROSJEKT}</td></tr>
    <tr><td>Merknad:</td><td>Arbeidsdokument generert fra
      utredningens markdownkilder. Utsagn er merket [DOK]
      (dokumentert) eller [ANT] (antakelse/analytisk
      vurdering).</td></tr>
  </table>
</div>"""


def lag_pdf(html_kropp, ut_fil):
    dokument = (f"<!DOCTYPE html><html lang='nb'><head>"
                f"<meta charset='utf-8'>"
                f"<style>{CSS}</style></head>"
                f"<body>{html_kropp}</body></html>")
    with tempfile.NamedTemporaryFile(
            "w", suffix=".html", delete=False,
            encoding="utf-8") as f:
        f.write(dokument)
        tmp = f.name
    subprocess.run(
        ["weasyprint", tmp, str(ut_fil)],
        check=True, capture_output=True, text=True)
    Path(tmp).unlink()
    print(f"  genererte {ut_fil.name}")


# ---------------------------------------------------------------
# Hoveddel
# ---------------------------------------------------------------


def generer_samlet(dato_str):
    deler = []
    for i, navn in enumerate(DELRAPPORTER):
        sti = RAPPORTER / navn
        del_html = md_til_html(sti, f"d{i}-")
        deler.append(f'<section class="delskille">{del_html}'
                     f"</section>")
    kropp = (forside(SAMLET_TITTEL,
                     "Samlet utredning — delrapport 1–9",
                     "Rapport", dato_str)
             + kolofon(SAMLET_TITTEL, dato_str)
             + bygg_innhold(deler)
             + "\n".join(deler))
    lag_pdf(kropp, UT / SAMLET_FIL)


def generer_enkelt(navn, dato_str):
    sti = RAPPORTER / navn
    md_tekst = sti.read_text(encoding="utf-8")
    tittel = hent_tittel(md_tekst)
    del_html = md_til_html(sti, "r-")
    kropp = (forside(tittel, PROSJEKT, "Rapport", dato_str)
             + kolofon(tittel, dato_str)
             + bygg_innhold([del_html])
             + f'<section class="delskille">{del_html}</section>')
    lag_pdf(kropp, UT / (sti.stem + ".pdf"))


def main():
    sjekk_verktoy()
    UT.mkdir(exist_ok=True)
    dato_str = date.today().strftime("%d.%m.%Y")
    generer_samlet(dato_str)
    if "--samlet" not in sys.argv:
        for navn in ENKELTRAPPORTER:
            generer_enkelt(navn, dato_str)
    print("Ferdig.")


if __name__ == "__main__":
    main()
