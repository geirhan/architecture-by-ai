# Tiltaksalternativer for EHDS-implementering i Norge

## Sammendrag

Denne rapporten beskriver tre tiltaksalternativer for implementering av EHDS-forordningen i Norge, samt nullalternativet. Alternativene varierer i ambisjonsnivå, tempo og kostnad:

- **Nullalternativet**: Videreføring av pågående initiativer uten nye tiltak rettet mot EHDS. Konsekvens: Norge oppfyller ikke forordningens krav og risikerer EØS-rettslige sanksjoner.
- **Alternativ 1 – Stegvis minimumstilnærming**: Implementere kun det som er strengt nødvendig for å oppfylle forordningens minimumskrav, trinnvis i takt med fristene.
- **Alternativ 2 – Akselerert helhetlig implementering**: Bruke EHDS som katalysator for bredere modernisering av norsk e-helseinfrastruktur.
- **Alternativ 3 – Nordisk samarbeidstilnærming**: Koordinert implementering med de øvrige nordiske landene for å dele kostnader, erfaringer og infrastruktur.

Alle tre tiltaksalternativene forutsetter EØS-innlemmelse med artikkel 103-forbehold og nødvendige lovendringer.

---

## Nullalternativet

### Beskrivelse

Nullalternativet innebærer at Norge viderefører pågående initiativer uten nye tiltak spesifikt rettet mot EHDS. Dette inkluderer:

- Videreføring av arbeidet med «Én innbygger – én journal» og endringer i pasientjournalloven
- Videreføring av NHNs MyHealth@EU-pilotering i begrenset omfang
- Videreføring av SPUHiN-prosjektet for sikre analyserom
- Videreføring av pågående standardiseringsarbeid
- Ingen nye bevilgninger eller organisatoriske endringer rettet mot EHDS

### Konsekvenser av nullalternativet

**Rettslige konsekvenser:**
- Norge vil ikke oppfylle EHDS-forordningens krav ved EØS-innlemmelse. Forordningen er EØS-relevant, og manglende gjennomføring kan føre til prosedyrer under EØS-avtalen (ESA-tilsyn, potensielle sanksjoner).
- Innbyggernes rettigheter etter EHDS (tilgang, nedlasting, opt-out) vil ikke ha rettslig forankring i norsk lov.

**Tekniske konsekvenser:**
- Norske EHR-systemer vil ikke støtte EEHRxF. Helseopplysninger kan ikke utveksles i europeisk format.
- Norge vil ikke være tilkoblet MyHealth@EU eller HealthData@EU operativt.
- Norske pasienter som behandles i andre EU/EØS-land vil ikke ha tilgang til sine helseopplysninger, og helsepersonell vil ikke kunne motta opplysninger om pasienter fra andre land.

**Organisatoriske konsekvenser:**
- Ingen digital helsemyndighet utpekt, ingen HDAB etablert. Norge vil mangle de forvaltningsstrukturene forordningen krever.

**Konsekvenser for forskning og innovasjon:**
- Norge vil stå utenfor den europeiske infrastrukturen for sekundærbruk av helsedata. Norske forskere får begrenset tilgang til europeiske helsedata, og europeiske forskere får ikke tilgang til norske data gjennom HealthData@EU.
- Konkurranseulempe for norske forskningsmiljøer og helsenæring.

**Samlet vurdering:**
Nullalternativet er i praksis ikke et reelt alternativ dersom Norge innlemmer EHDS i EØS-avtalen, fordi manglende gjennomføring vil utgjøre et brudd på Norges EØS-rettslige forpliktelser. Selv om innlemmelsestidspunktet er uavklart, er det en klar forventning om at EHDS vil bli innlemmet. Nullalternativet fungerer derfor primært som referansepunkt for å vurdere verdien av de øvrige alternativene.

---

## Alternativ 1: Stegvis minimumstilnærming

### Overordnet beskrivelse

Norge implementerer kun det som er strengt nødvendig for å oppfylle EHDS-forordningens minimumskrav, trinnvis i takt med fristene. Fokus er på å møte de rettslige forpliktelsene med lavest mulig kostnad og risiko, uten å bruke EHDS som anledning til bredere modernisering.

### Arkitekturvalg

