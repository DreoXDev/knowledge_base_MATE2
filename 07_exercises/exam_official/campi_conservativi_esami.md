# Esercizi ufficiali - Campi conservativi e potenziale

## Pattern generale

1. Riconoscere se il campo sembra costruito come gradiente.
2. Integrare una componente.
3. Aggiungere una funzione delle variabili rimanenti.
4. Verificare tutte le componenti di $\nabla U=F$.

## 13 aprile 2023 - Esercizio 3

### Traccia

$$
F_1=\ln(y^2z^2+1)
$$

$$
F_2=\frac{2xyz^2}{y^2z^2+1}
$$

$$
F_3=\frac{2xy^2z}{y^2z^2+1}
$$

### Potenziale

$$
U=x\ln(y^2z^2+1)
$$

### Verifica

$$
U_x=\ln(y^2z^2+1)
$$

$$
U_y=\frac{2xyz^2}{y^2z^2+1}
$$

$$
U_z=\frac{2xy^2z}{y^2z^2+1}
$$

## 14 luglio 2022 - Esercizio 5

### Traccia

$$
F_1=e^{z^2+y}+z^2e^{x+y}+ye^{z^2+x}
$$

$$
F_2=xe^{z^2+y}+z^2e^{x+y}+e^{z^2+x}
$$

$$
F_3=2xze^{z^2+y}+2ze^{x+y}+2yze^{z^2+x}
$$

### Potenziale

$$
U=xe^{z^2+y}+z^2e^{x+y}+ye^{z^2+x}
$$

## 22 novembre 2022 - Esercizio 5

### Traccia

$$
F_1=
\frac{2xy}{x^2+z^2+1}
+
\frac{2xz}{x^2+y^2+1}
$$

$$
F_2=
\ln(x^2+z^2+1)
+
\frac{2yz}{x^2+y^2+1}
$$

$$
F_3=
\ln(x^2+y^2+1)
+
\frac{2yz}{x^2+z^2+1}
$$

### Nota di verifica

Verificato sul PDF sorgente `01_sources/exams/esame_2022_11_22.pdf` con estrazione testuale: la terza componente e' coerente con il potenziale candidato sotto.

### Potenziale

$$
U=
y\ln(x^2+z^2+1)
+
z\ln(x^2+y^2+1)
$$

## Errori da evitare

- Dichiarare conservativo senza verificare $\nabla U=F$.
- Correggere un possibile refuso senza segnalarlo come dubbio.

## 22 febbraio 2023 - Campo con parametri

### Pattern

Il campo e' conservativo quando:

$$
a=b=c=1
$$

e il potenziale e':

$$
U=xe^{yz}+ze^{xy}+ye^{xz}
$$

## 24/27 settembre 2022 - Potenziale logaritmico ciclico

### Potenziale

$$
U=
x\ln(y^2+1)
+
y\ln(z^2+1)
+
z\ln(x^2+1)
$$

### Pattern

Ogni componente deriva da un termine logaritmico ciclico e da una derivata della variabile dentro il logaritmo.

## 19 luglio 2023 - Potenziale logaritmico in $z$

### Potenziale

$$
U=(xy^2+x^2y)\ln(z^2+1)
$$

### Verifica

$$
U_x=(y^2+2xy)\ln(z^2+1)
$$

$$
U_y=(2xy+x^2)\ln(z^2+1)
$$

$$
U_z=(xy^2+x^2y)\frac{2z}{z^2+1}
$$
