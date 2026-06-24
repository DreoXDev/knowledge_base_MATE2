# Integrali multipli

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 7-14
- Affidabilita': alta

## Somme di Riemann

Sia $D\subset\mathbb{R}^n$ un dominio limitato con frontiera differenziabile a tratti e sia $f$ limitata su $D$.

Si divide $D$ in parti $\Omega^{(j)}$ e si sceglie un punto:

$$
\xi^{(j)}\in\Omega^{(j)}.
$$

La somma di Riemann e':

$$
S_\rho(f)=
\sum_{j=1}^{N}
f(\xi^{(j)})m\Omega^{(j)}.
$$

## Definizione

Se esiste:

$$
\lim_{d(\rho)\to 0}S_\rho(f),
$$

dove $d(\rho)$ e' il massimo dei diametri delle parti, allora si definisce l'integrale multiplo:

$$
\int_D f(x)\,d\Omega.
$$

Spesso si scrive:

$$
\int\cdots\int_D f(x_1,\dots,x_n)\,dx_1\cdots dx_n.
$$

## Caso $f=1$

Se $f=1$:

$$
\int_D1\,d\Omega=mD.
$$

Nel piano restituisce l'area; nello spazio restituisce il volume.

## Contributo della frontiera

Nelle suddivisioni rettangolari, i pezzi incompleti vicino alla frontiera sono trascurabili perché la frontiera ha misura nulla e $f$ e' limitata.

## Collegamenti

- [[misura_jordan]]
- [[proprieta_integrali_multipli]]
- [[integrali_iterati]]
