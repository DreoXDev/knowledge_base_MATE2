# Error Log

## Errori ricorrenti negli esami batch 1

### Punti critici

- Non fermarsi a $\nabla f=0$: serve classificazione.
- Controllare punti degeneri se $D=0$.

### Lagrange

- Nei problemi su sfere, spesso il massimo/minimo e' nella direzione del gradiente della funzione lineare.
- Nei problemi con due vincoli, usare due moltiplicatori.

### Coordinate

- Primo ottante in sferiche: attenzione ai limiti angolari.
- Cilindro/paraboloide: usare coordinate cilindriche e jacobiano $\rho$.

### Green

- Controllare orientazione positiva.
- Se $Q_x-P_y$ e' costante, usare direttamente area.

### Campi conservativi

- I campi degli esami spesso sono gradienti costruiti da potenziali riconoscibili.
- Verificare sempre tutte le componenti di $\nabla U$.

### Possibile testo da verificare

- Esame 22/11/2022, esercizio 5: terza componente ricontrollata sul PDF sorgente tramite estrazione testuale; usare il potenziale registrato in `11_exams/by_year/2022_11_22.md`.

## Errori ricorrenti negli esami batch 2

### Metadati degli appelli

Alcuni file hanno nome e intestazione interna non coincidenti. Non cancellare questa informazione: conservarla nella scheda dell'esame.

### Funzioni lineari su sfera

Errore comune:
risolvere un sistema di Lagrange lungo quando basta riconoscere la direzione del vettore dei coefficienti.

### Green

Errore comune:
calcolare tutto il bordo quando $Q_x-P_y$ e' costante o nullo.

Corretto:
usare direttamente il lato doppio.

### Campi conservativi con parametri

Errore comune:
imporre solo una condizione di uguaglianza delle derivate miste e dimenticare le altre.

Corretto:
verificare tutte le componenti oppure riconoscere il potenziale e derivarlo.

### Coordinate sferiche

Errore comune:
dimenticare che, nella convenzione della lezione, il primo ottante ha:

$$
0\leq\theta\leq\frac{\pi}{2}
$$

se $\theta$ e' latitudine.

### Green su quarto di ellisse

Se $Q_x-P_y=0$, l'integrale e' nullo indipendentemente dalla forma precisa della regione, purche' il campo sia regolare e il bordo sia chiuso.

## Calcolo vettoriale finale

### Orientazione delle superfici

Errore comune:
calcolare un flusso senza controllare se $r_u\times r_v$ ha il verso della normale richiesta.

Corretto:
se $r_u\times r_v$ non e' concorde con $n$, cambiare segno.

### Integrale di superficie I specie vs II specie

Integrale di I specie:

$$
\int_Sf\,dS
$$

Integrale di II specie / flusso:

$$
\iint_SF\cdot n\,dS
$$

Il primo non dipende dall'orientazione; il secondo si'.

### Stokes: orientazione del bordo

Errore comune:
scegliere un verso arbitrario per $C$.

Corretto:
il verso di $C$ deve essere compatibile con la normale $n$.

### Gauss: normale uscente

Errore comune:
usare la normale entrante.

Corretto:
Gauss-Ostrogradski usa sempre la normale uscente.

### Guscio sferico

Nel guscio sferico, la normale uscente sulla sfera interna e' diretta verso il centro, quindi e':

$$
-\frac{r}{r}
$$

### Coordinate sferiche

La lezione usa $\theta$ come latitudine, quindi:

$$
dV=r^2\cos\theta\,dr\,d\varphi\,d\theta
$$

### Refusi / punti delicati

- Slide 5: controllare l'intervallo di $\theta$; usare la convenzione coerente $[-\pi/2,\pi/2]$.
- Slide 7: il cilindro sembra dover essere $x^2+y^2\leq a^2$.
- Slide 23: il secondo vettore tangente e' $r_y$, non un secondo $r_x$.
- Slide 35: parla di "dominio piano", ma descrive domini tridimensionali.
- Slide 45: per $F=(x^3,y^3,z^3)$, $\operatorname{div}F=3x^2+3y^2+3z^2$.

## Integrali multipli

### Dimenticare di disegnare il dominio

Errore comune:
invertire l'ordine di integrazione senza disegnare il dominio.

Corretto:
prima disegnare le curve e poi riscrivere i limiti.

### Non spezzare il dominio

Errore comune:
forzare una sola descrizione quando il dominio, invertendo l'ordine, richiede due intervalli.

