# 104_107 — Bloques de Fejér y gate exacto del transporte de fase

**Pregunta.** ¿La relajación por bloques de `104_67`, aplicada antes de
transportar la cota de fase de `104_41` desde \(a\geq4\) hasta \(a=1\),
reduce el costo lo suficiente para controlar el defecto de residuos de
`104_33`?

**Resultado.** El suavizado correcto sí produce una ganancia fuerte y
uniforme en el semiplano Euler. Sobre \(2L-1\) grados consecutivos, un
promedio triangular centrado en \(N\) satisface

\[
 \boxed{
 |\mathcal B^{\triangle}_{N,L,a}|
 \le {3\pi\over2}{N\over L}
       +2\left(1-{1\over L^2}\right),\qquad a\geq4.}       \tag{1}
\]

En particular, para \(N\asymp L\), el lado derecho es una constante, en
vez de la cota \(3n\) grado a grado. No se pierde ningún borde en (1).

Sin embargo, el filtro evaluado en un residuo interior es exactamente

\[
 T_{N,L}(w)+T_{N,L}(w^{-1})-2,
 \qquad
 T_{N,L}(w)=w^{N-L+1}
 \left({1-w^L\over L(1-w)}\right)^2.                       \tag{2}
\]

Para \(|w|<1\), el segundo sumando de (2) tiene tamaño

\[
 { |1-w^L|^2\over L^2|1-w|^2}\,|w|^{-N-L+1},              \tag{3}
\]

y nunca se anula: los únicos ceros de \(1-w^L\) están sobre
\(|w|=1\). Así el promedio que reduce la variación de frontera a
\(O(N/L+1)\) conserva, e incluso localiza en el extremo alto, la carga
exponencial de todo cero con parte real \(>1/2\).

El cuarteto racional \(w=i/2\) da ambos signos con tamaño
\(\asymp2^{N+L}/L^2\), mientras deja idéntica la fase sobre la línea
crítica. Por tanto queda refutado el transporte unilateral del promedio
de bloques usando solo la cota de fase y la homotopía. La desigualdad
correspondiente para los pesos literales \(\Lambda(m)\) sigue siendo un
teorema aritmético nuevo de fuerza RH; este documento no la prueba, ni
prueba A1 o RH.

---

## 1. Dos promedios consecutivos y por qué se usa el triangular

Sea, como en `104_41`,

\[
 W_n(t)=2-2\cos(n\theta(t)),\qquad
 {-1/2+it\over1/2+it}=e^{i\theta(t)},\qquad t>0,           \tag{4}
\]

donde \(\theta\) decrece de \(\pi\) a \(0\). Para el promedio uniforme
de \(L\) grados \(N,\ldots,N+L-1\),

\[
 W^{\rm unif}_{N,L}(\theta)
 =2-{2\over L}{\sin(L\theta/2)\over\sin(\theta/2)}
 \cos\left({(2N+L-1)\theta\over2}\right).                 \tag{5}
\]

Su variación exacta es

\[
 \operatorname {TV}_{\mathbb R}(W^{\rm unif}_{N,L})
 ={4\over L}\int_0^\pi
 \left|\sum_{n=N}^{N+L-1}n\sin(n\theta)\right|d\theta.   \tag{6}
\]

Ortogonalidad y Cauchy--Schwarz dan

\[
 \operatorname {TV}_{\mathbb R}(W^{\rm unif}_{N,L})
 \le {2\sqrt2\pi\over L}
       \left(\sum_{n=N}^{N+L-1}n^2\right)^{1/2}.           \tag{7}
\]

Esto mejora \(O(N)\) a \(O(N/\sqrt L)\), pero no es la escala óptima
para un bloque largo.

Para obtenerla, suponga \(N\geq L\geq1\) y ponga

\[
 \alpha_{L,k}:={L-|k|\over L^2},\qquad |k|<L,
 \qquad \sum_{|k|<L}\alpha_{L,k}=1.                       \tag{8}
\]

Defina

