# Discorso orale - Formula di Green

## Stato e navigazione rapida

- Priorita' orale: altissima.
- Stato: master file potenziato.
- Fonti: `01_sources/official_slides/09_campi_conservativi_green.pdf`.
- Teoria base: [[formula_green]], [[integrali_linea_II_specie]], [[campi_conservativi]], [[irrotazionalita_forme_chiuse_esatte]], [[green_stokes_gauss_collegamenti]].
- Discorsi collegati: [[integrali_linea_II_specie_discorso_completo]], [[campi_conservativi_discorso_completo]], [[stokes_discorso_completo]], [[integrali_multipli_discorso_completo]].
- Lavagna rapida: `06_oral_exam_discourses/04_lavagna/lavagna_green.md`.

## 0. Mappa del discorso

1. Presento la circuitazione di un campo piano.
2. Fisso dominio, frontiera e orientazione positiva.
3. Enuncio Green.
4. Spiego perche' compare $Q_x-P_y$.
5. Do l'idea della dimostrazione: domini normali e cancellazione dei bordi interni.
6. Faccio un esempio ufficiale.
7. Collego a Stokes e ai campi conservativi.

## 1. Obiettivo del discorso

Green trasforma una circuitazione lungo il bordo di un dominio piano in un integrale doppio sul dominio. Il cuore concettuale e' questo: l'effetto globale lungo la frontiera e' la somma delle rotazioni locali interne.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con dimostrazione: 13 minuti
- Estensioni/domande su orientazione, buchi e Stokes: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei dall'idea: la formula di Green permette di trasformare una circuitazione lungo una curva chiusa nel piano in un integrale doppio sul dominio racchiuso."

> "Considero un campo piano $F=(P,Q)$ e una frontiera $C=\partial D$ orientata positivamente, cioe' percorsa lasciando il dominio alla sinistra."

"integrale su C di P dx piu' Q dy uguale integrale doppio su D di Q_x meno P_y"

$$
\oint_C P\,dx+Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy.
$$

> "Il termine $Q_x-P_y$ e' il rotore scalare nel piano. Quindi Green dice che la circuitazione globale sul bordo e' la somma delle rotazioni locali dentro il dominio."

> "L'orientazione e' importante: se cambio verso alla frontiera, cambia il segno dell'integrale. Nei domini con buchi non dico semplicemente antiorario: dico che il dominio deve restare alla sinistra."

## 2. Prerequisiti da sapere

- Integrale di linea di II specie: [[integrali_linea_II_specie_discorso_completo]].
- Campi conservativi e circuitazione: [[campi_conservativi_discorso_completo]].
- Integrali doppi su domini normali: [[integrali_multipli_discorso_completo]].
- Rotore come misura locale di rotazione: [[rotore_divergenza_discorso_completo]].
- Stokes come generalizzazione spaziale: [[stokes_discorso_completo]], [[formula_stokes]].

## 3. Definizioni richiamate

- Campo piano: $F=(P,Q)$, con $P,Q$ funzioni di due variabili.
- Forma differenziale: $P\,dx+Q\,dy$.
- Circuitazione: integrale di II specie lungo una curva chiusa orientata.
- Frontiera: $C=\partial D$, bordo del dominio piano.
- Orientazione positiva: percorro $C$ lasciando il dominio alla sinistra.
- Dominio normale: dominio descrivibile con estremi di integrazione regolari rispetto a una variabile.
- Rotore scalare piano: $Q_x-P_y$.

## 4. Versione da 30 secondi

Se $D\subset\mathbb{R}^2$ ha frontiera $C=\partial D$ orientata positivamente e $F=(P,Q)$ e' regolare, allora:

$$
\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy.
$$

La formula dice che la circuitazione sul bordo e' uguale alla somma delle rotazioni locali dentro il dominio.

## 5. Copione da dire quasi a memoria

"Considero un campo piano $F=(P,Q)$ e un dominio $D$ con frontiera regolare a tratti. Oriento la frontiera positivamente, cioe' in modo che il dominio resti alla sinistra mentre la percorro. La formula di Green afferma che la circuitazione di $F$ lungo il bordo e' uguale all'integrale doppio su $D$ del rotore scalare $Q_x-P_y$. Dal punto di vista geometrico e' una formula di bilancio: le rotazioni interne si sommano, i contributi sui bordi interni si cancellano, e resta solo il bordo esterno."

## 6. Enunciato formale / definizione formale

