# Documento 88 — El flujo DBN como trayectoria hacia la variedad Hadamard-crítica

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 70, 71, 76, 79, 82, 85

---

## Resumen

Los documentos anteriores del Camino 3 han establecido dos resultados incondicionales —la completitud del span lineal de $\{e^{i\gamma_n s}\}$ en $L^2(W_\lambda dm_\infty)$ (Doc 85) y la reformulación variacional $\tilde\delta_\lambda^2 = 0 \iff$ RH (Doc 82)— y han identificado la barrera precisa: la variedad Hadamard-crítica $M = \{|\eta_{on}|^2 : \eta_{on} \text{ Hadamard-crítico}\}$ es una subvariedad no-lineal de codimensión infinita en el espacio de aproximación lineal. El presente documento explora si el flujo De Bruijn-Newman, que ya actuó como puente entre $\Lambda$ y la traza $T_\lambda$ en el Doc 70, proporciona una geometría adicional útil: la trayectoria $t \mapsto |\Xi_t|^2$ en $L^2(W_\lambda dm_\infty)$ entra en $M$ exactamente en $t = \Lambda$.

En §1 se establece que $t \mapsto f_t := |\Xi_t|^2$ define una curva analítica en $L^2(W_\lambda dm_\infty)$. En §2 se calcula la derivada $\partial_t f_t|_{t=0}$ y se conecta con la fórmula ya conocida de la Prop. 8.2 del Doc 70. En §3 se introduce la condición de tangencia a $M$ y se muestra su relación con RH. En §4 se demuestra que la traza $T_\lambda(t)$ es continua en $t$ y se establece la equivalencia $T_\lambda(t) = 0 \iff$ todos los ceros de $\Xi_t$ son reales (extensión del CTP a cada $t$). En §5 se estudia el flujo como homotopía entre $f_0$ y la variedad $M$. En §6 se examina el comportamiento de la trayectoria para $t \to \infty$. En §7 se analiza con honestidad la estrategia conjetural del flujo y por qué no produce una prueba de RH. En §8 se hace la síntesis del Camino 3 y se formula el obstáculo residual.

---

## §1. La curva $t \mapsto f_t$ en $L^2(W_\lambda\,dm_\infty)$

### 1.1. Definición del flujo y notación

Recordamos del Doc 70 (§2.1) que la función deformada de De Bruijn-Newman es

$$\Xi_t(s) = \int_{-\infty}^\infty e^{tu^2}\Phi(u)\,e^{isu}\,du, \qquad t \geq 0,$$

donde

$$\Phi(u) = \sum_{n=1}^\infty \bigl(2\pi^2 n^4 e^{9u/2} - 3\pi n^2 e^{5u/2}\bigr)\,e^{-\pi n^2 e^{2u}}$$

es el núcleo de Jacobi theta. Para $t = 0$: $\Xi_0 = \Xi$ (la función xi de Riemann estándar, $\Xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)|_{s=1/2+is}$ en la variable imaginaria). Para $t > \Lambda$: todos los ceros de $\Xi_t$ son reales (De Bruijn 1950).

Definimos la curva

$$f_t : s \mapsto |\Xi_t(s)|^2, \qquad t \geq 0.$$

### 1.2. La curva toma valores en $L^2(W_\lambda\,dm_\infty)$

**Proposición 1.1.** *Para cada $t \geq 0$, $f_t \in L^2(W_\lambda\,dm_\infty)$.*

