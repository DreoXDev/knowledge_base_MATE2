# Discorso orale - Campi conservativi

## Stato e navigazione rapida

- Priorita' orale: altissima.
- Stato: master file potenziato.
- Fonti: `01_sources/official_slides/08_integrali_linea_II_specie.pdf`, `01_sources/official_slides/09_campi_conservativi_green.pdf`.
- Teoria base: [[campi_conservativi]], [[indipendenza_cammino]], [[circuitazione]], [[irrotazionalita_forme_chiuse_esatte]], [[domini_semplicemente_connessi]].
- Discorsi collegati: [[integrali_linea_II_specie_discorso_completo]], [[green_discorso_completo]], [[stokes_discorso_completo]].
- Lavagna rapida: `06_oral_exam_discourses/04_lavagna/lavagna_campi_conservativi.md`.

## 0. Mappa del discorso

Campo conservativo -> potenziale -> indipendenza dal cammino -> circuitazione nulla -> irrotazionalita' -> Poincare' su domini semplicemente connessi -> controesempio del campo angolare.

## 1. Obiettivo del discorso

Spiegare quando un integrale di linea di II specie dipende solo dagli estremi e non dal cammino, e chiarire perche' "rotore nullo" non basta senza ipotesi sul dominio.

## Tempo stimato

- Versione essenziale: 10 minuti
- Versione completa con costruzione del potenziale: 16 minuti
- Estensioni/domande su dominio, rotore e campo angolare: 5 minuti

Totale realistico: 15-20 minuti.

## Discorso principale

> "Partirei dalla definizione: un campo vettoriale si dice conservativo se esiste una funzione scalare $U$, detta potenziale, tale che il campo sia il gradiente di $U$."

"F uguale gradiente di U"

$$
\vec F=\nabla U.
$$

> "La conseguenza fondamentale e' sugli integrali di linea di seconda specie: il lavoro lungo una curva dipende solo dagli estremi."

"integrale lungo gamma di F scalare d r uguale differenza di potenziale"

$$
\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1).
$$

> "Quindi su una curva chiusa l'integrale vale zero. Poi bisogna stare attenti al viceversa: rotore nullo e' necessario, ma per concludere conservativita' servono ipotesi sul dominio."

## 2. Prerequisiti da sapere

- Integrale di linea di II specie: [[integrali_linea_II_specie_discorso_completo]].
- Gradiente e potenziale: [[potenziale]], [[calcolo_potenziale]].
- Circuitazione e Green: [[circuitazione]], [[green_discorso_completo]].
- Domini semplicemente connessi: [[domini_semplicemente_connessi]].

## 3. Definizioni richiamate

- Campo vettoriale: funzione $F:\Omega\subset\mathbb{R}^n\to\mathbb{R}^n$.
- Potenziale: funzione $U$ tale che $F=\nabla U$.
- Integrale di II specie: $\int_C F\cdot\tau\,d\ell$.
- Circuitazione: integrale su curva chiusa.
- Campo irrotazionale: rotore nullo, o $P_y=Q_x$ nel piano.
- Forma chiusa: derivate incrociate compatibili.
- Forma esatta: esiste un potenziale.
- Dominio semplicemente connesso: senza buchi rilevanti per circuitazioni chiuse.

## 4. Versione da 30 secondi

Un campo e' conservativo se esiste $U$ con $F=\nabla U$. Allora:

$$
\int_C F\cdot\tau\,d\ell=U(B)-U(A),
$$

quindi l'integrale dipende solo dagli estremi. In particolare ogni circuitazione e' nulla. Se il dominio e' semplicemente connesso, l'irrotazionalita' e' anche sufficiente per avere un potenziale.

## 5. Copione da dire quasi a memoria

"Un campo conservativo e' un campo che nasce come gradiente di un potenziale. Questo rende gli integrali di linea molto piu' semplici: invece di parametrizzare il cammino, valuto il potenziale agli estremi. Le proprieta' equivalenti principali sono indipendenza dal cammino e circuitazione nulla su curve chiuse. Pero' devo stare attento: rotore nullo e' sempre necessario, ma diventa sufficiente solo con ipotesi sul dominio, per esempio semplicemente connesso. Il controesempio classico e' il campo angolare in $\mathbb{R}^2\setminus\{0\}$."

## 6. Enunciato formale / definizione formale

$F$ e' conservativo in $\Omega$ se esiste $U:\Omega\to\mathbb{R}$ tale che:

$$
F=\nabla U.
$$

Allora, per ogni curva $C$ da $A$ a $B$:

$$
\int_C F\cdot\tau\,d\ell=U(B)-U(A).
$$

Se $\Omega$ e' semplicemente connesso e $F$ e' irrotazionale, allora $F$ e' conservativo.

## 7. Spiegazione geometrica o intuitiva

Il potenziale assegna una quota a ogni punto. Il lavoro del campo tra due punti misura solo la differenza di quota, non la strada percorsa. Se torno al punto di partenza, la differenza di potenziale e' zero, quindi la circuitazione e' nulla.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo A - Dimostrazione da esame

