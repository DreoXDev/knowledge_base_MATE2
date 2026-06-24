# Esercizi ufficiali - Formula di Green

## Pattern generale

Per:

$$
F=(P,Q)
$$

Green dice:

$$
\oint_C P\,dx+Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy
$$

con orientazione positiva della frontiera.

## 14 luglio 2022 - Esercizio 4

### Traccia

$$
F=(x+y)^2e_1-(x^2+y^2)e_2
$$

sul triangolo di vertici:

$$
(0,0),\qquad (1,0),\qquad (0,1)
$$

### Risultato

$$
-1
$$

## 22 novembre 2022 - Esercizio 4

### Traccia

$$
F=(x-y)e_1+(x+y)e_2
$$

sul quadrato di vertici:

$$
(0,1),\quad (1,0),\quad (0,-1),\quad (-1,0)
$$

### Soluzione rapida

$$
Q_x-P_y=1-(-1)=2
$$

L'area del quadrato e' $2$, quindi:

$$
\oint_C F\cdot\tau\,d\ell=4
$$

con orientazione positiva.

## Errori da evitare

- Sbagliare l'orientazione.
- Confondere $P_y-Q_x$ con $Q_x-P_y$.
- Non usare l'area quando l'integranda e' costante.

## 22 febbraio 2023 - Circonferenza di raggio $R$

### Traccia

$$
F=(x^2y,-xy^2)
$$

su circonferenza di raggio $R$.

### Calcolo

$$
Q_x-P_y=-(x^2+y^2)
$$

Sul disco:

$$
\iint_D-(x^2+y^2)\,dx\,dy
=
-\frac{\pi R^4}{2}
$$

## 24/27 settembre 2022 - Triangolo

### Traccia

$$
F=(x-y,x-y)
$$

sul triangolo di vertici $(0,2)$, $(1,0)$, $(2,0)$.

### Risultato

$$
Q_x-P_y=2
$$

e l'area e' $2$, quindi il risultato e' $4$.

## 19 luglio 2023 - Quarto di ellisse

### Traccia

$$
F=(2xy^2,2x^2y)
$$

su un quarto di ellisse nel primo quadrante.

### Risultato

$$
Q_x-P_y=4xy-4xy=0
$$

quindi la circuitazione e' $0$.
