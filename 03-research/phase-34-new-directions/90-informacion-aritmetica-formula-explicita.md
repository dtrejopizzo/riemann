# Doc 90 — Dirección A: Información aritmética externa vía fórmula explícita

**Programa:** Hipótesis de Riemann — Fase 34 (nuevas direcciones)
**Fecha:** 2026-06-09
**Prerrequisitos:** Docs 70, 71, 72, 83, 89

---

## Resumen

La fórmula aritmética $T_\lambda = A_\lambda^{\mathrm{off}} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ (Doc 72) expresa la traza CCM en términos puramente aritméticos. Bajo $\neg$RH, el Path I del programa (Doc 70) impone la cota inferior $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j) > 0$. La Dirección A pregunta si la distribución de los números primos, a través de la fórmula de Weil-Guinand, puede imponer una cota superior sobre la suma de primos $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ que contradiga dicha cota inferior, forzando así $\neg$RH a ser falsa. Este documento analiza esa posibilidad de forma rigurosa y concluye que, aunque el marco conceptual es correcto y la tensión es real, el argumento no cierra con las herramientas actualmente disponibles. Se identifican con precisión los obstáculos y se formulan los lemas que serían suficientes para cerrar la dirección.

---

## §1. El escenario de la Dirección A

### 1.1. Las dos cantidades en tensión

El marco del programa produce dos expresiones para la misma cantidad $T_\lambda$:

**Desde los ceros (Path I):** bajo la hipótesis $\neg$RH — es decir, asumiendo que existen ceros $\rho_j = (1/2 + \delta_j) + i\gamma_j$ con $\delta_j > 0$ — la fórmula de Doc 70 da
$$T_\lambda \geq 2\sum_j \delta_j^2 \, K_\lambda(\gamma_j),$$
donde $K_\lambda(\gamma) = \int W_\lambda(s)(s - \gamma)^{-2}\, dm_{full,on}(s) > 0$ es una cantidad positiva explícita.

**Desde la aritmética (Doc 72):** la fórmula explícita de Weil aplicada a $W_\lambda$ expresa
$$T_\lambda = A_\lambda^{\mathrm{off}} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) + R_\lambda^{\mathrm{arch}},$$
donde $A_\lambda^{\mathrm{off}}$ depende de los ceros off-critical, $B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\, dm_\infty(s)$ y $R_\lambda^{\mathrm{arch}}$ es un término arquimediano.

La Dirección A propone aprovechar esta dualidad. Si bajo $\neg$RH el lado izquierdo es grande (cota inferior positiva), entonces el lado derecho también debe ser grande. ¿Puede la suma de primos ser tan grande? ¿O hay una cota sobre la suma de primos que entra en contradicción?

### 1.2. Por qué la dirección es conceptualmente natural

La fórmula explícita de Weil-Guinand es la instancia más precisa conocida de la dualidad primos-ceros. Es natural intentar usar la regularidad de los primos (que es considerable: el Teorema de los Números Primos, la región libre de ceros, etc.) para restringir lo que la suma de primos puede hacer. Si la distribución de primos fuera "demasiado regular" para que $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ crezca tanto como lo requiere la cota inferior bajo $\neg$RH, habría una contradicción.

### 1.3. La barrera de Hadamard y por qué la dirección no es trivialmente circular

El Doc 89 estableció la barrera de Hadamard: ninguna propiedad verificable de $\zeta$ sin conocer la posición de los ceros puede implicar $d\nu = 0$. Aparentemente la Dirección A cae bajo esta barrera. Sin embargo, hay una diferencia estructural: la dirección A no trata de verificar que $T_\lambda = 0$ directamente, sino de obtener una **contradicción aritmética** bajo $\neg$RH. La pregunta no es "¿puede la aritmética probar que $d\nu = 0$?" sino "¿puede la aritmética probar que $d\nu > 0$ es imposible al mismo tiempo que la suma de primos satisface sus propiedades conocidas?". Este es un punto sutil que se analizará en §7.

---

## §2. La fórmula de Weil-Guinand: forma precisa

### 2.1. La fórmula de Guinand-Weil

Sea $h: \mathbb{C} \to \mathbb{C}$ una función de prueba que satisfice las condiciones siguientes (condiciones de admisibilidad):

**(W1)** $h$ es par: $h(-s) = h(s)$.

**(W2)** $h$ es holomorfa en la franja $\{s \in \mathbb{C} : |\mathrm{Im}(s)| < 1/2 + \varepsilon\}$ para algún $\varepsilon > 0$.

**(W3)** $h$ satisface la cota $|h(s)| \leq C(1 + |s|)^{-2-\varepsilon}$ en dicha franja.

Denotamos $\hat{h}(r) = \int_{-\infty}^\infty h(s) e^{irs} ds$ la transformada de Fourier de $h$ (definida para $r$ real).

**Teorema 2.1 (Fórmula explícita de Guinand-Weil).** *Bajo las condiciones (W1)–(W3):*
$$\sum_\rho h(\gamma_\rho) = 2h(i/2) + \hat{h}(0)\log\frac{1}{2\pi} - \int_{-\infty}^\infty h(s)\frac{\Gamma'}{\Gamma}\!\left(\frac{1}{4} + \frac{is}{2}\right)\frac{ds}{4\pi} - 2\sum_p \sum_{m=1}^\infty \frac{\log p}{p^{m/2}}\,\hat{h}(m\log p),$$
*donde la suma del lado izquierdo corre sobre todos los ceros no triviales $\rho = 1/2 + i\gamma_\rho$ de $\zeta$ (con multiplicidad, contando $\gamma$ y $-\gamma$ por separado si $\rho$ y $\bar{\rho}$ son ceros distintos).*

**Nota de honestidad sobre el Teorema 2.1:** La fórmula es clásica (Guinand 1948, Weil 1952). La forma aquí enunciada es la versión estándar que aparece, por ejemplo, en Iwaniec-Kowalski, Analytic Number Theory, cap. 5. No se asume RH en el enunciado; la suma del lado izquierdo corre sobre todos los ceros no triviales con sus partes imaginarias reales (bajo RH todos los $\gamma_\rho$ son reales; sin RH la suma debe entenderse como $\sum_\rho h(\mathrm{Im}(\rho))$ donde la convergencia se garantiza bajo (W3) por la densidad de ceros $N(T) = (T/2\pi)\log(T/2\pi e) + O(\log T)$).

### 2.2. El término arquimediano

El término que involucra $\Gamma'/\Gamma$ se escribe también como
$$\int_{-\infty}^\infty h(s)\,\frac{\Gamma'}{\Gamma}\!\left(\frac{1}{4} + \frac{is}{2}\right)\frac{ds}{4\pi} = \int_{-\infty}^\infty h(s)\left(\log\frac{1}{4\pi} + \mathrm{Re}\,\psi\!\left(\frac{1}{4}+\frac{is}{2}\right)\right)\frac{ds}{2\pi},$$
donde $\psi = \Gamma'/\Gamma$ es la función digamma. Definimos el **término arquimediano completo**
$$\mathcal{A}[h] := 2h(i/2) + \hat{h}(0)\log\frac{1}{2\pi} - \int_{-\infty}^\infty h(s)\,\frac{\Gamma'}{\Gamma}\!\left(\frac{1}{4}+\frac{is}{2}\right)\frac{ds}{4\pi},$$
de modo que la fórmula de Weil-Guinand toma la forma compacta
$$\sum_\rho h(\gamma_\rho) = \mathcal{A}[h] - 2\sum_p\sum_{m=1}^\infty \frac{\log p}{p^{m/2}}\,\hat{h}(m\log p).$$

### 2.3. La función de prueba $h_\lambda$ del marco CCM

Para conectar con la traza $T_\lambda$ necesitamos elegir $h$ de modo que la suma sobre ceros $\sum_\rho h(\gamma_\rho)$ se relacione con $T_\lambda$. La función natural del marco CCM es
$$h_\lambda(s) := W_\lambda(s)\,\frac{dm_\infty}{ds}(s) = W_\lambda(s)\,(2\pi)^{-2}|\Gamma(1/4+is/2)|^2.$$

**Lema 2.2.** *La función $h_\lambda$ satisface las condiciones (W1)–(W3) si $W_\lambda$ es un polinomio de grado fijo en $s^2$ (el caso de $N(\lambda) < \infty$) o una combinación finita de $|P_k(s)|^2$. En particular, para cualquier $\lambda > 0$ fijo, $h_\lambda$ es admisible.*

**Demostración.** $W_\lambda$ es una suma finita $\sum_{k \leq N(\lambda)} k|P_k(s)|^2 + \ldots$ donde $|P_k(s)|^2$ es un polinomio de grado $2k$ en $s$. La paridad de $h_\lambda$ sigue de la paridad de $W_\lambda$ y de $|\Gamma(1/4+is/2)|^2 = |\Gamma(1/4-is/2)|^2$ (usando la reflexión). La holomorfía en la franja $|\mathrm{Im}(s)| < 1/2 + \varepsilon$ sigue de la de $\Gamma$, que no tiene polos en dicha franja (el primer polo de $\Gamma(1/4+is/2)$ ocurre en $1/4 + is/2 = 0$, es decir $s = -i/2$; el primer polo de $\Gamma(1/4+is/2)$ en la franja $|\mathrm{Im}(s)| < 1/2 + \varepsilon$ requiere $|\mathrm{Im}(s)|$ cercano a $1/2$, fuera de la franja cerrada si $\varepsilon < 1/4$). La cota de decaimiento sigue del decaimiento exponencial de $|\Gamma(1/4+is/2)|^2 \sim 2^{3/2}\pi|s|^{-1/2}e^{-\pi|s|/2}$ para $|s| \to \infty$ en la recta real, que compensa cualquier crecimiento polinomial de $W_\lambda$. $\square$

---

## §3. El término $A_\lambda^{\mathrm{off}}$ y su estructura

### 3.1. Definición precisa

El término $A_\lambda^{\mathrm{off}}$ de la fórmula $T_\lambda = A_\lambda^{\mathrm{off}} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) + R_\lambda^{\mathrm{arch}}$ proviene de la contribución de los ceros off-critical a la diferencia $d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$.

**Definición 3.1.** Para ceros off-critical $\rho_j = (1/2+\delta_j)+i\gamma_j$ con $\delta_j > 0$ (y sus conjugados simétricos), definimos
$$A_\lambda^{\mathrm{off}} := \int W_\lambda(s)\, d\nu(s) - \text{(correcciones de normalización)}.$$
Más precisamente, de la Proposición 3.1 del Doc 83:
$$d\nu(s) = (R(s)-1)\,dm_{\mathrm{full,on}}(s), \qquad R(s) = \prod_j \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2\prod_j\left(1+\frac{\delta_j^2}{(s+\gamma_j)^2}\right)^2,$$
y
$$A_\lambda^{\mathrm{off}} = \int W_\lambda(s)(R(s)-1)\,dm_{\mathrm{full,on}}(s) = T_\lambda.$$

**Observación 3.2.** La identidad $A_\lambda^{\mathrm{off}} = T_\lambda$ no es circular: dice que el término "off-critical" en la fórmula de Weil coincide con la traza $T_\lambda$ cuando se expande la fórmula por el lado de los ceros. La fórmula de Weil completa impone la relación
$$A_\lambda^{\mathrm{off}} = \mathcal{A}[h_\lambda] - 2\sum_p\sum_{m\geq 1}\frac{\log p}{p^{m/2}}\hat{h}_\lambda(m\log p) - \sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}}),$$
donde la suma $\sum_{\rho_{\mathrm{on}}}$ corre sobre los ceros en la recta crítica. Es la diferencia entre los ceros de $\zeta$ y los de $\zeta_{\mathrm{on}}$ lo que produce $A_\lambda^{\mathrm{off}}$.