*Demostración.* El factor $e^{tu^2}$ multiplica el integrando de $\Xi_t$. La función $\Phi$ decae superexponencialmente: por la estimación del Doc 70 (§2.1), $|\Phi(u)| = O(e^{-\pi e^{2u}})$ cuando $u \to +\infty$ y $|\Phi(u)| = O(e^{5|u|/2})$ cuando $u \to -\infty$, de modo que $|e^{tu^2}\Phi(u)| \leq C_T e^{-\pi e^{2u}/2}$ para $u \geq 0$ y $|e^{tu^2}\Phi(u)| \leq C_T e^{(t+1)u^2}$ para $u \leq 0$, con constante $C_T$ uniforme en $t \in [0,T]$. Por el teorema de Riemann-Lebesgue aplicado a la transformada de Fourier del integrando (que es integrable en $u$), $\Xi_t(s)$ decae rápidamente en $|s| \to \infty$. En particular, $|f_t(s)| = O(e^{-c|s|})$ para algún $c > 0$ dependiente de $t$. La medida $dm_\infty$ tiene densidad $w(s) \sim |s|^{-1/2}e^{-\pi|s|/2}$ y el peso $W_\lambda$ está acotado, de modo que $\int W_\lambda f_t^2\,dm_\infty < \infty$. $\square$

### 1.3. Analiticidad en $t$

**Proposición 1.2.** *La curva $t \mapsto \Xi_t$ en $L^2(W_\lambda\,dm_\infty)$ es analítica real en $t \geq 0$, y en consecuencia $t \mapsto f_t = |\Xi_t|^2$ es analítica real en $L^2(W_\lambda\,dm_\infty)$.*

*Demostración.* Para derivar bajo el signo integral en la norma $L^2(W_\lambda\,dm_\infty)$ basta verificar que $\partial_t^k e^{tu^2} = u^{2k}e^{tu^2}$ y que las estimaciones $\|u^{2k}e^{Tu^2}\Phi(u)\|_{L^1(du)} < \infty$ para todo $k \geq 0$ y $T < \infty$ se satisfacen por el decaimiento superexponencial de $\Phi$. La convergencia de la serie de Taylor $\Xi_t = \sum_{k=0}^\infty \frac{t^k}{k!}\int u^{2k}\Phi(u)e^{isu}\,du$ en la norma de $L^2(W_\lambda\,dm_\infty)$ se sigue del teorema de convergencia dominada y la estimación uniforme en $s$ de los términos. La analiticidad de $f_t = |\Xi_t|^2 = \Xi_t\overline{\Xi_t}$ se obtiene de la de $\Xi_t$ por bilinealidad. $\square$

### 1.4. La variedad Hadamard-crítica como subconjunto de $L^2(W_\lambda\,dm_\infty)$

Recordamos del Doc 82 (§3) que la variedad Hadamard-crítica es

$$M := \bigl\{|\eta_{on}|^2 : \eta_{on} \text{ es una función entera de orden 1 con todos sus ceros en }\operatorname{Re}(\rho) = 1/2\bigr\} \cap L^2(W_\lambda\,dm_\infty).$$

Más precisamente, $\eta_{on}$ es una función Hadamard-crítica si tiene la misma factorización de Hadamard que $\Xi$ pero con todos sus ceros proyectados a la recta crítica: $\eta_{on}(s) = e^{A+Bs}\prod_n (1 - s/\gamma_n)e^{s/\gamma_n}$ donde todos los $\gamma_n$ son reales.

**Proposición 1.3.** *Para $t > \Lambda$: $f_t \in M$. Para $t \in [0,\Lambda)$: $f_t \notin M$.*

*Demostración.* Para $t > \Lambda$: todos los ceros de $\Xi_t$ son reales por definición de $\Lambda$, luego $\Xi_t$ es Hadamard-crítica y $f_t = |\Xi_t|^2 \in M$. Para $t \in [0,\Lambda)$: por definición de $\Lambda$, $\Xi_t$ tiene al menos un cero con parte imaginaria no nula, luego $f_t \notin M$. $\square$

La trayectoria $t \mapsto f_t$ entra en $M$ exactamente en $t = \Lambda$: es el primer tiempo en que la curva toca la variedad Hadamard-crítica.

---

## §2. La derivada del flujo en $t = 0$

### 2.1. Cálculo de $\partial_t\Xi_t|_{t=0}$

Derivando bajo el signo integral:

$$\partial_t \Xi_t\big|_{t=0} = \int_{-\infty}^\infty u^2\Phi(u)\,e^{isu}\,du.$$

Por otro lado, la segunda derivada de $\Xi_0 = \Xi$ respecto a $s$ es

