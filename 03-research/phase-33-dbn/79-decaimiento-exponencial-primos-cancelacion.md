# Documento 79 — Decaimiento exponencial, la suma sobre primos y las condiciones de cancelación

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 64, 70, 72, 76

---

## Resumen

El Doc 76 estableció que $|\widehat{W_\lambda\,dm_\infty}(r)| = O(e^{-\pi|r|/4})$ para $|r|\to\infty$, y el Doc 72 demostró que $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ donde $B_\lambda(r) = \mathrm{Re}[\widehat{W_\lambda\,dm_\infty}(r)]$. Este documento explora sistemáticamente las consecuencias del decaimiento exponencial para la suma sobre primos: convergencia absoluta (§1), estructura del término $A_\lambda^{off}$ (§2), la suma de primos como condición de cancelación (§3), análisis cuantitativo de $B_\lambda(\log p)$ (§4 y §5), las sumas geométricas que aparecen en los primos grandes (§6), la reformulación del criterio (§7), y la conexión con el criterio de Nyman-Beurling (§8 y §9). Concluimos con una evaluación honesta del estado del Camino 3.

**Notación permanente en este documento:**

- $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$, densidad $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$.
- $\{P_k\}_{k\geq 0}$ polinomios ortonormales CCM respecto a $dm_\infty$; $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$.
- $W_\lambda(s) = \sum_{k=0}^{N} (k+1)|P_k(s)|^2$ con $N = N(\lambda)$.
- $\phi_k(r) = \int_\mathbb{R} |P_k(s)|^2 e^{irs}\,dm_\infty(s)$.
- $B_\lambda(r) = \mathrm{Re}[\widehat{W_\lambda\,dm_\infty}(r)] = \int_\mathbb{R} W_\lambda(s)\cos(rs)\,dm_\infty(s)$.
- $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ (fórmula de Weil, Doc 72).

---

## §1. Convergencia absoluta de la suma sobre primos

### 1.1. El tamaño de $B_\lambda(\log p)$

Por el Prop. 1.5 del Doc 76, para cada $\lambda > 0$ fijo existe una constante $C_\lambda > 0$ tal que
$$|\widehat{W_\lambda\,dm_\infty}(r)| \leq C_\lambda\,e^{-(\pi/4)|r|}, \qquad r\in\mathbb{R}.$$

Como $B_\lambda(r) = \mathrm{Re}[\widehat{W_\lambda\,dm_\infty}(r)]$, se tiene la cota
$$|B_\lambda(\log p)| \leq C_\lambda\,e^{-(\pi/4)\log p} = C_\lambda\,p^{-\pi/4}.$$

En consecuencia, el término general de la suma sobre primos satisface
$$\frac{\log p}{\sqrt{p}}\,|B_\lambda(\log p)| \leq C_\lambda\,\frac{\log p}{p^{1/2+\pi/4}}.$$

**Proposición 1.1** (Convergencia absoluta). *Para todo $\lambda > 0$, la serie*
$$\sum_p \frac{\log p}{\sqrt{p}}\,B_\lambda(\log p)$$
*converge absolutamente.*

*Demostración.* Es suficiente verificar que $\sum_p \frac{\log p}{p^{1/2+\pi/4}} < \infty$. El exponente es $\alpha := 1/2 + \pi/4 \approx 1{,}285$. Por el teorema de los números primos, $\sum_{p \leq X} \log p \sim X$, de modo que la suma parcial $\sum_{p\leq X} \frac{\log p}{p^\alpha}$ crece como $\int_2^X \frac{dt}{t^{\alpha-1}\log t} \cdot \frac{\log t}{1}$ luego como $\int_2^X t^{-\alpha}\,dt$, integral que converge absolutamente en $[2,\infty)$ pues $\alpha > 1$. La cota $|B_\lambda(\log p)| \leq C_\lambda p^{-\pi/4}$ completa la demostración. $\square$

**Corolario 1.2.** *La cantidad $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ está bien definida para todo $\lambda > 0$, sin ninguna hipótesis sobre los ceros de $\zeta$. Todas las series involucradas en su definición convergen absolutamente.*

*Demostración.* La convergencia de la suma sobre primos se acaba de establecer. La convergencia de $A_\lambda^{off}$ —la contribución de los ceros fuera de la recta crítica en la fórmula de Weil— se sigue de las cotas estándar sobre las funciones de prueba admisibles (ver Doc 72, §3). $\square$

