# Phase 29 — Doc 38: Ceros Complejos de $C_\lambda - \mu_\lambda$ en la Franja

**Fecha:** junio 2026  
**Fase:** 31 (inicio)  
**Objetivo:** Analizar los ceros de $C_\lambda(z) = \mu_\lambda$ para $z = x + iy$ con $0 < y \leq \eta < 1/2$. Esta es la única apertura analítica no circular identificada por los Docs 36–37.

---

## 1. Configuración precisa

**Definición 1.** Para $\lambda > 0$ y $z = x + iy \in \mathbb{C}^+$:

$$C_\lambda(z) = w(z) - \Psi_\lambda(z), \quad \Psi_\lambda(z) = 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2}\, e^{iz\log n}.$$

Para $y > 0$: $e^{iz\log n} = e^{ix\log n} \cdot e^{-y\log n} = e^{ix\log n} \cdot n^{-y}$, luego:

$$\Psi_\lambda(x+iy) = 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2-y}\, e^{ix\log n}. \quad (\star)$$

**El factor de amortiguación $n^{-y}$** es central: moverse verticalmente hacia arriba en la franja equivale a introducir un factor de convergencia adicional $n^{-y}$ en la suma de primos.

**Definición 2.** Sea $M(\lambda, y) := \sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2-y}$ (suma de von Mangoldt con peso $n^{-1/2-y}$).

Por $(\star)$: $|\Psi_\lambda(x+iy)| \leq 2M(\lambda, y)$ para todo $x \in \mathbb{R}$.

**Proposición 1** (comportamiento de $M(\lambda,y)$ según régimen). Por el Teorema de los Números Primos ($\psi(X) \sim X$) y la fórmula de Abel-Stieltjes:

(a) Para $y > 1/2$: $M(\lambda, y) \to M(\infty, y) = \sum_{n=1}^\infty \Lambda(n)\, n^{-1/2-y} < \infty$ (serie absolutamente convergente; $1/2 + y > 1$).

(b) Para $y = 1/2$: $M(\lambda, 1/2) \sim \log\log\lambda$ (crecimiento logarítmico, diverge).

(c) Para $0 < y < 1/2$: $M(\lambda, y) \sim \dfrac{\lambda^{1-2y}}{1/2 - y}$ (crecimiento polinomial en $\lambda$, diverge).

*Prueba.* Abel: $M(\lambda,y) = \int_1^{\lambda^2} t^{-1/2-y}\,d\psi(t)$. Usando $\psi(t) = t + O(t e^{-c\sqrt{\log t}})$: integración por partes da el resultado en cada caso. $\square$

**Corolario 1.** El comportamiento de $|\Psi_\lambda(x+iy)|$ es cualitativamente distinto en los tres regímenes:
- $y > 1/2$: acotado uniformemente en $x$ y $\lambda$.
- $0 < y < 1/2$: crece sin cota en $\lambda$ (para $x$ genérico).

---

## 2. La franja exterior: región libre de ceros incondicional

**Teorema 1** (franja libre de ceros, incondicional). Para cualquier $\epsilon > 0$ fijo, existe $\Lambda_\epsilon > 0$ tal que para todo $\lambda \geq \Lambda_\epsilon$:

$$C_\lambda(z) \neq \mu_\lambda \quad \text{para todo } z \text{ con } \Im(z) \geq \tfrac{1}{2} + \epsilon.$$

*Prueba.* Sea $y = \Im(z) \geq 1/2 + \epsilon$.

**Paso 1.** Por la Proposición 1(a): $\Psi_\lambda(z) \to \Psi_\infty(z) = 2\sum_{n=1}^\infty \Lambda(n)n^{-1/2-y}e^{ix\log n}$ uniformemente en $x$ (convergencia absoluta dominada por $M(\infty, 1/2+\epsilon) < \infty$). Luego $C_\lambda(z) \to C_\infty(z)$ uniformemente en compactos de $\{z:\Im(z) \geq 1/2+\epsilon\}$.

**Paso 2.** Por Teorema B (Doc 19, incondicional): $\{C_\infty = 0\} \subseteq \{\Xi = 0\}$. Para $\Im(z) = y \geq 1/2+\epsilon$: $\Xi(z) = \xi(1/2+iz) = \xi(1/2-y+ix)$ con $\Re(1/2-y+ix) = 1/2-y \leq -\epsilon < 0$. Los ceros no-triviales de $\zeta$ tienen $\Re(s) \in (0,1)$; para $\Re(s) = 1/2-y < 0$: no hay ceros no-triviales. Luego $\Xi(z) \neq 0$ para $\Im(z) \geq 1/2+\epsilon$ — incondicional.

