# Risultato: gradiente ortogonale alle curve di livello

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 27
- Affidabilita': alta
- Dimostrazione richiesta: si
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per interpretare geometricamente il gradiente e le curve di livello.

## Enunciato

Il gradiente di una funzione valutato in un punto e' ortogonale a tutte le curve di livello passanti per quel punto.

## Ipotesi

- $x(t)$ e' una curva di livello.
- $f$ e' differenziabile.
- $P=x(t)$.

## Dimostrazione

Poiche' lungo una curva di livello:

$$
f(x(t))=c,
$$

derivando:

$$
\frac{d}{dt}f(x(t))=0.
$$

Per la formula della derivata lungo una curva:

$$
\nabla f(P)\cdot x'(t)=0.
$$

Quindi $\nabla f(P)$ e' ortogonale al vettore tangente alla curva di livello.

## Intuizione geometrica

Il gradiente punta nella direzione in cui la funzione cambia, mentre lungo la curva di livello la funzione resta costante.

## Collegamenti

- [[curve_di_livello]]
- [[gradiente_derivata_direzionale]]

