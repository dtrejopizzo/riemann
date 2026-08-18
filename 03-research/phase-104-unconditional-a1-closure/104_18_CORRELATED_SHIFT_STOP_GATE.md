# 104_18 — Desplazamiento correlacionado finito: identidad y stop-gate

**Rol.** Mantener finitos y correlacionados el regulador
\(\varepsilon\downarrow0\) y el desplazamiento de Jordan \(u\downarrow0\),
antes de tomar el primer jet. El objetivo era comprobar si la positividad
exacta de \(J_u\) sobrevive a la colisión polo--Euler y produce la cota de
A1. El resultado es negativo pero preciso: se obtiene una identidad finita
nueva, una ecuación de renovación exacta y tres falsificadores. El límite
vuelve al costo firmado \(C_n\) de `104_16`.

Este documento **no prueba A1 ni RH**.

## 1. Pre-registro y no duplicación interna

Sean

\[
 F(s)=(s-1)\zeta(s),\qquad
 A_u(s)={\zeta(s-u)\over\zeta(s)},\qquad
 H_u(s)={F(s-u)\over F(s)}.
 \tag{1}
\]

`104_16` ya demostró el jet infinitesimal

\[
 \left.\partial_uH_u(s)\right|_{u=0}=-{F'(s)\over F(s)}
 \tag{2}
\]

y su pullback Cayley--Laguerre. Lo que se ensaya aquí no es otro jet:
se fija

\[
 s_\varepsilon(z)=1+\varepsilon+{z\over1-z},
 \qquad u=c\varepsilon,qquad 0<c<1,                 \tag{3}
\]

y se conserva \(H_{c\varepsilon}\) exacto hasta después de extraer el
coeficiente.

**Inputs permitidos.** Solo se usan la serie absolutamente convergente de
\(A_u\) en \(\Re s>1+u\), la identidad generatriz de Laguerre, sumación de
Abel y el orden real de \(F\) en \((1,\infty)\).

**Falsificador obligatorio.** Cualquier inferencia de signo debe sobrevivir
al producto simétrico \(X_a(s)=\xi(s+a)\xi(s-a)\), que tiene ceros fuera de
la línea \(1/2\) para todo \(a>0\).

## 2. Teorema de coeficientes finitos

Para \(\Re s>1+u\),

\[
 A_u(s)=\sum_{m\ge1}{J_u(m)\over m^s},
 \qquad
 J_u(m)=m^u\prod_{p\mid m}(1-p^{-u})\ge0.            \tag{4}
\]

Defínase

\[
 a_n(u,\varepsilon)
 :=\sum_{m\ge1}{J_u(m)\over m^{1+\varepsilon}}
                    L_n(\log m).                    \tag{5}
\]

La identidad generatriz

\[
 {e^{-xz/(1-z)}\over1-z}=\sum_{n\ge0}L_n(x)z^n
\]

da, para \(z\) en un entorno del origen,

\[
 \boxed{
 {A_u(s_\varepsilon(z))\over1-z}
 =\sum_{n\ge0}a_n(u,\varepsilon)z^n.}               \tag{6}
\]

Como

\[
 H_u(s)=\left(1-{u\over s-1}\right)A_u(s),          \tag{7}
\]

para \(u=c\varepsilon\) el factor polar es exactamente

\[
 P_{c,\varepsilon}(z)
 ={(1-c)\varepsilon+[1-(1-c)\varepsilon]z
   \over \varepsilon+(1-\varepsilon)z}.             \tag{8}
\]

Si

\[
 {H_u(s_\varepsilon(z))\over1-z}
 =\sum_{n\ge0}b_n(u,\varepsilon)z^n,                \tag{9}
\]

entonces (6)--(8) prueban la recurrencia finita

\[
 \boxed{
 \begin{aligned}
  \varepsilon b_0&=(\varepsilon-u)a_0,\\
  \varepsilon b_n+(1-\varepsilon)b_{n-1}
   &=(\varepsilon-u)a_n+(1-\varepsilon+u)a_{n-1},
       \qquad n\ge1.
 \end{aligned}}                                      \tag{10}
\]

No se ha separado ninguna cantidad divergente: (10) conserva acoplados el
polo y los coeficientes positivos de Jordan.

## 3. Forma de renovación exacta

Póngase

\[
 G_{n,c,\varepsilon}
 :=[z^n]{H_{c\varepsilon}(s_\varepsilon(z))-1
             \over c\varepsilon(1-z)}.              \tag{11}
\]

Y sea

\[
 S_u(x):=\sum_{m\le x}{J_u(m)\over m}.              \tag{12}
\]

Entonces

\[
 \boxed{
 \begin{aligned}
 G_{n,c,\varepsilon}
 &=\sum_{m\ge2}{J_u(m)\over u\,m^{1+\varepsilon}}
                    L_n(\log m)\\
 &\quad-\int_1^\infty x^{-1-\varepsilon}L_n(\log x)
                    S_u(x)\,dx,
 \qquad u=c\varepsilon.
 \end{aligned}}                                      \tag{13}
\]

*Demostración.* De (7),

\[
 {H_u(s)-1\over u}={A_u(s)-1\over u}-{A_u(s)\over s-1}. \tag{14}
\]

El primer término produce la suma de (13) mediante (6). Para el segundo,
sumación de Abel da, absolutamente en el semiplano usado,

\[
 {A_u(s)\over s-1}
 =\int_1^\infty x^{-s}S_u(x)\,dx.                   \tag{15}
\]

Aplicar la misma generatriz de Laguerre dentro de (15) prueba (13).
\(\square\)

La fórmula (13) exhibe el problema sin estimaciones: es la diferencia de
dos medidas positivas, pero ambas se prueban contra el polinomio firmado
\(L_n\). La positividad de \(J_u\) no decide el signo.

## 4. El límite correlacionado es independiente de \(c\)

Para cada \(n\ge1\) fijo, la analiticidad de \(F\) en \(s=1\) y (2) dan

\[
 \lim_{\varepsilon\downarrow0}G_{n,c,\varepsilon}
 =[z^n]{-F'(1+z/(1-z))/F(1+z/(1-z))\over1-z}.       \tag{16}
\]

La identidad exacta de `103_59`/`104_16` identifica este coeficiente como

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}G_{n,c,\varepsilon}
 =C_n:=\lambda_n^{\rm prime}-\lambda_{n+1}^{\rm prime},} \tag{17}
