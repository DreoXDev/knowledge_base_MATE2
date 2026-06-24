# Baricentro di un filo tramite integrali di linea

## Stato

- Fonte: `01_sources/official_slides/7_lezione_integrali_linea_I_specie.pdf`
- Slide: 12-14
- Affidabilita': alta

## Formula generale

Per un filo $C$ di densita' $\rho(x,y,z)$, le coordinate del baricentro sono:

$$
x_G=
\frac{\int_C \rho x\,d\ell}{\int_C \rho\,d\ell}
$$

$$
y_G=
\frac{\int_C \rho y\,d\ell}{\int_C \rho\,d\ell}
$$

$$
z_G=
\frac{\int_C \rho z\,d\ell}{\int_C \rho\,d\ell}.
$$

## Caso omogeneo

Se il filo e' omogeneo:

$$
x_G=
\frac{\int_C x\,d\ell}{L}
$$

$$
y_G=
\frac{\int_C y\,d\ell}{L}
$$

$$
z_G=
\frac{\int_C z\,d\ell}{L}
$$

dove:

$$
L=\int_C 1\,d\ell
$$

e' la lunghezza del filo.

## Esempio: elica

Per:

$$
x=a\cos t,\qquad y=a\sin t,\qquad z=ht
$$

con $t\in[0,b]$:

$$
d\ell=\sqrt{a^2+h^2}\,dt
$$

$$
L=b\sqrt{a^2+h^2}
$$

e:

$$
x_G=\frac{a\sin b}{b}
$$

$$
y_G=\frac{a(1-\cos b)}{b}
$$

$$
z_G=\frac{bh}{2}.
$$

## Collegamenti

- [[integrali_linea_I_specie]]
- [[baricentro_filo]]
