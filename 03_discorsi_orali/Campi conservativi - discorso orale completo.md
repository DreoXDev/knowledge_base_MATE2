# Campi conservativi - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare dei campi vettoriali conservativi. L'idea centrale e' che un campo e' conservativo quando puo' essere scritto come gradiente di una funzione scalare, detta potenziale. Questa proprieta' e' importante perche' trasforma gli integrali di linea di seconda specie: il lavoro del campo lungo una curva non dipende dal cammino scelto, ma solo dagli estremi.

Nel discorso voglio quindi collegare cinque idee: definizione di potenziale, indipendenza dal cammino, integrale nullo sulle curve chiuse, condizioni necessarie di irrotazionalita' e ruolo del dominio. Alla fine il punto delicato e' questo: se un campo e' conservativo allora e' irrotazionale, ma il viceversa richiede ipotesi aggiuntive, per esempio un dominio semplicemente connesso.

## Tempo stimato

- Versione essenziale: 10 minuti
- Versione completa con costruzione del potenziale: 16 minuti
- Estensioni/domande su dominio, rotore e controesempi: 5 minuti

Totale realistico: 15-20 minuti.

## Discorso principale

> "Partirei dalla definizione: un campo vettoriale si dice conservativo se esiste una funzione scalare $U$, detta potenziale, tale che il campo sia il gradiente di $U$."

"F uguale gradiente di U"

$$
\vec F=\nabla U.
$$

> "Questa proprieta' ha una conseguenza fondamentale: l'integrale di linea di seconda specie dipende solo dagli estremi della curva."

"integrale lungo gamma di F scalare d r uguale differenza di potenziale"

$$
\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1).
$$

> "Quindi, se la curva e' chiusa, parto e arrivo nello stesso punto e l'integrale vale zero. Poi distinguo bene le condizioni: conservativo implica irrotazionale, ma il viceversa richiede ipotesi sul dominio."

## 2. Prerequisiti richiamati rapidamente

### [[campi_vettoriali|Campo vettoriale]]

Un campo vettoriale associa a ogni punto del dominio un vettore:

$$
\vec F:\Omega\subset\mathbb R^n\to\mathbb R^n.
$$

**Possibile domanda del prof:** che differenza c'e' tra una funzione scalare e un campo vettoriale?

**Risposta breve:** una funzione scalare restituisce un numero, mentre un campo vettoriale restituisce un vettore in ogni punto.

### [[gradiente_derivata_direzionale|Gradiente]]

Il gradiente di una funzione scalare $U$ e' il campo vettoriale delle derivate parziali:

$$
\nabla U=
\left(
\frac{\partial U}{\partial x_1},\dots,\frac{\partial U}{\partial x_n}
\right).
$$

**Possibile domanda del prof:** perche' compare il gradiente nella definizione di campo conservativo?

**Risposta breve:** perche' un campo conservativo e' precisamente un campo che nasce da una funzione scalare, cioe' e' il gradiente di un potenziale.

### [[calcolo_potenziale|Funzione potenziale]]

Una funzione potenziale e' una funzione scalare $U$ tale che:

$$
\vec F=\nabla U.
$$

**Possibile domanda del prof:** il potenziale e' unico?

**Risposta breve:** no, e' determinato a meno di una costante additiva.

### [[integrali_linea_II_specie|Integrale di linea di seconda specie]]

Se $\gamma:[a,b]\to\mathbb R^n$ e' una curva regolare, l'integrale di seconda specie e':

$$
\int_\gamma \vec F\cdot d\vec r
=
\int_a^b \vec F(\gamma(t))\cdot\gamma'(t)\,dt.
$$

**Possibile domanda del prof:** che cosa misura?

**Risposta breve:** nel linguaggio fisico misura il lavoro del campo lungo la curva.

### [[curve_parametrizzate|Curva parametrizzata]]

Una curva e' una funzione $\gamma:[a,b]\to\mathbb R^n$. Se $\gamma(a)=P_1$ e $\gamma(b)=P_2$, allora la curva congiunge $P_1$ a $P_2$.

**Possibile domanda del prof:** perche' serve parametrizzare la curva?

**Risposta breve:** per trasformare l'integrale lungo la curva in un integrale ordinario rispetto a $t$.

### [[intorni_aperti_chiusi|Dominio aperto]]

Un dominio e' aperto se ogni suo punto e' interno, cioe' se attorno a ogni punto esiste un piccolo intorno contenuto nel dominio.

**Possibile domanda del prof:** dove serve l'apertura del dominio?

**Risposta breve:** serve quando considero piccoli spostamenti orizzontali o verticali attorno a un punto, per restare dentro il dominio.

### [[dominio_connesso_per_archi|Dominio connesso per archi]]