$$\Xi_0''(s) = \frac{d^2}{ds^2}\int \Phi(u)e^{isu}\,du = \int (iu)^2\Phi(u)e^{isu}\,du = -\int u^2\Phi(u)e^{isu}\,du.$$

Por tanto:

$$\partial_t\Xi_t\big|_{t=0} = -\Xi_0''(s).$$

### 2.2. La derivada de $f_t$ en $t = 0$

**Proposición 2.1.** *La derivada de la curva $f_t = |\Xi_t|^2$ en $t = 0$ es*

$$\partial_t f_t\big|_{t=0} = 2\operatorname{Re}\bigl[\overline{\Xi_0(s)}\,\partial_t\Xi_t|_{t=0}\bigr] = -2\operatorname{Re}\bigl[\overline{\Xi_0(s)}\,\Xi_0''(s)\bigr].$$

*Explícitamente:* $\partial_t f_t|_{t=0} = -2\bigl[\operatorname{Re}(\Xi_0)\operatorname{Re}(\Xi_0'') + \operatorname{Im}(\Xi_0)\operatorname{Im}(\Xi_0'')\bigr].$

*Demostración.* Regla de la cadena para $|\cdot|^2 = (\cdot)\overline{(\cdot)}$ y la fórmula del apartado anterior. La función $\Xi$ es de valor real en la recta crítica (parte imaginaria $\equiv 0$ cuando $s \in \mathbb{R}$ y $\Xi_0$ es real: ver e.g. Doc 70, §2.1), de modo que $\overline{\Xi_0(s)} = \Xi_0(s)$ para $s \in \mathbb{R}$ y la fórmula se simplifica, pero se escribe en la forma general para claridad. $\square$

### 2.3. Consistencia con el Doc 71

El Doc 71 (§1, fórmula principal) demostró que

$$\partial_t T_\lambda\big|_{t=0} = -4\int W_\lambda(s)\operatorname{Re}\bigl(\overline{H_0(s)}\,H_0''(s)\bigr)\,dm_\infty(s)$$

donde $H_0 = \Xi_0$. Esto es precisamente

$$\partial_t T_\lambda\big|_{t=0} = 2\int W_\lambda(s)\,\partial_t f_t\big|_{t=0}\,dm_\infty(s).$$

La derivada temporal de $T_\lambda$ coincide (salvo el factor $2$) con la integral de la derivada de la curva $f_t$ contra el peso $W_\lambda\,dm_\infty$. La coherencia entre las dos formulaciones es inmediata.

---

## §3. La condición de tangencia a $M$

### 3.1. El espacio tangente a $M$ en $f_0$

La variedad $M$ está parametrizada localmente por las posiciones $\{\gamma_n\} \subset \mathbb{R}$ de los ceros críticos. Si $f_0 = |\Xi_0|^2 \in M$ (es decir, si todos los ceros de $\Xi_0$ están en la recta crítica, i.e., si RH vale), el espacio tangente en $f_0$ es

$$T_{f_0}M = \overline{\operatorname{span}}\bigl\{\partial_{\gamma_n}|\eta_{on}|^2\big|_{\eta_{on}=\Xi_0} : n \geq 1\bigr\}^{L^2(W_\lambda dm_\infty)}.$$

La derivada en la dirección del $n$-ésimo cero es

$$\partial_{\gamma_n}|\eta_{on}|^2\big|_{\eta_{on}=\Xi_0} = 2\operatorname{Re}\bigl[\overline{\Xi_0(s)}\,\partial_{\gamma_n}\Xi_0(s)\bigr].$$

Dado que $\Xi_0(s) = A\prod_k(1 - s/\gamma_k)e^{s/\gamma_k}$ (factorización de Hadamard con ceros simples $\{\pm\gamma_k\}$), la derivada respecto a $\gamma_n$ del producto da

$$\partial_{\gamma_n}\Xi_0(s) = \Xi_0(s)\cdot\partial_{\gamma_n}\log\Xi_0(s) = \Xi_0(s)\cdot\Bigl(\frac{s}{\gamma_n^2} - \frac{s}{\gamma_n - s} \cdot \frac{1}{\gamma_n}\Bigr).$$

