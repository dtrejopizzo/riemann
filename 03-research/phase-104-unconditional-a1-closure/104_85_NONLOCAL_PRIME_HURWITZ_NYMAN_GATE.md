# 104_85 — Renormalización global de primos, Hurwitz y forma no local de Nyman

**Resultado.** Después del gate local de `104_84`, hay dos construcciones
que conservan genuinamente la interacción global de los primos.

1. Existe una sucesión explícita de funciones enteras y cero-libres,
   construida con todos los pesos \(\Lambda(m)\le X\) y el comparador
   continuo, que converge a \((s-1)\zeta(s)\) hasta \(\Re s=1\).
   Su convergencia local uniforme en \(\Re s>1/2\) es **equivalente a RH**.
2. La aproximación Möbius de Nyman--Báez-Duarte produce una forma Gram no
   local y positiva con kernel \(1/\max(m,n)\). Un solo cero
   \(\rho=\beta+i\gamma\), \(\beta>1/2\), impone a todo residual una norma
   al menos \((2\beta-1)/|\rho|^2\). Probar que esa norma tiende a cero es
   exactamente eliminar el factor de Blaschke de `104_84`.

Por tanto ni la renormalización global ni la energía cuadrática pierden la
obstrucción: la localizan de forma exacta. Este documento no prueba
Deep-\(\Lambda\), A1 ni RH.

---

## 1. Producto global renormalizado

Ponga

\[
 E(x)=\psi(x)-x,
 \qquad
 G_X(s)=\sum_{m\le X}{\Lambda(m)\over m^s}
         -\int_1^Xx^{-s}\,dx.                            \tag{1}
\]

La segunda función es entera: la aparente singularidad de la integral en
\(s=1\) es removible. Defina

\[
 F_X(s)=\zeta(2)\exp\left\{-\int_2^sG_X(w)\,dw\right\}. \tag{2}
\]

La integral no depende del camino porque \(G_X\) es entera. Cada \(F_X\)
es entera y nunca se anula. Integrando los dos términos de (1),

