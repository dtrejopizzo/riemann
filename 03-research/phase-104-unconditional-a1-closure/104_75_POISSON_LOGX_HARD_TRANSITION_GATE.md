# 104_75 — Transición dura en \(\log X\), poissonización y gate de Bessel

**Resultado.** La media Fermi de `104_69` puede reemplazarse, sin perder
la equivalencia con RH, por una afirmación unilateral de densidad para el
bloque prima--polo real. Una elección completamente explícita es

\[
 B_X=\sqrt{\log(X+e)},\qquad
 \Delta_X(B_X)={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\lambda_n+\log(n+1)\le B_X\}}.                 \tag{1}
\]

Entonces

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \Delta_X(B_X)\longrightarrow0.}                          \tag{2}
\]

Con la diagonal \(\varepsilon_X=e^{-X/100}\), (2) equivale exactamente a

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)-B_X
 \right\}}\longrightarrow0,                              \tag{3}
\]

donde

\[
 Q_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).                                   \tag{4}
\]

Así, el input que falta no es una cota aditiva \(O(1)\) para cada grado:
(3) es la capa dura exacta de Fermi. La §2.1 la debilita aún más: basta
excluir, en densidad logarítmica, sobrepasos de tamaño \(e^{\sqrt X}\).

La misma frontera admite una versión poissonizada, localizada en grados
\(n=t+O(\sqrt t)\). En esa coordenada la **primera media lineal** de los
coeficientes prima--Laguerre tiene una transformada de Bessel cerrada. El
cuarteto off-line demuestra, sin embargo, que esa media lineal no controla
la transición: su media lineal poissonizada tiende a \(4\), mientras su
detector Fermi tiende a \(1/4\). Por tanto Abel, Borel, Nörlund--Rice o la
identidad de Bessel, usados solo al primer orden, no prueban (3).

Este documento identifica el input mínimo que queda en la ruta \(\log X\)
y cierra el ataque lineal poissonizado. No prueba (3), A1 ni RH.

**No duplicación interna.** `104_62` estudia la representación de Fourier
de la logística y su microfrecuencia; `104_63`, una energía cuadrática
diádica; `104_69`, la diagonal finita en media logarítmica; y `104_73`,
la representación Bernstein de la razón de presiones. Aquí las piezas nuevas
son el nivel duro móvil (10)--(22), la localización poissonizada y el
contraste exacto Bessel--Fermi (38)/(42).

---

## 1. Capa dura exacta de la media Fermi

Ponga

\[
 x_n=\lambda_n+\log(n+1),\qquad
 a_n={1\over1+e^{x_n}},\qquad
 \mathfrak F(X)={1\over H_X}\sum_{n\le X}{a_n\over n}.   \tag{5}
\]

Para \(B\ge0\), defina

\[
 \Delta_X(B)={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{x_n\le B\}}.                              \tag{6}
\]

**Lema 1.1 (sandwich de transición).** Para todo \(X\) y \(B\ge0\),

\[
 \boxed{{1\over2}\Delta_X(0)\le\mathfrak F(X)
 \le\Delta_X(B)+e^{-B}.}                                 \tag{7}
\]

Además,

\[
 \boxed{
 \mathfrak F(X)\to0
 \quad\Longleftrightarrow\quad
 \text{existe }B_X\to\infty\text{ con }\Delta_X(B_X)\to0.} \tag{8}
\]

**Demostración.** Si \(x\le0\), entonces
\((1+e^x)^{-1}\ge1/2\). Si \(x>B\), entonces
\((1+e^x)^{-1}\le e^{-x}\le e^{-B}\). Esto prueba (7).

La implicación de derecha a izquierda en (8) sigue de (7). Para la
recíproca, fije un entero \(k\ge1\). Sobre \(x_n\le k\),

\[
 a_n\ge{1\over1+e^k},
 \qquad \Delta_X(k)\le(1+e^k)\mathfrak F(X)\longrightarrow0. \tag{9}
\]

