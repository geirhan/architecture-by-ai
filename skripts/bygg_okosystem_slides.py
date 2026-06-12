# -*- coding: utf-8 -*-
"""
Bygger ut presentasjonen «Kunnskapsforvaltning i et økosystemperspektiv»
med perspektivskifte-slidene (verdikjede -> økosystem).

Tar utgangspunkt i den påbegynte fila (slide 1-4: forside, kunnskapsbasert
praksis, aktørene/IGOE, verdikjeden) og APPENDER 6 nye narrative slides.
Innholdet er hentet fra rapporter/verdikjede-som-okosystem.md.
Skriver til en utkast-kopi for trygg gjennomgang før den slås sammen.
"""
import copy
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

_BASE = "/Users/geirkristianhansen/Library/CloudStorage/OneDrive-Helsedirektoratet/PRO-Offentlig KI-tjeneste for målrettede helseråd-HDIR - Dokumenter/Generelt/00 Kunnskapsforvaltning/Presentasjoner"
SRC = _BASE + "/Kunnskapsøkosystemet.pptx"
DST = _BASE + "/Kunnskapsøkosystemet-utkast.pptx"

# Hdir tema-farger
TEAL_DK = RGBColor(0x02, 0x50, 0x69)  # accent1
TEAL    = RGBColor(0x03, 0x7F, 0xA2)  # accent2
BLUE    = RGBColor(0x00, 0x69, 0xE7)  # accent3
MAGENTA = RGBColor(0x7C, 0x14, 0x5C)  # accent4
GREEN   = RGBColor(0x36, 0x65, 0x58)  # accent5
MINT    = RGBColor(0x94, 0xDB, 0xC9)  # accent6
LIGHT   = RGBColor(0xF0, 0xF5, 0xFF)  # lt2
DARK    = RGBColor(0x20, 0x20, 0x20)  # dk1
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
GREY    = RGBColor(0x50, 0x4F, 0x4F)  # dk2

prs = Presentation(SRC)
SW, SH = prs.slide_width, prs.slide_height

def layout(name):
    for l in prs.slide_layouts:
        if l.name == name:
            return l
    raise KeyError(name)

def add_slide(layout_name="Kun tittel"):
    return prs.slides.add_slide(layout(layout_name))

def set_title(slide, text):
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = text
            for p in ph.text_frame.paragraphs:
                for r in p.runs:
                    r.font.color.rgb = TEAL_DK
                    r.font.bold = True
            return ph

def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text

def textbox(slide, l, t, w, h):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tb.text_frame.word_wrap = True
    return tb

def para(tf, text, size=18, color=DARK, bold=False, italic=False,
         align=PP_ALIGN.LEFT, space_after=8, first=False, bullet=False):
    p = tf.paragraphs[0] if first and not tf.paragraphs[0].runs else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    r = p.add_run()
    r.text = text
    f = r.font
    f.size = Pt(size); f.bold = bold; f.italic = italic; f.color.rgb = color
    # fjern/legg punkt
    pPr = p._pPr if p._pPr is not None else p.get_or_add_pPr()
    for tag in ("a:buChar", "a:buAutoNum", "a:buNone"):
        for e in pPr.findall(qn(tag)):
            pPr.remove(e)
    if bullet:
        buFont = pPr.makeelement(qn("a:buFont"), {"typeface": "Arial"})
        buChar = pPr.makeelement(qn("a:buChar"), {"char": "•"})
        pPr.append(buFont); pPr.append(buChar)
        p.level = 0
    else:
        pPr.append(pPr.makeelement(qn("a:buNone"), {}))
    return p

def card(slide, l, t, w, h, fill, line=None, radius=0.10):
    sp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(l), Inches(t), Inches(w), Inches(h))
    sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = Pt(1)
    sp.shadow.inherit = False
    try:
        sp.adjustments[0] = radius
    except Exception:
        pass
    sp.text_frame.word_wrap = True
    sp.text_frame.margin_left = Inches(0.18)
    sp.text_frame.margin_right = Inches(0.18)
    sp.text_frame.margin_top = Inches(0.10)
    sp.text_frame.margin_bottom = Inches(0.10)
    return sp

def footer(slide, text="Basert på notatet «Verdikjeden sett som et økosystem» (rapporter/)"):
    tb = textbox(slide, 0.8, 7.05, 11.7, 0.35)
    para(tb.text_frame, text, size=9, color=GREY, first=True)

