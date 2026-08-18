# 104_40 — Resolvente variacional Euler canónico y gate de módulo crítico

**Estado.** Se atacó el rayo fijo \(g_n\), no la norma del operador de
bandera, con la factorización prima--polo canónica de 104_36. Para toda
regularización segura \(a>2\), el funcional simple-prime es un promedio
espectral firmado de

\[
 M(s)={1\over s-1}-\sum_p{\log p\over p^s}.
\]

Se permitió el resolvente positivo más general que conmuta con las
traslaciones, es decir, un multiplicador de Fourier positivo arbitrario.
La optimización variacional puede hacerse exactamente. Su mejor cota
inferior reemplaza \(\Re M\) por \(-|M|\). Al acercarse a \(a=1\), esa
cota diverge como \(-\log(1/(a-1))\) por cualquier cero crítico no
resonante, aunque el momento prima--polo renormalizado tenga límite finito.
Los ceros off-line producen antes un cruce de polo y el residuo exponencial
de 104_36.

Por tanto queda descartada toda prueba del margen proporcional mediante un
resolvente **positivo, cuadrático y translation-invariant** aplicado al
vector de discrepancia Euler. Esto es más amplio que usar la norma sin
peso de 104_36. No se descarta un resolvente no conmutativo adaptado al
grado, ni una identidad firmada que conserve la fase de \(M\). Este
documento no prueba A1 ni RH.

## 1. Prerregistro y falsificador

El blanco sigue siendo

\[
 \lambda_n\ge {501\over2002}A_n,
 \qquad n\ge150,                                      \tag{1}
\]

o, después de 104_32, la cota inferior correspondiente para
\(B_{n}^{(p+\mathrm{pole})}\), dejando la corrección
\(P_{n-1}^{(\ge2)}(1)\) explícita.

El único ansatz de este ataque es el siguiente: partir de

\[
 B_{n,a}^{(p+\mathrm{pole})}=\langle V_{n,a},g_n\rangle,
                                                               \tag{2}
\]

con todos los primos simples y el polo ya acoplados dentro de \(V_{n,a}\),
e insertar entre ambos factores un operador positivo \(R_a\) que conmute
con el semigrupo de traslaciones. No se toma valor absoluto primo a primo.

El falsificador obligatorio es

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5}.             \tag{3}
\]

Tiene \(\Re\rho=4/5\). Al bajar \(a\), el polo de la transformada de
Laplace cruza la frontera de Hardy en \(a=2\Re\rho=8/5\), y en \(a=1\)
queda en \(\Re z=3/10>0\). Para \(n=152\), su multiplicador residual es

\[
 1-\left(1-{1\over\rho}\right)^{152}=1-2^{-152}>0.           \tag{4}
\]

Así el ansatz no certifica al divisor off-line: la deformación necesaria
encuentra un polo y debe sumar su residuo. El checker reproduce (3)--(4)
con racionales gaussianos.

## 2. Identidad escalar exacta en el semiplano Euler

Usamos la normalización de 104_36:

\[
 g_n(x)=e^{-x/2}L_{n-1}^{(1)}(x),
 \qquad
 \widehat g_n(t)
 =1-\left({-1/2+it\over1/2+it}\right)^n.                    \tag{5}
\]

Sea

\[
 Q(s)=\sum_p{\log p\over p^s},
 \qquad M(s)={1\over s-1}-Q(s).                              \tag{6}
\]

Para \(a>2\), las integraciones de Euler convergen absolutamente y
104_36, (13), da

\[
 \widehat V_{n,a}(t)
 =a\widehat g_n(t)M\!\left(a(1/2+it)\right).                 \tag{7}
\]

Plancherel conserva la fase completa de la diferencia prima--polo:

\[
 \boxed{
 B_{n,a}^{(p+\mathrm{pole})}
 ={a\over2\pi}\int_{\mathbb R}|\widehat g_n(t)|^2
 \Re M\!\left(a(1/2+it)\right)\,dt.}                         \tag{8}
\]

La convergencia de (8) es absoluta para \(a>2\). En particular, (8) ya
es una estimación sobre el **vector fijo** \(g_n\); no aparece el supremo
espectral de 104_30.

## 3. Optimización sobre todos los resolventes positivos conmutativos

Un operador positivo translation-invariant es, en la representación de
Fourier, multiplicación por una función medible \(r(t)>0\). La desigualdad
de Young puntual, aplicada a \(z=aM(a(1/2+it))\), es

\[
 2\Re z\ge-r|z|^2-r^{-1}.                                  \tag{9}
\]

Por (8),

\[
 B_{n,a}^{(p+\mathrm{pole})}\ge-\mathcal C_{n,a}[r],         \tag{10}
\]

\[
 \mathcal C_{n,a}[r]
 ={1\over4\pi}\int_{\mathbb R}|\widehat g_n(t)|^2
 \left\{a^2r(t)|M(a(1/2+it))|^2+r(t)^{-1}\right\}\,dt.       \tag{11}
\]

No se perdió ninguna interacción antes de (11): el módulo contiene la
diferencia completa \(1/(s-1)-Q(s)\), y al cuadrarlo aparecen todos los
cruces primo--primo y primo--polo.

La variación en \(r\) es puntual y exacta. Para \(M\ne0\), el mínimo se
alcanza en \(r=(a|M|)^{-1}\); en un cero se obtiene por límite. Por tanto

\[
 \boxed{
 \inf_{r>0}\mathcal C_{n,a}[r]
 =\mathcal J_{n,a}
 :={a\over2\pi}\int_{\mathbb R}|\widehat g_n(t)|^2
 |M(a(1/2+it))|\,dt.}                                      \tag{12}
\]

