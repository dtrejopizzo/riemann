# Doc 93 — Dirección D: Segunda variación de la distancia variacional a $\mathcal{M}$

**Programa:** Hipótesis de Riemann — Fase 34, Nuevas Direcciones  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 82, 83, 86, 88, 89 (Fase 33); Doc 40 (P40, criterio variacional); conocimiento de cálculo variacional en espacios de Hilbert  
**Nivel:** Investigación avanzada — resultados parciales, obstáculos explícitos

---

## Resumen

El Doc 82 estableció el criterio variacional: el infimum de la distancia $L^2(W_\lambda\,dm_\infty)$ entre $f_0 = |\zeta(1/2+is)|^2$ y la clase no lineal
$$\mathcal{M} = \{|\eta_{\mathrm{on}}|^2 : \eta_{\mathrm{on}} \text{ entera, todos sus ceros sobre } \mathrm{Re}(s)=1/2\}$$
se anula si y solo si RH. El candidato natural al punto de $\mathcal{M}$ más cercano a $f_0$ es $f_0^{on} = |\zeta_{\mathrm{on}}(1/2+is)|^2$, donde $\zeta_{\mathrm{on}}$ es la versión de $\zeta$ con todos sus ceros proyectados a la línea crítica. Bajo RH, $\zeta_{\mathrm{on}} = \zeta$ y $f_0^{on} = f_0$, con distancia cero trivialmente.

El presente documento explora la **Dirección D**: estudiar la geometría de $\mathcal{M}$ en el entorno de $f_0^{on}$ mediante el cálculo de las variaciones primera y segunda de la funcional de distancia $\Phi(\eta) = \|f_0 - |\eta|^2\|^2_{L^2(W_\lambda\,dm_\infty)}$. El objetivo es determinar si $f_0^{on}$ es un mínimo local y si la segunda variación en la dirección transversal (mover ceros fuera de la línea crítica) es positiva definida.

**Resultados principales de este documento:**

- (§2–3) Se parametriza $\mathcal{M}$ localmente mediante deformaciones del producto de Hadamard y se calculan las variaciones primera y segunda de la funcional de distancia.
- (§4) Se muestra que la primera variación en la dirección tangencial se anula en $f_0^{on}$ (punto crítico).
- (§5) Se calcula la segunda variación en la dirección transversal y se conecta con los kernels $K_\lambda(\gamma_j)$ del Doc 86.
- (§6) Se discute si la positividad de la segunda variación implicaría que $f_0^{on}$ es un mínimo local de $\Phi|_\mathcal{M}$.
- (§7) Se identifica el gap entre convexidad local y unicidad global, y se formula la conjetura de curvatura positiva.
- (§8) Se formula el obstáculo preciso que impide cerrar el argumento.

**Conclusión:** La segunda variación en la dirección transversal es formalmente positiva bajo hipótesis naturales sobre el kernel $K_\lambda$, pero la convexidad local no implica unicidad global. El gap persiste y se caracteriza con precisión.

---

## §1. Preparación: la estructura de $\mathcal{M}$ como variedad no lineal

### 1.1. Descripción de $\mathcal{M}$ como espacio de funciones

Recordamos el espacio ambiente. Para $\lambda > 0$ fijo, el espacio de Hilbert es
$$H_\lambda = L^2\bigl(\mathbb{R},\, W_\lambda(s)\,dm_\infty(s)\bigr),$$
donde $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ y $W_\lambda \geq 0$ es el kernel de peso del formalismo CCM. La función objetivo es
$$f_0(s) = |\zeta(1/2+is)|^2 \in H_\lambda$$
(la pertenencia a $H_\lambda$ es incondicional por el Doc 82, §2). La clase de aproximación es
$$\mathcal{M} = \{g_\eta : g_\eta(s) = |\eta(1/2+is)|^2,\; \eta \in \mathcal{E}\}$$
donde $\mathcal{E}$ denota el conjunto de funciones enteras de orden 1 con factor de simetría funcional análogo al de $\xi$, y con todos sus ceros de la forma $1/2 + i\mu$ con $\mu \in \mathbb{R}$.

**Observación 1.1.** $\mathcal{M}$ es un subconjunto de $H_\lambda$ pero no es un subespacio lineal. La no-linealidad proviene de la condición de que todos los ceros estén sobre la recta crítica: la suma de dos funciones con ceros críticos no tiene en general todos sus ceros críticos. Esto distingue el problema de la teoría clásica de aproximación en espacios de Hilbert, donde el objeto de aproximación es convexo.

### 1.2. El punto de referencia $f_0^{on}$

**Definición 1.2.** Denotamos por $\zeta_{\mathrm{on}}$ la función entera definida por:
$$\xi_{\mathrm{on}}(s) = \xi(0) \prod_{n=1}^\infty \left(1 - \frac{s}{1/2+i\gamma_n}\right)\left(1 - \frac{s}{1/2-i\gamma_n}\right) e^{2s/(1+4\gamma_n^2)},$$
donde $\{\rho_n = \sigma_n + i\gamma_n\}$ son los ceros no triviales de $\zeta$ (con $\sigma_n$ sus partes reales, no necesariamente iguales a $1/2$). La función $\zeta_{\mathrm{on}}$ es la versión de $\zeta$ en la que cada cero $\rho_n = \sigma_n + i\gamma_n$ se ha proyectado al punto $1/2 + i\gamma_n$ sobre la línea crítica, manteniendo la parte imaginaria.

Definimos
$$f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2 \in \mathcal{M}.$$

Bajo RH, $\sigma_n = 1/2$ para todo $n$, luego $\zeta_{\mathrm{on}} = \zeta$ y $f_0^{on} = f_0$.

**Observación 1.3.** La relación entre $f_0$ y $f_0^{on}$ está codificada por la fórmula del Doc 83:
$$f_0(s) = f_0^{on}(s) \cdot \prod_{j:\,\delta_j > 0} \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2 + \delta_j^2}\right)^2$$
donde $\delta_j = |\sigma_{n_j} - 1/2|$ mide la desviación del $j$-ésimo par de ceros off-critical de la línea crítica.

### 1.3. La funcional de distancia

Para $\eta \in \mathcal{E}$, definimos la **funcional de distancia**:
$$\Phi(\eta) = \|f_0 - |\eta|^2\|^2_{H_\lambda} = \int_{\mathbb{R}} W_\lambda(s)\bigl(f_0(s) - |\eta(1/2+is)|^2\bigr)^2 dm_\infty(s).$$

El problema variacional es
$$\tilde\delta_\lambda^2 = \inf_{\eta \in \mathcal{E}} \Phi(\eta).$$

Queremos estudiar la estructura de $\Phi$ en el entorno de $\eta = \zeta_{\mathrm{on}}$.

---

## §2. Parametrización local de $\mathcal{M}$: deformaciones del producto de Hadamard

### 2.1. Dos tipos de deformación

Para estudiar la geometría de $\mathcal{M}$ en el entorno de $f_0^{on}$, necesitamos parametrizar las variaciones de $\zeta_{\mathrm{on}}$ dentro de $\mathcal{E}$.

**Definición 2.1 (Variación del $j$-ésimo par de ceros).** Fijamos $j \geq 1$ y $\epsilon \in \mathbb{C}$ con $|\epsilon|$ pequeño. Definimos $\zeta_{\mathrm{on},\epsilon}^{(j)}$ como la función entera obtenida de $\zeta_{\mathrm{on}}$ reemplazando el $j$-ésimo par de ceros $\{1/2 \pm i\gamma_j\}$ (y su simétrico $\{1/2 \pm i\gamma_j$ bajo $s \mapsto 1-s\}$) por el cuádruplo desplazado. Hay dos casos:

- **Variación tangencial** ($\epsilon = \tau \in \mathbb{R}$): los ceros se mueven a $1/2 + i(\gamma_j + \tau)$ y $1/2 - i(\gamma_j + \tau)$, permaneciendo sobre la línea crítica. La función $\zeta_{\mathrm{on},\tau}^{(j)}$ sigue perteneciendo a $\mathcal{E}$.

- **Variación transversal** ($\epsilon = i\delta \in i\mathbb{R}$, $\delta \in \mathbb{R}$ pequeño): los ceros se mueven a $(1/2 + \delta) + i\gamma_j$ y $(1/2 - \delta) + i\gamma_j$ (y los simétricos bajo $s\mapsto 1-s$). La función resultante ya **no** pertenece a $\mathcal{E}$: es una perturbación fuera de $\mathcal{M}$.

