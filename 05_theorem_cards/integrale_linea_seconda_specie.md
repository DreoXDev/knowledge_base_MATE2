# Definizione: integrale di linea di II specie

## Stato

- Fonte: `01_sources/official_slides/8_lezione_integrali_linea_II_specie.pdf`
- Pagina/slide: 11-13
- Affidabilita': alta
- Dimostrazione richiesta: formula operativa tramite parametrizzazione
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per integrare un campo vettoriale lungo una curva orientata, considerando la componente tangenziale del campo.

## Definizione

Sia $C$ una curva orientata e sia $\tau$ il versore tangente concorde con l'orientazione.

L'integrale di linea di II specie di $F$ lungo $C$ e':

$$
\int_C F\cdot \tau\,d\ell.
$$

## Ipotesi

- Curva orientata.
- Campo vettoriale definito lungo la curva.
- Versore tangente concorde con l'orientazione.

## Formula operativa

Se $r(t)$ e' concorde con l'orientazione:

$$
\int_C F\cdot \tau\,d\ell
=
\int_a^b F(r(t))\cdot r'(t)\,dt.
$$

## Forma differenziale

Nel piano, se $F=(P,Q)$:

$$
\int_C F\cdot \tau\,d\ell
=
\int_C P\,dx+Q\,dy.
$$

## Significato intuitivo

Misura quanto il campo spinge nella direzione del moto lungo la curva.

## Significato fisico

Rappresenta il lavoro di un campo di forze lungo un cammino.

## Punti delicati

- Orientazione.
- Campo vettoriale.
- Parametrizzazione.
- Se si inverte orientazione, il segno cambia.

## Esempio standard

$$
\int_C 3x^2y\,dx+(x^3+1)\,dy
$$

da $(0,0)$ a $(1,1)$ vale $2$ sui tre cammini della lezione perche' il campo e' conservativo.

## Domande del professore

- Che cosa misura?
- Che ruolo ha l'orientazione?
- Che differenza c'e' con un integrale di I specie?

## Collegamenti

- [[integrali_linea_II_specie]]
- [[forme_differenziali]]
- [[campi conservativi]]
