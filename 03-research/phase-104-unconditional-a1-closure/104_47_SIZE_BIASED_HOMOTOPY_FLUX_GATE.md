# 104_47 — Flujo size-biased de la homotopía y gate exacto de residuos

**Estado.** Se combinan, sin separar primos, potencias primas ni polo, la
homotopía \(a\downarrow1\) de `104_41` y el selector divisor exacto de
`104_43`. El resultado es una ley diferencial cerrada y una fórmula de
flujo firmada:

\[
 \boxed{
 a\,\partial_a\mathcal B_{n,a}
 =n\{\mathcal B_{n+1,a}-\mathcal B_{n,a}\}.}
 \tag{1}
\]

En coordenadas size-biased, la densidad de este flujo es exactamente la
diferencia entre el selector divisor de von Mangoldt y el selector uniforme
del polo, probados conjuntamente contra \(L_n\). El selector no depende de
\(a\); toda la dependencia de la homotopía queda en las dos leyes
exponencialmente inclinadas y en la escala del test.

La identidad no cierra el margen. Al integrarla desde un punto Euler
\(a_0\ge4\) hasta \(1\), la desigualdad unilateral necesaria para el flujo es
**equivalente**, sin resto, a

\[
 H_n=\lambda_n-{501\over2002}A_n\ge0.                       \tag{2}
\]

Cero por cero, el valor en el extremo crítico es el valor Euler menos el
flujo integrado; esa reconstrucción es exactamente el residuo que cruza el
círculo de Hardy. El cuarteto racional de `104_41` deja inalterada la fase
crítica y produce en el flujo una cantidad de tamaño \(2^{152}\). Por tanto
el selector size-biased localiza correctamente dónde debería entrar el nuevo
input aritmético, pero no lo fabrica.

Queda descartado el mecanismo «diferenciar en \(a\), aplicar solamente
Markov/Jensen al selector y cerrar el flujo por una desigualdad genérica».
No queda descartada una desigualdad firmada que use de manera esencial la
rigidez especial

\[
 \Lambda(p^k)=\log p                                                   \tag{3}
\]

en todas las torres a la vez. Este documento no prueba (2), A1 ni RH.

## 1. Auditoría de no duplicación

`104_18` correlaciona un desplazamiento de Jordan \(u=c\varepsilon\) con
\(\varepsilon\downarrow0\); su límite es el costo adyacente
\(C_n=\lambda_n^{\rm prime}-\lambda_{n+1}^{\rm prime}\). Aquí no hay
desplazamiento de Jordan: se deriva el parámetro geométrico
\(s=a/(1-z)\) de la homotopía completa.

`104_31` transporta hacia atrás un test fijo mediante el generador
\(-M_x\) y prueba la colisión de dominios en \(\varepsilon=1/2\). En (1) el
test se escala simultáneamente como \(P_n(ax)\), de modo que no se postula
un semigrupo inverso en un espacio de Hilbert. La obstrucción que aparece es
distinta: el flujo acopla exactamente los grados \(n\) y \(n+1\).

`104_43` construye el selector size-biased para un \(a>1\) fijo, y `104_44`
estudia su contracción Markov y el costo de reescalar Laguerre. No se repiten
ni la brecha cero ni el costo exponencial de escala. Lo nuevo aquí es
mantener el selector durante todo \(a\downarrow1\), calcular su ley de flujo
y compararla cero por cero con el término de residuos de `104_41`.

La cola Abel de coeficientes de `104_41` (4a) tampoco se reinvierte: (1) es
una identidad diferencial antes de intentar cualquier inferencia
Tauberiana.

## 2. Los dos selectores durante la homotopía

Sea \(a>1\), \(\varepsilon=a-1\), y escribamos

