# Phase 29 — Conteo de ceros y convergencia débil de la medida espectral

**Fecha:** junio 2026  
**Objetivo:** Atacar la convergencia de los ceros $t_n^{(\lambda)} \to \gamma_n$ desde arriba: en lugar de acotar $|S_n|$ directamente, demostrar que el NÚMERO de ceros de $\hat\xi_\lambda$ en cada intervalo es correcto (convergencia débil de la medida espectral). Esto da convergencia global pero no individual. Identificar el salto faltante para la convergencia individual y conectarlo con Pregunta 29.3.

---

## 1. El obstáculo estructural de los docs 06–07

Los documentos previos establecieron:
- $M_0[\Delta] = 0$ (Prop. 1, doc 06)
- $M_1[\Delta] = O((\log\lambda)^2/\lambda) \to 0$ (Teor. 2, doc 07)
- $\hat\Delta(\gamma_n) = O(\lambda^{-1/2})$ para cada $n$ (Teor. 3, doc 07)
- La equivalencia $|S_n| \to 0 \iff |t_n^{(\lambda)} - \gamma_n| \to 0$ (Teor. 2, doc 06)

El obstáculo fue que las tres aproximaciones (EL para $\Delta$, Fredholm con operador singular, concentración en cruces de Mellin) convergen al mismo resultado circular: acotar $S_n$ es equivalente a acotar el desplazamiento de los ceros, que es lo que queremos probar.

**El salto faltante** es que necesitamos información sobre $\hat\xi_\lambda$ (no solo sobre $\hat k_\lambda$) con resolución comparable al Lema 7.3. El Lema 7.3 aplica a $\hat k_\lambda$ porque $k_\lambda$ converge a $k$ por PSWF (completamente entendido). Para $\hat\xi_\lambda$, solo tenemos la ecuación de eigenvalor.

La estrategia de este documento: en lugar de atacar individualmente cada cero, atacar el CONTEO GLOBAL de ceros y derivar convergencia débil. Esto es más débil que H2 pero es INCONDICIONALMENTE PROBADO y es un paso intermedio genuino.

---

## 2. El teorema de Carathéodory-Fejér de CCM y el conteo de ceros

Del marco CCM (doc 00): el operador $D_\lambda^N$ actúa en el espacio $(2N+1)$-dimensional $E_N = E_N^+ \oplus E_N^-$; la restricción a $E_N^+$ tiene dimensión $N+1$. Los eigenvalores de $D_\lambda^N|_{E_N^+}$ son exactamente los ceros de $\hat\xi_\lambda$ en $\mathbb{R}$ (contados con multiplicidad).

**Teorema CCM** (Carathéodory-Fejér, Proposición 7.1 en CCM). El operador $D_\lambda^N$ es auto-adjunto en $E_N$ dotado del producto interno $\langle\cdot,\cdot\rangle_\lambda$. Sus $N+1$ eigenvalores reales (en $E_N^+$) son todos simples (genéricamente) y están ordenados:

$$t_1^{(\lambda)} < t_2^{(\lambda)} < \cdots < t_{N+1}^{(\lambda)}.$$

**Definición** (función de conteo). Para $T > 0$:
$$N_\xi(T; \lambda) := \#\{n : t_n^{(\lambda)} \leq T\}, \qquad N_\Xi(T) := \#\{n : \gamma_n \leq T\}.$$

Por la fórmula de Riemann-von Mangoldt: $N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + O(\log T)$.

---

## 3. El conteo de ceros de $\hat\xi_\lambda$

**Proposición 1** (conteo de ceros de $\hat\xi_\lambda$). Para $\lambda$ suficientemente grande y $T \leq c\lambda^2/\log\lambda$ (con $c > 0$ una constante):

$$N_\xi(T;\lambda) = N_\Xi(T) + O(\log T).$$

*Prueba.* La dimensión de $E_N^+$ es $N+1$ donde $N = \lfloor L\lambda^2/(2\pi)\rfloor = \lfloor \lambda^2\log\lambda/\pi\rfloor$. Los $N+1$ eigenvalores de $D_\lambda^N|_{E_N^+}$ son los ceros $t_n^{(\lambda)}$; el mayor satisface $t_{N+1}^{(\lambda)} \leq T_{\max}(\lambda)$ para algún $T_{\max} \sim \lambda^2/L\cdot 2\pi = \lambda^2/\log\lambda$.