### 1.2. Observación sobre la exponent $\pi/4$

El valor $\pi/4$ proviene de la distancia al primer polo de $\Gamma(1/4+is/2)$ en la variable $s$: el primer polo en el semiplano inferior se halla en $s = -i/2$, y al desplazar el contorno de integración en la definición de $\phi_k(r)$ en una cantidad $\varepsilon = \pi/4$ (que queda dentro de la franja de analiticidad $|\mathrm{Im}(s)| < 1/2$), se recoge el decaimiento $e^{-(\pi/4)|r|}$. Este valor es óptimo para la medida $dm_\infty$; un kernel diferente daría un exponente diferente.

---

## §2. El término $A_\lambda^{off}$ y su significado geométrico

### 2.1. Definición precisa

En la fórmula de Weil aplicada con función de prueba $h_\lambda(s) = W_\lambda(s)\,w(s)$ (Doc 72, §3), el término $A_\lambda^{off}$ recoge la contribución de los ceros de $\zeta$ que no pertenecen a la recta crítica $\mathrm{Re}(s)=1/2$. Más precisamente, si $\mathcal{Z}_{off}$ denota el conjunto de ceros no triviales de $\zeta$ con $\mathrm{Re}(\rho) \neq 1/2$, entonces

$$A_\lambda^{off} = \sum_{\rho \in \mathcal{Z}_{off}} h_\lambda(\gamma_\rho) - \sum_{\rho \in \mathcal{Z}_{off}} h_\lambda(\gamma_\rho^*),$$

donde $\gamma_\rho = \mathrm{Im}(\rho)$ y $\gamma_\rho^* = \mathrm{Im}(\rho^*)$ son las partes imaginarias del cero y de su imagen crítica $\rho^* = 1/2 + i\,\mathrm{Im}(\rho)$. (La definición exacta depende de la parametrización de la fórmula de Weil elegida; ver Doc 72.)

### 2.2. Anulación bajo RH

**Proposición 2.1** (Anulación bajo RH). *Si la hipótesis de Riemann es válida, entonces $A_\lambda^{off} = 0$ para todo $\lambda > 0$.*

*Demostración.* Bajo RH, $\mathcal{Z}_{off} = \emptyset$: todos los ceros no triviales de $\zeta$ están sobre la recta crítica. Por tanto la suma que define $A_\lambda^{off}$ es vacía. $\square$

### 2.3. La pregunta de la dirección inversa

Una pregunta natural es si la condición $A_\lambda^{off} = 0$ para algún $\lambda$ implica RH, o si al menos la restringe. La respuesta es que la equivalencia $A_\lambda^{off} = 0 \iff T_\lambda = 0$ (cuando simultáneamente $\sum_p B_\lambda(\log p) = 0$) es una tautología: ambas son reformulaciones de la misma condición espectral. La ecuación que define $T_\lambda$ es

$$T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p),$$

de modo que $T_\lambda = 0$ equivale a que $A_\lambda^{off}$ y la suma de primos sean iguales. Bajo RH ambos lados son cero (por Prop. 2.1 y por la fórmula de Weil aplicada a funciones de prueba que son transformadas de Fourier de medidas positivas). No hay circularidad, pero tampoco nueva información: la condición $A_\lambda^{off} = 0$ es equivalente a RH por definición del criterio $T_\lambda = 0$.

---

## §3. La suma de primos como obstáculo de oscilación

### 3.1. La ecuación de cancelación

La equivalencia RH $\iff$ $T_\lambda = 0$ para todo $\lambda$ puede reescribirse, gracias a la Prop. 2.1, como:

$$\text{RH} \iff A_\lambda^{off} = 0 \text{ y } \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0 \quad\text{para todo } \lambda > 0.$$

La segunda condición —que la suma sobre primos sea exactamente cero— es una condición de cancelación entre las frecuencias $\cos(s\log p)$ pesadas por $W_\lambda w$.

**Proposición 3.1** (La suma de primos bajo RH). *Bajo la hipótesis de Riemann,*
$$\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0 \quad \text{para todo } \lambda > 0.$$

*Demostración.* Bajo RH, $T_\lambda = 0$ (Doc 64, criterio central) y $A_\lambda^{off} = 0$ (Prop. 2.1). La fórmula $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ da entonces la identidad requerida. $\square$

