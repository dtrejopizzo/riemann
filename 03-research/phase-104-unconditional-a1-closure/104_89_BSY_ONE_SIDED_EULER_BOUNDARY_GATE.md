# 104_89 — Gate unilateral BSY para truncaciones Euler reales

**Resultado.** Las truncaciones globales cero-libres de `104_85`,
normalizadas en \(s=1\), tienen media logarítmica de Poisson exactamente
cero. La función límite

\[
 H(s)=(s-1)\zeta(s),\qquad H(1)=1,                       \tag{1}
\]

tiene media

\[
 D_B=-\log|B(0)|
 =\sum_{\Re\rho>1/2}m_\rho
      \log { |\rho|\over|1-\rho|}\ge0.                  \tag{2}
\]

Por tanto, para **cada** truncación \(X\),

\[
 \boxed{
 D_B\le
 \int_{\mathbb R}
 \left(
  \log|H(\tfrac12+it)|
  -\log|\widehat F_X(\tfrac12+it)|
 \right)_+
 {dt\over2\pi(t^2+1/4)}.}                               \tag{3}
\]

En consecuencia, basta construir una sucesión \(X_j\to\infty\) para la
cual el miembro derecho de (3) tienda a cero. Éste es un target directo,
unilateral y escrito solo con la zeta real y truncaciones de sus pesos
\(\Lambda(m)\); implicaría \(D_B=0\) y, por tanto, RH.

La convergencia puntual, casi everywhere o en medida de los logaritmos no
basta. Existe una familia explícita de funciones cero-libres, normalizadas,
cuyas medias son cero y cuyos log-módulos convergen casi everywhere al
módulo de una función con un cero interior. Toda la diferencia (2) escapa
en un pozo de Poisson de medida decreciente y profundidad creciente en el
punto de infinito de la recta crítica.

Además, polo, ecuación funcional y un canal Euler con soporte en las
potencias de los primos ordinarios y pesos de Mangoldt estrictamente
positivos tampoco fuerzan (3). La familia

\[
 Z_a(s)=C_a{(s-1)^2-a^2\over s-1}\zeta(s-a)\zeta(s+a),
 \qquad0<a<{1\over2},                                   \tag{4}
\]

tiene esas propiedades, con pesos

\[
 \Lambda(n)(n^a+n^{-a})>0,                              \tag{5}
\]

y posee ceros fuera de la línea. No conserva los pesos exactos
\(\Lambda(n)\); por el teorema de unicidad de `104_88`, conservarlos
literalmente fijaría la propia \(\zeta\).

Este documento no prueba (3), Deep-\(\Lambda\) ni RH. Identifica la cota
unilateral mínima para este ataque y demuestra por un falsificador exacto
por qué no se sigue de Fatou, subarmonicidad, positividad Euler ni
convergencia interior.

---

## 1. Normalización global con media cero

Sea \(F_X\) la función cero-libre de `104_85`. Al dividir por su valor en
uno se obtiene

\[
 \widehat F_X(s)={F_X(s)\over F_X(1)}=\exp L_X(s),       \tag{6}
\]

\[
 L_X(s)=
 \sum_{m\le X}{\Lambda(m)\over\log m}(m^{-s}-m^{-1})
 +\int_1^X{x^{-1}-x^{-s}\over\log x}\,dx.              \tag{7}
\]

La singularidad aparente del integrando en \(x=1\) es removible. Por ello
\(L_X\) es entera, \(\widehat F_X\) es entera y cero-libre, y
\(\widehat F_X(1)=1\).

Ponga

\[
 d\nu(t)={dt\over2\pi(t^2+1/4)}.                        \tag{8}
\]

Es una probabilidad y su función característica es

\[
 \int_{\mathbb R}e^{ity}\,d\nu(t)=e^{-|y|/2}.          \tag{9}
\]

En la recta crítica, \(u_X(t)=\log|\widehat F_X(1/2+it)|\)
vale

\[
\begin{aligned}
 u_X(t)={}&
 \sum_{m\le X}{\Lambda(m)\over\log m}
 \{m^{-1/2}\cos(t\log m)-m^{-1}\}\\
 &+\int_0^{\log X}
 {1-e^{y/2}\cos(ty)\over y}\,dy.                       \tag{10}
\end{aligned}
\]

La ecuación (9) anula por separado la media de cada llave y de cada
integrando:

\[
 \int m^{-1/2}\cos(t\log m)d\nu(t)=m^{-1},
 \qquad
 \int e^{y/2}\cos(ty)d\nu(t)=1.                        \tag{11}
\]

Las sumas e integrales son finitas, de modo que Fubini no presenta ningún
problema. Así

\[
 \boxed{\int_{\mathbb R}u_X(t)d\nu(t)=0\quad(X<\infty).} \tag{12}
\]

Ésta es también la fórmula de Poisson para
\(\log|\widehat F_X|\), vista desde \(s=1\), pero (10)--(11)
comprueban directamente que no se omitió una masa en infinito en cada
truncación.

## 2. El defecto exacto de la función límite

Use el mapa del disco al semiplano

\[
 s={1\over1-z}.                                         \tag{13}
\]

El centro \(z=0\) corresponde a \(s=1\), la circunferencia a
\(s=1/2+it\), y la medida angular se transforma exactamente en (8).
Los ceros de \(H\) con \(\Re\rho>1/2\) se transforman en

\[
 w_\rho={\rho-1\over\rho},\qquad |w_\rho|<1.            \tag{14}
\]

Poisson--Jensen da

\[
 \boxed{
 \int_{\mathbb R}\log|H(\tfrac12+it)|d\nu(t)
 =\sum_{\Re\rho>1/2}m_\rho\log{1\over|w_\rho|}
 =D_B.}                                                  \tag{15}
\]

El factor \(s-1\) tiene media logarítmica cero, de manera que (15) es la
forma normalizada del criterio Balazard--Saias--Yor. El crecimiento
polinomial de la zeta elimina un factor singular adicional.

Restando (12) de (15),

\[
 \int(u-u_X)d\nu=D_B,
 \qquad u(t)=\log|H(1/2+it)|.                            \tag{16}
\]

Como \(f\le f_+\), (16) implica (3). También da

\[
 \|u-u_X\|_{L^1(\nu)}\ge D_B.                           \tag{17}
\]

Hay una contabilidad aún más precisa. Si

\[
 I_X=\int (u-u_X)_+d\nu,
 \qquad J_X=\int (u_X-u)_+d\nu,                          \tag{17a}
\]

entonces (16) equivale exactamente a

\[
 \boxed{I_X=D_B+J_X.}                                    \tag{17b}
\]

En particular, el blanco \(I_{X_j}\to0\) exige simultáneamente
\(D_B=0\) y \(J_{X_j}\to0\). Es una condición suficiente para RH, pero
no se afirma aquí que RH por sí sola fuerce esa convergencia para esta
familia concreta de truncaciones. Esa dirección también necesita una
prueba de *tightness* de borde.

Por ello cualquiera de las dos condiciones

\[
 \|u-u_{X_j}\|_1\longrightarrow0,
 \qquad\hbox{o solamente}\qquad
 \|(u-u_{X_j})_+\|_1\longrightarrow0                   \tag{18}
\]

implica RH. La segunda es estrictamente la obligación unilateral natural;
controlar \((u_X-u)_+\) tiene la dirección equivocada.

### 2.1 El blanco no es más fuerte que RH si se permite una subsucesión

Para cortes reales \(X\ge2\), defina

\[
 J(x)=\sum_{2\le m\le x}{\Lambda(m)\over\log m},
 \qquad
 L_2(x)=\int_2^x{dt\over\log t},
 \qquad A(x)=J(x)-L_2(x).                               \tag{18a}
\]

Entonces

\[
 \boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
 \exists X_j\to\infty:\ 
 \|u-u_{X_j}\|_{L^1(\nu)}\to0.}                         \tag{18b}
\]

La implicación de derecha a izquierda ya es (17). Para la recíproca, bajo
RH la cota cuadrática de Cramér da

\[
 \int_2^\infty {A(x)^2\over x^2}\,dx<\infty.            \tag{18c}
\]

En efecto, la sumación parcial exacta

\[
 A(x)={\psi(x)-x\over\log x}
 +\int_2^x{\psi(t)-t\over t\log^2t}\,dt+{2\over\log2}   \tag{18d}
\]

y
\(\int_Y^{2Y}|\psi(t)-t|^2dt\ll Y^2\) bajo RH hacen
sumable el primer término por bloques diádicos; Cauchy--Schwarz da
\[
 \int_2^x{\psi(t)-t\over t\log^2t}\,dt
 =O(\sqrt x/\log^2x),
\]
que trata el segundo.