Un dominio $D$ e' connesso per archi se, dati due punti $P_1,P_2\in D$, esiste una curva contenuta in $D$ che li congiunge.

**Possibile domanda del prof:** perche' serve questa ipotesi?

**Risposta breve:** per poter definire il potenziale fissando un punto $P_0$ e integrando da $P_0$ a qualunque altro punto del dominio.

### Curva chiusa

Una curva e' chiusa se il punto iniziale coincide con il punto finale:

$$
\gamma(a)=\gamma(b).
$$

**Possibile domanda del prof:** che succede all'integrale di un campo conservativo su una curva chiusa?

**Risposta breve:** vale zero, perche' la differenza di potenziale tra punto finale e punto iniziale e' nulla.

### Teorema fondamentale del calcolo integrale

Se $g$ e' derivabile, allora:

$$
\int_a^b g'(t)\,dt=g(b)-g(a).
$$

**Possibile domanda del prof:** dove lo usi?

**Risposta breve:** nella dimostrazione di $\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1)$, applicandolo a $g(t)=U(\gamma(t))$.

### Regola di derivazione della funzione composta

Se $U$ e' derivabile e $\gamma(t)$ e' una curva, allora:

$$
\frac{d}{dt}U(\gamma(t))=\nabla U(\gamma(t))\cdot\gamma'(t).
$$

**Possibile domanda del prof:** qual e' il passaggio chiave della dimostrazione?

**Risposta breve:** riconoscere l'integranda come derivata della funzione composta $U(\gamma(t))$.

### [[scambio_derivate_parziali|Teorema di Schwarz]]

Se $U$ e' sufficientemente regolare, allora le derivate seconde miste coincidono:

$$
U_{x_i x_j}=U_{x_j x_i}.
$$

**Possibile domanda del prof:** dove entra nei campi conservativi?

**Risposta breve:** permette di dedurre le condizioni di irrotazionalita' dalle uguaglianze $F_i=U_{x_i}$.

### [[rotore|Rotore]]

In $\mathbb R^3$ il rotore misura la rotazione locale di un campo:

$$
\nabla\times \vec F.
$$

Nel piano la condizione corrispondente e':

$$
\frac{\partial F_1}{\partial y}=\frac{\partial F_2}{\partial x}.
$$

**Possibile domanda del prof:** rotore nullo basta sempre?

**Risposta breve:** no, e' sempre necessario; diventa sufficiente con ipotesi sul dominio, per esempio semplice connessione.

### [[domini_semplicemente_connessi|Dominio semplicemente connesso]]

Intuitivamente, un dominio semplicemente connesso non ha buchi che impediscono di contrarre le curve chiuse a un punto.

**Possibile domanda del prof:** perche' e' importante?

**Risposta breve:** perche' in un dominio semplicemente connesso l'irrotazionalita' puo' diventare condizione sufficiente per l'esistenza di un potenziale.

## 3. Definizione di campo conservativo

Sia

$$
\vec F =
F_1(x_1,\dots,x_n)\vec e_1+\dots+
F_n(x_1,\dots,x_n)\vec e_n.
$$

Il campo $\vec F$ si dice conservativo se esiste una funzione scalare $U$, detta funzione potenziale, tale che:

$$
\vec F=\nabla U.
$$

In componenti:

$$
F_i=\frac{\partial U}{\partial x_i}
$$

per ogni $i=1,\dots,n$.

Il campo vettoriale $\vec F$ e' un oggetto vettoriale; il potenziale $U$ e' una funzione scalare. Inoltre, se $U$ e' un potenziale, anche $U+c$ e' un potenziale, per ogni costante $c$.

**Da dire a voce:** in pratica, un campo conservativo e' un campo che non e' arbitrario, ma nasce come gradiente di una funzione scalare.

## 4. Primo esempio da fare alla lavagna

Considero il campo:

$$
\vec F(x,y)=(3x^2y,x^3+1).
$$

Cerco $U$ tale che:

$$
U_x=3x^2y,\qquad U_y=x^3+1.
$$

Un potenziale e':

$$
U(x,y)=x^3y+y+c.
$$

Infatti:

$$
\frac{\partial U}{\partial x}=3x^2y
$$

e

$$
\frac{\partial U}{\partial y}=x^3+1.
$$

Quindi $\vec F$ e' conservativo.

### Cosa scrivere alla lavagna

```text
F = (3x^2 y, x^3 + 1)

Cerco U tale che:
U_x = 3x^2 y
U_y = x^3 + 1

U(x,y) = x^3 y + y + c
```

### Cosa dire a voce

Questo esempio serve a fissare l'idea: se riesco a trovare una funzione $U$ le cui derivate parziali coincidono con le componenti del campo, allora il campo e' conservativo.

