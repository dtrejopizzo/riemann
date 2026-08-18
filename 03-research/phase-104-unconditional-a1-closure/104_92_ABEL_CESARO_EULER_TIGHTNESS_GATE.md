# 104_92 — Gate de tightness Euler bajo suavizados Abel--Cesàro

**Resultado.** Hay dos suavizados naturales del producto global de
`104_85` que conservan literalmente los pesos ordinarios
\(\Lambda(m)\), la normalización en \(s=1\), la cero-libertad de cada
aproximante y la media logarítmica de Poisson cero:

1. medias de Riesz--Cesàro del corte primo;
2. el Abel exponencial \(e^{-\varepsilon m}\) en el tamaño aritmético.

Ninguno convierte por sí solo el gate unilateral de `104_89` en una
estimación incondicional. Para cualquier suavizado finito \(w\), si

\[
 u_w(t)=\log|F_w(1/2+it)|,
 \qquad u(t)=\log|(s-1)\zeta(s)|_{s=1/2+it},
\]

entonces se conserva la identidad exacta

\[
 \boxed{
 \int (u-u_w)_+\,d\nu
 =D_B+\int(u_w-u)_+\,d\nu,}
 \qquad
 d\nu(t)={dt\over2\pi(t^2+1/4)}.                    \tag{1}
\]

Aquí \(D_B\ge0\) es el defecto de Blaschke de `104_89`, y
\(D_B=0\Longleftrightarrow\mathrm{RH}\). Por tanto demostrar que el
primer miembro de (1) tiende a cero para cualquiera de estas familias
**sí probaría RH**, pero el suavizado no rebaja el contenido del paso.

Se prueban dos no-go exactos.

* El Abel en el corte logarítmico se calcula en forma cerrada y es solo
  una traslación horizontal:

  \[
   \eta\int_0^\infty e^{-\eta R}L_R(s)\,dR
   =\log{H(s+\eta)\over H(1+\eta)},
   \qquad H(s)=(s-1)\zeta(s).                         \tag{2}
  \]

  Su rango cero-libre incondicional alcanza \(\eta=1/2\), pero no
  produce una familia \(\eta\downarrow0\): cruzar ese umbral equivale a
  excluir ceros en los semiplanos desplazados.

* Toda media positiva regular, incluida Cesàro o Abel, puede conservar
  íntegra una fuga de masa Poisson aunque los aproximantes sean
  cero-libres y normalizados. Además se construye un modelo Euler
  continuo con medida de Mangoldt positiva, PNT con error
  \(O(x^\beta)\), polo simple y ceros simétricos \(\beta,1-\beta\),
  \(1/2<\beta<1\), para el cual los defectos unilaterales Abel y Cesàro
  divergen al menos como

  \[
   {\varepsilon^{1/2-\beta}\over\log^2(1/\varepsilon)},
   \qquad
   {X^{\beta-1/2}\over\log^2X},                       \tag{3}
  \]

  respectivamente.

El modelo no vive sobre las potencias de primos ordinarios y no conserva
los valores exactos \(\Lambda(p^k)=\log p\). No refuta el target real.
Prueba que PNT, positividad y suavizado positivo no pueden demostrarlo.
Por la unicidad de `104_88`, un falsificador que conservara literalmente
todos los \(\Lambda(m)\) sería la propia zeta y, por tanto, un
contraejemplo a RH.

Este documento no prueba Deep-\(\Lambda\), A1 ni RH. Cierra únicamente la
posibilidad de obtener el paso faltante por una regularización
Abel--Cesàro más un principio general de tightness.

---

## 1. Todas las truncaciones suavizadas tienen media cero

En coordenada \(y=\log x\), introduzca la medida firmada

\[
 d\mathcal M(y)
 =\sum_{m\ge2}{\Lambda(m)\over\log m}\,
       \delta_{\log m}(dy)-{e^y\over y}\,dy.           \tag{4}
\]

La singularidad en \(y=0\) siempre aparece multiplicada por una función
que se anula allí. Para un peso real \(w\) de soporte compacto, o de
decaimiento suficiente, ponga