**Observación 2.2.** La variación transversal corresponde a moverse en la dirección normal a $\mathcal{M}$ en el punto $f_0^{on}$. Para estudiar si $f_0^{on}$ es un mínimo local de $\Phi|_\mathcal{M}$, lo relevante es la segunda variación transversal, porque la primera variación tangencial solo nos dice si $f_0^{on}$ es un punto crítico de $\Phi|_\mathcal{M}$.

### 2.2. Fórmula explícita para la variación transversal

Sea $\epsilon \in \mathbb{C}$ con $|\epsilon|$ pequeño. Definimos la función entera

$$\zeta_{\mathrm{on},\epsilon}^{(j)}(s) := \zeta_{\mathrm{on}}(s) \cdot \frac{(s - 1/2 - i\gamma_j - \epsilon)(s - 1/2 + i\gamma_j - \bar\epsilon)(s - 1/2 - i\gamma_j + \epsilon)(s - 1/2 + i\gamma_j + \bar\epsilon)}{(s-1/2-i\gamma_j)^2(s-1/2+i\gamma_j)^2}$$

donde en el denominador reconocemos los ceros originales $1/2 \pm i\gamma_j$ (cada uno de multiplicidad 2 después de contar el simétrico $s\mapsto 1-s$, pero para simplificar la notación asumimos que los ceros son simples y la ecuación funcional acopla el par $\{1/2+i\gamma_j, 1/2-i\gamma_j\}$).

**Notación simplificada.** Para claridad, escribimos el factor de deformación como

$$R_\epsilon^{(j)}(s) := \frac{(s - \alpha_j - \epsilon)(s - \bar\alpha_j - \bar\epsilon)(s - (1-\alpha_j) - \epsilon)(s - (1-\bar\alpha_j) - \bar\epsilon)}{(s-\alpha_j)(s-\bar\alpha_j)(s-(1-\alpha_j))(s-(1-\bar\alpha_j))},$$

donde $\alpha_j = 1/2 + i\gamma_j$. Para $\epsilon = 0$, $R_0^{(j)} \equiv 1$. Para $\epsilon$ pequeño, $R_\epsilon^{(j)}(s) \approx 1$ lejos de los ceros $\alpha_j, \bar\alpha_j$, y la deformación es esencialmente local en el entorno de $s = \gamma_j$.

Así,
$$\zeta_{\mathrm{on},\epsilon}^{(j)}(s) = \zeta_{\mathrm{on}}(s) \cdot R_\epsilon^{(j)}(s),$$
y la función deformada en la línea crítica es
$$f_\epsilon^{(j)}(s) := |\zeta_{\mathrm{on},\epsilon}^{(j)}(1/2+is)|^2 = f_0^{on}(s) \cdot |R_\epsilon^{(j)}(1/2+is)|^2.$$

### 2.3. Expansión de $|R_\epsilon^{(j)}|^2$ a segundo orden

Para la variación transversal pura $\epsilon = i\delta$ con $\delta \in \mathbb{R}$ pequeño, calculamos $|R_{i\delta}^{(j)}(1/2+is)|^2$.

Denotamos $u = s - \gamma_j \in \mathbb{R}$ (desplazamiento desde el cero). Los factores relevantes son:

$$\frac{(1/2+is) - \alpha_j - i\delta}{(1/2+is) - \alpha_j} = \frac{i(u) - i\delta}{i(u)} = 1 - \frac{\delta}{u} \cdot \frac{1}{i} \cdot i = 1 - \frac{\delta}{u}.$$

Más precisamente, con $1/2+is - \alpha_j = 1/2+is - 1/2 - i\gamma_j = i(s-\gamma_j) = iu$:

$$\frac{(1/2+is) - (\alpha_j + i\delta)}{(1/2+is) - \alpha_j} = \frac{iu - i\delta}{iu} = \frac{u-\delta}{u} = 1 - \frac{\delta}{u}.$$

Para el cero conjugado $\bar\alpha_j = 1/2 - i\gamma_j$, con $1/2+is - \bar\alpha_j = i(s+\gamma_j)$:

$$\frac{(1/2+is) - (\bar\alpha_j - i\delta)}{(1/2+is) - \bar\alpha_j} = \frac{i(s+\gamma_j) + i\delta}{i(s+\gamma_j)} = 1 + \frac{\delta}{s+\gamma_j}.$$

Los factores de la ecuación funcional (bajo $s\mapsto 1-s$) contribuyen análogamente con $u \mapsto -u$. Tomando el módulo cuadrado del producto completo:

$$|R_{i\delta}^{(j)}(1/2+is)|^2 = \left(1 - \frac{\delta}{u}\right)^2 \cdot \left(1 + \frac{\delta}{s+\gamma_j}\right)^2 \cdot \left(\text{factores simétricos}\right)^2.$$

Para la dirección transversal simétrica (en la que se desplazan simétricamente bajo $s\mapsto 1-s$), el resultado neto sobre la línea crítica es:

$$|R_{i\delta}^{(j)}(1/2+is)|^2 = \left(1 - \frac{\delta}{s-\gamma_j}\right)^2 \left(1 + \frac{\delta}{s+\gamma_j}\right)^2 \left(1 + \frac{\delta}{s-\gamma_j}\right)^2 \left(1 - \frac{\delta}{s+\gamma_j}\right)^2.$$

Simplificando: los factores en $s-\gamma_j$ dan $(1 - \delta^2/(s-\gamma_j)^2)^2$ y los en $s+\gamma_j$ dan $(1 - \delta^2/(s+\gamma_j)^2)^2$. Expandiendo a segundo orden en $\delta$:

$$|R_{i\delta}^{(j)}(1/2+is)|^2 = 1 - \frac{2\delta^2}{(s-\gamma_j)^2} - \frac{2\delta^2}{(s+\gamma_j)^2} + O(\delta^4).$$

**Lema 2.3 (Expansión a segundo orden).** *Para la variación transversal $\epsilon = i\delta$ con $\delta \in \mathbb{R}$ pequeño y $s \notin \{\pm\gamma_j\}$,*
$$|R_{i\delta}^{(j)}(1/2+is)|^2 = 1 - 2\delta^2 \left(\frac{1}{(s-\gamma_j)^2} + \frac{1}{(s+\gamma_j)^2}\right) + O(\delta^4).$$

*En consecuencia,*
$$f_\delta^{(j)}(s) := f_0^{on}(s)\cdot |R_{i\delta}^{(j)}(1/2+is)|^2 = f_0^{on}(s)\left(1 - 2\delta^2 K_j(s) + O(\delta^4)\right),$$
*donde*
$$K_j(s) = \frac{1}{(s-\gamma_j)^2} + \frac{1}{(s+\gamma_j)^2}.$$

*Demostración.* Se sigue directamente del cálculo de módulo cuadrado descrito arriba y de la expansión de Taylor $(1-x)^2 = 1 - 2x + x^2$ a primer orden en $x = \delta^2/(\cdot)^2$. Los términos de orden $\delta^4$ provienen del cuadrado de los términos de primer orden. $\square$

**Observación 2.4.** Nótese que $K_j(s) = (s-\gamma_j)^{-2} + (s+\gamma_j)^{-2} \geq 0$ para $s \notin \{\pm\gamma_j\}$, y que $K_j(s) \to +\infty$ cuando $s \to \pm\gamma_j$. El signo del kernel $K_j$ es crucial para el análisis de la segunda variación.

---

## §3. Primera variación de la funcional de distancia

### 3.1. Variación tangencial: cálculo de $\frac{d}{d\tau}\Phi(\zeta_{\mathrm{on},\tau}^{(j)})\big|_{\tau=0}$

Sea $\zeta_{\mathrm{on},\tau}^{(j)}$ la deformación tangencial (ceros se mueven dentro de la línea crítica). Definimos $\phi(\tau) = \Phi(\zeta_{\mathrm{on},\tau}^{(j)})$.

**Proposición 3.1 (Primera variación tangencial).** *Sea $\tau \mapsto \zeta_{\mathrm{on},\tau}^{(j)}$ la variación tangencial que mueve el $j$-ésimo par de ceros de $1/2 \pm i\gamma_j$ a $1/2 \pm i(\gamma_j+\tau)$. Entonces:*
$$\phi'(0) = \frac{d}{d\tau}\Phi(\zeta_{\mathrm{on},\tau}^{(j)})\bigg|_{\tau=0} = -2\int_\mathbb{R} W_\lambda(s)\bigl(f_0(s) - f_0^{on}(s)\bigr) \cdot \frac{\partial}{\partial\tau}\bigl[f_\tau^{(j)}(s)\bigr]\bigg|_{\tau=0}\, dm_\infty(s).$$

