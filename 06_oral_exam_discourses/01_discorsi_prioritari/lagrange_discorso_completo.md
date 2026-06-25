# Discorso orale - Moltiplicatori di Lagrange

## Stato e navigazione rapida

- Priorita' orale: altissima.
- Stato: master file potenziato.
- Fonti: `01_sources/official_slides/05_lagrange.pdf`.
- Teoria base: [[lagrange_un_vincolo_curve]], [[lagrange_un_vincolo_superfici]], [[lagrange_due_vincoli]], [[massimi_minimi_assoluti]], [[funzione_implicita]].
- Discorsi collegati: [[massimi_minimi_discorso_completo]], [[funzione_implicita_discorso_completo]], [[curve_superfici_discorso_completo]].
- Lavagna rapida: `06_oral_exam_discourses/04_lavagna/lavagna_lagrange.md`.

## 0. Mappa del discorso

1. Distinguo ottimizzazione libera e vincolata.
2. Spiego curva/superficie di livello e gradiente normale.
3. Enuncio il caso a un vincolo.
4. Generalizzo a due vincoli.
5. Dico che Lagrange produce candidati, non conclusioni automatiche.
6. Collego a Weierstrass e funzione implicita.

## 1. Obiettivo del discorso

Mostrare che in un estremo vincolato regolare la funzione non varia lungo le direzioni ammissibili, quindi il gradiente di $f$ deve stare nello spazio normale al vincolo.

## Tempo stimato

- Versione essenziale: 8 minuti
- Versione completa con dimostrazione geometrica: 13 minuti
- Estensioni/domande su due vincoli, Weierstrass e punti non regolari: 5 minuti

Totale realistico: 13-18 minuti.

## Discorso principale

> "Partirei distinguendo il problema libero dal problema vincolato. In un problema libero posso cercare punti con $\nabla f=0$, ma con un vincolo non tutte le direzioni sono ammissibili."

> "Nel punto di estremo vincolato la funzione non deve variare lungo le direzioni tangenti al vincolo. Quindi il gradiente di $f$ deve essere normale allo spazio tangente."

"gradiente di f uguale lambda gradiente di g"

$$
\nabla f(P)=\lambda\nabla g(P),\qquad g(P)=0.
$$

> "Questa e' una condizione necessaria: Lagrange produce candidati. Per concludere massimo o minimo devo poi confrontare i valori e controllare eventuali bordi o punti non regolari."

## 2. Prerequisiti da sapere

- Gradiente e curve di livello: [[gradiente_derivata_direzionale_discorso]].
- Estremi assoluti e Weierstrass: [[massimi_minimi_discorso_completo]], [[weierstrass_massimi_minimi_assoluti]].
- Teorema della funzione implicita: [[funzione_implicita_discorso_completo]].
- Superfici e normali: [[curve_superfici_discorso_completo]].

## 3. Definizioni richiamate

- Vincolo: equazione $g=0$ o sistema $g_1=g_2=0$.
- Vincolo regolare: gradiente del vincolo non nullo, o gradienti dei vincoli indipendenti.
- Gradiente: direzione di massima crescita, normale alle superfici di livello.
- Spazio tangente: direzioni ammesse dal vincolo.
- Spazio normale: direzioni ortogonali allo spazio tangente.
- Moltiplicatore: coefficiente nella combinazione lineare dei gradienti dei vincoli.
- Candidato: punto che soddisfa le condizioni necessarie.

## 4. Versione da 30 secondi

Se $P$ e' un estremo vincolato regolare di $f$ con vincolo $g=0$, allora:

$$
\nabla f(P)=\lambda\nabla g(P),\qquad g(P)=0.
$$

Con due vincoli:

$$
\nabla f(P)=\lambda\nabla g_1(P)+\mu\nabla g_2(P).
$$

Queste sono condizioni necessarie: poi devo confrontare i valori e controllare bordi o punti non regolari.

## 5. Copione da dire quasi a memoria

"Nel problema vincolato non posso imporre semplicemente $\nabla f=0$, perche' non tutte le direzioni sono ammissibili. In un estremo vincolato la derivata di $f$ deve essere nulla lungo ogni direzione tangente al vincolo. Quindi $\nabla f$ e' ortogonale allo spazio tangente. Ma anche il gradiente del vincolo e' normale al vincolo: per un vincolo regolare ottengo $\nabla f=\lambda\nabla g$. Con due vincoli lo spazio normale e' generato da $\nabla g_1$ e $\nabla g_2$."

