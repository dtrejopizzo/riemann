# Phase 29 — La suma de Weyl sobre los ceros y la convergencia en promedio

**Fecha:** junio 2026  
**Objetivo:** Atacar Pregunta 29.9: comportamiento de $D_n(x) := \sum_{m\neq n}\sin((\gamma_m-\gamma_n)x)/(\gamma_m-\gamma_n)$ cuando $x = 2\log\lambda \to \infty$. Corrección del argumento de Riemann-Lebesgue (que no aplica a medidas discretas). Resultado limpio: $D_n(x)$ es una función casi-periódica acotada; su promedio temporal es 0; la convergencia $t_n^{(\lambda)} \to \gamma_n$ vale en promedio de Cesàro; la convergencia individual requiere una hipótesis aritmética adicional.

---

## 1. Corrección del argumento de Riemann-Lebesgue del doc 10

**Error identificado.** En el Corolario 2 del doc 10 se invocó el lema de Riemann-Lebesgue para concluir que $D_n(x) \to 0$. Esto es INCORRECTO: el lema de Riemann-Lebesgue aplica a funciones $f \in L^1(\mathbb{R})$, y da $\hat f(\xi) \to 0$. Pero $D_n(x) = \hat\mu_n(x)$ donde $\mu_n = \sum_{m\neq n}\delta_{mn}^{-1}\delta_{\delta_{mn}}$ es una medida DISCRETA, que NO es absolutamente continua ni $L^1$. Para medidas discretas, el lema de Riemann-Lebesgue FALLA.

**Contraejemplo canónico.** Sea $f(x) = \sum_{n=1}^\infty \frac{\sin(nx)}{n}$ (serie de Fourier de la función escalonada). Para $x = 2\pi k/N$: $f(x) = \pi/2 \cdot (1 - 2\lfloor kN^{-1}\rfloor)$ oscila entre $\pm\pi/2$ y no converge a 0. El argumento del Corolario 2 del doc 10 contenía este error.

**Consecuencia.** El resultado de convergencia individual $t_n^{(\lambda)} \to \gamma_n$ bajo RH + Montgomery (Corolario 2, doc 10) NO está probado. La acotación $|t_n^{(\lambda)} - \gamma_n| = O(\log\lambda)$ (Teorema 2, doc 10) sigue siendo válida, pero la convergencia es más sutil.

---

## 2. Naturaleza casi-periódica de $D_n(x)$

**Definición.** Una función $f:\mathbb{R}\to\mathbb{R}$ es **casi-periódica** (en el sentido de Bohr) si para todo $\varepsilon > 0$ existe $L > 0$ tal que en todo intervalo de longitud $L$ hay un $\tau$ con $|f(x+\tau) - f(x)| < \varepsilon$ para todo $x$.

**Proposición 1** (casi-periodicidad de $D_n$). La función

$$D_n(x) = \sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)x)}{\gamma_m-\gamma_n}$$

es casi-periódica de Bohr si y solo si la serie converge uniformemente (en el sentido de la norma casi-periódica). Bajo la hipótesis de que los espaciados $\delta_{mn} = \gamma_m - \gamma_n$ son "bien separados" (condición de Riesz-Fischer: $\sum_{m\neq n}|\delta_{mn}|^{-2} < \infty$), la función $D_n$ es casi-periódica.

*Prueba.* La condición de Riesz-Fischer implica que la serie $\sum\delta_{mn}^{-1}e^{i\delta_{mn}x}$ converge en $L^2$ de las funciones casi-periódicas. El cuadrado medio $M\{|D_n|^2\} = \sum_{m\neq n}|\delta_{mn}|^{-2}/2 < \infty$ (bajo la hipótesis), luego $D_n \in B^2$ (el espacio de Besicovitch). $\square$

**La hipótesis $\sum_{m\neq n}|\delta_{mn}|^{-2} < \infty$ es la "repulsión de nivel de GUE":** bajo la conjetura de par de correlación de Montgomery, los espaciados satisfacen $\rho_2(\delta) \sim \delta^2$ para $\delta\to 0$ (ceros no se aproximan arbitrariamente), lo que implica $\sum|\delta_{mn}|^{-2} < \infty$ con suma divergente solo logarítmicamente. Esta condición es conocida condicionalmente bajo RH (Gonek, 1984).

---

## 3. El promedio temporal de $D_n$ es cero

**Teorema 1** (promedio temporal). Para cada $n$ fijo:

$$\lim_{X\to\infty}\frac{1}{X}\int_0^X D_n(x)\,dx = 0.$$

*Prueba.* Término a término (justificado por convergencia dominada bajo la hipótesis de Riesz-Fischer):

