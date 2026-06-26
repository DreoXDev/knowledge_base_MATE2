# Integrali di linea II specie - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare degli integrali di linea di seconda specie. L'idea centrale e' integrare un campo vettoriale lungo una curva orientata, misurando quanto il campo accompagna il movimento lungo la curva. Il caso fisico tipico e' il lavoro di una forza.

Nel discorso voglio collegare curve orientate, campo vettoriale, prodotto scalare con la velocita', dipendenza dall'orientazione e legame con campi conservativi.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con confronto con prima specie: 13 minuti
- Estensioni/domande su lavoro, potenziale e Green: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei dicendo che nella seconda specie non integro una densita' scalare lungo una curva, ma un campo vettoriale lungo una direzione."

Se $\gamma:[a,b]\to\mathbb R^n$ e' una curva regolare orientata e $\vec F$ e' un campo vettoriale, definisco:

$$
\int_\gamma \vec F\cdot d\vec r
=
\int_a^b \vec F(\gamma(t))\cdot\gamma'(t)\,dt.
$$

> "Il prodotto scalare seleziona la componente del campo nella direzione del moto."

## 2. Prerequisiti richiamati rapidamente

### [[campi_vettoriali|Campo vettoriale]]

Un campo vettoriale associa a ogni punto un vettore:

$$
\vec F:\Omega\to\mathbb R^n.
$$

**Possibile domanda del prof:** perche' serve un campo vettoriale?

**Risposta breve:** perche' devo confrontare un vettore del campo con la direzione della curva.

### [[curve_parametrizzate|Curva orientata]]

La parametrizzazione stabilisce anche un verso di percorrenza.

**Possibile domanda del prof:** se inverto il verso?

**Risposta breve:** l'integrale cambia segno.

### Prodotto scalare

Il prodotto $\vec F(\gamma(t))\cdot\gamma'(t)$ misura la componente tangenziale del campo.

**Possibile domanda del prof:** quando il contributo e' nullo?

**Risposta breve:** quando il campo e' ortogonale alla tangente.

## 3. Definizione formale

Se $\gamma(t)=(x(t),y(t),z(t))$ e $\vec F=(P,Q,R)$, allora:

$$
\int_\gamma \vec F\cdot d\vec r
=
\int_a^b
\left[
P(\gamma(t))x'(t)+Q(\gamma(t))y'(t)+R(\gamma(t))z'(t)
\right]dt.
$$

Nel piano:

$$
\int_\gamma P\,dx+Q\,dy.
$$

## 4. Primo esempio da fare alla lavagna

Prendo:

$$
\vec F=(-y,x)
$$

e la circonferenza unitaria orientata positivamente:

$$
\gamma(t)=(\cos t,\sin t),\qquad t\in[0,2\pi].
$$

Allora:

$$
\gamma'(t)=(-\sin t,\cos t),
$$

e:

$$
\vec F(\gamma(t))=(-\sin t,\cos t).
$$

Quindi:

$$
\vec F(\gamma(t))\cdot\gamma'(t)=1,
$$

e:

$$
\int_\gamma \vec F\cdot d\vec r=2\pi.
$$

### Cosa dire a voce

Il campo e' sempre tangente alla circonferenza e concorde con il verso, quindi il lavoro accumula positivamente.

## 5. Collegamento con campi conservativi

Se $\vec F=\nabla U$, allora:

$$
\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1).
$$

Quindi l'integrale dipende solo dagli estremi, non dal cammino.

Se $\gamma$ e' chiusa:

$$
\oint_\gamma \vec F\cdot d\vec r=0.
$$

**Da dire a voce:** questa e' una delle motivazioni principali per studiare i campi conservativi.

## 6. Disegni da fare alla lavagna

### Disegno 1 - campo e tangente

Disegno una curva, un vettore tangente $\gamma'(t)$ e un vettore del campo $\vec F$.

### Disegno 2 - verso opposto

Disegno la stessa curva percorsa al contrario e scrivo:

$$
\int_{-\gamma}\vec F\cdot d\vec r=-\int_\gamma\vec F\cdot d\vec r.
$$

### Disegno 3 - confronto con prima specie

Scrivo:

$$
\int_\gamma f\,ds
\quad\text{non orientato},\qquad
\int_\gamma\vec F\cdot d\vec r
\quad\text{orientato}.
$$

## Collegamenti utili nella KB

- [[integrali_linea_II_specie]]
- [[integrali_linea_I_specie]]
- [[campi_conservativi]]
- [[circuitazione]]
- [[formula_green]]
- [[curve_parametrizzate]]

## Immagini / visualizzazioni utili

![[oral_linea_II_tangente.png]]

Questa immagine serve per ricordare che conta la componente tangenziale del campo.

![[lezione_8_slide_09_campo_circonferenza_vettori.png]]

Utile per visualizzare un campo che gira lungo una circonferenza.

## 15. Versione discorso continuo da imparare

"Gli integrali di linea di seconda specie servono a integrare un campo vettoriale lungo una curva orientata. Se la curva e' parametrizzata da $\gamma(t)$, l'integrale e' $\int_a^b F(\gamma(t))\cdot\gamma'(t)dt$. Il prodotto scalare misura la componente del campo nella direzione di percorrenza della curva. Per questo l'integrale dipende dall'orientazione: se inverto la curva, cambia segno. Nel piano si scrive spesso $\int_\gamma P\,dx+Q\,dy$. Il significato fisico e' il lavoro di un campo di forze lungo un cammino. Se il campo e' conservativo, cioe' e' il gradiente di un potenziale, allora l'integrale dipende solo dagli estremi e vale la differenza di potenziale."

## 16. Versione lavagna

1. Scrivo $\gamma:[a,b]\to\mathbb R^n$.
2. Scrivo:

$$
\int_\gamma \vec F\cdot d\vec r
=
\int_a^b \vec F(\gamma(t))\cdot\gamma'(t)\,dt.
$$

3. Nel piano:

$$
\int_\gamma P\,dx+Q\,dy.
$$

4. Aggiungo il caso conservativo:

$$
\vec F=\nabla U
\Rightarrow
\int_\gamma \vec F\cdot d\vec r=U(B)-U(A).
$$

## 17. Possibili domande del professore

### 1. Che cosa si integra nella seconda specie?

Un campo vettoriale lungo una curva orientata.

### 2. Perche' dipende dal verso?

Perche' cambia segno la velocita' $\gamma'(t)$.

### 3. Che significato fisico ha?

Il lavoro di un campo lungo un cammino.

### 4. Differenza con prima specie?

La prima specie integra scalari rispetto a lunghezza; la seconda integra vettori rispetto a spostamento orientato.

### 5. Cosa succede per campi conservativi?

L'integrale dipende solo dagli estremi.

## 18. Mini-checklist finale

- So scrivere la definizione.
- So spiegare il prodotto scalare.
- So dire che dipende dall'orientazione.
- So collegare lavoro e potenziale.
- So confrontarlo con prima specie.

## 19. Controlli qualitativi

- Non usare $\|\gamma'(t)\|$ al posto di $\gamma'(t)$.
- Non dire che e' indipendente dal cammino in generale.
- Non dimenticare il segno se cambio verso.
