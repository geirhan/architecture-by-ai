# Kunnskapsgrunnlag: Teknisk infrastruktur, standarder og datamodeller for en modernisert kunnskapskjede

## 0. Om notatet

**Formål:** Bred kunnskapsinnhenting til støtte for utredningens vurdering av
mulige tekniske byggeklosser mot rotårsak **R4** (fragmentert IT-landskap og
ulike kodeverk) og **R2** (kjeden er designet for pre-digital tid — fritekst,
PDF, manglende metadata). Notatet er et kunnskapsgrunnlag, ikke en
anbefaling — det skal danne underlag for de tekniske/arkitektoniske delene
av delrapport 4 (ny verdikjede) og delrapport 5 (arkitektur og komponenter).

**Metode:** Systematisk websøk mot primærkilder (HL7.org, WHO.int,
EUR-Lex, regjeringen.no, helsedirektoratet.no, ehelse.no-arkivet, FHI,
health.ec.europa.eu/MDCG) supplert med sekundærkilder der primærkilde
manglet detaljer. Gjennomført som tre parallelle kunnskapsinnhentinger
2026-08-03.

**Merking:** [DOK] = dokumentert i oppgitt kilde. [ANT] = tolkning/antakelse
gjort av utreder, ikke direkte bekreftet i kilde. Der graden av sikkerhet
varierer internt i et avsnitt, er dette presisert løpende.

**Viktig forbehold:** Dette er et bredt kartleggingsnotat basert på ett
søkepass. Det er **ikke** kvalitetssikret på linje med de forankrede
delrapportene (jf. statussystemet i `rapporter/index.md`) og bør behandles
som "Under forankring"/utforskende kunnskapsgrunnlag inntil videre
verifisert.

---

## 1. Maskinlesbare retningslinjer

### 1.1 HL7 FHIR Clinical Practice Guidelines (CPG-on-FHIR)

- **Hva:** FHIR Implementation Guide som definerer hvordan en narrativ
  klinisk retningslinje kan representeres som beregnbart (computable)
  innhold — «Shareable, Publishable, Computable, and Executable» innhold,
  for nedstrøms bruk i beslutningsstøtte, kvalitetsmål og
  case-rapportering [DOK, hl7.org/fhir/uv/cpg].
- **Modenhet:** Standard for Trial Use (STU). v1.0.0 (STU1) publisert
  februar 2021 (FHIR R4); gjeldende v2.0.0 (STU2). Deler av
  innholdsstyringen er generalisert inn i et eget rammeverk (Canonical
  Resource Management Infrastructure, CRMI), som nå er anbefalt
  tilnærming [DOK]. Standarden er under aktiv utvikling, ikke ferdig
  konsolidert [ANT: ikke bredt/stabilt utbredt på tvers av mange
  jurisdiksjoner ennå].
- **Bruk i dag:** Best dokumentert i USA. CDCs retningslinje for
  opioidforskrivning (2022) er implementert som FHIR IG basert på
  CPG-metodikk, utviklet med Clinical Quality Framework (CQF), CDC og
  ONC, medsponset av CMS [DOK]. Pilotforsøk (TOWER-studien) har testet
  implementering i amerikansk primærhelsetjeneste (HIV-omsorg) [DOK].
- **Relevans for Norge:** Ingen treff på norsk bruk. Helsedirektoratet/
  tidligere Direktoratet for e-helse har publisert anbefaling om SMART on
  FHIR (HITR 1225:2019, merknad 25.09.2024) [DOK] — beslektet
  infrastruktur, men ikke CPG-on-FHIR for retningslinjeinnhold. [ANT]
  Norge har ikke tatt CPG-on-FHIR i bruk, men FHIR-kompetanse/
  SMART on FHIR-anbefalingen er et mulig fundament.
- **Kilder:** hl7.org/fhir/uv/cpg/ImplementationGuide-hl7.fhir.uv.cpg.html;
  hl7.org/fhir/uv/cpg/methodology.html; build.fhir.org/ig/HL7/cdc-opioid-cpg/;
  build.fhir.org/ig/cqframework/opioid-cds-r4/;
  helsedirektoratet.no – anbefaling om bruk av SMART on FHIR (merknad
  25.09.2024).

### 1.2 CQL (Clinical Quality Language)

- **Hva:** HL7-standardisert, domenespesifikt språk for klinisk logikk,
  lesbart for kliniske fageksperter. Brukes til klinisk beslutningsstøtte
  (CDS) og kvalitetsmåling (CQM). Kompileres til maskinlesbar Expression
  Logical Model (ELM), datamodell-uavhengig [DOK, cql.hl7.org].
- **Modenhet:** Gjeldende v1.5.3 (ikke ballot), v2.0.0 under balloting.
  Moden, veletablert standard særlig i amerikansk kvalitetsmåling
  (eCQM/CMS) [DOK, NCQA].
- **Bruk i dag:** Utstrakt i amerikansk eCQM/CMS-rapportering. CQL er den
  logiske «motoren» bak CPG-on-FHIR-artefakter som CDC-opioidretningslinjen
  [DOK/ANT — kobling fremgår indirekte via PlanDefinition/Library-ressurser].
