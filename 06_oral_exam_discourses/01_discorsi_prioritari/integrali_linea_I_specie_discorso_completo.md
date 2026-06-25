# Discorso orale - Integrali di linea di I specie

## Stato e navigazione rapida

- Priorita' orale: alta.
- Stato: master file potenziato.
- Fonti: `01_sources/official_slides/07_integrali_linea_I_specie.pdf`.
- Teoria base: [[integrali_linea_I_specie]], [[ascissa_curvilinea]], [[lunghezza_arco_curva]], [[baricentro_filo]].
- Discorsi collegati: [[integrali_linea_II_specie_discorso_completo]], [[curve_superfici_discorso_completo]].
- Lavagna rapida: `06_oral_exam_discourses/04_lavagna/lavagna_integrali_linea.md`.

## 0. Mappa del discorso

Curva parametrizzata -> lunghezza infinitesima $d\ell$ -> integrale di una funzione scalare lungo la curva -> interpretazioni: massa, area verticale, baricentro -> confronto con II specie.

## 1. Obiettivo del discorso

Spiegare che l'integrale di I specie misura la somma pesata di una funzione scalare lungo una curva, usando la lunghezza come elemento di integrazione.

## Tempo stimato

- Versione essenziale: 7 minuti
- Versione completa con costruzione da somme e interpretazioni: 12 minuti
- Estensioni/domande su parametrizzazione, massa e baricentro: 4 minuti

Totale realistico: 12-16 minuti.

## Discorso principale

> "Partirei dall'idea geometrica: sto integrando una funzione scalare lungo una curva, pesando ogni valore con un piccolo elemento di lunghezza."

> "Se la curva e' parametrizzata da $r(t)$, l'elemento di lunghezza e' la norma della velocita' per $dt$."

"d ell uguale norma di r primo di t dt"

$$
d\ell=\|r'(t)\|\,dt.
$$

"integrale su C di f d ell"

$$
\int_C f\,d\ell
=
\int_a^b f(r(t))\|r'(t)\|\,dt.
$$

> "A differenza della seconda specie, qui il verso di percorrenza non cambia il risultato, perche' compare una lunghezza e non una direzione orientata."

## 2. Prerequisiti da sapere

- Curve parametrizzate: [[curve_parametrizzate_discorso]].
- Lunghezza arco: [[lunghezza_arco_curva]].
- Ascissa curvilinea: [[ascissa_curvilinea]].
- Integrali di II specie per confronto: [[integrali_linea_II_specie_discorso_completo]].

## 3. Definizioni richiamate

- Curva regolare: parametrizzazione $r(t)$ con $r'(t)\ne 0$.
- Elemento di lunghezza: $d\ell=\|r'(t)\|dt$.
- Ascissa curvilinea: parametro naturale dato dalla lunghezza percorsa.
- Integrale di I specie: integrale di una funzione scalare rispetto a $d\ell$.
- Baricentro di un filo: media pesata delle coordinate lungo la curva.

## 4. Versione da 30 secondi

Se $C$ e' parametrizzata da $r(t)$, allora:

$$
\int_C f\,d\ell=\int_a^b f(r(t))\|r'(t)\|\,dt.
$$

Integro una funzione scalare lungo la curva, pesando ogni punto con l'elemento di lunghezza. Non dipende dall'orientazione della curva.

## 5. Copione da dire quasi a memoria

"L'integrale di linea di I specie nasce come limite di somme $\sum f(P_i)\Delta\ell_i$. Quindi non sto integrando rispetto a $dx$ o $dy$, ma rispetto alla lunghezza dell'arco. Se parametrizzo la curva con $r(t)$, l'elemento di lunghezza e' $\|r'(t)\|dt$, e ottengo la formula operativa. Serve per lunghezze, masse di fili, aree verticali sopra una curva e baricentri."

## 6. Enunciato formale / definizione formale

Per $C:r(t)$, $t\in[a,b]$:

$$
\int_C f\,d\ell=\int_a^b f(r(t))\|r'(t)\|\,dt.
$$

Se $f=1$:

$$
L(C)=\int_C 1\,d\ell.
$$

## 7. Spiegazione geometrica o intuitiva

La curva viene spezzata in piccoli archi $\Delta\ell_i$. In ogni punto scelgo un valore $f(P_i)$ e sommo $f(P_i)\Delta\ell_i$. Se $f$ e' densita', ottengo massa; se $f\ge 0$ sopra una curva piana, ottengo l'area di una parete verticale.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo A - Costruzione da somme

### 8.1 Versione breve

Si parte dalle somme:

$$
\sum_i f(P_i)\Delta\ell_i.
$$

Passando al limite e usando $\Delta\ell\sim \|r'(t)\|\Delta t$ si ottiene la formula parametrica.

### 8.2 Versione completa

Per una partizione di $[a,b]$, la lunghezza del pezzetto di curva e' approssimata da $\|r'(t_i)\|\Delta t_i$. Sostituendo nelle somme di Riemann:

$$
\sum_i f(r(t_i))\|r'(t_i)\|\Delta t_i
$$

e passando al limite si ottiene l'integrale.

### 8.3 Dove il professore puo' interrompere

- "Dipende dalla parametrizzazione?"
- "Dipende dall'orientazione?"
- "Che differenza c'e' con la II specie?"
- "Che cosa rappresenta $d\ell$?"

## 9. Rappresentazione grafica

### 9.1 Disegno minimo da lavagna

Disegna una curva $C$, dividila in piccoli archi $\Delta\ell_i$, scegli punti $P_i$ e scrivi:

$$
\sum_i f(P_i)\Delta\ell_i.
$$

### 9.2 Disegno completo

Disegna una curva nel piano e una parete sopra la curva di altezza $f$. Se $f\ge 0$, l'integrale misura l'area di questa superficie verticale.

### 9.3 Figure ufficiali collegate

- `08_visuals/figures/oral_linea_I_somme.png`
- `08_visuals/figures/lezione_7_slide_02_suddivisione_curva.png`
- `08_visuals/figures/lezione_7_slide_04_ascissa_curvilinea.png`
- `08_visuals/figures/lezione_7_slide_09_area.png`
- `08_visuals/figures/lezione_7_slide_10_semicirconferenza.png`

### 9.4 Link a visualizzazioni

- `08_visuals/visual_index.md`, sezione "Integrali di linea di I specie".

## 10. Cosa scrivere alla lavagna

### 10.1 Lavagna corta

$$
d\ell=\|r'(t)\|dt,\qquad
\int_C f\,d\ell=\int_a^b f(r(t))\|r'(t)\|dt.
$$

### 10.2 Lavagna completa

1. Somma $\sum f(P_i)\Delta\ell_i$.
2. Formula parametrica.
3. Caso $f=1$.
4. Interpretazione massa/area.
5. Box confronto con II specie.

### 10.3 Frasi da dire mentre scrivo

- "Qui la curva non e' orientata."
- "La norma della velocita' trasforma $dt$ in lunghezza."
- "Sto integrando una funzione scalare."

## 11. Esempio principale da fare

Semicirconferenza:

$$
\int_C xy^4\,d\ell,
$$

con:

$$
x=4\cos t,\qquad y=4\sin t,\qquad d\ell=4\,dt.
$$

Quindi si sostituisce:

$$
\int_C xy^4\,d\ell=\int_0^\pi (4\cos t)(4\sin t)^4\,4\,dt.
$$

## 12. Altri esempi utili

- Lunghezza di una curva: $f=1$.
- Massa di filo con densita' $\rho$.
- Baricentro: $\bar{x}=\frac{1}{m}\int_C x\rho\,d\ell$.
- Quarto di ellisse o curva piana ufficiale.

## 13. Terminologia corretta del professore

### Termini da usare

- elemento di lunghezza;
- ascissa curvilinea;
- funzione scalare;
- curva regolare;
- massa di un filo;
- baricentro.

### Frasi corrette da dire

- "L'integrale di I specie non dipende dal verso di percorrenza."
- "Il fattore $\|r'(t)\|$ e' l'elemento di lunghezza."
- "Se $f=1$ ottengo la lunghezza della curva."

### Termini/frasi da evitare

- "Integro un campo vettoriale."
- "Cambio il verso e cambia segno."
- Dimenticare $\|r'(t)\|$.

## 14. Domande possibili del professore

- Perche' compare la norma di $r'(t)$?
- Che succede se cambio parametrizzazione?
- Perche' il verso non conta?
- Come interpreti l'integrale come area?
- Come ricavi il baricentro?

## 15. Follow-up e trabocchetti

> I specie: integro una funzione scalare rispetto alla lunghezza.  
> II specie: integro un campo vettoriale lungo la direzione tangente orientata.

- In I specie non c'e' prodotto scalare con la tangente.
- In I specie il verso non cambia il segno.
- Se la curva non e' regolare a tratti, la formula va trattata con cautela.

## Collegamenti utili nella KB

- [[integrali_linea_II_specie_discorso_completo]]: confronto strutturale.
- [[curve_parametrizzate_discorso]]: parametrizzazione e velocita'.
- [[superfici_integrali_superficie_discorso]]: analogia con integrali su superfici.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[integrali_linea_I_specie]]
- [[ascissa_curvilinea]]
- [[lunghezza_arco_curva]]
- [[baricentro_filo]]
- `04_theory/01_curve_e_integrali_di_linea/integrali_linea_I_specie.md`
- `04_theory/01_curve_e_integrali_di_linea/lunghezza_arco_curva.md`

### Theorem cards

- [[integrale_linea_prima_specie]]
- [[ascissa_curvilinea]]
- [[baricentro_filo]]

### Discorsi collegati

- [[integrali_linea_II_specie_discorso_completo]]
- [[curve_parametrizzate_discorso]]

### Esercizi

- [[integrali_linea_I_specie]]
- `07_exercises/esercizi_per_topic/integrali_linea_I_specie.md`

### Esami ufficiali

- [[2023_04_13]]
- [[2023_07_19]]

### Figure / visual

- `08_visuals/figures/oral_linea_I_somme.png`
- `08_visuals/figures/lezione_7_slide_09_area.png`
- `08_visuals/figures/lezione_7_slide_10_semicirconferenza.png`

## 18. Errori da evitare

- Dimenticare $\|r'(t)\|$.
- Trattare l'integrale come orientato.
- Confondere funzione scalare e campo vettoriale.
- Usare $dx$ o $dy$ al posto di $d\ell$ senza giustificazione.

## 19. Mini ripasso finale

I specie = somma di valori scalari lungo una curva pesati dalla lunghezza. Formula: $\int f(r(t))\|r'(t)\|dt$. Non dipende dall'orientazione.

## 20. Checklist personale

- [ ] So derivare $d\ell=\|r'(t)\|dt$.
- [ ] So fare la semicirconferenza.
- [ ] So spiegare l'area sopra curva.
- [ ] So distinguere I e II specie.
- [ ] So citare baricentro e massa.
