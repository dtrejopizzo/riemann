# 104_110 — Núcleo primo literal de Fejér y gate VK del rayo exterior

**Pregunta.** ¿Puede probarse la cota uniforme que sobrevive en `104_108`,

\[
 \sup_{\phi\in\mathbb R}
 \left|\mathcal B^{\triangle}_{2L,L,1}(\phi)\right|
 \le \exp(o(L)),                                           \tag{1}
\]

insertando directamente el PNT efectivo de Vinogradov--Korobov en la
forma prima--Laguerre, sin separar polo, primos ni potencias primas?

**Resultado.** La forma prima literal sí admite un núcleo finito y un
contorno cerrados. Si

\[
 \alpha_{L,k}={L-|k|\over L^2}\quad (|k|<L),
 \qquad q=e^{-i\phi},
\]

se definen

\[
 \begin{aligned}
 P_{L,\phi}(u)
   &:=\sum_{|k|<L}\alpha_{L,k}q^k
           L_{2L+k-1}^{(1)}(u),\\
 Q_{L,\phi}(u)
   &:=\sum_{|k|<L}\alpha_{L,k}q^k
           L_{2L+k-1}^{(2)}(u),
 \end{aligned}                                             \tag{2}
\]

entonces, con \(E(x)=\psi(x)-x\),

\[
 \boxed{
 \mathcal B^{\triangle}_{2L,L,1}(\phi)
 =P_{L,\phi}(0)+
   \int_0^\infty E(e^u)e^{-u}Q_{L,\phi}(u)\,du.}           \tag{3}
\]

La identidad conserva conjuntamente la masa continua polar y todos los
átomos \(p^j\), con su peso real \(\Lambda(p^j)=\log p\).

Sin embargo, (1) **no** se deduce de la envolvente VK. Para la frecuencia
exacta \(\phi=\pi\), todos los sumandos de \(Q_{L,\pi}\) tienen el mismo
signo en el rayo exterior. Si

\[
 \eta(u)=c u^{3/5}(\log u)^{-1/5},\qquad
 U_L=L^{5/3}(\log L)^{1/3},                               \tag{4}
\]

entonces el majorante que resulta de

\[
 |E(e^u)|\le C e^u e^{-\eta(u)}                            \tag{5}
\]

satisface

\[
 \boxed{
 \int_0^\infty e^{-\eta(u)}|Q_{L,\pi}(u)|\,du
 \ge
 \exp\!\left{
 {4\over3}L\log L+{2\over3}L\log\log L-O(L)
 \right}.}                                               \tag{6}
\]

Así, el suavizado triangular y la modulación que reducen el costo de fase
en \(a\ge4\) a \(O(1)\) no reducen el costo absoluto VK en \(a=1\): la
frecuencia \(\pi\) alinea el rayo final. El déficit respecto de (1) es
\(\exp((4/3+o(1))L\log L)\), no una constante perdida.

Esto es un no-go para **PNT/VK + módulo después del acoplamiento
prima--polo**. No es una cota inferior para la expresión aritmética real de
(3). La cancelación firmada específica de los pesos literales
\(\Lambda(m)\) sigue siendo exactamente el teorema faltante. Este documento
no prueba (1), A1 ni RH.

---

## 1. Forma prima--polo antes de retirar el regulador

Retenga la definición de `104_41`. Para \(a>1\), la convergencia absoluta
permite sumar primero en el grado:

\[
 \begin{aligned}
 \mathcal B^{\triangle}_{2L,L,a}(\phi)
 =a\int_{1^-}^{\infty}y^{-a}
 P_{L,\phi}(a\log y)\,d\{\psi(y)-y\}.                    \tag{7}
 \end{aligned}
\]

La notación de Stieltjes en (7) no es cosmética:

\[
 d\psi(y)=\sum_{m\ge2}\Lambda(m)\,\delta_m,
 \qquad d y=\hbox{canal polar continuo}.                  \tag{8}
\]

