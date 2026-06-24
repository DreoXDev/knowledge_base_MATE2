# Superfici orientabili

## Definizione

Una superficie $S$ si dice orientabile se su $S$ e' possibile scegliere in modo continuo un campo di versori normali.

Una superficie orientabile su cui e' stata fissata una delle due normali possibili si dice superficie orientata.

In formule, scegliere un'orientazione significa fissare un campo:

$$
n:S\to\mathbb{R}^3
$$

tale che $n(P)$ sia normale a $S$ in ogni punto regolare $P$, $\|n(P)\|=1$ e la scelta vari con continuita'.

## Significato geometrico

Orientare una superficie vuol dire distinguere localmente un lato positivo e un lato negativo. Questa scelta e' indispensabile quando si calcola un flusso:

$$
\iint_S F\cdot n\,dS
$$

perche' cambiando verso alla normale cambia il segno dell'integrale.

## Esempio non orientabile

Il nastro di Mobius e' l'esempio classico di superficie non orientabile: percorrendo un giro completo si torna al punto di partenza con la normale invertita, quindi non esiste una scelta globale continua della normale.

## Collegamenti

- [[flusso_integrali_superficie_II_specie]]
- [[superfici_parametrizzate]]
- [[piano_tangente_superfici]]
