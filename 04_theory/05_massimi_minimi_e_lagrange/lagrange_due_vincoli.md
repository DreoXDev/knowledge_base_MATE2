# Moltiplicatori di Lagrange con due vincoli

## Stato

- Fonte: `01_sources/official_slides/5_lezione_moltiplicatori_lagrange.pdf`
- Slide: 28-42
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Problema

Studiare i punti stazionari di:

$$
f(x,y,z)
$$

ristretta alla curva $C$ ottenuta come intersezione di due superfici:

$$
G_1(x,y,z)=c_1
$$

$$
G_2(x,y,z)=c_2.
$$

Si assume che:

$$
\nabla G_1,\nabla G_2
$$

siano linearmente indipendenti.

## Metodo 1: parametrizzazione

Si parametrizza la curva $C$ e si studia la funzione composta di una variabile.

## Metodo 2: due moltiplicatori

Si introduce:

$$
L(x,y,z,\lambda_1,\lambda_2)
=
f(x,y,z)
-
\lambda_1(G_1(x,y,z)-c_1)
-
\lambda_2(G_2(x,y,z)-c_2).
$$

Il sistema e':

$$
\nabla f
=
\lambda_1\nabla G_1+\lambda_2\nabla G_2
$$

$$
G_1(x,y,z)=c_1
$$

$$
G_2(x,y,z)=c_2.
$$

## Interpretazione geometrica

La curva $C$ e' intersezione di due superfici. Il piano normale alla curva e' generato da:

$$
\nabla G_1(P)
$$

e:

$$
\nabla G_2(P).
$$

Nel punto stazionario vincolato, $\nabla f(P)$ deve appartenere a questo piano normale, quindi e' combinazione lineare dei due gradienti.

## Esempi ufficiali

### Intersezione di $x+y+z=0$ e $x-z=1$

Minimizzare:

$$
f(x,y,z)=x^2+y^2+z^2.
$$

Risultato:

$$
\left(\frac{1}{2},0,-\frac{1}{2}\right).
$$

### Intersezione di $2x-3y-z=4$ e $x-2y-2z=1$

Risultato:

$$
(1,-1,1).
$$

## Collegamenti

- [[superfici_di_livello]]
- [[formule_distanza_retta_piano]]

