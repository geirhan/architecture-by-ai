# Utredning: EHDS-forordningens konsekvenser for digitaliseringen i norsk helsesektor

*Utarbeidet for Helsedirektoratet, mars 2026*

---

## Ledersammendrag

**Hva er EHDS?** EHDS (forordning om det europeiske helsedataområdet, EU 2025/327) er en EU-forordning som skal gjøre det mulig å dele helseopplysninger trygt og effektivt mellom aktører i EU/EØS-land. Forordningen dekker to hovedområder: primærbruk (deling av helseopplysninger for behandling) og sekundærbruk (bruk av helsedata til forskning, innovasjon og folkehelse).

**Hvorfor er dette relevant for Norge?** Forordningen er vurdert som EØS-relevant og vil kreve lovendringer, ny forvaltningsstruktur og omfattende teknisk utvikling. Norsk helsesektor har utviklet seg med nasjonale standarder som ikke er kompatible med de felleseuropeiske kravene EHDS stiller. Utredningen har identifisert 21 gap fordelt på fire dimensjoner: rettslige (5), tekniske (6), organisatoriske (5) og semantiske (5).

**Hva er hovedutfordringene?** De fire grunnårsakene er: (1) historisk nasjonal utvikling uten europeisk harmonisering, (2) fragmentert informasjonslandskap med mange ulike systemer, (3) lovverk som ikke er tilpasset grensekryssende deling og (4) manglende forvaltningsstrukturer (digital helsemyndighet og tilgangsorgan for helsedata).

**Hva anbefales?** Utredningen anbefaler en hybridstrategi i tre faser:

- *Fase 1 (2026--2029):* Bruk en gateway-løsning for å oppfylle de første fristene for pasientoppsummeringer og e-resept. Design gateway-løsningen som midlertidig infrastruktur.
- *Fase 2 (2029--2031):* Start overgangen til HL7 FHIR som nasjonal standard. Implementer de neste datakategoriene (bilder, laboratoriesvar, epikriser) med FHIR-baserte grensesnitt.
- *Fase 3 (2031--2035):* Fullfør utfasingen av nasjonale meldingsstandarder. Norsk og europeisk interoperabilitet samles i én standard.

Nordisk samarbeid om delte komponenter og erfaringsdeling bør følges parallelt.

**Hva koster det?** Hybridstrategien anslås til 5--9 milliarder kroner i investeringskostnader over perioden 2026--2035. EU anslår besparelser på 11 milliarder euro for hele EU over ti år. Norges andel tilsvarer grovt 1,2--2,5 milliarder kroner. Usikkerheten i kostnadsestimatene er svært høy.

**Hva er de viktigste risikoene?**

1. Gateway-løsningen sementeres som permanent infrastruktur i stedet for midlertidig bro (risikonivå: høy).
2. Kostnadsoverskridelser i tråd med erfaringer fra Helseplattformen og andre store e-helseprosjekter (risikonivå: høy).
3. Forsinket EØS-innlemmelse gir kortere implementeringstid (risikonivå: høy).
4. Utilstrekkelig leverandørkapasitet for å tilpasse EPJ-systemer innen fristene (risikonivå: høy).

**Hva er neste steg?** Helsedirektoratet bør forankre hybridstrategien politisk hos HOD innen andre kvartal 2026. HOD bør utpeke digital helsemyndighet innen tredje kvartal 2026. Helsedirektoratet bør publisere en bindende nasjonal FHIR-overgangsplan innen fjerde kvartal 2026. Lovproposisjon bør fremmes for Stortinget innen første kvartal 2027.

---

## 1. Innledning

### 1.1 Bakgrunn og mandat

Helsedirektoratet har overordnet ansvar for å innføre EHDS i helse- og omsorgssektoren i Norge. Denne utredningen vurderer EHDS-forordningens konsekvenser for digitaliseringen i norsk helsesektor og gir en anbefaling for gjennomføring.

Utredningen er strukturert etter utredningsinstruksens seks spørsmål:
1. Hva er problemet, og hva vil vi oppnå?
2. Hvilke tiltak er relevante?
3. Hvilke prinsipielle spørsmål reiser tiltakene?
4. Hva er de positive og negative virkningene?
5. Hvilket tiltak anbefales, og hvorfor?
6. Hva er forutsetningene for vellykket gjennomføring?

### 1.2 Metode og avgrensninger

Utredningen bygger på ni delrapporter som dekker kunnskapsgrunnlag, problemdefinisjon, tiltaksalternativer, prinsipielle spørsmål, samfunnsøkonomisk vurdering, helsepersonellkonsekvenser, arkitekturkonsekvenser, anbefaling og gjennomføringsforutsetninger. Kildegrunnlaget omfatter over 30 offentlig tilgjengelige kilder, herunder Helsedirektoratets gapanalyse (april 2025), EU-kommisjonens konsekvensutredning, EØS-notatbasen og relevante EU-rettsakter.

