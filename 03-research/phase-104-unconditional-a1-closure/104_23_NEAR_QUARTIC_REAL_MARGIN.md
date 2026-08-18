# 104_23 — Margen real casi cuártico y polo hipergeométrico

> **Corrección vinculante (`104_56A`).** Las identidades y el Teorema 1.1
> de este documento siguen siendo correctos para la transferencia uniforme
> obtenida del único dato bruto \(T_n\ge1000\). Lo que se retira es su
> interpretación como frente intrínseco. A0 es válido para todo cutoff mayor:
> si \(4\lambda_n>A_n\), un cutoff adaptado suficientemente grande cierra A1.
> Además \(4\lambda_n-A_n\ge0\) para todos los índices prueba RH directamente,
> aunque no fuerce A1 en un cutoff finito prefijado mediante la sola cota
> bilateral de A0.

**Rol.** Extraer una elección uniforme más débil a partir de la mejora de
`104_22` y del piso declarado \(T_n\ge1000\). Con el cutoff efectivo
prefijado por ese único piso, la A1 original no requiere siquiera
\(3\lambda_n-A_n\ge0\): basta un margen real con exponente

\[
 r_*={2002\over501}=3.996007984\ldots<4.          \tag{1}
\]

Los canales Euler y Gamma conservan positividad para exponentes reales por
divisibilidad infinita. El precio es que el polo deja de tener cuatro
canales y pasa a una densidad hipergeométrica firmada. Este documento prueba
la reducción y la positividad de los dos canales aritmético--Gamma; no prueba
el signo final del polo acoplado, A1 ni RH.

## 1. Familia deducida de A0 y del piso del cutoff

Por `104_22`, para todo cutoff de Phase 104,

\[
 |R_n(T_n)|\le {A_n\over4(1+T_n)}.                \tag{2}
\]

Sea \(r>1\) y supóngase

\[
 D_n^{[r]}:=r\lambda_n-A_n\ge0.                  \tag{3}
\]

Entonces

\[
 \begin{aligned}
 C_n(T_n)
 &=\lambda_n-{A_n\over4}-R_n(T_n)\\
 &\ge A_n\left({1\over r}-{1\over4}
                  -{1\over4(1+T_n)}\right).       \tag{4}
 \end{aligned}
\]

El lado derecho es no negativo exactamente cuando

\[
 \boxed{r\le r_{\max}(T_n):={4(1+T_n)\over T_n+2}.} \tag{5}
\]

La función \(r_{\max}(T)\) es creciente. La tripla efectiva vinculante de
`104_01` impone \(T_n\ge U_0=1000\), de modo que el valor fijo

\[
 \boxed{r_*:=r_{\max}(1000)={4\cdot1001\over1002}
 ={2002\over501}}                                  \tag{6}
\]

sirve simultáneamente para todo \(n\). Así:

**Teorema 1.1.** Para cada \(n\ge150\),

\[
 D_n^{[r_*]}\ge0\quad\Longrightarrow\quad C_n(T_n)\ge0. \tag{7}
\]

Independientemente, por la identidad compacta ya probada,
\(C_n(T_n)\ge0\Longleftrightarrow\mathrm{A1}_n\). Por tanto (7) implica
la A1 original.

El target (7) es estrictamente más débil que el cúbico: de
\(3\lambda_n-A_n\ge0\) se sigue
\(r_*\lambda_n-A_n\ge(r_*/3-1)A_n>0\), pero no recíprocamente.

## 2. Germen completado para exponente real

Con

\[
 G(s)=s\pi^{-s/2}\Gamma(s/2),\qquad
 Y_r(s)={\xi(s)^r\over G(s)},                     \tag{8}
\]

la potencia se entiende como el germen analítico determinado por
\(r\log\xi(s)-\log G(s)\) alrededor de \(s=1\). No se afirma que
\(Y_r\) sea una función entera cuando \(r\notin\mathbb Z\); solo se usa su logaritmo
local, que es monovaluado porque \(\xi(1)\ne0\). Se tiene exactamente

\[
 \log{Y_r((1-z)^{-1})\over Y_r(1)}
 =\sum_{n\ge1}{r\lambda_n-A_n\over n}z^n.         \tag{9}
\]

En el semiplano real \(s>1+u\), donde todos los factores son positivos, el
cociclo es inequívoco y

