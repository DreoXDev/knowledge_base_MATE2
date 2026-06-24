# Definizione: campo conservativo

## Stato

- Fonte: `01_sources/official_slides/8_lezione_integrali_linea_II_specie.pdf`
- Pagina/slide: 18-19
- Affidabilita': alta
- Dimostrazione richiesta: non richiesta per la definizione
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per riconoscere i campi vettoriali che sono gradienti di una funzione potenziale.

## Definizione

Un campo vettoriale $F$ si dice conservativo o potenziale se esiste una funzione $U$ tale che:

$$
F=\nabla U.
$$

La funzione $U$ si chiama potenziale del campo.

## Ipotesi

- Campo vettoriale $F$ definito su un dominio $D$.
- Esistenza di una funzione $U:D\to\mathbb{R}$.

## In coordinate

Se:

$$
F=(F_1,\dots,F_n),
$$

allora $F=\nabla U$ significa:

$$
F_i=\frac{\partial U}{\partial x_i}
$$

per ogni $i$.

## Significato intuitivo

Un campo conservativo deriva da un potenziale scalare.

## Significato geometrico

L'integrale di linea di II specie di un campo conservativo dipende solo dagli estremi del cammino.

## Dimostrazione

Vedi [[campi_conservativi_indipendenza_cammino]].

## Punti delicati

- Dominio.
- Potenziale.
- Curve chiuse.
- Rotore nullo.

## Esempio standard

$$
F=(3x^2y,x^3+1)=\nabla(x^3y+y).
$$

## Domande del professore

- Quando un campo e' conservativo?
- Rotore nullo implica sempre conservativita'?
- Che ruolo ha il dominio?

## Collegamenti

- [[potenziale]]
- [[rotore]]
- [[integrali_linea_II_specie]]
- [[campi_conservativi_indipendenza_cammino]]
