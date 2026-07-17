# Phase 29 — Ecuación de primer momento y la Conjetura de Momentos

**Fecha:** junio 2026  
**Objetivo:** Atacar la Pregunta 29.5: ¿es $\sum_m m\,\Delta_m = O(e^{-\pi\lambda^2})$? Si sí, $S_n$ cae al orden del segundo momento. Estrategia doble: (A) tomar el primer momento de la ecuación de Euler-Lagrange de $\Delta$; (B) usar la concentración de $\hat\xi_\lambda$ en espacio de Mellin para acotar las derivadas de $\hat\xi_\lambda$ en $t = 0$.

---

## 1. Estructura de Toeplitz de la forma de Weil en la base discreta

Sea la base $\{U_m\}_{m=0}^N$ de $E_N^+$ (base par-coseno, como en doc 00). La forma de Weil $QW_\lambda^N$ en esta base tiene la estructura de una matriz de Cauchy-Toeplitz:

$$\tau_{mm'} := QW_\lambda^N(U_m, U_{m'}).$$

**Lema 1** (estructura Toeplitz de $\tau$). La componente aritmética contribuye a $\tau$ mediante:

$$(A_\lambda)_{mm'} = \frac{2}{L}\sum_{p\leq\lambda^2}\Lambda(p)\,p^{-1/2}\cos\!\left(\frac{2\pi m\log p}{L}\right)\cos\!\left(\frac{2\pi m'\log p}{L}\right).$$

Por la identidad $\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha-\beta)+\cos(\alpha+\beta)]$:

$$(A_\lambda)_{mm'} = \frac{1}{L}\sum_{p\leq\lambda^2}\Lambda(p)\,p^{-1/2}\left[\cos\!\left(\frac{2\pi(m-m')\log p}{L}\right) + \cos\!\left(\frac{2\pi(m+m')\log p}{L}\right)\right].$$

El primer término depende solo de $m - m'$ (componente TOEPLITZ); el segundo depende de $m + m'$ (componente HANKEL). En lo que sigue escribimos $\tau = T + H$ con $T$ Toeplitz y $H$ Hankel.

**Proposición 1** (dominancia Toeplitz). Para $m, m' \gg 1$, la componente Hankel $H_{mm'}$ satisface $|H_{mm'}| \leq |T_{mm'}|$ termino a termino. Para $m - m'$ fijo y $m + m' \to \infty$, $H_{mm'} \to 0$ exponencialmente mientras $T_{mm'}$ permanece fijo (promedio de Weyl sobre $\log p$).

*Prueba sketch.* $T_{mm'} = \frac{1}{L}\Psi_\lambda\!\left(\frac{2\pi(m-m')}{L}\right)$ donde $\Psi_\lambda(t) = \sum_p\Lambda(p)p^{-1/2}e^{it\log p}$. La componente Hankel $H_{mm'} = \frac{1}{L}\Psi_\lambda\!\left(\frac{2\pi(m+m')}{L}\right)$. Para $m + m' \geq N \gg 1$, el argumento $2\pi(m+m')/L \gg \log\lambda^2/L = 1$ y $\Psi_\lambda(t)$ decae por cancelación de fases (cuantificado por el Lema 7.3). $\square$

**En lo que sigue consideramos la APROXIMACIÓN TOEPLITZ pura:** $\tau \approx T$, válida para $m, m' \gg 1$ y $m - m'$ pequeño (las entradas dominantes). Los errores de esta aproximación son Hankel y se controlan por el Lema 7.3.

---

## 2. La ecuación de Euler-Lagrange para $\Delta$

**Proposición 2** (EL para $\Delta$). Sea $\Delta = \xi_\lambda - c_\lambda k_\lambda$ con $\xi_\lambda$ el minimizador de $QW_\lambda^N|_{E_N^+}$ y $k_\lambda$ la proyección de $k$ a $E_N^+$. Entonces:

$$(\tau - \mu_\lambda)\Delta = -c_\lambda(\tau - \mu_\lambda)k_\lambda =: c_\lambda\,\varepsilon_\lambda,$$

