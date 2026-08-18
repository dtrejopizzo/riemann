# 104_36 — Cholesky primos--polo y gate de dominio por residuos

**Estado.** El canal de primos simples--polo de `104_32` y `104_35`
admite una factorización de Cholesky/large-sieve exacta antes de llegar al
punto de Li. La factorización conserva conjuntamente todos los primos: su
norma es el módulo cuadrado de la diferencia prima--polo completa, no una
suma de valores absolutos por primo.

La continuación de esa norma al punto de Li, sin embargo, no existe. Cada
cero crítico produce un polo que se aproxima a la frontera de Hardy cuando
el regulador tiende a \(a\downarrow1\), y la norma cuadrada crece al menos
como \((a-1)^{-1}\). Un cero con \(\Re\rho>a/2\) coloca el polo dentro
del semiplano de Laplace y hace imposible incluso la pertenencia a
\(L^2(0,\infty)\). Para dos prefijos consecutivos, la pertenencia a
\(L^2\) ya implica que no hay tales ceros. En el límite \(a\downarrow1\)
esa condición contiene RH.

Por tanto el Cholesky natural no produce la coercividad de (26) en
`104_32`: pierde precisamente la cancelación firmada que mantiene finito el
momento escalar. El documento no prueba esa desigualdad, A1 ni RH.

## 1. Prerregistro y no duplicación

El blanco es

\[
 3A_n+4B_n^{(p+\mathrm{pole})}
 \ge {A_n\over1001}+4P_{n-1}^{(\ge2)}(1),            \tag{1}
\]

equivalente a (26) de `104_32`. Se ensaya una sola idea: escribir
\(B_{n,a}^{(p+\mathrm{pole})}\) como producto interno de un vector de
discrepancia prima--continua con el prefijo hard-edge, y usar una norma
cuadrática que conserve todos los términos cruzados.

`104_11` factoriza el kernel `max` de M1 y prueba que su Hessiana se cancela
al recomponer el funcional lineal. `104_31` estudia el flujo birth--death
en el grado. `104_33` lleva el símbolo de bandera a la línea crítica y
separa frontera y residuos. `104_35` obtiene la fórmula exacta en
\(\theta-x\) y descarta el Riccati de Selberg simple como fuente autónoma
de signo.

Lo nuevo aquí es distinto: se construye el vector de Cholesky global del
canal simple, se calcula su norma por Plancherel y se determina exactamente
su dominio mediante los residuos de \(Q(s)=\sum_p\log p\,p^{-s}\).

El falsificador es el cuarteto racional

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5}.       \tag{2}
\]

En el índice \(n=152\) su modo de Cholesky crece como
\(e^{3x/10}\) y no pertenece a \(L^2\). Así la factorización falla, en vez
de certificar falsamente, frente a un divisor off-line.

## 2. Semigrupo hard-edge y vector de discrepancia

Sea

\[
 \mathcal H=L^2(0,\infty),\qquad
 (S_tf)(x)=f(x-t){\bf1}_{x\ge t},\qquad
 T_t=e^{-t/2}S_t.                                      \tag{3}
\]

El semigrupo \(T_t\) es contractivo. Para

\[
 g_n(x)=e^{-x/2}L_{n-1}^{(1)}(x)                       \tag{4}
\]

la ortogonalidad de Laguerre y la identidad
\(L_{n-1}^{(1)}=\sum_{j=0}^{n-1}L_j\) dan

\[
 \|g_n\|_2^2=n.                                        \tag{5}
\]

La correlación de traslaciones de `104_28` se vuelve

\[
 \boxed{\langle T_tg_n,g_n\rangle
       =e^{-t}L_{n-1}^{(1)}(t).}                       \tag{6}
\]

Póngase

\[
 d\theta(y)=\sum_p\log p\,\delta_p(dy),
 \qquad d\sigma(y)=dy-d\theta(y).                     \tag{7}
\]

Para \(a>2\), la integral de Bochner

\[
 \boxed{
 V_{n,a}:=a\int_1^\infty T_{a\log y}g_n\,d\sigma(y)}   \tag{8}
\]

converge absolutamente en \(\mathcal H\), porque

