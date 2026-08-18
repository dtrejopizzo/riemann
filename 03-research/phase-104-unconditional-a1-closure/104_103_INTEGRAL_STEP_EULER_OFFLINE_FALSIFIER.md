# 104_103 — Falsificador Euler entero-escalonado con cero exterior

## Resultado

Este documento pregunta si la información que todavía no usa la energía de
`104_93` —integridad de los saltos de la función contadora, gaps y
composición multiplicativa exacta— excluye por sí sola una excursión

\[
 {x^\beta\over\log x}\cos(\gamma\log x+\phi),
 \qquad {1\over2}<\beta<1.                                  \tag{1}
\]

La respuesta es **no**, incluso conservando bastante más que en el
falsificador de `104_101`.

**Teorema A (sistema Euler escalonado con un cero prescrito).** Sea

\[
 \rho=\beta+i\gamma,
 \qquad {1\over2}<\beta<1,
 \qquad \gamma\ne0,                                        \tag{2}
\]

y sea $W\ge1$ un entero fijo. Existe una sucesión
$a_n\in\{0,1\}$, soportada en $(n,W)=1$, cuya función contadora

\[
 P(x)=\sum_{n\le x}a_n                                      \tag{3}
\]

satisface

\[
 P(x)=\operatorname {Li}(x)
      -2\Re\!\int_{X_0}^x{t^{\rho-1}\over\log t}\,dt+O(1)
      =\operatorname {Li}(x)
       -2\Re{x^\rho\over\rho\log x}
       +O\!\left({x^\beta\over\log ^2x}\right).           \tag{4}
\]

Los gaps consecutivos del soporte son $O_{W,\rho}(\log x)$. En
particular el sistema cumple la PNT y cualquier *envelope* fijo de tipo
Vinogradov--Korobov.

Declare cada $n$ con $a_n=1$ un generador primo abstracto de norma
$n$, y forme el monoide conmutativo libre generado por ellos. Su zeta
de Euler es

\[
 Z_{\mathcal P}(s)=\prod_{a_n=1}(1-n^{-s})^{-1},
 \qquad \Re s>1.                                           \tag{5}
\]

Entonces (5) admite continuación meromorfa local a entornos de
$1,\rho,\bar\rho$, tiene un polo simple en $1$ y ceros simples en
$\rho$ y $\bar\rho$. Sus pesos de Mangoldt son reales y no negativos:

\[
 \Lambda_{\mathcal P}(m)
 =\sum_{\substack{a_n=1,\ k\ge1\\n^k=m}}\log n\ge0,
 \qquad
 -{Z_{\mathcal P}'\over Z_{\mathcal P}}(s)
 =\sum_{m\ge2}{\Lambda_{\mathcal P}(m)\over m^s}.          \tag{6}
\]

La composición es exacta. Si

\[
 Z_{\mathcal P}(s)=\sum_{m\ge1}{g(m)\over m^s},
 \qquad g(m)\in\mathbb Z_{\ge0},                            \tag{7}
\]

entonces, coeficiente a coeficiente,

\[
 \boxed{\quad g(m)\log m
 =\sum_{d\mid m}g(m/d)\Lambda_{\mathcal P}(d).\quad}        \tag{8}
\]

**Teorema B (rigidez exacta de la norma ordinaria).** Para cualquier
sistema libre con normas generadoras enteras, si la aplicación norma al
monoide ordinario $\mathbb N$ es inyectiva, entonces su contadora de
generadores satisface

\[
 P_{\mathcal Q}(x)\le\pi(x)\qquad(x\ge2).                  \tag{8a}
\]

Si la aplicación norma es además sobreyectiva, los generadores son
exactamente los primos ordinarios. Por tanto toda deformación Euler
entera que conserve composición **biyectiva** es imposible: el sistema
queda rígidamente fijado. Las colisiones de norma son el escape explícito
usado en el Teorema A; en general, toda deformación no trivial debe
perder inyectividad o sobreyectividad de la norma. El Teorema B no afirma
cuál de las dos pérdidas es forzosa en otro modelo.

Por último, la energía prima correspondiente viola el blanco de
`104_93` con tasa polinomial:

\[
 \sum_{m\le N}{\{P(m)-\operatorname {Li}(m)\}^2\over m(m+1)}
 \asymp_{W,\rho}{N^{2\beta-1}\over\log ^2N}.               \tag{9}
\]

**Frontera exacta.** El teorema conserva saltos $0$--$1$, normas
enteras, gaps logarítmicos, una rueda finita arbitraria, PNT/VK, pesos
de Mangoldt positivos, Euler producto y factorización única en el
monoide abstracto. Lo que no conserva es que la aplicación norma sea
la factorización irreducible literal de $\mathbb N$: un generador puede
tener norma compuesta y dos enteros generalizados distintos pueden tener
la misma norma. Exigir que los generadores sean exactamente los
irreducibles ordinarios deja, como en `104_101`, el *singleton* de los
primos ordinarios.

Así, una excursión exterior no es incompatible con integridad,
escalonamiento, gaps ni con un Euler producto positivo abstracto. Para
los primos ordinarios solo puede excluirse usando una propiedad que
distingue su incrustación multiplicativa literal en $\mathbb N$. Esa
propiedad completa vuelve a ser la sucesión prima misma; el presente
falsificador no prueba ni refuta (9) para los primos ordinarios, A1 o RH.

---

## 1. Construcción de la escalera $0$--$1$

Elija primero dos enteros coprimos con $W$, $q_1,q_2>1$, y declare
$q_1,q_2,q_1q_2$ generadores en el prefijo finito. Esto instala la
colisión de norma

\[
 N([q_1q_2])=N([q_1][q_2])=q_1q_2,                         \tag{9a}
\]

Deje además fuera del prefijo algún primo ordinario $q_0$ distinto de
esas tres normas; así la norma tampoco es sobreyectiva. Estas decisiones
finitas no afectan ninguna asintótica ni singularidad en $\Re s>0$. Elija
ahora $X_0>q_1q_2$ tan grande que, para $x\ge X_0$,

\[
 2x^{\beta-1}\le{1\over2},
 \qquad {3\over2\log x}< {1\over W}.                       \tag{10}
\]

Defina la función real creciente

\[
 F(x)=\int_{X_0}^x
 {1-t^{\rho-1}-t^{\bar\rho-1}\over\log t}\,dt
 =\int_{X_0}^x
 {1-2t^{\beta-1}\cos(\gamma\log t)\over\log t}\,dt.      \tag{11}
\]

Por (10),

\[
 {1\over2\log x}\le F'(x)\le {3\over2\log x}.            \tag{12}
\]

Enumere los enteros mayores que $X_0$ y coprimos con $W$:
$r_0<r_1<\cdots$. Como $r_j-r_{j-1}\le W$, aumentando $X_0$
si hace falta, (12) da

\[
 0<F(r_j)-F(r_{j-1})<1.                                   \tag{13}
\]

Ponga

\[
 a_{r_j}=\lfloor F(r_j)\rfloor-\lfloor F(r_{j-1})\rfloor,
 \qquad a_n=0\quad(n\ne r_j),                              \tag{14}
\]

y absorba el prefijo finito en una constante. La ecuación (13) prueba
$a_n\in\{0,1\}$. Si $r(x)$ es el último candidato no mayor que
$x$, telescopar (14) da

\[
 P(x)=\lfloor F(r(x))\rfloor+C=F(x)+O_W(1).                \tag{15}
\]

La última igualdad usa $0\le x-r(x)<W$ y (12).

Para los gaps, tome $y=x+8\log x+W$. Para $x$ grande,
$\log y\le2\log x$, y por (12)

\[
 F(y-W)-F(x)\ge {y-W-x\over2\log y}\ge2.                 \tag{16}
\]

Hay un candidato entre $y-W$ e $y$, y el piso de $F$ debe haber
saltado antes de $y$. Esto prueba el gap $O(\log x)$.

Integración por partes compleja da

\[
 \int_{X_0}^x{t^{\rho-1}\over\log t}\,dt
 ={x^\rho\over\rho\log x}
 +O_\rho\!\left({x^\beta\over\log ^2x}\right),           \tag{17}
\]

y (4) sigue de (11), (15) y la definición de $\operatorname {Li}$,
con una constante de base absorbida. Para todo $C>0$,

\[
 {x^\beta\over\log x}
 =o\!\left(xe^{-C(\log x)^{3/5}(\log\log x)^{-1/5}}\right),\tag{18}
\]

lo que justifica la afirmación PNT/VK.

## 2. Continuación local y cero exterior

Sea la función zeta prima

\[
 \mathfrak p(s)=\sum_{n\ge2}{a_n\over n^s}
 =\int_{X_0^-}^{\infty}x^{-s}\,dP(x),
 \qquad \Re s>1.                                          \tag{19}
\]

Escriba $D(x)=P(x)-F(x)$. Por (15), $D=O(1)$, y la integración
de Stieltjes por partes muestra que

\[
 \int_{X_0^-}^{\infty}x^{-s}\,dD(x)
 =H_0(s)+s\int_{X_0}^{\infty}D(x)x^{-s-1}\,dx,             \tag{20}
\]

donde el término de borde $H_0(s)$ es una función entera. La expresión es holomorfa
en $\Re s>0$. Con $L=\log X_0$, ponga inicialmente

\[
 \mathscr E_L(z)=\int_L^\infty{e^{-zt}\over t}\,dt,
 \qquad \Re z>0.                                          \tag{21}
\]

Las ecuaciones (11), (19) y el cambio $x=e^t$ dan

\[
 \boxed{
 \mathfrak p(s)=
 \mathscr E_L(s-1)-\mathscr E_L(s-\rho)
 -\mathscr E_L(s-\bar\rho)+H(s),}                         \tag{22}
\]

donde $H$ es holomorfa en $\Re s>0$. Localmente en $z=0$,

\[
 \mathscr E_L(z)=-\log z+h_L(z),                           \tag{23}
\]

con $h_L$ holomorfa. Por tanto, en discos pequeños disjuntos,

\[
 \mathfrak p(s)=
 \begin{cases}
  -\log(s-1)+H_1(s),&s\sim1,\\
  \phantom{-}\log(s-\rho)+H_\rho(s),&s\sim\rho,\\
  \phantom{-}\log(s-\bar\rho)+H_{\bar\rho}(s),&s\sim\bar\rho,
 \end{cases}                                               \tag{24}
\]

con los tres restos holomorfos.

En $\Re s>1$, el logaritmo del producto (5) es

\[
 \log Z_{\mathcal P}(s)=
 \sum_{k\ge1}{\mathfrak p(ks)\over k}.                    \tag{25}
\]

Como $\beta>1/2$, para $s$ en un entorno suficientemente pequeño de
$\rho$, todos los términos $k\ge2$ de (25) están dados por series
absolutamente convergentes y forman una función holomorfa. De (24),

\[
 \log Z_{\mathcal P}(s)=\log(s-\rho)+K_\rho(s),
 \qquad
 Z_{\mathcal P}(s)=(s-\rho)e^{K_\rho(s)}.                 \tag{26}
\]

El coeficiente del logaritmo es el entero $+1$, de modo que su
monodromía desaparece al exponentiar: (26) es una continuación
holomorfa monovaluada, no solo una rama formal. Esto prueba el cero
simple. El argumento conjugado prueba el cero en $\bar\rho$, y el
coeficiente entero $-1$ de (24) en $1$ prueba, tras exponentiar, el
polo simple monovaluado.

## 3. Mangoldt positivo, composición exacta y rigidez de norma

Expandir cada factor geométrico de (5) produce (7), donde $g(m)$
cuenta, con multiplicidad, las factorizaciones abstractas cuya norma es
$m$. Cada coeficiente es un entero no negativo. Derivar (25) en
$\Re s>1$ produce (6). Multiplicar

\[
 -Z_{\mathcal P}'(s)=
 Z_{\mathcal P}(s)\sum_{d\ge2}{\Lambda_{\mathcal P}(d)\over d^s}
                                                               \tag{27}
\]

y comparar el coeficiente de $m^{-s}$ da (8), porque el lado izquierdo
es $g(m)\log m$. No se usa continuación analítica en esta identidad.

Para probar el Teorema B, factorice cada norma generadora $q\le x$ en
primos ordinarios y denote por

\[
 v_q=(v_p(q))_{p\le x}\in\mathbb Z_{\ge0}^{\pi(x)}          \tag{27a}
\]

su vector de exponentes. Si estos vectores fueran linealmente
dependientes sobre $\mathbb Q$, al limpiar denominadores y separar las
partes positiva y negativa se obtendrían dos productos distintos de
generadores con la misma norma. Eso contradice la inyectividad. Los
$v_q$ son, pues, linealmente independientes, y su cantidad no excede
la dimensión $\pi(x)$; esto prueba (8a).

Si la norma es también sobreyectiva y un generador tuviera norma
compuesta $ab$ con $a,b>1$, la sobreyectividad levantaría $a,b$ a dos
enteros generalizados. Su producto y el generador serían elementos
distintos con igual norma, contra la inyectividad. Toda norma generadora
es entonces un primo ordinario. Recíprocamente, cada primo ordinario
debe ser norma de algún elemento; su factorización libre solo puede
tener un generador, que por inyectividad es único. Así se recupera
exactamente el sistema primo ordinario.

La correspondiente función de Chebyshev también exhibe directamente el
cero plantado. Por suma de Stieltjes y (11),

\[
 \vartheta_{\mathcal P}(x)
 :=\sum_{n\le x}a_n\log n
 =x-{x^\rho\over\rho}-{x^{\bar\rho}\over\bar\rho}+O(\log x).
                                                               \tag{28}
\]

Las potencias $k\ge2$ aportan $O(\sqrt x\log^2x)$, así que

\[
 \psi_{\mathcal P}(x)
 =x-2\Re{x^\rho\over\rho}+O(\sqrt x\log^2x).              \tag{29}
\]

La oscilación exterior, el cero de (26) y los pesos positivos de (6)
son por tanto tres caras del mismo sistema exacto.

## 4. Energía polinomial

De (4) y (17), uniformemente para $x$ grande,

\[
 P(x)-\operatorname {Li}(x)
 =-{2x^\beta\over|\rho|\log x}
   \cos(\gamma\log x-\arg\rho)
  +O_\rho\!\left({x^\beta\over\log^2x}\right).            \tag{30}
\]

La cota superior de (9) es inmediata. Para la inferior, cada intervalo
de longitud fija en la variable $u=\log x$ contiene un subintervalo
de longitud fija donde el coseno de (30) tiene módulo al menos $1/2$.
Sobre el último de esos subintervalos contenido en
$[\log N-C_\gamma,\log N]$, el peso
$e^{(2\beta-1)u}/u^2$ es comparable con su valor en $u=\log N$.
La comparación suma--integral da

\[
 \sum_{m\le N}{m^{2\beta-2}\over\log^2m}
 \cos^2(\gamma\log m-\arg\rho)
 \asymp_\rho {N^{2\beta-1}\over\log^2N}.                  \tag{31}
\]

El error de (30) es menor por un factor $\log N$, y (9) sigue.

## 5. Qué decide y qué no decide

`104_101` ya construye una sucesión $0$--$1$ con rueda fija, gaps
logarítmicos y energía polinomial. El Teorema A agrega dos restricciones
que allí no estaban simultáneamente:

1. un Euler producto exacto con coeficientes enteros no negativos;
2. pesos de Mangoldt no negativos y la composición exacta (8), mientras
   se prescribe un cero exterior concreto.

La construcción no es una repetición de Hurwitz, Nyman--Beurling,
positividad de Weil ni de un modelo continuo de $\psi$. Tampoco se
reclama novedad bibliográfica para la filosofía de primos generalizados;
el contenido nuevo **dentro de esta fase** es el falsificador explícito
que enlaza (4), (6), (8), (9) y (26).

El resultado descarta una inferencia concreta:

\[
 \substack{\text{saltos }0\text{-}1+\text{gaps}+\text{PNT/VK}
 +\text{Euler positivo}+\text{composición abstracta}}
 \quad\not\Longrightarrow\quad
 \text{energía subpolinomial}.                              \tag{32}
\]

No descarta una identidad que use que $n$ es irreducible en el monoide
**ordinario** $(\mathbb N,\cdot)$. Pero esa condición no admite una
deformación: determina $a_n=\mathbf1_{\mathbb P}(n)$ coordenada por
coordenada. Probar la energía en ese singleton sigue siendo exactamente
el objetivo abierto.

## 6. Reproducción

Desde `tools/`:

```bash
python3 104_103_integral_step_euler_offline_falsifier_check.py
```

El checker hace dos pruebas separadas. Primero construye un prefijo de
(14) con $\beta=3/4,\gamma=1,W=6$, verifica saltos $0$--$1$, soporte,
tracking y gaps. Después toma los generadores obtenidos y comprueba (8)
**exactamente en aritmética entera**, representando cada logaritmo por
su vector de exponentes primos; esto incluye colisiones de norma. Por
último verifica la expansión local (23) con la serie convergente de
$E_1$. Los cálculos reales son diagnósticos de la construcción; las
pruebas uniformes son (10)--(31).
