# Phase 29 — La brecha espectral y el muro nuevo

**Fecha:** junio 2026  
**Objetivo:** Analizar con máxima precisión la brecha espectral $\delta_\lambda$ y proponer un ataque que evite la teoría de perturbaciones estándar.

---

## 1. Reformulación del muro central

Del documento 02: la teoría de perturbaciones falla porque:
$$\frac{\|A_\lambda\|_{\mathrm{op}}}{\delta_\lambda} \sim \lambda\,e^{4\pi\lambda^2} \to +\infty.$$

Sin embargo, la conclusión que necesitamos NO requiere $\|\xi_\lambda - k_\lambda\|_{L^2} \to 0$. Solo necesitamos que los ceros de $\hat\xi_\lambda$ converjan a los de $\hat k_\lambda$. Esta es una condición sobre el argumento de la función entera, no sobre su módulo en norma $L^2$.

**El muro se reformula:** ¿Por qué los ceros de $\hat\xi_\lambda$ convergen a los de $\hat k_\lambda$ aunque $\xi_\lambda$ no converge a $k_\lambda$ en norma $L^2$?

---

## 2. Estructura de los ceros de funciones enteras con todos los ceros reales

Sea $F(z)$ entera de orden 1, todos sus ceros reales $\{t_n\} \subset \mathbb{R}$ con $t_n \to \pm\infty$, y tal que $F$ es par ($F(-z) = F(z)$). Entonces:
$$F(z) = F(0)\prod_{n=1}^\infty\left(1 - \frac{z^2}{t_n^2}\right).$$

La convergencia de los ceros hacia $\{\gamma_n\}$ (ceros de $\Xi$) en el sentido $\sum_n |t_n - \gamma_n|^2 < \infty$ equivale (vía fórmulas de Newton para sumas de potencias) a la convergencia de los **momentos**:
$$m_k(F) := \sum_n \frac{1}{t_n^{2k}} \to m_k(\Xi) = \sum_n \frac{1}{\gamma_n^{2k}} \quad \forall k \geq 1.$$

Esta es la condición de **convergencia de momentos**.

**Proposición 1** (momentos de $\hat\xi_\lambda$ en términos de $QW_\lambda$). El $k$-ésimo momento de los ceros de $\hat\xi_\lambda$ satisface:
$$m_k(\hat\xi_\lambda) = \sum_n \frac{1}{(t_n^{(\lambda)})^{2k}} = (-1)^k\left.\frac{d^{2k}}{dz^{2k}}\log\hat\xi_\lambda(z)\right|_{z=0} + (\text{términos de tipo poly}).$$

Via la relación $\det_{\mathrm{reg}}(D_{\log}^{(\lambda,N)}-z) = -i\lambda^{-iz}\hat\xi_{\lambda,N}(z)$ (Teorema CCM), los momentos de los eigenvalores de $D_{\log}^{(\lambda,N)}$ son exactamente $m_k(\hat\xi_{\lambda,N})$.

---

## 3. Los momentos como funcionales de $QW_\lambda$

**Lema 1** (relación momento-forma). Para la función $\hat\xi_\lambda$ (transformada del minimizador $\xi_\lambda$ de $QW_\lambda|_{E^+}$):
$$m_1(\hat\xi_\lambda) = \sum_n \frac{1}{(t_n^{(\lambda)})^2} = \frac{\langle D_\lambda^2\xi_\lambda, \xi_\lambda\rangle}{\langle\xi_\lambda,\xi_\lambda\rangle_T} = \frac{QW_\lambda(D\xi_\lambda, D\xi_\lambda)}{QW_\lambda(\xi_\lambda,\xi_\lambda)},$$
donde $D = D_{\log}^{(\lambda)}$ es el operador de escalado.

Este primer momento es una razón de formas cuadráticas evaluadas en el minimizador. No depende del eigenvector completo en norma, sino de cómo el operador $D$ actúa sobre el minimizador.