\[
 \boxed{
 {Y_r(s-u)\over Y_r(s)}=H_u(s)^rK_u(s)^{r-1}.}    \tag{10}
\]

La normalización directa

\[
 {Y_r(s_\varepsilon(z)-u)/Y_r(s_\varepsilon(z))-1
  \over u(1-z)^2}
 =\sum_{m\ge0}h_{m,\varepsilon,c}^{[r]}z^m,
 \quad u=c\varepsilon,                            \tag{11}
\]

satisface

\[
 \boxed{
 h_{n-1,\varepsilon,c}^{[r]}
 \longrightarrow-(r\lambda_n-A_n).}              \tag{12}
\]

Por (7), probar que el límite de (11) es no positivo para \(r=r_*\) y
\(n\ge150\) prueba la A1 original.

## 3. Positividad Euler para toda potencia real

Póngase \(A_u(s)=\zeta(s-u)/\zeta(s)\). En \(\Re s>1+u\),

\[
 \log A_u(s)
 =\sum_p\sum_{k\ge1}{p^{ku}-1\over k p^{ks}},     \tag{13}
\]

y cada coeficiente es no negativo. Para todo \(r>0\),

\[
 A_u(s)^r
 =\exp\left(
 r\sum_p\sum_{k\ge1}{p^{ku}-1\over k p^{ks}}
 \right)                                          \tag{14}
\]

tiene una serie de Dirichlet con coeficientes no negativos: se obtiene
exponenciando, primo por primo, series con coeficientes no negativos y
término constante uno. En lenguaje probabilístico, la ley de \(\log N\)
es compound-Poisson con medida de Lévy

\[
 \boxed{
 \nu_A^{[r]}
 =r\sum_p\sum_{k\ge1}
 {p^{-k(1+\varepsilon-u)}-p^{-k(1+\varepsilon)}\over k}
 \delta_{k\log p}.}                               \tag{15}
\]

No se necesita que \(r\) sea entero.

## 4. Positividad Gamma para toda potencia real

La razón Gamma normalizada de `104_21` es infinitamente divisible. Su
medida de Lévy es

\[
 \nu_K(x)\,dx
 ={e^{-(3+\varepsilon-u)x}-e^{-(3+\varepsilon)x}
   \over x(1-e^{-2x})}\,dx\ge0.                  \tag{16}
\]

Por tanto \(K_u^{r-1}\), normalizada en \(s=1+\varepsilon\), es una
transformada de Laplace de medida positiva para todo \(r>1\), con medida de
Lévy \((r-1)\nu_K\). En particular esto vale para \(r_*\).

Las secciones 3--4 prueban que pasar de \(r=3\) a \(r_*\) no pierde la
positividad de Euler ni de Gamma. El único canal firmado sigue siendo el
polo.

## 5. Densidad exacta del polo real

Para \(s-1=\varepsilon+t\),

\[
 \left(1-{u\over s-1}\right)^r
 =\sum_{j\ge0}(-1)^j{r\choose j}{u^j\over(\varepsilon+t)^j}. \tag{17}
\]

Su transformada inversa de Laplace es

\[
 \delta_0(dy)+e^{-\varepsilon y}
 \sum_{j\ge1}(-1)^j{r\choose j}
 {u^jy^{j-1}\over(j-1)!}\,dy.                    \tag{18}
\]

Tras \(u=c\varepsilon\) y \(q=\varepsilon y\), la densidad continua se
suma exactamente como

\[
 \boxed{
 -rc\,e^{-q}\,{}_1F_1(1-r;2;cq)\,dq.}            \tag{19}
\]

Para \(3<r<4\), los canales \(j=1,3\) de (18) son negativos y los canales
\(j=2\) y \(j\ge4\) son positivos. En particular (19) es negativa en
\(q=0\); no es una medida positiva y no permite una prueba canal a canal.
La serie converge para todo \(q\), así que (19) es una identidad, no una
expansión asintótica.

## 6. Stop-gate uniforme de medida positiva

El defecto no desaparece al multiplicar por los canales aritmético y Gamma.
Normalicemos en \(s_0=1+\varepsilon\) el producto polo--Gamma

\[
 B_{r,u}(t)=\left({P_u(s_0+t)\over P_u(s_0)}\right)^r
             \left({K_u(s_0+t)\over K_u(s_0)}\right)^{r-1},
 \qquad P_u(s)=1-{u\over s-1}.                    \tag{20}
\]

