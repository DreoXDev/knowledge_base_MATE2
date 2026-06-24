# Discorso orale: formula di Stokes

## Versione breve

La formula di Stokes mette in relazione la circuitazione di un campo vettoriale lungo il bordo di una superficie con il flusso del rotore attraverso la superficie.

Se $S$ e' una superficie orientata con bordo $C=\partial S$, allora:

$$
\oint_CF\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

Il verso di percorrenza di $C$ deve essere compatibile con la normale $n$: un osservatore orientato secondo $n$, muovendosi lungo $C$, deve avere la superficie a sinistra.

L'idea e' che il rotore misura la tendenza locale del campo a ruotare, mentre la circuitazione misura l'effetto complessivo lungo il bordo.

## Versione completa

Per enunciare Stokes servono una superficie orientata $S$, il suo bordo $C=\partial S$ e un campo regolare. La scelta della normale su $S$ induce il verso positivo sul bordo. Con questa convenzione:

$$
\oint_CF\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

Quindi Stokes e' una generalizzazione della formula di Green: nel piano il rotore ha solo componente verticale e si ottiene:

$$
\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy
$$

## Esempi da citare

- Piano $2x+y+z=2$ nel primo ottante, campo $F=(xz,xy,3xz)$: risultato $-1$.
- Emisfero superiore della sfera di raggio $3$, campo $F=(y,-x,0)$: risultato $-18\pi$.

## Follow-up

- Come si sceglie l'orientazione del bordo?
- Che cos'e' il rotore?
- In che senso Green e' un caso particolare di Stokes?
- Come si verifica Stokes su un piano o su un emisfero?
