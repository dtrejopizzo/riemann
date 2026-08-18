# 104_59 — Gate de mayorización pre-log y Schur-convexidad

**Rol.** Auditar la última familia clásica propuesta para la ley
\(X=\log N\) antes de extraer el coeficiente Laguerre: mayorización de
vectores de masas, orden convexo de leyes y Schur-convexidad del test.

**Veredicto.** La capa probabilística ya estaba construida en 104_21 y
104_43. La mayorización clásica no lee el observable de A1:

1. mayorización de las **masas** olvida qué masa está unida a cada
   \(\log m\), mientras el momento Laguerre depende de esa unión;
2. mayorización de los **puntos de soporte** solo ordena funciones convexas
   o cóncavas, pero
   \(\varphi_n=L_{n-1}^{(1)}-n\) tiene curvatura de ambos signos para todo
   \(n\ge4\);
3. en la desintegración aritmética real, el selector divisor queda por
   encima del selector uniforme en \(N=2\) y por debajo en \(N=30\), ya
   para el test lineal.

Por tanto la familia clásica no aporta una desigualdad para A1. No queda
refutada una comparación global **firmada, dependiente de las posiciones y
específica de \(\Lambda\)**; pero al conservar esos datos su transformada
es exactamente el funcional \(R\) de 104_43, y su proyección Laguerre
vuelve al margen abierto. Este documento no prueba A1 ni RH.

## 1. Qué significa «mayorizar una ley»

Hay dos interpretaciones canónicas, y conviene no mezclarlas.

### 1.1 Mayorización del vector de probabilidades

Para una ley atómica

\[
 \mu=\sum_jp_j\delta_{x_j},                                      \tag{1}
\]

puede mayorizarse el vector no etiquetado \(p=(p_j)\). Toda función
Schur-convexa de \(p\) es simétrica: una permutación de las masas deja su
valor invariante.

El observable que aparece antes del límite regulado es, en cambio,

\[
 \mathcal L_n(\mu)=\sum_jp_j\varphi_n(x_j),
 \qquad \varphi_n(x)=L_{n-1}^{(1)}(x)-n.                       \tag{2}
\]

La asociación \(p_j\leftrightarrow x_j\) es parte esencial de (2). Por
ello (2) no es una función Schur del vector de masas.

El contraejemplo mínimo es exacto. Sobre los soportes
\((0,\ell)\), \(\ell=\log2>0\), tómense

\[
 p=(3/4,1/4),\qquad q=(1/4,3/4).                               \tag{3}
\]

Los vectores son permutaciones, luego \(p\succ q\) y \(q\succ p\). Para
\(n=2\),

\[
 \varphi_2(x)=L_1^{(1)}(x)-2=-x,
\]

y sin embargo

\[
 \mathcal L_2(p)=-{\ell\over4},\qquad
 \mathcal L_2(q)=-{3\ell\over4}.                              \tag{4}
\]

Así la mayorización de masas por sí sola ha descartado precisamente la
información que se necesita proyectar.

### 1.2 Mayorización de los puntos u orden convexo de medidas

La segunda interpretación conserva las posiciones. Para dos vectores con
la misma suma, \(x\succ y\), Karamata produce

\[
 \sum_j\phi(x_j)\ge\sum_j\phi(y_j)                              \tag{5}
\]

cuando \(\phi\) es convexa; invierte (5) cuando es cóncava. En lenguaje de
leyes, \(\mu\succeq_{\rm cx}\nu\) controla exactamente los tests convexos.
Las variantes de mayorización débil añaden monotonía al requisito.

Para el test real,

\[
 \varphi_n''(x)=L_{n-3}^{(3)}(x)\qquad(n\ge3).                  \tag{6}
\]

