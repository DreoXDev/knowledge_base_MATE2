# Metodo: massimi e minimi assoluti

## Stato

- Fonte: `01_sources/official_slides/6_lezione_massimi_minimi_assoluti.pdf`
- Slide: 8-44
- Affidabilita': alta

## Procedura

1. Verificare chiusura e limitatezza del dominio.
2. Cercare i punti stazionari interni con $\nabla f=0$.
3. Studiare ogni tratto della frontiera.
4. Aggiungere vertici o estremi dei parametri.
5. Valutare $f$ su tutti i candidati.
6. Confrontare i valori.

## Frontiera poligonale

Si parametrizza ogni lato come segmento. Se il lato va da $(x_1,y_1)$ a $(x_2,y_2)$:

$$
x=x_1+t(x_2-x_1),\qquad
y=y_1+t(y_2-y_1),
$$

con $t\in[0,1]$.

## Frontiera regolare

Se la frontiera e' un vincolo, ad esempio $G(x,y)=c$, si possono usare i moltiplicatori di Lagrange:

$$
\nabla f=\lambda\nabla G.
$$

## Errore comune

Fermarsi ai punti stazionari interni. Negli estremi assoluti la frontiera e' spesso decisiva.

## Collegamenti

- [[massimi_minimi_assoluti]]
- [[massimi_minimi_assoluti_frontiera_lagrange]]
