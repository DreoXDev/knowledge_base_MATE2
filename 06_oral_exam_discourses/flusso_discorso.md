# Discorso orale: flusso

## Versione breve

Il flusso di un campo vettoriale $F$ attraverso una superficie orientata $S$ e':

$$
\iint_SF\cdot n\,dS
$$

dove $n$ e' il versore normale scelto. A differenza dell'integrale di superficie di I specie, il flusso dipende dall'orientazione: cambiando $n$ in $-n$ il valore cambia segno.

Se $S$ e' parametrizzata da $r(u,v)$, allora:

$$
n\,dS=\pm(r_u\times r_v)\,du\,dv
$$

e quindi:

$$
\iint_SF\cdot n\,dS
=
\pm\iint_DF(r(u,v))\cdot(r_u\times r_v)\,du\,dv
$$

Il segno va scelto controllando se $r_u\times r_v$ e' concorde con la normale richiesta.

## Interpretazione

Fisicamente, se $F$ e' un campo di velocita', il flusso misura quanta materia attraversa la superficie nella direzione della normale scelta.

## Follow-up

- Perche' il flusso dipende dall'orientazione?
- Come si calcola il flusso tramite parametrizzazione?
- Qual e' la differenza tra I e II specie?
- Che cosa succede se la superficie e' chiusa?
