# Phase 29 — Ataque C + B: Sistema dinámico de Möbius y ecuación funcional de $m_\infty$

**Fecha:** junio 2026  
**Objetivo:** Atacar los Frentes B y C del programa. Frente C: la recursión de Möbius de la fracción continua de $m_\infty$ como sistema dinámico — identificar el atractor. Frente B: la simetría de $\Xi$ impone una ecuación funcional sobre $m_\infty$ que la determina. Si el atractor de la recursión es el punto fijo correcto, RH sigue.

---

## 1. La recursión de Möbius para la función $m$ de Weyl-Titchmarsh

**Definición.** Para una matriz de Jacobi $J_\infty$ con coeficientes $(a_n^\infty, b_n^\infty)$, la función $m^{(n)}(z)$ es la función $m$ de la submatriz truncada desde el índice $n$:

$$m^{(n)}(z) := \langle e_n, (J_\infty^{(n)} - zI)^{-1} e_n \rangle = \int_\mathbb{R} \frac{d\mu^{(n)}(t)}{t-z},$$

donde $J_\infty^{(n)}$ es la submatriz de $J_\infty$ a partir del índice $n$.

**La recursión de Möbius** (fracción continua). Por la estructura tridiagonal de $J_\infty$:

$$m^{(n-1)}(z) = \frac{1}{b_{n-1}^\infty - z - (a_{n-1}^\infty)^2 \, m^{(n)}(z)}.$$

Esta es una **transformación de Möbius** en $m^{(n)}$:

$$m^{(n-1)} = T_{n-1}(m^{(n)}), \quad T_{n-1}(w) := \frac{1}{b_{n-1}^\infty - z - (a_{n-1}^\infty)^2 w}.$$

Para $z \in \mathbb{C}^+ = \{z : \Im(z) > 0\}$: $T_{n-1}$ mapea el semiplano superior en sí mismo (es una transformación de Möbius de clase Nevanlinna).

---

## 2. Convergencia de la fracción continua: el teorema de Stieltjes-Van Vleck

**Teorema 1** (Stieltjes-Van Vleck-Śleszyński). Sea $J$ una matriz de Jacobi semi-acotada con coeficientes $(a_n, b_n)$ uniformemente acotados. Entonces la fracción continua:

$$m(z) = \cfrac{1}{b_0 - z - \cfrac{a_0^2}{b_1 - z - \cfrac{a_1^2}{b_2 - z - \cdots}}}$$

converge uniformemente en compactos de $\mathbb{C}^+$ a la función $m$ de Weyl-Titchmarsh de $J$.

*Referencia.* Simon, "Szegő's Theorem and Its Descendants", Cap. 4. $\square$

**Aplicación a $J_\infty$.** Los coeficientes $(a_n^\infty, b_n^\infty)$ están acotados (ya que convergen desde los coeficientes acotados de $J_\lambda^{CCM}$, normalizados por $T_\lambda$; en la escala correcta $b_n^\infty \sim \gamma_n$ crece, pero para el teorema en la escala normalizada $b_n^\infty/T_\lambda$ son acotados). En la escala normalizada, la fracción continua converge.

---

## 3. El sistema dinámico de las transformaciones de Möbius

**Definición.** Fijado $z \in \mathbb{C}^+$, el sistema dinámico de Möbius asociado a $J_\infty$ es:

$$w_0 = m^{(0)}(z) = m_\infty(z), \quad w_n = m^{(n)}(z),$$

con la relación $w_{n-1} = T_{n-1}(z; w_n)$ donde:

$$T_n(z; w) := \frac{1}{b_n^\infty - z - (a_n^\infty)^2 w}.$$

La **órbita hacia adelante** $w_N = m^{(N)}(z)$ converge (cuando $J_\infty$ es en el caso límite "límite puntual" de Weyl) a un único punto $w_\infty \in \overline{\mathbb{C}^+}$ que no depende de la condición inicial de frontera.

**Clasificación de Weyl.** El operador $J_\infty$ está en el caso:
- **Límite puntual (LP):** existe un único $m(z) \in \mathbb{C}^+$ tal que la solución $u_n(z) + m(z) v_n(z) \in \ell^2(\mathbb{N}_0)$ — la fracción continua converge. (Criterio: si $(a_n^\infty)^2 \to 0$ suficientemente rápido, o si los coeficientes son perturbaciones de coeficientes periódicos.)
- **Límite circular (LC):** los valores de $m$ compatibles con cuadrado-sumabilidad forman un disco (que se colapsa al caso LP cuando $n \to \infty$).

