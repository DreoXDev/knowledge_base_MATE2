# Discorso orale: superfici e integrali di superficie

## Versione breve

Per lavorare con gli integrali di superficie parto da una superficie regolare parametrizzata:

$$
r(u,v)=(x(u,v),y(u,v),z(u,v))
$$

L'elemento di area e':

$$
dS=\|r_u\times r_v\|\,du\,dv
$$

quindi l'area della superficie e':

$$
mS=\iint_D\|r_u\times r_v\|\,du\,dv
$$

Se invece la superficie e' il grafico $z=f(x,y)$, allora:

$$
dS=\sqrt{1+f_x^2+f_y^2}\,dx\,dy
$$

L'integrale di superficie di I specie e':

$$
\int_S f\,dS
$$

e si calcola sostituendo la parametrizzazione:

$$
\int_S f\,dS
=
\iint_D f(r(u,v))\|r_u\times r_v\|\,du\,dv
$$

Questo integrale non dipende dall'orientazione.

## Follow-up

- Come si ottiene la formula per il grafico $z=f(x,y)$?
- Qual e' la differenza tra area e flusso?
- Come si calcola l'area della sfera?
- Come si usa la funzione implicita per una superficie di livello?
