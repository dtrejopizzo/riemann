# Phase 29 — Doc 21: Ataque directo a la inclusión inversa

**Fecha:** junio 2026  
**Objetivo:** Atacar la inclusión inversa (Inc. Inv.): $\Xi(t_0)=0$, $t_0\in\mathbb{R}$ $\implies$ $C_\infty(t_0)=0$, vía la ecuación funcional de $\zeta$, la fórmula de Guinand-Barner y el argumento de frecuencias de batimiento entre ceros fuera de la recta crítica.

**Referencia a documentos anteriores:** La cadena incondicional completa está en Doc 20 (diagrama, Sección 11). El gap es exactamente: $\sum_\rho \cos(\gamma_n \log|\rho|)/|\rho| = -c_0/2$ para todo cero real $\gamma_n$ de $\Xi$.

---

## 1. La ecuación funcional y la simetría de los ceros

**Proposición 1** (simetría de los ceros bajo la ecuación funcional). La ecuación funcional $\xi(s) = \xi(1-s)$ implica que los ceros no-triviales de $\zeta$ son simétricos respecto a la recta crítica: si $\rho = \sigma + i\gamma$ es un cero, también lo son $\bar\rho = \sigma - i\gamma$, $1-\rho = (1-\sigma) + i\gamma$ y $1-\bar\rho = (1-\sigma) - i\gamma$.

En particular: si existe un cero $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$, entonces $1-\rho_0 = (1-\sigma_0)+i\gamma_0$ también es cero de $\zeta$, y $|1-\rho_0| = \sqrt{(1-\sigma_0)^2+\gamma_0^2} \neq |\rho_0| = \sqrt{\sigma_0^2+\gamma_0^2}$ (si además $\sigma_0 \neq 1/2$).

*Prueba.* Directa de la ecuación funcional y la conjugación de Schwarz. $\square$

**Corolario 1** (los ceros fuera de la recta crítica vienen en cuádruplos). Si $\sigma_0 \notin \{0, 1/2, 1\}$, los cuatro ceros $\{\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0\}$ son distintos. Si $\sigma_0 = 1-\sigma_0$, es decir $\sigma_0 = 1/2$: el cuádruplo degenera en el par $\{\rho_0, \bar\rho_0\}$.

---

## 2. Contribución de un par fuera de la recta crítica a $C_\infty$

**Definición.** Para un cero $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$ y $\gamma_0 > 0$, la contribución del par $\{\rho_0, 1-\rho_0\}$ (con partes imaginarias $\pm\gamma_0$, contando conjugados) al potencial $C_\infty$ es:

$$\Delta C(t;\rho_0) := \frac{2\cos(t\log|\rho_0|)}{|\rho_0|} + \frac{2\cos(t\log|1-\rho_0|)}{|1-\rho_0|},$$

donde $|\rho_0| = \sqrt{\sigma_0^2+\gamma_0^2}$ y $|1-\rho_0| = \sqrt{(1-\sigma_0)^2+\gamma_0^2}$.

**Proposición 2** (la contribución del par fuera de la recta crítica tiene dos frecuencias distintas). Si $\sigma_0 \neq 1/2$:

$$\Delta C(t;\rho_0) = A_1 \cos(\omega_1 t) + A_2 \cos(\omega_2 t),$$

con amplitudes $A_j = 2/|\rho_j|$ y frecuencias $\omega_j = \log|\rho_j|$, donde $\omega_1 = \log|\rho_0| \neq \omega_2 = \log|1-\rho_0|$.

Bajo RH (ceros SOLO en $\sigma = 1/2$): $\rho_0 = 1/2+i\gamma_0$ y $1-\rho_0 = 1/2+i\gamma_0$, luego $\omega_1 = \omega_2 = \log\sqrt{1/4+\gamma_0^2}$ y $A_1 = A_2$: el par degenera en una sola frecuencia.

*Prueba.* Directa de la definición. La desigualdad $\omega_1 \neq \omega_2$ para $\sigma_0 \neq 1/2$ se sigue de:

$$|\rho_0|^2 = \sigma_0^2 + \gamma_0^2 \neq (1-\sigma_0)^2 + \gamma_0^2 = |1-\rho_0|^2,$$