\[
 \mathfrak m(a)=-{\zeta'(a)\over\zeta(a)}
 =\sum_{d\ge2}{\Lambda(d)\over d^a}.                         \tag{4}
\]

Sean \(D_a,N_a'\) independientes con

\[
 \mathbb P(D_a=d)={\Lambda(d)d^{-a}\over\mathfrak m(a)},
 \qquad
 \mathbb P(N_a'=k)={k^{-a}\over\zeta(a)},                    \tag{5}
\]

y \(N_a^*=D_aN_a'\). Por `104_43`,

\[
 \mathbb P(D_a=d\mid N_a^*=N)
 ={\Lambda(d)\over\log N}{\bf1}_{d\mid N}.                  \tag{6}
\]

Denotemos este kernel por \(K\). Es importante que \(K\) no depende de
\(a\): variar \(a\) solo inclina exponencialmente la ley del producto.

En el canal polar, sean \(Y_a,Y_a'\) exponenciales independientes de tasa
\(\varepsilon\), y \(S_a^*=Y_a+Y_a'\). Condicionado a \(S_a^*=x\), \(Y_a\)
es uniforme en \([0,x]\); escribamos

\[
 (Uf)(x)={1\over x}\int_0^x f(y)\,dy.                        \tag{7}
\]

También \(U\) es independiente de \(a\). Sean

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad f_{n,a}(x)=P_n(ax).           \tag{8}
\]

La forma completa de `104_41` admite entonces la desintegración

\[
 \boxed{
 \begin{aligned}
 \mathcal B_{n,a}
  =a\bigg\{&\mathfrak m(a)
       \mathbb E\big[(Kf_{n,a})(N_a^*)\big]\\
    &-{1\over\varepsilon}
       \mathbb E\big[(Uf_{n,a})(S_a^*)\big]\bigg\}.
 \end{aligned}}                                             \tag{9}
\]

En efecto, las esperanzas condicionadas de (9) recuperan respectivamente
la ley de \(D_a\) y la de \(Y_a\). Por tanto (9) es exactamente

\[
 a\sum_{d\ge2}{\Lambda(d)\over d^a}P_n(a\log d)
 -a\int_0^\infty e^{-(a-1)x}P_n(ax)\,dx.                    \tag{10}
\]

No se tomó módulo, y ambos selectores permanecen dentro de la misma resta.
Además,

\[
 \lim_{a\downarrow1}\mathcal B_{n,a}=B_n=A_n-\lambda_n.     \tag{11}
\]

## 3. Ley diferencial exacta

La identidad elemental que gobierna el flujo es

\[
 \boxed{
 P_n(x)+xP_n'(x)-xP_n(x)=nL_n(x)
 =n\{P_{n+1}(x)-P_n(x)\}.}                                  \tag{12}
\]

Por consiguiente, para \(y\ge0\),

\[
 a{d\over da}\{a e^{-ay}P_n(ay)\}
 =n\{a e^{-ay}P_{n+1}(ay)-a e^{-ay}P_n(ay)\}.              \tag{13}
\]

Multiplicar (13) por \(e^y\) da la misma identidad con
\(e^{-(a-1)y}\), el peso polar. Para \(a\ge1+\delta>1\), las series y las
integrales de (10), junto con todas sus derivadas, convergen absolutamente.
Se puede por tanto derivar término a término y se obtiene (1).

La diferencia de grados conserva explícitamente los dos selectores. Si

\[
 \ell_{n,a}(x)=L_n(ax),                                      \tag{14}
\]

entonces

\[
 \boxed{
 \begin{aligned}
 \mathcal B_{n+1,a}-\mathcal B_{n,a}
 =a\bigg\{&\mathfrak m(a)
       \mathbb E[(K\ell_{n,a})(N_a^*)]\\
   &-{1\over\varepsilon}
       \mathbb E[(U\ell_{n,a})(S_a^*)]\bigg\}.
 \end{aligned}}                                             \tag{15}
\]

Así, la derivada de la homotopía no introduce una cantidad desconocida
auxiliar: introduce exactamente la comparación firmada divisor--uniforme
contra el siguiente Laguerre.

## 4. El teorema de flujo que faltaría es exactamente \(H_n\ge0\)

Fijemos \(a_0\ge4\) y definamos, manteniendo conjunta la resta,

\[
 \begin{aligned}
 \mathscr J_{n}(a_0):={}&n\lim_{\delta\downarrow0}
 \int_{1+\delta}^{a_0}
 \bigg\{\mathfrak m(a)
       \mathbb E[(K\ell_{n,a})(N_a^*)]\\
 &\hspace{38mm}-{1\over a-1}
       \mathbb E[(U\ell_{n,a})(S_a^*)]\bigg\}\,da.
                                                               \tag{16}
 \end{aligned}
\]

El límite de los dos términos por separado no se usa. Integrando (1) y
usando (11),

\[
 \boxed{\mathscr J_n(a_0)=\mathcal B_{n,a_0}-B_n.}           \tag{17}
\]

Póngase

\[
 \kappa={1501\over2002}.
\]

Como \(H_n=\kappa A_n-B_n\), (17) da la equivalencia exacta

\[
 \boxed{
 H_n\ge0
 \quad\Longleftrightarrow\quad
 \mathscr J_n(a_0)\ge\mathcal B_{n,a_0}-\kappa A_n.}        \tag{18}
\]

La cota de fase de `104_41`,
\(|\mathcal B_{n,a_0}|\le3n\), controla el extremo Euler. Todo el contenido
RH-strength queda en el signo integrado de (16). En particular, una
desigualdad de flujo que pruebe (18) sería un cierre válido; pero (18)
demuestra que no es una consecuencia gratuita de haber encontrado la ley
diferencial.

La separación de canales tampoco es admisible. La parte polar de (10) es

\[
 \mathcal Q_{n,a}
 :=a\int_0^\infty e^{-(a-1)x}P_n(ax)\,dx
 =1-\left({-1\over a-1}\right)^n.                           \tag{19}
\]

Por (11), la parte prima posee la misma divergencia principal que (19) al
bajar \(a\) a uno. Cada canal tiene tamaño \((a-1)^{-n}\), mientras su
diferencia tiene límite finito. Markov o Jensen aplicados antes de la resta
destruyen precisamente la cancelación que define (16).

## 5. Integrar el flujo no vuelve positivos los pesos

Para \(a_1>1\), el canal primo de (16) puede integrarse término a término.
La identidad

\[
 {d\over dx}\{e^{-x}L_n^{(-1)}(x)\}=-e^{-x}L_n(x)           \tag{20}
\]

da

\[
 \begin{aligned}
 &\int_{a_1}^{a_0}{\Lambda(d)\over d^a}L_n(a\log d)\,da\\
 &\quad={\Lambda(d)\over\log d}
 \left\{d^{-a_1}L_n^{(-1)}(a_1\log d)
       -d^{-a_0}L_n^{(-1)}(a_0\log d)\right\}.              \tag{21}
 \end{aligned}
\]

Aquí

\[
 {\Lambda(p^k)\over\log(p^k)}={1\over k},                  \tag{22}
\]

de modo que la homotopía sí revela exactamente las torres primas, sin
mayorarlas. Pero

\[
 L_n^{(-1)}(x)=-{x\over n}L_{n-1}^{(1)}(x)                  \tag{23}
\]

cambia de signo \(n-1\) veces en \((0,\infty)\). Por tanto los coeficientes
positivos \(1/k\) de (22) no producen un signo término a término. Al hacer
\(a_1\downarrow1\), los canales de (21) y (19) divergen y solo su resta
renormalizada converge. La integración exacta reorganiza el gate; no lo
convierte en positividad.

## 6. El cuarteto se reconstruye mediante un pulso de flujo

Sea

\[
 \rho={4+2i\over5},\qquad
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\},       \tag{24}
\]

y \(Q_\rho(s)=\prod_{\eta\in\mathcal O(\rho)}(s-\eta)\). Para
cada cero ponga

\[
 z_{\eta,a}=1-{a\over\eta}.                                 \tag{25}
\]

La contribución de \(Q_\rho\) al coeficiente de la homotopía es

\[
 \boxed{
 q_{n,a}:=-n[z^n]\log Q_\rho\!\left({a\over1-z}\right)
 =\sum_{\eta\in\mathcal O(\rho)}(z_{\eta,a}^{-n}-1).}       \tag{26}
\]

Cada sumando satisface la misma ley que (1):

\[
 a\,\partial_a q_{n,a}=n(q_{n+1,a}-q_{n,a}).                \tag{27}
\]

Para \(a_0=4\), todos los \(z_{\eta,4}\) están fuera del disco unidad. Al
llegar a \(a=1\), los cuatro valores son

\[
 {i\over2},\quad-{i\over2},\quad-2i,\quad2i.                \tag{28}
\]

Por tanto, para \(n=152\),

\[
 \boxed{q_{152,1}=2(2^{152}+2^{-152})-4>2^{153}-4.}         \tag{29}
\]

Su flujo integrado es, exactamente,

\[
 152\int_1^4{q_{153,a}-q_{152,a}\over a}\,da
 =q_{152,4}-q_{152,1}.                                      \tag{30}
\]

El miembro derecho contiene el pulso exponencial negativo que impide
transportar una cota superior desde \(a=4\). A la vez,
\(Q_\rho(1/2+it)>0\), de modo que multiplicar la función completada por
\(Q_\rho^M\) no cambia su fase en la línea crítica. Las ecuaciones
(26)--(30) identifican el residuo de `104_41` como la combinación exacta
«extremo Euler menos flujo», no como el flujo aislado ni como un error de
borde: \(q_{n,1}=q_{n,4}-(q_{n,4}-q_{n,1})\).

El cuarteto no conserva el selector (6), de modo que una desigualdad que
use verdaderamente los pesos exactos puede y debe rechazarlo. Lo que (30)
refuta es cerrar la homotopía usando solo su ley diferencial y la fase del
extremo.

## 7. Por qué la positividad size-biased genérica tampoco basta

Hay un falsificador que sí conserva toda la maquinaria probabilística
genérica. Sea \(0<c<1/2\) y

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c)
       =\sum_{n\ge1}{a_c(n)\over n^s},\qquad a_c(n)>0.       \tag{31}
\]

Su derivada logarítmica tiene pesos positivos

\[
 -{Z_c'(s)\over Z_c(s)}
 =\sum_{d\ge2}{\omega_c(d)\over d^s},\qquad
 \omega_c(d)=2\Lambda(d)\cosh(c\log d)>0.                  \tag{32}
\]

Comparar coeficientes en \(-Z_c'=(-Z_c'/Z_c)Z_c\) da

\[
 (\log n)a_c(n)=\sum_{d\mid n}\omega_c(d)a_c(n/d).          \tag{33}
\]

Por tanto la ley de \(Z_c\) posee la misma factorización size-biased, con
selector fijo

\[
 K_c(n,d)={\omega_c(d)a_c(n/d)\over(\log n)a_c(n)}
             {\bf1}_{d\mid n}.                              \tag{34}
\]

También satisface la ley diferencial (1), que es una identidad de la
composición \(a/(1-z)\), en su dominio Euler \(a>1+c\). Esto refuta
inferencias que usan solo positividad/Markov local en ese dominio; no afirma
que el modelo conserve una ley probabilística positiva durante todo el
trayecto \(a\downarrow1\). Sin embargo,
\(\xi(s+c)\xi(s-c)\) tiene ceros a ambos lados de su línea de simetría.
Así, positividad de pesos, factorización size-biased, propiedad de Markov,
invariancia del selector bajo la inclinación y la ley de flujo no pueden,
por sí solas, implicar el margen.

La propiedad que (32) pierde y (3) conserva es la constancia exacta del
peso a lo largo de cada torre prima. Una desigualdad futura debe usar esa
rigidez cuantitativamente; usar solo \(\omega(d)\ge0\) repetiría el
falsificador.

## 8. Veredicto

Queda probado incondicionalmente:

1. la desintegración completa (9), con \(K\) y \(U\) independientes de la
   homotopía;
2. la ley diferencial exacta (1) y su densidad firmada (15);
3. la equivalencia exacta flujo--margen (18);
4. la fórmula de torre integrada (21)--(23);
5. la reconstrucción cero por cero del residuo mediante extremo Euler y
   pulso de flujo (26)--(30);
6. que la maquinaria size-biased genérica también existe para el
   falsificador off-line (31)--(34).

Queda descartado:

```text
fase segura en a>=4
+ ley diferencial en a
+ Markov/Jensen para el selector
=> cota proporcional en a=1.
```

El sucesor mínimo es una cota inferior para el funcional **ya acoplado** de
(16), válida para los pesos exactos \(\Lambda(p^k)=\log p\), uniforme en
\(n\ge150\), y falsa al sustituirlos por (32). Por (18), ése no es un lema
técnico auxiliar: es precisamente el teorema aritmético nuevo que cerraría
A1.

## 9. Verificación reproducible

El archivo
`tools/size_bias_homotopy_flux_gate_check.py` usa únicamente enteros y
`Fraction`. Verifica:

* las identidades polinómicas (12), (20) y (23);
* el flujo polar exacto (19);
* la ley cero por cero (27) en racionales gaussianos;
* los cuatro puntos (28), la identidad exacta (29) y el tamaño del pulso;
* que todos los puntos del cuarteto están fuera del círculo en \(a=4\).

Se reproduce con

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 size_bias_homotopy_flux_gate_check.py
```
