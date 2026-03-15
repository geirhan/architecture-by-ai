# Arkitekturkonsekvensanalyse: EHDS-implementering i Norge

## Sammendrag

Denne rapporten analyserer arkitekturkonsekvensene av tre tiltaksalternativer for EHDS-implementering i Norge. Analysen vurderer hvert alternativ langs fem kvalitetsdimensjoner (interoperabilitet, teknisk gjeld, vendor lock-in, skalerbarhet, sikkerhet) og gjennomfører en komponentanalyse av påvirkningen på kjernejournal, reseptformidleren, helsenorge.no, EPJ-systemer og nye EHDS-komponenter.

**Hovedfunn:**

- **Alternativ 1 (Stegvis minimum)** gir lavest kortsiktig risiko, men skaper et permanent gateway-lag som genererer teknisk gjeld og opprettholder to parallelle standardverdener. Konverteringstap mellom nasjonale formater og EEHRxF er en reell pasientsikkerhetsrisiko.
- **Alternativ 2 (Akselerert helhetlig)** gir best arkitekturkvalitet over tid ved å konsolidere til FHIR som nasjonal standard, men har svært høy gjennomføringskompleksitet og krever omfattende endringsledelse.
- **Alternativ 3 (Nordisk samarbeid)** gir pragmatisk verdi gjennom delte komponenter og stordriftsfordeler i leverandørdialog, men løser ikke de nasjonale arkitekturspørsmålene isolert.

**Anbefaling:** Fra et arkitekturperspektiv anbefales en hybridtilnærming der alternativ 2 settes som strategisk mål, med alternativ 1 som taktisk startpunkt for de første fristene, og alternativ 3 som en parallell samarbeidsdimensjon. Det kritiske er å unngå at gateway-laget i alternativ 1 sementeres som permanent arkitektur.

---

## 1. Vurdering av nå-situasjonen

### Styrker i dagens arkitektur

Norsk helsesektor har flere arkitekturmessige styrker som gir et godt utgangspunkt for EHDS-implementering:

1. **Kjernejournal er operativ og utbredt.** Norge har allerede en nasjonal oppsummeringsløsning (Summary Care Record) som dekker kritisk informasjon, legemiddelopplysninger og journaldokumenter. Kjernejournal har FHIR-baserte API-er for kritisk informasjon og dokumentdeling (IHE MHD-profil). Dette gir et konkret fundament for Patient Summary-kategorien i EHDS.

2. **Reseptformidleren (e-resept) er moden.** Norge har en velfungerende nasjonal e-reseptløsning som allerede er pilotert mot MyHealth@EU. Sentrale legemiddelregistre (FEST) og prosesser for e-forskrivning er etablert.

3. **HelseID gir nasjonal identitets- og tilgangsinfrastruktur.** En sentral identitetstjeneste med OAuth 2.0/OpenID Connect er allerede på plass, noe som forenkler tilgangskontroll i EHDS-kontekst.

4. **Helsenettet (NHN) gir sikker transportinfrastruktur.** Etablert nettverksinfrastruktur med sikkerhetssoner og adressregister.

5. **MyHealth@EU-pilotering er gjennomført.** NHN har allerede pilotert grensekryssende datautveksling, noe som gir erfaring med NCPeH-arkitekturen (National Contact Point for eHealth).

6. **FHIR-kompetanse er under oppbygging.** DIPS har FHIR-baserte API-er (Open DIPS), HL7 Norway har publisert 20 nasjonale FHIR-basisprofiler, og det gjennomføres nordiske FHIR-hackathons.

### Svakheter i dagens arkitektur

1. **Meldingsbasert integrasjon dominerer.** Norsk helsesektor er bygget rundt punkt-til-punkt-meldingsutveksling med nasjonale meldingsstandarder. Denne arkitekturen er fundamentalt annerledes enn den API-baserte, ressursorienterte tilnærmingen i FHIR/EEHRxF.

2. **Fragmentert EPJ-landskap.** DIPS Arena (fleste helseforetak), Helseplattformen/Epic (Helse Midt-Norge), og flere leverandører i primærhelsetjenesten (CGM, Visma, Infodoc) skaper et heterogent integrasjonsbilde. Helseplattformen har en helt annen arkitektur (Epic) enn resten av sektoren.

3. **Semantisk heterogenitet.** Ulike kodeverk, terminologier og detaljeringsnivå på tvers av virksomheter. Begrenset bruk av SNOMED CT og LOINC som EHDS forutsetter. Mapping mellom nasjonale kodeverk (ICD-10, ICPC-2, NKPK) og europeiske er ufullstendig.