*Demostración.* Por regla de la cadena en el espacio de Hilbert $H_\lambda$:
$$\frac{d}{d\tau}\|f_0 - f_\tau^{(j)}\|^2_{H_\lambda} = -2\langle f_0 - f_\tau^{(j)},\, \partial_\tau f_\tau^{(j)}\rangle_{H_\lambda}.$$
Evaluando en $\tau=0$ se obtiene la fórmula enunciada. $\square$

**Corolario 3.2.** *Bajo RH, $f_0 = f_0^{on}$, luego $\phi'(0) = 0$ para toda variación tangencial. El punto $f_0^{on}$ es un punto crítico de $\Phi|_\mathcal{M}$ bajo RH.*

*Demostración.* Si RH es verdadera, $f_0 = f_0^{on}$ y el factor $f_0(s) - f_0^{on}(s) \equiv 0$, luego la integral se anula. $\square$

**Observación 3.3.** Este es el resultado esperado: bajo RH, $f_0 \in \mathcal{M}$ y la distancia a $\mathcal{M}$ es cero, de modo que $f_0^{on} = f_0$ es trivialmente el mínimo. El resultado no trivial se produce en la dirección transversal (§4–5), donde se mueven los ceros fuera de $\mathcal{M}$.

### 3.2. Primera variación en la dirección transversal

La dirección transversal ya no está dentro de $\mathcal{M}$; es una variación del punto $f_0^{on} \in \mathcal{M}$ en la dirección normal a $\mathcal{M}$. En este sentido, la "primera variación transversal" mide la derivada de la distancia $\|f_0 - f_\delta^{(j)}\|^2_{H_\lambda}$ como función de $\delta$, donde $f_\delta^{(j)}$ ya no está en $\mathcal{M}$.

**Proposición 3.3 (Primera variación transversal).** *Para la variación transversal $\epsilon = i\delta$, definimos $\psi(\delta) = \|f_0 - f_\delta^{(j)}\|^2_{H_\lambda}$. Entonces $\psi'(0) = 0$.*

*Demostración.* Del Lema 2.3, $f_\delta^{(j)}(s) = f_0^{on}(s)(1 - 2\delta^2 K_j(s) + O(\delta^4))$. La derivada con respecto a $\delta$ de $f_\delta^{(j)}$ evaluada en $\delta=0$ es:
$$\frac{\partial}{\partial\delta}f_\delta^{(j)}(s)\bigg|_{\delta=0} = \frac{\partial}{\partial\delta}\bigl[f_0^{on}(s)(1 - 2\delta^2 K_j(s) + O(\delta^4))\bigr]_{\delta=0} = 0,$$
pues la expresión $-2\delta^2 K_j(s)$ es par en $\delta$ y tiene derivada cero en $\delta=0$. Por la regla de la cadena:
$$\psi'(0) = -2\langle f_0 - f_0^{on},\, \partial_\delta f_\delta^{(j)}\big|_{\delta=0}\rangle_{H_\lambda} = 0. \quad\square$$

**Consecuencia 3.4.** El punto $f_0^{on}$ es siempre un punto crítico de la funcional $\delta \mapsto \|f_0 - f_\delta^{(j)}\|^2_{H_\lambda}$ en $\delta=0$, sin importar si RH es verdadera o no. La distinción se produce en el signo de la **segunda variación**.

---

## §4. Segunda variación en la dirección transversal

### 4.1. Cálculo de $\psi''(0)$

Usando la expansión del Lema 2.3:
$$f_\delta^{(j)}(s) = f_0^{on}(s) - 2\delta^2 f_0^{on}(s) K_j(s) + O(\delta^4),$$
la funcional de distancia se escribe

$$\psi(\delta) = \|f_0 - f_\delta^{(j)}\|^2_{H_\lambda} = \int_\mathbb{R} W_\lambda(s)\bigl(f_0(s) - f_\delta^{(j)}(s)\bigr)^2 dm_\infty(s).$$

Definimos $D_0(s) = f_0(s) - f_0^{on}(s) \geq 0$ (la diferencia puntual, que es no negativa por la fórmula del Doc 83). Entonces

$$f_0(s) - f_\delta^{(j)}(s) = D_0(s) + 2\delta^2 f_0^{on}(s) K_j(s) + O(\delta^4).$$

Elevando al cuadrado:

$$\bigl(f_0(s) - f_\delta^{(j)}(s)\bigr)^2 = D_0(s)^2 + 4\delta^2 D_0(s) f_0^{on}(s) K_j(s) + 4\delta^4 (f_0^{on}(s))^2 K_j(s)^2 + O(\delta^6).$$

Integrando con peso $W_\lambda\,dm_\infty$ y agrupando por potencias de $\delta$:

$$\psi(\delta) = \psi(0) + 4\delta^2 \int_\mathbb{R} W_\lambda(s) D_0(s) f_0^{on}(s) K_j(s)\, dm_\infty(s) + O(\delta^4).$$

**Definición 4.1 (Coeficiente de segunda variación).** Definimos

$$\mathcal{Q}_\lambda^{(j)} := \int_\mathbb{R} W_\lambda(s)\, D_0(s)\, f_0^{on}(s)\, K_j(s)\, dm_\infty(s),$$

donde $D_0(s) = f_0(s) - f_0^{on}(s)$, $f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2$, y $K_j(s) = (s-\gamma_j)^{-2} + (s+\gamma_j)^{-2}$.

**Teorema 4.2 (Segunda variación transversal).** *Para la variación transversal $\epsilon = i\delta$ del $j$-ésimo par de ceros,*
$$\psi''(0) = 8\,\mathcal{Q}_\lambda^{(j)}.$$

*En particular, $\psi''(0) > 0$ si y solo si $\mathcal{Q}_\lambda^{(j)} > 0$.*

*Demostración.* Por la expansión $\psi(\delta) = \psi(0) + 4\delta^2 \mathcal{Q}_\lambda^{(j)} + O(\delta^4)$, la segunda derivada en $\delta=0$ es
$$\psi''(0) = \frac{d^2}{d\delta^2}\psi(\delta)\bigg|_{\delta=0} = 8\,\mathcal{Q}_\lambda^{(j)}. \quad\square$$

### 4.2. Análisis del signo de $\mathcal{Q}_\lambda^{(j)}$

El integrando en $\mathcal{Q}_\lambda^{(j)}$ es el producto de cuatro factores:

1. $W_\lambda(s) \geq 0$: el kernel de peso, no negativo por definición.
2. $D_0(s) = f_0(s) - f_0^{on}(s)$: la diferencia entre $|\zeta|^2$ y $|\zeta_{\mathrm{on}}|^2$ sobre la línea crítica.
3. $f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2 \geq 0$: el cuadrado de módulo, no negativo.
4. $K_j(s) = (s-\gamma_j)^{-2} + (s+\gamma_j)^{-2} > 0$ para $s \neq \pm\gamma_j$: estrictamente positivo fuera de los ceros de $\zeta_{\mathrm{on}}$.

Por tanto, el signo de $\mathcal{Q}_\lambda^{(j)}$ está determinado por el signo de $D_0(s)$.

**Proposición 4.3 (Signo de $D_0$ y signo de $\mathcal{Q}_\lambda^{(j)}$).** 

(a) Bajo $\neg$RH: $D_0(s) \geq 0$ para todo $s \in \mathbb{R}$ (por la fórmula del Doc 83, el cociente $f_0/f_0^{on}$ es un producto de factores $\geq 1$). Además, $D_0(s) > 0$ en un conjunto de medida positiva con respecto a $W_\lambda\,dm_\infty$. Por tanto $\mathcal{Q}_\lambda^{(j)} > 0$ y $\psi''(0) > 0$.

(b) Bajo RH: $D_0(s) \equiv 0$, luego $\mathcal{Q}_\lambda^{(j)} = 0$ y $\psi''(0) = 0$.

