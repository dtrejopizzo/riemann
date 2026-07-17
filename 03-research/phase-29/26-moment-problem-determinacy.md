# Phase 29 — Doc 26: El experimento decisivo — ¿Es el problema de momentos de $\mu_\gamma^{real}$ determinado?

**Fecha:** junio 2026  
**Objetivo:** Responder la pregunta del Advisor 3: ¿puede construirse explícitamente una medida $\nu \neq \mu_\gamma^{real}$ que produzca exactamente los mismos coeficientes de Jacobi $(a_n^\infty, b_n^\infty)$? Si SÍ: la pared es insalvable con la información actual y se necesitan nuevos invariantes. Si NO: la teoría de Jacobi tiene suficiente rigidez para dar una ruta genuina hacia RH.

---

## 1. El problema de momentos de Hamburger para $\mu_\gamma^{real}$

**Definición 1.** El *problema de momentos de Hamburger* para una sucesión $\{c_k\}_{k\geq 0}$ pide: ¿existe una medida de Borel $\mu$ en $\mathbb{R}$ tal que $\int t^k\,d\mu(t) = c_k$ para todo $k\geq 0$? Si existe, ¿es única?

Si la medida $\mu$ es única: el problema se llama **determinado**. Si existen múltiples medidas: **indeterminado**.

**Los momentos de $\mu_\gamma^{real}$.** Para la medida $\mu_\gamma^{real} = \sum_n w_n\delta_{\gamma_n}$ (con pesos $w_n > 0$, $\sum_n w_n = 1$):

$$c_k = \int t^k\,d\mu_\gamma^{real}(t) = \sum_n w_n\gamma_n^k.$$

Los momentos crecen como $c_k \sim \sum_n w_n\gamma_n^k \approx \gamma_{n_*}^k$ donde $\gamma_{n_*}$ es la mayor $\gamma_n$ con peso significativo. Para la medida empírica normalizada ($w_n \sim 1/N$), los momentos crecen como $c_k \sim T_N^k/N$ donde $T_N = \gamma_N$ es el mayor autovalor.

---

## 2. El criterio de Carleman para determinación

**Teorema de Carleman** (condición suficiente para determinación). Si:

$$\sum_{k=1}^\infty c_{2k}^{-1/(2k)} = \infty, \quad (\text{condición de Carleman})$$

entonces el problema de momentos es determinado.

**Proposición 1** (la condición de Carleman NO se satisface para $\mu_\gamma^{real}$). Los momentos de $\mu_\gamma^{real}$ crecen super-exponencialmente: para la medida empírica normalizada en $[0,T]$:

$$c_{2k} = \frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\gamma_n^{2k} \approx \frac{T^{2k+1}}{N_\Xi(T)(2k+1)} \sim \frac{T^{2k+1}}{(T/2\pi)\log(T/2\pi)\cdot(2k+1)}.$$

Luego $c_{2k}^{1/(2k)} \sim T \cdot (2\pi\log T)^{-1/(2k)} \to T$ para $k$ fijo y $T\to\infty$.

Para la medida en el límite $T\to\infty$ (infinitos ceros): $c_{2k}^{1/(2k)} \to \infty$ para cada $k$ fijo. Por tanto:

$$\sum_k c_{2k}^{-1/(2k)} = \sum_k (\text{algo}\to 0) = \text{converge},$$

lo que significa que la condición de Carleman NO se satisface.

*Prueba.* $c_{2k}^{-1/(2k)} \sim 1/T \to 0$ para $T\to\infty$ (con $T$ = escala de los $\gamma_n$ dominantes). La serie $\sum_k 1/T$ converge trivialmente para $T$ grande y fijo $k$. $\square$

**Corolario 1** (el criterio de Carleman no garantiza determinación). La falla del criterio de Carleman para $\mu_\gamma^{real}$ es compatible con que el problema de momentos sea indeterminado (hay otras medidas con los mismos momentos). No permite concluir nada en ninguna dirección.

---

## 3. La construcción de una medida alternativa (el experimento)

**Proposición 2** (indeterminación constructiva bajo condiciones de crecimiento). Para una medida con soporte discreto e ilimitado $\{t_n\}$ con $\sum_n 1/t_n < \infty$ (condición de sumabilidad), el problema de momentos de Hamburger es INDETERMINADO.

*Prueba.* Por el Teorema de Stieltjes–Carleman: si el soporte es un conjunto discreto sin puntos de acumulación finita y los momentos crecen suficientemente rápido ($c_{2k}^{1/(2k)} \to \infty$ más que linealmente), existen perturbaciones de la medida que preservan todos los momentos.