Elija \(X_k\) creciente de modo que
\(\Delta_X(k)\le1/k\) para \(X\ge X_k\), y ponga \(B_X=k\) en
\([X_k,X_{k+1})\). Entonces \(B_X\to\infty\) y
\(\Delta_X(B_X)\to0\). \(\square\)

El lema separa dos preguntas que la forma suave mezcla: el valor de la
logística lejos de su transición es inocuo; todo el contenido está en la
densidad de los grados que cruzan el nivel \(x_n=B\).

---

## 2. Un nivel móvil explícito

El criterio no necesita escoger \(B_X\) después de conocer la sucesión.

**Teorema 2.1.** Sea \(B_X\ge0\) cualquier función tal que

\[
 B_X\longrightarrow\infty,
 \qquad B_X=o(\log X).                                    \tag{10}
\]

Entonces

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \Delta_X(B_X)\longrightarrow0.}                         \tag{11}
\]

En particular sirve la elección de (1).

**Demostración.** Bajo RH, \(\lambda_n\ge0\). Por tanto

\[
 x_n\le B_X\quad\Longrightarrow\quad
 n+1\le e^{B_X}.
\]

De aquí

\[
 \Delta_X(B_X)
 \le {H_{\lfloor e^{B_X}\rfloor}\over H_X}
 \le {B_X+O(1)\over\log X+O(1)}\longrightarrow0.          \tag{12}
\]

Si RH es falsa, `104_56` da \(c>0\), \(R>1\) y un conjunto
\(D\) de densidad logarítmica \(d>0\) tales que

\[
 \lambda_n\le-cR^n\qquad(n\in D)                          \tag{13}
\]

desde un índice fijo. Ponga

\[
 Y_X=\left\lceil{3\log\log(X+e^e)\over\log R}\right\rceil. \tag{14}
\]

Para \(n\in D\cap[Y_X,X]\), (10), (13) y
\(R^{Y_X}\ge\{\log(X+e^e)\}^3\) dan, para \(X\) grande,

\[
 x_n\le-cR^n+\log(X+1)\le B_X.                            \tag{15}
\]

La masa armónica retirada por \(n<Y_X\) es
\(H_{Y_X}=O(\log\log\log X)=o(H_X)\). Luego

\[
 \liminf_{X\to\infty}\Delta_X(B_X)\ge d>0,              \tag{16}
\]

contradiciendo el límite de (11). \(\square\)

La prueba solo usa la firma exponencial y de densidad positiva de un cero
exterior. No usa la positividad coeficiente a coeficiente de Li en la
dirección no-RH.

### 2.1 Un gate todavía más débil: tolerancia \(e^{\sqrt X}\)

Para probar RH ni siquiera hace falta controlar la transición de Fermi.
Fije \(0<\alpha<1\), ponga \(S_X=e^{X^\alpha}\) y defina

\[
 \Omega_X^{(\alpha)}
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\lambda_n+\log(n+1)\le-S_X\}}.                \tag{16a}
\]

Entonces

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \Omega_X^{(\alpha)}\longrightarrow0.}                  \tag{16b}
\]

Bajo RH el indicador es idénticamente cero. Si RH es falsa, tome \(D,c,R\)
como en (13) y elija \(K>1/\log R\). Para
\(n\in D\cap[KX^\alpha,X]\),

\[
 cR^n\ge 2e^{X^\alpha}+\log(X+1)                         \tag{16c}
\]

desde cierto \(X\). La densidad logarítmica de \(D\) da

\[
 {1\over H_X}\sum_{\substack{KX^\alpha\le n\le X\\n\in D}}{1\over n}
 \longrightarrow d(1-\alpha)>0.                          \tag{16d}
\]

Por (13), esos índices están contados en (16a), lo que prueba la
dirección contraria.