**Avgrensninger:**
- Den samfunnsøkonomiske vurderingen er forenklet i tråd med DFØs veileder, gitt det tidlige stadiet i utredningen.
- Gjennomføringsrettsaktene fra EU-kommisjonen er ikke vedtatt, noe som skaper vesentlig usikkerhet om detaljerte krav.
- Tidspunktet for EØS-innlemmelse er uavklart.

### 1.3 Leserveiledning

Rapporten er organisert slik at hvert kapittel kan leses selvstendig, men med kryssreferanser til relevante delrapporter for lesere som ønsker mer detaljer. Ledersammendraget gir et komplett bilde og kan leses alene. Faguttrykk forklares ved første bruk og er samlet i ordlisten (vedlegg D).

---

## 2. EHDS-forordningen i kortversjon

### Hva er EHDS?

EHDS (European Health Data Space -- det europeiske helsedataområdet) er en EU-forordning (EU 2025/327) som trådte i kraft 26. mars 2025. Forordningen etablerer felles regler, standarder og infrastruktur for deling av elektroniske helsedata i EU/EØS.

### Primærbruk: deling av helseopplysninger for behandling

EHDS gir innbyggere rett til å:
- Få tilgang til og laste ned egne helseopplysninger i et standardisert europeisk format (EEHRxF -- European Electronic Health Record exchange Format)
- Dele helseopplysninger med helsepersonell i hele EU/EØS gjennom MyHealth@EU
- Begrense helsepersonells tilgang til spesifikke opplysninger
- Reservere seg mot sekundærbruk av egne helsedata (opt-out)

Helseopplysninger deles i to grupper med ulike tidsfrister:
- **Gruppe 1 (mars 2029):** Pasientoppsummeringer og e-resept/e-dispensering
- **Gruppe 2 (mars 2031):** Medisinske bilder, laboratorieresultater og epikriser

### Sekundærbruk: helsedata for forskning og folkehelse

EHDS etablerer regler for bruk av helsedata til forskning, innovasjon, politikkutforming og folkehelse. Hvert land skal opprette et tilgangsorgan (HDAB -- Health Data Access Body) som behandler søknader om datatilgang og fører tilsyn med sikre analyserom. Den europeiske infrastrukturen for sekundærbruk kalles HealthData@EU.

### Hvem berøres?

Forordningen berører alle aktører i helse- og omsorgssektoren: Helse- og omsorgsdepartementet (HOD), Helsedirektoratet, Norsk helsenett (NHN), de regionale helseforetakene (RHF-ene), over 350 kommuner, EPJ-leverandører (elektronisk pasientjournal), fastleger, sykehus, apotek, forskningsinstitusjoner og innbyggerne selv.

### Tidsfrister

| Frist | Krav |
|-------|------|
| Mars 2027 | Forordningen får full anvendelse i EU |
| Mars 2029 | Gruppe 1 (pasientoppsummeringer, e-resept) operativt |
| Mars 2031 | Gruppe 2 (bilder, lab, epikriser) operativt |

*Merknad:* Norges tidsplan avhenger av tidspunktet for EØS-innlemmelse og kan avvike fra EU-fristene.

---

## 3. Problemanalyse

*Basert på delrapport: problemdefinisjon-ehds.md*

### Hva er det faktiske problemet?

Norsk helsesektor er ikke i stand til å oppfylle EHDS-kravene til deling av helsedata -- verken nasjonalt på tvers av virksomheter eller internasjonalt på tvers av landegrenser. Problemet er strukturelt og har fire grunnårsaker:

**1. Historisk nasjonal utvikling uten europeisk harmonisering.** Norske e-helseløsninger er bygget med nasjonale meldingsstandarder og kodeverk som fungerer internt, men som ikke er kompatible med det europeiske utvekslingsformatet (EEHRxF) som EHDS krever.

**2. Fragmentert informasjonslandskap.** Helseopplysninger befinner seg i mange ulike systemer med ulike formater og tilgangskontroller. Sammenstilling av informasjon er vanskelig, både innenfor og på tvers av virksomheter.

**3. Lovverk som ikke er tilpasset grensekryssende deling.** Pasientjournalloven, helseregisterloven og pasient- og brukerrettighetsloven er ikke harmonisert med EHDS-kravene til innbyggerrettigheter, sekundærbruk og grensekryssende datautveksling.

**4. Manglende forvaltningsstrukturer.** EHDS krever en nasjonal digital helsemyndighet og et tilgangsorgan for helsedata (HDAB). Disse rollene finnes ikke i dagens norske forvaltningsstruktur.

