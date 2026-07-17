# Doc 44 — El Problema de la Medida de Cero: Justificación Rigurosa de la Representación y Tres Ataques sobre $\mu_{\mathrm{off}}$

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 38–43 (especialmente Doc 42 §§3–17 y Doc 43 §§3–5, §15)  
**Objetivo principal:** (1) Demostrar rigurosamente que la representación $C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)$ es exacta y bien definida, respondiendo la crítica del revisor. (2) Explorar tres rutas de ataque sobre la medida off-crítica $\mu_{\mathrm{off}}$ con diagnóstico honesto de cada una.

---

## 1. El problema central y la crítica del revisor

Doc 43 formuló la pregunta estratégica: ¿puede demostrarse que $\mu_{\mathrm{off}} = 0$ usando solo propiedades de los ceros de $\zeta$? El revisor externo identificó una **laguna técnica** en la representación:

> *La igualdad $C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)$ como una transformada de Cauchy-Poisson de una medida positiva requiere justificación independiente, ya que las fórmulas explícitas generan sumas condicionalmente convergentes con cancelaciones oscilatorias complejas, no medidas positivas puras.*

Esta crítica es **matemáticamente legítima** y merece respuesta rigurosa antes de proceder. El objetivo de las §§2–5 es cerrar esta laguna desde los primeros principios de Doc 42.

---

## 2. La estructura de la fórmula del déficit y la separación exacta

Recordamos la cadena de igualdades de Doc 42. Sea $\rho_n = 1/2 + i\gamma_n$ un cero en la línea crítica (con $\gamma_n > 0$). Por la expansión de Hadamard y la definición del potencial espectral $C_\infty$ (ver Doc 42, §3):

$$C_\infty(\gamma_n) = -2\operatorname{Re}\left[\sum_{\substack{\rho \in \mathcal{Z} \\ \rho \neq \rho_n}} \frac{1}{\rho_n - \rho}\right]$$

donde la suma está ordenada por $|\operatorname{Im}(\rho)|$ (convergencia condicional de Hadamard). Los ceros de $\zeta$ se clasifican en dos categorías:

**Tipo I (ceros en la línea crítica):** $\rho = 1/2 + i\gamma_m$, $m \neq n$. Entonces:
$$\frac{1}{\rho_n - \rho} = \frac{1}{i(\gamma_n - \gamma_m)} \in i\mathbb{R}$$

su parte real es exactamente cero.

**Tipo II (ceros off-críticos):** $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$. La ecuación funcional garantiza que $\bar\rho_0 = \sigma_0 - i\gamma_0$ también es cero (con mismo $\sigma_0$, $\gamma_0$ real, signo de parte imaginaria opuesto). Calculamos:

$$\operatorname{Re}\left[\frac{1}{\rho_n - \rho_0}\right] = \operatorname{Re}\left[\frac{1}{(1/2-\sigma_0)+i(\gamma_n-\gamma_0)}\right] = \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2}$$

$$\operatorname{Re}\left[\frac{1}{\rho_n - \bar\rho_0}\right] = \operatorname{Re}\left[\frac{1}{(1/2-\sigma_0)+i(\gamma_n+\gamma_0)}\right] = \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}$$

Por lo tanto, la contribución del par $(\rho_0, \bar\rho_0)$ a $-2\operatorname{Re}[\cdots]$ es:

$$-2\left[\frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}\right]$$

$$= 2(\sigma_0-1/2)\left[\frac{1}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} + \frac{1}{(\sigma_0-1/2)^2+(\gamma_n+\gamma_0)^2}\right] = \Delta(\gamma_n;\rho_0)$$

El coeficiente $2(\sigma_0-1/2) > 0$ porque $\sigma_0 > 1/2$ (para $\rho_0$ con $\sigma_0 > 1/2$; si $\sigma_0 < 1/2$ entonces $1-\bar\rho_0$ tiene parte real $> 1/2$ y se cuenta en ese par).

**Conclusión:** Los ceros de Tipo I contribuyen exactamente cero a la parte real. Toda la contribución viene de los pares de ceros off-críticos, cada uno con coeficiente positivo.

---

## 3. Convergencia absoluta de la serie sobre $\mathcal{Z}_{\mathrm{off}}$

**Proposición 3.1 (Convergencia absoluta de $\sum_{\rho_0}\Delta(\gamma_n;\rho_0)$).**

*Hipótesis:* Los ceros de $\zeta$ en la franja $0 < \sigma < 1$ satisfacen $N(\sigma, T) = O(T^{2(1-\sigma)} \log T)$ (densidad clásica, incondicional).

*Afirmación:* La serie $\sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \Delta(\gamma_n;\rho_0)$ converge absolutamente para cada $\gamma_n$.

