# Area di una superficie

## Superficie parametrizzata

Sia $S$ una superficie regolare parametrizzata da:

$$
r(u,v)=(x(u,v),y(u,v),z(u,v))
$$

con $(u,v)\in D\subset\mathbb{R}^2$. L'elemento di area e':

$$
dS=\|r_u\times r_v\|\,du\,dv
$$

quindi:

$$
mS=\iint_D\|r_u\times r_v\|\,du\,dv
$$

Il prodotto vettoriale $r_u\times r_v$ misura l'area del parallelogramma infinitesimo generato dai due vettori tangenti.

## Grafico di una funzione

Se $S$ e' il grafico:

$$
z=f(x,y)
$$

allora:

$$
r_x=(1,0,f_x),\qquad r_y=(0,1,f_y)
$$

e:

$$
r_x\times r_y=(-f_x,-f_y,1)
$$

Percio':

$$
dS=\sqrt{1+f_x^2+f_y^2}\,dx\,dy
$$

e:

$$
mS=\iint_D\sqrt{1+f_x^2+f_y^2}\,dx\,dy
$$

## Superficie di livello

Se la superficie e' data da:

$$
F(x,y,z)=c
$$

e localmente si puo' scrivere come grafico $z=f(x,y)$, allora dal teorema della funzione implicita:

$$
f_x=-\frac{F_x}{F_z},\qquad f_y=-\frac{F_y}{F_z}
$$

quindi:

$$
dS=\frac{\|\nabla F\|}{|F_z|}\,dx\,dy
$$

sulla proiezione della superficie sul piano $xy$.

## Esempio: area della sfera

Con la convenzione del corso:

$$
x=R\cos\theta\cos\varphi,\qquad y=R\cos\theta\sin\varphi,\qquad z=R\sin\theta
$$

con $-\frac{\pi}{2}\leq\theta\leq\frac{\pi}{2}$ e $0\leq\varphi\leq2\pi$, si ha:

$$
\|r_\theta\times r_\varphi\|=R^2\cos\theta
$$

percio':

$$
mS=\int_0^{2\pi}\int_{-\pi/2}^{\pi/2}R^2\cos\theta\,d\theta\,d\varphi=4\pi R^2
$$

## Punti delicati

- La formula dell'area non dipende dall'orientazione, perche' usa la norma $\|r_u\times r_v\|$.
- Per il flusso invece si usa il vettore normale orientato, quindi il segno conta.
- Nella lezione 11 la convenzione sferica usa $\theta$ come latitudine.

## Collegamenti

- [[integrali_superficie_I_specie]]
- [[superfici_parametrizzate]]
- [[funzione_implicita_tre_variabili]]
