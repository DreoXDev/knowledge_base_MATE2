# Derivazione della funzione composta

## Definizione operativa

Sia $U:\mathbb R^n\to\mathbb R$ derivabile e sia $\gamma:[a,b]\to\mathbb R^n$ una curva derivabile:

$$
\gamma(t)=(x_1(t),\dots,x_n(t)).
$$

Allora:

$$
\frac{d}{dt}U(\gamma(t))
=
\nabla U(\gamma(t))\cdot\gamma'(t).
$$

In componenti:

$$
\frac{d}{dt}U(\gamma(t))
=
\frac{\partial U}{\partial x_1}\frac{dx_1}{dt}
+
\dots
+
\frac{\partial U}{\partial x_n}\frac{dx_n}{dt}.
$$

## Collegamento ai campi conservativi

Se $\vec F=\nabla U$, allora lungo una curva $\gamma$:

$$
\vec F(\gamma(t))\cdot\gamma'(t)
=
\nabla U(\gamma(t))\cdot\gamma'(t)
=
\frac{d}{dt}U(\gamma(t)).
$$

Questo e' il passaggio centrale nella dimostrazione dell'indipendenza dal cammino per i [[Campi conservativi - discorso orale completo|campi conservativi]].

## Domanda orale tipica

**Domanda:** perche' compare il prodotto scalare tra gradiente e velocita' della curva?

**Risposta:** perche' sto derivando una funzione scalare lungo una curva; la variazione di $U$ lungo $\gamma$ e' data dal gradiente di $U$ proiettato sulla direzione di moto $\gamma'(t)$.
