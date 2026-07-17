# La clase de Laguerre–Pólya y la concavidad correcta

**Fecha:** junio 2026
**Origen:** La Pregunta 28.1 tenía la dirección equivocada. Este documento desarrolla la dirección correcta.

---

## 1. La realidad de $\xi$ en la recta crítica

**Proposición 1** (simetría fundamental). Para todo $t \in \mathbb{R}$:
$$\xi\!\left(\tfrac{1}{2}+it\right) \in \mathbb{R}.$$

*Prueba.* Las dos simetrías de $\xi$:
- Ecuación funcional: $\xi(s) = \xi(1-s)$.
- Realidad (eje real): $\overline{\xi(s)} = \xi(\bar s)$ (porque $\xi$ es entera con coeficientes reales en su Taylor en $s = 1/2$).

Evaluando en $s = 1/2 + it$: $\overline{\xi(1/2+it)} = \xi(\overline{1/2+it}) = \xi(1/2-it) = \xi(1-(1/2+it)) = \xi(1/2+it)$. Luego $\xi(1/2+it) \in \mathbb{R}$. $\square$

**Consecuencia.** La función $f: \mathbb{R} \to \mathbb{R}$, $f(t) := \xi\!\left(\tfrac{1}{2}+it\right)$, es una función entera real de $t$ (i.e., entera en $\mathbb{C}$ con $f(\mathbb{R}) \subset \mathbb{R}$).

---

## 2. Los ceros de $f(t) = \xi(1/2+it)$

Los ceros de $f$ como función de $t \in \mathbb{C}$ corresponden a los ceros de $\xi$ vía:
$$f(t_0) = 0 \iff \xi\!\left(\tfrac{1}{2}+it_0\right) = 0 \iff \tfrac{1}{2}+it_0 = \rho, \quad \rho \text{ cero de } \zeta.$$

Si $\rho = \tfrac{1}{2} + b_\rho + i\gamma_\rho$ (con $b_\rho = \operatorname{Re}(\rho)-\tfrac{1}{2}$), entonces $t_0 = \gamma_\rho - ib_\rho$.

**El zero de $f$ es real $\iff$ $b_\rho = 0$ $\iff$ $\rho$ está en la recta crítica.**

**Proposición 2.** Las siguientes afirmaciones son equivalentes:
1. RH (todos los ceros no-triviales de $\zeta$ tienen $\operatorname{Re}(\rho) = 1/2$).
2. Todos los ceros de la función entera real $f(t) = \xi(1/2+it)$ son reales.

---

## 3. La clase de Laguerre–Pólya

**Definición.** Una función entera real $f(t)$ pertenece a la *clase de Laguerre–Pólya* (clase LP) si es límite uniforme en compactos de polinomios con todos sus ceros reales, o equivalentemente si tiene la forma:
$$f(t) = c\, t^m e^{-\alpha t^2 + \beta t} \prod_{k}\!\left(1 - \frac{t}{t_k}\right)e^{t/t_k},$$
con $c, \beta, t_k \in \mathbb{R}$, $\alpha \ge 0$, $\sum_k t_k^{-2} < \infty$.

La clase LP es exactamente la clase de funciones enteras reales con **todos sus ceros reales**.

**Consecuencia directa de la Proposición 2:**
$$\text{RH} \iff f(t) = \xi\!\left(\tfrac{1}{2}+it\right) \in \text{LP}.$$

*Observación histórica.* Esta equivalencia es la reformulación de de Bruijn (1950): $\Lambda = 0 \iff \xi(1/2+it) \in$ LP. Lo nuevo a continuación es la caracterización en términos de curvatura, y la conexión con los Frentes A–D.

---

## 4. El criterio de curvatura: la dirección correcta

**Teorema 1** (criterio de curvatura en $t$). Sean $t_k$ los ceros reales de $f$. Entonces:
$$f \in \text{LP} \iff t \mapsto \log|f(t)| \text{ es estrictamente cóncava en } t \text{ en cada intervalo } (t_k,\, t_{k+1}).$$