La elección concreta \(\alpha=1/2\) muestra la debilidad real del input:
basta excluir, en densidad logarítmica, sobrepasos prima--polo de tamaño
\(e^{\sqrt X}\). No hace falta decidir el signo ni obtener error aditivo
\(O(1)\) en la franja de transición.

---

## 3. Traducción diagonal a los pesos reales \(\Lambda(m)\)

Use `104_69`,

\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)-Q_{n,\varepsilon},
 \qquad \varepsilon_X=e^{-X/100}.                         \tag{17}
\]

Allí se prueba, con \(\eta=1/100-\log(200/199)>0\) y una constante
\(M_0=M_{199/200}<\infty\),

\[
 \delta_X:=\sup_{n\le X}
 |\lambda_{n,\varepsilon_X}-\lambda_n|
 \le2M_0Xe^{-\eta X}\longrightarrow0.                    \tag{18}
\]

Defina \(x_{n,\varepsilon}=\lambda_{n,\varepsilon}+\log(n+1)\) y

\[
 \Delta_{X,\varepsilon}(B)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{x_{n,\varepsilon}\le B\}}.              \tag{19}
\]

Para \(X\) grande, \(\delta_X<1\), y por tanto

\[
 \boxed{
 \Delta_X(B-1)\le\Delta_{X,\varepsilon_X}(B)
 \le\Delta_X(B+1).}                                      \tag{20}
\]

Si \(B_X\) satisface (10), también lo hacen \(B_X\pm1\). El Teorema
2.1 y (20) prueban

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \Delta_{X,\varepsilon_X}(B_X)\longrightarrow0.}        \tag{21}
\]

La afirmación es una equivalencia lógica de los dos criterios, no la falsa
estimación
\(\Delta_{X,\varepsilon_X}(B_X)-\Delta_X(B_X)\to0\): un indicador duro
no es Lipschitz y puede tener masa exactamente en la transición. Las dos
inclusiones con niveles \(B_X\pm1\), junto con el cuantificador «todo nivel
que satisface (10)» del Teorema 2.1, son precisamente lo que evita ese
salto ilegítimo.

Finalmente,

\[
 x_{n,\varepsilon_X}\le B_X
 \quad\Longleftrightarrow\quad
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)-B_X,                    \tag{22}
\]

lo que prueba (3). Para cada \(X\), (4) converge absolutamente. El blanco
(3) conserva polo, Gamma, primos y potencias primas dentro de una sola
comparación firmada; solo después cuenta los grados que la violan.

La variante aún más débil de (16b) tiene la forma aritmética

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}
 \right\}}\longrightarrow0.}                            \tag{22a}
\]

La equivalencia con RH sigue de (16b), pero, como el observable es un
indicador duro, no basta comparar informalmente el error \(o(1)\) con el
tamaño del umbral. Ponga \(S_X=e^{\sqrt X}\), y denote por

\[
 \Omega_X(S)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\lambda_n+\log(n+1)\le-S\}},
\]

y por \(\Omega_{X,\varepsilon_X}(S)\) la misma expresión con
\(\lambda_{n,\varepsilon_X}\). Cuando \(\delta_X<1\), (18) da

\[
 \boxed{
 \Omega_X(S_X+1)
 \le \Omega_{X,\varepsilon_X}(S_X)
 \le \Omega_X(S_X-1).}                                  \tag{22b}
\]

Bajo RH, \(\lambda_n\ge0\), y los tres eventos son vacíos para \(X\)
grande. Si RH es falsa, use (13) sobre el conjunto \(D\), y fije
\(K>1/\log R\). Para
\(n\in D\cap[K\sqrt X,X]\), tanto \(S_X+1\) como \(S_X-1\) son
despreciables frente a \(cR^n\). Por sumación parcial y la densidad natural
\(d\) de \(D\),

\[
 {1\over H_X}\sum_{\substack{K\sqrt X\le n\le X\\n\in D}}{1\over n}
 \longrightarrow {d\over2}>0.                           \tag{22c}
\]