4. **Manglende nasjonal informasjonsmodell.** Helse-NIM for oppsummerende helseopplysninger er under utvikling, men ikke ferdigstilt. Uten en autoritativ nasjonal informasjonsmodell er det vanskelig å sikre konsistent datarepresentasjon.

5. **Ingen infrastruktur for sekundærbruk.** Sikre analyserom (SPE) og HealthData@EU-tilkobling er i tidlig fase. Tilgangsmodellen for sekundærbruk er ikke etablert.

6. **Ingen nasjonal testinfrastruktur for EHR-sertifisering.** EHDS krever obligatorisk testing i nasjonalt testmiljø. Denne infrastrukturen eksisterer ikke.

### Vurdering av arkitekturmodenhet

Samlet sett befinner norsk helsesektor seg i en overgangsfase: nasjonale felleskomponenter (kjernejournal, e-resept, HelseID) gir et solid fundament, men integrasjonsmønstret (meldingsbasert), det semantiske grunnlaget og infrastrukturen for nye EHDS-funksjoner (sekundærbruk, sertifisering, grensekryssende utveksling) har betydelige gap.

---

## 2. Gap-analyse per alternativ

### 2.1 Alternativ 1 – Teknisk gap og konsekvenser

**Arkitekturvalg:** Føderert arkitektur med sentralt gateway-lag for konvertering mellom nasjonale formater og EEHRxF.

**Gap som må lukkes:**

| Gap | Tiltak | Kompleksitet | Risiko |
|-----|--------|-------------|--------|
| Manglende EEHRxF-støtte | Gateway-lag konverterer ved grensekryssing | Middels | Konverteringstap, semantisk informasjonstap |
| Manglende NCPeH | Bygge videre på NHN-pilot | Middels | Avhengig av gateway-kvalitet |
| Manglende HDAB | Ny funksjon på helsedata.no/FHI | Middels | Organisatorisk, ikke primært teknisk |
| Manglende testinfrastruktur | Begrenset testmiljø for prioriterte kategorier | Lav-Middels | Utilstrekkelig testdekning |
| Manglende sikre analyserom | SPUHiN videreføres | Middels | Knapp tidslinje |
| Semantisk mapping | Konverteringsregler i gateway | Hoy | Feilmapping, datatap |
| Innbyggerrettigheter | Tilpasning av helsenorge.no | Middels | Avhengig av gateway for EEHRxF-nedlasting |

**Kritisk konsekvens:** Gateway-tilnærmingen introduserer et sentralt feilpunkt (single point of failure) og en permanent konverteringskostnad. Erfaringer fra europeiske NCPeH-implementeringer viser at semantisk konvertering mellom nasjonale formater og felleseuropeiske formater er det mest feilprone leddet i grensekryssende datautveksling. Nasjonale systemer vil ikke dra nytte av FHIR-modernisering – gevinsten begrenses til grensekryssende scenarioer.

**Teknisk gjeld som genereres:**
- To parallelle standardverdener (nasjonale meldingsstandarder + EEHRxF) som begge må vedlikeholdes
- Gateway-konverteringsregler som må oppdateres når EEHRxF-spesifikasjoner endres
- EPJ-leverandører har ikke insentiv til å modernisere til FHIR nasjonalt

### 2.2 Alternativ 2 – Teknisk gap og konsekvenser

**Arkitekturvalg:** FHIR som nasjonal standard, nasjonale meldingsstandarder fases ut.

**Gap som må lukkes:**

| Gap | Tiltak | Kompleksitet | Risiko |
|-----|--------|-------------|--------|
| Manglende nasjonal FHIR-arkitektur | Helse-NIM, nasjonale FHIR-profiler, infrastruktur | Hoy | Spesifikasjonsarbeid tar tid |
| EPJ-migrering til FHIR | Alle leverandorer ma implementere FHIR-API | Svært hoy | Kapasitet, endringsmotstand |
| Utfasing av meldingsstandarder | Gradvis overgangsplan | Hoy | Overgangsperiode med to systemer |
| Manglende NCPeH | Bygge pa NHN-pilot, direkte FHIR | Middels | Enklere uten gateway-konvertering |
| HDAB, testinfrastruktur, SPE | Som alternativ 1, men bredere | Middels-Hoy | Parallell med FHIR-overgang |
| Terminologitjenester | Sentral nasjonal tjeneste for SNOMED CT, LOINC, ATC | Hoy | Krever nasjonal lisens og kompetanse |
| Kompetansebygging | Nasjonalt FHIR-kompetanseprogram | Middels | Kapasitetsmangel i overgangsperioden |

