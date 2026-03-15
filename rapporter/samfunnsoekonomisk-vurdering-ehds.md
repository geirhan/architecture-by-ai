# Samfunnsøkonomisk vurdering: EHDS-implementering i Norge

## Sammendrag

Denne rapporten gir en forenklet samfunnsøkonomisk vurdering av tiltaksalternativene for implementering av EHDS-forordningen (EU 2025/327) i Norge, strukturert etter DFØs 8-trinnsmodell for samfunnsøkonomiske analyser. Vurderingen dekker nullalternativet og tre tiltaksalternativer: (1) stegvis minimum, (2) akselerert helhetlig implementering, og (3) nordisk samarbeid.

**Hovedfunn:**

- **Nullalternativet er ikke reelt** ved EØS-innlemmelse, men tjener som referansepunkt. Kostnadene ved manglende etterlevelse (EØS-rettslige sanksjoner, tapt forskningstilgang, manglende pasientrettigheter) overstiger sannsynligvis kostnadene ved alle tiltaksalternativene.
- **Alternativ 2 (akselerert helhetlig)** vurderes som det mest samfunnsøkonomisk lønnsomme alternativet over en 15-årsperiode, til tross for høyere investeringskostnader, fordi det gir størst nasjonal nytteverdi og unngår teknisk gjeld fra doble standarder.
- **Alternativ 1 (stegvis minimum)** har lavest kortsiktig investeringskostnad, men skaper betydelige merkostnader over tid gjennom parallelle standarder og begrenset nasjonal effekt.
- **Alternativ 3 (nordisk samarbeid)** er en verdifull tilleggsdimensjon som kan redusere kostnader uavhengig av valgt hovedalternativ, men er ikke et selvstendig alternativ.
- **Usikkerheten er svært høy** på grunn av uavklarte gjennomføringsrettsakter, usikkert EØS-innlemmelsestidspunkt og manglende detaljerte kostnadsestimater fra sektoren.

Analysen er gjennomført på et overordnet nivå (forhåndsanalyse/forenklet analyse) i tråd med DFØs veileder, gitt det tidlige stadiet i utredningen og den store usikkerheten om sentrale parametere. En fullverdig samfunnsøkonomisk analyse bør gjennomføres når gjennomføringsrettsaktene er vedtatt og mer presise kostnadsestimater foreligger.

---

## 1. Problemdefinisjon og mål

### Problemet

Norsk helsesektor er ikke i stand til å oppfylle kravene EHDS stiller til deling av helsedata, verken nasjonalt på tvers av virksomheter eller internasjonalt på tvers av landegrenser. Problemet er strukturelt og sammensatt, med fire gjensidig forsterkende dimensjoner:

1. **Rettslige gap**: Gjeldende norsk helselovgivning mangler hjemler for grensekryssende deling, harmoniserte innbyggerrettigheter og rammeverk for sekundærbruk.
2. **Tekniske gap**: Norske EHR-systemer bruker nasjonale meldingsstandarder som ikke er kompatible med EEHRxF (HL7 FHIR). Infrastruktur for MyHealth@EU og HealthData@EU er ikke operativ.
3. **Organisatoriske gap**: Norge mangler digital helsemyndighet og HDAB som forordningen krever. Ansvarsfordelingen mellom Helsedirektoratet, NHN og andre aktører er ikke tilpasset.
4. **Semantiske gap**: Ulike kodeverk, terminologier og registreringspraksis gjør at data ikke betyr det samme på tvers av systemer.

### Mål

Norge skal oppfylle forpliktelsene i EHDS-forordningen innenfor fastsatte tidsfrister (gruppe 1: mars 2029, gruppe 2: mars 2031), slik at norske innbyggere, helsepersonell og forskere kan dra nytte av sikker og effektiv deling av helseopplysninger.

*For utfyllende problemanalyse, se rapporter/problemdefinisjon-ehds.md.*

---

## 2. Identifisering av tiltak

Fire alternativer er definert og beskrevet i detalj i rapporter/tiltaksalternativer-ehds.md:

| Alternativ | Kort beskrivelse | Ambisjonsnivå |
|-----------|------------------|---------------|
| **Nullalternativet** | Videreføring uten nye EHDS-tiltak | Ingen |
| **Alt. 1: Stegvis minimum** | Kun minimumskrav, føderert gateway, nasjonale standarder beholdes | Minimum etterlevelse |
| **Alt. 2: Akselerert helhetlig** | FHIR som nasjonal standard, bredere modernisering, nasjonalt program | Bredere modernisering |
| **Alt. 3: Nordisk samarbeid** | Delte komponenter og koordinering med nordiske land | Tilleggsdimensjon |