## 6. Enunciato formale / definizione formale

Un vincolo:

$$
\nabla f(P)=\lambda\nabla g(P),\qquad g(P)=0,\qquad \nabla g(P)\ne 0.
$$

Due vincoli:

$$
\nabla f(P)=\lambda\nabla g_1(P)+\mu\nabla g_2(P),\qquad g_1(P)=g_2(P)=0,
$$

con $\nabla g_1(P)$ e $\nabla g_2(P)$ indipendenti.

## 7. Spiegazione geometrica o intuitiva

Nel piano, il vincolo $g=0$ e' una curva. In un punto di massimo o minimo vincolato, una curva di livello di $f$ tocca il vincolo senza attraversarlo: le due curve sono tangenti e quindi i loro gradienti, normali alle curve, sono paralleli.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo A - Dimostrazione da esame

### 8.1 Versione breve

Prendo una curva regolare $\gamma(t)$ contenuta nel vincolo e passante per $P$. La funzione $f(\gamma(t))$ ha estremo in $t_0$, quindi:

$$
\frac{d}{dt}f(\gamma(t_0))=\nabla f(P)\cdot\gamma'(t_0)=0.
$$

Allora $\nabla f(P)$ e' ortogonale a tutte le tangenti ammissibili, quindi appartiene allo spazio normale.

### 8.2 Versione completa

Per un vincolo regolare, il teorema della funzione implicita garantisce localmente una curva o superficie regolare di livello. Lo spazio tangente e' il nucleo della derivata del vincolo. Se $\nabla f$ e' nullo su tutte le direzioni tangenti, allora e' nel complemento normale generato da $\nabla g$. Nel caso di due vincoli, il tangente e' l'intersezione dei nuclei e il normale e' generato da $\nabla g_1,\nabla g_2$.

### 8.3 Dove il professore puo' interrompere

- "Lagrange da' condizioni necessarie o sufficienti?"
- "Perche' serve la regolarita' del vincolo?"
- "Che cosa succede se il vincolo ha bordo?"
- "Come colleghi Lagrange alla funzione implicita?"

## 9. Rappresentazione grafica

### 9.1 Disegno minimo da lavagna

Disegna una curva vincolo $g=0$. Disegna alcune curve di livello di $f$. Nel punto di estremo fai vedere una curva di livello tangente al vincolo. Disegna $\nabla f$ e $\nabla g$ normali e paralleli.

### 9.2 Disegno completo

Per due vincoli, disegna due superfici $g_1=0$ e $g_2=0$ che si intersecano lungo una curva. Il vettore $\nabla f$ deve stare nel piano normale generato da $\nabla g_1$ e $\nabla g_2$.

### 9.3 Figure ufficiali collegate

- `08_visuals/figures/oral_lagrange_gradienti_paralleli.png`
- `08_visuals/figures/lezione_5_slide_05_gradiente_curva_livello.png`
- `08_visuals/figures/lezione_5_slide_19_gradiente_superficie_livello.png`
- `08_visuals/figures/lezione_5_slide_34_due_vincoli.png`

### 9.4 Link a visualizzazioni

- `08_visuals/visual_index.md`, sezione "Moltiplicatori di Lagrange".

## 10. Cosa scrivere alla lavagna

### 10.1 Lavagna corta

$$
\nabla f=\lambda\nabla g,\qquad g=0.
$$

$$
\nabla f=\lambda\nabla g_1+\mu\nabla g_2,\qquad g_1=g_2=0.
$$

### 10.2 Lavagna completa

1. Disegno livelli di $f$ e vincolo.
2. Scrivo "derivate tangenziali nulle".
3. Scrivo il sistema di Lagrange.
4. Scrivo "candidati -> confronto valori".

### 10.3 Frasi da dire mentre scrivo

- "Il gradiente e' normale alle curve di livello."
- "Il vincolo regolare ha uno spazio tangente ben definito."
- "Lagrange non conclude massimo/minimo: produce candidati."

## 11. Esempio principale da fare

Massimizzare $f=ax+by+cz$ su $x^2+y^2+z^2=R^2$.

$$
\nabla f=(a,b,c),\qquad \nabla g=(2x,2y,2z).
$$

