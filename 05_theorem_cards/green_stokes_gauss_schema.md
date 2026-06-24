# Scheda: Green, Stokes e Gauss

## Idea comune

I tre teoremi collegano un integrale sulla frontiera con un integrale nel dominio interno.

| Teorema | Frontiera | Interno | Operatore |
|---|---|---|---|
| Green | curva piana chiusa | dominio piano | $Q_x-P_y$ |
| Stokes | bordo di una superficie | superficie | $\operatorname{rot}$ |
| Gauss | superficie chiusa | volume | $\operatorname{div}$ |

## Formule

$$
\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy
$$

$$
\oint_{\partial S}F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

$$
\iint_{\partial\Omega}F\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

## Collegamenti

- [[green_stokes_gauss_collegamenti]]
- [[formula_green]]
- [[formula_stokes]]
- [[formula_gauss_ostrogradski]]
