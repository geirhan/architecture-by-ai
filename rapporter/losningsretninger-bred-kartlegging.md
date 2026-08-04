# Løsningsretninger for ny kunnskapsforvaltning — bred kartlegging

**Status:** Utforskende. Notatet er et syntetisert
kunnskapsgrunnlag fra fem parallelle kunnskapsinnhentinger
gjennomført 2026-08-03, og foregriper ikke beslutninger.
Det skal brukes til å åpne løsningsrommet før alternativer
velges og utdypes — ikke som beslutningsgrunnlag.

**Underlag:** Bygger på fem underlagsnotater i `rapporter/`:

1. [Internasjonale organisasjons- og prosessmodeller](kunnskapsinnhenting-organisasjonsmodeller.md)
2. [KI-/LLM-verktøy for evidenssyntese](kunnskapsinnhenting-ki-verktoy-evidenssyntese.md)
3. [Teknisk infrastruktur, standarder og datamodeller](teknisk-infrastruktur-standarder.md)
4. [Styrings- og organiseringsmodeller](kunnskapsinnhenting-styringsmodeller.md)
5. [Innbyggerrettet formidling og feedback-sløyfer](kunnskapsinnhenting-innbyggerrettet-formidling.md)

Alle enkeltfunn med [DOK]/[ANT]-merking og kildelenker står i
underlagsnotatene. Dette notatet refererer, det gjentar ikke
kildeapparatet.

**Forhold til delrapport 4:** Delrapport 4 skisserer fire
alternativer (nullalternativ, organisatorisk modernisering,
moderat KI-støtte, ambisiøs KI-pipeline). Kartleggingen her er
bevisst bredere: den identifiserer *retninger og byggeklosser*
som kan kombineres på tvers av delrapport 4s alternativer, og
som kan brukes til å stressteste om alternativbredden er stor
nok (jf. utredningsinstruksens krav om bredde).

---

## 1. Ledersammendrag

Kartleggingen identifiserer **ti løsningsretninger** i fire
grupper (organisering, teknologi/metodikk, styring/insentiver,
innbyggerrettet tjeneste). Tre tverrgående funn preger hele
materialet:

1. **Ingen enkeltretning dekker alle rotårsakene.** De mest
   lovende kombinasjonene kobler en metodisk/teknisk retning
   (f.eks. living guidelines + strukturert format) med en
   styringsretning (f.eks. forskriftsfestet samordningsmandat).
   Dette bekrefter konklusjonen i delrapport 2 kap. 9.5 om at
   tekniske valg må kombineres med organisatorisk-politiske
   tiltak.
2. **Leverandørpåstander om KI-ytelse spriker systematisk fra
   uavhengige evalueringer.** Dokumenterte eksempler: Elicit
   (94 % hevdet screening-treffsikkerhet mot 39,5 % målt
   sensitivitet i uavhengig studie) og OpenEvidence (100 % på
   legeeksamen mot 34–41 % på komplekse kliniske scenarier).
   Enhver løsningsretning som bygger på KI-verktøy må derfor
   forutsette uavhengig validering og human-in-the-loop.
3. **Bærekraftig finansiering og mandat er den vanligste
   dødsårsaken internasjonalt** — ikke teknologi. Australias
   living guidelines-taskforce mistet finansieringen i 2023 til
   tross for suksess; USAs nasjonale retningslinjedatabase ble
   nedlagt i 2018 da bevilgningen forsvant; NHS Apps Library ble
   skrotet som for tung. Løsningsretninger bør derfor vurderes
   like mye på institusjonell robusthet som på teknisk innhold.

---

## 2. Løsningsretningene

### Gruppe A: Organisering av kunnskapsproduksjonen

#### A1. Living guidelines med strukturert publisering

Kontinuerlig oppdatering på anbefalingsnivå i strukturert,
maskinlesbart format (MAGICapp-modellen), med hurtigspor for
praksisendrende enkeltfunn (BMJ Rapid Recommendations, mål 90
dager). Best dokumenterte internasjonale svar på R3 (kapasitet)
og R2 (pre-digital design). Dokumentert forbehold: modellen
endrer *hvordan* ressursene brukes, den reduserer dem ikke, og
den er sårbar for finansieringsbortfall (ALEC/Australia).
MAGIC-stiftelsen har base i Oslo — norsk samarbeidsmulighet som
bør avklares. *Akser: KI-drevet (delvis), kontinuerlig
oppdatering. Rotårsaker: R2, R3, delvis R4.*

#### A2. Systematisk internasjonal gjenbruk (adopter–adapter–utvikle)