**Kritisk konsekvens:** Alternativ 2 krever at alle EPJ-leverandorer (DIPS, Epic/Helseplattformen, CGM, Visma, Infodoc) implementerer FHIR-baserte grensesnitt. DIPS har allerede FHIR-API-er (Open DIPS), men Epic/Helseplattformen opererer med sin egen integrasjonsmodell. Primærhelsetjenesten har svært mange installasjoner med begrenset teknisk modenhet.

**Teknisk gjeld som unngås:**
- Ingen varig gateway-konvertering
- Nasjonale og europeiske standarder konvergerer
- EPJ-leverandorer moderniserer én gang, ikke to

**Ny risiko som introduseres:**
- Overgangsperioden (anslagsvis 3-5 ar) krever midlertidig støtte for bade gamle og nye standarder
- Helseplattformen/Epic har en annen arkitekturfilosofi enn FHIR-basert nasjonal standard

### 2.3 Alternativ 3 – Teknisk gap og konsekvenser

**Arkitekturvalg:** Felles nordisk referansearkitektur, delte komponenter, nasjonal kjerneinfrastruktur beholdes.

**Gap som må lukkes:**

| Gap | Tiltak | Kompleksitet | Risiko |
|-----|--------|-------------|--------|
| Manglende nordisk referansearkitektur | Felles spesifikasjonsarbeid | Middels (teknisk), Hoy (koordinering) | Ulik modenhet, ulike tidsplaner |
| Delte terminologitjenester | Felles nordisk plattform | Middels | Ulike nasjonale kodeverk |
| Delt testinfrastruktur | Felles nordisk testmiljø | Middels | Ulike kravnivåer |
| Koordinert leverandørdialog | Felles nordisk kravspesifikasjon | Lav-Middels | Begrenset formelt mandat |
| Nasjonale gap (som alt. 1 eller 2) | Nasjonal implementering | Avhenger av nasjonal tilnærming | Avhenger av nasjonal tilnærming |

**Kritisk konsekvens:** Alternativ 3 løser ikke de nasjonale arkitekturspørsmålene – Norge må uansett velge mellom en gateway-tilnærming (alternativ 1) eller en FHIR-first-tilnærming (alternativ 2) nasjonalt. Det nordiske samarbeidet gir imidlertid reell verdi i tre områder:

1. **Leverandoroverlapp:** DIPS, Epic, CGM og Visma opererer i flere nordiske land. Koordinerte krav gir stordriftsfordeler.
2. **FHIR-basisprofiler:** Nordiske HL7-affiliater har allerede påbegynt harmonisering av nasjonale FHIR-basisprofiler (Organization, Patient, Practitioner er profilert i alle land). Dette arbeidet kan akselereres.
3. **Terminologi og testing:** Delte ressurser for terminologimapping og testinfrastruktur kan redusere kostnadene for hvert land.

**Begrensning:** EU-landene (Sverige, Danmark, Finland) har andre frister enn EØS-landene (Norge, Island). Sveriges e-helsemyndighet og Finlands FHIR-miljø har ulik modenhet. Risikoen for «laveste felles nevner» er reell.

---

## 3. Arkitekturkvalitet per alternativ

### 3.1 Interoperabilitet

| Dimensjon | Alt. 1 | Alt. 2 | Alt. 3 |
|-----------|--------|--------|--------|
| Nasjonal interoperabilitet | Lav (status quo) | Hoy (FHIR-konvergens) | Avhenger av nasjonal tilnærming |
| Europeisk interoperabilitet | Middels (via gateway) | Hoy (native FHIR) | Middels-Hoy |
| Nordisk interoperabilitet | Lav | Middels | Hoy (felles profiler) |
| Semantisk interoperabilitet | Lav (konvertering) | Middels-Hoy (felles kodeverk) | Middels (delte terminologitjenester) |

**Vurdering:** Alternativ 1 gir «tilsynelatende interoperabilitet» gjennom gateway-konvertering, men reell semantisk interoperabilitet oppnås ikke fordi kildedataene forblir i nasjonale formater. Erfaringer fra europeiske NCPeH-implementeringer bekrefter at gateway-basert konvertering er det svakeste leddet. Alternativ 2 gir best interoperabilitet over tid fordi nasjonale og europeiske standarder konvergerer. Alternativ 3 gir merverdi for nordisk interoperabilitet, men er avhengig av nasjonal tilnærming for faktisk interoperabilitetsnivå.

### 3.2 Teknisk gjeld

