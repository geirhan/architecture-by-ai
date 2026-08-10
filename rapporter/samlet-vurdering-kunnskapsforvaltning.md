# Delrapport 7: Samlet vurdering og anbefaling

Del av utredning om ny verdikjede for kunnskapsforvaltning
i helsesektoren

> **Status: Utforskende.** Rapporten skisserer en
> helhetlig anbefaling med fremdriftsplan, risikomatrise
> og juridiske endringsbehov. Prosjektet er i fasen der
> aksene som ligger til grunn diskuteres og forankres;
> beslutningsgrunnlaget for anbefalingen er derfor ikke
> ferdig forankret. Materialet brukes til intern
> utforskning, ikke som anbefaling utad i nåværende fase.
> Se [statusnivåer](index.md#statusnivåer).

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

Utredningen er motivert av tre utviklingstrekk. For det
første øker forskningsproduksjonen raskere enn vi klarer
å bearbeide den manuelt. For det andre søker stadig flere
innbyggere helseinformasjon fra kommersielle KI-tjenester
uten kvalitetssikring. For det tredje stiller EU AI Act
og EHDS (forordningen om det europeiske helsedataområdet)
nye krav til digital modenhet.

### Anbefaling

Vi anbefaler en **faseinndelt innføring av KI-støttet
kunnskapsforvaltning** i tre faser – pilotering, utvidelse
og transformasjon. Alternativ 2 (moderat KI-støtte) er
startpunktet, med gradvis utvidelse mot alternativ 3
(ambisiøs KI-pipeline). Organisatoriske tiltak fra
alternativ 1 gjennomføres parallelt. Tidshorisont for
hver fase fastsettes i mulighetsstudien.

### Hovedfunn

**Dagens verdikjede er ikke bærekraftig.** Casestudier
(`casestudier-forsinkelser.md`) dokumenterer at den
reelle tiden fra forskning til bred praksisendring er
**7–15+ år**, og at den normerende delprosessen
(forskning til vedtatt retningslinje) varierer fra
rundt 1 år til 7+ år avhengig av sak. De tre mest
alvorlige flaskehalsene er at kunnskapsgrunnlaget blir
foreldet mens retningslinjeprosessen pågår, at
kapasiteten for systematiske oversikter er for lav, og
at retningslinjer ikke kobles til innbyggerinformasjon
(delrapport 2). Normeringen skjer dessuten i to
parallelle spor – statlig og foreningsdrevet – uten
forrangsregler eller koordineringsforum [DOK/ANT,
`profesjonsforeninger-normering.md`].

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

### Nøkkelvirkninger (kvalitative)

Vi gjengir ikke tallanslag som mangler dokumentert
kildegrunnlag. Konkrete tidsbesparelser, kostnader og
månedstall forutsetter derfor egne utredninger
(kost–nytte-analyse, mulighetsstudie).

<!-- markdownlint-disable MD013 -->

| Indikator | Dagens situasjon | Med anbefalt tiltak |
| --- | --- | --- |
| Gjennomløpstid forskning–praksisendring | 7–15+ år (casestudier) | Vesentlig kortere, særlig med aktive implementeringstiltak |
| Gjennomløpstid forskning–retningslinje | Stor variasjon (ca. 1 år til 7+ år, casestudier) | Stor reduksjon for faseinnført KI-støtte |
| Skalerbarhet (kapasitet vs. volum) | Kapasitet vokser ikke med forskningsvolum | Frikoblet fra bemanning fra fase 2 |
| Reaktivitet | Periodisk, episodisk | Kontinuerlig i fase 3 (living guidelines) |
| Investeringsnivå | – | Moderat (fase 1–2) til høy (fase 3) |
| Kvalitetsrisiko | Lav (etablerte prosesser, men utdatert innhold) | Lav–moderat (fase 1–2), moderat–høy (fase 3) |

<!-- markdownlint-enable MD013 -->

### Konsekvens av å ikke handle

Nullalternativet (videreføring uten endring) er ikke
bærekraftig. Konsekvensene inkluderer: økende gap mellom
tilgjengelig kunnskap og formidlet informasjon, tap av
innbyggernes tillit til offentlig helseinformasjon i
konkurranse med kommersielle KI-tjenester, risiko for
manglende EHDS-samsvar, og kompetanseflukt fra offentlig
sektor.

### Målgruppe

Denne rapporten er rettet mot Helse- og
omsorgsdepartementet (HOD), Helsedirektoratets ledelse,
de regionale helseforetakene, KS og Norsk helsenett.

---

## 2. Innledning

### 2.1 Utredningens oppdrag og formål

Formålet med utredningen er å vurdere hvordan vi kan
modernisere verdikjeden for kunnskapsforvaltning i
helsesektoren, slik at innbyggere og helsepersonell får
oppdatert og kvalitetssikret helseinformasjon raskt nok.
Utredningen er strukturert etter utredningsinstruksens
minimumskrav.

### 2.2 Oversikt over delrapporter

Utredningen består av syv delrapporter:

<!-- markdownlint-disable MD013 -->

| Nr. | Tittel | Innhold |
| ----- | -------- | --------- |
| 1 | Dagens verdikjede | Kartlegging av verdikjeden fra forskning til innbygger i fem steg |
| 2 | Utfordringer og flaskehalser | Analyse av åtte rangerte flaskehalser og konsekvenser |
| 3 | Store språkmodeller - muligheter og risikoer | Balansert vurdering av LLM-teknologi i helsekontekst |
| 4 | Alternativer for ny verdikjede | Fire alternativer med kostnads- og risikovurdering |
| 5 | Arkitektur og komponenter | Teknisk og organisatorisk arkitektur med ArchiMate |
| 6 | Internasjonale erfaringer | WHO, NICE, Cochrane, nordiske land og living guidelines |
| 7 | Samlet vurdering og anbefaling | Denne rapporten |

<!-- markdownlint-enable MD013 -->

Denne samlerapporten syntetiserer funn fra alle
delrapportene og gir en helhetlig anbefaling.

---

## 3. Sammendrag av funn fra delrapporter

### Delrapport 1: Dagens verdikjede

Verdikjeden fra forskning til innbygger består av tre
hovedsteg med fire parallelle strømmer i steg 3.
Casestudier (antibiotika, diabetes type 2,
slagbehandling) dokumenterer at den reelle tiden fra
forskning til bred praksisendring er 7–15+ år, og at
den normerende delprosessen varierer fra ca. 1 år til
7+ år avhengig av sak. Helsedirektoratet publiserer
ikke aggregerte tall for typisk prosessvarighet.

Kartleggingen viser at verdikjeden preges av manuelle
overganger, fragmentert ansvar og begrenset strukturering
av innhold. Kvalitetssikringen er robust innenfor hvert
steg, men det finnes ingen systematisk mekanisme som
sikrer sammenheng på tvers av stegene. Innholdet er i
stor grad fritekstbasert, noe som begrenser mulighetene
for automatisert videreforedling.

### Delrapport 2: Utfordringer og flaskehalser

Analysen identifiserer ni rangerte flaskehalser.
De fem mest alvorlige er:
(1) foreldelse av kunnskapsgrunnlaget underveis i
retningslinjeprosessen,
(2) kapasitetsbegrensning for systematiske
oversikter,
(3) manglende kobling mellom retningslinjer og
innbyggerinformasjon,
(4) implementeringsgapet i klinisk praksis
(oppjustert til «høy» basert på casestudier som
dokumenterer 7-15+ år til praksisendring), og
(5) refusjonsordninger som barriere for
legemiddelbruk (ny flaskehals, dokumentert med
8 år fra forskning til refusjon i diabetes-casen).

Strukturelle utfordringer inkluderer siloorganisering
mellom aktører, manglende standardisert
informasjonsflyt, dobbeltarbeid og fragmenterte
IT-systemer. Konsekvensene er at helserådene blir
utdaterte, at innbyggere søker til alternative kilder
med varierende kvalitet, og at gapet mellom tilgjengelig
og formidlet kunnskap øker.

### Delrapport 3: Store språkmodeller - muligheter og risikoer

LLM-teknologi har potensial til å akselerere
kunnskapssyntese (vesentlig tidsbesparelse i screening
ifølge internasjonale piloter, jf. delrapport 6),
støtte retningslinjeutvikling, forbedre
innbyggerinformasjon gjennom klarspråk-oversettelse, og
muliggjøre living guidelines (retningslinjer som
oppdateres fortløpende etter hvert som ny kunnskap
foreligger, i stedet for periodisk). Samtidig medfører
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

Fire alternativer vurderes, med ulik inngripningsgrad.
Alternativ 0 (nullalternativet) viderefører dagens
praksis og vurderes som ikke bærekraftig. Alternativ 1
(organisatorisk modernisering) styrker kapasiteten
gjennom økt bemanning og prosessoptimalisering, med
marginal til moderat effekt – løser ikke det
underliggende skaleringsproblemet (R2 pre-digital
design). Alternativ 2 (moderat KI-støtte) innfører KI
som støtteverktøy med menneskelig kontroll og styrker
særlig skalerbarhet og reaktivitet. Alternativ 3
(ambisiøs KI-pipeline) innebærer living guidelines,
personaliserte helseråd og EHDS-integrasjon, og endrer
alle fire systemegenskaper forutsatt at
governance-leddet er på plass.

Anbefalingen er en faseinndelt tilnærming der
alternativ 2 implementeres først, med gradvis
utvidelse mot alternativ 3. Organisatoriske tiltak
fra alternativ 1 anbefales gjennomført parallelt.
Governance-modellen spesifiserer roller for
Helsedirektoratet (overordnet governance),
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
vesentlig tidsbesparelse i screening. Nordiske land
viser at Finland og Danmark har kommet lengst med
sentral infrastruktur.

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

Verdikjeden mangler fem sentrale egenskaper. Egenskapene
er formulert etter MECE-prinsippet (Mutually Exclusive,
Collectively Exhaustive) – det vil si at kategoriene ikke
overlapper, og at de til sammen dekker alle de seks
dimensjonene i utfordringsbildet (delrapport 2 kap. 2.3):

- **Skalerbarhet**: Kapasiteten øker ikke i takt med
  forskningsvolumet.
- **Reaktivitet**: Gjennomløpstiden gjør det umulig å
  respondere raskt på ny evidens, særlig i kriser.
- **Sammenheng**: Stegene og systemene i verdikjeden er
  ikke koblet på en måte som sikrer konsistent og
  oppdatert informasjon gjennom hele kjeden.
- **Styrbarhet**: Ingen aktør styrer kjeden som helhet
  mot et felles mål. Ansvaret er fordelt uten et samlet
  mandat, og ingen har eierskap til implementeringsgapet.
- **Tillit og legitimitet**: Systemet beholder ikke
  innbyggeren som foretrukken kilde når alternative
  kilder (generativ KI, sosiale medier) overtar. Dette
  er en tverrgående egenskap – svikt her følger i stor
  grad av svikt i de fire andre.

Delrapport 2 kap. 9 gir en strukturert rotårsaksanalyse
som identifiserer seks rotårsaker (R1–R6) bak de ni
rangerte flaskehalsene, samt en relasjonstabell som
viser hvordan flaskehalsene forsterker hverandre. De
fire rene systemegenskapene over korresponderer direkte
med rotårsakene: skalerbarhet ↔ R3, reaktivitet ↔ R3 og
R6, sammenheng ↔ R4, styrbarhet ↔ R1 og R5.
Tillit/legitimitet er en effekt av de øvrige og knyttes
ikke til en enkelt rotårsak. Rotårsaksrammeverket
brukes i kap. 5.4 for en differensiert vurdering av
alternativene.

For sammenheng og styrbarhet forsterkes utfordringen av
at normeringslandskapet har to parallelle spor – statlig
og foreningsdrevet: rundt 13 av 22 undersøkte
fagmedisinske foreninger har egne normerende produkter
[DOK, `profesjonsforeninger-normering.md` kap. 5b].
Sporene mangler forrangsregler og koordineringsforum,
noe som forsterker både sammenhengs- og
styrbarhetsutfordringen [ANT, samme notat].

### 4.3 Implikasjoner av å videreføre status quo

Dersom dagens verdikjede videreføres uten endring, vil
følgende konsekvenser med høy sannsynlighet inntreffe:

1. **Kunnskapsgapet øker.** Akselererende
   forskningsproduksjon betyr at en stadig større andel
   av tilgjengelig kunnskap aldri når inn i den
   offisielle verdikjeden.
2. **Kommersielle KI-tjenester tar over.** Innbyggere
   bruker allerede ChatGPT, Gemini og lignende tjenester
   for helseinformasjon. Uten et kvalitetssikret
   offentlig alternativ vil denne trenden akselerere.
3. **Regulatorisk etterslep.** EHDS (Forordning
   2025/327) krever strukturert, delbar elektronisk
   helseinformasjon i standardformat innen 2029
   (art. 14 og 15) og tilgjengeliggjøring for
   sekundærbruk (art. 51). EU AI Act (Forordning
   2024/1689) krever dokumentert datakvalitet (art. 10),
   transparens (art. 13) og systemovervåking (art. 72)
   for høyrisiko-KI fra august 2026. Dagens verdikjede –
   preget av fritekst og fragmenterte IT-systemer –
   oppfyller ikke disse kravene i sin nåværende form.
   EHDS treffer likevel ikke kjerneleddene (oversikter,
   retningslinjer, innbyggerinfo) direkte; for disse er
   etterslepet indirekte. Kildeforankring:
   `regulatorisk-etterslep.md`.
4. **Tillitserodering.** Dersom offentlig
   helseinformasjon oppleves som utdatert sammenlignet
   med kommersielle alternativer, kan det undergrave
   tilliten til helsemyndighetene.

### 4.4 Løsningsdimensjoner – aksene i løsningsrommet

Før vi kan forankre en løsning, må vi bli enige om
dimensjonene i løsningsrommet. Rotårsakene R1–R6
er gruppert i fire akser som beskriver de
beslutningsdimensjonene enhver løsning må ta stilling
til. Dimensjonene er utledet og dokumentert i
[delrapport 2 kap. 9.7](utfordringer-og-flaskehalser.md)
og brukes som hovedlins i forankrings­presentasjonen
`utfordringsbildet-forankring.pptx`.

| Akse | Spenning | Rotårsaker |
|---|---|---|
| Menneskedrevet ←→ KI-drevet | Hvor mye av kunnskapsproduksjonen skal automatiseres? | R2, R3 |
| Fragmentert ←→ Sammenhengende | Ulike systemer og aktører, eller én samordnet kjede? | R4, R1 |
| Frivillig ←→ Forpliktende | Implementering på fagmiljøenes initiativ, eller styringskrav? | R5 |
| Behovsstyrt ←→ Kontinuerlig oppdatering | Oppdatering når det utløses, eller kontinuerlig oppdatering basert på innstrømmende evidens? | R3, R6 |

Verdikjeden befinner seg i dag nær venstre side av
alle fire aksene. Alternativene i delrapport 4
representerer ulike bevegelser langs disse aksene:
nullalternativet beveger seg ikke; alternativ 1
beveger seg primært langs aksene 2 og 3 (organisasjon
og styring); alternativ 2 og 3 beveger seg primært
langs aksene 1 og 4 (KI og lærende kjede). Ingen av
alternativene dekker alle aksene fullt ut – noe som
forklarer hvorfor parallelle organisatoriske tiltak
er nødvendige uansett valg av teknologisk
alternativ.

Aksene fungerer dermed som **sjekkliste for
fullstendighet**: et alternativ som ikke beveger seg
langs én av aksene, adresserer ikke den tilhørende
rotårsaken.

---

## 5. Virkninger, varighet og fordelingsvirkninger

Utredningsinstruksen krever at positive og negative
virkninger vurderes for alle alternativer, at
varigheten angis, og at fordelingsvirkninger
identifiseres. Dette kapitlet systematiserer denne
vurderingen.

### 5.1 Positive og negative virkninger per alternativ

#### Alternativ 0 (nullalternativet)

- **Positive virkninger**: Ingen endringskostnader,
  ingen implementeringsrisiko, bevarelse av kjente
  arbeidsprosesser.
- **Negative virkninger**: Økende kunnskapsgap,
  foreldede helseråd, tap av tillit til offentlig
  helseinformasjon, manglende EHDS-samsvar,
  kompetanseflukt fra offentlig sektor. Varig og
  tiltakende over tid.
- **Varighet**: Permanent og selvforsterkende.

#### Alternativ 1 (organisatorisk modernisering)

- **Positive virkninger**: Marginal til moderat
  reduksjon i gjennomløpstid, bedre koordinering
  mellom aktørene, styrket kapasitet for
  kunnskapsproduksjon.
- **Negative virkninger**: Varig økning i
  driftskostnader (lønnsutgifter), rekruttering i et
  stramt arbeidsmarked for spesialkompetanse,
  organisatorisk endringsmotstand. Løser ikke det
  underliggende skaleringsproblemet (R2).
- **Varighet**: Gevinstene er reelle men avtagende
  over tid etter hvert som forskningsvolumet
  fortsetter å vokse.

#### Alternativ 2 (moderat KI-støtte)

- **Positive virkninger**: Vesentlig reduksjon i
  gjennomløpstid, økt kapasitet uten tilsvarende
  bemanningsøkning (styrket skalerbarhet og
  reaktivitet), bedre innbyggerinformasjon,
  posisjonering for EHDS-samsvar.
- **Negative virkninger**: Moderat
  investeringskostnad, behov for
  kompetanseomstilling, risiko for
  automatiseringstillit, avhengighet av
  teknologileverandører, overgangsperiode med
  redusert produktivitet under implementering.
- **Varighet**: Gevinstene er varige og skalerbare.
  Omstillingskostnadene er forbigående.

#### Alternativ 3 (ambisiøs KI-pipeline)

- **Positive virkninger**: Stor reduksjon i
  gjennomløpstid, living guidelines, personaliserte
  helseråd, full EHDS-integrasjon, flerspråklig
  formidling. Endrer alle fire systemegenskaper
  forutsatt at governance-leddet etableres.
- **Negative virkninger**: Høy investeringskostnad,
  vesentlig organisatorisk transformasjon,
  moderat–høy kvalitetsrisiko, regulatorisk
  usikkerhet, fare for leverandørlåsing, redusert
  menneskelig kontroll. Tilliten blir den kritiske
  faktoren.
- **Varighet**: Gevinstene er varige og
  transformative hvis vellykket. Risikoen for
  feilslått implementering er størst i de tidlige
  fasene.

### 5.2 Fordelingsvirkninger

Tabellen nedenfor viser hvem som bærer kostnadene
og hvem som høster gevinstene av det anbefalte
tiltaket (alternativ 2 som startpunkt med gradvis
utvidelse mot alternativ 3).

<!-- markdownlint-disable MD013 -->

| Berørt gruppe | Kostnader | Gevinster |
| --- | --- | --- |
| **HOD** | Finansiering (omfang fastsettes i mulighetsstudien), politisk risiko | Bedre måloppnåelse, EHDS-samsvar |
| **Helsedirektoratet** | Organisasjonsutvikling, governance-ansvar | Raskere retningslinjearbeid, styrket fagmyndighetsrolle |
| **FHI** | Omstilling, ny kompetanse, endrede roller for fagpersoner | Økt produksjonskapasitet, mer tid til faglig vurdering |
| **NHN** | Ny KI-driftskapasitet, teknisk rekruttering | Styrket rolle som nasjonal tjenesteleverandør |
| **RHF-ene** | Tilpasning til nye formater, opplæring | Raskere tilgang til oppdaterte retningslinjer |
| **KS/kommunene** | Tilpasning av lokale prosesser | Bedre innbyggerinformasjon, redusert lokal kunnskapsproduksjon |
| **Helsepersonell** | Endrede arbeidsformer, KI-kompetansebehov | Oppdatert kunnskapsgrunnlag, bedre verktøy |
| **Innbyggere** | Usikkerhet om KI-generert informasjon | Raskere, mer tilgjengelig helseinformasjon |

<!-- markdownlint-enable MD013 -->

### 5.3 Ikke-prissatte virkninger

Flere viktige virkninger lar seg ikke prissette:

- **Tillit til offentlig helseinformasjon**: Både
  alternativ 0 (tillitserodering pga. utdatert
  innhold) og alternativ 2-3 (usikkerhet om
  KI-generert innhold) påvirker tilliten. Samlet
  vurdering: tiltaket styrker tilliten forutsatt
  transparent kommunikasjon om KI-bruk.
- **Faglig autonomi**: KI-verktøy endrer
  fagpersoners rolle fra produsent til
  kvalitetskontrollør. Dette kan oppleves som
  tap av faglig autonomi, men kan også frigjøre
  tid til faglig vurdering.
- **Demokratisk kontroll**: KI-systemer i
  helseinformasjon berører spørsmål om
  algoritmisk transparens og offentlig innsyn.
  Styrkes ved åpen kildekode og offentlig
  dokumentasjon av KI-bruk.
- **Likeverd og tilgjengelighet**: Forbedret
  flerspråklig og multimodal formidling kan
  redusere helseforskjeller. Risiko for at
  digitalt utenforskap forsterkes dersom
  tradisjonelle kanaler nedprioriteres.

### 5.4 Dekning av rotårsaker

I delrapport 4, kapittel 6, sammenligner vi
alternativene på operasjonelle og kvalitative
dimensjoner: tid, kostnad, kvalitet, risiko og
EHDS-samsvar. Tabellen nedenfor utvider sammenligningen
med **dekning av rotårsakene R1–R6** (definert i
delrapport 2 kap. 9). Dette gir beslutningstakere
et tydeligere bilde av hvilke rotårsaker som
faktisk adresseres av hvert alternativ – og hvilke
som krever tiltak **utenfor** alternativene i
delrapport 4.

<!-- markdownlint-disable MD013 -->

| Rotårsak | Alt. 0 | Alt. 1 | Alt. 2 | Alt. 3 |
| --- | --- | --- | --- | --- |
| **R1** Styringsmandat | Ikke | Delvis | Delvis | Delvis |
| **R2** Pre-digital design | Ikke | Marginalt | Ja | Fullt |
| **R3** Kapasitet vs. volum | Ikke | Delvis | Ja | Fullt |
| **R4** IT-fragmentering | Ikke | Marginalt | Ja | Fullt |
| **R5** Impl.insentiver | Ikke | Delvis | Delvis | Delvis |
| **R6** Feedback/måling | Ikke | Delvis | Ja | Fullt |

<!-- markdownlint-enable MD013 -->

**Hovedobservasjoner:**

- **R1 (styringsmandat) og R5 (implementerings-
  insentiver) dekkes ikke fullt ut av noen av
  alternativene.** Disse rotårsakene er i hovedsak
  politiske/organisatoriske og krever tiltak som
  ligger utenfor et KI-teknologisk program:
  lovfesting av oppgavedeling, etablering av forum
  for faglig normering (Røttingen kap. 11.9),
  samordning av retningslinje- og refusjonsbeslut-
  ninger, og eksplisitt eierskap til
  implementeringsgapet. Disse tiltakene anbefales
  gjennomført **parallelt** med den faseinndelte
  innføringen av KI-støtte.
- **R2, R3, R4 og R6 dekkes progressivt bedre fra
  alt. 1 til alt. 3.** Dette støtter anbefalingen
  om å starte med alternativ 2 og gradvis utvide
  mot alternativ 3.
- **Alternativ 3 skaper økt belastning på R1.**
  Governance-kravene under EU AI Act og behovet
  for tverrsektoriell koordinering øker med
  ambisjonsnivået i alternativ 3. Dersom R1 ikke
  adresseres parallelt, øker risikoen i senere
  faser.

Implikasjonen er tatt opp i kap. 6.2 (faseinndelt
gjennomføringsplan) og i risikomatrisen.

---

## 6. Anbefaling

### 6.1 Overordnet anbefaling

Vi anbefaler en **faseinndelt innføring av KI-støttet
kunnskapsforvaltning**. Alternativ 2 (moderat KI-støtte)
er startpunktet, og innføringen utvides gradvis mot
elementer fra alternativ 3 etter hvert som teknologi,
kompetanse og styringsmodell (governance) modnes.
Organisatoriske tiltak fra alternativ 1 gjennomføres
parallelt. Tilnærmingen balanserer behovet for
modernisering mot risikoen for feilslått
implementering.

Faseinndelingen angir rekkefølge og avhengigheter,
ikke konkrete varigheter. Tidsfastsettelse og kostnad
forutsetter mulighetsstudie og kost–nytte-analyse.

### 6.2 Fase 1: Pilotering

**Målsetning:** Bevise konseptet og bygge grunnlaget.

- KI-assistert screening av forskningslitteratur ved
  FHI (pilot på utvalgte fagområder)
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

**Risiko:** Lav.

### 6.3 Fase 2: Utvidelse

**Målsetning:** Skalere det som virker og utvide
funksjonaliteten.

- Skalering av KI-støttet screening til alle fagområder
  ved FHI
- KI-støttede utkast til systematiske oversikter
- Implementering av automatisk evidensvarsling for
  eksisterende retningslinjer
- Pilotering av KI-chatbot på helsenorge.no med RAG
  (retrieval-augmented generation – en teknikk der
  KI-modellen henter svar fra verifiserte
  kunnskapskilder i stedet for å generere dem fritt)
- Etablering av kunnskapsbase med strukturerte metadata
  og FHIR-grensesnitt
- Videreutvikling av governance basert på erfaringer
  fra fase 1

**Risiko:** Moderat.

### 6.4 Fase 3: Transformasjon

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

**Risiko:** Moderat–høy. Fase 3 forutsetter vellykket
gjennomføring av fase 1 og 2, samt at teknologien
modnes ytterligere.

### 6.5 Kostnadsramme

Investeringsnivå per fase, kvalitativt vurdert:

| Fase | Investeringsnivå | Risiko |
| --- | --- | --- |
| Fase 1: Pilotering | Lavt | Lav |
| Fase 2: Utvidelse | Moderat | Moderat |
| Fase 3: Transformasjon | Høyt | Moderat–høy |

Konkrete kostnadsestimater forutsetter detaljert
kost–nytte-analyse per fase, og inkluderer utvikling,
anskaffelse, kompetanseheving og organisasjonsutvikling.
Driftskostnader kommer i tillegg.

### 6.6 Organisatoriske forutsetninger

Vellykket gjennomføring forutsetter:

1. **Tydelig oppdrag fra HOD** med tilhørende
   finansiering og mandat
2. **Tverrsektoriell forankring** mellom
   Helsedirektoratet, FHI og NHN med felles
   forståelse av mål og ansvarsfordeling
3. **Kompetanseinvestering** i KI-forståelse og -bruk
   hos fagpersoner, samt rekruttering av teknisk
   kompetanse
4. **Regulatorisk pådriverrolle** der Helsedirektoratet
   går foran og setter EU AI Act i praktisk drift for
   helsesektoren
5. **Iterativ tilnærming** der hver fase evalueres
   før neste fase starter, med involvering av
   fagpersoner og innbyggere
6. **Realistiske forventninger** om at KI er et
   støtteverktøy, ikke en erstatning for faglig
   kompetanse

---

## 7. Risikomatrise

Tabellen under viser de viktigste risikoene for
KI-støttet kunnskapsforvaltning, med sannsynlighet,
konsekvens og forslag til tiltak (mitigering).

<!-- markdownlint-disable MD013 -->

| Nr. | Risiko | Sannsynlighet | Konsekvens | Samlet risiko | Mitigering |
| ----- | -------- | --------------- | ------------ | --------------- | ------------ |
| 1 | Hallusinering i KI-generert helseinnhold | Høy | Høy | **Kritisk** | RAG mot verifiserte kilder, automatisert faktasjekk, menneskelig validering før publisering, hallusinerings-deteksjon |
| 2 | Tap av tillit til offentlig helseinformasjon | Middels | Høy | **Høy** | Transparent kommunikasjon om KI-bruk, tydelig faglig ansvar, gradvis innføring med evaluering |
| 3 | Personvernbrudd | Lav | Høy | **Moderat** | DPIA (personvernkonsekvensvurdering) før publisering, dataminimering, norsk jurisdiksjon for datalagring, databehandleravtaler |
| 4 | Implementeringsforsinkelser | Høy | Middels | **Høy** | Faseinndelt tilnærming, tydelige milepæler, risikobasert prioritering |
| 5 | Teknologiavhengighet/leverandørlåsing | Middels | Middels | **Moderat** | Abstraksjonslag mot KI-modeller, åpne standarder, leverandøruavhengig arkitektur |
| 6 | Regulatorisk usikkerhet (EU AI Act) | Middels | Middels | **Moderat** | Proaktiv dialog med tilsynsmyndigheter, juridisk kompetanse, følge europeisk rettsutvikling |
| 7 | Organisatorisk motstand | Middels | Middels | **Moderat** | Involvering av berørt personell fra start, kompetanseheving, tydelig kommunikasjon om at KI støtter, ikke erstatter |
| 8 | Kompetansemangel | Høy | Middels | **Høy** | Langsiktig kompetansestrategi, rekruttering, samarbeid med universitetsmiljøer |
| 9 | Budsjettoverskridelser | Middels | Middels | **Moderat** | Faseinndelt investering med evaluering, grove estimater som oppdateres per fase |
| 10 | Innbyggere bruker ukvalifiserte KI-kilder | Høy | Høy | **Kritisk** | Proaktivt tilby kvalitetssikret KI-basert helseinformasjon, chatbot på helsenorge.no, synlighet i søkeresultater |
| 14 | KI-tjenesten bygges på et kildegrunnlag uten foreningssporet: en tjeneste som kun eksponerer statlig innhold, mangler store deler av den kliniske veiledningen klinikere faktisk bruker (lav klinisk legitimitet og dekning); alternativt eksponeres foreningsinnhold uten lisens- og konsistensavklaring [ANT; faktagrunnlag: `profesjonsforeninger-normering.md`] | Middels | Høy | **Høy** | Innholdsavtaler med foreningene, kildemerking, konsistenskontroll, avklaring av forrang mellom sporene |

<!-- markdownlint-enable MD013 -->

**Oppsummering av risikobildet:**

To risikoer vurderes som kritiske: hallusinering i
helseinnhold og at innbyggere søker ukvalifiserte
KI-kilder. Begge adresseres direkte av den anbefalte
tilnærmingen: hallusinering gjennom robust
kvalitetssikring, og konkurranserisikoen gjennom å tilby
et kvalitetssikret offentlig alternativ.

Fire risikoer vurderes som høye: tap av tillit,
implementeringsforsinkelser, kompetansemangel og et
kildegrunnlag uten foreningssporet (nr. 14, lagt til
sist; nr. 11–13 er scenariorisikoer i kap. 7.1). Disse
krever aktiv styring gjennom hele gjennomføringsperioden.

### 7.1 Scenariorisiko – strukturelle utviklingsbaner

Risikoene 1–10 over er **operasjonelle og
gjennomføringsorienterte**: de kan inntreffe innenfor det
anbefalte tiltaket og styres med konkrete
mitigeringstiltak (risikoreduserende tiltak). Delrapport 9
(Fremtidsscenarioer) peker på en annen risikotype:
**scenariorisiko**. Dette er risikoen for at hele
systemet driver mot en uønsket tilstand, uavhengig av
hvor godt det enkelte tiltaket gjennomføres [ANT, jf.
`fremtidsscenarioer.md`].

Disse risikoene skiller seg fra 1–10 ved at de gjelder
*hvilket fremtidsbilde* sektoren havner i (scenariokorset
S1–S4), ikke enkeltfeil i gjennomføringen. De er tatt med
fordi den viktigste av dem – drift mot fragmentering –
**krever ingen aktiv beslutning** for å inntreffe; den er
driftsbanen ved passivitet.

<!-- markdownlint-disable MD013 -->

| Nr. | Scenariorisiko | Sannsynlighet | Konsekvens | Samlet risiko | Mitigering |
| ----- | -------- | --------------- | ------------ | --------------- | ------------ |
| 11 | Drift mot fragmentert flora (S4): kommuner/HF/RHF bygger hver sin KI-løsning uten felles rammer | Høy | Høy | **Kritisk** | Etablere felles standarder, metadataprofiler og gjenbrukbar offentlig kunnskap *tidlig*; orkestreringsstrategi (jf. S3); kartlegge pågående lokale initiativer; gjøre det enklere å bygge *på* enn *ved siden av* |
| 12 | Plattformavhengighet (S2): én dominerende kommersiell/EPJ-integrert (elektronisk pasientjournal) KI blir en uformell standard («de facto standard») | Middels | Høy | **Høy** | Konkurransedyktig offentlig tilbud på tilgjengelighet og aktualitet; krav om at lokal/EPJ-KI bygger på norske retningslinjer; EU AI Act art. 10/13-etterlevelse; leverandøruavhengig arkitektur |
| 13 | Kollapsbane S1→S4: en sentral løsning som er for treg eller mangler mandat utløser de lokale initiativene den skulle erstatte | Middels | Høy | **Høy** | Sikre reaktivitet og tilgjengelighet i den sentrale løsningen; reelt styringsmandat (R1); bygge inn orkestrering fra start slik at en sentral motor (S1) kan utvikles mot et føderert økosystem (S3) |

<!-- markdownlint-enable MD013 -->

**Sammenheng med rotårsakene.** Scenariorisikoene
forsterker de samme rotårsakene utredningen allerede har
identifisert: S4-drift forsterker R1 (styringsmandat), R2
(fragmentering) og R4 (IT-fragmentering); S2 forsterker R1
i ekstrem grad (styringen flyttes til aktører utenfor norsk
myndighet). Den felles mitigeringen – tidlige felles
standarder og en eksplisitt orkestreringsstrategi – er
nettopp det som skiller det ønskede scenarioet (S3 Føderert
økosystem) fra det uønskede (S4 Fragmentert flora) [ANT,
jf. `fremtidsscenarioer.md` kap. 5;
`verdikjede-som-okosystem.md` kap. 4.2].

**Konsekvens for anbefalingen.** Scenariorisikoene
understreker at orkestrering (felles rammer som gjør lokal
innovasjon til en styrke fremfor en trussel) bør være et
**eksplisitt designkrav** i fase 1, ikke en oppgave som
utsettes til transformasjonsfasen. Dette utdyper de
organisatoriske forutsetningene i kap. 6.6.

---

## 8. Fremdriftsplan

### 8.1 Aktiviteter og avhengigheter

Tabellen viser rekkefølge, ansvar og kritiske
avhengigheter. Konkrete tidsanslag forutsetter
gjennomføringsplan med ressurser, og er derfor utelatt.

<!-- markdownlint-disable MD013 -->

| Aktivitet | Fase | Ansvarlig | Avhengigheter |
| --- | --- | --- | --- |
| **Fase 1: Pilotering** | | | |
| Oppdrag og finansiering fra HOD | 1 | HOD | Politisk beslutning |
| Etablere governance-rammeverk | 1 | Helsedirektoratet | Oppdrag fra HOD |
| KI-screening pilot ved FHI (utvalgte fagområder) | 1 | FHI | Governance-rammeverk |
| KI-klarspråk pilot | 1 | Helsedirektoratet/NHN | Governance-rammeverk |
| Kompetanseheving nøkkelpersonell | 1 | Alle aktører | Budsjett |
| Juridisk avklaring EU AI Act | 1 | Helsedirektoratet | – |
| **Milepæl M1:** Pilotevaluering og beslutning om fase 2 | 1 | Helsedirektoratet | Pilotresultater |
| **Fase 2: Utvidelse** | | | |
| Skalere KI-screening til alle fagområder | 2 | FHI | M1 |
| KI-støttede systematiske oversikter | 2 | FHI | M1 |
| Automatisk evidensvarsling | 2 | FHI/NHN | Kunnskapsbase |
| KI-chatbot pilot på helsenorge.no | 2 | NHN | Kunnskapsbase, governance |
| Etablere kunnskapsbase med FHIR | 2 | NHN | Arkitektur |
| **Milepæl M2:** Evaluering og beslutning om fase 3 | 2 | Helsedirektoratet | Fase 2-resultater |
| **Fase 3: Transformasjon** | | | |
| Living guidelines pilot | 3 | Helsedirektoratet/FHI | M2 |
| EHDS-integrasjon | 3 | NHN | Kunnskapsbase, EHDS-tidsplan |
| Personaliserte helseråd pilot | 3 | NHN/Helsedirektoratet | Regulatorisk avklaring |
| Flerspråklig formidling | 3 | NHN | Kunnskapsformidlingsplattform |
| **Milepæl M3:** Full operativ drift | 3 | Alle aktører | Alle faser |

<!-- markdownlint-enable MD013 -->

### 8.2 Kritiske avhengigheter

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

## 9. Samsvar med utredningsinstruksen

Utredningen svarer på utredningsinstruksens seks
minimumskrav:

### Krav 1: Problemet og målet

**Problemet:** Verdikjeden for kunnskapsforvaltning i
helsesektoren har dokumentert lang gjennomløpstid:
casestudier viser 7–15+ år fra forskning til bred
praksisendring, og at den normerende delprosessen
varierer fra ca. 1 år til 7+ år avhengig av sak
(`casestudier-forsinkelser.md`). Verdikjeden skalerer
ikke med økende forskningsvolum, og innbyggere søker i
økende grad helseinformasjon fra ukvalifiserte kilder.
(Delrapport 1 og 2.)

**Målet:** Redusere gjennomløpstiden vesentlig, øke
kapasiteten for kunnskapsproduksjon, sikre at offentlig
helseinformasjon er oppdatert og tilgjengelig, og
posisjonere Norge for EHDS-samsvar.

### Krav 2: Relevante tiltak

Fire alternativer er vurdert (delrapport 4), med ulik
inngripningsgrad i tråd med instruksens krav:

- Alternativ 0: Videreføring uten endring
  (ikke bærekraftig)
- Alternativ 1: Organisatorisk modernisering uten KI
  (økt bemanning, prosessoptimalisering)
- Alternativ 2: Moderat KI-støtte med menneskelig
  kontroll (anbefalt startpunkt)
- Alternativ 3: Ambisiøs KI-pipeline med living
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
- Konsekvenser for maktfordeling mellom stat,
  kommune og privat sektor ved økt sentralisering
  av kunnskapsproduksjon

### Krav 4: Berørte parter og virkninger

Berørte parter er kartlagt (delrapport 1, 4 og 8)
med systematisk vurdering av positive og negative
virkninger, varighet og fordelingsvirkninger
(kapittel 5):

- **HOD** som oppdragsgiver og politisk styringsnivå
- **Helsedirektoratet** som fagmyndighet og
  retningslinjeeier
- **FHI** som kunnskapsprodusent
- **NHN** som tjenesteleverandør
- **RHF-ene** som implementører i
  spesialisthelsetjenesten
- **KS og kommunene** som implementører i
  primærhelsetjenesten
- **Innbyggere** som sluttbrukere av
  helseinformasjon
- **Helsepersonell** som brukere av retningslinjer
  og fagkunnskap

Fordelingsvirkningstabell i kapittel 5.2 viser
hvem som bærer kostnader og hvem som høster
gevinster. Ikke-prissatte virkninger (tillit,
faglig autonomi, demokratisk kontroll, likeverd)
er vurdert i kapittel 5.3.

### Krav 5: Anbefalt tiltak

Faseinndelt innføring av KI-støttet
kunnskapsforvaltning i tre faser (pilotering,
utvidelse, transformasjon), med alternativ 2 som
startpunkt og organisatoriske tiltak fra alternativ 1
parallelt. Tidshorisont fastsettes i mulighetsstudien.
Se kapittel 6.

### Krav 6: Forutsetninger for vellykket gjennomføring

Seks organisatoriske forutsetninger er identifisert
(kapittel 6.6): tydelig oppdrag fra HOD,
tverrsektoriell forankring, kompetanseinvestering,
regulatorisk proaktivitet, iterativ tilnærming og
realistiske forventninger.

#### Juridiske endringsbehov

Vi har identifisert følgende juridiske avklaringer og
mulige endringer som forutsetninger:

- **Forskriftsendringer**: Vurdering av om
  forskrift om ledelse og kvalitetsforbedring
  i helse- og omsorgstjenesten krever oppdatering
  for å regulere bruk av KI-generert
  kunnskapsinnhold
- **Tildelingsbrev**: Oppdaterte tildelingsbrev til
  Helsedirektoratet og FHI med eksplisitt mandat
  for KI-støttet kunnskapsforvaltning
- **Databehandleravtaler**: Nye eller oppdaterte
  databehandleravtaler for skybaserte
  KI-tjenester, med særlig vurdering av
  tredjelandsoverføring (Schrems II)
- **EU AI Act-implementering**: Norsk
  gjennomføring av EU AI Act i EØS-avtalen,
  med operasjonalisering av høyrisikokrav for
  helsesektoren
- **MDR-grensedragning**: Rettslig avklaring av
  om KI-genererte helseråd (særlig
  personaliserte) klassifiseres som medisinsk
  utstyr etter MDR
- **Personvernkonsekvensvurdering (DPIA)**:
  Obligatorisk DPIA for alle KI-komponenter som
  behandler helseopplysninger eller
  brukerinteraksjoner
- **Foreningsutviklede veiledere**: Avklaring av
  rettslig status og forrang for foreningsutviklede
  veiledere i forsvarlighetsvurderinger etter
  helsepersonelloven § 4. Tilsynspraksis bruker dem
  allerede som norm (Helsetilsynet 2016), men uten
  nedfelt generelt prinsipp [DOK,
  `profesjonsforeninger-normering.md` kap. 3]

#### Evalueringsplan

Hver fase skal evalueres før beslutning om neste
fase. Evalueringsplanen er strukturert slik:

<!-- markdownlint-disable MD013 -->

| Fase | Evalueringstidspunkt | Ansvarlig | Evalueringskriterier | Metode |
| --- | --- | --- | --- | --- |
| Fase 1 | Mot slutten av pilotering | Helsedirektoratet | Faktisk tidsbesparelse vs. forhåndssatt mål, kvalitet på KI-generert innhold (feilrate), brukeraksept hos fagpersoner, samsvar med EU AI Act | Kvantitativ måling, brukerundersøkelse, ekstern kvalitetsrevisjon |
| Fase 2 | Mot slutten av utvidelse | Helsedirektoratet | Skaleringsresultater, innbyggertilfredshet med chatbot, kostnadsutvikling vs. forhåndssatt mål, KI-systemenes ytelse over tid | Kvantitativ måling, innbyggerundersøkelse, kost–nytte-analyse |
| Fase 3 | Mot slutten av transformasjon | Helsedirektoratet | Funksjonalitet av living guidelines, EHDS-integrasjon, samlet måloppnåelse for utredningen | Ekstern evaluering, internasjonal benchmarking |

<!-- markdownlint-enable MD013 -->

Evalueringen skal inkludere:

- Uavhengig ekstern vurdering for hver fase
- Innspill fra berørte aktører (FHI, NHN,
  helsepersonell, innbyggere)
- Åpen publisering av evalueringsresultater
- Eksplisitt go/no-go-beslutning før neste fase

---

## 10. Avsluttende merknad

### 10.1 Usikkerhet og begrensninger

Denne utredningen har vesentlige begrensninger som
leseren bør være oppmerksom på:

**Teknologisk usikkerhet.** KI-teknologi er i rask
utvikling. Vurderinger av ytelse og effekt er basert
på dagens teknologinivå og tidlige erfaringer. Faktisk
utvikling kan avvike både positivt og negativt.

**Kostnad og tidshorisont er ikke fastsatt.** Rapporten
gir kvalitative vurderinger (investeringsnivå, risiko,
effekt), men ikke konkrete kronebeløp eller månedstall.
Disse forutsetter detaljert kost–nytte-analyse og
mulighetsstudie per fase.

**Regulatorisk usikkerhet.** EU AI Act er nylig trådt i
kraft, og tolkningen for helsedomenet er ikke fullt
avklart. Forholdet mellom KI-generert helseinformasjon
og medisinsk utstyr-forordningen (MDR) er et uavklart
grenseområde.

**Begrenset empirisk grunnlag.** Flere av de
internasjonale erfaringene (delrapport 6) er fra
pilotprosjekter, ikke fullskala implementeringer.
Overførbarhet til norsk kontekst er vurdert, men kan
ikke garanteres.

**Dokumentasjonsprinsipp.** Vi gjengir ikke tallanslag
som mangler dokumentert kildegrunnlag. Tidligere
versjoner inneholdt scenariobaserte estimater
(%-tidsbesparelser, MNOK-kostnader, måneds-tall) som vi
ikke kunne forankre i offisielle eller peer-reviewed
kilder. Vi har derfor fjernet disse og erstattet dem
med kvalitative vurderinger.

### 10.2 Behov for videre arbeid

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
8. **Veivalg for foreningssporet**: Avklare om en
   fremtidig kunnskapsforvaltning skal innlemme,
   erstatte eller sameksistere med
   profesjonsforeningenes normerende produkter
   (behandles i delrapport 4) [ANT,
   `profesjonsforeninger-normering.md`]

### 10.3 Samlet vurdering

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

KI-teknologi kan løse disse utfordringene uten å svekke
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

Sist oppdatert: 2026-08-10

*Rapporten syntetiserer funn fra seks foregående
delrapporter. Den er ment som grunnlag for menneskelig
beslutningstaking, ikke som en endelig beslutning.
Tallanslag som ikke er forankret i dokumenterte kilder
er utelatt; konkretisering av tid, kostnad og
forventet effekt skjer i mulighetsstudie og
kost–nytte-analyse per fase.*

## Endringslogg

| Dato | Endring |
|---|---|
| 2026-04-08 | Versjon med scenariobaserte estimater for gjennomløpstid (2–3 år / 7–15+ år), kostnad (5–250 MNOK over faser) og tidsbesparelse (15–90 %). |
| 2026-05-20 | Kap. 4.4 «Løsningsdimensjoner – aksene» lagt til. Kap. 5.4 dekning av rotårsaker R1–R6 lagt til. |
| 2026-05-22 | Kap. 4.2 omformulert fra tre til fem kjerneegenskaper (skalerbarhet, reaktivitet, sammenheng, styrbarhet, tillit/legitimitet); MECE-oppsummering av D1–D6 fra delrapport 2 kap. 2.3. |
| 2026-05-26 | Konsistensgjennomgang: udokumenterte tallanslag fjernet (alle 2–3 år, 2,5–5 år, %-tidsbesparelser, MNOK-kostnader, måned-baserte fasevarigheter). Nøkkeltall- og kostnadstabeller omkalibrert til kvalitative gradsbetegnelser. Fremdriftsplan kap. 8.1 endret fra månedstall til rene avhengigheter. Tidsestimater forankret i `casestudier-forsinkelser.md` der dokumentert. |
| 2026-06-04 | Nytt kap. 7.1 «Scenariorisiko – strukturelle utviklingsbaner» med tre nye risikoer (11–13: drift mot S4, plattformavhengighet S2, kollapsbane S1→S4) basert på delrapport 9 (`fremtidsscenarioer.md`). Koblet til rotårsakene R1/R2/R4 og til orkestrering som designkrav (kap. 6.6). |
| 2026-08-10 | Profesjonsforening-perspektivet innarbeidet fra `profesjonsforeninger-normering.md`: tosporet normering i ledersammendrag og kap. 4.2, ny risiko 14 (kildegrunnlag uten foreningssporet), juridisk avklaringspunkt om foreningsveiledere og hpl. § 4 (kap. 9), veivalg innlemme/erstatte/sameksistere i kap. 10.2. |