La ecuación (12) es un teorema de optimalidad para toda esta clase de
resolventes. Un multiplicador positivo más elaborado no recupera la fase:
su mejor resultado es exactamente

\[
 B_{n,a}^{(p+\mathrm{pole})}\ge-\mathcal J_{n,a}.             \tag{13}
\]

## 4. El mejor costo diverge ya por los ceros críticos

La continuación meromorfa usada en 104_36 es

\[
 Q(s)=\sum_{k\ge1}\mu(k)\left(-{\zeta'\over\zeta}(ks)\right).
                                                               \tag{14}
\]

Si \(\rho=1/2+i\gamma\) es un cero crítico de multiplicidad \(m_\rho\),
entonces, en un disco sin otras singularidades,

\[
 M(s)={m_\rho\over s-\rho}+H_\rho(s),                        \tag{15}
\]

con \(H_\rho\) holomorfa. Sobre \(s=a(1/2+it)\), poniendo

\[
 \delta={a-1\over2},\qquad t_\rho(a)={\gamma\over a},        \tag{16}
\]

se tiene

\[
 s-\rho=\delta+ia\{t-t_\rho(a)\}.                           \tag{17}
\]

Para cada \(n\) hay un cero crítico con
\(\widehat g_n(\gamma)\ne0\). En efecto, por el teorema incondicional de
Hardy hay infinitos ceros distintos en la línea crítica, mientras que

\[
 \widehat g_n(t)=0
 \iff
 \left({-1/2+it\over1/2+it}\right)^n=1                     \tag{18}
\]

admite solo un conjunto finito de ordenadas reales.

Fijemos uno de esos ceros. Por continuidad de \(\widehat g_n\), y haciendo
el intervalo suficientemente pequeño en (15), existen constantes
\(c_{n,\rho}>0\), \(r_\rho>0\) y \(a_0>1\) tales que

\[
 \mathcal J_{n,a}
 \ge c_{n,\rho}
 \int_{-r_\rho}^{r_\rho}
 {du\over\sqrt{\delta^2+a^2u^2}}
 \ge c_{n,\rho}\log{1\over a-1}                    \tag{19}
\]

para \(1<a<a_0\), evitando los valores aislados en que la recta pase por
otra singularidad. En particular,

\[
 \boxed{\mathcal J_{n,a}\longrightarrow+\infty
 \quad(a\downarrow1).}                                      \tag{20}
\]

Este resultado es incondicional: usa solamente la existencia de infinitos
ceros críticos, no RH. La divergencia es logarítmica, frente a la
divergencia \((a-1)^{-1}\) de la norma cuadrada de 104_36; optimizar el
resolvente mejora el exponente, pero no deja un límite finito.

Por contraste, la combinación Abel prima--polo escalar tiene el límite
finito definido en 104_32. Luego la divergencia de (20) es creada
exactamente al reemplazar la fase de \(M\) por su módulo. La corrección de
potencias superiores, acotada por \(14n+1\), no puede cancelar una
divergencia en \(a\) para \(n\) fijo, y \(A_n\) tampoco depende de \(a\).

## 5. Qué ocurre con un cero off-line

Si \(\Re\rho>1/2\), el polo de (15) cruza la recta
\(\Re s=a/2\) en \(a=2\Re\rho\). La identidad Euler (8), inicialmente
probada para \(a>2\), no puede deformarse hasta \(a=1\) sin recoger ese
residuo. En la coordenada de Laplace de 104_36, el polo está en

\[
 z_{\rho,a}={\rho\over a}-{1\over2},                           \tag{21}
\]

y su multiplicador es

\[
 m_\rho\left[1-\left(1-{a\over\rho}\right)^n\right].         \tag{22}
\]

Las ecuaciones (21)--(22) son precisamente el dato que hace fallar el
falsificador (3). Por tanto el stop-gate tiene las dos ramas correctas:

* un cero off-line impide la deformación sin residuos;
* aun en ausencia de ese cruce, los ceros críticos hacen divergir la mejor
  cota cuadrática por módulo.

## 6. Decisión

Queda probado el siguiente no-go, con cuantificadores completos:

> **Teorema (gate variacional conmutativo).** Entre todas las
> factorizaciones de Young obtenidas insertando un operador positivo que
> conmuta con las traslaciones en la identidad prima--polo (2), la cota
> inferior óptima es (13). Su costo diverge al retirar el regulador por
> (20). Si se intenta deformar atravesando un cero off-line, aparece antes
> el residuo (22). Por tanto ninguna prueba de (1) puede salir de esta
> clase de resolventes.

El resultado no descarta:

1. un resolvente no translation-invariant que use de manera esencial el
   grado \(n\) y conserve una fase firmada;
2. una identidad aritmética que cancele los residuos con otro canal antes
   de aplicar una forma positiva;
3. el criterio de Schur adyacente \(\mathcal T_n\ge0\) de 104_34.

Sí descarta reemplazar la norma de 104_36 por un peso espectral positivo o
por un precondicionador de Fourier: después de optimizar todos ellos, la
misma pérdida de fase reaparece como \(|M|\).

## 7. Verificación reproducible

Ejecutar

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 canonical_euler_resolvent_gate_check.py

El programa usa Fraction para (3)--(4), la identidad de minimización de
Young en una malla racional y un polo crítico racional modelo
\(\rho=1/2+i\), para el cual
\(1-1/\rho=(3+4i)/5\) no es raíz de unidad. La tabla de
\(2\operatorname{arsinh}(1/\delta)\) solo ilustra la ley logarítmica de
(19); la decisión matemática es la prueba anterior, no la tabla decimal.