| Dimensjon | Alt. 1 | Alt. 2 | Alt. 3 |
|-----------|--------|--------|--------|
| Doble standarder | Ja (permanent) | Nei (overgangsperiode) | Avhenger av nasjonal tilnærming |
| Gateway-vedlikehold | Varig kostnad | Ingen | Mulig delt kostnad |
| Migrasjonsgjeld | Utsettes, akkumuleres | Håndteres proaktivt | Delvis delt |
| Konverteringsregler | Må holdes oppdatert | Ikke relevant | Kan deles |

**Vurdering:** Alternativ 1 genererer størst teknisk gjeld fordi det sementerer to parallelle standardverdener. Hvert gang EEHRxF-spesifikasjonene oppdateres, må konverteringsreglene i gateway-laget oppdateres tilsvarende. Over tid vil denne gjelden øke, ikke avta. Alternativ 2 har en overgangsperiode med midlertidig gjeld, men den langsiktige posisjonen er konsolidert. Alternativ 3 kan redusere vedlikeholdskostnadene gjennom deling, men løser ikke det underliggende problemet.

### 3.3 Vendor lock-in

| Dimensjon | Alt. 1 | Alt. 2 | Alt. 3 |
|-----------|--------|--------|--------|
| EPJ-leverandøravhengighet | Hoy (status quo) | Middels (apne API-er) | Middels (koordinerte krav) |
| Gateway-leverandør | Ny avhengighet (NHN/leverandør) | Ikke relevant | Mulig delt |
| Plattformavhengighet | Lav | Middels (FHIR-plattform) | Lav-Middels |

**Vurdering:** Alternativ 1 opprettholder dagens leverandøravhengighet og legger til en ny avhengighet av gateway-leverandøren. Alternativ 2 reduserer leverandøravhengigheten gjennom standardiserte FHIR-API-er – data blir mer portabel og leverandørbytte enklere. Helseplattformen/Epic representerer en særskilt lock-in-utfordring uavhengig av alternativ fordi Epic har en proprietær integrasjonsmodell som avviker fra åpne FHIR-baserte tilnærminger. Alternativ 3 kan styrke forhandlingsposisjonen overfor leverandører gjennom koordinerte nordiske krav.

### 3.4 Skalerbarhet

| Dimensjon | Alt. 1 | Alt. 2 | Alt. 3 |
|-----------|--------|--------|--------|
| Nye datakategorier | Vanskelig (ny konvertering per kategori) | Enklere (utvidelse av FHIR-profiler) | Avhenger av nasjonal tilnærming |
| Økt volum | Gateway kan bli flaskehals | Distribuert, skalerbart | Delt lastfordeling mulig |
| Nye tjenester | Begrenset av gateway | Nye tjenester kan bygges direkte på FHIR | Delte nordiske tjenester mulig |

**Vurdering:** EHDS innfører datakategorier i to faser (gruppe 1: mars 2029, gruppe 2: mars 2031), men forordningen åpner for fremtidig utvidelse. Alternativ 1 skalerer dårlig fordi hver ny datakategori krever nye konverteringsregler i gateway. Alternativ 2 skalerer bedre fordi FHIR-ressursmodellen er designet for utvidelse. Alternativ 3 gir potensial for delt skalering, men er avhengig av nordisk enighet om nye kategorier.

### 3.5 Sikkerhet og personvern by design

| Dimensjon | Alt. 1 | Alt. 2 | Alt. 3 |
|-----------|--------|--------|--------|
| Tilgangskontroll | HelseID + gateway-lag | HelseID + FHIR-autorisasjon | HelseID + nordisk IAM-samarbeid |
| Sporbarhet/logging | Gateway-logging + nasjonale logger | Ende-til-ende FHIR AuditEvent | Delt loggingsstandard mulig |
| Opt-out/reservasjon | Gateway må håndheve | Native i FHIR Consent | Koordinert implementering |
| Dataminimering | Gateway kan filtrere | FHIR-profiler styrer omfang | Felles profiler sikrer konsistens |
| Grensekryssende sikkerhet | eHDSI-sikkerhet via NCPeH | eHDSI-sikkerhet via NCPeH | eHDSI-sikkerhet via NCPeH |

**Vurdering:** Alle tre alternativer kan i prinsippet oppfylle sikkerhetskravene, men de gjør det på ulike måter. Alternativ 2 har en arkitekturmessig fordel fordi FHIR har innebygde ressurser for samtykke (Consent), sporbarhet (AuditEvent) og tilgangskontroll som kan brukes ende-til-ende. Alternativ 1 krever at gateway-laget implementerer disse funksjonene som et ekstra lag, noe som øker kompleksiteten og risikoen for feil. Alternativ 3 kan gi merverdi gjennom delt utvikling av sikkerhetsmønstre.

