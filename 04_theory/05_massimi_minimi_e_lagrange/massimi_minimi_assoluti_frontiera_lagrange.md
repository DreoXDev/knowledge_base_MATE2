# Massimi/minimi assoluti: frontiera e Lagrange

## Stato

- Fonte: `01_sources/official_slides/6_lezione_massimi_minimi_assoluti.pdf`
- Slide: 29-44
- Affidabilita': alta

## Quando serve

Quando la frontiera del dominio e' descritta da un'equazione, conviene studiarla come vincolo e usare i moltiplicatori di Lagrange.

Per un disco:

$$
x^2+y^2\leq a^2
$$

la frontiera e':

$$
G(x,y)=x^2+y^2=a^2.
$$

## Esempio sui dischi

Si considera:

$$
f(x,y)=3x^2+4y^2-6x
$$

su:

$$
x^2+y^2\leq a^2.
$$

Il punto stazionario interno e' $(1,0)$.

Sulla frontiera si risolve:

$$
6x-6=2x\lambda
$$

$$
8y=2y\lambda
$$

$$
x^2+y^2=a^2.
$$

Dalla seconda equazione:

$$
2y(4-\lambda)=0.
$$

Quindi $y=0$, oppure $\lambda=4$. Nel secondo caso si ottiene $x=-3$ e:

$$
y=\pm\sqrt{a^2-9}.
$$

Questi ultimi punti esistono solo se $a\geq 3$.

## Risultati dei casi della lezione

Per $a=\frac{1}{2}$:

- minimo assoluto in $\left(\frac{1}{2},0\right)$;
- massimo assoluto in $\left(-\frac{1}{2},0\right)$.

Per $a=2$:

- minimo assoluto in $(1,0)$;
- massimo assoluto in $(-2,0)$.

Per $a=4$:

- minimo assoluto in $(1,0)$;
- massimo assoluto in $(-3,\sqrt{7})$ e $(-3,-\sqrt{7})$.

## Due vincoli: sfera e piano

Per la curva intersezione:

$$
x^2+y^2+z^2=6
$$

$$
x+y+z=0
$$

si minimizza/massimizza la distanza al quadrato da $(1,1,0)$:

$$
f=(x-1)^2+(y-1)^2+z^2.
$$

Il sistema di Lagrange e':

$$
\nabla f=\lambda_1\nabla G_1+\lambda_2\nabla G_2.
$$

I candidati ottenuti sono:

$$
(1,1,-2),\qquad (-1,-1,2).
$$

Poiche':

$$
f(1,1,-2)=4,\qquad f(-1,-1,2)=12,
$$

il punto di minima distanza e' $(1,1,-2)$ e il punto di massima distanza e' $(-1,-1,2)$.

Nota: la slide 44 sembra indicare di nuovo $(1,1,-2)$ come massimo; dai valori e' un probabile refuso.

## Collegamenti

- [[massimi_minimi_assoluti]]
- [[lagrange]]
- [[lagrange_due_vincoli]]
- [[lagrange_ottimizzazione_vincolata]]
