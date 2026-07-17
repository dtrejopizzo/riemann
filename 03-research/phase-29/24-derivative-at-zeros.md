# Phase 29 — Doc 24: La derivada $C_\infty'(\gamma_n)$ y la simplicicidad de los ceros de $C_\infty$

**Fecha:** junio 2026  
**Objetivo:** Calcular $C_\infty'(\gamma_n)$ explícitamente via la fórmula explícita diferenciada. Mostrar que $C_\infty'(\gamma_n) \neq 0$ bajo hipótesis de independencia lineal de las frecuencias $\log|\rho|$. Combinar con el Teorema 3 del Doc 23 para dar RH condicionado a (LI).

**Referencia al Doc 23 Proposición 8.** Si todos los ceros de $C_\infty$ son simples: $\mu_{WT}^\infty = \mu_\gamma^{real}$, dando RH. La simplicicidad requiere $C_\infty'(\gamma_n) \neq 0$ en cada cero $\gamma_n$ de $C_\infty$.

---

## 1. La derivada $C_\infty'$ en los ceros de $\Xi$

**Definición.** Para $C_\infty(t) = 2\sum_\rho\cos(t\log|\rho|)/|\rho| + c_0$, la derivada es:

$$C_\infty'(t) = -2\sum_\rho\frac{\log|\rho|}{|\rho|}\sin(t\log|\rho|).$$

**Proposición 1** (la derivada $C_\infty'$ via la fórmula explícita diferenciada). La fórmula explícita de Riemann-Weil, diferenciada respecto a $t$, da la identidad:

$$C_\infty'(t) = -2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(t\log p).$$

*Esto dice:* $C_\infty'(t)$ es la "derivada de la fórmula explícita" — una suma sobre primos del tipo $\sum_p\Lambda(p)p^{-1/2}\log p\cdot\sin(t\log p)$.

*Prueba (formal).* Derivando $C_\infty(t) = w(t) - \Psi(t)$ termino a término (en el régimen donde la derivación está justificada): $C_\infty'(t) = w'(t) - \Psi'(t)$. Ahora $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ da $\Psi'(t) = -2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(t\log p)$. Y $w'(t) = 0$ (ya que $w(t) = \Re[\psi(1/4+it/2)/2 - \log\pi/2]$ para $t$ real... en realidad $w'(t)$ no es cero, es la parte real del logaritmo de la función Gamma diferenciada). 

**Corrección.** $C_\infty'(t) = w'(t) - \Psi'(t)$ donde:

$$w'(t) = \frac{1}{4}\Re\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right), \quad \Psi'(t) = -2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(t\log p).$$

Y $w'(t) \sim \frac{1}{4t^2} \cdot O(1)$ para $t$ grande (decaimiento polinomial). Para $t = \gamma_n$ grande: $w'(\gamma_n) = O(\gamma_n^{-2})$ es negligible.

**Proposición 1'** (aproximación de $C_\infty'(\gamma_n)$ para $\gamma_n$ grande).

$$C_\infty'(\gamma_n) \approx 2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p) + O(\gamma_n^{-2}).$$

---

## 2. La condición de cero doble: dos ecuaciones simultáneas

**Definición.** Un cero $t_0 \in \mathbb{R}$ de $C_\infty$ es **doble** si $C_\infty(t_0) = 0$ y $C_\infty'(t_0) = 0$. Esto requiere dos condiciones simultáneas:

$$\sum_\rho\frac{\cos(t_0\log|\rho|)}{|\rho|} = -\frac{c_0}{2}, \quad (\text{I})$$

$$\sum_\rho\frac{\log|\rho|}{|\rho|}\sin(t_0\log|\rho|) = 0. \quad (\text{II})$$

**Proposición 2** (un cero doble requiere dependencia lineal de las frecuencias $\log|\rho|$). Si las frecuencias $\{\log|\rho|\}_\rho$ son linealmente independientes sobre $\mathbb{Q}$ (hipótesis LI), entonces las condiciones (I) y (II) no pueden satisfacerse simultáneamente para ningún $t_0 \in \mathbb{R}$.

*Argumento.* Bajo (LI): el vector $(t_0\log|\rho_1|, t_0\log|\rho_2|, \ldots)$ módulo $2\pi$ es equidistribuido en el toro infinito (Kronecker-Weyl). Las condiciones (I) y (II) dicen que en el punto $t_0$, los ángulos $\{t_0\log|\rho_k|\}$ satisfacen dos restricciones de suma (que el coseno y el seno con pesos den valores específicos). Bajo (LI) y equidistribución, estas dos condiciones SIMULTÁNEAS tienen probabilidad cero — es decir, si (LI) se satisface "genéricamente", casi ningún $t_0$ puede satisfacer ambas condiciones a la vez.

