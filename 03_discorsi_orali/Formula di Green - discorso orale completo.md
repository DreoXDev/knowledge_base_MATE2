# Formula di Green - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare della formula di Green. L'idea centrale e' che una circuitazione lungo il bordo di un dominio piano puo' essere trasformata in un integrale doppio sul dominio stesso. In altre parole, invece di calcolare direttamente il lavoro del campo lungo una curva chiusa, posso sommare una quantita' locale interna: il rotore scalare $Q_x-P_y$.

Nel discorso voglio collegare quattro idee: integrale di linea di seconda specie, orientazione positiva della frontiera, rotore scalare piano e cancellazione dei bordi interni. Il punto delicato e' l'orientazione: il bordo deve essere percorso lasciando il dominio alla sinistra.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con idea di dimostrazione: 13 minuti
- Estensioni/domande su buchi, orientazione e Stokes: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei dall'idea: la formula di Green mette in relazione quello che succede sul bordo di un dominio piano con quello che succede dentro il dominio."

Considero un campo piano

$$
\vec F=(P,Q)
$$

e un dominio $D\subset\mathbb R^2$ con frontiera $C=\partial D$ orientata positivamente.

"orientata positivamente" significa che, mentre percorro il bordo, il dominio rimane alla mia sinistra.

La formula e':

$$
\oint_C P\,dx+Q\,dy
=
\iint_D \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\,dx\,dy.
$$

> "Il termine $Q_x-P_y$ e' il rotore scalare nel piano. Quindi Green dice che la circuitazione totale sul bordo e' la somma delle rotazioni locali interne."

## 2. Prerequisiti richiamati rapidamente

### [[integrali_linea_II_specie|Integrale di linea di seconda specie]]

Se $\gamma(t)=(x(t),y(t))$, allora:

$$
\int_\gamma P\,dx+Q\,dy
=
\int_a^b \big(P(\gamma(t))x'(t)+Q(\gamma(t))y'(t)\big)\,dt.
$$

**Possibile domanda del prof:** che cosa misura questo integrale?

**Risposta breve:** misura la circuitazione o il lavoro del campo lungo la curva orientata.

### [[integrali_multipli|Integrale doppio]]

Un integrale doppio somma una funzione su una regione piana:

$$
\iint_D f(x,y)\,dx\,dy.
$$

**Possibile domanda del prof:** perche' in Green compare un integrale doppio?

**Risposta breve:** perche' sto sommando nel dominio le rotazioni locali del campo.

### [[rotore|Rotore piano]]

Nel piano, per $\vec F=(P,Q)$, il rotore scalare e':

$$
Q_x-P_y.
$$

**Possibile domanda del prof:** perche' proprio $Q_x-P_y$?

**Risposta breve:** e' la componente lungo $z$ del rotore tridimensionale del campo $(P,Q,0)$.

### Orientazione positiva

La frontiera $C=\partial D$ e' orientata positivamente se il dominio resta alla sinistra mentre percorro $C$.

**Possibile domanda del prof:** se cambio verso al bordo?

**Risposta breve:** l'integrale di linea cambia segno, quindi anche la formula va letta con il verso corretto.

## 3. Enunciato formale

Sia $D$ un dominio piano regolare, con frontiera $C=\partial D$ regolare a tratti e orientata positivamente. Se $P,Q$ sono di classe $C^1$ in un aperto che contiene $D$, allora:

$$
\oint_C P\,dx+Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy.
$$

**Da dire a voce:** Green e' una formula bordo-interno: a sinistra ho una circuitazione, a destra ho un integrale doppio del rotore scalare.

## 4. Primo esempio da fare alla lavagna

Prendo il campo:

$$
\vec F=(-y,x)
$$

e il disco unitario $D=\{x^2+y^2\le 1\}$.

Qui:

$$
P=-y,\qquad Q=x,
$$

quindi:

$$
Q_x-P_y=1-(-1)=2.
$$

Per Green:

$$
\oint_{\partial D} -y\,dx+x\,dy
=
\iint_D2\,dx\,dy
=2\pi.
$$

### Cosa dire a voce

Questo esempio e' utile perche' evita una parametrizzazione diretta della circonferenza e mostra bene il significato geometrico: il campo gira intorno all'origine e la circuitazione totale e' proporzionale all'area.

## 5. Idea della dimostrazione

