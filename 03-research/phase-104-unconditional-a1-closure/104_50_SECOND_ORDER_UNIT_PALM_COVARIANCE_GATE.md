# 104_50 — Palm unitario de segundo orden y gate de orientación

**Resultado.** El selector unitario de `104_49` admite una extensión
cuadrática exacta. Si la ley zeta se sesga por \((\log N)^2\) y,
condicionado a \(N\), se eligen dos marcas unitarias independientes, entonces

\[
 m_2(s)\,\mathbb E_s^{[2]}\{f(Z_1)g(Z_2)\}
 =\mathbb E_s\{J_f(N)J_g(N)\}.                              \tag{1}
\]

Aquí \(J_f\) conserva simultáneamente todos los primos y todas sus
potencias. Al centrar (1), sin embargo, las torres de primos distintos se
cancelan exactamente por independencia. Una forma de reintroducirlas sin
abandonar esta construcción es formar el defecto selector--continuo

\[
 D_f(N)=J_f(N)-\int_0^{\log N}f(x)\,dx.                    \tag{2}
\]

Este defecto sí contiene correlaciones entre torres distintas. El polo se
puede reinsertar sin separar canales, pero entonces la identidad bilineal
completa es

\[
 \boxed{\mathbb E_s[Z_fZ_g]
 =\mathrm{Cov}_s(D_f,D_g)+M_s(f)M_s(g),}              \tag{3}
\]

donde \(M_s(f)\) es exactamente el funcional prima--polo de `104_45`.
Para el test Laguerre fijo, \(sM_s(f_{n,s})=\mathcal B_{n,s}\to B_n\).
Por tanto el cuadrado completado alrededor del margen requerido vale

\[
 \boxed{
 s^2\mathbb E_s\left(Z_{f_{n,s}}-{\kappa A_n\over s}\right)^2
 =s^2\mathrm{Var}_s(D_{f_{n,s}})
  +(\mathcal B_{n,s}-\kappa A_n)^2,}
 \qquad \kappa={1501\over2002}.                             \tag{4}
\]

La energía de segundo orden pierde exactamente la orientación del margen:
no distingue \(\mathcal B_{n,s}-\kappa A_n\) de su opuesto. Polarizar con
dos tests diferentes tampoco ayuda automáticamente: solo reemplaza el
cuadrado por el producto de sus dos medias, como muestra (3). Los candidatos
Stein naturales, la derivada y la primitiva del Laguerre, producen productos
con otros coeficientes \(\mathcal B_{k,s}\) desconocidos, no un ancla de signo
conocido.

El gate es adversarialmente correcto. Una construcción Palm de segundo
orden análoga y toda conclusión basada solo en positividad de covarianza
también valen para

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c),                               \tag{5}
\]

que tiene coeficientes y pesos logarítmicos positivos, pero cuya completada
posee ceros fuera de la línea de simetría. Un ejemplo local completamente
exacto, \(p=5\), \(5^c=2\), exhibe ya el selector desplazado y su covarianza
positiva con probabilidades racionales. Por ello queda descartado cerrar A1
mediante **positividad/PSD de la covarianza Palm cuadrática**, incluso
conservando el test real y el polo. No queda descartada una desigualdad
firmada adicional que correlacione una covarianza condicional con una función
del entero total; eso sería un input de orden superior, no una consecuencia
de (1)--(4).

Este documento no prueba

\[
 B_n\le {1501\over2002}A_n,\qquad n\ge150,                  \tag{6}
\]

ni A1 ni RH.

## 0. Auditoría interna de no duplicación

`E101_089` §12 ya demuestra que tensorizar dos renovaciones produce en la
rebanada hermítica solamente \(|\zeta|^2\) y pierde el factor interior de
Hardy. No se reclama de nuevo ese no-go ni novedad general para Palm,
size-bias o covarianzas. `104_43`--`104_45` construyen la primera marca y el
Stein cruzado; `104_49` refina la marca a la altura uniforme dentro de cada
torre y prueba la cancelación lineal momento--cumulante.

