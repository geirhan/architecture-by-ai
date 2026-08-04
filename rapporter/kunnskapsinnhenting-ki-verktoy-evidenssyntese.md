# Notat: KI-/LLM-baserte verktøy og tjenester for evidenssyntese og kunnskapsproduksjon

**Formål:** Grunnlagsmateriale for vurdering av mulige byggeklosser i løsningsretninger for ny verdikjede for kunnskapsforvaltning (forskning → systematiske oversikter → retningslinjer → beslutningsstøtte → innbyggerinformasjon). Adresserer særlig rotårsakene R2 (pre-digital design), R3 (kapasitet skalerer ikke med forskningsvolum) og R6 (manglende feedback-mekanismer).

**Søkedato:** 2026-08-03. Feltet endrer seg raskt — flere kilder er preprints (ikke fagfellevurdert) og leverandørmateriale. Dette er markert eksplisitt.

---

## 1. Problemforståelse fra kildematerialet

Kildene bekrefter et gjennomgående mønster: KI-/LLM-verktøy viser **lovende, men ujevn** ytelse på ulike deler av evidenssyntese-prosessen. Modenheten varierer sterkt mellom oppgavetyper — fra relativt moden (tittel/abstrakt-screening, dataekstraksjon med human-in-the-loop) til umoden og risikofylt (fulltekst-screening, uassistert klinisk rådgivning via generelle chatboter). Et gjennomgående funn på tvers av uavhengige evalueringer er at **leverandørers egne tall for nøyaktighet systematisk er høyere enn det uavhengige, fagfellevurderte studier finner** — dette gjelder både Elicit og OpenEvidence, se punkt 2 og 3. Regulatoriske myndigheter (WHO, NICE, EU) er i ferd med å etablere rammeverk, men disse er fortsatt under utvikling og gir foreløpig begrenset konkret veiledning for evidenssyntese spesifikt.

---

## 2. Verktøy for systematiske oversikter