Por tanto (7) contiene, antes de estimar, el polo, todos los primos y todas
las potencias primas. Equivalentemente,

\[
 \begin{aligned}
 \mathcal B^{\triangle}_{2L,L,a}(\phi)
 =a\sum_{m\ge2}{\Lambda(m)\over m^a}
       P_{L,\phi}(a\log m)
 -a\int_1^\infty y^{-a}P_{L,\phi}(a\log y)\,dy.          \tag{9}
 \end{aligned}
\]

No se asignará significado separado a los dos términos de (9) en \(a=1\).
Su combinación es la que continúa.

## 2. Generatriz y contorno finito exactos

Escriba

\[
 K_L(z)=\sum_{|k|<L}\alpha_{L,k}z^k
 ={(1-z^L)(1-z^{-L})\over
       L^2(1-z)(1-z^{-1})}.                               \tag{10}
\]

Las generatrices ordinarias

\[
 \sum_{d\ge0}L_d^{(1)}(u)z^d
 ={e^{-uz/(1-z)}\over(1-z)^2},
 \qquad
 \sum_{d\ge0}L_d^{(2)}(u)z^d
 ={e^{-uz/(1-z)}\over(1-z)^3}                             \tag{11}
\]

dan, para un círculo pequeño alrededor de cero,

\[
 \boxed{
 P_{L,\phi}(u)
 ={1\over2\pi i}\oint
 {e^{-uz/(1-z)}\over(1-z)^2z^{2L}}
 K_L(q/z)\,dz,}                                          \tag{12}
\]

y

\[
 \boxed{
 Q_{L,\phi}(u)
 ={1\over2\pi i}\oint
 {e^{-uz/(1-z)}\over(1-z)^3z^{2L}}
 K_L(q/z)\,dz.}                                          \tag{13}
\]

Aquí \(K_L(q/z)\) es un polinomio de Laurent finito; no se ha introducido
una serie bilateral ni una región de convergencia nueva.

También hay un contorno cerrado directamente para el observable. Sea

