# Helsepersonellvurdering: EHDS-konsekvenser for klinisk arbeidshverdag

## Sammendrag

Denne rapporten vurderer konsekvensene av EHDS-implementering i Norge sett fra helsepersonells perspektiv. Vurderingen dekker de tre tiltaksalternativene som er beskrevet i *tiltaksalternativer-ehds.md* og tar utgangspunkt i helsepersonells faktiske arbeidshverdag.

**Hovedfunn:**

- EHDS har potensial til a gi helsepersonell bedre tilgang til pasientinformasjon, saerlig i grensekryssende scenarioer og ved akuttbehandling av utenlandske pasienter. Dette er en reell klinisk gevinst.
- Innforing av strukturerte datakrav (EEHRxF) vil sannsynligvis oke dokumentasjonsbyrden pa kort sikt, i en sektor der helsepersonell allerede bruker uforholdsmessig mye tid pa dokumentasjon. Helsedirektoratets helsepersonellundersokelse fra 2024 viser at kun 52 % av helsepersonell er tilfredshorte med sine EPJ-systemer, og tilfredsheten falt fra 2023 til 2024.
- Erfaringene fra Helseplattformen i Midt-Norge viser at store systemendringer i helsesektoren medforer betydelig risiko for helsepersonells arbeidshverdag og pasientsikkerhet. Disse erfaringene ma tas pa alvor ved EHDS-implementering.
- Alternativ 1 (stegvis minimum) gir minst endring i arbeidshverdagen, men risikerer at helsepersonell ma forholde seg til dualiteten mellom nasjonale og europeiske formater. Alternativ 2 (akselerert helhetlig) gir storst langsiktig gevinst, men medforer hoy endringsbelastning. Alternativ 3 (nordisk samarbeid) kan gi bedre losninger gjennom erfaringsdeling.
- Det er avgjorende at helsepersonell involveres aktivt i utforming og implementering av EHDS-losninger, og at klinisk nytte -- ikke bare juridisk etterlevelse -- er styrende for designvalg.

---

## 1. Pavirkning pa klinisk arbeidshverdag

### 1.1 Dokumentasjonsbyrde

**Dagens situasjon er allerede krevende.** Internasjonal forskning viser at leger bruker opptil 49 % av arbeidsdagen pa EPJ og skrivebordsarbeid, mot 27 % pa direkte pasientkontakt (PMC/scoping review, 2024). I Norge bruker sykepleiere i snitt 120 minutter -- to timer -- per arbeidsdag pa EPJ, ifølge en undersøkelse blant 1805 medlemmer av Norsk Sykepleierforbund publisert i Sykepleien i 2024. Helsedirektoratets helsepersonellundersøkelse 2024 viser fallende tilfredshet med EPJ-systemer blant helsepersonell.

**EHDS vil kreve mer strukturert dokumentasjon.** Det europeiske utvekslingsformatet (EEHRxF) forutsetter at helseopplysninger registreres i strukturerte, kodede formater. I dag bruker norsk helsepersonell en blanding av fritekst og strukturerte felt. Overgangen til mer strukturert dokumentasjon kan oppleves som en begrensning av klinisk presisjon -- et poeng Legeforeningens IT-utvalg har fremhevet, der Petter Hurlen har stilt spørsmål ved om standardisert sprak kan erstatte legers fagsprak og kliniske presisjon.

**Risiko for dobbeltdokumentasjon.** Ved alternativ 1, der nasjonale standarder beholdes parallelt med EEHRxF for grensekryssende bruk, risikerer man at helsepersonell ma dokumentere i to formater -- eller at automatisk konvertering i gateway-laget introduserer feil som krever manuell korrigering. Erfaringene med Kjernejournal har allerede vist at dokumentasjon av kritisk informasjon i separate systemer medforer dobbeltdokumentasjon som er uforenlig med onsket om en enklere hverdag for helsepersonell.

**Muligheter for reduksjon av dokumentasjonsbyrde.** EHDS kan pa lengre sikt redusere byrden ved at informasjon registreres en gang og gjenbrukes pa tvers av systemer og landegrenser. EUs eget konsekvensnotat peker pa at interoperabilitet eliminerer repetitiv dataregistrering. Men dette forutsetter at implementeringen gjores riktig -- med fokus pa klinisk arbeidsflyt, ikke bare teknisk etterlevelse.

