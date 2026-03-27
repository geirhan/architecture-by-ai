# Delrapport 3: Store språkmodeller – muligheter og risikoer

## Del av utredning om ny verdikjede for kunnskapsforvaltning i helsesektoren

---

## 1. Innledning

Store språkmodeller (Large Language Models, LLM) og
generativ kunstig intelligens (KI) har gjennomgått
en eksepsjonell utvikling de siste årene. Fra å være
forskningsverktøy med begrenset praktisk nytte, har
modellene nådd et ytelsesnivå som gjør dem relevante
for en rekke kunnskapsintensive oppgaver – inkludert
oppgaver som tidligere var forbeholdt fageksperter.

For kunnskapsforvaltning i helsesektoren
representerer dette både betydelige muligheter og
vesentlige risikoer. Som beskrevet i delrapport 1,
er dagens verdikjede fra forskning til
innbyggerrettet helseinformasjon preget av lange
ledetider, ressurskrevende manuelle prosesser og
utfordringer med å holde innholdet oppdatert.
LLM-teknologi har potensial til å adressere flere av
disse utfordringene – men introduserer samtidig nye
typer risiko som er spesielt alvorlige i et
helsedomene.

Formålet med denne delrapporten er å gi en balansert
vurdering av muligheter og risikoer ved bruk av
LLM-er i kunnskapsforvaltning i helsesektoren, med
særlig vekt på de regulatoriske rammene som følger av
EU AI Act og relevansen for EHDS-konteksten.

**Metodisk merknad:** Vurderingene i denne rapporten
er basert på publisert forskning, offisielle
dokumenter fra EU og erfaringer fra tidlige
implementeringer internasjonalt. Feltet er i rask
utvikling, og flere av de kvantitative estimatene som
presenteres bør forstås som scenariobaserte anslag
snarere enn etablerte fakta. Usikkerhet er markert
der det er relevant.

---

## 2. Hva er store språkmodeller?

### Grunnleggende egenskaper

En stor språkmodell er et KI-system som er trent på
store mengder tekst for å forstå og generere
menneskelig språk. Modellene lærer statistiske
mønstre i språket – ordvalg, setningsstruktur,
resonnementskjeder – og kan bruke denne kunnskapen
til å utføre et bredt spekter av språkoppgaver uten
å være spesifikt programmert for hver enkelt oppgave.

Nøkkelegenskaper som gjør LLM-er relevante for
kunnskapsforvaltning inkluderer:

- **Språkforståelse**: Evne til å tolke komplekse
  tekster, identifisere nøkkelinformasjon og forstå
  kontekst
- **Oppsummering**: Kondensering av lange dokumenter
  til kortere sammendrag med bevart innhold
- **Oversettelse**: Konvertering mellom språk,
  inkludert fagspråk til klarspråk
- **Generering**: Produksjon av ny tekst basert på
  gitte premisser og instruksjoner
- **Klassifisering**: Kategorisering av innhold etter
  type, relevans eller kvalitet

### Eksempler på aktuelle modeller

Markedet for LLM-er er mangfoldig. Kommersielle
modeller som GPT-4 (OpenAI), Claude (Anthropic) og
Gemini (Google) tilbys som skytjenester. Åpne
modeller som Llama (Meta) kan kjøres på egen
infrastruktur. I nordisk kontekst finnes det arbeid
med modeller som har bedre forståelse av
skandinaviske språk, selv om disse per i dag er
mindre modne enn de ledende internasjonale modellene.

### Ytelse på medisinske benchmarks

LLM-er har vist økende ytelse på medisinske
kunnskapstester. GPT-4 bestod den amerikanske
legeeksamenen (USMLE) med god margin, og nyere
modeller scorer over 85 % på benchmarks som MedQA.
Det er imidlertid viktig å understreke at gode
resultater på standardiserte tester ikke automatisk
betyr at modellene er pålitelige i klinisk praksis.
Benchmarks tester gjenkjenning av fakta og
resonnement under kontrollerte betingelser, mens
klinisk og faglig arbeid krever helhetsvurdering,
kontekstforståelse og håndtering av usikkerhet.

---

## 3. Muligheter for kunnskapsforvaltning

### 3.1 Akselerert kunnskapssyntese

Den mest umiddelbare muligheten ligger i å
effektivisere prosessen med å sammenstille
forskningsevidens. Dagens prosess for systematiske
oversikter, som beskrevet i delrapport 1, er svært
ressurskrevende.

