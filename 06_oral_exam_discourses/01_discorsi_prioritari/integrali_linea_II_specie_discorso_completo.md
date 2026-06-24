# Discorso orale - Integrali di linea di II specie

## Stato

- Priorita' orale: alta
- Fonte principale: `01_sources/official_slides/08_integrali_linea_II_specie.pdf`
- Note collegate: `04_theory/01_curve_e_integrali_di_linea/integrali_linea_II_specie.md`

## 1. Obiettivo del discorso

Definire l'integrale della componente tangenziale di un campo lungo una curva orientata e collegarlo al lavoro.

## 2. Versione da 30 secondi

Per un campo $F$ e una curva orientata $C$:

$$
\int_C F\cdot\tau\,d\ell
=
\int_a^bF(r(t))\cdot r'(t)\,dt
$$

Dipende dall'orientazione.

## 3. Versione completa da orale

L'integrale di II specie integra lungo una curva la componente del campo nella direzione tangente. Se il campo rappresenta una forza, l'integrale rappresenta il lavoro. Cambiando verso alla curva, cambia il segno.

## 4. Enunciato formale

Se $r(t)$ e' una parametrizzazione concorde con l'orientazione:

$$
\int_C F\cdot\tau\,d\ell
=
\int_a^bF(r(t))\cdot r'(t)\,dt
$$

Nel piano, per $F=(P,Q)$:

$$
\int_C P\,dx+Q\,dy
$$

## 5. Dimostrazione / idea di dimostrazione

Poiche' $\tau=\frac{r'}{\|r'\|}$ e $d\ell=\|r'\|dt$, si ottiene:

$$
F\cdot\tau\,d\ell=F(r(t))\cdot r'(t)\,dt
$$

## 6. Rappresentazione grafica / intuizione geometrica

Disegnare una curva orientata e il campo lungo la curva. Conta solo la componente tangenziale del campo.

## 7. Cosa scrivere alla lavagna

1. Curva orientata $C$.
2. $\tau=\frac{r'}{\|r'\|}$.
3. Formula:

$$
\int_C F\cdot\tau\,d\ell=\int_a^bF(r(t))\cdot r'(t)\,dt
$$

4. Forma differenziale $P\,dx+Q\,dy$.

## 8. Cosa dire a voce

"A differenza della I specie, qui il verso conta: sto misurando quanto il campo spinge lungo il verso scelto."

## 9. Esempio da fare

Campo tangente alla circonferenza $F=(-y,x)$ sulla circonferenza unitaria: il lavoro lungo un giro positivo e' positivo e rappresenta la circuitazione.

## 10. Terminologia corretta

Usare: curva orientata, componente tangenziale, lavoro, forma differenziale, circuitazione.

## 11. Domande possibili del professore

- Differenza I specie / II specie?
- Perche' dipende dall'orientazione?
- Che cos'e' una forma differenziale?
- Come si calcola se il campo e' conservativo?

## 12. Follow-up e trabocchetti

- Se la parametrizzazione e' discorde, cambia il segno.
- Se $F=\nabla U$, si usa il potenziale.
- Su curva chiusa il risultato si chiama circuitazione.

## 13. Collegamenti con altri argomenti

- [[campi_conservativi_discorso_completo]]
- [[green_discorso_completo]]
- [[stokes_discorso_completo]]

## 14. Errori da evitare

- Usare la norma $\|r'\|$ invece del prodotto scalare con $r'$.
- Dimenticare l'orientazione.

## 15. Mini ripasso finale

II specie: campo vettoriale, curva orientata, componente tangenziale, formula $F(r(t))\cdot r'(t)$, lavoro e circuitazione, collegamento a potenziale.

## 16. Checklist personale

- [ ] So definire.
- [ ] So scrivere forma parametrica.
- [ ] So spiegare orientazione.
- [ ] So collegarlo ai campi conservativi.
