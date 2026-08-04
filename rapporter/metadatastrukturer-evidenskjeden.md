# Metadatastrukturer i evidenskjeden — PICO, GRADE og veien til automatiserbar kvalitetsvurdering

**Status:** Utforskende. Kunnskapsnotat basert på målrettede
kildesøk 2026-08-04, utløst av spørsmål om PICOs rolle i
automatisering av kvalitetsvurdering (jf. dialog om
MAGIC-stiftelsen). Notatet er ikke kvalitetssikret på linje med
forankrede delrapporter.

**Forhold til øvrige rapporter:** Utdyper og nyanserer
[teknisk-infrastruktur-standarder.md](teknisk-infrastruktur-standarder.md)
(EBMonFHIR, CPG-on-FHIR, WHO SMART, terminologi) og
[kunnskapsinnhenting-ki-verktoy-evidenssyntese.md](kunnskapsinnhenting-ki-verktoy-evidenssyntese.md)
(LLM-ekstraksjon, GRADE-kunnskapshull). Innebærer en **presisering
av rotårsak R2** i delrapport 2 (se kap. 6).

**Merking:** [DOK] = dokumentert i oppgitt kilde.
[ANT] = utrederens vurdering/antakelse.

---<!-- KOMMENTAR:  -->

## 1. Hvorfor PICO er nøkkelen til automatisering

PICO (populasjon, intervensjon, sammenligning, utfall) er den
minste strukturerte enheten i både systematiske oversikter og
retningslinjer — og dermed koblingspunktet all automatisering
avhenger av. Tre operasjoner blir mulige først når innholdet er
PICO-strukturert: [ANT]

1. **Automatisk kobling av ny evidens til eksisterende
   anbefalinger** — maskineriet bak living guidelines og
   automatisert evidensovervåking (L·OVE-plattformen er
   organisert per PICO-spørsmål). [DOK]
2. **Gjenbruk på tvers av land** — GRADE-ADOLOPMENT gjøres
   anbefaling-for-anbefaling, dvs. PICO-for-PICO.
3. **Automatisering av kvalitetsvurdering** — GRADE-vurdering
   skjer per *utfall innenfor et PICO*; strukturert PICO er en
   nødvendig (men ikke tilstrekkelig) forutsetning.

