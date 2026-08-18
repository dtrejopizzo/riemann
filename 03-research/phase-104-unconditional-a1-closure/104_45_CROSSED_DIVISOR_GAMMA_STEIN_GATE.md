# 104_45 — Stein cruzado divisor–Gamma y núcleo de cola firmado

**Rol.** Ejecutar el único sucesor dejado abierto por `104_43` y
`104_44`: comparar la ley aritmética size-biased y el split continuo
Gamma--exponencial **dentro de una sola identidad**, antes de aplicar una
energía o una desigualdad. El acoplamiento se puede construir exactamente.
Además, su representación Stein local de primer orden es canónica: no
depende de cómo se acoplen las dos leyes.

El resultado no es la cota unilateral buscada. El núcleo canónico es

\[
 K_s(x)=\sum_{\log m>x}{\Lambda(m)\over m^s}
        -{e^{-(s-1)x}\over s-1},                              \tag{1}
\]

y cambia de signo incluso antes y después del primer átomo primo. Al
integrarlo contra la derivada del test Laguerre, el operador recompone
exactamente

\[
 \mathcal B_{n,s}\longrightarrow B_n=A_n-\lambda_n.          \tag{2}
\]

Por tanto una cota unilateral suficientemente fuerte para este operador es
**equivalente**, no previa, a

\[
 B_n\le {1501\over2002}A_n.                                  \tag{3}
\]

Queda descartado obtener (3) por elección del coupling, orden de transporte,
positividad del kernel Stein o una energía cruzada local automática. Queda
viva una desigualdad no local específica para la correlación entre (1) y el
test Laguerre real. Este documento no prueba (3), A1 ni RH.

## 0. Auditoría interna de no duplicación

