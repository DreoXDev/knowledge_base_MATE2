# Rotore

## Stato

- Fonte: Lezione 11, slide 19.
- Affidabilita': alta.

## Definizione

Per un campo:

$$
F=F_1e_1+F_2e_2+F_3e_3
$$

il rotore e':

$$
\operatorname{rot}(F)=
\left(\frac{\partial F_3}{\partial y}-\frac{\partial F_2}{\partial z}\right)e_1
+
\left(\frac{\partial F_1}{\partial z}-\frac{\partial F_3}{\partial x}\right)e_2
+
\left(\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\right)e_3
$$

## Significato

Il rotore misura la tendenza locale del campo a ruotare. Nella formula di Stokes il flusso del rotore attraverso una superficie coincide con la circuitazione del campo lungo il bordo:

$$
\oint_{\partial S}F\cdot\tau\,d\ell
=
\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

## Collegamenti

- [[rotore_divergenza]]
- [[formula_stokes]]