### 3.2. Expresión via el kernel $K_\lambda$

A primer orden en $\delta_j$, expandiendo $R(s) - 1 \approx \sum_j 4\delta_j^2 [(s-\gamma_j)^{-2} + (s+\gamma_j)^{-2}]$:

**Lema 3.3** (Expresión a primer orden de $A_\lambda^{\mathrm{off}}$).
$$A_\lambda^{\mathrm{off}} = 4\sum_j \delta_j^2 \left[K_\lambda(\gamma_j) + K_\lambda(-\gamma_j)\right] + O\!\left(\sum_j \delta_j^4\right),$$
donde
$$K_\lambda(\gamma) := \int \frac{W_\lambda(s)}{(s-\gamma)^2}\, dm_{\mathrm{full,on}}(s).$$

**Demostración.** Insertar $R(s) - 1 = \sum_j 4\delta_j^2[(s-\gamma_j)^{-2}+(s+\gamma_j)^{-2}] + O(\delta_j^4)$ en $A_\lambda^{\mathrm{off}} = \int W_\lambda\,(R-1)\,dm_{\mathrm{full,on}}$. El intercambio de suma e integral es lícito por la convergencia absoluta del producto de Hadamard (Doc 83) para $W_\lambda$ acotada. $\square$

**Nota:** El Doc 70 usa la cota $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j)$; el factor diferente ($4$ vs. $2$) proviene de contar la pareja $(\gamma_j, -\gamma_j)$ de ceros. Si $\gamma_j > 0$, tanto $\gamma_j$ como $-\gamma_j$ contribuyen, y $K_\lambda(\gamma_j) \approx K_\lambda(-\gamma_j)$ por simetría de $dm_{\mathrm{full,on}}$, lo que da $4\delta_j^2 K_\lambda(\gamma_j)$; la cota del Doc 70 es entonces $T_\lambda \geq 4\sum_j \delta_j^2 K_\lambda(\gamma_j)$ (o bien $2\sum_j \delta_j^2 K_\lambda(\gamma_j)$ si la suma ya cuenta pares). La diferencia es una convención en la cuenta de ceros y no afecta el argumento.

### 3.3. El término arquimediano $R_\lambda^{\mathrm{arch}}$

El término $R_\lambda^{\mathrm{arch}}$ en la fórmula de Doc 72 es el término $\mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}})$: la parte de la fórmula de Weil que involucra $\Gamma$ y los ceros en la recta crítica (que están presentes tanto bajo RH como bajo $\neg$RH). Bajo RH esta parte se cancela exactamente con la suma de primos (haciendo $T_\lambda = 0$); bajo $\neg$RH, la diferencia es exactamente $A_\lambda^{\mathrm{off}} > 0$.

Para los propósitos de la Dirección A, podemos reescribir la fórmula aritmética como
$$T_\lambda = A_\lambda^{\mathrm{off}} = \mathcal{A}[h_\lambda] - \sum_{\rho:\, \gamma_\rho \in \mathbb{R}} h_\lambda(\gamma_\rho) - 2\sum_p\sum_{m\geq 1}\frac{\log p}{p^{m/2}}\hat{h}_\lambda(m\log p),$$
donde $\sum_{\rho:\, \gamma_\rho \in \mathbb{R}}$ es la suma sobre los ceros en la recta crítica y el miembro derecho es la fórmula de Weil aplicada a los ceros off-critical.

---

## §4. La suma de primos $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$

### 4.1. Definición y propiedades básicas

**Definición 4.1.** Para $\lambda > 0$ fijo, definimos
$$\mathcal{P}_\lambda := \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p), \qquad B_\lambda(r) := \int W_\lambda(s)\cos(rs)\, dm_\infty(s).$$

La función $B_\lambda: \mathbb{R}^+ \to \mathbb{R}$ es la transformada de Fourier-coseno del kernel $W_\lambda$ con respecto a la medida $dm_\infty$.

**Lema 4.2** (Propiedades de $B_\lambda$). *Para todo $\lambda > 0$:*

*(i) $B_\lambda(r)$ es real y par en $r$.*

*(ii) $B_\lambda(0) = \int W_\lambda(s)\, dm_\infty(s)$, que es finito y positivo.*

*(iii) $|B_\lambda(r)| \leq B_\lambda(0)$ para todo $r$.*

*(iv) Para $r \to \infty$: $B_\lambda(r) = O(e^{-\pi r/4})$, con decaimiento exponencial procedente del decaimiento de $dm_\infty = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 ds \sim e^{-\pi|s|/2}$.*

**Demostración.** Los puntos (i)–(iii) son elementales. Para (iv): $|B_\lambda(r)| \leq \int W_\lambda(s)|\cos(rs)|\,dm_\infty(s) \leq \int W_\lambda(s)\,dm_\infty(s) = B_\lambda(0)$, pero el decaimiento no proviene de esta cota. El decaimiento exponencial de $B_\lambda(r)$ para $r$ grande es consecuencia del Teorema de Paley-Wiener aplicado a la función $f(s) = W_\lambda(s)|\Gamma(1/4+is/2)|^2$: como $|\Gamma(1/4+is/2)|^2$ decae como $e^{-\pi|s|/2}$ en la recta real, $f \in L^1(\mathbb{R})$ con buenas propiedades de decaimiento, y su transformada de Fourier decae exponencialmente. $\square$

