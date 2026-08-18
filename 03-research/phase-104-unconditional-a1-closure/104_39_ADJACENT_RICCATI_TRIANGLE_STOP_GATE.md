# 104_39 — Riccati adyacente, triángulo discreto y stop-gate de necesidad

**Rol.** Auditar el criterio suficiente adyacente de `104_34`

\[
 \mathcal T_n=4H_nd_n-(H_n+d_n-H_{n+1})^2\ge0,
 \qquad
 H_n=\lambda_n-{501\over2002}A_n,
 \quad
 d_n={1501\over2002}\Delta A_n+\gamma,                 \tag{1}
\]

como una recurrencia de Riccati, y decidir si su positividad puede ser el
objetivo final en lugar de la desigualdad escalar \(H_n\ge0\).

El resultado es preciso:

1. (1) es exactamente una desigualdad triangular para
   \(\sqrt{H_n},\sqrt{d_n},\sqrt{H_{n+1}}\), no una recurrencia con un
   signo nuevo;
2. es **estrictamente más fuerte** que \(H_n\ge0\): un aporte de cuarteto
   enteramente sobre la línea crítica mantiene todos los márgenes
   positivos y rompe (1) de forma exacta;
3. bajo RH, para la zeta de Riemann, (1) sí vale para todo \(n\)
   suficientemente grande, por lo que no hay una obstrucción asintótica;
4. en consecuencia, (1) sigue siendo un criterio suficiente válido para
   la zeta real, pero no debe confundirse con A1 ni tratarse como condición
   necesaria. Probarlo exige regularidad aritmética adicional que el mero
   soporte crítico y la positividad de Li no contienen.

Este documento no prueba (1) para la zeta, A1 ni RH. Sí cierra el intento
de obtener (1) solo mediante álgebra de Riccati, positividad de los
coeficientes de Li o localización crítica término a término.

## 1. Factorización exacta: la recurrencia es un triángulo

Supongamos \(H_n\ge0\), \(d_n>0\) y \(H_{n+1}\ge0\), y escribamos

\[
 x_n=\sqrt{H_n},\qquad a_n=\sqrt{d_n},\qquad x_{n+1}=\sqrt{H_{n+1}}.
\]

La identidad algebraica

\[
\boxed{
 \mathcal T_n=
 \bigl((x_n+a_n)^2-x_{n+1}^2\bigr)
 \bigl(x_{n+1}^2-(x_n-a_n)^2\bigr)}                         \tag{2}
\]

prueba las equivalencias

\[
\boxed{
 \mathcal T_n\ge0
 \iff |x_n-a_n|\le x_{n+1}\le x_n+a_n}                     \tag{3}
\]

y

\[
\boxed{
 (\sqrt{H_n}-\sqrt{d_n})^2
 \le H_{n+1}\le
 (\sqrt{H_n}+\sqrt{d_n})^2.}                               \tag{4}
\]

Cuando \(H_nd_n>0\), existe por tanto un parámetro

\[
 u_n={H_n+d_n-H_{n+1}\over2\sqrt{H_nd_n}}
\]

tal que

\[
\boxed{
 H_{n+1}=H_n+d_n-2\sqrt{H_nd_n}\,u_n,\qquad |u_n|\le1.}   \tag{5}
\]

Ésta es la forma Riccati completa. El parámetro \(u_n\) no recibe signo de
la identidad: acotarlo por uno es exactamente la desigualdad de
Cauchy--Schwarz para la compresión de `104_34`, no una consecuencia nueva
de reescribirla.

En variables relativas \(r_n=H_{n+1}/H_n\) y
\(\delta_n=d_n/H_n\), (3) dice

\[
 (1-\sqrt{\delta_n})^2\le r_n\le
 (1+\sqrt{\delta_n})^2.                                    \tag{6}
\]

Para la escala esperada \(H_n\asymp n\log n\), \(d_n\asymp\log n\),
se tiene \(\delta_n\asymp n^{-1}\). Así (1) exige una regularidad local
de raíz cuadrada del margen, además de su positividad.

## 2. No es una condición necesaria para el margen

La diferencia entre positividad y regularidad adyacente puede exhibirse
con un cuarteto crítico exacto. Sea

\[
 L_n^{\rm crit}=4-4\cos(n\pi/2)\in\{0,4,8,4\}.              \tag{7}
\]

Es la contribución de Li de un cuarteto con \(|w|=1\), y en particular

\[
 L_n^{\rm crit}\ge0\qquad(n\ge1).                           \tag{8}
\]

Considérese primero el modelo normalizado

\[
 \widehat H_n=1+L_n^{\rm crit},\qquad \widehat d_n=1.       \tag{9}
\]

Todos los márgenes son al menos uno. Sin embargo, en \(n=4\),

\[
 \widehat H_4=1,\qquad \widehat H_5=5,\qquad
 \widehat{\mathcal T}_4
 =4-(1+1-5)^2=-5<0.                                         \tag{10}
\]

