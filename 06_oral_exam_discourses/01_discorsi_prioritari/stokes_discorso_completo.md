# Discorso orale - Formula di Stokes

## Stato

- Priorita' orale: altissima
- Fonte principale: `01_sources/official_slides/11_calcolo_vettoriale.pdf`
- Note collegate: `04_theory/06_teoremi_integrali/formula_stokes.md`
- Esercizi collegati: `07_exercises/esercizi_per_topic/stokes.md`

## 1. Obiettivo del discorso

Spiegare che Stokes generalizza Green alle superfici nello spazio, collegando circuitazione sul bordo e flusso del rotore.

## 2. Versione da 30 secondi

Se $S$ e' orientata e $C=\partial S$, allora:

$$
\oint_C F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

con orientazione compatibile tra $n$ e $C$.

## 3. Versione completa da orale

La formula di Stokes dice che la circuitazione di un campo lungo il bordo di una superficie e' uguale al flusso del rotore attraverso la superficie. Il rotore misura la tendenza locale alla rotazione, mentre la circuitazione misura l'effetto complessivo lungo il bordo.

## 4. Enunciato formale

Se $S$ e' una superficie orientata con bordo $C=\partial S$, e $F$ ha componenti con derivate continue, allora:

$$
\oint_C F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

## 5. Dimostrazione / idea di dimostrazione

### Idea intuitiva

Stokes si puo' pensare come somma di tanti piccoli contributi di Green su pezzetti della superficie. I contributi interni si cancellano e rimane solo il bordo esterno.

## 6. Rappresentazione grafica / intuizione geometrica

Disegnare una superficie con bordo, una normale $n$ e il verso del bordo indotto. Un osservatore orientato secondo $n$, percorrendo $C$, deve avere la superficie a sinistra.

Figure utili:
- `08_visuals/figures/lezione_11_slide_23_stokes_piano.png`
- `08_visuals/figures/lezione_11_slide_32_stokes_emisfero.png`

## 7. Cosa scrivere alla lavagna

1. Disegno $S$, $C=\partial S$, normale $n$.
2. Formula di Stokes.
3. Rotore:

$$
\operatorname{rot}(F)=
\left(F_{3y}-F_{2z},F_{1z}-F_{3x},F_{2x}-F_{1y}\right)
$$

4. Nota su orientazione compatibile.

## 8. Cosa dire a voce

"Stokes e' Green nello spazio: non integro piu' su un dominio piano, ma su una superficie, e al posto di $Q_x-P_y$ compare il rotore."

## 9. Esempi da fare

- Piano $2x+y+z=2$ con $F=(xz,xy,3xz)$: risultato $-1$.
- Emisfero superiore con $F=(y,-x,0)$: risultato $-18\pi$.
- Campo $F=(yz,xz,xy)$: rotore nullo, risultato $0$.

## 10. Terminologia corretta

Usare: bordo orientato, normale scelta, rotore, circuitazione, flusso del rotore.

## 11. Domande possibili del professore

- Che cos'e' il rotore?
- Come scelgo l'orientazione di $C$?
- Green e' davvero un caso particolare?
- Se cambio normale cosa succede?
- La superficie deve essere chiusa?

## 12. Follow-up e trabocchetti

- Superficie con bordo: Stokes.
- Superficie chiusa: spesso Gauss.
- Cambiare normale cambia anche il verso positivo del bordo.

## 13. Collegamenti con altri argomenti

- [[green_discorso_completo]]
- [[rotore_divergenza_discorso_completo]]
- [[gauss_ostrogradski_discorso_completo]]

## 14. Errori da evitare

- Dimenticare l'orientazione compatibile.
- Confondere Stokes con Gauss.
- Applicare Stokes senza bordo.

## 15. Mini ripasso finale

Stokes: bordo di superficie, circuitazione, rotore. Formula: integrale sul bordo uguale flusso del rotore. Orientazione: osservatore secondo $n$ ha $S$ a sinistra.

## 16. Checklist personale

- [ ] So enunciare.
- [ ] So definire rotore.
- [ ] So spiegare orientazione.
- [ ] So collegarlo a Green.