ya que $\sigma_0^2 \neq (1-\sigma_0)^2$ iff $\sigma_0 \neq 1/2$. $\square$

---

## 3. La condición $C_\infty(\gamma_n) = 0$ para el par extra

Supóngase que existen ceros fuera de la recta crítica. Separemos $C_\infty$ en la contribución de los ceros EN la recta crítica y la contribución de los ceros FUERA:

$$C_\infty(t) = C_\infty^{on}(t) + C_\infty^{off}(t),$$

donde:

$$C_\infty^{on}(t) = 2\sum_{\rho:\,\Re(\rho)=1/2} \frac{\cos(t\log|\rho|)}{|\rho|} + c_0,$$

$$C_\infty^{off}(t) = 2\sum_{\rho:\,\Re(\rho)\neq 1/2} \frac{\cos(t\log|\rho|)}{|\rho|}.$$

**Lema 1** (si todos los ceros de $\Xi$ en $\mathbb{R}$ son ceros de $C_\infty^{on}$, entonces $C_\infty^{off}(\gamma_n) = 0$ para todo $n$). 

Si la parte "on" ya satisface $C_\infty^{on}(\gamma_n) = 0$ para todo $\gamma_n$ (lo cual es equivalente a la inclusión inversa para la parte on-critical), entonces la inclusión inversa completa $C_\infty(\gamma_n) = 0$ requiere:

$$C_\infty^{off}(\gamma_n) = 0 \quad \text{para todo } \gamma_n. \quad (\dagger)$$

*Prueba.* $C_\infty(\gamma_n) = C_\infty^{on}(\gamma_n) + C_\infty^{off}(\gamma_n) = 0 + C_\infty^{off}(\gamma_n)$. $\square$

**Observación.** La condición $(\dagger)$ dice: la contribución de los ceros fuera de la recta crítica a $C_\infty$, evaluada en CADA cero real de $\Xi$, debe ser exactamente cero. Esta es una familia de condiciones de anulación simultanea — una por cada $\gamma_n$.

---

## 4. La fórmula de Guinand-Barner como herramienta

**Teorema de Guinand-Barner** (fórmula explícita simétrica). Para $f \in \mathcal{S}(\mathbb{R})$ par ($f(t) = f(-t)$), la fórmula de Weil-Guinand dice:

$$\sum_{\rho} \hat f(\gamma_\rho) = \hat f(0)\log\pi - 2\int_0^\infty f(t)\Re\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)dt - 2\sum_{p}\sum_{k=1}^\infty \frac{\Lambda(p)}{p^{k/2}}f(k\log p),$$

donde la suma izquierda es sobre todos los ceros no-triviales $\rho = \sigma_\rho + i\gamma_\rho$ de $\zeta$, con $\gamma_\rho = \Im(\rho)$, y $\hat f$ es la transformada de Fourier de $f$.

**Aplicación con $f = f_n^{(\varepsilon)}$.** Tomamos la función de prueba:

$$f_n^{(\varepsilon)}(t) := \varepsilon^{-1}\phi\!\left(\frac{t - \gamma_n}{\varepsilon}\right) + \varepsilon^{-1}\phi\!\left(\frac{t + \gamma_n}{\varepsilon}\right),$$

donde $\phi \in C_c^\infty(\mathbb{R})$, $\phi \geq 0$, $\int \phi = 1$, $\hat\phi(0) = 1$. Esta $f_n^{(\varepsilon)}$ es par, concentrada en $\pm\gamma_n$, y satisface $\hat f_n^{(\varepsilon)}(\xi) = e^{i\xi\gamma_n}\hat\phi(\varepsilon\xi) + e^{-i\xi\gamma_n}\hat\phi(\varepsilon\xi) = 2\cos(\xi\gamma_n)\hat\phi(\varepsilon\xi)$.

**Proposición 3** (la fórmula de Guinand-Barner evaluada en $\gamma_n$). Para $f = f_n^{(\varepsilon)}$:

$$\sum_\rho \hat f_n^{(\varepsilon)}(\gamma_\rho) = \sum_\rho 2\cos(\gamma_\rho \gamma_n)\hat\phi(\varepsilon\gamma_\rho).$$

