# 104_116 — Identidad Mecke de intercambio triangular y gate fuente--circulación

## Resultado

La identidad Mecke pedida para el pivote de `104_115` existe y se prueba
en forma cerrada. Sea (s=1+\varepsilon>1), sea

\[
 \mathbb P_s(N=n)={n^{-s}\over\zeta(s)},
 \qquad N=\prod_pp^{A_p},                                  \tag{1}
\]

y sea (\omega=(\omega_{pq})) una matriz antisimétrica de soporte
finito. Defina

\[
 (J_\omega G)(N)
 =\sum_{p\ne q}\omega_{pq}
   \left({q\over p}\right)^{s/2}
   \mathbf1_{A_q\ge1}\,G(Np/q).                          \tag{2}
\]

Entonces

\[
 \boxed{
 \langle F,J_\omega G\rangle_s
 =\sum_{p\ne q}{\omega_{pq}\over(pq)^{s/2}}
   \mathbb E_s\{\overline{F(qN)}G(pN)\}.}                \tag{3}
\]

El operador es antiautoadjunto. Además (J_\omega\mathbf1=0) si y solo
si, con (u_p=p^{-s/2}),

\[
 \omega u=0.                                               \tag{4}
\]

En una terna (a<b<c), (4) fija, salvo un escalar (\kappa), la corriente
local

\[
 \omega_{ab}=\kappa c^{-s/2},\qquad
 \omega_{bc}=\kappa a^{-s/2},\qquad
 \omega_{ca}=\kappa b^{-s/2}.                             \tag{5}
\]

Su forma bilineal es el determinante cíclico

\[
\boxed{
\begin{aligned}
 \langle F,J_{a,b,c}G\rangle_s
 ={\kappa\over(abc)^{s/2}}\mathbb E_s\{&
  \overline{F(bN)}G(aN)-\overline{F(aN)}G(bN)\\
 &+\overline{F(cN)}G(bN)-\overline{F(bN)}G(cN)\\
 &+\overline{F(aN)}G(cN)-\overline{F(cN)}G(aN)\}.
                                                               \tag{6}
\end{aligned}}
\]

La identidad (3)--(6) conserva los otros primos dentro de (N), es
firmada y no usa módulos. Sin embargo, no produce el puente afirmado en
`104_115`: es una **circulación bilineal**, mientras
(B_{n,s}) es una **fuente lineal prima--polo**. La diferencia no es un
resto Hardy automáticamente positivo. El borde que convertiría una
circulación en una fuente recompone exactamente el funcional
prima--polo (B_{n,s}), cuyo signo es A1.

Por tanto queda demostrada la identidad Mecke, pero queda refutado que
ella, por sí sola, complete el certificado resolvente. Este documento no
prueba A1 ni RH.

---

## 1. Mecke para retirar una unidad de una torre

Los exponentes de (1) son independientes y

\[
 \mathbb P_s(A_p=k)=(1-p^{-s})p^{-ks},\qquad k\ge0.        \tag{7}
\]

Para toda función integrable (H), desplazar (A_q=k+1) a (k) da

\[
 \boxed{
 \mathbb E_s\{\mathbf1_{A_q\ge1}H(N)\}
 =q^{-s}\mathbb E_s\{H(qN)\}.}                           \tag{8}
\]

Aplicando (8) a

\[
 H(N)=\overline{F(N)}G(Np/q)
\]

se obtiene

\[
\begin{aligned}
 &\mathbb E_s\{\mathbf1_{A_q\ge1}
       \overline{F(N)}G(Np/q)\}\\
 &\qquad=q^{-s}\mathbb E_s\{\overline{F(qN)}G(pN)\}.
                                                               \tag{9}
\end{aligned}
\]

Multiplicar por
(\omega_{pq}(q/p)^{s/2}) y sumar prueba (3).

## 2. Antiautoadjunción y conservación

Agrupando en (3) los pares ((p,q)) y ((q,p)),

\[
\begin{aligned}
 \langle F,J_\omega G\rangle_s
 =\sum_{p<q}{\omega_{pq}\over(pq)^{s/2}}
 \mathbb E_s\{&\overline{F(qN)}G(pN)\\
               &-\overline{F(pN)}G(qN)\}.
                                                               \tag{10}
\end{aligned}
\]

Intercambiar (F,G) y conjugar prueba

\[
 J_\omega^*=-J_\omega.                                   \tag{11}
\]

Por otra parte, directamente desde (2),

