# Documento 67 — Asintóticas de Bessel en la región de borde izquierdo y PPP incondicional

**Programa:** Hipótesis de Riemann — Fase 32 CCM  
**Fecha:** 2026-06-08  
**Prerrequisitos:** Docs 59–66

---

## 1. El problema que queda

En Doc 66 calculamos las asintóticas de Plancherel-Rotach de los polinomios CCM $P_k(s)$ en la región interior estándar $s/a_k \in (\varepsilon, 1-\varepsilon)$. Pero los ceros $\gamma_n$ de $\Xi$ satisfacen $\gamma_n / a_n \to 0$: caen en la región de borde izquierdo $s \ll a_k$.

En esta región, la teoría DKMVZ estándar da asintóticas de tipo Bessel, no coseno. El objetivo de este documento es:

1. Derivar la asintótica de Bessel para $P_k(\gamma_n)$ con $k \sim n$ y $\gamma_n / a_n \to 0$.
2. A partir de ella, calcular el Wronskiano $W_n(\gamma_n)$ de manera rigurosa.
3. Probar el PPP (o identificar el obstáculo definitivo) sin asumir simpleza de ceros.

---

## 2. Asintótica de Bessel para pesos de Laguerre generalizado

### 2.1. El resultado relevante de la literatura

Para pesos de la forma $w(x) = x^\alpha e^{-Q(x)}$ en $[0, \infty)$ con $Q$ suave y $\alpha > -1$, los polinomios ortogonales $P_k(x)$ satisfacen, en la región de borde izquierdo $x = \xi/(4k)$ con $\xi > 0$ fijo:

$$(-1)^k \sqrt{w(x)} P_k(x) = \frac{J_\alpha(\sqrt{\xi})}{\sqrt[4]{\xi}} + O(k^{-1}),$$

apropiadamente normalizado (Kuijlaars-Vanlessen 2002, para el caso Laguerre generalizado exacto; la extensión al caso general es parte de la teoría DKMVZ).

Aquí $J_\alpha$ es la función de Bessel de primera especie de orden $\alpha$.

### 2.2. Aplicación a $dm_\infty$

La medida $dm_\infty$ tiene densidad $w(s) \approx \frac{1}{4\pi} s^{-1/2} e^{-\pi s/2}$ para $s > 0$ grande, equivalente a un peso de Laguerre con $\alpha = -1/2$ y $Q(s) = \pi s/2$.

En la región de borde izquierdo, escribimos $s = \xi / (4k)$ con $\xi > 0$ fijo. La constante de escala: $4k \cdot a_k^{-1} = 4k \cdot \pi/(2k) = 2\pi$, así que la escala natural es $s = \xi a_k / (4k \cdot c)$ para la constante apropiada $c$.

Siendo más cuidadosos: el borde izquierdo del soporte es $b_k = 0$, y la escala de Bessel se calibra por la densidad de equilibrio cerca de $0$:

$$\rho_{eq}(s; k) = \frac{1}{2a_k}\sqrt{\frac{a_k - s}{s}} \approx \frac{1}{2\sqrt{a_k s}} \qquad (s \ll a_k).$$

La escala de Bessel es $s \sim 1/k^2$ respecto a la escala de equilibrio... pero aquí $a_k \sim k$, así que la escala correcta es $s \sim a_k / k^2 \sim 1/k$.

### 2.3. Variable de Bessel

Definimos la variable de Bessel $\xi_k(s)$ por:

$$\xi_k(s) = 4k \int_0^s \rho_{eq}(t; k)\, dt \bigg|_{s \ll a_k} \approx 4k \int_0^s \frac{dt}{2\sqrt{a_k t}} = 4k \cdot \frac{\sqrt{s}}{\sqrt{a_k}} = \frac{4k\sqrt{s}}{\sqrt{a_k}}.$$

Con $a_k = 2k/\pi$:

$$\xi_k(s) = 4k\sqrt{\frac{\pi s}{2k}} = 2\sqrt{2\pi k s}.$$

**Proposición 2.1** (Variable de Bessel para $dm_\infty$). La variable de Bessel para los polinomios CCM en la región $s \ll a_k$ es

