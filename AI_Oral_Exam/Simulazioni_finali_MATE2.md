# Simulazioni finali MATE2

Usare queste tre simulazioni come prove complete da 15-20 minuti. Ogni simulazione alterna discorso orale, lavagna, dimostrazione e piccolo esercizio.

## Simulazione 1 - Funzioni di piu' variabili, Hessiana, Lagrange

### Avvio professore

> "Parta dalla nozione di punto critico per una funzione di due variabili e mi spieghi come si classifica con l'Hessiana."

### Risposta attesa

- Definizione di punto stazionario: $\nabla f=0$.
- Matrice Hessiana.
- Test con:

$$
D=f_{xx}f_{yy}-f_{xy}^2.
$$

- Caso $D>0$, $D<0$, $D=0$.
- Collegamento a Taylor del secondo ordine.

### Follow-up

1. Perche' compare una forma quadratica?
2. Cosa succede se $D=0$?
3. Che differenza c'e' tra massimo locale e massimo assoluto?
4. Quando entra Weierstrass?

### Cambio tema

> "Ora mi colleghi questo al metodo dei moltiplicatori di Lagrange."

### Lavagna attesa

$$
\nabla f(P)=\lambda\nabla g(P),\qquad g(P)=0.
$$

Con due vincoli:

$$
\nabla f(P)=\lambda\nabla g_1(P)+\mu\nabla g_2(P).
$$

### Esercizio rapido

Massimizzare $f(x,y,z)=x+z$ sulla curva:

$$
x^2+3y^2=3,\qquad y+z=0.
$$

Impostare solo il sistema di Lagrange.

### File da consultare

- [[taylor_due_variabili]]
- [[test_hessiano_massimi_minimi]]
- [[lagrange_discorso_completo]]
- [[lagrange_due_vincoli]]
- [[lagrange_esami]]

## Simulazione 2 - Integrali di linea, campi conservativi, Green

### Avvio professore

> "Mi definisca l'integrale di linea di seconda specie e lo confronti con quello di prima specie."

### Risposta attesa

Prima specie:

$$
\int_C f\,d\ell=\int_a^b f(r(t))\|r'(t)\|\,dt.
$$

Seconda specie:

$$
\int_C F\cdot\tau\,d\ell
=
\int_a^b F(r(t))\cdot r'(t)\,dt.
$$

Differenza: funzione scalare/lunghezza contro campo vettoriale/orientazione.

### Follow-up

1. Perche' la prima specie non dipende dal verso?
2. Perche' la seconda specie cambia segno invertendo la curva?
3. Che cosa significa circuitazione?

### Cambio tema

> "Quando un campo e' conservativo?"

### Lavagna attesa

$$
\vec F=\nabla U
$$

$$
\int_\gamma \vec F\cdot d\vec r=U(P_2)-U(P_1)
$$

$$
\oint_\gamma \vec F\cdot d\vec r=0.
$$

### Collegamento a Green

Enunciare:

$$
\oint_C P\,dx+Q\,dy
=
\iint_D(Q_x-P_y)\,dx\,dy.
$$

Spiegare orientazione positiva: dominio a sinistra.

### Esercizio rapido

Per $F=(x-y,x+y)$ sul quadrato ruotato di area $2$:

$$
Q_x-P_y=1-(-1)=2
$$

quindi:

$$
\oint_C F\cdot\tau\,d\ell=4.
$$

### File da consultare

- [[integrali_linea_I_specie_discorso_completo]]
- [[integrali_linea_II_specie_discorso_completo]]
- [[campi_conservativi_discorso_completo]]
- [[green_discorso_completo]]
- [[green_esami]]

## Simulazione 3 - Superfici, flusso, Stokes, Gauss

### Avvio professore

> "Mi spieghi che cosa significa orientare una superficie e come si definisce il flusso."

### Risposta attesa

- Superficie orientabile: scelta continua della normale.
- Flusso:

$$
\iint_S F\cdot n\,dS.
$$

- Dipendenza dall'orientazione.

### Follow-up

1. Che differenza c'e' tra superficie aperta e chiusa?
2. Che cosa significa normale uscente?
3. Che differenza c'e' tra flusso e circuitazione?

### Stokes

> "Enunci ora Stokes."

$$
\oint_{\partial S}F\cdot\tau\,d\ell
=
\iint_S \operatorname{rot}F\cdot n\,dS.
$$

Punti da dire:

- bordo compatibile con la normale;
- Green come caso piano;
- se cambio normale cambio verso del bordo.

### Gauss-Ostrogradski

> "E Gauss-Ostrogradski?"

$$
\iint_{\partial\Omega}F\cdot n\,dS
=
\iiint_\Omega \operatorname{div}F\,dV.
$$

Punti da dire:

- superficie chiusa;
- normale uscente;
- divergenza come sorgenti/pozzi.

### Esercizio rapido

Per $F=(x,y,z)$ sulla sfera di raggio $R$:

$$
\operatorname{div}F=3.
$$

Quindi:

$$
\iint_SF\cdot n\,dS
=
3\cdot\frac{4}{3}\pi R^3
=
4\pi R^3.
$$

### File da consultare

- [[integrali_superficie_flusso_discorso_completo]]
- [[stokes_discorso_completo]]
- [[gauss_ostrogradski_discorso_completo]]
- [[rotore_divergenza_discorso_completo]]
- [[green_stokes_gauss_collegamenti]]

## Griglia di autovalutazione

Per ogni simulazione segnare:

- definizioni corrette;
- ipotesi dei teoremi esplicitate;
- formule scritte senza errori di segno;
- lavagna ordinata;
- esempio impostato;
- collegamento con almeno un altro argomento;
- risposta ai follow-up senza confondere condizioni necessarie e sufficienti.
