# 104_34 — Curvatura del prefijo de bandera y gate de Schur adyacente

**Rol.** Atacar directamente la cota proporcional restante

\[
 B_n:=A_n-\lambda_n\le {1501\over2002}A_n\qquad(n\ge150)
 \tag{1}
\]

desde la forma de bandera de `104_30`, sin tomar norma de operador ni
valores absolutos de la forma prima--polo. Primero se prueba y se refuta con
aritmética outward la dominación más directa de sus coeficientes Toeplitz.
Después se extrae una desigualdad coerciva estrictamente más flexible: la
positividad de una sola compresión de Schur adyacente para cada prefijo.

La desigualdad de Schur pasa el falsificador off-line y tiene margen grande
en el rango diagnóstico, pero no se prueba uniformemente. Por tanto este
documento no prueba A1 ni RH.

## 1. Auditoría de no duplicación

`103_52` obtuvo las recurrencias de diferencias para el margen anterior
\(2\lambda_n-A_n\). `103_55` certificó que su ansatz de curvatura positiva
falla en \(n=147\). `104_30` construyó la referencia positiva
\(\mathsf A_{\rm flag}\), la forma prima--polo \(\mathsf Q_0\) y sus
coeficientes

\[
 q_0=B_1=-\gamma,
 \qquad
 q_d={B_{d+1}-2B_d+B_{d-1}\over2}\quad(d\ge1).               \tag{2}
\]

Lo nuevo aquí es:

1. auditar la curvatura con la constante final \(501/2002\), no con
   \(1/2\), y hacerlo más allá del umbral \(150\);
2. probar la fórmula exacta de la compresión adyacente en la métrica de
   bandera;
3. aislar un único determinante cuadrático cuya positividad uniforme basta
   para cerrar (1), pero no exige signo de cada segunda diferencia.

No se usa literatura externa ni una búsqueda web en este ataque.

## 2. Defecto proporcional en el gauge correcto

Pongamos

\[
 c={501\over2002},\qquad
 \kappa=1-c={1501\over2002},\qquad
 H_n:=\kappa A_n-B_n=\lambda_n-cA_n.                           \tag{3}
\]

Entonces (1) es exactamente \(H_n\ge0\). La construcción de bandera de
`104_30` funciona sin cambios con base \(M=149\): el certificado finito da
\(A_{149}>0\), y \(\Delta A_k>0\) para \(k\ge149\). Adoptamos esa extensión
de una posición para poder iniciar la inducción en el último índice
certificado. En ese espacio definamos la forma algebraica

\[
 \mathsf M:=\kappa\mathsf A_{\rm flag}-\mathsf Q_0.           \tag{4}
\]

Para todo \(n\ge149\),

\[
 \boxed{\mathsf M[g_n]=H_n.}                                  \tag{5}
\]

Así (5) conserva el rayo fijo. No se pide un supremo de \(\mathsf M\) ni
positividad en todo el espacio.

## 3. Primer ataque: dominación coeficiente a coeficiente

Sea \(H_0=0\) y escribamos la segunda diferencia centrada

\[
 \nabla_c^2H_d=H_{d+1}-2H_d+H_{d-1}.                          \tag{6}
\]

Dos sumaciones discretas dan

\[
 H_n=nH_1+\sum_{d=1}^{n-1}(n-d)\nabla_c^2H_d.                \tag{7}
\]

Por tanto

\[
 H_1\ge0,\qquad \nabla_c^2H_d\ge0\ (d\ge1)                  \tag{8}
\]

sería una condición suficiente para (1). En la coordenada de `104_30`, (8)
es precisamente la dominación de los coeficientes Toeplitz

\[
 q_d(B)\le\kappa q_d(A)\qquad(d\ge1),                         \tag{9}
\]

porque

\[
 \kappa q_d(A)-q_d(B)={1\over2}\nabla_c^2H_d.                \tag{10}
\]

Esta prueba candidata no toma valores absolutos y sería más débil que pedir
positividad de toda la matriz. Sin embargo, es falsa para los datos reales
de zeta, incluso con la constante final.

### 3.1 Contra-certificado outward después de 150

`tools/flag_prefix_curvature_gate.py` reconstruye, con el generador
Hasse--eta certificado de `103_51`, los intervalos

\[
 H_n=\lambda_n^{\rm prime}+{1501\over2002}A_n.                \tag{11}
\]

Con \(K=850\), profundidad logarítmica \(820\) y escala \(10^{500}\),
prueba