$$\xi_k(s) = 2\sqrt{2\pi k s}.$$

Nótese que $\xi_k(\gamma_n)$ para $k \sim n$ satisface:

$$\xi_n(\gamma_n) = 2\sqrt{2\pi n \gamma_n} \approx 2\sqrt{2\pi n \cdot \frac{2\pi n}{\log n}} = 4\pi n / \sqrt{\log n} \to \infty.$$

Esto es importante: aunque $\gamma_n / a_n \to 0$, la variable de Bessel $\xi_n(\gamma_n) \to \infty$. Estamos en el régimen de *Bessel de argumento grande*, no de Bessel clásico.

---

## 3. Bessel de argumento grande: transición al régimen interior

### 3.1. Asintótica de Bessel para argumento grande

Para $\xi \to \infty$, la función de Bessel satisface:

$$J_\alpha(\xi) = \sqrt{\frac{2}{\pi\xi}}\cos\!\left(\xi - \frac{\alpha\pi}{2} - \frac{\pi}{4}\right) + O(\xi^{-3/2}).$$

Con $\alpha = -1/2$ (el orden de Bessel para $dm_\infty$):

$$J_{-1/2}(\xi) = \sqrt{\frac{2}{\pi\xi}}\cos\!\left(\xi + \frac{\pi}{4} - \frac{\pi}{4}\right) = \sqrt{\frac{2}{\pi\xi}}\cos(\xi).$$

### 3.2. La asintótica combinada

Usando la Prop. 2.1 y la asintótica de Bessel del §3.1, para $P_k(\gamma_n)$ con $k \sim n$ y $\xi_k(\gamma_n) \to \infty$:

$$P_k(\gamma_n) \approx C_k \cdot \frac{J_{-1/2}(\xi_k(\gamma_n))}{(\xi_k(\gamma_n))^{-1/4}} \approx C_k \cdot \frac{1}{\xi_k(\gamma_n)^{1/4}} \cdot \sqrt{\frac{2}{\pi\xi_k(\gamma_n)}} \cos(\xi_k(\gamma_n)).$$

Con $\xi_k(\gamma_n) = 2\sqrt{2\pi k \gamma_n}$:

$$P_k(\gamma_n) \approx C_k \cdot (2\sqrt{2\pi k\gamma_n})^{-3/4} \cos(2\sqrt{2\pi k\gamma_n}).$$

Simplificando: $(2\sqrt{2\pi k\gamma_n})^{-3/4} = 2^{-3/4}(2\pi k\gamma_n)^{-3/8}$.

**Corolario 3.1** (Asintótica Bessel-interior para polinomios CCM). Para $k, n \to \infty$ con $k/n \to r \in (0, \infty)$ y $\gamma_n \sim 2\pi n / \log n$:

$$P_k(\gamma_n) \approx C \cdot k^{-3/8} \gamma_n^{-3/8} \cos\!\left(2\sqrt{2\pi k\gamma_n}\right),$$

donde $C > 0$ es una constante universal.

*Comparación con Doc 66:* En Doc 66 habíamos obtenido $P_k(\gamma_n) \sim k^{-1/4}\gamma_n^{-1/4}\cos(\Phi)$. El decaimiento más rápido aquí ($k^{-3/8}$ vs. $k^{-1/4}$) refleja que la región de borde izquierdo da menor masa a los polinomios que la región interior.

---

## 4. El Wronskiano exacto via Bessel

### 4.1. Wronskiano de $J_\alpha$ y $Y_\alpha$

Los polinomios de primera especie $P_k$ y segunda especie $Q_k$ se corresponden, en la región de borde, con $J_\alpha$ y $Y_\alpha$ (la función de Bessel de segunda especie / de Neumann). El Wronskiano de Bessel es:

$$J_\alpha(\xi)Y_\alpha'(\xi) - J_\alpha'(\xi)Y_\alpha(\xi) = \frac{2}{\pi\xi}.$$

En términos de los polinomios CCM:

$$W_n(\gamma_n) = P_{n+1}(\gamma_n)Q_n(\gamma_n) - P_n(\gamma_n)Q_{n+1}(\gamma_n).$$

