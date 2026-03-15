# Anbefaling: EHDS-implementering i Norge

## Ledersammendrag

**Anbefaling: Norge bor velge en hybridstrategi der alternativ 1 (stegvis minimum) brukes som taktisk startpunkt for a mote de forste EHDS-fristene, med alternativ 2 (akselerert helhetlig) som bindende strategisk mal, og alternativ 3 (nordisk samarbeid) som parallell samarbeidsdimensjon.**

Denne anbefalingen er forankret i en sammenstilling av seks delrapporter som dekker kunnskapsgrunnlag, problemdefinisjon, tiltaksalternativer, prinsipielle sporsmal, samfunnsokonomisk vurdering, helsepersonellkonsekvenser og arkitekturkonsekvenser.

**Nokkeltall:**
- EHDS-forordningen (EU 2025/327) tradte i kraft mars 2025. Gruppe 1-fristen er mars 2029, gruppe 2-fristen er mars 2031.
- Estimert investeringskostnad: 3-6 mrd. NOK for alternativ 1 alene, 6-12 mrd. NOK for alternativ 2. Hybridstrategien antas a ligge i omradet 5-9 mrd. NOK.
- EU anslar EUR 11 mrd. i besparelser over ti ar for hele EU. Norges andel er grovt anslatt til 1,2-2,5 mrd. NOK.
- 21 identifiserte gap fordelt pa rettslige (5), tekniske (6), organisatoriske (5) og semantiske (5) dimensjoner.
- Arkitekturkvalitet: Alternativ 2 scorer 4,2/5, alternativ 3: 2,8/5, alternativ 1: 2,0/5.

**Hovedbegrunnelse:** Rent alternativ 1 gir for stor teknisk gjeld og for lav nasjonal nytteverdi. Rent alternativ 2 har for hoy gjennomforingsrisiko og for hoye kortsiktige kostnader. En hybridstrategi henter de beste elementene fra begge: pragmatisk start med tydelig retning mot langsiktig modernisering.

**Det kritiske designprinsippet:** Gateway-laget som etableres i forste fase, ma designes eksplisitt som midlertidig infrastruktur med en bindende utfasingsplan. Dersom gateway-laget sementeres som permanent arkitektur, vil Norge akkumulere teknisk gjeld som blir stadig dyrere a handtere.

---

## Samlet vurdering av alternativene

### Alternativ 1 -- Samlet vurdering

**Stegvis minimumstilnaerming: Gateway-basert etterlevelse av EHDS-krav.**

| Perspektiv | Vurdering |
|------------|-----------|
| **Okonomi** | Investeringskostnad 3-6 mrd. NOK. Arlig merkostnad 300-600 mill. NOK for doble standarder. Lavest kortsiktig kostnad, men okende totalkostnad over tid. |
| **Helsepersonell** | Minst forstyrrende pa kort sikt. Lav nasjonal nytteverdi -- helsepersonell far ikke bedre informasjonstilgang mellom norske virksomheter. Risiko for konverteringsfeil ved grensekryssende deling. |
| **Arkitektur** | Scorer 2,0/5 pa arkitekturkvalitet. Genererer permanent teknisk gjeld med to parallelle standardverdener. Gateway er et sentralt feilpunkt med 18-24 integrasjonspunkter. |
| **Prinsipielle sporsmal** | Oppfyller minimumskravene, men utnytter ikke handlingsrommet for a styrke pasientrettigheter eller nasjonal interoperabilitet. |

**Styrker:** Lavest kortsiktig risiko. Mest gjennomforbart innenfor stramme tidsfrister. Minst endringsmotstand.

**Svakheter:** Skaper varig teknisk gjeld. Doble standarder oker driftskostnadene over tid. Begrenset nasjonal verdi utover EOS-rettslig etterlevelse. Leverandorer har ikke insentiv til a modernisere til FHIR nasjonalt.

### Alternativ 2 -- Samlet vurdering

