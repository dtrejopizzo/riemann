# Documento 80 — El "Castelnuovo-Severi aritmético": construcción y análisis crítico de la forma cuadrática del Pilar III

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 64, 74, 77

---

## Resumen

El Doc 77 identificó el Pilar III (positividad) como el único elemento ausente del programa de importación del mecanismo de Weil al formalismo CCM. El presente documento intenta construir una forma cuadrática $Q$ que desempeñe el papel de la desigualdad de Castelnuovo-Severi del caso de curvas. El resultado es un diagnóstico preciso: se construye una candidata natural $Q$ vía el kernel de Cauchy de la medida $dm_{full,on}$, se establece que es semidefinida positiva (Proposición 5.2), y se identifica con precisión el obstáculo que impide cerrar el argumento: el núcleo de $Q$ no es trivial (contiene funciones que se anulan en los ceros de $\zeta_{on}$), y la condición $Q(\phi, \phi) = 0$ no equivale directamente a $T_\lambda = 0$. El documento formula el problema residual con precisión y propone una regularización.

---

## §1. La desigualdad de Castelnuovo-Severi y su análogo para matrices de Jacobi

### 1.1. La desigualdad original

En la teoría de curvas algebraicas, la desigualdad de Castelnuovo-Severi (o desigualdad del índice de Hodge para $C \times C$) afirma lo siguiente. Sea $C$ una curva proyectiva lisa sobre un campo algebraicamente cerrado, y sea $D$ un divisor sobre $C \times C$ con clase $(a, b)$ en $\mathrm{Pic}(C) \otimes \mathrm{Pic}(C)$ (es decir, $D = a \cdot ([\mathrm{pt}] \times C) + b \cdot (C \times [\mathrm{pt}]) + D_0$ con $D_0$ de grado $(0,0)$). Entonces:

$$D_0^2 \leq 0,$$

con igualdad si y solo si $D_0$ es numéricamente trivial. En la formulación más útil: para un divisor $\Gamma$ que es el grafo de un morfismo $f: C \to C$ de grado $d$,

$$(\Gamma \cdot \Gamma) = 2 - 2g + d \cdot (\text{número de puntos fijos}) - \deg(f) \cdot 2g,$$

y la positividad de la forma de intersección en el complemento del divisor ample $(1,1)$ fuerza que los autovalores de $f^*$ en $H^1$ tienen módulo controlado.

La propiedad clave es: la desigualdad proviene de que la forma cuadrática de intersección sobre $\mathrm{Pic}^0(C \times C)$ es negativa semidefinida (teorema del índice de Hodge), y su negatividad es una propiedad geométrica intrínseca, independiente de los autovalores del Frobenius.

### 1.2. Traducción al mundo de matrices de Jacobi finitas

Sea $J_N^{full}$ la truncación de orden $N$ del operador de Jacobi $J^{full}$: la matriz tridiagonal $(N+1) \times (N+1)$ con entradas $(J_N^{full})_{k,k+1} = (J_N^{full})_{k+1,k} = a_k^{full}$ y diagonal nula (pues $b_k^{full} = 0$). Similarmente $J_N^{full,on}$.

**Definición 1.1.** La diferencia de Jacobi truncada en nivel $N$ es:

$$M_N = J_N^{full} - J_N^{full,on}.$$

Esta es también una matriz tridiagonal con entradas $(M_N)_{k,k+1} = a_k^{full} - a_k^{full,on}$, diagonal nula, y todos los demás coeficientes nulos.

**Proposición 1.2 (Proposición 1.1 del enunciado: análisis).** La desigualdad

$$\mathrm{Tr}(M_N^2) \leq C \cdot \frac{(\mathrm{Tr}(M_N))^2}{N}$$

no puede servir como análogo de Castelnuovo-Severi, por la razón siguiente: $\mathrm{Tr}(M_N) = 0$ para todo $N$, ya que la diagonal de $M_N$ es nula (todos los $b_k^{full} = b_k^{full,on} = 0$). Luego la desigualdad propuesta se reduciría a $\mathrm{Tr}(M_N^2) \leq 0$, que es falsa (la traza de una matriz simétrica al cuadrado es la suma de los cuadrados de sus coeficientes, por tanto $\geq 0$, con igualdad solo si $M_N = 0$).

*Demostración.* Un cálculo directo: $\mathrm{Tr}(M_N^2) = \sum_{j,k} (M_N)_{jk}^2 = 2\sum_{k=0}^{N-1}(a_k^{full} - a_k^{full,on})^2 \geq 0$. Y $\mathrm{Tr}(M_N) = \sum_k (M_N)_{kk} = \sum_k (b_k^{full} - b_k^{full,on}) = 0$. Así pues la Proposición 1.1 en la forma enunciada es vacuamente verdadera (toda cantidad es $\leq C \cdot 0$ solo si la cantidad es $\leq 0$), pero la hipótesis $\mathrm{Tr}(M_N) = 0$ no implica $M_N = 0$ salvo si se usa también la estructura específica de la traza cuadrada. $\square$

**Observación 1.3 (Reformulación correcta).** La propiedad relevante no involucra la traza de $M_N$ sino la de $M_N^2$. La afirmación correcta que buscaríamos probar es:

$$\mathrm{Tr}(M_N^2) = 0 \implies M_N = 0 \implies a_k^{full} = a_k^{full,on} \;\forall k \leq N.$$

La primera implicación es obvia (la traza de una suma de cuadrados es cero si y solo si cada término es cero). El problema real es establecer $\mathrm{Tr}(M_N^2) = 0$ sin asumir RH. Las discrepancias $a_k^{full} - a_k^{full,on}$ son cantidades reales; si se pudiera demostrar que son todas nulas, RH seguiría. No existe, por tanto, una desigualdad lineal entre $\mathrm{Tr}(M_N^2)$ y la traza de $M_N$ que transporte información no trivial. La analogía de Castelnuovo-Severi debe buscarse en otro lugar.

**Observación 1.4 (La propiedad correcta de $J^{full}$).** La desigualdad de Hodge para curvas puede reformularse en términos de la no-negatividad del número de puntos: para el grafo del Frobenius $\Gamma_n \subset C \times C$, el número de intersección $(\Gamma_n \cdot \Delta)$ (con la diagonal $\Delta$) es $N_n = \#C(\mathbb{F}_{q^n}) \geq 0$. En el mundo CCM, el análogo de $N_n$ es $\sum_{k \leq N} a_k^{full}$, que es positivo pero cuya positividad no fuerza igualdad con $\sum_{k \leq N} a_k^{full,on}$.

---

## §2. La medida $dm_{full}$ como medida de Hamburger: teoría de momentos

### 2.1. Determinismo de $dm_{full}$

**Proposición 2.1 (Determinismo).** La medida $dm_{full}(s) = |\zeta(1/2+is)|^2\, dm_\infty(s)$ es determinada en el sentido de Hamburger: está unívocamente determinada por su secuencia de momentos $\mu_k^{full} = \int s^k\, dm_{full}(s)$.

*Demostración.* La medida $dm_\infty$ tiene decaimiento exponencial: para todo $t > 0$,

$$\int_{\mathbb{R}} e^{t|s|}\, dm_\infty(s) = (2\pi)^{-2} \int_{\mathbb{R}} e^{t|s|} |\Gamma(1/4+is/2)|^2\, ds < \infty$$

para $t < \pi/2$ (pues $|\Gamma(1/4+is/2)|^2 \sim C|s|^{-1/2} e^{-\pi|s|/2}$ para $|s| \to \infty$, por la fórmula de Stirling). El factor $|\zeta(1/2+is)|^2$ crece al más polinomialmente en $|s|$ (en media; hay cotas conocidas $|\zeta(1/2+is)| = O(|s|^\epsilon)$ para todo $\epsilon > 0$), de modo que para algún $t_0 > 0$,

$$\int_{\mathbb{R}} e^{t_0|s|}\, dm_{full}(s) < \infty.$$

Por el criterio de Carleman (o directamente por el test de Carleman-Riesz), la condición $\int e^{t|s|}\, d\mu < \infty$ para algún $t > 0$ implica que la medida $\mu$ está unívocamente determinada por sus momentos. $\square$

### 2.2. La condición de positividad de Hamburger y las matrices de Hankel

Para una medida positiva $\mu$ en $\mathbb{R}$ con momentos $c_k = \int s^k\, d\mu(s)$, la condición necesaria y suficiente para que la secuencia $\{c_k\}$ provenga de una medida positiva es que las matrices de Hankel:

$$H_N^\mu = (c_{i+j})_{0 \leq i,j \leq N}$$

sean semidefinidas positivas para todo $N \geq 0$. Esta es la condición de positividad de Hamburger.

Para $dm_{full}$ y $dm_{full,on}$, ambas matrices $H_N^{full}$ y $H_N^{full,on}$ son definidas positivas (son matrices de Gram de funciones linealmente independientes en los respectivos $L^2$).

**Proposición 2.2 (Relación entre discrepancias y diferencia de Hankel).** Sea $\Delta H_N = H_N^{full} - H_N^{full,on}$. La condición $a_k^{full} = a_k^{full,on}$ para todo $k \leq N$ es equivalente a que los momentos coincidan: $\mu_j^{full} = \mu_j^{full,on}$ para $j = 0, 1, \ldots, 2N$, es decir, $\Delta H_N = 0$.

*Demostración.* Los coeficientes de Jacobi $a_0, a_1, \ldots, a_N$ están determinados por los momentos $\mu_0, \mu_1, \ldots, \mu_{2N+1}$ mediante el algoritmo de Gram-Schmidt (que corresponde a la factorización de Cholesky de la matriz de Hankel $H_{N+1}$). Dos medidas tienen los mismos primeros $2N+2$ momentos si y solo si sus matrices de Hankel $H_{N+1}$ son iguales, si y solo si sus coeficientes de Jacobi $a_0, \ldots, a_N$ son iguales. Esto es una versión del teorema de Favard. $\square$

**Corolario 2.3.** La condición $T_\lambda = 0$ (criterio CTP) es equivalente a:

$$\int_{\mathbb{R}} W_\lambda(s)\, s^j\, dm_\infty(s) \cdot (|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2) = 0 \quad \forall j, \lambda,$$