**Vurdering:** Pa kort og mellomlang sikt (2027-2031) vil EHDS sannsynligvis oke dokumentasjonsbyrden for helsepersonell. Pa lang sikt kan byrden reduseres dersom «registrer en gang, bruk mange ganger»-prinsippet realiseres fullt ut. Risikoen for okt byrde er hoyest ved alternativ 2, der hele det nasjonale standardregimet legges om.

### 1.2 Informasjonstilgang

**Betydelig gevinst ved grensekryssende behandling.** EHDS vil gi helsepersonell tilgang til pasientoppsummeringer, medisinlister, allergier og annen kritisk informasjon om pasienter fra andre EU/EOS-land. Dette er en reell klinisk forbedring, spesielt for:
- Akuttmottak som tar imot utenlandske pasienter (turister, arbeidsinnvandrere, grensearbeidere)
- Helsetjenester i grenseomrader (sarlig mot Sverige og Finland)
- Oppfolging av pasienter som har mottatt behandling i utlandet

**Forbedret nasjonal informasjonstilgang (ved alternativ 2).** Dersom FHIR innfores som nasjonal standard, vil dette ogsa forbedre informasjonstilgangen mellom norske virksomheter -- noe som i dag er en kjent utfordring i det fragmenterte norske informasjonslandskapet.

**Risiko for informasjonsoverbelastning.** Mer informasjon er ikke alltid bedre. Helsepersonell risikerer a bli overveldet av store mengder data fra ulike kilder, i ulike formater og pa ulike sprak. God presentasjon og filtrering i EPJ-systemene blir avgjorende. Uten dette kan mer informasjon faktisk svekke pasientsikkerheten ved at viktig informasjon «drukner» i storyen.

**Vurdering:** Informasjonstilgangen vil forbedres, men gevinsten avhenger sterkt av hvordan informasjonen presenteres i EPJ-systemene helsepersonell bruker. Uten investering i brukergrensesnitt og klinisk tilpasning kan okt datamengde bli en belastning snarere enn en ressurs.

### 1.3 Arbeidsflyt

**Nye elementer i klinisk arbeidsflyt.** EHDS vil introdusere flere nye elementer:
- Haandtering av pasientenes opt-out/tilgangsreservasjon -- helsepersonell ma forholde seg til at pasienter kan begrense tilgang til sine opplysninger, ogsa i akutte situasjoner
- Mottak og vurdering av helseinformasjon fra andre land, muligens pa andre sprak
- Nye rutiner for dokumentasjon som sikrer at informasjonen er kompatibel med EEHRxF
- Endret samhandling med pasienter som har tilgang til og kan laste ned sine helseopplysninger i europeisk format

**Forstyrrelser i innarbeidede rutiner.** Helsepersonell har over ar utviklet effektive arbeidsrutiner tilpasset sine EPJ-systemer. Endringer i disse systemene -- enten det er nye felt, nye skjermbilder eller nye arbeidsprosesser -- medforer en omstillingsperiode der effektiviteten faller. Forskning viser at navigasjon i EPJ med dype menyhierarkier og lite intuitive merkelapper dobler antall klikk som trengs for a na riktig dokumentasjonsfelt, og feilregistrering forekom i 17 % av observerte oppgaver.

**Forenklinger pa sikt.** Dersom EHDS realiserer sin ambisjon om sømlos informasjonsdeling, kan dette forenkle arbeidsflyter knyttet til innhenting av informasjon fra andre virksomheter -- noe som i dag ofte krever telefoner, fakser eller manuell bestilling av papirkopier.

**Vurdering:** Arbeidsflyten vil endres. Pa kort sikt betyr dette okt kompleksitet og behov for ny laering. Pa lang sikt kan forenklinger oppna som folge av bedre interoperabilitet, men dette er ikke garantert.

---

## 2. Brukervennlighet

### 2.1 Systemendringer

**Pavirkning pa eksisterende EPJ-systemer.** Alle EPJ-systemer i bruk i Norge vil matte tilpasses for a stotte EEHRxF:

- **DIPS Arena** (de fleste helseforetak): Ma utvides med FHIR-stotte og EEHRxF-kompatible grensesnitt. Risiko for at nye moduler pavirker eksisterende funksjonalitet.
- **Helseplattformen/Epic** (Midt-Norge): Epic har internasjonal FHIR-stotte, men tilpasning til norske og europeiske krav vil likevel kreve konfigurasjon og utvikling. Gitt de eksisterende utfordringene med Helseplattformen, kan ytterligere endringer vaere sarlig krevende for helsepersonell i Midt-Norge.
- **CGM, Visma, Infodoc** (primaerhelsetjenesten): Disse systemene har varierende teknisk modenhet. Tilpasning til EEHRxF kan bli betydelig, og kapasiteten hos leverandorene er usikker.

**Erfaringer fra Helseplattformen.** Innforingen av Epic i Midt-Norge har gitt verdifulle, men ogsa smertefulle erfaringer. Tidsskriftet for Den norske legeforening omtalte Helseplattformen som «en IT-skandale i Midt-Norge». Rapporter viser at Helseplattformen har gjort helsepersonell mindre effektive, og Datatilsynet har pavist vesentlige mangler og brudd pa personvernreglene. Disse erfaringene viser tydelig risikoen ved store systemendringer i helsesektoren: selv med gode intensjoner kan resultatet bli lengre arbeidsdager, dyrere drift og svekket pasientsikkerhet.

**Vurdering:** Systemendringer er uunngaelige, men ma gjennomfores med stor varsomhet. Helsepersonell ma involveres tidlig i design og testing av nye grensesnitt. Erfaringene fra Helseplattformen ma brukes aktivt som laeringspunkter.

### 2.2 Nye grensesnitt

**Pasientens tilgangsportal.** EHDS gir pasienter rett til a se, laste ned og begrense tilgang til sine helseopplysninger. Dette vil sannsynligvis integreres i helsenorge.no, men helsepersonell ma haandtere konsekvensene: pasienter som har lest sine journaler og stiller sporsmal, pasienter som har begrenset tilgang til informasjon, og pasienter som onsker a dele informasjon fra behandling i utlandet.

**Grensekryssende informasjonsvisning.** Helsepersonell vil trenge nye visninger i sine EPJ-systemer for a se pasientoppsummeringer fra andre EU/EOS-land. Disse ma vaere intuitive, tydelig merket med opprinnelsesland, og oversatt eller presentert pa en forstaelig mate.

**Reservasjonsmekanismer.** Helsepersonell ma forholde seg til pasienters reservasjonsvalg og forstå hva som er tilgjengelig og hva som er begrenset. I akutte situasjoner ma det vaere klare prosedyrer for overprøving av reservasjoner.

**Vurdering:** Nye grensesnitt kan gi bedre funksjonalitet, men hvert nytt grensesnitt er ogsa en ny kilde til forvirring og feil. Designet ma ta utgangspunkt i kliniske behov, ikke i regulatoriske krav alene.

### 2.3 Opplaeringsbehov

**Omfanget av opplaering vil vaere betydelig.** Helsepersonell ma laere:
- Nye dokumentasjonskrav og strukturerte formater
- Nye funksjoner i EPJ-systemene
- Haandtering av grensekryssende pasientinformasjon
- Pasientrettigheter under EHDS (tilgang, reservasjon, nedlasting)
- Nye rutiner for informasjonssikkerhet og personvern

**Differensiert opplaeringsbehov.** Ulike yrkesgrupper og ulike arbeidssteder vil ha ulikt opplaeringsbehov. Akuttmottak med mange utenlandske pasienter har storre behov for opplaering i grensekryssende funksjonalitet enn en kommunal hjemmetjeneste.

**Opplaering ma vaere praksisnaer.** Helsedirektoratets helsepersonellundersokelse 2024 viser at digitale ferdigheter varierer betydelig blant helsepersonell. Opplaering ma vaere tilpasset den enkeltes forutsetninger og integrert i klinisk praksis, ikke bare e-laeringskurs.

**Vurdering:** Opplaeringsbehovet er betydelig og ma planlegges tidlig. Utilstrekkelig opplaering var en av kritikkpunktene ved Helseplattformen-innforingen, og feilen ma ikke gjentas ved EHDS-implementering. Legeforeningen har vaert tydelig pa at digitalisering ma forankres i klinisk praksis.

---

## 3. Pasientsikkerhet

