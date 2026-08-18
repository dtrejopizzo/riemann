# 104_21 — Gate global compound-Poisson y total positivity

**Rol.** Someter el gate global sobreviviente de `104_20` a las
estructuras positivas naturales de la convolución multiplicativa completa:
independencia por primos, representación compound-Poisson, PF/TP,
log-concavidad, variación disminuyente y representación por una medida de
Laplace positiva.

**Veredicto.** La ley aritmética normalizada sí es compound-Poisson y admite
un acoplamiento estocástico exacto al variar \(u\). Sin embargo, su núcleo en
la retícula de exponentes falla PF2 con un menor racional de dos primos, y el
cociclo **completado real** falla monotonía completa con una densidad
inversa de Laplace explícitamente negativa antes del primer átomo aritmético.
Por tanto no puede obtenerse el signo de \(g_{n,\varepsilon,c}\) mediante una
medida positiva global, PF\(_\infty\), TP o el orden estocástico de esta ley.
Esto no refuta el signo de \(g_{n,\varepsilon,c}\) ni prueba A1 o RH.

## 1. Ley aritmética normalizada

Fijemos \(0<u<\varepsilon\), \(s_0=1+\varepsilon\), y normalicemos los
coeficientes de `104_19`:

\[
 \mathbb P(N=m)
 ={b_u(m)m^{-1-\varepsilon}\over A_u(1+\varepsilon)^2},
 \qquad
 A_u(s)={\zeta(s-u)\over\zeta(s)}.                 \tag{1}
\]

Como \(b_u\) es multiplicativa, si

\[
 N=\prod_p p^{K_p},                                \tag{2}
\]

los exponentes \(K_p\) son independientes. Para

\[
 r=p^{-1-\varepsilon},\qquad Q=p^u,\qquad
 R=Qr=p^{-1-(\varepsilon-u)},                      \tag{3}
\]

la función generatriz local normalizada es

\[
 \boxed{
 G_p(z)=\mathbb E z^{K_p}
 =\left({1-R\over1-r}\right)^2
  \left({1-rz\over1-Rz}\right)^2.}                \tag{4}
\]

Cada factor sin cuadrado es una función generatriz de probabilidad. En
efecto, \(K_p=X_{p,1}+X_{p,2}\), con copias independientes de

\[
 \boxed{
 \begin{aligned}
  \mathbb P(X_p=0)&={1-R\over1-r},\\
  \mathbb P(X_p=k)&={1-R\over1-r}(R-r)R^{k-1},
       \qquad k\ge1.
 \end{aligned}}                                    \tag{5}
\]

La masa de (5) suma uno exactamente. Esta es una geométrica inflada en
cero, no una aproximación.

## 2. Identidad compound-Poisson global

Tomando logaritmos en (4),

\[
 \log G_p(z)
 =2\sum_{j\ge1}{R^j-r^j\over j}(z^j-1).           \tag{6}
\]

Por tanto \(X=\log N\) es una variable compound-Poisson sobre el semigrupo
aditivo generado por los \(\log p\), con medida de Lévy

\[
 \boxed{
 \nu_A
 =2\sum_p\sum_{j\ge1}
 {p^{-j(1+\varepsilon-u)}-p^{-j(1+\varepsilon)}\over j}
 \delta_{j\log p}.}                                \tag{7}
\]

La serie de masas de (7) converge para \(u<\varepsilon\). La fórmula (7)
es el producto de operadores sobre **todos** los primos: las interacciones
entre primos distintos se producen al exponenciar su suma, no se descartan
torre a torre.

Además, si \(0<u_1<u_2<\varepsilon\), entonces

\[
 \nu_A(u_2)-\nu_A(u_1)\ge0.                        \tag{8}
\]

Así puede acoplarse

\[
 X(u_2)=X(u_1)+Z_{u_1,u_2},                        \tag{9}
\]

donde el incremento \(Z_{u_1,u_2}\ge0\) es compound-Poisson e independiente.
La ley aritmética crece en orden de convolución y, en particular, en orden
estocástico. Este hecho solo ordena funciones monótonas (y sus refinamientos
convexos); los Laguerres del gate cambian de signo y no pertenecen a esas
clases.

