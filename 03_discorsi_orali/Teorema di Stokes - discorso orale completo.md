# Teorema di Stokes - discorso orale completo

## 1. Obiettivo del discorso

Vorrei parlare del teorema di Stokes. L'idea centrale e' che la circuitazione di un campo lungo il bordo di una superficie e' uguale al flusso del rotore attraverso la superficie.

Nel discorso voglio collegare superficie orientata, bordo compatibile, rotore, flusso e rapporto con la formula di Green.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con idea di dimostrazione: 13 minuti
- Estensioni/domande su orientazione e cambio di superficie: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei dicendo che Stokes e' una formula bordo-superficie: trasforma una circuitazione sul bordo in un flusso del rotore attraverso la superficie."

Sia $S$ una superficie orientata, con bordo:

$$
C=\partial S.
$$

Scelgo una normale $\vec n$ su $S$ e oriento il bordo in modo compatibile.

La formula e':

$$
\oint_{\partial S}\vec F\cdot\vec\tau\,ds
=
\iint_S \operatorname{rot}\vec F\cdot\vec n\,dS.
$$

> "Il punto delicato e' l'orientazione: la normale scelta determina il verso positivo del bordo."

## 2. Prerequisiti richiamati rapidamente

### [[integrali_linea_II_specie|Circuitazione]]

La circuitazione e' un integrale di linea di seconda specie lungo una curva chiusa.

**Possibile domanda del prof:** perche' il bordo e' chiuso?

**Risposta breve:** perche' e' il bordo di una superficie.

### [[rotore|Rotore]]

Il rotore misura la tendenza locale del campo a ruotare.

**Possibile domanda del prof:** perche' compare il rotore?

**Risposta breve:** perche' Stokes somma le rotazioni locali sulla superficie.

### [[integrale_superficiale|Flusso]]

Il membro destro e' il flusso del rotore attraverso $S$.

**Possibile domanda del prof:** che normale uso?

**Risposta breve:** la normale scelta per orientare la superficie, compatibile con il bordo.

## 3. Enunciato formale

Sia $S$ una superficie regolare a tratti, orientabile, con bordo $\partial S$. Se $\vec F$ e' regolare, allora:

$$
\oint_{\partial S}\vec F\cdot\vec\tau\,ds
=
\iint_S \operatorname{rot}\vec F\cdot\vec n\,dS.
$$

Il verso di $\partial S$ deve essere compatibile con $\vec n$ secondo la regola della mano destra.

## 4. Primo esempio da fare alla lavagna

Se due superfici $S_1$ e $S_2$ hanno lo stesso bordo $C$ e orientazioni compatibili, allora posso scegliere quella piu' comoda:

$$
\oint_C\vec F\cdot d\vec r
=
\iint_{S_1}\operatorname{rot}\vec F\cdot\vec n\,dS
=
\iint_{S_2}\operatorname{rot}\vec F\cdot\vec n\,dS.
$$

### Cosa dire a voce

Questo e' molto utile negli esercizi: se il bordo e' una circonferenza nello spazio, spesso sostituisco una calotta con un disco piano.

## 5. Idea della dimostrazione

Per una superficie parametrizzata:

$$
\sigma(u,v),
$$

riporto il problema al dominio dei parametri. Il bordo della superficie corrisponde al bordo del dominio piano. Applicando Green nel piano dei parametri, i termini si riorganizzano nel prodotto:

$$
\operatorname{rot}\vec F(\sigma(u,v))\cdot(\sigma_u\times\sigma_v).
$$

Quindi Stokes si puo' vedere come Green trasportato su una superficie.

**Da dire a voce:** per questo spesso si dice che Stokes generalizza Green.

## 6. Disegni da fare alla lavagna

### Disegno 1 - superficie con bordo

Disegno una superficie $S$ con bordo $C$.

### Disegno 2 - normale e verso compatibile

Metto una normale $\vec n$ e una freccia sul bordo, usando la regola della mano destra.

### Disegno 3 - cambio di superficie

Disegno due superfici con lo stesso bordo, per esempio calotta e disco.

## Collegamenti utili nella KB

- [[formula_stokes]]
- [[rotore]]
- [[integrali_linea_II_specie]]
- [[flusso_integrali_superficie_II_specie]]
- [[formula_green]]
- [[green_stokes_gauss_collegamenti]]

## Immagini / visualizzazioni utili

![[oral_stokes_superficie_bordo.png]]

Questa figura e' il riferimento principale per normale, bordo e orientazione compatibile.

![[lezione_11_slide_32_stokes_emisfero.png]]

Utile per l'idea di sostituire una superficie con un'altra avente lo stesso bordo.

## 15. Versione discorso continuo da imparare

"Il teorema di Stokes collega la circuitazione di un campo lungo il bordo di una superficie con il flusso del rotore attraverso la superficie. Considero una superficie orientata $S$, scelgo una normale $n$ e oriento il bordo $\partial S$ in modo compatibile, secondo la regola della mano destra. Allora l'integrale di linea di $F$ lungo il bordo e' uguale all'integrale superficiale del rotore di $F$ scalare la normale. Il significato geometrico e' che la circuitazione sul bordo e' la somma delle rotazioni locali sulla superficie. La formula di Green si puo' vedere come un caso piano di Stokes. Negli esercizi, Stokes e' utile anche per cambiare superficie mantenendo lo stesso bordo, scegliendo quella piu' semplice."

## 16. Versione lavagna

1. Disegno $S$ e $C=\partial S$.
2. Scelgo $\vec n$.
3. Oriento $C$ compatibilmente.
4. Scrivo:

$$
\oint_{\partial S}\vec F\cdot\vec\tau\,ds
=
\iint_S\operatorname{rot}\vec F\cdot\vec n\,dS.
$$

5. Scrivo "Green = caso piano".

## 17. Possibili domande del professore

### 1. Che cosa dice Stokes?

La circuitazione sul bordo e' il flusso del rotore attraverso la superficie.

### 2. Che orientazione serve?

Bordo e normale devono essere compatibili.

### 3. Posso cambiare superficie?

Si', se mantengo lo stesso bordo e le ipotesi sono rispettate.

### 4. Green e' un caso di Stokes?

Si', nel caso di superficie piana.

### 5. Differenza con Gauss?

Stokes usa bordo e rotore; Gauss usa superficie chiusa e divergenza.

## 18. Mini-checklist finale

- So enunciare la formula.
- So spiegare orientazione compatibile.
- So collegare Stokes a Green.
- So dire quando conviene cambiare superficie.
- So distinguere Stokes da Gauss.

## 19. Controlli qualitativi

- Non usare "normale uscente" se la superficie non chiude un volume.
- Non dimenticare il bordo.
- Non confondere rotore e divergenza.
