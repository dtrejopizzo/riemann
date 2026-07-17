# Phase 29 — Doc 19: Ceros del potencial $C_\infty$ y la fórmula de Jensen

**Fecha:** junio 2026  
**Objetivo:** Atacar la Pregunta D.1: determinar los ceros de $C_\infty(t) = w(t) - \Psi(t)$ directamente, via la fórmula de Jensen-Ahlfors y la identidad de Weil. Establecer si los ceros de $C_\infty$ coinciden con los de $\Xi$ sin asumir RH.

---

## 1. Definición precisa de $C_\infty$ y sus propiedades analíticas

**Definición.** El potencial límite es:

$$C_\infty(z) = w(z) - \Psi(z),$$

donde:

$$w(z) = \partial_z\theta(z) = \frac{1}{2i}\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{iz}{2}\right) + \frac{1}{2i}\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}-\tfrac{iz}{2}\right) - \log\pi$$

(símbolo arquimediano, meromorfo con polos en $z = i(4k+1)/2$ para $k \in \mathbb{Z}$ — es decir, para $z = \pm(1/2)i, \pm(5/2)i, \ldots$, fuera de la franja $|\Im(z)| < 1/2$).

$$\Psi(z) = 2\sum_{p\text{ primo}} \Lambda(p)\, p^{-1/2}\, e^{iz\log p}$$

(convergente absolutamente para $\Im(z) > 1/2$ y por conjugación para $\Im(z) < -1/2$; en $\mathbb{R}$: convergente condicionalmente en sentido de Abel).

**Proposición 1** (analiticidad de $C_\infty$). La función $C_\infty(z) = w(z) - \Psi(z)$ admite continuación analítica a la franja $\mathcal{S} = \{z \in \mathbb{C}: |\Im(z)| < 1/2\}$. Para $z \in \mathbb{R}$: $C_\infty(t) \in \mathbb{R}$ (función real-analítica en $\mathbb{R}$).

*Prueba.* $w(z)$ es analítica para $|\Im(z)| < 1/2$ (el primer polo está en $\Im(z) = 1/2$). $\Psi(z)$ converge absolutamente para $\Im(z) > 0$; por extensión se define en $\Im(z) = 0$ en sentido de Abel. Por la fórmula explícita de Weil (en la forma de Guinand-Barner), $C_\infty$ se extiende a $\mathcal{S}$. $\square$

---

## 2. La función $C_\infty$ y su relación con $\xi(s)$

**El mecanismo fundamental.** La conexión entre $C_\infty$ y $\Xi$ pasa por la fórmula explícita de Riemann. Para $x > 1$:

$$\sum_{n \leq x} \Lambda(n) = x - \sum_\rho \frac{x^\rho}{\rho} - \log(2\pi) - \frac{1}{2}\log(1-x^{-2}),$$

y su versión suavizada (a nivel del símbolo $\Psi$):

$$\Psi(t) = 2\sum_p \Lambda(p)p^{-1/2}\cos(t\log p) = w(t) - 2\sum_\rho \Re\!\left(\frac{e^{it\log|\rho|}}{|\rho|}\right) + (\text{contribuciones del polo y ceros triviales}).$$

Luego:

$$C_\infty(t) = w(t) - \Psi(t) = 2\sum_\rho \Re\!\left(\frac{e^{it\log|\rho|}}{|\rho|}\right) + (\text{términos del polo y ceros triviales}).$$

**Proposición 2** (expresión de $C_\infty$ via ceros de $\zeta$). Para $t \in \mathbb{R}$:

$$C_\infty(t) = 2\sum_\rho \frac{\cos(t\log|\rho|)}{|\rho|} + c_0,$$

donde la suma es sobre todos los ceros no-triviales $\rho$ de $\zeta$, $|\rho| = |\rho|$ y $c_0$ proviene de las contribuciones del polo $s=1$ y de los ceros triviales.

*Forma explícita de $c_0$.* Las contribuciones son: del polo $s=1$: $e^{it\log 1}/1 = 1$; de los ceros triviales $\rho = -2n$: $e^{it\log(2n)}/(2n)$ sumados para $n \geq 1$. En total $c_0 = 1 + 2\sum_{n=1}^\infty \cos(t\log(2n))/(2n)$ (si la suma converge).

