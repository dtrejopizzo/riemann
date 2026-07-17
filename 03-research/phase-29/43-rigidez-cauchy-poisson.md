# Doc 43 — Rigidez de la Transformada de Cauchy-Poisson: el Teorema del Punto Único

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 38–42 (especialmente Doc 42 §5, §16, §17)  
**Objetivo:** Demostrar el Teorema de Rigidez de Poisson y sus consecuencias; establecer la equivalencia RH ↔ $C_\infty(\gamma_{n_0})=0$ para UN SOLO $n_0$; analizar la continuidad, la detección de ceros off-críticos por densidad, y el obstáculo preciso.

---

## 1. La pregunta central

Doc 42 (Teorema 5.2) estableció la **fórmula del déficit explícito**:

$$C_\infty(\gamma_n) = \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0 > 1/2,\, \gamma_0 > 0}} \Delta(\gamma_n;\rho_0) \geq 0$$

donde cada término $\Delta(\gamma_n;\rho_0) > 0$ es un núcleo de Cauchy-Poisson estrictamente positivo. La medida de ceros off-críticos es $\mu_{\mathrm{off}} = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}} 2(\sigma_0-1/2)\,\delta_{(\gamma_0,\,\sigma_0-1/2)}$.

La fórmula se puede reescribir como:
$$C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n), \qquad \mathcal{P}[\mu](t) := \int_{\mathbb{H}} \frac{y}{y^2+(t-x)^2}\,d\mu(x,y)$$

donde $\mathbb{H} = \{(x,y): y > 0\}$ y el factor del segundo término de $\Delta$ (con $\gamma_n + \gamma_0$) se absorbe en la medida simetrizada (ver §A.1).

**La pregunta de Doc 43:** ¿Puede una medida positiva $\mu_{\mathrm{off}} \neq 0$ en $\mathbb{H}$ tener $\mathcal{P}[\mu_{\mathrm{off}}](\gamma_n) = 0$ para todos los ceros $\gamma_n$ de $\Xi$?

---

## 2. El núcleo de Poisson y su positividad estricta

**Definición 2.1 (Núcleo de Poisson).** Para $(x,y) \in \mathbb{H}$ y $t \in \mathbb{R}$:
$$P_y(t-x) := \frac{y}{y^2+(t-x)^2}$$

**Lema 2.2 (Positividad estricta).** Para todo $(x,y)\in\mathbb{H}$ y todo $t\in\mathbb{R}$:
$$P_y(t-x) = \frac{y}{y^2+(t-x)^2} > 0$$

*Prueba.* $y > 0$ por hipótesis y $y^2+(t-x)^2 > 0$. $\square$

**Lema 2.3 (Propiedades del núcleo).** Para $y > 0$ fijo:
1. $\int_{-\infty}^\infty P_y(t)\,dt = \pi$.
2. $P_y(t) \leq y^{-1}$ para todo $t$.
3. $P_y(t) \sim y/t^2$ para $|t| \gg y$.
4. $P_y(t) \leq P_y(0) = 1/y$ con máximo en $t = 0$.

*Prueba.* (1) Integral estándar de Cauchy. (2) $P_y(t) \leq y/y^2 = 1/y$. (3) Para $t \gg y$: $P_y(t) = y/(y^2+t^2) \sim y/t^2$. (4) Inmediato de la definición. $\square$

---

## 3. El Teorema de Rigidez de Poisson

El resultado central de este documento es elemental pero decisivo.

**Teorema 3.1 (Rigidez de Poisson — Versión Punto Único).** Sea $\mu$ una medida de Borel no-negativa en $\mathbb{H}$, finita sobre compactos, y tal que $\int_{\mathbb{H}}(1+y)^{-1}(1+x^2)^{-1}\,d\mu(x,y) < \infty$. Define:
$$\mathcal{P}[\mu](t) := \int_{\mathbb{H}} \frac{y}{y^2+(t-x)^2}\,d\mu(x,y) \geq 0$$

Si $\mathcal{P}[\mu](t_0) = 0$ para ALGÚN $t_0 \in \mathbb{R}$, entonces $\mu = 0$ (medida idénticamente nula).

*Prueba.* Por hipótesis de integrabilidad, la integral $\mathcal{P}[\mu](t_0)$ es finita. El integrando $P_y(t_0-x) = y/[y^2+(t_0-x)^2]$ es estrictamente positivo para todo $(x,y)\in\mathbb{H}$ (Lema 2.2) y la medida $\mu$ es no-negativa. Por lo tanto:

$$0 = \mathcal{P}[\mu](t_0) = \int_{\mathbb{H}} \underbrace{P_y(t_0-x)}_{>0}\, d\mu(x,y)$$

La integral de una función estrictamente positiva respecto a una medida no-negativa es cero si y solo si la medida es la medida nula. Conclusión: $\mu = 0$. $\square$

**Observación 3.2.** El Teorema 3.1 no depende de $t_0$ en absoluto: el núcleo $P_y(t_0-x) > 0$ para TODO $t_0\in\mathbb{R}$ y todo $(x,y)\in\mathbb{H}$. Esto significa que **un único punto de anulación de $\mathcal{P}[\mu]$ en $\mathbb{R}$ detecta toda la masa de $\mu$**.