Alternativ 3 er i praksis en samarbeidstilnærming som kan kombineres med enten alternativ 1 eller 2, og vurderes derfor som et supplement. I den samlede vurderingen behandles det som et tilleggsvalg.

---

## 3. Identifisering av virkninger

### 3.1 Prissatte virkninger (kostnadssiden)

Kostnadene er gruppert i hovedkategorier med kvalitativ angivelse av størrelsesorden per alternativ. Estimatene er basert på erfaringstall fra norske e-helseprosjekter, EU-kommisjonens konsekvensutredning (SWD(2022) 131) og Helsedirektoratets gapanalyse.

**Referansepunkter for kostnadsnivå:**
- EU-kommisjonens konsekvensutredning anslo samlede kostnader for EHDS-implementering i EU til EUR 351–743 millioner, med forventede besparelser på EUR 11 milliarder over ti år (kilde: EU-kommisjonen, SWD(2022) 131).
- Helseplattformen i Midt-Norge har hatt samlede kostnader på ca. 6,7 mrd. kroner per oktober 2024 (kilde: Riksrevisjonen). «Én innbygger – én journal» ble estimert til 22 mrd. kroner totalt (kilde: Helsedirektoratet).
- EU-kommisjonens estimat for etablering av HDAB-infrastruktur er ca. EUR 10,6 millioner i etableringskostnad og EUR 0,6 millioner i årlig vedlikehold per land, men dette forutsetter at kostnaden deles med andre dataområder (kilde: SWD(2022) 131).
- De regionale helseforetakene bruker allerede betydelige summer på IKT – Helse Vest rapporterte 482 mill. kr i årlige IKT-kostnader i 2024 for fem sentrale systemer alene (kilde: Helse Vest styresak).

#### Kostnadskategorier per alternativ

| Kostnadskategori | Null | Alt. 1 | Alt. 2 | Alt. 3 (tillegg) |
|-----------------|------|--------|--------|-------------------|
| **Systemutvikling og integrasjon** | | | | |
| - EEHRxF gateway/konvertering | 0 | Middels | Lav (innlemmes i FHIR-overgang) | Mulig deling |
| - Nasjonal FHIR-infrastruktur | 0 | Lav | Høy | Mulig deling |
| - MyHealth@EU tilkobling | Lav (kun pilot) | Middels | Middels | Mulig deling |
| - HealthData@EU tilkobling | Lav (kun pilot) | Middels | Middels | Mulig deling |
| - Testinfrastruktur | 0 | Middels | Høy | Mulig deling |
| - Leverandørtilpasning (EHR-systemer) | 0 | Høy | Svært høy | Stordriftsfordel |
| **Forvaltningsstruktur** | | | | |
| - Digital helsemyndighet | 0 | Middels | Høy | Koordineringskostnad |
| - HDAB etablering og drift | 0 | Middels | Høy | Mulig deling |
| - Sertifiserings- og tilsynsapparat | 0 | Middels | Høy | Felles spesifikasjoner |
| **Rettslige tilpasninger** | | | | |
| - Lovendringer og juridisk arbeid | 0 | Middels | Middels–Høy | Koordinert tolkning |
| **Opplæring og kompetanse** | | | | |
| - FHIR/EEHRxF-kompetanse | 0 | Middels | Høy | Felles program |
| - Endringsledelse i sektoren | 0 | Middels | Høy | Erfaringsdeling |
| **Løpende driftskostnader** | | | | |
| - Doble standarder (nasjonale + EEHRxF) | 0 | Høy (over tid) | Lav (konsolidert) | Lav–Middels |
| - Forvaltning av nye systemer | 0 | Middels | Middels–Høy | Deling mulig |

#### Indikative kostnadsintervaller (svært usikre)

Basert på tilgjengelige referansepunkter anslås følgende grove størrelsesordener for samlede investeringskostnader over implementeringsperioden (2026–2031):

| Alternativ | Investeringskostnad (mrd. NOK) | Årlig merkostnad drift (mill. NOK) |
|-----------|-------------------------------|-----------------------------------|
| Nullalternativet | 0 (men kostnader ved sanksjoner/tap) | 0 |
| Alt. 1: Stegvis minimum | 3–6 | 300–600 (doble standarder) |
| Alt. 2: Akselerert helhetlig | 6–12 | 200–400 (konsolidert) |
| Alt. 3: Nordisk samarbeid (tillegg) | +0,2–0,5 (koordinering) | +50–100 (koordinering), men besparelse 10–25 % på delte komponenter |

