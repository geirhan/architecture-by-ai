# Notat: Styrings- og organiseringsmodeller for en nasjonal kunnskaps-/KI-tjeneste for helseråd

**Formål**: Kunnskapsgrunnlag med vekt på rotårsak R1 (manglende helhetlig styringsmandat) og R5 (manglende implementeringsinsentiver), sett i lys av Meld. St. 11 (2025–2026) sin føring om "kjøp i markedet". Websøk 2026-08-03; ikke uttømmende.

---

## 1. Modeller for offentlig digital infrastruktur

### 1.1 Digdirs modell for nasjonale felleskomponenter
[DOK] Syv nasjonale felleskomponenter (Altinn, ID-porten, Digital postkasse, Folkeregisteret, Kontakt- og reservasjonsregisteret, Matrikkelen, Enhetsregisteret). Digdir har med KS/Skate fått oppdrag om samordnet modell for organisering, styring og finansiering. Nåværende finansieringsmodell beskrives eksplisitt som utilstrekkelig for forventet vekst; ny modell tar tid.
**Relevans R1/R5**: [ANT] Selv veletablerte felleskomponenter sliter med varig finansierings-/styringsmodell — en nasjonal kunnskaps-/KI-tjeneste bør ha tydeligere finansieringsmodell fra start.
Kilder: https://www.digdir.no/media/637/download, https://aarsrapport2021.digdir.no/kapittel-5/kapittel-5-vurdering-av-framtidsutsikter/9.html

### 1.2 Skate – samordningsråd
[DOK] Strategisk samarbeidsråd/rådgivende organ for Digdir og digitaliseringsministeren; toppledere fra offentlige virksomheter; nytt mandat april 2020. [ANT] Ikke vedtaksorgan — svakere enn lovfestet mandat, men norsk presedens for koordinering av ~20 aktører uten én samlet etat. Et "Skate for kunnskapsforvaltning" kan være lavterskel første skritt for R1.
Kilder: https://www.digdir.no/digitalisering-og-samordning/mandat-skate/1261, https://www.digdir.no/skate/dette-er-skate/3032

### 1.3 Government as a Platform (O'Reilly)
[DOK] Staten som plattform med delte komponenter, lav deltakelsesterskel, desentralisering. Estland/X-Road: sikker datautveksling kobler 900+ organisasjoner, eliminerer duplisering. **Relevans**: [ANT] Staten orkestrerer infrastruktur (API-er, standarder, tilgangsstyring), markedet leverer tjenester — konsistent med «kjøp i markedet» operasjonalisert som plattformstyring.
Kilder: https://medium.com/digitalhks/a-working-definition-of-government-as-a-platform-1fa6ff2f8e8d, https://direct.mit.edu/itgg/article/6/1/13/9649/Government-as-a-Platform

### 1.4 Estlands e-helsesystem
[DOK] EHIS operativt siden 2008. Suksessfaktorer: klar styring, rettslig klarhet, modent økosystem, enighet om tilgangsrettigheter, standardisering. [ANT] Sentral standardisering + desentralisert datalagring = mulig mellomposisjon i scenariokorset.
Kilde: https://ceur-ws.org/Vol-2336/MMHS2018_invited.pdf

### 1.5 Data trusts / data commons
[DOK] Fiduciære forvalterordninger for datadeling; EU Data Governance Act. [ANT] Umodent, hovedsakelig konseptuelt. Relevans lav–middels.
Kilder: https://www.cigionline.org/articles/what-data-trust/, https://www.newamerica.org/insights/commons-approach-to-data-governance/

---

## 2. Offentlig-privat samarbeid om KI-tjenester

### 2.1 NHS AI Lab / AI in Health and Care Award (2020–2024)
[DOK] Evaluering (Unity Insights 2023; npj Digital Medicine 2025): behov for å forenkle anskaffelsesprosesser. **Sentralt negativt funn**: i ett prosjekt fikk fagmiljøet som tok i bruk teknologien og reduserte akuttinnleggelser ingen direkte gevinst fordi budsjettene forble uendret — manglende kobling mellom faglig gevinst og finansieringsinsentiv. Nesten eksakt parallell til R5. Også: evalueringsmetoder må følge teknologiutviklingens takt.
Kilder: https://www.england.nhs.uk/long-read/planning-and-implementing-real-world-ai-evaluations-lessons-from-the-ai-in-health-and-care-award/, https://www.nature.com/articles/s41746-025-01805-w

### 2.2 Innovasjonspartnerskap i Norge
[DOK] LUP 15 år (Oslo Economics nov. 2025); eksempler Cekom, digitale helsetjenester hjemme (Østfold). Gründere opplever offentlig marked krevende. [ANT] Mulig anskaffelsesform for «kjøp i markedet», men ingen dokumentert storskala KI-helseerfaring i Norge — kunnskapsgap.
Kilder: https://innovativeanskaffelser.no/content/uploads/2025/11/oe-2025-87-innovative-offentlige-anskaffelser-i-15-ar.pdf