**Akselerert helhetlig implementering: FHIR som nasjonal standard, bredere modernisering.**

| Perspektiv | Vurdering |
|------------|-----------|
| **Okonomi** | Investeringskostnad 6-12 mrd. NOK. Arlig driftskostnad 200-400 mill. NOK (konsolidert). Hoyest initialkostnad, men mest lonnsomt over 15 ar. |
| **Helsepersonell** | Storst langsiktig gevinst med bedre nasjonal informasjonstilgang. Hoyest kortsiktig endringsbelastning. Risiko for «Helseplattformen i nasjonal skala» ved darlig gjennomforing. 16 anbefalinger for a ivareta helsepersonell. |
| **Arkitektur** | Scorer 4,2/5 pa arkitekturkvalitet. Ferrest transformasjonspunkter (12-15). Eliminerer doble standarder. Skalerer best til nye datakategorier. |
| **Prinsipielle sporsmal** | Sterkest posisjon for a realisere bade EHDS-krav og nasjonale digitaliseringsambisjoner. Storst potensial for a styrke pasientrettigheter og forskningstilgang. |

**Styrker:** Best arkitekturkvalitet. Storst nasjonal nytteverdi. Samsvarer med «En innbygger -- en journal»-visjonen. Eliminerer doble standarder. Best posisjonert for fremtidige krav.

**Svakheter:** Hoy gjennomforingskompleksitet. Hoy kostnad. Hoy endringsmotstand, saerlig fra leverandorer og virksomheter. Kapasitetsbegrensninger i bade offentlig og privat sektor. Erfaringene fra Helseplattformen viser risikoen ved store systemendringer.

### Alternativ 3 -- Samlet vurdering

**Nordisk samarbeidstilnaerming: Delte komponenter og koordinering med nordiske land.**

| Perspektiv | Vurdering |
|------------|-----------|
| **Okonomi** | Tilleggskostnad 0,2-0,5 mrd. NOK for koordinering, men besparelse 10-25 % pa delte komponenter. Kostnadseffektivt supplement. |
| **Helsepersonell** | Verdi gjennom erfaringsdeling -- laere av land som innforer EHDS for Norge. Koordinert leverandordialog gir bedre EPJ-tilpasninger. |
| **Arkitektur** | Scorer 2,8/5 som selvstendig alternativ, men loser ikke nasjonale arkitektursporsmal. Reell verdi i delte terminologitjenester, testinfrastruktur og FHIR-profiler. |
| **Prinsipielle sporsmal** | Sterkere nordisk forhandlingsposisjon overfor EU ved gjennomforingsrettsakter. Koordinert tolkning av handlingsrommet. |

**Styrker:** Kostnadseffektivt. Stordriftsfordeler i leverandordialog (DIPS, CGM, Visma opererer i flere nordiske land). Erfaringsdeling reduserer implementeringsrisiko.

**Svakheter:** Ikke et selvstendig alternativ -- Norge ma uansett velge mellom gateway (alt. 1) eller FHIR-first (alt. 2) nasjonalt. Koordineringskompleksitet mellom selvstendige nasjoner. EU-land og EOS-land har ulike tidsfrister. Risiko for «laveste felles nevner».

---

## Anbefaling

### Den anbefalte hybridstrategien

Basert pa sammenstillingen av alle delrapporter anbefales folgende hybridstrategi:

**Fase 1 (2026-2029): Taktisk etterlevelse med strategisk retning**
- Etabler gateway-laget for gruppe 1-kategoriene (pasientoppsummeringer, e-resept) basert pa alternativ 1.
- Bygg pa kjernejournals eksisterende FHIR-API-er og reseptformidlerens MyHealth@EU-pilot.
- **Kritisk:** Design gateway-laget eksplisitt som midlertidig infrastruktur. Bygg det modulaert slik at det kan fases ut komponent for komponent.
- Publiser en bindende nasjonal FHIR-overgangsplan (roadmap) med konkrete milepaler.
- Krev at alle nye integrasjoner bruker FHIR fra dag en.
- Etabler digital helsemyndighet og HDAB.

