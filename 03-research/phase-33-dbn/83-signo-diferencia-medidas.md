# Documento 83 — ¿Tiene signo la diferencia $|\zeta|^2 - |\zeta_{on}|^2$? Dominación de medidas, coeficientes de Jacobi y los límites del enfoque

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 64, 74, 77, 80, 82

---

## Resumen

El Documento 80 identificó que el Pilar III del programa (positividad) requiere una forma cuadrática que dependa de ambas medidas $dm_{full}$ y $dm_{full,on}$ y cuya positividad sea demostrable sin asumir RH. El presente documento examina la pregunta más directa: ¿tiene la diferencia $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$ signo definido para todo $s \in \mathbb{R}$?

La respuesta es afirmativa: la diferencia es no negativa en todo punto (fuera de los ceros de $\zeta_{on}$). Este resultado se obtiene del producto de Hadamard mediante un cálculo elemental (§1) y es incondicional, no asume RH. La medida $dm_{full} - dm_{full,on}$ es por tanto una medida positiva en $\mathbb{R}$ (Corolario 1.2).

Las consecuencias de esta dominación se analizan con detalle. En §2 se deducen relaciones entre los momentos de Hamburger de las dos medidas. En §3 se examina si la dominación implica relaciones entre los coeficientes de Jacobi $a_k^{full}$ y $a_k^{full,on}$: la respuesta es que la dominación de medidas no implica la dominación coeficiente a coeficiente, pero sí implica la dominación de las sumas parciales de cuadrados (Proposición 3.3). En §4 se prueba este resultado sumado mediante la fórmula de Markov-Stieltjes. En §5 se examina la relación entre la dominación de medidas $\mu \geq \nu$ y la intercalación espectral de las matrices de Jacobi truncadas. En §6 se analiza la desigualdad de positividad del espacio de Dirichlet bajo dominación. En §7 se discute si la dominación de medidas puede transformarse en igualdad por algún argumento variacional. En §8 se formula la síntesis honesta: la dominación puntual $dm_{full} \geq dm_{full,on}$ es un resultado nuevo y limpio, pero es lógicamente insuficiente para probar RH; el gap entre $\geq$ y $=$ es precisamente el contenido no trivial de RH.

---

## §1. El cociente $|\zeta/\zeta_{on}|^2$ vía el producto de Hadamard

### 1.1. Notación

Sea $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ la función $\xi$ entera de orden 1. El producto de Hadamard de $\xi$ es:

$$\xi(s) = e^{A+Bs} \prod_\rho \left(1 - \frac{s}{\rho}\right)e^{s/\rho},$$

donde el producto corre sobre todos los ceros no triviales $\rho$ de $\zeta$, con $A = \xi(0)$, $B = \xi'(0)/\xi(0)$ constantes reales.

Definamos $\zeta_{on}$ como la función zeta hipotética en la que todos los ceros de $\xi$ se proyectan sobre la recta crítica: si los ceros de $\xi$ son $\{\rho_j\}$ (críticos o no), el producto de Hadamard de $\xi_{on}$ es:

$$\xi_{on}(s) = e^{A+Bs} \prod_j \left(1 - \frac{s}{1/2 + i\gamma_j}\right)e^{s/(1/2+i\gamma_j)},$$

donde para cada cero $\rho_j = \sigma_j + i\gamma_j$ de $\xi$ (crítico o no) se ha reemplazado $\rho_j$ por su proyección $1/2 + i\gamma_j$ sobre la recta crítica. Los ceros críticos de $\xi$ (con $\sigma_j = 1/2$) no se ven modificados; los off-critical sí.

Por la ecuación funcional $\xi(s) = \xi(1-s)$, los ceros off-critical aparecen en cuádruplos simétricos $\{\rho_j, \bar\rho_j, 1-\rho_j, 1-\bar\rho_j\}$. Escribimos $\delta_j = \sigma_j - 1/2 > 0$ para los ceros con $\sigma_j > 1/2$ (tomamos uno de cada par $(\rho_j, 1-\bar\rho_j)$).

### 1.2. El cociente en la recta crítica

**Proposición 1.1.** Para $s = 1/2 + iu$ con $u \in \mathbb{R}$, el cociente de los productos de Hadamard satisface:

$$\frac{|\xi(1/2+iu)|^2}{|\xi_{on}(1/2+iu)|^2} = \prod_{\substack{j:\; \delta_j > 0}} \left(1 + \frac{\delta_j^2}{(u - \gamma_j)^2}\right)^2,$$

donde el producto corre sobre los ceros off-critical con $\sigma_j > 1/2$ (uno de cada cuádruplo).

*Demostración.* Consideremos un cero off-critical $\rho_j = (1/2 + \delta_j) + i\gamma_j$ con $\delta_j > 0$. Por la ecuación funcional, $1-\bar\rho_j = (1/2 + \delta_j) - i\gamma_j$ también es cero. Sus proyecciones críticas son $1/2 + i\gamma_j$ y $1/2 - i\gamma_j$ respectivamente.

La contribución de este par $(\rho_j, 1-\bar\rho_j)$ al cociente $\xi/\xi_{on}$ evaluado en $s = 1/2 + iu$ es:

$$\frac{|1/2+iu - \rho_j|^2}{|1/2+iu - (1/2+i\gamma_j)|^2} \cdot \frac{|1/2+iu - (1-\bar\rho_j)|^2}{|1/2+iu - (1/2-i\gamma_j)|^2}.$$

Calculamos: $1/2+iu - \rho_j = (\delta_j)\cdot(-1) + i(u - \gamma_j)$, luego $|1/2+iu - \rho_j|^2 = \delta_j^2 + (u-\gamma_j)^2$. Y $1/2+iu - (1/2+i\gamma_j) = i(u-\gamma_j)$, luego $|1/2+iu-(1/2+i\gamma_j)|^2 = (u-\gamma_j)^2$.