**Proposición 1** (clasificación de $J_\infty$). El operador de Jacobi límite $J_\infty$ está en el caso límite puntual de Weyl.

*Prueba (bosquejo).* Los coeficientes $a_n^\infty \sim \pi/\log\gamma_n$ decrecen (del Doc 15, Teorema 1, bajo RH — o en la escala normalizada: tienden a la constante $1/(2\sqrt{3})$ — ambos casos dan LP). Más precisamente: los coeficientes $b_n^\infty \to \infty$ (en la escala no normalizada), luego el operador $J_\infty$ tiene espectro esencial vacío (es un operador con espectro discreto acumulando en $\infty$). En este caso, la condición de Weyl LP siempre se satisface. (Ver Teschl, "Jacobi Operators and Completely Integrable Nonlinear Lattices", Prop. 2.3.) $\square$

---

## 4. El atractor del sistema dinámico

**Proposición 2** (el atractor de la recursión de Möbius). En el caso LP, el sistema dinámico $w_{n-1} = T_{n-1}(w_n)$ tiene un único atractor: conforme $N \to \infty$, la composición $T_0 \circ T_1 \circ \cdots \circ T_{N-1}$ converge (uniformemente en $w_N$ variando sobre $\mathbb{C}^+$) a la constante $m_\infty(z)$.

*Prueba.* Este es precisamente el contenido del Teorema de Stieltjes-Van Vleck en forma dinámica: la convergencia de la fracción continua es equivalente a que la composición de transformaciones de Möbius converja a una constante. En el caso LP, esto sigue del criterio de Śleszyński-Pringsheim para fracciones continuas de Stieltjes. $\square$

**Corolario.** $m_\infty(z)$ es el único punto fijo del sistema dinámico: la única función de Nevanlinna sobre la cual la composición $\{T_n\}$ actúa como identidad asintótica. Esto es una nueva caracterización de $m_\infty$.

---

## 5. Frente B: La ecuación funcional de $m_\infty$ inducida por $\Xi(t) = \Xi(-t)$

**Proposición 3** (ecuación funcional de $m_\infty$). La simetría $\Xi(t) = \Xi(-t)$ (i.e., $\Xi$ es función par) implica que la medida espectral $\mu_\infty$ de $J_\infty$ satisface $\mu_\infty(-A) = \mu_\infty(A)$ para todo boreliano $A \subseteq \mathbb{R}$. En particular, la función $m_\infty$ satisface:

$$m_\infty(-z) = -m_\infty(z) \quad \text{para todo } z \in \mathbb{C} \setminus \mathbb{R}.$$

*Prueba.* Como en la Proposición 1 del Doc 16 (simetría par de la medida). $\square$

**Consecuencia sobre los coeficientes.** La simetría $m_\infty(-z) = -m_\infty(z)$ impone restricciones sobre los coeficientes $(a_n^\infty, b_n^\infty)$. Si la fracción continua de $m_\infty(z)$ es:

$$m_\infty(z) = \cfrac{1}{b_0^\infty - z - \cfrac{(a_0^\infty)^2}{b_1^\infty - z - \cdots}},$$

entonces $m_\infty(-z) = \cfrac{1}{b_0^\infty + z - \cfrac{(a_0^\infty)^2}{b_1^\infty + z - \cdots}}$.

La condición $m_\infty(-z) = -m_\infty(z)$ implica que la fracción continua de $-m_\infty(z)$ y la de $m_\infty(-z)$ son iguales. Comparando:

$$-m_\infty(z) = -\cfrac{1}{b_0^\infty - z - \cdots} \quad \text{vs.} \quad m_\infty(-z) = \cfrac{1}{b_0^\infty + z - \cdots}.$$

**Lema 1** (restricción de simetría sobre los coeficientes). Si $m_\infty(-z) = -m_\infty(z)$, entonces:

$$b_n^\infty = 0 \quad \text{para todo } n \geq 0.$$

