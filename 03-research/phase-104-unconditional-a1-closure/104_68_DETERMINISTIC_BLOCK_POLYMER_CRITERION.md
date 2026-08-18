# 104_68 — Criterio de bloques deterministas y polímero prima--Laguerre

**Resultado.** La existencia abstracta de bloques buenos de `104_61` puede
reemplazarse por una sucesión completamente determinista:

\[
 I_L=\{L^2,L^2+1,\ldots,L^2+L-1\}.                         \tag{1}
\]

Defina

\[
 a_n={1\over1+(n+1)e^{\lambda_n}},
 \qquad
 P_L=\prod_{n\in I_L}(1-a_n).                              \tag{2}
\]

Entonces

\[
 \boxed{
 \mathrm {RH}
 \quad\Longleftrightarrow\quad
 \sum_{n\in I_L}a_n\longrightarrow0
 \quad\Longleftrightarrow\quad
 P_L\longrightarrow1.}                                     \tag{3}
\]

Si RH es falsa ocurre la dicotomía opuesta:

\[
 \liminf_{L\to\infty}\sum_{n\in I_L}a_n\geq1,
 \qquad P_L\longrightarrow0.                               \tag{4}
\]

El inverso de \(P_L\) posee una expansión exacta de polímeros finitos y un
lift prima--Laguerre que conserva juntos polo, bloque arquimediano, primos y
potencias primas. Más aún, el regulador puede diagonalizarse con la ventana:
se obtiene una sola sucesión de productos Euler absolutamente convergentes,
sin límite interior. La expansión no entrega aún una cota: es un gas sin
interacciones cuya función de partición factoriza de nuevo grado por grado.
Toda la dificultad permanece dentro de la actividad emparejada de cada
grado. Este documento prueba (3)--(4), no A1 ni RH.

---

## 1. Por qué las ventanas deterministas bastan

Ponga

\[
 x_n=\lambda_n+\log(n+1),\qquad
 z_n=e^{-x_n}={e^{-\lambda_n}\over n+1}.                    \tag{5}
\]

Entonces

\[
 a_n={z_n\over1+z_n},qquad
 1-a_n={1\over1+z_n}
 ={1\over1+e^{-(\lambda_n+\log(n+1))}}.                    \tag{6}
\]

### 1.1 Dirección RH

Bajo RH, \(\lambda_n\geq0\), luego

\[
 0\leq a_n\leq{1\over n+2},qquad
 0\leq z_n\leq{1\over n+1}.                               \tag{7}
\]

Como \(|I_L|=L\) y \(n\geq L^2\) en (1),

\[
 \boxed{
 \sum_{n\in I_L}a_n
 \leq{L\over L^2+2}\leq{1\over L}.}                      \tag{8}
\]

Para números \(0\leq a_n<1\),

\[
 1-\sum_{n\in I_L}a_n
 \leq\prod_{n\in I_L}(1-a_n)\leq1.                       \tag{9}
\]

Las ecuaciones (8)--(9) dan \(P_L\to1\).

### 1.2 Dirección no-RH

Si RH es falsa, `104_56` produce \(R>1\), \(c>0\), un entero \(M\) y un
conjunto sindético \(D\), después de un prefijo, tales que

\[
 \lambda_n\leq-cR^n\qquad(n\in D).                         \tag{10}
\]

Todo intervalo de \(M\) enteros suficientemente lejano contiene un elemento
de \(D\). Por tanto, para todo \(L\geq M\) grande existe

\[
 d_L\in I_L\cap D.                                         \tag{11}
\]

En ese índice,

\[
 1-a_{d_L}
 ={(d_L+1)e^{\lambda_{d_L}}
   \over1+(d_L+1)e^{\lambda_{d_L}}}
 \leq(d_L+1)e^{-cR^{d_L}}\longrightarrow0,                 \tag{12}
\]

y, por ello, \(a_{d_L}\to1\). Se sigue que

\[
 \sum_{n\in I_L}a_n\geq a_{d_L}\longrightarrow1
 \quad\text{por abajo},                                   \tag{13}
\]

mientras

\[
 0<P_L\leq1-a_{d_L}\longrightarrow0.                      \tag{14}
\]

Esto prueba (4) y las implicaciones recíprocas de (3). No se elige una
subsucesión adaptada a los ceros: las ventanas cuadráticas (1) interceptan
automáticamente cualquier conjunto sindético.

La potencia dos no es esencial. La misma prueba vale para cualquier familia
determinista de intervalos consecutivos \(J_k\) que satisfaga

\[
 |J_k|\longrightarrow\infty,qquad
 { |J_k|\over\min J_k}\longrightarrow0.                    \tag{14a}
\]

La primera condición intercepta todo conjunto sindético bajo no-RH; la
segunda hace \(\sum_{n\in J_k}(n+2)^{-1}=o(1)\) bajo RH. La elección (1)
es la normalización entera más simple y evita todo parámetro adaptativo.

### 1.3 Equivalencia interna entre suma y producto

La equivalencia de los dos límites de (3) no usa coeficientes de Li. De
(6),