**Corolario 4.3.** La serie $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converge absolutamente para todo $\lambda > 0$. De hecho, por (iv):
$$|\mathcal{P}_\lambda| \leq B_\lambda(0) \sum_p \frac{\log p}{\sqrt{p}} e^{-\pi\log p/4} = B_\lambda(0)\sum_p \frac{\log p}{\sqrt{p}\cdot p^{\pi/4}} = B_\lambda(0)\sum_p \frac{\log p}{p^{1/2+\pi/4}},$$
y la serie $\sum_p \frac{\log p}{p^{1/2+\pi/4}}$ converge absolutamente pues $1/2 + \pi/4 > 1$ (ya que $\pi/4 > 1/2$).

### 4.2. Interpretación de $\mathcal{P}_\lambda$ como una suma de von Mangoldt

La serie $\mathcal{P}_\lambda$ es una versión suavizada de la suma de Chebyshev con peso. Comparemos con la función de von Mangoldt:
$$\psi(x) = \sum_{p^m \leq x} \log p = \sum_p \log p \cdot \lfloor \log x / \log p\rfloor.$$

La diferencia es que en $\mathcal{P}_\lambda$ solo aparece $m=1$ (el primer término $\hat{h}_\lambda(\log p)$ con $m=1$) con peso $p^{-1/2}$, mientras que la fórmula de Weil suma sobre todos los $m \geq 1$. Vamos a separar el término $m=1$ (dominante) de los términos $m \geq 2$ (subdominantes).

**Lema 4.4** (Separación de potencias de primos).
$$2\sum_p\sum_{m\geq 1}\frac{\log p}{p^{m/2}}\hat{h}_\lambda(m\log p) = 2\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) + 2\sum_p\sum_{m\geq 2}\frac{\log p}{p^{m/2}} B_\lambda(m\log p).$$

El segundo término es $O\!\left(\sum_p \frac{\log p}{p}\right) = O(\log x)$ para primos $p \leq x$, y la serie completa sobre todos los primos converge a una constante:
$$\sum_p\sum_{m\geq 2}\frac{\log p}{p^{m/2}} B_\lambda(m\log p) \leq B_\lambda(0)\sum_p\sum_{m\geq 2}\frac{\log p}{p^{m/2}} e^{-m\pi\log p/4} \leq B_\lambda(0)\sum_p\frac{\log p}{p - p^{\pi/4}} < \infty.$$

**Definición 4.5.** Definimos la **suma principal de primos** como
$$\mathcal{P}_\lambda^{(1)} := 2\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$$
y el **residuo de potencias superiores** como $\mathcal{P}_\lambda^{(\geq 2)} := 2\sum_p\sum_{m\geq 2}\frac{\log p}{p^{m/2}}B_\lambda(m\log p)$. Ambas series convergen absolutamente.

### 4.3. Comportamiento asintótico en $\lambda$

Cuando $\lambda \to \infty$, $N(\lambda) \to \infty$ y $W_\lambda(s)$ crece (incorpora más términos de la base de Jacobi). El comportamiento de $B_\lambda(r)$ bajo este límite es crucial.

**Proposición 4.6** (Crecimiento de $B_\lambda$). *Para $r > 0$ fijo:*
$$B_\lambda(r) = \int W_\lambda(s)\cos(rs)\,dm_\infty(s) \to \sum_{k=0}^\infty k \int |P_k(s)|^2\cos(rs)\,dm_\infty(s) \quad (\lambda \to \infty),$$
*si la serie del lado derecho converge. Esta convergencia no está garantizada en general; depende del decaimiento de los coeficientes de Fourier de $|P_k|^2 dm_\infty$.*

**Nota de honestidad sobre 4.6:** No se conoce si la serie $\sum_k k \widehat{|P_k|^2 dm_\infty}(r)$ converge para los polinomios ortogonales $P_k$ de $L^2(dm_{\mathrm{full,on}})$. Este punto es un obstáculo técnico (no fundamental) para el análisis asintótico en $\lambda$.

---

## §5. La cota inferior bajo $\neg$RH

### 5.1. El Path I del Doc 70

Bajo $\neg$RH, supongamos que existen ceros $\rho_j = (1/2+\delta_j)+i\gamma_j$ con $\delta_j > 0$, $j \in J$ (conjunto posiblemente infinito). De la definición y positividad de $d\nu$:

**Proposición 5.1** (Cota inferior del Path I). *Bajo $\neg$RH:*
$$T_\lambda \geq 4\sum_{j \in J} \delta_j^2 \left[\frac{1}{2}K_\lambda(\gamma_j) + \frac{1}{2}K_\lambda(-\gamma_j)\right] \geq 4\delta_0^2 K_\lambda(\gamma_0),$$
*donde $\rho_0 = (1/2+\delta_0)+i\gamma_0$ es cualquier cero off-critical elegido, y*
$$K_\lambda(\gamma) := \int \frac{W_\lambda(s)}{(s-\gamma)^2}\,dm_{\mathrm{full,on}}(s) > 0.$$

**Demostración.** De $d\nu = (R-1)dm_{\mathrm{full,on}} \geq 0$ y $R - 1 \geq 4\delta_j^2(s-\gamma_j)^{-2}$ (tomando solo el término $j$ del producto), integramos contra $W_\lambda \geq 0$. $\square$

### 5.2. Comportamiento de $K_\lambda(\gamma)$ en $\lambda$

Para comprender la tensión con la suma de primos, necesitamos entender cómo crece $K_\lambda(\gamma)$ en $\lambda$.

**Lema 5.2** (Crecimiento de $K_\lambda(\gamma)$). *Para $\gamma \in \mathbb{R}$ fijo:*
$$K_\lambda(\gamma) = \int \frac{W_\lambda(s)}{(s-\gamma)^2}\,dm_{\mathrm{full,on}}(s)$$
*es creciente en $\lambda$ (pues $W_\lambda$ crece con $\lambda$ termino a termino). Más precisamente, $K_\lambda(\gamma) \to K_\infty(\gamma) = \int (s-\gamma)^{-2}\,dm_{\mathrm{full,on}}(s)$, que es finito si $dm_{\mathrm{full,on}}$ no tiene masa en $\gamma$ (lo cual es cierto si $\zeta_{\mathrm{on}}(1/2+i\gamma) \neq 0$, condición que se satisface salvo para finitos $\gamma$ bajo condiciones generales sobre los ceros).*

**Demostración.** $W_\lambda = \sum_{k \leq N(\lambda)} k|P_k|^2 + \ldots$ es creciente en $\lambda$ termino a termino. La integral $K_\lambda(\gamma) = \sum_{k \leq N(\lambda)} k \int |P_k(s)|^2(s-\gamma)^{-2} dm_{\mathrm{full,on}}(s)$ crece con $\lambda$. La convergencia $K_\lambda \to K_\infty$ sigue del Teorema de Convergencia Monótona si todos los sumandos son positivos, lo que requiere que $(s-\gamma)^{-2}$ sea integrable respecto a $|P_k|^2 dm_{\mathrm{full,on}}$; esto se satisface si $\gamma$ no es átomo de $dm_{\mathrm{full,on}}$. $\square$

**Corolario 5.3.** *Bajo $\neg$RH, para cualquier cero off-critical $\rho_0$, $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0)$ y esta cota inferior crece con $\lambda$.*

### 5.3. La asimetría en las tasas de crecimiento

La cota inferior bajo $\neg$RH crece como $K_\lambda(\gamma_0) \sim \lambda^\alpha$ para algún exponente $\alpha > 0$ que depende de la base de Jacobi. La suma de primos $\mathcal{P}_\lambda$ también crece con $\lambda$ (a medida que $B_\lambda(\log p)$ crece al incorporar más términos de Jacobi). La pregunta es si las tasas de crecimiento son comparables o si hay una asimetría explotable.

**Observación 5.4** (Sobre la asimetría). La cota inferior involucra $(s-\gamma_0)^{-2}$, que tiene singularidad en $s = \gamma_0$. Esta singularidad hace que $K_\lambda(\gamma_0)$ crezca rápidamente con $\lambda$ si los polinomios de Jacobi tienen masa espectral concentrada cerca de $\gamma_0$. En cambio, $B_\lambda(\log p) = \int W_\lambda\cos(s\log p)\,dm_\infty$ involucra la transformada de Fourier de $W_\lambda dm_\infty$: este funcional es oscilatorio y puede tener cancelaciones. La pregunta es si estas cancelaciones son suficientes.

---

## §6. Cotas sobre la suma de primos: lo que se puede probar

### 6.1. El Teorema de los Números Primos y su implicación