\[
 L_w(s)=\int_0^\infty
 w(y)(e^{-sy}-e^{-y})\,d\mathcal M(y),
 \qquad F_w(s)=e^{L_w(s)}.                              \tag{5}
\]

Entonces \(F_w\) es entera y cero-libre en los casos finitos considerados
abajo, y \(F_w(1)=1\). Sobre \(s=1/2+it\),

\[
 \Re(e^{-sy}-e^{-y})=e^{-y/2}\cos(ty)-e^{-y}.          \tag{6}
\]

La función característica de la probabilidad de Cauchy \(\nu\) es

\[
 \int_{\mathbb R}e^{ity}\,d\nu(t)=e^{-|y|/2}.         \tag{7}
\]

Por (6)--(7), cada modo de (5) tiene media cero. Fubini es legítimo para
todo peso finito o exponencial usado aquí, y da

\[
 \boxed{\int_{\mathbb R}\log|F_w(1/2+it)|\,d\nu(t)=0.} \tag{8}
\]

Tres elecciones concretas son:

\[
\begin{array}{c|c}
\text{corte duro en }R & w_R(y)={\bf1}_{[0,R]}(y),\\[2mm]
\text{Riesz--Cesàro de orden }k
  & w_{R,k}(y)=(1-y/R)_+^k,\\[2mm]
\text{Abel en }X=e^R & w_\varepsilon(y)=e^{-\varepsilon e^y}.
\end{array}                                             \tag{9}
\]

La última familia es particularmente limpia:

\[
\begin{aligned}
 L_\varepsilon^{\rm ar}(s)
={}&\sum_{m\ge2}{\Lambda(m)\over\log m}e^{-\varepsilon m}
       (m^{-s}-m^{-1})\\
 &+\int_1^\infty e^{-\varepsilon x}
       {x^{-1}-x^{-s}\over\log x}\,dx.                \tag{10}
\end{aligned}
\]

Para cada \(\varepsilon>0\), (10) es entera, su exponencial nunca se
anula, vale uno en \(s=1\), usa los \(\Lambda(m)\) literales y satisface
(8). También es exactamente el promedio Abel de los cortes duros en la
variable aritmética:

\[
 L_\varepsilon^{\rm ar}(s)
 =\varepsilon\int_1^\infty e^{-\varepsilon X}
       L_{\log X}(s)\,dX.                              \tag{11}
\]

En \(\Re s>1\), convergencia dominada da

\[
 L_\varepsilon^{\rm ar}(s)
 \longrightarrow\log H(s)\qquad(\varepsilon\downarrow0), \tag{12}
\]

con la rama fijada por \(H(1)=1\). VK permite transportar el germen hasta
\(\Re s=1\), pero no hasta un semiplano fijo a su izquierda, exactamente
como en `104_85`.

## 2. La obligación unilateral es invariante bajo el suavizado

Sea \(u_w(t)=\Re L_w(1/2+it)\), y sea \(u\) el log-módulo de \(H\).
Por `104_89`,

\[
 \int u\,d\nu=D_B,
 \qquad \int u_w\,d\nu=0.                              \tag{13}
\]

Definiendo

\[
 I_w=\int(u-u_w)_+d\nu,
 \qquad J_w=\int(u_w-u)_+d\nu,                         \tag{14}
\]

la identidad \(f=f_+-(-f)_+\) prueba (1):

\[
 \boxed{I_w=D_B+J_w.}                                  \tag{15}
\]

No hay pérdida de constantes ni estimación. En particular:

\[
 I_{w_j}\to0
 \quad\Longrightarrow\quad D_B=0
 \quad\Longleftrightarrow\quad\mathrm{RH}.            \tag{16}
\]

La parte adicional \(J_{w_j}\to0\) es tightness de borde. No es una
consecuencia formal de que \(w_j\to1\), de convergencia interior ni de la
media cero.

## 3. El Abel logarítmico es una traslación, no un escape

Para el corte duro \(L_R=L_{w_R}\), ponga

\[
 \mathcal A_\eta L(s)
 =\eta\int_0^\infty e^{-\eta R}L_R(s)\,dR.             \tag{17}
\]

