# Discorso orale: Campi conservativi

## Versione breve

Un campo vettoriale $F$ si dice conservativo se esiste una funzione scalare $U$, detta potenziale, tale che:

$$
F=\nabla U.
$$

Per un campo conservativo, l'integrale di linea di II specie lungo una curva orientata dipende solo dagli estremi della curva.

Infatti, se $C$ va da $P_0$ a $P_1$, allora:

$$
\int_C F\cdot \tau\,d\ell
=
U(P_1)-U(P_0).
$$

La dimostrazione si ottiene parametrizzando il cammino con $r(t)$ e usando la regola della funzione composta:

$$
F(r(t))\cdot r'(t)
=
\nabla U(r(t))\cdot r'(t)
=
\frac{d}{dt}U(r(t)).
$$

Integrando, si ottiene la differenza dei valori del potenziale agli estremi.

## Dimostrazione parlata

Vedi il passaggio con la regola della funzione composta nella versione breve.

## Frasi utili

- "L'idea geometrica e' che..."
- "Le ipotesi servono a garantire che..."
- "Questo teorema mette in relazione..."
- "Un caso particolare importante e'..."

## Follow-up probabili

- Che cos'e' un potenziale?
- Perche' il campo conservativo da' indipendenza dal cammino?
- Come si usa il potenziale per calcolare un integrale?
- Perche' l'esempio delle slide vale $2$ per tre cammini diversi?

## Errori da evitare

- Dimenticare l'orientazione della curva.
- Usare il teorema senza avere un potenziale.
- Confondere definizione di campo conservativo con criteri successivi sul rotore.