**Consecuencia:** Para probar la convergencia del primer momento:
$$m_1(\hat\xi_\lambda) \to m_1(\Xi) = \sum_\rho \frac{1}{\gamma_\rho^2},$$
necesitamos mostrar que $\langle D_\lambda^2\xi_\lambda,\xi_\lambda\rangle_T \to \langle D_\infty^2 k, k\rangle_{T_\infty}$ (en un sentido apropiado con $\lambda \to \infty$).

---

## 4. El mecanismo de los ceros: la identidad de Carathéodory–Fejér

El Teorema CCM establece que los ceros de $\hat\xi_{\lambda,N}$ son exactamente los eigenvalores de $D_{\log}^{(\lambda,N)}$. La pregunta de convergencia se traduce en:

**¿Cómo varían los eigenvalores de $D_{\log}^{(\lambda,N)}$ con $\lambda, N$?**

Por la estructura de rango-uno:
$$D_{\log}^{(\lambda,N)} = D - |D\xi\rangle\langle\delta_N|$$

Los eigenvalores de este operador satisfacen la ecuación característica (del Lema 5.4 de CCM):
$$\det(D_{\log}^{(\lambda,N)} - z) = \det(D-z)\cdot \hat\xi_{\lambda,N}(z).$$

La ecuación $\hat\xi_{\lambda,N}(z) = 0$ determina los eigenvalores. Explícitamente (de la fórmula del Lema 5.4):
$$\hat\xi_{\lambda,N}(z) = \sum_{|n| \leq N} \frac{\xi_n^{(\lambda,N)}}{z - 2\pi n/L}\cdot\frac{\sin(zL/2)}{\sqrt{L}/2}.$$

Los ceros de $\hat\xi_{\lambda,N}$ son los valores $z$ donde esta suma se anula. Estos dependen de los coeficientes $\xi_n^{(\lambda,N)}$ (los del eigenvector $\xi_{\lambda,N}$ en la base $\{V_n\}$).

**Observación clave:** Los ceros de $\hat\xi_{\lambda,N}$ no son simples funciones de los coeficientes $\xi_n$ — son soluciones de una ecuación racional en $z$. Aunque los $\xi_n$ puedan cambiar drásticamente con $\lambda$ (debido a la gran perturbación aritmética), los ceros de $\hat\xi$ pueden mantenerse cerca de los de $\hat k_\lambda$ por un efecto de cancelación.

---

## 5. El mecanismo de cancelación: hipótesis sobre los coeficientes

**Hipótesis HC** (coeficientes). Los coeficientes $\xi_n^{(\lambda,N)}$ del minimizador $\xi_{\lambda,N}$ satisfacen:
$$\xi_n^{(\lambda,N)} = c_{\lambda,N}\,k_n^{(\lambda)} + r_n^{(\lambda,N)},$$
donde $k_n^{(\lambda)}$ son los coeficientes de $k_\lambda$, y el "residuo" $r_n^{(\lambda,N)}$ satisface:
$$\sum_{|n|\leq N} \frac{r_n^{(\lambda,N)}}{z - 2\pi n/L} = O\!\left(\frac{1}{\lambda^{1/2-\alpha}}\right) \quad \text{para } z \in K \subset S_{1/2}.$$

Si HC vale, entonces:
$$\hat\xi_{\lambda,N}(z) = c_{\lambda,N}\hat k_\lambda(z) + O(\lambda^{-1/2+\alpha}) \to c\,\Xi(z).$$

**El problema:** HC es una hipótesis sobre la estructura fina de los coeficientes $\xi_n^{(\lambda,N)}$. No se sigue de la teoría de perturbaciones estándar (que falló). Necesita un argumento diferente.

---

## 6. Ataque via unicidad del minimizador con condiciones de frontera

**Proposición 2** (caracterización variacional de $\xi_\lambda$). El minimizador $\xi_\lambda$ de $QW_\lambda|_{E^+}$ es la única función par en $\mathcal{H}_\lambda^+$ que satisface:
$$\left(Q^{\mathrm{arch}} + Q^{\mathrm{cross}} - A_\lambda\right)f = \mu_\lambda f, \quad \delta(\xi_\lambda) = 1,$$
donde $\mu_\lambda$ es el eigenvalor mínimo.