---

## 4. Integrasjonskompleksitet

### Integrasjonspunkter per alternativ

| Integrasjonspunkt | Alt. 1 | Alt. 2 | Alt. 3 |
|-------------------|--------|--------|--------|
| EPJ → Gateway/FHIR-plattform | ~5-7 leverandører | ~5-7 leverandører | ~5-7 leverandører |
| Gateway/FHIR → NCPeH | 1 | 1 | 1 |
| NCPeH → MyHealth@EU | 1 | 1 | 1 |
| Kjernejournal → Gateway/FHIR | 1 | 1 | 1 |
| Reseptformidleren → Gateway/FHIR | 1 | 1 | 1 |
| Helsenorge.no → Gateway/FHIR | 1 | 1 | 1 |
| HDAB → HealthData@EU | 1 | 1 | 1 |
| Sikre analyserom → HDAB | 1 | 1 | 1 |
| Gateway-konverteringsmoduler | ~6-10 (per datakategori) | 0 | 0-5 (delt) |
| Nordisk koordinering | 0 | 0 | ~4-6 (per delt komponent) |
| **Totalt estimat** | **~18-24** | **~12-15** | **~16-22** |

### Avhengighetsanalyse

**Alternativ 1 – Kritisk avhengighetskjede:**
```
EPJ (nasjonalt format) → Gateway-konvertering → EEHRxF → NCPeH → MyHealth@EU
```
Enhver feil i gateway-konverteringen propagerer til grensekryssende utveksling. Gateway er et sentralt feilpunkt.

**Alternativ 2 – Enklere avhengighetskjede:**
```
EPJ (FHIR) → Nasjonal FHIR-plattform → NCPeH → MyHealth@EU
```
Færre transformasjonspunkter, men avhengig av at alle leverandører leverer FHIR.

**Alternativ 3 – Tillegg av nordisk lag:**
```
[Nasjonal kjede som alt. 1 eller 2] + Nordisk koordineringslag
```
Legger til en koordineringsdimensjon som kan forsinke nasjonal beslutningsevne.

### Risikovurdering av integrasjonskompleksitet

| Risikofaktor | Alt. 1 | Alt. 2 | Alt. 3 |
|--------------|--------|--------|--------|
| Antall transformasjonspunkter | Hoy | Lav | Middels |
| Avhengighet av enkeltkomponent | Hoy (gateway) | Middels | Middels |
| Leverandørkoordinering | Middels | Hoy | Hoy |
| Tidskritisk avhengighet | Middels | Hoy | Hoy |
| Semantisk feilrisiko | Hoy | Middels | Middels |

---

## 5. Komponentanalyse

### 5.1 Kjernejournal – påvirkning og tilpasningsbehov

Kjernejournal er den nasjonale komponenten som er nærmest EHDS-kravene for Patient Summary (prioritert kategori, gruppe 1).

| Aspekt | Alt. 1 | Alt. 2 | Alt. 3 |
|--------|--------|--------|--------|
| Tilpasning | Middels: Eksisterende data eksponeres via gateway i EEHRxF | Hoy: Kjernejournal migrerer til FHIR-basert datamodell, blir nasjonal Patient Summary-tjeneste | Middels: Som alt. 1 eller 2, med nordisk profilering |
| FHIR-modenhet | Har allerede FHIR-API for kritisk informasjon og dokumentdeling (MHD) | Utvides med IPS (International Patient Summary) FHIR-profil | Nordisk IPS-profilering |
| Risiko | Konverteringstap ved gateway-oversettelse | Migrasjonsrisiko, men bedre langsiktig | Koordineringsrisiko |
| Estimert innsats | Middels | Hoy | Middels-Hoy |

**Vurdering:** Kjernejournal har et godt utgangspunkt med eksisterende FHIR-API-er. I alternativ 1 eksponeres kjernejournaldata via gateway, men konvertering fra nasjonalt format til IPS kan gi informasjonstap (f.eks. i struktureringen av kritisk informasjon, legemiddelopplysninger). I alternativ 2 videreutvikles kjernejournal til en fullverdig nasjonal IPS-tjeneste basert på HL7 FHIR IPS-profilen. Alternativ 2 er mest arkitekturryddig, men krever størst innsats.

### 5.2 Reseptformidleren – påvirkning og tilpasningsbehov