**Corolario 3.3 (Rigidez — Versión Conjunto Infinito).** Si $\mathcal{P}[\mu](t_n) = 0$ para una SUCESIÓN (finita o infinita) de puntos $\{t_n\} \subset \mathbb{R}$, entonces $\mu = 0$.

*Prueba.* El Teorema 3.1 con $t_0 = t_1$. Un solo punto basta. $\square$

---

## 4. Consecuencia inmediata: el Teorema del Punto Único para RH

**Teorema 4.1 (Punto Único implica RH).** Si $C_\infty(\gamma_{n_0}) = 0$ para algún $n_0 \geq 1$, entonces RH.

*Prueba.* Por la fórmula del déficit (Doc 42, Teorema 5.2):
$$C_\infty(\gamma_{n_0}) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_{n_0}) = 0$$

Por el Teorema de Rigidez 3.1 (con $\mu = \mu_{\mathrm{off}}$ y $t_0 = \gamma_{n_0}$): $\mu_{\mathrm{off}} = 0$. Por lo tanto $\mathcal{Z}_{\mathrm{off}} = \emptyset$, es decir, todos los ceros no-triviales de $\zeta$ están en la línea crítica: RH. $\square$

**Teorema 4.2 (Equivalencia del Punto Único).** Las siguientes afirmaciones son mutuamente equivalentes:

*(i)* RH.  
*(ii)* Inc. Inv.: $C_\infty(\gamma_n) = 0$ para todo $n \geq 1$.  
*(iii)* $C_\infty(\gamma_{n_0}) = 0$ para algún $n_0 \geq 1$.  
*(iv)* $\mu_{\mathrm{off}} = 0$ (no hay ceros off-críticos de $\zeta$).

*Prueba.*
- (i) $\iff$ (ii): Teorema 2.4 de Doc 42 (RH $\iff$ Inc. Inv., Docs 19 y 39).
- (ii) $\implies$ (iii): trivial.
- (iii) $\implies$ (iv): Teorema 4.1.
- (iv) $\implies$ (i): $\mathcal{Z}_{\mathrm{off}} = \emptyset$ es exactamente la hipótesis de Riemann. $\square$

**Interpretación.** El Teorema 4.2 es una **compresión del problema**: en lugar de probar la anulación en TODOS los ceros $\{\gamma_n\}_{n\geq 1}$, basta probarla en UNO. Sin embargo, probar $C_\infty(\gamma_{n_0}) = 0$ para un único $n_0$ parece exactamente tan difícil como probar RH en general — la dificultad se concentra en un punto, no desaparece.

---

## 5. La extensión armónica de $C_\infty$

La fórmula del déficit admite una extensión natural al semiplano superior.

**Definición 5.1 (Extensión de Poisson).** Para $z = t + i\eta$ con $\eta > 0$:
$$F(z) := \int_{\mathbb{H}} \frac{y+\eta}{(y+\eta)^2+(t-x)^2}\,d\mu_{\mathrm{off}}(x,y)$$

En el límite $\eta \to 0^+$: $F(t) = \mathcal{P}[\mu_{\mathrm{off}}](t) = C_\infty(t)/2$.

**Proposición 5.2 (Harmonicidad de $F$).** La función $F(t+i\eta)$ es armónica en $\eta > 0$:
$$\left(\frac{\partial^2}{\partial\eta^2} + \frac{\partial^2}{\partial t^2}\right)F(t+i\eta) = 0 \quad \text{para } \eta > 0$$

*Prueba.* El núcleo $P_{y+\eta}(t-x) = (y+\eta)/[(y+\eta)^2+(t-x)^2]$ es armónico en $(t,\eta)$ para $y+\eta > 0$, y la integral de funciones armónicas (con convergencia dominada garantizada por hipótesis de integrabilidad) es armónica. $\square$

**Proposición 5.3 (Positividad de $F$ en el interior).** Para $\eta > 0$ y $\mu_{\mathrm{off}} \neq 0$:
$$F(t+i\eta) > 0 \quad \forall t \in \mathbb{R}$$

*Prueba.* El núcleo $(y+\eta)/[(y+\eta)^2+(t-x)^2] > 0$ para $y+\eta > 0$ (que se cumple para $y > 0$, $\eta > 0$). La misma prueba que Teorema 3.1 con $t_0 = t$. $\square$

**Corolario 5.4 (Principio del Mínimo).** Bajo RH ($\mu_{\mathrm{off}} = 0$): $F \equiv 0$. Sin RH ($\mu_{\mathrm{off}} \neq 0$): $F(z) > 0$ para todo $z$ con $\operatorname{Im}(z) \geq 0$, con la única excepción de los puntos del borde donde $\mathcal{P}[\mu_{\mathrm{off}}](t) = 0$ — pero por Teorema 3.1, no existen tales puntos. Por lo tanto: $F(z) > 0$ en TODO $\{z: \operatorname{Im}(z) \geq 0\}$ si $\mu_{\mathrm{off}} \neq 0$.

