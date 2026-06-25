# Discorso orale - Formula di Gauss-Ostrogradski

## Stato e navigazione rapida

- Priorita' orale: altissima.
- Stato: master file potenziato.
- Fonti: `01_sources/official_slides/11_calcolo_vettoriale.pdf`.
- Teoria base: [[formula_gauss_ostrogradski]], [[rotore_divergenza]], [[campi_solenoidali_potenziale_vettore]], [[green_stokes_gauss_collegamenti]], [[flusso_integrali_superficie_II_specie]].
- Discorsi collegati: [[stokes_discorso_completo]], [[integrali_superficie_flusso_discorso_completo]], [[campi_solenoidali_discorso_completo]].
- Lavagna rapida: `06_oral_exam_discourses/04_lavagna/lavagna_gauss.md`.

## 0. Mappa del discorso

Volume -> superficie chiusa -> normale uscente -> flusso del campo -> divergenza nel volume -> interpretazione sorgenti/pozzi -> confronto con Stokes.

## 1. Obiettivo del discorso

Spiegare che il flusso uscente da una superficie chiusa e' determinato dalla divergenza del campo nel volume racchiuso.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con idea di dimostrazione: 13 minuti
- Estensioni/domande su gusci, singolarita' e confronto con Stokes: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei dall'idea di bilancio: il flusso netto uscente da una superficie chiusa misura quanta sorgente netta del campo c'e' dentro il volume."

> "Prendo un volume $\Omega$ e la sua superficie chiusa $S=\partial\Omega$, orientata con normale uscente."

"flusso uscente uguale integrale triplo della divergenza"

$$
\iint_{\partial\Omega}F\cdot n\,dS
=
\iiint_\Omega \operatorname{div}F\,dV.
$$

> "La superficie deve essere chiusa: se e' aperta, prima devo chiuderla oppure usare un altro teorema. La normale richiesta e' quella uscente dal volume."

## 2. Prerequisiti da sapere

- Flusso attraverso superfici: [[integrali_superficie_flusso_discorso_completo]].
- Divergenza: [[rotore_divergenza_discorso_completo]].
- Superfici orientabili: [[curve_superfici_discorso_completo]].
- Stokes per confronto: [[stokes_discorso_completo]].

## 3. Definizioni richiamate

- Volume $\Omega$: regione tridimensionale.
- Superficie chiusa: $S=\partial\Omega$ senza bordo.
- Normale uscente: normale orientata verso l'esterno del volume.
- Flusso: $\iint_S F\cdot n\,dS$.
- Divergenza: $\operatorname{div}F=P_x+Q_y+R_z$.
- Campo solenoidale: campo con divergenza nulla.

## 4. Versione da 30 secondi

Se $S=\partial\Omega$ e' una superficie chiusa orientata con normale uscente, allora:

$$
\iint_S F\cdot n\,dS=\iiint_\Omega \operatorname{div}F\,dV.
$$

La formula dice che il flusso netto uscente e' la somma delle sorgenti e dei pozzi interni.

## 5. Copione da dire quasi a memoria

"Gauss-Ostrogradski collega un integrale superficiale a un integrale triplo. Prendo un volume $\Omega$ e la sua superficie chiusa orientata con normale uscente. Il flusso totale del campo attraverso la frontiera e' uguale all'integrale della divergenza nel volume. La divergenza misura localmente quanto il campo nasce o scompare: se e' positiva ho sorgenti, se e' negativa ho pozzi."

## 6. Enunciato formale / definizione formale

Per $F=(P,Q,R)$ regolare e $\Omega$ regolare:

$$
\iint_{\partial\Omega} F\cdot n\,dS
=
\iiint_{\Omega} (P_x+Q_y+R_z)\,dV.
$$

L'orientazione richiesta e' la normale uscente.

## 7. Spiegazione geometrica o intuitiva

Dividendo il volume in tante celle, i flussi attraverso le facce interne si cancellano perche' ogni faccia e' vista con normali opposte da due celle adiacenti. Resta solo il flusso attraverso la superficie esterna.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo A - Dimostrazione da esame

### 8.1 Versione breve

Si dimostra componente per componente usando il teorema fondamentale del calcolo su domini semplici:

$$
\iiint_\Omega P_x\,dV=\iint_{\partial\Omega}P n_x\,dS,
$$

e analogamente per $Q_y$ e $R_z$. Sommando si ottiene la formula.

### 8.2 Versione completa

Per un dominio semplice rispetto a $x$, l'integrale di $P_x$ produce il contributo sulle due facce estreme, con segno coerente con la normale uscente. Ripetendo rispetto a $y$ e $z$, i contributi si sommano in $F\cdot n$. Per domini piu' generali si suddivide in domini semplici; i contributi interni si cancellano.

### 8.3 Dove il professore puo' interrompere

- "Perche' la normale e' uscente?"
- "Che differenza c'e' con Stokes?"
- "Cosa succede se la superficie e' aperta?"
- "Che significa divergenza nulla?"

## 9. Rappresentazione grafica

### 9.1 Disegno minimo da lavagna

Disegna un volume $\Omega$, la superficie chiusa $S=\partial\Omega$, normali uscenti e scrivi:

$$
\iint_SF\cdot n\,dS=\iiint_\Omega \operatorname{div}F\,dV.
$$

### 9.2 Disegno completo

Disegna un guscio sferico: sfera esterna con normale verso fuori, sfera interna con normale uscente dal guscio verso il centro. Evidenzia che il verso della normale interna cambia il segno del flusso.

