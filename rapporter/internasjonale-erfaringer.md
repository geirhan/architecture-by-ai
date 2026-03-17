# Delrapport 6: Internasjonale erfaringer med KI-støttet kunnskapsforvaltning i helse

## 1. Innledning

Denne delrapporten kartlegger internasjonale erfaringer med bruk av kunstig intelligens (KI) i kunnskapsforvaltning innen helsesektoren. Formålet er å identifisere relevante initiativ, trekke ut lærdommer og vurdere overførbarhet til norsk kontekst – spesielt med tanke på en ny verdikjede for kunnskapsforvaltning.

Rapporten dekker både etablerte rammeverk (WHO SMART Guidelines, NICE Evidence Standards Framework), pågående pilotprosjekter (Cochrane), nordiske erfaringer og fremvoksende initiativ fra teknologiselskaper og forlagsaktører. For hvert initiativ vurderes relevans, modenhet og hva Norge kan lære.

**Metodisk merknad:** Kartleggingen er basert på offentlig tilgjengelig dokumentasjon og publiserte rapporter. Flere av initiativene beskrevet her er under rask utvikling, og status kan ha endret seg siden kildene ble publisert. Usikkerhet er eksplisitt markert der det er relevant.

---

## 2. WHO SMART Guidelines

### Bakgrunn og motivasjon

WHO har utviklet SMART Guidelines som en systematisk tilnærming til digitalisering av kliniske retningslinjer. SMART står for **Standards-based, Machine-readable, Adaptive, Requirements-based, Testable**. Rammeverket ble utviklet fordi tradisjonelle retningslinjer i PDF- eller tekstformat har vist seg vanskelige å implementere konsistent i kliniske beslutningsstøttesystemer.

### Femstegsmodellen

SMART Guidelines følger en femstegsmodell for å transformere narrative anbefalinger til digitale artefakter:

1. **Narrative retningslinjer** – Tradisjonelle kliniske anbefalinger
2. **Semistrukturert innhold** – Beslutningslogikk og arbeidsflyter dokumenteres
3. **Maskinlesbare representasjoner** – Formalisering i standarder som FHIR og CQL (Clinical Quality Language)
4. **Eksekverbare spesifikasjoner** – Programvarenøytrale implementeringsguider
5. **Dynamiske, tilpasningsdyktige systemer** – Kontinuerlig oppdatering basert på ny evidens

Rammeverket er per i dag tilgjengelig for ni helseområder, inkludert svangerskapsomsorg, HIV, tuberkulose og immunisering.

### Maskinlesbare retningslinjer

Et sentralt bidrag fra WHO er demonstrasjonen av at FHIR-baserte implementeringsguider kan fungere som et programvarenøytralt format for retningslinjer. Dette muliggjør at ulike EPJ-leverandører kan implementere samme retningslinje uten å måtte utvikle egne tolkninger av det kliniske innholdet.

### Relevans for Norge og EHDS

WHO SMART Guidelines er særlig relevant for Norge av tre grunner:

- **FHIR-kompatibilitet:** Norge har allerede investert betydelig i HL7 FHIR som interoperabilitetsstandard, noe som gir et godt utgangspunkt for å ta i bruk maskinlesbare retningslinjer.
- **EHDS-kobling:** EHDS forutsetter økt datadeling på tvers av landegrenser. Maskinlesbare retningslinjer kan bidra til at beslutningsstøtte fungerer konsistent uavhengig av nasjonale EPJ-systemer.
- **Metodisk rammeverk:** Femstegsmodellen gir en konkret modenhetsmodell som norske aktører kan bruke for å vurdere hvor langt de er kommet i digitaliseringen av retningslinjer.

---

## 3. NICE (Storbritannia)

### Evidence Standards Framework for digitale helseteknologier

National Institute for Health and Care Excellence (NICE) i Storbritannia har utviklet et Evidence Standards Framework (ESF) for å evaluere digitale helseteknologier. Rammeverket ble oppdatert i 2022 for å adressere KI-spesifikke problemstillinger, inkludert adaptive algoritmer.

ESF klassifiserer digitale helseteknologier i funksjonskategorier med tilhørende krav til evidens. Teknologier med høyere risiko (for eksempel KI-basert diagnostikk) krever strengere evidens enn informasjonsverktøy. Oppdateringen i 2022 ble gjennomført i samarbeid med blant annet Imperial College London, University of Birmingham og Alan Turing Institute.

**Viktig presisering:** At en teknologi møter ESF-standardene betyr ikke at den har fått NICE-godkjenning. ESF er et vurderingsrammeverk, ikke en godkjenningsordning.

### NICEs tilnærming til KI i retningslinjer

