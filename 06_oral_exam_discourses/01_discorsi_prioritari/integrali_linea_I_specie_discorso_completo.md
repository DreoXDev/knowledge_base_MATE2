# Discorso orale - Integrali di linea di I specie

## Stato

- Priorita' orale: alta
- Fonte principale: `01_sources/official_slides/07_integrali_linea_I_specie.pdf`
- Note collegate: `04_theory/01_curve_e_integrali_di_linea/integrali_linea_I_specie.md`

## 1. Obiettivo del discorso

Definire l'integrale di una funzione scalare lungo una curva e spiegare perche' compare l'elemento di lunghezza $d\ell$.

## 2. Versione da 30 secondi

Se $C$ e' parametrizzata da $r(t)$:

$$
\int_C f\,d\ell=\int_a^b f(r(t))\|r'(t)\|\,dt
$$

Non dipende dall'orientazione.

## 3. Versione completa da orale

L'integrale di I specie nasce come limite di somme $\sum f(P_i)\Delta\ell_i$ lungo una curva. L'elemento $d\ell$ e' l'elemento di lunghezza. Se uso un parametro qualunque, $d\ell=\|r'(t)\|dt$.

## 4. Enunciato formale

Per una curva regolare $r:[a,b]\to\mathbb{R}^n$:

$$
\int_C f\,d\ell=
\int_a^b f(r(t))\|r'(t)\|\,dt
$$

## 5. Dimostrazione / idea di dimostrazione

Si approssima la curva con segmenti. La lunghezza infinitesima percorsa in tempo $dt$ e' $\|r'(t)\|dt$, da cui la formula.

## 6. Rappresentazione grafica / intuizione geometrica

Se $f\geq0$, l'integrale puo' essere visto come area di una "parete" costruita sopra la curva.

Figure utili:
- `08_visuals/figures/lezione_7_slide_02_suddivisione_curva.png`
- `08_visuals/figures/lezione_7_slide_09_area.png`

## 7. Cosa scrivere alla lavagna

1. Somma $\sum f(P_i)\Delta\ell_i$.
2. $d\ell=\|r'(t)\|dt$.
3. Formula parametrica.
4. Caso $f=1$: lunghezza.

## 8. Cosa dire a voce

"L'integrale di I specie pesa la funzione con la lunghezza della curva. Per questo non conta il verso di percorrenza."

## 9. Esempio da fare

Su una semicirconferenza, parametrizzo con seno/coseno, calcolo $\|r'(t)\|$ e sostituisco nella formula.

## 10. Terminologia corretta

Usare: elemento di lunghezza, ascissa curvilinea, parametro arbitrario, curva regolare.

## 11. Domande possibili del professore

- Perche' compare $\|r'(t)\|$?
- Dipende dall'orientazione?
- Che cos'e' l'ascissa curvilinea?
- Cosa succede se $f=1$?

## 12. Follow-up e trabocchetti

- Non dimenticare $\|r'(t)\|$.
- Non confondere $dt$ con $d\ell$.
- Non usare prodotto scalare con il campo: quello e' II specie.

## 13. Collegamenti con altri argomenti

- [[integrali_linea_II_specie_discorso_completo]]
- [[baricentro_filo_discorso]]
- [[lunghezza_arco_curva]]

## 14. Errori da evitare

- Scrivere solo $\int f(r(t))dt$.
- Dire che dipende dal verso.

## 15. Mini ripasso finale

I specie: funzione scalare su curva, elemento $d\ell$, formula con norma della derivata, indipendente dall'orientazione, caso $f=1$ lunghezza.

## 16. Checklist personale

- [ ] So definire tramite somme.
- [ ] So spiegare $d\ell$.
- [ ] So fare formula parametrica.
- [ ] So fare esempio.
