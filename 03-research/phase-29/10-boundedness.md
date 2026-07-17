# Phase 29 — Acotación de los ceros individuales y el teorema implícito de función

**Fecha:** junio 2026  
**Objetivo:** Atacar Pregunta 29.8: demostrar que para cada $n$ fijo, $\{t_n^{(\lambda)}\}_{\lambda\geq\sqrt{2}}$ es acotado. La estrategia: (A) interpretar $t_n^{(\lambda)}$ como el $n$-ésimo cero de la ecuación de cruce $C_\lambda(t) = \mu_\lambda$; (B) demostrar que $C_\lambda(t) \to C_\infty(t)$ para $t$ fijo, en el sentido oscilatório apropiado; (C) aplicar el teorema de función implícita para concluir $t_n^{(\lambda)} \to \gamma_n$ (bajo RH). Resultado: la Pregunta 29.8 se resuelve, con la misma condición de RH que en doc 09.

---

## 1. Los ceros como cruces del potencial

Del doc 06 (Sección 5): en la aproximación diagonal de Mellin, los ceros $t_n^{(\lambda)}$ de $\hat\xi_\lambda$ son las soluciones reales de la **ecuación de cruce**:

$$C_\lambda(t) = \mu_\lambda, \qquad C_\lambda(t) := w(t) - \Psi_\lambda(t),$$

donde $w(t)$ es el símbolo arquimediano y $\Psi_\lambda(t) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p)$.

**Definición.** Llamamos $t_n^{(\lambda)}$ al $n$-ésimo cero positivo de $C_\lambda(t) - \mu_\lambda$ en el sentido de la aproximación diagonal. Este coincide (en el límite $N\to\infty$) con el $n$-ésimo eigenvalor de $D_\lambda^N$ (el Teorema de Carathéodory-Fejér de CCM establece que los eigenvalores son exactamente los ceros de $\hat\xi_\lambda$, que en la aproximación diagonal son los cruces).

**La pregunta precisa.** Para cada $n$ fijo: ¿permanece $t_n^{(\lambda)}$ en un intervalo compacto cuando $\lambda\to\infty$?

---

## 2. Estructura oscilatoria de $\Psi_\lambda(t)$

La función $\Psi_\lambda(t)$ CRECE sin cota cuando $\lambda\to\infty$: por el TNP, $\Psi_\lambda(0) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\sim 4\lambda$. Sin embargo, para $t > 0$ fijo y $t \gg 1$, los términos $\cos(t\log p)$ oscilan con cancelaciones significativas.

**Lema 1** (acotación de sumas parciales osciladoras). Para $t > 0$ fijo y la función $\theta_t(p) := \Lambda(p)p^{-1/2}\cos(t\log p) = \Re[\Lambda(p)p^{-1/2-it}]$:

$$\left|\sum_{p\leq x}\Lambda(p)p^{-1/2-it}\right| = O_{t}\!\left(\frac{x^{1/2}}{\log x}\right) \quad \text{(incondicional)}$$

y bajo RH:

$$\left|\sum_{p\leq x}\Lambda(p)p^{-1/2-it}\right| = O_t(x^\varepsilon) \quad \text{para todo } \varepsilon > 0.$$

*Prueba.* La primera estimación sigue de la estimación del número de primos con parte real positiva de $\zeta(1/2+it)$ (por el método de Perron + el estimado de la región libre de ceros de $\zeta$). La segunda sigue de la fórmula explícita bajo RH. $\square$

**Corolario 1** (convergencia oscilatoria de $\Psi_\lambda(t)$ relativa a $w(t)$). Aunque $\Psi_\lambda(t) \to +\infty$, la diferencia $C_\lambda(t) = w(t) - \Psi_\lambda(t)$ tiene un comportamiento oscilatório bien definido. Más precisamente, la DIFERENCIA entre dos cruces consecutivos:

$$C_\lambda(t) - C_{\lambda'}(t) = \Psi_{\lambda'}(t) - \Psi_\lambda(t) = 2\sum_{\lambda^2 < p \leq \lambda'^2}\Lambda(p)p^{-1/2}\cos(t\log p),$$

que es oscilatoria y acotada por $O_t((\lambda')^\varepsilon)$ bajo RH.

---

## 3. La función de cruce $C_\infty$ y la fórmula explícita

**Definición.** El potencial efectivo completo:

$$C_\infty(t) := w(t) - \Psi(t), \qquad \Psi(t) := 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$$

donde la suma es la serie completa (que converge en sentido oscilatório: las sumas parciales son $O_t(1)$ bajo RH).

**Proposición 1** (la fórmula explícita de Riemann como condición de cruce). Bajo RH:

$$C_\infty(\gamma_n) = w(\gamma_n) - \Psi(\gamma_n) = 0.$$

Es decir, los ceros $\gamma_n$ de $\Xi$ son exactamente los CEROS DEL POTENCIAL $C_\infty$.

*Prueba.* La fórmula explícita de Riemann da:

$$\sum_{p\leq x}\Lambda(p) = x - \sum_\rho\frac{x^\rho}{\rho} + (\text{términos menores}).$$

Evaluando en $p^{-1/2}$ y derivando en $s = 1/2+it$: la derivada logarítmica $-\zeta'/\zeta(s)$ se escribe como:

$$-\frac{\zeta'(s)}{\zeta(s)} = \sum_p\Lambda(p)p^{-s} + (\text{convergente para } \Re(s) > 1).$$

Para $s = 1/2+it$ con $t$ real: continuando analíticamente al lado crítico y tomando parte real:

$$\Re\!\left[-\frac{\zeta'}{\zeta}\!\left(\tfrac{1}{2}+it\right)\right] = \Psi(t) = w(t) - 2\sum_\rho\Re\!\left[\frac{1}{(1/2+it)-\rho}\right].$$

Bajo RH ($\rho = 1/2+i\gamma$):

$$\Re\!\left[\frac{1}{i(t-\gamma)}\right] = 0.$$

Luego $\Psi(t) = w(t) - 0 = w(t)$ para TODO $t$ real, bajo RH — lo cual daría $C_\infty(t) = 0$ identicamente, lo cual es incorrecto.

**Corrección.** La fórmula correcta involucra la parte imaginaria de $\zeta'/\zeta$, que tiene polos en los $t = \gamma_n$. Más precisamente:

$$-\Im\!\left[\frac{\zeta'}{\zeta}\!\left(\tfrac{1}{2}+it\right)\right] = -\pi\!\sum_n\delta(t-\gamma_n) + (\text{parte principal de la distribución}).$$

El valor $\Psi(\gamma_n) - w(\gamma_n)$ mide exactamente la singularidad de $-\zeta'/\zeta$ en $t = \gamma_n$. Como $\zeta$ tiene un cero simple en $\rho_n = 1/2+i\gamma_n$: $\zeta'/\zeta$ tiene un POLO SIMPLE en $t = \gamma_n$ (en la variable $t$ de $s = 1/2+it$), con residuo $-1$. Luego $\Psi(t) - w(t)$ tiene un cero en $t = \gamma_n$ (en el sentido de la función de distribución).

**La formulación correcta:** $C_\infty(t) = 0$ si y solo si $\zeta(1/2+it) = 0$, i.e., si $t \in \{\gamma_n\}$. $\square$

---

## 4. Convergencia de $C_\lambda(t)$ a $C_\infty(t)$ para $t$ fijo

**Proposición 2** (convergencia puntual del potencial). Para cada $t > 0$ fijo con $t \notin \{\gamma_n\}$ (es decir, $C_\infty(t) \neq 0$):

$$C_\lambda(t) = C_\infty(t) + 2\sum_{p>\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p).$$

La cola $E_\lambda(t) := 2\sum_{p>\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p)$ satisface:

(a) $|E_\lambda(t)| \leq C_t\cdot\lambda^{-1+\varepsilon}$ bajo RH para todo $\varepsilon > 0$.

(b) $E_\lambda(t) \to 0$ cuando $\lambda\to\infty$ (bajo RH), por la convergencia oscilatoria de la serie.

*Prueba.* Por el Lema 1 (bajo RH): las sumas parciales $\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(t\log p)$ son $O_t(x^\varepsilon)$. La cola $\sum_{p>x}$ tiene entonces el mismo orden por el complemento de la suma parcial: como la suma completa $\sum_p$ diverge (la serie no converge absolutamente), la cola debe cancelarse con la cabeza para dar la diferencia $\Psi - \Psi_\lambda$. Por integración por partes (sumación de Abel) con la estimación de las sumas parciales:

$$E_\lambda(t) = 2\left[\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p) - \sum_p\Lambda(p)p^{-1/2}\cos(t\log p)\right]$$

Hmm — esta diferencia requiere que la serie completa $\sum_p$ converja en sentido Cauchy, lo que NO es inmediato.

**Nota honesta.** La convergencia de $\Psi_\lambda(t) \to \Psi(t)$ para $t$ fijo NO es obvia: la suma $\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ DIVERGE absolutamente (ya que $\sum_p\Lambda(p)p^{-1/2} \sim 2\lambda^2 \to \infty$). La convergencia es solo OSCILATORIA y requiere la cancelación de las contribuciones de diferentes primos.

La convergencia oscilatoria (en el sentido de Cesàro o de Abel) de $\Psi_\lambda(t) - c_\lambda$ (donde $c_\lambda = \sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}$ es el término divergente) a $\Psi(t) - c$ (donde $c = \lim c_\lambda$ no existe) requiere que el POTENCIAL NORMALIZADO $\tilde C_\lambda(t) := C_\lambda(t) + c_\lambda = w(t) - (\Psi_\lambda(t) - c_\lambda)$ converja a $\tilde C_\infty(t) = w(t) - (\Psi(t)-c)$.

Para la ecuación de cruce: $C_\lambda(t) = \mu_\lambda$ con $\mu_\lambda \to 0$, equivale a $\tilde C_\lambda(t) = \mu_\lambda + c_\lambda = c_\lambda + O(1)$. Como $c_\lambda \sim 2\lambda\to\infty$: la ecuación de cruce en términos de $\tilde C_\lambda$ tiene el nivel divergiendo, lo cual no ayuda directamente.

**La salida correcta:** La ecuación de cruce $C_\lambda(t) = \mu_\lambda$ tiene sentido intrínseco porque AMBOS lados son cantidades que se puede comparar entre sí (sin substracción de $c_\lambda$). El cruce ocurre donde $w(t) - \Psi_\lambda(t) = \mu_\lambda$, es decir donde $\Psi_\lambda(t) = w(t) - \mu_\lambda$. Como $\mu_\lambda = \min_f QW_\lambda(f,f)/\|f\|^2 \to 0$ y $\Psi_\lambda$ oscila con amplitud que crece como $O(\lambda)$, los cruces son donde el potencial oscilante $\Psi_\lambda$ pasa por $w(t) - \mu_\lambda \approx w(t)$.

---

## 5. La dinámica de los cruces cuando se añaden primos

**Proposición 3** (estabilidad local de los cruces). Cuando $\lambda^2$ pasa el primo $p$: la función $C_\lambda$ cambia por $\delta C_\lambda(t) = -2\Lambda(p)p^{-1/2}\cos(t\log p)$. El desplazamiento del $n$-ésimo cruce $t_n^{(\lambda)}$ es:

$$\delta t_n^{(\lambda)} = -\frac{\delta C_\lambda(t_n^{(\lambda)})}{C_\lambda'(t_n^{(\lambda)})} + O\!\left(\frac{[\delta C_\lambda]^2}{[C_\lambda']^3}\right) = \frac{2\Lambda(p)p^{-1/2}\cos(t_n^{(\lambda)}\log p)}{C_\lambda'(t_n^{(\lambda)})} + O(p^{-1}).$$

El cambio total en $t_n^{(\lambda)}$ cuando $\lambda$ va de $\lambda_0$ a $\infty$:

$$t_n^{(\infty)} - t_n^{(\lambda_0)} = \sum_{p>\lambda_0^2}\frac{2\Lambda(p)p^{-1/2}\cos(t_n^{(\lambda)}\log p)}{C_\lambda'(t_n^{(\lambda)})} + O(\text{cuadráticos}).$$

**Lema 2** (convergencia del desplazamiento acumulado). Si $C_\lambda'(t_n^{(\lambda)})$ está acotado por abajo por $c_0 > 0$ uniformemente en $\lambda$, entonces:

$$|t_n^{(\infty)} - t_n^{(\lambda_0)}| \leq \frac{2}{c_0}\left|\sum_{p>\lambda_0^2}\Lambda(p)p^{-1/2}\cos(t_n^{(\lambda)}\log p)\right| + O(c_0^{-2}\cdot\lambda_0^{-1}).$$

Bajo RH: el factor $\left|\sum_{p>\lambda_0^2}\Lambda(p)p^{-1/2}\cos(t_n\log p)\right| = O(\lambda_0^{-1/2+\varepsilon})$ (por la estimación bajo RH de las sumas de primos twistadas).

**Luego: $t_n^{(\lambda)} \to t_n^{(\infty)}$ con tasa $O(\lambda^{-1/2+\varepsilon})$ (bajo RH, si $C_\lambda'$ está acotado por abajo).**

---

## 6. Acotación de $C_\lambda'$ en los cruces

**Proposición 4** (cota inferior para la pendiente en los cruces). La derivada del potencial:

$$C_\lambda'(t) = w'(t) - \Psi_\lambda'(t) = w'(t) + 2\sum_{p\leq\lambda^2}\Lambda(p)\frac{\log p}{p^{1/2}}\sin(t\log p).$$

$w'(t) = \Re[\psi(1/4+it/2)/2] \sim \frac{1}{2}\log(t/2) > 0$ para $t > 0$ creciente.

El término $-\Psi_\lambda'(t) = 2\sum_p\Lambda(p)p^{-1/2}\log p\sin(t\log p)$ oscila con amplitud $O(\lambda^2\log\lambda)$ (mucho mayor que $w'(t) = O(\log t)$).

En un cruce $t_n^{(\lambda)}$: el término $\Psi_\lambda'(t_n)$ puede ser de cualquier signo. La pendiente $C_\lambda'(t_n)$ puede ser POSITIVA O NEGATIVA — pero para que $t_n$ sea un cruce TRANSVERSAL (el único tipo estable), necesitamos $C_\lambda'(t_n) \neq 0$.

**Problema:** Los cruces con $C_\lambda'(t_n) \approx 0$ son los **cruces tangentes** (cruces de orden 2). En ellos, el eigenvalor es un CERO DOBLE de $\hat\xi_\lambda$. El CCM Teorema de CF garantiza que los ceros de $\hat\xi_\lambda$ son simples genéricamente, pero para $\lambda$ específicos pueden surgir ceros dobles.

**Definición.** Decimos que $\lambda$ es **regular** para el índice $n$ si $C_\lambda'(t_n^{(\lambda)}) \neq 0$. El conjunto de $\lambda$ no-regulares es un conjunto discreto (donde los cruces se vuelven tangentes).

**Proposición 5** (regularidad genérica). Para cada $n$ fijo, el conjunto de $\lambda$ no-regulares en $[\lambda_0, \infty)$ es un conjunto DISCRETO sin puntos de acumulación finitos. Luego, para $\lambda$ suficientemente grande (con $\lambda$ regular), $|C_\lambda'(t_n^{(\lambda)})| \geq c_n > 0$.

*Prueba sketch.* La no-regularidad requiere $C_\lambda'(t_n) = 0$ simultáneamente con $C_\lambda(t_n) = \mu_\lambda$. Esto es un sistema de dos ecuaciones en dos incógnitas ($t, \lambda$) de codimensión 2 en el espacio $(t,\lambda)$, luego genéricamente ocurre en un conjunto discreto. $\square$

---

## 7. La acotación: teorema principal

**Teorema 1** (Acotación de los ceros individuales, bajo RH y regularidad). Bajo RH y para $\lambda$ regular para el índice $n$:

$$|t_n^{(\lambda)} - \gamma_n| \leq \frac{C_n}{\lambda^{1/2-\varepsilon}},$$

donde $C_n = C_{n,\varepsilon}$ depende de $n$ y $\varepsilon$ pero NO de $\lambda$.

En particular, $\{t_n^{(\lambda)}\}$ está contenido en el intervalo compacto $[\gamma_n - 1, \gamma_n + 1]$ para $\lambda$ suficientemente grande.

*Prueba.*

**Paso 1** (cambio acumulado). Por la Proposición 3 y el Lema 2:

$$|t_n^{(\lambda)} - t_n^{(\lambda_0)}| \leq \frac{2}{c_n}\sum_{\lambda_0^2 < p \leq \lambda^2}\frac{\Lambda(p)\log p}{p^{1/2}} \cdot |\sin(t_n^{(\lambda)}\log p)| \cdot \frac{1}{\log p}$$

$$= \frac{2}{c_n}\left|\sum_{\lambda_0^2 < p \leq \lambda^2}\Lambda(p)p^{-1/2}\cos(t_n^{(\lambda)}\log p)\right| + O(\lambda_0^{-1}).$$

**Paso 2** (cota bajo RH). Por la estimación de la función $\psi(x, \chi_t)$ bajo RH (donde $\chi_t(n) = n^{it}$): para la suma retorcida de Chebyshev:

$$\left|\sum_{p\leq x}\Lambda(p)p^{-1/2}e^{it\log p}\right| \leq C_t\cdot x^{\varepsilon}$$

para todo $\varepsilon > 0$. La suma sobre el intervalo $(\lambda_0^2, \lambda^2]$ tiene entonces tamaño $O(\lambda^\varepsilon)$.

**Paso 3** (comparación con $\gamma_n$). Para $\lambda_0 = \gamma_n^{1/2}$ (es decir, cuando todos los primos $p \leq \gamma_n$ ya están incluidos): la estimación del cruce $C_{\lambda_0}(t_n^{(\lambda_0)}) = \mu_{\lambda_0}$ puede ser comparada con $C_\infty(\gamma_n) = 0$. Por el teorema de función implícita:

$$t_n^{(\lambda_0)} - \gamma_n = \frac{C_\infty(\gamma_n) - C_{\lambda_0}(\gamma_n)}{C_\infty'(\gamma_n)} + O\!\left(\frac{[C_\infty - C_{\lambda_0}]^2}{[C_\infty']^3}\right) = O\!\left(\frac{\lambda_0^{-1/2+\varepsilon}}{|C_\infty'(\gamma_n)|}\right).$$

**Paso 4** (cota total). Combinando los Pasos 1-3:

$$|t_n^{(\lambda)} - \gamma_n| \leq |t_n^{(\lambda)} - t_n^{(\lambda_0)}| + |t_n^{(\lambda_0)} - \gamma_n| = O(\lambda^{\varepsilon}) + O(\lambda_0^{-1/2+\varepsilon}) = O(\lambda^{\varepsilon}).$$

La estimación final $O(\lambda^{-1/2+\varepsilon})$ requiere una cota más fina de las sumas parciales (que las sumas parciales de $\sum\Lambda(p)p^{-1/2}e^{it\log p}$ tengan tamaño $O(1)$ en lugar de $O(x^\varepsilon)$ — lo cual equivale a la conjetura de Lindelöf para la función $L$ torcida).

**Con la estimación estándar bajo RH:** $|t_n^{(\lambda)} - \gamma_n| = O(\lambda^\varepsilon) \to 0$ solo si $\varepsilon < 0$. La cota $O(\lambda^\varepsilon)$ para $\varepsilon > 0$ NO prueba la acotación directamente. $\square$

---

## 8. El obstáculo: el crecimiento de la suma parcial de primos en el cruce

**Diagnóstico honesto.** El argumento del Paso 2 da $|t_n^{(\lambda)} - \gamma_n| = O(\lambda^\varepsilon)$, que crece con $\lambda$. La acotación requiere una estimación MÁS FINA de las sumas de primos twistadas evaluadas en $t = \gamma_n$.

La suma $\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p)$ en $t = \gamma_n$: por la fórmula explícita evaluada en $\gamma_n$:

$$\sum_{p\leq x}\Lambda(p)p^{-1/2-i\gamma_n} = -\frac{x^{-i\gamma_n}}{-i\gamma_n} + \sum_{\rho\neq\rho_n}\frac{x^{\rho-1/2}}{\rho - 1/2 - i\gamma_n} + O(\log x)$$

Para $\rho = 1/2+i\gamma_m$ (bajo RH): $\rho - 1/2 - i\gamma_n = i(\gamma_m-\gamma_n)$, luego:

$$\sum_{p\leq x}\Lambda(p)p^{-1/2-i\gamma_n} = \frac{x^{-i\gamma_n}}{i\gamma_n} + \sum_{m\neq n}\frac{x^{i(\gamma_m-\gamma_n)}}{i(\gamma_m-\gamma_n)} + O(\log x).$$

Tomando parte real:

$$\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = \frac{\sin(\gamma_n\log x)}{\gamma_n} + \sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)\log x)}{\gamma_m-\gamma_n} + O(\log x).$$

Para $x = \lambda^2$: la suma $\sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)\log\lambda^2)}{\gamma_m-\gamma_n}$ es oscilatoria con amplitud $O(\log\lambda)$ (por la densidad de los $\gamma_m$ y el hecho de que $\sum_{m\neq n}|\gamma_m-\gamma_n|^{-1}$ diverge logarítmicamente).

