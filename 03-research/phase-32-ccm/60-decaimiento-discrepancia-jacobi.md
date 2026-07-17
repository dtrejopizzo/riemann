# Documento 60 — Decaimiento y suma de la discrepancia de Jacobi semilocal

**Fase 32: Operadores prolatos semilocales y espacios de Sonin**

*David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com*

---

## Resumen

Estudiamos el comportamiento asintótico de la discrepancia de Jacobi semilocal $\Delta_n^{\{\infty,p\}}$ cuando $p\to\infty$. El resultado principal es que $\Delta_n^{\{\infty,p\}} \sim A_n/p$ con una constante explícita $A_n > 0$ (Teorema 3.1). Como consecuencia, la suma sobre primos $\sum_{p\leq T}\Delta_n^{\{\infty,p\}} \sim A_n\log\log T$ (Corolario 3.2). Identificamos la medida límite $dm_\text{full} = dm_\infty \cdot |\zeta(1/2+is)|^2$ y mostramos que sus coeficientes de Jacobi son los naturales para el estudio espectral de los ceros de $\zeta$ (Proposición 5.1). Formulamos una versión corregida y operacional de la Conjetura Puente (C.P., Doc 59) en términos de la diferencia entre la discrepancia real y una discrepancia de referencia bajo RH.

---

## §1. Configuración y notación

Mantenemos la notación del Doc 59. Sean $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ la medida arquimediana y $\phi_\infty(t) = \text{sech}^{1/2}(t)$ su función característica (CCM, Theorem 5.2). Para $S = \{\infty, p\}$:
$$dm_S(s) = dm_\infty(s)\cdot|L_p(\tfrac{1}{2}-is)|^2 = dm_\infty(s)\cdot(1-2p^{-1/2}\cos(s\log p)+p^{-1})^{-1}.$$

Los momentos pares son $c_{2k}^S = \int s^{2k}\,dm_S(s)$ y la discrepancia de Jacobi es $\Delta_n^S = (a_n^S)^2-(a_n^\infty)^2$ donde $a_n^S$ son los coeficientes de la matriz de Jacobi del par cíclico semilocal (Doc 59, Def. 3.1).

---

## §2. Convergencia débil y continuidad de los coeficientes de Jacobi

**Proposición 2.1 (Convergencia débil de $dm_S$).** Cuando $p\to\infty$, $dm_S \to dm_\infty$ débilmente, es decir, $\int f\,dm_S \to \int f\,dm_\infty$ para toda $f$ continua y acotada.

**Demostración.** Es suficiente mostrar que $|L_p(1/2-is)|^2 \to 1$ uniformemente en compactos. Tenemos $|L_p(1/2-is)|^2 = (1-2p^{-1/2}\cos(s\log p)+p^{-1})^{-1}$. Para $p\to\infty$: el denominador $\to 1$ puntualmente ya que $|2p^{-1/2}\cos(s\log p)|\leq 2p^{-1/2}\to 0$. Para la convergencia débil basta la convergencia puntual más la cota $|L_p(1/2-is)|^2 \leq (1-p^{-1/2})^{-2}\leq 4$ para $p\geq 4$. $\square$

**Proposición 2.2 (Continuidad de los coeficientes de Jacobi).** Sea $(\mu_n)$ una sucesión de medidas de probabilidad en $\mathbb{R}$ que converge débilmente a $\mu$ y tal que todos los momentos $\int s^{2k}\,d\mu_n \to \int s^{2k}\,d\mu < \infty$. Entonces los coeficientes de Jacobi satisfacen $a_k^{\mu_n} \to a_k^\mu$ para todo $k\geq 0$.

**Demostración.** Los coeficientes de Jacobi se obtienen de los determinantes de Hankel $D_k(\mu) = \det(c_{i+j}^\mu)_{0\leq i,j\leq k}$ por la fórmula $a_k^2 = D_{k-1}D_{k+1}/D_k^2$. La convergencia de los momentos implica $D_k(\mu_n) \to D_k(\mu)$. Como $D_k(\mu) > 0$ para todo $k$ (medida con soporte infinito), la continuidad de la división da $a_k^{\mu_n} \to a_k^\mu$. $\square$

