# Moltiplicatori di Lagrange con un vincolo in $\mathbb{R}^3$

## Stato

- Fonte: `01_sources/official_slides/5_lezione_moltiplicatori_lagrange.pdf`
- Slide: 17-27
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Problema

Studiare i punti stazionari di:

$$
f(x,y,z)
$$

ristretta a una superficie vincolo:

$$
G(x,y,z)=c.
$$

## Metodo 1: parametrizzazione della superficie

Si parametrizza la superficie:

$$
(x(u,v),y(u,v),z(u,v))
$$

e si studia:

$$
F(u,v)=f(x(u,v),y(u,v),z(u,v)).
$$

## Metodo 2: Lagrange

Si introduce:

$$
L(x,y,z,\lambda)
=
f(x,y,z)-\lambda(G(x,y,z)-c).
$$

Le condizioni sono:

$$
\nabla f(P)=\lambda\nabla G(P)
$$

$$
G(x,y,z)=c.
$$

## Interpretazione geometrica

In un punto stazionario vincolato, $\nabla f(P)$ e' ortogonale alla superficie.

Poiche' $\nabla G(P)$ e' normale alla superficie di livello $G=c$, si ha:

$$
\nabla f(P)=\lambda\nabla G(P).
$$

## Esempio ufficiale

Punto del piano:

$$
x+y+z=0
$$

a minima distanza da $(1,1,1)$.

Risultato:

$$
(0,0,0)
$$

e:

$$
\lambda=-2.
$$

La distanza e':

$$
\sqrt{3}.
$$

## Nota di attenzione

Nel metodo con parametrizzazione, la costante nello sviluppo di $F(s,t)$ sembra avere un refuso nelle slide. Il punto di minimo non cambia.

## Collegamenti

- [[superfici_di_livello]]
- [[gradiente_superfici_livello]]
- [[formule_distanza_retta_piano]]

