# 104_43 — Size-bias zeta, selector divisor y gate martingala

**Rol.** Explotar la identidad especial

\[
 \log n=\sum_{d\mid n}\Lambda(d)
\]

antes de separar primos, potencias primas y polo. La ley zeta posee una
factorización size-biased exacta: al sesgar por \(\log N\), se obtiene
\(N^\star=DN'\), donde \(N'\) vuelve a tener la ley zeta y \(D\) tiene
exactamente los pesos \(\Lambda(d)d^{-s}\). Condicionado a
\(N^\star=n\), el divisor \(D\) se elige con probabilidad
\(\Lambda(d)/\log n\). El comparador polar es la factorización continua
\(\Gamma(2,\varepsilon)=\operatorname{Exp}(\varepsilon)+
\operatorname{Exp}(\varepsilon)\), cuyo selector condicionado es uniforme
en el intervalo logarítmico.

La factorización es exacta y conserva simultáneamente todas las potencias
primas y todos los demás primos. Sin embargo:

1. el selector divisor no domina ni es dominado por el selector uniforme,
   ya para el test lineal y los enteros reales \(2\) y \(30\);
2. comparar las dos leyes seleccionadas por transformada de Laplace da
   **exactamente**
   \(R(t)=-\zeta'/\zeta(1+t)-1/t\), es decir, el gate escalar ya abierto;
3. Efron--Stein aplicado por separado a la ley zeta pierde la cancelación
   Abel: para el test Laguerre de grado \(n-1\), su energía diverge al menos
   como
   \(\{\binom{2n-2}{n-1}-1\}\varepsilon^{-2n+2}\).

Por tanto queda descartado cerrar el margen mediante orden condicional,
data processing o una energía tensorizada positiva aplicada separadamente.
No queda descartada una desigualdad **firmada y acoplada** específica para
la diferencia selector-divisor/selector-uniforme; por la identidad de
transformadas, producirla sería precisamente nuevo contenido aritmético.
Este documento no prueba \(H_n\ge0\), A1 ni RH.

La normalización del frente es

\[
 H_n=\lambda_n-{501\over2002}A_n,
 \qquad
 {2002\over501}H_n=r_*\lambda_n-A_n,
 \qquad r_*={2002\over501}.                                   \tag{0}
\]

Por tanto una cota unilateral para el generador completado con exponente
\(r_*\) cerraría el target; ninguna de las contracciones probadas abajo
aporta esa cota.

## 1. Auditoría interna de no duplicación

`104_16` ya prueba que el cociclo Jordan positivo pierde el signo al
emparejarse con el polo. `104_20` conserva torres completas, pero su cuadrado
local no es una norma. `104_21` construye la ley compound-Poisson global y
su identidad de Mecke. `104_24` aplica Stein--Mecke al cociclo completado y
obtiene un generador firmado. `104_29` demuestra que partir en \(\log2\)
recompone exactamente el margen buscado.

Lo que no estaba escrito en esos documentos es la desintegración
size-biased sobre el **entero producto** \(N^\star\), con el kernel

\[
 K(n,d)={\Lambda(d)\over\log n}{\bf1}_{d\mid n},                 \tag{1}
\]

ni su comparación exacta con el split uniforme del polo. La identidad es
la versión de divisor de Mecke, no una fuente adicional de positividad. No
se reclama novedad bibliográfica para la teoría general de size-bias o para
Efron--Stein.

## 2. Ley zeta y factorización size-biased exacta

Fijemos \(s=1+\varepsilon>1\) y sea

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad m\ge1.           \tag{2}
\]

En el producto de Euler,

\[
 N=\prod_p p^{K_p},\qquad
 \mathbb P(K_p=k)=(1-p^{-s})p^{-ks},\quad k\ge0,               \tag{3}
\]

y los \(K_p\) son independientes. Pongamos

