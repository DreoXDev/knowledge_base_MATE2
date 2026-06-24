# Formula di Taylor per funzioni di due variabili

## Stato

- Fonte: `01_sources/official_slides/3_lezione_massimi_minimi_locali.pdf`
- Slide: 1-11
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Idea

Per ottenere Taylor in due variabili si restringe la funzione alla retta che congiunge il punto base $P$ al punto $P'$ e si applica Taylor a una funzione di una variabile.

## Setup

Sia $P=(\bar{x},\bar{y})$ e sia:

$$
P'=(x,y)=(\bar{x}+\Delta x,\bar{y}+\Delta y).
$$

La retta che congiunge $P$ e $P'$ e':

$$
x(t)=\bar{x}+t\Delta x,\qquad y(t)=\bar{y}+t\Delta y.
$$

Definiamo:

$$
F(t)=f(\bar{x}+t\Delta x,\bar{y}+t\Delta y).
$$

## Taylor del primo ordine

Usando la regola della funzione composta:

$$
F'(0)=f_x(\bar{x},\bar{y})\Delta x+f_y(\bar{x},\bar{y})\Delta y.
$$

Quindi:

$$
f(x,y)
=
f(\bar{x},\bar{y})
+
f_x(\bar{x},\bar{y})\Delta x
+
f_y(\bar{x},\bar{y})\Delta y
+
Resto.
$$

## Taylor del secondo ordine

Si ha:

$$
F''(0)
=
f_{xx}(\bar{x},\bar{y})(\Delta x)^2
+
2f_{xy}(\bar{x},\bar{y})\Delta x\Delta y
+
f_{yy}(\bar{x},\bar{y})(\Delta y)^2.
$$

Lo sviluppo al secondo ordine e':

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

## Caso generale in $n$ variabili

$$
f(x)
=
f(\bar{x})
+
\sum_{i=1}^n f_{x_i}(\bar{x})\Delta x_i
+
\frac{1}{2}
\sum_{i=1}^n
\sum_{j=1}^n
f_{x_i x_j}(\bar{x})\Delta x_i\Delta x_j
+
\cdots
$$

## Esempi

### Taylor di $\cos(x+y)$ in $(0,0)$

$$
f(0,0)=1,\qquad
f_x(0,0)=0,\qquad f_y(0,0)=0
$$

$$
f_{xx}(0,0)=-1,\qquad f_{xy}(0,0)=-1,\qquad f_{yy}(0,0)=-1.
$$

Quindi:

$$
\cos(x+y)=1-\frac{1}{2}(x^2+2xy+y^2)+Resto
$$

cioe':

$$
\cos(x+y)=1-\frac{1}{2}(x+y)^2+Resto.
$$

### Polinomio quadratico

Per:

$$
f(x,y)=3+6y+x^2+2xy+7y^2
$$

lo sviluppo di Taylor al secondo ordine in $(0,0)$ coincide con la funzione stessa.

## Domande orali

- Come si ricava Taylor in due variabili?
- Perche' si restringe la funzione a una retta?
- Come si calcola $F'(0)$?
- Come si calcola $F''(0)$?

## Collegamenti

- [[derivate_parziali]]
- [[hessiana_forme_quadratiche]]

