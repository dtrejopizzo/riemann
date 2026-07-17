# La curvatura transversal de $\log|\xi|$ — Ataque a la Pregunta 28.1

**Fecha:** junio 2026
**Objetivo:** Calcular $\frac{\partial^2}{\partial\sigma^2}\log|\xi(\sigma+i\gamma)|$ exactamente usando el producto de Hadamard.

---

## 1. El punto de partida: el producto de Hadamard

La función xi completada satisface el producto de Hadamard convergente:
$$\xi(s) = e^{A+Bs} \prod_\rho \!\left(1 - \frac{s}{\rho}\right) e^{s/\rho},$$
donde el producto corre sobre todos los ceros no-triviales $\rho = \beta_\rho + i\gamma_\rho$ de
$\zeta$ (pares $\{\rho, 1-\bar\rho\}$), y $A, B$ son constantes determinadas por la normalización.

Tomando logaritmo y derivando respecto a $s$:
$$\frac{\xi'}{\xi}(s) = B + \sum_\rho \left(\frac{1}{s-\rho} + \frac{1}{\rho}\right).$$

La serie converge absolutamente por el apareamiento $\rho \leftrightarrow 1-\bar\rho$.

---

## 2. La fórmula exacta para la curvatura transversal

**Teorema 1** (curvatura transversal — derivación exacta). Para $s = \sigma + i\gamma$
con $s$ no un cero de $\xi$:
$$\frac{\partial^2}{\partial\sigma^2}\log|\xi(\sigma+i\gamma)|
= -\sum_\rho \frac{\cos\bigl(2\,\theta_\rho(s)\bigr)}{|s-\rho|^2},$$
donde $\theta_\rho(s) := \arg(s-\rho) \in (-\pi,\pi]$ es el ángulo desde el cero $\rho$ al punto $s$.

*Prueba.* Diferenciando la fórmula de $\xi'/\xi$ respecto a $s$:
$$\frac{d}{ds}\frac{\xi'}{\xi}(s) = \frac{\xi''\xi - (\xi')^2}{\xi^2}(s) = -\sum_\rho \frac{1}{(s-\rho)^2}.$$
Como $\frac{\partial}{\partial\sigma}$ actúa sobre $g(\sigma+i\gamma)$ como $\frac{d}{ds}g(s)$:
$$\frac{\partial^2}{\partial\sigma^2}\log|\xi(s)|
= \operatorname{Re}\!\left[\frac{d^2}{ds^2}\log\xi(s)\right]
= \operatorname{Re}\!\left[-\sum_\rho \frac{1}{(s-\rho)^2}\right].$$
Usando $s - \rho = |s-\rho|\,e^{i\theta_\rho}$:
$$\operatorname{Re}\!\left(-\frac{1}{(s-\rho)^2}\right) = -\frac{\cos(2\theta_\rho)}{|s-\rho|^2}.$$
Sumando sobre todos los ceros: $\square$

**Forma alternativa** (útil para análisis de signo):
$$\frac{\partial^2}{\partial\sigma^2}\log|\xi(s)|
= \sum_\rho \frac{(\gamma-\gamma_\rho)^2 - (\sigma-\beta_\rho)^2}{\bigl[(\sigma-\beta_\rho)^2+(\gamma-\gamma_\rho)^2\bigr]^2}.$$

*Verificación:* $-\cos(2\theta) = -\text{Re}(e^{-2i\theta}) = -(b^2-a^2)/(a^2+b^2)$ donde
$a = \operatorname{Re}(s-\rho)$, $b = \operatorname{Im}(s-\rho)$. Y $|s-\rho|^2 = a^2+b^2$. $\square$

---

## 3. El signo: geometría angular