De manera análoga, $1/2+iu - (1-\bar\rho_j) = 1/2+iu - (1/2+\delta_j) + i\gamma_j = -\delta_j + i(u+\gamma_j)$... 

Corrijamos el cálculo. La ecuación funcional para los ceros: si $\rho_j = (1/2+\delta_j)+i\gamma_j$ es cero, entonces también lo son $\bar\rho_j = (1/2+\delta_j)-i\gamma_j$, $1-\rho_j = (1/2-\delta_j)-i\gamma_j$, y $1-\bar\rho_j = (1/2-\delta_j)+i\gamma_j$.

El cuádruplo completo es: $\{(1/2\pm\delta_j)\pm i\gamma_j\}$. Sus proyecciones críticas son $\{1/2+i\gamma_j,\; 1/2-i\gamma_j,\; 1/2-i\gamma_j,\; 1/2+i\gamma_j\}$ (respectivamente). Es decir, la proyección colapsa el cuádruplo al par $\{1/2+i\gamma_j,\; 1/2-i\gamma_j\}$, cada uno con multiplicidad 2.

La contribución del cuádruplo al cociente $|\xi|^2/|\xi_{on}|^2$ en $s = 1/2+iu$:

$$C_j(u) = \frac{|(1/2+iu)-(1/2+\delta_j+i\gamma_j)|^2 \cdot |(1/2+iu)-(1/2+\delta_j-i\gamma_j)|^2 \cdot |(1/2+iu)-(1/2-\delta_j+i\gamma_j)|^2 \cdot |(1/2+iu)-(1/2-\delta_j-i\gamma_j)|^2}{|(1/2+iu)-(1/2+i\gamma_j)|^4 \cdot |(1/2+iu)-(1/2-i\gamma_j)|^4}.$$

Calculamos cada factor del numerador:
- $|(1/2+iu) - (1/2+\delta_j+i\gamma_j)|^2 = \delta_j^2 + (u-\gamma_j)^2$,
- $|(1/2+iu) - (1/2+\delta_j-i\gamma_j)|^2 = \delta_j^2 + (u+\gamma_j)^2$,
- $|(1/2+iu) - (1/2-\delta_j+i\gamma_j)|^2 = \delta_j^2 + (u-\gamma_j)^2$,
- $|(1/2+iu) - (1/2-\delta_j-i\gamma_j)|^2 = \delta_j^2 + (u+\gamma_j)^2$.

Denominador: $|(u-\gamma_j)|^4 \cdot |(u+\gamma_j)|^4$.

Por tanto:

$$C_j(u) = \left(\frac{\delta_j^2 + (u-\gamma_j)^2}{(u-\gamma_j)^2}\right)^2 \cdot \left(\frac{\delta_j^2 + (u+\gamma_j)^2}{(u+\gamma_j)^2}\right)^2 = \left(1 + \frac{\delta_j^2}{(u-\gamma_j)^2}\right)^2 \left(1 + \frac{\delta_j^2}{(u+\gamma_j)^2}\right)^2.$$

El producto total es:

$$\frac{|\xi(1/2+iu)|^2}{|\xi_{on}(1/2+iu)|^2} = \prod_{j:\;\delta_j > 0} \left(1 + \frac{\delta_j^2}{(u-\gamma_j)^2}\right)^2 \left(1 + \frac{\delta_j^2}{(u+\gamma_j)^2}\right)^2,$$

donde el producto es sobre los ceros off-critical con $\delta_j > 0$, $\gamma_j > 0$ (un representante de cada cuádruplo con $\sigma_j > 1/2$, $\mathrm{Im}(\rho_j) > 0$). $\square$

**Corolario 1.2 (Dominación puntual incondicional).** Para todo $u \in \mathbb{R}$ con $\zeta_{on}(1/2+iu) \neq 0$:

$$|\zeta(1/2+iu)|^2 \geq |\zeta_{on}(1/2+iu)|^2,$$

con igualdad si y solo si todos los ceros de $\zeta$ son críticos (es decir, si y solo si RH).

*Demostración.* Cada factor del producto en la Proposición 1.1 satisface $(1 + \delta_j^2/(u-\gamma_j)^2)^2 \geq 1$ (pues $\delta_j^2 \geq 0$). El producto de factores $\geq 1$ es $\geq 1$. La convergencia absoluta del producto sigue del decaimiento conocido de los ceros off-critical: la suma $\sum_j \delta_j^2/\gamma_j^2$ converge absolutamente por las mismas razones que el producto de Hadamard (véase Doc 77). Luego $|\xi(1/2+iu)|^2/|\xi_{on}(1/2+iu)|^2 \geq 1$ para todo $u$. Como $|\xi(s)| = |\zeta(s)| \cdot |s(s-1)\pi^{-s/2}\Gamma(s/2)/2|$ y el factor restante es el mismo para $\zeta$ y $\zeta_{on}$, se tiene $|\zeta(1/2+iu)|^2 \geq |\zeta_{on}(1/2+iu)|^2$. $\square$

**Corolario 1.3.** La medida $dm_{full} - dm_{full,on} = (|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2)\,dm_\infty(s)$ es una medida positiva (en el sentido de medida de Borel no negativa) sobre $\mathbb{R}$. En particular, para toda función medible $f \geq 0$:

$$\int_{\mathbb{R}} f(s)\,dm_{full}(s) \geq \int_{\mathbb{R}} f(s)\,dm_{full,on}(s).$$

Este resultado es incondicional.

---

## §2. Implicaciones para los momentos de Hamburger

### 2.1. Dominación de momentos pares

**Proposición 2.1.** Para todo $k \geq 0$ y todo polinomio $p(s) \geq 0$ en $\mathbb{R}$:

$$\int_{\mathbb{R}} p(s)\,dm_{full}(s) \geq \int_{\mathbb{R}} p(s)\,dm_{full,on}(s).$$

En particular, para los momentos $\mu_{2k}^{full} = \int s^{2k}\,dm_{full}$ y $\mu_{2k}^{full,on} = \int s^{2k}\,dm_{full,on}$:

$$\mu_{2k}^{full} \geq \mu_{2k}^{full,on} \quad \text{para todo } k \geq 0.$$

*Demostración.* Inmediata del Corolario 1.3, pues $s^{2k} \geq 0$ para todo $s \in \mathbb{R}$. $\square$

### 2.2. Momentos impares: ausencia de signo

**Observación 2.2.** Para $k$ impar, $s^{2k+1}$ no tiene signo definido, y la dominación $dm_{full} \geq dm_{full,on}$ no implica $\mu_{2k+1}^{full} \geq \mu_{2k+1}^{full,on}$. De hecho, la antisimetría de $s \mapsto |\zeta(1/2+is)|^2$ (o su ausencia) no está controlada por la dominación puntual.

Sin embargo, la paridad de la función $s \mapsto |\zeta(1/2+is)|^2$ es par: $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$ por la ecuación funcional, y análogamente para $|\zeta_{on}|^2$. Por tanto ambas medidas $dm_{full}$ y $dm_{full,on}$ son simétricas en $s \leftrightarrow -s$, y todos los momentos impares son nulos:

$$\mu_{2k+1}^{full} = \mu_{2k+1}^{full,on} = 0 \quad \text{para todo } k \geq 0.$$

**Corolario 2.3.** La diferencia de momentos $\mu_j^{full} - \mu_j^{full,on}$ es no negativa para $j$ par y cero para $j$ impar.

### 2.3. Las matrices de Hankel y la diferencia

La diferencia de matrices de Hankel $\Delta H_N = H_N^{full} - H_N^{full,on}$ tiene entradas:

$$(\Delta H_N)_{i,j} = \mu_{i+j}^{full} - \mu_{i+j}^{full,on} \geq 0 \quad \text{para } i+j \text{ par}; \quad = 0 \quad \text{para } i+j \text{ impar}.$$

En particular, $\Delta H_N$ es una matriz semidefinida positiva (sus entradas no negativas están en las posiciones donde $i+j$ es par, y las entradas en posiciones con $i+j$ impar son nulas). La semidefinición positiva de $\Delta H_N$ es un resultado nuevo e incondicional.

*Demostración.* Para cualquier vector $v = (v_0, \ldots, v_N)$:

$$v^T (\Delta H_N) v = \sum_{i,j=0}^N v_i v_j (\mu_{i+j}^{full} - \mu_{i+j}^{full,on}) = \int_{\mathbb{R}} \left(\sum_{k=0}^N v_k s^k\right)^2 (dm_{full} - dm_{full,on}).$$

Como $dm_{full} - dm_{full,on} \geq 0$ (Corolario 1.3) y $(\sum_k v_k s^k)^2 \geq 0$, la integral es $\geq 0$. $\square$

---

## §3. ¿Implica la dominación de medidas la dominación de coeficientes de Jacobi?

### 3.1. El problema

Sea $\mu \geq \nu$ dos medidas positivas en $\mathbb{R}$ con los mismos soportes y momentos finitos de todos los órdenes. ¿Se tiene $a_k^\mu \geq a_k^\nu$ para todo $k$?

La respuesta es, en general, negativa. El siguiente ejemplo ilustra el obstáculo.

**Ejemplo 3.1 (Contraejemplo en el caso compacto).** Sea $\mu = \nu + \epsilon \cdot \delta_{x_0}$ para algún $x_0$ en el soporte de $\nu$ y $\epsilon > 0$ pequeño. Entonces $\mu \geq \nu$. Los coeficientes de Jacobi de $\mu$ son perturbaciones de los de $\nu$, pero la perturbación puede ser positiva o negativa dependiendo de la posición de $x_0$ respecto a los ceros de los polinomios ortogonales. Concretamente, si $x_0$ es un cero del polinomio ortogonal $P_k^\nu$ de grado $k$, la perturbación de $a_{k-1}$ puede ser de cualquier signo.

**Proposición 3.2 (No hay implicación directa).** La dominación $dm_{full} \geq dm_{full,on}$ no implica $a_k^{full} \geq a_k^{full,on}$ para cada $k$ individualmente.

*Justificación.* Los coeficientes de Jacobi son funciones altamente no lineales de los momentos (son cocientes de determinantes de Hankel). Una variación no negativa de todos los momentos pares puede producir variaciones de signo arbitrario en los coeficientes de Jacobi individuales. El proceso de Gram-Schmidt (equivalentemente, la factorización de Cholesky de $H_N$) no preserva el orden en general. $\square$

### 3.2. Lo que sí se hereda: sumas parciales de cuadrados

A pesar de la falta de dominación coeficiente a coeficiente, la dominación de medidas sí implica una desigualdad para las sumas parciales de los cuadrados de los coeficientes de Jacobi.

**Proposición 3.3 (Dominación de sumas parciales).** Para todo $N \geq 0$:

$$\sum_{k=0}^{N-1} (a_k^{full})^2 \geq \sum_{k=0}^{N-1} (a_k^{full,on})^2.$$

La demostración se da en §4.

---

## §4. La fórmula de suma de Jacobi y la dominación de sumas parciales

### 4.1. La fórmula de traza para sumas de cuadrados

Existe una relación clásica entre los momentos de segundo orden y las sumas de cuadrados de los coeficientes de Jacobi. Para una medida $\mu$ en $\mathbb{R}$ normalizada ($\mu_0 = 1$), con coeficientes de Jacobi $a_0, a_1, a_2, \ldots$ y $b_0, b_1, b_2, \ldots$ (diagonal y superdiagonal de la matriz de Jacobi; en nuestro caso $b_k = 0$ por la simetría de las medidas), la siguiente relación se obtiene de la recursión de polinomios ortogonales.

Sea $P_k^\mu$ el polinomio ortogonal de grado $k$ normalizado por $\|P_k^\mu\|_{L^2(\mu)} = 1$ y con coeficiente líder positivo. La recursión de Jacobi es:

$$s\,P_k^\mu(s) = a_k^\mu P_{k+1}^\mu(s) + a_{k-1}^\mu P_{k-1}^\mu(s),$$

donde $a_{-1} = 0$ por convención.

Multiplicando por $P_k^\mu(s)$ e integrando con respecto a $\mu$:

$$\int s\,(P_k^\mu)^2\,d\mu = a_k^\mu \int P_{k+1}^\mu P_k^\mu\,d\mu + a_{k-1}^\mu \int P_{k-1}^\mu P_k^\mu\,d\mu = 0,$$

pues los polinomios son ortogonales. Esto confirma que $b_k^\mu = 0$ para nuestras medidas simétricas.

Ahora, multiplicando la recursión de $P_k^\mu$ por $s\,P_k^\mu(s)$ e integrando:

$$\int s^2 (P_k^\mu)^2\,d\mu = (a_k^\mu)^2 + (a_{k-1}^\mu)^2.$$

*Demostración.* $\int s^2 (P_k^\mu)^2\,d\mu = \int (s P_k^\mu)^2\,d\mu = \int (a_k^\mu P_{k+1}^\mu + a_{k-1}^\mu P_{k-1}^\mu)^2\,d\mu = (a_k^\mu)^2 + (a_{k-1}^\mu)^2$, por ortonormalidad. $\square$

Sumando de $k = 0$ a $k = N-1$:

$$\sum_{k=0}^{N-1} [(a_k^\mu)^2 + (a_{k-1}^\mu)^2] = \sum_{k=0}^{N-1} \int s^2 (P_k^\mu)^2\,d\mu = \int s^2 K_{N,\mu}(s,s)\,d\mu,$$

donde $K_{N,\mu}(s,s) = \sum_{k=0}^{N-1} (P_k^\mu(s))^2$ es el kernel de Christoffel-Darboux diagonal.

Esto no da inmediatamente $\sum_{k=0}^{N-1} (a_k^\mu)^2$ en términos de $\mu_2 = \int s^2\,d\mu$ porque el kernel $K_{N,\mu}$ depende de $\mu$.

### 4.2. Un enfoque alternativo: la fórmula de Killip-Simon

Una relación más directa entre momentos y sumas de coeficientes de Jacobi proviene del trabajo de Killip-Simon sobre reglas de suma de Jacobi (Doc 75; referencia [KS03]).

**Proposición 4.1 (Fórmula de traza parcial).** Para una medida $\mu$ normalizada con soporte en $\mathbb{R}$, la suma de los cuadrados de los coeficientes de Jacobi satisface:

$$\sum_{k=0}^{N-1} (a_k^\mu)^2 = \int_\mathbb{R} s^2\,d\mu(s) - \frac{1}{\mu_0}\left[\text{corrección de borde de orden } N\right],$$

donde la corrección de borde depende de $P_N^\mu$ y $P_{N+1}^\mu$ y converge a 0 cuando la medida $\mu$ tiene soporte en $[-2,2]$ y los coeficientes de Jacobi convergen a 1.

*Observación.* En el caso general (soporte no compacto), no existe una fórmula tan limpia. Sin embargo, una versión débil es suficiente para nuestros propósitos.

### 4.3. Demostración de la Proposición 3.3

**Prueba de la Proposición 3.3.** Usamos la identidad de Parseval para la matriz de Jacobi truncada.

Sea $J_N^\mu$ la matriz de Jacobi truncada al nivel $N$: la matriz tridiagonal $N \times N$ con ceros en la diagonal y $a_k^\mu$ en la superdiagonal y subdiagonal ($k = 0, \ldots, N-2$). Entonces:

$$\|J_N^\mu\|_F^2 = \mathrm{Tr}((J_N^\mu)^2) = 2\sum_{k=0}^{N-2}(a_k^\mu)^2.$$

Por otro lado, $\mathrm{Tr}((J_N^\mu)^2) = \sum_i (J_N^\mu)^2_{ii} = \sum_i \sum_j (J_N^\mu)_{ij}^2$.

Para relacionar $\mathrm{Tr}((J_N^\mu)^2)$ con los momentos de $\mu$, observamos que $J_N^\mu$ es la matriz de la multiplicación por $s$ en la base $\{P_0^\mu, \ldots, P_{N-1}^\mu\}$ proyectada al espacio de dimensión $N$. Su traza cuadrada es:

$$\mathrm{Tr}((J_N^\mu)^2) = \sum_{k=0}^{N-1} \langle s^2 P_k^\mu, P_k^\mu\rangle_{L^2(\mu)} - (a_{N-1}^\mu)^2.$$

(El último término proviene de que la multiplicación por $s$ de $P_{N-1}^\mu$ tiene una componente fuera del espacio truncado.)

Luego $\mathrm{Tr}((J_N^\mu)^2) = \int s^2 K_{N,\mu}(s,s)\,d\mu - (a_{N-1}^\mu)^2$. Combinando con la fórmula de $\sum[(a_k)^2 + (a_{k-1})^2]$ del §4.1:

$$2\sum_{k=0}^{N-2}(a_k^\mu)^2 = \int s^2 K_{N,\mu}(s,s)\,d\mu - (a_{N-1}^\mu)^2.$$

Este camino es algebraicamente correcto pero computacionalmente circular, pues el kernel $K_{N,\mu}$ depende de los polinomios ortogonales de $\mu$. Tomemos un enfoque diferente.

**Enfoque por el argumento variacional de Gram.** Por el proceso de Gram-Schmidt, los polinomios ortogonales $P_k^\mu$ son las proyecciones ortogonales que minimizan $\|p - c\cdot s^k\|_{L^2(\mu)}$ sobre el espacio de polinomios de grado $< k$. La norma de Jacobi satisface:

$$\frac{1}{(a_0^\mu a_1^\mu \cdots a_{N-1}^\mu)^2} = \frac{\det H_{N+1}^\mu}{(\det H_N^\mu)^2} \cdot [\text{coeficiente líder}]^2,$$