Per domini semplici si dimostrano due identita':

$$
\iint_D P_y\,dx\,dy=-\int_C P\,dx,
$$

e

$$
\iint_D Q_x\,dx\,dy=\int_C Q\,dy.
$$

Sommando:

$$
\int_C P\,dx+\int_C Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy.
$$

Per domini piu' generali si divide $D$ in pezzi semplici. I bordi interni vengono percorsi due volte in versi opposti e quindi si cancellano.

**Da dire a voce:** questa cancellazione dei bordi interni e' la vera immagine mentale del teorema.

## 6. Disegni da fare alla lavagna

### Disegno 1 - dominio orientato

Disegno un dominio $D$ e la sua frontiera $C$. Metto frecce antiorarie sul bordo esterno e scrivo:

$$
C=\partial D,\qquad D\text{ a sinistra}.
$$

### Disegno 2 - cancellazione dei bordi interni

Divido il dominio in due sottodomini. Sul bordo comune metto due frecce opposte e scrivo:

"i contributi interni si cancellano".

### Disegno 3 - dominio con buco

Disegno una corona circolare. Il bordo esterno e' antiorario, il bordo interno e' orario, per mantenere il dominio alla sinistra.

## Collegamenti utili nella KB

- [[formula_green]]
- [[integrali_linea_II_specie]]
- [[campi_conservativi]]
- [[irrotazionalita_forme_chiuse_esatte]]
- [[formula_stokes]]
- [[integrali_multipli]]

## Immagini / visualizzazioni utili

![[oral_green_orientazione_positiva.png]]

Questa figura serve per fissare l'orientazione positiva: il dominio resta alla sinistra.

![[oral_green_cancellazione_bordi.png]]

Questa immagine e' utile nella dimostrazione: i bordi interni si cancellano e rimane solo la frontiera esterna.

## 15. Versione discorso continuo da imparare

"La formula di Green e' un teorema che collega un integrale di linea lungo il bordo di un dominio piano con un integrale doppio sul dominio. Considero un campo piano $F=(P,Q)$ e un dominio regolare $D$ con bordo $C=\partial D$ orientato positivamente, cioe' in modo che il dominio resti alla sinistra. Allora la circuitazione di $F$ lungo $C$, cioe' l'integrale di $P\,dx+Q\,dy$, e' uguale all'integrale doppio su $D$ di $Q_x-P_y$. Il termine $Q_x-P_y$ e' il rotore scalare nel piano, quindi il significato geometrico e' che la circuitazione globale sul bordo e' la somma delle rotazioni locali interne. Nella dimostrazione, per domini semplici si usano il teorema fondamentale del calcolo e gli integrali iterati; per domini piu' generali si spezza il dominio in pezzi e i bordi interni si cancellano. L'attenzione principale e' l'orientazione: se cambio verso alla frontiera, cambia il segno dell'integrale."

## 16. Versione lavagna

1. Scrivo $F=(P,Q)$.
2. Disegno $D$ e $C=\partial D$.
3. Scrivo "orientazione positiva = dominio a sinistra".
4. Scrivo:

$$
\oint_C P\,dx+Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy.
$$

5. Disegno la cancellazione dei bordi interni.

## 17. Possibili domande del professore

### 1. Che cosa dice Green?

Trasforma una circuitazione sul bordo in un integrale doppio del rotore scalare.

### 2. Che cos'e' l'orientazione positiva?

Percorro il bordo lasciando il dominio alla sinistra.

### 3. Cosa succede se il dominio ha un buco?

Il bordo esterno e' orientato antiorariamente, quello interno orariamente, sempre per lasciare il dominio alla sinistra.

### 4. Perche' si cancellano i bordi interni?

Perche' ogni bordo interno viene percorso due volte in versi opposti.

### 5. Green e' collegato a Stokes?

Si', Green e' il caso piano della formula di Stokes.

## 18. Mini-checklist finale

- So enunciare la formula.
- So spiegare l'orientazione positiva.
- So dire che $Q_x-P_y$ e' il rotore scalare.
- So fare un esempio rapido.
- So spiegare la cancellazione dei bordi interni.

## 19. Controlli qualitativi

- Non confondere Green con Gauss.
- Non dimenticare il segno dell'orientazione.
- Non dire "antiorario" senza pensare ai buchi.
- Collegare sempre la formula al significato geometrico.