### De viktigste gapene

Utredningen har identifisert 21 gap, fordelt slik:

| Dimensjon | Antall gap | Eksempler |
|-----------|------------|-----------|
| Rettslige | 5 | Manglende hjemmel for grensekryssende deling, uharmoniserte innbyggerrettigheter, manglende rammeverk for sekundærbruk |
| Tekniske | 6 | Manglende EEHRxF-støtte, manglende tilkobling til MyHealth@EU, manglende testinfrastruktur |
| Organisatoriske | 5 | Ingen utpekt digital helsemyndighet, ingen HDAB, kompleks aktørstruktur |
| Semantiske | 5 | Ulike kodeverk, ulik registreringspraksis, ufullstendig nasjonal informasjonsmodell |

---

## 4. Tiltaksalternativer

*Basert på delrapport: tiltaksalternativer-ehds.md*

Utredningen har vurdert fire alternativer:

### Nullalternativet

Norge viderefører pågående initiativer uten nye EHDS-tiltak. Konsekvens: Norge oppfyller ikke forordningens krav og risikerer EØS-rettslige sanksjoner. Nullalternativet er ikke reelt dersom EHDS innlemmes i EØS-avtalen.

### Alternativ 1: Stegvis minimumstilnærming

Norge implementerer kun det som er strengt nødvendig for å oppfylle minimumskravene. Et sentralt gateway-lag konverterer mellom nasjonale formater og EEHRxF ved grensekryssende utveksling. Nasjonale meldingsstandarder beholdes for nasjonal bruk. Estimert investeringskostnad: 3--6 milliarder kroner.

### Alternativ 2: Akselerert helhetlig implementering

Norge bruker EHDS som katalysator for bredere modernisering. HL7 FHIR innføres som nasjonal standard, og nasjonale meldingsstandarder fases ut. Estimert investeringskostnad: 6--12 milliarder kroner.

### Alternativ 3: Nordisk samarbeidstilnærming

Norge koordinerer implementeringen med nordiske naboland for å dele kostnader og erfaringer. Alternativ 3 er et supplement som kan kombineres med alternativ 1 eller 2, ikke et selvstendig alternativ.

### Sammenligning

| Dimensjon | Alt. 1 | Alt. 2 | Alt. 3 |
|-----------|--------|--------|--------|
| Investeringskostnad | 3--6 mrd. | 6--12 mrd. | +0,2--0,5 mrd. (tillegg) |
| Nasjonal nytteverdi | Lav | Høy | Middels |
| Arkitekturkvalitet | 2,0/5 | 4,2/5 | 2,8/5 |
| Gjennomføringsrisiko | Middels | Høy | Middels |
| Teknisk gjeld | Permanent (doble standarder) | Overgangsperiode | Avhenger av nasjonalt valg |

---

## 5. Konsekvensvurdering

### 5.1 Samfunnsøkonomisk perspektiv

*Basert på delrapport: samfunnsoekonomisk-vurdering-ehds.md*

Den samfunnsøkonomiske vurderingen er strukturert etter DFØs 8-trinnsmodell. Usikkerheten er svært høy grunnet uavklarte gjennomføringsrettsakter, usikkert EØS-innlemmelsestidspunkt og manglende kostnadsestimater fra sektoren.

**Hovedfunn:**

- Nullalternativet er ikke reelt ved EØS-innlemmelse. Kostnadene ved manglende etterlevelse overstiger sannsynligvis kostnadene ved alle tiltaksalternativene.
- Alternativ 2 vurderes som mest samfunnsøkonomisk lønnsomt over en 15-årsperiode, til tross for høyere investeringskostnader, fordi det gir størst nasjonal nytteverdi og unngår teknisk gjeld.
- EU-kommisjonen anslår samlede besparelser på 11 milliarder euro over ti år for hele EU. Norges andel er grovt anslått til 1,2--2,5 milliarder kroner.

**Nøkkeltall:**

| Alternativ | Investeringskostnad | Årlig merkostnad drift |
|------------|--------------------|-----------------------|
| Alt. 1 | 3--6 mrd. NOK | 300--600 mill. NOK (doble standarder) |
| Alt. 2 | 6--12 mrd. NOK | 200--400 mill. NOK (konsolidert) |
| Hybridstrategi | 5--9 mrd. NOK | Avtagende over tid |

Kostnadene bæres primært av staten, helseforetakene og EPJ-leverandørene. Nytten kommer i størst grad pasienter, helsepersonell, forskere og innovasjonsmiljøer til gode. Små kommuner og mindre leverandører risikerer uforholdsmessig høye kostnader uten støtteordninger.

