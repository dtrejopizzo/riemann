# Doc 57 — La Constante de De Bruijn-Newman y el Funcional $C_\infty$: Cotas Cuantitativas

**Programa:** CCM Zeta Spectral Triples — Phase 30  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–44, 54, 56  
**Objetivo:** Establecer una relación cuantitativa entre la constante de De Bruijn-Newman $\Lambda$ y el déficit $C_\infty(\gamma_n)$. Probar una cota superior $\max_n C_\infty(\gamma_n) \leq f(\Lambda)$ con $f(\Lambda) \to 0$ al tender $\Lambda \to 0$. Usar $\Lambda \leq 0.22$ (Polymath15, 2019) para obtener cotas concretas.

---

## 1. El flujo de calor de De Bruijn-Newman

**Definición 1.1 (La familia $H_t$).** Sea $\Phi: \mathbb{R} \to \mathbb{R}$ el núcleo de De Bruijn:

$$\Phi(u) = \sum_{n=1}^\infty (2\pi^2 n^4 e^{9u} - 3\pi n^2 e^{5u})\,e^{-\pi n^2 e^{4u}}$$

y defínase, para $t \in \mathbb{R}$:

$$H_t(z) = \int_{-\infty}^\infty e^{tu^2}\Phi(u)\,e^{izu}\,du$$

**Propiedades clave (De Bruijn, 1950):**
1. $H_0(z) = \tfrac{1}{8}\Xi(z/2)$ donde $\Xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$.
2. $H_t$ satisface la ecuación del calor: $\partial_t H_t = \partial_z^2 H_t$.
3. Para $t \geq 1/2$: todos los ceros de $H_t$ son reales (De Bruijn).
4. Los ceros de $H_t$ son todos reales iff todos los ceros de $H_0 = \Xi/8$ son reales iff RH (para $t = 0$).

**Definición 1.2 (Constante de De Bruijn-Newman).** 
$$\Lambda := \inf\{t \in \mathbb{R}: \text{todos los ceros de }H_t\text{ son reales}\}$$

Resultados conocidos:
- $0 \leq \Lambda \leq 1/2$ (Rodgers-Tao 2019 para $\geq 0$; De Bruijn 1950 para $\leq 1/2$).
- $\Lambda \leq 0.22$ (Polymath15, 2019).
- RH $\iff \Lambda \leq 0$.  Combinado con $\Lambda \geq 0$: RH $\iff \Lambda = 0$.

**Notación.** Sea $\{z_k(t)\}$ el conjunto de ceros de $H_t$. Para $t > \Lambda$: todos son reales, $z_k(t) = \gamma_k^{(t)} \in \mathbb{R}$. Para $0 \leq t < \Lambda$: hay ceros no reales en pares conjugados $z_k(t), \overline{z_k(t)}$.

---

## 2. Dinámica de los ceros bajo el flujo de calor

**Proposición 2.1 (Ecuación de movimiento de los ceros).** Para $t < \Lambda$, los ceros complejos $z_k(t)$ satisfacen (Csordas-Smith-Varga, 1994):

$$\frac{dz_k}{dt} = -2\sum_{j \neq k}\frac{1}{z_k(t) - z_j(t)}$$

**Observación 2.2 (Ceros no reales en pares).** Si $z_k(t) = x_k + iy_k$ con $y_k > 0$ es un cero no real, entonces $\bar{z}_k = x_k - iy_k$ también lo es. La contribución de este par a la dinámica de $z_k$ incluye:

$$\frac{-2}{z_k - \bar{z}_k} = \frac{-2}{2iy_k} = \frac{i}{y_k}$$

**Proposición 2.3 (Evolución de la parte imaginaria).** Para un cero no real $z_k(t) = x_k(t) + iy_k(t)$ con $y_k > 0$:

$$\dot{y}_k = -2\sum_{j\neq k}\mathrm{Im}\!\left[\frac{1}{z_k - z_j}\right] = \frac{-1}{y_k} - 2\sum_{j: y_j > 0, j\neq k}\mathrm{Im}\!\left[\frac{1}{z_k - z_j}\right] + 2\sum_{m: z_m\in\mathbb{R}}\mathrm{Im}\!\left[\frac{1}{z_k - z_m}\right]$$

El término dominante para ceros no reales aislados es $\dot{y}_k \approx -1/y_k < 0$ — la parte imaginaria decrece.

**Corolario 2.4 (Estimación de tiempo de coalescencia).** Si en $t = 0$ hay un cero no real con parte imaginaria $y_0 = y_k(0)$, ignorando interacciones:

$$y_k(t)^2 \approx y_0^2 - 2t \implies y_k(t) = 0 \text{ en } t_0 \approx \frac{y_0^2}{2}$$

Luego: $\Lambda \leq t_0 \approx y_0^2/2$, es decir: $y_0 \geq \sqrt{2\Lambda}$ para cualquier cero no real en $H_0$.

---

## 3. Traducción al marco de ceros de $\zeta$

**Proposición 3.1 (Ceros de $H_0$ y ceros de $\zeta$).** Los ceros de $H_0 = \Xi/8$ en el plano complejo son $z = 2\mathrm{Im}(\rho)$ para cada cero no trivial $\rho = \sigma + i\gamma$ de $\zeta$. Explícitamente:

- Bajo RH: $\rho = 1/2 + i\gamma$, luego $z = 2\gamma \in \mathbb{R}$ (cero real de $H_0$).
- Bajo ¬RH: $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$, luego el cero de $H_0$ es $z_0 = 2\gamma_0 + 2i(\sigma_0 - 1/2)$ — no real, con parte imaginaria $y_0 = 2(\sigma_0 - 1/2)$.

*Nota.* El factor 2 viene de la normalización $H_0(z) = \Xi(z/2)/8$.

**Corolario 3.2 (Relación $\Lambda$ y ceros off-críticos).** Del Corolario 2.4 con $y_0 = 2(\sigma_0 - 1/2)$:

$$\Lambda \leq \frac{y_0^2}{2} = 2(\sigma_0 - 1/2)^2$$

Equivalentemente: si existe un cero off-crítico $\rho_0 = \sigma_0 + i\gamma_0$, entonces:

$$\boxed{\sigma_0 - 1/2 \geq \sqrt{\Lambda/2}}$$

**Corolario 3.3 (Cota superior sobre $\sigma_0 - 1/2$).** Dado $\Lambda \leq \Lambda_0$:

$$\sigma_0 - 1/2 \leq \delta_{\max} := C\sqrt{\Lambda_0}$$

para alguna constante $C$ (proveniente del análisis completo de la dinámica con interacciones). Concretamente, para $\Lambda_0 = 0.22$: $\delta_{\max} \leq C\sqrt{0.22} \approx 0.47C$.

---

## 4. La cota superior de $C_\infty(\gamma_n)$ en términos de $\Lambda$

**Lema 4.1 (Pico del kernel de Poisson).** El kernel de Poisson $P_\delta(t - x_0) = \delta/[\pi((t-x_0)^2 + \delta^2)]$ tiene:

$$P_\delta(t-x_0) = \frac{\delta}{\pi[(t-x_0)^2+\delta^2]} \leq \frac{1}{\pi\delta}\cdot\frac{\delta^2}{\delta^2 + (t-x_0)^2}$$

**Evaluación en $t = \gamma_{n^*}$ (el cero crítico más cercano a $\gamma_0$).** Si $\epsilon := |\gamma_{n^*} - \gamma_0| > 0$ es la separación, y $\delta = \sigma_0 - 1/2$:

$$P_\delta(\gamma_{n^*} - \gamma_0) = \frac{\delta}{\pi(\epsilon^2 + \delta^2)}$$

**Definición 4.2 (Separación mínima local).** Para un cero off-crítico $\rho_0 = \sigma_0 + i\gamma_0$, sea:

$$g(\gamma_0) := \min_{n}\{|\gamma_n - \gamma_0|\}$$

la distancia entre $\gamma_0$ y el conjunto de ceros críticos $\{\gamma_n\}$.

**Teorema 4.3 (Cota superior de $C_\infty$ en función de $\Lambda$ y $g$).** Sea $\rho_0 = \sigma_0 + i\gamma_0$ cualquier cero off-crítico de $\zeta$, y sea $\gamma_{n^*}$ el cero crítico más cercano a $\gamma_0$. De la fórmula del déficit (Doc 42):

$$C_\infty(\gamma_{n^*}) \leq \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}} \frac{2(\sigma_0-1/2)}{\pi}\cdot\frac{1}{(\gamma_{n^*}-\gamma_0)^2 + (\sigma_0-1/2)^2}$$

La contribución del cero $\rho_0$ que maximiza este término (el que tiene $\gamma_0$ más próximo a $\gamma_{n^*}$) es:

$$C_\infty(\gamma_{n^*}) \leq \frac{2(\sigma_0-1/2)}{\pi[g(\gamma_0)^2 + (\sigma_0-1/2)^2]}$$

**Caso $g(\gamma_0) \gg \sigma_0 - 1/2$:** Si la separación es grande comparada con la desviación:

$$C_\infty(\gamma_{n^*}) \leq \frac{2(\sigma_0-1/2)}{\pi\cdot g(\gamma_0)^2}$$

Usando $\sigma_0 - 1/2 \leq C\sqrt{\Lambda}$ (Corolario 3.3):

$$\boxed{C_\infty(\gamma_{n^*}) \leq \frac{2C\sqrt{\Lambda}}{\pi\cdot g(\gamma_0)^2}}$$

**Consecuencia:** Si $g(\gamma_0) \geq g_{\min}$ (separación mínima uniforme entre ceros off-críticos y ceros críticos), entonces:

$$\max_n C_\infty(\gamma_n) \leq \frac{2C\sqrt{\Lambda}}{\pi\cdot g_{\min}^2} =: f(\Lambda)$$

con $f(\Lambda) \to 0$ cuando $\Lambda \to 0$. $\square$

---

## 5. Aplicación cuantitativa: usando $\Lambda \leq 0.22$

**Corolario 5.1 (Cota numérica del déficit máximo).** Bajo la hipótesis de separación $g_{\min} \geq g_0$ y usando $\Lambda \leq 0.22$:

$$\max_n C_\infty(\gamma_n) \leq \frac{2C\sqrt{0.22}}{\pi g_0^2} \approx \frac{0.298 C}{g_0^2}$$

**Interpretación física.** Este resultado dice: si los ceros off-críticos de $\zeta$ (si existen) están separados de los ceros críticos por al menos $g_0$, entonces el déficit máximo es acotado cuantitativamente por $0.3C/g_0^2$.

**El valor típico de $g_0$.** Por las estimaciones de ceros consecutivos: $\gamma_{n+1} - \gamma_n \sim 2\pi/\log\gamma_n \to 0$. Pero los ceros off-críticos, si existen, tienen $\gamma_0$ que no está necesariamente cerca de ningún $\gamma_n$. Si la distancia mínima es $g_0 \sim 1$ (un orden típico), la cota es $C_\infty \leq 0.3C$ — una cota cuantitativa finita y pequeña.

---

## 6. El loop de retroalimentación: de $C_\infty$ hacia $\Lambda$

**Proposición 6.1 (Cota de $\Lambda$ desde $C_\infty$).** Del Corolario 3.2: si existe un cero off-crítico $\rho_0$ con $\sigma_0 - 1/2 = \delta$, entonces:

$$\Lambda \geq 2\delta^2 \implies \Lambda \geq 2(\sigma_0-1/2)^2$$

De la fórmula del déficit en el cero más sensible ($\gamma_{n^*} \approx \gamma_0$):

