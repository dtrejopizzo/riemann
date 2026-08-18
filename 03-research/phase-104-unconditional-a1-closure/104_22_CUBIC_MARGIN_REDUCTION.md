# 104_22 — Reducción cúbica estrictamente más débil de A1

**Rol.** Retener un factor que la prueba publicada de A0 descarta y usarlo
para reemplazar el margen fuerte

\[
 2\lambda_n-A_n\ge0
\]

por el margen estrictamente más débil

\[
 \boxed{D_n^{[3]}:=3\lambda_n-A_n\ge0.}           \tag{1}
\]

Este reemplazo sí implica la **A1 original**, con el mismo coeficiente
\(1/4\) y el mismo cutoff, no una variante de la desigualdad. El cociclo
cúbico asociado tiene tres copias Euler positivas y dos copias Gamma
positivas. Probar su signo global cerraría A1 y RH. El signo todavía no se
prueba en este documento.

## 1. El factor retenido en A0

La última línea de la prueba de `thm:a0-tail-direct` es, antes de relajarla,

\[
 |R_n(T_n)|
 \le {B_n\over4}\int_{T_n}^{\infty}(1+u)^{-2}\,du,
 \qquad 0<B_n\le A_n.                              \tag{2}
\]

La integral de (2) se evalúa exactamente. Por tanto A0 prueba en realidad

\[
 \boxed{
 |R_n(T_n)|\le {B_n\over4(1+T_n)}
              \le {A_n\over4(1+T_n)}.}             \tag{3}
\]

La cota impresa \(|R_n(T_n)|\le A_n/4\) se obtiene de (3) descartando el
factor \((1+T_n)^{-1}\). No se añade ninguna hipótesis y no se usa RH.
Para la tripla efectiva fijada en `104_01`, \(T_n\ge U_0=1000\); para la
versión abstracta basta reemplazar cualquier cutoff admisible por
\(\max(T_n,2)\).

## 2. Teorema de reducción cúbica

Recordemos la identidad exacta para la A1 original:

\[
 C_n(T_n)=\lambda_n-{1\over4}A_n-R_n(T_n).         \tag{4}
\]

**Teorema 2.1.** Supóngase \(A_n>0\), \(T_n\ge2\), (3) y
\(D_n^{[3]}\ge0\). Entonces \(C_n(T_n)\ge0\), y por tanto A1 vale para ese
índice.

**Demostración.** De \(3\lambda_n-A_n\ge0\) se obtiene
\(\lambda_n\ge A_n/3\). Usando (3) en (4),

\[
 \begin{aligned}
 C_n(T_n)
 &\ge {A_n\over3}-{A_n\over4}-|R_n(T_n)|\\
 &\ge {A_n\over12}-{A_n\over4(1+T_n)}\ge0,
 \end{aligned}                                    \tag{5}
\]

porque \(T_n\ge2\). \(\square\)

El target (1) es estrictamente más débil que el usado en `103_59`--`104_21`.
En efecto, \(2\lambda_n-A_n\ge0\) implica
\(3\lambda_n-A_n\ge A_n/2>0\), mientras que el valor algebraico
\(\lambda_n=A_n/3\) satisface (1) y viola el margen cuadrático.

## 3. La familia completada y el cociclo cúbico

Póngase

\[
 G(s)=s\pi^{-s/2}\Gamma(s/2),\qquad
 Y_r(s)={\xi(s)^r\over G(s)},\qquad r\ge2.         \tag{6}
\]

Las definiciones de los coeficientes de Li y de la parte arquimediana dan

\[
 \log{Y_r((1-z)^{-1})\over Y_r(1)}
 =\sum_{n\ge1}{D_n^{[r]}\over n}z^n,
 \qquad D_n^{[r]}=r\lambda_n-A_n.                 \tag{7}
\]

Sea

\[
 F(s)=(s-1)\zeta(s),\quad
 H_u(s)={F(s-u)\over F(s)},\quad
 K_u(s)=\pi^{u/2}{\Gamma(1+(s-u)/2)\over
                         \Gamma(1+s/2)}.           \tag{8}
\]

Como \(\xi(s)=\tfrac12G(s)F(s)\) y
\(G(s-u)/G(s)=K_u(s)\), se tiene la factorización exacta

\[
 \boxed{
 {Y_r(s-u)\over Y_r(s)}=H_u(s)^rK_u(s)^{r-1}.}    \tag{9}
\]

Para \(r=3\), el frente nuevo es

\[
 \boxed{\mathcal S_u^{[3]}(s)=H_u(s)^3K_u(s)^2.} \tag{10}
\]

En el semiplano \(\Re s>1+u\), las tres copias Euler tienen la serie

\[
 \left({\zeta(s-u)\over\zeta(s)}\right)^3
 =\sum_{m\ge1}{(J_u*J_u*J_u)(m)\over m^s},
 \qquad J_u*J_u*J_u\ge0,                           \tag{11}
\]

y las dos copias de \(K_u\) son la convolución de dos medidas Beta
positivas. Los únicos signos explícitos están en el factor polar
\((1-u/(s-1))^3\); deben conservarse acoplados con (11) y Gamma.

La transformada inversa de Laplace de ese factor, en la coordenada usada
por (12), tiene los cuatro canales exactos

\[
 \delta_0-3u e^{-\varepsilon y}\,dy
 +3u^2y e^{-\varepsilon y}\,dy
 -{u^3\over2}y^2e^{-\varepsilon y}\,dy.           \tag{11a}
\]

