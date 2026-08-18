# 104_52 — Hessiano conectado de dos torres y gate de flujo cuadrático

**Objetivo del ataque.** Construir una forma de segundo orden que mantenga
simultáneamente los pesos reales \(\Lambda(p^k)=\log p\), el polo, el factor
Gamma y la fase Laguerre, y buscar en ella una cota coerciva para

\[
 H_n:=\lambda_n-{501\over2002}A_n
 ={1501\over2002}A_n-B_n\ge0,\qquad n\ge150.              \tag{1}
\]

Se obtiene una representación exacta. Sea

\[
 F(s)=(s-1)\zeta(s),\qquad
 G(s)={1\over2}s\pi^{-s/2}\Gamma(s/2),\qquad
 \kappa={1501\over2002},                                  \tag{2}
\]

y \(J_\kappa=\log F+\kappa\log G\), con las ramas reales en
\(s>1\). Entonces el Hessiano conectado completo es

\[
 \boxed{
 J_\kappa''(s)=
 \sum_{p}\sum_{k\ge1}\sum_{j=1}^{k}
       (\log p)^2p^{-ks}
 -{1\over(s-1)^2}
 +\kappa\sum_{r\ge1}{1\over(s+2r)^2}.}                   \tag{3}
\]

La primera suma es un par ordenado **anidado dentro de una misma torre**;
la segunda es su análogo continuo polar y la tercera conserva exactamente
el canal Gamma. La conclusión decisiva es negativa: antes de llegar a
(3), todos los pares entre torres primas distintas y todos los cruces
primo--polo se cancelan idénticamente al pasar del segundo momento al
Hessiano de \(\log F\). No queda una covarianza entre \(p\ne q\) sobre la
que pueda actuar una cota de no alineación.

Además, el miembro derecho de (3) no tiene signo ni siquiera en el rayo
real: su prolongación vale \(<0\) en \(s=1\) y \(>0\) en \(s=10\), con
certificados racionales. El cociclo mixto del test Laguerre también posee
ambos signos para cada \(n\ge4\). Por tanto la representación no produce
la coercividad proporcional de (1). El mismo mecanismo conectado existe
para \(\zeta(s+c)\zeta(s-c)\), cuyo sistema completado tiene ceros fuera de
la línea crítica.

Queda descartado el mecanismo estrecho

```text
segundo momento de dos marcas / covarianza de dos torres
+ sustracción conectada
+ signo del Hessiano real o del cociclo mixto Laguerre
    => H_n >= 0.
```

La misma cancelación se extiende a todo cumulante conectado de orden finito
de la jerarquía derivativa de \(\log F\): subir simplemente de dos a tres o
más marcas del observable aditivo \(\log N\) tampoco crea una interacción
entre primos distintos. Esto no habla de cumulantes de observables no
lineales arbitrarios de \(N\). No se descarta una desigualdad no lineal
sobre momentos **desconectados** que se aplique antes del logaritmo y
sobreviva a la cancelación. Este documento no prueba (1), A1 ni RH.

## 0. Auditoría de no duplicación

`103_68` ya factoriza una función completada como cociente de transformadas
de Laplace y calcula sus dos primeros cumulantes. `104_43`--`104_45`
construyen una sola marca size-biased; `104_49` prueba la cancelación de los
momentos completos contra los cumulantes grado por grado. No se cuentan de
nuevo esos resultados.

La adición estrecha aquí es distinta: se polariza literalmente el segundo
momento en dos marcas de torres, se calcula qué parte conectada sobrevive al
logaritmo y se incorpora el factor Gamma con el coeficiente exacto
\(1501/2002\) exigido por A1. La cancelación de todos los pares
\(p\ne q\), la fórmula completa (3), su cambio de signo racional y el flujo
cuadrático de la sección 6 son el contenido de este gate.

## 1. Dos marcas divisor y el kernel `lcm`

Fijemos \(s>1\). Bajo la ley zeta

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad X=\log N,  \tag{4}
\]

condicionado a \(N\), elija dos marcas \(D_1,D_2\) independientes con

\[
 \mathbb P(D_i=d\mid N)
 ={\Lambda(d)\over X}\mathbf1_{d\mid N}.                 \tag{5}
\]