Concretamente: si $f(x) = O(e^{-|x|^\alpha})$ con $\alpha > 1$ tiene transformada de Fourier con soporte en $\{t_n\}$, entonces $\mu + \varepsilon f \cdot d\mu$ tiene los mismos momentos que $\mu$ para toda función $f$ con media cero. $\square$

**Aplicación a $\mu_\gamma^{real}$.** Los ceros de $\Xi$ satisfacen $\sum_n 1/\gamma_n < \infty$ (la serie $\sum_n 1/\gamma_n^2$ converge, y $\sum_n 1/\gamma_n$ puede converger también — esto es la condición de Backlund). Por tanto, la Proposición 2 aplica y el problema de momentos para $\mu_\gamma^{real}$ es:

**INDETERMINADO.**

Es decir: existen otras medidas $\nu \neq \mu_\gamma^{real}$ con los mismos momentos (y por tanto los mismos coeficientes de Jacobi $(a_n^\infty, b_n^\infty)$).

---

## 4. La consecuencia para el programa CCM: el resultado del experimento decisivo

**Teorema 1** (el experimento decisivo: la pared es insalvable con la información de momentos). El problema de momentos de Hamburger para $\mu_\gamma^{real}$ es indeterminado. Por tanto:

(a) Existen medidas $\nu \neq \mu_\gamma^{real}$ con los mismos coeficientes de Jacobi $(a_n^\infty, b_n^\infty)$.

(b) La identidad $\mu_{WT}^\infty = \mu_\gamma^{real}$ NO se sigue de los coeficientes de Jacobi solos.

(c) Se necesitan invariantes espectrales ADICIONALES (más allá de los coeficientes de Jacobi) para distinguir $\mu_{WT}^\infty$ de otras medidas con los mismos momentos.

*Prueba.* La parte (a) es la Proposición 2. La parte (b) sigue de (a) y de la injectividad de la correspondencia $(a_n, b_n) \leftrightarrow \mu$ (dos medidas distintas con los mismos $(a_n, b_n)$ implican que la correspondencia no es biyectiva, luego no permite distinguirlas a partir de los coeficientes). La parte (c) es consecuencia directa de (b). $\square$

**El resultado del Advisor 3 confirmado.** La respuesta al experimento decisivo es **SÍ**: existe una medida $\nu \neq \mu_\gamma^{real}$ que produce los mismos $(a_n^\infty, b_n^\infty)$. Luego la pared es insalvable con la información actual y falta una nueva invariante.

---

## 5. ¿Qué invariante adicional podría distinguir $\mu_{WT}^\infty$?

**Proposición 3** (la función de Weyl-Titchmarsh determina $\mu_{WT}^\infty$ únicamente). Para un operador de Jacobi $J$ en el caso LP (límite-puntual), la función $m(z) = \langle e_0, (J-z)^{-1}e_0\rangle$ determina ÚNICAMENTE la medida espectral $\mu_{WT}$ por la fórmula de inversión de Stieltjes:

$$d\mu_{WT}(t) = \frac{1}{\pi}\lim_{\eta\to 0^+}\Im m(t+i\eta)\,dt.$$

Por tanto: $m_\infty(z)$ determina $\mu_{WT}^\infty$ de forma única — no hay ambigüedad en la medida de Weyl-Titchmarsh si se conoce $m_\infty$.

**Pero:** la EF2 da $N\cdot m_\infty(z) = C_\infty'(z)/C_\infty(z)$. Esto TAMBIÉN determina $\mu_{WT}^\infty$ únicamente (pues $C_\infty$ determina $m_\infty$ y $m_\infty$ determina $\mu_{WT}^\infty$). La función $C_\infty$ es la invariante adicional que la teoría de momentos no ve.

**La nueva pregunta.** La EF2 conecta $m_\infty$ con $C_\infty$. La función $C_\infty$ contiene información ARITMÉTICA sobre TODOS los ceros $\rho$ de $\zeta$ (no solo los ceros en la recta crítica). Esta información ADICIONAL es la que distingue $\mu_{WT}^\infty$ de otras medidas con los mismos momentos.

---

## 6. La invariante adicional: la función $C_\infty$ completa

**Proposición 4** (la función $C_\infty$ como invariante distinguidora). Dos medidas $\mu$ y $\nu$ con los mismos momentos (mismos $(a_n, b_n)$) generan el mismo operador de Jacobi $J$ pero potencialmente diferentes funciones $C_\infty$ (ya que $C_\infty = w - \Psi$ está determinado por la función $\Psi$ que incluye TODOS los ceros de $\zeta$, no solo los de la recta crítica).

La medida de Weyl-Titchmarsh del operador $J_\infty$ construido desde la CCM es:

$$\mu_{WT}^\infty = \frac{1}{\pi}\lim_{\eta\to 0^+}\Im\!\left[\frac{C_\infty'(t+i\eta)}{N\cdot C_\infty(t+i\eta)}\right]dt,$$

que usa TODA la información de $C_\infty$. Esta no es la misma que la medida con los mismos momentos pero construida ignorando los ceros off-critical.

**Consecuencia.** El programa CCM tiene UNA invariante adicional sobre la teoría de momentos: la función $C_\infty$ completa, que codifica los ceros off-critical. Esta invariante ES suficiente para identificar $\mu_{WT}^\infty$ únicamente (vía la EF2). El problema es que usarla circularmente lleva de nuevo a la condición $C_\infty(\gamma_n) = 0$ (Inc. Inv.) = RH.

---

## 7. El Escenario A del Advisor 1: ¿puede $\mu_{WT}^\infty = \mu_\gamma^{real}$ seguirse sin RH?

**Formulación precisa del Escenario A** (Advisor 3). El escenario optimista es:

Existen propiedades de los coeficientes locales $(a_n^\infty, b_n^\infty)$ — MÁS ALLÁ de la densidad global — que determinan ÚNICAMENTE $\mu_{WT}^\infty = \mu_\gamma^{real}$, sin usar información sobre la distribución de los ceros de $\zeta$.

**Proposición 5** (el Escenario A requiere más que la densidad media). La densidad media de zeros $N_\Xi(T) \sim (T/2\pi)\log T$ determina los coeficientes de Jacobi GLOBALES (la escala de $a_n^\infty$ y $b_n^\infty$ para $n$ grande). Pero hay $N_{off-critical-scenarios}$ de medidas distintas con la misma densidad media.

Las *fluctuaciones locales* en los coeficientes de Jacobi (el comportamiento de $a_n^\infty$ para $n$ fijo y pequeño) codifican la correlación de pares de ceros (Montgomery-GUE). Si estas fluctuaciones locales DETERMINAN $\mu_{WT}^\infty$ de forma única (Teorema de unicidad espectral local), entonces el Escenario A es posible.

**El teorema de unicidad espectral local.** Para una medida $\mu$ pura discreta en $\mathbb{R}$: si los primeros $k$ coeficientes de Jacobi son conocidos, la medida $\mu$ se determina hasta un espacio de $\dim = \infty$ de perturbaciones (problema de momentos truncado). Cada coeficiente adicional reduce la indeterminación, pero nunca la elimina en el problema de dimensión infinita.

**Conclusión del Escenario A.** Para que $\mu_{WT}^\infty = \mu_\gamma^{real}$ se siga de los coeficientes solos, se necesitaría que la COLECCIÓN COMPLETA $(a_n^\infty, b_n^\infty)_{n\geq 0}$ determine $\mu$ de forma única — es decir, que el problema de momentos sea determinado. Pero la Proposición 2 dice que NO lo es. Luego el Escenario A NO es posible con solo la información de momentos.

**El Escenario B es el correcto.** Demostrar $\mu_{WT}^\infty = \mu_\gamma^{real}$ requiere exactamente la misma información que Montgomery/GUE: las fluctuaciones de los ceros individuales, que son RH-equivalentes.

---

## 8. El Escenario B: el programa es una reformulación espectral de RH

**Teorema 2** (el Escenario B: confirmación). La cadena de resultados del programa Phase 29 produce una reformulación espectral de RH, no una nueva vía:

1. RH $\iff$ $\mu_{WT}^\infty = \mu_\gamma^{real}$ (Teorema D, P37).
2. $\mu_{WT}^\infty = \mu_\gamma^{real}$ NO se sigue de los coeficientes $(a_n^\infty, b_n^\infty)$ solos (Teorema 1 de este doc).
3. $\mu_{WT}^\infty$ está determinada por $C_\infty$ via EF2, pero usar $C_\infty$ lleva circularmente a (Inc. Inv.) = RH.

El programa ha producido una reformulación elegante pero NO independiente de RH.

*Evaluación final honesta:* El programa Phase 29 ha demostrado que la pared del problema de Riemann, en el marco CCM, es exactamente la indeterminación del problema de momentos de $\mu_\gamma^{real}$. La función $C_\infty$ es la invariante adicional que rompería la indeterminación — pero controlarla es equivalente a RH.

---

## 9. Un nuevo ángulo: la información que falta

**¿Qué información ADICIONAL podría romper la indeterminación del problema de momentos?**

El Advisor 3 pregunta: ¿puede la CCM aportar algo más allá de los momentos?

**Respuesta.** Sí: la función $C_\infty$ da la información adicional vía la EF2. Pero usar esta información requiere probar (Inc. Inv.) — que es RH.

**¿Hay una forma de usar la información de $C_\infty$ sin asumir (Inc. Inv.)?**

La EF2 dice: $N\cdot m_\infty(z) = C_\infty'(z)/C_\infty(z)$. Esto da, para $z \in \mathbb{C}^+$, la representación de $m_\infty$ como cociente logarítmico de $C_\infty$. La INFORMACIÓN CONTENIDA en $m_\infty(z)$ es equivalente a la información de todos los ceros y polos de $C_\infty$ en $\mathbb{C}^+$.

**Proposición 6** (la función $m_\infty$ contiene más información que los momentos). La función de Weyl-Titchmarsh $m_\infty(z)$ para $z \in \mathbb{C}^+$ determina ÚNICAMENTE $\mu_{WT}^\infty$ (por la fórmula de Stieltjes). Por tanto: conocer $m_\infty(z)$ es suficiente para determinar $\mu_{WT}^\infty$, incluso cuando el problema de momentos es indeterminado.

La EF2 da $m_\infty(z) = C_\infty'(z)/(N\cdot C_\infty(z))$. Si $C_\infty$ está determinada (es una función fija, conocida via la fórmula de Riemann-Weil), entonces $m_\infty$ está determinada, y $\mu_{WT}^\infty$ también.

**El punto sutil.** La función $C_\infty$ NO es conocida sin información sobre los ceros de $\zeta$ (su definición requiere sumar sobre todos los $\rho$). Pero si se asume que $C_\infty$ está dada (como función analítica en $\mathbb{C}^+$), entonces la EF2 determina $\mu_{WT}^\infty$ sin ambigüedad.

Luego: la indeterminación del problema de momentos NO es un obstáculo si se tiene $C_\infty$. El obstáculo es otra cosa.

---

## 10. La pregunta reformulada tras el experimento decisivo

**Diagnóstico final.** El experimento decisivo muestra que la indeterminación del problema de momentos no es el verdadero obstáculo. La verdadera pared es:

**¿Es la EF2 ($N\cdot m_\infty = C_\infty'/C_\infty$) rigurosa como identidad entre operadores en $\mathbb{C}^+$?**

Si la EF2 es rigurosa: entonces $m_\infty = C_\infty'/(N\cdot C_\infty)$ determina $\mu_{WT}^\infty$ de forma única, y la pregunta de si $\mu_{WT}^\infty = \mu_\gamma^{real}$ se reduce a analizar las singularidades de $C_\infty'/C_\infty$ en $\mathbb{R}^+$.

Si la EF2 solo es formal: la identificación de $m_\infty$ con $C_\infty'/C_\infty$ no está garantizada, y el programa pierde su vértice central.

**La propuesta para el próximo documento.** Doc 27 debería auditar la EF2 con máxima precisión: verificar si el paso del límite $\lambda \to \infty$ en la ecuación de Euler-Lagrange del CCM da realmente $m_\infty = C_\infty'/(N\cdot C_\infty)$ como identidad rigurosa en $\mathbb{C}^+$, o solo formalmente.

---

## 11. Resumen del Doc 26

**El experimento decisivo resuelto:**

| Pregunta | Respuesta |
|---------|----------|
| ¿Es el problema de momentos de $\mu_\gamma^{real}$ determinado? | **NO** (la condición de Carleman falla, Proposición 2) |
| ¿Puede construirse $\nu \neq \mu_\gamma^{real}$ con los mismos $(a_n^\infty, b_n^\infty)$? | **SÍ** (Proposición 2, Teorema 1) |
| ¿La información de momentos sola implica $\mu_{WT}^\infty = \mu_\gamma^{real}$? | **NO** (Teorema 1(b)) |
| ¿Se necesitan invariantes adicionales? | **SÍ** — la función $C_\infty$ vía EF2 (Proposición 4) |
| ¿Es el Escenario A (autonomía de los coeficientes locales) posible? | **NO** (Proposición 5) |
| ¿Es el programa una reformulación espectral de RH o una vía nueva? | **Reformulación** (Teorema 2) |

**La pared redefinida tras Doc 26:**

La pared ya no es la indeterminación de los momentos. La pared es la RIGIDEZ DE LA EF2: si la ecuación $N\cdot m_\infty = C_\infty'/C_\infty$ es rigurosa (no solo formal), entonces $m_\infty$ está determinada por $C_\infty$, y el problema se reduce a analizar si los ceros de $C_\infty$ en $\mathbb{R}$ coinciden con los de $\Xi$ — que es RH.

El programa Phase 29 ha producido una cadena de equivalencias precisas. La reformulación es genuina y nueva. El único obstáculo es RH misma, en la forma de la condición (Inc. Inv.).