## 5. Teorema: campo conservativo implica indipendenza dal cammino

Sia $\vec F$ un campo conservativo e sia $\gamma$ una curva che congiunge $P_1$ e $P_2$. Se $\vec F=\nabla U$, allora:

$$
\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1).
$$

Quindi:

- l'integrale di linea dipende solo dagli estremi;
- non dipende dalla curva scelta;
- se la curva e' chiusa, l'integrale vale zero.

## 6. Dimostrazione del teorema

Sia:

$$
\gamma:[a,b]\to\mathbb R^n
$$

con:

$$
\gamma(t)=(x_1(t),\dots,x_n(t))
$$

e:

$$
\gamma(a)=P_1,\qquad \gamma(b)=P_2.
$$

Per definizione di integrale di linea di seconda specie:

$$
\int_\gamma \vec F\cdot d\vec r
=
\int_a^b \vec F(\gamma(t))\cdot \gamma'(t)\,dt.
$$

Poiche' $\vec F=\nabla U$:

$$
\int_a^b \vec F(\gamma(t))\cdot \gamma'(t)\,dt
=
\int_a^b \nabla U(\gamma(t))\cdot \gamma'(t)\,dt.
$$

Espandendo:

$$
\int_a^b
\left(
\frac{\partial U}{\partial x_1}\frac{dx_1}{dt}
+
\dots
+
\frac{\partial U}{\partial x_n}\frac{dx_n}{dt}
\right)dt.
$$

Per la regola della derivata della funzione composta:

$$
\frac{d}{dt}U(\gamma(t))
=
\nabla U(\gamma(t))\cdot \gamma'(t).
$$

Quindi:

$$
\int_\gamma \vec F\cdot d\vec r
=
\int_a^b \frac{d}{dt}U(\gamma(t))\,dt
=
U(\gamma(b))-U(\gamma(a)).
$$

Cioe':

$$
\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1).
$$

### Cosa dire a voce

Il passaggio fondamentale e' riconoscere nell'integranda la derivata della funzione composta $U(\gamma(t))$.

### Possibile domanda del prof

**Domanda:** quale teorema stai usando nel passaggio finale?

**Risposta:** il teorema fondamentale del calcolo integrale, applicato alla derivata rispetto a $t$ della funzione composta $U(\gamma(t))$.

## 7. Conseguenza: integrale su curve chiuse

Se $\gamma$ e' chiusa, allora $P_1=P_2$, quindi:

$$
\oint_\gamma \vec F\cdot d\vec r
=
U(P_1)-U(P_1)=0.
$$

Posso anche spiegarlo con il disegno degli appunti. Considero una curva chiusa come unione di due curve: una curva $\gamma_1$ e la curva $-\gamma_2$, dove $\gamma_2$ ha gli stessi estremi di $\gamma_1$ ma viene percorsa in verso opposto. Cambiando verso a una curva cambia il segno dell'integrale. Siccome in un campo conservativo gli integrali sui due cammini con gli stessi estremi sono uguali, la somma e' zero.

```text
gamma = gamma_1 unione (-gamma_2)

int_gamma F . dr
= int_gamma1 F . dr + int_-gamma2 F . dr
= int_gamma1 F . dr - int_gamma2 F . dr
= 0
```

## Moduli aggiuntivi se il prof lascia continuare

### Modulo A - Teorema inverso: indipendenza dal cammino implica campo conservativo

Sia

$$
\vec F=F_1(x,y)\vec e_1+F_2(x,y)\vec e_2
$$

un campo vettoriale continuo definito su un dominio $D$ aperto e connesso per archi.

Se l'integrale di linea di seconda specie e' indipendente dal cammino, allora $\vec F$ e' conservativo.

La costruzione e' questa:

- si fissa un punto $P_0\in D$;
- per ogni punto $P\in D$ si definisce

$$
U(P)=\int_\gamma \vec F\cdot d\vec\ell,
$$

dove $\gamma$ e' una qualunque curva contenuta in $D$ che congiunge $P_0$ a $P$;

- la definizione e' ben posta perche' l'integrale e' indipendente dal cammino.

## 9. Dimostrazione della costruzione del potenziale

### Obiettivo

Voglio mostrare che:

$$
\frac{\partial U}{\partial x}=F_1
$$

e:

$$
\frac{\partial U}{\partial y}=F_2.
$$

Allora:

$$
\nabla U=(F_1,F_2)=\vec F.
$$

### Derivata rispetto a $x$

Fisso:

$$
P=(x,y)
$$

e considero:

$$
P'=(x+\Delta x,y).
$$

Per indipendenza dal cammino, posso scegliere la curva da $P_0$ a $P'$ come curva composta da:

1. una curva da $P_0$ a $P$;
2. il segmento orizzontale da $P$ a $P'$.

Allora:

$$
U(x+\Delta x,y)-U(x,y)
=
\int_{\gamma_2}\vec F\cdot d\vec\ell,
$$

dove $\gamma_2$ e' il segmento orizzontale.

Parametrizzo:

$$
x(t)=x+t\Delta x,\qquad y(t)=y,\qquad t\in[0,1].
$$

Quindi:

$$
\frac{dx}{dt}=\Delta x,\qquad \frac{dy}{dt}=0.
$$

L'integrale diventa:

$$
\int_{\gamma_2}\vec F\cdot d\vec\ell
=
\int_0^1
\left[
F_1(x+t\Delta x,y)\Delta x+
F_2(x+t\Delta x,y)\cdot 0
\right]dt.
$$

Cioe':

$$
\int_{\gamma_2}\vec F\cdot d\vec\ell
=
\Delta x\int_0^1F_1(x+t\Delta x,y)\,dt.
$$

Per il teorema della media integrale, esiste $\bar t\in[0,1]$ tale che:

$$
\int_0^1F_1(x+t\Delta x,y)\,dt
=
F_1(x+\bar t\Delta x,y).
$$

Quindi:

$$
\frac{U(x+\Delta x,y)-U(x,y)}{\Delta x}
=
F_1(x+\bar t\Delta x,y).
$$

Passando al limite per $\Delta x\to 0$, usando la continuita' di $F_1$:

$$
\frac{\partial U}{\partial x}(x,y)=F_1(x,y).
$$

### Derivata rispetto a $y$

Il ragionamento e' analogo. Considero:

$$
P''=(x,y+\Delta y)
$$

e il segmento verticale:

$$
x(t)=x,\qquad y(t)=y+t\Delta y.
$$

Allora:

$$
\frac{dx}{dt}=0,\qquad \frac{dy}{dt}=\Delta y.
$$

Quindi:

$$
U(x,y+\Delta y)-U(x,y)
=
\Delta y\int_0^1F_2(x,y+t\Delta y)\,dt.
$$

Applicando ancora il teorema della media integrale e poi passando al limite:

$$
\frac{\partial U}{\partial y}(x,y)=F_2(x,y).
$$

### Conclusione

Abbiamo ottenuto:

$$
\nabla U=(F_1,F_2)=\vec F.
$$

Quindi $\vec F$ e' conservativo.

### Dove entrano le ipotesi

- Il dominio connesso per archi serve per poter collegare $P_0$ a ogni punto $P$.
- L'indipendenza dal cammino serve per rendere ben definita $U(P)$.
- L'apertura del dominio serve per poter fare piccoli spostamenti da $P$ a $P'$ restando in $D$.
- La continuita' di $\vec F$ serve nel passaggio al limite.
- Il teorema della media integrale serve per trasformare l'integrale medio nel valore del campo in un punto intermedio.

## 10. Disegni da fare alla lavagna

### Disegno 1 - campo conservativo e potenziale

Disegnare:

- un dominio $D$;
- due punti $P_1$ e $P_2$;
- due curve diverse $\gamma_1$ e $\gamma_2$ che li collegano.

Scrivere:

$$
\int_{\gamma_1}\vec F\cdot d\vec r
=
\int_{\gamma_2}\vec F\cdot d\vec r.
$$

### Disegno 2 - curva chiusa

Disegnare:

- una curva chiusa;
- la divisione ideale in $\gamma_1$ e $-\gamma_2$;
- le frecce dei versi di percorrenza.

Scrivere:

$$
\oint_\gamma \vec F\cdot d\vec r=0.
$$

### Disegno 3 - costruzione del potenziale

Disegnare:

- il dominio $D$;
- il punto fissato $P_0$;
- il punto variabile $P=(x,y)$;
- il punto vicino $P'=(x+\Delta x,y)$;
- una curva qualsiasi da $P_0$ a $P$;
- un segmentino orizzontale da $P$ a $P'$.

Scrivere:

$$
U(P)=\int_{P_0}^{P}\vec F\cdot d\vec\ell
$$

e:

$$
U(P')-U(P)=\int_P^{P'}\vec F\cdot d\vec\ell.
$$

### Disegno 4 - segmento orizzontale

Disegnare solo il segmento da $(x,y)$ a $(x+\Delta x,y)$.

Scrivere:

$$
x(t)=x+t\Delta x,\qquad y(t)=y.
$$

## 11. Condizioni necessarie di irrotazionalita'

Se $\vec F$ e' conservativo, allora esiste $U$ tale che:

$$
F_i=\frac{\partial U}{\partial x_i}.
$$

Percio':

