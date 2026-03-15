# Problemdefinisjon: EHDS og digitalisering av norsk helsesektor

## Sammendrag

Norge står overfor en omfattende tilpasning til EHDS-forordningen (EU 2025/327). Det faktiske problemet er ikke bare at Norge mangler tekniske systemer – det er at norsk helsesektor har utviklet seg organisk over flere tiår med nasjonale standarder, fragmentert ansvarsfordeling og ulike juridiske rammer som ikke er kompatible med de felleseuropeiske kravene EHDS stiller. Problemet har fire dimensjoner: rettslige gap, tekniske gap, organisatoriske gap og semantiske gap. Disse forsterker hverandre og må løses koordinert innenfor stramme tidsfrister.

Målet er å gjøre Norge i stand til å dele helseopplysninger sikkert og effektivt med resten av EU/EØS, samtidig som vi styrker nasjonal datakvalitet, pasientrettigheter og grunnlaget for forskning og innovasjon.

---

## Det faktiske problemet

Problemet handler i bunn og grunn om at norsk helsesektor ikke er i stand til å oppfylle de kravene EHDS stiller til deling av helsedata – verken nasjonalt på tvers av virksomheter eller internasjonalt på tvers av landegrenser. Dette er ikke et enkeltstående teknisk problem, men et sammensatt strukturelt problem med flere grunnårsaker.

**Grunnårsak 1: Historisk nasjonal utvikling uten europeisk harmonisering.** Norske e-helseløsninger er utviklet over flere tiår med nasjonale meldingsstandarder, nasjonale kodeverk og nasjonale arkitekturvalg. Disse fungerer internt, men er ikke kompatible med det europeiske utvekslingsformatet (EEHRxF) som EHDS krever (kilde: Helsedirektoratets gapanalyse, april 2025).

**Grunnårsak 2: Fragmentert informasjonslandskap.** Helseopplysninger befinner seg i mange ulike systemer med ulike formater, ulike personidentifiserende data og ulike tilgangskontrollmekanismer. Sammenstilling av informasjon er en kjent utfordring, både innenfor og på tvers av virksomheter (kilde: Helsedirektoratets konsekvensvurdering).

**Grunnårsak 3: Lovverk som ikke er tilpasset grensekryssende deling.** Gjeldende norsk helselovgivning (pasientjournalloven, helseregisterloven, pasient- og brukerrettighetsloven) er ikke harmonisert med EHDS-kravene til pasientrettigheter, sekundærbruk og grensekryssende datautveksling (kilde: EØS-notatbasen, regjeringen.no).

**Grunnårsak 4: Manglende forvaltningsstrukturer.** EHDS krever nye nasjonale organer og roller (digital helsemyndighet, HDAB) som ikke finnes i dagens forvaltningsstruktur. Eksisterende ansvarsfordeling mellom Helsedirektoratet, NHN og andre aktører er ikke tilpasset de forpliktelsene forordningen pålegger (kilde: EU 2025/327, Helsedirektoratet).

---

### Rettslige gap

Norge har et velfungerende helserettslig rammeverk, men det er utviklet for nasjonale forhold og har flere gap i forhold til EHDS:

1. **Manglende hjemmel for grensekryssende deling av helseopplysninger.** Dagens lovverk regulerer primært nasjonal utveksling. EHDS krever at pasientopplysninger kan deles med helsepersonell i andre EU/EØS-land via MyHealth@EU. Dette krever nye rettslige hjemler (kilde: EØS-notatbasen).

2. **Innbyggernes rettigheter er ikke fullt harmonisert.** EHDS gir innbyggere rettigheter som delvis avviker fra gjeldende norsk rett, herunder:
   - Rett til å laste ned egne helseopplysninger i europeisk utvekslingsformat
   - Rett til tilgangsbegrensning overfor helsepersonell (med visse unntak)
   - Rett til å reservere seg mot sekundærbruk (opt-out)
   - Det er uavklart om borgere vil få rett til å reservere seg mot deling via MyHealth@EU (kilde: Helsedirektoratets gapanalyse).

