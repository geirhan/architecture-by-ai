# Delrapport 2: Utfordringer og flaskehalser i verdikjeden for kunnskapsforvaltning

## Del av utredning om ny verdikjede for kunnskapsforvaltning i helsesektoren

---

## 1. Innledning

### 1.1 Formål

Denne rapporten kartlegger og analyserer utfordringer
og flaskehalser i dagens verdikjede for
kunnskapsforvaltning i helsesektoren. Kartleggingen
bygger på funn fra delrapport 1 (Dagens verdikjede)
og har som mål å identifisere de mest kritiske
hindringene for effektiv og rettidig
kunnskapsformidling fra forskning til innbyggere.

En systematisk forståelse av hvor og hvorfor
forsinkelser oppstår er en forutsetning for å vurdere
forbedringstiltak, herunder bruk av storspråkmodeller
(LLM) og andre teknologiske virkemidler som
analyseres i delrapport 3.

### 1.2 Metodisk tilnærming

Analysen baserer seg på:

- **Offentlig tilgjengelige kilder**: Rapporter fra
  Helsedirektoratet, FHI, Riksrevisjonen,
  regjeringen og internasjonale organisasjoner
  (WHO, Cochrane).
- **Stortingsmeldinger**: Meld. St. 9 (2023–2024)
  Nasjonal helse- og samhandlingsplan, særlig
  kapittel 6 (kunnskapsbasert tjeneste) og
  kapittel 9 (digitalisering) [1][2].
- **Scenarioanalyse**: Der presise tall ikke er
  tilgjengelige, benyttes scenariobaserte estimater
  (konservativt, moderat, optimistisk) med eksplisitt
  markering av usikkerhet.
- **Funn fra delrapport 1**: Tidsestimatene og
  aktørkartleggingen fra den forrige delrapporten
  danner grunnlag for analysen.

**Viktig merknad**: Kvantitative indikatorer i denne
rapporten er estimater basert på tilgjengelig
informasjon og scenarioanalyse. Der tallgrunnlaget er
usikkert, er dette eksplisitt markert.

---

## 2. Utfordringsbildet -- samlet oversikt

Dette kapittelet gir en kort, samlende beskrivelse
av utfordringsbildet før de detaljerte analysene i
kap. 3-9. Hensikten er at leseren skal ha helheten
i hodet før symptomer (flaskehalser), strukturer
(kap. 6) og rotårsaker (kap. 9) gjennomgås.

### 2.1 Hovedproblemet i én setning

**Verdikjeden fra forskning til kvalitetssikret
helseinformasjon for innbyggere holder verken tritt
med forskningsproduksjonen eller innbyggernes
informasjonsbehov, og er ikke rustet til å skalere
i krisesituasjoner.**

Casestudier dokumenterer at den reelle tiden fra
forskning til bred praksisendring er **7-15+ år**,
mens forskningsproduksjonen vokser eksponentielt og
kommersielle KI-tjenester allerede tar over deler
av rollen offentlig helseinformasjon hadde.

### 2.2 Seks dimensjoner ved utfordringen

Utfordringsbildet har seks dimensjoner som virker
samtidig og forsterker hverandre. Hver dimensjon
utdypes i senere kapitler eller i andre
delrapporter.

#### D1: Tid og gjennomløp

- 2-3 år fra forskning til retningslinje;
  6-12 måneder videre til oppdatert
  innbyggerinformasjon.
- 7-15+ år fra forskning til bred
  praksisendring (casestudier).
- 8 år fra publisert evidens til
  forhåndsgodkjent refusjon (diabetes-casen).
- *Detaljer*: kap. 3 (flaskehalser), kap. 4
  (konsekvenser), casestudier-forsinkelser.md.

#### D2: Kapasitet og volum

- Over 3 millioner vitenskapelige artikler
  publiseres årlig globalt.
- FHI har begrenset stab for systematiske
  oversikter; Hdir erkjenner i årsrapport 2024
  «et økende gap mellom muligheter og
  forventninger ... og hva vi har kapasitet
  til».
- *Detaljer*: kap. 3.1, rolledeling-rapporten
  kap. 3.4.

#### D3: Struktur og styring

- Ansvar for verdikjeden er fordelt på rundt 20
  aktører uten helhetlig styringsmandat. Disse
  inkluderer HOD, Helsedirektoratet, FHI, NHN,
  Statens legemiddelverk/DMP, de fire RHF-ene
  med tilhørende helseforetak, KS,
  fastlegevirksomheter, kommunale helse- og
  omsorgstjenester, brukerorganisasjoner og
  fagmiljøer i universitets- og høgskolesektoren.
  Full oversikt med roller, ansvar og leveranser
  finnes i delrapport 8 (aktoeranalyse.md).
- Fragmenterte IT-systemer og ulike kodeverk
  hindrer informasjonsflyt mellom retningslinjer,
  Helsebiblioteket, helsenorge.no og EPJ-er.
- Fritekst-basert innhold uten metadata hindrer
  automatisering, sporbarhet og gjenbruk.
- *Detaljer*: kap. 6 (strukturelle utfordringer),
  rolledeling-rapporten, delrapport 8.

#### D4: Implementering og insentiver

- Ingen aktør eier implementeringsgapet mellom
  publisert retningslinje og endret klinisk
  praksis.
- Refusjonsbeslutninger er en separat
  beslutningskjede uten systematisk samordning
  med retningslinjer.
- Begrenset systematisk overvåking av
  etterlevelse i kommuner og helseforetak.
- *Detaljer*: kap. 3.4, 3.5; casestudier.

#### D5: Tillit og innbyggerbehov

- 99 % av befolkningen kjenner Helsenorge,
  men 54 % bruker generativ KI; mange yngre
  bruker ChatGPT som kilde til
  helseinformasjon.
- Innbyggerinformasjon er generisk og lite
  tilpasset, og det mangler systematiske
  feedback-kanaler.
- Tilgjengelighetsutfordringer for eldre,
  flerspråklige og personer med
  funksjonsnedsettelser.
- *Detaljer*: kap. 4.3, kap. 7.

#### D6: Beredskap

- Verdikjeden skalerer ikke til kriser
  (COVID-19 krevde improvisering).
- *Detaljer*: kap. 4.4 (COVID-19).

**Merknad om regulatoriske rammer**: EU AI Act og
EHDS er ikke direkte regulatoriske krav til
*dagens* verdikjede for kunnskapsforvaltning.
De blir derimot bindende rammer **når** verdikjeden
moderniseres med KI-støtte (alternativ 2 og 3 i
delrapport 4) eller når retningslinjer skal
publiseres maskinlesbart for grenseoverskridende
bruk. Disse rammene behandles derfor i
delrapport 3 (LLM og EU AI Act) og delrapport 5
(arkitektur og EHDS), ikke som en selvstendig
dimensjon ved utfordringsbildet i dag.

### 2.3 Tre kjerneegenskaper verdikjeden mangler

Samlet vurdering (delrapport 7 kap. 4.2)
oppsummerer dimensjonene D1-D6 i tre kjerne-
egenskaper som dagens verdikjede mangler:

- **Skalerbarhet** -- kapasiteten øker ikke i
  takt med forskningsvolumet (jf. D2).