- **Føderert arkitektur med sentralt kontaktpunkt.** Eksisterende systemer beholdes i størst mulig grad. Det etableres et sentralt «oversettingslag» (gateway) som konverterer mellom nasjonale formater og EEHRxF ved grensekryssende utveksling.
- **Begrenset gjenbruk.** Eksisterende nasjonale meldingsstandarder beholdes for nasjonal bruk. EEHRxF implementeres kun for grensekryssende scenarioer.
- **Minimum nasjonal testinfrastruktur.** Testmiljø etableres for de prioriterte kategoriene, men ikke bredere.

### Regulatorisk tilnærming

- Lovendringer begrenses til det som er strengt nødvendig for å gjennomføre forordningen i norsk rett.
- Innbyggerrettigheter implementeres i tråd med forordningens minimumskrav.
- Nasjonalt handlingsrom utnyttes for å begrense omfanget av endringer der forordningen tillater det.

### Organisatorisk modell

- Helsedirektoratet utpekes som digital helsemyndighet, med eksisterende organisasjon og begrenset styrking.
- HDAB etableres som en ny funksjon, fortrinnsvis ved å bygge videre på helsedata.no/FHI-infrastrukturen.
- NHN viderefører operativt ansvar for MyHealth@EU-tilkobling.
- Koordinering skjer gjennom eksisterende styringsstrukturer, uten nye programorganisasjoner.

### Tidslinje og milepæler

| Tidspunkt | Milepæl |
|-----------|---------|
| 2026 Q3 | Digital helsemyndighet formelt utpekt |
| 2027 Q1 | Lovproposisjon fremmet for Stortinget |
| 2027 Q4 | Lovendringer vedtatt og trådt i kraft |
| 2028 Q1 | Nasjonal gateway for EEHRxF-konvertering i testdrift |
| 2028 Q2 | HDAB etablert med grunnleggende funksjonalitet |
| 2028 Q4 | Testmiljø for obligatorisk testing av EHR-systemer operativt |
| 2029 Q1 | Gruppe 1 (pasientoppsummeringer, e-resept) operativt via MyHealth@EU |
| 2030 Q1 | Sikre analyserom for sekundærbruk operativt |
| 2031 Q1 | Gruppe 2 (bilder, lab, epikriser) operativt via MyHealth@EU |

### Viktigste risikoer

1. **Gateway-tilnærmingen kan gi lav datakvalitet.** Automatisk konvertering mellom nasjonale formater og EEHRxF kan gi tap av informasjon eller feilaktig mapping, med potensiell pasientsikkerhetsrisiko.
2. **Begrenset nasjonal nytteverdi.** Dersom EEHRxF kun brukes for grensekryssende scenarioer, får ikke Norge den fulle gevinsten av bedre nasjonal interoperabilitet.
3. **Teknisk gjeld.** Å opprettholde to parallelle standarder (nasjonale meldingsstandarder + EEHRxF for grensekryssende) øker kompleksiteten og vedlikeholdskostnadene over tid.
4. **Leverandørkapasitet.** Selv minimumskravene krever at EHR-leverandører gjennomfører betydelig utvikling. Det er usikkert om kapasiteten er tilstrekkelig.
5. **Stramme tidsfrister.** Selv med minimumstilnærming er tidsplanen krevende, gitt usikkerhet om EØS-innlemmelse og mange avhengigheter.

### Estimert kostnadsnivå

**Middels.** Lavere enn alternativ 2, men fortsatt betydelige investeringer knyttet til gateway-utvikling, HDAB-etablering, lovendringer, testinfrastruktur og leverandørtilpasning. Løpende driftskostnader for to parallelle standarder kan over tid bli kostbare.

---

## Alternativ 2: Akselerert helhetlig implementering

### Overordnet beskrivelse

Norge bruker EHDS som katalysator for en bredere modernisering av nasjonal e-helseinfrastruktur. EEHRxF (HL7 FHIR) innføres som nasjonal standard for datautveksling, ikke bare for grensekryssende scenarioer. Eksisterende initiativer (Én innbygger – én journal, Helse-NIM, MyHealth@EU) akselereres og koordineres under ett program.

### Arkitekturvalg