\[
 \begin{aligned}
 W^\triangle_{N,L}(t)
   &:=\sum_{|k|<L}\alpha_{L,k}W_{N+k}(t),\\
 \mathcal B^\triangle_{N,L,a}
   &:=\sum_{|k|<L}\alpha_{L,k}\mathcal B_{N+k,a}.
 \end{aligned}                                             \tag{9}
\]

Estos son promedios genuinos de los grados consecutivos
\(N-L+1,\ldots,N+L-1\); no aparece ningún coeficiente de signo
negativo. La transformada exacta de (8) es

\[
 H_L(\theta):=\sum_{|k|<L}\alpha_{L,k}e^{ik\theta}
 =\left({\sin(L\theta/2)\over L\sin(\theta/2)}\right)^2.
                                                               \tag{10}
\]

Por tanto

\[
 \boxed{
 W^\triangle_{N,L}(\theta)
 =2-2H_L(\theta)\cos(N\theta).}                           \tag{11}
\]

En particular \(W^\triangle_{N,L}\geq0\), por ser un promedio de los
\(W_n\), y \(W^\triangle_{N,L}(t)\to0\) cuando
\(|t|\to\infty\). En el otro extremo,

\[
 W^\triangle_{N,L}(0)
 =\begin{cases}
 2,&L\text{ par},\\
 2-2(-1)^N/L^2,&L\text{ impar}.
 \end{cases}                                               \tag{12}
\]

La ecuación (12) se registra para evitar desechar el borde \(t=0\) al
partir la integral en dos semirrectas. En la integral sobre toda
\(\mathbb R\) no es un borde; los únicos bordes de la integración por
partes están en \(\pm\infty\), donde (11) se anula.

---

## 2. Variación total del bloque de Fejér

De (11) y de la monotonía de \(\theta(t)\) en cada semirrecta se obtiene
la identidad exacta

\[
 \boxed{
 \operatorname {TV}_{\mathbb R}(W^\triangle_{N,L})
 =4\int_0^\pi
   \left|{d\over d\theta}{H_L(\theta)\cos(N\theta)\}
   \right|d\theta.}                                      \tag{13}
\]

Además,

\[
 \int_0^\pi H_L(\theta)d\theta={\pi\over L}.             \tag{14}
\]

Necesitamos también una cota uniforme, con constante explícita, para la
variación de \(H_L\):

\[
 \boxed{
 \operatorname {TV}_{[0,\pi]}(H_L)
 \le {4\over3}\left(1-{1\over L^2}\right).}              \tag{15}
\]