Lo que se añade aquí es estrecho: la ley Palm cuadrática (9)--(10), la
diagonalización exacta (15)--(16), la covarianza multi-torre explícita del
defecto (23), el colapso bilineal con el presupuesto real (29), la auditoría
derivada/primitiva (30)--(34) y el test racional del divisor desplazado
(39)--(43).

## 1. Segunda ley de Palm del selector unitario

Fijemos \(s=1+\varepsilon>1\) y

\[
 \mathbb P_s(N=n)={n^{-s}\over\zeta(s)},\qquad
 N=\prod_p p^{A_p},\qquad X=\log N.                        \tag{7}
\]

Para una función de crecimiento polinómico, póngase

\[
 \boxed{
 J_f(n)=\sum_{p^{a_p}\parallel n}(\log p)
              \sum_{k=1}^{a_p}f(k\log p)
       =\sum_{d\mid n}\Lambda(d)f(\log d).}                \tag{8}
\]

En particular, la renovación unitaria da \(J_1(n)=\log n=X\). Sean

\[
 m_j(s)=\mathbb E_sX^j,\qquad
 \mathbb P_s^{[2]}(N^{[2]}=n)
 ={(\log n)^2n^{-s}\over\zeta(s)m_2(s)}.                  \tag{9}
\]

Condicionado a \(N^{[2]}=n\), elija independientemente \(Z_1,Z_2\) en el
multiconjunto

\[
 \mathcal M(n)=\{(p,k):p^{a_p}\parallel n,\ 1\le k\le a_p\}
\]

mediante

\[
 \boxed{
 \mathbb P(Z_i=k\log p\mid n)={\log p\over\log n}.}       \tag{10}
\]

La suma de (10) es uno por \(\sum_pa_p\log p=\log n\). Además,

\[
 (\log n)^2\mathbb E\{f(Z_1)g(Z_2)\mid n\}=J_f(n)J_g(n).
\]

Promediar con (9) prueba (1). No se ha reemplazado una torre por su primer
nivel ni se han separado los otros primos.

El comparador polar es igualmente exacto. Si \(Y\sim\mathrm{Exp}
(\varepsilon)\) y

\[
 C_f(Y)=\int_0^Y f(x)\,dx,                                  \tag{11}
\]

entonces \(\mathbb EY^2=2/\varepsilon^2\). Sesgar por \(Y^2\) da
\(Y^{[2]}\sim\Gamma(3,\varepsilon)\); condicionado a \(Y^{[2]}=y\),
elija \(U_1,U_2\) independientemente y uniformes en \([0,y]\). Se obtiene

\[
 {2\over\varepsilon^2}\mathbb E\{f(U_1)g(U_2)\}
 =\mathbb E\{C_f(Y)C_g(Y)\}.                               \tag{12}
\]

## 2. Qué ocurre al centrar: diagonalización por torre

De \(\mathbb P_s(A_p\ge k)=p^{-ks}\),

\[
 \mu_s^\Lambda(f):=\mathbb E_sJ_f
 =\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d).              \tag{13}
\]

La probabilidad de que dos potencias primas dividan simultáneamente a
\(N\) es

\[
 \mathbb P_s(d\mid N,\ e\mid N)=\mathrm{lcm}(d,e)^{-s}.
\]

Por tanto (1) posee la forma cerrada

\[
 \mathbb E_s[J_fJ_g]
 =\sum_{d,e\ge2}{\Lambda(d)\Lambda(e)\over
             \mathrm{lcm}(d,e)^s}f(\log d)g(\log e). \tag{14}
\]

Al sustraer el producto de medias,

\[
\begin{aligned}
 \Gamma_s^\Lambda(f,g)
 :={}&\mathrm{Cov}_s(J_f,J_g)\\
 ={}&\sum_{d,e\ge2}\Lambda(d)\Lambda(e)f(\log d)g(\log e)
 \{\mathrm{lcm}(d,e)^{-s}-d^{-s}e^{-s}\}.           \tag{15}
\end{aligned}
\]