GRADE-ADOLOPMENT: eksplisitt, anbefaling-for-anbefaling
vurdering av om internasjonale retningslinjer (NICE, WHO, SIGN,
nordiske) kan adopteres direkte, adapteres eller må utvikles
nasjonalt. Metodisk moden (GRADE guidance 39, 2024). Reduserer
de novo-produksjon betydelig; mer transparent enn dagens
uformelle «vi ser til Sverige»-praksis. *Akser: kontinuerlig/
behovsstyrt nøytral. Rotårsak: R3.*

#### A3. Sentral metodestøtte med distribuert faglig eierskap

Nederlandsk modell (Kennisinstituut): en permanent finansiert
enhet leverer søk, GRADE-vurdering og skrivestøtte, mens
fagmiljøene eier og autoriserer innholdet. Alternativ variant:
amerikansk bestiller–utfører-modell (AHRQ/EPC) der staten
bestiller oversikter fra akademiske miljøer på kontrakt.
Negative kontraster er dokumentert: ren føderasjon uten sentral
støtte (Tyskland/AWMF, ujevn kvalitet) og ukoordinert
finansiering (Canada, industriavhengighet). *Akser:
sammenhengende. Rotårsaker: R1 (delvis), R3.*

#### A4. Redusert produktbredde per produkt

Dansk presedens (NKR→NKA): bevisst nedskalering fra brede
retningslinjer til smalere, avgrensede anbefalinger for å holde
tritt med kapasiteten. Lavterskel organisatorisk grep som kan
kombineres med alle andre retninger. *Rotårsak: R3.*

### Gruppe B: Teknologi og metodikk

#### B1. KI-støttet evidenssyntese med human-in-the-loop

LLM-screening av tittel/abstrakt som første filter (moden,
dokumentert sensitivitet opp mot 99 % i beste studier),
KI-assistert dataekstraksjon og risk-of-bias-vurdering
(RobotReviewer best validert — konklusjon: beslutningsstøtte,
ikke autonomi). Dokumenterte tidsbesparelser på 50–75 % i
enkeltstudier, men ingen samlet metaanalyse. Fulltekst-screening
og GRADE-vurdering er umodne. Cochranes plattformstudie av
KI-verktøy ferdigstilles andre halvår 2026 og bør avventes/
følges. *Akser: KI-drevet. Rotårsaker: R2, R3.*

#### B2. Maskinlesbar kunnskapsinfrastruktur

CPG-on-FHIR, CQL, WHO SMART Guidelines L1–L5, CDS Hooks —
standarder for å representere retningslinjer som beregnbart
innhold. Alle er reelle HL7/WHO-standarder, men i tidlig/
pilotfase internasjonalt, og ingen dokumentert norsk bruk er
funnet. Norsk terminologigrunnlag (SNOMED CT i etablert
forvaltning, lenkestrategi til ICD-10/ICPC-2) er en eksisterende
byggekloss. EHDS-koblingen til kunnskapsproduktene er svak/
indirekte (bekrefter `regulatorisk-etterslep.md`). *Akser:
sammenhengende, KI-drevet (muliggjør). Rotårsaker: R2, R4.*

*Tillegg 2026-08-04:* Oppfølgende kartlegging
([metadatastrukturer-evidenskjeden.md](metadatastrukturer-evidenskjeden.md))
viser at startpunktet for B2 er bedre enn først lagt til grunn:
Helsedirektoratets publiseringsmodell har allerede PICO som
innholdstype med åpent API, og GRADE-metodikken er etablert —
gapet er at evidenskjeden (PICO → utfall → GRADE) publiseres som
prosa/PDF, ikke som terminologibundne data. Dette gjelder hele
feltet internasjonalt, ikke bare Norge.

#### B3. Generativt KI-lag oppå kuratert kunnskapsbase

UpToDate Expert AI-mønsteret: LLM-svar generert utelukkende fra
en kvalitetssikret, kontinuerlig oppdatert kunnskapsbase, med
sporbarhet til kilde og resonnement. Arkitektonisk direkte
overførbart til et norsk KI-lag oppå kvalitetssikrede
retningslinjer/Helsebiblioteket. Merk: ingen uavhengig
evaluering av UpToDate-løsningen funnet, og DFD-rapporten «Fra
ord til økosystem» (sep. 2025) sier det er for tidlig å avgjøre
om RAG+LLM er modent for norsk helsetjeneste. *Akser: KI-drevet,
kontinuerlig. Rotårsaker: R2, R6 (delvis).*

#### B4. Automatisert evidensovervåking («living evidence»)

