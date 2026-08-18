# 104_91 — Dualidad PD exacta y gate de la torre remota

**Resultado.** La formulación dual de la cota unilateral de 104_89 no
contiene una relajación oculta. Si

\[
 d\nu(t)={dt\over2\pi(t^2+1/4)},\qquad
 k(y)=\int_{\mathbb R}e^{ity}\,d\nu(t)=e^{-|y|/2},       \tag{1}
\]

entonces los núcleos que aparecen al variar \(0\leq\varphi\leq1\) son
exactamente

\[
 \mathcal K=\{K\in C(\mathbb R;\mathbb R):K\text{ es par, y }
              K,\ k-K\text{ son definidas positivas}\}.         \tag{2}
\]

No se gana coercividad reemplazando el supremo sobre selectores por un
supremo sobre (2): son el mismo problema, y los puntos extremos vuelven a
ser los selectores indicadores.

La parte aritmética del funcional posee la forma global cerrada

\[
 \int\varphi u_X\,d\nu
 =\int_{1^-}^{X}
 \left\{x^{-1/2}K(\log x)-{K(0)\over x}\right\}
 d\{J(x)-\mathrm{Li}(x)\},                       \tag{3}
\]

donde

\[
 dJ=\sum_{p^a}{1\over a}\,\delta_{p^a},\qquad
 d\mathrm{Li}(x)={dx\over\log x}.               \tag{4}
\]

Como \(d\mathrm{Li}\,\) tiene masa infinita en \(1^+\), (3) no
declara que su diferencia sea una medida de Radon en un entorno de uno.
La notación significa el funcional impropio regularizado

\[
 \int_{1^-}^Xq\,d(J-\mathrm{Li})
 :=\sum_{p^a\leq X}{q(p^a)\over a}
   -\lim_{\delta\downarrow0}\int_{1+\delta}^X
                  q(x){dx\over\log x},                 \tag{4a}
\]

para los tests \(q(x)=O(\log x)\) que aparecen aquí.

Así (3) conserva a la vez todas las torres y el comparador. La inversión
de renovación/Möbius no añade un término de signo: reconstruye la misma
discrepancia regularizada, como ya anticipan 104_80 y E101_087, §11.

Se prueba además un gate cuantitativo más fuerte que el modelo fijo de
104_90. Para cada prefijo \(M\) existe un primo ordinario \(P>M\) y un
sistema Euler que:

1. coincide literalmente con \(\Lambda(n)\) para todo \(n\leq M\);
2. coincide con la zeta en todas las torres salvo \(P^a\);
3. tiene pesos no negativos sobre las potencias de primos ordinarios;
4. conserva un PNT continuo con error de tipo Vinogradov--Korobov;
5. admite un completamiento entero con simetría \(s\leftrightarrow1-s\);
6. tiene un cero real
   \(\beta_P=\tfrac12+\log(3/2)/(2\log P)>1/2\).

Su defecto de Jensen contiene al menos

\[
 \boxed{
 D_P=\log {\log P+\log(3/2)\over
                 \log P-\log(3/2)}>0.}                 \tag{5}
\]

Por tanto ningún argumento basado en prefijos exactos, restricciones PD,
positividad, soporte primo, PNT y una ecuación funcional amplia puede
probar la cota unilateral. Una demostración para la zeta real tiene que
usar simultáneamente la igualdad literal de todas las torres y los datos
exactos de su completamiento. El contramodelo altera una torre y tiene
polos Euler adicionales; no es un contraejemplo a RH.

Este documento no prueba el límite Deep-\(\Lambda\), A1 ni RH.

---

## 1. La clase PD es exactamente el intervalo de selectores

Como \(u(t)\) y \(u_X(t)\) son pares, en

\[
 I_X=\sup_{0\leq\varphi\leq1}
       \int\varphi(t)\{u(t)-u_X(t)\}\,d\nu(t)           \tag{6}
\]

se puede reemplazar \(\varphi\) por
\((\varphi(t)+\varphi(-t))/2\). Suponga desde ahora que \(\varphi\) es
par y defina

\[
 K_\varphi(y)=\int\varphi(t)e^{ity}\,d\nu(t)
              =\int\varphi(t)\cos(ty)\,d\nu(t).        \tag{7}
\]

Las medidas positivas \(\varphi\nu\) y \((1-\varphi)\nu\) tienen
transformadas \(K_\varphi\) y \(k-K_\varphi\). El teorema de Bochner da
inmediatamente que ambas son definidas positivas.

La recíproca es igual de importante. Si \(K\) y \(k-K\) son continuas y
definidas positivas, Bochner produce medidas positivas simétricas
\(\mu,\eta\) tales que

\[
 \widehat\mu=K,\qquad \widehat\eta=k-K.                 \tag{8}
\]

Por unicidad de la transformada de Fourier de medidas finitas,

\[
 \mu+\eta=\nu.                                         \tag{9}
\]