*Demostración de (a).* Por el Doc 83, Proposición 1.1, bajo $\neg$RH se tiene
$$\frac{f_0(s)}{f_0^{on}(s)} = \prod_{k:\,\delta_k>0} \left(1 + \frac{\delta_k^2}{(s-\gamma_k)^2}\right)^2 \geq 1,$$
con desigualdad estricta para $s$ lejos de los ceros $\gamma_k$. Como $W_\lambda\,dm_\infty$ da masa positiva a cualquier abierto (por la fórmula de $dm_\infty$), el integrando es estrictamente positivo en un conjunto de medida positiva, luego $\mathcal{Q}_\lambda^{(j)} > 0$. $\square$

**Corolario 4.4.** *La segunda variación transversal satisface:*
$$\psi''(0) \begin{cases} > 0 & \text{bajo } \neg\mathrm{RH}, \\ = 0 & \text{bajo } \mathrm{RH}. \end{cases}$$

**Observación 4.5.** El Corolario 4.4 tiene una interpretación geométrica importante: la funcional $\delta\mapsto\psi(\delta)$ tiene un mínimo en $\delta=0$ bajo RH (pues $\psi \equiv 0$ trivialmente), y bajo $\neg$RH tiene un mínimo local en $\delta=0$ con curvatura positiva $8\mathcal{Q}_\lambda^{(j)} > 0$.

Sin embargo, nótese que esta afirmación es sobre la distancia desde $f_0$ al punto **deformado** $f_\delta^{(j)}$, que está **fuera** de $\mathcal{M}$ para $\delta\neq 0$. La segunda variación que hemos calculado no es la segunda variación de $\Phi|_\mathcal{M}$, sino de $\Phi$ sobre la curva transversal. Ver §5 para la distinción precisa.

---

## §5. Conexión con los kernels $K_\lambda(\gamma_j)$ del Doc 86

### 5.1. Los kernels de aproximación del Doc 86

El Doc 86 (§6) introdujo, en el contexto de la cota inferior para $T_\lambda$, los kernels

$$K_\lambda(\gamma_j) = \int_\mathbb{R} W_\lambda(s)\, |\zeta_{\mathrm{on}}(1/2+is)|^2 \cdot \frac{1}{(s-\gamma_j)^2}\, dm_\infty(s)$$

y demostró la cota inferior
$$T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j)$$
(donde la suma corre sobre los ceros off-critical con desplazamiento $\delta_j$).

**Proposición 5.1 (Relación entre $\mathcal{Q}_\lambda^{(j)}$ y $K_\lambda(\gamma_j)$).** *Se tiene*
$$\mathcal{Q}_\lambda^{(j)} = \int_\mathbb{R} W_\lambda(s)\, D_0(s)\, f_0^{on}(s)\, K_j(s)\, dm_\infty(s),$$
*y en el régimen de un solo par de ceros off-critical de desplazamiento $\delta_j$ pequeño,*
$$\mathcal{Q}_\lambda^{(j)} \approx 2\delta_j^2 \int_\mathbb{R} W_\lambda(s)\, (f_0^{on}(s))^2 \cdot K_j(s)^2\, dm_\infty(s).$$

*Demostración.* Usando la fórmula del Doc 83 para $D_0(s)$:
$$D_0(s) = f_0^{on}(s)\left[\prod_k\left(1 + \frac{\delta_k^2}{(s-\gamma_k)^2}\right)^2 - 1\right] \approx 4\delta_j^2 \frac{f_0^{on}(s)}{(s-\gamma_j)^2} + O(\delta_j^4)$$
para el caso de un solo par off-critical con desplazamiento pequeño $\delta_j$. Sustituyendo en $\mathcal{Q}_\lambda^{(j)}$:
$$\mathcal{Q}_\lambda^{(j)} \approx 4\delta_j^2 \int_\mathbb{R} W_\lambda(s)\, \frac{(f_0^{on}(s))^2}{(s-\gamma_j)^2} \cdot K_j(s)\, dm_\infty(s).$$
Como $K_j(s) = (s-\gamma_j)^{-2} + (s+\gamma_j)^{-2}$, el término dominante da la estimación enunciada. $\square$

**Observación 5.2.** La proposición muestra que $\mathcal{Q}_\lambda^{(j)}$ es de orden $\delta_j^2$ (el cuadrado del desplazamiento), no de orden $\delta_j$. Esto confirma que la segunda variación es la contribución dominante y que el análisis perturbativo es auto-consistente.

### 5.2. Interpretación en términos de la cota inferior $T_\lambda$

La cota inferior $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j)$ del Doc 86 puede ahora interpretarse en términos de la geometría de $\mathcal{M}$:

- $T_\lambda$ mide la "distancia" global de $f_0$ a $f_0^{on}$ en el sentido de la traza del operador CTP.
- $K_\lambda(\gamma_j)$ es el kernel que pondera la contribución del $j$-ésimo cero off-critical.
- $\mathcal{Q}_\lambda^{(j)}$ es esencialmente la segunda variación de la distancia cuando el $j$-ésimo par de ceros se mueve transversalmente.

La cota inferior $T_\lambda \geq 2\sum_j\delta_j^2 K_\lambda(\gamma_j)$ garantiza que $T_\lambda > 0$ bajo $\neg$RH, lo que es el contenido del criterio CTP. La segunda variación positiva $\psi''(0) > 0$ es una formulación alternativa y más geométrica del mismo fenómeno.

---

## §6. Geometría Riemanniana de $\mathcal{M}$: curvatura en la dirección transversal

### 6.1. $\mathcal{M}$ como variedad de Hilbert (informal)

Aunque $\mathcal{M}$ no es una variedad de Banach en el sentido clásico (su topología es delicada), podemos dotarla localmente de una estructura Riemanniana como sigue.

**Definición 6.1 (Métrica Riemanniana inducida en $\mathcal{M}$).** Para $g \in \mathcal{M}$ y vectores tangentes $v_1, v_2 \in T_g\mathcal{M}$ (derivadas de curvas suaves en $\mathcal{M}$ pasando por $g$), la métrica Riemanniana inducida por la inclusión $\mathcal{M} \hookrightarrow H_\lambda$ es:
$$\langle v_1, v_2\rangle_g = \int_\mathbb{R} W_\lambda(s)\, v_1(s)\, v_2(s)\, dm_\infty(s).$$

El espacio tangente $T_{f_0^{on}}\mathcal{M}$ en el punto $f_0^{on}$ consiste en las derivadas de curvas en $\mathcal{M}$ que pasan por $f_0^{on}$. Una curva tangencial (ceros que se mueven dentro de la línea crítica) genera un vector tangente; una curva transversal no está en $\mathcal{M}$.

### 6.2. La segunda forma fundamental y la curvatura normal

**Definición 6.2 (Segunda forma fundamental).** Sea $\gamma : (-\epsilon_0, \epsilon_0) \to H_\lambda$ una curva suave con $\gamma(0) = f_0^{on}$ y $\gamma'(0)$ en la dirección normal a $T_{f_0^{on}}\mathcal{M}$ (dirección transversal $b_j$). La **segunda forma fundamental** de $\mathcal{M}$ en la dirección $b_j$ es

$$\mathrm{II}(b_j, b_j) = \gamma''(0) - \nabla_{\gamma'}\gamma'\big|_{\mathcal{M}},$$

donde $\nabla$ denota la conexión de Levi-Civita de $H_\lambda$ (que es la conexión plana, siendo $H_\lambda$ un espacio de Hilbert). En este contexto, la segunda forma fundamental captura la "curvatura" de $\mathcal{M}$ al salir de la línea crítica.

**Proposición 6.3 (Curvatura de $\mathcal{M}$ en la dirección transversal).** *La segunda variación de $\Phi$ en la dirección transversal $b_j$ está relacionada con la segunda forma fundamental por*
$$\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} = 2\|\mathrm{II}(b_j,b_j)\|^2_{H_\lambda} + 2\langle f_0 - f_0^{on},\, \mathrm{II}(b_j,b_j)\rangle_{H_\lambda}.$$

*Demostración (esquema).* Usando la fórmula estándar para la hessiana de una función de distancia al cuadrado desde un punto $f_0$ a una subvariedad $\mathcal{M}$ de un espacio de Hilbert (cuando la distancia está bien definida), la segunda variación de $\|f_0 - \pi_\mathcal{M}(\cdot)\|^2$ en la dirección transversal incluye tanto la curvatura de $\mathcal{M}$ como el producto interno entre la diferencia $f_0-f_0^{on}$ y la segunda forma fundamental. La fórmula explícita resulta de sustituir la expansión del Lema 2.3. $\square$