El espacio tangente $T_{f_0}M$ contiene funciones de la forma $2\operatorname{Re}[\overline{\Xi_0}\Xi_0 \cdot g_n]$ donde $g_n$ son funciones meromorfas con polos en los ceros de $\Xi_0$.

### 3.2. La derivada del flujo como vector tangente (bajo RH)

**Proposición 3.1.** *Si RH vale ($\Lambda = 0$), entonces $\partial_t f_t|_{t=0} \in T_{f_0}M$.*

*Demostración.* Bajo RH, $f_0 \in M$ (todos los ceros de $\Xi_0$ son críticos) y la curva $t \mapsto f_t$ satisface $f_t \in M$ para todo $t \geq 0$ (pues para $t \geq 0 = \Lambda$ todos los ceros de $\Xi_t$ son reales). En consecuencia, la curva entera $t \mapsto f_t$ está contenida en $M$ para $t \geq 0$, y su derivada en $t = 0$ es un vector tangente a $M$ en $f_0$. $\square$

*Observación.* Bajo $\neg$RH ($\Lambda > 0$), la curva $t \mapsto f_t$ llega a $M$ únicamente en $t = \Lambda$. La derivada $\partial_t f_t|_{t=0}$ no pertenece a $T_{f_0}M$ sino que apunta hacia el interior del complemento $L^2(W_\lambda dm_\infty) \setminus M$ (si $f_0 \notin M$ el espacio tangente a $M$ en $f_0$ ni siquiera está definido).

---

## §4. Continuidad de $T_\lambda(t)$ y extensión del CTP

### 4.1. El criterio CTP para cada $t$

**Proposición 4.1.** *Para cada $t \geq 0$ fijo: $T_\lambda(t) = 0$ para todo $\lambda > 0$ si y solo si todos los ceros de $\Xi_t$ son reales.*

*Demostración.* Idéntica a la del Thm. 3.1 del Doc 64, reemplazando $\Xi_0$ por $\Xi_t$ en todos los argumentos. La estructura de los coeficientes de Jacobi de la medida $|\Xi_t|^2 dm_\infty$ está determinada por la posición de los ceros de $\Xi_t$ de exactamente la misma manera que para $t = 0$. $\square$

### 4.2. Continuidad de $T_\lambda(t)$ en $t$

**Proposición 4.2.** *La función $t \mapsto T_\lambda(t)$ es continua en $[0,\infty)$ para cada $\lambda > 0$ fijo.*

*Demostración.* Por definición, $T_\lambda(t)$ se expresa en términos de los coeficientes de Jacobi de la medida $|\Xi_t|^2 dm_\infty$ (ver Doc 70, §3.2). Estos coeficientes dependen continuamente de $t$ si la medida $|\Xi_t|^2 dm_\infty$ varía continuamente en $t$ en sentido débil. Tenemos $|\Xi_t(s)|^2 = \bigl|\int e^{tu^2}\Phi(u)e^{isu}du\bigr|^2$, que es continua en $t$ para cada $s$ fijo por la continuidad del integrando $e^{tu^2}\Phi(u)$ en $t$. La convergencia dominada aplica para $t$ en compactos $[0,T]$: el dominador es $\bigl|\int e^{Tu^2}|\Phi(u)|\,du\bigr|^2$ que es finito por el decaimiento superexponencial de $\Phi$. Luego $|\Xi_t(s)|^2 \to |\Xi_{t_0}(s)|^2$ en $L^1(W_\lambda\,dm_\infty)$ cuando $t \to t_0$, lo que implica la convergencia débil de las medidas y la continuidad de los coeficientes de Jacobi. $\square$

**Corolario 4.3.** *$\lim_{t \to 0^+} T_\lambda(t) = T_\lambda(0)$ para cada $\lambda > 0$.*

### 4.3. Reformulación de $\Lambda$ via continuidad

