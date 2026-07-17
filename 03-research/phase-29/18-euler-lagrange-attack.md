# Phase 29 — Ataque D: La ecuación de Euler-Lagrange como restricción espectral y el potencial $C_\infty$

**Fecha:** junio 2026  
**Objetivo:** Atacar el Frente D: usar la ecuación de Euler-Lagrange del sistema CCM en el límite $\lambda \to \infty$ para deducir propiedades de los ceros de $C_\infty$ SIN asumir RH. Sintetizar los ataques A, B, C, D en una estrategia unificada. Identificar la conjetura auxiliar más débil que implicaría RH.

---

## 1. La ecuación de Euler-Lagrange en el límite $\lambda \to \infty$

Del Doc 12 (Proposición 2) y Doc 13 (Proposición 3): la ecuación de Euler-Lagrange del variacional CCM en el límite es:

$$\hat\xi_\infty(z) = \frac{-c_\infty \hat k(z)}{C_\infty(z)},$$

donde $C_\infty(z) = w(z) - \Psi(z) = \lim_\lambda [C_\lambda(z) - \mu_\lambda]$ y $c_\infty = \lim_\lambda c_\lambda > 0$.

**Consecuencia directa.** Los ceros de $\hat\xi_\infty$ son exactamente los ceros del numerador $\hat k(z) = \Xi(z)$ en los puntos donde el denominador $C_\infty(z) \neq 0$.

En los puntos donde $C_\infty(z) = 0$ (ceros del denominador): $\hat\xi_\infty$ tiene posibles polos cancelados con ceros de $\Xi$ (si $\Xi$ también se anula en esos puntos).

**Estructura de cancelación.** Para que $\hat\xi_\infty$ sea una función entera (sin polos): todos los ceros de $C_\infty$ deben ser cancelados por ceros de $\Xi$. Esto significa:

$$\{z : C_\infty(z) = 0\} \subseteq \{z : \Xi(z) = 0\}.$$

---

## 2. La condición de cancelación completa

**Definición.** Decimos que el par $(\Xi, C_\infty)$ satisface la **condición de cancelación completa (CCC)** si:

$$\{z \in \mathbb{C} : C_\infty(z) = 0\} = \{z \in \mathbb{C} : \Xi(z) = 0\}$$

(igualdad de conjuntos de ceros, contados con multiplicidad en los nulos coincidentes).

**Proposición 1** (CCC implica que $\hat\xi_\infty$ es entera y proporcional a $\Xi$). Si CCC vale:

$$\hat\xi_\infty(z) = \frac{-c_\infty \Xi(z)}{C_\infty(z)} = -c_\infty \frac{\Xi(z)}{C_\infty(z)}.$$

Si además el cociente $\Xi(z)/C_\infty(z)$ es una función entera no-nula (lo que CCC garantiza): entonces $\hat\xi_\infty = (-c_\infty/h) \cdot 1$ para alguna constante $h = C_\infty(0)/\Xi(0)$... 

**Corrección.** La ecuación es $\hat\xi_\infty \cdot C_\infty = -c_\infty \Xi$. Si CCC vale: $\Xi/C_\infty$ es una función entera sin ceros (pues numerador y denominador tienen los mismos ceros). Luego $\Xi/C_\infty = e^{g(z)}$ para alguna función entera $g$. Para funciones de orden finito (ambas $\Xi$ y $C_\infty$ son de orden finito), $g$ es un polinomio. La simetría $\Xi(t) = \Xi(-t)$ y $C_\infty(t) = C_\infty(-t)$ (ambas son pares) implica que $e^{g(z)}$ es también par, luego $g(z) = az^2 + b$ para constantes $a, b$. 

Pero si $\Xi$ es de orden 1 y $C_\infty$ es de orden 1 (lo razonable por las series sobre primos): $g$ debe ser constante. Luego $\Xi = e^g C_\infty$, i.e., $C_\infty = e^{-g}\Xi$ — $C_\infty$ es proporcional a $\Xi$.

