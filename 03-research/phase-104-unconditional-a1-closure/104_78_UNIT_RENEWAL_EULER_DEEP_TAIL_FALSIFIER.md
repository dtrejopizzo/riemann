# 104_78 — Falsificador Euler unitario para la cola profunda

**Resultado.** La renovación exacta

\[
 \sum_{D\mid N}\Lambda(D)=\log |N|,
 \tag{1}
\]

la constancia \(\Lambda(P^k)=\log |P|\) sobre cada torre, la positividad de
los pesos, un producto de Euler con multiplicidades primas enteras no
negativas, una ecuación funcional \(s\leftrightarrow1-s\) y una ley prima
**de grado** con error relativo exponencial **no bastan**, ni
conjuntamente, para demostrar el gate profundo de `104_75`.

Se construye un monoide aritmético libre y completamente explícito cuyo
zeta es

\[
 \boxed{
 Z(T)={(1-3T)(1-2T)\over(1-T)(1-6T)},\qquad T=6^{-s}.}
 \tag{2}
\]

Su producto de Euler tiene un número entero no negativo de primos en cada
grado, todas sus torres tienen multiplicidad unitaria y

\[
 Z(1/(6T))=Z(T).                                          \tag{3}
\]

Además, si \(\Psi_k\) es la masa de von Mangoldt en grado \(k\)
normalizada por \(\log6\), entonces

\[
 \boxed{\Psi_k=6^k+1-3^k-2^k,}                           \tag{4}
\]

de modo que, coeficiente a coeficiente en la variable de grado, el error
relativo es \(O(2^{-k})\). Esta es la versión reticular del PNT propia del
modelo; no es el PNT ordinario \(\psi(x)\sim x\) en una variable continua
de norma (véase la \S5).

No obstante, los ceros

\[
 \beta_+=\log_6 3>{1\over2},\qquad
 \beta_-=\log_6 2=1-\beta_+                              \tag{5}
\]

están fuera de la recta central. La forma prima--Laguerre regulada, con
polo, bloque complementario, primos y potencias primas conservados hasta
el final, satisface

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf 1_{\{Q_{n,\varepsilon_X}\ge
 A_n+P_{n,\varepsilon_X}+\log(n+1)+e^{\sqrt X}\}}
 \longrightarrow {1\over4},
 \qquad \varepsilon_X=e^{-X/100}.                        \tag{6}
\]

Así (6) es un falsificador más fuerte que el cuarteto abstracto de
`104_75`/`104_77`: posee un producto de Euler positivo, renovación exacta y
torres unitarias. No es, sin embargo, un contraejemplo para los pesos
ordinarios \(\Lambda(m)\): sus primos son primos formales graduados, con
normas \(6^d\) y multiplicidades. El veredicto preciso es que cualquier
prueba de la cola profunda para la zeta real debe usar una propiedad que
distinga la colocación de los primos ordinarios de este sistema; no puede
deducirse solo de (1), de las torres, de la ley prima de grado, de la
ecuación funcional y de positividad.

Este documento no prueba el límite de `104_75`, A1 ni RH.

---

## 1. Primos formales y multiplicidades enteras

Sea

\[
 M_d(r)={1\over d}\sum_{e\mid d}\mu(e)r^{d/e}            \tag{7}
\]

el número de collares aperiódicos de longitud \(d\) sobre un alfabeto de
\(r\) letras. Defina

\[
 \boxed{\pi_d=M_d(6)+M_d(1)-M_d(3)-M_d(2).}              \tag{8}
\]

Cada \(\pi_d\) es entero. También es no negativo: tome dentro de un
alfabeto de seis letras dos subalfabetos disjuntos de tamaños tres y dos.
Los collares aperiódicos que usan solo el primero y los que usan solo el
segundo son subconjuntos disjuntos de los collares sobre seis letras. Por
ello \(M_d(6)\ge M_d(3)+M_d(2)\), y sumar \(M_d(1)\ge0\)
prueba la afirmación.

Construya el monoide abeliano libre que tiene \(\pi_d\) generadores
primos de grado \(d\), y asigne a cada generador la norma \(6^d\). La
identidad clásica de collares

\[
 \prod_{d\ge1}(1-T^d)^{-M_d(r)}={1\over1-rT}             \tag{9}
\]

da, como identidad de series formales,

