# Documento 70 — De Bruijn-Newman y la traza CCM: $\Lambda$ como tiempo de extinción de $T_\lambda(t)$

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-08  
**Prerrequisitos:** Docs 59–69 (Fase 32), en especial Doc 64 (CTP) y Doc 68 (Wronskiano exacto)

---

## 1. Motivación: conectar dos reformulaciones de RH

Tenemos dos equivalencias:

**CTP (Doc 64):** RH $\iff T_\lambda = 0$ para todo $\lambda > 0$.

**De Bruijn-Newman:** RH $\iff \Lambda \leq 0$ (y Rodgers-Tao 2018: $\Lambda \geq 0$, luego RH $\iff \Lambda = 0$).

La pregunta natural es: ¿hay una forma de expresar $\Lambda$ en términos de la traza $T_\lambda$?

---

## 2. El flujo de De Bruijn-Newman

### 2.1. Definición estándar

La función de De Bruijn-Newman de parámetro $t \in \mathbb{R}$ es

$$H_t(z) = \int_0^\infty e^{tu^2}\, \Phi(u)\cos(zu)\, du,$$

donde $\Phi(u) = \sum_{n=1}^\infty (2\pi^2 n^4 e^{9u/2} - 3\pi n^2 e^{5u/2}) e^{-\pi n^2 e^{2u}}$ es el núcleo de Jacobi theta. Para $t = 0$: $H_0(z) = \Xi(z/2)$ (la función xi de Riemann).

La constante de De Bruijn-Newman se define como

$$\Lambda = \inf\{t \in \mathbb{R} : H_t \text{ tiene todos sus ceros reales}\}.$$

Se sabe: $-\infty < \Lambda \leq 1/2$ (De Bruijn 1950), $\Lambda \geq 0$ (Rodgers-Tao 2018), RH $\iff \Lambda = 0$.

### 2.2. Dinámica de los ceros bajo el flujo

Los ceros de $H_t$, denotados $\{z_n(t)\}$, satisfacen la ecuación de movimiento (válida mientras sean simples):

$$\frac{dz_n}{dt} = \sum_{m \neq n} \frac{-2}{z_n(t) - z_m(t)}.$$

Para $t > \Lambda$, todos los ceros son reales y se *repelen* mutuamente (dinámica de Dyson-Calogero-Moser). Los ceros reales satisfacen $\dot{z}_n > 0$ si $z_n$ es el máximo local de la densidad de ceros, indicando dispersión.

Para $t < \Lambda$, hay ceros complejos $z_n = \alpha_n + i\beta_n$ con $\beta_n \neq 0$ que "caen" hacia la recta real cuando $t \to \Lambda$.

---

## 3. La traza parametrizada $T_\lambda(t)$

### 3.1. Medidas dependientes de $t$

Para cada $t \geq 0$, definimos la medida completa deformada:

$$dm_{full}^t(s) = dm_\infty(s) \cdot |H_t(s)|^2 \cdot C_t^{-1},$$

donde $C_t = \int |H_t(s)|^2\, dm_\infty(s)$ es la constante de normalización. La medida $dm_{full}^{t=0} = dm_{full}$ es la medida del Doc 64 (antes de la normalización).

La medida de referencia "on-critical" para el parámetro $t$:

$$dm_{full,on}^t(s) = dm_\infty(s) \cdot |H_t^{on}(s)|^2 \cdot C_t^{-1},$$

donde $H_t^{on}$ se construye a partir de $H_t$ reflejando todos sus ceros complejos a la recta real (la imagen $\rho \mapsto \frac{1}{2} + i\operatorname{Im}(\rho)$).

**Observación 3.1.** Para $t > \Lambda$: todos los ceros de $H_t$ son reales, luego $H_t = H_t^{on}$ y $dm_{full}^t = dm_{full,on}^t$. Por la Prop. 2.1 de Doc 64 y el Thm. 3.1: $T_\lambda(t) = 0$ para todo $\lambda$.

