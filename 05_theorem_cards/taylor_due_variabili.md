# Formula: Taylor due variabili

## Stato

- Fonte: `01_sources/official_slides/3_lezione_massimi_minimi_locali.pdf`
- Slide: 1-11
- Affidabilita': alta
- Dimostrazione richiesta: derivazione tramite restrizione a retta
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per approssimare una funzione di due variabili vicino a un punto e per studiare il comportamento locale nei punti stazionari.

## Ipotesi

- $f:\mathbb{R}^2\to\mathbb{R}$.
- Derivate parziali continue fino all'ordine richiesto in un intorno di $P=(\bar{x},\bar{y})$.

## Formula al secondo ordine

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

## Derivazione

Si considera la retta:

$$
x(t)=\bar{x}+t\Delta x,\qquad y(t)=\bar{y}+t\Delta y
$$

e la funzione:

$$
F(t)=f(\bar{x}+t\Delta x,\bar{y}+t\Delta y).
$$

Applicando Taylor monodimensionale a $F$ in $t=0$ e usando la regola della funzione composta si ottiene la formula.

## Punti delicati

- Il termine misto e' $2f_{xy}\Delta x\Delta y$.
- In un punto stazionario il termine lineare si annulla.

## Esempi standard

- $\cos(x+y)$ in $(0,0)$.
- Polinomio quadratico di grado al piu' due.

## Collegamenti

- [[taylor_due_variabili]]
- [[hessiana_forme_quadratiche]]