El Doc 70 (§4) estableció $\Lambda = \inf\{t \geq 0 : T_\lambda(t) = 0\;\forall\lambda\}$. La continuidad de $T_\lambda(t)$ permite precisar este infimum:

**Corolario 4.4.** *$\Lambda = \min\{t \geq 0 : T_\lambda(t) = 0\;\forall\lambda\}$ si el infimum es alcanzado; i.e., si $\Lambda < \infty$ entonces $T_\lambda(\Lambda) = 0$ para todo $\lambda > 0$.*

*Demostración.* Sea $\{t_n\}$ una sucesión decreciente con $t_n \to \Lambda$ y $T_\lambda(t_n) = 0$ para todo $n$ y todo $\lambda$. Por continuidad de $T_\lambda(\cdot)$, $T_\lambda(\Lambda) = \lim_{n} T_\lambda(t_n) = 0$. $\square$

Este resultado es conocido indirectamente (los ceros de $\Xi_\Lambda$ son todos reales, ver De Bruijn 1950), pero la demostración via continuidad de $T_\lambda$ es coherente con el formalismo CCM.

---

## §5. El flujo como homotopía y tiempo de entrada en $M$

### 5.1. La trayectoria $[0,\infty) \to L^2(W_\lambda\,dm_\infty)$

La curva $\gamma : t \mapsto f_t$ es una trayectoria analítica real en $L^2(W_\lambda\,dm_\infty)$ (Prop. 1.2) que parte de $f_0 = |\Xi_0|^2 \in L^2(W_\lambda\,dm_\infty)$ y satisface:

- Para $t \in [0,\Lambda)$: $\gamma(t) \notin M$ (hay ceros off-critical, Prop. 1.3).
- Para $t \geq \Lambda$: $\gamma(t) \in M$ (todos los ceros son reales, Prop. 1.3).
- $\gamma(\Lambda) = f_\Lambda \in M$ (límite en $t = \Lambda$ por Prop. 4.2 y Cor. 4.3).

La trayectoria entra en $M$ exactamente en el tiempo $t = \Lambda$, y permanece en $M$ para todo $t$ posterior.

### 5.2. Formulación como problema de primer tiempo de llegada

La constante de De Bruijn-Newman se puede leer como el **primer tiempo de llegada** de la trayectoria $\gamma$ a la subvariedad $M$:

$$\Lambda = \inf\{t \geq 0 : \gamma(t) \in M\}.$$

Esta formulación geométrica en $L^2(W_\lambda\,dm_\infty)$ es equivalente a la definición original de $\Lambda$ (via la posición de los ceros de $\Xi_t$) y equivalente a la del Doc 70 (via la extinción de $T_\lambda(t)$). Las tres formulaciones son reformulaciones del mismo hecho.

### 5.3. El caso RH $\iff$ partida desde $M$

**Proposición 5.1.** *$\Lambda = 0$ si y solo si $\gamma(0) = f_0 \in M$, lo que es equivalente a RH.*

*Demostración.* $\Lambda = 0 \iff$ todos los ceros de $\Xi_0$ son reales $\iff f_0 \in M \iff$ RH. La equivalencia entre $\Lambda = 0$ y RH es el resultado de Rodgers-Tao (2018: $\Lambda \geq 0$) combinado con el enunciado $\Lambda \leq 0 \iff$ RH. $\square$

Bajo RH, la trayectoria comienza en $M$ y permanece en $M$ para todo $t \geq 0$. Bajo $\neg$RH, la trayectoria empieza en el exterior de $M$ y llega a $M$ por primera vez en $t = \Lambda > 0$.

---

## §6. Comportamiento asintótico de la trayectoria para $t \to \infty$

### 6.1. Crecimiento de $\Xi_t$ y dispersión de ceros

Para $t \to \infty$ el factor $e^{tu^2}$ concentra la masa del integrando de $\Xi_t$ en los valores de $u$ que maximizan $tu^2 - \pi n^2 e^{2u}$ (competencia entre el factor gaussiano y el decaimiento de $\Phi$). El análisis de punto de silla da que la contribución dominante proviene de $u^* \sim \frac{1}{2}\log(t/(2\pi n^2))$, y la función $\Xi_t$ crece como $e^{t(\log t)^2/4}$ cuando $t \to \infty$ (crecimiento superexponencial).