Cuando \(\Re s+\eta>1\), la integral es absolutamente intercambiable y

\[
 \mathcal A_\eta L(s)
 =\int_0^\infty e^{-\eta y}
      (e^{-sy}-e^{-y})\,d\mathcal M(y).                \tag{18}
\]

La parte discreta es

\[
 \log\zeta(s+\eta)-\log\zeta(1+\eta),                 \tag{19}
\]

y Frullani da para la continua

\[
 \int_0^\infty
 {e^{-\eta y}-e^{-(s+\eta-1)y}\over y}\,dy
 =\log{s+\eta-1\over\eta}.                            \tag{20}
\]

Esto prueba (2). Sobre el semiplano de Poisson \(\Re s>1/2\), la
derivación incondicional cubre \(\eta>1/2\); el borde
\(\eta=1/2\) se obtiene por el PNT y límite desde la derecha. Para
\(0<\eta<1/2\), la continuación de (2) tiene un cero en ese semiplano
exactamente cuando existe \(\rho\) con
\(\Re\rho>1/2+\eta\). Por tanto afirmar simultáneamente

\[
 \mathcal A_\eta L=\log{H(s+\eta)\over H(1+\eta)}
 \quad\text{como logaritmo holomorfo cero-libre en }\Re s>1/2          \tag{21}
\]

para una sucesión \(\eta\downarrow0\) ya excluye todos los ceros
derechos. El Abel logarítmico llega a la misma frontera RH desde otra
coordenada; no la atraviesa.

## 4. No-go para toda media positiva regular

En el disco, ponga

\[
 C_r(z)={1+rz\over1-rz},
 \qquad
 G_r(z)=\exp\{D[C_r(z)-C_{-r}(z)]\},
 \quad0<r<1.                                            \tag{22}
\]

Cada \(G_r\) es cero-libre y \(G_r(0)=1\). En la frontera,

\[
 g_r(\theta):=\log|G_r(e^{i\theta})|
 =D\{P_r(\theta)-P_{-r}(\theta)\},                    \tag{23}
\]

donde \(P_r\) es el kernel de Poisson. Todos los \(g_r\) tienen media
cero y, crucialmente,

\[
 \mathrm{sgn}\,g_r(\theta)=\mathrm{sgn}\,\cos\theta
 \quad\text{para todo }r.                              \tag{24}
\]

Además,

\[
 \int(g_r)_+{d\theta\over2\pi}
 =D\left\{{4\over\pi}
   \arctan{1+r\over1-r}-1\right\}\longrightarrow D.  \tag{25}
\]

Sea \((a_{N,j})\) cualquier matriz de sumación positiva regular:
\(a_{N,j}\ge0\), \(\sum_j a_{N,j}=1\), y su masa abandona todo segmento
inicial fijo. Si \(r_j\uparrow1\), (24) da la igualdad, no solo una cota,

\[
 \left(\sum_j a_{N,j}g_{r_j}\right)_+
 =\sum_j a_{N,j}(g_{r_j})_+.                            \tag{26}
\]

Por (25), ambos costos unilaterales de la media tienden a \(D\). Esto
incluye Cesàro \(a_{N,j}=N^{-1}{\bf1}_{j\le N}\) y Abel
\(a_{q,j}=(1-q)q^{j-1}\), \(q\uparrow1\). Las medias geométricas

\[
 \exp\left\{\sum_j a_{N,j}\log G_{r_j}(z)\right\}     \tag{27}
\]

siguen siendo holomorfas, normalizadas y cero-libres. Así una media
positiva regular no destruye automáticamente una fuga firmada: si las
crestas tienen el mismo signo geométrico, las conserva exactamente.

El falsificador incluye incluso convergencia interior. En todo compacto
del disco,

\[
 G_r(z)\longrightarrow
 G_*(z):=\exp\{D[C_1(z)-C_{-1}(z)]\}.                  \tag{27a}
\]