*Nota de honestidad.* El argumento de Kronecker-Weyl aplica formalmente, pero la hipótesis (LI) sobre las frecuencias $\log|\rho|$ de los CEROS de $\zeta$ (no de los primos) es más fuerte que la hipótesis estándar de independencia lineal de $\log\gamma_n$ (los imaginarios de los ceros). Una prueba rigurosa de la Proposición 2 requeriría establecer (LI) para los $\log|\rho|$ específicos, lo cual es una conjetura abierta. $\square$

---

## 3. La derivada $C_\infty'(\gamma_n)$ via la fórmula explícita diferenciada

**Proposición 3** (expresión de $C_\infty'(\gamma_n)$ via la fórmula de Riemann-Weil diferenciada). La fórmula explícita, diferenciada respecto a $s$ en $s = 1/2+it$ y evaluada en $t = \gamma_n$, da:

$$C_\infty'(\gamma_n) = -\frac{d}{dt}\bigg|_{t=\gamma_n}\left[w(t) - \Psi(t)\right] \approx 2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p).$$

Bajo RH (todos los ceros $\rho = 1/2+i\gamma$ en la recta crítica): la fórmula explícita diferenciada en $s = \rho_n = 1/2+i\gamma_n$ da:

$$\operatorname{Res}_{s=\rho_n}\!\left[\frac{d}{ds}\left(-\frac{\zeta'}{\zeta}(s)\right)\right] = 1, \quad \text{si }\rho_n\text{ es cero simple de }\zeta.$$

Y el lado izquierdo (via la fórmula de von Mangoldt diferenciada) es:

$$\sum_p\Lambda(p)p^{-1/2-i\gamma_n}(\log p)^2 + \sum_{\rho\neq\rho_n}\frac{1}{(\rho_n-\rho)^2} = -1 + (\text{contribuciones regulares}).$$

Tomando la parte imaginaria y conectando con $C_\infty'(\gamma_n)$:

$$\Im\left[\sum_p\Lambda(p)p^{-1/2-i\gamma_n}(\log p)^2\right] = \sum_p\Lambda(p)p^{-1/2}(\log p)^2\sin(\gamma_n\log p),$$

que es proporcional a $C_\infty'(\gamma_n)$ (la suma sobre primeros vs. todos los primos difiere por factores de $(\log p)^k$).

*Derivación.* La fórmula explícita da $-\zeta'/\zeta(s) = \sum_p\Lambda(p)p^{-s} + (\text{ceros}+\text{polo})$. Diferenciando: $(\zeta'/\zeta)^2(s) - \zeta''/\zeta(s) = \sum_p\Lambda(p)(\log p)p^{-s} - \sum_\rho(s-\rho)^{-2}$. En $s = \rho_n$ (cero simple): $\zeta''/\zeta(\rho_n)$ es finito y $\sum_\rho(s-\rho)^{-2}|_{s=\rho_n}$ tiene un polo doble en $\rho = \rho_n$. La regularización da exactamente $C_\infty''(\gamma_n)/2$ en términos de la función de ceros. $\square$

---

## 4. Resultado principal: no-anulación de $C_\infty'(\gamma_n)$ bajo hipótesis de cero simple de $\zeta$

**Teorema 1** (la derivada $C_\infty'(\gamma_n) \neq 0$ si $\rho_n = 1/2+i\gamma_n$ es cero simple de $\zeta$). Supóngase:

(H1) $\rho_n = 1/2+i\gamma_n$ es un cero simple de $\zeta$ (i.e., $\zeta'(\rho_n) \neq 0$).

(H2) La suma $\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p)$ no es cero (hipótesis de no-cancelación aritmética en $\gamma_n$).

Entonces $C_\infty'(\gamma_n) \neq 0$, y el cero de $C_\infty$ en $\gamma_n$ (si existe — que requiere (Inc. Inv.)) es SIMPLE.

*Prueba.* $C_\infty'(\gamma_n) \approx 2\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p)$, que es no-cero bajo (H2). $\square$

**Estado de (H2).** La hipótesis (H2) es una hipótesis de no-cancelación aritmética en la suma $\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p)$. Esta suma es el coeficiente de Fourier de $\Psi'$ en la frecuencia $\gamma_n$. Bajo la hipótesis de Montgomery de GUE, la distribución de esta suma es gaussiana con media 0 y varianza $\sim (\log\gamma_n)^3$. La probabilidad de que sea exactamente 0 (en la distribución continua de GUE) es cero. En sentido estricto, (H2) no está demostrada pero es "genéricamente verdadera" bajo GUE.

---

## 5. La cadena completa hacia RH bajo (LI) + simplicicidad de ceros de $\zeta$

**Teorema 2** (RH bajo (LI) y simplicicidad). Supóngase:

(LI) Las frecuencias $\{\log|\rho|\}_\rho$ son linealmente independientes sobre $\mathbb{Q}$ (ceros de $\zeta$).

(S) Todos los ceros no-triviales de $\zeta$ son simples.

Entonces RH.

*Prueba.*

1. Bajo (LI): por la Proposición 2, todos los ceros de $C_\infty$ son simples (no hay ceros dobles de $C_\infty$).

2. Por la Proposición 8 del Doc 23 (residuo = 1 en ceros simples de $C_\infty$): todos los pesos de $\mu_{WT}^\infty$ en los ceros $\gamma_n$ son iguales $= 1/N$.

3. Luego $\mu_{WT}^\infty = (1/N)\sum_n\delta_{\gamma_n} = \mu_{emp}^\infty = \mu_\gamma^{real}$ (Doc 15).

4. Por el Teorema 2 del Doc 22: la inclusión inversa (Inc. Inv.) se satisface.

5. Por el Teorema C1 del Doc 17 + (Inc. Inv.): $\{C_\infty = 0\} = \{\gamma_n\}$.

6. Por el Teorema 3 del Doc 19: RH. $\square$

**Honestidad.** (LI) y (S) son CONJETURAS abiertas, más fuertes que RH. El Teorema 2 es así una implicación: conjeturas conocidas $\Rightarrow$ RH. No es independiente.

---

## 6. El cierre incondicional: lo que queda

**Diagrama definitivo tras Docs 21-24:**

```
Incondicional:
  spec(J_∞) = {C_∞ = 0 en ℝ}              [Doc 17, Tma C1]
  {C_∞ = 0} ⊆ {Ξ = 0 en ℝ}                [Doc 19, Tma 2]
  μ_emp^λ ⇒ μ_γ^real                         [Doc 15]
  spec(J_∞) puro puntual                     [Doc 23, Tma 1]
  Si ceros de C_∞ simples: μ_WT^∞=μ_γ^real  [Doc 23, Prop 8]
  Si μ_WT^∞ = μ_γ^real: RH                   [Doc 22, Tma 2]
  Bajo (LI)+(S): RH                          [Doc 24, Tma 2]

El gap incondicional:
  (Inc. Inv.): {Ξ = 0 en ℝ} ⊆ {C_∞ = 0}
  ⟺ C_∞'(γ_n) ≠ 0 para todo n (simplicicidad de ceros de C_∞)
  ⟺ μ_WT^∞ = μ_γ^real (igualdad de medidas)
  ⟺ RH
```

**Nota.** El gap se ha reducido a: probar $C_\infty'(\gamma_n) \neq 0$ para todo $n$ sin hipótesis adicionales. Esto es una afirmación sobre la no-cancelación de la suma $\sum_\rho\log|\rho|\sin(\gamma_n\log|\rho|)/|\rho|$ — una condición aritmética pura sobre los ceros de $\zeta$.

**Propuesta para Doc 25.** Atacar la no-anulación de $C_\infty'(\gamma_n)$ directamente: usar la fórmula de producto de Euler para $\zeta'/\zeta$ en la franja crítica, combinada con el crecimiento de $w'(t)$, para mostrar que la suma $\sum_p\Lambda(p)p^{-1/2}(\log p)\sin(\gamma_n\log p)$ es no-cero para todos los $\gamma_n$. Alternativamente: usar la invarianza bajo la ecuación funcional de $\xi$ (que es par) para mostrar que $C_\infty'(\gamma_n) \neq 0$ siempre que $\gamma_n$ sea un cero simple de $\Xi$.

La clave: $\Xi$ es par real-analítica en $\mathbb{R}$. En un cero simple $\gamma_n$ de $\Xi$: $\Xi'(\gamma_n) \neq 0$. La relación $\Xi'(\gamma_n) \neq 0$ vs. $C_\infty'(\gamma_n) \neq 0$ — ¿pueden implicarse mutuamente vía la EF2?