- **Relevans for Norge:** Ingen norske treff. [ANT] Relevant som teknisk
  uttrykksspråk dersom Norge velger FHIR-basert infrastruktur for
  maskinlesbare retningslinjer/kvalitetsindikatorer, men ikke dokumentert
  norsk bruk i dag.
- **Kilder:** cql.hl7.org; cql.hl7.org/STU2/01-introduction.html;
  github.com/cqframework/clinical_quality_language;
  ncqa.org/resources/clinical-quality-language-and-cql-engines-the-basics/.

### 1.3 WHO SMART Guidelines (L1–L4/L5)

- **Hva:** WHO-rammeverk (Standards-based, Machine-readable, Adaptive,
  Requirements-based, Testable) som lagdeler kliniske/folkehelse­
  retningslinjer for digitalisering:
  - **L1 Narrativ** — tradisjonell tekst, men med prosess tilpasset
    digital transformasjon [DOK]
  - **L2 Operasjonell (Digital Adaptation Kit, DAK)** — strukturert,
    programvareuavhengig dokumentasjon [DOK]
  - **L3 Maskinlesbar** — FHIR-basert operasjonalisering av L2 [DOK]
  - **L4 Kjørbar (Executable)** — referanseapplikasjoner/-tjenester [DOK]
  - **L5 Dynamisk** — presisjonshelse-modeller, nevnt i enkelte kilder,
    mer eksperimentelt [DOK/ANT — minst modent laget]
- **Modenhet:** DAK-er (L2) finnes for mødrehelse, HIV, familieplanlegging,
  tuberkulose, barnehelse i humanitære kriser, immunisering, medfødte
  tilstander, egenmåling av blodtrykk i svangerskap, postnatal omsorg
  [DOK, who.int]. L3/L4 under aktiv utvikling (egne WHO SMART-IG-er for
  immunisering og TB på build.fhir.org) [DOK]. Samlet: L1–L2 relativt
  modent og i bruk; L3 i pilotfase; L4–L5 tidlig/eksperimentelt [ANT].
- **Bruk i dag:** Primært lav- og mellominntektsland via WHOs
  «pathfinder»-program — Ghana og Etiopia eksplisitt nevnt som pilotland,
  med følgeforskning (JMIR 2025) [DOK]. Utviklet med bl.a. UNICEF [DOK].
- **Relevans for Norge:** Ingen dokumentasjon på norsk/nordisk bruk eller
  vurdering. [ANT] Rammeverket er designet for land med svakere digital
  grunninfrastruktur og er trolig mindre direkte overførbart til Norge
  som allerede har etablert EPJ, kjernejournal, reseptformidler. Selve
  **metodikken** (narrativ → strukturert operasjonelt innhold, L1→L2) kan
  likevel være overførbar uavhengig av landkontekst.
- **Kilder:** who.int/teams/digital-health-and-innovation/smart-guidelines;
  thelancet.com/journals/landig/article/PIIS2589-7500(21)00038-8/fulltext;
  medinform.jmir.org/2025/1/e58858; smart.who.int/dak-tb/,
  smart.who.int/dak-immz/; cdn.who.int (WHO DAK-dokument).

### 1.4 Arden Syntax og CDS Hooks

- **Hva:** Arden Syntax — eldre HL7-standard (1990-tallet) for kliniske
  beslutningsregler som frittstående «Medical Logic Modules». CDS
  Hooks — nyere HL7-spesifikasjon der en EPJ («CDS Client») kaller en
  ekstern beslutningsstøttetjeneste («CDS Service») på definerte hooks
  (f.eks. ved forskrivning) [DOK, cds-hooks.hl7.org].
- **Modenhet:** CDS Hooks har formell «maturity model»
  (definisjon→testing→implementering→produksjon→balloting), gjeldende
  v2.0/2.0.1 [DOK]. Arden Syntax er eldre og mer etablert, men
  forskningslitteratur (Wien, MIE 2025) tyder på at den nå ofte
  integreres *sammen med* CDS Hooks og FHIR fremfor å stå alene [DOK].
  Adopsjon av CDS Hooks beskrives som «tentativ» selv sammenlignet med
  SMART on FHIR — barrierer: leverandørarbeidsbyrde, ansvar/liability ved
  feilaktige forslag, krav til ytelse/tilgjengelighet [DOK, sekundærkilde].
- **Bruk i dag:** Universitetssykehuset i Wien bruker Arden
  Syntax/ArdenSuite integrert med CDS Hooks, FHIR og openEHR til
  automatisert retningslinjebehandling og pandemivarsling [DOK]. Bredere
  amerikansk bruk under vekst i takt med FHIR-adopsjon, uten konkrete
  navngitte produksjonstall funnet [ANT].
- **Relevans for Norge:** Ingen norske treff. [ANT] Arkitektonisk
  relevant som grensesnitt for å koble maskinlesbare retningslinjer til
  norske EPJ ved forskrivning/journalføring, men krever at norske
  EPJ-leverandører implementerer CDS Hooks-klient — ikke dokumentert i
  dag.