**Viktig forbehold:** Disse intervallene er grove estimater basert på begrenset datagrunnlag. De faktiske kostnadene kan avvike vesentlig. Erfaringer fra store norske e-helseprosjekter (Helseplattformen, Én innbygger – én journal) viser at kostnadsoverskridelser er vanlige. EU-kommisjonens estimater fra konsekvensutredningen er basert på gjennomsnitt for alle medlemsland og tar ikke hensyn til norske særforhold.

### 3.2 Ikke-prissatte kvantifiserbare virkninger (nyttesiden)

Disse virkningene kan i prinsippet kvantifiseres, men det foreligger ikke tilstrekkelig datagrunnlag for å prissette dem pålitelig.

| Virkning | Indikator | Null | Alt. 1 | Alt. 2 | Alt. 3 |
|----------|-----------|------|--------|--------|--------|
| **Reduserte dobbeltundersøkelser** | Antall unødvendige undersøkelser unngått per år | 0 | Lav (kun grensekryssende) | Middels (nasjonalt + grensekryssende) | Lav–Middels |
| **Tidsbesparelser for helsepersonell** | Timer spart på informasjonsinnhenting per år | 0 | Lav | Middels–Høy | Lav–Middels |
| **Raskere forskningstilgang** | Gjennomsnittlig tid fra søknad til datatilgang | 0 | Middels forbedring | Høy forbedring | Middels–Høy forbedring |
| **Reduserte medisinske feil** | Antall unngåtte feil ved grensekryssende behandling | 0 | Middels | Middels–Høy | Middels |
| **Økt bruk av e-resept grensekryssende** | Antall grensekryssende e-resepter per år | 0 | Middels | Middels | Middels |
| **Redusert tid til legemiddelutvikling** | Måneder spart per klinisk studie | 0 | Lav | Middels | Middels |

**EU-kommisjonens estimat for nyttevirkninger:** EUR 5,4 mrd. fra optimalisert bruk av helsedata til forskning og innovasjon, og EUR 5,5 mrd. fra bedre tilgang og utveksling av helsedata i helsetjenesten, samlet EUR 11 mrd. over ti år for hele EU (kilde: SWD(2022) 131). Norges andel kan grovt anslås til 1–2 % basert på befolkningsandel, dvs. EUR 110–220 mill. (ca. 1,2–2,5 mrd. NOK over ti år). Sykehus kan oppnå opptil 15 % besparelser ved bedre bruk av eksisterende helseinformasjon (kilde: EU-kommisjonen).

### 3.3 Ikke-kvantifiserbare virkninger

Disse virkningene er viktige for den samlede vurderingen, men lar seg verken kvantifisere eller prissette på en meningsfull måte.

**Positive virkninger:**

| Virkning | Beskrivelse | Relevans per alternativ |
|----------|------------|------------------------|
| **Styrket pasientmedvirkning** | Pasienter får bedre kontroll over egne helsedata, inkludert rett til tilgang, nedlasting og tilgangsbegrensning | Alle tiltaksalternativer, størst i alt. 2 |
| **Bedre forskningsdata** | Standardiserte, høykvalitets helsedata gir bedre grunnlag for medisinsk forskning, folkehelse og legemiddelutvikling | Alle, størst i alt. 2 |
| **Økt tillit til helsesystemet** | Transparens og kontroll kan styrke innbyggernes tillit til digital helsedatahåndtering | Alle, forutsatt god gjennomføring |
| **Innovasjon og næringsutvikling** | Tilgang til helsedata kan stimulere utvikling av nye helseteknologiløsninger og tjenester | Størst i alt. 2 og 3 |
| **Norsk konkurranseposisjon i forskning** | Norske forskere får tilgang til europeisk datamaterialevia HealthData@EU | Alle tiltaksalternativer |
| **Harmonisering med europeiske standarder** | Reduserer fragmentering og letter samarbeid med europeiske partnere | Størst i alt. 2 |
| **Forbedret beredskap** | Bedre datatilgang kan styrke beredskapsevnen ved fremtidige pandemier/helsekriser | Alle, størst i alt. 2 |

**Negative virkninger / risikoer:**