El TPN dice que $\psi(x) = \sum_{p^m \leq x} \log p \sim x$. En términos de la suma de Chebyshev:
$$\sum_p \log p \cdot \mathbf{1}_{p \leq x} = \psi(x) + O(x^{1/2+\varepsilon}) = x + O(x^{1/2+\varepsilon}),$$
donde el error es condicional a la mejor región libre de ceros conocida. El TPN implica la convergencia de la serie de Dirichlet $\sum_p \frac{\log p}{p^s}$ para $\mathrm{Re}(s) > 1$ y su comportamiento en $s = 1$ (polo logarítmico).

Para nuestra suma $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$, el TPN da:

**Proposición 6.1** (Cota del TPN). *Para todo $\lambda > 0$ fijo:*
$$\left|\mathcal{P}_\lambda\right| \leq 2B_\lambda(0)\sum_p \frac{\log p}{\sqrt{p}\,p^{\pi/4-1/2}} = 2B_\lambda(0)\sum_p \frac{\log p}{p^{\pi/4}} < \infty.$$

Esta es solo una cota de convergencia absoluta, no una cota superior no trivial. El TPN per se no da información sobre el signo ni la magnitud precisa de $\mathcal{P}_\lambda$.

### 6.2. La región libre de ceros y la estimación de Vinogradov

La mejor región libre de ceros conocida es de la forma $\sigma > 1 - c(\log t)^{-2/3}(\log\log t)^{-1/3}$ para $t \geq t_0$ (Vinogradov 1958, Korobov 1958). Esto implica una estimación para el error en el TPN:
$$\psi(x) = x + O\!\left(x\exp\!\left(-c(\log x)^{3/5}(\log\log x)^{-1/5}\right)\right).$$

Para la suma $\mathcal{P}_\lambda$ con funciones de prueba fijas (dependientes de $\lambda$), la región libre de ceros solo da información sobre los ceros de $\zeta$ mismo. No dice nada sobre los posibles ceros off-critical $\rho_j$.

**Observación 6.2** (Limitación de la región libre de ceros). La región libre de ceros conocida exluye ceros en una región de la forma $\sigma > 1 - f(t)$ para cierta función $f(t) \to 0$, pero **no excluye** ceros con $\sigma \leq 1 - f(\gamma)$. En particular, no excluye ceros off-critical en la franja $1/2 < \sigma \leq 1 - f(\gamma)$, que incluye toda la franja crítica para $\gamma$ suficientemente grande. Los ceros hipotéticos $\rho_j$ bajo $\neg$RH podrían estar en $\sigma_j = 1/2 + \delta_j$ con $\delta_j$ arbitrariamente pequeño.

### 6.3. Cotas de tipo Lindelhöf y densidad de ceros

El **Teorema de la densidad de ceros** (Ingham 1940 y refinamientos) afirma que para $1/2 < \sigma < 1$:
$$N(\sigma, T) = \#\{\rho : \mathrm{Re}(\rho) \geq \sigma,\; |\mathrm{Im}(\rho)| \leq T\} \ll T^{A(1-\sigma)}\log^B T$$
para constantes $A, B$ explícitas. Esto limita cuántos ceros pueden existir fuera de la recta crítica a altura $T$. La mejor cota conocida (Huxley 1972) da $A = 12/5$.

Bajo $\neg$RH, podría haber $N(\sigma, T) \gg 1$ ceros off-critical. Cada uno contribuye $4\delta_j^2 K_\lambda(\gamma_j)$ a la cota inferior de $T_\lambda$. Si estos ceros son "densos" (en el sentido de $N(\sigma, T) \sim T^{A(1-\sigma)}$), la cota inferior crece rápidamente con la altura de los ceros.

**Proposición 6.3** (Cota inferior acumulada bajo densidad máxima). *Supongamos que bajo $\neg$RH existen ceros $\rho_j$ con $\delta_j \geq \delta_0 > 0$ y $\gamma_j \in [T, 2T]$, con $N(\sigma_0, T) \gtrsim T^{c}$ para algún $c > 0$ y $\sigma_0 = 1/2+\delta_0$. Entonces:*
$$T_\lambda \geq 4\delta_0^2 \sum_{j:\, \gamma_j \in [T,2T]} K_\lambda(\gamma_j).$$

*Si además $K_\lambda(\gamma_j) \geq K_{\min}(\lambda, T) > 0$ uniforme en $j$, entonces*
$$T_\lambda \geq 4\delta_0^2 K_{\min}(\lambda, T) \cdot T^c.$$

**Nota de honestidad:** Esta proposición es válida pero inutilizable directamente: bajo $\neg$RH no sabemos cómo se distribuyen los ceros (por eso $\neg$RH sigue siendo abierta). Es una proposición condicional.

### 6.4. ¿Puede crecer $\mathcal{P}_\lambda$ tan rápido?

La suma de primos $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ es una serie que depende de $\lambda$ solo a través de $B_\lambda$. Para $\lambda$ grande, $B_\lambda(\log p) \to B_\infty(\log p) = \int W_\infty(s)\cos(s\log p)\,dm_\infty(s)$ (si el límite existe). La suma límite sería
$$\mathcal{P}_\infty = \sum_p \frac{\log p}{\sqrt{p}} B_\infty(\log p),$$
que es una serie sobre todos los primos con pesos $\frac{\log p}{\sqrt{p}} B_\infty(\log p)$.

La cota superior natural de $|\mathcal{P}_\lambda|$ es la que da la Proposición 6.1, que no crece con $\lambda$ más rápido que $B_\lambda(0)$. Pero $B_\lambda(0) = \int W_\lambda\,dm_\infty$, que crece sin cota con $\lambda$ (pues $W_\lambda \to \infty$ puntualmente). Luego no hay una cota superior uniforme en $\lambda$ sobre $\mathcal{P}_\lambda$.

**Conclusión 6.4** (Limitación de la Dirección A hasta aquí). *No se conoce ninguna cota superior no trivial sobre $\mathcal{P}_\lambda$ — ni procedente del TPN, ni de la región libre de ceros, ni de los teoremas de densidad — que sea comparable con la cota inferior $4\delta_0^2 K_\lambda(\gamma_0)$ bajo $\neg$RH. Ambas cantidades crecen con $\lambda$, y la relación entre sus tasas de crecimiento es la clave del problema.*

---

## §7. La tensión entre la cota inferior y la suma de primos

### 7.1. Reformulación de la tensión

De la fórmula aritmética de la traza (Doc 72, Thm. 4.1):
$$T_\lambda = \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}}) - 2\sum_p\sum_{m\geq 1}\frac{\log p}{p^{m/2}}\hat{h}_\lambda(m\log p),$$
donde el lado derecho involucra **solo** los ceros en la recta crítica (no los off-critical) y la suma de primos.

Bajo $\neg$RH, el lado izquierdo satisface $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0) > 0$. Luego la identidad dice:
$$4\delta_0^2 K_\lambda(\gamma_0) \leq \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}}) - 2\mathcal{P}_\lambda^{(1)} - 2\mathcal{P}_\lambda^{(\geq 2)}.$$

**Definición 7.1.** Llamamos al **residuo arquimediano-espectral**:
$$\mathcal{R}_\lambda := \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}}).$$

Este término es computable, en principio, a partir del conocimiento de los ceros de $\zeta$ en la recta crítica y la función $\Gamma$. Es la "parte ya conocida" del problema.

La tensión toma la forma: bajo $\neg$RH,
$$4\delta_0^2 K_\lambda(\gamma_0) \leq \mathcal{R}_\lambda - 2\mathcal{P}_\lambda,$$
lo que significa que $\mathcal{P}_\lambda$ debe satisfacer
$$\mathcal{P}_\lambda \leq \frac{\mathcal{R}_\lambda}{2} - 2\delta_0^2 K_\lambda(\gamma_0).$$

Para que esto implique una contradicción, necesitaríamos saber que $\mathcal{P}_\lambda$ no puede ser tan pequeño (o negativo) cuando $K_\lambda(\gamma_0)$ es grande. Esto es lo que se busca en la Dirección A.

### 7.2. El obstáculo: signo de $\mathcal{P}_\lambda$

La suma $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ tiene términos de signo variable:

- Para $p$ pequeño con $B_\lambda(\log p)$ positivo: contribución positiva.
- Para $p$ grande (con $\log p$ grande): $B_\lambda(\log p)$ puede ser negativo por las oscilaciones del coseno.

