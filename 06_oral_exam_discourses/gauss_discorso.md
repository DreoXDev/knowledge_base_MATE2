# Discorso orale: formula di Gauss-Ostrogradski

## Versione breve

La formula di Gauss-Ostrogradski, o teorema della divergenza, afferma che per una superficie chiusa $S=\partial\Omega$ orientata con normale uscente:

$$
\iint_SF\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

Quindi il flusso uscente totale e' uguale all'integrale della divergenza nel volume.

## Significato

La divergenza misura sorgenti e pozzi locali. Se $\operatorname{div}F=0$, il campo non ha sorgenti nette nel dominio e il flusso totale attraverso ogni superficie chiusa e' nullo.

## Esempi da citare

- Per $F=(x,y,z)$ sulla sfera di raggio $R$, il flusso e' $4\pi R^3$.
- Per $F=(x^3,y^3,z^3)$ sulla sfera, il flusso e' $\frac{12}{5}\pi R^5$.
- Per $F=r/r^3$ su un guscio sferico, il flusso totale e' $0$.

## Errori da evitare

- Usare la normale entrante.
- Applicare Gauss a una superficie non chiusa senza chiuderla.
- Dimenticare che nel guscio la normale uscente sulla sfera interna punta verso il centro.
