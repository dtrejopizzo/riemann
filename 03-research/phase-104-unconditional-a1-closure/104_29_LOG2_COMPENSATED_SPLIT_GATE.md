# 104_29 — Corte compensado en \(\log2\) y gate de transporte firmado

**Rol.** Ejecutar la propuesta de separar la variable de Laplace en el primer
átomo aritmético. El corte es natural y produce una identidad exacta. Sin
embargo, una comparación de masas sin el test Laguerre es inválida e
informativamente vacía; la versión compensada que conserva el test recompone
exactamente el margen \(D_n^{[r]}=r\lambda_n-A_n\).

Este documento no prueba A1 ni RH. Localiza MW-2 en el hueco
\((0,\log2)\), cuantifica su acción sobre el vector real y muestra qué
desigualdad firmada global seguiría siendo necesaria.

## 1. Generador completado antes de retirar el regulador

Fijemos

\[
 r>1,\qquad s_0=1+\varepsilon,\qquad u=c\varepsilon,
 \qquad 0<c<1.
\]

La primera variación del cociclo real de 104_23--104_24 tiene la medida de
Lévy completada

\[
 \boxed{
 \kappa_{r,\varepsilon}(dx)
 =r e^{-(1+\varepsilon)x}\,d\psi(e^x)
  -r e^{-\varepsilon x}\,dx
  +(r-1){e^{-(3+\varepsilon)x}\over1-e^{-2x}}\,dx.}             \tag{1}
\]

La parte Gamma de (1) es \((r-1)/(2x)+O_r(1)\) cuando \(x\downarrow0\).
Por ello (1) no tiene masa total finita cerca de cero. La acción correcta
sobre un test \(\varphi\) es compensada:

\[
 \mathcal G_{r,\varepsilon}\varphi
 :=\int_0^\infty\bigl(\varphi(x)-\varphi(0)\bigr)
       \kappa_{r,\varepsilon}(dx).                              \tag{2}
\]

Para un polinomio, la diferencia en (2) es \(O(x)\), y

\[
 \int_0^\infty x(1+x^k)|\kappa_{r,\varepsilon}|(dx)<\infty
\]

para todo \(k\) y todo \(\varepsilon>0\). Así (2), no una diferencia
informal de masas infinitas, es el objeto legítimo.

## 2. Identidad Laguerre exacta y corte en el primer primo

Pongamos

\[
 \varphi_n(x)=L_{n-1}^{(1)}(x)-n,\qquad \varphi_n(0)=0.          \tag{3}
\]

La linealización normalizada del cociclo da

\[
 \boxed{
 -D_n^{[r]}
 =-nD_1^{[r]}
  +\lim_{\varepsilon\downarrow0}
       \int_0^\infty\varphi_n(x)\kappa_{r,\varepsilon}(dx),}
 \qquad D_n^{[r]}=r\lambda_n-A_n.                              \tag{4}
\]

Sea \(a=\log2\). No hay átomos de \(d\psi(e^x)\) en \(0<x<a\), y el
átomo \(m=2\) se asigna al bloque exterior. Por tanto (4) se parte
exactamente como

\[
 -D_n^{[r]}=-nD_1^{[r]}
 +\lim_{\varepsilon\downarrow0}
 \bigl(J_n^{<}(\varepsilon)+J_n^{\ge}(\varepsilon)\bigr),       \tag{5}
\]

donde

\[
 \boxed{
 J_n^{<}(\varepsilon)
 =\int_0^a\varphi_n(x)e^{-\varepsilon x}
 \left[-r+(r-1){e^{-3x}\over1-e^{-2x}}\right]dx}                \tag{6}
\]

y

\[
 \boxed{
 \begin{aligned}
 J_n^{\ge}(\varepsilon)
 ={}&r\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       \varphi_n(\log m)\\
 &+\int_a^\infty\varphi_n(x)e^{-\varepsilon x}
 \left[-r+(r-1){e^{-3x}\over1-e^{-2x}}\right]dx .
 \end{aligned}}                                                 \tag{7}
\]

Las ecuaciones (5)--(7) conservan polo, Gamma, todos los primos y el test
Laguerre. El teorema que cerraría el margen sería

\[
 \boxed{
 \limsup_{\varepsilon\downarrow0}J_n^{\ge}(\varepsilon)
 \le nD_1^{[r]}-\lim_{\varepsilon\downarrow0}J_n^{<}(\varepsilon)
 \qquad(n\ge150).}                                              \tag{8}
\]

Pero, por (5), (8) es exactamente \(D_n^{[r]}\ge0\). El corte organiza la
cancelación; no la demuestra.

## 3. La obstrucción localizada y su escala sobre el test real

En el hueco aritmético aparece la densidad