Luego \(0\leq\mu\leq\nu\), existe
\(\varphi=d\mu/d\nu\) con \(0\leq\varphi\leq1\), y
\(K=K_\varphi\). Esto prueba

\[
 \boxed{
 \{K_\varphi:0\leq\varphi\leq1,\ \varphi\text{ par}\}
 =\mathcal K.}                                         \tag{10}
\]

El intervalo de orden \(0\leq\varphi\leq1\) tiene como puntos extremos
las funciones características. Por (10), también son los puntos extremos
de \(\mathcal K\). En particular el selector óptimo

\[
 \varphi_X=\mathbf1_{\{u>u_X\}}                        \tag{11}
\]

no desaparece bajo la traducción PD. Un minimax que solo reemplace (6) por
(2) vuelve exactamente a (6).

## 2. Forma de Stieltjes que conserva todas las torres

Ponga

\[
 h_x(t)=x^{-1/2}\cos(t\log x)-x^{-1}.                  \tag{12}
\]

La ecuación (10) de 104_89 se escribe, sin separar torres,

\[
 \boxed{u_X(t)=\int_{1^-}^{X}h_x(t)\,
              d\{J(x)-\mathrm{Li}(x)\}.}        \tag{13}
\]

En efecto, el átomo en \(p^a\) tiene masa
\(1/a=\Lambda(p^a)/\log(p^a)\). La parte continua de (13), con
\(x=e^y\), es

\[
 -\int_1^Xh_x(t){dx\over\log x}
 =\int_0^{\log X}{1-e^{y/2}\cos(ty)\over y}\,dy.      \tag{14}
\]

La singularidad en \(x=1\) es removible porque
\(h_x(t)=O(\log x)\). Como (13) es finita, Fubini es legítimo. Si
\(c=K_\varphi(0)=\int\varphi\,d\nu\), entonces

\[
 \int\varphi h_x\,d\nu
 =x^{-1/2}K_\varphi(\log x)-{c\over x}.                \tag{15}
\]

Las ecuaciones (13)--(15) prueban (3).

Para registrar el dual completo, sea

\[
 \mathcal U(K)=\int\varphi_K(t)u(t)\,d\nu(t),          \tag{16}
\]

donde \(\varphi_K\) es la densidad única de (10). Entonces

\[
 \boxed{
 I_X=\sup_{K\in\mathcal K}
 \left[
  \mathcal U(K)-
  \int_{1^-}^{X}
  \{x^{-1/2}K(\log x)-K(0)/x\}\,
  d(J-\mathrm{Li})(x)
 \right].}                                             \tag{17}
\]

La positividad definida restringe conjuntamente todos los valores
\(K(\log p^a)\), pero (10) muestra que no impone nada que no estuviera ya
en el selector original. Probar que (17) tiende a cero sigue siendo la
desigualdad aritmética unilateral de 104_89.

La renovación exacta tampoco produce una reserva. En coordenada
logarítmica, \(L*N=yN\), o equivalentemente
\(\Lambda*1=\log\). Resolverla para \(L\) da de nuevo
\(L=\mu*\log\); exponenciar \(dJ\) reconstruye el mismo producto Euler.
104_80, ecuaciones (10)--(13), demuestra que esta inversión vuelve al
mismo germ meromorfo y conserva cada polo procedente de un cero. Por eso
no se reabre aquí como mecanismo distinto.

## 3. Contramodelo en una torre prima arbitrariamente remota

Sea \(P>6\) un primo ordinario y defina

\[
 Z_-(T)={(1-3T)(1-2T)\over(1-T)(1-6T)},\qquad
 T_P(s)=\sqrt{P/6}\,P^{-s},                             \tag{18}
\]

\[
 W_P(s)=Z_-(T_P(s)),\qquad Z_P(s)=\zeta(s)W_P(s).       \tag{19}
\]

Para

\[
 A_a=6^a+1-3^a-2^a=(3^a-1)(2^a-1)>0                  \tag{20}
\]

se tiene, donde converge absolutamente,

\[
 \log W_P(s)=\sum_{a\geq1}{A_a\over a}
                    (P/6)^{a/2}P^{-as}.                \tag{21}
\]

Por tanto