La misma obstrucción no depende de la normalización. Sea una sucesión base
con \(H_n\ge0\) y sea \(d_q>0\) fijo. Elija \(q\equiv0\pmod4\). Al
añadir \(M L_n^{\rm crit}\), con multiplicidad entera \(M\ge1\), se tiene
\(L_q^{\rm crit}=0\), \(L_{q+1}^{\rm crit}=4\), y se conserva
\(H_n\ge0\) para todo \(n\), pero

\[
 \mathcal T_q(M)=4H_qd_q-
   (H_q+d_q-H_{q+1}-4M)^2\longrightarrow-\infty              \tag{11}
\]

cuando \(M\to\infty\) a través de los enteros.

Por tanto:

\[
\boxed{
 H_n\ge0\ \hbox{para todo }n
 \quad\not\Longrightarrow\quad
 \mathcal T_n\ge0\ \hbox{para todo }n.}                   \tag{12}
\]

El ejemplo no pretende ser otro producto de Euler: prueba exactamente que
el criterio adyacente no se deduce de positividad de Li, simetría funcional
y soporte crítico. Una prueba para la zeta debe usar la distribución y los
pesos especiales de sus primos; no alcanza sumar contribuciones positivas
de ceros críticos.

## 3. El falsificador fuera de la línea en forma racional

Puede hacerse racional el testigo off-line de `104_34`. Tome

\[
 w={5i\over4},\qquad
 \rho={1\over1-w}={16\over41}+{20\over41}i,                  \tag{13}
\]

de modo que \(0<\Re\rho<1/2\). La órbita funcional recíproca aporta

\[
 L_n^{\rm off}
 =4-\left(w^n+\bar w^n+w^{-n}+\bar w^{-n}\right).           \tag{14}
\]

Para \(n=4k\),

\[
 L_{4k}^{\rm off}
 =4-2\left((5/4)^{4k}+(4/5)^{4k}\right),                    \tag{15}
\]

que es negativo y exponencial en módulo. Contra cualquier base
polinómica existe entonces un primer cruce \(H_{N-1}\ge0>H_N\). Si
\(\mathcal T_{N-1}\ge0\), (4) forzaría \(H_N\ge0\), contradicción. Por
consiguiente \(\mathcal T_{N-1}<0\).

El verificador racional adjunto usa la base \(n^2\), encuentra el primer
cruce exactamente en \(N=28\) y comprueba el determinante negativo sin
punto flotante.

## 4. Bajo RH el gate es asintóticamente automático

Esta sección solo clasifica la fuerza lógica de (1); no se usa como input
incondicional.

Supongamos RH. Para cada cero \(1/2+i\gamma\), \(\gamma>0\), sea

\[
 \vartheta_\gamma=2\arctan {1\over2\gamma},
 \qquad 0<\vartheta_\gamma\le {1\over\gamma}.
\]

La representación positiva de Li es

\[
 \lambda_n=2\sum_{\gamma>0}
       \bigl(1-\cos(n\vartheta_\gamma)\bigr).                \tag{16}
\]

La serie de la diferencia converge absolutamente y

\[
\begin{aligned}
 |\Delta\lambda_n|
 &\le2\sum_{\gamma>0}
   \min\left\{\vartheta_\gamma,
        {2n+1\over2}\vartheta_\gamma^2\right\}\\
 &\le2\sum_{0<\gamma\le n}{1\over\gamma}
 +(2n+1)\sum_{\gamma>n}{1\over\gamma^2}.                   \tag{17}
\end{aligned}
\]

La cota clásica \(N(T)=O(T\log T)\), integrada por partes en (17), da

\[
 \boxed{\Delta\lambda_n=O(\log^2 n)\qquad({\rm RH}).}       \tag{18}
\]

Por otra parte,

\[
 A_n={n\over2}(\log n+\gamma-1-\log2\pi)+O(\log n),
 \qquad
 \Delta A_n={1\over2}\log n+O(1),                          \tag{19}
\]

y el teorema condicional de Lagarias da

\[
 \lambda_n=A_n+O(\sqrt n\log n).                            \tag{20}
\]

Con \(c=501/2002\), \(\kappa=1-c\), se sigue

\[
 H_n={\kappa\over2}n\log n+O(n),\qquad
 d_n={\kappa\over2}\log n+O(1),                            \tag{21}
\]

mientras que

\[
 H_n+d_n-H_{n+1}
 =\Delta A_n+\gamma-\Delta\lambda_n
 =O(\log^2 n).                                               \tag{22}
\]

Finalmente,

\[
\boxed{
 \mathcal T_n
 =\kappa^2 n\log^2 n
  +O(n\log n+\sqrt n\log^2 n+\log^4 n)>0}                  \tag{23}
\]

para todo \(n\) suficientemente grande bajo RH.

La conclusión correcta es doble. El gate no es demasiado fuerte en la
escala asintótica real de zeta, pero sí añade una condición local finita
que RH/positividad por sí solas no proporcionan. No se puede declarar
\(\mathcal T_n\ge0\) equivalente a RH sin certificar además todos sus
índices finitos.

## 5. Libertad de la referencia: óptimo formal y circularidad

La referencia diagonal de bandera de `104_34` no es la única forma
positiva que interpola \(A_n\) sobre los prefijos. Esta libertad parece
permitir mejorar el determinante, pero su optimización exacta muestra que
no crea una desigualdad.

