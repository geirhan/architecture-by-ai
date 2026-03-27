# Delrapport 5: Arkitektur og komponenter for KI-støttet kunnskapsforvaltning

## Del av utredning om ny verdikjede for kunnskapsforvaltning i helsesektoren

---

## 1. Innledning

### 1.1 Formål

Denne delrapporten beskriver den tekniske og organisatoriske
arkitekturen for en KI-støttet verdikjede for kunnskapsforvaltning
i helsesektoren. Arkitekturen bygger på funnene fra de foregående
delrapportene: kartlegging av dagens verdikjede (delrapport 1),
identifiserte utfordringer og flaskehalser (delrapport 2),
vurdering av LLM-teknologiens muligheter og risikoer
(delrapport 3) og internasjonale erfaringer (delrapport 6).

Formålet er å gi et konkret bilde av hvilke komponenter som
trengs, hvordan de henger sammen, og hvordan de kan realiseres
innenfor eksisterende nasjonale rammer for e-helse.

### 1.2 ArchiMate som modelleringsspråk

Arkitekturen er beskrevet i tråd med ArchiMate-rammeverket,
som er en åpen standard for virksomhetsarkitektur
(The Open Group). ArchiMate strukturerer arkitekturen
i tre hovedlag:

- **Forretningslaget** – prosesser, roller og
  informasjonsobjekter
- **Applikasjonslaget** – programvarekomponenter, tjenester
  og integrasjoner
- **Teknologilaget** – infrastruktur, plattformer og nettverk

Denne lagdelingen gir en systematisk tilnærming til å
beskrive løsningen fra forretningsbehov til teknisk
realisering.

### 1.3 Kobling til EHDS-arkitektur

Arkitekturen er utformet med tanke på samsvar med det
europeiske helsedataområdet (EHDS). Kunnskapsforvaltning
understøtter EHDS' primærbruk ved å sikre at
helseinformasjon som deles på tvers av landegrenser er
basert på oppdatert, verifisert kunnskap. Nærmere vurdering
av EHDS-koblingen gis i kapittel 6.

---

## 2. Arkitekturprinsipper

Følgende prinsipper ligger til grunn for arkitekturen. De er
forankret i Referansearkitektur for e-helse og tilpasset den
spesifikke konteksten for KI-støttet kunnskapsforvaltning.

| Prinsipp | Beskrivelse | Implikasjon |
| --- | --- | --- |
| **Åpenhet og transparens** | Alle KI-prosesser skal være sporbare og forklarbare | Kildehenvisninger og beslutningslogg i alle KI-genererte produkter |
| **Modularitet og løs kobling** | Komponenter skal kunne utvikles, byttes ut og skaleres uavhengig | Standardiserte API-er mellom alle komponenter |
| **Gjenbruk av nasjonale felleskomponenter** | Eksisterende nasjonal infrastruktur skal benyttes der det er mulig | Bruk av HelseID, Grunndata, helsenettet |
| **Sikkerhet og personvern by design** | Sikkerhets- og personvernhensyn skal integreres fra start | DPIA, dataminimering, tilgangskontroll i alle lag |
| **Skalerbarhet** | Arkitekturen skal tåle varierende belastning og voksende datavolum | Skybasert infrastruktur med elastisk skalering |
| **Leverandøruavhengighet** | Løsningen skal ikke være låst til én leverandør eller teknologiplattform | Åpne standarder, abstraksjonslag mot KI-modeller |
| **Samsvar med Referansearkitektur for e-helse** | Arkitekturen skal følge nasjonale arkitekturkrav | Vurdering mot gjeldende referansearkitektur |

---

## 3. Forretningslag (ArchiMate Business Layer)

Forretningslaget beskriver prosessene, rollene og
informasjonsobjektene som arkitekturen skal understøtte.

### 3.1 Forretningsprosesser

Den nye verdikjeden består av fem hovedprosesser, der
KI-støtten varierer i grad og karakter:

#### 1. Kunnskapssyntese (KI-assistert)