### 8.1 Versione breve

Se $F=\nabla U$ e $r(t)$ parametrizza $C$ da $A$ a $B$, allora:

$$
\int_C F\cdot\tau\,d\ell=\int_a^b \nabla U(r(t))\cdot r'(t)\,dt
=\int_a^b \frac{d}{dt}U(r(t))\,dt=U(B)-U(A).
$$

### 8.2 Versione completa

Da $F=\nabla U$ segue l'indipendenza dal cammino. Da questa segue circuitazione nulla, perche' una curva chiusa ha stesso punto iniziale e finale. Viceversa, se ogni circuitazione e' nulla, definisco $U(P)=\int_{P_0}^{P}F\cdot\tau\,d\ell$; la circuitazione nulla rende questa definizione indipendente dal cammino, e derivando si ottiene $\nabla U=F$.

### 8.3 Dove il professore puo' interrompere

- "Rotore nullo basta sempre?"
- "Che differenza c'e' tra forma chiusa ed esatta?"
- "Perche' il campo angolare non e' conservativo?"
- "Come costruisci il potenziale?"

## 9. Rappresentazione grafica

### 9.1 Disegno minimo da lavagna

Disegna due cammini diversi da $P_0$ a $P_1$ e scrivi:

$$
\int_{C_1}F\cdot\tau\,d\ell=\int_{C_2}F\cdot\tau\,d\ell.
$$

Poi disegna una curva chiusa e scrivi:

$$
\oint_C F\cdot\tau\,d\ell=0.
$$

### 9.2 Disegno completo

Disegna $\mathbb{R}^2\setminus\{0\}$, una circonferenza attorno all'origine e il campo angolare tangente. Scrivi che il dominio ha un buco e:

$$
\oint_C F\cdot\tau\,d\ell=2\pi.
$$

### 9.3 Figure ufficiali collegate

- `08_visuals/figures/lezione_9_slide_06_segmento_dominio_aperto.png`
- `08_visuals/figures/lezione_9_slide_13_irrotazionalita.png`
- `08_visuals/figures/lezione_8_slide_08_campo_circonferenza.png`
- `08_visuals/figures/lezione_8_slide_09_campo_circonferenza_vettori.png`

### 9.4 Link a visualizzazioni

- `08_visuals/visual_index.md`, sezioni "Campi conservativi e Green" e "Integrali di linea di II specie".

## 10. Cosa scrivere alla lavagna

### 10.1 Lavagna corta

$$
F=\nabla U\quad\Rightarrow\quad \int_C F\cdot\tau\,d\ell=U(B)-U(A).
$$

$$
C\ \text{chiusa}\quad\Rightarrow\quad \oint_C F\cdot\tau\,d\ell=0.
$$

### 10.2 Lavagna completa

1. Definizione $F=\nabla U$.
2. Teorema fondamentale lungo curve.
3. Equivalenze principali.
4. Poincare' su dominio semplicemente connesso.
5. Controesempio del campo angolare.

### 10.3 Frasi da dire mentre scrivo

- "Conservativo significa gradiente di un potenziale."
- "La circuitazione nulla e' una proprieta' globale."
- "Il dominio conta: il buco puo' impedire il potenziale globale."

## 11. Esempio principale da fare

Per $F=(3x^2y,x^3+1)$:

$$
U_x=3x^2y,\qquad U=x^3y+\phi(y).
$$

Da $U_y=x^3+\phi'(y)=x^3+1$ segue $\phi(y)=y$, quindi:

$$
U=x^3y+y.
$$

Da $(0,0)$ a $(1,1)$ il lavoro vale $U(1,1)-U(0,0)=2$.

## 12. Altri esempi utili

- Campo angolare $F=\left(-\frac{y}{x^2+y^2},\frac{x}{x^2+y^2}\right)$: irrotazionale fuori dall'origine ma non conservativo su $\mathbb{R}^2\setminus\{0\}$.
- Potenziale logaritmico dagli esami.
- Campo con rotore non nullo: non conservativo.

## 13. Terminologia corretta del professore

### Termini da usare

- potenziale;
- indipendenza dal cammino;
- circuitazione nulla;
- irrotazionale;
- forma chiusa;
- forma esatta;
- dominio semplicemente connesso.

### Frasi corrette da dire

- "Irrotazionale e' necessario; diventa sufficiente con ipotesi topologiche sul dominio."
- "La circuitazione nulla e' una condizione globale."
- "Il potenziale e' definito a meno di costante."

### Termini/frasi da evitare

- "Rotore nullo implica sempre conservativo."
- "Il potenziale e' unico" senza dire "a meno di costante".
- "Il campo angolare ha potenziale globale."

## 14. Domande possibili del professore

- Quali proprieta' equivalgono alla conservativita'?
- Come costruisci un potenziale?
- Perche' il dominio semplicemente connesso e' importante?
- Che cosa succede su una curva chiusa?
- Come si collega Green?

## 15. Follow-up e trabocchetti

- Confondere condizione locale e globale.
- Dimenticare la costante del potenziale.
- Non controllare il dominio prima di applicare Poincare'.
- Confondere circuitazione nulla con flusso nullo.