### 3.1 Bedre informasjonstilgang

**Tilgang til kritisk informasjon om utenlandske pasienter.** I dag behandles utenlandske pasienter i Norge ofte uten tilgang til deres medisinske historikk, medisinliste eller allergier. EHDS vil gjore denne informasjonen tilgjengelig gjennom MyHealth@EU, noe som er en direkte forbedring av pasientsikkerheten.

**Pasientoppsummeringer (Patient Summary).** Fra 2029 (gruppe 1) skal pasientoppsummeringer vaere tilgjengelige pa tvers av landegrensene. Dette inkluderer allergier, aktive diagnoser, medisinliste og andre kritiske opplysninger. For helsepersonell som behandler en bevisstlos utenlandsk turist eller en kronisk syk arbeidsinnvandrer, kan dette vaere forskjellen pa riktig og feil behandling.

**E-resept pa tvers av landegrenser.** Grensekryssende e-resept og e-dispensering vil gjore det mulig a forsikre seg om hva pasienten faktisk bruker av legemidler, redusere risiko for interaksjoner og gi et mer komplett bilde av pasientens medisinbruk.

**Vurdering:** Den pasientsikkerhetsmessige gevinsten av EHDS er reell og bor kommuniseres tydelig til helsepersonell. Bedre informasjon gir bedre beslutninger.

### 3.2 Nye risikoer

**Sprakbarrierer.** Pasientinformasjon fra andre land vil vaere kodet med internasjonale terminologier (SNOMED CT, ICD, ATC), men fritekstfelt og kliniske notater vil vaere pa originalspraket. Helsepersonell risikerer a miste kontekst eller misforsta informasjon. Automatisk oversettelse kan introdusere feil.

**Konverteringsfeil.** Ved alternativ 1, der en gateway konverterer mellom nasjonale formater og EEHRxF, er det risiko for tap eller forvrengning av informasjon. Automatisk mapping mellom ulike kodesystemer er ikke feilfritt, og konverteringsfeil kan ha kliniske konsekvenser.

**Falsk trygghet.** Helsepersonell kan stole pa at informasjonen fra et annet land er komplett, nar den i virkeligheten kun representerer et utvalg. Pasientoppsummeringen er ikke det samme som en fullstendig journal, og forventningsstyring er viktig.

**Informasjonskvalitet.** Kvaliteten pa helsedata varierer mellom EU/EOS-land. Helsepersonell ma vaere klar over at informasjon fra et annet land kan vaere ufullstendig, utdatert eller strukturert etter andre kliniske tradisjoner.

**Vurdering:** De nye risikoene er haandterbare, men krever bevissthet, opplaering og gode systemdesign. Det ma vaere tydelig for helsepersonell hva slags informasjon de ser, hvor den kommer fra, og hva som eventuelt mangler.

### 3.3 Akuttsituasjoner

**Storst gevinst i akutte scenarioer.** Tilgang til pasientoppsummeringer, allergier og medisinlister ved akutt behandling av utenlandske pasienter er kanskje den mest apenbare kliniske gevinsten av EHDS. I dag ma helsepersonell ofte basere seg pa pasientens egen hukommelse (dersom pasienten er ved bevissthet) eller behandle uten informasjon.

**Utfordringer med tilgang i pressede situasjoner.** I akutte situasjoner er tid kritisk. Systemene ma designes slik at tilgang til grensekryssende informasjon er rask og enkel -- ikke bak flere innlogginger, samtykkesjekker eller trege systemresponser. Reservasjonsmekanismer ma ha klare overprovingsregler for akutte situasjoner.

**Vurdering:** Akuttscenarioer bor vaere et designprinsipp for EHDS-implementeringen: systemene ma fungere nar det haster mest. Brukergrensesnittet ma gjore det mulig a fa tilgang til kritisk informasjon innen sekunder, ikke minutter.

---

## 4. Vurdering per yrkesgruppe

### 4.1 Sykehusleger

**Pavirkning: Middels til hoy.**

Sykehusleger vil merke EHDS gjennom:
- Nye dokumentasjonskrav for strukturert registrering i EEHRxF-kompatible felt
- Tilgang til pasientinformasjon fra andre land (sarlig pa akuttmottak, i grensenare sykehus og ved poliklinisk behandling av utenlandske pasienter)
- Endringer i EPJ-systemene (DIPS Arena eller Helseplattformen/Epic)
- Nye krav til haandtering av pasientens reservasjonsvalg

