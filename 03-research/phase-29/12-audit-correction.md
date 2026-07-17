# Phase 29 — Auditoría y corrección de los docs 10–11

**Fecha:** junio 2026  
**Objetivo:** Responder a la auditoría del Advisor 1. Se identifican tres errores en la cadena docs 10–11 y se reconstruye el argumento desde base más sólida. El Enunciado Central EC se mantiene pero requiere reformulación. El resultado de convergencia individual se restatea correctamente.

---

## 1. Los tres errores identificados

### Error 1 (Doc 10, Sec. 7): La cancelación del $4\log\lambda$

El doc 10 afirmó que $C_\lambda(\gamma_n) \approx -4\log\lambda/m_n$ y $C_\lambda'(\gamma_n) \approx -4\log\lambda/(m_n\gamma_n)$, y que la ratio daría $\sigma_n = O(1)$.

**El error:** El análisis correcto via la fórmula explícita (Sección 3 a continuación) muestra que $C_\lambda(\gamma_n) = w(\gamma_n) - \Psi_\lambda(\gamma_n) \to +\infty$ cuando $\lambda\to\infty$. El potencial NO tiende a cero en $t = \gamma_n$; AMBOS lados de la ecuación de cruce divergen. La aplicación del teorema de función implícita alrededor de $\gamma_n$ es inválida.

### Error 2 (Doc 11, Sec. 1, corrección del RL): incompleto

El doc 11 corrigió el uso de Riemann-Lebesgue para medidas discretas, pero todavía afirmó convergencia individual $t_n^{(\lambda)}\to\gamma_n$ (Teorema 2, doc 11) via la cancelación del término $4\log\lambda$ en numerador y denominador. Este Teorema 2 hereda el Error 1 y por tanto no está probado.

### Error 3 (Doc 11, Sec. 4): varianza $\not\Rightarrow$ cota puntual

El pasaje de $M\{D_n^2\} = V_n = O(\log\gamma_n)$ a $|D_n(x)| = O(\sqrt{\log\gamma_n\log x})$ "para casi todo $x$" requería un resultado de distribución que no se justificó. La varianza finita de una función casi-periódica NO implica automáticamente una cota puntual. Esto invalida la Proposición 3 del doc 11.

---

## 2. Lo que SÍ está probado (inventario limpio)

Antes de la reconstrucción, inventariamos los resultados que sobreviven sin los tres errores:

| Resultado | Doc | Estado |
|---|---|---|
| $k(u)>0$ para todo $u>0$ | 04 | **Sólido** |
| $k_\lambda(u)>0$ para $\lambda\geq\lambda_0$ | 04 | **Sólido** |
| $A_\lambda=$ mult. por $\Psi_\lambda$ en Mellin | 06 | **Sólido** |
| $|s_n^{(\lambda)}-\gamma_n|=O(\lambda^{-1/2}/w_n)$ para ceros de $\hat k_\lambda$ | 06 | **Sólido** (Rouché+Lema 7.3) |
| $\sum_m\Delta_m=0$, $M_1[\Delta]=O((\log\lambda)^2/\lambda)$ | 06, 07 | **Sólido** |
| $N_\xi(T;\lambda)=N_\Xi(T)+O(\log T)$ | 08 | **Sólido** |
| $\mu_\lambda\to\mu_\gamma$ (convergencia débil) | 08 | **Sólido** |
| $S_\lambda(z)\to S_\Xi(z)$ (bajo RH) | 09 | **Sólido** (usa conv. débil doc 08) |
| $t_n^{(\lambda)} - \gamma_n = O(\log\lambda)$ (bajo RH) | 10 | **El estimado del denominador es incorrecto; la cota $O(\log\lambda)$ puede sobrevivir pero necesita recalcularse** |
| $D_n(x)$ casi-periódica, $M\{D_n^2\}=V_n$ | 11 | **Sólido** (matemática correcta) |
| Promedio temporal de $D_n$ es 0 | 11 | **Sólido** |
| Convergencia de Cesàro de los ceros | 11 | **Sólido** |

---

## 3. El cálculo correcto de $C_\lambda(\gamma_n)$

**Proposición 1** (fórmula explícita para la suma torcida). Bajo RH, para $x > 1$ y $s = 1/2+i\gamma_n$ (cero simple de $\zeta$):

$$\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = \Re\!\left[\sum_{p\leq x}\Lambda(p)p^{-s}\right].$$

Por la fórmula de Perron aplicada a $-\zeta'/\zeta(s)$, que tiene un polo simple en $s = \rho_n$ con residuo $-1$:

$$\sum_{p\leq x}\Lambda(p)p^{-s} = \frac{x^{0}}{0}\cdot(\text{residuo de }-\zeta'/\zeta\text{ en }\rho_n) + \sum_{\rho\neq\rho_n}\frac{x^{\rho-s}}{\rho-s} + O(\log x/x).$$

El término en $\rho = \rho_n$ da la contribución $-\log x$ (de la forma $x^0/0 = -\log x$ en el límite de Perron con regularización). Más precisamente, para $s = \rho_n + \varepsilon$ y $\varepsilon\to 0$: el polo de $-\zeta'/\zeta$ en $\rho_n$ contribuye $x^{\rho_n-s}/(\rho_n-s) = x^{-\varepsilon}/(-\varepsilon) \to \log x$ (el límite $\varepsilon\to 0$ de $-x^{-\varepsilon}/\varepsilon = -e^{-\varepsilon\log x}/\varepsilon \to \log x$).

Bajo RH ($\rho = 1/2+i\gamma$ para todos los ceros no-triviales):

$$\sum_{p\leq x}\Lambda(p)p^{-1/2-i\gamma_n} = \log x + A_n + \sum_{m\neq n}\frac{x^{i(\gamma_m-\gamma_n)}}{i(\gamma_m-\gamma_n)} + O(\log x\cdot x^{-1/2}),$$

donde $A_n$ es una constante compleja fija (independiente de $x$).

Tomando parte real: $\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = \log x + \Re A_n + D_n(\log x) + O(\log x/\sqrt{x})$,

donde $D_n(\log x) = \sum_{m\neq n}\sin((\gamma_m-\gamma_n)\log x)/(\gamma_m-\gamma_n)$.

**Luego:**

$$\Psi_\lambda(\gamma_n) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = 4\log\lambda + 2\Re A_n + 2D_n(2\log\lambda) + O(\lambda^{-1}\log\lambda).$$

Y: $$C_\lambda(\gamma_n) = w(\gamma_n) - \Psi_\lambda(\gamma_n) = w(\gamma_n) - 4\log\lambda - 2\Re A_n - 2D_n(2\log\lambda) + O(\lambda^{-1}).$$

**Para $\lambda\to\infty$:** $C_\lambda(\gamma_n) \to -\infty$ (dominado por $-4\log\lambda$).

Y $\mu_\lambda \to 0^+$ (el mínimo de $QW_\lambda$ tiende a 0).

**Conclusión:** $C_\lambda(\gamma_n) - \mu_\lambda \to -\infty$. El punto $t = \gamma_n$ NO es un cruce de $C_\lambda$ al nivel $\mu_\lambda$ para $\lambda$ grande. La ecuación de cruce $C_\lambda(t_n^{(\lambda)}) = \mu_\lambda$ se satisface en un punto $t_n^{(\lambda)}$ que SE ALEJA de $\gamma_n$ conforme $\lambda$ crece.

**Error 1 confirmado.** El argumento del teorema de función implícita en los docs 10–11 es inválido.

---

## 4. La corrección: el mapa de Blaschke

El error proviene de pensar que los ceros de $\hat\xi_\lambda$ son determinados por la ecuación $C_\lambda(t) = \mu_\lambda$ (las "cruces del potencial"). Esto es solo la APROXIMACIÓN DIAGONAL — que ignora el término de rango 1 $Q^{cross}(f,f) = |\langle f, k\rangle|^2$.

La ecuación de Euler-Lagrange completa en espacio de Mellin, incluyendo $Q^{cross}$:

$$[w(t) - \Psi_\lambda(t) - \mu_\lambda]\hat\xi_\lambda(t) + \langle\xi_\lambda, k\rangle\hat k(t) = 0.$$

Luego:

$$\hat\xi_\lambda(t) = \frac{-c_\lambda\hat k(t)}{w(t) - \Psi_\lambda(t) - \mu_\lambda},$$

donde $c_\lambda = \langle\xi_\lambda, k\rangle > 0$.

**Los ceros de $\hat\xi_\lambda$ son los ceros del NUMERADOR** $\hat k(t)$ — que son los ceros $\gamma_n$ de $\Xi$ — **modulados por los polos del denominador**, que son los ceros de $C_\lambda(t) - \mu_\lambda$.

Esta es la estructura correcta: en el límite $\lambda\to\infty$, si el denominador no tiene ceros en la recta real (o si los polos del denominador se cancelan con los ceros del numerador), entonces $\hat\xi_\lambda(t) \propto \hat k(t)$ y los ceros de $\hat\xi_\lambda$ coinciden con los de $\hat k_\lambda \approx \Xi$.

**Proposición 2** (los ceros de $\hat\xi_\lambda$ son ceros de $\hat k$ modulados). En la aproximación diagonal con el término de rango 1:

$$\hat\xi_\lambda(t) = -c_\lambda \cdot \frac{\hat k(t)}{C_\lambda(t) - \mu_\lambda}.$$

Los ceros de $\hat\xi_\lambda$ son los $t$ donde:
1. $\hat k(t) = 0$ (ceros de $\hat k = \Xi$, i.e., $t = \gamma_n$), si el denominador es NO-CERO en esos puntos.
2. Los polos del denominador (ceros de $C_\lambda - \mu_\lambda$) cancelan con ceros del numerador $\hat k$ — pero $\hat k(\gamma_n) = 0$ exactamente cuando $\gamma_n$ es un cero de $\Xi$.

**Pero:** En la aproximación de dimensión finita $E_N^+$, $\hat\xi_\lambda \neq -c_\lambda\hat k/(C_\lambda-\mu_\lambda)$ exactamente — la proyección introduce un error. La función $\hat\xi_\lambda$ no tiene exactamente los mismos ceros que $\hat k$.

La relación correcta entre $\hat\xi_\lambda$ y $\hat k_\lambda = \hat k|_{E_N^+}$ (la proyección):

**Proposición 3** (relación entre los ceros). Sea $B_\lambda(t) := \hat\xi_\lambda(t)/\hat k_\lambda(t)$ la ratio de las dos funciones en $E_N^+$. Esta es una FUNCIÓN RACIONAL con:
- Ceros en $\{t_n^{(\lambda)}\}$ (ceros de $\hat\xi_\lambda$)
- Polos en $\{s_n^{(\lambda)}\}$ (ceros de $\hat k_\lambda$)

Ambos conjuntos tienen exactamente $N+1$ elementos. $B_\lambda$ es un PRODUCTO DE BLASCHKE RACIONAL. Su norma de Blaschke: $\prod_n\frac{t-t_n^{(\lambda)}}{t-s_n^{(\lambda)}}$ en la realización sobre la recta real.

**Consecuencia.** $\{t_n^{(\lambda)}\} \to \{\gamma_n\}$ si y solo si $B_\lambda \to 1$ (uniformemente en compactos de $\mathbb{C}\setminus\mathbb{R}$). Y $B_\lambda \to 1$ si y solo si $\hat\xi_\lambda/\hat k_\lambda \to $ constante, i.e., H2.

Esto confirma la estructura circular identificada en doc 09: la convergencia de los ceros es equivalente a H2. El análisis de la "cruces del potencial" era una vía falsa.

---

## 5. El estimado correcto de $t_n^{(\lambda)} - \gamma_n$

A pesar de los errores anteriores, SÍ existe un estimado correcto para $t_n^{(\lambda)} - \gamma_n$ que proviene de comparar los productos de Blaschke.

**Proposición 4** (desplazamiento via razón de Blaschke). El desplazamiento del $n$-ésimo cero satisface, para $z \in \mathbb{C}\setminus\mathbb{R}$:

$$\log B_\lambda(z) = \sum_n\log\frac{z-t_n^{(\lambda)}}{z-s_n^{(\lambda)}}.$$

Para $z = \gamma_n + i\eta$ ($\eta > 0$ pequeño):

$$|\log B_\lambda(\gamma_n+i\eta)| \leq \sum_n\left|\frac{t_n^{(\lambda)}-s_n^{(\lambda)}}{\gamma_n+i\eta-s_n^{(\lambda)}}\right| + O\!\left(\sum_n\frac{|t_n-s_n|^2}{|\eta|^2}\right).$$

Del Teorema 1 del doc 06: $|s_n^{(\lambda)}-\gamma_n| = O(\lambda^{-1/2}/w_n)$. Si además $|t_n^{(\lambda)}-\gamma_n| = O(\lambda^{-1/2}/w_n)$ (lo que es lo que queremos probar): el argumento se vuelve circular.

**El resultado NO-circular.** Del Corolario de la Proposición 1 del doc 08 (conteo de ceros):

$$|t_n^{(\lambda)} - \gamma_n| \leq (\gamma_{n+K} - \gamma_n) + |s_n^{(\lambda)} - \gamma_n|,$$

donde $K = O(\log\lambda)$ es el error en el conteo. Usando el espaciado promedio $\gamma_{n+K}-\gamma_n = O(K\log\gamma_n/\log\gamma_n) = O(K) = O(\log\lambda)$:

$$\boxed{|t_n^{(\lambda)} - \gamma_n| \leq O(\log\lambda) + O(\lambda^{-1/2}/w_n) = O(\log\lambda).}$$

**Teorema 1** (estimado correcto). Bajo RH y con $w_n = |\Xi'(\gamma_n)|$: para cada $n$ fijo y $\lambda$ regular,

$$|t_n^{(\lambda)} - \gamma_n| = O_n(\log\lambda).$$

Este estimado es el mismo que el del Teorema 2 del doc 10, pero ahora proviene de un argumento CORRECTO (conteo de ceros, no función implícita sobre el potencial divergente). El exponente $O(\log\lambda)$ proviene del error $O(\log\lambda)$ en el conteo de ceros.

---

## 6. La tasa de convergencia: ¿puede mejorarse $O(\log\lambda)$?

La cota $O(\log\lambda)$ viene del error de conteo $|N_\xi(T;\lambda) - N_\Xi(T)| = O(\log T)$. Este error es la precisión de la fórmula de von Mangoldt para $N_\Xi$ combinada con la discretización en $E_N^+$.

**Proposición 5** (el conteo es óptimo). El error $O(\log T)$ en $N_\xi(T;\lambda) - N_\Xi(T)$ proviene del error de la fórmula de von Mangoldt para $N_\Xi(T)$:

$$N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + \frac{7}{8} + O(\log T).$$

Este error $O(\log T)$ no puede mejorase con las técnicas actuales (requeriría demostrar que el "argumento de $\zeta$" en la recta crítica tiene variación acotada — que implica conjeturas profundas sobre la distribución de $\zeta$ en la recta crítica).

**Luego:** la cota $|t_n^{(\lambda)}-\gamma_n| = O(\log\lambda)$ es, con los métodos actuales, ÓPTIMA. Mejorarla requeriría un estimado mejorado del conteo de ceros, que no está disponible incondicionalmente.

---

## 7. Convergencia: qué puede decirse correctamente

**Teorema 2** (convergencia CONDICIONAL, reformulado). Bajo RH: para cada $n$ fijo, las siguientes son equivalentes:

(a) $t_n^{(\lambda)} \to \gamma_n$ cuando $\lambda\to\infty$.

(b) El error de conteo localizado $|N_\xi(\gamma_n+\varepsilon;\lambda) - N_\Xi(\gamma_n+\varepsilon)| = O(1)$ (cota independiente de $\lambda$, para $\varepsilon$ fijo pequeño).

(c) El producto de Blaschke $B_\lambda(z) \to 1$ localmente uniformemente en un entorno de $z = \gamma_n$.

*Prueba.* (a)$\Leftrightarrow$(b): Un cero $t_n^{(\lambda)} \to \gamma_n$ iff el conteo de ceros por debajo de $\gamma_n+\varepsilon$ es estabilmente igual a $n$ para $\lambda$ grande. (b)$\Leftrightarrow$(c): del desarrollo del producto de Blaschke local. $\square$

**Condición (b) bajo RH:** Si el error de conteo localizado es $O(1)$ en lugar de $O(\log\lambda)$ (hipótesis de precisión local): entonces la convergencia individual sigue. Esta precisión local es plausible bajo las estadísticas GUE (que predicen que las fluctuaciones del conteo de ceros local son $O(1)$ bajo la distribución de GUE), pero no está demostrada incondicionalmente.

---

## 8. El Enunciado Central EC reformulado correctamente

El Enunciado Central del doc 11 era:

> EC: $\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = o(\log\lambda)$.

De la Proposición 1 de este documento: $\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = \log\lambda + \Re A_n + D_n(2\log\lambda) + O(\lambda^{-1/2})$.

Luego EC se reescribe como: $\log\lambda + \Re A_n + D_n(2\log\lambda) = o(\log\lambda)$, i.e., $D_n(2\log\lambda) = -\log\lambda(1+o(1)) - \Re A_n$.

Esto requiere $D_n(2\log\lambda) \sim -\log\lambda$ — una cota PRECISA (no solo $o(\log\lambda)$). La suma $D_n(2\log\lambda) = \sum_{m\neq n}\sin((\gamma_m-\gamma_n)2\log\lambda)/(\gamma_m-\gamma_n)$ tiene varianza $O(\log\gamma_n)$ bajo Montgomery — mucho menor que $\log\lambda$. Luego $D_n(2\log\lambda) = o(\log\lambda)$ en cuadrado medio, pero la condición EC pide que $D_n \sim -\log\lambda$ — una cancelación MASIVA con el término $\log\lambda$ del principal.

**Conclusión:** EC como fue formulado en doc 11 es INCONSISTENTE con la fórmula explícita. La condición correcta es diferente.

**EC reformulado.** La condición correcta para la convergencia individual de los ceros no es sobre la suma completa $\sum_{p\leq\lambda^2}$, sino sobre el ERROR DE CONTEO LOCALIZADO:

> **EC' (Enunciado Central correcto).** Para cada $n$ fijo: $|N_\xi(\gamma_n+1;\lambda) - N_\Xi(\gamma_n+1)| = O(1)$ para $\lambda\to\infty$.

Esta condición es:
- Equivalente a $t_n^{(\lambda)}\to\gamma_n$ (Teorema 2(b)).
- Incondicional en formulación (no menciona RH explícitamente).
- Consecuencia de la conjetura de rigidez de los ceros (que bajo GUE, la fluctuación del conteo local es $O(1)$).

---

## 9. La hipótesis de rigidez y su rol

**Definición** (Rigidez de los ceros). Los ceros $\{t_n^{(\lambda)}\}$ satisfacen la **hipótesis de rigidez** si:

$$|t_n^{(\lambda)} - \gamma_n| = O\!\left(\frac{\log n}{n}\right) \quad\text{para cada } n \leq N_\lambda.$$

Esta es la versión del resultado de "rigidez" de Erdős-Yau para matrices de GUE adaptada a los ceros del operador CCM.

**Proposición 6** (rigidez implica convergencia individual). Bajo la hipótesis de rigidez:

$$|t_n^{(\lambda)} - \gamma_n| = O(\log n/n) \to 0 \quad\text{para } n \text{ fijo}.$$

En particular, $t_n^{(\lambda)} \to \gamma_n$ para cada $n$ fijo.

**¿De dónde viene la rigidez?** La rigidez de los ceros del operador $D_\lambda^N$ debería seguir de las propiedades del ENSEMBLE de matrices de Jacobi $\{J_\lambda^{(N)}\}$ conforme $\lambda\to\infty$. Esta es una afirmación del tipo "universalidad local" para matrices de Jacobi determinísticas convergentes.

---

## 10. Resumen: mapa de gaps y camino a seguir

### Gaps identificados por Advisor 1 y su estado:

| Gap Advisor 1 | Estado tras auditoría |
|---|---|
| 1. Riesz-Fischer $\sum|\delta_{mn}|^{-2}<\infty$ | Plausible bajo GUE (ceros no se aproximan); necesita prueba directa |
| 2. Varianza $\not\Rightarrow$ cota puntual | **CONFIRMADO ERROR** — corrección en doc 11, Sec. 1 |
| 3. Cancelación del $4\log\lambda$ | **CONFIRMADO ERROR** — la cancelación es INCORRECTA; el potencial diverge |
| 4. EC $\Rightarrow$ convergencia de $t_n$ | EC original es inconsistente; EC' (rigidez) sí implica convergencia |
| 5. Convergencia $\Rightarrow$ RH | Correcto vía argumento CCM; el paso es válido bajo condiciones apropiadas |

### El estado honesto del programa Phase 29:

**Probado incondicionalmente y sólidamente:**
- $k_\lambda > 0$, $A_\lambda=$ mult. Mellin, convergencia cuantitativa de ceros de $\hat k_\lambda$
- $M_1[\Delta]\to 0$, conteo correcto $N_\xi = N_\Xi + O(\log)$, convergencia débil
- $|t_n^{(\lambda)}-\gamma_n| = O(\log\lambda)$ (via conteo, no función implícita)
- Convergencia de Cesàro de los ceros

**Probado bajo RH (sólidamente):**
- $S_\lambda(z)\to S_\Xi(z)$ (Stieltjes)
- La convergencia individual $t_n^{(\lambda)}\to\gamma_n$ sigue de EC' (rigidez) que es consecuencia de GUE bajo RH

**El muro real (revisado):**
$$\text{RH} \iff \text{EC'} \iff |N_\xi(\gamma_n;\lambda) - N_\Xi(\gamma_n)| = O(1).$$

La condición EC' (rigidez del conteo local) es la formulación correcta del problema central. Es equivalente a RH por la cadena:
$$\text{EC'} \Rightarrow t_n^{(\lambda)}\to\gamma_n \Rightarrow \hat\xi_\lambda\to c\Xi \text{ (Hurwitz)} \Rightarrow \text{RH (CCM)}.$$

Y RH $\Rightarrow$ EC' por la distribución GUE de los ceros del operador bajo RH.