La energía finita (18c) permite elegir una sucesión no atómica con
\[
 {A(X_j)^2\over X_j}\longrightarrow0.                  \tag{18e}
\]

Para \(s=1/2+it\), integración por partes en la cola da

\[
\begin{aligned}
 \log H(s)-L_X(s)
 ={}&-(X^{-s}-X^{-1})A(X)\\
 &+s\int_X^\infty A(x)x^{-s-1}dx
 -\int_X^\infty A(x)x^{-2}dx.                          \tag{18f}
\end{aligned}
\]

Mellin--Plancherel y la elección de \(\nu\) producen las identidades

\[
\begin{aligned}
 \int\left|s\int_X^\infty A(x)x^{-s-1}dx\right|^2d\nu
 &=\int_X^\infty{A(x)^2\over x^2}dx,\\
 \int|X^{-s}-X^{-1}|^2d\nu&=X^{-1}-X^{-2}.             \tag{18g}
\end{aligned}
\]

El último término de (18f) tiende a cero por Cauchy--Schwarz. Las
ecuaciones (18c), (18e) y (18g) dan convergencia en \(L^2(\nu)\), y por
tanto en \(L^1(\nu)\), de las partes reales. Esto prueba (18b).

La equivalencia usa en la dirección RH \(\Rightarrow\) la estimación
condicional de Cramér; no es un avance hacia una prueba incondicional.
Su función aquí es demostrar que el gate unilateral con subsucesión tiene
exactamente la fuerza correcta. Las fases 49 y 101 ya contienen criterios
de energía de Cramér equivalentes; no se reclama aquí una nueva equivalencia,
sino su traducción a las truncaciones duras concretas de (7).

## 3. Escape de masa en el punto de infinito

Sea \(b_a\) un factor de Blaschke elemental con \(0<|a|<1\), normalizado
por \(b_a(0)=|a|\), y ponga

\[
 H_a(z)={b_a(z)\over|a|},
 \qquad D=-\log|a|>0.                                   \tag{19}
\]

Entonces \(H_a(0)=1\), tiene un cero interior y

\[
 \log|H_a(e^{i\theta})|=D                              \tag{20}
\]

casi everywhere. Para \(0<r<1\), defina

\[
 F_r(z)=\exp\left\{
 D\left[1-{1+rz\over1-rz}\right]\right\}.             \tag{21}
\]

Cada \(F_r\) es cero-libre y \(F_r(0)=1\). En la frontera,

\[
 \log|F_r(e^{i\theta})|
 =D\{1-P_r(\theta)\},
 \qquad
 P_r(\theta)={1-r^2\over|1-re^{i\theta}|^2}.           \tag{22}
\]

Como \(\int P_r\,d\theta/(2\pi)=1\), cada media de (22) es cero.
Pero \(P_r(\theta)\to0\) para todo \(\theta\ne0\), así que los
log-módulos convergen casi everywhere y en medida a (20), cuya media es
\(D\). Además,

\[
 \int|D-\log|F_r||{d\theta\over2\pi}
 =D\int P_r{d\theta\over2\pi}=D.                       \tag{23}
\]

Toda la masa perdida vive en el pozo negativo \(-DP_r\), concentrado en
\(z=1\), que mediante (13) es \(|t|=\infty\). Esto falsifica cualquier
paso basado solo en convergencia casi everywhere, convergencia en medida,
Fatou o subharmonicidad.

Visto desde el cociente \(Q_r=H_a/F_r\), se tiene exactamente

\[
 \log|Q_r(e^{i\theta})|=DP_r(\theta)\ge0,
 \qquad I_r=D,\quad J_r=0.                              \tag{23a}
\]

Así el falsificador satura (17b): el defecto interior completo reaparece
en la parte positiva aunque el cociente tienda a uno casi everywhere.

El falsificador puede hacerse localmente invisible dentro del disco:

\[
 S_{r,n}(z)=\exp\left\{
 D\left[1-{1+rz^n\over1-rz^n}\right]\right\}.          \tag{24}
\]

Si \(n\to\infty\), entonces \(S_{r,n}\to1\) uniformemente en todo
compacto del disco. Eligiendo simultáneamente \(r=r_n\uparrow1\) con
\(\sum_n\sqrt{1-r_n}<\infty\), Borel--Cantelli da

\[
 \log|S_{r_n,n}(e^{i\theta})|\longrightarrow D          \tag{25}
\]