NICE har begynt å utforske hvordan KI kan støtte retningslinjearbeidet internt. Dette inkluderer bruk av KI-verktøy for å akselerere evidensgjennomgang og identifisere relevante studier i store dokumentmengder. Tilnærmingen er gradvis og forsiktig, med vekt på transparens og menneskelig overstyring.

### Lessons learned

Erfaringene fra NICE peker på flere viktige lærdommer:

- **Tydelig klassifisering er nødvendig:** Ikke alle KI-systemer i helse krever samme evidensnivå. Et differensiert rammeverk reduserer unødvendige barrierer for lavrisikoteknologier.
- **Transparens og forklarbarhet:** NICE legger vekt på at KI-baserte anbefalinger skal kunne forklares for klinikere.
- **Iterativ oppdatering:** Rammeverket oppdateres jevnlig i takt med teknologisk utvikling, noe som er viktig gitt det raske tempoet i KI-feltet.

---

## 4. Cochrane – KI-piloter

### Bruk av KI i systematiske oversikter

Cochrane, som er den ledende internasjonale aktøren for produksjon av systematiske oversikter, har igangsatt flere pilotprosjekter for å undersøke hvordan KI kan effektivisere oversiktsprosessen. Systematiske oversikter er svært arbeidskrevende – en typisk oversikt tar 12–18 måneder å produsere.

### Automatisert screening og dataekstraksjon

De mest lovende anvendelsesområdene inkluderer:

- **Tittel- og abstraktscreening:** KI-verktøy brukes for å redusere antall artikler som må vurderes manuelt, typisk med 50–70 % tidsbesparelse. Verktøyene prioriterer artikler etter sannsynlighet for relevans.
- **Dataekstraksjon:** Semiautomatisk ekstraksjon av nøkkeldata fra inkluderte studier (studiepopulasjon, intervensjon, utfall).
- **Kvalitetsvurdering:** Foreløpige forsøk med KI-støttet vurdering av risiko for systematiske skjevheter (bias).

### Resultater og utfordringer

Resultatene er lovende, men det er viktige forbehold:

- **Sensitivitet versus spesifisitet:** I screening er det kritisk å ikke miste relevante studier. KI-verktøy må kalibreres for høy sensitivitet, noe som kan begrense tidsbesparelsen.
- **Faglig kontroll:** Cochrane understreker at KI-verktøyene støtter, men ikke erstatter, faglig vurdering. Alle KI-assisterte trinn gjennomgås av fagpersoner.
- **Reproduserbarhet:** Det er utfordringer knyttet til reproduserbarhet når KI-modeller oppdateres over tid.

### Implikasjoner for FHIs arbeid

Folkehelseinstituttet (FHI) produserer kunnskapsoppsummeringer og systematiske oversikter for norsk helsetjeneste. Cochranes erfaringer er direkte relevante:

- FHI kan vurdere å ta i bruk KI-støttet screening for å redusere tidsbruk i kunnskapsproduksjonen.
- Cochranes vektlegging av menneskelig overstyring er godt i tråd med FHIs etablerte metodetradisjon.
- FHI bør følge Cochranes arbeid med validering av KI-verktøy og eventuelt delta i internasjonale valideringsstudier.

---

## 5. Nordiske erfaringer

### Danmark

Sundhedsdatastyrelsen har arbeidet med standardisering av helsedata og har hatt fokus på sekundærbruk av helsedata. AI Danmark-initiativet har inkludert helse som et prioritert satsingsområde, med vekt på ansvarlig bruk av KI. Danmark har kommet relativt langt med sentral infrastruktur for helsedata (Sundhedsdatanettet), noe som gir et bedre grunnlag for KI-anvendelser enn i mer fragmenterte systemer.

*Usikkerhet: Detaljert informasjon om spesifikke KI-piloter innen kunnskapsforvaltning i dansk helsevesen har vært vanskelig å verifisere gjennom offentlig tilgjengelige kilder. Beskrivelsen baserer seg på overordnet informasjon.*

### Sverige

eHälsomyndigheten koordinerer digital helseutvikling i Sverige. Socialstyrelsen, som har ansvar for nasjonale retningslinjer, har begynt å utforske KI-støttet retningslinjearbeid. Sverige har en tradisjon for registerbasert forskning som gir et godt datagrunnlag for KI-utvikling, men retningslinjearbeidet er fortsatt i stor grad manuelt.

### Finland

Finland skiller seg ut med Kanta-systemet, en nasjonal infrastruktur for helsedata som dekker resepter, pasientjournaler og arkiv. Finlands nasjonale KI-strategi for helse inkluderer tiltak for sekundærbruk av helsedata (Findata) og utforsking av KI i klinisk beslutningsstøtte. Finlands tilnærming med sentral datainfrastruktur har potensielt overføringsverdi til Norge.