- **Kilder:** cds-hooks.hl7.org (v2.0.1, v1.0); MIE 2025-artikkel
  (klauspeteradlassnig.com); pubmed.ncbi.nlm.nih.gov/30306929/;
  pubmed.ncbi.nlm.nih.gov/32578563/.

### 1.5 EBMonFHIR

- **Hva:** HL7-prosjekt («Evidence-Based Medicine on FHIR», godkjent
  16.05.2018) som utvikler FHIR-ressurser for å representere
  forskningsevidens og systematiske oversikter maskinlesbart. Sentrale
  ressurser: `ArtifactAssessment`, `Citation`, `Evidence`,
  `EvidenceReport`, `EvidenceVariable` [DOK].
- **Modenhet:** Sponses av HL7s Clinical Decision Support Work Group,
  medsponset av Clinical Quality Information og Biomedical Research and
  Regulation Work Groups. Bredt internasjonalt frivillig nettverk
  (~100 personer). Fremstår som **tidlig/pilot-stadium**, ingen
  dokumentasjon på storskala produksjonsbruk funnet [ANT].
- **Bruk i dag:** Internasjonalt frivillig HL7-nettverk. Ingen navngitte
  produksjonsbrukere utover HL7-fellesskapet selv funnet [ANT — mulig
  reelt kunnskapsgap; naturlig å undersøke kobling til Cochrane/GRADE].
- **Relevans for Norge:** Ingen norske treff. [ANT] Konseptuelt relevant
  for R2 (fritekst/PDF → strukturert evidens) — EBMonFHIR adresserer
  representasjon av *evidensgrunnlaget* bak retningslinjer, altså et ledd
  tidligere i kjeden enn CPG-on-FHIR (som representerer selve
  anbefalingen).
- **Kilder:** confluence.hl7.org/display/CDS/EBMonFHIR;
  github.com/HL7/ebm; PMC11234056 (Making Science Computable);
  PMC9748541 (EBMonFHIR-baserte verktøy).

---

## 2. Kunnskapsrepresentasjon og terminologi

### 2.1 SNOMED CT

- **Hva:** Internasjonal klinisk referanseterminologi (diagnoser, funn,
  prosedyrer mv.).
- **Status i Norge:** Fra pilot til etablert forvaltning. Avdeling
  terminologi i Helsedirektoratet har ansvar for nasjonal forvaltning som
  «National Release Center» [DOK]. Historikk: Direktoratet for e-helse
  anbefalte SNOMED CT som felles terminologi i 2018; Nasjonalt
  e-helsestyre sluttet seg til dette mars 2019; «Visjon for Felles
  språk v1» utgitt 2019 [DOK].
- **Bruk i dag:** Helsenorge, Helseplattformen, pleieplaner i alle
  helseregioner, antibiotikaveiledning, kreftregisterets
  koloskopijournaler [DOK]. Ny nasjonal veileder under planlegging [DOK].
- **Relevans:** Strategien er å **lenke** SNOMED CT til eksisterende
  kodeverk (ICD-10, ICPC-2) heller enn å erstatte dem, for å muliggjøre
  automatisert rapportering til kvalitetsregistre [DOK]. Direkte relevant
  for R4 — dette er selve mekanismen for å redusere kodeverksfragmentering.
- **Kilder:** helsedirektoratet.no/digitalisering-og-e-helse/
  helsefaglig-terminologi/snomed-ct-i-norge (hentet 05.02.2025);
  ehelse.no/kodeverk-og-terminologi/SNOMED-CT/.

### 2.2 ICD-10/ICD-11

- ICD-10 er gjeldende i Norge. Overgang til ICD-11 er et etablert
  prosjekt (opprettet 2024) med foreløpig mål om innføring **2028–2029**
  [DOK]. Norge samarbeider med andre nordiske land i NordClass ICD-11
  Task Force [DOK]. [ANT] Dette er et flerårig sideløp — ikke en
  kortsiktig løsningsbrikke for R4, men bør tas høyde for i
  tidslinjevurderinger.
- **Kilde:** helsedirektoratet.no/digitalisering-og-e-helse/
  helsefaglige-kodeverk/icd/om-overgangen-til-icd-11-i-norge.

### 2.3 ICPC-2

- Aktivt forvaltet og oppdatert årlig (publisert 1. januar,
  endringsforslag frist 1. mai) [DOK]. Brukes i primærhelsetjenesten for
  kontaktårsak/diagnose. Moden, veletablert i norsk allmennpraksis.
- **Kilde:** helsedirektoratet.no/digitalisering-og-e-helse/
  helsefaglige-kodeverk/icpc.

### 2.4 ATC/DDD

- ATC/DDD-metodikken forvaltes internasjonalt av WHO Collaborating Centre
  for Drug Statistics Methodology, lokalisert ved **Folkehelseinstituttet
  i Oslo** (etablert 1982, statlig finansiert) [DOK]. I Norge brukes
  ATC-koder i Reseptregisteret, grossistbasert legemiddelstatistikk og
  Legemiddelverkets FEST [DOK]. Norge er vertskap for selve WHO-senteret —
  en internasjonal styrke og et modent, veletablert kodeverk.