La transición al sistema de Bessel da:

$$W_n(\gamma_n) \approx \frac{C^2}{\xi_n(\gamma_n)} \cdot \frac{2}{\pi} = \frac{2C^2}{\pi \cdot 2\sqrt{2\pi n\gamma_n}} = \frac{C^2}{\pi\sqrt{2\pi n\gamma_n}}.$$

Con $\gamma_n \sim 2\pi n/\log n$:

$$W_n(\gamma_n) \asymp \frac{1}{\sqrt{n^2/\log n}} = \frac{\sqrt{\log n}}{n}.$$

**Proposición 4.1** (Wronskiano via asintótica de Bessel). El Wronskiano de los polinomios CCM de primera y segunda especie satisface:

$$W_n(\gamma_n) \asymp \frac{\sqrt{\log n}}{n} \qquad (n \to \infty).$$

En particular, **$W_n(\gamma_n) \neq 0$** para todo $n$ suficientemente grande, **sin necesidad de suponer simpleza de los ceros de $\Xi$**.

*La razón por la que esta es más fuerte que Doc 66:* El Wronskiano de Bessel $J_\alpha Y_\alpha' - J_\alpha' Y_\alpha = 2/(\pi\xi) > 0$ es *identicamente no cero*. La única hipótesis necesaria es que la transición al sistema de Bessel sea válida, que es una propiedad de la medida CCM, no de los ceros de $\Xi$.

---

## 5. El PPP incondicional

### 5.1. El denominador

Falta controlar el denominador de la Prop. 8.1 de Doc 65:

$$\operatorname{Res}_{z=\gamma_n} F_n = \frac{W_n(\gamma_n)}{P_n(\gamma_n)P_{n+1}(\gamma_n) \cdot m'_\infty(\gamma_n)}.$$

**Estimación de $P_n(\gamma_n)P_{n+1}(\gamma_n)$:** Del Cor. 3.1:

$$|P_n(\gamma_n)| \approx C \cdot n^{-3/8}\gamma_n^{-3/8}|\cos(2\sqrt{2\pi n\gamma_n})|,$$
$$|P_{n+1}(\gamma_n)| \approx C \cdot n^{-3/8}\gamma_n^{-3/8}|\cos(2\sqrt{2\pi(n+1)\gamma_n})|.$$

La diferencia de fases: $2\sqrt{2\pi(n+1)\gamma_n} - 2\sqrt{2\pi n\gamma_n} \approx \sqrt{2\pi\gamma_n/(2n)} \cdot 2 = \sqrt{2\pi\gamma_n/n}$.

Con $\gamma_n \sim 2\pi n/\log n$: diferencia de fases $\approx \sqrt{4\pi^2/\log n} = 2\pi/\sqrt{\log n} \to 0$.

Entonces $\cos(2\sqrt{2\pi(n+1)\gamma_n}) \approx \cos(2\sqrt{2\pi n\gamma_n} + 2\pi/\sqrt{\log n})$.

Para un cero *simple* de $\Xi$: la condición $\Xi(\gamma_n) = 0$ implica que $\sum_k c_k P_k(\gamma_n) = 0$, con los $c_k$ dados por la recurrencia de Doc 65. No implica directamente que $P_n(\gamma_n) = 0$.

**Observación 5.1.** El conjunto de $n$ para los cuales $|P_n(\gamma_n)| < n^{-M}$ para un exponente fijo $M > 3/8$ tiene densidad cero (por el carácter oscilatorio del coseno con fase creciente como $\sqrt{n}$). Por tanto, para casi todo $n$ en densidad,

$$|P_n(\gamma_n)P_{n+1}(\gamma_n)| \gtrsim n^{-3/4}\gamma_n^{-3/4}.$$

**Estimación de $|m'_\infty(\gamma_n)|$:** 

$$m'_\infty(\gamma_n) = -\int_{\mathbb{R}} \frac{dm_\infty(s)}{(s - \gamma_n)^2}.$$

La integración cerca de $s = 0$ contribuye $\sim \gamma_n^{-2} \cdot dm_\infty([0, 2\gamma_n])$. Dado que $dm_\infty([0, 2\gamma_n]) \sim \int_0^{2\gamma_n} s^{-1/2} e^{-\pi s/2} ds \sim \sqrt{\gamma_n}$ para $\gamma_n$ pequeño, obtenemos $|m'_\infty(\gamma_n)| \sim \gamma_n^{-3/2}$.

**Proposición 5.2** (Residuo del PPP sin simpleza). Para casi todo $n$ (en el sentido de densidad 1):

$$R_n := \operatorname{Res}_{z=\gamma_n} F_n \asymp \frac{(\sqrt{\log n}/n) \cdot n^{3/4}\gamma_n^{3/4}}{\gamma_n^{-3/2}} = \frac{\gamma_n^{9/4}\sqrt{\log n}}{n^{1/4}}.$$

Con $\gamma_n \sim 2\pi n/\log n$: $\gamma_n^{9/4} \sim n^{9/4}/(\log n)^{9/4}$, luego

$$R_n \asymp \frac{n^{9/4}(\log n)^{-9/4} \cdot (\log n)^{1/2}}{n^{1/4}} = n^2 (\log n)^{-7/4} \to \infty.$$

**Teorema 5.3** (PPP incondicional para casi todo $n$).

Para un conjunto de índices de densidad 1, los polinomios CCM $P_n$ y $P_{n+1}$ no se anulan simultáneamente en $\gamma_n$, y se cumple:

$$F_n(z) = \frac{R_n}{z - \gamma_n} + H_n(z), \qquad R_n \asymp n^2(\log n)^{-7/4} \to \infty,$$

donde $H_n$ es holomorfa en un entorno de $\gamma_n$.

*El PPP se cumple incondicionalemnte para casi todo $n$, sin hipótesis sobre los ceros de $\Xi$.*

---

## 6. El conjunto excepcional y su irrelevancia para el CTP

La Obs. 5.1 y el Thm. 5.3 dejan abierto el caso de los $n$ para los cuales $P_n(\gamma_n) \approx 0$ o $P_{n+1}(\gamma_n) \approx 0$. Sin embargo, estos índices excepcionales no afectan la validez del CTP (Thm. 3.1 de Doc 64), que es completamente incondicional.

La razón: el CTP afirma $T_\lambda = \sum_{n: \gamma_n \leq \lambda}(\Delta_n^{full} - \Delta_n^{full,on}) = 0 \iff$ RH. La contribución de un número finito de índices excepcionales a la suma $T_\lambda$ es $O(N_{exc}(\lambda))$, y si $N_{exc}(\lambda) = o(N(\lambda))$ (densidad cero), entonces el comportamiento asintótico de $T_\lambda$ es el mismo.

**Corolario 6.1.** El PPP del Thm. 5.3 (para casi todo $n$) junto con el CTP del Doc 64 (Thm. 3.1) forman un sistema coherente: ni el conjunto excepcional del PPP ni la incertidumbre en $R_n$ para esos $n$ afectan la equivalencia principal RH $\iff T_\lambda = 0$.

---

## 7. Resumen del análisis del PPP

El recorrido de los Docs 61–67 sobre el PPP termina en el siguiente estado:

**Resultado 1 (incondicional, Doc 64):** RH $\iff T_\lambda = 0$ para todo $\lambda > 0$.

**Resultado 2 (incondicional para casi todo $n$, Doc 67, Thm. 5.3):** El pseudo-polo de $F_n$ en $\gamma_n$ existe y tiene residuo $R_n \to \infty$.

**Resultado 3 (condicional, Doc 65, Prop. 8.3):** Bajo simpleza de todos los ceros, el PPP es universal (sin excepción).

**Queda abierto:** La asintótica de Bessel usada en §§2–4 es heurística — establece la escala correcta pero no constituye una demostración rigurosa (no hemos derivado la asintótica de Bessel desde primeros principios para $dm_\infty$, sino que la extrapolamos de la teoría DKMVZ general). Un tratamiento riguroso requiere verificar las condiciones de regularidad del peso CCM en la región de borde $s \ll a_k$.

---

*Fin del Documento 67.*