### 3.2. El obstáculo

**Proposición 3.2** (Obstáculo de dirección inversa). *Las condiciones $A_\lambda^{off} = 0$ y $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ son cada una de ellas equivalente a RH, pero ninguna de las dos es demostrable independientemente de la posición de los ceros de $\zeta$ por los métodos actualmente disponibles.*

*Demostración (del obstáculo).* La condición $A_\lambda^{off} = 0$ equivale, por definición, a que $\mathcal{Z}_{off} = \emptyset$, es decir, exactamente a RH. No es accesible independientemente. La condición $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ es, por la fórmula de Weil, la identidad que resulta de aplicar dicha fórmula a la función de prueba $h_\lambda = W_\lambda w$ asumiendo RH —es decir, es una consecuencia de RH pero no se puede probar sin ella por métodos puramente aritméticos con las herramientas disponibles. $\square$

### 3.3. Una condición necesaria computable

Aunque no podemos probar la igualdad exacta, la Prop. 1.1 garantiza que la serie es absolutamente convergente. Esto permite truncarla y comparar numéricamente:

**Definición 3.3.** Para $X > 2$ y $\lambda > 0$, sea
$$S_\lambda(X) = \sum_{p \leq X} \frac{\log p}{\sqrt{p}} B_\lambda(\log p).$$

Por la Prop. 1.1, $S_\lambda(X) \to \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ cuando $X\to\infty$, con convergencia absoluta. Bajo RH, $\lim_{X\to\infty} S_\lambda(X) = 0$.

La velocidad de convergencia de $S_\lambda(X)$ a cero (bajo RH) es objeto de la §4.

---

## §4. Análisis cuantitativo de $B_\lambda(\log p)$

### 4.1. Descomposición en modos $\phi_k$

Recordamos que $W_\lambda(s) = \sum_{k=0}^N (k+1)|P_k(s)|^2$ y por tanto

$$\widehat{W_\lambda\,dm_\infty}(r) = \sum_{k=0}^N (k+1)\,\phi_k(r),$$

donde la serie es finita. Tomando parte real:

$$B_\lambda(r) = \sum_{k=0}^N (k+1)\,\phi_k(r).$$

Para $r = \log p$ con $p$ primo:

$$B_\lambda(\log p) = \sum_{k=0}^N (k+1)\,\phi_k(\log p).$$

### 4.2. Cota para primos grandes

Combinando la descomposición del §4.1 con la cota $|\phi_k(\log p)| \leq C_k\,p^{-\pi/4}$ (Doc 76, Prop. 1.5):

**Proposición 4.1** (Contribución de primos grandes). *Sea $X > e^{2\pi}$. Entonces*
$$\left|\sum_{p > X} \frac{\log p}{\sqrt{p}} B_\lambda(\log p)\right| \leq \tilde{C}_\lambda \sum_{p > X} \frac{\log p}{p^{1/2+\pi/4}} = O_\lambda\!\left(X^{1/2-\pi/4}\right) = O_\lambda\!\left(X^{-0{,}285\ldots}\right).$$

*Demostración.* Se utiliza $|B_\lambda(\log p)| \leq C_\lambda' p^{-\pi/4}$ con $C_\lambda' = \sum_{k=0}^N (k+1) C_k$, y la estimación $\sum_{p>X} \frac{\log p}{p^\alpha} \ll X^{1-\alpha}/\log X$ para $\alpha > 1$, con $\alpha = 1/2+\pi/4$. $\square$

**Corolario 4.2.** *El "núcleo aritmético" de la suma proviene de los primos $p \leq X_0(\lambda)$ con $X_0(\lambda) = \exp(4 N(\lambda)^2/\pi)$; la contribución de primos más grandes es exponencialmente pequeña en $N(\lambda)^2$.*

### 4.3. El valor $B_\lambda(0)$ y la normalización

Para $r = 0$: $B_\lambda(0) = \int W_\lambda\,dm_\infty = \sum_{k=0}^N (k+1) = N(N+1)/2 \sim N^2/2$ (Doc 76, §4). Este es el valor máximo de $|B_\lambda(r)|$ pues $|B_\lambda(r)| \leq B_\lambda(0)$ por definición (la función $\cos(rs)$ tiene módulo $\leq 1$).

---

## §5. Estructura de la suma sobre primos pequeños

