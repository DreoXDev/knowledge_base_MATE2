# Discorsi da 2 minuti

## Green in 2 minuti

Green trasforma una circuitazione piana in un integrale doppio. Con $F=(P,Q)$ e $C=\partial D$ orientata positivamente:

$$
\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dx\,dy
$$

Orientazione positiva significa dominio a sinistra. La dimostrazione usa due identita' e la cancellazione dei bordi interni.

## Lagrange in 2 minuti

Per ottimizzare con vincolo regolare $g=0$:

$$
\nabla f=\lambda\nabla g
$$

Con due vincoli:

$$
\nabla f=\lambda\nabla g_1+\mu\nabla g_2
$$

Lagrange da' candidati: poi confronto i valori e controllo punti non regolari o bordi.

## Stokes in 2 minuti

Stokes generalizza Green:

$$
\oint_C F\cdot\tau\,d\ell=\iint_S\operatorname{rot}(F)\cdot n\,dS
$$

Il bordo deve essere orientato compatibilmente con la normale.

## Gauss in 2 minuti

Gauss collega flusso uscente e divergenza:

$$
\iint_{\partial\Omega}F\cdot n\,dS=\iiint_\Omega\operatorname{div}F\,dV
$$

Serve superficie chiusa e normale uscente.

## Campi conservativi in 2 minuti

Campo conservativo significa $F=\nabla U$. Allora l'integrale di linea dipende solo dagli estremi:

$$
\int_C F\cdot\tau\,d\ell=U(P_1)-U(P_0)
$$

## Integrali di linea I specie in 2 minuti

$$
\int_C f\,d\ell=\int_a^b f(r(t))\|r'(t)\|\,dt
$$

Integra una funzione scalare lungo una curva e non dipende dall'orientazione.

## Integrali di linea II specie in 2 minuti

$$
\int_C F\cdot\tau\,d\ell=\int_a^bF(r(t))\cdot r'(t)\,dt
$$

Integra la componente tangenziale di un campo e dipende dall'orientazione.