Reseptformidleren (e-resept) er allerede pilotert mot MyHealth@EU og håndterer en prioritert kategori (gruppe 1).

| Aspekt | Alt. 1 | Alt. 2 | Alt. 3 |
|--------|--------|--------|--------|
| Tilpasning | Lav-Middels: Videreføre pilot, gateway-konvertering til ePrescription/eDispensation | Middels: Migrering til FHIR-basert reseptmodell nasjonalt | Lav-Middels: Som alt. 1, med nordisk harmonisering av legemiddeldata |
| MyHealth@EU-tilkobling | Via NCPeH, allerede pilotert | Via NCPeH, enklere med native FHIR | Via NCPeH, nordisk koordinering |
| FEST-tilpasning | Mapping fra FEST til europeiske legemiddelkodeverk | FEST moderniseres til FHIR-terminologi | Nordisk mapping av legemiddeldata |
| Risiko | Begrenset – e-resept er relativt modent | Migrering av FEST er omfattende | Ulike nasjonale legemiddelregistre |

**Vurdering:** Reseptformidleren er den mest modne komponenten for EHDS. MyHealth@EU-piloteringen har allerede vist at grensekryssende e-resept fungerer. Hovedutfordringen er semantisk: mapping mellom norske legemiddelkodeverk (FEST/ATC) og europeiske formater. I alternativ 1 håndteres dette i gateway, i alternativ 2 moderniseres FEST-integrasjonen til FHIR. Alternativ 3 gir verdi fordi nordiske legemiddelmarkeder har overlapp og delt terminologiarbeid er nyttig.

### 5.3 Helsenorge.no – påvirkning og tilpasningsbehov

Helsenorge.no er innbyggerportalen som må understøtte nye EHDS-rettigheter.

| Aspekt | Alt. 1 | Alt. 2 | Alt. 3 |
|--------|--------|--------|--------|
| Innbyggerrettigheter | Tilgangsbegrensning, nedlasting i EEHRxF, opt-out | Samme + native FHIR-basert innsyn | Samme + nordisk harmonisering |
| Nedlasting av EEHRxF | Via gateway-konvertering | Direkte fra FHIR-kilde | Via gateway eller direkte |
| Opt-out-mekanisme | Ny funksjonalitet | Ny funksjonalitet (FHIR Consent) | Koordinert nordisk tilnærming |
| Grensekryssende innsyn | Ny funksjonalitet via MyHealth@EU | Ny funksjonalitet via MyHealth@EU | Ny funksjonalitet via MyHealth@EU |

**Vurdering:** Helsenorge.no krever ny funksjonalitet uavhengig av alternativ: nedlasting av helseopplysninger i EEHRxF, mekanisme for tilgangsbegrensning overfor helsepersonell, og opt-out fra sekundærbruk. Forskjellen mellom alternativene er primært i backend: i alternativ 1 henter helsenorge.no data via gateway i EEHRxF-format, i alternativ 2 hentes data direkte fra FHIR-kilder.

### 5.4 EPJ-systemer – påvirkning og tilpasningsbehov

EPJ-systemene er det mest heterogene og risikofylte området for alle tre alternativer.

| EPJ-system | Markedsandel | FHIR-modenhet | Alt. 1 | Alt. 2 | Alt. 3 |
|------------|-------------|---------------|--------|--------|--------|
| DIPS Arena | ~73% HF | Middels-Hoy (Open DIPS FHIR) | Minimal endring nasjonalt, gateway-konvertering | Full FHIR-migrering, bygge på eksisterende API | Koordinert med nordiske DIPS-kunder |
| Epic/Helseplattformen | Helse Midt-Norge | Middels (Epic FHIR R4) | Gateway-konvertering fra Epic-format | Epic har FHIR, men proprietær modell | Begrenset nordisk relevans (kun Norge) |
| CGM | Primærhelsetjeneste | Lav | Gateway-konvertering | Full FHIR-implementering | Koordinert med nordiske CGM-kunder |
| Visma | Kommunal omsorg | Lav | Gateway-konvertering | Full FHIR-implementering | Koordinert med nordiske Visma-kunder |
| Infodoc | Fastleger | Lav | Gateway-konvertering | Full FHIR-implementering | Begrenset nordisk relevans |

**Vurdering:**

**DIPS Arena** er best posisjonert for FHIR-overgang med eksisterende FHIR-API-er og openEHR-basert arkitektur. DIPS opererer også i Danmark, noe som gir nordisk synergi.