Como \(\Lambda\) está soportada en potencias primas, el corchete de (15)
es cero si \(d\) y \(e\) pertenecen a torres distintas. Así

\[
 \boxed{
 \Gamma_s^\Lambda(f,g)
 =\sum_p(\log p)^2\sum_{k,l\ge1}f(k\ell_p)g(l\ell_p)
 \{p^{-s\max(k,l)}-p^{-s(k+l)}\},}                         \tag{16}
\]

donde \(\ell_p=\log p\). La forma es PSD, pues es la covarianza de los
observables aditivos \(J_f,J_g\) bajo la ley base, pero es una suma directa
de formas de una sola torre. No se afirma aquí que (15) sea la covarianza
de \(Z_1,Z_2\) bajo la ley sesgada: sus marginales sesgadas son distintas.
En particular, la forma centrada canónica inducida por (1) **no** puede ser
el mecanismo global multi-torre buscado.

El lado continuo tiene exactamente la misma estructura de cola:

\[
 \boxed{
 \Gamma_\varepsilon^0(f,g)
 =\int_0^\infty\!\int_0^\infty f(x)g(y)
 \{e^{-\varepsilon\max(x,y)}-e^{-\varepsilon(x+y)}\}
 \,dx\,dy.}                                                \tag{17}
\]

Tanto (16) como (17) son PSD por separado. Su diferencia no posee signo.
Por ejemplo, un test no nulo soportado dentro de
\((0,\log2)\) anula (16) y hace (17) estrictamente positiva; un test
concentrado en torno a un único nivel primo hace aparecer el signo opuesto
en la diferencia. Esta observación solo descarta un orden operatorial; el
test de A1 se trata sin localización en la sección siguiente.

## 3. Covarianza que sí conserva torres distintas y polo

Defina

\[
 U_f(x)=\int_0^x f(t)\,dt,\qquad
 D_f(N)=J_f(N)-U_f(X),                                     \tag{18}
\]

y el transporte determinista entre la ley total zeta y el polo

\[
 T_s(f)=\mathbb E_sU_f(X)-\mathbb E U_f(Y).                 \tag{19}
\]

Finalmente póngase

\[
 Z_f=D_f+T_s(f),\qquad
 M_s(f)=\mu_s^\Lambda(f)-\int_0^\infty e^{-\varepsilon x}f(x)\,dx.
                                                                    \tag{20}
\]

Entonces

\[
 \mathbb E_sZ_f=M_s(f).                                    \tag{21}
\]

La variable \(D_f\) es precisamente el defecto unitario condicionado de
`104_49`; a diferencia de (16), su covarianza contiene el entero producto
completo. En efecto, para cualquier \(h\), la identidad de Mecke divisora
es

\[
 \boxed{
 \mathbb E_s\{J_f(N)h(X)\}
 =\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
       \mathbb E_s h(X+\log d).}                            \tag{22}
\]

Usando (14) y (22),

\[
\begin{aligned}
 \mathbb E_s[D_fD_g]={}&
 \sum_{d,e\ge2}{\Lambda(d)\Lambda(e)\over
    \mathrm{lcm}(d,e)^s}f(\log d)g(\log e)\\
 &-\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
       \mathbb E_sU_g(X+\log d)\\
 &-\sum_{e\ge2}{\Lambda(e)\over e^s}g(\log e)
       \mathbb E_sU_f(X+\log e)
 +\mathbb E_s\{U_f(X)U_g(X)\}.                            \tag{23}
\end{aligned}
\]

Los tres últimos términos de (23) retienen las interacciones entre todas
las torres a través de la ley de \(X\). Esta es la identidad de segundo
orden que no estaba en `104_49`.

Ahora centre (21). Para **todo par** de tests admisibles,