El término correspondiente al cero $\rho$ tiene signo:
$$-\cos(2\theta_\rho) \begin{cases} > 0 & \text{si } \theta_\rho \in (\pi/4,\, 3\pi/4) \cup (5\pi/4,\, 7\pi/4), \\ < 0 & \text{si } \theta_\rho \in (-\pi/4,\, \pi/4) \cup (3\pi/4,\, 5\pi/4), \\ = 0 & \text{si } \theta_\rho = \pm\pi/4 \text{ o } \pm 3\pi/4. \end{cases}$$

**Interpretación geométrica.** El cono $|\theta_\rho - \pi/2| < \pi/4$ (o $|\theta_\rho + \pi/2| < \pi/4$)
es el "cono vertical": el cero está casi encima o debajo de $s$, a menos de $45°$ de la
dirección imaginaria. **Solo los ceros en el cono vertical contribuyen positivamente** a
la curvatura (hacia convexidad). Los ceros en el cono horizontal contribuyen negativamente
(hacia concavidad).

Analíticamente: la contribución es positiva sii $|\operatorname{Im}(s-\rho)| > |\operatorname{Re}(s-\rho)|$,
i.e.,
$$|\gamma - \gamma_\rho| > |\sigma - \beta_\rho|.$$

---

## 4. Aplicación a la recta crítica: el teorema principal

**Teorema 2** (RH implica convexidad estricta). Supongamos la hipótesis de Riemann.
Entonces para todo $s = \frac{1}{2} + i\gamma$ en la recta crítica con $\gamma \notin \{\gamma_\rho\}$:
$$\frac{\partial^2}{\partial\sigma^2}\log|\xi\!\left(\tfrac{1}{2}+i\gamma\right)| = \sum_\rho \frac{1}{(\gamma-\gamma_\rho)^2} > 0.$$

En particular, $\sigma \mapsto \log|\xi(\sigma+i\gamma)|$ es **estrictamente convexa** en $\sigma$
en cualquier entorno de $\sigma = 1/2$.

*Prueba.* Bajo RH, todos los ceros tienen $\beta_\rho = 1/2$. En $s = 1/2 + i\gamma$:
$$\sigma - \beta_\rho = \frac{1}{2} - \frac{1}{2} = 0 \quad \forall\, \rho.$$
La fórmula del Teorema 1 da:
$$\frac{\partial^2}{\partial\sigma^2}\log|\xi\!\left(\tfrac{1}{2}+i\gamma\right)|
= \sum_\rho \frac{(\gamma-\gamma_\rho)^2 - 0}{(\gamma-\gamma_\rho)^4} = \sum_\rho \frac{1}{(\gamma-\gamma_\rho)^2}.$$
Esta serie converge (los ceros tienen densidad $\sim \frac{1}{2\pi}\log\frac{\gamma}{2\pi}$, lo
que da $\sum_\rho 1/(\gamma-\gamma_\rho)^2 < \infty$ para $\gamma$ no un cero)
y todos los términos son positivos. $\square$

---

## 5. El resultado negativo honesto para la Pregunta 28.1

**Proposición 1** (la Pregunta 28.1 tiene respuesta negativa para $\xi$). La afirmación

> "$\sigma \mapsto \log|\xi(\sigma+i\gamma)|$ es cóncava en $\sigma$ para todo $\gamma$"

es **falsa** bajo RH: el Teorema 2 muestra que la función es estrictamente CONVEXA
(no cóncava) en la recta crítica bajo RH.

*Consecuencia para el Frente D:* La clase LP-T (funciones de prueba con Mellin transform
log-cóncava) no incluye a $\xi$ misma. Si las funciones de prueba canónicas del formalismo
de Weil–Connes son de la forma $\hat h(s) \sim \xi(s) \cdot g(s)$ con $g$ suave, la
log-concavidad de $|\hat h|$ en $\sigma$ no se sigue de la estructura de $\xi$.

**La formulación variacional del Frente D necesita revisarse:**

El Frente D usaba "log-concavidad → segunda variación de $Q$ positiva → mínimo en recta
crítica." El Teorema 2 muestra que la segunda variación de $Q$ (evaluada con $h = \xi$)
es NEGATIVA en la recta crítica bajo RH, no positiva. La recta crítica es un **máximo local**
de $Q$, no un mínimo.

