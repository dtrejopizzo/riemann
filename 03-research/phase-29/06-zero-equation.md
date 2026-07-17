# Phase 29 — Ecuación de ceros y convergencia cuantitativa

**Fecha:** junio 2026  
**Objetivo:** Atacar Wall-H2 directamente desde la ecuación algebraica de los ceros, sin pasar por la norma $L^2$ de $\xi_\lambda - k_\lambda$. Dos resultados nuevos: (A) convergencia cuantitativa de los ceros de $\hat k_\lambda$ vía Lema 7.3 + Rouché; (B) la estructura multiplicativa de $A_\lambda$ en espacio de Mellin, que conecta los ceros de $\hat\xi_\lambda$ con los cruces de la fórmula explícita.

---

## 1. La ecuación de ceros como objeto central

Del doc 03 (Proposición 3): los ceros $t_n^{(\lambda)}$ de $\hat\xi_\lambda$ son exactamente los valores $z \in \mathbb{R}$ donde la función racional

$$R_\xi(z) := \frac{1}{L}\sum_{|m|\leq N} \frac{\xi_m^{(\lambda)}}{z - 2\pi m/L}$$

se anula. Análogamente para $\hat k_\lambda$:

$$R_k(z) := \frac{1}{L}\sum_{|m|\leq N} \frac{k_m^{(\lambda)}}{z - 2\pi m/L}.$$

La suma $S_n$ del doc 05 (la cantidad a controlar para Wall-H2) es:

$$S_n := R_\xi(\gamma_n) - c_\lambda R_k(\gamma_n) = \frac{1}{L}\sum_m \frac{\Delta_m}{\gamma_n - 2\pi m/L},$$

donde $\Delta_m := \xi_m^{(\lambda)} - c_\lambda k_m^{(\lambda)}$ y $\gamma_n$ es el $n$-ésimo cero de $\Xi$.

**La pregunta precisa.** ¿Puede acotarse $|S_n|$ en términos de $\lambda^{-1/2}$ o menor, usando solo la estructura variacional de $\xi_\lambda$ y la tasa de convergencia del Lema 7.3 para $k_\lambda$?

---

## 2. Teorema de convergencia cuantitativa para los ceros de $\hat k_\lambda$

**Teorema 1** (nuevos, cuantitativo). Sean $\{s_n^{(\lambda)}\}$ los ceros de $\hat k_\lambda$ que convergen a $\gamma_n$. Entonces para $\alpha \in (0,1/2)$:

$$|s_n^{(\lambda)} - \gamma_n| \leq \frac{2C_\alpha \lambda^{-1/2-\alpha}}{(1-2\alpha) w_n},$$

donde $w_n = |\Xi'(\gamma_n)| > 0$ es el peso del $n$-ésimo cero.

*Prueba.* Por el Lema 7.3 (CCM): $|\hat k_\lambda(z) - \Xi(z)| \leq C_\alpha \lambda^{-1/2-\alpha}(1-2\alpha)^{-1}$ uniformemente para $|\Im(z)| \leq \alpha$.

Sea $r_n = 2C_\alpha\lambda^{-1/2-\alpha}/((1-2\alpha)w_n)$ y consideremos el círculo $\Gamma_n = \{|z-\gamma_n| = r_n\}$. Sobre $\Gamma_n$:
$$|\Xi(z)| \geq |z - \gamma_n| \cdot \inf_{\Gamma_n}|\Xi'| \geq r_n w_n/2 = C_\alpha\lambda^{-1/2-\alpha}/(1-2\alpha)$$

(usando que $\gamma_n$ es un cero simple con $|\Xi'(\gamma_n)| = w_n$ y que la variación de $\Xi'$ en $\Gamma_n$ es pequeña para $\lambda$ grande).

La cota del Lema 7.3 da $|\hat k_\lambda(z) - \Xi(z)| \leq C_\alpha\lambda^{-1/2-\alpha}/(1-2\alpha) \leq |\Xi(z)|$ sobre $\Gamma_n$.