\[
\begin{aligned}
 \mathbb E_s[Z_fZ_g]
 &=\mathrm{Cov}_s(Z_f,Z_g)+\mathbb E_sZ_f\,\mathbb E_sZ_g\\
 &=\boxed{\mathrm{Cov}_s(D_f,D_g)+M_s(f)M_s(g).}      \tag{24}
\end{aligned}
\]

La segunda igualdad usa que \(T_s(f),T_s(g)\) son deterministas. Esta es
la identidad bilineal general: ninguna elección de polarización evita el
producto de las dos medias.

## 4. Test Laguerre fijo y auditoría de derivada/primitiva

Sea

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad f_{n,s}(x)=P_n(sx).          \tag{25}
\]

Entonces

\[
 U_{f_{n,s}}(X)={1-L_n(sX)\over s}                         \tag{26}
\]

y

\[
 \boxed{
 D_{n,s}(N)=
 \sum_{p^{a_p}\parallel N}(\log p)
       \sum_{k=1}^{a_p}P_n(sk\log p)
 -{1-L_n(s\log N)\over s}.}                               \tag{27}
\]

Este es exactamente el defecto \(\Delta_{n,s}\) de `104_49`, sin tomar
signos término a término. Además,

\[
 \boxed{sM_s(f_{n,s})=\mathcal B_{n,s},\qquad
        \mathcal B_{n,s}\longrightarrow B_n.}             \tag{28}
\]

Sustituir (28) en (24), primero con \(f=g=f_{n,s}\) y luego desplazando
por el presupuesto determinista \(\kappa A_n/s\), prueba (4). Más
generalmente,

\[
\begin{aligned}
 &s^2\mathbb E_s
 \left(Z_{f_{n,s}}-{\kappa A_n\over s}\right)
 \left(Z_{f_{m,s}}-{\kappa A_m\over s}\right)\\
 &\quad=s^2\mathrm{Cov}_s(D_{n,s},D_{m,s})
 +(\mathcal B_{n,s}-\kappa A_n)
  (\mathcal B_{m,s}-\kappa A_m).                           \tag{29}
\end{aligned}
\]

Por tanto la polarización solo produce productos de márgenes. Para
descartar los dos anclajes Stein más naturales, usamos las identidades

\[
 f'_{n,s}(x)=-s\sum_{k=1}^{n-1}f_{k,s}(x),                  \tag{30}
\]

\[
 U_{f_{n,s}}(x)={f_{1,s}(x)-f_{n+1,s}(x)+f_{n,s}(x)\over s}.
                                                                    \tag{31}
\]

Por linealidad de \(M_s\),

