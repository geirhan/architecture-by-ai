# Klarspråksgjennomgang av delrapport 1–9

**Status**: Under arbeid — internt arbeidsdokument
**Sist oppdatert**: 2026-08-10
**Metode**: Hver delrapport er vurdert mot prinsippene i
prosjektskillen `klarsprak-offentlig` (basert på Språkloven § 9
og Språkrådets klarspråksprinsipper). Gjennomgangen omfatter
trinn 1 (overordnet evaluering) og trinn 2 (konkrete eksempler
med forbedringsforslag). Trinn 3 (omskriving av rapportene) ble
gjennomført 2026-08-10 for alle ni delrapportene, innenfor strenge
rammer: meningsinnhold, [DOK]/[ANT]-merking, kildereferanser og
kapittelnummerering er bevart, og omskrivinger som ville tilført
en tolkning (f.eks. å navngi en aktør uten kildedekning) er løst
konservativt eller ikke gjennomført.

Merk: [DOK]/[ANT]-merkingen er en bevisst metodisk konvensjon i
prosjektet og er ikke vurdert som språksvakhet.

## 1. Samlet bilde

| Delrapport | Nivå | Viktigste forbedring |
|---|---|---|
| 1 – Dagens verdikjede | Godt | Løft kjernekonklusjonen (kap. 8) frem til innledningen |
| 2 – Utfordringer og flaskehalser | Middels | Passiv med usynlig avsender; forklar PICO, GRADE, IGOE, RHF, EPJ ved første bruk |
| 3 – LLM muligheter og risikoer | Godt | Erstatt «det er»-konstruksjoner med tydelig subjekt; kort ledersammendrag øverst |
| 4 – Ny verdikjede | Middels | Synlig avsender i tiltak og anbefaling («Det etableres…», «Det anbefales…»); bryt opp de lengste periodene |
| 5 – Arkitektur og komponenter | Godt | Forklar RAG, DPIA, EHRxF, guardrails, vektorindeksering ved første bruk |
| 6 – Internasjonale erfaringer | Godt | Forklar FHIR, ESF, USMLE, «living guidelines»; norske og parallelle overskrifter/lister |
| 7 – Samlet vurdering | Middels | Substantivsyke og passiv uten avsender; stram inn ledersammendraget |
| 8 – Aktøranalyse | Middels | Bryt opp de komprimerte «Guides»-blokkene i IGOE-analysen til punktlister |
| 9 – Fremtidsscenarioer | Middels | Splitt lange, innskutte setninger; forklar «orkestrering» og andre nøkkelbegreper |

Fire delrapporter vurderes som «Godt» (1, 3, 5, 6) og fem som
«Middels» (2, 4, 7, 8, 9). Ingen vurderes som «Svakt». Merk at de
tre mest beslutningsnære dokumentene (delrapport 2, 4 og 7 —
utfordringsbildet, alternativene og den samlede vurderingen) alle
ligger på «Middels». Klarspråksinnsatsen bør derfor prioriteres
der beslutningstakerne faktisk leser.

## 2. Tverrgående mønstre

Fem svakheter går igjen på tvers av delrapportene:

1. **Passiv form med usynlig avsender** (alle delrapporter, mest
   uttalt i 2, 4, 7 og 8). Formuleringer som «Det etableres…»,
   «Det anbefales…», «overlates til», «er fordelt på» skjuler
   hvem som handler eller har ansvar. Dette er mest alvorlig i
   tiltaks- og anbefalingstekst, der leseren trenger å vite hvem
   som skal gjøre hva. Merk at enkelte omskrivinger («Ingen aktør
   følger opp…») innebærer en tolkning som må sjekkes mot
   kildegrunnlaget før endring.
2. **Uforklarte faguttrykk og forkortelser** (alle delrapporter).
   Gjengangere: PICO, GRADE, IGOE, RHF, EPJ (dp2), RNAO, EHDS i
   selve delrapporten (dp4), RAG, DPIA, EHRxF, guardrails (dp5),
   FHIR, ESF, USMLE (dp6), MECE, mitigering (dp7), IDEF0, EMA,
   SPC (dp8), orkestrering, «de facto standard» (dp9). Én kort
   forklaring ved første bruk per delrapport er nok.
3. **Substantivsyke** (mest uttalt i 4, 7 og 9): «foreldelse av
   kunnskapsgrunnlaget», «kapasitetsbegrensning for», «etablering
   av», «muliggjør faseinndelt implementering». Omskriving til
   verb gjør teksten mer konkret og kortere.
4. **Lange setninger med innskutte ledd** (mest uttalt i 2, 4 og
   9): perioder på 40–90 ord med semikolon, tankestreker og
   parentetiske innskudd mellom subjekt og verb. Løsningen er
   gjennomgående den samme: splitt i to–tre setninger med én
   tanke per setning.
5. **Viktigste først etterleves ujevnt** (1, 3, 5, 6, 8):
   hovedkonklusjonen kommer ofte først i siste kapittel. Delrapport
   2 er her et positivt forbilde («Hovedproblemet i én setning» i
   kap. 2.1). Et kort «hovedbudskap»-avsnitt øverst i hver
   delrapport ville løftet skumlesbarheten betydelig.

I tillegg noteres enkelte engelske innslag som bør fornorskes
(«Lessons learned»-overskrift i dp6, «konsumerer» i dp9) og
hyppig «jf.» i løpende tekst (dp4), som etter Språkrådets råd bør
skrives ut.

**Styrker som bør bevares**: gjennomgående god kapittelstruktur og
informative overskrifter, utstrakt og god tabellbruk, kort og
presis avgrensningstekst, samt kildedisiplinen med [DOK]/[ANT].

## 3. Anbefalt videre prosess

1. **Prioriter delrapport 2, 4 og 7** (beslutningsnære, alle på
   «Middels»). Størst effekt per innsats: aktiv form i tiltaks- og
   anbefalingstekst, og forklaring av faguttrykk ved første bruk.
2. **Ta delrapport 8 og 9 i neste runde**: punktlister i
   IGOE-delen (dp8) og setningssplitting (dp9) er mekaniske grep
   med lav risiko for meningsendring.
3. **Delrapport 1, 3, 5 og 6 trenger bare lettere justering**:
   faguttrykksforklaringer og «viktigste først»-grep.
4. **Forankrede rapporter (dp1, dp8) endres bevisst**: ordlyds-
   endringer i forankrede dokumenter bør besluttes eksplisitt,
   siden teksten er brukt som referanse i pågående arbeid.
5. Etter eventuelle endringer i delrapportene: kjør
   `python3 skripts/generer_html.py` før commit.

Omskrivinger der klarspråksversjonen tilfører en tolkning (f.eks.
å navngi en aktør der originalen er passiv) må sjekkes mot
kildegrunnlaget før de gjennomføres — klarspråk skal ikke endre
meningsinnhold eller sikkerhetsnivå i utsagn.

---

## 4. Delrapport 1 — Dagens verdikjede

### Overordnet evaluering

