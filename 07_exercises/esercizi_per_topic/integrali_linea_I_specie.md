# Esercizi - Integrali di linea di I specie

## Esercizio 1 - Semicirconferenza

Calcolare:

$$
\int_C xy^4\,d\ell
$$

dove $C$ e' la semicirconferenza:

$$
x^2+y^2=16,\qquad x\geq 0.
$$

Parametrizzazione:

$$
x(t)=4\cos t,\qquad y(t)=4\sin t
$$

con:

$$
t\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right].
$$

Elemento di lunghezza:

$$
d\ell=4\,dt.
$$

Calcolo:

$$
\int_C xy^4\,d\ell
=
4^6
\int_{-\pi/2}^{\pi/2}
\cos t\sin^4 t\,dt.
$$

Ponendo $u=\sin t$:

$$
4^6\int_{-1}^{1}u^4\,du
=
\frac{2}{5}4^6.
$$

Risultato:

$$
\frac{2}{5}4^6=1638.4.
$$

## Esercizio 2 - Baricentro di un'elica

Calcolare il baricentro dell'arco di elica:

$$
x=a\cos t,\qquad y=a\sin t,\qquad z=ht
$$

con $t\in[0,b]$, supponendo il filo omogeneo.

Elemento di lunghezza:

$$
d\ell=\sqrt{a^2+h^2}\,dt.
$$

Lunghezza:

$$
L=b\sqrt{a^2+h^2}.
$$

Risultato:

$$
x_G=\frac{a\sin b}{b}
$$

$$
y_G=\frac{a(1-\cos b)}{b}
$$

$$
z_G=\frac{bh}{2}.
$$

## Esercizio 3 - Curva piana con parametro $t$

Calcolare:

$$
\int_C \sqrt{x^2+y^2}\,d\ell
$$

dove:

$$
x(t)=a(\cos t+t\sin t)
$$

$$
y(t)=a(\sin t-t\cos t)
$$

con $t\in[0,2\pi]$.

Restrizione dell'integranda:

$$
\sqrt{x^2+y^2}=|a|\sqrt{1+t^2}.
$$

Derivata:

$$
r'(t)=
\begin{pmatrix}
at\cos t\\
at\sin t
\end{pmatrix}
$$

e:

$$
\|r'(t)\|=|a|t.
$$

Calcolo:

$$
\int_C \sqrt{x^2+y^2}\,d\ell
=
a^2\int_0^{2\pi}\sqrt{1+t^2}\,t\,dt.
$$

Risultato:

$$
\frac{a^2}{3}\left[(1+4\pi^2)^{3/2}-1\right].
$$

## Esercizio 4 - Quarto di ellisse

Calcolare:

$$
\int_C xy\,d\ell
$$

dove $C$ e' il quarto dell'ellisse:

$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1
$$

nel primo quadrante.

Parametrizzazione:

$$
r(t)=
\begin{pmatrix}
a\cos t\\
b\sin t
\end{pmatrix}
$$

con:

$$
t\in\left[0,\frac{\pi}{2}\right].
$$

Restrizione dell'integranda:

$$
x(t)y(t)=ab\sin t\cos t.
$$

Elemento di lunghezza:

$$
\|r'(t)\|
=
\sqrt{a^2\sin^2t+b^2\cos^2t}
=
\sqrt{(a^2-b^2)\sin^2t+b^2}.
$$

Integrale:

$$
\int_C xy\,d\ell
=
ab
\int_0^{\pi/2}
\sin t\cos t
\sqrt{(a^2-b^2)\sin^2t+b^2}
\,dt.
$$

Risultato:

$$
\frac{ab}{3}
\frac{a^3-b^3}{a^2-b^2}
=
\frac{ab}{3}
\frac{a^2+ab+b^2}{a+b}.
$$

Nota: il caso $a=b$ va trattato come caso limite o calcolato separatamente.