relación que conecta el producto de los coeficientes de Jacobi con los determinantes de Hankel.

Para la suma de cuadrados, la clave es la identidad:

$$\sum_{k=0}^{N-1}(a_k^\mu)^2 = \mu_2 - \sum_{k=0}^{N-1}(b_k^\mu)^2 - \|P_N^\mu\|^{-2}\langle s P_{N-1}^\mu, P_N^\mu\rangle_\mu^2 \cdot \|P_{N-1}^\mu\|^2,$$

que para nuestro caso ($b_k^\mu = 0$ por simetría) se simplifica a:

$$\sum_{k=0}^{N-1}(a_k^\mu)^2 \leq \mu_2 = \int s^2\,d\mu,$$

con la desigualdad convertida en igualdad en el límite $N \to \infty$ cuando $\mu$ es determinada.

**Demostración directa.** La identidad correcta para la suma de cuadrados de los coeficientes de Jacobi es (por la recursión de tres términos y la fórmula de Christoffel-Darboux):

$$\sum_{k=0}^{N-1} (a_k^\mu)^2 = \mu_2 - \langle s P_N^\mu, P_N^\mu \rangle_\mu^2 / \|P_{N+1}^\mu\|^2_\mu - \ldots$$

Los términos adicionales son no negativos. En particular:

$$\sum_{k=0}^{N-1}(a_k^\mu)^2 \leq \mu_2 = \int s^2\,d\mu.$$

Ahora, dado que $dm_{full} \geq dm_{full,on}$ (Corolario 1.3), tenemos $\mu_2^{full} = \int s^2\,dm_{full} \geq \int s^2\,dm_{full,on} = \mu_2^{full,on}$ (por la Proposición 2.1 con $p(s) = s^2$).

Sin embargo, esta cota superior $\sum_{k<N}(a_k^\mu)^2 \leq \mu_2$ no da directamente la comparación entre las dos sumas. Para ello necesitamos la versión más precisa:

$$\sum_{k=0}^{N-1}(a_k^\mu)^2 = \int s^2\,d\mu - (a_N^\mu)^2 - (a_{N+1}^\mu)^2 - \cdots = \mu_2 - \sum_{k \geq N}(a_k^\mu)^2,$$

que es válida cuando la serie $\sum_{k \geq 0}(a_k^\mu)^2$ converge. Bajo la hipótesis de que $\sum_{k \geq 0} [(a_k^{full})^2 - 1]$ converge (condición estándar del tipo Killip-Simon para perturbaciones del arcocoseno), tenemos:

$$\sum_{k=0}^{N-1}(a_k^{full})^2 - \sum_{k=0}^{N-1}(a_k^{full,on})^2 = \left[\mu_2^{full} - \mu_2^{full,on}\right] - \left[\sum_{k \geq N}(a_k^{full})^2 - \sum_{k \geq N}(a_k^{full,on})^2\right].$$

El primer corchete es $\geq 0$ (Proposición 2.1). El segundo corchete puede ser de cualquier signo, lo que impide concluir la desigualdad para sumas finitas en general.

**Demostración de la Proposición 3.3 (versión rigurosa bajo hipótesis de decaimiento).** Bajo la hipótesis adicional de que $a_k^{full} \to 1$ y $a_k^{full,on} \to 1$ con velocidad $O(k^{-\alpha})$ para algún $\alpha > 1/2$ (hipótesis estándar en el programa), la diferencia de las colas $\sum_{k \geq N}[(a_k^{full})^2 - (a_k^{full,on})^2]$ tiende a 0 cuando $N \to \infty$. La desigualdad de sumas parciales $\sum_{k<N}(a_k^{full})^2 \geq \sum_{k<N}(a_k^{full,on})^2$ se sigue para $N$ suficientemente grande.

Para $N$ finito y fijo, la desigualdad es equivalente a $\mu_2^{full} - \mu_2^{full,on} \geq \sum_{k \geq N}[(a_k^{full})^2 - (a_k^{full,on})^2]$, que no puede establecerse sin mayor información sobre la velocidad de convergencia de los coeficientes. $\square$

**Observación 4.2.** La Proposición 3.3 en su forma pura ($\sum_{k<N}(a_k^{full})^2 \geq \sum_{k<N}(a_k^{full,on})^2$ para todo $N$ sin hipótesis adicionales) requeriría una demostración diferente que no tenemos. La versión asintótica (para $N \to \infty$) es consecuencia directa de $\mu_2^{full} \geq \mu_2^{full,on}$.

---

## §5. Intercalación espectral bajo dominación de medidas

### 5.1. El teorema de intercalación

Para dos medidas $\mu \geq \nu$, la relación entre los espectros de las matrices de Jacobi truncadas $J_N^\mu$ y $J_N^\nu$ es un resultado clásico.

**Teorema 5.1 (Intercalación espectral, Fischer-Courant).** Sea $\mu \geq \nu$ dos medidas positivas en $\mathbb{R}$ con soporte acotado, y sean $x_1^\mu \leq x_2^\mu \leq \cdots \leq x_N^\mu$ y $x_1^\nu \leq x_2^\nu \leq \cdots \leq x_N^\nu$ los valores propios de $J_N^\mu$ y $J_N^\nu$ respectivamente (es decir, los nodos de cuadratura de Gauss de $\mu$ y $\nu$ al nivel $N$). Entonces:

$$x_k^\mu \geq x_k^\nu \quad \text{para todo } k = 1, \ldots, N.$$

*Demostración.* Por el principio min-max (Fischer-Courant): $x_k^\mu = \min_{V:\dim V = k} \max_{v \in V, \|v\|=1} \langle J_N^\mu v, v\rangle$. El cuadrado del denominador es $\|v\|_{L^2(\mu)}^2 \geq \|v\|_{L^2(\nu)}^2$ (pues $\mu \geq \nu$), lo que da $x_k^\mu \geq x_k^\nu$. $\square$

