# Funzione implicita in tre variabili

## Stato

- Fonte: `01_sources/official_slides/6_lezione_massimi_minimi_assoluti.pdf`
- Slide: 52-59
- Affidabilita': alta

## Enunciato

Sia $F(x,y,z)$ con derivate parziali continue in un intorno di $(x_0,y_0,z_0)$, con:

$$
F(x_0,y_0,z_0)=0
$$

e:

$$
F_z(x_0,y_0,z_0)\neq 0.
$$

Allora localmente l'equazione $F(x,y,z)=0$ definisce una e una sola funzione $z=f(x,y)$, con $z_0=f(x_0,y_0)$ e derivate parziali continue.

## Derivate

Dall'identita':

$$
F(x,y,f(x,y))=0
$$

si ottiene:

$$
F_x+F_z f_x=0
$$

$$
F_y+F_z f_y=0.
$$

Quindi:

$$
f_x=-\frac{F_x}{F_z},\qquad
f_y=-\frac{F_y}{F_z}.
$$

## Superfici di livello

Una superficie di livello $F(x,y,z)=c$ si riscrive come $F(x,y,z)-c=0$. Se valgono le ipotesi, localmente la superficie si puo' rappresentare come grafico $z=f(x,y)$.

## Esempio: sfera

Per $x^2+y^2+z^2=1$ si pone $F(x,y,z)=x^2+y^2+z^2-1$. Poiche' $F_z=2z$, il teorema si applica dove $z\neq 0$, cioe' fuori dall'equatore se vogliamo scrivere $z=f(x,y)$.

Nella semisfera inferiore:

$$
f(x,y)=-\sqrt{1-x^2-y^2}
$$

e:

$$
f_x=\frac{x}{\sqrt{1-x^2-y^2}},\qquad
f_y=\frac{y}{\sqrt{1-x^2-y^2}}.
$$

Queste formule coincidono con:

$$
f_x=-\frac{F_x}{F_z},\qquad
f_y=-\frac{F_y}{F_z}.
$$

## Collegamenti

- [[superfici_di_livello]]
- [[piano_tangente_superfici]]
- [[funzione_implicita_superfici_livello]]