### 2.3 Vendor lock-in
[DOK] Anskaffelsesforskriften § 13-4 b: enkeltleverandørunntak gjelder ikke der eksklusiviteten er skapt av oppdragsgiver selv. [DOK] **Helseplattformen (Epic, Midt-Norge)**: Riksrevisjonen — sterkt kritikkverdig planlegging/organisering/gjennomføring; mer krevende og kostbar enn forutsatt; Epic manglet kunnskap om norske forhold; tilsvarende kritikk i Finland og Danmark. Regjeringen har bestilt egen analyse. [ANT] Sterkt argument for exit-strategi, krav om interoperabilitet/portabilitet og konkurranseutsatt vedlikehold ved «kjøp i markedet».
Kilder: https://www.regjeringen.no/no/dokumenter/analyse-av-fordeler-og-ulemper-ved-helseplattformen/id3143739/, https://anbud365.no/bransjer/it-teknologi/eu-domstolens-generaladvokat-om-lock-in-effekt-i-it-kontrakter-strammes-skruen-til-for-nar-man-kan-fortsette-med-opprinnelig-leverandor/

---

## 3. Orkestreringsmodeller for økosystemer

### 3.1 DiGA (Tyskland)
[DOK] Digital Healthcare Act (2019); BfArM fast-track: sikkerhet/funksjonalitet/personvern/interoperabilitet + dokumentert positiv helseeffekt; beslutning innen 90 dager; godkjente DiGA-er automatisk refusjonsberettiget for 74+ mill. forsikrede. 374 000+ forskrivninger. Kritikk: krevende dokumentasjonskrav, kan hemme innovasjon.
**Relevans R5: svært høy** — mest modne modellen for kobling kvalitetsgodkjenning → automatisk finansiering. R1: viser at ett organ kan ha samlet godkjenningsmandat.
Kilder: https://www.nature.com/articles/s41746-024-01137-1, https://www.nature.com/articles/s41746-025-01879-6

### 3.2 NHS Apps Library → DTAC (UK)
[DOK] Apps Library/DAQ avviklet etter kritikk (ineffektivt, dårlig samsvar med NHS-prioriteringer). DTAC lansert 2020; forenklet 2024 og igjen feb. 2026 (25 % færre spørsmål, duplisering fjernet). **Advarsel mot for tung godkjenningsordning; iterativ forenkling er mønsteret.**
Kilder: https://transform.england.nhs.uk/key-tools-and-info/digital-technology-assessment-criteria-dtac/how-to-use-the-dtac/, https://htn.co.uk/2026/02/25/digital-technology-assessment-criteria-refreshed-to-create-simpler-more-trusted-pathway-for-nhs-digital-innovation/

### 3.3 NICE Evidence Standards Framework
[DOK] Tier 1–3 (3a/3b) etter funksjon; minimums- og beste praksis-krav per nivå; oppdatert for KI/adaptive algoritmer. Relevant mal for risikodifferensierte krav.
Kilde: https://www.nice.org.uk/what-nice-does/digital-health/evidence-standards-framework-esf-for-digital-health-technologies

### 3.4 API-styring – Altinn og PSD2
[DOK] Altinn REST/SOAP-API-er, modernisering. PSD2 pålegger banker å åpne API-er — økt konkurranse/innovasjon. [ANT] Lovpålagt API-åpning som modell for at private KI-leverandører kan koble seg til offentlig kunnskapsinfrastruktur på like vilkår — ikke dokumentert i helsesektor; kunnskapsgap.

---

## 4. Insentiv- og implementeringsmodeller (R5)

### 4.1 Pay-for-performance internasjonalt
[DOK] Blandet evidens: effekt ofte liten/fraværende, kortvarig, utilsiktede konsekvenser. Norge: Kvalitetsbasert finansiering (KBF) fra 2014. Teoretiske utfordringer: multi-task-problemer, altruistiske agenter. [ANT] Rene økonomiske insentiver bør ikke foreslås som eneste R5-løsning.
Kilder: https://www.michaeljournal.no/article/2017/01/06-Kvalitetsbasert-finansiering, https://www.regjeringen.no/contentassets/dc00b0a95cf349748bf94d49189b6b2f/no/sved/kunnskap.pdf

### 4.2 ISF-erfaring
[DOK] ISF fra 1997. **Negativt funn**: forsøk på økonomiske insentiver for kvalitetsregisterdekning viste ingen klar sammenheng mellom insentiv og resultat — direkte norsk advarsel for R5.
Kilde: https://www.helsedirektoratet.no/tilskudd-og-finansiering/finansiering/innsatsstyrt-finansiering-isf

