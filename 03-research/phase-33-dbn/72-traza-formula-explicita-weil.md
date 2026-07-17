# Documento 72 — La traza CCM y la fórmula explícita de Weil

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-08  
**Prerrequisitos:** Docs 64, 69, 70, 71

---

## 1. Motivación

En Docs 70–71 la traza $T_\lambda$ apareció como un objeto que "siente" la posición de los ceros de $\zeta$ a través de la diferencia $dm_{full} - dm_{full,on}$. La fórmula explícita de Weil es la herramienta clásica que relaciona los ceros de $\zeta$ con la distribución de primos. Si $T_\lambda$ puede expresarse via la fórmula de Weil, obtenemos una lectura aritmética de la traza CCM.

---

## 2. La fórmula explícita de Weil

### 2.1. Forma estándar

Sea $h: \mathbb{R} \to \mathbb{C}$ una función de prueba que satisface: es par, analítica en la franja $|\operatorname{Im}(s)| < 1/2 + \varepsilon$ para algún $\varepsilon > 0$, y $|h(s)| = O((1+|s|)^{-2-\varepsilon})$. Sea $\hat{h}(r) = \int_{\mathbb{R}} h(s)e^{irs}\, ds$ su transformada de Fourier.

La fórmula explícita de Weil dice:

$$\sum_{\gamma} h(\gamma) = \hat{h}(0)\log(1/2\pi) + \hat{h}(i/2) - \int_{\mathbb{R}} h(s)\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{is}{2}\right)\frac{ds}{4\pi} - \sum_p\sum_{m=1}^\infty \frac{\log p}{p^{m/2}}(\hat{h}(m\log p) + \hat{h}(-m\log p)),$$

donde la suma del lado izquierdo corre sobre las partes imaginarias $\gamma$ de los ceros no triviales de $\zeta$ (con multiplicidad, y contando $\gamma$ y $-\gamma$ separadamente).

### 2.2. Variante para funciones de prueba $h = h_\lambda$

Queremos aplicar la fórmula con $h(s) = \operatorname{Im} G_{kk}^{full}(s + i0^+)/\pi$ (la parte imaginaria normalizada del resolvent diagonal), que satisface $h(s) = |P_k(s)|^2 w(s)$ donde $w$ es la densidad de $dm_\infty$.

Para la diferencia $\Delta_n^{full} - \Delta_n^{full,on}$, la función de prueba relevante sería

$$h_n(s) = (|P_{n+1}(s)|^2 - |P_n(s)|^2) w(s) = \kappa_n(s)/(a_n^\infty)^2.$$

Y para la traza sumada:

$$h_\lambda(s) = W_\lambda(s) w(s) = W_\lambda(s) \frac{dm_\infty}{ds}(s).$$

---

## 3. La traza CCM via fórmula de Weil

### 3.1. La representación de $T_\lambda$ como suma sobre ceros

De la Prop. 6.1 de Doc 69:

$$T_\lambda = \frac{1}{\pi}\int_{\mathbb{R}} W_\lambda(s)\left(|\zeta\!\left(\tfrac{1}{2}+is\right)|^2 - |\zeta_{on}\!\left(\tfrac{1}{2}+is\right)|^2\right)w(s)\, ds.$$

La diferencia $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$ puede expandirse usando el logaritmo de la función zeta:

$$\log|\zeta(1/2+is)|^2 = \log|\zeta_{on}(1/2+is)|^2 + 2\sum_{\rho\notin\text{crit.}} \log\left|\frac{1/2+is - \rho}{1/2+is - \rho'}\right|,$$

donde $\rho$ son los ceros off-critical de $\zeta$ y $\rho' = 1/2 + i\operatorname{Im}(\rho)$ son sus imágenes críticas. Exponenciando y tomando la diferencia:

$$|\zeta|^2 - |\zeta_{on}|^2 = |\zeta_{on}|^2 \left(\prod_{\rho\notin\text{crit.}}\left|\frac{1/2+is-\rho}{1/2+is-\rho'}\right|^2 - 1\right).$$

### 3.2. Linealización a primer orden

Para la estimación principal (asumiendo que si $\neg$RH hay un número finito de ceros off-critical o que la contribución de uno domina):

$$|\zeta|^2 - |\zeta_{on}|^2 \approx 2|\zeta_{on}|^2 \sum_{\rho\notin\text{crit.}}\operatorname{Re}\log\frac{1/2+is-\rho}{1/2+is-\rho'}.$$

El logaritmo:

$$\operatorname{Re}\log\frac{1/2+is-\rho}{1/2+is-\rho'} = \log\frac{|1/2+is-\rho|}{|1/2+is-\rho'|}.$$

Para $\rho = \sigma_0 + i\gamma_0$ con $\sigma_0 > 1/2$:

$$\log|1/2+is-\rho| - \log|1/2+is-\rho'| = \frac{1}{2}\log\frac{(s-\gamma_0)^2 + (\sigma_0-1/2)^2}{(s-\gamma_0)^2 + 0}.$$

Para $\sigma_0 - 1/2 \ll 1$ (cero cerca de la recta crítica):

$$\approx \frac{(\sigma_0-1/2)^2/2}{(s-\gamma_0)^2} \qquad \text{para } |s-\gamma_0| \gg \sigma_0-1/2.$$

### 3.3. La traza en términos de primos

**Proposición 3.1** (Traza CCM via Weil, primer orden).

Aplicando la fórmula explícita de Weil con función de prueba $h_\lambda(s) = W_\lambda(s)w(s)/\pi$ y usando que la suma sobre ceros es $\sum_\gamma W_\lambda(\gamma) w(\gamma)$:

$$T_\lambda = \int W_\lambda(s)(|\zeta|^2 - |\zeta_{on}|^2) dm_\infty - \text{corrección de normalización}$$

se expande (formalmente) como:

$$T_\lambda = \sum_\gamma W_\lambda(\gamma)w(\gamma)\left[P_\gamma^{off}\right] - \sum_p\sum_{m\geq 1} \frac{\log p}{p^{m/2}} B_\lambda(m\log p) + \text{término archim.},$$

donde $P_\gamma^{off}$ es la contribución de los ceros off-critical y $B_\lambda(r) = \int W_\lambda(s)w(s)e^{irs}\, ds$ es la transformada de Fourier de $W_\lambda w$.

### 3.4. La transformada de Fourier de $W_\lambda w$

De la forma de Abel de $W_\lambda$ (Doc 63, Cor. 7.2):

$$W_\lambda(s)w(s) = \sum_{n=1}^{N(\lambda)} n\, |P_n(s)|^2 w(s) + (a_{N(\lambda)}^\infty)^2|P_{N(\lambda)+1}|^2 w(s).$$

La transformada de Fourier de $|P_n|^2 w$ es la función de autocorrelación espectral de $P_n$ con peso $dm_\infty$:

$$\widehat{|P_n|^2 w}(r) = \int |P_n(s)|^2 e^{irs}\, dm_\infty(s).$$

Por la simetría $s \mapsto -s$ de $dm_\infty$ y la paridad de $|P_n|^2$, esta integral es real y par en $r$.

**Corolario 3.2.** La transformada de Fourier de la función de prueba $h_\lambda = W_\lambda w$ satisface:

$$B_\lambda(r) = \sum_{n=1}^{N(\lambda)} n\, \widehat{|P_n|^2 w}(r) + (a_{N(\lambda)}^\infty)^2\, \widehat{|P_{N(\lambda)+1}|^2 w}(r).$$

Para $r = m\log p$ (la frecuencia correspondiente al primo $p$), $B_\lambda(m\log p)$ mide cuánta correlación tienen los polinomios CCM con la frecuencia $e^{im\log p}$.

---

## 4. La fórmula aritmética de la traza

### 4.1. Forma explícita principal

**Teorema 4.1** (Fórmula aritmética de $T_\lambda$). Formalmente:

$$T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) + O(1/\sqrt{p^2}),$$

donde:
- $A_\lambda^{off} = $ contribución de los ceros off-critical de $\zeta$ (cero bajo RH).
- $B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\, dm_\infty(s)$ es la parte de $W_\lambda$ correlacionada con la frecuencia del primo $p$.

*Bajo RH:* $A_\lambda^{off} = 0$ y los términos primos se cancelan mutuamente (por la fórmula explícita aplicada a $|\zeta_{on}|^2$, que también contribuye a $T_\lambda = 0$).

### 4.2. El término primo

$$B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\, dm_\infty(s) = \sum_{n=1}^{N(\lambda)} n \int |P_n(s)|^2\cos(s\log p)\, dm_\infty(s).$$

El integral $\int |P_n(s)|^2\cos(s\log p)\, dm_\infty(s)$ es el coeficiente de Fourier de la densidad espectral del polinomio $P_n$ a frecuencia $\log p$.

**Observación 4.2.** El término de Mertens de Doc 60 (tasa de Jacobi $\Delta_n^{∞,p} = A_n/p$) es exactamente el primer término de esta expansión para la fórmula de Weil aplicada al incremento de un solo $\Delta_n$ (no a la traza completa). La fórmula aritmética del Thm. 4.1 es la versión global (sumada con pesos Abel $n$) de ese mismo cálculo.

---

## 5. Interpretación: $T_\lambda$ detecta correlaciones entre frecuencias de primos y el espectro de Jacobi CCM

### 5.1. El significado de $B_\lambda(\log p)$

$B_\lambda(\log p)$ mide cuánta "energía" de los polinomios CCM con peso Abel cae en la frecuencia $\log p$. Si $W_\lambda$ es suave a escala $\sim 1/\log p$, entonces $B_\lambda(\log p) \approx W_\lambda(0) \cdot \hat{w}(\log p)$.

Para $\log p \gg 1$ (primos grandes), $B_\lambda(\log p)$ decae exponencialmente (porque $dm_\infty$ decae como $e^{-\pi|s|/2}$ y el coseno no compensa). El término dominante viene de primos pequeños.

### 5.2. El término $p = 2$

Para el primo más pequeño $p = 2$:

$$B_\lambda(\log 2) = \sum_{n=1}^{N(\lambda)} n\int |P_n(s)|^2\cos(s\log 2)\, dm_\infty(s).$$

Esta es la correlación entre el espectro de Jacobi CCM (con pesos lineales $n$) y la frecuencia de oscilación $\log 2 \approx 0.693$.

Esto conecta con el resultado de Doc 60 (tasa para $p = 2$): $\Delta_n^{∞,2} = A_n/2 + O(\log 2/2^{3/2})$, y la suma $\sum_{n \leq N(\lambda)} n \cdot A_n/2$ es exactamente de la forma de $B_\lambda(\log 2) / 2$ (con $A_n$ los coeficientes del Thm. de tasa).

---

## 6. La fórmula aritmética como evidencia de la estructura

### 6.1. La traza es una forma lineal sobre los primos

De la fórmula del Thm. 4.1:

$$T_\lambda \approx A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p).$$

Esto dice que $T_\lambda$ se descompone en:
1. **Un término de ceros** $A_\lambda^{off}$ (contribución directa de los ceros off-critical).
2. **Una suma sobre primos** $-\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ (contribución de la distribución de primos).

Bajo RH, los dos términos se cancelan exactamente, dando $T_\lambda = 0$. Este es el mecanismo preciso por el cual RH implica $T_\lambda = 0$.

### 6.2. Nueva reformulación de RH

**Proposición 6.1** (Cancelación aritmética equivalente a RH). Las siguientes son equivalentes:

1. RH.
2. Para todo $\lambda > 0$: $\displaystyle\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = A_\lambda^{off} = 0$.
3. Para todo $\lambda > 0$ y todo primo $p$: los coeficientes de Fourier $B_\lambda(\log p)$ de la función de prueba $W_\lambda w$ son exactamente los que la fórmula de Weil predice a partir de los ceros críticos.

*Honestidad:* Esta proposición es una reformulación de RH via la fórmula de Weil — no es más difícil ni más fácil que RH. Pero da una interpretación aritmética concreta de $T_\lambda$: **la traza CCM mide cuánto se desvían los coeficientes de Fourier del espectro de Jacobi respecto a lo que la fórmula de Weil predice para ceros críticos**.

---

## 7. El término de Mertens como caso especial

La consistencia del cuadro se verifica notando que:

- Doc 60 probó $\Delta_n^{∞,p} = A_n/p + O(\log p/p^{3/2})$. Esto es la contribución de un solo primo a la discrepancia del $n$-ésimo coeficiente de Jacobi.
- El Thm. 4.1 generaliza esto: la *traza* $T_\lambda = \sum_n w_n \Delta_n$ (con pesos Abel $w_n = n$) tiene una expansión en primos donde el término de $p$ es $-(\log p/\sqrt{p}) \cdot B_\lambda(\log p)$.
- La suma de Mertens $\sum_{p \leq T} \Delta_n^{∞,p} \sim A_n\log\log T$ (Doc 60, Cor. 3.2) corresponde a $\sum_{p \leq T} B_n(\log p)/p$ donde $B_n(\log p) = \int |P_n|^2\cos(s\log p) dm_\infty \cdot A_n$ — exactamente el término de Mertens del Doc 60.

**Corolario 7.1.** La suma $\sum_{n \leq N(\lambda)} n \cdot \left(\sum_{p \leq T} \Delta_n^{∞,p}\right) \sim \left(\sum_{n \leq N(\lambda)} n A_n\right) \log\log T$. Esta es la contribución de Mertens ponderada con los pesos Abel, y es la contribución del lado aritmético a $T_\lambda$ en el caso semilocal finito.

---

## 8. Resumen y cierre de Fase 33

Los Docs 70–72 han explorado la conexión entre la traza CCM y el flujo de De Bruijn-Newman:

| Resultado | Tipo | Doc |
|-----------|------|-----|
| $\Lambda = \inf\{t: T_\lambda(t)=0\,\forall\lambda\}$ | Incondicional | 70 |
| $\partial_t T_\lambda|_{t=0}$ = forma cuadrática en $(c_k)$ | Exacto | 71 |
| Cancelación exacta de la derivada $\iff$ RH (con información inicial) | Condicional | 71 |
| $T_\lambda = A_\lambda^{off} - \sum_p (\log p/\sqrt{p}) B_\lambda(\log p)$ | Formal/Weil | 72 |
| $T_\lambda = 0 \iff$ cancelación aritmética exacta | Reformulación | 72 |
| Consistencia con Mertens (Doc 60) | Verificación | 72 |

**El estado de Fase 33:** Los tres documentos revelan la estructura de $T_\lambda$ desde ángulos distintos (flujo de calor, forma cuadrática, fórmula de Weil). Ninguno prueba RH — pero cada uno identifica dónde está el núcleo del problema:

> **El núcleo es la cancelación exacta entre el término de ceros y la suma de primos en la fórmula de Weil, con $W_\lambda$ como función de prueba.** Probar esa cancelación es precisamente RH.

La rama es viva pero el problema central permanece. El formalismo CCM-Jacobi proporciona una función de prueba natural y geométricamente motivada ($W_\lambda$) para la fórmula de Weil, lo cual puede ser de valor independiente.

---

*Fin del Documento 72 y de Fase 33.*
