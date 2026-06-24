# Teorema: formula di Green

## Stato

- Fonte: `01_sources/official_slides/9_lezione_campi_vettoriali_conservativi.pdf`
- Slide: 17-36
- Affidabilita': alta

## Enunciato

Se $F=(P,Q)$ e $C=\partial\sigma$ e' orientata positivamente, allora:

$$
\oint_C P\,dx+Q\,dy
=
\iint_\sigma(Q_x-P_y)\,dx\,dy.
$$

## Ipotesi

- $\sigma$ dominio piano semplice.
- $C$ frontiera differenziabile a tratti.
- $P,Q,Q_x,P_y$ continue su $\overline{\sigma}$.
- Orientazione positiva: il dominio resta a sinistra.

## Dimostrazione

Si dimostrano:

$$
\iint_\sigma P_y\,dx\,dy=-\int_C P\,dx
$$

e:

$$
\iint_\sigma Q_x\,dx\,dy=\int_C Q\,dy.
$$

Poi si sommano le identita'.

## Collegamenti

- [[formula_green]]
- [[green]]
