# Teorema: Gauss-Ostrogradski

## Stato

- Fonte: Lezione 11, slide 35-48.
- Affidabilita': alta.
- Ultimo aggiornamento: 2026-06-24

## Enunciato

Se $\Omega\subset\mathbb{R}^3$ e' un dominio semplice limitato con frontiera $S=\partial\Omega$ e $n$ e' la normale uscente, allora:

$$
\iint_SF\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

## Ipotesi

- $\Omega$ dominio semplice limitato.
- $S=\partial\Omega$ differenziabile a tratti.
- $F$ regolare nel dominio, frontiera inclusa.

## Significato intuitivo

Il flusso uscente totale e' la somma delle sorgenti interne misurate dalla divergenza.

## Punti delicati

- La superficie deve essere chiusa.
- La normale e' sempre uscente.
- Nei gusci, sulla superficie interna la normale uscente punta verso il centro.

## Esempio standard

Per $F=(x,y,z)$ sulla sfera di raggio $R$:

$$
\iint_SF\cdot n\,dS=4\pi R^3
$$

## Collegamenti

- [[formula_gauss_ostrogradski]]
- [[divergenza]]
- [[flusso_integrale_superficie_II_specie]]