Esempio:
la regione tra $y=1/x$, $y=x$ e $x=2$ va spezzata rispetto a $y$.

### Dimenticare il jacobiano

Errore comune:
passare a coordinate polari/cilindriche/sferiche senza moltiplicare per il jacobiano.

Corretto:

- polari: $dx\,dy=\rho\,d\rho\,d\theta$;
- cilindriche: $dx\,dy\,dz=\rho\,d\rho\,d\varphi\,dz$;
- sferiche della lezione: $dx\,dy\,dz=r^2\cos\theta\,dr\,d\varphi\,d\theta$.

### Confondere convenzioni sferiche

La lezione usa $\theta$ come latitudine:

$$
z=r\sin\theta
$$

e quindi il jacobiano e':

$$
r^2\cos\theta.
$$

Non confondere con la convenzione standard di molti libri.

### Integrazione per fili vs strati

- Fili: si integra lungo una variabile interna, fissata la proiezione.
- Strati: si integra sulle sezioni $S_z$ e poi rispetto a $z$.

### Refusi / controlli

- Slide 21: il rettangolo deve avere $c\leq y\leq d$.
- Ultima parte sulle coordinate sferiche: controllare la notazione di $\theta$ se compare $r^2\sin\theta$.

## Campi conservativi e Green

### Irrotazionalita' non sempre sufficiente

Errore comune: dire che se $P_y=Q_x$ allora il campo e' sempre conservativo.

Corretto: serve anche una condizione sul dominio, ad esempio semplice connessione.

### Campo angolare

Il campo:

$$
F=
\left(
-\frac{y}{x^2+y^2},
\frac{x}{x^2+y^2}
\right)
$$

e' irrotazionale su $\mathbb{R}^2\setminus\{0\}$ ma non e' conservativo su tutto il dominio, perche':

$$
\oint_C F\cdot\tau\,d\ell=2\pi
$$

sulla circonferenza unitaria orientata positivamente.

### Orientazione in Green

Errore comune: usare Green con orientazione sbagliata.

Corretto: la frontiera deve essere orientata in modo che il dominio resti a sinistra.

### Domini con buchi

Per domini con buchi, la frontiera esterna e' antioraria e le frontiere interne sono orarie.

### Refusi da segnalare

- Slide 24: nella riga dell'integrale di bordo dovrebbe comparire $dy$, non $dx$.
- Slide 35: in un esercizio piano compare un termine $F_3 dz/dt$, da ignorare come probabile residuo di template.
- Slide 29: l'ordine delle parametrizzazioni del quadrato va letto dalla parametrizzazione effettiva, non solo dall'elenco dei vertici.

## Integrali di linea di II specie

### Dimenticare l'orientazione

Errore comune: trattare l'integrale di II specie come se fosse indipendente dall'orientazione.

Corretto: se si inverte l'orientazione, l'integrale cambia segno.

### Confondere integrale di I e II specie

Integrale di I specie:

$$
\int_C f\,d\ell
$$

Integrale di II specie:

$$
\int_C F\cdot\tau\,d\ell
$$

oppure:

$$
\int_C F(r(t))\cdot r'(t)\,dt.
$$

### Dimenticare il prodotto scalare con $r'(t)$

Errore comune: sostituire solo $F(r(t))$ senza moltiplicare per $r'(t)$.

Corretto:

$$
\int_C F\cdot\tau\,d\ell
=
\int_a^b F(r(t))\cdot r'(t)\,dt
$$

per parametrizzazione concorde.

### Segno della parametrizzazione

Se la parametrizzazione e' discorde con l'orientazione della curva, bisogna cambiare segno.

### Campi conservativi

Errore comune: ricalcolare l'integrale lungo cammini diversi quando si ha gia' un potenziale.

Se $F=\nabla U$, allora:

$$
\int_C F\cdot\tau\,d\ell=U(P_1)-U(P_0).
$$

## Integrali di linea di I specie

### Dimenticare il fattore $\|r'(t)\|$

Errore comune:

$$
\int f(r(t))\,dt.
$$

Corretto:

$$
\int_C f\,d\ell
=
\int f(r(t))\|r'(t)\|\,dt.
$$

### Confondere $dt$ e $d\ell$

$d\ell$ e' l'elemento di lunghezza lungo la curva:

$$
d\ell=\|r'(t)\|dt.
$$

### Non restringere correttamente la funzione

