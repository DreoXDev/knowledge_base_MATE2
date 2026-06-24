# Restrizione di una funzione a una curva

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 20-24
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Definizione

Sia:

$$
x:[a,b]\subset\mathbb{R}\to\mathbb{R}^n
$$

una curva regolare, e sia:

$$
f:\mathbb{R}^n\to\mathbb{R}
$$

una funzione di $n$ variabili.

La funzione:

$$
F:[a,b]\subset\mathbb{R}\to\mathbb{R}
$$

ottenuta componendo:

$$
F(t):=f(x(t))=f(x_1(t),\dots,x_n(t))
$$

si chiama restrizione di $f$ alla curva $x(t)$.

## Derivata lungo una curva

Se $f$ e' differenziabile e:

$$
F(t)=f(x_1(t),\dots,x_n(t)),
$$

allora la derivata di $F$ in $\bar{t}$ si chiama derivata di $f$ lungo la curva nel punto:

$$
P=(x_1(\bar{t}),\dots,x_n(\bar{t})).
$$

Vale:

$$
F'(\bar{t})
=
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}(P)
\frac{dx_i}{dt}(\bar{t}).
$$

## Dimostrazione

Dalla differenziabilita':

$$
\Delta f=
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}(P)\Delta x_i
+
o(\rho).
$$

Dividendo per $\Delta t$:

$$
\frac{\Delta f}{\Delta t}
=
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}(P)
\frac{\Delta x_i}{\Delta t}
+
\frac{o(\rho)}{\Delta t}.
$$

Passando al limite per $\Delta t\to 0$ lungo la curva si ottiene:

$$
F'(\bar{t})
=
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}(P)
\frac{dx_i}{dt}(\bar{t}).
$$

## Esempio

Per:

$$
f(x,y)=x^2y^3,\qquad x(t)=t+1,\qquad y(t)=t^2,
$$

nel punto $(2,1)$ si ha $t=1$. La restrizione e':

$$
F(t)=(t+1)^2t^6=t^8+2t^7+t^6.
$$

Quindi:

$$
F'(t)=8t^7+14t^6+6t^5
$$

e:

$$
F'(1)=28.
$$

Metodo alternativo:

$$
\nabla f(2,1)=(4,12),\qquad x'(1)=(1,2),
$$

quindi:

$$
F'(1)=4\cdot 1+12\cdot 2=28.
$$

## Collegamenti

- [[curve_parametrizzate]]
- [[gradiente_derivata_direzionale]]
- [[derivata_lungo_curva]]