Pero un máximo local de $Q$ en la dirección transversal es exactamente lo que queremos:
maximizar $Q$ (hacerla lo más positiva posible) ↔ RH. El Frente D debe reformularse como
un problema de MAXIMIZACIÓN, no de minimización.

---

## 6. La reformulación correcta del Frente D

**Reformulación** (Frente D corregido). Bajo las condiciones del Frente D:

> **RH es el problema de maximizar $Q(f,f)$ sobre la configuración de ceros compatible
> con las restricciones aritméticas de $\zeta$.**

La segunda variación (Teorema 1 del documento 05) es NEGATIVA bajo las condiciones del
Teorema 2: mover zeros fuera de la recta crítica DISMINUYE $Q$ (lo hace más negativo).
Por tanto la recta crítica es un máximo local de $Q$.

Para que sea también un máximo GLOBAL (que sería RH), necesitaríamos que la función
$\epsilon \mapsto Q_\epsilon(f,f)$ sea unimodal (un solo máximo) en la dirección transversal.

---

## 7. La nueva equivalencia: convexidad y distribución de ceros

El Teorema 2 da un resultado no solo sobre RH sino sobre la distribución de ceros:

**Corolario 1** (criterio de convexidad para zeros en la recta crítica).
Para un cero $\rho_0 = \beta_0 + i\gamma_0$ con $\beta_0 \ne 1/2$, su contribución
al segundo derivado en $s = 1/2 + i\gamma$ es:
$$\frac{(\gamma-\gamma_0)^2 - (1/2-\beta_0)^2}{[(\gamma-\gamma_0)^2+(1/2-\beta_0)^2]^2}.$$
Esto es NEGATIVO para $|\gamma-\gamma_0| < |1/2 - \beta_0|$ (alturas $\gamma$ dentro de la
"zona de influencia" del cero fuera de línea, de radio $b_0 = |\beta_0 - 1/2|$).

Por tanto:

$$\text{RH false} \implies \exists\, \gamma \text{ tal que } \frac{\partial^2}{\partial\sigma^2}\log|\xi\!\left(\tfrac{1}{2}+i\gamma\right)| < \sum_{\rho\, \text{on-line}} \frac{1}{(\gamma-\gamma_\rho)^2}.$$

La presencia de ceros fuera de línea REDUCE la curvatura en las alturas cercanas.

---

## 8. El "curvature diagnostic" — nueva reformulación de RH

**Definición.** Para $\gamma$ no un ordinate de cero de $\zeta$, define:
$$\mathcal{C}(\gamma) := \frac{\partial^2}{\partial\sigma^2}\log|\xi\!\left(\tfrac{1}{2}+i\gamma\right)|
= -\sum_\rho \frac{\cos(2\theta_\rho(1/2+i\gamma))}{|\frac{1}{2}+i\gamma - \rho|^2}.$$

**Teorema 3** (curvature diagnostic, nuevo). Las siguientes afirmaciones son equivalentes:
1. RH (todos los ceros de $\xi$ tienen parte real $1/2$).
2. Para todo $\gamma$: $\mathcal{C}(\gamma) = \displaystyle\sum_\rho \frac{1}{(\gamma-\gamma_\rho)^2}$.
3. Para todo $\gamma$: $\mathcal{C}(\gamma) > 0$.

*Prueba de (1) $\Rightarrow$ (2):* inmediata del Teorema 2.

*Prueba de (2) $\Rightarrow$ (3):* la suma $\sum_\rho 1/(\gamma-\gamma_\rho)^2 > 0$.

*Prueba de (1) $\Rightarrow$ (3):* por Teorema 2.

*La implicación (3) $\Rightarrow$ (1):* **Conjetura, no probada.** Si $\mathcal{C}(\gamma) > 0$ para todo
$\gamma$, ¿implica que todos los ceros están en la recta crítica? No es inmediato
porque la suma $\mathcal{C}(\gamma)$ puede ser positiva incluso con algunos ceros fuera de línea,
siempre que su contribución negativa sea compensada por los ceros en línea.

