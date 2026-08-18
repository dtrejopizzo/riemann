# 104_42 — Precondicionador no conmutativo adaptado al grado: óptimo exacto y stop-gate

**Estado.** Se atacó directamente

\[
 B_n:=A_n-\lambda_n\le \kappa A_n,\qquad
 \kappa={1501\over2002},\qquad n\ge150.                     \tag{1}
\]

Se permitieron precondicionadores positivos dependientes de \(n\), sin
ninguna condición de conmutación. El operador aritmético contiene
simultáneamente todas las potencias primas, el polo continuo y la fase.
También se estudió la compresión previa al espacio de los primeros \(n\)
estados de Laguerre.

El resultado es exacto:

1. la mejor completación cuadrática entre **todos** los precondicionadores
   positivos no conmutativos vale el módulo del momento que se quiere
   acotar; cuando \(B_n>0\), su valor óptimo es \(B_n\) mismo;
2. la compresión canónica por grado conserva la fase y elimina la cola de
   Hardy, pero su ganancia sobre el dato nuevo es
   \(\sqrt{n/2}>1\), por lo que no propaga una cota superior.

Esto descarta la **optimización algebraica autónoma** de completaciones
cuadráticas positivas, no una identidad lineal firmada. Tampoco impide que
una elección explícita de \(R\) pudiera recibir una cota aritmética nueva;
tal cota tendría que aportar por sí misma el margen de (1). No se prueba
(1), A1 ni RH.

## 1. Operador Euler--polo completo

Sean

\[
 g_n(x)=e^{-x/2}L_{n-1}^{(1)}(x),\qquad
 (T_tf)(x)=e^{-t/2}f(x-t){\bf1}_{x\ge t}.                    \tag{2}
\]

Entonces

\[
 \|g_n\|_2^2=n,\qquad
 \langle T_tg_n,g_n\rangle=e^{-t}L_{n-1}^{(1)}(t).          \tag{3}
\]

Escribamos la medida completa de von Mangoldt como

\[
 d\Psi(y)=\sum_{m\ge2}\Lambda(m)\,\delta_m(dy).             \tag{4}
\]

Para \(a>2\), la integral de Bochner

\[
 \boxed{\mathcal D_a
 =a\int_1^\infty T_{a\log y}\{d\Psi(y)-dy\}}                \tag{5}
\]

define un operador acotado en \(L^2(0,\infty)\), pues la norma de cada
traslación es \(y^{-a/2}\). Póngase

\[
 v_{n,a}=\mathcal D_ag_n,\qquad
 b_{n,a}=\langle v_{n,a},g_n\rangle\in\mathbb R.             \tag{6}
\]

Sin separar ningún canal, (3) da

\[
\boxed{
\begin{aligned}
 b_{n,a}
={}&a\sum_{m\ge2}{\Lambda(m)\over m^a}
       L_{n-1}^{(1)}(a\log m)\\
 &-a\int_1^\infty y^{-a}L_{n-1}^{(1)}(a\log y)\,dy .
\end{aligned}}                                               \tag{7}
\]

Si \(s_a(z)=a/(1-z)\), la identidad de coeficientes de 104_32 prueba

\[
 \boxed{
 b_{n,a}=-n[z^n]\log\bigl((s_a(z)-1)\zeta(s_a(z))\bigr).}    \tag{8}
\]

Como \((s-1)\zeta(s)\) es analítica y no nula en \(s=1\), la fórmula de
coeficientes (8) continúa \(b_{n,a}\) a un entorno de \(a=1\), y

\[
 \boxed{\lim_{a\downarrow1}b_{n,a}=A_n-\lambda_n=B_n.}       \tag{9}
\]

En (9) el límite es el de esa continuación. La integral de Bochner (5)
y la serie separada (7) solo convergen directamente en el dominio seguro
\(a>2\).

Así (5)--(9) conservan primos, potencias primas, polo y fase. En el
semiplano de convergencia absoluta,

