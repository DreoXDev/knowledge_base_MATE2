# Gradiente e derivata direzionale

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 25-26
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Gradiente

Il gradiente di $f$ e' la funzione a valori vettoriali:

$$
\nabla f=
\left(
\frac{\partial f}{\partial x_1},
\dots,
\frac{\partial f}{\partial x_n}
\right).
$$

La differenziabilita' puo' essere scritta come:

$$
\Delta f=
\nabla f(P)\cdot \Delta x+o(\rho),
$$

dove:

$$
\Delta x=(\Delta x_1,\dots,\Delta x_n).
$$

## Derivata lungo una curva

La formula della derivata lungo una curva puo' essere riscritta come:

$$
F'(\bar{t})
=
\left.
\frac{d}{dt}
\right|_{t=\bar{t}}
f(x(t))
=
\nabla f(P)\cdot
\frac{dx}{dt}(\bar{t}).
$$

## Derivata direzionale

Se $v$ e' un vettore unitario, il prodotto scalare:

$$
\nabla f(P)\cdot v
$$

si dice derivata di $f$ nella direzione di $v$ nel punto $P$ e si indica con:

$$
L_v(f)(P).
$$

Equivalentemente:

$$
L_v(f)(P)
=
\left.
\frac{d}{dt}
\right|_{t=0}
f(P+vt).
$$

## Intuizione geometrica

La derivata direzionale misura la variazione istantanea della funzione quando ci si muove da $P$ nella direzione unitaria $v$.

## Collegamenti

- [[restrizione_funzione_curva]]
- [[curve_di_livello]]
- [[gradiente_derivata_direzionale]]

