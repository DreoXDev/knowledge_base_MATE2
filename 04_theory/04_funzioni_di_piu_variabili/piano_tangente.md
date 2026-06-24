# Piano tangente

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 16-19
- Affidabilita': alta, con refuso da verificare sull'esempio delle slide 18-19
- Ultimo aggiornamento: 2026-06-23

## Definizione

Per una funzione di due variabili $f(x,y)$ differenziabile in:

$$
P=(\bar{x},\bar{y})
$$

il piano:

$$
z-f(P)
=
f_x(P)(x-\bar{x})
+
f_y(P)(y-\bar{y})
$$

si chiama piano tangente al grafico di $f$ in:

$$
(\bar{x},\bar{y},f(\bar{x},\bar{y})).
$$

## Approssimazione lineare

La differenziabilita' significa che vicino a $P$ la funzione e' ben approssimata dalla funzione lineare:

$$
f^{lin}(x,y)
=
f(\bar{x},\bar{y})
+
f_x(P)(x-\bar{x})
+
f_y(P)(y-\bar{y}).
$$

Il piano tangente e' il grafico di $f^{lin}$.

## Nota sull'esempio delle slide

La slide 18 considera $f=x^2+y^2$, ma poi indica $f(1,1)=-2$. Questo e' incompatibile con $x^2+y^2$.

Con $f=-x^2-y^2$ si avrebbe $f(1,1)=-2$, ma le derivate sarebbero $f_x(1,1)=-2$ e $f_y(1,1)=-2$, mentre la slide riporta valori positivi.

Per ora l'esempio va segnato come da verificare e non usato come fonte consolidata per un calcolo finale.

## Grafici / Figure

- `08_visuals/figures/lezione_2_slide_19_piano_tangente.png`

## Collegamenti

- [[differenziabilita]]
- [[piano_tangente]]