Sammenstilling av forskningsevidens til strukturerte
kunnskapsoppsummeringer. KI-komponentene utfører søk,
screening og førsteutkast til dataekstraksjon, men
fageksperter har ansvar for kvalitetsvurdering og
konklusjon. Som beskrevet i delrapport 3, kan denne
prosessen potensielt redusere tidsbruken med 30–80 prosent
avhengig av prosesstrinn, forutsatt tilstrekkelig
menneskelig kvalitetssikring.

#### 2. Retningslinjeutvikling (KI-støttet)

Utvikling og oppdatering av nasjonale faglige
retningslinjer. KI-komponenter identifiserer ny relevant
evidens, genererer utkast og utfører konsistenssjekk mot
eksisterende retningslinjer. Retningslinjepaneler beholder
beslutningsmyndighet.

#### 3. Kvalitetssikring (hybrid menneske-KI)

Systematisk kontroll av KI-generert innhold. Inkluderer
automatisert faktasjekk mot kildemateriale, deteksjon av
hallusinering og inkonsistens, samt menneskelig
fagfellevurdering. Denne prosessen er kritisk for å
opprettholde tillit til kunnskapsproduksjonen.

#### 4. Kunnskapsformidling (automatisert med redaksjonelt tilsyn)

Publisering og distribusjon av verifisert kunnskap.
KI-komponenter håndterer klarspråk-oversettelse,
formatering for ulike kanaler og flerspråklig tilpasning.
Redaksjonelt ansvar forblir hos mennesker.

#### 5. Innbyggerdialog (KI-chatbot med eskalering til menneske)

Konversasjonsbasert helseinformasjon for innbyggere.
KI-chatboten besvarer spørsmål basert på verifiserte
kunnskapskilder, med tydelige mekanismer for eskalering
til helsepersonell ved behov. Chatboten genererer aldri
medisinske råd utover det som finnes i de godkjente
kildene.

### 3.2 Forretningsroller

| Rolle | Aktør | Ansvar i verdikjeden |
| --- | --- | --- |
| Kunnskapsprodusent | FHI | Utarbeider kunnskapsoppsummeringer og systematiske oversikter |
| Retningslinjeeier | Helsedirektoratet | Utvikler og vedlikeholder nasjonale faglige retningslinjer |
| Tjenesteleverandør | NHN | Drifter og forvalter tekniske komponenter og nasjonal infrastruktur |
| Kvalitetssikrer | Fageksperter | Validerer KI-generert innhold og godkjenner publikasjoner |
| Innbygger | Sluttbruker | Mottar helseinformasjon via helsenorge.no, chatbot og andre kanaler |

### 3.3 Forretningsobjekter

De sentrale informasjonsobjektene i verdikjeden er:

- **Forskningsartikkel** – Primærkilde fra vitenskapelige
  tidsskrifter
- **Kunnskapsoppsummering** – Strukturert syntese av
  forskningsevidens
- **Retningslinje** – Normerende dokument med faglige
  anbefalinger
- **Innbyggerrettet helseråd** – Klarspråklig
  helseinformasjon tilpasset innbyggere
- **Kvalitetsrapport** – Dokumentasjon av
  kvalitetssikringsprosesser og -resultater

Disse objektene har relasjoner seg imellom: en retningslinje
er basert på kunnskapsoppsummeringer, som igjen bygger på
forskningsartikler. Innbyggerrettede helseråd avledes fra
retningslinjer. Kvalitetsrapporter dokumenterer prosessene
som produserer de øvrige objektene.

---

## 4. Applikasjonslag (ArchiMate Application Layer)

### 4.1 Kjernekomponenter

Applikasjonslaget består av seks kjernekomponenter som til
sammen realiserer forretningsprosessene.

#### Komponent 1: Kunnskapssyntese-motor

KI-komponenten for automatisert litteraturgjennomgang og
kunnskapssyntese.

| Aspekt | Beskrivelse |
| --- | --- |
| **Funksjoner** | Systematisk søk i vitenskapelige databaser, screening av titler og sammendrag, dataekstraksjon fra fulltekst, generering av synteseutkast |
| **Teknologi** | LLM med RAG (Retrieval-Augmented Generation) mot indekserte vitenskapelige databaser |
| **Datakonsumenter** | FHI-forskere, retningslinjearbeidsgrupper |
| **Integrasjoner** | PubMed, Cochrane Library, Embase, Epistemonikos |