**Fase 2 (2029-2031): Gradvis overgang til FHIR**
- Implementer gruppe 2-kategoriene (bilder, lab, epikriser) med FHIR-baserte grensesnitt der mulig.
- Start utfasing av gateway-konvertering for komponenter der kildene er blitt FHIR-native.
- Sett krav til EPJ-leverandorer om FHIR-stotte i anskaffelsesavtaler og kontraktsfornyelser.
- Evaluer og juster planen basert pa erfaringer fra fase 1.

**Fase 3 (2031-2035): Konsolidering til alternativ 2**
- Fullfore utfasing av nasjonale meldingsstandarder.
- Alle EPJ-leverandorer leverer FHIR-baserte API-er.
- Gateway-laget fases ut.
- Nasjonal og europeisk interoperabilitet konvergerer.

**Parallelt spor: Nordisk samarbeid**
- Etabler nordisk EHDS-koordineringsgruppe innen 2026 Q2.
- Prioriter delte terminologitjenester, testinfrastruktur og FHIR-basisprofiler.
- Koordiner leverandordialog med DIPS, CGM og Visma.
- Bruk erfaringer fra EU-land (Sverige, Danmark, Finland) som starter implementeringen for Norge.

### Begrunnelse forankret i alle analysene

**Fra det samfunnsokonomiske perspektivet:** Alternativ 2 er mest lonnsomt over 15 ar, men usikkerheten er svaert hoy. Hybridstrategien reduserer risikoen for store feilinvesteringer tidlig, samtidig som den sikrer at Norge beveger seg mot den langsiktig optimale losningen. Nordisk samarbeid gir 10-25 % besparelse pa delte komponenter.

**Fra helsepersonellperspektivet:** Hybridstrategien gir minst mulig forstyrrelse pa kort sikt (alternativ 1 for gruppe 1), men sikrer langsiktig forbedring av informasjonstilgangen (alternativ 2 som mal). Det er avgjorende at de 16 anbefalingene fra helsepersonellvurderingen folges, saerlig kravet om netto-noytral dokumentasjonsbirde og praksisnaer opplaering.

**Fra arkitekturperspektivet:** Hybridstrategien innebar en kompromissperiode med noe teknisk gjeld (gateway-laget), men unngaer den permanente gjelden ved rent alternativ 1. Det kritiske designprinsippet -- at gateway-laget er midlertidig -- er det viktigste enkeltpunktet i hele anbefalingen. Arkitekturkonsekvensanalysen viser at alternativ 2 scorer 4,2/5 mot alternativ 1s 2,0/5, noe som gir klar retning.

**Fra det prinsipielle perspektivet:** Hybridstrategien gir tid til grundig politisk behandling av de prinsipielle sporsmalen (personvern vs. datatilgjengelighet, nasjonal suverenitet, pasientrettigheter) i fase 1, samtidig som den sikrer at Norge ikke faller etter fristene. Det nasjonale handlingsrommet bor utnyttes strategisk, saerlig for a styrke opt-out-rettigheter og ivareta taushetsplikten.

### Avveininger og usikkerhet

**Avveininger:**
- Hybridstrategien er et kompromiss som ikke gir den laveste kostnaden pa kort sikt (det gjor rent alternativ 1) eller den hoyeste arkitekturkvaliteten umiddelbart (det gjor rent alternativ 2). Den gir i stedet den beste balansen mellom risiko, kostnad og langsiktig verdi.
- Det er en reell risiko for at den politiske forpliktelsen til overgang fra fase 1 til fase 2/3 svekkes over tid. Gateway-laget kan bli permanent «fordi det fungerer». Dette er den storste risikoen ved hybridstrategien.