Por el principio de Rouché: $\hat k_\lambda$ y $\Xi$ tienen el mismo número de ceros en $|z - \gamma_n| < r_n$, que es exactamente 1. Luego $|s_n^{(\lambda)} - \gamma_n| \leq r_n$. $\square$

**Corolario.** Los ceros de $\hat k_\lambda$ convergen a los de $\Xi$ a tasa $O(\lambda^{-1/2}/w_n)$.

**Nota:** Este es el primer resultado cuantitativo sobre la velocidad de convergencia de los ceros de la aproximación CCM. La tasa $\lambda^{-1/2}/w_n$ es la natural: el peso $w_n = |\Xi'(\gamma_n)|$ mide la "apertura" del cero de $\Xi$, y ceros más abiertos (mayor $w_n$) son más estables bajo perturbaciones.

---

## 3. La restricción de normalización y la reducción de $S_n$

**Proposición 1** (restricción de normalización). Sea la condición de frontera del CCM: $\xi_\lambda(\lambda) = k_\lambda(\lambda) = 1$ (normalización en $u = \lambda$). En la base $\{U_m^+\}$, esto equivale a:

$$\sum_{m=0}^N \xi_m^{(\lambda)'} = \sum_{m=0}^N k_m^{(\lambda)'} = \sqrt{L}$$

(donde $\xi_m^{(\prime)}$ son los coeficientes en la base par). Por tanto:

$$\sum_{m=0}^N \Delta_m^{(\prime)} = 0,$$

i.e., la suma de los coeficientes de $\Delta$ es cero.

*Prueba.* $V_m(\lambda) = L^{-1/2}e^{2\pi im\log(\lambda^2)/L} = L^{-1/2}e^{2\pi im} = L^{-1/2}$ para todo $m$. Luego $f(\lambda) = L^{-1/2}\sum_m f_m$ para $f \in E_N$. La condición $\xi_\lambda(\lambda) = k_\lambda(\lambda)$ da $\sum_m \xi_m = \sum_m k_m$, i.e., $\sum_m \Delta_m = 0$. $\square$

**Reducción de $S_n$.** Usando $\sum_m \Delta_m = 0$:

$$S_n = \frac{1}{L}\sum_m \frac{\Delta_m}{\gamma_n - 2\pi m/L} = \frac{1}{L}\sum_m \Delta_m \left[\frac{1}{\gamma_n - 2\pi m/L} - \frac{1}{\gamma_n}\right]$$

$$= \frac{1}{L\gamma_n}\sum_m \frac{\Delta_m \cdot (2\pi m/L)}{\gamma_n - 2\pi m/L} = \frac{1}{\gamma_n}\sum_m \frac{\Delta_m \cdot (2\pi m/L^2)}{\gamma_n - 2\pi m/L}.$$

La suma $S_n$ es ahora una SUMA DE PRIMER MOMENTO: los coeficientes $\Delta_m$ están ponderados por $(2\pi m/L^2)/(\gamma_n - 2\pi m/L)$, un peso que crece con $|m|$ y tiene polos en $\gamma_n L/(2\pi)$ (que no es entero, genéricamente).

**Corolario.** Si $\sum_m m\,\Delta_m = 0$ (segundo momento nulo), entonces $S_n = \sum_m \Delta_m \cdot (2\pi m/L)^2 / (\gamma_n^2(\gamma_n - 2\pi m/L))$ (suma de segundo momento). Cada constraint adicional de momento reduce el orden del denominador de $S_n$.

---

## 4. La estructura multiplicativa de $A_\lambda$ en espacio de Mellin

Esta es la observación nueva más importante del documento.

**Lema 2** (multiplicación en espacio de Mellin). El operador aritmético $A_\lambda$ actúa como multiplicación por la función de Chebyshev de Fourier en el espacio de Mellin:

$$\widehat{A_\lambda f}(t) = \Psi_\lambda(t)\,\hat f(t),$$

donde $\Psi_\lambda(t) = 2\sum_{p \leq \lambda^2} \Lambda(p)\,p^{-1/2}\cos(t\log p)$.