### 5.2 Helsepersonellperspektiv

*Basert på delrapport: helsepersonellvurdering-ehds.md*

**Hovedfunn:**

- EHDS kan gi helsepersonell bedre tilgang til pasientinformasjon, særlig ved behandling av utenlandske pasienter. Dette er en reell klinisk gevinst.
- Kravene til strukturert dokumentasjon (EEHRxF) vil sannsynligvis øke dokumentasjonsbyrden på kort sikt. Helsedirektoratets undersøkelse fra 2024 viser at kun 52 prosent av helsepersonell er fornøyd med sine EPJ-systemer.
- Erfaringene fra Helseplattformen i Midt-Norge viser at store systemendringer medfører betydelig risiko for helsepersonells arbeidshverdag og pasientsikkerhet.

**16 anbefalinger for å ivareta helsepersonell, blant annet:**
- Helsedirektoratet bør stille krav om netto-nøytral dokumentasjonsbyrde: for hvert nye krav som innføres, skal det identifiseres en forenkling som kompenserer.
- Helsedirektoratet bør etablere kliniske referansegrupper med alle berørte yrkesgrupper.
- Opplæring bør starte minst 12 måneder før innføring av nye systemer.
- Systemene bør designes for akuttsituasjoner: tilgang til grensekryssende pasientinformasjon på maksimalt to klikk fra hovedskjermbildet.

**Påvirkning per yrkesgruppe:**

| Yrkesgruppe | Påvirkning | Hovedbekymring |
|-------------|------------|----------------|
| Sykehusleger | Middels til høy | Økt dokumentasjonsbyrde, systemendringer |
| Fastleger | Lav til middels | Endringer i EPJ-systemer, struktureringskrav |
| Sykepleiere | Middels | Allerede høy EPJ-tid (2 timer/dag), ytterligere krav |
| Helsefagarbeidere | Lav | Varierende digital kompetanse |
| Farmasøyter | Middels til høy | Grensekryssende e-resepter, språkbarrierer |

### 5.3 Arkitekturperspektiv

*Basert på delrapport: arkitekturkonsekvenser-ehds.md*

**Hovedfunn:**

Alternativ 2 scorer klart best på arkitekturkvalitet (4,2/5 mot alternativ 1: 2,0/5) langs fem dimensjoner:

| Dimensjon | Alt. 1 | Alt. 2 |
|-----------|--------|--------|
| Interoperabilitet | 2/5 | 5/5 |
| Teknisk gjeld | 1/5 | 4/5 |
| Leverandøravhengighet | 2/5 | 4/5 |
| Skalerbarhet | 2/5 | 4/5 |
| Sikkerhet by design | 3/5 | 4/5 |

**Styrker i dagens arkitektur:** Kjernejournal er operativ med FHIR-baserte API-er. Reseptformidleren er pilotert mot MyHealth@EU. HelseID gir nasjonal identitetsinfrastruktur. NHN har gjennomført MyHealth@EU-pilotering.

**Svakheter i dagens arkitektur:** Meldingsbasert integrasjon dominerer. EPJ-landskapet er fragmentert (DIPS, Epic/Helseplattformen, CGM, Visma, Infodoc). Semantisk heterogenitet med ulike kodeverk. Ingen infrastruktur for sekundærbruk.

**Den viktigste arkitekturbeslutningen** er ikke valget mellom alternativ 1 eller 2, men om gateway-laget i alternativ 1 designes som midlertidig bro eller permanent infrastruktur. Dersom det blir permanent, akkumulerer Norge teknisk gjeld som blir stadig dyrere å håndtere.

### 5.4 Prinsipielle spørsmål

*Basert på delrapport: prinsipielle-spoersmaal-ehds.md*

Utredningen identifiserer tre grunnleggende spenninger:

**1. Åpenhet mot beskyttelse.** EHDS krever økt deling av helsedata. Norsk tradisjon legger stor vekt på taushetsplikten. Løsningen ligger i robuste tekniske og juridiske sikkerhetstiltak som gjør økt deling mulig uten å undergrave tilliten.

**2. Europeisk harmonisering mot nasjonal tilpasning.** EHDS er en forordning (ikke et direktiv), noe som begrenser det nasjonale handlingsrommet. Norge bør kartlegge og utnytte tilpasningsmulighetene systematisk.

**3. Ambisjon mot gjennomføringsevne.** Gjennomføringsevnen varierer mellom aktører. En trinnvis tilnærming med tilstrekkelig finansiering og kompetansebygging er avgjørende.

**Sentrale avveininger:**