$$
\frac{\partial F_i}{\partial x_j}
=
U_{x_i x_j}
$$

e:

$$
\frac{\partial F_j}{\partial x_i}
=
U_{x_j x_i}.
$$

Per il teorema di Schwarz:

$$
U_{x_i x_j}=U_{x_j x_i}.
$$

Quindi:

$$
\frac{\partial F_i}{\partial x_j}
=
\frac{\partial F_j}{\partial x_i},
\qquad i\neq j.
$$

Queste sono condizioni necessarie: se il campo e' conservativo, allora e' irrotazionale.

## 12. Caso piano e caso tridimensionale

### Caso $n=2$

Se:

$$
\vec F(x,y)=F_1(x,y)\vec e_1+F_2(x,y)\vec e_2,
$$

allora:

$$
\frac{\partial F_1}{\partial y}
=
\frac{\partial F_2}{\partial x}.
$$

### Caso $n=3$

Se:

$$
\vec F(x,y,z)=F_1\vec e_1+F_2\vec e_2+F_3\vec e_3,
$$

allora:

$$
\frac{\partial F_1}{\partial y}
=
\frac{\partial F_2}{\partial x},
$$

$$
\frac{\partial F_1}{\partial z}
=
\frac{\partial F_3}{\partial x},
$$

$$
\frac{\partial F_2}{\partial z}
=
\frac{\partial F_3}{\partial y}.
$$

Equivalentemente:

$$
\nabla\times\vec F=\vec 0.
$$

## 13. Attenzione: necessarie ma non sempre sufficienti

Vale sempre:

$$
\vec F \text{ conservativo}
\Rightarrow
\vec F \text{ irrotazionale}.
$$

In generale pero' non sempre vale il viceversa. Per poter concludere che un campo irrotazionale e' conservativo servono ipotesi aggiuntive sul dominio, tipicamente che il dominio sia semplicemente connesso.

**Da dire a voce:** quindi l'annullarsi del rotore e' una condizione necessaria. Diventa anche sufficiente sotto opportune ipotesi sul dominio, tipicamente se il dominio e' semplicemente connesso.

Collegamenti utili:

- [[domini_semplicemente_connessi|Dominio semplicemente connesso]]
- [[rotore|Rotore]]
- [[formula_green|Teorema di Green]]

## Collegamenti utili nella KB

