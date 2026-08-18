# 104_97 — Gate adversarial crítico para la constante diádica $1/8$

## Resultado

La cota candidata de `104_96`,

\[
 \Delta_j\le {1\over8j^2},
 \tag{C}
\]

es un blanco suficiente para RH, pero **no es una consecuencia de la
escala crítica** \(\Re\rho=1/2\). Más precisamente, dados
\(c>0\), \(\gamma>0\) y \(\phi\in\mathbb R\), defina

\[
 B_m^{c,\gamma,\phi}
 ={c\sqrt m\over\log m}\cos(\gamma\log m+\phi),
 \qquad
 \Delta_j^{c,\gamma,\phi}
 =\sum_{2^{j-1}<m\le2^j}
 {\{B_m^{c,\gamma,\phi}\}^2\over m(m+1)}.
 \tag{1}
\]

Si \(L=\log2\), entonces

\[
 \boxed{
 j^2\Delta_j^{c,\gamma,\phi}
 ={c^2\over L^2}
 \int_{(j-1)L}^{jL}\cos^2(\gamma t+\phi)\,dt+o(1).}
 \tag{2}
\]

En particular,

\[
 \liminf_{j\to\infty}j^2\Delta_j^{c,\gamma,\phi}
 \ge c^2\left{
 {1\over2L}-{ |\sin(\gamma L)|\over2\gamma L^2}
 \right}.
 \tag{3}
\]

Para \(c=1\), \(\gamma=7\), el lado derecho de (3) es

\[
 0.5741254552\ldots>{1\over8}.
 \tag{4}
\]

Así, este control puramente crítico viola (C) para todo \(j\)
suficientemente grande, aunque su energía total converge. La potencia
\(j^{-2}\) es la escala correcta; la constante universal \(1/8\) no lo
es.

Hay también una normalización que reproduce exactamente el residuo de un
cero crítico. Un par de multiplicidad \(M\) en
\(\rho=1/2\pm i\gamma\) aporta, en el primer término asintótico de la
fórmula explícita de \(J(x)\),

\[
 B_m^{[M,\gamma]}
 =-2M\Re {m^{1/2+i\gamma}\over
                   (1/2+i\gamma)\log m}.
 \tag{5}
\]

Esto es (1) con

\[
 c={2M\over\sqrt{1/4+\gamma^2}}
 \tag{6}
\]

y una fase fija. Tomando la primera ordenada de Riemann
\(\gamma_1=14.13472514173469\ldots\) y \(M=4\), (3) da

\[
 \liminf j^2\Delta_j^{[4,\gamma_1]}
 \ge0.2222079232\ldots>{1\over8}.
 \tag{7}
\]

El ejemplo (5)--(7) es un **testigo espectral sobre la línea**, no la
zeta de Riemann: el primer cero de \(\zeta\) es simple en el rango
verificado, y modificar su multiplicidad modifica la función y sus pesos
Euler. Por tanto (7) no refuta (C) para los pesos ordinarios. Sí refuta
rigurosamente cualquier prueba que pretenda obtener la constante
\(1/8\) usando solamente que todos los exponentes espectrales tienen
parte real \(1/2\).

Si se desea realizar literalmente ese espectro como un completamiento,

\[
 \Xi_{M,\gamma}(s)
 =\{(s-1/2)^2+\gamma^2\}^{M}
 \tag{7a}
\]

es entero, real-simétrico, satisface
\(\Xi_{M,\gamma}(1-s)=\Xi_{M,\gamma}(s)\), y todos sus ceros son
\(1/2\pm i\gamma\). Su derivada logarítmica tiene exactamente esos dos
residuos de multiplicidad \(M\), que producen (5) en el lado espectral
formal de una fórmula explícita. El modelo (7a) no tiene una aritmética
prima asociada ni el producto de Euler ordinario; su única función es probar que
«ecuación funcional + todos los ceros en la línea» tampoco determina la
constante \(1/8\).

El estado correcto de (C) para \(\zeta\) queda entonces así:

* (C) para los pesos ordinarios implicaría RH por `104_93`;
* RH implica \(\sum_j\Delta_j<\infty\), pero esa sumabilidad no implica
  ninguna envolvente prefijada \(Cj^{-2}\);
* ni `104_93`, ni la localización de los ceros en la línea, prueban (C);
* (7) no es un contraejemplo a (C) para \(\zeta\).

En consecuencia, (C) debe retirarse como supuesto «control crítico» y
conservarse solamente como conjetura aritmética adicional, falsable y de
fuerza al menos RH. Este documento no prueba ni refuta (C) para los pesos
ordinarios, y no prueba RH.

---

## 1. Prueba de la fórmula asintótica

