# Discorso orale: massimi e minimi assoluti

## Versione breve

Per trovare massimi e minimi assoluti su un dominio chiuso e limitato parto dal teorema di Weierstrass, che garantisce l'esistenza degli estremi se la funzione e' continua.

Poi costruisco l'elenco dei candidati: punti stazionari interni, punti critici sulla frontiera e vertici. Infine valuto la funzione su tutti i candidati e confronto i valori.

## Versione completa

Il punto importante e' che un estremo assoluto non deve per forza essere un punto stazionario interno. Se sta sulla frontiera, la condizione $\nabla f=0$ non e' in generale necessaria.

Su un rettangolo o su un triangolo studio la frontiera parametrizzando i lati. Su un disco studio la circonferenza di frontiera e posso usare Lagrange:

$$
\nabla f=\lambda\nabla G.
$$

Se la frontiera e' una curva intersezione di due vincoli nello spazio, uso:

$$
\nabla f=\lambda_1\nabla G_1+\lambda_2\nabla G_2.
$$

Il passaggio finale e' sempre il confronto dei valori di $f$.

## Errori da evitare

- Fermarsi a $\nabla f=0$.
- Dimenticare i vertici.
- Usare Lagrange e non confrontare i valori finali.

## Collegamenti

- [[weierstrass_discorso]]
- [[lagrange_discorso]]