- [[integrali_linea_II_specie|Integrali di linea di seconda specie]]: sono l'ambiente naturale in cui si parla di lavoro e indipendenza dal cammino.
- [[campi_vettoriali|Campi vettoriali]]: un campo conservativo e' un caso particolare di campo vettoriale.
- [[gradiente_derivata_direzionale|Gradiente]]: la definizione e' $\vec F=\nabla U$.
- [[calcolo_potenziale|Potenziale]]: serve per costruire concretamente la funzione $U$ a partire dalle componenti del campo.
- [[forme_differenziali|Forme differenziali]]: collega la scrittura $P\,dx+Q\,dy$ alla nozione di forma esatta.
- [[indipendenza_cammino|Indipendenza dal cammino]]: e' la proprieta' equivalente piu' importante per gli integrali di linea.
- [[circuitazione|Curve chiuse e circuitazione]]: spiega perche' sui cammini chiusi l'integrale di un campo conservativo vale zero.
- [[irrotazionalita_forme_chiuse_esatte|Condizioni di irrotazionalita']] : chiarisce il passaggio da forma esatta a forma chiusa.
- [[rotore|Rotore]]: rotore nullo e' la condizione locale di irrotazionalita'.
- [[formula_green|Teorema di Green]]: collega l'integrale lungo una curva chiusa con un integrale doppio del rotore scalare nel piano.
- [[curve_parametrizzate|Curve regolari]]: servono per definire gli integrali di linea.
- [[intorni_aperti_chiusi|Dominio aperto]]: serve nelle dimostrazioni locali con piccoli segmenti.
- [[dominio_connesso_per_archi|Dominio connesso per archi]]: serve per collegare il punto fissato $P_0$ a ogni punto del dominio.
- [[domini_semplicemente_connessi|Dominio semplicemente connesso]]: serve per passare da irrotazionale a conservativo.
- [[scambio_derivate_parziali|Teorema di Schwarz]]: giustifica l'uguaglianza delle derivate incrociate.
- [[teorema_fondamentale_calcolo_integrale|Teorema fondamentale del calcolo integrale]]: chiude la dimostrazione trasformando l'integrale di una derivata in una differenza di valori.
- [[derivazione_funzione_composta|Derivazione della funzione composta]]: spiega il passaggio $\frac{d}{dt}U(\gamma(t))=\nabla U(\gamma(t))\cdot\gamma'(t)$.

## 15. Versione discorso continuo da imparare

### 15.1 Introduzione

Vorrei parlare dei campi conservativi. Un campo vettoriale e' conservativo quando puo' essere scritto come gradiente di una funzione scalare, detta potenziale. Questa definizione e' importante perche' ha una conseguenza molto forte sugli integrali di linea di seconda specie: il lavoro del campo lungo una curva dipende solo dal punto iniziale e dal punto finale, non dal percorso scelto.

### 15.2 Definizione

Formalmente, se ho un campo

$$
\vec F=F_1\vec e_1+\dots+F_n\vec e_n,
$$

dico che e' conservativo se esiste $U$ tale che:

$$
\vec F=\nabla U.
$$

Questo significa che ogni componente del campo e' una derivata parziale del potenziale:

$$
F_i=U_{x_i}.
$$

Il potenziale e' una funzione scalare e non e' unico: posso sempre aggiungere una costante.

### 15.3 Esempio semplice

Per fissare l'idea posso fare l'esempio:

$$
\vec F(x,y)=(3x^2y,x^3+1).
$$

Cerco $U$ con $U_x=3x^2y$ e $U_y=x^3+1$. Un potenziale e':

$$
U(x,y)=x^3y+y+c.
$$

Infatti derivando rispetto a $x$ ottengo $3x^2y$, e derivando rispetto a $y$ ottengo $x^3+1$. Quindi questo campo e' conservativo.

### 15.4 Conservativo implica indipendenza dal cammino

Il teorema fondamentale dice che, se $\vec F=\nabla U$ e $\gamma$ e' una curva da $P_1$ a $P_2$, allora:

$$
\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1).
$$

Quindi non conta quale curva ho scelto: conta solo la differenza di potenziale tra il punto finale e il punto iniziale.

### 15.5 Dimostrazione

Parametrizzo la curva con $\gamma(t)$, per $t\in[a,b]$. Per definizione:

$$
\int_\gamma \vec F\cdot d\vec r
=
\int_a^b \vec F(\gamma(t))\cdot\gamma'(t)\,dt.
$$

Se $\vec F=\nabla U$, questo diventa:

$$
\int_a^b \nabla U(\gamma(t))\cdot\gamma'(t)\,dt.
$$

Ma per la regola della funzione composta:

$$
\nabla U(\gamma(t))\cdot\gamma'(t)
=
\frac{d}{dt}U(\gamma(t)).
$$

Quindi l'integrale e':

$$
\int_a^b \frac{d}{dt}U(\gamma(t))\,dt.
$$

Per il teorema fondamentale del calcolo integrale ottengo:

$$
U(\gamma(b))-U(\gamma(a))=U(P_2)-U(P_1).
$$

### 15.6 Curve chiuse

A questo punto posso osservare una conseguenza importante. Se il campo e' conservativo, allora l'integrale lungo una curva chiusa e' nullo. Infatti una curva chiusa parte e arriva nello stesso punto, quindi applicando la formula precedente ottengo:

$$
U(P)-U(P)=0.
$$

In modo equivalente, posso pensare una curva chiusa come una curva $\gamma_1$ piu' la curva $-\gamma_2$. Le due curve hanno gli stessi estremi, quindi gli integrali sono uguali; ma una delle due e' percorsa in verso opposto, quindi entra con il segno meno. La somma e' zero.

### 15.7 Teorema inverso

Esiste anche un risultato inverso. Se ho un campo continuo in un dominio aperto e connesso per archi, e l'integrale di linea e' indipendente dal cammino, allora posso costruire un potenziale.

Fisso un punto $P_0$ e definisco:

$$
U(P)=\int_{P_0}^{P}\vec F\cdot d\vec\ell.
$$

Questa definizione e' ben posta perche' per ipotesi l'integrale non dipende dalla curva scelta, ma solo dagli estremi.

### 15.8 Costruzione del potenziale

Per dimostrare che questa $U$ e' davvero un potenziale, devo mostrare che $U_x=F_1$ e $U_y=F_2$.

Fisso $P=(x,y)$ e considero $P'=(x+\Delta x,y)$. Per indipendenza dal cammino posso andare da $P_0$ a $P'$ passando prima da $P$ e poi lungo il segmentino orizzontale da $P$ a $P'$. Allora la differenza:

$$
U(x+\Delta x,y)-U(x,y)
$$

e' l'integrale del campo su quel segmento orizzontale.

Parametrizzo il segmento con:

$$
x(t)=x+t\Delta x,\qquad y(t)=y.
$$

Allora $dx/dt=\Delta x$ e $dy/dt=0$, quindi:

$$
U(x+\Delta x,y)-U(x,y)
=
\Delta x\int_0^1F_1(x+t\Delta x,y)\,dt.
$$

Divido per $\Delta x$ e, usando il teorema della media integrale e la continuita' di $F_1$, passando al limite ottengo:

$$
U_x(x,y)=F_1(x,y).
$$

Allo stesso modo, usando un segmento verticale, ottengo:

$$
U_y(x,y)=F_2(x,y).
$$

Quindi $\nabla U=\vec F$, e il campo e' conservativo.

### 15.9 Condizioni di irrotazionalita'

Se un campo e' conservativo, allora $\vec F=\nabla U$. In componenti $F_i=U_{x_i}$. Se derivo $F_i$ rispetto a $x_j$ ottengo $U_{x_i x_j}$, mentre se derivo $F_j$ rispetto a $x_i$ ottengo $U_{x_j x_i}$. Per il teorema di Schwarz queste derivate coincidono, quindi:

$$
\frac{\partial F_i}{\partial x_j}
=
\frac{\partial F_j}{\partial x_i}.
$$

Nel piano questa condizione diventa:

$$
F_{1,y}=F_{2,x}.
$$

Nello spazio equivale a:

$$
\nabla\times\vec F=\vec 0.
$$

### 15.10 Attenzione al dominio

La cosa da non sbagliare e' che queste condizioni sono necessarie ma non sempre sufficienti. Il rotore nullo dice che il campo e' localmente compatibile con un potenziale, ma per avere un potenziale globale devo guardare il dominio.

Se il dominio ha buchi, puo' succedere che un campo sia irrotazionale ma non conservativo. Il controesempio classico e' il campo angolare su $\mathbb R^2\setminus\{0\}$: il rotore e' nullo fuori dall'origine, ma l'integrale su una circonferenza attorno all'origine non e' zero.

### 15.11 Conclusione

Quindi la catena logica da ricordare e': campo conservativo significa esistenza del potenziale; il potenziale implica indipendenza dal cammino; su curve chiuse l'integrale e' nullo; da conservativo segue irrotazionale; e, con ipotesi sul dominio come la semplice connessione, l'irrotazionalita' puo' diventare anche sufficiente.

## 16. Versione lavagna

### Schema lavagna

1. Definizione

$$
\vec F \text{ conservativo}
\iff
\exists U:\vec F=\nabla U.
$$

2. Componenti

$$
F_i=\frac{\partial U}{\partial x_i}.
$$

3. Esempio

$$
\vec F=(3x^2y,x^3+1),\qquad
U=x^3y+y+c.
$$

4. Teorema

$$
\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1).
$$

