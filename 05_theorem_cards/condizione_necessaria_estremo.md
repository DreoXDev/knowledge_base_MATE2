# Teorema: condizione necessaria di estremo locale

## Stato

- Fonte: `01_sources/official_slides/3_lezione_massimi_minimi_locali.pdf`
- Slide: 13
- Affidabilita': alta
- Dimostrazione richiesta: si
- Ultimo aggiornamento: 2026-06-23

## Enunciato

Supponiamo che $f:\mathbb{R}^n\to\mathbb{R}$ abbia un estremo locale in:

$$
P=(\bar{x}_1,\dots,\bar{x}_n).
$$

Se le derivate parziali prime esistono in $P$, allora:

$$
f_{x_i}(P)=0
$$

per ogni $i=1,\dots,n$.

## Dimostrazione

Si restringe $f$ alla retta:

$$
x_1=\bar{x}_1+t,\qquad
x_2=\bar{x}_2,\dots,x_n=\bar{x}_n.
$$

La funzione:

$$
F(t)=f(\bar{x}_1+t,\bar{x}_2,\dots,\bar{x}_n)
$$

ha un estremo in $t=0$. Quindi:

$$
F'(0)=0.
$$

Ma per definizione:

$$
F'(0)=f_{x_1}(P).
$$

Dunque:

$$
f_{x_1}(P)=0.
$$

Il ragionamento e' analogo per le altre variabili.

## Punti delicati

- La condizione e' necessaria, non sufficiente.
- Serve l'esistenza delle derivate parziali prime in $P$.

## Collegamenti

- [[massimi_minimi_locali]]
- [[punti_stazionari]]

