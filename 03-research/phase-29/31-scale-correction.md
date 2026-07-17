# Phase 29 — Doc 31: Corrección del Error de Escala del Doc 30 — $b_n \neq 0$

**Fecha:** junio 2026  
**Objeto:** El Doc 30 estableció un "problema de escala" basado en que $\|J_\infty\|_{op} \leq 2\pi/\log\gamma_0 \approx 2.36$, concluyendo que $\gamma_n \notin \text{spec}(J_\infty)$. Este doc corrige ese error: el Doc 30 asumió erróneamente que $b_n^\infty = 0$.

---

## 1. La corrección del Doc 30: $b_n^\infty \approx \gamma_n$

**El error del Doc 30.** La Proposición 1 del Doc 30 afirmó "$J_\infty$ con $a_n^\infty = \pi/\log\gamma_n$ y $b_n^\infty = 0$ es compacto con norma $\approx 2.36$". El error está en $b_n^\infty = 0$.

**La lectura correcta del Doc 15 (Parte C y Teorema 1).** Para el régimen local de los coeficientes de Jacobi del CCM:

$$b_n^{(\lambda)} \approx \frac{\gamma_n + \gamma_{n+1}}{2} \approx \gamma_n + O\!\left(\frac{1}{\log\gamma_n}\right), \quad a_n^{(\lambda)} \approx \frac{\gamma_{n+1}-\gamma_n}{2} \approx \frac{\pi}{\log\gamma_n}.$$

En el límite $\lambda\to\infty$ (con $n$ fijo): $b_n^\infty \approx \gamma_n$ (grande, diverge con $n$) y $a_n^\infty \approx \pi/\log\gamma_n \to 0$ (pequeño).

**La medida espectral de $J_\infty$.** El operador $J_\infty$ con $b_n = \gamma_n$ y $a_n = \pi/\log\gamma_n$ tiene sus eigenvalores en los $\gamma_n$ (aproximadamente), y la media espectral es $\mu_\gamma^{real}$. Esto es consistente con la escala (los $\gamma_n$ son los eigenvalores, del orden de 14, 21, ...).

---

## 2. El operador $J_\infty$ correcto: no-acotado

**Proposición 1** (correcta). El operador $J_\infty$ con $b_n^\infty = \gamma_n$ (ceros de $\Xi$) y $a_n^\infty = \pi/\log\gamma_n$ es:

(a) **No-acotado**: $\|J_\infty\|_{op} = \infty$ pues $b_n \to \infty$.

(b) **Esencialmente auto-adjunto** sobre $D_0 = \{u \in \ell^2: \sum_n n|u_n|^2 < \infty\}$: pues los b_n crecen como $\gamma_n \sim n\log n$ (por PNT), que está en la clase de Carleman.

(c) **Espectro puntual puro** (si los $\gamma_n$ son eigenvalores simples): los $a_n = \pi/\log\gamma_n \to 0$ dan pequeñas perturbaciones off-diagonal; los eigenvalores de $J_\infty$ se aproximan a los de la parte diagonal (los $\gamma_n$), perturbados por los $a_n$.

(d) **La norma de la perturbación off-diagonal**: $\|J_\infty - \text{diag}(\gamma_n)\|_{op} \leq 2\sup_n a_n^\infty = 2\pi/\log\gamma_0 \approx 2.36$.

*Prueba.* (a) $\sup_n |b_n| = \sup_n \gamma_n = \infty$. (b) Carleman: $\sum_n 1/b_n = \sum_n 1/\gamma_n$ converge (pues $\gamma_n > 14n$ para todo $n$), así que $J_\infty$ tiene dominio natural. (c) y (d) directos. $\square$

---

## 3. La estructura perturbativa: $J_\infty = D + P$

**Descomposición.** Sea $D = \text{diag}(\gamma_n)$ (el operador diagonal con los $\gamma_n$ en la diagonal) y $P$ la perturbación off-diagonal con $P_{n,n+1} = P_{n+1,n} = a_n^\infty = \pi/\log\gamma_n$ (todo lo demás cero).

$$J_\infty = D + P, \quad \|P\|_{op} \leq 2\pi/\log\gamma_0 \approx 2.36.$$

**Proposición 2** (perturbación pequeña relativa al spacing). El radio de perturbación $\|P\|_{op} \approx 2.36$ es comparable al espaciado mínimo $\gamma_1 - \gamma_0 \approx 21.0 - 14.1 = 6.9$. La perturbación $P$ tiene norma menor que el gap mínimo del espectro de $D$:

$$\|P\|_{op} \approx 2.36 < \frac{\gamma_1 - \gamma_0}{2} \approx 3.45.$$

Luego: los eigenvalores de $J_\infty$ están BIEN SEPARADOS y próximos a los de $D$ (i.e., a los $\gamma_n$).

*Prueba.* Para $n\geq 0$: $a_n = \pi/\log\gamma_n$ y $(\gamma_{n+1}-\gamma_n)/2 = a_n$ (que es la misma cantidad). Luego la perturbación off-diagonal tiene exactamente la magnitud del half-spacing, y la teoría de perturbaciones de Weyl garantiza que los eigenvalores de $J_\infty$ están en los intervalos $[\gamma_n - a_n, \gamma_n + a_n]$ (para $a_n$ pequeño relativo al siguiente gap). $\square$

---

## 4. La reanalisis de Inc. Inv. con $b_n \approx \gamma_n$

**Proposición 3** (reformulación de Inc. Inv. con $b_n \approx \gamma_n$). Con el correcto $b_n^\infty = \gamma_n + \epsilon_n$ (donde $\epsilon_n = O(1/\log\gamma_n)$ es una corrección pequeña):

Los eigenvalores de $J_\infty$ son $\tilde\gamma_n = \gamma_n + \delta_n$ donde $|\delta_n| \leq \|P\|_{op}\cdot\|R_n\|$ (la perturbación del eigenvalor $\gamma_n$ de $D$).

Inc. Inv. es la condición: $\tilde\gamma_n = \gamma_n$ para todo $n$ (los eigenvalores de $J_\infty$ coinciden exactamente con los $\gamma_n$, no con algún desplazamiento $\delta_n \neq 0$).

**Proposición 4** (la EF2 con $b_n \approx \gamma_n$). La EF2 del Doc 17:

$$N\cdot m_\infty^{WT}(z) = \frac{C_\infty'(z)}{C_\infty(z)}$$

sigue siendo válida con el operador $J_\infty$ correcto (con $b_n = \gamma_n$). Los eigenvalores de $J_\infty$ son los polos de $m_\infty^{WT}$, que son los ceros de $C_\infty$.

Inc. Inv. dice: los ceros de $C_\infty$ en $\mathbb{R}$ son exactamente los $\gamma_n$.

Con el correcto $b_n = \gamma_n$: el espectro de $J_\infty$ (los eigenvalores $\tilde\gamma_n$) está en el rango $[\gamma_n - 2.36, \gamma_n + 2.36]$ para cada $n$. Inc. Inv. requiere que $\tilde\gamma_n = \gamma_n$ exactamente (sin desplazamiento).

---

## 5. La teoría de perturbaciones exacta para la condición $\tilde\gamma_n = \gamma_n$

**Teorema 1** (condición de punto fijo perturbativo). El eigenvalor $\tilde\gamma_n$ de $J_\infty = D + P$ satisface la ecuación implícita (Teorema de Kato-Rellich):

$$\tilde\gamma_n = \gamma_n + \sum_{k\neq n}\frac{|P_{nk}|^2}{\gamma_n - \gamma_k} + O\!\left(\|P\|^4/\text{gap}^3\right) = \gamma_n + a_{n-1}^2 A_{n-1} + a_n^2 B_n + O(\|P\|^4),$$

donde $A_{n-1} = 1/(\gamma_n - \gamma_{n-1}) + \ldots$ y $B_n = 1/(\gamma_n - \gamma_{n+1}) + \ldots$ son las contribuciones del segundo orden de la teoría de perturbaciones.

La condición $\tilde\gamma_n = \gamma_n$ (eigenvalor no desplazado) requiere:

$$a_{n-1}^2\cdot\frac{1}{\gamma_n-\gamma_{n-1}} + a_n^2\cdot\frac{1}{\gamma_n-\gamma_{n+1}} + \text{correcciones} = 0.$$

**Proposición 5** (la condición de no-desplazamiento como ecuación entre ceros). Con $a_{n-1} = \pi/\log\gamma_{n-1}$ y $a_n = \pi/\log\gamma_n$, y $\gamma_n - \gamma_{n-1} \approx 2\pi/\log\gamma_{n-1}$ y $\gamma_n - \gamma_{n+1} \approx -2\pi/\log\gamma_n$:

$$\text{Corrección de 2° orden} = \frac{(\pi/\log\gamma_{n-1})^2}{2\pi/\log\gamma_{n-1}} - \frac{(\pi/\log\gamma_n)^2}{2\pi/\log\gamma_n} = \frac{\pi}{2\log\gamma_{n-1}} - \frac{\pi}{2\log\gamma_n}.$$

Para $n$ grande: $\pi/(2\log\gamma_{n-1}) - \pi/(2\log\gamma_n) \approx \pi/(2\log\gamma_n) - \pi/(2\log\gamma_n) + O(1/(\log\gamma_n)^2 \cdot 1/n) \to 0$.

Luego: la corrección de segundo orden es $O(1/(n(\log n)^2)) \to 0$. Los eigenvalores de $J_\infty$ son $\tilde\gamma_n = \gamma_n + O(1/(n(\log n)^2))$.

---

## 6. El resultado perturbativo: los eigenvalores convergen a los $\gamma_n$

**Teorema 2** (eigenvalores de $J_\infty$ son asintóticamente $\gamma_n$). Con $b_n = \gamma_n$ y $a_n = \pi/\log\gamma_n$:

$$\tilde\gamma_n = \gamma_n + O\!\left(\frac{1}{n(\log n)^2}\right) \quad \text{cuando } n\to\infty.$$

En particular: $\tilde\gamma_n \to \gamma_n$ como $n\to\infty$ (los eigenvalores se aproximan a los $\gamma_n$ para $n$ grande).

*Prueba.* De la Proposición 5: la corrección de 2° orden es $O(1/(n\log^2 n))$. Las correcciones de orden superior son $O(\|P\|^4/\text{gap}^3) = O(a_n^4/(\gamma_{n+1}-\gamma_n)^3) = O(1/(\log n)^4/n^3) = O(1/(n^3\log^4 n))$ — negligible. $\square$

**La distinción entre asintótico y exacto.** El Teorema 2 dice que $\tilde\gamma_n - \gamma_n \to 0$, pero no que $\tilde\gamma_n = \gamma_n$ EXACTAMENTE. El gap Inc. Inv. es exactamente si $\tilde\gamma_n = \gamma_n$ (no solo asintóticamente). La teoría de perturbaciones solo da una aproximación; la condición exacta requiere que TODOS los términos de la serie se cancelen.

---

## 7. La condición exacta de no-desplazamiento

**Proposición 6** (condición exacta para $\tilde\gamma_n = \gamma_n$). El eigenvalor de $J_\infty$ es exactamente $\gamma_n$ (sin desplazamiento) si y solo si la ecuación de resolución:

$$\gamma_n \text{ es eigenvalor de } J_\infty \iff (J_\infty - \gamma_n) u = 0 \text{ tiene solución } u \in \ell^2(\mathbb{N})$$

tiene solución. Esto equivale a: la solución de la recurrencia

$$a_{n-1}^\infty u_{n-1} + b_n^\infty u_n + a_n^\infty u_{n+1} = \gamma_n u_n, \quad \text{i.e.,} \quad a_{n-1}^\infty u_{n-1} + a_n^\infty u_{n+1} = (\gamma_n - b_n^\infty) u_n,$$

con $b_n^\infty = \gamma_n$ es:

$$a_{n-1}^\infty u_{n-1} + a_n^\infty u_{n+1} = 0.$$

En el caso $b_n^\infty = \gamma_n$ EXACTAMENTE: la ecuación en el punto $n$ es $a_{n-1}u_{n-1} + a_n u_{n+1} = 0$, que da $u_{n+1} = -(a_{n-1}/a_n) u_{n-1}$.

**El sistema de recurrencias con $b_n = \gamma_n$.** La ecuación $(J_\infty - \gamma_n)u = 0$ en componentes:

Para $k \neq n$: $a_{k-1} u_{k-1} + a_k u_{k+1} = (\gamma_n - \gamma_k) u_k$.

Para $k = n$: $a_{n-1} u_{n-1} + a_n u_{n+1} = 0$.

La ecuación en $k = n$ da una relación entre $u_{n-1}$ y $u_{n+1}$: $u_{n+1} = -(a_{n-1}/a_n) u_{n-1} = -(\log\gamma_n/\log\gamma_{n-1}) u_{n-1}$. Para $n$ grande: $(a_{n-1}/a_n) = \log\gamma_n/\log\gamma_{n-1} \approx 1 + (\log\gamma_n - \log\gamma_{n-1})/\log\gamma_{n-1} \approx 1 + (\log p_n)/\log\gamma_{n-1}$ (donde $p_n$ es el "log-ratio" de ceros consecutivos) — muy cercano a 1 para $n$ grande.

La relación $u_{n+1} \approx -u_{n-1}$ (para $n$ grande) impone una condición de REFLEXIÓN en el paso $n$: el eigenvector se "refleja" alrededor del índice $n$.

**El análisis local de la eigenfunción.** Para $k < n$ (lejos de $n$): la ecuación $(J_\infty - \gamma_n) u = 0$ tiene el factor $(\gamma_n - \gamma_k) > 0$ en el término derecho. Esta es una ecuación de tipo Schrödinger con potencial $V(k) = \gamma_k - \gamma_n$ (negativo para $k < n$, positivo para $k > n$). El nivel $\gamma_n$ está en el "nivel de energía" que separa los dos regímenes.

Cerca del índice $n$ (donde $V(k) = \gamma_k - \gamma_n \approx (k-n) \cdot \gamma_n'$): la recurrencia se comporta como una ecuación diferencial de tipo oscilador armónico localizado — el eigenvector se localiza alrededor del índice $n$.

---

## 8. La condición de cuadratura: $b_n = \gamma_n$ exacto vs. aproximado

El resultado clave del Doc 15 dice:

$$b_n^{(\lambda)} \approx \gamma_n + O(1/\log\gamma_n).$$

La corrección $O(1/\log\gamma_n)$ en $b_n$ vs. la perturbación off-diagonal $a_n = \pi/\log\gamma_n$: ambos son del mismo orden. La condición "$b_n = \gamma_n$ exactamente" requiere que la corrección $O(1/\log\gamma_n)$ sea exactamente cero.

**Proposición 7** (Inc. Inv. y la corrección en $b_n$). Los eigenvalores de $J_\infty$ son exactamente $\gamma_n$ iff $b_n^\infty = \gamma_n$ exactamente Y la solución de la recurrencia con $b_n = \gamma_n$ es $\ell^2$.

La condición $b_n^\infty = \gamma_n$ exactamente (sin corrección $O(1/\log\gamma_n)$) ES EQUIVALENTE a que los eigenvalores de $J_\lambda^N$ converjan a $\gamma_n$ con corrección cero — que es Inc. Inv.

En otras palabras: Inc. Inv. ↔ $b_n^{(\lambda)} \to \gamma_n$ (con la corrección $\epsilon_n \to 0$) ↔ $J_\infty$ tiene eigenvalores exactamente en $\gamma_n$.

---

## 9. Diagnóstico final corregido

**Corrección al Doc 30.** El "problema de escala" del Doc 30 era ficticio: se basó en $b_n = 0$ cuando en realidad $b_n \approx \gamma_n$. Con el correcto $b_n = \gamma_n$, el operador $J_\infty$ es no-acotado y tiene eigenvalores en la escala de los $\gamma_n$.

**Estado del programa post-corrección.** La EF2 del Doc 17 aplica al operador $J_\infty$ no-acotado con $b_n = \gamma_n$, $a_n = \pi/\log\gamma_n$. Inc. Inv. requiere:

$$\text{spec}(J_\infty) = \{\gamma_n\}, \quad \text{i.e., los eigenvalores son exactamente los }\gamma_n \text{ (sin desplazamiento)}.$$

Por el Teorema 2: los eigenvalores son $\gamma_n + O(1/(n\log^2 n))$ — muy próximos pero no exactamente iguales a los $\gamma_n$ en general. Inc. Inv. requiere que el error sea exactamente cero.

**El gap reformulado (post-corrección).** Inc. Inv. es la condición:

$$\forall n: \tilde\gamma_n = \gamma_n \iff C_\infty(\gamma_n) = 0 \iff \text{la suma de perturbaciones de todos los ordenes se cancela exactamente}.$$

Esta cancelación exacta, en ausencia de una razón estructural (como simetría global), es una condición no-trivial que no está garantizada por la estructura del operador solo — requiere la fórmula explícita o algún principio analítico adicional.

**El camino más prometedor (sintetizando los Docs 27-31).** La única vía que no ha sido cerrada es el **Frente B** propuesto en el Doc 28: la función $C_\infty(t) = w(t) - \Psi(t)$ como función quasi-periódica. Su relación con el operador $J_\infty$ (ahora correctamente entendido como no-acotado con $b_n = \gamma_n$) es exactamente la EF2. La pregunta de si $C_\infty(\gamma_n) = 0$ para todos los $\gamma_n$ podría responderse estudiando la distribución de valores de $C_\infty$ en los puntos $\gamma_n$ usando la ergodía de funciones quasi-periódicas y el comportamiento estadístico del sistema de ceros de $\zeta$.