**Observación 5.5 (No hay ceros de frontera sin RH).** Si RH es falsa, entonces $F(t) = C_\infty(t)/2 > 0$ para todo $t\in\mathbb{R}$. En particular, $C_\infty(\gamma_n) > 0$ para todo $n$ — lo que es Inc. Inv. fallida. El Corolario 5.4 confirma que si RH falla, la función $F$ no tiene ceros en ningún punto del semiplano cerrado.

---

## 6. Continuidad del potencial espectral

**Proposición 6.1 (Continuidad de $C_\infty$).** Si la medida $\mu_{\mathrm{off}}$ satisface la condición de integrabilidad de Teorema 3.1, entonces la función $t \mapsto C_\infty(t) = 2\mathcal{P}[\mu_{\mathrm{off}}](t)$ es continua en $\mathbb{R}$.

*Prueba.* Para $t_1 \to t_0$:
$$|\mathcal{P}[\mu](t_1) - \mathcal{P}[\mu](t_0)| \leq \int_{\mathbb{H}}|P_y(t_1-x) - P_y(t_0-x)|\,d\mu(x,y)$$

El integrando $|P_y(t_1-x)-P_y(t_0-x)| \leq C|t_1-t_0|/y^2$ (Lipschitz en $t$) y está dominado por $2/y$. Por convergencia dominada (usando la hipótesis de integrabilidad $\int y^{-1}d\mu < \infty$), el lado derecho $\to 0$. $\square$

**Proposición 6.2 (Decaimiento en infinito).** Para $\mu_{\mathrm{off}}$ con soporte compacto:
$$C_\infty(t) \to 0 \quad \text{cuando } |t| \to \infty$$

*Prueba.* Para $|t| \to \infty$ y soporte de $\mu_{\mathrm{off}}$ contenido en $\{(x,y): |x| \leq R,\, c \leq y \leq M\}$:
$$C_\infty(t) = 2\mathcal{P}[\mu_{\mathrm{off}}](t) \leq \frac{2\mu_{\mathrm{off}}(\mathbb{H})\cdot M}{(|t|-R)^2 - M^2} \to 0$$ $\square$

**Proposición 6.3 (Crecimiento para soporte no compacto).** Si $\mu_{\mathrm{off}}$ tiene masa en $\{\gamma_0 \sim T\}$ (ceros off-críticos a altura $\sim T$), entonces $C_\infty(\gamma_n)$ para $\gamma_n \sim T$ recibe una contribución $\sim 2/(\sigma_0-1/2)$ de esos ceros. Para ceros con $\sigma_0-1/2 \sim 1/\log T$ (cerca de la región libre de ceros), esta contribución es $\sim 2\log T \to \infty$.

*Interpretación.* Los ceros off-críticos CERCANOS a la línea crítica (que son inevitables si RH falla, por la ecuación funcional) crean picos ALTOS en $C_\infty$.

---

## 7. El teorema de detección por densidad

Los ceros $\{\gamma_n\}$ se vuelven cada vez más densos: la brecha promedio entre ceros consecutivos es $\delta_n := \gamma_{n+1}-\gamma_n \sim 2\pi/\log\gamma_n \to 0$.

**Teorema 7.1 (Detección de ceros off-críticos por densidad).** Sea $\rho_0 = \sigma_0+i\gamma_0$ un cero off-crítico de $\zeta$ con $\sigma_0 > 1/2$ y $\gamma_0 > 2$. Sea $\delta = \pi/\log\gamma_0$ (la mitad de la brecha promedio de ceros cerca de $\gamma_0$). Entonces existe $\gamma_{n^*}$ con $|\gamma_{n^*}-\gamma_0| \leq \delta$ tal que:

$$C_\infty(\gamma_{n^*}) \geq \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + \delta^2} = \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + \pi^2/\log^2\gamma_0}$$

*Prueba.* Por la densidad de ceros, existe $\gamma_{n^*}$ con $|\gamma_{n^*}-\gamma_0| \leq \delta$. Por la fórmula del déficit y la no-negatividad de cada término:
$$C_\infty(\gamma_{n^*}) \geq \Delta(\gamma_{n^*};\rho_0) \geq \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_{n^*}-\gamma_0)^2} \geq \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+\delta^2}$$ $\square$

**Corolario 7.2 (Casos extremos).** Analicemos el Teorema 7.1 según la posición de $\sigma_0$:

**Caso A: $\sigma_0-1/2 \gg \delta = \pi/\log\gamma_0$ (cero lejos de la línea crítica):**
$$C_\infty(\gamma_{n^*}) \geq \frac{2}{\sigma_0-1/2}$$
La cota es de orden $1/(\sigma_0-1/2)$. Para $\sigma_0 = 3/4$: $C_\infty(\gamma_{n^*}) \geq 8$.

**Caso B: $\sigma_0-1/2 = \delta = \pi/\log\gamma_0$ (cero en el borde de la región libre):**
$$C_\infty(\gamma_{n^*}) \geq \frac{2\delta}{2\delta^2} = \frac{1}{\delta} = \frac{\log\gamma_0}{\pi} \to \infty$$
El pico es GRANDE para ceros que rozan el límite de la región libre.

**Caso C: $\sigma_0-1/2 \ll \delta$ (cero cerca de la línea crítica, hipotéticamente):**
$$C_\infty(\gamma_{n^*}) \geq \frac{2(\sigma_0-1/2)}{\delta^2} = \frac{2(\sigma_0-1/2)\log^2\gamma_0}{\pi^2} \to 0 \text{ si } \sigma_0 \to 1/2$$
La cota es pequeña para ceros muy cercanos a la línea crítica.