Kontinuerlig overvåking av ny forskning med push-varsling til
retningslinjeeiere (Epistemonikos/L·OVE-mønsteret; i drift
internasjonalt, brukt av WHO). Trolig den mest modne enkelt-
byggeklossen for R6-siden «fange opp ny evidens i tide», og en
forutsetning for A1. *Akser: kontinuerlig oppdatering.
Rotårsaker: R3, R6.*

### Gruppe C: Styring og insentiver

#### C1. Forskriftsfestet samordningsmandat

Norsk presedens: Samfunnssikkerhetsinstruksens modell (kap. VI)
— ett organ gis forskriftsfestet samordningsansvar overfor
øvrige aktører, med definert eskaleringsvei ved uenighet, uten
omorganisering. Mest konkrete og handlingsrettede R1-retningen
innenfor norsk forvaltningstradisjon. Mykere variant: et
«Skate for kunnskapsforvaltning» (rådgivende samordningsråd).
Nordisk sammenligningscase: Sveriges formaliserte «statlig
styrning med kunskap» (Socialstyrelsen 2025 — primærkilde bør
leses). *Akser: sammenhengende, forpliktende. Rotårsak: R1.*

#### C2. Godkjenningsordning som kobler kvalitet til finansiering

DiGA-modellen (Tyskland): myndighetsgodkjenning av digitale
helseløsninger gir automatisk refusjonsrett — mest modne malen
for å koble kvalitetskrav til insentiver i et leverandørmarked.
Dokumentert motstykke: NHS Apps Library ble nedlagt som for
tung, og etterfølgeren DTAC er forenklet iterativt (2020→2026).
Relevant for orkestrering av tredjeparts kunnskaps-/KI-tjenester
i et økosystem (jf. scenariokorset S3 vs. S4). *Akser:
forpliktende. Rotårsaker: R5, R1 (delvis).*

#### C3. Forpliktelsesmekanismer uten lovpålegg

Dansk «comply or explain»: retningslinjer er rådgivende, men
avvik skal begrunnes i journal. Mellomting mellom frivillig og
lovpålagt; effekt udokumentert. Advarsel fra empirien: rene
økonomiske insentiver har svak dokumentert effekt internasjonalt
(P4P) og i Norge (ISF-forsøket med kvalitetsregisterdekning
viste ingen målbar sammenheng). NHS AI Award dokumenterte at
påvist gevinst ikke ble implementert fordi budsjettstrukturen
ikke koblet gevinst til fagmiljøet — en nesten eksakt
R5-parallell. *Akser: forpliktende (gradvis). Rotårsak: R5.*

#### C4. Plattformstyring ved kjøp i markedet

Government-as-a-Platform (Estland/X-Road som forbilde): staten
definerer og eier infrastrukturen (API-er, standarder,
tilgangsstyring, godkjenning), markedet leverer tjenester på
toppen. Operasjonaliserer Meld. St. 11s «kjøp i markedet» uten å
gjenta Helseplattformen/Epic-erfaringen (Riksrevisjonens
kritikk; vendor lock-in): krav om interoperabilitet,
portabilitet og exit-strategi må inn i anskaffelsen. *Akser:
sammenhengende. Rotårsaker: R1, R4; risikoreduksjon for S2
(plattformavhengighet).*

### Gruppe D: Innbyggerrettet tjeneste og feedback

#### D1. Trinnvis offentlig KI-helsetjeneste med kildeforankring

Helsedirektoratets egen skisserte retning (temaside + oppdrag
fra HOD): tre tjenestenivåer fra generell informasjon via
målrettede råd til automatisert helsehjelp, RAG mot Helsenorge/
Helsebiblioteket/FHI, guardrails og løpende kvalitetsmåling.
Internasjonalt sammenligningsgrunnlag: Singapore HealthHub AI
(nærmeste dokumenterte case for «målrettede helseråd», men liten
pilot, n=27) og NHS' KI-triagesatsing. Dokumentert
sikkerhetskrav fra forskningen: multi-turn/adversariell testing
(feilrater opp mot 50 % i flerturssamtaler ved brukerdistress,
mot 0–15 % i enkeltspørsmål). Juridisk må skillet primærbruk
(personalisering mot journaldata — samtykke) og sekundærbruk
(modellforbedring — EHDS/opt-out) avklares. *Akser: KI-drevet,
sammenhengende. Rotårsaker: R2; formålsbærende for hele kjeden.*

#### D2. Feedback-sløyfer fra bruk til kunnskapsproduksjon