- **Reaktivitet** -- gjennomløpstiden gjør det
  umulig å respondere raskt på ny evidens, og
  spesielt i krisesituasjoner (jf. D1, D6).
- **Sammenheng** -- stegene er ikke koblet på en
  måte som sikrer konsistent og oppdatert
  informasjon gjennom hele kjeden (jf. D3, D4,
  D5).

### 2.4 Hvorfor utfordringene må forstås samlet

Tre forhold gjør at en sektor- eller
kapittelvis tilnærming alene er utilstrekkelig:

1. **Utfordringene forsterker hverandre.** En
   detaljert relasjonstabell (kap. 9.4.2) viser
   at flere flaskehalser forårsaker eller
   forsterker andre. Tiltak som adresserer ett
   symptom uten å adressere driveren gir
   begrenset effekt.
2. **Tiltakene må adressere både teknologi og
   organisasjon.** Rotårsaksanalysen (kap. 9.2)
   identifiserer seks rotårsaker, hvorav noen
   er teknisk-prosessuelle (R2, R3, R4, R6) og
   andre er organisatorisk-politiske (R1, R5).
   Et rent KI-program vil ikke dekke R1 og R5.
3. **Konsekvensen av å ikke handle er
   selvforsterkende.** Jo lengre utdaterte
   helseråd, kommersielle KI-alternativer og
   fragmentert IT-landskap forblir uadressert,
   desto vanskeligere -- og dyrere -- blir det
   å gjenvinne offentlig sektors rolle som
   primær kilde til kvalitetssikret
   helseinformasjon.

### 2.5 Leseveiledning videre

- **Kap. 3** beskriver flaskehalsene per ledd i
  verdikjeden (D1, D2, D4).
- **Kap. 4** dokumenterer konsekvensene
  (D1, D5, D6).
- **Kap. 5** gir kvantitative indikatorer der
  de finnes.
- **Kap. 6** behandler strukturelle utfordringer
  (D3).
- **Kap. 7** dekker innbyggerrettet informasjon
  (D5).
- **Kap. 8** rangerer flaskehalsene etter
  alvorlighet og angir videre analyser.
- **Kap. 9** gir rotårsaksanalysen som binder
  D1-D6 sammen og kobler hver flaskehals til
  rotårsakene R1-R6.

---

## 3. Flaskehalser i verdikjeden

### 3.1 Forskningsproduksjon til systematisk oversikt

**Flaskehals: Volumet overgår kapasiteten for manuell
bearbeiding.**

Den globale forskningsproduksjonen innen helse og
medisin har økt eksponentielt de siste tiårene.
Estimater fra internasjonale kilder indikerer at det
publiseres over 3 millioner vitenskapelige artikler
årlig på tvers av alle fagområder, med en betydelig
andel innen medisin og helsefag. For FHI og andre
kunnskapsprodusenter innebærer dette at mengden
potensielt relevant forskning langt overstiger
kapasiteten for manuell screening og
kvalitetsvurdering.

Sentrale utfordringer i dette steget:

- **Skalering**: Manuell screening av titler,
  sammendrag og fulltekst krever
  spesialistkompetanse og er svært tidkrevende.
  En enkelt systematisk oversikt kan kreve
  gjennomgang av flere tusen artikler.
- **Språkbarriere**: Forskningslitteraturen er i all
  hovedsak på engelsk. Kontekstualisering til norske
  forhold krever faglig vurdering som går utover
  ren oversettelse.
- **Kapasitetsbegrensninger**: FHI har en begrenset
  stab av fagpersoner med kompetanse til å utføre
  systematiske oversikter. Antallet oversikter som
  kan produseres årlig er derfor begrenset.
- **Reproduserbarhet**: Den manuelle prosessen gjør
  det krevende å oppdatere oversikter når ny
  forskning publiseres.

**Typisk tidsbruk**: 12-24 måneder per systematisk
oversikt (jf. delrapport 1).

### 3.2 Systematisk oversikt til retningslinje

**Flaskehals: Kunnskapsgrunnlaget foreldes underveis
i retningslinjeprosessen.**

Overgangen fra ferdig kunnskapsoppsummering til
publisert nasjonal faglig retningslinje er den mest
tidkrevende enkeltovergangen i verdikjeden. Det er
også her den største risikoen for at
kunnskapsgrunnlaget blir utdatert før retningslinjen
ferdigstilles.

Sentrale utfordringer:

- **Foreldelse underveis**: Med en typisk
  utviklingstid på 12-24 måneder kan ny forskning
  ha endret evidensgrunnlaget vesentlig før
  retningslinjen publiseres. I noen tilfeller er
  kunnskapsoppsummeringen flere år gammel når
  retningslinjen ferdigstilles.
- **Kompleks konsensusprosess**:
  Retningslinjeutvikling involverer tverrfaglige
  arbeidsgrupper med representanter fra kliniske
  fagmiljøer, brukerorganisasjoner og forvaltning.
  Konsensusbygging er nødvendig, men tidkrevende.
- **Høringsrunder**: Offentlige høringer gir viktige
  innspill og forankring, men legger typisk
  3-6 måneder til prosessen. I tilfeller med mange
  høringsinnspill kan bearbeidingen ta enda lengre
  tid.
- **Begrenset kapasitet**: Helsedirektoratet har et
  begrenset antall retningslinjeprosjekter som kan
  pågå parallelt. Prioritering mellom fagområder er
  nødvendig, noe som innebærer at enkelte områder
  får lenger ventetid.
- **Avhengighet mellom retningslinjer**: Noen
  retningslinjer avhenger av oppdatering av andre
  retningslinjer eller lovverk, noe som kan skape
  ytterligere forsinkelser.

**Typisk tidsbruk**: 12-24 måneder (jf. delrapport 1).

### 3.3 Retningslinje til formidlet kunnskap

**Flaskehals: Oversettelse fra fagspråk til
innbyggerspråk er ressurskrevende og ikke
systematisert.**

Når en retningslinje er publisert, gjenstår arbeidet
med å gjøre innholdet tilgjengelig for helsepersonell
(via Helsebiblioteket) og innbyggere (via
helsenorge.no og andre kanaler). Denne overgangen er
ofte undervurdert i ressursplanlegging.

Sentrale utfordringer:

- **Klarspråk er en fagdisiplin**: Å oversette
  komplekst medisinsk innhold til klarspråk uten å
  miste presisjon krever både medisinsk og
  kommunikasjonsfaglig kompetanse. Denne
  kombinasjonen er begrenset tilgjengelig.
- **Fragmentert formidling**: Innbyggerrettet
  helseinformasjon formidles gjennom flere kanaler
  (helsenorge.no, Helsedirektoratets nettsider,
  kommunale nettsider, helseforetak). Det er
  begrenset koordinering mellom kanalene, noe som
  kan gi inkonsistent informasjon.
- **Manglende systematisk oppdatering**: Det finnes
  ingen automatisert kobling mellom oppdaterte
  retningslinjer og tilhørende
  innbyggerinformasjon. Oppdatering skjer i praksis
  manuelt og ad hoc, noe som innebærer risiko for
  at innbyggerinformasjon ikke reflekterer gjeldende
  anbefalinger.
- **Prioritering**: Ikke alle retningslinjer
  resulterer i oppdatert innbyggerinformasjon.
  Områder med lavere offentlig oppmerksomhet kan ha
  utdatert informasjon over lengre tid.