Aquí están todos los lóbulos. Para probar (15), escriba
\(x=\theta/2\). Entre dos ceros consecutivos de
\(\sin(Lx)/\sin x=U_{L-1}(\cos x)\) hay exactamente un punto crítico:
Rolle da uno y el grado de \(U'_{L-1}\) impide que haya más. El lóbulo
que empieza en \(x=j\pi/L\), \(j\geq1\), tiene altura a lo sumo

\[
 {1\over L^2\sin^2(j\pi/L)}.                              \tag{16}
\]

Para \(L\) par, la identidad

\[
 \sum_{j=1}^{L/2-1}\csc^2(j\pi/L)={L^2-4\over6}           \tag{17}
\]

da (15), contando una vez la caída del lóbulo principal y dos veces cada
lóbulo interior. Para \(L\) impar se usa

\[
 \sum_{j=1}^{(L-1)/2}\csc^2(j\pi/L)={L^2-1\over6},        \tag{18}
\]

se retira el último sumando, que es al menos \(1\), y se añade el borde
\(H_L(\pi)=1/L^2\). El mismo lado derecho de (15) resulta. Para \(L=1\),
ambos lados valen cero.

Aplicando la regla del producto en (13), y luego (14)--(15),

\[
 \boxed{
 \operatorname {TV}_{\mathbb R}(W^\triangle_{N,L})
 \le4\left\{{\pi N\over L}
       +{4\over3}\left(1-{1\over L^2}\right)\right\}.}  \tag{19}
\]

---

## 3. Cota unilateral en el semiplano Euler

La identidad de fase de `104_41` es lineal en \(W_n\). Por (9),

\[
 \mathcal B^\triangle_{N,L,a}
 =-{1\over2\pi}\int_{\mathbb R}
 W^\triangle_{N,L}(t)d\vartheta_a(t).                     \tag{20}
\]

Para \(a\geq4\), `104_41` prueba
\(|\vartheta_a(t)|<3\pi/4\). Integrando (20) por partes sobre toda la
recta, los bordes de \(\pm\infty\) son cero por (11). Las posibles
variaciones en \(t=0\) desde las dos semirrectas se cancelan porque tanto
\(W^\triangle_{N,L}\) como la rama conjugada de la fase son continuas
allí. De (19),

\[
 \begin{aligned}
 |\mathcal B^\triangle_{N,L,a}|
 &\le {1\over2\pi}{3\pi\over4}
       \operatorname {TV}_{\mathbb R}(W^\triangle_{N,L})\\
 &\le {3\pi\over2}{N\over L}
       +2\left(1-{1\over L^2}\right),
 \end{aligned}                                             \tag{21}
\]

que prueba (1). En particular, para \(N=2L+O(1)\), el bloque completo
está acotado por \(3\pi+2+o(1)\). Esta es una desigualdad bilateral y,
por tanto, contiene las dos versiones unilaterales. No se usó

\[
 \left|\int gh\right|\leq\int|g||h|;
\]

solo la fase completa prima--polo y la variación del test combinado.

Hay una distinción lógica vinculante. La cota (21) controla la **media
firmada** de los \(2L-1\) grados; no afirma que esos grados formen un
bloque bueno en el sentido coeficiente a coeficiente de `104_67`. Valores
positivos y negativos grandes pueden cancelarse dentro de la media. Para
usar directamente el criterio de `104_67` haría falta controlar el máximo,
la parte positiva o cada grado del bloque. Ninguna de esas operaciones es
lineal en \(W_n\), y (21) no las estima.

---

## 4. Transporte exacto de los residuos del bloque

Para un cero \(\rho\) con \(\Re\rho>1/2\), ponga

\[
 w=1-{1\over\rho},\qquad |w|<1.                            \tag{22}
\]

La identidad de `104_33`, sin omitir factores, es

\[
 {\mathcal F_n(w)\over\rho(\rho-1)}=w^n+w^{-n}-2.          \tag{23}
\]

La transformada algebraica de los pesos (8) vale para todo \(w\ne0,1\):

\[
 \begin{aligned}
 T_{N,L}(w)
 &:=\sum_{|k|<L}\alpha_{L,k}w^{N+k}\\
 &=w^{N-L+1}\left({1-w^L\over L(1-w)}\right)^2.           \tag{24}
 \end{aligned}
\]

Promediando (23) se obtiene exactamente (2). Por consiguiente, la
versión en bloques de (22) de `104_41` es

\[
 \boxed{
 B^\triangle_{N,L}=\mathcal P^\triangle_{N,L}
 +\sum_{\Re\rho>1/2}m_\rho
 \{T_{N,L}(w_\rho)+T_{N,L}(w_\rho^{-1})-2\}.}             \tag{25}
\]

La suma se entiende con las mismas órbitas funcionales y el mismo límite
simétrico que en `104_33`; el promedio es finito, así que puede
intercambiarse con cada suma parcial. No aparece término de borde nuevo.

Usando (24) dos veces,

\[
 \begin{aligned}
 T_{N,L}(w)+T_{N,L}(w^{-1})
  =\left({1-w^L\over L(1-w)}\right)^2
   \{w^{N-L+1}+w^{-N-L+1}\}.                              \tag{26}
\end{aligned}
\]

Si \(|w|<1\), el coeficiente de \(w^{-N-L+1}\) en (26) no es cero, pues
\(w^L\ne1\). Su módulo es exactamente (3). Así la reducción de variación
de (21) no produce reducción exponencial en los residuos: el extremo
superior \(N+L-1\), cuyo peso es solo \(L^{-2}\), domina una evaluación
fuera del círculo.

---

## 5. Falsificador racional de ambos signos

Tome

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5}.         \tag{27}
\]