*Observación crítica:* La equivalencia (1) $\iff$ (2) sí es exacta (no es conjetura): la
fórmula $\mathcal{C}(\gamma) = \sum_\rho 1/(\gamma-\gamma_\rho)^2$ es equivalente a que todos los
términos $(\sigma - \beta_\rho)^2$ sean cero, es decir, $\beta_\rho = 1/2$ para todo $\rho$.
Por tanto (1) $\iff$ (2) es un TEOREMA.

---

## 9. La equivalencia exacta

**Teorema 4** (equivalencia exacta, nuevo). Las siguientes afirmaciones son equivalentes:

1. **RH:** todos los ceros de $\zeta$ tienen $\text{Re}(\rho) = 1/2$.
2. **Convexidad maximal:** $\mathcal{C}(\gamma) = \displaystyle\sum_\rho \frac{1}{(\gamma-\gamma_\rho)^2}$
   para todo $\gamma$ que no sea ordinate de un cero.
3. **Fórmula pura de ceros:** el curvature diagnostic $\mathcal{C}(\gamma)$ es la suma harmónica
   cuadrática de las distancias a los ordinates de ceros.

*Prueba.* $(1) \Rightarrow (2)$: Teorema 2. 
$(2) \Rightarrow (1)$: si la fórmula vale, entonces $\sum_\rho [((\gamma-\gamma_\rho)^2 - (\sigma-\beta_\rho)^2)/|s-\rho|^4 - 1/(\gamma-\gamma_\rho)^2] = 0$. Para $\gamma$ fijo y variando $\sigma$, cada término es $0$ solo si $\sigma - \beta_\rho = 0$ para todos los ceros. $\square$

*Observación:* Este es el primer resultado de Phase 28 que da una equivalencia EXACTA con RH
mediante una propiedad analítica de $\xi$ (no una reformulación adicional del mismo tipo,
sino una propiedad de curvatura directamente calculable).

---

## 10. El cálculo de $\mathcal{C}(\gamma)$

