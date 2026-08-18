# 104_70 — Fermi de temperatura variable y no-go polar universal

**Resultado.** Una temperatura que decrece subexponencialmente no destruye
el criterio Fermi. En particular,

\[
 t_n=e^{-\sqrt n},\qquad b_n=e^{2\sqrt n},                 \tag{1}
\]

da

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 {1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+\exp(t_n(\lambda_n+b_n))}\longrightarrow0.}     \tag{2}
\]

La temperatura menor tampoco resuelve el condicionamiento prima--polo.
Hay una incompatibilidad exacta: si \(\varepsilon_n\to0\) y
\(t_np_n(\varepsilon_n)\) permanece acotado, entonces
\(t_nR^n\to0\) para todo \(R>1\). Pero detectar cualquier modo off-line de
tasa \(R\) exige \(t_nR^n\to\infty\). No existe una escala que cumpla ambas
obligaciones.

El lift prima--Laguerre acoplado sigue siendo exacto. Para la elección (1)
puede diagonalizarse como en 104_69; para una temperatura general hace falta
además una condición cuantitativa como (21a) de abajo. Las condiciones
(V1)--(V3) por sí solas no controlan el crecimiento superior de \(t_n\) y,
por tanto, la cota de Cauchy no basta por sí sola para concluir esa
aproximación diagonal. La parte polar separada
tiene, en el ejemplo (1), costo \(\exp(X^2/100-\sqrt X)\), esencialmente el
mismo costo cuadrático. Este documento prueba el criterio y el no-go; no
prueba su límite para zeta, A1 ni RH.

---

## 1. Criterio general de temperatura variable

Sean \(t_n>0\), \(b_n\ge0\), y ponga

\[
 a_n(t,b)={1\over1+\exp(t_n(\lambda_n+b_n))},\qquad
 \mathfrak F_{t,b}(X)
 ={1\over H_X}\sum_{n\le X}{a_n(t,b)\over n}.              \tag{3}
\]

Las condiciones naturales son

\[
\begin{array}{ll}
 \text{(V1)}&t_nb_n\longrightarrow\infty,\\
 \text{(V2)}&t_nR^n\longrightarrow\infty
              \quad\hbox{para todo }R>1,\\
 \text{(V3)}&b_n/R^n\longrightarrow0
              \quad\hbox{para todo }R>1.
\end{array}                                                \tag{4}
\]

**Teorema 1.1.** Bajo (V1)--(V3),

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \mathfrak F_{t,b}(X)\longrightarrow0
 \quad\Longleftrightarrow\quad
 \liminf_{X\to\infty}\mathfrak F_{t,b}(X)=0.}              \tag{5}
\]

**Demostración.** Bajo RH, \(\lambda_n\ge0\), luego

\[
 0\le a_n(t,b)\le{1\over1+e^{t_nb_n}}\longrightarrow0.
 \tag{6}
\]

La media logarítmica de una sucesión acotada que tiende a cero también
tiende a cero.

Si RH es falsa, 104_56 da \(c>0\), \(R>1\) y un conjunto \(D\) de densidad
natural \(d>0\) tales que \(\lambda_n\le-cR^n\) en \(D\). Por (V3),
\(b_n\le(c/2)R^n\) eventualmente. Entonces, en \(D\),

\[
 t_n(\lambda_n+b_n)
 \le-{c\over2}t_nR^n\longrightarrow-\infty               \tag{7}
\]

por (V2), y \(a_n(t,b)\to1\). La densidad logarítmica de \(D\) da

\[
 \liminf_{X\to\infty}\mathfrak F_{t,b}(X)\ge d>0.
 \tag{8}
\]
\(\square\)

Una familia suficiente, más fácil de comprobar, es

\[
 0<t_n\le1,\qquad
 -\log t_n=o(n),\qquad
 \log(1+b_n)=o(n),\qquad
 t_nb_n\to\infty.                                         \tag{9}
\]

Las dos condiciones \(o(n)\) implican (V2)--(V3). Es importante conservar
la condición sobre \(b_n\): las hipótesis
\(-\log t_n=o(n)\) y \(t_nb_n\to\infty\) solas permitirían una barrera
superexponencial que ocultara toda excursión.

La elección (1) satisface (9), pues

\[
 -\log t_n=\sqrt n=o(n),\qquad
 \log b_n=2\sqrt n=o(n),\qquad
 t_nb_n=e^{\sqrt n}\to\infty.                              \tag{10}
\]