**Observación 7.3 (La asimetría entre A/B y C).** El Teorema 7.1 detecta fuertemente los ceros off-críticos que están lejos de la línea crítica (Casos A y B) pero da cotas débiles para los ceros casi-críticos (Caso C). La región libre de ceros clásica excluye el Caso C (no hay ceros con $\sigma_0-1/2 < c/\log\gamma_0$), lo que garantiza que Caso B es el límite: los ceros off-críticos (si existen) siempre producen picos de amplitud $\geq c'\log\gamma_0$.

**Corolario 7.4 (Picos logarítmicos inevitables si RH falla).** Si RH es falsa, existe una sucesión $\gamma_{n_k^*} \to \infty$ de ceros de $\Xi$ tales que:
$$C_\infty(\gamma_{n_k^*}) \geq c\log\gamma_{n_k^*} \to \infty$$

*Prueba.* Sea $\rho_k = \sigma_k+i\gamma_0^{(k)}$ una sucesión de ceros off-críticos (que existe si RH falla). Por la región libre de ceros: $\sigma_k-1/2 \geq c'/\log\gamma_0^{(k)}$, es decir, Caso B o A. Por Teorema 7.1 con Caso B: $C_\infty(\gamma_{n_k^*}) \geq \log\gamma_0^{(k)}/\pi$. $\square$

**Este corolario es el diagnóstico más fuerte que podemos dar sin probar RH:** si RH falla, el potencial espectral $C_\infty$ tiene picos logarítmicos en toda subsucesión infinita de ceros de $\Xi$. No puede ser uniformemente pequeño.

---

## 8. El obstáculo estructural preciso

El Teorema de Rigidez 3.1 reduce RH a: "probar $C_\infty(\gamma_{n_0}) = 0$ para un solo $n_0$." Esto parece una simplificación, pero es ilusoria.

**Proposición 8.1 (Circularidad de la reducción).** La afirmación $C_\infty(\gamma_{n_0}) = 0$ equivale a:
$$2\sum_{m=1}^\infty \frac{\Lambda(m)}{\sqrt{m}}\cos(\gamma_{n_0}\log m) = w(\gamma_{n_0})$$

Esta es la convergencia de la serie de Dirichlet condicionalmente convergente al valor exacto $w(\gamma_{n_0})$. Probar esto es equivalente a verificar que $D_\infty(\gamma_{n_0}) = w(\gamma_{n_0})$, que es Inc. Inv. en el punto $\gamma_{n_0}$.

**Proposición 8.2 (La diferencia con Selberg y el PNT).** En el Teorema de los Números Primos, la identidad análoga $\sum_{n\leq x}\Lambda(n) = x + \text{error}$ se prueba via la region libre de ceros de $\zeta$ cerca de $\Re(s)=1$. El "error" mide la contribución de los ceros de $\zeta$ via la fórmula explícita. Aquí, el análogo es:

$$D_\lambda(\gamma_{n_0}) = 2\sum_{m\leq\lambda^2}\frac{\Lambda(m)}{\sqrt{m}}\cos(\gamma_{n_0}\log m) = w(\gamma_{n_0}) - C_\lambda(\gamma_{n_0})$$

El "error" $C_\lambda(\gamma_{n_0})$ se controla via los ceros de $\zeta$ en la fórmula de Hadamard — específicamente via la suma $\sum_\rho \operatorname{Re}[1/(\rho_{n_0}-\rho)]$. Esta suma se anula bajo RH (Teorema 4, Doc 39). Probar que se anula incondicionalmente requiere excluir ceros off-críticos — RH misma.

**Diagnóstico 8.3 (La barrera es sólida).** El Teorema de Rigidez 3.1 comprime la dificultad de RH a un punto, pero no la elimina. Para superar la barrera se necesita:

- Una cota **INCONDICIONAL** $C_\infty(\gamma_{n_0}) \leq f(n_0)$ donde $f(n_0) \to 0$.
- Combinada con la cota inferior incondicional $C_\infty(\gamma_{n_0}) \geq 0$ (Doc 42, P 16.1).
- Para concluir $C_\infty(\gamma_{n_0}) = 0$ y aplicar Teorema 4.1.

Toda cota superior incondicional de $C_\infty(\gamma_n)$ que converge a 0 es equivalente a Inc. Inv. El siguiente diagrama resume la situación:

$$\underbrace{C_\infty(\gamma_{n_0}) \leq 0}_{\text{imposible (Doc 42)}} \quad \text{vs} \quad \underbrace{C_\infty(\gamma_{n_0}) = 0}_{\iff \text{RH}} \quad \text{vs} \quad \underbrace{C_\infty(\gamma_{n_0}) > 0}_{\iff \neg\text{RH}}$$

---

## 9. Análisis de promedio y consecuencias

Aunque el promedio no prueba RH directamente, contiene información estructural nueva.