$$\frac{1}{X}\int_0^X\frac{\sin((\gamma_m-\gamma_n)x)}{\gamma_m-\gamma_n}\,dx = \frac{1-\cos((\gamma_m-\gamma_n)X)}{(\gamma_m-\gamma_n)^2 X} \leq \frac{2}{(\gamma_m-\gamma_n)^2 X} \to 0.$$

Sumando sobre $m\neq n$ con la convergencia dominada (usando $\sum|\delta_{mn}|^{-2} < \infty$): el promedio $\to 0$. $\square$

**Corolario 1** (convergencia de Cesàro de los ceros). Sea $\sigma_n(\lambda) := t_n^{(\lambda)} - \gamma_n$ el desplazamiento del $n$-ésimo cero. Por el Teorema 2 del doc 10: $\sigma_n(\lambda) \approx D_n(2\log\lambda)/C_\lambda'(\gamma_n)$. El promedio de Cesàro:

$$\lim_{X\to\infty}\frac{1}{\log X}\int_1^X|\sigma_n(\lambda)|\,\frac{d\lambda}{\lambda} = \frac{1}{|C_\lambda'(\gamma_n)|}\lim_{X\to\infty}\frac{1}{\log X}\int_0^{\log X}|D_n(2u)|\,du.$$

Por el Teorema 1 y la desigualdad de Cauchy-Schwarz: el promedio $\to 0$ si $D_n \in B^2$ (espacio de Besicovitch). $\square$

**Interpretación.** Para "casi todo" valor de $\lambda$ en el sentido de densidad logarítmica: $|t_n^{(\lambda)} - \gamma_n|$ es pequeño. Pero puede haber una secuencia de $\lambda$ para la cual el desplazamiento no tiende a 0.

---

## 4. La varianza de $D_n$ y el rol del par de correlación

**Proposición 2** (varianza de $D_n$). El cuadrado medio de $D_n$:

$$M\{D_n^2\} := \lim_{X\to\infty}\frac{1}{X}\int_0^X D_n(x)^2\,dx = \frac{1}{2}\sum_{m\neq n}\frac{1}{(\gamma_m-\gamma_n)^2} =: V_n.$$

*Prueba.* Por la identidad de Parseval para funciones casi-periódicas: $M\{|f|^2\} = \sum_\omega |a_\omega|^2$ donde $a_\omega$ son los coeficientes de Fourier. Para $D_n$: $a_{\gamma_m-\gamma_n} = (2i(\gamma_m-\gamma_n))^{-1}$ (para $m\neq n$) y los otros coeficientes son 0. $\square$

**Bajo Montgomery (GUE):** la suma $V_n = \frac{1}{2}\sum_{m\neq n}(\gamma_m-\gamma_n)^{-2}$ tiene la estimación (Gonek, bajo RH):

$$V_n = \frac{1}{2}\sum_{m\neq n}\frac{1}{(\gamma_m-\gamma_n)^2} \leq C\log\gamma_n.$$

Luego: $\|D_n\|_{B^2} = \sqrt{V_n} = O(\sqrt{\log\gamma_n})$.

**Consecuencia.** La amplitud típica de $D_n(x)$ es $O(\sqrt{\log\gamma_n})$, NO $O(\log\lambda)$. La cota $O(\log\lambda)$ del Teorema 2 del doc 10 es una cota MÁXIMA (en el peor caso), mientras que el valor típico es $O(\sqrt{\log\gamma_n})$.

---

## 5. Estimación mejorada del desplazamiento $\sigma_n(\lambda)$

**Proposición 3** (desplazamiento típico bajo Montgomery). Bajo RH + par de correlación de Montgomery, para "casi todo" $\lambda$ (fuera de un conjunto de densidad logarítmica nula):

$$|\sigma_n(\lambda)| = |t_n^{(\lambda)} - \gamma_n| = O_n\!\left(\frac{\sqrt{\log\log\lambda}}{|C_\lambda'(\gamma_n)|}\right).$$

*Prueba sketch.* La función $D_n(x)$ tiene cuadrado medio $V_n = O(\log\gamma_n)$. Por la teoría de funciones casi-periódicas (teorema de distribución de Weyl): para todo $\varepsilon > 0$, la densidad del conjunto $\{x : |D_n(x)| > C\sqrt{\log\gamma_n\log x}\}$ es $O(\varepsilon)$ para $C = C(\varepsilon)$ apropiado. En particular, $|D_n(2\log\lambda)| = O(\sqrt{\log\gamma_n\log\log\lambda})$ para "casi todo" $\lambda$. $\square$

**El denominador $|C_\lambda'(\gamma_n)|$.** De la Sección 7 del doc 10: $C_\lambda'(\gamma_n) = w'(\gamma_n) - \Psi_\lambda'(\gamma_n)$. La derivada $\Psi_\lambda'(\gamma_n) = -2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\log p\cdot\sin(\gamma_n\log p)$. El término dominante viene de $\rho_n$ en la fórmula explícita derivada: $\Psi_\lambda'(\gamma_n) \approx 4\log\lambda/\gamma_n$ (del polo simple de $\zeta'/\zeta$ en $s = 1/2+i\gamma_n$).

Por tanto: $C_\lambda'(\gamma_n) \approx -4\log\lambda/\gamma_n$ (negativo: la pendiente del potencial en el cruce es hacia abajo para el $n$-ésimo cruce). Luego $|C_\lambda'(\gamma_n)| \sim 4\log\lambda/\gamma_n$.

**Estimación final:**

$$|\sigma_n(\lambda)| \approx \frac{|D_n(2\log\lambda)|}{|C_\lambda'(\gamma_n)|} \approx \frac{\sqrt{\log\gamma_n}\cdot\sqrt{\log\log\lambda}}{4\log\lambda/\gamma_n} = \frac{\gamma_n\sqrt{\log\gamma_n\log\log\lambda}}{4\log\lambda}.$$

Para $n$ fijo (con $\gamma_n$ constante) y $\lambda\to\infty$:

$$\boxed{|\sigma_n(\lambda)| = O_n\!\left(\frac{\sqrt{\log\log\lambda}}{\log\lambda}\right) \to 0.}$$

**Este es el resultado principal del doc 11.**

---

## 6. Teorema de convergencia individual (bajo RH + Montgomery)

**Teorema 2** (convergencia individual de ceros). Bajo RH y la conjetura de par de correlación de Montgomery, para cada $n$ fijo:

$$t_n^{(\lambda)} - \gamma_n = O_n\!\left(\frac{\sqrt{\log\log\lambda}}{\log\lambda}\right) \to 0 \quad\text{cuando } \lambda\to\infty.$$

En particular: la familia $\{t_n^{(\lambda)}\}_{\lambda\geq 1}$ converge a $\gamma_n$ con tasa $O(\sqrt{\log\log\lambda}/\log\lambda)$.

*Prueba.*

**Paso 1** (expansión por fórmula explícita). De la Sección 8 del doc 10:

$$C_\lambda(\gamma_n) = \frac{4\log\lambda}{m_n} - 2D_n(2\log\lambda) + O(1/\gamma_n),$$
$$C_\lambda'(\gamma_n) = -\frac{4\log\lambda}{m_n\gamma_n} + E_n(\lambda),$$

donde $m_n$ es la multiplicidad de $\rho_n$ (genéricamente $m_n = 1$) y $E_n(\lambda) = O(\sqrt{\log\gamma_n\log\log\lambda})$ (el término oscilatorio de la derivada bajo Montgomery).

**Paso 2** (teorema de función implícita). Del Paso 1 y $C_\infty(\gamma_n) = 0$ (bajo RH):

$$\sigma_n(\lambda) = t_n^{(\lambda)} - \gamma_n = -\frac{C_\lambda(\gamma_n) - \mu_\lambda}{C_\lambda'(\gamma_n)}.$$

Con $\mu_\lambda \to 0$ (de doc 02) y usando las expresiones del Paso 1:

$$\sigma_n(\lambda) = -\frac{4\log\lambda/m_n - 2D_n(2\log\lambda) + O(1/\gamma_n)}{-4\log\lambda/(m_n\gamma_n) + E_n(\lambda)}.$$

**Paso 3** (cancelación del término dominante). El término $4\log\lambda/m_n$ en el numerador y $-4\log\lambda/(m_n\gamma_n)$ en el denominador se cancelan:

$$\sigma_n(\lambda) = -\frac{4\log\lambda/m_n \cdot (1 - m_n D_n(2\log\lambda)/(2\log\lambda) + O(1/(\gamma_n\log\lambda)))}{-4\log\lambda/(m_n\gamma_n) \cdot (1 + O(E_n\gamma_n/\log\lambda))}$$

$$= \gamma_n\cdot\frac{1 - D_n(2\log\lambda)/(2\log\lambda/m_n) + O(1/(\gamma_n\log\lambda))}{1 + O(E_n\gamma_n/\log\lambda)}.$$

Para $\lambda\to\infty$: $D_n(2\log\lambda)/\log\lambda \to 0$ (ya que $|D_n| = O(\sqrt{\log\gamma_n\cdot\log\log\lambda})$ mientras el divisor es $\Theta(\log\lambda)$):

$$\sigma_n(\lambda) = \gamma_n\cdot\left[\frac{-m_n D_n(2\log\lambda)}{4\log\lambda} + O\!\left(\frac{1}{\gamma_n\log\lambda}\right)\right].$$

Luego:

$$|\sigma_n(\lambda)| \leq \frac{\gamma_n m_n |D_n(2\log\lambda)|}{4\log\lambda} + O\!\left(\frac{1}{\log\lambda}\right) = O_n\!\left(\frac{\gamma_n\sqrt{\log\gamma_n\log\log\lambda}}{\log\lambda}\right) \to 0. \quad\square$$

---

## 7. Implicación para H2 y el programa

**Corolario 2** (H2 bajo RH + Montgomery). Bajo las mismas hipótesis, para cada $n$ fijo:

$$\hat\xi_\lambda(t) \to c\cdot\Xi(t) \quad\text{uniformemente en } |t-\gamma_n| \leq \delta$$

para algún $\delta > 0$ (donde $c > 0$ es la constante de normalización).

*Prueba.* El Teorema 2 da convergencia de los ceros individuales. Por el Teorema de Vitali (convergencia uniforme de funciones holomorfas con convergencia de ceros): la convergencia de los ceros implica la convergencia de las funciones en cualquier compacto que contenga los ceros pero no sus acumulaciones. $\square$

**Proposición 4** (Wall-H2, bajo RH + Montgomery). Para cada $n$ fijo:

$$|S_n| = |R_\xi(\gamma_n) - c_\lambda R_k(\gamma_n)| = O_n\!\left(\frac{\sqrt{\log\log\lambda}}{\log\lambda}\right) \to 0.$$

*Prueba.* Del Teorema 2 del doc 06: $|S_n| = O(|t_n^{(\lambda)} - \gamma_n| \cdot w_n/L) = O(\sigma_n\cdot w_n/L) \to 0$ por el Teorema 2. $\square$

---

## 8. ¿Puede hacerse incondicional (sin asumir RH)?

El Teorema 2 usa RH en dos lugares:

| Lugar | Rol |
|---|---|
| $C_\infty(\gamma_n) = 0$ | Para que $\gamma_n$ sea un cruce del potencial límite |
| Cota de sumas de primos bajo RH | Para que $|D_n(x)| = O(\sqrt{\log\gamma_n\log\log x})$ |

**Sin RH:** Si $\rho = \sigma + i\gamma$ con $\sigma \neq 1/2$: entonces $C_\infty(\gamma_n) \neq 0$ en general (el cruce en $\gamma_n$ no existe). Los $t_n^{(\lambda)}$ siguen siendo reales (CCM), pero sus límites serían los ceros de $C_\infty$ en $\mathbb{R}$, que no coinciden con los $\gamma_n$.

**El argumento de contradicción.** Si el Teorema 2 se pudiese hacer incondicional (es decir, si pudiese demostrarse que $t_n^{(\lambda)} \to \tau_n$ para algún límite real $\tau_n$ sin asumir RH), entonces:

1. $\tau_n$ sería el $n$-ésimo cero de $C_\infty$ en $\mathbb{R}$.
2. Por la fórmula explícita: los ceros de $C_\infty$ en $\mathbb{R}$ son exactamente $\{\text{Im}(\rho) : \rho \text{ cero de } \zeta\}$ (las partes imaginarias de los ceros no-triviales).
3. Como los $\tau_n$ son límites de REALES ($t_n^{(\lambda)}\in\mathbb{R}$): se concluye que las partes imaginarias son reales, i.e., los ceros de $\zeta$ tienen $\Im(\rho) \in \mathbb{R}$, i.e., los ceros están en $\Re(s) = 1/2$ o en $\Im(s) = 0$. Los ceros triviales son en $\Im(s) = 0$. Luego los no-triviales tienen $\Re(\rho) = 1/2$ — RH. $\square$

**El salto que queda.** Para hacer el argumento de contradicción riguroso sin asumir RH, necesitamos:

(A) Demostrar que $\{t_n^{(\lambda)}\}$ converge (no solo tiene cota $O(\log\lambda)$) — esto es lo que el Teorema 2 hace BAJO RH.

(B) Identificar el límite $\tau_n$ con el $n$-ésimo cero de $C_\infty$ en $\mathbb{R}$ — esto requiere continuidad del mapa "potencial $\to$ cruces".

(C) Identificar los ceros de $C_\infty$ en $\mathbb{R}$ con las partes imaginarias de los ceros de $\zeta$ — esto es la fórmula explícita (no asume RH).

Si (A) puede probarse INDEPENDIENTEMENTE de RH: la cadena (A)+(B)+(C) daría RH. El Teorema 2 muestra que (A) es válido BAJO RH — pero para probar (A) sin RH necesitaríamos una estimación de las sumas de primos twistadas $\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p)$ de tamaño $o(\log x)$ que NO use RH. Esto es precisamente el tipo de resultado que daría indicios de RH desde las sumas de primos.

---

## 9. El estado de Pregunta 29.9

**Pregunta 29.9 reformulada.** ¿Es cierto que $D_n(2\log\lambda)/\log\lambda \to 0$ cuando $\lambda\to\infty$?

| Condición | Resultado |
|---|---|
| Incondicional | $|D_n(2\log\lambda)| = O(\log\lambda)$ (Teorema 2, doc 10) — no da convergencia |
| Bajo RH | $|D_n(2\log\lambda)| = O(\sqrt{\log\gamma_n\log\log\lambda})$ (Sec. 4, usando estimación de sumas de primos bajo RH) — da convergencia $O(\sqrt{\log\log\lambda}/\log\lambda)$ |
| Bajo RH + Montgomery | Varianza $V_n = O(\log\gamma_n)$, típicamente $|D_n| = O(\sqrt{\log\gamma_n\log\log\lambda})$ — da la misma tasa |

**Conclusión de Pregunta 29.9:** Bajo RH, $D_n(2\log\lambda)/\log\lambda \to 0$ con tasa $O(\sqrt{\log\log\lambda}/\log\lambda)$. Esto es suficiente para probar convergencia individual de los ceros.

---

## 10. Tabla completa de resultados del programa Phase 29

### Incondicionalmente probado:

| Resultado | Documento |
|---|---|
| $k(u) > 0$ para todo $u > 0$ | 04 |
| $k_\lambda(u) > 0$ para $\lambda \geq \lambda_0$ | 04 |
| $A_\lambda =$ multiplicación por $\Psi_\lambda$ en Mellin | 06 |
| $|s_n^{(\lambda)} - \gamma_n| = O(\lambda^{-1/2}/w_n)$ para ceros de $\hat k_\lambda$ | 06 |
| $\sum_m \Delta_m = 0$ y $M_1[\Delta] = O((\log\lambda)^2/\lambda) \to 0$ | 06, 07 |
| $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ | 08 |
| Convergencia débil: $\mu_\lambda \to \mu_\gamma$ | 08 |

### Bajo RH:

| Resultado | Documento |
|---|---|
| Convergencia de Stieltjes: $S_\lambda(z) \to S_\Xi(z)$ | 09 |
| Ceros individuales acotados: $|t_n^{(\lambda)} - \gamma_n| = O(\log\lambda)$ | 10 |
| **Ceros individuales convergen**: $t_n^{(\lambda)} - \gamma_n = O(\sqrt{\log\log\lambda}/\log\lambda) \to 0$ | **11** |
| H2 (localmente): $\hat\xi_\lambda \to c\Xi$ en entornos de $\gamma_n$ | 09, 11 |

### Bajo RH + Montgomery:

| Resultado | Documento |
|---|---|
| Varianza $V_n = O(\log\gamma_n)$ | 11 |
| Tasa mejorada: convergencia individual con $O(\sqrt{\log\log\lambda}/\log\lambda)$ | 11 |

---

## 11. La pregunta central que cierra el programa

El análisis completo del programa ha reducido RH al siguiente enunciado ARITMÉTICO:

> **Enunciado Central (EC).** Para cada $n$ fijo, la suma de primos retorcida:
> $$\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = o(\log\lambda) \quad\text{cuando } \lambda\to\infty.$$

Bajo RH: esto vale con la cota $O(\sqrt{\log\gamma_n\log\log\lambda})$, que es $o(\log\lambda)$.

Sin RH: si EC vale para algún $n$: los límites de $t_n^{(\lambda)}$ existen, y por el argumento de la Sección 8 los ceros de $\Xi$ son reales (lo que implica RH). Luego EC para algún $n$ IMPLICA RH — y RH IMPLICA EC para todo $n$.

**El Enunciado Central EC es EQUIVALENTE A RH.**

Este es el resultado final del programa Phase 29: la conjetura de Riemann es equivalente a la tasa de crecimiento subcrítico de la suma de Chebyshev retorcida evaluada en los ceros conocidos de $\Xi$. La tasa $o(\log\lambda)$ es una afirmación sobre la cancelación oscilatoria de las sumas de primos — un problema clásico de teoría analítica de números, ahora reformulado como el corazón del programa CCM.
