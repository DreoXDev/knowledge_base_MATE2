# Formula: restrizione di una funzione a una superficie

## Stato

- Fonte: `01_sources/official_slides/4_lezione_superfici.pdf`
- Slide: 9-13
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Setup

Sia $\mathbf{x}:D\subset\mathbb{R}^2\to\mathbb{R}^3$ una superficie regolare e sia $f:\mathbb{R}^3\to\mathbb{R}$.

## Restrizione

$$
F(s,t)=f(x(s,t),y(s,t),z(s,t)).
$$

## Formula

Se $f$ e' differenziabile:

$$
F_s(\bar{s},\bar{t})
=
\nabla f(P)\cdot \mathbf{x}_s(\bar{s},\bar{t})
$$

e:

$$
F_t(\bar{s},\bar{t})
=
\nabla f(P)\cdot \mathbf{x}_t(\bar{s},\bar{t}),
$$

dove $P=\mathbf{x}(\bar{s},\bar{t})$.

## Collegamenti

- [[restrizione_funzione_superficie]]
- [[gradiente_derivata_direzionale]]

