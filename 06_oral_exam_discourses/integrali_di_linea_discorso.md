# Discorso orale: Integrali di linea

## Obiettivo

Preparare una risposta da esame orale su questo argomento.

## Durata target

- Risposta breve: 1 minuto.
- Risposta completa: 3-5 minuti.
- Con dimostrazione: 5-8 minuti.

## Versione breve

Per gli integrali di linea di I specie si integra una funzione scalare lungo una curva usando l'elemento di lunghezza $d\ell$.

Se $C$ e' parametrizzata da $r(t)$, allora:

$$
\int_C f\,d\ell=\int f(r(t))\|r'(t)\|\,dt.
$$

Il caso $f=1$ restituisce la lunghezza della curva. Per il discorso completo vedi [[integrali_linea_I_specie_discorso]].

Per gli integrali di linea di II specie, invece, si integra un campo vettoriale lungo una curva orientata:

$$
\int_C F\cdot \tau\,d\ell
=
\int F(r(t))\cdot r'(t)\,dt
$$

per una parametrizzazione concorde. Per il discorso completo vedi [[integrali_linea_II_specie_discorso]].

## Versione completa

Gli integrali di linea permettono di integrare lungo una curva invece che su un intervallo. Per la prima specie l'integranda e' una funzione scalare e il peso geometrico e' la lunghezza elementare della curva. Per la seconda specie l'integranda e' un campo vettoriale e si considera la sua componente tangenziale lungo una curva orientata.

Operativamente, per la I specie si parametrizza la curva, si sostituiscono le coordinate nella funzione e si usa $d\ell=\|r'(t)\|dt$. Per la II specie si calcola invece $F(r(t))\cdot r'(t)$.

## Dimostrazione parlata

La formula deriva dal passaggio dall'ascissa curvilinea al parametro arbitrario. Se $\ell$ misura la lunghezza lungo la curva, allora:

$$
\frac{d\ell}{dt}=\|r'(t)\|.
$$

Quindi:

$$
\int_C f\,d\ell=\int f(r(t))\|r'(t)\|\,dt.
$$

## Frasi utili

- "L'idea geometrica e' che..."
- "Le ipotesi servono a garantire che..."
- "Questo teorema mette in relazione..."
- "Un caso particolare importante e'..."

## Follow-up probabili

- Che cos'e' $d\ell$?
- Perche' il caso $f=1$ da' la lunghezza?
- Come si collega al baricentro di un filo?
- Che differenza c'e' tra I specie e II specie?
- Perche' la II specie dipende dall'orientazione?

## Errori da evitare

- Dimenticare il fattore $\|r'(t)\|$.
- Confondere $dt$ con $d\ell$.
- Dimenticare il prodotto scalare $F(r(t))\cdot r'(t)$ nella II specie.