### Island

Island har en liten, men digitalt avansert helsesektor. Digital helsestrategi fokuserer på integrerte systemer og datadeling. Størrelsen gjør at implementering kan skje raskt, men erfaringene er vanskeligere å skalere til norske forhold.

### Samlet nordisk vurdering

De nordiske landene deler mange felles trekk: universelle helsesystemer, høy digital modenhet og sterke personverntradisjoner. Samtidig er det forskjeller i grad av sentralisering og infrastrukturmodenhet. Finland og Danmark har kommet lengst med sentral helsedata-infrastruktur, noe som gir bedre forutsetninger for KI-anvendelser. Norge har en mer fragmentert struktur, noe som representerer både en utfordring og et argument for å investere i felles arkitektur.

---

## 6. Andre relevante initiativ

### Store språkmodeller i medisinsk kontekst

Store språkmodeller (LLM-er) fra aktører som OpenAI og Google har vist oppsiktsvekkende ytelse på medisinske benchmarks. Googles Med-PaLM 2 oppnådde i 2023 resultater på nivå med ekspertnivå på den amerikanske medisinske lisensieringseksamen (USMLE). OpenAIs GPT-4 har vist tilsvarende resultater.

**Viktig forbehold:** Ytelse på standardiserte tester oversettes ikke direkte til klinisk nytteverdi. Utfordringer inkluderer hallusinering (fabrikering av fakta), manglende oppdatering med ny evidens, og begrenset tilpasning til lokale retningslinjer og praksis. Disse verktøyene er per i dag best egnet som støtteverktøy for fagpersoner, ikke som autonome beslutningsverktøy.

### Forlagsaktører og KI-støttet kunnskapsproduksjon

Elsevier (del av RELX Group) har investert betydelig i KI-støttet kunnskapsproduksjon, inkludert verktøy for automatisert litteratursøk, datautvinning og kunnskapsgrafer. Disse verktøyene er primært rettet mot forskere og kunnskapsprodusenter, men har potensielle anvendelser for retningslinjearbeid.

### Living guidelines-bevegelsen

Australia har vært en pioner innen «living guidelines» – retningslinjer som oppdateres kontinuerlig i stedet for periodisk. Australian Living Evidence Consortium har utviklet metoder og infrastruktur for dette. WHO har også tatt i bruk living guidelines for utvalgte emner. KI-støttet overvåking av ny evidens er en nøkkelkomponent som gjør kontinuerlig oppdatering praktisk gjennomførbar.

Living guidelines-konseptet er svært relevant for norsk kunnskapsforvaltning, da det adresserer et kjent problem med at retningslinjer kan bli utdaterte mellom revisjonssykluser.

---

## 7. Overførbarhet til Norge

### WHO SMART Guidelines

| Aspekt | Vurdering |
|--------|-----------|
| **Relevans** | Høy. Norge har allerede FHIR-kompetanse og -infrastruktur. |
| **Hva kan Norge lære?** | Femstegsmodellen som modenhetsrammeverk. Programvarenøytral tilnærming til maskinlesbare retningslinjer. |
| **Hva er ulikt?** | WHO fokuserer primært på lav- og mellominntektsland. Norsk helsesektor har mer komplekse EPJ-systemer. |
| **Konkret adopsjon** | Pilotere SMART Guidelines-tilnærmingen for utvalgte nasjonale retningslinjer. Vurdere bruk av CQL for beslutningslogikk. |

### NICE Evidence Standards Framework

| Aspekt | Vurdering |
|--------|-----------|
| **Relevans** | Høy. Norge trenger tilsvarende rammeverk for vurdering av KI-teknologier i helse. |
| **Hva kan Norge lære?** | Differensiert klassifisering av digitale helseteknologier etter risikonivå. Iterativ oppdatering av rammeverk. |
| **Hva er ulikt?** | NICE har en mer sentral rolle i teknologivurdering enn noen enkelt norsk aktør. NHS er mer sentralisert enn norsk helsetjeneste. |
| **Konkret adopsjon** | Helsedirektoratet kan vurdere å utvikle et tilsvarende nasjonalt rammeverk, tilpasset norsk regulering og EU AI Act. |

### Cochrane KI-piloter

| Aspekt | Vurdering |
|--------|-----------|
| **Relevans** | Høy for FHI og kunnskapsproduksjonsmiljøer. |
| **Hva kan Norge lære?** | Hvilke trinn i systematisk oversiktsproduksjon som egner seg best for KI-støtte. Validerings- og kvalitetssikringsmetoder. |
| **Hva er ulikt?** | Cochrane har større volum og internasjonalt nedslagsfelt. FHI opererer i norsk kontekst med egne prioriteringskriterier. |
| **Konkret adopsjon** | FHI kan pilotere KI-støttet screening i utvalgte kunnskapsoppsummeringer, med Cochranes metoder som utgangspunkt. |