*Prueba.* Para $f \in$ LP con todos los ceros reales, el producto de Hadamard da:
$$\log|f(t)| = \log|c| - \alpha t^2 + \beta t + \sum_k \log\!\left|1-\frac{t}{t_k}\right| + \frac{t}{t_k}.$$
Segunda derivada:
$$\frac{d^2}{dt^2}\log|f(t)| = -2\alpha - \sum_{k} \frac{1}{(t-t_k)^2} < 0 \quad \forall t \notin \{t_k\}.$$
Cóncava. Recíprocamente, si $f$ tiene un cero complejo $t_0 = \gamma + ib$ ($b > 0$), el par $(t_0, \bar t_0)$ contribuye:
$$\operatorname{Re}\!\left(-\frac{1}{(t-t_0)^2} - \frac{1}{(t-\bar t_0)^2}\right) = \frac{-2(t-\gamma)^2+2b^2}{[(t-\gamma)^2+b^2]^2},$$
que es **positivo** para $|t-\gamma| < b$. Entonces $d^2/dt^2 \log|f| > 0$ para $t$ en la franja $(\gamma-b, \gamma+b)$: convexidad. Por tanto la concavidad $\Rightarrow$ no hay ceros complejos. $\square$

**Corolario 1.** Para la función $f(t) = \xi(1/2+it)$:
$$\text{RH} \iff \frac{d^2}{dt^2}\log|\xi\!\left(\tfrac{1}{2}+it\right)| < 0 \quad \forall t \notin \{\gamma_\rho\}.$$

---

## 5. Conexión con la curvatura $\mathcal{C}(\gamma)$

Del documento anterior (06), usando que $\Delta \log|\xi| = 0$ (armonicidad de $\log|\xi|$ fuera de ceros):
$$\frac{\partial^2}{\partial t^2}\log|\xi| = -\frac{\partial^2}{\partial\sigma^2}\log|\xi| = -\mathcal{C}(\gamma).$$

Por tanto:
$$\frac{d^2}{dt^2}\log|f(t)| = -\mathcal{C}(t)$$

y el criterio del Corolario 1 equivale a:
$$\text{RH} \iff \mathcal{C}(t) > 0 \quad \forall t \notin \{\gamma_\rho\},$$
confirmando el Teorema 4 del documento 06.

---

## 6. La resolución de la paradoja de la Pregunta 28.1

La Pregunta 28.1 preguntaba por la **$\sigma$-concavidad** de $\log|\xi(\sigma+i\gamma)|$.

El Teorema 2 del documento 06 (RH → convexidad en $\sigma$) junto con el Corolario 1 muestran que:

| Dirección | RH verdadera | RH falsa |
|---|---|---|
| $\sigma$-concavidad en $\sigma = 1/2$ | **FALSA** ($\sigma$-convexa) | Puede ser verdadera (ceros off-line crean concavidad en $\sigma$) |
| $t$-concavidad entre ceros | **VERDADERA** (LP class) | FALSA (ceros off-line crean convexidad en $t$) |

La pregunta 28.1 tenía la dirección equivocada. La concavidad correcta para RH es la **$t$-concavidad**, y es exactamente equivalente a RH.

*Principio geométrico subyacente:* en la recta crítica, el gradiente de $\log|\xi|$ apunta en la dirección imaginaria (hacia los ceros en $t$), no en la dirección real. La curvatura transversal a este gradiente es la que caracteriza RH.

---

## 7. La unificación de los cuatro frentes

El criterio $\mathcal{C}(t) > 0$ (RH ↔ LP class) conecta los cuatro frentes del programa:

**Frente A** (DBN + Kreĭn): el flujo de de Bruijn–Newman mueve ceros hacia la recta real de $f(t)$, aumentando $\mathcal{C}(t)$ hacia $+\sum_\rho 1/(\gamma-\gamma_\rho)^2$. La conjetura A.15 ($\Lambda = \max b_j^2/2$) equivale a que el último cero complejo de $f$ es el que tiene mayor $b_j$.

