# 104_24 — Canales directos y gate Stein--Mecke firmado

**Rol.** Expandir sin diferencias innecesarias el cociclo cúbico de
`104_22` y ejecutar el sucesor Stein--Mecke de `104_21`. La expansión de
cuatro canales es exacta y converge al margen cúbico directo
\(3\lambda_n-A_n\). Stein conserva todos los otros primos, pero su
generador completado es firmado antes del primer átomo aritmético. Así
muere la prueba por positividad del generador; no muere la posible
desigualdad especial no local para Laguerre.

Este documento no prueba A1 ni RH.

## 1. Teorema exacto de cuatro canales

Sea

\[
 d_u:=J_u*J_u*J_u\ge0,
 \qquad s_0=1+\varepsilon,\qquad u=c\varepsilon,\quad 0<c<1. \tag{1}
\]

Para el canal Gamma usemos dos copias de la medida positiva

\[
 d\nu_{\varepsilon,u}(v)
 ={\pi^{u/2}\over\Gamma(u/2)}
 v^{(1+\varepsilon-u)/2}(1-v)^{u/2-1}\,dv.        \tag{2}
\]

Definamos

\[
\begin{aligned}
 T_{k,\delta}:={}&
 \sum_{m\ge1}{d_u(m)\over m^{s_0}}
 \int_0^1\!\int_0^1
 L_k^{(1)}\!\left(\log m-\tfrac12\log(vw)\right)
 d\nu(v)d\nu(w),                                  \tag{3}\\
 T_{k,j}:={}&
 \sum_{m\ge1}{d_u(m)\over m^{s_0}}
 \int_0^1\!\int_0^1\!\int_0^\infty
 L_k^{(1)}\!\left(\log m+y-\tfrac12\log(vw)\right)
 {y^j\over j!}e^{-\varepsilon y}\,dy\,d\nu(v)d\nu(w),
 \quad j=0,1,2.                                    \tag{4}
\end{aligned}
\]

Aquí y abajo \(d\nu=d\nu_{\varepsilon,u}\). Todas las sumas e integrales
convergen absolutamente para \(u<\varepsilon\).

**Teorema 1.1.** Si

\[
 \mathcal S_u^{[3]}(s)=H_u(s)^3K_u(s)^2,
 \qquad s_\varepsilon(z)=s_0+{z\over1-z},          \tag{5}
\]

entonces

\[
 \boxed{
 [z^k]{\mathcal S_u^{[3]}(s_\varepsilon(z))\over(1-z)^2}
 =T_{k,\delta}-3uT_{k,0}+3u^2T_{k,1}-u^3T_{k,2}.} \tag{6}
\]

Por tanto

\[
 \boxed{
 h_{k,\varepsilon,c}^{[3]}
 ={T_{k,\delta}-3uT_{k,0}+3u^2T_{k,1}-u^3T_{k,2}-(k+1)
   \over u}}                                       \tag{7}
\]

y

\[
 h_{k,\varepsilon,c}^{[3]}\longrightarrow
 -(3\lambda_{k+1}-A_{k+1}).                       \tag{8}
\]

**Demostración.** Se usan

\[
 {e^{-xz/(1-z)}\over(1-z)^2}
 =\sum_{k\ge0}L_k^{(1)}(x)z^k                    \tag{9}
\]

y, para \(j\ge0\),

\[
 {1\over(\varepsilon+z/(1-z))^{j+1}}
 =\int_0^\infty {y^j\over j!}e^{-\varepsilon y}
 e^{-yz/(1-z)}\,dy.                               \tag{10}
\]

La expansión

\[
 \left(1-{u\over s-1}\right)^3
 =1-{3u\over s-1}+{3u^2\over(s-1)^2}
       -{u^3\over(s-1)^3}                         \tag{11}
\]

produce (6). El término sustraído en (7) es \(k+1\), no uno, porque
\([z^k](1-z)^{-2}=k+1\). Finalmente (8) es (12) de `104_23` con \(r=3\).
\(\square\)

## 2. Ley global y medida de Lévy completada

Normalicemos la parte aritmética mediante

\[
 \mathbb P(N=m)
 ={d_u(m)m^{-s_0}\over A_u(s_0)^3},
 \qquad X=\log N.                                  \tag{12}
\]

Es compound-Poisson con medida

\[
 \nu_A^{[3]}
 =3\sum_p\sum_{j\ge1}{R_p^j-r_p^j\over j}
 \delta_{j\log p},
 \quad r_p=p^{-1-\varepsilon},\quad
 R_p=p^{-1-(\varepsilon-u)}.                      \tag{13}
\]

Una copia Gamma y una copia polar normalizadas tienen respectivamente

\[
\begin{aligned}
 \nu_K(y)\,dy
 &={e^{-(3+\varepsilon-u)y}-e^{-(3+\varepsilon)y}
    \over y(1-e^{-2y})}\,dy,\\
 \nu_P(y)\,dy
 &={e^{-(\varepsilon-u)y}-e^{-\varepsilon y}\over y}\,dy.
                                                               \tag{14}
\end{aligned}
\]

El exponente de Lévy del cociclo cúbico normalizado tiene el kernel firmado

\[
 \boxed{\nu_3=\nu_A^{[3]}+2\nu_K-3\nu_P.}         \tag{15}
\]