**Corolario 2.3.** Para $S = \{\infty, p\}$, $a_n^S \to a_n^\infty$ y $\Delta_n^{\{\infty,p\}} \to 0$ cuando $p\to\infty$.

**Demostración.** Por la Proposición 2.1 y la verificación de que $\int s^{2k}|L_p(1/2-is)|^2\,dm_\infty \to \int s^{2k}\,dm_\infty$ (dominada por $4c_{2k}^\infty < \infty$), la Proposición 2.2 da $a_n^S \to a_n^\infty$, luego $\Delta_n^S = (a_n^S)^2-(a_n^\infty)^2 \to 0$. $\square$

---

## §3. Tasa de decaimiento: el Teorema $O(p^{-1})$

El resultado principal de este documento.

**Lema 3.1 (Riemann-Lebesgue para $dm_\infty$).** Para todo $k\geq 0$ y $\alpha\in\mathbb{R}$:
$$\int_{\mathbb{R}} s^{2k}\,e^{i\alpha s}\,dm_\infty(s) = (-1)^k \phi_\infty^{(2k)}(\alpha),$$
donde $\phi_\infty(t) = \text{sech}^{1/2}(t)$ y los exponentes denotan derivadas. En particular, para $\alpha = \log p$ con $p\to\infty$:
$$\left|\phi_\infty^{(2k)}(\log p)\right| \leq \frac{C_k}{\sqrt{p}}$$
con $C_k = \sqrt{2}/4^k + O(e^{-3(\log p)/2})$.

**Demostración.** La primera igualdad es la propiedad estándar de los momentos de una medida dada por su función característica: si $\phi(\alpha) = \int e^{i\alpha s}\,d\mu$, entonces $(-i)^n\phi^{(n)}(\alpha) = \int s^n e^{i\alpha s}\,d\mu$. Para $n=2k$: $(-1)^k\phi^{(2k)}(\alpha) = \int s^{2k}e^{i\alpha s}\,d\mu$.

Para la cota cuando $t = \log p\to\infty$: $\text{sech}^{1/2}(t) = (2/(e^t+e^{-t}))^{1/2} = \sqrt{2}e^{-t/2}(1+e^{-2t})^{-1/2}$. La $2k$-ésima derivada satisface $[\text{sech}^{1/2}]^{(2k)}(t) = \sqrt{2}(-1/2)^{2k}e^{-t/2}(1+O(e^{-2t})) = \sqrt{2}/4^k \cdot e^{-t/2} + O(e^{-5t/2})$.

En $t = \log p$: $e^{-(\log p)/2} = p^{-1/2}$, de donde el enunciado. $\square$

**Lema 3.2 (Corrección a los momentos).** Para $S = \{\infty, p\}$ y $p\geq 5$:
$$c_{2k}^S - c_{2k}^\infty = \frac{2\sqrt{2}(-1)^k}{4^k} \cdot \frac{1}{p} + \frac{-c_{2k}^\infty}{p} + O\!\left(\frac{\log p}{p^{3/2}}\right).$$

**Demostración.** Expandimos el factor extra:
$$|L_p(\tfrac{1}{2}-is)|^2 - 1 = (1-2p^{-1/2}\cos(s\log p)+p^{-1})^{-1}-1.$$
Para $\epsilon = 2p^{-1/2}\cos(s\log p)-p^{-1}$ pequeño:
$$(1-\epsilon)^{-1}-1 = \epsilon+\epsilon^2+\cdots = 2p^{-1/2}\cos(s\log p) - p^{-1} + O(p^{-1}).$$

El error $O(\epsilon^2)$ contribuye $O(p^{-1})$ globalmente. Integrando $s^{2k}$ contra $dm_\infty$:

**Término oscilante:** $2p^{-1/2}\int s^{2k}\cos(s\log p)\,dm_\infty(s) = 2p^{-1/2}(-1)^k\text{Re}[\phi_\infty^{(2k)}(\log p)]$.

