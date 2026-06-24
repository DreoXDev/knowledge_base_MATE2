# Integrali di linea di I specie

## Stato

- Fonte: `01_sources/official_slides/7_lezione_integrali_linea_I_specie.pdf`
- Slide: 1-20
- Affidabilita': alta

## Idea intuitiva

L'integrale di linea di I specie generalizza l'integrale di una funzione lungo un intervallo al caso in cui il dominio di integrazione sia una curva.

Si sommano i valori della funzione lungo la curva pesati per piccoli elementi di lunghezza $d\ell$.

## Definizione tramite somme

Sia $C$ una curva regolare in $\mathbb{R}^n$ e sia:

$$
f:\mathbb{R}^n\to\mathbb{R}.
$$

Si suddivide $C$ in archi di lunghezza $\Delta\ell_i$ e si sceglie un punto $P_i$ su ogni arco.

Se il limite:

$$
\lim_{\Delta\ell\to 0}
\sum_i f(P_i)\Delta\ell_i
$$

esiste e non dipende dalla suddivisione ne' dalla scelta dei punti $P_i$, allora si chiama integrale di linea di I specie di $f$ lungo $C$ e si indica con:

$$
\int_C f\,d\ell.
$$

## Ascissa curvilinea

Fissato $P_0=x(t_0)$, l'ascissa curvilinea e':

$$
\ell(t)
=
\int_{t_0}^{t}
\left\|
\frac{dr}{dt}
\right\|
dt
$$

cioe':

$$
\ell(t)
=
\int_{t_0}^{t}
\sqrt{
\left(\frac{dx_1}{dt}\right)^2+\cdots+
\left(\frac{dx_n}{dt}\right)^2
}
\,dt.
$$

## Formula con ascissa curvilinea

Se la curva e' parametrizzata con l'ascissa curvilinea:

$$
x_i=x_i(\ell),
$$

allora:

$$
\int_C f\,d\ell
=
\int_{\ell_1}^{\ell_2}
f(x_1(\ell),\dots,x_n(\ell))\,d\ell.
$$

## Formula con parametrizzazione arbitraria

Se:

$$
r(t)=(x_1(t),\dots,x_n(t)),\qquad t\in[t_1,t_2],
$$

allora:

$$
\int_C f\,d\ell
=
\int_{t_1}^{t_2}
f(x_1(t),\dots,x_n(t))
\left\|
r'(t)
\right\|
\,dt
$$

cioe':

$$
\int_C f\,d\ell
=
\int_{t_1}^{t_2}
f(x_1(t),\dots,x_n(t))
\sqrt{
\left(\frac{dx_1}{dt}\right)^2+\cdots+
\left(\frac{dx_n}{dt}\right)^2
}
\,dt.
$$

## Interpretazione geometrica

Se $f\geq 0$, l'integrale puo' essere interpretato come l'area della superficie verticale costruita sopra la curva $C$ con altezza $f$.

## Caso particolare

Se $f=1$:

$$
\int_C 1\,d\ell
$$

e' la lunghezza della curva.

## Procedura operativa

1. Parametrizzare la curva $C$.
2. Determinare l'intervallo del parametro.
3. Calcolare $r'(t)$.
4. Calcolare $\|r'(t)\|$.
5. Restringere $f$ alla curva, cioe' calcolare $f(r(t))$.
6. Integrare:

$$
\int_{t_1}^{t_2}f(r(t))\|r'(t)\|\,dt.
$$

## Collegamenti

- [[lunghezza_arco_curva]]
- [[ascissa_curvilinea]]
- [[baricentro_filo]]
- [[integrale_linea_prima_specie]]