Ponga \(X=2^{j-1}\). El sumando de (1) es

\[
 {c^2\cos^2(\gamma\log m+\phi)
  \over (m+1)\log^2m}.
 \tag{8}
\]

Reemplazar \((m+1)^{-1}\) por \(m^{-1}\) cuesta

\[
 O_{c}\!\left(\sum_{X<m\le2X}{1\over m^2\log^2m}\right)
 =O_c\!\left({1\over X\log^2X}\right).
 \tag{9}
\]

Para

\[
 f(x)={\cos^2(\gamma\log x+\phi)\over x\log^2x},
\]

se tiene, uniformemente en el bloque,

\[
 |f'(x)|\ll_\gamma {1\over x^2\log^2x}.
 \tag{10}
\]

Comparar cada \(f(m)\) con su integral en \([m-1,m]\), y sumar (10),
da

\[
 \sum_{X<m\le2X}f(m)
 =\int_X^{2X}f(x)\,dx
 +O_\gamma\!\left({1\over X\log^2X}\right).
 \tag{11}
\]

Tras \(x=e^t\),

\[
 \int_X^{2X}f(x)\,dx
 =\int_{(j-1)L}^{jL}{\cos^2(\gamma t+\phi)\over t^2}\,dt.
 \tag{12}
\]

En ese intervalo,

\[
 {j^2\over t^2}={1\over L^2}+O(1/j)
 \tag{13}
\]

uniformemente. Multiplicar (9)--(12) por \(j^2\) prueba (2).

Finalmente,

\[
 \begin{aligned}
 \int_{(j-1)L}^{jL}\cos^2(\gamma t+\phi)\,dt
  ={L\over2}
  +{\sin(\gamma L)\over2\gamma}
    \cos\{\gamma(2j-1)L+2\phi\}.
 \end{aligned}
 \tag{14}
\]

La cota inferior de (14) prueba (3). Las evaluaciones (4) y (7) son
mera sustitución en una expresión cerrada.

## 2. Relación exacta con la fórmula explícita

La fórmula explícita para la función de Riemann \(J\) contiene
\(-\operatorname {Li}(x^\rho)\) por cada cero, con emparejamiento
simétrico. Para cualquier conjunto **finito** de ceros críticos,

\[
 \operatorname {Li}(x^\rho)
 ={x^\rho\over\rho\log x}
 +O_\rho\!\left({x^{1/2}\over\log^2x}\right),
 \qquad x\to\infty.
 \tag{15}
\]

El par \(1/2\pm i\gamma\), repetido \(M\) veces, produce (5) más un
error de orden inferior. Esto justifica que (5) sea el control crítico
con la normalización correcta de residuo, en vez de un simple perfil de
potencia inventado.

Para la zeta ordinaria hay que sumar todos sus ceros y conservar los
términos cruzados. Si, bajo RH, se trunca a \(0<\gamma\le T\), el
polinomio principal es

\[
 F_T(t)=-2\Re\sum_{0<\gamma\le T}
 {e^{i\gamma t}\over1/2+i\gamma}.
 \tag{16}
\]

Su energía local es

\[
 {1\over L^2}\int_{(j-1)L}^{jL}F_T(t)^2\,dt.
 \tag{17}
\]

Los términos cruzados de (17) no tienen signo. Por ello no es lícito
sumar cotas individuales como (3), ni tampoco descartar un bloque finito
para obtener una cota inferior del cuadrado completo. Pasar
uniformemente de (17) a todos los ceros con una constante \(1/8\) es una
desigualdad local de marco adicional; no es el contenido del enunciado
RH.

## 3. Sustituto crítico válido

El único control general que sí se deduce de `104_93` bajo RH es

\[
 \boxed{
 \sum_{j\ge1}\Delta_j<\infty,
 \qquad
 \Delta_j=o(1).}
 \tag{18}
\]

No se puede promover (18), por pura teoría de series positivas, a
\(O(j^{-2})\): una sucesión sumable puede tener picos arbitrariamente
mayores que \(j^{-2}\) sobre una subsucesión dispersa. Para cerrar RH
incondicionalmente sigue bastando cualquier mayorante sumable probado
directamente para los pesos ordinarios, o la condición equivalente
\(\sum_j\Delta_j<\infty\); el número \(1/8\) no debe tratarse como una
constante impuesta por la línea crítica.

## 4. Reproducción

Desde `tools/`:

```bash
python3 dyadic_one_eighth_critical_gate_check.py
```

El checker evalúa las constantes cerradas de (3), verifica el testigo
normalizado (7), y compara (2) con las sumas discretas de (1). Sus
cálculos son diagnósticos de la fórmula; la prueba es (8)--(14).
