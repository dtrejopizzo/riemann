# 104_115 — Gate del resolvente global y pivote a torres primas vecinas

## Resultado

Se auditó el certificado escalar propuesto

\[
 \left\|(-S_\varepsilon)^{1/2}g_n+
 {\eta_n\over2}(-S_\varepsilon)^{-1/2}C_\varepsilon g_n
 \right\|_{\pi_\varepsilon}^{2},
 \qquad C_\varepsilon=i[X,S_\varepsilon].                 \tag{1}
\]

El generador global de intercambios entre todas las torres no define un
operador de Markov en el régimen de Abel (\varepsilon\downarrow0). Aun
si se lo trunca, el término cruzado de (1) es idénticamente cero para el
vector Laguerre real y la ecuación de Poisson no satisface en general la
condición de compatibilidad con el núcleo por capas. Por tanto (1) no
puede ser el certificado de A1 tal como fue enunciado.

El pivote a intercambios entre primos consecutivos sí produce un generador
autoadjunto bien definido. Después de proyectar las constantes de cada
capa, la ecuación de Poisson se resuelve y el término resolvente es
positivo. Un twist complejo recupera un término de fase, pero éste cambia
de signo con el grado Laguerre. El sucesor correcto no es otro certificado
escalar: debe ser un lift de al menos dos componentes que acople grados
Laguerre adyacentes mediante una corriente local entre torres.

Este documento prueba el gate y construye el operador local. No prueba
A1 ni RH.

---

## 1. El generador global no existe cerca de Abel

Escriba

\[
 \nu=(\nu_p)_p,\qquad m(\nu)=\prod_pp^{\nu_p},\qquad
 X(\nu)=\log m(\nu),
\]

y

\[
 \pi_\varepsilon(\nu)
 ={m(\nu)^{-1-\varepsilon}\over\zeta(1+\varepsilon)}.
                                                               \tag{2}
\]

El generador propuesto mueve una unidad desde la torre (q) hasta la
torre (p), con tasa

\[
 r_{q\to p}(\nu)
 =\mathbf1_{\nu_q>0}\sqrt{\log p\log q}
   \left({q\over p}\right)^{(1+\varepsilon)/2}.              \tag{3}
\]

Las tasas satisfacen balance detallado formal. En efecto, si

\[
 \nu'=\nu+e_p-e_q,
\]

entonces

