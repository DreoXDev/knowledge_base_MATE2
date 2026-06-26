# Formula di Gauss-Ostrogradski - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare della formula di Gauss-Ostrogradski, o teorema della divergenza. L'idea centrale e' che il flusso totale uscente da una superficie chiusa e' uguale alla somma delle sorgenti interne del campo, misurate tramite la divergenza.

Nel discorso voglio collegare superficie chiusa, normale uscente, flusso, divergenza e interpretazione fisica come bilancio tra interno e bordo.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con esempio: 13 minuti
- Estensioni/domande su superfici aperte, gusci e campi solenoidali: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei dall'idea di bilancio: se un campo ha sorgenti dentro un volume, allora attraverso la superficie che racchiude quel volume esce un flusso netto."

Prendo un volume $\Omega\subset\mathbb R^3$ e la sua frontiera $S=\partial\Omega$, orientata con normale uscente.

La formula e':

$$
\iint_{\partial\Omega}\vec F\cdot \vec n\,dS
=
\iiint_\Omega \operatorname{div}\vec F\,dV.
$$

> "A sinistra ho un integrale superficiale, cioe' il flusso attraverso il bordo. A destra ho un integrale triplo, cioe' la somma della divergenza dentro il volume."

## 2. Prerequisiti richiamati rapidamente

### [[flusso_integrali_superficie_II_specie|Flusso]]

Il flusso di un campo attraverso una superficie orientata e':

$$
\iint_S\vec F\cdot\vec n\,dS.
$$

**Possibile domanda del prof:** che cosa misura?

**Risposta breve:** misura quanto campo attraversa la superficie nel verso della normale scelta.

### [[divergenza|Divergenza]]

Per $\vec F=(P,Q,R)$:

$$
\operatorname{div}\vec F=P_x+Q_y+R_z.
$$

**Possibile domanda del prof:** che significato ha?

**Risposta breve:** misura localmente se il campo si comporta come sorgente o come pozzo.

### Superficie chiusa

Una superficie chiusa e' il bordo di un volume, quindi non ha bordo proprio:

$$
S=\partial\Omega.
$$

**Possibile domanda del prof:** posso applicare Gauss a una superficie aperta?

**Risposta breve:** no, prima devo chiuderla oppure aggiungere la parte mancante.

## 3. Enunciato formale

Sia $\Omega$ un dominio regolare di $\mathbb R^3$, con frontiera $\partial\Omega$ orientata dalla normale uscente. Se $\vec F$ e' regolare, allora:

$$
\iint_{\partial\Omega}\vec F\cdot\vec n\,dS
=
\iiint_\Omega \operatorname{div}\vec F\,dV.
$$

**Da dire a voce:** la normale uscente non e' una scelta decorativa: e' parte dell'enunciato.

## 4. Primo esempio da fare alla lavagna

Prendo:

$$
\vec F=(x,y,z)
$$

e $\Omega$ la sfera di raggio $R$.

Allora:

$$
\operatorname{div}\vec F=1+1+1=3.
$$

Quindi:

$$
\iint_{\partial\Omega}\vec F\cdot\vec n\,dS
=
\iiint_\Omega 3\,dV
=
3\cdot\frac{4}{3}\pi R^3
=
4\pi R^3.
$$

### Cosa dire a voce

Questo esempio mostra che spesso Gauss evita un calcolo diretto di superficie: basta integrare la divergenza sul volume.

## 5. Idea della dimostrazione

Si dimostra prima su domini semplici. Per la componente $P$:

$$
\iiint_\Omega P_x\,dV
=
\iint_{\partial\Omega}P n_x\,dS.
$$

Analogamente:

$$
\iiint_\Omega Q_y\,dV
=
\iint_{\partial\Omega}Q n_y\,dS,
$$

e

$$
\iiint_\Omega R_z\,dV
=
\iint_{\partial\Omega}R n_z\,dS.
$$

Sommando si ottiene:

$$
\iiint_\Omega(P_x+Q_y+R_z)\,dV
=
\iint_{\partial\Omega}(P n_x+Q n_y+R n_z)\,dS.
$$

Il membro di destra e' proprio $\iint_{\partial\Omega}\vec F\cdot\vec n\,dS$.

## 6. Disegni da fare alla lavagna

### Disegno 1 - volume e normale uscente

Disegno un solido $\Omega$ e frecce normali che puntano verso l'esterno. Scrivo:

$$
S=\partial\Omega,\qquad \vec n=\text{normale uscente}.
$$

### Disegno 2 - celle interne

Divido il volume in piccole celle e mostro che i flussi sulle facce interne si cancellano.

### Disegno 3 - guscio

Disegno una regione tra due sfere. La normale sulla sfera interna punta verso il centro, perche' deve uscire dal guscio.

## Collegamenti utili nella KB

- [[formula_gauss_ostrogradski]]
- [[divergenza]]
- [[flusso_integrali_superficie_II_specie]]
- [[campi_solenoidali]]
- [[formula_stokes]]
- [[green_stokes_gauss_collegamenti]]

## Immagini / visualizzazioni utili

![[oral_gauss_normale_uscente.png]]

Questa figura serve per ricordare che la normale e' uscente dal volume.

![[lezione_11_slide_42_normale_sfera.png]]

Utile per visualizzare la normale su una sfera e per evitare errori di verso.

## 15. Versione discorso continuo da imparare

"La formula di Gauss-Ostrogradski, o teorema della divergenza, collega il flusso di un campo attraverso una superficie chiusa con l'integrale della divergenza nel volume racchiuso. Considero un volume $\Omega$ e la sua frontiera $\partial\Omega$, orientata con normale uscente. Se il campo e' regolare, allora il flusso uscente di $F$ attraverso la frontiera e' uguale all'integrale triplo della divergenza di $F$ su $\Omega$. Il significato geometrico e fisico e' un bilancio: la divergenza misura le sorgenti e i pozzi locali, mentre il flusso misura quello che esce globalmente dal bordo. Se divido il volume in piccole celle, i flussi sulle facce interne si cancellano e rimane solo la superficie esterna."

## 16. Versione lavagna

1. Disegno $\Omega$.
2. Scrivo $S=\partial\Omega$.
3. Metto normali uscenti.
4. Scrivo:

$$
\iint_{\partial\Omega}\vec F\cdot\vec n\,dS
=
\iiint_\Omega\operatorname{div}\vec F\,dV.
$$

5. Aggiungo: $\operatorname{div}\vec F=P_x+Q_y+R_z$.

## 17. Possibili domande del professore

### 1. Che cosa dice Gauss?

Il flusso uscente da una superficie chiusa e' l'integrale della divergenza nel volume.

### 2. La superficie deve essere chiusa?

Si'. Se e' aperta, Gauss non si applica direttamente.

### 3. Quale normale si usa?

La normale uscente dal volume.

### 4. Che cosa significa divergenza nulla?

Che il campo non ha sorgenti o pozzi locali; si dice solenoidale.

### 5. Differenza con Stokes?

Gauss usa superficie chiusa e divergenza; Stokes usa superficie con bordo e rotore.

## 18. Mini-checklist finale

- So enunciare la formula.
- So spiegare normale uscente e superficie chiusa.
- So calcolare la divergenza.
- So fare l'esempio $F=(x,y,z)$.
- So distinguere Gauss da Stokes.

## 19. Controlli qualitativi

- Non applicare Gauss a superfici aperte.
- Non scegliere la normale arbitrariamente.
- Non confondere divergenza e rotore.
- Dire sempre "flusso uscente".
