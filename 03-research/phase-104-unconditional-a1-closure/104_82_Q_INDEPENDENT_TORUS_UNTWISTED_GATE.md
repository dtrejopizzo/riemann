# 104_82 — Independencia de las longitudes primas y gate del punto *untwisted*

**Resultado.** La independencia lineal sobre \(\mathbf Q\) de
\(\{\log p\}\), la inyectividad de la norma y la factorización única
diagonalizan exactamente las correlaciones después de introducir fases
primas independientes. No controlan, sin embargo, el valor sin twist que
aparece en el observable profundo de `104_75`.

Hay dos obstrucciones exactas.

1. El flujo de Kronecker identifica una media de Haar, mientras el punto
   aritmético es \(\theta_p=0\) para todo \(p\). La evaluación en ese punto
   no es un funcional uniformemente acotado por las normas torales. En
   dimensión \(J\), un polinomio soportado en productos *squarefree* tiene
   media cero, norma \(L^2\) de orden \(2^{J/2}\), y valor untwisted de
   orden \(2^J\).
2. Más decisivamente, el falsificador Euler off-line de `104_78` puede
   deformarse de modo que **todas** sus longitudes primas sean
   \(\mathbf Q\)-linealmente independientes. El producto de Euler sigue
   siendo positivo, el monoide sigue teniendo factorización única y la
   norma pasa a ser inyectiva. La deformación es un factor holomorfo y no
   nulo en \(\Re s>0\), por lo que no cancela los ceros exteriores y la
   densidad profunda continúa siendo \(1/4\).

Por tanto queda cerrado el ataque estrecho

```text
independencia Q-lineal de log p / inyectividad de la norma
+ ortogonalidad en el toro o involución prima--semiprima
=> límite profundo para el punto untwisted.
```

Esto no descarta una desigualdad que use, además, la colocación cuantitativa
específica de los primos ordinarios, el PNT continuo y el factor Gamma. No
prueba el límite profundo, A1 ni RH.

---

## 1. Lo que la independencia sí prueba

Fije un conjunto finito de primos \({\cal P}\), un corte \(K\), y escriba

\[
 c_{p,k}^{(n,\varepsilon)}
 ={\log p\over p^{k(1+\varepsilon)}}
 L_{n-1}^{(1)}(k\log p).
\]

El lift toral truncado del bloque de Mangoldt es

\[
 Q_{n,\varepsilon}^{{\cal P},K}(\theta)
 =\sum_{p\in{\cal P}}\sum_{1\le k\le K}
 c_{p,k}^{(n,\varepsilon)}e^{ik\theta_p}.               \tag{1}
\]

En \(\theta=0\), (1) es exactamente la truncación de
\(Q_{n,\varepsilon}\). Por factorización única,

\[
 \sum_{p\in{\cal P}}m_p\log p=0,
 \qquad m_p\in\mathbf Z,
 \quad\Longrightarrow\quad m_p=0\ \ (p\in{\cal P}).   \tag{2}
\]

El flujo continuo

\[
 t\longmapsto (t\log p)_{p\in{\cal P}}\pmod {2\pi}
\]

es por ello equidistribuido en el toro. En particular,

\[
 \lim_{T\to\infty}{1\over2T}\int_{-T}^{T}
 Q_{n,\varepsilon}^{{\cal P},K}
       ((t\log p)_p)\,dt=0,                              \tag{3}
\]

y Parseval da la identidad diagonal

\[
 \lim_{T\to\infty}{1\over2T}\int_{-T}^{T}
 \left|Q_{n,\varepsilon}^{{\cal P},K}
       ((t\log p)_p)\right|^2dt
 =\sum_{p\in{\cal P}}\sum_{k\le K}|c_{p,k}|^2.         \tag{4}
\]

La misma prueba vale para cualquier polinomio divisor: caracteres
distintos corresponden a vectores de exponentes distintos. Ésta es toda la
ganancia automática de la factorización única: ortogonalidad después de
promediar los twists.

## 2. La evaluación untwisted no está controlada

La obstrucción ya aparece dentro de una sola torre prima. Para

\[
 S_K(\theta)=\sum_{k=1}^{K}e^{ik\theta},
\]

se tiene exactamente

\[
 \int_{\mathbb T}S_K=0,\qquad
 \|S_K\|_2^2=K,\qquad S_K(0)=K.                         \tag{4a}
\]

Así ni siquiera la ortogonalidad de las distintas potencias de un primo
acota su suma en la fase alineada.

Sean \(\theta_1,\ldots,\theta_J\) las fases de \(J\) primos y considere