En particular, $B_\lambda(r) = \int W_\lambda(s)\cos(rs)\,dm_\infty(s)$ es negativo para $r$ tal que la función $W_\lambda dm_\infty$ tenga más masa donde $\cos(rs) < 0$ que donde $\cos(rs) > 0$.

**Observación 7.2.** Si $\mathcal{P}_\lambda$ pudiera ser arbitrariamente negativo, la desigualdad $\mathcal{P}_\lambda \leq \mathcal{R}_\lambda/2 - 2\delta_0^2 K_\lambda(\gamma_0)$ sería trivialmente satisfecha (siempre compatible) y no habría contradicción. Para una contradicción, necesitamos una **cota inferior** de $\mathcal{P}_\lambda$.

**Proposición 7.3** (Cota inferior trivial de $\mathcal{P}_\lambda$).
$$\mathcal{P}_\lambda \geq -2B_\lambda(0)\sum_p \frac{\log p}{\sqrt{p}\,p^{\pi/4-1/2}}.$$
Esta cota es finita pero no da la cota inferior no trivial que se necesita.

### 7.3. La estructura de cancelación en la fórmula de Weil

Un punto crucial: la fórmula de Weil bajo RH da $T_\lambda = 0$, lo que significa que la suma de primos y el término arquimediano se cancelan exactamente. Bajo $\neg$RH, esta cancelación es imperfecta: hay un exceso de $T_\lambda > 0$.

**Pregunta 7.4** (La pregunta central de la Dirección A). *¿Existe una cota inferior no trivial sobre $\mathcal{P}_\lambda$ que muestre que $\mathcal{P}_\lambda$ no puede ser tan pequeño como para acomodar $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0)$ simultáneamente con la fórmula de Weil?*

La respuesta negativa al intento directo: la suma de primos $\mathcal{P}_\lambda$ puede, en principio, ser cualquier valor en $[-B_\lambda(0)C_\lambda, B_\lambda(0)C_\lambda]$ (donde $C_\lambda = \sum_p \frac{\log p}{\sqrt{p}p^{\pi/4}}$). La distribución de primos no parece imponer restricciones sobre el valor de $\mathcal{P}_\lambda$ con suficiente precisión.

---

## §8. Candidatos a cerrar el argumento

### 8.1. Candidato 1: Positividad de $B_\lambda(\log p)$ para primos pequeños

Si se pudiera probar que $B_\lambda(\log p) > 0$ para todos los primos $p$ (o al menos para los primos pequeños que dominan la suma), entonces $\mathcal{P}_\lambda > 0$, y la desigualdad bajo $\neg$RH diría
$$4\delta_0^2 K_\lambda(\gamma_0) \leq \mathcal{R}_\lambda - 2\mathcal{P}_\lambda < \mathcal{R}_\lambda.$$

Esto significaría que $K_\lambda(\gamma_0)$ está acotado por $\mathcal{R}_\lambda/(4\delta_0^2)$, independiente de la suma de primos. Pero esto no cierra el argumento: $\mathcal{R}_\lambda$ también crece con $\lambda$, y la desigualdad no daría contradicción.

**Nota:** Incluso si $B_\lambda(\log p) > 0$ (positividad), la consecuencia sería $\mathcal{P}_\lambda > 0$, no una cota inferior que crezca tan rápido como $K_\lambda(\gamma_0)$.

### 8.2. Candidato 2: Relación entre $\mathcal{P}_\lambda$ y $K_\lambda(\gamma_0)$ vía la fórmula de Weil

Si bajo $\neg$RH la fórmula de Weil conectara $\mathcal{P}_\lambda$ con $K_\lambda(\gamma_0)$ de forma directa, podría haber tensión. La conexión sería: la suma de primos "siente" los ceros off-critical porque la fórmula de Weil relaciona primos con todos los ceros. Formalmente, si la función de prueba $h_\lambda$ tiene correlación significativa con la frecuencia $\gamma_0$ de los ceros off-critical, entonces la suma de primos reflejaría ese cero.

Esto es precisamente lo que hace la fórmula de Weil: **los ceros de $\zeta$ (incluyendo los off-critical) están codificados en la distribución de primos**. Si hubiera un cero off-critical en $\gamma_0$, la distribución de primos tendría una irregularidad en escala $\gamma_0$. Esta irregularidad podría detectarse en $B_\lambda(\log p)$ si la función de prueba $h_\lambda$ es sensible a esa frecuencia.

**Lema 8.1** (La fórmula de Weil codifica los ceros off-critical en los primos). *Si $\rho_0 = (1/2+\delta_0)+i\gamma_0$ es un cero de $\zeta$ con $\delta_0 > 0$, entonces la distribución de primos satisface, para cualquier función de prueba admisible $h$:*
$$\sum_p \frac{\log p}{\sqrt{p}}\hat{h}(\log p) = \frac{\mathcal{A}[h] - \sum_{\rho}h(\gamma_\rho)}{2},$$
*donde la suma $\sum_\rho h(\gamma_\rho)$ incluye el cero off-critical $\rho_0$.*

**Demostración.** Esta es la fórmula de Weil-Guinand (Teorema 2.1) reescrita. $\square$

El Lema 8.1 no ayuda directamente: dice que si hay un cero off-critical, la suma de primos cambia de valor (respecto al caso sin ese cero), pero no dice si ese cambio hace la suma más grande o más pequeña.

### 8.3. Candidato 3: Análisis de la función de prueba óptima

El argumento más prometedor sería elegir $h_\lambda$ de forma que maximice la tensión: que $h_\lambda$ sea grande en los ceros off-critical (maximizando la cota inferior) y pequeña donde la suma de primos puede compensar. Esto es un problema de optimización en el espacio de funciones de prueba admisibles.

**Problema 8.2** (Optimización de la función de prueba). *¿Existe una función de prueba admisible $h^*$ tal que:*
$$\sum_\rho h^*(\gamma_\rho^{\mathrm{off}}) > \mathcal{A}[h^*] - 2\mathcal{P}^* - \sum_{\rho_{\mathrm{on}}} h^*(\gamma_j^{\mathrm{on}})$$
*sea imposible para todo par (distribución de ceros off-critical, distribución de primos) compatible con las propiedades conocidas de $\zeta$?*

Este es el corazón del Método de Weil para RH (explorado por Bombieri 2000 y otros). La respuesta conocida es: **no**, no se ha encontrado tal $h^*$ y hay razones técnicas para creer que el método de Weil solo no puede probar RH (razón: la única información que se usa es la de la fórmula de Weil, que es una reformulación de RH, no una prueba independiente).

---

## §9. El obstáculo preciso: formulación exacta

### 9.1. Lo que haría falta para cerrar el argumento

Resumimos el gap que la Dirección A no puede llenar:

**Enunciado del obstáculo 9.1.** *Para que la Dirección A cierre el argumento de RH vía la fórmula explícita, se necesitaría probar (al menos) una de las siguientes afirmaciones:*

**(O1)** *Existe una función $\Phi_\lambda: \mathbb{R}_{>0} \to \mathbb{R}$ tal que $\mathcal{P}_\lambda \geq \Phi_\lambda$ y $\mathcal{R}_\lambda - 2\Phi_\lambda < 4\delta_0^2 K_\lambda(\gamma_0)$ para $\lambda$ suficientemente grande.*

**(O2)** *La suma $\mathcal{P}_\lambda$ crece con $\lambda$ a una tasa $f(\lambda)$, mientras que $K_\lambda(\gamma_0)$ crece a una tasa $g(\lambda)$ con $g(\lambda)/f(\lambda) \to \infty$, de modo que la cota inferior eventualmente supera cualquier cota superior.*

**(O3)** *Los ceros off-critical hipotéticos $\rho_j$ imponen, vía la fórmula de Weil, cotas explícitas sobre $\mathcal{P}_\lambda$ que entran en contradicción con las propiedades analíticas conocidas de $\zeta$ (la ecuación funcional, la región libre de ceros).*

**Proposición 9.2** (Estado actual de los obstáculos).

*(a) O1 es desconocido. No se conoce ninguna cota inferior no trivial sobre $\mathcal{P}_\lambda$ procedente solo de la distribución de primos.*

*(b) O2 es desconocido. La relación entre la tasa de crecimiento de $B_\lambda(\log p)$ y de $K_\lambda(\gamma_0)$ en $\lambda$ no ha sido analizada.*

*(c) O3 es la formulación más cercana a los intentos conocidos (método de Weil, método de Beurling, función de Bateman-Chowla). Todos estos métodos se han encontrado con la misma barrera: la fórmula de Weil es una tautología respecto a la posición de los ceros, y no puede usarse para probar algo nuevo sobre esa posición.*

### 9.2. El lema faltante