La ecuación de Euler-Lagrange es:
$$(B_\lambda - A_\lambda)\xi_\lambda = \mu_\lambda\xi_\lambda$$
donde $B_\lambda = Q^{\mathrm{arch}} + Q^{\mathrm{cross}}|_{E^+}$.

Esto puede reescribirse como:
$$\xi_\lambda = \mu_\lambda (B_\lambda - A_\lambda)^{-1}\xi_\lambda.$$

O equivalentemente, $\xi_\lambda$ pertenece al kernel del operador $B_\lambda - A_\lambda - \mu_\lambda$. 

**Idea de ataque:** Expresar $(B_\lambda - A_\lambda - \mu_\lambda)^{-1}$ usando la fórmula de resolución, y demostrar que la dependencia de los ceros de $\hat\xi_\lambda$ en $A_\lambda$ es suave/continua incluso cuando $A_\lambda$ es grande.

---

## 7. La ecuación de los ceros vía teoría espectral

**Proposición 3** (ecuación de los ceros). Los ceros $\{t_n^{(\lambda)}\}$ de $\hat\xi_\lambda$ satisfacen la ecuación implícita:
$$\hat\xi_\lambda(t) = 0 \iff \frac{1}{L}\sum_{|n|\leq N}\frac{\xi_n^{(\lambda)}}{t - 2\pi n/L} = 0.$$

Esto es equivalente a que $t$ es un valor propio del operador de escalado $D_{\log}^{(\lambda,N)}$, cuya ecuación espectral es:
$$1 = \langle\delta_N, (D - t)^{-1}D\xi_{\lambda,N}\rangle = \sum_{|n|\leq N}\frac{2\pi n/L}{t - 2\pi n/L}\,\xi_n^{(\lambda)}.$$

Reordenando:
$$\sum_{|n|\leq N}\frac{2\pi n/L}{t - 2\pi n/L}\,\xi_n^{(\lambda)} = 1.$$

Esta es la **ecuación de los ceros** en forma explícita. Los ceros son los valores $t$ que satisfacen esta ecuación racional (en $t$).

**Para estudiar la convergencia de los ceros:** necesitamos entender cómo varía el conjunto de soluciones de esta ecuación cuando los coeficientes $\xi_n^{(\lambda)}$ varían con $\lambda$.

---

## 8. Un estimado de estabilidad de los ceros

**Teorema 1** (estabilidad de los ceros — resultado parcial). Sea $F_\lambda(z) = \hat\xi_\lambda(z)$ y $G_\lambda(z) = \hat k_\lambda(z)$. Supongamos:
1. Todos los ceros de $F_\lambda$ y $G_\lambda$ son reales.
2. $F_\lambda$ y $G_\lambda$ tienen el mismo tipo exponencial: $\log|F_\lambda(iy)| \sim \log|G_\lambda(iy)| \sim (\log\lambda)|y|$ para $y \to \pm\infty$.
3. Los ceros de $G_\lambda$ están en las posiciones $\{s_n^{(\lambda)}\}$ con separación $\min_n|s_n^{(\lambda)}-s_{n+1}^{(\lambda)}| \geq \delta > 0$.
4. $|F_\lambda(z) - G_\lambda(z)| \leq \epsilon |G_\lambda(z)|$ para $z$ en la frontera de los discos $D_n = \{|z-s_n^{(\lambda)}| \leq \delta/2\}$.

Entonces: cada disco $D_n$ contiene exactamente un cero de $F_\lambda$, y este cero $t_n^{(\lambda)}$ satisface $|t_n^{(\lambda)} - s_n^{(\lambda)}| \leq \epsilon\delta/2$.

*Prueba.* Por el principio del argumento (Rouché): en $\partial D_n$, $|F_\lambda - G_\lambda| \leq \epsilon|G_\lambda| < |G_\lambda|$ (para $\epsilon < 1$), luego $F_\lambda$ y $G_\lambda$ tienen el mismo número de ceros en $D_n$, que es 1. El estimado del cero sigue de la diferenciabilidad de los ceros en funciones analíticas. $\square$