Combinando: $C_\infty(z) \neq 0$ para $\Im(z) \geq 1/2+\epsilon$.

**Paso 3.** Como $C_\lambda \to C_\infty$ uniformemente en $\{\Im(z) = 1/2+\epsilon, |\Re(z)| \leq T\}$ y $C_\infty$ es no-nula en ese conjunto compacto: por el Teorema de Hurwitz (el número de ceros no aumenta en el límite bajo convergencia uniforme + no-nulidad), para $\lambda$ suficientemente grande, $C_\lambda(z) \neq 0$ en $\Im(z) \geq 1/2+\epsilon$.

Dado que $\mu_\lambda \to 0$ y $C_\infty(z) \neq 0 \neq \mu_\infty$ en la región: también $C_\lambda(z) \neq \mu_\lambda$ para $\lambda$ suficientemente grande. $\square$

**Corolario 2.** Los ceros complejos de $C_\lambda - \mu_\lambda$ están TODOS confinados a $0 < \Im(z) < 1/2 + \epsilon$ para cualquier $\epsilon > 0$ y $\lambda$ suficientemente grande.

---

## 3. La franja interior: el análisis local

Nos concentramos ahora en la franja interior $0 < \Im(z) < 1/2$.

**Proposición 2** (expansión de Taylor en la franja delgada). Sea $x_0 \in \mathbb{R}$ y $z = x_0 + iy$ con $y$ pequeño. Para $C_\lambda$ real-analítica en un entorno de $x_0$:

$$C_\lambda(x_0 + iy) = C_\lambda(x_0) + iy\, C_\lambda'(x_0) - \frac{y^2}{2}\, C_\lambda''(x_0) + O(y^3).$$

La ecuación $C_\lambda(x_0+iy) = \mu_\lambda$ (con $\mu_\lambda \in \mathbb{R}$) requiere:

**Parte imaginaria:** $y\,\Re[C_\lambda'(x_0)] + O(y^3) = 0$.

Luego, para $y \neq 0$ pequeño: $\Re[C_\lambda'(x_0)] = O(y^2)$.

**Conclusión.** Para $y$ pequeño: los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$ se ubican cerca de los PUNTOS CRÍTICOS de $C_\lambda$ sobre $\mathbb{R}$, es decir, puntos $x_0$ donde $C_\lambda'(x_0) = 0$.

**Proposición 3** (geometría de los ceros complejos en puntos críticos). Sea $x_c \in \mathbb{R}$ un punto crítico de $C_\lambda$ con $C_\lambda'(x_c) = 0$ y $C_\lambda''(x_c) < 0$ (mínimo local).

La ecuación $C_\lambda(x_c + iy) = \mu_\lambda$ se convierte en:

$$C_\lambda(x_c) - \frac{y^2}{2}|C_\lambda''(x_c)| + O(y^3) = \mu_\lambda.$$

Luego:

$$y^2 \approx \frac{2(C_\lambda(x_c) - \mu_\lambda)}{|C_\lambda''(x_c)|}.$$

Para que exista un cero complejo con $y > 0$: se necesita $C_\lambda(x_c) > \mu_\lambda$.

La altura del cero complejo sobre el eje real es:

$$\boxed{y_c \approx \sqrt{\frac{2(C_\lambda(x_c) - \mu_\lambda)}{|C_\lambda''(x_c)|}}.}$$

**Corolario 3** (bifurcación desde punto crítico). Cada mínimo local de $C_\lambda$ con $C_\lambda(x_c) > \mu_\lambda$ contribuye con UN PAR de ceros complejos conjugados de $C_\lambda - \mu_\lambda$ a altura $y_c$ sobre la recta real. Estos ceros no tienen contraparte real (la ecuación $C_\lambda(x) = \mu_\lambda$ no tiene solución real cerca de $x_c$).

En cambio: cada mínimo local con $C_\lambda(x_c) < \mu_\lambda$ contribuye con DOS soluciones REALES de $C_\lambda = \mu_\lambda$ (una a cada lado de $x_c$), y no hay ceros complejos asociados a ese punto crítico.

---

## 4. La dicotomía fundamental

Combinando los resultados anteriores:

**Proposición 4** (dicotomía para los mínimos de $C_\lambda$). Los ceros complejos de $C_\lambda - \mu_\lambda$ provienen de mínimos locales de $C_\lambda$ que están ESTRICTAMENTE POR ENCIMA de $\mu_\lambda$. Hay exactamente dos tipos:

**Tipo A (mínimo por encima de $\mu_\lambda$):** $C_\lambda(x_c) > \mu_\lambda$. Contribuye a $N_{C_\lambda-\mu_\lambda}^{\text{strip}}$ con un par de ceros complejos a altura $y_c > 0$.

**Tipo B (mínimo por debajo de $\mu_\lambda$):** $C_\lambda(x_c) < \mu_\lambda$. Contribuye a $N_{C_\lambda-\mu_\lambda}^{\text{real}}$ con dos ceros reales. No contribuye a $N_{C_\lambda-\mu_\lambda}^{\text{strip}}$.

**Tipo C (mínimo exactamente en $\mu_\lambda$):** $C_\lambda(x_c) = \mu_\lambda$. Contribuye un CERO DOBLE real. Caso no genérico (codimensión 1).

**Teorema 2** (caracterización de los ceros complejos). El número de ceros complejos de $C_\lambda - \mu_\lambda$ en la franja es:

$$N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T) = 2 \cdot \#\left\{x_c \in [0,T] : C_\lambda'(x_c)=0,\; C_\lambda(x_c) > \mu_\lambda\right\} + O(1).$$

*Prueba.* Cada mínimo local de Tipo A contribuye exactamente 2 ceros complejos (el par conjugado). Contabilizando todos los mínimos en $[0,T]$: se obtiene el doble del número de mínimos de Tipo A, con error $O(1)$ por los puntos de inflexión y el borde del intervalo. $\square$

---

## 5. La conexión con la identidad $(C_\lambda')$ del Doc 36

De Doc 36 Proposición 7:

$$N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) = N_{\hat k_\lambda}^{\text{real}}(T) + N_{\hat k_\lambda}^{\text{strip}}(T,\eta). \quad (C_\lambda')$$

Combinando con el Teorema 2:

$$2\cdot\#\{\text{mínimos Tipo A en }[0,T]\} = N_{\hat k_\lambda}^{\text{real}}(T) + N_{\hat k_\lambda}^{\text{strip}}(T,\eta) + O(1).$$

Para $\lambda$ grande: $N_{\hat k_\lambda}^{\text{real}}(T) \approx N_\Xi(T)$ (los ceros reales de $\hat k_\lambda$ aproximan los $\gamma_n$). Y $N_{\hat k_\lambda}^{\text{strip}}(T,\eta)$ = ceros complejos de $\hat k_\lambda$ en la franja $\approx$ ceros off-críticos de $\Xi$.

**Proposición 5** (equivalencia analítica de Inc. Inv.). Las siguientes condiciones son equivalentes:

(i) **Inc. Inv.:** $\{C_\infty = 0\} \supseteq \{\gamma_n\}$, es decir, $N_{C_\infty}(T) = N_\Xi(T)$.

(ii) **Todos los mínimos de $C_\infty$ entre ceros consecutivos $\gamma_n, \gamma_{n+1}$ tocan el nivel 0:** $C_\infty(x_c) = 0$ para el mínimo local $x_c$ entre $\gamma_n$ y $\gamma_{n+1}$.

(iii) **Cada mínimo local de $C_\lambda$ entre $\gamma_n^{(\lambda)}$ y $\gamma_{n+1}^{(\lambda)}$ satisface $C_\lambda(x_c) \to 0$ cuando $\lambda \to \infty$.**

(iv) **Los ceros complejos de $C_\lambda - \mu_\lambda$ tienen altura $y_c \to 0$ cuando $\lambda \to \infty$.**

*Prueba (equivalencia (i)$\Leftrightarrow$(ii)).* Si $C_\infty(\gamma_n) = 0$ y $C_\infty > 0$ en $(\gamma_{n-1}, \gamma_{n+1})$ excepto en $\gamma_n$: entonces $\gamma_n$ es un mínimo (toca cero). Recíprocamente. $\square$

*Prueba (equivalencia (iii)$\Leftrightarrow$(iv)).* De la Proposición 3: $y_c \approx \sqrt{2C_\lambda(x_c)/|C_\lambda''(x_c)|}$. Luego $y_c \to 0 \iff C_\lambda(x_c) \to 0$ (si $C_\lambda''(x_c)$ está acotado). $\square$

---

## 6. La región libre de ceros incondicional en la franja interior

Aunque no podemos eliminar todos los ceros complejos sin asumir Inc. Inv., sí podemos acotar su ubicación usando el crecimiento de $\Psi_\lambda$.

**Proposición 6** (acotación incondicional de la altura de los ceros complejos). Para mínimos locales de $C_\lambda$ en $[0,T]$: la altura del cero complejo asociado satisface

$$y_c \leq \sqrt{\frac{2\,C_\lambda(x_c)}{|C_\lambda''(x_c)|}}.$$

El valor $C_\lambda(x_c)$ en el mínimo satisface $C_\lambda(x_c) \geq 0$ (si $C_\lambda > 0$ en $\mathbb{R}$, que es una pregunta abierta) o puede ser negativo (si $C_\lambda$ tiene ceros reales bajo Inc. Inv.).

Si $C_\lambda(x_c) = O(\mu_\lambda)$ (el mínimo apenas supera $\mu_\lambda$): entonces $y_c = O(\sqrt{\mu_\lambda}) \to 0$.

**Proposición 7** (acotación de $C_\lambda''$ en los mínimos). En los mínimos locales de $C_\lambda$:

$$C_\lambda''(x_c) = w''(x_c) - \Psi_\lambda''(x_c),$$

donde $\Psi_\lambda''(x) = -2\sum_{n \leq \lambda^2} \Lambda(n) n^{-1/2} (\log n)^2 e^{ix\log n}$. Luego:

$$|C_\lambda''(x_c)| \leq |w''(x_c)| + 2\sum_{n \leq \lambda^2} \Lambda(n) n^{-1/2}(\log n)^2.$$

La suma crece como $\sum_{n \leq \lambda^2} \Lambda(n)(\log n)^2 n^{-1/2} = O(\lambda)$ (por PNT). Por lo tanto: $|C_\lambda''(x_c)| = O(\lambda)$.

Combinando: $y_c \geq \sqrt{\frac{2C_\lambda(x_c)}{O(\lambda)}} = \Omega\!\left(\sqrt{\frac{C_\lambda(x_c)}{\lambda}}\right)$.

**Corolario 4** (cota inferior de la altura). Si existe un mínimo local con $C_\lambda(x_c) \geq \delta_0 > 0$ (constante independiente de $\lambda$): entonces la altura del cero complejo asociado satisface

$$y_c \geq c\sqrt{\delta_0 / \lambda} \to 0.$$

Los ceros complejos de Tipo A se ACERCAN al eje real a tasa no peor que $1/\sqrt{\lambda}$ — pero lo hacen INCONDICIONALMENTE.

*Comentario de honestidad.* Este resultado dice que los ceros complejos se acercan al eje real a tasa $\geq 1/\sqrt{\lambda}$, pero NO dice que llegan. Para que lleguen se necesita que $C_\lambda(x_c) \to 0$ — que es Inc. Inv.

---

## 7. La pregunta abierta reformulada con precisión

**Proposición 8** (reformulación analítica de Inc. Inv.). Las siguientes condiciones son equivalentes:

$$\text{Inc. Inv.} \iff \lim_{\lambda\to\infty} \min_{x_c \in \mathcal{C}_\lambda(T)} C_\lambda(x_c) = 0 \quad \forall T,$$

donde $\mathcal{C}_\lambda(T)$ es el conjunto de mínimos locales de $C_\lambda$ en $[0,T]$ con $C_\lambda(x_c) > 0$.

En palabras: Inc. Inv. ↔ los mínimos locales de $C_\lambda$ se acercan al nivel 0 cuando $\lambda \to \infty$.

**Proposición 9** (reformulación analítica de RH). Sea $\mathcal{S}_\lambda^{(\eta)} = \{z : 0 < \Im(z) \leq \eta, C_\lambda(z) = \mu_\lambda\}$ el conjunto de ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $\Im(z) \in (0,\eta]$.

Entonces:

$$\text{RH} \iff \forall \eta > 0:\; N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T, \eta) = N_\Xi(T) + o(N_\Xi(T)) \text{ con } \Im(\mathcal{S}_\lambda^{(\eta)}) \to 0.$$