Complete el cuarteto funcional como en `104_41`. Su polinomio es
estrictamente positivo sobre \(\Re s=1/2\), de modo que multiplicar el
completamiento por cualquier potencia del cuarteto no cambia la fase en
la línea crítica.

Sea \(4\mid L\) y defina

\[
 c_L:={(1-2^{-L})^2\over L^2},\qquad
 \left({1-w^L\over L(1-w)}\right)^2
 =c_L\,{12+16i\over25}.                                  \tag{28}
\]

Para \(N_+=2L+1\), los exponentes en (26) son \(L+2\) y \(-3L\), y

\[
 \Re\{T_{N_+,L}(w)+T_{N_+,L}(w^{-1})\}
 ={12c_L\over25}\{2^{3L}-2^{-L-2}\}.                    \tag{29}
\]

Para \(N_-=2L+3\), son \(L+4\) y \(-(3L+2)\), y

\[
 \Re\{T_{N_-,L}(w)+T_{N_-,L}(w^{-1})\}
 =-{12c_L\over25}\{2^{3L+2}-2^{-L-4}\}.                 \tag{30}
\]

La contribución de Li del cuarteto al promedio es

\[
 Q^\triangle_{N,L}
 =4-2\Re\{T_{N,L}(w)+T_{N,L}(w^{-1})\},                  \tag{31}
\]

y el cambio correspondiente en \(B^\triangle_{N,L}\) es
\(-M Q^\triangle_{N,L}\) para multiplicidad \(M\). De (29), el cambio
es positivo y de tamaño \(\asymp M2^{3L}/L^2\); de (30), es negativo y
del mismo tamaño. En cambio (21), con \(N_\pm/L=2+O(1/L)\), tiene un
lado derecho menor que una constante absoluta.

Por tanto fallan **ambos** transportes candidatos

\[
 B^\triangle_{N,L}\leq C,
 \qquad B^\triangle_{N,L}\geq-C,                         \tag{32}
\]

si solo se usan fase crítica, simetrías funcionales y homotopía sin el
término (25). El cuarteto no tiene los pesos de Euler de los primos
ordinarios; por eso (29)--(30) no refutan una desigualdad específica de
\(\Lambda(m)\). Sí prueban que el promedio de bloques no permite
transportar (21) por una razón de escala o por cancelación automática del
filtro.

---

## 6. Decisión

```text
probado:
  fórmula cerrada para el promedio uniforme y su TV exacta;
  filtro triangular positivo sobre 2L-1 grados consecutivos;
  TV exacta como integral y cota explícita O(N/L+1);
  cota de fase |B^triangle_{N,L,a}|=O(N/L+1), a>=4;
  transporte exacto del filtro a cada residuo interior;
  ausencia de ceros del multiplicador dentro del disco;
  cuarteto racional con defectos de ambos signos ~2^(N+L)/L^2.

ganancia real:
  el promedio por bloques elimina por completo el costo lineal de la
  frontera cuando L es comparable con N.

descartado:
  que esa ganancia de frontera atenúe o cancele el defecto off-line;
  transportar cualquiera de las dos desigualdades unilaterales de (21)
  usando solo fase, simetría y homotopía.

sobrevive:
  probar directamente para los pesos ordinarios Lambda(m) una cota
  unilateral de bloques que acople P^triangle con la suma de (25).

no probado:
  esa cota aritmética, el criterio de bloques, A1 o RH.
```

El resultado no es otra coordenada de energía: conserva exactamente el
andamiaje \(a\geq4\), la fase completa, la suma de residuos y el
falsificador de la ruta Li--Laguerre.

## 7. Verificación reproducible

El archivo `tools/fejer_block_phase_transport_check.py` usa únicamente
`Fraction` y racionales gaussianos. Comprueba la normalización y el
centro de los pesos, (24), (23), (26), y las fórmulas firmadas
(28)--(31) para múltiples \(L\). La cota analítica de variación se prueba
en §2 y no se sustituye por muestreo.

Se reproduce con

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 fejer_block_phase_transport_check.py
```