3. **Sekundærbruk krever nytt rettslig rammeverk.** EHDS etablerer en egen tilgangsmodell for sekundærbruk med datatillatelser, sikre analyserom og HDAB som tilgangsportvokter. Norsk lov har i dag andre mekanismer for forskningstilgang (f.eks. gjennom REK, Datatilsynet og helsedata.no), og disse må tilpasses (kilde: Helsedirektoratet, helsedata.no).

4. **EØS-innlemmelse med artikkel 103-forbehold.** Forordningen krever Stortingets godkjenning fordi den fordrer lovendringer og har budsjettmessige konsekvenser. Tidspunktet for innlemmelse er uavklart og påvirker alle frister (kilde: regjeringen.no).

5. **Forholdet mellom EHDS og GDPR.** EHDS etablerer sektorspesifikke regler som supplerer GDPR, og i noen tilfeller gir rettigheter som ikke finnes eksplisitt i GDPR. Samspillet mellom disse regelsettene i norsk kontekst krever juridisk avklaring (kilde: DLA Piper, helsedata.no).

---

### Tekniske gap

Norsk helsesektor registrerer allerede data i de prioriterte kategoriene, men med formater og infrastruktur som ikke oppfyller EHDS-kravene:

1. **Manglende støtte for EEHRxF.** Norske EHR-systemer benytter nasjonale meldingsstandarder for datautveksling. EHDS krever det europeiske utvekslingsformatet (EEHRxF), basert på HL7 FHIR. Overgangen fra nasjonale meldingsstandarder til FHIR-baserte grensesnitt er påbegynt, men langt fra fullført (kilde: Helsedirektoratet).

2. **Manglende tilkobling til MyHealth@EU.** NHN har pilotert tilkobling med utvalgte kommuner i 2024, men dette er ikke operativt for hele sektoren. Full tilkobling krever at alle relevante EHR-systemer kan levere og motta data i korrekt format (kilde: NHN).

3. **Manglende infrastruktur for sekundærbruk.** HealthData@EU-tilkobling og nasjonale sikre analyserom (Secure Processing Environments) er under utvikling gjennom SPUHiN-prosjektet, men ikke operativt (kilde: Helsedirektoratet, helsedata.no).

4. **Manglende nasjonal testinfrastruktur.** EHDS krever obligatorisk testing av EHR-systemer i nasjonalt testmiljø. Slik testinfrastruktur må etableres (kilde: Helsedirektoratets gapanalyse).

5. **Sertifiserings- og CE-merkingskrav.** EHR-systemleverandører må gjennomføre selvdeklarasjon og obligatorisk testing. Nasjonale løsninger som kjernejournal og reseptformidleren har et noe enklere kravregime fordi de er «tatt i bruk» men ikke «plassert på markedet», men også disse må oppfylle interoperabilitetskrav (kilde: Helsedirektoratets gapanalyse).

6. **Ulik modenhet på tvers av sektoren.** Spesialisthelsetjenesten, fastleger, kommunale helse- og omsorgstjenester og private aktører har svært ulik teknisk modenhet og ulike systemer. Dette gjør en enhetlig implementering krevende.

---

### Organisatoriske gap

1. **Ingen utpekt digital helsemyndighet.** EHDS krever at hvert land utpeker en nasjonal digital helsemyndighet (Digital Health Authority). I Norge er det ikke formelt avklart om dette skal være Helsedirektoratet, NHN eller et annet organ. Helsedirektoratet har den strategiske rollen, mens NHN har den operative (kilde: EU 2025/327, CLAUDE.md rolleoversikt).

2. **Ingen etablert HDAB.** Norge må opprette eller utpeke et Health Data Access Body som skal administrere tilgang til helsedata for sekundærbruk, vurdere søknader, utstede datatillatelser og føre tilsyn med sikre analyserom. Denne funksjonen finnes ikke i dag (kilde: EU 2025/327, helsedata.no).