\[
 \widehat v_{n,a}(t)
 =a\widehat g_n(t)\,\mathcal M\!\left(a(1/2+it)\right),
 \qquad
 \mathcal M(s)=-{\zeta'\over\zeta}(s)-{1\over s-1}.          \tag{10}
\]

La resta cancela el polo de \(s=1\), pero no los polos de los ceros.

## 2. Óptimo no conmutativo

> **Lema 2.1.** Sean \(v,g\) vectores de un espacio de Hilbert real y
> \(b=\langle v,g\rangle\). Para todo operador acotado, autoadjunto,
> estrictamente positivo e invertible \(R\), defina
>
> \[
> \mathcal C_R(v,g)
> ={1\over2}\{\langle Rv,v\rangle+\langle R^{-1}g,g\rangle\}.
> \]
>
> Entonces
>
> \[
> b\le\mathcal C_R(v,g),\qquad
> \boxed{\inf_{R>0}\mathcal C_R(v,g)=|b|.}                  \tag{11}
> \]

**Demostración.** Se tiene

\[
 2\{\mathcal C_R-b\}
 =\|R^{1/2}v-R^{-1/2}g\|^2\ge0,                             \tag{12}
\]

y Cauchy en la métrica \(R\) da

\[
 \mathcal C_R\ge
 \sqrt{\langle Rv,v\rangle\langle R^{-1}g,g\rangle}
 \ge|\langle v,g\rangle|.                                  \tag{13}
\]

Si \(b\ne0\), sea \(\sigma=\mathrm{sgn}\,b\). Existe \(R>0\) tal que

\[
 Rv=\sigma g.                                               \tag{14}
\]

En efecto, para \(u=v/\|v\|\), descomponga
\(\sigma g/\|v\|=\alpha u+\beta e\), donde \(e\perp u\) es unitario y
\(\alpha=|b|/\|v\|^2>0\). Sobre
\(\mathrm{span}\,\{u,e\}\), tome

\[
 R=\begin{pmatrix}\alpha&\beta\\ \beta&d\end{pmatrix},
 \qquad d>{\beta^2\over\alpha},                             \tag{15}
\]

y extiéndalo por la identidad. Entonces
\(R^{-1}g=\sigma v\), y ambos términos de (11) valen \(|b|\).
Si \(b=0\), \(v\perp g\); pesos \(\tau\) sobre \(v\) y
\(\tau^{-1}\) sobre \(g\), seguidos de \(\tau\downarrow0\), dan el
ínfimo cero. \(\square\)

Aplicado a (6),

\[
 b_{n,a}\le\mathcal C_{n,a}[R],\qquad
 \boxed{\inf_{R>0}\mathcal C_{n,a}[R]=|b_{n,a}|.}            \tag{16}
\]

Si \(b_{n,a}\le0\), el objetivo con lado derecho positivo es automático y
la completación pierde el signo. Si \(b_{n,a}>0\), único régimen que puede
violar (1), el óptimo de (16) es \(b_{n,a}\) mismo. Por consiguiente,

\[
 \mathcal C_{n,a}[R]\le\kappa A_n                           \tag{17}
\]

ya contiene \(b_{n,a}\le\kappa A_n\). El operador (15) alcanza el óptimo
usando el vector aritmético completo y el signo de \(b_{n,a}\), de modo
que no constituye una estimación independiente.

Toda factorización
\(\|Cv-C^{-*}g\|^2\ge0\) pertenece a esta clase tomando \(R=C^*C\).
Esto incluye factores triangulares, matrices densas de grado y factores no
normales antes de formar el cuadrado.

El alcance de esta conclusión es preciso: (16) muestra que elegir u
optimizar \(R\) usando solo el álgebra hilbertiana no crea una holgura. Si
una construcción aritmética explícita probara (17) para algún \(R\), sí
cerraría (1), pero (17) contendría entonces el nuevo teorema unilateral y
no sería consecuencia del Lema 2.1.

## 3. Precio de condición en el borde

Sea \(\rho=1/2+i\gamma\) un cero crítico de multiplicidad \(m_\rho\).
Localmente,

\[
 \mathcal M(s)=-{m_\rho\over s-\rho}+H_\rho(s).              \tag{18}
\]

Para cada \(n\) puede elegirse tal cero con
\(\widehat g_n(\gamma)\ne0\): Hardy da infinitos ceros críticos, mientras
los ceros reales de \(\widehat g_n\) forman un conjunto finito.
Integrando (18) en un intervalo fijo alrededor de \(\gamma/a\), se obtiene,
siempre que la continuación de \(v_{n,a}\) pertenezca a \(L^2\),

\[
 \boxed{\|v_{n,a}\|_2^2\ge {c_{n,\rho}\over a-1}}
 \qquad(1<a<a_{n,\rho}),                                   \tag{19}
\]

con \(c_{n,\rho}>0\).

Defina

\[
 m(R)=\|R^{-1}\|^{-1},\qquad
 \mathrm{cond}(R)={\|R\|\over m(R)}.
\]

Si \(\mathcal C_{n,a}[R_{n,a}]\le C_0\), entonces

\[
 m(R_{n,a})\|v_{n,a}\|^2\le2C_0,\qquad
 {n\over\|R_{n,a}\|}\le2C_0.                               \tag{20}
\]

Por (19),

\[
 \boxed{\mathrm{cond}(R_{n,a})
 \ge {n c_{n,\rho}\over4C_0^2(a-1)}.}                       \tag{21}
\]

Así cualquier precondicionador de costo finito debe degenerar al menos
como \((a-1)^{-1}\). La libertad no conmutativa traslada la divergencia a
la condición del precondicionador; para alcanzar el óptimo debe alinear
singularmente el vector aritmético con \(g_n\).

## 4. Compresión canónica por grado

Para comprimir correctamente la forma, ponga

\[
 \mathcal X_a={\mathcal D_a+\mathcal D_a^*\over2}.           \tag{22}
\]

Entonces \(b_{n,a}=\langle\mathcal X_ag_n,g_n\rangle\).
Sea \(P_n\) la proyección ortogonal sobre

\[
 \mathcal V_n=\mathrm{span}\,\{\phi_0,\ldots,\phi_{n-1}\},
 \qquad \phi_j=e^{-x/2}L_j(x).                              \tag{23}
\]

Como \(g_n=\sum_{j<n}\phi_j\in\mathcal V_n\),

\[
 b_{n,a}=\langle P_n\mathcal X_ag_n,g_n\rangle
 \le\sqrt n\,\|P_n\mathcal X_ag_n\|.                        \tag{24}
\]

La proyección \(P_n\) no conmuta con ninguna traslación no trivial y (24)
no contiene la norma de la cola de Hardy.

En el límite de Abel, la forma simétrica es la matriz Toeplitz
\(\mathsf Q_0=[q_{|j-k|}]\) de 104_30. Con \(B_0=0\),

\[
 q_0=B_1,\qquad
 q_d={B_{d+1}-2B_d+B_{d-1}\over2}\quad(d\ge1).              \tag{25}
\]

Ponga \(\Delta B_j=B_{j+1}-B_j\), incluida
\(\Delta B_0=B_1\). Para \(0\le j<n\),

\[
\begin{aligned}
 (P_n\mathsf Q_0g_n)_j
 &=q_0+\sum_{d=1}^{j}q_d+\sum_{d=1}^{n-1-j}q_d\\
 &=\boxed{{\Delta B_j+\Delta B_{n-1-j}\over2}}.             \tag{26}
\end{aligned}
\]

Por tanto (24) tiene el límite finito y completamente firmado

\[
 \boxed{
 B_n\le{\sqrt n\over2}
 \left\{\sum_{j=0}^{n-1}
  (\Delta B_j+\Delta B_{n-1-j})^2\right\}^{1/2}.}            \tag{27}
\]

Esta desigualdad conserva la cancelación conjunta de los pesos
\(\Lambda(m)\), pero no cierra una inducción. Mantenga fijos
\(B_0,\ldots,B_{n-1}\) y escriba \(x=B_n\to+\infty\). El valor \(x\)
entra solo en \(j=0,n-1\), mediante

\[
 \Delta B_{n-1}+\Delta B_0=x-B_{n-1}+B_1.                  \tag{28}
\]

El lado derecho de (27) es entonces

\[
 {\sqrt n\over2}\{2x^2+O_n(x)+O_n(1)\}^{1/2}
 =\boxed{\sqrt{n\over2}\,x+O_n(1).}                         \tag{29}
\]

Para \(n\ge3\), \(\sqrt{n/2}>1\). Así (27) es compatible con valores
arbitrariamente grandes del dato nuevo \(B_n\), incluso si todos los datos
anteriores son conocidos. Los pesos diagonales no uniformes vuelven, al
optimizarse, al lema 2.1 y al valor \(|B_n|\).

## 5. Falsificador off-line

Tome

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5}.           \tag{30}
\]

