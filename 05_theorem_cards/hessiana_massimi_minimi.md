# Teorema: classificazione tramite Hessiana

## Stato

- Fonte: `01_sources/official_slides/3_lezione_massimi_minimi_locali.pdf`
- Slide: 16-18
- Affidabilita': alta
- Dimostrazione richiesta: da verificare
- Ultimo aggiornamento: 2026-06-23

## Setup

Sia $P$ un punto stazionario e sia $H(P)$ la matrice Hessiana.

## Enunciato

- Se la forma quadratica associata a $H(P)$ e' definita positiva, allora $P$ e' minimo locale.
- Se e' definita negativa, allora $P$ e' massimo locale.
- Se e' indefinita, allora $P$ non e' un estremo locale ed e' un punto sella.
- Se e' semidefinita, il test non basta.

## Idea

Nei punti stazionari il segno di $\Delta f$ e' determinato al secondo ordine dalla forma quadratica Hessiana, salvo casi degeneri in cui il resto diventa rilevante.

## Punti delicati

- Applicare il test solo nei punti stazionari.
- Se la forma e' semidefinita, bisogna studiare termini ulteriori.

## Collegamenti

- [[hessiana_forme_quadratiche]]
- [[test_hessiano_massimi_minimi]]