\[
 b_r(x)=-r+(r-1){e^{-3x}\over1-e^{-2x}}.                       \tag{9}
\]

El segundo término de (9) decrece estrictamente de \(+\infty\) a cero.
Existe por tanto un único \(x_r>0\) con \(b_r(x_r)=0\). En
\(x_0=\frac12\log2\),

\[
 b_r(x_0)=-r+{r-1\over\sqrt2}<-1<0.                            \tag{10}
\]

Esto recupera el testigo de 104_23 y prueba que ningún argumento basado en
positividad de la medida completada puede funcionar.

Su acción sobre el test específico tiene una lectura distinta. En el
intervalo fijo \([x_r,a]\), la asintótica de Laguerre a argumento fijo da,
uniformemente lejos de cero,

\[
 L_{n-1}^{(1)}(x)=O_r(n^{1/4}),
 \qquad
 \varphi_n(x)=-n+O_r(n^{1/4}).                                 \tag{11}
\]

En consecuencia, para

\[
 M_r:=\int_{x_r}^{a}(-b_r(x))\,dx>0,
\]

se tiene

\[
 \int_{x_r}^{a}\varphi_n(x)b_r(x)\,dx
 =nM_r+O_r(n^{1/4}).                                           \tag{12}
\]

El testigo local de no-positividad aporta sólo escala \(O_r(n)\), frente a
\(A_n\asymp n\log n\). Es robusto como stop-gate de medidas positivas,
pero no es por sí solo la obstrucción proporcional. La dificultad queda en
el bloque exterior (7), donde polo y primos se cancelan a todos los órdenes.

## 4. Por qué el balance de masas da un falso diagnóstico

La masa prima positiva del generador para \(\varepsilon>0\) vale

\[
 r\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 =-r{\zeta'\over\zeta}(1+\varepsilon)
 \sim {r\over\varepsilon}.                                    \tag{13}
\]

La masa negativa de cualquier compacto dentro de \((0,\log2)\) es
\(O_r(1)\). Así la parte aritmética «domina en masa» de manera automática,
sin que ello implique ningún signo para (7). Sobre el camino
\(u=c\varepsilon\) ocurre la misma falsa victoria después de normalizar:
la masa aritmética de Lévy tiende a \(-r\log(1-c)>0\), mientras la masa
negativa en un compacto del hueco es \(O(\varepsilon)\).

Al reponer el test Laguerre, separar primos y polo tampoco es posible. Como
\(\varphi_n\) tiene grado \(n-1\),

\[
 \int_0^\infty x^{n-1}e^{-\varepsilon x}\,dx
 ={(n-1)!\over\varepsilon^n}.                                  \tag{14}
\]

Los momentos principales del polo y de la suma prima son, por tanto, de
orden \(\varepsilon^{-n}\) y se cancelan en la combinación completada.
Tomar valores absolutos, masas o partes positivas antes de esa cancelación
reproduce exactamente la pérdida de 103_53--103_57.

## 5. Falsificador y frontera lógica

Toda inferencia que use únicamente:

* positividad de los coeficientes Euler;
* el hueco de soporte \((0,\log2)\);
* Gamma positiva y simetría funcional;

debe someterse al cuarteto off-line

\[
 w={1\over2}e^{74\pi i/75},\qquad \rho=(1-w)^{-1}.              \tag{15}
\]

Para \(n=150\), su contribución al margen de exponente \(r\) contiene

\[
 4r\bigl(1-\cosh(150\log2)\bigr)<0,                            \tag{16}
\]

y puede amplificarse por multiplicidad. Una prueba de (8) debe usar una
propiedad cuantitativa especial de los pesos reales
\(\Lambda(p^k)=\log p\) y debe fallar para (15).

## 6. Relación con los gates anteriores

* 104_23 ya prueba el testigo local (10).
* La primera variación (1) es el kernel Stein--Mecke de 104_24.
* El bloque (7), sin separar las torres primas, es el gate multiplicativo
  global sobreviviente de 104_20.
* Separar su parte prima de la polar repite la obstrucción de endpoint de
  103_53--103_57.

Por tanto \(\log2\) es el corte geométrico correcto, pero no crea
coercividad. El sucesor vivo sigue siendo una desigualdad firmada no local
para (7), o equivalentemente una cota directa sobre el rayo hard-edge de
104_28.

## Estado

* **Probado:** generador compensado, corte exacto (5)--(7), unicidad del
  cruce (9), escala local (12) y divergencia separada (14).
* **Descartado:** comparar masas positivas y negativas sin el test Laguerre.
* **No reducido:** la desigualdad útil (8) es exactamente
  \(D_n^{[r]}\ge0\).
* **Frente vivo:** una cota firmada para la forma prima--polo renormalizada
  sobre \(g_n\), usando interacción multiplicativa real entre torres.