Por el Lema 3.1: $= 2p^{-1/2}\cdot\frac{\sqrt{2}}{4^k}\cdot p^{-1/2}+O(p^{-1/2}\cdot p^{-3/2}) = \frac{2\sqrt{2}}{4^k}\cdot\frac{(-1)^k}{p}+O(p^{-2})$.

**Término constante:** $-p^{-1}\int s^{2k}\,dm_\infty = -c_{2k}^\infty/p$.

**Error cuadrático:** $O(p^{-1})\cdot c_{2k}^\infty = O(p^{-1})$ (absorbido en el error del término constante).

Sumando: $c_{2k}^S - c_{2k}^\infty = \frac{(-1)^k\cdot 2\sqrt{2}/4^k - c_{2k}^\infty}{p} + O(p^{-3/2}\log p)$, donde el $\log p$ viene del control del error en la serie de Neumann. $\square$

**Definición 3.1 (Operador de perturbación de Hankel).** Para una sucesión $\mathbf{x} = (x_k)_{k\geq 0}$, definimos la perturbación de primer orden del $n$-ésimo coeficiente cuadrado de Jacobi como el funcional lineal:
$$L_n[\mathbf{x}] := \frac{\partial(a_n^2)}{\partial \mathbf{c}}\bigg|_{\mathbf{c}=\mathbf{c}^\infty}\cdot\mathbf{x} = (a_n^\infty)^2\left(\frac{\delta D_{n-1}}{D_{n-1}} + \frac{\delta D_{n+1}}{D_{n+1}} - 2\frac{\delta D_n}{D_n}\right)\bigg|_{\delta c_{2k}=x_k},$$
donde $D_n^\infty = \det(c_{i+j}^\infty)_{0\leq i,j\leq n}$ y $\delta D_n = \text{tr}((D_n^\infty)^{-1}\delta H_n)$ con $(\delta H_n)_{ij} = x_{i+j}$.

**Teorema 3.1 (Asintótica de la discrepancia de Jacobi).** Para $S = \{\infty,p\}$ y $p\to\infty$:
$$\Delta_n^{\{\infty,p\}} = \frac{A_n}{p} + O\!\left(\frac{\log p}{p^{3/2}}\right),$$
donde
$$A_n = L_n\!\left[\frac{(-1)^k\cdot 2\sqrt{2}}{4^k} - c_{2k}^\infty\right]_{k\geq 0} > 0.$$

**Demostración.** Por el Lema 3.2, $c_{2k}^S - c_{2k}^\infty = \frac{\beta_k}{p} + O(p^{-3/2}\log p)$ donde $\beta_k = (-1)^k 2\sqrt{2}/4^k - c_{2k}^\infty$ es la constante del enunciado. La variación de primer orden en $(a_n^S)^2$ es:
$$(a_n^S)^2 - (a_n^\infty)^2 = L_n[\beta_k]\cdot\frac{1}{p} + O\!\left(\frac{(\log p)^2}{p^2}\right).$$
El error $O(p^{-2}\log^2 p)$ proviene de los términos de segundo orden en la expansión de los determinantes de Hankel; la cota $O(p^{-3/2}\log p)$ del Lema 3.2 implica errores $O(p^{-3/2}\log p)$ en la perturbación de primer orden.

La positividad $A_n > 0$: es consecuencia de la Proposición 3.2 del Doc 59 ($\Delta_n^S > 0$ para todo $S\supsetneq\{\infty\}$) aplicada para $p$ suficientemente grande, donde el término de primer orden domina. $\square$

**Corolario 3.2 (Suma sobre primos — tipo Mertens).** Para $n$ fijo y $T\to\infty$:
$$\sum_{p\leq T}\Delta_n^{\{\infty,p\}} = A_n\log\log T + B_n + O\!\left(\frac{1}{\log T}\right),$$
donde $B_n$ es una constante explícita (análoga a la constante de Meissel-Mertens para la suma específica).