\[
 \boxed{
 -{1058\over10^5}
 <H_{221}-2H_{220}+H_{219}
 <-{10577\over10^6}<0.}                                      \tag{12}
\]

Equivalentemente,

\[
 \nabla_c^2H_{220}<0,
 \qquad q_{220}(B)>\kappa q_{220}(A).                         \tag{13}
\]

El índice está dentro del rango infinito que A1 debe controlar. Así, bajar
la proporción desde \(1/2\) hasta \(501/2002\) no rescata la inducción por
curvatura ni la dominación coeficiente a coeficiente. Este es un stop-gate
exacto nuevo; no depende del diagnóstico FFT.

## 4. Compresión adyacente exacta

La falla de (8) no impide que la energía acumulada \(H_n\) sea positiva.
Para conservar esa acumulación, consideremos únicamente el plano

\[
 \mathcal P_n=\operatorname{span}\{g_n,\phi_n\},\qquad n\ge149. \tag{14}
\]

Los dos vectores son ortogonales para \(\mathsf A_{\rm flag}\), y

\[
 \mathsf A_{\rm flag}[\phi_n]=\Delta A_n.                    \tag{15}
\]

La identidad Toeplitz (2) da, sin ninguna estimación,

\[
 \begin{aligned}
 \mathsf Q_0(g_n,g_n)&=B_n,\\
 \mathsf Q_0(\phi_n,\phi_n)&=B_1=-\gamma,\\
 \mathsf Q_0(g_n,\phi_n)
 &=\sum_{d=1}^{n}q_d
 ={1\over2}(\Delta B_n-B_1).
 \end{aligned}                                                \tag{16}
\]

Definamos

\[
 d_n:=\kappa\Delta A_n+\gamma>0.                              \tag{17}
\]

Como \(B_n=\kappa A_n-H_n\), las ecuaciones (4), (16)--(17)
producen la matriz exacta

\[
 \boxed{
 \mathsf M|_{\mathcal P_n}=
 \begin{pmatrix}
 H_n&-\frac12(H_n+d_n-H_{n+1})\\
 -\frac12(H_n+d_n-H_{n+1})&d_n
 \end{pmatrix}.}                                              \tag{18}
\]

No aparece ninguna cola de operador: (18) usa solamente dos rayos
adyacentes y los valores escalares exactos.

## 5. Teorema suficiente de Schur adyacente

Pongamos

\[
 \boxed{
 \mathcal T_n
 :=4H_nd_n-(H_n+d_n-H_{n+1})^2
 =4(\kappa A_n-B_n)(\kappa\Delta A_n+\gamma)
   -(\Delta B_n+\gamma)^2.}                                  \tag{19}
\]

**Proposición.** Si

\[
 \mathcal T_n\ge0\qquad(n\ge149),                            \tag{20}
\]

entonces \(H_n\ge0\) para todo \(n\ge149\), y por tanto se obtiene (1)
para todo \(n\ge150\).

**Prueba.** El certificado finito de `103_51` da
\(\lambda_{149}-A_{149}/2>0\), y \(A_{149}>0\). Como

\[
 H_{149}=\lambda_{149}-{501\over2002}A_{149}
 =\left(\lambda_{149}-{A_{149}\over2}\right)
   +{250\over1001}A_{149},                                    \tag{21}
\]

se tiene \(H_{149}>0\). Supongamos inductivamente \(H_n\ge0\). Por
(17), \(d_n>0\), y (20) dice que el determinante de (18) es no negativo.
La matriz (18) es entonces semidefinida positiva. Puesto que
\(g_{n+1}=g_n+\phi_n\),

\[
 H_{n+1}=\mathsf M[g_n+\phi_n]\ge0.                           \tag{22}
\]

La inducción prueba la afirmación. \(\square\)

En forma escalar, (20) es la cota coerciva

\[
 \boxed{
 |\Delta B_n+\gamma|
 \le2\sqrt{(\kappa A_n-B_n)(\kappa\Delta A_n+\gamma)}.}     \tag{23}
\]

Es una cota de **pendiente firmada por energía acumulada**, no un signo de
curvatura, una positividad término a término ni una norma de operador. La
identidad (12) no la refuta.

Hay una formulación útil para el siguiente ataque. Para \(t\in\mathbb R\),

\[
 g_n+t\phi_n
 =e^{-x/2}\bigl(L_{n-1}^{(1)}(x)+tL_n(x)\bigr),               \tag{24}
\]

