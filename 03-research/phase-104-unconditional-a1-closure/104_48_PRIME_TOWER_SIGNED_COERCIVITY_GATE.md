# 104_48 — Fase cerrada por torre prima y gate de multiplicidad unitaria

**Objetivo del ataque.** Se intenta probar directamente

\[
 B_n=A_n-\lambda_n\le \kappa A_n,
 \qquad \kappa={1501\over2002},\qquad n\ge150,              \tag{1}
\]

usando la rigidez

\[
 \Lambda(p^k)=\log p\qquad(k\ge1)                           \tag{2}
\]

antes de estimar. Se obtiene una suma cerrada por torre que conserva toda
la fase Laguerre y una desigualdad unilateral exacta. Sin embargo, la
desigualdad tiene la dirección incorrecta para (1), y sobrevive sin cambios
esenciales al falsificador desplazado

\[
 \omega_c(m)=2\Lambda(m)\cosh(c\log m),\qquad 0<c<1/2.      \tag{3}
\]

También se obtiene un no-go cuantitativo más estrecho: positividad, soporte
en las potencias primas, PNT y **constancia exacta a lo largo de cada
torre** no bastan. Aumentar la multiplicidad de una sola torre completa
rompe cualquier cota proporcional ya en \(n=151\), conservando todas esas
propiedades. Por tanto el input futuro debe usar la multiplicidad unitaria
exacta de cada primo, equivalentemente la identidad global de renovación

\[
 \sum_{d\mid m}\Lambda(d)=\log m.                           \tag{4}
\]

Pero (4) determina a \(\Lambda\) de manera única; al incorporarla mediante
el selector divisor se vuelve exactamente a `104_43`--`104_47`. Este
ataque no prueba (1), A1 ni RH.

## 0. Auditoría de no duplicación

El documento 103_66 telescopa una torre en annuli multiplicativos y,
después de sumar en todos los primos, obtiene el germ normalizado. No
calcula la fase cerrada (12) de una torre individual. El documento 104_20
factoriza diferencias locales de torres dentro de un cuadrado operacional
y prueba ambos signos; no usa la suma de Poisson. El documento 104_47
introduce ya el falsificador (3), pero no comprueba si una desigualdad
firmada derivada de la constancia de torre lo acepta o lo rechaza.

La fibra singleton (33) y falsificadores asintóticos de coherencia de torre
ya aparecen en E101_089, §§9--10. No se reclaman de nuevo. Las adiciones
estrechas de este documento son: la fase cerrada (12), la prueba de que su
signo automático acepta (3), y el testigo finito (24)--(31), que rompe el
margen directamente en \(n=151\) alterando una sola torre completa.

## 1. Suma cerrada de una torre completa

Escribamos

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad
 \Phi_n(x)=\sum_{k\ge1}e^{-kx}P_n(kx),\qquad x>0.           \tag{5}
\]

Para \(a>2\), la forma Euler--polo completa de `104_41` se agrupa
absolutamente por primos como

\[
 \boxed{
 \mathcal B_{n,a}
 =a\sum_p(\log p)\Phi_n(a\log p)-Q_{n,a},}
 \qquad
 Q_{n,a}=a\int_0^\infty e^{-(a-1)u}P_n(au)\,du.            \tag{6}
\]

La transformada de Laplace de \(P_n\) es

\[
 \int_0^\infty e^{-su}P_n(u)\,du
 =1-\left(1-{1\over s}\right)^n,
 \qquad \Re s>0.                                           \tag{7}
\]

En particular,

\[
 \boxed{Q_{n,a}=1-\left({-1\over a-1}\right)^n.}          \tag{8}
\]

La torre (5) tiene dos formas cerradas adicionales. La generatriz de
Laguerre da

\[
 \boxed{
 \sum_{n\ge1}\Phi_n(x)z^{n-1}
 ={1\over(1-z)^2\{e^{x/(1-z)}-1\}}.}                       \tag{9}
\]

Si \(A_j(q)\) es el polinomio euleriano, normalizado por

\[
 \sum_{k\ge1}k^j q^k={qA_j(q)\over(1-q)^{j+1}},            \tag{10}
\]

entonces, con \(q=e^{-x}\),

