# Discorso orale - Integrali doppi per strati

## Obiettivo del discorso

Spiegare come si imposta un integrale doppio guardando il dominio a strati, cioe' fissando una variabile esterna e integrando sull'altra variabile lungo una sezione del dominio.

## Tempo stimato

- Versione essenziale: 7 minuti
- Versione completa con esempio e disegno: 12 minuti
- Estensioni/domande su cambio d'ordine e domini spezzati: 4 minuti

Totale realistico: 12-16 minuti.

## Discorso principale

> "Partirei dal disegno del dominio. Negli integrali doppi la parte piu' importante non e' scrivere subito la formula, ma capire come viene attraversato il dominio."

> "Per strati, fisso una variabile esterna e descrivo la sezione interna come un intervallo che dipende da quella variabile."

"integrale doppio su omega scritto come integrale esterno in x e interno in y"

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_a^b
\left(
\int_{y_1(x)}^{y_2(x)} f(x,y)\,dy
\right)dx.
$$

> "A voce direi: faccio scorrere $x$ da $a$ a $b$; per ogni $x$ guardo il segmento verticale del dominio, da $y_1(x)$ a $y_2(x)$."

## Piccolo esempio iniziale

Se:

$$
\Omega=\{(x,y):0\le x\le 1,\ 0\le y\le x\},
$$

allora:

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_0^1 dx\int_0^x f(x,y)\,dy.
$$

> "Questo esempio e' utile perche' si vede subito il segmento verticale: fissato $x$, $y$ parte da zero e arriva alla retta $y=x$."

## Teorema

Se $\Omega$ e' normale rispetto a $x$, cioe':

$$
\Omega=\{(x,y):a\le x\le b,\ y_1(x)\le y\le y_2(x)\},
$$

allora:

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_a^b dx
\int_{y_1(x)}^{y_2(x)}
f(x,y)\,dy.
$$

## Dimostrazione

> "L'idea della dimostrazione e' la stessa degli integrali iterati: suddivido il dominio in strisce verticali sottili."

Per ogni $x$ fissato, la sezione verticale del dominio e':

$$
y_1(x)\le y\le y_2(x).
$$

L'integrale interno somma il contributo lungo quella sezione:

$$
\int_{y_1(x)}^{y_2(x)}f(x,y)\,dy.
$$

Poi l'integrale esterno somma tutte le sezioni mentre $x$ varia da $a$ a $b$.

## Conseguenze / osservazioni importanti

- Il disegno del dominio decide gli estremi.
- Se una retta verticale taglia il dominio in piu' pezzi, bisogna spezzare il dominio.
- Se $f\ge 0$, l'integrale doppio rappresenta un volume sotto il grafico $z=f(x,y)$.
- Lo stesso dominio puo' spesso essere descritto anche con l'altro ordine.

## Moduli aggiuntivi se il prof lascia continuare

### Modulo 1 - Strati orizzontali

Se invece il dominio e' normale rispetto a $y$:

$$
\Omega=\{(x,y):c\le y\le d,\ x_1(y)\le x\le x_2(y)\},
$$

allora:

$$
\iint_\Omega f(x,y)\,dx\,dy
=
\int_c^d dy
\int_{x_1(y)}^{x_2(y)}
f(x,y)\,dx.
$$

> "Qui faccio scorrere $y$ e guardo sezioni orizzontali."

### Modulo 2 - Quando conviene cambiare ordine

> "Cambio ordine quando l'integrale interno diventa difficile o quando il dominio e' descritto meglio nell'altro verso."

## Cosa scrivere alla lavagna

1. Disegno del dominio con strisce verticali.
2. Dominio normale:

$$
\Omega=\{a\le x\le b,\ y_1(x)\le y\le y_2(x)\}.
$$

3. Formula:

$$
\iint_\Omega f\,dx\,dy
=
\int_a^b dx\int_{y_1(x)}^{y_2(x)}f(x,y)\,dy.
$$

4. Esempio triangolo:

$$
0\le x\le 1,\qquad 0\le y\le x.
$$

## Domande possibili del professore

### Domanda: cosa significa dominio normale rispetto a $x$?

Risposta: significa che fissato $x$ tra due estremi costanti, la sezione verticale del dominio e' un intervallo unico in $y$.

### Domanda: quando devo spezzare il dominio?

Risposta: quando una sezione verticale non e' descritta da un solo intervallo oppure cambia formula agli estremi.

### Domanda: che differenza c'e' tra integrale doppio e integrale iterato?

Risposta: l'integrale doppio e' l'oggetto geometrico sul dominio; l'integrale iterato e' un modo operativo per calcolarlo quando il dominio e' descritto bene.

## Immagini / visualizzazioni utili

![[lezione_10_slide_08_suddivisione_dominio.png]]

- Mostra la suddivisione del dominio: serve per ricordare che l'integrale doppio nasce da una somma su piccoli pezzi.

![[lezione_10_slide_11_suddivisione_rettangolare.png]]

- Utile per spiegare la lettura del dominio tramite sezioni ordinate.

## Collegamenti utili nella KB

- [[integrali_iterati]]: formula generale degli integrali iterati.
- [[integrali_multipli]]: definizione generale di integrale multiplo.
- [[inversione_ordine_integrazione]]: quando conviene cambiare ordine.
- [[integrali_multipli_discorso_completo]]: discorso generale sugli integrali multipli.
- [[RAG_THEORY_MAP]]: mappa per recuperare teoria ed esercizi.

## 17. Link a teoria, theorem cards, esercizi, esami

### Teoria

- [[integrali_iterati]]
- [[integrali_multipli]]
- [[inversione_ordine_integrazione]]
- `04_theory/08_integrali_multipli/integrali_iterati.md`
- `04_theory/08_integrali_multipli/integrali_multipli.md`

### Discorsi collegati

- [[integrali_multipli_discorso_completo]]
- [[integrali_doppi_fili_discorso_completo]]

### Esercizi

- [[integrali_multipli]]
- `07_exercises/esercizi_per_topic/integrali_multipli.md`

### Figure / visual

- `08_visuals/figures/lezione_10_slide_08_suddivisione_dominio.png`
- `08_visuals/figures/lezione_10_slide_11_suddivisione_rettangolare.png`