Tras \(u=c\varepsilon\), \(r=\varepsilon y\), la parte continua es

\[
 c\left(-3+3cr-{c^2r^2\over2}\right)e^{-r}\,dr. \tag{11b}
\]

Es negativa cerca de cero y para \(r\) grande, para todo \(c>0\). Por
tanto el margen cúbico no se obtiene declarando positivos los cuatro
canales por separado: la ventaja de (1) debe explotarse en la suma global
Euler--Gamma--polo.

## 4. Coeficientes y gate exacto

Fijemos

\[
 s_\varepsilon(z)=1+\varepsilon+{z\over1-z},
 \qquad u=c\varepsilon,\quad0<c<1,                \tag{12}
\]

y definamos la normalización que apunta **directamente** al margen, sin
introducir una diferencia primera innecesaria,

\[
 {\mathcal S_{c\varepsilon}^{[3]}(s_\varepsilon(z))-1
  \over c\varepsilon(1-z)^2}
 =\sum_{m\ge0}h_{m,\varepsilon,c}^{[3]}z^m.       \tag{13}
\]

Al retirar el regulador,

\[
 {\mathcal S_u^{[3]}(s)-1\over u}
 \longrightarrow-{(Y_3)'(s)\over Y_3(s)}.
\]

Diferenciando (7) y usando \((1-z)^{-2}=s^2\) resulta

\[
 \boxed{
 h_{n-1,\varepsilon,c}^{[3]}
 \longrightarrow-D_n^{[3]}=-(3\lambda_n-A_n),
 \qquad n\ge1.}                                   \tag{14}
\]

En efecto,

\[
 s^2{(Y_3)'(s)\over Y_3(s)}
 ={d\over dz}\log Y_3((1-z)^{-1})
 =\sum_{n\ge1}D_n^{[3]}z^{n-1}.                   \tag{15}
\]

Por tanto basta probar \(h_{n-1,\varepsilon,c}^{[3]}\le0\) al retirar el
regulador, para todo \(n\ge150\). Esta condición converge exactamente al
gate cúbico directo \(D_n^{[3]}\ge0\); no exige la condición más fuerte
\(\Delta D_n^{[3]}\ge0\). El Teorema 2.1 y la cadena ya probada
A1 \(\Rightarrow\Omega_7\Rightarrow\) RH completarían entonces el objetivo.

La normalización anterior de `104_19`, con solo \((1-z)^{-1}\), sigue siendo
válida, pero converge a \(-\Delta D_n^{[3]}\). Se conserva únicamente como
herramienta opcional si una identidad de diferencias la favorece; no es el
target principal.

## 5. Identidad local de tercer orden

La factorización de torres de `104_20` se generaliza sin pérdida para todo
**entero** \(r\ge1\). Si \(Q=p^u\) y

\[
 a_k^{[r]}={k+r-1\choose r-1}Q^k,
 \]

con \(a_k^{[r]}=0\) para \(k<0\), entonces

\[
 (J_u^{*r})(p^k)=\nabla^r a_k^{[r]}.              \tag{16}
\]

En efecto, las funciones generatrices de ambos lados son

\[
 \left({1-x\over1-Qx}\right)^r.                  \tag{17}
\]

La sumación discreta convierte (16) en \((I-\rho E_\ell)^r\), y al
mantener el polo \((1-u/(s-1))^r\) se obtiene la potencia algebraica local
\(\mathsf C_{p,\varepsilon,c}^r\). Para \(r=3\) es un cubo algebraico, no
un operador positivo. Esta identidad organiza el cociclo cúbico pero no
decide el signo global de (13).

Para \(r\notin\mathbb N\) no se usa la notación \(J_u^{*r}\) ni una
diferencia ordinaria de orden \(r\). El coeficiente local se define en ese
caso por \([x^k]((1-x)/(1-Qx))^r\), y el tratamiento correcto es la serie
binomial fraccionaria de `104_23`.

## 6. Diagnóstico y frente vivo

`tools/cubic_cocycle_probe.py` evalúa (13) por extracción de Cauchy en dos
radios. En `float64`, para \(\varepsilon=0.1\), \(c=1/2\), aparecen

\[
 h_{n-1,\varepsilon,c}^{[3]}<0\qquad(1\le n\le1201).
\]

En el rango objetivo \(150\le n\le1201\), el mayor coeficiente observado es
aproximadamente \(-390.1000885\), en \(n=150\). Es evidencia, no un
certificado: ambos radios comparten evaluación de \(\zeta\), Lanczos, FFT y
errores de coma flotante.

El frente vivo queda así:

\[
 \boxed{
 \text{probar globalmente }h_{n-1,\varepsilon,c}^{[3]}\le0
 \text{ al retirar }\varepsilon,
 \quad\text{o probar directamente }D_n^{[3]}\ge0.} \tag{18}
\]

La identidad Stein--Mecke global de `104_21` sigue disponible, ahora con
la medida de Lévy aritmética multiplicada por tres y dos copias Gamma. Una
prueba debe conservar acoplado el polo cúbico; valor absoluto o signo por
torre vuelve a los stop-gates anteriores.

## Estado

- **Probado incondicionalmente:** (3), Teorema 2.1 y las identidades
  (7)--(17).
- **Mejora real del frente:** la A1 original ya no requiere el margen
  cuadrático; basta el margen cúbico estrictamente más débil.
- **Abierto:** el signo global (18). Este documento no prueba todavía A1
  ni RH.