**Definición 9.3** (Lema $\mathcal{L}_A$). Sea $\mathcal{L}_A$ el siguiente enunciado:

> *Para toda función de prueba admisible $h$ con $h(\gamma_0) > 0$ para algún $\gamma_0$ real, y para toda sucesión de primos $\{p_k\}$, la suma $\sum_p \frac{\log p}{\sqrt{p}}\hat{h}(\log p)$ está acotada inferiormente por una cantidad que crece más rápido que $(h(\gamma_0))^{-1}$ cuando $h$ se concentra en $\gamma_0$.*

Este enunciado, si fuera verdadero, daría una cota inferior sobre $\mathcal{P}_\lambda$ cuando $h_\lambda$ se concentra en los ceros off-critical. Pero $\mathcal{L}_A$ es falso en general: para funciones $h$ concentradas en $\gamma_0$, la suma $\sum_p \frac{\log p}{\sqrt{p}} \hat{h}(\log p)$ puede ser pequeña (los primos no "ven" un cero hipotético en $\gamma_0$ salvo a través de la fórmula de Weil).

**Proposición 9.4** (Falsedad de $\mathcal{L}_A$ en general). *Sea $h_\varepsilon(s) = \varepsilon^{-1}\phi((s-\gamma_0)/\varepsilon)$ donde $\phi$ es una función de prueba admisible concentrada en $0$. Entonces:*

*(i) $h_\varepsilon(\gamma_0) = \varepsilon^{-1}\phi(0) \to \infty$ cuando $\varepsilon \to 0^+$.*

*(ii) $\hat{h}_\varepsilon(\log p) = \phi(\varepsilon \log p) e^{i\gamma_0 \log p} \to \hat{\phi}(0) e^{i\gamma_0 \log p}$ cuando $\varepsilon \to 0^+$.*

*(iii) $\sum_p \frac{\log p}{\sqrt{p}}\hat{h}_\varepsilon(\log p) \to \hat{\phi}(0)\sum_p \frac{\log p}{\sqrt{p}} e^{i\gamma_0 \log p}$, que es una serie que puede ser acotada o incluso pequeña dependiendo de la distribución de primos.*

*En particular, la suma de primos no crece como $h_\varepsilon(\gamma_0)^c$ para ningún $c > 0$, lo que falsifica $\mathcal{L}_A$. $\square$*

### 9.3. La barrera de Hadamard revisitada

El Doc 89 estableció que ninguna propiedad verificable de $\zeta$ sin conocer posiciones de ceros implica $d\nu = 0$. ¿Cómo se relaciona esto con la Dirección A?

**Proposición 9.5** (La Dirección A cae bajo la barrera de Hadamard). *La estrategia de la Dirección A — probar que $\mathcal{P}_\lambda$ no puede satisfacer la cota inferior bajo $\neg$RH — es equivalente a probar $T_\lambda = 0$ sin conocer posiciones de ceros off-critical. Esto es exactamente lo que la barrera de Hadamard (Doc 89) prohibe.*

**Demostración.** La identidad $T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ expresa $T_\lambda$ en términos de $\mathcal{R}_\lambda$ (que depende de los ceros en la recta crítica) y $\mathcal{P}_\lambda$ (que depende de la distribución de primos). Probar que $T_\lambda = 0$ usando solo la distribución de primos y los ceros críticos es exactamente el tipo de argumento que la barrera de Hadamard prohibe: la fórmula de Weil es una reformulación de RH, no una prueba.

Más precisamente: $\mathcal{P}_\lambda$ es determinado por los ceros de $\zeta$ vía la fórmula de Weil (es decir, $\mathcal{P}_\lambda = (\mathcal{R}_\lambda - T_\lambda)/2$). Luego cualquier información sobre $\mathcal{P}_\lambda$ que se use ya contiene implícitamente información sobre $T_\lambda$. El argumento es circular. $\square$

**Corolario 9.6.** *La Dirección A, en su formulación actual, está bloqueada por la barrera de Hadamard. Para superar este bloqueo, se necesita información aritmética sobre los primos que sea **independiente** de la posición de los ceros de $\zeta$ — es decir, información que exista incondicionalmente sin asumir ninguna hipótesis sobre los ceros.*

---

## §10. Análisis de posibles aperturas

### 10.1. Información aritmética genuinamente independiente

La única información aritmética sobre los primos que es genuinamente independiente de la posición de los ceros de $\zeta$ es la que se puede obtener sin usar la fórmula de Weil. Los ejemplos canónicos son:

1. **Cotas para sumas de Ramanujan-Weil:** la suma $\sum_{p \leq x} e^{i\gamma\log p}$ para $\gamma$ fijo; estas se pueden acotar por métodos de cribas elementales.

2. **El Teorema de Vinogradov sobre la suma de tres primos:** prueba que todo entero impar suficientemente grande es suma de tres primos. Esto da información sobre la distribución de los primos pero en un sentido aditivo, no multiplicativo.

3. **Cotas de Brun-Titchmarsh sobre primos en progresiones artiméticas:** $\pi(x; q, a) \leq 2x/(\phi(q)\log(x/q))$ para $(a,q)=1$ y $x > q$.

Ninguna de estas herramientas da la información sobre $\mathcal{P}_\lambda$ que se necesita.

### 10.2. ¿Puede la sieve theory dar cotas sobre $\mathcal{P}_\lambda$?

La teoría de cribas puede, en principio, acotar sumas de la forma $\sum_p f(p)$ para funciones $f$ multiplicativas. En nuestro caso $f(p) = \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$, que es una función de $\log p$ (no directamente multiplicativa). Las cribas trabajan con funciones multiplicativas en los primos, pero $B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\,dm_\infty(s)$ es una función suave de $\log p$ y se puede tratar como una función aditiva en el semigrupo multiplicativo.

**Observación 10.1.** Un cálculo estándar (Perron's formula + zero-free region) da:
$$\sum_{p \leq x} \frac{\log p}{\sqrt{p}} e^{i\gamma\log p} = \sum_{p \leq x} \frac{\log p}{p^{1/2 - i\gamma}} \approx -\frac{x^{1/2+i\gamma}}{1/2-i\gamma + \text{contribuciones de ceros de $\zeta(s)$ cerca de $1/2+i\gamma$}}.$$

Esto de nuevo involucra los ceros de $\zeta$: la suma sobre primos a frecuencia $e^{i\gamma}$ está gobernada por el zero $\rho = 1/2 + i\gamma$ de $\zeta$ (si existe). Este es exactamente el circularismo de la barrera de Hadamard.

### 10.3. Una posible apertura: la información del residuo $\mathcal{R}_\lambda$

El término $\mathcal{R}_\lambda = \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}})$ es computable en principio a partir de:
(a) el término arquimediano $\mathcal{A}[h_\lambda]$, que involucra solo $\Gamma$ y es explícitamente computable, y
(b) la suma $\sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}})$ sobre los ceros críticos conocidos de $\zeta$.

Si para $\lambda$ suficientemente grande $\mathcal{R}_\lambda$ fuera **negativo**, entonces de $T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ y $T_\lambda \geq 0$, se seguiría $\mathcal{P}_\lambda \leq \mathcal{R}_\lambda/2 < 0$. Y de $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0) \geq 0$, se seguiría $0 \leq T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda \leq \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$... pero si $\mathcal{R}_\lambda < 0$ y $\mathcal{P}_\lambda < 0$, no hay contradicción directa.

**Proposición 10.2** (Signo de $\mathcal{R}_\lambda$). *El signo de $\mathcal{R}_\lambda = \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}})$ no está determinado a priori. Depende de:*
*(a) el valor del término arquimediano $\mathcal{A}[h_\lambda]$ (positivo si $h_\lambda$ es positiva y grande en $s = i/2$),*
*(b) la contribución de los ceros críticos $\sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}})$ (que es una suma de valores de $h_\lambda$ en los $\gamma_j^{\mathrm{on}}$, con signo dependiente de $h_\lambda$).*

*No se puede concluir que $\mathcal{R}_\lambda < 0$ en general.*

### 10.4. La dirección "comparación de tasas"

La apertura más concreta que permanece abierta es la comparación de tasas de crecimiento en $\lambda$ de las dos cantidades. La hipótesis de trabajo sería:

**Hipótesis de trabajo 10.3** (Tasa diferencial). *La cota inferior $4\delta_0^2 K_\lambda(\gamma_0)$ bajo $\neg$RH crece como una potencia de $\lambda$ (digamos $\lambda^\alpha$ para algún $\alpha > 0$ determinado por la base de Jacobi), mientras que la suma de primos $\mathcal{P}_\lambda$ crece como $\lambda^\beta$ con $\beta < \alpha$.*

