#!/usr/bin/env python3
"""
Genererer presentasjonen `igoe-aktørmatrise.pptx` i visualiseringer/.

Presentasjonen viser IGOE-matrisen (aktør x prosess) som er utledet av
delrapport 8 (aktoeranalyse.md) kap. 5.2-5.3. Hver aktør markeres med sin
IGOE-rolle (I=Input, G=Guide, O=Output, E=Enabler) i hver av de seks
prosessene i verdikjeden.

Bygger på Helsedirektoratets mal `HdirMal.pptx` slik at master-grafikk,
fonter og logo arves. Tabellinnhold og fargekoding settes programmatisk.

Kjør: python3 skripts/lag_igoe_matrise_pptx.py
"""
import os
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAL = os.path.join(BASE, "HdirMal.pptx")
# ASCII-filnavn bevisst valgt: æøå i filnavn gir NFC/NFD-trøbbel på macOS
# (mellom skriving og gjenåpning) og kan skape friksjon i git/OneDrive-sync.
OUT = os.path.join(BASE, "visualiseringer", "igoe-aktormatrise.pptx")

# ---- Fargepalett (konsistent med prosjektets profil) ----
HDIR_BLA = RGBColor(0x00, 0x33, 0x66)      # mørk blå, jf. HTML-rapportene
GRA_MORK = RGBColor(0x33, 0x33, 0x33)
HVIT = RGBColor(0xFF, 0xFF, 0xFF)
RAD_LYS = RGBColor(0xF2, 0xF5, 0xF8)       # lys blagra for annenhver rad
RAD_HVIT = RGBColor(0xFF, 0xFF, 0xFF)
KANT = RGBColor(0xCC, 0xD4, 0xDD)

# IGOE-rollefarger (tekst i celler)
FARGE_I = RGBColor(0x1B, 0x5E, 0x20)   # Input  - grønn
FARGE_G = RGBColor(0xB7, 0x4A, 0x00)   # Guide  - oransje/brun
FARGE_O = RGBColor(0x0D, 0x47, 0xA1)   # Output - blå
FARGE_E = RGBColor(0x6A, 0x1B, 0x9A)   # Enabler- lilla

ROLLEFARGE = {"I": FARGE_I, "G": FARGE_G, "O": FARGE_O, "E": FARGE_E}

# Layout-indekser i HdirMal.pptx
L_FORSIDE = 0
L_TITTEL_INNHOLD = 5
L_KUN_TITTEL = 10

# ---------------------------------------------------------------------------
# DATA: matrisen fra delrapport 8 kap. 5.2 (invertert fra prosess til aktør)
# ---------------------------------------------------------------------------
PROSESSER = ["P1", "P2", "P3", "P4", "P5", "P6"]

# (aktørnavn, {prosess: "roller"})
MATRISE = [
    ("HOD",                                   {"P1": "G", "P2": "G", "P3": "G"}),
    ("Stortinget",                            {"P2": "G", "P3": "G", "P5": "G", "P6": "G"}),
    ("FHI",                                   {"P1": "O E", "P2": "I", "P6": "I O E"}),
    ("Helsedirektoratet",                     {"P1": "G", "P2": "O E", "P3": "I G", "P6": "I G O"}),
    ("Helsebiblioteket",                      {"P1": "E", "P2": "E", "P3": "E", "P4": "O E"}),
    ("RHF-ene / HF-ene",                      {"P2": "I", "P3": "I O E", "P6": "I"}),
    ("KS / kommunene",                        {"P2": "I", "P3": "I O E"}),
    ("Fagmedisinske foreninger",              {"P2": "I E", "P4": "G O E"}),
    ("Bruker-/pasientorganisasjoner",         {"P2": "I", "P6": "I O E"}),
    ("Internasj. forskning / Cochrane",       {"P1": "I", "P4": "I"}),
    ("UpToDate / BMJ Best Practice",          {"P4": "G O E"}),
    ("Tidsskriftet / Sykepleien Forskning",   {"P4": "G O E"}),
    ("Klinikere (internasjonalt)",            {"P4": "I"}),
    ("Legemiddelselskaper",                   {"P5": "I"}),
    ("EMA",                                   {"P5": "G E"}),
    ("DMP",                                   {"P5": "G O E"}),
    ("Felleskatalogen",                       {"P5": "O E"}),
    ("RELIS",                                 {"P5": "G O E"}),
    ("Helsepersonell / pasienter",            {"P5": "I"}),
    ("helsenorge.no / NHN",                   {"P6": "O E"}),
    ("FNSP",                                  {"P6": "I O E"}),
    ("NHI.no",                                {"P6": "I O E"}),
    ("Medier / helsejournalistikk",           {"P6": "I O E"}),
    ("Pressens Faglige Utvalg (PFU)",         {"P6": "G"}),
]

