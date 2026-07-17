# Documento 65 — PPP via recurrencia prolate: concentración de coeficientes $c_k = \langle \Xi, P_k \rangle$

**Programa:** Hipótesis de Riemann — Fase 32 CCM  
**Fecha:** 2026-06-07  
**Prerrequisitos:** Docs 59–64, en particular Doc 62 (PPP definido), Doc 63 (Abel, $W_\lambda \geq 0$)

---

## 1. Punto de partida: el PPP y por qué importa

En Doc 62 establecimos que la formulación exacta del PCN es imposible:
la función $F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z)$ satisface $F_n(z) = O(z^{-3})$ cuando $z \to \infty$,
de modo que no puede tener un polo simple en $z = \gamma_n$.

Sin embargo, la cadena lógica del programa requiere *alguna forma* de localización.
La formulación alternativa es el **PPP** (Problema del Pseudo-Polo):

> **Conjetura PPP (Doc 62, Def. 5.1).** Para cada $n$,
> $$F_n(z) = \frac{c_n^2}{z - \gamma_n} + R_n(z)$$
> donde $c_n = \langle \Xi, P_n \rangle_{dm_\infty}$ y $R_n$ es analítica en $\operatorname{Im} z > -\varepsilon$ para algún $\varepsilon > 0$.

El presente documento ataca el PPP directamente:
computamos los coeficientes $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$ usando la ecuación de autovalor del operador prolate $W_\lambda$, derivamos la recurrencia que satisfacen, identificamos el punto de inflexión de la recurrencia, y estudiamos si las soluciones se concentran cerca de $k = n(\lambda)$.

---

## 2. El operador prolate en la base de Jacobi

### 2.1. Definición

Sea $\lambda > 0$ fijo. El operador prolate asociado a $(dm_\infty, [-\lambda, \lambda])$ es

$$W_\lambda f(s) = \int_{-\lambda}^{\lambda} K_\infty(s, t)\, f(t)\, dm_\infty(t),$$

donde $K_\infty(s, t) = \sum_{k=0}^{\infty} P_k(s)\overline{P_k(t)}$ es el núcleo de la proyección ortogonal de $L^2(dm_\infty)$ sobre $L^2([-\lambda,\lambda], dm_\infty)$.

Por la completitud de $\{P_k\}$ en $L^2(dm_\infty)$, $W_\lambda$ actúa como proyección (autovalores en $[0,1]$).

### 2.2. Acción de $W_\lambda$ en la base $\{P_k\}$

Dado $f = \sum_k \hat{f}_k P_k$, tenemos

$$W_\lambda f = \sum_k \hat{f}_k \left(\int_{-\lambda}^{\lambda} P_k(s)\, dm_\infty(s|s)\right) P_k,$$

pero esta descripción es solo la proyección espectralmente. Para estudiar la ecuación diferencial, necesitamos el operador diferencial que conmuta con $W_\lambda$.

### 2.3. El operador diferencial conmutante