- **Kilder:** atcddd.fhi.no/atc_ddd_methodology/who_collaborating_centre/;
  fhi.no/he/legemiddelbruk/who-senteret/;
  helsedirektoratet.no/standarder/atc-anatomisk-terapeutisk-
  kjemisk-legemiddelregister.

### 2.5 Ontologier og kunnskapsgrafer for medisinsk evidens

- **Hva:** UMLS (Unified Medical Language System, NLM/USA) integrerer
  mange medisinske vokabularer under felles konseptidentifikatorer.
  BioPortal (NCBO) tilbyr mapping mellom ontologier. Begge brukes som
  byggeklosser i kunnskapsgrafer for biomedisin, inkl. kobling til
  SNOMED [DOK].
- **Modenhet:** UMLS/BioPortal er modne, veletablerte
  forskningsinfrastrukturer (NLM). Anvendelse i **produksjonssatte
  kliniske systemer** i offentlig sektor er mindre dokumentert — mesteparten
  av litteraturen er forsknings-/metodeartikler (2023–2026, inkl. bruk med
  språkmodeller for å redusere hallusinasjon). [ANT] Kunnskapsgrafer for
  medisinsk evidens generelt er på forsknings-/pilotstadium for
  produksjonsbruk, mens UMLS/BioPortal som terminologi-mapping-verktøy er
  modne.
- **Bruk i dag:** Primært forskningsmiljøer og NLM selv. Ingen offentlige
  europeiske/norske produksjonseksempler funnet.
- **Relevans for Norge:** Ingen norske treff. [ANT] Konseptuelt relevant
  som mulig fremtidig arkitekturkomponent for å koble maskinlesbare
  retningslinjer (CPG-on-FHIR/SMART Guidelines), evidens (EBMonFHIR) og
  terminologi (SNOMED CT, ICPC-2, ATC) i en sammenhengende kunnskapsgraf —
  men uten dokumentert norsk/nordisk implementering.
- **Kilder:** link.springer.com/chapter/10.1007/978-3-032-05176-9_3;
  PMC11655564 (Petagraph); lhncbc.nlm.nih.gov (LHC-publications).

---

## 3. Kobling til EHDS (Forordning 2025/327)

**Hovedkonklusjon (etter direkte tekstsøk i forordningen, CELEX
32025R0327):** Koblingen mellom EHDS og kliniske retningslinjer/
beslutningsstøtte er **svak/indirekte, ikke direkte** [DOK]. Forordningen
inneholder ingen forekomster av «clinical decision support», og bruker
«guidelines» kun om datakvalitet, håndheving og forskningsmetodikk — ikke
pasientnære faglige retningslinjer [DOK]. Dette er konsistent med og
utdyper funnet i det tidligere kildeforankringsnotatet
`regulatorisk-etterslep.md`, som konkluderte at EHDS ikke treffer
kjerneleddene i verdikjeden (oversikter, retningslinjer, innbyggerinfo)
direkte.

- **European Electronic Health Record Exchange Format (EEHRxF)**
  (art. 14, 23, 105): Format for **pasientdata** (patient summary,
  e-resept, bildediagnostikk mv.) — ikke kunnskapsinnhold [DOK].
- **MyHealth@EU** (primærbruk) og **HealthData@EU** (sekundærbruk): Begge
  er datadelingsinfrastruktur, uten eksplisitt kobling til
  kunnskapsformidling/retningslinjer i forordningsteksten [DOK].
- **Vurdering:** Kildegrunnlaget støtter ikke en påstand om at EHDS har
  direkte relevans for norske kliniske retningslinjer eller
  kunnskapsoppsummeringer. Koblingen som finnes, er indirekte — via
  datakvalitetskrav og infrastruktur for pasientdata som i prinsippet kan
  gjenbrukes teknisk, ikke via forordningens eget saklige virkeområde.
  [ANT] EHDS bør derfor primært vurderes som en **tilstøtende**
  regulatorisk ramme for denne utredningens formål, ikke en direkte
  hjemmel eller driver for kunnskapskjeden.
- **Kilde:** EUR-Lex, Regulation (EU) 2025/327 (CELEX 32025R0327).

---

## 4. Nasjonale byggeklosser i Norge

### 4.1 Helsebiblioteket som mulig nasjonal infrastruktur

**Sentralt, verifisert funn** fra Meld. St. 11 (2025–2026)
Helsepersonellplan 2040, kapittel 8.3 (s. 92–93):

> «En videreutvikling av Helsebiblioteket til en nasjonal infrastruktur
> for kunnskapsformidling skal derfor utredes.» [DOK]

samt i tiltaksdelen:

> «legge til rette for en trinnvis videreutvikling av Helsebiblioteket …
> til en offentlig infrastruktur for kunnskapsformidling» [DOK]