**Sarlige bekymringer:**
- Legeforeningen har tydelig signalisert at digitalisering ma forankres i klinisk praksis, og at brukervennlighet er pasientsikkerhet, ikke luksus
- Tiden leger bruker pa EPJ er allerede for hoy -- ytterligere dokumentasjonskrav uten tilsvarende forenklinger vil mote sterk motstand
- Erfaringer fra Helseplattformen viser at sykehusleger er spesielt sarbare for store systemendringer

**Anbefalinger for denne gruppen:**
- Involver sykehusleger i utforming av nye EPJ-grensesnitt
- Vurder bruk av KI-stottet dokumentasjon for a kompensere for okte struktureringskrav
- Sikre at EHDS-relaterte endringer testes grundig i klinisk praksis for utrulling

### 4.2 Fastleger

**Pavirkning: Lav til middels.**

Fastleger vil i mindre grad berores av grensekryssende funksjonalitet (færre utenlandske pasienter i lopende behandling), men vil pavirkes av:
- Endringer i EPJ-systemer (CGM, Visma, Infodoc)
- Okte krav til strukturert dokumentasjon
- Nye krav til pasientoppsummeringer som del av gruppe 1 (2029)
- Oppfolging av pasienter som har mottatt e-resept i utlandet

**Sarlige bekymringer:**
- Fastlegene har allerede en presset arbeidshverdag med mange dokumentasjonskrav
- Helsedirektoratets helsepersonellundersokelse viser at fastleger (80 %) er mer tilfredse med sine EPJ-systemer enn gjennomsnittet -- noe som betyr at de har mer a tape pa systemendringer
- Leverandorsituasjonen i primaerhelsetjenesten er fragmentert, og risikoen for ulik kvalitet pa EHDS-tilpasning er hoy

**Anbefalinger for denne gruppen:**
- Prioriter minimal forstyrrelse av fastlegenes arbeidsflyt
- Sikre at EPJ-leverandorene i primaerhelsetjenesten far tydelige spesifikasjoner og tilstrekkelig tid til tilpasning
- Utnytt fastlegenes hoye EPJ-tilfredshet ved a bygge EHDS-funksjonalitet inn i eksisterende arbeidsflyter

### 4.3 Sykepleiere

**Pavirkning: Middels.**

Sykepleiere bruker allerede to timer per dag pa EPJ-dokumentasjon ifølge NSFs undersøkelse. EHDS kan pavirke dem gjennom:
- Okte krav til strukturert dokumentasjon, sarlig for pasientoppsummeringer og epikriser
- Nye felt og skjermbilder i EPJ-systemene
- Haandtering av pasienters reservasjonsvalg i daglig pleie

**Sarlige bekymringer:**
- Sykepleiere har allerede en betydelig dokumentasjonsbyrde -- ytterligere tid pa EPJ gar direkte utover pasientnaer tid
- NSF har vaert tydelig pa at sykepleiere ma involveres i valg og utvikling av teknologiske losninger
- Kommunale sykepleiere bruker ofte EPJ-systemer med lavere modenhet og darligere brukervennlighet

**Anbefalinger for denne gruppen:**
- Gjennomfor konsekvensanalyse av nye dokumentasjonskrav for sykepleieres tidsbruk
- Prioriter forenklinger i dokumentasjonsflyten som kompenserer for EHDS-relaterte tillegg
- Involver sykepleiere i testing av nye EPJ-grensesnitt

### 4.4 Helsefagarbeidere i kommunal omsorg

**Pavirkning: Lav.**

Helsefagarbeidere i kommunal omsorg vil i begrenset grad berores direkte av EHDS, men kan oppleve:
- Endringer i kommunale EPJ-systemer (som allerede er under utskifting mange steder)
- Nye krav til dokumentasjon i hjemmetjeneste og sykehjem
- Behov for opplaering i nye systemer og rutiner

**Sarlige bekymringer:**
- Kommunesektoren har de storste utfordringene med EPJ-systemer som ikke stotter arbeidshverdagen tilstrekkelig
- Digital kompetanse varierer betydelig i denne yrkesgruppen
- Mange kommuner planlegger allerede EPJ-bytte -- EHDS-krav kan komme pa toppen av dette

