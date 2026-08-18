# 104_56 — Criterio de Li relajado en densidad y en bloques

**Rol.** Auditar la propuesta de reemplazar «para todo \(n\ge150\)» por
una condición fuera de un conjunto excepcional. El resultado no prueba A1
ni RH. Sí debilita rigurosamente el cuantificador necesario para una prueba:

* si RH es falsa, los índices en los que falla el margen cuártico contienen
  un conjunto **sindético**;
* por tanto basta probar el margen en bloques consecutivos de longitud no
  acotada, o fuera de un conjunto de densidad logarítmica superior cero;
* no hay una constante de densidad positiva universal deducible de los
  axiomas de Bombieri--Lagarias. Las fases dominantes pueden hacer esa
  densidad arbitrariamente pequeña.

La última precisión corrige la propuesta inicial de una constante
\(\delta _0>0\) fija.

---

## 1. Qué dice exactamente Bombieri--Lagarias, Teorema 1(c)

Sea \(R\) un multiconjunto que satisface las hipótesis de sumabilidad de
Bombieri--Lagarias y ponga

\[
 u_\rho:=\left(1-{1\over\rho}\right)^{-1}
 ={\rho\over\rho-1}.
\tag{1}
\]

El Teorema 1 de Bombieri--Lagarias, *Complements to Li's criterion for the
Riemann hypothesis*, J. Number Theory **77** (1999), 274--287, afirma la
equivalencia entre

\[
 \Re\rho\le {1\over2}\quad(\rho\in R)
\tag{2}
\]

y la siguiente cota unilateral subexponencial: para cada
\(\varepsilon>0\) existe \(c(\varepsilon)>0\) tal que

\[
 \sum_{\rho\in R}\Re(1-u_\rho^n)
 \ge-c(\varepsilon)e^{\varepsilon n}
 \qquad(n\ge1).
\tag{3}
\]

Su Corolario 1 aplica esto a un multiconjunto estable bajo conjugación y
\(\rho\mapsto1-\rho\). En esa situación

\[
 \lambda_{-n}=\lambda_n,
\qquad
 \lambda_{-n}:=\sum_\rho^*(1-u_\rho^n).
\tag{4}
\]

El artículo prueba que, si (2) falla, el miembro de (3) es negativo y de
tamaño exponencial **infinitas veces**. El enunciado publicado no afirma
densidad natural, densidad logarítmica ni una constante universal. La cita
«sometimes exponentially large» de Lagarias 2007 debe leerse con este
alcance.

La prueba de Bombieri--Lagarias contiene, sin embargo, más estructura de la
que explicita su enunciado. La sección siguiente extrae esa consecuencia.

---

## 2. Modos exteriores dominantes

Supóngase que RH es falsa. Entonces hay algún \(u_\rho\) con
\(|u_\rho|>1\). Como

\[
 |u_\rho|^2-1={2\Re\rho-1\over|\rho-1|^2}
\tag{5}
\]

y el lado derecho tiende a cero cuando \(|\rho|\to\infty\), existe un
máximo

\[
 R:=\max_\rho|u_\rho|>1.
\tag{6}
\]

Solo un número finito de ceros lo alcanza. Escríbanse, con multiplicidad,

\[
 u_1=Re^{i\phi _1},\ldots,u_K=Re^{i\phi _K}.
\tag{7}
\]

La estabilidad por conjugación hace real

\[
 S(n):=\sum_{j=1}^K\cos(n\phi_j).
\tag{8}
\]

El argumento de las páginas 3--4 de Bombieri--Lagarias da un
\(1<R_1<R\) tal que

\[
 \boxed{
 \lambda_n=-R^nS(n)
 +O(n^2R_1^n+n^2).}
\tag{9}
\]

En efecto, los demás modos exteriores tienen módulo a lo sumo \(R_1\), los
elementos con \(|\rho|\le n\) son \(O(n^2)\) bajo su hipótesis (ii), y la
cola \(|\rho|>n\) es \(O(n^2)\). La ecuación (4) convierte su cálculo con
exponente \(-n\) en (9). Esta orientación es importante: los modos
dominantes son \(u_\rho=\rho/(\rho-1)\) correspondientes a ceros a la
**derecha** de \(1/2\), no \(1-1/\rho\).

Para el coeficiente incompleto de Lagarias se obtiene la misma parte
dominante. Una vez \(n>\max_j|\Im\rho_j|^2\), todos los modos (7) están
incluidos en \(\lambda_n(\sqrt n)\). Riemann--von Mangoldt y la brecha
\(R_1<R\) dan

\[
 \boxed{
 \lambda_n(\sqrt n)=-R^nS(n)+
 O\!\left(\sqrt n\log n\,(1+R_1^n)\right).}
\tag{10}
\]

Así (9) y (10) tienen simultáneamente el mismo signo exponencial sobre
cualquier conjunto donde \(S(n)\) esté separado de cero.

---

## 3. El refuerzo correcto: un conjunto sindético de excursiones

