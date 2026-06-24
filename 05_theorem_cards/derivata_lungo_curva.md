# Teorema: derivata lungo una curva

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 20-24
- Affidabilita': alta
- Dimostrazione richiesta: si
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per derivare la restrizione di una funzione di piu' variabili a una curva parametrizzata.

## Enunciato

Se $f$ e' differenziabile e:

$$
F(t)=f(x_1(t),\dots,x_n(t)),
$$

allora:

$$
F'(\bar{t})
=
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}(P)
\frac{dx_i}{dt}(\bar{t}),
$$

dove:

$$
P=(x_1(\bar{t}),\dots,x_n(\bar{t})).
$$

## Ipotesi

- $f$ differenziabile.
- $x(t)$ curva parametrizzata.
- Le componenti $x_i(t)$ sono derivabili nel punto considerato.

## Dimostrazione

Dalla differenziabilita':

$$
\Delta f=
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}(P)\Delta x_i
+
o(\rho).
$$

Si divide per $\Delta t$:

$$
\frac{\Delta f}{\Delta t}
=
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}(P)
\frac{\Delta x_i}{\Delta t}
+
\frac{o(\rho)}{\Delta t}.
$$

Passando al limite lungo la curva:

$$
F'(\bar{t})
=
\sum_{i=1}^n
\frac{\partial f}{\partial x_i}(P)
\frac{dx_i}{dt}(\bar{t}).
$$

## Collegamenti

- [[restrizione_funzione_curva]]
- [[gradiente_derivata_direzionale]]