La identidad de Mecke asociada a (7), para toda función para la cual ambos
lados converjan, es

\[
 \boxed{
 \mathbb E[X\varphi(X)]
 =\int_0^\infty y\,\mathbb E[\varphi(X+y)]\,\nu_A(dy).} \tag{10}
\]

Éste es el sucesor global concreto del cuadrado local: conserva en la
esperanza de la derecha todos los demás primos. No tiene signo para una
prueba Laguerre oscilatoria.

## 3. PF2 falla ya en una coordenada prima

Sea

\[
 a_k=b_u(p^k)r^k\qquad(k\ge0).                     \tag{11}
\]

Usando la fórmula exacta de `104_19`,

\[
 \boxed{a_1^2-a_0a_2=r^2(Q-1)(Q-3).}              \tag{12}
\]

En consecuencia, para \(1<Q<3\) la sucesión no es log-cóncava ni PF2. En
particular no es PF\(_\infty\), y el producto de Euler no puede justificarse
como un operador de variación disminuyente mediante factores TP locales.

Hay un testigo enteramente racional que ya contiene dos primos. Tómese

\[
 u=1,\qquad\varepsilon=2,\qquad c={1\over2},       \tag{13}
\]

y escribamos \(w(m)=b_1(m)m^{-3}\). Entonces

\[
 w(3)={4\over27},\qquad
 w(6)={1\over27},\qquad
 w(12)={5\over432}.                                \tag{14}
\]

El menor PF2 en la fibra \(3\cdot2^k\) vale

\[
 \boxed{
 \det\begin{pmatrix}w(6)&w(12)\\w(3)&w(6)\end{pmatrix}
 =w(6)^2-w(3)w(12)=-{1\over2916}<0.}               \tag{15}
\]

La normalización de (1) multiplica (15) por una constante positiva y no
cambia su signo. El testigo no reemplaza la aritmética por un divisor
abstracto: usa los primos reales \(2\) y \(3\).

## 4. Medidas de Lévy de Gamma y del canal polar

La razón Gamma normalizada es la transformada de Laplace de

\[
 \eta=-{1\over2}\log V,
 \qquad
 V\sim {\rm Beta}\left({3+\varepsilon-u\over2},{u\over2}\right).
                                                               \tag{16}
\]

Su medida de Lévy es

\[
 \boxed{
 \nu_K(x)\,dx
 ={e^{-(3+\varepsilon-u)x}-e^{-(3+\varepsilon)x}
   \over x(1-e^{-2x})}\,dx.}                       \tag{17}
\]

En cambio, el factor polar normalizado es el inverso de la transformada de
Laplace de \(P_1+P_2\), donde los \(P_i\) son independientes y

\[
 \mathbb P(P_i=0)=1-c,\qquad
 \mathbb P(P_i\in dx)=c(\varepsilon-u)e^{-(\varepsilon-u)x}\,dx.
                                                               \tag{18}
\]

La medida de Lévy de esa suma es

\[
 \boxed{
 \nu_P(x)\,dx
 =2{e^{-(\varepsilon-u)x}-e^{-\varepsilon x}\over x}\,dx.}   \tag{19}
\]

Por tanto el logaritmo del cociclo completado normalizado tiene la medida
de Lévy **firmada**

\[
 \boxed{\nu_{\mathcal S}=\nu_A+\nu_K-\nu_P.}       \tag{20}
\]

La resta de (19) ya advierte que (9) no se transmite automáticamente al
cociclo completado. La sección siguiente prueba algo más fuerte: no existe
siquiera otra representación de su transformada por una medida positiva.

## 5. Contraejemplo global a monotonía completa

Con los parámetros racionales (13), la variable Beta de (16) tiene
\(V\sim{\rm Beta}(2,1/2)\), y la densidad normalizada de \(\eta\) es

\[
 f(x)={3\over2}{e^{-4x}\over\sqrt{1-e^{-2x}}},
 \qquad x>0.                                       \tag{21}
\]