La regularidad de la matriz transporta ese límite a (27). La función
\(G_*\) es holomorfa, normalizada y cero-libre; salvo en los dos puntos
singulares de borde, \(C_1-C_{-1}\) tiene parte real cero, de modo que
\(\log|G_*|=0\) casi en todas partes. A pesar de ello, por (25)--(26),
las partes positiva y negativa del defecto fronterizo siguen tendiendo a
\(D\). Ni siquiera «límite interior cero-libre + sumación positiva
regular» implica tightness.

## 5. Contra-modelo Euler positivo con PNT

El no-go anterior es funcional. El siguiente conserva además un canal
Euler continuo positivo y un PNT fuerte.

Fije \(1/2<\beta<1\) y elija \(X_0>1\) tan grande que

\[
 X_0^{\beta-1}+X_0^{-\beta}<1.                          \tag{28}
\]

Defina la medida de Mangoldt continua

\[
 d\Psi_\beta(x)=
 \begin{cases}
 dx,&1\le x<X_0,\\
 \{1-x^{\beta-1}-x^{-\beta}\}\,dx,&x\ge X_0.
 \end{cases}                                           \tag{29}
\]

Es positiva por (28), y

\[
 \Psi_\beta(x)=x+O(x^\beta).                           \tag{30}
\]

En particular, (30) es más fuerte que una majorante de tipo VK para
\(x\) grande. Su transformada de Mellin centrada es

\[
 \int_1^\infty x^{-s}\{d\Psi_\beta(x)-dx\}
 =-{X_0^{\beta-s}\over s-\beta}
  -{X_0^{1-\beta-s}\over s-(1-\beta)}.                \tag{31}
\]

Los residuos en \(\beta\) y \(1-\beta\) son \(-1\). Defina el
renormalizado normalizado

\[
\begin{aligned}
 P_\beta(s)
 =-\int_{X_0}^\infty &(x^{-s}-x^{-1})\\
 &\times {x^{\beta-1}+x^{-\beta}\over\log x}\,dx,
 \qquad H_\beta(s)=e^{P_\beta(s)}                     \tag{32}
\end{aligned}
\]

primero para \(\Re s>\beta\), y luego por continuación. Como

\[
 P_\beta'(s)
 ={X_0^{\beta-s}\over s-\beta}
 +{X_0^{1-\beta-s}\over s-(1-\beta)},                 \tag{33}
\]

la continuación de \(H_\beta\) tiene ceros simples en
\(\beta,1-\beta\). La función

\[
 Z_\beta(s)={H_\beta(s)\over s-1}                     \tag{34}
\]

tiene polo simple en uno y