3. **Kompleks aktørstruktur.** Norsk helsesektor har mange aktører med ulike roller: HOD (politisk), Helsedirektoratet (strategi/rammer), NHN (drift/forvaltning), fire RHF-er, over 350 kommuner, private aktører og en rekke systemleverandører. Koordinering av EHDS-implementering på tvers av alle disse er en vesentlig organisatorisk utfordring (kilde: Helsedirektoratet).

4. **Kapasitets- og kompetansemangel.** Implementeringen krever spesialisert kompetanse innen HL7 FHIR, EEHRxF, europeisk helserett, interoperabilitetsstandarder og grensekryssende infrastruktur. Det er usikkert om tilstrekkelig kompetanse er tilgjengelig (kilde: Helsedirektoratet).

5. **Uavklart forhold mellom eksisterende organer.** Forholdet mellom Helsedirektoratet, NHN, helsedata.no, FHI og andre aktører i lys av EHDS-kravene er ikke avklart. Særlig gjelder dette sekundærbruk, der helsedata.no allerede har en koordinerende rolle for forskningstilgang (kilde: Helsedirektoratets konsekvensvurdering).

---

### Semantiske gap

Semantisk interoperabilitet – at data betyr det samme uavhengig av hvem som sender og mottar – er kanskje det mest underkommuniserte og vanskeligste gapet:

1. **Ulike kodeverk og terminologier.** Norske helsevirksomheter bruker en blanding av nasjonale og internasjonale kodeverk (ICD-10, ICPC-2, NKPK, FEST osv.), men bruken er ikke enhetlig, og mappingen til de europeiske kodeverkene EHDS krever (f.eks. SNOMED CT, LOINC, ATC) er ufullstendig (kilde: Helsedirektoratets konsekvensvurdering).

2. **Ulik strukturering og detaljeringsnivå.** Selv når helseopplysninger registreres i de samme kategoriene, varierer struktureringen og detaljeringsnivået mellom virksomheter og systemer. EHDS krever et minimumsinnhold og en minimumsstruktur for de prioriterte kategoriene (kilde: Helsedirektoratets gapanalyse).

3. **Nasjonal informasjonsmodell under utvikling.** Helsedirektoratet har startet arbeidet med nasjonal informasjonsmodell (Helse-NIM) for oppsummerende helseopplysninger (Patient Summary), men dette arbeidet er ikke ferdigstilt (kilde: Helsedirektoratet).

4. **Datakvalitetsutfordringer.** Helseopplysninger kan være registrert for andre formål enn det EHDS krever, noe som gir utfordringer med datakvalitet, kompletthet og relevans. Deling av data med lav kvalitet kan gi begrenset nytte eller i verste fall utgjøre en pasientsikkerhetsrisiko.

5. **Kulturelle forskjeller i registreringspraksis.** Ulike fagmiljøer og virksomheter har ulik registreringspraksis. Harmonisering av praksis er en langvarig prosess som krever endringsledelse, opplæring og insentiver.

---

## Mål

Basert på problemanalysen defineres følgende mål for EHDS-implementeringen i Norge:

### Overordnet mål
Norge skal oppfylle forpliktelsene i EHDS-forordningen innenfor fastsatte tidsfrister, slik at norske innbyggere, helsepersonell og forskere kan dra nytte av sikker og effektiv deling av helseopplysninger innenfor og på tvers av landegrenser i EU/EØS.

### Delmål

**Rettslige delmål:**
1. Norsk helselovgivning skal være harmonisert med EHDS-forordningen innen tidspunktet for EØS-innlemmelse
2. Innbyggernes rettigheter etter EHDS (tilgang, nedlasting, tilgangsbegrensning, opt-out) skal ha rettslig forankring i norsk lov
3. Rettslig rammeverk for sekundærbruk (HDAB, datatillatelser, sikre analyserom) skal være på plass

