# Discorso orale - Campi conservativi e potenziale

## Stato

- Priorita' orale: altissima
- Fonte principale: `01_sources/official_slides/08_integrali_linea_II_specie.pdf`, `01_sources/official_slides/09_campi_conservativi_green.pdf`
- Note collegate: `04_theory/03_potenziale_e_campi_conservativi/campi_conservativi.md`

## 1. Obiettivo del discorso

Spiegare cosa significa che un campo e' conservativo, come si usa un potenziale e perche' il dominio conta.

## 2. Versione da 30 secondi

Un campo $F$ e' conservativo se esiste $U$ tale che:

$$
F=\nabla U
$$

Allora:

$$
\int_C F\cdot\tau\,d\ell=U(P_1)-U(P_0)
$$

e l'integrale non dipende dal cammino.

## 3. Versione completa da orale

Un campo conservativo e' un campo che deriva da un potenziale. Questo rende gli integrali di linea facili: dipendono solo dagli estremi. In particolare, su curve chiuse la circuitazione e' nulla. Il criterio locale e' l'irrotazionalita', ma per avere il viceversa serve una condizione sul dominio, come la semplice connessione.

## 4. Enunciato formale

Se $F=\nabla U$, allora per ogni curva regolare $C$ da $P_0$ a $P_1$:

$$
\int_C F\cdot\tau\,d\ell=U(P_1)-U(P_0)
$$

Se $C$ e' chiusa:

$$
\oint_C F\cdot\tau\,d\ell=0
$$

## 5. Dimostrazione / idea di dimostrazione

Parametrizzo $C$ con $r(t)$. Allora:

$$
F(r(t))\cdot r'(t)=\nabla U(r(t))\cdot r'(t)=\frac{d}{dt}U(r(t))
$$

Integrando:

$$
\int_a^b\frac{d}{dt}U(r(t))\,dt=U(r(b))-U(r(a))
$$

## 6. Rappresentazione grafica / intuizione geometrica

Le curve di livello del potenziale sono ortogonali al campo. Il lavoro lungo un percorso dipende solo dal salto di potenziale.

## 7. Cosa scrivere alla lavagna

1. $F=\nabla U$.
2. Formula fondamentale:

$$
\int_C F\cdot\tau\,d\ell=U(P_1)-U(P_0)
$$

3. Circuitazione nulla.
4. Criterio: $\operatorname{rot}F=0$ e dominio semplicemente connesso.
5. Controesempio campo angolare.

## 8. Cosa dire a voce

"Irrotazionale e conservativo non sono la stessa cosa in ogni dominio. Il campo angolare mostra che la topologia del dominio e' fondamentale."

## 9. Esempio da fare

Campo angolare:

$$
F=\left(-\frac{y}{x^2+y^2},\frac{x}{x^2+y^2}\right)
$$

su $\mathbb{R}^2\setminus\{0\}$: e' irrotazionale ma non conservativo, perche' sulla circonferenza unitaria la circuitazione vale $2\pi$.

## 10. Terminologia corretta

Usare: potenziale, conservativo, irrotazionale, circuitazione, semplicemente connesso, forma chiusa/esatta.

## 11. Domande possibili del professore

- Differenza tra conservativo e irrotazionale?
- Come si trova un potenziale?
- Perche' serve la semplice connessione?
- Che cosa dice Poincare?
- Collegamento con Green?

## 12. Follow-up e trabocchetti

- Rotore nullo non basta in domini con buchi.
- Potenziale definito a meno di costante.
- Circuitazione nulla su ogni curva chiusa equivale a indipendenza dal cammino.

## 13. Collegamenti con altri argomenti

- [[green_discorso_completo]]
- [[integrali_linea_II_specie_discorso_completo]]
- [[calcolo_potenziale]]

## 14. Errori da evitare

- Dire che irrotazionale implica sempre conservativo.
- Non specificare il dominio.
- Sbagliare segno nel campo angolare.

## 15. Mini ripasso finale

Conservativo significa $F=\nabla U$. Integrale di linea uguale differenza di potenziale. Circuitazione chiusa nulla. Irrotazionalita' e' criterio locale; per il viceversa serve il dominio.

## 16. Checklist personale

- [ ] So definire potenziale.
- [ ] So dimostrare indipendenza dal cammino.
- [ ] So spiegare Poincare.
- [ ] So fare campo angolare.