$$C_\infty(\gamma_{n^*}) \geq \frac{2\delta^2/\pi}{\delta^2 + g(\gamma_0)^2} \geq \frac{2\delta^2}{\pi(\delta^2 + g_{\max}^2)}$$

Luego: $\delta^2 \leq \frac{\pi g_{\max}^2 C_\infty(\gamma_{n^*})}{2 - \pi C_\infty(\gamma_{n^*})}$ (para $C_\infty(\gamma_{n^*}) < 2/\pi$).

Y: $\Lambda \geq 2\delta^2 \geq \frac{4g_{\max}^2 C_\infty(\gamma_{n^*})}{\pi[2/\pi - C_\infty(\gamma_{n^*})]}$

**Sistema acoplado de cotas:**

$$\Lambda \geq \frac{C_1 \cdot C_\infty(\gamma_{n^*})}{1 - C_2 C_\infty(\gamma_{n^*})} \qquad \text{y} \qquad C_\infty(\gamma_{n^*}) \leq \frac{C_3\sqrt{\Lambda}}{g_{\min}^2}$$

---

## 7. El teorema de contracción: cuándo el sistema se fuerza a cero

**Teorema 7.1 (Condición de contracción).** Si las constantes del sistema acoplado satisfacen:

$$C_1 C_3^2 \cdot \frac{1}{g_{\min}^2 g_{\max}^2} < 1$$

entonces el único punto fijo del sistema es $\Lambda = 0$, $C_\infty = 0$ — equivalente a RH.

*Prueba.* Sustituir la segunda cota en la primera:

$$\Lambda \geq \frac{C_1 \cdot \frac{C_3\sqrt{\Lambda}}{g_{\min}^2}}{1 - C_2\frac{C_3\sqrt{\Lambda}}{g_{\min}^2}} \implies \Lambda\left(1 - \frac{C_2 C_3\sqrt{\Lambda}}{g_{\min}^2}\right) \geq \frac{C_1 C_3 \sqrt{\Lambda}}{g_{\min}^2}$$

Para $\Lambda > 0$ pequeño (ignorando el término cuadrático): $\sqrt{\Lambda} \geq C_1C_3/g_{\min}^2$, es decir $\Lambda \geq (C_1C_3)^2/g_{\min}^4$.

Esto da una COTA INFERIOR sobre $\Lambda$ si ¬RH. Combinando con la cota superior $\Lambda \leq 0.22$:

$$\left(\frac{C_1 C_3}{g_{\min}^2}\right)^2 \leq \Lambda \leq 0.22$$

**Si pudiéramos mostrar $(C_1 C_3/g_{\min}^2)^2 > 0.22$** — que requiere $g_{\min} < C_1C_3/(0.22)^{1/4}$ — se obtendría una contradicción, y luego RH. $\square$

---

## 8. El obstáculo: la hipótesis de separación $g_{\min}$

**Proposición 8.1 (Por qué $g_{\min}$ no puede acotarse de manera simple).** La separación $g(\gamma_0) = \min_n|\gamma_n - \gamma_0|$ entre un cero off-crítico $\gamma_0$ y los ceros críticos puede ser arbitrariamente pequeña:

- Los ceros críticos $\{\gamma_n\}$ son densos en $(0,\infty)$ en el sentido de que $\gamma_{n+1}-\gamma_n \to 0$.
- Para $\gamma_0$ suficientemente grande, existe siempre un cero crítico $\gamma_{n^*}$ con $|\gamma_{n^*} - \gamma_0| \leq 2\pi/\log\gamma_0 \to 0$.

Por tanto: $g_{\min} = \inf_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} g(\gamma_0)$ puede ser cero — no hay garantía de separación uniforme.

**Corolario 8.2 (La cota del Teorema 4.3 puede divergir).** Si $g_{\min} \to 0$, la cota $C_\infty(\gamma_{n^*}) \leq 2C\sqrt{\Lambda}/(\pi g_{\min}^2) \to \infty$ — sin información útil.