- **Målgruppe og struktur**: Strukturen er i hovedsak god og tilpasset fagpersoner/beslutningstakere – overskrifter følger verdikjedens logikk, og tabeller brukes godt til å oppsummere aktører og egenskaper. Kapittel 7 og 8 følger «viktigste først»-prinsippet dårligere: konklusjonen i kap. 8 kommer etter en lang oppramsing av observasjoner i kap. 7, i stedet for at hovedbudskapet løftes tidligere.
- **Flyt og setningslengde**: De fleste setningene er innenfor anbefalt lengde, men enkelte er tunge på grunn av mange innskutte leddsetninger og opphopning av informasjon (se eksempler i kap. 1.2, 3a og 5.2).
- **Gjentakende mønstre**: Utstrakt bruk av substantivsyke («Innholdsproduksjonen er desentralisert», «formidling», «operasjonalisering», «tilpasning») og passiv/upersonlig form uten synlig avsender («det finnes ingen mekanisme», «Dokumentasjonen indikerer»). Dette er delvis bevisst og akseptabelt i en analytisk rapport, men noen steder skjuler det hvem som faktisk gjør eller bør gjøre noe.
- **Faguttrykk**: De fleste sentrale forkortelser (GRADE, KBP, PICO, FEST) forklares ved første bruk. Noen unntak: «SPC» (kap. 3c) forklares ikke, og «redaktøransvar» vs. «utgiveransvar» (kap. 3d) brukes uten at forskjellen defineres for leseren.
- **Positivt**: Tabellene i kap. 2, 5.1 og 6 er et godt klarspråksgrep – de gjør komplekse sammenligninger skannbare. Kap. 1.3 (avgrensning) er kort og presist formulert.

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| 1.1 | «Denne rapporten kartlegger dagens prosess fra forskning til formidlet kunnskap til innbyggere i den norske helsesektoren. Kartleggingen danner grunnlag for å identifisere utfordringer, flaskehalser og forbedringsmuligheter i verdikjeden.» | «Rapporten kartlegger hvordan kunnskap beveger seg fra forskning til innbyggere i den norske helsesektoren. Kartleggingen skal avdekke utfordringer, flaskehalser og forbedringsmuligheter i verdikjeden.» | Substantivsyke («formidlet kunnskap», «identifisere») omskrives til verb; kortere setninger. |
| 1.2 | «Verdikjeden i denne rapporten fokuserer primært på infrastrukturen som understøtter trinnene 1-4 på nasjonalt nivå – hvordan forskningsbasert kunnskap sammenstilles, kvalitetssikres og gjøres tilgjengelig.» | «Rapporten ser primært på infrastrukturen som understøtter trinn 1–4 på nasjonalt nivå, altså hvordan Helsedirektoratet, FHI og andre aktører sammenstiller, kvalitetssikrer og tilgjengeliggjør forskningsbasert kunnskap.» | Passiv uten synlig avsender («sammenstilles, kvalitetssikres og gjøres tilgjengelig») gjøres aktiv – synliggjør hvem som gjør hva. |
| 3a | «Utviklingsprosessen er beskrevet i Helsedirektoratets Veileder for utvikling av kunnskapsbaserte retningslinjer [19] og involverer tverrfaglige arbeidsgrupper med bidrag fra fagmedisinske foreninger og brukerrepresentanter, ekstern høring og systematisk vurdering av evidens opp mot norske forhold [2].» | «Helsedirektoratets Veileder for utvikling av kunnskapsbaserte retningslinjer [19] beskriver utviklingsprosessen. Den involverer tverrfaglige arbeidsgrupper med bidrag fra fagmedisinske foreninger og brukerrepresentanter, ekstern høring, og systematisk vurdering av evidens opp mot norske forhold [2].» | Setningen er lang (43 ord) med to sammenkjedede tanker. Splitt i to setninger og aktiv form (§5, §6). |
| 3a | «Dette er den mest autoritative strømmen – den eneste der kunnskap gjennomgår formell normering for norsk kontekst.» | «Dette er den mest autoritative strømmen. Det er den eneste der kunnskap gjennomgår formell normering for norsk kontekst.» | Tankestrek-konstruksjon splittes i to setninger for bedre lesbarhet (§5). |
| 3d | «Innholdsproduksjonen er desentralisert med tydelig ansvarsfordeling: Helsedirektoratet har utgiveransvaret og det etiske og rettslige ansvaret for informasjonsinnholdet, mens NHN er produkteier og har redaktøransvaret – inkludert ansvar for at lokale redaktører følger innholdsstrategien [21] og kvalitetsretningslinjene [10].» | «Helsenorge.no har desentralisert innholdsproduksjon med tydelig ansvarsfordeling: Helsedirektoratet har utgiveransvaret – det etiske og rettslige ansvaret for informasjonsinnholdet – mens NHN er produkteier med redaktøransvaret. Redaktøransvaret innebærer blant annet å sikre at lokale redaktører følger innholdsstrategien [21] og kvalitetsretningslinjene [10].» | Substantivsyke + svært lang setning (48 ord) med innskutt leddsetning. Splitt, og forklar kort hva «redaktøransvar» innebærer (§9). |
| 5.2 | «Overgangen fra retningslinje til innbyggerinformasjon krever at komplekst medisinsk fagspråk gjøres tilgjengelig uten å miste presisjon.» | «Når en retningslinje blir til innbyggerinformasjon, må komplekst medisinsk fagspråk gjøres forståelig uten å miste presisjon.» | Substantivsyke («Overgangen … krever at») omskrives til en mer direkte konstruksjon (§7). |
| 5.2 | «Overgangen fra kunnskapsoppsummering til retningslinje innebærer at vitenskapelig evidens veies mot verdier, ressursbruk og norsk kontekst.» | «Når en kunnskapsoppsummering blir til retningslinje, veier Helsedirektoratet vitenskapelig evidens mot verdier, ressursbruk og norsk kontekst.» | Passiv uten avsender («veies») gjøres aktiv og avsenderen synliggjøres (§6). |
| 5.4 | «Dokumentasjonen indikerer at det i dag mangler gjennomgående standardiserte maskinlesbare formater for kunnskapsinnhold på tvers av strømmene.» | «Dokumentasjonen viser at det i dag mangler standardiserte, maskinlesbare formater for kunnskapsinnhold på tvers av strømmene.» | «Gjennomgående» er overflødig; «indikerer» presiseres til «viser» der funnet er klart dokumentert. |
| 6 | «Kvalitetssikringen i verdikjeden er robust i hvert enkelt steg, men det finnes begrenset systematisk kvalitetssikring av sammenheng på tvers av steg.» | «Kvalitetssikringen er robust i hvert enkelt steg i verdikjeden, men det mangler systematisk kvalitetssikring av sammenhengen mellom stegene.» | «Finnes begrenset» er en omstendelig kansellivending; «mangler» er mer direkte (§8). |
| 6 | «Det er for eksempel ingen automatisert mekanisme som sikrer at innbyggerinformasjon oppdateres når underliggende retningslinjer endres, eller at motstridigheter mellom strømmene blir identifisert og løst.» | «Det finnes for eksempel ingen automatisk mekanisme som sikrer at innbyggerinformasjon oppdateres når retningslinjer endres, eller som fanger opp og løser motstridende informasjon mellom strømmene.» | Passivkonstruksjonen «blir identifisert og løst» gjøres mer direkte (§6). |
| 8 | «Dagens verdikjede fungerer tilstrekkelig for hver enkelt strøm, men systemet som helhet mangler integrasjon.» | (Behold, men flytt tidligere.) | Dette er kjernebudskapet i hele delrapporten, men kommer først i kap. 8. Bør oppsummeres allerede i innledningen (§2, «viktigste først»). |
| 8 | «Forbedringer blir ikke fulgt opp systematisk på tvers av strømmer.» | «Ingen aktør følger systematisk opp forbedringer på tvers av strømmene.» | Passiv uten avsender gjøres aktiv – men «ingen aktør» er en tolkning som bør sjekkes mot kildegrunnlaget før endring (§6). |
| 3c | Bruk av «SPC» uten forklaring | Innfør: «godkjente preparatomtaler (SPC – Summary of Product Characteristics)» ved første bruk i kap. 3c. | Faguttrykket SPC forklares ikke ved første bruk (§9). |
| 2 (steg 3) | «Kunnskapen fra steg 1 og 2 omsettes og formidles til helsepersonell og innbyggere gjennom fire parallelle hovedstrømmer.» | «Helsepersonell og innbyggere mottar kunnskapen fra steg 1 og 2 gjennom fire parallelle hovedstrømmer.» | Passiv («omsettes og formidles») gjøres aktiv, med mottaker som subjekt (§6). |

**Samlet vurdering: Godt.** Solid struktur, gode tabeller og gjennomgående forklarte faguttrykk. Viktigste forbedring: løft kjernekonklusjonen («verdikjeden fungerer i hvert steg, men mangler integrasjon på tvers») frem til innledningen, og gjør passivkonstruksjoner uten synlig avsender om til aktiv form der avsenderen er kjent.

## 5. Delrapport 2 — Utfordringer og flaskehalser

### Overordnet evaluering