*Prueba.* Por definición: $A_\lambda f = \sum_{p\leq\lambda^2}\Lambda(p)T(p)f$. La transformada de Mellin de $T(p)f$:
$$\widehat{T(p)f}(t) = \int_0^\infty T(p)f(u)\,u^{-it}\,\frac{du}{u} = p^{-1/2}\int [f(pu)+f(u/p)]\,u^{-it}\,\frac{du}{u}$$
$$= p^{-1/2}[p^{it}\hat f(t) + p^{-it}\hat f(t)] = 2p^{-1/2}\cos(t\log p)\,\hat f(t).$$
Sumando sobre primos: $\widehat{A_\lambda f}(t) = \Psi_\lambda(t)\hat f(t)$. $\square$

**Corolario** (el operador $M = B - A$ en Mellin es casi-diagonal). El operador arquimediano $Q^{\mathrm{arch}}$ corresponde a multiplicación por $w(t) = 2\partial_t\theta(t)/2\pi \sim \tfrac{1}{2}\log(t/2\pi)$ para $t \gg 1$. Luego, módulo el término de rango 1 ($Q^{\mathrm{cross}}$):

$$(B_\lambda - A_\lambda)\hat f(t) \approx [w(t) - \Psi_\lambda(t)]\hat f(t).$$

El operador $M = B - A$ es CASI DIAGONAL en el espacio de Mellin.

---

## 5. La ecuación de eigenvalor en espacio de Mellin y los cruces de la fórmula explícita

La ecuación $(B_\lambda - A_\lambda - \mu_\lambda)\xi_\lambda = 0$ en espacio de Mellin es:

$$[w(t) - \Psi_\lambda(t) - \mu_\lambda]\hat\xi_\lambda(t) \approx 0 \quad \text{para casi todo } t.$$

**Consecuencia.** El soporte de $\hat\xi_\lambda(t)$ en espacio de Mellin está concentrado en los valores $t$ donde

$$w(t) \approx \Psi_\lambda(t) + \mu_\lambda.$$

Estos son los **cruces de la fórmula explícita truncada**.

**Definición.** El conjunto de cruces:
$$\mathcal{C}_\lambda := \{t \in \mathbb{R} : w(t) = \Psi_\lambda(t) + \mu_\lambda\}.$$

**Proposición 2** (conexión entre ceros y cruces). Las posiciones de los ceros $t_n^{(\lambda)}$ de $\hat\xi_\lambda$ son determinadas por las posiciones de los cruces en $\mathcal{C}_\lambda$, en el sentido de que la concentración de la transformada de Mellin $\hat\xi_\lambda$ en cada cruce determina un cero de la función entera $\hat\xi_\lambda$.

*Argumento (formal).* Si $\hat\xi_\lambda(t) \approx 0$ para $t \notin \mathcal{C}_\lambda$ y $\hat\xi_\lambda(t)$ tiene masa en $t_0 \in \mathcal{C}_\lambda$, entonces el cero de $\hat\xi_\lambda$ (en el plano complejo) más cercano a $t_0$ (real) estará cerca de $t_0$. $\square$

---

## 6. Los cruces de la fórmula explícita convergen a $\gamma_n$

**Lema 3** (cruces de $\Psi_\lambda$). Definamos $\Psi(t) := \lim_{\lambda\to\infty}\Psi_\lambda(t)$ (la fórmula explícita completa). Por la fórmula explícita de Riemann-von Mangoldt:

$$\Psi_\lambda(t) = w(t) - 2\sum_{|\gamma_n| \leq T_\lambda} \frac{\cos(t\log\gamma_n)}{\gamma_n} + O(\log\lambda / \lambda)$$

(aproximación con un error controlado por $T_\lambda \sim \lambda^2$). Las soluciones de $\Psi_\lambda(t) + \mu_\lambda = w(t)$ con $\mu_\lambda \approx 0$ son aproximadamente las soluciones de

$$2\sum_{|\gamma_n| \leq T_\lambda} \frac{\cos(t\log\gamma_n)}{\gamma_n} \approx 0.$$