\[
 D_J(\theta)=\prod_{j=1}^{J}(1+e^{i\theta_j})-1
 =\sum_{\varnothing\ne S\subseteq\{1,\ldots,J\}}
   e^{i\sum_{j\in S}\theta_j}.                         \tag{5}
\]

Cada carácter de (5) es la marca de un producto *squarefree* distinto;
no hay colisiones precisamente por factorización única. Sin embargo,

\[
 \int_{\mathbb T^J}D_J\,d\theta=0,\qquad
 \|D_J\|_2^2=2^J-1,\qquad
 D_J(0)=2^J-1.                                          \tag{6}
\]

Para el polinomio real \(F_J=\Re D_J\),

\[
 \int F_J=0,\qquad
 \|F_J\|_2^2={2^J-1\over2},\qquad
 F_J(0)=2^J-1.                                          \tag{7}
\]

Así la norma de la evaluación en el punto untwisted crece al menos como
\(2^{J/2}\). Tomando \(J\asymp\sqrt X\), el valor puntual ya alcanza la
escala \(e^{\sqrt X}\) del gate profundo aunque la media de Haar sea cero.
No hay una constante uniforme que transfiera (3), (4), o cualquier
estimación \(L^2\) obtenida por independencia, al punto \(0\).

La obstrucción también decide la propuesta de una involución
prima--semiprima. El carácter de un primo es \(e_p\), mientras el de
\(qr\) es \(e_q+e_r\). Una involución que preserve la fase requeriría

\[
 e_p=e_q+e_r,                                            \tag{8}
\]

o, en la coordenada de longitudes,

\[
 \log p=\log q+\log r.                                  \tag{9}
\]

Las ecuaciones (8)--(9) son imposibles entre primos. Por tanto la
independencia no crea la cancelación: impide justamente un emparejamiento
exacto entre los dos tipos de fibra. En \(\theta=0\), en cambio, todos los
caracteres valen \(1\), y el signo depende de la suma numérica completa de
los coeficientes, sobre la cual (2) no contiene información.

## 3. Falsificador no reticular con longitudes independientes

Parta del monoide de `104_78`. Tiene \(\pi_d\ge0\) primos formales de
grado \(d\), longitud base

\[
 a_i=d_i h,\qquad h=\log6,
\]

y función zeta

\[
 Z_0(s)={(1-3\,6^{-s})(1-2\,6^{-s})
          \over(1-6^{-s})(1-6^{1-s})}.                  \tag{10}
\]

Enumere los primos formales por \(i\ge1\), sea \(q_i\) el \(i\)-ésimo
primo racional, y defina

\[
 \delta_i=2^{-2^{i+10}}\sqrt{q_i},\qquad
 \ell_i=a_i+\delta_i.                                  \tag{11}
\]

La sucesión \((\ell_i)\) es \(\mathbf Q\)-linealmente independiente.
En efecto, una relación finita daría

\[
 \left(\sum_i r_id_i\right)\log6
 +\sum_i r_i2^{-2^{i+10}}\sqrt{q_i}=0,
 \qquad r_i\in\mathbf Q.                               \tag{12}
\]

El segundo término es algebraico. Si el primer coeficiente no fuera cero,
(12) haría algebraico a \(\log6\), contradiciendo
Lindemann--Weierstrass. Si fuera cero, la independencia sobre \(\mathbf Q\)
de las raíces cuadradas de primos distintos fuerza \(r_i=0\) para todo
\(i\).

Construya ahora el monoide abeliano libre sobre esos mismos generadores,
pero con norma \(|P_i|=e^{\ell_i}\). Tiene factorización única y, por
(12), la aplicación norma es inyectiva. Sus pesos de Mangoldt son

\[
 \widetilde\Lambda(P_i^k)=\ell_i>0.                    \tag{13}
\]

Para \(\Re s>1\), su producto de Euler es

\[
 \widetilde Z(s)=\prod_{i\ge1}(1-e^{-s\ell_i})^{-1}.
                                                               \tag{14}
\]

La convergencia es absoluta: como \(\ell_i\ge a_i\) y
\(\pi_d\ll6^d/d\), para \(\sigma>1\)

\[
 \sum_i e^{-\sigma\ell_i}
 \le\sum_{d\ge1}\pi_d6^{-\sigma d}<\infty.             \tag{14a}
\]

## 4. La deformación no mueve ni cancela el cero exterior

En \(\Re s>1\), (14) se factoriza exactamente como

\[
 \widetilde Z(s)=Z_0(s)G(s),
\qquad
 G(s)=\prod_{i\ge1}{1-e^{-sa_i}\over1-e^{-s\ell_i}}.   \tag{15}
\]

