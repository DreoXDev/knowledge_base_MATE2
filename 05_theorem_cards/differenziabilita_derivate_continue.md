# Teorema: derivate parziali continue implicano differenziabilita'

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 15
- Affidabilita': alta
- Dimostrazione richiesta: da verificare nelle note del corso
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa come criterio sufficiente pratico per stabilire la differenziabilita'.

## Enunciato

Sia $f$ una funzione di $n$ variabili. Se $f$ possiede le derivate parziali del primo ordine in un intorno di:

$$
P=(\bar{x}_1,\dots,\bar{x}_n)
$$

e queste sono continue in $P$, allora $f$ e' differenziabile in $P$.

## Ipotesi

- Derivate parziali del primo ordine esistenti in un intorno di $P$.
- Derivate parziali continue in $P$.

## Tesi

$f$ e' differenziabile in $P$.

## Dimostrazione

Idea della dimostrazione nel caso di due variabili. Per $P=(x_0,y_0)$ si scrive l'incremento come somma di due incrementi lungo direzioni coordinate:

$$
f(x,y)-f(x_0,y_0)
=
[f(x,y)-f(x_0,y)]+[f(x_0,y)-f(x_0,y_0)].
$$

Applicando il teorema di Lagrange in una variabile a ciascun termine:

$$
f(x,y)-f(x_0,y_0)
=
f_x(\xi,y)(x-x_0)+f_y(x_0,\eta)(y-y_0).
$$

Per la continuita' delle derivate parziali in $P$, i coefficienti si avvicinano a $f_x(P)$ e $f_y(P)$. Quindi l'incremento si scrive come parte lineare piu' errore infinitesimo:

$$
f(x,y)-f(P)
=
f_x(P)(x-x_0)+f_y(P)(y-y_0)+o(\|(x,y)-P\|).
$$

Questo e' proprio il criterio di differenziabilita'. In piu' variabili il ragionamento si ripete spezzando l'incremento lungo le direzioni coordinate.

## Punti delicati

- E' un criterio sufficiente, non una condizione necessaria.
- L'esistenza delle derivate parziali senza continuita' non basta in generale.

## Collegamenti

- [[differenziabilita]]
- [[derivate_parziali]]
