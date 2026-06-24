# Curve parametrizzate

## Stato

- Fonte: `01_sources/official_slides/1_lezione_II_2022_23_SDM.pdf`
- Slide: 1-12
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Idea intuitiva

Una curva parametrizzata descrive il moto di un punto nello spazio al variare di un parametro $t$.

Il parametro puo' essere pensato come tempo, ma in generale e' solo una variabile reale che ordina i punti percorsi dalla curva.

## Definizione

Una curva parametrizzata in $\mathbb{R}^n$ e' una funzione:

$$
x : [a,b]\subset\mathbb{R}\to\mathbb{R}^n
$$

data da:

$$
x(t)=
\begin{pmatrix}
x_1(t)\\
\vdots\\
x_n(t)
\end{pmatrix}
$$

Le funzioni $x_i(t)$, con $i=1,\dots,n$, sono dette componenti della curva.

## Vettore tangente

Se le componenti $x_i(t)$ sono derivabili con continuita', il vettore:

$$
\frac{dx}{dt}
=
\left(
\frac{dx_1}{dt},
\dots,
\frac{dx_n}{dt}
\right)
$$

calcolato in $\bar{t}$ si chiama vettore tangente alla curva nel punto:

$$
(x_1(\bar{t}),\dots,x_n(\bar{t})).
$$

Se $t$ rappresenta il tempo, allora il vettore tangente si chiama anche vettore velocita'.

## Curva regolare

La lezione considera una curva $x(t):[a,b]\subset\mathbb{R}\to\mathbb{R}^n$ tale che:

1. $x(t_1)\neq x(t_2)$ se $t_1\neq t_2$ e $t_1,t_2\in[a,b]$;
2. la lunghezza del vettore tangente sia strettamente positiva per ogni valore del parametro:

$$
\left\|
\frac{dx}{dt}
\right\|
=
\sqrt{
\left(\frac{dx_1}{dt}\right)^2
+
\cdots
+
\left(\frac{dx_n}{dt}\right)^2
}
>0.
$$

In questo caso la parametrizzazione e' detta regolare.

## Curva chiusa regolare

Se $x(a)=x(b)$ e valgono tutte le restanti condizioni, allora la curva e' detta curva chiusa regolare.

Nota: la condizione di iniettivita' va trattata con attenzione nel caso chiuso, perche' per curve chiuse si ammette $x(a)=x(b)$.

## Esempi fondamentali

### Moto rettilineo uniforme

La curva:

$$
x(t)=vt+x_0,\qquad t\in[a,b]
$$

descrive il segmento di retta che congiunge:

$$
x_a=va+x_0
$$

e:

$$
x_b=vb+x_0.
$$

In componenti:

$$
x_i(t)=v_i t+x_i^0.
$$

Il vettore tangente e':

$$
\frac{dx}{dt}=v,
$$

quindi e' costante.

### Moto rettilineo non uniforme

La curva in $\mathbb{R}^2$:

$$
x(t)=t^3,\qquad y(t)=t^3
$$

ha sostegno sulla retta:

$$
y=x.
$$

Il vettore tangente e':

$$
\frac{dx}{dt}=3t^2,\qquad
\frac{dy}{dt}=3t^2.
$$

La curva geometrica e' una retta, ma la velocita' dipende dal parametro.

### Moto su una semiretta

La curva:

$$
x(t)=t^2,\qquad y(t)=t^2
$$

soddisfa:

$$
y=x,\qquad x\geq 0,\qquad y\geq 0.
$$

Il sostegno e' quindi una semiretta nel primo quadrante.

Il vettore tangente e':

$$
\frac{dx}{dt}=2t,\qquad
\frac{dy}{dt}=2t.
$$

Questa parametrizzazione non e' regolare in $t=0$, perche' il vettore tangente si annulla.

### Moto circolare uniforme

La curva:

$$
x(t)=R\cos t,\qquad y(t)=R\sin t,\qquad t\in[0,2\pi]
$$

descrive una circonferenza, perche':

$$
x^2+y^2=R^2.
$$

Il vettore tangente e':

$$
\frac{dx}{dt}=-R\sin t,\qquad
\frac{dy}{dt}=R\cos t.
$$

La sua lunghezza e' costante e vale $R$.

### Elica nello spazio

La curva in $\mathbb{R}^3$:

$$
x(t)=R\cos t,\qquad y(t)=R\sin t,\qquad z(t)=ct,\qquad t\in[0,2\pi]
$$

ha vettore tangente:

$$
\frac{dx}{dt}=-R\sin t,\qquad
\frac{dy}{dt}=R\cos t,\qquad
\frac{dz}{dt}=c.
$$

La lunghezza del vettore tangente e':

$$
\sqrt{R^2+c^2}.
$$

Nota di verifica: nella slide il testo del vettore tangente sembra omettere il fattore $R$ nelle prime due componenti. Qui e' riportata la formula coerente con $x(t)=R\cos t$ e $y(t)=R\sin t$.

## Intuizione geometrica

La curva geometrica e la parametrizzazione non sono la stessa cosa.

Due parametrizzazioni possono descrivere lo stesso sostegno geometrico ma con velocita' diverse.

Esempi:
- $x(t)=t^3$, $y(t)=t^3$ descrive la retta $y=x$, ma con velocita' non costante.
- $x(t)=t^2$, $y(t)=t^2$ descrive solo la semiretta $y=x$, $x,y\geq 0$.

## Grafici / Figure

- Vettore velocita' su semiretta: `08_visuals/figures/lezione_II_slide_08_velocita_semiretta.png`
- Vettore velocita' su circonferenza: `08_visuals/figures/lezione_II_slide_10_velocita_circonferenza.png`
- Elica nello spazio: `08_visuals/figures/lezione_II_slide_12_elica.png`

## Collegamenti

- [[lunghezza_arco_curva]]
- [[integrali di linea di prima specie]]
- [[integrali di linea di seconda specie]]

## Domande orali possibili

- Che cos'e' una curva parametrizzata?
- Che differenza c'e' tra curva geometrica e parametrizzazione?
- Che cos'e' il vettore tangente?
- Quando una curva e' regolare?
- Perche' $x(t)=t^2$, $y(t)=t^2$ non e' regolare in $t=0$?
- Che cosa significa curva chiusa regolare?

## Risposta breve da orale

Una curva parametrizzata in $\mathbb{R}^n$ e' una funzione vettoriale $x:[a,b]\to\mathbb{R}^n$. Le sue componenti sono le funzioni $x_1(t),\dots,x_n(t)$. Se queste componenti sono derivabili con continuita', il vettore $\frac{dx}{dt}$ e' il vettore tangente, o vettore velocita' se $t$ rappresenta il tempo. La parametrizzazione e' regolare quando la norma del vettore tangente non si annulla mai.