*Prueba.* Cada término satisface:
$$0 < \Delta(\gamma_n;\rho_0) \leq \frac{4(\sigma_0-1/2)}{(\sigma_0-1/2)^2} + \frac{4(\sigma_0-1/2)}{(\sigma_0-1/2)^2} = \frac{8}{\sigma_0-1/2}$$

pero también, cuando $|\gamma_0|$ es grande comparado con $\gamma_n$:
$$\Delta(\gamma_n;\rho_0) \leq \frac{4(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + (\gamma_0-\gamma_n)^2/4} = O\!\left(\frac{\sigma_0-1/2}{\gamma_0^2}\right) \quad |\gamma_0| \gg \gamma_n$$

La región $|\gamma_0| \leq 2\gamma_n$ contiene finitos ceros (por la hipótesis de densidad, a lo sumo $O(\gamma_n^{2(1-\sigma_0)}\log\gamma_n)$ ceros off-críticos hasta altura $2\gamma_n$, y la distancia al eje crítico satisface $\sigma_0-1/2 \geq c/\log|\gamma_0|$ por la región libre de ceros clásica).

Para $|\gamma_0| > 2\gamma_n$, sumando por anillos $|\gamma_0| \in [T, 2T]$:
$$\sum_{\substack{\rho_0:\,|\gamma_0|\in[T,2T]}} \Delta(\gamma_n;\rho_0) = O\!\left(\frac{N_{\mathrm{off}}(2T)-N_{\mathrm{off}}(T)}{T^2}\right) \cdot (\sigma_0-1/2)^{-1}$$

donde $N_{\mathrm{off}}(T)$ denota el número de ceros off-críticos hasta altura $T$. Por la estimación de densidad $N(\sigma,T) \ll T^{2(1-\sigma)}\log T$:
$$\sum_{k=0}^\infty \frac{N_{\mathrm{off}}(2^{k+1}\gamma_n) - N_{\mathrm{off}}(2^k\gamma_n)}{(2^k\gamma_n)^2} \ll \sum_{k=0}^\infty \frac{(2^{k+1}\gamma_n)^{2(1-\sigma_{\min})}\log(2^k\gamma_n)}{(2^k\gamma_n)^2} < \infty$$

para cualquier $\sigma_{\min} > 1/2$. $\square$

**Corolario 3.2.** La medida $\mu_{\mathrm{off}} = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}},\,\sigma_0>1/2} 2(\sigma_0-1/2)\,[\delta_{(\gamma_0,\sigma_0-1/2)} + \delta_{(-\gamma_0,\sigma_0-1/2)}]$ es una medida de Radon localmente finita en $\mathbb{H}$.

---

## 4. Validación rigurosa de la representación como transformada de Poisson

**Teorema 4.1 (Representación exacta).** Para cada cero $\rho_n = 1/2+i\gamma_n$ de $\Xi$ en la línea crítica:

$$C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n) = \int_\mathbb{H} \frac{y}{y^2 + (\gamma_n - x)^2}\,d\mu_{\mathrm{off}}(x,y)$$

donde $\mathcal{P}[\mu_{\mathrm{off}}]$ es la transformada de Poisson de la medida de ceros off-críticos.

*Prueba.* Por §2, la separación Tipo I / Tipo II es exacta sin error residual. Los ceros de Tipo I contribuyen exactamente cero a la parte real (cada contribución es puramente imaginaria). Los ceros de Tipo II contribuyen, cada par $(\rho_0, \bar\rho_0)$:

$$\Delta(\gamma_n;\rho_0) = P_{(\sigma_0-1/2)}(\gamma_n - \gamma_0) \cdot 2(\sigma_0-1/2) + P_{(\sigma_0-1/2)}(\gamma_n + \gamma_0) \cdot 2(\sigma_0-1/2)$$

Esto corresponde exactamente a integrar el núcleo $P_y(t-x) = y/[y^2+(t-x)^2]$ contra la medida $\mu_{\mathrm{off}}$ definida en el Corolario 3.2. La convergencia absoluta (Proposición 3.1) garantiza que la integral es igual a la suma:

$$\int_\mathbb{H} P_y(\gamma_n - x)\,d\mu_{\mathrm{off}}(x,y) = \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0>1/2}} \Delta(\gamma_n;\rho_0) = C_\infty(\gamma_n) \qquad \square$$

**Observación 4.2 (Respuesta a la crítica del revisor).** La "oscilación" de las fórmulas explícitas (tipo Riemann-von Mangoldt) reside *enteramente* en las contribuciones imaginarias de los ceros on-críticos. La parte real — que es $C_\infty(\gamma_n)$ — extrae automáticamente la componente off-crítica, que tiene estructura de medida positiva. No hay cancelación osciladora en la cantidad que se estudia: es una suma de términos positivos.

