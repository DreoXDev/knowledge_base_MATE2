# Discorso orale: collegamento tra Green, Stokes e Gauss

## Versione breve

Le formule di Green, Stokes e Gauss sono tre teoremi integrali che collegano un integrale su una frontiera con un integrale sul dominio interno.

La formula di Green lavora nel piano:

$$
\oint_C P\,dx+Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy
$$

La formula di Stokes generalizza questa idea alle superfici nello spazio:

$$
\oint_{\partial S}F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

La formula di Gauss-Ostrogradski riguarda invece il flusso attraverso una superficie chiusa:

$$
\iint_{\partial\Omega}F\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

Quindi Green e Stokes riguardano circuitazione e rotore, mentre Gauss riguarda flusso e divergenza.

## Follow-up

- Quale teorema uso se ho una curva chiusa nel piano?
- Quale teorema uso se ho il bordo di una superficie?
- Quale teorema uso se ho una superficie chiusa?