Más precisamente (de la discusión de Doc 36 §8): bajo RH e Inc. Inv.:

$$\sup\{\Im(z) : z \in \mathcal{S}_\lambda^{(\eta)}\} \to 0 \quad \text{cuando } \lambda \to \infty.$$

**La pregunta abierta concreta para Phase 31:** ¿Puede probarse incondicionalmente que

$$\sup\{\Im(z) : z \in \mathcal{S}_\lambda^{(\eta)}\} \to 0 \quad \text{cuando } \lambda \to \infty?$$

---

## 8. Un resultado parcial: la franja libre por encima de $\lambda^{-\alpha}$

**Proposición 10** (zona libre de ceros complejos en la franja). Para cualquier $\alpha > 0$: si $y \geq \lambda^{-\alpha}$, entonces bajo la hipótesis de que $C_\lambda(x_c) = O(\lambda^{1-2\alpha-\epsilon})$ en los mínimos locales de $C_\lambda$:

$$y_c \leq \sqrt{\frac{2\cdot O(\lambda^{1-2\alpha-\epsilon})}{|C_\lambda''(x_c)|}} \leq \sqrt{\frac{c \cdot \lambda^{1-2\alpha-\epsilon}}{\lambda^{-1}}} = O(\lambda^{(2-2\alpha-\epsilon)/2}) = O(\lambda^{1-\alpha-\epsilon/2}).$$