#### Komponent 2: Retningslinjestøttesystem

Verktøy for KI-støttet utvikling og vedlikehold av nasjonale
faglige retningslinjer.

| Aspekt | Beskrivelse |
| --- | --- |
| **Funksjoner** | Generering av retningslinjeutkast basert på kunnskapsgrunnlag, konsistenssjekk mot eksisterende retningslinjer, versjonskontroll, endringslogg |
| **Teknologi** | LLM med spesialiserte instruksjoner for retningslinjeformat, integrasjon med kunnskapssyntese-motoren |
| **Datakonsumenter** | Helsedirektoratets retningslinjeforfattere og -paneler |
| **Integrasjoner** | Kunnskapssyntese-motor, kunnskapsbase |

#### Komponent 3: Kunnskapsformidlingsplattform

Plattform for publisering og distribusjon av verifisert
kunnskap.

| Aspekt | Beskrivelse |
| --- | --- |
| **Funksjoner** | Automatisk klarspråk-oversettelse av faglig innhold, flerspråklig støtte (norsk bokmål, nynorsk, samisk, engelsk), multiformat-publisering (web, PDF, API) |
| **Teknologi** | LLM for teksttilpasning, maler for ulike formater |
| **Datakonsumenter** | Innbyggere, helsepersonell |
| **Integrasjoner** | helsenorge.no, Helsedirektoratets nettsider, Helsebiblioteket |

#### Komponent 4: Innbygger-chatbot

Konversasjonsbasert grensesnitt for helseinformasjon til
innbyggere.

| Aspekt | Beskrivelse |
| --- | --- |
| **Funksjoner** | Spørsmål-svar basert på verifiserte kilder, konteksttilpasning, tydelig kommunikasjon av begrensninger, eskalering til helsepersonell |
| **Teknologi** | LLM med RAG mot verifiserte kunnskapskilder i kunnskapsbasen, guardrails for å hindre uautorisert medisinsk rådgivning |
| **Datakonsumenter** | Innbyggere |
| **Integrasjoner** | helsenorge.no, kunnskapsbase, eventuelt HelseID for personalisering |

#### Komponent 5: Kvalitetssikringsmodul

Automatisert og semi-automatisert kvalitetskontroll av
KI-generert innhold.

| Aspekt | Beskrivelse |
| --- | --- |
| **Funksjoner** | Faktasjekk mot kildemateriale, hallusinerings-deteksjon, sporbarhet (hvilke kilder et utsagn bygger på), revisjonslogg |
| **Teknologi** | Dedikerte modeller for faktasjekk og hallusinerings-deteksjon, regelbaserte sjekker for formatkonformitet |
| **Datakonsumenter** | Kvalitetssikrere, revisorer |
| **Integrasjoner** | Alle øvrige kjernekomponenter |

#### Komponent 6: Kunnskapsbase

Strukturert lager for verifisert kunnskap som fungerer som
den autoritative kilden for alle andre komponenter.

| Aspekt | Beskrivelse |
| --- | --- |
| **Funksjoner** | Versjonering av kunnskapsobjekter, metadata-håndtering, søk og oppslag, API for maskinell tilgang |
| **Teknologi** | Dokumentdatabase med vektorindeksering, HL7 FHIR Clinical Knowledge Resources for strukturerte data |
| **Datakonsumenter** | Alle kjernekomponenter, eksterne systemer |
| **Integrasjoner** | FHIR-grensesnitt, EHDS-grensesnitt |

### 4.2 Integrasjoner

Komponentene integrerer med et bredt sett av interne og
eksterne systemer:

| Integrasjon | Type | Formål |
| --- | --- | --- |
| Nasjonale helseregistre | API | Tilgang til registerdata som kontekst for kunnskapssyntese |
| HL7 FHIR | Standardisert grensesnitt | Strukturert utveksling av klinisk kunnskap (Clinical Knowledge Resources, CDS Hooks) |
| EHDS / MyHealth@EU | Grensekryssende grensesnitt | Deling av kunnskap med europeiske partnere |
| helsenorge.no | Web-integrasjon | Publisering av innbyggerrettet informasjon og chatbot |
| Helsepersonellportalen | Web-integrasjon | Tilgang for helsepersonell til faglige ressurser |
| Cochrane, PubMed, Embase | API | Tilgang til internasjonale kunnskapskilder |
| HelseID | Autentisering | Sikker pålogging for helsepersonell og eventuelt innbyggere |