Learning health system-mønsteret: kvalitetsregistre,
pasientrapportering og bruksdata mates tilbake til
kunnskapsproduksjonen (ImproveCareNow, svenske registre).
Viktig funn: ingen dokumentert internasjonal modell finnes for
sløyfen «innbygger-chatbot-bruk → oppdatert kunnskapsgrunnlag» —
feltet er umodent globalt, ikke bare i Norge. Norge kan altså
ikke kopiere en ferdig modell for denne delen; den må utvikles,
men eksisterende norsk infrastruktur (kvalitetsregistre,
kvalitetsindikatorsystemet med 185 indikatorer) er mulige
startpunkter. *Akser: kontinuerlig oppdatering. Rotårsak: R6.*

---

## 3. Dekningsmatrise mot rotårsakene

| Retning | R1 | R2 | R3 | R4 | R5 | R6 |
| --- | :-: | :-: | :-: | :-: | :-: | :-: |
| A1 Living guidelines | | ● | ● | ○ | | ○ |
| A2 Internasjonal gjenbruk | | | ● | | | |
| A3 Sentral metodestøtte | ○ | | ● | | | |
| A4 Redusert produktbredde | | | ● | | | |
| B1 KI-støttet evidenssyntese | | ● | ● | | | |
| B2 Maskinlesbar infrastruktur | | ● | | ● | | |
| B3 KI-lag på kuratert base | | ● | | | | ○ |
| B4 Automatisert evidensovervåking | | | ● | | | ● |
| C1 Samordningsmandat | ● | | | ○ | | |
| C2 Godkjenning↔finansiering | ○ | | | | ● | |
| C3 Forpliktelsesmekanismer | | | | | ● | |
| C4 Plattformstyring | ● | | | ● | | |
| D1 Offentlig KI-tjeneste | | ● | | | | |
| D2 Feedback-sløyfer | | | | | ○ | ● |

● = adresserer direkte, ○ = delvis/indirekte. [ANT] Matrisen er
utrederens sammenstilling av funnene i underlagsnotatene.

Lesningen bekrefter aksens funksjon som sjekkliste (delrapport 2
kap. 9.7): en helhetlig løsning trenger minst én retning fra
hver gruppe. Gruppene A/B uten C gjentar det internasjonale
mønsteret «teknisk suksess, institusjonell død»; C uten A/B
adresserer ikke kapasitets- og formatproblemene.

## 4. Hva kartleggingen betyr for delrapport 4

[ANT] Tre observasjoner til bruk ved neste revisjon av
alternativene:

1. **Alternativbredden kan utvides med en «gjenbruksakse».**
   Ingen av dagens fire alternativer inneholder systematisk
   internasjonal gjenbruk (A2) — en retning med lav kostnad og
   direkte R3-effekt som kan legges inn i alle alternativer.
2. **Styringsretningene (C1–C4) er underspesifisert i dagens
   alternativer.** Delrapport 4s governance-kapittel kan
   konkretiseres med de dokumenterte modellene (samordnings-
   mandat, DiGA-lignende godkjenning, plattformstyring).
3. **Alternativ 3 (ambisiøs KI-pipeline) bør stressterstes mot
   valideringsfunnene.** Sprikene mellom leverandørtall og
   uavhengige evalueringer (Elicit, OpenEvidence) og de umodne
   leddene (fulltekst-screening, GRADE, feedback-sløyfen) tilsier
   at pipeline-ambisjonen må bygges rundt human-in-the-loop og
   uavhengig validering i alle ledd.

## 5. Viktigste kunnskapsgap på tvers

Fullstendige gap-lister står i underlagsnotatene. De viktigste
på tvers:

1. Norges forhold til MAGIC-stiftelsen (Oslo) — bør avklares
   direkte (mulig lavthengende samarbeid).
2. Cochranes KI-plattformstudie — resultater ventes andre
   halvår 2026; sentrale valg om B1 bør ikke låses før disse
   foreligger.
3. Juridisk klassifisering under EU AI Act/MDR: (a) om
   evidenssyntese-verktøy (ikke pasientrettet) er høyrisiko,
   (b) grensen generisk kunnskapsformidling vs. pasientspesifikk
   beslutningsstøtte (MDCG 2019-11: menneske i loopen fjerner
   ikke MDR-plikt), (c) primær-/sekundærbruksskillet for
   personalisering i D1.
4. Ingen samlet, fagfellevurdert metaanalyse av tidsbesparelse
   ved KI-støttet evidenssyntese — tallgrunnlag for
   kost–nytte-analyse mangler fortsatt.
5. Effektdokumentasjon for forpliktelsesmekanismer (dansk
   «comply or explain», kvalitetsindikatorsystemets faktiske
   fangst av etterlevelse) mangler.

---

Sist oppdatert: 2026-08-03