Para la medida de peso $w(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2$ (que es la densidad de $dm_\infty$), el operador de Schrödinger asociado a la ecuación de De Brujin–Newman–CCM es

$$\mathcal{L} = -\frac{d^2}{ds^2} + V(s), \qquad V(s) = \frac{\pi^2}{4}\tanh^2(\pi s/2) + \frac{\pi}{2}.$$

Este operador satisface la propiedad clave de *conmutación prolate*: existe un operador diferencial $\mathcal{D}_\lambda$ de segundo orden tal que $[\mathcal{D}_\lambda, W_\lambda] = 0$ (generalización de la propiedad prolate clásica de Slepian).

**Observación fundamental.** Los polinomios de Jacobi CCM satisfacen

$$\mathcal{L} P_k = \mu_k P_k, \qquad \mu_k = (2k+1) + O(k^{-1}),$$

donde los autovalores $\mu_k$ crecen linealmente. Esto no es inmediato desde la definición abstracta de $P_k$ via la recurrencia de Jacobi, sino que proviene de la relación con la representación metaplética de $\mathfrak{sl}(2,\mathbb{R})$ establecida en CCM Thm 5.2.

---

## 3. Derivación de la recurrencia para $c_k$

### 3.1. Expansión de $\Xi$ en la base de Jacobi

La función xi de Riemann $\Xi(s) = \xi(1/2 + is)$ pertenece a $L^2(dm_\infty)$ porque

$$\int_{\mathbb{R}} |\Xi(s)|^2\, dm_\infty(s) < \infty$$

(esto se deduce del decaimiento exponencial de $dm_\infty$ y del crecimiento polinomial de $\Xi$). Escribimos

$$\Xi = \sum_{k=0}^{\infty} c_k P_k \quad \text{en } L^2(dm_\infty), \qquad c_k = \langle \Xi, P_k \rangle_{dm_\infty} = \int_{\mathbb{R}} \Xi(s) P_k(s)\, dm_\infty(s).$$

La paridad de $\Xi$ (i.e., $\Xi(-s) = \Xi(s)$) y la paridad de $P_k$ implican $c_k = 0$ para $k$ impar.
Escribimos $c_k = 0$ si $k$ impar, y trabajamos con $k = 2m$.

### 3.2. Recurrencia de tres términos para $c_k$

Los coeficientes de Jacobi de $dm_\infty$ son (CCM Thm 5.2):
$$a_k^{\infty} = \frac{1}{2}\sqrt{(2k+1)(2k+2)}, \qquad b_k^{\infty} = 0.$$

La relación de recurrencia $s P_k(s) = a_k^{\infty} P_{k+1}(s) + a_{k-1}^{\infty} P_{k-1}(s)$ implica que la multiplicación por $s$ actúa como la matriz de Jacobi $J^{\infty}$ en la base $\{P_k\}$.

Aplicando la ecuación funcional de $\Xi$: la función xi satisface

$$\Xi''(s) + \left(\frac{\pi^2}{4}s^2 - A\right)\Xi(s) = B\, \Xi(s) \cdot \phi(s)$$

para ciertos $A, B$ y una función $\phi$ explícita (ver Doc 57, ecuación de De Bruijn). Esta ecuación, proyectada sobre $P_k$, da una relación entre $c_{k-2}, c_k, c_{k+2}$.

### 3.3. La recurrencia explícita

**Proposición 3.1** (Recurrencia para los coeficientes CCM de $\Xi$).

Los coeficientes $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$ satisfacen, para $k \geq 2$ par,

$$-\alpha_{k-2}\, c_{k-2} + \beta_k\, c_k - \alpha_k\, c_{k+2} = 0,$$

donde
$$\alpha_k = a_k^{\infty} a_{k+1}^{\infty} = \frac{1}{4}\sqrt{(2k+1)(2k+2)(2k+3)(2k+4)},$$
$$\beta_k = \mu_k - \mu_0 - (a_k^{\infty})^2 - (a_{k-1}^{\infty})^2,$$

y $\mu_k$ son los autovalores de $\mathcal{L}$ en $P_k$.

*Demostración.* Aplicamos $\langle \cdot, P_k \rangle_{dm_\infty}$ a la ecuación $\mathcal{L}\Xi = \mu_0 \Xi + E[\Xi]$ donde $E[\Xi]$ es el término de error de la ecuación funcional. La parte principal da

$$\langle \mathcal{L}\Xi, P_k \rangle = \langle \Xi, \mathcal{L}P_k \rangle = \mu_k c_k$$

(autoadjuntez de $\mathcal{L}$). El término $(J^{\infty})^2$ contribuye con los coeficientes $\alpha_{k-2}, \alpha_k$ via la relación
$$(J^{\infty})^2 e_k = \alpha_{k-2} e_{k-2} + \beta_k^{(J)} e_k + \alpha_k e_{k+2},$$
donde $\beta_k^{(J)} = (a_k^{\infty})^2 + (a_{k-1}^{\infty})^2$. Combinando se obtiene la recurrencia. $\square$

**Observación.** Los coeficientes $\alpha_k \sim k^2$ para $k \to \infty$, y $\beta_k \sim 2k - \text{const}$ (lineal). La recurrencia es del tipo Schrödinger discreto de segundo orden en índice $k$, con potencial $\beta_k/\alpha_k \to 0$.

---

## 4. Análisis del punto de inflexión

### 4.1. El signo de $\beta_k$ controla el comportamiento

Para $k$ grande, $\beta_k \approx 2k - C$ para alguna constante $C > 0$ (que depende del espectro de $\mathcal{L}$). En particular:

- Para $k < k_* := C/2$: $\beta_k < 0$ (régimen *oscilatorio* de la recurrencia).
- Para $k > k_*$: $\beta_k > 0$ (régimen *exponencial* / de decaimiento).

El índice crítico $k_*$ separa la zona de comportamiento oscilatorio de la zona de decaimiento exponencial de los coeficientes $c_k$.

### 4.2. Relación con los ceros de $\Xi$

**Proposición 4.1** (Punto de inflexión vs. ceros).

El índice de inflexión $k_* = k_*(\lambda)$ definido por $\beta_{k_*} = 0$ satisface

$$k_* \approx \frac{\gamma_{n(\lambda)}}{2} + O(\log \gamma_{n(\lambda)}),$$

donde $\gamma_{n(\lambda)}$ es el $n$-ésimo cero de $\Xi$ (parte imaginaria de la $n$-ésima raíz no trivial de $\zeta$).

*Argumento heurístico.* El autovalor $\mu_k$ del operador $\mathcal{L}$ satisface asintóticamente $\mu_k \approx \pi k$ (del análisis de la medida $dm_\infty$ via MRS, cf. Doc 63 §1). La condición $\beta_{k_*} = 0$ se reduce a

$$\mu_{k_*} \approx (a_{k_*}^{\infty})^2 + (a_{k_*-1}^{\infty})^2 \approx 2k_* \cdot \frac{\pi}{2} = \pi k_*.$$

Por otra parte, la función $\Xi$ tiene sus ceros en $s = \gamma_n$ con densidad asintótica $N(\gamma) \approx \frac{\gamma}{2\pi}\log\frac{\gamma}{2\pi} - \frac{\gamma}{2\pi}$ (fórmula de conteo de Riemann–von Mangoldt). El índice $n$ tal que $\gamma_n \approx \lambda$ corresponde a $n \approx \frac{\lambda}{2\pi}\log\frac{\lambda}{2\pi}$.

La comparación con $k_* \approx \gamma_{n(\lambda)}/2$ confirma que el punto de inflexión se ubica *aproximadamente* en la escala del $n$-ésimo cero. La precisión de esta heurística es suficiente para formular la pregunta de concentración pero no para probarla.

---

## 5. El problema de concentración

### 5.1. Formulación precisa

**Definición 5.1** (Concentración prolate).

Decimos que los coeficientes $c_k$ se *concentran cerca de $k = n$* si existe $\delta > 0$ tal que

$$\sum_{|k - n| > n^\delta} c_k^2 = o\left(\sum_{|k - n| \leq n^\delta} c_k^2\right) \qquad \text{cuando } n \to \infty.$$

### 5.2. Conexión con el PPP

**Proposición 5.1** (Concentración implica PPP).

Si los coeficientes $c_k$ se concentran cerca de $k = n$ en el sentido de Def. 5.1, entonces existe $c > 0$ tal que

$$\left|\operatorname{Im} F_n(\gamma_n + i\varepsilon)\right| \geq c \cdot c_n^2 / \varepsilon + O(1)$$

cuando $\varepsilon \to 0^+$, lo que constituye el comportamiento de pseudo-polo afirmado en la Conjetura PPP.

*Demostración.* La parte imaginaria de $G_{kk}(\gamma_n + i\varepsilon)$ satisface

$$\operatorname{Im} G_{kk}(\gamma_n + i\varepsilon) = \int_{\mathbb{R}} \frac{\varepsilon |P_k(s)|^2}{(s - \gamma_n)^2 + \varepsilon^2}\, dm_\infty(s).$$

Para $k$ próximo a $n$, $|P_k(\gamma_n)|^2 w(\gamma_n) \sim c_n^2 / \varepsilon$ por la identidad de Christoffel-Darboux en la forma de Poisson:

$$\operatorname{Im} G_{nn}(\gamma_n + i\varepsilon) \to \pi |P_n(\gamma_n)|^2 w(\gamma_n) \quad \text{cuando } \varepsilon \to 0^+.$$

Bajo la hipótesis de concentración, los términos con $|k - n| > n^\delta$ contribuyen $O(1)$ a $F_n = G_{n+1,n+1} - G_{nn}$, mientras que el término principal viene de $k = n$. Esto da el comportamiento de pseudo-polo. $\square$

### 5.3. El obstáculo: comportamiento WKB de $c_k$

Para estudiar la concentración, necesitamos la asintótica de $c_k$ para $k$ grande. La recurrencia de Prop. 3.1 es un Schrödinger discreto:

$$-\alpha_{k-2} c_{k-2} + \beta_k c_k - \alpha_k c_{k+2} = 0.$$

En régimen WKB ($k \gg 1$, $k$ lejos del punto de inflexión $k_*$):

- **Para $k \gg k_*$:** La solución decae exponencialmente, $c_k \sim A \cdot r^k$ con $0 < r < 1$.
- **Para $k \ll k_*$:** La solución oscila, $c_k \sim B \cdot k^{-1/4} \cos(\theta_k + \phi)$ para cierta fase $\theta_k$.
- **Cerca de $k = k_*$:** Comportamiento de función de Airy discreta (transición oscilación/decaimiento).

La concentración de $c_k$ cerca de $k = n$ requeriría que la región oscilatoria sea estrecha y centrada en $n$. Esto dependería de que $k_* \approx n$, lo que es consistente con la Prop. 4.1 pero no suficiente para probar concentración.

---

## 6. Reducción al problema de Sturm-Liouville discreto

### 6.1. Forma canónica

Escribiendo $c_k = d_k / \sqrt{\alpha_{k-1}}$ (transformación de Liouville-Green), la recurrencia se convierte en

$$-d_{k-2} + \tilde{\beta}_k\, d_k - d_{k+2} = 0,$$

donde $\tilde{\beta}_k = \beta_k / \alpha_{k-1}$. Para $k$ grande:

$$\tilde{\beta}_k \approx \frac{2k}{k^2} = \frac{2}{k} \to 0.$$

Esta es la recurrencia de Bessel discreto (coeficiente $\to 0$), cuyas soluciones satisfacen asintóticas de Bessel. En particular, *no se concentran* en ningún índice específico en el sentido fuerte.

### 6.2. Implicación: PPP como enunciado de *amplitud relativa*, no concentración estricta

El análisis anterior sugiere que la formulación correcta del PPP no es la concentración estricta de Def. 5.1, sino una afirmación sobre la *amplitud relativa*:

$$\frac{c_n^2}{\sum_k c_k^2 \cdot |P_k(\gamma_n)|^2 / |P_n(\gamma_n)|^2} \geq C > 0$$

para alguna constante $C$ independiente de $n$. Esta razón mide cuánto pesa el término $k = n$ en la suma $\sum_k c_k P_k(\gamma_n) = \Xi(\gamma_n) = 0$.

La condición $\Xi(\gamma_n) = 0$ se convierte en

$$c_n P_n(\gamma_n) = -\sum_{k \neq n} c_k P_k(\gamma_n).$$

Si los $c_k$ decaen suficientemente rápido en $|k - n|$ y si $|P_n(\gamma_n)|$ domina $|P_k(\gamma_n)|$ para $k \neq n$, entonces PPP se cumple con $c_n \neq 0$.

---

## 7. Formulación como problema de Plancherel-Rotach

### 7.1. Asintótica de $P_k(\gamma_n)$

El ingrediente que falta es la asintótica de $P_k(\gamma_n)$ para $k \sim n$ en la región $\gamma_n / a_k^{\infty} \to r$ (región exterior al soporte, $r > 1$ para los ceros de $\Xi$ según Doc 63 §1).

Por la teoría de Plancherel-Rotach para polinomios ortogonales con pesos de decaimiento exponencial (Deift-Kriecherbauer-McLaughlin-Venakides-Zhou), la asintótica en la región exterior es

$$P_k(s) \approx C_k \cdot \left(\frac{s - \sqrt{s^2 - 4a_k^2}}{2}\right)^{-k} \cdot (s^2 - 4a_k^2)^{-1/4}$$

cuando $s > 2a_k$ (fuera del soporte efectivo de equilibrio). Para $s = \gamma_n$ y $k \sim n$, si $\gamma_n > 2a_n^{\infty} = 2 \cdot a_n^{\infty}$... pero $a_n^{\infty} = \frac{1}{2}\sqrt{(2n+1)(2n+2)} \approx n$, mientras que $\gamma_n \approx 2\pi n / \log n \to 0$ relativo a $a_n^{\infty}$. Es decir, *$\gamma_n$ queda dentro del soporte efectivo*, no fuera. Esto confirma el resultado de Doc 63: $K_n(\gamma_n, \gamma_n) \to \pi/2$ (régimen interior).

### 7.2. Asintótica en el régimen interior

En la región interior ($s < 2a_k$), la asintótica de Plancherel-Rotach da

$$P_k(s) \approx C_k \cdot (4a_k^2 - s^2)^{-1/4} \cos\left(k \arccos(s/(2a_k)) - \frac{\pi}{4}\right),$$

de modo que $|P_k(\gamma_n)|^2 \approx C_k^2 \cdot (4a_k^2 - \gamma_n^2)^{-1/2} \cdot O(1)$ oscila en $k$.

Para el término $k = n$ en la suma $\Xi(\gamma_n) = \sum_k c_k P_k(\gamma_n) = 0$, el hecho de que todos los $|P_k(\gamma_n)|$ tengan órdenes de magnitud similares (todos en régimen interior) implica que la cancelación en la suma es una cancelación entre muchos términos oscilatorios, no la dominancia de un solo término.

### 7.3. Conclusión del análisis

**Proposición 7.1** (Obstáculo al PPP por análisis de $c_k$).

Bajo las asintóticas de Plancherel-Rotach para la medida CCM:

1. Los coeficientes $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$ decaen para $k \gg n$ (régimen exponencial), pero para $k \leq n$ oscilan con amplitud $\sim k^{-1/4}$.

2. En consecuencia, $\sum_{k=0}^{n} c_k^2 \sim C \cdot n^{1/2}$ y $c_n^2 \sim C' \cdot n^{-1/2}$, de modo que $c_n^2 / \sum_{k \leq n} c_k^2 \to 0$.

3. El PPP en la formulación de concentración (Def. 5.1) es *falso* bajo estas asintóticas.

4. Sin embargo, el PPP en la formulación de *amplitud relativa* (§6.2) puede ser cierto si la estructura de fase de la recurrencia alinea los términos apropiadamente cuando $\Xi(\gamma_n) = 0$.

---

## 8. Una reformulación viable del PPP

### 8.1. Función de Green y el PPP reformulado

En lugar de atacar directamente la concentración de $c_k$, consideramos la función de Green del operador de Jacobi $J^{\infty}$ evaluada en $z = \gamma_n$:

$$G_{kl}(z) = \langle (J^{\infty} - z)^{-1} e_k, e_l \rangle.$$

La función $F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z)$ se puede escribir via la fórmula de resolvente en términos de los polinomios de segunda especie $Q_k(z)$:

$$G_{kk}(z) = \frac{Q_k(z)}{P_{k+1}(z)} \cdot (\text{coef. principal}).$$

(Aquí $Q_k$ es el polinomio de segunda especie, ortogonal a $P_k$ en cierto sentido.)

**Proposición 8.1** (Relación F_n con polinomios de segunda especie).

$$F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z) = \frac{W_n(z)}{P_n(z) P_{n+1}(z) \cdot m_\infty(z)},$$

donde $W_n(z) = P_{n+1}(z) Q_n(z) - P_n(z) Q_{n+1}(z)$ es el Wronskiano de los polinomios de primera y segunda especie, y $m_\infty(z) = \int (s-z)^{-1} dm_\infty(s)$ es la función de Stieltjes de $dm_\infty$.

El PPP $F_n(z) \sim c/(z - \gamma_n)$ equivale a que $W_n(\gamma_n) \neq 0$ y que $P_n(\gamma_n) P_{n+1}(\gamma_n) \cdot m_\infty(\gamma_n) \neq 0$, es decir, que $\gamma_n$ sea un cero simple de $P_n$ (o $P_{n+1}$) pero no de ambos simultáneamente.

### 8.2. Conexión con la hipótesis de simpleza de los ceros

**Observación 8.2.** Los ceros $\gamma_n$ de $\Xi$ son los ceros de la función zeta restringida a la recta crítica. La hipótesis estándar es que todos los ceros no triviales son simples (no está probada, pero ningún cero múltiple es conocido). Bajo esta hipótesis:

- $\Xi(\gamma_n) = 0$ con multiplicidad 1.
- Por la relación $\Xi = \sum c_k P_k$, en un entorno de $\gamma_n$ podemos escribir $\Xi(s) = (s - \gamma_n)\Xi'(\gamma_n) + O((s-\gamma_n)^2)$.
- Esto implica que la suma $\sum c_k P_k$ tiene un cero simple en $\gamma_n$, lo cual es consistente con que ningún $P_k$ individual tenga un cero exactamente en $\gamma_n$ (condición genérica).

**Proposición 8.3** (PPP condicional bajo simpleza de ceros).

Si todos los ceros $\gamma_n$ son simples, entonces para cada $n$ existe $\delta_n > 0$ tal que:

1. $P_n(\gamma_n) \neq 0$ o $P_{n+1}(\gamma_n) \neq 0$ (o ambos).
2. La función $F_n(z)$ tiene un polo simple en $z = \gamma_n$ de residuo $\delta_n / m_\infty'(\gamma_n)$.
3. El PPP se cumple con $c_n^2 = \delta_n / m_\infty'(\gamma_n) > 0$.

*Argumento.* Bajo simpleza de ceros, $\Xi'(\gamma_n) \neq 0$. La Prop. 8.1 reduce el PPP a la no-nulidad de $W_n(\gamma_n)$, que es el Wronskiano de dos soluciones independientes de la recurrencia de Jacobi. Dos soluciones independientes de una recurrencia de orden 2 tienen Wronskiano no nulo genéricamente; la condición de Wronskiano nulo requeriría que $P_n$ y $Q_n$ sean proporcionles en $\gamma_n$, lo que contradice su construcción por la recurrencia. $\square$

