# Phase 29 — Doc 35: Dirección D — Deslocalización de Eigenvectores y el Teorema de Szegő

**Fecha:** junio 2026  
**Dirección:** D (deslocalización de eigenvectores via la teoría de polinomios ortogonales y Szegő)  
**Objetivo:** Inc. Inv. es equivalente a la deslocalización uniforme de los eigenvectores de $J_\infty$ (Doc 22): $|c_n|^2 = 1/N$ para todos los $n$. Investigar si la teoría de Szegő para operadores de Jacobi implica esta deslocalización para el operador $J_\infty = D + P$ del CCM.

---

## 1. La deslocalización como reformulación de Inc. Inv.

**Recordatorio (Doc 22, Proposición 8).** Sean $\{\psi_n\}_{n\geq 1}$ los eigenvectores de $J_\infty$ correspondientes a los eigenvalores $\{\tilde\gamma_n\}$, normalizados. Los pesos de deslocalización son $c_n := \langle e_0, \psi_n\rangle$ (componente en el vector cíclico $e_0$).

**Proposición 1** (equivalencia deslocalización—Inc. Inv., Doc 22). Las siguientes son equivalentes:

(i) $|c_n|^2 = 1/N$ para todo $n = 1, \ldots, N$ (deslocalización uniforme).

(ii) $m_\infty^{WT}(z) = m_\infty^{emp}(z)$ (las funciones WT y empírica coinciden).

(iii) Inc. Inv.: $\tilde\gamma_n = \gamma_n$ para todo $n$ Y los pesos son iguales.

*Prueba.* $m^{WT}(z) = \sum_n |c_n|^2/(z-\tilde\gamma_n)$ y $m^{emp}(z) = (1/N)\sum_n 1/(z-\gamma_n)$. Si $\tilde\gamma_n = \gamma_n$ y $|c_n|^2 = 1/N$: las dos funciones coinciden. La dirección inversa: por la unicidad de la representación de Stieltjes. $\square$

**Simplificación.** Si ya sabemos (del Doc 31 Teorema 2) que $\tilde\gamma_n = \gamma_n + O(1/(n\log^2 n))$ (perturbación pequeña), la pregunta de deslocalización se reduce a: ¿los pesos satisfacen $|c_n|^2 = 1/N$ cuando los eigenvalores son exponencialmente próximos a los $\gamma_n$?

---

## 2. Los polinomios ortogonales y sus normas

**Definición.** Sean $\{P_n\}_{n\geq 0}$ los polinomios ortogonales con respecto a la medida espectral $\mu_\infty^{WT}$ de $J_\infty$:

$$\int P_n(t) P_m(t) \, d\mu_\infty^{WT}(t) = \delta_{nm}, \quad P_n(t) = k_n t^n + \ldots, \; k_n > 0.$$

Los coeficientes de Jacobi de $J_\infty$ están relacionados por:

$$b_n = \frac{\langle t P_n, P_n\rangle}{1} = \int t P_n(t)^2 \, d\mu_\infty^{WT}(t), \quad a_n^2 = \frac{k_n}{k_{n+1}} \cdot \frac{1}{\|P_n\|^2}.$$

**El peso de deslocalización.** El componente $c_n$ del eigenvector $\psi_n$ en $e_0$ satisface:

$$|c_n|^2 = \mu_\infty^{WT}(\{\tilde\gamma_n\}) = \frac{1}{k_{n_0}^2 \|P_{n_0}\|^{-2}} = \frac{1}{|P_{n_0}'(\tilde\gamma_n)|^2 \|P_{n_0}\|^2},$$

donde la primera expresión usa la relación estándar entre la medida espectral y los polinomios ortogonales.

En términos más concretos: $|c_n|^2 = 1/\sum_k P_k(\tilde\gamma_n)^2$ (por la resolución de la identidad).

**La deslocalización uniforme.** $|c_n|^2 = 1/N$ iff $\sum_k P_k(\tilde\gamma_n)^2 = N$ para todo $n$. Para $N \to \infty$: esto dice que los polinomios ortogonales evaluados en los eigenvalores tienen normas iguales — una condición de "equidistribución" de los $P_k$ en los puntos $\tilde\gamma_n$.

---

## 3. El Teorema de Szegő para medidas en la recta real

**El Teorema de Szegő clásico (1920).** Sea $\mu$ una medida en $[-1,1]$ absolutamente continua con densidad $w(x) = d\mu/dx > 0$ casi en todas partes. Sea $k_n$ el coeficiente líder del $n$-ésimo polinomio ortogonal. Entonces:

$$\lim_{n\to\infty} k_n^{-2} = \exp\!\left\{\frac{1}{2\pi}\int_{-1}^1 \frac{\log w(x)}{\sqrt{1-x^2}}\,dx\right\} > 0,$$

si y solo si la condición de Szegő $\int \log w(x)/\sqrt{1-x^2}\,dx > -\infty$ se satisface. Si la condición falla: $k_n^{-2} \to 0$, es decir, $k_n \to \infty$ ("los polinomios son grandes").

**Versión para la recta real (Krein, 1945).** Para medidas $\mu$ en $\mathbb{R}$ con soporte no-acotado: la condición de Szegő generalizada toma la forma del decaimiento de los coeficientes del producto de Blaschke en el semi-plano superior.

**La condición de Szegő para $\mu_\infty^{WT}$.** La medida $\mu_\infty^{WT}$ de $J_\infty$ es la medida espectral del operador de Jacobi con coeficientes $(b_n, a_n) = (\gamma_n, \pi/\log\gamma_n)$.

Para un operador de Jacobi con coeficientes $(b_n, a_n)$: la teoría de Szegő (en la versión de Simon-Steklov) relaciona las propiedades asintóticas de los polinomios con las propiedades asintóticas de los coeficientes. Específicamente (Simon, 2004):

$$\text{Szegő} \iff \sum_n (b_n - b_n^{(0)})^2 + (a_n - a_n^{(0)})^2 < \infty,$$

donde $(b_n^{(0)}, a_n^{(0)})$ son los coeficientes de un operador de referencia "libre."

---

## 4. El operador de referencia para $J_\infty$

**El operador libre natural.** El operador $J_\infty = D + P$ tiene coeficientes diagonales $b_n = \gamma_n$ (parte libre) y perturbación $P$ con coeficientes $a_n = \pi/\log\gamma_n$. El operador de referencia natural es el operador diagonal $D = \text{diag}(\gamma_n)$.

**El operador diagonal $D$.** Para el operador PURAMENTE DIAGONAL $D = \text{diag}(\gamma_n)$: los eigenvalores son exactamente $\gamma_n$ y los eigenvectores son $\{e_n\}$ (la base canónica). En este caso: $\langle e_0, e_n\rangle = \delta_{n0}$ — el eigenvector $e_0$ tiene componente $c_0 = 1$ en el autovector $e_0$ (eigenvalor $\gamma_0$) y $c_n = 0$ para $n \geq 1$. Es decir, $D$ está MÁXIMAMENTE LOCALIZADO en $e_0$.

Esto es lo opuesto a la deslocalización: en el operador libre $D$, todo el peso está en $n=0$, no distribuido uniformemente.

**El rol de la perturbación $P$.** La perturbación $P$ (con coeficientes $a_n = \pi/\log\gamma_n$) es la que "mezcla" los eigenvalores y produce deslocalización. La fuerza de la deslocalización depende del tamaño de $P$: $\|P\|_{op} \leq 2\pi/\log\gamma_0 \approx 2.36$.

**Proposición 2** (la condición de Szegő para $J_\infty$ vs $D$). La desviación de los coeficientes de $J_\infty$ del operador de referencia $D$ es:

$$\sum_n (b_n - b_n^{(D)})^2 + (a_n - a_n^{(D)})^2 = \sum_n 0^2 + \left(\frac{\pi}{\log\gamma_n}\right)^2 = \pi^2\sum_n \frac{1}{(\log\gamma_n)^2}.$$

Esta serie DIVERGE (pues $\log\gamma_n \sim \log n + \log\log n$ y $\sum 1/(\log n)^2$ diverge).

**Conclusión.** La condición de Szegő (finitud de la suma de cuadrados) NO se satisface para $J_\infty$ respecto al operador diagonal $D$. El Teorema de Szegő (en la forma de perturbación finita) no aplica directamente.

---

## 5. La teoría de Szegő "a escala logarítmica"

**Operador de referencia modificado.** En lugar de comparar con $D$, comparamos con un operador de Jacobi cuasi-libre $D^{(0)}$ con:

$$b_n^{(0)} = \gamma_n, \quad a_n^{(0)} = \frac{\pi}{\log\gamma_n}.$$

Este es el operador $J_\infty$ mismo. Trivialmente: $J_\infty = D^{(0)}$, y la "perturbación" es cero.

El Teorema de Szegő en este contexto diría algo sobre las normas de los polinomios ortogonales con respecto a $\mu_\infty^{WT}$ comparadas con los polinomios ortogonales de $D^{(0)}$.

**El problema.** El operador $D^{(0)} = J_\infty$ tiene un espectro conocido (los eigenvalores $\tilde\gamma_n$), pero los PESOS $|c_n|^2$ son lo que queremos determinar. El Teorema de Szegő no se aplica a sí mismo: necesitamos un OTRO operador como referencia.

---

## 6. El Teorema de Szegő para operadores de Jacobi con coeficientes crecientes

**La teoría de OPRL con coeficientes no-acotados.** Para operadores de Jacobi con $b_n \to \infty$ (como $J_\infty$ con $b_n = \gamma_n \to \infty$): la teoría de Szegő clásica no aplica (está diseñada para coeficientes acotados). Se requiere la teoría de "polinomios ortogonales de peso variable" (varying weight) o la teoría de Szegő para operadores de Jacobi con crecimiento.

**Teorema de Szegő generalizado (Lubinsky-Saff, 1988; Levin-Lubinsky, 2008).** Para medidas $\mu$ con densidad que decrece como $w(x) \sim e^{-Q(x)}$ para una función $Q(x) \to \infty$: los polinomios ortogonales satisfacen:

$$k_n(a_n^{(Q)})^n \to 1,$$

donde $a_n^{(Q)}$ es el radio del "equilibrio externo" de la función $Q$. Este resultado controla las NORMAS de los polinomios pero no los VALORES en puntos individuales.

**Aplicación tentativa a $\mu_\infty^{WT}$.** La medida $\mu_\infty^{WT}$ tiene soporte discreto $\{\tilde\gamma_n\}$ — no es absolutamente continua. Para medidas DISCRETAS: los polinomios ortogonales satisfacen la relación de tres términos, pero la teoría de Szegő generalizada no se aplica directamente a medidas discretas con soporte no-acotado.

---

## 7. El argumento de la equidistribución de Weyl

**La observación.** Los coeficientes del operador $J_\infty$ satisfacen $a_n = \pi/\log\gamma_n$ y $b_n = \gamma_n$. La perturbación $P$ tiene entradas:

$$P_{n,n+1} = P_{n+1,n} = a_n = \frac{\pi}{\log\gamma_n}.$$

Para la deslocalización, necesitamos que los eigenvectores de $J_\infty = D + P$ "mezclen" las componentes de $D$.

**La equidistribución de Weyl.** Por el Teorema de Weyl sobre la equidistribución: si los $\{\log\gamma_n \cdot t \mod 2\pi\}$ son equidistribuidos en $[0,2\pi]$ para todo $t$ irracional, entonces las sumas $\sum_n f(\gamma_n)\cos(t\log\gamma_n)$ se promedian a cero — una forma de "incoherencia" entre los modos del eigenvector.

**La incoherencia y la deslocalización.** Un eigenvector deslocalizdo $\psi_n$ de $J_\infty = D + P$ satisface:

$$\psi_n = e_n + \sum_{k \neq n} \frac{P_{kn}}{\gamma_n - \gamma_k} e_k + O(\|P\|^2).$$

Los coeficientes de primer orden de la perturbación:

$$\langle e_0, \psi_n\rangle = \frac{P_{0n}}{\gamma_n - \gamma_0} + O(\|P\|^2) = \frac{a_0}{\gamma_n - \gamma_0} + O(\|P\|^2).$$

Para $n$ grande: $|c_n|^2 \approx a_0^2/(\gamma_n-\gamma_0)^2 = (\pi/\log\gamma_0)^2/\gamma_n^2 \to 0$.

Esto NO es $1/N$: los pesos decaen a 0 para $n$ grande en el primer orden de perturbación.

**El problema con la perturbación estándar.** En primer orden, los pesos $|c_n|^2 \sim \pi^2/(\gamma_n^2\log^2\gamma_0)$ decaen a cero con $n$. Para que $|c_n|^2 = 1/N$ (uniformemente): los órdenes superiores de la perturbación deben CANCELAR el decaimiento de primer orden y producir un peso uniforme.

Esta cancelación es el MISMO problema que Inc. Inv.: requiere exactitud en todos los órdenes de la perturbación.

---

## 8. Un enfoque alternativo: la matriz de resolución y la función de correlación

**El operador de proyección.** Sea $P^{>T} = \sum_{n: \gamma_n > T} |e_n\rangle\langle e_n|$ el proyector sobre el complemento de los $N = N_\Xi(T)$ primeros eigenvalores. La deslocalización uniforme equivale a:

$$\langle e_0, P^{>T} e_0\rangle = \sum_{n: \gamma_n > T} |c_n|^2 = 1 - \frac{N_\Xi(T)}{N}$$

para cualquier truncación $T$.

**La identidad de Parseval.** $\sum_{n=0}^\infty |c_n|^2 = 1$ (ortogonalidad). La deslocalización uniforme requiere:

$$\sum_{n=0}^{N_\Xi(T)-1} |c_n|^2 = \frac{N_\Xi(T)}{N} \quad \text{para todo } T.$$

Esto dice que los pesos son "proporcionales al conteo" — una condición de equidistribución de los pesos.

**La función de conteo de peso.** Define $W(T) := \sum_{n: \tilde\gamma_n \leq T} |c_n|^2 = \mu_\infty^{WT}([0,T])$. La deslocalización uniforme equivale a:

$$W(T) = \frac{N_{C_\infty}(T)}{N} \cdot 1 = \frac{N_\Xi(T)}{N}$$

(usando que los eigenvalores de $J_\infty$ son los ceros de $C_\infty$, y asumiendo $N_{C_\infty}(T) = N_\Xi(T)$, que es Inc. Inv.).

Nuevamente: la deslocalización uniforme está directamente vinculada a Inc. Inv. — no hay un camino independiente.

---

## 9. El resultado de Simon sobre la deslocalización de operadores de Jacobi

**Teorema de Simon (2003) sobre polinomios ortogonales de tipo libre.** Para operadores de Jacobi con $a_n \to 0$ y $b_n \to \infty$ (el régimen de $J_\infty$ = caso "Freud"): los eigenvectores satisfacen una ley de LOCALIZACIÓN, no de deslocalización. Específicamente:

Si $b_n \to \infty$ y $a_n/b_n \to 0$ (caso de nuestro $J_\infty$ con $b_n = \gamma_n$ y $a_n = \pi/\log\gamma_n$): los eigenvectores se concentran LOCALMENTE cerca de cada eigenvalor, con $|c_n|^2 \to 0$ para $n \to \infty$.

*Esta es la LEY CONTRARIA a la deslocalización uniforme.*

**Proposición 3** (localización de $J_\infty$, tentativo). Para el operador $J_\infty$ con $b_n = \gamma_n \to \infty$ y $a_n = \pi/\log\gamma_n \to 0$: en el régimen $n \to \infty$, los eigenvectores satisfacen:

$$|c_n|^2 = |\langle e_0, \psi_n\rangle|^2 \to 0.$$

*Prueba tentativa.* Del cálculo perturbativo (§7): en primer orden, $|c_n|^2 \approx a_0^2/\gamma_n^2 \to 0$. Las correcciones de orden superior no cambian el hecho de que $|c_n|^2 \to 0$ para $n \to \infty$. $\square$ (pendiente de verificación rigurosa.)

**La tensión con Inc. Inv.** Si $|c_n|^2 \to 0$: la deslocalización uniforme FALLA (ya que los pesos no son constantes). Pero Inc. Inv. equivale a deslocalización uniforme (Proposición 1). ¿Esto refuta Inc. Inv.?

---

## 10. Resolución de la tensión: el rol del factor $N$

**El punto sutil.** La "deslocalización uniforme" $|c_n|^2 = 1/N$ involucra el factor $N$ (el número total de eigenvalores). Para $N \to \infty$: $1/N \to 0$. Luego $|c_n|^2 = 1/N \to 0$ es CONSISTENTE con $|c_n|^2 \to 0$.

La deslocalización dice: todos los $|c_n|^2$ son IGUALES (cada uno igual a $1/N$). La localización dice: los $|c_n|^2$ decaen a 0 con $n$ (algunos son mucho menores que la media $1/N$).

**La condición precisa.** Para $n$ en el rango $[0, N-1]$ (los $N$ primeros eigenvalores): deslocalización requiere $|c_n|^2 \approx 1/N$ uniformemente. Localización dice que para $n \sim N$: $|c_n|^2 \ll 1/N$.

**Proposición 4** (incompatibilidad con la teoría de operadores no-acotados). Para operadores de Jacobi con $b_n \to \infty$ y la estructura de $J_\infty$: la teoría de operadores no-acotados (Atkinson, 1964; Janas-Naboko, 1999) muestra que los eigenvectores satisfacen $|c_n|^2 \sim C/\gamma_n^\alpha$ para algún $\alpha > 0$. Esto es $|c_n|^2 \sim 1/n^{(1+\alpha)\beta}$ con $\gamma_n \sim n\log n$ (por la fórmula de von Mangoldt).

La media: $\frac{1}{N}\sum_{n=0}^{N-1}|c_n|^2 = \frac{1}{N}\sum_{n=0}^{N-1}\frac{C}{\gamma_n^\alpha} \approx \frac{C}{N}\sum_{n=0}^N\frac{1}{(n\log n)^\alpha} \approx \frac{C}{N}\cdot\frac{N^{1-\alpha}}{(\log N)^\alpha}$.

Para que la media sea $\approx 1/N$: se necesita $C\cdot N^{1-\alpha}/(\log N)^\alpha \approx 1$, es decir, $N^\alpha \approx C(\log N)^\alpha$, que falla para $\alpha > 0$.

**Conclusión tentativa.** Para los operadores de Jacobi con el comportamiento asintótico de $J_\infty$ ($b_n \sim n\log n$, $a_n \sim \pi/\log n$): la distribución de pesos NO es uniforme — los pesos decaen con $n$. Esto sugiere que la deslocalización uniforme ($|c_n|^2 = 1/N$) NO se satisface en general para $J_\infty$.

Si esto es correcto: Inc. Inv. (= deslocalización uniforme) NO seguiría del comportamiento de los eigenvectores de un operador de Jacobi con estos coeficientes. Sería un OBSTÁCULO NUEVO.

---

## 11. Honestidad: la Dirección D como obstáculo más que como herramienta

**El resultado sorprendente (y honesto).** El análisis de la deslocalización sugiere que el operador $J_\infty$, con sus coeficientes específicos $b_n = \gamma_n$ y $a_n = \pi/\log\gamma_n$, NO exhibe deslocalización uniforme en general. Los eigenvectores de operadores de Jacobi no-acotados son generalmente LOCALIZADOS (pesos que decaen con el índice).

**La resolución (si existe).** Inc. Inv. sería cierta SOLO SI los pesos $|c_n|^2$ de $J_\infty$ son exactamente $1/N$ — una condición ESPECIAL que va contra el comportamiento genérico de los operadores de Jacobi no-acotados. Esto solo puede ocurrir si hay una razón estructural profunda (aritmética o espectral) que FUERZA la uniformidad de los pesos.

Esta razón estructural, si existe, estaría conectada con la ARITMÉTICA de los ceros de $\zeta$ y no con propiedades genéricas de los operadores de Jacobi.

**Corolario 4** (reformulación más profunda del muro). El análisis de la Dirección D sugiere que Inc. Inv. es equivalente a una condición ARITMÉTICA profunda: los pesos $|c_n|^2$ de los eigenvectores de $J_\infty$ son uniformes iff la distribución de los ceros de $\zeta$ tiene una "propiedad de equidistribución" que va más allá de la simple densidad von Mangoldt.

Esta observación conecta Inc. Inv. con las conjeturas de Montgomery sobre los pares de correlaciones de los ceros (Random Matrix Theory), donde la uniformidad de los pesos sería una consecuencia de la estructura GUE de los ceros.

---

## 12. Conclusión de la Dirección D

**Resultado positivo.** La formulación de Inc. Inv. como deslocalización $|c_n|^2 = 1/N$ es correcta y explícita. La condición tiene una interpretación clara en términos de la función de Weyl-Titchmarsh.

**Resultado negativo.** La teoría de Szegő para operadores de Jacobi no-acotados (el régimen de $J_\infty$) predice LOCALIZACIÓN, no deslocalización. Esto sugiere que la deslocalización uniforme es una condición ESPECIAL, no genérica.

**El muro profundizado.** Inc. Inv. requiere que los eigenvectores de $J_\infty$ sean uniformemente deslocalizados — una condición que sería violada en el régimen genérico de operadores de Jacobi no-acotados. La única razón por la que podría satisfacerse es la ESTRUCTURA ARITMÉTICA específica de los coeficientes $b_n = \gamma_n$ (ceros de $\zeta$) y $a_n = \pi/\log\gamma_n$ (espaciados de los ceros).

**Conexión con RMT.** Si los ceros de $\zeta$ tienen las correlaciones predichas por GUE (conjetura de Montgomery), entonces los eigenvalores de $J_\infty$ tienen la estructura espectral de una matriz aleatoria unitaria — y en ese régimen, los eigenvectores SON uniformemente deslocalizados (conjetura de delocalization de eigenvectores de matrices aleatorias). Probar Inc. Inv. desde esta perspectiva requeriría pasar por la conjetura de Montgomery, que es abierta.

---

*Fin de los documentos de Phase 30. Resumen en Doc 36.*