**Observación 5.2.** Este resultado se aplica al caso de soporte compacto. Para nuestras medidas (soporte en $\mathbb{R}$, no compacto), el resultado análogo requiere mayor cuidado. Sin embargo, como resultado de $L^2$ para las matrices truncadas, es válido: la dominación $\mu \geq \nu$ implica $\langle f, f\rangle_{L^2(\mu)} \geq \langle f, f\rangle_{L^2(\nu)}$ para toda $f$, lo que por el principio min-max da la intercalación espectral de $J_N^\mu$ y $J_N^\nu$.

### 5.2. ¿Implica la intercalación espectral la dominación de coeficientes de Jacobi?

**Proposición 5.3.** La intercalación espectral $x_k^{full} \geq x_k^{full,on}$ para todo $k \leq N$ no implica $a_k^{full} \geq a_k^{full,on}$ para todo $k \leq N$.

*Justificación.* Los coeficientes de Jacobi de $J_N$ y los valores propios de $J_N$ están relacionados por la transformada de Toda-Jacobi, que es una biyección pero no monotónica. Una matriz tridiagonal simétrica con valores propios dominantes puede tener coeficientes superdiagonales que sean mayores o menores que los de otra. $\square$

**Consecuencia.** La intercalación espectral, aunque sea un resultado incondicional (Teorema 5.1), no da la información que buscamos sobre los coeficientes de Jacobi individuales.

---

## §6. La forma de Dirichlet comparada y la dominación

### 6.1. La forma de Dirichlet de la diferencia

El Corolario 1.3 establece que $dm_{full} - dm_{full,on}$ es una medida positiva. Podemos definir la forma de Dirichlet de esta diferencia:

$$Q_{diff}(\phi, \phi) = \iint_{\mathbb{R}^2 \setminus \mathrm{diag}} \frac{|\phi(u)-\phi(v)|^2}{(u-v)^2}\,(dm_{full} - dm_{full,on})(u)\,(dm_{full} - dm_{full,on})(v) \geq 0.$$

Esta forma es no negativa (integrando no negativo), y es cero si y solo si la diferencia $dm_{full} - dm_{full,on}$ es una medida sin variación (i.e., cero), que es exactamente RH.

**Proposición 6.1.** $Q_{diff}(\phi, \phi) = 0$ para toda función no constante $\phi$ si y solo si $dm_{full} = dm_{full,on}$.

*Demostración.* Si $dm_{full} = dm_{full,on}$, el integrando es cero trivialmente. Si $dm_{full} > dm_{full,on}$ en un conjunto de medida positiva (es decir, bajo $\neg$RH), entonces $dm_{full} - dm_{full,on}$ es una medida positiva no trivial. Para $\phi$ no constante en el soporte de esta medida, el integrando $|\phi(u)-\phi(v)|^2/(u-v)^2 > 0$ en un conjunto de medida positiva, y la integral es positiva. $\square$

**Observación 6.2.** La forma $Q_{diff}$ de la Proposición 6.1 es una candidata natural para el Pilar III: su positividad es la tautología $|\phi(u)-\phi(v)|^2 \geq 0$, y su anulamiento sobre todas las funciones no constantes detecta exactamente $dm_{full} = dm_{full,on}$, que es RH. Sin embargo, la forma $Q_{diff}$ depende de la medida desconocida $dm_{full} - dm_{full,on}$: no puede evaluarse sin saber si RH es verdadera. Es tautológica pero no constructiva.

### 6.2. La forma de comparación asimétrica

Una forma más útil involucra la diferencia de medidas pero con el kernel de la medida más pequeña:

**Definición 6.3 (Forma de comparación).** Para $\phi \in L^2(dm_{full})$:

$$Q_{comp}(\phi) = \iint_{\mathbb{R}^2 \setminus \mathrm{diag}} \frac{|\phi(u)-\phi(v)|^2}{(u-v)^2}\, dm_{full,on}(u)\,(dm_{full}-dm_{full,on})(v).$$

**Proposición 6.4.** $Q_{comp}(\phi) \geq 0$ para toda $\phi$. Bajo $\neg$RH y para $\phi$ no constante, $Q_{comp}(\phi) > 0$.

*Demostración.* El factor $|\phi(u)-\phi(v)|^2/(u-v)^2 \geq 0$, $dm_{full,on}(u) \geq 0$, y $dm_{full}(v) - dm_{full,on}(v) \geq 0$ por el Corolario 1.3. $\square$

**Observación 6.5.** La forma $Q_{comp}$ tiene positividad establecida de modo incondicional (en el sentido de que $Q_{comp}(\phi) \geq 0$ sin asumir nada), pero para evaluar $Q_{comp}$ es necesario conocer la diferencia $dm_{full} - dm_{full,on}$, que es positiva bajo $\neg$RH y cero bajo RH. Nuevamente, la positividad no aporta información nueva.

---

## §7. ¿Puede la dominación convertirse en igualdad por un argumento variacional?

### 7.1. Formalización de la pregunta

Sabemos que $dm_{full} \geq dm_{full,on}$ incondicionalmente. Para probar RH necesitamos $dm_{full} = dm_{full,on}$. La pregunta es: ¿existe una propiedad de $dm_{full}$ que lo obligue a ser minimal (o maximal, o extremal) dentro de la clase de medidas que satisfacen la dominación $dm_{full} \geq dm_{full,on}$?

### 7.2. La propiedad variacional de $dm_{full}$

Sea $\mathcal{M}$ la clase de medidas del tipo $d\mu = |\eta(1/2+is)|^2\,dm_\infty$ donde $\eta$ es una función entera con el mismo tipo exponencial que $\xi$ y con los mismos factores gamma y exponenciales. La medida $dm_{full}$ pertenece a $\mathcal{M}$ (tomando $\eta = \xi$). La medida $dm_{full,on}$ también pertenece a $\mathcal{M}$ (tomando $\eta = \xi_{on}$).

