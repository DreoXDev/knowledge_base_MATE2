# Discorso orale - Formula di Stokes

## Stato e navigazione rapida

- Priorita' orale: altissima.
- Stato: master file potenziato.
- Fonti: `01_sources/official_slides/11_calcolo_vettoriale.pdf`.
- Teoria base: [[formula_stokes]], [[rotore_divergenza]], [[green_stokes_gauss_collegamenti]], [[integrali_linea_II_specie]], [[flusso_integrali_superficie_II_specie]].
- Discorsi collegati: [[green_discorso_completo]], [[integrali_linea_II_specie_discorso_completo]], [[gauss_ostrogradski_discorso_completo]].
- Lavagna rapida: `06_oral_exam_discourses/04_lavagna/lavagna_stokes.md`.

## 0. Mappa del discorso

Superficie orientata -> bordo compatibile -> circuitazione sul bordo -> flusso del rotore -> Green come caso piano -> esempi di uso per cambiare superficie.

## 1. Obiettivo del discorso

Spiegare che Stokes collega la circuitazione lungo il bordo di una superficie con il flusso del rotore attraverso la superficie.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con idea di dimostrazione: 13 minuti
- Estensioni/domande su orientazione, Green e cambio di superficie: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei dicendo che Stokes e' il teorema che collega una circuitazione su un bordo con il flusso del rotore attraverso una superficie."

> "Scelgo una superficie orientata $S$, una normale $n$ e il bordo $C=\partial S$ orientato in modo compatibile con quella normale."

"integrale sul bordo di F scalare tau d ell uguale flusso del rotore"

$$
\oint_{\partial S}F\cdot\tau\,d\ell
=
\iint_S \operatorname{rot}F\cdot n\,dS.
$$

> "Il punto delicato e' l'orientazione: se cambio la normale, cambia anche il verso positivo del bordo. In questo senso Stokes e' la versione spaziale della formula di Green."

## 2. Prerequisiti da sapere

- Integrale di linea di II specie: [[integrali_linea_II_specie_discorso_completo]].
- Rotore e flusso: [[rotore_divergenza_discorso_completo]], [[integrali_superficie_flusso_discorso_completo]].
- Green: [[green_discorso_completo]].
- Superfici orientabili: [[curve_superfici_discorso_completo]].

## 3. Definizioni richiamate

- Superficie orientata: superficie con normale scelta con continuita'.
- Bordo della superficie: curva $C=\partial S$.
- Orientazione compatibile: normale e verso del bordo legati dalla regola della mano destra.
- Rotore: campo che misura la rotazione locale.
- Flusso del rotore: $\iint_S \operatorname{rot}F\cdot n\,dS$.

## 4. Versione da 30 secondi

Se $S$ e' una superficie orientata con bordo $C=\partial S$ orientato compatibilmente, allora:

$$
\oint_C F\cdot\tau\,d\ell=\iint_S \operatorname{rot}F\cdot n\,dS.
$$

Stokes dice che la circuitazione sul bordo e' uguale alla somma delle rotazioni locali attraversate dalla superficie.

## 5. Copione da dire quasi a memoria

"La formula di Stokes e' la versione spaziale di Green. Prendo una superficie orientata $S$ e il suo bordo $C$. Se il verso di $C$ e' compatibile con la normale scelta su $S$, la circuitazione di $F$ lungo $C$ e' uguale al flusso del rotore di $F$ attraverso $S$. L'orientazione e' la parte delicata: cambiando normale cambia anche il verso positivo del bordo."

## 6. Enunciato formale / definizione formale

Per $F$ regolare, $S$ orientabile e regolare a tratti, $C=\partial S$:

$$
\oint_{\partial S}F\cdot\tau\,d\ell
=
\iint_S \operatorname{rot}F\cdot n\,dS.
$$

## 7. Spiegazione geometrica o intuitiva

Stokes somma le piccole circuitazioni locali sulla superficie. I bordi interni si cancellano, come in Green, e resta solo il bordo esterno della superficie.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo A - Dimostrazione da esame

### 8.1 Versione breve

Per una superficie parametrizzata $\sigma(u,v)$ si riporta tutto al dominio dei parametri. Il bordo di $S$ corrisponde al bordo del dominio piano e Green applicato nel piano dei parametri produce la formula con il rotore.

### 8.2 Versione completa

Si scrive l'integrale di linea sul bordo tramite la parametrizzazione $\sigma$. L'integrale diventa una forma differenziale nel piano $(u,v)$. Applicando Green al dominio dei parametri, i termini si riorganizzano nel prodotto $\operatorname{rot}F(\sigma(u,v))\cdot(\sigma_u\times\sigma_v)$, cioe' nel flusso del rotore.

### 8.3 Dove il professore puo' interrompere

- "Qual e' l'orientazione compatibile?"
- "Green e' davvero un caso particolare?"
- "Posso cambiare superficie mantenendo lo stesso bordo?"
- "Che succede se la superficie e' chiusa?"

## 9. Rappresentazione grafica

### 9.1 Disegno minimo da lavagna

Disegna una superficie $S$ con bordo $C$, una normale $n$, una freccia su $C$ e scrivi "orientazione compatibile".

### 9.2 Disegno completo

Mostra che se guardo nella direzione di $n$, il bordo e' percorso lasciando la superficie a sinistra. Disegna anche una superficie alternativa con lo stesso bordo per spiegare quando conviene cambiare $S$.

