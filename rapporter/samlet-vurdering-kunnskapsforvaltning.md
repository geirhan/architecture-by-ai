# Delrapport 7: Samlet vurdering og anbefaling

Del av utredning om ny verdikjede for kunnskapsforvaltning
i helsesektoren

---

## 1. Ledersammendrag

### Bakgrunn

Helsedirektoratet har gjennomført denne utredningen for å
vurdere om og hvordan verdikjeden for kunnskapsforvaltning
i helsesektoren bør moderniseres. Verdikjeden dekker hele
løpet fra internasjonal forskning til kvalitetssikret
helseinformasjon til innbyggere, og involverer FHI,
Helsedirektoratet, Norsk helsenett (NHN), de regionale
helseforetakene og KS.

Utredningen er motivert av tre samtidige utviklingstrekk:
(1) forskningsproduksjonen øker eksponentielt og overgår
kapasiteten for manuell bearbeiding,
(2) innbyggere i økende grad søker helseinformasjon fra
kommersielle KI-tjenester uten kvalitetssikring, og
(3) nye regulatoriske rammer gjennom EU AI Act og EHDS
stiller krav til digital modenhet.

### Hovedfunn

**Dagens verdikjede er ikke bærekraftig.**
Gjennomløpstiden fra ny forskning til oppdatert
innbyggerinformasjon er 2-6,5 år (delrapport 1).
De tre mest alvorlige flaskehalsene er foreldelse av
kunnskapsgrunnlaget underveis i retningslinjeprosessen,
kapasitetsbegrensning for systematiske oversikter, og
manglende kobling mellom retningslinjer og
innbyggerinformasjon (delrapport 2).

**KI-teknologi kan adressere flaskehalsene.** Store
språkmodeller (LLM) kan akselerere kunnskapssyntese,
støtte retningslinjeutvikling, forbedre
innbyggerinformasjon og muliggjøre kontinuerlig
oppdatering. Samtidig medfører teknologien risikoer
knyttet til hallusinering, tillit, bias og personvern.
EU AI Act klassifiserer KI i helse som høyrisiko
(delrapport 3).

**Internasjonale erfaringer støtter en faseinndelt
tilnærming.** WHO SMART Guidelines, NICE, Cochrane og
nordiske land viser at KI som støtteverktøy med
menneskelig kontroll gir resultater, mens autonome
KI-systemer i helse fortsatt er umodne (delrapport 6).

### Anbefaling

Utredningen anbefaler en **faseinndelt innføring av
KI-støttet kunnskapsforvaltning** over tre faser i løpet
av 0-48 måneder, med alternativ 1 (moderat KI-støtte)
som startpunkt og gradvis utvidelse mot alternativ 2
(ambisiøs KI-pipeline).

### Nøkkeltall

<!-- markdownlint-disable MD013 -->

| Indikator | Dagens situasjon | Med anbefalt tiltak |
| --- | --- | --- |
| Gjennomløpstid forskning-innbygger | 2-6,5 år | 1-3 år (fase 1-2), uker-måneder (fase 3) |
| Estimert tidsbesparelse | N/A | 40-60 % (fase 1-2), 70-90 % (fase 3) |
| Investeringskostnad (fase 1-2) | N/A | 20-50 MNOK over 2-3 år |
| Investeringskostnad (inkl. fase 3) | N/A | 100-250 MNOK over 4-6 år |
| Kvalitetsrisiko | Lav (etablerte prosesser, men utdatert innhold) | Lav-moderat (fase 1-2), moderat-høy (fase 3) |

<!-- markdownlint-enable MD013 -->

*Merknad: Kostnadsestimatene har vesentlig usikkerhet
og bør verifiseres gjennom detaljerte
kost-nytte-analyser.*

### Konsekvens av å ikke handle

Nullalternativet (videreføring uten endring) er ikke
bærekraftig på mellomlang sikt (3-5 år). Konsekvensene
inkluderer: økende gap mellom tilgjengelig kunnskap og
formidlet informasjon, tap av innbyggernes tillit til
offentlig helseinformasjon i konkurranse med kommersielle
KI-tjenester, risiko for manglende EHDS-samsvar, og
kompetanseflukt fra offentlig sektor.