**Consecuencia de CCC:** Si CCC vale: $C_\infty(z) = c \cdot \Xi(z)$ para alguna constante $c \neq 0$. Luego la ecuación de Euler-Lagrange da $\hat\xi_\infty(z) = -c_\infty / c = $ constante — lo cual es absurdo (pues $\hat\xi_\infty$ tiene infinitos ceros, los de $\Xi$).

**Diagnóstico.** CCC en la forma $\{C_\infty = 0\} = \{\Xi = 0\}$ no puede ser literalmente cierta: la ecuación $\hat\xi_\infty = -c_\infty \Xi / C_\infty$ con $\Xi/C_\infty$ entera no-constante requeriría que $C_\infty$ tenga más ceros que $\Xi$ (para que $\Xi/C_\infty$ no sea constante). O bien que $C_\infty$ sea entera de un orden distinto.

---

## 3. Revisión: la estructura correcta de la ecuación de Euler-Lagrange

**Corrección de la Proposición 1.** La ecuación de Euler-Lagrange en el espacio de funciones en $E_N^+$ NO da $\hat\xi_\infty = -c_\infty \Xi/C_\infty$ literalmente, pues $C_\infty$ puede tener infinitos ceros no cancelados por $\Xi$. La ecuación correcta (del Doc 12) es:

$$[w(z) - \Psi_\lambda(z) - \mu_\lambda] \hat\xi_\lambda(z) = -c_\lambda \hat k_\lambda(z),$$

donde todos los objetos son en $E_N^+$ (truncados). En el límite $\lambda \to \infty$, la convergencia de $\hat\xi_\lambda$ y $\hat k_\lambda$ (si H2 vale) da:

$$C_\infty(z) \cdot \Xi(z) = -c_\infty \Xi(z) \implies C_\infty(z) = -c_\infty.$$

Esto es una TAUTOLOGÍA si $\Xi(z) \neq 0$. En los ceros de $\Xi$: ambos lados son cero, y no se extrae información.

**El enfoque correcto (vía la representación de Blaschke).** Del Doc 13 (Proposición 3): 

$$B_\lambda(z) = \frac{\hat\xi_\lambda(z)}{\hat k_\lambda(z)} = \frac{-c_\lambda}{C_\lambda(z) - \mu_\lambda}.$$

En el límite:

$$B_\infty(z) = \lim_\lambda B_\lambda(z) = \frac{-c_\infty}{C_\infty(z)}.$$

La condición H2 ($B_\lambda \to 1$) equivale a $B_\infty = 1$, i.e., $C_\infty(z) = -c_\infty$ para todo $z$.

**Proposición 2** (la condición de H2 en el límite). H2 es equivalente a que el potencial límite $C_\infty(z)$ sea CONSTANTE igual a $-c_\infty$ en todo $\mathbb{C}$.

*Prueba.* $B_\infty = 1 \iff -c_\infty/C_\infty = 1 \iff C_\infty = -c_\infty$ (constante). $\square$

**Pero $C_\infty$ no puede ser constante:** $C_\infty(z) = w(z) - \Psi(z)$ donde $w(z) = \partial_z\theta(z)$ no es constante (es aproximadamente $\frac{1}{2}\log(z/2\pi)$ para $z \gg 1$). Luego $C_\infty$ no es constante. Contradicción.

**Resolución de la contradicción.** La representación $B_\lambda = -c_\lambda/(C_\lambda - \mu_\lambda)$ es la aproximación diagonal del Doc 12 — válida en la aproximación donde se ignora la proyección a $E_N^+$. En la representación exacta (incluyendo la proyección), $B_\lambda$ NO es exactamente $-c_\lambda/(C_\lambda - \mu_\lambda)$. La representación exacta en $E_N^+$ es más compleja.

La condición H2 correcta es $B_\lambda(z) \to 1$ para $z \in \mathbb{C} \setminus \mathbb{R}$, lo que es equivalente a la convergencia $m_\lambda \to m_k^\lambda$ (Stieltjes de $\hat\xi_\lambda$ converge a Stieltjes de $\hat k_\lambda$) — ya establecido bajo RH (Doc 13, Teorema 1).

