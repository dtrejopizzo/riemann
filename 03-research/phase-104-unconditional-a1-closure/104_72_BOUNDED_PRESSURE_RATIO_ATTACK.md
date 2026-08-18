# 104_72 — Razón de presiones acotada y gate de transición

**Resultado.** Para \(\tau>0\), el observable

\[
 g_\tau(x)
 ={1\over\tau}\{\log(1+e^{-x})
 -\log(1+e^{-(x+\tau)})\}
 ={1\over\tau}\int_0^\tau {ds\over1+e^{x+s}}              \tag{1}
\]

pertenece a \([0,1]\), tiende a cero cuando \(x\to+\infty\) y a uno cuando
\(x\to-\infty\). En las ventanas deterministas

\[
 I_L=\{L^2,L^2+1,\ldots,L^2+L-1\},                        \tag{2}
\]

si \(x_n=\lambda_n+\log(n+1)\) y

\[
 G_L=\sum_{n\in I_L}g_\tau(x_n),                          \tag{3}
\]

entonces

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 G_L\longrightarrow0.}                                    \tag{4}
\]

La exponencial de \(\tau G_L\) es una razón de dos particiones:

\[
 \boxed{e^{\tau G_L}
 =\prod_{n\in I_L}{1+z_n\over1+e^{-\tau}z_n},\qquad
 z_n={e^{-\lambda_n}\over n+1}.}                          \tag{5}
\]

Cada factor está entre \(1\) y \(e^\tau\). Así las actividades
astronómicas se saturan en vez de explotar.

Esta es una ventaja cuantitativa real frente a `104_71`. Allí una sola
actividad \(z_n=e^{-\lambda_n}/(n+1)\) puede hacer crecer la partición como
\(e^{-\lambda_n}\); aquí el mismo sitio aporta a lo sumo \(e^\tau\). Por
eso (5) conserva exactamente la relajación de densidad: cuenta cuántos
sitios entran en la fase mala, sin ponderar otra vez su profundidad
exponencial.

La saturación no elimina el condicionamiento prima--polo. La transición
ocurre cuando \(z_n\asymp1\), y decidir de qué lado está exige conocer
\(Q_{n,\varepsilon}-\{A_n+p_n(\varepsilon)+\log(n+1)\}\) con error
aditivo \(O(1)\). Sus dos términos grandes tienen tamaño
\(\exp(X^2/100+o(1))\) en la diagonal de 104_69. La razón acotada sigue
requiriendo, en esa franja, precisión relativa
\(\exp(-X^2/100+O(1))\).

Este documento prueba el criterio, su lift diagonal y el no-go de
separación. No prueba que \(G_L\to0\) para zeta, A1 ni RH.

---

## 1. Propiedades elementales de la presión

Ponga \(q=e^{-\tau}\in(0,1)\) y \(z=e^{-x}\). Entonces

\[
 g_\tau(x)={1\over\tau}\log{1+z\over1+qz}.                 \tag{6}
\]

Como

\[
 1\le {1+z\over1+qz}\le{1\over q}=e^\tau,
\]

se obtiene \(0\le g_\tau\le1\). Además,

\[
 g_\tau(x)\le {1\over\tau}\log(1+z)\le {z\over\tau}.
 \tag{7}
\]

La sensibilidad respecto de \(\log z=-x\) es

\[
 {d\over d\log z}\log{1+z\over1+qz}
 ={(1-q)z\over(1+z)(1+qz)}.                               \tag{8}
\]

El máximo se alcanza en \(z=q^{-1/2}=e^{\tau/2}\), y vale

\[
 \max_{z>0}{(1-q)z\over(1+z)(1+qz)}
 =\tanh{\tau\over4}.                                      \tag{9}
\]

Por tanto

\[
 |g_\tau'(x)|\le{\tanh(\tau/4)\over\tau}< {1\over4}.
 \tag{10}
\]

La derivada tiende a cero en ambos extremos. Toda la información de signo
vive en una franja de ancho \(O_\tau(1)\) alrededor de
\(x=-\tau/2\), o equivalentemente \(z=e^{\tau/2}\).

---

## 2. Criterio de ventanas

**Teorema 2.1.** Se cumple (4). Más precisamente:

* bajo RH,
  \[
   0\le G_L\le {L\over\tau(L^2+1)}=O_\tau(L^{-1});         \tag{11}
  \]
* si RH es falsa, existen \(M<\infty\) y \(L_0\) tales que
  \[
   \liminf_{L\to\infty}{G_L\over L}\ge {1\over M}>0.       \tag{12}
  \]

**Demostración.** Bajo RH, \(\lambda_n\ge0\), luego
\(z_n\le1/(n+1)\). Las ecuaciones (2) y (7) dan

\[
 G_L\le {1\over\tau}\sum_{n\in I_L}{1\over n+1}
 \le {L\over\tau(L^2+1)}.
\]

