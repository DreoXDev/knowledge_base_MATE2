# Differenziabilita'

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 11-15
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Definizione

$f$ e' differenziabile in:

$$
\bar{x}=(\bar{x}_1,\dots,\bar{x}_n)
$$

se esistono costanti $m_1,\dots,m_n$ tali che:

$$
f(x_1,\dots,x_n)
=
f(\bar{x}_1,\dots,\bar{x}_n)
+
\sum_{k=1}^n m_k(x_k-\bar{x}_k)
+
o(\rho)
$$

dove:

$$
\rho=
\sqrt{
(x_1-\bar{x}_1)^2+\cdots+(x_n-\bar{x}_n)^2
}
$$

e:

$$
\lim_{\rho\to 0}\frac{o(\rho)}{\rho}=0.
$$

## Significato intuitivo

La funzione e' differenziabile quando vicino al punto puo' essere approssimata bene da una funzione affine.

## Corollario

La differenziabilita' implica la continuita'.

## Teorema: differenziabilita' implica esistenza delle derivate parziali

Se $f$ e' differenziabile in $\bar{x}$, allora possiede le derivate parziali del primo ordine in quel punto e:

$$
m_i=f_{x_i}(\bar{x}).
$$

## Dimostrazione del teorema

Dalla differenziabilita':

$$
\Delta f=
\sum_{i=1}^n m_i\Delta x_i+o(\rho).
$$

Scegliendo $\Delta x_i=0$ per tutti gli indici tranne uno, ad esempio per $i=1$, si ottiene:

$$
\Delta f=m_1\Delta x_1+o(\Delta x_1).
$$

Quindi:

$$
\frac{\Delta f}{\Delta x_1}
=
m_1+\frac{o(\Delta x_1)}{\Delta x_1}.
$$

Passando al limite:

$$
\lim_{\Delta x_1\to 0}\frac{\Delta f}{\Delta x_1}=m_1,
$$

percio':

$$
f_{x_1}(\bar{x})=m_1.
$$

Il ragionamento e' analogo per le altre variabili.

## Teorema: derivate parziali continue implicano differenziabilita'

Se $f$ possiede derivate parziali del primo ordine in un intorno di $P$ e queste sono continue in $P$, allora $f$ e' differenziabile.

La slide rimanda alle note del corso per la dimostrazione.

## Attenzione

Il converso "esistono derivate parziali quindi la funzione e' differenziabile" non e' garantito in generale.

## Collegamenti

- [[derivate_parziali]]
- [[piano_tangente]]
- [[differenziabilita_derivate_parziali]]
- [[differenziabilita_derivate_continue]]