### 9.3 Figure ufficiali collegate

- `08_visuals/figures/oral_gauss_normale_uscente.png`
- `08_visuals/figures/lezione_11_slide_35_regioni_semplici.png`
- `08_visuals/figures/lezione_11_slide_42_normale_sfera.png`
- `08_visuals/figures/lezione_11_slide_15_flusso.png`

### 9.4 Link a visualizzazioni

- `08_visuals/visual_index.md`, sezione "Calcolo vettoriale e integrali di superficie".

## 10. Cosa scrivere alla lavagna

### 10.1 Lavagna corta

$$
S=\partial\Omega,\qquad n=\text{normale uscente}
$$

$$
\iint_SF\cdot n\,dS=\iiint_\Omega \operatorname{div}F\,dV.
$$

### 10.2 Lavagna completa

1. Disegno volume e normali uscenti.
2. Formula.
3. Interpretazione divergenza.
4. Esempio sfera.
5. Box confronto con Stokes.

### 10.3 Frasi da dire mentre scrivo

- "La superficie deve essere chiusa."
- "La normale e' uscente dal volume."
- "La divergenza misura sorgenti e pozzi."

## 11. Esempio principale da fare

Per $F=(x,y,z)$ su una sfera di raggio $R$:

$$
\operatorname{div}F=3.
$$

Quindi:

$$
\iint_S F\cdot n\,dS=\iiint_\Omega 3\,dV=3\cdot\frac{4}{3}\pi R^3=4\pi R^3.
$$

## 12. Altri esempi utili

- $F=(x^3,y^3,z^3)$ su sfera: usare simmetria e coordinate sferiche se serve.
- Campo $\frac{r}{\|r\|^3}$ su guscio sferico: attenzione alla singolarita' e alle normali.
- Campo solenoidale: divergenza nulla, flusso netto nullo su superfici chiuse adatte.

## 13. Terminologia corretta del professore

### Termini da usare

- superficie chiusa;
- normale uscente;
- flusso;
- divergenza;
- volume racchiuso;
- sorgenti e pozzi;
- campo solenoidale.

### Frasi corrette da dire

- "Gauss richiede una superficie chiusa."
- "La normale e' orientata verso l'esterno del volume."
- "Il flusso netto e' l'integrale della divergenza."

### Termini/frasi da evitare

- "Normale compatibile col bordo" per Gauss.
- Applicare Gauss direttamente a superfici aperte.
- Confondere divergenza e rotore.

## 14. Domande possibili del professore

- Perche' serve una superficie chiusa?
- Come orienti un guscio sferico?
- Che differenza c'e' tra flusso e circuitazione?
- Che cosa significa divergenza nulla?
- Quando conviene usare Gauss?

## 15. Follow-up e trabocchetti

> Stokes: superficie con bordo, circuitazione sul bordo, rotore.  
> Gauss: superficie chiusa, flusso uscente, divergenza.

- Una superficie aperta va chiusa prima di usare Gauss.
- La normale interna di un buco punta verso il centro del buco, non verso l'esterno geometrico della sfera interna.
- Le singolarita' interne vanno controllate.

## Collegamenti utili nella KB

- [[stokes_discorso_completo]]: confronto tra teoremi integrali.
- [[integrali_superficie_flusso_discorso_completo]]: definizione di flusso.
- [[campi_solenoidali_discorso_completo]]: divergenza nulla.
- [[green_stokes_gauss_collegamenti]]: schema comune dei teoremi.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[formula_gauss_ostrogradski]]
- [[rotore_divergenza]]
- [[campi_solenoidali_potenziale_vettore]]
- [[green_stokes_gauss_collegamenti]]
- [[flusso_integrali_superficie_II_specie]]
- `04_theory/06_teoremi_integrali/formula_gauss_ostrogradski.md`
- `04_theory/02_campi_vettoriali/rotore_divergenza.md`

### Theorem cards

- [[formula_gauss_ostrogradski]]
- [[green_stokes_gauss_schema]]
- [[flusso_integrale_superficie_II_specie]]

### Discorsi collegati

- [[stokes_discorso_completo]]
- [[integrali_superficie_flusso_discorso_completo]]
- [[campi_solenoidali_discorso_completo]]

### Esercizi

- [[integrali_superficie_calcolo_vettoriale]]
- [[flusso_esami]]
- `07_exercises/exam_official/flusso_esami.md`

### Esami ufficiali

- [[2023_04_13]]
- [[2023_07_19]]
- [[2022_09_24_or_27]]

### Figure / visual

- `08_visuals/figures/oral_gauss_normale_uscente.png`
- `08_visuals/figures/lezione_11_slide_42_normale_sfera.png`

## 18. Errori da evitare

- Usare Gauss su superfici aperte senza chiuderle.
- Sbagliare il verso della normale.
- Confondere divergenza con rotore.
- Ignorare singolarita' nel volume.

## 19. Mini ripasso finale

Gauss = superficie chiusa + normale uscente + flusso del campo + divergenza nel volume. E' un bilancio sorgenti/pozzi.

## 20. Checklist personale

- [ ] So disegnare volume e normali uscenti.
- [ ] So spiegare il guscio sferico.
- [ ] So fare $F=(x,y,z)$ sulla sfera.
- [ ] So distinguere Gauss da Stokes.
- [ ] So dire cosa succede se la superficie e' aperta.