Por tanto los dos extremos de (22b) tienen límite inferior positivo bajo
no-RH, y el observable central tiende a cero si y solo si RH. Esto prueba
rigurosamente el lift diagonal de (16b). Entre (3) y (22a), el segundo es
el target aritmético lógicamente más débil.

---

## 4. Poissonización localizada del mismo gate

Sea \(N_t\sim\operatorname {Pois}(t)\) y defina

\[
 \mathfrak P(t)=e^{-t}\sum_{n\ge1}{t^n\over n!}
 {1\over1+(n+1)e^{\lambda_n}}.                            \tag{23}
\]

**Teorema 4.1.** Se tiene

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \mathfrak P(t)\longrightarrow0.}                        \tag{24}
\]

**Demostración.** Bajo RH, el sumando es a lo sumo \(1/(n+2)\), de
modo que

\[
 0\le\mathfrak P(t)
 \le\mathbb E{1\over N_t+1}
 ={1-e^{-t}\over t}\longrightarrow0.                     \tag{25}
\]

Suponga RH falsa y use el conjunto sindético \(D\) de (13), con huecos
a lo sumo \(M_D\). Sobre \(D\), el sumando de (23) tiende uniformemente a
uno en la cola. En la ventana

\[
 J_t=[t-2\sqrt t,t+2\sqrt t]\cap\mathbb N,                \tag{26}
\]

la razón entre dos masas de Poisson separadas por a lo sumo \(M_D\) tiende
uniformemente a uno. Parta \(J_t\) en bloques de \(M_D\) enteros y elija un
elemento de \(D\) en cada bloque. Como

\[
 \mathbb P(N_t\in J_t)\ge {3\over4}                       \tag{27}
\]

por Chebyshev, y los dos fragmentos de borde tienen masa \(o(1)\), existe
\(c_{M_D}>0\) tal que

\[
 \liminf_{t\to\infty}\mathbb P(N_t\in D)\ge c_{M_D}.   \tag{28}
\]

Por tanto \(\liminf\mathfrak P(t)\ge c_{M_D}>0\). \(\square\)

La misma prueba, sustituyendo la logística por el indicador, da para
cualquier \(B_t\to\infty\), \(B_t=o(\log t)\),

\[
 \boxed{
 \mathrm {RH}\Longleftrightarrow
 e^{-t}\sum_{n\ge1}{t^n\over n!}
 {\bf1}_{\{\lambda_n+\log(n+1)\le B_t\}}
 \longrightarrow0.}                                      \tag{29}
\]

En la dirección RH, el evento obliga a
\(N_t\le e^{B_t}=t^{o(1)}\), cuya probabilidad tiende a cero. En la
dirección contraria, el evento contiene \(D\cap J_t\) para \(t\) grande.

### 4.1 Una sola diagonal Euler

Ponga

\[
 K_t=\lceil2t\rceil,
 \qquad \varepsilon_t=e^{-K_t/100},                       \tag{30}
\]

y trunque (23) en \(1\le n\le K_t\), sustituyendo
\(\lambda_n\) por \(\lambda_{n,\varepsilon_t}\). Llame al resultado
\(\mathfrak P_{\rm diag}(t)\). De (18), aplicado con \(X=K_t\), y de la
Lipschitzianidad \(1/4\) de la logística,

\[
 |\mathfrak P_{\rm diag}(t)-\mathfrak P(t)|
 \le {M_0\over2}K_te^{-\eta K_t}
 +\mathbb P(N_t>K_t).                                     \tag{31}
\]

La cota de Chernoff

\[
 \mathbb P(N_t\ge2t)\le(e/4)^t                            \tag{32}
\]

hace tender (31) a cero. Para el detector duro, defina

\[
 \mathfrak D_{\rm diag}(t,B)
 =e^{-t}\sum_{1\le n\le K_t}{t^n\over n!}
 {\bf1}_{\{\lambda_{n,\varepsilon_t}+\log(n+1)\le B\}}.
 \tag{32a}
\]

