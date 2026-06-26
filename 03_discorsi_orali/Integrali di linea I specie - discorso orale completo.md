# Integrali di linea I specie - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare degli integrali di linea di prima specie. L'idea centrale e' integrare una funzione scalare lungo una curva, pesando ogni punto con l'elemento di lunghezza $ds$. Quindi non sto calcolando il lavoro di un campo, ma sto sommando una densita' distribuita su una curva.

Nel discorso voglio collegare curve parametrizzate, lunghezza d'arco, indipendenza dalla parametrizzazione e applicazioni come massa di un filo e baricentro.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con esempi fisici: 12 minuti
- Estensioni/domande su parametrizzazione e baricentro: 5 minuti

Totale realistico: 12-17 minuti.

## Discorso principale

> "Partirei dalla differenza rispetto agli integrali di seconda specie: nella prima specie integro una funzione scalare lungo una curva, quindi uso l'elemento di lunghezza."

Se $\gamma:[a,b]\to\mathbb R^n$ e' una curva regolare e $f$ e' una funzione scalare, definisco:

$$
\int_\gamma f\,ds
=
\int_a^b f(\gamma(t))\|\gamma'(t)\|\,dt.
$$

> "Il fattore $\|\gamma'(t)\|$ serve a trasformare il parametro $t$ in lunghezza effettiva lungo la curva."

## 2. Prerequisiti richiamati rapidamente

### [[curve_parametrizzate|Curva parametrizzata]]

Una curva e' una funzione:

$$
\gamma(t)=(x(t),y(t),z(t)).
$$

**Possibile domanda del prof:** perche' parametrizzo?

**Risposta breve:** per ridurre l'integrale sulla curva a un integrale ordinario in $t$.

### [[lunghezza_arco_curva|Elemento di arco]]

L'elemento di lunghezza e':

$$
ds=\|\gamma'(t)\|\,dt.
$$

**Possibile domanda del prof:** cosa succede se la curva e' percorsa piu' velocemente?

**Risposta breve:** cambia $\|\gamma'(t)\|$, ma il prodotto finale rappresenta sempre lunghezza geometrica.

### Funzione scalare

La funzione $f$ assegna un numero a ogni punto della curva.

**Possibile domanda del prof:** che differenza c'e' con la seconda specie?

**Risposta breve:** qui integro scalari rispetto a lunghezza; nella seconda specie integro un campo vettoriale lungo una direzione.

## 3. Definizione formale

Sia $\gamma:[a,b]\to\mathbb R^n$ una curva regolare e sia $f$ continua sul sostegno della curva. Allora:

$$
\int_\gamma f\,ds
=
\int_a^b f(\gamma(t))\|\gamma'(t)\|\,dt.
$$

Se $f=1$, ottengo la lunghezza della curva:

$$
L(\gamma)=\int_a^b\|\gamma'(t)\|\,dt.
$$

## 4. Primo esempio da fare alla lavagna

Prendo la circonferenza unitaria:

$$
\gamma(t)=(\cos t,\sin t),\qquad t\in[0,2\pi].
$$

Allora:

$$
\gamma'(t)=(-\sin t,\cos t),\qquad \|\gamma'(t)\|=1.
$$

Se $f(x,y)=1$, allora:

$$
\int_\gamma 1\,ds=\int_0^{2\pi}1\,dt=2\pi.
$$

### Cosa dire a voce

Questo recupera la lunghezza della circonferenza unitaria.

## 5. Interpretazione fisica

Se $f$ e' una densita' lineare $\rho$, allora:

$$
m=\int_\gamma \rho\,ds
$$

e' la massa del filo.

Il baricentro si calcola con:

$$
\bar x=\frac{1}{m}\int_\gamma x\rho\,ds,\qquad
\bar y=\frac{1}{m}\int_\gamma y\rho\,ds.
$$

**Da dire a voce:** la prima specie e' naturale quando la curva e' un oggetto geometrico, come un filo.

## 6. Disegni da fare alla lavagna

### Disegno 1 - curva suddivisa

Disegno una curva spezzata in piccoli archi e scrivo $ds$ su un pezzetto.

### Disegno 2 - filo con densita'

Disegno una curva piu' spessa e scrivo $\rho(x,y)$ lungo il filo.

### Disegno 3 - confronto con seconda specie

Scrivo:

$$
\int_\gamma f\,ds
\qquad\text{contro}\qquad
\int_\gamma \vec F\cdot d\vec r.
$$

## Collegamenti utili nella KB

- [[integrali_linea_I_specie]]
- [[curve_parametrizzate]]
- [[lunghezza_arco_curva]]
- [[baricentro_filo]]
- [[integrali_linea_II_specie]]

## Immagini / visualizzazioni utili

![[oral_linea_I_somme.png]]

Questa immagine aiuta a vedere l'integrale come somma lungo piccoli tratti di curva.

![[lezione_7_slide_02_suddivisione_curva.png]]

Utile per richiamare la suddivisione della curva e il passaggio al limite.

## 15. Versione discorso continuo da imparare

"Gli integrali di linea di prima specie servono a integrare una funzione scalare lungo una curva. Se la curva e' parametrizzata da $\gamma(t)$, l'integrale non e' semplicemente l'integrale di $f(\gamma(t))$, perche' devo tener conto della lunghezza effettiva percorsa. Per questo compare il fattore $\|\gamma'(t)\|$, cioe' $ds=\|\gamma'(t)\|dt$. La formula e' quindi $\int_\gamma f\,ds=\int_a^b f(\gamma(t))\|\gamma'(t)\|dt$. Se $f=1$ ottengo la lunghezza della curva; se $f$ e' una densita' lineare ottengo la massa di un filo. La differenza con la seconda specie e' che qui integro una quantita' scalare rispetto alla lunghezza, mentre nella seconda specie integro un campo vettoriale nella direzione del moto."

## 16. Versione lavagna

1. Scrivo $\gamma:[a,b]\to\mathbb R^n$.
2. Scrivo $ds=\|\gamma'(t)\|dt$.
3. Scrivo:

$$
\int_\gamma f\,ds=\int_a^b f(\gamma(t))\|\gamma'(t)\|dt.
$$

4. Aggiungo i casi $f=1$ e $f=\rho$.

## 17. Possibili domande del professore

### 1. Che cosa si integra nella prima specie?

Una funzione scalare lungo una curva.

### 2. Perche' compare $\|\gamma'(t)\|$?

Perche' converte il parametro in lunghezza d'arco.

### 3. Dipende dall'orientazione?

No, perche' compare la norma della velocita'.

### 4. Se $f=1$ cosa ottengo?

La lunghezza della curva.

### 5. Differenza con seconda specie?

Prima specie: scalare per lunghezza. Seconda specie: campo vettoriale per spostamento orientato.

## 18. Mini-checklist finale

- So scrivere la definizione.
- So spiegare $ds$.
- So dire che non dipende dall'orientazione.
- So fare l'esempio della circonferenza.
- So collegare massa e baricentro.

## 19. Controlli qualitativi

- Non dimenticare $\|\gamma'(t)\|$.
- Non confondere $ds$ con $dt$.
- Non parlare di lavoro fisico: quello e' seconda specie.