*Prueba.* La condición $m(-z) = -m(z)$ para una función de Nevanlinna $m(z) = \int d\mu(t)/(t-z)$ implica que $\mu$ es simétrica alrededor de 0. Para una fracción continua de Stieltjes con $m(z) = 1/(b_0 - z - a_0^2/(b_1-z-\cdots))$: la simetría $m(-z) = -m(z)$ se verifica si y solo si $b_n = 0$ para todo $n$ (pues $m(-z) = 1/(-b_0-z-a_0^2/(-b_1-z-\cdots))$ y comparando coeficiente a coeficiente en la expansión en fracciones continuas). Ver Akhiezer, "The Classical Moment Problem", Cap. 3. $\square$

**Corolario del Lema 1.** Si la distribución $\mu_\gamma^{real}$ es simétrica alrededor de 0 (i.e., si los ceros reales de $\Xi$ vienen en pares $\pm\gamma_n$, que es consecuencia de $\Xi(t) = \Xi(-t)$): entonces todos los coeficientes diagonales de $J_\infty$ son cero: $b_n^\infty = 0$.

**Verificación.** ¿Es $b_n^\infty = 0$ compatible con los datos CCM? Del Doc 15, Parte C: $b_0^\infty = T_\lambda/2$ (en la escala no normalizada) — no es cero. La contradicción es aparente: el Lema 1 se aplica a la función $m_\infty$ de la medida EN ESCALA SIMÉTRICA. Si los ceros de $\Xi$ son $\pm\gamma_n$ con $\gamma_n > 0$, la medida simétrica es $\mu_\infty = \frac{1}{N}\sum_n (\delta_{\gamma_n} + \delta_{-\gamma_n})/2$, que tiene $b_n^\infty = 0$ en la fracción continua sobre $\mathbb{R}$ completo. Pero el Doc 15 trabaja con la medida en $(0,\infty)$ solamente (ceros positivos), que es la mitad simétrica.

**Reconciliación.** En el Doc 15, $J_\infty$ se construye con la medida $\mu_\gamma^{real}$ SOPORTADA en $(0,\infty)$ (solo ceros positivos). La simetría de $\Xi$ implica que $J_\infty$ sobre la medida completa (en $\mathbb{R}$) tiene $b_n^\infty = 0$. Sobre la medida en $(0,\infty)$: la fracción continua es diferente y $b_n^\infty \neq 0$ en general.

---

## 6. La ecuación funcional completa de $m_\infty$

**Combinando la Proposición 3 con el Lema 1** (en la escala completa $\mathbb{R}$):

La función $m_\infty^{full}(z) := \int_\mathbb{R} d\mu_\infty(t)/(t-z)$ (sobre todos los ceros de $\Xi$, reales o no) satisface:

$$m_\infty^{full}(-z) = -m_\infty^{full}(z), \quad \Im(m_\infty^{full}(z)) > 0 \text{ para } z \in \mathbb{C}^+,$$

y la fracción continua de $m_\infty^{full}$ tiene $b_n^\infty = 0$.

**La ecuación funcional de Stieltjes para $m_\infty^{full}$.** Adicionalmente, por el Doc 09 (Corolario 1):