para casi todo \(\theta\), mientras cada media sigue siendo cero. Por
tanto ni siquiera convergencia local interior más convergencia fronteriza
casi everywhere proporciona la uniformidad integrable de (18).

El defecto puede sobrevivir incluso cuando el límite también es cero-libre.
Ponga

\[
 C_r(w)={1+rw\over1-rw},
 \qquad
 G_{r,n}(z)=\exp\{D[C_r(z^n)-C_{-r}(z^n)]\}.             \tag{25a}
\]

Entonces \(G_{r,n}(0)=1\), no tiene ceros y su log-módulo de borde es

\[
 \log|G_{r,n}(e^{i\theta})|
 =D\{P_r(n\theta)-P_{-r}(n\theta)\},                    \tag{25b}
\]

de media cero. Si \(n\to\infty\) y \(r=r_n\uparrow1\) con
\(\sum_n\sqrt{1-r_n}<\infty\), entonces \(G_{r_n,n}\to1\)
uniformemente en compactos y (25b) tiende a cero casi everywhere. Sin
embargo, como el signo de \(P_r-P_{-r}\) es el de \(\cos\theta\),

\[
 \int(P_r-P_{-r})_+{d\theta\over2\pi}
 ={4\over\pi}\arctan{1+r\over1-r}-1\longrightarrow1.  \tag{25c}
\]

Por tanto

\[
 \int\log^+|G_{r_n,n}|{d\theta\over2\pi}\longrightarrow D. \tag{25d}
\]

Este falsificador balanceado prueba que ni siquiera «defecto interior
cero + límite cero-libre + convergencia local y fronteriza» fuerza por sí
solo \(J_X\to0\) en (17b). Para las truncaciones Euler reales esa
convergencia podría seguir siendo cierta, pero sería un teorema aritmético
adicional y no un principio funcional general.

## 4. Falsificador con soporte primo ordinario

Fije \(0<a<1/2\) y elija \(C_a\) para que (4) tenga residuo uno en
\(s=1\). Los polos de \(\zeta(s-a)\) y \(\zeta(s+a)\), situados en
\(1+a\) y \(1-a\), son cancelados por \((s-1)^2-a^2\). Queda solamente
el polo explícito en \(s=1\).

La función completada es

\[
 \Xi_a(s)={1\over4C_a}(s^2-a^2)(s-1)\pi^{-s}
 \Gamma\!\left({s-a\over2}\right)
 \Gamma\!\left({s+a\over2}\right) Z_a(s)
 =\xi(s-a)\xi(s+a),                                    \tag{26}
\]

y satisface \(\Xi_a(s)=\Xi_a(1-s)\). En \(\Re s>1+a\), su canal Euler
es

\[
 -{d\over ds}\log\{\zeta(s-a)\zeta(s+a)\}
 =\sum_{n\ge2}{\Lambda(n)(n^a+n^{-a})\over n^s}.       \tag{27}
\]

Los coeficientes del canal Euler son estrictamente positivos y viven en
las potencias de los primos ordinarios; el factor racional de (4) forma
parte del bloque de completamiento, no de ese canal. Como existen
infinitos ceros
\(\rho=1/2+i\gamma\) de \(\zeta\), (26) tiene ceros

\[
 \rho+a,qquad\rho-a,                                   \tag{28}
\]

fuera de la línea. Por tanto positividad, soporte, polo y ecuación funcional
no controlan (3). El dato que (27) altera es exactamente la altura de cada
salto: \(n^a+n^{-a}\) sustituye al peso unitario del canal zeta.

## 5. Las torres exactas tampoco tienen signo unilateral

La contribución completa de una torre prima ordinaria, antes de combinarla
con las demás torres y con el comparador continuo, es

\[
 \begin{aligned}
 \tau_p(t)
 &=\sum_{k\ge1}{p^{-k/2}\cos(kt\log p)-p^{-k}\over k}\\
 &=\log{1-p^{-1}\over|1-p^{-1/2-it}|}.                  \tag{29}
 \end{aligned}
\]

La imagen de \(t\log p\) módulo \(2\pi\) bajo \(\nu\) tiene densidad
*wrapped-Cauchy* \(P_r(\theta)d\theta/(2\pi)\),
\(r=p^{-1/2}\), porque sus momentos son \(r^{|k|}\). De aquí

\[
 \int\tau_p\,d\nu=0,
 \qquad
 \tau_p(0)=\log(1+p^{-1/2})>0,
 \qquad
 \tau_p(\pi/\log p)=\log(1-p^{-1/2})<0.                \tag{30}
\]

