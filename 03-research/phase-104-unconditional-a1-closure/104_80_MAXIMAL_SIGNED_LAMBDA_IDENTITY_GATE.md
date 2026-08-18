# 104_80 — Identidad firmada máxima de Mangoldt y polo no removible

**Resultado.** La cancelación conjunta solicitada entre los pesos reales
\(\Lambda(m)\), todas las potencias primas y el comparador polar posee una
forma cerrada. Para

\[
 P_n(u)=L_{n-1}^{(1)}(u),\qquad
 t={z\over1-z},\qquad s_\varepsilon(z)=1+\varepsilon+t,
\]

\[
 Q_{n,\varepsilon}=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 P_n(\log m),\qquad
 p_n(\varepsilon)=\int_0^\infty e^{-\varepsilon u}P_n(u)\,du,
\]

se tiene, inicialmente en el disco explícito donde las dobles series
usadas abajo convergen absolutamente,

\[
 |z|<r_\varepsilon:={\varepsilon\over1+\varepsilon},
\]

\[
 \boxed{
 \sum_{n\ge1}\{Q_{n,\varepsilon}-p_n(\varepsilon)\}z^{n-1}
 =-{d\over dz}\log\!\left[
  (s_\varepsilon(z)-1)\zeta(s_\varepsilon(z))\right].}       \tag{1}
\]

La inversión \(\Lambda=\mu*\log\) y la fórmula de adición de Laguerre
producen exactamente la misma identidad como convolución firmada. No queda
dentro de esta expansión lineal un término cruzado adicional que pueda
recibir un signo.

La identidad (1) **no prueba** el límite profundo de `104_75`. Si \(\rho\)
es un cero no trivial de multiplicidad \(m_\rho\), entonces el miembro
derecho tiene un polo en

\[
 z_{\rho,\varepsilon}
 ={\rho-1-\varepsilon\over\rho-\varepsilon},              \tag{2}
\]

y

\[
 |z_{\rho,\varepsilon}|<1
 \quad\Longleftrightarrow\quad
 \Re\rho>{1\over2}+\varepsilon.                           \tag{3}
\]

Su parte principal es

\[
 \boxed{
 -{d\over dz}\log\!\left[
  (s_\varepsilon(z)-1)\zeta(s_\varepsilon(z))\right]
 ={m_\rho/z_{\rho,\varepsilon}
       \over1-z/z_{\rho,\varepsilon}}+\text{holomorfa}.} \tag{4}
\]

Por tanto aporta exactamente
\(m_\rho z_{\rho,\varepsilon}^{-n}\) al coeficiente de grado \(n-1\).
Ninguna reordenación absolutamente convergente de la expansión
Möbius--divisor (10)--(13) puede borrar (4): todas representan el mismo
germ meromorfo, y la unicidad de continuación conserva sus polos y
residuos. Una formulación Palm o cumulante queda incluida en esta
conclusión solo cuando, al expandirse, es tal reordenamiento del mismo
germ.

Así, la identidad conjunta existe y es exacta, pero convierte el target en
la afirmación de que no hay polos (2) dentro del disco cuando
\(\varepsilon\downarrow0\). Exigirlo para todo \(\varepsilon>0\) excluye
ceros con \(\Re\rho>1/2\); la simetría funcional
\(\rho\leftrightarrow1-\overline\rho\) excluye entonces también
\(\Re\rho<1/2\). Esa afirmación es precisamente RH. Este
documento cierra el ataque por **identidad algebraica adicional**; no prueba
el límite profundo, A1 ni RH.

---

## 1. Suma simultánea de todos los grados

La generatriz ordinaria de Laguerre da

\[
 \sum_{n\ge1}P_n(u)z^{n-1}
 ={1\over(1-z)^2}\exp\!\left(-{uz\over1-z}\right).
                                                                    \tag{5}
\]

Para justificar el intercambio, ponga \(r=|z|\). Como los coeficientes de
\(P_n(u)=L_{n-1}^{(1)}(u)\) alternan en signo, para \(u\ge0\)

\[
 |P_n(u)|\le L_{n-1}^{(1)}(-u),
\]

y (5) da

\[
 \sum_{n\ge1}|P_n(u)|r^{n-1}
 \le {1\over(1-r)^2}
       \exp\!\left({ur\over1-r}\right).                 \tag{5a}
\]