\[
 (J_\omega\mathbf1)(N)
 =\sum_{q:A_q\ge1}q^{s/2}sum_p\omega_{pq}p^{-s/2}.       \tag{12}
\]

Esto se anula para todo (N) exactamente cuando (\omega u=0), pues
la antisimetría hace equivalentes el núcleo derecho y el izquierdo.

En dimensión tres, toda matriz antisimétrica no nula tiene núcleo de
dimensión uno. Sustituir (5) muestra directamente que su vector de núcleo
es

\[
 (a^{-s/2},b^{-s/2},c^{-s/2}),                            \tag{13}
\]

lo que prueba la unicidad de (5). Insertarla en (10) prueba (6).

## 3. Especialización Laguerre

Tome

\[
 F_n(N)=L_{n-1}^{(1)}(\log N),\qquad
 G_n(N)=L_{n-2}^{(2)}(\log N)=-{d\over dx}
 L_{n-1}^{(1)}(x)\bigg|_{x=\log N}.                       \tag{14}
\]

Entonces (6) es un promedio exacto de áreas orientadas de la curva

\[
 x\longmapsto
 \bigl(L_{n-1}^{(1)}(x),L_{n-2}^{(2)}(x)\bigr)            \tag{15}
\]

evaluada en los tres desplazamientos

\[
 x+\log a,\qquad x+\log b,\qquad x+\log c.                \tag{16}
\]

Ésta explica el cruzado no nulo observado en `104_115`. También explica
por qué no aparece un signo global gratuito: la curva (15) gira cada vez
que el Laguerre cruza uno de sus ceros.

## 4. Por qué no aparece (B_{n,s})

La forma prima--polo regularizada es lineal en el test:

\[
 M_s(f)
 =\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
  -\int_0^\infty e^{-(s-1)x}f(x)\,dx,
 \qquad B_{n,s}=sM_s(f_{n,s}).                            \tag{17}
\]

En cambio, (3) es alternante y bilineal:

\[
 \langle F,J_\omega F\rangle_s=0,
 \qquad
 \langle F,J_\omega(G+cF)\rangle_s
 =\langle F,J_\omega G\rangle_s.                         \tag{18}
\]

También anula constantes por construcción. El funcional (17) no lo hace:

\[
 M_s(1)=-{\zeta'(s)\over\zeta(s)}-{1\over s-1},          \tag{19}
\]

que no es idénticamente cero. Por ello no existe una identificación
natural de (3) con (M_s) en una clase lineal de tests que contenga las
constantes. Hace falta añadir una corriente abierta hacia el comparador
continuo.

Sea (J^{\rm open}) esa extensión hipotética. La identidad de divergencia
discreta--continua tendría necesariamente la forma

\[
 \langle\mathbf1,J^{\rm open}f\rangle=M_s(f).             \tag{20}
\]

Pero (20), con el test Laguerre, es precisamente el funcional que se desea
acotar. Cerrar la corriente para recuperar positividad elimina (20);
abrirla para recuperar (17) vuelve a introducir (B_{n,s}) con su signo
desconocido. Éste es el gate fuente--circulación.

La identidad general de Palm de segundo orden de `104_50` expresa la misma
obstrucción en coordenadas de covarianza:

\[
 \mathbb E_s[Z_fZ_g]
 =\operatorname{Cov}_s(D_f,D_g)+M_s(f)M_s(g).             \tag{21}
\]

La nueva fórmula (3) no contradice (21): extrae la parte alternante de los
intercambios, mientras (21) extrae la parte simétrica. Ninguna de las dos
orienta por sí sola el término lineal (M_s(f)).

## 5. Consecuencia para el certificado de `104_115`

El bloque matricial

\[
 \begin{pmatrix}-S&\eta J_\omega\\-\eta J_\omega&-S\end{pmatrix}
                                                               \tag{22}
\]

puede ser positivo por Schur, y su cruzado se calcula exactamente con
(6). Pero no existe la identidad afirmada

\[
 {3\over4}A_n-\delta_n-B_{n,s}
 =\langle G_n,(22)G_n\rangle+\mathcal R_{n,s}             \tag{23}
\]

con (\mathcal R_{n,s}\ge0) como consecuencia de Mecke. Definir
\(\mathcal R_{n,s}\) por (23) solo renombra A1. Para sostener (23) haría
falta un teorema adicional que compare la fuente abierta (20) con la
energía de circulación (22); ésa es nuevamente una desigualdad firmada
prima--polo, no una identidad.

## Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 triangle_exchange_mecke_check.py
```