### 3.2. Definición de la traza deformada

$$T_\lambda(t) := \sum_{n:\, \gamma_n(t) \leq \lambda} \left(\Delta_n^{full,t} - \Delta_n^{full,on,t}\right),$$

donde $\Delta_n^{full,t} = (a_n^{full,t})^2 - (a_n^\infty)^2$ es la discrepancia de los coeficientes de Jacobi de $dm_{full}^t$ respecto a la medida archimediana.

**Proposición 3.2** (Consistencia con el CTP). El Thm. 3.1 de Doc 64 se aplica a cada $t$ fijo: $T_\lambda(t) = 0$ para todo $\lambda$ si y solo si $dm_{full}^t = dm_{full,on}^t$, i.e., si y solo si todos los ceros de $H_t$ son reales.

*Demostración.* Idéntica a la del Doc 64, reemplazando $H_0$ por $H_t$. $\square$

---

## 4. $\Lambda$ como tiempo de extinción de $T_\lambda(t)$

### 4.1. El enunciado central

**Teorema 4.1** (Caracterización de $\Lambda$ via traza CCM).

$$\Lambda = \inf\{t \geq 0 : T_\lambda(t) = 0 \text{ para todo } \lambda > 0\}.$$

*Demostración.*

**"$\leq$":** Si $t > \Lambda$, todos los ceros de $H_t$ son reales, luego $T_\lambda(t) = 0$ para todo $\lambda$ (Obs. 3.1). Por tanto $\{t : T_\lambda(t) = 0 \ \forall\lambda\} \supseteq (\Lambda, \infty)$, y el ínfimo del conjunto izquierdo es $\leq \Lambda$.

**"$\geq$":** Si $t < \Lambda$, entonces $H_t$ tiene al menos un cero complejo $z_0 = \alpha_0 + i\beta_0$ con $\beta_0 \neq 0$. El argumento del Cor. 7.5 de Doc 63 (ahora con $H_t$ en lugar de $H_0$) muestra que $T_\lambda(t) > 0$ para $\lambda$ suficientemente grande. (La prueba es idéntica: $W_\lambda \geq 0$, la corrección es absolutamente continua y no nula, luego la integral es positiva.) Por tanto $t \notin \{t : T_\lambda(t) = 0 \ \forall\lambda\}$, y el ínfimo del conjunto derecho es $\geq \Lambda$. $\square$

### 4.2. Reformulación de RH

Dado que $\Lambda \geq 0$ (Rodgers-Tao) y $\Lambda \leq 1/2$ (De Bruijn), el Teorema 4.1 da:

$$\text{RH} \iff \Lambda = 0 \iff T_\lambda(0) = 0 \text{ para todo } \lambda > 0.$$

Esto no es nuevo respecto al CTP de Doc 64 (es la misma equivalencia en $t = 0$). Lo nuevo es que $\Lambda$ tiene una descripción espectral-variacional concreta:

> **$\Lambda$ es el tiempo mínimo en que la traza de discrepancia CCM se extingue.**

---

## 5. Monotonicidad de $T_\lambda(t)$

### 5.1. La pregunta

¿Es $T_\lambda(t)$ monótona decreciente en $t$?

Si $\partial_t T_\lambda(t) \leq 0$, la traza "converge a cero desde arriba" cuando $t \to \Lambda^+$, lo que daría una imagen más precisa de la constante $\Lambda$.

### 5.2. La fórmula de la derivada temporal

Diferenciando $T_\lambda(t) = \int W_\lambda(s)\,(dm_{full}^t - dm_{full,on}^t)(s)$ respecto a $t$:

$$\partial_t T_\lambda(t) = \int W_\lambda(s)\, \partial_t(dm_{full}^t - dm_{full,on}^t)(s).$$

La derivada $\partial_t dm_{full}^t$ se calcula usando $\partial_t H_t = \partial_{ss} H_t$ (ecuación del calor):