Det er en nyanseforskjell mellom «nasjonal» (statusdelen) og «offentlig»
(tiltaksdelen) i meldingsteksten som bør avklares videre — uklart om dette
er bevisst begrepsbruk eller inkonsistens i kilden [ANT]. Dette er
konsistent med og utdyper allerede forankret funn i delrapport
`helsepersonellplan-2040.md`. Merk statusforbehold: dette er en melding,
ikke et vedtak, og selve Helsebibliotek-tiltaket er en
utredningsbeslutning (utrede, ikke bygge).

### 4.2 Helsenorge.no

- Innbyggerrettet plattform, sentral kanal for helseinformasjon til
  befolkningen. [ANT] Formelt eierskap/driftsansvar (Helsedirektoratet
  som konseptansvarlig, NHN som driftsleverandør) bør verifiseres presist
  mot NHN/Hdir-kilder utover det som allerede er dekket i prosjektets
  øvrige delrapporter (jf. CLAUDE.md-rollebeskrivelsen).
- **Relevans:** Naturlig kandidat som distribusjonskanal for
  innbyggerrettet kunnskapsinnhold i en modernisert kjede — allerede lagt
  til grunn i delrapport 4 og Meld. St. 11 kap. 7.2 (jf.
  `helsepersonellplan-2040.md`).

### 4.3 Kjernejournal

- Inneholder pasientdata (kritisk info, resepter, kontakter), ikke
  kunnskapsinnhold/retningslinjer i seg selv. [ANT] Relevant primært som
  mulig integrasjonspunkt for pasientspesifikk beslutningsstøtte
  (CDS Hooks-lignende mønster), ikke som lager for kunnskapsprodukter.

### 4.4 Felles språk / SNOMED CT-programmet

- Se pkt. 2.1 over — status: fra pilot til etablert forvaltning i
  Helsedirektoratet, med lenkestrategi til ICD-10/ICPC-2.

### 4.5 NHNs plattformtjenester og HelseID

- NHN drifter nasjonale plattformtjenester (meldingsutveksling,
  API-infrastruktur, HelseID for autentisering/autorisasjon) [DOK,
  konsistent med NHNs rolle beskrevet i CLAUDE.md]. HelseID er relevant
  som mulig tilgangsstyringsmekanisme for en fremtidig kunnskapstjeneste
  (f.eks. differensiert tilgang for helsepersonell vs. innbyggere).
- [ANT] Ingen av disse er i kildene eksplisitt koblet til
  kunnskapsformidling — dette er en arkitektonisk vurdering, ikke et
  dokumentert faktum.

---

## 5. RAG-/LLM-arkitekturer over kvalitetssikret kunnskapsinnhold

### 5.1 Arkitekturmønstre

- RAG-mønsteret: retriever henter relevante segmenter fra en avgrenset
  korpus (f.eks. kliniske retningslinjer), generator (LLM) produserer
  svar basert på spørring + hentede segmenter, for å forankre svar og
  redusere hallusinasjon [DOK].
- Konkret forskningseksempel: NICE-basert RAG-system (UK) med 10 195
  tekstchunker fra 300 kliniske retningslinjer. Faithfulness
  (groundedness) 99,5 % med RAG mot 43 % for ren medisinsk baseline uten
  RAG (Wang et al., arXiv:2510.02967, okt. 2025) [DOK] — forskningsprosjekt,
  ikke bekreftet driftssatt NHS-tjeneste.
- Litteraturen skiller «naïve», «advanced» og «modular» RAG. Modulær RAG
  støtter flere retrieval-strategier og kildetyper — [ANT] relevant for
  en norsk kjede med flere innholdstyper (retningslinjer, evidens,
  innbyggerinfo).
- [ANT] Ingen kilde gir «beste praksis» for chunking/embedding spesifikt
  for norsk medisinsk fagspråk — trolig et gap som må utredes empirisk.

### 5.2 Styringsmekanismer i regulert kontekst

- Anbefalt praksis: sporing av dokumentkilde, versjonshistorikk,
  tidsstempel for embedding, revisjonsspor for etterlevelse [DOK].
  Kunnskapsbasen bør begrenses til autoritative, versjonskontrollerte
  kilder, med klare «refusal policies» og ikke-forhandlingsbar menneskelig
  kontroll av kliniske beslutninger [DOK].
- [ANT] Ingen offentlig, formalisert myndighetsstandard funnet for
  hvordan versjonering/sporbarhet konkret skal implementeres i regulert
  helsekontekst — feltet er i praksisutvikling, ikke normert.

### 5.3 Erfaringer fra offentlig sektor

- **Sentralt norsk funn:** Rapporten *«Fra ord til økosystem:
  Språkmodeller og generativ KI i Norge»* (Digitaliserings- og
  forvaltningsdepartementet, Agenda Kaupang/Simula, regjeringen.no, sep.
  2025) sier eksplisitt at RAG er lovende, men **det er fortsatt for
  tidlig å avgjøre om RAG+LLM fungerer godt nok for relevante
  bruksområder i norsk helse- og omsorgstjeneste** — mer erfaring trengs
  før storskala anbefaling [DOK].