Il punto di massimo e':

$$
R\frac{(a,b,c)}{\sqrt{a^2+b^2+c^2}},
$$

e il massimo vale:

$$
R\sqrt{a^2+b^2+c^2}.
$$

Il minimo e' l'opposto.

## 12. Altri esempi utili

- Massimo di $xyz$ con $x+y+z=1$.
- Distanza punto-retta o punto-piano.
- Due vincoli: intersezione di superfici.
- Frontiera di dominio chiuso: studio interno, bordo e confronto.

## 13. Terminologia corretta del professore

### Termini da usare

- vincolo regolare;
- moltiplicatore di Lagrange;
- candidato;
- direzione tangente;
- spazio normale;
- condizione necessaria;
- compattezza.

### Frasi corrette da dire

- "Il metodo fornisce candidati, poi confronto i valori."
- "La regolarita' serve per avere un tangente ben definito."
- "Con due vincoli il gradiente di $f$ sta nello span dei gradienti dei vincoli."

### Termini/frasi da evitare

- "Lagrange trova il massimo" senza confronto.
- "Devo imporre $\nabla f=0$" in un problema vincolato.
- "Il vincolo non regolare non importa."

## 14. Domande possibili del professore

- Lagrange da' condizioni necessarie o sufficienti?
- Perche' serve regolarita' del vincolo?
- Che succede se il vincolo ha bordo?
- Perche' compare una combinazione lineare con due vincoli?
- Come colleghi Lagrange al teorema della funzione implicita?

## 15. Follow-up e trabocchetti

- Se $\nabla g=0$, il metodo puo' non applicarsi.
- Se il dominio e' compatto, Weierstrass garantisce esistenza, ma non identifica i punti.
- Se c'e' bordo, va studiato separatamente.
- Con due vincoli bisogna controllare indipendenza dei gradienti.

## Collegamenti utili nella KB

- [[massimi_minimi_discorso_completo]]: estremi assoluti e confronto valori.
- [[funzione_implicita_discorso_completo]]: regolarita' del vincolo.
- [[curve_superfici_discorso_completo]]: tangenti e normali.
- [[weierstrass_massimi_minimi_assoluti]]: esistenza su compatti.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[lagrange_un_vincolo_curve]]
- [[lagrange_un_vincolo_superfici]]
- [[lagrange_due_vincoli]]
- [[massimi_minimi_assoluti]]
- [[funzione_implicita]]
- `04_theory/05_massimi_minimi_e_lagrange/lagrange_un_vincolo_superfici.md`
- `04_theory/05_massimi_minimi_e_lagrange/lagrange_due_vincoli.md`

### Theorem cards

- [[lagrange]]
- [[lagrange_un_vincolo_superfici]]
- [[lagrange_due_vincoli]]
- [[weierstrass_massimi_minimi_assoluti]]

### Discorsi collegati

- [[massimi_minimi_discorso_completo]]
- [[funzione_implicita_discorso_completo]]
- [[curve_superfici_discorso_completo]]

### Esercizi

- [[lagrange_esami]]
- [[lagrange_ottimizzazione_vincolata]]
- [[massimi_minimi_assoluti]]

### Esami ufficiali

- [[2023_04_13]]
- [[2022_07_14]]
- [[2022_11_22]]
- [[2023_02_22]]
- [[2022_09_24_or_27]]

### Figure / visual

- `08_visuals/figures/oral_lagrange_gradienti_paralleli.png`
- `08_visuals/figures/lezione_5_slide_34_due_vincoli.png`

## 18. Errori da evitare

- Non aggiungere il vincolo al sistema.
- Non confrontare i valori finali.
- Trattare condizioni necessarie come sufficienti.
- Ignorare punti non regolari.

## 19. Mini ripasso finale

Lagrange = estremo vincolato regolare -> derivata nulla lungo le tangenti -> gradiente di $f$ nello spazio normale. Produce candidati; la conclusione richiede confronto e controllo dei casi esclusi.

## 20. Checklist personale

- [ ] So disegnare livelli tangenti al vincolo.
- [ ] So spiegare uno e due vincoli.
- [ ] So dire "necessaria, non sufficiente".
- [ ] So collegare a Weierstrass.
- [ ] So fare l'esempio della funzione lineare sulla sfera.