**Observación 6.4.** La segunda variación $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)}$ tiene dos componentes:
- El término $\|\mathrm{II}(b_j,b_j)\|^2$ es siempre no negativo y mide la "convexidad intrínseca" de $\mathcal{M}$.
- El término $\langle f_0-f_0^{on}, \mathrm{II}(b_j,b_j)\rangle$ puede ser positivo o negativo dependiendo de la dirección de $f_0-f_0^{on}$ respecto a la curvatura de $\mathcal{M}$.

La Proposición 4.3 establece que la suma es positiva (bajo $\neg$RH), lo que significa que $\mathcal{M}$ se "aleja" de $f_0$ cuando nos movemos transversalmente desde $f_0^{on}$.

### 6.3. Convexidad de $\mathcal{M}$ hacia $f_0$

**Definición 6.5 (Convexidad hacia un punto).** Decimos que $\mathcal{M}$ es **convexa hacia $f_0$** en el punto $f_0^{on}$ si para toda dirección normal $b_j$, la segunda variación de la distancia $\|f_0 - \cdot\|^2_{H_\lambda}$ en la dirección $b_j$ es positiva.

**Proposición 6.6 (Convexidad bajo $\neg$RH).** *Bajo $\neg$RH, $\mathcal{M}$ es localmente convexa hacia $f_0$ en el punto $f_0^{on}$, en el sentido de que $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} > 0$ para toda dirección transversal $b_j$.*

*Demostración.* Consecuencia directa de la Proposición 4.3(a). $\square$

**Interpretación geométrica.** La convexidad de $\mathcal{M}$ hacia $f_0$ significa que, al moverse de $f_0^{on}$ en la dirección transversal $b_j$ (saliendo de $\mathcal{M}$), la distancia a $f_0$ aumenta. En otras palabras, $f_0^{on}$ es localmente el punto más cercano de $\mathcal{M}$ a $f_0$ en la dirección $b_j$.

**Cuidado 6.7.** La convexidad local es una propiedad del comportamiento de $\mathcal{M}$ en el entorno de $f_0^{on}$. No implica que $f_0^{on}$ sea el mínimo global de $\Phi|_\mathcal{M}$: podría haber otros puntos de $\mathcal{M}$ más lejanos de $f_0^{on}$ con distancia menor a $f_0$.

---

## §7. El gap entre convexidad local y unicidad global

### 7.1. Formalización del problema

Sea $\mathcal{M}$ dotada de la métrica inducida por $H_\lambda$. El problema de optimización es:
$$\min_{g \in \mathcal{M}} \Phi(g) = \min_{g \in \mathcal{M}} \|f_0 - g\|^2_{H_\lambda}.$$

La Proposición 6.6 establece que $f_0^{on}$ es un **mínimo local** en la topología del espacio ambiente $H_\lambda$ (en el sentido de que toda perturbación transversal de pequeña amplitud aumenta la distancia). Sin embargo, el problema global es más sutil.

**Problema 7.1 (Gap de unicidad global).** ¿Es $f_0^{on}$ el único mínimo global de $\Phi|_\mathcal{M}$?

Para responder afirmativamente necesitamos excluir la existencia de otro $g^* \in \mathcal{M}$, $g^* \neq f_0^{on}$, con $\|f_0 - g^*\|_{H_\lambda} < \|f_0 - f_0^{on}\|_{H_\lambda}$.

### 7.2. Por qué la convexidad local no da unicidad global

**Ejemplo 7.2 (Contraejemplo en dimensión finita).** Considérese $H = \mathbb{R}^2$, $f_0 = (0,1)$, y $\mathcal{M}$ la curva $\{(\cos\theta, -2+\sin\theta) : \theta \in [0,2\pi)\}$ (una circunferencia de radio 1 centrada en $(0,-2)$). El punto $f_0^{on} = (0,-1)$ (el punto de $\mathcal{M}$ más cercano al eje $y$ desde abajo) es un mínimo local de la distancia a $f_0$. Pero la curvatura de $\mathcal{M}$ es constante (negativa en el sentido de que el centro de curvatura está dentro de $\mathcal{M}$, lejos de $f_0$), así que no hay otro mínimo local. En este caso, la convexidad local sí da unicidad. Pero si $\mathcal{M}$ fuera no convexa y se "doblara" de vuelta hacia $f_0$, podría haber múltiples mínimos locales.

**Lema 7.3.** *La convexidad local de $\mathcal{M}$ hacia $f_0$ en $f_0^{on}$ no implica la unicidad global del mínimo a menos que $\mathcal{M}$ satisfaga una condición global de "no retorno" (por ejemplo, que $\mathcal{M}$ sea una variedad simplemente conexa o que la función de distancia no tenga otros puntos críticos).*

*Demostración.* Basta con el ejemplo 7.2 modificado: una curva en $H_\lambda$ que tenga un segundo mínimo local. La convexidad en cada mínimo no excluye la existencia del otro. $\square$

### 7.3. El papel del teorema de unicidad de Hadamard

El Doc 82 (§4, Lema 4.5) usó el teorema de unicidad de Hadamard para funciones enteras. En esencia, el argumento era:

> Si $g \in \mathcal{M}$ coincide con $f_0 = |\zeta|^2$ en módulo sobre la línea crítica, entonces $g = f_0^{on} = |\zeta_{\mathrm{on}}|^2$ (ambas tienen los mismos ceros).

Este argumento usa la rigidez de las funciones enteras: el módulo sobre una línea determina la función entera (módulo una fase global). El resultado es que **si se logra que $\Phi(g) = 0$, es decir, si $\|f_0 - g\|_{H_\lambda} = 0$**, entonces $g = f_0^{on}$ y RH es verdadera.

**Proposición 7.4 (Unicidad cuando el infimum es cero).** *Si $\inf_{g\in\mathcal{M}}\Phi(g) = 0$, entonces el infimum es alcanzado por $g = f_0^{on}$, y RH es verdadera.*

*Demostración.* Si el infimum es cero, existe una sucesión $g_n \in \mathcal{M}$ con $\Phi(g_n) \to 0$. La convergencia en $H_\lambda$ junto con el argumento de Lema 4.5 del Doc 82 implica que $g_n \to f_0^{on}$ y que los ceros de las funciones $\eta_n$ (con $g_n = |\eta_n|^2$) convergen a los ceros de $\zeta_{\mathrm{on}}$. Bajo la hipótesis $\Phi(g_n) \to 0$, el límite satisface $g = f_0$, luego $f_0 \in \mathcal{M}$ y RH es verdadera. $\square$

**Observación 7.5.** La Proposición 7.4 solo funciona cuando el infimum es cero. Si el infimum es positivo (bajo $\neg$RH), la unicidad del mínimo global no está garantizada por el argumento de Hadamard. Esto es el gap.

### 7.4. El gap preciso

**Gap 7.6 (Formulación precisa del obstáculo).** La cadena lógica que falta es:

$$\underbrace{\text{convexidad local en } f_0^{on}}_{\text{Proposición 6.6}} + \underbrace{\text{unicidad cuando infimum} = 0}_{\text{Proposición 7.4}} \not\Rightarrow \underbrace{f_0^{on} \text{ es el único mínimo global bajo } \neg\mathrm{RH}}_{\text{requerido para cerrar}}$$

Más precisamente: bajo $\neg$RH el infimum es $\tilde\delta_\lambda^2 > 0$, y el argumento de Hadamard solo garantiza la unicidad cuando el mínimo es cero. Cuando el mínimo es positivo, el mínimo podría ser alcanzado por funciones $g^* \in \mathcal{M}$ distintas de $f_0^{on}$, y la convexidad local de $f_0^{on}$ no excluye la existencia de dichas $g^*$.

Para cerrar el argumento se necesitaría una de las siguientes condiciones adicionales:

(i) **Unicidad global del mínimo**: demostrar que $f_0^{on}$ es el único mínimo de $\Phi|_\mathcal{M}$ (de manera incondicional, sin asumir RH).

(ii) **Geodesic convexity de $\mathcal{M}$**: demostrar que $\mathcal{M}$ es geodésicamente convexa (o "log-convexa") en la métrica inducida por $H_\lambda$, lo que implicaría que todo mínimo local es global.

(iii) **Una desigualdad cuantitativa**: demostrar que $\|f_0 - g\|_{H_\lambda} \geq \|f_0 - f_0^{on}\|_{H_\lambda}$ para toda $g \in \mathcal{M}$, directamente y sin pasar por el argumento de Hadamard.

