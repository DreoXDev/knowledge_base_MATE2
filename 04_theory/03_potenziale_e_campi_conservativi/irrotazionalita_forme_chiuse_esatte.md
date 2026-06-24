# Irrotazionalita', forme chiuse ed esatte

## Stato

- Fonte: `01_sources/official_slides/9_lezione_campi_vettoriali_conservativi.pdf`
- Slide: 13-16, 36
- Affidabilita': alta

## Condizioni necessarie

Se $F=\nabla U$ e le derivate parziali sono continue, allora:

$$
\frac{\partial F_i}{\partial x_j}
=
\frac{\partial F_j}{\partial x_i}.
$$

Nel piano, per $F=(P,Q)$:

$$
P_y=Q_x.
$$

In $\mathbb{R}^3$:

$$
F_{1,y}=F_{2,x},\qquad
F_{1,z}=F_{3,x},\qquad
F_{3,y}=F_{2,z}.
$$

## Forme chiuse ed esatte

Per:

$$
\omega=F_1\,dx_1+\cdots+F_n\,dx_n,
$$

la forma e' chiusa se soddisfa le condizioni di irrotazionalita'.

La forma e' esatta se:

$$
\omega=dU
$$

cioe':

$$
\omega=
\frac{\partial U}{\partial x_1}\,dx_1+\cdots+
\frac{\partial U}{\partial x_n}\,dx_n.
$$

Traduzione:

- forma esatta equivale a campo conservativo;
- forma chiusa equivale a campo irrotazionale;
- ogni forma esatta e' chiusa;
- in domini semplicemente connessi, ogni forma chiusa e' esatta.

## Lemma di Poincare'

Se $F:D\subset\mathbb{R}^n\to\mathbb{R}^n$ e' di classe $C^1$, $D$ e' semplicemente connesso e valgono le condizioni:

$$
\frac{\partial F_i}{\partial x_j}
=
\frac{\partial F_j}{\partial x_i},
$$

allora $F$ ammette potenziale in $D$.

## Collegamenti

- [[domini_semplicemente_connessi]]
- [[lemma_poincare]]
- [[campi_non_semplicemente_connessi]]