**Anbefalinger for denne gruppen:**
- Koordiner EHDS-tilpasning med pagaende EPJ-utskiftinger i kommunene
- Tilby praktisk, praksisnaer opplaering tilpasset yrkesgruppens forutsetninger
- Begrens direkte EHDS-eksponering til det strengt nodvendige

### 4.5 Apotek/farmasoyter

**Pavirkning: Middels til hoy (for e-resept/e-dispensering).**

Farmasoyter vil vaere blant de forste som merker EHDS i praksis, fordi e-resept og e-dispensering er i gruppe 1 (2029):
- Grensekryssende e-resepter: farmasoyter ma kunne motta og ekspedere resepter utstedt i andre EU/EOS-land
- Nye krav til verifikasjon av utenlandske resepter
- Endringer i apoteksystemene for a stotte europeiske formater

**Sarlige bekymringer:**
- Sprakbarrierer ved ekspedisjon av utenlandske resepter
- Ulike legemiddelnavn, styrker og formuleringer pa tvers av land
- Behov for a verifisere at utenlandske legemidler har norsk markedsforing eller godkjent alternativ

**Anbefalinger for denne gruppen:**
- Utvikle tydelige retningslinjer og oppslagesverk for grensekryssende reseptekspedisjon
- Sikre at apoteksystemene viser legemiddelinformasjon pa en entydig mate uavhengig av opprinnelsesland
- Planlegg opplaering i god tid for 2029-fristen

---

## 5. Vurdering per alternativ

### 5.1 Alternativ 1 -- Fra helsepersonells perspektiv

**Fordeler:**
- Minst mulig endring i daglig arbeidsflyt -- nasjonale standarder beholdes for nasjonal bruk
- Lavere opplaeringsbehov pa kort sikt
- Eksisterende EPJ-systemer endres minimalt
- Helsepersonell trenger i stor grad bare a forholde seg til grensekryssende funksjonalitet nar det er klinisk relevant

**Ulemper:**
- Gateway-tilnaermingen kan gi konverteringsfeil som pavirker pasientsikkerheten
- Helsepersonell ma forholde seg til at informasjon som sendes ut av landet kan miste presisjon i konverteringen
- Dualiteten mellom nasjonale og europeiske formater kan skape forvirring
- Den nasjonale nytteverdien er lav -- informasjonsutveksling mellom norske virksomheter forbedres ikke
- Over tid kan opprettholdelse av to parallelle standarder gi hoyere kompleksitet for helsepersonell

**Samlet vurdering fra helsepersonellperspektiv:** Det minst forstyrrende alternativet pa kort sikt, men gir begrenset positiv effekt pa arbeidshverdagen. Risiko for at helsepersonell opplever EHDS som et rent byrakratisk prosjekt uten klinisk verdi.

### 5.2 Alternativ 2 -- Fra helsepersonells perspektiv

**Fordeler:**
- En nasjonal FHIR-standard vil pa sikt forbedre informasjonsutveksling ogsa mellom norske virksomheter -- en reell gevinst for helsepersonell
- Eliminerer dualiteten mellom nasjonale og europeiske formater
- Bredere modernisering kan gi anledning til a forbedre EPJ-brukervennlighet generelt
- Storre mulighet for KI-stottet dokumentasjon og beslutningsstotte basert pa strukturerte data
- Kompetanseprogrammet gir mulighet for systematisk opplaering

**Ulemper:**
- Hoy endringsbelastning over kort tid -- risiko for «endringstretthet»
- Erfaringene fra Helseplattformen viser at store, samtidige endringer i EPJ-systemer kan vaere svart krevende for helsepersonell
- Risiko for at endringene drives av tekniske og regulatoriske hensyn fremfor kliniske behov
- Hogere risiko for uforutsette problemer og feil i overgangsfasen
- Endringsmotstand fra helsepersonell som har investert tid i a laere eksisterende systemer

**Samlet vurdering fra helsepersonellperspektiv:** Storst langsiktig potensial, men ogsa storst kortsiktig risiko. Forutsetter sterk klinisk forankring, god involverning av helsepersonell og realistisk tidsplan. Hvis det gjores darlig, kan det bli «Helseplattformen i nasjonal skala».

