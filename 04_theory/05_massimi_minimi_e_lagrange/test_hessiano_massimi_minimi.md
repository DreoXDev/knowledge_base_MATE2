# Test Hessiano per massimi e minimi locali

## Stato

- Fonte: `01_sources/official_slides/3_lezione_massimi_minimi_locali.pdf`
- Slide: 18, 22-25
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Setup

Sia $P$ un punto stazionario per $f(x,y)$ e sia:

$$
D(P)=
(f_{xx}f_{yy}-f_{xy}^2)(P).
$$

## Test pratico

- Se $D(P)>0$ e $f_{xx}(P)>0$, $P$ e' un punto di minimo locale.
- Se $D(P)>0$ e $f_{xx}(P)<0$, $P$ e' un punto di massimo locale.
- Se $D(P)<0$, $P$ e' un punto sella.
- Se $D(P)=0$, il test non permette di stabilire con certezza la natura del punto stazionario.

## Idea

In un punto stazionario il termine lineare dello sviluppo di Taylor scompare. Nei casi non degeneri, il segno della variazione $\Delta f$ e' determinato dalla forma quadratica associata alla Hessiana.

## Procedura operativa

1. Calcolare $\nabla f$.
2. Risolvere $\nabla f=0$.
3. Calcolare la Hessiana.
4. Valutare $D(P)$ e $f_{xx}(P)$ nei punti stazionari.
5. Classificare i punti.

## Attenzione

Il test Hessiano si applica ai punti stazionari. Se $D(P)=0$, servono altri metodi o termini di ordine superiore.

## Collegamenti

- [[massimi_minimi_locali]]
- [[hessiana_forme_quadratiche]]
- [[test_determinante_hessiano]]

