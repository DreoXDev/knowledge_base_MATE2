# Metodo di Lagrange - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare del metodo dei moltiplicatori di Lagrange. L'idea centrale e' trovare massimi e minimi di una funzione quando i punti non sono liberi, ma devono stare su un vincolo.

Nel discorso voglio collegare vincolo, gradiente, condizione geometrica di tangenza e sistema di Lagrange. Il punto delicato e' che il metodo fornisce candidati: poi bisogna discutere l'esistenza e confrontare i valori.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con esempio: 14 minuti
- Estensioni/domande su due vincoli, regolarita' e Weierstrass: 5 minuti

Totale realistico: 14-19 minuti.

## Discorso principale

> "Partirei dall'idea geometrica: se cerco un estremo di $f$ sul vincolo $g=0$, nel punto di estremo la curva di livello di $f$ deve essere tangente al vincolo."

Se il vincolo e' regolare, questo significa che i gradienti sono paralleli:

$$
\nabla f=\lambda \nabla g.
$$

Insieme al vincolo:

$$
g(x,y)=0.
$$

Quindi il sistema di Lagrange e':

$$
\begin{cases}
\nabla f=\lambda\nabla g,\\
g=0.
\end{cases}
$$

## 2. Prerequisiti richiamati rapidamente

### [[gradiente_derivata_direzionale|Gradiente]]

Il gradiente punta nella direzione di massima crescita ed e' ortogonale alle curve di livello.

**Possibile domanda del prof:** perche' entra il gradiente?

**Risposta breve:** perche' all'estremo vincolato confronto le normali alle curve di livello.

### [[massimi_e_minimi_vincolati|Vincolo]]

Il vincolo limita i punti ammissibili, per esempio:

$$
g(x,y)=0.
$$

**Possibile domanda del prof:** posso usare il test hessiano libero?

**Risposta breve:** non direttamente, perche' il dominio ammissibile e' il vincolo.

### [[weierstrass_massimi_minimi_assoluti|Weierstrass]]

Se l'insieme ammissibile e' compatto e $f$ e' continua, massimo e minimo assoluti esistono.

**Possibile domanda del prof:** Lagrange garantisce l'esistenza?

**Risposta breve:** no, fornisce candidati; l'esistenza si discute a parte.

## 3. Enunciato formale

Siano $f,g$ di classe $C^1$ e sia il vincolo:

$$
g(x,y)=0.
$$

Se $P$ e' un estremo vincolato regolare e:

$$
\nabla g(P)\ne0,
$$

allora esiste $\lambda$ tale che:

$$
\nabla f(P)=\lambda\nabla g(P).
$$

## 4. Primo esempio da fare alla lavagna

Massimizzare e minimizzare:

$$
f(x,y)=x+y
$$

sulla circonferenza:

$$
g(x,y)=x^2+y^2-1=0.
$$

Scrivo:

$$
\nabla f=(1,1),\qquad \nabla g=(2x,2y).
$$

Sistema:

$$
\begin{cases}
1=2\lambda x,\\
1=2\lambda y,\\
x^2+y^2=1.
\end{cases}
$$

Dalle prime due equazioni:

$$
x=y.
$$

Allora:

$$
2x^2=1,\qquad x=\pm\frac{1}{\sqrt2}.
$$

I candidati sono:

$$
\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
\qquad
\left(-\frac1{\sqrt2},-\frac1{\sqrt2}\right).
$$

I valori sono:

$$
\sqrt2,\qquad -\sqrt2.
$$

## 5. Interpretazione geometrica

Sulle curve di livello di $f$, il gradiente $\nabla f$ e' normale alla curva di livello. Sul vincolo $g=0$, il gradiente $\nabla g$ e' normale al vincolo.

In un estremo vincolato regolare, la curva di livello di $f$ tocca il vincolo senza attraversarlo. Quindi le normali sono parallele:

$$
\nabla f=\lambda\nabla g.
$$

**Da dire a voce:** $\lambda$ serve solo a dire "paralleli", non ha sempre un significato da calcolare separatamente.

## 6. Disegni da fare alla lavagna

### Disegno 1 - vincolo e curve di livello

Disegno una curva $g=0$ e alcune curve di livello di $f$.

### Disegno 2 - tangenza

Nel punto di estremo disegno la curva di livello tangente al vincolo.

### Disegno 3 - gradienti paralleli

Disegno $\nabla f$ e $\nabla g$ sulla stessa retta normale.

## Collegamenti utili nella KB

- [[lagrange]]
- [[lagrange_un_vincolo_curve]]
- [[lagrange_due_vincoli]]
- [[massimi_minimi_assoluti]]
- [[gradiente_curve_livello]]
- [[weierstrass_massimi_minimi_assoluti]]

## Immagini / visualizzazioni utili

![[oral_lagrange_gradienti_paralleli.png]]

Questa figura e' centrale: mostra la tangenza tra curva di livello e vincolo.

![[lezione_5_slide_05_gradiente_curva_livello.png]]

Utile per ricordare che il gradiente e' ortogonale alle curve di livello.

## 15. Versione discorso continuo da imparare

"Il metodo di Lagrange serve a cercare estremi di una funzione quando i punti devono soddisfare un vincolo. Se voglio estremizzare $f$ sotto il vincolo $g=0$, l'idea geometrica e' che nel punto di estremo la curva di livello di $f$ e il vincolo sono tangenti. Poiche' i gradienti sono normali alle curve di livello, questa tangenza si traduce nel fatto che $\nabla f$ e $\nabla g$ sono paralleli. Quindi esiste un numero $\lambda$ tale che $\nabla f=\lambda\nabla g$, insieme al vincolo $g=0$. Risolvo il sistema, trovo i candidati e poi confronto i valori della funzione, ricordando che Lagrange non sostituisce la discussione dell'esistenza."

## 16. Versione lavagna

1. Scrivo problema:

$$
\text{estremizzare } f(x,y)\quad\text{soggetto a }g(x,y)=0.
$$

2. Disegno vincolo e livelli.
3. Scrivo:

$$
\nabla f=\lambda\nabla g,\qquad g=0.
$$

4. Risolvo un esempio.
5. Confronto i valori.

## 17. Possibili domande del professore

### 1. Perche' i gradienti sono paralleli?

Perche' le curve di livello sono tangenti e i gradienti sono normali.

### 2. Serve $\nabla g\ne0$?

Si', per avere un vincolo regolare.

### 3. Lagrange trova sempre massimo e minimo?

No, trova candidati regolari.

### 4. Cosa faccio dopo aver trovato i candidati?

Calcolo i valori di $f$ e li confronto.

### 5. E con due vincoli?

Uso $\nabla f=\lambda\nabla g+\mu\nabla h$ con entrambi i vincoli.

## 18. Mini-checklist finale

- So spiegare la tangenza.
- So scrivere il sistema.
- So dire l'ipotesi $\nabla g\ne0$.
- So fare un esempio.
- So confrontare i valori finali.

## 19. Controlli qualitativi

- Non dimenticare il vincolo nel sistema.
- Non scambiare candidati con estremi garantiti.
- Non usare il test libero senza adattarlo al vincolo.