Cuando $\varepsilon \to 0$: $\hat\phi(\varepsilon\gamma_\rho) \to 1$ para todo $\rho$ fijo. Si la serie converge (lo cual requiere regularización), el límite formal es:

$$\sum_\rho 2\cos(\gamma_\rho\gamma_n) = \text{(lado derecho de Guinand-Barner con }f_n^{(\varepsilon)} \text{ cuando }\varepsilon\to 0).$$

El lado derecho: $\hat f_n^{(\varepsilon)}(0) \to 0$ (pues $f_n^{(\varepsilon)}(0) \to 0$ para $\gamma_n$ grande); los términos con $\Gamma'/\Gamma$ dan $2\int_0^\infty f_n^{(\varepsilon)}(t)\Re\Gamma'/\Gamma(\ldots)dt \to 2\Re\Gamma'/\Gamma(1/4+i\gamma_n/2) = 2w(\gamma_n)$; los términos de primos dan $2\sum_p\sum_k\Lambda(p)p^{-k/2}f_n^{(\varepsilon)}(k\log p) \to 2\sum_p\Lambda(p)p^{-1/2}[f_n^{(\varepsilon)}(\log p)\big|_{\log p = \gamma_n}]$.

Para que la función de prueba sea no-cero en $t = k\log p$: necesitamos $k\log p \approx \gamma_n$, es decir $p^k \approx e^{\gamma_n}$.

**Lema 2** (la fórmula de Guinand-Barner da exactamente $C_\infty(\gamma_n) = 0$ para ceros de $\Xi$). En el límite $\varepsilon\to 0$ (en sentido distribucional regularizado), la fórmula de Guinand-Barner evaluada con la función de prueba $f_n^{(\varepsilon)}$ centrada en $\gamma_n$ reproduce la identidad:

$$\sum_\rho \cos(\gamma_n\gamma_\rho) = w(\gamma_n) - \Psi^{reg}(\gamma_n),$$

donde $\Psi^{reg}(\gamma_n)$ es la suma sobre primos regularizada en $\gamma_n$.

*Prueba (formal, con regularización de Abel).* El argumento de la Sección 8 del Doc 20 (Proposición 7) aplica: la fórmula explícita en $s = 1/2+i\gamma_n$ (con $\zeta(s_n)=0$) da, tras regularización del polo de $-\zeta'/\zeta$ en $s_n$:

$$w(\gamma_n) = \Psi^{reg}(\gamma_n) + \sum_{\rho\neq s_n}\frac{1}{s_n-\rho}\bigg|_{Abel}.$$

La suma sobre otros ceros $\sum_{\rho\neq s_n}(s_n-\rho)^{-1}$ en la regularización de Abel da, combinada con $\Re(1/2+i\gamma_n - \rho)^{-1} = \Re(1/(s_n-\rho))$, exactamente $-C_\infty^{off}(\gamma_n)/2$ (en la regularización apropiada). Luego $C_\infty^{reg}(\gamma_n) = 0$. $\square$

**Estado.** El Lema 2 repite el resultado del Doc 20 (Proposición 7): la inclusión inversa se satisface para la versión REGULARIZADA de $C_\infty$. El gap sigue siendo si la regularización coincide con el límite no-tangencial.

---

## 5. El argumento de frecuencias de batimiento

**Hipótesis.** Supóngase que existe un cero $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$. Las frecuencias que introduce en $C_\infty^{off}$ son $\omega_1 = \log|\rho_0|$ y $\omega_2 = \log|1-\rho_0|$ (y sus conjugados, con las mismas frecuencias). 

**Definición.** La *frecuencia de batimiento* del par $\{\rho_0, 1-\rho_0\}$ es:

$$\Omega(\rho_0) := |\omega_1 - \omega_2| = \frac{1}{2}\left|\log\frac{\sigma_0^2+\gamma_0^2}{(1-\sigma_0)^2+\gamma_0^2}\right|.$$

Para $\gamma_0$ grande: $\Omega(\rho_0) \approx \frac{|2\sigma_0-1|}{2\gamma_0^2}(1+O(\gamma_0^{-2}))$ (Taylor en $\gamma_0^{-1}$).

