# Skripts og engangs-operasjoner

Denne mappen inneholder skript brukt for engangs-
operasjoner mot prosjektets artefakter (typisk pptx-
manipulering der python-pptx er enklere enn manuell
redigering), samt backuper tatt før slike operasjoner.

Skriptene er dokumentasjon av hva som faktisk ble gjort,
slik at en lignende endring kan reproduseres senere.
De er ikke en del av en løpende byggepipeline.

## Filer

### update_slide9.py

Engangs-script som oppdaterte slide 9 i
`Presentasjoner/utfordringsbildet-forankring.pptx`
fra tre kjerneegenskaper (3 spalter) til fem
(4 spalter i topprad + tillit/legitimitet som
tverrgående bunnblokk). Klonet eksisterende
placeholder-XML for å bevare malstil.

Kjørt: 2026-05-22
Resulterende endring lever utenfor git, i OneDrive-
mappen `Presentasjoner/`.

### utfordringsbildet-forankring.BACKUP3.pptx

Backup av `utfordringsbildet-forankring.pptx` tatt
2026-05-22 før `update_slide9.py` ble kjørt.
Beholdt som rollback-mulighet siden pptx-filen
ikke ligger i git.

### update_pptx_konsistens.py

Engangs-script som ryddet tre konsistens-feil i
`Presentasjoner/utfordringsbildet-forankring.pptx`
i tråd med endringene som ble gjort i delrapport 1, 4
og 7 (commit ce7169b):

1. Slide 5: "Fem utfordringer med verdikjeden" endret
   til "Fem kjerneegenskaper verdikjeden mangler"
   (speilet av slide 9-tittel).
2. Slide 11 (agenda): "Tre kjerneegenskaper" endret til
   "Fem kjerneegenskaper" (samme endring som ble gjort
   i rapportene 22. mai).
3. Slide 13 (D1+D2): udokumenterte tall "2-3 år fra
   forskning til retningslinje" og "6-12 måneder videre
   til oppdatert innbyggerinformasjon" fjernet, første
   erstattet med case-spennvidde fra
   casestudier-forsinkelser.md.

Kjørt: 2026-05-27

### utfordringsbildet-forankring.BACKUP4.pptx

Backup av `utfordringsbildet-forankring.pptx` tatt
2026-05-27 før `update_pptx_konsistens.py` ble kjørt.
Beholdt som rollback-mulighet.