**El Teorema 1 reduce la convergencia a:** verificar que $|F_\lambda(z) - G_\lambda(z)| \leq \epsilon|G_\lambda(z)|$ en la frontera de discos suficientemente pequeños centrados en los ceros de $G_\lambda$.

Esto es un **estimado puntual** sobre las funciones (no una cota $L^2$ de eigenvectores), y en principio puede verificarse aunque la brecha espectral sea pequeña.

---

## 9. El nuevo muro: estimado puntual de $F_\lambda - G_\lambda$

El estimado $|F_\lambda(z) - G_\lambda(z)| \leq \epsilon|G_\lambda(z)|$ en círculos alrededor de los ceros de $G_\lambda$ requiere:
$$|\hat\xi_\lambda(z) - c_\lambda\hat k_\lambda(z)| \leq \epsilon|c_\lambda\hat k_\lambda(z)|.$$

Expandiendo:
$$\hat\xi_\lambda(z) - c_\lambda\hat k_\lambda(z) = \int_{\lambda^{-1}}^\lambda (\xi_\lambda(u) - c_\lambda k_\lambda(u))\,u^{-iz}\,d^*u.$$

Para $z = s_n^{(\lambda)} + iy$ con $|y| = \delta/2$:
$$|\hat\xi_\lambda(z) - c_\lambda\hat k_\lambda(z)| \leq \|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}\cdot\lambda^{|y|}.$$

Necesitamos que $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}\cdot\lambda^{\delta/2} \leq \epsilon|c_\lambda\hat k_\lambda(z)|$.

El muro: si $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}$ crece polinomialmente en $\lambda$ (lo más optimista que se puede esperar dado que la brecha espectral es $O(e^{-4\pi\lambda^2})$), pero $|c_\lambda\hat k_\lambda(z)|$ cerca de un cero de $G_\lambda$ es $O(|z - s_n|/\prod_m|z-s_m|)$ — que puede ser EXPONENCIALMENTE PEQUEÑO en $T_n$ (por los términos de la función $\Xi$ lejos del origen) — el estimado puede romperse para ceros grandes.

**Muro preciso:**
$$\text{Wall-H2}: \quad \frac{\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}\cdot\lambda^{\delta/2}}{|c_\lambda\hat k_\lambda(s_n^{(\lambda)} + i\delta/2)|} \to 0 \text{ para todo } n.$$

Esto NO puede seguirse de ningún estimado general de norma $L^2$ o $L^1$ de $\xi_\lambda - c_\lambda k_\lambda$. Requiere información detallada sobre cómo $\Xi(z)$ se comporta cerca de sus ceros — en particular, la derivada $|\Xi'(\gamma_n)|$ (el "peso" del cero).

---

## 10. El peso de los ceros de $\Xi$ como protección

**Definición.** El peso del cero $\gamma_n$ de $\Xi$ es $w_n := |\Xi'(\gamma_n)|$.

**Hecho conocido** (Titchmarsh). Si los ceros son simples (lo que se cree pero no está probado), $w_n > 0$ para todo $n$. La distribución de los pesos está relacionada con los momentos de $|\Xi'|$ en la recta crítica, que se estudian en la Teoría de la Función Zeta de Selberg.

**Proposición 4** (condición en términos del peso). El estimado de Wall-H2 para el $n$-ésimo cero se transforma en:
$$\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1} \ll \frac{w_n}{\lambda^{\delta/2}}.$$

Si $w_n \geq c > 0$ uniformemente en $n$ (que se creería bajo RH + simple zeros), y $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1} = O(\lambda^{-\eta})$ para algún $\eta > \delta/2$, entonces Wall-H2 está resuelto.

**El verdadero obstáculo:** No se conoce la tasa de decaimiento de $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}$. La brecha espectral doblemente exponencialmente pequeña sugiere que $\xi_\lambda$ puede diferir significativamente de $k_\lambda$ en norma. Sin embargo, la diferencia en norma puede ser en una dirección ortogonal a los ceros — que es lo que importa.