Más cuantitativamente, para \(p\ge5\), sobre el tercio central del
círculo se tiene \(P_r\ge1/3\) y \(-\tau_p\ge r/4\). Por la media cero,

\[
 \boxed{
 \int(\tau_p)_+d\nu
 =\int(-\tau_p)_+d\nu
 \ge {1\over36\sqrt p}.}                                \tag{31}
\]

En consecuencia, sumar los costos positivos torre por torre hasta \(P\)
pierde al menos \(\gg\sqrt P/\log P\). La relación exacta
\(\Lambda(p^k)=\log p\) no proporciona un signo local; cualquier prueba
de (18) debe conservar la cancelación global entre torres y comparador.

La forma dual exhibe la misma obligación. Para \(f=u-u_X\),

\[
 \int f_+d\nu
 =\sup_{0\le\varphi\le1}\int\varphi f\,d\nu.            \tag{32}
\]

Si

\[
 c_\varphi=\int\varphi d\nu,
 \qquad
 K_\varphi(y)=\Re\int\varphi(t)e^{ity}d\nu(t),          \tag{33}
\]

entonces (10) da exactamente

\[
\begin{aligned}
 \int\varphi u_Xd\nu={}&
 \sum_{m\le X}{\Lambda(m)\over\log m}
 \{m^{-1/2}K_\varphi(\log m)-m^{-1}c_\varphi\}\\
 &+\int_0^{\log X}{c_\varphi-e^{y/2}K_\varphi(y)\over y}\,dy. \tag{34}
\end{aligned}
\]

Para \(\varphi=1\), (9) hace cero cada llave: ésa es (12). Para el
selector óptimo \(\varphi=\mathbf1_{\{u>u_X\}}\), tanto
\(K_\varphi\) como \(e^{-|y|/2}-K_\varphi\) son definidas positivas, pero
no tienen signo escalar. El hueco es, por tanto, una desigualdad uniforme
sobre estas submedidas correlacionadas con la propia zeta, no otra identidad
de media.

## 6. Energía de Cauchy y límite de las cotas PNT

La medida (8) tiene el kernel exacto

\[
 \int u^{-1/2-it}v^{-1/2+it}d\nu(t)
 ={1\over\max(u,v)}.                                    \tag{35}
\]

Para una medida firmada truncada \(d\sigma\), con
\(V(y)=\sigma([1,y])\), se sigue

\[
 \boxed{
 \int\left|\int u^{-1/2-it}d\sigma(u)\right|^2d\nu(t)
 =\int_1^\infty{|V(y)|^2\over y^2}\,dy.}               \tag{36}
\]

Tomando \(d\sigma=\mathbf1_{[1,X]}(d\psi-dx)\), el miembro derecho es

\[
 \int_1^X{(\psi(y)-y+1)^2\over y^2}\,dy
 +{(\psi(X)-X+1)^2\over X}.                            \tag{37}
\]

La cota inferior incondicional de energía prima registrada en `103_71`
implica que (31) crece al menos como \(c\log X\). En particular, esta
familia de derivadas logarítmicas ni siquiera está acotada en
\(L^2(\nu)\), incluso en el escenario RH. Pasar de ellas a los logaritmos
suaviza una potencia de \(\log x\), pero Vinogradov--Korobov sigue sin dar
la cota de borde (18). La desigualdad unilateral no se obtiene elevando la
topología de convergencia interior de `104_85` a una cota cuadrática cruda.

## 7. Estado exacto

Se ha probado:

\[
 \text{cota unilateral (18)}\Longrightarrow D_B=0
 \Longleftrightarrow \mathrm{RH}.                       \tag{38}
\]

También se ha probado que ninguna de las siguientes propiedades implica
(18): cero-libertad de cada aproximante, normalización en \(s=1\),
convergencia interior, convergencia fronteriza casi everywhere o en medida,
positividad del canal Euler, soporte de ese canal en potencias primas,
polo único y ecuación funcional. El input aún no probado debe impedir específicamente
el escape de masa negativa de (22) para las alturas exactas
\(\Lambda(m)\).

## 8. Reproducción

Desde el directorio tools:

    python3 bsy_one_sided_euler_boundary_check.py

El checker confirma la masa positiva cerrada del spike balanceado y la
media cero con costos de ambos signos de las torres primas. Son controles
numéricos de identidades ya demostradas arriba, no certificados de (18).