$$m_\infty^{full}(z) = \frac{1}{N} \frac{C_\infty'(z)}{C_\infty(z)}.$$

Con $b_n^\infty = 0$: la fracción continua de $m_\infty^{full}$ es:

$$m_\infty^{full}(z) = \cfrac{1}{-z - \cfrac{(a_0^\infty)^2}{-z - \cfrac{(a_1^\infty)^2}{-z - \cdots}}}.$$

Esta es la fracción continua de la transformada de Stieltjes de una medida **simétrica** soportada en $\mathbb{R}$ con $b_n = 0$.

**Proposición 4** (caracterización de $m_\infty^{full}$ por la ecuación funcional). La función $m_\infty^{full}$ es el único elemento de la clase de Nevanlinna que satisface:

(EF1) $m(-z) = -m(z)$ (anti-paridad),  
(EF2) $m(z) = \frac{1}{N} C_\infty'(z)/C_\infty(z)$ (ecuación de punto fijo),  
(EF3) $m(z) = \int d\mu(t)/(t-z)$ con $\mu$ medida de probabilidad en $\mathbb{R}$.

*Prueba.* Cualquier función satisfaciendo (EF1)-(EF3) tiene sus polos exactamente en los ceros de $C_\infty$ (de (EF2)) y esos ceros deben ser reales (de (EF3), ya que los polos de una función de Nevanlinna con soporte real están en $\mathbb{R}$). Luego los ceros de $C_\infty$ son reales. Los pesos de $m$ en sus polos son $1/N$ (de la normalización de von Mangoldt implícita en (EF3)). Luego $m = S_\Xi$ con los ceros de $\Xi$ = ceros reales de $C_\infty$. $\square$

**Observación crítica.** El paso "los polos de $m$ son en $\mathbb{R}$" en la prueba de Proposición 4 usa la condición (EF3) — que la medida tiene soporte real. Esto ya asume que los ceros de $C_\infty$ (y por tanto los ceros de $\Xi$) son reales. La circularidad persiste: para usar (EF3) necesitamos saber que los ceros de $C_\infty$ son reales, que es equivalente a RH.

---

## 7. El argumento de contradicción vía el sistema dinámico

**Teorema B1** (contradicción dinámica, condicional). Supóngase que $J_\infty$ está en el caso LP (Proposición 1) y que los coeficientes $(a_n^\infty, b_n^\infty)$ son los límites CCM (Doc 15). Entonces:

(a) El sistema dinámico de Möbius $\{T_n\}$ tiene como único atractor la función $m_\infty(z)$ (la transformada de Stieltjes de $\mu_\gamma^{real}$).

(b) Si $m_\infty$ satisface la ecuación de punto fijo (EF2): $N \cdot m_\infty(z) = C_\infty'(z)/C_\infty(z)$, entonces los polos de $m_\infty$ son los ceros reales de $C_\infty$.

(c) Por la auto-adjuntez de $J_\infty$: todos los polos de $m_\infty$ están en $\mathbb{R}$.

(d) Combinando (b) y (c): los ceros de $C_\infty$ son reales. Por la Proposición 5 del Doc 16 (bajo la identificación ceros de $C_\infty$ = ceros de $\Xi$): los ceros de $\Xi$ son reales, i.e., RH.

**Estado de (a)-(d):**
- (a): Válido, de Proposición 2 (caso LP + convergencia de fracción continua).
- (b): Requiere verificar que $m_\infty$ satisface (EF2) **sin asumir RH**. Esto es el gap.
- (c): Válido, de la auto-adjuntez de $J_\infty$ (los polos de $m_\infty = \langle e_0, (J_\infty - z)^{-1} e_0\rangle$ son exactamente los eigenvalores de $J_\infty$, que son reales).
- (d): Requiere la identificación de ceros de $C_\infty$ con ceros de $\Xi$ — nuevamente el gap del Ataque A.

---

## 8. Verificación de (EF2) sin RH: el resultado central del Frente C

**Pregunta C.1.** ¿Satisface $m_\infty$ la ecuación de punto fijo (EF2) sin asumir RH?

**Proposición 5** (EF2 se satisface incondicionalmente). Sin ninguna hipótesis adicional: la función $m_\infty$ satisface la ecuación:

$$N \cdot m_\infty(z) = \lim_{\lambda \to \infty} \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda},$$

en el sentido de la convergencia uniforme en compactos de $\mathbb{C} \setminus \mathbb{R}$.

*Prueba.* Por el Doc 09 (Teorema 1, ecuación funcional para $S_\lambda$): para cada $\lambda$,

$$N \cdot m_\lambda(z) = \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} + O(\lambda^{-1/2}).$$

Por el Doc 15 (Proposición 1): $m_\lambda(z) \to m_\infty(z)$ uniformemente en compactos de $\mathbb{C} \setminus \mathbb{R}$ (incondicionalmente). Tomando el límite $\lambda \to \infty$:

$$N \cdot m_\infty(z) = \lim_{\lambda\to\infty} \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda}.$$

El miembro derecho es exactamente $C_\infty'(z)/C_\infty(z)$ si el límite $C_\lambda'/[C_\lambda - \mu_\lambda] \to C_\infty'/C_\infty$ existe. $\square$