\[
 -{Z_\beta'\over Z_\beta}(s)
 =\int_1^\infty x^{-s}\,d\Psi_\beta(x).               \tag{35}
\]

Así el canal de Mangoldt es positivo, satisface PNT y, sin embargo, posee
un par simétrico fuera de la línea.

### 5.1 Falla cuantitativa de Cesàro

La media Cesàro de los cortes duros en \(X\) inserta el peso
\((1-x/X)_+\). Sea \(P_{\beta,X}^{C}\) la versión de (32) con ese peso.
En \(s=1/2\),

\[
 -P_{\beta,X}^{C}(1/2)
 \gg {X^{\beta-1/2}\over\log X}.                       \tag{36}
\]

La misma cota, con constante menor, vale para
\(|t|\le c/\log X\): en \(x\le X\), la fase
\(\cos(t\log x)\) permanece positiva si \(c\) es pequeño. Como
\(\nu([-c/\log X,c/\log X])\asymp1/\log X\),

\[
 \boxed{
 \int(-\Re P_{\beta,X}^{C}(1/2+it))_+d\nu(t)
 \gg {X^{\beta-1/2}\over\log^2X}\longrightarrow\infty.} \tag{37}
\]

### 5.2 Falla cuantitativa de Abel

Inserte ahora \(e^{-\varepsilon x}\) en (32) y llame al resultado
\(P_{\beta,\varepsilon}^{A}\). En la ventana
\(x\asymp\varepsilon^{-1}\),

\[
 -\Re P_{\beta,\varepsilon}^{A}(1/2+it)
 \gg {\varepsilon^{1/2-\beta}\over
          \log(1/\varepsilon)}                         \tag{38}
\]

uniformemente para \(|t|\le c/\log(1/\varepsilon)\).
La cola \(x>\varepsilon^{-2}\) es exponencialmente despreciable y el
intervalo fijo \([X_0,4]\) cuesta \(O(1)\), de modo que no pueden cancelar
la ventana principal. Integrando otra vez contra \(\nu\),

\[
 \boxed{
 \int(-\Re P_{\beta,\varepsilon}^{A}(1/2+it))_+d\nu(t)
 \gg {\varepsilon^{1/2-\beta}\over
          \log^2(1/\varepsilon)}\longrightarrow\infty.} \tag{39}
\]

El límite \(H_\beta\) es finito sobre la recta crítica. Por ello sustituir
\(-\Re P_{\beta,\varepsilon}^{A,C}\) por el defecto positivo entre el
log-módulo límite y el aproximante solo cambia (37)--(39) en un término
acotado. El gate unilateral falla de manera divergente.

El modelo (29) no tiene soporte discreto ni la ecuación funcional completa
de la zeta. Su función es falsificar la inferencia

\[
 \text{PNT/VK + medida Mangoldt positiva + Abel/Cesàro}
 \Longrightarrow\text{tightness unilateral}.          \tag{40}
\]

`104_90` conserva, en otra construcción, soporte sobre potencias de primos
ordinarios y una ecuación funcional amplia, a costa de alterar una torre y
admitir polos Euler adicionales. Los dos falsificadores son complementarios.

## 6. Auditoría de duplicación interna

* `104_64` y `104_66` Abelizan el **grado de Li** y el regulador
  prima--Laguerre, no el cutoff de Euler de `104_85`.
* `104_75` poissoniza el grado y obtiene la transformada de Bessel del
  primer momento; tampoco suaviza el cutoff primo.
* `104_79` trabaja con la ley zeta antes del logaritmo y prueba una falla de
  uniformidad diagonal distinta.
* `104_85` construye el corte duro global; `104_89` obtiene el gate
  unilateral y los spikes individuales. Las fórmulas (10)--(11), la
  barrera de traslación (17)--(21) y la estabilidad de los spikes bajo
  toda matriz positiva regular no aparecen allí.
* E101.060--E101.068 usan Abel en el índice exterior de otro current.
  E101.086--E101.087 estudian una energía log-gaussiana del error primo.
  Son precedentes de la misma pared de tightness, pero no contienen las
  truncaciones Euler normalizadas de (9)--(11).

Por tanto este gate no repite el ataque Hurwitz/Nyman: no usa Hurwitz para
intentar el cierre ni introduce un residual Möbius. Su conclusión es
negativa y específica al suavizado del cutoff Euler.

## 7. Estado exacto

Se ha probado:

\[
\begin{gathered}
 \text{Riesz--Cesàro y Abel aritmético preservan media Poisson cero},\\
 \text{tightness unilateral para los }\Lambda(m)\text{ reales}
   \Longrightarrow\mathrm{RH},\\
 \text{Abel logarítmico}=\text{traslación horizontal},\\
 \text{sumación positiva regular no elimina spikes alineados},\\
 \text{PNT + positividad no implican tightness, incluso con suavizado}.
\end{gathered}                                           \tag{41}
\]

No se ha probado:

\[
 \int(u-u_{w_j})_+d\nu\longrightarrow0
 \quad\text{para los pesos ordinarios }\Lambda(m).     \tag{42}
\]

La ecuación (42) sigue siendo un criterio RH-equivalente (con la tightness
correspondiente), no una consecuencia incondicional de las regularizaciones.

## 8. Reproducción

Desde `tools/`:

```bash
python3 abel_cesaro_euler_tightness_check.py
```

El checker verifica la masa unilateral cerrada de (25), su conservación
bajo medias Cesàro/Abel, la positividad y los residuos del modelo
(29)--(31), y el crecimiento numérico de las escalas de (36)/(38). Es un
control diagnóstico de identidades demostradas arriba; no certifica (42).