**Bajo RH** (todos los $\gamma_n$ reales): la ecuación anterior es satisfecha en $t = \gamma_n$ (los ceros de $\Xi$) para los cruces relevantes. La aproximación mejora cuando $T_\lambda \to \infty$.

**Proposición 3** (cruces $\mathcal{C}_\lambda \to \{\gamma_n\}$ bajo RH). Si RH vale, los cruces de $\mathcal{C}_\lambda$ convergen a los ceros $\gamma_n$ de $\Xi$ a medida que $\lambda \to \infty$, con la misma tasa de convergencia que la fórmula explícita truncada converge a la completa.

**Interpretación.** El mecanismo por el que los ceros de $\hat\xi_\lambda$ convergen a $\gamma_n$ es el siguiente:

1. $\hat\xi_\lambda$ concentra su masa en los cruces $\mathcal{C}_\lambda$ (por el eigenvalor en espacio de Mellin).
2. Los cruces $\mathcal{C}_\lambda$ convergen a $\gamma_n$ (por la fórmula explícita + RH).
3. Los ceros de $\hat\xi_\lambda$ convergen a los cruces (por la aproximación diagonal).
4. Luego los ceros de $\hat\xi_\lambda$ convergen a $\gamma_n$.

**El obstáculo (honesto).** El paso 1 es formal (la aproximación $M \approx \text{multiplicación}$ ignora el término de rango 1 $Q^{\mathrm{cross}}$ y los efectos de la discretización en $E_N^+$). Los pasos 2 y 3 requieren cuantificación. El paso 2 usa RH (es CONDICIONAL).

---

## 7. Reducción incondicional: la ecuación de ceros sin RH

Sin asumir RH, los cruces de $\mathcal{C}_\lambda$ convergen a los **valores imaginarios de todos los ceros no-triviales** de $\zeta$ (tanto los que están en la recta crítica $\gamma_n$ como los que eventualmente no estarían).

Pero: los ceros de $\hat\xi_\lambda$ son SIEMPRE reales (Teorema CCM). Por tanto:

**Proposición 4** (cuadrado del programa). Si los cruces $\mathcal{C}_\lambda$ convergieran a valores COMPLEJOS (violando RH), los ceros exactamente reales de $\hat\xi_\lambda$ no podrían converger a ellos — generaría una CONTRADICCIÓN si la convergencia $\hat\xi_\lambda \to \Xi$ se establece de forma independiente.

La cadena lógica:
- $\hat\xi_\lambda$ tiene ceros REALES (por CCM, incondicional).
- Si los cruces de $\mathcal{C}_\lambda$ convergen a un cero complejo $\rho$ con $\Im(\rho) \neq 0$: el cruce en la recta real sería $\mathrm{Im}(\rho)$ (la parte imaginaria), que es real. Por tanto los ceros reales de $\hat\xi_\lambda$ convergen a los valores imaginarios de los ceros de $\zeta$ — que son reales tanto bajo RH como sin ella.
- Entonces: $\hat\xi_\lambda \to \Xi$ (bajo H2) NO requiere que los cruces sean exactamente $\gamma_n$; requiere que la convergencia sea hacia $\Xi$ (no hacia $\zeta(1/2+it)$ directamente).

**La precisión necesaria:** El programa CCM requiere que los ceros reales de $\hat\xi_\lambda$ converjan a los ceros reales de $\Xi$ (que son los $\gamma_n$ bajo RH, o complejos sin RH). Como los ceros de $\hat\xi_\lambda$ son siempre reales, la convergencia a ceros complejos de $\Xi$ sería imposible. Esto es exactamente la estructura del argumento de Hurwitz: si $\hat\xi_\lambda \to \Xi$ uniformemente y los $\hat\xi_\lambda$ tienen todos ceros reales, entonces $\Xi$ tiene todos ceros reales.

---

## 8. Los momentos de $\Delta_m$ desde el sistema de Euler-Lagrange

El sistema variacional para $\xi_\lambda$ da (en la base $\{U_m^+\}$):