- **Nasjonal FHIR-basert arkitektur.** EEHRxF/HL7 FHIR innføres som nasjonal standard for datautveksling, i tillegg til grensekryssende bruk. Nasjonale meldingsstandarder fases gradvis ut.
- **Sentralisert informasjonsmodell.** Helse-NIM utvides til å dekke alle prioriterte kategorier og danner grunnlaget for nasjonal og europeisk interoperabilitet.
- **Sentral nasjonal infrastruktur.** NHN utvikler og drifter sentrale komponenter for formatkonvertering, terminologitjenester, sertifiseringsverktøy og testinfrastruktur.
- **Maksimal gjenbruk og konsolidering.** Eksisterende løsninger (kjernejournal, reseptformidleren, helsenorge.no) videreutvikles for å oppfylle EHDS-krav, fremfor å bygge parallelle systemer.

### Regulatorisk tilnærming

- Lovendringer gjennomføres bredt, med sikte på å ikke bare oppfylle minimumskravene, men også legge til rette for videre digitalisering.
- Pågående lovarbeid (pasientjournalloven, helseregisterloven, helseforskningsloven) koordineres tett med EHDS-kravene.
- Norge bruker det nasjonale handlingsrommet proaktivt for å styrke pasientrettigheter og forskningsdata-tilgang.

### Organisatorisk modell

- **Nasjonalt EHDS-program.** Det etableres et tverrsektorielt program med tydelig mandat, budsjett og styringsstruktur, ledet av Helsedirektoratet i samarbeid med HOD.
- **Styrket digital helsemyndighet.** Helsedirektoratets rolle som digital helsemyndighet styrkes med dedikerte ressurser for EHDS-implementering, europeisk samarbeid og standardisering.
- **Profesjonell HDAB.** HDAB etableres som en robust funksjon med tilstrekkelig kapasitet, bygget på helsedata.no-infrastrukturen men med vesentlig styrking.
- **Koordinert leverandørdialog.** Systematisk samarbeid med EHR-leverandører for å sikre rettidig tilpasning, inkludert felles veikart og incitamenter.
- **Kompetanseprogram.** Nasjonalt program for å bygge kompetanse innen HL7 FHIR, EEHRxF og europeisk helseinteroperabilitet.

### Tidslinje og milepæler

| Tidspunkt | Milepæl |
|-----------|---------|
| 2026 Q2 | Nasjonalt EHDS-program etablert med mandat og budsjett |
| 2026 Q3 | Digital helsemyndighet formelt utpekt og styrket |
| 2026 Q4 | Nasjonal veikart for FHIR-overgang publisert |
| 2027 Q1 | Lovproposisjon fremmet for Stortinget |
| 2027 Q2 | Helse-NIM for gruppe 1 ferdigstilt |
| 2027 Q4 | Lovendringer vedtatt. Nasjonal FHIR-infrastruktur i testdrift |
| 2028 Q1 | HDAB operativ med grunnleggende funksjonalitet |
| 2028 Q2 | Første EHR-systemer sertifisert for EEHRxF |
| 2028 Q4 | MyHealth@EU operativt for gruppe 1 |
| 2029 Q1 | Gruppe 1 fullt operativt. Sikre analyserom i pilotdrift |
| 2029 Q3 | Helse-NIM for gruppe 2 ferdigstilt |
| 2030 Q1 | HealthData@EU og sikre analyserom fullt operativt |
| 2030 Q4 | Første EHR-systemer sertifisert for gruppe 2 |
| 2031 Q1 | Gruppe 2 fullt operativt |

### Viktigste risikoer

1. **Høy kompleksitet.** Å kombinere EHDS-implementering med bredere modernisering øker prosjektets kompleksitet og antall avhengigheter.
2. **Høy kostnad.** Vesentlig høyere investeringsbehov enn alternativ 1, med usikkerhet om totalrammen.
3. **Endringsmotstand.** Utfasing av nasjonale meldingsstandarder til fordel for FHIR kan møte motstand fra leverandører og virksomheter som har investert tungt i eksisterende løsninger.
4. **Kapasitetsbegrensninger.** Både offentlige og private aktører kan mangle kapasitet til å gjennomføre endringene i det tempoet som kreves.
5. **Avhengighet av EU-prosesser.** Gjennomføringsrettsaktene fra EU-kommisjonen er ikke vedtatt. Dersom disse forsinkes eller endrer innretning, kan den norske planen måtte revideres.

