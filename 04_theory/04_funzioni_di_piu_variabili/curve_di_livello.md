# Curve di livello

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 27-34
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Definizione

Una curva:

$$
x:[a,b]\subset\mathbb{R}\to\mathbb{R}^n
$$

si dice curva di livello di:

$$
f:\mathbb{R}^n\to\mathbb{R}
$$

se la restrizione di $f$ alla curva e' costante:

$$
f(x_1(t),\dots,x_n(t))=c.
$$

## Gradiente ortogonale alle curve di livello

Derivando lungo una curva di livello:

$$
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}
\frac{dx_i}{dt}
=
0.
$$

Quindi il gradiente di una funzione valutato in un punto e' ortogonale a tutte le curve di livello passanti per quel punto.

## Caso di due variabili

Nel caso $n=2$, le curve di livello si ottengono risolvendo:

$$
f(x,y)=c
$$

al variare di $c$.

## Esempi

### $f(x,y)=x^2+y^2$

Le curve di livello esistono per:

$$
c\geq 0
$$

e sono circonferenze di raggio:

$$
\sqrt{c}.
$$

### $f(x,y)=-x^2-y^2$

Le curve di livello esistono per:

$$
c\leq 0
$$

e sono circonferenze di raggio:

$$
\sqrt{|c|}.
$$

### $f(x,y)=x^2-y^2$

Le curve di livello sono definite per ogni $c$.

Per $c=0$:

$$
x^2-y^2=0
$$

quindi:

$$
(x-y)(x+y)=0
$$

e si ottengono le due rette:

$$
y=x
\qquad
y=-x.
$$

Per $c>0$ e $c<0$ si ottengono iperboli.

## Grafici / Figure

- `08_visuals/figures/lezione_2_slide_30_livello_x2_piu_y2.png`
- `08_visuals/figures/lezione_2_slide_32_livello_meno_x2_meno_y2.png`
- `08_visuals/figures/lezione_2_slide_34_livello_x2_meno_y2.png`

## Collegamenti

- [[gradiente_derivata_direzionale]]
- [[gradiente_curve_livello]]

