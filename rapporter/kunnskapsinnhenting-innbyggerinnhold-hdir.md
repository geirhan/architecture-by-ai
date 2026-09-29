# Kunnskapsinnhenting: Innbyggerrettet innhold Helsedirektoratet har ansvar for

**Status**: Utforskende — kunnskapsinnhentingsnotat

**Sist oppdatert**: 2026-09-29

## Om dette notatet

Notatet gir en samlet oversikt over hvilket innbyggerrettet
innhold Helsedirektoratet (Hdir) har ansvar for, og hva slags
ansvar det er. Det er laget som underlag til arbeidet med
nasjonalt ansvar for kunnskaps- og informasjonsforvaltning
(jf. [oppdragsteksten](../kilder/oppdragstekst.md)), der
spørsmålet er hvilke kilder en offentlig KI-tjeneste for
målrettede helseråd kan bygge på, og hvem som har ansvar for
dem.

Utredningen har til nå beskrevet den innbyggerrettede strømmen
overordnet ([delrapport 1, kap. 3d](dagens-verdikjede.md)), men
ingen dokumenter i prosjektet gir en oversikt over hva Hdir
selv står ansvarlig for.

**Metode** (2026-09-29):

1. Fire parallelle søk: helsedirektoratet.no; helsenorge.no og
   Helfo; kampanjer, apper, hjelpetelefoner og andre nettsteder;
   lokale prosjektdokumenter i OneDrive-mappen.
2. **Fullstendig gjennomgang av helsenorge.no**: Alle 2 707
   URL-er i nettstedets sitemap er hentet, og feltet «Innholdet
   er levert og kvalitetssikret av …» og datoen i
   kildehenvisningen («oppdatert …») er lest ut maskinelt.
   Resultatet for Hdir og Helfo ligger i vedlegget
   [innbyggerinnhold-hdir-helsenorge.csv](innbyggerinnhold-hdir-helsenorge.csv)
   (1 179 sider).
3. Egen kontroll av sentrale primærkilder: hovedinstruksen
   (27.01.2026), tildelingsbrevet for 2026 og Hdirs side om
   innholds-API-et.

Utsagn er merket **[DOK]** (dokumentert i navngitt kilde),
**[ANT]** (vurdering eller slutning) eller **[USIKKER]**
(tvetydig eller ikke bekreftet).

**Tolkning av oppdraget**: «Informasjonsforvaltningsoppdraget»
er her lest som arbeidet med nasjonalt ansvar for kunnskaps- og
informasjonsforvaltning, altså samme spor som utredningen.
Rent administrativ informasjon (f.eks. om tilskudd og
autorisasjon) er ikke med, med mindre den er rettet mot
innbyggere som pasienter, brukere eller pårørende.

---

## Hovedbudskap

1. **Hdir er den største innholdsleverandøren på helsenorge.no.**
   Hdir står som leverandør på 973 av 2 252 sider som har
   leverandørmerking (43 %). På bokmål er det 462 av 1 474 sider
   (31 %). Helfo, som er Hdirs ytre etat, leverer ytterligere
   230 sider. Til sammen står Hdir og Helfo bak 1 179 sider.
   Delrapport 1 og aktøranalysen beskriver Hdir mest som utgiver.
   Tallene viser at Hdir også er den største faglige
   produsenten. [DOK, egen opptelling]
2. **Nesten alt flerspråklig innhold på Helsenorge kommer fra
   Hdir**: omtrent 90 % av sidene på innvandrerspråk (235 av 259)
   og 51 av 67 sider på nordsamisk. [DOK, egen opptelling]
3. **Hdir har minst seks ulike typer ansvar**, og de gir ulik
   kontroll over innholdet: utgiver, faglig produsent,
   dataansvarlig, etatsstyrer (Helfo), medeier og finansierer
   eller oppdragsgiver. En stor del av innholdet som finansieres
   av Hdir, redigeres av andre, for eksempel RUStelefonen/Rusinfo,
   dinutvei.no og Verdensdagen for psykisk helse. [DOK/ANT]
4. **Innbyggerinnhold på helsedirektoratet.no er hengt på
   fagprodukter**, ikke organisert som en egen kategori.
   Eksempler er pasientinformasjon i pakkeforløp og i
   sykmelderveilederen, og rundt 40 brosjyrer. Hdirs innholds-API
   sier rett ut at **«Målgruppe er ikke tatt i bruk i
   innholdet»**. Da kan innbyggerinnhold ikke skilles maskinelt
   fra innhold for helsepersonell. Det er et direkte hinder for
   KI-klare data. [DOK]
5. **Grunnlaget for utgiveransvaret på Helsenorge er uklart.**
   Den gjeldende redaksjonelle modellen (NHN, 2022) sier at
   «Direktoratet for e-helse har rollen utgiver *og ansvarlig
   redaktør*». Andre kilder, inkludert delrapport 1, legger
   redaktøransvaret til NHN. Hovedinstruksen fra 2026 nevner
   ikke Helsenorge eller utgiveransvaret. [DOK]
