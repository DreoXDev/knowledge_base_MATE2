# Funzione implicita

## Stato

- Fonte: `01_sources/official_slides/6_lezione_massimi_minimi_assoluti.pdf`
- Slide: 45-59
- Affidabilita': alta

## Idea

Il teorema della funzione implicita dice quando un'equazione del tipo:

$$
F=0
$$

permette di descrivere localmente una variabile come funzione delle altre.

## Caso di due variabili

Se $F(x_0,y_0)=0$ e:

$$
F_y(x_0,y_0)\neq 0,
$$

allora localmente l'equazione $F(x,y)=0$ definisce una funzione:

$$
y=f(x).
$$

Derivando l'identita' $F(x,f(x))=0$:

$$
F_x+F_y f'=0,
$$

quindi:

$$
f'=-\frac{F_x}{F_y}.
$$

## Caso di tre variabili

Se $F(x_0,y_0,z_0)=0$ e:

$$
F_z(x_0,y_0,z_0)\neq 0,
$$

allora localmente l'equazione $F(x,y,z)=0$ definisce una funzione:

$$
z=f(x,y).
$$

Derivando $F(x,y,f(x,y))=0$:

$$
f_x=-\frac{F_x}{F_z},
\qquad
f_y=-\frac{F_y}{F_z}.
$$

## Significato geometrico

Vicino a un punto regolare, una curva o una superficie di livello puo' essere vista localmente come grafico.

## Collegamenti

- [[funzione_implicita_due_variabili]]
- [[funzione_implicita_tre_variabili]]
- [[funzione_implicita_curve_livello]]
- [[funzione_implicita_superfici_livello]]
