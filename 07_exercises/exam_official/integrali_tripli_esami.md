# Esercizi ufficiali - Integrali tripli e volumi

## 13 aprile 2023 - Esercizio 4

### Traccia

$$
\iiint_\Omega
\frac{dx\,dy\,dz}{(1+x+y+z)^3}
$$

con:

$$
\Omega=\{x,y,z\geq0,\ x+y+z\leq1\}
$$

### Pattern

- tetraedro;
- integrazione iterata;
- esercizio vicino alle slide sugli integrali multipli.

### Risultato

$$
\frac{1}{2}\ln2-\frac{5}{16}
$$

## 14 luglio 2022 - Esercizio 3

### Traccia

$$
D=\{x^2+y^2+z^2\leq1,\ x>0,\ y>0,\ z>0\}
$$

calcolare:

$$
\iiint_D xyz\,dx\,dy\,dz
$$

### Pattern

- primo ottante;
- coordinate sferiche;
- attenzione ai limiti angolari della convenzione del corso.

## 22 novembre 2022 - Esercizio 3

### Traccia

Volume delimitato da:

$$
x^2+y^2=1,\qquad z=0,\qquad z=4-x^2-y^2
$$

### Soluzione

In coordinate cilindriche:

$$
0\leq\rho\leq1,\qquad 0\leq\theta\leq2\pi,\qquad 0\leq z\leq4-\rho^2
$$

quindi:

$$
V=
\int_0^{2\pi}\int_0^1\rho(4-\rho^2)\,d\rho\,d\theta
=
\frac{7\pi}{2}
$$

## Errori da evitare

- Dimenticare il jacobiano $\rho$ o $r^2\cos\theta$.
- Usare coordinate sferiche con una convenzione diversa da quella del corso senza adattare i limiti.

## 24/27 settembre 2022 - Integrale sulla sfera

### Traccia

$$
\iiint_D(x^2+y^2)\,dx\,dy\,dz
$$

dove $D$ e' la sfera di raggio $1$.

### Risultato

Per simmetria:

$$
\iiint_D(x^2+y^2)\,dV
=
\frac{8\pi}{15}
$$

## 19 luglio 2023 - Primo ottante della sfera

### Traccia

$$
\iiint_\Omega(x^2+y^2+z^2)^2\,dx\,dy\,dz
$$

con $\Omega$ primo ottante della sfera unitaria.

### Risultato

$$
\frac{\pi}{14}
$$
