# Campi su domini non semplicemente connessi

## Stato

- Fonte: `01_sources/official_slides/9_lezione_campi_vettoriali_conservativi.pdf`
- Slide: 50-56
- Affidabilita': alta

## Campo radiale logaritmico

Il campo:

$$
F=
\left(
\frac{2x}{x^2+y^2},
\frac{2y}{x^2+y^2}
\right)
$$

e' definito su $\mathbb{R}^2\setminus\{0\}$ e ammette potenziale globale:

$$
U=\ln(x^2+y^2).
$$

Questo mostra che la semplice connessione e' una condizione sufficiente, non necessaria.

## Campo angolare

Il campo:

$$
F=
\left(
-\frac{y}{x^2+y^2},
\frac{x}{x^2+y^2}
\right)
$$

e' irrotazionale su:

$$
\mathbb{R}^2\setminus\{0\},
$$

ma non e' conservativo su tutto il dominio.

Sulla circonferenza unitaria percorsa in senso antiorario:

$$
x=\cos t,\qquad y=\sin t,\qquad t\in[0,2\pi],
$$

si ha:

$$
\oint_C F\cdot\tau\,d\ell=2\pi.
$$

Una circuitazione non nulla su una curva chiusa impedisce l'esistenza di un potenziale globale.

## Potenziale locale

Sui sottodomini semplicemente connessi si puo' scrivere localmente:

$$
U=\arctan\frac{y}{x},
$$

cioe' il potenziale e' l'angolo polare $\theta$.

Ma $\theta$ non e' una funzione monodroma su tutto $\mathbb{R}^2\setminus\{0\}$: dopo un giro completo passa da $\theta_0$ a $\theta_0+2\pi$.

## Collegamenti

- [[domini_semplicemente_connessi]]
- [[campo_angolare_non_conservativo]]