\[
 \boxed{
 \Phi_n(x)=
 \sum_{j=0}^{n-1}{n\choose j+1}{(-x)^j\over j!}
 {qA_j(q)\over(1-q)^{j+1}}.}                               \tag{11}
\]

Las fórmulas (6), (9) y (11) no separan las potencias superiores ni toman
valores absolutos. A diferencia del telescopado de annuli de `103_66`, (9)
retiene explícitamente la fase de una torre individual. Al sumar en
primos, naturalmente recompone el mismo germ normalizado de `103_66`; no
se reclama una segunda reducción de A1.

## 2. Fórmula de Poisson y la única dirección automática

La función \(t\mapsto e^{-xt}P_n(xt){\bf1}_{t\ge0}\) tiene variación
acotada y decaimiento exponencial. La fórmula de Poisson unilateral, con
medio peso en cero, y (7) dan

\[
 \boxed{
 \Phi_n(x)
 ={1\over x}-{n\over2}
 +{2\over x}\sum_{\ell\ge1}
 \Re\left\{1-w_{\ell}(x)^n\right\},}
 \qquad
 w_\ell(x)={2\pi i\ell\over x+2\pi i\ell}.                \tag{12}
\]

La serie de (12) converge absolutamente: su sumando real es
\(O_n(x^2/\ell^2)\). Además

\[
 |w_\ell(x)|<1,
 \qquad
 \Re\{1-w_\ell(x)^n\}\ge1-|w_\ell(x)|^n>0.               \tag{13}
\]

Por consiguiente la rigidez de una torre sí produce un signo, pero es

\[
 \boxed{\Phi_n(x)>{1\over x}-{n\over2}.}                   \tag{14}
\]

La obligación (1) necesita una **cota superior** para la suma prima menos
el polo. La desigualdad (14) es inferior. Tampoco puede invertirse por un
signo puntual ni sumarse en (6): su lado derecho tiende a \(-n/2\) cuando
\(x\to\infty\), de modo que la suma de esos minorantes sobre los primos
diverge a \(-\infty\). Es una desigualdad exacta de una torre, no una
minoración global finita. Además, como

\[
 P_n(x)={(-1)^{n-1}x^{n-1}\over(n-1)!}+O_n(x^{n-2}),       \tag{15}
\]

se tiene

\[
 \Phi_n(x)=e^{-x}P_n(x)+O_n(e^{-2x}x^{n-1}),               \tag{16}
\]

y por tanto \(\Phi_n(x)\) tiene signo \((-1)^{n-1}\) para
\(x\) suficientemente grande.

## 3. El signo de fase también acepta los pesos desplazados

Para ver exactamente qué distingue (12), definamos, para \(r>0\),

\[
 \Phi_{n,r}(x)=\sum_{k\ge1}e^{-rkx}P_n(kx).                \tag{17}
\]

La misma prueba da

\[
\begin{aligned}
 \Phi_{n,r}(x)
 ={}&{1\over x}\left\{1-\left(1-{1\over r}\right)^n\right\}
      -{n\over2}\\
 &+{2\over x}\sum_{\ell\ge1}
 \Re\{1-w_{\ell,r}(x)^n\},                               \tag{18}\\
 w_{\ell,r}(x)
 ={}&{r-1+2\pi i\ell/x\over r+2\pi i\ell/x}.
\end{aligned}
\]

La identidad elemental

\[
 1-|w_{\ell,r}(x)|^2
 ={2r-1\over r^2+(2\pi\ell/x)^2}                           \tag{19}
\]

muestra que todos los sumandos de fase en (18) siguen siendo positivos
para \(r>1/2\).

Ahora, torre por torre,

\[
\begin{aligned}
 &\sum_{k\ge1}{\omega_c(p^k)\over p^{ka}}
       P_n(ak\log p)\\
 &\qquad=(\log p)
 \left\{\Phi_{n,1-c/a}(a\log p)
          +\Phi_{n,1+c/a}(a\log p)\right\}.                \tag{20}
\end{aligned}
\]

Como \(a>1\) y \(0<c<1/2\), las dos tasas de (20) son mayores que
\(1/2\). Así, la positividad de fase (13) sobrevive completa al sistema
desplazado. No puede ser el input que pruebe (1).