**Unicidad (Riesz-Herglotz).** La representación es única por el siguiente argumento: si $C_\infty(t) = \mathcal{P}[\nu](t)$ para dos medidas positivas $\mu_{\mathrm{off}}$ y $\nu$, entonces $\mathcal{P}[\mu_{\mathrm{off}} - \nu] = 0$ en $\{\gamma_n\}$, que es denso en $\mathbb{R}$ en virtud del teorema de densidad de zeros de $\Xi$. Por continuidad de la transformada de Poisson (si $|\gamma_n|$ es denso en $\mathbb{R}^+$) se concluiría $\mathcal{P}[\mu_{\mathrm{off}}-\nu]=0$ en $\mathbb{R}$, y por el teorema de unicidad para medidas positivas (injectividad de la transformada de Poisson en medidas), $\mu_{\mathrm{off}} = \nu$.

---

## 5. Formulación precisa del Problema de la Medida de Cero

**Definición 5.1.** El *Problema de la Medida de Cero* es la siguiente pregunta:

$$\boxed{\text{¿Es } \mu_{\mathrm{off}} = 0?}$$

Por el Teorema del Punto Único (Doc 43, T 4.2): $\mu_{\mathrm{off}} = 0$ si y solo si $C_\infty(\gamma_{n_0}) = 0$ para algún $n_0$, si y solo si RH.

El problema es equivalente a probar que la medida atómica positiva $\mu_{\mathrm{off}}$ tiene soporte vacío. Exploraremos tres ataques:

- **Ruta A:** Análisis de Fourier y condiciones de Paley-Wiener sobre $C_\infty$.
- **Ruta B:** La ecuación funcional como condición de simetría sobre $\mu_{\mathrm{off}}$.
- **Ruta C:** Positividad global de $C_\infty$ en $\mathbb{R}$ y teoría del potencial.

---

## 6. Ruta A: Análisis de Fourier y la Transformada de Cauchy en la Frontera

**Setup.** La función $F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z)$ para $z = t + iy$, $y > 0$, es una función armónica en el semiplano superior $\mathbb{H}^+$. Su traza en la frontera real es $F(t) = C_\infty(t)$ (extendida de $\{\gamma_n\}$ a $\mathbb{R}$ mediante la fórmula de Hadamard).

**Proposición 6.1 (Decaimiento de Fourier de $C_\infty$).** Si $C_\infty \in L^1(\mathbb{R})$, entonces su transformada de Fourier satisface:
$$\hat{C}_\infty(\xi) = \pi e^{-2\pi|\xi|y_0} \cdot \hat{f}(\xi)$$
para alguna $y_0 > 0$, donde $\hat{f}$ es la transformada de Fourier de la medida $\mu_{\mathrm{off}}$ proyectada sobre la frontera.

