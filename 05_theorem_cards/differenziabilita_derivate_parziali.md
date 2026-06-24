# Teorema: differenziabilita' implica derivate parziali

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 13-14
- Affidabilita': alta
- Dimostrazione richiesta: si
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per mostrare che la differenziabilita' e' piu' forte della semplice esistenza delle derivate parziali.

## Enunciato

Se $f$ e' differenziabile in:

$$
\bar{x}=(\bar{x}_1,\dots,\bar{x}_n),
$$

allora possiede le derivate parziali del primo ordine in quel punto e:

$$
m_i=f_{x_i}(\bar{x}).
$$

## Ipotesi

- $f$ e' differenziabile in $\bar{x}$.
- L'espansione differenziabile ha coefficienti $m_1,\dots,m_n$.

## Tesi

$$
f_{x_i}(\bar{x})=m_i,\qquad i=1,\dots,n.
$$

## Dimostrazione

Dalla differenziabilita':

$$
\Delta f=
\sum_{i=1}^n m_i\Delta x_i+o(\rho).
$$

Fissiamo una sola variabile, ad esempio $x_1$, ponendo $\Delta x_i=0$ per $i\neq 1$. Allora $\rho=|\Delta x_1|$ e:

$$
\Delta f=m_1\Delta x_1+o(\Delta x_1).
$$

Dividendo per $\Delta x_1$:

$$
\frac{\Delta f}{\Delta x_1}
=
m_1+\frac{o(\Delta x_1)}{\Delta x_1}.
$$

Passando al limite per $\Delta x_1\to 0$:

$$
\lim_{\Delta x_1\to 0}\frac{\Delta f}{\Delta x_1}=m_1.
$$

Quindi:

$$
f_{x_1}(\bar{x})=m_1.
$$

Lo stesso argomento vale per ogni variabile.

## Punti delicati

- Si varia una sola coordinata alla volta.
- Il termine $o(\rho)$ diventa $o(\Delta x_i)$ lungo l'asse coordinato scelto.

## Collegamenti

- [[differenziabilita]]
- [[derivate_parziali]]