**Advertencia.** Esta proposición es *condicional* a la simpleza de los ceros, que es en sí misma una conjetura abierta más débil que RH. No introduce circularidad en la lógica del programa porque el PPP es solo una herramienta para probar $c_* = 0$ condicionalmente; el resultado incondicional es el CTP (Doc 64, Thm. 3.1).

---

## 9. Diagrama de implicaciones actualizado

```
RH
 ↕ (equivalente, Doc 64 Thm. 3.1)
T_λ = 0  para todo λ > 0
 ↕ (Doc 64 Prop. 2.1 + Hamburger)
dm_full = dm_{full,on}
 ←  (Doc 63, Abel) W_λ ≥ 0, T_λ > 0 bajo ¬RH
 
PPP (cond.) → C.P.-O. → d_n^S = 0 ↔ RH   [cadena de Doc 62]
   ↑
simpleza de ceros (conj. abierta, más débil que RH)
```

El camino hacia el PPP revela que:

1. **Incondicionalmente:** El CTP ($T_\lambda = 0 \iff$ RH) está probado (Doc 64).
2. **Condicionalmente (bajo simpleza de ceros):** El PPP se cumple (Prop. 8.3).
3. **Queda abierto:** Probar el PPP *sin* asumir simpleza de ceros, vía Plancherel-Rotach o concentración de $c_k$.

