# Teorema: funzione implicita

## Stato

- Fonte: `01_sources/official_slides/6_lezione_massimi_minimi_assoluti.pdf`
- Pagina/slide: 45-59
- Affidabilita': alta
- Dimostrazione richiesta: formule derivate tramite derivazione identita'
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa quando un'equazione del tipo $F=0$ definisce localmente una variabile come funzione delle altre.

## Enunciato

In due variabili, se $F(x_0,y_0)=0$ e $F_y(x_0,y_0)\neq 0$, allora localmente si puo' scrivere $y=f(x)$.

In tre variabili, se $F(x_0,y_0,z_0)=0$ e $F_z(x_0,y_0,z_0)\neq 0$, allora localmente si puo' scrivere $z=f(x,y)$.

## Ipotesi

- Derivate parziali continue nell'intorno del punto.
- Punto sulla curva/superficie: $F=0$.
- Derivata rispetto alla variabile da isolare non nulla.

## Tesi

$$
y=f(x)\quad\text{oppure}\quad z=f(x,y)
$$

## Significato intuitivo

Vicino a un punto regolare, una curva o una superficie di livello puo' essere vista come un grafico.

## Significato geometrico

Per le curve di livello si puo' isolare localmente una coordinata; per le superfici di livello si puo' descrivere localmente la superficie come grafico.

## Dimostrazione

Dall'identita' $F(x,f(x))=0$:

$$
F_x+F_y f'=0
$$

quindi:

$$
f'=-\frac{F_x}{F_y}.
$$

Dall'identita' $F(x,y,f(x,y))=0$:

$$
F_x+F_z f_x=0,\qquad F_y+F_z f_y=0,
$$

quindi:

$$
f_x=-\frac{F_x}{F_z},\qquad f_y=-\frac{F_y}{F_z}.
$$

## Punti delicati

- Per scrivere $y=f(x)$ serve $F_y\neq 0$.
- Per scrivere $z=f(x,y)$ serve $F_z\neq 0$.
- Il risultato e' locale, non necessariamente globale.

## Esempio standard

- Circonferenza $x^2+y^2=1$: localmente $y=\pm\sqrt{1-x^2}$ dove $y\neq 0$.
- Sfera $x^2+y^2+z^2=1$: localmente $z=\pm\sqrt{1-x^2-y^2}$ dove $z\neq 0$.

## Domande del professore

- Quali sono le ipotesi?
- Dove si usa la condizione sulla derivata non nulla?
- Come si interpreta geometricamente?
- Come si ricavano le formule delle derivate?

## Collegamenti

- [[funzione_implicita_due_variabili]]
- [[funzione_implicita_tre_variabili]]
- [[funzione_implicita_curve_livello]]
- [[funzione_implicita_superfici_livello]]