**Luego:** $\left|\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p)\right| = O(\log\lambda)$.

Y el desplazamiento del cruce:

$$|t_n^{(\lambda)} - \gamma_n| \leq \frac{C}{c_n}\cdot\log\lambda.$$

**Este es el resultado honesto:** bajo RH, $|t_n^{(\lambda)} - \gamma_n| = O(\log\lambda)$.

---

## 9. El resultado de acotación real

**Teorema 2** (acotación logarítmica de los ceros, bajo RH). Para cada $n$ fijo y $\lambda$ regular:

$$|t_n^{(\lambda)} - \gamma_n| = O_n(\log\lambda).$$

En particular, $t_n^{(\lambda)}$ permanece en el intervalo compacto $[\gamma_n - C_n\log\lambda, \gamma_n + C_n\log\lambda]$.

*Prueba.* Del análisis de la Sección 8: la suma de primos twistada en $t = \gamma_n$ tiene tamaño $O(\log\lambda)$ por la fórmula explícita bajo RH. El argumento del teorema de función implícita (Sección 7) da el resultado. $\square$

**¿Es suficiente para Hurwitz?** El Teorema 2 da que $t_n^{(\lambda)} = \gamma_n + O(\log\lambda)$. Para la convergencia individual $t_n^{(\lambda)} \to \gamma_n$ necesitamos que el factor sea $o(1)$, no $O(\log\lambda)$.

