#!/usr/bin/env python3
"""
Oppdaterer slide 9 i utfordringsbildet-forankring.pptx:
  fra TRE kjerneegenskaper (3 spalter) til FEM (4 spalter + tverrgaaende bunnblokk).
Bevarer malstil ved aa KLONE eksisterende placeholder-XML (arver font/farge fra malen).
Layout: fire likeverdige egenskaper i topprad, tillit/legitimitet som bred bunnblokk.
"""
import copy
from pptx import Presentation
from pptx.util import Emu
from pptx.oxml.ns import qn

PPTX = "/Users/geirkristianhansen/Library/CloudStorage/OneDrive-Helsedirektoratet/PRO-Offentlig KI-tjeneste for målrettede helseråd-HDIR - Dokumenter/Generelt/00 Kunnskapsforvaltning/Presentasjoner/utfordringsbildet-forankring.pptx"

prs = Presentation(PPTX)
slide = prs.slides[8]  # slide 9 (0-indeksert)

# ---- Geometri for fire kolonner + bunnblokk ----
LEFT0 = 695326
RIGHT = 11496674            # hoeyre kant (kol3 L + W i original)
TOTAL_W = RIGHT - LEFT0     # 10801348
GAP = 200000
COL_W = (TOTAL_W - 3 * GAP) // 4   # 2550337
COL_L = [LEFT0 + i * (COL_W + GAP) for i in range(4)]

TITLE_T = 1952624
TITLE_H = 640800
BODY_T = 2682240
BODY_H = 2350000            # krympet for aa gi plass til bunnblokk

BOTTOM_T = 5180000
BOTTOM_H = 1180000

# ---- Hjelpere ----
def shapes_by_text(prefix):
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip().startswith(prefix):
            out.append(sh)
    return out

def set_pos(sh, L, T, W, H):
    sh.left = Emu(int(L)); sh.top = Emu(int(T))
    sh.width = Emu(int(W)); sh.height = Emu(int(H))

def set_title_text(sh, txt):
    """Sett tittel-tekst i en title-placeholder, behold foerste run sin stil."""
    tf = sh.text_frame
    # behold foerste paragraf, fjern ekstra
    p0 = tf.paragraphs[0]
    # tøm runs unntatt aa beholde rPr fra foerste
    runs = p0.runs
    if runs:
        runs[0].text = txt
        for r in runs[1:]:
            r._r.getparent().remove(r._r)
    else:
        p0.add_run().text = txt
    # fjern ekstra paragrafer
    for p in tf.paragraphs[1:]:
        p._p.getparent().remove(p._p)

def set_body_text(sh, lines):
    """Sett brødtekst: liste av (tekst, er_kilde_linje)."""
    tf = sh.text_frame
    # bruk foerste paragraf som mal for rPr
    template_p = tf.paragraphs[0]._p
    # hent rPr fra foerste run om finnes
    first_run = tf.paragraphs[0].runs[0] if tf.paragraphs[0].runs else None
    rpr_xml = None
    if first_run is not None:
        rpr = first_run._r.find(qn('a:rPr'))
        if rpr is not None:
            rpr_xml = copy.deepcopy(rpr)
    # fjern alle paragrafer
    for p in list(tf.paragraphs):
        p._p.getparent().remove(p._p)
    txBody = tf._txBody
    for txt in lines:
        p = txBody.makeelement(qn('a:p'), {})
        r = txBody.makeelement(qn('a:r'), {})
        if rpr_xml is not None:
            r.append(copy.deepcopy(rpr_xml))
        t = txBody.makeelement(qn('a:t'), {})
        t.text = txt
        r.append(t)
        p.append(r)
        txBody.append(p)

# ---- 1. Tittel ----
for sh in slide.shapes:
    if sh.has_text_frame and sh.text_frame.text.strip().startswith("Tre kjerneegenskaper"):
        set_title_text(sh, "Fem kjerneegenskaper verdikjeden mangler")
        break

# ---- 2. Identifiser eksisterende kolonner ----
skal_t = shapes_by_text("Skalerbarhet")[0]
skal_b = shapes_by_text("Kapasiteten")[0]
reak_t = shapes_by_text("Reaktivitet")[0]
reak_b = shapes_by_text("Gjennomløpstiden")[0]
samm_t = shapes_by_text("Sammenheng")[0]
samm_b = shapes_by_text("Stegene")[0]

