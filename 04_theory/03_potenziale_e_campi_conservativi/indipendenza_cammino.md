# Indipendenza dal cammino

## Stato

- Fonte: `01_sources/official_slides/9_lezione_campi_vettoriali_conservativi.pdf`
- Slide: 1-7
- Affidabilita': alta

## Teorema

Sia:

$$
F=F_1(x,y)e_1+F_2(x,y)e_2
$$

continuo e definito in un dominio aperto e connesso per archi $D$.

Se l'integrale di linea di II specie di $F$ non dipende dal cammino, allora $F$ e' conservativo.

## Costruzione del potenziale

Fissato $P_0=(x_0,y_0)\in D$, si definisce:

$$
U(x,y)=
\int_{(x_0,y_0)}^{(x,y)}F_1\,dx+F_2\,dy.
$$

Il valore e' ben definito perche' non dipende dal cammino scelto.

## Dimostrazione di $U_x=F_1$

Per $\Delta x$ piccolo, poiche' $D$ e' aperto, il segmento da $(x,y)$ a $(x+\Delta x,y)$ resta in $D$.

Per indipendenza dal cammino:

$$
\Delta U
=
\int_{(x,y)}^{(x+\Delta x,y)}F_1\,dx+F_2\,dy.
$$

Parametrizzando:

$$
x(t)=x+t\Delta x,\qquad y(t)=y,\qquad t\in[0,1],
$$

si ha:

$$
\Delta U
=
\Delta x\int_0^1F_1(x+t\Delta x,y)\,dt.
$$

Per continuita' e passaggio al limite:

$$
U_x=F_1.
$$

Analogamente:

$$
U_y=F_2.
$$

Quindi $F=\nabla U$.

## Collegamenti

- [[campi_conservativi]]
- [[integrali_linea_II_specie]]
- [[circuitazione]]