### Estimert kostnadsnivå

**Høy.** Vesentlig høyere investeringskostnad enn alternativ 1, men potensielt lavere totalkostnad over tid fordi man unngår doble standarder og teknisk gjeld. Den bredere moderniseringen kan også gi nasjonale effektiviseringsgevinster som delvis motvirker merkostnaden.

---

## Alternativ 3: Nordisk samarbeidstilnærming

### Overordnet beskrivelse

Norge koordinerer EHDS-implementeringen med de øvrige nordiske landene (Sverige, Danmark, Finland, Island) for å dele erfaringer, kostnader og infrastruktur. De nordiske landene har lignende helsesystemer, offentlige forvaltningsstrukturer og digitaliserings-modenhet, og står overfor mange av de samme utfordringene.

### Arkitekturvalg

- **Felles nordisk referansearkitektur.** De nordiske landene utvikler en felles referansearkitektur for EHDS-implementering, med nasjonale tilpasninger der det er nødvendig.
- **Delte komponenter.** Terminologitjenester, konverteringsverktøy, testinfrastruktur og kompetanseressurser utvikles i fellesskap og deles mellom landene.
- **Koordinert leverandørdialog.** Flere nordiske leverandører opererer i flere nordiske markeder. En koordinert tilnærming til leverandørkrav og sertifisering kan gi stordriftsfordeler.
- **Nasjonal kjerneinfrastruktur.** Hver nasjon beholder sin kjerneinfrastruktur (MyHealth@EU-kontaktpunkt, HDAB), men med felles standarder og grensesnitt.

### Regulatorisk tilnærming

- Nasjonale lovendringer gjennomføres i hvert land, men med koordinert tolkning av forordningens krav.
- Felles nordisk posisjon i EU-prosesser for gjennomføringsrettsakter, for å sikre at nordiske hensyn ivaretas.
- Erfaringsutveksling om nasjonalt handlingsrom og rettslig tilpasning.

### Organisatorisk modell

- **Nordisk EHDS-koordineringsgruppe.** Etablering av et uformelt eller formelt nordisk samarbeidsforum for EHDS-implementering, forankret i eksisterende nordiske samarbeidsstrukturer (f.eks. Nordisk ministerråd, NordForsk).
- **Nasjonale program med nordisk koordinering.** Hvert land har sitt nasjonale program, men med faste koordineringspunkter for erfaringsdeling, felles spesifikasjoner og delt utvikling.
- **Felles kompetansebygging.** Nordisk program for kompetanseutvikling innen HL7 FHIR, EEHRxF og EHDS-relaterte temaer.

### Tidslinje og milepæler

| Tidspunkt | Milepæl |
|-----------|---------|
| 2026 Q2 | Nordisk EHDS-koordineringsgruppe etablert |
| 2026 Q3 | Felles nordisk referansearkitektur påbegynt |
| 2026 Q4 | Nasjonal digital helsemyndighet utpekt i alle nordiske land |
| 2027 Q2 | Felles nordisk spesifikasjon for terminologitjenester |
| 2027 Q4 | Delt nordisk testinfrastruktur i pilotdrift |
| 2028 Q2 | HDAB operativ i alle nordiske land |
| 2029 Q1 | Gruppe 1 operativt. Nordisk pilottest av grensekryssende utveksling |
| 2030 Q1 | HealthData@EU og sikre analyserom operativt |
| 2031 Q1 | Gruppe 2 fullt operativt |

### Viktigste risikoer

1. **Koordineringskompleksitet.** Nordisk samarbeid krever enighet mellom selvstendige nasjoner med ulike politiske prosesser og tidsplaner. EU-land (Sverige, Danmark, Finland) og EØS-land (Norge, Island) har ulike tidsfrister.
2. **Ulik modenhet.** De nordiske landene har ulik teknisk modenhet og ulike nasjonale systemer, noe som begrenser hva som kan deles.
3. **Risiko for forsinkelse.** Avhengighet av nordisk koordinering kan forsinke nasjonale beslutninger og implementering dersom enighet tar tid.
4. **Begrenset formelt mandat.** Nordisk samarbeid er frivillig, og det er begrenset formell myndighet til å forplikte deltakerlandene.
5. **Potensial for «laveste felles nevner».** Felles løsninger kan bli kompromisser som ikke er optimale for noe enkelt land.

