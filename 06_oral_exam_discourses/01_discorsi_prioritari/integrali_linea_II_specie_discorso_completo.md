# Discorso orale - Integrali di linea di II specie

## Stato e navigazione rapida

- Priorita' orale: altissima.
- Stato: master file potenziato.
- Fonti: `01_sources/official_slides/08_integrali_linea_II_specie.pdf`.
- Teoria base: [[integrali_linea_II_specie]], [[campi_vettoriali]], [[forme_differenziali]], [[campi_conservativi]], [[formula_green]].
- Discorsi collegati: [[integrali_linea_I_specie_discorso_completo]], [[campi_conservativi_discorso_completo]], [[green_discorso_completo]].
- Lavagna rapida: `06_oral_exam_discourses/04_lavagna/lavagna_integrali_linea.md`.

## 0. Mappa del discorso

Curva orientata -> campo vettoriale -> componente tangenziale -> lavoro -> forma differenziale -> potenziale se il campo e' conservativo -> Green se la curva e' chiusa.

## 1. Obiettivo del discorso

Spiegare l'integrale di un campo vettoriale lungo una curva orientata e il suo significato come lavoro/circuitazione.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con derivazione della formula e forma differenziale: 13 minuti
- Estensioni/domande su potenziale, verso e Green: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei dalla differenza rispetto alla prima specie: qui non integro una funzione scalare rispetto alla lunghezza, ma un campo vettoriale lungo una curva orientata."

> "In ogni punto prendo solo la componente del campo nella direzione tangente alla curva."

"integrale di F scalare tau d ell"

$$
\int_C F\cdot\tau\,d\ell
=
\int_a^b F(r(t))\cdot r'(t)\,dt.
$$

> "Nel piano questa formula si scrive anche come forma differenziale $P\,dx+Q\,dy$. Il verso e' parte del dato: se inverto la curva, l'integrale cambia segno."

## 2. Prerequisiti da sapere

- Curve parametrizzate e verso: [[curve_parametrizzate_discorso]].
- Campi vettoriali: [[campi_vettoriali_discorso]].
- I specie per confronto: [[integrali_linea_I_specie_discorso_completo]].
- Campi conservativi: [[campi_conservativi_discorso_completo]].
- Green: [[green_discorso_completo]].

## 3. Definizioni richiamate

- Curva orientata: curva con verso di percorrenza fissato.
- Versore tangente: $\tau=\frac{r'}{\|r'\|}$.
- Campo vettoriale: $F=(P,Q)$ o $F=(P,Q,R)$.
- Lavoro: somma delle componenti tangenziali del campo lungo lo spostamento.
- Forma differenziale: $P\,dx+Q\,dy$.
- Circuitazione: integrale lungo curva chiusa.

## 4. Versione da 30 secondi

Se $C$ e' orientata e parametrizzata da $r(t)$, allora:

$$
\int_C F\cdot\tau\,d\ell=\int_a^b F(r(t))\cdot r'(t)\,dt.
$$

Nel piano, per $F=(P,Q)$:

$$
\int_C P\,dx+Q\,dy.
$$

Misura il lavoro del campo lungo la curva e cambia segno se inverto il verso.

## 5. Copione da dire quasi a memoria

"L'integrale di linea di II specie integra un campo vettoriale lungo una curva orientata. Non sommo tutto il campo, ma solo la componente nella direzione tangente. Per questo compare $F\cdot\tau\,d\ell$, che diventa $F(r(t))\cdot r'(t)\,dt$. Nel piano si scrive anche come forma differenziale $P\,dx+Q\,dy$. Se il campo e' conservativo posso usare un potenziale; se la curva e' chiusa posso collegarmi a Green."

## 6. Enunciato formale / definizione formale

Per $C:r(t)$, $t\in[a,b]$:

$$
\int_C F\cdot\tau\,d\ell
=
\int_a^b F(r(t))\cdot r'(t)\,dt.
$$

Se $F=(P,Q)$ e $r(t)=(x(t),y(t))$:

$$
\int_C P\,dx+Q\,dy
=
\int_a^b [P(x(t),y(t))x'(t)+Q(x(t),y(t))y'(t)]\,dt.
$$

## 7. Spiegazione geometrica o intuitiva

In ogni punto della curva guardo quanto il campo spinge nella direzione di percorrenza. La componente perpendicolare alla curva non contribuisce al lavoro. Se cambio verso, cambia il tangente e quindi cambia il segno.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo A - Derivazione della formula

### 8.1 Versione breve

