# Massimi e minimi locali

## Stato

- Fonte: `01_sources/official_slides/3_lezione_massimi_minimi_locali.pdf`
- Slide: 12-15
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Massimo locale

$P$ e' un punto di massimo locale per $f$ se esiste un intorno $B_\delta(P)$ tale che:

$$
f(P')\leq f(P)
$$

per ogni $P'\in B_\delta(P)$.

E' massimo locale stretto se:

$$
f(P')<f(P)
$$

per ogni $P'\neq P$ sufficientemente vicino.

## Minimo locale

$P$ e' un punto di minimo locale per $f$ se esiste un intorno $B_\delta(P)$ tale che:

$$
f(P')\geq f(P)
$$

per ogni $P'\in B_\delta(P)$.

E' minimo locale stretto se:

$$
f(P')>f(P)
$$

per ogni $P'\neq P$ sufficientemente vicino.

## Condizione necessaria di estremo

Se $f$ ha un estremo locale in $P$ e le derivate parziali prime esistono in $P$, allora:

$$
f_{x_i}(P)=0
$$

per ogni $i$.

Equivalentemente:

$$
\nabla f(P)=0.
$$

## Punto stazionario

Un punto $P$ e' stazionario se:

$$
\nabla f(P)=0.
$$

## Interpretazione geometrica

Per funzioni di due variabili, se $P$ e' un punto stazionario, il piano tangente e' orizzontale:

$$
z=f(P).
$$

## Attenzione

Essere punto stazionario e' condizione necessaria ma non sufficiente per essere massimo o minimo. Anche un punto sella puo' avere piano tangente orizzontale.

## Collegamenti

- [[condizione_necessaria_estremo]]
- [[punti_stazionari]]
- [[test_hessiano_massimi_minimi]]

