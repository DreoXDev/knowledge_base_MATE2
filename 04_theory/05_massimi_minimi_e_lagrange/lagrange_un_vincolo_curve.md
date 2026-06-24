# Moltiplicatori di Lagrange con un vincolo in $\mathbb{R}^2$

## Stato

- Fonte: `01_sources/official_slides/5_lezione_moltiplicatori_lagrange.pdf`
- Slide: 1-16
- Affidabilita': alta, con nota su probabile refuso nella slide 7
- Ultimo aggiornamento: 2026-06-23

## Problema

Studiare i punti stazionari di una funzione:

$$
f(x,y)
$$

ristretta alla curva vincolo:

$$
g(x,y)=c.
$$

## Metodo 1: parametrizzazione

Si cerca una parametrizzazione:

$$
x=x(t),\qquad y=y(t)
$$

e si studia:

$$
F(t)=f(x(t),y(t)).
$$

## Metodo 2: Lagrange

Si introduce:

$$
L(x,y,\lambda)=f(x,y)-\lambda(g(x,y)-c).
$$

Le condizioni di stazionarieta' sono:

$$
f_x=\lambda g_x
$$

$$
f_y=\lambda g_y
$$

$$
g=c
$$

equivalentemente:

$$
\nabla f(P)=\lambda\nabla g(P).
$$

## Interpretazione geometrica

In un punto stazionario vincolato, la derivata direzionale di $f$ lungo ogni vettore tangente alla curva vincolo e' nulla.

Quindi $\nabla f(P)$ e' ortogonale alla curva.

Poiche' anche $\nabla g(P)$ e' ortogonale alla curva di livello $g=c$, i due gradienti sono paralleli:

$$
\nabla f(P)=\lambda\nabla g(P).
$$

Nota: la slide 7 sembra dire che $\nabla f(P)$ e $\nabla g(P)$ sono linearmente indipendenti; dalla conclusione devono invece essere dipendenti/paralleli.

## Esempio ufficiale

Punto della retta:

$$
x-y=3
$$

a minima distanza da $(1,2)$.

Risultato:

$$
(3,0)
$$

distanza:

$$
2\sqrt{2}.
$$

## Errori da evitare

- Dimenticare il vincolo $g=c$ nel sistema.
- Dire che $\nabla f=0$: nel problema vincolato non e' richiesto.
- Non verificare che il punto trovato appartenga al vincolo.
- Confondere parallelismo e ortogonalita': $\nabla f$ e' ortogonale al vincolo e parallelo a $\nabla g$.

## Collegamenti

- [[curve_di_livello]]
- [[lagrange]]
- [[formule_distanza_retta_piano]]

