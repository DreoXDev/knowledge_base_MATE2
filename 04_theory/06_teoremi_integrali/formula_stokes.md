# Formula di Stokes

## Enunciato

Sia $S$ una superficie orientata con bordo $C=\partial S$. Sia $F$ un campo vettoriale le cui componenti sono continue con le derivate parziali su $S$ e sulla frontiera.

Allora:

$$
\oint_C F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

dove $n$ e' la normale scelta sulla superficie e $\tau$ e' il versore tangente al bordo.

## Orientazione compatibile

Il verso di percorrenza di $C$ deve essere compatibile con $n$: un osservatore orientato secondo $n$, muovendosi lungo $C$, deve avere la superficie $S$ alla propria sinistra.

## Significato

Stokes collega:

- la circuitazione del campo lungo il bordo della superficie;
- il flusso del rotore attraverso la superficie.

In questo senso il rotore misura la circuitazione infinitesima, e la formula dice che l'effetto globale lungo il bordo e' la somma degli effetti locali sulla superficie.

## Green come caso particolare

La formula di Green e' il caso piano della formula di Stokes. Se $S$ e' un dominio piano nel piano $xy$ e:

$$
F=(P,Q,0)
$$

allora:

$$
\operatorname{rot}(F)\cdot e_3=Q_x-P_y
$$

e Stokes diventa:

$$
\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy
$$

## Esempio ufficiale

Per:

$$
F=(xz,xy,3xz)
$$

sulla porzione del piano $2x+y+z=2$ nel primo ottante, orientata verso l'alto, si ottiene:

$$
\iint_S\operatorname{rot}(F)\cdot n\,dS=-1
$$

e lo stesso valore si ottiene sommando gli integrali di linea sui tre lati del triangolo.

## Collegamenti

- [[rotore_divergenza]]
- [[formula_green]]
- [[green_stokes_gauss_collegamenti]]
