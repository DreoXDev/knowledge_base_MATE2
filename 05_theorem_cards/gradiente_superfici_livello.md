# Risultato: gradiente ortogonale alle superfici di livello

## Stato

- Fonte: `01_sources/official_slides/4_lezione_superfici.pdf`
- Slide: 14-15
- Affidabilita': alta
- Dimostrazione richiesta: si
- Ultimo aggiornamento: 2026-06-23

## Enunciato

Se $S$ e' una superficie di livello di $f:\mathbb{R}^3\to\mathbb{R}$, allora $\nabla f$ e' ortogonale a $S$.

## Dimostrazione

Se $S$ e' parametrizzata da $\mathbf{x}(s,t)$ e:

$$
f(\mathbf{x}(s,t))=c,
$$

allora la restrizione $F(s,t)$ e' costante. Quindi:

$$
F_s=0,\qquad F_t=0.
$$

Per la regola composta su superfici:

$$
F_s=\nabla f\cdot \mathbf{x}_s=0
$$

e:

$$
F_t=\nabla f\cdot \mathbf{x}_t=0.
$$

Poiche' $\mathbf{x}_s$ e $\mathbf{x}_t$ generano il piano tangente, $\nabla f$ e' ortogonale al piano tangente.

## Collegamenti

- [[superfici_di_livello]]
- [[piano_tangente_superficie_livello]]