### 9.3 Figure ufficiali collegate

- `08_visuals/figures/oral_stokes_superficie_bordo.png`
- `08_visuals/figures/lezione_11_slide_23_stokes_piano.png`
- `08_visuals/figures/lezione_11_slide_27_lati_stokes.png`
- `08_visuals/figures/lezione_11_slide_32_stokes_emisfero.png`

### 9.4 Link a visualizzazioni

- `08_visuals/visual_index.md`, sezione "Calcolo vettoriale e integrali di superficie".

## 10. Cosa scrivere alla lavagna

### 10.1 Lavagna corta

$$
C=\partial S,\qquad
\oint_C F\cdot\tau\,d\ell=\iint_S \operatorname{rot}F\cdot n\,dS.
$$

### 10.2 Lavagna completa

1. Disegno superficie-bordo-normale.
2. Orientazione compatibile.
3. Formula.
4. "Green = caso piano".
5. Esempio.

### 10.3 Frasi da dire mentre scrivo

- "Il bordo eredita il verso dalla normale."
- "Stokes trasforma circuitazione in flusso del rotore."
- "Se cambio normale, cambia il verso positivo del bordo."

## 11. Esempio principale da fare

Emisfero superiore con bordo circolare: usando Stokes si puo' sostituire l'emisfero con il disco piano avente lo stesso bordo, se l'orientazione e' coerente. Nel materiale ufficiale compare il risultato $-18\pi$.

## 12. Altri esempi utili

- Piano nel primo ottante con risultato $-1$.
- Campo con rotore nullo: circuitazione nulla su bordi compatibili.
- Stesso bordo, superficie piu' comoda.

## 13. Terminologia corretta del professore

### Termini da usare

- superficie orientata;
- bordo;
- orientazione compatibile;
- rotore;
- flusso del rotore;
- circuitazione.

### Frasi corrette da dire

- "Stokes e' Green nello spazio."
- "La normale scelta determina il verso positivo del bordo."
- "La superficie deve avere bordo."

### Termini/frasi da evitare

- Confondere normale uscente con normale compatibile.
- Applicare Stokes a una superficie chiusa senza bordo.
- Dimenticare il verso del bordo.

## 14. Domande possibili del professore

- Come scelgo il verso del bordo?
- Perche' Green e' un caso particolare?
- Quando conviene usare Stokes?
- Che differenza c'e' tra Stokes e Gauss?
- Se $\operatorname{rot}F=0$, cosa concludi?

## 15. Follow-up e trabocchetti

- Superficie con bordo: Stokes.
- Superficie chiusa: di solito Gauss.
- Se inverti la normale, devi invertire il bordo.
- Il rotore nullo porta circuitazione nulla sui bordi considerati.

## Immagini / visualizzazioni utili

![[oral_stokes_superficie_bordo.png]]

- Figura principale: superficie, bordo, normale e verso compatibile.

![[lezione_11_slide_23_stokes_piano.png]]

- Utile per ricordare il collegamento con Green come caso piano.

![[lezione_11_slide_32_stokes_emisfero.png]]

- Serve per l'esempio in cui si cambia superficie mantenendo lo stesso bordo.

## Collegamenti utili nella KB

- [[green_discorso_completo]]: caso piano.
- [[integrali_linea_II_specie_discorso_completo]]: lato sinistro.
- [[gauss_ostrogradski_discorso_completo]]: confronto rotore/divergenza.
- [[rotore_divergenza_discorso_completo]]: operatori differenziali.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[formula_stokes]]
- [[rotore_divergenza]]
- [[green_stokes_gauss_collegamenti]]
- [[integrali_linea_II_specie]]
- [[flusso_integrali_superficie_II_specie]]
- `04_theory/06_teoremi_integrali/formula_stokes.md`
- `04_theory/02_campi_vettoriali/rotore_divergenza.md`

### Theorem cards

- [[formula_stokes]]
- [[green_stokes_gauss_schema]]
- [[flusso_integrale_superficie_II_specie]]

### Discorsi collegati

- [[green_discorso_completo]]
- [[integrali_linea_II_specie_discorso_completo]]
- [[gauss_ostrogradski_discorso_completo]]

### Esercizi

- [[stokes]]
- [[integrali_superficie_calcolo_vettoriale]]
- `07_exercises/esercizi_per_topic/stokes.md`

### Esami ufficiali

- [[2023_04_13]]
- [[2023_07_19]]

### Figure / visual

- `08_visuals/figures/oral_stokes_superficie_bordo.png`
- `08_visuals/figures/lezione_11_slide_32_stokes_emisfero.png`

## 18. Errori da evitare

- Usare una normale e un bordo non compatibili.
- Confondere Stokes con Gauss.
- Applicare Stokes a una superficie senza bordo.
- Dimenticare che il lato destro e' flusso del rotore, non flusso del campo.

## 19. Mini ripasso finale

Stokes = bordo di superficie + circuitazione + rotore. Formula: integrale sul bordo uguale flusso del rotore. Orientazione: normale e bordo devono essere compatibili.

## 20. Checklist personale

- [ ] So disegnare superficie, bordo e normale.
- [ ] So spiegare l'orientazione compatibile.
- [ ] So collegare Stokes a Green.
- [ ] So distinguere Stokes e Gauss.
- [ ] So fare almeno un esempio ufficiale.