# ---------------------------------------------------------------------------
# Hjelpere
# ---------------------------------------------------------------------------

def add_slide(prs, layout_idx):
    return prs.slides.add_slide(prs.slide_layouts[layout_idx])


def set_title(slide, text):
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = text
            return ph
    return None


def txbox(slide, l, t, w, h):
    return slide.shapes.add_textbox(Emu(l), Emu(t), Emu(w), Emu(h))


def add_para(tf, runs, first=False, align=PP_ALIGN.LEFT, space_after=6):
    """runs = liste av (tekst, dict med size/bold/color/italic)."""
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    for text, opt in runs:
        r = p.add_run()
        r.text = text
        f = r.font
        f.size = Pt(opt.get("size", 16))
        f.bold = opt.get("bold", False)
        f.italic = opt.get("italic", False)
        f.color.rgb = opt.get("color", GRA_MORK)
        if opt.get("name"):
            f.name = opt["name"]
    return p


# ---------------------------------------------------------------------------
# Bygg presentasjonen
# ---------------------------------------------------------------------------
prs = Presentation(MAL)
# Fjern det ene eksempel-lysbildet i malen – både listeoppføringen OG selve
# slide-parten, ellers blir den liggende igjen som en foreldreløs del og gir
# en duplikat slide1.xml i pakken (som PowerPoint kan reagere på).
xml_slides = prs.slides._sldIdLst
for sldId in list(xml_slides):
    rId = sldId.get(qn("r:id"))
    prs.part.drop_rel(rId)   # gjør slide-parten ureferert → ikke serialisert
    xml_slides.remove(sldId)

SW = prs.slide_width
SH = prs.slide_height

# --- Slide 1: Forside ---
s = add_slide(prs, L_FORSIDE)
set_title(s, "Aktørene i et IGOE-perspektiv")
# undertittel-placeholder (idx 13/14 er body)
for ph in s.placeholders:
    if ph.placeholder_format.idx in (13, 14):
        ph.text = "Hvilken rolle hver aktør spiller i de seks prosessene i verdikjeden for kunnskapsforvaltning"
        break

# --- Slide 2: Hva er IGOE ---
s = add_slide(prs, L_KUN_TITTEL)
set_title(s, "Hva er IGOE?")
tb = txbox(s, 700000, 1700000, 11900000, 5000000)
tf = tb.text_frame
tf.word_wrap = True
add_para(tf, [("IGOE (Inputs, Guides, Outputs, Enablers) beskriver de grunnleggende "
               "komponentene i en prosess – en videreføring av IDEF0, tilpasset "
               "tjenestebaserte virksomheter.", {"size": 17})], first=True, space_after=14)
for bok, farge, navn, forkl in [
    ("I", FARGE_I, "Inputs", "Noe som transformeres eller forbrukes av prosessen. «Hva vi trenger.»"),
    ("G", FARGE_G, "Guides", "Politikk, regelverk, metode og utløsende hendelser som styrer. «Hvorfor, når og hvordan.»"),
    ("O", FARGE_O, "Outputs", "Resultatet av transformasjonen. «Hva vi produserer.»"),
    ("E", FARGE_E, "Enablers", "Ressurser som muliggjør arbeidet uten selv å forbrukes. «Hvor, og med hva og hvem.»"),
]:
    add_para(tf, [
        (f"{bok}  ", {"size": 18, "bold": True, "color": farge}),
        (f"{navn} – ", {"size": 17, "bold": True, "color": farge}),
        (forkl, {"size": 17}),
    ], space_after=8)
add_para(tf, [("Viktig: Inputs endres av prosessen; guides og enablers endres ikke.",
               {"size": 14, "italic": True})], space_after=0)