**Typisk tidsbruk**: 6-12 måneder (jf. delrapport 1).

### 3.4 Formidlet kunnskap til endret praksis

**Flaskehals: Implementeringsgapet mellom anbefaling
og klinisk praksis.**

Selv når oppdaterte retningslinjer og
innbyggerinformasjon foreligger, er det et velkjent
gap mellom anbefalt praksis og faktisk praksis i
helsetjenesten. Meld. St. 9 (2023–2024) fastslår at
«avstanden mellom forskning og praksis skyldes ulike
forhold», herunder «manglende
implementeringskompetanse og tilstrekkelig
kapasitet» [1]. Kommunesektoren er særlig utsatt:
stortingsmeldingen konstaterer at «kommunene mangler
strukturer som kan understøtte strategisk innføring
av kunnskapsbaserte tiltak» [1].

Rammeverket for kunnskapsbasert praksis [7]
identifiserer seks trinn fra refleksjon til
evaluering. Verdikjedens sentrale infrastruktur
understøtter primært trinn 1-4 (refleksjon,
spørsmålsformulering, søk, kritisk vurdering),
mens trinn 5 (anvende) og 6 (evaluere) overlates
til den enkelte virksomhet. RNAO
kunnskap-til-handling-modellen [8], som er oversatt
og tilpasset til norske forhold, gir et strukturert
rammeverk for disse siste trinnene, men er ikke
systematisk integrert i den nasjonale verdikjeden.
Modellen identifiserer barrierer som negative
holdninger til endring, manglende
ledelsesforankring og uenighet om faglig innhold –
og anbefaler kombinasjon av flere virkemidler
(audit/feedback, opplæringsmøter, praksisbesøk)
for å oppnå praksisendring.

Sentrale utfordringer:

- **Variasjon mellom virksomheter**: Etterlevelse av
  nasjonale retningslinjer varierer betydelig mellom
  helseforetak, kommuner og fastleger.
  Riksrevisjonen har ved flere anledninger pekt på
  slik variasjon. En revisjonsrapport fra Sørlandet
  sykehus (2025) dokumenterer konkrete gap mellom
  nasjonale retningslinjer og lokal praksis [3].
- **Manglende målingsmekanismer**: Det er begrenset
  systematisk overvåking av i hvilken grad
  retningslinjer følges i klinisk praksis.
- **Informasjonsoverbelastning**: Helsepersonell
  forholder seg til et stort antall retningslinjer
  og oppdateringer, noe som kan føre til at
  enkeltvise endringer oversees. En studie
  publisert i Sykepleien viser at helsesøstres
  faktiske bruk av kunnskapskilder i praksis
  avviker fra den intenderte bruken i
  verdikjeden [4].
- **Lokal tilpasning**: Retningslinjer må ofte
  tilpasses lokale forhold, noe som krever lokal
  kapasitet og kompetanse.
- **Digitalisering løser ikke gapet alene**: En
  DNV-rapport fra 2025 finner at 80 % av
  helsepersonell mener digitale verktøy har
  forbedret pasientbehandlingen, men bare 38 %
  rapporterer redusert klinisk arbeidsbelastning.
  Kun 47 % opplever at teknologien har lettet
  administrative oppgaver [5]. Dette tyder på at
  digitalisering i seg selv ikke er tilstrekkelig
  for å lukke implementeringsgapet.

### 3.5 Refusjonsordninger som flaskehals

**Flaskehals: Refusjonsordninger forsinker faktisk
bruk av anbefalte legemidler.**

Casestudier (se casestudier-forsinkelser.md)
avdekker at refusjonsordninger utgjør en vesentlig,
men tidligere ikke identifisert, flaskehals i
verdikjeden. Selv etter at en retningslinje
anbefaler et legemiddel, kan praktiske barrierer
i refusjonssystemet forsinke bred klinisk bruk
med flere år.

Sentrale utfordringer:

- **Individuell søknadsplikt**: Når et legemiddel
  ikke har forhåndsgodkjent refusjon, må leger
  søke individuelt om refusjon for hver pasient.
  Dette er en administrativ barriere som
  dokumentert reduserer faktisk bruk.
- **Lang behandlingstid**: Prosessen fra
  retningslinjeinkludering til forhåndsgodkjent
  refusjon kan ta flere år. Diabetes-casen viser
  at det tok nesten 8 år fra EMPA-REG-studien
  (2015) til forhåndsgodkjent refusjon for
  SGLT2-hemmere (2023).
- **Fragmentert beslutningskjede**: Beslutninger
  om refusjon tas av et annet organ enn det som
  utvikler retningslinjer, uten systematisk
  koordinering av tidslinjene.

**Typisk tilleggsforsinkelse**: 3-8 år fra
retningslinjeinkludering til forhåndsgodkjent
refusjon (basert på diabetes-casen).

---

## 4. Konsekvenser av forsinkelser

Forsinkelsene i verdikjeden har direkte konsekvenser
for kvaliteten på helsetjenester og
helseinformasjon som når innbyggere.

### 4.1 Utdaterte helseråd

Gjennomløpstiden fra ny evidens til oppdatert
innbyggerinformasjon var opprinnelig estimert til
2-6,5 år (delrapport 1). Casestudier
(casestudier-forsinkelser.md) dokumenterer at den
reelle tiden fra forskning til bred praksisendring
er **7-15+ år**, noe som innebærer at innbyggere i
mange tilfeller mottar helseråd basert på forskning
som er betydelig eldre enn hva den tilgjengelige
kunnskapen tilsier. Dette
kan gjelde alt fra ernæringsråd til anbefalinger om
medisinbruk og livsstilsendringer.

### 4.2 Helsepersonell uten oppdatert kunnskapsgrunnlag

Forsinkelser i retningslinjeoppdateringer innebærer
at helsepersonell risikerer å basere sine kliniske
vurderinger på utdaterte anbefalinger. Dette er
særlig problematisk i fagfelt med rask
kunnskapsutvikling.

### 4.3 Innbyggere søker alternative kilder

Når offentlige kilder oppleves som utdaterte eller
utilstrekkelige, søker innbyggere informasjon fra
andre kilder. Søkedata og brukerundersøkelser
indikerer at en betydelig andel av befolkningen
bruker Google, sosiale medier og i økende grad
generative AI-verktøy som ChatGPT for å finne
helseinformasjon. Disse kildene har variabel kvalitet
og mangler den systematiske kvalitetssikringen som
kjennetegner den offisielle verdikjeden.

### 4.4 Lærdommer fra COVID-19

COVID-19-pandemien demonstrerte tydelig at den
tradisjonelle verdikjeden ikke skalerer til
krisesituasjoner. Kunnskapsgrunnlaget endret seg
daglig, og de etablerte prosessene for
kunnskapsoppsummering og retningslinjeutvikling var
for langsomme til å holde tritt.
Helsemyndighetene måtte improvisere hurtigprosesser,
noe som viste at det er mulig å akselerere
verdikjeden, men også at det krever ekstraordinære
ressurser og medfører økt risiko for feil.

### 4.5 Eksempel: Ernæringsråd

