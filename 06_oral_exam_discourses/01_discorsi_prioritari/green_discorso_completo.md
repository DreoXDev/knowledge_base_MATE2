# Discorso orale - Formula di Green

## Stato

- Priorita' orale: altissima
- Fonte principale: `01_sources/official_slides/09_campi_conservativi_green.pdf`
- Note collegate: `04_theory/06_teoremi_integrali/formula_green.md`
- Esercizi collegati: `07_exercises/exam_official/green_esami.md`

## 1. Obiettivo del discorso

Spiegare che Green collega la circuitazione di un campo piano lungo il bordo di un dominio con l'integrale doppio del rotore scalare nel dominio. Il punto delicato e' l'orientazione positiva della frontiera.

## 2. Versione da 30 secondi

La formula di Green dice che, per $F=(P,Q)$ e $C=\partial D$ orientata positivamente:

$$
\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy
$$

Trasforma una circuitazione sul bordo in un integrale doppio sul dominio.

## 3. Versione completa da orale

Considero un dominio piano $D$ con bordo $C$ regolare a tratti, orientato positivamente, cioe' percorso in modo che il dominio resti a sinistra. Se $P$ e $Q$ hanno derivate parziali continue, allora la circuitazione del campo $F=(P,Q)$ lungo $C$ e' uguale all'integrale su $D$ della quantita' $Q_x-P_y$, che e' il rotore scalare del campo piano. Geometricamente Green somma le rotazioni locali del campo dentro il dominio e ottiene l'effetto globale lungo il bordo.

## 4. Enunciato formale

Se $D\subset\mathbb{R}^2$ e' un dominio piano semplice, $C=\partial D$ e' orientata positivamente, e $P,Q$ sono di classe $C^1$, allora:

$$
\oint_C P\,dx+Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy
$$

## 5. Dimostrazione / idea di dimostrazione

### Dimostrazione completa

Per domini normali si dimostrano separatamente:

$$
\iint_D P_y\,dx\,dy=-\int_C P\,dx
$$

e:

$$
\iint_D Q_x\,dx\,dy=\int_C Q\,dy
$$

Sommando:

$$
\int_C P\,dx+\int_C Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy
$$

Per domini piu' generali si suddivide il dominio in pezzi normali. I contributi sui bordi interni si cancellano perche' vengono percorsi in versi opposti.

### Idea intuitiva

Il bordo misura l'effetto complessivo; l'integrale doppio somma le rotazioni infinitesime interne. I contributi interni si annullano e resta solo il bordo esterno.

## 6. Rappresentazione grafica / intuizione geometrica

Disegnare un dominio orientato in senso antiorario e indicare "dominio a sinistra". Per domini con buchi, il bordo esterno e' antiorario e i bordi interni sono orari.

Figure utili:
- `08_visuals/figures/lezione_9_slide_20_orientazione_frontiera.png`
- `08_visuals/figures/lezione_9_slide_26_contributi_interni.png`

## 7. Cosa scrivere alla lavagna

1. $F=(P,Q)$, $C=\partial D$ orientata positivamente.
2. Formula:

$$
\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy
$$

3. Disegno dominio con freccia antioraria.
4. Due identita':

$$
\iint_D P_y\,dx\,dy=-\int_C P\,dx,\qquad
\iint_D Q_x\,dx\,dy=\int_C Q\,dy
$$

5. Somma finale.

## 8. Cosa dire a voce

"Green e' utile per passare da un integrale di linea lungo una curva chiusa a un integrale doppio sul dominio. L'orientazione positiva e' fondamentale: se inverto il verso, cambia il segno."

## 9. Esempi da fare

- Triangolo ufficiale: risultato $-1$.
- Quadrato ruotato: se $Q_x-P_y=2$ e area $2$, risultato $4$.
- Circonferenza con $F=(x^2y,-xy^2)$:

$$
Q_x-P_y=-(x^2+y^2)
$$

e sul disco di raggio $R$:

$$
\oint_C F\cdot\tau\,d\ell=-\frac{\pi R^4}{2}
$$

## 10. Terminologia corretta

Usare: orientazione positiva, circuitazione, rotore scalare, dominio a sinistra, frontiera.

Evitare: "area del bordo" o "rotore vettoriale nel piano" senza chiarire la componente scalare.

## 11. Domande possibili del professore

- Che cosa significa orientazione positiva?
- Perche' compare $Q_x-P_y$?
- Che collegamento c'e' con Stokes?
- Che succede se il dominio ha buchi?
- Se $Q_x-P_y=0$, cosa concludo?

## 12. Follow-up e trabocchetti

- Se si percorre $C$ in verso opposto, il segno cambia.
- Se il dominio ha buchi, le frontiere interne sono orientate in senso opposto.
- $Q_x-P_y=0$ implica circuitazione nulla su curve chiuse adatte, ma il discorso va collegato alle ipotesi sul dominio.

## 13. Collegamenti con altri argomenti

- [[stokes_discorso_completo]]
- [[campi_conservativi_discorso_completo]]
- [[integrali_linea_II_specie_discorso_completo]]

## 14. Errori da evitare

- Dimenticare l'orientazione.
- Scrivere $P_y-Q_x$ invece di $Q_x-P_y$.
- Usare Green senza verificare regolarita' e curva chiusa.

## 15. Mini ripasso finale

Green: bordo chiuso, dominio a sinistra, formula con $Q_x-P_y$. Dimostrazione: due identita' separate e cancellazione dei bordi interni. Collegamento: e' il caso piano di Stokes.

## 16. Checklist personale

- [ ] So enunciare.
- [ ] So spiegare orientazione positiva.
- [ ] So dimostrare con le due identita'.
- [ ] So fare un esempio.
- [ ] So collegarlo a Stokes.