### Målgruppe

Denne rapporten er rettet mot Helse- og
omsorgsdepartementet (HOD), Helsedirektoratets ledelse,
de regionale helseforetakene, KS og Norsk helsenett.

---

## 2. Innledning

### 2.1 Utredningens oppdrag og formål

Utredningen har som formål å vurdere hvordan verdikjeden
for kunnskapsforvaltning i helsesektoren kan moderniseres
for å sikre at innbyggere og helsepersonell får tilgang
til oppdatert, kvalitetssikret helseinformasjon innenfor
akseptable tidsrammer. Utredningen er strukturert etter
utredningsinstruksens minimumskrav.

### 2.2 Oversikt over delrapporter

Utredningen består av syv delrapporter:

<!-- markdownlint-disable MD013 -->

| Nr. | Tittel | Innhold |
| ----- | -------- | --------- |
| 1 | Dagens verdikjede | Kartlegging av verdikjeden fra forskning til innbygger i fem steg |
| 2 | Utfordringer og flaskehalser | Analyse av åtte rangerte flaskehalser og konsekvenser |
| 3 | Store språkmodeller - muligheter og risikoer | Balansert vurdering av LLM-teknologi i helsekontekst |
| 4 | Alternativer for ny verdikjede | Tre alternativer med kostnads- og risikovurdering |
| 5 | Arkitektur og komponenter | Teknisk og organisatorisk arkitektur med ArchiMate |
| 6 | Internasjonale erfaringer | WHO, NICE, Cochrane, nordiske land og living guidelines |
| 7 | Samlet vurdering og anbefaling | Denne rapporten |

<!-- markdownlint-enable MD013 -->

Denne samlerapporten syntetiserer funn fra alle
delrapportene og gir en helhetlig anbefaling.

---

## 3. Sammendrag av funn fra delrapporter

### Delrapport 1: Dagens verdikjede

Verdikjeden fra forskning til innbygger består av fem
hovedsteg: (1) internasjonal forskning,
(2) systematiske oversikter ved FHI,
(3) retningslinjeutvikling ved Helsedirektoratet,
(4) kunnskapsformidling via Helsebiblioteket, og
(5) innbyggerinformasjon via helsenorge.no.
Total gjennomløpstid estimeres til 2-6,5 år avhengig
av scenario.

Kartleggingen viser at verdikjeden preges av manuelle
overganger, fragmentert ansvar og begrenset strukturering
av innhold. Kvalitetssikringen er robust innenfor hvert
steg, men det finnes ingen systematisk mekanisme som
sikrer sammenheng på tvers av stegene. Innholdet er i
stor grad fritekstbasert, noe som begrenser mulighetene
for automatisert videreforedling.

### Delrapport 2: Utfordringer og flaskehalser

Analysen identifiserer åtte rangerte flaskehalser. De
tre mest alvorlige er: (1) foreldelse av
kunnskapsgrunnlaget underveis i retningslinjeprosessen,
der ny forskning kan endre evidensgrunnlaget vesentlig
før retningslinjen ferdigstilles,
(2) kapasitetsbegrensning for systematiske oversikter,
der forskningsvolumet langt overstiger FHIs kapasitet
for manuell screening, og (3) manglende kobling mellom
retningslinjer og innbyggerinformasjon, der oppdatering
skjer manuelt og ad hoc.

Strukturelle utfordringer inkluderer siloorganisering
mellom aktører, manglende standardisert
informasjonsflyt, dobbeltarbeid og fragmenterte
IT-systemer. Konsekvensene er utdaterte helseråd, at
innbyggere søker alternative kilder med variabel
kvalitet, og et økende gap mellom tilgjengelig og
formidlet kunnskap.

### Delrapport 3: Store språkmodeller - muligheter og risikoer