### 2.1 Elicit (Elicit.com / Elicit Pro)
- **Hva det gjør:** KI-drevet forskningsassistent for søk, screening (inklusjon/eksklusjon), dataekstraksjon og syntese av vitenskapelig litteratur. Har et eget "Systematic Review"-produkt.
- **Modenhet:** Kommersielt, aktivt i bruk, men markedsført med et modenhetsnivå som uavhengige studier ikke fullt ut bekrefter.
- **Dokumentert ytelse [DOK]:**
  - Elicits egen evaluering hevder 94 % korrekt screening og 94–99 % ekstraksjonsnøyaktighet, samt at verktøyet kan spare opptil 80 % av tiden ([Elicit-blogg](https://elicit.com/blog/how-we-evaluated-elicit-systematic-review)).
  - En uavhengig, fagfellevurdert evaluering (Cochrane Evidence Synthesis and Methods, 2025) fant derimot at **sensitiviteten for screening var lav — gjennomsnittlig 39,5 % (25,5–69,2 %)** sammenlignet med 94,5 % for opprinnelige menneskelige reviews ([Lau et al. 2025](https://onlinelibrary.wiley.com/doi/full/10.1002/cesm.70050); [PMC-versjon](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12483133/)).
  - Hilkenmeier et al. 2025 evaluerte Elicit som semi-automatisert "andre reviewer" for dataekstraksjon — proof-of-concept, ikke full validering ([SAGE 2025](https://journals.sagepub.com/doi/10.1177/08944393251404052)).
  - BMC-studie om Elicit brukt konkret i en systematisk oversikt ([BMC Med Res Methodol 2025](https://link.springer.com/article/10.1186/s12874-025-02528-y)).
- **Vurdering:** Sprikende funn mellom leverandørens interne tall og uavhengig evaluering er betydelig — spesielt for screening-sensitivitet: lav sensitivitet betyr at relevante studier faller ut uoppdaget. Alvorlig svakhet ved bruk uten menneskelig dobbeltsjekk.
- **Relevans:** Aktuelt som supplerende verktøy i en human-in-the-loop-modell, ikke som erstatning for menneskelig screening per nå.

### 2.2 Covidence, DistillerSR, EPPI-Reviewer, Rayyan, RobotReviewer, laser AI (Evidence Prime)
- **Hva de gjør:** Etablerte plattformer for hele eller deler av systematisk oversikt-arbeidsflyt (deduplisering, screening, dataekstraksjon, risk-of-bias-vurdering, PRISMA-rapportering). Alle har i økende grad bygget inn ML/LLM-komponenter.
- **Modenhet og karakteristikk [DOK/ANT]:**
  - **Covidence**: Mest brukt, intuitivt grensesnitt, abonnementsbasert (ca. 339 USD/år for én oversikt per 2026) ([oversikt](https://blog.hifivestar.com/posts/top-systematic-review-software-2025)).
  - **DistillerSR**: For organisasjoner med mange samtidige oversikter; ML-prioritering for screening ([eldre evaluering, PMC 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7559198/)).
  - **EPPI-Reviewer**: Utviklet av EPPI-Centre (UCL), lengst forskningstradisjon på tekstmining i evidenssyntese.
  - **Rayyan**: Gratis grunnnivå, betalt nivå med PICO-ekstraksjon, "AI Analyzer/Reviewer", Auto-Extract Data og PRISMA-generator ([rayyan.ai](https://www.rayyan.ai/)); uavhengig evaluering av automatisert abstraktscreening ([PMC 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9161508/)) — eldre studie, før nyere LLM-funksjoner.
  - **RobotReviewer**: Spesialisert NLP-verktøy for automatisert risk-of-bias-vurdering. Mest grundig uavhengig validert:
    - Non-inferiority RCT: 88,8 % nøyaktighet med assistanse vs. 90,2 % i kontrollgruppe (Annals of Internal Medicine, [DOI](https://doi.org/10.7326/m22-0092)).
    - Enighet med doble uavhengige menneskelige vurderinger: ca. 72 % ([BMC 2022](https://link.springer.com/article/10.1186/s12874-022-01649-y)).
    - Sterk variasjon per bias-domene: sensitivitet 0,44–0,88, spesifisitet 0,48–0,95; best på allocation concealment (PPV 0,79), dårligst på blinding av assessorer (PPV 0,25).
    - Semi-automatisering raskere (755 vs. 824 sek); 91 % av ML-vurderingene akseptert — men **menneskelig supervisjon kreves fortsatt**.
  - **Laser AI (Evidence Prime)**: Leverandørtall: 53 % reduksjon i ekstraksjonstid, 43 % reduksjon i screening-arbeidsmengde, deduplisering 100 % spesifisitet/95 % sensitivitet ([laser.ai](https://www.laser.ai/)) — **[ANT] ikke uavhengig verifisert**.
- **Vurdering:** RobotReviewer er best validert, med klar konklusjon: egnet som beslutningsstøtte, ikke autonomt. Sammenligningsstudier ([PMC12947929](https://pmc.ncbi.nlm.nih.gov/articles/PMC12947929/), [PMC12035789](https://pmc.ncbi.nlm.nih.gov/articles/PMC12035789/)) viser at "best i test" avhenger av bruksformål.

### 2.3 LLM-basert screening generelt
- **[DOK]:**
  - Meta-analyse (JMIR 2025): sensitivitet 0,77–0,99, spesifisitet 0,91–0,98 for LLM-assistert screening — bredt spenn.
  - Modellforskjeller: GPT-4o/Llama 3.3 70B høy spesifisitet, lavere sensitivitet; Gemini 1.5 Pro/Claude 3.5 Sonnet omvendt.
  - Tittel/abstrakt-screening mest moden (sens. 99,2 %, spes. 83,6 % i én 2026-oversikt); fulltekst-screening vesentlig svakere (97,6 %/47,4 %) — mange falske positiver.
  - Preprint (nov. 2025, ikke fagfellevurdert): "nær-perfekt sensitivitet" med dual-model LLM-ensemble ([medRxiv](https://www.medrxiv.org/content/10.1101/2025.11.03.25339455.full.pdf)) — [ANT].
  - 2026 systematisk oversikt (ScienceDirect): "lovende ytelse for enkelte oppgaver, men krever forsiktig implementering" — høy risiko for falske negativer ved uassistert bruk.
- **Relevans:** LLM-screening av tittel/abstrakt kan trygt brukes som første filter/prioritering i human-in-the-loop, men ikke som eneste beslutningspunkt; fulltekst-screening bør fortsatt være hovedsakelig menneskestyrt.

### 2.4 Cochrane Evidence Pipeline og Cochranes AI-satsing
- **Evidence Pipeline:** Automatisering + "crowd verification"; Cochrane planlegger å øke andelen oversikter støttet av tjenesten ([cochrane.org](https://www.cochrane.org/about-us/news/cochrane-launches-innovative-study-assess-ai-tools-evidence-synthesis)).
- **AI-verktøy-pilot (nov. 2025):** 48 forslag, kortlistet til 2 hovedkandidater + 5 reserver. Platformstudie ferdigstilles andre halvår 2026 — **resultater foreligger ikke ennå** ([cochrane.org](https://www.cochrane.org/about-us/news/call-proposals-ai-tools-transform-evidence-synthesis)).
- **Posisjonsuttalelse:** Cochrane, Campbell, JBI og CEE felles posisjonsuttalelse om KI i evidenssyntese (2025) ([Cochrane Library](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.ED000178/full)) — **bør leses i sin helhet** som premissdokument.
- ChatGPT vs. Cochrane-forfattere på risk-of-bias: [Taneri et al. 2025](https://onlinelibrary.wiley.com/doi/full/10.1002/cesm.70044) — bør følges opp.
- LLM-pipeline for dataekstraksjon i folkehelseoversikter: [Simmons et al. 2025](https://doi.org/10.1002/cesm.70061).

---

## 3. Kunnskapsoppslagstjenester med KI

### 3.1 OpenEvidence
- Gratis (for verifisert helsepersonell) KI-søketjeneste for kliniske spørsmål med kildehenvisninger; "Consult" og "Deep Consult".
- Svært raskt voksende; Microsoft-samarbeid; verdsatt til 3,5 mrd. USD ([openevidence.com](https://www.openevidence.com/announcements/openevidence-the-fastest-growing-application-for-physicians-in-history-announces-dollar210-million-round-at-dollar35-billion-valuation)).
- **[DOK]:** Leverandør hevder 100 % på USMLE — men uavhengig pilotstudie (medRxiv nov. 2025, **preprint**) fant **34–41 % nøyaktighet** på komplekse subspesialist-scenarier; repeterbarhet 72–77 % ([medRxiv](https://www.medrxiv.org/content/10.64898/2025.11.29.25341091.full.pdf)).
- **Sentralt funn:** stort avvik mellom eksamensbenchmarks og realistisk klinisk kompleksitet — generell advarsel mot eksamensbenchmarks som mål på klinisk pålitelighet.
- **[ANT]** Uklar regulatorisk status som medisinsk utstyr i EU/Norge — bør avklares (jf. [iatrox.com](https://www.iatrox.com/blog/openevidence-chatgpt-5-medwise-ai-iatrox-uk-clinicians-dtac-nice-esf)).

### 3.2 UpToDate Expert AI (Wolters Kluwer)
- Generativ KI-beslutningsstøtte bygget på UpToDates kuraterte kunnskapsbase (ikke åpent internett), med sporbarhet til kilde og resonnement. Lansert Q4 2025; 50+ store amerikanske helseforetak; utvidet med Lexidrug ([wolterskluwer.com](https://www.wolterskluwer.com/en/news/wolters-kluwer-adds-uptodate-lexidrug-to-genai-powered-clinical-decision-support-uptodate-expert-ai)).
- **[ANT]** Ingen uavhengig fagfellevurdert evaluering funnet — kun leverandørens pressemeldinger.
- **Relevans:** Arkitekturmodellen — generativt KI-lag oppå kuratert, kvalitetssikret kunnskapsbase — er direkte overførbar til et norsk KI-lag oppå kvalitetssikrede retningslinjer. Adresserer R6 (kunnskapsbasen oppdateres kontinuerlig, KI-svaret følger med).

### 3.3 BMJ Best Practice
- **[ANT]** Ikke dekket i denne runden — historisk mer konservativ tilnærming til generativ KI; oppfølgingssøk anbefales.

### 3.4 Andre KI-kliniske søketjenester
- Praktiki, Pathway, iatroX, Medwise AI som konkurrenter i UK/EU-markedet ([iatrox.com](https://www.iatrox.com/blog/review-ai-clinical-search-praktiki-openevidence-pathway-iatrox-medwise-2025)) — [ANT] marked i rask fragmentering/konsolidering, aktører posisjonerer seg mot europeisk regulering (DTAC, NICE ESF).

### 3.5 Glass Health
- KI-basert "co-pilot": differensialdiagnoser og behandlingsplaner med kildehenvisninger + ambient scribing. Leverandøren presiserer selv at verktøyet ikke diagnostiserer — all output må verifiseres av kliniker ([glass.health](https://glass.health/developer-api)).
- **Relevans:** Designmønster — KI integrert i eksisterende arbeidsflyt fremfor separat verktøy (adresserer kjent lav bruksrate ved friksjon).

### 3.6 Klinikere/innbyggere som bruker generelle chatboter (risiko)
- **[DOK]:** 94 % av 1000+ leger (Sermo 2025) bekymret for pasienters bruk av generell KI til medisinske råd.
- Evaluering av fire chatboter: "problematiske" svar hos 21,6 % (Claude) til 43,2 % (Llama); "utrygge" svar 5–13 % ([CIDRAP](https://www.cidrap.umn.edu/misc-emerging-topics/ai-chatbots-provide-poor-answers-medical-questions-half-time-study-finds); [npj Digital Medicine](https://www.nature.com/articles/s41746-026-02428-5)).
- Positivt unntak: Googles AMIE mot 20 klinikere på 302 komplekse kasus — AMIE alene 59 % riktig diagnose vs. 34 % for uassisterte klinikere; klinikere med AMIE bedre enn med søkemotorer (Nature 2025).
- **[DOK] Regulatorisk gap:** Formålsbygde KI-helseverktøy reguleres som medisinsk utstyr; generelle plattformer (ChatGPT) faller utenfor.
- **Vurdering:** Uassistert bruk av generelle chatboter er risikabelt; klinikerassistert bruk (menneske i loop) kan gi bedre resultat enn uassistert menneske. Støtter "beslutningsstøtte, ikke erstatning"-arkitektur.

---

## 4. "Living evidence"-plattformer og automatisert forskningsovervåking

### 4.1 Epistemonikos og L·OVE
- Database for systematiske oversikter/enkeltstudier med KI-støttet søk; L·OVE ([iloveevidence.com](https://iloveevidence.com/)) varsler daglig om nye artikler og oppdaterer evidensgrunnlag kontinuerlig. Etablert, i drift, brukt av WHO under covid-19.
- Mekanismer [DOK]: kontinuerlig databasesøk med push-varsling, RCT-klassifiserere, tekstmining, automatisk fulltekst-henting.
- **Relevans:** Trolig **det mest direkte relevante byggeklossmønsteret for R6** — automatisert kontinuerlig overvåking av ny forskning.

### 4.2 Living guidelines / living systematic reviews
- Scoping review (Wiley 2026) om KI/automatisering i living guidelines ([Ismaila et al.](https://onlinelibrary.wiley.com/doi/10.1002/gin2.70079)) — bør leses i dybden.
- JMIR 2026: "Living Evidence Synthesis Using AI" som formell metodikk v1 ([JMIR](https://www.jmir.org/2026/1/e76130)) — nytt/umodent.
- **[DOK] Kjent begrensning:** automatiseringsskjevhet ("automation bias") og mangel på ekte semantisk forståelse ([Springer 2025](https://link.springer.com/article/10.1186/s13643-025-02842-y)).

### 4.3 Trip Database
- **[ANT]** Ikke funnet i dette søket — bør følges opp.

---

## 5. Dokumentert evidens for kvalitet/tidsbesparelse — samlet

### 5.1 Tidsbesparelse [DOK, sprikende kilder — flere preprints]
- Generelt anslag: 50–75 % reduksjon i aktiv screening-/ekstraksjonstid.
- AutoLit: 50 % tidsbesparelse i abstraktscreening, 70–80 % i kvalitativ ekstraksjon ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12552804/)).
- Storskala-eksempel: 9 132 artikler prosessert på 20 timer vs. estimert 385 menneske-timer (19,3x) — kilde ikke fullt identifisert, bør verifiseres.
- Case: 334 personetimer spart totalt over screening/ekstraksjon/utkast ([npj Digital Medicine](https://www.nature.com/articles/s41746-025-01840-7)).
- Pilot: menneske-KI-samarbeid ga 71,4 % bedre recall og 44,2 % kortere screeningtid; ekstraksjon 23,5 % høyere nøyaktighet, 63,4 % tidsreduksjon.
- **[ANT]:** Ingen samlet fagfellevurdert meta-analyse av tidsbesparelse finnes — kunnskapsgap.

### 5.2 GRADE-vurdering med LLM
- **[ANT] Vesentlig kunnskapsgap:** Ingen dokumentert forskning funnet spesifikt på LLM-automatisering av GRADE-vurdering. Bør følges opp mot GRADE Working Group/GRADEpro.
- **[ANT] Presisering (2026-08-04):** Kunnskapshullet skyldes trolig delvis et strukturelt forhold, ikke bare manglende forskningsinteresse: GRADE-vurderinger publiseres i dag som prosa/PDF over hele feltet (også internasjonalt), slik at det knapt finnes offentlige, strukturerte GRADE-data å trene eller evaluere modeller mot. Se [metadatastrukturer-evidenskjeden.md](metadatastrukturer-evidenskjeden.md) kap. 4–5 for kildegrunnlag.

### 5.3 Utkastskriving
- Kun indirekte dokumentert; bør følges opp spesifikt for retningslinjetekst og innbyggerinformasjon.

### 5.4 Kjente begrensninger — oppsummert
1. Sprik leverandørtall vs. uavhengig evaluering (Elicit: 94 % vs. 39,5 %; OpenEvidence: 100 % USMLE vs. 34–41 %).
2. Fulltekst-screening og komplekse kliniske spørsmål systematisk svakere.
3. **Falske negativer** er mest alvorlig — feilen er usynlig for bruker.
4. Domenevariasjon gjør "ett samlet nøyaktighetstall" misvisende.
5. Repeterbarhet er eget problem (72–77 % konkordans ved gjentatt spørring).

---

## 6. Hva helsemyndigheter sier om LLM i kunnskapsproduksjon

### 6.1 WHO
- "Ethics and governance of AI for health: guidance on large multi-modal models" ([who.int](https://www.who.int/publications/i/item/9789240084759)) — risiko, etiske prinsipper og styringstiltak for LMM i helse. [ANT] Dato/versjonsstatus bør verifiseres.

### 6.2 NICE
- Posisjonsuttalelse "Use of AI in evidence generation" ([nice.org.uk](https://www.nice.org.uk/corporate/ecd11/resources/use-of-ai-in-evidence-generation-nice-position-statement-pdf-40464268944325)): transparens, streng validering, menneskelig tilsyn. Viser til Cochranes kommende veiledning og GIN-arbeidsgruppe.

### 6.3 FDA
- Utkast til KI-veiledning (jan. 2025), endelig forventet Q2 2026, i tråd med felles FDA–EMA-prinsipper ([intuitionlabs.ai](https://intuitionlabs.ai/articles/fda-ai-drug-development-guidance)). [ANT] Rettet mot legemiddelregulering — indirekte relevans.

### 6.4 EU AI Act
- KI for diagnose, klinisk beslutningsstøtte, behandlingsanbefaling, triagering klassifiseres som **høyrisiko**. Kjerneforpliktelser gjelder fullt fra **august 2026** ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/article/6/); [Frontiers 2026](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1808373/full)).
- **Uklart:** om evidenssyntese-verktøy (screening-støtte for retningslinjeutvikling, ikke pasientrettet) faller i høyrisikokategorien — bør avklares juridisk.

---

## 7. Kunnskapsgap og oppfølging

| Gap | Beskrivelse | Oppfølging |
|---|---|---|
| GRADE + LLM | Ingen dokumentert forskning funnet | Presise søk; kontakt GRADE Working Group |
| Cochrane-pilotresultater | Ferdig 2. halvår 2026 | Følg opp høsten/vinteren 2026 |
| BMJ Best Practice KI | Ikke undersøkt | Dedikert søk |
| Trip Database KI | Ikke funnet | Dedikert søk |
| Laser AI-tall | Ikke uavhengig verifisert | Sjekk laser.ai/publications |
| Norsk/nordisk kontekst | Ingen treff om norske aktørers bruk | Intern kartlegging; Helsebiblioteket |
| Konsolidert tidsbesparelse-metaanalyse | Finnes ikke | Avvent Cochrane/JBI-veiledning |
| WHO-veiledningens dato/status | Usikker | Verifiser mot who.int |
| AI Act-klassifisering av syntese-verktøy | Uklar | Juridisk avklaring |

## 8. Motstridende informasjon
1. **Elicit:** leverandør 94 % vs. uavhengig 39,5 % sensitivitet — klareste motsigelsen.
2. **OpenEvidence:** USMLE 100 % vs. 34–41 % på komplekse scenarier.
3. **RobotReviewer:** 88,8 % nøyaktighet vs. 72 % enighet — ulike studiedesign, må ikke sammenstilles ukritisk.
