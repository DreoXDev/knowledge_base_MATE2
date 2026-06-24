# Esercizi - Moltiplicatori di Lagrange

## Esercizio 1 - Distanza minima punto-retta

### Traccia

Determinare il punto sulla retta:

$$
x-y=3
$$

a minima distanza dal punto $(1,2)$.

### Metodo parametrico

Si minimizza:

$$
f(x,y)=(x-1)^2+(y-2)^2.
$$

Con $x=t$, $y=t-3$:

$$
F(t)=(t-1)^2+(t-5)^2=2t^2-12t+26
$$

$$
F'(t)=4t-12.
$$

Quindi:

$$
t=3
$$

e il punto e':

$$
(3,0).
$$

### Metodo Lagrange

$$
\nabla f=
\begin{pmatrix}
2x-2\\
2y-4
\end{pmatrix},
\qquad
\nabla g=
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
$$

Sistema:

$$
2x-2=\lambda
$$

$$
2y-4=-\lambda
$$

$$
x-y=3.
$$

Risultato:

$$
(3,0)
$$

Distanza:

$$
2\sqrt{2}.
$$

---

## Esercizio 2 - Distanza minima punto-piano

### Traccia

Calcolare il punto del piano:

$$
x+y+z=0
$$

a minima distanza da $(1,1,1)$.

### Metodo parametrico

$$
x=s,\qquad y=t,\qquad z=-s-t.
$$

Si ottiene il punto:

$$
(0,0,0).
$$

Nota: sviluppando la funzione ristretta, il termine costante sembra essere $2$ e non $3$ come riportato nelle slide; il punto critico non cambia.

### Metodo Lagrange

$$
\nabla f=
\begin{pmatrix}
2(x-1)\\
2(y-1)\\
2(z-1)
\end{pmatrix},
\qquad
\nabla G=
\begin{pmatrix}
1\\
1\\
1
\end{pmatrix}.
$$

Sistema:

$$
2(x-1)=\lambda
$$

$$
2(y-1)=\lambda
$$

$$
2(z-1)=\lambda
$$

$$
x+y+z=0.
$$

Risultato:

$$
(0,0,0)
$$

e:

$$
\lambda=-2.
$$

Distanza:

$$
\sqrt{3}.
$$

---

## Esercizio 3 - Distanza minima dall'origine su intersezione di due piani

### Traccia

Calcolare il punto a minima distanza dall'origine sulla retta intersezione di:

$$
x+y+z=0
$$

$$
x-z=1.
$$

### Metodo parametrico

Poni:

$$
x=t,\qquad z=t-1,\qquad y=-2t+1.
$$

Allora:

$$
F(t)=t^2+(-2t+1)^2+(t-1)^2=6t^2-6t+2
$$

$$
F'(t)=12t-6.
$$

Quindi:

$$
t=\frac{1}{2}.
$$

Risultato:

$$
\left(\frac{1}{2},0,-\frac{1}{2}\right).
$$

### Metodo Lagrange

Sistema:

$$
2x=\lambda+\mu
$$

$$
2y=\lambda
$$

$$
2z=\lambda-\mu
$$

$$
x+y+z=0
$$

$$
x-z-1=0.
$$

Risultato:

$$
\left(\frac{1}{2},0,-\frac{1}{2}\right).
$$

---

## Esercizio 4 - Seconda intersezione di due piani

### Traccia

Calcolare il punto a minima distanza dall'origine sulla retta intersezione di:

$$
2x-3y-z=4
$$

$$
x-2y-2z=1.
$$

### Metodo parametrico

Poni:

$$
z=t.
$$

Si ottiene:

$$
x=5-4t,\qquad y=2-3t,\qquad z=t.
$$

La distanza al quadrato e':

$$
f(t)=26t^2-52t+29
$$

$$
f'(t)=52t-52.
$$

Quindi:

$$
t=1.
$$

Risultato:

$$
(1,-1,1).
$$

### Metodo Lagrange

Sistema:

$$
2x=2\lambda_1+\lambda_2
$$

$$
2y=-3\lambda_1-2\lambda_2
$$

$$
2z=-\lambda_1-2\lambda_2
$$

$$
2x-3y-z-4=0
$$

$$
x-2y-2z-1=0.
$$

Risultato:

$$
(1,-1,1)
$$

con:

$$
\lambda_1=2,\qquad \lambda_2=-2.
$$