LLM-teknologi har potensial til å akselerere
kunnskapssyntese (50-80 % tidsbesparelse i screening),
støtte retningslinjeutvikling, forbedre
innbyggerinformasjon gjennom klarspråk-oversettelse, og
muliggjøre living guidelines. Samtidig medfører
teknologien risikoer: hallusinering (generering av
plausible, men feilaktige utsagn), utfordringer med
tillit og legitimitet, bias fra treningsdata,
personvernhensyn ved skybaserte tjenester, og juridisk
usikkerhet.

EU AI Act klassifiserer KI i helse som høyrisiko og
stiller krav til risikostyring, datakvalitet,
transparens, menneskelig tilsyn og logging. Trinnvis
ikrafttredelse frem til 2027 gir et tidsvindu for
forberedelse. Rapporten konkluderer med at nøkkelen
ligger i governance, kvalitetssikring og menneskelig
tilsyn.

### Delrapport 4: Alternativer for ny verdikjede

Tre alternativer vurderes. Alternativ 0
(nullalternativet) viderefører dagens praksis og
vurderes som ikke bærekraftig. Alternativ 1 (moderat
KI-støtte) innfører KI som støtteverktøy med
menneskelig kontroll, gir 40-60 % tidsbesparelse til
en investeringskostnad på 20-50 MNOK. Alternativ 2
(ambisiøs KI-pipeline) innebærer living guidelines,
personaliserte helseråd og EHDS-integrasjon, med
70-90 % tidsbesparelse og investeringskostnad på
100-250 MNOK.

Anbefalingen er en faseinndelt tilnærming der
alternativ 1 implementeres først, med gradvis utvidelse
mot alternativ 2. Governance-modellen spesifiserer
roller for Helsedirektoratet (overordnet governance),
FHI (KI-støttet kunnskapssyntese), NHN (drift av
infrastruktur) og fageksperter (validering).

### Delrapport 5: Arkitektur og komponenter

Arkitekturen er beskrevet med ArchiMate i tre lag. Seks
kjernekomponenter identifiseres:
kunnskapssyntese-motor, retningslinjestøttesystem,
kunnskapsformidlingsplattform, innbygger-chatbot,
kvalitetssikringsmodul og kunnskapsbase. Arkitekturen
bygger på FHIR for interoperabilitet, HelseID for
autentisering, og NHN-infrastruktur for drift.
EHDS-kobling ivaretas gjennom FHIR-baserte grensesnitt
og MyHealth@EU-integrasjon.

Sentrale arkitekturprinsipper er åpenhet og
transparens, modularitet, gjenbruk av nasjonale
felleskomponenter, sikkerhet by design, skalerbarhet
og leverandøruavhengighet.

### Delrapport 6: Internasjonale erfaringer

Kartleggingen viser fem internasjonale trender:
(1) bevegelse fra periodisk til kontinuerlig
oppdatering, (2) maskinlesbarhet som mål med FHIR som
standard, (3) KI som støtteverktøy med menneskelig
kontroll, (4) differensiert risikobasert regulering, og
(5) sentral infrastruktur som forutsetning.
WHO SMART Guidelines gir et modenhetssrammeverk for
maskinlesbare retningslinjer. NICE ESF tilbyr et
differensiert rammeverk for vurdering av
KI-teknologier. Cochranes piloter demonstrerer
50-70 % tidsbesparelse i screening. Nordiske land viser
at Finland og Danmark har kommet lengst med sentral
infrastruktur.

---

## 4. Helhetlig problemanalyse

### 4.1 Sammenstilling av utfordringene

Utredningen avdekker et mønsterbilde der utfordringene
forsterker hverandre. Lang gjennomløpstid (delrapport 1)
skyldes både kapasitetsbegrensninger og prosessdesign
(delrapport 2). Mangel på strukturerte data og
standardiserte grensesnitt (delrapport 1, 2) forhindrer
automatisering og sporbarhet. Siloorganisering
(delrapport 2) gjør det vanskelig å optimalisere
verdikjeden som helhet. Samtidig akselererer
forskningsproduksjonen og innbyggernes forventninger
til oppdatert informasjon.