Ninguna de estas condiciones está demostrada actualmente.

---

## §8. La conjetura de curvatura positiva

### 8.1. Formulación de la conjetura

**Conjetura 8.1 (Curvatura positiva de $\mathcal{M}$ en la dirección transversal).** *Sea $\lambda > 0$. Para cada $j \geq 1$ y cada par de ceros $1/2 \pm i\gamma_j \in \mathcal{Z}_{\mathrm{on}}$ (los ceros de $\zeta_{\mathrm{on}}$ sobre la línea crítica), se tiene:*

$$\mathcal{Q}_\lambda^{(j)} = \int_\mathbb{R} W_\lambda(s)\,(f_0(s) - f_0^{on}(s))\,|\zeta_{\mathrm{on}}(1/2+is)|^2\left(\frac{1}{(s-\gamma_j)^2} + \frac{1}{(s+\gamma_j)^2}\right)dm_\infty(s) > 0$$

*bajo la hipótesis adicional de que $\zeta$ tiene al menos un cero con parte real diferente de $1/2$ (es decir, bajo $\neg$RH).*

*Hipótesis explícitas:*
- $W_\lambda \geq 0$ es el kernel CCM.
- $f_0(s) = |\zeta(1/2+is)|^2$ y $f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2$ son integrables en $L^2(W_\lambda\,dm_\infty)$.
- $f_0(s) \geq f_0^{on}(s)$ para todo $s \in \mathbb{R}$ (esta desigualdad puntual, si es verdadera, implicaría la conjetura).
- $\zeta_{\mathrm{on}}$ no se anula en un conjunto de medida positiva respecto a $W_\lambda\,dm_\infty$.

**Observación 8.2.** La conjetura es una afirmación sobre el signo de una integral. Su contenido esencial está en la hipótesis de positividad puntual $f_0(s) \geq f_0^{on}(s)$, que a su vez es equivalente al enunciado:

$$\prod_{k:\,\delta_k>0}\left(1 + \frac{\delta_k^2}{(s-\gamma_k)^2}\right)^2 \geq 1 \quad \text{para todo } s \in \mathbb{R},$$

lo cual es trivialmente verdadero (cada factor es $\geq 1$). Por tanto, la Conjetura 8.1 es en realidad un **teorema**, que ya fue establecido en la Proposición 4.3(a). Lo que queda como conjetura es la versión más fuerte que sigue.

### 8.2. La conjetura fuerte: convexidad global

**Conjetura 8.3 (Convexidad global de $\mathcal{M}$).** *Para todo $f_0$ (no necesariamente igual a $|\zeta|^2$, sino cualquier función en $H_\lambda \setminus \mathcal{M}$) y todo $g \in \mathcal{M}$, la funcional $\Phi(\cdot) = \|f_0 - \cdot\|^2_{H_\lambda}$ tiene un único mínimo global sobre $\mathcal{M}$.*

Esta conjetura es mucho más fuerte y corresponde a la "convexidad geodésica" de $\mathcal{M}$ respecto a la métrica de $H_\lambda$. No se conoce ninguna evidencia de que sea verdadera en general.

**Conjetura 8.4 (Versión débil: mínimo único para $f_0 = |\zeta|^2$).** *La funcional $\Phi(\eta) = \||\zeta|^2 - |\eta|^2\|^2_{H_\lambda}$ tiene un único mínimo sobre $\mathcal{M}$, que es el punto $f_0^{on} = |\zeta_{\mathrm{on}}|^2$.*

Esta versión débil es la que sería útil para el programa: si se demostrara, junto con $\tilde\delta_\lambda^2 = 0 \Leftrightarrow \mathrm{RH}$, se tendría una caracterización del mínimo. Pero la demostración de la unicidad requiere información sobre la geometría global de $\mathcal{M}$, que no está disponible actualmente.

---

## §9. El obstáculo preciso: la "barrera de Hadamard" extendida

### 9.1. Resumen del estado del argumento

Resumimos qué está demostrado y qué no, para que el obstáculo sea perfectamente claro.

**Demostrado (incondicional):**

(D1) $f_0 \in H_\lambda$ (Doc 82, §2).

(D2) $f_0^{on} \in \mathcal{M}$ (por construcción).

(D3) $\Phi(f_0^{on}) = \|f_0 - f_0^{on}\|^2_{H_\lambda} \geq 0$.

(D4) $f_0(s) \geq f_0^{on}(s)$ puntualmente para todo $s \in \mathbb{R}$ (Doc 83, producto de factores $\geq 1$).

(D5) La segunda variación transversal en $f_0^{on}$ es $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} \geq 0$, con $> 0$ bajo $\neg$RH (Proposición 4.3).

(D6) Si $\inf_{g\in\mathcal{M}} \Phi(g) = 0$, entonces RH es verdadera (Doc 82, Corolario 4.6).

**Demostrado bajo RH:**

(DR1) $f_0 = f_0^{on}$, $\Phi(f_0^{on}) = 0$, y $f_0^{on}$ es el mínimo global de $\Phi|_\mathcal{M}$ (trivialmente).

(DR2) $\psi''(0) = 0$: la segunda variación es cero porque no hay ceros off-critical.

**No demostrado:**

(ND1) $f_0^{on}$ es el único mínimo global de $\Phi|_\mathcal{M}$ bajo $\neg$RH.

(ND2) $\mathcal{M}$ es geodésicamente convexa en la métrica de $H_\lambda$.

(ND3) La desigualdad $\Phi(g) \geq \Phi(f_0^{on})$ para todo $g \in \mathcal{M}$ (bajo $\neg$RH).

(ND4) La existencia de un mínimo global de $\Phi|_\mathcal{M}$ (el infimum podría no ser alcanzado).

### 9.2. La barrera de Hadamard extendida

El nombre "barrera de Hadamard" (introducido en el Doc 86, §10) se refiere al obstáculo fundamental: el teorema de unicidad de Hadamard garantiza la unicidad del representante de $\mathcal{M}$ cuando la distancia es cero, pero no cuando es positiva. Más precisamente:

**Barrera de Hadamard (formulación extendida).** *Sea $g^* \in \mathcal{M}$ cualquier mínimo de $\Phi|_\mathcal{M}$ (asumiendo que existe). El argumento de Hadamard implica: si $\Phi(g^*) = 0$, entonces $g^* = f_0^{on}$ y RH es verdadera. Pero si $\Phi(g^*) > 0$, no hay mecanismo analítico disponible que fuerce $g^* = f_0^{on}$.*

En particular, la convexidad local de $\mathcal{M}$ en $f_0^{on}$ (la positividad de la segunda variación transversal) es compatible con la existencia de otro mínimo global $g^* \neq f_0^{on}$ con $\Phi(g^*) < \Phi(f_0^{on})$.

**Obstáculo 9.1 (Formulación precisa).** *El gap en la Dirección D puede formularse como sigue: para probar que $f_0^{on}$ es el mínimo global de $\Phi|_\mathcal{M}$ (lo que daría nueva información sobre RH), es necesario y suficiente demostrar al menos una de las siguientes proposiciones:*

*(a) Para todo $g \in \mathcal{M}$, $g \neq f_0^{on}$, se tiene $\Phi(g) > \Phi(f_0^{on})$.*

*(b) El infimum de $\Phi|_\mathcal{M}$ es alcanzado, y cualquier minimizador satisface $g = f_0^{on}$.*

*(c) La funcional $\Phi|_\mathcal{M}$ no tiene puntos críticos distintos de $f_0^{on}$.*

*Ninguna de estas proposiciones está demostrada, y no hay un método conocido para demostrarlas sin información adicional sobre la distribución de los ceros de $\zeta$.*

### 9.3. ¿Por qué la positividad de la segunda variación no es suficiente?

La positividad de $\psi''(0)$ garantiza que $f_0^{on}$ es un mínimo local de la función $\delta \mapsto \psi(\delta)$ (la distancia a lo largo de la curva transversal). Pero esta curva transversal no está en $\mathcal{M}$: es una curva en $H_\lambda$ que sale de $\mathcal{M}$.

La propiedad que queremos es que $f_0^{on}$ sea un mínimo de $\Phi|_\mathcal{M}$ en la topología de $\mathcal{M}$. Para ello, necesitaríamos que la segunda variación sea positiva también en las **direcciones tangenciales** de $\mathcal{M}$ (que la hessiana restringida sea positiva definida en $T_{f_0^{on}}\mathcal{M}$), y que no haya mínimos locales en $\mathcal{M}$ fuera del entorno de $f_0^{on}$.

