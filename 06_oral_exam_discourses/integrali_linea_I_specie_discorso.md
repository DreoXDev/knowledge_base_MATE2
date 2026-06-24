# Discorso orale: integrali di linea di I specie

## Versione breve

L'integrale di linea di I specie serve a integrare una funzione scalare lungo una curva.

L'idea e' suddividere la curva in piccoli archi di lunghezza $\Delta\ell_i$, scegliere un punto $P_i$ su ciascun arco e considerare le somme:

$$
\sum_i f(P_i)\Delta\ell_i.
$$

Se il limite esiste e non dipende dalla suddivisione, si ottiene:

$$
\int_C f\,d\ell.
$$

Se la curva e' parametrizzata da $r(t)$, con $t\in[t_1,t_2]$, allora:

$$
\int_C f\,d\ell
=
\int_{t_1}^{t_2}f(r(t))\|r'(t)\|\,dt.
$$

Quindi operativamente si restringe la funzione alla curva e si moltiplica per l'elemento di lunghezza $d\ell=\|r'(t)\|dt$.

Il caso $f=1$ restituisce la lunghezza della curva.

## Follow-up

- Che differenza c'e' tra integrale su intervallo e integrale su curva?
- Che cos'e' $d\ell$?
- Perche' compare $\|r'(t)\|$?
- Qual e' l'interpretazione geometrica?