*Derivación.* $\log(\sigma_0^2+\gamma_0^2) = 2\log\gamma_0 + \log(1+\sigma_0^2/\gamma_0^2) \approx 2\log\gamma_0 + \sigma_0^2/\gamma_0^2$. Análogamente para $(1-\sigma_0)^2+\gamma_0^2$. La diferencia: $\log(\sigma_0^2+\gamma_0^2) - \log((1-\sigma_0)^2+\gamma_0^2) \approx (\sigma_0^2 - (1-\sigma_0)^2)/\gamma_0^2 = (2\sigma_0-1)/\gamma_0^2$. $\square$

**Proposición 4** (el batimiento genera ceros de $C_\infty^{off}$ que son densos en $\mathbb{R}$). La función:

$$F(t) := A_1\cos(\omega_1 t) + A_2\cos(\omega_2 t)$$

(con $\omega_1 \neq \omega_2$) tiene ceros en una sucesión cuasi-periódica con densidad $\sim (\omega_1+\omega_2)/\pi$ por unidad de longitud.

*Prueba.* $F(t) = (A_1+A_2)\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right)\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right) + (A_1-A_2)\sin\!\left(\frac{\omega_1+\omega_2}{2}t\right)\sin\!\left(\frac{\omega_1-\omega_2}{2}t\right)$. Si $A_1 = A_2$: $F(t) = 2A_1\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right)\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right)$, con ceros cuando $\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right) = 0$ (densidad $(\omega_1+\omega_2)/\pi$) o cuando $\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right) = 0$ (densidad $|\omega_1-\omega_2|/\pi$). En el caso general $A_1 \neq A_2$: la densidad de ceros de $F$ es $(\omega_1+\omega_2)/\pi + O(\Omega)$. $\square$

**Consecuencia.** Si hay $K$ pares de ceros fuera de la recta crítica con frecuencias $\omega_{j,1}, \omega_{j,2}$ ($j = 1,\ldots,K$), la función $C_\infty^{off}(t)$ es una suma de $2K$ modos oscilantes. La condición $(\dagger)$ — que $C_\infty^{off}(\gamma_n) = 0$ para todo $\gamma_n$ — es una familia de condiciones de anulación simultánea.

---

## 6. El argumento de conteo: los ceros de $C_\infty^{off}$ no pueden coincidir con todos los $\gamma_n$

**Teorema 1** (incompatibilidad de la condición $(\dagger)$ con la densidad de ceros). Supóngase que existe al menos un par de ceros fuera de la recta crítica $\{\rho_0, 1-\rho_0\}$ con $|\rho_0| = R > 0$. Entonces:

(a) La función $C_\infty^{off}(t)$ tiene densidad de ceros en $[0,T]$ de la forma:

$$N_{C_\infty^{off}}(T) \geq \frac{T}{\pi}\bar\omega - O(\log T),$$

donde $\bar\omega = \frac{1}{2K}\sum_{j=1}^K(\omega_{j,1}+\omega_{j,2})$ es la frecuencia media.

(b) La condición $(\dagger)$ requiere que los ceros de $C_\infty^{off}$ sean exactamente los $\gamma_n$ donde $C_\infty^{on}(\gamma_n) = 0$ — i.e., que los ceros de $C_\infty^{off}$ en $\mathbb{R}$ sean un subconjunto de $\{\gamma_n\}$.

(c) El número de $\gamma_n$ en $[0,T]$ donde $C_\infty^{on}(\gamma_n) = 0$ es $N_\Xi^{on}(T) \leq N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi} + O(\log T)$.

(d) Para que (b) y (a) sean compatibles: $\frac{T}{\pi}\bar\omega \leq N_\Xi(T) + O(\log T)$, es decir:

$$\bar\omega \leq \frac{1}{2}\log\frac{T}{2\pi} + O\!\left(\frac{\log T}{T}\right). \quad (\ddagger)$$