- *Personvern:* Opt-out-retten fra sekundærbruk kan bli illusorisk dersom unntakene for «offentlig interesse» er for brede. Norge bør ta stilling til om innbyggerne skal få sterkere reservasjonsrett enn minimumskravene.
- *Maktfordeling:* Kommunene risikerer uforholdsmessig høye kostnader. Staten bør fullfinansiere kommunenes merkostnader.
- *Pasientrettigheter:* EHDS gir nye rettigheter som ikke finnes i gjeldende norsk rett (nedlasting i EEHRxF, grensekryssende deling, tilgangsbegrensning). Disse krever teknisk infrastruktur som ikke er på plass.
- *Mindreåriges rettigheter:* Det norske systemet med gradert samtykkekompetanse for barn bør videreføres innenfor EHDS-rammeverket.

---

## 6. Anbefaling

*Basert på delrapport: anbefaling-ehds.md*

### Den anbefalte hybridstrategien

Utredningen anbefaler en hybridstrategi der alternativ 1 (stegvis minimum) brukes som taktisk startpunkt, alternativ 2 (akselerert helhetlig) settes som bindende strategisk mål, og alternativ 3 (nordisk samarbeid) følges som parallell samarbeidsdimensjon.

**Fase 1 (2026--2029): Taktisk etterlevelse med strategisk retning**

- Helsedirektoratet og NHN etablerer et gateway-lag for gruppe 1-kategoriene (pasientoppsummeringer, e-resept).
- NHN bygger videre på kjernejournals FHIR-API-er og reseptformidlerens MyHealth@EU-pilot.
- Helsedirektoratet publiserer en bindende nasjonal FHIR-overgangsplan.
- Alle nye integrasjoner skal bruke FHIR fra dag én.
- HOD utpeker digital helsemyndighet. Helsedirektoratet etablerer HDAB.

*Kritisk designprinsipp:* Gateway-laget skal designes eksplisitt som midlertidig infrastruktur med en bindende utfasingsplan.

**Fase 2 (2029--2031): Gradvis overgang til FHIR**

- NHN og leverandørene implementerer gruppe 2-kategoriene med FHIR-baserte grensesnitt der mulig.
- Helsedirektoratet starter utfasing av gateway-konvertering for komponenter der kildene er blitt FHIR-native.
- Helsedirektoratet setter krav til EPJ-leverandører om FHIR-støtte i anskaffelser og kontraktsfornyelser.

**Fase 3 (2031--2035): Konsolidering**

- NHN fullfører utfasing av nasjonale meldingsstandarder for EHDS-kategorier.
- Alle EPJ-leverandører leverer FHIR-baserte API-er.
- Gateway-laget fases ut.

**Parallelt: Nordisk samarbeid**

- Helsedirektoratet etablerer en nordisk EHDS-koordineringsgruppe innen andre kvartal 2026.
- Landene deler terminologitjenester, testinfrastruktur og FHIR-basisprofiler.
- Helsedirektoratet koordinerer leverandørdialog med DIPS, CGM og Visma, som opererer i flere nordiske markeder.

### Begrunnelse

| Perspektiv | Begrunnelse for hybridstrategien |
|------------|----------------------------------|
| Samfunnsøkonomi | Reduserer risikoen for feilinvesteringer tidlig, samtidig som Norge beveger seg mot den langsiktig optimale løsningen |
| Helsepersonell | Minst mulig forstyrrelse på kort sikt, men sikrer langsiktig forbedring |
| Arkitektur | Kompromissperiode med noe teknisk gjeld, men unngår den permanente gjelden ved rent alternativ 1 |
| Prinsipielt | Gir tid til grundig politisk behandling, samtidig som Norge holder fristene |

### Estimert kostnad for hybridstrategien: 5--9 milliarder kroner

| Periode | Årlig investering | Kumulativt | Hovedaktiviteter |
|---------|-------------------|------------|------------------|
| 2026--2027 | 500--800 mill. | 1,0--1,6 mrd. | Program, lovarbeid, spesifikasjoner, NCPeH |
| 2028--2029 | 800--1 200 mill. | 2,6--4,0 mrd. | Gateway, testinfrastruktur, HDAB, gruppe 1 |
| 2030--2031 | 600--1 000 mill. | 3,8--6,0 mrd. | Gruppe 2, FHIR-overgang, sikre analyserom |
| 2032--2035 | 400--800 mill./år | 5,4--9,2 mrd. | FHIR-konsolidering, gateway-utfasing |

---

## 7. Gjennomføringsforutsetninger

*Basert på delrapport: gjennomfoeringsforutsetninger-ehds.md*

### Juridiske forutsetninger

Fem lover må endres eller suppleres:

| Lov | Endringsbehov |
|-----|---------------|
| Pasientjournalloven | Hjemmel for grensekryssende deling, krav til EPJ-systemer |
| Pasient- og brukerrettighetsloven | Nye innbyggerrettigheter (nedlasting, tilgangsbegrensning, opt-out) |
| Helseregisterloven | Tilpasning til sekundærbruk, datatillatelser, sikre analyserom |
| Helsepersonelloven | Tilpasning av taushetsplikt til grensekryssende deling |
| Helseforskningsloven | Harmonisering med EHDS-modellen for sekundærbruk |

EØS-innlemmelse krever artikkel 103-forbehold og Stortingets samtykke.

### Organisatoriske forutsetninger

- HOD bør utpeke Helsedirektoratet som digital helsemyndighet innen tredje kvartal 2026.
- Helsedirektoratet bør etablere HDAB med utgangspunkt i Helsedataservice ved FHI innen andre kvartal 2028.
- Helsedirektoratet bør etablere et nasjonalt EHDS-program med tverrsektoriell styringsgruppe innen andre kvartal 2026.

### Kompetanseforutsetninger

- Norge trenger minst 200 FHIR-spesialister i offentlig sektor innen 2029 (i dag anslagsvis under 50).
- Helsedirektoratet bør etablere et nasjonalt FHIR-kompetanseprogram i samarbeid med HL7 Norway innen første kvartal 2027.
- Kompetansebyggingen bør dekke FHIR, semantisk interoperabilitet (SNOMED CT, LOINC), europeisk samarbeid og endringsledelse.

### Tekniske forutsetninger

- NHN skal etablere nasjonalt kontaktpunkt for e-helse (NCPeH) operativt for gruppe 1 innen fjerde kvartal 2028.
- NHN skal etablere testinfrastruktur for obligatorisk testing av EPJ-systemer innen fjerde kvartal 2028.
- NHN og FHI skal etablere sikre analyserom for sekundærbruk innen første kvartal 2030.
- Helsedirektoratet skal etablere en sentral nasjonal terminologitjeneste (SNOMED CT, LOINC, ATC) innen andre kvartal 2028.

### Økonomiske forutsetninger

Staten bør bære 60--70 prosent av kostnadene gjennom bevilgninger over HODs budsjett. Kommunesektorens merkostnader bør fullfinansieres av staten. Norge bør aktivt søke EU-midler gjennom EU4Health, CEF Digital og Horizon Europe.

---

## 8. Risiko

*Basert på delrapport: gjennomfoeringsforutsetninger-ehds.md*

### De fem viktigste risikoene

| Nr | Risiko | Sannsynlighet | Konsekvens | Tiltak |
|----|--------|---------------|------------|--------|
| 1 | Gateway-laget sementeres som permanent infrastruktur | Høy | Svært høy | Bindende politisk vedtak om FHIR-overgangsplan. Årsrapportering til Stortinget. |
| 2 | Kostnadsoverskridelser | Svært høy | Høy | Trinnvis implementering med stoppunkter. Realistisk budsjettering. |
| 3 | Forsinket EØS-innlemmelse | Høy | Høy | Forhandle tilpasningstekst med overgangsfrister. Starte forberedelser før innlemmelse. |
| 4 | Utilstrekkelig leverandørkapasitet | Høy | Høy | Tidlig leverandørdialog. Koordinert nordisk kravstilling. |
| 5 | Konverteringsfeil i gateway gir pasientsikkerhetsrisiko | Middels | Svært høy | Grundig testing og klinisk kvalitetssikring. Pilotdrift. |

### Samlet risikobilde

Utredningen har identifisert 15 risikoer. Ingen har risikonivå «svært høy» (rød), men fire har risikonivå «høy» (oransje) og ni har risikonivå «middels» (gul). Den strategisk viktigste risikoen er at gateway-laget blir permanent, fordi dette i praksis betyr at Norge velger alternativ 1 med all den tekniske gjelden det medfører.

---

## 9. Neste steg

Helsedirektoratet anbefaler følgende konkrete handlinger:

| Nr | Handling | Ansvarlig | Frist |
|----|----------|-----------|-------|
| 1 | Forankre hybridstrategien politisk hos HOD | Helsedirektoratet | 2026 Q2 |
| 2 | Etablere nasjonalt EHDS-program med mandat og budsjett | HOD / Helsedirektoratet | 2026 Q2 |
| 3 | Utpeke digital helsemyndighet formelt | HOD | 2026 Q3 |
| 4 | Publisere bindende nasjonal FHIR-overgangsplan | Helsedirektoratet | 2026 Q4 |
| 5 | Gjennomføre leverandørdialog med DIPS, Epic, CGM, Visma, Infodoc | Helsedirektoratet / NHN | 2026 Q3 |
| 6 | Etablere nordisk EHDS-koordineringsgruppe | Helsedirektoratet | 2026 Q2 |
| 7 | Fremme lovproposisjon for Stortinget | HOD | 2027 Q1 |
| 8 | Etablere HDAB med grunnleggende funksjonalitet | Helsedirektoratet / FHI | 2028 Q2 |
| 9 | Gjennomføre fullverdig samfunnsøkonomisk analyse | Helsedirektoratet / DFØ | 2027 Q4 |
| 10 | Etablere kliniske referansegrupper | Helsedirektoratet | 2026 Q3 |
| 11 | Starte nasjonalt FHIR-kompetanseprogram | Helsedirektoratet / NHN | 2027 Q1 |
| 12 | Etablere nasjonal testinfrastruktur for EPJ-systemer | NHN | 2028 Q4 |

---

## Vedlegg

### A. Delrapporter

| Delrapport | Beskrivelse |
|------------|-------------|
| kunnskapsgrunnlag-ehds.md | Faktagrunnlag med 30 kilder. Strukturert etter utredningsinstruksens seks spørsmål. |
| problemdefinisjon-ehds.md | Problemanalyse med 4 grunnårsaker og 21 identifiserte gap langs fire dimensjoner. |
| tiltaksalternativer-ehds.md | Nullalternativet og 3 tiltaksalternativer med sammenlignende tabell. |
| prinsipielle-spoersmaal-ehds.md | Drøfting av 6 hovedområder: personvern, suverenitet, maktfordeling, pasientrettigheter, interoperabilitet, likebehandling. |
| samfunnsoekonomisk-vurdering-ehds.md | Forenklet samfunnsøkonomisk vurdering etter DFØs 8-trinnsmodell. Estimat: 3--12 mrd. NOK. |
| helsepersonellvurdering-ehds.md | Konsekvensanalyse per yrkesgruppe. 16 anbefalinger. Helseplattformen som referanse. |
| arkitekturkonsekvenser-ehds.md | Arkitekturvurdering langs 5 dimensjoner. Alternativ 2 scorer 4,2/5. Hybridstrategi anbefalt. |
| anbefaling-ehds.md | Sammenstilt anbefaling: hybridstrategi i tre faser med nordisk samarbeid. |
| gjennomfoeringsforutsetninger-ehds.md | 5 lover, 200+ FHIR-spesialister, 5--9 mrd. NOK. 15 identifiserte risikoer. |

### B. Visualiseringer

| Visualisering | Beskrivelse |
|---------------|-------------|
| naa-situasjon-arkitektur.html | ArchiMate-inspirert diagram over dagens arkitektur for helsedatadeling i Norge. |
| ehds-maalarkitektur.html | Målarkitektur for EHDS i Norge med tidsfrister og komponentstatus. |
| gap-analyse-per-alternativ.html | Sammenligning av alternativer langs fem arkitekturkvalitetsdimensjoner med radardiagram. |
| tidslinje-ehds-implementering.html | Interaktiv tidslinje 2026--2035 med EU-frister og norske milepæler. |
| risikomatrise-ehds.html | Interaktiv risikomatrise med 15 risikoer plottet på sannsynlighet og konsekvens. |
| ehds-utredning-dashbord.html | Overordnet dashbord for ledelsen med nøkkeltall, samsvarsstatus og top 5 risikoer. |
| aktoer-ansvar-oversikt.html | Visualisering av aktørers roller og ansvar i EHDS-innføringen. |

### C. Kilder

**EU-rettsakter og EU-kilder:**
1. Regulation (EU) 2025/327 -- EUR-Lex
2. European Health Data Space Regulation -- EU-kommisjonen
3. Impact Assessment SWD(2022) 131 -- EU-kommisjonen
4. HDABs Community of Practice -- EU-kommisjonen

**Norske myndighetskilder:**
5. Helsedirektoratets EHDS konsekvensvurdering -- Gapanalyse pr. 11. april 2025
6. EØS-notat: Forordning om det europeiske helsedataområdet -- regjeringen.no
7. Prop. 91 L (2021--2022) -- Endringer i pasientjournalloven
8. Prop. 1 S (2025--2026) -- Helse- og omsorgsdepartementet
9. Nasjonal e-helsestrategi -- Helsedirektoratet
10. Meld. St. 9 (2023--2024) -- Nasjonal helse- og samhandlingsplan
11. Meld. St. 23 (2024--2025) -- regjeringen.no
12. Oversikt over kriterier til sikre analyserom -- Helsedirektoratet
13. SPUHiN-prosjektet -- Helsedirektoratet
14. Nasjonal informasjonsmodell (Helse-NIM) -- Helsedirektoratet
15. MyHealth@EU -- Norsk helsenett
16. Standardiseringstiltak knyttet til EHDS -- Helsedirektoratet