Si \(n\ge4\), el Laguerre del lado derecho tiene \(n-3\) ceros simples
positivos. Su signo alterna entre ellos. En consecuencia, para **cada**
\(n\ge4\), y por tanto para cada \(n\ge150\), \(\varphi_n\) no es
globalmente convexa ni globalmente cóncava. Además
\(\varphi_n'=-L_{n-2}^{(2)}\) cambia de signo, por lo que tampoco pertenece
a las clases creciente-convexa o decreciente-convexa de los órdenes
débiles.

Esto no es una objeción asintótica. El primer caso, \(n=4\), ya da dos
testigos cerrados:

\[
 \varphi_4(x)=-6x+2x^2-{x^3\over6},\qquad
 \varphi_4''(x)=4-x.                                          \tag{7}
\]

Para cualquier \(a\ge h\ge0\), el vector
\((a-h,a+h)\) mayoriza a \((a,a)\), y el defecto de Karamata es

\[
 \boxed{
 \varphi_4(a-h)+\varphi_4(a+h)-2\varphi_4(a)
 =h^2(4-a).}                                                   \tag{8}
\]

Con \((a,h)=(1,1)\), (8) vale \(3>0\); con \((a,h)=(5,1)\), vale
\(-1<0\). La misma relación de mayorización exige orientaciones opuestas.

El cambio de signo también ocurre sobre logaritmos de enteros. Si
\(\ell=\log2\), entonces

\[
 (\log1,\log4)\succ(\log2,\log2)
\]

y (8) vale

\[
 \ell^2(4-\ell)>0.                                             \tag{9}
\]

En cambio,

\[
 (\log64,\log256)\succ(\log128,\log128)
\]

y el mismo defecto vale

\[
 \ell^2(4-7\ell)<0.                                           \tag{10}
\]

Los signos de (9)--(10) no usan decimales: \(2<e\) da
\(\ell<1\), mientras \(e<3\) y \(3^4=81<128=2^7\) dan
\(4<7\ell\).

Por tanto no existe una orientación Schur universal para la familia de
tests que contiene A1. Partir el eje en intervalos de curvatura constante
no resuelve el problema: introduce términos de borde con signos alternos y
se convierte en la comparación firmada por lóbulos de 103_64.

## 2. La ley pre-log ya estaba disponible

La propuesta no duplica el Schur **matricial** de 104_34; ese documento
usa un complemento de Schur en dos rayos adyacentes. Tampoco duplica la
función de Schur analítica pre-log de 103_24 §6. Sí coincide con dos
construcciones probabilísticas previas:

1. 104_21 §1--§2 normaliza el producto Euler y prueba que
   \(X=\log N\) es compound-Poisson. Para \(u_2>u_1\) construye el
   acoplamiento exacto

   \[
    X(u_2)=X(u_1)+Z_{u_1,u_2},\qquad Z_{u_1,u_2}\ge0.          \tag{11}
   \]

   Esto ya da orden estocástico y sus refinamientos convexos. El propio
   documento registra que los Laguerre oscilatorios no pertenecen a esas
   clases.

2. 104_43 y 104_44 trabajan antes de separar el entero producto. La
   identidad \(\Lambda*1=\log\) da

   \[
    N^\star=DN',\qquad
    \mathbb P(D=d\mid N^\star=N)
      ={\Lambda(d)\over\log N}{\bf1}_{d\mid N}.                \tag{12}
   \]

   El comparador polar selecciona uniformemente un punto de
   \([0,\log N]\). Ésta es precisamente la casilla natural donde intentar
   una mayorización pre-log aritmética.

Además, 103_64 §6 ya audita el orden convexo después de la descomposición
en celdas: el costo es separable, su diferencia de Monge es cero y la
primitiva aritmética cambia de signo, con certificados reales
\(G(2976)>10\) y \(G(4000)<-3700\). 104_14 importa ese stop-gate al mapa
de Phase 104.

## 3. El comparador aritmético real no tiene orientación

La falta de convexidad del test ya impide usar Karamata. Hay además una
obstrucción anterior: ni siquiera el selector divisor real posee una
orientación uniforme respecto del selector continuo.

Condicionado a \(N\), sea

\[
 Y=\log D,\qquad U_N\sim{\rm Unif}[0,\log N].                   \tag{13}
\]

Para el test lineal \(f(y)=y\), 104_43 obtiene

\[
 2L\{\mathbb E(Y\mid N)-\mathbb E U_N\}
 =\sum_p a_p(a_p+1)(\log p)^2-L^2,
 \quad N=\prod_pp^{a_p},\quad L=\log N.                       \tag{14}
\]

En \(N=2\), (14) es \((\log2)^2>0\). En \(N=30\), poniendo
\(a=\log2,b=\log3,c=\log5\), es

\[
 a^2+b^2+c^2-2ab-2ac-2bc
 =(a+b-c)^2-4ab<0.                                             \tag{15}
\]

La última desigualdad es exacta: \(0<a+b-c=\log(6/5)<a\), luego
\((a+b-c)^2<a^2<4ab\). Así fallan ambas orientaciones uniformes ya
para una función simultáneamente creciente, convexa y cóncava.

Este testigo usa los pesos reales
\(\Lambda(2),\Lambda(3),\Lambda(5)\); no sustituye la aritmética por una
ley abstracta.

## 4. El candidato mínimo y su no-go

El uso clásico más fuerte que puede hacerse sin añadir estructura nueva es:

> **Candidato PM.** Construir un orden de mayorización entre la ley
> aritmética pre-log y una ley de referencia, y aplicar Karamata o
> Schur-convexidad para ordenar sus momentos \(\mathcal L_n\).

El candidato PM falla de dos maneras independientes:

* si se mayoriza el vector de masas, (3)--(4) prueban que el observable no
  desciende al cociente por permutaciones;
* si se mayoriza la variable aleatoria, (6)--(10) prueban que el observable
  no pertenece al cono dual del orden, para ninguno de los índices del
  rango objetivo.

La versión condicionada a las factorizaciones reales falla además por
(14)--(15). Por ello no hay un teorema útil de la familia clásica que
derive A1 después de establecer una sola relación de mayorización.

## 5. Qué no queda descartado

Los testigos no excluyen una identidad que haga simultáneamente lo
siguiente:

1. conserve la etiqueta \(m\mapsto\log m\);
2. distinga cada intervalo de curvatura de \(\varphi_n\);
3. compense los signos entre distintas factorizaciones \(N=dk\);
4. mantenga unidos el polo, Gamma y todos los pesos \(\Lambda(p^j)\).

Pero esto ya no es Schur-convexidad ni Karamata. Al promediar globalmente
la comparación (12), 104_43 §5 demuestra que su transformada de Laplace
es exactamente

\[
 R(t)=-{\zeta'\over\zeta}(1+t)-{1\over t},                    \tag{16}
\]

y que la proyección Laguerre produce
\(\Delta A_n-\Delta\lambda_n\). Por tanto una desigualdad firmada especial
para (16) sigue siendo un frente legítimo, pero no es una consecuencia de
mayorización: es el contenido aritmético abierto.

El falsificador off-line sigue siendo vinculante para cualquier sucesor.
Las propiedades positivas de la ley Euler y las relaciones de
mayorización anteriores no ven por sí solas el cuarteto
\(4-4\cosh(n\alpha)\cos(n\theta)\); una inferencia que también lo aceptara
no podría cerrar A1.

## 6. Verificación exacta

Ejecutar

    cd 03-research/phase-104-unconditional-a1-closure
    python3 tools/prelog_majorisation_gate_check.py

El verificador usa Fraction para:

* los defectos \(+3\) y \(-1\) de (8);
* las factorizaciones formales (9)--(10);
* la obstrucción por permutación (4);
* intervalos outward por la serie de artanh para certificar los signos
  reales de (14)--(15).

No evalúa \(\zeta\), coeficientes de Li, A1 ni RH.

## Estado

* **Duplicación localizada:** la ley pre-log y sus acoplamientos ya están
  en 104_21, 104_43 y 104_44.
* **Descartado:** mayorización clásica seguida de Schur-convexidad,
  Karamata, orden estocástico o convexo del test Laguerre.
* **No descartado:** una comparación global firmada, etiquetada y
  específica de \(\Lambda\); por (16), sigue siendo el mismo gate
  aritmético de fuerza A1.
* **Cierre:** no se prueba A1 ni RH.
