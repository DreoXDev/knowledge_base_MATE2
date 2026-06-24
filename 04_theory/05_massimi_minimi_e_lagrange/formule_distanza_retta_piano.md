# Formule di distanza da rette e piani

## Stato

- Fonte: `01_sources/official_slides/5_lezione_moltiplicatori_lagrange.pdf`
- Slide: 10-12, 23-24
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Distanza punto-retta nel piano

La distanza tra un punto $P=(\bar{x},\bar{y})$ e una retta:

$$
ax+by=c
$$

e':

$$
\frac{|a\bar{x}+b\bar{y}-c|}{\sqrt{a^2+b^2}}.
$$

Nell'esempio della retta $x-y=3$ e del punto $(1,2)$:

$$
\frac{|1-2-3|}{\sqrt{2}}
=
2\sqrt{2}.
$$

## Distanza punto-piano nello spazio

La distanza tra un punto $P=(\bar{x},\bar{y},\bar{z})$ e un piano:

$$
ax+by+cz=d
$$

e':

$$
\frac{|a\bar{x}+b\bar{y}+c\bar{z}-d|}
{\sqrt{a^2+b^2+c^2}}.
$$

Nell'esempio del piano $x+y+z=0$ e del punto $(1,1,1)$:

$$
\frac{|1+1+1|}{\sqrt{1+1+1}}
=
\sqrt{3}.
$$

## Uso nei problemi di ottimizzazione

Nei problemi di distanza si puo' minimizzare la distanza al quadrato, perche' la radice quadrata e' crescente sui valori non negativi.

## Collegamenti

- [[lagrange_un_vincolo_curve]]
- [[lagrange_un_vincolo_superfici]]
- [[lagrange_due_vincoli]]

