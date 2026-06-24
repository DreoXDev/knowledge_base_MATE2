# Lunghezza di un arco di curva

## Stato

- Fonte: `01_sources/official_slides/1_lezione_II_2022_23_SDM.pdf`
- Slide: 13-17
- Affidabilita': alta
- Ultimo aggiornamento: 2026-06-23

## Idea intuitiva

La lunghezza di una curva si ottiene sommando le lunghezze di piccoli segmenti che approssimano localmente la curva.

Nel limite, questa somma diventa l'integrale della norma del vettore tangente.

## Formula

Sia:

$$
x_i=x_i(t),\qquad i=1,\dots,n
$$

una curva regolare con $t\in[a,b]$.

La lunghezza dell'arco e':

$$
\ell
=
\int_a^b
\left\|
\frac{dx}{dt}
\right\|
dt
$$

cioe':

$$
\ell
=
\int_a^b
\sqrt{
\left(\frac{dx_1}{dt}\right)^2
+
\cdots
+
\left(\frac{dx_n}{dt}\right)^2
}
\,dt.
$$

## Derivazione intuitiva

Per una curva:

$$
x_i=x_i(t),\qquad i=1,\dots,n
$$

su un intervallo $[\bar{t},\bar{t}+\Delta t]$, si approssima localmente ogni componente con Taylor del primo ordine:

$$
x_i^{lin}(t)
=
x_i(\bar{t})
+
\frac{dx_i}{dt}(\bar{t})(t-\bar{t}).
$$

Il segmento approssimante ha lunghezza:

$$
\sqrt{
\left(\frac{dx_1}{dt}(\bar{t})\right)^2
+
\cdots
+
\left(\frac{dx_n}{dt}(\bar{t})\right)^2
}
\Delta t.
$$

Suddividendo $[t_1,t_2]$ in $N$ sottointervalli di lunghezza:

$$
\Delta t=\frac{t_2-t_1}{N}
$$

si ottiene la somma:

$$
\sum_{i=0}^{N-1}
\sqrt{
\left(\frac{dx_1}{dt}(t_1+i\Delta t)\right)^2
+
\cdots
+
\left(\frac{dx_n}{dt}(t_1+i\Delta t)\right)^2
}
\Delta t.
$$

Per $N\to\infty$ questa somma tende alla formula integrale della lunghezza.

## Esempio: segmento

Un segmento nel piano puo' essere parametrizzato da:

$$
x(t)=(x_2-x_1)t+x_1,\qquad
y(t)=(y_2-y_1)t+y_1,\qquad t\in[0,1].
$$

La lunghezza e':

$$
\ell
=
\int_0^1
\sqrt{
(x_2-x_1)^2+(y_2-y_1)^2
}
\,dt
$$

quindi:

$$
\ell
=
\sqrt{
(x_2-x_1)^2+(y_2-y_1)^2
}.
$$

## Esempio: circonferenza

Per la circonferenza:

$$
x(t)=R\cos t,\qquad y(t)=R\sin t,\qquad t\in[0,2\pi],
$$

la norma del vettore tangente e' $R$. Quindi:

$$
\ell
=
\int_0^{2\pi} R\,dt
=
2\pi R.
$$

## Intuizione geometrica

La quantita':

$$
\left\|
\frac{dx}{dt}
\right\|
$$

rappresenta la velocita' scalare con cui la curva viene percorsa.

Per questo la lunghezza totale e' l'integrale della velocita' scalare nel tempo.

## Collegamento con integrali di linea di I specie

La lunghezza di un arco e' il caso particolare dell'integrale di linea di I specie con funzione integranda costante $f=1$:

$$
L=\int_C 1\,d\ell.
$$

Fonte: `01_sources/official_slides/7_lezione_integrali_linea_I_specie.pdf`, slide 1-3.

## Grafici / Figure

- Approssimazione tramite segmenti: `08_visuals/figures/lezione_II_slide_17_approssimazione_lunghezza.png`

## Collegamenti

- [[curve_parametrizzate]]
- [[integrale_linea_prima_specie]]

## Domande orali possibili

- Come si definisce la lunghezza di un arco di curva regolare?
- Perche' nella formula compare la norma del vettore tangente?
- Come si ottiene la lunghezza della circonferenza?
- Come si motiva la formula con l'approssimazione tramite segmenti?