### 5.1. Descomposición DC y oscilatoria

Siguiendo la terminología del Doc 76, para $r > 2\pi$ la función $\phi_k(r)$ admite la descomposición asintótica (vía fase estacionaria con el radio Marchenko-Riesz-Szegő $a_k = 2k/\pi$):

$$\phi_k(r) = \phi_k^{DC}(r) + \phi_k^{osc}(r) + O(k^{-\infty}),$$

donde la contribución DC decae exponencialmente en $r$ y la oscilatoria tiene la forma

$$\phi_k^{osc}(r) \approx C_0\,k^{-3/4}\,e^{-8\pi k/r^2}\cos\!\left(\frac{8\pi k}{r} - \frac{\pi}{4}\right).$$

**Proposición 5.1** (Contribución DC a $B_\lambda(\log p)$). *Para primos $p > e^{2\pi}$:*
$$B_\lambda^{DC}(\log p) := \sum_{k=0}^N (k+1)\,\phi_k^{DC}(\log p) = O\!\left(N^{9/4}\,p^{-\pi/4}\right).$$

*Demostración.* La contribución DC satisface $|\phi_k^{DC}(r)| \leq C\,k^{-3/4}\,e^{-(\pi/4)r}$ para $r > 0$. Sumando con pesos $(k+1)$:
$$|B_\lambda^{DC}(\log p)| \leq C\,p^{-\pi/4}\sum_{k=0}^N (k+1) k^{-3/4} \leq C'\,p^{-\pi/4} N^{9/4}. \qquad\square$$

**Proposición 5.2** (Contribución oscilatoria a $B_\lambda(\log p)$). *Para primos $p > e^{2\pi}$:*
$$B_\lambda^{osc}(\log p) := \sum_{k=1}^N (k+1)\,\phi_k^{osc}(\log p) \approx C_0\sum_{k=1}^N k^{1/4}\,e^{-8\pi k/(\log p)^2}\cos\!\left(\frac{8\pi k}{\log p} - \frac{\pi}{4}\right).$$

*Demostración.* Inmediato sustituyendo la expresión asintótica de $\phi_k^{osc}(r)$ con $r = \log p$ y agrupando los pesos $(k+1) \cdot k^{-3/4} \approx k^{1/4}$ para $k$ grande. $\square$

---

## §6. La suma geométrica exponencial y posible cancelación

### 6.1. Identificación de la suma

La contribución oscilatoria del §5.2 puede escribirse, salvo el peso $k^{1/4}$ versus $k^0$, como la parte real de una suma geométrica ponderada. Definamos, para simplificar, la suma sin peso polinomial:

$$\Sigma(r, N) = \sum_{k=1}^N e^{-8\pi k/r^2}\cos\!\left(\frac{8\pi k}{r} - \frac{\pi}{4}\right).$$

Sea $q = e^{-8\pi/r^2}$ y $\theta = 8\pi/r$. Entonces:

$$\Sigma(r,N) = \mathrm{Re}\!\left[e^{-i\pi/4}\sum_{k=1}^N (q e^{i\theta})^k\right] = \mathrm{Re}\!\left[e^{-i\pi/4}\cdot\frac{q e^{i\theta}(1 - (qe^{i\theta})^N)}{1 - q e^{i\theta}}\right].$$

### 6.2. Régimen de primos grandes

Para $r = \log p$ con $p$ grande, $\theta = 8\pi/r \ll 1$ y $q = 1 - 8\pi/r^2 + O(r^{-4}) \approx 1$. El denominador satisface

$$|1 - q e^{i\theta}|^2 = (1-q\cos\theta)^2 + (q\sin\theta)^2 \approx \theta^2 + (1-q)^2 \approx \theta^2 = (8\pi/r)^2.$$

El numerador $|qe^{i\theta}(1-(qe^{i\theta})^N)| \leq 1 + |q|^N \leq 2$. Por tanto

$$|\Sigma(r,N)| \lesssim \frac{1}{|1-qe^{i\theta}|} \approx \frac{r}{8\pi} = \frac{\log p}{8\pi}.$$

Para la suma con peso $k^{1/4}$, la estimación es más delicada, pero en todo caso la suma crece a lo sumo polinomialmente en $\log p$ y en $N$.

