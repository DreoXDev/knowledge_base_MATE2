# Integrali doppi per strati - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare del calcolo degli integrali doppi per strati. L'idea e' descrivere un dominio piano come unione di segmenti verticali o orizzontali e trasformare l'integrale doppio in un integrale iterato.

Nel discorso voglio collegare dominio normale, ordine di integrazione, estremi variabili e interpretazione geometrica come somma di strati.

## Tempo stimato

- Versione essenziale: 7 minuti
- Versione completa con cambio d'ordine: 12 minuti
- Estensioni/domande su regioni non normali: 5 minuti

Totale realistico: 12-17 minuti.

## Discorso principale

> "Partirei dall'idea geometrica: per calcolare un integrale doppio posso tagliare il dominio in strati, cioe' in segmenti paralleli, e integrare prima lungo ogni segmento e poi sommare tutti gli strati."

Se il dominio e' normale rispetto a $x$, cioe':

$$
D=\{(x,y):a\le x\le b,\ \alpha(x)\le y\le\beta(x)\},
$$

allora:

$$
\iint_D f(x,y)\,dx\,dy
=
\int_a^b\left(\int_{\alpha(x)}^{\beta(x)}f(x,y)\,dy\right)dx.
$$

## 2. Prerequisiti richiamati rapidamente

### [[integrali_multipli|Integrale doppio]]

L'integrale doppio somma una funzione su una regione piana.

**Possibile domanda del prof:** che cosa rappresenta geometricamente?

**Risposta breve:** se $f\ge0$, rappresenta un volume sotto il grafico di $f$ sopra il dominio $D$.

### [[integrali_iterati|Integrale iterato]]

Un integrale iterato calcola prima rispetto a una variabile e poi rispetto all'altra.

**Possibile domanda del prof:** l'ordine conta?

**Risposta breve:** il valore finale e' lo stesso sotto ipotesi regolari, ma gli estremi cambiano.

### Dominio normale

Un dominio normale rispetto a $x$ e' tagliato da rette verticali in segmenti.

**Possibile domanda del prof:** se non e' normale?

**Risposta breve:** lo divido in piu' domini normali.

## 3. Definizione formale

Se:

$$
D=\{(x,y):a\le x\le b,\ \alpha(x)\le y\le\beta(x)\},
$$

allora:

$$
\iint_D f(x,y)\,dx\,dy
=
\int_a^b\int_{\alpha(x)}^{\beta(x)}f(x,y)\,dy\,dx.
$$

Se invece:

$$
D=\{(x,y):c\le y\le d,\ \gamma(y)\le x\le\delta(y)\},
$$

allora:

$$
\iint_D f(x,y)\,dx\,dy
=
\int_c^d\int_{\gamma(y)}^{\delta(y)}f(x,y)\,dx\,dy.
$$

## 4. Primo esempio da fare alla lavagna

Prendo:

$$
D=\{(x,y):0\le x\le 1,\ 0\le y\le x\}.
$$

Allora:

$$
\iint_D f(x,y)\,dx\,dy
=
\int_0^1\int_0^x f(x,y)\,dy\,dx.
$$

Se $f(x,y)=1$, ottengo l'area:

$$
\int_0^1\int_0^x1\,dy\,dx
=
\int_0^1x\,dx
=
\frac12.
$$

### Cosa dire a voce

Qui sto sommando segmenti verticali di lunghezza $x$, mentre $x$ varia da 0 a 1.

## 5. Cambio dell'ordine di integrazione

Lo stesso triangolo puo' essere descritto anche come:

$$
D=\{(x,y):0\le y\le1,\ y\le x\le1\}.
$$

Quindi:

$$
\iint_D f(x,y)\,dx\,dy
=
\int_0^1\int_y^1 f(x,y)\,dx\,dy.
$$

**Da dire a voce:** cambiare ordine significa ridisegnare il dominio e riscrivere correttamente gli estremi.

## 6. Disegni da fare alla lavagna

### Disegno 1 - strati verticali

Disegno il dominio e un segmento verticale da $y=\alpha(x)$ a $y=\beta(x)$.

### Disegno 2 - strati orizzontali

Disegno lo stesso dominio e un segmento orizzontale da $x=\gamma(y)$ a $x=\delta(y)$.

### Disegno 3 - dominio da spezzare

Disegno una regione non normale e la divido in due regioni normali.

## Collegamenti utili nella KB

- [[integrali_iterati]]
- [[integrali_multipli]]
- [[integrazione_per_strati]]
- [[inversione_ordine_integrazione]]
- [[misura_jordan]]

## Immagini / visualizzazioni utili

![[lezione_10_slide_08_suddivisione_dominio.png]]

Questa immagine aiuta a vedere il dominio come somma di parti elementari.

![[lezione_10_slide_19_sezione_trasversale.png]]

Utile per l'idea di sezione o strato.

## 15. Versione discorso continuo da imparare

"Gli integrali doppi per strati si basano sull'idea di descrivere il dominio come unione di segmenti verticali o orizzontali. Se il dominio e' normale rispetto a $x$, lo posso scrivere come $a\le x\le b$ e $\alpha(x)\le y\le\beta(x)$. Allora l'integrale doppio diventa un integrale iterato: prima integro rispetto a $y$ lungo il segmento verticale, poi sommo questi contributi al variare di $x$. Se il dominio e' normale rispetto a $y$, faccio l'analogo con segmenti orizzontali. Il punto piu' importante all'orale e' disegnare il dominio: gli estremi non si indovinano, si leggono dal disegno."

## 16. Versione lavagna

1. Disegno $D$.
2. Scrivo:

$$
D=\{(x,y):a\le x\le b,\ \alpha(x)\le y\le\beta(x)\}.
$$

3. Scrivo:

$$
\iint_D f\,dx\,dy
=
\int_a^b\int_{\alpha(x)}^{\beta(x)}f(x,y)\,dy\,dx.
$$

4. Mostro il cambio d'ordine.

## 17. Possibili domande del professore

### 1. Che cosa vuol dire integrare per strati?

Tagliare il dominio in segmenti e sommare i contributi.

### 2. Che cos'e' un dominio normale?

Un dominio intersecato da ogni retta parallela a un asse in un segmento.

### 3. Se il dominio non e' normale?

Lo divido in domini normali.

### 4. Come cambio ordine di integrazione?

Ridisegno il dominio e riscrivo gli estremi rispetto all'altra variabile.

### 5. Qual e' l'errore piu' comune?

Scambiare gli estremi senza ridisegnare il dominio.

## 18. Mini-checklist finale

- So riconoscere un dominio normale.
- So scrivere gli estremi.
- So cambiare ordine.
- So spiegare il significato geometrico.
- So spezzare un dominio non normale.

## 19. Controlli qualitativi

- Disegnare sempre il dominio.
- Non invertire gli estremi a memoria.
- Non confondere strati con fili.