# --- Slide 3: Slik leser du matrisen ---
s = add_slide(prs, L_KUN_TITTEL)
set_title(s, "Slik leser du matrisen")
tb = txbox(s, 700000, 1700000, 11900000, 5000000)
tf = tb.text_frame
tf.word_wrap = True
add_para(tf, [("Aktører står som rader, de seks prosessene i verdikjeden som kolonner. "
               "Hver celle viser hvilken IGOE-rolle aktøren har i den prosessen.",
               {"size": 17})], first=True, space_after=14)
add_para(tf, [("De seks prosessene (jf. delrapport 8 kap. 5.2):", {"size": 16, "bold": True})], space_after=6)
for kode, navn in [
    ("P1", "Kunnskapsoppsummering (steg 2)"),
    ("P2", "Retningslinjeutvikling (strøm 3a)"),
    ("P3", "Implementering i helsetjenesten (strøm 3a)"),
    ("P4", "Klinisk kunnskapssammenstilling (strøm 3b)"),
    ("P5", "Legemiddelgodkjenning og -informasjon (strøm 3c)"),
    ("P6", "Innbyggerrettet formidling (strøm 3d)"),
]:
    add_para(tf, [
        (f"{kode}  ", {"size": 16, "bold": True, "color": HDIR_BLA}),
        (navn, {"size": 16}),
    ], space_after=4)
add_para(tf, [("Tom celle = aktøren er ikke nevnt i den prosessen i kap. 5.2.",
               {"size": 14, "italic": True})], space_after=0)

# --- Slide 4: Selve matrisen ---
s = add_slide(prs, L_KUN_TITTEL)
set_title(s, "IGOE-matrise: aktør × prosess")

n_rows = len(MATRISE) + 1
n_cols = 1 + len(PROSESSER)
tbl_l, tbl_t = 360000, 1300000
tbl_w = SW - 2 * 360000
tbl_h = SH - tbl_t - 360000
gfx = s.shapes.add_table(n_rows, n_cols, Emu(tbl_l), Emu(tbl_t), Emu(tbl_w), Emu(tbl_h))
table = gfx.table

# Kolonnebredder: aktørkolonne bred, prosesskolonner like
akt_w = int(tbl_w * 0.34)
proc_w = (tbl_w - akt_w) // len(PROSESSER)
table.columns[0].width = Emu(akt_w)
for i in range(1, n_cols):
    table.columns[i].width = Emu(proc_w)

# Slå av PowerPoints innebygde tabellstil-banding (vi styrer farger selv)
tblPr = table._tbl.tblPr
tblPr.set("firstRow", "0")
tblPr.set("bandRow", "0")


def style_cell(cell, fill=None, anchor=MSO_ANCHOR.MIDDLE):
    cell.vertical_anchor = anchor
    cell.margin_left = Emu(45000)
    cell.margin_right = Emu(45000)
    cell.margin_top = Emu(18000)
    cell.margin_bottom = Emu(18000)
    if fill is not None:
        cell.fill.solid()
        cell.fill.fore_color.rgb = fill
    else:
        cell.fill.background()


def header_cell(cell, text):
    style_cell(cell, fill=HDIR_BLA)
    tf = cell.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = HVIT


# Header-rad
header_cell(table.cell(0, 0), "Aktør")
for j, pkode in enumerate(PROSESSER, start=1):
    header_cell(table.cell(0, j), pkode)

# Datarader
for ri, (aktor, roller) in enumerate(MATRISE, start=1):
    radfarge = RAD_LYS if ri % 2 == 0 else RAD_HVIT
    # aktørcelle
    c = table.cell(ri, 0)
    style_cell(c, fill=radfarge)
    p = c.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run(); r.text = aktor
    r.font.size = Pt(11.5); r.font.bold = True; r.font.color.rgb = GRA_MORK
    # prosesscellene
    for j, pkode in enumerate(PROSESSER, start=1):
        c = table.cell(ri, j)
        style_cell(c, fill=radfarge)
        tf = c.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        koder = roller.get(pkode, "").split()
        if not koder:
            continue
        for k, kode in enumerate(koder):
            rr = p.add_run()
            rr.text = (" " if k else "") + kode
            rr.font.size = Pt(12); rr.font.bold = True
            rr.font.color.rgb = ROLLEFARGE.get(kode, GRA_MORK)