$$\partial_t |H_t(s)|^2 = 2\operatorname{Re}(\overline{H_t(s)}\, \partial_t H_t(s)) = 2\operatorname{Re}(\overline{H_t(s)}\, H_t''(s)).$$

Integrando por partes (usando $W_\lambda$ suave):

$$\partial_t T_\lambda(t) = 2\int W_\lambda(s)\operatorname{Re}(\overline{H_t}\, H_t'' - \overline{H_t^{on}}\, (H_t^{on})'')\, dm_\infty(s).$$

Integrando por partes en $s$ (la derivada actúa sobre $W_\lambda$):

$$\partial_t T_\lambda(t) = -2\int W_\lambda'(s)\operatorname{Re}(\overline{H_t}\, H_t' - \overline{H_t^{on}}\, (H_t^{on})')\, dm_\infty(s) + \text{frontera}.$$

### 5.3. El signo de la derivada: análisis via ceros

Para $t > \Lambda$, $H_t$ tiene todos los ceros reales, así que $H_t = H_t^{on}$ y $\partial_t T_\lambda(t) = 0$ consistentemente.

Para $t < \Lambda$, los ceros complejos de $H_t$ inducen una perturbación no nula. La ecuación de movimiento de los ceros (§2.2) describe la dinámica: los ceros complejos se mueven hacia la recta real cuando $t$ aumenta, reduciendo la contribución de la corrección off-critical.

**Conjetura 5.1** (Monotonicidad). Para $0 \leq t_1 < t_2$:
$$T_\lambda(t_1) \geq T_\lambda(t_2) \geq 0.$$

Esta conjetura es plausible porque:
- El flujo de calor "regulariza" $H_t$: dispersa los ceros fuera de la recta real acercándolos a ella.
- La cantidad $dm_{full}^t - dm_{full,on}^t$ mide exactamente cuánto se desvían los ceros de $H_t$ de la recta real, y esta desviación decrece con $t$.

*Estado:* conjetura, no probada en este documento. Su prueba requería controlar $\operatorname{Re}(\overline{H_t}H_t'' - \overline{H_t^{on}}(H_t^{on})'')$ en el soporte de $dm_\infty$, que involucra estimados sobre la distribución de los ceros complejos de $H_t$.

---

## 6. Cota inferior para $\Lambda$

### 6.1. Relación cuantitativa

Si la monotonicidad (Conj. 5.1) vale, entonces para $t < \Lambda$:

$$T_\lambda(0) \geq T_\lambda(t) \geq 0.$$

Del Cor. 7.5 de Doc 63 (adaptado a $H_t$ con su cero complejo dominante $z_0(t) = \alpha_0(t) + i\beta_0(t)$):

$$T_\lambda(t) \geq c_0 \cdot N(\lambda) \cdot w(\alpha_0(t)) \cdot |\beta_0(t)|^2,$$

donde $|\beta_0(t)|$ es el tamaño de la parte imaginaria del cero más cercano a la recta real.

Tomando $t \to \Lambda^-$ y usando que $|\beta_0(\Lambda)| = 0$ (los ceros llegan a la recta real exactamente en $t = \Lambda$):

$$T_\lambda(0) \geq T_\lambda(\Lambda^-) = 0.$$

Esto es consistente pero no da información nueva sobre $\Lambda$.

### 6.2. La tasa de extinción como información de $\Lambda$

La información nueva vendría de la **tasa de extinción**: si $T_\lambda(t) \sim C(\lambda) \cdot (\Lambda - t)^\alpha$ cuando $t \to \Lambda^-$, entonces $\alpha$ y $C(\lambda)$ codifican información cuantitativa sobre $\Lambda$.

Para el modelo más simple (un solo cero complejo en $z_0 = \alpha_0 + i\beta_0$ con trayectoria $\beta_0(t) \sim \sqrt{2(\Lambda - t)}$ bajo la dinámica de Dyson):

$$T_\lambda(t) \sim c \cdot N(\lambda) \cdot (\Lambda - t), \qquad t \to \Lambda^-.$$

Por tanto:

$$\Lambda = \lim_{t \to \Lambda^-} \frac{T_\lambda(t)}{c \cdot N(\lambda)}.$$

Esta es una forma de "medir" $\Lambda$ mediante la traza CCM, aunque requiere conocer la trayectoria de los ceros (que es información a priori tan difícil como RH).

---

## 7. Una cota superior para $\Lambda$ via CTP

### 7.1. Enunciado

**Proposición 7.1** (Cota superior para $\Lambda$). Si existe $t_0 \geq 0$ tal que $T_\lambda(t_0) = 0$ para todo $\lambda > 0$, entonces $\Lambda \leq t_0$.

*Demostración.* Del Thm. 4.1, si $T_\lambda(t_0) = 0$ para todo $\lambda$, entonces $t_0 \in \{t : T_\lambda(t) = 0 \ \forall\lambda\}$, luego $\inf \geq t_0$ implica $\Lambda \leq t_0$. $\square$

### 7.2. Consecuencia práctica

Para probar RH ($\Lambda = 0$) es suficiente probar $T_\lambda(0) = 0$ para todo $\lambda$ (esto es el CTP del Doc 64). La Prop. 7.1 no da un camino nuevo, pero reformula la estrategia: en lugar de trabajar directamente con $\Lambda$, uno estudia si hay $t_0$ arbitrariamente pequeño con $T_\lambda(t_0) = 0$.

---

## 8. La conexión con la ecuación de Toda discreta

### 8.1. El flujo de Jacobi inducido

El flujo $t \mapsto dm_{full}^t$ induce un flujo $t \mapsto \{a_n^{full,t}\}_{n\geq 0}$ sobre los coeficientes de Jacobi. La pregunta natural es qué ecuación satisfacen $(a_n^{full,t})_{n,t}$.

Para medidas que evolucionan según la ecuación del calor, la evolución inducida sobre los coeficientes de Jacobi se relaciona con la **cadena de Toda**:

$$\dot{a}_n = a_n(b_{n+1} - b_n), \qquad \dot{b}_n = 2(a_n^2 - a_{n-1}^2),$$

donde $b_n$ son los coeficientes diagonales (que son cero para medidas simétricas en $t = 0$).

Para medidas simétricas (como la nuestra, donde $dm_\infty$ es par y $|H_t|^2$ es par): $b_n = 0$ para todo $t$. La cadena de Toda se reduce a:

$$\dot{a}_n = 0 \cdot (0 - 0) = 0?$$

No, esto es incorrecto: la cadena de Toda para medidas simétricas con $b_n = 0$ tiene $\dot{b}_n = 2(a_n^2 - a_{n-1}^2) \neq 0$ en general, lo que genera $b_n \neq 0$ para $t > 0$. La simetría $b_n = 0$ se rompe bajo el flujo (a menos que $a_n$ sean constantes).

**Observación 8.1.** El flujo de De Bruijn-Newman *no* preserva la simetría de la medida. Para $t > 0$, la medida $dm_{full}^t$ puede perder la simetría $s \mapsto -s$, lo que introduce $b_n \neq 0$ en la cadena de Jacobi. Esto complica el análisis.

### 8.2. El caso $t$ pequeño: perturbación lineal

Para $t \ll 1$, expandimos $H_t \approx H_0 + t H_0'' + O(t^2)$:

$$|H_t|^2 \approx |H_0|^2 + 2t\operatorname{Re}(\overline{H_0} H_0'') + O(t^2).$$

La corrección de primer orden a $dm_{full}^t$ es:

$$\delta dm^{(1)}(s) = 2t\operatorname{Re}(\overline{H_0(s)} H_0''(s)) dm_\infty(s) \cdot C_0^{-1}.$$

Por la representación CD (Doc 61, Thm. 2.1), la corrección de primer orden a $(a_n^{full,t})^2$ es:

$$\delta(a_n^2)^{(1)} = 2t \int (|P_{n+1}|^2 - |P_n|^2) \operatorname{Re}(\overline{H_0} H_0'') dm_\infty.$$

