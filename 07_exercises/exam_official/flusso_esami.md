# Esercizi ufficiali - Flusso

## 13 aprile 2023 - Esercizio 5

### Traccia

Calcolare il flusso di:

$$
F=(x,y,z)
$$

attraverso il triangolo del piano:

$$
x+y+z=1
$$

nel primo ottante, con normale che forma angolo acuto con $e_3$.

### Soluzione

Scriviamo la superficie come grafico:

$$
r(x,y)=(x,y,1-x-y)
$$

sul triangolo:

$$
T=\{x\geq0,\ y\geq0,\ x+y\leq1\}
$$

Si ha:

$$
r_x=(1,0,-1),\qquad r_y=(0,1,-1)
$$

e:

$$
r_x\times r_y=(1,1,1)
$$

che ha componente $z$ positiva, quindi e' concorde con l'orientazione richiesta.

Allora:

$$
F(r(x,y))\cdot(r_x\times r_y)
=
x+y+1-x-y
=
1
$$

Quindi:

$$
\iint_SF\cdot n\,dS
=
\iint_T1\,dx\,dy
=
\frac{1}{2}
$$

## Collegamento teoria

- `04_theory/07_superfici_e_integrali_superficiali/flusso_integrali_superficie_II_specie.md`
- `07_exercises/esercizi_per_topic/integrali_superficie_calcolo_vettoriale.md`

## Errori da evitare

- Non controllare l'orientazione della normale.
- Usare $\|r_x\times r_y\|$ invece del vettore orientato nel flusso.