Cuando el error uniforme de (18) es menor que uno,

\[
 \mathfrak D(t,B-1)-\mathbb P(N_t>K_t)
 \le\mathfrak D_{\rm diag}(t,B)
 \le\mathfrak D(t,B+1),                                  \tag{32b}
\]

donde \(\mathfrak D(t,B)\) denota la suma infinita de (29) con nivel
\(B\). Como \(B_t\pm1\) sigue satisfaciendo las hipótesis de (29), también
el detector duro diagonal es equivalente a RH. Así (24) y (29) admiten
una suma exterior finita y una única serie Euler absolutamente convergente
para cada \(t\).

---

## 5. La transformada lineal de Bessel

La poissonización sí simplifica exactamente el **primer momento** del
bloque prima--Laguerre. Para \(u>0\),

\[
 \boxed{
 \sum_{n\ge1}{t^n\over n!}L_{n-1}^{(1)}(u)
 =e^t\sqrt{t\over u}\,J_1(2\sqrt{tu}).}                  \tag{33}
\]

El valor en \(u=0\) se entiende por continuidad. La identidad sigue al
comparar las series

\[
 J_1(2\sqrt{tu})
 =\sum_{j\ge0}{(-1)^j(tu)^{j+1/2}\over j!(j+1)!}.         \tag{34}
\]

Para \(\varepsilon>0\), la convergencia absoluta permite intercambiar
sumas y obtener

\[
\boxed{
 e^{-t}\sum_{n\ge1}{t^n\over n!}Q_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 \sqrt{t\over\log m}\,
 J_1(2\sqrt{t\log m}).}                                  \tag{35}
\]

Aquí la convergencia necesaria para el intercambio no se deduce de una
cancelación de Bessel. En efecto, poniendo \(u=\log m\), la expansión
finita de Laguerre da

\[
 \sum_{n\ge1}{t^n\over n!}|L_{n-1}^{(1)}(u)|
 \le e^t\sqrt{t\over u}\,I_1(2\sqrt{tu})
 \le C_t e^{2\sqrt{tu}}.
\]

Para todo \(\varepsilon>0\), la desigualdad
\(2\sqrt{tu}\le(\varepsilon/2)u+2t/\varepsilon\) reduce entonces la
doble serie absoluta a una constante por
\(\sum_m\Lambda(m)m^{-1-\varepsilon/2}<\infty\). Por tanto (35) es una
identidad legítima de series absolutamente convergentes, no una
reordenación formal.

El polo también se suma exactamente. De la definición binomial,

\[
 p_n(\varepsilon)=1-\left(1-{1\over\varepsilon}\right)^n
 =1+(-1)^{n-1}\left({1-\varepsilon\over\varepsilon}\right)^n,
\]

y por ello

\[
 \boxed{
 e^{-t}\sum_{n\ge1}{t^n\over n!}p_n(\varepsilon)
 =1-e^{-t/\varepsilon}.}                                  \tag{36}
\]

Las ecuaciones (35)--(36) dan una transformada lineal cerrada y
completamente aritmética. No dan una cota para el indicador de (29): la
operación \(x\mapsto{\bf1}_{x\le B}\), o su suavizado Fermi, se aplica
**antes** de promediar.

---

## 6. No-go exacto del primer momento

Considere el cuarteto racional

\[
 q_n=4-2\operatorname {Re}\{w^n+w^{-n}\},
 \qquad w=2i.                                             \tag{37}
\]

Su media lineal poissonizada tiene la fórmula exacta

\[
\boxed{
 e^{-t}\sum_{n\ge1}{q_nt^n\over n!}
 =4-2\operatorname {Re}\left{
 e^{(w-1)t}+e^{(w^{-1}-1)t}\right}\longrightarrow4.}    \tag{38}
\]

En cambio, con

