# Esercizi - Superfici e piano tangente

## Esercizio 1 - Restrizione di una funzione a un piano

### Traccia

Sia il piano:

$$
x=1+2s,\qquad y=s-t,\qquad z=1+s+3t
$$

e sia:

$$
f(x,y,z)=y^2+x-z.
$$

Calcolare la restrizione di $f$ al piano.

### Svolgimento

$$
F(s,t)
=
(s-t)^2+1+2s-1-s-3t
$$

quindi:

$$
F(s,t)=s^2-2st+t^2+s-3t.
$$

---

## Esercizio 2 - Derivate della restrizione tramite gradiente

### Traccia

Per la funzione dell'esercizio precedente calcolare $F_s(0,0)$ e $F_t(0,0)$.

### Svolgimento diretto

$$
F_s=2s-2t+1
$$

$$
F_t=-2s+2t-3
$$

quindi:

$$
F_s(0,0)=1,\qquad F_t(0,0)=-3.
$$

### Svolgimento con gradiente

$$
P=(1,0,1)
$$

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

$$
F_s(0,0)=\nabla f(1,0,1)\cdot \mathbf{x}_s(0,0)=1
$$

$$
F_t(0,0)=\nabla f(1,0,1)\cdot \mathbf{x}_t(0,0)=-3.
$$

---

## Esercizio 3 - Piano tangente alla sfera parametrizzata

### Traccia

Sia la sfera:

$$
\mathbf{x}(\theta,\varphi)
=
\begin{pmatrix}
\cos\theta\cos\varphi\\
\cos\theta\sin\varphi\\
\sin\theta
\end{pmatrix}.
$$

Calcolare il piano tangente nel punto:

$$
\mathbf{x}\left(0,\frac{\pi}{2}\right)=(0,1,0).
$$

### Svolgimento

$$
\mathbf{x}_\theta\left(0,\frac{\pi}{2}\right)
=
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}
$$

$$
\mathbf{x}_\varphi\left(0,\frac{\pi}{2}\right)
=
\begin{pmatrix}
-1\\
0\\
0
\end{pmatrix}.
$$

Forma parametrica:

$$
x=-t,\qquad y=1,\qquad z=s.
$$

Forma cartesiana:

$$
y=1.
$$

---

## Esercizio 4 - Piano tangente alla sfera come superficie di livello

### Traccia

Considerare la sfera:

$$
F(x,y,z)=x^2+y^2+z^2=1.
$$

Calcolare il piano tangente nel punto $(0,1,0)$.

### Svolgimento

$$
\nabla F(x,y,z)=
\begin{pmatrix}
2x\\
2y\\
2z
\end{pmatrix}
$$

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

---

## Esercizio 5 - Prodotto vettoriale dei vettori tangenti della sfera

### Traccia

Calcolare:

$$
\mathbf{x}_\theta\left(0,\frac{\pi}{2}\right)
\times
\mathbf{x}_\varphi\left(0,\frac{\pi}{2}\right)
$$

dove:

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

### Risultato

$$
\mathbf{x}_\theta\left(0,\frac{\pi}{2}\right)
\times
\mathbf{x}_\varphi\left(0,\frac{\pi}{2}\right)
=
\begin{pmatrix}
0\\
-1\\
0
\end{pmatrix}.
$$