La identidad \(\sum_{d\mid N}\Lambda(d)=\log N\) hace de (5) una
probabilidad cuando \(N>1\); en \(N=1\) se usa un estado cementerio, cuya
contribución desaparece por el factor \(X^2\). Para todo test \(Q\) para el
cual las sumas converjan,

\[
 \boxed{
 \mathbb E_s\{X^2Q(\log D_1,\log D_2)\}
 =\sum_{d,e\ge2}{\Lambda(d)\Lambda(e)\over
       \mathrm{lcm}(d,e)^s}Q(\log d,\log e).}       \tag{6}
\]

En efecto, después de cancelar \(X^2\), la suma sobre los múltiplos de
\(\mathrm{lcm}(d,e)\) vale
\(\zeta(s)\mathrm{lcm}(d,e)^{-s}\).

El comparador polar tiene una fórmula exactamente paralela. Sea
\(X_0\sim\mathrm{Exp}(s-1)\) y, condicionado a \(X_0=L\), elija
\(U_1,U_2\) independientes y uniformes en \([0,L]\). Entonces

\[
 \boxed{
 \mathbb E\{X_0^2Q(U_1,U_2)\}
 =\int_0^\infty\!\int_0^\infty
 e^{-(s-1)\max(x,y)}Q(x,y)\,dx\,dy.}                     \tag{7}
\]

Las ecuaciones (6)--(7) son una comparación de dos marcas completa; no
separan potencias primas ni toman valores absolutos.

Pero su parte conectada ya es local a una torre. Al sustraer el producto
de las intensidades de una marca, el kernel aritmético es

\[
 C_s(d,e)=\Lambda(d)\Lambda(e)
 \{\mathrm{lcm}(d,e)^{-s}-(de)^{-s}\}.             \tag{8}
\]

Si \(d=p^k,e=q^\ell\) y \(p\ne q\), entonces
\(\mathrm{lcm}(d,e)=de\), luego

\[
 \boxed{C_s(p^k,q^\ell)=0\qquad(p\ne q).}                \tag{9}
\]

Si \(p=q\), (8) es positivo y depende de \(\max(k,\ell)\). Así la
covarianza de divisibilidad detecta repeticiones dentro de una torre, no
una interacción entre torres diferentes. Esto es también consecuencia
directa de la independencia de los exponentes geométricos \(A_p\) en (4).

## 2. Cancelación exacta de los pares desconectados

Escribamos

\[
 \mathcal L(s)=\sum_{m\ge2}{\Lambda(m)\over m^s},\qquad
 \mathcal K_2(s)=\sum_{m\ge2}{\Lambda(m)\log m\over m^s}.\tag{10}
\]

