# Samsvarssjekk: Utredningen mot oppdragsteksten

**Status:** Utforskende – til drøfting med prosjekteier.

**Grunnlag:** Oppdragsteksten i `kilder/oppdragstekst.md`
(uformell gjengivelse, opplyst i prosjektet 2026-08-14 –
en mer formell utgave kan komme og vil i så fall kreve
at denne sjekken oppdateres). Vurderingen bygger på
systematisk gjennomgang av samtlige rapporter i
`rapporter/` per 2026-08-14.

---

## 1. Ledersammendrag

Oppdragsteksten har tre elementer: (1) behov og
problemer med dagens organisering av
kunnskapsforvaltning – vurdert opp mot at kildene skal
benyttes til *utvikling og testing av KI-systemer for
målrettede helseråd*, (2) hvordan ansvar for produksjon
og kvalitet i kunnskapskilder *bør* fordeles, og
(3) igangsetting av arbeid for å definere *rammer for
KI-klare data*.

**Samlet vurdering:** Utredningen har svært sterk
dekning av de *deskriptive* delene av oppdraget og svak
dekning av de *spissede og normative* delene:

| Oppdragselement | Deskriptiv dekning | Spisset/normativ dekning |
|---|---|---|
| 1. Behov/problemer (KI-linsen) | **Høy** – D1–D6, R1–R6, ni flaskehalser, casestudier | **Lav** – KI-formålet er fraværende i problemanalysens formålskapitler |
| 2. Ansvarsfordeling («bør») | **Høy** – aktør-, prosess- og etatsnivå kartlagt | **Delvis** – rollemodell finnes for KI-bruk, men kjernespørsmålet står åpent som veivalg |
| 3. Rammer for KI-klare data | **Høy** – standardkatalog, K6-del-evner, metadatakart | **Lav** – begrepet finnes ikke; ingen kravliste, standardvalg eller igangsatt arbeid |

De tre viktigste funnene:

1. **KI opptrer i utredningen nesten utelukkende som
   løsningsmulighet** (KI-støttet produksjon, RAG,
   chatbot) – ikke som formålet kildene skal
   kvalifiseres mot. Oppdraget spør det motsatte: Er
   kildene egnet som *grunnlag* for utvikling og
   testing av KI-systemer? Begrepet «målrettede
   helseråd» finnes bare fire steder i hele
   rapportsamlingen, ingen av dem i delrapport 1, 2
   eller samlet vurdering. «KI-klare data» finnes ikke
   i noen rapport.
2. **«Bør»-spørsmålet om ansvar er sirkulert, ikke
   besvart.** Veivalget for forholdet stat/forening er
   løftet i fire dokumenter som alle henviser til
   hverandre uten at noen konkluderer eller gir
   utrederens vurdering. Rollemodellen i delrapport 4
   kap. 7.1 er reell, men gjelder ansvar for *KI-bruk
   og governance* – ikke for produksjon og kvalitet i
   kunnskapskildene som sådan.
3. **Byggeklossene for «rammer for KI-klare data»
   finnes spredt, men er ikke samlet til noen
   leveranse.** K6.1–K6.4 er et kravskjelett,
   teknisk-notatet en standardkatalog med
   modenhetsvurdering, metadatastruktur-notatet en
   taksonomi – men det finnes ingen kravliste, ikke noe
   standardvalg for Norge, intet forvaltningsregime, og
   tiltakstabellen i samlet vurdering har ingen
   aktivitet som igangsetter arbeidet.

Ingen rapport refererer i dag til oppdragsteksten, og
det finnes ingen sporing fra oppdragselement til
rapportkapittel.

---

## 2. Detaljerte funn per oppdragselement

### 2.1 Element 1: Behov og problemer – med KI-linsen

**Ordlyd:** «Starte med hva som er behovene og
problemer med dagens organisering av
kunnskapsforvaltning når disse kildene skal benyttes
til utvikling og testing av KI-systemer for målrettede
helseråd»

**Dekket [DOK]:**

- Behovs- og problemanalysen er grundig: delrapport 1
  (fire strømmer, avhengigheter, kvalitetssikring,
  seks observasjoner), delrapport 2 (hovedproblem,
  D1–D6, fem kjerneegenskaper, R1–R6, ni rangerte
  flaskehalser), casestudiene (7–15+ år),
  aktøranalysen (~20 aktører, IGOE).
