# Cambiamento di variabili e jacobiano

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 44-51
- Affidabilita': alta

## Trasformazione nel piano

Si considera:

$$
x=x(\xi,\eta),\qquad y=y(\xi,\eta).
$$

Il determinante jacobiano e':

$$
\frac{D(x,y)}{D(\xi,\eta)}
=
\begin{vmatrix}
x_\xi & x_\eta\\
y_\xi & y_\eta
\end{vmatrix}
=
x_\xi y_\eta-y_\xi x_\eta.
$$

## Formula

$$
\iint_D f(x,y)\,dx\,dy
=
\iint_\Omega
f(x(\xi,\eta),y(\xi,\eta))
\left|
\frac{D(x,y)}{D(\xi,\eta)}
\right|
d\xi\,d\eta.
$$

## Significato geometrico

Il valore assoluto del jacobiano misura il fattore locale con cui la trasformazione dilata o contrae le aree.

## Dimensione generale

$$
\int_D f(x_1,\dots,x_n)\,d^nx
=
\int_\Omega
f(x_1(\xi),\dots,x_n(\xi))
\left|
\frac{D(x_1,\dots,x_n)}
{D(\xi_1,\dots,\xi_n)}
\right|
d^n\xi.
$$

## Collegamenti

- [[jacobiano]]
- [[coordinate_polari_cilindriche_sferiche]]
