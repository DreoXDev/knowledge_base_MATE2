# Discorso orale: curve parametrizzate e lunghezza di un arco

## Obiettivo

Preparare una risposta orale su curve parametrizzate, vettore tangente, regolarita' e lunghezza di un arco.

## Durata target

- Risposta breve: 2 minuti.
- Risposta completa: 5 minuti.
- Con derivazione della lunghezza: 7-8 minuti.

## Versione breve

Una curva parametrizzata in $\mathbb{R}^n$ e' una funzione vettoriale $x:[a,b]\to\mathbb{R}^n$, cioe' a ogni valore del parametro $t$ associa un punto dello spazio. Scriviamo le sue componenti come $x_1(t),\dots,x_n(t)$.

Se le componenti sono derivabili, il vettore derivata $\frac{dx}{dt}$ e' il vettore tangente alla curva; se $t$ rappresenta il tempo, viene interpretato come vettore velocita'.

Una parametrizzazione e' regolare quando il vettore tangente non si annulla mai, cioe' $\left\|\frac{dx}{dt}\right\|>0$. Questo evita punti in cui la curva si ferma o perde una direzione tangente ben definita.

La lunghezza di un arco di curva regolare e':

$$
\ell
=
\int_a^b
\left\|
\frac{dx}{dt}
\right\|
dt
$$

cioe' si integra la velocita' scalare lungo l'intervallo del parametro.

## Versione completa

Una curva parametrizzata e' il modo con cui descriviamo una curva tramite un parametro reale. In $\mathbb{R}^n$ scriviamo $x(t)=(x_1(t),\dots,x_n(t))$, con $t\in[a,b]$. Le funzioni $x_i(t)$ sono le componenti della curva.

Il punto importante e' distinguere il sostegno geometrico dal modo in cui viene percorso. Ad esempio $x(t)=t^3$, $y(t)=t^3$ sta sulla retta $y=x$, ma il vettore tangente $(3t^2,3t^2)$ non e' costante, quindi il moto non e' uniforme. Invece $x(t)=t^2$, $y(t)=t^2$ descrive solo la semiretta nel primo quadrante e non e' regolare in $t=0$, perche' il vettore tangente $(2t,2t)$ si annulla.

Per una curva regolare, la lunghezza si calcola integrando la norma del vettore tangente:

$$
\ell
=
\int_a^b
\left\|
\frac{dx}{dt}
\right\|
dt.
$$

Questa formula dice che sommiamo, istante per istante, la velocita' scalare con cui percorriamo la curva.

## Derivazione parlata della formula della lunghezza

L'idea e' approssimare la curva con tanti piccoli segmenti. Su un intervallo molto piccolo $[\bar{t},\bar{t}+\Delta t]$, approssimo ogni componente con Taylor del primo ordine:

$$
x_i^{lin}(t)
=
x_i(\bar{t})
+
\frac{dx_i}{dt}(\bar{t})(t-\bar{t}).
$$

Il tratto di curva viene quindi approssimato da un segmento, la cui lunghezza e' circa:

$$
\left\|
\frac{dx}{dt}(\bar{t})
\right\|
\Delta t.
$$

Se divido l'intervallo in molti sottointervalli, sommo questi contributi. Passando al limite ottengo l'integrale:

$$
\ell
=
\int_a^b
\left\|
\frac{dx}{dt}
\right\|
dt.
$$

## Follow-up probabili

- Che differenza c'e' tra curva e parametrizzazione?
- Una stessa curva puo' avere velocita' diverse?
- Quando una parametrizzazione non e' regolare?
- Come si calcola la lunghezza di una circonferenza?
- Perche' serve la norma del vettore tangente?

## Errori da evitare

- Confondere il sostegno geometrico con la parametrizzazione.
- Dimenticare di controllare se il vettore tangente si annulla.
- Dimenticare il fattore $R$ nel vettore tangente della circonferenza o dell'elica.

