# Discorso orale: differenziabilita' e piano tangente

## Versione breve

Una funzione di piu' variabili e' differenziabile in un punto se vicino a quel punto puo' essere approssimata da una funzione affine, con un errore infinitesimo di ordine superiore rispetto alla distanza dal punto.

Formalmente, $f$ e' differenziabile in $\bar{x}$ se:

$$
f(x)=f(\bar{x})+\sum_{k=1}^n m_k(x_k-\bar{x}_k)+o(\rho)
$$

con:

$$
\lim_{\rho\to 0}\frac{o(\rho)}{\rho}=0.
$$

In questo caso la funzione e' continua e possiede derivate parziali del primo ordine, con $m_i=f_{x_i}(\bar{x})$.

Nel caso di due variabili, l'approssimazione lineare definisce il piano tangente:

$$
z-f(P)=f_x(P)(x-\bar{x})+f_y(P)(y-\bar{y}).
$$

## Dimostrazione da sapere

Differenziabilita' implica esistenza delle derivate parziali: si parte dalla formula di differenziabilita' e si lascia variare una sola coordinata alla volta. In questo modo il rapporto incrementale lungo quell'asse tende al coefficiente $m_i$.

## Follow-up

- Differenziabilita' implica continuita'?
- Esistenza delle derivate parziali implica differenziabilita'?
- Qual e' il significato geometrico del piano tangente?

