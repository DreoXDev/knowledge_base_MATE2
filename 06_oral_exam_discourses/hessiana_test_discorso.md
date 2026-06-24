# Discorso orale: Hessiana e classificazione dei punti stazionari

## Versione breve

Per classificare un punto stazionario si usa Taylor al secondo ordine. Poiche' in un punto stazionario il termine lineare si annulla, il comportamento locale della funzione e' determinato, almeno nei casi non degeneri, dalla parte quadratica:

$$
\frac{1}{2}
\left[
f_{xx}(P)(\Delta x)^2
+
2f_{xy}(P)\Delta x\Delta y
+
f_{yy}(P)(\Delta y)^2
\right].
$$

Questa parte quadratica e' associata alla matrice Hessiana:

$$
H(P)=
\begin{pmatrix}
f_{xx}(P) & f_{xy}(P)\\
f_{yx}(P) & f_{yy}(P)
\end{pmatrix}.
$$

Nel caso di due variabili si pone:

$$
D(P)=f_{xx}(P)f_{yy}(P)-f_{xy}(P)^2.
$$

Se $D(P)>0$ e $f_{xx}(P)>0$, il punto e' minimo locale. Se $D(P)>0$ e $f_{xx}(P)<0$, e' massimo locale. Se $D(P)<0$, e' punto sella. Se $D(P)=0$, il test e' inconclusivo.

## Follow-up

- Perche' il caso $D=0$ e' inconclusivo?
- Che relazione c'e' tra Hessiana e forma quadratica?
- Come si collega il test a Taylor?