`104_24` construye el generador Stein--Mecke completado y prueba que su
medida de saltos ya es firmada antes de \(\log2\); no acopla las dos leyes.
`104_29` corta ese generador en \(\log2\) y demuestra que la recomposición
es exactamente el margen buscado. `104_43` descubre la factorización
size-biased \(DN'\), el selector divisor y la divergencia de Efron--Stein
cuando se aplica a cada canal por separado. `104_44` añade el transporte
Markov, su brecha cero y la identidad conjunta de medias (su (25b)).

Lo que faltaba verificar era si un coupling **cruzado**, después de igualar
las masas prima y polo, podía conservar la cancelación y crear coercividad.
Lo nuevo y estrecho de este documento es: la igualación (13), la
independencia del kernel respecto del coupling (21), su falsificador
aritmético (29) y la cancelación simbólica exacta (40). No se reclama
novedad bibliográfica para teoría de Stein, size-bias o transporte óptimo.

## 1. Las dos factorizaciones completas

Fijemos

\[
 s=1+\varepsilon>1,\qquad
 \mathcal L_s=-{\zeta'\over\zeta}(s),\qquad
 R(q)=-{\zeta'\over\zeta}(1+q)-{1\over q}.                   \tag{4}
\]

La ley aritmética conjunta de `104_43` es

\[
 \mathbb Q_s(D=d,N'=k)
 ={\Lambda(d)(dk)^{-s}\over-\zeta'(s)},\qquad d\ge2, k\ge1.\tag{5}
\]

Sus coordenadas son independientes, \(D\) tiene la ley von Mangoldt
normalizada y \(N'\) tiene la ley zeta. El producto \(DN'\) tiene la ley
size-biased por \(\log N\), y, condicionado a \(DN'=n\),

\[
 \mathbb P(D=d\mid DN'=n)
 ={\Lambda(d)\over\log n}{\bf1}_{d\mid n}.                   \tag{6}
\]

En coordenadas aditivas escribimos

\[
 Y=\log D,\qquad X=\log N',\qquad S=Y+X.                     \tag{7}
\]

El comparador polar conserva también sus dos coordenadas. Sean

\[
 Y_0,X_0\stackrel{\rm ind}{\sim}\operatorname{Exp}(\varepsilon),
 \qquad S_0=Y_0+X_0\sim\Gamma(2,\varepsilon).                \tag{8}
\]

Condicionado a \(S_0=u\), \(Y_0\) es uniforme en \([0,u]\). Así, para

\[
 (\mathsf K_sf)(n)={1\over\log n}
       \sum_{d\mid n}\Lambda(d)f(\log d),\qquad
 (\mathsf Cf)(u)={1\over u}\int_0^u f(x)\,dx,                \tag{9}
\]

con la extensión \(\mathsf Cf(0)=f(0)\), valen

\[
 \mathbb E[f(Y)\mid S]=\mathsf K_sf(e^S),\qquad
 \mathbb E[f(Y_0)\mid S_0]=\mathsf Cf(S_0).                 \tag{10}
\]

Las ecuaciones (5)--(10) mantienen juntos todos los primos, todas las
potencias primas, el cofactor zeta y las dos coordenadas del split Gamma.
Aquí \(\Gamma(2,\varepsilon)\) es el Gamma probabilístico obtenido al
size-biasar el polo exponencial. El factor Gamma arquimediano de la función
completada no se ha omitido: su contribución exacta es el bloque \(A_n\) del
lado derecho de (3). La identidad \(B_n=A_n-\lambda_n\) aísla precisamente
el bloque prima--polo que debe compararse con ese \(A_n\).

## 2. Igualación exacta de masas y coupling cruzado

La diferencia prima--polo que debe estimarse es

\[
 \mathfrak M_\varepsilon(f)
 :=\sum_{m\ge2}{\Lambda(m)\over m^s}f(\log m)
    -\int_0^\infty e^{-\varepsilon x}f(x)\,dx.               \tag{11}
\]

Por la expansión de Laurent,

\[
 \varepsilon\mathcal L_s=1-\gamma\varepsilon+O(\varepsilon^2).
                                                                    \tag{12}
\]

En realidad

\[
 0<\varepsilon\mathcal L_s<1\qquad(\varepsilon>0).          \tag{12a}
\]

La primera desigualdad es inmediata y la segunda equivale a
\(R(\varepsilon)<0\), probada para todo \(\varepsilon>0\) en (40a) abajo.
Por tanto, sin restringir \(\varepsilon\), añadimos a la ley aritmética un
estado cementerio \(\partial=(0,0)\) y definimos

\[
 \widehat{\mathbb Q}_s
 =\varepsilon\mathcal L_s\,\mathbb Q_s
  +(1-\varepsilon\mathcal L_s)\delta_\partial.               \tag{13}
\]

Es una probabilidad, igual que la ley \(\mathbb Q_\varepsilon^0\) del par
\((Y_0,X_0)\). Sea \(\Pi_s\) **cualquier** coupling entre (13) y
\(\mathbb Q_\varepsilon^0\); en el estado cementerio ponemos
\(Y=X=S=0\). Entonces

\[
\boxed{
 \mathfrak M_\varepsilon(f)
 =R(\varepsilon)f(0)
  +{1\over\varepsilon}\,
     \mathbb E_{\Pi_s}\{f(Y)-f(Y_0)\}.}                     \tag{14}
\]

**Prueba.** La primera marginal de \(\Pi_s\) da

\[
 {1\over\varepsilon}\mathbb E f(Y)
 =\sum_{m\ge2}{\Lambda(m)\over m^s}f(\log m)
  +(\varepsilon^{-1}-\mathcal L_s)f(0),                      \tag{15}
\]

mientras que la segunda da

\[
 {1\over\varepsilon}\mathbb E f(Y_0)
 =\int_0^\infty e^{-\varepsilon x}f(x)\,dx.                 \tag{16}
\]

Como \(\varepsilon^{-1}-\mathcal L_s=-R(\varepsilon)\), (15)--(16)
prueban (14). \(\square\)

La misma identidad puede conservar explícitamente ambos totales. Sobre la
variable total aditiva defina

\[
 \widehat{\mathsf K}_sf(0)=f(0),\qquad
 \widehat{\mathsf K}_sf(u)=\mathsf K_sf(e^u)\quad(u>0).
\]

Entonces

\[
\boxed{
 \mathfrak M_\varepsilon(f)
 =R(\varepsilon)f(0)
 +{1\over\varepsilon}\mathbb E_{\Pi_s}
 \{\widehat{\mathsf K}_sf(S)-\mathsf Cf(S_0)\}.}            \tag{17}
\]

Ésta es la identidad Stein cruzada a nivel divisor--cofactor/Gamma--split.
No se ha estimado ninguna de las dos energías por separado.

## 3. El kernel Stein cruzado es canónico

Para una función \(C^1\) de crecimiento polinómico,

\[
 f(a)-f(b)=(a-b)\int_0^1f'(b+u(a-b))\,du.                    \tag{18}
\]

Definamos la medida orientada de ocupación

\[
 \Theta_{s,\Pi}(B)
 ={1\over\varepsilon}\mathbb E_{\Pi_s}
 \left[(Y-Y_0)\int_0^1
 {\mathbf 1}_B(Y_0+u(Y-Y_0))\,du\right].                    \tag{19}
\]

Para \(\varepsilon>0\), ambas marginales poseen momentos de todo orden:
en el lado aritmético esto es la convergencia absoluta de las derivadas de
la serie de Dirichlet en \(s>1\). Por tanto (19) tiene los momentos
necesarios para tests polinómicos y Fubini en (18)--(20) está justificado.

Entonces (14) se vuelve

\[
 \mathfrak M_\varepsilon(f)
 =R(\varepsilon)f(0)+\int_0^\infty f'(x)\Theta_{s,\Pi}(dx). \tag{20}
\]

La aparente libertad de escoger \(\Pi_s\) desaparece por completo:

**Teorema 3.1 (unicidad del kernel cruzado).** Para todo coupling
\(\Pi_s\), la medida (19) es absolutamente continua en \((0,\infty)\) y

\[
\boxed{
 \Theta_{s,\Pi}(dx)=K_s(x)\,dx,
 \quad
 K_s(x)=\sum_{\log m>x}{\Lambda(m)\over m^s}
       -{e^{-\varepsilon x}\over\varepsilon}.}              \tag{21}
\]

En particular, (21) es la única medida local de primer orden que puede
representar (14) para todos los tests.

**Prueba.** La densidad orientada de un segmento \([b,a]\) es

\[
 {\bf1}_{b<x<a}-{\bf1}_{a<x<b}
 ={\mathbf 1}_{a>x}-{\mathbf 1}_{b>x}.                       \tag{22}
\]

Promediar (22) en (19) usa solo las marginales:

\[
 {1\over\varepsilon}
 \{\mathbb P(Y>x)-\mathbb P(Y_0>x)\}.
\]

Para \(x>0\), el cementerio no contribuye,

\[
 \mathbb P(Y>x)
 =\varepsilon\sum_{\log m>x}{\Lambda(m)\over m^s},
 \qquad \mathbb P(Y_0>x)=e^{-\varepsilon x},                \tag{23}
\]

y resulta (21). La unicidad sigue probando contra derivadas compactamente
soportadas. \(\square\)

Por tanto ni el coupling monótono, ni el óptimo, ni uno dependiente de
\(n\) puede cambiar el kernel Stein de primer orden: todos producen (21).

## 4. Falsificador aritmético: tres signos alrededor de \(\log2\)

El kernel (21) carece de signo para los pesos **reales** de zeta. Sea
\(a=\log2\). Para \(0<x<a\),

\[
 K_s(x)=R(\varepsilon)+{1-e^{-\varepsilon x}\over\varepsilon}.
                                                                    \tag{24}
\]

Usando \(R(\varepsilon)\to-\gamma\), se obtiene

\[
 \lim_{\varepsilon\downarrow0}K_s(0+)=-\gamma<0,            \tag{25}
\]

\[
 \lim_{\varepsilon\downarrow0}K_s(a-)=\log2-\gamma>0.      \tag{26}
\]

Al cruzar el átomo \(m=2\), (21) salta hacia abajo en
\((\log2)2^{-s}\), de modo que

\[
 \lim_{\varepsilon\downarrow0}K_s(a+)
 ={\log2\over2}-\gamma<0.                                   \tag{27}
\]

Los signos son rigurosos, por ejemplo a partir de las cotas elementales

\[
 {1\over2}<\gamma<{3\over5},
 \qquad {2\over3}<\log2<1.                                  \tag{28}
\]

Para fijar que (28) no es input numérico: la comparación integral da
\(H_N-\log(N+1)<\gamma<H_N-\log N\). Con \(N=6\), la cota
\(\log7<39/20\) (los primeros siete términos de \(e^{39/20}\) ya suman
\(35844308849/5120000000>7\)) prueba \(\gamma>1/2\). Con \(N=25\), los
primeros 27 términos positivos de

\[
 \log25=2\sum_{j\ge0}{(12/13)^{2j+1}\over2j+1}
\]

superan racionalmente \(H_{25}-3/5\), y prueban
\(\gamma<3/5\). Finalmente la misma serie con argumento \(1/3\) da
\(\log2>2/3\), mientras \(\log2=\int_1^2dx/x<1\).

En efecto, (26) es mayor que \(2/3-3/5=1/15\), mientras (27) es menor
que \(1/2-1/2=0\). Por continuidad, para todo \(\varepsilon>0\)
suficientemente pequeño el kernel presenta el patrón

\[
 \boxed{K_s(0+)<0,\qquad K_s(a-)>0,\qquad K_s(a+)<0.}        \tag{29}
\]

Esto refuta, dentro de la aritmética real, positividad del kernel cruzado,
orden monótono entre los selectores y toda coercividad obtenida solamente
de un signo punto a punto de \(\Theta_{s,\Pi}\).

El contenido aritmético de \(K_s\) también puede verse sin probabilidades.
Si \(E(u)=\psi(e^u)-e^u\), integración de Stieltjes por partes da, fuera
de los átomos y con los límites laterales correspondientes en ellos,

\[
 \boxed{
 K_s(x)=-e^{-sx}E(x)+s\int_x^\infty e^{-su}E(u)\,du.}        \tag{29a}
\]

Así el kernel cruzado es exactamente una cola suavizada del error de PNT.
Usar una cota puntual sobre (29a) pierde la fase, mientras conservar su
signo completo conduce a la correlación Laguerre de la sección siguiente.

## 5. Especialización al vector Laguerre y equivalencia exacta

Sea \(n\ge2\) y

\[
 f_{n,s}(x)=L_{n-1}^{(1)}(sx),\qquad f_{n,s}(0)=n.            \tag{30}
\]

La derivada es

\[
 f'_{n,s}(x)=-sL_{n-2}^{(2)}(sx).                            \tag{31}
\]

La forma completa de `104_41` y `104_44` satisface

\[
 \mathcal B_{n,s}=s\mathfrak M_\varepsilon(f_{n,s}),
 \qquad \lim_{s\downarrow1}\mathcal B_{n,s}=B_n.           \tag{32}
\]

Aplicando (20)--(21), obtenemos la identidad Stein cruzada exacta

\[
\boxed{
 \mathcal B_{n,s}
 =snR(\varepsilon)
 -s^2\int_0^\infty L_{n-2}^{(2)}(sx)K_s(x)\,dx.}             \tag{33}
\]

No hay valor absoluto en (33); todos los \(p^k\), el polo y la fase
Laguerre permanecen acoplados. Sin embargo, (33) es una integración por
partes exacta de (11), no una desigualdad.

Con

\[
 \kappa={1501\over2002},                                    \tag{34}
\]

la cota que cerraría Phase 104 es, por (32)--(33), exactamente

\[
\boxed{
 \lim_{\varepsilon\downarrow0}
 \left\{snR(\varepsilon)
 -s^2\int_0^\infty L_{n-2}^{(2)}(sx)K_s(x)\,dx\right\}
 \le\kappa A_n.}                                            \tag{35}
\]

Pero el miembro izquierdo de (35) es \(B_n\). Así (35) es equivalente a
(3), y no puede registrarse como un lema intermedio.

La forma de coupling muestra la misma equivalencia de modo aún más directo:

\[
\boxed{
 \lim_{\varepsilon\downarrow0}{s\over\varepsilon}
 \mathbb E_{\Pi_s}
 \{f_{n,s}(Y)-f_{n,s}(Y_0)\}
 \le \kappa A_n+n\gamma.}                                  \tag{36}
\]

Por (14), (36) vale si y solo si (3). Cambiar el coupling no cambia la
esperanza ni el kernel (21).

## 6. Auditoría en transformadas: el operador recompone \(R\)

La descomposición de (17) hace visible dónde se cancela cualquier ganancia
aparente. Añada y reste \(\mathsf Cf(S)\). Para
\(f_t(x)=e^{-tx}\), defina

\[
 A_s(t)={1-\zeta(s+t)/\zeta(s)\over t},
 \quad A_s(0)=\mathcal L_s.                                  \tag{37}
\]

El defecto selector divisor--uniforme tiene símbolo

\[
 \Sigma_s(t)=\mathcal L_{s+t}-A_s(t),                        \tag{38}
\]

mientras el transporte entre el total aritmético aumentado y
\(\Gamma(2,\varepsilon)\) tiene símbolo

\[
 \Tau_s(t)=A_s(t)-R(\varepsilon)-{1\over\varepsilon+t}.      \tag{39}
\]

El término cementerio de (14) aporta \(R(\varepsilon)\). Por tanto

\[
\boxed{
 R(\varepsilon)+\Sigma_s(t)+\Tau_s(t)
 =\mathcal L_{s+t}-{1\over\varepsilon+t}
 =R(\varepsilon+t).}                                        \tag{40}
\]

Así, incluso antes de especializar a Laguerre, el Stein cruzado recompone
la función generatriz escalar exacta de `104_03`. Estimar (38) y (39) por
separado destruye la cancelación de \(A_s(t)\); mantenerlos juntos da (40).
Aquí sí existe una conclusión unilateral genuina en la subclase
exponencial. Por el teorema de Alzer--Kwong registrado en `104_18` §5,

\[
 F(s)=(s-1)\zeta(s)
 \quad\hbox{es estrictamente creciente para }s>1,
\]

se tiene

\[
 M_\Lambda(1+q)={F'(1+q)\over F(1+q)}>0,
 \qquad R(q)=-M_\Lambda(1+q)<0 \quad(q>0).                \tag{40a}
\]

Por tanto \(\mathfrak M_\varepsilon(e^{-t\,\cdot})=R(\varepsilon+t)<0\)
para todo \(t\ge0\). Por mezclas positivas, la misma desigualdad vale para
todo test completamente monótono para el cual Fubini esté justificado.

Este orden de Laplace no se puede promover a completa monotonía de
\(-R\). En efecto, póngase

\[
 \mathscr M(q):=-R(q)
 ={1\over q}-\sum_{m\ge2}{\Lambda(m)\over m^{1+q}}.
\]

Para todo entero \(j\ge0\), la diferenciación absoluta da

\[
 \boxed{
 (-1)^j\mathscr M^{(j)}(q)
 ={j!\over q^{j+1}}
 -\sum_{m\ge2}{\Lambda(m)(\log m)^j\over m^{1+q}}.}         \tag{40b}
\]

Tome \(j=32\) y \(q=32/\log2\). El solo átomo \(m=2\) de la suma es

\[
 { (\log2)^{33}\over2e^{32}},
 \qquad {32!\over q^{33}}
 ={32!(\log2)^{33}\over32^{33}}.                            \tag{40c}
\]

La comparación es exacta, sin racionalizar \(\log2\): de \(e<68/25\) y

\[
 32^{33}25^{32}>2\cdot32!\,68^{32}
\]

se sigue \(32^{33}>2\cdot32!e^{32}\). Por (40b)--(40c),

\[
 \boxed{\mathscr M^{(32)}(32/\log2)<0,}                     \tag{40d}
\]

contrario al signo exigido por el teorema de Bernstein. Así, ni siquiera
\(-R\) es completamente monótona. Además, aun una representación positiva de
Laplace no fijaría el signo del emparejamiento con \(L_n\), que cambia de
signo. Derivar (40) y combinar binomialmente recompone exactamente los
coeficientes \(B_n\), no una cota para ellos. La conclusión unilateral (40a)
es genuina, pero no alcanza el cono polinómico necesario para (35).

## 7. Falsificador estructural off-line

El hecho de conservar un coupling completo no autoriza una desigualdad
probabilística automática. Para \(a>0\), considere

\[
 Z_a(s)=\zeta(s+a)\zeta(s-a),\qquad
 X_a(s)=\xi(s+a)\xi(s-a).                                   \tag{41}
\]

En el semiplano \(\Re s>1+a\), la serie de Dirichlet de \(Z_a\) tiene
coeficientes positivos y

\[
 -{Z_a'\over Z_a}(s)
 =\sum_{m\ge2}{2\Lambda(m)\cosh(a\log m)\over m^s}.         \tag{42}
\]

Si \(Z_a(s)=\sum b_a(n)n^{-s}\), entonces la identidad formal
\(-Z_a'=(-Z_a'/Z_a)Z_a\) da

\[
 b_a(n)\log n
 =\sum_{d\mid n}2\Lambda(d)\cosh(a\log d)\,b_a(n/d).       \tag{43}
\]

Por ello (5)--(23), con sus pesos correspondientes, sus dos polos y sus
factores Gamma, se reproducen para \(X_a\) dentro de ese semiplano: hay
factorización size-biased, selector divisor positivo, split continuo y Stein
cruzado. Esta afirmación es local al dominio donde las dos tasas polares son
positivas; no postula un coupling probabilístico positivo hasta la línea de
simetría. Sin embargo \(X_a\) tiene ceros en
\(1/2\pm a+i\gamma\), fuera de esa línea.

Así, una inferencia basada únicamente en positividad de los pesos,
factorización size-biased, coupling, Jensen, identidad de segmentos y
splits Gamma también se aplicaría al falsificador (41). Una prueba válida
de (35) debe usar una propiedad cuantitativa adicional y específica de

\[
 \Lambda(p^k)=\log p,                                        \tag{44}
\]

capaz de correlacionar los cambios de signo de (21) con los del Laguerre.
El falsificador no refuta una desigualdad que realmente use (44); refuta
que el formalismo Stein cruzado, por sí solo, aporte el signo.

## 8. Decisión

Queda probado incondicionalmente:

1. el coupling de masa igualada (13)--(17), conservando
   divisor--cofactor y Gamma--split;
2. la representación Stein local canónica (20)--(21), independiente del
   coupling;
3. el patrón real de tres signos (29) alrededor del primer primo;
4. la identidad Laguerre exacta (33);
5. la recomposición completa del símbolo \(R\) en (40), junto con el
   signo unilateral \(R(q)<0\) sobre tests exponenciales.

Queda descartado:

```text
escoger un coupling mejor -> kernel Stein positivo;
orden de transporte divisor/uniforme -> cota unilateral;
energía cruzada local automática -> margen proporcional;
separar selector y total -> ganancia (A_s se cancela exactamente);
usar solo positividad/factorización/Gamma -> cierre (falsificador X_a).
```

Permanece abierto, sin reducción adicional:

\[
 \int_0^\infty L_{n-2}^{(2)}(sx)K_s(x)\,dx
 \quad\hbox{con su signo completo},                          \tag{45}
\]

uniformemente en \(n\ge150\) al retirar \(s\downarrow1\). Por (33), la
desigualdad requerida para (45) es exactamente (3), no una condición más
débil ya obtenida.

## 9. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 crossed_divisor_gamma_stein_gate_check.py
```

El checker usa únicamente enteros y `Fraction`. Verifica la identidad de
segmento orientado, la derivada Laguerre (31), la cancelación formal (40),
las implicaciones racionales de los signos (28)--(29), el certificado de
no-monotonía completa (40c)--(40d) y la identidad de convolución abstracta
subyacente a (43). No evalúa zeta, A1 ni RH.
