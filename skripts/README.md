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
