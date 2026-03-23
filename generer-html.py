#!/usr/bin/env python3
"""
Genererer HTML-versjoner av alle markdown-rapporter.
Bruker pandoc for markdown→HTML-konvertering og prosjektets template.
"""

import subprocess
import sys
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
RAPPORT_DIR = SCRIPT_DIR / "rapporter"
HTML_DIR = RAPPORT_DIR / "html"
TEMPLATE = HTML_DIR / "template.html"

# Mapping: (markdown-fil, html-fil, full tittel, navigasjonsnavn)
RAPPORTER = [
    ("dagens-verdikjede.md", "dagens-verdikjede.html",
     "Delrapport 1: Dagens verdikjede for kunnskapsforvaltning", "Dagens verdikjede"),
    ("utfordringer-og-flaskehalser.md", "utfordringer-og-flaskehalser.html",
     "Delrapport 2: Utfordringer og flaskehalser", "Utfordringer"),
    ("llm-muligheter-og-risikoer.md", "llm-muligheter-og-risikoer.html",
     "Delrapport 3: Store språkmodeller – muligheter og risikoer", "LLM muligheter"),
    ("ny-verdikjede.md", "ny-verdikjede.html",
     "Delrapport 4: Alternativer for ny verdikjede", "Ny verdikjede"),
    ("arkitektur-og-komponenter.md", "arkitektur-og-komponenter.html",
     "Delrapport 5: Arkitektur og komponenter", "Arkitektur"),
    ("internasjonale-erfaringer.md", "internasjonale-erfaringer.html",
     "Delrapport 6: Internasjonale erfaringer", "Internasjonale erfaringer"),
    ("samlet-vurdering-kunnskapsforvaltning.md", "samlet-vurdering.html",
     "Delrapport 7: Samlet vurdering og anbefaling", "Samlet vurdering"),
    ("aktoeranalyse.md", "aktoeranalyse.html",
     "Delrapport 8: Aktøranalyse for verdikjeden", "Aktøranalyse"),
]

SUBTITLE = "Del av utredning om ny verdikjede for kunnskapsforvaltning i helsesektoren"

# Faste navigasjonselementer (forside, ledersammendrag, visualiseringer)
STATIC_NAV = [
    ("index.html", "Forside"),
    ("ledersammendrag.html", "Ledersammendrag"),
]
STATIC_NAV_END = [
    ("visualiseringer.html", "Visualiseringer"),
]


def check_pandoc():
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("FEIL: pandoc er ikke installert. Kjør: brew install pandoc")
        sys.exit(1)


def generate_nav(active_html: str) -> str:
    """Generer navigasjonsbar-HTML med aktiv side markert."""
    items = []

    for href, label in STATIC_NAV:
        cls = ' class="active"' if href == active_html else ""
        items.append(f'    <li><a href="{href}"{cls}>{label}</a></li>')

    for _, html_fil, _, nav_navn in RAPPORTER:
        cls = ' class="active"' if html_fil == active_html else ""
        items.append(f'    <li><a href="{html_fil}"{cls}>{nav_navn}</a></li>')

    for href, label in STATIC_NAV_END:
        cls = ' class="active"' if href == active_html else ""
        items.append(f'    <li><a href="{href}"{cls}>{label}</a></li>')

    return "<nav>\n  <ul>\n" + "\n".join(items) + "\n  </ul>\n</nav>"


def md_to_html_body(md_path: Path) -> str:
    """Konverter markdown til HTML-fragment med pandoc."""
    result = subprocess.run(
        [
            "pandoc", str(md_path),
            "--from", "markdown+pipe_tables+fenced_code_blocks+backtick_code_blocks+strikeout",
            "--to", "html5",
            "--strip-comments",
            "--syntax-highlighting=none",
        ],
        capture_output=True, text=True, check=True,
    )
    body = result.stdout

    # Fjern første H1 (den brukes som tittel i header)
    body = re.sub(r"<h1[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.DOTALL)

    return body


def convert_report(md_fil: str, html_fil: str, tittel: str):
    """Konverter én rapport fra markdown til HTML."""
    md_path = RAPPORT_DIR / md_fil
    html_path = HTML_DIR / html_fil

    if not md_path.exists():
        print(f"  ADVARSEL: {md_path} finnes ikke, hopper over")
        return False

    template = TEMPLATE.read_text(encoding="utf-8")
    nav_html = generate_nav(html_fil)
    body_html = md_to_html_body(md_path)

    html = template.replace("$title$", tittel)
    html = html.replace("$subtitle$", SUBTITLE)
    html = html.replace("$nav$", nav_html)
    html = html.replace("$body$", body_html)

    html_path.write_text(html, encoding="utf-8")
    print(f"  OK: {md_fil} -> {html_fil}")
    return True


def main():
    check_pandoc()

    if not TEMPLATE.exists():
        print(f"FEIL: Template ikke funnet: {TEMPLATE}")
        sys.exit(1)

    print("Genererer HTML fra markdown-rapporter...\n")

    converted = 0
    for md_fil, html_fil, tittel, _ in RAPPORTER:
        if convert_report(md_fil, html_fil, tittel):
            converted += 1

    print(f"\nFerdig. {converted} rapporter konvertert til {HTML_DIR}/")


if __name__ == "__main__":
    main()
