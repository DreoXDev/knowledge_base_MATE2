# Discorso orale - Funzione implicita

## Versione da 30 secondi

Il teorema della funzione implicita dice quando un'equazione $F(x,y)=0$ permette di scrivere localmente $y=f(x)$, oppure $F(x,y,z)=0$ permette di scrivere $z=f(x,y)$.

## Enunciati e formule

In due variabili, se $F(x_0,y_0)=0$ e $F_y(x_0,y_0)\neq0$, allora localmente $y=f(x)$ e:

$$
f'=-\frac{F_x}{F_y}
$$

In tre variabili, se $F_z\neq0$, allora localmente $z=f(x,y)$ e:

$$
f_x=-\frac{F_x}{F_z},\qquad f_y=-\frac{F_y}{F_z}
$$

## Intuizione geometrica

In due variabili una curva di livello puo' diventare localmente un grafico. In tre variabili una superficie di livello puo' diventare localmente un grafico.

## Esempi

- Circonferenza: vicino ai punti con $F_y\neq0$ si puo' scrivere $y=f(x)$.
- Sfera: lontano dall'equatore rispetto alla variabile $z$, si puo' scrivere $z=f(x,y)$.

## Errori da evitare

- Isolare una variabile rispetto alla quale la derivata e' nulla.
- Confondere condizione sufficiente locale con descrizione globale.

## Mini ripasso

Guardo quale derivata parziale non si annulla. Quella e' la variabile che posso isolare localmente. Le formule delle derivate si ottengono derivando implicitamente.
