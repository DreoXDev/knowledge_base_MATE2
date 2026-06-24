# Campi conservativi e potenziale

## Stato

- Fonte: `01_sources/official_slides/8_lezione_integrali_linea_II_specie.pdf`
- Slide: 18-22
- Affidabilita': alta

## Gradiente

Data una funzione:

$$
U:D\subset\mathbb{R}^n\to\mathbb{R}
$$

il suo gradiente e':

$$
\nabla U=
\left(
\frac{\partial U}{\partial x_1},
\dots,
\frac{\partial U}{\partial x_n}
\right).
$$

## Campo conservativo

Un campo vettoriale $F$ si dice conservativo o potenziale se esiste una funzione:

$$
U:D\to\mathbb{R}
$$

tale che:

$$
F=\nabla U.
$$

La funzione $U$ si chiama potenziale del campo $F$.

## Teorema: indipendenza dal cammino

Se $F$ e' conservativo e continuo in un dominio $D$, e se $C$ e' una curva regolare orientata contenuta in $D$, allora:

$$
\int_C F\cdot \tau\,d\ell
=
U(P_1)-U(P_0)
$$

dove $P_0$ e $P_1$ sono gli estremi della curva.

## Significato

Per un campo conservativo, l'integrale di linea di II specie dipende solo dagli estremi del cammino e non dal cammino scelto.

## Dimostrazione

Sia $r(t)=(x_1(t),\dots,x_n(t))$ una parametrizzazione concorde con l'orientazione.

Allora:

$$
\int_C F\cdot \tau\,d\ell
=
\int_{t_0}^{t_1}
F(r(t))\cdot r'(t)\,dt.
$$

Poiche' $F=\nabla U$:

$$
F(r(t))\cdot r'(t)
=
\nabla U(r(t))\cdot r'(t)
=
\frac{d}{dt}U(r(t))
$$

per la regola della funzione composta.

Quindi:

$$
\int_C F\cdot \tau\,d\ell
=
\int_{t_0}^{t_1}
\frac{d}{dt}U(r(t))\,dt
=
U(r(t_1))-U(r(t_0))
$$

cioe':

$$
U(P_1)-U(P_0).
$$

## Esempio

Per:

$$
F=(3x^2y,x^3+1)
$$

un potenziale e':

$$
U(x,y)=x^3y+y.
$$

Quindi per ogni cammino da $(0,0)$ a $(1,1)$:

$$
\int_C F\cdot \tau\,d\ell
=
U(1,1)-U(0,0)
=
2
$$

indipendentemente dal cammino.

## Collegamenti

- [[integrali_linea_II_specie]]
- [[campi_conservativi_indipendenza_cammino]]
- [[potenziale]]