Esta conclusión no es solo diagnóstica. Póngase

\[
 \Xi_c(s)=\xi(s+c)\xi(s-c).                                \tag{21}
\]

Su derivada logarítmica de Euler tiene exactamente los pesos (3), y
\(\Xi_c(1-s)=\Xi_c(s)\). Si
\(\rho=1/2+i\gamma\) es un cero crítico de \(\xi\), (21) tiene el
cuarteto

\[
 \rho-c,\quad\bar\rho-c,\quad\rho+c,\quad\bar\rho+c,      \tag{22}
\]

fuera de la línea de simetría. Para
\(w=1-(\rho-c)^{-1}=e^{\alpha+i\theta}\), \(\alpha>0\), la respuesta
de ese cuarteto al coeficiente de Li es

\[
 4-4\cosh(n\alpha)\cos(n\theta).                           \tag{23}
\]

El fallo ocurre en grados arbitrariamente grandes, no solo en un
coeficiente inicial. En efecto, para los ceros \(\eta\) de (21) ponga
\(w_\eta=1-\eta^{-1}\). Como \(|w_\eta|\to1\) cuando
\(|\Im\eta|\to\infty\), el número

\[
 R=\max_\eta |w_\eta|>1                                   \tag{23a}
\]

se alcanza en un multiconjunto finito. Después de retirar ese conjunto,
existe \(R_2<R\) que domina los restantes \(w_\eta\) exteriores al disco
unidad. Si los dominantes son \(R e^{i\theta_1},\ldots,
R e^{i\theta_M}\), la expansión de Darboux de la función generadora de Li
(equivalentemente, separar esas singularidades finitas en el producto de
Hadamard) da

\[
 \lambda_n[\Xi_c]
 =-R^n\sum_{j=1}^{M}e^{in\theta_j}
   +O(R_2^n)+O_c(n\log n).                                 \tag{23b}
\]

El lado derecho es real porque el multiconjunto es estable por
conjugación. La aproximación simultánea de Dirichlet proporciona
infinitos \(n\) para los cuales todos los
\(e^{in\theta_j}\) están arbitrariamente cerca de \(1\). En esa
subsucesión,

\[
 \lambda_n[\Xi_c]\le-{M\over2}R^n                          \tag{23c}
\]

para \(n\) suficientemente grande. Ésta es también la prueba estándar de
la dirección obstructiva del criterio de Bombieri--Lagarias en este caso.
En particular, ninguna desigualdad proporcional positiva, uniforme para
los grados grandes, vale para (3). Las ecuaciones (18)--(20) muestran que
el signo automático obtenido por Poisson no detecta esa falsedad.

## 4. No-go mínimo conservando torres completas

El siguiente testigo conserva más estructura que el átomo primo simple de
`104_35`. Fijemos un primo \(p_0\) y un entero \(t\ge1\), y reemplacemos
solo su factor local por multiplicidad \(1+t\):

\[
 \zeta_t(s)=\zeta(s)(1-p_0^{-s})^{-t}.                     \tag{24}
\]

Los pesos de su derivada logarítmica son

\[
 \Lambda_t(p^k)=
 \begin{cases}
  (1+t)\log p_0,&p=p_0,\\
  \log p,&p\ne p_0,
 \end{cases}
 \qquad k\ge1.                                             \tag{25}
\]

Así, (25) conserva positividad, el soporte exacto en potencias primas y la
constancia en \(k\) de **cada torre completa**. También conserva PNT con el
mismo término principal, pues

\[
 \psi_t(x)-\psi(x)
 =t(\log p_0)\left\lfloor{\log x\over\log p_0}\right\rfloor
 =O_{t,p_0}(\log x).                                       \tag{26}
\]

Sin embargo, su cambio en el límite crítico de (6) es ordinariamente
convergente y vale exactamente

\[
 \boxed{B_n[\Lambda_t]-B_n[\Lambda]
 =t(\log p_0)\Phi_n(\log p_0).}                            \tag{27}
\]

La positividad de (27) puede certificarse sin cálculo de raíces. Sea
\(n=151\), \(N=n-1=150\), y escribamos