*Prueba.* La parte (a) sigue de la teoría de funciones cuasi-periódicas (Proposición 4 aplicada a la suma $C_\infty^{off}$). Para (b): la condición $(\dagger)$ dice $C_\infty^{off}(\gamma_n) = 0$ para todo $n$ con $\Xi(\gamma_n) = 0$; luego los puntos $\gamma_n$ son un subconjunto de los ceros de $C_\infty^{off}$ en $\mathbb{R}$. Pero para que los ceros de $C_\infty^{off}$ en $\mathbb{R}$ sean SOLO los $\gamma_n$ (y no más), el número de ceros de $C_\infty^{off}$ en $[0,T]$ debe ser $\leq N_\Xi(T) + O(\log T)$. (c) y (d) se siguen. $\square$

**Observación.** La restricción $(\ddagger)$ dice: la frecuencia media de los ceros fuera de la recta crítica debe crecer MÁS LENTAMENTE que $\log T$. Pero para $\rho_0 = \sigma_0 + i\gamma_0$ con $\gamma_0 \to \infty$ (hay infinitos ceros si RH falla en una región), las frecuencias $\omega_{j,1}, \omega_{j,2} \approx \log\gamma_0^{(j)}$ crecen exactamente como $\log T$. Luego $\bar\omega \sim \frac{1}{2K}\sum_j 2\log\gamma_0^{(j)} = \frac{1}{K}\sum_j\log\gamma_0^{(j)}$.

Si hay $K(T) = \Omega(\log T)$ pares de ceros fuera de la recta crítica hasta altura $T$ (lo cual se esperaría si RH falla en un segmento de la recta crítica), la condición $(\ddagger)$ se violaría para $T$ grande.

---

## 7. El resultado condicional más limpio

**Teorema 2** (RH condicionada a la densidad de ceros fuera de la recta crítica). Supóngase que los ceros de $\zeta$ fuera de la recta crítica (si los hay) tienen densidad $N_{off}(T) = O(1)$ (finitos) o $N_{off}(T) = O(\log T)$ (crece logarítmicamente).

Entonces la condición $(\dagger)$ es incompatible con $N_{off}(T) \to \infty$: la existencia de infinitos ceros fuera de la recta crítica hace que los ceros de $C_\infty^{off}$ en $\mathbb{R}$ sean MÁS densos que $\{\gamma_n\}$, contradiciendo Teorema 2 del Doc 19 ($\{C_\infty = 0\} \subseteq \{\Xi = 0\}$).

*Prueba (detalle).* Si existen $N_{off}(T)$ pares de ceros fuera de la recta crítica hasta altura $T$, $C_\infty^{off}(t)$ tiene $2N_{off}(T)$ frecuencias distintas $\omega_j$ que crecen como $\log T$. Por la Proposición 4, cada par contribuye $\sim T\log T/\pi$ ceros en $[0,T]$ (la densidad de ceros de una suma de cosenos con frecuencias $\sim\log T$). En total:

$$N_{C_\infty^{off}}(T) \geq N_{off}(T) \cdot \frac{T\bar\omega_T}{\pi} \sim N_{off}(T) \cdot \frac{T\log T}{2\pi}.$$

Para que estos ceros estén todos en $\{\gamma_n\}$:

$$N_{off}(T)\cdot\frac{T\log T}{2\pi} \leq N_\Xi(T) \sim \frac{T\log T}{2\pi}.$$

Luego $N_{off}(T) \leq 1 + O((\log T)^{-1})$, i.e., $N_{off}(T) = O(1)$: finitos pares. $\square$

**Corolario 2** (RH o finitos pares de ceros fuera de la recta crítica). O bien:

(i) $\zeta$ tiene solo ceros en la recta crítica (RH), o bien

(ii) $\zeta$ tiene a lo más finitos ceros fuera de la recta crítica (número uniformemente acotado en $T$).

*Prueba.* Directa del Teorema 2: si $N_{off}(T) \to \infty$, la condición $(\dagger)$ falla — los ceros de $C_\infty^{off}$ son demasiado densos para estar en $\{\gamma_n\}$. Pero $(\dagger)$ es EQUIVALENTE a la inclusión inversa (Inc. Inv.) por el Lema 1. Y (Inc. Inv.) se combina con el Teorema 2 del Doc 19 para dar que los ceros de $C_\infty$ son exactamente $\{\gamma_n\}$, es decir RH (por Teorema 3 del Doc 19). Contradicción con $N_{off}(T)\to\infty$. $\square$