## 3. Identidad Stein--Mecke sin perder los otros primos

Definamos \(\mu_3\) por su transformada de Laplace

\[
 \mathcal L\mu_3(t)
 ={\mathcal S_u^{[3]}(s_0+t)\over
   \mathcal S_u^{[3]}(s_0)}.                       \tag{15a}
\]

Para justificar la identidad siguiente se trunca (13) y también
\(\nu_K\) a \(y\ge\delta\), se deriva la transformada truncada y se pasa
primero en la altura aritmética y luego \(\delta\downarrow0\). El paso está
dominado porque, para cada grado fijo \(k\),

\[
 \int_0^\infty y(1+y^k)|\nu_3|(dy)<\infty.        \tag{15b}
\]

La singularidad \(\nu_K(y)\asymp u/(2y)\) en cero tiene actividad infinita,
pero el factor \(y\) de (15b) la hace integrable. Así, para tests
polinomiales, vale

\[
 \boxed{
 \int x\varphi(x)\,d\mu_3(x)
 =\int_0^\infty y\int\varphi(x+y)\,d\mu_3(x)\,\nu_3(dy).} \tag{16}
\]

Esta identidad conserva dentro de \(\mu_3\) todos los primos distintos del
salto seleccionado. Para

\[
 a_k=\int L_k^{(1)}(x)\,d\mu_3(x),                \tag{17}
\]

la recurrencia de Laguerre produce

\[
\boxed{
 (2k+2)a_k-(k+1)a_{k+1}-(k+1)a_{k-1}
 =\int y\int L_k^{(1)}(x+y)\,d\mu_3(x)\,\nu_3(dy).} \tag{18}
\]

Se toma \(a_{-1}=0\). La ecuación (18) es una recurrencia global exacta,
pero no tiene signo porque \(\nu_3\) no es positiva.

## 4. Testigo exacto antes del primer primo

La falta de signo ocurre en la aritmética real, no en un falsificador
abstracto. Tómese

\[
 \varepsilon=2,\qquad u=1,\qquad c={1\over2},\qquad
 y_0={1\over2}\log2.                              \tag{19}
\]

Como \(0<y_0<\log2\), la medida \(\nu_A^{[3]}\) no tiene soporte en un
entorno de \(y_0\). Evaluando la parte continua de (15),

\[
 \boxed{
 (2\nu_K-3\nu_P)(y_0)
 ={\frac52-2\sqrt2\over y_0}<0.}                  \tag{20}
\]

La desigualdad es exacta: \(2\sqrt2>5/2\) porque
\(8>25/4\). Por continuidad, \(\nu_3\) es estrictamente negativa en un
intervalo abierto contenido en \((0,\log2)\).

Para \(\varepsilon>0\) fijo, al tomar primero \(u\downarrow0\),

\[
 {\nu_3\over u}\longrightarrow
 \kappa_\varepsilon(dy),                          \tag{21}
\]

donde

\[
\boxed{
 \kappa_\varepsilon(dy)
 =3e^{-(1+\varepsilon)y}\,d\psi(e^y)
 -3e^{-\varepsilon y}\,dy
 +{2e^{-(3+\varepsilon)y}\over1-e^{-2y}}\,dy.}   \tag{22}
\]

Sobre el camino diagonal \(u=c\varepsilon\), \(\varepsilon\downarrow0\),
la misma convergencia es local/vaga hacia \(\kappa_0\). La densidad continua
de ese kernel local en \(y_0\) vale

\[
 {2e^{-3y_0}\over1-e^{-2y_0}}-3=\sqrt2-3<0.       \tag{23}
\]

Por tanto el defecto de positividad persiste exactamente en el régimen que
extrae \(3\lambda_n-A_n\). La notación \(\kappa_0\) no designa una medida
de variación total finita en toda la semirrecta: toda recomposición global
con Laguerres se entiende como el límite Abel emparejado
\(\varepsilon\downarrow0\), no como una integral ordinaria contra
\(\kappa_0\).

## 5. Alcance del stop-gate

La medida (22) es de forma transparente

\[
 \text{primos}-\text{polo}+\text{Gamma}.
\]

Integrar \(\kappa_\varepsilon\) contra la respuesta Laguerre de (18) y luego
tomar el límite Abel recompone
\(3\lambda_n-A_n\); integrar por partes el primer término contra
\(d\psi(e^y)\) vuelve a \(\psi(e^y)-e^y\), es decir, a la correlación
ponderada de A1. Stein--Mecke no agrega por sí sola un input aritmético
nuevo.

Queda cerrado únicamente este mecanismo:

> positividad de la medida de Lévy completada + orden de saltos
> \(\Longrightarrow h_k\le0\).

El testigo (20) hace falsa su premisa. No refuta la desigualdad especial
\(h_{k,\varepsilon,c}^{[3]}\le0\): una cancelación no local propia de los
Laguerres y de las masas reales \(\Lambda(p^j)\) todavía podría probarla.

## Estado

- **Probado:** cuatro canales directos, Stein--Mecke global, recurrencia
  Laguerre y testigo exacto de signo.
- **Descartado:** cerrar el margen cúbico por positividad/orden del
  generador completado.
- **Abierto dentro de este mecanismo:** una desigualdad firmada no local para
  (18), o el margen real más débil de `104_23`.