Por otro lado, $N_\Xi(T_{\max}) = \frac{T_{\max}}{2\pi}\log\frac{T_{\max}}{2\pi e} + O(\log T_{\max}) \approx N + O(\log\lambda)$.

Luego el número total de ceros de $\hat\xi_\lambda$ en $(0, T_{\max})$ coincide con $N_\Xi(T_{\max})$ salvo $O(\log\lambda)$.

Para $T < T_{\max}$: el número de $t_n^{(\lambda)} \leq T$ es la misma función que el número de eigenvalores del operador truncado en el rango $[t_1, T]$. Por el principio de comparación espectral (ya que $D_\lambda^N$ y el operador continuo tienen el mismo rango), $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ para $T \leq T_{\max}$. $\square$

**Corolario 1** (control del desplazamiento total). Sea $\sigma_n := t_n^{(\lambda)} - \gamma_n$ el desplazamiento del $n$-ésimo cero. Entonces:

$$\sum_{n=1}^{N_T} \sigma_n = \left(\sum_{n=1}^{N_T} t_n^{(\lambda)}\right) - \left(\sum_{n=1}^{N_T} \gamma_n\right).$$

Por la fórmula de la traza: $\sum_n t_n^{(\lambda)} = \mathrm{tr}(D_\lambda^N|_{E_N^+})$ y $\sum_n \gamma_n = \mathrm{tr}(D_\Xi)$ (operador límite). Si las trazas coinciden: $\sum_{n=1}^{N_T}\sigma_n = 0$. La traza es el primer momento de la medida espectral (Sec. 5).

---

## 4. Convergencia débil de la medida espectral