### 4.2 Kjerneproblemet

Kjerneproblemet er at **verdikjeden er designet for en
pre-digital tid**. Prosessene, organisasjonsstrukturene
og verktøyene ble utviklet i en æra med lavere
forskningsvolum, der manuell bearbeiding var den eneste
tilgjengelige metoden. Denne strukturen har tjent
sektoren godt, men den skalerer ikke til dagens og
fremtidens kunnskapsvolum.

Verdikjeden mangler tre sentrale egenskaper:

- **Skalerbarhet**: Kapasiteten øker ikke i takt med
  forskningsvolumet.
- **Reaktivitet**: Gjennomløpstiden gjør det umulig å
  respondere raskt på ny evidens.
- **Sammenheng**: Stegene i verdikjeden er ikke koblet
  på en måte som sikrer konsistent og oppdatert
  informasjon gjennom hele kjeden.

### 4.3 Implikasjoner av å videreføre status quo

Dersom dagens verdikjede videreføres uten endring, vil
følgende konsekvenser med høy sannsynlighet inntreffe
i løpet av 3-5 år:

1. **Kunnskapsgapet øker.** Akselererende
   forskningsproduksjon betyr at en stadig større andel
   av tilgjengelig kunnskap aldri når inn i den
   offisielle verdikjeden.
2. **Kommersielle KI-tjenester tar over.** Innbyggere
   bruker allerede ChatGPT, Gemini og lignende tjenester
   for helseinformasjon. Uten et kvalitetssikret
   offentlig alternativ vil denne trenden akselerere.
3. **Regulatorisk etterslep.** EHDS og EU AI Act
   forutsetter digital modenhet som dagens verdikjede
   ikke har.
4. **Tillitserodering.** Dersom offentlig
   helseinformasjon oppleves som utdatert sammenlignet
   med kommersielle alternativer, kan det undergrave
   tilliten til helsemyndighetene.

---

## 5. Anbefaling

### 5.1 Overordnet anbefaling

Det anbefales en **faseinndelt innføring av KI-støttet
kunnskapsforvaltning** der alternativ 1 (moderat
KI-støtte) implementeres som startpunkt, med gradvis
utvidelse mot elementer fra alternativ 2 etter hvert
som teknologi, kompetanse og governance modnes.
Tilnærmingen balanserer behovet for modernisering mot
risikoen for feilslått implementering.

### 5.2 Fase 1: Pilotering (0-18 måneder)

**Målsetning:** Bevise konseptet og bygge grunnlaget.

- KI-assistert screening av forskningslitteratur ved
  FHI (pilot på 2-3 fagområder)
- KI-assistert oversettelse av retningslinjer til
  klarspråk/innbyggerspråk (pilot)
- Etablering av governance-rammeverk og kvalitetskrav
  for KI-bruk
- Kompetanseheving hos nøkkelpersonell i FHI,
  Helsedirektoratet og NHN
- Evaluering av pilotresultater som grunnlag for videre
  beslutning
- Juridisk avklaring av forholdet mellom KI-generert
  helseinnhold og EU AI Act

**Estimert kostnad:** 5-15 MNOK. **Risiko:** Lav.

### 5.3 Fase 2: Utvidelse (12-36 måneder)

**Målsetning:** Skalere det som virker og utvide
funksjonaliteten.

- Skalering av KI-støttet screening til alle fagområder
  ved FHI
- KI-støttede utkast til systematiske oversikter
- Implementering av automatisk evidensvarsling for
  eksisterende retningslinjer
- Pilotering av KI-chatbot på helsenorge.no med RAG mot
  verifiserte kunnskapskilder
- Etablering av kunnskapsbase med strukturerte metadata
  og FHIR-grensesnitt
- Videreutvikling av governance basert på erfaringer
  fra fase 1

**Estimert kostnad:** 15-35 MNOK. **Risiko:** Moderat.

### 5.4 Fase 3: Transformasjon (24-48 måneder)

**Målsetning:** Transformere verdikjeden og koble til
europeisk infrastruktur.