\]

independientemente de \(c\in(0,1)\). En particular, conservar el
desplazamiento finito no crea un margen nuevo: al retirar el regulador
regresa exactamente el gate anterior.

## 5. El orden real no controla los coeficientes Cayley

Alzer--Kwong, Corolario 4.1, prueba que

\[
 {(s-1)\zeta(s)\over s^\alpha}
 \quad\hbox{es estrictamente creciente en }(1,\infty)
 \quad\Longleftrightarrow\quad \alpha\le\gamma.
\]

La elección \(\alpha=0\) implica que \(F\) es estrictamente creciente.
Por tanto, para \(0\le r<1\),

\[
 0<H_{c\varepsilon}(s_\varepsilon(r))<1.            \tag{18}
\]

Sin embargo, `104_16` certifica exactamente

\[
 C_6\in
 [0.008107486973374973910460,
  0.008107486973374973910461].                       \tag{19}
\]

Por (17), para cada \(c\in(0,1)\) fijo se tiene
\(G_{6,c,\varepsilon}>0\) para todo \(\varepsilon>0\)
suficientemente pequeño, aunque la función de (11) sea negativa sobre el
rayo real. Así, el orden radial (18) no implica orden coeficiente a
coeficiente tras el pullback Cayley.

Referencia: H. Alzer y M. K. Kwong, *Some inequalities for the Riemann
zeta function*, Rend. Istit. Mat. Univ. Trieste 53 (2021),
[PDF oficial](https://rendiconti.dmi.units.it/volumi/53/005.pdf).

## 6. La variable \(c\) tampoco es completamente monótona

En el centro \(z=0\), defínase

\[
 h_\varepsilon(c)
 :=H_{c\varepsilon}(1+\varepsilon)
 ={F(1+(1-c)\varepsilon)\over F(1+\varepsilon)}.    \tag{20}
\]

Entonces

\[
 h_\varepsilon'''(c)
 =-\varepsilon^3{F'''(1+(1-c)\varepsilon)
                    \over F(1+\varepsilon)}.        \tag{21}
\]

Con la convención

\[
 \zeta(1+t)={1\over t}+
     \sum_{k\ge0}{(-1)^k\gamma_k\over k!}t^k,
\]

se tiene \(F'''(1)=3\gamma_2<0\). El signo no se toma de una aproximación:
`tools/jordan_cocycle_sign_gate.py` certifica racionalmente

\[
 -3\gamma_2\in
 [0.029071089578616955453591,
  0.029071089578616955453592].
\]

Por continuidad, existe
\(\varepsilon_0>0\) tal que \(h_\varepsilon'''(c)>0\) para
\(0<\varepsilon<\varepsilon_0\) y \(0\le c\le3/4\). Integrando tres veces,

\[
 \boxed{
 h_\varepsilon(3/4)-3h_\varepsilon(1/2)
 +3h_\varepsilon(1/4)-h_\varepsilon(0)>0.}          \tag{22}
\]