### 5.3 Alternativ 3 -- Fra helsepersonells perspektiv

**Fordeler:**
- Nordisk erfaringsdeling kan gi bedre losninger basert pa andres feil og suksesser
- Felles nordisk leverandordialog kan sikre bedre kvalitet pa EPJ-tilpasninger (flere nordiske leverandorer opererer i flere land)
- Felles nordisk kompetanseprogram kan gi mer robust opplaering
- Koordinert tilnaerming gir storre gjennomslagskraft overfor EU nar det gjelder a ivareta kliniske hensyn

**Ulemper:**
- Risiko for at nordisk koordinering forsinker nasjonale beslutninger og implementering
- Kompromisslosninger som ikke er optimale for norske forhold
- Ekstra kompleksitet i styringsstruktur som kan gjore det vanskeligere a ivareta helsepersonells behov

**Samlet vurdering fra helsepersonellperspektiv:** Et godt supplement til enten alternativ 1 eller 2, saerlig fordi erfaringsdeling kan redusere risikoen for implementeringsfeil. Bor ikke brukes som begrunnelse for a utsette nasjonale beslutninger.

---

## 6. Anbefalinger

Basert pa analysen over, fremmes folgende anbefalinger for a ivareta helsepersonells interesser ved EHDS-implementering:

### 6.1 Involvering og medvirkning

1. **Etabler kliniske referansegrupper** med representanter fra alle berdrte yrkesgrupper (leger, sykepleiere, farmasoyter, helsefagarbeidere) som deltar i hele implementeringsprosessen -- fra kravspesifikasjon til testing og evaluering.

2. **Krev brukertesting med reelle kliniske scenarioer** for alle nye EPJ-grensesnitt og arbeidsflyter. Erfaringene fra Helseplattformen viser at utilstrekkelig klinisk testing medforer alvorlige konsekvenser.

3. **Gi Legeforeningen, NSF og andre fagorganisasjoner formell rolle** i styring og kvalitetssikring av implementeringen.

### 6.2 Dokumentasjonsbyrde

4. **Still krav om netto-nøytral dokumentasjonsbyrde.** For hvert nye dokumentasjonskrav som innfores, ma det identifiseres en forenkling som kompenserer. EHDS bor ikke oke total dokumentasjonstid for helsepersonell.

5. **Akseler bruk av KI-stottet dokumentasjon** (talegjenkjenning, automatisk strukturering av fritekst, forslag til kodeverkverdier) som kompenserende tiltak for okte struktureringskrav.

6. **Evaluer reell tidsbruk** pa EHDS-relatert dokumentasjon etter innforing, og juster losninger basert pa funn.

### 6.3 Opplaering

7. **Start opplaering tidlig** -- minst 12 maneder for innforing av nye systemer og funksjoner. Utilstrekkelig opplaeringstid var en sentral svakhet ved Helseplattformen.

8. **Gjor opplaering praksisnaer og differensiert** -- tilpasset ulike yrkesgrupper, arbeidsplasser og tekniske forutsetninger. E-laering alene er ikke tilstrekkelig.

9. **Alloker tid til opplaering innenfor arbeidstiden** -- ikke som tillegg til en allerede presset arbeidshverdag.

### 6.4 Pasientsikkerhet

10. **Design for akuttsituasjoner forst.** Tilgang til grensekryssende pasientinformasjon ma vaere rask og enkel -- maksimalt to klikk fra hovedskjermbildet i EPJ.

11. **Implementer tydelig merking av informasjonens opprinnelse og begrensninger** -- helsepersonell ma umiddelbart se at informasjonen kommer fra et annet land, hvilket land, og at den kan vaere ufullstendig.

12. **Utvikle klare retningslinjer for spraakbarrierer** ved mottak av grensekryssende informasjon, inkludert tilgang til medisinskfaglig oversettelse.

### 6.5 Implementeringsstrategi

13. **Laer av Helseplattformen.** Gjennomfor en systematisk erfaringsoppsummering fra innforingen i Midt-Norge og bruk funnene aktivt i EHDS-planleggingen.

14. **Velg trinnvis innforing** med mulighet for a justere underveis, fremfor «big bang»-utrulling. Alternativ 1 er minst risikabelt for helsepersonell pa kort sikt, men bor kombineres med en tydelig plan for videre utvikling.