Antes de normalizar por su valor en \(t=0\), la transformada inversa del
factor polar es

\[
 \delta_0-2e^{-2x}\,dx+xe^{-2x}\,dx.              \tag{22}
\]

La parte absolutamente continua de la convolución de (21) y (22) es

\[
 h(x)=f(x)-2\int_0^xe^{-2y}f(x-y)\,dy
          +\int_0^xye^{-2y}f(x-y)\,dy.             \tag{23}
\]

Poniendo \(Q=\sqrt{1-e^{-2x}}\), las dos integrales se calculan sin
aproximaciones:

\[
 \begin{aligned}
 \int_0^xe^{-2y}f(x-y)\,dy
   &={3\over2}e^{-2x}Q,\\
 \int_0^xye^{-2y}f(x-y)\,dy
   &={3\over2}e^{-2x}(\mathrm{artanh}\,Q-Q).
 \end{aligned}                                     \tag{24}
\]

En consecuencia,

\[
 \boxed{
 h(x)={3\over2}e^{-2x}
 \left({1\over Q}-4Q+\mathrm{artanh}\,Q\right).}          \tag{25}
\]

En el punto exacto \(x_0=\frac12\log2\), se tiene \(Q=1/\sqrt2\) y

\[
 {1\over Q}-4Q+\mathrm{artanh}\,Q
 =-\sqrt2+\mathrm{artanh}(1/\sqrt2)<0.       \tag{26}
\]

La última desigualdad es elemental y estricta:

\[
 \mathrm{artanh}\,q
 =q\int_0^1{ds\over1-q^2s^2}
 <2q=\sqrt2,
 \qquad q={1\over\sqrt2}.                         \tag{27}
\]

Ahora repóngase el factor aritmético global (1). Su ley tiene una masa
positiva en \(X=0\) y no tiene soporte en \(0<X<\log2\). Como
\(0<x_0<\log2\), la densidad inversa de Laplace del cociclo **completo** en
\(x_0\) es \(h(x_0)\) multiplicada por la masa en cero y por constantes de
normalización positivas. Es, por (26), estrictamente negativa.

La unicidad de la transformada de Laplace para medidas finitas firmadas
impide reemplazar esta inversa por otra medida positiva. Por el teorema de
Bernstein,

\[
 \boxed{
 t\longmapsto{\mathcal S_1(3+t)\over\mathcal S_1(3)}
 \quad\hbox{no es completamente monótona en }t\ge0.}          \tag{28}
\]

Este es un testigo sobre el producto Euler y los factores Gamma y polar
reales, no sobre un modelo off-line.

## 6. Alcance exacto y sucesor

Los resultados anteriores cierran las siguientes rutas:

1. PF\(_\infty\), TP y variación disminuyente obtenidas factorizando el
   producto por coordenadas primas: las mata (12)--(15).
2. Representar el cociclo completado como transformada de una probabilidad
   positiva y aplicar orden estocástico: la mata (28).
3. Transferir directamente el acoplamiento creciente (9) a los coeficientes
   Laguerre: el factor polar es una deconvolución y el test oscilatorio no
   preserva ese orden.

No se ha probado que \(g_{n,\varepsilon,c}\) tenga signo positivo, negativo
o cambiante. En particular, (28) no implica que alguno de los coeficientes
del gate tenga el signo incorrecto.

El sucesor global más concreto que queda visible es (10): una identidad de
Stein--Mecke aplicada **después** de conservar Gamma, polo y la esperanza
sobre todos los otros primos. Para aportar una cota nueva deberá probar una
desigualdad firmada especial para los tests Laguerre completados. Aplicar
valor absoluto a (10) devuelve la pérdida ya registrada, y reemplazar esos
tests por funciones monótonas vuelve a una clase que no contiene A1. No se
reclama aquí tal desigualdad.

## 7. Verificación reproducible

Ejecutar

```text
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 global_compound_poisson_tp_check.py
```

El programa usa `Fraction` para todas las decisiones de signo. Verifica
(14)--(15), la identidad local (12) en el testigo y el certificado simbólico
de (27); no usa coma flotante para certificar ninguna desigualdad.