- Helsedirektoratet omtaler at RAG testes i DigiUNG og Helsesvar, og
  anbefaler et felles kvalitetsrammeverk for testing/evaluering av
  LLM-er (med FHI, Helsetilsynet, Digdir m.fl.), med gradvis pilotering
  fra lavrisiko administrative bruksområder [DOK].
- Internasjonalt: ingen bekreftede, offisielt dokumenterte, driftssatte
  RAG/LLM-løsninger over kvalitetssikret klinisk kunnskap funnet hos WHO
  eller europeiske helsemyndigheter for øvrig [ANT — fravær støtter at
  feltet er tidlig/umodent, men er ikke bevis på at slike løsninger ikke
  finnes ikke-offentliggjort].
- Ingen norsk kilde beskriver et driftssatt RAG-system spesifikt over
  Helsedirektoratets nasjonale faglige retningslinjer.

### 5.4 Kjente risikoer/fallgruver

- Analyse (mai 2025, PMC): GPT-4.1 utelot gjeldende kliniske
  retningslinjer i 46 % av svar om hyperkolesterolemi, 22 % om type
  2-diabetes, til tross for eksplisitt instruksjon; DeepSeek-V3 utelot
  dem i 97 % av tilfellene [DOK].
- WHO (18. jan. 2024): *«Ethics and governance of AI for health:
  guidance on large multi-modal models»*, 40+ anbefalinger. Identifiserte
  risikoer: villedende/skjev informasjon, ulik tilgang, cybersikkerhet
  [DOK].
- RAG reduserer, men eliminerer ikke, hallusinasjon — avhenger av
  treffsikker retrieval og at modellen faktisk begrenser seg til hentet
  evidens [DOK].

---

## 6. EU AI Act og MDR — implikasjoner for beslutningsstøtte

### 6.1 EU AI Act — høyrisikoklassifisering

- Art. 6 gir to veier til høyrisiko: (1) sikkerhetskomponent i produkt
  under Vedlegg I-harmoniseringslovgivning (f.eks. MDR) som krever
  tredjeparts samsvarsvurdering, eller (2) systemer listet i Vedlegg
  III [DOK].
- Vedlegg III (8 kategorier) nevner **ikke** eksplisitt klinisk
  beslutningsstøtte. Nærmest er kategori 5 (essensielle tjenester:
  berettigelse til offentlige helsetjenester, forsikringsprising,
  nødtriage) — ikke det samme som et generelt kunnskapsstøtteverktøy
  [DOK].
- [ANT, juridisk usikker tolkning] Et RAG/LLM-kunnskapsstøttesystem
  faller trolig **ikke** direkte inn under Vedlegg III, med mindre det er
  sikkerhetskomponent i MDR-regulert utstyr som krever tredjepartsvurdering
  (Art. 6(1)) eller brukes til triage-lignende formål. Bør bekreftes mot
  Kommisjonens Art. 6-veiledning (frist 2. februar 2026).
- Art. 10 krever for høyrisikosystemer: dokumenterte data-/designvalg,
  skjevhetsvurdering (særlig helse/sikkerhet), representative og
  feilfrie datasett [DOK]. For systemer uten egen modelltrening (rent RAG
  uten finjustering) gjelder kravene trolig kun testdatasett (Art. 10(6))
  [ANT — uklart om dette dekker selve kunnskapskorpuset]. Dette er
  konsistent med, og utdyper, den sterkeste koblingen identifisert i det
  tidligere notatet `regulatorisk-etterslep.md` (AI Act art. 10 vs.
  fritekst/fragmentering, R2/R4).
- Høyrisikokrav trer i kraft **2. august 2026** [DOK].

### 6.2 MDR — klassifisering som medisinsk utstyr (MDSW)

- MDCG 2019-11 (revidert 17. juni 2025) er sentral veiledning for
  MDSW-kvalifisering/klassifisering, inkl. KI-basert programvare [DOK].
- **Rule 11** dekker klinisk beslutningsstøtte. Sentralt funn: **at en
  kliniker er «i loopen» fjerner ikke klassifiseringen som medisinsk
  utstyr** [DOK].
- Klassifisering spenner fra Klasse I til III avhengig av konsekvensen av
  beslutningen som tas basert på output [DOK].
- Programvare som kun lagrer/gjenfinner data (EPJ, timeavtaler) er ikke
  MDSW. Avgjørende: produsenten må «kommunisere» medisinsk bruksformål
  [DOK].
- [ANT, kritisk uavklart vurdering] Skillet mellom generisk
  kunnskapsformidling (trolig ikke MDSW) og pasientspesifikk
  beslutningsstøtte (trolig MDSW) bør avklares eksplisitt med
  jurister/Legemiddelverket før arkitekturvalg låses.
- **Forbehold:** MDCG 2019-11 og MDCG 2025-6 er ikke lest i fulltekst
  direkte (teknisk PDF-ekstraksjonsbegrensning under research) — funnene
  bygger delvis på sekundærkilder og bør verifiseres mot primærteksten.