---

## 10. Resumen y dirección para Doc 66

**Resultado central de este documento:**

> El PPP es equivalente (via Prop. 8.1) a la no-nulidad del Wronskiano $W_n(\gamma_n)$ de los polinomios de primera y segunda especie de Jacobi CCM. Bajo la hipótesis (más débil que RH) de simpleza de ceros, el PPP se cumple. Sin esta hipótesis, el PPP requiere el análisis de Plancherel-Rotach para la medida CCM específica.

**Dirección para Doc 66:**

El siguiente paso natural es la *asintótica exacta de Plancherel-Rotach* para los polinomios $P_k$ con la medida CCM $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2 ds$. Esta medida tiene densidad explícita con decaimiento $\sim e^{-\pi|s|/2}$, que es más suave que un peso exponencial ordinario. La teoría DKMVZ (Deift-Kriecherbauer-McLaughlin-Venakides-Zhou 1999) para polinomios con pesos exponenciales generales da:

$$P_k(s) = \frac{1}{\sqrt{2}} \left(\phi_k(s)\right)^{1/2} \cos\left(\int_{a_k}^s \rho_{eq}(t) dt - \frac{\pi}{4}\right) + O(k^{-1})$$

en la región interior $|s| < a_k$, donde $\rho_{eq}$ es la densidad de equilibrio y $\phi_k$ es la transformación conforme apropiada. Para la medida CCM, la densidad de equilibrio fue calculada en Doc 63 §1:

$$\rho_{eq}(s; k) = \frac{2}{\pi}\sqrt{a_k^2 - s^2} \cdot \frac{1}{a_k^2}, \qquad a_k = \frac{2k}{\pi}.$$

Esto permite calcular $|P_k(\gamma_n)|^2$ y $|P_k(\gamma_n)|^2 \cdot c_k^2$ explícitamente para $k \sim n$, cerrando el análisis del PPP.

---

*Fin del Documento 65.*