Sea

\[
 \alpha=(\phi_1,\ldots,\phi_K)\in\mathbb T^K,
 \qquad
 H=\overline{\{n\alpha:n\in\mathbb Z\}}.
\tag{11}
\]

\(H\) es un grupo compacto monotético y la traslación por \(\alpha\) es
mínima y únicamente ergódica sobre \(H\). Sea

\[
 F(x_1,\ldots,x_K)=\sum_{j=1}^K\cos x_j.
\tag{12}
\]

Como \(F(0)=K\), puede elegirse

\[
 {K\over2}<\eta<K
\tag{13}
\]

de modo que la medida de Haar \(\mu_H\) satisfaga
\(\mu_H(F=\eta)=0\). Esto es posible porque una distribución de
probabilidad tiene a lo sumo un conjunto numerable de átomos. El abierto

\[
 U_\eta:=\{x\in H:F(x)>\eta\}
\tag{14}
\]

contiene un entorno no vacío del origen y por tanto

\[
 d:=\mu_H(U_\eta)>0.
\tag{15}
\]

Por equidistribución en el grupo compacto, el conjunto de retornos

\[
 D_\eta:=\{n\ge1:n\alpha\in U_\eta\}
\tag{16}
\]

tiene densidad natural \(d\). Además es **sindético**. Para verlo, las
traslaciones \(U_\eta-j\alpha\), \(j\ge0\), cubren \(H\) por minimalidad;
la compacidad da una subcubierta finita. Por tanto existe \(L<\infty\)
tal que todo intervalo de \(L\) enteros contiene un miembro de
\(D_\eta\).

En \(D_\eta\), \(S(n)>\eta\). De (9)--(10), para todo \(n\) suficientemente
grande en \(D_\eta\),

\[
 \boxed{
 \lambda_n\le-{\eta\over2}R^n,
 \qquad
 \lambda_n(\sqrt n)\le-{\eta\over2}R^n.}
\tag{17}
\]

Hemos probado:

**Teorema 3.1 (excursiones densas si RH falla).** Si RH es falsa, los
conjuntos

\[
 \{n:\lambda_n<0\},\qquad
 \{n:4\lambda_n\le A_n\}
\tag{18}
\]

contienen, salvo un prefijo finito, un mismo conjunto sindético de densidad
natural positiva. La segunda afirmación usa únicamente
\(A_n=O(n\log n)\), que es despreciable frente a (17).

El mismo teorema vale para cualquier margen
\(\lambda_n\ge cA_n\) con \(c>0\) fijo, y también para una perturbación
aditiva subexponencial menor que \(R^n\).

---

## 4. Dos criterios de RH con cuantificador relajado

Defina la densidad logarítmica superior

\[
 \overline\delta_{\log}(E)
 :=\limsup_{X\to\infty}{1\over\log X}
   \sum_{\substack{n\le X\\n\in E}}{1\over n}.
\tag{19}
\]

**Corolario 4.1 (excepción de densidad cero).** Las siguientes afirmaciones
son equivalentes:

1. RH;
2. existe \(E\subset\mathbb N\) con
   \(\overline\delta_{\log}(E)=0\) tal que, para todo \(n\) suficientemente
   grande fuera de \(E\),

   \[
   4\lambda_n>A_n;
   \tag{20}
   \]

3. (20) vale fuera de un conjunto cuya densidad natural superior es cero.

**Prueba.** Bajo RH, el teorema asintótico de Lagarias da
\(\lambda_n=A_n+O(\sqrt n\log n)\), mientras
\(A_n\sim\tfrac12n\log n\). Por tanto (20) vale eventualmente con
\(E=\varnothing\). Recíprocamente, si RH falla, (18) contiene un conjunto
de densidad natural \(d>0\). Por sumación parcial ese conjunto también
tiene densidad logarítmica \(d\), y debe estar contenido en cualquier
excepción a (20), contradiciendo (19). \(\square\)

La versión logarítmica es la relajación más amplia de las dos: una excepción
puede tener bloques locales grandes y aun así densidad logarítmica cero.

**Corolario 4.2 (criterio de bloques).** RH equivale a que existan bloques
consecutivos de longitudes no acotadas en los que

\[
 4\lambda_n>A_n
\tag{21}
\]

para cada índice del bloque.

**Prueba.** RH da (21) en toda una semirrecta. Si RH falla, el conjunto de
fallos contiene, después de un prefijo, un conjunto sindético; por tanto la
longitud de un bloque de éxitos está uniformemente acotada. \(\square\)

Este corolario elimina por completo la obligación de controlar cada grado:
un método de promedio sería suficiente si produjera bloques buenos de
longitud creciente, no solo muchos índices buenos dispersos.

---

## 5. Por qué no existe una \(\delta_0\) universal desde los axiomas BL

La densidad \(d\) de (15) depende de las fases dominantes. No puede
reemplazarse por una constante positiva universal usando solo sumabilidad,
conjugación y simetría funcional.