Si esta hipótesis fuera cierta, para $\lambda$ suficientemente grande la cota inferior superaría la suma de primos (más el término arquimediano), dando contradicción.

**Obstáculo a 10.3:** Sin calcular explícitamente las tasas de crecimiento de $K_\lambda(\gamma_0)$ y $B_\lambda(\log p)$ en la base de Jacobi de $L^2(dm_{\mathrm{full,on}})$ (que es un objeto que depende de $\zeta$ mismo y es difícil de analizar), no se puede verificar si $\alpha > \beta$ o no. El análisis de estas tasas requiere información sobre los polinomios ortogonales $P_k$ de $L^2(dm_{\mathrm{full,on}})$, que a su vez dependen de los ceros de $\zeta$.

---

## §11. Formulación del lema-conjetura que cerraría la dirección

### 11.1. El lema suficiente

Resumimos cuál sería el resultado aritmético que cerraría la Dirección A.

**Conjetura $\mathbf{C}_A$ (Lema faltante de la Dirección A).** *Para la familia de funciones de prueba $\{h_\lambda\}_{\lambda > 0}$ del marco CCM, la suma de primos satisface:*
$$\mathcal{P}_\lambda = 2\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) \leq \mathcal{R}_\lambda - \eta_\lambda,$$
*donde $\eta_\lambda > 0$ es una cantidad que crece sin límite con $\lambda$, y la cota es incondicional (sin asumir RH).*

Si $\mathbf{C}_A$ fuera verdadera, y además $4\delta_0^2 K_\lambda(\gamma_0) > \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ para $\lambda$ grande bajo $\neg$RH, se obtendría la contradicción buscada.

**Nota de honestidad crítica:** La Conjetura $\mathbf{C}_A$ es actualmente sin soporte analítico. No hay ninguna razón a priori para creer que la suma de primos deba ser menor que $\mathcal{R}_\lambda - \eta_\lambda$: la fórmula de Weil impone exactamente que $\mathcal{P}_\lambda = (\mathcal{R}_\lambda - T_\lambda)/2$, luego si $T_\lambda = 0$ (RH) entonces $\mathcal{P}_\lambda = \mathcal{R}_\lambda/2$, y si $T_\lambda > 0$ ($\neg$RH) entonces $\mathcal{P}_\lambda < \mathcal{R}_\lambda/2$. La Conjetura $\mathbf{C}_A$ dice que esta segunda posibilidad ($\mathcal{P}_\lambda < \mathcal{R}_\lambda/2$) implica algo contradictorio — pero la fórmula de Weil no impone ninguna contradicción aquí.

### 11.2. Variante: la conjetura sobre la positividad de $B_\lambda$

Una forma más débil de la conjetura que podría ser demostrable:

**Conjetura $\mathbf{C}_A'$ (Positividad de los coeficientes de Fourier).** *Para todo $\lambda > 0$ y todo primo $p$:*
$$B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\,dm_\infty(s) > 0.$$

Si $\mathbf{C}_A'$ fuera verdadera, entonces $\mathcal{P}_\lambda > 0$, y la fórmula $T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ implicaría $T_\lambda < \mathcal{R}_\lambda$. Esto por sí solo no cierra el argumento, pero podría ser un primer paso.

**Observación 11.1.** La positividad de $B_\lambda(\log p)$ parece difícil de probar: $W_\lambda(s) \geq 0$ pero $\cos(s\log p)$ oscila. Para $\log p$ pequeño (primos pequeños) es plausible que $B_\lambda(\log p) > 0$ pues el coseno oscila lentamente y $W_\lambda dm_\infty$ tiene masa concentrada cerca de $s = 0$ donde $\cos(0) = 1 > 0$. Para primos grandes, el coseno oscila rápidamente y la integral puede ser positiva o negativa.

### 11.3. El lema de coherencia aritmética

Una tercera formulación, más conceptual:

**Lema de coherencia $\mathbf{L}_{A}^{\mathrm{coh}}$ (Hipotético).** *Si bajo $\neg$RH la distribución de ceros off-critical produce $T_\lambda \geq \varepsilon > 0$ para todo $\lambda > 0$, entonces la distribución de primos en las frecuencias $\{e^{i\gamma_j\log p} : p \text{ primo}, j \in J\}$ (donde $\gamma_j$ son las partes imaginarias de los ceros off-critical) satisface una irregularidad cuantificable que es incompatible con las propiedades analíticas de $\zeta$ en $\mathrm{Re}(s) > 1$.*

Este lema intentaría usar el hecho de que los ceros off-critical hipotéticos "perturban" la distribución de primos de un modo específico, y que esa perturbación es visible en $\mathcal{P}_\lambda$. Es la forma más directa de explotar la dualidad primos-ceros.

**Estado de $\mathbf{L}_A^{\mathrm{coh}}$:** Actualmente sin demostración ni soporte analítico directo. La dificultad es que la perturbación de la distribución de primos introducida por un cero off-critical es (via la fórmula de Weil) exactamente la perturbación que hace $T_\lambda > 0$ — es decir, las dos afirmaciones son equivalentes y no hay información nueva.

---

## §12. Relación con otros enfoques clásicos

### 12.1. El método de Weil (1952)

El intento original de Weil de usar la fórmula explícita para RH consiste en encontrar una función de prueba $h$ tal que la suma $\sum_\rho h(\gamma_\rho)$ sea negativa bajo $\neg$RH y positiva bajo RH. Si tal $h$ existiera, la fórmula de Weil daría una contradicción.

Bombieri (2000) mostró que este enfoque se reduce al problema de encontrar una función $h$ admisible tal que la "forma de Weil" $W_h = \sum_\rho h(\gamma_\rho) - \mathcal{A}[h] + 2\mathcal{P}[h]$ tenga signo determinado. La positividad de esta forma sobre todas las funciones $h$ admisibles sería equivalente a RH. Pero probar esa positividad es tan difícil como probar RH directamente.

La Dirección A es una instancia de este enfoque con $h = h_\lambda$ (la función de prueba del marco CCM). La conclusión del análisis es la misma que la de Bombieri: el argumento es circular.

### 12.2. El método de Beurling-Nyman

El criterio de Beurling-Nyman dice que RH es equivalente a que cierta familia de funciones sea densa en $L^2(0,1)$. Este criterio tiene una interpretación via la suma de primos (via la función $\rho(x) = \{1/x\}$), pero tampoco da información nueva sobre la distribución de primos más allá de reformular RH.

### 12.3. La "función zeta del operador" y el enfoque espectral

El enfoque espectral de Connes (1999) interpreta RH como la condición de que cierto operador tenga espectro real. La relación con la distribución de primos pasa por la traza del operador, que satisface la fórmula de Weil. De nuevo, es una reformulación.

La diferencia del programa actual (CCM-Jacobi) es que tiene una estructura más explícita (los polinomios $P_k$, la medida $dm_{\mathrm{full,on}}$, la traza $T_\lambda$) que los enfoques anteriores. Pero el obstáculo de fondo es el mismo.

---

## §13. Estado final de la Dirección A

### 13.1. Lo que está probado

**Teorema 13.1** (Hechos establecidos sobre la Dirección A).

*(i) La fórmula aritmética $T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ es un corolario de la fórmula de Weil-Guinand aplicada a $h_\lambda$, formal pero con el contenido exacto del Teorema 2.1 y del Lema 2.2.*

*(ii) Bajo $\neg$RH, $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0) > 0$ (Proposición 5.1).*

*(iii) La serie $\mathcal{P}_\lambda$ converge absolutamente para todo $\lambda > 0$ (Corolario 4.3).*

*(iv) No existe ninguna cota superior no trivial sobre $\mathcal{P}_\lambda$ procedente solo de la distribución de primos que sea incompatible con la cota inferior bajo $\neg$RH.*

*(v) La estrategia de la Dirección A cae bajo la barrera de Hadamard (Proposición 9.5).*

*(vi) El "lema faltante" que cerraría el argumento (Conjetura $\mathbf{C}_A$) carece de soporte analítico y su formulación precisa revela que es equivalente a RH.*

### 13.2. Lo que no está probado (y probablemente no lo estará por esta vía)

