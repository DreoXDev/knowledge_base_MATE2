# Teorema: Stokes

## Stato

- Fonte: Lezione 11, slide 20-34.
- Affidabilita': alta.
- Ultimo aggiornamento: 2026-06-24

## Enunciato

Se $S$ e' una superficie orientata con bordo $C=\partial S$ e $F$ ha componenti continue con derivate parziali continue, allora:

$$
\oint_C F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

## Ipotesi

- $S$ orientata.
- $C=\partial S$ orientata in modo compatibile con $n$.
- $F$ sufficientemente regolare su $S$ e sulla frontiera.

## Significato intuitivo

La circuitazione lungo il bordo e' la somma della rotazione locale del campo sulla superficie.

## Punti delicati

- Il verso di $C$ non e' arbitrario.
- Se si cambia $n$, cambia anche il verso positivo del bordo.
- Green e' il caso piano di Stokes.

## Esempio standard

Per $F=(xz,xy,3xz)$ sul piano $2x+y+z=2$ nel primo ottante, orientato verso l'alto, entrambi i membri valgono $-1$.

## Collegamenti

- [[formula_stokes]]
- [[green]]
- [[rotore]]