**Automatisert screening av forskningslitteratur:**
LLM-er kan gjennomgå store mengder
forskningsartikler og identifisere hvilke som er
relevante for en gitt problemstilling. I tradisjonell
systematisk oversiktsarbeid bruker forskere betydelig
tid på å screene titler og sammendrag. KI-assistert
screening har potensial til å redusere denne tiden
vesentlig.

**KI-assistert dataekstraksjon:** Etter at relevante
studier er identifisert, må nøkkeldata ekstraheres –
studiedesign, deltakertall, utfallsmål, resultater.
LLM-er kan automatisere deler av denne prosessen, med
menneskelig kvalitetssikring av resultatene.

**Raskere oppdatering av systematiske oversikter:**
Et sentralt problem i dag er at systematiske
oversikter ofte er utdaterte når de publiseres.
KI-støttet overvåking og screening kan bidra til
hyppigere oppdateringer.

**Scenariobaserte estimater for tidsbesparelse:**

| Prosesstrinn | Tradisjonell tidsbruk | Estimert tidsbruk med KI-støtte | Estimert besparelse |
| --- | --- | --- | --- |
| Screening av titler/sammendrag | 2-4 uker | 2-5 dager | 50-80 % |
| Fulltekstgjennomgang | 2-3 uker | 1-2 uker | 30-50 % |
| Dataekstraksjon | 2-4 uker | 1-2 uker | 30-50 % |
| Kvalitetsvurdering | 1-2 uker | 1-2 uker | Begrenset |

*Merknad: Disse estimatene er scenariobaserte og
bygger på tidlige erfaringer fra blant annet Cochrane
og NICE (se delrapport 6). Faktisk tidsbesparelse vil
avhenge av domene, datakvalitet og grad av
menneskelig kvalitetssikring.*

### 3.2 Retningslinjestøtte

LLM-er kan støtte retningslinjearbeidet på flere
nivåer:

**Identifisering av ny evidens:** Kontinuerlig
overvåking av publisert forskning for å identifisere
studier som kan påvirke eksisterende retningslinjer.
Dette adresserer en vesentlig utfordring i dagens
verdikjede, der det kan gå lang tid mellom publisert
forskning og oppdaterte retningslinjer.

**Utkast til retningslinjetekst:** Gitt et
oppsummert kunnskapsgrunnlag, kan LLM-er generere
utkast til retningslinjeformuleringer. Det er viktig
å understreke at dette er utkast som må gjennomgås og
godkjennes av fageksperter og retningslinjepaneler –
ikke ferdige produkter.

**Konsistenssjekk:** Norske retningslinjer utvikles
av ulike arbeidsgrupper over tid. LLM-er kan brukes
til å identifisere motstridende eller inkonsistente
anbefalinger på tvers av retningslinjer.

**Pasientversjoner:** Automatisk generering av
lettleste versjoner av faglige retningslinjer,
tilpasset innbyggere uten helsefaglig bakgrunn. Dette
kan bidra til raskere tilgjengeliggjøring av
oppdatert informasjon på helsenorge.no.

### 3.3 Forbedret innbyggerinformasjon

**Klarspråk og tilgjengelighet:** LLM-er kan
konvertere fagspråk til klarspråk systematisk og
konsistent, og dermed forbedre tilgjengeligheten av
helseinformasjon for innbyggere med ulik bakgrunn.

**Flerspråklig tilgjengeliggjøring:** Med økende
mangfold i befolkningen er det behov for
helseinformasjon på flere språk. LLM-er kan bidra
til raskere oversettelse, men kvalitetssikring av
medisinsk oversettelse er kritisk og krever faglig
gjennomgang.

**Konversasjonsbasert helseinformasjon:** KI-baserte
chatboter kan gi innbyggere mulighet til å stille
spørsmål og få svar basert på kvalitetssikret
innhold. Slike løsninger kan gi mer tilgjengelig
helseinformasjon, men reiser samtidig vesentlige
spørsmål om ansvar og kvalitetssikring
(se kapittel 4).

### 3.4 Kontinuerlig kunnskapsoppdatering

LLM-er kan muliggjøre en overgang fra periodisk
oppdaterte retningslinjer til
«living guidelines» – retningslinjer som oppdateres
kontinuerlig etter hvert som ny evidens publiseres:

- **Sanntidsovervåking** av nye publikasjoner innen
  definerte fagområder
- **Automatisert varsling** til retningslinjepaneler
  når ny evidens kan påvirke eksisterende
  anbefalinger
- **KI-assistert vurdering** av om ny evidens endrer
  evidensgrunnlaget vesentlig

Dette konseptet krever robuste
kvalitetssikringsmekanismer og tydelig governance
for å fungere i praksis. Erfaringer fra WHO SMART
Guidelines og Cochrane (se delrapport 6) gir nyttige
referansepunkter.