\[
 -\log P_L=\sum_{n\in I_L}\log(1+z_n),                     \tag{15}
\]

y para \(z\geq0\),

\[
 {z\over1+z}\leq\log(1+z)\leq z.                          \tag{16}
\]

Así

\[
 \sum_{n\in I_L}a_n\leq-\log P_L.                         \tag{17}
\]

La implicación \(P_L\to1\Rightarrow\sum a_n\to0\) sigue de (17); la
otra ya sigue de (9). La normalización logística no oculta un pico: un solo
\(a_n\to1\) fuerza el producto a cero.

---

## 2. Expansión de polímeros exacta

Por (5)--(6),

\[
 \boxed{
 P_L^{-1}
 =\prod_{n\in I_L}(1+z_n)
 =\sum_{S\subseteq I_L}
 \exp\!\left(-\sum_{n\in S}
 \{\lambda_n+\log(n+1)\}\right).}                         \tag{18}
\]

El conjunto vacío aporta uno. Si se define la actividad de un polímero
\(S\) por

\[
 Z(S)=\prod_{n\in S}{e^{-\lambda_n}\over n+1},             \tag{19}
\]

(18) es la función de partición de un gas de sitios con ocupación cero o
uno. Todos los pesos son positivos. Bajo RH, (7) da

\[
 0\leq P_L^{-1}-1
 \leq\exp\!\left(\sum_{n\in I_L}z_n\right)-1
 \leq e^{1/L}-1.                                           \tag{20}
\]

Si RH es falsa, el sitio \(d_L\) de (11) tiene

\[
 z_{d_L}\geq{e^{cR^{d_L}}\over d_L+1},                    \tag{21}
\]

por lo que \(P_L^{-1}\geq1+z_{d_L}\to\infty\).

---

## 3. Lift prima--Laguerre regulado

Use la convención de `104_61`:

\[
\begin{aligned}
 \lambda_{n,\varepsilon}
 ={}&A_n+p_n(\varepsilon)-Q_{n,\varepsilon},\\
 Q_{n,\varepsilon}
 ={}&\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),\\
 \lambda_{n,\varepsilon}&\longrightarrow\lambda_n.
                                                               \tag{22}
\end{aligned}
\]

Para \(\varepsilon>0\), ponga