Puesto que \(\zeta'/\zeta=-\mathcal L\), la diferenciación absoluta en
\(s>1\) da

\[
 {F''(s)\over F(s)}
 =\mathcal L(s)^2+\mathcal K_2(s)
       -{2\mathcal L(s)\over s-1}.                        \tag{11}
\]

Los tres términos de (11) son, respectivamente, los pares de potencias
primas independientes, la colisión anidada y los dos cruces primo--polo.
Por otro lado,

\[
 \left({F'(s)\over F(s)}\right)^2
 ={1\over(s-1)^2}+\mathcal L(s)^2
       -{2\mathcal L(s)\over s-1}.                        \tag{12}
\]

Restando (12) de (11),

\[
 \boxed{(\log F)''(s)=\mathcal K_2(s)-{1\over(s-1)^2}.}  \tag{13}
\]

En particular, \(\mathcal L^2\), incluidos todos los productos
\(p^{-ks}q^{-\ell s}\) con \(p\ne q\), desaparece con coeficiente
**exactamente cero**. Lo mismo ocurre con los cruces primo--polo. No es una
cota ni una pérdida causada por Cauchy--Schwarz: es la sustracción
momento--cumulante que define el logaritmo.

La renovación unitaria vuelve (13) una forma de pares anidados:

\[
 \begin{aligned}
 \mathcal K_2(s)
 &=\sum_m{\Lambda(m)\over m^s}\sum_{d\mid m}\Lambda(d)\\
 &=\sum_p\sum_{k\ge1}\sum_{j=1}^{k}
       (\log p)^2p^{-ks},                                  \tag{14}\\
 {1\over(s-1)^2}
 &=\int_{0\le y\le x<\infty}e^{-(s-1)x}\,dy\,dx.        \tag{15}
 \end{aligned}
\]

Como \(\Lambda(m)\ne0\) obliga a \(m=p^k\), el divisor marcado en (14)
pertenece necesariamente a la misma torre que el divisor exterior.

### 2.1. La obstrucción vale en todo orden conectado

No se recuperan interacciones entre torres pasando al tercer cumulante. Para
todo entero \(r\ge2\), la diferenciación absoluta en \(s>1\) da

\[
 \boxed{
 (\log F)^{(r)}(s)=(-1)^r
 \left\{
  \sum_{m\ge2}{\Lambda(m)(\log m)^{r-1}\over m^s}
  -{(r-1)!\over(s-1)^r}
 \right\}.}                                               \tag{15a}
\]

Si \(m=p^k\), entonces

\[
 \Lambda(m)(\log m)^{r-1}
 =(\log p)^r
 \sum_{j_1,\ldots,j_{r-1}=1}^{k}1.                       \tag{15b}
\]

Así cada cumulante de orden \(r\) es una marca exterior y \(r-1\) marcas
anidadas en **la misma** torre. Esto no es peculiar del segundo orden: es
la aditividad de \(\log\zeta=\sum_p-\log(1-p^{-s})\). Todos los cumulantes
mixtos de factores Euler distintos son cero.

El factor Gamma tampoco cambia esa conclusión. Derivando (18), para
\(r\ge2\),

\[
 (\log G)^{(r)}(s)
 =(-1)^r(r-1)!\sum_{j\ge1}{1\over(s+2j)^r}.               \tag{15c}
\]

Por consiguiente

\[
 \boxed{
 J_\kappa^{(r)}(s)=(-1)^r\left\{
 \sum_m{\Lambda(m)(\log m)^{r-1}\over m^s}
 -{(r-1)!\over(s-1)^r}
 +\kappa(r-1)!\sum_{j\ge1}{1\over(s+2j)^r}
 \right\}.}                                               \tag{15d}
\]

Por tanto ningún cumulante conectado de orden finito **de esta jerarquía
aditiva** puede ser el mecanismo multitorre faltante. Una ruta futura podría
usar un observable no lineal distinto; si permanece en la jerarquía de
\(\log F\), tendría que aplicar una desigualdad a los momentos desconectados
antes de que el logaritmo los elimine y controlar conjuntamente los términos
que después se cancelan.

## 3. Incorporación exacta de Gamma y el margen de A1

La factorización completada es \(\xi=FG\), salvo la constante ya incluida
en (2). Con la normalización de Phase 104,

\[
 A_n=n[z^n]\log G((1-z)^{-1}),\qquad
 B_n=-n[z^n]\log F((1-z)^{-1}).                           \tag{16}
\]

Por tanto (1) equivale exactamente a

\[
 \boxed{H_n=n[z^n]J_\kappa((1-z)^{-1})\ge0.}              \tag{17}
\]

No se ha aproximado el bloque Gamma. Su Hessiano es explícito. Si
\(\psi_1\) denota la trigamma,

\[
 \begin{aligned}
 (\log G)''(s)
 &=-{1\over s^2}+{1\over4}\psi_1(s/2)\\
 &=-{1\over s^2}+\sum_{r\ge0}{1\over(s+2r)^2}
 =\sum_{r\ge1}{1\over(s+2r)^2}.                          \tag{18}
 \end{aligned}
\]

Combinar (13), (14), (15) y (18) prueba (3). También el canal Gamma es una
forma de par continuo, pues

\[
 {1\over(s+2r)^2}
 =\int_{0\le y\le x<\infty}e^{-(s+2r)x}\,dy\,dx.         \tag{19}
\]

Así (3) mantiene realmente acoplados, en una sola forma firmada, torres
primas, polo y Gamma.

Para evitar cualquier uso ilegítimo de la serie Euler en \(s=1\), tome
\(a>1\), \(s_a(z)=a/(1-z)\), y defina

\[
 \mathcal H_{n,a}=n[z^n]J_\kappa(s_a(z)).                 \tag{20}
\]

En un disco pequeño todo el trayecto entre \(a\) y \(s_a(z)\) queda en
\(\Re s>1\), y

\[
 \boxed{
 \mathcal H_{n,a}
 =a[z^{n-1}]{1\over(1-z)^2}
 \left\{J_\kappa'(a)+\int_a^{s_a(z)}J_\kappa''(u)\,du\right\}.} \tag{21}
\]

La expresión entre llaves es \(J_\kappa'(s_a(z))\). Al retirar
\(a\downarrow1\), (20)--(21) convergen coeficiente a coeficiente a (17).
Ésta es la representación exacta de dos torres solicitada. Probar que su
límite es no negativo para todo \(n\ge150\) sigue siendo exactamente (1).

## 4. El Hessiano completo tiene ambos signos

La prolongación analítica de (3) a \(s=1\) puede evaluarse con la expansión

\[
 (s-1)\zeta(s)=1+\gamma(s-1)-\gamma_1(s-1)^2+O((s-1)^3).
\]

De aquí y (18),

\[
 \boxed{
 J_\kappa''(1)=-\gamma^2-2\gamma_1
      +\kappa\left({\pi^2\over8}-1\right)<0.}             \tag{22}
\]

El signo no depende de decimales de punto flotante. Las cotas racionales
ya usadas en `103_68`,

\[
 \gamma>{577\over1000},\qquad
 \gamma_1>-{73\over1000},\qquad
 \pi^2<{987\over100},                                    \tag{23}
\]

dan el techo exacto

\[
 J_\kappa''(1)
 <-\left({577\over1000}\right)^2+{146\over1000}
 +{1501\over2002}\left({987\over800}-1\right)
 =-{531207\over45500000}<0.                               \tag{24}
\]

En la otra dirección, (3) y (18) implican

\[
 J_\kappa''(10)
 >-{1\over81}+\kappa\sum_{r\ge1}{1\over(10+2r)^2}
 \ge-{1\over81}+{\kappa\over24}>0,                      \tag{25}
\]

porque para la función decreciente \((10+2x)^{-2}\),
la suma desde \(r=1\) domina su integral desde \(1\), que vale \(1/24\),
y \(81\cdot1501>24\cdot2002\). El término \(\mathcal K_2(10)\) es
positivo y solo mejora (25).

Por continuidad, el Hessiano del **funcional exacto del margen** cambia de
signo en \((1,10)\). No existe una convexidad real global que pueda
proporcionar (1).

## 5. El cociclo de fase Laguerre tampoco tiene signo

La interacción natural de dos incrementos de torres \(x,y>0\) sobre

\[
 P_n(t)=L_{n-1}^{(1)}(t)
\]

es el cociclo mixto

\[
 \Delta_{x,y}P_n(t)
 =P_n(t+x+y)-P_n(t+x)-P_n(t+y)+P_n(t).                    \tag{26}
\]

Para \(n\ge3\), la identidad de derivación Laguerre da

\[
 \boxed{
 \Delta_{x,y}P_n(t)
 =\int_0^x\!\int_0^y L_{n-3}^{(3)}(t+u+v)\,dv\,du.}       \tag{27}
\]

Si \(n\ge4\), \(L_{n-3}^{(3)}\) posee \(n-3\) ceros positivos simples y
alterna signo entre ellos. Eligiendo \(t\) dentro de un intervalo de signo
y luego \(x,y>0\) suficientemente pequeños, (27) adopta ambos signos. Esto
incluye cada grado \(n\ge150\).

El fenómeno ya se ve sin asintótica:

\[
 P_4(t)=4-6t+2t^2-{t^3\over6},\qquad
 \Delta_{x,y}P_4(t)=xy\left(4-t-{x+y\over2}\right).       \tag{28}
\]

Por tanto ni la parte conectada de dos marcas ni su test Laguerre poseen
el signo necesario para una desigualdad punto a punto. Integrarlos sin
separarlos devuelve exactamente (21).

## 6. Flujo de homotopía de segundo orden

Sea \(D=a\partial_a\). La ley de primer orden de `104_47` vale para
cualquier logaritmo compuesto con \(a/(1-z)\), en particular para
\(\mathcal H_{n,a}\):

\[
 D\mathcal H_{n,a}
 =n(\mathcal H_{n+1,a}-\mathcal H_{n,a}).                 \tag{29}
\]

Aplicándola una segunda vez y restando (29),

\[
 \boxed{
 D(D-1)\mathcal H_{n,a}
 =n(n+1)
 \{\mathcal H_{n+2,a}-2\mathcal H_{n+1,a}
                         +\mathcal H_{n,a}\}.}            \tag{30}
\]

Éste es el flujo cuadrático exacto. No crea una energía positiva: el lado
derecho es una segunda diferencia firmada, y por (21) su integral con los
datos de borde reconstruye \(H_n\) sin resto. Estimarlo con un signo sería
otra formulación de la coercividad faltante, no una consecuencia de la
identidad.

## 7. Falsificador desplazado

Para \(0<c<1/2\), normalice

\[
 F_c(s)=\{s-1-c\}\{s-1+c\}\zeta(s+c)\zeta(s-c).          \tag{31}
\]

En su semiplano Euler,

\[
 \mathcal L_c(s)=\mathcal L(s-c)+\mathcal L(s+c)
 =\sum_m{2\Lambda(m)\cosh(c\log m)\over m^s}.            \tag{32}
\]

La misma cancelación de (11)--(13) da

\[
 \boxed{
 (\log F_c)''(s)
 =\sum_m{2\Lambda(m)\cosh(c\log m)\log m\over m^s}
 -{1\over(s-1-c)^2}-{1\over(s-1+c)^2}.}                  \tag{33}
\]

El completado tampoco introduce pares cruzados:

\[
 \{\log G(s+c)+\log G(s-c)\}''
 =(\log G)''(s+c)+(\log G)''(s-c).                        \tag{33a}
\]

Otra vez no sobreviven pares entre primos distintos. Además
\(\log(p^k)=\sum_{j=1}^k\log p\), de modo que el primer término de (33)
admite el mismo marcado uniforme anidado que (14), aunque su peso exterior
dependa de \(k\). El completado \(\xi(s+c)\xi(s-c)\) tiene ceros a ambos
lados de \(\Re s=1/2\) y coeficientes de Li exponencialmente negativos en
una subsucesión (`104_48`, (21)--(23c)).

Así, segundo momento, sustracción conectada, marca interior uniforme,
canales polares y Gamma no bastan como axiomas abstractos. Una desigualdad
válida todavía podría usar el valor exterior exacto
\(\Lambda(p^k)=\log p\), que (32) pierde; pero el Hessiano de segundo orden
no genera interacción alguna entre torres para explotarlo.

## 8. Veredicto

Queda probado incondicionalmente:

1. el selector exacto de dos marcas y sus kernels `lcm` (6)--(9);
2. la cancelación conectada de todos los pares \(p\ne q\) y de los cruces
   primo--polo (11)--(13);
3. la forma anidada torre--polo--Gamma (3), (14)--(19);
4. la reconstrucción exacta del margen (17), (20)--(21);
5. el cambio de signo racional del Hessiano completo (22)--(25);
6. los dos signos del cociclo Laguerre (26)--(28);
7. el flujo cuadrático (30) y su análogo desplazado (33).

El resultado no es la cota (1). El frente superviviente se estrecha una
vez más: una cota proporcional debe retener una correlación **desconectada
y no lineal** antes de que el logaritmo elimine las interacciones entre
torres. Aumentar el orden del cumulante conectado del observable aditivo
\(\log N\) no sirve, por (15a)--(15d). El mecanismo debe además usar la
multiplicidad exterior unitaria para rechazar (32). No se ha construido esa
desigualdad.

## 9. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 connected_two_tower_flux_gate_check.py
```

El checker usa solo enteros y `Fraction`. Verifica la cancelación simbólica
de (11)--(13), la renovación anidada finita, el kernel `lcm`, los
certificados racionales (24)--(25), los dos signos exactos del cociclo
Laguerre en grado 151 y la identidad de flujo (30). No evalúa A1 ni RH.
