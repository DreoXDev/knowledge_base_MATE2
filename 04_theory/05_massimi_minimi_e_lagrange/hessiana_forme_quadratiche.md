# Hessiana e forme quadratiche

## Stato

- Fonte: `01_sources/official_slides/3_lezione_massimi_minimi_locali.pdf`
- Slide: 16-24
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Taylor nei punti stazionari

Se $P=(\bar{x},\bar{y})$ e' stazionario, il termine lineare di Taylor si annulla e:

$$
\Delta f
=
\frac{1}{2}
\left[
f_{xx}(P)(\Delta x)^2
+
2f_{xy}(P)\Delta x\Delta y
+
f_{yy}(P)(\Delta y)^2
\right]
+
Resto.
$$

## Matrice Hessiana

$$
H(P)
=
\begin{pmatrix}
f_{xx}(P) & f_{xy}(P) \\
f_{yx}(P) & f_{yy}(P)
\end{pmatrix}.
$$

Se $f_{xy}=f_{yx}$, la matrice e' simmetrica.

## Forma quadratica associata

$$
Q(\Delta x,\Delta y)
=
H_{11}(\Delta x)^2
+
2H_{12}\Delta x\Delta y
+
H_{22}(\Delta y)^2.
$$

## Classificazione della forma quadratica

- Definita positiva: $Q\geq 0$ e si annulla solo per il vettore nullo.
- Semidefinita positiva: $Q\geq 0$ ma si annulla anche per qualche vettore non nullo.
- Definita negativa: $Q\leq 0$ e si annulla solo per il vettore nullo.
- Semidefinita negativa: $Q\leq 0$ ma si annulla anche per qualche vettore non nullo.
- Indefinita: assume valori sia positivi sia negativi.

## Completamento dei quadrati

Se $H_{11}\neq 0$:

$$
Q
=
H_{11}
\left(
\Delta x+\frac{H_{12}}{H_{11}}\Delta y
\right)^2
+
\frac{\det H}{H_{11}}(\Delta y)^2.
$$

Se $H_{22}\neq 0$:

$$
Q
=
\frac{\det H}{H_{22}}(\Delta x)^2
+
H_{22}
\left(
\Delta y+\frac{H_{12}}{H_{22}}\Delta x
\right)^2.
$$

## Conseguenze

- Se $\det H>0$ e $H_{11}>0$, la forma e' definita positiva.
- Se $\det H>0$ e $H_{11}<0$, la forma e' definita negativa.
- Se $\det H<0$, la forma e' indefinita.
- Se $\det H=0$, il test e' inconclusivo.

## Collegamenti

- [[taylor_due_variabili]]
- [[test_hessiano_massimi_minimi]]
- [[hessiana_massimi_minimi]]