**Epic/Helseplattformen** er en særskilt utfordring. Epic har FHIR R4-støtte, men Epics integrasjonsmodell er proprietær og styrt fra leverandørens side. I alternativ 1 kan Helseplattformen levere data til gateway i sitt format. I alternativ 2 må Epic/Helseplattformen tilpasse seg norske FHIR-profiler, noe som krever forhandling med Epic (USA-basert leverandør).

**Primærhelsetjenesten** (CGM, Visma, Infodoc) har lavest FHIR-modenhet og flest installasjoner. I alternativ 1 skjermes disse i stor grad fra EHDS-krav. I alternativ 2 må alle implementere FHIR, noe som er den mest krevende overgangen i hele sektoren.

### 5.5 Nye komponenter (NCP, HDAB, sikre analyserom)

| Ny komponent | Formål | Alle alternativer | Alt. 3 tilleggsverdi |
|--------------|--------|-------------------|---------------------|
| **NCPeH (National Contact Point for eHealth)** | Gateway til MyHealth@EU | Må etableres. NHN har piloterfaring. Bygger på OpenNCP-programvare. | Nordisk erfaringsdeling om NCPeH-implementering |
| **HDAB (Health Data Access Body)** | Administrere sekundærbruk-tilgang | Må etableres. Bygge på helsedata.no-infrastruktur. Vurdere søknader, utstede datatillatelser, føre tilsyn med SPE. | Nordisk harmonisering av søknadsprosesser |
| **Sikre analyserom (SPE)** | Trygge miljøer for sekundærbruksanalyse | Må etableres. SPUHiN-prosjektet gir grunnlag. Krever sertifisering etter EHDS-krav. | Nordisk deling av SPE-infrastruktur eller krav |
| **Nasjonal testinfrastruktur** | Obligatorisk testing av EHR-systemer | Må etableres. Testmiljø for EEHRxF-konformitet. | Delt nordisk testinfrastruktur |
| **Terminologitjeneste** | Mapping mellom kodeverk | Sentral nasjonal tjeneste for SNOMED CT, LOINC, ATC-mapping. | Delt nordisk terminologiplattform |

**Vurdering:** De nye komponentene må etableres uavhengig av alternativ. Forskjellen er omfanget: i alternativ 1 er de begrenset til grensekryssende bruk, i alternativ 2 er de nasjonale kjernekomponenter, og i alternativ 3 kan de deles med nordiske naboer. Alternativ 3 gir størst kostnadsbesparelse for nye komponenter fordi utviklingskostnadene kan deles.

---

## 6. Anbefaling fra arkitekturperspektiv

### Samlet arkitekturvurdering

| Kvalitetsdimensjon | Alt. 1 | Alt. 2 | Alt. 3 |
|-------------------|--------|--------|--------|
| Interoperabilitet | 2/5 | 5/5 | 3/5 |
| Teknisk gjeld | 1/5 | 4/5 | 2/5 |
| Vendor lock-in | 2/5 | 4/5 | 3/5 |
| Skalerbarhet | 2/5 | 4/5 | 3/5 |
| Sikkerhet by design | 3/5 | 4/5 | 3/5 |
| **Gjennomsnitt** | **2.0** | **4.2** | **2.8** |

*(1 = dårlig, 5 = utmerket)*

### Anbefaling

Fra et rent arkitekturperspektiv gir **alternativ 2 (Akselerert helhetlig)** klart best arkitekturkvalitet over tid. Det er det eneste alternativet som:

1. Eliminerer doble standarder og varig teknisk gjeld
2. Gir reell nasjonal interoperabilitet som bivirkning av EHDS-implementeringen
3. Reduserer vendor lock-in gjennom standardiserte, åpne API-er
4. Skalerer naturlig til nye datakategorier
5. Bruker FHIR-standardens innebygde sikkerhets- og samtykkemekanismer

**Men:** Arkitekturkvalitet er bare én dimensjon. Alternativ 2 har høyest gjennomføringskompleksitet, høyest kostnad og størst endringsmotstand. En pragmatisk tilnærming er:

**Anbefalt hybridstrategi:**

1. **Start med alternativ 1 for de første fristene** (gruppe 1, mars 2029): Etabler gateway for pasientoppsummeringer og e-resept. Bruk kjernejournals eksisterende FHIR-API-er og reseptformidlerens MyHealth@EU-pilot som fundament.

2. **Sett alternativ 2 som strategisk mål fra dag én**: Publiser en nasjonal FHIR-overgangsplan (roadmap). Krev at alle nye integrasjoner bruker FHIR. Sett krav til EPJ-leverandører om FHIR-støtte i anskaffelsesavtaler.