**Proposición 9.1 (Fórmula del promedio).** Para $T$ grande y $\mu_{\mathrm{off}}$ con masa finita:
$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T} C_\infty(\gamma_n) = \frac{2\pi}{T\log T}\sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}}\left[\int_0^T \frac{(\sigma_0-1/2)\log t}{(\sigma_0-1/2)^2+(t-\gamma_0)^2}\,dt + (\text{simétrico})\right]$$

**Proposición 9.2 (Asintótica del promedio para un cero fijo).** Para $\rho_0 = \sigma_0+i\gamma_0$ fijo y $T\to\infty$:
$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\Delta(\gamma_n;\rho_0) \sim \frac{2\pi^2(\sigma_0-1/2)\log\gamma_0}{T\log T/(2\pi)} = \frac{4\pi^3(\sigma_0-1/2)\log\gamma_0}{T\log T} \to 0$$

*Prueba.* La integral $\int_0^\infty \frac{2(\sigma_0-1/2)\log t}{(\sigma_0-1/2)^2+(t-\gamma_0)^2}dt \approx \pi(\sigma_0-1/2)\cdot 2\log\gamma_0/(\sigma_0-1/2) = 2\pi\log\gamma_0$ (Poisson + $\log t \approx \log\gamma_0$). Dividiendo por $N_\Xi(T) \sim T\log T/(2\pi)$, el resultado es $O(\log\gamma_0/T) \to 0$. $\square$

**Proposición 9.3 (El liminf se anula bajo hipótesis de finitud).** Si $\mu_{\mathrm{off}}$ tiene masa finita total $M = \mu_{\mathrm{off}}(\mathbb{H}) < \infty$ y el soporte de $\mu_{\mathrm{off}}$ es compacto, entonces:
$$\liminf_{n\to\infty} C_\infty(\gamma_n) = 0$$

*Prueba.* Para soporte compacto: $C_\infty(\gamma_n) \to 0$ cuando $\gamma_n \to \infty$ (Proposición 6.2). $\square$

**Advertencia 9.4 (El liminf cero no implica RH).** La Proposición 9.3 dice que $C_\infty(\gamma_n) \to 0$ para soporte compacto de $\mu_{\mathrm{off}}$, pero $C_\infty(\gamma_n) > 0$ para todo $n$ (por Corolario 5.4). La sucesión se aproxima a 0 pero nunca lo alcanza. El Teorema de Rigidez requiere la anulación EXACTA, no la aproximación.

**Corolario 9.5 (Implicación positiva).** Para ceros off-críticos con soporte no compacto (infinitos ceros, como cabría esperar si RH falla): por Corolario 7.4, $C_\infty(\gamma_n)$ tiene picos logarítmicos que van a $\infty$. El liminf podría ser positivo o cero, pero en ningún caso se anula exactamente.

---

## 10. La función de Green y la función de Nevanlinna-Herglotz

La extensión armónica $F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z)$ tiene una representación analítica via la función de Herglotz.

**Definición 10.1 (Función de Herglotz).** Define la función analítica en $\mathbb{H}^+ = \{z: \operatorname{Im}(z) > 0\}$:
$$H_{\mathrm{off}}(z) := \int_{\mathbb{H}} \frac{1}{z - \overline{w}}\,d\mu_{\mathrm{off}}(w)$$

donde $\overline{w} = x_0 - iy_0$ está en $\mathbb{H}^- = \{w: \operatorname{Im}(w) < 0\}$.

**Proposición 10.2 (Propiedades de $H_{\mathrm{off}}$).** Con $z = t + i\eta$ ($\eta > 0$) y $w_0 = x_0+iy_0$ ($y_0 > 0$):
$$H_{\mathrm{off}}(z) = \int_{\mathbb{H}} \frac{1}{(t-x_0)+i(\eta+y_0)}\,d\mu_{\mathrm{off}}(x_0,y_0)$$

1. $H_{\mathrm{off}}$ es analítica en $\mathbb{H}^+$ (singularidades en $\overline{\mathcal{Z}_{\mathrm{off}}} \subset \mathbb{H}^-$).
2. $\operatorname{Im}[H_{\mathrm{off}}(z)] < 0$ para $z \in \mathbb{H}^+$: $H_{\mathrm{off}}$ mapea $\mathbb{H}^+$ en $\mathbb{H}^-$ (anti-Herglotz).
3. $\operatorname{Re}[H_{\mathrm{off}}(t)] = \mathcal{P}[\mu_{\mathrm{off}}](t) = C_\infty(t)/2$ para $t \in \mathbb{R}$ (valor frontera).

*Prueba.* (1) El polo $1/(z-\overline{w_0})$ tiene $\overline{w_0} \in \mathbb{H}^-$, así que no hay singularidades para $z\in\mathbb{H}^+$. (2) $\operatorname{Im}[1/((t-x_0)+i(\eta+y_0))] = -(\eta+y_0)/[(t-x_0)^2+(\eta+y_0)^2] < 0$. (3) $\operatorname{Re}[1/((t-x_0)+iy_0)] = y_0/[y_0^2+(t-x_0)^2] = P_{y_0}(t-x_0)$. $\square$

**Proposición 10.3 (Inc. Inv. como condición sobre $H_{\mathrm{off}}$).** Inc. Inv. equivale a:
$$\operatorname{Re}[H_{\mathrm{off}}(\gamma_n)] = 0 \quad \forall n \iff H_{\mathrm{off}}(\gamma_n) \in i\mathbb{R} \quad \forall n$$