Para \(n\equiv0\pmod4\), su cuarteto aporta

\[
 \lambda_n^{\rm off}=4-2(2^n+2^{-n}),\qquad
 B_n^{\rm off}=2(2^n+2^{-n})-4.                             \tag{31}
\]

En \(n=152\),

\[
 B_{152}^{\rm off}>{1501\over2002}\,152^2.                 \tag{32}
\]

El óptimo (16) devuelve el mismo valor excesivo y no certifica al divisor
falso. Al deformar desde \(a>2\), el polo de (10) cruza la frontera en
\(a=8/5\), como en 104_36. La compresión tampoco lo borra: el crecimiento
reaparece en las dos coordenadas extremas de (28).

## 6. Decisión

    probado incondicionalmente:
      operador Euler--polo con todas las Lambda(m), (5)--(10);
      óptimo sobre todo R positivo no conmutativo, (11)--(16);
      cond(R) >= c/(a-1) para todo costo acotado cuya
        continuacion vectorial pertenezca a L2, (21);
      compresión por grado y fórmula firmada (26)--(27);
      ganancia defectuosa sqrt(n/2)>1, (29);
      fallo ante el cuarteto off-line, (30)--(32).

    descartado:
      cerrar (1) mediante la sola optimizacion algebraica de una
        completación cuadrática positiva;
      obtener margen solo singularizando el precondicionador;
      usar la proyección de grado como recurrencia inductiva.

    permanece abierto:
      una desigualdad lineal unilateral que conserve el signo canónico
      de Lambda(m) sin convertir la correlación en energía positiva;
      (1), A1 y RH.

## 7. Verificación

Ejecutar:

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 degree_adapted_noncommutative_gate_check.py

El programa usa Fraction. Verifica matrices positivas no diagonales que
alcanzan (11) para productos internos de ambos signos, la inversión
Toeplitz (25), las coordenadas (26), el coeficiente \(n/2\) al cuadrado de
(29) y el falsificador (32). No usa punto flotante.
