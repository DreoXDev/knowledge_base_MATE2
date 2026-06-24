# Definizione: integrale di linea di I specie

## Stato

- Fonte: `01_sources/official_slides/7_lezione_integrali_linea_I_specie.pdf`
- Pagina/slide: 2-8
- Affidabilita': alta
- Dimostrazione richiesta: formula operativa tramite cambio parametro
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per integrare una funzione scalare lungo una curva.

## Definizione

Sia $C$ una curva regolare in $\mathbb{R}^n$ e sia $f:\mathbb{R}^n\to\mathbb{R}$.

L'integrale di linea di I specie e' il limite, se esiste, delle somme:

$$
\sum_i f(P_i)\Delta\ell_i
$$

e si indica con:

$$
\int_C f\,d\ell.
$$

## Ipotesi

- $C$ curva regolare.
- $f$ funzione scalare definita lungo la curva.
- Esistenza del limite delle somme integrali.

## Formula operativa

Se $C$ e' parametrizzata da:

$$
r(t)=(x_1(t),\dots,x_n(t)),\qquad t\in[t_1,t_2],
$$

allora:

$$
\int_C f\,d\ell
=
\int_{t_1}^{t_2}
f(r(t))\|r'(t)\|\,dt.
$$

## Significato intuitivo

Somma i valori della funzione lungo la curva pesandoli con piccoli elementi di lunghezza.

## Significato geometrico

Se $f\geq 0$, misura l'area della superficie costruita sopra la curva con altezza $f$.

## Caso particolare

$$
\int_C 1\,d\ell
$$

e' la lunghezza della curva.

## Punti delicati

- Non dimenticare il fattore $\|r'(t)\|$.
- Prima si restringe $f$ alla curva, poi si integra.
- $d\ell=\|r'(t)\|dt$.

## Esempio standard

Semicirconferenza $x^2+y^2=16$, $x\geq 0$, parametrizzata da $x=4\cos t$, $y=4\sin t$.

## Domande del professore

- Che cosa misura?
- Dipende dall'orientazione della curva?
- Perche' compare $\|r'(t)\|$?

## Collegamenti

- [[integrali_linea_I_specie]]
- [[ascissa_curvilinea]]
- [[lunghezza_arco_curva]]