---

## 5. Teknologilag (ArchiMate Technology Layer)

### 5.1 Infrastruktur

Infrastrukturen skal sikre at løsningen kan driftes sikkert
og stabilt innenfor norsk jurisdiksjon.

**Nasjonal skyinfrastruktur:** Komponentene driftes på
infrastruktur levert gjennom NHN eller godkjent norsk
skytjeneste. Databehandling av helsedata skal skje innenfor
norsk jurisdiksjon, i samsvar med krav fra
pasientjournalloven og personopplysningsloven.

**KI-beregningsressurser:** LLM-baserte tjenester krever
betydelig beregningskapasitet. Arkitekturen legger opp til
en hybrid modell der:

- Egne GPU-klynger kan benyttes for sensitive oppgaver
  og egentrenede modeller
- Kommersielle KI-API-er kan benyttes for oppgaver uten
  sensitiv data, forutsatt databehandleravtale og godkjent
  jurisdiksjon

**Sikker datalagring:** All lagring av kunnskapsobjekter,
loggdata og metadata skjer på norsk infrastruktur med
kryptering i hvile og under transport.

**Nettverk og sikkerhetssoner:** Løsningen opererer innenfor
NHNs sikkerhetsarkitektur med definerte soner for
internett-eksponerte tjenester, interne tjenester og data.

### 5.2 Teknologistakk

| Lag | Teknologi | Merknad |
| --- | --- | --- |
| **KI-modeller** | LLM-er (kommersielle API-er og/eller egne modeller) | Abstraksjonslag som gjør det mulig å bytte modell uten å endre øvrig arkitektur |
| **RAG-rammeverk** | Vektordatabaser (f.eks. pgvector, Qdrant), embedding-modeller | For kontekstbasert søk i kunnskapsbasen |
| **Orkestrering** | Agentrammeverk for KI-pipelines | Koordinerer flertrinns KI-prosesser (søk, screening, syntese) |
| **Observerbarhet** | Sentralisert logging, monitorering, sporbarhet | Full revisjonsspor for alle KI-operasjoner |
| **Autentisering** | HelseID | Nasjonal løsning for identitets- og tilgangsstyring |
| **Autorisasjon** | Rollebasert tilgangskontroll | Basert på forretningsrollene definert i kapittel 3.2 |
| **Kryptering** | TLS 1.3, AES-256 | I transport og i hvile |

---

## 6. Kobling til EHDS

Arkitekturen er utformet med sikte på samsvar med
EHDS-forordningen. Koblingspunktene er særlig relevante
på tre områder:

### 6.1 Interoperabilitet og standarder

EHDS stiller krav til bruk av europeiske standarder for
helseinformasjon. Arkitekturen adresserer dette gjennom bruk
av HL7 FHIR som primært grensesnitt for strukturerte data,
og gjennom støtte for European Health Record Exchange Format
(EHRxF). Kunnskapsbasen (komponent 6) er designet for å
eksponere data i FHIR-format, noe som muliggjør deling med
europeiske partnere.

### 6.2 MyHealth@EU og grensekryssende tjenester

NHN fungerer som nasjonalt kontaktpunkt for grensekryssende
helsetjenester gjennom MyHealth@EU.
Kunnskapsforvaltningsarkitekturen kan understøtte dette ved
å tilby verifisert, flerspråklig helseinformasjon som kan
deles med andre medlemsland. Innbygger-chatboten
(komponent 4) kan potensielt integreres med grensekryssende
tjenester for å gi helseinformasjon til innbyggere som
oppholder seg i andre land.

### 6.3 Kunnskapsforvaltning som enabler for EHDS primærbruk

EHDS' primærbruk handler om å styrke innbyggeres kontroll
over egne helseopplysninger og forbedre
helsetjenestelevering. KI-støttet kunnskapsforvaltning
understøtter dette ved å:

- Sikre at helseinformasjon som deles på tvers av
  landegrenser er oppdatert og kvalitetssikret
