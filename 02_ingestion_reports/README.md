# Ingestion Reports

Ogni PDF o piccolo batch di fonti deve avere un report prima di aggiornare la teoria consolidata.

## Workflow

1. L'utente manda o indica un PDF.
2. La chat analizza il file.
3. La chat produce un piano specifico.
4. Codex applica il piano:
   - copia fonte in `01_sources/`;
   - crea ingestion report;
   - aggiorna theory notes;
   - aggiorna theorem cards;
   - aggiorna oral discourses;
   - aggiorna RAG index;
   - estrae o registra figure utili;
   - aggiorna domande orali.
5. Eseguire i controlli:
   - `python scripts/check_links.py`
   - `python scripts/scan_math_format.py`