**Usikkerhet:**
- Gjennomforingsrettsaktene fra EU-kommisjonen er ikke vedtatt. Dersom disse krever mer enn antatt, styrkes argumentet for alternativ 2. Dersom de tillater mer fleksibilitet, styrkes argumentet for alternativ 1.
- Tidspunktet for EOS-innlemmelse er uavklart. Forsinkelse gir mer forberedelsestid, men kan ogsa gi kortere implementeringstid.
- Leverandorkapasiteten er ukjent. Dersom leverandorene ikke har kapasitet, kan selv minimumstilnaermingen bli vanskelig.
- Helseplattformen/Epic representerer en saerskilt usikkerhet uavhengig av alternativ.

**Minoritetssyn:**
- *Arkitekturperspektivet* argumenterer for a ga mer direkte pa alternativ 2, fordi gateway-laget introduserer risiko og teknisk gjeld som kunne vaert unngatt. Dette perspektivet anerkjennes, men vurderes som for risikabelt gitt usikkerhetene og den korte tiden til forste frist.
- *Helsepersonellperspektivet* argumenterer for a prioritere minimal forstyrrelse (alternativ 1 uten overgangsplan), for a unnga risikoen for «Helseplattformen i nasjonal skala». Dette perspektivet anerkjennes, men vurderes som utilstrekkelig langsiktig.

---

## Kritiske suksessfaktorer

For at hybridstrategien skal lykkes, ma folgende vaere pa plass:

### 1. Politisk forpliktelse til langsiktig retning
- HOD ma forplikte seg til FHIR som nasjonal standard, ikke bare til EHDS-etterlevelse.
- Stortinget ma gi langsiktig finansieringsramme som strekker seg utover enkeltbudsjettar.
- Overgangen fra fase 1 til fase 2 ma forankres i politisk bindende vedtak (f.eks. stortingsmelding eller proposisjon), ikke kun i administrative planer.

### 2. Tydelig programorganisasjon
- Nasjonalt EHDS-program med klart mandat, budsjett og styringsstruktur, ledet av Helsedirektoratet.
- Programmet ma ha myndighet pa tvers av sektorens aktorer og beslutningsmyndighet for arkitekturvalg.
- Tydelig ansvarsfordeling mellom Helsedirektoratet (strategi, standarder), NHN (drift, infrastruktur) og andre aktorer.

### 3. Bindende FHIR-overgangsplan
- En tydelig, offentlig og bindende plan for overgang fra nasjonale meldingsstandarder til FHIR.
- Konkrete milepaler for nar gateway-laget skal fases ut per komponent.
- Krav om FHIR i alle nye anskaffelser og kontraktsfornyelser fra 2027.

### 4. Tidlig og systematisk leverandordialog
- Leverandormote innen 2026 Q3 med tydelige signaler om krav og tidsfrister.
- Saerlig dialog med Epic/Helseplattformen om hvordan Epics integrasjonsmodell skal fungere med norske FHIR-profiler.
- Koordinert nordisk leverandordialog med DIPS, CGM og Visma.

### 5. Kommunesektoren ma stettes
- Statlig finansiering av kommunenes EHDS-tilpasning i trad med prinsippet om at palagt oppgaver fullfinansieres.
- Kompetansebistand til sma kommuner.
- Koordinering med KS som kommunenes interesseorganisasjon.

### 6. Klinisk forankring gjennom hele prosessen
- Kliniske referansegrupper med representanter fra alle bererte yrkesgrupper.
- Krav om brukertesting med reelle kliniske scenarioer.
- Netto-noytral dokumentasjonsbirde som designprinsipp.
- Laerdom fra Helseplattformen ma brukes aktivt.

### 7. Kompetansebygging
- Nasjonalt FHIR-kompetanseprogram som starter senest 2027.
- Nordisk samarbeid om kompetanseutvikling.
- HL7 FHIR, EEHRxF og europeisk helseinteroperabilitet som prioriterte kompetanseomrader.

---

## Neste steg

