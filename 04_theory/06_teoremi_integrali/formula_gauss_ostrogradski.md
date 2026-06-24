# Formula di Gauss-Ostrogradski

## Enunciato

Sia $\Omega\subset\mathbb{R}^3$ un dominio semplice limitato, con frontiera:

$$
S=\partial\Omega
$$

differenziabile a tratti. Sia $F=(F_1,F_2,F_3)$ un campo le cui componenti sono continue con le derivate parziali richieste nel dominio, frontiera inclusa.

Allora:

$$
\iint_S F\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

dove $n$ e' la normale uscente.

## Significato

La formula collega il flusso totale uscente attraverso una superficie chiusa con l'integrale della divergenza nel volume racchiuso. Se la divergenza e' positiva, il campo ha sorgenti nette; se e' negativa, ha pozzi netti; se e' nulla, il flusso uscente totale e' nullo.

## Idea della dimostrazione

Si dimostra separatamente per le tre componenti:

$$
\iint_S(F_1e_1\cdot n)\,dS=\iiint_\Omega\frac{\partial F_1}{\partial x}\,dV
$$

$$
\iint_S(F_2e_2\cdot n)\,dS=\iiint_\Omega\frac{\partial F_2}{\partial y}\,dV
$$

$$
\iint_S(F_3e_3\cdot n)\,dS=\iiint_\Omega\frac{\partial F_3}{\partial z}\,dV
$$

Per esempio, se:

$$
z_1(x,y)\leq z\leq z_2(x,y)
$$

allora il contributo della componente $F_3$ sulla superficie superiore meno quello sulla superficie inferiore e':

$$
\iint_D\left[F_3(x,y,z_2(x,y))-F_3(x,y,z_1(x,y))\right]\,dx\,dy
$$

che coincide con:

$$
\iint_D\int_{z_1(x,y)}^{z_2(x,y)}
\frac{\partial F_3}{\partial z}\,dz\,dx\,dy
$$

per il teorema fondamentale del calcolo.

## Esempio ufficiale

Per $F=(x,y,z)$ e $S$ sfera di raggio $R$:

$$
\operatorname{div}F=3
$$

e quindi:

$$
\iint_SF\cdot n\,dS
=
3\cdot\frac{4}{3}\pi R^3
=
4\pi R^3
$$

## Collegamenti

- [[flusso_integrali_superficie_II_specie]]
- [[rotore_divergenza]]
- [[campi_solenoidali_potenziale_vettore]]
- [[green_stokes_gauss_collegamenti]]
