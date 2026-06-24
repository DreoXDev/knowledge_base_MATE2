# Esercizi - Campi conservativi e Green

## Esercizio 1 - Green su quadrato ruotato

Campo:

$$
F=(x-y,\ x+y).
$$

Curva $C$: quadrato con vertici:

$$
(0,1),\ (1,0),\ (0,-1),\ (-1,0).
$$

Lato destro di Green:

$$
\iint_S(Q_x-P_y)\,dx\,dy
=
\iint_S 2\,dx\,dy.
$$

L'area del quadrato e' $2$, quindi:

$$
\iint_S2\,dx\,dy=4.
$$

Le parametrizzazioni della slide 29 percorrono il bordo in orientazione positiva. Sommando i quattro contributi dell'integrale di linea si ottiene:

$$
\int_0^1 8t\,dt=4.
$$

Nota: l'ordine effettivo dei lati va letto dalle parametrizzazioni della slide 29.

## Esercizio 2 - Green su triangolo

Campo:

$$
F=((x+y)^2,\ -(x^2+y^2)).
$$

Curva $C$: triangolo di vertici:

$$
(0,0),\ (1,0),\ (0,1).
$$

Lato destro:

$$
\iint_S(Q_x-P_y)\,dx\,dy
=
\iint_S(-4x-2y)\,dx\,dy
=
-1.
$$

Le parametrizzazioni dei lati sono:

$$
x=t,\ y=0
$$

$$
x=1-t,\ y=t
$$

$$
x=0,\ y=1-t
$$

con $t\in[0,1]$.

Sommando i tre contributi si ottiene:

$$
\int_0^1(-1)\,dt=-1.
$$

Nota: nella slide 35 compare un termine $F_3 dz/dt$, da ignorare come probabile residuo di template.

## Esercizio 3 - Potenziale $x^2y^2z^2$

Per:

$$
F=(2xy^2z^2,\ 2yx^2z^2,\ 2zx^2y^2)
$$

un potenziale e':

$$
U=x^2y^2z^2.
$$

## Esercizio 4 - Potenziale logaritmico in $\mathbb{R}^3$

Per:

$$
F=
\left(
\frac{2x}{x^2+y^2+z^2},
\frac{2y}{x^2+y^2+z^2},
\frac{2z}{x^2+y^2+z^2}
\right),
$$

un potenziale e':

$$
U=\ln(x^2+y^2+z^2).
$$

## Esercizio 5 - Parametro $\lambda$

Per il campo:

$$
\left(
\lambda x+2xy^2z^3,\ 
\lambda y+2x^2yz^3,\ 
\lambda z+3x^2y^2z^2
\right),
$$

un potenziale e':

$$
U=x^2y^2z^3+\frac{1}{2}\lambda(x^2+y^2+z^2).
$$

La condizione:

$$
\int_\gamma \omega=0
$$

porta a:

$$
8+3\lambda=0.
$$

Quindi:

$$
\lambda=-\frac{8}{3}.
$$

## Esercizio 6 - Integrale su elica

Per:

$$
r(t)=\left(\cos t,\sin t,\frac{t}{\pi}\right),\qquad t\in[0,\pi],
$$

e potenziale:

$$
U=x^3y-y^2x+zx,
$$

gli estremi sono:

$$
P_0=(1,0,0),\qquad P_1=(-1,0,1).
$$

Quindi:

$$
\int_\gamma \omega=U(P_1)-U(P_0)=-1.
$$

## Esercizio 7 - Campo angolare non conservativo

Studiare il campo:

$$
F=
\left(
-\frac{y}{x^2+y^2},
\frac{x}{x^2+y^2}
\right)
$$

su $\mathbb{R}^2\setminus\{0\}$.

Sulla circonferenza unitaria:

$$
x=\cos t,\qquad y=\sin t,\qquad t\in[0,2\pi],
$$

si ha:

$$
\oint_C F\cdot\tau\,d\ell
=
\int_0^{2\pi}1\,dt
=
2\pi.
$$

Il campo non e' conservativo su tutto $\mathbb{R}^2\setminus\{0\}$, anche se e' irrotazionale.
