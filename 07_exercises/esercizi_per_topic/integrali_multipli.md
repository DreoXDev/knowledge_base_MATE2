# Esercizi - Integrali multipli

## Esercizio 1 - Quadrato

Calcolare:

$$
\iint_R \frac{1}{(x+y)^2}\,dx\,dy,
\qquad
R=[3,4]\times[1,2].
$$

Risultato:

$$
\ln\frac{25}{24}.
$$

## Esercizio 2 - Inversione tra parabola e retta

Calcolare:

$$
\int_0^1 dx\int_{x^2}^{x}xy^2\,dy.
$$

Il dominio e' compreso tra $y=x^2$ e $y=x$. Invertendo:

$$
0\leq y\leq1,
\qquad
y\leq x\leq\sqrt{y}.
$$

Quindi:

$$
\int_0^1dy\int_y^{\sqrt{y}}xy^2\,dx
=
\frac{1}{40}.
$$

## Esercizio 3 - Inversione con integranda non elementare

Calcolare:

$$
\int_0^1dx\int_x^1e^{y^2}\,dy.
$$

Invertendo:

$$
0\leq y\leq1,
\qquad
0\leq x\leq y.
$$

Allora:

$$
\int_0^1dy\int_0^y e^{y^2}\,dx
=
\int_0^1 ye^{y^2}\,dy
=
\frac{1}{2}(e-1).
$$

## Esercizio 4 - Regione tra $y=e^x$, $x=0$, $y=2$

Calcolare:

$$
\iint_\Omega e^{x+y}\,dx\,dy.
$$

Il dominio puo' essere scritto:

$$
1\leq y\leq2,
\qquad
0\leq x\leq\ln y.
$$

Risultato:

$$
e.
$$

## Esercizio 5 - Regione tra $y=1/x$, $y=x$, $x=2$

Calcolare:

$$
\iint_\Omega \frac{x^2}{y^2}\,dx\,dy.
$$

Rispetto a $x$:

$$
1\leq x\leq2,
\qquad
\frac{1}{x}\leq y\leq x.
$$

Invertendo si spezza:

$$
\frac{1}{2}\leq y\leq1,
\qquad
\frac{1}{y}\leq x\leq2,
$$

$$
1\leq y\leq2,
\qquad
y\leq x\leq2.
$$

Risultato:

$$
\frac{9}{4}.
$$

## Esercizio 6 - Regione tra parabola orizzontale e retta

Calcolare:

$$
\iint_\Omega (x+2y)\,dx\,dy
$$

dove $\Omega$ e' compresa tra $x=y^2-4$ e $x=5$.

Limiti:

$$
-3\leq y\leq3,
\qquad
y^2-4\leq x\leq5.
$$

Risultato:

$$
\frac{252}{5}.
$$

## Esercizio 7 - Area dell'ellisse

Calcolare l'area della regione:

$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}\leq1.
$$

Risultato:

$$
\pi ab.
$$

## Esercizio 8 - Tetraedro

Calcolare:

$$
\iiint_\Omega
\frac{dx\,dy\,dz}{(1+x+y+z)^3}
$$

dove $\Omega$ e' il tetraedro:

$$
x\geq0,
\qquad
y\geq0,
\qquad
z\geq0,
\qquad
x+y+z\leq1.
$$

Limiti per fili:

$$
0\leq x\leq1,
\qquad
0\leq y\leq1-x,
\qquad
0\leq z\leq1-x-y.
$$

Risultato:

$$
\frac{1}{2}\ln2-\frac{5}{16}.
$$

## Esercizio 9 - Paraboloide e assi coordinati

Calcolare:

$$
\iiint_\Omega xyz\,dx\,dy\,dz
$$

dove $\Omega$ e' delimitata da:

$$
z=x^2+y^2,
\qquad
x=0,
\qquad
y=0,
\qquad
z=1.
$$

Risultato:

$$
\frac{1}{32}.
$$

## Esercizio 10 - Volume dell'ellissoide

Per:

$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\leq1
$$

il volume e':

$$
\frac{4}{3}\pi abc.
$$