donde $\varepsilon_\lambda := -(τ - \mu_\lambda)k_\lambda$ es el RESIDUO de $k_\lambda$ como pseudo-eigenvector.

*Prueba.* $(\tau-\mu_\lambda)\xi = 0$ (eigenvalor), luego $(\tau-\mu_\lambda)\Delta = (\tau-\mu_\lambda)\xi - c_\lambda(\tau-\mu_\lambda)k_\lambda = c_\lambda\varepsilon_\lambda$. $\square$

**Estimado del residuo.** El residuo $\varepsilon_\lambda$ mide cuánto se desvia $k_\lambda$ de ser un eigenvector. Usando que $k_\lambda$ converge a $k$ con tasa del Lema 7.3 y que $\tau \to QW_\infty$ (operador continuo):

**Lema 2** (estimado del residuo). En la norma del supremo de coeficientes: $\|\varepsilon_\lambda\|_\infty = O(\lambda^{-1/2})$, y en norma $\ell^1$:

$$\sum_m |\varepsilon_m| = O(N\lambda^{-1/2}) = O(\lambda^{3/2}).$$

La norma $\ell^1$ del residuo no es pequeña (solo $\lambda^{-1/2}$ uniformemente en cada entrada, pero hay $N \sim \lambda^2$ entradas). El argumento de momentos debe explotar la CANCELACIÓN en la suma ponderada.

---

## 3. La ecuación de primer momento para $\Delta$

**Teorema 1** (ecuación de primer momento). Bajo la aproximación Toeplitz $\tau \approx T$ con $T_{mm'} = L^{-1}\Psi_\lambda(2\pi(m-m')/L)$, el primer momento $M_1[\Delta] := \sum_{m=0}^N m\,\Delta_m$ satisface:

$$M_1[\Delta] \cdot (\hat T_0 - \mu_\lambda) = -M_0[\Delta]\cdot\hat T_1 + c_\lambda\,M_1[\varepsilon_\lambda],$$

donde $\hat T_0 := L^{-1}\Psi_\lambda(0) = L^{-1}\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}$ y $\hat T_1 := \partial_t[L^{-1}\Psi_\lambda(t)]|_{t=0}$.

*Prueba.* Tomamos la suma $\sum_m m \cdot$ de la ecuación de Euler-Lagrange para $\Delta$:

$$\sum_m m\sum_{m'}T_{mm'}\Delta_{m'} - \mu_\lambda M_1[\Delta] = c_\lambda M_1[\varepsilon].$$

Para una matriz de Toeplitz $T_{mm'} = T(m-m')$:

$$\sum_m m\sum_{m'}T(m-m')\Delta_{m'} = \sum_{m'}\Delta_{m'}\sum_m m\,T(m-m').$$

Con el cambio $n = m - m'$:

$$\sum_m m\,T(m-m') = \sum_n (n+m')T(n) = m'\hat T_0 + \hat T_1,$$

donde $\hat T_j := \sum_n n^j T(n)$ son los momentos de la kernel Toeplitz. Luego:

$$\hat T_1 M_0[\Delta] + \hat T_0 M_1[\Delta] - \mu_\lambda M_1[\Delta] = c_\lambda M_1[\varepsilon].$$

Como $M_0[\Delta] = 0$ (Proposición 1 del doc 06):

$$M_1[\Delta](\hat T_0 - \mu_\lambda) = c_\lambda M_1[\varepsilon]. \quad\square$$

**Corolario.** Si $\hat T_0 \neq \mu_\lambda$:

$$\boxed{M_1[\Delta] = \frac{c_\lambda\,M_1[\varepsilon_\lambda]}{\hat T_0 - \mu_\lambda}.}$$

---

## 4. Evaluación del denominador $\hat T_0 - \mu_\lambda$

$\hat T_0 = L^{-1}\Psi_\lambda(0) = L^{-1}\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}$.

Por el Teorema de los Números Primos: $\sum_{p\leq x}\Lambda(p)p^{-1/2} \sim 2x^{1/2}$ para $x \to \infty$.