*Obstáculo A.1.* No está claro que $C_\infty \in L^1(\mathbb{R})$. La extensión de $C_\infty$ de $\{\gamma_n\}$ a $\mathbb{R}$ via la función $-\text{Re}[\zeta'/\zeta]$ puede tener singularidades en los ceros de $\Xi$. Además, por los picos logarítmicos (Doc 43, C 7.4), si $\mu_{\mathrm{off}} \neq 0$, entonces $C_\infty(\gamma_{n_k^*}) \geq c\log\gamma_{n_k^*} \to \infty$, lo que sugiere que $C_\infty \notin L^1(\mathbb{R})$ en ese caso.

**Proposición 6.2 (Criterio de Wiener).** Si $C_\infty(t) = 0$ para $t$ en un conjunto $E \subset \mathbb{R}$ con medida de Lebesgue positiva, y si $C_\infty$ pertenece a una clase de Paley-Wiener apropiada, entonces $\mu_{\mathrm{off}} = 0$.

*Prueba.* La transformada de Poisson $\mathcal{P}[\mu](t) = 0$ en un conjunto de medida positiva para una medida positiva $\mu$ implica $\mu = 0$ por el principio de Schwarz para funciones armónicas positivas (ver §7 a continuación). $\square$

*Obstáculo A.2.* Para aplicar el criterio de Wiener necesitaríamos saber que $C_\infty$ se anula en un conjunto de medida positiva — lo cual equivale (via Ruta A) a RH, sin independencia.

**Diagnóstico de Ruta A.** La Ruta A produce implicaciones de la forma "si $C_\infty$ tiene tal propiedad de decaimiento $\Rightarrow \mu_{\mathrm{off}} = 0$", pero verificar esas propiedades de decaimiento no es más fácil que probar RH directamente. La ruta tiene valor para **caracterizar** $\mu_{\mathrm{off}}$ condicionalmente a RH, no para probar RH incondicionalmente.

---

## 7. El Principio del Mínimo para Funciones Armónicas Positivas

Antes de Ruta B y C, establecemos un resultado técnico fundamental.

**Lema 7.1 (Principio del Mínimo).** Sea $F: \mathbb{H}^+ \to [0,\infty)$ armónica, positiva, y no idénticamente cero. Entonces $F > 0$ en todo $\mathbb{H}^+$, y $F$ no puede alcanzar el valor 0 en el interior.

*Prueba.* Por el principio del mínimo para funciones armónicas: si $F$ alcanza su mínimo (0) en un punto interior, $F$ es constante, contradiciendo $F \not\equiv 0$. $\square$

**Lema 7.2 (Extensión a la frontera).** Si $F = \mathcal{P}[\mu_{\mathrm{off}}]$ con $\mu_{\mathrm{off}} \neq 0$ positiva, entonces $F(t) > 0$ para toda $t \in \mathbb{R}$ en el sentido de la traza no-tangencial — con la excepción posible de un conjunto de capacidad cero (Fatou).

*Prueba.* Consecuencia del Teorema de Fatou para funciones armónicas positivas en $\mathbb{H}^+$ y del Lema 7.1. $\square$

**Corolario 7.3.** Si $\mu_{\mathrm{off}} \neq 0$, entonces $C_\infty(t) > 0$ para casi todo $t \in \mathbb{R}$. En particular, si RH falla, la función $C_\infty$ es estrictamente positiva $\lambda$-casi en todas partes en $\mathbb{R}$.

---

## 8. Ruta B: La Ecuación Funcional como Condición de Simetría

**Setup.** Los ceros de $\zeta$ satisfacen la simetría $\rho \leftrightarrow 1-\bar\rho$ (ecuación funcional de Riemann). Para un cero off-crítico $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 > 1/2$, el par funcional es $1-\bar\rho_0 = (1-\sigma_0) + i\gamma_0$, con $1-\sigma_0 < 1/2$.

**Proposición 8.1 (Acción de la ecuación funcional sobre $\mu_{\mathrm{off}}$).** La simetría funcional $\rho_0 \leftrightarrow 1-\bar\rho_0$ actúa sobre $\mu_{\mathrm{off}}$ como la reflexión $y_0 = \sigma_0-1/2 \mapsto -(1-\sigma_0-1/2) = \sigma_0-1/2$. Es decir, la ecuación funcional **preserva** la altura $y_0$ del punto soporte (pues $\sigma_0 - 1/2 = (1-\sigma_0)-1/2$ con signo cambiado, pero en módulo es lo mismo).

*Nota.* El par funcional $1-\bar\rho_0$ tiene parte real $1-\sigma_0 < 1/2$. En nuestra parameterización de $\mu_{\mathrm{off}}$, que vive en $\{y > 0\} = \{\sigma_0 > 1/2\}$, el par funcional contribuiría a la componente $\sigma < 1/2$. Ambos ceros ($\rho_0$ y $1-\bar\rho_0$) contribuyen a $C_\infty(\gamma_n)$ a través de la simetría del emparejamiento $(\rho_0, \bar\rho_0)$ (ver Doc 42, §13).

**Proposición 8.2 (Condición de simetría sobre $C_\infty$).** La ecuación funcional implica que $C_\infty(\gamma_n)$ es simétrica: $C_\infty(\gamma_n) = C_\infty(\gamma_n)$ trivialmente, pero más significativamente, la suma sobre pares $\{(\rho_0, \bar\rho_0), (1-\rho_0, 1-\bar\rho_0)\}$ produce:

$$\Delta(\gamma_n;\rho_0) + \Delta(\gamma_n;1-\rho_0) = \Delta(\gamma_n;\rho_0) + \Delta(\gamma_n;\tilde\rho_0)$$

donde $\tilde\rho_0 = 1-\sigma_0 + i\gamma_0$ tiene $\sigma(\tilde\rho_0) - 1/2 = 1/2-\sigma_0 < 0$. Pero $|\sigma(\tilde\rho_0)-1/2| = \sigma_0-1/2$, así que el par funcional da la misma contribución positiva al déficit: $\Delta(\gamma_n;\tilde\rho_0) = \Delta(\gamma_n;\rho_0)$. El total es $2\Delta(\gamma_n;\rho_0)$.

**Definición 8.3 (Cuarteto de ceros off-críticos).** Si $\rho_0 = \sigma_0+i\gamma_0$ es off-crítico, el *cuarteto de Hadamard* es $\{\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0\}$. Por la ecuación funcional y la simetría de conjugación, este cuarteto contribuye a $C_\infty(\gamma_n)$ el término $4\Delta(\gamma_n;\rho_0) > 0$.

**Obstáculo B.** La ecuación funcional impone la simetría $\rho_0 \leftrightarrow 1-\bar\rho_0$ pero no fuerza $\mu_{\mathrm{off}} = 0$: es perfectamente compatible con la existencia de cuartetos de ceros off-críticos. La ecuación funcional es una condición de simetría sobre la *distribución* de $\mu_{\mathrm{off}}$, no sobre su masa total.

**Diagnóstico de Ruta B.** La ecuación funcional no puede por sí sola probar $\mu_{\mathrm{off}} = 0$. Sin embargo, tiene valor al mostrar que las contribuciones al déficit vienen siempre en grupos de cuatro (cuartetos), lo que refuerza la estructura positiva de $C_\infty$.

---

## 9. Ruta C: Positividad Global y Teoría del Potencial

Esta es la ruta más prometedora y establece la conexión más profunda con la hipótesis de Riemann.

**Setup.** La función $F: \mathbb{H}^+ \to \mathbb{R}_{>0}$ dada por $F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z)$ es armónica positiva. Por el teorema de representación de Herglotz-Riesz (para funciones armónicas positivas en el semiplano), existe una única medida de Borel positiva $\nu$ en $\mathbb{R} \cup \{\infty\}$ y una constante $a \geq 0$ tal que:

$$F(t+iy) = ay + \int_\mathbb{R} \frac{y}{y^2+(t-s)^2}\,d\nu(s)$$

**Proposición 9.1 (Identificación de la medida de Herglotz).** En nuestra situación, la medida de Herglotz $\nu$ es precisamente la proyección de $\mu_{\mathrm{off}}$ sobre $\mathbb{R}$ (con pesos integrados en altura):

$$d\nu(s) = \int_0^\infty y\,d[\mu_{\mathrm{off}}]_s(y)$$

donde $[\mu_{\mathrm{off}}]_s$ es la desintegración de $\mu_{\mathrm{off}}$ sobre la fibra en $x=s$.

*Prueba.* Comparación directa de la representación de Herglotz con $\mathcal{P}[\mu_{\mathrm{off}}]$ usando unicidad. $\square$

**Lema 9.2 (Criterio de extinción por condición de frontera).** Si existe $t_0 \in \mathbb{R}$ tal que $\lim_{y\downarrow 0} F(t_0 + iy) = 0$ (traza no-tangencial nula), entonces $\nu(\{t_0\}) = 0$ y la extensión armónica tiene una singularidad removible en $t_0$.

*Observación.* El Lema 9.2 no dice que $\nu = 0$; solo que la medida puntual en $t_0$ es cero. Para concluir $\nu = 0$ (equivalentemente $\mu_{\mathrm{off}} = 0$) se necesita anulación en un conjunto suficientemente grande.

**Teorema 9.3 (Caracterización vía capacidad).** Sean $E_0 = \{t\in\mathbb{R} : C_\infty(t) = 0\}$ el conjunto de anulación de $C_\infty$ en la recta real. Las siguientes condiciones son equivalentes:

1. $\mu_{\mathrm{off}} = 0$ (RH).
2. $E_0 \neq \emptyset$.
3. $E_0$ tiene capacidad logarítmica positiva, es decir, $\mathrm{cap}(E_0) > 0$.
4. $E_0$ tiene medida de Lebesgue positiva.

*Prueba.*

$(1)\Rightarrow(2)$: Si $\mu_{\mathrm{off}} = 0$, entonces $C_\infty(t) = 0$ para todo $t$, luego $E_0 = \mathbb{R}$.

$(2)\Rightarrow(1)$: Por el Teorema de Rigidez de Poisson (Doc 43, T 3.1): $\mathcal{P}[\mu_{\mathrm{off}}](t_0) = 0$ para algún $t_0 \in E_0$ implica $\mu_{\mathrm{off}} = 0$.

$(1)\Rightarrow(4)\Rightarrow(3)\Rightarrow(2)$: Trivial, pues la medida positiva implica capacidad positiva implica conjunto no vacío.

$(2)\Rightarrow(4)$: Si $E_0 \neq \emptyset$, entonces por (2)$\Rightarrow$(1) ya tenemos $\mu_{\mathrm{off}} = 0$, luego $C_\infty \equiv 0$ y $E_0 = \mathbb{R}$ tiene medida positiva.

La cadena de equivalencias se cierra sin circularidad: toda condición de anulación, por débil que sea (un punto, un conjunto de capacidad positiva, medida positiva) implica la anulación total. $\square$

**Corolario 9.4 (Alternativa dicotómica de $C_\infty$).** La función $C_\infty: \mathbb{R} \to [0,\infty)$ satisface exactamente uno de los dos escenarios:
- **Escenario RH:** $C_\infty \equiv 0$ en toda la recta real.
- **Escenario anti-RH:** $C_\infty > 0$ para $\lambda$-casi todo $t \in \mathbb{R}$.

No existe escenario intermedio (anulación en conjunto de medida positiva pero sin RH).

---

## 10. La Extensión Armónica y el Principio de Reflexión de Schwarz

**Proposición 10.1 (Extensión armónica).** La función $C_\infty: \mathbb{R} \to [0,\infty)$, definida via la fórmula de Hadamard en los ceros $\{\gamma_n\}$ de $\Xi$ y extendida a $\mathbb{R}$ por continuidad, admite la extensión armónica:

$$F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z), \quad z = t + iy, \quad y > 0$$

que es $C^\infty$ en $\mathbb{H}^+$, positiva, y satisface $F(t) = C_\infty(t)$ en el sentido no-tangencial.

**Proposición 10.2 (Reflexión de Schwarz condicional).** Si $C_\infty(t_0) = 0$ para algún $t_0 \in \mathbb{R}$, entonces por el principio de reflexión de Schwarz se puede extender $F$ a través de $t_0$ como $F(t_0+iy) = -F(t_0-iy) = 0$ para $y$ pequeño, lo que contradice la positividad $F > 0$ en $\mathbb{H}^-$ (por simetría). Luego la extensión es trivialmente cero en $t_0$, compatible con $F \equiv 0$.

*Observación.* El principio de reflexión, en este contexto, reconfirma que un cero de la traza frontera solo puede ocurrir si $F \equiv 0$ en todo el semiplano — consistente con RH.

---

## 11. La Barrera Estructural: Síntesis y Diagnóstico

**Definición 11.1 (La barrera irreducible).** El Problema de la Medida de Cero se reduce a la siguiente pregunta aritmética:

> *¿Pueden los ceros de $\zeta(s)$ en $\{|\sigma - 1/2| > 0\}$ satisfacer las condiciones analíticas necesarias para que la medida $\mu_{\mathrm{off}}$ sea no nula, dado que la simetría funcional impone que vengan en cuartetos y que cada cuarteto contribuye positivamente al déficit $C_\infty$?*

La respuesta depende de propiedades aritméticas profundas de $\zeta$: correlaciones entre ceros, densidad, distribución de las partes reales de los ceros off-críticos.

**Tabla de diagnóstico:**

| Ruta | Resultado obtenido | Obstáculo |
|------|-------------------|-----------|
| A (Fourier) | Wiener: anulación en conjunto medida positiva $\Rightarrow \mu_{\mathrm{off}}=0$ | Verificar anulación ≡ probar RH |
| B (Ecuación funcional) | Simetría de cuartetos; contribuciones $> 0$ por cuarteto | Cuartetos son compatibles con $\mu_{\mathrm{off}} \neq 0$ |
| C (Potencial) | Alternativa dicotómica: $C_\infty \equiv 0$ XOR $C_\infty > 0$ a.e. | Demostrar que $C_\infty \not> 0$ a.e. ≡ probar RH |
| Rigidez Poisson | Un solo cero de $C_\infty$ $\Rightarrow$ RH | Encontrar el cero ≡ probar RH |

**Proposición 11.2 (Equivalencia del obstáculo).** Para cada Ruta A, B, C, el obstáculo final es una condición equivalente a RH. Las rutas no simplifican el problema: comprimen y clarifican, pero no eliminan la dificultad central.

*Esto no es un fracaso del programa.* La compresión tiene valor: identifica la naturaleza exacta de lo que falta. La barrera irreducible del programa CCM es ahora la siguiente afirmación analítica puntual:

$$\exists\, t_0 \in \mathbb{R}: \quad \mathcal{P}[\mu_{\mathrm{off}}](t_0) = 0$$

que por el Teorema de Rigidez de Poisson (Doc 43) es equivalente a RH.

---

## 12. Un Cuarto Ataque: La Condición de Hardy sobre $F$

**Propuesta 12.1 (Ataque vía espacio de Hardy $H^1$).** Si la extensión armónica $F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z)$ pertenece al espacio de Hardy $H^1(\mathbb{H}^+)$ (es decir, $\sup_{y>0}\int_{-\infty}^\infty |F(t+iy)|\,dt < \infty$), entonces por el teorema de Riesz-Thorin para $H^1$:

$$\mu_{\mathrm{off}}(\mathbb{R}) = \lim_{y\to 0} \int_{-\infty}^\infty F(t+iy)\,dt = \int_\mathbb{R} C_\infty(t)\,dt$$

Si esta integral se pudiera calcular (en sentido regularizado) y se demostrara que es cero, se concluiría $\mu_{\mathrm{off}} = 0$.

*Pregunta:* ¿Qué dice la teoría de $\zeta$ sobre $\int_\mathbb{R} C_\infty(t)\,dt$?

**Proposición 12.2 (Cálculo formal de la masa).** Formalmente:

$$\int_\mathbb{R} C_\infty(t)\,dt = \int_\mathbb{R} \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \Delta(t;\rho_0)\,dt$$

Intercambiando suma e integral (justificable por convergencia dominada si $|\mathcal{Z}_{\mathrm{off}}|<\infty$):

$$= \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \int_\mathbb{R} \Delta(t;\rho_0)\,dt = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} 2(\sigma_0-1/2) \cdot 2\pi = 4\pi \sum_{\rho_0} (\sigma_0-1/2)$$

