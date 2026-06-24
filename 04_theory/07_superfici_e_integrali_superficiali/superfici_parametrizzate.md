# Superfici parametrizzate

## Stato

- Fonte: `01_sources/official_slides/4_lezione_superfici.pdf`
- Slide: 1-8
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Definizione

Una superficie parametrizzata in $\mathbb{R}^3$ e' definita da una funzione:

$$
\mathbf{x}:D\subset\mathbb{R}^2\to\mathbb{R}^3
$$

data da:

$$
\mathbf{x}(s,t)=
\begin{pmatrix}
x(s,t)\\
y(s,t)\\
z(s,t)
\end{pmatrix}.
$$

L'immagine di $\mathbf{x}(s,t)$ al variare di $(s,t)\in D$ e' una superficie $S$ in $\mathbb{R}^3$.

## Vettori tangenti

Fissando $t=\bar{t}$ si ottiene una curva sulla superficie. Il vettore:

$$
\mathbf{x}_s(\bar{s},\bar{t})
=
\begin{pmatrix}
\frac{\partial x}{\partial s}(\bar{s},\bar{t})\\
\frac{\partial y}{\partial s}(\bar{s},\bar{t})\\
\frac{\partial z}{\partial s}(\bar{s},\bar{t})
\end{pmatrix}
$$

e' tangente a questa curva.

Fissando $s=\bar{s}$ si ottiene un'altra curva sulla superficie. Il vettore:

$$
\mathbf{x}_t(\bar{s},\bar{t})
=
\begin{pmatrix}
\frac{\partial x}{\partial t}(\bar{s},\bar{t})\\
\frac{\partial y}{\partial t}(\bar{s},\bar{t})\\
\frac{\partial z}{\partial t}(\bar{s},\bar{t})
\end{pmatrix}
$$

e' tangente a questa seconda curva.

## Superficie regolare

La superficie e' regolare se:

1. $\mathbf{x}(s,t)$ e' iniettiva;
2. $\mathbf{x}_s$ e $\mathbf{x}_t$ sono linearmente indipendenti in ogni punto.

L'indipendenza lineare garantisce che i due vettori tangenti generino un piano tangente ben definito.

Nota: l'iniettivita' globale e' delicata per parametrizzazioni periodiche, ad esempio sulla sfera. Per ora si segue la formulazione della slide.

## Esempio: sfera

$$
\mathbf{x}(\theta,\varphi)
=
\begin{pmatrix}
R\cos\theta\cos\varphi\\
R\cos\theta\sin\varphi\\
R\sin\theta
\end{pmatrix}
$$

con:

$$
\theta\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right],
\qquad
\varphi\in[0,2\pi).
$$

L'angolo $\theta$ e' la latitudine, mentre $\varphi$ e' la longitudine.

Le curve $\mathbf{x}(\theta,\bar{\varphi})$ sono i meridiani. Le curve $\mathbf{x}(\bar{\theta},\varphi)$ sono i paralleli.

I vettori tangenti sono:

$$
\mathbf{x}_\theta
=
\begin{pmatrix}
-R\sin\theta\cos\varphi\\
-R\sin\theta\sin\varphi\\
R\cos\theta
\end{pmatrix}
$$

e:

$$
\mathbf{x}_\varphi
=
\begin{pmatrix}
-R\cos\theta\sin\varphi\\
R\cos\theta\cos\varphi\\
0
\end{pmatrix}.
$$

## Superfici come grafici

Una superficie grafico ha parametrizzazione:

$$
\mathbf{x}(x,y)=
\begin{pmatrix}
x\\
y\\
f(x,y)
\end{pmatrix}
$$

e vettori tangenti:

$$
\mathbf{x}_x=
\begin{pmatrix}
1\\
0\\
f_x
\end{pmatrix},
\qquad
\mathbf{x}_y=
\begin{pmatrix}
0\\
1\\
f_y
\end{pmatrix}.
$$

Questi vettori sono indipendenti.

## Teorema locale

Localmente una superficie regolare puo' essere sempre espressa come grafico di una funzione di due variabili.

Per esempio, la sfera di raggio $R$ centrata nell'origine puo' essere rappresentata localmente come unione delle due semisfere:

$$
f(x,y)=\sqrt{R^2-x^2-y^2}
$$

e:

$$
f(x,y)=-\sqrt{R^2-x^2-y^2}.
$$

## Figure

- `08_visuals/figures/lezione_4_slide_06_sfera.png`

## Domande orali

- Che cos'e' una superficie parametrizzata?
- Che cosa sono $\mathbf{x}_s$ e $\mathbf{x}_t$?
- Quando una superficie e' regolare?
- Come si parametrizza una sfera?
- Che cosa sono meridiani e paralleli?
- Perche' un grafico di funzione e' una superficie regolare?

## Collegamenti

- [[piano_tangente_superfici]]
- [[superfici_di_livello]]

