# Esercizi - Integrali di superficie e flusso

## Area della sfera

Parametrizzazione:

$$
x=R\cos\theta\cos\varphi,\qquad
y=R\cos\theta\sin\varphi,\qquad
z=R\sin\theta
$$

con $-\frac{\pi}{2}\leq\theta\leq\frac{\pi}{2}$ e $0\leq\varphi\leq2\pi$.

Poiche':

$$
\|r_\theta\times r_\varphi\|=R^2\cos\theta
$$

si ottiene:

$$
mS=\int_0^{2\pi}\int_{-\pi/2}^{\pi/2}R^2\cos\theta\,d\theta\,d\varphi=4\pi R^2
$$

## Area di un grafico

Per $z=f(x,y)$:

$$
r_x=(1,0,f_x),\qquad r_y=(0,1,f_y)
$$

e:

$$
r_x\times r_y=(-f_x,-f_y,1)
$$

Quindi:

$$
mS=\iint_D\sqrt{1+f_x^2+f_y^2}\,dx\,dy
$$

## Porzione di sfera nel cilindro

Per la sfera:

$$
z=\pm\sqrt{R^2-x^2-y^2}
$$

contenuta nel cilindro $x^2+y^2\leq a^2$, con $a<R$, considerando le due calotte:

$$
mD=4\pi R\int_0^a\frac{\rho}{\sqrt{R^2-\rho^2}}\,d\rho
$$

e quindi:

$$
mD=4\pi\left(R^2-R\sqrt{R^2-a^2}\right)
$$

## Flusso attraverso il triangolo $x+y+z=1$

Sia:

$$
F=(x,y,z)
$$

Sul triangolo $T=\{x\geq0,\ y\geq0,\ x+y\leq1\}$ si usa:

$$
r(x,y)=(x,y,1-x-y)
$$

Con orientazione verso l'alto:

$$
F(r(x,y))\cdot(r_x\times r_y)=1
$$

Percio':

$$
\iint_SF\cdot n\,dS=\iint_T1\,dx\,dy=\frac{1}{2}
$$
