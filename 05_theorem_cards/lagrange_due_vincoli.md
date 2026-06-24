# Lagrange con due vincoli

## Stato

- Fonte: `01_sources/official_slides/5_lezione_moltiplicatori_lagrange.pdf`
- Slide: 28-42
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Setup

$$
f(x,y,z)
$$

vincolata a:

$$
G_1(x,y,z)=c_1
$$

$$
G_2(x,y,z)=c_2
$$

con $\nabla G_1$ e $\nabla G_2$ linearmente indipendenti.

## Sistema

$$
\nabla f
=
\lambda_1\nabla G_1+\lambda_2\nabla G_2
$$

$$
G_1=c_1
$$

$$
G_2=c_2.
$$

## Interpretazione

Il gradiente di $f$ appartiene al piano normale alla curva intersezione, generato da $\nabla G_1$ e $\nabla G_2$.

## Esempi

- Intersezione di $x+y+z=0$ e $x-z=1$: punto minimo $\left(\frac{1}{2},0,-\frac{1}{2}\right)$.
- Intersezione di $2x-3y-z=4$ e $x-2y-2z=1$: punto minimo $(1,-1,1)$.

## Collegamenti

- [[lagrange_due_vincoli]]
- [[lagrange]]