\[
 \boxed{
 M_s(f'_{n,s})=-\sum_{k=1}^{n-1}\mathcal B_{k,s},\qquad
 M_s(U_{f_{n,s}})
 ={\mathcal B_{1,s}-\mathcal B_{n+1,s}+\mathcal B_{n,s}\over s^2}.}
                                                                    \tag{32}
\]

Así, polarizar con la derivada introduce el producto de
\(\mathcal B_{n,s}\) con una suma de coeficientes anteriores; polarizar
con la primitiva introduce el producto con una diferencia adyacente.
Ninguno es un término lineal de signo conocido.

La única ancla elemental con media conocida es \(f\equiv1\). En ese caso

\[
 D_1=J_1-X=0,\qquad Z_1=M_s(1)=R(\varepsilon)<0,            \tag{33}
\]

y (24) se reduce a

\[
 \mathbb E_s[Z_fZ_1]=R(\varepsilon)M_s(f).                 \tag{34}
\]

La ecuación (34) recupera orientación solo porque su lado izquierdo ya
es el funcional buscado multiplicado por el escalar conocido
\(R(\varepsilon)\): probarle el signo requerido es exactamente probar el
signo de \(M_s(f)\). No aparece una desigualdad de covarianza, pues
\(Z_1\) es constante. Esto cierra la auditoría derivada/primitiva/ancla.

Hay otra polarización orientada natural: usar como segundo test el score
total \(X=\log N\). Para un test \(f\) independiente de \(s\), derivar la
familia exponencial y usar el comparador continuo da

\[
 \boxed{
 \mathrm{Cov}_s(J_f,X)
 -\mathrm{Cov}_\varepsilon(C_f(Y),Y)
 =-\partial_sM_s(f).}                                      \tag{34a}
\]

En efecto, \(\partial_s\mathbb E_sJ_f=-\mathrm{Cov}_s(J_f,X)\),
mientras

\[
 \mathrm{Cov}_\varepsilon(C_f(Y),Y)
 =\int_0^\infty xe^{-\varepsilon x}f(x)\,dx.
\]

Si el test depende de \(s\), el miembro derecho de (34a) se reemplaza por

\[
 M_s(\partial_sf_s)-\partial_sM_s(f_s).                    \tag{34b}
\]

Para \(f_{n,s}=P_n(s\,\cdot)\), (34b) es exactamente otra escritura de
la ley de flujo ya probada en `104_47`,

\[
 s\,\partial_s\mathcal B_{n,s}
 =n(\mathcal B_{n+1,s}-\mathcal B_{n,s}).                  \tag{34c}
\]

Por tanto el score sí conserva una cantidad lineal orientada, pero es la
derivada exacta del funcional de primer orden. Integrarla recompone
\(\mathcal B_{n,s}\) y sus residuos; no aporta una desigualdad adicional.

## 5. Falsificador desplazado que pasa el gate PSD cuadrático

La identidad (24) es todavía más general. Sea

\[
 Z(s)=\sum_{n\ge1}{a(n)\over n^s},\qquad a(n)>0,
\]

y suponga la renovación positiva

\[
 (\log n)a(n)=\sum_{d\mid n}\omega(d)a(n/d).               \tag{35}
\]

Defina

\[
 J_f^Z(n)={1\over a(n)}\sum_{d\mid n}
       \omega(d)a(n/d)f(\log d).                            \tag{36}
\]

Entonces \(J_1^Z(n)=\log n\), y el Palm aritmético (9)--(10) y el
álgebra bilineal (18)--(24) se repiten con la ley
\(a(n)n^{-s}/Z(s)\). El comparador continuo se sustituye por los polos
reales del sistema. Para (37), si
\(\varepsilon_\pm=s-1\mp c\), se toma exactamente

\[
 T_{s,c}(f)=\mathbb E_{s,c}U_f(X)
 -\int_0^\infty\{e^{-\varepsilon_-x}
                 +e^{-\varepsilon_+x}\}f(x)\,dx.           \tag{36a}
\]

Cada uno de los dos sumandos polares posee por separado la construcción
Gamma de (11)--(12), y la identidad (24) sigue siendo puramente algebraica.
En particular, toda positividad de covarianza Palm es una consecuencia
genérica de (35), no de la ubicación de los ceros.

Tome ahora

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c),\qquad 0<c<{1\over2}.          \tag{37}
\]

Sus coeficientes son positivos y

\[
 \omega_c(d)=2\Lambda(d)\cosh(c\log d)>0                  \tag{38}
\]

satisface (35). Por tanto su segundo Palm, su matriz de covarianza y la
identidad bilineal (24) son todos válidos en \(s>1+c\).

La diferencia con el selector unitario puede verse con racionales. Elija

\[
 p=5,\qquad 5^c=2,\qquad s=2.                             \tag{39}
\]

Como \(2<\sqrt5\), se tiene \(0<c<1/2\). Para el factor local desplazado,
con \(r=5^c=2\),

\[
 b_1=r+r^{-1}={5\over2},\qquad
 b_2=r^2+1+r^{-2}={21\over4}.                              \tag{40}
\]

Condicionado al exponente total dos, (35) da