# ---------------------------------------------------------------------------
# SLIDE 5 — Men slik treffes beslutningene faktisk
# ---------------------------------------------------------------------------
s = add_slide("Kun tittel")
set_title(s, "Men slik treffes beslutningene faktisk")
tb = textbox(s, 0.8, 2.0, 11.7, 0.9)
para(tb.text_frame, "Innbyggeren og klinikeren venter ikke ved enden av kjeden. "
     "De velger fritt mellom mange kilder samtidig.", size=22, color=DARK,
     bold=True, first=True)

# kilde-chips
kilder = ["Sosiale medier", "KI-tjenester", "UpToDate / BMJ", "NHI.no",
          "Utenlandske nettsider", "Medier", "Venner og familie",
          "Offentlig verdikjede"]
x, y, w, h, gap = 0.8, 3.2, 2.72, 0.62, 0.18
per_row = 4
for i, k in enumerate(kilder):
    row, col = divmod(i, per_row)
    cx = x + col * (w + gap)
    cy = y + row * (h + gap)
    public = (k == "Offentlig verdikjede")
    c = card(s, cx, cy, w, h, TEAL_DK if public else LIGHT)
    para(c.text_frame, k, size=13, bold=public,
         color=WHITE if public else DARK, align=PP_ALIGN.CENTER, first=True)

tb = textbox(s, 0.8, 5.6, 11.7, 1.0)
para(tb.text_frame, "Den offentlige verdikjeden er ÉN kilde blant mange "
     "— og ofte den tregeste.", size=20, color=MAGENTA, bold=True, first=True)
footer(s)
notes(s, "Kilde: [DOK] delrapport 2 kap. 4.3 og 5.4; visualisering verdikjede-naa.html. "
         "Poeng: i en kjedemodell er disse kildene «utenfor kjeden» — i virkeligheten "
         "konkurrerer de om de samme beslutningene. Dette er bruddet som motiverer "
         "perspektivskiftet.")

# ---------------------------------------------------------------------------
# SLIDE 6 — Skift linsen: sett innbyggeren i sentrum
# ---------------------------------------------------------------------------
s = add_slide("Kun tittel")
set_title(s, "Skift linsen: sett innbyggeren i sentrum")

# Sentrert innbygger-pille
goal = card(s, 3.17, 2.2, 7.0, 1.2, TEAL_DK, radius=0.5)
goal.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
para(goal.text_frame, "INNBYGGEREN I SENTRUM: gode, kunnskapsbaserte "
     "helsebeslutninger for hele befolkningen", size=18, color=WHITE, bold=True,
     align=PP_ALIGN.CENTER, first=True)

tb = textbox(s, 0.8, 3.9, 11.7, 2.6)
para(tb.text_frame, "Ikke verdikjeden i sentrum — men innbyggeren. "
     "Det er innbyggere og pasienter som til slutt får nytten av kunnskapen; "
     "verdikjeden blir ett bidrag blant flere, ikke selve systemet.",
     size=20, bold=True, color=DARK, first=True, space_after=14)
para(tb.text_frame, "Det endrer hva som teller som suksess:", size=18,
     color=DARK, space_after=6)
para(tb.text_frame, "Ikke «leverte verdikjeden en retningslinje?»", size=18,
     color=GREY, italic=True, bullet=True)
para(tb.text_frame, "Men «traff innbyggeren og klinikeren en god beslutning "
     "— og bidro vårt tilbud til den, sammenlignet med alternativene de "
     "faktisk brukte?»", size=18, color=BLUE, bold=True, bullet=True)
footer(s, "Se visualiseringene okosystem-verdikjede.html og verdikjede-til-okosystem.html")
notes(s, "Kilde: notat kap. 3.1. Dette er mer enn en visuell omlegging — det endrer "
         "suksesskriteriet fra «leverte vi produktet» til «påvirket vi beslutningen». "
         "Vis gjerne morfe-visualiseringen verdikjede-til-okosystem.html her.")

# ---------------------------------------------------------------------------
# SLIDE 7 — Økosystemet: innbyggeren i sentrum, tre ringer rundt
# ---------------------------------------------------------------------------
s = add_slide("Kun tittel")
set_title(s, "Økosystemet: innbyggeren i sentrum, tre ringer rundt")

