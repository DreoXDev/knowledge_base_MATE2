# Calcolo del potenziale

## Stato

- Fonte: `01_sources/official_slides/9_lezione_campi_vettoriali_conservativi.pdf`
- Slide: 37-49
- Affidabilita': alta

## Metodo per integrazione progressiva

Dato $F=(F_1,\dots,F_n)$, si cerca $U$ tale che:

$$
U_{x_i}=F_i.
$$

Si integra una componente alla volta, introducendo funzioni arbitrarie delle variabili non ancora integrate e determinandole con le altre equazioni.

## Esempio 1

Per:

$$
F=(2xy^2z^2,\ 2yx^2z^2,\ 2zx^2y^2)
$$

un potenziale e':

$$
U=x^2y^2z^2.
$$

Si puo' anche integrare lungo il segmento:

$$
x(t)=xt,\qquad y(t)=yt,\qquad z(t)=zt,\qquad t\in[0,1].
$$

## Esempio 2

Per:

$$
F=
\left(
\frac{2x}{x^2+y^2+z^2},
\frac{2y}{x^2+y^2+z^2},
\frac{2z}{x^2+y^2+z^2}
\right),
$$

su $\mathbb{R}^3\setminus\{0\}$ un potenziale e':

$$
U=\ln(x^2+y^2+z^2).
$$

Nota: $\mathbb{R}^3\setminus\{0\}$ e' semplicemente connesso, a differenza di $\mathbb{R}^2\setminus\{0\}$.

## Esempio con parametro

Per il campo:

$$
\left(
\lambda x+2xy^2z^3,\ 
\lambda y+2x^2yz^3,\ 
\lambda z+3x^2y^2z^2
\right),
$$

un potenziale e':

$$
U=x^2y^2z^3+\frac{1}{2}\lambda(x^2+y^2+z^2).
$$

Dagli estremi della curva della lezione si ottiene:

$$
U(1,1,2)-U(0,0,0)=8+3\lambda.
$$

La condizione di integrale nullo impone:

$$
\lambda=-\frac{8}{3}.
$$

## Esempio sull'elica

Per:

$$
r(t)=\left(\cos t,\sin t,\frac{t}{\pi}\right),\qquad t\in[0,\pi],
$$

e campo con potenziale:

$$
U=x^3y-y^2x+zx,
$$

l'integrale tra $P_0=(1,0,0)$ e $P_1=(-1,0,1)$ vale:

$$
U(P_1)-U(P_0)=-1.
$$

## Collegamenti

- [[campi_conservativi]]
- [[campi_conservativi_green]]
