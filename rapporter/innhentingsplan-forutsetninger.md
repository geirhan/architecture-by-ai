# Innhentingsplan for verifisering av forutsetninger

**Status**: Under arbeid — internt arbeidsdokument
**Sist oppdatert**: 2026-08-18

## Formål og bruk

Denne planen operasjonaliserer de prioriterte
verifiseringene fra
[forutsetningsanalysen](forutsetningsanalyse-rammeniva.md)
(kap. 6) og
[antakelsesregisteret](antakelsesregister.md) (kap. 3).
For hvert punkt angis: spørsmålet, mottaker eller kilde,
hva som hviler på svaret, utkast til henvendelse (der det
trengs), og hva som skjer med utredningen ved ulike svar.

Hvert punkt har et statusfelt som oppdateres underveis:
*Ikke startet → Sendt/igangsatt → Svar mottatt →
Innarbeidet*. Arbeidsdelingen er markert per punkt:
**[Du]** krever formell avsender, tilgang eller intern
beslutning; **[Claude]** kan utføres i en arbeidsøkt uten
nye tilganger.

Anbefalt rekkefølge: send henvendelsene (punkt 1, 3, 4)
og avklar API-tilgangen (punkt 6) først — de har ledetid.
De åpne sveipene (punkt 2 og deler av punkt 1) kan kjøres
parallelt. Punkt 5 er den billigste enkelthandlingen og
kan gjøres i dag.

## Oversikt

| # | Punkt | Bærer | Ansvar | Status |
|---|---|---|---|---|
| 1 | KI-initiativ i kommuner og helseforetak | Drift-tesen, nullalternativvurderingen | Du + Claude | Ikke startet |
| 2 | Kommersielle aktørers tilgang til offentlige kilder | Drift-tesen (S2-vurderingen) | Claude + du (policy) | Ikke startet |
| 3 | Etterspørsels- og bruksdata | Konkurranseargumentet, tempopremisset, blindsone­punkt 2 | Du | Ikke startet |
| 4 | Forrangsregler og koordinering stat/forening | K10/K19, risiko 14, R1-utvidelsen | Du | Ikke startet |
| 5 | Sende FHI-svardokumentet | Åpner kanal for flere verifiseringer | Du | Ikke startet |
| 6 | API-verifisering av PICO-innhold | R2-presiseringen, K6.1-vurderingen | Du (tilgang) + Claude | Parkert (401) |
| 7 | Juridisk utredning AI Act/MDR | Arkitekturvalg, cluster 3 | Du (bestilling) | Ikke startet |
| 8 | Restliste: mindre verifiseringer | Enkeltvurderinger | Mest Claude | Ikke startet |

---

## 1. KI-initiativ i kommuner og helseforetak

**Spørsmål**: Finnes det faktiske, pågående initiativ i
kommuner og helseforetak for å bygge eller anskaffe egne
KI-løsninger for kunnskapsstøtte/helseinformasjon?