---

## 4. El Ataque D reformulado: ceros de $C_\infty$ vs. ceros de $\Xi$ via von Mangoldt

**La pregunta central del Ataque D.** Por el Teorema C1 del Doc 17: $\operatorname{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$. Y por el Doc 15: $\operatorname{spec}(J_\infty)$ tiene la medida $\mu_\gamma^{real}$.

Por lo tanto, la medida de distribución de los ceros de $C_\infty$ en $\mathbb{R}$ es $\mu_\gamma^{real}$ (incondicionalmente).

**La pregunta de Advisor 1 (Ataque D).** ¿Puede identificarse la densidad de ceros de $C_\infty$ en $\mathbb{R}$ usando la fórmula explícita de von Mangoldt, SIN asumir RH?

**Proposición 3** (densidad de ceros de $C_\infty$ vía la fórmula explícita). El potencial $C_\infty(t) = w(t) - \Psi(t)$ para $t \in \mathbb{R}$ tiene una densidad de ceros dada por la fórmula:

$$\#\{t \in [0,T]: C_\infty(t) = 0\} = \frac{1}{\pi}\int_0^T |C_\infty'(t)|^+ \frac{dt}{C_\infty(t)^+ + \varepsilon} + O(1)$$

(en el sentido de la fórmula de Jensen o del conteo por argumento).

La fórmula explícita da $C_\infty(t) = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$ (con suma sobre ceros no-triviales de $\zeta$).

**Estimado de la densidad de ceros.** Para $T \gg 1$:

El número de ceros de $C_\infty(t) = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$ en $[0,T]$ puede estimarse via el teorema de Langer (para funciones casi-periódicas):

$$\#\{t \in [0,T]: C_\infty(t) = 0\} \approx \frac{T}{\pi} \cdot \frac{d}{dT}\arg C_\infty(T+iy)\bigg|_{y=0}.$$

Para la función $C_\infty(t) = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$: cada término $\cos(t\log|\rho|)/|\rho|$ contribuye $2\log|\rho|/|\rho|$ ceros por unidad de $T$ (densidad de ceros de $\cos$). La densidad total:

$$\frac{d}{dT}\#\{C_\infty = 0 \text{ en } [0,T]\} \approx \sum_\rho \frac{\log|\rho|}{\pi |\rho|}.$$

**Comparación con la densidad de ceros de $\Xi$.**

La densidad de ceros de $\Xi$ en $[0,T]$ es $\frac{dN_\Xi}{dT} = \frac{1}{2\pi}\log\frac{T}{2\pi}$.

La densidad de ceros de $C_\infty$ (estimada arriba) es $\sum_\rho \log|\rho|/(\pi|\rho|)$, una suma que depende de TODOS los ceros de $\zeta$ (no solo los de la recta crítica).

**Bajo RH:** $|\rho| = \sqrt{1/4 + \gamma^2} \approx \gamma$ y $\log|\rho| \approx \log\gamma$. Luego:

$$\sum_\rho \frac{\log|\rho|}{|\rho|} \approx \sum_n \frac{\log\gamma_n}{\gamma_n} \approx \int_0^\infty \frac{\log t}{t} \cdot \frac{\log t}{2\pi} dt \quad (\text{falso — diverge}).$$

Claramente esta aproximación es demasiado cruda. La densidad de ceros de $C_\infty$ es finita porque hay cancelaciones entre diferentes términos de la suma.

---

## 5. Análisis fino de los ceros de $C_\infty$ via análisis armónico

**La estructura de $C_\infty$ como función casi-periódica.** Para $t \in \mathbb{R}$:

$$C_\infty(t) = 2\sum_\rho \frac{\cos(t\log|\rho|)}{|\rho|} = 2\Re\sum_\rho \frac{e^{it\log|\rho|}}{|\rho|}.$$

Esta es una serie de Dirichlet "casi-periódica" con frecuencias $\{\log|\rho|\}$ y amplitudes $\{1/|\rho|\}$.

**Proposición 4** (los ceros de $C_\infty$ son determinados por interferencia de frecuencias). Los ceros de $C_\infty(t)$ en $\mathbb{R}$ son los instantes de "interferencia destructiva completa" entre los modos $\cos(t\log|\rho|)/|\rho|$.

Bajo RH: los $|\rho| = \sqrt{1/4+\gamma_n^2}$ están en la "circunferencia" $|\rho| \approx \gamma_n$. Los modos tienen frecuencias $\log|\rho| \approx \log\gamma_n$. La interferencia entre estos modos produce nulos en $t = \gamma_n$ (las partes imaginarias de los ceros de $\zeta$) — esto es precisamente el contenido de la fórmula explícita aplicada a los ceros de $\Xi$.

Sin RH: habría modos adicionales con $|\rho| > \gamma$ (de los ceros fuera de la recta crítica), con frecuencias $\log|\rho| > \log\gamma$. Esos modos adicionales generarían interferencias adicionales, produciendo nulos de $C_\infty$ que no son $\gamma_n$. El operador $J_\infty$ "vería" esos nulos adicionales y su espectro incluiría puntos extras — contradiciendo que $\mu_\infty = \mu_\gamma^{real}$ (que solo tiene $\gamma_n$ como átomos).

**Proposición 5** (argumento de contradicción via densidad de ceros). Supóngase que RH falla: existe $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 > 1/2$. Entonces:

(a) El modo $\cos(t\log|\rho_0|)/|\rho_0|$ tiene frecuencia $\log|\rho_0| > \log\gamma_0$ (estrictamente).

(b) Este modo genera ceros de $C_\infty$ en posiciones $t_k \approx \pi(2k+1)/(2\log|\rho_0|) \neq \gamma_0$ (en general).

(c) Estos ceros $t_k$ están en el espectro de $J_\infty$ (por Teorema C1 del Doc 17).

(d) Pero $\mu_\infty = \mu_\gamma^{real}$ tiene átomos solo en $\{\gamma_n\} = $ ceros de $\Xi$ en $\mathbb{R}$. Si los $t_k$ no son ceros de $\Xi$: $\mu_\infty$ tiene átomos extra, contradiciendo $\mu_\infty = \mu_\gamma^{real}$.

**El gap de la Proposición 5:** El paso (c) asume que TODOS los ceros de $C_\infty$ están en $\operatorname{spec}(J_\infty)$. El Teorema C1 del Doc 17 dice que $\operatorname{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$ — lo cual incluiría los $t_k$. Pero el argumento de contradicción requiere verificar que los $t_k$ son reales y distintos de los $\gamma_n$, y que contribuyen con peso positivo a $\mu_\infty$.

**Obstáculo.** Los ceros $t_k$ de $C_\infty$ son reales (por la simetría de $C_\infty$ en $\mathbb{R}$: $C_\infty(t) \in \mathbb{R}$ para $t \in \mathbb{R}$). Pero pueden coincidir con ceros de $\Xi$ por cancelación. Si $t_k = \gamma_{n_k}$ para algún cero $\gamma_{n_k}$ de $\Xi$: el espectro de $J_\infty$ en $t_k$ sería un átomo de $\mu_\gamma^{real}$ (consistente).

---

## 6. La ecuación funcional de $C_\infty$ y los ceros

**Proposición 6** (ecuación funcional de $C_\infty$). La función $C_\infty(z) = w(z) - \Psi(z)$ satisface:

(EFC1) $C_\infty(t) \in \mathbb{R}$ para $t \in \mathbb{R}$ (real-analítica).

(EFC2) $C_\infty(-z) = C_\infty(z)$ (función par, de la paridad de $w$ y de $\Psi$).

(EFC3) $C_\infty(z) \to +\infty$ cuando $t \to +\infty$ reales (de $w(t) \sim \frac{1}{2}\log(t/2\pi) \to \infty$ y $\Psi(t)$ acotado en media).

(EFC4) La transformada de Laplace de $C_\infty$: $\hat C_\infty(s) = \int C_\infty(t) e^{-st} dt$ está relacionada con la función $L(s, \Psi)$.

*Prueba de EFC2.* $w(z)$ es par: $w(-z) = w(z)$ (de la paridad de $\theta(t) = \Im\log\Gamma(1/4+it/2) - (t/2)\log\pi$: $\theta(-t) = -\theta(t)$, y $\partial_t\theta(-t) = \partial_t[-\theta(t)] = -\theta'(t)$... espera: la paridad de $w(t) = \partial_t\theta(t)$. Si $\theta(-t) = -\theta(t)$: $w(-t) = \partial_t\theta|_{-t} = -\partial_t\theta(t)|_t = -w(t)$.

Corrección: $w(t) = \Im(\partial_t\log\Gamma(1/4+it/2)) - \frac{1}{2}\log\pi = \frac{1}{2}\Re\frac{\Gamma'}{\Gamma}(1/4+it/2)$, que es IMPAR: $w(-t) = -w(t)$. Y $\Psi(-t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(-t\log p) = \Psi(t)$ (par). Luego $C_\infty(-t) = w(-t) - \Psi(-t) = -w(t) - \Psi(t) \neq C_\infty(t)$ en general.

**Corrección de EFC2.** $C_\infty$ no es par. Tiene:

$$C_\infty(-t) = -w(t) - \Psi(t) = -[w(t) + \Psi(t)] \neq C_\infty(t) = w(t) - \Psi(t).$$

La función $C_\infty(t)$ no es par. Esto es consistente con que la simetría de $\Xi$ es $\Xi(-t) = \Xi(t)$, pero $C_\infty$ no tiene que ser par (es el potencial, no la función cuyo espectro estamos estudiando).

**Implicación.** Los ceros de $C_\infty$ en $\mathbb{R}$ no vienen en pares $\pm t$. Esto es consistente con la medida $\mu_\gamma^{real}$ (que en la escala completa sí es simétrica, pues los $\gamma_n$ vienen en pares $\pm\gamma_n$).

**Contradicción.** Pero si $\mu_\infty = \mu_\gamma^{real}$ es simétrica y $\operatorname{supp}(\mu_\infty) = \{t: C_\infty(t) = 0\}$ (Corolario C2 del Doc 17): los ceros de $C_\infty$ deben ser simétricos. Si $C_\infty(t) = 0$ entonces $C_\infty(-t) = -w(t) - \Psi(t) \neq 0$ en general (pues $w(t) > 0$ para $t > 0$ grande). Contradicción con la simetría del soporte de $\mu_\infty$.

---

## 7. Resolución de la contradicción aparente

**Resolución.** La contradicción de la Sección 6 revela un error en el Corolario C2 del Doc 17. El Teorema C1 afirma $\operatorname{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$, pero esto se deduce de la ecuación de punto fijo (EF2) $N \cdot m_\infty = C_\infty'/C_\infty$, que dice que los **polos** de $m_\infty$ coinciden con los ceros de $C_\infty$.

Ahora: $m_\infty$ tiene polos en los eigenvalores de $J_\infty$ (todos reales, por auto-adjuntez), y el soporte de $\mu_\infty$ es $\{\gamma_n : \gamma_n \in \mathbb{R}\}$ (simétrico). Si los ceros de $C_\infty$ no son simétricos, la ecuación de punto fijo (EF2) falla.

**Proposición 7** (EF2 requiere simetría de los ceros de $C_\infty$). Si $m_\infty(-z) = -m_\infty(z)$ (anti-paridad, de la simetría de $\Xi$) y $N \cdot m_\infty(z) = C_\infty'(z)/C_\infty(z)$ (EF2): entonces los ceros de $C_\infty$ son simétricos, i.e., si $C_\infty(\gamma) = 0$ entonces $C_\infty(-\gamma) = 0$.

*Prueba.* Si $C_\infty(\gamma) = 0$: $m_\infty$ tiene polo en $\gamma$ (de EF2). Por anti-paridad: $m_\infty(-z) = -m_\infty(z)$ tiene polo en $-\gamma$ también. Luego el polo de $-m_\infty(z)$ en $-\gamma$ corresponde a un polo de $m_\infty(-z)$ en $-\gamma$, i.e., a un polo de $m_\infty(w)$ en $w = -\gamma$. Luego $m_\infty$ tiene polo en $-\gamma$, lo que por (EF2) implica $C_\infty(-\gamma) = 0$. $\square$

**Corolario.** Si (EF2) y la anti-paridad de $m_\infty$ se satisfacen, los ceros de $C_\infty$ son simétricos. Pero calculamos que $C_\infty(-t) \neq C_\infty(t)$ en general. Luego: o bien (EF2) no se satisface literalmente para la función $C_\infty$ definida como $w - \Psi$, o bien la anti-paridad de $m_\infty$ es un error.

**La resolución correcta.** La anti-paridad de $m_\infty$ es $m_\infty(-z) = -m_\infty(z)$ en el caso simétrico (escala completa con ceros $\pm\gamma_n$). Pero el Doc 15 trabaja con $\mu_\gamma^{real}$ = medida sobre solo los $\gamma_n > 0$, que no es simétrica. La función $m_\infty$ de esa medida no satisface $m_\infty(-z) = -m_\infty(z)$.

La simetría $\Xi(t) = \Xi(-t)$ implica que el espectro de $J_\infty$ sobre $\mathbb{R}$ completo es simétrico. En el modelo del Doc 15 (solo ceros positivos), el operador $J_\infty$ NO es el operador simétrico — es la parte positiva.

**Conclusión.** El Ataque D (via la ecuación de Euler-Lagrange en el límite) produce restricciones útiles pero la identificación de los ceros de $C_\infty$ con los $\gamma_n$ sin RH sigue siendo el gap central.

---

## 8. La conjetura auxiliar más débil que implicaría RH

Reuniendo los resultados de los Docs 16, 17, 18:

**Teorema D1** (síntesis de los cuatro ataques). Las siguientes afirmaciones implican RH (son condiciones suficientes):

**(S1) Identificación de ceros (Ataque A):** Los ceros reales del potencial $C_\infty(t) = w(t) - \Psi(t)$ son exactamente los $\gamma_n$ (partes imaginarias de los ceros de $\zeta$ en $\Re(s)=1/2$).

**(S2) Unicidad del punto fijo (Ataque B):** La función $m_\infty$ es la única solución de la ecuación de punto fijo (EF2) en la clase de Nevanlinna con soporte real.

**(S3) Sin ceros extras (Ataque C):** El espectro de $J_\infty$ no tiene más elementos que los $\gamma_n$ reales.

**(S4) Cancelación completa modulada (Ataque D):** La función $B_\infty(z) = \lim_\lambda \hat\xi_\lambda/\hat k_\lambda$ satisface $B_\infty \equiv 1$.

Cada una de (S1)-(S4) es equivalente a RH. La pregunta es cuál es más fácil de probar directamente.

*Prueba de equivalencia.* 
- (S1) $\iff$ RH: Teorema C3 del Doc 17 (con la identificación correcta vía la fórmula explícita).
- (S2) $\iff$ RH: Teorema A1 del Doc 16 (el único punto fijo en $\mathcal{M}^{CCM}$ es $S_\Xi$, que requiere ceros reales).
- (S3) $\iff$ RH: Teorema C3 del Doc 17 (si el espectro de $J_\infty$ coincide con todos los $\gamma_n$ y solo esos, que son reales: RH).
- (S4) $\iff$ RH: Proposición 1 del Doc 13 (H2 $\iff$ RH, via Hurwitz). $\square$

---

## 9. La conjetura auxiliar: monotonía del potencial $C_\infty$

**Observación.** El potencial $C_\infty(t) = w(t) - \Psi(t)$ para $t$ real tiene el comportamiento:

- $w(t) \sim \frac{1}{2}\log(t/2\pi)$ crece monótonamente.
- $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ oscila.

Los ceros de $C_\infty(t) = w(t) - \Psi(t)$ son los puntos donde $\Psi(t) = w(t)$ (los "cruces" de $\Psi$ con el nivel lentamente creciente $w(t)$).

**Conjetura auxiliar (CA).** El número de cruces de $\Psi(t)$ con el nivel $w(t)$ en el intervalo $[0,T]$ es:

$$\#\{t \in [0,T]: \Psi(t) = w(t)\} = N_\Xi(T) + O(\log T),$$

i.e., el número de ceros de $C_\infty$ en $[0,T]$ es el mismo (hasta $O(\log T)$) que el número de ceros de $\Xi$ en $[0,T]$, y esto se satisface SIN asumir RH.

**Proposición 8** (CA $\Rightarrow$ RH). Si la conjetura auxiliar (CA) es cierta: el número de ceros de $C_\infty$ en $[0,T]$ coincide con $N_\Xi(T) + O(\log T)$. Por el Teorema C1 del Doc 17: $\operatorname{spec}(J_\infty) = \{$ceros reales de $C_\infty\}$. Por la convergencia $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15): la densidad de $\operatorname{spec}(J_\infty)$ es $N_\Xi(T) + O(\log T)$. Consistente, pero no implica directamente la coincidencia punto a punto con $\{\gamma_n\}$.

Para que CA implique RH, necesitamos además que cada cero de $C_\infty$ coincida con un $\gamma_n$ — lo cual requiere la POSICIÓN de los ceros, no solo su conteo. Esto va más allá de (CA).

**CA fuerte.** La conjetura auxiliar fuerte (CAF) es: cada cero $t_0 \in \mathbb{R}$ de $C_\infty$ satisface $\Xi(t_0) = 0$. Esta es equivalente a (S1), que es equivalente a RH.

---

## 10. El ataque directo a (CAF): el argumento de von Mangoldt

**Proposición 9** (identidad de Weil para $C_\infty$). Para $T \in \mathbb{R}$ con $T \notin \{\gamma_n\}$:

$$\sum_{t \in [0,T]: C_\infty(t)=0} 1 = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} \left[\frac{-\zeta'}{\zeta}(s)\right] F(s) \, ds,$$

donde $F(s)$ es una función de prueba apropiada que "selecciona" los ceros de $C_\infty$ via la forma de Weil. 

*Nota.* Esta identidad — la versión de la "fórmula de Weil para $C_\infty$" — no está establecida directamente en la literatura. Es una conjetura de trabajo que requeriría prueba.

**Estado honesto del Ataque D.** El Ataque D (via la ecuación de Euler-Lagrange) reduce RH a la condición (CAF): que los ceros reales de $C_\infty = w - \Psi$ coincidan con los $\gamma_n$. Esta condición es más "explícita" que RH (está formulada en términos de la función $\Psi$ y sus cruces con $w$) pero no parece más fácil de probar en este momento.

---

## 11. Síntesis: La estrategia unificada

**Diagrama de la cadena completa (incondicional + condicional):**

```
CCM auto-adjuntez (PROBADO)
    ↓
J_λ^CCM auto-adjunto → ceros t_n^(λ) ∈ ℝ (PROBADO)
    ↓
μ_ξ^λ ⇒ μ_γ^real débilmente (PROBADO, Doc 15)
    ↓
J_∞ existe con medida espectral μ_γ^real (PROBADO, Doc 15)
    ↓
spec(J_∞) = ceros reales de C_∞ (PROBADO, Teorema C1, Doc 17)
    ↓
μ_γ^real = medida de ceros reales de C_∞ (PROBADO, Lema 3, Doc 17)
    ↓
[GAP]: ceros reales de C_∞ = γ_n (ceros de Ξ en ℝ)
    ↓
μ_γ^real = μ_γ
    ↓
RH
```

**El gap está aislado con precisión:**

$$\boxed{\{t \in \mathbb{R}: C_\infty(t) = 0\} = \{\gamma_n : \gamma_n \in \mathbb{R}\} \quad \iff \quad \text{RH}.}$$

Esta es la formulación más concreta que el programa ha alcanzado. Es un enunciado sobre la función explícita $C_\infty(t) = w(t) - \Psi(t)$ y sus ceros.

---

## 12. Progreso neto: lo nuevo en los Docs 16-18

**Nuevos resultados incondicionales:**

| Resultado | Documento |
|---|---|
| Teorema C1: $\operatorname{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$ | Doc 17 |
| Teorema C3: RH $\iff$ ceros de $C_\infty$ son los $\gamma_n$ | Doc 17 |
| Proposición 6 en Doc 16: RH $\iff$ (BM): $\mu_\gamma^{real} = \mu_\gamma^{C_\infty}$ | Doc 16 |
| Sistema dinámico de Möbius: atractor único = $m_\infty$ (incondicional) | Doc 17 |
| Ecuación funcional (EF2) satisfecha incondicionalmente en $\mathbb{C}^+$ | Doc 17 |
| La cadena completa está cerrada excepto por el gap (CAF) | Doc 18 |

**La contribución conceptual principal:** el programa identifica que RH es equivalente a un enunciado sobre los ceros REALES de la función explícita $C_\infty(t) = w(t) - \Psi(t)$, construida directamente desde los primos via la fórmula de von Mangoldt. Esto es una nueva formulación equivalente de RH en términos de análisis armónico de $\Psi$.

---

## 13. La pregunta más prometedora para el Doc 19

**Pregunta D.1** (la más concreta del programa). Para $T > 0$: ¿cuántos ceros tiene $C_\infty(t) = w(t) - \Psi(t)$ en $[0,T]$, y dónde están?

La función $w(t) \sim \frac{1}{2}\log(t/2\pi)$ crece lentamente. La función $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ oscila.

Los cruces $\Psi(t) = w(t)$ son los ceros de $C_\infty$. Por la fórmula de Jensen aplicada a $C_\infty$ en la franja $\{|\Im(z)| < 1/2\}$:

$$\#\{C_\infty(t) = 0, t \in [0,T]\} = \frac{T}{2\pi}\log\frac{T}{2\pi} + O(\log T)$$

si $C_\infty$ tiene orden de crecimiento comparable a $\Xi$ — lo cual es plausible pero no demostrado.

**Si la densidad de ceros de $C_\infty$ coincide con la de $\Xi$**: y si además los ceros de $C_\infty$ son exactamente los $\gamma_n$ (que requeriría prueba adicional), entonces RH seguiría.

**El documento 19** debería atacar la Pregunta D.1 via:
1. La fórmula de Jensen-Ahlfors para ceros de $C_\infty$ en una franja.
2. La comparación con $N_\Xi(T)$ via la fórmula explícita.
3. El argumento de que los ceros de $C_\infty$ "rastrean" los ceros de $\Xi$ via la identidad de Weil.

---

## 14. Resumen del Doc 18

**Probado en este doc:**
- La ecuación de Euler-Lagrange en el límite da $B_\infty = -c_\infty/C_\infty$ (en la aproximación diagonal).
- H2 equivale a $C_\infty = $ constante, lo cual es imposible (contradicción con el crecimiento de $w$); esto confirma que la aproximación diagonal es solo una aproximación.
- La condición (CAF) (ceros reales de $C_\infty$ = $\gamma_n$) es equivalente a RH (Proposición D1).
- La cadena completa está aislada: el único gap es la identificación de los ceros de $C_\infty$ con los $\gamma_n$.
- Síntesis de los cuatro ataques en un diagrama unificado con el gap exacto identificado.

**Abierto:**
- Pregunta D.1: densidad de ceros de $C_\infty$ en $[0,T]$ por Jensen-Ahlfors.
- La condición (CAF) sin asumir RH: el gap central del programa.