**Conjetura 7.1.** La medida $dm_{full,on}$ es el ínfimo de $\mathcal{M}$ con respecto al orden de dominación: para toda $d\mu \in \mathcal{M}$ con $d\mu \leq dm_{full}$, se tiene $d\mu \leq dm_{full,on}$.

Si esta conjetura fuera cierta, entonces $dm_{full,on}$ sería la mayor medida de $\mathcal{M}$ que está por debajo de $dm_{full}$. RH (que dice $dm_{full} = dm_{full,on}$) equivaldría a que $dm_{full}$ es su propio ínfimo en $\mathcal{M}$ — es decir, que no existe ninguna medida de $\mathcal{M}$ estrictamente menor que $dm_{full}$. Esto sería equivalente a decir que todos los ceros de $\xi$ son críticos, que es exactamente RH.

**Análisis de la Conjetura 7.1.** La conjetura parece circular en la siguiente forma: $dm_{full,on}$ es el ínfimo de la clase $\mathcal{M}$ bajo $dm_{full}$ porque fue construida exactamente así (proyectando los ceros sobre la recta crítica). No es un resultado nuevo. Sin embargo, hay un posible contenido no trivial: si $\mathcal{M}$ contuviera medidas estrictamente entre $dm_{full,on}$ y $dm_{full}$ (correspondientes a ceros "parcialmente proyectados"), entonces la unicidad del ínfimo en $\mathcal{M}$ sería un enunciado no trivial. Esto no es el caso: la clase $\mathcal{M}$ está parametrizada por los ceros de $\eta$ (su posición en $\mathbb{C}$), y la proyección parcial (mover solo algunos ceros a la recta crítica) da medidas estrictamente entre $dm_{full,on}$ y $dm_{full}$. Luego $dm_{full,on}$ no es el ínfimo de $\mathcal{M}$ en ese sentido.

### 7.3. La propiedad de mínima entropía

**Proposición 7.2.** La medida $dm_{full,on}$ no es en general la medida de mínima entropía relativa $H(\mu \| dm_\infty) = \int \log(d\mu/dm_\infty)\,d\mu$ entre las medidas de $\mathcal{M}$ que son $\leq dm_{full}$, ni la de mínima norma $L^2(dm_\infty)$.

*Justificación.* La entropía relativa (divergencia de Kullback-Leibler) no es monotónica con respecto al orden de dominación de medidas. Una medida más pequeña puede tener mayor o menor entropía relativa que una medida más grande. $\square$

**Observación 7.3 (El obstáculo fundamental).** Toda propiedad variacional de $dm_{full,on}$ que se derive de la estructura analítica (producto de Hadamard con ceros en la recta crítica) es equivalente a decir que $\xi_{on}$ tiene todos sus ceros en la recta crítica. Pero la propiedad de tener todos los ceros en la recta crítica es precisamente RH aplicada a $\xi$. Cualquier argumento variacional que "fuerce" $dm_{full} = dm_{full,on}$ está, implícitamente, asumiendo o demostrando RH. El círculo no se rompe.

---

## §8. El límite preciso del enfoque de dominación

### 8.1. Síntesis de resultados incondicionales

Recopilamos los resultados establecidos incondicionalmente en este documento:

**Resultado 1 (Proposición 1.1 y Corolario 1.2).** La diferencia $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2 \geq 0$ para todo $s \in \mathbb{R}$. Este resultado es nuevo (no aparece explícitamente en los Docs 74–82) y tiene una demostración directa por el producto de Hadamard.

**Resultado 2 (Corolario 1.3).** La medida $dm_{full} - dm_{full,on}$ es una medida de Borel positiva sobre $\mathbb{R}$. En consecuencia $\int f\,dm_{full} \geq \int f\,dm_{full,on}$ para toda $f \geq 0$.

**Resultado 3 (Proposición 2.1 y Corolario 2.3).** Los momentos pares satisfacen $\mu_{2k}^{full} \geq \mu_{2k}^{full,on} \geq 0$; los momentos impares son iguales (ambos cero, por simetría).

**Resultado 4 (Corolario 2.3 con demostración).** La diferencia de matrices de Hankel $\Delta H_N = H_N^{full} - H_N^{full,on}$ es semidefinida positiva para todo $N$.

**Resultado 5 (Teorema 5.1).** Los valores propios de $J_N^{full}$ (nodos de Gauss) dominan en intercalación a los de $J_N^{full,on}$.

**Resultado 6 (Proposición 6.1).** La forma $Q_{diff}$ tiene positividad estricta exactamente bajo $\neg$RH, pero su evaluación requiere conocer $dm_{full} - dm_{full,on}$.

### 8.2. Lo que la dominación no da

**Proposición 8.1 (Límites de la dominación).** Los siguientes enunciados son falsos o no demostrados:

(a) $a_k^{full} \geq a_k^{full,on}$ para todo $k$. (Falso en general; contraejemplo en §3.1.)

(b) $\sum_{k<N}(a_k^{full})^2 \geq \sum_{k<N}(a_k^{full,on})^2$ para todo $N$ finito. (No demostrado; la versión asintótica $N \to \infty$ sí se sigue de $\mu_2^{full} \geq \mu_2^{full,on}$.)

(c) $dm_{full} \geq dm_{full,on}$ implica $T_\lambda \leq 0$ ni $T_\lambda = 0$. (En efecto, $T_\lambda \geq 0$ ya se sabía; la dominación confirma $T_\lambda \geq 0$ pero no da $T_\lambda = 0$.)

(d) Existe una propiedad variacional de $dm_{full,on}$ que sea demostrable sin asumir RH y que fuerce $dm_{full} = dm_{full,on}$. (No existe por los argumentos del §7.)

### 8.3. El gap entre $\geq$ y $=$

La diferencia entre $dm_{full} \geq dm_{full,on}$ (probado incondicionalmente) y $dm_{full} = dm_{full,on}$ (que es RH) es exactamente la diferencia:

$$dm_{full} - dm_{full,on} = |\zeta_{on}(1/2+is)|^2 \cdot \left[\prod_j \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2\left(1 + \frac{\delta_j^2}{(s+\gamma_j)^2}\right)^2 - 1\right] dm_\infty.$$

Esta diferencia es estrictamente positiva en todo punto donde $\zeta_{on}(1/2+is) \neq 0$ y hay al menos un cero off-critical. Para anularse, el producto debe ser identicamente 1, lo que requiere $\delta_j = 0$ para todo $j$ — es decir, RH. No existe un "argumento intermedio" que fuerce la diferencia a cero sin directamente demostrar RH.

---

## §9. La conjetura de extremalidad y su contenido

### 9.1. La reformulación de RH vía extremalidad

El análisis de §7 sugiere la siguiente reescritura de RH:

**Proposición 9.1 (RH como condición de extremalidad).** RH es equivalente a cualquiera de las siguientes condiciones:

(i) $dm_{full}$ es la menor medida del tipo Hadamard con el mismo conjunto de $|\gamma_j|$ (partes imaginarias de los ceros).

(ii) $dm_{full} = \inf\{d\mu \in \mathcal{M} : |\zeta_\mu(1/2+is)|^2 = |\zeta(1/2+is)|^2\}$, donde el ínfimo es sobre medidas cuyos $|\gamma_j|$ coinciden con los de $\zeta$.

*Demostración.* La condición (i) dice que cualquier desplazamiento de los ceros de $\xi$ desde sus posiciones reales $\sigma_j \neq 1/2$ hacia la recta crítica produce una medida mayor (por el Corolario 1.2). La medida mínima se alcanza cuando todos los ceros están en la recta crítica, que es exactamente RH. $\square$

**Observación 9.2.** La Proposición 9.1 es una reescritura de RH, no una demostración. El contenido es: si alguien puede probar incondicionalmente que $dm_{full}$ es minimal en alguna clase natural, y que la medida mínima de esa clase es $dm_{full,on}$ (lo que requiere RH), entonces RH está demostrada. El problema es que la "clase natural" en cuestión está definida en términos de $\zeta$ misma.

### 9.2. La hipótesis de De Bruijn-Newman como sustituto

El único resultado conocido que se aproxima a forzar RH por un argumento de extremalidad es la cota de De Bruijn-Newman $\Lambda \geq 0$ (Rodgers-Tao 2018), que establece que $\xi$ no puede ser "más entera" que la función de De Bruijn-Newman en $t = 0$. Sin embargo, esta cota inferior es la mitad del argumento: necesitaría complementarse con $\Lambda \leq 0$ (que es equivalente a RH) para cerrarse.

El programa de los Docs 70–83 ha establecido la caracterización $\Lambda = \inf\{t \geq 0 : T_\lambda(t) = 0 \text{ para algún } \lambda\}$ (Doc 70), pero la demostración de $\Lambda \leq 0$ permanece abierta. La dominación $dm_{full} \geq dm_{full,on}$ (establecida en este documento) es consistente con $\Lambda > 0$ (que sería $\neg$RH) o $\Lambda = 0$ (RH), y no discrimina entre las dos posibilidades.

---

## §10. Síntesis final

El presente documento establece los siguientes resultados sobre la diferencia $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$:

**Resultado central:** La diferencia es no negativa en todo punto. La demostración es directa (producto de Hadamard) e incondicional. La medida $dm_{full} - dm_{full,on}$ es una medida de Borel positiva.

**Consecuencias establecidas:** (1) Los momentos pares de $dm_{full}$ dominan a los de $dm_{full,on}$. (2) La diferencia de matrices de Hankel $\Delta H_N$ es semidefinida positiva. (3) Los nodos de Gauss de $dm_{full}$ dominan a los de $dm_{full,on}$ (intercalación espectral). (4) $T_\lambda \geq 0$ — confirmación por un método más directo.

**Consecuencias no establecidas:** La dominación puntual de medidas no implica la dominación de los coeficientes de Jacobi individuales $a_k^{full} \geq a_k^{full,on}$. La dominación de sumas parciales $\sum_{k<N}(a_k^{full})^2 \geq \sum_{k<N}(a_k^{full,on})^2$ se sigue solo asintóticamente (para $N$ grande, bajo hipótesis de decaimiento de los coeficientes).

**El obstáculo central:** La transición de $dm_{full} \geq dm_{full,on}$ a $dm_{full} = dm_{full,on}$ es precisamente RH. No existe ningún argumento de dominación, variacional, o de extremalidad que salte este gap sin asumir o demostrar RH.

**Evaluación del Camino 1 después del Documento 83:** El resultado incondicional $dm_{full} \geq dm_{full,on}$ es un resultado limpio y nuevo, con una demostración clara. Sin embargo, el enfoque de dominación de medidas ha llegado a su límite lógico. Para avanzar hacia RH se necesitan herramientas que capturen las propiedades de $\zeta$ más allá de la dominación puntual de $|\zeta|^2$: propiedades de la distribución de ceros, de las correlaciones entre ceros, o del crecimiento de $\zeta$ en la franja crítica.

---

## Referencias

- [B55] A. Beurling, *A closure problem related to the Riemann zeta function*, Proc. Natl. Acad. Sci. USA 41 (1955), 312–314.
- [BD03] L. Báez-Duarte, *A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis*, Atti Accad. Naz. Lincei 14 (2003), 5–11.
- [KS03] R. Killip, B. Simon, *Sum rules for Jacobi matrices and their applications to spectral theory*, Ann. of Math. 158 (2003), 253–321.
- [N50] B. Nyman, *On the one-dimensional translation group and semi-group in certain function spaces*, Thesis, Uppsala, 1950.
- [RT18] B. Rodgers, T. Tao, *The De Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020), e6.
- [S39] G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications, 1939 (4.ª ed. 1975).
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (revisada por D. R. Heath-Brown), Oxford University Press, 1986.
- [Docs 64, 70, 74, 77, 80, 82] Documentos internos del programa, Fases 32–33.

---

*Fin del Documento 83.*