---

## 2. Caracterización exacta del costo polar

El término polar regulado es

\[
 p_n(\varepsilon)
 =1+(-1)^{n-1}
 \left({1-\varepsilon\over\varepsilon}\right)^n.           \tag{11}
\]

Ponga

\[
 A(\varepsilon)={1-\varepsilon\over\varepsilon}.
\]

Para \(0<\varepsilon<1/2\),

\[
 |p_n(\varepsilon)-1|=A(\varepsilon)^n.                   \tag{12}
\]

Si \(0<t_n\le1\), entonces

\[
 \left|\,t_n|p_n(\varepsilon_n)|
 -t_n|p_n(\varepsilon_n)-1|\,\right|\le t_n\le1.
 \tag{12a}
\]

Por tanto la acotación del polo \(t_np_n\) y la de su parte divergente
\(t_n(p_n-1)\) son equivalentes. Trabajaremos con la segunda porque posee
la fórmula exacta (12).

Por tanto, dado \(K>0\),

\[
 t_n|p_n(\varepsilon_n)-1|\le K
\]

si y solo si

\[
 A(\varepsilon_n)\le(K/t_n)^{1/n},
\]

o, equivalentemente,

\[
 \boxed{\varepsilon_n\ge
 {1\over1+(K/t_n)^{1/n}}.}                                \tag{13}
\]

Si \(-\log t_n=o(n)\) y \(K\) es fijo, el lado derecho de (13) tiende a
\(1/2\). Así, controlar el polo obliga a mantener
\(\varepsilon_n\ge1/2-o(1)\), no a enviarlo a cero.

Para (1), con \(K=1\),

\[
 \varepsilon_n\ge
 {1\over1+e^{1/\sqrt n}}
 ={1\over2}-{1\over4\sqrt n}+O(n^{-3/2}).                  \tag{14}
\]

La reducción de temperatura solo mueve el regulador admisible hacia
\(1/2\); no hacia el borde \(\varepsilon=0\).

---

## 3. No-go universal temperatura--regulador

La incompatibilidad no depende de la elección subexponencial.

**Teorema 3.1.** Sean \(t_n>0\) y \(\varepsilon_n\to0\). Si existe
\(K<\infty\) tal que

\[
 t_n|p_n(\varepsilon_n)-1|\le K                           \tag{15}
\]

eventualmente, entonces para todo \(R>1\),

\[
 \boxed{t_nR^n\longrightarrow0.}                          \tag{16}
\]

En particular, (15) es incompatible con (V2).

**Demostración.** De (12) y (15),

\[
 t_nR^n
 \le K\left({R\over A(\varepsilon_n)}\right)^n
 =K\left({R\varepsilon_n\over1-\varepsilon_n}\right)^n.
 \tag{17}
\]

Como \(\varepsilon_n\to0\), la base del último miembro tiende a cero; es
menor, por ejemplo, que \(1/2\) desde algún índice. Esto prueba (16).
\(\square\)

La recíproca útil es igualmente fuerte. Si (V2) vale, entonces para toda
\(\varepsilon_n\to0\),

\[
 \boxed{t_n|p_n(\varepsilon_n)-1|\longrightarrow\infty.}  \tag{18}
\]

En efecto, dado cualquier \(R>1\), eventualmente
\(A(\varepsilon_n)\ge R\), y (12) domina a \(t_nR^n\).

Así no existe una temperatura que simultáneamente:

1. detecte todas las tasas off-line \(R>1\);
2. permita \(\varepsilon_n\to0\); y
3. mantenga acotado el canal polar antes de combinarlo con los primos.

Para permitir (2)--(3) sería necesario

\[
 {-\log t_n\over n}\longrightarrow\infty,                 \tag{19}
\]

pero entonces \(t_nR^n\to0\) para todo \(R>1\), exactamente la pérdida del
detector.

---

## 4. El lift acoplado sigue existiendo

Aunque el polo separado diverge, la combinación emparejada

\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)
 -\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)                                    \tag{20}
\]

permanece disponible. Para un \(X\) finito use, como en 104_69,

\[
 \varepsilon_X=e^{-X/100}.                                \tag{21}
\]

Ponga

\[
 \Theta_X={1\over H_X}\sum_{n\le X}{t_n\over n}.
\]

La aproximación diagonal que sigue queda garantizada si