\[
 \prod_{d\ge1}(1-T^d)^{-\pi_d}
 ={(1-3T)(1-2T)\over(1-T)(1-6T)}=Z(T).                   \tag{10}
\]

No hay pesos fraccionarios ni torres truncadas en (10). Si \(P\) es uno
de esos primos, defina

\[
 \Lambda_{\mathcal P}(P^j)=\deg(P)\log6,
 \qquad \Lambda_{\mathcal P}(N)=0
 \quad\hbox{si \(N\) no es potencia de un primo}.       \tag{11}
\]

Para \(N=\prod_P P^{a_P}\),

\[
 \sum_{D\mid N}\Lambda_{\mathcal P}(D)
 =\sum_P a_P\deg(P)\log6=\log|N|,                       \tag{12}
\]

que es la renovación unitaria exacta, elemento por elemento.

Tomando derivada logarítmica en (10),

\[
 \sum_{d\mid k}d\pi_d=6^k+1-3^k-2^k.                  \tag{13}
\]

La masa de Mangoldt no normalizada en grado \(k\) es \(\log6\) veces el
miembro izquierdo. En lo sucesivo absorbemos \(\log6\) en el kernel y
llamamos \(\Psi_k\) al entero de (13). La ecuación (4) y la ley prima
fuerte **de grado** quedan probadas. No se la identificará en lo que
sigue con el PNT continuo de los enteros ordinarios.

---

## 2. Ecuación funcional y cero exterior

Una sustitución directa prueba (3):

\[
 \begin{aligned}
 (1-3/(6T))(1-2/(6T))
   &={(1-3T)(1-2T)\over6T^2},\\
 (1-1/(6T))(1-1/T)
   &={(1-T)(1-6T)\over6T^2}.
 \end{aligned}                                          \tag{14}
\]

Quitando los dos polos, la función completada puede tomarse como

\[
 \Xi(s)=6^s(1-3\,6^{-s})(1-2\,6^{-s}).                  \tag{15}
\]

De (14), \(\Xi(1-s)=\Xi(s)\). Sus ceros son

\[
 \beta_\pm+{2\pi i k\over\log6},\qquad k\in\mathbb Z, \tag{16}
\]

con \(\beta_\pm\) dados por (5). En particular el sistema viola su
análogo de RH.

Defina sus coeficientes de Li por

\[
 \lambda_n^{\mathcal P}
 ={1\over(n-1)!}\left.{d^n\over ds^n}
 \{s^{n-1}\log\Xi(s)\}\right|_{s=1}.                  \tag{17}
\]

Sea \(h=\log6\), \(L_{n-1}=L_{n-1}^{(1)}\). Al desarrollar los dos
logaritmos de (15), la identidad

\[
 {1\over(n-1)!}\left.{d^n\over ds^n}
 \{s^{n-1}e^{-us}\}\right|_{s=1}
 =-u e^{-u}L_{n-1}(u)                                    \tag{18}
\]

produce la fórmula aritmética convergente

\[
 \boxed{
 \lambda_n^{\mathcal P}
 =hn+h\sum_{k\ge1}{2^{-k}+3^{-k}\}L_{n-1}(kh).}        \tag{19}
\]

La generatriz

\[
 \mathcal G_{\mathcal P}(z)
 =z{d\over dz}\log{\Xi(1/(1-z))\over\Xi(1)}
 =\sum_{n\ge1}\lambda_n^{\mathcal P}z^n               \tag{20}
\]

tiene su singularidad de menor módulo en

\[
 w_0=1-{1\over\beta_+}
 =-{\log2\over\log3},qquad
 R:=|w_0|^{-1}={\log3\over\log2}>1.                    \tag{21}
\]

Es única: para \(\rho=\beta_++i\gamma\),

\[
 \left|1-{1\over\rho}\right|^2
 ={(1-\beta_+)^2+\gamma^2\over\beta_+^2+\gamma^2},     \tag{22}
\]

que es estrictamente mínima en \(\gamma=0\); los ceros con parte real
\(\beta_-<1/2\) dan módulos mayores que uno. Restando la parte principal
en \(w_0\) y aplicando Cauchy en un círculo hasta la siguiente
singularidad se obtiene

\[
 \boxed{
 \lambda_n^{\mathcal P}=-w_0^{-n}+O(R_1^n),
 \qquad 1<R_1<R.}                                       \tag{23}
\]

