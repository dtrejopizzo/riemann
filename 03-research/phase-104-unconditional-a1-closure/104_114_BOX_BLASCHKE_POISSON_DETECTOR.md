# 104_114 — Detector Blaschke--Poisson de la caja profunda

**Pregunta.** Después de `104_112`--`104_113`, el frente es excluir la caja

\[
 0<\gamma\lesssim T,\qquad
 \beta-\frac12\gtrsim{\gamma^2\over T^2}.                \tag{1}
\]

¿Hay una forma local, en el disco de Cayley, que detecte exactamente esos
ceros y pueda transformarse en una desigualdad nueva para los primos
ordinarios?

**Resultado.** Hay un detector exacto, pero no es una fuente nueva de
signo. En la coordenada

\[
 s={1\over1-z},\qquad E(z)=(s-1)\zeta(s),
\]

los ceros con \(\Re\rho>1/2\) son los ceros interiores

\[
 a_\rho={\rho-1\over\rho}=e^{-a_\rho^{\rm rad}+i\theta_\rho}.
\]

La caja (1) es equivalente a una familia de cajas de Carleson

\[
 1-|a_\rho|\gtrsim T^{-2},\qquad |\theta_\rho|\gtrsim T^{-1}
 \quad(\hbox{con } |\theta_\rho|\asymp \gamma^{-1}).      \tag{2}
\]

Para \(z\in\mathbb D\), la factorización de `104_111`
\[
 E(z)=B(z)O(z)
\]
da el déficit exacto

\[
 \boxed{
 \mathcal J(z):=
 P_z(\log|E^*|)-\log|E(z)|
 =
 \sum_{\Re\rho>1/2} m_\rho
 \log\left|
 {1-\overline{a_\rho}z\over z-a_\rho}
 \right|.
 }                                                       \tag{3}
\]

Aquí \(P_z\) es la integral de Poisson en el borde. Por tanto
\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 \mathcal J(z)\equiv0\quad(z\in\mathbb D).              \tag{4}
\]

Además, un cero en la caja (1) produce un pico positivo de tamaño
\(\gg1\) en \(\mathcal J(z)\) para un \(z\) de la misma caja hiperbólica.
Así, excluir \(R_T\) equivale a probar
\[
 \sup_{z\in\mathcal C_T}\mathcal J(z)\longrightarrow0
\]
en una familia cofinal de cajas \(\mathcal C_T\).

Este detector es útil como coordenada exacta del obstáculo, pero no prueba
RH. Toda prueba de \(\mathcal J=0\) es exactamente la eliminación del
factor de Blaschke interior de `104_111`. La frontera \(P_z(\log|E^*|)\)
vive en la recta crítica; convertirla en una desigualdad prima ordinaria
vuelve a la fórmula explícita de Weil. Por tanto la vía
Poisson--Jensen/outer-function no es una fuente independiente de signo.

---

## 1. Geometría de la caja en el disco

Para \(\rho=\beta+i\gamma\), \(\beta>1/2\), ponga

\[
 a_\rho^{\rm rad}
 ={1\over2}\log{|\rho|^2\over|\rho-1|^2}.
\]

Entonces

\[
 |a_\rho|=e^{-a_\rho^{\rm rad}},\qquad
 a_\rho^{\rm rad}\asymp{\beta-\frac12\over\gamma^2}.
\]

La fase satisface

\[
 \theta_\rho=\arg{\,\rho-1\over\rho}
 =\arg\left(1-{1\over\rho}\right),
 \qquad |\theta_\rho|\asymp{1\over\gamma}
\]

para \(\gamma\ge2\). Por tanto (1) se traduce en

\[
 1-|a_\rho|\asymp a_\rho^{\rm rad}\gtrsim T^{-2},
 \qquad |\theta_\rho|\gtrsim T^{-1}.                    \tag{5}
\]

