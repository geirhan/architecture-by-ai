#!/usr/bin/env python3
"""
Genererer HTML-versjoner av alle markdown-rapporter i rapporter/.
Oppdager automatisk alle .md-filer og utleder tittel fra H1-overskriften.
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

SUBTITLE = "Del av utredning om ny verdikjede for kunnskapsforvaltning i helsesektoren"

# Filer som ikke skal konverteres (indeksfiler o.l.)
SKIP_FILES = {"index.md"}

# Overstyring av navigasjonsnavn og HTML-filnavn per markdown-fil.
# Filer som ikke er listet her får automatisk generert navn.
# Format: "markdown-fil.md": ("html-fil.html", "Navigasjonsnavn")
OVERRIDES = {
    "dagens-verdikjede.md": ("dagens-verdikjede.html", "Dagens verdikjede"),
    "utfordringer-og-flaskehalser.md": ("utfordringer-og-flaskehalser.html", "Utfordringer"),
    "llm-muligheter-og-risikoer.md": ("llm-muligheter-og-risikoer.html", "LLM muligheter"),
    "ny-verdikjede.md": ("ny-verdikjede.html", "Ny verdikjede"),
    "arkitektur-og-komponenter.md": ("arkitektur-og-komponenter.html", "Arkitektur"),
    "internasjonale-erfaringer.md": ("internasjonale-erfaringer.html", "Internasjonal erfaring"),
    "samlet-vurdering-kunnskapsforvaltning.md": ("samlet-vurdering.html", "Samlet vurdering"),
    "aktoeranalyse.md": ("aktoeranalyse.html", "Aktøranalyse"),
}

# Faste navigasjonselementer som alltid vises først/sist
STATIC_NAV_START = [
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


def extract_title_from_md(md_path: Path) -> str:
    """Hent H1-overskriften fra markdown-filen som tittel."""
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return md_path.stem.replace("-", " ").title()


def make_nav_name(title: str) -> str:
    """Lag kort navigasjonsnavn fra tittelen.

    Bruker første meningsfulle del av tittelen etter eventuelt
    'Delrapport N: ' prefix. Kutter ved naturlige grenser for å
    holde navigasjonen kompakt men lesbar.
    """
    # Fjern "Delrapport N: " prefix
    nav = re.sub(r"^Delrapport \d+:\s*", "", title)
    # Prøv å kutte ved en naturlig grense hvis tittelen er lang
    if len(nav) > 25:
        for sep in [" – ", " - "]:
            idx = nav.find(sep)
            if 0 < idx < 35:
                nav = nav[:idx]
                break
        else:
            # Kutt ved siste mellomrom før 25 tegn
            cut = nav.rfind(" ", 0, 25)
            if cut > 10:
                nav = nav[:cut]
    return nav


def discover_reports() -> list[tuple[Path, str, str, str]]:
    """
    Oppdag alle .md-filer i rapporter/ og returner sortert liste med
    (md_path, html_filnavn, tittel, navigasjonsnavn).

    Bruker OVERRIDES for kjente filer, og genererer automatisk
    for nye filer som ikke er konfigurert.
    """
    reports = []
    for md_path in sorted(RAPPORT_DIR.glob("*.md")):
        if md_path.name in SKIP_FILES:
            continue
        title = extract_title_from_md(md_path)
        if md_path.name in OVERRIDES:
            html_name, nav_name = OVERRIDES[md_path.name]
        else:
            html_name = md_path.stem + ".html"
            nav_name = make_nav_name(title)
        reports.append((md_path, html_name, title, nav_name))
    return reports


def generate_nav(reports: list, active_html: str) -> str:
    """Generer navigasjonsbar-HTML med aktiv side markert."""
    items = []

    for href, label in STATIC_NAV_START:
        cls = ' class="active"' if href == active_html else ""
        items.append(f'    <li><a href="{href}"{cls}>{label}</a></li>')

    for _, html_fil, _, nav_navn in reports:
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


def convert_report(reports: list, md_path: Path, html_fil: str, tittel: str) -> bool:
    """Konverter én rapport fra markdown til HTML."""
    html_path = HTML_DIR / html_fil

    template = TEMPLATE.read_text(encoding="utf-8")
    nav_html = generate_nav(reports, html_fil)
    body_html = md_to_html_body(md_path)

    html = template.replace("$title$", tittel)
    html = html.replace("$subtitle$", SUBTITLE)
    html = html.replace("$nav$", nav_html)
    html = html.replace("$body$", body_html)

    html_path.write_text(html, encoding="utf-8")
    print(f"  OK: {md_path.name} -> {html_fil}")
    return True


def main():
    check_pandoc()

    if not TEMPLATE.exists():
        print(f"FEIL: Template ikke funnet: {TEMPLATE}")
        sys.exit(1)

    reports = discover_reports()

    if not reports:
        print("Ingen markdown-rapporter funnet i rapporter/")
        sys.exit(0)

    print(f"Fant {len(reports)} markdown-rapporter, genererer HTML...\n")

    converted = 0
    for md_path, html_fil, tittel, _ in reports:
        if convert_report(reports, md_path, html_fil, tittel):
            converted += 1

    print(f"\nFerdig. {converted} rapporter konvertert til {HTML_DIR}/")


if __name__ == "__main__":
    main()