### Nordiske erfaringer

| Aspekt | Vurdering |
|--------|-----------|
| **Relevans** | Høy, gitt likheter i helsesystemer og regulering. |
| **Hva kan Norge lære?** | Finlands sentraliserte datainfrastruktur (Kanta/Findata). Danmarks tilnærming til helsedata-standardisering. |
| **Hva er ulikt?** | Ulik grad av sentralisering. Norge har et mer fragmentert helsedata-landskap. |
| **Konkret adopsjon** | Etablere nordisk erfaringsutveksling om KI i kunnskapsforvaltning. Vurdere Findata-modellen for sekundærbruk av data. |

### Living guidelines

| Aspekt | Vurdering |
|--------|-----------|
| **Relevans** | Svært høy. Adresserer et konkret problem i norsk retningslinjearbeid. |
| **Hva kan Norge lære?** | Metoder for kontinuerlig evidensovervåking. Infrastruktur for oppdatering av retningslinjer. |
| **Hva er ulikt?** | Australsk helsetjeneste har annen struktur, men metodene er overførbare. |
| **Konkret adopsjon** | Pilotere living guidelines-tilnærmingen for utvalgte retningslinjer, med KI-støttet evidensovervåking. |

---

## 8. Oppsummering og nøkkelfunn

### Trender på tvers av land

1. **Fra periodisk til kontinuerlig oppdatering:** Flere land beveger seg mot living guidelines og kontinuerlig evidensovervåking.
2. **Maskinlesbarhet som mål:** WHO, NICE og flere nasjonale aktører arbeider mot maskinlesbare retningslinjer, med FHIR som sentral standard.
3. **KI som støtteverktøy, ikke erstatning:** Ingen av de kartlagte initiativene erstatter faglig vurdering med KI. KI brukes for effektivisering og kvalitetsstøtte.
4. **Differensiert regulering:** Det er en internasjonal trend mot risikobasert regulering av KI i helse, i tråd med EU AI Act.
5. **Sentral infrastruktur som forutsetning:** Land med mer sentralisert helsedata-infrastruktur (Finland, Danmark) har bedre forutsetninger for KI-anvendelser.

### Felles utfordringer

- **Kvalitetssikring:** Hvordan validere KI-genererte bidrag i kunnskapsproduksjonen?
- **Reproduserbarhet:** KI-modeller endrer seg over tid, noe som utfordrer reproduserbarhet i vitenskapelig arbeid.
- **Kompetanse:** Behov for tverrfaglig kompetanse som kombinerer klinisk kunnskap, informatikk og KI.
- **Personvern og etikk:** Balanse mellom datautnyttelse og personvern, særlig ved sekundærbruk av helsedata.
- **Leverandøravhengighet:** Risiko for å bli avhengig av proprietære KI-løsninger fra store teknologiselskaper.

### Beste praksis som bør vurderes i norsk sammenheng

1. **Adopt WHO SMART Guidelines-tilnærmingen** for strukturering av nasjonale retningslinjer, med prioriterte pilotområder.
2. **Utvikle et nasjonalt rammeverk** for evaluering av KI-teknologier i helse, inspirert av NICE ESF og tilpasset EU AI Act.
3. **Pilotere KI-støttet kunnskapsproduksjon** i samarbeid mellom FHI, Helsedirektoratet og akademiske miljøer, med Cochranes metoder som referanse.
4. **Etablere nordisk samarbeid** om KI i kunnskapsforvaltning for å dele erfaringer og redusere duplisert arbeid.
5. **Utforske living guidelines-modellen** for utvalgte retningslinjer der evidensgrunnlaget endres raskt.
6. **Investere i sentral infrastruktur** for helsedata som grunnlag for KI-anvendelser, med lærdommer fra Finland og Danmark.

---

*Denne rapporten er del av en utredning om ny verdikjede for kunnskapsforvaltning i helsesektoren. Vurderingene er basert på offentlig tilgjengelig dokumentasjon og må ses i sammenheng med de øvrige delrapportene i utredningen.*

**Kilder:**
- WHO SMART Guidelines: https://www.who.int/teams/digital-health-and-innovation/smart-guidelines
- NICE Evidence Standards Framework: https://www.nice.org.uk/about/what-we-do/our-programmes/evidence-standards-framework-for-digital-health-technologies
- Cochrane – KI og systematiske oversikter: https://www.cochrane.org/news/artificial-intelligence-and-evidence-synthesis
