# Derivate parziali

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 6-10
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Definizione generale

Per una funzione di $n$ variabili, la derivata parziale rispetto a $x_j$ nel punto:

$$
P=(\bar{x}_1,\dots,\bar{x}_n)
$$

e':

$$
\frac{\partial f}{\partial x_j}(P)
=
\lim_{\Delta x_j\to 0}
\frac{
f(\bar{x}_1,\dots,\bar{x}_{j-1},\bar{x}_j+\Delta x_j,\bar{x}_{j+1},\dots,\bar{x}_n)
-
f(\bar{x}_1,\dots,\bar{x}_n)
}
{\Delta x_j}.
$$

Notazioni alternative:

$$
f_{x_j}
\qquad
f'_{x_j}.
$$

## Caso di due variabili

$$
\frac{\partial f}{\partial x}(\bar{x},\bar{y})
=
\lim_{\Delta x\to 0}
\frac{f(\bar{x}+\Delta x,\bar{y})-f(\bar{x},\bar{y})}{\Delta x}
$$

$$
\frac{\partial f}{\partial y}(\bar{x},\bar{y})
=
\lim_{\Delta y\to 0}
\frac{f(\bar{x},\bar{y}+\Delta y)-f(\bar{x},\bar{y})}{\Delta y}.
$$

## Esempio

Per:

$$
f(x,y)=x^2y^3
$$

si ha:

$$
f_x=2xy^3
$$

e:

$$
f_y=3x^2y^2.
$$

## Derivate parziali di ordine superiore

Per $f(x,y)=x^2y^3$:

$$
f_{xx}=2y^3,\qquad
f_{xy}=6xy^2,\qquad
f_{yx}=6xy^2,\qquad
f_{yy}=6x^2y.
$$

## Teorema di scambio

Se le derivate parziali fino all'ordine $N$ esistono in un intorno di $P$ e quelle di ordine $N$ sono continue in $P$, allora il risultato non dipende dall'ordine di derivazione.

In particolare:

$$
\frac{\partial^2 f}{\partial x\partial y}
=
\frac{\partial^2 f}{\partial y\partial x}.
$$

## Note di attenzione

- Slide 7: probabile refuso, la parte con tre variabili riguarda funzioni di tre variabili, non di due.
- Slide 8: probabile refuso nel calcolo di $f_y$; il denominatore deve essere $\Delta y$ e il limite deve essere per $\Delta y\to 0$.

## Errori da evitare

- Le derivate parziali studiano la variazione rispetto a una sola variabile alla volta.
- L'esistenza delle derivate parziali da sola non garantisce la differenziabilita'.

## Collegamenti

- [[differenziabilita]]
- [[scambio_derivate_parziali]]

