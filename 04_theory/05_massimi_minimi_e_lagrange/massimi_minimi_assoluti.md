# Massimi e minimi assoluti

## Stato

- Fonte: `01_sources/official_slides/6_lezione_massimi_minimi_assoluti.pdf`
- Slide: 4-44
- Affidabilita': alta

## Teorema di esistenza

Se:

$$
f:D\subset\mathbb{R}^n\to\mathbb{R}
$$

e' continua su un insieme chiuso e limitato $D$, allora $f$ ammette punti di minimo assoluto e punti di massimo assoluto.

Questo e' il teorema di Weierstrass nel contesto della lezione.

## Idea centrale

Gli estremi assoluti possono stare nell'interno del dominio, sulla frontiera, oppure nei vertici o negli estremi dei tratti di frontiera.

Per questo non basta risolvere $\nabla f=0$.

## Metodo operativo

1. Verificare che il dominio sia chiuso e limitato.
2. Cercare i punti stazionari interni con $\nabla f=0$.
3. Studiare la restrizione di $f$ alla frontiera.
4. Aggiungere vertici o estremi dei tratti di frontiera.
5. Valutare $f$ su tutti i candidati.
6. Confrontare i valori.

## Rettangolo

Per:

$$
f(x,y)=x^2-2xy+2y
$$

su:

$$
R=[0,3]\times[0,2]
$$

il punto stazionario interno e' $(1,1)$. La frontiera si studia lato per lato:

$$
x=t,\ y=0,\quad x=3,\ y=t,\quad x=t,\ y=2,\quad x=0,\ y=t.
$$

I candidati finali sono:

$$
(0,0),\ (3,0),\ (0,2),\ (3,2),\ (1,1),\ (2,2).
$$

Il massimo assoluto e' in $(3,0)$; i minimi assoluti sono in $(0,0)$ e $(2,2)$.

## Triangolo

Per:

$$
f(x,y)=x^3-x^2y+3xy^2
$$

sul triangolo di vertici $(0,0)$, $(1,0)$, $(1,1)$, i candidati finali sono:

$$
(0,0),\ (1,0),\ (1,1),\ \left(1,\frac{1}{6}\right).
$$

Il massimo assoluto e' in $(1,1)$; il minimo assoluto e' in $(0,0)$.

## Parametrizzazione di un segmento

Il segmento da $(x_1,y_1)$ a $(x_2,y_2)$ si parametrizza con:

$$
x=x_1+t(x_2-x_1)
$$

$$
y=y_1+t(y_2-y_1)
$$

con $t\in[0,1]$.

## Collegamenti

- [[intorni_aperti_chiusi]]
- [[massimi_minimi_assoluti_frontiera_lagrange]]
- [[lagrange_due_vincoli]]
- [[weierstrass_massimi_minimi_assoluti]]
- [[massimi_minimi_assoluti_metodo]]
