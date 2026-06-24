# Discorso orale - Formula di Gauss-Ostrogradski

## Stato

- Priorita' orale: altissima
- Fonte principale: `01_sources/official_slides/11_calcolo_vettoriale.pdf`
- Note collegate: `04_theory/06_teoremi_integrali/formula_gauss_ostrogradski.md`
- Esercizi collegati: `07_exercises/esercizi_per_topic/gauss_ostrogradski.md`

## 1. Obiettivo del discorso

Spiegare che Gauss collega il flusso uscente da una superficie chiusa con l'integrale della divergenza nel volume interno.

## 2. Versione da 30 secondi

Se $S=\partial\Omega$ e $n$ e' la normale uscente:

$$
\iint_SF\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

## 3. Versione completa da orale

La divergenza misura sorgenti e pozzi locali. Integrandola su tutto il volume ottengo la produzione totale di campo; questa deve coincidere con il flusso uscente attraverso la frontiera chiusa.

## 4. Enunciato formale

Se $\Omega$ e' un dominio semplice limitato con frontiera $S=\partial\Omega$ differenziabile a tratti, e $F$ e' regolare, allora:

$$
\iint_{\partial\Omega}F\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

con $n$ normale uscente.

## 5. Dimostrazione / idea di dimostrazione

### Dimostrazione completa

Si dimostra per componenti. Per $F_3e_3$, se:

$$
z_1(x,y)\leq z\leq z_2(x,y)
$$

il flusso sulle parti laterali verticali non contribuisce alla componente $e_3$. Restano grafico inferiore e superiore:

$$
\iint_D \left[F_3(x,y,z_2)-F_3(x,y,z_1)\right]\,dx\,dy
$$

che coincide con:

$$
\iint_D\int_{z_1}^{z_2}\frac{\partial F_3}{\partial z}\,dz\,dx\,dy
$$

per il teorema fondamentale del calcolo. Si ripete per $F_1$ e $F_2$ e si somma.

## 6. Rappresentazione grafica / intuizione geometrica

Disegnare una superficie chiusa con frecce normali uscenti. Per un guscio, sulla sfera interna la normale uscente punta verso il centro.

Figura utile:
- `08_visuals/figures/lezione_11_slide_42_normale_sfera.png`

## 7. Cosa scrivere alla lavagna

1. Superficie chiusa $S=\partial\Omega$.
2. Normale uscente.
3. Formula.
4. Divergenza:

$$
\operatorname{div}F=F_{1x}+F_{2y}+F_{3z}
$$

5. Schema dimostrazione per $F_3$.

## 8. Cosa dire a voce

"Gauss e' il teorema naturale del flusso: se conosco la divergenza nel volume, evito spesso un integrale superficiale difficile."

## 9. Esempi da fare

- $F=(x,y,z)$ su sfera: $4\pi R^3$.
- $F=(x^3,y^3,z^3)$ su sfera: $\frac{12}{5}\pi R^5$.
- Campo $r/r^3$ su guscio: flusso totale $0$.

## 10. Terminologia corretta

Usare: superficie chiusa, normale uscente, divergenza, flusso uscente, sorgenti/pozzi.

## 11. Domande possibili del professore

- Perche' normale uscente?
- Differenza tra Stokes e Gauss?
- Che cos'e' un campo solenoidale?
- Cosa succede se la superficie non e' chiusa?

## 12. Follow-up e trabocchetti

- Gauss non si applica direttamente a superfici aperte.
- Nei gusci la normale interna cambia verso.
- Divergenza nulla significa flusso totale nullo su superfici chiuse nel dominio.

## 13. Collegamenti con altri argomenti

- [[flusso_discorso]]
- [[campi_solenoidali_discorso_completo]]
- [[rotore_divergenza_discorso_completo]]

## 14. Errori da evitare

- Usare normale entrante.
- Dimenticare che la superficie deve essere chiusa.
- Confondere rotore e divergenza.

## 15. Mini ripasso finale

Gauss: superficie chiusa, normale uscente, flusso uguale integrale della divergenza. Dimostrazione per componenti usando il teorema fondamentale del calcolo.

## 16. Checklist personale

- [ ] So enunciare.
- [ ] So spiegare divergenza.
- [ ] So fare idea di dimostrazione.
- [ ] So fare esempio sfera.
