# Esercizi - Funzione implicita

## Esercizio 1 - Circonferenza

Studiare localmente:

$$
x^2+y^2=1
$$

come grafico $y=f(x)$.

Pongo:

$$
F(x,y)=x^2+y^2-1.
$$

Poiche':

$$
F_y=2y,
$$

il teorema si applica dove $y\neq 0$, quindi in tutti i punti della circonferenza eccetto $(1,0)$ e $(-1,0)$.

Nel semipiano superiore:

$$
y=\sqrt{1-x^2}
$$

e:

$$
f'=-\frac{x}{\sqrt{1-x^2}}=-\frac{F_x}{F_y}.
$$

## Esercizio 2 - Sfera

Studiare localmente:

$$
x^2+y^2+z^2=1
$$

come grafico $z=f(x,y)$.

Pongo:

$$
F(x,y,z)=x^2+y^2+z^2-1.
$$

Poiche':

$$
F_z=2z,
$$

il teorema si applica dove $z\neq 0$, quindi nei punti non situati sull'equatore.

Nel semispazio inferiore:

$$
z=-\sqrt{1-x^2-y^2}.
$$

Le derivate sono:

$$
f_x=\frac{x}{\sqrt{1-x^2-y^2}},\qquad
f_y=\frac{y}{\sqrt{1-x^2-y^2}},
$$

e coincidono con:

$$
f_x=-\frac{F_x}{F_z},\qquad
f_y=-\frac{F_y}{F_z}.
$$