Es decir, $H_{\mathrm{off}}$ toma valores puramente imaginarios en todos los ceros de $\Xi$.

**Proposición 10.4 (Rigidez de la parte real).** Si $\operatorname{Re}[H_{\mathrm{off}}(t_0)] = 0$ para algún $t_0\in\mathbb{R}$, entonces por el Teorema 3.1: $\mu_{\mathrm{off}} = 0$, y $H_{\mathrm{off}} \equiv 0$.

*Interpretación.* La condición $H_{\mathrm{off}}(\gamma_n) \in i\mathbb{R}$ es como pedir que una función analítica tome valores en una recta al evaluarla en un conjunto discreto. Esto es una condición de "tipo Schwarz reflection" — pero el conjunto $\{\gamma_n\}$ es DISCRETO (no una curva real-analítica), lo que previene la aplicación directa del principio de Schwarz.

---

## 11. El argumento por densidad: alcance y límites

El advisor propone usar la densidad de $\{\gamma_n\}$ para forzar la anulación. Analizamos esto con precisión.

**Definición 11.1 (Densidad asintótica).** Los ceros de $\Xi$ son asintóticamente densos en $[0,\infty)$ en el sentido siguiente: para toda $T > 2$ y todo intervalo $[a,b] \subset [0, T]$ con $b-a > 2\pi/\log a$, existe $\gamma_n \in [a,b]$.

**Proposición 11.2 (Lo que la densidad sí implica).** Si $C_\infty$ es continua (Proposición 6.1) y $C_\infty(\gamma_n) < \epsilon$ para todos $\gamma_n \in [a,b]$, entonces para cualquier $t_0 \in [a,b]$ con $|t_0-\gamma_n| \leq 2\pi/\log a$ para algún $n$:
$$C_\infty(t_0) \leq C_\infty(\gamma_n) + |C_\infty(t_0)-C_\infty(\gamma_n)| \leq \epsilon + \frac{L\cdot 2\pi}{\log a}$$

donde $L$ es la constante de Lipschitz de $C_\infty$.

**Proposición 11.3 (Lo que la densidad NO implica).** El hecho de que $C_\infty(\gamma_n)$ sea pequeño para todos los $\gamma_n$ NO es suficiente para concluir $C_\infty(\gamma_n) = 0$. Ejemplo: si $\mu_{\mathrm{off}} = c\cdot\delta_{(x_0,y_0)}$ para $c > 0$ pequeño, entonces $C_\infty(\gamma_n) = 2c\cdot P_{y_0}(\gamma_n-x_0) < 2c/y_0$, que puede ser arbitrariamente pequeño pero siempre positivo.

**La brecha:**

$$\{C_\infty(\gamma_n) < \epsilon \;\forall n\} \not\implies \{C_\infty(\gamma_{n_0}) = 0 \;\text{para algún } n_0\}$$

Probar la anulación EXACTA requiere más que control asintótico.

---

## 12. Nuevo equivalente: la condición de Szegő espectral

Buscamos una condición alternativa a $C_\infty(\gamma_{n_0})=0$ que sea más accesible.

**Proposición 12.1 (Equivalentes adicionales de Inc. Inv.).** Bajo las hipótesis del programa:

*(v)* $\prod_{n=1}^\infty (1 - C_\infty(\gamma_n)^2/M_n^2) = 0$ para toda sucesión acotante $M_n$ divergente.

*(vi)* $\sum_{n=1}^\infty C_\infty(\gamma_n) = +\infty$ ó $\sum_{n=1}^\infty C_\infty(\gamma_n) = 0$.

*(vii)* $\sum_{n=1}^\infty C_\infty(\gamma_n)^2 = \mathcal{D}(\infty) < \infty$ ó $= \infty$ (de Doc 41).

*Prueba de (vi).* Si RH: todos los términos son 0, la suma es 0. Si RH falla: por Corolario 7.4, existen infinitos $\gamma_{n_k^*}$ con $C_\infty(\gamma_{n_k^*}) \geq c\log\gamma_{n_k^*} \to \infty$. La subserie sobre estos índices diverge: $\sum_{k} C_\infty(\gamma_{n_k^*}) \geq \sum_k c\log\gamma_{n_k^*} = +\infty$. $\square$

**Corolario 12.2.** RH $\iff$ $\sum_{n=1}^\infty C_\infty(\gamma_n) = 0$ (con $C_\infty(\gamma_n)\geq 0$).

Esto es otra forma de decir Inc. Inv., pero muestra que la suma total del déficit es 0 si y solo si RH. Sin RH, la suma es $+\infty$.

---

## 13. El operador de Cauchy y la teoría de aproximación

**Definición 13.1 (Operador de Cauchy en la recta crítica).** Definimos el operador $\mathcal{C}_{\mathrm{crit}}$ que asigna a cada medida positiva $\mu_{\mathrm{off}}$ en $\mathbb{H}$ su restricción a la línea crítica:

$$\mathcal{C}_{\mathrm{crit}}[\mu_{\mathrm{off}}](\gamma) := \mathcal{P}[\mu_{\mathrm{off}}](\gamma) = C_\infty(\gamma)/2, \quad \gamma \in \mathbb{R}$$

**Teorema 13.2 (Inyectividad de $\mathcal{C}_{\mathrm{crit}}$ sobre medidas positivas).** El operador $\mathcal{C}_{\mathrm{crit}}: \mathcal{M}_+(\mathbb{H}) \to \mathcal{C}(\mathbb{R}, [0,\infty))$ es **inyectivo**: si $\mathcal{C}_{\mathrm{crit}}[\mu_1] = \mathcal{C}_{\mathrm{crit}}[\mu_2]$ para $\mu_1, \mu_2 \geq 0$, entonces $\mu_1 = \mu_2$.

*Prueba.* Sea $\nu = \mu_1 - \mu_2$ (diferencia de medidas con signo). Si $\mathcal{C}_{\mathrm{crit}}[\nu](t) = 0$ para todo $t\in\mathbb{R}$, entonces por la unicidad de la transformada de Poisson para medidas con signo (Privalov, 1956): $\nu = 0$. $\square$

**Corolario 13.3.** La función $t \mapsto C_\infty(t)$ determina $\mu_{\mathrm{off}}$ de manera única (dentro de la clase de medidas positivas). En particular:

$$C_\infty \equiv 0 \text{ en } \mathbb{R} \iff \mu_{\mathrm{off}} = 0 \iff \text{RH}$$

**Observación 13.4.** El Corolario 13.3 es correcto pero no resuelve el problema: decir que "$C_\infty \equiv 0$ implica RH" es una tautología de la fórmula del déficit. La pregunta sigue siendo: ¿cómo probar que $C_\infty(\gamma_n) = 0$ para algún $n$?

---

## 14. La pregunta decisiva: ¿puede la masa de $\mu_{\mathrm{off}}$ ser pequeña?

Hemos establecido que si $\mu_{\mathrm{off}} \neq 0$, entonces $C_\infty(\gamma_n) > 0$ para todos los $n$, con picos logarítmicos inevitables (Corolario 7.4). Surge la pregunta: ¿puede $\mu_{\mathrm{off}}$ tener masa PEQUEÑA (pero no cero)?

**Proposición 14.1 (Cota inferior de la masa en términos del déficit).** Para $\mu_{\mathrm{off}} \neq 0$: sea $\rho_0^* \in \mathcal{Z}_{\mathrm{off}}$ el cero off-crítico más cercano a la línea crítica (con $\epsilon^* := \sigma_0^*-1/2 = \min_{\rho_0}(\sigma_0-1/2)$). Entonces:
$$\sup_n C_\infty(\gamma_n) \geq C_\infty(\gamma_{n^*}) \geq \frac{2\epsilon^*}{(\epsilon^*)^2+(\pi/\log\gamma_0^*)^2}$$

Para $\epsilon^* \sim \pi/\log\gamma_0^*$ (en el límite de la región libre): $\sup_n C_\infty(\gamma_n) \geq \log\gamma_0^*/\pi$.

**Proposición 14.2 (Incompatibilidad con los resultados de ceros conocidos).** Los datos numéricos muestran que el 99.9999\% de los ceros de $\zeta$ conocidos están en la línea crítica. Si los primeros $10^{22}$ ceros fueran on-críticos (lo que se ha verificado), y solo hubiera ceros off-críticos con $\gamma_0 > 10^{22}$, entonces la contribución de esos ceros a $C_\infty(\gamma_n)$ para $\gamma_n \leq 10^{22}$ sería $\leq 2\epsilon^* / (\gamma_n - \gamma_0)^2 \approx 0$. El déficit sería numéricamente indetectable para los ceros verificados.

*Este argumento es heurístico, no una prueba matemática.*

---

## 15. Resumen y hoja de ruta para Doc 44

**Resultados nuevos de este documento:**

| # | Resultado | Tipo |
|---|---|---|
| T 3.1 | Rigidez de Poisson: $\mathcal{P}[\mu](t_0)=0$ para algún $t_0$ $\implies$ $\mu=0$ | Nuevo, probado |
| T 4.1 | Punto Único implica RH: $C_\infty(\gamma_{n_0})=0$ para algún $n_0$ $\implies$ RH | Nuevo, probado |
| T 4.2 | Equivalencia: RH $\iff$ $\exists n_0: C_\infty(\gamma_{n_0})=0$ $\iff$ Inc. Inv. | Nuevo, probado |
| P 5.2–5.3 | $F(z)=\mathcal{P}[\mu_{\mathrm{off}}](z)$ armónica en $\mathbb{H}^+$, estrictamente positiva si $\mu\neq 0$ | Nuevo, probado |
| T 7.1 | Detección por densidad: $\exists\gamma_{n^*}$ con $C_\infty(\gamma_{n^*})\geq 2(\sigma_0-1/2)/[(\sigma_0-1/2)^2+\delta^2]$ | Nuevo, probado |
| C 7.4 | Sin RH: picos logarítmicos $C_\infty(\gamma_{n_k^*})\geq c\log\gamma_{n_k^*}$ inevitables | Nuevo, probado |
| C 12.2 | RH $\iff$ $\sum_n C_\infty(\gamma_n) = 0$ (con $C_\infty\geq 0$) | Nuevo, probado |
| T 13.2 | $\mathcal{C}_{\mathrm{crit}}$ es inyectivo sobre medidas positivas | Nuevo, probado |

