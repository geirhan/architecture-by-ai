# Kildeforankring: «Regulatorisk etterslep» i lys av EHDS og EU AI Act

**Utarbeidet:** 2026-05-21
**Gjelder:** Påstanden «regulatorisk etterslep» som brukes i
delrapport 4 (`ny-verdikjede.md`, kap. 2.3), delrapport 7
(`samlet-vurdering-kunnskapsforvaltning.md`, kap. 4.2) og på slide 12
(«Konsekvenser av å videreføre dagens praksis») i presentasjonen
`Presentasjoner/utfordringsbildet-forankring.pptx`.
**Formål:** Forankre påstanden i konkrete bestemmelser fra Forordning
(EU) 2025/327 (EHDS) og Forordning (EU) 2024/1689 (EU AI Act), og
markere hvor påstanden er dokumentert ([DOK]) og hvor den er en
analytisk slutning ([ANT]).

> **Sammenheng med delrapport 2:** Delrapport 2
> (`utfordringer-og-flaskehalser.md`, kap. 2.2) inneholder en merknad
> om at EHDS og EU AI Act *ikke* er direkte regulatoriske krav til
> *dagens* verdikjede, men blir bindende rammer **når** verdikjeden
> moderniseres. Dette notatet utdyper og artikkelfester den
> avgrensningen.

---

## Metodisk forbehold

EUR-Lex returnerte tomme sider ved direkte henting (trolig
JavaScript-gjengivelse). Artikkeltekst for EHDS er i hovedsak hentet
fra Europakommisjonens offisielle FAQ-dokument (DG SANTE, v1.1, sist
oppdatert 26. mars 2026) – autoritativt, men ikke rettslig bindende i
seg selv. Artikkeltekst for AI Act er hentet fra
artificialintelligenceact.eu. Selve artikkelnumrene og fristene
behandles som [DOK]; tolkninger som [ANT]. Se også kunnskapsgapene
til slutt.

---

## Kort konklusjon

Påstanden «regulatorisk etterslep» er **delvis presis** og krever to
nyanser:

1. **EHDS regulerer primært deling og tilgang til pasientdata** –
   ikke direkte produksjon av systematiske oversikter, nasjonale
   faglige retningslinjer eller innbyggerinformasjon, som er
   kjerneleddene i kunnskapsforvaltnings-verdikjeden. Etterslepet for
   disse leddene er **indirekte**: svakere datagrunnlag gir svakere
   sekundærbruk, som over tid svekker kunnskapsgrunnlaget. [ANT]
2. **Den sterkeste direkte koblingen er AI Act Art. 10**
   (datakvalitet for trening av høyrisiko-KI) sett mot dagens
   fritekstbaserte og fragmenterte helsedata (R2/R4): vil vi bruke KI
   i kunnskapsproduksjonen, krever loven strukturerte data av en
   kvalitet verdikjeden i dag ikke leverer. [ANT for koblingen, DOK
   for kravet]

Selve kravene, artiklene og fristene (august 2026 / mars 2029 / mars
2031) er dokumenterbare. **Koblingen til verdikjedens spesifikke
svakheter** (R2, R3, R4, R6) er en begrunnet analytisk slutning, ikke
en eksplisitt forordningstekst.

---

## Del 1 – EHDS (Forordning (EU) 2025/327)

EHDS har tre hoveddeler med ulike adressater (Art. 1, Recital 1)
[DOK]:

- **Kap. II** – primærbruk: pasientrettigheter og helsepersonells
  tilgang til elektronisk helseinformasjon.
- **Kap. III** – EHR-systemer: krav til journalsystemer
  (interoperabilitet, logging).
- **Kap. IV** – sekundærbruk: datainnehaveres plikt til å gjøre data
  tilgjengelig for forskning og policy via HealthData@EU.

**Avgrensning:** EHDS regulerer ikke direkte produksjon av
systematiske oversikter, faglige retningslinjer, refusjonsbeslutninger
eller innbyggerinformasjon. Disse er ikke primæradressater. [ANT]

| Bestemmelse | Hva den krever | Frist | Kobling | Markering |
|---|---|---|---|---|
| **Art. 14(1)** | Seks prioritetskategorier (pasientsammendrag, e-resept, e-ekspedering; deretter bilder, prøvesvar, utskrivningsrapporter) tilgjengelig i strukturert form | Fase 1: 26.3.2029; fase 2: 26.3.2031 | R2, R4 | DOK (krav) / ANT (kobling) |
| **Art. 15(1)** | EHR-systemer skal kunne eksportere/importere i felles format (EEHRxF); spesifikasjoner vedtas innen 26.3.2027 | 2029/2031 | R2, R4 | DOK / ANT |
| **Art. 13(4)** | Gjennomføringsakt om datakvalitet for primærbruk | Akt innen 26.3.2027 | R2, R4 | DOK / ANT |
| **Art. 25–49** | Krav til EHR-systemer (interoperabilitets- og loggkomponent, CE-merking, registrering) | Systemer på markedet etter 26.3.2029 | R2, R4 | DOK / ANT |
| **Art. 51 m.fl.** | Datainnehavere (helseforetak, kommuner, FHI, DMP) plikter å gjøre data tilgjengelig for sekundærbruk | 26.3.2029 (noen kategorier 2031) | R3, R4 | DOK / ANT |
| **Art. 78** | Datakvalitets- og nytteetikett for datasett til sekundærbruk | (følger sekundærbruk) | R4, R6 | DOK / ANT |

