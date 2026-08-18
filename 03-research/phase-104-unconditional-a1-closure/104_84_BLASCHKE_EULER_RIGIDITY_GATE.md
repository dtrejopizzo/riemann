# 104_84 — Factor interior de Blaschke y rigidez de las identidades Euler locales

**Resultado.** El observable profundo de `104_75` admite una frontera
canónica en el disco. Defina

\[
 s(z)={1\over1-z},\qquad
 E(z)=(s(z)-1)\zeta(s(z)),\qquad E(0)=1.                 \tag{1}
\]

Los ceros de \(E\) en \(\mathbb D\) son exactamente

\[
 w_\rho={\rho-1\over\rho},\qquad \Re\rho>{1\over2}.    \tag{2}
\]

Forman una sucesión de Blaschke. Si \(B\) es su producto interior, entonces

\[
 \boxed{
 {1\over2\pi}\int_{-\infty}^{\infty}
 {\log|\zeta(\tfrac12+it)|\over t^2+\tfrac14}\,dt
 =-\log B(0)
 =\sum_{\Re\rho>1/2}m_\rho
       \log{|\rho|\over|\rho-1|}\ge0.}                 \tag{3}
\]

El límite profundo, la ausencia de polos interiores de `104_80`,
\(B\equiv1\), la igualdad a cero en (3) y RH son el mismo enunciado. La
ecuación (3) es el criterio de Balazard--Saias--Yor escrito en la coordenada
de esta fase.

Hay además una rigidez algebraica. Toda modificación por factores Euler
locales analíticos cuyo primer coeficiente primo sea constante se factoriza
como una potencia de \(\zeta\) por un factor holomorfo y no nulo en
\(\Re s>1/2\). Por ello Möbius, *squarefree*, \(\zeta(2s)\) y cualquier
identidad Euler local finita tienen una dicotomía exacta: conservan el
factor interior con la misma multiplicidad, o cancelan también todo el
observable. No pueden demostrar (3) con igualdad.

Esto no prueba Deep-\(\Lambda\), A1 ni RH. Identifica con precisión el
único sucesor no descartado: una desigualdad genuinamente no local entre
primos que pruebe \(B(0)=1\). Una nueva factorización local, una cota de
módulo fronterizo o una identidad de convolución no bastan.

---

## 1. Geometría del disco

El mapa \(s=(1-z)^{-1}\) envía \(\mathbb D\) sobre
\(\Re s>1/2\), y

\[
 |w_\rho|<1
 \quad\Longleftrightarrow\quad
 |\rho-1|<|\rho|
 \quad\Longleftrightarrow\quad
 \Re\rho>{1\over2}.                                    \tag{4}
\]

Además,

\[
 1-|w_\rho|^2={2\Re\rho-1\over|\rho|^2}
 \le {1\over|\rho|^2}.                                 \tag{5}
\]

Riemann--von Mangoldt implica
\(\sum_\rho |\rho|^{-2}<\infty\). Por (5), los ceros interiores
satisfacen

\[
 \sum_{\Re\rho>1/2}m_\rho(1-|w_\rho|)<\infty.          \tag{6}
\]

Su producto de Blaschke converge:

\[
 B(z)=\prod_{\Re\rho>1/2}
 \left{
 { |w_\rho|\over w_\rho}
 {w_\rho-z\over1-\overline{w_\rho}z}
 \right}^{m_\rho}.                                    \tag{7}
\]

La función de (1) es de clase Smirnov en el disco: tras cancelar el polo
de \(\zeta\) en \(s=1\), las cotas de crecimiento polinomial de
\((s-1)\zeta(s)\) en \(\Re s\ge1/2\), transportadas por el mapa conforme,
dan integrabilidad de \(\log^+|E|\). Continúa a través de todo arco de
\(\partial\mathbb D\) salvo \(z=1\); allí tiene crecimiento polinomial.
Por tanto no aparece un factor interior singular y la factorización
canónica tiene la forma

\[
 E(z)=B(z)O(z),                                         \tag{8}
\]

con \(O\) exterior.

## 2. Identidad de Jensen

En la frontera, fuera de \(z=1\), escriba \(z=e^{i\theta}\). Entonces

\[
 s(e^{i\theta})={1\over2}+{i\over2}\cot{\theta\over2}
 ={1\over2}+it,\qquad
 |d\theta|={dt\over t^2+1/4}.                           \tag{9}
\]

La fórmula de Jensen radial, seguida del límite \(r\uparrow1\), da

\[
 {1\over2\pi}\int_0^{2\pi}\log|E(e^{i\theta})|\,d\theta
 =\sum_{\Re\rho>1/2}m_\rho\log{1\over|w_\rho|},        \tag{10}
\]

porque \(E(0)=1\). En \(|z|=1\),

\[
 \log|E(z)|=\log|\zeta(\tfrac12+it)|+log|s-1|.         \tag{11}
\]

El segundo término tiene media cero. En efecto,
\(s-1=z/(1-z)\), de modo que

\[
 {1\over2\pi}\int_0^{2\pi}\log|s-1|\,d\theta
 =-{1\over2\pi}\int_0^{2\pi}\log|1-e^{i\theta}|\,d\theta
 =0.                                                     \tag{12}
\]

Las ecuaciones (9)--(12) prueban (3). Cada sumando de su lado derecho es
estrictamente positivo. Usando la simetría funcional
\(\rho\mapsto1-\overline\rho\), se obtiene

\[
 \text{lado derecho de (3)}=0
 \quad\Longleftrightarrow\quad \mathrm{RH}.            \tag{13}
\]

