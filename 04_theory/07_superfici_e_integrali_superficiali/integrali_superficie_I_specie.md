# Integrali di superficie di I specie

## Definizione

Sia $f(x,y,z)$ una funzione definita su un dominio che contiene una superficie regolare $S$. L'integrale:

$$
\int_S f\,dS
$$

si chiama integrale di superficie di I specie.

## Formula parametrica

Se:

$$
r(u,v)=(x(u,v),y(u,v),z(u,v))
$$

parametrizza $S$ per $(u,v)\in D$, allora:

$$
\int_S f\,dS
=
\iint_D f(r(u,v))\|r_u\times r_v\|\,du\,dv
$$

## Interpretazione

E' l'analogo superficiale dell'integrale di linea di I specie. Si puo' pensare come limite di somme:

$$
\sum_i f(P_i)mS_i
$$

dove $S_i$ sono piccole porzioni della superficie e $P_i\in S_i$.

## Dipendenza dall'orientazione

L'integrale di I specie non dipende dall'orientazione della superficie, perche' nell'elemento $dS$ compare la norma del prodotto vettoriale.

## Collegamenti

- [[area_superficie]]
- [[flusso_integrali_superficie_II_specie]]
- [[integrali_linea_I_specie]]