- Overgang til living guidelines på utvalgte fagområder
- Full pipeline fra evidensovervåking til publisert
  innbyggerinformasjon med KI-støtte
- Integrasjon med EHDS-infrastruktur og MyHealth@EU
- Pilotering av personaliserte helseråd (avhengig av
  regulatorisk avklaring)
- Etablering av feedback-loop fra klinisk praksis
- Flerspråklig, multimodal formidling av
  helseinformasjon

**Estimert kostnad:** 80-200 MNOK.
**Risiko:** Moderat-høy.

*Merknad: Fase 3 representerer et langsiktig mål som
forutsetter vellykket gjennomføring av fase 1 og 2,
samt at teknologien modnes ytterligere.
Kostnadsestimatet har høy usikkerhet.*

### 5.5 Samlet kostnadsramme

<!-- markdownlint-disable MD013 -->

| Fase | Periode | Estimert kostnad | Usikkerhet |
| ------ | --------- | ----------------- | ------------ |
| Fase 1: Pilotering | 0-18 mnd | 5-15 MNOK | Moderat |
| Fase 2: Utvidelse | 12-36 mnd | 15-35 MNOK | Moderat-høy |
| Fase 3: Transformasjon | 24-48 mnd | 80-200 MNOK | Høy |
| **Totalt** | **0-48 mnd** | **100-250 MNOK** | **Høy** |

<!-- markdownlint-enable MD013 -->

Kostnadsestimatene inkluderer utvikling, anskaffelse,
kompetanseheving og organisasjonsutvikling.
Driftskostnader kommer i tillegg. Estimatene er grove
og bør verifiseres gjennom detaljerte
kost-nytte-analyser for hver fase.

### 5.6 Organisatoriske forutsetninger

Vellykket gjennomføring forutsetter:

1. **Tydelig oppdrag fra HOD** med tilhørende
   finansiering og mandat
2. **Tverrsektoriell forankring** mellom
   Helsedirektoratet, FHI og NHN med felles
   forståelse av mål og ansvarsfordeling
3. **Kompetanseinvestering** i KI-forståelse og -bruk
   hos fagpersoner, samt rekruttering av teknisk
   kompetanse
4. **Regulatorisk proaktivitet** der Helsedirektoratet
   tar en ledende rolle i å operasjonalisere EU AI Act
   for helsesektoren
5. **Iterativ tilnærming** der hver fase evalueres
   før neste fase starter, med involvering av
   fagpersoner og innbyggere
6. **Realistiske forventninger** om at KI er et
   støtteverktøy, ikke en erstatning for faglig
   kompetanse

---

## 6. Risikomatrise

Tabellen nedenfor oppsummerer de ti viktigste risikoene
for KI-støttet kunnskapsforvaltning, med vurdering av
sannsynlighet, konsekvens og foreslåtte
mitigeringstiltak.

<!-- markdownlint-disable MD013 -->

| Nr. | Risiko | Sannsynlighet | Konsekvens | Samlet risiko | Mitigering |
| ----- | -------- | --------------- | ------------ | --------------- | ------------ |
| 1 | Hallusinering i KI-generert helseinnhold | Høy | Høy | **Kritisk** | RAG mot verifiserte kilder, automatisert faktasjekk, menneskelig validering før publisering, hallusinerings-deteksjon |
| 2 | Tap av tillit til offentlig helseinformasjon | Middels | Høy | **Høy** | Transparent kommunikasjon om KI-bruk, tydelig faglig ansvar, gradvis innføring med evaluering |
| 3 | Personvernbrudd | Lav | Høy | **Moderat** | DPIA før publisering, dataminimering, norsk jurisdiksjon for datalagring, databehandleravtaler |
| 4 | Implementeringsforsinkelser | Høy | Middels | **Høy** | Faseinndelt tilnærming, tydelige milepæler, risikobasert prioritering |
| 5 | Teknologiavhengighet/leverandørlåsing | Middels | Middels | **Moderat** | Abstraksjonslag mot KI-modeller, åpne standarder, leverandøruavhengig arkitektur |
| 6 | Regulatorisk usikkerhet (EU AI Act) | Middels | Middels | **Moderat** | Proaktiv dialog med tilsynsmyndigheter, juridisk kompetanse, følge europeisk rettsutvikling |
| 7 | Organisatorisk motstand | Middels | Middels | **Moderat** | Involvering av berørt personell fra start, kompetanseheving, tydelig kommunikasjon om at KI støtter, ikke erstatter |
| 8 | Kompetansemangel | Høy | Middels | **Høy** | Langsiktig kompetansestrategi, rekruttering, samarbeid med universitetsmiljøer |
| 9 | Budsjettoverskridelser | Middels | Middels | **Moderat** | Faseinndelt investering med evaluering, grove estimater som oppdateres per fase |
| 10 | Innbyggere bruker ukvalifiserte KI-kilder | Høy | Høy | **Kritisk** | Proaktivt tilby kvalitetssikret KI-basert helseinformasjon, chatbot på helsenorge.no, synlighet i søkeresultater |