- Enkeltfunn med direkte KI-relevans finnes:
  fritekst uten metadata som «strukturell blokker for
  en KI-støttet verdikjede» (dp2 kap. 6.6.4 [ANT]);
  uavklart lisensgrunnlag for gjenbruk av
  foreningsinnhold «i en statlig KI-tjeneste» (dp5
  kap. 4.1 [DOK]); åpent spørsmål om AI Act art. 10
  gjelder RAG-kunnskapskorpuset (teknisk-notatet
  kap. 6.1 [ANT], antakelsesregisteret).

**Avvik:**

- Formålskapitlene i delrapport 1 (kap. 1.1) og
  delrapport 2 (kap. 1.1) nevner ikke KI-formålet.
  Avgrensningen i dp1 kap. 1.3 tar ikke stilling til
  om kildene skal tjene som grunnlag for
  KI-utvikling/testing.
- De KI-relevante funnene ligger i *løsningsdelen*
  (dp5, teknisk-notatet) – oppdraget ber analysen
  «starte med» dette.
- Ingen dimensjon eller rotårsak er formulert som
  «kildene er ikke egnet som grunnlag for
  KI-utvikling/-testing». Manglende delanalyser:
  lisens-/rettighetsgrunnlag for KI-bruk, versjonering
  og sporbarhet som forutsetning for testsett,
  dekningsgrad per fagområde, gullstandard-/
  evalueringsdatasett for testing av KI-svar.
- Begrepet «målrettede helseråd» brukes kun i
  `kunnskapsinnhenting-innbyggerrettet-formidling.md`
  (som eneste sted med formålet som eksplisitt ramme)
  og `losningsretninger-bred-kartlegging.md`;
  delrapportene bruker «personaliserte/persontilpassede
  helseråd» uten kobling til oppdragets begrep.

### 2.2 Element 2: Ansvarsfordeling for produksjon og kvalitet

**Ordlyd:** «hvordan bør ansvar for produksjon og
kvalitet i kunnskapskilder fordeles?»

**Dekket [DOK]:**

- *Dagens* fordeling er kartlagt på alle nivåer:
  aktørnivå (dp8 kap. 2–5, IGOE per prosess),
  etatsnivå (rolledelingsrapporten: FHI/Hdir-gråsoner,
  fravær av verdikjedeeier, Røttingen-forslagene ikke
  gjennomført), tosporet normering
  (profesjonsforening-notatet kap. 3 og 3.1: lovfestet
  mandat, 13 av 22 foreninger med egne normerende
  produkter, ingen forrangsregler), helsenorge-ansvaret
  (utgiver- vs. redaktøransvar).
- *Normative* bidrag finnes: rollemodellen i dp4
  kap. 7.1 (Hdir governance/kvalitetsrammeverk for
  KI-generert innhold, FHI validering, NHN drift),
  kvalitetssikringsmodellen i dp4 kap. 7.2–7.3 og 8,
  fire styringsgrep i rolledelingsrapporten kap. 7.2
  (eksplisitt verdikjedemandat, avklart KI-ansvar,
  formalisert bestiller–utfører, avklart
  helsenorge-grensesnitt), grensesnittformalisering
  med ansvarlig aktør per grensesnitt (dp4 kap. 6.4).

**Avvik:**

- Rollemodellen i dp4 kap. 7.1 fordeler ansvar for
  *KI-bruk og governance* – ikke for produksjon og
  kvalitet i kunnskapskildene som sådan.
  Alternativene 0–3 er ambisjonsnivåer, ikke
  alternative ansvarsmodeller; dp4 kap. 6.3 sier selv
  at ingen av dem tar stilling til stat/forening.
- Kjernespørsmålet (innlemme/erstatte/sameksistere)
  står åpent i fire dokumenter som henviser til
  hverandre (dp4 kap. 6.3 → 7.1 → samlet vurdering
  kap. 10.2 pkt. 8 → dp4; kapabilitetskartet har ved
  design henvist hvem-spørsmålet samme sted).
  Oppdraget spør «bør» – utredningen svarer i praksis
  «dette er et veivalg for beslutningstakerne», uten
  utrederens egen vurdering.
- Tverrgående kvalitetsansvar (K19) har ingen
  foreslått ansvarlig; K19 bygges heller ikke av noen
  løsningsretning.
- Ansvar for at kildene er *KI-klare* er ikke plassert
  hos noen aktør (kobling til element 3).
- **Indre motstrid:** samlet vurdering kap. 10.3
  hevder at «ansvarsfordelingen er på plass» – i strid
  med R1, aktøranalysens observasjon 1 og 4 og
  rolledelingsrapportens kap. 5.1/7.1. Formuleringen
  står i dokumentet beslutningstakere leser først.

### 2.3 Element 3: Rammer for KI-klare data

**Ordlyd:** «For å sikre tilgang til kvalitetssikrede
kunnskapskilder på relevante områder igangsettes arbeid
for å definere rammer for KI-klare data.»

