# Teorema: Green

## Stato

- Fonte: `01_sources/official_slides/9_lezione_campi_vettoriali_conservativi.pdf`
- Pagina/slide: 17-36
- Affidabilita': alta
- Dimostrazione richiesta: si', tramite identita' separate su $P_y$ e $Q_x$
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per trasformare una circuitazione lungo una curva chiusa in un integrale doppio sul dominio racchiuso.

## Enunciato

Se $F=(P,Q)$ e $C=\partial\sigma$ e' orientata positivamente:

$$
\oint_C P\,dx+Q\,dy
=
\iint_\sigma(Q_x-P_y)\,dx\,dy.
$$

## Ipotesi

- Dominio piano semplice $\sigma$.
- Frontiera $C$ differenziabile a tratti.
- $P,Q,Q_x,P_y$ continue su $\overline{\sigma}$.
- Orientazione positiva: dominio a sinistra.

## Tesi

$$
\oint_C F\cdot\tau\,d\ell
=
\iint_\sigma(Q_x-P_y)\,dx\,dy
$$

## Significato intuitivo

La circuitazione lungo il bordo misura l'accumulo del rotore scalare $Q_x-P_y$ dentro il dominio.

## Significato geometrico

Collega il bordo di una regione piana con la regione interna.

## Dimostrazione

Vedi [[formula_green]].

## Punti delicati

- Orientazione.
- Dominio e bordo.
- Regolarita'.
- Buchi: bordo esterno antiorario, bordi interni orari.

## Esempio standard

Verifica sul quadrato ruotato della lezione: entrambi i membri valgono $4$.

## Domande del professore

- Quali sono le ipotesi?
- Che ruolo ha l'orientazione?
- Come collega bordo e dominio?

## Collegamenti

- [[stokes]]
- [[integrali_linea_II_specie]]
- [[formula_green]]
