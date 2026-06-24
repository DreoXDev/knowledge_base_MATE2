# Teorema: scambio delle derivate parziali

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 9-10
- Affidabilita': alta
- Dimostrazione richiesta: da verificare
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per scambiare l'ordine di derivazione nelle derivate parziali miste sotto ipotesi di regolarita'.

## Enunciato

Se $f$ possiede derivate parziali fino all'ordine $N$ in un intorno di un punto $P$ e le derivate parziali di ordine $N$ sono continue in $P$, allora le derivate parziali di ordine $N$ in $P$ non dipendono dall'ordine in cui vengono effettuate.

## Ipotesi

- Derivate parziali fino all'ordine $N$ in un intorno di $P$.
- Derivate parziali di ordine $N$ continue in $P$.

## Tesi

Per esempio, nel caso $n=N=2$:

$$
\frac{\partial^2 f}{\partial x\partial y}
=
\frac{\partial^2 f}{\partial y\partial x}.
$$

## Esempio standard

Per $f(x,y)=x^2y^3$:

$$
f_{xy}=6xy^2,\qquad f_{yx}=6xy^2.
$$

## Collegamenti

- [[derivate_parziali]]

