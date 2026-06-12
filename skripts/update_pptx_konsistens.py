#!/usr/bin/env python3
"""
Konsistensoppdatering av utfordringsbildet-forankring.pptx
(2026-05-27, etter samme prinsipp som rapport-ryddingen):

1. Slide 5: "Fem utfordringer med verdikjeden" -> "Fem kjerneegenskaper
   verdikjeden mangler" (speilet av slide 9-tittel).
2. Slide 11 (agenda): "Tre kjerneegenskaper verdikjeden mangler" ->
   "Fem kjerneegenskaper verdikjeden mangler".
3. Slide 13 (D1+D2): fjern udokumenterte tall "2-3 år fra forskning
   til retningslinje" og "6-12 måneder videre til oppdatert
   innbyggerinformasjon", erstatt med case-spennvidde.

Bevarer all formatering ved å manipulere kun .text på runs der mulig,
eller erstatte hele paragrafer ved å beholde første run sin rPr.
"""
import copy
from pptx import Presentation
from pptx.oxml.ns import qn

PPTX = "/Users/geirkristianhansen/Library/CloudStorage/OneDrive-Helsedirektoratet/PRO-Offentlig KI-tjeneste for målrettede helseråd-HDIR - Dokumenter/Generelt/00 Kunnskapsforvaltning/Presentasjoner/utfordringsbildet-forankring.pptx"

prs = Presentation(PPTX)


def replace_run_text(shape, old_text, new_text):
    """Finn run-tekst som matcher old_text og erstatt med new_text. Bevarer rPr."""
    if not shape.has_text_frame:
        return False
    for p in shape.text_frame.paragraphs:
        for r in p.runs:
            if r.text.strip() == old_text.strip():
                r.text = new_text
                return True
    return False


def replace_paragraph_text(shape, old_substr, new_text):
    """Finn paragraf som inneholder old_substr og erstatt hele tekstinnholdet.
    Beholder første run sin rPr."""
    if not shape.has_text_frame:
        return False
    for p in shape.text_frame.paragraphs:
        full = "".join(r.text for r in p.runs)
        if old_substr in full:
            # behold rPr fra første run
            runs = p.runs
            if not runs:
                continue
            first_rpr = runs[0]._r.find(qn('a:rPr'))
            rpr_xml = copy.deepcopy(first_rpr) if first_rpr is not None else None
            # fjern alle runs
            for r in runs:
                r._r.getparent().remove(r._r)
            # legg til ny run med samme rPr
            new_r = p._p.makeelement(qn('a:r'), {})
            if rpr_xml is not None:
                new_r.append(rpr_xml)
            t = p._p.makeelement(qn('a:t'), {})
            t.text = new_text
            new_r.append(t)
            p._p.append(new_r)
            return True
    return False


def delete_paragraph_containing(shape, substr):
    """Slett en hel paragraf som inneholder substr."""
    if not shape.has_text_frame:
        return False
    for p in list(shape.text_frame.paragraphs):
        full = "".join(r.text for r in p.runs)
        if substr in full:
            p._p.getparent().remove(p._p)
            return True
    return False


# ---- 1. Slide 5: tittel -------------------------------------------------
slide5 = prs.slides[4]
done = False
for sh in slide5.shapes:
    if sh.has_text_frame and "Fem utfordringer" in sh.text_frame.text:
        if replace_paragraph_text(sh, "Fem utfordringer med verdikjeden",
                                   "Fem kjerneegenskaper verdikjeden mangler"):
            done = True
            print("Slide 5: tittel oppdatert.")
            break
if not done:
    print("Slide 5: tittel IKKE oppdatert (sjekk manuelt).")

# ---- 2. Slide 11: agenda-linje ------------------------------------------
slide11 = prs.slides[10]
done = False
for sh in slide11.shapes:
    if sh.has_text_frame and "Tre kjerneegenskaper" in sh.text_frame.text:
        if replace_paragraph_text(sh, "Tre kjerneegenskaper verdikjeden mangler",
                                   "Fem kjerneegenskaper verdikjeden mangler"):
            done = True
            print("Slide 11: agenda-linje oppdatert.")
            break
if not done:
    print("Slide 11: agenda-linje IKKE oppdatert (sjekk manuelt).")

# ---- 3. Slide 13: D1-tall -----------------------------------------------
slide13 = prs.slides[12]
# Erstatt "2-3 år fra forskning til retningslinje" med case-spennvidde
# Fjern "6-12 måneder videre til oppdatert innbyggerinformasjon"
done_replace = False
done_delete = False
for sh in slide13.shapes:
    if sh.has_text_frame and "2-3 år fra forskning" in sh.text_frame.text:
        if replace_paragraph_text(sh, "2-3 år fra forskning til retningslinje",
                                   "Ca. 1 år til 7+ år for normerende delprosess (case-spennvidde)"):
            done_replace = True
            print("Slide 13: '2-3 år' erstattet med case-spennvidde.")
        if delete_paragraph_containing(sh, "6-12 måneder videre"):
            done_delete = True
            print("Slide 13: '6-12 måneder' linje fjernet.")
        break
if not done_replace:
    print("Slide 13: '2-3 år' IKKE erstattet (sjekk manuelt).")
if not done_delete:
    print("Slide 13: '6-12 måneder' IKKE fjernet (sjekk manuelt).")

prs.save(PPTX)
print(f"\nLagret: {PPTX}")
print(f"Totalt lysbilder: {len(prs.slides)}")