El módulo fronterizo no ve el factor interior punto a punto:
\(|B(e^{i\theta})|=1\) casi en todas partes. Solo la normalización
interior \(B(0)\), recuperada por Jensen, registra los ceros derechos.

## 3. Qué fijan exactamente los primos ordinarios

El semiplano Euler \(\Re s>1\) corresponde al horodisco

\[
 \left|z-{1\over2}\right|<{1\over2}.                   \tag{14}
\]

Allí,

\[
 E(z)={z\over1-z}
 \prod_p\left(1-p^{-1/(1-z)}\right)^{-1}.              \tag{15}
\]

Los valores exactos de (15) en cualquier abierto, o incluso en un
intervalo real con punto de acumulación, fijan \(E\) en todo su dominio por
el teorema de identidad. En particular fijan \(B\) y \(O\). Ésta es una
unicidad de la función, no una prueba de que \(B=1\): evaluar o continuar
la función determinada no suministra el signo opuesto que anule la suma
positiva de (3).

La ecuación funcional solo empareja el cero interior \(w_\rho\) con el
exterior \(1/\overline{w_\rho}\). No obliga a que ambos estén en
\(|z|=1\).

## 4. Lema de rigidez Euler local

Sea \(\phi\) analítica y no nula cerca de cero, con

\[
 \phi(0)=1,\qquad \log\phi(u)=cu+O(u^2).                \tag{16}
\]

Para \(\Re s>1\), defina

\[
 F_\phi(s)=\prod_p\phi(p^{-s}).                         \tag{17}
\]

Entonces, en ese semiplano,

\[
 F_\phi(s)=\zeta(s)^cH_\phi(s),                        \tag{18}
\]

donde

\[
 \log H_\phi(s)=
 \sum_p\left\{\log\phi(p^{-s})+c\log(1-p^{-s})\right\}.
                                                               \tag{19}
\]

Cada sumando de (19) es \(O(p^{-2\Re s})\), localmente uniforme. La serie
converge normalmente en \(\Re s>1/2\), de modo que \(H_\phi\) es
holomorfa y no nula allí. En términos de derivadas logarítmicas,

\[
 -{F_\phi'\over F_\phi}
 =-c{\zeta'\over\zeta}-{H_\phi'\over H_\phi}.         \tag{20}
\]

Si \(\rho\) es un cero derecho de multiplicidad \(m_\rho\), el primer
término de (20) tiene residuo \(-cm_\rho\) y el segundo es holomorfo.
Por tanto:

* si \(c\ne0\), la transformación conserva el polo que genera
  Deep-\(\Lambda\), solo escalado por \(c\);
* si \(c=0\), el producto es no nulo en \(\Re s>1/2\), pero ha eliminado
  también toda información sobre los ceros de \(\zeta\).

Esto incluye las coordenadas

\[
 {\zeta(s)\over\zeta(2s)},\qquad {1\over\zeta(s)},
 \qquad {\zeta(s)^2\over\zeta(2s)},                    \tag{21}
\]

y las identidades Euler locales finitas obtenidas de Möbius o de la
restricción *squarefree*. Como \(\Re(2\rho)>1\), una corrección construida
con \(\zeta(2s)\) es holomorfa y no nula en \(\rho\); no puede cancelar
selectivamente el cero.

La ecuación funcional tampoco altera la dicotomía:

\[
 \zeta(1-s)=\chi(s)^{-1}\zeta(s).                       \tag{22}
\]

Así, \(\zeta(s)^a\zeta(1-s)^b\) conserva el cero con multiplicidad
\(a+b\) si \(a+b\ne0\); si \(a+b=0\), queda únicamente el factor Gamma
explícito \(\chi^{-b}\), que no contiene la aritmética buscada.

## 5. Falsificador de las propiedades cualitativas

La exactitud de (15) no admite un contramodelo distinto: conservar sus
valores en un abierto obliga a coincidir con \(E\). Pero las propiedades
cualitativas que suelen sustituir esa exactitud sí admiten un factor
interior arbitrario.

Para \(0<\delta<1/2\), \(\gamma>0\), ponga

\[
 X_{\delta,\gamma}(s)=C
 \left((s-\tfrac12-i\gamma)^2-\delta^2\right)
 \left((s-\tfrac12+i\gamma)^2-\delta^2\right),          \tag{23}
\]

con \(C>0\) elegido de modo que \(X_{\delta,\gamma}(1)=1\). Entonces

\[
 X_{\delta,\gamma}(s)=X_{\delta,\gamma}(1-s),          \tag{24}
\]

es real sobre el eje real, positivo y no nulo para \(s>1\), y añade el
cuarteto

\[
 {1\over2}\pm\delta\pm i\gamma.                        \tag{25}
\]

Por tanto \(\xi(s)X_{\delta,\gamma}(s)\) conserva ecuación funcional,
realidad, orden finito, normalización y positividad en el rayo Euler, pero
tiene \(B\ne1\). No conserva los valores Euler ordinarios exactos; hacerlo
es imposible por unicidad analítica.

## 6. Decisión

```text
probado:
  Deep-Lambda = ausencia del factor Blaschke interior;
  identidad BSY/Jensen exacta (3);
  el producto Euler exacto determina la función, pero no da B(0)=1;
  toda identidad Euler local conserva el polo o borra el observable;
  FE y el módulo fronterizo no detectan por sí solos B.

descartado:
  otra factorización local Möbius/squarefree/zeta(2s)
  + ecuación funcional o módulo fronterizo
  => Deep-Lambda.

único sucesor no descartado por este gate:
  una desigualdad no local, específica de la colocación conjunta de los
  primos ordinarios, que pruebe B(0)=1.

no probado:
  B(0)=1, Deep-Lambda, A1 o RH.
```