\[
 \boxed{\pi(1)={25\over42},\qquad \pi(2)={17\over42}.}     \tag{41}
\]

En particular,

\[
 \mathrm{Var}(K\mid A=2)
 ={25\cdot17\over42^2}={425\over1764}>0,                  \tag{42}
\]

mientras el selector unitario da \(1/4=441/1764\). El segundo orden
detecta cuantitativamente que la marca desplazada no es uniforme, pero su
conclusión automática sigue siendo solo PSD, y (42) la satisface. En la
representación latente de dos colores, los parámetros geométricos locales
son

\[
 q_-={2\over25},\qquad q_+={1\over50},                     \tag{43}
\]

y la covarianza del **score coloreado antes de condicionar por el exponente
total** es la suma de dos kernels PSD de la forma (16). Para un test general,
la covarianza del selector condicionado \(J_f^Z\) no es igual a esa suma:
por varianza total es menor o igual en la diagonal, y la diferencia es la
varianza condicional perdida. La desigualdad puede ser estricta: para
\(f(k\log p)=k\), condicionado a exponente total dos, el score latente toma
los valores \(3,2,3\) en las particiones \((0,2),(1,1),(2,0)\), todas de
probabilidad positiva. La conclusión necesaria aquí es solo que ambas
covarianzas son PSD; no se usa una igualdad entre ellas.

Finalmente, la completada

\[
 \Xi_c(s)=\xi(s+c)\xi(s-c)                                 \tag{44}
\]

es simétrica respecto de \(1/2\) y posee ceros
\(1/2\pm c+i\gamma\) fuera de esa línea. Para un cuarteto exterior,
si \(1-1/\rho=e^{\alpha+i\theta}\), su respuesta de Li es

\[
 4-4\cosh(n\alpha)\cos(n\theta).                           \tag{45}
\]

Si \(R>1\) es el módulo exterior máximo y su multiconjunto dominante tiene
cardinal \(M\), la aproximación simultánea de Dirichlet da infinitos grados
con

\[
 \lambda_n[\Xi_c]\le-{M\over2}R^n.                         \tag{46}
\]

Así, una inferencia que use solo (35), Palm de segundo orden y PSD
probaría también una conclusión cuantitativamente falsa para (44). La
igualdad especial de uniformidad puede excluir (41), pero una vez convertida
solamente en covarianza positiva pierde esa distinción de signo.

## 6. Veredicto

Queda probado incondicionalmente:

1. el Palm unitario de segundo orden (1), (9)--(10);
2. la forma cerrada de covarianza (14)--(17);
3. la cancelación exacta entre torres distintas al centrar \(J_f\);
4. la identidad multi-torre del defecto (22)--(23);
5. la identidad bilineal completada (24) y su especialización al margen
   Laguerre (4), (29);
6. el colapso explícito de las polarizaciones derivada y primitiva (32);
7. el colapso de la polarización con el score al flujo conocido
   (34a)--(34c);
8. el gate desplazado racional (39)--(43).

Queda descartado:

```text
segunda ley de Palm
+ PSD/covarianza del selector unitario
+ cuadrado o polarización del defecto completado
    => cota unilateral B_n <= (1501/2002) A_n.
```

El sucesor que no queda refutado debe conservar la **orientación** antes
de centrar: por ejemplo, una correlación firmada entre la varianza
condicional de la marca uniforme y una función no constante del entero
total. Debe usar la igualdad exacta de uniformidad, no solo su consecuencia
PSD, y fallar para (41). Tal correlación es de orden superior al mecanismo
auditado aquí.

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 second_order_unit_palm_covariance_check.py
```

El checker usa solo enteros, `Fraction` y polinomios racionales. Verifica
la identidad Palm condicionada, la cancelación entre torres distintas en
(15), las identidades Laguerre (26), (30)--(31), la descomposición
bilineal (24), el selector desplazado (40)--(42) y la positividad exacta
de los kernels locales racionales (43). No evalúa zeta, A1 ni RH.