**Hva som hviler på svaret**: Drift-tesen — premisset om
at passivitet gir fragmentering (S4) — er «plausibel
slutning, ikke dokumentert kartlegging»
([delrapport 9 kap. 7](fremtidsscenarioer.md#7-forbehold-og-kunnskapsgap)).
Dette er enkeltverifiseringen med størst avkastning i
utredningen (antakelsesregisterets cluster 1).

**[Claude] Åpent sveip først**: Doffin-kunngjøringer,
RHF-enes styresaker, KS-rapporter og mediedekning, slik
at henvendelsene kan vise til konkrete funn og bli
lettere å svare på.

**[Du] Henvendelser**: én til KS (e-helseområdet), én til
hver av de fire RHF-enes IKT-/innovasjonsmiljøer, og
internt spørsmål til Hdir-rådgivere med sektordialog.

**Utkast til henvendelse**:

> Helsedirektoratet utreder fremtidig organisering av
> kunnskapsforvaltningen i helsesektoren. Et sentralt
> usikkerhetsmoment er om kommuner/helseforetak i dag
> planlegger eller har igangsatt egne KI-løsninger for
> kunnskapsstøtte eller helseinformasjon (f.eks.
> KI-assistenter mot egne eller eksterne kunnskapskilder).
> Kjenner dere til slike initiativ i deres
> region/medlemsmasse? Både konkrete prosjekter,
> anskaffelser under planlegging og «nei, ikke som vi
> kjenner til» er nyttige svar. Kort svar per e-post er
> tilstrekkelig.

**Ved svar**: Flere konkrete initiativ → drift-tesen
oppgraderes mot [DOK], hastverksargumentet styrkes.
Dokumentert fravær → nullalternativvurderingen i
[delrapport 4 kap. 2.5](ny-verdikjede.md) og
scenariorisikoene i
[delrapport 7 kap. 7.1](samlet-vurdering-kunnskapsforvaltning.md#71-scenariorisiko--strukturelle-utviklingsbaner)
må dempes, og «vent og se» styrkes som rasjonell
mulighet.

**Status**: Ikke startet

## 2. Kommersielle aktørers tilgang til offentlige kilder

**Spørsmål**: Kan kommersielle aktører (EPJ-leverandører,
KI-tjenester) rettslig og teknisk bygge på
Helsedirektoratets API-er, Helsenorge-innholdet og
Helsebiblioteket — og ønsker Helsedirektoratet det?

**Hva som hviler på svaret**: Det nye drift-premisset (b)
fra forutsetningsanalysen: hvis kommersielle aktører kan
kvalitetssikre mot norske offentlige kilder, blir
S2-scenarioet langt mindre skadelig, og skillet S2/S3 en
gradsforskjell. Berører også generativitetsargumentet i
[økosystemnotatet kap. 4.3](verdikjede-som-okosystem.md#43-generativitet-og-ehds).

**[Claude]**: Gjennomgå bruksvilkår, lisenser og teknisk
tilgjengelighet for de tre kildene; dokumentere hva som
faktisk er åpent i dag.

**[Du]**: Policyavklaringen — om kommersiell gjenbruk er
ønsket strategi — er en intern diskusjon som bør løftes i
prosjektet; funnene fra sveipet er underlaget.

**Ved svar**: Åpent + ønsket → S2-beskrivelsen i
[delrapport 9](fremtidsscenarioer.md) nyanseres og
generativitetsstrategien styrkes som alternativ til egen
kanal. Lukket/uavklart → dagens S2-vurdering står, men
får dokumentert grunnlag.

**Status**: Ikke startet

## 3. Etterspørsels- og bruksdata

**Spørsmål**: Hvor henter innbyggere og helsepersonell
faktisk helsekunnskap i dag — og hvor stor andel går til
kilder utenfor den offentlige kjeden?

**Hva som hviler på svaret**: Konkurranseargumentet kan i
dag ikke tallfestes (økosystemnotatet kap. 7); hele
etterspørselssiden er blindsone­punkt 2 i
[forutsetningsanalysen](forutsetningsanalyse-rammeniva.md)
(kap. 6). Svaret påvirker både problemets
alvorlighetsgrad og valget mellom egen kanal og
generativitet.

**[Du] To spor**:

1. **Helsenorge-statistikk fra NHN**: søkeord, trafikk,
   mest brukte sider, utvikling over tid. Intern
   henvendelse; NHN har tallene.
2. **Befolkningsdata**: vurder å kjøpe inn 2–3 spørsmål i
   en løpende undersøkelse (f.eks. Helsepolitisk
   barometer) om hvor innbyggere henter helseinformasjon,
   med KI-tjenester som eksplisitt svaralternativ. Dette
   er også punkt 6 («innbyggerundersøkelse») i
   [delrapport 7 kap. 10.2](samlet-vurdering-kunnskapsforvaltning.md#102-behov-for-videre-arbeid).

**Utkast til henvendelse (NHN)**:

> I forbindelse med utredningen av ny verdikjede for
> kunnskapsforvaltning trenger vi et bilde av faktisk
> bruk av Helsenorge som kunnskapskilde: trafikk- og
> søkestatistikk for helseinformasjonssidene (gjerne de
> siste 3–5 år), mest besøkte temaer, og eventuelle data
> om henvisningskilder. Har dere en standardrapport, eller
> kan et uttrekk bestilles?

**Ved svar**: Høy og stabil bruk → «taper terreng»-
argumentet svekkes og må presiseres. Lav/fallende bruk →
konkurranseargumentet får empiri og kan oppgraderes til
[DOK].

**Status**: Ikke startet

## 4. Forrangsregler og koordinering stat/forening

**Spørsmål**: Finnes det noen formell koordinering,
konsultasjonsordning eller forrangsregel mellom nasjonale
faglige retningslinjer og profesjonsforeningenes
veiledere?

**Hva som hviler på svaret**: K10/K19-vurderingene i
[kapabilitetskartet](kapabilitetskart-verdikjeden.md),
R1-utvidelsen i
[delrapport 2 kap. 9.2](utfordringer-og-flaskehalser.md#92-seks-rotårsaker)
og risiko 14 i
[delrapport 7](samlet-vurdering-kunnskapsforvaltning.md#7-risikomatrise).
Dette er et fraværsfunn (cluster 6) — metodisk skjørt til
det er bekreftet av dem som ville visst det.

**[Du] To henvendelser**: internt til
retningslinjemiljøet i Hdir, og eksternt til
Legeforeningen (fagmedisinsk avdeling). Kan også stilles
muntlig i møter som likevel skjer — noter i så fall dato
og kilde.

**Utkast til henvendelse (Legeforeningen)**:

> Helsedirektoratet kartlegger samspillet mellom
> nasjonale faglige retningslinjer og fagmedisinske
> foreningers veiledere. Finnes det i dag noen formell
> eller uformell ordning for koordinering mellom sporene
> — f.eks. gjensidig konsultasjon ved revisjon, omforent
> praksis for hva som gjelder ved motstrid, eller
> etablerte kontaktpunkter? Vi er også interessert i om
> foreningene selv opplever behov for en slik ordning.

**Ved svar**: Ordninger finnes → K10-vurderingen
oppjusteres og «uformelle forbindelser»-diagnosen
nyanseres. Bekreftet fravær → fraværsfunnet oppgraderes
til [DOK] og veivalgs­drøftingen i
[delrapport 4 kap. 6.3](ny-verdikjede.md) styrkes.

**Status**: Ikke startet

## 5. Sende FHI-svardokumentet

**Hva**: [Svardokumentet til Kim Kristoffer
Dysthe](svar-kim-kommentarer.md) har ligget klart som
utkast siden mai, med seks avklaringsspørsmål som
overlapper denne planen (FHIs faktiske kapasitet,
direktebruk av forskning i normerende produkter —
verifiseringspunkt 13 i
[antakelsesregisteret](antakelsesregister.md)).

**[Du]**: Les gjennom utkastet og send det. Dette er den
billigste enkelthandlingen på listen og åpner kanalen som
kan besvare flere av de øvrige punktene.

**Ved svar**: Innarbeides via
[innarbeidingsplanen](innarbeiding-kim-kommentarer.md).

**Status**: Ikke startet

## 6. API-verifisering av PICO-innhold

**Spørsmål**: Inneholder PICO-objektene i
Helsedirektoratets retningslinje-API reelle,
strukturerte data (populasjon, intervensjon, utfall) —
eller er de tomme skall?

**Hva som hviler på svaret**: R2-presiseringen i
[delrapport 2](utfordringer-og-flaskehalser.md#92-seks-rotårsaker),
K6.1-vurderingen («Delvis») og startpunktet for
retning B2 (jf.
[metadatanotatet](metadatastrukturer-evidenskjeden.md)).

**[Du]**: Avklar API-abonnementet internt — nøklene i
vault avvises med 401, og verifiseringen har vært parkert
siden det. Dette er en intern IT-/tilgangssak.

**[Claude]**: Når tilgangen virker, tar selve
verifiseringen under en time (uttrekk og gjennomgang av
PICO-objekter fra 2–3 retningslinjer).

**Status**: Parkert (401) — venter på tilgang

## 7. Juridisk utredning AI Act/MDR

**Hva**: Skillet mellom generisk kunnskapsformidling
(trolig ikke medisinsk utstyr) og pasientspesifikk
beslutningsstøtte (trolig medisinsk utstyr) må avklares
juridisk **før** arkitekturvalg låses
([antakelsesregisterets](antakelsesregister.md)
cluster 3; punkt 2 i
[delrapport 7 kap. 10.2](samlet-vurdering-kunnskapsforvaltning.md#102-behov-for-videre-arbeid)).

**[Du]**: Dette skal ikke innhentes, men **bestilles**:
få utredningen formelt i bestilling hos Hdirs jurister
med DMP som kontaktpunkt for utstyrsspørsmålet. Planens
bidrag er å presisere bestillingen:

> Utred: (1) om en offentlig KI-tjeneste for målrettede
> helseråd til innbyggere faller inn under MDR
> (MDCG 2019-11 Rule 11) og/eller AI Act høyrisiko-
> kategoriene, i tre varianter — generisk formidling,
> målrettet informasjon, individuell beslutningsstøtte;
> (2) hvilke krav AI Act art. 10 (datastyring) stiller
> til kunnskapskorpuset i en RAG-løsning; (3)
> konsekvensene av Kommisjonens kommende Art.
> 6-veiledning for klassifiseringen.

**Status**: Ikke startet

## 8. Restliste: mindre verifiseringer

Fra [antakelsesregisterets](antakelsesregister.md)
verifiseringsliste; lav innsats per punkt.

| Punkt | Metode | Ansvar |
|---|---|---|
| NRF/MAGICapp-koblingen (nedgradert til uverifisert) | Én e-post til Norsk revmatologisk forening eller MAGIC | Du (avsender), Claude (utkast) |
| Fravær av LLM+GRADE-forskning og tidsbesparelse-metaanalyse | Oppdatert systematisk litteratursøk | Claude |
| MAGIC-litteraturens forfatterskapskonsentrasjon | Forfatterskapssjekk av sentrale publikasjoner | Claude |
| Helsenorge-eierskap/driftsansvar presist (Hdir/NHN) | Kildeavklaring, ev. internt spørsmål | Claude, du ved behov |
| NICEs rettslige mandat og kostnadsprofil | Dokumentsøk (UK-lovgivning, NICE-årsrapporter) | Claude |
| Antibiotika-casets tidstall | Finne offentlig kilde, ellers beholde som [ANT] | Claude |
| Sak 13-sakspapiret og 2015-rapportens vedtaksstatus (Legeforeningen) | Hente/lese dokumentene, ev. be Legeforeningen om kopi | Du (tilgang), Claude (lesning) |
| Norsk bruk av RoB 2/AGREE II/COS i praksis | Henvendelse FHI/Hdir metodemiljø (kan kobles til punkt 5) | Du |

**Status**: Ikke startet

---

## Innarbeiding av svar

Når svar foreligger: oppdater statusfeltet her, innarbeid
funnet i de berørte dokumentene med [DOK]-merking og
kilde («opplyst i e-post/møte, dato, avsender» er
tilstrekkelig), og oppdater
[antakelsesregisteret](antakelsesregister.md) og ved
behov premissformuleringene i
[samlet vurdering kap. 2.3](samlet-vurdering-kunnskapsforvaltning.md#23-dette-legger-utredningen-til-grunn).
Be Claude om å gjøre innarbeidingen — denne planen er
skrevet for å kunne hentes frem igjen i en senere økt.
