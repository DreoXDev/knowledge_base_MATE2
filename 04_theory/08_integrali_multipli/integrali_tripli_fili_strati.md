# Integrali tripli: fili e strati

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 35-43
- Affidabilita': alta

## Integrazione per fili

Se $D$ e' regolare nella direzione $z$, con proiezione $S$ sul piano $xy$ e:

$$
z_1(x,y)\leq z\leq z_2(x,y),
$$

allora:

$$
\iiint_D f(x,y,z)\,dx\,dy\,dz
=
\iint_S dx\,dy
\int_{z_1(x,y)}^{z_2(x,y)}
f(x,y,z)\,dz.
$$

## Integrazione per strati

Se $S_z$ sono le sezioni del dominio con piani paralleli al piano $xy$:

$$
\iiint_D f(x,y,z)\,dx\,dy\,dz
=
\int_a^b dz
\iint_{S_z}f(x,y,z)\,dx\,dy.
$$

## Esempio: tetraedro

Per il tetraedro:

$$
x=0,\qquad y=0,\qquad z=0,\qquad x+y+z=1,
$$

si usa:

$$
0\leq x\leq 1,\qquad 0\leq y\leq 1-x,\qquad 0\leq z\leq 1-x-y.
$$

Per l'integrale della lezione il risultato e':

$$
\frac{1}{2}\ln2-\frac{5}{16}.
$$

## Esempio: volume ellissoide

Per:

$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1,
$$

le sezioni $z=\bar z$ sono ellissi di area:

$$
\pi ab\left(1-\frac{\bar z^2}{c^2}\right).
$$

Il volume e':

$$
V=\frac{4}{3}\pi abc.
$$