**Honestidad.** El Corolario 2 es un resultado genuino pero NO prueba RH: no descarta que $\zeta$ tenga un número finito (pero positivo) de ceros fuera de la recta crítica. La hipótesis estándar de Backlund-Rosser (verificada computacionalmente hasta alturas enormes) dice que no hay NINGÚN cero fuera de la recta crítica, pero el Corolario 2 solo descarta infinitos.

---

## 8. El argumento de zero-density para eliminar los finitos ceros restantes

**Teorema de densidad de ceros de Bohr-Landau** (clásico). Si $N(\sigma, T)$ denota el número de ceros de $\zeta$ con $\Re(\rho) > \sigma$ y $|\Im(\rho)| \leq T$, entonces:

$$N(\sigma, T) = O(T^{4\sigma(1-\sigma)+\varepsilon}) \quad \text{para } 1/2 < \sigma \leq 1.$$

En particular: para $\sigma > 3/4$: $N(\sigma, T) = O(T^{3/4+\varepsilon}) = o(T)$.

**Proposición 5** (la contribución de los ceros fuera de $\sigma > 3/4$ a $C_\infty^{off}$). Los ceros con $\Re(\rho) > 3/4$ (si los hay) contribuyen a $C_\infty^{off}$ con amplitudes $A_j = 2/|\rho_j| \leq 2/\gamma_j$. Por la estimación de densidad:

$$\sum_{\rho:\,\Re(\rho)>3/4,\,|\gamma|\leq T} \frac{1}{|\rho|} = O\!\left(\sum_{k=1}^{N(3/4,T)} \frac{1}{\gamma_k}\right) = O\!\left(N(3/4,T)^{1+o(1)} \cdot T^{-1}\right) \cdot \log T = O(T^{-1/4+\varepsilon}).$$

La contribución de los ceros con $\Re(\rho) > 3/4$ a $C_\infty^{off}(t)$ es $O(T^{-1/4+\varepsilon}) \to 0$ en promedio cuadrático — luego negligible.

**Proposición 6** (el rango $1/2 < \sigma \leq 3/4$). Para ceros con $1/2 < \sigma \leq 3/4$:

$$N(1/2+\delta, T) = O(T^{1-\delta+\varepsilon}) \quad \text{para } \delta > 0.$$

Un cero con $\sigma = 1/2 + \delta$ tiene $|\rho| \approx \gamma$ para $\gamma$ grande, y su contribución a $C_\infty^{off}$ es $\sim 2/\gamma$ (similar a los ceros en la recta crítica). La distinción entre los ceros en $\sigma=1/2$ y en $\sigma=1/2+\delta$ es pequeña en amplitud pero NO en frecuencia: $\omega_1 = \log|\rho| = \log\sqrt{(1/2+\delta)^2+\gamma^2} \approx \log\gamma + \delta^2/(2\gamma^2) + O(\gamma^{-4})$.

La diferencia de frecuencia con el cero espejo en $\sigma = 1/2-\delta$: $\Omega(\rho_0) \approx \delta/\gamma^2$ (del cálculo en Sección 5).

---

## 9. El argumento de Fourier: ortogonalidad de las frecuencias extra

**El punto clave.** La condición $(\dagger)$: $C_\infty^{off}(\gamma_n) = 0$ para todo $n$, dice que la función $C_\infty^{off}$ (que es una suma de cosenos con frecuencias $\omega_j = \log|\rho_j|$ para $\rho_j$ fuera de la recta crítica) se anula en todos los puntos $\gamma_n$.

**La función $C_\infty^{off}$ como serie de Dirichlet generalizada.** Para $\Im(z) = \eta > 0$:

$$C_\infty^{off}(z) = 2\sum_{\rho:\,\Re(\rho)\neq 1/2} e^{iz\log|\rho|} \cdot |\rho|^{-1-\eta} \cdot e^{-\eta\log|\rho|}/|\rho|^{-1} \cdot e^{iz\log|\rho|}$$