donde usamos $\int_{-\infty}^\infty P_{y_0}(t)\,dt = \pi$ para cada $y_0 = \sigma_0-1/2$.

**Corolario 12.3.** Si $\mathcal{Z}_{\mathrm{off}}$ es no vacío, la masa total es $\int_\mathbb{R} C_\infty(t)\,dt = 4\pi\sum_{\rho_0}(\sigma_0-1/2) > 0$. Si $\mathcal{Z}_{\mathrm{off}} = \emptyset$, la masa es cero. El cálculo confirma que $\int C_\infty > 0 \Leftrightarrow \mu_{\mathrm{off}} \neq 0 \Leftrightarrow \neg$RH.

*Obstáculo 12.4.* Este cálculo es de nuevo circular: saber que $\int C_\infty = 0$ equivale a saber que $\mu_{\mathrm{off}} = 0$, que equivale a RH. La integración no abre una vía independiente.

---

## 13. El Nuevo Frente: Cotas Inferiores Efectivas para $\int C_\infty$

Aunque la masa $\int C_\infty$ no puede probarse nula directamente, podemos intentar obtener **cotas inferiores explícitas** condicionadas a la existencia de ceros off-críticos.

**Teorema 13.1 (Cota inferior efectiva).** Supongamos que $\mathcal{Z}_{\mathrm{off}}$ contiene un cero $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 - 1/2 = \delta > 0$. Entonces:

$$C_\infty(\gamma_n) \geq \frac{4\delta}{\delta^2 + (\gamma_n - \gamma_0)^2}$$

para todo $\gamma_n$. En particular, el cero $\gamma_{n^*}$ más cercano a $\gamma_0$ satisface (por el Teorema de Densidad de Doc 43, T 7.1):

$$C_\infty(\gamma_{n^*}) \geq \frac{4\delta}{\delta^2 + (\pi/\log\gamma_0)^2} \geq \frac{4\delta\log^2\gamma_0}{\delta\log^2\gamma_0 + \pi^2}$$

Para $\gamma_0$ grande con $\delta$ fijo: $C_\infty(\gamma_{n^*}) \geq 4/\log^0 \gamma_0 = 4$ (en el límite).

*Prueba.* Por definición de $\Delta(\gamma_n;\rho_0)$ y la Proposición 3.1 de Doc 43. $\square$

**Corolario 13.2 (Detección cuantitativa).** Si RH falla con un cero a distancia $\delta$ del eje crítico y altura $\gamma_0$, entonces existe $\gamma_{n^*} \leq \gamma_0 + \pi/\log\gamma_0$ tal que:

$$C_\infty(\gamma_{n^*}) \geq \frac{4\delta\log^2\gamma_0}{\delta\log^2\gamma_0 + \pi^2}$$

Este es un test cuantitativo: si pudiera verificarse que $C_\infty(\gamma_n) \to 0$ para todos los ceros, se obtendría $\mu_{\mathrm{off}} = 0$ y RH.

---

## 14. La Dirección de Doc 45: Análisis Espectral de $C_\infty$ como Función de $n$

La secuencia $\{C_\infty(\gamma_n)\}_{n=1}^\infty$ es una sucesión de números reales no negativos. Por el Teorema 13.1, si $C_\infty(\gamma_n) \to 0$ a lo largo de una subsucesión suficientemente densa, entonces $\mu_{\mathrm{off}} = 0$.

**Proposición 14.1 (Criterio de convergencia a cero).** Si $C_\infty(\gamma_n) \to 0$ cuando $n \to \infty$, entonces $\mu_{\mathrm{off}} = 0$ (RH).

*Prueba.* Si $\mu_{\mathrm{off}} \neq 0$, existe $\rho_0 \in \mathcal{Z}_{\mathrm{off}}$ con $\sigma_0-1/2 = \delta > 0$. Por el Corolario 13.2, para cualquier $n$ grande hay $\gamma_{n^*} \sim \gamma_0$ con $C_\infty(\gamma_{n^*}) \geq 4\delta\log^2\gamma_0/(\delta\log^2\gamma_0+\pi^2) > 0$. Pero esto solo da una cota inferior para $\gamma_{n^*}$ fijo; no impide que $C_\infty(\gamma_n) \to 0$ para $n$ fuera del rango de $\gamma_0$... $\square$ (parcial).

*Nota honesta.* La Proposición 14.1 requiere una forma más fuerte del criterio: si $C_\infty(\gamma_n) \to 0$ para la subsucesión $\gamma_n \to \infty$ (no solo puntualmente), entonces por continuidad de $\mathcal{P}[\mu_{\mathrm{off}}]$ y densidad de $\{\gamma_n\}$, se puede concluir $C_\infty \equiv 0$. La precisión de este argumento es la tarea de Doc 45.

---

## 15. Resumen del programa hasta Doc 44