Si RH es falsa, 104_56 proporciona \(c>0\), \(R>1\), un conjunto
sindético \(D\) y una cota de huecos \(M\), tales que
\(\lambda_n\le-cR^n\) en \(D\). Cada subintervalo de \(M\) enteros en
\(I_L\) contiene un \(d\in D\). En esos índices,

\[
 x_d\le-cR^d+\log(d+1)\longrightarrow-\infty,
\qquad g_\tau(x_d)\longrightarrow1.                       \tag{13}
\]

Partiendo \(I_L\) en \(\lfloor L/M\rfloor\) subintervalos disjuntos,
para cada \(\delta>0\) y todo \(L\) suficientemente grande se obtiene
\(G_L\ge(1-\delta)\lfloor L/M\rfloor\). Dividir por \(L\) y luego hacer
\(\delta\downarrow0\) prueba (12). En particular
\(\liminf G_L\ge1\), y (4) sigue.
\(\square\)

La razón (5) se obtiene sumando (6). De \(0\le g_\tau\le1\),

\[
 1\le e^{\tau G_L}\le e^{\tau L}.                         \tag{14}
\]

Bajo RH la razón tiende a uno. Bajo no-RH crece al menos como
\(\exp\{(\tau/M+o(1))L\}\).

---

## 3. Lift prima--Laguerre con una diagonal única

Sea

\[
 X_L=L^2+L-1,\qquad
 \varepsilon_L=e^{-X_L/100}.                              \tag{15}
\]

Para \(L\ge8\), \(X_L\ge70\), de modo que
\(\varepsilon_L\le1/2\). Use

\[
\begin{aligned}
 \lambda_{n,\varepsilon_L}
 &=A_n+p_n(\varepsilon_L)-Q_{n,\varepsilon_L},\\
 Q_{n,\varepsilon_L}
 &=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon_L}}
 L_{n-1}^{(1)}(\log m).
\end{aligned}                                             \tag{16}
\]

Con

\[
 r={199\over200},\qquad
 \eta={1\over100}-\log{200\over199}>0,\qquad
 M_0=M_{199/200},
\]

104_66 da, uniformemente para \(n\in I_L\),

\[
 |\lambda_{n,\varepsilon_L}-\lambda_n|
 \le2M_0X_Le^{-\eta X_L}.                                 \tag{17}
\]

Defina \(x_{n,\varepsilon_L}=
\lambda_{n,\varepsilon_L}+\log(n+1)\) y

\[
 G_{L,\varepsilon_L}
 =\sum_{n\in I_L}g_\tau(x_{n,\varepsilon_L}).              \tag{18}
\]

Por (10) y (17),

\[
 \boxed{
 |G_{L,\varepsilon_L}-G_L|
 \le {2M_0L X_L\tanh(\tau/4)\over\tau}
 e^{-\eta X_L}\longrightarrow0.}                         \tag{19}
\]

Así RH equivale también a \(G_{L,\varepsilon_L}\to0\).

Ponga

\[
 z_{n,\varepsilon_L}
 ={e^{-A_n-p_n(\varepsilon_L)}\over n+1}
 \prod_{m\ge2}\exp\!\left(
 {\Lambda(m)\over m^{1+\varepsilon_L}}
 L_{n-1}^{(1)}(\log m)\right).                            \tag{20}
\]

Para cada \(L\), el producto converge absolutamente y
\(z_{n,\varepsilon_L}=e^{-\lambda_{n,\varepsilon_L}}/(n+1)>0\).
La razón regulada exacta es

\[
\boxed{
 e^{\tau G_{L,\varepsilon_L}}
 =\prod_{n\in I_L}
 {1+z_{n,\varepsilon_L}
  \over1+e^{-\tau}z_{n,\varepsilon_L}}.}                  \tag{21}
\]

No hay límite interno \(\varepsilon\downarrow0\). Cada factor de (21)
permanece en \([1,e^\tau]\), aun cuando la actividad de (20) sea enorme.

---

## 4. ¿La razón acotada mejora el condicionamiento?

### 4.1 Lo que sí mejora respecto de `104_71`

La partición de `104_71` contiene el factor \(1+z_n\), no acotado. Una
excursión \(-\lambda_n\asymp R^n\) produce un factor de orden
\(\exp(R^n)\), de modo que profundidad y frecuencia quedan mezcladas. En
cambio,

\[
 {1+z_n\over1+e^{-\tau}z_n}\longrightarrow e^\tau
 \qquad(z_n\to\infty).                                  \tag{22a}
\]

Un sitio malo profundo y uno todavía más profundo tienen el mismo costo
asintótico. Por eso el crecimiento de la razón es lineal en el número de
sitios malos en escala logarítmica, como muestran (12) y (31), en vez de
estar dominado por la peor excursión. Esta mejora es la que permite usar
la conclusión de densidad/sindeticidad de `104_56` sin volver a exigir una
cota individual para \(e^{-\lambda_n}\).

