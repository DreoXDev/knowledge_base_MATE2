# Definizione: misura di Jordan

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 1-6
- Affidabilita': alta

## Definizione

A un dominio $\Omega\subset\mathbb{R}^n$ con frontiera regolare a tratti si associa un numero positivo $m\Omega$, detto misura di Jordan.

Per $n=2$ si parla di area; per $n=3$ si parla di volume.

## Costruzione nel piano

Si approssima $\Omega$ con quadrati di reticolo:

- per difetto, usando quadrati contenuti in $\Omega$;
- per eccesso, usando quadrati che incontrano $\overline{\Omega}$.

Le aree limite sono:

$$
m_i\Omega=\lim_{N\to\infty}m\Omega_N^{int},
\qquad
m_e\Omega=\lim_{N\to\infty}m\Omega_N^{est}.
$$

Il dominio e' misurabile se:

$$
m_i\Omega=m_e\Omega.
$$

## Criterio

Un insieme piano e' misurabile secondo Jordan se la frontiera ha misura nulla.

## Collegamenti

- [[misura_jordan]]
- [[integrali_multipli]]