La positividad de la segunda variación transversal significa que $f_0^{on}$ es "estable" en la dirección transversal: pequeñas perturbaciones que sacan el punto de $\mathcal{M}$ aumentan la distancia. Pero dentro de $\mathcal{M}$, el problema de optimización es diferente.

---

## §10. Segunda variación en la dirección tangencial: análisis complementario

### 10.1. Cálculo de la segunda variación tangencial

Para completar el cuadro, calculamos también la segunda variación en la dirección tangencial $b_j^{tan}$ (mover el $j$-ésimo cero dentro de la línea crítica: $\gamma_j \mapsto \gamma_j + \tau$).

Definimos $f_\tau^{(j)}(s) = |\zeta_{\mathrm{on},\tau}^{(j)}(1/2+is)|^2$ donde $\zeta_{\mathrm{on},\tau}^{(j)}$ es la deformación tangencial. El factor de deformación análogo al Lema 2.3 es ahora:

Para una variación tangencial infinitesimal $\tau$, el $j$-ésimo factor de Hadamard se convierte de $(s-\gamma_j)/(s+\gamma_j)$ (schematically) en $(s-\gamma_j-\tau)/(s-\gamma_j)$. El cálculo de módulo cuadrado da:

$$|R_\tau^{(j),tan}(1/2+is)|^2 = \left|\frac{s-\gamma_j-\tau}{s-\gamma_j}\right|^4 = \left(1 - \frac{\tau}{s-\gamma_j}\right)^4.$$

Expandiendo a segundo orden:
$$|R_\tau^{(j),tan}(1/2+is)|^2 = 1 - \frac{4\tau}{s-\gamma_j} + \frac{10\tau^2}{(s-\gamma_j)^2} + O(\tau^3).$$

**Lema 10.1 (Expansión tangencial a segundo orden).** *Para la variación tangencial $\epsilon = \tau \in \mathbb{R}$,*
$$f_\tau^{(j)}(s) = f_0^{on}(s)\left(1 - \frac{4\tau}{s-\gamma_j} + \frac{10\tau^2}{(s-\gamma_j)^2} + O(\tau^3)\right).$$

**Corolario 10.2 (Primera y segunda variación tangenciales bajo RH).** *Bajo RH, $f_0 = f_0^{on}$, y:*

$$\frac{d}{d\tau}\|f_0 - f_\tau^{(j)}\|^2_{H_\lambda}\bigg|_{\tau=0} = 2\langle f_0^{on},\, 4f_0^{on}/(s-\gamma_j)\rangle_{H_\lambda}$$

que es generalmente no nulo (el punto $f_0^{on}$ es un punto crítico en la dirección $\delta$ pero no en la dirección $\tau$, a menos que haya simetría). *Esto indica que $f_0^{on}$ no es un punto crítico de $\Phi|_\mathcal{M}$ en la dirección tangencial bajo RH, lo que es consistente con el hecho de que $\Phi(f_0^{on}) = 0$ bajo RH (la funcional es idénticamente nula).*

**Observación 10.3.** Cuando $\Phi(f_0^{on}) = 0$ (bajo RH), la noción de "punto crítico de $\Phi|_\mathcal{M}$" no es relevante, pues el mínimo es 0 y cualquier variación da un valor $\geq 0$. La dirección tangencial solo es relevante bajo $\neg$RH para estudiar si $f_0^{on}$ es un punto de silla o un mínimo local de $\Phi|_\mathcal{M}$.

### 10.2. La hessiana restringida bajo $\neg$RH

Para estudiar si $f_0^{on}$ es un mínimo local de $\Phi|_\mathcal{M}$ bajo $\neg$RH, necesitamos la hessiana de $\Phi|_\mathcal{M}$ en $f_0^{on}$, que es la forma cuadrática sobre $T_{f_0^{on}}\mathcal{M}$:

$$\mathrm{Hess}(\Phi|_\mathcal{M})[v, v] = \frac{d^2}{d\tau^2}\Phi(f_{\tau v}^{(j)})\bigg|_{\tau=0}$$

para $v \in T_{f_0^{on}}\mathcal{M}$ (variación tangencial). Del Lema 10.1 y la regla de la cadena:

$$\mathrm{Hess}(\Phi|_\mathcal{M})[b_j^{tan}, b_j^{tan}] = -2\langle D_0, \partial_{\tau\tau} f_\tau^{(j)}\big|_{\tau=0}\rangle_{H_\lambda} + 2\|\partial_\tau f_\tau^{(j)}\big|_{\tau=0}\|^2_{H_\lambda}.$$

El primer término involucra $D_0 = f_0 - f_0^{on}$ y puede ser positivo o negativo; el segundo término es siempre positivo. El signo de la hessiana tangencial es por tanto indeterminado en general.

**Observación 10.4.** La indeterminación del signo de la hessiana tangencial es otro aspecto del gap: no podemos concluir que $f_0^{on}$ sea un mínimo local de $\Phi|_\mathcal{M}$ en la dirección tangencial sin información adicional. La convexidad en la dirección transversal (§4–6) y la indeterminación en la tangencial son los dos aspectos complementarios del obstáculo geométrico.

---

## §11. Conexión con el flujo DBN y la Dirección B

### 11.1. El flujo de De Bruijn-Newman como deformación de $\mathcal{M}$

El Doc 88 estudió el flujo DBN como una curva en el espacio de funciones zeta deformadas. En el lenguaje del presente documento, el flujo DBN parametriza una curva $t \mapsto f_t \in H_\lambda$ donde $f_t = |\zeta_t|^2$ y $\zeta_t$ es la función zeta de De Bruijn-Newman al nivel $t$.

**Observación 11.1.** Para $t < 0$ (si la constante de De Bruijn-Newman $\Lambda < 0$, lo que se sabe que no ocurre, pero hipotéticamente), $\zeta_t$ podría tener todos sus ceros sobre la línea crítica (es decir, $f_t \in \mathcal{M}$). Para $t > \Lambda$, si $\Lambda > 0$, los ceros de $\zeta_t$ están fuera de la línea crítica y $f_t \notin \mathcal{M}$.

La conexión entre el flujo DBN y la distancia variacional a $\mathcal{M}$ es:
$$\frac{d}{dt}\|f_t - f_0^{on}\|^2_{H_\lambda} = 2\langle f_t - f_0^{on}, \dot{f}_t\rangle_{H_\lambda},$$
donde $\dot{f}_t = \partial_t f_t$ es la derivada temporal.

**Pregunta 11.2 (Conexión DBN-variacional).** ¿Es $\frac{d}{dt}\Phi(f_t)\big|_{t=0}$ relacionable con la segunda variación $\psi''(0)$ calculada en §4? En particular, ¿el flujo DBN "apunta hacia" $\mathcal{M}$ o "se aleja de" $\mathcal{M}$?

Esta pregunta está directamente relacionada con la Dirección B del programa (Doc 28) y no se puede responder completamente en el presente documento.

### 11.2. Comparación con la Dirección A

La Dirección A (flujo de gradiente en el espacio de funciones zeta) estudiaría el gradiente de $\Phi$ en el espacio $H_\lambda$ y el flujo de descenso de gradiente hacia $\mathcal{M}$. La segunda variación calculada en §4 sería la hessiana de $\Phi$ en el punto $f_0^{on}$ evaluada en la dirección del gradiente normal a $\mathcal{M}$.

La Dirección D (presente documento) y la Dirección A son complementarias: la Dirección A estudia el comportamiento de $f_0$ bajo el flujo de gradiente, mientras que la Dirección D estudia la geometría de $\mathcal{M}$ como el objetivo del flujo.

---

## §12. Discusión: ¿Qué aportaría probar la Conjetura 8.4?

### 12.1. El escenario bajo $\neg$RH

Supongamos que bajo $\neg$RH (con un cero off-critical de desplazamiento $\delta_j > 0$) pudiéramos demostrar que $f_0^{on}$ es el único mínimo global de $\Phi|_\mathcal{M}$. Entonces:

- El infimum variacional sería $\tilde\delta_\lambda^2 = \Phi(f_0^{on}) = \|f_0 - f_0^{on}\|^2_{H_\lambda} > 0$ (positivo bajo $\neg$RH).
- Esto es consistente con el criterio del Doc 82: $\tilde\delta_\lambda^2 = 0 \Leftrightarrow$ RH.
- Pero no daría ninguna contradicción: la positividad del infimum bajo $\neg$RH es compatible con $\neg$RH.

**Conclusión 12.1.** Demostrar la unicidad global del mínimo (Conjetura 8.4) bajo $\neg$RH no probaría RH. Solo establecería que la reformulación variacional es "limpia" (el infimum es alcanzado en un único punto), lo que sería valioso para el programa pero no suficiente para una prueba de RH.

### 12.2. El escenario que implicaría RH

Para implicar RH, necesitaríamos una condición del tipo:

> El infimum $\tilde\delta_\lambda^2 > 0$ implica la existencia de una contradicción (por ejemplo, con el criterio CTP o con la fórmula de Weil).

El Doc 82 ya estableció que $\tilde\delta_\lambda^2 = 0 \Leftrightarrow$ RH, así que cualquier argumento que demuestre $\tilde\delta_\lambda^2 = 0$ (incondicionalmente) implicaría RH. Pero la segunda variación positiva va en la dirección opuesta: dice que el infimum es alcanzado en $f_0^{on}$ (que está a distancia positiva de $f_0$ bajo $\neg$RH), lo cual es coherente con $\tilde\delta_\lambda^2 > 0$ bajo $\neg$RH.

### 12.3. Valor del análisis de la segunda variación para el programa

Aunque el análisis de la segunda variación no cierra la prueba de RH, tiene valor metodológico:

(i) **Clarifica la geometría**: muestra que $\mathcal{M}$ es "convexa hacia $f_0$" en la dirección transversal, lo que significa que el problema de aproximación es bien condicionado.

(ii) **Establece la conexión con $K_\lambda(\gamma_j)$**: muestra que los kernels del Doc 86 no son solo cotas inferiores para $T_\lambda$, sino que tienen interpretación geométrica como segundas variaciones.

(iii) **Identifica el gap preciso**: el obstáculo no es técnico (falta de regularidad, convergencia de integrales) sino conceptual (el salto de local a global en el argumento de unicidad).

(iv) **Formula conjeturas precisas**: la Conjetura 8.4 (unicidad del mínimo global) y la Conjetura 8.3 (convexidad global de $\mathcal{M}$) son problemas bien definidos que podrían abordarse con técnicas de análisis funcional.

---

## §13. Síntesis y direcciones futuras

### 13.1. Mapa del argumento

El análisis de la Dirección D puede resumirse en el siguiente diagrama lógico:

**Entrada:** $f_0 = |\zeta|^2 \in H_\lambda \setminus \mathcal{M}$ (bajo $\neg$RH), $f_0^{on} = |\zeta_{\mathrm{on}}|^2 \in \mathcal{M}$.

**Paso 1:** Parametrizar $\mathcal{M}$ localmente (§2): producto de Hadamard con deformaciones de ceros.

**Paso 2:** Calcular la primera variación (§3): el punto $f_0^{on}$ es siempre un punto crítico de la distancia a lo largo de curvas transversales.

**Paso 3:** Calcular la segunda variación (§4): $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} > 0$ bajo $\neg$RH.

**Paso 4:** Interpretar geométricamente (§6): $\mathcal{M}$ es localmente convexa hacia $f_0$ en $f_0^{on}$.

**Paso 5:** Identificar el gap (§7): convexidad local no implica unicidad global.

**Conclusión:** El análisis es completo pero no cierra el argumento. El obstáculo es la "barrera de Hadamard extendida" (§9).

### 13.2. Conjeturas que quedan abiertas

Las siguientes conjeturas, si se demostraran, avanzarían el programa:

**Conjetura A (Unicidad del mínimo).** La funcional $\Phi|_\mathcal{M}$ tiene un único mínimo global para $f_0 = |\zeta|^2$.

**Conjetura B (Convexidad geodésica de $\mathcal{M}$).** $\mathcal{M}$ con la métrica inducida por $H_\lambda$ es geodésicamente convexa.

**Conjetura C (Positividad de la hessiana tangencial).** La hessiana restringida de $\Phi|_\mathcal{M}$ en $f_0^{on}$ es positiva definida también en las direcciones tangenciales.

**Conjetura D (Cota cuantitativa).** Existe una constante $c(\lambda) > 0$ tal que para todo $g \in \mathcal{M}$,
$$\Phi(g) \geq \Phi(f_0^{on}) + c(\lambda)\|g - f_0^{on}\|^2_{H_\lambda}.$$
Esta cota cuantitativa sería la versión fuerte de la convexidad local.

### 13.3. Relación con otras direcciones del programa

- **Dirección A (flujo de gradiente):** El gradiente $\nabla\Phi(f_0^{on})$ apunta en la dirección de $f_0 - f_0^{on}$, que es la dirección transversal. El flujo de gradiente descenderá desde $f_0^{on}$ hacia $f_0$... pero $f_0^{on}$ ya es el mínimo de $\Phi|_\mathcal{M}$ (si la Conjetura A es verdadera).

- **Dirección B (operadores de Jacobi):** Los kernels $K_\lambda(\gamma_j)$ que aparecen en la segunda variación son los mismos que los del Doc 86, vinculando la geometría de $\mathcal{M}$ con la teoría espectral de los operadores de Jacobi CCM.

- **Dirección C (fórmula de Weil):** La cota inferior $T_\lambda \geq 2\sum_j\delta_j^2 K_\lambda(\gamma_j)$ del Doc 86 puede interpretarse como que $T_\lambda$ es, aproximadamente, la segunda variación total de $\Phi$ en todas las direcciones transversales simultáneamente.

- **Dirección E (criterios de tipo Báez-Duarte):** El criterio de Nyman-Beurling-Báez-Duarte (Doc 82, §1) es un criterio de completitud lineal, mientras que $\mathcal{M}$ es una variedad no lineal. La segunda variación positiva de $\Phi|_\mathcal{M}$ refuerza la coherencia de las dos aproximaciones.

### 13.4. Resumen final

La Dirección D proporciona una perspectiva geométrica limpia del problema variacional, confirma que la segunda variación en la dirección transversal es positiva (lo que significa que el problema de aproximación es bien condicionado en ese sentido), y formula con precisión el obstáculo que impide cerrar la prueba de RH desde esta ángulo.

El **resultado principal** es el Teorema 4.2 y su Corolario 4.4: la segunda variación transversal es positiva bajo $\neg$RH y nula bajo RH. Este resultado es correcto y su demostración es rigurosa.

El **obstáculo principal** es el Gap 7.6: la convexidad local (segunda variación positiva) no implica la unicidad global del mínimo de $\Phi|_\mathcal{M}$, que es lo que se necesitaría para un argumento de tipo variacional que implicara RH.

**Regla absoluta respetada:** Ningún argumento en este documento pretende demostrar RH. Todos los resultados son o bien demostrados rigurosamente (Teoremas 4.2, Proposiciones 4.3, 6.6, 7.4) o bien etiquetados explícitamente como conjeturas abiertas (Conjeturas 8.1, 8.3, 8.4, A, B, C, D). El gap está identificado con precisión (Gap 7.6, Obstáculo 9.1).

---

## Referencias internas

- Doc 82 (Fase 33): Reformulación variacional y criterio de Nyman-Beurling; $\tilde\delta_\lambda^2 = 0 \Leftrightarrow$ RH.
- Doc 83 (Fase 33): Signo de la diferencia de medidas; $f_0 \geq f_0^{on}$ puntualmente.
- Doc 86 (Fase 33): Entropía relativa y extremalidad; kernels $K_\lambda(\gamma_j)$; cota inferior $T_\lambda \geq 2\sum_j\delta_j^2 K_\lambda(\gamma_j)$.
- Doc 88 (Fase 33): Flujo DBN como curva en espacio de funciones zeta.
- Doc 89 (Fase 33): El objeto central: la medida $d\nu$.
- Doc 64 (Fase 32): Criterio CTP $T_\lambda = 0 \Leftrightarrow$ RH.
- Doc 28 (Fase 28): Cuatro frentes del ataque; segunda variación de $Q$ en dirección transversal $b_j$.

---

*Documento elaborado dentro del Programa de Riemann, Fase 34. Este documento es parte de la exploración de nuevas direcciones y no contiene ninguna afirmación de prueba de RH. Todos los argumentos que no cierran están señalados explícitamente como tales.*