# ---- 3. Re-posisjoner de tre eksisterende til kol 0,1,2 og oppdater tekst ----
set_pos(skal_t, COL_L[0], TITLE_T, COL_W, TITLE_H)
set_pos(skal_b, COL_L[0], BODY_T, COL_W, BODY_H)
set_body_text(skal_b, ["Kapasiteten øker ikke i takt med forskningsvolumet.", "Knytter til D2 (R3)."])

set_pos(reak_t, COL_L[1], TITLE_T, COL_W, TITLE_H)
set_pos(reak_b, COL_L[1], BODY_T, COL_W, BODY_H)
set_body_text(reak_b, ["Gjennomløpstiden gjør det umulig å respondere raskt på ny evidens, spesielt i kriser.", "Knytter til D1, D6 (R3, R6)."])

set_pos(samm_t, COL_L[2], TITLE_T, COL_W, TITLE_H)
set_pos(samm_b, COL_L[2], BODY_T, COL_W, BODY_H)
set_body_text(samm_b, ["Steg og systemer er ikke koblet slik at informasjonen er konsistent og oppdatert gjennom hele kjeden.", "Knytter til D3 (teknisk), D4 (R4)."])

# ---- 4. Klon Skalerbarhet-paret til kol 3 = Styrbarhet ----
spTree = slide.shapes._spTree
def clone(sh):
    el = copy.deepcopy(sh._element)
    spTree.append(el)
    # returner et python-pptx shape-wrapper
    from pptx.shapes.placeholder import _InheritsTextFrame  # ikke nødvendig
    return el

# klon title
styr_t_el = copy.deepcopy(skal_t._element)
styr_b_el = copy.deepcopy(skal_b._element)
spTree.append(styr_t_el)
spTree.append(styr_b_el)
# nye placeholder-idx for aa unngå kollisjon
def set_ph_idx(el, idx):
    ph = el.find('.//'+qn('p:ph'))
    if ph is not None:
        ph.set('idx', str(idx))
def set_id_name(el, _id, name):
    cNvPr = el.find('.//'+qn('p:cNvPr'))
    if cNvPr is not None:
        cNvPr.set('id', str(_id)); cNvPr.set('name', name)
set_ph_idx(styr_t_el, 20); set_id_name(styr_t_el, 201, "Styr titel")
set_ph_idx(styr_b_el, 21); set_id_name(styr_b_el, 202, "Styr innhold")

# wrap for enklere manipulasjon
from pptx.shapes.autoshape import Shape
styr_t = Shape(styr_t_el, slide.shapes)
styr_b = Shape(styr_b_el, slide.shapes)
set_pos(styr_t, COL_L[3], TITLE_T, COL_W, TITLE_H)
set_pos(styr_b, COL_L[3], BODY_T, COL_W, BODY_H)
set_title_text(styr_t, "Styrbarhet")
set_body_text(styr_b, ["Ingen aktør kan styre kjeden som helhet mot et felles mål; ansvar er fordelt uten helhetlig mandat, og ingen eier implementeringsgapet.", "Knytter til D3 (styring), D4 (R1, R5)."])

# ---- 5. Klon til bred bunnblokk = Tillit og legitimitet ----
till_t_el = copy.deepcopy(skal_t._element)
till_b_el = copy.deepcopy(skal_b._element)
spTree.append(till_t_el)
spTree.append(till_b_el)
set_ph_idx(till_t_el, 22); set_id_name(till_t_el, 203, "Tillit titel")
set_ph_idx(till_b_el, 23); set_id_name(till_b_el, 204, "Tillit innhold")
till_t = Shape(till_t_el, slide.shapes)
till_b = Shape(till_b_el, slide.shapes)
set_pos(till_t, LEFT0, BOTTOM_T, TOTAL_W, 460000)
set_pos(till_b, LEFT0, BOTTOM_T + 470000, TOTAL_W, BOTTOM_H - 470000)
set_title_text(till_t, "Tillit og legitimitet  (tverrgående – følger av de fire over)")
set_body_text(till_b, ["Systemet beholder ikke innbyggeren som foretrukken kilde når treg, generisk og fragmentert informasjon taper for raskere alternativer (generativ KI, sosiale medier). Knytter til D5. Svikt her er i stor grad en effekt av svikt i de fire egenskapene over."])

prs.save(PPTX)
print("Slide 9 oppdatert: fire egenskaper i topp + tillit/legitimitet som bunnblokk.")
print("Totalt lysbilder:", len(prs.slides))