| Virkning | Beskrivelse | Relevans per alternativ |
|----------|------------|------------------------|
| **Personvernrisiko** | Økt deling av sensitive helsedata på tvers av landegrenser medfører nye risikoer | Alle, håndteres ulikt |
| **Endringsmotstand** | Omstilling av arbeidsprosesser, systemer og standarder møter motstand fra helsepersonell og leverandører | Størst i alt. 2 |
| **Avhengighet av EU-prosesser** | Norge blir avhengig av EU-kommisjonens tidsplan for gjennomføringsrettsakter | Alle |
| **Tap av nasjonal fleksibilitet** | Forordningen begrenser nasjonalt handlingsrom for helsedata-regulering | Alle |
| **Kompetansekonkurranse** | Stor etterspørsel etter FHIR- og interoperabilitetskompetanse kan drive opp lønnskostnader og skape kapasitetsutfordringer | Størst i alt. 2 |
| **Implementeringsrisiko** | Store IT-prosjekter i offentlig sektor har historisk høy risiko for forsinkelser og kostnadsoverskridelser (jf. Helseplattformen) | Størst i alt. 2 |

---

## 4. Tallfesting og verdsetting

Gitt den store usikkerheten gjennomføres tallfesting og verdsetting som en kvalitativ vurdering av størrelsesorden. Følgende kategorier benyttes:

| Kategori | Størrelsesorden |
|----------|----------------|
| Lav | Under 500 mill. NOK (investering) / under 50 mill. NOK (årlig drift) |
| Middels | 500 mill. – 2 mrd. NOK (investering) / 50–200 mill. NOK (årlig drift) |
| Høy | 2–6 mrd. NOK (investering) / 200–500 mill. NOK (årlig drift) |
| Svært høy | Over 6 mrd. NOK (investering) / over 500 mill. NOK (årlig drift) |

### Samlet kostnadsvurdering per alternativ

| Dimensjon | Null | Alt. 1 | Alt. 2 | Alt. 3 (tillegg) |
|-----------|------|--------|--------|-------------------|
| Investeringskostnad | Lav | Høy (3–6 mrd.) | Svært høy (6–12 mrd.) | Lav–Middels (+0,2–0,5 mrd.) |
| Årlig driftskostnad (merkostnad) | Lav | Høy (doble standarder) | Middels (konsolidert) | Lav |
| Totalkostnad over 15 år (NPV) | Lav direkte, men høy alternativkostnad | Svært høy | Svært høy | Middels (tillegg) |

### Samlet nyttevurdering per alternativ

| Dimensjon | Null | Alt. 1 | Alt. 2 | Alt. 3 (tillegg) |
|-----------|------|--------|--------|-------------------|
| Nasjonal interoperabilitet | Ingen | Lav | Svært høy | Middels |
| Grensekryssende datadeling | Ingen | Middels | Høy | Middels–Høy |
| Forskningstilgang | Ingen | Middels | Høy | Middels–Høy |
| Pasientrettigheter | Ingen | Middels | Høy | Middels |
| Effektivisering av helsetjenesten | Ingen | Lav | Høy | Middels |
| Innovasjon og næringsutvikling | Ingen | Lav | Middels–Høy | Middels |

### Netto nyttevurdering

| Alternativ | Kostnader | Nytte | Netto vurdering |
|-----------|-----------|-------|-----------------|
| Nullalternativet | Lav direkte, men EØS-sanksjoner og tapte muligheter | Ingen | Negativ (ikke reelt) |
| Alt. 1 | Høy (økende over tid pga. doble standarder) | Middels (primært grensekryssende) | Svakt positiv kortsiktig, usikker langsiktig |
| Alt. 2 | Svært høy initialt, men avtagende over tid | Høy–Svært høy (nasjonal + grensekryssende) | Positiv langsiktig, men høy gjennomføringsrisiko |
| Alt. 3 (tillegg) | Lav–Middels merkostnad | Middels tilleggsnytte | Positiv (kostnadseffektivt supplement) |

---

## 5. Vurdering av usikkerhet

### Hva er mest usikkert?

Usikkerheten i denne vurderingen er **svært høy**. Følgende parametere er mest usikre og har størst betydning for konklusjonen:

| Usikkerhetsfaktor | Vurdering | Konsekvens for analysen |
|-------------------|-----------|------------------------|
| **Gjennomføringsrettsakter fra EU** | Mange sentrale spesifikasjoner skal vedtas mars 2025 – mars 2027. Innholdet er ukjent. | Kan endre omfanget av kravene vesentlig. Kan gjøre alt. 1 mer eller mindre krevende |
| **Tidspunkt for EØS-innlemmelse** | Avhenger av politisk prosess i EØS-komiteen og Stortinget | Påvirker alle tidsfrister og dermed kostnadsprofilen |
| **Leverandørenes kapasitet og kostnader** | Ukjent hvor mange systemer som berøres og hva tilpasningene vil koste | Leverandørkostnader kan utgjøre den største enkeltkostnaden |
| **Kommunesektorens beredskap** | Over 350 kommuner med svært ulik modenhet | Kan kreve langt større investeringer enn antatt |
| **Faktisk realisering av nyttevirkninger** | Basert på EU-estimater, ikke norske erfaringstall | Nyttevirkningene kan bli vesentlig lavere enn anslått |
| **Erfaringer fra Helseplattformen** | Viser at store e-helseprosjekter har høy risiko for kostnadsoverskridelser og forsinkelser | Tilsier et konservativt kostnadsestimat, særlig for alt. 2 |
| **Teknologisk utvikling** | Rask utvikling innen AI, FHIR og helsedata kan endre forutsetningene | Kan både redusere og øke kostnader |

### Sensitivitetsanalyse (kvalitativ)

**Scenario 1: Gjennomføringsrettsaktene krever mer enn antatt**
- Alt. 1 blir dyrere fordi gateway-tilnærmingen ikke er tilstrekkelig
- Alt. 2 påvirkes mindre fordi bredere tilnærming gir mer fleksibilitet
- Konklusjon: Styrker alt. 2 relativt til alt. 1

**Scenario 2: Leverandørkostnadene dobles**
- Alle alternativer blir vesentlig dyrere
- Alt. 2 rammes hardest i absolutte tall, men alt. 1 rammes også fordi leverandørtilpasning er uunngåelig
- Konklusjon: Øker risikoen for alle alternativer, men endrer ikke rangeringen vesentlig

**Scenario 3: Kommunesektoren krever 50 % mer enn antatt**
- Øker kostnadene for alle alternativer
- Alt. 2 rammes mer fordi ambisjonsnivået er høyere
- Konklusjon: Kan gjøre alt. 1 mer attraktivt kortsiktig

**Scenario 4: Nyttevirkningene blir 50 % lavere enn antatt**
- Alt. 2s fordel over alt. 1 reduseres
- Alt. 1 kan bli foretrukket dersom nyttevirkningene primært er grensekryssende
- Konklusjon: Styrker argumentet for en stegvis tilnærming

**Scenario 5: EØS-innlemmelse forsinkes med 2 år**
- Alle alternativer får mer tid til forberedelse
- Kan gi tid til å starte med alt. 1 og gradvis bevege seg mot alt. 2
- Konklusjon: Styrker argumentet for en pragmatisk mellomvei

---

## 6. Samlet vurdering

### Sammenstilling av virkninger per alternativ

| Vurderingskriterium | Null | Alt. 1 | Alt. 2 | Alt. 3 (tillegg) |
|---------------------|------|--------|--------|-------------------|
| Samfunnsøkonomisk lønnsomhet (langsiktig) | Svært negativ | Svakt positiv | Positiv | Positiv (supplement) |
| Gjennomførbarhet | N/A | Middels–Høy | Middels | Middels (avhenger av partnere) |
| Risiko for kostnadsoverskridelse | Lav | Middels | Høy | Middels |
| EØS-rettslig etterlevelse | Ikke oppfylt | Oppfylt | Oppfylt | Oppfylt (med hovedalternativ) |
| Nasjonal nytteverdi utover EHDS | Ingen | Lav | Høy | Middels |
| Fleksibilitet/tilpasningsevne | Lav | Middels | Middels–Høy | Høy |
| Fordelingsvirkninger | Skjev (tap for alle) | Akseptable | Gode, men omfordelende | Gode |

### Kvalitativ rangering

1. **Alternativ 2 + 3** (akselerert helhetlig med nordisk samarbeid): Høyest samfunnsøkonomisk lønnsomhet over 15 år, men krever politisk vilje til store investeringer og aksept for høy gjennomføringsrisiko.

2. **Alternativ 1 + 3** (stegvis minimum med nordisk samarbeid): Lavere risiko og mer gjennomførbart, men lavere langsiktig nytteverdi og risiko for teknisk gjeld som øker totalkostnaden over tid.

3. **Alternativ 1 alene**: Oppfyller minimumskravene, men gir begrenset nasjonal verdi og skaper doble standarder.

