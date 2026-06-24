# Campi vettoriali

## Stato

- Fonte: `01_sources/official_slides/8_lezione_integrali_linea_II_specie.pdf`
- Slide: 1-10
- Affidabilita': alta

## Definizione

Un campo vettoriale:

$$
F:\Omega\subset\mathbb{R}^n\to\mathbb{R}^n
$$

e' un'applicazione che a ogni punto $x\in\Omega$ associa un vettore $F(x)$.

## Esempi fisici

- Campo gravitazionale.
- Campo di forze.
- Campo delle velocita' di un fluido.

## Rappresentazione nel piano

Per rappresentare graficamente un campo vettoriale nel piano:

1. scelto $(x,y)$, si considera $F(x,y)$;
2. si trasla il vettore affinche' abbia origine in $(x,y)$;
3. si ripete per vari punti del piano.

## Esempio: campo rotazionale

Consideriamo:

$$
F(x,y)=(-y,x).
$$

In forma con la base canonica:

$$
F=-y e_1+x e_2.
$$

Il vettore ha lunghezza:

$$
\|F(x,y)\|=\sqrt{x^2+y^2}
$$

e coincide con il vettore velocita' del moto circolare:

$$
x=r\cos t,\qquad y=r\sin t
$$

perche':

$$
\frac{dx}{dt}=-r\sin t=-y
$$

$$
\frac{dy}{dt}=r\cos t=x.
$$

## Figure

- `08_visuals/figures/lezione_8_slide_08_campo_circonferenza.png`
- `08_visuals/figures/lezione_8_slide_10_campo_normalizzato.png`

## Domande orali

- Che cos'e' un campo vettoriale?
- Come si rappresenta graficamente?
- Che esempi fisici conosci?
- Perche' $F(x,y)=(-y,x)$ e' tangente alle circonferenze centrate nell'origine?

## Collegamenti

- [[integrali_linea_II_specie]]
- [[campi_conservativi]]