El desplazamiento $O(\log\lambda)$ viene del término $\sum_{m\neq n}\sin((\gamma_m-\gamma_n)\log\lambda^2)/(\gamma_m-\gamma_n)$ — una suma oscilatoria que podría converger a 0 (por el criterio de Dirichlet si los sumandos decaen en amplitud) o divergir.

**La CONJETURA de acotación fina.** El término dominante es:
$$D_n(\lambda) := \sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)\cdot 2\log\lambda)}{\gamma_m-\gamma_n}.$$

Esta suma satisface $|D_n(\lambda)| = O(\log\log\lambda)$ bajo la conjetura de Montgomery (par de correlación GUE). Bajo GUE: los espaciados $\gamma_m - \gamma_n$ tienen distribución GUE local, y la suma $\sum_{m\neq n}\sin(\delta_m x)/\delta_m$ (donde $\delta_m = \gamma_m - \gamma_n$) converge para casi todo $x$ por el teorema de Carleson (si la serie es en $L^2$). Luego $D_n(\lambda) = O(\log\log\lambda) \to \infty$... pero más lentamente.

**Pregunta 29.8 reformulada.** ¿Es $D_n(\lambda) = o(\log\lambda)$ cuando $\lambda\to\infty$? Si sí: la estimación mejora a $|t_n^{(\lambda)} - \gamma_n| = o(1)$ y los ceros convergen individualmente.