Fije enteros \(K\ge2\), \(q>2K\), ponga
\(\theta=2\pi/q\), y elija

\[
 1<R<\sec\theta.
\tag{22}
\]

Considere los modos exteriores

\[
 Re^{\pm ik\theta}\qquad(1\le k<K),
\tag{23}
\]

cada uno con multiplicidad \(K-k\), y complete cada punto mediante
conjugación y \(u\mapsto u^{-1}\). Los puntos
\(\rho=u/(u-1)\) satisfacen

\[
 {1\over2}<\Re\rho<1.
\tag{24}
\]

La primera desigualdad equivale a \(|u|>1\); la segunda sigue de
\(R\cos(k\theta)<1\), garantizada por (22) y
\(k\theta\in[\theta,\pi)\).
Es, pues, un multiconjunto finito admisible con las simetrías de una
ecuación funcional y ceros fuera de la línea.

Su suma dominante es

\[
 \begin{aligned}
 S_K(n)
 &=2\sum_{k=1}^{K-1}(K-k)
       \cos\!\left({2\pi kn\over q}\right)\\
 &=K\left\{\mathsf F_K\!\left({2\pi n\over q}\right)-1\right\},
 \end{aligned}
\tag{25}
\]

donde

\[
 \mathsf F_K(x)={1\over K}
 \left({\sin(Kx/2)\over\sin(x/2)}\right)^2
\tag{26}
\]

es el núcleo de Fejér. Si \(S_K(n)\ge0\), entonces

\[
 \left|\sin{\pi n\over q}\right|\le {1\over\sqrt K}.
\tag{27}
\]

Por tanto la proporción de clases módulo \(q\) donde el término dominante
puede ser negativo es a lo sumo

\[
 \boxed{
 {2\over\pi}\arcsin{1\over\sqrt K}+{1\over q}.}
\tag{28}
\]

Esta cantidad tiende a cero tomando primero \(K\to\infty\) y después
\(q/K\to\infty\). En las demás clases \(S_K(n)<0\), y el coeficiente de Li
es eventualmente positivo. Así la densidad de excursiones negativas puede
ser arbitrariamente pequeña dentro de la clase abstracta de
Bombieri--Lagarias.

Esto no construye un producto de Euler igual a \(\zeta\), ni prueba que las
fases dominantes de \(\zeta\) tengan esa geometría. Prueba exactamente que
una \(\delta_0\) universal no sale del teorema BL ni de las simetrías. Para
la zeta hipotéticamente no-RH existe algún \(d_\zeta>0\), pero depende de
ceros desconocidos. La formulación robusta y utilizable es, por ello,
«excepción de densidad cero» o «bloques de longitud no acotada».

---

## 6. Relación con los stop-gates previos

* `104_17` mostró que Abel--Fejér radial puede ser positivo aun cuando
  coeficientes individuales sean exponencialmente negativos. El criterio
  de bloques no contradice ese no-go: exige información Tauberiana firmada
  capaz de fabricar intervalos enteros, no solo un promedio positivo.
* `104_33` y `104_41` localizaron el defecto en la suma de residuos
  exteriores. Las fases \(\phi_j\) de este documento son precisamente los
  modos de módulo máximo de esa suma. No aparece un mecanismo nuevo para
  acotarla.
* La relajación sí abre métodos que antes eran lógicamente insuficientes:
  una estimación media puede cerrar RH si implica bloques buenos de tamaño
  creciente o un conjunto excepcional de densidad logarítmica cero.

---

## 7. Verificación reproducible

`tools/density_relaxed_li_criterion_check.py` verifica:

1. la orientación exacta \(u=\rho/(\rho-1)\) en un cuarteto racional;
2. la identidad finita de Fejér (25);
3. la cota de conteo (28) para una familia periódica;
4. que su densidad puede bajar del uno por ciento y que el conjunto de
   retornos sigue siendo sindético.

La herramienta verifica álgebra finita y conteos periódicos; los pasos de
grupo compacto y los términos de error de (9)--(10) están demostrados en
el texto, no certificados por punto flotante.

---

## 8. Veredicto

\[
\boxed{
\begin{gathered}
 \mathrm{RH\ falsa}
 \Longrightarrow
 \{n:4\lambda_n\le A_n\}
 \text{ contiene un conjunto sindético de densidad positiva},\\[2mm]
 \mathrm{RH}
 \Longleftrightarrow
 \text{el margen cuártico vale en bloques de longitud no acotada},\\[2mm]
 \mathrm{RH}
 \Longleftrightarrow
 \text{el margen cuártico vale fuera de una excepción de densidad
 logarítmica cero}.
\end{gathered}}
\tag{29}
\]

La propuesta de relajar el cuantificador es válida y considerablemente más
fuerte de lo esperado. La versión con una constante universal
\(\delta_0>0\) no está justificada y es falsa en la clase abstracta BL.
Nada de (29) prueba todavía uno solo de los bloques buenos requeridos para
la zeta real; ése es el nuevo objetivo cuantitativo.