4. **Alternativ 2 alene**: Høyest potensial, men mangler stordriftsfordelene fra nordisk samarbeid.

5. **Nullalternativet**: Ikke reelt ved EØS-innlemmelse.

---

## 7. Fordelingsvirkninger

### Hvem bærer kostnadene?

| Aktør | Type kostnad | Størrelsesorden | Merknader |
|-------|-------------|-----------------|-----------|
| **Staten (HOD/Helsedirektoratet/NHN)** | Nasjonal infrastruktur, forvaltningsstruktur, lovendringer, koordinering | Høy–Svært høy | Hoveddelen av investeringskostnadene |
| **Regionale helseforetak** | Tilpasning av systemer, endrede arbeidsprosesser, opplæring | Høy | Fire RHF-er med ulik utgangspunkt (Helse Midt-Norge har Helseplattformen) |
| **Kommuner** | Tilpasning av systemer, opplæring, endret praksis | Middels–Høy samlet | Svært ulikt fordelt – store kommuner har mer kapasitet enn små |
| **EPJ-leverandører** | Systemtilpasning, sertifisering, testing | Høy | Vil i praksis videreføres til kundene gjennom høyere lisens-/utviklingskostnader |
| **Private helseaktører** | Systemtilpasning, opplæring | Middels | Ulik kapasitet og betalingsevne |
| **Pasienter (indirekte)** | Tilpasning til nye rettigheter/systemer, personvernrisiko | Lav | Primært omstillingskostnader |

### Hvem får nytten?

| Aktør | Type nytte | Størrelsesorden |
|-------|-----------|-----------------|
| **Pasienter/innbyggere** | Bedre tilgang til egne data, sikrere grensekryssende behandling, økt kontroll | Middels–Høy |
| **Helsepersonell** | Bedre informasjonstilgang, redusert dobbeltarbeid, færre medisinske feil | Middels–Høy (størst i alt. 2) |
| **Forskere og akademia** | Bedre datatilgang via HDAB, europeisk samarbeid, raskere forskning | Høy |
| **Legemiddelindustri og helseteknologi** | Raskere utvikling, bedre data, nye markeder | Middels–Høy |
| **Samfunnet generelt** | Bedre folkehelse, beredskap, innovasjon | Middels (langsiktig) |

### Geografisk fordeling

| Dimensjon | Vurdering |
|-----------|-----------|
| **By vs. distrikt** | Distrikter med færre helseressurser kan ha størst nytte av bedre informasjonstilgang, men bærer også relativt sett høyere omstillingskostnader. Små kommuner med begrenset IKT-kapasitet kan oppleve uforholdsmessig store kostnader. |
| **Kommuner vs. helseforetak** | Helseforetakene har generelt større IKT-kapasitet og kan håndtere omstillingen bedre. Kommunene er mer sårbare, særlig de minste. KS' rolle som koordinator blir avgjørende. |
| **Regionale forskjeller** | Helse Midt-Norge (med Helseplattformen/Epic) har en annen utgangssituasjon enn de øvrige regionene. Tilpasningskostnadene kan variere betydelig mellom regionene. |
| **Grensekryssende dimensjon** | Nordlige og sørlige grenseregioner (med henholdsvis svensk/finsk og dansk tilknytning) kan ha særlig nytte av grensekryssende datautveksling. Områder med mange turister (fjordregioner, Nordkapp) berøres også. |

### Omfordelingsvirkninger

EHDS-implementeringen innebærer en omfordeling der:
- **Kostnadene primært bæres av det offentlige og leverandørene**, som i sin tur finansieres av skatteinntekter og økte priser.
- **Nytten er bredere fordelt**, men kommer i størst grad pasienter, forskere og innovasjonsmiljøer til gode.
- **Det er en risiko for at små kommuner og mindre leverandører rammes uforholdsmessig** dersom det ikke etableres støtteordninger og overgangsmekanismer.

---

## 8. Anbefaling

### Anbefalt alternativ: Alternativ 2 (akselerert helhetlig) med elementer av alternativ 3 (nordisk samarbeid)

Basert på den samlede vurderingen anbefales alternativ 2 som det mest samfunnsøkonomisk lønnsomme alternativet over en 15-årsperiode, supplert med nordisk samarbeid (alternativ 3). Begrunnelsen er som følger:

