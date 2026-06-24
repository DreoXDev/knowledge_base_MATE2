# Formula di Green

## Stato

- Fonte: `01_sources/official_slides/9_lezione_campi_vettoriali_conservativi.pdf`
- Slide: 17-36
- Affidabilita': alta, con note su possibili refusi nelle slide 24 e 35

## Idea

La formula di Green mette in relazione la circuitazione lungo una curva chiusa con un integrale doppio sul dominio piano racchiuso dalla curva.

## Enunciato

Sia $\sigma$ un dominio piano semplice con frontiera:

$$
C=\partial\sigma
$$

differenziabile a tratti.

Sia $F=(P,Q)$ con $P,Q$ continue e con $Q_x$ e $P_y$ continue in $\overline{\sigma}$.

Orientiamo $C$ in modo che il dominio resti sempre a sinistra. Allora:

$$
\oint_C P\,dx+Q\,dy
=
\iint_\sigma
(Q_x-P_y)\,dx\,dy.
$$

Equivalentemente:

$$
\oint_C F\cdot\tau\,d\ell
=
\iint_\sigma
\left(
\frac{\partial F_2}{\partial x}
-
\frac{\partial F_1}{\partial y}
\right)
dx\,dy.
$$

## Orientazione positiva

La frontiera e' orientata positivamente se, percorrendola, il dominio rimane a sinistra.

Per domini con buchi:

- la frontiera esterna si percorre in senso antiorario;
- le frontiere interne si percorrono in senso orario.

## Dimostrazione

Si dimostrano separatamente:

$$
\iint_\sigma P_y\,dx\,dy
=
-\int_C P\,dx
$$

e:

$$
\iint_\sigma Q_x\,dx\,dy
=
\int_C Q\,dy.
$$

Sommando si ottiene Green.

Per regioni semplici generali, si suddivide il dominio in sottoregioni; i contributi interni si annullano a coppie perche' sono percorsi in versi opposti.

## Conseguenza

In un dominio semplicemente connesso, per campi piani di classe $C^1$:

$$
Q_x=P_y
$$

e' equivalente alla conservativita'.

## Note di attenzione

- Slide 24: nella riga dell'integrale di bordo dovrebbe comparire $dy$, non $dx$.
- Slide 35: in un esercizio piano compare un termine $F_3 dz/dt$, probabile residuo di template.
- Slide 29: l'ordine delle parametrizzazioni del quadrato va letto dalle formule dei lati.

## Collegamenti

- [[green]]
- [[irrotazionalita_forme_chiuse_esatte]]
- [[campi_conservativi]]