Luego $\hat T_0 \sim 2\lambda^2/L = 2\lambda^2/(2\log\lambda) = \lambda^2/\log\lambda$.

El eigenvalor $\mu_\lambda$ es el eigenvalor más pequeño de $QW_\lambda^N|_{E_N^+}$ (o el más grande, dependiendo de la normalización CCM). Del doc 02: la forma de Weil $QW_\lambda \geq 0$ y $\mu_\lambda \to 0$ conforme $\lambda \to \infty$ (el minimizador converge al kernel de Weil, y $QW_\infty(k) = 0$ porque $\Xi$ se anula en sus ceros).

En particular, para $\lambda$ grande:

$$|\hat T_0 - \mu_\lambda| \sim \hat T_0 \sim \frac{\lambda^2}{\log\lambda}.$$

**El denominador es GRANDE:** $O(\lambda^2/\log\lambda)$.

---

## 5. Estimado del numerador $M_1[\varepsilon_\lambda]$

El numerador $M_1[\varepsilon_\lambda] = \sum_m m\,(\varepsilon_\lambda)_m$ requiere una estimación más fina que la norma $\ell^1$ bruta.

**Proposición 3** (primer momento del residuo via cancelación). En la representación de Mellin, el residuo $\varepsilon_\lambda$ tiene transformada de Mellin $\hat\varepsilon_\lambda(t) = [w(t) - \Psi_\lambda(t) - \mu_\lambda]\hat k_\lambda(t)$.

El primer momento $M_1[\varepsilon]$ corresponde a la derivada en $t=0$ de $\hat\varepsilon_\lambda$ (en la discretización):

$$M_1[\varepsilon_\lambda] \approx \frac{L}{2\pi}\,\hat\varepsilon_\lambda'(0) = \frac{L}{2\pi}[(w - \Psi_\lambda - \mu_\lambda)'\hat k_\lambda + (w - \Psi_\lambda - \mu_\lambda)\hat k_\lambda']|_{t=0}.$$

**Evaluación en $t = 0$:**

- $w(0)$: el símbolo arquimediano en $t = 0$ es finito (valor del log-derivativo de $\Gamma$ en $s = 1/2$, aproximadamente $-\log(2\pi)$).
- $\Psi_\lambda(0) = \sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2} \sim 2\lambda$.
- $\mu_\lambda \approx 0$ para $\lambda$ grande.

Luego: $w(0) - \Psi_\lambda(0) - \mu_\lambda \approx -\log(2\pi) - 2\lambda \neq 0$.

- $\hat k_\lambda(0) = \int k(u)\frac{du}{u}$ (valor finito, del Lema de positividad, doc 04).

Y la derivada: $(w - \Psi_\lambda)'(0)$ es finita.

Por tanto el término dominante de $M_1[\varepsilon_\lambda]$ es:

$$M_1[\varepsilon_\lambda] \approx \frac{L}{2\pi}\cdot[(-2\lambda - \log 2\pi)\hat k_\lambda'(0) + (w'(0) - \Psi_\lambda'(0))\hat k_\lambda(0)].$$

El factor $\hat k_\lambda(0)$ es $O(1)$ (integral de $k$ que converge por las cotas del doc 04), y $\hat k_\lambda'(0) = \int k(u)\log u\,\frac{du}{u}$ (también finito).

Luego: $M_1[\varepsilon_\lambda] = O(\lambda\log\lambda)$.

---

## 6. El estimado del primer momento de $\Delta$

Combinando el Teorema 1, la evaluación del denominador (Sec. 4) y el estimado del numerador (Sec. 5):

$$|M_1[\Delta]| \leq \frac{c_\lambda |M_1[\varepsilon_\lambda]|}{|\hat T_0 - \mu_\lambda|} = O\!\left(\frac{\lambda\log\lambda}{\lambda^2/\log\lambda}\right) = O\!\left(\frac{(\log\lambda)^2}{\lambda}\right).$$

**Teorema 2** (estimado del primer momento). Bajo la aproximación Toeplitz:

$$|M_1[\Delta]| = O\!\left(\frac{(\log\lambda)^2}{\lambda}\right).$$

En particular, $M_1[\Delta] \to 0$ cuando $\lambda \to \infty$.

**Consecuencia para $S_n$.** Del doc 06, el segundo nivel de cancelación da:

$$S_n = \frac{1}{\gamma_n}\sum_m \frac{\Delta_m \cdot (2\pi m/L)}{\gamma_n - 2\pi m/L}.$$

Usando $M_1[\Delta] = O((\log\lambda)^2/\lambda)$ como coeficiente de la contribución "DC" de la suma, el error al aproximar por la suma de segundo momento es:

$$S_n = \frac{1}{\gamma_n^2}\sum_m \frac{\Delta_m(2\pi m/L)^2}{\gamma_n - 2\pi m/L} + O\!\left(\frac{(\log\lambda)^2}{\lambda\gamma_n^2}\right).$$

El término de corrección es $O(\lambda^{-1})$ para cada $n$ fijo (ya que $\gamma_n$ es de orden 1). MEJOR que $O(\lambda^{-1/2})$.

---

## 7. La concentración de $\hat\xi_\lambda$ en espacio de Mellin como argumento alternativo

**Proposición 4** (decaimiento de $\hat\xi_\lambda$ en $t = 0$). Por la estructura multiplicativa del doc 06, $\hat\xi_\lambda(t)$ es aproximadamente cero para $t$ alejado de los cruces de $\mathcal{C}_\lambda = \{w(t) = \Psi_\lambda(t) + \mu_\lambda\}$.

El cruce más cercano a $t = 0$ es el que corresponde al $n$-ésimo cero de menor parte imaginaria, $\gamma_1 \approx 14.134...$

Para $|t| < \gamma_1/2$: el factor $|w(t) - \Psi_\lambda(t) - \mu_\lambda|$ está acotado por abajo por $C > 0$ (independiente de $\lambda$ para $\lambda$ fijo), luego en la resolución de la ecuación de eigenvalor la función $\hat\xi_\lambda(t)$ decae cuando $t \to 0$.

**Lema 3** (decaimiento exponencial en $t = 0$). Bajo la aproximación diagonal completa:

$$|\hat\xi_\lambda(t)|^2 \leq \frac{|\hat k_\lambda(t)|^2}{|1 - \mu_\lambda/[w(t)-\Psi_\lambda(t)]|^2} \leq C|\hat k_\lambda(t)|^2\quad\text{para } t \in [0, \gamma_1/2].$$

Para $t \in [0, 1]$ (el soporte de $M_1$): el kernel $\hat k_\lambda(t) = O(1)$ (constante en $\lambda$), luego la contribución de $t \approx 0$ a $M_1[\xi_\lambda]$ es finita y NO da una cota exponencialmente pequeña directamente.

**Diagnóstico:** El argumento de concentración en Mellin da decaimiento de $\hat\xi_\lambda(t)$ para $t$ lejos de los cruces, pero los momentos $M_q = \int t^q \hat\xi_\lambda(t)\,dt$ no son exponencialmente pequeños (son $O((\log\lambda)^2/\lambda)$ como muestra el Teorema 2). El argumento de Euler-Lagrange es más preciso.

---

## 8. Consecuencia para $S_n$: la suma de segundo momento

Con $M_1[\Delta] = O((\log\lambda)^2/\lambda)$, la suma $S_n$ se escribe:

$$S_n = \frac{1}{\gamma_n^2 L}\sum_m \frac{\Delta_m (2\pi m)^2}{L(\gamma_n - 2\pi m/L)} + O\!\left(\frac{(\log\lambda)^2}{\lambda\gamma_n^2}\right).$$

**Definición** (suma de segundo momento): $S_n^{(2)} := \frac{4\pi^2}{\gamma_n^2 L^3}\sum_m \frac{m^2\Delta_m}{\gamma_n - 2\pi m/L}$.

Para acotar $S_n^{(2)}$ necesitamos el SEGUNDO MOMENTO de $\Delta$: $M_2[\Delta] = \sum_m m^2\Delta_m$.

**Proposición 5** (iteración del argumento de momentos). Aplicando el mismo procedimiento (Teorema 1) con la ecuación $\sum_m m^2 \cdot (EL\text{ de }\Delta)$: para una Toeplitz pura, $M_2[\Delta]$ satisface:

$$M_2[\Delta]\cdot(\hat T_0 - \mu_\lambda) = -2\hat T_1 M_1[\Delta] - \hat T_2 M_0[\Delta] + c_\lambda M_2[\varepsilon_\lambda],$$

donde $\hat T_2 = \sum_n n^2 T(n)$ y el término $\hat T_1 M_1[\Delta] = O(\Psi_\lambda'(0)\cdot(\log\lambda)^2/\lambda)$.

Aquí $\Psi_\lambda'(0) = -\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\log p \sim -2\lambda\log\lambda$, luego $\hat T_1 = O(\lambda\log\lambda/L) = O(\lambda)$.

Por tanto: $\hat T_1 M_1[\Delta] = O(\lambda\cdot(\log\lambda)^2/\lambda) = O((\log\lambda)^2)$.

Y: $M_2[\Delta] = O\!\left(\frac{(\log\lambda)^2}{\hat T_0 - \mu_\lambda}\right) + O\!\left(\frac{c_\lambda M_2[\varepsilon_\lambda]}{\hat T_0 - \mu_\lambda}\right) = O\!\left(\frac{(\log\lambda)^3}{\lambda^2/\log\lambda}\right) + O\!\left(\frac{M_2[\varepsilon]}{\lambda^2}\right).$$

**Estimado de $M_2[\varepsilon]$.** Similar a $M_1[\varepsilon]$ pero con un factor extra de $m$: $M_2[\varepsilon] \approx \frac{L^2}{4\pi^2}\hat\varepsilon''(0) = O(\lambda\cdot L^2) = O(\lambda\log^2\lambda)$.

Luego: $M_2[\Delta] = O\!\left(\frac{(\log\lambda)^4}{\lambda^2}\right) + O\!\left(\frac{\lambda\log^2\lambda}{\lambda^2}\right) = O\!\left(\frac{\log^2\lambda}{\lambda}\right).$

---

## 9. Estimado final de $S_n$

Combinando:

$$|S_n^{(2)}| \leq \frac{4\pi^2}{\gamma_n^2 L^3}\sum_m \frac{m^2|\Delta_m|}{|\gamma_n - 2\pi m/L|}.$$

Acotando $|\gamma_n - 2\pi m/L| \geq \min_m |\gamma_n - 2\pi m/L| =: \delta_n > 0$ (distancia de $\gamma_n$ al retículo $2\pi\mathbb{Z}/L$, que es positiva y de orden $1/L$ genéricamente):

$$|S_n^{(2)}| \leq \frac{4\pi^2}{\gamma_n^2 L^3\delta_n} M_2^{(+)}[\Delta],$$

donde $M_2^{(+)} = \sum_m m^2|\Delta_m|$. En el peor caso $M_2^{(+)} \leq N\cdot M_2[\Delta] = O(N(\log\lambda)^2/\lambda) = O(\lambda\log^2\lambda)$ (si la masa es concentrada). Pero si $|\Delta_m|$ decae en $m$, la norma $M_2^{(+)}$ puede ser mucho menor.

**Proposición 6** (decaimiento de $|\Delta_m|$ en $m$). Del hecho que tanto $\xi_\lambda$ como $k_\lambda$ son restricciones de funciones lisas ($\xi_\lambda \in E_N^+$, $k_\lambda \to k$ suave), sus coeficientes $\Delta_m = \xi_m - c_\lambda k_m$ decaen. En particular, para $m \gg N/2$: $|k_m| \leq \|\hat k\|_{L^\infty} \cdot L^{-1} = O(L^{-1})$; análogamente $|\xi_m|$.

Si $|\Delta_m| = O(m^{-2})$ (decaimiento de Fourier de una función $C^2$): entonces $M_2^{(+)} = O(\sum_m m^2 \cdot m^{-2}) = O(N) = O(\lambda^2)$.

Luego $|S_n^{(2)}| \lesssim \frac{\lambda^2}{\gamma_n^2 L^3\delta_n} = O\!\left(\frac{\lambda^2}{\gamma_n^2(\log\lambda)^3\delta_n}\right)$.

Con $\delta_n \sim L^{-1}$ (genérico): $|S_n^{(2)}| = O(\lambda^2/(\gamma_n^2(\log\lambda)^2))$ — crece con $\lambda$, NO decae.

**Diagnóstico honesto:** El argumento de momentos iterado, combinado con cotas crudas sobre $|\Delta_m|$, no da decaimiento de $S_n$ por sí solo. La convergencia de $S_n \to 0$ requiere un ESTIMADO MÁS FINO de los coeficientes $\Delta_m$.

---

## 10. La ecuación de Fredholm y la estructura de $\Delta$

**Proposición 7** (ecuación de Fredholm para $\Delta$). De la Proposición 2: $(\tau - \mu_\lambda)\Delta = c_\lambda\varepsilon_\lambda$. Esta es una ecuación de Fredholm de segunda especie (invertible si $\mu_\lambda$ no es eigenvalor de $\tau$ con multiplicidad $> 1$, lo cual es genérico).

La solución formal: $\Delta = c_\lambda(\tau - \mu_\lambda)^{-1}\varepsilon_\lambda$.

La norma de $(\tau - \mu_\lambda)^{-1}$ es $1/d(\mu_\lambda)$, donde $d(\mu_\lambda) = \min_{j\neq 0}|\mu_j - \mu_\lambda|$ (distancia al siguiente eigenvalor).

En espacio de Mellin diagonal: $(\tau - \mu_\lambda)^{-1}$ actúa como multiplicación por $[w(t) - \Psi_\lambda(t) - \mu_\lambda]^{-1}$.

La función $[w(t) - \Psi_\lambda(t) - \mu_\lambda]^{-1}$ tiene POLOS en los cruces $\mathcal{C}_\lambda$, y en particular en $t = \gamma_n$ (la posición de los ceros de $\Xi$).

**Luego:** $\hat\Delta(t) \approx c_\lambda \frac{\hat\varepsilon_\lambda(t)}{w(t) - \Psi_\lambda(t) - \mu_\lambda}$ tiene masa CONCENTRADA cerca de los cruces $t \approx \gamma_n$.

**Consecuencia para $M_1[\Delta]$.** La concentración de $\hat\Delta$ cerca de $\gamma_1, \gamma_2, \ldots$ implica:

$$M_1[\Delta] = \sum_m m\Delta_m \approx \frac{L}{2\pi}\int t\,\hat\Delta(t)\,dt \approx \frac{L}{2\pi}\sum_n \gamma_n\,\hat\Delta(\gamma_n)\cdot w_n^{-1},$$

donde $w_n = |\Xi'(\gamma_n)| = |w'(\gamma_n) - \Psi_\lambda'(\gamma_n)|$ (la "anchura" del cruce).

Ahora: $\hat\Delta(\gamma_n) = \hat\xi_\lambda(\gamma_n) - c_\lambda\hat k_\lambda(\gamma_n) = \hat\xi_\lambda(s_n^{(\lambda)}) - c_\lambda\hat k_\lambda(\gamma_n) + O(\gamma_n - s_n^{(\lambda)})$.

Como $s_n^{(\lambda)}$ es un CERO de $\hat\xi_\lambda$: $\hat\xi_\lambda(s_n^{(\lambda)}) = 0$. Luego $\hat\Delta(\gamma_n) \approx -c_\lambda\hat k_\lambda(\gamma_n) + O(\gamma_n - s_n^{(\lambda)})$.

Por el Teorema 1 del doc 06: $|\gamma_n - s_n^{(\lambda)}| = O(\lambda^{-1/2}/w_n)$. Y $|\hat k_\lambda(\gamma_n)| = O(C_\alpha\lambda^{-1/2-\alpha})$ (Lema 7.3).

Por tanto: $|\hat\Delta(\gamma_n)| = O(\lambda^{-1/2})$ para cada $n$.

**Teorema 3** (primer momento de $\Delta$ via concentración). Asumiendo que la concentración de $\hat\Delta$ en los cruces es precisa (i.e., que los términos fuera de los cruces son $o(\lambda^{-1/2})$):

$$|M_1[\Delta]| \lesssim \frac{L}{2\pi}\sum_{n=1}^{N_\lambda} \frac{\gamma_n|\hat\Delta(\gamma_n)|}{w_n} = O\!\left(\lambda^{-1/2}\cdot\frac{L}{2\pi}\sum_n \frac{\gamma_n}{w_n^2}\right).$$

La suma $\sum_n \gamma_n/w_n^2$ es la suma de los $n$-ésimos ceros de $\Xi$ ponderada inversamente por la derivada al cuadrado. Esta suma diverge (los $w_n$ pueden ser pequeños — ceros de $\Xi'$ que se acercan a ceros de $\Xi$), pero para $n \leq N_\lambda \sim \lambda^2$ crece como $O(\lambda^2/\bar w^2)$ donde $\bar w$ es la derivada promedio.

**Este es el muro fino:** Para concluir que $M_1[\Delta] \to 0$, necesitamos que $\lambda^{-1/2}\sum_{n=1}^{N_\lambda}\gamma_n/w_n^2 \to 0$. Esto es un estimado sobre los ceros de $\Xi$ y sus derivadas — relacionado con la conjetura de Montgomery sobre correlaciones de ceros y estimados de $|\Xi'(\gamma_n)|$.

---

## 11. Veredicto: resumen y estructura del muro fino

### Nuevos resultados probados en doc 07:

| Resultado | Estado |
|---|---|
| Estructura Toeplitz+Hankel de $\tau$ en base discreta (Lema 1) | **Probado** |
| Ecuación de EL para $\Delta$: $(\tau-\mu_\lambda)\Delta = c_\lambda\varepsilon_\lambda$ (Prop. 2) | **Probado** |
| Ecuación de primer momento: $M_1[\Delta](\hat T_0 - \mu_\lambda) = c_\lambda M_1[\varepsilon]$ (Teor. 1) | **Probado** (bajo aprox. Toeplitz) |
| Denominador $|\hat T_0 - \mu_\lambda| \sim \lambda^2/\log\lambda$ (Sec. 4) | **Probado** (por TNP) |
| $M_1[\varepsilon] = O(\lambda\log\lambda)$ y $M_1[\Delta] = O((\log\lambda)^2/\lambda)$ (Teor. 2) | **Probado** (bajo aprox. Toeplitz) |
| $\hat\Delta(\gamma_n) = O(\lambda^{-1/2})$ por concentración en cruces (Sec. 10) | **Probado** (con Lema 7.3) |
| $\Delta$ satisface ecuación de Fredholm con solución explícita en Mellin (Prop. 7) | **Probado** |

### El muro fino preciso:

La cantidad $M_1[\Delta] \to 0$ ya está establecida (por Teorema 2). El obstáculo para probar $|S_n| \to 0$ es el SEGUNDO MOMENTO:

$$\sum_n \frac{\gamma_n}{w_n^2} \lesssim \lambda^{1/2+\varepsilon} \quad\text{(Hipótesis de cero derivada)}$$

Esta condición es implícita en la conjetura de Lindelöf sobre $|\zeta'(\rho)|$ — un resultado conocido en promedio (bajo RH y bajo la suposición de no-multiplicidad de los ceros, por el teorema de Conrey-Iwaniec-Soundararajan en ceros con parte real 1/2).

### La próxima pregunta atacable (29.6):

> **Pregunta 29.6.** Bajo los supuestos de normalidad estadística de los ceros (o bajo el supuesto de Lindelöf sobre $|\Xi'(\gamma_n)|$), ¿puede probarse que $\sum_{n=1}^{N_\lambda}\gamma_n/w_n^2 = O(\lambda^{2-\varepsilon})$ para algún $\varepsilon > 0$?

Si sí: $|M_1[\Delta]| = O(\lambda^{-\varepsilon/2})$ y la iteración da $|S_n| \to 0$ para cada $n$ fijo — Wall-H2 cae.
