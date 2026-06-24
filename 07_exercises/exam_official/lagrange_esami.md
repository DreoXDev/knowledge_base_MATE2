# Esercizi ufficiali - Lagrange

## Pattern generale

Con un vincolo:

$$
\nabla f=\lambda\nabla g
$$

Con due vincoli:

$$
\nabla f=\lambda\nabla g+\mu\nabla h
$$

Alla fine bisogna sempre confrontare i valori di $f$ sui candidati.

## 13 aprile 2023 - Esercizio 1

### Traccia

Massimizzare:

$$
f=xyz
$$

con:

$$
x+y+z=1,\qquad x,y,z\geq0
$$

### Soluzione guidata

Sul bordo almeno una variabile e' nulla, quindi $f=0$. Nell'interno:

$$
\nabla f=\lambda\nabla(x+y+z)
$$

cioe':

$$
yz=\lambda,\qquad xz=\lambda,\qquad xy=\lambda
$$

Nel caso interno $x,y,z>0$, segue:

$$
x=y=z
$$

e dal vincolo:

$$
x=y=z=\frac{1}{3}
$$

Risultato:

$$
f_{\max}=\frac{1}{27}
$$

## 14 luglio 2022 - Esercizio 2

### Traccia

Determinare massimo e minimo assoluto di:

$$
f=x-y+z
$$

sulla sfera:

$$
3x^2+3y^2+3z^2=4
$$

### Risultati

$$
f_{\max}=2,\qquad f_{\min}=-2
$$

nei punti:

$$
\left(\frac{2}{3},-\frac{2}{3},\frac{2}{3}\right),
\qquad
\left(-\frac{2}{3},\frac{2}{3},-\frac{2}{3}\right)
$$

## 22 novembre 2022 - Esercizio 2

### Traccia

Massimo e minimo di:

$$
f=x+z
$$

sulla curva:

$$
x^2+3y^2=3,\qquad y+z=0
$$

### Sistema

$$
\nabla f=\lambda(2x,6y,0)+\mu(0,1,1)
$$

con i due vincoli.

### Errori da evitare

- Usare un solo moltiplicatore con due vincoli.
- Dimenticare il vincolo lineare $y+z=0$.

## 22 febbraio 2023 - Esercizio 2

### Traccia

Massimo e minimo di:

$$
f=x+2y+3z
$$

sulla sfera:

$$
x^2+y^2+z^2=14
$$

### Risultato

Il vettore dei coefficienti e' $(1,2,3)$ e ha norma $\sqrt{14}$, uguale al raggio. Quindi:

$$
f_{\max}=14,\qquad f_{\min}=-14
$$

nei punti $(1,2,3)$ e $(-1,-2,-3)$.

## 24/27 settembre 2022 - Esercizio 2

### Traccia

Massimo e minimo di $f=z$ sulla curva:

$$
x^2+y^2=8,\qquad x+y+z=0
$$

### Risultato

Massimo in $(-2,-2,4)$ e minimo in $(2,2,-4)$.

## 19 luglio 2023 - Esercizio 2

### Traccia

Retta intersezione:

$$
x+y=2,\qquad x+y+2z=0
$$

Punto di minima distanza dall'origine.

### Risultato

$$
(1,1,-1)
$$

con distanza $\sqrt{3}$.
