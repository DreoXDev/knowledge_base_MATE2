# Intorni, limiti e continuita' in $\mathbb{R}^n$

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 4-5
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Intorni

Per $x^*\in\mathbb{R}^n$:

$$
B_a(x^*)=
\{x\in\mathbb{R}^n:\|x-x^*\|<a\}
$$

e' l'intorno di centro $x^*$ e raggio $a$.

In $\mathbb{R}^2$ e' l'interno di una circonferenza di raggio $a$ centrata in $x^*$. In $\mathbb{R}^3$ e' l'interno di una sfera di raggio $a$ centrata in $x^*$.

## Limite

Si dice che:

$$
\lim_{x\to x_0}f(x)=l
$$

se per ogni $\varepsilon>0$ esiste $\delta>0$ tale che:

$$
|f(x)-l|<\varepsilon
$$

per tutti i punti $x\in B_\delta(x_0)$ eccetto al piu' $x_0$.

## Continuita'

$f$ e' continua in $x_0$ se:

$$
\lim_{x\to x_0} f(x)=f(x_0).
$$

## Intuizione orale

Nei limiti di piu' variabili, $x$ puo' avvicinarsi a $x_0$ lungo infinite direzioni e traiettorie. Questo rende il concetto piu' delicato rispetto al caso reale monodimensionale.

## Collegamenti

- [[funzioni_di_piu_variabili]]
- [[differenziabilita]]

