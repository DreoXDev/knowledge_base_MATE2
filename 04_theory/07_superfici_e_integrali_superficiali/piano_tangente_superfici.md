# Piano tangente a superfici

## Stato

- Fonte: `01_sources/official_slides/4_lezione_superfici.pdf`
- Slide: 16-22, 25-26
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Piano in forma parametrica

Dato un punto di passaggio:

$$
\bar{x}=(\bar{x},\bar{y},\bar{z})
$$

e due vettori linearmente indipendenti $v$ e $w$ paralleli al piano, l'equazione parametrica del piano e':

$$
\mathbf{x}=\bar{x}+sv+tw,
\qquad s,t\in\mathbb{R}.
$$

## Piano in forma cartesiana

Dato un vettore normale:

$$
n=
\begin{pmatrix}
a\\
b\\
c
\end{pmatrix},
$$

l'equazione cartesiana del piano e':

$$
a(x-\bar{x})+b(y-\bar{y})+c(z-\bar{z})=0.
$$

## Piano tangente a superficie parametrizzata

Sia $\mathbf{x}(u,v)$ una superficie parametrizzata. L'equazione parametrica del piano tangente a $S$ in $\bar{x}=\mathbf{x}(\bar{u},\bar{v})$ e':

$$
\mathbf{x}
=
\bar{x}
+
s\,\mathbf{x}_u(\bar{u},\bar{v})
+
t\,\mathbf{x}_v(\bar{u},\bar{v}).
$$

In forma cartesiana si puo' usare il normale:

$$
n=
\mathbf{x}_u(\bar{u},\bar{v})
\times
\mathbf{x}_v(\bar{u},\bar{v}).
$$

Se $n=(a,b,c)$, allora:

$$
a(x-\bar{x})+b(y-\bar{y})+c(z-\bar{z})=0.
$$

## Esempio: sfera parametrizzata

Per la sfera di raggio $1$:

$$
\mathbf{x}(\theta,\varphi)
=
\begin{pmatrix}
\cos\theta\cos\varphi\\
\cos\theta\sin\varphi\\
\sin\theta
\end{pmatrix},
$$

nel punto:

$$
\mathbf{x}\left(0,\frac{\pi}{2}\right)=(0,1,0)
$$

si ha:

$$
\mathbf{x}_\theta\left(0,\frac{\pi}{2}\right)
=
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}
$$

e:

$$
\mathbf{x}_\varphi\left(0,\frac{\pi}{2}\right)
=
\begin{pmatrix}
-1\\
0\\
0
\end{pmatrix}.
$$

La forma parametrica e':

$$
x=-t,\qquad y=1,\qquad z=s.
$$

Quindi il piano cartesiano e':

$$
y=1.
$$

Con il prodotto vettoriale:

$$
\mathbf{x}_\theta\left(0,\frac{\pi}{2}\right)
\times
\mathbf{x}_\varphi\left(0,\frac{\pi}{2}\right)
=
\begin{pmatrix}
0\\
-1\\
0
\end{pmatrix},
$$

si ottiene ancora il piano $y=1$.

## Figure

- `08_visuals/figures/lezione_4_slide_18_piano_tangente_parametrico.png`
- `08_visuals/figures/lezione_4_slide_26_prodotto_vettoriale_sfera.png`

## Collegamenti

- [[superfici_parametrizzate]]
- [[superfici_di_livello]]
- [[prodotto_vettoriale]]

