# Coordinate polari, cilindriche e sferiche

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 52-63
- Affidabilita': alta, con nota sulla convenzione sferica finale

## Coordinate polari

$$
x=\rho\cos\theta,\qquad y=\rho\sin\theta.
$$

Jacobiano:

$$
\frac{D(x,y)}{D(\rho,\theta)}=\rho.
$$

Quindi:

$$
dx\,dy=\rho\,d\rho\,d\theta.
$$

## Coordinate cilindriche

$$
x=\rho\cos\varphi,\qquad y=\rho\sin\varphi,\qquad z=z.
$$

Jacobiano:

$$
\frac{D(x,y,z)}{D(\rho,\varphi,z)}=\rho.
$$

Quindi:

$$
dx\,dy\,dz=\rho\,d\rho\,d\varphi\,dz.
$$

## Coordinate sferiche della lezione

La lezione usa $\theta$ come latitudine:

$$
x=r\cos\theta\cos\varphi
$$

$$
y=r\cos\theta\sin\varphi
$$

$$
z=r\sin\theta.
$$

Jacobiano:

$$
\frac{D(x,y,z)}{D(r,\varphi,\theta)}
=
r^2\cos\theta.
$$

Quindi:

$$
dx\,dy\,dz=r^2\cos\theta\,dr\,d\varphi\,d\theta.
$$

## Volume della sfera

Per $x^2+y^2+z^2\leq R^2$:

$$
0\leq r\leq R,\qquad
0\leq\varphi\leq2\pi,\qquad
-\frac{\pi}{2}\leq\theta\leq\frac{\pi}{2}.
$$

Quindi:

$$
V=
\int_{-\pi/2}^{\pi/2}d\theta
\int_0^{2\pi}d\varphi
\int_0^Rr^2\cos\theta\,dr
=
\frac{4}{3}\pi R^3.
$$

## Attenzione

Non confondere questa convenzione con quella standard di molti libri, dove $\theta$ indica l'angolo polare rispetto all'asse $z$.

Nell'ultima parte della lezione compare una notazione con $r^2\sin\theta$: va controllata visivamente perche' sembra cambiare convenzione angolare.