### 4.2 Lo que no mejora: la transición emparejada

Escriba

\[
 C_{n,\varepsilon}
 =A_n+p_n(\varepsilon)+\log(n+1),\qquad
 Q=Q_{n,\varepsilon}.
\]

Entonces

\[
 z_{n,\varepsilon}=e^{Q-C_{n,\varepsilon}},
\]

y el factor de (21) puede escribirse sin una actividad separada:

\[
 \mathcal R_\tau(C,Q)
 ={e^C+e^Q\over e^C+e^{-\tau}e^Q}
 ={1+e^{Q-C}\over1+e^{-\tau}e^{Q-C}}.                    \tag{22}
\]

La traslación común desaparece:

\[
 \mathcal R_\tau(C+T,Q+T)=\mathcal R_\tau(C,Q).            \tag{23}
\]

Esto explica la saturación, pero también localiza la información faltante:
solo importa la diferencia firmada

\[
 Q-C=-\{\lambda_{n,\varepsilon}+\log(n+1)\}.               \tag{24}
\]

**Lema 4.1 (inestabilidad de separación).** Para \(a>0\) y cualquier
\(T\in\mathbb R\),

\[
\begin{aligned}
 \mathcal R_\tau(T,T-a)
 &={1+e^{-a}\over1+e^{-\tau-a}}\longrightarrow1,\\
 \mathcal R_\tau(T,T+a)
 &={1+e^{a}\over1+e^{a-\tau}}\longrightarrow e^\tau
\end{aligned}
 \qquad(a\to\infty).                                      \tag{25}
\]

Los dos pares de entrada difieren solo en \(2a\) en la coordenada \(Q\),
independientemente del tamaño común \(T\). Si \(|T|\to\infty\) y
\(a=o(|T|)\), su perturbación relativa tiende a cero mientras las salidas
permanecen separadas por \(e^\tau-1+o(1)\).

En la diagonal (15), para \(n=X_L\),

\[
 \log|p_n(\varepsilon_L)-1|
 ={X_L^2\over100}+o(1).                                   \tag{26}
\]

El canal primo posee el mismo término dominante y (24) es su diferencia
finita. Tomando, por ejemplo, \(a=X_L\), el lema muestra que distinguir
entre las dos zonas saturadas exige precisión relativa

\[
 \boxed{\exp\{-X_L^2/100+O(\log X_L)\}.}                   \tag{27}
\]

Para resolver la propia franja de transición \(Q-C=O_\tau(1)\), el costo
es incluso

\[
 \boxed{\exp\{-X_L^2/100+O(1)\}.}                          \tag{28}
\]

La razón cancela el **valor** de una actividad ya identificada como enorme,
pero no permite decidir si es enorme o diminuta sin conocer antes el signo
de la diferencia completa. Tomar módulos o acotar \(C\) y \(Q\) por
separado no determina (22).

Éste es un no-go para separación de canales. No descarta una identidad
firmada que estime directamente \(Q-C\) o el producto completo (21).

---

## 5. Cuarteto falsificador

Para

\[
 Q_n^{\mathrm{off}}
 =4-2\operatorname {Re}\{(2i)^n+(2i)^{-n}\},              \tag{29}
\]

se tiene

\[
 g_\tau(Q_n^{\mathrm{off}}+\log(n+1))
 \longrightarrow
 \begin{cases}
 1,&n\equiv0\pmod4,\\
 0,&n\not\equiv0\pmod4.
 \end{cases}                                               \tag{30}
\]

Todo bloque \(I_L\) contiene \(L/4+O(1)\) múltiplos de cuatro. Por tanto

\[
 \boxed{
 {G_L^{\mathrm{off}}\over L}\longrightarrow{1\over4},
 \qquad
 e^{\tau G_L^{\mathrm{off}}}
 =\exp\{(\tau/4+o(1))L\}.}                                \tag{31}
\]

La razón permanece dentro del techo \(e^{\tau L}\), pero rechaza
cuantitativamente el divisor off-line.

---

## 6. Veredicto

**Probado:** el criterio (4), la dicotomía lineal (11)--(12), la razón
acotada (5)/(14), el lift diagonal (19)--(21), el lema de separación
(25)--(28) y el cuarteto (31).

**Ganancia:** reemplazar la partición positiva por una razón de presiones
elimina la explosión exterior de las actividades grandes y produce factores
uniformemente acotados.

**No-go:** la transición depende exclusivamente de la diferencia
prima--polo completa. La saturación posterior no reduce la precisión
necesaria para decidir su signo.

**No probado:** \(G_L\to0\) desde los pesos reales \(\Lambda(m)\), A1 o RH.

---

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 bounded_pressure_ratio_check.py
```

El checker verifica (1), las cotas de cada factor, el máximo de sensibilidad,
la dicotomía del lema 4.1, el cuarteto y la escala diagonal. Los teoremas
asintóticos se prueban en el texto.