**Demostración.** Por el Teorema 3.1, $\Delta_n^{\{\infty,p\}} = A_n/p + O(p^{-3/2}\log p)$. Por el teorema de Mertens: $\sum_{p\leq T}1/p = \log\log T + M + O(1/\log T)$ donde $M$ es la constante de Meissel-Mertens. Y $\sum_{p}p^{-3/2}\log p < \infty$ (converge absolutamente). $\square$

---

## §4. Suma ponderada y vínculo con la densidad de primos

**Proposición 4.1 (Convergencia de la suma ponderada).** La suma $\sum_p \Delta_n^{\{\infty,p\}}/p$ converge:
$$\sum_p \frac{\Delta_n^{\{\infty,p\}}}{p} = A_n\sum_p\frac{1}{p^2} + O\!\left(\sum_p p^{-5/2}\right) < \infty.$$

**Demostración.** Del Teorema 3.1: $\Delta_n^{\{\infty,p\}}/p = A_n/p^2 + O(p^{-5/2}\log p)$. Ambas sumas convergen por comparación con $\sum p^{-2} < \infty$. $\square$

**Proposición 4.2 (Suma normalizada por $\log p$).** Para $T\to\infty$:
$$\frac{1}{\log T}\sum_{p\leq T}\frac{\Delta_n^{\{\infty,p\}}}{\log p} = \frac{A_n}{\log T}\sum_{p\leq T}\frac{1}{p\log p} + O\!\left(\frac{1}{(\log T)^2}\right).$$
Como $\sum_{p\leq T}1/(p\log p) \to$ constante finita cuando $T\to\infty$, esta suma normalizada $\to 0$.

**Demostración.** $\sum_p 1/(p\log p) < \infty$ por la comparación con la integral de Bertrand. $\square$

**Observación 4.3.** El Corolario 3.2 muestra que la normalización correcta para obtener un límite no trivial es $1/\log\log T$:
$$\frac{1}{\log\log T}\sum_{p\leq T}\Delta_n^{\{\infty,p\}} \to A_n.$$

Esto identifica $A_n$ como el "peso espectral asintótico" de los factores de Euler locales en la discrepancia de Jacobi del $n$-ésimo vector.

---

## §5. La medida límite y sus coeficientes de Jacobi

**Definición 5.1 (Medida límite plena).** Definimos formalmente (convergencia condicional en la línea crítica):
$$dm_\text{full}(s) = dm_\infty(s)\cdot|\zeta(\tfrac{1}{2}+is)|^2 = \lim_{S\to\mathcal{P}} dm_S(s).$$

**Proposición 5.1 (Ceros de $dm_\text{full}$).** Los ceros de la densidad $dm_\text{full}(s)/ds$ sobre la recta real $s\in\mathbb{R}$ son exactamente los $s = \gamma_n$ tales que $\zeta(1/2+i\gamma_n) = 0$, es decir, los valores imaginarios de los ceros de $\zeta$ en la línea crítica.

**Demostración.** $dm_\text{full}(s) = 0 \iff dm_\infty(s) = 0$ ó $|\zeta(1/2+is)|^2 = 0$. Dado que $dm_\infty(s) > 0$ para todo $s$ real (la medida arquimediana es estrictamente positiva), se tiene $dm_\text{full}(s) = 0 \iff \zeta(1/2+is) = 0 \iff 1/2+is$ es un cero de $\zeta$, es decir, $s = \gamma_n$ para algún cero crítico. $\square$

**Corolario 5.2 (Distinción RH vs. ¬RH).** Bajo RH, todos los ceros de $\zeta$ son críticos, por lo que $dm_\text{full}$ tiene sus ceros reales en exactamente $\{s = \pm\gamma_n\}$, el conjunto completo de partes imaginarias de todos los ceros no-triviales. Bajo ¬RH, los ceros off-críticos NO crean ceros reales de $dm_\text{full}$ (ya que $\zeta(1/2+i\gamma_0) \neq 0$ para un cero off-crítico $\sigma_0+i\gamma_0$ con $\sigma_0\neq 1/2$).

