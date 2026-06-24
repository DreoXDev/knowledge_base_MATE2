# Scheda: integrale superficiale

## Stato

- Fonte: Lezione 11, slide 11-15.
- Affidabilita': alta.
- Ultimo aggiornamento: 2026-06-24

## Quando si usa

Si usa per integrare una funzione o un campo vettoriale su una superficie.

## Integrale di superficie di I specie

Per una funzione scalare $f$:

$$
\int_S f\,dS
$$

Se $S$ e' parametrizzata da $r(u,v)$:

$$
\int_S f\,dS=
\iint_D f(r(u,v))\|r_u\times r_v\|\,du\,dv
$$

Questo integrale non dipende dall'orientazione.

## Integrale di superficie di II specie / flusso

Per un campo vettoriale $F$ su una superficie orientata:

$$
\iint_SF\cdot n\,dS
$$

Se $S$ e' parametrizzata da $r(u,v)$:

$$
\iint_SF\cdot n\,dS
=
\pm\iint_DF(r(u,v))\cdot(r_u\times r_v)\,du\,dv
$$

Il segno dipende dall'orientazione.

## Significato intuitivo

L'integrale di I specie somma valori scalari pesati dall'area. Il flusso misura quanta parte del campo attraversa la superficie nella direzione della normale scelta.

## Punti delicati

- Parametrizzazione.
- Orientazione.
- Normale.
- Distinguere I specie e II specie.

## Esempio standard

Per $F=(x,y,z)$ sul triangolo del piano $x+y+z=1$ nel primo ottante, orientato verso l'alto:

$$
\iint_SF\cdot n\,dS=\frac{1}{2}
$$

## Domande del professore

- Che cosa cambia tra integrale di superficie scalare e flusso?
- Che ruolo ha la normale?

## Collegamenti

- [[superfici]]
- [[gauss]]
- [[stokes]]
- [[integrali_superficie_I_specie]]
- [[flusso_integrali_superficie_II_specie]]