### 6.3 Samspillet mellom AI Act og MDR

- MDCG 2025-6 (19. juni 2025) er offisiell FAQ om samspillet
  MDR/IVDR og AI-forordningen [DOK].
- Nøkkelpunkter (via sekundærkilder, ikke primærtekst): «produsent» i
  MDR = «tilbyder» i AI-forordningen; klassifisering etter
  AI-forordningen medfører **ikke automatisk** høyere MDR-risikoklasse —
  systemene vurderes uavhengig; MDCG oppfordrer til å integrere
  AI-forordningens krav i eksisterende MDR-kvalitetsstyringssystem
  fremfor parallelle systemer [DOK/sekundærkilde].
- Konsekvens: MDR Klasse I-selvsertifiserte systemer (uten
  tredjepartsvurdering) utløser trolig ikke Art. 6(1)-høyrisikoplikter;
  kun Klasse IIa+ med teknisk kontrollorgan gjør det [ANT].

### 6.4 Viktig spenning å fremheve videre

Det er en spenning — ikke en motstrid — mellom en mulig antakelse om at
«menneske i loopen» reduserer regulatorisk risiko, og MDCG 2019-11s
eksplisitte presisering at human-in-the-loop **ikke** fjerner
MDR-klassifiseringsplikten for klinisk beslutningsstøtteprogramvare. Dette
bør fremheves eksplisitt i den videre arkitektur- og
governance-vurderingen (delrapport 4/5), fordi det svekker en mulig
"lettvekts-antakelse" om at menneskelig kvalitetssikring alene holder
systemet utenfor MDR/AI Act-krav.

---

## 7. Motstridende informasjon i kildematerialet

Ingen direkte motstridende kildeutsagn er identifisert i dette
kunnskapsinnhentingspasset. Én reell spenning er identifisert internt i
kildematerialet:

- **SNOMED CT-strategi vs. FHIR-native ambisjon:** Norges SNOMED
  CT-strategi er å **lenke** til eksisterende kodeverk (ICD-10, ICPC-2)
  fremfor å erstatte dem [DOK, pkt. 2.1]. Internasjonale eksempler på
  CPG-on-FHIR/SMART Guidelines (pkt. 1.1, 1.3) forutsetter ofte sterkere
  FHIR-native terminologibruk. Dette er ikke en motstrid i kildene, men
  en arkitektonisk spenning som bør drøftes eksplisitt dersom Norge
  vurderer en full CPG-on-FHIR/SMART Guidelines-arkitektur.
- **«Nasjonal» vs. «offentlig» infrastruktur for Helsebiblioteket:**
  Meld. St. 11 kap. 8.3 bruker «nasjonal infrastruktur» i statusdelen og
  «offentlig infrastruktur» i tiltaksdelen (pkt. 4.1) — uklart om dette er
  bevisst distinksjon eller inkonsistent begrepsbruk i kilden [ANT].

---

## 8. Samlet kunnskapsgapsoversikt og forslag til oppfølging

| # | Gap | Forslag til oppfølging |
|---|-----|------------------------|
| 1 | CPG-on-FHIR/CQL i Norge/Norden — ingen dokumentert vurdering funnet | Avklar direkte med Helsedirektoratets fagmiljø for standardisering |
| 2 | CDS Hooks-støtte hos norske EPJ-leverandører (DIPS, Helseplattformen/Epic, CGM, Infodoc m.fl.) — ikke dekket av offentlige kilder | Direkte leverandørhenvendelse eller intern NHN-dokumentasjon |
| 3 | EBMonFHIR produksjonsmodenhet — uklart om noen har tatt det i bruk utover HL7s eget miljø | Følg opp mot Cochrane/GRADE-nettverket |
| 4 | WHO SMART Guidelines' overførbarhet til høyinntektsland som Norge | Avklar med oppdragsgiver om ambisjonen er metodikk (lagdeling) eller konkret plattform |
| 5 | ATC/ICPC-2 kobling til maskinlesbare CPG-artefakter — ingen konkrete eksempler funnet, verken internasjonalt eller i Norge | Noteres som reelt kunnskapshull i utredningen |
| 6 | Formelt eierskap/driftsmodell Helsenorge — bør presiseres | Verifiser mot NHN/Hdir-kilder |
| 7 | MDCG 2019-11 og 2025-6 ikke lest i fulltekst (PDF-begrensning) | Hent og verifiser manuelt, spesielt Rule 11-klassifiseringstabellen |
| 8 | Ingen bekreftet driftssatt offentlig RAG/LLM-løsning over kvalitetssikret klinisk kunnskap, verken i Norge eller internasjonalt | Følg DFD/Hdir sine pågående piloter (DigiUNG, Helsesvar, ETI) |
| 9 | Presis juridisk grense mellom «generisk kunnskapsformidling» (trolig ikke MDSW) og «pasientspesifikk beslutningsstøtte» (trolig MDSW) | Avklar med jurist/Legemiddelverket/DFØ før arkitekturvalg låses |
| 10 | Kommisjonens Art. 6-klassifiseringsveiledning for AI Act ikke publisert ennå (frist 2. feb. 2026) | Følg opp når publisert |
| 11 | Ontologier/kunnskapsgrafer for medisinsk evidens — ingen norske/europeiske produksjonseksempler | Undersøk norske FoU-miljøer (NTNU, SINTEF, NHN FoU) |