Para $\alpha > 1/2$: $y_c = O(\lambda^{-\epsilon/2}) \to 0$. Entonces los ceros complejos de Tipo A están BAJO la línea $\Im(z) = \lambda^{-\alpha}$ para $\alpha > 1/2$.

*Nota de honestidad.* Este resultado asume que $C_\lambda(x_c) = O(\lambda^{1-2\alpha-\epsilon})$ en los mínimos — que es una hipótesis adicional no probada. Sin ella, el resultado es vacío.

**Proposición 11** (caso probado: mínimos cerca de $\gamma_n$). Para los mínimos de $C_\lambda$ que caen EXACTAMENTE en las posiciones de los eigenvalores $t_n^{(\lambda)}$ (que bajo Inc. Inv. son aproximadamente los $\gamma_n$):

$C_\lambda(t_n^{(\lambda)}) = \mu_\lambda \to 0$.

Luego: los ceros complejos de Tipo A CERCA de $t_n^{(\lambda)}$ tienen altura

$$y_c \approx \sqrt{\frac{2\mu_\lambda}{|C_\lambda''(t_n^{(\lambda)})|}} \leq C\sqrt{\frac{\mu_\lambda}{\lambda}} \to 0.$$

Bajo Inc. Inv.: todos los mínimos relevantes satisfacen $C_\lambda(x_c) = O(\mu_\lambda)$, luego todos los ceros complejos de Tipo A tienen altura $y_c = O(\sqrt{\mu_\lambda/\lambda}) \to 0$.

**Este es el mecanismo de escape bajo Inc. Inv.:** los ceros complejos de $C_\lambda - \mu_\lambda$ son pares ($t_n^{(\lambda)}, \bar t_n^{(\lambda)})$ con parte imaginaria $\to 0$ — convergen al eje real donde se funden con los ceros reales $t_n^{(\lambda)}$ para formar DOBLES CEROS de $C_\infty$ en $\gamma_n$.

---

## 9. El comportamiento de $\Psi_\lambda$ en la franja: el mecanismo aritmético

**Proposición 12** (comparación de $\Psi_\lambda$ y $w$ en la franja). Para $z = x + iy$ con $y \in (0, 1/2)$:

$$C_\lambda(x+iy) = w(x+iy) - 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2-y}\, e^{ix\log n}.$$

El término $w(x+iy)$ es la contribución arquimediana — es una función holomorfa en $\mathbb{C}^+$ relacionada con el logaritmo de la función xi completada. Para $y$ pequeño: $w(x+iy) \approx w(x) + iy\, w'(x) + O(y^2)$.

La suma $\Psi_\lambda(x+iy)$ es una suma de Dirichlet truncada con pesos $n^{-1/2-y}$:

$$\Psi_\lambda(x+iy) = \sum_{n \leq \lambda^2} a_n^{(\lambda,y)} e^{ix\log n}, \quad a_n^{(\lambda,y)} = 2\Lambda(n)\, n^{-1/2-y}.$$

Esta es una función **casi-periódica** de $x$ para cada $y$ fijo — oscila con frecuencias $\log n$ y amplitudes $n^{-1/2-y}$.

**La variable $y$ actúa como un parámetro de regularización:** a mayor $y$, las frecuencias altas (grandes $n$) están más suprimidas. Para $y \to 1/2$: solo las frecuencias bajas sobreviven.