**For alternativ 2:**
1. **Unngår teknisk gjeld.** Alternativ 1 skaper doble standarder (nasjonale meldingsstandarder + EEHRxF) som over tid kan koste mer enn den initielle besparelsen ved å velge minimum.
2. **Størst nasjonal nytteverdi.** FHIR som nasjonal standard gir interoperabilitetsgevinster som går langt utover det EHDS krever – bedre informasjonsflyt mellom norske virksomheter, bedre datakvalitet, redusert dobbeltarbeid.
3. **Samsvarer med eksisterende ambisjoner.** «Én innbygger – én journal»-visjonen og Nasjonal helse- og samhandlingsplan 2024–2027 peker allerede i denne retningen.
4. **Bedre posisjonert for fremtidige krav.** EHDS vil sannsynligvis utvides med nye kategorier og krav over tid. En helhetlig tilnærming gir bedre fundament.
5. **EU-estimater antyder positiv netto nytte.** EUR 11 mrd. i besparelser over ti år for EU indikerer at nyttevirkningene er betydelige, selv med konservative anslag for Norges andel.

**For nordisk samarbeid (alternativ 3):**
1. **Kostnadseffektivt supplement.** Deling av terminologitjenester, testinfrastruktur og kompetanseressurser kan gi 10–25 % besparelse på utvalgte komponenter.
2. **Stordriftsfordeler i leverandørdialogen.** Flere nordiske leverandører opererer i flere markeder, og koordinerte krav gir bedre forhandlingsposisjon.
3. **Erfaringsdeling reduserer risiko.** Læring fra land som starter implementeringen før Norge gir verdifull innsikt.

### Viktige forutsetninger for anbefalingen

Anbefalingen forutsetter at:
1. Det etableres en tydelig programorganisasjon med tilstrekkelig mandat og budsjett.
2. Det gis politisk forpliktelse til langsiktig finansiering (utover enkeltbudsjettår).
3. Kommunesektoren får tilstrekkelig støtte til omstillingen, inkludert finansiering og kompetansebistand.
4. Leverandørdialogen starter tidlig med tydelige signaler om krav og tidsfrister.
5. Det etableres en klar plan for gradvis utfasing av nasjonale meldingsstandarder, med tilstrekkelig overgangsperiode.
6. Nordisk samarbeid forankres politisk og organisatorisk, med realistiske forventninger til hva som kan deles.

### Alternativ anbefaling ved begrenset politisk vilje eller budsjett

Dersom det ikke er politisk vilje til investeringsnivået i alternativ 2, anbefales en **pragmatisk mellomvei**: Start med alternativ 1 for å møte de første fristene (gruppe 1: mars 2029), men med en bindende plan for overgang til alternativ 2 i perioden 2029–2033. Dette reduserer kortsiktig risiko, men øker totalkostnaden over tid og forutsetter at den politiske forpliktelsen til overgang opprettholdes over flere regjeringsperioder.

---

## Forholdsmessighet

### Vurdering av analysenivå

Denne vurderingen er gjennomført som en **forenklet samfunnsøkonomisk analyse** (forhåndsanalyse) i tråd med DFØs veileder. Følgende forhold begrunner det valgte analysenivået:

**Faktorer som tilsier grundigere analyse:**
- EHDS-implementeringen er et svært stort tiltak med samlede kostnader anslått til flere milliarder kroner.
- Tiltaket berører alle virksomheter i helse- og omsorgssektoren og millioner av innbyggere.
- Irreversibilitet: Valg av arkitektur og standarder er vanskelige å reversere.
- Fordelingsvirkningene er betydelige.

**Faktorer som begrenser analysenivået:**
- Gjennomføringsrettsaktene fra EU-kommisjonen er ikke vedtatt, noe som skaper fundamental usikkerhet om kravene.
- Tidspunktet for EØS-innlemmelse er uavklart.
- Det mangler detaljerte kostnadsestimater fra leverandører og helsevirksomheter.
- Helsedirektoratets egen gapanalyse (april 2025) gir kun overordnede vurderinger av kostnader.

**Anbefaling om videre analyse:**
En fullverdig samfunnsøkonomisk analyse (med prissatte nyttevirkninger, diskontering og beregning av netto nåverdi) bør gjennomføres når:
1. Gjennomføringsrettsaktene er vedtatt (forventet mars 2027)
2. EØS-innlemmelsestidspunktet er avklart
3. Detaljerte kostnadsestimater fra leverandører og virksomheter foreligger
4. Erfaringer fra tidlige implementeringer i EU-land er tilgjengelige

---

## Kilder

### Primærkilder for denne vurderingen

