# Skripts og engangs-operasjoner

Denne mappen inneholder skript brukt for engangs-
operasjoner mot prosjektets artefakter (typisk pptx-
manipulering der python-pptx er enklere enn manuell
redigering), samt backuper tatt før slike operasjoner.

Skriptene er dokumentasjon av hva som faktisk ble gjort,
slik at en lignende endring kan reproduseres senere.
Unntaket er `generer_html.py`, som er et gjenbrukbart
byggeskript som skal kjøres på nytt hver gang
delrapportene endres.

## Filer

### generer_html.py

Gjenbrukbart byggeskript som regenererer hele
HTML-versjonen av utredningen i `rapporter/html/`.
Konverterer delrapportene fra markdown med pandoc,
setter innholdet inn i `rapporter/html/template.html`,
bygger identisk navigasjonsbar på alle sider, skriver
om interne `.md`-lenker til `.html` og pakker tabeller
i overflow-wrapper. Spesialsidene (forside,
ledersammendrag, visualiseringer) regenereres ikke fra
markdown, men får navigasjonsbaren oppdatert på plass.
Nye delrapporter legges til i `SIDER`-listen i skriptet.

Kjøres fra prosjektroten:
`python3 skripts/generer_html.py` (krever pandoc).

### lag_igoe_matrise_pptx.py

Genererer `visualiseringer/igoe-aktormatrise.pptx`
(6 lysbilder i Helsedirektoratets mal `HdirMal.pptx`)
med aktørene som rader og verdikjedens seks prosesser
(P1–P6) som kolonner, basert på delrapport 8
(`aktoeranalyse.md`) kap. 5.2 og 5.3.

Kjørt: 2026-06-10

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