Los ceros de $\Xi_t$ para $t \to \infty$ se distribuyen con densidad creciente: la $n$-ésima parte imaginaria de los ceros satisface $\gamma_n(t) \sim c\sqrt{t}\cdot h(n)$ donde $h(n)$ depende de la distribución de ceros de $\Xi_0$. La separación entre ceros consecutivos crece como $\sqrt{t}$, de modo que los ceros se dispersan a medida que $t$ aumenta.

### 6.2. La función $f_t$ para $t \to \infty$ como elemento de $M$

Para cada $t > \Lambda$, $f_t \in M$, pero los elementos de $M$ que parametrizan $f_t$ tienen ceros en $\{\pm\gamma_n(t)\}$ que se dispersan a infinito cuando $t \to \infty$. En el límite $t \to \infty$, la función $f_t/\|f_t\|$ converge débilmente a cero en $L^2(W_\lambda\,dm_\infty)$ (la masa se escapa a infinito). La trayectoria $\gamma(t)$ no converge en norma a ningún punto de $M$ cuando $t \to \infty$; en cambio, $\|f_t\|_{L^2} \to \infty$ y la trayectoria "escapa" a infinito en el espacio.

La homotopía entre $f_0$ y $M$ que proporciona el flujo DBN es por tanto una homotopía hacia un punto de $M$ que depende de $t$, no hacia un punto fijo. La trayectoria entra en $M$ en $t = \Lambda$ pero continúa moviéndose dentro de $M$ indefinidamente.

---

## §7. La estrategia conjetural del flujo y su obstáculo

### 7.1. La idea y por qué no funciona

La continuidad de $T_\lambda(t)$ (Prop. 4.2) y el hecho de que $T_\lambda(t) = 0$ para $t > \Lambda$ sugieren la siguiente estrategia para probar RH: si se puede demostrar que $T_\lambda(t) = 0$ para algún $t > 0$ (por argumentos independientes de la posición de los ceros de $\Xi_0$), entonces por continuidad $T_\lambda(0) = 0$, es decir RH.

El obstáculo es que la condición $T_\lambda(t) = 0$ para $t > 0$ es precisamente equivalente a que todos los ceros de $\Xi_t$ sean reales (Prop. 4.1), lo cual es cierto para $t > \Lambda$ pero que $\Lambda = 0$ (i.e., $t = 0^+$ ya tiene $T_\lambda = 0$) es de nuevo RH. No hay ninguna forma de verificar $T_\lambda(t) = 0$ para $t > 0$ fijo sin conocer la posición de los ceros de $\Xi_t$, y conocer esa posición para $t$ pequeño equivale a conocer la posición de los ceros de $\Xi_0$ (por continuidad de los ceros en $t$).

### 7.2. La conjetura de monotonía y su insuficiencia

El Doc 70 formuló la conjetura:

**Conjetura de Monotonía.** *$t \mapsto T_\lambda(t)$ es no creciente en $[0,\infty)$.*

Si esta conjetura fuera cierta:
- Para $t > \Lambda$: $T_\lambda(t) = 0$.
- Para $0 \leq t \leq \Lambda$: $T_\lambda(t) \geq T_\lambda(\Lambda) = 0$ (por monotonía).
- En particular, $T_\lambda(0) \geq 0$.

Pero esto ya se sabe: $T_\lambda(0) \geq 0$ es la desigualdad demostrada en el Doc 83 (la dominación de medidas $dm_{full} \geq dm_{full,on}$ implica $T_\lambda(0) \geq 0$). La monotonía confirmaría que la trayectoria es no creciente pero no probaría que $T_\lambda(0) = 0$.

Para probar RH a partir de la monotonía se necesitaría un argumento adicional que obligue a $T_\lambda(0)$ a ser cero, no meramente no negativo. Tal argumento no se conoce.