<!-- markdownlint-enable MD013 -->

**Oppsummering av risikobildet:**

To risikoer vurderes som kritiske: hallusinering i
helseinnhold og at innbyggere søker ukvalifiserte
KI-kilder. Begge adresseres direkte av den anbefalte
tilnærmingen: hallusinering gjennom robust
kvalitetssikring, og konkurranserisikoen gjennom å tilby
et kvalitetssikret offentlig alternativ.

Tre risikoer vurderes som høye: tap av tillit,
implementeringsforsinkelser og kompetansemangel. Disse
krever aktiv styring gjennom hele gjennomføringsperioden.

---

## 7. Fremdriftsplan

### 7.1 Overordnet tidslinje

<!-- markdownlint-disable MD013 -->

| Aktivitet | Fase | Tidsrom | Ansvarlig | Avhengigheter |
| ------------- | ------ | --------- | ------------- | --------------- |
| **Fase 1: Pilotering** | | **0-18 mnd** | | |
| Oppdrag og finansiering fra HOD | 1 | Mnd 0-3 | HOD | Politisk beslutning |
| Etablere governance-rammeverk | 1 | Mnd 1-6 | Helsedirektoratet | Oppdrag fra HOD |
| KI-screening pilot ved FHI (2-3 fagområder) | 1 | Mnd 3-15 | FHI | Governance-rammeverk |
| KI-klarspråk pilot | 1 | Mnd 6-15 | Helsedirektoratet/NHN | Governance-rammeverk |
| Kompetanseheving nøkkelpersonell | 1 | Mnd 3-18 | Alle aktører | Budsjett |
| Juridisk avklaring EU AI Act | 1 | Mnd 1-12 | Helsedirektoratet | - |
| **Milepæl M1:** Pilotevaluering og beslutning om fase 2 | 1 | Mnd 18 | Helsedirektoratet | Pilotresultater |
| **Fase 2: Utvidelse** | | **12-36 mnd** | | |
| Skalere KI-screening til alle fagområder | 2 | Mnd 12-24 | FHI | M1 |
| KI-støttede systematiske oversikter | 2 | Mnd 15-30 | FHI | M1 |
| Automatisk evidensvarsling | 2 | Mnd 18-30 | FHI/NHN | Kunnskapsbase |
| KI-chatbot pilot på helsenorge.no | 2 | Mnd 18-36 | NHN | Kunnskapsbase, governance |
| Etablere kunnskapsbase med FHIR | 2 | Mnd 12-30 | NHN | Arkitektur |
| **Milepæl M2:** Evaluering og beslutning om fase 3 | 2 | Mnd 36 | Helsedirektoratet | Fase 2-resultater |
| **Fase 3: Transformasjon** | | **24-48 mnd** | | |
| Living guidelines pilot | 3 | Mnd 24-42 | Helsedirektoratet/FHI | M2 |
| EHDS-integrasjon | 3 | Mnd 30-48 | NHN | Kunnskapsbase, EHDS-tidsplan |
| Personaliserte helseråd pilot | 3 | Mnd 36-48 | NHN/Helsedirektoratet | Regulatorisk avklaring |
| Flerspråklig formidling | 3 | Mnd 30-42 | NHN | Kunnskapsformidlingsplattform |
| **Milepæl M3:** Full operativ drift | 3 | Mnd 48 | Alle aktører | Alle faser |