Ernæringsområdet illustrerer utfordringen: Ny
forskning om for eksempel tilsatt sukker, mettet fett
eller kosttilskudd kan endre evidensgrunnlaget
vesentlig, men de offisielle ernæringsrådene
oppdateres sjelden. Kostradsrapporten fra
Helsedirektoratet har historisk hatt lang tid mellom
revisjonene, noe som kan bidra til at innbyggere
opplever et gap mellom medieomtale av ny forskning
og offisielle anbefalinger.

---

## 5. Kvantitative indikatorer og statistikk

### 5.1 Produksjonskapasitet for systematiske oversikter og retningslinjer

**Status:** Disse tallene mangler etterprøvbar
dokumentasjon og må innhentes direkte fra FHI og
Helsedirektoratet gjennom:

- Offisielle årsrapporter fra FHI om
  kunnskapsoppsummeringsproduksjon
- Offisielle oversikter fra Helsedirektoratet over
  retningslinjeproduuksjon per år
- Statistikk fra helsenorge.no om
  oppdateringsfrekvens for innbyggerartikler

Uten slike kilder bør ikke estimater presenteres
i denne rapporten.

### 5.2 Oppdateringsgrad for retningslinjer

**Status:** Systematisk oversikt over alderen på
gjeldende retningslinjer og oppdateringsgraden finnes
ikke dokumentert i tilgjengelige kilder. Dette bør
kartlegges gjennom direkte undersøkelse av
Helsedirektoratets retningslinjearchiv.

### 5.3 Gjennomløpstider i verdikjeden

**Status:** Som dokumentert i delrapport 1, mangler
eksakte tidsestimater kilder. Gjennomløpstiden er
kjent som lang, men nøyaktige målinger av hvert ledd
mangler.

### 5.4 Innbyggernes informasjonskilder – dokumenterte tall

Følgende indikatorer er basert på verifiserte kilder
fra Helsedirektoratet (2024) og forskning:

#### Helsenorge.no brukerstatistikk

| Indikator | Verdi | År |
| --- | --- | --- |
| Totalt antall besøk på Helsenorge | 131 millioner | 2024 |
| Gjennomsnittlig månedlige besøk | 10,9 millioner | 2024 |
| **Innbyggeres kjennskap til Helsenorge** | **99 %** | 2024 |
| Andel som har logget seg inn på Helsenorge | 80 % | 2024 |
| Andel som bruker Helsenorge for å finne **generell helseinformasjon** | 51 % | 2024 |

