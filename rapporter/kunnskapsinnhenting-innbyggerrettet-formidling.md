# Kunnskapsnotat: Innbyggerrettet kunnskapsformidling og feedback-sløyfer

**Formål:** Kunnskapsgrunnlag til utredningen om ny verdikjede for kunnskapsforvaltning, med sikte på offentlig KI-tjeneste for målrettede helseråd (jf. Meld. St. 11 (2025–2026) kap. 7.2 og rotårsak R6 – manglende feedback-/målemekanismer).

**Metode:** Systematisk websøk mot internasjonale erfaringer (NHS, Danmark, Estland, Singapore), fagfellevurdert litteratur om RAG/guardrails/red-teaming, samt norske primærkilder. Alle påstander merket [DOK]/[ANT]. Søkedato 2026-08-03.

---

## 0. Norsk kontekst — hva er allerede besluttet/planlagt

**[DOK]** Helsedirektoratet har publisert en temaside om «Offentlig KI-tjeneste for helserelaterte spørsmål» med en trinnvis plan:
- Tre tjenestenivåer: (1) generell, ikke-handlingsrettet helseinformasjon, (2) individuelt tilpassede/målrettede helseråd med begrenset handlingsretning, (3) automatisert helsehjelp (krever ny regulering). Direktoratet foreslår å utforske et "mellomsteg".
- Sikkerhetsmekanismer: guardrails, løpende kvalitetsmåling og avviksoppfølging, menneskelig testing/tilsyn, transparens via kvalitetsrammeverk.
- Kildeforankring: RAG mot Helsenorge, Helsebiblioteket og FHI.
- Personalisering basert på brukerdata; bokmål, nynorsk og samisk.
- Foreslåtte tidlige lavrisiko-tjenester: KI-forenklet informasjonstilgang (NHN), målrettede kostråd, klarspråk-modul for prøvesvar/legemidler, nasjonal triageringsløsning, vaksineveileder, tilpassede rehabiliteringsprogram.
- To nye ansvarsområder foreslås: (a) nasjonalt ansvar for KI-tjenesten (kandidat: Helsedirektoratet), (b) nasjonalt ansvar for kunnskaps-/informasjonsforvaltning på tvers (kandidater: FHI eller Helsedirektoratet).
- Kritiske åpne spørsmål: menneskelig kontroll ved fullautomatiserte svar; «falsk trygghet»; press på tjenester; helseforskjeller.
Kilde: [Helsedirektoratet – Offentlig KI-tjeneste](https://www.helsedirektoratet.no/digitalisering-og-e-helse/kunstig-intelligens/offentlig-ki-tjeneste-for-helserelaterte-sporsmal)

**[DOK]** HOD har bedt Helsedirektoratet utvikle offentlig KI-tjeneste for kvalitetssikrede og persontilpassede helseråd. HELFO har allerede en chat-løsning på Helsenorge som kan utvides. Kilde: [Nyhetssak](https://www.helsedirektoratet.no/nyheter/helsedirektoratet-satser-pa-trygge-helserad-med-kunstig-intelligens)

**[DOK]** «Felles KI-plan 2024–2025» har levert kunnskapsgrunnlag om språkmodeller (mai 2024) og risikovurdering (des. 2024). Kilde: [Felles KI-plan](https://www.helsedirektoratet.no/rapporter/felles-ki-plan-for-trygg-og-effektiv-bruk-av-ki-i-helse-og-omsorgstjenesten-2024-2025)

**Vurdering:** Prosjektets premisser (digital førstelinje via Helsenorge, RAG mot godkjente kilder, trinnvis risikobasert utrulling) er allerede formulert av Helsedirektoratet selv.

---

## 1. Offentlige KI-chatboter/helseassistenter internasjonalt

### NHS (England)
- [DOK] Sammenligningsstudie (Cureus/PMC 2025): GPT-5 og Gemini 2.5 Flash vs. NHS 111 online på 10 simulerte scenarier — KI identifiserte alle akuttilfeller (NHS 111 undertriagerte ett), men overtriagerte av og til ikke-akutte; raskere, men til tider uklare anbefalinger. Behov for storskala testing før klinisk bruk. Kilde: [PMC12741861](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12741861/)
- [DOK] NHS 10-årsplan + £10 mrd. KI-satsing; KI-triageverktøy i NHS-appen; KI-notatverktøy-pilot (St George's) sparte 47 min/vakt (enkeltstående pilot). Kilder: [Global Government Forum](https://www.globalgovernmentforum.com/nhs-ai-rollout-10-year-health-plan/), [NHS England juli 2026](https://www.england.nhs.uk/2026/07/nhs-accelerates-artificial-intelligence-rollout-to-cut-waiting-times-and-improve-care-for-millions/)
- [DOK] Systematisk oversikt (npj Digital Medicine): symptomsjekkere risikoaverse (overtriagerer), nøyaktighet 11,5–90,0 %; LLM-er moderat (57,8–76,0 %) — bedre enn lekfolk (47,3–62,4 %). Kilde: [npj](https://www.nature.com/articles/s41746-025-01566-6)

### Danmark
- [DOK] Ingen dokumentert nasjonal KI-chatbot på sundhed.dk funnet — kun regionale initiativ (CAI-X/OUH, «Mit Sygehus»). Kilder: [SDU](https://www.sdu.dk/da/om-sdu/fakulteterne/teknik/nyt_fra_det_tekniske_fakultet/kunstig-intelligens-skal-forbedre-sundhedsvaesenet), [CIMT](https://cimt.dk/projekter/innovationsprojekter/chatbots)
- Kunnskapsgap: verifiser direkte mot Sundhedsdatastyrelsen før bruk som sammenligningscase.

### Estland
- [DOK] «Suve» — statsgodkjent covid-chatbot (2020), regelbasert, ikke generativ. Begrenset overføringsverdi. Kilder: [Invest in Estonia](https://investinestonia.com/estonia-created-suve-an-automated-chatbot-to-provide-trustworthy-information-during-the-covid-19-situation/), [OECD OPSI](https://oecd-opsi.org/covid-response/suve-chatbot/)

### Singapore
- [DOK] HealthHub AI (Synapxe) — beta av samtalebasert KI-assistent i nasjonal helseapp; kildeforankret mot HealthHub-innhold; fire språk; kan forklare labsvar. Kilde: [HealthHub FAQ](https://support.healthhub.sg/hc/en-us/articles/45221988949785-What-is-HealthHub-AI-Beta)
- [DOK] Pilotstudie (npj Digital Medicine mars 2026): agentic AI for personlige helseplaner i nasjonalt forebyggingsprogram; n=27; signifikant positiv brukeraksept (p<0,05), verdsatt personalisering (p=0,003). **Mest direkte sammenlignbare dokumenterte case for «målrettede helseråd»** — men liten pilot [ANT: begrenset generaliserbarhet]. Kilde: [npj 2026](https://www.nature.com/articles/s41746-026-02514-8)

---

## 2. Personalisering og samtykke/personvern

- [DOK] EHDS (2025/327, gjelder fra 26.03.2027): rett til gratis elektronisk tilgang til egne helsedata via access service; GDPR-samtykke sentralt for primærbruk. Kilder: [EY](https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds), [LoC](https://www.loc.gov/item/global-legal-monitor/2025-05-05/european-union-new-regulation-establishes-the-european-health-data-space-for-exchange-of-health-records/)
- [DOK] Sekundærbruk: HDAB-godkjenning, ikke individuelt samtykke; ubetinget opt-out-rett. Kilde: [Aridhia](https://www.aridhia.com/blog/ehds-patient-consent-and-the-expectations-on-secure-processing-environment-providers/)
- [DOK] Helsedirektoratets EHDS-konsekvensvurdering (11.04.2025) har kapitler om innbyggerrettigheter og sekundærbruk. Kilder: [Rettigheter](https://www.helsedirektoratet.no/rapporter/ehds-konsekvensvurdering--gapanalyse-pr.11.april-2025/primaerbruk-av-helseopplysninger/rettigheter-for-innbygger), [Sekundærbruk](https://www.helsedirektoratet.no/rapporter/ehds-konsekvensvurdering--gapanalyse-pr.11.april-2025/sekundaerbruk-av-helsedata)
- [DOK] Litteratur peker på svakheter ved binære opt-out-modeller; granulære brukerstyrte samtykkeplattformer foreslått. Kilder: [npj](https://www.nature.com/articles/s41746-025-02147-3), [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1386505625000899)
- **[ANT] Åpent rettslig spørsmål:** kobling mot kjernejournal/journal for personalisering = primærbruk (samtykke), mens modellforbedring på aggregerte data kan falle under EHDS-sekundærbruk med opt-out — ikke bekreftet, bør avklares juridisk.

---

## 3. Kvalitetssikring av KI-generert innbyggerinformasjon

- [DOK] RAG + programmerbare guardrails som standardtilnærming; personvernrisiko (eksponering av bakenforliggende data) vedvarende problem. Kilder: [NVIDIA](https://developer.nvidia.com/blog/develop-secure-reliable-medical-apps-with-rag-and-nvidia-nemo-guardrails/), [arXiv](https://arxiv.org/pdf/2511.11347)
- [DOK, sekundærkilder — verifiser primærstudier] 49,6 % av KI-chatbotsvar på helsespørsmål problematiske (BMJ Open-basert); Mount Sinai-studie: ChatGPT Health undertriagerte 52 % av reelle nødsituasjoner. Kilder: [The Conversation](https://theconversation.com/half-of-ai-health-answers-are-wrong-even-though-they-sound-convincing-new-study-280512), [TeleDirectMD](https://teledirectmd.com/health-guides/ai-chatbot-medical-information-safety/)
- [DOK] Red-teaming-protokoll (Scientific Reports 2026): tre pilarer (feilstratifisering, dobbeltsporet testing single/multi-turn, sårbarhetsinformert utbedring). Robust på Document Adherence (0/60 feil), 15 % feilrate på Instruction Adherence; ved multi-turn stresstest 50 % feilrate på råd-spørsmål og 40 % ved brukerdistress. **Mest metodisk overførbare funn: test med multi-turn/adversarielle scenarioer.** Kilde: [Sci Rep 2026](https://www.nature.com/articles/s41598-026-45719-3)

---

## 4. Learning health system / feedback-sløyfer (R6)

- [DOK] LHS-konsept: rutinedata + ekstern evidens → feedback-sløyfer → praksisendring nær sanntid; kvalitetsregistre som infrastruktur. Kilder: [PMC10809034](https://pmc.ncbi.nlm.nih.gov/articles/PMC10809034/), [Wiley 2025](https://onlinelibrary.wiley.com/doi/full/10.1002/lrh2.70036)
- [DOK] Eksempler: ImproveCareNow (100+ sentre, 30 000+ pasienter, internasjonalt LHS); Svenska Reumatologiregistret (pasientrapportering rett i journal); Australias nasjonale rammeverk for kvalitetsregistre.
- [DOK] WHO SMART Guidelines / DAK-implementeringserfaringer fra pilotland ([Lancet Digital Health 2021](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(21)00038-8/fulltext), [JMIR 2025](https://medinform.jmir.org/2025/1/e58858)).
- **[ANT] Sentralt funn:** Ingen kilde beskriver en dokumentert feedback-sløyfe fra **innbyggerrettet KI-chatbot-bruk** til oppdatering av normerende kunnskapsgrunnlag — umodent felt internasjonalt. Norge kan ikke kopiere en ferdig modell; den må utvikles selv.

---

## 5. Risikoer

- [DOK] Feilinformasjon: se pkt. 3. Kun 35 % stoler på ChatGPT i medisinske temaer; 63,6 % mener den ikke bør gi medisinske råd ([Express Legal Funding](https://expresslegalfunding.com/chatgpt-study/)).
- [DOK] Helsekompetanse/digital ekskludering (Norge): 1 av 3 i utvalgte innvandrergrupper har svært begrenset helsekompetanse; ~480 000 personer 60+ er «ikke-digitale» ([Hdir IS-2959](https://www.helsedirektoratet.no/rapporter/befolkningens-helsekompetanse/Befolkningens%20helsekompetanse%20-%20del%20I.pdf)).
- [DOK] Ansvar: Tysk dom (OLG Hamm, mai 2026) — virksomheten som drifter chatbot er ansvarlig for feilaktige svar. EU AI Act: objektivt ansvar mulig for defekt høyrisiko-KI; AI Liability Directive med årsakspresumsjon. Kilder: [LoC](https://www.loc.gov/item/global-legal-monitor/2026-06-09/germany-court-rules-chatbot-operators-are-liable-for-ai-hallucinations/), [Bird & Bird](https://www.twobirds.com/en/insights/2025/liability-of-healthcare-ai-providers-in-the-eu-how-to-navigate-risks-in-a-shifting-regulatory-ecosys)
- [ANT] Ingen empiri på hvordan et offentlig alternativ påvirker tillit/bruk av kommersielle chatboter — gap; bør inn i evalueringsdesign for norsk pilot.

---

## Kunnskapsgap

| Gap | Oppfølging |
|---|---|
| Dansk nasjonal KI-chatbot — ikke funnet | Henvendelse Sundhedsdatastyrelsen |
| Feedback-loop KI-bruk → kunnskapsproduksjon — ingen internasjonale eksempler | Styrker R6-funn; ev. søk mot leverandører |
| Mount Sinai/BMJ Open-tall kun via sekundærkilder | Les primærstudier før sitering |
| Primær-/sekundærbruk-skillet for personalisering | Juridisk avklaring i Hdir |
| Tillitseffekt av offentlig alternativ | Inn i pilot-evalueringsdesign |
| Estland/Singapore-overførbarhet | Bruk med forbehold (skala, teknologigenerasjon) |
