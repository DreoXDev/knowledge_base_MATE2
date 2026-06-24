# Discorso orale: gradiente e derivata direzionale

## Versione breve

Il gradiente di una funzione $f$ e' il vettore formato dalle sue derivate parziali:

$$
\nabla f=
\left(
\frac{\partial f}{\partial x_1},
\dots,
\frac{\partial f}{\partial x_n}
\right).
$$

Se si restringe $f$ a una curva $x(t)$, si ottiene $F(t)=f(x(t))$. La derivata lungo la curva e':

$$
F'(\bar{t})
=
\nabla f(P)\cdot x'(\bar{t}),
$$

dove $P=x(\bar{t})$.

Se $v$ e' un vettore unitario, la derivata direzionale nella direzione $v$ e':

$$
L_v(f)(P)=\nabla f(P)\cdot v,
$$

cioe' misura la variazione istantanea della funzione quando ci si muove dal punto $P$ nella direzione $v$.

## Follow-up

- Perche' $v$ deve essere unitario?
- Che relazione c'e' tra derivata lungo una curva e derivata direzionale?
- Come si dimostra la formula della derivata lungo una curva?