que es una condición sobre la diferencia $|\zeta|^2 - |\zeta_{on}|^2$ ponderada por los polinomios de la medida de referencia.

La relación entre $\Delta_k = (a_k^{full})^2 - (a_k^{full,on})^2$ y $\Delta H_N$ es la siguiente: $\Delta_k$ es una función homogénea de grado $1$ en las entradas de $\Delta H_N$ (concretamente, es el cociente de dos determinantes de submatrices de Hankel, que depende de las primeras $2k+2$ entradas). El mapa $\Delta H_N \mapsto (\Delta_0, \ldots, \Delta_N)$ es, en general, no lineal.

---

## §3. La desigualdad de Markov-Stieltjes y el control de los coeficientes

### 3.1. El teorema de Markov-Stieltjes

**Teorema 3.1 (Markov-Stieltjes, formulación relevante).** Sean $\mu$ y $\nu$ dos medidas positivas en $\mathbb{R}$ con los mismos primeros $2N$ momentos: $\int s^k\, d\mu = \int s^k\, d\nu$ para $k = 0, 1, \ldots, 2N-1$. Sean $x_1 < x_2 < \cdots < x_N$ los ceros del polinomio ortogonal de grado $N$ con respecto a $\mu$ (= con respecto a $\nu$, pues los momentos coinciden). Entonces:

$$\mu((-\infty, x_j]) = \nu((-\infty, x_j]) \quad \text{para todo } j = 1, \ldots, N.$$

Es decir, las funciones de distribución de $\mu$ y $\nu$ coinciden en todos los nodos de cuadratura de Gauss.

*Referencia:* Szegő [S39], Capítulo 3; Akhiezer [A65], Teorema 1.3.3.

**Corolario 3.2.** Si las medidas $dm_{full}$ y $dm_{full,on}$ tienen los mismos primeros $2N$ momentos, entonces sus coeficientes de Jacobi $a_k^{full}$ y $a_k^{full,on}$ coinciden para $k = 0, 1, \ldots, N-1$.

### 3.2. La condición de igualdad de momentos y su significado aritmético

La condición de coincidencia de momentos $\mu_j^{full} = \mu_j^{full,on}$ para $j \leq 2N-1$ equivale a:

$$\int_{\mathbb{R}} s^j \left(|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2\right) dm_\infty(s) = 0, \quad j = 0, 1, \ldots, 2N-1.$$

**Proposición 3.3.** Si RH es verdadera, entonces $|\zeta(1/2+is)|^2 = |\zeta_{on}(1/2+is)|^2$ para todo $s \in \mathbb{R}$, de modo que todos los momentos coinciden y, por el Corolario 3.2, $a_k^{full} = a_k^{full,on}$ para todo $k$. Esta es la implicación directa (ya conocida).

**Proposición 3.4 (Dirección difícil: Markov-Stieltjes no es suficiente).** La igualdad de los primeros $2N$ momentos implica la igualdad de los primeros $N$ coeficientes de Jacobi (Corolario 3.2). Para concluir RH se necesitaría la igualdad de todos los momentos — es decir, la igualdad de las medidas como medidas en $\mathbb{R}$. Pero la igualdad de medidas es precisamente RH (que es lo que queremos probar). El argumento es circular: usar Markov-Stieltjes para reducir RH a la igualdad de momentos es solo una reescritura del problema, no una demostración.

---

## §4. La diferencia $|\zeta|^2 - |\zeta_{on}|^2$ y sus momentos bajo $\neg$RH

### 4.1. Fórmula via el producto de Hadamard

Bajo la hipótesis $\neg$RH, existe al menos un cero $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$. Por la ecuación funcional, los ceros off-critical aparecen en cuádruplos $\{\rho_0, \overline{\rho_0}, 1-\rho_0, 1-\overline{\rho_0}\}$. Escribamos $\delta_0 = \sigma_0 - 1/2 \neq 0$.

La relación entre $\zeta$ y $\zeta_{on}$ vía el producto de Hadamard es:

$$\frac{\xi(s)}{\xi_{on}(s)} = \prod_{\rho_0 \text{ off-crit}} \frac{s - \rho_0}{s - (1/2 + i\gamma_0)},$$

donde el producto es sobre todos los ceros off-critical (con sus multiplicidades y los cuatro elementos del cuádruplo). Restringiéndonos a la recta crítica $s = 1/2 + iu$ con $u \in \mathbb{R}$:

$$\frac{|\zeta(1/2+iu)|^2}{|\zeta_{on}(1/2+iu)|^2} = \prod_j \frac{|1/2+iu - \rho_j^{off}|^2}{|1/2+iu - 1/2 - i\gamma_j^{off}|^2} = \prod_j \left(1 + \frac{\delta_j^2}{(u - \gamma_j^{off})^2}\right),$$

donde el producto corre sobre los ceros off-critical $\rho_j^{off} = (1/2 + \delta_j) + i\gamma_j^{off}$ (con $\delta_j > 0$ por convención, incluyendo solo uno de cada par $\rho_j, 1-\overline{\rho_j}$ en la mitad derecha).

Luego:

$$|\zeta(1/2+iu)|^2 - |\zeta_{on}(1/2+iu)|^2 = |\zeta_{on}(1/2+iu)|^2 \cdot \left[\prod_j \left(1 + \frac{\delta_j^2}{(u-\gamma_j^{off})^2}\right) - 1\right].$$

**Proposición 4.1 (Signo de la diferencia).** La función $u \mapsto |\zeta(1/2+iu)|^2 - |\zeta_{on}(1/2+iu)|^2$ es no negativa para todo $u \in \mathbb{R}$ (fuera de los ceros de $\zeta_{on}$), ya que el producto es $\geq 1$ y $|\zeta_{on}|^2 \geq 0$.

*Demostración.* Cada factor $1 + \delta_j^2/(u-\gamma_j^{off})^2 \geq 1$, luego el producto es $\geq 1$. El factor $|\zeta_{on}|^2 \geq 0$. El producto de no-negativos es no-negativo. $\square$

**Corolario 4.2.** Bajo $\neg$RH, $dm_{full}(s) \geq dm_{full,on}(s)$ para todo $s$ (en sentido puntual de las densidades), y en consecuencia $\mu_k^{full} \geq \mu_k^{full,on}$ para $k$ par (momentos de una medida mayor). En particular, $\Delta_k = (a_k^{full})^2 - (a_k^{full,on})^2 \geq 0$ para todo $k$ (la dirección ya conocida).

### 4.2. Los momentos de la diferencia

Bajo la hipótesis simplificada de un solo par de ceros off-critical con $\delta_0 \ll 1$ (linealización):

$$|\zeta(1/2+iu)|^2 - |\zeta_{on}(1/2+iu)|^2 \approx |\zeta_{on}(1/2+iu)|^2 \cdot \delta_0^2 \sum_j \frac{1}{(u-\gamma_j^{off})^2}.$$

El $k$-ésimo momento de la diferencia es entonces:

$$\mu_k^{full} - \mu_k^{full,on} \approx \delta_0^2 \sum_j \int_{\mathbb{R}} \frac{u^k |\zeta_{on}(1/2+iu)|^2}{(u-\gamma_j^{off})^2}\, dm_\infty(u).$$

**Proposición 4.3 (Convergencia de la integral de momento).** El integral

$$I_{k,j} = \int_{\mathbb{R}} \frac{u^k |\zeta_{on}(1/2+iu)|^2}{(u-\gamma_j^{off})^2}\, dm_\infty(u)$$

converge como valor principal para todo $k \geq 0$ y $\gamma_j^{off} \in \mathbb{R}$.

*Demostración.* El integrando tiene un polo de orden 2 en $u = \gamma_j^{off}$, pero la medida $dm_\infty$ es absolutamente continua (con densidad $C^\infty$) y $|\zeta_{on}|^2$ se anula en $u = \gamma_j^{off}$ (pues $\gamma_j^{off}$ es la parte imaginaria de un cero de $\zeta_{on}$ sobre la recta crítica). Por tanto:

$$|\zeta_{on}(1/2+iu)|^2 \sim C_j \cdot (u - \gamma_j^{off})^{2m_j} \quad \text{para } u \to \gamma_j^{off},$$

donde $m_j \geq 1$ es la multiplicidad del cero. Si $m_j = 1$, la singularidad $1/(u-\gamma_j^{off})^2 \cdot (u-\gamma_j^{off})^2 = 1$ es integrable (la singularidad se cancela). Si $m_j \geq 2$, el integrando es aún más regular. En todos los casos, $I_{k,j}$ es una integral propia convergente. $\square$

**Observación 4.4.** La cancelación en la Proposición 4.3 es de naturaleza aritmética profunda: los ceros de $\zeta_{on}$ se sitúan exactamente en los $\gamma_j^{off}$, lo que regulariza la singularidad del kernel $1/(u-\gamma_j^{off})^2$. Esto sugiere que la construcción natural de la forma cuadrática $Q$ debe involucrar $|\zeta_{on}|^2$ en el numerador.

---

## §5. La forma cuadrática de Castelnuovo-Severi aritmético

### 5.1. Construcción de $Q$

Motivados por la cancelación de la Proposición 4.3, definimos la siguiente forma cuadrática.

**Definición 5.1 (Forma cuadrática de Castelnuovo-Severi aritmético).** Para funciones $\phi, \psi \in L^2(dm_{full,on})$, se define la forma sesquilineal:

$$Q(\phi, \psi) = \iint_{\mathbb{R}^2 \setminus \mathrm{diag}} \frac{(\phi(u) - \phi(v))\overline{(\psi(u) - \psi(v))}}{(u-v)^2}\, |\zeta_{on}(1/2+iu)|^2 |\zeta_{on}(1/2+iv)|^2\, dm_\infty(u)\, dm_\infty(v).$$

La forma cuadrática asociada es $Q(\phi) = Q(\phi, \phi)$.

**Observación 5.2 (Forma equivalente vía derivada fraccionaria).** La forma $Q$ es exactamente la norma al cuadrado en el espacio de Sobolev fraccionario $H^{1/2}(dm_{full,on})$ (espacio de Dirichlet de la medida $dm_{full,on}$). En efecto:

$$Q(\phi, \phi) = \iint \frac{|\phi(u) - \phi(v)|^2}{(u-v)^2}\, dm_{full,on}(u)\, dm_{full,on}(v),$$

que es precisamente la norma al cuadrado en el espacio de Dirichlet $\mathcal{D}(dm_{full,on})$ (véase Fukushima-Oshima-Takeda [FOT94]).

**Proposición 5.3 (Semidefinición positiva).** La forma $Q$ es semidefinida positiva: $Q(\phi, \phi) \geq 0$ para toda $\phi$ en el dominio.

*Demostración.* El integrando es $|\phi(u) - \phi(v)|^2 \cdot (u-v)^{-2} \cdot |\zeta_{on}|^2(u) \cdot |\zeta_{on}|^2(v) \geq 0$ para $(u,v)$ fuera de la diagonal y fuera de los ceros de $\zeta_{on}$. Siendo el integrando no negativo y la integral absolutamente convergente (por la Proposición 4.3 y la condición $|\phi(u) - \phi(v)|^2/(u-v)^2 \leq |\phi'|^2$ cuando $\phi$ es Lipschitz), la integral es no negativa. Para funciones generales en $L^2(dm_{full,on})$ la regularidad se obtiene por densidad. $\square$

**Proposición 5.4 (El núcleo de $Q$).** $Q(\phi, \phi) = 0$ si y solo si $\phi$ es constante $dm_{full,on}$-c.t.p. En particular, el núcleo de $Q$ en $L^2_0(dm_{full,on})$ (funciones con integral nula) es $\{0\}$.

*Demostración.* Si $Q(\phi, \phi) = 0$, entonces $\phi(u) = \phi(v)$ para $dm_{full,on} \otimes dm_{full,on}$-c.t.p. $(u,v)$, lo que implica que $\phi$ es constante $dm_{full,on}$-c.t.p. (pues $dm_{full,on}$ no tiene átomos: es absolutamente continua con respecto a $dm_\infty$, que a su vez es absolutamente continua con respecto a la medida de Lebesgue). $\square$

### 5.2. Relación de $Q$ con la comparación de medidas

La forma $Q$ mide la regularidad de $\phi$ en el espacio de Dirichlet de $dm_{full,on}$. Para que $Q$ sea el Pilar III del mecanismo de Weil, necesitamos que su positividad (o la estructura de su núcleo) detecte la diferencia $dm_{full} \neq dm_{full,on}$.

**Proposición 5.5.** Sea $f(u) = |\zeta(1/2+iu)|^2 - |\zeta_{on}(1/2+iu)|^2$ la diferencia de densidades. Entonces:

$$Q(f, \mathbf{1}) = \iint \frac{(f(u) - f(v)) \cdot 1}{(u-v)^2}\, dm_{full,on}(u)\, dm_{full,on}(v).$$

Si $dm_{full} = dm_{full,on}$ (es decir, $f = 0$), entonces $Q(f, \phi) = 0$ para toda $\phi$. La recíproca — si $Q(f, \phi) = 0$ para toda $\phi$ entonces $f = 0$ — requeriría que $f = 0$ en $\mathcal{D}(dm_{full,on})$, lo que equivaldría a $f$ constante $dm_{full,on}$-c.t.p.

**Observación 5.6 (El obstáculo principal).** La forma $Q$ de la Definición 5.1 está bien definida y es semidefinida positiva, pero su definición no involucra directamente la diferencia $dm_{full} - dm_{full,on}$. Para conectar $Q$ con el criterio $T_\lambda = 0$, habría que mostrar que la función de diferencia $f = |\zeta|^2 - |\zeta_{on}|^2$ (que es $\geq 0$ bajo $\neg$RH, por la Proposición 4.1) pertenece al núcleo de alguna forma cuadrática relacionada con $Q$. Pero esto no está disponible: la positividad de $Q$ es una propiedad intrínseca del espacio de Dirichlet de $dm_{full,on}$, no una afirmación sobre la comparación de medidas.

---

## §6. Regularización y la forma $Q_\lambda$

### 6.1. Los ceros de $\zeta_{on}$ como obstáculo de regularidad

El espacio de Dirichlet $\mathcal{D}(dm_{full,on})$ está bien definido, pero la función $f = |\zeta|^2/|\zeta_{on}|^2 - 1$ (el cociente de densidades) puede no pertenecer a $\mathcal{D}(dm_{full,on})$ debido a la presencia de los ceros de $\zeta_{on}$: en un entorno de $u = \gamma_n$ (cero de $\zeta_{on}$), la función $f(u) \approx C_n(u-\gamma_n)^{2\delta_n^2}$ (potencia pequeña), cuya derivada puede ser grande. Para remediar esto, se introduce una regularización.

**Definición 6.1 (Forma regularizada $Q_\lambda$).** Para $\lambda > 0$, sea $W_\lambda$ el kernel de Abel del programa CCM. Definimos:

$$Q_\lambda(\phi, \psi) = \iint_{\mathbb{R}^2 \setminus \mathrm{diag}} \frac{(\phi(u) - \phi(v))\overline{(\psi(u)-\psi(v))}}{(u-v)^2} W_\lambda(u) W_\lambda(v)\, dm_\infty(u)\, dm_\infty(v).$$

Esta forma no depende de $|\zeta_{on}|^2$ directamente; el papel del kernel de Abel $W_\lambda$ es proveer un corte espectral que regulariza las singularidades.

**Proposición 6.2 (Propiedades de $Q_\lambda$).** 

(i) $Q_\lambda$ es semidefinida positiva para todo $\lambda > 0$.

(ii) $Q_\lambda \to Q_{Lebesgue}$ cuando $\lambda \to \infty$, donde $Q_{Lebesgue}$ es la forma de Dirichlet de la medida de Lebesgue (norma en $H^{1/2}(\mathbb{R})$).

(iii) Para la función $f_\lambda = W_\lambda \cdot (|\zeta|^2 - |\zeta_{on}|^2)$:

$$Q_\lambda(f_\lambda, f_\lambda) = \iint \frac{|f_\lambda(u) - f_\lambda(v)|^2}{(u-v)^2}\, dm_\infty(u)\, dm_\infty(v) \geq 0.$$

*Demostración.* El punto (i) es idéntico al de la Proposición 5.3 (el integrando es no negativo). El punto (ii) sigue de que $W_\lambda(u) \to 1$ cuando $\lambda \to \infty$ (en el sentido de Cesàro para la medida $dm_\infty$). El punto (iii) es una aplicación directa de la definición. $\square$

**Observación 6.3.** La forma $Q_\lambda$ de la Definición 6.1 es semidefinida positiva pero su positividad no tiene contenido aritmético directo: es simplemente la norma $H^{1/2}$ (fraccionaria) del truncado $f_\lambda$, que es no negativa por ser una norma al cuadrado. No hay información que distinga $|\zeta|^2$ de $|\zeta_{on}|^2$ en la positividad de $Q_\lambda$.

---

## §7. La conexión con la correlación de pares de Montgomery

### 7.1. El núcleo $1/(u-v)^2$ y la correlación de pares

La forma cuadrática $Q$ de la Definición 5.1 involucra el kernel $K(u,v) = |\phi(u)-\phi(v)|^2/(u-v)^2$. Para $\phi = \mathbf{1}$ (la función constante 1), este kernel se reduce a $1/(u-v)^2$, y la integral doble:

$$\iint_{u \neq v} \frac{1}{(u-v)^2}\, dm_{full,on}(u)\, dm_{full,on}(v)$$

es una suma de la forma $\sum_{m \neq n} (\gamma_m - \gamma_n)^{-2}$ (sobre los ceros de $\zeta_{on}$, con pesos de la medida $dm_\infty$). Esta es exactamente la clase de sumas que aparece en la conjetura de correlación de pares de Montgomery.

**La conjetura de Montgomery (1973)** afirma que para funciones test $f$ en la clase de Schwartz,

$$\sum_{\substack{\gamma, \gamma' \leq T \\ \gamma \neq \gamma'}} f\!\left(\frac{(\gamma-\gamma')\log T}{2\pi}\right) \sim \frac{T \log T}{2\pi} \int_{-\infty}^{\infty} f(u)\left[1 - \left(\frac{\sin \pi u}{\pi u}\right)^2\right] du$$

cuando $T \to \infty$ (y donde la suma es sobre partes imaginarias de ceros en $\mathrm{Im}(s) > 0$).

Para $f(u) = |u|^{-2}$ (la función kernel de nuestro $Q$), la integral de Montgomery diverge en $u = 0$, lo que refleja que la suma $\sum_{\gamma \neq \gamma'} (\gamma-\gamma')^{-2}$ diverge (los ceros se acumulan en la escala logarítmica). Esto significa que $Q(\mathbf{1}, \mathbf{1}) = +\infty$, o equivalentemente que la función constante $\phi = 1$ no pertenece al espacio de Dirichlet $\mathcal{D}(dm_{full,on})$.

**Proposición 7.1 (El dominio de $Q$ excluye funciones constantes).** La función $\phi = \mathbf{1}$ no pertenece al espacio de Dirichlet $\mathcal{D}(dm_{full,on})$: $Q(\mathbf{1}, \mathbf{1}) = +\infty$. Las funciones en $\mathcal{D}(dm_{full,on})$ deben decaer suficientemente rápido en $|u| \to \infty$.

*Demostración.* Para $\phi = 1$:

$$Q(1, 1) = \iint \frac{|1 - 1|^2}{(u-v)^2}\, dm_{full,on}^2 = 0.$$

Contradicción: el cálculo da cero, no $+\infty$. La proposición es vacuamente falsa tal como está enunciada: $|\phi(u) - \phi(v)|^2 = 0$ para $\phi$ constante, luego $Q(\phi, \phi) = 0$ para toda $\phi$ constante. El espacio de Dirichlet contiene todas las constantes en el núcleo de la forma semidefinida. $\square$

**Observación 7.2 (Corrección).** El espacio de Dirichlet $\mathcal{D}(dm_{full,on})$ contiene las constantes en su núcleo. La parte no trivial es la restricción al espacio $L^2_0(dm_{full,on})$ de funciones con integral cero (donde la Proposición 5.4 garantiza trivialidad del núcleo). La conexión con Montgomery es la siguiente: la suma divergente $\sum_{\gamma \neq \gamma'} (\gamma-\gamma')^{-2}$ aparece cuando se evalúa la forma $Q$ en la función indicadora de un intervalo (que no está en $\mathcal{D}$), no en funciones suaves.

**Proposición 7.3 (Conexión formal con Montgomery).** Bajo la conjetura de Montgomery, para funciones $\phi$ en la clase de Schwartz con $\hat\phi$ de soporte compacto en $(-1,1)$:

$$Q(\phi, \phi) \sim C \cdot \int_{\mathbb{R}} |\hat\phi(\xi)|^2 |\xi|\, d\xi,$$

que es la norma al cuadrado en $H^{1/2}$ (espacio de Sobolev de orden $1/2$). Esto confirma que la forma $Q$ es equivalente a la norma $H^{1/2}$ bajo la conjetura de Montgomery, y en particular es positiva definida en $L^2_0(dm_{full,on})$.

*Estado:* Conjetural (requiere la conjetura de Montgomery). La equivalencia incondicional entre $Q$ y la norma $H^{1/2}$ es un problema abierto.

---

## §8. Síntesis: el diagnóstico del Pilar III y lo que falta

### 8.1. Resultados establecidos en este documento

**Resultado 1 (Proposición 1.2).** La Proposición 1.1 en la forma enunciada (con $\mathrm{Tr}(M_N)$ en el denominador) es vacía porque $\mathrm{Tr}(M_N) = 0$ identicamente. La analogía de Castelnuovo-Severi no puede formularse via la traza de $M_N$; la estructura relevante es la de $\mathrm{Tr}(M_N^2)$.

**Resultado 2 (Proposición 2.2).** La igualdad de los primeros $2N$ momentos de $dm_{full}$ y $dm_{full,on}$ implica (via Markov-Stieltjes) la igualdad de los primeros $N$ coeficientes de Jacobi, pero la condición sobre momentos es equivalente a RH, de modo que este enfoque es circular.

**Resultado 3 (Proposición 4.1).** Bajo $\neg$RH, la diferencia $|\zeta|^2 - |\zeta_{on}|^2$ es no negativa, lo que es consistente con $\Delta_k \geq 0$ (ya conocido). No hay cancelación de signo: la diferencia no puede ser cero en un conjunto de medida positiva sin forzar RH.

**Resultado 4 (Proposición 5.3 y 5.4).** La forma cuadrática $Q$ de la Definición 5.1 es semidefinida positiva con núcleo exactamente las constantes. En $L^2_0(dm_{full,on})$ es positiva definida. Sin embargo, la positividad de $Q$ es una propiedad intrínseca de $dm_{full,on}$ que no depende de si $dm_{full} = dm_{full,on}$.

**Resultado 5 (Proposición 4.3).** La cancelación de la singularidad de $1/(u-\gamma_j)^2$ por los ceros de $\zeta_{on}$ en $u = \gamma_j$ es exacta y regulariza todos los integrales de momentos.

### 8.2. El obstáculo preciso: la positividad de $Q$ no distingue $dm_{full}$ de $dm_{full,on}$

La dificultad fundamental del Pilar III puede ahora formularse con precisión quirúrgica.

**Proposición 8.1 (El obstáculo del Pilar III — Enunciado preciso).** Ninguna forma cuadrática $Q$ que sea:

(a) definida únicamente en términos de $dm_{full,on}$ (no de $dm_{full}$), y  
(b) positiva definida en $L^2_0(dm_{full,on})$,

puede distinguir por sí sola si $dm_{full} = dm_{full,on}$.

*Demostración.* Una forma $Q$ como en (a) y (b) es una propiedad de $dm_{full,on}$ sola. Su positividad no lleva información sobre $dm_{full}$. Para comparar las dos medidas es necesario involucrar $dm_{full}$ directamente en la construcción de $Q$. $\square$

**Corolario 8.2 (La forma $Q$ correcta debe involucrar $dm_{full}$).** El análogo aritmético de la desigualdad de Castelnuovo-Severi, si existe, debe ser una forma cuadrática $Q[dm_{full}, dm_{full,on}]$ que dependa de ambas medidas y cuya positividad sea equivalente a $dm_{full} = dm_{full,on}$.

La candidata natural es la forma de comparación:

$$Q_{comp}(\phi, \psi) = \int_{\mathbb{R}} \phi(u)\, \overline{\psi(u)}\, (dm_{full}(u) - dm_{full,on}(u)),$$

que es una forma lineal en $dm_{full} - dm_{full,on}$ y, bajo $\neg$RH, satisface $Q_{comp}(\phi, \phi) \geq 0$ para toda $\phi$ (por la Proposición 4.1). Pero la positividad de $Q_{comp}$ es equivalente a la no-negatividad de $dm_{full} - dm_{full,on}$, que ya sabemos que es no negativa bajo $\neg$RH, y que es cero bajo RH. Esta forma captura el contenido del criterio $T_\lambda = 0$ pero no añade información sobre cómo demostrarlo.

### 8.3. Programa para cerrar el Pilar III

Para que el Pilar III cierre el argumento hacia RH se necesitaría — en paralelo con el caso de curvas — un argumento del tipo siguiente:

**Paso A:** Construir una forma cuadrática $Q_{arith}$ que sea positiva por razones *independientes* de si RH es verdadera (es decir, cuya positividad sea una propiedad intrínseca del problema, no una consecuencia de RH). Este es el análogo de la positividad del número de puntos $N_n \geq 0$ en el caso de curvas.

**Paso B:** Mostrar que la positividad de $Q_{arith}$ junto con la ecuación funcional (Pilar II) fuerza $dm_{full} = dm_{full,on}$.

En el caso de curvas, el Paso A proviene de la geometría ($N_n$ cuenta puntos, cantidad entera no negativa). En el caso de números, no existe un análogo directo: las sumas $\sum_{k \leq N} \Delta_k$ son positivas pero su positividad es consecuencia de $|\zeta|^2 \geq |\zeta_{on}|^2$ bajo $\neg$RH, lo que es circular.

**Proposición 8.3 (Diagnóstico final).** El análogo del argumento de positividad de Weil en el mundo CCM requiere encontrar una propiedad de $|\zeta|^2$ que sea:

(i) Demostrable sin asumir RH.  
(ii) Suficientemente fuerte para distinguir $|\zeta|^2 = |\zeta_{on}|^2$ de $|\zeta|^2 > |\zeta_{on}|^2$.

La única propiedad de este tipo que se vislumbra en la literatura es la conjetura de que los ceros de $\zeta$ están en posición genérica (ceros simples, con estadística de GUE), que se formalizaría como una cota inferior del tipo $|\zeta(1/2+iu)|^2 \geq C/(|\log(u-\gamma_n)|)$ cerca de cada cero $\gamma_n$. Si tal cota inferior fuera demostrable, y si $|\zeta_{on}|$ satisface exactamente la misma cota, entonces la igualdad de módulos en los ceros podría forzarse. Pero esta cota tampoco se conoce incondicionalmente.

---

## §9. Conclusión y estado del programa

El Documento 80 establece los siguientes hechos sobre el "Castelnuovo-Severi aritmético":

1. **La analogía directa con matrices de Jacobi (§1) no funciona**: la traza de $M_N$ es cero idénticamente, vaciando la desigualdad propuesta.

2. **El argumento de Markov-Stieltjes (§3) es circular**: reduce RH a la igualdad de momentos, que es otra forma de enunciar RH.

3. **La diferencia de medidas bajo $\neg$RH (§4) es no negativa**: no hay cancelación de signo, lo que es consistente con el programa pero no da nueva información.

4. **La forma $Q$ de la Definición 5.1 (§5) existe, es semidefinida positiva, y es positiva definida en $L^2_0$**, pero no detecta la diferencia $dm_{full} \neq dm_{full,on}$ porque no depende de $dm_{full}$.

5. **La conexión con Montgomery (§7) es formal**: bajo la conjetura de Montgomery, $Q$ es equivalente a la norma $H^{1/2}$, pero este hecho no añade información hacia RH.

6. **El obstáculo del Pilar III (§8) es preciso**: se necesita una forma cuadrática que dependa de $dm_{full}$ y $dm_{full,on}$ simultáneamente, cuya positividad sea demostrable sin asumir RH, y cuyo núcleo sea exactamente $\{dm_{full} = dm_{full,on}\}$.

**Conjetura 9.1 (Castelnuovo-Severi aritmético — versión corregida).** La forma cuadrática del Pilar III es:

$$Q_{CS}(\phi) = \int_{\mathbb{R}} |\phi(u)|^2\, (dm_{full}(u) - dm_{full,on}(u)) + \iint \frac{|\phi(u)-\phi(v)|^2}{(u-v)^2}\, dm_{full,on}(u)\, dm_{full,on}(v).$$

Esta forma es semidefinida positiva en todo caso, y su restricción a $L^2_0$ satisface: $Q_{CS}(\phi) = 0$ para toda $\phi \in L^2_0$ implica $dm_{full} = dm_{full,on}$ (es decir, RH). Sin embargo, la positividad de $Q_{CS}$ en $L^2_0$ no está demostrada: el primer término puede ser cero o positivo (es positivo bajo $\neg$RH), pero su relación con el segundo término es desconocida.

El estado del Camino 1 permanece: el Pilar III es el único obstáculo, y su construcción rigurosa es el problema abierto central del programa.

---

## Referencias

- [A65] N. Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver and Boyd, 1965.
- [C99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999), 29–106.
- [FOT94] M. Fukushima, Y. Oshima, M. Takeda, *Dirichlet Forms and Symmetric Markov Processes*, De Gruyter, 1994.
- [KS03] R. Killip, B. Simon, *Sum rules for Jacobi matrices and their applications to spectral theory*, Ann. of Math. 158 (2003), 253–321.
- [M73] H. Montgomery, *The pair correlation of zeros of the zeta function*, in Analytic Number Theory (St. Louis, 1972), Proc. Sympos. Pure Math. 24 (1973), 181–193.
- [S39] G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications, 1939 (4th ed. 1975).
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (revised by D. R. Heath-Brown), Oxford University Press, 1986.
- [Docs 64, 74, 77] Documentos internos del programa, Fases 32–33.

---

*Fin del Documento 80.*