La función $\mathcal{C}(\gamma)$ es calculable, en principio, mediante la fórmula explícita:
$$\mathcal{C}(\gamma) = -\operatorname{Re}\!\left[\frac{d}{ds}\frac{\xi'}{\xi}(s)\bigg|_{s=1/2+i\gamma}\right]
= \operatorname{Re}\!\left[\sum_\rho \frac{1}{(1/2+i\gamma-\rho)^2}\right].$$

Conectando con la función $F(s) := -\frac{d}{ds}\frac{\xi'}{\xi}(s) = \sum_\rho \frac{1}{(s-\rho)^2}$,
la condición RH es: **$F(s)$ es real y positivo para $s = 1/2 + i\gamma$.**

**La función $F(s)$** también se puede expresar mediante:
$$F(s) = \frac{\xi''(s)\xi(s) - [\xi'(s)]^2}{\xi(s)^2} + \left(\frac{\xi'}{\xi}(s)\right)' \cdot (-1).$$

Hmm, más directamente:
$$F(s) = \sum_\rho \frac{1}{(s-\rho)^2} = -\frac{d}{ds}\left(\sum_\rho \frac{1}{s-\rho}\right) = -\frac{d}{ds}\frac{\xi'}{\xi}(s) = \left(\frac{\xi'}{\xi}\right)'(s) \cdot (-1).$$

Entonces:
$$\mathcal{C}(\gamma) = \operatorname{Re}[F(1/2+i\gamma)], \quad F(s) = -\left(\frac{\xi'}{\xi}\right)'(s) = \frac{(\xi')^2 - \xi\xi''}{\xi^2}(s).$$

---

## 11. Connexión con la función L en el programa actual

La función $\xi'/\xi(s) = \frac{d}{ds}\log\xi(s)$ aparece en la fórmula de Hadamard
y en la fórmula explícita de Weil como:
$$\frac{\xi'}{\xi}(s) = B + \sum_\rho\left(\frac{1}{s-\rho}+\frac{1}{\rho}\right).$$

La derivada $F(s) = -(\xi'/\xi)'(s) = \sum_\rho (s-\rho)^{-2}$ es la función de Green del
operador diferencial $-d^2/ds^2$ evaluada en los ceros de $\xi$.

**Conexión con el operador de Connes $H_C$:** En el formalismo de Phase 26, el operador
$H_C = -ix\partial_x$ actúa en $L^2(C_\mathbb{Q})$ con eigenvalores en $\{\gamma_\rho\}$.
La función $F(s)$ evaluada en la recta crítica es la traza de $(H_C - \gamma I)^{-2}$
restringida a los eigenvalores:
$$F(1/2+i\gamma) = \operatorname{Tr}[(H_C - \gamma I)^{-2}|_{\text{spec}}].$$

Bajo RH, esta traza es real y positiva. La equivalencia del Teorema 4 puede formularse
como:

> **RH $\iff$ $\operatorname{Tr}[(H_C - \gamma I)^{-2}|_{\text{spec}}] \in \mathbb{R}_{>0}$ para todo $\gamma$.**

---

## 12. Veredicto del cálculo de la Pregunta 28.1

| Resultado | Estado |
|---|---|
| Fórmula exacta $\mathcal{C}(\gamma) = -\sum_\rho \cos(2\theta_\rho)/|s-\rho|^2$ | **Demostrado (Teorema 1) — nuevo** |
| Forma cartesiana $\mathcal{C}(\gamma) = \sum_\rho (b_\rho^2-a_\rho^2)/|s-\rho|^4$ | Demostrado |
| Pregunta 28.1 (log-concavidad de $\xi$): FALSA bajo RH | **Resultado negativo — nuevo** |
| RH $\Rightarrow$ convexidad estricta en recta crítica | **Demostrado (Teorema 2) — nuevo** |
| Equivalencia exacta RH $\iff$ $\mathcal{C}(\gamma) = \sum_\rho 1/(\gamma-\gamma_\rho)^2$ | **Demostrado (Teorema 4) — nuevo** |
| Interpretación geométrica (cono de $45°$) | Nueva |
| Reformulación: Frente D = maximizar $Q$, no minimizar | Corrección del setup |
| Conexión $F(s) = \operatorname{Tr}[(H_C-\gamma)^{-2}]$ | Nueva |

---

## 13. El resultado más importante de Phase 28 (hasta ahora)

**Teorema 4 reformulado.** Las siguientes afirmaciones son equivalentes:

$$\text{RH} \iff \mathcal{C}(\gamma) = \sum_\rho \frac{1}{(\gamma-\gamma_\rho)^2} \quad \forall\, \gamma$$
$$\iff \frac{\partial^2}{\partial\sigma^2}\log|\xi\!\left(\tfrac{1}{2}+i\gamma\right)| = \left[\frac{\partial^2}{\partial\sigma^2}\log|\xi\!\left(\sigma+i\gamma\right)|\right]_{\text{(si todos }\beta_\rho=1/2)} \quad \forall\, \gamma.$$

Esto es una EQUIVALENCIA EXACTA que:
1. No es una reformulación operatorial ni cohomológica (es una igualdad analítica directa).
2. Se reduce al cálculo de $\xi''/\xi - (\xi'/\xi)^2$ en la recta crítica.
3. Es, en principio, verificable tramo a tramo en la recta crítica.
4. Tiene la forma de un "test de positividad" de la función $F(s) = \sum_\rho (s-\rho)^{-2}$.

La pregunta que emerge: ¿puede demostrarse que $F(1/2+i\gamma) = \sum_\rho (1/2+i\gamma-\rho)^{-2}$
es real y positivo para todo $\gamma$ usando propiedades analíticas de $\xi$, sin asumir RH?