Usando la integración por partes ($H_0'' = -\mathcal{L}_0 H_0$ donde $\mathcal{L}_0$ es el operador de Schrödinger):

$$\delta(a_n^2)^{(1)} = -2t \int (|P_{n+1}|^2 - |P_n|^2) \operatorname{Re}(\overline{H_0} \mathcal{L}_0 H_0) dm_\infty.$$

Expandiendo $H_0 = \sum_k c_k P_k$ (donde $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$, como en Doc 65):

$$\operatorname{Re}(\overline{H_0} \mathcal{L}_0 H_0) = \operatorname{Re}\left(\sum_{k,l} \bar{c}_k c_l P_k \mathcal{L}_0 P_l\right) = \operatorname{Re}\left(\sum_k |c_k|^2 \mu_k P_k^2 + \text{cross terms}\right),$$

donde $\mu_k$ son los autovalores de $\mathcal{L}_0$ en $P_k$ (Doc 65, §2.3).

**Proposición 8.2** (Derivada temporal de la traza en $t = 0$).

$$\partial_t T_\lambda \bigg|_{t=0} = -4\int W_\lambda(s) \operatorname{Re}(\overline{H_0(s)} H_0''(s)) dm_\infty(s).$$

Si esta derivada es negativa (lo que requeriría $\operatorname{Re}(\overline{H_0}H_0'') > 0$ en el soporte de $W_\lambda$, i.e., que $H_0$ y $H_0''$ tengan parte real del mismo signo), entonces $T_\lambda(t)$ decrece inicialmente, consistente con la Conj. 5.1.

---

## 9. Resultado condicional: cota cuantitativa para $\Lambda$

**Teorema 9.1** (Cota inferior para $\Lambda$ via $T_\lambda(0)$, condicional a Conj. 5.1).

Asumiendo la monotonicidad del Conj. 5.1, para todo $\lambda > 0$ y todo $t < \Lambda$:

$$T_\lambda(0) \geq T_\lambda(t) \geq c_0 \cdot N(\lambda) \cdot (2\pi)^{-2}|\Gamma(1/4 + i\alpha_0/2)|^2 \cdot |\beta_0(t)|^2,$$

donde $z_0(t) = \alpha_0(t) + i\beta_0(t)$ es el cero de $H_t$ más cercano a la recta real.

*Consecuencia:* si $T_\lambda(0) = o(N(\lambda))$ cuando $\lambda \to \infty$, entonces $\Lambda = 0$ (RH).

Esto es el primer enunciado que conecta RH con una condición *cuantitativa* sobre la tasa de crecimiento de $T_\lambda(0)$. Sin embargo, aún depende de la monotonicidad no probada.

---

## 10. Resumen y dirección para Doc 71

**Resultado central (incondicional):**
$$\Lambda = \inf\{t \geq 0 : T_\lambda(t) = 0 \;\forall\lambda > 0\}.$$

Esta es una nueva caracterización de la constante de De Bruijn-Newman en términos del formalismo CCM-Jacobi.

**Resultado condicional (asumiendo Conj. 5.1):** $T_\lambda(0) = o(N(\lambda)) \implies \Lambda = 0$.

**Queda abierto:**
1. Probar la monotonicidad $\partial_t T_\lambda(t) \leq 0$.
2. Calcular $\partial_t T_\lambda(0)$ explícitamente en términos de $c_k = \langle\Xi, P_k\rangle$.
3. Conectar la dinámica de Jacobi con la cadena de Toda o Ablowitz-Ladik.

**Doc 71** debe abordar el punto 2: la derivada $\partial_t T_\lambda(0)$ es explícita via la Prop. 8.2 y los coeficientes $c_k$. Si $\partial_t T_\lambda(0) < 0$ bajo $\neg$RH, esto daría una condición diferencial sobre $T_\lambda$ que acota $\Lambda$ desde abajo.

---

*Fin del Documento 70.*
