# Campi solenoidali e potenziale vettore

## Campi solenoidali

Un campo vettoriale $F$ si dice solenoidale se:

$$
\operatorname{div}F=0
$$

In termini fisici, un campo solenoidale non ha sorgenti o pozzi interni. Nel caso di un fluido incomprimibile, la portata attraverso le sezioni di un tubo di flusso resta costante.

## Rotore e divergenza

Se $F$ e' il rotore di un campo vettoriale $A$, cioe':

$$
F=\operatorname{rot}A
$$

allora:

$$
\operatorname{div}F=\operatorname{div}(\operatorname{rot}A)=0
$$

La dimostrazione e' un calcolo in coordinate cartesiane e usa l'uguaglianza delle derivate miste.

## Potenziale vettore

Un campo $A$ tale che:

$$
F=\operatorname{rot}A
$$

si chiama potenziale vettore di $F$.

Il viceversa richiede ipotesi sul dominio: in domini semplicemente connessi, la condizione $\operatorname{div}F=0$ e' anche sufficiente per l'esistenza di un potenziale vettore.

## Tubi di flusso

Se $F$ e' solenoidale e si considera una superficie chiusa formata da due sezioni trasversali $S_1,S_2$ e da una superficie laterale costituita da linee di campo, il flusso laterale e' nullo. Per Gauss:

$$
\iint_{\partial\Omega}F\cdot n\,dS=0
$$

quindi il flusso attraverso $S_1$ e quello attraverso $S_2$ coincidono in modulo, con segni opposti rispetto alla normale uscente.

## Collegamenti

- [[rotore_divergenza]]
- [[formula_gauss_ostrogradski]]
- [[flusso_integrali_superficie_II_specie]]