El factor \(G\) se prolonga holomórficamente y sin ceros a todo
\(\Re s>0\). Para verlo, en cualquier compacto de ese semiplano,

\[
 \left|{\partial\over\partial x}
       \log(1-e^{-sx})\right|
 =\left|{s\over e^{sx}-1}\right|
 \le C_K e^{-\sigma_Kx}.                               \tag{16}
\]

Por Bertrand, \(q_i<2^i\), y de (11) se sigue
\(\sum_i\delta_i<\infty\). Integrar (16) entre \(a_i\) y \(\ell_i\)
muestra que

\[
 \sum_i\{\log(1-e^{-sa_i})-\log(1-e^{-s\ell_i})\}    \tag{17}
\]

converge uniformemente en compactos de \(\Re s>0\). Su exponencial es
precisamente \(G\), de modo que es holomorfo y nunca se anula allí.

La continuación meromorfa definida por (15) conserva por tanto todos los
ceros y polos de \(Z_0\) en \(\Re s>0\). En particular conserva el cero

\[
 \beta_+={\log3\over\log6}>{1\over2}.                  \tag{18}
\]

Con el mapa de `104_80`, ese cero produce

\[
 z_{+,\varepsilon}
 ={\beta_+-1-\varepsilon\over\beta_+-\varepsilon},
 \qquad
 |z_{+,\varepsilon}|^{-1}\longrightarrow
 R={\log3\over\log2}>1.                               \tag{19}
\]

El sumando \(-\partial_z\log G(s_\varepsilon(z))\) es holomorfo en el
disco unidad. Fije \(r\) entre \(|z_{+,0}|\) y el módulo de la siguiente
singularidad de \(Z_0\), con \(r<1\). Para \(\varepsilon\) pequeño es
uniformemente holomorfo en \(|z|\le r\), y Cauchy acota sus coeficientes
por \(O(r^{-n})\), donde \(r^{-1}<R\). No puede cancelar el término
dominante de (19).

Más formalmente, si \(\Xi^0_\varepsilon\) es el completamiento regulado
de `104_78`, defina

\[
 \widetilde\Xi_\varepsilon(s)
 =\Xi^0_\varepsilon(s)G(s+\varepsilon).                 \tag{19a}
\]

Éste es exactamente el cambio que resulta de sustituir
\(Z_0(s+\varepsilon)\) por
\(\widetilde Z(s+\varepsilon)=Z_0(s+\varepsilon)G(s+\varepsilon)\)
en el canal Euler, conservando los demás bordes. Definimos
\(\widetilde\lambda_{n,\varepsilon}\) por la misma derivada de Li de
`104_78`, ecuación (17), aplicada a (19a).

En consecuencia, en la diagonal \(\varepsilon_X=e^{-X/100}\), los
coeficientes de Li del modelo deformado satisfacen

\[
 \widetilde\lambda_{n,\varepsilon_X}
 =-z_{+,\varepsilon_X}^{-n}+O(R_1^n),
 \qquad 1<R_1<R,\quad 1\le n\le X.                    \tag{20}
\]

Para los grados pares, (20) es \(-(1+o(1))R^n\). El mismo cálculo armónico
de `104_78`, \S4, da

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf1_{\{\widetilde\lambda_{n,\varepsilon_X}
          +\log(n+1)\le-e^{\sqrt X}\}}
 \longrightarrow {1\over4}.}                           \tag{21}
\]

Así el resultado off-line de `104_81` sobrevive después de eliminar las
colisiones reticulares de normas y de imponer independencia
\(\mathbf Q\)-lineal completa.

La deformación sumable no elimina los polos verticales heredados de
\(Z_0\) sobre \(\Re s=1\). Por eso este modelo no satisface el PNT
continuo y tampoco conserva el completamiento Gamma estándar de Riemann.
Es un falsificador exacto de la **independencia como input suficiente**, no
de un futuro teorema que use simultáneamente esas estructuras adicionales.

## 5. Alcance exacto

```text
probado:
  independencia Q-lineal => equidistribución y Parseval torales;
  la evaluación untwisted no es uniformemente controlable por esas medias;
  no existe una involución exacta prima--semiprima que preserve fase;
  existe un Euler positivo, de factorización única y norma inyectiva,
  con longitudes primas Q-independientes y densidad profunda 1/4.

descartado:
  independencia / inyectividad / factorización única
  + promedio toral o apareamiento exacto de fibras
  => límite profundo.

no descartado:
  una desigualdad que use conjuntamente PNT continuo, Gamma y la
  colocación cuantitativa exacta de los primos ordinarios.

no probado:
  el límite profundo para Lambda ordinaria, A1 o RH.
```
