# Ingestion Report - Calcolo vettoriale

## File analizzato

- Nome: `11_lezione_calcolo_vettoriale.pdf`
- Fonte: slide ufficiali del professore
- Pagine: 51
- Affidabilita': alta

## Argomenti principali

- Superfici orientabili e superfici orientate.
- Area di una superficie parametrizzata, di un grafico e di una superficie di livello.
- Integrali di superficie di I specie.
- Flusso o integrali di superficie di II specie.
- Rotore e divergenza.
- Formula di Stokes.
- Formula di Gauss-Ostrogradski.
- Campi solenoidali, potenziale vettore e tubi di flusso.
- Collegamento finale tra Green, Stokes e Gauss.

## Teoremi / Risultati

| Risultato | Tipo | File target | Priorita' |
|---|---|---|---|
| Superficie orientabile | Definizione | `04_theory/07_superfici_e_integrali_superficiali/superfici_orientabili.md` | Alta |
| Area di superficie | Formula | `04_theory/07_superfici_e_integrali_superficiali/area_superficie.md` | Alta |
| Integrale di superficie di I specie | Definizione | `04_theory/07_superfici_e_integrali_superficiali/integrali_superficie_I_specie.md` | Alta |
| Flusso | Definizione | `04_theory/07_superfici_e_integrali_superficiali/flusso_integrali_superficie_II_specie.md` | Alta |
| Rotore e divergenza | Definizioni | `04_theory/02_campi_vettoriali/rotore_divergenza.md` | Alta |
| Formula di Stokes | Teorema | `04_theory/06_teoremi_integrali/formula_stokes.md` | Alta |
| Formula di Gauss-Ostrogradski | Teorema | `04_theory/06_teoremi_integrali/formula_gauss_ostrogradski.md` | Alta |
| Campi solenoidali e potenziale vettore | Definizione/criterio | `04_theory/02_campi_vettoriali/campi_solenoidali_potenziale_vettore.md` | Media |
| Green, Stokes, Gauss | Schema | `04_theory/06_teoremi_integrali/green_stokes_gauss_collegamenti.md` | Alta |

## Esempi ufficiali

- Area della sfera di raggio $R$: $4\pi R^2$.
- Area di una porzione di sfera ritagliata da un cilindro.
- Flusso di $F=(x,y,z)$ attraverso il triangolo del piano $x+y+z=1$: risultato $\frac{1}{2}$.
- Verifica di Stokes sul piano $2x+y+z=2$: risultato $-1$.
- Verifica di Stokes sull'emisfero superiore della sfera di raggio $3$: risultato $-18\pi$.
- Esempio con rotore nullo e potenziale $U=xyz$.
- Flusso del campo radiale $F=(x,y,z)$ sulla sfera: $4\pi R^3$.
- Flusso di $F=(x^3,y^3,z^3)$ sulla sfera: $\frac{12}{5}\pi R^5$.
- Flusso del campo $r/r^3$ su un guscio sferico: $0$.

## Figure estratte

- `08_visuals/figures/lezione_11_slide_02_mobius.png`
- `08_visuals/figures/lezione_11_slide_05_area_sfera.png`
- `08_visuals/figures/lezione_11_slide_06_area_grafico.png`
- `08_visuals/figures/lezione_11_slide_15_flusso.png`
- `08_visuals/figures/lezione_11_slide_17_triangolo_piano.png`
- `08_visuals/figures/lezione_11_slide_19_rotore_divergenza.png`
- `08_visuals/figures/lezione_11_slide_23_stokes_piano.png`
- `08_visuals/figures/lezione_11_slide_27_lati_stokes.png`
- `08_visuals/figures/lezione_11_slide_32_stokes_emisfero.png`
- `08_visuals/figures/lezione_11_slide_35_regioni_semplici.png`
- `08_visuals/figures/lezione_11_slide_42_normale_sfera.png`

## Note di attenzione

- La lezione usa la convenzione sferica gia' fissata nella lezione 10: $\theta$ e' latitudine, quindi $z=r\sin\theta$ e $dV=r^2\cos\theta\,dr\,d\theta\,d\varphi$.
- Slide 5: l'intervallo coerente per $\theta$ nella parametrizzazione della sfera e' $[-\pi/2,\pi/2]$.
- Slide 7: il cilindro coerente con il calcolo e' $x^2+y^2\leq a^2$.
- Slide 23: il secondo vettore tangente e' $r_y$, non un secondo $r_x$.
- Slide 35: il testo parla di dominio piano, ma le formule descrivono domini tridimensionali semplici.
- Slide 45: per $F=(x^3,y^3,z^3)$ si usa $\operatorname{div}F=3x^2+3y^2+3z^2$.