En \(u=0\), la parte continua de la transformada inversa de Laplace de
\(\partial_uB_{r,u}|_{u=0}\) es

\[
 \boxed{
 f_{r,\varepsilon}(x)
 =-r e^{-\varepsilon x}
 +(r-1){e^{-(3+\varepsilon)x}\over1-e^{-2x}}.}    \tag{21}
\]

En \(x_0=\frac12\log2\), antes del primer átomo primo,

\[
 f_{r,\varepsilon}(x_0)
 =e^{-\varepsilon x_0}\left(-r+{r-1\over\sqrt2}\right)<0
 \qquad(r>1).                                     \tag{22}
\]

El factor aritmético normalizado \(A_u^r\) tiene masa positiva en cero y
todo su soporte restante en \([\log2,\infty)\). Por ello no puede alterar
la densidad en un entorno de \(x_0\). Tomando un test no negativo soportado
en ese entorno, (22) prueba que, para cada \(r>1\) y \(\varepsilon>0\)
fijos, existe \(u_0(r,\varepsilon)>0\) tal que para
\(0<u<u_0(r,\varepsilon)\) el cociclo completado normalizado no es la
transformada de Laplace de una medida positiva.

Los cuantificadores también cubren el camino correlacionado, pero esto no se
deduce de un Taylor uniforme en \(u\): la normalización polar contiene
\((1-c)^{-r}\). Se verifica directamente. Sea \(\varphi\ge0\) suave, no nula,
con soporte en un intervalo compacto alrededor de \(x_0\) contenido en
\((0,\log2)\), y sea \(\mu_{r,c\varepsilon,\varepsilon}\) la inversa de
Laplace del cociclo completo normalizado. Como no hay átomos aritméticos en
ese soporte, y la masa en cero del canal Euler tiende a \((1-c)^r\) y cancela
el factor polar \((1-c)^{-r}\), la expansión diagonal da

\[
 \langle\varphi,\mu_{r,c\varepsilon,\varepsilon}\rangle
 =c\varepsilon\!\int_0^\infty\!\varphi(x)
 \left[-r+(r-1){e^{-3x}\over1-e^{-2x}}\right]dx+o(\varepsilon). \tag{22a}
\]

El corchete de (22a) vale \(-r+(r-1)/\sqrt2<0\) en \(x_0\), y sigue siendo
negativo en un soporte suficientemente pequeño. Por ello el lado izquierdo
es negativo para todo \(\varepsilon>0\) suficientemente pequeño sobre
\(u=c\varepsilon\). Aquí el \(o(\varepsilon)\) se entiende para
\(c,r\) y el test compacto \(\varphi\) fijos.

Así quedan descartadas uniformemente las rutas Bernstein, medida positiva
y orden estocástico, incluso en el régimen \(u\downarrow0\) que extrae
(12). Esto no decide los coeficientes Cayley individuales.

## 7. Diagnóstico y frente exacto

Para exponente real, una extracción de Cauchy requiere continuar de forma
coherente la rama de \(r\log\xi\) a lo largo de todo el contorno. La versión
actual de `tools/cubic_cocycle_probe.py` usa logaritmos principales punto a
punto; sus filas no enteras se consideran exploratorias y **no se usan como
evidencia** en este documento.

La elección uniforme obtenida usando únicamente el piso declarado
\(T_n\ge1000\) es

\[
 \boxed{
 r_*\lambda_n-A_n\ge0\qquad(n\ge150),
 \quad r_*={2002\over501}.}                       \tag{23}
\]

Equivalentemente, hay que controlar globalmente (11) después de combinar
la ley compound-Poisson (15), la ley Gamma (16) y la densidad polar (19).
El gate es RH-strength, pero es cuantitativamente más débil que todos los
márgenes usados antes en la fase.

## Estado

- **Probado:** Teorema 1.1, el cociclo real local, la positividad
  infinitamente divisible de Euler--Gamma y la fórmula polar (19).
- **Avance:** usando solo \(T_n\ge1000\), el coeficiente exigido baja de \(1/3\) a
  \(1/r_*=501/2002\approx0.25024975\), muy cerca del mínimo \(1/4\).
- **Abierto:** el signo global de (11); no se reclama A1 ni RH.
