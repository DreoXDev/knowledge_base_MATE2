# Teorema fondamentale del calcolo integrale

## Definizione operativa

Se $g:[a,b]\to\mathbb R$ e' derivabile con derivata integrabile, allora:

$$
\int_a^b g'(t)\,dt=g(b)-g(a).
$$

## Formula da ricordare

Nel contesto dei campi conservativi si applica alla funzione composta:

$$
g(t)=U(\gamma(t)).
$$

Quindi:

$$
\int_a^b \frac{d}{dt}U(\gamma(t))\,dt
=
U(\gamma(b))-U(\gamma(a)).
$$

## Collegamento ai campi conservativi

Nel discorso sui [[Campi conservativi - discorso orale completo|campi conservativi]] questo teorema chiude la dimostrazione:

$$
\int_\gamma \vec F\cdot d\vec r
=
U(P_2)-U(P_1).
$$

Il passaggio precedente usa la [[derivazione_funzione_composta|derivazione della funzione composta]].

## Domanda orale tipica

**Domanda:** quale teorema usi per passare dall'integrale della derivata alla differenza di potenziale?

**Risposta:** uso il teorema fondamentale del calcolo integrale applicato alla funzione $t\mapsto U(\gamma(t))$.