En particular, para \(n\) par,

\[
 \lambda_n^{\mathcal P}=-(1+o(1))R^n.                  \tag{24}
\]

---

## 3. Forma prima--polo completamente acoplada

El falsificador puede escribirse exactamente en la forma del gate
aritmético. Para \(\varepsilon>0\), ponga

\[
 \begin{aligned}
 P_{n,\varepsilon}
   &=h\sum_{k\ge1}6^{-\varepsilon k}L_{n-1}(kh),\\
 Q_{n,\varepsilon}
   &=h\sum_{k\ge1}\Psi_k\,6^{-(1+\varepsilon)k}
       L_{n-1}(kh),                                      \tag{25}\\
 A_n&=hn+h\sum_{k\ge1}6^{-k}L_{n-1}(kh),\\
 \lambda_{n,\varepsilon}^{\mathcal P}
   &=A_n+P_{n,\varepsilon}-Q_{n,\varepsilon}.
 \end{aligned}
\]

Todas las series de (25) convergen absolutamente. Usando (4), sin separar
ninguna torre,

\[
 \begin{aligned}
 \lambda_{n,\varepsilon}^{\mathcal P}
 ={}&hn+h\sum_{k\ge1}6^{-k}L_{n-1}(kh)\\
 &+h\sum_{k\ge1}{-6^{-k}+2^{-k}+3^{-k}\}
       6^{-\varepsilon k}L_{n-1}(kh).                    \tag{26}
 \end{aligned}
\]

Por (19), \(\lambda_{n,\varepsilon}^{\mathcal P}\to
\lambda_n^{\mathcal P}\) para cada \(n\). Más importa aquí la diagonal
\(\varepsilon_X=e^{-X/100}\). El cero dominante de la contribución
\(2^{-k}6^{-\varepsilon_Xk}\) se desplaza de \(\beta_+\) a
\(\beta_+-\varepsilon_X\); por tanto

\[
 w_X=1-{1\over\beta_+-\varepsilon_X}=w_0+O(\varepsilon_X).
 \tag{27}
\]

Las demás singularidades permanecen separadas uniformemente de \(w_X\).
Para hacer explícito que no se perdió ningún factor, (26) es el
coeficiente de Li de la función meromorfa

\[
 \Xi_\varepsilon(s)=6^s(1-6^{-s})
 {\{1-3\,6^{-(s+\varepsilon)}\}
  \{1-2\,6^{-(s+\varepsilon)}\}
  \over 1-6^{-(s+\varepsilon)}}.                        \tag{27a}
\]

En efecto, desarrollar sus cuatro logaritmos reproduce término a
término (26). El cero exterior está en
\(\beta_+-\varepsilon\), el polo artificial está en
\(-\varepsilon\), y el cero fijo restante está en \(0\), en cada caso
junto con sus traslaciones por \(2\pi i\mathbb Z/h\). Las familias con
parte real \(0\) o \(-\varepsilon\) se envían por
\(s=(1-z)^{-1}\) fuera del disco unidad; la familia con parte real
\(\beta_--\varepsilon<1/2\) también. Las singularidades no reales de la
familia \(\beta_+-\varepsilon\) quedan uniformemente más lejos del origen
que \(w_X\). Por tanto, tras sustraer la parte principal en \(w_X\), existe
un disco fijo, mayor que \(|w_X|\), en el que el resto es holomorfo y
uniformemente acotado para \(\varepsilon\) pequeño. Cauchy da, ahora
uniformemente para \(\varepsilon_X\to0\),

\[
 \boxed{
 \lambda_{n,\varepsilon_X}^{\mathcal P}
 =-w_X^{-n}+O(R_1^n),\qquad
 1\le n\le X,}                                           \tag{28}
\]

para algún \(1<R_1<R\), con constante absoluta uniforme en \(n\) y en
\(X\) grande. Como
\(n\varepsilon_X\to0\) uniformemente en \(n\le X\),

\[
 |w_X|^{-n}=R^n(1+o(1)).                                 \tag{29}
\]

Las ecuaciones (28)--(29) conservan el canal polar y toda la suma Euler:
son una evaluación de su diferencia exacta (25), no una cota separada.

---

## 4. La cola profunda tiene densidad \(1/4\)

El evento de (6) equivale exactamente a