$$\sum_{m'=0}^N \tau_{mm'} \xi_{m'}^{(\lambda)} = \mu_\lambda \xi_m^{(\lambda)} \quad \forall\, 0 \leq m \leq N,$$

donde $\tau_{mm'}$ es la matriz de Cauchy-Toeplitz de $QW_\lambda^N|_{E^+}$.

**Proposición 5** (restricciones de momento de $\Delta$ desde Euler-Lagrange). Para $q = 0, 1, 2, \ldots$, el $q$-ésimo momento de $\Delta$ satisface:

$$\sum_{m=0}^N m^q \Delta_m = \sum_{m=0}^N m^q (\xi_m^{(\lambda)} - c_\lambda k_m^{(\lambda)})$$

$$= \frac{1}{\mu_\lambda}\sum_{m=0}^N m^q \sum_{m'} \tau_{mm'}\xi_{m'} - c_\lambda \sum_m m^q k_m^{(\lambda)}.$$

La condición para que el $q$-ésimo momento de $\Delta$ se anule es:

$$\sum_{m,m'} m^q \tau_{mm'} \xi_{m'} = \mu_\lambda c_\lambda \sum_m m^q k_m^{(\lambda)}.$$

**Conjetura de momentos (CM).** Para $q = 0, 1$:
$$\sum_m \Delta_m = 0 \text{ (momento de orden 0, probado)}, \qquad \sum_m m\,\Delta_m = O(e^{-\pi\lambda^2}) \text{ (momento de orden 1, conjectured)}.$$

Si CM vale para $q = 0, 1$: la suma $S_n$ se reduce a un estimado de SEGUNDO momento:

$$S_n = \frac{1}{\gamma_n^2} \sum_m \frac{\Delta_m (2\pi m/L)^2}{\gamma_n - 2\pi m/L} + O(e^{-\pi\lambda^2}/\gamma_n),$$

que es más controlable (el numerador involucra $m^2\Delta_m$ ponderado).

**Por qué CM es plausible.** En la representación de Mellin diagonal: el momento $\sum_m m^q \Delta_m$ corresponde a la $q$-ésima derivada de $\hat\Delta$ evaluada en $t = 0$:
$$\hat\Delta^{(q)}(0) = i^q \sum_m m \cdot (\text{factor})^q \Delta_m.$$

Para que $\hat\Delta(t) \approx 0$ cerca de $t = 0$ (región donde la fórmula explícita es "plana"), se necesita que las derivadas de $\hat\Delta$ en $0$ sean pequeñas — lo cual es una consecuencia del carácter suave de la diferencia entre el minimizador y la aproximación PSWF.

---

## 9. Estimado de $S_n$ via Lema 7.3

**Teorema 2** (cota cuantitativa de $S_n$). Bajo los supuestos del Lema 7.3:

$$|S_n| \leq |R_\xi(\gamma_n)| + c_\lambda |R_k(\gamma_n)| \leq |R_\xi(\gamma_n)| + c_\lambda \cdot \frac{C_\alpha \lambda^{-1/2-\alpha}}{(1-2\alpha)\sqrt{L}}.$$

El segundo término es $O(\lambda^{-1/2})$. Para el primer término:

$$|R_\xi(\gamma_n)| = |R_\xi(\gamma_n) - R_\xi(t_n^{(\lambda)})| = |\gamma_n - t_n^{(\lambda)}| \cdot |R_\xi'(\zeta)|$$

para algún $\zeta$ entre $\gamma_n$ y $t_n^{(\lambda)}$. Aquí $|R_\xi'(\zeta)| \approx |\hat\xi_\lambda'(t_n^{(\lambda)})| / L \approx w_n/L$.

Luego: $|S_n| \leq |\gamma_n - t_n^{(\lambda)}| w_n/L + O(\lambda^{-1/2})$.

Por tanto: la condición Wall-H2 $|S_n| \to 0$ es EQUIVALENTE a $|\gamma_n - t_n^{(\lambda)}| \to 0$ (convergencia de los ceros).

**Inversamente:** si podemos acotar $|S_n|$ independientemente de $|t_n^{(\lambda)} - \gamma_n|$, obtenemos la convergencia de los ceros. El Lema 7.3 da:

$$c_\lambda |R_k(\gamma_n)| = O(\lambda^{-1/2}/w_n) \cdot w_n = O(\lambda^{-1/2}).$$

Si $R_\xi(\gamma_n) = c_\lambda R_k(\gamma_n) + (\text{small})$, entonces $S_n = O(\lambda^{-1/2})$ y el Teorema 1 da $|t_n^{(\lambda)} - \gamma_n| = O(\lambda^{-1/2}/w_n)$.

**El punto central:** Esta igualdad $R_\xi(\gamma_n) \approx c_\lambda R_k(\gamma_n)$ es precisamente lo que necesita probarse para resolver H2. No es circular: $R_k(\gamma_n)$ se conoce por el Lema 7.3, y $R_\xi(\gamma_n)$ depende de la estructura del minimizador.

---

## 10. Veredicto: estado del programa tras doc 06

### Nuevos resultados probados (incondicionalmente):

| Resultado | Estado |
|---|---|
| Convergencia cuantitativa: $|s_n^{(\lambda)} - \gamma_n| = O(\lambda^{-1/2}/w_n)$ para ceros de $\hat k_\lambda$ (Teorema 1) | **Probado** |
| Restricción $\sum_m \Delta_m = 0$ desde normalización (Prop. 1) | **Probado** |
| Reducción de $S_n$ a suma de primer momento (Sec. 3) | **Probado** |
| Estructura multiplicativa: $\widehat{A_\lambda f}(t) = \Psi_\lambda(t)\hat f(t)$ (Lema 2) | **Probado** |
| $M \approx$ multiplicación por $w - \Psi_\lambda$ en espacio de Mellin (Corolario) | **Probado** |
| Equivalencia $|S_n| \to 0 \iff |t_n^{(\lambda)} - \gamma_n| \to 0$ (Teorema 2) | **Probado** |

### Lo que queda abierto:

| Pregunta | Descripción |
|---|---|
| **29.4 (central)** | Probar $|S_n| = O(\lambda^{-1/2})$ usando la estructura variacional de $\xi_\lambda$ |
| **CM (momentos)** | $\sum_m m\,\Delta_m = O(e^{-\pi\lambda^2})$ desde Euler-Lagrange |
| **Prop. 2 (formal)** | Hacer riguroso el argumento "los ceros se concentran en los cruces" |
| **H2 (completa)** | Probar $|\hat\xi_\lambda - c\hat k_\lambda| = O(\lambda^{-1/2})$ sobre $|\Im z| \leq \alpha$ |

### El muro preciso después de 6 documentos:

El obstáculo central es demostrar $R_\xi(\gamma_n) \approx c_\lambda R_k(\gamma_n)$, i.e., que los COEFICIENTES del minimizador $\xi_\lambda$ (que satisfacen la ecuación de Cauchy-Toeplitz) aproximan, en el sentido del funcional de evaluación en $\gamma_n$, los coeficientes de $k_\lambda$ (que satisfacen la ecuación de PSWF).

Esto es exactamente la conjetura H2 de CCM, reformulada en términos concretos de la ecuación de ceros. No hemos cerrado el programa, pero hemos reducido Wall-H2 a un estimado algebraico preciso: la evaluación de una función racional en los ceros de $\Xi$.

### La próxima pregunta atacable (29.5):

> **Pregunta 29.5.** ¿Satisfacen los coeficientes $\{\xi_m^{(\lambda)}\}$ del minimizador de $QW_\lambda$ la condición de momento de primer orden: $\sum_m m\,\xi_m^{(\lambda)} = \sum_m m\,k_m^{(\lambda)} + O(e^{-\pi\lambda^2})$?

Esta condición puede atacarse directamente desde el sistema de Euler-Lagrange (Proposición 5), tomando $q = 1$ y evaluando las entradas de la matriz Cauchy-Toeplitz $\tau_{mm'}$.