5. Dimostrazione compatta

$$
\int_\gamma \vec F\cdot d\vec r
=
\int_a^b \nabla U(\gamma(t))\cdot\gamma'(t)\,dt
=
\int_a^b \frac{d}{dt}U(\gamma(t))\,dt
=
U(P_2)-U(P_1).
$$

6. Curva chiusa

$$
\gamma \text{ chiusa}
\Rightarrow
\oint_\gamma \vec F\cdot d\vec r=0.
$$

7. Teorema inverso

$$
U(P)=\int_{P_0}^{P}\vec F\cdot d\vec\ell.
$$

8. Derivata rispetto a $x$

$$
U(x+\Delta x,y)-U(x,y)
=
\Delta x\int_0^1F_1(x+t\Delta x,y)\,dt.
$$

$$
U_x(x,y)=F_1(x,y).
$$

9. Derivata rispetto a $y$

$$
U_y(x,y)=F_2(x,y).
$$

10. Irrotazionalita'

$$
\frac{\partial F_i}{\partial x_j}
=
\frac{\partial F_j}{\partial x_i}.
$$

Nel piano:

$$
F_{1,y}=F_{2,x}.
$$

Nello spazio:

$$
\nabla\times\vec F=\vec 0.
$$

11. Attenzione finale

```text
Conservativo => irrotazionale.
Irrotazionale => conservativo solo con ipotesi sul dominio.
```

## 17. Possibili domande del professore

### 1. Che cosa significa che un campo e' conservativo?

Significa che esiste una funzione scalare $U$ tale che $\vec F=\nabla U$.

### 2. Perche' $U$ si chiama potenziale?

Perche' il lavoro del campo si calcola come differenza dei valori di $U$ agli estremi, cioe' come differenza di potenziale.

### 3. Il potenziale e' unico?

No. E' unico a meno di una costante additiva.

### 4. Che cosa significa che l'integrale e' indipendente dal cammino?

Significa che, fissati punto iniziale e punto finale, l'integrale ha lo stesso valore per tutte le curve ammissibili che li collegano.

### 5. Perche' se il campo e' conservativo l'integrale lungo una curva chiusa e' nullo?