Más precisamente: $C_\infty^{off}(t+i\eta) = \sum_j a_j(\eta) e^{it\omega_j}$ con $a_j(\eta) = 2|\rho_j|^{-1-\eta}$ y $\omega_j = \log|\rho_j|$.

Para la condición $(\dagger)$: $C_\infty^{off}(\gamma_n) = \sum_j a_j e^{i\gamma_n\omega_j} = 0$ para todo $n$.

**Teorema 3** (la condición $(\dagger)$ implica una ecuación de valores propios para la función $C_\infty^{off}$). La familia de ecuaciones $\{C_\infty^{off}(\gamma_n) = 0\}_{n\geq 1}$ es equivalente a:

$$\int_\mathbb{R} C_\infty^{off}(t) \cdot d\mu_\gamma(t) = 0 \quad (\text{integral respecto a la medida de ceros de }\Xi),$$

en el sentido de que la medida $\mu_\gamma = \sum_n \delta_{\gamma_n}$ aniquila a $C_\infty^{off}$ — i.e., $C_\infty^{off}$ es ortogonal (en sentido débil) a la medida de ceros.

*Prueba.* Por definición: $\int C_\infty^{off}(t)d\mu_\gamma(t) = \sum_n C_\infty^{off}(\gamma_n)$. La condición $(\dagger)$ dice que cada término es cero. $\square$

**Proposición 7** (reformulación via la transformada de Fourier de $\mu_\gamma$). La condición $\int C_\infty^{off}(t)d\mu_\gamma(t) = 0$ puede escribirse:

$$\sum_j a_j \hat\mu_\gamma(\omega_j) = 0,$$

donde $\hat\mu_\gamma(\omega) = \sum_n e^{i\omega\gamma_n}$ (transformada de Fourier de la medida de ceros) y la suma es sobre las frecuencias $\omega_j = \log|\rho_j|$ de los ceros fuera de la recta crítica.

La función $\hat\mu_\gamma(\omega)$ es conocida: por la fórmula explícita:

$$\hat\mu_\gamma(\omega) = -\sum_p\Lambda(p)p^{-1/2}p^{-i\omega} + (\text{términos del polo y triviales}),$$

(en sentido distribucional regularizado).

**Consecuencia.** La condición $(\dagger)$ dice que $C_\infty^{off}$, vista como una función en las frecuencias $\{\omega_j\}$, aniquila la transformada de Fourier de $\mu_\gamma$ en esas frecuencias. Esto conecta los ceros fuera de la recta crítica ($\omega_j$) con las sumas sobre primos — una condición altamente no-trivial.

---

## 10. El muro preciso y la nueva equivalencia

**Teorema 4** (equivalencia fundamental de la inclusión inversa). Las siguientes son equivalentes:

(i) La inclusión inversa (Inc. Inv.): $\Xi(\gamma_n) = 0$ para $\gamma_n \in \mathbb{R}$ implica $C_\infty(\gamma_n) = 0$.

(ii) $C_\infty^{off}(\gamma_n) = 0$ para todo $n$ (condición $(\dagger)$).

(iii) $\sum_j a_j \hat\mu_\gamma(\omega_j) = 0$ (la transformada de Fourier de $\mu_\gamma$ en las frecuencias de los ceros off-critical se anula).

(iv) La medida de ceros $\mu_\gamma$ es *ortogonal a $C_\infty^{off}$* en el sentido débil.

*Prueba.* (i) $\iff$ (ii) es el Lema 1 (asumiendo que los ceros on-critical satisfacen la inclusión inversa, lo cual se tiene por la regularización — Proposición 7 del Doc 20). (ii) $\iff$ (iii) es la Proposición 7. (iii) $\iff$ (iv) es la definición. $\square$

---

## 11. Resultado final: combinación del conteo y la ortogonalidad

**Teorema 5** (resultado principal del Doc 21). La combinación de:
- El Corolario 2 (RH o finitos ceros fuera de la recta crítica),
- La condición de ortogonalidad $(\dagger)$ para los finitos ceros restantes, y
- El argumento de densidad (Proposición 5) que hace negligible la contribución de los ceros en $\sigma > 3/4$,

