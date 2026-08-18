# 104_32 — Presupuesto explícito de potencias primas superiores

**Rol.** Separar rigurosamente las potencias \(p^k, k\ge2\), del canal
primo singular en el punto de Li.  El resultado es incondicional: la parte
de potencias superiores es una corrección ordinariamente convergente de
tamaño \(O(n)\), con constante explícita.  El único canal que necesita
regularización conjunta queda formado por los primos \(p\) y el polo en
\(s=1\).

El documento no prueba la cota coerciva de `104_26`, A1 ni RH.  En
particular, el umbral obtenido al absorber la corrección por valor absoluto
en \(A_n/1001\) es deliberadamente enorme.

## 1. Generador exacto y separación de Möbius

Sea \(N=n-1\ge0\) y defínase

\[
 R_N:=P_N^{(\ge2)}(1)
 :=\sum_p\sum_{k\ge2}{\log p\over p^k}
       L_N^{(1)}(k\log p).                              \tag{1}
\]

Para cada \(N\) la serie converge absolutamente. En efecto,
\(L_N^{(1)}\) es un polinomio fijo y
\(\sum_p\sum_{k\ge2}(\log p)^{N+1}k^Np^{-k}<\infty\).

Póngase

\[
 \mathcal L(s):=-{\zeta'\over\zeta}(s),\qquad
 H_{\ge2}(s):=\sum_p\sum_{k\ge2}\log p\,p^{-ks}.
\]

La inversión de Möbius de
\(\mathcal L(s)=\sum_{k\ge1}Q(ks)\),
\(Q(s)=\sum_p\log p\,p^{-s}\), da, para \(\Re s>1/2\),

\[
 \boxed{H_{\ge2}(s)
 =-\sum_{j\ge2}\mu(j)\mathcal L(js).}               \tag{2}
\]

La serie del lado derecho converge localmente de manera normal en ese
semiplano. La función generatriz de Laguerre da entonces, para \(|z|<1\),

\[
 \boxed{
 \sum_{N\ge0}R_Nz^N
 ={1\over(1-z)^2}
 H_{\ge2}\!\left({1\over1-z}\right).}              \tag{3}
\]

No hay suma de ceros ni hipótesis sobre su localización en (1)--(3).

## 2. El polo \(j=2\) y su signo

Como \(\mu(2)=-1\), el primer término de (2) es
\(+\mathcal L(2s)\). Cerca de \(s=1/2\),

\[
 \mathcal L(2s)={1\over2s-1}+O(1).                \tag{4}
\]

Bajo \(s=(1-z)^{-1}\), la contribución exacta del término polar de (4) a
(3) es

\[
 {1\over(1-z)^2}{1\over2/(1-z)-1}
 ={1\over1-z^2}
 ={1\over2}\left({1\over1-z}+{1\over1+z}\right). \tag{5}
\]

Por tanto:

* el singular principal localizado en \(z=-1\) aporta
  \(\frac12(-1)^N\), positivo para \(N\) par y negativo para \(N\) impar;
* el coeficiente del modelo polar completo (5) es exactamente
  \[
    [z^N](1-z^2)^{-1}={\bf1}_{2\mid N}.             \tag{6}
  \]

El término \(1/[2(1-z)]\) de (5) no es una singularidad real del generador
completo en \(z=1\): allí \(s\to\infty\) y \(H_{\ge2}(s)\) es plano. Se
cancela con la parte regular al recomponer (3). En consecuencia, (5)--(6)
determinan el término principal **del polo \(j=2\)**, no una asintótica
dominante del coeficiente completo \(R_N\).

En la convención prima--Laguerre de `103_14`, ecuación (4), la contribución
a \(\lambda_n^{\rm prime}\) lleva el signo opuesto. Así, el singular local
de cuadrados aporta \(-\frac12(-1)^N\) a ese canal.

## 3. Cota uniforme del bloque de cuadrados

Escribamos

\[
 S_{2,N}:=\sum_p{\log p\over p^2}L_N^{(1)}(2\log p),
 \qquad
 M_{2,N}:=\int_1^\infty x^{-2}L_N^{(1)}(2\log x)\,dx. \tag{7}
\]

La misma generatriz usada en (5) prueba exactamente

\[
 M_{2,N}={\bf1}_{2\mid N}.                         \tag{8}
\]

Usaremos dos desigualdades clásicas y elementales:

\[
 \theta(x):=\sum_{p\le x}\log p\le2(\log2)x\quad(x\ge1),       \tag{9}
\]
\[
 |L_N^{(1)}(u)|\le(N+1)e^{u/2}\quad(u\ge0).                    \tag{10}
\]

Para (10), basta combinar la desigualdad de Fejér
\(|L_j(u)|\le e^{u/2}\) con
\(L_N^{(1)}=\sum_{j=0}^NL_j\).

Póngase \(f_N(x)=x^{-2}L_N^{(1)}(2\log x)\) y
\(E_2(x)=\theta(x)-x+2\). Como \(E_2(2^-)=0\), la integración de
Stieltjes en \([2^-,\infty)\) da

\[
 S_{2,N}-M_{2,N}
 =-\int_1^2f_N(x)\,dx-\int_{2^-}^\infty E_2(x)\,df_N(x).        \tag{11}
\]

De (9), para \(x\ge2\),

\[
 |E_2(x)|\le2(\log2)x.                            \tag{12}
\]

Con \(u=2\log x\), la identidad

\[
 {d\over du}\bigl(e^{-u}L_N^{(1)}(u)\bigr)
 =-e^{-u}L_N^{(2)}(u)                              \tag{13}
\]

y (10) producen

\[
 \left|\int_1^2f_N(x)\,dx\right|\le(\log2)(N+1). \tag{14}
\]

Por ortogonalidad de Laguerre,

\[
 \int_0^\infty e^{-u}u^2[L_N^{(2)}(u)]^2\,du
 =(N+1)(N+2).                                      \tag{15}
\]

Aplicando Cauchy--Schwarz a (11)--(13), con \(u_0=2\log2\), se obtiene

\[
\begin{aligned}
 \left|\int_{2^-}^\infty E_2\,df_N\right|
 &\le2\log2\int_{u_0}^\infty
       e^{-u/2}|L_N^{(2)}(u)|\,du\\
 &\le \sqrt{2\log2\,(N+1)(N+2)}.                \tag{16}
\end{aligned}
\]

Así,

\[
 \boxed{
 |S_{2,N}-{\bf1}_{2\mid N}|
 \le(\log2)(N+1)
 +\sqrt{2\log2\,(N+1)(N+2)}.}                   \tag{17}
\]

## 4. Cota del bloque \(k\ge3\)

Por (10),

\[
 \left|\sum_p\sum_{k\ge3}{\log p\over p^k}
 L_N^{(1)}(k\log p)\right|
 \le(N+1)C_{\ge3},                                \tag{18}
\]

donde

\[
 C_{\ge3}:=\sum_p{\log p\over p^{3/2}(1-p^{-1/2})}
 \le\sum_{m\ge2}{\log m\over m^{3/2}(1-m^{-1/2})}<11.        \tag{19}
\]

La última constante no usa cálculo numérico: los términos \(m=2,3\) son
menores que \(3/2\) y \(1\), respectivamente; para \(m\ge4\),
\((1-m^{-1/2})^{-1}\le2\), y la monotonía de
\(g(x)=\log x\,x^{-3/2}\) da

\[
 2\sum_{m\ge4}g(m)
 \le2\left(g(4)+\int_4^\infty g(x)\,dx\right)
 <2\left({1\over4}+4\right)={17\over2}.           \tag{20}
\]

## 5. Teorema explícito y presupuesto cuártico

De (17)--(20), con \(n=N+1\), resulta:

**Teorema 5.1 (potencias superiores).** Para todo \(n\ge1\),

\[
 \boxed{
 |P_{n-1}^{(\ge2)}(1)|
 \le1+(11+\log2)n+\sqrt{2\log2\,n(n+1)}
 <14n+1.}                                           \tag{21}
\]

La regularización de `103_14` puede ahora separarse sin ambigüedad. Si
\(B_n^{(p+\mathrm{pole})}\) denota el límite conjunto del canal \(k=1\)
y del polo,

\[
 B_n^{(p+\mathrm{pole})}
 :=\lim_{a\downarrow1}\left\{
 n[z^n]\log(s_a(z)-1)
 -a\sum_p{\log p\over p^a}L_{n-1}^{(1)}(a\log p)
 \right\},
 \quad s_a(z)={a\over1-z}.                         \tag{22}
\]

En efecto, para \(a>1\), la identidad de Euler regularizada es

\[
\begin{aligned}
n[z^n]\log\!\bigl((s_a(z)-1)\zeta(s_a(z))\bigr)
={}&n[z^n]\log(s_a(z)-1)\\
&-a\sum_p\sum_{k\ge1}{\log p\over p^{ka}}
 L_{n-1}^{(1)}(ka\log p).                         \tag{23}
\end{aligned}
\]

El lado izquierdo converge a \(\lambda_n^{\rm prime}\), pues
\((s-1)\zeta(s)\) es analítica y no nula en \(s=1\). En el bloque
\(k\ge2\), la convergencia dominada permite tomar \(a\downarrow1\) término
a término y produce \(-P_{n-1}^{(\ge2)}(1)\). Por consiguiente, la
identidad exacta es

\[
 \boxed{\lambda_n^{\rm prime}
 =B_n^{(p+\mathrm{pole})}-P_{n-1}^{(\ge2)}(1).}    \tag{24}
\]

Por tanto el frente cuártico de `104_26` queda, exactamente,

\[
 \boxed{
 D_n^{[4]}=3A_n+4B_n^{(p+\mathrm{pole})}
             -4P_{n-1}^{(\ge2)}(1),}               \tag{25}
\]

y su obligación coerciva es equivalente a la desigualdad **solo
primos--polo**

\[
 \boxed{
 3A_n+4B_n^{(p+\mathrm{pole})}
 \ge {A_n\over1001}+4P_{n-1}^{(\ge2)}(1).}         \tag{26}
\]

El lado derecho de (26) es un presupuesto exacto y absolutamente
convergente; no es una nueva incógnita regularizada.

Para cuantificar cuándo puede descartarse incluso por valor absoluto,
usamos el piso probado en `103_02`,

\[
 A_n\ge {n\over2}(\log n-2.899)\qquad(n\ge19).     \tag{27}
\]

Las cuentas racionales dan:

\[
 |P_{n-1}^{(\ge2)}(1)|\le {A_n\over1001}
 \quad\text{si}\quad n\ge\lceil e^{28032}\rceil, \tag{28}
\]

\[
 4|P_{n-1}^{(\ge2)}(1)|\le {A_n\over1001}
 \quad\text{si}\quad n\ge\lceil e^{112116}\rceil.            \tag{29}
\]

El factor cuatro de (29), y no (28), es el relevante para `104_26`.
Estos umbrales no cubren el frente \(n\ge150\); su función es demostrar
sin una hipótesis asintótica que las potencias superiores son
\(o(A_n)\), retirar de manera exacta toda su regularización y localizar el
único canal proporcional todavía abierto en primos--polo.

## Estado

- **Probado incondicionalmente:** (2), (3), el término polar (5)--(6), la
  cota uniforme (21), la separación exacta (24)--(26) y los umbrales
  (28)--(29).
- **No probado:** el signo del coeficiente completo \(R_N\), una cota que
  absorba (21) en \(A_n/1001\) desde \(n=150\), o la desigualdad
  primos--polo (26).
- **Frente resultante:** coercividad no local del canal conjunto
  primos--polo, con la corrección de potencias superiores ya explícita y
  sin regularización.
