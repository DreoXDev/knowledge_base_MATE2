# Discorso orale: formula di Green

## Versione breve

La formula di Green collega l'integrale di linea di II specie lungo una curva chiusa con un integrale doppio sul dominio piano racchiuso dalla curva.

Se $F=(P,Q)$ e $C=\partial\sigma$ e' orientata positivamente, cioe' percorsa lasciando il dominio a sinistra, allora:

$$
\oint_C P\,dx+Q\,dy
=
\iint_\sigma
(Q_x-P_y)\,dx\,dy.
$$

Le ipotesi sono che il dominio sia piano semplice, la frontiera sia differenziabile a tratti e le derivate $Q_x$ e $P_y$ siano continue.

## Dimostrazione parlata

Si dimostra prima per domini descrivibili sia rispetto a $x$ sia rispetto a $y$, provando separatamente:

$$
\iint_\sigma P_y\,dx\,dy=-\int_C P\,dx
$$

e:

$$
\iint_\sigma Q_x\,dx\,dy=\int_C Q\,dy.
$$

Sommando si ottiene Green.

Per domini piu' generali si suddivide la regione in sottoregioni: i contributi interni si cancellano perche' vengono percorsi in versi opposti.

## Follow-up

- Qual e' l'orientazione positiva?
- Cosa succede se il dominio ha buchi?
- Come si collega Green ai campi conservativi?