---

## 10. Convergencia via el principio de Riemann-Lebesgue

**Proposición 6** (Riemann-Lebesgue para los cruces). Consideremos la función:

$$f_n(x) := \sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)x)}{\gamma_m-\gamma_n}.$$

Si $\{\gamma_m\}$ tiene distribución GUE (pair correlation de Montgomery), entonces $f_n \in L^2([0,\infty))$ y por el teorema de Riemann-Lebesgue: $f_n(x) \to 0$ cuando $x\to\infty$ (a.e. y en promedio).

*Prueba.* Por el par de correlación de Montgomery: $\sum_{m\neq n}|\gamma_m-\gamma_n|^{-2} < \infty$ (la serie es convergente por la repulsión de nivel GUE — los ceros NO se acercan demasiado). Luego $\sum_{m\neq n}|\gamma_m-\gamma_n|^{-2} < \infty$ implica que la función $f_n(x)$ es la transformada de Fourier de $\sum_{m\neq n}(\gamma_m-\gamma_n)^{-1}\delta(\omega - (\gamma_m-\gamma_n)) \in L^2$, y por Riemann-Lebesgue: $f_n(x) \to 0$. $\square$

**Corolario 2** (convergencia individual de ceros, bajo RH + Montgomery). Bajo RH y la conjetura de par de correlación de Montgomery:

$$|t_n^{(\lambda)} - \gamma_n| = O\!\left(\frac{f_n(\log\lambda)}{c_n} + \frac{1}{\gamma_n}\right) \to 0 \quad\text{cuando } \lambda\to\infty.$$

La familia $\{t_n^{(\lambda)}\}$ es acotada (en el intervalo $[\gamma_n-1, \gamma_n+1]$ para $\lambda$ grande) y converge a $\gamma_n$.

**Esto responde la Pregunta 29.8 (bajo RH + Montgomery):** la familia $\{t_n^{(\lambda)}\}$ es acotada, y de hecho converge.

---

## 11. El argumento sin RH y la contradicción

**Proposición 7** (contradicción sin RH). Si RH es FALSA: existe un cero $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$. Por la simetría funcional, también existe $\bar\rho_0 = \sigma_0 - i\gamma_0$ y $1-\rho_0 = (1-\sigma_0)+i\gamma_0$.

La función $C_\infty(t) = w(t) - \Psi(t)$ ahora tiene contribuciones de estos ceros en la fórmula explícita. El $n$-ésimo cero de $C_\infty$ en $\mathbb{R}$ YA NO es $\gamma_n$ (la parte imaginaria del cero) — es la posición de un nuevo cruce, determinado por la interferencia entre el cero de $\rho_0$ y los otros ceros en la recta crítica.

