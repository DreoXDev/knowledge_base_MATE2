# Esercizi - Cambiamento di variabili e coordinate

## Esercizio 1 - Area del cerchio in coordinate polari

### Traccia

Calcolare l'area del cerchio:

$$
D=\{(x,y):x^2+y^2\leq R^2\}.
$$

### Soluzione

Coordinate polari:

$$
x=\rho\cos\theta,
\qquad
y=\rho\sin\theta.
$$

$$
dx\,dy=\rho\,d\rho\,d\theta.
$$

Limiti:

$$
0\leq\rho\leq R,
\qquad
0\leq\theta\leq2\pi.
$$

Quindi:

$$
\iint_Ddx\,dy
=
\int_0^{2\pi}d\theta
\int_0^R\rho\,d\rho
=
\pi R^2.
$$

## Esercizio 2 - Paraboloide in coordinate cilindriche

### Traccia

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

### Coordinate cilindriche

$$
x=\rho\cos\varphi,
\qquad
y=\rho\sin\varphi.
$$

$$
dx\,dy\,dz=\rho\,d\rho\,d\varphi\,dz.
$$

Limiti:

$$
0\leq\rho\leq1,
\qquad
0\leq\varphi\leq\frac{\pi}{2},
\qquad
\rho^2\leq z\leq1.
$$

Risultato:

$$
\frac{1}{32}.
$$

## Esercizio 3 - Volume della sfera in coordinate sferiche

### Traccia

Calcolare il volume della sfera:

$$
x^2+y^2+z^2\leq R^2.
$$

### Coordinate sferiche della lezione

$$
x=r\cos\theta\cos\varphi,
\qquad
y=r\cos\theta\sin\varphi,
\qquad
z=r\sin\theta.
$$

$$
dx\,dy\,dz=r^2\cos\theta\,dr\,d\varphi\,d\theta.
$$

Limiti:

$$
0\leq r\leq R,
\qquad
0\leq\varphi\leq2\pi,
\qquad
-\frac{\pi}{2}\leq\theta\leq\frac{\pi}{2}.
$$

Risultato:

$$
\frac{4}{3}\pi R^3.
$$