spheres = [
    ("Innbyggere og pasienter — i sentrum", "Det er innbyggere og pasienter i "
     "Norge som skal ta, og få nytten av, gode kunnskapsbaserte helsebeslutninger", TEAL_DK,
     "sentrum — målet alt annet tjener"),
    ("Ring 1: Kildene innbyggeren bruker", "Fastlege og helsepersonell, "
     "helsenorge.no, sykehus.no — og NHI.no, KI-tjenester, sosiale medier, medier, "
     "utenlandske nettsider, venner/familie, pasientorg.", TEAL,
     "kanalene innbyggeren faktisk henter kunnskap fra (blå = offentlig, oransje = andre)"),
    ("Ring 2: Kunnskapsprodusenter og kvalitetsvurdering", "FHI, Hdir, RHF, KS, "
     "DMP, Felleskatalogen/RELIS, fagmed. foreninger, Tidsskriftet, universiteter/"
     "høyskoler — og internasjonal forskning, Cochrane/WHO, UpToDate/BMJ, NEL", BLUE,
     "produserer og kvalitetsvurderer kunnskapen kildene formidler"),
    ("Ring 3: Rammesettere og infrastruktur", "Stortinget, HOD, politikere/ledere, "
     "EU, EMA/WHO, Datatilsynet/Språkrådet/PFU, NHN, Helsebiblioteket, EPJ-leverandører", GREEN,
     "ytterst — styrer og muliggjør hele systemet"),
]
y = 1.9
rh = 1.18
gap = 0.12
for i, (name, members, color, role) in enumerate(spheres):
    cy = y + i * (rh + gap)
    # tynn rolle-etikett til venstre
    band = card(s, 0.8, cy, 11.7, rh, color)
    tf = band.text_frame
    tf.word_wrap = True
    para(tf, name, size=16, color=WHITE, bold=True, first=True, space_after=2)
    para(tf, members, size=12.5, color=WHITE, space_after=2)
    para(tf, "Økosystemrolle: " + role, size=11, color=MINT, italic=True)
footer(s, "Aktørplasseringer: [DOK] delrapport 8. Rolletilordning: [ANT]. "
          "Speiler okosystem-verdikjede.html")
notes(s, "Kilde: notat kap. 3.2 (tabell) og okosystem-verdikjede.html. Innbyggeren står "
         "i kjernen; ringene er konsentriske rundt den: kildene innbyggeren bruker innerst "
         "(ring 1, der helsepersonell er én av kildene), så kunnskapsprodusentene (ring 2), "
         "og rammesettere/infrastruktur ytterst (ring 3). Skillet offentlig/andre bæres nå "
         "av farge (blå/oransje), ikke av egne ringer. Økosystemroller "
         "(keystone/plattform/nisje/dominator) er en analytisk [ANT]-tilordning. Merk: "
         "Helsebiblioteket og NHN er keystone/plattform — muliggjørere for store deler av systemet.")

# ---------------------------------------------------------------------------
# SLIDE 8 — Tre ting linsen avdekker
# ---------------------------------------------------------------------------
s = add_slide("Kun tittel")
set_title(s, "Tre ting linsen avdekker")
cols = [
    ("1. Vi konkurrerer om oppmerksomhet",
     "Kvalitet alene vinner ikke. En kvalitetssikret, men treg og lite "
     "tilgjengelig kanal taper for raske alternativer. Derfor er reaktivitet "
     "en kjerneegenskap — ikke bare en ønskelig egenskap.", TEAL),
    ("2. Styring blir orkestrering, ikke kontroll",
     "Vi kan styre den offentlige verdikjeden, men ikke økosystemet. "
     "De fleste kildene innbyggerne bruker ligger utenfor norsk "
     "myndighetsstyring.", MAGENTA),
    ("3. Generativitet — kan andre bygge på oss?",
     "Et sunt økosystem lar andre gjenbruke det offentlige tilbudet. "
     "Strukturert, maskinlesbar kunnskap (jf. EHDS-prinsippene) sprer "
     "kvalitetssikret innhold lenger ut enn våre egne kanaler rekker.", GREEN),
]
cw = 3.7
gap = 0.30
x0 = 0.8
top = 2.1
ch = 4.3
for i, (head, body, color) in enumerate(cols):
    cx = x0 + i * (cw + gap)
    head_box = card(s, cx, top, cw, 1.15, color)
    head_box.text_frame.anchor = MSO_ANCHOR.MIDDLE
    para(head_box.text_frame, head, size=15, color=WHITE, bold=True,
         align=PP_ALIGN.LEFT, first=True)
    body_box = card(s, cx, top + 1.15 + 0.12, cw, ch - 1.15 - 0.12, LIGHT)
    body_box.text_frame.anchor = MSO_ANCHOR.TOP
    para(body_box.text_frame, body, size=14, color=DARK, first=True)