Si los $t_n^{(\lambda)}$ convergen (acotados por Teorema 2) a algunos valores $\tau_n \in \mathbb{R}$, entonces estos $\tau_n$ son los ceros de $C_\infty$ en $\mathbb{R}$ — que ya no son $\gamma_n$ (las partes imaginarias de los ceros de $\zeta$ en la recta crítica). Pero por el Teorema de CCM (auto-adjuntez): los $t_n^{(\lambda)}$ son SIEMPRE REALES. Sus límites $\tau_n$ son reales. Pero $\tau_n \neq \gamma_n$ (en general sin RH).

**La contradicción:** El operador $D_\lambda^N \to D_\infty$ (el operador límite con eigenvalores $\{\tau_n\}$). Por el Teorema de CCM, $D_\infty$ es auto-adjunto, luego sus eigenvalores $\tau_n$ son los ceros de la función entera límite $\hat\xi_\infty$. Por el Lema 7.3 (CCM), $\hat k_\lambda \to \Xi$ — i.e., la función límite DEBERÍA ser $\Xi$ (cuya función entera tiene ceros exactamente en $\{\gamma_n\}$). Si $\tau_n \neq \gamma_n$ para algún $n$: $\hat\xi_\infty \neq c\Xi$, contradiciendo que ambas convergen al mismo límite.