\[
 a_n^q={1\over1+(n+1)e^{q_n}},                            \tag{39}
\]

se tiene

\[
 a_n^q\longrightarrow
 \begin{cases}
 1,&n\equiv0\pmod4,\\
 0,&n\not\equiv0\pmod4.
 \end{cases}                                              \tag{40}
\]

La fórmula de filtro de raíces de la unidad da

\[
 \mathbb P(N_t\equiv r\!\!\pmod4)
 ={1\over4}\sum_{j=0}^3i^{-rj}e^{t(i^j-1)}\longrightarrow{1\over4}. \tag{41}
\]

Por consiguiente,

\[
 \boxed{e^{-t}\sum_{n\ge1}{a_n^qt^n\over n!}
 \longrightarrow{1\over4}.}                              \tag{42}
\]

El gate extremadamente permisivo (16a) también rechaza el cuarteto. Para
\(\alpha=1/2\), solo la clase \(n\equiv0\pmod4\) contribuye, y la condición
se cumple desde \(n=(1/\log2+o(1))\sqrt X\). Por sumación armónica,

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{q_n+\log(n+1)\le-e^{\sqrt X}\}}
 \longrightarrow{1\over8}.}                              \tag{42a}
\]

En efecto, los múltiplos de cuatro aportan
\(\frac14\{\log X-\frac12\log X+O(1)\}\), y las otras tres clases no
cruzan el umbral.

El contraste (38)/(42) es el falsificador solicitado: la primera media de
Bessel es positiva, acotada y asintóticamente inocua, mientras un cuarto de
los grados cruza la transición por una distancia exponencial. Por tanto
ninguna inferencia Tauberiana basada **solo en una cota o una asintótica de
esa primera media** puede llevar desde (35), o desde una continuación
Nörlund--Rice lineal equivalente, hasta (29) sin una hipótesis unilateral
adicional. Esto no afirma que la transformada completa, conocida exactamente
para todo \(t\), pierda información: como toda transformada exponencial de
una sucesión de crecimiento admisible, puede invertirse coeficiente a
coeficiente. El no-go concierne precisamente al uso de primer orden.

Esto no refuta una identidad no lineal nueva que actúe directamente sobre
el bloque emparejado. Precisa cuál debe ser su salida: (3), o su versión
poissonizada (29).

---

## 7. Veredicto

**Probado:** el sandwich (7), el nivel móvil explícito (11), su lift
diagonal exacto (21)--(22), el criterio poissonizado (24)/(29), la diagonal
finita (31), la transformada de Bessel (35), el polo (36) y el falsificador
(38)--(42).

**Reducción real:** ya no hace falta controlar
\(Q_{n,\varepsilon}-A_n-p_n(\varepsilon)\) con error \(O(1)\) para cada
\(n\). La capa exacta es (3), pero para probar RH basta el target mucho más
débil (22a): los sobrepasos mayores que \(e^{\sqrt X}\) deben ocupar
densidad logarítmica cero.

**No-go:** la primera media lineal, aunque posea la identidad de Bessel
exacta, no controla esa densidad. La pieza que falta es una desigualdad de
gran desviación unilateral para la diferencia prima--polo completa, incluso
al nivel extremadamente permisivo (22a). Una cota de segundo momento con
la escala correcta, por ejemplo

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 \left(
 Q_{n,\varepsilon_X}-A_n-p_n(\varepsilon_X)-\log(n+1)
 \right)_+^2
 =o(e^{2\sqrt X}),
\]

sería suficiente por Chebyshev, pero `104_63` prueba que
Parseval/Christoffel--Darboux desnudo vuelve a exigir la misma cancelación
firmada.

**No probado:** (3), (29), A1 o RH.

---

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 poisson_logx_hard_transition_check.py
```

El checker verifica (33), (36), (38), la equidistribución de las clases
módulo cuatro, el límite Fermi del cuarteto y la aproximación al límite
profundo \(1/8\) de (42a).