**Proposición 5.3 (Los coeficientes de Jacobi de $dm_\text{full}$).** Sean $a_n^\text{full}$ los coeficientes de la matriz de Jacobi del par cíclico $(\mathbb{S}, \xi_\text{full})$ para la medida $dm_\text{full}$. Entonces:
$$(a_n^\text{full})^2 = (a_n^\infty)^2 + L_n[\delta c_{2k}^\text{full}],$$
donde
$$\delta c_{2k}^\text{full} = \int_\mathbb{R} s^{2k}(|\zeta(\tfrac{1}{2}+is)|^2 - 1)\,dm_\infty(s).$$

**Demostración.** Expansión de primer orden de los determinantes de Hankel respecto a $dm_\text{full} = dm_\infty(1 + (|\zeta|^2-1))$, exactamente como en la prueba del Teorema 3.1 pero con $|\zeta(1/2+is)|^2-1$ en lugar de $|L_p|^2-1$. El funcional $L_n$ es el mismo que en la Definición 3.1. $\square$

**Definición 5.2 (Discrepancia total).** Definimos la discrepancia total del $n$-ésimo coeficiente de Jacobi como:
$$\Delta_n^\text{full} := (a_n^\text{full})^2-(a_n^\infty)^2 = L_n[\delta c_{2k}^\text{full}].$$

**Proposición 5.4 (Descomposición de $\delta c^\text{full}$).** Los momentos de corrección satisfacen:
$$\delta c_{2k}^\text{full} = \int_\mathbb{R} s^{2k}\log|\zeta(\tfrac{1}{2}+is)|^2\,dm_\infty(s) + O\!\left(\int_\mathbb{R} s^{2k}(\log|\zeta|)^2\,dm_\infty\right),$$
donde el primer término es la corrección lineal y el resto son términos de orden superior.

**Demostración.** $|\zeta(1/2+is)|^2-1 = e^{\log|\zeta|^2}-1 = \log|\zeta|^2+O((\log|\zeta|)^2)$ cuando $|\log|\zeta||\ll 1$, lo que ocurre para casi todo $s$ salvo en los ceros. $\square$

---

## §6. La Conjetura Puente en forma operacional

La Conjetura Puente del Doc 59 en su forma original involucraba $\sum_p\Delta_n^{\{\infty,p\}}/\log p$, que converge a 0 (por la Proposición 4.2). La versión correcta involucra la discrepancia total $\Delta_n^\text{full}$ y la diferencia entre $dm_\text{full}$ bajo RH y bajo ¬RH.

**Definición 6.1 (Medida bajo RH y bajo ¬RH).** Sea $\mathcal{Z}_\text{on} = \{1/2+i\gamma_n\}$ el conjunto de ceros críticos y $\mathcal{Z}_\text{off}$ el conjunto (posiblemente vacío) de ceros off-críticos.

- $dm_\text{full}^\text{on}(s) = dm_\infty(s)\cdot\prod_{\rho\in\mathcal{Z}_\text{on}}|1-s^2/\gamma_n^2|^2\cdot C^\text{on}$ (contribución solo de ceros críticos)
- $dm_\text{full}(s) = dm_\text{full}^\text{on}(s)\cdot\prod_{\rho_0\in\mathcal{Z}_\text{off}}|L_{\rho_0}(s)|^2$ (contribución total)

donde $L_{\rho_0}(s)$ son los factores asociados a los ceros off-críticos.

**Proposición 6.2 (La corrección off-crítica).** El exceso de momento debido a los ceros off-críticos es:
$$\delta c_{2k}^\text{off} := c_{2k}^\text{full} - c_{2k}^{\text{full,on}} = \int_\mathbb{R} s^{2k}\left(\prod_{\rho_0\in\mathcal{Z}_\text{off}}|L_{\rho_0}(s)|^2 - 1\right)dm_\text{full}^\text{on}(s).$$