1. DFØ (2023/2025). *Veileder i samfunnsøkonomiske analyser*. Direktoratet for forvaltning og økonomistyring. [https://www.dfo.no/fagomrader/utredning-og-analyse-av-statlige-tiltak/samfunnsokonomiske-analyser/veileder-i-samfunnsokonomiske-analyser](https://www.dfo.no/fagomrader/utredning-og-analyse-av-statlige-tiltak/samfunnsokonomiske-analyser/veileder-i-samfunnsokonomiske-analyser)

2. EU-kommisjonen (2022). *Impact Assessment on the European Health Data Space, SWD(2022) 131*. [https://health.ec.europa.eu/publications/impact-assessment-european-health-data-space_en](https://health.ec.europa.eu/publications/impact-assessment-european-health-data-space_en)

3. EU-kommisjonen (2025). *European Health Data Space Regulation (EHDS)*. [https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)

4. Helsedirektoratet (2025). *EHDS konsekvensvurdering – Gapanalyse pr. 11. april 2025*. [https://www.helsedirektoratet.no/rapporter/ehds-konsekvensvurdering--gapanalyse-pr.11.april-2025](https://www.helsedirektoratet.no/rapporter/ehds-konsekvensvurdering--gapanalyse-pr.11.april-2025)

5. Regjeringen.no. *EØS-notat: Forordning om det europeiske helsedataområdet (EHDS)*. [https://www.regjeringen.no/no/sub/eos-notatbasen/notatene/2022/juni/forslag-til-forordning-om-det-europeiske-helsedataomradet-ehds/id3014792/](https://www.regjeringen.no/no/sub/eos-notatbasen/notatene/2022/juni/forslag-til-forordning-om-det-europeiske-helsedataomradet-ehds/id3014792/)

6. Regjeringen.no (2025). *Analyse av fordeler og ulemper ved Helseplattformen. Rapport 2025/38*. [https://www.regjeringen.no/no/dokumenter/analyse-av-fordeler-og-ulemper-ved-helseplattformen/id3143739/](https://www.regjeringen.no/no/dokumenter/analyse-av-fordeler-og-ulemper-ved-helseplattformen/id3143739/)

7. TEHDAS (2023). *Sustainability Plan for Secondary Use of Health Data in the European Health Data Space*. [https://tehdas.eu/app/uploads/2023/09/tehdas-sustainability-plan-for-ehds.pdf](https://tehdas.eu/app/uploads/2023/09/tehdas-sustainability-plan-for-ehds.pdf)

8. HaDEA (2025). *EU-funded projects contributing to the implementation of the European Health Data Space*. [https://hadea.ec.europa.eu/news/eu-funded-projects-contributing-implementation-european-health-data-space-2025-03-28_en](https://hadea.ec.europa.eu/news/eu-funded-projects-contributing-implementation-european-health-data-space-2025-03-28_en)

### Underlagsdokumenter fra dette prosjektet

9. Kunnskapsgrunnlag for EHDS (rapporter/kunnskapsgrunnlag-ehds.md)
10. Problemdefinisjon for EHDS-implementering (rapporter/problemdefinisjon-ehds.md)
11. Tiltaksalternativer for EHDS-implementering (rapporter/tiltaksalternativer-ehds.md)

### Referansepunkter for norske e-helseprosjekter

12. Helseplattformen AS. *Økonomien i Helseplattformen – fakta bak tallene*. [https://www.helseplattformen.no/om-oss/helseplattformen-i-media/nodvendig-fakta-om-helseplattformen/okonomien-i-helseplattformen/](https://www.helseplattformen.no/om-oss/helseplattformen-i-media/nodvendig-fakta-om-helseplattformen/okonomien-i-helseplattformen/)

13. Regjeringen.no. *Nasjonal helse- og samhandlingsplan 2024–2027*. [https://www.regjeringen.no/no/dokumenter/meld.-st.-9-20232024/id3027594/](https://www.regjeringen.no/no/dokumenter/meld.-st.-9-20232024/id3027594/)

---

*Denne rapporten er utarbeidet 15. mars 2026 som en forenklet samfunnsøkonomisk vurdering etter DFØs 8-trinnsmodell. Analysen er basert på offentlig tilgjengelige kilder og tidligere rapporter fra dette prosjektet. Rapporten bør oppdateres når gjennomføringsrettsakter fra EU-kommisjonen vedtas, EØS-innlemmelse avklares, og mer detaljerte kostnadsestimater foreligger.*
