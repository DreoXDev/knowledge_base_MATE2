# Discorso orale: moltiplicatori di Lagrange

## Obiettivo

Preparare una risposta da esame orale su questo argomento.

## Versione breve

Il metodo dei moltiplicatori di Lagrange serve a trovare punti stazionari di una funzione soggetta a vincoli.

Nel caso di una funzione $f(x,y)$ vincolata a una curva $g(x,y)=c$, in un punto stazionario vincolato la derivata direzionale di $f$ lungo ogni direzione tangente al vincolo deve essere nulla.

Questo significa che il gradiente $\nabla f$ e' ortogonale alla curva vincolo. Ma anche $\nabla g$ e' ortogonale alla curva di livello $g=c$. Quindi i due gradienti sono paralleli:

$$
\nabla f(P)=\lambda\nabla g(P)
$$

insieme al vincolo:

$$
g(P)=c.
$$

Nel caso di una superficie $G(x,y,z)=c$ vale lo stesso ragionamento:

$$
\nabla f(P)=\lambda\nabla G(P).
$$

Nel caso di due vincoli $G_1=c_1$ e $G_2=c_2$, il gradiente di $f$ deve essere combinazione lineare dei gradienti dei vincoli:

$$
\nabla f(P)=\lambda_1\nabla G_1(P)+\lambda_2\nabla G_2(P).
$$

## Follow-up probabili

- Perche' il gradiente e' ortogonale al vincolo?
- Cosa rappresenta il moltiplicatore $\lambda$?
- Cosa cambia tra uno e due vincoli?
- Il metodo garantisce sempre massimo/minimo?

## Errori da evitare

- Dimenticare i vincoli nel sistema.
- Imporre $\nabla f=0$ come se il problema fosse libero.
- Confondere parallelismo dei gradienti con ortogonalita' tra gradienti.