Cochrane har bygget infrastruktur for dette: en
[PICO-ontologi](https://data.cochrane.org/ontologies) bundet mot
etablerte helsevokabularer, med annotering av oversikter gjennom
[Linked Data-prosjektet](https://www.cochranelibrary.com/about-cochrane-pico-linked-data)
og verktøyene PICO Annotator og PICOfinder. [DOK]

**Evidens for automatisert PICO-håndtering:** LLM-ekstraksjon av
P og I/C når over 80 % nøyaktighet i nyere studier; **utfall (O)
er systematisk svakest**. En systematisk oversikt finner 65–90 %
nøyaktighet for blandede ekstraksjonsoppgaver, der utelatelser
(ikke hallusinasjoner) dominerer feilbildet (60–74 % av feilene)
— feil som er usynlige for brukeren. Anbefalt bruk: assisterende,
i arbeidsflyter med menneskelig verifisering. [DOK]
(Kilder: [Performance of LLMs in data extraction](https://www.sciencedirect.com/science/article/abs/pii/S1532046426001103),
[rapid feasibility study](https://arxiv.org/abs/2405.14445),
[benchmark Research Synthesis Methods](https://www.cambridge.org/core/journals/research-synthesis-methods/article/what-level-of-automation-is-good-enough-a-benchmark-of-large-language-models-for-metaanalysis-data-extraction/2EA4DAFAAC11E76216DC0A512CA29D59),
[ROBoto2](https://arxiv.org/pdf/2511.03048))

---

## 2. PICO i dagens norske retningslinjer — status

Et sentralt funn som **nyanserer utfordringsbildet**: PICO er
allerede i bruk i norske retningslinjer, på tre nivåer.

### 2.1 Metodisk

Helsedirektoratets veileder for utvikling av kunnskapsbaserte
retningslinjer ([IS-1870, 2012](https://www.helsedirektoratet.no/veiledere/utvikling-av-kunnskapsbaserte-retningslinjer))
foreskriver PICO for å strukturere spørsmål før litteratursøk. [DOK]

### 2.2 I publiseringsmodellen

Helsedirektoratets innholdsmodell (dokumentert i
[case-beskrivelse fra CMS-leverandøren Enonic](https://www.enonic.com/no/ressurser/guider/strukturert-innhold-helsedirektoratet))
har hierarkiet retningslinje → kapittel → **anbefaling → PICO →
bevisprofil**, med 25 kjernemetadatafelt inkludert kliniske koder
(SNOMED CT, ICD-10, ICPC-2). Det
[åpne API-et](https://www.helsedirektoratet.no/om-oss/apne-data-api/hvordan-finne-frem-i-innholdet)
eksponerer `pico` som egen innholdstype
(`https://api.helsedirektoratet.no/innhold/innhold?infoTyper=pico`)
— kun for nasjonale faglige retningslinjer; antibiotika-
retningslinjene har egne datamodeller. [DOK]

*Verifikasjonsstatus:* API-et krever gratis abonnementsnøkkel
(forsøk uten nøkkel ga HTTP 401); hvilke felter PICO-objektene
faktisk inneholder (strukturerte data vs. HTML-tekst) er derfor
**ikke empirisk verifisert**. [DOK om 401; se kunnskapsgap]

### 2.3 Konkrete eksempler (diabetes-retningslinjen)

**[Risikovurdering og påvisning av diabetes](https://www.helsedirektoratet.no/retningslinjer/diabetes/diagnostikk-av-diabetes-risikovurdering-og-oppfolging-av-personer-med-hoy-risiko-for-a-utvikle-diabetes/risikovurdering-og-pavisning-av-diabetes)**
(svak anbefaling): PICO vist som P = generell befolkning,
I = screening for diabetes, C = ingen screening, O = dødelighet
og kardiovaskulær dødelighet — med effektestimater fra Ely-
kohorten (HR 0,79) og ADDITION-Cambridge (HR 1,02). [DOK]

**[Retinopati og netthinneundersøkelse](https://www.helsedirektoratet.no/retningslinjer/diabetes/retinopati-og-regelmessig-netthinneundersokelse-ved-diabetes)**:
tre anbefalinger med hver sin PICO og eksplisitt GRADE-
resonnering (f.eks. «nedgradert på grunn av usikker
appliserbarhet til norske forhold»). **Evidensprofilene ligger
som PDF-lenker.** [DOK]

### 2.4 Hvor struktureringen stopper

PICO-elementer og GRADE-vurderinger fremstilles som tekst for
menneskelig lesing; evidensprofiler som PDF; utfall er ikke
terminologikodet; effektestimater er ikke datafelter. En maskin
kan derfor ikke besvare «hvilke anbefalinger berøres av denne nye
studien?» eller regenerere en evidensprofil. [ANT]

### 2.5 Hvorfor ikke dypere? Offentlig begrunnelse

Eneste funne eksplisitte forklaring er pragmatisk (Enonic-casen):
*«ikke all data har ennå hatt et dyptgående behov for å
struktureres med for eksempel SNOMED CT. Dette er imidlertid et
pågående arbeid.»* [DOK] Ingen offentlig utredning eller
beslutningsdokumentasjon som begrunner at kunnskapsgrunnlaget
ikke publiseres som strukturerte data, ble funnet — fraværet
tyder på at dette aldri har vært en eksplisitt beslutning, men et
resultat av at publiseringen ble designet for menneskelig lesing
før automatisert gjenbruk ble aktuelt formål. [ANT]

---

## 3. De øvrige metadatastrukturene i evidenskjeden

Ordnet etter hvor de sitter i kjeden:

**Evidensnivået:** studieregistre (ClinicalTrials.gov/WHO ICTRP)
og identifikatorer (DOI, ORCID, Crossref/OpenAlex) muliggjør
automatisk overvåking; rapporteringsstandarder (CONSORT, PRISMA)
og MeSH-indeksering bedrer maskinell ekstraksjon; **Core Outcome
Sets** (COMET-initiativet) angriper det svakeste PICO-elementet
(O) ved å standardisere utfall per tilstand.

**Kvalitetsvurderingsnivået:** **Risk of Bias 2** er et
strukturert skjema (domener, signalspørsmål) — grunnlaget for at
RobotReviewer-familien kunne automatisere deler av vurderingen;
**GRADE-evidensprofiler** har de facto feltstruktur via GRADEpro
(per utfall: studier, design, nedgraderingsgrunner,
effektestimat, KI, sikkerhetsnivå).

**Anbefalings-/beslutningsnivået:** **EBMonFHIR** (HL7:
`Evidence`, `EvidenceVariable` ≈ PICO som datamodell, `Citation`,
`ArtifactAssessment` ≈ kvalitetsvurdering som data);
**CPG-on-FHIR + CQL** (anbefaling som utførbar logikk); WHO SMART
Guidelines' lagmodell L1–L5 som modenhetsskala (norske
retningslinjer ligger rundt L1–L2 [ANT]); **AGREE II/GIN-
standarder** som metadata om retningslinjens metodiske kvalitet.

**Terminologinivået:** SNOMED CT, ICD, ICPC-2, ATC, LOINC — limet
som gjør PICO-elementer sammenlignbare på tvers. Norsk fortrinn:
Felles språk og norske FHIR-basisprofiler. [DOK/ANT]

---

## 4. Bruksgrad i dagens verdikjede — modenhetskart

Sentralt skille: *metodisk bruk* (mennesker følger strukturen)
vs. *databruk* (strukturen publiseres maskinlesbart).

| Struktur | Metodisk bruk | Som maskinlesbare data | Norsk kjede |
| --- | --- | --- | --- |
| Studieregistre, DOI/ORCID | Høy (obligatorisk) | Høy | Høy |
| CONSORT/PRISMA, MeSH | Høy | Middels | Høy (via databasene) |
| Core Outcome Sets | **Lav** utenfor enkeltfelt | Lav | Ukjent/lav [ANT] |
| Risk of Bias 2 | Høy i oversikter | **Lav** (prosa/PDF) | Høy metodisk [ANT] |
| GRADE/evidensprofiler | Høy (100+ org., inkl. Hdir/FHI) | **Lav** (GRADEpro internt, PDF ut) | Høy metodisk, PDF ut [DOK] |
| PICO | Høy i prosess | Delvis (Cochrane; Hdir-innholdstype) | Delvis [DOK] |
| EBMonFHIR | — | **Pilot/tidlig** | Ingen kjent bruk |
| CPG-on-FHIR/CQL/SMART | — | Pilot (USA, LMIC) | Ingen dokumentert bruk [DOK] |
| AGREE II/GIN | Høy i fagfellevurdering | Nei | Metodisk [ANT] |
| Terminologier | Høy i tjenesten | Høy i EPJ/registre, **ikke bundet til kunnskapsprodukter** | Samme mønster [DOK/ANT] |

Nøkkelfunn bak tabellen:

- **Core Outcome Sets — dokumentert lav bruk:** en gjennomgang i
  fem store medisinske tidsskrifter fant at **ingen** av 95
  studier rapporterte fullt COS (2 % delvis); bruksgrad spenner
  fra 0 % (urinsyregikt) til >80 % (revmatoid artritt, der
  OMERACT har arbeidet i tiår). COMET-databasen dekker 481
  tilstander, men eksistens ≠ bruk. [DOK]
  ([Use of COS was low, J Clin Epidemiol](https://www.sciencedirect.com/science/article/pii/S0895435621003413),
  [COMET COS Uptake](https://www.comet-initiative.org/COSUptake),
  [lungekreft-COS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11532957/),
  [5-års oppfølging](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12366604/))
- **EBMonFHIR — aktivt, men pilot:**
  [FEvIR-plattformen](https://fevir.net/resources/Project/46952)
  med ~30 verktøy, internasjonalt frivillignettverk (~100
  personer), implementasjonsguide i ballot-stadium. Levende
  standardiseringsmiljø, ikke produksjonsinfrastruktur. [DOK]
  ([EBMonFHIR-based tools, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9748541/),
  [HL7-blogg](https://blog.hl7.org/working-fevirishing-with-fhir-resources))
- **Kvalitetsvurderingsleddet — universell metodikk, null
  datapublisering:** GRADE brukes av 100+ organisasjoner (WHO,
  NICE, Cochrane, Helsedirektoratet, FHI), RoB 2 er standard i
  nye oversikter — men vurderingene publiseres som prosa/PDF
  over hele feltet. De norske diabetes-eksemplene er
  normalpraksis internasjonalt, ikke et norsk avvik. [DOK/ANT]

---

## 5. Samlet mønster

Bruken er **høy i ytterkantene og lav i midten**: inngangen
(registre, identifikatorer, indeksering) og tjenestesiden
(terminologier i EPJ/registre) er godt strukturert; midtleddet —
kvalitetsvurderingen som automatiseringen trenger mest — har
strukturert *metodikk* men ustrukturert *publisering*. Ingen
nasjonal kjede publiserer i dag evidensprofiler som strukturerte
data i produksjon, så vidt denne kartleggingen viser. [ANT]

**Strategisk implikasjon:** Norge er ikke bakpå — ingen er foran.
Det finnes ingen ferdig modell å importere (som for
feedback-sløyfene i D2), men et land med Norges utgangspunkt
(etablert GRADE-praksis, PICO-innholdstype i publiseringsmodellen,
Felles språk, åpent API) kunne være blant de første som lukker
gapet — trolig til lavere kostnad enn utfordringsbildet antyder,
siden innholdet allerede produseres strukturert internt
(GRADEpro-arbeidsfiler, PICO-elementer). Tre strukturer er mest
verdt å følge: **EBMonFHIR** (evidens og kvalitetsvurdering som
data), **GRADE-evidensprofilens feltstruktur** (lavthengende:
innholdet finnes, bare i feil format) og **Core Outcome Sets**
(utfall er både svakeste ekstraksjonsledd og kjernen i GRADE).
[ANT]

**MAGIC-koblingen:** MAGICapps verdi ligger mindre i applikasjonen
og mer i at innholdet blir PICO-strukturert data. Ved et eventuelt
norsk veivalg er det *datastrukturen*, ikke verktøyet, som bør
være bindingen (jf. leverandørvurderingen i
[kunnskapsinnhenting-organisasjonsmodeller.md](kunnskapsinnhenting-organisasjonsmodeller.md)
pkt. 1.1.1). [ANT]

---

## 6. Implikasjoner for utredningen

Alle tre implikasjoner er innarbeidet i de berørte dokumentene
2026-08-04:

1. **R2 presisert i delrapport 2** — *gjennomført*, se
   [utfordringer-og-flaskehalser.md](utfordringer-og-flaskehalser.md)
   kap. 9.2 (datert presisering under R2) og endringsloggen der.
   Karakteristikken «fritekst, PDF, manglende metadata» var for
   kategorisk for Helsedirektoratets retningslinjer:
   anbefalingsnivå-struktur, PICO-elementer, SNOMED CT-metadata
   og åpent API finnes allerede. Det presise gapet er at
   **evidenskjeden bak anbefalingen (PICO → utfall → GRADE) ikke
   er strukturerte, terminologibundne data**, og at strukturen
   ikke er konsistent på tvers av produkttyper og verdikjedens
   øvrige ledd (FHI-oversikter, Helsebiblioteket,
   innbyggerinnhold). [ANT]
2. **Retning B2 har bedre startpunkt enn først lagt til grunn** —
   *gjennomført*, se tillegg datert 2026-08-04 under B2 i
   [losningsretninger-bred-kartlegging.md](losningsretninger-bred-kartlegging.md).
   Et konkret «første grep» kan defineres: publisere
   GRADE-evidensprofilene som strukturerte data og
   terminologibinde PICO-elementene. Verdifullt uansett
   alternativvalg, fordi det muliggjør alt det andre
   (A1, A2, B1, B4) senere. [ANT]
3. **GRADE+LLM-kunnskapshullet presisert i KI-notatet** —
   *gjennomført*, se
   [kunnskapsinnhenting-ki-verktoy-evidenssyntese.md](kunnskapsinnhenting-ki-verktoy-evidenssyntese.md)
   §5.2: hullet skyldes trolig delvis at GRADE-data ikke finnes
   offentlig som trenings-/regnegrunnlag — nok en konsekvens av
   publiseringsgapet. [ANT]

*Ikke endret, bevisst:* Delrapport 7 kap. 4.2 («designet for en
pre-digital tid») står — formuleringen gjelder kjeden som helhet
og delrapport 7 revideres samlet senere. Forankringspresentasjonen
(`utfordringsbildet-forankring.pptx`) bruker samme
R2-formulering; presiseringen bør tas inn i talepunktene ved
neste bruk. [ANT]

## 7. Kunnskapsgap

1. **Innholdet i API-ets PICO-objekter er uverifisert** (krever
   abonnementsnøkkel) — bør verifiseres empirisk med noen få
   API-kall; avgjør [DOK]-status for flere [ANT] i kap. 2.
2. **FHIs praksis**: i hvilken grad FHIs oversikter produseres i
   GRADEpro og hvilke strukturerte data som finnes internt, er
   ikke undersøkt — internt spørsmål til FHI.
3. **Helsebibliotekets metadatamodell** er ikke undersøkt —
   relevant gitt Meld. St. 11 kap. 8.3 (nasjonal infrastruktur
   for kunnskapsformidling).
4. **Interne vurderinger i Helsedirektoratet** av dypere
   strukturering (retningslinjesekretariatet/redaksjonen) er
   ikke innhentet — den egentlige kilden til «hvorfor ikke
   dypere».
5. **COS-dekning for norske prioriterte tilstander** er ikke
   kartlagt.

---

Sist oppdatert: 2026-08-04
