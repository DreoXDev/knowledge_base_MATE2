# Strategia esercizi esame MATE2

## Struttura tipica

Ogni appello contiene 5 esercizi da 6 punti.

Dal batch iniziale emergono spesso:

1. punti critici;
2. Lagrange;
3. integrale multiplo;
4. Green / Stokes / flusso;
5. campo conservativo e potenziale.

## Strategia rapida

### Punti critici

- Scrivere subito $\nabla f=0$.
- Fattorizzare se possibile.
- Hessiana:

$$
D=f_{xx}f_{yy}-f_{xy}^2
$$

- Se $D>0$ e $f_{xx}>0$: minimo.
- Se $D>0$ e $f_{xx}<0$: massimo.
- Se $D<0$: sella.
- Se $D=0$: test non conclusivo.

### Lagrange

- Scrivere chiaramente funzione e vincoli.
- Un vincolo:

$$
\nabla f=\lambda\nabla g
$$

- Due vincoli:

$$
\nabla f=\lambda\nabla g+\mu\nabla h
$$

- Confrontare i valori finali.

### Campi conservativi

- Cercare pattern da potenziale.
- Integrare una componente e introdurre funzione delle variabili rimanenti.
- Verificare sempre $\nabla U=F$.

### Integrali tripli

- Disegnare o descrivere dominio.
- Scegliere coordinate:
  - tetraedro: cartesiane;
  - cilindro/paraboloide: cilindriche;
  - sfera/ottante: sferiche.
- Non dimenticare il jacobiano.

### Green

- Calcolare:

$$
Q_x-P_y
$$

- Se e' costante, usare area.
- Controllare orientazione positiva.

### Flusso

- Se superficie parametrizzata:

$$
\iint F(r(u,v))\cdot(r_u\times r_v)\,du\,dv
$$

- Controllare orientazione.
- Se superficie chiusa, valutare se conviene Gauss.

## Pattern batch 2

### Funzioni lineari su sfera

Per $f=ax+by+cz$ su:

$$
x^2+y^2+z^2=R^2
$$

il massimo e' nel punto:

$$
R\frac{(a,b,c)}{\sqrt{a^2+b^2+c^2}}
$$

e il minimo e' il punto opposto.

### Distanza da retta intersezione di piani

Prima semplificare i vincoli. Spesso l'intersezione permette di eliminare una variabile e ridurre a un problema elementare.

### Green

Calcolare subito:

$$
Q_x-P_y
$$

Se:
- e' $0$, la circuitazione e' $0$;
- e' costante, basta moltiplicare per l'area;
- e' radiale/polinomiale, passare a coordinate adatte.

### Potenziali logaritmici ciclici

Pattern frequente:

$$
U=x\ln(y^2+1)+y\ln(z^2+1)+z\ln(x^2+1)
$$

oppure varianti simmetriche.

Derivare sempre il candidato per verificarlo.