---

## 4. Risikoer og utfordringer

### 4.1 Hallusinering og faktafeil

LLM-er kan generere tekst som fremstår plausibel og
velformulert, men som inneholder faktiske feil. Denne
egenskapen, ofte kalt «hallusinering», er en iboende
egenskap ved hvordan modellene fungerer – de
genererer tekst basert på statistisk sannsynlighet,
ikke basert på en verifisert kunnskapsbase.

I helsedomenet er dette spesielt alvorlig. En
feilaktig referanse i en akademisk tekst kan være
pinlig; et feilaktig helseråd kan i verste fall være
skadelig. Dokumenterte eksempler inkluderer modeller
som har angitt feil dosering av legemidler, oppgitt
ikke-eksisterende interaksjoner eller generert
referanser til studier som ikke finnes.

**Mitigeringsstrategier:**

- **RAG (Retrieval-Augmented Generation):** LLM-en
  kobles mot en verifisert kunnskapsbase og
  genererer svar basert på faktisk dokumentasjon
  snarere enn intern «hukommelse». Dette reduserer,
  men eliminerer ikke, risikoen for feil.
- **Human-in-the-loop:** Menneskelig fagekspertise i
  kvalitetssikringen av alle KI-genererte produkter,
  med tydelige prosesser for godkjenning før
  publisering.
- **Automatisert faktasjekk:** Kryssverifisering av
  påstander mot etablerte kilder.

### 4.2 Tillit og legitimitet

Bruk av KI i helseinformasjon berører flere
tillitsdimensjoner:

**Innbyggernes tillit:** Undersøkelser tyder på at
befolkningen har varierende tillit til KI-generert
helseinformasjon. Noen studier indikerer at
innbyggere foretrekker informasjon de oppfatter som
skrevet av mennesker, selv når KI-generert
informasjon objektivt sett er likeverdig. Transparens
om KI-bruk kan både styrke og svekke tillit, avhengig
av kontekst og kommunikasjon.

**Helsepersonells aksept:** Helsepersonell som skal
bruke KI-støttede verktøy må ha tillit til
systemenes pålitelighet. Tidlige erfaringer tyder på
at aksepten er høyere når KI presenteres som et
støtteverktøy som fagpersonell kan overprøve, snarere
enn et autonomt beslutningssystem.

**Institusjonell legitimitet:** For Helsedirektoratet
som fagmyndighet er det avgjørende at KI-bruk ikke
undergraver myndighetens troverdighet. Dersom
innbyggere opplever at helseråd «bare er generert av
en maskin», kan det svekke tilliten til offentlig
helseinformasjon generelt. Tydelig kommunikasjon om
hvordan KI brukes – og om at fagpersoner alltid har
det endelige ansvaret – er nødvendig.

### 4.3 Bias og rettferdighet

LLM-er trenes på store tekstkorpus som reflekterer
eksisterende skjevheter i medisinsk forskning og
samfunnet for øvrig:

- **Underrepresentasjon:** Minoritetsgrupper, kvinner
  og eldre er historisk underrepresentert i kliniske
  studier. KI-modeller som trenes på denne
  litteraturen kan reprodusere og forsterke slike
  skjevheter.
- **Språkbias:** De fleste ledende LLM-er er primært
  trent på engelskspråklig tekst. Ytelsen på norsk
  er typisk lavere, og modellene kan ha begrenset
  forståelse av norsk helsekontekst, organisering
  og terminologi.
- **Kulturell bias:** Helseråd som er tilpasset én
  kulturell kontekst er ikke nødvendigvis
  overførbare til norske forhold. LLM-er kan
  generere anbefalinger som er fornuftige i en
  amerikansk kontekst men irrelevante eller
  misvisende i Norge.

### 4.4 Personvern og datasikkerhet

Helsedata er klassifisert som særlig sensitive
personopplysninger under GDPR artikkel 9. Bruk av
LLM-er i kunnskapsforvaltning reiser flere
personvernspørsmål:

- **Skytjenester:** De mest kapable LLM-ene tilbys
  som skytjenester fra amerikanske selskaper.
  Overføring av helsedata til slike tjenester krever
  særskilt rettslig grunnlag og risikovurdering.
- **Nasjonal kontroll:** Det er et prinsipielt
  spørsmål om kritisk infrastruktur for
  helseinformasjon bør avhenge av utenlandske
  leverandører og modeller som norske myndigheter
  har begrenset innsyn i.