*Kilde:
[Innbyggerundersøkelsen om digitalisering i helse- og omsorgstjenesten 2024 – Helsedirektoratet](https://www.helsedirektoratet.no/rapporter/innbyggerundersokelsen-om-digitalisering-i-helse-og-omsorgstjenesten-2024-bruk-av-holdninger-til-og-tilfredshet-med-digitale-helsetjenester)*

#### Innbyggeres digitale helsetjenestekontakt

| Indikator | Verdi | År |
| --- | --- | --- |
| Andel som har vært i digital kontakt med helsetjenesten (siste 12 mnd) | 59 % | 2024 |
| Andel som bruker e-konsultasjon hos fastlege | 18,6 % | 2024 |

*Kilde:
[Bruk av digitale helsetjenester – Helsedirektoratet](https://www.helsedirektoratet.no/rapporter/innbyggerundersokelsen-om-digitalisering-i-helse-og-omsorgstjenesten-2024-bruk-av-holdninger-til-og-tilfredshet-med-digitale-helsetjenester/funn-og-analyser/bruk-av-digitale-helsetjenester)*

#### Generativ AI og helseinformasjon

| Indikator | Verdi | År/kilde |
| --- | --- | --- |
| Norske befolkningens bruk av generativ AI (ChatGPT, etc.) | 54 % | 2025 |
| Unge som evaluerte ChatGPT positivt for helsespørsmål | Høy tilfredshet | 2023 studie |

**Kontekst:** En norsk studie av 123 unge (16-20 år)
sammenlignet ChatGPT (GPT-4) med fagpersoner på
ung.no for mentalhelsespørsmål. Deltakerne vurderte
informasjonen fra ChatGPT som god, og ville oftere
anbefale den til andre, selv med fagfolk som
alternativ.

*Kilder:
[Unge og helseinformasjon. ChatGPT vs. Fagpersoner – Utdanningsforskning.no](https://utdanningsforskning.no/artikler/2025/unge-og-helseinformasjon.-chatgpt-vs.-fagpersoner/)
og
[Slik bruker nordmenn generativ kunstig intelligens – SSB](https://www.ssb.no/teknologi-og-innovasjon/informasjons-og-kommunikasjonsteknologi-ikt/artikler/slik-bruker-nordmenn-kunstig-intelligens)*

#### Helseinformasjon fra Google og andre kilder

Forskning fra Tromsøundersøkelsen (norsk
befolkningsstudie) viser at innbyggere bruker
nettsøk (Google), sosiale media (Facebook), videosøk
(YouTube) og helseapper for å lete etter
helseinformasjon. Søk på nettet har størst
påvirkning på beslutninger om å oppsøke lege eller
ikke, spesielt blant yngre og mer utdannede personer.

*Kilde:
[Vi søker etter helseinformasjon på nettet, men går vi til legen etterpå? – Forskning.no](https://www.forskning.no/data-helsetjenester-internett/vi-soker-etter-helseinformasjon-pa-nettet-men-gar-vi-til-legen-etterpa/1709876)*

**Merknad:** Det mangler fortsatt presise tall for
hvor stor andel som bruker Google vs. Helsenorge vs.
medier som *første kilde* for helseinformasjon, og
hvor mye som spesifikt brukes generativ AI for
helseinformasjon (i motsetning til generell AI-bruk).

---

## 6. Strukturelle utfordringer

Utover flaskehalsene i hvert enkelt steg i
verdikjeden, finnes det overordnede strukturelle
utfordringer som påvirker verdikjeden som helhet.

### 6.1 Siloorganisering

Ansvaret for de ulike stegene i verdikjeden er
fordelt på flere organisasjoner (FHI,
Helsedirektoratet, NHN, helseforetak, kommuner) med
ulike styringslinjer, budsjettprosesser og
prioriteringer. Meld. St. 9 (2023–2024)
understreker at «praksisnær forskning,
implementeringsforskning, kunnskapsutvikling og
innovasjon er helt nødvendig» og at det kreves
«endringer av atferd på individ-, organisatorisk-
og systemnivå» [1]. Det finnes ikke et helhetlig
styringsmandat for verdikjeden fra forskning til
innbygger, noe som kan føre til suboptimalisering
innenfor det enkelte steg uten at helheten
ivaretas.

### 6.2 Manglende standardisert informasjonsflyt

Som beskrevet i delrapport 1 mangler det
gjennomgående maskinlesbare formater og
standardiserte grensesnitt mellom stegene. Kunnskapen
transporteres i stor grad som ustrukturert fritekst,
noe som gjør automatisert videreforedling og
sporbarhet vanskelig.

### 6.3 Dobbeltarbeid

Flere aktører utfører overlappende oppgaver uten
tilstrekkelig koordinering. Eksempler inkluderer:

- Flere organisasjoner oversetter og
  kontekstualiserer den samme internasjonale
  forskningen uavhengig av hverandre.
- Innbyggerinformasjon om samme tema kan finnes på
  både helsenorge.no, Helsedirektoratets nettsider
  og regionale helseforetaks nettsider, uten
  systematisk koordinering.
- Fagprosedyrer utvikles lokalt i helseforetak uten
  systematisk gjenbruk på tvers.

### 6.4 Fragmenterte IT-systemer

Verdikjeden støtter seg på ulike IT-systemer som i
begrenset grad er integrert. Retningslinjeverktøy,
publiseringsløsninger, Helsebibliotekets systemer og
helsenorge.no har separate
innholdsforvaltningssystemer uten automatisert
informasjonsflyt mellom seg.

Meld. St. 9 (2023–2024) konstaterer at det «også
framover vil være flere systemer i bruk» og at
«kommunesektoren har de største utfordringene» [2].
Fragmenteringen er særlig godt dokumentert på
legemiddelområdet, der Helsedirektoratets
kunnskapsgrunnlag identifiserer at «aktører
benytter ulike kodeverk for samme
informasjonselement» og at spesialisthelsetjenesten
må «komplettere, kompensere og kvalitetssikre
legemiddeldata lokalt og regionalt, noe som er
ressurskrevende» [6]. Helsepersonell «må bruke
unødvendig mye tid på å få oversikt over hvilke
legemidler pasienten bruker» ved overganger mellom
virksomheter [6].

### 6.5 Begrenset bruk av strukturerte data og metadata

Innhold gjennom verdikjeden er i hovedsak
fritekstbasert med begrenset bruk av strukturerte
metadata. Dette vanskeliggjør:

- Automatisert identifisering av utdatert innhold
- Kobling mellom retningslinjer og tilhørende
  innbyggerinformasjon
- Sporbarhet fra anbefaling tilbake til underliggende
  evidens
- Gjenbruk av innhold på tvers av kanaler og formater

### 6.6 Praktiske konsekvenser av strukturelle svakheter

Dette kapittelet samler de praktiske konsekvensene av
de strukturelle svakhetene beskrevet i 5.1–5.5 og av
konsekvensene for innbyggere som utdypes i kapittel 3
og 6. Hvert punkt er merket **[DOK]** der påstanden er
dokumentert i kildematerialet, eller **[ANT]** der den
er en analytisk slutning som ikke er direkte
dokumentert.

#### 6.6.1 Konsekvenser av siloorganisering og manglende helhetlig styringsmandat

- **[DOK]** Ingen enkelt aktør er ansvarlig for samlet
  gjennomløpstid fra forskning til praksisendring.
  Verdikjeden krysser minst tre etater
  (FHI → Hdir → NHN) uten overordnet mandat
  (rolledeling-sentral-helseforvaltning.md, kap. 5.3).
- **[DOK]** Retningslinjer (Hdir), innbyggerinformasjon
  (NHN/helsenorge.no) og faglig oppdatering
  (FHI/Helsebiblioteket) oppdateres uavhengig av
  hverandre, uten automatisert kobling
  (kap. 3.3 i denne rapporten).
- **[DOK]** Budsjettkutt i én etat rammer hele kjeden:
  Helsebibliotekets kutt i 2023 fjernet tilgang til
  Cochrane Library og Embase -- sentrale kilder for
  helsepersonell (delrapport 8).
- **[ANT]** Når ingen eier helheten, blir
  forbedringstiltak i ett ledd ikke nødvendigvis
  omsatt i raskere innbyggerinformasjon eller
  praksisendring. Gevinsten «går tapt» i neste
  overgang.

#### 6.6.2 Konsekvenser av fragmenterte IT-systemer

- **[DOK]** På legemiddelområdet bruker aktører ulike
  kodeverk for samme informasjonselement.
  Spesialisthelsetjenesten må «komplettere,
  kompensere og kvalitetssikre legemiddeldata lokalt
  og regionalt» [6].
- **[DOK]** Ved overganger mellom virksomheter må
  helsepersonell «bruke unødvendig mye tid på å få
  oversikt over hvilke legemidler pasienten
  bruker» [6].
- **[ANT]** Fragmenteringen forsterker
  implementeringsgapet: selv oppdaterte
  retningslinjer når ikke klinikere der de jobber
  (i EPJ-en), men ligger i separate portaler som
  må oppsøkes aktivt.

#### 6.6.3 Konsekvenser av dobbeltarbeid

- **[DOK]** FHI og Hdir har overlappende leveranser
  innen innbyggerrettet informasjon uten tydelig
  arbeidsdeling (delrapport 8, kap. 4;
  rolledeling-rapporten, kap. 3.2).
- **[DOK]** Fagprosedyrer utvikles lokalt i
  helseforetak uten systematisk gjenbruk på tvers
  (kap. 6.3 i denne rapporten).
- **[ANT]** Dobbeltarbeidet binder opp knappe
  FHI-ressurser som kunne vært brukt på nye
  systematiske oversikter, og gir inkonsistens når
  innbyggere finner ulike anbefalinger hos Hdir,
  FHI og helseforetak.

#### 6.6.4 Konsekvenser av fritekst og manglende metadata

- **[DOK]** Fritekst-basert innhold gjør det vanskelig
  å identifisere utdatert innhold automatisk, koble
  retningslinjer til innbyggerinformasjon, spore
  anbefaling tilbake til evidens og gjenbruke
  innhold på tvers av kanaler (kap. 6.5).
- **[ANT]** Dette er en strukturell blokker for en
  KI-støttet verdikjede (jf. delrapport 4 og 5):
  uten strukturerte metadata kan ikke living
  guidelines eller automatisert overvåking av
  evidensgrunnlag implementeres effektivt.

#### 6.6.5 Konsekvenser av manglende målemekanismer

- **[DOK]** Det er begrenset systematisk overvåking
  av i hvilken grad retningslinjer følges i klinisk
  praksis (kap. 3.4). Produksjonskapasitet hos FHI
  og Hdir samt oppdateringsgrad for retningslinjer
  mangler etterprøvbar dokumentasjon (kap. 5 og
  merknad om kilder).
- **[ANT]** Uten måling vet man ikke om tiltak
  virker. Dette svekker evidensgrunnlaget for
  prioriteringer mellom fagområder og for
  forbedring av selve verdikjeden.

#### 6.6.6 Kunnskapshull som bør lukkes

For å vurdere omfanget av konsekvensene ovenfor mer
presist, bør følgende spørsmål besvares gjennom
primærkilder eller intervjuer:

- Hvor lang er faktisk forsinkelse mellom oppdatert
  retningslinje (Hdir) og oppdatert
  helsenorge.no-artikkel, per tema?
- I hvilken grad velger klinikere pragmatiske kilder
  (kolleger, lokale prosedyrer) framfor nasjonale
  retningslinjer, og hvordan varierer dette mellom
  fagområder?
- Hvor stor andel av innbyggere bruker kommersiell
  KI (ChatGPT m.fl.) *som første kilde* for
  helseinformasjon, i motsetning til generell
  AI-bruk?
- Har rolledeling etter omorganiseringen i januar
  2024 *objektivt* forverret situasjonen for
  verdikjeden, eller bare endret karakter på
  problemene?

---

## 7. Utfordringer spesifikke for innbyggerrettet informasjon

### 7.1 Klarspråk møter kompleksitet

Mange helsefaglige temaer er iboende komplekse. Å
formidle usikkerhet, betinget risiko og individuelle
forskjeller i et klarspråk som er tilgjengelig for
hele befolkningen, er en varig utfordring. Forenkling
kan gå på bekostning av presisjon, og omvendt.

### 7.2 Manglende personalisering

Dagens innbyggerinformasjon er i all hovedsak
generisk. Den tar ikke hensyn til individuelle
faktorer som alder, kjønn, kroniske sykdommer,
medisinbruk eller risikoprofil. Innbyggere med
sammensatte helsebehov må selv syntetisere
informasjon fra flere artikler og kilder for å få et
relevant bilde av sin situasjon.

### 7.3 Tilgjengelighet

Ikke alle innbyggere har samme forutsetninger for å
finne og forstå digital helseinformasjon:

- **Digital kompetanse**: Eldre og personer med lav
  digital kompetanse kan ha vanskeligheter med å
  navigere nettbasert helseinformasjon.
- **Språklig mangfold**: Innbyggere med andre morsmål
  enn norsk har begrenset tilgang til kvalitetssikret
  helseinformasjon på sitt språk.
- **Funksjonsnedsettelser**: Universell utforming av
  helseinformasjon er ikke gjennomgående ivaretatt.

### 7.4 Manglende feedback-loop

Det finnes begrensede mekanismer for å fange opp
innbyggernes erfaringer med og behov for
helseinformasjon. Det mangler systematiske
tilbakemeldingskanaler som gjør det mulig å:

- Identifisere hvilke temaer innbyggere etterlyser
  informasjon om
- Avdekke misforståelser eller feilinformasjon som
  er utbredt
- Måle om innbyggerinformasjonen faktisk fører til
  bedre helsevalg
- Prioritere innholdsproduksjon basert på faktisk
  behov

---

## 8. Oppsummering

### 8.1 De viktigste flaskehalsene rangert etter alvorlighet

Basert på analysen over, og underbygget av tre
casestudier (casestudier-forsinkelser.md), rangeres
de viktigste flaskehalsene etter samlet
alvorlighet. Implementeringsgapet og
refusjonsordninger er oppjustert til «høy» basert
på casedokumentasjonen:

| Rang | Flaskehals | Alvorlighet | Begrunnelse |
| --- | --- | --- | --- |
| 1 | Foreldelse av kunnskapsgrunnlag underveis i retningslinjeprosessen | Høy | Lengste enkeltforsinkelse, direkte påvirkning på kvalitet |
| 2 | Kapasitetsbegrensning for systematiske oversikter | Høy | Begrenser volumet av oppdatert kunnskap som kan produseres |
| 3 | Manglende kobling mellom retningslinje og innbyggerinformasjon | Høy | Gjør at forsinkelsen forsterkes i siste ledd |
| 4 | Implementeringsgapet i klinisk praksis | Høy | Casestudier dokumenterer 7-15+ år fra forskning til bred praksisendring. Passiv publisering er utilstrekkelig; aktive tiltak er nødvendige |
| 5 | Refusjonsordninger som barriere for legemiddelbruk | Høy | Diabetes-casen: 8 år fra forskning til forhåndsgodkjent refusjon. Fragmentert beslutningskjede mellom retningslinjer og refusjon |
| 6 | Siloorganisering og fragmentert ansvar | Middels | Strukturell årsak til flere av de øvrige flaskehalsene |
| 7 | Manglende strukturerte data og metadata | Middels | Hindrer automatisering og sporbarhet |
| 8 | Manglende personalisering av innbyggerinformasjon | Middels | Reduserer relevans og nytteverdi for den enkelte |
| 9 | Tilgjengelighetsutfordringer | Middels | Ekskluderer sårbare grupper |

### 8.2 Videre analyser

Flaskehalsene identifisert i denne rapporten danner
grunnlag for de neste delrapportene i utredningen:

- **Delrapport 3** vil analysere hvordan
  storspråkmodeller (LLM) og annen KI-teknologi kan
  adressere de identifiserte flaskehalsene, med
  særlig vekt på akselerering av
  kunnskapsoppsummering, oversettelse og
  klarspråkformidling.
- **Delrapport 4** vil skissere en ny verdikjede som
  utnytter teknologiske muligheter for å redusere
  gjennomløpstid og øke kvalitet, samtidig som
  nødvendig menneskelig kvalitetssikring ivaretas.

---

## 9. Rotårsaksanalyse og relasjoner mellom utfordringer

### 9.1 Formål og metode

De ni flaskehalsene i kap. 8 er rangert etter
alvorlighet, men de opptrer ikke uavhengig av
hverandre. Flere av dem deler underliggende
drivere, og noen flaskehalser **forårsaker** eller
**forsterker** andre. Dette kapittelet bygger på
den distribuerte kausallogikken i kap. 6 og 6.6 i
denne rapporten, kap. 5.5 i rolledeling-rapporten,
kap. 4 i samlet vurdering (delrapport 7) og
IGOE-analysen i delrapport 8, og syntetiserer
disse til **seks rotårsaker** og et knippe
**kausalkjeder**.

Metoden er en strukturert «hvorfor»-analyse: for
hver flaskehals stilles spørsmålet «hvorfor
eksisterer denne?» i opptil 3–4 nivåer, til
analysen lander på et forhold som ikke kan
forklares videre innenfor verdikjedens egne
rammer.

Hvert utsagn er merket **[DOK]** der det er
dokumentert i kildematerialet, eller **[ANT]** der
det er en analytisk slutning. Skillet følger
konvensjonen fra kap. 6.6.

### 9.2 Seks rotårsaker

#### R1: Manglende helhetlig styringsmandat

**Beskrivelse**: Ingen aktør har overordnet
ansvar for verdikjeden fra forskning til
innbygger.

- **[DOK]** Dokumentert i rolledeling-rapporten
  kap. 5 (H3, vurdert som «sterk støtte»), med
  referanser til Røttingen-rapporten,
  Riksrevisjonen og delrapport 8.
- **[DOK]** Røttingens forslag om forum for
  faglig normering er ikke gjennomført
  (rolledeling kap. 5.2).
- **[DOK]** Departementet har «i stor grad
  delegert ansvaret for gjennomføring» til
  etatene (rolledeling kap. 5.2).

**Forklarer flaskehalsene**: 3 (manglende
kobling retningslinje–innbyggerinformasjon), 5
(refusjonsordninger som separat
beslutningskjede), 6 (siloorganisering).

#### R2: Verdikjeden er designet for pre-digital tid

**Beskrivelse**: Prosessene, innholdet og
overgangene er bygd rundt manuell behandling av
fritekst.

- **[DOK]** Kap. 4.2 i samlet vurdering slår
  fast: «Verdikjeden er designet for en
  pre-digital tid.»
- **[DOK]** Innhold gjennom verdikjeden er i
  hovedsak fritekstbasert med begrenset bruk av
  strukturerte metadata (kap. 6.5 i denne
  rapporten).
- **[DOK]** Manuelle overganger og ustrukturert
  fritekst gjør automatisert videreforedling og
  sporbarhet vanskelig (kap. 6.2).

**Forklarer flaskehalsene**: 1 (foreldelse i
retningslinjeprosessen), 7 (manglende
strukturerte data).

#### R3: Kapasitet skalerer ikke med forskningsvolum

**Beskrivelse**: Manuell screening,
kvalitetsvurdering og retningslinjeutvikling
kan ikke vokse i takt med en eksponentielt
økende forskningsproduksjon.

- **[DOK]** Over 3 millioner vitenskapelige
  artikler publiseres årlig (kap. 3.1).
- **[DOK]** FHI har begrenset stab av
  fagpersoner med kompetanse til å utføre
  systematiske oversikter (kap. 3.1).
- **[DOK]** Hdirs årsrapport 2024 erkjenner «et
  økende gap mellom muligheter og
  forventninger … og hva vi har kapasitet til»
  (rolledeling kap. 3.4, [5]).

**Forklarer flaskehalsene**: 1, 2
(kapasitetsbegrensning for systematiske
oversikter).

#### R4: Fragmentert IT-landskap og ulike kodeverk

**Beskrivelse**: Retningslinjeverktøy,
Helsebibliotek, helsenorge.no og EPJ-er er
separate innholdsforvaltningssystemer uten
automatisert informasjonsflyt.

- **[DOK]** Fragmenterte IT-systemer er
  dokumentert i kap. 6.4 i denne rapporten og
  i Helsedirektoratets kunnskapsgrunnlag for
  legemiddelområdet [6].
- **[DOK]** Aktører bruker ulike kodeverk for
  samme informasjonselement
  (legemiddelområdet) [6].
- **[DOK]** Ingen automatisert kobling mellom
  oppdaterte retningslinjer og helsenorge.no
  (kap. 3.3 og 6.6.1).

**Forklarer flaskehalsene**: 3, 7.

#### R5: Manglende insentiver og eierskap for implementering

**Beskrivelse**: Ingen aktør er formelt
ansvarlig for at en publisert retningslinje
faktisk blir fulgt i klinisk praksis, og
refusjonsordninger er en separat beslutnings-
kjede.

- **[DOK]** Meld. St. 9 (2023–2024): «avstanden
  mellom forskning og praksis skyldes ulike
  forhold», herunder «manglende
  implementeringskompetanse og tilstrekkelig
  kapasitet» [1].
- **[DOK]** Beslutninger om refusjon tas av et
  annet organ enn det som utvikler
  retningslinjer, uten systematisk koordinering
  av tidslinjene (kap. 3.5).
- **[DOK]** Begrenset systematisk overvåking av
  i hvilken grad retningslinjer følges i
  klinisk praksis (kap. 3.4, 6.6.5).
- **[ANT]** Uten eier av implementeringsgapet
  blir aktive tiltak (audit/feedback,
  opplæring, praksisbesøk) ad hoc og avhengig
  av enkeltvirksomheters kapasitet.

**Forklarer flaskehalsene**: 4
(implementeringsgapet), 5 (refusjonsordninger).

#### R6: Manglende feedback- og målemekanismer

**Beskrivelse**: Systemet mangler instrumenter
for å måle sin egen ytelse, eller for å fange
opp innbyggernes og klinikernes behov.

- **[DOK]** Produksjonskapasitet, oppdaterings-
  grad for retningslinjer og gjennomløpstider
  mangler etterprøvbar dokumentasjon (kap. 4,
  merknad om kilder).
- **[DOK]** Begrensede mekanismer for å fange
  opp innbyggernes erfaringer med og behov for
  helseinformasjon (kap. 7.4).
- **[ANT]** Uten måling vet verken beslutnings-
  takere eller fagmiljøer om tiltak virker.
  Dette svekker grunnlaget for prioriteringer
  mellom fagområder og for forbedring av selve
  verdikjeden (kap. 6.6.5).

**Forklarer flaskehalsene**: 8 (manglende
personalisering), 9 (tilgjengelighetsutfordringer),
og indirekte 1–5 ved at manglende måling hindrer
korrigerende tiltak.

### 9.3 Dekning: Hver flaskehals kobles til minst én rotårsak

<!-- markdownlint-disable MD013 -->

| # | Flaskehals (fra kap. 8.1) | Primær rotårsak | Sekundære rotårsaker |
| --- | --- | --- | --- |
| 1 | Foreldelse av kunnskapsgrunnlag underveis | R3 (kapasitet vs. volum) | R2, R6 |
| 2 | Kapasitetsbegrensning for systematiske oversikter | R3 | R2 |
| 3 | Manglende kobling retningslinje–innbyggerinformasjon | R4 (IT-fragmentering) | R1, R2 |
| 4 | Implementeringsgapet i klinisk praksis | R5 (manglende insentiver) | R4, R6 |
| 5 | Refusjonsordninger som barriere | R5 | R1 |
| 6 | Siloorganisering og fragmentert ansvar | R1 (styringsmandat) | R5 |
| 7 | Manglende strukturerte data og metadata | R2 (pre-digital design) | R4 |
| 8 | Manglende personalisering av innbyggerinformasjon | R6 (feedback/måling) | R2, R4 |
| 9 | Tilgjengelighetsutfordringer | R6 | R1 |

<!-- markdownlint-enable MD013 -->

Alle ni flaskehalser har minst én rotårsak. Fem
av ni har sekundære rotårsaker, noe som
bekrefter at utfordringene henger sammen.

### 9.4 Relasjoner mellom utfordringer

Flaskehalsene forsterker hverandre. Kapittelet
her beskriver først seks sentrale kausalkjeder
narrativt, og samler deretter relasjonene i en
tabell.

#### 9.4.1 Seks sentrale kausalkjeder

1. **Kjede A – Styring til implementering**:
   R1 (manglende styringsmandat) → flaskehals 6
   (siloorganisering) → flaskehals 3 (manglende
   kobling mellom retningslinje og
   innbyggerinformasjon) → tillitstap og økende
   bruk av kommersielle KI-kilder (kap. 4.3).
   **[DOK]** kausalkjede i rolledeling kap. 5.5
   og dp2 kap. 6.6.1.
2. **Kjede B – Volum slår kapasitet**: Økende
   forskningsvolum (kap. 3.1) → R3 (kapasitet
   vs. volum) → flaskehals 2 → flaskehals 1
   (foreldelse underveis) → utdaterte
   retningslinjer (kap. 4.2). **[DOK]**.
3. **Kjede C – Refusjonskjede**: Retningslinje
   publisert → individuell søknadsplikt (R5) →
   flaskehals 5 → 3–8 års forsinkelse i faktisk
   bruk (diabetes-casen). **[DOK]** i
   casestudier-forsinkelser.md og kap. 3.5.
4. **Kjede D – Fritekst blokkerer
   automatisering**: R2 (pre-digital design) →
   flaskehals 7 (manglende strukturerte data)
   → KI-støttet verdikjede kan ikke
   implementeres uten kompenserende
   tiltak (kap. 6.6.4). **[ANT]** siste ledd.
5. **Kjede E – Implementeringsgap uten eier**:
   Publisert retningslinje → ingen aktiv
   oppfølging (R5) → flaskehals 4 →
   dokumentert 7–15+ år til praksisendring
   (casestudier). **[DOK]**.
6. **Kjede F – Budsjettkutt forplanter seg**:
   Budsjettkutt hos Helsebiblioteket (2023) →
   tap av Cochrane/Embase → færre systematiske
   oversikter → R3 forsterkes → flaskehals 1
   forsterkes. **[DOK]** i delrapport 8 og
   kap. 6.6.1.

#### 9.4.2 Relasjonstabell

Tabellen under viser parvise relasjoner mellom
flaskehalsene (kolonner) og angir om raden
**forårsaker** (F), **forsterker** (+) eller er
**uavhengig av** (·) kolonnen. Tabellen leses
radvis.

<!-- markdownlint-disable MD013 -->

| Fra \ Til | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1** Foreldelse | – | · | + | + | · | · | · | · | · |
| **2** Kap. syst. oversikter | F | – | · | · | · | · | · | · | · |
| **3** Manglende kobling | · | · | – | + | · | · | · | + | + |
| **4** Implementeringsgap | · | · | · | – | + | · | · | · | · |
| **5** Refusjon | · | · | · | + | – | · | · | · | · |
| **6** Siloorganisering | + | + | F | + | F | – | + | + | + |
| **7** Fritekst/metadata | + | + | F | + | · | · | – | F | + |
| **8** Personalisering | · | · | · | · | · | · | · | – | + |
| **9** Tilgjengelighet | · | · | · | · | · | · | · | + | – |

<!-- markdownlint-enable MD013 -->

Tegnforklaring: **F** = forårsaker, **+** =
forsterker, **·** = uavhengig, **–** = samme
flaskehals.

Observasjon: Flaskehals 6 (siloorganisering) og
flaskehals 7 (fritekst/metadata) har flest
utgående relasjoner, noe som bekrefter at de
fungerer som **strukturelle drivere** for flere
av de øvrige flaskehalsene. Dette er konsistent
med R1 og R2 som de to bredest forklarende
rotårsakene.

### 9.5 Implikasjoner for valg av tiltak

Rotårsaksanalysen har to direkte implikasjoner
for vurderingen av alternativene i delrapport 4:

1. **Alternativene måles i dag primært på tid og
   kostnad** (dp4 kap. 6). En rotårsaksbasert
   sammenligning (se dp4 kap. 6 i revidert
   utgave og dp7 kap. 5.4) viser at enkelte
   rotårsaker – særlig R1 (styringsmandat) og
   deler av R5 (refusjonskjede) – **ikke
   adresseres fullt ut av noen av alternativene**
   i dp4. De krever politiske eller
   tverrsektorielle tiltak som må løpe parallelt.
2. **Tekniske alternativer uten organisatorisk
   tiltak vil gi begrenset effekt**. R1, R5 og
   R6 er i hovedsak organisatoriske/politiske,
   mens R2, R3 og R4 er tekniske/prosessuelle.
   Alternativ 2 og 3 adresserer R2–R4 godt, men
   må kombineres med tiltak som adresserer
   R1, R5 og R6.

Disse implikasjonene er tatt opp i den utvidede
sammenligningstabellen i delrapport 4 kap. 6 og
gjentatt i delrapport 7 kap. 5.4.

### 9.6 Kunnskapshull

Rotårsaksanalysen hviler på kildene identifisert
over, men flere spørsmål kan ikke besvares uten
primærdata:

- Hvilken av rotårsakene R1–R6 er mest
  kostnadseffektiv å adressere først, når
  tiltak over flere rotårsaker sammenlignes?
- I hvilken grad vil organisatoriske tiltak
  alene (alternativ 1) være tilstrekkelige for
  R5 og R6, eller forutsetter disse også
  tekniske tiltak?
- Hvor robust er kausalkjede D (fritekst →
  blokkert automatisering) for ulike
  KI-arkitekturer? Noen modeller kan håndtere
  ustrukturert fritekst direkte, andre krever
  strukturerte data.

---

Sist oppdatert: 2026-04-27

---

## Merknad om kilder

Flere sentrale indikatorer i denne rapporten mangler
etterprøvbar dokumentasjon:

- **Produksjonskapasitet (FHI og
  Helsedirektoratet)**: Presise tall for årlig
  produksjon av systematiske oversikter,
  retningslinjer og innbyggerartikler finnes ikke i
  offentlig tilgjengelige kilder. Disse bør
  innhentes gjennom direkte kontakt med
  organisasjonene.

- **Oppdateringsgrad for retningslinjer**:
  Systematisk oversikt over hvor stor andel av
  Helsedirektoratets retningslinjer som er oppdatert
  eller utdaterte finnes ikke. Dette bør kartlegges
  gjennom arkivgjennomgang.

- **Gjennomløpstider**: Som dokumentert i
  delrapport 1, mangler nøyaktige målinger av hvor
  lang tid hvert ledd i verdikjeden tar.

- **Informasjonskilder**: Presise tall for hvor stor
  andel av innbyggere som bruker Google vs.
  Helsenorge vs. medier *som første kilde* for
  helseinformasjon mangler. Likeledes mangler
  spesifikk statistikk på bruk av generativ AI
  *spesifikt for helseinformasjon*.

Disse manglende tallene er kritiske for å vurdere
omfanget av utfordringene identifisert i denne
rapporten. De bør prioriteres for innsamling i
senere faser av prosjektet.

---

## Referanser

[1]: Helse- og omsorgsdepartementet. *Meld. St. 9
(2023–2024), kapittel 6: En kunnskapsbasert og godt
ledet tjeneste med god kvalitet og pasient- og
brukersikkerhet*.
<https://www.regjeringen.no/no/dokumenter/meld.-st.-9-20232024/id3027594/?ch=6>

[2]: Helse- og omsorgsdepartementet. *Meld. St. 9
(2023–2024), kapittel 9: Digitalisering i helse-
og omsorgstjenesten*.
<https://www.regjeringen.no/no/dokumenter/meld.-st.-9-20232024/id3027594/?ch=9>

[3]: Sørlandet sykehus HF. *Revisjonsrapport:
Nasjonale faglige retningslinjer – implementering
og etterlevelse* (2025).
<https://www.sshf.no/49981b/siteassets/dokumenter/styredokumenter/styredokumenter-2025/2025-05/032-2025-vedl-revisjonsrapport-nasjonale-faglige-retningslinjer---implementering-og-etterlevelse-sshf-1.pdf>

[4]: Sykepleien. *Hvordan helsesøstre bruker
kunnskapskilder*.
<https://sykepleien.no/sites/default/files/pdf-export/pdf-export-64242.pdf>

[5]: DNV. *Ny rapport: Digital helse gir bedre
behandling, men øker ikke produktiviteten* (2025).
<https://www.dnv.no/news/2025/ny-rapport-digital-helse-gir-bedre-behandling-men-oker-ikke-produktiviteten/>

[6]: Helsedirektoratet. *Kunnskapsgrunnlag for plan
for digitalisering på legemiddelområdet*.
<https://www.helsedirektoratet.no/digitalisering-og-e-helse/plan-for-digitalisering-pa-legemiddelomradet/kunnskapsgrunnlag-for-plan-for-digitalisering-pa-legemiddelomradet>

[7]: Helsebiblioteket. *Kunnskapsbasert praksis –
kunnskapsbasertpraksis.no*.
<https://www.helsebiblioteket.no/innhold/artikler/kunnskapsbasert-praksis/kunnskapsbasertpraksis.no>

[8]: Helsebiblioteket. *Kunnskap til handling –
implementeringsverktøy basert på RNAO-modellen*.
<https://www.helsebiblioteket.no/innhold/artikler/kunnskapsbasert-praksis/kunnskapsbasertpraksis.no/5.anvende/5.1-kunnskap-til-handling>
