# Formula: lunghezza di un arco di curva

## Stato

- Fonte: `01_sources/official_slides/1_lezione_II_2022_23_SDM.pdf`
- Slide: 13-17
- Affidabilita': alta
- Dimostrazione richiesta: piu' che dimostrazione, derivazione intuitiva tramite approssimazione
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per calcolare la lunghezza di una curva regolare parametrizzata.

## Ipotesi

- Curva parametrizzata $x:[a,b]\to\mathbb{R}^n$.
- Componenti derivabili con continuita'.
- Curva regolare, cioe' $\left\|\frac{dx}{dt}\right\|>0$.

## Formula

$$
\ell
=
\int_a^b
\left\|
\frac{dx}{dt}
\right\|
dt
$$

equivalentemente:

$$
\ell
=
\int_a^b
\sqrt{
\left(\frac{dx_1}{dt}\right)^2
+
\cdots
+
\left(\frac{dx_n}{dt}\right)^2
}
\,dt.
$$

## Significato intuitivo

La lunghezza si ottiene integrando la velocita' scalare lungo l'intervallo di parametrizzazione.

## Derivazione intuitiva

Si approssima localmente la curva con il suo sviluppo di Taylor del primo ordine. Ogni tratto piccolo viene sostituito da un segmento, la cui lunghezza e' approssimata dalla norma del vettore tangente moltiplicata per $\Delta t$. Sommando questi contributi su una partizione e passando al limite si ottiene:

$$
\ell
=
\int_a^b
\left\|
\frac{dx}{dt}
\right\|
dt.
$$

## Esempi standard

- Lunghezza di un segmento.
- Lunghezza di una circonferenza.

## Domande del professore

- Perche' si integra la norma del vettore tangente?
- Cosa rappresenta $\left\|\frac{dx}{dt}\right\|$?
- Come si ricava la formula con Taylor del primo ordine?

## Collegamenti

- [[curve_parametrizzate]]
- [[lunghezza_arco_curva]]