- **Målgruppe og struktur er stort sett godt tilpasset**: Rapporten er skrevet for fagpersoner og beslutningstakere, og kap. 2.1 («Hovedproblemet i én setning») plasserer hovedbudskapet tidlig og tydelig – det er god klarspråkspraksis. Leseveiledningen i kap. 2.5 og rangeringstabellen i kap. 8.1 gjør teksten skannbar.
- **Enkelte tunge, flerleddede setninger** bryter 25–30-ords-regelen, særlig i kap. 2.2–2.3, 3.1, 4.3 og 9.7, ofte med parentetiske innskudd mellom hovedledd.
- **Gjennomgående mønster med passiv form og usynlig avsender**: Formuleringer som «det finnes ikke», «stilles spørsmålet», «er utledet», «overlates til», «er undervurdert» skjuler hvem som gjør eller bør gjøre noe – et gjentakende trekk gjennom hele rapporten.
- **Noe substantivsyke**: tunge nominaliseringer som «forskningsproduksjonen», «overgangen», «prioritering», «suboptimalisering» og «konsensusbygging».
- **Inkonsekvent forklaring av faguttrykk**: Rapporten er forbilledlig på å forklare metodiske begreper som MECE og [DOK]/[ANT], men flere faguttrykk introduseres uten forklaring ved første bruk – blant annet PICO, GRADE, IGOE, RHF og EPJ.

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| 2.2 (D3) | «Ansvar for verdikjeden er fordelt på rundt 20 aktører uten helhetlig styringsmandat.» | «Rundt 20 aktører deler ansvaret for verdikjeden, uten at noen har et helhetlig styringsmandat.» | Prinsipp 6 (aktiv form) – gjør aktørene til synlig subjekt. |
| 2.3 | «De seks dimensjonene i kap. 2.2 er bevisst *observasjoner* som virker samtidig -- de er ikke ment som en gjensidig utelukkende inndeling, og flere av dem overlapper (lang tid er delvis et symptom på lav kapasitet; manglende eierskap for implementering er delvis en styringssvikt).» | «De seks dimensjonene i kap. 2.2 er bevisst valgt som *observasjoner* som virker samtidig. De er ikke en gjensidig utelukkende inndeling, og flere overlapper. For eksempel er lang tid delvis et symptom på lav kapasitet, og manglende eierskap for implementering er delvis en styringssvikt.» | Prinsipp 5 – deler opp en lang periode med innskutt parentes i tre kortere setninger. |
| 3.1 | «Estimater fra internasjonale kilder indikerer at det publiseres over 3 millioner vitenskapelige artikler årlig på tvers av alle fagområder, med en betydelig andel innen medisin og helsefag.» | «Internasjonale kilder anslår at det publiseres over 3 millioner vitenskapelige artikler årlig på tvers av alle fagområder. En betydelig andel av disse er innen medisin og helsefag.» | Prinsipp 5 – splitter en 31-ords setning i to. |
| 3.2 | «Overgangen fra ferdig kunnskapsoppsummering til publisert nasjonal faglig retningslinje er den mest tidkrevende enkeltovergangen i verdikjeden.» | «Det tar lengst tid å gå fra ferdig kunnskapsoppsummering til publisert retningslinje – dette er det mest tidkrevende steget i verdikjeden.» | Prinsipp 7 – erstatter dobbel bruk av «overgang(en)» med verb. |
| 3.2 | «Begrenset kapasitet: Helsedirektoratet har et begrenset antall retningslinjeprosjekter som kan pågå parallelt. Prioritering mellom fagområder er nødvendig, noe som innebærer at enkelte områder får lenger ventetid.» | «Begrenset kapasitet: Helsedirektoratet kan bare kjøre et begrenset antall retningslinjeprosjekter samtidig. Direktoratet må derfor prioritere mellom fagområder, og enkelte områder får lenger ventetid.» | Prinsipp 6 og 7 – synlig avsender og «prioritering» omskrevet til verb. |
| 3.4 | «Verdikjedens sentrale infrastruktur understøtter primært trinn 1-4 ... mens trinn 5 (anvende) og 6 (evaluere) overlates til den enkelte virksomhet.» | «Verdikjedens sentrale infrastruktur understøtter primært trinn 1–4 ..., mens den enkelte virksomhet selv må ivareta trinn 5 (anvende) og 6 (evaluere).» | Prinsipp 6 – «overlates til» pulveriserer ansvar; virksomheten gjøres til aktivt subjekt. |
| 3.3 | «Denne overgangen er ofte undervurdert i ressursplanlegging.» | «Virksomhetene undervurderer ofte denne overgangen i ressursplanleggingen.» (Krever avklaring: hvem – nasjonale myndigheter, RHF-ene eller kommunene?) | Prinsipp 6 – «er undervurdert» skjuler hvem som gjør vurderingen. |
| 4.3 | «Søkedata og brukerundersøkelser indikerer at en betydelig andel av befolkningen bruker Google, sosiale medier og i økende grad generative AI-verktøy som ChatGPT for å finne helseinformasjon.» | «Søkedata og brukerundersøkelser viser at mange innbyggere bruker Google og sosiale medier for å finne helseinformasjon. I økende grad brukes også generative KI-verktøy som ChatGPT.» | Prinsipp 5 – deler en 36-ords setning i to. |
| 6.1 | «Det finnes ikke et helhetlig styringsmandat for verdikjeden fra forskning til innbygger, noe som kan føre til suboptimalisering innenfor det enkelte steg uten at helheten ivaretas.» | «Ingen aktør har et helhetlig styringsmandat for verdikjeden fra forskning til innbygger. Det kan føre til at hvert steg optimaliseres for seg selv, uten at noen ivaretar helheten.» | Prinsipp 6 og 9 – «det finnes ikke» skjuler ansvarsforholdet; «suboptimalisering» er unødvendig sjargong. |
| 9.1 | «Metoden er en strukturert «hvorfor»-analyse: for hver flaskehals stilles spørsmålet «hvorfor eksisterer denne?» i opptil 3–4 nivåer, til analysen lander på et forhold som ikke kan forklares videre innenfor verdikjedens egne rammer.» | «Metoden er en strukturert «hvorfor»-analyse: Vi stiller spørsmålet «hvorfor eksisterer denne?» for hver flaskehals, i opptil 3–4 nivåer, til vi når et forhold som ikke kan forklares videre innenfor verdikjedens egne rammer.» | Prinsipp 6 – «stilles» skjuler at det er utrederne som utfører analysen. |
| 9.7 | «Dimensjonene er utledet ved å gruppere rotårsakene etter typen beslutning de utløser, og uttrykt som akser fremfor bokser for å understreke at de er gradvise valgrom – ikke enten-eller.» | «Vi har utledet dimensjonene ved å gruppere rotårsakene etter hvilken type beslutning de utløser. Vi uttrykker dem som akser, ikke bokser, for å vise at de er gradvise valgrom – ikke et enten-eller.» | Prinsipp 5 og 6 – deler en lang passiv periode i to aktive setninger. |
| 9.2 (R2) | «...anbefalingsnivå-struktur med PICO som egen innholdstype ... og PICO/GRADE brukes metodisk i utviklingen (IS-1870).» | «...anbefalingsnivå-struktur med PICO (Population, Intervention, Comparison, Outcome – rammeverk for å formulere kliniske spørsmål) som egen innholdstype ... PICO og GRADE (metode for å gradere kvaliteten på evidens) brukes metodisk i utviklingen (IS-1870).» | Prinsipp 9 – PICO og GRADE brukes gjennomgående uten å forklares ved første bruk. |
| 2.2 (D3) | «...de fire RHF-ene med tilhørende helseforetak...» | «...de fire regionale helseforetakene (RHF-ene) med tilhørende helseforetak...» | Prinsipp 9 – RHF forklares ikke ved første bruk i denne delrapporten. |
| 6.6.2 | «...selv oppdaterte retningslinjer når ikke klinikere der de jobber (i EPJ-en), men ligger i separate portaler...» | «...selv oppdaterte retningslinjer når ikke klinikere der de jobber – i pasientjournalsystemet (EPJ) – men ligger i separate portaler...» | Prinsipp 9 – EPJ (elektronisk pasientjournal) forklares ikke ved første bruk. |
| 9.1 | «...IGOE-analysen i delrapport 8...» | «...IGOE-analysen (rammeverk for å kartlegge Input, Guidance, Output og Enablers per aktør) i delrapport 8...» | Prinsipp 9 – IGOE nevnes uten forklaring. |

**Samlet vurdering: Middels.** Strukturen og den tidlige konklusjonen er god, men gjennomgående passiv form med usynlig avsender og et knippe uforklarte faguttrykk (PICO, GRADE, IGOE, RHF, EPJ) er den viktigste forbedringen.

## 6. Delrapport 3 — Store språkmodeller: muligheter og risikoer

### Overordnet evaluering

- **Målgruppe og struktur**: Rapporten treffer godt for fagpersoner/beslutningstakere. Strukturen følger en logisk flyt, men bryter «viktigste først»-prinsippet: leseren må gjennom fem kapitler før hovedkonklusjonen (kap. 7). Et kort ledersammendrag øverst ville gjort rapporten mer skumlesbar.
- **Flyt og setningslengde**: Setningene er stort sett godt tilpasset. Noen enkeltsetninger nærmer seg eller overskrider 30 ord med flere innskutte leddsetninger.
- **Gjentakende mønstre**: Utstrakt bruk av passiv/upersonlig konstruksjon med usynlig avsender («Det er...», «Det er behov for...», «Det gjenstår å se...», «Det er avgjørende...») – det klart mest gjennomgående avviket.
- **Faguttrykk**: Stort sett godt forklart ved første bruk (LLM, RAG, GPAI, MDR). Unntak: «kunnskapssyntese» og «living guidelines» brukes uten (fullstendig) forklaring.
- **Punktlister**: God parallell oppbygning i de fleste lister; noen blander lengre forklarende setninger med korte stikkord.

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| 1 | «Formålet med denne delrapporten er å gi en balansert vurdering av muligheter og risikoer ved bruk av LLM-er i kunnskapsforvaltning i helsesektoren, med særlig vekt på de regulatoriske rammene som følger av EU AI Act og relevansen for EHDS-konteksten.» | «Denne delrapporten vurderer muligheter og risikoer ved bruk av LLM-er i kunnskapsforvaltning i helsesektoren. Vi legger særlig vekt på kravene i EU AI Act og hva de betyr for EHDS.» | Prinsipp 5 (42 ord i én setning) og prinsipp 6 (aktiv form, synlig avsender). |
| 4.5 | «Dersom KI-generert helseinformasjon fører til skade, oppstår spørsmål om hvem som er ansvarlig.» | «Hvis KI-generert helseinformasjon fører til skade, oppstår spørsmålet: hvem er ansvarlig?» | Prinsipp 8 – fjerne kansellipreget «oppstår spørsmål om». |
| 4.5 | «Det gjenstår å se hvordan reglene vil bli tolket og håndhevet i praksis» | «Det er foreløpig uklart hvordan myndighetene vil tolke og håndheve reglene i praksis» | Prinsipp 6 – passiv uten synlig avsender. |
| 4.2 | «Det er avgjørende at KI-bruk ikke undergraver myndighetens troverdighet.» | «Helsedirektoratet må sikre at KI-bruk ikke undergraver myndighetens troverdighet.» | Prinsipp 6 – usynlig avsender. |
| 4.5 | «Informasjonssystemer faller normalt utenfor, men jo mer personaliserte og handlingsrettede rådene er, desto nærmere kommer man grensen for medisinsk utstyr.» | «Informasjonssystemer regnes normalt ikke som medisinsk utstyr. Men jo mer personaliserte og handlingsrettede rådene er, desto nærmere kommer systemet grensen til medisinsk utstyr.» | Prinsipp 5 – del opp lang periode med to hovedtanker. |
| 5 | «Denne tidsplanen gir norske aktører en avgrenset periode til å forberede seg, men arbeidet bør starte tidlig gitt kompleksiteten i helsedomenet.» | «Tidsplanen gir norske aktører en avgrenset periode til å forberede seg. Arbeidet bør likevel starte tidlig, fordi helsedomenet er komplekst.» | Prinsipp 5 og 7 («kompleksiteten i» → «er komplekst»). |
| 5 | «Norske helsemyndigheter må: Kartlegge hvilke eksisterende og planlagte KI-systemer som faller inn under reguleringsregimet» | «Norske helsemyndigheter må kartlegge hvilke eksisterende og planlagte KI-systemer reglene omfatter» | Prinsipp 9 – «reguleringsregimet» erstattet med enklere formulering. |
| 6 | «KI-systemer som påvirker offentlig helseinformasjon bør være underlagt demokratisk kontroll.» | «Folkevalgte organer bør ha demokratisk kontroll over KI-systemer som påvirker offentlig helseinformasjon.» | Prinsipp 6 – passiv uten synlig aktør. |
| 6 | «Det er et strategisk valg mellom å bruke kommersielle modeller (...) og å investere i egne eller nordiske modeller (...).» | «Norge står overfor et strategisk valg: bruke kommersielle modeller (...) eller investere i egne eller nordiske modeller (...).» | Prinsipp 6 – synliggjør hvem som velger. |
| 3.1 | «KI-assistert screening har potensial til å redusere denne tiden vesentlig.» | «KI-assistert screening kan redusere tidsbruken vesentlig.» | Prinsipp 8 – fjern «har potensial til å». |
| 3.1 | «kunnskapssyntese» (brukes uten forklaring) | «kunnskapssyntese (å sammenstille forskningsfunn til samlet kunnskap)» ved første bruk | Prinsipp 9. |
| 3.4 | «living guidelines» (delvis forklart) | «'living guidelines' – retningslinjer som oppdateres fortløpende etter hvert som ny evidens publiseres, i stedet for på faste tidspunkt» | Prinsipp 9 – gjør forklaringen fullstendig. |
| 4.5 | «Helsedirektoratet som avsender av informasjonen vil sannsynligvis bære ansvaret uavhengig av om innholdet er generert av KI eller mennesker – men dette er foreløpig rettslig uavklart.» | «Helsedirektoratet vil trolig bære ansvaret som avsender, uavhengig av om KI eller mennesker har laget innholdet. Dette spørsmålet er foreløpig ikke rettslig avklart.» | Prinsipp 5 – splitt lang periode med tankestrek-innskudd. |