---

## 9. Samlet kildeliste

**Standarder og teknisk dokumentasjon (HL7/WHO):**
- https://hl7.org/fhir/uv/cpg/
- https://hl7.org/fhir/uv/cpg/methodology.html
- https://build.fhir.org/ig/HL7/cdc-opioid-cpg/
- https://build.fhir.org/ig/cqframework/opioid-cds-r4/
- https://cql.hl7.org/
- https://cql.hl7.org/STU2/01-introduction.html
- https://github.com/cqframework/clinical_quality_language
- https://www.ncqa.org/resources/clinical-quality-language-and-cql-engines-the-basics/
- https://cds-hooks.hl7.org/
- https://confluence.hl7.org/display/CDS/EBMonFHIR
- https://github.com/HL7/ebm
- https://www.who.int/teams/digital-health-and-innovation/smart-guidelines
- https://smart.who.int/dak-tb/index.html
- https://smart.who.int/dak-immz/

**Norske kilder:**
- https://www.helsedirektoratet.no/faglige-rad/anbefaling-om-bruk-av-smart-on-fhir/anbefaling-om-bruk-av-smart-on-fhir.pdf (merknad 25.09.2024)
- https://www.helsedirektoratet.no/digitalisering-og-e-helse/helsefaglig-terminologi/snomed-ct-i-norge (hentet 05.02.2025)
- https://www.ehelse.no/kodeverk-og-terminologi/SNOMED-CT/detaljert-om-snomed-ct/bruk-av-snomed-ct-i-noreg
- https://www.helsedirektoratet.no/digitalisering-og-e-helse/helsefaglige-kodeverk/icd/om-overgangen-til-icd-11-i-norge
- https://www.helsedirektoratet.no/digitalisering-og-e-helse/helsefaglige-kodeverk/icpc
- https://atcddd.fhi.no/atc_ddd_methodology/who_collaborating_centre/
- https://www.fhi.no/he/legemiddelbruk/who-senteret/
- https://www.helsedirektoratet.no/standarder/atc-anatomisk-terapeutisk-kjemisk-legemiddelregister
- Meld. St. 11 (2025–2026) Helsepersonellplan 2040, kap. 8.3 (regjeringen.no)
- «Fra ord til økosystem: Språkmodeller og generativ KI i Norge» (DFD, Agenda Kaupang/Simula, sep. 2025), regjeringen.no
- Helsedirektoratet, rapport om store språkmodeller i helse- og omsorgstjenesten (kvalitetsrammeverk-anbefaling)

**EU-kilder:**
- EUR-Lex, Regulation (EU) 2025/327 (EHDS), CELEX 32025R0327
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 (AI Act)
- https://artificialintelligenceact.eu/article/6/
- https://artificialintelligenceact.eu/article/10/
- https://artificialintelligenceact.eu/annex/3/
- https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2019_11_guidance_en_0.pdf (MDCG 2019-11)
- https://health.ec.europa.eu/document/download/b78a17d7-e3cd-4943-851d-e02a2f22bbb4_en?filename=mdcg_2025-6_en.pdf (MDCG 2025-6)

**Forskning/øvrige myndighetskilder:**
- WHO, «Ethics and governance of AI for health: guidance on large multi-modal models» (18.01.2024): https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content
- Wang et al., «Grounding LLMs in Clinical Evidence: RAG for NICE Guidelines», arXiv:2510.02967 (okt. 2025)
- PMC13110572 — omission/hallucination-analyse av kliniske retningslinjer i LLM-output
- The Lancet Digital Health, PIIS2589-7500(21)00038-8 (WHO SMART Guidelines)
- medinform.jmir.org/2025/1/e58858 (Ghana/Etiopia DAK-følgeforskning)

---

## 10. Relasjon til øvrig utredning

Dette notatet bygger videre på og er konsistent med:
- `regulatorisk-etterslep.md` — bekrefter og utdyper konklusjonen om at
  EHDS ikke treffer kjerneleddene i verdikjeden direkte, og at AI Act
  art. 10 er den sterkeste direkte reguleringskoblingen til R2/R4.
- `helsepersonellplan-2040.md` — bekrefter og siterer direkte
  Helsebibliotek-funnet fra Meld. St. 11 kap. 8.3.
- `utfordringer-og-flaskehalser.md` (R4: fragmentert IT-landskap/
  kodeverk) — gir teknisk konkretisering av mulige byggeklosser som kan
  adressere R4.

Notatet bør vurderes innarbeidet i delrapport 4 (ny verdikjede, som
teknisk grunnlag for alternativene) og delrapport 5 (arkitektur og
komponenter, som standardgrunnlag) ved neste revisjon av disse.