\[
 P_{151}(x)=\sum_{j=0}^{N}(-1)^j a_j(x),
 \qquad
 a_j(x)={151\choose j+1}{x^j\over j!}.                    \tag{28}
\]

Para \(0\le j<N\),

\[
 {a_{j+1}(x)\over a_j(x)}
 ={x(N-j)\over(j+1)(j+2)}
 \ge {x\over N(N+1)}.                                     \tag{29}
\]

Si \(x>N(N+1)=22650\), las magnitudes de (28) crecen
estrictamente. Como \(N\) es par, emparejar desde el término principal da

\[
 P_{151}(x)>0\qquad(x>22650).                               \tag{30}
\]

Por Bertrand existe un primo

\[
 2^{33977}<p_0<2^{33978}.
\]

La cota elemental \(\log2>2/3\) implica
\(\log p_0>22651\). Por (30),
\(P_{151}(k\log p_0)>0\) para todo \(k\ge1\), y entonces

\[
 \boxed{\Phi_{151}(\log p_0)>0.}                           \tag{31}
\]

Haciendo \(t\) arbitrariamente grande en (27) se viola cualquier cota
\(B_{151}\le C A_{151}\) con \(C\) fijo. Por tanto

```text
positividad + soporte p^k + constancia completa por torre + PNT
    no implica una cota proporcional para B_n.
```

El falsificador no satisface el valor unitario exacto de (2) en la torre
\(p_0\). Ése es precisamente el borde lógico que identifica.

## 5. La multiplicidad unitaria no deja una familia intermedia

La propiedad global que fija simultáneamente esas multiplicidades es (4),
o en convolución de Dirichlet,

\[
 \Lambda*{\bf1}=\log.                                      \tag{32}
\]

Como \({\bf1}^{-1}=\mu\), (32) tiene la única solución

\[
 \boxed{\Lambda=\mu*\log.}                                \tag{33}
\]

Esto ya fue aislado como «singleton fiber» en `E101_089`, §9. En
particular:

* usar solo constancia de torres deja entrar el testigo (24)--(31);
* imponer (32) elimina el testigo, pero selecciona exactamente a
  \(\Lambda\), sin un cono o una homotopía auxiliar;
* desintegrar (32) produce el selector divisor exacto de `104_43`, y su
  flujo firmado es el funcional equivalente al margen de `104_47`.

Por ello la suma cerrada (9)--(12) no suministra una nueva desigualdad
coerciva. El teorema todavía faltante debe ser una comparación **global y
no local** que use (32) junto con el test Laguerre, manteniendo el polo
hasta el final, y que pruebe directamente (1). Eso es exactamente la pieza
RH-strength aún abierta.

## 6. Veredicto

Queda probado incondicionalmente:

1. el cierre exacto por torre (6), (9) y (11);
2. la representación de fase de Poisson (12) y su cota unilateral (14);
3. que ese signo también vale para las dos torres desplazadas de (3);
4. el no-go de multiplicidad local (24)--(31), ya en \(n=151\);
5. que la renovación exacta (32) tiene la fibra singleton (33).

Queda descartado:

```text
fase unilateral por torre
+ positividad
+ constancia de los pesos a lo largo de p^k
+ PNT
    => B_n <= (1501/2002) A_n.
```

No queda descartada una desigualdad global que use la renovación exacta
(32) de manera no local. No se ha probado (1), A1 ni RH.

## 7. Verificación reproducible

`tools/prime_tower_signed_coercivity_gate_check.py` usa solo enteros,
`Fraction` y aritmética gaussiana racional. Verifica:

* los coeficientes de Laguerre y la transformada (7);
* la suma euleriana cerrada (11) para varios grados racionales;
* la identidad algebraica (19) y la positividad de los átomos de fase;
* la separación desplazada (20) a truncación finita;
* el crecimiento alternante (29)--(30) para \(n=151\);
* la identidad del cuarteto (23) sobre el test racional de `104_41`.

El checker no pretende certificar una suma infinita por truncación. La
fórmula de Poisson (12) se prueba analíticamente a partir de (7), y (31)
se sigue término a término de (30); el programa comprueba las identidades
algebraicas finitas que entran en esas dos pruebas.

Se reproduce con

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 prime_tower_signed_coercivity_gate_check.py
```