\[
\begin{aligned}
 F_X(s)=\zeta(2)\exp\Bigg\{&
 \sum_{m\le X}{\Lambda(m)\over\log m}
       (m^{-s}-m^{-2})\\
 &+\int_1^X{x^{-2}-x^{-s}\over\log x}\,dx\Bigg\},      \tag{3}
\end{aligned}

donde el cociente en \(x=1\) se entiende por continuidad. La fórmula usa
simultáneamente todas las potencias primas hasta \(X\); no es un cambio
local fijo de factores Euler.

La integración de Stieltjes da la identidad exacta

\[
 \boxed{
 G_X(s)=1+E(X)X^{-s}
        +s\int_1^XE(x)x^{-s-1}\,dx.}                    \tag{4}
\]

En efecto,

\[
 \sum_{m\le X}\Lambda(m)m^{-s}
 =\psi(X)X^{-s}+s\int_1^X\psi(x)x^{-s-1}\,dx,          \tag{5}
\]

y la parte con \(\psi(x)=x\) menos el comparador de (1) es exactamente
uno.

## 2. Semiplano alcanzado incondicionalmente

La cota Vinogradov--Korobov efectiva tiene la forma

\[
 |E(x)|\le x\exp\{-\eta(\log x)\},
 \qquad
 \eta(u)\asymp u^{3/5}(\log u)^{-1/5}.                  \tag{6}
\]

Por (4), el borde y la cola convergen uniformemente en compactos de
\(\Re s\ge1\). Para \(\Re s>1\),

\[
 G_X(s)\longrightarrow
 -{\zeta'\over\zeta}(s)-{1\over s-1}
 =-{d\over ds}\log\{(s-1)\zeta(s)\}.                  \tag{7}
\]

La normalización \(F_X(2)=\zeta(2)=(2-1)\zeta(2)\) prueba

\[
 F_X(s)\longrightarrow (s-1)\zeta(s)                  \tag{8}
\]

localmente uniformemente en el semiplano certificado.

VK no entrega ningún \(\Re s>1-\delta\), \(\delta>0\) fijo. En efecto, la
majorante que resulta de (4) contiene

\[
 \int^\infty
 \exp\{\delta u-\eta(u)\}\,du=\infty,                 \tag{9}
\]

y el borde es
\(\exp\{\delta\log X-\eta(\log X)\}\), que tampoco tiende a cero.
Cambiar las constantes de (6) no altera esta barrera de exponentes.

## 3. Equivalencia de Hurwitz

Se tiene

\[
 \boxed{
 F_X\longrightarrow(s-1)\zeta(s)
 \text{ localmente uniformemente en }\Re s>{1\over2}
 \quad\Longleftrightarrow\quad \mathrm{RH}.}           \tag{10}
\]

Si ocurre la convergencia, el teorema de Hurwitz y el hecho de que cada
\(F_X\) es cero-libre implican que \((s-1)\zeta(s)\) es cero-libre en ese
semiplano. La simetría funcional da RH.

Recíprocamente, RH implica la cota de von Koch

\[
 E(x)=O(x^{1/2}\log^2x),                                \tag{11}
\]

y (4) converge uniformemente en cada compacto de \(\Re s>1/2\), lo que
prueba (10).

La falla es cuantitativamente visible. Si \(\rho\) es un cero derecho y
el círculo \(|s-\rho|=r\) no contiene otros ceros, entonces para todo
\(X\)

\[
 \boxed{
 \sup_{|s-\rho|=r}|F_X(s)-(s-1)\zeta(s)|
 \ge \min_{|s-\rho|=r}|(s-1)\zeta(s)|>0.}              \tag{12}
\]

De lo contrario, Rouché obligaría a la función cero-libre \(F_X\) a tener
un cero dentro del círculo. Un modo \(E_\rho(x)\asymp x^\rho\) produce la
misma obstrucción en (4) mediante un término
\(X^{\rho-s}/(s-\rho)\).

## 4. Residual no local de Nyman

Defina

\[
 g_N=\sum_{k\le N}{\mu(k)\over k},
 \qquad
 A_N(s)=\sum_{k\le N}{\mu(k)\over k^s}
          -Ng_NN^{-s}.                                  \tag{13}
\]

Entonces \(A_N(1)=0\), lo que cancela el polo de \(\zeta\), y el residual

\[
 f_N(s)={1-\zeta(s)A_N(s)\over s}                       \tag{14}
\]

tiene norma de Hardy

\[
 d_N^2={1\over2\pi}\int_{-\infty}^{\infty}
 { |1-\zeta(\tfrac12+it)A_N(\tfrac12+it)|^2
  \over t^2+1/4}\,dt.                                  \tag{15}
\]

En la coordenada de Mellin, si un residual finito se escribe
\(\sum_m r_mm^{-s}\), Plancherel da la forma exacta

\[
 \boxed{
 \left\|\sum_mr_mm^{-s}/s\right\|_2^2
 =\sum_{m,n}{r_m\overline{r_n}\over\max(m,n)}.}        \tag{16}
\]

El kernel conserva todas las interacciones y es PSD porque

\[
 {1\over\max(m,n)}
 =\int_0^1
 \mathbf1_{\{x\le1/m\}}\mathbf1_{\{x\le1/n\}}\,dx.  \tag{17}
\]

## 5. Un cero impone una distancia positiva

Si \(\rho=\beta+i\gamma\), \(\beta>1/2\), es cero de \(\zeta\), entonces
para **todo** multiplicador \(A_N\)

\[
 f_N(\rho)={1\over\rho}.                                \tag{18}
\]

La desigualdad de evaluación en
\(H^2(\Re s>1/2)\) da

\[
 |f_N(\rho)|^2\le {d_N^2\over2\beta-1}.
\]

Por tanto

\[
 \boxed{d_N^2\ge{2\beta-1\over|\rho|^2}>0}            \tag{19}
\]

para cualquier elección de pesos, no solo (13). En el disco,
\((2\beta-1)/|\rho|^2=1-|w_\rho|^2\), exactamente el defecto de un factor
de Blaschke elemental.

Ponga, en el disco,

\[
 \mathcal G(z)=z\,\zeta\!\left({1\over1-z}\right),
 \qquad \mathcal G(0)=1.                                \tag{20}
\]

Esta función pertenece a \(H^2(\mathbb D)\) y tiene el mismo factor
interior \(B\) que `104_84`; los factores que la distinguen de \(E\) son
exteriores. En la normalización Hardy canónica, el cierre de todos los
multiplicadores exteriores satisface

\[
 \inf_P\|1-\mathcal G P\|_2^2=1-|B(0)|^2.              \tag{21}
\]

donde \(B\) es el factor interior de `104_84`. Así

\[
 d_N\longrightarrow0
 \quad\Longleftrightarrow\quad B\equiv1
 \quad\Longleftrightarrow\quad\mathrm{RH}.             \tag{22}
\]

La positividad de (16) no da una cota superior tendiente a cero. Los pesos
de Möbius son el candidato aritmético canónico, pero demostrar (22) es
precisamente el criterio Nyman--Beurling/Báez-Duarte.

## 6. Decisión

```text
probado:
  renormalización cero-libre all-primes (1)--(4);
  su convergencia hasta Re s=1 por VK;
  convergencia hasta Re s>1/2 iff RH;
  residual Nyman y forma Gram no local exacta;
  todo cero derecho impone la distancia positiva (19).

descartado:
  PNT/VK + producto parcial renormalizado + Hurwitz => RH;
  positividad de la forma Gram, sin una cota superior nueva => RH.

no probado:
  la convergencia de (10), d_N->0, B(0)=1, Deep-Lambda, A1 o RH.
```
