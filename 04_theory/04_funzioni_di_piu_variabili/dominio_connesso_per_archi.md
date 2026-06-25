# Dominio connesso per archi

## Definizione

Un dominio $D\subseteq\mathbb R^n$ si dice connesso per archi se, dati due punti qualunque $P_1,P_2\in D$, esiste una curva continua $\gamma$ contenuta in $D$ che li congiunge:

$$
\gamma(a)=P_1,\qquad \gamma(b)=P_2,\qquad \gamma([a,b])\subseteq D.
$$

## Formula/idea da ricordare

La proprieta' da ricordare e':

$$
\forall P_1,P_2\in D,\quad \exists \gamma\subset D \text{ da } P_1 \text{ a } P_2.
$$

## Collegamento ai campi conservativi

Nel discorso sui [[Campi conservativi - discorso orale completo|campi conservativi]], questa ipotesi serve nella costruzione del potenziale:

$$
U(P)=\int_{P_0}^{P}\vec F\cdot d\vec\ell.
$$

Se il dominio non fosse connesso per archi, non potrei garantire una curva contenuta in $D$ che collega il punto fissato $P_0$ a ogni punto $P$ del dominio.

## Domanda orale tipica

**Domanda:** perche' nella costruzione del potenziale si assume che il dominio sia connesso per archi?

**Risposta:** perche' devo poter raggiungere ogni punto $P$ partendo da $P_0$ tramite una curva contenuta nel dominio; altrimenti l'integrale che definisce $U(P)$ non sarebbe definibile su tutto il dominio.