\[
 \|T_{a\log y}g_n\|_2=\sqrt n\,y^{-a/2}
\]

y tanto \(\int_1^\infty y^{-a/2}dy\) como
\(\sum_p\log p\,p^{-a/2}\) convergen. De (6),

\[
\begin{aligned}
 \langle V_{n,a},g_n\rangle
 &={a}\int_1^\infty y^{-a}L_{n-1}^{(1)}(a\log y)
       \{dy-d\theta(y)\}\\
 &=B_{n,a}^{(p+\mathrm{pole})}.
\end{aligned}                                             \tag{9}
\]

La segunda igualdad es exactamente (4)--(6) de `104_35`, incluidos el
polo continuo y el signo. Por Cauchy--Schwarz,

\[
 B_{n,a}^{(p+\mathrm{pole})}
 \ge-\sqrt n\,\|V_{n,a}\|_2.                         \tag{10}
\]

Ésta es la cota inferior de tipo coercivo que (1) necesitaría si la norma
permaneciera uniformemente finita al retirar el regulador.

## 3. Identidad large-sieve exacta

Adoptemos

\[
 Q(s)=\sum_p{\log p\over p^s},\qquad
 M(s)={1\over s-1}-Q(s)                               \tag{11}
\]

en \(\Re s>1\). La transformada de Fourier de (4), extendida por cero a
la recta, es

\[
 \widehat g_n(t)
 =1-\left({-1/2+it\over1/2+it}\right)^n.              \tag{12}
\]

Para \(a>2\), todas las integraciones de (8) son absolutas y

\[
 \boxed{
 \widehat V_{n,a}(t)
 =a\widehat g_n(t)M\!\left(a(1/2+it)\right).}          \tag{13}
\]

Plancherel da el Cholesky colectivo buscado:

\[
 \boxed{
 \|V_{n,a}\|_2^2
 ={a^2\over2\pi}\int_{-\infty}^{\infty}
 |\widehat g_n(t)|^2
 \left|M\!\left(a(1/2+it)\right)\right|^2dt.}        \tag{14}
\]

La suma sobre primos y el polo se forman dentro de \(M\) antes de tomar el
módulo. Al expandir (14) aparecen todas las interacciones entre dos primos
y entre primos y continuo. No se ha usado positividad término a término ni
la desigualdad triangular en la suma de Euler.

El problema de (14) no es algebraico, sino su dominio: la condición
\(a>2\) coloca toda la recta de integración en el semiplano del producto de
Euler. Llegar a \(a=1\) mueve esa recta hasta la línea crítica.

## 4. Forma exacta en \(\theta-x\)

Aunque (8) no sea una integral de Bochner para \(a\le2\), define una
función localmente cuadrado-integrable punto a punto: para cada \(x\) solo
intervienen \(y\le X=e^{x/a}\). Sea

\[
 D_\theta(X)=X-1-\theta(X).                             \tag{15}
\]

Como

\[
 (T_{a\log y}g_n)(x)
 =e^{-x/2}L_{n-1}^{(1)}(x-a\log y){\bf1}_{y\le X},      \tag{16}
\]

