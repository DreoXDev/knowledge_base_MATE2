# Teorema: campi conservativi e indipendenza dal cammino

## Stato

- Fonte: `01_sources/official_slides/8_lezione_integrali_linea_II_specie.pdf`
- Slide: 20-22
- Affidabilita': alta

## Enunciato

Sia $F$ un campo vettoriale conservativo e continuo in un dominio $D$, e sia $C$ una curva regolare orientata contenuta in $D$.

Allora:

$$
\int_C F\cdot \tau\,d\ell
=
U(P_1)-U(P_0)
$$

dove $U$ e' un potenziale di $F$ e $P_0,P_1$ sono gli estremi della curva.

## Conseguenza

L'integrale dipende solo dagli estremi e non dal cammino scelto.

## Dimostrazione

Usare una parametrizzazione concorde $r(t)$.

Poiche':

$$
F=\nabla U
$$

si ha:

$$
F(r(t))\cdot r'(t)
=
\nabla U(r(t))\cdot r'(t)
=
\frac{d}{dt}U(r(t)).
$$

Quindi:

$$
\int_C F\cdot \tau\,d\ell
=
\int_{t_0}^{t_1}\frac{d}{dt}U(r(t))\,dt
=
U(P_1)-U(P_0).
$$

## Domande orali

- Qual e' il ruolo del potenziale?
- Perche' si usa la regola della funzione composta?
- Cosa significa indipendenza dal cammino?

## Collegamenti

- [[campi_conservativi]]
- [[integrali_linea_II_specie]]
