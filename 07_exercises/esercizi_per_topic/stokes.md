# Esercizi - Formula di Stokes

## Piano nel primo ottante

Campo:

$$
F=(xz,xy,3xz)
$$

Superficie: porzione del piano:

$$
2x+y+z=2
$$

nel primo ottante, orientata verso l'alto.

Il rotore e':

$$
\operatorname{rot}(F)=(0,x-3z,y)
$$

Con:

$$
r(x,y)=(x,y,2-2x-y)
$$

si ha:

$$
r_x\times r_y=(2,1,1)
$$

e:

$$
\operatorname{rot}(F)\cdot(r_x\times r_y)=7x+4y-6
$$

Sul dominio $0\leq x\leq1$, $0\leq y\leq2-2x$:

$$
\int_0^1\int_0^{2-2x}(7x+4y-6)\,dy\,dx=-1
$$

Quindi la circuitazione sul bordo vale $-1$.

## Emisfero superiore

Campo:

$$
F=(y,-x,0)
$$

Superficie: emisfero superiore della sfera:

$$
x^2+y^2+z^2=9
$$

orientato verso l'alto.

Sul bordo:

$$
x=3\cos t,\qquad y=3\sin t,\qquad z=0
$$

con $t\in[0,2\pi]$. Il primo membro di Stokes vale:

$$
-18\pi
$$

Il rotore e':

$$
\operatorname{rot}(F)=-2e_3
$$

e il flusso del rotore sull'emisfero da' lo stesso risultato.

## Porzione sferica con rotore nullo

Campo:

$$
F=(yz,xz,xy)
$$

Superficie: porzione della sfera $x^2+y^2+z^2=4$ con $z\geq0$, ritagliata dal cilindro $x^2+y^2=1$, orientata verso l'alto.

Si ha:

$$
\operatorname{rot}(F)=0
$$

Inoltre il campo ha potenziale:

$$
U=xyz
$$

quindi anche l'integrale di linea sul bordo e' nullo.