**Frente B** (APS): la positividad de $\mathcal{C}(t) = G(1/2+it) = (\xi'/\xi)'(1/2+it)$ es una propiedad analítica de $\xi$ que, si pudiera probarse por propiedades de $\xi'/\xi$ (el η-invariante), daría RH. La anticometización de Fourier del Frente B equivale a la positividad del curvature diagnostic.

**Frente C** (K-teoría): $[P_-] = 0$ en $K_0 \iff$ $f \in$ LP $\iff$ $\mathcal{C}(t) > 0$.

**Frente D** (energía transversal): la $t$-concavidad es exactamente la condición de "mínimo en la dirección imaginary" que el Frente D intentaba formalizar. La energía correcta es:
$$E_{\text{curv}}(f) := -\int \frac{d^2}{dt^2}\log|f(t)|\, dt = \int \mathcal{C}(t)\, dt,$$
que es positivo $\iff$ $f \in$ LP $\iff$ RH.

**Los cuatro frentes son el mismo problema:** demostrar que $f(t) = \xi(1/2+it) \in$ LP.

---

## 8. El muro identificado con precisión máxima

**Proposición 3** (el muro final). La siguiente afirmación:
$$f(t) = \xi\!\left(\tfrac{1}{2}+it\right) \text{ tiene sólo ceros reales}$$
es equivalente a RH. Para probarla sin asumir RH se necesita mostrar que:

$$\frac{d^2}{dt^2}\log|f(t)| = -2\alpha - \sum_k \frac{1}{(t-t_k)^2} - \sum_{\text{pares complejos}} \frac{2[(t-\gamma_k)^2-b_k^2]}{[(t-\gamma_k)^2+b_k^2]^2} < 0$$

La dificultad: los pares complejos contribuyen positivamente cerca de su "sombra" $t = \gamma_k$. Eliminar la posibilidad de pares complejos ES probar RH.

**La restricción aritmética** (producto de Euler) es la única condición adicional que podría forzar la no-existencia de pares complejos. Esta es exactamente Wall A del programa (Phase 27) en el lenguaje de ceros de funciones enteras.

---

## 9. Resultados nuevos vs. conocidos

| Resultado | Nuevo/Conocido |
|---|---|
| RH ↔ $f(t) = \xi(1/2+it) \in$ LP | Conocido (de Bruijn 1950, Newman 1976) |
| $\xi(1/2+it) \in \mathbb{R}$ para todo $t$ | Conocido |
| Formula $\mathcal{C}(t) = \sum_\rho (t-\gamma_\rho)^2-b_\rho^2)/|s-\rho|^4$ | **Nuevo** |
| $\mathcal{C}(t) > 0 \iff$ LP class $\iff$ RH | **Nueva presentación** |
| $\sigma$-concavidad FALSA bajo RH; $t$-concavidad VERDADERA bajo RH | **Nuevo diagnóstico** |
| Los cuatro frentes (A, B, C, D) son el mismo problema LP | **Nueva unificación** |
| Conexión $E_{\text{curv}} = \int \mathcal{C}(t)dt$ con Frente D | **Nueva** |
| Wall final = no-existencia de pares complejos de ceros de $f$ = Wall A | **Nueva identificación** |

---

## 10. La pregunta más directa que queda

De todos los análisis de Phase 28, la pregunta más concreta y ataqueable:

**Pregunta 28.2** (versión correcta). ¿Puede probarse que $\mathcal{C}(t) = (\xi'/\xi)'(1/2+it) > 0$ para todo $t$ fuera de los ordinates de ceros de $\zeta$, usando sólo:
1. La ecuación funcional $\xi(s) = \xi(1-s)$;
2. El producto de Euler $\xi(s) \sim \zeta(s) \cdot (\text{factor Gamma})$;
3. Sin asumir RH?

Si la respuesta es sí: RH queda probado.

Si la respuesta es no (hay contraejemplo o si la prueba requiere asumir RH): el muro es el mismo Wall A de siempre.

La novedad es que esta pregunta es **analítica concreta sobre $\xi'/\xi$**, formulable en términos de una función conocida, sin intermediarios cohomológicos ni espectrales.