- Muliggjøre automatisk oversettelse og tilpasning av
  helseinformasjon til ulike språk og kontekster
- Tilby strukturerte, maskinlesbare retningslinjer som
  kan integreres i kliniske beslutningsstøttesystemer

---

## 7. Standarder og rammeverk

Arkitekturen bygger på et bredt sett av standarder og
rammeverk for å sikre interoperabilitet, kvalitet og
regulatorisk samsvar.

| Standard / rammeverk | Anvendelse i arkitekturen |
| --- | --- |
| **HL7 FHIR** | Strukturert utveksling av klinisk kunnskap (Clinical Knowledge Resources, CDS Hooks) |
| **IHE-profiler** | Rammeverk for integrasjon mellom helseapplikasjoner |
| **SNOMED CT** | Klinisk terminologi for strukturering av kunnskapsobjekter |
| **ICD-11** | Klassifikasjon av sykdommer og helsetilstander |
| **ATC** | Klassifikasjon av legemidler |
| **openEHR** | Kliniske arketyper for strukturert helsedata |
| **WHO SMART Guidelines** | Rammeverk for maskinlesbare retningslinjer (se delrapport 6) |
| **ISO 13606** | Standard for kommunikasjon av helseinformasjon |
| **EU AI Act** | Regulatorisk rammeverk for KI-systemer (se delrapport 3) |

Valg av standarder er gjort med tanke på samsvar med
EHDS-krav og eksisterende norsk e-helsepraksis. WHO SMART
Guidelines er særlig relevant fordi rammeverket gir en
metodikk for å konvertere narrative retningslinjer til
maskinlesbare formater – noe som understøtter automatisert
konsistenssjekk og integrasjon med kliniske
beslutningsstøttesystemer.

---

## 8. Sikkerhet og personvern

### 8.1 Trusselmodell

KI-støttet kunnskapsforvaltning introduserer trusler som
skiller seg fra tradisjonelle helse-IT-systemer:

- **Hallusinering:** KI-modeller kan generere plausible,
  men faktisk feilaktige utsagn. I helsekontekst kan dette
  ha direkte konsekvenser for innbyggere.
- **Prompt injection:** Ondsinnet manipulering av
  KI-chatboten for å generere uønsket innhold.
- **Datalekkasje:** Risiko for at treningsdata eller
  konfidensiell informasjon eksponeres gjennom modellens
  svar.
- **Bias:** Systematisk skjevhet i KI-generert innhold som
  kan diskriminere bestemte grupper.
- **Modellmanipulasjon:** Risiko for at underliggende
  modeller påvirkes av ondsinnet aktør.

### 8.2 Personvernkonsekvensvurdering (DPIA)

Arkitekturen forutsetter gjennomføring av DPIA før
implementering. Sentrale vurderingstemaer inkluderer:

- Behandling av personopplysninger i innbygger-chatboten
- Bruk av helserelaterte data for trening og finjustering
  av modeller
- Logging av brukerinteraksjoner
- Grensekryssende dataoverføring i EHDS-kontekst

### 8.3 Tilgangsstyring og roller

Tilgangsstyring baseres på HelseID og rollebasert
tilgangskontroll. Rollene følger forretningsrollene
definert i kapittel 3.2:

| Rolle | Tilgangsnivå |
| --- | --- |
| Fagekspert / kvalitetssikrer | Lese, redigere og godkjenne kunnskapsobjekter |
| Retningslinjeforfatter | Lese, opprette og redigere retningslinjer |
| Redaktør | Publisere og avpublisere innhold |
| Systemadministrator | Konfigurasjon og drift |
| Innbygger | Lese publisert innhold, bruke chatbot |

### 8.4 Logging, sporbarhet og dataminimering

Alle KI-operasjoner loggføres med full sporbarhet: hvilken
modell som ble brukt, hvilke kilder som ble konsultert, og
hvilket resultat som ble generert. Logging av
brukerinteraksjoner med chatboten begrenses til det som er
nødvendig for kvalitetsforbedring og feilretting, i tråd
med prinsippet om dataminimering.

### 8.5 Nasjonal kontroll