15. **Maal og rapporter konsekvenser for helsepersonell** lopende -- ikke bare teknisk etterlevelse, men faktisk pavirkning pa arbeidshverdag, dokumentasjonstid og klinisk kvalitet.

16. **Bruk nordisk samarbeid (alternativ 3) aktivt** for erfaringsdeling uavhengig av valgt hovedalternativ, saerlig for a laere av land som innforer EHDS for Norge.

---

## Kilder

- [Helseplattformen -- en IT-skandale i Midt-Norge, Tidsskrift for Den norske legeforening (2023)](https://tidsskriftet.no/2023/01/leder/helseplattformen-en-it-skandale-i-midt-norge)
- [Rapport: Helseplattformen har gjort helsepersonell mindre effektive, mn24.no](https://www.mn24.no/nyheter/i/8pwEWw/rapport-helseplattformen-har-gjort-helsepersonell-mindre-effektive)
- [Vil avvikle Helseplattforma, NRK (2025)](https://www.nrk.no/trondelag/mdg-la-fram-forslag-om-a-avvikle-helseplattforma_-_-pa-tide-a-skjaere-bort-denne-it-svulsten-1.17795671)
- [Helsepersonellundersokelsen om digitalisering 2024, Helsedirektoratet](https://www.helsedirektoratet.no/rapporter/helsepersonellundersokelsen-om-digitalisering-i-helse-og-omsorgstjenesten-2024-bruk-av-holdninger-til-og-tilfredshet-med-digitale-helsetjenester)
- [Erfaringer og tilfredshet med EPJ-systemer, Helsedirektoratet (2024)](https://www.helsedirektoratet.no/rapporter/helsepersonellundersokelsen-om-digitalisering-i-helse-og-omsorgstjenesten-2024-bruk-av-holdninger-til-og-tilfredshet-med-digitale-helsetjenester/funn-og-analyser/erfaringer-og-tilfredshet-med-elektroniske-pasientjournalsystemer)
- [eHelse 2025: Brukervennlighet er ikke luksus, men pasientsikkerhet, Legeforeningen](https://www.legeforeningen.no/nyheter/2025/ehelse-2025-brukervennlighet-er-ikke-luksus-men-pasientsikkerhet/)
- [EHiN 2025: Digitalisering ma forankres i klinisk praksis, Legeforeningen](https://www.legeforeningen.no/nyheter/2025/ehin-2025-digitalisering-ma-forankres-i-klinisk-praksis/)
- [Sykepleiere bruker naermere to timer per arbeidsdag pa EPJ, Sykepleien (2024)](https://sykepleien.no/2024/09/sykepleiere-bruker-naermere-timer-arbeidsdag-pa-elektroniske-journalsystemer)
- [Informasjonsutveksling med redusert klinisk rapporteringsbyrde, Digdir/Stimulab](https://www.digdir.no/stimulab/direktoratet-e-helse-informasjonsutveksling-med-redusert-klinisk-rapporteringsbyrde/3604)
- [Usability Challenges in EHR: Impact on Documentation Burden and Clinical Workflow, PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12206486/)
- [EHDS Implementation guide for hospitals and healthcare professionals, Tiro Health](https://www.tiro.health/resources/european-health-data-space-ehds-implementation-guide-for-hospitals-and-healthcare-professionals)
- [EHDS: Stakeholder perspectives on implementation readiness, Better](https://www.better.care/document/ehds-implementation-readiness-report/)
- Tiltaksalternativer for EHDS-implementering i Norge (rapporter/tiltaksalternativer-ehds.md)
- Problemdefinisjon: EHDS og digitalisering av norsk helsesektor (rapporter/problemdefinisjon-ehds.md)

---

*Denne vurderingen er utarbeidet 15. mars 2026 og representerer et helsepersonellperspektiv pa EHDS-implementering. Vurderingen bor ses i sammenheng med de ovrige rapportene i prosjektet, sarlig tiltaksalternativer-ehds.md og problemdefinisjon-ehds.md. Vurderingen bor revideres nar gjennomforingsrettsakter fra EU-kommisjonen vedtas og mer detaljert informasjon om EPJ-leverandorenes planer foreligger.*
