# 104_83 — Gate Fourier de \(\Xi\): cumulantes exactos y cancelación modular de borde

**Resultado.** La representación theta positiva lleva el observable profundo
de `104_75` a una fórmula exacta en los cumulantes de una única ley de
probabilidad. Esa fórmula no da una desigualdad nueva: el logaritmo conserva
todos los ceros de \(\xi\), y el evento profundo es precisamente una cola de
la transformada binomial de todos los cumulantes.

La auditoría Fourier sí produce un falsificador específico del kernel de
Riemann. Escribiendo el kernel como suma de sus modos theta,

\[
 \Phi(u)=\sum_{m\ge1}f_m(u),\qquad
 f_m(u)=\pi m^2e^{5u/2}(2\pi m^2e^{2u}-3)
          e^{-\pi m^2e^{2u}},                                  \tag{1}
\]

se sabe por `103_47` que la cola puntual satisface
\(0<(\Phi-f_1)/f_1<1/300\). Sin embargo, la modularidad obliga a

\[
 \Phi^{(2j+1)}(0)=0\quad(j\ge0),                                \tag{2}
\]

mientras \(f_1'(0)>0\). En consecuencia, la cola, aunque puntualmente
menor que \(1/300\), cancela **exactamente el cien por ciento** del primer
jet impar. En Fourier la pérdida es completa:

\[
 C_1(t):=\int_0^\infty f_1(u)\cos(tu)\,du
       =-{f_1'(0)\over t^2}+O(t^{-4}),                           \tag{3}
\]

\[
 C_{\ge2}(t):=\int_0^\infty(\Phi-f_1)(u)\cos(tu)\,du
       ={f_1'(0)\over t^2}+O(t^{-4}),
 \qquad {C_{\ge2}(t)\over C_1(t)}\longrightarrow-1.            \tag{4}
\]

Así, dominancia del primer modo, truncación de modos, PF de orden finito y
cotas puntuales de la cola no controlan el observable profundo. La única
posibilidad theta que sobrevive debe usar simultáneamente **todos** los
pesos modulares, **todas** las cancelaciones (2), y el logaritmo antes de
extraer coeficientes. No se demuestra aquí esa desigualdad restante, el
límite profundo ni RH.

---

## 1. La coordenada probabilística exacta

La identidad theta, con una constante positiva irrelevante, es

\[
 \xi(s)=c\int_{\mathbb R}\Phi(|u|)e^{(s-1/2)u}\,du.             \tag{5}
\]

Defina la probabilidad inclinada

\[
 d\nu(u)={\Phi(|u|)e^{u/2}\,du
            \over\int_{\mathbb R}\Phi(|v|)e^{v/2}\,dv},
 \qquad U\sim\nu.                                                \tag{6}
\]

Entonces, para todo \(t\in\mathbb C\),

\[
 M(t):=\mathbb E e^{tU}={\xi(1+t)\over\xi(1)}.                 \tag{7}
\]

Como \(1/(1-z)=1+z/(1-z)\), la identidad generadora de Li da

\[
 \boxed{
 \sum_{n\ge1}{\lambda_n\over n}z^n
 =\log\mathbb E\exp\!\left({z\over1-z}U\right).}              \tag{8}
\]

Si \(\kappa_j\) es el cumulante de orden \(j\) de \(U\), la expansión
es absolutamente legítima cerca de cero y produce

\[
 \boxed{
 \lambda_n
 =\sum_{j=1}^n{\binom nj\over(j-1)!}\,\kappa_j.}               \tag{9}
\]

Por tanto el observable profundo es exactamente

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
  \sum_{j=1}^n{\binom nj\over(j-1)!}\kappa_j+\log(n+1)
  \le-e^{\sqrt X}\right\}}.                                   \tag{10}
\]

La positividad de \(\nu\) prueba \(\kappa_2\ge0\), pero no fija los
cumulantes superiores. Más decisivamente, \(\log M\) tiene singularidades
exactamente en los ceros de \(M\). Una cota de Cauchy para sus coeficientes
que atraviese el primer cero interior ya presupone la ausencia de ese cero.
Así (8) no elimina la obstrucción meromorfa de `104_80`; la expresa con una
sola ley positiva.