Arkitekturen sikrer nasjonal kontroll over helsedata gjennom
krav om norsk jurisdiksjon for datalagring og
databehandling. Ved bruk av kommersielle KI-API-er skal det
foreligge databehandleravtale, og sensitive data skal ikke
sendes ut av landet uten tilstrekkelig rettslig grunnlag.

---

## 9. Komponentdiagram – tekstbasert beskrivelse

Arkitekturen kan beskrives som et lagdelt diagram med fire
nivåer. Denne beskrivelsen er ment som grunnlag for
visualisering.

### Lag 1: Brukergrensesnitt (øverst)

Tre brukergrupper med tilhørende grensesnitt:

- **Innbygger** -> helsenorge.no (helseinformasjon og
  chatbot)
- **Helsepersonell** -> Helsepersonellportalen (faglige
  retningslinjer, kunnskapsressurser)
- **Fagekspert** -> Fagverktøy (kunnskapssyntese,
  retningslinjeredigering, kvalitetssikring)

### Lag 2: Applikasjonstjenester (midten)

De seks kjernekomponentene arrangert i to rader:

#### Produksjonskomponenter

- Kunnskapssyntese-motor <-> Retningslinjestøttesystem
  <-> Kunnskapsformidlingsplattform

#### Støttekomponenter

- Kvalitetssikringsmodul (kobler til alle
  produksjonskomponenter)
- Kunnskapsbase (sentral datakilde for alle komponenter)
- Innbygger-chatbot (konsumerer fra kunnskapsbasen)

### Lag 3: Integrasjonslag

- API-gateway (ekstern og intern trafikk)
- FHIR-server (standardiserte grensesnitt)
- EHDS-adapter (MyHealth@EU-tilkobling)
- Integrasjoner mot Cochrane, PubMed, Embase

### Lag 4: Infrastruktur (nederst)

- NHN skyinfrastruktur (compute, storage, nettverk)
- KI-beregningsressurser (GPU-klynger)
- HelseID (autentisering og autorisasjon)
- Sikkerhet (kryptering, brannmurer, sikkerhetssoner)
- Observerbarhet (logging, monitorering, sporbarhet)

**Dataflyt:** Kunnskap flyter fra eksterne kilder (lag 3)
gjennom produksjonskomponentene (lag 2) til kunnskapsbasen,
og derfra ut til brukerne (lag 1).
Kvalitetssikringsmodulen opererer som en tverrgående
kontroll på alle trinn.

---

## 10. Oppsummering

Arkitekturen for KI-støttet kunnskapsforvaltning bygger
på følgende grunnpilarer:

**Gjenbruk av eksisterende infrastruktur.** Løsningen
benytter NHNs nasjonale infrastruktur, HelseID for
identitetshåndtering og etablerte integrasjonsmønstre fra
norsk e-helse. Dette reduserer implementeringsrisiko og
utnytter investeringer som allerede er gjort.

**Modulær tilnærming.** De seks kjernekomponentene er løst
koblet gjennom standardiserte grensesnitt. Dette muliggjør
faseinndelt implementering der man kan starte med de
komponentene som gir størst verdi først
(f.eks. kunnskapssyntese-motoren) og gradvis bygge ut.

**Menneske-i-sløyfen.** Arkitekturen er konsekvent utformet
med menneskelig kvalitetssikring som en integrert del av
alle prosesser. KI-komponentene fungerer som verktøy for
fageksperter – ikke som erstatning.

**EHDS-samsvar.** Bruk av HL7 FHIR, åpne standarder og
grensekryssende grensesnitt posisjonerer løsningen for
samsvar med EHDS-forordningens krav til interoperabilitet.

**Sikkerhet og transparens.** Full sporbarhet for alle
KI-operasjoner, nasjonal kontroll over data og systematisk
håndtering av KI-spesifikke trusler (hallusinering, bias,
prompt injection).

For en samlet vurdering av arkitekturen i kontekst av
gjennomførbarhet, risiko og anbefalinger, se delrapport 7.

---

*Denne rapporten er del 5 av en utredning om ny verdikjede
for kunnskapsforvaltning i helsesektoren. Rapporten bør
leses i sammenheng med øvrige delrapporter, spesielt
delrapport 3 (LLM – muligheter og risikoer) og delrapport 6
(internasjonale erfaringer).*
