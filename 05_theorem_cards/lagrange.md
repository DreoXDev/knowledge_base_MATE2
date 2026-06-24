# Teorema: moltiplicatori di Lagrange

## Stato

- Fonte: `01_sources/official_slides/5_lezione_moltiplicatori_lagrange.pdf`
- Slide: 1-42
- Affidabilita': alta, con refusi segnalati nelle note teoriche
- Dimostrazione richiesta: interpretazione geometrica
- Ultimo aggiornamento: 2026-06-23

## Quando si usa

Si usa per trovare candidati stazionari di una funzione soggetta a vincoli.

## Idea geometrica

In un problema vincolato non si richiede $\nabla f=0$, perche' non ci si puo' muovere in tutte le direzioni. Si richiede che la derivata direzionale lungo le direzioni tangenti al vincolo sia nulla.

## Un vincolo

Per $f$ vincolata a $g=c$:

$$
\nabla f(P)=\lambda\nabla g(P)
$$

insieme a:

$$
g(P)=c.
$$

## Due vincoli

Per $f$ vincolata a $G_1=c_1$ e $G_2=c_2$:

$$
\nabla f(P)
=
\lambda_1\nabla G_1(P)+\lambda_2\nabla G_2(P)
$$

insieme ai due vincoli.

## Punti delicati

- Lagrange produce candidati stazionari vincolati, non automaticamente massimo/minimo globale.
- Il vincolo va sempre incluso nel sistema.
- Con due vincoli serve l'indipendenza di $\nabla G_1$ e $\nabla G_2$.

## Collegamenti

- [[lagrange_un_vincolo_curve]]
- [[lagrange_un_vincolo_superfici]]
- [[lagrange_due_vincoli]]
