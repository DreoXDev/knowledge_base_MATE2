# Teorema: integrazione per fili

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 35-41
- Affidabilita': alta

## Enunciato

Sia $D\subset\mathbb{R}^3$ regolare nella direzione $z$ e sia $S$ la sua proiezione sul piano $xy$.

Se:

$$
z_1(x,y)\leq z\leq z_2(x,y)
$$

allora:

$$
\iiint_D f(x,y,z)\,dx\,dy\,dz
=
\iint_S dx\,dy
\int_{z_1(x,y)}^{z_2(x,y)}
f(x,y,z)\,dz.
$$

## Idea

Si fissano $(x,y)$ nella proiezione e si integra lungo il filo parallelo all'asse $z$.

## Collegamenti

- [[integrali_tripli_fili_strati]]
- [[integrazione_per_strati]]