## 2. Auditoría PF/total-positiva

La log-concavidad estricta del kernel real \(\Phi(|u|)\) fue probada en
`103_34`; esto proporciona la información de orden dos. No se puede elevar
silenciosamente a PF\(_\infty\).

En efecto, la caracterización de Schoenberg de las funciones de frecuencia
de Pólya dice que, si una función integrable no nula es PF\(_\infty\), su
transformada bilateral de Laplace es, en su franja de convergencia, el
recíproco de una función entera de Laguerre--Pólya. En particular esa
transformada no tiene ceros donde es finita. Aquí

\[
 \int_{\mathbb R}\Phi(|u|)e^{itu}\,du=c^{-1}\xi(1/2+it)       \tag{11}
\]

tiene infinitos ceros reales incondicionalmente. Luego el kernel de
traslación asociado a la \(Phi\) real **no es PF\(_\infty\)**.

Esto no contradice el PF de orden dos. Solo demuestra que alguna menor de
orden finito superior debe fallar; no hace falta adivinarla ni usar un
cálculo decimal. Por otra parte, imponer PF/Jensen a todos los órdenes a la
sucesión central

\[
 c_N={1\over(2N)!}\int_{\mathbb R}u^{2N}\Phi(|u|)\,du           \tag{12}
\]

es precisamente la pertenencia de \(\Xi\) a Laguerre--Pólya, equivalente
a RH (`103_31`). Por tanto:

```text
PF de traslación infinito: falso para el kernel real;
PF/Jensen central infinito: criterio equivalente a RH;
PF de cualquier orden fijo: insuficiente para (10).
```

## 3. El primer jet ya destruye la dominancia modal

La derivada logarítmica del primer modo en cero es

