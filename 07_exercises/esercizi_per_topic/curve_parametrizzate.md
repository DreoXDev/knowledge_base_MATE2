# Esercizi - Curve parametrizzate

## Esercizio 1 - Moto rettilineo uniforme

### Traccia

Data la curva:

$$
x(t)=vt+x_0
$$

calcolare il vettore tangente e interpretare il moto.

### Svolgimento

$$
\frac{dx}{dt}=v
$$

Il vettore tangente e' costante, quindi il moto e' rettilineo uniforme.

---

## Esercizio 2 - Moto rettilineo non uniforme

### Traccia

Data la curva:

$$
x(t)=t^3,\qquad y(t)=t^3
$$

determinare il sostegno geometrico e il vettore tangente.

### Svolgimento

Eliminando il parametro:

$$
y=x
$$

Il vettore tangente e':

$$
(3t^2,3t^2)
$$

La curva sta sulla retta $y=x$, ma il vettore tangente non e' costante.

---

## Esercizio 3 - Moto su semiretta

### Traccia

Data la curva:

$$
x(t)=t^2,\qquad y(t)=t^2
$$

determinare il sostegno geometrico e verificare se e' regolare.

### Svolgimento

Si ha $y=x$ e $x,y\geq 0$, quindi il sostegno e' una semiretta.

Il vettore tangente e':

$$
(2t,2t)
$$

In $t=0$ si annulla, quindi la parametrizzazione non e' regolare in $t=0$.

---

## Esercizio 4 - Lunghezza circonferenza

### Traccia

Calcolare la lunghezza della curva:

$$
x(t)=R\cos t,\qquad y(t)=R\sin t,\qquad t\in[0,2\pi]
$$

### Svolgimento

Il vettore tangente e':

$$
(-R\sin t,R\cos t)
$$

La sua norma e':

$$
R
$$

Quindi:

$$
\ell=\int_0^{2\pi}R\,dt=2\pi R.
$$