# Liten fargeforklaring nederst (egen tekstboks over tabellens nederste kant er vanskelig;
# legger den som tynn rad-uavhengig boks øverst høyre i stedet)
leg = txbox(s, tbl_l, 900000, tbl_w, 360000)
ltf = leg.text_frame
lp = ltf.paragraphs[0]
lp.alignment = PP_ALIGN.LEFT
for kode, navn, farge in [("I", "Input", FARGE_I), ("G", "Guide", FARGE_G),
                           ("O", "Output", FARGE_O), ("E", "Enabler", FARGE_E)]:
    r = lp.add_run(); r.text = f"{kode}={navn}    "
    r.font.size = Pt(12); r.font.bold = True; r.font.color.rgb = farge

# --- Slide 5: Hovedfunn ---
s = add_slide(prs, L_KUN_TITTEL)
set_title(s, "Hva matrisen viser")
tb = txbox(s, 700000, 1550000, 11900000, 5300000)
tf = tb.text_frame
tf.word_wrap = True
funn = [
    ("HOD og Stortinget styrer, men transformerer ingenting.",
     "De opptrer kun som guide-settere (G) – aldri I, O eller E."),
    ("FHI og Helsedirektoratet har bredest fotavtrykk og veksler rolle.",
     "FHI er output-produsent i P1, men kun input-leverandør i P2 – det er Hdir som lager det normerende produktet."),
    ("Helsebiblioteket er enabler i fire prosesser (P1–P4) uten egen output.",
     "En sårbarhet: kuttene i 2023 (Cochrane Library, Embase) rammet store deler av verdikjeden samtidig."),
    ("RHF/HF og KS/kommune er I+O+E i samme prosess (P3).",
     "De både mottar, transformerer og muliggjør implementeringen – med tydelig enabler-asymmetri mot primærhelsetjenesten."),
    ("P6 har flest output-produsenter, men sprikende guides.",
     "Hdir-utgiveransvar vs. PFUs Vær Varsom vs. organisasjonenes vedtekter – ingen innebygd konsistensmekanisme."),
]
first = True
for tittel, brod in funn:
    add_para(tf, [(tittel, {"size": 16, "bold": True, "color": HDIR_BLA})],
             first=first, space_after=2)
    first = False
    add_para(tf, [(brod, {"size": 14})], space_after=12)

# --- Slide 6: Kilde og forbehold ---
s = add_slide(prs, L_KUN_TITTEL)
set_title(s, "Kilde og forbehold")
tb = txbox(s, 700000, 1700000, 11900000, 4800000)
tf = tb.text_frame
tf.word_wrap = True
add_para(tf, [("Kildegrunnlag", {"size": 17, "bold": True, "color": HDIR_BLA})],
         first=True, space_after=4)
add_para(tf, [("Matrisen er utledet av delrapport 8 – Aktøranalyse "
               "(aktoeranalyse.md), kap. 5.2 (IGOE per prosess) og kap. 5.3 "
               "(observasjoner). Rollene er invertert fra prosess-perspektiv til "
               "aktør-perspektiv.", {"size": 15})], space_after=14)
add_para(tf, [("Forbehold", {"size": 17, "bold": True, "color": HDIR_BLA})], space_after=4)
add_para(tf, [("• IGOE er et prosessrammeverk. Matrisen er en analytisk lins som "
               "viser aktørenes roller, ikke et nytt empirisk funn.", {"size": 15})],
         space_after=4)
add_para(tf, [("• Tomme celler betyr «ikke nevnt i kap. 5.2», ikke nødvendigvis "
               "«ingen rolle».", {"size": 15})], space_after=4)
add_para(tf, [("• EMA er omtalt som del av DMPs rammeverk i dp8 og har ingen egen "
               "kildeforankret aktørprofil.", {"size": 15})], space_after=14)
add_para(tf, [("Delrapport 8 har status: Forankret.", {"size": 13, "italic": True})],
         space_after=0)

prs.save(OUT)
print("Lagret:", OUT)
print("Antall lysbilder:", len(prs.slides._sldIdLst))