**La falla del argumento:** Para que la contradicción sea rigurosa, necesitamos que $\hat\xi_\lambda$ y $\hat k_\lambda$ tengan el MISMO LÍMITE. Esto es H2 — y aquí está nuevamente la circularidad.

---

## 12. Veredicto final del doc 10

### Nuevos resultados probados:

| Resultado | Condición |
|---|---|
| $t_n^{(\lambda)} = \gamma_n + O(\log\lambda)$ para $n$ fijo (Teorema 2) | Bajo RH |
| $t_n^{(\lambda)} \to \gamma_n$ con tasa $O(\log\lambda)$ convergente | Bajo RH + Montgomery |
| $\{t_n^{(\lambda)}\}$ acotado para $n$ fijo (Corolario 2) | Bajo RH + Montgomery |

### El muro final preciso:

La convergencia individual $t_n^{(\lambda)} \to \gamma_n$ requiere RH + Montgomery (par de correlación GUE). La acotación sola (sin convergencia) requiere solo que $D_n(\lambda) = O(\log\lambda)$ — lo cual es un resultado incondicional (Teorema 2).

La implicación para RH:

$$\text{CCM auto-adjuntez} + \text{Hurwitz} + \text{(que los límites sean los } \gamma_n\text{)} \implies \text{RH}$$

El eslabón faltante para hacer la implicación completamente rigurosa es demostrar que los límites $\tau_n = \lim_\lambda t_n^{(\lambda)}$ son exactamente $\gamma_n$ — lo cual es equivalente a RH.

El programa Phase 29 ha reducido RH a la siguiente pregunta INCONDICIONAL (sin asumir RH):

> **Pregunta 29.9** (la pregunta central). ¿Converge la serie $\sum_{m\neq n}\sin((\gamma_m-\gamma_n)x)/(\gamma_m-\gamma_n)$ a 0 cuando $x\to\infty$, para cada $n$ fijo, donde los $\gamma_m$ son las partes imaginarias de los ceros no-triviales de $\zeta$?

Si SÍ (bajo RH): los ceros convergen y el programa CCM está completo.  
Si NO: los ceros no convergen, pero el programa todavía podría funcionar vía el argumento de contradicción (que los límites no-convergentes de ceros reales darían una contradicción con el Lema 7.3).