6. **Omfanget vokser.** Tildelingsbrevet for 2026 gir Hdir minst
   seks nye oppdrag om innbyggerinformasjon på Helsenorge, blant
   annet om pårørende, eldre, prioritering, gynekologiske
   undersøkelser, fritt sykehusvalg og en digital veiviser.
   I tillegg kommer oppfølgingen av KI-tjenesten. [DOK]
7. **Oppdateringsstatus**: 23 % av Hdirs daterte sider på
   Helsenorge har ikke vært oppdatert på over tre år. Snittet for
   hele nettstedet er 16 %, for Helfo 11 % og for BMJ-innholdet
   41 %. Kvalitetsretningslinjene krever faglig gjennomgang minst
   hvert tredje år. [DOK, egen opptelling; se forbehold i 2.1]

---

## 1. Seks typer ansvar

Hdirs forhold til innbyggerinnhold spenner fra fullt eierskap
til ren finansiering. Skillet betyr mye for spørsmålet om hvilke
kilder en KI-tjeneste kan bygge på, og hvem som kan stilles til
ansvar for kvaliteten.

| Ansvarstype | Hva det innebærer | Eksempler |
| --- | --- | --- |
| Utgiver | Etisk og rettslig ansvar for innholdet i en kanal, uavhengig av hvem som skrev det | Alt redaksjonelt innhold på helsenorge.no |
| Faglig produsent | Hdir skriver og kvalitetssikrer innholdet selv | 973 sider på Helsenorge, kostrådene, brosjyrer, pasientinformasjon i pakkeforløp |
| Dataansvarlig | Ansvar etter personvernregelverket for en løsning | Kjernejournal, e-resept, chat og talerobot på Helsenorge |
| Etatsstyrer | Hdir styrer Helfo, som produserer eget innhold | 230 Helfo-sider på Helsenorge, helfo.no |
| Medeier | Delt ansvar med andre etater | Nøkkelhullet og Kostholdsplanleggeren (med Mattilsynet) |
| Finansierer eller oppdragsgiver | Hdir betaler eller bestiller, andre redigerer | RUStelefonen/Rusinfo, dinutvei.no, Verdensdagen for psykisk helse, hjelpetelefoner |

[ANT] For en KI-tjeneste er det bare de tre første typene (og
til dels den fjerde) der Hdir kan garantere kvalitet og
oppdatering direkte. Innhold i de to siste gruppene er
innbyggerrettet og ofte Hdir-finansiert, men Hdir har ikke
redaksjonell kontroll over det.

---

## 2. Helsenorge.no

### 2.1 Opptelling av innholdsleverandører