Prima di integrare bisogna sostituire:

$$
x=x(t),\quad y=y(t),\quad z=z(t)
$$

nella funzione integranda.

### Caso $f=1$

Se $f=1$, l'integrale di linea restituisce la lunghezza della curva:

$$
\int_C 1\,d\ell=L.
$$

### Ellisse con $a=b$

Nell'esempio del quarto di ellisse, la formula finale:

$$
\frac{ab}{3}\frac{a^3-b^3}{a^2-b^2}
$$

richiede attenzione se $a=b$. In quel caso si considera il limite oppure si calcola separatamente.

## Massimi e minimi assoluti

### Non basta studiare l'interno

Errore comune: trovare solo i punti con $\nabla f=0$ e concludere.

Corretto: su domini chiusi e limitati bisogna studiare anche la frontiera e i vertici.

### Frontiera di segmenti

Errore comune: dimenticare gli estremi degli intervalli quando si studiano i lati.

Corretto: i vertici vanno sempre aggiunti ai candidati.

### Lagrange sulla frontiera

Errore comune: usare Lagrange sulla frontiera ma non confrontare i valori finali.

Corretto: Lagrange da' candidati, poi bisogna valutare $f$.

### Refuso slide 44

La slide sembra dire che il punto di massima distanza e' ancora $(1,1,-2)$, ma dai valori:

$$
f(1,1,-2)=4
$$

$$
f(-1,-1,2)=12
$$

il punto di massima distanza e':

$$
(-1,-1,2).
$$

## Funzione implicita

### Variabile da isolare

Errore comune: applicare il teorema per scrivere $y=f(x)$ anche quando $F_y=0$.

Corretto: per isolare $y$ serve $F_y\neq 0$.

### Circonferenza

Per $x^2+y^2=1$, non si puo' scrivere localmente $y=f(x)$ nei punti $(1,0)$ e $(-1,0)$ usando questo criterio, perche' $F_y=0$.

### Sfera

Per $x^2+y^2+z^2=1$, non si puo' scrivere localmente $z=f(x,y)$ sull'equatore usando questo criterio, perche' $F_z=0$.

## Moltiplicatori di Lagrange

### Nei problemi vincolati non si impone $\nabla f=0$

Errore comune:
trattare un problema vincolato come un problema libero.

Corretto:
si impone che la derivata di $f$ sia nulla solo lungo le direzioni tangenti al vincolo.

### Parallelismo dei gradienti

Errore comune:
dire che $\nabla f$ e $\nabla g$ sono ortogonali tra loro.

Corretto:
sono entrambi ortogonali al vincolo, quindi sono paralleli:

$$
\nabla f=\lambda\nabla g.
$$

### Dimenticare il vincolo

Errore comune:
risolvere solo $\nabla f=\lambda\nabla g$.

Corretto:
bisogna sempre aggiungere:

$$
g=c
$$

oppure tutti i vincoli presenti.

### Due vincoli

Errore comune:
usare un solo moltiplicatore per due vincoli.

Corretto:

$$
\nabla f=\lambda_1\nabla G_1+\lambda_2\nabla G_2.
$$

### Distanza al quadrato

Nei problemi di distanza si puo' minimizzare la distanza al quadrato perche' la radice e' crescente sui valori non negativi.

### Refusi da segnalare

- Slide 7: probabilmente "linearmente indipendenti" dovrebbe essere "linearmente dipendenti/paralleli".
- Slide 25: nello sviluppo di $F(s,t)$ per la distanza punto-piano il termine costante sembra essere $2$, non $3$.

## Superfici e piano tangente

### Confondere coordinate e parametrizzazione

Errore comune:
usare la stessa lettera $x$ senza distinguere tra coordinata e funzione vettoriale.

Corretto:
nelle note usare $\mathbf{x}(s,t)$ per la parametrizzazione e $x,y,z$ per le coordinate.

### Regolarita'

Errore comune:
dimenticare che per avere una superficie regolare i vettori $\mathbf{x}_s$ e $\mathbf{x}_t$ devono essere linearmente indipendenti.

Se sono dipendenti, non generano un piano tangente ben definito.

### Gradiente e superfici di livello

Errore comune:
dire che il gradiente e' tangente alla superficie di livello.

Corretto:
il gradiente e' ortogonale alla superficie di livello.

### Piano tangente parametrico vs cartesiano

Errore comune:
confondere la forma parametrica:

$$
\mathbf{x}=\bar{x}+s\mathbf{x}_u+t\mathbf{x}_v
$$

con la forma cartesiana:

$$
a(x-\bar{x})+b(y-\bar{y})+c(z-\bar{z})=0.
$$

### Prodotto vettoriale e orientazione

La slide cita la regola della mano sinistra. Verificare la convenzione nelle lezioni successive prima di usarla per orientazioni, flussi, Stokes e Gauss.

## Taylor, Hessiana, massimi e minimi

### Punto stazionario non significa estremo

Errore comune:
concludere che ogni punto stazionario sia massimo o minimo.

Corretto:
un punto stazionario puo' essere massimo, minimo, punto sella o caso degenerato.

### Applicare il test Hessiano fuori dai punti stazionari

Errore comune:
calcolare l'Hessiana in un punto qualsiasi e classificare direttamente.

Corretto:
prima si risolve $\nabla f=0$, poi si applica il test nei punti stazionari.

### Caso $D=0$

Errore comune:
classificare comunque il punto quando:

$$
D=f_{xx}f_{yy}-f_{xy}^2=0.
$$

Corretto:
il test e' inconclusivo. Bisogna usare altri metodi o termini di ordine superiore.

### Segno di $f_{xx}$

Errore comune:
se $D>0$, dimenticare di guardare il segno di $f_{xx}$.

Corretto:
- $D>0$, $f_{xx}>0$ implica minimo;
- $D>0$, $f_{xx}<0$ implica massimo.

### Piano tangente orizzontale

Errore comune:
dire che piano tangente orizzontale implica massimo/minimo.

Corretto:
e' condizione necessaria, non sufficiente.

## Funzioni di piu' variabili

### Esistenza delle derivate parziali non implica differenziabilita'

Errore comune:
pensare che se esistono tutte le derivate parziali allora la funzione e' automaticamente differenziabile.

Corretto:
la differenziabilita' implica esistenza delle derivate parziali, ma il converso non vale in generale. Un criterio sufficiente e' che le derivate parziali esistano in un intorno e siano continue nel punto.

### Piano tangente

Errore comune:
scrivere il piano tangente senza verificare la differenziabilita'.

Formula:

$$
z-f(P)=f_x(P)(x-\bar{x})+f_y(P)(y-\bar{y})
$$

### Curve di livello

Errore comune:
confondere il grafico della funzione con le curve di livello.

Il grafico di $f(x,y)$ e' una superficie in $\mathbb{R}^3$.

Le curve di livello sono curve nel piano ottenute da:

$$
f(x,y)=c.
$$

### Gradiente ortogonale

Errore comune:
dire che il gradiente e' tangente alle curve di livello.

Corretto:
il gradiente e' ortogonale alle curve di livello, perche' lungo una curva di livello la funzione e' costante e quindi:

$$
\nabla f(P)\cdot x'(t)=0.
$$

### Refusi da verificare nella Lezione 2

- Slide 7: la parte con $x,y,z$ riguarda funzioni di tre variabili, non di due.
- Slide 8: nel calcolo di $f_y$ il denominatore deve essere $\Delta y$.
- Slide 18: l'esempio del piano tangente contiene incongruenze tra funzione dichiarata e valori calcolati.

## Curve parametrizzate

### Parametrizzazione vs curva geometrica

Errore comune:
confondere il sostegno geometrico della curva con il modo in cui viene percorso.

Esempio:
$x(t)=t^3$, $y(t)=t^3$ ha sostegno sulla retta $y=x$, ma il vettore tangente non e' costante.

### Regolarita'

Errore comune:
dire che una parametrizzazione e' regolare solo perche' il sostegno geometrico e' una curva semplice.

Esempio:
$x(t)=t^2$, $y(t)=t^2$ non e' regolare in $t=0$ perche':

$$
\frac{dx}{dt}=2t,\qquad \frac{dy}{dt}=2t
$$

e quindi il vettore tangente si annulla.

### Elica e fattore $R$

Per:

$$
x(t)=R\cos t,\qquad y(t)=R\sin t,\qquad z(t)=ct
$$

il vettore tangente corretto e':

$$
(-R\sin t, R\cos t, c)
$$

e la norma e':

$$
\sqrt{R^2+c^2}
$$

## Registro generale

Registro degli errori ricorrenti durante esercizi, ripassi e simulazioni orali.

| Data | Argomento | Errore | Correzione | Da ripassare |
|---|---|---|---|---|
| | | | | |