**Dekket [DOK]:**

- Kunnskapsgrunnlaget er uvanlig solid:
  standardkatalog med modenhetsvurdering
  (teknisk-notatet kap. 1–2: CPG-on-FHIR, CQL,
  WHO SMART L1–L5, EBMonFHIR, SNOMED CT m.fl.),
  metadatastruktur-taksonomi for hele evidenskjeden
  (`metadatastrukturer-evidenskjeden.md`), gapanalyse
  på del-evnenivå (K6.1 PICO-data Delvis / K6.2
  GRADE-data Svak / K6.3 terminologibinding Fraværende
  / K6.4 maskinlesbar publisering Fraværende),
  diagnosen «strukturert metodikk, ustrukturert
  publisering», regulatoriske ytre rammer (AI Act
  art. 10, EHDS art. 78) og et konkret første grep
  (publisere GRADE-evidensprofiler som strukturerte
  data, terminologibinde PICO-elementene).

**Avvik:**

- Begrepet «KI-klare data» er ikke innført i noen
  rapport (null treff utenom oppdragsteksten).
- Ingen normativ kravliste («et KI-klart
  kunnskapsobjekt skal ha: identifikator, versjon,
  PICO-felt, utfallskoding, GRADE-felt,
  terminologibinding, lisens, opphav, format …»).
- Ingen profil-/standardbeslutning for Norge (gapene
  1, 3, 4 og 5 i teknisk-notatet kap. 8 er åpne);
  ingen avgrensning av «relevante områder»; intet
  forvaltningsregime (eier, versjonering,
  etterlevelse, finansiering – K18/K20/K21 er evner,
  ikke operasjonalisert ansvar; K20 og K21 bygges av
  ingen løsningsretning).
- Ikke koblet til *utvikling og testing* av
  KI-systemer: treningsdata, evalueringssett/
  gullstandarder, RAG-korpuskrav og lisens for KI-bruk
  er ikke analysert (AI Act art. 10-spørsmålet står
  som åpen antakelse).
- Ikke prosjektifisert: tiltakstabellen i samlet
  vurdering har ingen aktivitet «definere rammer for
  KI-klare data»; nærmeste er kunnskapsbase med FHIR
  (fase 2, systemleveranse).
- Faktagrunnlag delvis uverifisert: Hdirs PICO-API
  (parkert, 401), FHIs GRADEpro-praksis,
  Helsebibliotekets metadatamodell.
- `visualiseringer/KI-klareData.pptx` finnes, men er
  verken indeksert i `visualiseringer/index.md` eller
  referert fra noen rapport.

---

## 3. Identifiserte avvik med alvorlighetsgrad

| # | Avvik | Alvorlighet | Konsekvens ved manglende oppfølging |
|---|---|---|---|
| A1 | KI-formålet (kildene som grunnlag for utvikling/testing av KI-systemer) er fraværende i problemanalysens formålskapitler og D/R-rammeverk | **Høy** | Utredningen kan ikke vise at problemanalysen besvarer oppdragets første og styrende spørsmål; risiko for at funnene avvises som «riktig svar på feil spørsmål» |
| A2 | «Rammer for KI-klare data» er verken definert eller igangsatt som leveranse | **Høy** | Oppdragets eneste eksplisitte «igangsettes»-leveranse mangler; materialet finnes, men er usynlig for beslutningstakere |
| A3 | «Bør»-spørsmålet om produksjons- og kvalitetsansvar er sirkulert mellom fire dokumenter uten konklusjon eller utrederens vurdering | **Høy** | Beslutningstakere får ikke beslutningsgrunnlaget oppdraget ber om; veivalget kan bli tatt implisitt |
| A4 | Samlet vurdering kap. 10.3 («ansvarsfordelingen er på plass») motsier utredningens egne funn (R1, dp8, rolledeling kap. 5.1) | **Middels** | Undergraver troverdigheten til hele ansvarsanalysen i dokumentet ledelsen leser først |
| A5 | Oppdragets begrepsapparat brukes ikke («målrettede helseråd» 4 treff, «KI-klare data» 0 treff); ingen sporing oppdrag → rapportkapittel | **Middels** | Vanskelig å vise samsvar ved rapportering; begrepsglidning mot «personaliserte helseråd» uten begrunnelse |
| A6 | Tverrgående kvalitetsansvar (K19) og ansvar for KI-klare kilder er ikke plassert hos noen aktør | **Middels** | De to ansvarsområdene oppdraget faktisk innfører, forblir eierløse |
| A7 | `KI-klareData.pptx` er ikke indeksert eller tekstforankret | **Lav** | Tenkning om element 3 kan gå tapt; brudd på prosjektets egen indekseringsrutine |

