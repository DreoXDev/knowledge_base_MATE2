# Flusso e integrali di superficie di II specie

## Definizione

Sia $F$ un campo vettoriale e sia $S$ una superficie orientata con versore normale $n$. L'integrale:

$$
\iint_S F\cdot n\,dS
$$

si chiama flusso di $F$ attraverso $S$, oppure integrale di superficie di II specie.

## Formula parametrica

Se $S$ e' parametrizzata da:

$$
r(u,v)
$$

con $(u,v)\in D$, allora:

$$
n\,dS=\pm(r_u\times r_v)\,du\,dv
$$

Il segno e' positivo se $r_u\times r_v$ ha lo stesso verso della normale scelta, negativo altrimenti. Quindi:

$$
\iint_S F\cdot n\,dS
=
\pm\iint_D F(r(u,v))\cdot(r_u\times r_v)\,du\,dv
$$

## Dipendenza dall'orientazione

A differenza degli integrali di superficie di I specie, il flusso dipende dall'orientazione. Se si cambia $n$ in $-n$, allora:

$$
\iint_S F\cdot(-n)\,dS
=
-\iint_S F\cdot n\,dS
$$

## Interpretazione fisica

Se $F$ e' il campo delle velocita' di un fluido, allora $F\cdot n\,dS$ misura la quantita' infinitesima di fluido che attraversa la superficie nella direzione della normale scelta.

## Esempio: triangolo nel piano $x+y+z=1$

Sia:

$$
F=(x,y,z)
$$

e sia $S$ il triangolo nel piano $x+y+z=1$ tagliato dai piani coordinati, orientato con normale che forma un angolo acuto con $e_3$. Scrivendo:

$$
r(x,y)=(x,y,1-x-y)
$$

sul triangolo:

$$
T=\{(x,y):x\geq0,\ y\geq0,\ x+y\leq1\}
$$

si ottiene:

$$
F(r(x,y))\cdot(r_x\times r_y)=x+y+z=1
$$

percio':

$$
\iint_SF\cdot n\,dS=\iint_T1\,dx\,dy=\frac{1}{2}
$$

## Collegamenti

- [[integrali_superficie_I_specie]]
- [[formula_gauss_ostrogradski]]
- [[formula_stokes]]
