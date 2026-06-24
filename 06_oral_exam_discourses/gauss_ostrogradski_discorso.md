# Discorso orale: formula di Gauss-Ostrogradski

## Versione breve

La formula di Gauss-Ostrogradski collega il flusso uscente di un campo attraverso una superficie chiusa con l'integrale della divergenza nel volume racchiuso.

Se $S=\partial\Omega$ e' la frontiera di un dominio tridimensionale e $n$ e' la normale uscente, allora:

$$
\iint_SF\cdot n\,dS
=
\iiint_\Omega\operatorname{div}F\,dV
$$

La divergenza misura localmente quanto il campo si comporta come sorgente o pozzo. Integrandola sul volume si ottiene il flusso totale uscente.

## Idea della dimostrazione

La dimostrazione si basa sul teorema fondamentale del calcolo applicato separatamente alle tre componenti del campo. Per la componente $F_3$, ad esempio, se il dominio e' compreso tra $z_1(x,y)$ e $z_2(x,y)$, la differenza dei valori di $F_3$ sulle due superfici orizzontali coincide con:

$$
\int_{z_1(x,y)}^{z_2(x,y)}\frac{\partial F_3}{\partial z}\,dz
$$

Le componenti $F_1$ e $F_2$ si trattano allo stesso modo nelle altre direzioni.

## Follow-up

- Perche' la normale deve essere uscente?
- Che cos'e' la divergenza?
- Qual e' l'interpretazione fisica?
- Come si usa Gauss per evitare il calcolo diretto del flusso?