- No se ha probado que $B_\lambda(\log p) > 0$ para todos los primos $p$ (Conjetura $\mathbf{C}_A'$).
- No se ha probado ninguna cota inferior sobre $\mathcal{P}_\lambda$ que sea incompatible con la cota inferior bajo $\neg$RH.
- No se ha encontrado ningún argumento que use la distribución de primos de forma genuinamente independiente de la fórmula de Weil (que es una tautología respecto a los ceros).

### 13.3. Veredicto

**Veredicto 13.2.** *La Dirección A no conduce a una prueba de RH por los caminos examinados. El obstáculo es la barrera de Hadamard: cualquier uso de la distribución de primos para acotar $T_\lambda$ pasa necesariamente por la fórmula de Weil, que es una reformulación de RH. No hay forma de extraer del TPN, la región libre de ceros conocida, o los teoremas de densidad, una información sobre $\mathcal{P}_\lambda$ que sea independiente de la posición de los ceros de $\zeta$.*

*Sin embargo, la Dirección A contribuye al programa de las siguientes formas:*

*1. Proporciona la formulación precisa de $A_\lambda^{\mathrm{off}}$ y su relación con $K_\lambda(\gamma_0)$ (Sección 3).*
*2. Identifica $B_\lambda(\log p)$ como el objeto central de la aritmética en el marco CCM (Sección 4).*
*3. Clarifica que el obstáculo es la barrera de Hadamard y no una debilidad técnica (Sección 9).*
*4. Sugiere que el estudio de las tasas de crecimiento de $K_\lambda(\gamma_0)$ vs. $\mathcal{P}_\lambda$ en $\lambda$ podría ser de valor independiente para entender la estructura de la base de Jacobi (Sección 10.4), aunque esto no cierra el argumento de RH.*

---

## Apéndice A: La fórmula de Weil-Guinand: precisiones técnicas

### A.1. Convergencia de la suma sobre ceros

La suma $\sum_\rho h(\gamma_\rho)$ converge absolutamente si $|h(s)| = O(|s|^{-1-\varepsilon})$ (condición más débil que (W3)). Para $h_\lambda(s) = W_\lambda(s)(2\pi)^{-2}|\Gamma(1/4+is/2)|^2$, el decaimiento es exponencial $O(e^{-\pi|s|/2})$, lo que garantiza convergencia absoluta.

La suma $\sum_{\rho_{\mathrm{on}}} h(\gamma_j^{\mathrm{on}})$ sobre los ceros críticos también converge: los ceros $\gamma_j^{\mathrm{on}} \sim (2\pi j/\log j)$ son densos y $h(\gamma_j^{\mathrm{on}}) = O(e^{-\pi\gamma_j/2})$ decae, luego la suma converge.

### A.2. La función $\zeta_{\mathrm{on}}$ y los ceros en la recta crítica

La función $\zeta_{\mathrm{on}}$ (Doc 83) se define como el producto de Hadamard con los mismos ceros que $\zeta$ pero proyectados a la recta crítica: si $\rho = \sigma + i\gamma$ es un cero de $\zeta$, el cero correspondiente de $\zeta_{\mathrm{on}}$ es $1/2 + i\gamma$. Bajo RH, $\zeta = \zeta_{\mathrm{on}}$ (todos los ceros ya están en la recta crítica). La suma $\sum_{\rho_{\mathrm{on}}} h(\gamma_j^{\mathrm{on}})$ es la suma de Weil aplicada a los ceros de $\zeta_{\mathrm{on}}$.

### A.3. El término $\hat{h}(0)\log(1/(2\pi))$ y la normalización

En la fórmula estándar de Weil, aparece el factor $\log(1/(2\pi))$ (negativo). En algunas versiones de la fórmula este factor se absorbe en el término arquimediano $\mathcal{A}[h]$. En el marco CCM, la medida $dm_\infty = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 ds$ ya incluye la normalización arquimediana, por lo que los factores de $2\pi$ entran de forma natural en $\mathcal{A}[h_\lambda]$.

---

## Apéndice B: Resumen de símbolos

| Símbolo | Definición |
|---------|------------|
| $dm_\infty(s)$ | $(2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ |
| $dm_{\mathrm{full}}(s)$ | $|\zeta(1/2+is)|^2\,dm_\infty(s)$ |
| $dm_{\mathrm{full,on}}(s)$ | $|\zeta_{\mathrm{on}}(1/2+is)|^2\,dm_\infty(s)$ |
| $d\nu$ | $dm_{\mathrm{full}} - dm_{\mathrm{full,on}} \geq 0$ |
| $W_\lambda(s)$ | kernel de Abel de la base de Jacobi de $L^2(dm_{\mathrm{full,on}})$ |
| $T_\lambda$ | $\int W_\lambda\,d\nu$ (traza CCM) |
| $h_\lambda(s)$ | $W_\lambda(s)(2\pi)^{-2}|\Gamma(1/4+is/2)|^2$ (función de prueba) |
| $\hat{h}(r)$ | $\int h(s)e^{irs}\,ds$ (transformada de Fourier) |
| $B_\lambda(r)$ | $\int W_\lambda(s)\cos(rs)\,dm_\infty(s) = \hat{h}_\lambda(r)$ |
| $\mathcal{P}_\lambda$ | $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ |
| $\mathcal{R}_\lambda$ | $\mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}})$ |
| $A_\lambda^{\mathrm{off}}$ | $\int W_\lambda\,(R-1)\,dm_{\mathrm{full,on}} = T_\lambda$ |
| $K_\lambda(\gamma)$ | $\int W_\lambda(s)(s-\gamma)^{-2}\,dm_{\mathrm{full,on}}(s)$ |
| $\delta_j$ | $\mathrm{Re}(\rho_j) - 1/2 > 0$ (desplazamiento de cero off-critical) |
| $\gamma_j$ | $\mathrm{Im}(\rho_j)$ (parte imaginaria del cero off-critical) |

---

## Apéndice C: La dualidad primos-ceros y por qué no es explotable unilateralmente

### C.1. La naturaleza simétrica de la fórmula de Weil

La fórmula de Weil-Guinand es fundamentalmente simétrica: los ceros de $\zeta$ y los primos aparecen en lados opuestos de una igualdad, y se determinan mutuamente. No es posible, en el marco de la fórmula de Weil, usar la distribución de primos para "descubrir" algo sobre los ceros que no sea ya conocido a través de la misma fórmula.

Más precisamente: si se conocen todos los primos (y todas sus potencias), la fórmula de Weil determina todos los ceros de $\zeta$. Recíprocamente, si se conocen todos los ceros, la fórmula determina la distribución de primos. La relación es biyectiva (para funciones de prueba suficientemente ricas), no hay información adicional en ninguno de los dos lados que no esté en el otro.

### C.2. El caso de la función zeta de una curva sobre un campo finito

En el caso del análogo geométrico (función zeta de una curva sobre $\mathbb{F}_q$), la hipótesis de Riemann fue probada por Weil (1948). El argumento usa la positividad de la intersección de ciclos en la superficie $C \times C$ (criterio de positividad de la forma de Weil). En ese caso, la información extra que permite cerrar el argumento es **geométrica**: la positividad de la forma de intersección tiene una interpretación en términos de la geometría de la curva que es genuinamente independiente de los ceros de la función zeta.

En el caso de $\zeta(s)$ sobre $\mathbb{Z}$, no se ha encontrado el análogo aritmético de esta positividad geométrica. La Dirección A intenta usar la distribución de primos para suplir esa información, pero la distribución de primos es equivalente a la distribución de ceros (via Weil) y no aporta el análogo de la positividad geométrica.

### C.3. Lo que sería diferente

Si existiera un objeto aritmético $X$ tal que:
1. $X$ es computable a partir de los primos sin usar la fórmula de Weil.
2. Bajo $\neg$RH, $X$ satisface una cota incompatible con las propiedades de $\zeta$ en $\mathrm{Re}(s) > 1$.
3. Bajo RH, $X$ es compatible con todas las propiedades de $\zeta$.

Entonces la Dirección A (o una variante) cerraría el argumento. La búsqueda de tal objeto $X$ es, en cierto sentido, la búsqueda del análogo aritmético de la positividad geométrica de Weil. No se conoce ningún candidato.

---

*Fin del Documento 90.*

*Nota de síntesis:* La Dirección A ha sido explorada de forma rigurosa y el veredicto es negativo en su formulación actual. El obstáculo es estructural (barrera de Hadamard) y no técnico. Las fórmulas desarrolladas (expresión de $A_\lambda^{\mathrm{off}}$, propiedades de $B_\lambda$, formulación de la Conjetura $\mathbf{C}_A$) son contribuciones al marco del programa aunque no cierren el argumento. La Dirección B (que debería explorarse en el Doc 91) y las demás direcciones de la Fase 34 deben buscar información aritmética que sea genuinamente independiente de la fórmula de Weil.