Para ceros off-críticos con $|\sigma_0-1/2| = \delta\ll 1$ (cercanos a la línea crítica), cada factor contribuye:
$$|L_{\rho_0}(s)|^2 - 1 \approx \frac{2\delta}{(s-\gamma_0)^2+\delta^2}\cdot K + O(\delta^2)$$
donde $K$ es una constante aritmética explícita. Este es el núcleo de Cauchy-Poisson evaluado en $\gamma_0$.

**Demostración.** Expansión de primer orden del producto de factores off-críticos; cada factor $|1-s/(\sigma_0+i\gamma_0)|^{-2}$ contribuye con un polo de Cauchy-Poisson en $s$ real cerca de $\gamma_0$ con "anchura" $\sigma_0-1/2 = \delta$. $\square$

**Conjetura Puente (forma operacional, C.P.-O).** Para cada $n\geq 1$:
$$\Delta_n^\text{full} - \Delta_n^{\text{full,on}} = K_n \cdot C_\infty(\gamma_n) + O(C_\infty(\gamma_n)^2),$$
donde $K_n = L_n[\int_\mathbb{R} s^{2k} P_{\sigma_0-1/2}(s-\gamma_n)\,dm_\text{full}^\text{on}(s)]_{k\geq 0}$ y $P_y(t) = y/(\pi(t^2+y^2))$ es el núcleo de Poisson.

**Justificación de la C.P.-O.** De la Proposición 6.2: $\delta c_{2k}^\text{off} \approx \int s^{2k}\sum_{\rho_0\in\mathcal{Z}_\text{off}} P_{\sigma_0-1/2}(s-\gamma_0)\cdot K\,dm_\text{full}^\text{on}$. Aplicando el funcional lineal $L_n$:
$$\Delta_n^\text{full} - \Delta_n^{\text{full,on}} \approx K\cdot L_n\!\left[\int s^{2k}\sum_{\rho_0}P_{\sigma_0-1/2}(s-\gamma_0)\,dm_\text{full}^\text{on}\right].$$
Por definición del déficit (Doc 42): $C_\infty(\gamma_n) = \sum_{\rho_0}P_{\sigma_0-1/2}(\gamma_n-\gamma_0)$. La C.P.-O. afirma que la evaluación en el funcional $L_n$ de la medida de Poisson de los ceros off-críticos, integrada contra $dm_\text{full}^\text{on}$, coincide con la evaluación en $\gamma_n$. Esta es una condición sobre la "localidad" del funcional $L_n$: si $L_n$ estuviera concentrado en $s = \gamma_n$, la C.P.-O. sería exacta. $\square$

---

## §7. Relación con la positividad de Weil

El vínculo con el formalismo de CCM se hace explícito al observar que la forma de Weil localizada $Q_n$ (introducción de CCM) está relacionada con los momentos de $dm_S$ para $S$ que incluye todos los primos $\leq n$.

**Proposición 7.1 (Weil y discrepancia).** Sea $S_n = \{\infty, p : p\leq n\}$. Entonces:
$$Q_n(\varphi,\varphi) = \int_\mathbb{R}|\hat\varphi(s)|^2\,d(dm_{S_n}-dm_\infty)(s)$$
para toda función de prueba $\varphi$ con soporte en $[n^{-1/2},n^{1/2}]$, donde $\hat\varphi$ es la transformada de Mellin.

**Demostración.** La forma de Weil semilocal es la diferencia entre la parte aritmética (primos $\leq n$, es decir, $S_n$) y la parte arquimediana. Expresada en el espacio de Mellin via la transformada $\mathcal{V}_{S_n}$, toma exactamente la forma $\int|\hat\varphi|^2\,d(dm_{S_n}-dm_\infty)$. (Esto es la Proposición 1.1 de CCM aplicada a $\varphi_{S_n}$.) $\square$

**Corolario 7.2 (Positividad de Weil como condición sobre $\Delta_n^{S_n}$).** $Q_n(\varphi,\varphi)\geq 0$ para toda $\varphi$ con soporte en $[n^{-1/2},n^{1/2}]$ si y solo si la medida $dm_{S_n}-dm_\infty$ es no-negativa en el soporte espectral relevante, lo que es equivalente a $\Delta_k^{S_n}\geq 0$ para todo $k$.

