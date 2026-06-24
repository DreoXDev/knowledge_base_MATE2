# Esercizi - Formula di Gauss-Ostrogradski

## Campo radiale sulla sfera

Campo:

$$
F=(x,y,z)
$$

Superficie:

$$
x^2+y^2+z^2=R^2
$$

con normale uscente.

Poiche':

$$
\operatorname{div}F=3
$$

per Gauss:

$$
\iint_SF\cdot n\,dS
=
3\cdot\frac{4}{3}\pi R^3
=
4\pi R^3
$$

## Campo cubico sulla sfera

Campo:

$$
F=(x^3,y^3,z^3)
$$

Allora:

$$
\operatorname{div}F=3x^2+3y^2+3z^2
$$

Per Gauss sulla sfera di raggio $R$:

$$
\iint_SF\cdot n\,dS
=
3\iiint_\Omega(x^2+y^2+z^2)\,dV
$$

In coordinate sferiche del corso:

$$
dV=r^2\cos\theta\,dr\,d\theta\,d\varphi
$$

quindi:

$$
3\int_0^{2\pi}\int_{-\pi/2}^{\pi/2}\int_0^R r^4\cos\theta\,dr\,d\theta\,d\varphi
=
\frac{12}{5}\pi R^5
$$

## Guscio sferico

Campo:

$$
F=\frac{(x,y,z)}{(x^2+y^2+z^2)^{3/2}}
$$

Dominio: guscio tra le sfere di raggi $a$ e $b$, con $b>a$.

Sul bordo esterno:

$$
F\cdot n=\frac{1}{b^2}
$$

Sul bordo interno la normale uscente dal guscio punta verso il centro, quindi:

$$
F\cdot n=-\frac{1}{a^2}
$$

Il flusso totale e':

$$
-\frac{1}{a^2}4\pi a^2+\frac{1}{b^2}4\pi b^2=0
$$

Coerentemente, $\operatorname{div}F=0$ nel guscio.

## Campi solenoidali

Se $\operatorname{div}F=0$, allora per Gauss il flusso totale attraverso ogni superficie chiusa contenuta nel dominio e' nullo. Nei tubi di flusso questo implica che il flusso attraverso sezioni diverse resta costante.