\[
 \lambda_{n,\varepsilon_X}^{\mathcal P}+\log(n+1)
 \le-e^{\sqrt X}.                                       \tag{30}
\]

Fije \(\delta>0\). Por (28)--(29), para \(X\) grande, todo entero par

\[
 n\ge {1+\delta\over\log R}\sqrt X                     \tag{31}
\]

satisface (30), y ningún entero impar en ese rango la satisface. Del otro
lado, (28) y una cota de Cauchy uniforme para los grados menores muestran
que (30) no se cumple cuando

\[
 n\le {1-\delta\over\log R}\sqrt X.                    \tag{32}
\]

La franja entre (31) y (32) tiene masa armónica \(O_\delta(1)\), que es
\(o(H_X)\). Finalmente,

\[
 \sum_{\substack{c\sqrt X\le n\le X\\2\mid n}}{1\over n}
 ={1\over2}\log{X\over c\sqrt X}+O(1)
 ={1\over4}\log X+O_c(1).                              \tag{33}
\]

Dividir por \(H_X=\log X+O(1)\), y luego dejar
\(\delta\downarrow0\), prueba (6).

---

## 5. Alcance exacto del no-go

El sistema (2) satisface simultáneamente:

1. pesos de Mangoldt no negativos y constantes en cada torre;
2. multiplicidad unitaria de cada primo formal;
3. renovación divisora exacta (12);
4. producto de Euler con \(\pi_d\in\mathbb Z_{\ge0}\);
5. ecuación funcional exacta (3);
6. ley prima de grado con error relativo \(O(2^{-k})\);
7. la misma fase Laguerre y el mismo acoplamiento polo--Euler de (25).

Y, aun así, falla el límite profundo con valor exacto \(1/4\). Por tanto
ninguna desigualdad **universal** derivada solo de esos siete inputs puede
probar `104_75`.

El sistema no comparte varios datos esenciales de la zeta de Riemann: el
espectro de normas son potencias de seis con multiplicidad, no todos los
enteros con factorización ordinaria; su completamiento no contiene el
factor Gamma real de \(\zeta\); y es un sistema graduado, por lo que tiene
periodicidad vertical y polos en toda la progresión
\(1+2\pi i\mathbb Z/\log6\), no un único polo sobre la recta
\(\Re s=1\).

En particular, tampoco satisface el PNT ordinario en la variable continua
de norma. Si

\[
 \psi_{\mathcal P}(x)
   =\sum_{|N|\le x}\Lambda_{\mathcal P}(N),
\]

entonces

\[
 \psi_{\mathcal P}(6^k)
 =h\sum_{j\le k}(6^j+1-3^j-2^j)
 ={6h\over5}\,6^k+O(3^k+k),                             \tag{34}
\]

mientras la misma función permanece constante en
\([6^k,6^{k+1})\). Así, \(\psi_{\mathcal P}(x)/x\) oscila entre límites
distintos (desde \(h/5\) hasta \(6h/5\), salvo la convención en los
extremos) y no tiende a \(1\).

Estos datos no son defectos ocultos del falsificador: delimitan
exactamente su alcance. El documento descarta un teorema universal basado
en los siete inputs de grado enumerados arriba; **no** descarta un
argumento que use el PNT continuo, el soporte no reticular
\(\{\log m:m\in\mathbb N\}\), la multiplicidad uno de cada norma entera
ordinaria o el factor Gamma. Una prueba para los pesos reales
\(\Lambda(m)\) debe usar de manera esencial al menos una propiedad que el
modelo no conserve.

**Veredicto.** El selector unitario y las interacciones multiplicativas de
`104_20`/`104_48`/`104_49` no pueden, como axiomas abstractos, dar la cota
unilateral pedida. El único frente sobreviviente sigue siendo una
desigualdad específica de la localización ordinaria \(\{\log p\}\) y del
factor Gamma de Riemann. No se obtuvo esa desigualdad aquí.

---

## 6. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 unit_renewal_euler_deep_tail_falsifier.py
```

El checker verifica exactamente las multiplicidades, (13), la renovación
en elementos formales de prueba y (14). Numéricamente verifica la
singularidad dominante de (20) por extracción de Cauchy y la convergencia
de la densidad armónica del modelo dominante a \(1/4\). La prueba de los
enunciados para todo grado está en el texto.