- **Treningsdata:** Spørsmål om hvorvidt data som
  sendes til skytjenester kan bli brukt til videre
  modelltrening, krever avtalemessige og tekniske
  avklaringer.

For kunnskapsforvaltning – i motsetning til klinisk
beslutningsstøtte – vil mye av arbeidet handle om
offentlig tilgjengelig forskning snarere enn
individuelle pasientdata. Dette reduserer
personvernrisikoen for flere bruksområder, men
fjerner den ikke helt, spesielt dersom modellene
skal brukes med kontekstuell informasjon.

### 4.5 Juridiske risikoer

**Ansvar ved feil:** Dersom KI-generert
helseinformasjon fører til skade, oppstår spørsmål
om hvem som er ansvarlig. Helsedirektoratet som
avsender av informasjonen vil sannsynligvis bære
ansvaret uavhengig av om innholdet er generert av KI
eller mennesker – men dette er foreløpig rettslig
uavklart.

**Regulatorisk usikkerhet:** EU AI Act trådte i kraft
i 2024, men flere sentrale bestemmelser har trinnvis
ikrafttredelse frem til 2027. Det gjenstår å se
hvordan reglene vil bli tolket og håndhevet i
praksis, spesielt i grensesnittet mellom
helseinformasjon og medisinsk utstyr.

**Medisinsk utstyr eller ikke?** Et sentralt
grensedragningsspørsmål er om et KI-system som gir
helseråd til innbyggere klassifiseres som medisinsk
utstyr etter MDR (Medical Device Regulation).
Informasjonssystemer faller normalt utenfor, men jo
mer personaliserte og handlingsrettede rådene er,
desto nærmere kommer man grensen for medisinsk
utstyr.

---

## 5. EU AI Act – implikasjoner for helsesektoren

### Risikoklassifisering

EU AI Act klassifiserer KI-systemer i risikonivåer.
KI-systemer som er sikkerhetskomponenter i medisinsk
utstyr klassifiseres som **høyrisiko**. For
kunnskapsforvaltning i helse avhenger
klassifiseringen av systemets konkrete bruk:

- **Generell helseinformasjon** (f.eks. oppsummering
  av retningslinjer): Sannsynligvis ikke høyrisiko
- **Personaliserte helseråd:** Kan falle inn under
  høyrisiko, avhengig av grad av personalisering og
  medisinsk innhold
- **Klinisk beslutningsstøtte:** Typisk høyrisiko

### Krav til høyrisiko KI-systemer

For systemer som klassifiseres som høyrisiko, stiller
EU AI Act krav om:

- **Risikostyringssystem:** Løpende identifisering
  og håndtering av risikoer
- **Datakvalitet:** Trenings-, validerings- og
  testdata skal være relevante, representative og
  frie for feil
- **Teknisk dokumentasjon:** Detaljert dokumentasjon
  av systemets virkemåte og begrensninger
- **Logging:** Automatisk registrering av hendelser
  for sporbarhet
- **Transparens:** Brukere skal informeres om at de
  interagerer med et KI-system, og om systemets
  evner og begrensninger
- **Menneskelig tilsyn:** Systemet skal utformes slik
  at mennesker kan overstyre det
- **Nøyaktighet og robusthet:** Systemet skal
  fungere konsistent og pålitelig

### Samsvar med medisinsk utstyr-forordning

EU AI Act krever at KI-systemer som klassifiseres som
medisinsk utstyr også oppfyller kravene i MDR. Dette
innebærer samsvarsvurdering, CE-merking og
oppfølging etter markedsføring. For
kunnskapsforvaltningssystemer er det avgjørende å
avklare om og i hvilken grad MDR-kravene kommer til
anvendelse.

### Implikasjoner for norsk implementering

Som EØS-land vil Norge implementere EU AI Act. I
kombinasjon med EHDS innebærer dette at norske
helsemyndigheter må:

- Kartlegge hvilke eksisterende og planlagte
  KI-systemer som faller inn under
  reguleringsregimet
- Etablere prosesser for samsvarsvurdering og tilsyn
- Sikre at KI-systemer som brukes i verdikjeden for
  kunnskapsforvaltning oppfyller kravene til
  transparens, datakvalitet og menneskelig tilsyn
- Vurdere behovet for nasjonal veiledning om
  grensedragningen mellom helseinformasjon og
  medisinsk utstyr

### Tidsplan

EU AI Act har trinnvis ikrafttredelse:

- **Februar 2025:** Forbud mot uakseptabel risiko
- **August 2025:** Krav til generelle KI-modeller
  (GPAI)
- **August 2026:** Hovedkravene for
  høyrisiko-systemer