\[
 -{W_P'\over W_P}(s)
 =\sum_{a\geq1}{b_P(P^a)\over P^{as}},                \tag{22}
\]

\[
 \boxed{
 b_P(P^a)=\log P\,(P/6)^{a/2}A_a>0.}                  \tag{23}
\]

El canal Euler de \(Z_P\) tiene pesos

\[
 \Lambda_P(n)=
 \begin{cases}
  \Lambda(n)+b_P(n),&n=P^a,\\
  \Lambda(n),&n\ne P^a.
 \end{cases}                                           \tag{24}
\]

Si \(P>M\), entonces (24) coincide con la función de Mangoldt ordinaria
para todo \(n\leq M\), y coincide en todas las torres salvo una.

### 3.1. PNT continuo

Ponga

\[
 \sigma_P={\log\sqrt{6P}\over\log P}
 ={1\over2}+{\log6\over2\log P}<1.                    \tag{25}
\]

Como \(A_a\leq2\,6^a\), una suma geométrica da

\[
 \sum_{P^a\leq x}b_P(P^a)=O_P(x^{\sigma_P}).          \tag{26}
\]

En consecuencia

\[
 \psi_P(x)=x+O\{xe^{-\eta(\log x)}+x^{\sigma_P}\}
            =x+O_P\{xe^{-\eta(\log x)}\},             \tag{27}
\]

porque \(\sigma_P<1\) y \(\eta(y)=o(y)\). El umbral y la constante de
(27) pueden depender de \(P\); el exponente VK no cambia.

### 3.2. Completamiento y cero exterior

Defina

\[
 r_P(s)={1\over2}+{\log P\over\log6}
                   \left(s-{1\over2}\right),          \tag{28}
\]

de modo que \(T_P(s)=6^{-r_P(s)}\) y
\(r_P(1-s)=1-r_P(s)\). La función

\[
 \Xi_-(r)=6^r-5+6^{1-r}                               \tag{29}
\]

es entera y satisface \(\Xi_-(1-r)=\Xi_-(r)\). Por ello

\[
 \mathcal X_P(s)=\xi(s)\Xi_-(r_P(s))                  \tag{30}
\]

es entera y simétrica bajo \(s\mapsto1-s\). Es realmente un
completamiento de (19): si \(q=6^r\), entonces

\[
 \Xi_-(r)={(q-1)(q-6)\over q}\,Z_-(q^{-1}).            \tag{30a}
\]

El factor delante de \(Z_-\) cancela precisamente sus polos adicionales.
Los ceros añadidos del completamiento son

\[
 {1\over2}\pm{\log(3/2)\over2\log P}
       +{2\pi ik\over\log P},\qquad k\in\mathbb Z.     \tag{31}
\]

En particular

\[
 \beta_P={1\over2}+{\log(3/2)\over2\log P}>{1\over2}. \tag{32}
\]

El término de Jensen de ese cero real es

\[
 \log{\beta_P\over1-\beta_P}
 =\log {\log P+\log(3/2)\over
              \log P-\log(3/2)}=D_P>0,                \tag{33}
\]

que prueba (5). Los demás ceros derechos solo añaden términos no
negativos.

Además, al hacer \(P\to\infty\), se tiene

\[
 D_P\sim{2\log(3/2)\over\log P},\qquad
 \beta_P\downarrow{1\over2},                          \tag{34}
\]

y \(W_P\to1\) localmente uniformemente en cada
\(\Re s\geq1/2+\delta\). Por tanto los contramodelos pueden coincidir en
prefijos cada vez mayores y ser localmente invisibles a distancia fija de
la frontera, aunque cada uno conserve un defecto positivo.

## 4. Alcance exacto del falsificador

El sistema (19) no conserva todos los datos de la zeta:

* altera la torre \(P^a\) mediante (23);
* \(W_P\) posee polos Euler adicionales, que son cancelados por el factor
  explícito que relaciona \(W_P\) con (29);
* (30) contiene un factor simétrico adicional y no es el completamiento
  literal de Riemann.

Por la unicidad de 104_88, ningún contramodelo distinto puede conservar
simultáneamente todos los valores \(\Lambda(n)\) y la misma normalización:
eso fijaría a \(\zeta\). Así el alcance correcto es

\[
 \begin{gathered}
 \text{prefijos exactos arbitrariamente largos + PD + positividad +}\\
 \text{soporte ordinario + PNT/VK + FE amplia}
 \not\Longrightarrow \text{cota unilateral},          \tag{35}\\
 \text{pero (35) no descarta una desigualdad que use literalmente todas}\\
 \text{las torres ordinarias y el completamiento exacto de Riemann.}
 \end{gathered}
\]

La consecuencia operativa es doble:

1. la coordenada PD/minimax de (17) no reduce el target;
2. ningún certificado por compactación de prefijos puede cerrarlo con
   constantes uniformes obtenidas solo de los datos cualitativos de
   (35).

El frente restante sigue siendo una cota global específica de la
discrepancia regularizada \(dJ-d\mathrm{Li}\,\) de los enteros
ordinarios.

## 5. Reproducción

Desde el directorio tools:

    python3 dual_pd_remote_tower_gate_check.py

El programa verifica la identidad dual finita, la positividad numérica de
las dos matrices PD para un selector de prueba, las identidades algebraicas
(20)--(23), la simetría (28)--(31), la coincidencia en prefijos y el defecto
(33). Las afirmaciones para todo \(P\), todo prefijo y todo núcleo están
probadas arriba; el cálculo es un control de implementación, no su
sustituto.
