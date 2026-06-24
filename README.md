# Knowledge Base Matematica 2

Repository/vault Obsidian per preparare l'esame orale di Matematica 2.

## Obiettivo

Costruire una base di conoscenza affidabile, navigabile e interrogabile per:
- studiare teoria;
- ripassare dimostrazioni;
- preparare discorsi orali;
- esercitarsi con domande classiche;
- simulare l'interrogazione con una chat AI.

## Esame

- Corso: Matematica 2
- Modalita': orale
- Data: 30 giugno
- Focus: teoria, ipotesi, enunciati, dimostrazioni, intuizione geometrica e collegamenti.

## Regola LaTeX

Usare sempre:
- `$...$` per formule inline;
- `$$...$$` per formule a blocco.

Non usare i delimitatori LaTeX con parentesi tonde o quadre nei file Markdown consolidati.

## Fonte primaria

1. PDF ufficiali del professore.
2. Esercizi ufficiali.
3. Appunti personali o di altri studenti, se coerenti.
4. Sintesi consolidate della KB.
5. Inferenze AI, solo se marcate.

## Struttura

- `00_meta/`: panoramica, stato progetto, policy fonti e strategia di studio.
- `01_sources/`: fonti ufficiali e appunti organizzati.
- `02_ingestion_reports/`: report per ogni PDF o batch analizzato.
- `03_transcriptions/`: trascrizioni grezze o pulite delle fonti.
- `04_theory/`: note teoriche consolidate.
- `05_theorem_cards/`: schede dei teoremi con ipotesi, tesi e dimostrazione.
- `06_oral_exam_discourses/`: discorsi pronti per l'orale.
- `07_exercises/`: esercizi, esempi e log degli errori.
- `08_visuals/`: figure, grafici e snippet GeoGebra.
- `09_exam_questions/`: domande classiche e follow-up.
- `10_rag/`: entrypoint e mappe per retrieval AI.
- `AI_Oral_Exam/`: prompt finali per simulazioni orali.
- `templates/`: modelli riutilizzabili.
- `scripts/`: controlli minimi su link e formato matematico.
- `raw_assets/`: asset iniziali non ancora necessariamente analizzati.

## Workflow di studio

1. Parti da `04_theory/00_teoria_index.md`.
2. Apri la theorem card collegata in `05_theorem_cards/`.
3. Ripeti enunciato, ipotesi, tesi e significato geometrico.
4. Se richiesto, ricostruisci la dimostrazione a voce.
5. Passa al discorso in `06_oral_exam_discourses/`.
6. Allenati con `09_exam_questions/domande_classiche.md`.
7. Registra errori ricorrenti in `07_exercises/error_log.md` o nei log di sessione.

## Workflow AI/RAG

Una chat AI deve partire da:
1. `AI_CONTEXT.md`
2. `10_rag/RAG_ENTRYPOINT.md`
3. `10_rag/RAG_THEORY_MAP.md`
4. `05_theorem_cards/`
5. `06_oral_exam_discourses/`
6. `09_exam_questions/`

La chat deve segnalare fonti mancanti e non inventare dimostrazioni non presenti nella KB.

## Workflow futuro di ingest PDF

1. L'utente manda un PDF alla chat.
2. La chat analizza il PDF.
3. La chat produce un piano Codex specifico per aggiornare la repo.
4. Codex applica il piano:
   - copia fonte in `01_sources/`;
   - crea ingestion report;
   - aggiorna theory notes;
   - aggiorna theorem cards;
   - aggiorna oral discourses;
   - aggiorna RAG index;
   - estrae o registra figure utili;
   - aggiorna domande orali.
5. La repo viene controllata con:
   - link check;
   - math format check;
   - TODO scan.