---

## 11. Veredicto de Phase 29: lo que se probó y el muro nuevo

### Resultados nuevos de Phase 29:

| Resultado | Estado |
|---|---|
| Par-simple para $\lambda \geq \lambda_0$ (dominancia aritmética vía TPN) | **NUEVO (probado en doc 01)** |
| Fallo de par-simple para $\lambda < \sqrt{2}$ | **NUEVO (probado en doc 01)** |
| Teoría de perturbaciones estándar falla (brecha $O(e^{-4\pi\lambda^2})$ vs norma $O(\lambda)$) | **NUEVO (diagnosticado en doc 02-03)** |
| La convergencia requiere proximidad en ceros, no en norma $L^2$ | **NUEVO (reformulación)** |
| Estabilidad de ceros via Rouché (condición suficiente para H2) | **NUEVO (Teorema 1, doc 03)** |
| Wall-H2: estimado puntual $\|\xi_\lambda - k_\lambda\|_{L^1} = o(w_n\lambda^{-\delta/2})$ | **NUEVO (muro preciso)** |

### El muro nuevo (genuinamente diferente de todos los muros previos):

**Wall-H2:** El eigenvector mínimo $\xi_\lambda$ de $QW_\lambda|_{E^+}$ debe diferir de $k_\lambda$ en norma $L^1$ en un orden menor que $w_n/\lambda^{\delta/2}$ para cada $n$. Esto NO puede seguirse de ningún estimado de norma de operador estándar (la brecha espectral es demasiado pequeña). El mecanismo que lo garantizaría es específico de la estructura aritmética del minimizador $\xi_\lambda$ — en particular, de cómo el Euler producto truncado actúa sobre el kernel de Weil $k_\lambda$.

**Diferencia con los muros previos:**
- Wall A (propagación aritmética): sobre la factorización de $Q$ — no es lo mismo.
- Wall MW-4 (Hasse-Minkowski): sobre formas cuadráticas en dimensión infinita — no aplica aquí.
- Wall H2: sobre la estabilidad de ceros de una función entera bajo una perturbación de eigenvector grande en norma pero potencialmente pequeña en posición de ceros.

Este es el primer muro del programa que NO involucra la positividad de Weil directamente, sino la **continuidad del espectro** de una familia de operadores auto-adjuntos por construcción.

---

## 12. La pregunta más atacable que queda

**Pregunta 29.1.** ¿Es $k_\lambda(u) \geq 0$ para todo $u \in [\lambda^{-1},\lambda]$?

Si sí: $I_p(k_\lambda) \geq 0$ para todo primo $p$, la condición de dominancia DA es más fácil de verificar, y el mecanismo de par-simple para todo $\lambda \geq \sqrt{2}$ tiene apoyo estructural.

**Pregunta 29.2.** ¿Puede acotarse $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}$ vía alguna fórmula explícita para el cambio en eigenvector bajo la perturbación aritmética $A_\lambda$?

La respuesta exacta usa la fórmula de resolución:
$$\xi_\lambda - c_\lambda k_\lambda = (B_\lambda - \mu_\lambda)^{-1}A_\lambda k_\lambda + O(\|A_\lambda k_\lambda\|^2/\delta_\lambda^2)$$
(primer orden de perturbación), que es $O(\lambda e^{4\pi\lambda^2})$ — demasiado grande. Pero la norma $L^1$ de $\int u^{-iz}(\xi_\lambda - k_\lambda)d^*u$ puede ser mucho más pequeña por cancelaciones.

**Pregunta 29.3.** ¿Vale $\sum_n|t_n^{(\lambda)}-\gamma_n|^2 < C$ con $C$ independiente de $\lambda$?

Esta es la versión de convergencia en $\ell^2$ de los ceros. Si vale, por el Lema de Hadamard (doc 02), la convergencia de funciones sigue. Es una conjetura sobre regularidad espectral del operador $D_{\log}^{(\lambda,N)}$.

Estas tres preguntas son las más concretas y atacables que emergen de Phase 29.
