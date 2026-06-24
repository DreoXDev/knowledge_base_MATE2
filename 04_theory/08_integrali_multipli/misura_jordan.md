# Misura di Jordan

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 1-6
- Affidabilita': alta

## Definizione

A un dominio $\Omega\subset\mathbb{R}^n$ con frontiera differenziabile si associa un numero positivo:

$$
m\Omega
$$

detto misura di Jordan. Per $n=2$ e' l'area; per $n=3$ e' il volume.

## Proprietà

Per un parallelepipedo rettangolo:

$$
a_j\leq x_j\leq b_j,\qquad j=1,\dots,n,
$$

la misura e':

$$
m\Delta=(b_1-a_1)\cdots(b_n-a_n).
$$

Se $\Omega_1\subset\Omega_2$, allora $m\Omega_1\leq m\Omega_2$.

Se $\Omega$ e' suddiviso in due regioni senza interni comuni:

$$
m\Omega=m\Omega_1+m\Omega_2.
$$

## Misurabilita' nel piano

Con approssimazioni per difetto e per eccesso:

$$
m_i\Omega=\lim_{N\to\infty}m\Omega_N^{int},\qquad
m_e\Omega=\lim_{N\to\infty}m\Omega_N^{est}.
$$

Se:

$$
m_i\Omega=m_e\Omega,
$$

allora $\Omega$ e' misurabile o quadrabile.

Un insieme piano e' misurabile se la sua frontiera ha misura nulla. In particolare, ogni dominio con frontiera curva differenziabile a tratti e' misurabile.

## Collegamenti

- [[integrali_multipli]]
