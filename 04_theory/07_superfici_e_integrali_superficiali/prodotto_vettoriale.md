# Prodotto vettoriale

## Stato

- Fonte: `01_sources/official_slides/4_lezione_superfici.pdf`
- Slide: 23-26
- Affidabilita': alta, con nota su convenzione/orientazione
- Ultimo aggiornamento: 2026-06-23

## Definizione geometrica

Dati due vettori:

$$
v=
\begin{pmatrix}
v_1\\
v_2\\
v_3
\end{pmatrix}
$$

e:

$$
w=
\begin{pmatrix}
w_1\\
w_2\\
w_3
\end{pmatrix},
$$

il loro prodotto vettoriale e':

$$
v\times w
=
\|v\|\|w\|\sin\alpha\, n,
$$

dove $\alpha$ e' l'angolo tra i due vettori e $n$ e' un versore ortogonale al piano generato da $v$ e $w$.

## Formula in coordinate

$$
v\times w
=
\begin{pmatrix}
v_2w_3-v_3w_2\\
v_3w_1-v_1w_3\\
v_1w_2-v_2w_1
\end{pmatrix}.
$$

## Uso per superfici

Per una superficie parametrizzata $\mathbf{x}(u,v)$, il vettore:

$$
\mathbf{x}_u\times \mathbf{x}_v
$$

e' normale al piano tangente.

## Nota di attenzione

La slide cita la "regola della mano sinistra". Nella maggior parte dei corsi si usa la regola della mano destra; verificare la convenzione nelle lezioni successive prima di usarla per orientazioni, flussi, Stokes e Gauss.

## Collegamenti

- [[piano_tangente_superfici]]

