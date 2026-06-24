# Esercizi - Integrali di linea di II specie

## Esercizio 1 - Tre cammini diversi

Calcolare:

$$
\int_C 3x^2y\,dx+(x^3+1)\,dy
$$

nei seguenti casi:

1. segmento da $(0,0)$ a $(1,1)$;
2. arco della parabola $y=x^2$ da $(0,0)$ a $(1,1)$;
3. spezzata passante per $(1,0)$.

## Cammino 1 - Segmento

Parametrizzazione:

$$
x(t)=t,\qquad y(t)=t,\qquad t\in[0,1].
$$

Allora:

$$
dx=dt,\qquad dy=dt
$$

e:

$$
\int_0^1
\left[
3t^3+(t^3+1)
\right]dt
=
2.
$$

## Cammino 2 - Parabola

Parametrizzazione:

$$
x(t)=t,\qquad y(t)=t^2,\qquad t\in[0,1].
$$

Allora:

$$
dx=dt,\qquad dy=2t\,dt
$$

e:

$$
\int_0^1
\left[
3t^4+(t^3+1)2t
\right]dt
=
2.
$$

## Cammino 3 - Spezzata

Primo tratto:

$$
x(t)=t,\qquad y(t)=0,\qquad t\in[0,1].
$$

Secondo tratto:

$$
x(t)=1,\qquad y(t)=t,\qquad t\in[0,1].
$$

Il valore totale e':

$$
2.
$$

## Interpretazione tramite potenziale

Il campo e':

$$
F=(3x^2y,x^3+1)
$$

ed e' conservativo perche':

$$
F=\nabla(x^3y+y).
$$

Un potenziale e':

$$
U(x,y)=x^3y+y.
$$

Quindi:

$$
\int_C F\cdot \tau\,d\ell
=
U(1,1)-U(0,0)
=
2
$$

indipendentemente dal cammino.