footer(s)
notes(s, "Kilde: notat kap. 4.1 (konkurranse), 4.2 (orkestrering), 4.3 (generativitet). "
         "Disse tre er kjernebudskapet. Punkt 2 skjerper R1: selv et fullkomment "
         "styringsmandat over de offentlige aktørene gir ikke kontroll over økosystemet.")

# ---------------------------------------------------------------------------
# SLIDE 9 — Hva det betyr for utredningen vår
# ---------------------------------------------------------------------------
s = add_slide("Kun tittel")
set_title(s, "Hva det betyr for utredningen vår")
items = [
    ("Skjerper R1 (styringsmandat)",
     "Et mandat over de offentlige aktørene gir ikke kontroll over økosystemet. "
     "Vi trenger både orden i eget hus og en orkestreringsstrategi utad."),
    ("Forklarer to kjerneegenskaper vi kan TAPE",
     "Reaktivitet og tillit/legitimitet er ikke gitt — i et konkurranseutsatt "
     "informasjonsmiljø beholder ikke offentlig kanal oppmerksomheten automatisk."),
    ("Gir de fire løsningsaksene ekstra begrunnelse",
     "Hastighet, sammenheng (= generativitet), forpliktelse og kontinuerlig "
     "oppdatering handler om å hevde seg i økosystemet — ikke bare intern orden."),
    ("Keystone-sårbarheter = systemrisiko",
     "Helsebiblioteket og NHN-plattformen muliggjør store deler av systemet. "
     "Svikt der er ikke en lokal budsjettsak, men en systemrisiko."),
]
y = 2.0
rh = 1.12
gap = 0.14
for i, (head, body) in enumerate(items):
    cy = y + i * (rh + gap)
    # fargestripe
    card(s, 0.8, cy, 0.16, rh, BLUE if i % 2 == 0 else TEAL)
    tb = textbox(s, 1.1, cy, 11.4, rh)
    para(tb.text_frame, head, size=16, color=TEAL_DK, bold=True, first=True, space_after=3)
    para(tb.text_frame, body, size=13.5, color=DARK)
footer(s)
notes(s, "Kilde: notat kap. 4.2, 4.4 og 5 (kobling til analyseapparatet) samt kap. 6 "
         "(konsekvenser). Poeng: linsen erstatter ikke D-ene, R-ene, kjerneegenskapene "
         "eller aksene — den forklarer hvorfor flere av dem ser ut som de gjør, og legger "
         "til en systemdimensjon.")

# ---------------------------------------------------------------------------
# SLIDE 10 — Hva linsen er, og ikke er + landing
# ---------------------------------------------------------------------------
s = add_slide("Kun tittel")
set_title(s, "Hva linsen er — og ikke er")
tb = textbox(s, 0.8, 1.95, 11.7, 2.3)
para(tb.text_frame, "En analytisk lins, ikke et nytt empirisk funn — den "
     "organiserer det vi allerede vet.", size=18, color=DARK, first=True, bullet=True, space_after=10)
para(tb.text_frame, "Erstatter ikke D1–D6, R1–R6, kjerneegenskapene eller "
     "aksene — den forklarer hvorfor de ser ut som de gjør.", size=18,
     color=DARK, bullet=True, space_after=10)
para(tb.text_frame, "Sier noe om RETNING (hvorfor), ikke HVOR LANGT vi skal "
     "gå — det avgjøres i alternativvurderingen.", size=18, color=DARK, bullet=True)

# landingssitat
quote = card(s, 0.8, 4.6, 11.7, 1.9, LIGHT, line=TEAL_DK)
quote.text_frame.anchor = MSO_ANCHOR.MIDDLE
para(quote.text_frame, "«Vi kan styre verdikjeden, men ikke økosystemet — "
     "derfor må vi gjøre det offentlige tilbudet så raskt, tilgjengelig og "
     "gjenbrukbart at innbyggere og andre aktører velger å bruke det.»",
     size=18, color=TEAL_DK, bold=True, italic=True,
     align=PP_ALIGN.CENTER, first=True)
footer(s)
notes(s, "Kilde: notat kap. 7 (forbehold) og kap. 4.2 (landingsbudskap). "
         "Avslutt med landingssetningen. Den binder sammen konkurranse (slide 8.1), "
         "orkestrering (8.2) og generativitet (8.3) i én setning.")

prs.save(DST)
print("Lagret:", DST)
print("Antall slides:", len(prs.slides))