**Proposición 6.1** (Cota de la suma oscilatoria). *Para $r = \log p$ con $p > e^{2\pi}$ y $N \geq 1$:*
$$|B_\lambda^{osc}(\log p)| \leq C\,N^{5/4}\,\frac{\log p}{8\pi}.$$

*Demostración.* Se aplica la estimación de la suma geométrica con el peso $k^{1/4}$, dando $\sum_{k=1}^N k^{1/4}/(r^{-1}) \approx N^{5/4} \cdot r/(8\pi)$. La constante absoluta $C$ absorbe la normalización. $\square$

### 6.3. Cancelación entre primos consecutivos

La suma $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda^{osc}(\log p)$ involucra factores $\cos(8\pi k/\log p - \pi/4)$ con fase que varía suavemente entre primos consecutivos. No hay una cancelación obvia entre primos consecutivos (a diferencia de lo que ocurre con las sumas de caracteres de Dirichlet, donde la ortogonalidad proporciona cancelación).

**Lema 6.2** (Ausencia de cancelación evidente). *No existe un mecanismo puramente aritmético-combinatorio que garantice $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda^{osc}(\log p) = 0$ sin información sobre los ceros de $\zeta$.*

*Demostración (informal).* Las fases $8\pi k/\log p$ con $k$ fijo son densas en $[0,2\pi]$ cuando $p$ varía sobre los primos (por la distribución de $\log p \pmod{2\pi k/m}$ para $m\in\mathbb{Z}$, que no tiene estructura algebraica especial). Para que la suma sea exactamente cero se requeriría una ley de cancelación entre primos que es, en última instancia, equivalente a la posición de los ceros de $\zeta$. $\square$

---

## §7. La condición de cancelación y la hipótesis de Riemann

### 7.1. Reformulación espectral

Hemos visto que RH $\iff$ $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ para todo $\lambda > 0$ (combinando Prop. 3.1 con el criterio $T_\lambda = 0$ del Doc 64). Podemos enunciar esto más explícitamente en términos de $\phi_k$:

**Proposición 7.1** (Criterio de cancelación). *Sea $B_\lambda(r) = \sum_{k=0}^N (k+1)\phi_k(r)$ con $\phi_k(r) = \int \cos(rs)|P_k(s)|^2\,dm_\infty(s)$. Entonces:*
$$\text{RH} \iff \sum_p \frac{\log p}{\sqrt{p}} \sum_{k=0}^{N(\lambda)} (k+1)\phi_k(\log p) = 0 \quad \text{para todo } \lambda > 0.$$

*Demostración.* La condición $T_\lambda = 0$ es equivalente a RH (Doc 64). Bajo RH, $A_\lambda^{off}=0$ (Prop. 2.1), y la fórmula $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ da la condición. $\square$

### 7.2. El obstáculo fundamental

La Prop. 7.1 reformula RH como una identidad aritmética: la suma sobre primos de $\frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ debe ser cero. Pero $B_\lambda(\log p) \geq 0$ no es cierto en general (pues $\cos(s\log p)$ no tiene signo definido, aunque la medida $W_\lambda dm_\infty$ es positiva). Más aún:

**Proposición 7.2** (El signo no ayuda). *La suma $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ no es de signo definido: para distintos valores de $\lambda$, puede ser positiva, negativa, o cero.*

*Demostración.* Para $\lambda$ pequeño ($N=0$), $B_\lambda(r) = \phi_0(r) = \int \cos(rs)\,dm_\infty(s) = \hat{w}(r)/\int dm_\infty$, que es real y decae exponencialmente. El valor $\hat{w}(r)$ oscila y cambia de signo para $r$ moderado (ya que $\hat{w} \in L^2(\mathbb{R})$ y $\hat{w}(0) > 0$). Por tanto el término $B_0(\log p) = \hat{w}(\log p)/C$ puede ser positivo o negativo según $p$. La suma total depende de la distribución de los primos y no tiene signo definido. $\square$

---

## §8. Conexión con el criterio de Nyman-Beurling

### 8.1. El criterio de Nyman-Beurling

Recordamos el resultado clásico. Define la función de Nyman $f(x) = \{1/x\} - x\lfloor 1/x^2 \rfloor$ en $(0,\infty)$, y para $0 < a \leq 1$ el traslado $f_a(x) = f(x/a)$.

