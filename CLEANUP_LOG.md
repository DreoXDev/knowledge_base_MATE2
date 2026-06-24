# Cleanup Log - Post raw analysis

## Obiettivo

Pulizia finale della repo dopo ingestione delle lezioni ufficiali e degli esami.

## Data

- Avvio cleanup: 2026-06-24

## Regole

- Non cancellare PDF raw.
- Non perdere collegamenti alle fonti ufficiali.
- Non duplicare note teoriche se esiste gia' una nota equivalente.
- Tutte le formule devono usare `$...$` e `$$...$$`.
- Ogni file nuovo deve essere linkato da almeno un index.

## Azioni

- Creato branch `cleanup/post-raw-analysis`.
- Creati snapshot `.cleanup_dirs_snapshot.txt` e `.cleanup_files_snapshot.txt`.
- Creata sezione `12_final_review/`.
- Creato entrypoint `START_HERE.md`.
- Create mappe finali in `03_maps/`.
- Aggiunti script di controllo copertura fonti e target RAG.