<!-- markdownlint-enable MD013 -->

### 7.2 Kritiske avhengigheter

- **Fase 2 avhenger av fase 1:** Beslutning om
  skalering forutsetter vellykket pilotering og
  positiv evaluering.
- **Fase 3 avhenger av fase 2:** Transformative
  elementer som living guidelines krever at
  grunnleggende infrastruktur (kunnskapsbase,
  KI-pipeline) er på plass.
- **EHDS-integrasjon avhenger av europeisk tidsplan:**
  Norges mulighet for å integrere med
  EHDS-infrastrukturen er avhengig av fremdriften i
  europeisk implementering.
- **Regulatorisk avklaring er tverrgående:** EU AI Acts
  trinnvise ikrafttredelse (2025-2027) påvirker alle
  faser.

---

## 8. Samsvar med utredningsinstruksen

Utredningen svarer på utredningsinstruksens seks
minimumskrav:

### Krav 1: Problemet og målet

**Problemet:** Verdikjeden for kunnskapsforvaltning i
helsesektoren har en gjennomløpstid på 2-6,5 år fra ny
forskning til oppdatert innbyggerinformasjon.
Verdikjeden skalerer ikke med økende forskningsvolum,
og innbyggere søker i økende grad helseinformasjon fra
ukvalifiserte kilder. (Delrapport 1 og 2.)

**Målet:** Redusere gjennomløpstiden vesentlig
(40-90 %), øke kapasiteten for kunnskapsproduksjon,
sikre at offentlig helseinformasjon er oppdatert og
tilgjengelig, og posisjonere Norge for EHDS-samsvar.

### Krav 2: Relevante tiltak

Tre alternativer er vurdert (delrapport 4):

- Alternativ 0: Videreføring uten endring
  (ikke bærekraftig)
- Alternativ 1: Moderat KI-støtte med menneskelig
  kontroll (anbefalt startpunkt)
- Alternativ 2: Ambisiøs KI-pipeline med living
  guidelines (langsiktig mål)

### Krav 3: Prinsipielle spørsmål

Utredningen adresserer flere prinsipielle spørsmål
(delrapport 3):

- Bør offentlige helsemyndigheter bruke KI i
  kunnskapsproduksjon?
- Hvor går grensen mellom KI-støtte og KI-autonomi?
- Hvem har ansvar når KI bidrar til feilaktige
  helseråd?
- Hvordan sikre demokratisk kontroll over KI i helse?
- Bør Norge utvikle egne modeller eller bruke
  kommersielle?

### Krav 4: Berørte parter

Berørte parter er kartlagt (delrapport 1 og 4):

- **HOD** som oppdragsgiver og politisk styringsnivå
- **Helsedirektoratet** som fagmyndighet og
  retningslinjeeier
- **FHI** som kunnskapsprodusent
- **NHN** som tjenesteleverandør
- **RHF-ene** som implementører i
  spesialisthelsetjenesten
- **KS og kommunene** som implementører i
  primærhelsetjenesten
- **Innbyggere** som sluttbrukere av helseinformasjon
- **Helsepersonell** som brukere av retningslinjer og
  fagkunnskap

### Krav 5: Anbefalt tiltak

Faseinndelt innføring av KI-støttet
kunnskapsforvaltning over tre faser (0-48 måneder),
med alternativ 1 som startpunkt. Se kapittel 5.

### Krav 6: Forutsetninger for vellykket gjennomføring

Seks forutsetninger er identifisert (kapittel 5.6):
tydelig oppdrag fra HOD, tverrsektoriell forankring,
kompetanseinvestering, regulatorisk proaktivitet,
iterativ tilnærming og realistiske forventninger.

---

## 9. Avsluttende merknad