Poiche' $\tau=\frac{r'}{\|r'\|}$ e $d\ell=\|r'\|dt$, allora:

$$
F\cdot\tau\,d\ell
=
F(r(t))\cdot\frac{r'(t)}{\|r'(t)\|}\|r'(t)\|dt
=
F(r(t))\cdot r'(t)dt.
$$

### 8.2 Versione completa

Si parte dalla somma dei lavori elementari $F(P_i)\cdot\Delta r_i$. Con una parametrizzazione regolare $\Delta r_i\sim r'(t_i)\Delta t_i$, quindi il limite delle somme e' l'integrale $\int F(r(t))\cdot r'(t)dt$.

### 8.3 Dove il professore puo' interrompere

- "Perche' il verso cambia il segno?"
- "Che differenza c'e' con I specie?"
- "Quando posso usare il potenziale?"
- "Come entra Green?"

## 9. Rappresentazione grafica

### 9.1 Disegno minimo da lavagna

Disegna una curva orientata $C$, il versore tangente $\tau$, il campo $F$ e la proiezione $F\cdot\tau$ lungo la tangente.

### 9.2 Disegno completo

Disegna due cammini diversi tra gli stessi estremi e spiega che in generale il lavoro cambia. Poi aggiungi il caso conservativo, dove i due lavori coincidono perche' esiste un potenziale.

### 9.3 Figure ufficiali collegate

- `08_visuals/figures/oral_linea_II_tangente.png`
- `08_visuals/figures/lezione_8_slide_08_campo_circonferenza.png`
- `08_visuals/figures/lezione_8_slide_09_campo_circonferenza_vettori.png`
- `08_visuals/figures/lezione_8_slide_10_campo_normalizzato.png`

### 9.4 Link a visualizzazioni

- `08_visuals/visual_index.md`, sezione "Integrali di linea di II specie e campi vettoriali".

## 10. Cosa scrivere alla lavagna

### 10.1 Lavagna corta

$$
\int_C F\cdot\tau\,d\ell=\int_a^b F(r(t))\cdot r'(t)\,dt.
$$

$$
\int_C P\,dx+Q\,dy.
$$

### 10.2 Lavagna completa

1. Curva orientata e tangente.
2. Formula parametrica.
3. Forma differenziale.
4. Caso conservativo.
5. Collegamento a Green per curve chiuse.

### 10.3 Frasi da dire mentre scrivo

- "Conta solo la componente tangenziale del campo."
- "Qui il verso e' parte del dato."
- "Se $F=\nabla U$, uso il potenziale."

## 11. Esempio principale da fare

Esempio dei tre cammini:

$$
\int_C 3x^2y\,dx+(x^3+1)\,dy.
$$

Il campo e' conservativo con:

$$
U=x^3y+y.
$$

Quindi da $(0,0)$ a $(1,1)$:

$$
U(1,1)-U(0,0)=2.
$$

## 12. Altri esempi utili

- Campo tangente alla circonferenza.
- Curva chiusa e circuitazione.
- Campo non conservativo con lavoro dipendente dal cammino.
- Campo conservativo calcolato con potenziale.

## 13. Terminologia corretta del professore

### Termini da usare

- curva orientata;
- versore tangente;
- componente tangenziale;
- lavoro;
- forma differenziale;
- circuitazione;
- potenziale.

### Frasi corrette da dire

- "L'integrale cambia segno se inverto il verso."
- "Nel piano posso scriverlo come $P\,dx+Q\,dy$."
- "Se il campo e' conservativo il lavoro dipende solo dagli estremi."

### Termini/frasi da evitare

- "E' come I specie ma con vettori" senza parlare di orientazione.
- Dimenticare il prodotto scalare.
- Dire che ogni integrale di II specie si calcola con potenziale.

## 14. Domande possibili del professore

- Perche' compare $r'(t)$ e non $\|r'(t)\|$?
- Che cosa succede invertendo la curva?
- Come riconosci un campo conservativo?
- Che cosa significa circuitazione?
- Come passi da $F\cdot\tau\,d\ell$ a $P\,dx+Q\,dy$?

## 15. Follow-up e trabocchetti

> I specie: integro una funzione scalare rispetto alla lunghezza.  
> II specie: integro un campo vettoriale lungo la direzione tangente orientata.

- II specie dipende dal verso.
- La componente normale non fa lavoro.
- Se $F=\nabla U$, non serve parametrizzare il cammino.

## Collegamenti utili nella KB

- [[campi_conservativi_discorso_completo]]: potenziale e indipendenza dal cammino.
- [[green_discorso_completo]]: circuitazione su curva chiusa.
- [[stokes_discorso_completo]]: circuitazione come bordo di superficie.
- [[integrali_linea_I_specie_discorso_completo]]: confronto con integrale scalare.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[integrali_linea_II_specie]]
- [[campi_vettoriali]]
- [[campi_conservativi]]
- [[formula_green]]
- `04_theory/01_curve_e_integrali_di_linea/integrali_linea_II_specie.md`
- `04_theory/02_campi_vettoriali/campi_vettoriali.md`

### Theorem cards

- [[integrale_linea_seconda_specie]]
- [[forme_differenziali]]
- [[campi_conservativi]]

### Discorsi collegati

- [[integrali_linea_I_specie_discorso_completo]]
- [[campi_conservativi_discorso_completo]]
- [[green_discorso_completo]]

### Esercizi

- [[integrali_linea_II_specie]]
- [[campi_conservativi_green]]
- `07_exercises/esercizi_per_topic/integrali_linea_II_specie.md`

### Esami ufficiali

- [[2023_04_13]]
- [[2022_11_22]]
- [[2022_09_24_or_27]]

### Figure / visual

- `08_visuals/figures/oral_linea_II_tangente.png`
- `08_visuals/figures/lezione_8_slide_09_campo_circonferenza_vettori.png`

## 18. Errori da evitare

- Usare $\|r'(t)\|$ al posto di $r'(t)$ nella formula di II specie.
- Dimenticare l'orientazione.
- Confondere lavoro e massa.
- Usare il potenziale senza verificare conservativita'.

## 19. Mini ripasso finale

II specie = lavoro di un campo lungo una curva orientata. Formula: $\int F(r(t))\cdot r'(t)dt$. Se il campo e' conservativo, si usa il potenziale; se la curva e' chiusa, compare la circuitazione.

## 20. Checklist personale

- [ ] So spiegare il prodotto scalare tangenziale.
- [ ] So distinguere I e II specie.
- [ ] So fare l'esempio del potenziale $x^3y+y$.
- [ ] So dire cosa cambia invertendo il verso.
- [ ] So collegare a Green.
