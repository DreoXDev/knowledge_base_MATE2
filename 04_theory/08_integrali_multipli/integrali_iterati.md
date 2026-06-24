# Integrali iterati

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 17-21
- Affidabilita': alta

## Dominio normale rispetto a $x$

Se:

$$
\Omega=\{(x,y):a\leq x\leq b,\ y_1(x)\leq y\leq y_2(x)\},
$$

allora:

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_a^b dx
\int_{y_1(x)}^{y_2(x)}
f(x,y)\,dy.
$$

## Dominio normale rispetto a $y$

Se:

$$
\Omega=\{(x,y):c\leq y\leq d,\ x_1(y)\leq x\leq x_2(y)\},
$$

allora:

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_c^d dy
\int_{x_1(y)}^{x_2(y)}
f(x,y)\,dx.
$$

## Interpretazione geometrica

Se $f\geq 0$, l'integrale doppio rappresenta il volume del solido compreso tra il dominio di base e il grafico $z=f(x,y)$.

## Collegamenti

- [[inversione_ordine_integrazione]]
- [[formula_green]]