### 9.1 Usikkerhet og begrensninger

Denne utredningen har vesentlige begrensninger som
leseren bør være oppmerksom på:

**Teknologisk usikkerhet.** KI-teknologi er i rask
utvikling. Estimater for ytelse, kostnad og
tidsbesparelse er basert på dagens teknologinivå og
tidlige erfaringer. Faktisk utvikling kan avvike
både positivt og negativt.

**Kostnadsusikkerhet.** Kostnadsestimatene er grove
(størrelsesorden) og har betydelig usikkerhet, særlig
for fase 3. Detaljerte kost-nytte-analyser bør
gjennomføres for hver fase.

**Regulatorisk usikkerhet.** EU AI Act er nylig trådt
i kraft, og tolkningen for helsedomenet er ikke fullt
avklart. Forholdet mellom KI-generert helseinformasjon
og medisinsk utstyr-forordningen (MDR) er et uavklart
grenseområde.

**Begrenset empirisk grunnlag.** Flere av de
internasjonale erfaringene (delrapport 6) er fra
pilotprosjekter, ikke fullskala implementeringer.
Overførbarhet til norsk kontekst er vurdert, men kan
ikke garanteres.

**Scenariobaserte estimater.** Kvantitative indikatorer
i utredningen er i hovedsak scenariobaserte estimater,
ikke presise måleresultater. De bør behandles som
retningsgivende.

### 9.2 Behov for videre arbeid

Utredningen identifiserer følgende behov for videre
arbeid:

1. **Detaljert kost-nytte-analyse** for fase 1, som
   grunnlag for investeringsbeslutning
2. **Juridisk utredning** av forholdet mellom
   KI-generert helseinnhold, EU AI Act og MDR i
   norsk kontekst
3. **Personvernkonsekvensvurdering (DPIA)** for de
   planlagte komponentene, særlig innbygger-chatbot
4. **Kompetansekartlegging** i FHI, Helsedirektoratet
   og NHN for å identifisere gap og
   rekrutteringsbehov
5. **Teknisk proof-of-concept** for KI-støttet
   screening og klarspråk-oversettelse
6. **Innbyggerundersøkelse** om holdninger til
   KI-generert helseinformasjon fra offentlige kilder
7. **Nordisk samarbeidsforum** for erfaringsutveksling
   om KI i kunnskapsforvaltning

### 9.3 Samlet vurdering

Dagens verdikjede for kunnskapsforvaltning er et
resultat av tiårs faglig utvikling og har tjent den
norske helsesektoren godt.
Kvalitetssikringsmekanismene er veletablerte, og
aktørkartleggingen viser at kompetansen og
ansvarsfordelingen er på plass.

Utfordringen er at verdikjeden ikke er designet for
det kunnskapsvolumet og de forventningene som preger
dagens og fremtidens helsesektor. Gjennomløpstiden er
for lang, kapasiteten for lav, og sammenkoblingen
mellom stegene for svak.

KI-teknologi representerer en mulighet til å adressere
disse utfordringene uten å undergrave
kvalitetssikringen. Internasjonale erfaringer viser at
KI som støtteverktøy med menneskelig kontroll gir
resultater. Den anbefalte faseinndelte tilnærmingen gir
mulighet for å hente lærdom og justere underveis, uten
å påta seg uakseptabel risiko.

Alternativet til styrt innføring er ikke fravær av KI.
Det er ukontrollert bruk av kommersielle KI-verktøy
uten governance, kvalitetssikring eller demokratisk
kontroll. Utredningen anbefaler at norske
helsemyndigheter tar en proaktiv rolle og former
utviklingen fremfor å la den forme seg.

---

Sist oppdatert: 2026-03-15

*Merknader om usikkerhet: Denne rapporten syntetiserer
funn fra seks foregående delrapporter. Estimatene er
scenariobaserte og har vesentlig usikkerhet, særlig for
kostnader og tidsbesparelse. Rapporten er ment som
grunnlag for menneskelig beslutningstaking, ikke som en
endelig beslutning.*