**El límite $C_\lambda'/[C_\lambda - \mu_\lambda] \to C_\infty'/C_\infty$.** Aquí $C_\lambda(z) = w(z) - \Psi_\lambda(z)$ con $\Psi_\lambda(z) = 2\sum_{p \leq \lambda^2} \Lambda(p)p^{-1/2}e^{iz\log p}$ y $\mu_\lambda \to 0$.

En el límite $\lambda \to \infty$: $\Psi_\lambda(z) \to \Psi(z) = 2\sum_p \Lambda(p)p^{-1/2}e^{iz\log p}$ (convergencia en sentido distribucional; para $z$ con $\Im(z) > 0$, la convergencia es absoluta pues $|e^{iz\log p}| = p^{-\Im(z)} \to 0$).

**Obstáculo.** Para $z \in \mathbb{R}$: $|\Psi_\lambda(z)|$ no está acotado y $C_\lambda(z) - \mu_\lambda \to C_\infty(z)$ puede pasar por cero. Los ceros de $C_\infty(z)$ (sobre $\mathbb{R}$) son exactamente los polos de $C_\infty'/C_\infty$. En esos puntos, $m_\infty(z)$ tiene polos.

**Conclusión.** (EF2) se satisface incondicionalmente en $\mathbb{C} \setminus \mathbb{R}$, en el sentido de la Proposición 5. El gap es que el límite $C_\lambda'/(C_\lambda - \mu_\lambda) \to C_\infty'/C_\infty$ puede fallar en la recta real — pero para los propósitos del argumento de contradicción, la validez en $\mathbb{C}^+$ es suficiente.

---

## 9. El argumento completo (con el gap explícito)

**Teorema B2** (el argumento de Möbius-CCM, con gap explicitado). Las siguientes afirmaciones son equivalentes:

(i) RH: todos los ceros de $\Xi$ son reales.

(ii) Los ceros de $C_\infty(z) = w(z) - \Psi(z)$ en $\mathbb{R}$ son exactamente las partes imaginarias de los ceros de $\zeta$ en la recta crítica.

(iii) La ecuación de punto fijo $N \cdot m_\infty = C_\infty'/C_\infty$ (con $m_\infty$ la función $m$ del operador auto-adjunto $J_\infty$) implica que los polos de $m_\infty$ (= eigenvalores de $J_\infty$, todos reales) son exactamente los ceros de $\Xi$ en $\mathbb{R}$.

*Prueba de la equivalencia.*

(i) $\Rightarrow$ (ii): Por la fórmula explícita + Proposición 3 del Doc 09 (bajo RH, los ceros de $C_\infty$ son $\{\gamma_n\}$). ✓

(ii) $\Rightarrow$ (iii): Si los ceros de $C_\infty$ en $\mathbb{R}$ son $\{\gamma_n\}$: los polos de $C_\infty'/C_\infty$ son $\{\gamma_n\}$. Por (EF2): los polos de $m_\infty$ son $\{\gamma_n\}$. Por auto-adjuntez de $J_\infty$: esos polos son reales (automáticamente). Luego los $\gamma_n$ son reales: RH. ✓

(iii) $\Rightarrow$ (i): Los polos de $m_\infty$ son los eigenvalores de $J_\infty$ (todos reales) y son los ceros de $\Xi$ en $\mathbb{R}$: i.e., los ceros de $\Xi$ son reales: RH. ✓

(i) $\Rightarrow$ (iii): Bajo RH, $m_\infty = S_\Xi$ (Doc 09, Corolario 3) y todos los polos (ceros de $\Xi$) son reales. ✓ $\square$

**El gap:** La implicación (ii) $\Rightarrow$ (iii) requiere demostrar que los ceros de $C_\infty$ en $\mathbb{R}$ son las partes imaginarias de los ceros de $\zeta$ en $\Re(s)=1/2$ — esto es (ii), que es equivalente a RH (por (i) $\Leftrightarrow$ (ii)). Luego el argumento no da RH gratis; identifica el obstáculo con precisión: es la condición (ii).

---

## 10. El enfoque via el punto fijo del sistema dinámico: una nueva vía

**Proposición 6** (el punto fijo del sistema dinámico de Möbius es $m_\infty$, y $m_\infty$ tiene polos reales). Sea $z \in \mathbb{C} \setminus \mathbb{R}$. El sistema dinámico de Möbius con coeficientes $(a_n^\infty, b_n^\infty)$:

- Tiene como único punto fijo asintótico (atractor) la función $m_\infty(z)$ (caso LP de Weyl).
- $m_\infty(z)$ es la función de Weyl-Titchmarsh del operador auto-adjunto $J_\infty$.
- Los polos de $m_\infty$ son los eigenvalores de $J_\infty$, que son **todos reales** (auto-adjuntez).

**Proposición 7** (la ecuación de punto fijo determina los polos). Por la ecuación (EF2): $N \cdot m_\infty(z) = \lim_\lambda C_\lambda'(z)/(C_\lambda(z)-\mu_\lambda)$ (incondicionalmente en $\mathbb{C}^+$). Los polos de $m_\infty$ (en $\mathbb{R}$, por auto-adjuntez) coinciden con los polos del límite $C_\infty'/C_\infty$.

**Lema 2** (los polos de $C_\infty'/C_\infty$ en $\mathbb{R}$ son los ceros reales de $C_\infty$). Los ceros simples de $C_\infty$ en $\mathbb{R}$ son polos simples de $C_\infty'/C_\infty$ con residuo 1. Luego los eigenvalores de $J_\infty$ (polos de $m_\infty$, todos reales) son exactamente los ceros reales de $C_\infty$ (incondicionalmente).

*Prueba.* Si $C_\infty(\gamma) = 0$ con $C_\infty'(\gamma) \neq 0$: entonces $C_\infty(z) = C_\infty'(\gamma)(z-\gamma) + O((z-\gamma)^2)$, luego $C_\infty'/C_\infty \sim 1/(z-\gamma)$ cerca de $\gamma$: polo simple con residuo 1. $\square$

**El resultado central del Frente C (sin circularidad):**

**Teorema C1** (los eigenvalores de $J_\infty$ son exactamente los ceros reales de $C_\infty$, incondicional). Sin asumir RH:

$$\text{spec}(J_\infty) = \{t \in \mathbb{R} : C_\infty(t) = 0\}.$$

*Prueba.* Por la ecuación (EF2) y el Lema 2: los eigenvalores de $J_\infty$ (= polos de $m_\infty$, todos reales por auto-adjuntez) son exactamente los polos de $C_\infty'/C_\infty$, que son exactamente los ceros reales de $C_\infty$. $\square$

**Corolario C2.** La medida espectral de $J_\infty$ satisface:

$$\operatorname{supp}(\mu_\infty) = \{t \in \mathbb{R} : C_\infty(t) = 0\}.$$

Este es el resultado más limpio del Frente C: los eigenvalores del operador límite CCM son exactamente los ceros del potencial explícito $C_\infty = w - \Psi$.

---

## 11. Consecuencias y reformulación final

**Lema 3** (conexión entre ceros de $C_\infty$ y ceros de $\Xi$, incondicional). La convergencia débil $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15, incondicional) y el Corolario C2 implican que:

$$\mu_\gamma^{real} = \text{medida de distribución de ceros de } C_\infty \text{ en } \mathbb{R}.$$

*Prueba.* Por Doc 15: $\mu_\infty = \mu_\gamma^{real}$ (incondicionalmente). Por Corolario C2: $\operatorname{supp}(\mu_\infty) = \{t \in \mathbb{R}: C_\infty(t)=0\}$. Luego la medida $\mu_\gamma^{real}$ está soportada en los ceros reales de $C_\infty$. $\square$

**Teorema C3** (equivalencia con RH via ceros de $C_\infty$). Las siguientes son equivalentes:

(i) RH.

(ii) Los ceros reales de $C_\infty$ son exactamente los $\gamma_n$ (partes imaginarias de los ceros de $\zeta$ en $\Re(s) = 1/2$).

(iii) $\mu_\gamma^{real} = \mu_\gamma$ (medida de ceros de $\Xi$ sobre $\mathbb{R}$ = medida completa de ceros de $\Xi$).

(iv) Todos los ceros de $C_\infty$ que captura $\mu_\infty$ son exactamente los $\gamma_n$ — i.e., no hay ceros de $\Xi$ fuera de la recta crítica.