**Sentrale presiseringer fra FAQ [DOK]:**

- EHDS pålegger *ikke* digitalisering av papirdokumenter – rettighetene
  gjelder data som *allerede* behandles elektronisk (FAQ sp. 6).
- EHR-systemer trenger *ikke* bruke EEHRxF internt, bare kunne
  importere/eksportere i det (FAQ sp. 23).
- Sekundærbruk omfatter eksplisitt «training of AI algorithms that
  could be used in healthcare» (Art. 53(1)(e), Recital 61).

**Hva EHDS direkte vs. indirekte berører i verdikjeden:**

| Verdikjedeledd | Direkte EHDS-krav? | Artikkel |
|---|---|---|
| Primærforskning (produksjon) | Nei – kun indirekte via sekundærbruk | Art. 51, 53 |
| Systematiske oversikter (FHI) | Nei – kun tilgang til data | Art. 51, 53 |
| Nasjonale faglige retningslinjer (Hdir) | Nei – kun bedre datagrunnlag over tid | – |
| Implementering i klinisk praksis | **Ja** – krav til EHR-systemer | Art. 25–49 |
| helsenorge.no (NHN) | Delvis – pasienttilgang | Art. 3, 4, 12 |
| Refusjonsbeslutninger (DMP) | **Ja** – som datainnehaver | Art. 51, 60 |

---

## Del 2 – EU AI Act (Forordning (EU) 2024/1689)

AI Act regulerer KI-systemer, ikke all databruk. Relevant for
verdikjeden der KI tas i bruk i (1) evidenssyntese, (2)
retningslinjearbeid, (3) innbyggertjenester på helsenorge.no, eller
(4) klinisk beslutningsstøtte. Verdikjeden bruker i dag KI i begrenset
grad på disse måtene – AI Act er derfor mer relevant for fremtidige
tilstander enn dagens praksis. Det er nettopp kjernen i
«etterslep»-problematikken. [ANT]

| Bestemmelse | Hva den krever | Frist | Kobling | Markering |
|---|---|---|---|---|
| **Annex III + Art. 6** | KI som vurderer rett til helsetjenester (5a) og akuttmedisinsk triage (5d) er høyrisiko. KI-støttet litteratursøk/evidenssyntese/retningslinjeproduksjon er **ikke** listet som høyrisiko | – | – | DOK (klassifisering) |
| **Art. 9** | Kontinuerlig risikostyringssystem | 2.8.2026 | R3, R6 | DOK / ANT |
| **Art. 10** | Datakvalitet for trening: relevant, representativt, mest mulig feilfritt og komplett | 2.8.2026 | **R2, R4** (sterkeste kobling), R3 | DOK / ANT |
| **Art. 13** | Transparens og dokumentert ytelse overfor brukere | 2.8.2026 | R6, R2 | DOK / ANT |
| **Art. 16** | Leverandørplikter: kvalitetsstyring, dokumentasjon, logging, samsvarsvurdering, CE-merking | 2.8.2026 | R3, R4 | DOK / ANT |
| **Art. 72** | Post-market overvåking: aktiv, systematisk innsamling av ytelsesdata gjennom levetiden | 2.8.2026 | **R6** (direkteste kravuttrykk for feedback), R3 | DOK / ANT |

**Viktig avgrensning [ANT]:** En generisk KI-chatbot med
helseinformasjon på helsenorge.no er antakelig *ikke* høyrisiko under
Annex III – med mindre tjenesten gjør individuelle vurderinger av
rett til helsetjenester (5a). Dette avhenger av konkret
implementering (jf. kunnskapsgap 4).

---

## Del 3 – Hvor er gapet størst?

| Krav | Frist | Modenhetsgap (anslått) |
|---|---|---|
| AI Act høyrisiko-KI (Art. 9, 10, 13, 16, 72) | 2.8.2026 | Høyt – men kun der KI faktisk er tatt i bruk |
| EHDS digitale helseautoriteter etablert | 26.3.2027 | Lavt (pågår) |
| EHDS spesifikasjoner EEHRxF (Kommisjonen) | 26.3.2027 | N/A |
| EHDS EHR-systemer i EEHRxF (fase 1) | 26.3.2029 | Middels–høyt |
| EHDS datainnehavere tilgjengelig for HDAB | 26.3.2029 | Middels–høyt |
| EHDS EEHRxF (fase 2) / genetiske data | 26.3.2031 | Høyt |

- **Størst gap:** AI Act Art. 10 (datakvalitet for trening) vs.
  fritekst og fragmenterte kodeverk (R2, R4).
