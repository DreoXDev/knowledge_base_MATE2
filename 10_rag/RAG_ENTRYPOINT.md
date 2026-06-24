# RAG Entrypoint - Matematica 2

Quando una chat AI usa questa repo, deve seguire questo ordine:

1. Capire se la richiesta e':
   - spiegazione teorica;
   - dimostrazione;
   - domanda orale;
   - esercizio;
   - simulazione professore;
   - revisione di una risposta dello studente.

2. Consultare:
   - `10_rag/RAG_THEORY_MAP.md`;
   - `05_theorem_cards/` per teoremi;
   - `06_oral_exam_discourses/` per risposte orali;
   - `09_exam_questions/` per domande e follow-up;
   - `07_exercises/` per esempi.

3. Rispondere in stile orale:
   - preciso;
   - non eccessivamente professorale;
   - con formule corrette;
   - con ipotesi esplicitate;
   - con eventuale intuizione geometrica.

4. Non inventare dimostrazioni se la KB non le contiene.