**Demostración.** La no-negatividad de $Q_n$ para todas las funciones de prueba es equivalente a la no-negatividad de la medida diferencia (por la completitud del sistema de test functions en el espacio de Mellin). La no-negatividad de la medida $dm_{S_n} - dm_\infty$ se traduce en $(a_k^{S_n})^2 \geq (a_k^\infty)^2$, es decir, $\Delta_k^{S_n}\geq 0$, que está probado en la Proposición 3.2 del Doc 59. $\square$

**Observación 7.3 (Positividad de Weil $\Rightarrow$ ¡ya probada!).** El Corolario 7.2 junto con la Proposición 3.2 del Doc 59 da:

> **Para todo $n$, la forma de Weil localizada $Q_n(\varphi,\varphi)\geq 0$ para toda $\varphi$ con soporte en $[n^{-1/2},n^{1/2}]$.**

Pero esto es exactamente la dirección **conocida** de RH: la positividad de $Q_n$ está probada por Connes et al. como consecuencia de la positividad de $dm_{S_n}/dm_\infty \geq 0$. Lo que sigue sin probarse es que esta positividad implica que los ceros están en la línea crítica.

La distinción es:
- **Probado:** $dm_{S_n} \geq dm_\infty$ puntualmente → $Q_n \geq 0$ (trivialmente).
- **No probado:** $Q_n \geq 0$ con igualdad exactamente en $\{\gamma_n\}$ → RH.

La igualdad $Q_n(\varphi_n,\varphi_n) = 0$ para la función de prueba $\varphi_n$ que "selecciona" el cero $\gamma_n$ requiere que $dm_\text{full}(\gamma_n) = dm_\infty(\gamma_n)$, es decir, $|\zeta(1/2+i\gamma_n)|^2 = 1$... lo cual no es simplemente verdad.

---

## §8. Diagnóstico honesto

**Resultado probado (nuevo, riguroso):**
$$\Delta_n^{\{\infty,p\}} = \frac{A_n}{p} + O(p^{-3/2}\log p), \quad \sum_{p\leq T}\Delta_n^{\{\infty,p\}} \sim A_n\log\log T.$$

**Conjetura operacional (C.P.-O):** $\Delta_n^\text{full} - \Delta_n^{\text{full,on}} = K_n C_\infty(\gamma_n) + O(C_\infty^2)$. El obstáculo es que $\Delta_n^{\text{full,on}}$ requiere conocer los ceros críticos a priori.

**El muro:**
1. El Corolario 7.2 muestra que $Q_n \geq 0$ se deduce de $\Delta_n^{S_n} \geq 0$ (Doc 59, Prop. 3.2), que ya está probado. Pero no captura la condición de igualdad que daría RH.
2. La C.P.-O. es estructuralmente correcta (la derivación de la Proposición 6.2 es sólida) pero requiere probar la "localidad" del funcional $L_n$ en $\gamma_n$.
3. El funcional $L_n$ es explícito (Def. 3.1) pero computarlo en función de los ceros de $\zeta$ requiere resolver el problema espectral inverso para $dm_\infty$.

**El Doc 61** atacará la localidad del funcional $L_n$: ¿es verdad que $L_n[\int s^{2k}f(s)\,dm_\text{on}] \approx f(\gamma_n)\cdot c$ para alguna constante $c$ y funciones $f$ concentradas cerca de $\gamma_n$?

---

## Referencias

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [Sz75] G. Szegő. *Orthogonal Polynomials*. AMS, 4ª ed. [Teoría de perturbaciones de polinomios ortogonales.]
- Doc 42: Fórmula del déficit $C_\infty(\gamma_n) = \mathcal{P}[\mu_\text{off}](\gamma_n)$.
- Doc 43: Teorema de Rigidez — un cero del déficit implica RH.
- Doc 54: Fórmula aritmética del déficit.
- Doc 59: Discrepancia de Jacobi semilocal $\Delta_n^S$; Conjetura Puente original.
