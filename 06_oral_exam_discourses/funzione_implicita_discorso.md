# Discorso orale: Funzione implicita

## Obiettivo

Preparare una risposta da esame orale su questo argomento.

## Durata target

- Risposta breve: 1 minuto.
- Risposta completa: 3-5 minuti.
- Con dimostrazione: 5-8 minuti.

## Versione breve

Il teorema della funzione implicita dice quando un'equazione $F=0$ permette di isolare localmente una variabile come funzione delle altre.

In due variabili, se $F(x_0,y_0)=0$ e $F_y(x_0,y_0)\neq 0$, allora vicino al punto posso scrivere $y=f(x)$ e:

$$
f'=-\frac{F_x}{F_y}.
$$

In tre variabili, se $F_z(x_0,y_0,z_0)\neq 0$, posso scrivere $z=f(x,y)$ e:

$$
f_x=-\frac{F_x}{F_z},\qquad f_y=-\frac{F_y}{F_z}.
$$

## Versione completa

Il problema e' capire quando un'equazione implicita, come una curva di livello o una superficie di livello, puo' essere vista localmente come grafico.

Per $F(x,y)=0$, l'ipotesi $F_y\neq 0$ dice che la variabile $y$ e' isolabile localmente. Per $F(x,y,z)=0$, l'ipotesi $F_z\neq 0$ permette di isolare $z$.

Geometricamente, una curva regolare puo' essere vista localmente come grafico, e una superficie regolare puo' essere vista localmente come grafico, purche' si scelga una variabile isolabile.

## Dimostrazione parlata

Si deriva l'identita' $F(x,f(x))=0$ e si ottiene $F_x+F_y f'=0$. Da qui segue $f'=-F_x/F_y$.

In tre variabili si deriva $F(x,y,f(x,y))=0$ rispetto a $x$ e a $y$, ottenendo $f_x=-F_x/F_z$ e $f_y=-F_y/F_z$.

## Frasi utili

- "L'idea geometrica e' che..."
- "Le ipotesi servono a garantire che..."
- "Questo teorema mette in relazione..."
- "Un caso particolare importante e'..."

## Follow-up probabili

- Perche' serve $F_y\neq 0$?
- Dove non si applica alla circonferenza?
- Dove non si applica alla sfera se voglio scrivere $z=f(x,y)$?

## Errori da evitare

- Confondere risultato locale e globale.
- Provare a isolare $y$ quando $F_y=0$.
- Provare a isolare $z$ quando $F_z=0$.