3. **Unngå at gateway sementeres**: Design gateway-laget eksplisitt som midlertidig. Bygg det modulært slik at det kan fases ut komponent for komponent etter hvert som kildene blir FHIR-native.

4. **Forfølg alternativ 3 parallelt**: Nordisk samarbeid om terminologitjenester, testinfrastruktur og FHIR-basisprofiler gir verdi uavhengig av nasjonal tilnærming. Koordinert leverandørdialog med DIPS, CGM og Visma er pragmatisk fordi disse opererer i flere nordiske markeder.

5. **Prioriter Epic/Helseplattformen-dialogen tidlig**: Helseplattformen representerer den største arkitekturrisikooen uavhengig av alternativ. Avklar tidlig hvordan Epic-plattformen skal integreres med norske FDS-krav og FHIR-profiler.

### Kritisk suksessfaktor

Den viktigste arkitekturbeslutningen er **ikke valget mellom alternativ 1, 2 eller 3**, men om gateway-laget i alternativ 1 designes som **midlertidig bro** eller **permanent infrastruktur**. Hvis det blir permanent, akkumulerer Norge teknisk gjeld som blir stadig dyrere å håndtere. Hvis det designes som midlertidig med en tydelig utfasingsplan, kan det fungere som et pragmatisk steg mot alternativ 2.

---

## Kilder

### Prosjektinterne rapporter
- `rapporter/kunnskapsgrunnlag-ehds.md` – Kunnskapsgrunnlag for EHDS-utredning
- `rapporter/problemdefinisjon-ehds.md` – Problemdefinisjon med gap-analyse
- `rapporter/tiltaksalternativer-ehds.md` – Beskrivelse av tiltaksalternativer

### Norske kilder
- [Helsedirektoratets EHDS konsekvensvurdering – Gapanalyse pr. 11. april 2025](https://www.helsedirektoratet.no/rapporter/ehds-konsekvensvurdering--gapanalyse-pr.11.april-2025)
- [NHN Utviklerportal – Kjernejournal FHIR API](https://utviklerportal.nhn.no/informasjonstjenester/kjernejournal/kritisk-informasjon/kritisk-info-fhir-api/)
- [Open DIPS – FHIR-dokumentasjon](https://open.dips.no/docs/fhir)
- [HL7 Norway – Nasjonale FHIR-profiler](https://simplifier.net/organization/hl7norway)
- [HL7 Norway FHIR Hackathon 2025](https://hl7norway.github.io/FHIR-hackathon-2025/currentbuild/index.html)
- [MyHealth@EU – Norsk helsenett](https://www.nhn.no/tjenester/myhealth)

### Nordiske kilder
- [FHIR Base Profiles in the Nordics – Vitalis 2025](https://invitepeople.com/public/events/bd0a6002b4/seminars/de0ea39774)
- [Nordic Health Information Partnership](https://fhir.fi/en/demo2025/nhip/)
- [DK Core FHIR Implementation Guide v3.5.0](https://hl7.dk/fhir/core/)
- [HL7 Finland – FHIR Demo 2025](https://fhir.fi/en/demo2025/hl7-finland/)
- [Cross-border eP and PS in the Nordic countries – E-halsomyndigheten](https://www.ehalsomyndigheten.se/globalassets/ehm/3_om-oss/rapporter/cross-border-ep-and-ps-in-the-nordic-countries.pdf)

### Europeiske kilder
- [Frontiers: Challenges of national health data ecosystems – Italian example](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1644719/full)
- [Frontiers: Interoperability using FHIR Mapping Language – CDA to FHIR](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2024.1480600/full)
- [EHDS infrastructure: platforms powering EU health data](https://www.better.care/blog-en/ehds-infrastructure-platforms/)
- [HL7 Europe publishes new FHIR implementation guides for the EHDS](https://medium.com/digital-health-brief/hl7-europe-publishes-new-fhir-implementation-guides-for-the-ehds-61baceae06b4)
- [EU-kommisjonen – Electronic cross-border health services](https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en)

---

*Denne rapporten er utarbeidet 15. mars 2026 som del av Helsedirektoratets arkitekturvurdering for EHDS-implementering i Norge. Rapporten bygger på kunnskapsgrunnlaget, problemdefinisjonen og tiltaksalternativene, supplert med websøk om nordiske FHIR-implementeringserfaringer og europeiske arkitekturtilnærminger. Vurderingene bør revideres når gjennomføringsrettsakter vedtas og mer detaljert teknisk informasjon fra leverandører foreligger.*