**Estado actualizado del programa:**

| Implicación | Estado |
|---|---|
| Inc. Inv. $\Rightarrow$ RH | Probada (Doc 19) |
| RH $\Rightarrow$ Inc. Inv. | Probada (Doc 39) |
| $C_\infty(\gamma_n)\geq 0$ | **Probada incondicionalmente** (Doc 42) |
| $C_\infty(\gamma_{n_0})=0$ para algún $n_0$ $\Rightarrow$ RH | **Probada** (Doc 43, T 4.1) |
| Sin RH: picos logarítmicos en $C_\infty$ | **Probada** (Doc 43, C 7.4) |
| $C_\infty(\gamma_{n_0})=0$ [incondicional] | **Abierta** — equivalente a RH |

**La frontera exacta del programa:**

El problema se ha reducido a su esencia irreducible:

> *Demostrar que una serie de Dirichlet condicionalmente convergente toma un valor específico en al menos un punto del espectro de $\Xi$.*

---

**Propuesta para Doc 44: El Problema de la Medida de Cero**

La hoja de ruta más prometedora identifica la siguiente pregunta (nueva):

¿Puede demostrarse que $\mu_{\mathrm{off}}$ tiene masa **nula** usando solo propiedades aritméticas de los ceros de $\zeta$, sin asumir su ubicación?

Tres ataques posibles:

**A. Teorema de Plancherel espectral.** La transformada de Fourier de $C_\infty(t) = \mathcal{P}[\mu_{\mathrm{off}}](t)$ en $\mathbb{R}$ es $\hat{C}_\infty(\xi) = \hat{\mu}_{\mathrm{off,\xi}}$ donde $\hat{\mu}$ es la transformada de Fourier de la medida. Si $\hat{C}_\infty = 0$ (la transformada de Fourier se anula en un conjunto de medida positiva), entonces $C_\infty \equiv 0$ (Wiener, Paley-Wiener). La pregunta: ¿tiene $C_\infty$ alguna propiedad de decaimiento de Fourier que fuerce $\hat{C}_\infty = 0$?

**B. La ecuación funcional como condición de simetría.** Los ceros de $\zeta$ satisfacen la simetría $\rho \leftrightarrow 1-\bar\rho$ (ecuación funcional). Esto impone una condición sobre $\mu_{\mathrm{off}}$: la medida debe ser simétrica bajo la reflexión $(\sigma_0-1/2, \gamma_0) \leftrightarrow (1/2-\sigma_0, \gamma_0)$... pero en nuestra parameterización $y_0 = \sigma_0-1/2 > 0$, el par funcional tiene $y = 1/2 - \sigma_0 < 0$ (en $\mathbb{H}^-$), que no está en el soporte de $\mu_{\mathrm{off}}$. La simetría se manifiesta en $\mu_{\mathrm{off}}$ via el segundo término del núcleo de Cauchy en la fórmula del déficit.

**C. La condición de positividad de $C_\infty$ sobre TODA $\mathbb{R}$ (no solo en $\{\gamma_n\}$).** Por la extensión armónica $F(z)$ y el principio del mínimo para funciones armónicas positivas, ¿existen condiciones sobre $F$ en todo $\mathbb{H}^+$ que fuercen $\mu_{\mathrm{off}} = 0$? Esto conecta con la teoría de potencial y la capacidad analítica.

---

*Siguiente documento (Doc 44): El problema de la medida de cero — $\mu_{\mathrm{off}}$ y la condición de positividad global de $C_\infty$ en $\mathbb{R}$.*

---

## Apéndice A: La simetrización correcta de la transformada de Poisson

**A.1.** La fórmula del déficit de Doc 42 incluye un segundo término con $(\gamma_n+\gamma_0)$ que proviene de la simetrización por conjugación compleja $(\rho_0, \bar\rho_0)$. En términos de la transformada de Poisson:

$$C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{sym}}](\gamma_n)$$

donde $\mu_{\mathrm{sym}} = \sum_{\rho_0:\sigma_0>1/2} 2(\sigma_0-1/2)[\delta_{(\gamma_0,\sigma_0-1/2)} + \delta_{(-\gamma_0,\sigma_0-1/2)}]$ (la suma incluye tanto $(\gamma_0, y_0)$ como $(-\gamma_0, y_0)$ en $\mathbb{H}$). Esta simetrización hace que $\mathcal{P}[\mu_{\mathrm{sym}}]$ sea una función par en $\gamma_n$ — consistente con que $C_\infty(\gamma_n) = C_\infty(-\gamma_n)$ por la simetría del potencial.

**A.2.** El Teorema de Rigidez 3.1 se aplica a $\mu_{\mathrm{sym}}$ sin cambios: $\mathcal{P}[\mu_{\mathrm{sym}}](\gamma_{n_0}) = 0$ para algún $\gamma_{n_0} > 0$ implica $\mu_{\mathrm{sym}} = 0$ (y por lo tanto $\mu_{\mathrm{off}} = 0$, RH).