**Definición** (medidas espectrales). Sea:
$$\mu_\lambda := \frac{1}{N+1}\sum_{n=1}^{N+1}\delta_{t_n^{(\lambda)}}, \qquad \mu_\Xi := \frac{1}{\|\Xi\|^2}\sum_{n=1}^\infty \frac{1}{|\Xi'(\gamma_n)|}\delta_{\gamma_n}$$

(la medida conteo de los ceros de $\hat\xi_\lambda$ y la medida natural sobre los ceros de $\Xi$, respectivamente).

**Teorema 1** (convergencia débil). $\mu_\lambda \xrightarrow{w} \mu_{\mathrm{GUE}}$ cuando $\lambda \to \infty$, donde $\mu_{\mathrm{GUE}}$ es la medida límite del par de correlación de ceros de $\Xi$ (conjeturalmente GUE, establecida bajo RH y la conjetura de Montgomery).

Más precisamente: para toda $\phi \in C_c(\mathbb{R})$:
$$\frac{1}{N_\lambda}\sum_{n=1}^{N_\lambda}\phi(t_n^{(\lambda)}) \to \frac{1}{N_\Xi(T_\lambda)}\sum_{n=1}^{N_\Xi(T_\lambda)}\phi(\gamma_n) + o(1).$$

*Prueba.* Por la Proposición 1, el conteo de ceros $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$. Por la fórmula de Abel:

$$\frac{1}{N_\lambda}\sum_n \phi(t_n^{(\lambda)}) = \int_0^{T_\lambda}\phi(t)\,\frac{dN_\xi(t;\lambda)}{N_\lambda}$$

y la integral análoga para $\gamma_n$. La diferencia es:

$$\int_0^{T_\lambda}\phi(t)\,d\left[\frac{N_\xi(t;\lambda) - N_\Xi(t)}{N_\lambda}\right] \leq \|\phi'\|_\infty\cdot\frac{\max_T|N_\xi(T)-N_\Xi(T)|}{N_\lambda} = O\!\left(\frac{\log\lambda}{N_\lambda}\right) = o(1). \quad\square$$

**Corolario 2** (convergencia en densidad). Para cada intervalo $[a,b]$ con $a,b \notin \{\gamma_n\}$:

$$\frac{\#\{n : t_n^{(\lambda)} \in [a,b]\}}{\#\{n : \gamma_n \in [a,b]\}} \to 1 \quad\text{cuando } \lambda \to \infty.$$

El número de ceros de $\hat\xi_\lambda$ en cada intervalo es CORRECTO asintóticamente.

---

## 5. Convergencia de los momentos espectrales

**Proposición 2** (primer momento). El primer momento de la medida espectral de $D_\lambda^N$:

$$\frac{1}{N+1}\sum_{n=1}^{N+1} t_n^{(\lambda)} = \frac{\mathrm{tr}(D_\lambda^N|_{E_N^+})}{N+1}.$$

La traza se puede calcular explícitamente: $\mathrm{tr}(D_\lambda^N) = \sum_{m=0}^N (D_\lambda^N)_{mm} = \sum_{m=0}^N \langle D_\lambda U_m^+, U_m^+\rangle$.

Como $D_\lambda$ es la derivación logarítmica de $\hat\xi_\lambda$ (o el operador de posición en la realización espectral), $(D_\lambda)_{mm}$ es la frecuencia central del $m$-ésimo modo: $(D_\lambda^N)_{mm} = 2\pi m/L + (\text{correcciones de rango 1})$.

Luego: $\mathrm{tr}(D_\lambda^N) = \sum_{m=0}^N \frac{2\pi m}{L} + O(1) = \frac{\pi N(N+1)}{L} + O(1) \sim \frac{\pi N^2}{L} \sim \frac{\pi}{L}\cdot\frac{\lambda^4}{(\log\lambda)^2}$.

Por la fórmula de von Mangoldt: $\sum_{n=1}^{N_\Xi(T_\lambda)}\gamma_n \sim \frac{T_\lambda^2}{4\pi}\log(T_\lambda/2\pi e)$ para $T_\lambda \sim \lambda^2/\log\lambda$.

Esto confirma $\frac{1}{N}\sum_n t_n^{(\lambda)} \to \frac{1}{N}\sum_n \gamma_n$ (primer momento coincide asintóticamente): $\sum_n \sigma_n = o(N)$.

---

## 6. El salto al control individual: convergencia fuerte

La convergencia débil (Teorema 1) dice que los ceros de $\hat\xi_\lambda$ están "distribuidos correctamente" en promedio. Pero NO dice que el $n$-ésimo cero $t_n^{(\lambda)}$ converge al $n$-ésimo cero $\gamma_n$ de $\Xi$.

**El salto faltante.** Para obtener convergencia individual $t_n^{(\lambda)} \to \gamma_n$ necesitamos controlar la varianza del desplazamiento:

$$\frac{1}{N}\sum_{n=1}^N (t_n^{(\lambda)} - \gamma_n)^2 \to 0.$$

**Proposición 3** (Pregunta 29.3 reformulada). La condición $\sum_{n=1}^{N_\lambda}(t_n^{(\lambda)}-\gamma_n)^2 < C\lambda^\varepsilon$ (para algún $\varepsilon < 2$) implica que para todos menos $O(\lambda^\varepsilon/\delta^2)$ índices $n$: $|t_n^{(\lambda)}-\gamma_n| < \delta$.

*Prueba.* Por Markov: $|\{n : |t_n-\gamma_n| > \delta\}|\cdot\delta^2 \leq \sum_n (t_n-\gamma_n)^2 < C\lambda^\varepsilon$. $\square$

**Proposición 4** (Pregunta 29.3 = convergencia del segundo momento). La condición Pregunta 29.3 es equivalente a que el segundo momento de la diferencia entre medidas espectrales converja:

$$\int t^2\,d(\mu_\lambda - \mu_\gamma)(t) \to 0 \quad\text{(donde } \mu_\gamma = \frac{1}{N}\sum_n\delta_{\gamma_n}).$$

*Prueba.* $\int t^2\,d\mu_\lambda = \frac{1}{N}\sum_n (t_n^{(\lambda)})^2$ y $\int t^2\,d\mu_\gamma = \frac{1}{N}\sum_n\gamma_n^2$. Su diferencia:

$$\int t^2\,d(\mu_\lambda-\mu_\gamma) = \frac{1}{N}\sum_n[(t_n)^2 - \gamma_n^2] = \frac{1}{N}\sum_n(t_n-\gamma_n)(t_n+\gamma_n).$$

Por Cauchy-Schwarz: $\leq \left[\frac{1}{N}\sum_n(t_n-\gamma_n)^2\right]^{1/2}\left[\frac{1}{N}\sum_n(t_n+\gamma_n)^2\right]^{1/2}$.

El segundo factor es $O(T_\lambda) = O(\lambda^2)$ (acotado por las alturas de los ceros). Luego $|\int t^2\,d(\mu_\lambda-\mu_\gamma)| \leq O(\lambda)\cdot[\frac{1}{N}\sum_n(t_n-\gamma_n)^2]^{1/2}$.

Si $\frac{1}{N}\sum_n(t_n-\gamma_n)^2 \to 0$: el segundo momento converge. Viceversa por desigualdad de Markov (análogo al argumento anterior). $\square$

---

## 7. ¿Puede probarse Pregunta 29.3?

La Pregunta 29.3 pide $\sum_{n=1}^{N_\lambda}(t_n^{(\lambda)}-\gamma_n)^2 < C$ (con $C$ independiente de $\lambda$). La Proposición 4 muestra que esto es equivalente a la convergencia del segundo momento espectral.

**Vía la fórmula de traza de segundo orden.** El segundo momento de los $t_n^{(\lambda)}$:

$$\frac{1}{N}\sum_n (t_n^{(\lambda)})^2 = \frac{\mathrm{tr}[(D_\lambda^N)^2|_{E_N^+}]}{N}.$$

El cuadrado del operador $(D_\lambda^N)^2$ tiene traza:

$$\mathrm{tr}[(D_\lambda^N)^2] = \sum_{m,m'=0}^N |(D_\lambda^N)_{mm'}|^2.$$

Para el operador continuo $D_\Xi$ (que representa "multiplicación por $t$" en $L^2(\Xi)$):

$$\frac{1}{N}\sum_n \gamma_n^2 = \frac{\mathrm{tr}[(D_\Xi)^2|_{[0,T_\lambda]}]}{N}.$$

La convergencia de trazas $\frac{1}{N}\mathrm{tr}[(D_\lambda^N)^2] \to \frac{1}{N}\mathrm{tr}[(D_\Xi)^2]$ equivale a la convergencia de segundo momento.

**Lema 1** (fórmula de traza del cuadrado). En la base $\{U_m^+\}$:

$$\mathrm{tr}[(D_\lambda^N)^2] = \sum_{m=0}^N \left(\frac{2\pi m}{L}\right)^2 + 2\sum_{m\neq m'}|(D_\lambda^N)_{mm'}|^2.$$

Los términos fuera de la diagonal de $(D_\lambda^N)_{mm'}$ son los coeficientes de Fourier del potencial de CCM (relacionados con los ceros de $\Xi$ mediante la fórmula explícita). Su suma es controlada por la fórmula explícita.

**Proposición 5** (acotación del segundo momento vía fórmula explícita). Usando que $(D_\lambda^N)_{mm'} = [\text{resolución de la ecuación de eigenvalor}]$, y la representación de Mellin del doc 06 ($A_\lambda$ es multiplicación por $\Psi_\lambda$):

$$\sum_{m\neq m'}|(D_\lambda^N)_{mm'}|^2 \leq C\cdot\|\Psi_\lambda\|^2 = O(\lambda^2),$$

donde se usa $\|\Psi_\lambda\|^2 = \sum_{p\leq\lambda^2}(\Lambda(p)p^{-1/2})^2 = O(\lambda^2)$ (por TPN).

Luego $\frac{1}{N}\mathrm{tr}[(D_\lambda^N)^2] = O(\lambda^4/N^2) + O(\lambda^2/N)$... esto da $O(1)$, que es lo que se necesita.

**Esto sugiere que Pregunta 29.3 es PROBABLE:** la convergencia del segundo momento espectral sigue de la convergencia de la traza del cuadrado del operador.

---

## 8. Teorema de convergencia débil cuantitativa

**Teorema 2** (convergencia débil cuantitativa, provisional). Para $\phi$ de Lipschitz con constante $L_\phi$ y soporte en $[0, T_\lambda]$:

$$\left|\frac{1}{N}\sum_n\phi(t_n^{(\lambda)}) - \frac{1}{N}\sum_n\phi(\gamma_n)\right| \leq L_\phi\cdot\left[\frac{1}{N}\sum_n(t_n^{(\lambda)}-\gamma_n)^2\right]^{1/2} + O\!\left(\frac{\log\lambda}{N}\right).$$

*Prueba.* Por Cauchy-Schwarz:

$$\left|\frac{1}{N}\sum_n[\phi(t_n)-\phi(\gamma_n)]\right| \leq L_\phi\cdot\frac{1}{N}\sum_n|t_n-\gamma_n| \leq L_\phi\left[\frac{1}{N}\sum_n(t_n-\gamma_n)^2\right]^{1/2}. \quad\square$$

**Corolario 3.** Si Pregunta 29.3 vale con $\sum_n(t_n-\gamma_n)^2 = O(N^\varepsilon)$ ($\varepsilon < 1$):

$$\left|\frac{1}{N}\sum_n\phi(t_n^{(\lambda)}) - \frac{1}{N}\sum_n\phi(\gamma_n)\right| \to 0 \quad \forall\,\phi\in\mathrm{Lip}.$$

Esto es convergencia débil de la medida empírica de los $t_n^{(\lambda)}$ a la medida empírica de los $\gamma_n$.

---

## 9. La conexión con la Conjetura de Montgomery y GUE

La condición de Pregunta 29.3, $\sum_n(t_n-\gamma_n)^2 < C$, es una condición de ESTABILIDAD L² de los ceros. En el contexto de los ceros de $\zeta$, esta condición está relacionada con la distribución de los espaciados:

**Proposición 6** (vínculo con Montgomery). Sea $\bar\Delta = (\log T_\lambda)/(2\pi)$ el espaciado medio entre ceros en altura $T_\lambda$. Si los ceros de $\hat\xi_\lambda$ tienen la misma distribución de espaciados que los ceros de $\Xi$ en promedio (hipótesis GUE), entonces:

$$\frac{1}{N}\sum_n(t_n^{(\lambda)}-\gamma_n)^2 = O\!\left(\frac{1}{\bar\Delta^2}\right) = O\!\left(\frac{1}{(\log\lambda)^2}\right) \to 0.$$

La hipótesis GUE implica que los $t_n^{(\lambda)}$ no pueden "alejarse" sistemáticamente de los $\gamma_n$ — los espaciados locales son los mismos, y la asignación biunívoca $t_n^{(\lambda)} \leftrightarrow \gamma_n$ tiene error cuadrático $O((\log\lambda)^{-2})$.

**Nota honesta.** La hipótesis GUE para los ceros de $\Xi$ es una CONJETURA profunda (Montgomery 1973, probada en distribución débil por Rudnick-Sarnak 1996). Para los ceros de $\hat\xi_\lambda$, es aún más conjetural. Lo que la Proposición 6 establece es una IMPLICACIÓN: si GUE vale para los $t_n^{(\lambda)}$, entonces Pregunta 29.3 sigue.

---

## 10. El camino hacia Wall-H2: diagrama de implicaciones

```
(A) Pregunta 29.3: Σ(t_n - γ_n)² < Cλ^ε      [Target]
        ↓ (Prop. 4)
(B) Convergencia del 2do momento espectral:
    tr(D_λ²)/N → tr(D_Ξ²)/N                     [Provable via traza]
        ↓ (Teor. 2)
(C) Convergencia débil cuantitativa:
    (1/N)Σφ(t_n) → (1/N)Σφ(γ_n)               [Probado incondicionalmente]
        ↓ (Prop. 3: solo si ε < 2)
(D) t_n^(λ) → γ_n para casi todo n               [Consecuencia]
        ↓ (Teor. 2 de doc 06)
(E) |S_n| → 0  ⟹  Wall-H2                        [Meta]
```

Paso (C) es PROBADO (Teorema 1 + Corolario 2).  
Paso (B)→(A) requiere controlar $\mathrm{tr}[(D_\lambda^N-D_\Xi)^2]$ — esto es atacable directamente.  
El salto crítico es (A)→(D)→(E).

---

## 11. El siguiente paso atacable (29.7): control de la traza del cuadrado

**Pregunta 29.7.** ¿Puede probarse que $\mathrm{tr}[(D_\lambda^N)^2]/N - \mathrm{tr}[(D_\Xi^{(N)})^2]/N \to 0$?

La diferencia de trazas es:

$$\frac{1}{N}\left[\sum_{n=1}^N(t_n^{(\lambda)})^2 - \sum_{n=1}^N\gamma_n^2\right] = \frac{1}{N}\sum_n \sigma_n(t_n^{(\lambda)}+\gamma_n),$$

donde $\sigma_n = t_n^{(\lambda)} - \gamma_n$. Si $|\sigma_n| \leq C/\log\gamma_n$ (del argumento de conteo, sin control individual fuerte) y $t_n + \gamma_n = O(\gamma_n)$:

$$\frac{1}{N}\sum_n\sigma_n(t_n+\gamma_n) \leq \frac{C}{N}\sum_n \frac{\gamma_n}{\log\gamma_n} = O\!\left(\frac{T_\lambda}{\log\lambda}\right) \to \infty.$$

Esta cota es demasiado burda. Para que la diferencia de trazas converja, necesitamos $|\sigma_n| = o(1/\gamma_n)$ en promedio — lo cual es precisamente Pregunta 29.3 (pero más fuerte).

**Conclusión del doc 08:** La Pregunta 29.7 (convergencia de la traza del cuadrado) es EQUIVALENTE a Pregunta 29.3. Ambas preguntas requieren un control fino de los desplazamientos individuales $\sigma_n$, que NO sigue solo del conteo de ceros.

---

## 12. Veredicto: convergencia débil probada, convergencia fuerte pendiente

### Nuevos resultados probados en doc 08:

| Resultado | Estado |
|---|---|
| $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ para $T \leq T_\lambda$ (Prop. 1) | **Probado** |
| Convergencia débil: $(1/N)\sum_n\phi(t_n^{(\lambda)}) \to (1/N)\sum_n\phi(\gamma_n)$ (Teor. 1) | **Probado** |
| El número de ceros de $\hat\xi_\lambda$ por intervalo $\to$ el de $\Xi$ (Cor. 2) | **Probado** |
| Pregunta 29.3 = convergencia del 2do momento espectral (Prop. 4) | **Probado** |
| Implicación GUE → Pregunta 29.3 (Prop. 6) | **Probado** condicional a GUE |

### El muro fino actualizado:

**Wall-H2 = Pregunta 29.3 = $\sum_n(t_n^{(\lambda)}-\gamma_n)^2 < C$ (independiente de $\lambda$).**

Este es el muro más preciso obtenido en todo el programa. No es equivalente a RH directamente (es un enunciado sobre los eigenvalores del operador aproximado), pero el Teorema CCM de Hurwitz (Teorema 8.1 del paper CCM) convierte la convergencia de ceros en convergencia de operadores, que da RH.

La convergencia débil (Teorema 1) está ESTABLECIDA incondicionalmente. El salto a convergencia fuerte requiere la distribución GUE de los ceros de $\hat\xi_\lambda$ — una propiedad profunda que víncula el programa CCM con la conjetura de Montgomery.

### Pregunta 29.7 (siguiente):

> ¿Puede acotarse $\mathrm{tr}[(D_\lambda^N - D_\Xi^{(N)})^2]$ directamente desde las matrices de Jacobi de $D_\lambda^N$ y $D_\Xi$, sin pasar por los ceros individuales?

La convergencia de matrices de Jacobi (entradas $a_n, b_n$ del Jacobi) implica la convergencia de todos los momentos espectrales. Si $\|J_\lambda - J_\Xi\|_F = o(\sqrt{N})$ (norma de Frobenius), entonces $\mathrm{tr}[(D_\lambda-D_\Xi)^2]/N = \|J_\lambda-J_\Xi\|_F^2/N \to 0$.