una integración de Stieltjes, usando
\((L_{n-1}^{(1)})'=-L_{n-2}^{(2)}\), da para \(n\ge2\)

\[
 \boxed{
 V_{n,a}(x)=ae^{-x/2}\left[
 nD_\theta(X)-a\int_1^X{D_\theta(y)\over y}
 L_{n-2}^{(2)}(x-a\log y)\,dy\right].}              \tag{17}
\]

Para \(n=1\), el término integral desaparece:

\[
 \boxed{V_{1,a}(x)=ae^{-x/2}D_\theta(e^{x/a}),}        \tag{18}
\]

y por tanto

\[
 \boxed{\|V_{1,a}\|_2^2
 =a^3\int_1^\infty D_\theta(X)^2X^{-a-1}\,dX}         \tag{19}
\]

si cualquiera de los lados es finito. La norma de Cholesky ya contiene,
en su primer estado, la energía cuadrática completa del error de PNT. No
es un estimador más débil del momento lineal.

## 5. Transformada de Laplace y residuos de los ceros

Para \(\Re z>1/a-1/2\), la transformada de Laplace de (17) se puede calcular
en el semiplano de convergencia absoluta. Definiendo

\[
 G_n(z)=\int_0^\infty e^{-zx}g_n(x)\,dx
 =1-\left({z-1/2\over z+1/2}\right)^n,                \tag{20}
\]

se obtiene

\[
 \boxed{
 \mathcal L V_{n,a}(z)
 =aG_n(z)M\!\left(a(z+1/2)\right).}                  \tag{21}
\]

La continuación meromorfa relevante no necesita separar potencias primas.
Si

\[
 \mathcal L_\zeta(s)=-{\zeta'\over\zeta}(s),
\]

la inversión de Möbius da

\[
 Q(s)=\sum_{k\ge1}\mu(k)\mathcal L_\zeta(ks).         \tag{22}
\]

En \(\Re s>1/2\), los términos \(k\ge2\) son regulares y la serie converge
normalmente en compactos, salvo el borde \(s=1/2\). Por ello, si \(\rho\)
es un cero no trivial de multiplicidad \(m_\rho\), entonces \(M\) tiene en
\(s=\rho\) residuo \(+m_\rho\).

La ecuación (21) tiene entonces un polo en

\[
 z_{\rho,a}={\rho\over a}-{1\over2}                   \tag{23}
\]

con residuo exacto

\[
 \boxed{
 \mathop{\mathrm{Res}}_{z=z_{\rho,a}}
 \mathcal LV_{n,a}(z)
 =m_\rho\left[1-\left(1-{a\over\rho}\right)^n\right].} \tag{24}
\]

Esto da un gate de dominio, no solo una cota mala. Si
\(V_{n,a}\in L^2(0,\infty)\), su transformada de Laplace es holomorfa en
\(\Re z>0\). En consecuencia, para cada cero con
\(\Re\rho>a/2\) necesariamente

\[
 \left(1-{a\over\rho}\right)^n=1.                   \tag{25}
\]

La condición (25) no puede valer para dos índices consecutivos. Si valiera
para \(n\) y \(n+1\), su cociente daría \(1-a/\rho=1\), imposible. Se ha
probado así:

> **Teorema de dominio.** Si \(V_{n,a}\) y \(V_{n+1,a}\) pertenecen a
> \(L^2(0,\infty)\), entonces \(\zeta\) no tiene ceros en
> \(\Re s>a/2\). En particular, disponer de la factorización de Hilbert
> para todos los prefijos \(n\ge150\) y para \(a\downarrow1\) ya excluye
> todos los ceros con \(\Re\rho>1/2\), es decir, ya contiene RH por la
> simetría funcional.

No se ha supuesto una fórmula explícita para demostrar este teorema: basta
la unicidad de la transformada de Laplace de una función \(L^2\) y el
residuo (24).

## 6. Los ceros críticos hacen divergir la norma aun bajo RH

El problema persiste incluso si todos los ceros son críticos. Fijemos un
cero \(\rho=1/2+i\gamma\) y un índice \(n\) para el cual

\[
 1-\left(1-{1\over\rho}\right)^n\ne0.                \tag{26}
\]

Tal cero existe para todo \(n\): hay infinitos ceros críticos, mientras
que (26) puede fallar solo cuando \(1-1/\rho\) pertenece al conjunto finito
de raíces \(n\)-ésimas de la unidad.

Para \(a>1\), el polo (23) está a distancia

\[
 \delta_a={a-1\over2a}                                      \tag{27}
\]

a la izquierda del eje imaginario. Aislando ese polo en un disco sin otros
ceros, (21) tiene sobre la frontera la forma

\[
 aG_n(it)M(a(1/2+it))
 ={R_{n,a}\over\delta_a+i(t-\gamma/a)}+H_{n,a}(t),     \tag{28}
\]

donde \(R_{n,a}\) tiende al valor no nulo de (26) multiplicado por
\(m_\rho\), y \(H_{n,a}\) queda uniformemente acotada en un intervalo fijo
tras sustraer la parte principal. Integrando el cuadrado en ese intervalo,

\[
 \int {dt\over\delta_a^2+(t-\gamma/a)^2}
 \asymp{1\over\delta_a},                                  \tag{29}
\]

se obtiene, para \(a\downarrow1\),

\[
 \boxed{\|V_{n,a}\|_2^2\ge {c_{n,\rho}\over a-1}}
 \qquad(c_{n,\rho}>0),                                     \tag{30}
\]

si la continuación pertenece a \(L^2\). En \(a=1\) el polo cae exactamente
sobre la frontera y el multiplicador no es cuadrado-integrable.

La divergencia (30) es incondicional porque la existencia de infinitos
ceros sobre la línea crítica es el teorema de Hardy. La cantidad escalar
\(B_{n,a}^{(p+\mathrm{pole})}=\langle V_{n,a},g_n\rangle\) sí tiene límite
finito: la proyección contra el test fijo \(g_n\), que decae
exponencialmente, integra cada modo de frontera. La norma de Cholesky
elimina ese test amortiguador y eleva al cuadrado el polo de frontera.

## 7. Falsificador off-line cuantitativo

Para el cuarteto (2),

\[
 \Re\rho-{1\over2}={3\over10}.                       \tag{31}
\]

En \(a=1\) y \(n=152\),

\[
 G_{152}(\rho-1/2)
 =1-w^{152}=1-2^{-152}>0.                              \tag{32}
\]

Por (23)--(24), el vector de Cholesky tendría un modo no nulo proporcional
a

\[
 e^{(3/10+2i/5)x},                                      \tag{33}
\]

que no pertenece a \(L^2(0,\infty)\). Para fijar la normalización, la
contribución de este cuarteto al coeficiente de Li es

\[
 Q_n^{\mathrm{off}}
 :=4-2\Re(w^n+w^{-n})
 =4-4\cosh(n\log2)\cos(n\pi/2).                      \tag{34}
\]

Como \(152\equiv0\pmod4\),

\[
 \boxed{Q_{152}^{\mathrm{off}}
 =4-4\cosh(152\log2)<0.}                               \tag{35}
\]

Así el mecanismo no es ciego al falsificador: su dominio se rompe antes de
producir una desigualdad falsa. `tools/simple_prime_cholesky_gate.py`
verifica (31)--(32) y las transformadas racionales de Laguerre con
`Fraction`.

## 8. Consecuencia para el frente proporcional

De (10), una condición suficiente para (1) habría sido

\[
 \sqrt n\,\liminf_{a\downarrow1}\|V_{n,a}\|_2
 \le {\left(3-1/1001\right)A_n
          -4P_{n-1}^{(\ge2)}(1)\over4}.                \tag{36}
\]

El lado derecho es finito. El lado izquierdo diverge por (30). Por tanto
(36), y toda prueba que aplique Cauchy a este vector sin una resta adicional,
queda descartada.

Restar los modos (24) antes de tomar la norma vuelve finita la construcción,
pero exige identificar todos los residuos críticos y decidir qué hacer con
los residuos interiores off-line. Al devolver esas contribuciones a la
proyección sobre \(g_n\), se recuperan exactamente los términos de Li que
la desigualdad pretende controlar. Esa renormalización no es una cota nueva.

## Decisión

```text
probado incondicionalmente:
  vector de discrepancia prima--polo (8) para a>2;
  identidad escalar (9) y Cholesky/large-sieve colectivo (14);
  fórmula exacta en theta-x (17)--(19);
  transformada de Laplace (21) y residuo de cada cero (24);
  dos prefijos L2 consecutivos => región Re rho <= a/2;
  divergencia de norma >= c/(a-1) por un cero crítico;
  ruptura exponencial para el cuarteto racional off-line.

descartado:
  Cauchy--Schwarz sobre el vector global como cierre de (1);
  continuar la norma segura a=2+ hasta a=1 sin pagar residuos;
  llamar "large sieve" a la resta de esos residuos sin reinsertar Li.

permanece abierto:
  una cota unilateral de la proyección firmada
  <V_{n,a},g_n> que sobreviva al límite sin controlar la norma completa;
  (1), A1 y RH.
```
