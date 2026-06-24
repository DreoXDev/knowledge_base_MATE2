# Rotore e divergenza

Sia:

$$
F=F_1(x,y,z)e_1+F_2(x,y,z)e_2+F_3(x,y,z)e_3
$$

un campo vettoriale definito in un dominio $\Omega\subset\mathbb{R}^3$.

## Rotore

Il rotore di $F$ e' il campo vettoriale:

$$
\operatorname{rot}(F)=
\left(\frac{\partial F_3}{\partial y}-\frac{\partial F_2}{\partial z}\right)e_1
+
\left(\frac{\partial F_1}{\partial z}-\frac{\partial F_3}{\partial x}\right)e_2
+
\left(\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\right)e_3
$$

Il rotore misura la tendenza locale del campo a ruotare. Compare nella formula di Stokes:

$$
\oint_{\partial S}F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

## Divergenza

La divergenza di $F$ e' la funzione scalare:

$$
\operatorname{div}F=
\frac{\partial F_1}{\partial x}
+
\frac{\partial F_2}{\partial y}
+
\frac{\partial F_3}{\partial z}
$$

La divergenza misura localmente quanto il campo si comporta come sorgente o pozzo. Compare nella formula di Gauss-Ostrogradski:

$$
\iint_{\partial\Omega}F\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

## Collegamenti

- [[formula_stokes]]
- [[formula_gauss_ostrogradski]]
- [[campi_solenoidali_potenziale_vettore]]