\[
 z_{n,\varepsilon}
 ={e^{-A_n-p_n(\varepsilon)}\over n+1}
 \prod_{m\geq2}\exp\!\left(
 {\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right).                             \tag{23}
\]

El producto converge absolutamente en el logaritmo y
\(z_{n,\varepsilon}=e^{-\lambda_{n,\varepsilon}}/(n+1)\).
Como \(I_L\) y su conjunto potencia son finitos para cada \(L\), se puede
pasar al borde término a término:

\[
\boxed{
\begin{aligned}
 P_L^{-1}
 =\lim_{\varepsilon\downarrow0}
 \sum_{S\subseteq I_L}
 &{\exp\!\left(-\sum_{n\in S}
       \{A_n+p_n(\varepsilon)\}\right)
  \over\prod_{n\in S}(n+1)}\\
 &\times\prod_{m\geq2}\exp\!\left(
 {\Lambda(m)\over m^{1+\varepsilon}}
 \sum_{n\in S}L_{n-1}^{(1)}(\log m)\right).
                                                               \tag{24}
\end{aligned}}
\]

La ecuación (24) conserva, para cada polímero, el polo, el bloque
arquimediano, todos los primos y todas las potencias primas hasta después de
sumar los grados del polímero. El orden de límites es vinculante:

\[
 \varepsilon\downarrow0\quad\text{con }L\text{ fijo},
 \qquad\text{después }L\to\infty.                           \tag{25}
\]

No se ha probado uniformidad que permita invertirlos.

### 3.1 Diagonal única para las ventanas cuadráticas

La estimación de Cauchy de `104_66` elimina el doble límite de (25). Ponga

\[
 N_L=L^2+L-1,\qquad \varepsilon_L=e^{-N_L/100},
 \qquad r={199\over200},
 \qquad \eta={1\over100}-\log{200\over199}>0.              \tag{25a}
\]

Existe una constante fija \(M=M_{199/200}<\infty\) tal que, para \(L\)
suficientemente grande y todo \(n\in I_L\),

\[
 |\lambda_{n,\varepsilon_L}-\lambda_n|
 \le 2MN_Le^{-\eta N_L}=:\delta_L.                        \tag{25b}
\]

Defina

\[
 a_{n,\varepsilon_L}={1\over1+(n+1)e^{\lambda_{n,\varepsilon_L}}},
 \qquad
 P_{L,\varepsilon_L}=\prod_{n\in I_L}(1-a_{n,\varepsilon_L}). \tag{25c}
\]

La logística es \(1/4\)-Lipschitz. Además, para vectores con coordenadas en
\([0,1]\), la diferencia de sus productos está acotada por la suma de las
diferencias coordenada a coordenada. Por tanto

\[
\begin{aligned}
 \left|\sum_{n\in I_L}a_{n,\varepsilon_L}
       -\sum_{n\in I_L}a_n\right|
 &\le {L\delta_L\over4},\\
 |P_{L,\varepsilon_L}-P_L|
 &\le {L\delta_L\over4},
\end{aligned}                                             \tag{25d}
\]

y el lado derecho tiende exponencialmente a cero. En consecuencia,

\[
\boxed{
 \mathrm {RH}
 \Longleftrightarrow
 \sum_{n\in I_L}a_{n,\varepsilon_L}\longrightarrow0
 \Longleftrightarrow
 P_{L,\varepsilon_L}\longrightarrow1.}                   \tag{25e}
\]

Para cada \(L\), la fórmula sin límite interior es

\[
\boxed{
 P_{L,\varepsilon_L}^{-1}
 =\sum_{S\subseteq I_L}
 {e^{-\sum_{n\in S}(A_n+p_n(\varepsilon_L))}
  \over\prod_{n\in S}(n+1)}
 \prod_{m\ge2}\exp\!\left(
 {\Lambda(m)\over m^{1+\varepsilon_L}}
 \sum_{n\in S}L_{n-1}^{(1)}(\log m)\right).}             \tag{25f}
\]

La suma en \(S\) es finita y cada producto Euler converge absolutamente.
La diagonal (25a) no prueba (25e); solo coloca el criterio exacto dentro de
una única familia aritmética convergente.

---

## 4. Auditoría: el polímero no crea interacción aritmética nueva

A pesar de la suma sobre subconjuntos, (18) es un gas **sin interacción**:

\[
 \log P_L^{-1}=\sum_{n\in I_L}\log(1+z_n).                 \tag{26}
\]

Los términos cruzados de (18) son exactamente productos de actividades
individuales; desaparecen al tomar el logaritmo. No existe una reserva
conectada entre grados que pueda pagar un sitio malo. Esto distingue (24)
de una verdadera expansión de cúmulos con interacción firmada.

Además, todos los términos de (18) son positivos. Una cota superior
\(P_L^{-1}=1+o(1)\) obliga ya a que cada actividad sea pequeña:

\[
 0\leq z_n\leq P_L^{-1}-1\qquad(n\in I_L).                 \tag{27}
\]

En particular, (20) no se puede obtener cancelando polímeros distintos.
La única cancelación disponible es la interna de (23), entre
\(p_n(\varepsilon)\) y la suma de Mangoldt, antes de exponenciar.

Para \(n\) fijo, ambas partes tienen tamaño \(\varepsilon^{-n}\). Separar
los factores de (23) produce exponentes de ese tamaño y pierde la parte
finita, como ya cuantifican `104_61` y `104_63`. Agrupar varios grados en
\(S\) no cambia este hecho: el grado máximo de \(S\) domina la divergencia
si los canales se estiman por separado.

Por tanto (24) aporta un **objetivo determinista**, pero no un mecanismo de
cota. Probar desde (24)

\[
 \boxed{P_L^{-1}=1+o(1)}                                    \tag{28}
\]

es exactamente la nueva formulación suficiente para RH.

---

## 5. Falsificador off-line

Para el cuarteto racional de `104_17`,

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\}.            \tag{29}
\]

Cada intervalo de cuatro enteros contiene un \(d\equiv0\pmod4\), y para
ese índice \(-Q_d\geq2^d\). Por tanto, para todo \(L\geq4\), existe
\(d_L\in I_L\) tal que

\[
 1-a_{d_L}
 \leq(d_L+1)e^{-2^{d_L}},\qquad
 P_L\leq(d_L+1)e^{-2^{d_L}}\longrightarrow0.               \tag{30}
\]

El criterio determinista rechaza el cuarteto en **cada** ventana grande,
no solo en promedio o en una subsucesión.

---

## 6. Veredicto

**Probado.** El criterio determinista (3), la dicotomía fuerte (4), la
expansión de polímeros (18), el lift prima--Laguerre (24), la diagonal única
(25e)--(25f) y el falsificador (30).

**Ganancia.** Ya no hay un selector existencial de intervalos: basta la
familia explícita \([L^2,L^2+L-1]\). El target es un límite escalar positivo,
\(P_L^{-1}\to1\), con una expansión aritmética finita exacta.

**No-go.** El polímero es no interactuante. La positividad de sus actividades
impide cancelar subconjuntos, y la factorización devuelve la dificultad a
cada actividad prima--polo emparejada. Presentar (18) como una interacción
nueva sería incorrecto.

**No probado.** (28) para los pesos reales \(\Lambda(m)\), un bloque nuevo
de coeficientes, A1 o RH.

---

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 deterministic_block_polymer_check.py
```

El checker usa `Fraction`. Verifica la cota RH modelo (8), las identidades
(6), (9), (15)--(18) para actividades racionales, que cada \(I_L\) con
\(L\geq4\) intercepta la clase mala del cuarteto, y la cota exacta
\(-Q_d\geq2^d\). También comprueba la desigualdad telescópica de productos
usada en (25d) y la caída de la envolvente diagonal. No certifica el límite
aritmético (28).
