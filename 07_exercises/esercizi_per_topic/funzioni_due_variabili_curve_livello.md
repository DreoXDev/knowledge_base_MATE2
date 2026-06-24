# Esercizi - Funzioni di due variabili e curve di livello

## Esercizio 1 - Derivate parziali

### Traccia

Calcolare le derivate parziali di:

$$
f(x,y)=x^2y^3.
$$

### Svolgimento

$$
f_x=2xy^3
$$

$$
f_y=3x^2y^2.
$$

---

## Esercizio 2 - Derivate di ordine superiore

### Traccia

Per $f(x,y)=x^2y^3$, calcolare alcune derivate seconde.

### Svolgimento

$$
f_{xx}=2y^3,\qquad
f_{xy}=6xy^2,\qquad
f_{yx}=6xy^2,\qquad
f_{yy}=6x^2y.
$$

Le derivate miste coincidono nell'esempio:

$$
f_{xy}=f_{yx}.
$$

---

## Esercizio 3 - Piano tangente

### Traccia

Scrivere la formula generale del piano tangente al grafico di $f(x,y)$ in $P=(\bar{x},\bar{y})$.

### Svolgimento

Se $f$ e' differenziabile in $P$, allora:

$$
z-f(P)=f_x(P)(x-\bar{x})+f_y(P)(y-\bar{y}).
$$

### Nota

L'esempio numerico delle slide 18-19 e' da verificare per incongruenze tra funzione dichiarata e valori calcolati.

---

## Esercizio 4 - Derivata lungo una curva

### Traccia

Sia:

$$
f(x,y)=x^2y^3
$$

e:

$$
x(t)=t+1,\qquad y(t)=t^2.
$$

Calcolare la derivata della restrizione di $f$ alla curva nel punto $(2,1)$.

### Svolgimento

Il parametro e' $t=1$.

Metodo 1:

$$
F(t)=(t+1)^2t^6=t^8+2t^7+t^6
$$

$$
F'(t)=8t^7+14t^6+6t^5
$$

$$
F'(1)=28.
$$

Metodo 2:

$$
F'(1)=\nabla f(2,1)\cdot x'(1)
$$

$$
\nabla f(2,1)=(4,12)
$$

$$
x'(1)=(1,2)
$$

$$
F'(1)=4+24=28.
$$

---

## Esercizio 5 - Curve di livello

### $f(x,y)=x^2+y^2$

Le curve di livello sono:

$$
x^2+y^2=c,\qquad c\geq 0,
$$

cioe' circonferenze di raggio $\sqrt{c}$.

### $f(x,y)=-x^2-y^2$

Le curve di livello sono:

$$
-x^2-y^2=c,\qquad c\leq 0,
$$

cioe' circonferenze di raggio $\sqrt{|c|}$.

### $f(x,y)=x^2-y^2$

Le curve di livello sono:

$$
x^2-y^2=c.
$$

Per $c=0$:

$$
(x-y)(x+y)=0,
$$

quindi:

$$
y=x
\qquad
y=-x.
$$

Per $c>0$ e $c<0$ si ottengono iperboli.

