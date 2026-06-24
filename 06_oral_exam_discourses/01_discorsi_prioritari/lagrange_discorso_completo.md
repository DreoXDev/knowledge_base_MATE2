# Discorso orale - Moltiplicatori di Lagrange

## Stato

- Priorita' orale: altissima
- Fonte principale: `01_sources/official_slides/05_lagrange.pdf`
- Note collegate: `04_theory/05_massimi_minimi_e_lagrange/lagrange_un_vincolo_superfici.md`, `04_theory/05_massimi_minimi_e_lagrange/lagrange_due_vincoli.md`
- Esercizi collegati: `07_exercises/exam_official/lagrange_esami.md`

## 1. Obiettivo del discorso

Spiegare Lagrange come condizione necessaria per trovare candidati a estremi vincolati. L'idea geometrica e' che, nel punto di estremo, la funzione non puo' variare lungo le direzioni tangenti al vincolo.

## 2. Versione da 30 secondi

Con un vincolo $g=0$, se $P$ e' un punto regolare di estremo vincolato, allora:

$$
\nabla f(P)=\lambda\nabla g(P)
$$

Con due vincoli:

$$
\nabla f=\lambda\nabla g_1+\mu\nabla g_2
$$

Poi si confrontano i valori sui candidati.

## 3. Versione completa da orale

Quando ottimizzo $f$ su un vincolo, non devo imporre $\nabla f=0$ come nel caso libero. Devo imporre che la derivata di $f$ sia nulla lungo le direzioni ammesse dal vincolo. Siccome il gradiente e' normale alle superfici di livello, nel caso di un vincolo regolare la normale a $f$ deve essere parallela alla normale del vincolo. Da qui nasce $\nabla f=\lambda\nabla g$.

## 4. Enunciato formale

Un vincolo:

$$
\nabla f=\lambda\nabla g,\qquad g=0
$$

Due vincoli:

$$
\nabla f=\lambda\nabla g_1+\mu\nabla g_2,\qquad g_1=0,\quad g_2=0
$$

## 5. Dimostrazione / idea di dimostrazione

### Idea intuitiva

Nel caso di una curva vincolo, le direzioni ammesse sono tangenti al vincolo. In un estremo vincolato la derivata direzionale di $f$ lungo ogni tangente e' nulla, quindi $\nabla f$ e' ortogonale a tutte le tangenti. Ma anche $\nabla g$ e' ortogonale al vincolo. Quindi i due gradienti sono paralleli.

Per due vincoli in $\mathbb{R}^3$, la curva ammissibile e' intersezione di due superfici: lo spazio normale e' generato da $\nabla g_1$ e $\nabla g_2$.

## 6. Rappresentazione grafica / intuizione geometrica

Disegnare curve di livello di $f$ tangenti alla curva vincolo. Il punto di estremo e' dove la curva di livello "tocca" il vincolo senza attraversarlo.

Figure utili:
- `08_visuals/figures/lezione_5_slide_05_gradiente_curva_livello.png`
- `08_visuals/figures/lezione_5_slide_19_gradiente_superficie_livello.png`

## 7. Cosa scrivere alla lavagna

### Un vincolo

$$
\nabla f=\lambda\nabla g,\qquad g=0
$$

### Due vincoli

$$
\nabla f=\lambda\nabla g_1+\mu\nabla g_2,\qquad g_1=0,\quad g_2=0
$$

Poi disegno curve di livello e vincolo.

## 8. Cosa dire a voce

"Lagrange non mi garantisce automaticamente massimo o minimo: mi fornisce candidati. Per gli estremi assoluti devo usare compattezza, confrontare i valori e controllare eventuali bordi o punti non regolari."

## 9. Esempi da fare

- Funzione lineare su sfera: il massimo sta nella direzione del vettore dei coefficienti.
- Massimo di $xyz$ con $x+y+z=1$: candidato $x=y=z=\frac{1}{3}$.
- Distanza da retta intersezione di piani: si puo' ridurre o usare due vincoli.

## 10. Terminologia corretta

Usare: vincolo regolare, gradiente normale, candidato, estremo vincolato, compattezza.

Evitare: "Lagrange trova il massimo" senza dire che trova candidati.

## 11. Domande possibili del professore

- Perche' i gradienti sono paralleli?
- Che cosa succede se $\nabla g=0$?
- Lagrange da' condizioni sufficienti?
- Come si usa con due vincoli?
- Come si collega a Weierstrass?

## 12. Follow-up e trabocchetti

- Se il dominio ha bordo, bisogna controllarlo.
- Se il vincolo non e' regolare, Lagrange puo' non applicarsi.
- Con due vincoli servono due moltiplicatori.

## 13. Collegamenti con altri argomenti

- [[weierstrass_discorso]]
- [[massimi_minimi_discorso_completo]]
- [[funzione_implicita_discorso_completo]]

## 14. Errori da evitare

- Imporre $\nabla f=0$ in un problema vincolato.
- Non aggiungere il vincolo al sistema.
- Non confrontare i valori finali.

## 15. Mini ripasso finale

Lagrange: in un estremo vincolato la derivata lungo le tangenti al vincolo e' nulla. Quindi $\nabla f$ appartiene allo spazio normale del vincolo. Con un vincolo e' parallelo a $\nabla g$; con due vincoli e' combinazione di $\nabla g_1,\nabla g_2$.

## 16. Checklist personale

- [ ] So spiegare l'intuizione geometrica.
- [ ] So scrivere uno e due vincoli.
- [ ] So dire che non e' sufficiente.
- [ ] So fare esempio su sfera.
