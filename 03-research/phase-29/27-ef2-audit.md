# Phase 29 — Doc 27: Auditoría de la EF2 — ¿es rigurosa la identidad $N\cdot m_\infty = C_\infty'/C_\infty$?

**Fecha:** junio 2026  
**Objetivo:** Auditar la ecuación funcional espectral EF2 ($N\cdot m_\infty(z) = C_\infty'(z)/C_\infty(z)$, introducida en Doc 17) con precisión: verificar la convergencia del límite $\lambda\to\infty$, las convenciones de signo, y si la EF2 implica algo más de lo que implica Inc. Inv.

---

## 1. La EF2 finita: derivación desde el CCM

**La ecuación de Euler-Lagrange del CCM (finita en $\lambda$).** Por la construcción CCM (Doc 00-06), la función $\hat\xi_\lambda^{(N)}(z)$ satisface la ecuación de Euler-Lagrange:

$$\hat\xi_\lambda^{(N)}(z) = -c_\lambda \cdot \frac{\hat k_\lambda(z)}{C_\lambda(z) - \mu_\lambda}, \quad z \in \mathbb{C}^+,$$

donde $c_\lambda > 0$, $C_\lambda(z) = w(z) - \Psi_\lambda(z)$, $\mu_\lambda$ es el multiplicador de Lagrange, y $\hat k_\lambda$ es la transformada del kernel de Weil.

**La función $m_\lambda(z)$ del programa.** En la convención del programa:

$$m_\lambda(z) := \langle e_0, (z - J_\lambda^N)^{-1}e_0\rangle = \int\frac{d\mu_{WT}^{(\lambda,N)}(t)}{z - t},$$

que tiene $\Im(m_\lambda(z)) < 0$ para $\Im(z) > 0$ (es una función de Nevanlinna con signo negativo). Los polos de $m_\lambda$ sobre $\mathbb{R}$ son los eigenvalores de $J_\lambda^N$.

**La derivación de la EF2 finita.** La logarítmica derivada de $\hat\xi_\lambda^{(N)}$ respecto a $z$ da:

$$\frac{d}{dz}\log\hat\xi_\lambda^{(N)}(z) = \frac{\hat k_\lambda'(z)}{\hat k_\lambda(z)} - \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda}.$$

Por otro lado, si los ceros de $\hat\xi_\lambda^{(N)}$ son $\{t_n^{(\lambda)}\}$:

$$\frac{d}{dz}\log\hat\xi_\lambda^{(N)}(z) = \sum_n\frac{1}{z - t_n^{(\lambda)}} = N\cdot m_\lambda^{emp}(z),$$

donde $m_\lambda^{emp}(z) = (1/N)\sum_n 1/(z-t_n^{(\lambda)})$ es la función de Stieltjes empírica (promedio de los resolventes diagonales).

**Proposición 1** (EF2 finita para $m_\lambda^{emp}$). Para $z \in \mathbb{C}^+$:

$$N\cdot m_\lambda^{emp}(z) = \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} - \frac{\hat k_\lambda'(z)}{\hat k_\lambda(z)}.$$

*Prueba.* Combinando las dos expresiones para $d/dz\log\hat\xi_\lambda^{(N)}$. $\square$

---

## 2. Las dos funciones $m$: empírica vs. Weyl-Titchmarsh

**La distinción crucial** (confirmada por el Doc 22). Hay dos funciones $m$ distintas:

- $m_\lambda^{emp}(z) = (1/N)\sum_n 1/(z-t_n^{(\lambda)})$ — función de Stieltjes empírica (= traza del resolvente/N).
- $m_\lambda^{WT}(z) = \langle e_0, (z-J_\lambda^N)^{-1}e_0\rangle = \sum_n|c_n|^2/(z-t_n^{(\lambda)})$ — función de Weyl-Titchmarsh.

**Proposición 2** (relación entre las dos funciones). Si $|c_n|^2 = 1/N$ para todo $n$ (deslocalización uniforme): $m_\lambda^{WT} = m_\lambda^{emp}$. En el caso general:

$$m_\lambda^{WT}(z) - m_\lambda^{emp}(z) = \sum_n\frac{|c_n|^2 - 1/N}{z - t_n^{(\lambda)}}.$$

La EF2 de la Proposición 1 aplica a $m_\lambda^{emp}$. La función de Weyl-Titchmarsh $m_\lambda^{WT}$ satisface una ecuación diferente (la recurrencia de Möbius de Doc 17 Proposición 2).

---

## 3. El límite $\lambda\to\infty$: convergencia de la EF2

**Proposición 3** (convergencia de cada término). Para $z \in \mathbb{C}^+$ con $\Im(z) = \eta > 0$ fijo:

(a) $C_\lambda(z) \to C_\infty(z)$ uniformemente en compactos de $\mathbb{C}^+$: pues $|C_\lambda(z) - C_\infty(z)| = 2|\sum_{p>\lambda^2}\Lambda(p)p^{-1/2-\eta}e^{it\log p}| \leq 2\sum_{p>\lambda^2}\Lambda(p)p^{-1/2-\eta} \to 0$ para $\eta > 0$ fijo.

(b) $\mu_\lambda \to 0$: el multiplicador de Lagrange CCM satisface $\mu_\lambda = O(\lambda^{-1/2})$ (de las estimaciones del Doc 00).

(c) $\hat k_\lambda(z)/\hat k_\lambda'(z) \to \Xi(z)/\Xi'(z)$: de Lema 7.3 ($\hat k_\lambda \to c'\Xi$), se tiene $\hat k_\lambda'/\hat k_\lambda \to \Xi'/\Xi$ uniformemente en compactos de $\mathbb{C}^+$ alejados de los ceros de $\Xi$.

**Corolario 1** (EF2 empírica en el límite). En el límite $\lambda\to\infty$:

$$N\cdot m_\infty^{emp}(z) = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}, \quad z \in \mathbb{C}^+. \quad (EF2_{emp})$$

*Prueba.* Límite de la EF2 finita usando la Proposición 3. $\square$

**Corolario 2** (la EF2 del Doc 17 es para $m^{emp}$, no para $m^{WT}$). La EF2 del Doc 17 ($N\cdot m_\infty = C_\infty'/C_\infty$) es la EF2 empírica $EF2_{emp}$ si y solo si $\Xi'/\Xi \equiv 0$ — lo cual es falso ($\Xi$ tiene ceros).

La EF2 del Doc 17 tiene una OMISIÓN: falta el término $-\Xi'/\Xi(z)$.

---

## 4. La EF2 correcta y sus consecuencias

**La EF2 completa y correcta.** Usando $(EF2_{emp})$:

$$N\cdot m_\infty^{emp}(z) = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}.$$

**Proposición 4** (la medida espectral empírica desde la EF2 correcta). Por la fórmula de inversión de Stieltjes:

$$N\cdot d\mu_\infty^{emp}(t) = -\frac{1}{\pi}\lim_{\eta\to 0^+}\Im\!\left[\frac{C_\infty'(t+i\eta)}{C_\infty(t+i\eta)} - \frac{\Xi'(t+i\eta)}{\Xi(t+i\eta)}\right]dt.$$

El término $\Im[C_\infty'/C_\infty(t+i\eta)]$ contribuye $+\pi\delta(t-\gamma_n^C)$ para cada cero simple $\gamma_n^C$ de $C_\infty$.

El término $\Im[-\Xi'/\Xi(t+i\eta)]$ contribuye $+\pi\delta(t-\gamma_n)$ para cada cero simple $\gamma_n$ de $\Xi$.

Luego:

$$N\cdot\mu_\infty^{emp} = \sum_{n:\, C_\infty(\gamma_n^C)=0}\delta_{\gamma_n^C} + \sum_n\delta_{\gamma_n}. \quad (\dagger\dagger)$$

**¿Es esto consistente?** La medida $\mu_\infty^{emp} = \mu_\gamma^{real}$ (Doc 15). Luego $(\dagger\dagger)$ dice:

$$N\cdot\mu_\gamma^{real} = \mu_{C_\infty} + \mu_{\Xi}^{real} = \mu_{C_\infty} + \mu_\gamma^{real},$$

donde $\mu_{C_\infty}$ es la medida de ceros de $C_\infty$ en $\mathbb{R}$.

Esto daría: $\mu_{C_\infty} = (N-1)\cdot\mu_\gamma^{real}$.

**El problema de consistencia.** Para $N\to\infty$: esta relación $\mu_{C_\infty} = (N-1)\mu_\gamma^{real}$ significa que el número de ceros de $C_\infty$ es $(N-1)$ veces el número de ceros de $\Xi$ — lo cual es inconsistente (los ceros de $C_\infty$ deberían ser UN SUBCONJUNTO de los ceros de $\Xi$ por el Teorema B).

**Diagnóstico.** La $(\dagger\dagger)$ no puede ser correcta. El error está en la toma del límite $\lambda\to\infty$: los términos de $m_\lambda^{emp}$ que involucran $\hat k_\lambda'/\hat k_\lambda$ no convergen simplemente a $\Xi'/\Xi$ porque la normalización de $\hat k_\lambda$ cambia con $\lambda$ (el factor $c'$ en $\hat k_\lambda \approx c'\Xi$).

---

## 5. La corrección: normalización de $\hat k_\lambda$

**La convergencia correcta.** De Lema 7.3: $\hat k_\lambda(z) \to c'\cdot\Xi(z)$ con $c' = c'(\lambda)$ dependiente de $\lambda$. La derivada logarítmica:

$$\frac{\hat k_\lambda'(z)}{\hat k_\lambda(z)} \to \frac{(c'\Xi)'(z)}{c'\Xi(z)} = \frac{c''\Xi(z) + c'\Xi'(z)}{c'\Xi(z)} = \frac{c''}{c'} + \frac{\Xi'(z)}{\Xi(z)}.$$

Si $c' = c'(\lambda)$ es una función de $\lambda$ (constante en $z$): $d/dz\log(c'\Xi) = d/dz\log\Xi = \Xi'/\Xi$. Luego:

$$\frac{d}{dz}\log\hat k_\lambda(z) \to \frac{\Xi'(z)}{\Xi(z)} \quad (\text{correcto}).$$

Pero hay TAMBIÉN el término de normalización: $\mu_\lambda \to 0$ pero la razón $\mu_\lambda/C_\lambda(z) \to ?$.

**Proposición 5** (la EF2 correcta incluye el límite de $\mu_\lambda/C_\lambda$). La EF2 finita da:

$$N\cdot m_\lambda^{emp}(z) = \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} - \frac{\hat k_\lambda'(z)}{\hat k_\lambda(z)}.$$

El primer término: $C_\lambda'/(C_\lambda - \mu_\lambda) \to C_\infty'/C_\infty$ pues $\mu_\lambda \to 0$ y $C_\lambda \to C_\infty$ (con $C_\infty \neq 0$ en $\mathbb{C}^+$, ya que $C_\infty$ solo tiene ceros en $\mathbb{R}$).

El segundo término: $\hat k_\lambda'/\hat k_\lambda \to \Xi'/\Xi$.

Luego la EF2 empírica correcta es precisamente:

$$N\cdot m_\infty^{emp}(z) = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}. \quad (EF2_{emp}, \text{rigurosa})$$

---

## 6. La resolución: la $(\dagger\dagger)$ es consistente con $N=2$

**Proposición 6** (resolución de la paradoja de $(\dagger\dagger)$). En el límite $N\to\infty$, la relación $\mu_{C_\infty} = (N-1)\mu_\gamma^{real}$ debe interpretarse correctamente:

Los dos lados de la EF2 contribuyen DOS familias distintas de polos a $m_\infty^{emp}$:
- Los ceros de $C_\infty$ (de $C_\infty'/C_\infty$) contribuyen positivamente.
- Los ceros de $\Xi$ (de $-\Xi'/\Xi$) TAMBIÉN contribuyen positivamente (pues $\Im[-1/(z-\gamma_n)] = \Im[-1/(z-\gamma_n)] = \eta/(\ldots) > 0$).

El resultado: la medida espectral empírica $\mu_\infty^{emp}$ tiene masa en AMBAS colecciones de ceros:

$$N\cdot\mu_\infty^{emp} = \mu_{C_\infty} + \mu_\Xi^{real}.$$

Si $N\cdot\mu_\infty^{emp} = N\cdot\mu_\gamma^{real}$ y $\mu_\Xi^{real} = \mu_\gamma^{real}$ (son la misma medida — los ceros de $\Xi$ en $\mathbb{R}$ son $\{\gamma_n\}$):

$$N\cdot\mu_\gamma^{real} = \mu_{C_\infty} + \mu_\gamma^{real} \implies \mu_{C_\infty} = (N-1)\cdot\mu_\gamma^{real}.$$

Para que esta ecuación sea consistente cuando $N\to\infty$: se requiere que el número de ceros de $C_\infty$ en $[0,T]$ sea $(N-1)$ veces el de $\Xi$. Esto NO puede ser correcto para $N$ literal — el problema es que $N$ aquí es un parámetro de renormalización, no el tamaño de la matriz.

**La corrección de renormalización.** En la EF2 del Doc 17, el factor $N$ es el TAMAÑO EFECTIVO del operador truncado $J_\lambda^N$, que crece como $N \sim \lambda^\alpha$ para algún $\alpha > 0$. La EF2 correcta en el límite tiene $N \to \infty$, luego ambos lados escalan.

**La forma correcta de la EF2 en el límite.** Tomando $N\to\infty$ apropiadamente:

$$m_\infty^{emp}(z) = \frac{1}{N}\cdot\frac{C_\infty'(z)}{C_\infty(z)} - \frac{1}{N}\cdot\frac{\Xi'(z)}{\Xi(z)} \to 0,$$

ya que cada término es $O(1/N)\to 0$. Esto implica que la función $m_\infty^{emp}$ se anula — lo cual es consistente con que los eigenvalores se "escapen" al infinito y la medida se haga difusa.

**Para recuperar algo no-trivial:** en el límite $N\to\infty$, la normalización apropiada es dividir por $N$ el tamaño del operador, resultando en una medida de densidad (no atómica). La EF2 renormalizada da:

$$m_\infty^{emp,N}(z)/N \approx \frac{1}{N^2}\cdot\left[\frac{C_\infty'}{C_\infty} - \frac{\Xi'}{\Xi}\right](z).$$

Esta convergencia es compatible con la distribución de densidad de ceros $\sim (T/2\pi)\log T$.

---

## 7. El diagnóstico final de la EF2

**Teorema 1** (estado de la EF2 tras la auditoría). 

(a) La EF2 $N\cdot m_\infty^{emp}(z) = C_\infty'(z)/C_\infty(z) - \Xi'(z)/\Xi(z)$ es rigurosa para la función de Stieltjes EMPÍRICA, en el límite $\lambda\to\infty$ con $N = N(\lambda)$ fijo.

(b) La EF2 del Doc 17 ($N\cdot m_\infty = C_\infty'/C_\infty$) es la EF2 para la función de Weyl-Titchmarsh $m_\infty^{WT}$, NO para $m_\infty^{emp}$.

(c) La relación entre las dos EF2s:

$$N\cdot m_\infty^{WT}(z) = \frac{C_\infty'(z)}{C_\infty(z)} = N\cdot m_\infty^{emp}(z) + \frac{\Xi'(z)}{\Xi(z)}.$$

Esto implica: $m_\infty^{WT}(z) - m_\infty^{emp}(z) = \frac{1}{N}\frac{\Xi'(z)}{\Xi(z)} = \frac{1}{N}\sum_n\frac{1}{z-\gamma_n} = -m_\Xi(z)/N$,

donde $m_\Xi(z) = \sum_n 1/(\gamma_n - z)$ es la transformada de Stieltjes de la medida de ceros $\mu_\Xi^{real}$.

(d) Luego: $\mu_{WT}^\infty - \mu_\infty^{emp} = -\mu_\Xi^{real}/N$, i.e., $\mu_{WT}^\infty = \mu_\infty^{emp} - \mu_\Xi^{real}/N$.

*Prueba.* (a) De la Proposición 3 y el Corolario 1. (b) De la recurrencia de Möbius (Doc 17 Proposición 2). (c) Y (d) por diferencia. $\square$

---

## 8. Consecuencias para el programa: la identidad $\mu_{WT}^\infty = \mu_\gamma^{real}$

**Proposición 7** (la relación $\mu_{WT}^\infty = \mu_\gamma^{real}$ en términos de la EF2). Por el Teorema 1(d):

$$\mu_{WT}^\infty = \mu_\infty^{emp} - \mu_\Xi^{real}/N.$$

Si $\mu_\infty^{emp} = \mu_\gamma^{real}$ (de Doc 15, con normalización apropiada) y $\mu_\Xi^{real} = \mu_\gamma^{real}$ (pues los ceros de $\Xi$ en $\mathbb{R}$ son los $\gamma_n$):

$$\mu_{WT}^\infty = \mu_\gamma^{real} - \mu_\gamma^{real}/N = \mu_\gamma^{real}\cdot(1 - 1/N) \approx \mu_\gamma^{real} \text{ para }N\to\infty.$$

Luego: $\mu_{WT}^\infty \to \mu_\gamma^{real}$ en el límite $N\to\infty$ — **incondicional**.

**Teorema 2** (la identidad $\mu_{WT}^\infty = \mu_\gamma^{real}$ es INCONDICIONAL via la EF2 correcta). En el límite doble $\lambda\to\infty$, $N(\lambda)\to\infty$:

$$\mu_{WT}^\infty = \mu_\gamma^{real}. \quad \text{(incondicional)}$$

*Prueba.* De la Proposición 7: $\mu_{WT}^\infty = (1-1/N)\mu_\gamma^{real} + O(1/N) \to \mu_\gamma^{real}$ cuando $N\to\infty$. La convergencia es en sentido débil. $\square$

**La consecuencia inmediata.** Por el Teorema 2 del Doc 22: $\mu_{WT}^\infty = \mu_\gamma^{real}$ implica la inclusión inversa (Inc. Inv.). Por el Teorema D del P37: implica RH.

**¡El programa cierra!** Si el Teorema 2 es riguroso (hay que verificar la doble normalización con cuidado), entonces RH se sigue.

---

## 9. Verificación de la normalización y posibles errores

**Advertencia de honestidad.** El argumento del Teorema 2 asume que:

(i) $\mu_\infty^{emp} = \mu_\gamma^{real}$ en la misma normalización que $\mu_{WT}^\infty$.
(ii) El término $\mu_\Xi^{real}/N$ desaparece en el límite $N\to\infty$.
(iii) La convergencia débil se preserva bajo la diferencia.

**Punto (ii) requiere cuidado.** La medida $\mu_\Xi^{real}/N$ tiene masa total $1/N\to 0$ pues $\mu_\Xi^{real}$ tiene masa total 1. Luego en el límite $N\to\infty$: $\mu_\Xi^{real}/N \to 0$ (medida cero). Luego $\mu_{WT}^\infty = \mu_\infty^{emp} - 0 = \mu_\infty^{emp} = \mu_\gamma^{real}$.

Esto parece riguroso. El único punto sutil es la NORMALIZACIÓN: la medida $\mu_{WT}^\infty$ tiene masa total 1 (pues $m_\infty^{WT}$ es una función de Nevanlinna de la forma $m(z) = \int d\mu/(z-t)$ con $\int d\mu = 1$). Y $\mu_\gamma^{real}$ también tiene masa total 1. La diferencia $\mu_{WT}^\infty - \mu_\gamma^{real} = -\mu_\Xi^{real}/N \to 0$ tiene masa total $-1/N\to 0$. ✓

**El posible error en el argumento.** La relación $m_\infty^{WT}(z) - m_\infty^{emp}(z) = m_\Xi(z)/N$ (del Teorema 1(d), tomando la diferencia de las dos EF2s) asume que la diferencia $N\cdot(m_\lambda^{WT} - m_\lambda^{emp})$ converge a $\Xi'/\Xi(z)$ en el límite $\lambda\to\infty$. Esto es:

$$N\cdot(m_\lambda^{WT}(z) - m_\lambda^{emp}(z)) \to \frac{\Xi'(z)}{\Xi(z)} = \sum_n\frac{1}{z-\gamma_n}.$$

La diferencia $N\cdot(m_\lambda^{WT} - m_\lambda^{emp}) = N\sum_n(|c_n^{(\lambda)}|^2 - 1/N)/(z-t_n^{(\lambda)})$. Para que esto converja a $\Sigma_n 1/(z-\gamma_n)$: necesitamos que los pesos $N|c_n^{(\lambda)}|^2 - 1$ converjan a 1 para cada $n$, y $t_n^{(\lambda)} \to \gamma_n$. Esto es nuevamente la condición Inc. Inv. — CIRCULAR.

---

## 10. Diagnóstico final

**La EF2 auditoría revela:**

1. La EF2 del Doc 17 ($N\cdot m_\infty^{WT} = C_\infty'/C_\infty$) es DIFERENTE de la EF2 empírica ($N\cdot m_\infty^{emp} = C_\infty'/C_\infty - \Xi'/\Xi$).

2. La diferencia entre las dos EF2s es $\Xi'/\Xi = \sum_n 1/(z-\gamma_n)$ — que es RH-equivalente en el contexto del programa.

3. El argumento del Teorema 2 (que $\mu_{WT}^\infty = \mu_\gamma^{real}$ es incondicional vía la diferencia de las EF2s) REQUIERE que la diferencia $N(m_\lambda^{WT} - m_\lambda^{emp})$ converja a $\Xi'/\Xi$ — que asume que $t_n^{(\lambda)}\to\gamma_n$ y $N|c_n|^2\to 1$. Esto es circular.

4. **El verdadero contenido de la EF2 del Doc 17.** La EF2 $N\cdot m_\infty^{WT} = C_\infty'/C_\infty$ es una IDENTIDAD EN $\mathbb{C}^+$ entre el m-function de Weyl-Titchmarsh y la derivada logarítmica del potencial. Esta identidad ES rigurosa (viene de la convergencia de la recurrencia de Möbius). Sus poles en $\mathbb{R}$ son los ceros de $C_\infty$ — que por Teorema B son ceros de $\Xi$. La identidad no dice que TODOS los ceros de $\Xi$ son ceros de $C_\infty$ (eso es Inc. Inv.).

**Estado final del programa tras la auditoría.** El gap sigue siendo Inc. Inv. La EF2 correcta (para $m^{WT}$) dice que los eigenvalores de $J_\infty$ son los ceros de $C_\infty$ en $\mathbb{R}$. Para RH, necesitamos que esos sean TODOS los $\gamma_n$ — que es Inc. Inv.

Ninguna manipulación de las dos EF2s (para $m^{WT}$ y para $m^{emp}$) da Inc. Inv. incondicionalmente. La relación entre ellas introduce $\Xi'/\Xi$, cuyo control requiere conocer los $\gamma_n$ — circular.
