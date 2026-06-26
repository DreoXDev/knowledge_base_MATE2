# Discorso orale - Integrali doppi per fili

## Obiettivo del discorso

Spiegare come calcolare un integrale doppio leggendo il dominio come un fascio di fili, cioe' sezioni parallele che vengono sommate una dopo l'altra.

## Tempo stimato

- Versione essenziale: 7 minuti
- Versione completa con esempio e confronto con strati: 12 minuti
- Estensioni/domande su inversione d'ordine e domini spezzati: 4 minuti

Totale realistico: 12-16 minuti.

## Discorso principale

> "Partirei dicendo che fili e strati sono due modi di leggere lo stesso dominio. Cambio prospettiva: invece di vedere il dominio a bande, lo vedo come un insieme di sezioni, cioe' fili."

> "Operativamente scelgo una variabile esterna e, per ogni valore fissato, integro lungo il filo interno."

"integrale doppio come somma di integrali lungo fili"

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_c^d
\left(
\int_{x_1(y)}^{x_2(y)}f(x,y)\,dx
\right)dy.
$$

> "A voce direi: fisso $y$, guardo il filo orizzontale del dominio, integro da sinistra a destra, poi faccio scorrere $y$."

## Piccolo esempio iniziale

Per il triangolo:

$$
\Omega=\{(x,y):0\le y\le 1,\ y\le x\le 1\},
$$

si ha:

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_0^1dy\int_y^1f(x,y)\,dx.
$$

> "Questo e' lo stesso triangolo che potrei descrivere anche nell'altro ordine. Qui pero' lo leggo con fili orizzontali."

## Teorema

Se $\Omega$ e' normale rispetto a $y$:

$$
\Omega=\{(x,y):c\le y\le d,\ x_1(y)\le x\le x_2(y)\},
$$

allora:

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_c^d dy
\int_{x_1(y)}^{x_2(y)}
f(x,y)\,dx.
$$

## Dimostrazione

> "La dimostrazione e' una lettura geometrica delle somme di Riemann: tengo fissa una coordinata, sommo lungo il filo, poi sommo tutti i fili."

Per $y$ fissato, il filo orizzontale e':

$$
x_1(y)\le x\le x_2(y).
$$

Il contributo di quel filo e':

$$
\int_{x_1(y)}^{x_2(y)}f(x,y)\,dx.
$$

Integrando poi rispetto a $y$ si sommano tutti i fili del dominio.

## Conseguenze / osservazioni importanti

- Fili e strati non sono due teorie diverse: sono due letture dello stesso integrale doppio.
- Conviene scegliere i fili quando gli estremi diventano piu' semplici.
- Se il dominio cambia forma, si spezza in sottodomini.
- Il disegno e' parte della soluzione, non un accessorio.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo 1 - Confronto con gli strati

Per lo stesso dominio si puo' spesso scrivere:

$$
\int_a^b dx\int_{y_1(x)}^{y_2(x)}f(x,y)\,dy
$$

oppure:

$$
\int_c^d dy\int_{x_1(y)}^{x_2(y)}f(x,y)\,dx.
$$

> "La scelta migliore e' quella che evita spezzamenti o rende piu' facile l'integrale interno."

### Modulo 2 - Collegamento ai tripli

Nei tripli, la stessa idea diventa integrazione per fili in una direzione, per esempio:

$$
\iiint_D f\,dx\,dy\,dz
=
\iint_S dx\,dy
\int_{z_1(x,y)}^{z_2(x,y)}f(x,y,z)\,dz.
$$

## Cosa scrivere alla lavagna

1. Disegno del dominio con fili orizzontali.
2. Dominio normale:

$$
\Omega=\{c\le y\le d,\ x_1(y)\le x\le x_2(y)\}.
$$

3. Formula:

$$
\iint_\Omega f\,dx\,dy
=
\int_c^d dy\int_{x_1(y)}^{x_2(y)}f(x,y)\,dx.
$$

4. Box: "scelgo l'ordine che descrive meglio il dominio".

## Domande possibili del professore

### Domanda: fili e strati sono la stessa cosa?

Risposta: sono due modi diversi di descrivere il dominio con integrali iterati. L'integrale doppio e' lo stesso, cambia l'ordine di lettura.

### Domanda: come scelgo l'ordine?

Risposta: guardo il disegno e scelgo l'ordine che produce estremi piu' semplici o evita di spezzare il dominio.

### Domanda: cosa succede se il filo incontra il dominio in due intervalli separati?

Risposta: bisogna spezzare il dominio oppure usare l'altro ordine di integrazione.

## Immagini / visualizzazioni utili

![[lezione_10_slide_36_integrazione_fili.png]]

- Figura principale per ricordare la logica dei fili: si integra lungo sezioni e poi si sommano le sezioni.

![[lezione_10_slide_19_sezione_trasversale.png]]

- Utile per collegare l'idea dei fili alle sezioni di un dominio.

## Collegamenti utili nella KB

- [[integrali_iterati]]: formule operative dei due ordini.
- [[inversione_ordine_integrazione]]: confronto tra ordini di integrazione.
- [[integrali_tripli_fili_strati]]: estensione della stessa idea agli integrali tripli.
- [[integrali_multipli_discorso_completo]]: quadro generale sugli integrali multipli.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[integrali_iterati]]
- [[inversione_ordine_integrazione]]
- [[integrali_tripli_fili_strati]]
- `04_theory/08_integrali_multipli/integrali_iterati.md`
- `04_theory/08_integrali_multipli/inversione_ordine_integrazione.md`

### Discorsi collegati

- [[integrali_multipli_discorso_completo]]
- [[integrali_doppi_strati_discorso_completo]]

### Esercizi

- [[integrali_multipli]]
- `07_exercises/esercizi_per_topic/integrali_multipli.md`

### Figure / visual

- `08_visuals/figures/lezione_10_slide_36_integrazione_fili.png`
- `08_visuals/figures/lezione_10_slide_19_sezione_trasversale.png`
