# Teorema: indipendenza dal cammino implica conservativita'

## Stato

- Fonte: `01_sources/official_slides/9_lezione_campi_vettoriali_conservativi.pdf`
- Slide: 1-7
- Affidabilita': alta

## Enunciato

Se $F=(F_1,F_2)$ e' continuo in un dominio aperto e connesso per archi $D$ e l'integrale:

$$
\int_C F_1\,dx+F_2\,dy
$$

non dipende dal cammino, allora $F$ e' conservativo.

## Idea della dimostrazione

Si fissa $P_0$ e si definisce:

$$
U(P)=\int_{P_0}^{P}F_1\,dx+F_2\,dy.
$$

L'indipendenza dal cammino rende $U$ ben definita. Poi si mostra che $U_x=F_1$ e $U_y=F_2$ usando piccoli segmenti contenuti nel dominio.

## Collegamenti

- [[indipendenza_cammino]]
- [[campi_conservativi]]