\[
 {\pi_\varepsilon(\nu')\over\pi_\varepsilon(\nu)}
 =\left({q\over p}\right)^{1+\varepsilon},
\]

y por ello

\[
 \pi_\varepsilon(\nu)r_{q\to p}(\nu)
 =\pi_\varepsilon(\nu')r_{p\to q}(\nu').                   \tag{4}
\]

Pero desde el estado (\nu=e_q), la tasa total de salida domina, salvo
una constante dependiente de (q),

\[
 \sum_p {\sqrt{\log p}\over p^{(1+\varepsilon)/2}}.          \tag{5}
\]

La serie sobre primos de (5) diverge cuando
((1+\varepsilon)/2\le1), es decir, para todo
(0<\varepsilon\le1). Éste contiene el régimen completo requerido para
tomar (\varepsilon\downarrow0). Así el generador global no tiene tasa
de salida finita y (1) no está definido.

## 2. Dos obstrucciones algebraicas independientes

Suponga momentáneamente que se truncó el conjunto de primos, de modo que
(S_\varepsilon) es una matriz real autoadjunta en
(L^2(\pi_\varepsilon)). Sea (X) multiplicación por (\log m) y

\[
 C_\varepsilon=i[X,S_\varepsilon].                         \tag{6}
\]

Entonces (C_\varepsilon) es autoadjunto. Para todo vector real (g),

\[
\begin{aligned}
 \langle C_\varepsilon g,g\rangle
 &=i\{\langle XS_\varepsilon g,g\rangle
       -\langle S_\varepsilon Xg,g\rangle\}\\
 &=i\{\langle S_\varepsilon g,Xg\rangle
       -\langle Xg,S_\varepsilon g\rangle\}=0.             \tag{7}
\end{aligned}
\]

En particular, para

\[
 g_n(\nu)=L_{n-1}^{(1)}(X(\nu)),                            \tag{8}
\]

el supuesto término de interacción (I_2) desaparece exactamente. La
norma de (1) contiene solo dos términos positivos y no retiene la
orientación firmada que debía controlar (B_n).

Hay además un núcleo grande. Los intercambios conservan

\[
 \Omega(\nu)=\sum_p\nu_p,
\]

de modo que toda función constante en una capa (\{\Omega=k\}) pertenece
al núcleo de (S_\varepsilon). Si (\mathbf1_k) es la constante de esa
capa,

\[
 \langle\mathbf1_k,C_\varepsilon g\rangle
 =-i\langle S_\varepsilon X\mathbf1_k,g\rangle,             \tag{9}
\]

que no es cero en general. Por tanto

\[
 -S_\varepsilon h=C_\varepsilon g                           \tag{10}
\]

no satisface la condición de Fredholm. La ecuación correcta tendría que
ser

\[
 -S_\varepsilon h=(I-\Pi)C_\varepsilon g,                  \tag{11}
\]

donde (\Pi) proyecta sobre las constantes de cada capa. El (I_3) de la
propuesta original tampoco estaba definido sin esta proyección.

## 3. Generador localizado en torres vecinas

Enumere los primos (p_1<p_2<\cdots), ponga

\[
 d_j=\log {p_{j+1}\over p_j},\qquad a_j=d_j^{-2},           \tag{12}
\]

y permita solamente los movimientos
(p_j\leftrightarrow p_{j+1}). Las tasas son

\[
\begin{aligned}
 r_{j\to j+1}(\nu)
 &=\mathbf1_{\nu_{p_j}>0}\,a_j
   \left({p_j\over p_{j+1}}\right)^{(1+\varepsilon)/2},\\
 r_{j+1\to j}(\nu)
 &=\mathbf1_{\nu_{p_{j+1}}>0}\,a_j
   \left({p_{j+1}\over p_j}\right)^{(1+\varepsilon)/2}.
                                                               \tag{13}
\end{aligned}
\]

Cada estado tiene a lo sumo (2\Omega(\nu)) movimientos distintos; su
tasa total es finita. La misma cuenta de (4) prueba balance detallado.
El factor (d_j^{-2}) es la normalización difusiva natural en la variable
(X=\log m): compensa exactamente el cuadrado del salto entre torres
cercanas.

En cada truncamiento finito de una capa, (S_\varepsilon^{\rm nb}) es
autoadjunto, irreducible y tiene como núcleo solo las constantes. La
ecuación proyectada

\[
 -S_\varepsilon^{\rm nb}h
 =(I-\Pi)C_\varepsilon^{\rm nb}g                            \tag{14}
\]

tiene solución única bajo la normalización (\Pi h=0), y

\[
 \langle h,(I-\Pi)C_\varepsilon^{\rm nb}g\rangle
 =\langle h,-S_\varepsilon^{\rm nb}h\rangle\ge0.           \tag{15}
\]

Así el término resolvente queda reparado, sin suponer una brecha espectral
uniforme al retirar los truncamientos.

## 4. Qué recupera y qué no recupera un twist de fase

Sea (c_{xy}=\pi(x)r(x,y)=c_{yx}) la conductancia de una arista no
orientada y (d_{xy}=X(y)-X(x)). Para

\[
 g_\tau(x)=e^{i\tau X(x)}F(X(x)),\qquad F\ \hbox{real},     \tag{16}
\]

la forma del conmutador es

\[
 \boxed{
 \langle Cg_\tau,g_\tau\rangle
 =2\sum_{\{x,y\}}c_{xy}d_{xy}
   \sin(\tau d_{xy})F(X(x))F(X(y)).}                      \tag{17}
\]

La fase reaparece, pero el producto de Laguerres en (17) cambia de signo
al cruzar sus ceros. Por ello cercanía de torres no implica signo uniforme.
Conectar solamente aristas dentro de un mismo lóbulo haría positivo el
producto, pero separaría precisamente los bordes entre lóbulos donde vive
la cancelación buscada.

La verificación finita `tools/neighbor_prime_resolvent_check.py`, en la
capa (\Omega=1), confirma:

* balance detallado y autoadjunción con errores menores que (3\cdot10^{-15});
* (\langle Cg_n,g_n\rangle=0) para el vector real;
* incompatibilidad no nula de la ecuación de Poisson sin proyectar;
* residuo menor que (3\cdot10^{-12}) en la ecuación proyectada;
* positividad de (15);
* cambio de signo del término de fase: con 48 primos,
  (\varepsilon=1/2) y (\tau=1/5), vale aproximadamente
  (+0.2111) en (n=24), (-0.3859) en (n=32) y
  (-0.7145) en (n=48).

## 5. Sucesor exacto

El fallo de (7) es propio de un certificado escalar. La forma mínima que
puede tener interacción real es un lift de dos componentes. Póngase, por
ejemplo,

\[
 G_n=
 \begin{pmatrix}
 L_{n-1}^{(1)}(X)\\
 L_{n-2}^{(2)}(X)
 \end{pmatrix},                                          \tag{18}
\]

usando que

\[
 {d\over dX}L_{n-1}^{(1)}(X)=-L_{n-2}^{(2)}(X).           \tag{19}
\]

El nuevo blanco es construir una corriente local (J_\varepsilon),
antisimétrica y con (J_\varepsilon\mathbf1=0), sobre ciclos de tres
torres consecutivas, y demostrar una identidad de la forma

\[
 {3\over4}A_n-\delta_n-B_{n,\varepsilon}
 =\left\langle G_n,
 \begin{pmatrix}
 -S_\varepsilon^{\rm nb}&\eta_nJ_\varepsilon\\
 -\eta_nJ_\varepsilon&-S_\varepsilon^{\rm nb}
 \end{pmatrix}G_n\right\rangle
 +\mathcal R_{n,\varepsilon}.                            \tag{20}
\]

Aquí sí aparece el cruzado real

\[
 2\eta_n\left\langle
 L_{n-1}^{(1)}(X),J_\varepsilon L_{n-2}^{(2)}(X)
 \right\rangle,                                         \tag{21}
\]

que puede conservar la orientación de la recurrencia Laguerre. Los ciclos
de longitud tres son necesarios: una cadena de vecinos es un árbol y no
posee una corriente local no trivial que sea simultáneamente
antisimétrica, conservativa y nula sobre constantes.

El paso bloqueante de (20) ya no es invertir un generador global. Es una
identidad Mecke de segundo orden que relacione la corriente de tres torres
con el término lineal real (B_{n,\varepsilon}), seguida de una cota de
Schur para la matriz de (20). Éste es el próximo ataque falsable; (1) queda
retirado.

El script `tools/neighbor_prime_two_component_check.py` construye esta
corriente en la capa finita (\Omega=1). Verifica (J^*=-J),
(J\mathbf1=0) y calcula la constante de Schur exacta

\[
 \eta_{\max}
 =\left\|(-S)^{-1/2}J(-S)^{-1/2}\right\|^{-1}.             \tag{22}
\]

Para 48 primos y (\varepsilon=1/2) obtiene
(\eta_{\max}\simeq0.7194) y una forma de bloques no negativa en todos
los grados ensayados. El cruzado de los grados adyacentes es positivo en
(4\le n\le48) en ese truncamiento. En truncamientos mayores se observan
ambos signos cuando (\varepsilon) todavía está lejos de cero, mientras
los ensayos cercanos al régimen Abel vuelven a ser positivos. Esto es solo
un diagnóstico: al disminuir (\varepsilon), una fracción creciente de
la medida estacionaria queda fuera de todo truncamiento fijo. No se usa
como lema.

## Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 neighbor_prime_resolvent_check.py
python3 neighbor_prime_two_component_check.py
```