y (18) da

\[
 \mathsf M[g_n+t\phi_n]
 =H_n-t(H_n+d_n-H_{n+1})+t^2d_n.                              \tag{25}
\]

Luego \(\mathcal T_n\ge0\) equivale a la no negatividad de (25) para todo
\(t\), y basta verificarla en el taper óptimo

\[
 t_n^*={H_n+d_n-H_{n+1}\over2d_n},\qquad
 \mathsf M[g_n+t_n^*\phi_n]={\mathcal T_n\over4d_n}.          \tag{26}
\]

Así el frente puede atacarse como una familia Laguerre **tapered** de dos
grados consecutivos. Sigue siendo una forma prima--polo renormalizada, pero
ya no pide controlar ningún vector ajeno al camino de prefijos.

## 6. Falsificador off-line

La condición (20) no es ciega a un cero fuera de la línea. Añadamos un
cuarteto funcional con

\[
 w=e^{\alpha+i\theta},\qquad
 \rho=(1-w)^{-1},\qquad
 0<\alpha<\theta^2/4,\qquad \theta={2\pi\over q},              \tag{27}
\]

donde \(q>149\) es primo. Para \(\alpha\) suficientemente pequeño el
cuarteto queda en \(0<\Re\rho<1/2\), y su contribución es

\[
 L_n^{\rm off}=4-4\cosh(n\alpha)\cos(n\theta).                \tag{28}
\]

Para el conjunto finito \(n\le149\), (28) converge cuando
\(\alpha\downarrow0\) a \(4-4\cos(n\theta)>0\); no destruye el dato base.
Pero en la subsucesión \(n=kq\),

\[
 L_{kq}^{\rm off}=4-4\cosh(kq\alpha)\longrightarrow-\infty   \tag{29}
\]

exponencialmente, y domina a \(A_n=O(n\log n)\). Por tanto el margen
perturbado \(H_n\) cruza de positivo a negativo. En el primer cruce,
\(H_n\ge0\), \(H_{n+1}<0\) y \(d_n>0\); si \(\mathcal T_n\ge0\), (18)
sería positiva y (22) impediría el cruce. Necesariamente
\(\mathcal T_n<0\).

Así (20) detecta el falsificador off-line exigido: no puede ser deducida
solo de simetría funcional y del bloque arquimediano con una base finita.
No se afirma que el cuarteto artificial preserve un producto de Euler con
coeficientes von Mangoldt positivos; esa estructura aritmética especial
sigue siendo precisamente el posible input de una prueba de (20).

## 7. Verificación y escala observada

El mismo certificado outward que prueba (12) da, en el índice donde muere
la curvatura,

\[
 2220.98<\mathcal T_{219}<2220.99.                             \tag{30}
\]

Luego el sucesor de Schur no es otra escritura del signo refutado.

El diagnóstico no certificado
`tools/flag_prefix_adjacent_schur_diagnostic.py`, con dos radios Cauchy,
da para \(149\le n\le500\):

* bloques de curvatura centrada negativa
  \([199,241]\), \([293,336]\), \([383,417]\), \([464,499]\);
* \(\min\mathcal T_n\approx1224.944748587\), en \(n=149\);
* discrepancia máxima entre radios de \(5.1\cdot10^{-9}\) en los
  coeficientes de Li.

Estas cifras solo seleccionan el sucesor; no prueban su signo uniforme.

Se reproduce con

```bash
cd 03-research/phase-104-unconditional-a1-closure
python3 tools/flag_prefix_curvature_gate.py --index 219 --K 850 --terms 820
python3 tools/flag_prefix_adjacent_schur_diagnostic.py \
  --nmax 500 --first 149 --fft-power 18
```

## Estado

* **Probado:** la compresión exacta (18), el criterio suficiente
  (19)--(22) y su sensibilidad off-line.
* **Certificado con intervalos:** la dominación de curvatura final falla en
  \(\nabla_c^2H_{220}<0\), después del umbral; simultáneamente
  \(\mathcal T_{219}>2220\).
* **Descartado:** probar (1) por
  \(q_d(B)\le(1501/2002)q_d(A)\) coeficiente a coeficiente.
* **Frente vivo:** probar (23) para todo \(n\ge149\) conservando la
  colisión prima--polo. Es estrictamente local en la familia de prefijos y
  evita el supremo gapless de operador, pero sigue siendo un teorema
  RH-strength no demostrado.
* **No probado:** (20), A1 y RH.