Una representación Hausdorff/completamente monótona exigiría que esta
tercera diferencia fuera \(\le0\). El fallo ocurre ya antes de extraer
coeficientes en \(z\).

## 7. No-go para anular idénticamente el canal explícito con shifts finitos

Sean \(c_1,\ldots,c_M>0\) distintos y \(w_1,\ldots,w_M\) constantes.
En una combinación lineal de (7) con **pesos constantes**, la anulación
idéntica del canal explícito proporcional a \((s-1)^{-1}\) exigiría

\[
 \sum_{j=1}^M w_jc_jA_{c_j\varepsilon}(s)=0.        \tag{23}
\]

Multiplicando por \(\zeta(s)\),

\[
 \sum_{j=1}^M w_jc_j\zeta(s-c_j\varepsilon)=0.     \tag{24}
\]

La unicidad de series de Dirichlet convierte (24) en
\(\sum_jw_jc_jm^{c_j\varepsilon}=0\) para todo \(m\). Hacer
\(m\to\infty\) elimina sucesivamente el exponente mayor y prueba

\[
 w_1=\cdots=w_M=0.                                  \tag{25}
\]

Esto no afirma que \(H_u\) tenga un polo real en \(s=1\): el cero de
\(A_u\) cancela el factor aparente. Afirma solo que ningún sistema finito de
pesos constantes borra por separado ese canal en la identidad (7).

Para los shifts normalizados \((H_{c_j\varepsilon}-1)/(c_j\varepsilon)\),
la misma prueba se aplica sin el factor \(c_j\). En esa familia normalizada,
cancelar solo el primer orden mediante \(\sum_jw_j=0\) tampoco ayuda: por
(17), cancela simultáneamente el objetivo \(C_n\).

Dentro de la clase de productos finitos de los factores explícitos
\((1-c_jx)\) con exponentes constantes, una combinación multiplicativa
tampoco puede borrar ese canal. Si

\[
 \prod_{j=1}^M(1-c_jx)^{\alpha_j}\equiv1,           \tag{26}
\]

el logaritmo de (26) da
\(\sum_j\alpha_jc_j^k=0\) para todo \(k\ge1\). Las primeras \(M\)
ecuaciones forman un sistema de Vandermonde y fuerzan
\(\alpha_1=\cdots=\alpha_M=0\).

## 8. Falsificador off-line

Sea

\[
 X_a(s)=\xi(s+a)\xi(s-a),\qquad 0<a<\tfrac12.       \tag{27}
\]

Esta función satisface \(X_a(1-s)=X_a(s)\) y tiene ceros
\(1/2\pm a+i\gamma\), fuera de la línea de simetría. Su componente
polo--Euler es

\[
 F_a(s)=F(s+a)F(s-a),
\]

y el cociclo factoriza como

\[
 {F_a(s-u)\over F_a(s)}=H_u(s+a)H_u(s-a).           \tag{28}
\]

En el semiplano real seguro, ambos factores satisfacen el orden (18). Las
series de los cocientes Euler son productos de series con coeficientes
Jordan no negativos en \(\Re s>1+a+u\). Por tanto esos inputs locales son
compatibles con ceros fuera de la línea. Este ejemplo, por sí solo, no
transporta la positividad hasta el germen Cayley crítico; la obstrucción
precisa para tal regla de continuación se demuestra en `104_19` §7.

## 9. Veredicto y sucesor

El desplazamiento correlacionado deja cuatro resultados exactos:

1. la recurrencia finita (10);
2. la renovación acoplada (13);
3. el colapso inevitable al costo firmado (17);
4. los stop-gates (19), (22), (25)--(28).

Queda descartada esta inferencia:

\[
 J_{c\varepsilon}\ge0
 +H_{c\varepsilon}<1\text{ en el rayo real}
 \quad\Longrightarrow\quad
 C_n\text{ tiene el signo requerido}.              \tag{29}
\]

El sucesor mínimo que conserva además la mitad Gamma del strong margin es
el cociclo sin ramas

\[
 \mathcal S_u(s)={Y(s-u)\over Y(s)}=H_u(s)^2K_u(s), \tag{30}
\]

con \(Y\) de `103_49`/`103_59`. No es un objeto nuevo: es el cuadrado del
medio-cociclo de `104_16`. Solo queda por auditar si sus tres canales
finitos

\[
 A_u(s)^2\left(1-{2u\over s-1}+{u^2\over(s-1)^2}\right)K_u(s) \tag{31}
\]

conservan una cancelación que se pierde al tomar el jet. Ese es el ataque
siguiente; (17) impide contarlo de antemano como progreso hacia A1.