## Immagini / visualizzazioni utili

![[lezione_8_slide_09_campo_circonferenza_vettori.png]]

- Utile per discutere il campo angolare e il fatto che il dominio bucato puo' impedire un potenziale globale.

![[lezione_9_slide_06_segmento_dominio_aperto.png]]

- Serve nella costruzione del potenziale: piccoli segmenti orizzontali/verticali devono restare nel dominio.

![[lezione_9_slide_13_irrotazionalita.png]]

- Aiuta a ricordare le condizioni di irrotazionalita' e il passaggio dalle derivate incrociate.

## Collegamenti utili nella KB

- [[integrali_linea_II_specie_discorso_completo]]: lavoro del campo.
- [[integrali_linea_II_specie|Integrali di linea di seconda specie]]: definizione tecnica di $\int_\gamma \vec F\cdot d\vec r$.
- [[campi_vettoriali|Campi vettoriali]]: contesto della definizione.
- [[gradiente_derivata_direzionale|Gradiente]]: serve per leggere $\vec F=\nabla U$.
- [[calcolo_potenziale|Potenziale]]: costruzione pratica di $U$.
- [[indipendenza_cammino|Indipendenza dal cammino]]: proprieta' equivalente alla conservativita'.
- [[circuitazione|Curve chiuse e circuitazione]]: conseguenza principale sui cammini chiusi.
- [[irrotazionalita_forme_chiuse_esatte|Condizioni di irrotazionalita']] : condizioni necessarie e distinzione chiusa/esatta.
- [[rotore|Rotore]]: formulazione tridimensionale dell'irrotazionalita'.
- [[scambio_derivate_parziali|Teorema di Schwarz]]: giustifica le derivate incrociate.
- [[intorni_aperti_chiusi|Dominio aperto]]: serve nella costruzione locale del potenziale.
- [[dominio_connesso_per_archi|Dominio connesso per archi]]: serve per definire $U(P)$ da un punto base.
- [[domini_semplicemente_connessi|Dominio semplicemente connesso]]: ipotesi tipica per rendere sufficiente il rotore nullo.
- [[teorema_fondamentale_calcolo_integrale|Teorema fondamentale del calcolo integrale]]: chiude la dimostrazione del teorema fondamentale dei campi conservativi.
- [[derivazione_funzione_composta|Derivazione della funzione composta]]: identifica l'integranda come derivata di $U(\gamma(t))$.
- [[green_discorso_completo]]: circuitazione e rotore scalare.
- [[formula_green|Teorema di Green]]: collega circuitazioni chiuse e rotore scalare nel piano.
- [[forme_differenziali|Forme differenziali]]: linguaggio alternativo per $P\,dx+Q\,dy$.
- [[stokes_discorso_completo]]: rotore e circuitazione nello spazio.
- [[campi_solenoidali_discorso_completo]]: confronto con divergenza e flusso.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[campi_conservativi]]
- [[indipendenza_cammino]]
- [[circuitazione]]
- [[irrotazionalita_forme_chiuse_esatte]]
- [[domini_semplicemente_connessi]]
- [[campi_non_semplicemente_connessi]]
- [[calcolo_potenziale]]
- `04_theory/03_potenziale_e_campi_conservativi/campi_conservativi.md`
- `04_theory/03_potenziale_e_campi_conservativi/campi_non_semplicemente_connessi.md`

### Theorem cards

- [[campi_conservativi]]
- [[campi_conservativi_indipendenza_cammino]]
- [[circuitazione_campi_conservativi]]

### Discorsi collegati

- [[integrali_linea_II_specie_discorso_completo]]
- [[green_discorso_completo]]
- [[stokes_discorso_completo]]

### Esercizi

- [[campi_conservativi_esami]]
- [[campi_conservativi_green]]
- `07_exercises/exam_official/campi_conservativi_esami.md`

### Esami ufficiali

- [[2022_11_22]]
- [[2023_04_13]]
- [[2022_09_24_or_27]]

### Figure / visual

- `08_visuals/figures/lezione_9_slide_06_segmento_dominio_aperto.png`
- `08_visuals/figures/lezione_9_slide_13_irrotazionalita.png`
- `08_visuals/figures/lezione_8_slide_09_campo_circonferenza_vettori.png`

## 18. Errori da evitare

- Dire che irrotazionale implica sempre conservativo.
- Non citare il dominio.
- Dimenticare che il potenziale e' a meno di costante.
- Non distinguere cammino aperto e curva chiusa.

## 19. Mini ripasso finale

Conservativo = potenziale. Potenziale -> lavoro $U(B)-U(A)$ -> indipendenza dal cammino -> circuitazione nulla. Rotore nullo basta solo con ipotesi sul dominio.

## 20. Checklist personale

- [ ] So costruire il potenziale di $F=(3x^2y,x^3+1)$.
- [ ] So disegnare due cammini con stessi estremi.
- [ ] So spiegare il campo angolare.
- [ ] So dire quando Poincare' si applica.
- [ ] So collegare a Green.
