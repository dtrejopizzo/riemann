# 104_31 — Flujo en \(\varepsilon\) y stop-gate de observabilidad en \(1/2\)

**Rol.** Auditar el intento de partir de un regulador donde el operador de
Euler converge en norma y transportar hacia atrás el test hard-edge mediante
la recurrencia tridiagonal de Laguerre. El flujo es exacto y tiene una
realización unitaria muy simple: su generador es menos la multiplicación por
\(x\). Precisamente esa realización fija un umbral agudo. El test transportado
hacia atrás pertenece al espacio de Laguerre si y solo si
\(\varepsilon<1/2\), mientras la suma de Euler como operador acotado converge
en norma solo para \(\varepsilon>1/2\). El punto \(1/2\) no pertenece a
ninguno de los dos dominios.

La métrica positiva \(A_{\rm flag}\), que sí interpola exactamente
\(A_{\rm flag}[g_n]=A_n\) para \(n\ge150\), no elimina la colisión. Su espacio
no es invariante por el generador, éste no es simétrico para esa métrica y,
aun después de comprimir, los pesos \(\Delta A_k\asymp\log k\) no cambian el
radio exponencial que produce el umbral.

Este documento es un stop-gate para **esta combinación concreta**:
``operador Euler absolutamente convergente + transporte Hilbert hacia atrás''.
No descarta una identidad renormalizada firmada en dualidad de distribuciones,
no prueba A1 y no prueba RH.

## 1. El flujo exacto de los coeficientes regulados

Para \(\varepsilon>0\), sea

\[
 p_n(\varepsilon)=
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}L_n(\log m),
 \qquad
 j_n(\varepsilon)={ (\varepsilon-1)^n\over\varepsilon^{n+1}},
 \qquad
 c_n=p_n-j_n .                                             \tag{1}
\]

Las series obtenidas al derivar (1) convergen absolutamente en todo
semiplano \(\varepsilon\ge\varepsilon_0>0\). La recurrencia ordinaria

\[
 -xL_n(x)=(n+1)L_{n+1}(x)-(2n+1)L_n(x)+nL_{n-1}(x),          \tag{2}
\]

con \(L_{-1}=0\), da

\[
 p_n'=(n+1)p_{n+1}-(2n+1)p_n+np_{n-1}.                      \tag{3}
\]

El término polar no es una corrección externa al flujo. Tiene la
representación

\[
 j_n(\varepsilon)=\int_0^\infty e^{-\varepsilon x}L_n(x)\,dx,             \tag{4}
\]

y por (2) satisface la misma ecuación. Equivalentemente, una cuenta directa
da

\[
 j_n'={ (\varepsilon-1)^{n-1}\over\varepsilon^{n+2}}
       (n+1-\varepsilon)
 =(n+1)j_{n+1}-(2n+1)j_n+nj_{n-1}.                           \tag{5}
\]

Por tanto, para todo \(n\ge0\), con \(c_{-1}=0\),

