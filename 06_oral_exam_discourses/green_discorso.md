# Discorso orale: Green

## Obiettivo

Preparare una risposta da esame orale su questo argomento.

## Durata target

- Risposta breve: 1 minuto.
- Risposta completa: 3-5 minuti.
- Con dimostrazione: 5-8 minuti.

## Versione breve

La formula di Green collega la circuitazione lungo il bordo di un dominio piano con un integrale doppio sul dominio.

Se $F=(P,Q)$ e $C=\partial\sigma$ e' orientata positivamente:

$$
\oint_C P\,dx+Q\,dy
=
\iint_\sigma(Q_x-P_y)\,dx\,dy.
$$

Per orientazione positiva si intende che, percorrendo il bordo, il dominio resta a sinistra.

## Versione completa

Le ipotesi sono: dominio piano semplice, frontiera differenziabile a tratti, derivate $Q_x$ e $P_y$ continue su $\overline{\sigma}$.

La dimostrazione si ottiene provando separatamente:

$$
\iint_\sigma P_y\,dx\,dy=-\int_C P\,dx
$$

e:

$$
\iint_\sigma Q_x\,dx\,dy=\int_C Q\,dy.
$$

Sommando le due formule si ottiene Green.

Per domini divisi in sottoregioni, i lati interni si cancellano perche' percorsi in versi opposti.

## Dimostrazione parlata

Vedi [[formula_green_discorso]].

## Frasi utili

- "L'idea geometrica e' che..."
- "Le ipotesi servono a garantire che..."
- "Questo teorema mette in relazione..."
- "Un caso particolare importante e'..."

## Follow-up probabili

- Qual e' l'orientazione positiva?
- Cosa cambia se il dominio ha buchi?
- Come si collega Green alla conservativita'?

## Errori da evitare

- Usare l'orientazione opposta.
- Dimenticare il segno $Q_x-P_y$.
- Applicare Green senza controllare le ipotesi sul dominio e sulla regolarita'.
