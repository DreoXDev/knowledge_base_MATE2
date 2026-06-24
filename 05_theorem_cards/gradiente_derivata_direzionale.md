# Formula: gradiente e derivata direzionale

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 25-26
- Affidabilita': alta
- Dimostrazione richiesta: no
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per calcolare la variazione istantanea di una funzione lungo una direzione.

## Gradiente

$$
\nabla f=
\left(
\frac{\partial f}{\partial x_1},
\dots,
\frac{\partial f}{\partial x_n}
\right).
$$

## Derivata direzionale

Se $v$ e' unitario:

$$
L_v(f)(P)=\nabla f(P)\cdot v.
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

## Collegamenti

- [[gradiente_derivata_direzionale]]
- [[derivata_lungo_curva]]