\[
 {f_1'(0)\over f_1(0)}
 ={5\over2}+{4\pi\over2\pi-3}-2\pi
 ={15\pi-4\pi^2-15/2\over2\pi-3}.                     \tag{13}
\]

Es estrictamente positiva con un certificado racional. La función
\(g(x)=15x-4x^2-15/2\) decrece para \(x\ge3\), y \(\pi<22/7\); por tanto

\[
 g(\pi)>g(22/7)={13\over98}>0.                                 \tag{14}
\]

La transformación modular hace que \(\Phi(|u|)\) sea suave y par. En
particular \(\Phi'(0)=0\). La serie de derivadas de (1) converge
absolutamente en cero por el factor \(e^{-\pi m^2}\), de modo que

\[
 \boxed{\sum_{m\ge2}f_m'(0)=-f_1'(0)<0.}                        \tag{15}
\]

El contraste con la cota puntual es exacto:

\[
 0<\sum_{m\ge2}f_m(0)<{f_1(0)\over300},
 \qquad
 \sum_{m\ge2}f_m'(0)=-f_1'(0).                                \tag{16}
\]

La diferenciación amplifica los modos superiores por potencias de
\(m^2\); no existe una estimación de Fourier que conserve el factor
\(1/300\) sin contabilizar esta cancelación.

## 4. Prueba de la cancelación Fourier completa

Todas las derivadas de \(f_1\) son integrables en \([0,\infty)\). Cuatro
integraciones por partes dan

\[
 C_1(t)=-{f_1'(0)\over t^2}
        +{f_1'''(0)\over t^4}
        +{1\over t^4}\int_0^\infty f_1^{(4)}(u)\cos(tu)\,du.   \tag{17}
\]

Esto prueba (3), y en particular \(C_1(t)<0\) para todo \(t\)
suficientemente grande.

Para el kernel completo, la paridad suave da (2), y todas sus derivadas
son integrables. Repitiendo la integración por partes \(2N\) veces,

\[
 C(t):=\int_0^\infty\Phi(u)\cos(tu)\,du=O_N(t^{-2N})
 \qquad(N\ge1).                                                 \tag{18}
\]

Como \(C_{\ge2}=C-C_1\), las ecuaciones (17)--(18), con \(N=3\),
prueban (4). En particular, en cada cero crítico suficientemente alto
\(\gamma\) de \(\Xi\),

\[
 C_{\ge2}(\gamma)=-C_1(\gamma),                                \tag{19}
\]

y ambos miembros son no nulos. Hay infinitos tales ceros por el teorema
incondicional de Hardy y por el signo eventual de \(C_1\). La cola theta
no es una perturbación Fourier pequeña: es el término que cancela todos
los jets algebraicos del modo principal.

## 5. La identidad residual que conserva todos los pesos y la modularidad

La traducción exacta de `103_47`,

\[
 f_m(u)=m^{-1/2}f_1(u+\log m),                                  \tag{20}
\]

permite reordenar el kernel completo sin retirar ningún modo. Para todo
\(w\in\mathbb C\), por convergencia absoluta localmente uniforme,

\[
\begin{aligned}
 \int_0^\infty\Phi(u)\cosh(wu)\,du
  =\int_0^\infty f_1(v)
   \sum_{m\le e^v}m^{-1/2}
       \cosh\!\bigl(w(v-\log m)\bigr)\,dv.             \tag{21}
\end{aligned}
\]

En efecto, se sustituye (20) y en el término \(m\) se cambia
\(v=u+\log m\). El dominio pasa a ser \(v\ge\log m\); al intercambiar
la suma y la integral sobreviven exactamente los enteros \(m\le e^v\).
Equivalentemente, el corchete de (21) es

\[
 {1\over2}\left\{
 e^{wv}\sum_{m\le e^v}m^{-1/2-w}
 +e^{-wv}\sum_{m\le e^v}m^{-1/2+w}\right\}.           \tag{22}
\]

Esta es la posibilidad residual que conserva simultáneamente los pesos
exactos de la suma theta, los desplazamientos modulares y la fase
compleja. Para \(w\) real el integrando es positivo. Para
\(w=b+it\), \(b\ne0\), las dos sumas de (22) son complejas y no tienen
signo; su no anulación para todo \(t\) es justamente la localización de
ceros que falta. Sustituirlas por su término integral, acotarlas por
módulos o truncar \(m\) destruye las cancelaciones (2)--(4).

La identidad (21) es por tanto un punto de entrada legítimamente
theta-específico. No es una prueba de que su integral sea no nula fuera del
eje imaginario.

## 6. Consecuencia para Deep-\(\Lambda\)

Las ecuaciones (8)--(10) muestran que una desigualdad de densidad puede
formularse enteramente con el kernel positivo. Las ecuaciones (15)--(19)
prueban que no puede obtenerse mediante ninguno de estos pasos:

1. retirar los modos \(m\ge2\) por su tamaño puntual;
2. conservar un número finito de cancelaciones de borde;
3. usar PF/TP de orden fijo y pasar después al límite;
4. sustituir el logaritmo de (8) por la transformada lineal (11).

El único sucesor Fourier no falsificado es una desigualdad **no local y a
todos los órdenes** para la suma modular completa, aplicada después del
logaritmo. Debe usar simultáneamente los pesos exactos
\(m^{-1/2}\), los desplazamientos \(\log m\) de `103_47`, y la familia
entera (2), por ejemplo directamente mediante (21)--(22). Separar
cualquiera de esas tres piezas vuelve a (3)--(4).

Este sucesor es una especificación precisa, no un lema ya demostrado. El
presente documento cierra el ataque por dominancia/PF Fourier, pero no
prueba (10), Deep-\(\Lambda\), A1 ni RH.

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 xi_fourier_deep_gate_check.py
```

El checker certifica con `Fraction` el signo (14), verifica la cancelación
de los primeros cuatro jets impares por suma theta y muestra, solo como
diagnóstico de cuadratura, la cancelación Fourier en los tres primeros
ceros críticos. La prueba de (3)--(4) es la integración por partes anterior
y no depende del punto flotante.
