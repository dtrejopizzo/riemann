# Documento 73 — Intento de prueba: tres ataques a $T_\lambda = 0$ y el obstáculo fundamental

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 64, 70, 71, 72

---

## 1. El problema en su forma más limpia

Tenemos (Doc 64, Thm. 3.1):

$$\text{RH} \iff T_\lambda = 0 \;\text{ para todo } \lambda > 0,$$

con

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\bigl(|\zeta(\tfrac{1}{2}+is)|^2 - |\zeta_{on}(\tfrac{1}{2}+is)|^2\bigr)\,dm_\infty(s).$$

Para probar RH es suficiente probar $T_\lambda = 0$ para todo $\lambda$.

Tenemos: $W_\lambda \geq 0$ (Doc 63), $|\zeta|^2 - |\zeta_{on}|^2 \geq 0$ puntualmente bajo $\neg$RH (del producto de Hadamard, ver §2 abajo), y $T_\lambda > 0$ bajo $\neg$RH. Para probar RH necesitamos un argumento que establezca $T_\lambda \leq 0$, o que establezca $|\zeta|^2 = |\zeta_{on}|^2$, o cualquier otra vía que fuerce $T_\lambda = 0$.

Presentamos tres ataques.

---

## 2. Verificación: $|\zeta(1/2+is)|^2 \geq |\zeta_{on}(1/2+is)|^2$ puntualmente

Antes de atacar, establecemos la desigualdad puntual que hace al problema difícil.

Bajo $\neg$RH existe al menos un cero $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 > 1/2$. Por la ecuación funcional, los ceros off-critical vienen en cuádruplos $\{\sigma_0 \pm i\gamma_0,\, (1-\sigma_0) \pm i\gamma_0\}$. La construcción de $\zeta_{on}$ reemplaza este cuádruplo por el par crítico $\{1/2 \pm i\gamma_0\}$ (doble multiplicidad o par simple, dependiendo de la convención).

La contribución del cuádruplo off-critical al cociente de Hadamard:

$$\frac{|\zeta(1/2+is)|^2}{|\zeta_{on}(1/2+is)|^2}\bigg|_{\text{cuádruplo}} = \frac{|(1/2-\sigma_0)^2 + (s-\gamma_0)^2|}{(s-\gamma_0)^2} \cdot \frac{|(1/2-\sigma_0)^2 + (s+\gamma_0)^2|}{(s+\gamma_0)^2} \geq 1$$

para $s \notin \{-\gamma_0, \gamma_0\}$, con igualdad solo cuando $\sigma_0 = 1/2$ (RH).

**Conclusión:** $|\zeta(1/2+is)|^2 \geq |\zeta_{on}(1/2+is)|^2$ puntualmente, con igualdad a.e. sii RH.

Esto confirma que el integrando de $T_\lambda$ es no-negativo. Para probar $T_\lambda = 0$ necesitamos un argumento que vaya *contra* este integrando — una cota superior que lo cancele.

---

## 3. Ataque 1: la fórmula de Weil como restricción sobre $\int W_\lambda |\zeta|^2 dm_\infty$

### 3.1. Lo que la fórmula de Weil dice

La fórmula explícita de Weil (aplicada al logaritmo de $\zeta$, no a $|\zeta|^2$) establece: para cualquier función de prueba $h$ analítica y con decaimiento apropiado,

$$\sum_n h(\gamma_n) = -\sum_p \sum_{m \geq 1} \frac{\log p}{p^{m/2}} \hat{h}(m\log p) + C[h],$$

donde la suma izquierda es sobre las partes imaginarias $\gamma_n$ de todos los ceros de $\zeta$ y $C[h]$ son los términos archimedianos (gamma y polo). El lado derecho depende solo de la función de prueba $h$ y de los primos — no de la posición exacta de los ceros.

### 3.2. La conexión con $T_\lambda$