### 4.3 Kvalitetsindikatorer i Norge
[DOK] OECD-modell, seks dimensjoner; 185 aktive nasjonale indikatorer (2022); prosessindikatorer måler retningslinjeetterlevelse. [ANT] Eksisterende infrastruktur som kunne utvides — men faktisk fangst av etterlevelse udokumentert; kunnskapsgap.
Kilde: https://www.helsedirektoratet.no/statistikk/kvalitetsindikatorer/om-kvalitet-og-kvalitetsindikatorer

### 4.4 Danmark: «comply or explain»
[DOK] NKR/NKA er rådgivende, ikke bindende — men avvik må begrunnes og dokumenteres i pasientjournalen. [ANT] Interessant mellomting lovpålagt/frivillig; effektmåling ikke funnet — kunnskapsgap.
Kilde: https://www.sst.dk/vidensbase/retningslinjer-og-procedurer-i-dit-arbejde/nationale-kliniske-anbefalinger-og-retningslinjer/brug-af-faglige-vejledninger

---

## 5. Styringsmandat (R1)

### 5.1 Sverige: Socialstyrelsen og «statlig styrning med kunskap»
[DOK] Nasjonale retningslinjer som prioriteringsstøtte; regionenes formaliserte kunskapsstyrningsstruktur kobler nasjonalt og regionalt nivå. Eget dokument «Statlig styrning med kunskap» (Socialstyrelsen 2025) — **svært relevant primærkilde, bør leses i sin helhet**.
Kilde: https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/dokument-webb/ovrigt/statlig-styrning-med-kunskap-2025.pdf

### 5.2 England: NICE
[DOK] Første nasjonale organ med myndighet til veiledning på tvers av alle helseteknologier. Kontrastmodell til norsk R1. [ANT] NICEs rettslige mandatgrunnlag uklart fra søket — kunnskapsgap.
Kilde: https://pmc.ncbi.nlm.nih.gov/articles/PMC7387327/

### 5.3 Norske presedenser for lovfestet koordineringsmandat
[DOK] **Samfunnssikkerhetsinstruksen** (forskrift 2017-09-01-1349 kap. VI): JD har hovedansvar for samordning innen kritiske samfunnsfunksjoner, med eskaleringsvei til regjeringen ved uenighet. [DOK] KDD samordner politikk for nasjonale minoriteter. **Mest konkrete, handlingsrettede modellen for R1 innen norsk forvaltningstradisjon**: forskriftsfestet samordningsansvar for Helsedirektoratet overfor FHI, NHN, RHF-ene og KS med eskaleringsvei til HOD — uten omorganisering.
Kilder: https://lovdata.no/dokument/INS/forskrift/2017-09-01-1349/KAPITTEL_10-2-6, https://www.regjeringen.no/no/tema/urfolk-og-minoriteter/nasjonale-minoriteter/midtspalte/ansvarsfordeling-og-samordning/id444295/

---

## Kunnskapsgap
1. Digdirs finansieringsmodell — dokument funnet, ikke lest i dybden.
2. Altinn API-styring vs. PSD2 — ingen direkte sammenligning funnet.
3. NICEs rettslige mandat — uklar; sjekk primærkilde.
4. Effektmåling av dansk «comply or explain» — ikke funnet.
5. Kvalitetsindikatorsystemets faktiske fangst av etterlevelse — udokumentert.
6. «Spørrende anskaffelser» — ikke funnet som etablert begrep.
7. DiGA pris-/refusjonsforhandling etter godkjenning — lite dekket.

## Motstridende informasjon
- P4P-forskning (svak effekt) vs. fortsatt aktiv bruk/videreutvikling av ISF/KBF i Norge — spenning som bør merkes hvis P4P-lignende mekanismer foreslås.
- Høy norsk bruk av innovative anskaffelser vs. dokumentert høy terskel for gründere — begge kan være sanne; ikke siter isolert.

## De 8 mest relevante funnene (R1/R5)
1. [R1] Samfunnssikkerhetsinstruksens samordningsmodell — mest konkrete norske presedensen.
2. [R1] Sveriges «statlig styrning med kunskap» — nordisk sammenligningscase.
3. [R5] NHS AI Award: påvist gevinst ikke implementert pga. frikoblet budsjettstruktur.
4. [R5] DiGA: kvalitetsgodkjenning → automatisk refusjon; moden mal med kjent leverandørkritikk.
5. [R1/R5] Norsk ISF-erfaring: insentiv for registerdekning uten dokumentert effekt.
6. [R1] Helseplattformen/Epic — vendor lock-in-korrektiv for «kjøp i markedet».
7. [R1/R5] NHS Apps Library nedlagt → DTAC iterativt forenklet — advarsel mot tung godkjenningsordning.
8. [R1] GaaP/Estland — plattformstyring som operasjonalisering av «kjøp i markedet».
