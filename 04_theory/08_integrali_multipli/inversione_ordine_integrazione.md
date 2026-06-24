# Inversione dell'ordine di integrazione

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 22-33
- Affidabilita': alta

## Metodo

1. Disegnare il dominio.
2. Identificare le curve che delimitano la regione.
3. Riscrivere il dominio rispetto all'altra variabile.
4. Spezzare il dominio se necessario.

## Esempio: tra $y=x^2$ e $y=x$

$$
\int_0^1 dx\int_{x^2}^{x}xy^2\,dy
=
\int_0^1dy\int_y^{\sqrt{y}}xy^2\,dx
=
\frac{1}{40}.
$$

## Esempio con integranda non elementare

$$
\int_0^1dx\int_x^1e^{y^2}\,dy
=
\int_0^1dy\int_0^ye^{y^2}\,dx
=
\frac{1}{2}(e-1).
$$

## Esempio con dominio da spezzare

Per la regione tra:

$$
y=\frac{1}{x},\qquad y=x,\qquad x=2,
$$

invertendo rispetto a $y$ bisogna spezzare:

$$
\frac{1}{2}\leq y\leq 1,\qquad \frac{1}{y}\leq x\leq 2
$$

e:

$$
1\leq y\leq 2,\qquad y\leq x\leq 2.
$$

## Collegamenti

- [[integrali_iterati]]
- [[integrali_multipli]]