El borde radial \(T^{-2}\) coincide con la escala del detector Deep:
un modo con \(1-|a|\asymp T^{-2}\) tiene crecimiento
\(\exp(n/T^2)\), y en grados \(n\asymp T^4\) alcanza
\(\exp(T^2)=e^{\sqrt X}\).

## 2. Jensen local exacto

La factorización de `104_111` da \(E=BO\), sin factor interior singular.
Para el producto de Blaschke normalizado

\[
 b_a(z)={|a|\over a}{a-z\over1-\bar a z},
 \qquad b_a(0)=|a|,
\]

se tiene
\[
 \log|B(z)|
 =\sum_{\Re\rho>1/2}m_\rho
 \log\left|{a_\rho-z\over1-\overline{a_\rho}z}\right|.
\]

Como \(O\) es exterior,

\[
 \log|O(z)|=P_z(\log|E^*|).
\]

Restando \(\log|E(z)|=\log|B(z)|+\log|O(z)|\), resulta (3). La cantidad
\(\mathcal J(z)\) es no negativa y se anula en un punto si y solo si no
hay ceros interiores que contribuyan al potencial visto desde ese punto.
Se anula identicamente si y solo si \(B\equiv1\).

## 3. Un cero de la caja produce un pico

Sea \(a\in\mathbb D\) un cero interior. Tome \(z\) en el mismo radio y con
\[
 1-|z|=\kappa(1-|a|),\qquad 0<\kappa<1,\qquad \arg z=\arg a.
\]

Entonces
\[
 \left|{1-\bar a z\over z-a}\right|
 ={1-|a||z|\over ||z|-|a||}
 ={(1-|a|)+|a|(1-|z|)\over |(1-|a|)-(1-|z|)|}.
\]

Si \(1-|z|=\kappa(1-|a|)\), el cociente tiende a
\[
 {1+\kappa\over1-\kappa}
\]
cuando \(|a|\to1\). Así un solo cero de la caja aporta al menos
\[
 \log{1+\kappa\over1-\kappa}+o(1)                       \tag{6}
\]
a \(\mathcal J(z)\), con multiplicidad. La detección es local y de tamaño
constante; no se pierde en promedios.

## 4. Por qué no es un mecanismo nuevo de cierre

La identidad (3) prueba que el detector correcto existe y es positivo. El
problema es que su positividad es la del factor de Blaschke, no una
desigualdad aritmética que lo anule. Para concluir RH habría que demostrar

\[
 P_z(\log|E^*|)\le \log|E(z)|
 \qquad(z\in\mathbb D),                                  \tag{7}
\]

porque la desigualdad opuesta es la subarmonicidad automática de
\(\log|E|\). Pero (7) es exactamente decir que no hay factor interior.

En términos de primos, \(\log E(z)\) en \(\Re s>1\) tiene serie de Euler,
pero \(P_z(\log|E^*|)\) vive en la frontera \(\Re s=1/2\). Transportar
esa frontera a los primos requiere la fórmula explícita de Weil con un
test adaptado al núcleo de Poisson. La contribución de un cero interior es
precisamente el término positivo de (3). Por tanto la desigualdad que
anularía \(\mathcal J\) es Weil-positivity/RH en esta familia de tests, no
una consecuencia de PNT, densidad, o de la factorización exterior.

## 5. Consecuencia

La caja profunda puede ser atacada en dos coordenadas equivalentes:

1. la coordenada Li/Deep de `104_75`--`104_113`, donde un cero en la caja
   produce excursiones negativas profundas;
2. la coordenada Blaschke--Poisson (3), donde el mismo cero produce un pico
   positivo local de Green.

Ambas aíslan el mismo factor interior. Ninguna reduce la última tarea. Un
sucesor real tendría que probar una desigualdad prima ordinaria que fuerce
\(\mathcal J(z)=0\) en cajas cofinales y que falle para los modelos Euler
exteriores. En ausencia de esa desigualdad, el detector es una coordenada
limpia del obstáculo, no una prueba de RH.