La integral $T_\lambda = \int W_\lambda (|\zeta|^2 - |\zeta_{on}|^2) dm_\infty$ involucra $|\zeta|^2$, no los ceros directamente. La relación entre $|\zeta(1/2+is)|^2$ y los ceros es:

$$\log|\zeta(1/2+is)|^2 = 2\sum_n \log\left|1 - \frac{s}{\gamma_n}\right| + \text{suave}.$$

(La suma es sobre las partes imaginarias de los ceros, con convergencia absoluta tras el factor de convergencia de Weierstrass.)

La fórmula de Weil habla de $\frac{d}{ds}\log|\zeta|$ (la derivada logarítmica), no de $\log|\zeta|$ mismo.

### 3.3. El obstáculo: log vs. cuadrado

La relación entre lo que da la fórmula de Weil ($\frac{d}{ds}\log|\zeta|$, o equivalentemente $-\text{Re}\frac{\zeta'}{\zeta}(1/2+is)$) y lo que necesitamos para $T_\lambda$ ($|\zeta(1/2+is)|^2$) requiere:

$$|\zeta(1/2+is)|^2 = \exp\!\left(2\int_{-\infty}^s \left(-\text{Im}\frac{\zeta'}{\zeta}(1/2+it)\right) dt\right) \cdot |\zeta(1/2-i\infty)|^2.$$

La cota $|\zeta(1/2 - i\infty)|^2$ es el "valor en el infinito" — y la función $\zeta$ no se puede evaluar en $-i\infty$ directamente. Esta integración introduce una constante de integración que depende de los ceros globalmente.

**Resultado del Ataque 1:** La fórmula de Weil no da directamente información sobre $T_\lambda$. Relaciona $\frac{d}{ds}\log|\zeta|$ con primos, pero la conexión con $|\zeta|^2$ requiere integración con condiciones de frontera que son exactamente equivalentes a RH.

---

## 4. Ataque 2: la desigualdad de Jensen y la convexidad logarítmica

### 4.1. Jensen aplicado a $W_\lambda dm_\infty$

La función $W_\lambda dm_\infty$ es una medida positiva finita (no de probabilidad, pero podemos normalizar). Sea $\mu_\lambda = W_\lambda dm_\infty / \|W_\lambda\|_{L^1(dm_\infty)}$.

La desigualdad de Jensen para la función convexa $e^x$:

$$\int e^{2u} d\mu_\lambda \geq \exp\!\left(2\int u\, d\mu_\lambda\right),$$

con $u = \log|\zeta(1/2+is)|$ y $u_{on} = \log|\zeta_{on}(1/2+is)|$.

Da: $\int W_\lambda |\zeta|^2 dm_\infty \geq \exp(2\int W_\lambda \log|\zeta| dm_\infty / \|W_\lambda\|_1) \cdot \|W_\lambda\|_1$.

### 4.2. La cota que necesitaríamos

Para probar $T_\lambda = \int W_\lambda(|\zeta|^2 - |\zeta_{on}|^2) dm_\infty \leq 0$ necesitaríamos una cota superior:

$$\int W_\lambda |\zeta|^2 dm_\infty \leq \int W_\lambda |\zeta_{on}|^2 dm_\infty.$$

Jensen solo da cotas inferiores (no superiores) para $\int e^{2u}$. Para obtener una cota superior necesitaríamos la desigualdad opuesta — que $e^x$ sea cóncava, lo cual es falso.

**Resultado del Ataque 2:** La convexidad de $e^x$ trabaja en la dirección equivocada. Jensen da cotas inferiores para $\int |\zeta|^2 dm_\infty$, no superiores. Este ataque no solo falla — falla en la dirección opuesta a lo que necesitamos.

---

## 5. Ataque 3: usando la ecuación funcional de $\zeta$

### 5.1. La ecuación funcional sobre la recta crítica

La ecuación funcional $\xi(s) = \xi(1-s)$ implica $\Xi(-t) = \Xi(t)$ (paridad). Sobre la recta crítica $s = 1/2 + it$:

$$|\zeta(1/2+it)|^2 = |\chi(1/2+it)|^{-1} \cdot |\zeta(1/2+it)|^2,$$

donde $|\chi(1/2+it)| = 1$. Esto es una tautología — la ecuación funcional no da información nueva sobre el módulo sobre la recta crítica.

### 5.2. La restricción de Bohr-Landau-von Mangoldt

La media cuadrada de $|\zeta(1/2+is)|$ sobre intervalos $[T, 2T]$ se conoce:

$$\frac{1}{T}\int_T^{2T} |\zeta(1/2+it)|^2 dt \sim \log T.$$

Y para $|\zeta_{on}|$: la misma fórmula se cumple porque $\zeta_{on}$ tiene la misma distribución de ceros en promedio (mismo índice asintótico $N(T) \sim \frac{T}{2\pi}\log T$).

Entonces:
$$\frac{1}{T}\int_T^{2T} W_\lambda(t)(|\zeta|^2 - |\zeta_{on}|^2) dt \to 0 \quad (T \to \infty)?$$

No necesariamente: $W_\lambda$ está fijo y la integral es sobre $t$ grande, no sobre la región relevante.

### 5.3. La restricción de Lindelöf

La hipótesis de Lindelöf (consecuencia de RH, pero no equivalente a él) diría $|\zeta(1/2+it)| = O(t^\varepsilon)$. Esto daría una cota sobre $T_\lambda$ para $\lambda$ grande, pero no que $T_\lambda = 0$.

**Resultado del Ataque 3:** La ecuación funcional y las medias cuadradas no dan $T_\lambda = 0$ sin hipótesis adicionales equivalentes a RH.

---

## 6. El obstáculo fundamental: nombrado con precisión

Los tres ataques fallan en el mismo punto. El obstáculo se puede enunciar con precisión:

**Proposición 6.1** (El obstáculo).

Las siguientes son equivalentes:

1. $T_\lambda = 0$ para todo $\lambda > 0$.
2. $\int W_\lambda(s)(|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2) dm_\infty(s) = 0$ para todo $\lambda$.
3. $|\zeta(1/2+is)|^2 = |\zeta_{on}(1/2+is)|^2$ para $dm_\infty$-casi todo $s$.
4. RH.

*Demostración.* (1)$\iff$(2): por definición. (2)$\iff$(3): porque $\{W_\lambda\}_{\lambda>0}$ es una familia separante en $L^1(dm_\infty)$ (al tomar $\lambda \to \infty$, $W_\lambda$ converge a $\sum_{n=0}^\infty n|P_n|^2$, que es densa por completitud de $\{P_n\}$). (3)$\iff$(4): por el argumento Hadamard de Doc 64. $\square$

**El obstáculo es exactamente que (3) es RH.** No hay ninguna información adicional en el formalismo CCM que distinga $|\zeta|^2$ de $|\zeta_{on}|^2$ sin ya saber que son iguales.

---

## 7. Una nueva observación: la restricción del producto de Euler

### 7.1. Lo que es nuevo

Hay un hecho que los Docs 70-72 no usaron completamente: la función $\zeta$ tiene un producto de Euler $\zeta(s) = \prod_p (1-p^{-s})^{-1}$, y $\zeta_{on}$ NO tiene este producto de Euler.

Esto es una restricción fundamental: $dm_{full} = dm_\infty \cdot |\zeta(1/2+is)|^2$ está dada por UNA FUNCIÓN ESPECÍFICA — la función zeta de Riemann — que satisface el producto de Euler. La función $dm_{full,on} = dm_\infty \cdot |\zeta_{on}(1/2+is)|^2$ está dada por una función arbitraria construida solo por su distribución de ceros.

### 7.2. La reformulación del problema

La pregunta $T_\lambda = 0$ equivale a: ¿el módulo $|\zeta(1/2+is)|$ sobre la recta crítica es el mismo que el módulo de la función $\zeta_{on}$ construida por sus ceros críticos?

La respuesta sería positiva si: la distribución de ceros de $\zeta$ sobre la recta crítica *determina completamente* el módulo $|\zeta(1/2+is)|$, con el producto de Euler imponiendo que no puede haber ningún "exceso" de módulo.

**Conjetura 7.1** (El complemento de RH).

El módulo $|\zeta(1/2+is)|^2$ sobre la recta crítica es el *mínimo* posible entre todas las funciones enteras con el mismo producto de Euler y la misma distribución de ceros reales (ceros con $\beta = 1/2$), sujeto a la ecuación funcional.

Si la Conj. 7.1 es cierta, entonces $|\zeta|^2 \leq |\zeta_{on}|^2$ puntualmente, lo que combinado con $|\zeta|^2 \geq |\zeta_{on}|^2$ (§2) da $|\zeta|^2 = |\zeta_{on}|^2$, es decir, RH.

### 7.3. Análisis de la Conjetura 7.1

La Conj. 7.1 dice que el producto de Euler *fuerza* que no haya ceros off-critical. Esto es precisamente la fuerza del producto de Euler — las singularidades de $\log\zeta$ en el semiplano $\text{Re}(s) > 1$ están completamente determinadas por los primos, y la extensión analítica a $\text{Re}(s) = 1/2$ debería ser "minimal" en algún sentido.

Para formalizar: si $\zeta$ tuviera un cero off-critical $\sigma_0 + i\gamma_0$ con $\sigma_0 > 1/2$, el cociente $|\zeta(1/2+is)|^2 / |\zeta_{on}(1/2+is)|^2 > 1$ en la mayor parte de la recta crítica (§2). Esto significaría que $\int |\zeta|^2 dm_\infty > \int |\zeta_{on}|^2 dm_\infty$.

Pero el producto de Euler da:

$$\int_{\mathbb{R}} |\zeta(1/2+is)|^2 dm_\infty(s) = \sum_{n=1}^\infty \frac{d(n)^2}{n} \cdot \hat{w}(\log n),$$

donde $d(n)$ es el número de divisores de $n$ y $\hat{w}$ es la transformada de Fourier de la densidad $w = dm_\infty/ds$. Este es un número fijo, completamente determinado por los primos — independiente de si RH es verdad o no.

Y para $\zeta_{on}$:

$$\int_{\mathbb{R}} |\zeta_{on}(1/2+is)|^2 dm_\infty(s) = ?$$

Aquí está el problema: $\zeta_{on}$ NO tiene un producto de Euler, así que no podemos calcular $\int |\zeta_{on}|^2 dm_\infty$ de la misma manera.

---

## 8. El verdadero núcleo del problema

**Proposición 8.1** (El corazón del obstáculo).

Las siguientes son equivalentes:

1. RH.
2. $\int |\zeta_{on}(1/2+is)|^2 dm_\infty(s) = \int |\zeta(1/2+is)|^2 dm_\infty(s) = \sum_n d(n)^2 \hat{w}(\log n)/n$.
3. La función $\zeta_{on}$ satisface la misma fórmula de media cuadrática sobre $dm_\infty$ que la función zeta.

*Demostración.* (1)$\Rightarrow$(2): bajo RH, $|\zeta| = |\zeta_{on}|$ sobre la recta crítica, luego las integrales son iguales, y la de $|\zeta|^2$ se calcula por el producto de Euler. (2)$\Rightarrow$(1): si las medias cuadradas son iguales y $|\zeta| \geq |\zeta_{on}|$ puntualmente (§2), entonces $|\zeta| = |\zeta_{on}|$ a.e., que es RH. $\square$

**Observación 8.2.** La igualdad del número $\sum_n d(n)^2 \hat{w}(\log n)/n$ con $\int |\zeta_{on}|^2 dm_\infty$ requiere que $\zeta_{on}$, aunque no tiene producto de Euler, tenga la misma norma en $L^2(dm_\infty)$ que la función $\zeta$. Esto es equivalente a RH — una tautología.

---

## 9. ¿Existe algún ángulo nuevo?

### 9.1. El producto de Euler como restricción sobre la función de prueba

Una idea genuinamente nueva: en lugar de tratar $|\zeta|^2$ como una función arbitraria, usar explícitamente que $|\zeta(1/2+is)|^2 = \prod_p |1-p^{-1/2-is}|^{-2}$.

La integral:

$$\int W_\lambda(s) |\zeta(1/2+is)|^2 dm_\infty(s) = \int W_\lambda(s) \prod_p |1-p^{-1/2-is}|^{-2} dm_\infty(s).$$

Expandiendo el producto (formalmente):

$$= \int W_\lambda(s) \sum_{n \geq 1} d(n) n^{-1/2-is} \sum_{m \geq 1} d(m) m^{-1/2+is} dm_\infty(s)$$
$$= \sum_{n,m \geq 1} \frac{d(n)d(m)}{\sqrt{nm}} \int W_\lambda(s) (n/m)^{is} dm_\infty(s).$$

El integral interno es la transformada de Fourier de $W_\lambda dm_\infty$ evaluada en $\log(m/n)$:

$$\int W_\lambda(s) (n/m)^{is} dm_\infty(s) = \widehat{W_\lambda dm_\infty}(\log(n/m)).$$

Por tanto:

$$\int W_\lambda |\zeta|^2 dm_\infty = \sum_{n,m \geq 1} \frac{d(n)d(m)}{\sqrt{nm}} \widehat{W_\lambda dm_\infty}(\log(n/m)).$$

Esta es la *representación aritmética exacta* de $\int W_\lambda |\zeta|^2 dm_\infty$ en términos del producto de Euler.

### 9.2. La transformada de Fourier de $W_\lambda dm_\infty$

De la forma Abel de $W_\lambda$:

$$W_\lambda(s) = \sum_{k=1}^{N(\lambda)} k\, |P_k(s)|^2 + (a_{N(\lambda)}^\infty)^2 |P_{N(\lambda)+1}|^2,$$

su transformada de Fourier respecto a $dm_\infty$:

$$\widehat{W_\lambda dm_\infty}(r) = \sum_{k=1}^{N(\lambda)} k \underbrace{\int |P_k(s)|^2 e^{irs} dm_\infty(s)}_{\phi_k(r)} + (a_{N(\lambda)}^\infty)^2 \phi_{N(\lambda)+1}(r),$$

donde $\phi_k(r) = \int |P_k(s)|^2 e^{irs} dm_\infty$ es la función característica de la medida espectral $|P_k|^2 dm_\infty$.

**Proposición 9.1** (Representación aritmética de $T_\lambda$).

$$T_\lambda = \sum_{n,m} \frac{d(n)d(m)}{\sqrt{nm}} \widehat{W_\lambda dm_\infty}(\log(n/m)) - \int W_\lambda |\zeta_{on}|^2 dm_\infty.$$

El primer término es explícito en términos de primos y de los polinomios CCM. El segundo término requiere conocer $\zeta_{on}$.

### 9.3. Por qué este ángulo es prometedor

El primer término $\sum_{n,m} d(n)d(m)/\sqrt{nm} \cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ es completamente explícito y calculable. Es una función de $\lambda$ que depende solo de la estructura CCM.

Si pudiéramos mostrar que este primer término *iguala* a $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ independientemente de la posición de los ceros — es decir, que la suma aritmética ya fuerza la igualdad — tendríamos RH.

La pregunta precisa: ¿es la identidad

$$\sum_{n,m} \frac{d(n)d(m)}{\sqrt{nm}} \widehat{W_\lambda dm_\infty}(\log(n/m)) = \int W_\lambda |\zeta_{on}|^2 dm_\infty$$

verificable *sin* asumir RH?

La respuesta es: solo si $\int W_\lambda |\zeta_{on}|^2 dm_\infty = \int W_\lambda |\zeta|^2 dm_\infty$, que es RH. Hemos cerrado otro círculo.

---

## 10. Diagnóstico final: la naturaleza del obstáculo

Todos los ataques convergen al mismo obstáculo:

> **La función $|\zeta_{on}(1/2+is)|^2$ no puede calcularse explícitamente sin ya saber la posición exacta de todos los ceros de $\zeta$ (que es la información que queremos probar).**

Más precisamente:

- $|\zeta(1/2+is)|^2$ tiene una representación aritmética explícita via el producto de Euler (Prop. 9.1).
- $|\zeta_{on}(1/2+is)|^2$ no tiene esta representación — es una función construida puramente por sus ceros.
- La diferencia $|\zeta|^2 - |\zeta_{on}|^2$ no puede simplificarse sin saber explícitamente la posición de los ceros.

El formalismo CCM da una función de prueba óptima ($W_\lambda$, con positividad, motivación representación-teórica, y conexión aritmética via Weil), pero no una nueva fuente de información sobre la posición de los ceros.

---

## 11. La siguiente puerta: ¿puede calcularse $\int W_\lambda |\zeta_{on}|^2 dm_\infty$?

**Observación 11.1.** La función $|\zeta_{on}(1/2+is)|^2$ satisface:

$$|\zeta_{on}(1/2+is)|^2 = \prod_n \frac{s^2 + \gamma_n^2}{\gamma_n^2} \cdot C$$

(producto de Hadamard, solo ceros críticos, con constante de normalización $C$). Esto da:

$$\log|\zeta_{on}(1/2+is)|^2 = \sum_n \log\!\left(1 + \frac{s^2}{\gamma_n^2}\right) + \log C.$$

El integral $\int W_\lambda(s) \log|\zeta_{on}(1/2+is)|^2 dm_\infty(s)$ se puede calcular si conocemos $\phi_k(r) = \int |P_k|^2 e^{irs} dm_\infty$ explícitamente (i.e., si tenemos las asintóticas de Plancherel-Rotach completas).

Esta es la conexión con Doc 66: las asintóticas de PR para $P_k$ evaluadas en $\gamma_n$ (los ceros críticos) darían $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ explícitamente. Y comparar con $\sum_{n,m} d(n)d(m)/\sqrt{nm} \cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ daría la identidad equivalente a RH.

**La nueva puerta que se abre:** Calcular $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ explícitamente via las asintóticas de Plancherel-Rotach y comparar con la representación aritmética de $\int W_\lambda |\zeta|^2 dm_\infty$. Si los dos son iguales, RH es cierto. Si no, $\neg$RH.

Esto no es una prueba — es un cálculo cuantitativo que *verificaría* RH (o refutaría RH) si se pudiera realizar. La dificultad es que el cálculo requiere conocer los $\gamma_n$ explícitamente (los ceros de $\zeta$ sobre la recta crítica), que son infinitos y no se conocen en forma cerrada.

---

## 12. Conclusión honesta

**No hemos probado RH.** Pero hemos identificado con precisión quirúrgica dónde está el obstáculo:

> Es la imposibilidad de calcular $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ sin conocer los $\gamma_n$ (ceros críticos de $\zeta$), y la imposibilidad de comparar esto con $\int W_\lambda |\zeta|^2 dm_\infty = \sum_{n,m} d(n)d(m)/\sqrt{nm} \cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ sin asumir RH.

El formalismo CCM ha reducido RH a una identidad entre:
1. Una suma aritmética explícita (divisores, primos, transformada de Fourier de $W_\lambda dm_\infty$).
2. Un producto de Hadamard sobre los ceros críticos de $\zeta$.

Estas dos cantidades son iguales si y solo si RH es cierto.

---

*Fin del Documento 73.*