\[
 \boxed{c_n'=(n+1)c_{n+1}-(2n+1)c_n+nc_{n-1}.}               \tag{6}
\]

No se separó el límite \(\varepsilon\downarrow0\): (6) vale antes de la
colisión polo--primos.

## 2. Realización unitaria: \(Q=-M_x\)

Sea

\[
 \mathcal H=L^2((0,\infty),e^{-x}dx).
\]

Los polinomios \(L_0,L_1,\ldots\) son una base ortonormal de
\(\mathcal H\). La aplicación

\[
 U:\ell^2(\mathbb N_0)\longrightarrow\mathcal H,
 \qquad Ua=\sum_{n\ge0}a_nL_n                                  \tag{7}
\]

es unitaria. Si \(X=M_x\), con dominio

\[
 \mathcal D(X)=\{f\in\mathcal H:xf\in\mathcal H\},
\]

entonces (2) prueba

\[
 U^{-1}(-X)U=Q,
 \qquad
 (Qa)_n=(n+1)a_{n+1}-(2n+1)a_n+na_{n-1}.                    \tag{8}
\]

Así, \(Q\) es autoadjunto, no positivo, tiene espectro
\(( -\infty,0]\), y

\[
 Ue^{tQ}U^{-1}=M_{e^{-tx}}\qquad(t\ge0).                    \tag{9}
\]

La sucesión completa \(c(\varepsilon)\) no se afirma aquí como un vector de
\(\ell^2\): los átomos primos definen naturalmente un funcional más
singular. Las ecuaciones (7)--(9) dicen qué exigiría una implementación
Hilbert del transporte débil. Para un test finito \(a\), transportar desde
\(\varepsilon\) hasta cero obliga a mover el test por el adjunto:

\[
 \langle a,c(0)\rangle
 =\langle e^{-\varepsilon Q}a,c(\varepsilon)\rangle,
 \qquad
 Ue^{-\varepsilon Q}a=e^{\varepsilon x}Ua,                   \tag{10}
\]

si el miembro derecho pertenece al dominio de la dualidad usada.

## 3. Umbral agudo del prefijo hard-edge

El vector prefijo de `104_28` es

\[
 u_n=(\underbrace{1,\ldots,1}_{n},0,\ldots),
 \qquad
 Uu_n=P_n(x):=L_{n-1}^{(1)}(x)=\sum_{k=0}^{n-1}L_k(x).        \tag{11}
\]

Como \(P_n\) es un polinomio no nulo de grado \(n-1\), con coeficiente
principal \((-1)^{n-1}/(n-1)!\),

\[
 \|e^{\varepsilon x}P_n\|_{\mathcal H}^2
 =\int_0^\infty |P_n(x)|^2e^{-(1-2\varepsilon)x}\,dx.        \tag{12}
\]

Por tanto

\[
 \boxed{e^{\varepsilon x}P_n\in\mathcal H
        \quad\Longleftrightarrow\quad\varepsilon<\tfrac12.} \tag{13}
\]

En el borde \(\varepsilon=1/2\) queda la integral de un polinomio al
cuadrado; por encima del borde aparece crecimiento exponencial. El blow-up
desde abajo también es exacto en primer orden. Si
\(\delta=1-2\varepsilon\downarrow0\), entonces

\[
 \boxed{
 \|e^{\varepsilon x}P_n\|_{\mathcal H}^2
 \sim { (2n-2)!\over((n-1)!)^2}\,\delta^{-(2n-1)}
 = {2n-2\choose n-1}\delta^{-(2n-1)}.}                       \tag{14}
\]

Luego (13) no es una pérdida de constante: es el dominio maximal del
semigrupo inverso sobre este test.

## 4. El dominio seguro de Euler toca el borde por el otro lado

En la realización de traslaciones de `104_28`, la suma que se querría
construir antes de evaluar sobre \(g_n\) es

\[
 \mathcal E_\varepsilon
 =\sum_{m\ge2}{\Lambda(m)\over m^{1/2+\varepsilon}}
       (S_{\log m}+S_{\log m}^*).                             \tag{15}
\]

Para la traslación unilateral, \(\|S_a\|=1\) y
\(\|S_a+S_a^*\|=2\). En particular, la construcción término a término en
norma está gobernada por

\[
 \sum_{m\ge2}{\Lambda(m)\over m^{1/2+\varepsilon}},          \tag{16}
\]

que converge exactamente cuando \(1/2+\varepsilon>1\). Incluso sin pedir
convergencia absoluta, los sumandos positivos no dan convergencia en norma
en el borde: probando las sumas parciales sobre funciones casi constantes en
intervalos mucho más largos que todos los \(\log m\) presentes, su norma es
arbitrariamente próxima a dos veces la suma escalar correspondiente. Así,

\[
 \boxed{\mathcal E_\varepsilon\text{ converge en norma por esta suma}
        \quad\Longleftrightarrow\quad\varepsilon>\tfrac12.}  \tag{17}
\]

La desigualdad es **estricta**. En \(\varepsilon=1/2\) aparece
\(\sum\Lambda(m)/m\), que diverge. Combinando (13) y (17),

\[
 \{\varepsilon:\text{test backward admisible}\}=(0,1/2),
 \qquad
 \{\varepsilon:\text{operador Euler seguro}\}=(1/2,\infty),             \tag{18}
\]

y el punto común aparente pertenece a ninguno.

Esto no contradice (6b) de `104_28`: después de evaluar sobre el rayo
\(g_n\), el solapamiento aporta otro factor \(m^{-1/2}\) y la **forma
escalar** converge para todo \(\varepsilon>0\). Lo que (18) descarta es
separarla primero como un operador acotado y luego recuperar el borde por
transporte Hilbert.

## 5. Auditoría de la métrica \(A_{\rm flag}\)

Póngase \(M=150\), \(P_M=\sum_{j<M}L_j\), y

\[
 \mathcal H_{\rm flag}
 =\mathrm{span}\,\{P_M,L_M,L_{M+1},\ldots\}\subset\mathcal H.        \tag{19}
\]

La familia mostrada en (19) es ortogonal en \(\mathcal H\). Con
\(d_k=\Delta A_k=A_{k+1}-A_k\), defínase

\[
 \left\|a_0P_M+\sum_{k\ge M}a_kL_k\right\|_{A_{\rm flag}}^2
 =A_M|a_0|^2+\sum_{k\ge M}d_k|a_k|^2.                         \tag{20}
\]

Como \(d_k>0\) desde mucho antes de \(M\), (20) es positiva. Además,

\[
 P_n=P_M+\sum_{k=M}^{n-1}L_k,
 \qquad
 \boxed{\|P_n\|_{A_{\rm flag}}^2
 =A_M+\sum_{k=M}^{n-1}\Delta A_k=A_n.}                       \tag{21}
\]

La identidad (21) corrige genuinamente la ausencia de una referencia
positiva señalada en `104_28`. No basta, sin embargo, para transportar (6).

### 5.1 La bandera no es invariante por \(Q\)

La telescopía de (2) da

\[
 QP_M=M(L_M-L_{M-1}).                                         \tag{22}
\]

Si \(\Pi_{\rm flag}\) es la proyección ortogonal de \(\mathcal H\) sobre
(19), entonces \(\Pi_{\rm flag}L_{M-1}=P_M/M\), y

\[
 \Pi_{\rm flag}QP_M=-P_M+ML_M,                               \tag{23}
\]

\[
 (I-\Pi_{\rm flag})QP_M=P_M-ML_{M-1},
 \qquad
 \boxed{\|(I-\Pi_{\rm flag})QP_M\|_{\mathcal H}^2=M(M-1).} \tag{24}
\]

Para \(M=150\), la fuga cuadrática es \(22350\). Por tanto no existe la
restricción \(Q|_{\mathcal H_{\rm flag}}\) como generador del flujo exacto.
Comprimirlo elimina (24) y cambia la dinámica en el borde.

### 5.2 La compresión tampoco es unitaria para \(A_{\rm flag}\)

Sea \(Q_{\rm flag}=\Pi_{\rm flag}Q\Pi_{\rm flag}\). Sus primeras filas son

\[
 \begin{aligned}
 Q_{\rm flag}P_M&=-P_M+ML_M,\\
 Q_{\rm flag}L_M&=P_M-(2M+1)L_M+(M+1)L_{M+1}.
 \end{aligned}                                                \tag{25}
\]

En la cola conserva la matriz tridiagonal ordinaria. Pero (20) da

\[
 \langle Q_{\rm flag}P_M,L_M\rangle_A
 -\langle P_M,Q_{\rm flag}L_M\rangle_A
 =M\Delta A_M-A_M>0,                                         \tag{26}
\]

porque \(A_0=0\) y \(\Delta^2A_j>0\) hacen a
\(\Delta A_j\) estrictamente creciente. Para \(k\ge M\),

\[
 \langle QL_k,L_{k+1}\rangle_A-
 \langle L_k,QL_{k+1}\rangle_A
 =(k+1)(\Delta A_{k+1}-\Delta A_k)
 =(k+1)\Delta^2A_k>0.                                        \tag{27}
\]

Así, cambiar la métrica destruye la autoadjunción que justificaba mover el
semigrupo de un lado al otro en (10). Re-simetrizar (25) modificaría sus
tasas y ya no realizaría la recurrencia (6).

### 5.3 Aun la versión proyectada conserva el umbral \(1/2\)

Hay un test más favorable: ignorar la fuga de dimensión finita y preguntar
solo si la cola Laguerre de \(e^{\varepsilon x}P_n\) tiene norma (20). Para
\(0\le\varepsilon<1\), sean

\[
 a_k^{(n)}(\varepsilon)
 =\int_0^\infty e^{-(1-\varepsilon)x}P_n(x)L_k(x)\,dx.         \tag{28}
\]

La generatriz ordinaria de Laguerre y
\(\int_0^\infty e^{-sx}P_n(x)dx=1-((s-1)/s)^n\) dan la identidad racional

\[
 \boxed{
 \sum_{k\ge0}a_k^{(n)}(\varepsilon)z^k
 ={1\over1-z}\left[
 1-\left({(1+\varepsilon)z-\varepsilon
             \over1-\varepsilon+\varepsilon z}\right)^n
 \right].}                                                   \tag{29}
\]

La singularidad de (29) está en
\(z_0=-(1-\varepsilon)/\varepsilon\). Poniendo
\(r=\varepsilon/(1-\varepsilon)\), extracción en ese polo da, para \(n\)
fijo,

\[
 a_k^{(n)}(\varepsilon)
 =(-1)^{n+k+1}{\varepsilon^{1-n}\over(1-\varepsilon)^n}
   {k+n-1\choose n-1}r^k
   +O_{n,\varepsilon}(k^{n-2}r^k).                            \tag{30}
\]

Para \(n=1\) el término de error se omite; para \(\varepsilon=0\) la
sucesión es simplemente el prefijo finito original.

Por la fórmula exacta de `103_52`,

\[
 \Delta A_k=-{\gamma+\log(4\pi)\over2}
 +\sum_{\ell\ \mathrm{impar}}{1-(1-1/\ell)^k\over\ell},    \tag{31}
\]

se tiene \(\Delta A_k\asymp\log k\) y, para \(k\ge M\),
\(\Delta A_k\ge\Delta A_M>0\). Las ecuaciones (30)--(31) prueban

\[
 \boxed{
 \sum_{k\ge M}\Delta A_k|a_k^{(n)}(\varepsilon)|^2<\infty
 \quad\Longleftrightarrow\quad\varepsilon<\tfrac12.}       \tag{32}
\]

La métrica positiva no mueve el borde; lo hace más singular por un factor
logarítmico. En efecto, en \(\varepsilon=1/2\),

\[
 \sum_{M\le k\le K}\Delta A_k|a_k^{(n)}(1/2)|^2
 \asymp_n K^{2n-1}\log K,                                   \tag{33}
\]

y para \(1/2<\varepsilon<1\) crece como

\[
 \asymp_{n,\varepsilon}r^{2K}K^{2n-2}\log K.                 \tag{34}
\]

Desde abajo, la norma cuadrática de la cola tiene orden

\[
 (1-2\varepsilon)^{-(2n-1)}
 \log{1\over1-2\varepsilon}.                                \tag{35}
\]

Por consiguiente \(A_{\rm flag}\) sí construye el denominador escalar
correcto sobre cada prefijo, pero no crea un solapamiento entre el dominio
Euler seguro y el dominio del transporte inverso.

## 6. Alcance del stop-gate

Queda probado:

1. el flujo exacto (6), antes de retirar el regulador;
2. la realización autoadjunta \(Q=-M_x\);
3. el umbral agudo (13), con blow-up (14);
4. el umbral estricto de convergencia en norma (17);
5. que \(\mathcal H_{\rm flag}\) no es invariante, que \(Q_{\rm flag}\) no
   es \(A_{\rm flag}\)-simétrico y que incluso su cola proyectada conserva
   el mismo umbral.

Se descarta únicamente el siguiente movimiento:

> construir primero el canal primo como operador acotado en un regulador
> Euler seguro y recuperar el observable de A1 aplicando el semigrupo
> birth--death hacia atrás en un espacio Hilbert de Laguerre.

Sigue abierto un teorema que conserve polo, Gamma y primos como un único
funcional renormalizado firmado. Tal teorema no puede justificarse por el
solapamiento de dominios de este flujo: ese solapamiento es vacío.

## 7. Verificación

Desde `phase-104-unconditional-a1-closure/tools`:

```bash
python3 epsilon_flow_observability_gate_check.py
```

El script usa solo `Fraction`. Verifica (2), el flujo polar (5), la generatriz
(29) contra integración exacta para varios grados y reguladores, y la fuga
(24) con valor \(22350\) para \(M=150\).