\[
 \mathfrak m(s):=\mathbb E_s\log N
 =-{\zeta'\over\zeta}(s)
 =\sum_{d\ge2}{\Lambda(d)\over d^s}>0.                         \tag{4}
\]

La ley sesgada por \(\log N\) es

\[
 \mathbb P_s^\star(N^\star=m)
 ={(\log m)m^{-s}\over-\zeta'(s)},\qquad m\ge2.               \tag{5}
\]

**Teorema 2.1 (factorización divisor--cofactor).** Sean independientes

\[
 \mathbb P_s(D=d)={\Lambda(d)d^{-s}\over\mathfrak m(s)},
 \qquad
 \mathbb P_s(N'=k)={k^{-s}\over\zeta(s)}.                     \tag{6}
\]

Entonces

\[
 \boxed{N^\star\ \buildrel d\over=\ DN'.}                    \tag{7}
\]

Además, para cada \(n\ge2\),

\[
 \boxed{
 \mathbb P(D=d\mid DN'=n)
 ={\Lambda(d)\over\log n}{\bf1}_{d\mid n}.}                  \tag{8}
\]

*Demostración.* La masa conjunta en \((d,k)\) es

\[
 {\Lambda(d)d^{-s}\over\mathfrak m(s)}
 {k^{-s}\over\zeta(s)}
 ={\Lambda(d)(dk)^{-s}\over-\zeta'(s)}.                       \tag{9}
\]

Sumar (9) sobre \(dk=n\) y usar
\(\sum_{d\mid n}\Lambda(d)=\log n\) produce (5) y (7).
Dividir (9) por la masa resultante de \(n\) produce (8). \(\square\)

En coordenadas aditivas,

\[
 X=\log N',\qquad Y=\log D,\qquad S=\log N^\star=X+Y,          \tag{10}
\]

con \(X\) e \(Y\) independientes. Toda la interacción entre distintos
primos permanece dentro de la ley de \(S\); no se ha agrupado torre a
torre ni tomado valores absolutos.

## 3. Comparador polar y selector uniforme

Sea \(Y_0\sim\operatorname{Exp}(\varepsilon)\). Su sesgo por el valor es
\(S_0^\star\sim\Gamma(2,\varepsilon)\), y admite la factorización

\[
 S_0^\star=Y_0+Y_0',                             \tag{11}
\]

con dos exponenciales independientes de tasa \(\varepsilon\). Condicionado
a \(S_0^\star=x\), la variable seleccionada \(Y_0\) es uniforme en
\([0,x]\). Por tanto el análogo continuo de (1) es

\[
 (Uf)(x)={1\over x}\int_0^x f(y)\,dy.                         \tag{12}
\]

En el lado aritmético, si \(L=\log n\), (8) da

\[
 (Kf)(n)={1\over L}\sum_{d\mid n}\Lambda(d)f(\log d).        \tag{13}
\]

Las dos identidades de conservación de la media son

\[
 \mathbb E_s^\star Kf(N^\star)=\mathbb E_s f(Y),
 \qquad
 \mathbb E\,Uf(S_0^\star)=\mathbb E f(Y_0).                   \tag{14}
\]

Jensen condicional da data processing, por ejemplo

\[
 \operatorname{Var}_{\mathbb P_s^\star}(Kf)
 \le \operatorname{Var}_{\mathbb P_s(D)}(f),                 \tag{15}
\]

y la desigualdad análoga para \(U\). Es una contracción de la parte
centrada. La constante --la media de \(f\)-- pasa sin cambio por (14), y
es precisamente la componente que aparece en la suma prima--polo. Por ello
(15), por sí sola, no puede fijar su signo.

## 4. El selector discreto no posee orden unilateral

La falla ocurre antes de usar un Laguerre. Para \(f(y)=y\), si
\(n=\prod_p p^{a_p}\) y \(L=\log n\), entonces

\[
 (Kf)(n)
 ={1\over2L}\sum_{p^{a_p}\parallel n}
     a_p(a_p+1)(\log p)^2,\qquad
 (Uf)(L)={L\over2}.                                             \tag{16}
\]

En consecuencia,

\[
 \boxed{
 2L\{(Kf)(n)-(Uf)(L)\}
 =\sum_p a_p(a_p+1)(\log p)^2-L^2.}                            \tag{17}
\]

Para \(n=2\), (17) vale \((\log2)^2>0\). Para \(n=30\), escribamos
\(a=\log2\), \(b=\log3\), \(c=\log5\). El lado derecho es

\[
 a^2+b^2+c^2-2ab-2ac-2bc=(a+b-c)^2-4ab<0.                     \tag{18}
\]

La última desigualdad no es numérica: como

\[
 0<a+b-c=\log(6/5)<\log2=a,
\]

se tiene

\[
 (a+b-c)^2-4ab<a^2-4ab=a(a-4b)<0.                             \tag{19}
\]

Por tanto no existe un acoplamiento condicionado a \(S=L\) que coloque
siempre al divisor seleccionado por encima del uniforme, ni uno que lo
coloque siempre por debajo. En particular fallan ambos órdenes estocásticos
condicionales y cualquier orden convexo que ya ordene las funciones
lineales. Una comparación global, después de promediar en \(n\), no queda
refutada por (18); necesitaría cancelación entre factorizaciones distintas.

## 5. La comparación marginal es exactamente \(R\)

Para un test polinómico \(f\), definamos el funcional prima--polo
emparejado

\[
 \mathfrak M_\varepsilon(f)
 :=\mathfrak m(1+\varepsilon)\,\mathbb E f(Y)
   -{1\over\varepsilon}\mathbb E f(Y_0).                       \tag{20}
\]

Por (6) y la densidad exponencial,

\[
 \boxed{
 \mathfrak M_\varepsilon(f)
 =\sum_{d\ge2}{\Lambda(d)\over d^{1+\varepsilon}}f(\log d)
  -\int_0^\infty e^{-\varepsilon x}f(x)\,dx.}                 \tag{21}
\]

Al tomar \(f_t(x)=e^{-tx}\), se obtiene

\[
\begin{aligned}
 \mathfrak M_\varepsilon(f_t)
 &=\mathfrak m(1+\varepsilon+t)-{1\over\varepsilon+t}\\
 &=\boxed{R(\varepsilon+t)},                                  \tag{22}
\end{aligned}

donde

\[
 R(q)=-{\zeta'\over\zeta}(1+q)-{1\over q}.                   \tag{23}
\]

Esto identifica sin resto el error del acoplamiento size-biased. Si

\[
 L_n(x)=\sum_{j=0}^n{n\choose j}{(-x)^j\over j!},              \tag{24}
\]

derivar (22) en \(t=0\) da

\[
 \boxed{
 \mathfrak M_\varepsilon(L_n)
 =\sum_{j=0}^n{n\choose j}{R^{(j)}(\varepsilon)\over j!}.}     \tag{25}
\]

En el límite \(\varepsilon\downarrow0\), (25) es exactamente el
coeficiente binomial \(C_n\) de `104_03`, y

\[
 C_n=\Delta A_n-\Delta\lambda_n.                              \tag{26}
\]

Usar \(L_{n-1}^{(1)}-n\) en (21), y añadir la densidad Gamma explícita,
da el generador compensado de `104_29`. Así, la desintegración por divisores
no reemplaza el gate: su error de comparación es su función generatriz
escalar exacta.

## 6. Stop-gate cuantitativo de Efron--Stein

La independencia (3) permite una energía tensorizada genuina. Sea
\(K_p'\) una copia independiente de \(K_p\), sea

\[
 X_\varepsilon=\log N,\qquad
 X_\varepsilon^{(p)}
 =X_\varepsilon-(\log p)K_p+(\log p)K_p',                     \tag{27}
\]

y defínase

\[
 \mathcal E_\varepsilon(f)
 ={1\over2}\sum_p\mathbb E
  \{f(X_\varepsilon)-f(X_\varepsilon^{(p)})\}^2.             \tag{28}
\]

Para todo polinomio fijo, la serie converge cuando \(\varepsilon>0\), y
Efron--Stein, primero sobre un número finito de primos y luego por límite,
da

\[
 \operatorname{Var}f(X_\varepsilon)
 \le\mathcal E_\varepsilon(f).                               \tag{29}
\]

La Laurent de zeta en uno implica, para cada \(k\ge1\),

\[
 \mathbb E X_\varepsilon^k
 ={(-1)^k\zeta^{(k)}(1+\varepsilon)\over
    \zeta(1+\varepsilon)}
 =k!\,\varepsilon^{-k}\{1+O_k(\varepsilon)\}.                \tag{30}
\]

Pongamos

\[
 \varphi_n(x)=L_{n-1}^{(1)}(x)-n,\qquad d=n-1.                 \tag{31}
\]

Su coeficiente líder es \((-1)^d/d!\). Usando (30) en los dos momentos
líderes,

\[
 \boxed{
 \operatorname{Var}\varphi_n(X_\varepsilon)
 =\left\{{2d\choose d}-1+O_n(\varepsilon)\right\}
   \varepsilon^{-2d}.}                                        \tag{32}
\]

Por (29), la energía positiva (28) es al menos del orden de (32). Para
todo \(n\ge2\), y en particular para \(n\ge150\), diverge cuando se retira
el regulador. El comparador exponencial tiene la misma escala principal.
La diferencia prima--polo de (21), en cambio, tiene límite Abel finito por
(22).

Así, aplicar Cauchy--Schwarz/Poincaré a cada canal antes de restarlos cambia
un objeto finito por dos energías de tamaño
\(\varepsilon^{-2n+2}\). No es una pérdida de constante: elimina la
cancelación que define el funcional. Este argumento no descarta una energía
**cruzada** construida sobre un acoplamiento de las dos leyes; (18) prueba
que el acoplamiento cruzado no puede basarse en un orden monótono del
selector canónico.

### 6.1. El escalado \(L_n(\varepsilon x)\) no recupera el coeficiente

Hay un escape aparente de (32): bajo la ley zeta,
\(\varepsilon X_\varepsilon\) converge con todos sus momentos a una
exponencial de tasa uno. Por ello un test escalado como
\(L_n(\varepsilon x)\) tiene norma acotada. Pero (22) muestra exactamente
qué información retiene:

\[
 \boxed{
 \mathfrak M_\varepsilon\bigl(L_n(\varepsilon\,\cdot)\bigr)
 =\sum_{j=0}^n{n\choose j}{\varepsilon^jR^{(j)}(\varepsilon)\over j!}.}
                                                                    \tag{33}
\]

Como \(R\) es analítica en cero, (33) tiende a \(R(0)\); si se resta el
término constante del test, tiende a cero. El coeficiente sin amortiguar es,
en cambio,

\[
 C_n=\sum_{j=0}^n{n\choose j}{R^{(j)}(0)\over j!}.                \tag{34}
\]

En (33), la diagonal que transporta \(R^{(j)}\) lleva el factor
\(\varepsilon^j\). Invertir esa transformación triangular para recuperar
el jet de orden \(n\) exige un factor \(\varepsilon^{-n}\); al cuadrarlo
reaparece \(\varepsilon^{-2n}\), la escala de la energía del test no
escalado del mismo grado. Por tanto el test
escalado controla una media Abel/triangular, no el coeficiente individual.

Esto es consistente con tres stop-gates previos: `104_17` prueba que la
positividad Abel no controla los coeficientes; `104_18` prueba que conservar
un shift correlacionado finito vuelve al mismo \(C_n\) al retirar el
regulador; `104_31` localiza la pérdida de observabilidad al invertir el
flujo en \(\varepsilon\). Aquí no se afirma un no-go para toda familia de
tests dependiente de \(\varepsilon\), sino para el rescate directo mediante
el escalado que mantiene acotada la energía.

## 7. Falsificador off-line

La maquinaria probabilística genérica tampoco distingue por sí sola la
línea crítica. Para \(a>0\), la parte Euler de

\[
 X_a(s)=\xi(s+a)\xi(s-a)                                      \tag{35}
\]

es el producto de dos leyes zeta independientes, con exponentes geométricos
de parámetros \(p^{-(s+a)}\) y \(p^{-(s-a)}\). Su derivada logarítmica tiene
pesos positivos

\[
 2\Lambda(m)\cosh(a\log m),                                  \tag{36}
\]

y admite las mismas identidades de size-bias, un selector análogo con esos
pesos, data processing y Efron--Stein. Sin embargo, como prueba `104_16`,
\(X_a\) tiene ceros fuera de su línea de simetría.

Por ello una inferencia que use únicamente independencia geométrica,
positividad de los saltos y una desigualdad tensorizada también se aplicaría
al falsificador (35). Una prueba válida debe usar cuantitativamente los
pesos exactos \(\Lambda(p^k)=\log p\) en la **diferencia firmada** (21), y
debe dejar de ser válida al reemplazarlos por (36).

## 8. Decisión y sucesor

Queda probado incondicionalmente:

1. la factorización size-biased exacta (7)--(8);
2. su comparador polar como split uniforme (11)--(12);
3. data processing sin pérdida de primos (15);
4. el cambio de signo real del selector frente al uniforme (17)--(19);
5. la identidad exacta del error con \(R\) (22)--(26);
6. la pérdida de escala de la energía Efron--Stein separada (32).

Quedan descartados:

```text
orden unilateral divisor <-> uniforme;
data processing de la media -> signo prima-polo;
Poincare/Efron--Stein por canales separados -> limite Abel finito;
tensorizacion positiva generica -> margen H_n.
```

El único sucesor que esta coordenada deja vivo es una desigualdad cruzada
firmada para

\[
 \mathfrak m(1+\varepsilon)\,\mathbb E f(Y)
 -\varepsilon^{-1}\mathbb E f(Y_0),                            \tag{37}
\]

con \(f=L_{n-1}^{(1)}-n\), conservando después el término Gamma y el límite
Abel. Por (22), esa desigualdad debe aportar información que no sea una
mera contracción probabilística: la transformada de (37) sobre los tests
exponenciales ya es \(R\) en coordenadas size-biased.

## 9. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 zeta_size_bias_martingale_gate_check.py
```

El checker usa aritmética entera y `Fraction`. Verifica la identidad formal
del selector divisor, los signos opuestos de (17) en \(2\) y \(30\), y las
constantes enteras de (32) para \(2\le n\le50\). No evalúa zeta, A1 ni RH.