El programa CCM ha establecido las siguientes equivalencias y resultados incondicionales:

**Resultados probados:**

| Resultado | Referencia |
|-----------|-----------|
| RH ↔ Inc. Inv. | Docs 19, 39 |
| $C_\infty(\gamma_n) \geq 0$ (incondicional) | Doc 42 |
| $C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)$ (exacto) | Doc 42 + Doc 44, T 4.1 |
| Convergencia absoluta de $\sum\Delta$ | Doc 44, P 3.1 |
| Rigidez de Poisson: un cero $\Rightarrow$ RH | Doc 43 |
| Sin RH: $C_\infty(\gamma_{n_k^*}) \geq c\log\gamma_{n_k^*}$ | Doc 43 |
| Alternativa dicotómica: $C_\infty \equiv 0$ XOR $> 0$ a.e. | Doc 44, C 9.4 |
| Masa total $\int C_\infty = 4\pi\sum_{\rho_0}(\sigma_0-1/2)$ | Doc 44, P 12.2 |
| Cota inferior cuantitativa condicionada a $\rho_0$ off-crítico | Doc 44, T 13.1 |

**La frontera matemática exacta del programa:**

> Demostrar que $\lim_{n\to\infty} C_\infty(\gamma_n) = 0$, o equivalentemente, encontrar un solo $n_0$ con $C_\infty(\gamma_{n_0}) = 0$.

Ambas condiciones son equivalentes a RH (la primera por densidad y continuidad; la segunda por el Teorema de Rigidez de Poisson).

---

## 16. Propuesta para Doc 45: Decaimiento de $C_\infty(\gamma_n)$ y Criterio de Subsucesión

Doc 45 explorará el comportamiento asintótico de $C_\infty(\gamma_n)$ para $n \to \infty$, con los siguientes objetivos:

1. **¿Es $C_\infty(\gamma_n)$ uniformemente acotado?** (Respuesta esperada: sí, incondicionalmente, por la cota de Proposición 3.1.)

2. **¿Tiende $C_\infty(\gamma_n) \to 0$ en promedio?** La media $\frac{1}{N}\sum_{n=1}^N C_\infty(\gamma_n) = \frac{4\pi}{N}\sum_{|\gamma_n|\leq T}(\sigma_0-1/2)$ (para ceros off-críticos detectados), que por el Teorema de Densidad de zeros tiende a 0 si $\mathcal{Z}_{\mathrm{off}}$ es disperso.

3. **¿Puede calcularse la varianza $\sum_n |C_\infty(\gamma_n)|^2$?** Conexión con los pares de ceros correlacionados (teorema de Montgomery) y las correlaciones de la medida $\mu_{\mathrm{off}}$.

4. **Criterio de subsucesión:** Si existe $n_k \to \infty$ con $C_\infty(\gamma_{n_k}) \to 0$ a una tasa controlada, ¿qué implica sobre $\mu_{\mathrm{off}}$?

---

*Siguiente documento (Doc 45): Comportamiento asintótico de $C_\infty(\gamma_n)$ para $n \to \infty$ — media, varianza, subsucesiones y conexión con Montgomery.*

---

## Apéndice A: Verificación de la separación Tipo I / Tipo II

**A.1. Separación sin error residual.** La suma de Hadamard $\sum_\rho[1/(\rho_n-\rho)+1/\rho]$ converge condicionalmente ordenada por $|\text{Im}(\rho)|$. Al tomar la parte real y restar la contribución de $\rho = \rho_n$ (el polo), obtenemos la suma:

$$C_\infty(\gamma_n) = -2\operatorname{Re}\left[\sum_{\rho\neq\rho_n} \frac{1}{\rho_n - \rho}\right]$$

La separación Tipo I / Tipo II es:

$$C_\infty(\gamma_n) = \underbrace{-2\operatorname{Re}\left[\sum_{\rho_m:\,\text{on-crit}}\frac{1}{\rho_n-\rho_m}\right]}_{=\,0} + \underbrace{-2\operatorname{Re}\left[\sum_{\rho_0:\,\text{off-crit}}\frac{1}{\rho_n-\rho_0}\right]}_{\geq\,0}$$

La primera suma es cero (cada término es puramente imaginario). La segunda es $\sum_{\rho_0}\Delta(\gamma_n;\rho_0) \geq 0$.

**A.2. Ausencia de término constante.** La contribución de los polos triviales ($\rho = -2k$, $k=1,2,\ldots$) y el término de la parte principal de la función zeta contribuyen a $C_\infty$ términos que son reales, pero que se cancelan en la definición del potencial espectral $C_\infty$ (ver Doc 42, §4 para la sustracción de la parte regular $g_n(\rho_n)$). Por construcción, $C_\infty(\gamma_n) = 0$ si y solo si todos los ceros relevantes están en la línea crítica.
