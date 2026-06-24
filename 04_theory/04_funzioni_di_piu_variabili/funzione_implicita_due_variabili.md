# Funzione implicita in due variabili

## Stato

- Fonte: `01_sources/official_slides/6_lezione_massimi_minimi_assoluti.pdf`
- Slide: 45-51
- Affidabilita': alta

## Enunciato

Sia $F(x,y)$ con derivate parziali continue in un intorno di $(x_0,y_0)$, con:

$$
F(x_0,y_0)=0
$$

e:

$$
F_y(x_0,y_0)\neq 0.
$$

Allora localmente l'equazione $F(x,y)=0$ definisce una e una sola funzione $y=f(x)$, con $y_0=f(x_0)$ e derivata continua.

## Derivata

Dall'identita':

$$
F(x,f(x))=0
$$

derivando rispetto a $x$:

$$
F_x+F_y f'=0.
$$

Quindi:

$$
f'=-\frac{F_x}{F_y}.
$$

## Curve di livello

Una curva di livello $F(x,y)=c$ si riscrive come $F(x,y)-c=0$. Se valgono le ipotesi del teorema, localmente la curva e' il grafico di una funzione $y=f(x)$.

## Esempio: circonferenza

Per $x^2+y^2=1$ si pone $F(x,y)=x^2+y^2-1$. Poiche' $F_y=2y$, si puo' scrivere localmente $y=f(x)$ nei punti con $y\neq 0$, quindi non nei punti $(1,0)$ e $(-1,0)$ usando questa scelta.

Nel semipiano superiore:

$$
y=\sqrt{1-x^2}
$$

e:

$$
f'=-\frac{x}{\sqrt{1-x^2}}=-\frac{F_x}{F_y}.
$$

## Collegamenti

- [[curve_di_livello]]
- [[funzione_implicita]]
- [[funzione_implicita_curve_livello]]