**Helsepersonell og sektor:**
17. Helsepersonellundersøkelsen om digitalisering 2024 -- Helsedirektoratet
18. Helseplattformen -- Tidsskrift for Den norske legeforening
19. Legeforeningen: Brukervennlighet er pasientsikkerhet
20. Sykepleien: Sykepleiere bruker to timer per dag på EPJ
21. Kartlegging av digital modenhet -- KS

**Stortinget:**
22. Enighet om helsedata (EHDS) -- Stortinget EU/EØS-nytt
23. Nytt regelverk for deling av helsedata -- Stortinget

**Juridiske kilder:**
24. Forordning om europeisk helsedataområde -- europalov.no
25. EØS-avtalen artikkel 103 -- europalov.no
26. DLA Piper: EHDS og GDPR

**Tekniske kilder:**
27. HL7 Europe: FHIR Implementation Guides for EHDS
28. HL7 Norway -- Nasjonale FHIR-profiler
29. Open DIPS -- FHIR-dokumentasjon
30. NHN Utviklerportal -- Kjernejournal FHIR API
31. DFØ: Veileder i samfunnsøkonomiske analyser

**Nordiske kilder:**
32. FHIR Base Profiles in the Nordics -- Vitalis 2025
33. Cross-border eP and PS in the Nordic countries -- E-hälsomyndigheten

### D. Ordliste

| Forkortelse | Forklaring |
|-------------|------------|
| ATC | Anatomisk terapeutisk kjemisk klassifikasjon (kodeverk for legemidler) |
| CEF | Connecting Europe Facility (EUs finansieringsmekanisme for digital infrastruktur) |
| DFØ | Direktoratet for forvaltning og økonomistyring |
| DHA | Digital Health Authority (nasjonal digital helsemyndighet) |
| DPIA | Data Protection Impact Assessment (personvernkonsekvensutredning) |
| EEHRxF | European Electronic Health Record exchange Format (det europeiske utvekslingsformatet for helsedata) |
| EHDS | European Health Data Space (det europeiske helsedataområdet, forordning EU 2025/327) |
| eIDAS | Electronic Identification, Authentication and Trust Services (EU-forordning om digital identitet) |
| EPJ | Elektronisk pasientjournal |
| EUDI | European Digital Identity (europeisk digital identitet, digital lommebok) |
| FEST | Forskrivnings- og ekspedisjonsstøtte (norsk legemiddeldatabase) |
| FHIR | Fast Healthcare Interoperability Resources (HL7-standard for helsedatautveksling) |
| FHI | Folkehelseinstituttet |
| GDPR | General Data Protection Regulation (personvernforordningen) |
| HDAB | Health Data Access Body (nasjonalt tilgangsorgan for helsedata til sekundærbruk) |
| HelseID | Norsk identitets- og tilgangsinfrastruktur for helsesektoren |
| Helse-NIM | Nasjonal informasjonsmodell for helseopplysninger |
| HL7 | Health Level Seven International (standardiseringsorganisasjon for helseinformatikk) |
| HOD | Helse- og omsorgsdepartementet |
| ICD-10 | International Classification of Diseases, 10. revisjon |
| ICPC-2 | International Classification of Primary Care, 2. utgave |
| IHE | Integrating the Healthcare Enterprise (interoperabilitetsinitiativ) |
| IPS | International Patient Summary (internasjonal pasientoppsummering) |
| KS | Kommunesektorens organisasjon |
| LOINC | Logical Observation Identifiers Names and Codes (kodeverk for laboratoriesvar) |
| MHD | Mobile access to Health Documents (IHE-profil) |
| NCPeH | National Contact Point for eHealth (nasjonalt kontaktpunkt for grensekryssende e-helse) |
| NHN | Norsk helsenett |
| NOU | Norsk offentlig utredning |
| RHF | Regionalt helseforetak |
| SMART | Substitutable Medical Applications, Reusable Technologies (applikasjonsrammeverk for FHIR) |
| SNOMED CT | Systematized Nomenclature of Medicine -- Clinical Terms (medisinsk terminologi) |
| SPE | Secure Processing Environment (sikkert analyserom) |
| SPUHiN | Secure Provision and Use of Health data in Norway (EU4Health-prosjekt) |

---

*Denne utredningen er utarbeidet mars 2026 som del av Helsedirektoratets arbeid med å vurdere konsekvensene av EHDS-forordningen for norsk helsesektor. Utredningen bør revideres når gjennomføringsrettsakter fra EU-kommisjonen vedtas, EØS-innlemmelse avklares og mer detaljerte kostnadsestimater foreligger.*