| Nr | Handling | Ansvarlig | Frist |
|----|----------|-----------|-------|
| 1 | **Forankre hybridstrategien politisk.** Legge frem anbefaling for HOD med anmodning om prinsippvedtak om FHIR som nasjonal standard og bindende overgangsplan. | Helsedirektoratet | 2026 Q2 |
| 2 | **Etablere nasjonalt EHDS-program** med mandat, budsjett og styringsstruktur. Programmet skal dekke bade fase 1 og den langsiktige overgangen. | HOD / Helsedirektoratet | 2026 Q2 |
| 3 | **Utpeke digital helsemyndighet formelt.** Avklare ansvarsfordelingen mellom Helsedirektoratet og NHN. | HOD | 2026 Q3 |
| 4 | **Publisere nasjonal FHIR-overgangsplan (roadmap)** med konkrete milepaler, krav til leverandorer og utfasingsplan for gateway-laget. | Helsedirektoratet | 2026 Q4 |
| 5 | **Gjennomfore leverandordialog.** Innkalle DIPS, Epic, CGM, Visma og Infodoc til felles mote med tydelige signaler om krav og tidsfrister. Saerskilt dialog med Epic om Helseplattformen. | Helsedirektoratet / NHN | 2026 Q3 |
| 6 | **Etablere nordisk EHDS-koordineringsgruppe** i samarbeid med svenske, danske, finske og islandske helsemyndigheter. | Helsedirektoratet | 2026 Q2 |
| 7 | **Fremme lovproposisjon for Stortinget** med nodvendige lovendringer for EOS-innlemmelse av EHDS. | HOD | 2027 Q1 |
| 8 | **Etablere HDAB** med grunnleggende funksjonalitet, bygget pa helsedata.no/Helsedataservice-infrastrukturen. | Helsedirektoratet / FHI | 2028 Q2 |
| 9 | **Gjennomfore fullverdig samfunnsokonomisk analyse** nar gjennomforingsrettsaktene er vedtatt. | Helsedirektoratet / DFO | 2027 Q4 |
| 10 | **Etablere kliniske referansegrupper** med representanter fra Legeforeningen, NSF, Farmasoytforbundet og andre fagorganisasjoner. | Helsedirektoratet | 2026 Q3 |
| 11 | **Starte nasjonalt FHIR-kompetanseprogram** i samarbeid med HL7 Norway og nordiske partnere. | Helsedirektoratet / NHN | 2027 Q1 |
| 12 | **Etablere nasjonal testinfrastruktur** for obligatorisk testing av EHR-systemer mot EEHRxF. | NHN | 2028 Q4 |

---

## Referanser

Denne anbefalingen er basert pa folgende delrapporter fra prosjektet:

1. `rapporter/kunnskapsgrunnlag-ehds.md` -- Kunnskapsgrunnlag for EHDS-utredning
2. `rapporter/problemdefinisjon-ehds.md` -- Problemdefinisjon med gap-analyse
3. `rapporter/tiltaksalternativer-ehds.md` -- Beskrivelse av tiltaksalternativer
4. `rapporter/prinsipielle-spoersmaal-ehds.md` -- Prinsipielle sporsmal ved EHDS-innforing
5. `rapporter/samfunnsoekonomisk-vurdering-ehds.md` -- Samfunnsokonomisk vurdering
6. `rapporter/helsepersonellvurdering-ehds.md` -- Helsepersonellvurdering
7. `rapporter/arkitekturkonsekvenser-ehds.md` -- Arkitekturkonsekvensanalyse

---

*Denne anbefalingen er utarbeidet 15. mars 2026 som en sammenstilling av alle delrapporter i Helsedirektoratets arkitekturvurdering for EHDS-implementering i Norge. Anbefalingen bor revideres nar gjennomforingsrettsakter fra EU-kommisjonen vedtas, EOS-innlemmelse avklares, og mer detaljerte kostnadsestimater foreligger.*