\[
 M_\Lambda(s)={1\over s-1}+{\zeta'(s)\over\zeta(s)}.
\]

La ecuación (8) de `104_41`, diferenciada en la variable generatriz, da

\[
 \sum_{n\ge1}B_nz^{n-1}
 =-{1\over(1-z)^2}
 M_\Lambda\!\left({1\over1-z}\right).                   \tag{14}
\]

En consecuencia,

\[
 \boxed{
 \mathcal B^{\triangle}_{2L,L,1}(\phi)
 =-{1\over2\pi i}\oint
 {M_\Lambda((1-z)^{-1})\over
   (1-z)^2z^{2L}}K_L(q/z)\,dz.}                           \tag{15}
\]

La función \(M_\Lambda=F'/F\), con \(F(s)=(s-1)\zeta(s)\), es regular en
\(s=1\). Por ello (15) es un contorno local legítimo, no una deformación a
través de ceros.

## 3. Retirada conjunta del regulador

Para cada \(L\) fijo, VK hace desaparecer el borde en infinito al integrar
(7) por partes y bajar \(a\) hasta \(1\). En el borde inferior
\(E(1)=-1\). Como

\[
 {d\over du}L_d^{(1)}(u)=-L_{d-1}^{(2)}(u),
 \qquad
 L_d^{(2)}(u)=L_d^{(1)}(u)+L_{d-1}^{(2)}(u),              \tag{16}
\]

se tiene exactamente

\[
 P_{L,\phi}(u)-P'_{L,\phi}(u)=Q_{L,\phi}(u).             \tag{17}
\]

Así,

\[
 \begin{aligned}
 \int_{1^-}^{\infty}y^{-1}P_{L,\phi}(\log y)\,dE(y)
 &=P_{L,\phi}(0)
   +\int_1^\infty {E(y)\over y^2}
       Q_{L,\phi}(\log y)\,dy,
 \end{aligned}                                           \tag{18}
\]

que, mediante \(y=e^u\), prueba (3). Para un solo grado, (18) es la
identidad conocida

\[
 B_n=n+\int_0^\infty E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.   \tag{19}
\]

La frontera \(n\) de (19) no se ha descartado; al promediarla produce
exactamente \(P_{L,\phi}(0)\).

## 4. La frecuencia \(\pi\) alinea todo el rayo final

Necesitamos una cota elemental para los ceros de Laguerre. Los ceros de
\(L_d^{(\alpha)}\) son los autovalores del truncamiento \(d\times d\) de
la matriz de Jacobi con diagonal \(2j+\alpha+1\) y extradiagonales
\(\sqrt{(j+1)(j+\alpha+1)}\). Gershgorin y

\[
 \sqrt{j(j+\alpha)}\le j+{\alpha\over2}
\]

dan

\[
 0<x_{d,j}<4d+2\alpha+2.                                 \tag{20}
\]

En (2), los grados \(d=2L+k-1\) satisfacen \(d\le3L-2\). Para
\(u\ge24L\), (20) con \(\alpha=2\) da \(x_{d,j}<u/2\). Como el coeficiente
principal de \(L_d^{(2)}\) es \((-1)^d/d!\),

\[
 (-1)^dL_d^{(2)}(u)
 ={1\over d!}\prod_{j=1}^d(u-x_{d,j})
 \ge{(u/2)^d\over d!}.                                   \tag{21}
\]

Tome ahora \(\phi=\pi\), de modo que \(q^k=(-1)^k\). Puesto que

\[
 (-1)^k(-1)^{2L+k-1}=-1,                                 \tag{22}
\]

**cada** sumando de \(Q_{L,\pi}(u)\) es negativo en \(u\ge24L\). No hay
cancelación entre grados. Reteniendo solo \(k=0\), cuyo peso es \(1/L\),

\[
 \boxed{
 |Q_{L,\pi}(u)|
 \ge {1\over L}{(u/2)^{2L-1}\over(2L-1)!}
 \qquad(u\ge24L).}                                      \tag{23}
\]

Esta alineación exacta es la contraparte prima--Laguerre de la resonancia
de residuos de `104_108`, pero no usa ceros de \(\zeta\).

## 5. Brecha de escala para VK

Para \(U_L\) de (4), se tiene \(U_L\ge24L\) cuando \(L\) es grande y

\[
 \eta(U_L+1)=O(L).                                       \tag{24}
\]

La función \(\eta\) es creciente en ese rango. De (23), sobre
\([U_L,U_L+1]\),

\[
 \begin{aligned}
 \log\!\int_0^\infty e^{-\eta(u)}|Q_{L,\pi}(u)|\,du
 &\ge
 (2L-1)\log(U_L/2)-\log(2L-1)!\\
 &\quad-\log L-\eta(U_L+1).                              \tag{25}
 \end{aligned}
\]

La cota elemental

\[
 \log d!\le d\log d-d+O(\log d)
\]

convierte (25) en (6). En particular, ni siquiera una cota
\(e^{cL}\) puede obtenerse tomando módulos después de (3), mucho menos la
barrera \(e^{\sqrt L}\) de `104_108`.

El mismo cálculo tiene una lectura como operador: la norma del funcional
\(E\mapsto\int E(e^u)e^{-u}Q_{L,\pi}(u)du\) sobre la bola ponderada de VK
es al menos el lado derecho de (6). La aritmética real puede estar muy lejos
de un extremal de esa bola; VK, por sí sola, no cuantifica esa distancia.

## 6. La monotonía tampoco repara el majorante

El punto anterior no depende de permitir errores arbitrariamente
oscilatorios. Fije una función suave \(0\le\chi_L\le1\), soportada en
\([U_L,U_L+1]\), igual a uno en
\([U_L+1/4,U_L+3/4]\), y con \(|\chi_L'|\le5\). Ponga

\[
 E_L(e^u)=-1-{1\over2}e^u e^{-\eta(U_L+1)}\chi_L(u),
 \qquad \Psi_L(y)=y+E_L(y).                              \tag{26}
\]

Para (L) grande,

\[
 \Psi_L'(y)
 =1-{1\over2}e^{-\eta(U_L+1)}
   \{\chi_L(\log y)+\chi_L'(\log y)\}
 \ge0.                                                    \tag{27}
\]

Además, por monotonía de \(\eta\),

\[
 |E_L(e^u)|\le e^u e^{-\eta(u)}                         \tag{28}
\]

para todo \(u\) suficientemente grande; sobre un compacto inicial puede
ajustarse la constante de la envolvente. La parte constante \(-1\) de
\(E_L\) cancela exactamente el borde:

\[
 P_{L,\pi}(0)-\int_0^\infty e^{-u}Q_{L,\pi}(u)\,du=0.    \tag{28a}
\]

Además,

\[
 |P_{L,\pi}(0)|
 \le\sum_{|k|<L}\alpha_{L,k}(2L+k)
 \le3L.                                                   \tag{28b}
\]

Como el resto de \(E_L\) y \(Q_{L,\pi}\) son ambos negativos en todo el
soporte, (23) muestra que la versión de (3) asociada a \(\Psi_L\) tiene
tamaño

\[
 \exp\!\left{
 {4\over3}L\log L+{2\over3}L\log\log L-O(L)
 \right}.                                                \tag{29}
\]

Por tanto VK más monotonía de la función acumulativa tampoco fuerza (1).
Este comparador es continuo y no tiene soporte en potencias primas. No es
un contraejemplo para los \(\Lambda(m)\) ordinarios; identifica exactamente
la información adicional que tendría que usar una prueba aritmética.

## 7. Auditoría frente a las fases anteriores

- `103_56` ya prueba que el módulo de un kernel Laguerre individual bajo
  VK tiene escala incorrecta. Aquí se cierra el caso nuevo que dejó
  `104_108`: un bloque triangular de longitud comparable al grado y con
  modulación uniforme. La identidad (22) muestra por qué ese suavizado no
  ayuda en la frecuencia \(\pi\).
- `103_70`--`103_71` descartan normas Hardy separadas después de una
  descomposición de Vaughan. Aquí no se descompone \(\Lambda\): (7), (15)
  y (18) mantienen el observable completo.
- `104_41` y `104_107` prueban cotas (O(L)) y (O(1)), respectivamente,
  en \(a\ge4\). La ecuación (6) cuantifica por qué VK no transporta esas
  cotas hasta \(a=1\).
- `104_53` clasifica identidades polinómicas aditivas de momentos. El
  presente argumento no introduce momentos ni cumulantes.
- `104_65` trata filtros locales fijos. El filtro triangular aquí depende
  de \(L\), tiene ancho \(2L-1\), y por ello no está cubierto por aquel
  teorema.

## 8. Veredicto

**Probado:** la forma prima literal (7)--(9), los núcleos cerrados
(12)--(13), el contorno completo (15), la retirada conjunta (3), la
alineación exacta del rayo exterior (22)--(23) y la brecha VK (6).

**Descartado:** obtener la cota uniforme de `104_108` usando solamente el
PNT/VK, aun conservando el acoplamiento prima--polo hasta la integración por
partes y aun añadiendo monotonía de la función acumulativa.

**Sobrevive:** demostrar, para los pesos literales \(\Lambda(m)\), una
cancelación firmada que haga pequeño (3) uniformemente en \(\phi\). Debe
usar información que no esté contenida en el tamaño VK ni en la monotonía;
por `104_108`, una barrera subexponencial de ese tipo probaría RH.

**No probado:** esa cancelación literal, (1), A1 o RH.

## 9. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 literal_prime_fejer_vk_gate_check.py
```

El checker usa `Fraction`. Verifica las identidades finitas de generatriz,
\(P-P'=Q\), la alineación de signos y la cota exterior (23) en familias
exactas. La estimación asintótica (25) está demostrada en el texto y no se
sustituye por muestreo.