**Best etterlevelse:** den deskriptive problem- og
ansvarsanalysen (element 1 og 2, «hva er»-delen) –
grundig, kildeforankret og med gjennomarbeidet
begrepsapparat. **Dårligst etterlevelse:** element 3
normativt («rammer for KI-klare data» som leveranse)
og KI-spissingen av element 1.

---

## 4. Anbefalinger

1. **Reformuler formålskapitlene** i delrapport 1 og 2
   slik at KI-formålet blir eksplisitt: kildene skal
   vurderes som grunnlag for utvikling og testing av
   KI-systemer for målrettede helseråd. Vurder samtidig
   om avgrensningen i dp1 kap. 1.3 skal justeres.
   (Lukker del av A1, A5.)
2. **Suppler problemanalysen med en
   KI-egnethetsvurdering av kildene**: lisens/
   rettigheter for KI-bruk, versjonering/sporbarhet,
   dekningsgrad per fagområde, evalueringssett for
   testing. Kan gjøres som nytt delkapittel i dp2
   eller eget notat; flere av punktene finnes allerede
   spredt ([ANT]-merket) og trenger samling og
   verifisering. (Lukker A1.)
3. **Samle element 3-materialet i én leveranse
   «Rammer for KI-klare data»**: K6.1–K6.4 som
   kravskjelett, teknisk-notatet kap. 1–2 som
   standardvalg-grunnlag, AI Act art. 10/EHDS art. 78
   som ytre rammer, K18/K20/K21 som forvaltningsregime
   – og legg inn en eksplisitt fase 1-aktivitet med
   ansvarlig aktør i samlet vurderings tiltakstabell.
   (Lukker A2, del av A6.)
4. **Etabler utrederens vurdering av
   ansvarsveivalget** i samlet vurdering (eller dp4):
   enten en begrunnet anbefaling, eller en tydelig
   fremstilling av alternativene med kriterier og
   konsekvenser – ikke bare henvisning videre. Rett
   samtidig formuleringen i samlet vurdering kap. 10.3.
   (Lukker A3, A4.)
5. **Lag en dekningsmatrise oppdragselement →
   rapportkapittel** (kan bygge på denne rapporten) og
   innfør oppdragets begreper der de hører hjemme.
   (Lukker A5.)
6. **Indekser `KI-klareData.pptx`** i
   `visualiseringer/index.md` og vurder om innholdet
   skal tekstforankres i en rapport. (Lukker A7.)
7. **Innhent den formelle oppdragsteksten** når den
   foreligger, og oppdater `kilder/oppdragstekst.md`
   og denne sjekken.

---

## 5. Forbehold

- Oppdragsteksten som er lagt til grunn er en uformell
  gjengivelse; en formell utgave kan endre ordlyd og
  dermed vurderingene, særlig for element 1
  (formuleringen «utvikling og testing») og element 3
  («igangsettes»).
- Vurderingen «utrederens vurdering mangler» (A3) kan
  være et bevisst valg: CLAUDE.md fastsetter at
  analysene skal informere menneskelige beslutninger,
  ikke ta dem. Anbefaling 4 er derfor formulert som et
  valg mellom anbefaling og beslutningsgrunnlag.
- Kartleggingen er gjort maskinelt (tekstsøk +
  gjennomlesing av relevante kapitler); enkeltpassasjer
  kan være oversett.

---

Sist oppdatert: 2026-08-14

## Kildegrunnlag

Oppdragstekst: `kilder/oppdragstekst.md`. Rapporter
gjennomgått: `dagens-verdikjede.md`,
`utfordringer-og-flaskehalser.md`, `ny-verdikjede.md`,
`aktoeranalyse.md`,
`rolledeling-sentral-helseforvaltning.md`,
`profesjonsforeninger-normering.md`,
`kapabilitetskart-verdikjeden.md`,
`losningsretninger-bred-kartlegging.md`,
`teknisk-infrastruktur-standarder.md`,
`metadatastrukturer-evidenskjeden.md`,
`arkitektur-og-komponenter.md`,
`llm-muligheter-og-risikoer.md`,
`regulatorisk-etterslep.md`,
`samlet-vurdering-kunnskapsforvaltning.md`,
`antakelsesregister.md`,
`kunnskapsinnhenting-innbyggerrettet-formidling.md`,
`kunnskapsinnhenting-styringsmodeller.md`,
`kunnskapsinnhenting-organisasjonsmodeller.md`,
`internasjonale-erfaringer.md`, `index.md` samt
`visualiseringer/index.md`.