**Grunnlag** [DOK]: 2 707 URL-er fra
[helsenorge.no/sitemap.xml](https://www.helsenorge.no/sitemap.xml),
hentet 2026-09-29. 2 252 sider har leverandørmerking. De 454 uten
merking er for det meste oversiktssider, oversettelsessider og
samvalgsverktøy.

| Leverandør | Sider i alt | Bokmål | Daterte sider eldre enn 3 år |
| --- | ---: | ---: | ---: |
| **Helsedirektoratet** | **973** | **462** | 23 % |
| Giftinformasjonen (FHI) | 351 | 337 | 5 % |
| **Helfo** | **230** | **132** | 11 % |
| Folkehelseinstituttet (øvrig) | 119 | 67 | 18 % |
| Norsk helsenett | 103 | 45 | 17 % |
| Oslo universitetssykehus | 95 | 88 | – |
| BMJ Best Practice | 76 | 74 | 41 % |
| Alle med leverandørmerking | 2 252 | 1 474 | 16 % |

Merknader:

- En side kan ha flere leverandører. 96 Hdir-sider er levert
  sammen med andre, oftest NHN (25), Helfo (24), Nasjonalt senter
  for selvmordsforskning og -forebygging (21), FHI (20) og
  Pasientreiser (15). [DOK]
- Giftinformasjonen har ligget under FHI siden 2015 og er derfor
  ikke regnet som Hdir-innhold
  ([SML](https://sml.snl.no/Giftinformasjonen),
  [FHIs historie](https://www.fhi.no/om/fhi/folkehelseinstituttets-historie/)).
  [DOK]
- **Forbehold om datoene** [USIKKER]: Datoen er hentet fra den
  automatisk genererte kildehenvisningen på siden («oppdatert …»).
  Den kan vise siste redigering og ikke nødvendigvis siste faglige
  gjennomgang. Andelen «eldre enn 3 år» er derfor en indikasjon,
  ikke et mål på brudd på treårskravet. Ikke-norske sider mangler
  som regel norsk datoformat og er ikke med i aldersberegningen.
- **Forbehold om dekning** [USIKKER]: Tellingen forutsetter at
  sitemapen er fullstendig. Det er ikke kontrollert mot
  publiseringsløsningen (CMS). Merkingen viser hvem som
  *leverer* innholdet, ikke nødvendigvis hvilken avdeling i Hdir
  som er faglig ansvarlig.

### 2.2 Hva Hdir-innholdet dekker

De største temaområdene blant Hdirs 462 bokmålssider [DOK]:

| Temaområde (URL-segment) | Sider | Eksempler |
| --- | ---: | --- |
| Sykdom | 122 | Psykiske lidelser (17), matallergi (10), øyesykdommer (10), diabetes (9), mage-tarm (8), demens (7), pakkeforløp for kreft, psykisk helsevern |
| Gravid | 46 | Svangerskapsomsorg, kosthold i svangerskapet |
| Hjelpetilbud i kommunene | 38 | BPA, avlastning, helse- og omsorgstjenester |
| Barn | 27 | Barns helse og utvikling |
| Psykisk helse | 24 | Selvmordstanker, selvskading, stress |
| Kosthold og ernæring | 19 | Kostråd, vegetarkost for spedbarn og gravide |
| Rettigheter | 17 | Pasient- og brukerrettigheter |
| Trening og fysisk aktivitet | 13 | Aktivitetsråd |
| Hørsel, syn, undersøkelse og behandling, sex og samliv, rus, førstehjelp, snus og røykeslutt, utlendinger i Norge | 5–12 hver | Blant annet jodtabletter ved atomulykker og rettigheter for flyktninger |

I tillegg eier Hdir levevanesatsingen **Lev**
([helsenorge.no/lev](https://www.helsenorge.no/lev/)), som er
«levert og kvalitetssikret av Helsedirektoratet». Den har
underverktøy som salttest og selvtest. [DOK]

[ANT] Det er verdt å merke seg at Hdir leverer 122
sykdomsartikler. Utkastet til oppdrag om KI-tjenesten
(supplerende tildelingsbrev, mars 2026) nevner at Hdir «må
frigjøre personer som produserer innhold på Helsenorge
(helsepersonell?)». Spørsmålstegnet tyder på at det internt er
uklart hvem i Hdir som produserer dette innholdet.

### 2.3 Helfo-innholdet

Helfos 132 bokmålssider handler om behandling i utlandet (34),
refusjon og støtteordninger (21), bo i utlandet (19), betaling
for helsetjenester (15), utlendinger i Norge (13), klage og
erstatning, rettigheter, fastlegebytte og frikort. [DOK]

[ANT] Dette er rettighets- og ytelsesinformasjon og ikke
helseråd. Søkeordsanalysen for 2026 (lokal fil, se kap. 6)
viser at nettopp tjenestetemaene (frikort, fastlege, resept,
Helfo, pasientreiser) er der Helsenorge dekker søkene best,
med 86 % topp 3-plassering.

### 2.4 Tjenester og data der Hdir har ansvar

| Tjeneste | Hdirs rolle | Kilde |
| --- | --- | --- |
| Kjernejournal (innbyggervisning) | Dataansvarlig fra 1.6.2024. NHN er databehandler. | [DOK] [Hdir](https://www.helsedirektoratet.no/nyheter/far-dataansvar-for-kjernejournal-og-e-resept), hovedinstruksen kap. 3.2 |
| E-resept, Mine resepter | Dataansvarlig fra 1.6.2024 | [DOK] Samme kilder |
| Chat og talerobot på Helsenorge | Dataansvarlig. Helfo betjener chatten. | [DOK] [Hdirs personvernerklæring](https://www.helsedirektoratet.no/om-oss/om-nettstedet/personvernerklaering/nar-behandler-vi-personopplysninger/pa-nett-og-dialog-med-innbyggere) |
| Velg behandlingssted (ventetider) | Hdir eier veilederen for ventetidsberegning. Behandlingsstedene rapporterer. | [DOK] [Veileder](https://www.helsedirektoratet.no/veiledere/veileder-for-fastsetting-av-forventede-ventetider-til-informasjonstjenesten-velg-behandlingssted) |
| Nasjonale kvalitetsindikatorer | Lovpålagt ansvar. Pasienter og innbyggere er uttalt målgruppe. Publiseres på helsedirektoratet.no. | [DOK] [Kvalitetsindikatorer](https://www.helsedirektoratet.no/statistikk/kvalitetsindikatorer), hovedinstruksen kap. 3.2 |

[ANT] Her gjelder et annet styringsregime (dataansvar og
registerregelverk) enn for det redaksjonelle innholdet
(utgiveransvar og kvalitetsretningslinjer). En KI-tjeneste som
skal gi personlig tilpassede råd, må forholde seg til begge.

### 2.5 Styringsdokumentene for utgiveransvaret

NHNs innholdsstrategi for Helsenorge 2021–2026 består av tre
dokumenter [DOK]:

- [Redaksjonell modell](https://www.nhn.no/tjenester/helsenorge/helseinformasjon/innholdsstrategi-for-helsenorge/_/attachment/inline/1bdac36d-bd10-4f23-b270-f93f7455927e:3212231446159bfc4d81491b2e362e972ce96531/redaksjonell-modell.pdf)
  (2022). Utgiveren «står etisk og rettslig ansvarlig for
  innholdet», har ansvar for «utgivergrunnlag, herunder formål,
  krav og retningslinjer for faglig kvalitet» og for
  «virkemidler som får aktørene i sektoren til å bidra med
  innhold». Modellen sier: «Direktoratet for e-helse har rollen
  utgiver og ansvarlig redaktør.» NHN har en egen taktisk
  redaktørrolle og kan stoppe innhold.
- [Retningslinjer for kvalitet](https://www.helsenorge.no/49aec9/globalassets/redaksjonelt/retningslinjer-for-kvalitet.pdf).
  Fem prinsipper: relevant, tilgjengelig, kunnskapsbasert,
  etterprøvbart og oppdatert. Innholdet skal sjekkes av faglig
  ansvarlig «minst hvert tredje år».
- [Innholdsstrategien](https://www.helsenorge.no/49efff/globalassets/redaksjonelt/innholdsstrategi-helsenorge.pdf)
  med [Helsenorgemetoden](https://www.helsenorge.no/49aed5/globalassets/redaksjonelt/helsenorgemetoden.pdf).

Åpne punkter:

- **Utgiver etter fusjonen** [USIKKER]: Ingen oppdatert versjon
  av den redaksjonelle modellen etter at Direktoratet for e-helse
  ble innlemmet i Hdir 1.1.2024 er funnet. At utgiverrollen er
  videreført til Hdir, er en rimelig slutning [ANT], men den er
  ikke dokumentert i et styringsdokument.
- **«Ansvarlig redaktør»** [USIKKER]: Modellen gir
  direktoratet rollen som ansvarlig redaktør. Helsenorges
  om-side og [delrapport 1](dagens-verdikjede.md) sier at NHN har
  redaktøransvaret. Begrepene brukes ulikt i prosjektets egne
  dokumenter også («redaktøransvar», «redaksjonsansvar»,
  «redaksjonelt ansvar»).
- **Hovedinstruksen** (fastsatt 27.01.2026) sier at Hdir skal
  «gi råd i faglige spørsmål … samt befolkningen», og at Hdir er
  «nasjonal myndighet for digitalisering og
  informasjonsforvaltning». Den nevner **ikke** Helsenorge eller
  utgiveransvaret. [DOK] Det støtter det Utredning v2.0 (lokal
  fil) skriver, nemlig at «utgiveransvaret ikke er understøttet
  av styringsdokumenter».
- **Innholdsstrategien gjelder til og med 2026.** [DOK] Den går
  altså ut samtidig som utredningen leverer sin anbefaling.

---

## 3. Helsedirektoratet.no

Hovedtyngden av helsedirektoratet.no er skrevet for helsepersonell
og tjenesteytere. Innbyggerinnhold finnes, men er spredt og
hengt på fagprodukter. [DOK/ANT]

| Innholdsgruppe | Målgruppe | Hdirs rolle | Kilde |
| --- | --- | --- | --- |
| Kostråd for befolkningen (revidert 15.08.2024) | Befolkningen, også brukt av fagfolk | Faglig eier og utgiver | [DOK] [Kostråd](https://www.helsedirektoratet.no/faglige-rad/kostradene-og-naeringsstoffer/kostrad-for-befolkningen) |
| Pasientinformasjon i pakkeforløp (f.eks. «Pakkeforløp hjem», hjerneslag) | Pasienter og pårørende | Faglig eier | [DOK] [Hjerneslag](https://www.helsedirektoratet.no/nasjonale-forlop/hjerneslag/pasientinformasjon) |
| Pasientinformasjon i sykmelderveilederen (egenmelding, gradert sykmelding, sorg) | Pasienter | Faglig eier | [DOK] [Sykmelderveilederen](https://www.helsedirektoratet.no/veiledere/sykmelderveileder/pasientinformasjon) |
| Brosjyrer og plakater (om lag 40). Trykte bestillinger stanset 1.7.2022, nå bare PDF. | Mest innbyggere | Faglig eier | [DOK] [Brosjyrer](https://www.helsedirektoratet.no/brosjyrer) |
| Kalkulator for helseeffekter av fysisk aktivitet | Innbyggere | Eier | [DOK] |
| Nasjonale kvalitetsindikatorer | Pasienter, tjenesten og myndigheter | Ansvarlig etter loven | [DOK] Se 2.4 |
| Kommunikasjonsmateriell om deling av helseopplysninger (PJD) | Helsepersonell og innbyggere | Produsent | [DOK] [PJD](https://www.helsedirektoratet.no/digitalisering-og-e-helse/pasientens-journaldokumenter-pjd/Kommunikasjonsmateriell_deling_av_helseopplysninger) |
| Temaside om forebyggende hjemmebesøk | Eldre og pårørende (skal revideres) | Eier | [DOK] Tildelingsbrevet 2026, TB2026-20 |

**Innholds-API-et (HAPI)** [DOK]
([Om API-tjenesten](https://www.helsedirektoratet.no/om-oss/apne-data-api/om-api-tjenesten),
[Hvordan finne frem i innholdet](https://www.helsedirektoratet.no/om-oss/apne-data-api/hvordan-finne-frem-i-innholdet)):

- Retningslinjer, råd, pakkeforløp, rundskriv, artikler m.m.
  leveres som JSON, Markdown og HTML under lisensen NLOD.
- Innholdet er hierarkisk: produkt → kapittel → normerende enhet
  → referanser/PICO.
- Det finnes om lag 40 innholdstyper. **Ingen av dem er
  «brosjyre» eller «pasientinformasjon».**
- Innholdet kodes med ICPC-2, ICD-10 og SNOMED CT, men sitat:
  **«Målgruppe er ikke tatt i bruk i innholdet.»**

[ANT] Nettstedets robots.txt sperrer stien `/malgrupper/`. Det
tyder på at publiseringsløsningen har en målgruppestruktur som
ikke er tatt i bruk på innholdet. Dette er ikke bekreftet.

**Hdirs synlighet i søk** [DOK, søkeordsanalysen 2026, lokal
fil]: helsedirektoratet.no er blant de fem øverste treffene på
bare om lag 4 % av helsesøkevolumet. Unntakene er Hdirs egne
folkehelseområder: kostråd (52 %), fysisk aktivitet (68 %) og
snus og røyk (32 %).

**Hull i dette søket**: Temaoversikten `/tema` ga 404-feil, og
sitemapen for helsedirektoratet.no er avkortet ved nøyaktig
10 000 URL-er uten brosjyreseksjonen. Omfanget av
innbyggerinnhold på helsedirektoratet.no er derfor ikke talt
opp. [DOK]

---

## 4. Andre kanaler: kampanjer, apper, hjelpetelefoner og samarbeid

### 4.1 Hdir eier eller er avsender

| Navn | Type | Kilde |
| --- | --- | --- |
| Slutta-appen (røyk, snus og fra 2025 også vape; over 1,5 mill. nedlastinger) | App | [DOK] [Hdir-nyhet](https://www.helsedirektoratet.no/nyheter/kutter-vape-med-slutta-appen) |
| sigarettavhengighet.no (Fagerström-test) | Nettsted. Hdir er behandlingsansvarlig. | [DOK] [Personvern](https://www.sigarettavhengighet.no/personvern.html) |
| roykesluttgevinster.no | Nettsted | [USIKKER] Eierskap ikke bekreftet |
| Lev (tidligere «Bare Du»), kommunikasjonskonsept for levevaner | Kampanje, landingsside på Helsenorge, annonsørinnhold i VG | [DOK] |
| Stopptober | Årlig kampanje, annonsørinnhold i VG og Nettavisen | [DOK] [Hdir-nyhet](https://www.helsedirektoratet.no/nyheter/na-er-det-stopptober-igjen) |
| Generasjon FRI (nikotin, 13–17 år) | Kampanje med landingsside på ung.no, som Bufdir eier | [DOK] |
| ABC for god psykisk helse (5,2 mill. kr i 2026) | Nasjonal informasjon fra Hdir, lokal gjennomføring i fylkene | [DOK] Tildelingsbrevet 2026 |
| Antibiotikakampanje | Kampanje med byrå | [USIKKER] Status ikke kjent |
| YouTube-kanalen «Helsedirektoratet» og profiler på andre sosiale medier | Video og korte formater | [DOK] Omfanget ikke kartlagt |

### 4.2 Hdir er medeier

| Navn | Rolle | Kilde |
| --- | --- | --- |
| Nøkkelhullet | «Helsedirektoratet og Mattilsynet har ansvar for ordningen» | [DOK] [Hdir](https://www.helsedirektoratet.no/tema/kosthold-og-ernaering/matbransje-serveringsmarked-og-arbeidsliv/merkeordningen-nokkelhullet) |
| Kostholdsplanleggeren | Utviklet og finansiert sammen med Mattilsynet | [DOK] [kostholdsplanleggeren.no](https://kostholdsplanleggeren.no/) |
| Matvaretabellen | Mattilsynet har det administrative ansvaret. Hdir har vært med på finansieringen. | [DOK/USIKKER] [Mattilsynet](https://www.mattilsynet.no/mat-og-drikke/matvaretabellen/opphavsrett); dagens finansieringsandel ikke bekreftet |
| Matportalen | Lagt ned, innholdet flyttet til mattilsynet.no | [DOK] [Mattilsynet](https://www.mattilsynet.no/mat-og-drikke/forbrukere/matportalen-er-lagt-ned) |

### 4.3 Hdir finansierer eller bestiller, andre redigerer

| Navn | Hvem redigerer | Kilde |
| --- | --- | --- |
| RUStelefonen/Rusinfo | Velferdsetaten i Oslo kommune, på oppdrag fra og finansiert av Hdir siden 2002 | [DOK] [Rusinfo om oss](https://rusinfo.no/om-rustelefonen/) |
| dinutvei.no (vold og overgrep) | NKVTS, på oppdrag fra Hdir | [DOK] |
| Verdensdagen for psykisk helse | Mental Helse, finansiert av Hdir | [DOK] [verdensdagen.no](https://www.verdensdagen.no/) |
| Hjelpetelefoner og chat innen psykisk helse, rus og vold | Ulike organisasjoner, via tilskudd fra Hdir | [DOK] [Tilskuddsordningen](https://www.helsedirektoratet.no/tilskudd-og-finansiering/tilskudd/hjelpetelefon-og-chattilbud-innen-psykisk-helse-rusmiddel-og-voldsfeltet) |
| Hjelpelinjen (spill) | Samarbeid mellom Lotteritilsynet og Sykehuset Innlandet | [USIKKER] Hdirs rolle ikke bekreftet |
| Gjør kloke valg (3 mill. kr i tilskudd i 2026) | Legeforeningen | [DOK] Tildelingsbrevet 2026 |
| Informasjonsarbeid i pasient- og brukerorganisasjoner | Mottakerorganisasjonene | [DOK] [Tilskudd](https://tilskudd.lottstift.no/ordning/DT-0656/2025/frivillig-informasjons-og-kontaktskapende-arbeid) |
| organdonasjon.no | Stiftelsen Organdonasjon. Hdir er samarbeidspartner. | [DOK] [organdonasjon.no](https://organdonasjon.no/) |

[ANT] Dette er innbyggerrettet helseinformasjon som ofte bærer
Hdirs navn eller finansiering, men der Hdir ikke kontrollerer
den faglige kvaliteten. Om slikt innhold skal kunne være kilde
for en offentlig KI-tjeneste, er et prinsipielt spørsmål som
bør avklares.

---

## 5. Nye oppdrag i 2026 om innbyggerinformasjon

Fra [tildelingsbrevet 2026](https://sikt-fvdb-storage.s3.eu-north-1.amazonaws.com/tildelingsbrev/helsedirektoratet_tildeling_2026.pdf)
[DOK]:

| Oppdrag | Innhold | Frist |
| --- | --- | --- |
| TB2026-17 Digital førstelinje | Følge opp rapporten «En offentlig KI-tjeneste for helserelaterte spørsmål på Helsenorge» (8.10.2025). Etablere første trinn av en digital veiviser inn til helsetjenestene, sammen med NHN. | 31.12.2026 |
| TB2026-15 Allmennlegetjenesten | Pasientinformasjon om gynekologiske undersøkelser på helsenorge.no og ung.no, sammen med Legeforeningen | 30.6.2026 |
| TB2026-20 Bo trygt hjemme | Informasjon på helsenorge.no for eldre og pårørende. Revidere temasiden om forebyggende hjemmebesøk. Gjennomgå pårørendesidene på Helsenorge («byråkratisk» språk, vanskelig å finne). | 1.11.2026 |
| TB2026-23 Prioritering (Meld. St. 21) | Informasjon om prioritering på helsenorge.no og en informasjonsstrategi for befolkningen | – |
| TB2026-60 Ventetid | «Bedre informasjon på Helsenorge» om fritt sykehusvalg | – |
| Styringsparameter 3.2.1 | «Gjøre det enklere for befolkningen å finne, forstå og ta i bruk råd om levevaner». Nøkkeltall: kjennskap og tillit til kostrådene og Nøkkelhullet. | Løpende |
| Styringsparameter 3.3.1 | «Bidra til økt helsekompetanse i befolkningen» | Løpende |
| TB2026-38 Informasjonsforvaltning, kodeverk og terminologi | Helhetlig strategi for kodesystemer og standarder, koordinert med EHDS | – |

[ANT] Oppdragene legger mer innbyggerinnhold til Hdir, mens
spørsmålet om hvem som skal forvalte det, fortsatt er åpent.

---

## 6. Hva de lokale prosjektdokumentene sier

Kort oppsummering av skanningen av OneDrive-mappen [DOK, interne
dokumenter]:

- **Ingen dokumenter har en oversikt** over hvilket
  innbyggerinnhold Hdir selv har ansvar for. Kampanjer,
  Helfo-innhold og innbyggerinformasjon om kjernejournal og
  e-resept er ikke omtalt.
- **KKD-notatet** («Helsenorge og utfordringer med
  innholdsartikler», utkast): Snaut 20 % av sykdomsartiklene
  (fra BMJ) forsvinner 31. august. NHN har foreslått at Hdir
  «overtar det faglige ansvaret» for omskrevne tekster. FHI og
  Hdir har avvist forslaget. Helsenorge mangler innhold om
  hverdagsplager. *Tellingen i dette notatet fant 76 sider med
  BMJ som leverandør per 29.9. Om det er rester som fortsatt skal
  fjernes, eller andre avtaler, er ikke avklart.* [USIKKER]
- **Utredning v2.0** (Word): Rotårsak 1 sier at det er uklart
  hvem som har det medisinskfaglige ansvaret, og at
  utgiveransvaret ikke er understøttet av styringsdokumenter.
  Nullalternativet sier at Hdir har «det medisinske
  hovedansvaret». Formuleringene trekker i ulik retning.
- **Søkeordsanalysen 2026** (WPP Media): Rundt 6,6 millioner
  helsesøk i måneden. Helsenorge er blant de tre øverste treffene
  på 34 % av volumet når søk på navnet Helsenorge holdes utenfor.
  Dekningen er svak på kosthold (8 %), alkohol (3–5 %) og
  behandling (15 %).
- **Interessentanalysen (RACI)**: «Formidling til innbyggere» har
  ingen som står som øverst ansvarlig (A).

---

## 7. Observasjoner for utredningen

Dette er slutninger [ANT] som underlag for drøfting, ikke
konklusjoner.

1. **Hdir er allerede den største faglige
   innholdsprodusenten.** Spørsmålet om nasjonalt ansvar for
   informasjonsforvaltning handler derfor ikke bare om å
   *tildele* et ansvar. Det handler også om å *formalisere og
   samle* et ansvar Hdir i praksis har, men som er fordelt på
   mange avdelinger uten felles styringsgrunnlag.
2. **Målgruppe mangler som metadata** både i Hdirs API og i
   Helsenorges leverandørmerking. For KI-klare data må det
   avgjøres om målgruppe skal legges inn som metadata, eller om
   utvalget av kilder skal styres manuelt. Dette henger sammen
   med transparenslaget i KI-klareData-rammeverket («Er eierskap
   og kvalitet tydelig og kjent?»).
3. **Ansvaret er fordelt på seks typer**, og det gir ulik
   kontroll. Å avgrense en KI-tjenestes kildegrunnlag til
   innhold der Hdir er utgiver eller produsent er enkelt å
   begrunne. Å ta med finansiert innhold krever egne avtaler om
   kvalitet.
4. **Flerspråklig innhold er i praksis et Hdir-ansvar.** Det er
   relevant for tjenestens språkkrav (bokmål, nynorsk og
   samisk).
5. **Hdirs innhold har en dokumenterbar etterslepsrisiko.** 23 %
   av de daterte sidene er over tre år gamle (se forbeholdet i
   2.1), og det finnes ingen automatisk kobling fra endret
   retningslinje til Helsenorge-artikkel
   ([rolledeling](rolledeling-sentral-helseforvaltning.md)).
6. **Styringsgrunnlaget går ut samtidig med anbefalingen.**
   Innholdsstrategien 2021–2026 og en redaksjonell modell som
   fortsatt nevner Direktoratet for e-helse er et naturlig
   tidspunkt for å revidere utgiverrollen.

---

## 8. Kunnskapshull og forslag til neste steg

| Hull | Forslag |
| --- | --- |
| Formelt grunnlag for utgiveransvaret og rollen «ansvarlig redaktør» etter fusjonen | Be NHN og Hdirs juridiske avdeling bekrefte gjeldende modell |
| Hvilke avdelinger i Hdir som leverer de 973 sidene, og med hvilke ressurser | Hent ut lokal redaktør og faglig ansvarlig per side fra Helsenorges publiseringsløsning (CMS) via NHN |
| Faktisk dato for siste faglige gjennomgang, ikke bare siste redigering | Samme uttrekk fra CMS |
| Omfanget av innbyggerinnhold på helsedirektoratet.no | Uttrekk fra Hdirs CMS eller API med innholdstype «brosjyre» eller «pasientinformasjon» |
| Om `/malgrupper/` i Hdirs CMS kan tas i bruk som metadata | Avklar med forvalteren av innholds-API-et |
| BMJ-sidene som fortsatt ligger ute (76) | Avklar med Helsenorge-redaksjonen |
| Hdirs rolle i Hjelpelinjen, roykesluttgevinster.no og Matvaretabellen | Enkel verifisering per tjeneste |
| Innhold i sosiale medier | Egen kartlegging hvis det er aktuelt som kilde |
| Helfos plass i den redaksjonelle modellen (egen lokal redaktør eller under Hdir) | Avklar med Helfo og NHN |

---

## Kilder

**Styringsdokumenter**

- [Hovedinstruks for Helsedirektoratet, 27.01.2026](https://www.regjeringen.no/contentassets/d8f63d7d01d64def982cb7c8ce1eeb64/hovedinstruks-for-helsedirektoratet2.pdf)
- [Tildelingsbrev 2026 til Helsedirektoratet](https://sikt-fvdb-storage.s3.eu-north-1.amazonaws.com/tildelingsbrev/helsedirektoratet_tildeling_2026.pdf)
- [Redaksjonell modell, Helsenorge (NHN, 2022)](https://www.nhn.no/tjenester/helsenorge/helseinformasjon/innholdsstrategi-for-helsenorge/_/attachment/inline/1bdac36d-bd10-4f23-b270-f93f7455927e:3212231446159bfc4d81491b2e362e972ce96531/redaksjonell-modell.pdf)
- [Retningslinjer for kvalitet, Helsenorge](https://www.helsenorge.no/49aec9/globalassets/redaksjonelt/retningslinjer-for-kvalitet.pdf)
- [Innholdsstrategi Helsenorge 2021–2026](https://www.helsenorge.no/49efff/globalassets/redaksjonelt/innholdsstrategi-helsenorge.pdf)
- [Helsenorgemetoden](https://www.helsenorge.no/49aed5/globalassets/redaksjonelt/helsenorgemetoden.pdf)

**Helsedirektoratet**

- [Om API-tjenesten](https://www.helsedirektoratet.no/om-oss/apne-data-api/om-api-tjenesten)
- [Hvordan finne frem i innholdet (API)](https://www.helsedirektoratet.no/om-oss/apne-data-api/hvordan-finne-frem-i-innholdet)
- [Om Helsedirektoratets normerende produkter](https://www.helsedirektoratet.no/om-oss/om-helsedirektoratets-normerende-produkter)
- [Brosjyrer](https://www.helsedirektoratet.no/brosjyrer)
- [Kostråd for befolkningen](https://www.helsedirektoratet.no/faglige-rad/kostradene-og-naeringsstoffer/kostrad-for-befolkningen)
- [Nasjonale kvalitetsindikatorer](https://www.helsedirektoratet.no/statistikk/kvalitetsindikatorer)
- [Offentlig KI-tjeneste for helserelaterte spørsmål](https://www.helsedirektoratet.no/digitalisering-og-e-helse/kunstig-intelligens/offentlig-ki-tjeneste-for-helserelaterte-sporsmal)
- [Personvern: på nett og dialog med innbyggere](https://www.helsedirektoratet.no/om-oss/om-nettstedet/personvernerklaering/nar-behandler-vi-personopplysninger/pa-nett-og-dialog-med-innbyggere)
- [Får dataansvar for kjernejournal og e-resept](https://www.helsedirektoratet.no/nyheter/far-dataansvar-for-kjernejournal-og-e-resept)
- [Nasjonal digitaliseringsmonitor, besøk på Helsenorge](https://www.helsedirektoratet.no/statistikk/nasjonal-digitaliseringsmonitor/antall-besok-pa-helsenorge--apne-sider)

**Helsenorge og andre kanaler**

- [helsenorge.no/sitemap.xml](https://www.helsenorge.no/sitemap.xml) (hentet 2026-09-29) og
  vedlegget [innbyggerinnhold-hdir-helsenorge.csv](innbyggerinnhold-hdir-helsenorge.csv)
- [helsenorge.no/lev](https://www.helsenorge.no/lev/)
- [Rusinfo, om oss](https://rusinfo.no/om-rustelefonen/)
- [Matvaretabellen, opphavsrett](https://www.mattilsynet.no/mat-og-drikke/matvaretabellen/opphavsrett)
- [Matportalen er lagt ned](https://www.mattilsynet.no/mat-og-drikke/forbrukere/matportalen-er-lagt-ned)
- [organdonasjon.no](https://organdonasjon.no/)
- [Giftinformasjonen (SML)](https://sml.snl.no/Giftinformasjonen)

**Lokale dokumenter** (OneDrive-mappen «00 Kunnskapsforvaltning»)

- Helsenorge og utfordringer med innholdsartikler_KKD (utkast).docx
- Utkast til oppdrag Hdir KI-tjeneste, supplerende tildelingsbrev mars 2026
- Rapport/Utredning – Ansvar for og organisering av nasjonal kunnskapsforvaltning.docx (v2.0)
- Verdikjede i kunnskapsforvaltning for offentlig KI_FHI.docx
- Bakgrunnsinformasjon/Helsenorge søkeordsanalyse master 2026.xlsx og presentasjon (PDF)
- Interessentanalyse Offentlig KI-tjeneste – arbeidsdokument.xlsx