**Samlet vurdering: Godt.** Viktigste forbedring: erstatt gjennomgående «det er»-konstruksjoner med tydelig subjekt, og vurder et kort ledersammendrag først.

## 7. Delrapport 4 — Ny verdikjede

### Overordnet evaluering

- **Struktur og målgruppe**: Godt strukturert etter utredningsinstruksens mal, med informative kapitteloverskrifter og faste underoverskrifter (Beskrivelse, Konsekvenser, Risiko, Kostnad, Vurdering). Sammendraget (kap. 10) og anbefalingen (kap. 9.1) kommer imidlertid sent – et kort ledersammendrag først i dokumentet ville styrket «viktigste først».
- **Setningslengde**: De fleste setninger er innenfor 25–30 ord, men noen passasjer – særlig faktaboksen om Meld. St. 11 før kap. 1 og resonnementer i kap. 6.1/6.2 og 9.1 – har svært lange setninger med semikolon, innskutte sitater og leddsetninger.
- **Substantivsyke**: Gjennomgående mange nominaliseringer («videreføring», «etablering», «gjennomføring», «tilrettelegging», «reduksjon i gjennomløpstid»).
- **Passiv form / usynlig avsender**: Gjennomgående mønster, særlig i tiltaksbeskrivelsene («Det etableres...», «Det anbefales...») – gjør det uklart hvem som skal utføre tiltaket.
- **Faguttrykk**: RAG forklares godt; EHDS, RNAO og enkelte forkortelser forklares ikke ved første bruk i selve delrapporten. «Jf.» brukes hyppig i løpende tekst, i strid med Språkrådets anbefaling.

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| Før kap. 1 | «Regjeringen har lagt fram en plan som gir politisk retning til kjernen i flere av alternativene her: kap. 7.2 varsler en «trygg, offentlig KI-basert tjeneste» som del av en digital førstelinje, via Helsenorge, utviklet «i samarbeid med næringslivet og ved kjøp av kvalitetssikrede KI-løsninger i markedet» og som «bygges ut trinnvis»; kap. 8.3 varsler at KI gir muligheter for «produksjon, oppsummering og mer målrettet formidling av kunnskap, tilpasset norske forhold», og at Helsebiblioteket skal utredes videreutviklet til en «nasjonal infrastruktur for kunnskapsformidling».» | «Regjeringens plan gir politisk retning til flere av alternativene. Kap. 7.2 varsler en «trygg, offentlig KI-basert tjeneste» som del av en digital førstelinje via Helsenorge, utviklet i samarbeid med næringslivet og ved kjøp av kvalitetssikrede KI-løsninger. Tjenesten skal bygges ut trinnvis. Kap. 8.3 varsler at KI kan gi bedre produksjon, oppsummering og formidling av kunnskap tilpasset norske forhold, og at Helsebiblioteket skal utredes videreutviklet til en nasjonal infrastruktur for kunnskapsformidling.» | Prinsipp 5 – én over 90 ord lang setning splittes i fire kortere. |
| 1.2 | «Rapporten er strukturert i tråd med utredningsinstruksens krav 2 (utrede relevante tiltak) og krav 5 (anbefalt tiltak).» | «Rapporten følger utredningsinstruksens krav 2 (utrede relevante tiltak) og krav 5 (anbefalt tiltak).» | Prinsipp 6 – passiv «er strukturert». |
| 2.1 | «Nullalternativet innebærer at dagens verdikjede for kunnskapsforvaltning videreføres uten vesentlige endringer.» | «Nullalternativet innebærer at aktørene viderefører dagens verdikjede for kunnskapsforvaltning uten vesentlige endringer.» | Prinsipp 6 – «videreføres» er passiv uten synlig avsender. |
| 2.5 | «Videreføring uten endring innebærer en implisitt aksept av at offentlig helseinformasjon gradvis taper relevans sammenlignet med kommersielle alternativer.» | «Å videreføre dagens praksis uten endring betyr i praksis å akseptere at offentlig helseinformasjon gradvis taper relevans sammenlignet med kommersielle alternativer.» | Prinsipp 7 – tung nominalstil omskrives til verb. |
| 3.2 | «Det etableres en systematisk prosess der oppdaterte retningslinjer utløser obligatorisk oppdatering av tilhørende innbyggerinformasjon...» | «Helsedirektoratet etablerer en systematisk prosess der oppdaterte retningslinjer utløser obligatorisk oppdatering av tilhørende innbyggerinformasjon...» | Prinsipp 6 – «Det etableres» er et gjennomgående usynlig-avsender-mønster i kap. 3.2, 4.2 og 5.2. |
| 3.2 | «Det etableres et tverrsektorielt koordineringsforum med representanter fra Helsedirektoratet, FHI og NHN som møtes regelmessig...» | «Helsedirektoratet, FHI og NHN etablerer et tverrsektorielt koordineringsforum som møtes regelmessig...» | Prinsipp 6 – gjør avsenderen tydelig. |
| 5.2 | «Når ny evidens identifiseres som tilstrekkelig robust til å påvirke anbefalinger, genererer KI-systemet et utkast til oppdatert retningslinje...» | «Når KI-systemet identifiserer ny evidens som tilstrekkelig robust til å påvirke anbefalinger, genererer det et utkast til oppdatert retningslinje...» | Prinsipp 6 – KI-systemet er allerede det naturlige subjektet. |
| 6.1.1 | «Styringsmandatet krever politiske grep (lovfesting, etablering av forum for faglig normering, tydeligere departemental styring) som ligger utenfor mandatet til et KI-teknologisk tiltak.» | «Styringsmandatet krever politiske grep – å lovfeste oppgavedeling, etablere et forum for faglig normering og styre tydeligere fra departementet – som ligger utenfor mandatet til et KI-teknologisk tiltak.» | Prinsipp 7 – nominaliseringer omskrives til verb. |
| 9.1 | «Det anbefales en faseinndelt tilnærming der alternativ 2 (moderat KI-støtte) implementeres som startpunkt, med gradvis utvidelse mot elementer fra alternativ 3...» | «Rapporten anbefaler en faseinndelt tilnærming der Helsedirektoratet innfører alternativ 2 (moderat KI-støtte) som startpunkt, med gradvis utvidelse mot elementer fra alternativ 3...» | Prinsipp 2 og 6 – rapportens kjernebudskap bør stå i aktiv form. |
| 9.1 | «RNAO kunnskap-til-handling-modellen, som er oversatt til norske forhold, gir et strukturert rammeverk for å lukke dette gapet...» | «RNAO-modellen (Registered Nurses' Association of Ontario) for kunnskap til handling, som er oversatt til norske forhold, gir et strukturert rammeverk for å lukke dette gapet...» | Prinsipp 9 – RNAO forklares ikke ved første bruk. |
| 2.3 | «EHDS (Forordning 2025/327) krever at EHR-systemer kan eksportere og importere strukturert pasientinformasjon i felles europeisk format innen 2029...» | «EHDS (forordningen om det europeiske helsedataområdet, 2025/327) krever at journalsystemer (EHR-systemer) kan eksportere og importere strukturert pasientinformasjon i felles europeisk format innen 2029...» | Prinsipp 9 – EHDS bør skrives ut ved første substansielle bruk i delrapporten. |
| Gjennomgående | «Konsekvensen på systemegenskapene (jf. delrapport 2 kap. 2.3): ...» | «Konsekvensen for systemegenskapene, se delrapport 2 kap. 2.3, er at ...» | Prinsipp 8 og «vanlige feil» – «jf.» bør skrives ut i løpende tekst, særlig ved hyppig bruk. |

**Samlet vurdering: Middels.** Solid struktur og informative overskrifter, men gjennomgående passiv/usynlig avsender («Det etableres...», «Det anbefales...») og enkelte svært lange setninger. Viktigste forbedring: synlig avsender i aktivsetninger for tiltak og anbefalinger, og oppbryting av de lengste periodene.

## 8. Delrapport 5 — Arkitektur og komponenter

### Overordnet evaluering

- **Målgruppe og struktur**: Strukturen følger ArchiMate-lagene logisk, egnet for fagpersoner. Flere underoverskrifter (f.eks. «5.1 Infrastruktur», «7. Standarder og rammeverk») er generiske og forteller ikke hva avsnittet konkluderer med.
- **Viktigste først**: Kapittel 10 (oppsummering) inneholder de mest handlingsrelevante poengene, men står sist.
- **Flyt og setningslengde**: Generelt godt luftet med korte avsnitt, men enkelte setninger er lange med flere innskutte ledd (kap. 1.1, 4.1, 6.3, 8.1).
- **Gjentakende mønstre**: Utstrakt bruk av passiv/upersonlig konstruksjon uten synlig avsender («forutsettes», «skal sikre»). Dels bevisst i en arkitekturbeskrivelse, men enkelte steder skjuler det hvem som har ansvar.
- **Faguttrykk**: Mange forkortelser (RAG, DPIA, CDS Hooks, EHRxF, openEHR, ISO 13606, ATC) brukes uten forklaring ved første bruk, selv om ArchiMate og EHDS forklares greit i kap. 1.2–1.3.

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| 1.1 | «Denne delrapporten beskriver den tekniske og organisatoriske arkitekturen for en KI-støttet verdikjede for kunnskapsforvaltning i helsesektoren. Arkitekturen bygger på funnene fra de foregående delrapportene: kartlegging av dagens verdikjede (delrapport 1), identifiserte utfordringer og flaskehalser (delrapport 2), vurdering av LLM-teknologiens muligheter og risikoer (delrapport 3) og internasjonale erfaringer (delrapport 6).» | «Denne delrapporten beskriver den tekniske og organisatoriske arkitekturen for en KI-støttet verdikjede for kunnskapsforvaltning i helsesektoren. Den bygger på funn fra fire tidligere delrapporter: kartlegging av dagens verdikjede (delrapport 1), utfordringer og flaskehalser (delrapport 2), muligheter og risikoer ved LLM-teknologi (delrapport 3) og internasjonale erfaringer (delrapport 6).» | Prinsipp 5 – 50-ords setning med tung oppramsing splittes. |
| 4.1 | «**Teknologi** \| LLM med RAG (Retrieval-Augmented Generation) mot indekserte vitenskapelige databaser» | «**Teknologi** \| LLM med RAG (retrieval-augmented generation – søk i egne datakilder som grunnlag for svar) mot indekserte vitenskapelige databaser» | Prinsipp 9 – den engelske utskrivingen forklarer ikke konseptet. |
| 6.3 | «EHDS' primærbruk handler om å styrke innbyggeres kontroll over egne helseopplysninger og forbedre helsetjenestelevering. KI-støttet kunnskapsforvaltning understøtter dette ved å: [...]» | «EHDS' primærbruk skal styrke innbyggeres kontroll over egne helseopplysninger og forbedre helsetjenestene. KI-støttet kunnskapsforvaltning kan bidra til dette på tre måter: [...]» | Prinsipp 7/8 – «helsetjenestelevering» er unødvendig nominalisering. |
| 8.1 | «KI-støttet kunnskapsforvaltning introduserer trusler som skiller seg fra tradisjonelle helse-IT-systemer:» | «KI-støttet kunnskapsforvaltning skaper nye typer trusler sammenlignet med tradisjonelle helse-IT-systemer:» | Prinsipp 7 – mer direkte verbbruk. |
| 3.1 | «Denne prosessen er kritisk for å opprettholde tillit til kunnskapsproduksjonen.» | «Denne prosessen er avgjørende for at brukerne skal ha tillit til kunnskapen som produseres.» | Prinsipp 6 og 1 – tydeliggjør hvem som skal ha tillit. |
| 5.1 | «Infrastrukturen skal sikre at løsningen kan driftes sikkert og stabilt innenfor norsk jurisdiksjon.» | «Infrastrukturen skal gjøre det mulig å drifte løsningen sikkert og stabilt innenfor norsk jurisdiksjon.» | Prinsipp 5/6 – «sikre at» er en unødvendig omvei. |
| 5.1 | «Egne GPU-klynger kan benyttes for sensitive oppgaver og egentrenede modeller» | «Man kan bruke egne GPU-klynger til sensitive oppgaver og egentrenede modeller.» | Prinsipp 8 – «benyttes» er kanselliaktig variant av «bruke». |
| 4.1 | «Dokumentdatabase med vektorindeksering, HL7 FHIR Clinical Knowledge Resources for strukturerte data» | «Dokumentdatabase med vektorindeksering (søk basert på semantisk likhet), og HL7 FHIR Clinical Knowledge Resources – en internasjonal standard for strukturerte kliniske kunnskapsdata» | Prinsipp 9 – begge faguttrykk forutsetter forkunnskap. |
| 8.2 | «Arkitekturen forutsetter gjennomføring av DPIA før implementering.» | «Før løsningen tas i bruk, må virksomheten gjennomføre en DPIA (personvernkonsekvensvurdering – en vurdering av personvernrisiko).» | Prinsipp 6 og 9 – «Arkitekturen forutsetter» skjuler hvem som skal handle. |
| 8.5 | «Arkitekturen sikrer nasjonal kontroll over helsedata gjennom krav om norsk jurisdiksjon for datalagring og databehandling.» | «Arkitekturen sikrer nasjonal kontroll over helsedata ved å kreve at data lagres og behandles innenfor norsk jurisdiksjon.» | Prinsipp 7 – tung nominalisering omskrives verbbasert. |
| 10 | «Dette muliggjør faseinndelt implementering der man kan starte med de komponentene som gir størst verdi først (f.eks. kunnskapssyntese-motoren) og gradvis bygge ut.» | «Dette gjør det mulig å innføre løsningen i faser: man kan starte med komponentene som gir størst verdi (for eksempel kunnskapssyntese-motoren) og bygge ut gradvis.» | Prinsipp 7 – «muliggjør faseinndelt implementering» er tung nominalisering. |
| 2 | «Sikkerhets- og personvernhensyn skal integreres fra start» | «Løsningen skal ivareta sikkerhet og personvern fra første designfase» | Prinsipp 6 – «skal integreres» er passiv uten synlig utfører. |
| 6.1 | «Arkitekturen adresserer dette gjennom bruk av HL7 FHIR som primært grensesnitt for strukturerte data, og gjennom støtte for European Health Record Exchange Format (EHRxF).» | «Arkitekturen møter dette kravet på to måter: den bruker HL7 FHIR som hovedgrensesnitt for strukturerte data, og den støtter European Health Record Exchange Format (EHRxF – et europeisk format for utveksling av pasientjournaldata).» | Prinsipp 5 og 9 – to poenger uten tydelig opplisting; EHRxF forklares ikke. |
| 4.1 | «guardrails for å hindre uautorisert medisinsk rådgivning» | «tekniske sperrer («guardrails») som skal hindre at chatboten gir uautorisert medisinsk rådgivning» | Prinsipp 9 – engelsk fagsjargong uten norsk forklaring. |

**Samlet vurdering: Godt.** Strukturert og konsekvent. Viktigste forbedring: forklar sentrale faguttrykk og forkortelser (RAG, DPIA, EHRxF, guardrails, vektorindeksering) ved første bruk, og erstatt tunge nominaliseringer med direkte verbformer i kap. 6, 8 og 10.

## 9. Delrapport 6 — Internasjonale erfaringer

### Overordnet evaluering

- **Målgruppe og struktur**: Tilpasset fagpersoner og beslutningstakere med klar, logisk struktur. Noen overskrifter er generiske («Resultater og utfordringer», «Andre relevante initiativ»).
- **Flyt og setningslengde**: Gjennomgående moderat lengde og lett å lese; stort sett aktiv form med tydelig avsender.
- **Substantivsyke**: Forekommer punktvis, særlig i kapittel 7 og 8, men er ikke gjennomgående.
- **Faguttrykk uten forklaring**: Det klareste gjentakende mønsteret – CQL forklares, men FHIR, ESF, USMLE, Med-PaLM 2, «living guidelines» og sensitivitet/spesifisitet gjør det ikke.
- **Skumlesbarhet**: Punktlistene har stort sett god parallell oppbygning, men rapporten mangler et kort «hovedbudskap»-avsnitt før kapittel 1 – konklusjonene kommer først i kapittel 8.

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| 2 | «SMART står for Standards-based, Machine-readable, Adaptive, Requirements-based, Testable.» | «SMART står for Standards-based, Machine-readable, Adaptive, Requirements-based, Testable (standardbasert, maskinlesbar, tilpasningsdyktig, kravbasert og testbar).» | Prinsipp 9 – engelsk forkortelse uten norsk forklaring. |
| 3 | «National Institute for Health and Care Excellence (NICE) i Storbritannia har utviklet et Evidence Standards Framework (ESF) for å evaluere digitale helseteknologier.» | «National Institute for Health and Care Excellence (NICE) i Storbritannia har utviklet et rammeverk for evidenskrav, Evidence Standards Framework (ESF), for å vurdere digitale helseteknologier.» | Prinsipp 9 – ESF forklares ikke i klartekst ved første bruk. |
| 3 | Overskrift: «Lessons learned» | «Erfaringer fra NICE» | Prinsipp 3 og 10 – engelsk overskrift i norsk fagrapport; bør ha norsk, informativ tittel. |
| 4 | «Sensitivitet versus spesifisitet: I screening er det kritisk å ikke miste relevante studier.» | «Sensitivitet og spesifisitet: I screening er det avgjørende å ikke overse relevante studier. Sensitivitet er andelen relevante studier verktøyet fanger opp.» | Prinsipp 9 – begrepsparet er sentralt, men forklares ikke. |
| 6 | «Store språkmodeller (LLM-er) fra aktører som OpenAI og Google har vist oppsiktsvekkende ytelse på medisinske benchmarks.» | «Store språkmodeller (LLM-er, dataprogrammer som genererer og tolker tekst) fra aktører som OpenAI og Google har vist svært god ytelse på medisinske tester.» | Prinsipp 9 og 10 – «benchmarks» uforklart; «oppsiktsvekkende» er unødvendig vurderende. |
| 6 | «Googles Med-PaLM 2 oppnådde i 2023 resultater på nivå med ekspertnivå på den amerikanske medisinske lisensieringseksamen (USMLE).» | «Googles språkmodell Med-PaLM 2 oppnådde i 2023 resultater på ekspertnivå på den amerikanske legeeksamenen USMLE (United States Medical Licensing Examination).» | Prinsipp 9 – verken Med-PaLM 2 eller USMLE forklares. |
| 6 | Overskrift: «Living guidelines-bevegelsen» | «Levende retningslinjer: kontinuerlig oppdatering i stedet for periodisk revisjon» | Prinsipp 3 og 9 – begrepet forklares først i avsnittet under, ikke i overskriften. |
| 6 | «Australia har vært en pioner innen «living guidelines» – retningslinjer som oppdateres kontinuerlig i stedet for periodisk.» | «Australia har vært en pioner innen levende retningslinjer (løpende oppdaterte retningslinjer, på engelsk «living guidelines») – retningslinjer som oppdateres fortløpende i stedet for på faste tidspunkt.» | Prinsipp 9 – introduser norsk term siden begrepet brukes gjentatte ganger senere. |
| 8 | «5. Sentral infrastruktur som forutsetning: Land med mer sentralisert helsedata-infrastruktur (Finland, Danmark) har bedre forutsetninger for KI-anvendelser.» | «5. Sentral infrastruktur gir bedre forutsetninger: Land med mer sentralisert helsedata-infrastruktur, som Finland og Danmark, har bedre forutsetninger for å ta i bruk KI.» | Prinsipp 7 – punktoverskrift formuleres som påstand for parallellitet. |
| 8 | «6. Investere i sentral infrastruktur for helsedata som grunnlag for KI-anvendelser, med lærdommer fra Finland og Danmark.» | «6. Invester i sentral infrastruktur for helsedata, med lærdom fra Finland og Danmark, som grunnlag for KI-bruk.» | Prinsipp 4 – de øvrige punktene bruker imperativ; punkt 6 bryter mønsteret med infinitiv. |
| 4 | «Cochrane, som er den ledende internasjonale aktøren for produksjon av systematiske oversikter, har igangsatt flere pilotprosjekter for å undersøke hvordan KI kan effektivisere oversiktsprosessen.» | «Cochrane er den ledende internasjonale aktøren for systematiske oversikter. Organisasjonen har satt i gang flere pilotprosjekter for å undersøke hvordan KI kan effektivisere oversiktsarbeidet.» | Prinsipp 5 – innskutt relativsetning mellom subjekt og verb; splitting bedrer flyten. |
| 5 | «Danmark har kommet relativt langt med sentral infrastruktur for helsedata (Sundhedsdatanettet), noe som gir et bedre grunnlag for KI-anvendelser enn i mer fragmenterte systemer.» | «Danmark har kommet relativt langt med sentral infrastruktur for helsedata (Sundhedsdatanettet). Dette gir et bedre grunnlag for KI-bruk enn i mer fragmenterte systemer.» | Prinsipp 5 – «noe som»-konstruksjonen deles opp. |
| 3 | «ESF klassifiserer digitale helseteknologier i funksjonskategorier med tilhørende krav til evidens.» | «ESF deler digitale helseteknologier inn i funksjonskategorier, med ulike krav til evidens for hver kategori.» | Prinsipp 6/7 – tydeliggjør hvem som gjør hva mot hva. |

**Samlet vurdering: Godt.** Strukturert, i hovedsak aktiv, korte lesbare setninger. Viktigste forbedring: forklar sentrale faguttrykk og forkortelser ved første bruk, og gjør punktlisten i kapittel 8 og enkelte overskrifter konsekvent norske og parallelt oppbygd.

## 10. Delrapport 7 — Samlet vurdering

### Overordnet evaluering

- **Målgruppe og struktur**: Ledersammendraget følger i hovedsak omvendt pyramide, men anbefalingen kommer etter to lange bakgrunnsavsnitt og en funn-seksjon på over 300 ord – konklusjonen bør ligge tettere på toppen. Kapitlet ellers har informative overskrifter og tabeller som gjør teksten skannbar.
- **Flyt og setningslengde**: Enkelte setninger er svært lange med flere innskutte leddsetninger (kap. 4.2, 7.1) og krever gjenlesing.
- **Substantivsyke er gjennomgående**: «foreldelse av kunnskapsgrunnlaget», «kapasitetsbegrensning for systematiske oversikter», «tap av tillit», «regulatorisk etterslep» går igjen og gjør setninger tunge og upersonlige.
- **Passiv/usynlig avsender** på sentrale steder («Rapporten følger prinsippet om...», «Det anbefales...») der aktør kunne vært synliggjort – særlig viktig i et dokument der beslutningstakere skal vite hvem som anbefaler hva.
- **Faguttrykk forklares ujevnt**: MECE, RAG, DPIA, EPJ, R1–R6 og «living guidelines» brukes uten forklaring ved første forekomst i kapittel 1 og 4.
- **Ledersammendraget spesifikt**: Handlingsorientert med riktige elementer, men lengre enn typisk lederformat (ca. 500 ord) og med tung syntaks der en enklere oppramsing ville løftet lesbarheten.

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| 1 | «Utredningen er motivert av tre samtidige utviklingstrekk: (1) forskningsproduksjonen øker eksponentielt og overgår kapasiteten for manuell bearbeiding, (2) innbyggere i økende grad søker helseinformasjon fra kommersielle KI-tjenester uten kvalitetssikring, og (3) nye regulatoriske rammer gjennom EU AI Act og EHDS stiller krav til digital modenhet.» | «Utredningen er motivert av tre utviklingstrekk. For det første øker forskningsproduksjonen raskere enn vi klarer å bearbeide den manuelt. For det andre søker stadig flere innbyggere helseinformasjon fra kommersielle KI-tjenester uten kvalitetssikring. For det tredje stiller EU AI Act og EHDS (forordningen om det europeiske helsedataområdet) nye krav til digital modenhet.» | Prinsipp 5 – lang periode splittes i fire setninger; prinsipp 9 – EHDS forklares. |
| 1 | «De tre mest alvorlige flaskehalsene er foreldelse av kunnskapsgrunnlaget underveis i retningslinjeprosessen, kapasitetsbegrensning for systematiske oversikter, og manglende kobling mellom retningslinjer og innbyggerinformasjon» | «De tre mest alvorlige flaskehalsene er at kunnskapsgrunnlaget blir foreldet mens retningslinjeprosessen pågår, at kapasiteten for systematiske oversikter er for lav, og at retningslinjer ikke kobles til innbyggerinformasjon.» | Prinsipp 7 – nominaliseringer omskrives til verb/setninger. |
| 1 | «Rapporten følger prinsippet om at tallanslag uten dokumentert kildegrunnlag ikke gjengis.» | «Vi gjengir ikke tallanslag som mangler dokumentert kildegrunnlag.» | Prinsipp 6 – synliggjør avsender. |
| 2.1 | «Utredningen har som formål å vurdere hvordan verdikjeden for kunnskapsforvaltning i helsesektoren kan moderniseres for å sikre at innbyggere og helsepersonell får tilgang til oppdatert, kvalitetssikret helseinformasjon innenfor akseptable tidsrammer.» | «Formålet med utredningen er å vurdere hvordan vi kan modernisere verdikjeden for kunnskapsforvaltning i helsesektoren, slik at innbyggere og helsepersonell får oppdatert og kvalitetssikret helseinformasjon raskt nok.» | Prinsipp 5 – 36-ords setning brytes ned. |
| 3 | «Konsekvensene er utdaterte helseråd, at innbyggere søker alternative kilder med variabel kvalitet, og et økende gap mellom tilgjengelig og formidlet kunnskap.» | «Konsekvensene er at helserådene blir utdaterte, at innbyggere søker til alternative kilder med varierende kvalitet, og at gapet mellom tilgjengelig og formidlet kunnskap øker.» | Prinsipp 4 – parallell oppbygning i oppramsingen. |
| 4.2 | «De er formulert som en gjensidig utelukkende og samlet uttømmende (MECE) oppsummering av de seks dimensjonene i utfordringsbildet (delrapport 2 kap. 2.3)» | «Egenskapene er formulert etter MECE-prinsippet (Mutually Exclusive, Collectively Exhaustive) – det vil si at kategoriene ikke overlapper, og at de til sammen dekker alle de seks dimensjonene i utfordringsbildet (delrapport 2 kap. 2.3).» | Prinsipp 9 – MECE forklares og norskes. |
| 4.2 | «Styrbarhet: Ingen aktør kan styre kjeden som helhet mot et felles mål; ansvar er fordelt uten helhetlig mandat, og ingen eier implementeringsgapet.» | «Styrbarhet: Ingen aktør styrer kjeden som helhet mot et felles mål. Ansvaret er fordelt uten et samlet mandat, og ingen har eierskap til implementeringsgapet.» | Prinsipp 5 – semikolon-konstruksjon splittes. |
| 4.4 | «Forankring av en løsning forutsetter først enighet om dimensjonene i løsningsrommet.» | «Før vi kan forankre en løsning, må vi bli enige om dimensjonene i løsningsrommet.» | Prinsipp 6/7 – nominalisering omskrives til aktive verb. |
| 5.4 | «Sammenligningen i dp4 kap. 6 måler alternativene på operasjonelle og kvalitative dimensjoner (tid, kostnad, kvalitet, risiko, EHDS-samsvar osv.).» | «I delrapport 4, kapittel 6, sammenligner vi alternativene på operasjonelle og kvalitative dimensjoner: tid, kostnad, kvalitet, risiko og EHDS-samsvar.» | Prinsipp 8 – «dp4» skrives ut i løpende tekst. |
| 6.1 | «Det anbefales en faseinndelt innføring av KI-støttet kunnskapsforvaltning der alternativ 2 (moderat KI-støtte) implementeres som startpunkt, med gradvis utvidelse mot elementer fra alternativ 3 etter hvert som teknologi, kompetanse og governance modnes.» | «Vi anbefaler en faseinndelt innføring av KI-støttet kunnskapsforvaltning. Alternativ 2 (moderat KI-støtte) er startpunktet, og innføringen utvides gradvis mot elementer fra alternativ 3 etter hvert som teknologi, kompetanse og styringsmodell (governance) modnes.» | Prinsipp 6 og 5 – «det anbefales» gjøres aktiv; 45-ords setning deles i to. |
| 6.6 pkt. 4 | «Regulatorisk proaktivitet der Helsedirektoratet tar en ledende rolle i å operasjonalisere EU AI Act for helsesektoren» | «Regulatorisk pådriverrolle: Helsedirektoratet går foran og setter EU AI Act i praktisk drift for helsesektoren» | Prinsipp 7/8 – «operasjonalisere» er tung fagsjargong. |
| 7 | «Tabellen nedenfor oppsummerer de ti viktigste risikoene for KI-støttet kunnskapsforvaltning, med vurdering av sannsynlighet, konsekvens og foreslåtte mitigeringstiltak.» | «Tabellen under viser de ti viktigste risikoene for KI-støttet kunnskapsforvaltning, med sannsynlighet, konsekvens og forslag til tiltak (mitigering).» | Prinsipp 9 – «mitigeringstiltak» er ikke innarbeidet norsk. |
| 7.1 | «Delrapport 9 (Fremtidsscenarioer) identifiserer i tillegg en annen risikotype: scenariorisiko – risikoen for at hele systemet driver mot en uønsket strukturell tilstand, uavhengig av hvor godt det enkelte tiltaket gjennomføres» | «Delrapport 9 (Fremtidsscenarioer) peker på en annen risikotype: scenariorisiko. Dette er risikoen for at hele systemet driver mot en uønsket tilstand, uavhengig av hvor godt det enkelte tiltaket gjennomføres.» | Prinsipp 5 – kolon-setning med innskutt definisjon deles i to. |
| 9, Krav 6 | «Følgende juridiske avklaringer og potensielle endringer er identifisert som forutsetninger» | «Vi har identifisert følgende juridiske avklaringer og mulige endringer som forutsetninger» | Prinsipp 6 – passiv gjøres aktiv. |
| 10.3 | «KI-teknologi representerer en mulighet til å adressere disse utfordringene uten å undergrave kvalitetssikringen.» | «KI-teknologi kan løse disse utfordringene uten å svekke kvalitetssikringen.» | Prinsipp 7/8 – omstendelig substantivsyke/anglisisme erstattes med direkte verb. |

**Samlet vurdering: Middels.** God overordnet struktur, men gjennomgående substantivsyke, enkelte for lange setninger og usynlig avsender trekker ned. Viktigste forbedring: omskriv de mest brukte substantivsyke-konstruksjonene («foreldelse av», «manglende kobling mellom», «det anbefales») til aktive verbsetninger med synlig avsender.

## 11. Delrapport 8 — Aktøranalyse

### Overordnet evaluering

- **Målgruppe og struktur**: Systematisk kartlegging med logisk og forutsigbar struktur (aktørkart → tverrgående observasjoner → IGOE-analyse). Konklusjonene i kapittel 4 og 5.3 kommer sent – akseptabelt for et oppslagsverk, men en ulempe for lesere som vil ha hovedfunnene raskt.
- **Flyt og setningslengde**: Aktørbeskrivelsene (kap. 2) er korte og greie. IGOE-analysen (kap. 5.2) er derimot tung: «Guides»-feltene pakker fire–fem selvstendige opplysninger inn i én løpende tekstblokk.
- **Mønstre å forbedre**: Gjennomgående passiv og upersonlig form uten synlig avsender («er organisert etter», «leveres av», «finnes ingen mekanisme»), spesielt merkbart i observasjonene i kapittel 4 og 5.3.
- **Faguttrykk**: IDEF0, GRADE, EMA, FEST, SPC, DRUID/Apriori, KUPP introduseres uten forklaring ved første bruk.
- **Skannbarhet i IGOE-delen**: «Guides»-beskrivelsene ville vært vesentlig mer skannbare som punktlister – det mest gjennomgående strukturelle forbedringspotensialet i rapporten.

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| 1.1 | «Aktøranalysen er skilt ut som egen delrapport for å gi en helhetlig fremstilling av roller, ansvar og relasjoner...» | «Vi har skilt ut aktøranalysen som egen delrapport for å gi en helhetlig fremstilling av roller, ansvar og relasjoner...» | Prinsipp 6 – aktiv form, synlig avsender. |
| 2 | «Aktørene er organisert etter hvilken strøm de primært tilhører.» | «Vi organiserer aktørene etter hvilken strøm de primært tilhører.» | Prinsipp 6 – usynlig avsender gjøres synlig. |
| 2.8 | «Tjenesten er under gjenoppbygging etter en periode med nedleggelse [4].» | «Helsebiblioteket bygger nå opp tjenesten igjen etter at den ble lagt ned en periode [4].» | Prinsipp 6 – hvem som gjenoppbygger er uklart i originalen. |
| 2.14 | «Innholdet leveres av offentlige helseaktører (sykehus, Helsedirektoratet, Helfo, FHI m.fl.) og skal være forskningsbasert...» | «Offentlige helseaktører (sykehus, Helsedirektoratet, Helfo, FHI m.fl.) leverer innholdet, som skal være forskningsbasert...» | Prinsipp 6 – aktiv form fremfor passiv. |
| 4 (pkt. 1) | «Ansvaret er fordelt på nærmere 20 aktører uten et overordnet system som sikrer konsistens på tvers.» | «Nærmere 20 aktører deler ansvaret, uten at noe overordnet system sikrer konsistens på tvers.» | Prinsipp 6 – aktiv form. |
| 5.1 | «Rammeverket er en videreføring av IDEF0-metodikken, tilpasset tjenestebaserte virksomheter.» | «Rammeverket bygger på IDEF0-metodikken (en etablert metode for prosessmodellering), tilpasset tjenestebaserte virksomheter.» | Prinsipp 9 – faguttrykk forklart ved første bruk. |
| 5.2, prosess 1 | «Metode: GRADE-metodikk, Cochrane Handbook, systematisk oversiktsmetodikk. Rammer: Helseforskningsloven, forskningsetiske retningslinjer, FHIs mandat.» | «Metode: GRADE-metodikk (system for å vurdere kvaliteten på forskningsbasert kunnskap), Cochrane Handbook og systematisk oversiktsmetodikk. / Rammer: Helseforskningsloven, forskningsetiske retningslinjer og FHIs mandat.» (egne linjer) | Prinsipp 9 og 3–4 – forklar GRADE; del opp i egne linjer for skumlesing. |
| 5.2, prosess 5 | «Rammer: Legemiddelloven, EU-regulering (EMA-prosedyrer), ICH-retningslinjer, SPC-standarder, produsentuavhengighetsprinsippet.» | «Rammer: legemiddelloven, EU-regulering gjennom EMA (Det europeiske legemiddelbyrået), ICH-retningslinjer og SPC-standarder (standarder for godkjente preparatomtaler), samt prinsippet om produsentuavhengighet.» | Prinsipp 9 – EMA og SPC brukes uten forklaring. |
| 5.2, prosess 1 | «Utløsende hendelse: … Metode: … Rammer: … Avsluttende hendelse: …» (én sammenhengende tekstblokk) | Samme innhold som punktliste med én linje per element (Utløsende hendelse / Metode / Rammer / Avsluttende hendelse). | Prinsipp 3–4 – punktlister gjør tett informasjon skannbar. |
| 5.2, prosess 6 | «Rammer: Helsedirektoratets utgiveransvar, kvalitetsretningslinjer, klarspråkstandard (språkloven paragraf 9), personvernregelverk, smittevernloven, presseetiske retningslinjer (Vær Varsom-plakaten), redaksjonell uavhengighet.» | Punktliste: «– Helsedirektoratets utgiveransvar og kvalitetsretningslinjer / – Klarspråkstandard (språkloven § 9) / – Personvernregelverk og smittevernloven / – Presseetiske retningslinjer (Vær Varsom-plakaten) / – Redaksjonell uavhengighet» | Prinsipp 3–4 – kommaoppramsing på sju ledd gjøres skannbar. |
| 5.3, pkt. 3 | «I dag finnes ingen systematisk mekanisme som sikrer at alle prosessene oppdaterer sin praksis når felles guides endres.» | «I dag mangler verdikjeden en systematisk mekanisme som sikrer at alle prosessene oppdaterer praksisen sin når felles guides endres.» | Prinsipp 6 – «det finnes» erstattes med konkret subjekt. |
| 5.3, pkt. 7 | «Det finnes ingen formell prosess der output fra prosess 3 (erfaring fra implementering) systematisk tilbakeføres som input til prosess 2 (retningslinjerevisjon).» | «Verdikjeden mangler en formell prosess for å tilbakeføre erfaring fra implementering (prosess 3) systematisk som grunnlag for retningslinjerevisjon (prosess 2).» | Prinsipp 6–7 – aktiv form og fjernet substantivsyke. |
| 2.9 | «Sykepleien Forskning er nivå 1-tidsskrift utgitt av NSF [8].» | «NSF gir ut Sykepleien Forskning, som er et nivå 1-tidsskrift [8].» | Prinsipp 6 – avsender (NSF) gjøres synlig som subjekt. |

**Samlet vurdering: Middels.** Hovedsvakheten er den komprimerte «Guides»-strukturen i IGOE-analysen (kap. 5.2), som bør brytes opp i punktlister, kombinert med gjennomgående passiv/usynlig avsender i observasjonskapitlene og noen uforklarte faguttrykk.

## 12. Delrapport 9 — Fremtidsscenarioer

### Overordnet evaluering

- **Målgruppe og struktur**: God grunnstruktur – konklusjon kommer tidlig (kap. 1), og [DOK]/[ANT]-merkingen fungerer godt som kildedisiplin. Overskriftene er informative nok til å følge argumentasjonen ved skumlesing.
- **Flyt og setningslengde**: Gjennomgående problem er svært lange setninger med mange innskutte leddsetninger og parenteser (særlig kap. 3 og 4). Mange setninger passerer 30–40 ord når parentetiske tillegg telles med.
- **Gjentakende mønstre**: Hyppig bruk av doble tankestreker for innskutt informasjon, som gjør at hovedsetningen mister kraft. Flere avsnitt pakker to–tre selvstendige poenger inn i én periode adskilt med semikolon.
- **Faguttrykk**: Sentrale begreper («orkestrering», «generativitet», «scenariokors», «kollapsbane», «dominator»-rollen) brukes gjennomgående uten kort forklaring ved første bruk, selv om de er bærende for argumentasjonen.
- **Kanselli-/akademisk stil**: Enkelte formuleringer er unødig tunge («i sin natur», «i praksis et bestemt sett posisjoner»).

### Konkrete eksempler

| Kap. | Opprinnelig formulering | Klarspråksversjon | Begrunnelse (prinsipp) |
|---|---|---|---|
| 2.1 | «Utredningen kan ikke vite hvordan KI-landskapet i helsesektoren ser ut om fem til ti år. Den kan derimot identifisere de kritiske usikkerhetene som vil forme det, og beskrive konsistente fremtidsbilder for ulike kombinasjoner av dem.» | «Vi kan ikke vite hvordan KI-landskapet i helsesektoren ser ut om fem til ti år. Men vi kan identifisere de kritiske usikkerhetene som vil forme det, og beskrive konsistente fremtidsbilder for dem.» | Prinsipp 6 – «Utredningen» som subjekt gjør avsenderen upersonlig. |
| 3.4 | «Hver løsning er rasjonell lokalt, men summen er fragmentering: ulik kvalitetssikring, ulike svar på samme spørsmål, dobbeltarbeid og uklart ansvar når noe går galt» | «Hver løsning er rasjonell lokalt. Men summen blir fragmentering – ulik kvalitetssikring, ulike svar på samme spørsmål, dobbeltarbeid og uklart ansvar når noe går galt.» | Prinsipp 5 – kolon-setning med fire sammenkjedede fraser splittes. |
| 3.1 | «Kommuner og helseforetak konsumerer fra den sentrale motoren fremfor å bygge egne.» | «Kommuner og helseforetak bruker den sentrale motoren i stedet for å bygge egne løsninger.» | Prinsipp 9/10 – «konsumerer» er unødvendig anglisisme. |
| 5.2 | «Hovedfunnet for delrapport 4: valget står ikke bare mellom alternativene, men om de utformes for å orkestrere et økosystem (S3) eller bare bygge en sentral motor (S1).» | «Hovedfunnet for delrapport 4 er dette: Valget står ikke bare mellom alternativene. Det avgjørende er om alternativene utformes for å orkestrere et økosystem (S3), eller om de bare bygger en sentral motor (S1).» | Prinsipp 5 og 2 – kolon-konstruksjonen skjuler konklusjonen. |
| 2.2 | «Dette er aksen økosystemnotatet reiser som «orkestrering vs. kontroll» [...], og den treffer R1 og kjerneegenskapen tillit/legitimitet.» | «Dette er samme akse som økosystemnotatet omtaler som «orkestrering vs. kontroll» [...]. Aksen påvirker R1 (styringsmandat) og kjerneegenskapen tillit/legitimitet.» | Prinsipp 5 – to ulike poenger splittes; R1 forklares. |
| Innledning | «Planen er ikke en prediksjon, men gir et eksplisitt politisk signal om retning i scenariokorset: regjeringen varsler en offentlig orkestrert linje med kjøp i markedet [...] og en «nasjonal infrastruktur for kunnskapsformidling» [...] – en bevegelse mot S1 [...] / S3 [...].» | «Planen er ikke en prediksjon. Den gir et politisk signal om retning: Regjeringen varsler en offentlig orkestrert linje med kjøp i markedet [...] og en «nasjonal infrastruktur for kunnskapsformidling» [...]. Signalet peker mot S1 (Nasjonal motor) eller S3 (Føderert økosystem).» | Prinsipp 5 – over 60 ord med kolon, to sitater og skråstrek-notasjon splittes i tre setninger. |
| 2.3 | «Det opprinnelige bekymringsscenarioet – at kommuner og helseforetak bygger egne løsninger tett opp mot det sentrale mandatet – lever i sin rene form i S4, og i en styrt og konstruktiv form i S3.» | «Det opprinnelige bekymringsscenarioet er at kommuner og helseforetak bygger egne løsninger tett opp mot det sentrale mandatet. Dette scenarioet finnes i ren form i S4, og i en styrt og konstruktiv form i S3.» | Prinsipp 5 – langt innskudd mellom subjekt og verb. |
| 3.2 | «Disse blir de facto standard fordi de er tilgjengelige der arbeidet og søket faktisk skjer» | «Disse løsningene blir en uformell standard («de facto standard») fordi de er tilgjengelige der arbeidet og søket faktisk skjer.» | Prinsipp 9 – «de facto standard» forklares ved første bruk. |
| 3.3 | «Det offentlige orkestrerer fremfor å kontrollere: det gjør sitt tilbud så åpent og gjenbrukbart at andre velger å bygge på det» | «Det offentlige orkestrerer i stedet for å kontrollere. Det betyr at det offentlige gjør sitt tilbud så åpent og gjenbrukbart at andre velger å bygge videre på det.» | Prinsipp 9/5 – «orkestrerer» er bærende, men uforklart begrep; første forekomst bør forklares. |
| 4.2 | «S1 er altså ikke selvbærende uten reaktivitet og mandat.» | «S1 er altså avhengig av at løsningen er reaktiv og har et tydelig mandat – ellers er den ikke selvbærende.» | Prinsipp 7 – komprimert, kryptisk formulering skrives ut. |
| 4.3 | «Scenariokorset gjør dermed synlig hva delrapport 4 allerede konkluderte kvalitativt: nullalternativet er ikke bærekraftig – men det viser i tillegg hvilke konkrete baner passivitet leder til.» | «Scenariokorset bekrefter det delrapport 4 allerede konkluderte: Nullalternativet er ikke bærekraftig. I tillegg viser scenariokorset hvilke konkrete baner passivitet fører til.» | Prinsipp 5 – kolon + tankestrek i samme setning splittes i tre korte. |
| 6, pkt. 1 | «Orkestrering bør være et eksplisitt designkrav, ikke en ettertanke.» | «Orkestrering bør være et krav fra starten av arkitekturarbeidet – ikke noe som legges til i etterkant.» | Prinsipp 9/10 – «ettertanke» som forvaltningsmetafor er upresis. |
| 3.1 | «Helsedirektoratet eier strategi og takt; NHN drifter» | «Helsedirektoratet eier strategien og bestemmer tempoet. NHN drifter løsningen.» | Prinsipp 5 – telegramaktig semikolon-setning; «drifter» mangler objekt. |
| 8 | «Denne litteraturen er anvendt analytisk [ANT]; den er ikke en empirisk kilde om norsk helsesektor.» | «Denne litteraturen er brukt analytisk, altså som metodegrunnlag [ANT]. Den er ikke en empirisk kilde om norsk helsesektor.» | Prinsipp 6/7 – «anvendt analytisk» er tungt; semikolon erstattes med punktum. |

**Samlet vurdering: Middels.** Strukturen og kildedisiplinen er solid, men gjennomgående lange, innskutte setninger med tankestreker/kolon og uforklarte nøkkelbegreper («orkestrering», «de facto standard», «kollapsbane») er den viktigste forbedringen.
