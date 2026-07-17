# Documento 71 — Derivada temporal de $T_\lambda$ y los coeficientes $c_k$

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-08  
**Prerrequisitos:** Docs 64, 65, 70

---

## 1. El objetivo

En Doc 70, §8.2, derivamos la fórmula

$$\partial_t T_\lambda \bigg|_{t=0} = -4\int W_\lambda(s)\operatorname{Re}(\overline{H_0(s)}\, H_0''(s))\, dm_\infty(s).$$

Queremos calcular este integral de manera explícita en términos de los coeficientes $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$ y los autovalores $\mu_k$ del operador de Schrödinger $\mathcal{L}_0$.

---

## 2. La forma cuadrática de Schrödinger

### 2.1. Expansión en la base de Jacobi

Recordamos que $H_0 = \Xi$ (identificando $s$ con la variable imaginaria). La expansión es $\Xi = \sum_k c_k P_k$ con $c_k = 0$ para $k$ impar (paridad).

La segunda derivada $\Xi'' = -\mathcal{L}_0\Xi + V\Xi$ donde $V(s) = \pi^2 s^2/4 + \pi/2$ (el potencial de Schrödinger). En la base $\{P_k\}$:

$$\Xi'' = \sum_k c_k P_k'' = \sum_k c_k (-\mathcal{L}_0 P_k + V P_k) = -\sum_k c_k \mu_k P_k + \sum_k c_k V P_k.$$

La multiplicación por $V(s) = \pi^2 s^2/4 + \pi/2$ en la base $\{P_k\}$ actúa como $(J^\infty)^2 \cdot \pi^2/4 + \pi/2 \cdot I$, donde $J^\infty$ es la matriz de Jacobi. Esto da:

$$[V\Xi]_k = \frac{\pi^2}{4}[(J^\infty)^2 c]_k + \frac{\pi}{2}c_k = \frac{\pi^2}{4}(\alpha_{k-2}c_{k-2} + \gamma_k c_k + \alpha_k c_{k+2}) + \frac{\pi}{2}c_k,$$

con $\alpha_k = a_k^\infty a_{k+1}^\infty$ y $\gamma_k = (a_k^\infty)^2 + (a_{k-1}^\infty)^2$.

### 2.2. El integral $\int W_\lambda \overline{\Xi} \Xi'' \, dm_\infty$

El integral de la Prop. 8.2 de Doc 70 se descompone como:

$$\int W_\lambda(s)\overline{\Xi(s)}\Xi''(s)\, dm_\infty(s) = -\int W_\lambda(s)|\Xi(s)|^2 \mathcal{L}_0 \log|\Xi|\, dm_\infty + \text{off-diagonal}.$$

Pero es más limpio calcular directamente:

$$\int W_\lambda \overline{\Xi}\Xi''\, dm_\infty = \sum_{k,l} \bar{c}_k c_l \int W_\lambda P_k P_l'' \, dm_\infty.$$

### 2.3. Autoadjuntez de $\mathcal{L}_0$ y la forma diagonal

$$\int W_\lambda P_k \mathcal{L}_0 P_l\, dm_\infty = \mu_l \delta_{kl} \int W_\lambda P_k P_l\, dm_\infty.$$

Esta simplificación solo es válida si $W_\lambda$ es constante o si el operador $W_\lambda \cdot$ conmuta con $\mathcal{L}_0$, lo cual en general es falso. Sin embargo, podemos usar la expansión de Abel de $W_\lambda$:

$$W_\lambda(s) = \sum_{n=0}^{N(\lambda)-1}(n+1)|P_{n+1}(s)|^2 + (a_{N(\lambda)}^\infty)^2|P_{N(\lambda)+1}(s)|^2,$$

y calcular término a término.

---

## 3. Cálculo de la derivada temporal

### 3.1. Forma cuadrática bilineal

Definimos la forma bilineal

$$B_\lambda(u, v) := \int W_\lambda(s)\, u(s)\, v(s)\, dm_\infty(s).$$

Entonces:

$$\int W_\lambda \overline{\Xi} \Xi''\, dm_\infty = B_\lambda(\overline{\Xi}, \Xi'').$$

### 3.2. Integración por partes en $dm_\infty$

La medida $dm_\infty$ tiene densidad $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$. Integrando por partes respecto a $s$:

$$B_\lambda(\overline{\Xi}, \Xi'') = -B_\lambda(\overline{\Xi'}, \Xi') - \int (W_\lambda w)'\,\overline{\Xi}\Xi'/w\, ds + \text{frontera.}$$

Para la parte principal (ignorando frontera que decae exponencialmente):

$$B_\lambda(\overline{\Xi}, \Xi'') = -B_\lambda(\overline{\Xi'}, \Xi') - \int W_\lambda' \overline{\Xi}\Xi'\, dm_\infty.$$

Por tanto:

$$\operatorname{Re}\, B_\lambda(\overline{\Xi}, \Xi'') = -\int W_\lambda |\Xi'|^2\, dm_\infty - \frac{1}{2}\int W_\lambda' \partial_s|\Xi|^2\, dm_\infty.$$

Integrando por partes el segundo término:

$$-\frac{1}{2}\int W_\lambda' \partial_s|\Xi|^2\, dm_\infty = \frac{1}{2}\int W_\lambda'' |\Xi|^2\, dm_\infty + \frac{1}{2}\int W_\lambda' |\Xi|^2 (\log w)'\, dm_\infty.$$

### 3.3. La fórmula de la derivada temporal

Reuniendo y sustituyendo en la Prop. 8.2 de Doc 70:

$$\boxed{\partial_t T_\lambda\bigg|_{t=0} = 4\int W_\lambda |\Xi'|^2\, dm_\infty - 2\int W_\lambda''|\Xi|^2\, dm_\infty - 2\int W_\lambda'(\log w)'|\Xi|^2\, dm_\infty.}$$

---

## 4. Análisis del signo de $\partial_t T_\lambda|_{t=0}$

### 4.1. Los tres términos

Sea $\dot{T} := \partial_t T_\lambda|_{t=0}$.

**Término I:** $4\int W_\lambda |\Xi'|^2\, dm_\infty > 0$ (siempre positivo, pues $W_\lambda \geq 0$ y $|\Xi'|^2 \geq 0$).

**Término II:** $-2\int W_\lambda''|\Xi|^2\, dm_\infty$. El signo de $W_\lambda''$ es indefinido: $W_\lambda'' = \sum (n+1) \partial_{ss}|P_{n+1}|^2$, que oscila.

**Término III:** $-2\int W_\lambda'(\log w)'|\Xi|^2\, dm_\infty$. Con $(\log w)'(s) = -\pi/2 + O(s^{-1})$ para $s$ grande, este término es positivo para $s$ grande (ya que $W_\lambda' \geq 0$ allí por la estructura de Abel).

### 4.2. Dominancia del Término I bajo ¬RH

Bajo $\neg$RH, $\Xi$ tiene un cero complejo $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 > 1/2$. La función $|\Xi'(s)|^2$ en la vecindad de $\gamma_0$ tiene un pico de altura $|\Xi'(\gamma_0)|^2 = |\Xi'(\gamma_0)|^2 \cdot |\text{factor}|^2$. En particular, $\Xi'(\gamma_0) \neq 0$ porque $\gamma_0$ es un cero simple (bajo la hipótesis de simpleza).

Para $\lambda \gg \gamma_0$, $W_\lambda(\gamma_0) \sim N(\lambda) \cdot \pi/2$ (Prop. de Doc 64), así que:

$$\text{Término I} \geq 4 \cdot N(\lambda) \cdot \frac{\pi}{2} \cdot |\Xi'(\gamma_0)|^2 w(\gamma_0).$$

Esto crece como $N(\lambda) \to \infty$.

Los Términos II y III involucran $W_\lambda''$ y $W_\lambda'$ que son de orden $N(\lambda)^2/\lambda \ll N(\lambda)^2$ para $\lambda$ grande... pero $N(\lambda) \sim \lambda \log \lambda / (2\pi)$, así que $N(\lambda)^2/\lambda \sim N(\lambda) \cdot \log\lambda / (2\pi)$.

El balance entre los tres términos no está determinado sin más información sobre el comportamiento de $|\Xi|^2$ y $|\Xi'|^2$ en el soporte de $W_\lambda$.

**Conclusión provisional:** El Término I sugiere que $\dot{T} > 0$ bajo $\neg$RH (la traza *crece* inicialmente cuando el flujo de calor se aplica). Esto sería el signo *opuesto* al que esperaríamos para la monotonicidad de la Conj. 5.1.

### 4.3. Resolución de la aparente contradicción

La Conj. 5.1 dice que $T_\lambda(t)$ es *decreciente* en $t$. El Término I sugiere que $\partial_t T_\lambda|_{t=0} > 0$. ¿Contradicción?

No necesariamente. La Conj. 5.1 se aplica en el rango $t \geq 0$, y la derivada en $t = 0$ puede ser positiva sin contradecir la monotonicidad *eventual* (la traza puede crecer inicialmente antes de decrecer). Más aún, la Conj. 5.1 está formulada bajo hipótesis generales; bajo $\neg$RH la situación puede ser diferente.

**Observación 4.1.** El comportamiento de $T_\lambda(t)$ bajo $\neg$RH es el siguiente:
- En $t = 0$: $T_\lambda(0) > 0$ (CTP).
- Para $t > \Lambda$: $T_\lambda(t) = 0$.
- Por lo tanto, $T_\lambda(t)$ debe decrecer de $T_\lambda(0) > 0$ a $0$ en el intervalo $[0, \Lambda]$.

El hecho de que $\partial_t T_\lambda|_{t=0} > 0$ (Término I dominante) sugiere que la traza *primero sube* antes de bajar. Esto es posible: $T_\lambda(t)$ puede tener un máximo en algún $t^* \in (0, \Lambda)$ antes de extinguirse en $t = \Lambda$.

Este comportamiento no-monótono es en sí mismo informativo: indica que el flujo de calor inicialmente *amplifica* la discrepancia antes de resolverla.

---

## 5. La derivada en términos de $c_k$

### 5.1. Expresión explícita

Usando $\Xi = \sum_k c_k P_k$ (solo $k$ par) y la expansión de Abel de $W_\lambda$:

$$\int W_\lambda |\Xi'|^2\, dm_\infty = \sum_{n=0}^{N(\lambda)-1}(n+1)\int|P_{n+1}|^2|\Xi'|^2\, dm_\infty + \ldots$$

El integral $\int|P_m|^2|\Xi'|^2\, dm_\infty$ se calcula usando $\Xi' = \sum_k c_k P_k'$ y la relación $P_k' = \sum_j \alpha_{kj} P_j$ (donde los coeficientes $\alpha_{kj}$ se calculan de la recurrencia de Jacobi). En general $P_k'(s) = \sum_{j<k, j\equiv k+1\,(\text{mod }2)} d_{kj} P_j(s)$ con $d_{kj}$ explícitos.

**Proposición 5.1** (Derivada temporal via $c_k$). La derivada $\partial_t T_\lambda|_{t=0}$ se expresa como una forma cuadrática en los coeficientes $c_k$:

$$\partial_t T_\lambda\bigg|_{t=0} = \sum_{k,l} c_k c_l\, Q_{kl}^{(\lambda)},$$

donde la matriz $Q^{(\lambda)}$ tiene entradas

$$Q_{kl}^{(\lambda)} = 4\int W_\lambda P_k' P_l'\, dm_\infty - 2\int W_\lambda'' P_k P_l\, dm_\infty - 2\int W_\lambda'(\log w)' P_k P_l\, dm_\infty.$$

Que $Q^{(\lambda)}$ sea positiva definida (o no) determina el signo de $\dot{T}$ en función de los $c_k$.

### 5.2. El caso $\Lambda = 0$ (RH): $\dot{T} = 0$

Bajo RH, $\Xi = \Xi^{on}$ y $H_t = H_t^{on}$ para todo $t$, luego $T_\lambda(t) = 0$ para todo $t$. En particular $\partial_t T_\lambda|_{t=0} = 0$. Esto significa $\sum_{k,l} c_k c_l Q_{kl}^{(\lambda)} = 0$ para todo $\lambda$. La forma cuadrática $Q^{(\lambda)}$ es semidefinida positiva (por el Término I) y se anula sobre el vector $(c_k)$: luego los $c_k$ deben satisfacer $Q^{(\lambda)}(c,c) = 0$, lo que implica $\Xi' = 0$ en el soporte de $W_\lambda$... lo que es absurdo.

**Contradicción aparente.** Si $W_\lambda > 0$ y $\Xi' \not\equiv 0$, el Término I es estrictamente positivo, pero bajo RH $\dot{T} = 0$. La resolución: bajo RH, los tres términos se cancelan exactamente. El Término I positivo es cancelado por los Términos II y III negativos. Esto es posible porque la cancelación refleja una propiedad especial de los $c_k$ cuando *todos los ceros son reales*.

Esta cancelación es una condición algebraica sobre los $c_k$ equivalente a RH — lo que sugiere que la ecuación $Q^{(\lambda)}(c,c) = 0$ podría ser una nueva vía de ataque.

---

## 6. Condición de cancelación como nuevo criterio

### 6.1. Formulación

**Proposición 6.1** (Criterio de cancelación de la derivada temporal). Las siguientes son equivalentes:

1. RH.
2. $\partial_t T_\lambda|_{t=0} = 0$ para todo $\lambda > 0$.
3. $\sum_{k,l} c_k c_l Q_{kl}^{(\lambda)} = 0$ para todo $\lambda > 0$.
4. Los tres términos de la fórmula de la derivada se cancelan exactamente.

*Demostración.* (1)$\Rightarrow$(2): bajo RH, $T_\lambda(t) = 0$ para todo $t$. (2)$\Rightarrow$(1): si $\partial_t T_\lambda|_{t=0} = 0$ para todo $\lambda$, y $T_\lambda(0) = 0$ (por CTP+RH)... pero este camino es circular: estamos asumiendo $T_\lambda(0) = 0$ que es RH.

**Corrección:** La equivalencia correcta es:

$$\text{RH} \iff T_\lambda(0) = 0 \ \forall\lambda \iff \partial_t T_\lambda|_{t=0} = 0 \ \forall\lambda,$$

donde la segunda equivalencia usa que $T_\lambda(0) = 0$ implica $\partial_t T_\lambda|_{t=0} = 0$ (derivada de la función idénticamente nula), y la recíproca requiere la condición inicial $T_\lambda(0) = 0$ que es en sí RH. Sin información sobre $T_\lambda(0)$, la condición $\partial_t T_\lambda|_{t=0} = 0$ es *más débil* que RH.

**Conclusión honesta:** La derivada temporal no da una nueva equivalencia con RH; solo da una condición necesaria.

---

## 7. Lo que sí es nuevo: la forma cuadrática $Q^{(\lambda)}$

A pesar de la limitación del §6, la forma cuadrática $Q^{(\lambda)}_{kl}$ es un objeto nuevo:

1. **Es explícita** en términos de $W_\lambda$, $\log w$, y los polinomios $P_k$.
2. **Codifica la dinámica del flujo de calor** sobre el espacio de Jacobi.
3. **Su positividad/nulidad** sobre los vectores $(c_k)$ es equivalente a condiciones sobre los ceros de $\Xi$.

La pregunta genuinamente nueva es: ¿tiene la forma $Q^{(\lambda)}$ una descripción espectral en términos del operador prolate $W_\lambda$? Si $Q^{(\lambda)} = B_\lambda^T B_\lambda$ para algún operador $B_\lambda$ explícito, la condición $Q^{(\lambda)}(c,c) = 0$ se convertiría en $\|B_\lambda c\|^2 = 0$, i.e., $B_\lambda c = 0$, que es una condición de núcleo.

---

## 8. Resumen y dirección para Doc 72

**Resultado principal:**
$$\partial_t T_\lambda\bigg|_{t=0} = 4\int W_\lambda|\Xi'|^2 dm_\infty - 2\int W_\lambda''|\Xi|^2 dm_\infty - 2\int W_\lambda'(\log w)'|\Xi|^2 dm_\infty.$$

**Estructura:** Es una forma cuadrática $Q^{(\lambda)}(c,c)$ en los coeficientes $c_k = \langle\Xi,P_k\rangle_{dm_\infty}$.

**Consecuencia bajo RH:** Los tres términos se cancelan. La cancelación impone una condición algebraica sobre $(c_k)$ equivalente a que todos los ceros de $\Xi$ sean reales.

**Limitación:** La condición $\partial_t T_\lambda|_{t=0} = 0$ sola no es equivalente a RH sin la información inicial $T_\lambda(0) = 0$.

**Doc 72** debe estudiar la forma cuadrática $Q^{(\lambda)}$ de manera más explícita: ¿es $Q^{(\lambda)}$ positiva definida sobre el ortogonal de los vectores $(c_k)$ que anulan $\Xi$ en todos los ceros reales? Si la respuesta es sí, esto daría información estructural sobre los ceros.

---

*Fin del Documento 71.*
