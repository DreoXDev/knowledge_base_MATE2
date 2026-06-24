# Superfici di livello

## Stato

- Fonte: `01_sources/official_slides/4_lezione_superfici.pdf`
- Slide: 14-15, 21-22
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Definizione

Sia:

$$
f:\mathbb{R}^3\to\mathbb{R}.
$$

Una superficie regolare $S$ di parametrizzazione:

$$
\mathbf{x}(s,t)=
\begin{pmatrix}
x(s,t)\\
y(s,t)\\
z(s,t)
\end{pmatrix}
$$

e' una superficie di livello di $f$ se la restrizione di $f$ a $S$ e' costante:

$$
f(x(s,t),y(s,t),z(s,t))=\text{costante}.
$$

## Esempio

Per:

$$
f(x,y,z)=x^2+y^2+z^2
$$

le superfici di livello esistono per $c\geq 0$ e sono sfere centrate nell'origine di raggio:

$$
\sqrt{c}.
$$

## Gradiente ortogonale alle superfici di livello

Se $S$ e' una superficie di livello di $f$, allora:

$$
F_s=\nabla f\cdot \mathbf{x}_s=0
$$

e:

$$
F_t=\nabla f\cdot \mathbf{x}_t=0.
$$

Quindi il gradiente di $f$ e' ortogonale ai vettori $\mathbf{x}_s$ e $\mathbf{x}_t$, che sono tangenti alla superficie e linearmente indipendenti.

Di conseguenza $\nabla f$ e' ortogonale alle superfici di livello.

## Piano tangente a una superficie di livello

Se $S$ e' definita da:

$$
F(x,y,z)=c,
$$

l'equazione cartesiana del piano tangente a $S$ nel punto:

$$
\bar{x}=(\bar{x},\bar{y},\bar{z})
$$

e':

$$
F_x(\bar{x})(x-\bar{x})
+
F_y(\bar{x})(y-\bar{y})
+
F_z(\bar{x})(z-\bar{z})
=
0.
$$

## Esempio: sfera

Per:

$$
F(x,y,z)=x^2+y^2+z^2=1
$$

nel punto $(0,1,0)$:

$$
\nabla F(0,1,0)=
\begin{pmatrix}
0\\
2\\
0
\end{pmatrix}.
$$

Quindi:

$$
2(y-1)=0
$$

ossia:

$$
y=1.
$$

## Collegamenti

- [[gradiente_derivata_direzionale]]
- [[piano_tangente_superfici]]
- [[gradiente_superfici_livello]]

