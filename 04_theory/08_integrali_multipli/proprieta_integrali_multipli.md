# Proprieta' degli integrali multipli

## Stato

- Fonte: `01_sources/official_slides/10_lezione_integrali_multipli.pdf`
- Slide: 15-16
- Affidabilita': alta

## Linearita'

$$
\int_\Omega[c_1f_1+c_2f_2]\,d\Omega
=
c_1\int_\Omega f_1\,d\Omega
+
c_2\int_\Omega f_2\,d\Omega.
$$

## Additivita' rispetto al dominio

Se $\Omega=\Omega_1\cup\Omega_2$ e $\Omega_1,\Omega_2$ non hanno punti interni comuni:

$$
\int_\Omega f\,d\Omega
=
\int_{\Omega_1}f\,d\Omega
+
\int_{\Omega_2}f\,d\Omega.
$$

## Monotonia

Se $f_1\leq f_2$ su $\Omega$, allora:

$$
\int_\Omega f_1\,d\Omega
\leq
\int_\Omega f_2\,d\Omega.
$$

## Teorema della media

Se $f$ e' continua sulla chiusura di un dominio connesso $\Omega$, allora esiste $x_0\in\overline{\Omega}$ tale che:

$$
f(x_0)=\bar f,
$$

dove:

$$
\bar f=
\frac{1}{m\Omega}
\int_\Omega f(x)\,d\Omega.
$$