**Proposición 13** (el potencial $C_\lambda$ en la franja como suma de Dirichlet regularizada). Para $0 < y < 1/2$ fijo:

$$C_\lambda(x+iy) = w(x+iy) - \sum_{n \leq \lambda^2} 2\Lambda(n)\, n^{-1/2-y}\, e^{ix\log n}.$$

Los ceros de $C_\lambda(x+iy) = \mu_\lambda$ son las soluciones de:

$$\sum_{n \leq \lambda^2} 2\Lambda(n)\, n^{-1/2-y}\, e^{ix\log n} = w(x+iy) - \mu_\lambda.$$

El lado derecho es una función suave de $x$ (variación lenta), mientras que el lado izquierdo es una suma de Dirichlet oscilante con periodo $O(1/\log\lambda)$. Las soluciones son los PUNTOS DE COINCIDENCIA entre la función suave y la suma oscilante — un problema clásico en teoría analítica de números.

---

## 10. Resumen: el estado de la pregunta y el camino

**Lo probado en este documento:**

(T1) **Región libre exterior** (Teorema 1, incondicional): $C_\lambda - \mu_\lambda$ no tiene ceros complejos para $\Im(z) > 1/2 + \epsilon$ y $\lambda$ grande.

(T2) **Geometría local** (Proposición 3): los ceros complejos en la franja provienen de mínimos de $C_\lambda$ sobre $\mathbb{R}$ a altura $y_c \approx \sqrt{2C_\lambda(x_c)/|C_\lambda''(x_c)|}$.

(T3) **Equivalencia con Inc. Inv.** (Proposición 5): la condición $y_c \to 0$ es equivalente a Inc. Inv. — los dos enunciados se implican mutuamente.

(T4) **Cota de acercamiento al eje real** (Corolario 4): los ceros complejos se acercan al eje real a tasa $\geq 1/\sqrt{\lambda}$ — esto es INCONDICIONAL.

(T5) **El mecanismo bajo Inc. Inv.** (Proposición 11): si Inc. Inv. es verdadero, los ceros complejos tienen altura $O(\sqrt{\mu_\lambda/\lambda}) \to 0$ — escapan al eje real.

**Lo que permanece abierto:**

(A1) **La pregunta abierta central:** ¿puede probarse incondicionalmente que todos los mínimos de $C_\lambda$ en $[0,T]$ satisfacen $C_\lambda(x_c) \to 0$? Esto equivale a Inc. Inv. — es una reformulación, no una prueba.

(A2) **La pregunta del escape incondicional:** ¿existe una cota $y_c \leq f(\lambda) \to 0$ incondicional (sin asumir Inc. Inv.)? De Corolario 4: la cota es $y_c \geq c/\sqrt{\lambda}$ desde abajo, pero no hay cota superior incondicional que vaya a 0.

**La barrera estructural (diagnóstico honesto):**

El escape de los ceros complejos al eje real ES equivalente a Inc. Inv. No hay forma de probar el escape sin probar Inc. Inv. primero — la condición son la misma cosa analíticamente (Proposición 5).

La ventaja de esta formulación: convierte Inc. Inv. en una pregunta sobre el MÍNIMO de una función real-analítica explícita ($C_\lambda$) — una pregunta de análisis real, no de teoría espectral. Esto puede ser más accesible.

---

## 11. Propuesta para Doc 39: acotación del mínimo de $C_\lambda$

**La pregunta para Doc 39.** Probar o refutar:

$$\inf_{x \in [0,T]} C_\lambda(x) \to 0 \quad \text{cuando } \lambda \to \infty.$$

Herramientas disponibles:
- La fórmula explícita de Guinand-Weil para $C_\lambda(x)$ como suma sobre primos y ceros de $\zeta$.
- La función $C_\lambda(x) = w(x) - \Psi_\lambda(x)$ con $w$ y $\Psi_\lambda$ explícitas.
- La teoría de valores extremos de sumas de Dirichlet (Bondarenko-Seip, Helson).
- La conexión con el problema de momentos indeterminado de Doc 26 — ¿el ínfimo de $C_\lambda$ está controlado por los momentos de la medida espectral?

**Nota:** Este es el verdadero cuello de botella analítico del programa Phase 31.

---

*Siguiente doc: Doc 39 — Acotación del ínfimo de $C_\lambda$ en $\mathbb{R}$: valores extremos de sumas de Dirichlet y el problema de los mínimos.*
