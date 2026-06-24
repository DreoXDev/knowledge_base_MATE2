# Discorso orale: formula di Taylor per funzioni di due variabili

## Versione breve

Per ottenere la formula di Taylor di una funzione di due variabili si considera un punto base $P=(\bar{x},\bar{y})$ e un punto vicino $P'=(\bar{x}+\Delta x,\bar{y}+\Delta y)$. Si parametrizza la retta che li congiunge con:

$$
x(t)=\bar{x}+t\Delta x,\qquad y(t)=\bar{y}+t\Delta y
$$

e si considera la funzione di una variabile:

$$
F(t)=f(\bar{x}+t\Delta x,\bar{y}+t\Delta y).
$$

Applicando Taylor a $F$ in $t=0$ e calcolando le derivate con la regola della funzione composta si ottiene lo sviluppo di Taylor di $f$.

Al secondo ordine:

$$
f(x,y)
=
f(\bar{x},\bar{y})
+
f_x(\bar{x},\bar{y})\Delta x
+
f_y(\bar{x},\bar{y})\Delta y
+
\frac{1}{2}
\left[
f_{xx}(\bar{x},\bar{y})(\Delta x)^2
+
2f_{xy}(\bar{x},\bar{y})\Delta x\Delta y
+
f_{yy}(\bar{x},\bar{y})(\Delta y)^2
\right]
+
Resto.
$$

## Follow-up

- Da dove viene il termine misto?
- Perche' si usa una retta?
- Quali ipotesi di regolarita' servono?