Se $D$ e' un dominio piano regolare, $C=\partial D$ e' orientata positivamente, e $P,Q\in C^1$ in un aperto che contiene $D$, allora:

$$
\oint_C P\,dx+Q\,dy
=
\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\,dx\,dy.
$$

## 7. Spiegazione geometrica o intuitiva

Il termine $Q_x-P_y$ e' la componente scalare del rotore nel piano. Se in tanti piccoli rettangoli interni misuro la tendenza del campo a girare, i lati comuni vengono percorsi in versi opposti e quindi si annullano. Sopravvive solo il bordo esterno: per questo un integrale di bordo diventa un integrale d'area.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo A - Dimostrazione da esame

### 8.1 Versione breve

Per domini normali si dimostrano:

$$
\iint_D P_y\,dx\,dy=-\int_C P\,dx,\qquad
\iint_D Q_x\,dx\,dy=\int_C Q\,dy.
$$

Sottraendo la prima e sommando la seconda si ottiene Green. Per domini piu' generali si suddivide in pezzi normali e i bordi interni si cancellano.

### 8.2 Versione completa

Se $D=\{(x,y):a\le x\le b,\ \alpha(x)\le y\le\beta(x)\}$, allora:

$$
\iint_D P_y\,dx\,dy=\int_a^b(P(x,\beta(x))-P(x,\alpha(x)))\,dx.
$$

Con l'orientazione positiva questo corrisponde a $-\int_C P\,dx$. In modo analogo, per un dominio normale rispetto a $y$:

$$
\iint_D Q_x\,dx\,dy=\int_C Q\,dy.
$$

Sommando:

$$
\int_C P\,dx+\int_C Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy.
$$

### 8.3 Dove il professore puo' interrompere

- "Che cosa vuol dire orientazione positiva?"
- "Perche' il bordo interno si cancella?"
- "La formula vale se il dominio ha buchi?"
- "Dove usi la regolarita' $C^1$?"

## 9. Rappresentazione grafica

### 9.1 Disegno minimo da lavagna

Disegna un dominio piano $D$, scrivi $C=\partial D$, metti frecce antiorarie sul bordo esterno e aggiungi: "orientazione positiva = dominio a sinistra".

### 9.2 Disegno completo

Disegna un dominio diviso in due sottodomini. Evidenzia il bordo interno percorso due volte in versi opposti e scrivi: "i contributi interni si cancellano". Se il dominio ha un buco, disegna la frontiera interna in senso orario.

### 9.3 Figure ufficiali collegate

- `08_visuals/figures/oral_green_orientazione_positiva.png`
- `08_visuals/figures/oral_green_cancellazione_bordi.png`
- `08_visuals/figures/lezione_9_slide_20_orientazione_frontiera.png`
- `08_visuals/figures/lezione_9_slide_26_contributi_interni.png`
- `08_visuals/figures/lezione_9_slide_29_parametrizzazione_quadrato.png`
- `08_visuals/figures/lezione_9_slide_33_parametrizzazione_triangolo.png`

### 9.4 Link a visualizzazioni

- `08_visuals/visual_index.md`, sezione "Campi conservativi e Green".

## 10. Cosa scrivere alla lavagna

### 10.1 Lavagna corta

$$
F=(P,Q),\qquad C=\partial D\ \text{positiva}
$$

$$
\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy.
$$

### 10.2 Lavagna completa

1. Disegno del dominio.
2. Formula.
3. Due identita' sui domini normali.
4. Cancellazione dei bordi interni.
5. Esempio numerico.

### 10.3 Frasi da dire mentre scrivo

- "Positiva significa dominio a sinistra."
- "Il termine $Q_x-P_y$ e' il rotore scalare."
- "I lati interni sono percorsi in versi opposti."

## 11. Esempio principale da fare

Quadrato ruotato. Se $F=(x-y,x+y)$, allora:

$$
Q_x-P_y=1-(-1)=2.
$$

Sul quadrato ruotato di area $2$:

$$
\oint_C F\cdot\tau\,d\ell=2\cdot 2=4.
$$

## 12. Altri esempi utili

- Triangolo ufficiale: usare la parametrizzazione dei lati e poi Green.
- Circonferenza: se $F=(x^2y,-xy^2)$, allora $Q_x-P_y=-(x^2+y^2)$.
- Dominio con buco: sottolineare il verso orario della frontiera interna.

## 13. Terminologia corretta del professore

### Termini da usare