**Tekniske delmål:**
4. Norske EHR-systemer skal støtte EEHRxF for de prioriterte kategoriene innen fristene (gruppe 1: mars 2029, gruppe 2: mars 2031)
5. Norge skal være operativt tilkoblet MyHealth@EU for grensekryssende utveksling av primærbruksdata
6. Norge skal være operativt tilkoblet HealthData@EU for sekundærbruk
7. Nasjonal testinfrastruktur for obligatorisk testing av EHR-systemer skal være etablert
8. Sikre analyserom som tilfredsstiller EHDS-kravene skal være operative

**Organisatoriske delmål:**
9. Nasjonal digital helsemyndighet skal være utpekt og operativ
10. HDAB skal være etablert og operativ
11. Ansvarsfordelingen mellom nasjonale aktører skal være tydelig avklart

**Semantiske delmål:**
12. Nasjonal informasjonsmodell (Helse-NIM) for prioriterte kategorier skal være ferdigstilt og implementert
13. Nødvendig mapping mellom nasjonale og europeiske kodeverk skal være etablert
14. Registreringspraksis skal understøtte minimumsinnhold og -struktur for prioriterte kategorier

---

## Berørte aktører

### Nasjonale myndigheter og forvaltningsorganer

| Aktør | Påvirkning |
|-------|-----------|
| **Helse- og omsorgsdepartementet (HOD)** | Politisk ansvar for lovendringer, EØS-innlemmelse, bevilgninger og utpeking av nasjonale myndighetsroller |
| **Helsedirektoratet** | Trolig rolle som digital helsemyndighet, ansvar for strategi, rammer, standarder, informasjonsmodeller og kodeverk. Må etablere nye funksjoner og styrke europeisk samarbeid |
| **Norsk helsenett (NHN)** | Operativ ansvarlig for MyHealth@EU-tilkobling, drift av nasjonale komponenter. Må tilpasse teknisk infrastruktur til EHDS-krav |
| **Helsedata.no / FHI** | Berørt av HDAB-etablering og krav til sekundærbruk. Eksisterende funksjoner for forskningstilgang må tilpasses |

### Helsetjenesten

| Aktør | Påvirkning |
|-------|-----------|
| **Regionale helseforetak (RHF-ene)** | Må sikre at helseforetakene etterlever EHDS-krav til EHR-systemer, datakvalitet og grensekryssende deling. Ansvar for risikovurderinger |
| **Kommunene (via KS)** | Over 350 kommuner med kommunale helse- og omsorgstjenester må tilpasse systemer og praksis. Stor variasjon i teknisk modenhet |
| **Fastleger** | Må bruke EHR-systemer som oppfyller EHDS-krav. Endret registreringspraksis |
| **Private helseaktører** | Omfattes av kravene på linje med offentlige aktører |

### Leverandører og næringsliv

| Aktør | Påvirkning |
|-------|-----------|
| **EHR-systemleverandører** | Må tilpasse systemer til EEHRxF, gjennomføre selvdeklarasjon og obligatorisk testing. Betydelig utviklingskostnad |
| **Annen helseteknologiindustri** | Berørt av nye krav til datadeling, sertifisering og interoperabilitet |

### Innbyggere og pasienter

| Aktør | Påvirkning |
|-------|-----------|
| **Innbyggere/pasienter** | Nye rettigheter til tilgang, nedlasting, tilgangsbegrensning og opt-out. Mulighet for å dele helseopplysninger ved reise/flytting i EU/EØS |

### Forskning og innovasjon

| Aktør | Påvirkning |
|-------|-----------|
| **Forskningsinstitusjoner** | Ny tilgangsmodell for helsedata via HDAB. Bruk av sikre analyserom. Potensielt bedre datatilgang, men nye prosesser |
| **Legemiddelindustri og medisinsk teknologi** | Nye muligheter for tilgang til helsedata for forskning og utvikling via HDAB |

---

*Denne problemdefinisjonen er basert på kunnskapsgrunnlaget for EHDS (rapporter/kunnskapsgrunnlag-ehds.md) og utarbeidet 15. mars 2026. Problemdefinisjonen bør oppdateres når gjennomføringsrettsakter fra EU-kommisjonen vedtas og norsk EØS-innlemmelse avklares.*