Si \(r<\varepsilon/(1+\varepsilon)\), entonces
\(\varepsilon-r/(1-r)>0\), y por tanto

\[
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 \sum_{n\ge1}|P_n(\log m)|r^{n-1}
 \le {1\over(1-r)^2}
 \sum_{m\ge2}{\Lambda(m)\over
 m^{1+\varepsilon-r/(1-r)}}<\infty.                    \tag{5b}
\]

La misma cota, integrada contra \(e^{-\varepsilon u}du\), justifica la
serie polar. Tonelli para los módulos y luego Fubini para las series
complejas dan

\[
\begin{aligned}
 \sum_{n\ge1}Q_{n,\varepsilon}z^{n-1}
 &={1\over(1-z)^2}
   \sum_{m\ge2}{\Lambda(m)\over
       m^{1+\varepsilon+z/(1-z)}}\\
 &={1\over(1-z)^2}
   \left(-{\zeta'\over\zeta}\right)(s_\varepsilon(z)).
                                                               \tag{6}
\end{aligned}
\]

Asimismo,

\[
 \sum_{n\ge1}p_n(\varepsilon)z^{n-1}
 ={1\over(1-z)^2}
   \int_0^\infty e^{-(\varepsilon+t)u}\,du
 ={1\over(1-z)^2}{1\over s_\varepsilon(z)-1}.           \tag{7}
\]

Como \(s_\varepsilon'(z)=(1-z)^{-2}\), restar (7) de (6)
prueba (1):

\[
 {1\over(1-z)^2}
 \left\{-{\zeta'\over\zeta}(s)-{1\over s-1}\right\}
 =-{d\over dz}\log\{(s-1)\zeta(s)\}.                   \tag{8}
\]

Multiplicando (1) por \(z\) se obtiene la versión con potencias \(z^n\):

\[
 \sum_{n\ge1}(Q_{n,\varepsilon}-p_n(\varepsilon))z^n
 =-z{d\over dz}\log\{(s_\varepsilon(z)-1)
                         \zeta(s_\varepsilon(z))\}.      \tag{9}
\]

## 2. La involución Möbius produce la misma función

La identidad de convolución de Dirichlet es

\[
 \Lambda(r)=\sum_{d\mid r}\mu(d)\log(r/d).              \tag{10}
\]

En forma combinatoria, si
\(r=\prod_{j=1}^kp_j^{a_j}\), expanda \(\log(r/d)\) en las
marcas \(\log p_j\). Para \(k\ge2\), cada sumando con marca \(j\) se
empareja cambiando la presencia en \(d\) de cualquier primo
\(p_h\ne p_j\); los signos de Möbius son opuestos. Solo sobre una torre
\(r=p^a\) sobrevive \(a-(a-1)=1\) copia de \(\log p\). Esta es una
involución sign-reversing exacta, no una estimación.

La fórmula de adición

\[
 L_{n-1}^{(1)}(x+y)
 =\sum_{j=0}^{n-1}L_j(x)L_{n-1-j}(y)                    \tag{11}
\]

convierte (10), con \(a=1+\varepsilon\), en

\[
 \boxed{
 Q_{n,\varepsilon}=\sum_{j=0}^{n-1}M_j(a)C_{n-1-j}(a),} \tag{12}
\]

donde

\[
 M_j(a)=\sum_{d\ge1}{\mu(d)\over d^a}L_j(\log d),
 \qquad
 C_k(a)=\sum_{m\ge1}{\log m\over m^a}L_k(\log m).       \tag{13}
\]

Todo converge absolutamente para \(a>1\). Sumar (12) en el grado vuelve
a (6). Al incorporar (7), la convolución es exactamente el cociente
logarítmico (1). En particular, la cancelación de fibras multiprimo no
genera una reserva: deja precisamente las torres que forman
\(-\zeta'/\zeta\).

## 3. Lema del polo no removible

Sea \(F_\varepsilon(z)=(s_\varepsilon(z)-1)
\zeta(s_\varepsilon(z))\). Si \(\rho\) es un cero no trivial de orden
\(m_\rho\), entonces localmente

\[
 F_\varepsilon(z)=
 (s_\varepsilon(z)-\rho)^{m_\rho}H(z),\qquad H(z_\rho)\ne0.
\]

Como \(s_\varepsilon'(z_\rho)\ne0\),

\[
 -{F_\varepsilon'(z)\over F_\varepsilon(z)}
 =-{m_\rho\over z-z_{\rho,\varepsilon}}+O(1),           \tag{14}
\]

que es (4). Además,

\[
 |\rho-\varepsilon|^2-|\rho-1-\varepsilon|^2
 =2\Re\rho-1-2\varepsilon.                              \tag{15}
\]

Las ecuaciones (2)--(3) siguen inmediatamente. La multiplicidad
\(m_\rho\) es positiva, mientras el residuo complejo de
\(-F_\varepsilon'/F_\varepsilon\) en \(z_{\rho,\varepsilon}\) es
\(-m_\rho\). Otro cero en el mismo punto suma la misma contribución y no
la resta. El comparador polar ya está contenido en \(F_\varepsilon\) y la
parte Gamma es holomorfa en la imagen de un cero no trivial, de modo que
ninguno cancela (14).

**Corolario 3.1 (maximalidad dentro de los reagrupamientos).** Toda
identidad obtenida de (10)--(13) mediante reordenamientos absolutamente
convergentes coincide con (1) en un entorno de cero. En
\(\mathbb C\setminus\{1\}\), su continuación meromorfa tiene en cada
preimagen (2) de un cero \(\rho\) de \(\zeta\) un polo de residuo
\(-m_\rho\). Estos son todos sus polos allí; los ceros triviales también
aparecen por (2), pero quedan fuera del disco unidad. Por tanto la identidad
no puede implicar la holomorfía del disco sin un input adicional que
excluya los polos no triviales interiores.

La conclusión usa solo unicidad de continuación. No afirma que toda futura
desigualdad aritmética sea imposible: una desigualdad específica de la
ubicación de los primos ordinarios podría, en principio, demostrar que los
polos no existen. Lo que queda descartado es obtener esa conclusión de una
nueva **reescritura exacta** de la misma convolución.

## 4. Relación exacta con el observable profundo

Para la diagonal de `104_75`,
\(\varepsilon_X=e^{-X/100}\), se tiene

\[
 \lambda_{n,\varepsilon_X}
 =A_n+p_n(\varepsilon_X)-Q_{n,\varepsilon_X},
 \qquad
 \sup_{n\le X}|\lambda_{n,\varepsilon_X}-\lambda_n|=o(1).
                                                               \tag{16}
\]

Si existe un cero con \(\Re\rho>1/2\), entonces para \(X\) grande
\(\varepsilon_X<\Re\rho-1/2\), y (3) coloca su polo dentro del disco.
Los polos interiores de módulo mínimo producen, por recurrencia simultánea
de sus fases, un conjunto sindético \(D\) y constantes \(c>0,R>1\) con

\[
 \lambda_n\le-cR^n\qquad(n\in D)                         \tag{17}
\]

desde un índice fijo (`104_56`). Para cualquier
\(K>1/\log R\), (17) cruza \(-e^{\sqrt X}\) en
\(D\cap[K\sqrt X,X]\), cuya masa armónica es una proporción positiva de
\(H_X\). Por (16), el evento aritmético profundo tiene entonces liminf
positivo.

Recíprocamente, probar que dicho evento tiene densidad logarítmica cero
excluye todo polo interior y prueba RH. La identidad (1) no interpone un
lema más débil entre esas dos afirmaciones: muestra que son la misma
obstrucción en coordenadas Euler y meromorfas.

## 5. Decisión

```text
probado:
  identidad conjunta exacta (1)/(9);
  involución Möbius sign-reversing y convolución Laguerre (12);
  localización y residuo exactos de cada cero (2)--(4);
  imposibilidad de borrar el polo mediante otro reagrupamiento
  absolutamente convergente de (10)--(13).

descartado:
  otro reordenamiento absolutamente convergente de (10)--(13)
  (incluidas formas Palm/cumulantes que se reduzcan a él)
  + una nueva identidad algebraica del mismo germ
  => límite profundo.

no descartado:
  una desigualdad analítica nueva, específica de los primos ordinarios,
  que pruebe directamente que no existen los polos interiores.

no probado:
  el límite profundo, A1 o RH.
```

## 6. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 maximal_signed_lambda_identity_check.py
```

El checker usa `Fraction`. Verifica la fórmula de adición (11), la
involución de (10) sobre factorizaciones formales, la equivalencia de
módulo (15) y los coeficientes geométricos de (4). Es una verificación de
las identidades algebraicas; la prueba analítica está en el texto.