- formula di Green;
- circuitazione;
- frontiera;
- orientazione positiva;
- dominio a sinistra;
- rotore scalare;
- curva regolare a tratti.

### Frasi corrette da dire

- "Percorro la frontiera in modo che il dominio rimanga alla mia sinistra."
- "Il termine $Q_x-P_y$ e' la componente scalare del rotore nel caso piano."
- "Green e' il caso piano di Stokes."

### Termini/frasi da evitare

- "Il bordo ha area."
- "Il rotore e' $P_y-Q_x$."
- "Posso sempre usare Green", senza citare regolarita' e curva chiusa.

## 14. Domande possibili del professore

**Prof:** Perche' non basta dire che il bordo e' antiorario?  
**Risposta:** Perche' se il dominio ha buchi, le frontiere interne vanno percorse in senso orario per mantenere il dominio alla sinistra.

**Prof:** Che succede se percorro $C$ nel verso opposto?  
**Risposta:** L'integrale cambia segno.

**Prof:** Se $Q_x-P_y=0$, cosa concludi?  
**Risposta:** Su domini adatti la circuitazione e' nulla; per collegarlo alla conservativita' devo controllare anche le ipotesi topologiche.

## 15. Follow-up e trabocchetti

- Green richiede una curva chiusa.
- Il verso del bordo decide il segno.
- Nei domini con buchi l'orientazione va descritta con "dominio a sinistra", non solo "antioraria".
- $Q_x-P_y=0$ non basta sempre per dire conservativo se il dominio non e' semplicemente connesso.

## Immagini / visualizzazioni utili

![[oral_green_orientazione_positiva.png]]

- Serve per fissare l'orientazione positiva: mentre percorro il bordo, il dominio resta alla sinistra.

![[oral_green_cancellazione_bordi.png]]

- Visualizza l'idea della dimostrazione: i bordi interni vengono percorsi in versi opposti e si cancellano.

![[lezione_9_slide_33_parametrizzazione_triangolo.png]]

- Utile per un esempio concreto su dominio triangolare e per ricordare che Green richiede una curva chiusa orientata.

## Collegamenti utili nella KB

- [[stokes_discorso_completo]]: generalizzazione a superfici nello spazio.
- [[campi_conservativi_discorso_completo]]: circuitazione nulla e potenziale.
- [[integrali_linea_II_specie_discorso_completo]]: Green parte da un integrale di II specie.
- [[integrali_multipli_discorso_completo]]: lato destro come integrale doppio.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[formula_green]]
- [[integrali_linea_II_specie]]
- [[campi_conservativi]]
- [[irrotazionalita_forme_chiuse_esatte]]
- [[green_stokes_gauss_collegamenti]]
- `04_theory/06_teoremi_integrali/formula_green.md`
- `04_theory/01_curve_e_integrali_di_linea/integrali_linea_II_specie.md`

### Theorem cards

- [[formula_green]]
- [[forme_differenziali]]

### Discorsi collegati

- [[integrali_linea_II_specie_discorso_completo]]
- [[campi_conservativi_discorso_completo]]
- [[stokes_discorso_completo]]

### Esercizi

- [[green_esami]]
- [[campi_conservativi_green]]
- `07_exercises/exam_official/green_esami.md`

### Esami ufficiali

- [[2022_07_14]]
- [[2022_11_22]]
- [[2022_09_24_or_27]]
- [[2023_07_19]]

### Figure / visual

- `08_visuals/figures/oral_green_orientazione_positiva.png`
- `08_visuals/figures/oral_green_cancellazione_bordi.png`
- `08_visuals/figures/lezione_9_slide_33_parametrizzazione_triangolo.png`

## 18. Errori da evitare

- Scrivere $P_y-Q_x$ al posto di $Q_x-P_y$.
- Dimenticare l'orientazione positiva.
- Applicare Green a una curva aperta.
- Non distinguere bordo esterno e bordo interno.

## 19. Mini ripasso finale

Green = bordo chiuso + dominio a sinistra + rotore scalare $Q_x-P_y$. Dimostrazione: due identita' su domini normali e cancellazione dei bordi interni. Collegamenti naturali: campi conservativi e Stokes.

## 20. Checklist personale

- [ ] So enunciare la formula senza invertire il segno.
- [ ] So spiegare "dominio a sinistra".
- [ ] So disegnare un dominio con buco.
- [ ] So fare il quadrato ruotato.
- [ ] So collegare Green a Stokes.
