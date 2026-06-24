# Definizione: integrale multiplo

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 7-14
- Affidabilita': alta

## Definizione

Dato un dominio limitato $D\subset\mathbb{R}^n$, si divide $D$ in parti $\Omega^{(j)}$ e si sceglie un punto $\xi^{(j)}$ in ciascuna parte.

La somma di Riemann e':

$$
S_\rho(f)=
\sum_{j=1}^{N}
f(\xi^{(j)})m\Omega^{(j)}.
$$

Se il limite per $d(\rho)\to 0$ esiste, si definisce:

$$
\int_D f(x)\,d\Omega
=
\lim_{d(\rho)\to0}S_\rho(f).
$$

## Caso $f=1$

Se $f=1$, l'integrale restituisce la misura del dominio:

$$
\int_D1\,d\Omega=mD.
$$

## Collegamenti

- [[integrali_multipli]]
- [[misura_jordan]]

