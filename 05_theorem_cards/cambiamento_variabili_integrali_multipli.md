# Teorema: cambiamento di variabili negli integrali multipli

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 44-50
- Affidabilita': alta

## Enunciato nel piano

Sia:

$$
x=x(\xi,\eta),
\qquad
y=y(\xi,\eta)
$$

una trasformazione regolare che manda $\Omega$ nel dominio $D$. Allora:

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

## Enunciato in dimensione $n$

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

- [[cambiamento_variabili_jacobiano]]
- [[jacobiano]]