### 7.3. La condición de derivada cero y su coherencia

Bajo RH ($\Lambda = 0$): la curva $\gamma$ está en $M$ para todo $t \geq 0$, luego $T_\lambda(t) = 0$ para todo $t \geq 0$, y en particular $\partial_t T_\lambda|_{t=0} = 0$.

El Doc 71 calculó que

$$\partial_t T_\lambda\big|_{t=0} = -4\int W_\lambda(s)\operatorname{Re}\bigl(\overline{\Xi_0(s)}\,\Xi_0''(s)\bigr)\,dm_\infty(s)$$

y demostró que esta expresión es una forma cuadrática en los coeficientes $c_k = \langle \Xi_0, P_k\rangle_{dm_\infty}$ que se cancela exactamente cuando los ceros de $\Xi_0$ son críticos (condición algebraica sobre los $c_k$). La condición $\partial_t T_\lambda|_{t=0} = 0$ es por tanto otra reformulación de RH, no un resultado nuevo.

**Proposición 7.1.** *Las siguientes condiciones son equivalentes:*
*(i) RH;*
*(ii) $T_\lambda(0) = 0$ para todo $\lambda > 0$;*
*(iii) $T_\lambda(t) = 0$ para todo $t \geq 0$ y todo $\lambda > 0$;*
*(iv) $\partial_t T_\lambda|_{t=0} = 0$ para todo $\lambda > 0$;*
*(v) $f_0 \in M$;*
*(vi) $\Lambda = 0$.*

*Demostración.* La equivalencia (i) $\iff$ (ii) es el CTP (Doc 64). La equivalencia (ii) $\iff$ (vi) es la caracterización del Doc 70. La equivalencia (vi) $\iff$ (v) es la Prop. 5.1. La implicación (iii) $\implies$ (ii) es inmediata. La implicación (i) $\implies$ (iii): bajo RH, $T_\lambda(t) = 0$ para $t \geq 0$ porque $\Lambda = 0$ y $T_\lambda(t) = 0$ para $t \geq \Lambda = 0$. La equivalencia (ii) $\iff$ (iv): el Doc 71 demuestra que $\partial_t T_\lambda|_{t=0} = 0$ iff los coeficientes $c_k$ satisfacen la condición de cancelación, que es equivalente a que todos los ceros de $\Xi_0$ sean críticos. $\square$

La multiplicidad de formulaciones equivalentes refleja la coherencia interna del formalismo, no una ganancia de información.

---

## §8. Síntesis del Camino 3 y el obstáculo residual

### 8.1. Resultados incondicionales establecidos

El Camino 3 ha producido los siguientes resultados rigurosos e incondicionales:

**R1 (Doc 82, Cor. 4.6).** El infimum variacional $\tilde\delta_\lambda^2 := \inf\{\||\zeta|^2 - |\eta_{on}|^2\|^2_{L^2(W_\lambda dm_\infty)} : \eta_{on} \in M\}$ satisface $\tilde\delta_\lambda^2 = 0 \iff$ RH.

**R2 (Doc 85, Thm. 5.1).** El span lineal de $\{e^{i\gamma_n s}\}_{n \geq 1}$ es denso en $L^2(W_\lambda\,dm_\infty)$. Los $\gamma_n = \operatorname{Im}(\rho_n)$ son siempre reales por la ecuación funcional, independientemente de RH.

**R3 (este documento, Prop. 1.2 y Prop. 4.2).** La curva $t \mapsto f_t = |\Xi_t|^2$ es analítica real en $L^2(W_\lambda\,dm_\infty)$ y la traza $t \mapsto T_\lambda(t)$ es continua en $[0,\infty)$.

**R4 (este documento, Prop. 5.1).** $\Lambda = \inf\{t \geq 0 : f_t \in M\}$, y $\Lambda = 0 \iff f_0 \in M \iff$ RH.

**R5 (este documento, Prop. 7.1).** Las condiciones (i)–(vi) de la Prop. 7.1 son todas equivalentes a RH.

### 8.2. La brecha que persiste