Sea \(\mathsf A\) cualquier forma positiva con
\(\mathsf A[g_n]=A_n\), y ponga

\[
 a_n=\mathsf A[\phi_n],\qquad D_n=\kappa a_n+\gamma.
\]

Como \(g_{n+1}=g_n+\phi_n\), se tiene

\[
 \mathsf A(g_n,\phi_n)={\Delta A_n-a_n\over2}.
\]

Para \(\mathsf M=\kappa\mathsf A-\mathsf Q_0\), la compresión sobre
\(\mathrm{span}\,\{g_n,\phi_n\}\) tiene diagonal \(H_n,D_n\) y
determinante, multiplicado por cuatro,

\[
 F_n(D)=4H_nD-(H_n+D-H_{n+1})^2.                             \tag{24}
\]

Como función de \(D\), es una parábola cóncava y

\[
 \boxed{D_n^{\rm opt}=H_n+H_{n+1},\qquad
        \max_DF_n(D)=4H_nH_{n+1}.}                           \tag{25}
\]

El óptimo formal reduce el determinante exactamente a la positividad que
se quiere propagar. Pero realizarlo exige elegir

\[
 a_n^{\rm opt}={H_n+H_{n+1}-\gamma\over\kappa},              \tag{26}
\]

que ya contiene \(H_{n+1}\). Es una codificación circular del objetivo,
además de las restricciones globales que impondría construir una sola
forma positiva con todas esas diagonales.

Hay una referencia fija extrema que sirve para comprobar que el cambio de
gauge tampoco aporta signo. Declare ortogonales los prefijos \(g_k\) y
déles normas cuadradas \(A_k\). Esta forma es positiva y

\[
 a_n=A_n+A_{n+1}.
\]

En la base \(\{g_n,g_{n+1}\}\), su compresión es

\[
 \begin{pmatrix}
 H_n&-\frac12(B_n+B_{n+1}+\gamma)\\
 -\frac12(B_n+B_{n+1}+\gamma)&H_{n+1}
 \end{pmatrix},                                             \tag{27}
\]

porque

\[
 \mathsf Q_0(g_n,g_{n+1})
 =B_n+{\Delta B_n+\gamma\over2}
 ={B_n+B_{n+1}+\gamma\over2}.
\]

Esto produce otro criterio suficiente,

\[
 \boxed{
 \mathcal U_n:=4H_nH_{n+1}-(B_n+B_{n+1}+\gamma)^2\ge0.}     \tag{28}
\]

No es un teorema nuevo sobre zeta: la contribución crítica de la sección 2
lo rompe para multiplicidad grande, pues el término cuadrático en \(M\)
domina al lineal. Tampoco (28) se ordena en general con (1); controla el
valor \(B_n+B_{n+1}\), mientras (1) controla la pendiente
\(\Delta B_n\). La elección de referencia solo mueve la dificultad entre
esas dos coordenadas.

Por tanto, optimizar la métrica de referencia no da un mecanismo
coercivo. El óptimo es tautológico y las referencias fijas vuelven a pedir
una desigualdad aritmética firmada no demostrada.

## 6. Consecuencia para el frente de Phase 104

La inducción mínima que se desea es solo

\[
 H_{n+1}=H_n+d_n-(H_n+d_n-H_{n+1})\ge0.                      \tag{29}
\]

La cota de Schur sustituye el requisito unilateral de (29) por

\[
 |H_n+d_n-H_{n+1}|\le2\sqrt{H_nd_n},                         \tag{30}
\]

que controla también el signo innecesario y es estrictamente más fuerte,
como muestra (10). La forma Riccati no elimina esa pérdida.

Por tanto `104_34` queda como un criterio suficiente legítimo, pero no
como el único frente. Tras el stop-gate Hankel de `104_37`, seguir buscando
una prueba abstracta de (30) mediante PSD, suma de cuadrados o positividad
de cuartetos críticos repetiría una categoría ya refutada. Solo tendría
sentido retomarlo si aparece una desigualdad específica para los pesos
\(\log p\) que controle la pendiente firmada

\[
 \Delta B_n+\gamma.
\]

En ausencia de esa entrada, el objetivo matemáticamente más estrecho sigue
siendo el margen escalar \(H_n\ge0\), equivalente al techo proporcional
adoptado, no el determinante adyacente.

## Verificación

```bash
cd 03-research/phase-104-unconditional-a1-closure
python3 tools/adjacent_riccati_gate_check.py
```

El script usa solo `Fraction` y verifica (2), el testigo crítico (10), el
punto racional (13) y el primer cruce off-line de la sección 3.

## Estado

* **Probado:** equivalencias triangulares (2)--(6).
* **Probado exactamente:** margen positivo no implica el gate adyacente.
* **Probado condicionalmente:** RH implica el gate para todo índice
  suficientemente grande.
* **Descartado:** obtener el gate solo de la forma Riccati, positividad de
  Li o soporte crítico término a término.
* **No probado:** el gate para la zeta en todo \(n\ge149\), A1 y RH.
