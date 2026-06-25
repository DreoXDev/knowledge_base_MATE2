# Teorema: differenziabilita' e continuita'

## Stato

- Fonte: `01_sources/official_slides/2_lezione_funzioni_due_variabili_curve_livello.pdf`
- Slide: 11
- Affidabilita': alta
- Dimostrazione richiesta: da verificare
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per collegare l'approssimazione lineare locale alla continuita' della funzione.

## Enunciato

Se $f$ e' differenziabile in un punto, allora $f$ e' continua in quel punto.

## Ipotesi

- $f:D\subset\mathbb{R}^n\to\mathbb{R}$.
- $f$ differenziabile nel punto $\bar{x}$.

## Tesi

$$
\lim_{x\to\bar{x}} f(x)=f(\bar{x}).
$$

## Significato intuitivo

Se una funzione e' ben approssimata da una funzione affine con errore piu' piccolo della distanza dal punto, allora non puo' avere salto nel punto.

## Dimostrazione

La differenziabilita' in $\bar{x}$ significa che:

$$
f(x)=f(\bar{x})+L(x-\bar{x})+o(\|x-\bar{x}\|)
$$

per una applicazione lineare $L$. Quindi:

$$
f(x)-f(\bar{x})=L(x-\bar{x})+o(\|x-\bar{x}\|).
$$

Quando $x\to\bar{x}$, il termine lineare tende a zero e anche il termine $o(\|x-\bar{x}\|)$ tende a zero. Dunque:

$$
\lim_{x\to\bar{x}}f(x)=f(\bar{x}).
$$

## Collegamenti

- [[differenziabilita]]
- [[intorni_limiti_continuita]]
