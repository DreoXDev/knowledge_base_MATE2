# Collegamento tra Green, Stokes e Gauss

Green, Stokes e Gauss-Ostrogradski sono teoremi integrali che collegano un integrale su una frontiera con un integrale sul dominio interno.

## Green

La formula di Green lavora nel piano:

$$
\oint_C P\,dx+Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy
$$

Collega la circuitazione lungo una curva chiusa piana con l'integrale del rotore scalare nel dominio piano.

## Stokes

La formula di Stokes generalizza Green alle superfici nello spazio:

$$
\oint_{\partial S}F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

Collega la circuitazione lungo il bordo della superficie con il flusso del rotore attraverso la superficie.

## Gauss-Ostrogradski

La formula di Gauss-Ostrogradski riguarda superfici chiuse:

$$
\iint_{\partial\Omega}F\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

Collega il flusso uscente attraverso la frontiera del volume con l'integrale della divergenza nel volume.

## Schema orale

| Teorema | Frontiera | Interno | Operatore |
|---|---|---|---|
| Green | curva chiusa piana | dominio piano | rotore scalare |
| Stokes | bordo di una superficie | superficie | rotore |
| Gauss | superficie chiusa | volume | divergenza |

## Quando usarli

- Uso Green quando ho una curva chiusa nel piano e voglio trasformare un integrale di linea in un integrale doppio.
- Uso Stokes quando ho il bordo di una superficie nello spazio e compare una circuitazione.
- Uso Gauss quando ho una superficie chiusa e voglio calcolare un flusso.

## Collegamenti

- [[formula_green]]
- [[formula_stokes]]
- [[formula_gauss_ostrogradski]]