- **August 2027:** Utvidede krav for
  høyrisiko-systemer som også er medisinsk utstyr

Denne tidsplanen gir norske aktører en avgrenset
periode til å forberede seg, men arbeidet bør starte
tidlig gitt kompleksiteten i helsedomenet.

---

## 6. Prinsipielle spørsmål

Innføring av LLM-er i kunnskapsforvaltning i helse
reiser flere prinsipielle spørsmål som krever
politisk og faglig avklaring:

**Bør offentlige helsemyndigheter bruke KI i
kunnskapsproduksjon?**
Spørsmålet er ikke lenger om KI vil bli tatt i
bruk – det skjer allerede – men hvordan offentlige
myndigheter skal forholde seg til teknologien.
Alternativet til styrt innføring er ikke fravær av
KI, men ukontrollert bruk av kommersielle KI-verktøy
uten kvalitetssikring og governance.

**Hvor går grensen mellom KI-støtte og
KI-autonomi?**
Det er en vesentlig forskjell mellom KI som
assisterer en fagperson (foreslår, sorterer,
oppsummerer) og KI som produserer ferdige helseråd
uten menneskelig gjennomgang. For
kunnskapsforvaltning i en myndighetsrolle bør
prinsippet om menneskelig tilsyn stå sentralt, i
tråd med EU AI Acts krav.

**Hvem har ansvar når KI bidrar til feilaktige
helseråd?**
Selv med menneskelig tilsyn kan feil slippe gjennom.
Det er behov for tydelig ansvarsallokering, både
juridisk og organisatorisk. Helsedirektoratets rolle
som fagmyndighet tilsier at direktoratet vil bære
ansvaret for innholdet uavhengig av
produksjonsmetode.

**Hvordan sikre demokratisk kontroll over KI i
helse?**
KI-systemer som påvirker offentlig helseinformasjon
bør være underlagt demokratisk kontroll. Dette
inkluderer innsyn i hvordan systemene fungerer,
mulighet for offentlig debatt om bruksområder, og
politisk styring av rammer og grenser.

**Bør Norge utvikle egne modeller eller bruke
kommersielle?**
Det er et strategisk valg mellom å bruke
kommersielle modeller (raskere, mer kapable, men
avhengig av utenlandske leverandører) og å investere
i egne eller nordiske modeller (større kontroll, men
høyere kostnad og sannsynligvis lavere ytelse på kort
sikt). En mellomvei kan være å bruke kommersielle
modeller med nasjonalt kontrollerte kunnskapsbaser
gjennom RAG-arkitekturer.

---

## 7. Oppsummering

Store språkmodeller representerer en teknologi med
betydelig potensial for å forbedre
kunnskapsforvaltning i helsesektoren. De mest
lovende bruksområdene – akselerert
kunnskapssyntese, retningslinjestøtte, forbedret
innbyggerinformasjon og kontinuerlig
kunnskapsoppdatering – adresserer reelle og
dokumenterte utfordringer i dagens verdikjede.

Samtidig medfører teknologien vesentlige risikoer.
Hallusinering, tillitsutfordringer, bias,
personvernhensyn og juridisk usikkerhet er ikke
hypotetiske bekymringer, men konkrete
problemstillinger som må håndteres før og under
innføring.

Nøkkelen til vellykket bruk av LLM-er i
kunnskapsforvaltning ligger i tre forhold:

1. **Governance:** Tydelige rammer for hvilke
   bruksområder som er akseptable, hvem som har
   beslutningsmyndighet, og hvordan KI-bruk styres
   og kontrolleres.
2. **Kvalitetssikring:** Robuste prosesser for
   menneskelig gjennomgang av KI-generert innhold,
   med særlig vekt på faktasjekk og
   kildeverifisering.
3. **Menneskelig tilsyn:** Prinsippet om at
   fagpersoner alltid har det endelige ansvaret for
   innholdet som publiseres, i tråd med EU AI Acts
   krav.

EU AI Act gir et regulatorisk rammeverk som norske
helsemyndigheter må forholde seg til, og som gir
nyttige føringer for ansvarlig innføring av KI. Den
trinnvise ikrafttredelsen gir et tidsvindu for
forberedelse, men arbeidet med å etablere
governance-strukturer, kvalitetssikringsprosesser og
kompetanse bør starte umiddelbart.

Delrapport 4 vil bygge videre på denne analysen og
beskrive en konkret ny verdikjede for
kunnskapsforvaltning med KI-støtte, der mulighetene
og risikoene som er beskrevet her adresseres gjennom
arkitektur, prosesser og organisering.
