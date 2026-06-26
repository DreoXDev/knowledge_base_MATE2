# Integrali doppi per fili - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare del metodo dei fili per gli integrali doppi. L'idea e' calcolare un integrale doppio sommando contributi lungo curve o segmenti, spesso quando il dominio e' piu' comodo da descrivere con una famiglia di fili.

Nel discorso voglio collegare sezioni del dominio, integrali iterati, coordinate adatte e differenza rispetto al metodo per strati.

## Tempo stimato

- Versione essenziale: 7 minuti
- Versione completa con esempio: 12 minuti
- Estensioni/domande su coordinate e cambiamento di variabili: 5 minuti

Totale realistico: 12-17 minuti.

## Discorso principale

> "Partirei dall'idea: il metodo per fili consiste nel vedere il dominio come unione di fili, cioe' di sezioni semplici, e poi sommare il contributo di tutti questi fili."

In pratica, scelgo una variabile che individua il filo e una variabile che percorre il filo. Per esempio, se il dominio e' descritto da:

$$
D=\{(x,y):c\le y\le d,\ \gamma(y)\le x\le\delta(y)\},
$$

allora sto usando fili orizzontali:

$$
\iint_D f(x,y)\,dx\,dy
=
\int_c^d\left(\int_{\gamma(y)}^{\delta(y)}f(x,y)\,dx\right)dy.
$$

## 2. Prerequisiti richiamati rapidamente

### [[integrali_multipli|Integrale doppio]]

Somma una funzione su un dominio piano.

**Possibile domanda del prof:** perche' posso iterare?

**Risposta breve:** per il teorema di riduzione degli integrali doppi su domini regolari.

### [[integrazione_per_fili|Metodo dei fili]]

Consiste nel fissare una variabile e integrare lungo la sezione corrispondente.

**Possibile domanda del prof:** fili e strati sono due metodi diversi?

**Risposta breve:** sono due modi geometrici di leggere lo stesso integrale iterato, scegliendo sezioni comode.

### Coordinate adatte

A volte i fili diventano piu' naturali dopo un cambio di coordinate, per esempio polari.

**Possibile domanda del prof:** quando conviene cambiare coordinate?

**Risposta breve:** quando il dominio o la funzione hanno simmetria.

## 3. Definizione operativa

Il metodo dei fili ha tre passi:

1. Disegno il dominio.
2. Scelgo una famiglia di fili che lo ricopre senza sovrapposizioni.
3. Scrivo l'integrale interno lungo il filo e l'integrale esterno sull'insieme dei fili.

In forma semplice:

$$
\iint_D f\,dA
=
\int_{\text{fili}}\left(\int_{\text{singolo filo}}f\,ds_{\text{piano}}\right).
$$

Nel caso cartesiano questo diventa un integrale iterato ordinario.

## 4. Primo esempio da fare alla lavagna

Prendo il triangolo:

$$
D=\{(x,y):0\le y\le1,\ y\le x\le1\}.
$$

Lo leggo per fili orizzontali: fissato $y$, il filo va da $x=y$ a $x=1$.

Quindi:

$$
\iint_D f(x,y)\,dx\,dy
=
\int_0^1\int_y^1 f(x,y)\,dx\,dy.
$$

Se $f=1$:

$$
\int_0^1\int_y^1 1\,dx\,dy
=
\int_0^1(1-y)\,dy
=
\frac12.
$$

### Cosa dire a voce

Il filo e' orizzontale: prima percorro il filo, poi faccio variare l'altezza $y$.

## 5. Collegamento con coordinate polari

Nel disco:

$$
D=\{(r,\theta):0\le r\le R,\ 0\le\theta\le2\pi\}
$$

posso pensare a fili radiali: fisso $\theta$ e faccio variare $r$.

Ricordo pero' che:

$$
dA=r\,dr\,d\theta.
$$

Quindi:

$$
\iint_D f(x,y)\,dx\,dy
=
\int_0^{2\pi}\int_0^R f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta.
$$

**Da dire a voce:** nelle coordinate non cartesiane il fattore jacobiano e' essenziale.

## 6. Disegni da fare alla lavagna

### Disegno 1 - fili orizzontali

Disegno un dominio e una famiglia di segmenti orizzontali.

### Disegno 2 - fili radiali

Disegno un disco e raggi che partono dall'origine.

### Disegno 3 - confronto con strati

Scrivo:

"strati = sezioni pensate come fette; fili = sezioni pensate come curve da percorrere".

## Collegamenti utili nella KB

- [[integrazione_per_fili]]
- [[integrazione_per_strati]]
- [[integrali_iterati]]
- [[cambiamento_variabili_integrali_multipli]]
- [[coordinate_polari]]

## Immagini / visualizzazioni utili

![[lezione_10_slide_36_integrazione_fili.png]]

Questa immagine e' il riferimento principale per il metodo dei fili.

![[lezione_10_coordinate_polari.png]]

Utile quando i fili sono radiali e il dominio ha simmetria circolare.

## 15. Versione discorso continuo da imparare

"Il metodo dei fili per gli integrali doppi consiste nel descrivere il dominio come unione di sezioni, che chiamo fili. Scelgo una variabile che identifica il filo e una variabile che percorre il filo. In coordinate cartesiane, per esempio, fissato $y$ posso integrare lungo un segmento orizzontale in $x$ e poi sommare tutti i fili al variare di $y$. Il metodo e' molto vicino agli integrali iterati: la differenza e' soprattutto geometrica, perche' mi aiuta a leggere correttamente il dominio. In coordinate polari i fili possono essere raggi o circonferenze, ma in quel caso bisogna ricordare il jacobiano, per esempio $dA=r\,dr\,d\theta$."

## 16. Versione lavagna

1. Disegno il dominio.
2. Evidenzio un filo.
3. Scrivo:

$$
\iint_D f\,dA
=
\int_{\text{parametro dei fili}}
\int_{\text{filo}} f.
$$

4. Nel caso cartesiano:

$$
\int_c^d\int_{\gamma(y)}^{\delta(y)}f(x,y)\,dx\,dy.
$$

## 17. Possibili domande del professore

### 1. Che cos'e' un filo?

Una sezione del dominio ottenuta fissando una variabile o un parametro.

### 2. Che differenza c'e' con gli strati?

Sono letture geometriche simili; il punto e' scegliere sezioni comode.

### 3. Dove entra il jacobiano?

Quando uso coordinate non cartesiane.

### 4. Come evito sovrapposizioni?

Scelgo una famiglia di fili che ricopra il dominio una sola volta.

### 5. Qual e' l'errore piu' comune?

Dimenticare il fattore $r$ nelle coordinate polari.

## 18. Mini-checklist finale

- So disegnare i fili.
- So scrivere l'integrale interno.
- So indicare il parametro esterno.
- So usare coordinate polari con jacobiano.
- So distinguere metodo e calcolo meccanico.

## 19. Controlli qualitativi

- Non usare fili che coprono due volte il dominio.
- Non dimenticare il jacobiano.
- Non saltare il disegno.