Perche' punto iniziale e punto finale coincidono, quindi $U(P)-U(P)=0$.

### 6. Il viceversa e' vero?

Se l'integrale e' indipendente dal cammino, allora posso costruire un potenziale. Se invece so solo che il rotore e' nullo, il viceversa richiede ipotesi sul dominio.

### 7. Qual e' il ruolo del dominio?

Il dominio decide se una condizione locale, come rotore nullo, puo' diventare globale, cioe' esistenza di un potenziale su tutto il dominio.

### 8. Perche' serve che il dominio sia connesso per archi?

Perche' devo poter collegare il punto fissato $P_0$ a ogni punto $P$ con una curva contenuta nel dominio.

### 9. Perche' nella costruzione del potenziale si fissa un punto $P_0$?

Per avere un riferimento da cui misurare il valore del potenziale tramite l'integrale del campo.

### 10. Perche' la definizione di $U(P)$ e' ben posta?

Perche' l'integrale e' indipendente dal cammino, quindi qualunque curva da $P_0$ a $P$ da' lo stesso valore.

### 11. Dove si usa la continuita' del campo nella dimostrazione?

Nel passaggio al limite del rapporto incrementale, per ottenere $F_1(x,y)$ e $F_2(x,y)$.

### 12. Dove si usa il teorema della media integrale?

Quando trasformo l'integrale medio di $F_1$ o $F_2$ lungo il segmentino nel valore della funzione in un punto intermedio.

### 13. Dove si usa la regola della funzione composta?

Nella dimostrazione di conservativo implica indipendenza dal cammino, per riconoscere:

$$
\nabla U(\gamma(t))\cdot\gamma'(t)
=
\frac{d}{dt}U(\gamma(t)).
$$

### 14. Cosa sono le condizioni di irrotazionalita'?

Sono le uguaglianze tra derivate incrociate delle componenti del campo:

$$
\frac{\partial F_i}{\partial x_j}
=
\frac{\partial F_j}{\partial x_i}.
$$

### 15. In $\mathbb R^2$ qual e' la condizione?

Se $\vec F=(F_1,F_2)$, allora:

$$
\frac{\partial F_1}{\partial y}
=
\frac{\partial F_2}{\partial x}.
$$

### 16. In $\mathbb R^3$ qual e' la condizione?

Che il rotore sia nullo:

$$
\nabla\times\vec F=\vec 0.
$$

### 17. Rotore nullo implica sempre campo conservativo?

No. Serve anche controllare il dominio. In un dominio semplicemente connesso, sotto regolarita' adeguata, il rotore nullo e' sufficiente.

### 18. Cosa cambia se il dominio ha un buco?

Puo' esistere una circuitazione non nulla attorno al buco, quindi il campo puo' essere irrotazionale ma non conservativo globalmente.

### 19. Puoi fare un esempio di campo conservativo?

Si':

$$
\vec F=(3x^2y,x^3+1)
$$

ha potenziale:

$$
U=x^3y+y+c.
$$

### 20. Puoi spiegare il legame con il lavoro di una forza?

Se $\vec F$ e' una forza conservativa, il lavoro lungo una traiettoria dipende solo dagli estremi:

$$
L=U(P_2)-U(P_1).
$$

Quindi non serve conoscere tutto il cammino.

## 18. Mini-checklist finale da ripetere prima dell'esame

- [ ] So definire campo conservativo.
- [ ] So spiegare cos'e' il potenziale.
- [ ] So fare l'esempio $F=(3x^2y,x^3+1)$.
- [ ] So dimostrare che conservativo implica indipendenza dal cammino.
- [ ] So spiegare perche' sulle curve chiuse l'integrale e' zero.
- [ ] So costruire il potenziale da un integrale indipendente dal cammino.
- [ ] So dimostrare $U_x=F_1$ e $U_y=F_2$.
- [ ] So enunciare le condizioni di irrotazionalita'.
- [ ] So distinguere condizioni necessarie e sufficienti.
- [ ] So spiegare il ruolo del dominio.
- [ ] So fare i disegni principali alla lavagna.

## 19. Controlli qualitativi

- Il discorso e' costruito per essere ripetuto a voce.
- Le formule usano delimitatori Obsidian: `$...$` e `$$...$$`.
- La dimostrazione conservativo implica indipendenza dal cammino contiene parametrizzazione, funzione composta e teorema fondamentale.
- La dimostrazione inversa contiene definizione di $U(P)$, segmenti orizzontali/verticali, teorema della media integrale e continuita'.
- E' esplicitato che le condizioni di irrotazionalita' sono necessarie ma non sempre sufficienti.
- La sezione lavagna e' sintetica e ordinata.
- Gli appunti originali in `human/orale` restano fonti grezze e non vengono modificati.