Los resultados R1–R5 son reformulaciones equivalentes de RH en el espacio $L^2(W_\lambda\,dm_\infty)$. La brecha es siempre la misma: pasar de la aproximación lineal (R2: span lineal denso) a la membresía en la clase no-lineal $M$ (R1: el infimum $\tilde\delta_\lambda^2$ es cero).

La aproximación lineal dice: $|\zeta|^2$ puede aproximarse en norma $L^2$ por combinaciones lineales de funciones que incluyen elementos de $M$. La membresía en $M$ dice: $|\zeta|^2$ es exactamente un elemento de $M$, es decir $\zeta$ tiene todos sus ceros en la recta crítica. La distancia de una clase lineal a una subvariedad no-lineal puede ser cero sin que el punto pertenezca a la subvariedad (se puede aproximar arbitrariamente bien sin alcanzar). La equivalencia $\tilde\delta_\lambda^2 = 0 \iff$ RH afirma que en este caso concreto la distancia es cero exactamente cuando se alcanza la variedad, pero esto es el contenido de RH, no una consecuencia de la teoría de aproximación.

### 8.3. La pregunta abierta que resume el Camino 3

El único camino no circular identificado en el Camino 3 requiere probar incondicionalmente una de las siguientes:

**(Q1)** Que $\partial_t T_\lambda|_{t=0} \leq 0$ (derivada temporal no positiva), o más fuerte, que la Conjetura de Monotonía vale. Esto no probaría RH pero restringiría el comportamiento de $T_\lambda$ y podría combinarse con otros argumentos.

**(Q2)** Que $T_\lambda(t) = 0$ para algún $t > 0$ específico sin usar la posición de los ceros de $\Xi_t$. Esto implicaría RH por continuidad, pero se desconoce cómo hacerlo: la única herramienta para demostrar $T_\lambda(t) = 0$ pasa por conocer los ceros, que es precisamente lo que no se conoce.

**(Q3)** Que la función $t \mapsto \Lambda(f_t, M)$ (distancia de $f_t$ a $M$ en $L^2(W_\lambda\,dm_\infty)$) tiene una velocidad de decrecimiento que fuerza $\Lambda(f_0, M) = 0$ por un argumento de comparación. Tal argumento requeriría una estimación cuantitativa de la geometría de $M$ (curvatura, radio de inyectividad) que actualmente no está disponible.

Ninguna de las tres vías está desbloqueada. El flujo DBN como curva en $L^2(W_\lambda\,dm_\infty)$ proporciona una imagen geométrica limpia de RH ($f_0 \in M$) y de $\Lambda$ (primer tiempo de llegada a $M$), pero no una estrategia de prueba nueva.

---

## §9. Conclusión

El Documento 88 cierra el Camino 3 con la siguiente descripción geométrica de su contenido:

En el espacio $L^2(W_\lambda\,dm_\infty)$, la hipótesis de Riemann equivale a que el punto $f_0 = |\Xi_0|^2$ pertenece a la subvariedad no-lineal $M$ de codimensión infinita. El flujo De Bruijn-Newman define una curva analítica $t \mapsto f_t$ que entra en $M$ exactamente en el tiempo $\Lambda$ (la constante de De Bruijn-Newman). La traza $T_\lambda(t)$ mide la distancia de $f_t$ a $M$ (en el sentido de los coeficientes de Jacobi) y es continua en $t$.

La reformulación es coherente, completa y honesta: cada uno de los criterios equivalentes a RH que el Camino 3 ha producido (el variacional, el de completitud, el del flujo, el de la derivada temporal) son diferentes formulaciones de la misma cosa. La geometría del flujo DBN en $L^2(W_\lambda\,dm_\infty)$ no abre una nueva ruta hacia la prueba; ilustra la equivalencia $\Lambda = 0 \iff$ RH en lenguaje geométrico, sin añadir herramientas para verificar esa equivalencia de manera no circular.

El obstáculo fundamental del Camino 3 —la brecha entre aproximación lineal y membresía en la clase no-lineal— permanece abierto.

---

*Fin del Documento 88.*