### Estimert kostnadsnivå

**Middels til høy.** Høyere koordineringskostnad enn alternativ 1, men potensielt lavere totalkostnad enn alternativ 2 gjennom deling av utviklingskostnader. Besparelsene avhenger av i hvilken grad felles komponenter faktisk lar seg realisere.

---

## Sammenligning av alternativer

| Dimensjon | Nullalternativet | Alt. 1: Stegvis minimum | Alt. 2: Akselerert helhetlig | Alt. 3: Nordisk samarbeid |
|-----------|-----------------|------------------------|------------------------------|--------------------------|
| **Investerings-kostnad** | Lav (kun pågående) | Middels | Høy | Middels–Høy |
| **Driftskostnad over tid** | Lav (men manglende etterlevelse) | Middels–Høy (doble standarder) | Middels (konsolidert) | Middels |
| **Risiko for forsinket etterlevelse** | Svært høy | Middels | Middels–Lav | Middels |
| **Risiko for EØS-rettslige sanksjoner** | Svært høy | Lav | Lav | Lav |
| **Nasjonal nytteverdi utover EHDS** | Ingen | Lav | Høy | Middels |
| **Kompleksitet** | Lav | Middels | Høy | Høy (koordinering) |
| **Gjenbruk av eksisterende løsninger** | Ja (uten tilpasning) | Høy | Middels (gradvis utfasing) | Middels–Høy |
| **Tidslinje for gruppe 1** | Ikke oppnåelig | Mars 2029 (stram) | Q4 2028 (margin) | Mars 2029 |
| **Tidslinje for gruppe 2** | Ikke oppnåelig | Mars 2031 (stram) | Mars 2031 (med margin) | Mars 2031 |
| **Ambisjonsnivå** | Ingen | Minimum etterlevelse | Bredere modernisering | Etterlevelse med nordisk samarbeid |
| **Endringsmotstand** | Lav | Middels | Høy | Middels |
| **Avhengighet av andre aktører** | Lav | Middels | Middels | Høy (nordisk enighet) |

### Anbefalt retning

Denne rapporten anbefaler ikke et bestemt alternativ, men peker på følgende vurderingspunkter for beslutningstakere:

1. **Nullalternativet er ikke reelt** dersom EHDS innlemmes i EØS-avtalen. Det fungerer kun som referansepunkt.

2. **Alternativ 1 er lavest risiko på kort sikt**, men skaper teknisk gjeld og doble standarder som øker kostnadene over tid. Det gir begrenset nasjonal nytteverdi utover det som er påkrevd.

3. **Alternativ 2 gir størst langsiktig verdi**, men krever politisk vilje til høyere investeringer, sterk programstyring og aksept for høyere gjennomføringsrisiko.

4. **Alternativ 3 kan kombineres** med enten alternativ 1 eller 2 som en tilleggsdimensjon. Nordisk samarbeid er verdifullt uavhengig av nasjonalt ambisjonsnivå, men bør ikke brukes som erstatning for nasjonale beslutninger og handlingsevne.

5. **En pragmatisk mellomvei** kan være å starte med alternativ 1 for å møte de første fristene, men med en tydelig plan for overgang til alternativ 2 etter hvert som erfaringsgrunnlaget og de europeiske spesifikasjonene modnes. Nordisk samarbeid (alternativ 3) bør uansett forfølges parallelt.

---

*Denne rapporten er basert på kunnskapsgrunnlaget (rapporter/kunnskapsgrunnlag-ehds.md) og problemdefinisjonen (rapporter/problemdefinisjon-ehds.md) for EHDS, utarbeidet 15. mars 2026. Tiltaksalternativene bør revideres når gjennomføringsrettsakter fra EU-kommisjonen vedtas, EØS-innlemmelse avklares, og mer detaljert informasjon om kostnader og leverandørkapasitet foreligger.*