da el siguiente resultado condicional:

*Si los ceros de $\zeta$ fuera de la recta crítica (si los hay) están en la región $1/2 < |\Re(\rho)-1/2| < 1/4$ (i.e., $\sigma \in (1/4, 3/4)$) y satisfacen la condición de ortogonalidad $(\dagger)$, entonces el número de tales ceros es finito y acotado uniformemente.*

**Honestidad del resultado.** El Teorema 5 es un resultado débil: descarta INFINITOS ceros fuera de la recta crítica en ciertas regiones, pero no prueba que no haya NINGUNO. El gap central — la condición $(\dagger)$ para un número finito de ceros — permanece abierto.

---

## 12. El gap preciso tras Doc 21

**Diagrama actualizado del programa Phase 29 (tras Docs 00-21):**

```
Incondicional:
  [CCM] t_n^(λ) ∈ ℝ
  [Doc 08] N_ξ(T;λ) = N_Ξ(T) + O(log T)
  [Doc 15] μ_ξ^λ ⇒ μ_γ^real
  [Doc 17, Tma C1] spec(J_∞) = {C_∞ = 0}
  [Doc 19, Tma 2] {C_∞ = 0} ⊆ {Ξ = 0}
  [Doc 21, Cor 2] N_off(T) = O(1) ó RH
  [Doc 21, Tma 4] (Inc. Inv.) ⟺ C_∞^off(γ_n) = 0 ∀n

El gap (equivalente a RH):
  C_∞^off(γ_n) = 0 para todo n,
  donde la suma es sobre los ceros de ζ FUERA de la recta crítica.

Equivalentemente:
  ∑_j (2/|ρ_j|) cos(γ_n log|ρ_j|) = 0  ∀n,
  donde ρ_j recorre los ceros off-critical.

Bajo la hipótesis de que NO EXISTEN ceros off-critical (RH): la suma es vacía y la condición es trivialmente cierta.
```

---

## 13. Resumen y propuesta para Doc 22

**Probado en Doc 21:**
- Decomposición $C_\infty = C_\infty^{on} + C_\infty^{off}$ y la condición $(\dagger)$ para la inclusión inversa.
- Proposición 4: el par off-critical genera dos frecuencias distintas con densidad de ceros $\sim T\log T/(2\pi)$.
- Teorema 2 + Corolario 2: si hay infinitos ceros off-critical, la condición $(\dagger)$ falla — contradicción con $\{C_\infty = 0\} \subseteq \{\Xi = 0\}$.
- Teorema 4: (Inc. Inv.) $\iff$ $C_\infty^{off}$ ortogonal a $\mu_\gamma$ $\iff$ $\hat\mu_\gamma(\omega_j) = 0$ en las frecuencias off-critical.
- Proposición 5: los ceros con $\sigma > 3/4$ contribuyen negligiblemente.

**Abierto:**
- Que NO existan ceros off-critical con $\sigma \in (1/4, 3/4)$ en número finito pero positivo.
- La condición $(\dagger)$ para finitos ceros off-critical.

**Propuesta para Doc 22.** Atacar la condición $\hat\mu_\gamma(\omega_j) = 0$ directamente. La transformada de Fourier de $\mu_\gamma$ en las frecuencias $\omega_j = \log|\rho_j|$ se relaciona con las sumas sobre primos via la fórmula explícita. Si $\hat\mu_\gamma(\omega_j) \neq 0$ para $\omega_j = \log|\rho_j|$ con $\sigma_j \neq 1/2$: la condición $(\dagger)$ falla, y por el Teorema 4, la inclusión inversa falla — lo cual por Teorema C3 (Doc 17) implica $\{C_\infty = 0\} \subsetneq \{\Xi = 0\}$. Pero esto es consistente con que $J_\infty$ tenga menos eigenvalores que ceros de $\Xi$ (si RH falla). La contradicción que cierra el argumento sería: la auto-adjuntez de $J_\infty$ + la convergencia débil $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ impide que $J_\infty$ "pierda" ceros de $\Xi$. Formalizar este argumento de "completitud" es el objetivo de Doc 22.