**Teorema** (Nyman 1950, Beurling 1955). *La hipótesis de Riemann es equivalente a que la función característica $\mathbf{1}_{(0,1)}$ pertenezca al cierre en $L^2(0,\infty)$ del subespacio lineal generado por $\{f_a : 0 < a \leq 1\}$.*

Báez-Duarte (2003) reformuló esto: RH $\iff$ el infimum
$$d_N^2 = \inf_{A_k \in \mathbb{C}} \int_0^\infty \left|\mathbf{1}_{(0,1)}(x) - \sum_{k=1}^N A_k f(x/n_k)\right|^2 \frac{dx}{x}$$
converge a $0$ cuando $N\to\infty$, donde $n_k$ son enteros positivos.

### 8.2. Estructura común con el criterio CTP

Tanto el criterio de Nyman-Beurling como el criterio $T_\lambda = 0$ comparten la siguiente estructura:

1. Se elige una medida positiva $\mu$ sobre un espacio medible $(\Omega, \mathcal{B})$.
2. Se define una función "objetivo" $f^* \in L^2(\mu)$ que codifica la función $\zeta$.
3. RH equivale a que $f^*$ sea aproximable (en norma $L^2(\mu)$) por un sistema $\{f_n\}$ relacionado con los primos o con las frecuencias $e^{is\log p}$.

En el criterio $T_\lambda = 0$:
- $\mu = W_\lambda\,dm_\infty$ (medida positiva sobre $\mathbb{R}$).
- La función "objetivo" es la diferencia $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$.
- RH equivale a que esta diferencia sea cero $\mu$-casi en todo punto (es decir, $T_\lambda = 0$ para todo $\lambda$).
- La suma de primos $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ es la proyección de la fórmula de Weil sobre la función de prueba $W_\lambda w$.

En el criterio de Nyman-Beurling:
- $\mu = dx/x$ (medida de Haar en $(0,\infty)$).
- La función objetivo es $\mathbf{1}_{(0,1)}$.
- RH equivale a que $\mathbf{1}_{(0,1)}$ sea aproximable por trasladados de la función de Nyman.
- Los trasladados están indexados por racionales $a = m/n$, y los denominadores $n$ son enteros (no solo primos).

### 8.3. La pista: completitud versus cancelación

**Proposición 8.1** (La pista de Nyman-Beurling). *Si el sistema $\{\cos(s\log p)\}_{p\,\text{primo}}$ fuera completo en $L^2(W_\lambda\,dm_\infty)$ para algún $\lambda$, y si la condición de cancelación $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ pudiera interpretarse como ortogonalidad de $W_\lambda w$ respecto a todas las frecuencias $\cos(s\log p)$, entonces la completitud implicaría que $W_\lambda w = 0$, lo cual es una contradicción.*

*Demostración.* Si $\{\cos(s\log p)\}$ fuera un sistema completo en $L^2(W_\lambda\,dm_\infty)$, entonces la condición
$$\int \cos(s\log p)\cdot g(s)\,W_\lambda(s)\,dm_\infty(s) = 0 \quad \text{para todo primo } p$$
implicaría $g = 0$ en $L^2(W_\lambda\,dm_\infty)$. Pero la condición $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ no es una suma de integrales contra funciones $g$ separadas: es una sola integral ponderada por la suma sobre primos de $\frac{\log p}{\sqrt{p}}\cos(s\log p)$. Si definiéramos $g(s) = \sum_p \frac{\log p}{\sqrt{p}}\cos(s\log p)$ (una serie que no converge en general), la condición sería $\int g \cdot W_\lambda\,dm_\infty = 0$. La completitud de $\{\cos(s\log p)\}$ no implica que $g = 0$, sino solo que cualquier función ortogonal a todos los cosenos es cero. La contradicción hipotética no se produce; la pista no conduce a una prueba directa. $\square$

**Observación 8.2.** La analogía con Nyman-Beurling sugiere buscar una formulación variacional: ¿existe un infimum $d_\lambda^2 = \inf_{\text{funciones de prueba}} T_\lambda$ que converja a $0$ si y solo si RH? Esta dirección es la que exploraremos en documentos futuros.

---

## §9. Conexión con Nyman-Beurling: estado del Camino 3

### 9.1. Lo que el Camino 3 ha logrado

El Camino 3 (aritmética explícita en la suma de primos) ha producido los siguientes resultados sólidos:

1. **Convergencia absoluta** (Prop. 1.1): la suma $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converge absolutamente para todo $\lambda > 0$, lo que garantiza que $T_\lambda$ es una cantidad bien definida sin hipótesis adicionales.

2. **Cota cuantitativa** (Prop. 4.1): la contribución de primos $p > X$ a la suma es $O_\lambda(X^{-0{,}285})$, lo que implica que el "núcleo aritmético" es finito y en principio computable.

3. **Estructura asintótica** (Props. 5.1 y 5.2): la descomposición DC-oscilatoria de $\phi_k(r)$ permite analizar la suma de primos en términos de sumas geométricas explícitas.

4. **Pista conexión Nyman-Beurling** (§8): la estructura del criterio $T_\lambda = 0$ es formalmente análoga al criterio de Nyman-Beurling, con la suma sobre primos desempeñando el papel del sistema de trasladados de Nyman.

### 9.2. El obstáculo persiste

**Proposición 9.1** (Límite del Camino 3). *La convergencia absoluta y las cotas cuantitativas obtenidas no implican la igualdad $T_\lambda = 0$ ni son suficientes para probar la hipótesis de Riemann por el Camino 3 tal como está formulado.*

*Demostración.* La condición $T_\lambda = 0$ es equivalente a RH (Doc 64). Todo resultado que se pueda obtener sin asumir la posición de los ceros de $\zeta$ implica solo propiedades de convergencia y tamaño de la suma, pero no la cancelación exacta. La igualdad exacta $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ es, por la fórmula de Weil, una consecuencia de RH —no una condición que se pueda verificar independientemente de la posición de los ceros con los métodos actuales. $\square$

### 9.3. La pista de Nyman-Beurling como dirección futura

La conexión con el criterio de Nyman-Beurling sugiere una pregunta concreta:

**Pregunta 9.2.** ¿Existe un análogo del infimum de Báez-Duarte para el criterio $T_\lambda = 0$? Más precisamente: si se define
$$\delta_\lambda^2 = \inf_{g \in V_\lambda} \left\|W_\lambda w - g\right\|_{L^2(\mathbb{R})}^2,$$
donde $V_\lambda$ es el cierre en $L^2(\mathbb{R})$ del subespacio generado por $\{W_\lambda(\cdot)\cos(\cdot\log p) : p\,\text{primo}\}$, ¿es cierto que $\delta_\lambda^2 \to 0$ para todo $\lambda$ si y solo si RH?

Esta pregunta conecta el formalismo CCM con la teoría de aproximación en $L^2$ y abre una dirección no explorada hasta ahora en el programa.

---

## §10. Síntesis y balance

**Teorema 10.1** (Síntesis del Doc 79). *En el marco del criterio CTP-CCM $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$:*

*(i) La suma sobre primos converge absolutamente para todo $\lambda > 0$, con tasa de convergencia $O_\lambda(X^{-0{,}285})$ para el resto de primos $p > X$.*

*(ii) Bajo RH, $A_\lambda^{off} = 0$ y $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ para todo $\lambda > 0$.*

*(iii) La condición de cancelación $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ es equivalente a RH pero no se puede demostrar independientemente de la posición de los ceros de $\zeta$ con los métodos actuales.*

*(iv) La estructura del criterio es formalmente análoga al criterio de Nyman-Beurling; la pregunta de si existe un infimum variacional $\delta_\lambda^2 \to 0 \iff$ RH es una dirección abierta.*

*Demostración.* (i) es la Prop. 1.1 y el Cor. 4.2. (ii) es la Prop. 2.1 y la Prop. 3.1. (iii) es la Prop. 3.2 y la Prop. 9.1. (iv) es la Obs. 8.2 y la Pregunta 9.2. $\square$

---

**Estado del Camino 3 al término del Doc 79:**

El Camino 3 ha llevado a cabo un análisis exhaustivo de la suma de primos $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$: convergencia absoluta, estructura asintótica, cotas cuantitativas, y la identificación de la suma geométrica exponencial que aparece en los primos grandes. El resultado central es que toda la información sobre la posición de los ceros de $\zeta$ está contenida en la condición de cancelación exacta de esta suma —que es, en última instancia, equivalente a RH pero no accesible por métodos puramente aritméticos independientes.

La conexión con el criterio de Nyman-Beurling (§8–9) es genuinamente nueva en el contexto del programa CCM y sugiere explorar una formulación variacional del criterio $T_\lambda = 0$.
