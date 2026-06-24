# Restrizione di una funzione a una superficie

## Stato

- Fonte: `01_sources/official_slides/4_lezione_superfici.pdf`
- Slide: 9-13
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Definizione

Sia:

$$
\mathbf{x}:D\subset\mathbb{R}^2\to\mathbb{R}^3
$$

una superficie parametrizzata regolare $S$, e sia:

$$
f:\mathbb{R}^3\to\mathbb{R}.
$$

La restrizione di $f$ a $S$ e':

$$
F(s,t)=f(x(s,t),y(s,t),z(s,t)).
$$

## Regola della funzione composta

Se $f$ e' differenziabile e $\mathbf{x}$ e' regolare, allora:

$$
F_s(\bar{s},\bar{t})
=
\nabla f(P)\cdot \mathbf{x}_s(\bar{s},\bar{t})
$$

e:

$$
F_t(\bar{s},\bar{t})
=
\nabla f(P)\cdot \mathbf{x}_t(\bar{s},\bar{t})
$$

dove:

$$
P=\mathbf{x}(\bar{s},\bar{t}).
$$

La dimostrazione e' analoga al caso delle curve.

## Esempio ufficiale

Piano:

$$
x=1+2s,\qquad y=s-t,\qquad z=1+s+3t.
$$

Funzione:

$$
f(x,y,z)=y^2+x-z.
$$

Restrizione:

$$
F(s,t)
=
(s-t)^2+1+2s-1-s-3t
$$

quindi:

$$
F(s,t)=s^2-2st+t^2+s-3t.
$$

Nel punto $(s,t)=(0,0)$:

$$
F_s(0,0)=1,\qquad F_t(0,0)=-3.
$$

Con il gradiente:

$$
\nabla f(1,0,1)=
\begin{pmatrix}
1\\
0\\
-1
\end{pmatrix}
$$

$$
\mathbf{x}_s(0,0)=
\begin{pmatrix}
2\\
1\\
1
\end{pmatrix}
$$

$$
\mathbf{x}_t(0,0)=
\begin{pmatrix}
0\\
-1\\
3
\end{pmatrix}
$$

si ottengono gli stessi valori tramite prodotto scalare:

$$
F_s(0,0)=1,\qquad F_t(0,0)=-3.
$$

## Domande orali

- Che cos'e' la restrizione di una funzione a una superficie?
- Come si calcolano le derivate parziali della restrizione?
- Qual e' il ruolo del gradiente?
- In che senso questa formula generalizza la restrizione a curve?

## Collegamenti

- [[superfici_parametrizzate]]
- [[superfici_di_livello]]