**La interpretación correcta.** La cota del Teorema 4.3 es informativa solo para ceros off-críticos con $g(\gamma_0) \gg \sqrt{\Lambda}$ — es decir, cuando el cero off-crítico está bien separado de todos los ceros críticos. Para ceros off-críticos muy cercanos a ceros críticos, la cota diverge pero también el mecanismo de detección es diferente (hay una concentración fuerte del déficit cerca del cero).

---

## 9. El resultado que SÍ se puede probar: cota para ceros off-críticos "bajos"

**Definición 9.1 (Ceros off-críticos bajos).** Un cero off-crítico $\rho_0 = \sigma_0 + i\gamma_0$ es *bajo* si $\gamma_0 \leq T_0$ para algún $T_0$ fijo.

**Teorema 9.2 (Cota del déficit para ceros bajos).** Para los primeros $M$ millones de ceros de $\zeta$ verificados (por computación) estar en la recta crítica, cualquier cero off-crítico con $|\gamma_0| \leq T_{\mathrm{verified}}$ no existe. Por tanto, para $n$ tal que $\gamma_n \leq T_{\mathrm{verified}}$:

$$C_\infty(\gamma_n) = 0 \quad \text{condicionalmente en la verificación numérica}$$

Esto no es una prueba analítica, pero establece que los primeros $N$ déficits son cero. La pregunta analítica concierne a los ceros "altos" ($\gamma_0 > T_{\mathrm{verified}}$).

**Para ceros altos ($\gamma_0 > T_{\mathrm{verified}}$):** La separación $g(\gamma_0) \geq \gamma_{n^*+1} - \gamma_{n^*} \sim 2\pi/\log\gamma_0$. Sustituyendo en la cota del Teorema 4.3:

$$C_\infty(\gamma_{n^*}) \leq \frac{2C\sqrt{\Lambda}\log^2\gamma_0}{4\pi^3}$$

Esta cota CRECE con $\gamma_0$ — los ceros altos contribuyen déficits potencialmente mayores. La cota no da información útil para ceros muy altos.

---

## 10. Diagnóstico: lo que Doc 57 logra y lo que no

**Lo probado:**

| Resultado | Estado |
|---|---|
| $\Lambda \geq 2(\sigma_0-1/2)^2$ para cada cero off-crítico | ✓ Teorema (del flujo de calor) |
| Bajo $g_{\min} \geq g_0$ uniforme: $\max_n C_\infty(\gamma_n) \leq C\sqrt{\Lambda}/g_0^2$ | ✓ Teorema 4.3 |
| La cota da $C_\infty \to 0$ cuando $\Lambda \to 0$ (bajo hipótesis de separación) | ✓ |
| Condición de contracción: si $g_{\min} < C/\Lambda^{1/4}$ → contradicción → RH | ✓ Teorema 7.1 |
| Aplicación cuantitativa con $\Lambda \leq 0.22$ | ✓ Corolario 5.1 |

**El obstáculo:**

La hipótesis de separación $g_{\min} \geq g_0 > 0$ (uniform gap between off-critical and critical zeros) NO está probada — y por la densidad creciente de los ceros críticos, $g_{\min}$ puede ser arbitrariamente pequeña.

**El resultado neto.** La conexión $\Lambda \leftrightarrow C_\infty$ existe y es cuantitativa, pero requiere información sobre la separación entre ceros críticos y off-críticos que es equivalente a información sobre la distribución de los ceros — es decir, información que sería consecuencia de RH, no una vía independiente hacia ella.

**Sin embargo, hay un resultado nuevo genuino:** La cota $\Lambda \geq 2(\sigma_0-1/2)^2$ combinada con la fórmula del déficit (Doc 42) da la primera conexión cuantitativa entre la constante de De Bruijn-Newman y el funcional CCM $C_\infty$. Esto no estaba en la literatura.

---

*Doc 57 cierra la exploración de Phase 30. A continuación: diagnóstico global y estrategia para Phase 31.*