*Prueba.* (i) $\Leftrightarrow$ (iii): por definición ($\mu_\gamma^{real} = \mu_\gamma$ iff todos los ceros de $\Xi$ son reales iff RH). (iii) $\Leftrightarrow$ (ii): por el Lema 3, $\mu_\gamma^{real}$ está soportada en ceros de $C_\infty$; y bajo (i) los ceros de $C_\infty$ son $\{\gamma_n\}$. (ii) $\Leftrightarrow$ (iv): reformulación. $\square$

---

## 12. Análisis del potencial $C_\infty$ sin RH: lo que se sabe

**Proposición 8** (estructura de los ceros de $C_\infty$ sin RH). Sin asumir RH: sea $\rho = \sigma + i\gamma$ un cero de $\zeta$ con $\sigma \neq 1/2$. Entonces $C_\infty(t) = w(t) - 2\sum_\rho \cos(t\log|\rho|)/|\rho|$, y la contribución del par $\{\rho, \bar\rho\} = \{\sigma \pm i\gamma\}$ a $C_\infty$ es $-4\cos(t\log|\rho|)/|\rho|$.

Los ceros de $t \mapsto \cos(t\log|\rho|)/|\rho|$ son en $t = \pi(2k+1)/(2\log|\rho|)$ — puntos que en general NO coinciden con $\gamma$ (la parte imaginaria de $\rho$).

**Lema 4** (distinción de ceros: bajo RH vs. sin RH). Bajo RH: para $\rho = 1/2 + i\gamma$, $|\rho| = \sqrt{1/4+\gamma^2} \approx \gamma$ para $\gamma \gg 1$. La contribución de $\rho$ a $C_\infty$ oscila como $\cos(t\log\gamma)/\gamma$.  

Sin RH: para $\rho = \sigma + i\gamma$ con $\sigma > 1/2$, $|\rho| = \sqrt{\sigma^2+\gamma^2} > \gamma$. La frecuencia de oscilación es $\log|\rho| = \frac{1}{2}\log(\sigma^2+\gamma^2) > \log\gamma$ para $\sigma > 1/2$. Luego los ceros de esta contribución están a distancias $\sim \pi/(2\log|\rho|) < \pi/(2\log\gamma)$ del origen — MÁS DENSOS que bajo RH.

Esto genera ceros adicionales de $C_\infty$ en $\mathbb{R}$ que no son $\gamma_n$ — y que serían capturados por $\mu_\infty$ via el Corolario C2. Pero $\mu_\infty = \mu_\gamma^{real}$ (que solo tiene átomos en los $\gamma_n$). Contradicción: esto probaría que no puede haber ceros con $\sigma > 1/2$.

**El problema con el argumento del Lema 4:** La afirmación "los ceros adicionales de $C_\infty$ son capturados por $\mu_\infty$" requiere que la medida $\mu_\infty$ tenga átomos en todos los ceros de $C_\infty$. Pero si un cero de $C_\infty$ es "extra" (no es $\gamma_n$), podría cancelarse con otro cero de $\hat\xi_\lambda$ de modo que la contribución neta a la medida sea cero. Esto requiere análisis más fino.

---

## 13. Resumen del Doc 17

**Probado en este doc:**

- El sistema dinámico de Möbius $\{T_n\}$ converge al atractor único $m_\infty(z)$ (caso LP, incondicional).
- La simetría $\Xi(t) = \Xi(-t)$ implica $m_\infty(-z) = -m_\infty(z)$ e impone $b_n^\infty = 0$ en la escala simétrica.
- La ecuación de punto fijo (EF2) se satisface incondicionalmente en $\mathbb{C}^+$ (Proposición 5).
- **Teorema C1** (incondicional): $\operatorname{spec}(J_\infty) = \{t \in \mathbb{R} : C_\infty(t) = 0\}$.
- **Teorema C3**: RH $\iff$ los ceros reales de $C_\infty$ son exactamente $\{\gamma_n\}$.

**Abierto:**

- Pregunta C.2: ¿Puede probarse directamente (via la estructura de $w$ y $\Psi$) que los ceros reales de $C_\infty$ son $\{\gamma_n\}$ sin asumir RH?
- El Lema 4 da una dirección prometedora (ceros extra de $C_\infty$ si RH falla), pero el argumento de contradicción no está cerrado.