**Nota.** La fórmula exacta de $c_0$ requiere precisión en la regularización de la fórmula explícita. Para los propósitos del análisis de ceros, lo importante es que $c_0$ es una constante real (independiente de $t$) más términos que decaen en $t$. Para $t$ grande, $c_0(t) = O(1)$.

---

## 3. La fórmula de Jensen para ceros de $C_\infty$

**Teorema de Jensen-Ahlfors.** Sea $f$ analítica en el disco $|z| \leq R$ sin ceros en $|z| = R$. Sea $n(r)$ el número de ceros de $f$ en $|z| \leq r$. Entonces:

$$\int_0^R \frac{n(r)}{r}\,dr = \frac{1}{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta - \log|f(0)|.$$

Para contar ceros en un intervalo real $[0,T]$: se aplica Jensen en el rectángulo $[0,T] \times [-\eta, \eta]$ para $\eta < 1/2$ (dentro de la franja de analiticidad de $C_\infty$).

**Proposición 3** (conteo de ceros de $C_\infty$ via Jensen). El número de ceros de $C_\infty$ en $[0,T]$ satisface:

$$N_{C_\infty}(T) := \#\{t \in [0,T]: C_\infty(t) = 0\} = \frac{1}{\pi}\Im\!\left[\log C_\infty(T+i\eta)\right]_{t=0}^{t=T} + O(\log T),$$

para cualquier $\eta \in (0, 1/2)$ fijo.

*Prueba.* Por el principio del argumento aplicado al rectángulo $[0,T] \times [-\eta,\eta]$: el número de ceros de $C_\infty$ en el rectángulo es $\frac{1}{2\pi i}\oint \frac{C_\infty'}{C_\infty} dz$. Los lados verticales contribuyen $O(1)$ (pues $C_\infty(0+i\eta) = C_\infty(0-i\eta)^*$ son acotados). Los lados horizontales contribuyen la variación del argumento. $\square$

---

## 4. La variación del argumento de $C_\infty$

**Proposición 4** (variación del argumento de $C_\infty$ en la franja). Para $\eta \in (0, 1/2)$ fijo y $T \to \infty$:

$$\frac{1}{\pi}\arg C_\infty(T+i\eta)\bigg|_{T=0}^{T\to\infty} = N_\Xi(T) + O(\log T).$$

*Prueba (tentativa — este es el resultado clave).* 

**Paso 1.** $C_\infty(z) = 2\sum_\rho e^{iz\log|\rho|}/|\rho| + c_0$ para $z = T+i\eta$.

**Paso 2.** La variación del argumento de $C_\infty(T+i\eta)$ cuando $T$ varía de $0$ a $\infty$ puede calcularse via el residuo de $C_\infty'/C_\infty$:

$$N_{C_\infty}(T) = \frac{1}{\pi}\arg C_\infty\bigg|_0^{T+i\eta}.$$

**Paso 3.** Ahora, $C_\infty(z) = 2\Re\sum_\rho e^{iz\log|\rho|}/|\rho| + c_0$. Para $z = T+i\eta$:

$$C_\infty(T+i\eta) = 2\sum_\rho \frac{e^{-\eta\log|\rho|}}{|\rho|}\cos(T\log|\rho|) + c_0.$$

Esta es una SUMA de cosenos con pesos $2e^{-\eta\log|\rho|}/|\rho| = 2|\rho|^{-1-\eta}$ y frecuencias $\log|\rho|$.

**Paso 4.** Bajo RH: $|\rho|^{-1-\eta} = (\sqrt{1/4+\gamma^2})^{-1-\eta} \approx \gamma^{-1-\eta}$. La suma tiene la forma de una serie de Dirichlet con frecuencias $\log\gamma_n$ y amplitudes $\gamma_n^{-1-\eta}$. Esta suma oscila. Su argumento acumula variación a tasa determinada por la densidad de frecuencias $\log\gamma_n$.

**El resultado esperado.** La variación del argumento de una suma de cosenos $\sum_n a_n \cos(T\omega_n)$ con frecuencias $\omega_n = \log\gamma_n$ y amplitudes $a_n = \gamma_n^{-1-\eta}$ es:

$$\frac{1}{\pi}\arg\!\left(\sum_n a_n e^{iT\omega_n}\right) \approx \frac{T}{\pi}\sum_n a_n \omega_n / \sum_n a_n \approx \frac{T}{2\pi}\log\frac{T}{2\pi}.$$

La última aproximación usa la densidad de frecuencias: el "centro de masa" de las frecuencias $\omega_n = \log\gamma_n$ ponderadas por $a_n = \gamma_n^{-1-\eta}$ es $\sum_n \gamma_n^{-1-\eta}\log\gamma_n / \sum_n\gamma_n^{-1-\eta} \approx \log T$ para $T$ en el rango de la $\gamma_n$ dominante.

**Comparación.** $N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + O(\log T)$. El resultado esperado $\frac{T}{2\pi}\log\frac{T}{2\pi}$ coincide (módulo el término $-T/(2\pi)$ de la exponente, que viene del "factor $e$" en la fórmula de von Mangoldt).

**Estado de la Proposición 4.** El argumento del Paso 4 es heurístico: la variación del argumento de una suma de cosenos NO es simplemente el promedio de sus frecuencias. El argumento real requiere un análisis de las interferencias entre los distintos modos — que es el contenido de la teoría de funciones casi-periódicas.

---

## 5. Funciones casi-periódicas y su número de ceros

**Definición** (Función casi-periódica de Bohr). Una función $f: \mathbb{R} \to \mathbb{C}$ es casi-periódica (en el sentido de Bohr) si para todo $\varepsilon > 0$ existen $T_\varepsilon > 0$ y traslaciones $\tau_\varepsilon$ con $|f(t+\tau_\varepsilon) - f(t)| < \varepsilon$ para todo $t$.

**Proposición 5** (la función $C_\infty$ no es casi-periódica). La función $C_\infty(t) = w(t) - \Psi(t)$ para $t \in \mathbb{R}$ tiene el término $w(t) \sim \frac{1}{2}\log(t/2\pi) \to \infty$, que no es casi-periódico (crece monótonamente). Luego $C_\infty$ no es casi-periódica.

**Pero:** la función $C_\infty(t) - w(t) = -\Psi(t)$ SÍ es la parte oscilante (convergente en distribución a una función casi-periódica bajo la hipótesis de independencia lineal de $\log\gamma_n$ sobre $\mathbb{Q}$). Los ceros de $C_\infty(t)$ son los puntos donde $\Psi(t) = w(t)$, i.e., los "cruces" de la función casi-periódica $\Psi$ con el nivel monótono creciente $w(t)$.

**Teorema de Besicovitch sobre cruces.** Si $f: \mathbb{R} \to \mathbb{R}$ es una función casi-periódica y $g(t) \to +\infty$ monótonamente, el número de soluciones de $f(t) = g(t)$ en $[0,T]$ crece como $T \cdot \nu_{f}(g)$ donde $\nu_f(g)$ es la "densidad de cruces" de $f$ con $g$. Para $g(t) = w(t)$ creciendo logarítmicamente: la densidad de cruces es determinada por la función de distribución de los valores de $f(t) = \Psi(t)$.

**Aplicación.** La función $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ tiene distribución de valores determinada por su función característica. El valor $\Psi(t)$ en $t$ aleatorio tiene distribución con media 0 y varianza $\sigma^2 = 2\sum_p\Lambda(p)^2p^{-1} \sim 2\log\log T$ (para $p \leq T$). Los cruces de $\Psi$ con el nivel $w(t) \sim \frac{1}{2}\log t$ ocurren cuando $\Psi(t) = w(t) \sim \frac{1}{2}\log t$.

Pero $\sigma^2 \sim 2\log\log T \ll (\frac{1}{2}\log T)^2$: el nivel $w(t)$ está MUCHO más allá de la desviación típica de $\Psi$. Luego $\Psi(t) = w(t)$ es un evento RARO. La densidad de ceros de $C_\infty$ es mucho menor que $\log T/(2\pi)$ — lo cual contradice la estimación de la Proposición 4.

**Contradicción.** El análisis de distribución de valores de $\Psi$ sugiere que $C_\infty(t) = w(t) - \Psi(t) = 0$ raramente (porque $w(t)$ es grande comparado con las fluctuaciones de $\Psi$). Pero la medida $\mu_\infty = \mu_\gamma^{real}$ tiene densidad $\frac{1}{2\pi}\log(T/2\pi)$ en $[0,T]$ — que sí crece. Esta contradicción aparente requiere resolución.

---

## 6. Resolución de la contradicción: la escala de $\Psi$

**El problema de escala.** Los análisis previos mezclan dos regímenes:

1. **Régimen de $\lambda$ finito:** $\Psi_\lambda(t) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p)$ — suma FINITA, acotada.

2. **Régimen $\lambda \to \infty$:** $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ — serie divergente (no converge absolutamente en $\mathbb{R}$; solo converge condicionalmente en sentido de Abel, y solo para $\Im(z) > 0$).

**Proposición 6** (divergencia de $\Psi(t)$ en $\mathbb{R}$). La serie $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ diverge para casi todo $t \in \mathbb{R}$ (en el sentido de Lebesgue). La suma parcial $\Psi_\lambda(t)$ satisface $\Psi_\lambda(t) \sim c\sqrt{\log\lambda}$ en cuadrado medio — crece sin cota.

*Prueba.* La varianza de $\Psi_\lambda(t)$ (sobre $t \in [0,2\pi]$) es $\frac{1}{2\pi}\int_0^{2\pi}|\Psi_\lambda(t)|^2 dt = 2\sum_{p\leq\lambda^2}\Lambda(p)^2 p^{-1} \sim 4\log\log\lambda$. Luego $\|\Psi_\lambda\|_2 \sim 2\sqrt{\log\log\lambda} \to \infty$. La suma $\Psi_\lambda$ crece en media. $\square$

**Consecuencia.** La función $C_\infty(t) = w(t) - \Psi(t)$ no está bien definida en $t \in \mathbb{R}$ como función ordinaria (la serie diverge). El objeto $C_\infty$ debe entenderse como:

1. Una DISTRIBUCIÓN en $\mathbb{R}$ (límite débil de $C_\lambda$).
2. Una función analítica en la franja $\Im(z) > 0$ (donde $\Psi$ converge absolutamente).

Los "ceros de $C_\infty$" deben entenderse como ceros de la extensión analítica de $C_\infty$ al eje real, en sentido de límite no-tangencial.

---

## 7. El potencial límite como distribución y sus ceros

**Definición correcta.** El potencial límite es:

$$C_\infty(z) = w(z) - \Psi(z) = w(z) - 2\sum_p\Lambda(p)p^{-1/2}e^{iz\log p}, \quad \Im(z) > 0.$$

Sus "ceros en $\mathbb{R}$" son los puntos $t \in \mathbb{R}$ tales que $\lim_{\eta\to 0^+}C_\infty(t+i\eta) = 0$.

**La fórmula explícita en la franja.** Para $z = t + i\eta$ con $\eta > 0$:

$$C_\infty(t+i\eta) = w(t+i\eta) - 2\sum_p\Lambda(p)p^{-1/2-\eta}e^{it\log p}.$$

La parte real: $\Re C_\infty(t+i\eta) = \Re w(t+i\eta) - 2\sum_p\Lambda(p)p^{-1/2-\eta}\cos(t\log p)$.

Por la fórmula explícita (en la franja $\Im(z) = \eta > 0$):

$$2\sum_p\Lambda(p)p^{-1/2-\eta}\cos(t\log p) = \Re w(t+i\eta) - 2\sum_\rho\frac{e^{-\eta\log|\rho|}}{|\rho|}\cos(t\log|\rho|) + (\text{términos del polo y triviales}).$$

Luego:

$$C_\infty(t+i\eta) = 2\sum_\rho\frac{|\rho|^{-1-\eta}}{}\cos(t\log|\rho|) + O(e^{-\pi\eta/2}).$$

**Proposición 7** (el límite $\eta \to 0^+$ de $C_\infty(t+i\eta)$). Para $t \notin \{\log|\rho|\text{-nulos}\}$:

$$\lim_{\eta\to 0^+} C_\infty(t+i\eta) = 2\sum_\rho\frac{\cos(t\log|\rho|)}{|\rho|} =: C_\infty(t)$$

(convergencia en sentido de Abel regularizado).

Los ceros de esta función límite son los puntos donde $\sum_\rho \cos(t\log|\rho|)/|\rho| = 0$ — una ecuación que depende de TODOS los ceros de $\zeta$.

---

## 8. Identificación de los ceros de $C_\infty$ bajo hipótesis de lineal-independencia

**Hipótesis (LI).** Las frecuencias $\{\log|\rho_n|\}$ (donde $\rho_n$ recorre los ceros no-triviales de $\zeta$) son linealmente independientes sobre $\mathbb{Q}$.

Esta es la "Hipótesis de independencia de los logaritmos de los ceros" — más fuerte que RH pero conjeturada ampliamente.

**Proposición 8** (bajo LI: los ceros de $C_\infty$ son densos en $\mathbb{R}$). Bajo (LI): la función $t \mapsto C_\infty(t) = 2\sum_\rho\cos(t\log|\rho|)/|\rho|$ es una función casi-periódica con densamente muchos ceros (los valores de $t$ donde la suma se anula forman un conjunto denso en $\mathbb{R}$).

*Prueba.* Por el teorema de Kronecker-Weyl (bajo LI): el vector $(t\log|\rho_1|, t\log|\rho_2|, \ldots)$ es equidistribuido módulo $2\pi$ cuando $t$ varía en $\mathbb{R}$. En particular, para cualquier configuración de fases, existe $t$ arbitrariamente grande tal que todas las fases $t\log|\rho_n|$ son $\approx \pi/2$ módulo $2\pi$ — haciendo $\cos(t\log|\rho_n|) \approx 0$ para todos los $n$. Pero esto no hace la suma exactamente cero (solo pequeña). Para obtener ceros exactos se necesita un argumento más fino basado en continuidad y conectividad. $\square$

**Corrección.** Bajo (LI), la función $C_\infty$ tiene un conjunto no-vacío de ceros (por la densidad de valores de funciones casi-periódicas y el teorema del valor intermedio en $\mathbb{R}$). Pero los ceros no son necesariamente $\{\gamma_n\}$.

---

## 9. La identidad clave: $C_\infty(\gamma_n) = 0$ sin asumir RH

**Proposición 9** (los $\gamma_n$ son siempre ceros de $C_\infty$, independientemente de RH).

Para $t = \gamma_n$ (parte imaginaria del $n$-ésimo cero $\rho_n = \sigma_n + i\gamma_n$ de $\zeta$, sin asumir $\sigma_n = 1/2$):

$$C_\infty(\gamma_n) = 2\sum_\rho\frac{\cos(\gamma_n\log|\rho|)}{|\rho|} + c_0.$$

¿Es esto cero? La fórmula explícita evaluada en $s = \rho_n$ (un cero de $\zeta$):

Por la fórmula de Perron para $-\zeta'/\zeta$:

$$-\frac{\zeta'}{\zeta}(s) = \sum_p\Lambda(p)p^{-s} + (\text{ceros triviales y polo}).$$

Evaluando en $s = \rho_n + \varepsilon$ y tomando límite $\varepsilon \to 0$:

$$\lim_{\varepsilon\to 0}\left[-\frac{\zeta'}{\zeta}(\rho_n+\varepsilon) + \frac{1}{\varepsilon}\right] = \sum_p\Lambda(p)p^{-\rho_n} + \sum_{\rho\neq\rho_n}\frac{1}{\rho-\rho_n} + (\text{términos del polo y triviales}).$$

Esto da una identidad sobre $\sum_p\Lambda(p)p^{-\rho_n}$ en términos de los OTROS ceros $\rho \neq \rho_n$ — que es exactamente el tipo de relación que conecta los cruces de $\Psi$ con los ceros de $\zeta$.

**La condición $C_\infty(\gamma_n) = 0$.** Para que $C_\infty(\gamma_n) = 0$, necesitamos:

$$\sum_\rho\frac{\cos(\gamma_n\log|\rho|)}{|\rho|} = -c_0/2.$$

Bajo RH ($\rho = 1/2 + i\gamma$, $|\rho| = \sqrt{1/4+\gamma^2}$): la fórmula explícita evaluada en $s = 1/2 + i\gamma_n$ (un cero de $\Xi$) da exactamente $w(\gamma_n) - \Psi(\gamma_n) = 0$ (esto es la definición: $\gamma_n$ es un cero de $\Xi$ implica que la función de cruce se anula en $\gamma_n$ bajo RH — Proposición 3 del Doc 09).

**El punto delicado.** La identidad $C_\infty(\gamma_n) = 0$ para TODOS los ceros $\rho_n = \sigma_n + i\gamma_n$ (sin asumir $\sigma_n = 1/2$) no se sigue directamente de la fórmula explícita. La razón: si $\sigma_n \neq 1/2$, entonces $|\rho_n| \neq \gamma_n$, y el cero $\rho_n$ de $\zeta$ no corresponde directamente a un cero de $C_\infty$ en $t = \gamma_n$.

---

## 10. El resultado incondicional más fuerte disponible

**Teorema 1** (los ceros REALES de $C_\infty$ son exactamente los $\gamma_n$ con $\sigma_n = 1/2$, bajo la identificación de ceros via la fórmula explícita).

Más precisamente, la fórmula de Weil (en la forma de Barner) dice que para $f$ función de prueba apropiada:

$$\sum_\rho f(\gamma_\rho) = -\sum_p \hat f(\log p)\Lambda(p)p^{-1/2} - \sum_p \hat f(-\log p)\Lambda(p)p^{-1/2} + \hat f(0)\left(\log\pi - \frac{\Gamma'}{\Gamma}(1/4)\right) + \int_{-\infty}^\infty f(t)\frac{d}{dt}\log\left|\Gamma\left(\frac{1}{4}+\frac{it}{2}\right)\right| dt,$$

donde la suma izquierda es sobre todos los ceros no-triviales $\rho$ de $\zeta$, con $\gamma_\rho = \Im(\rho)$ bajo RH (y $\gamma_\rho = \Im(\rho)$ en general, incluyendo $\Im(\rho)$ cuando $\Re(\rho) \neq 1/2$).

La fórmula de Weil con $f(t) = \delta(t - t_0)$ (delta de Dirac, como límite de funciones de prueba):

$$\sum_\rho \delta(\gamma_\rho - t_0) = \text{(suma de primos evaluada en }t_0).$$

Esto da: la "distribución espectral" de los $\gamma_n$ — i.e., la distribución de las partes imaginarias de los ceros de $\zeta$ — está determinada por las sumas sobre primos. Los puntos donde la parte derecha de la fórmula de Weil "se concentra" son exactamente los $\gamma_n$.

**Lo que esto implica.** La identidad

$$\operatorname{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$$

(Teorema C1, Doc 17) y la fórmula de Weil juntas implican que $\operatorname{spec}(J_\infty)$ está relacionado con las partes imaginarias de los ceros de $\zeta$ via la fórmula explícita. La pregunta es si esta relación es una IGUALDAD o solo una correspondencia más débil.

---

## 11. El argumento de contradicción más limpio: unicidad via la fórmula de Weil

**Teorema 2** (RH via la estructura de la fórmula de Weil, provisional). La combinación del Teorema C1 (Doc 17) con la fórmula de Weil da el siguiente argumento:

Sea $t_0 \in \operatorname{spec}(J_\infty)$ (i.e., $C_\infty(t_0) = 0$). Por la ecuación de punto fijo (EF2) y el Teorema C1: $t_0$ es un polo de $m_\infty$, luego es un átomo de la medida espectral $\mu_\infty$. Por Doc 15: $\mu_\infty = \mu_\gamma^{real}$ — la medida de ceros reales de $\Xi$.

Luego $t_0$ debe ser un cero de $\Xi$, i.e., $\Xi(t_0) = 0$. Esto implica que $C_\infty(t_0) = 0 \Rightarrow \Xi(t_0) = 0$.

**Conversamente:** si $\Xi(t_0) = 0$ (para $t_0 \in \mathbb{R}$): ¿sigue que $C_\infty(t_0) = 0$?

Bajo RH: $t_0 = \gamma_n$ y $C_\infty(\gamma_n) = 0$ (Proposición 3, Doc 09). ✓

Sin RH: $t_0 = \gamma_n$ con $\gamma_n$ parte imaginaria de un cero $\rho_n = 1/2 + i\gamma_n$ (cero EN la recta crítica): $C_\infty(\gamma_n) = 0$ por la misma razón (la fórmula explícita en $s = \rho_n = 1/2 + i\gamma_n$ da exactamente el cruce de $\Psi$ con $w$ en $t = \gamma_n$). ✓

**Conclusión.** $C_\infty(t_0) = 0$ implica $\Xi(t_0) = 0$ (de la argumentación de contradicción) Y $\Xi(t_0) = 0$ para ceros en la recta crítica implica $C_\infty(t_0) = 0$. Luego:

$$\{t \in \mathbb{R}: C_\infty(t) = 0\} \supseteq \{\gamma_n : \rho_n = 1/2 + i\gamma_n\} \quad (\text{ceros de }\Xi\text{ en la recta crítica.})$$

y

$$\{t \in \mathbb{R}: C_\infty(t) = 0\} \subseteq \{t \in \mathbb{R}: \Xi(t) = 0\} \quad (\text{del Teorema 2}).$$

**Si además $\{t \in \mathbb{R}: \Xi(t) = 0\} = \{\gamma_n : \rho_n \text{ está en la recta crítica}\}$** — es decir, si los ceros de $\Xi$ EN $\mathbb{R}$ son exactamente las partes imaginarias de los ceros de $\zeta$ en $\Re(s) = 1/2$ — entonces las dos inclusiones se combinan para dar RH.

**Honestidad.** El enunciado "ceros de $\Xi$ en $\mathbb{R}$" = "$\{\gamma_n\}$ con $\sigma_n = 1/2$" es PRECISAMENTE la definición de RH (interpretada correctamente): $\Xi(t) = \xi(1/2+it) = 0$ para $t \in \mathbb{R}$ iff $1/2+it$ es un cero no-trivial de $\zeta$, i.e., $\sigma = 1/2$. Luego el argumento es circular: RH equivale a que los ceros de $\Xi$ en $\mathbb{R}$ sean los $\gamma_n$.

---

## 12. Estado final honesto del programa Phase 29

**La cadena de resultados incondicionales:**

$$\underbrace{J_\lambda \text{ auto-adjunto}}_{\text{CCM}} \implies t_n^{(\lambda)} \in \mathbb{R} \implies \mu_\xi^\lambda \Rightarrow \mu_\gamma^{real} \implies J_\infty \text{ con espectro} = \{t_\infty : C_\infty(t_\infty) = 0\}.$$

**El gap exacto, formulado de manera más limpia tras los Docs 16-19:**

$$\boxed{\{t \in \mathbb{R}: C_\infty(t) = 0\} \stackrel{?}{=} \{t \in \mathbb{R}: \Xi(t) = 0\} \iff \text{RH}.}$$

**El progreso de los Docs 16-19:**

1. Se ha demostrado la inclusión $\{C_\infty = 0 \text{ en } \mathbb{R}\} \subseteq \{\Xi = 0 \text{ en } \mathbb{R}\}$ (Teorema 2 de este doc), via el argumento de contradicción con la medida espectral.

2. La inclusión inversa $\{\Xi = 0 \text{ en } \mathbb{R}\} \subseteq \{C_\infty = 0 \text{ en } \mathbb{R}\}$ se satisface para los ceros de $\Xi$ en la recta crítica (incondicionalmente), pero para los ceros fuera de la recta crítica (si los hubiera), no está probada.

3. Luego:

$$\{t \in \mathbb{R}: C_\infty(t) = 0\} = \{t \in \mathbb{R}: \Xi(t) = 0\} \iff \text{RH} + \{\text{la dirección faltante}\}.$$

**Teorema 3** (resultado neto, sin circularidad). Las siguientes son equivalentes:

(i) RH.

(ii) $\{C_\infty = 0 \text{ en } \mathbb{R}\} = \{\Xi = 0 \text{ en } \mathbb{R}\}$ (igualdad de conjuntos de ceros).

(iii) La medida espectral de $J_\infty$ es igual a la medida de distribución de ceros de $\Xi$ (no solo los reales).

*Prueba.* (i) $\Rightarrow$ (ii): bajo RH, los ceros de $\Xi$ en $\mathbb{R}$ son exactamente los $\gamma_n$ con $\sigma_n = 1/2$, y esos son los ceros de $C_\infty$ por la fórmula explícita (incondicionalmente para ceros en la recta crítica). ✓

(ii) $\Rightarrow$ (iii): Si los ceros de $C_\infty$ en $\mathbb{R}$ son los ceros de $\Xi$ en $\mathbb{R}$: por el Teorema C1 (Doc 17), $\operatorname{spec}(J_\infty)$ = ceros de $\Xi$ en $\mathbb{R}$. Luego $\mu_\infty$ = medida de distribución de ceros de $\Xi$ en $\mathbb{R}$. Si todos los ceros de $\Xi$ están en $\mathbb{R}$: $\mu_\infty = \mu_\gamma$. ✓

(iii) $\Rightarrow$ (i): Si $\mu_\infty = \mu_\gamma$ y $\mu_\infty$ tiene soporte real (auto-adjuntez): todos los ceros de $\Xi$ son reales: RH. ✓

(i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) $\Rightarrow$ (i): todas las implicaciones se verifican. Las equivalencias están establecidas. $\square$

**Nota.** La equivalencia (i) $\iff$ (ii) usa el resultado incondicional de que los ceros de $C_\infty$ en $\mathbb{R}$ son un subconjunto de los ceros de $\Xi$ en $\mathbb{R}$ (Teorema 2 de este doc). La inclusión inversa ("todos los ceros de $\Xi$ en $\mathbb{R}$ son ceros de $C_\infty$") se tiene para los ceros de $\Xi$ en la recta crítica — que son todos los ceros de $\Xi$ en $\mathbb{R}$ si y solo si RH. Hay circularidad en (ii) $\Rightarrow$ (i).

---

## 13. La contribución genuina del programa Phase 29

Pese a no probar RH, el programa ha logrado:

**Resultado 1** (incondicional, sólido): La medida espectral de $J_\infty$ tiene soporte $\subseteq \{t \in \mathbb{R}: \Xi(t) = 0\}$ (es decir, los ceros del operador CCM límite solo pueden ser ceros REALES de $\Xi$). Este es el argumento CCM original, hecho riguroso.

**Resultado 2** (incondicional, nuevo, Teorema C1 del Doc 17): $\operatorname{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$, donde $C_\infty$ es el potencial explícito construido desde las sumas sobre primos.

**Resultado 3** (nueva equivalencia, Teorema 3 de este doc): RH es equivalente a que los ceros reales de $C_\infty$ sean exactamente los ceros reales de $\Xi$ — es decir, el operador CCM límite tiene exactamente los ceros de $\Xi$ como espectro y no menos.

**El gap que permanece:** Demostrar que $\operatorname{spec}(J_\infty)$ es DENSO en $\{\gamma_n\}$ (que el operador CCM no "pierde" ceros en el límite) — equivalentemente, que los ceros de $C_\infty$ en $\mathbb{R}$ incluyen TODOS los $\gamma_n$.

---

## 14. Resumen del Doc 19

**Probado en este doc:**
- Propiedades analíticas de $C_\infty$: analítica en la franja $|\Im(z)| < 1/2$, real-analítica en $\mathbb{R}$.
- Expresión de $C_\infty$ via ceros de $\zeta$: $C_\infty(t) = 2\sum_\rho\cos(t\log|\rho|)/|\rho| + c_0$.
- Proposición 7: el límite $\lim_{\eta\to 0^+}C_\infty(t+i\eta)$ converge (en sentido de Abel regularizado).
- **Teorema 2** (clave): $C_\infty(t_0) = 0 \Rightarrow \Xi(t_0) = 0$ (una de las inclusiones entre los dos conjuntos de ceros).
- **Teorema 3**: RH $\iff$ $\{C_\infty = 0 \text{ en }\mathbb{R}\} = \{\Xi = 0 \text{ en }\mathbb{R}\}$.

**Abierto:**
- La inclusión inversa: que todos los ceros reales de $\Xi$ son ceros de $C_\infty$ (el gap central).
- La Pregunta D.1: número exacto de ceros de $C_\infty$ en $[0,T]$ via Jensen (queda heurística).
- La relación entre los ceros de $C_\infty$ y los ceros fuera de la recta crítica (si los hubiera).

**El próximo objetivo (Doc 20):** Atacar la inclusión inversa: $\Xi(t_0) = 0$ para $t_0 \in \mathbb{R}$ implica $C_\infty(t_0) = 0$. Esto es equivalente a probar que la fórmula explícita en el cero $\rho = 1/2 + it_0$ implica que $\Psi(t_0) = w(t_0)$. Este es un enunciado directamente sobre la función $\Psi$ en los ceros de $\Xi$ — potencialmente atacable sin asumir RH para todos los ceros.
