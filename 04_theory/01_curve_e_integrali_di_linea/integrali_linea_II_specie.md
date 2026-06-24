# Integrali di linea di II specie

## Stato

- Fonte: `01_sources/official_slides/8_lezione_integrali_linea_II_specie.pdf`
- Slide: 11-17
- Affidabilita': alta

## Idea intuitiva

L'integrale di linea di II specie misura la componente tangenziale di un campo vettoriale lungo una curva orientata.

In fisica rappresenta il lavoro compiuto da un campo di forze lungo un cammino.

## Definizione

Sia $C$ una curva orientata e sia $\tau$ il versore tangente diretto secondo l'orientazione di $C$.

L'integrale di linea di II specie di un campo vettoriale $F$ lungo $C$ e':

$$
\int_C F\cdot \tau\,d\ell
$$

cioe' l'integrale di I specie della componente tangenziale di $F$ lungo la curva.

## Formula con parametrizzazione

Se:

$$
r(t)=(x_1(t),\dots,x_n(t)),\qquad t\in[a,b]
$$

e' una parametrizzazione concorde con l'orientazione di $C$, allora:

$$
\int_C F\cdot \tau\,d\ell
=
\int_a^b F(r(t))\cdot r'(t)\,dt
$$

cioe':

$$
\int_C F\cdot \tau\,d\ell
=
\int_a^b
\left(
F_1(r(t))\frac{dx_1}{dt}
+
\cdots+
F_n(r(t))\frac{dx_n}{dt}
\right)dt.
$$

Se la parametrizzazione e' discorde, il segno cambia.

## Forma differenziale

L'integrale si scrive anche:

$$
\int_C F_1\,dx_1+\cdots+F_n\,dx_n.
$$

L'espressione:

$$
F_1\,dx_1+\cdots+F_n\,dx_n
$$

e' una forma differenziale, o 1-forma.

Nel piano:

$$
\int_C P\,dx+Q\,dy
$$

dove $F=(P,Q)$.

## Differenza rispetto agli integrali di I specie

Gli integrali di I specie integrano una funzione scalare rispetto alla lunghezza $d\ell$ e non dipendono dall'orientazione.

Gli integrali di II specie integrano la componente tangenziale di un campo vettoriale e dipendono dall'orientazione.

## Procedura operativa

1. Parametrizzare la curva rispettando l'orientazione.
2. Calcolare $r'(t)$.
3. Calcolare $F(r(t))$.
4. Calcolare il prodotto scalare $F(r(t))\cdot r'(t)$.
5. Integrare rispetto al parametro.

## Collegamenti

- [[integrali_linea_I_specie]]
- [[campi_vettoriali]]
- [[campi_conservativi]]
- [[integrale_linea_seconda_specie]]