\[
 \boxed{X e^{-\eta X}\Theta_X\longrightarrow0.}          \tag{21a}
\]

Esta condición vale, en particular, si \(0<t_n\le1\), y por tanto para la
elección (1). No es una consecuencia de (V1)--(V3): esas condiciones
permiten temperaturas \(t_n\) que crezcan más rápido que \(e^{\eta n}\).

Defina

\[
 \mathfrak F^{\mathrm{var}}_{\varepsilon_X}(X)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+\exp(t_n(\lambda_{n,\varepsilon_X}+b_n))}.
 \tag{22}
\]

La derivada respecto de \(\lambda\) tiene módulo a lo sumo \(t_n/4\).
La cota uniforme de 104_69 da, con

\[
 \eta={1\over100}-\log{200\over199}>0,\qquad M=M_{199/200},
\]

\[
 \boxed{
 |\mathfrak F^{\mathrm{var}}_{\varepsilon_X}(X)
 -\mathfrak F_{t,b}(X)|
 \le {M\over2}Xe^{-\eta X}\Theta_X\longrightarrow0.}      \tag{23}
\]

Sustituyendo (20), la expresión exacta es

\[
\boxed{
\begin{aligned}
 \mathfrak F^{\mathrm{var}}_{\varepsilon_X}(X)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 \Bigg[1+
 &e^{t_n(A_n+b_n+p_n(\varepsilon_X))}\\
 &\times\prod_{m\ge2}
 \exp\!\left(
 -{t_n\Lambda(m)\over m^{1+\varepsilon_X}}
 L_{n-1}^{(1)}(\log m)\right)
 \Bigg]^{-1}.
\end{aligned}}                                            \tag{24}
\]

Para cada \(X\), todos los productos convergen absolutamente. La
temperatura aparece dentro de la fase completa y no autoriza separar sus
factores.

En el extremo \(n=X\), la elección (1) y (21) da

\[
\begin{aligned}
 \log\{t_X|p_X(\varepsilon_X)-1|\}
 &=-\sqrt X+X\log(e^{X/100}-1)\\
 &={X^2\over100}-\sqrt X+o(1).
\end{aligned}                                             \tag{25}
\]

La mejora \(-\sqrt X\) es despreciable frente al costo \(X^2/100\). El
canal primo debe cancelar la fase polar con precisión relativa

\[
 \boxed{\exp\{-X^2/100+O(X)\}.}                            \tag{26}
\]

El factor \(t_X\) multiplica tanto los dos canales grandes como su
diferencia; por eso se cancela exactamente al medir precisión relativa.
La temperatura reduce la magnitud absoluta de ambas fases, pero no su
condicionamiento relativo.

---

## 5. Falsificador off-line

Para el cuarteto

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\},            \tag{27}
\]

y la elección (1):

* si \(n\equiv0\pmod4\), entonces
  \(t_n(Q_n+b_n)\to-\infty\);
* si \(n\equiv2\pmod4\), entonces
  \(t_n(Q_n+b_n)\to+\infty\);
* si \(n\) es impar, \(Q_n=4\) y
  \(t_n(Q_n+b_n)=4e^{-\sqrt n}+e^{\sqrt n}\to+\infty\).

Por consiguiente,

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+\exp(t_n(Q_n+b_n))}
 \longrightarrow{1\over4}.}                              \tag{28}
\]

El detector de temperatura variable no borra el divisor off-line.

---

## 6. Veredicto

**Probado:** el criterio general (5), el ejemplo (1), la caracterización
(13), el no-go universal (15)--(18), el lift acoplado (24), su aproximación
diagonal bajo (21a), el costo (25) y el falsificador (28).

**Ganancia:** bajar la temperatura conserva el criterio y ofrece una
familia nueva de observables acotados.

**No-go:** ninguna temperatura capaz de detectar todo \(R>1\) puede,
simultáneamente con \(\varepsilon_n\to0\), mantener acotado el polo
regulado. El ahorro subexponencial de temperatura nunca compensa la carga
polar.

**No probado:** una cota para el producto completo (24), el límite Fermi
para los pesos reales, A1 o RH.

---

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 variable_temperature_fermi_gate_check.py
```

El checker verifica la identidad polar, el umbral (13), la divergencia
(18), el valor \(1/4\) del cuarteto y la escala (25). Los teoremas
asintóticos se prueban en el texto.