- **Nest størst:** EHDS Art. 14(1)/15(1) (strukturert EHR i EEHRxF)
  vs. norske journalsystemers evne til å levere seks
  prioritetskategorier i standardformat innen 2029.
- **Viktigst for verdikjeden spesifikt:** EHDS Art. 51
  (sekundærbruksplikt) for FHI som forskningsmiljø/dataholder og DMP
  som refusjonsorgan/dataholder.

---

## Del 4 – Mer presise formuleringer

**Dagens formulering (slide 12 / delrapport 7):**
> «EHDS og EU AI Act forutsetter digital modenhet som dagens
> verdikjede ikke har.»

**Variant A – faglig rapport (anbefalt for delrapport 4 og 7):**
> «EHDS (Forordning 2025/327) krever at EHR-systemer kan eksportere og
> importere strukturert pasientinformasjon i et felles europeisk
> format (EEHRxF) innen 2029 (Art. 14(1) og 15(1)), og at helseforetak
> og kommuner gjør datasett tilgjengelig for sekundærbruk (Art. 51)
> fra samme tidspunkt. EU AI Act (Forordning 2024/1689) stiller fra
> august 2026 krav om dokumentert datakvalitet (Art. 10), transparens
> (Art. 13) og post-market overvåking (Art. 72) for høyrisiko-KI i
> helse. Begge forutsetter strukturert, maskinlesbar helseinformasjon
> og systematiske feedback-mekanismer – kapabiliteter verdikjeden i dag
> ikke har på plass.»

**Variant B – presentasjon for ledelse (kortere, til slide 12):**
> «EHDS krever strukturert og delbar elektronisk helseinformasjon i
> standardformat innen 2029 (Art. 14 og 15). EU AI Act krever
> dokumentert datakvalitet og systemovervåking for KI i helse fra
> 2026 (Art. 9, 10 og 72). Dagens verdikjede – preget av fritekst og
> fragmenterte IT-systemer – oppfyller ikke disse kravene i sin
> nåværende form.»

**Variant C – med avgrensning eksplisitt (akademisk):**
> «EHDS (Art. 14–15 og 51) stiller krav om strukturert elektronisk
> helseinformasjon og tilgjengeliggjøring for sekundærbruk som gjelder
> helsetjenestens driftsdata og journalsystemer, men regulerer ikke
> direkte produksjon av systematiske oversikter, retningslinjer eller
> innbyggerinformasjon. EU AI Act (Art. 9–10, 13, 72) treffer
> verdikjeden der KI tas i bruk i evidenssyntese, klinisk
> beslutningsstøtte eller innbyggertjenester. Den digitale modninga
> begge forordningene forutsetter – strukturerte data, standardiserte
> kodeverk, systematiske feedback-mekanismer – mangler i deler av
> verdikjeden i dag.»

---

## Kunnskapsgap og forbehold

1. **EUR-Lex ikke verifisert direkte** – artikkelsitater bygger på
   Kommisjonens FAQ (DG SANTE v1.1, 26.3.2026), som er autoritativ,
   men ikke rettslig bindende.
2. **Hdirs egen gapanalyse (11.4.2025) ikke lest i fulltekst** – kun
   innholdsfortegnelsen var tilgjengelig. Den kan inneholde
   norskspesifikke vurderinger som bør innarbeides.
3. **Ingen nasjonal kartlegging** av hvilke konkrete journalsystemer
   og helseforetak som mangler hvilke kapabiliteter – påstanden om
   etterslep er ikke understøttet av nasjonal empiri på systemnivå.
4. **helsenorge.no/NHN som høyrisiko-KI ikke avklart** – avhenger av
   om kommende KI-funksjoner gjør individuelle vurderinger av
   helserettigheter (Annex III 5a).
5. **EØS-innlemmelse av EHDS pågår** – EHDS er EØS-relevant og skal
   innlemmes av EFTA-sekretariatet, men prosessen er ikke fullført
   (FAQ sp. 57). [DOK]

---

## Kilder

1. **Forordning (EU) 2025/327** – Det europeiske helsedataområdet
   (EHDS). https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng
2. **Forordning (EU) 2024/1689** – EU AI Act.
   https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
3. **Europakommisjonen, DG SANTE (2026)** – FAQ on the European
   Health Data Space, v1.1, 26. mars 2026.
4. **EU Artificial Intelligence Act – artikkelbase** –
   https://artificialintelligenceact.eu (Annex III, Art. 6, 9, 10,
   13, 16, 72).
5. **Helsedirektoratet (2025)** – EHDS konsekvensvurdering –
   gapanalyse pr. 11. april 2025 (kun innholdsfortegnelse lest).
6. **Europakommisjonen** – European Health Data Space Regulation –
   health.ec.europa.eu.

---

## Endringslogg

| Dato | Endring |
|---|---|
| 2026-05-21 | Notat opprettet. Verifisering av «regulatorisk etterslep» mot EHDS- og AI Act-artikler. Avgrensning: EHDS treffer ikke kjerneleddene (oversikter/retningslinjer/innbyggerinfo) direkte; sterkeste direkte kobling er AI Act Art. 10 vs. R2/R4. |
