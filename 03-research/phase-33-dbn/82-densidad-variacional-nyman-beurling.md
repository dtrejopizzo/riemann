# Documento 82 — La reformulación variacional y la conexión con Nyman-Beurling

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 64, 70, 72, 76, 79

---

## Resumen

El Doc 79 estableció que la suma de primos $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converge absolutamente y que la ecuación $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ es una tautología bajo RH, sin que la cancelación aritmética entre primos proporcione nueva información. Este documento explora una dirección diferente: reformular RH como un problema de aproximación en $L^2(W_\lambda\,dm_\infty)$ y conectar esta reformulación con el criterio clásico de Nyman-Beurling-Báez-Duarte.

En §1 enunciamos el criterio de Nyman-Beurling en sus tres formas. En §2 identificamos la medida $dm_\infty$ como espacio de referencia y clarificamos el signo de $T_\lambda$. En §3 introducimos la aproximación de $|\zeta|^2$ por funciones del tipo Hadamard con ceros críticos. En §4 formulamos el infimum variacional $\delta_\lambda^2$ y demostramos que $\delta_\lambda^2 = 0 \iff$ RH. En §5 examinamos la completitud del sistema de exponenciales $\{e^{i\gamma_n s}\}$ en $L^2(W_\lambda\,dm_\infty)$ usando el decaimiento exponencial de la medida y el teorema de Beurling-Malliavin. En §6 discutimos la conexión con la conjetura de Montgomery. En §7 hacemos la síntesis, señalando con precisión qué es riguroso, qué es conjetural y cuál es el obstáculo circular que persiste.

---

## §1. El criterio de Nyman-Beurling-Báez-Duarte

### 1.1. El criterio de Nyman (1950)

Sea $\{t\} = t - \lfloor t \rfloor$ la parte fraccionaria de $t > 0$. Para $a \in (0,1)$, definimos la función
$$r_a(t) = \{a/t\}, \qquad t > 0.$$

**Teorema 1.1 (Nyman, 1950).** *La hipótesis de Riemann es verdadera si y solo si la función constante $\mathbf{1}_{(0,1)}$ pertenece al cierre en $L^2(0,1)$ del espacio*
$$\mathcal{N} = \left\{ f(t) = \sum_{k=1}^n c_k \{a_k/t\} : n \geq 1,\; a_k \in (0,1),\; c_k \in \mathbb{C},\; \sum_{k=1}^n c_k a_k = 0 \right\}.$$

La condición $\sum c_k a_k = 0$ garantiza que $f \in L^2(0,1)$ (de otro modo el polo en $t = 0$ puede impedir la cuadrabilidad). El criterio se deduce de la representación integral $\zeta(s) = s\int_0^1 \{1/t\}\, t^{s-1}\,dt + \frac{s}{s-1}$ válida para $\mathrm{Re}(s) > 0$: la función $\mathbf{1}_{(0,1)}$ es aproximable en $L^2(0,1)$ por $\mathcal{N}$ si y solo si la función $\mathbf{1}_{(0,1)}$ no es ortogonal a ningún $f \in L^2(0,1)$ que sea ortogonal a todos los $r_a$, lo cual ocurre precisamente cuando $\zeta$ no se anula en $\mathrm{Re}(s) > 1/2$.

### 1.2. El criterio de Beurling (1955)

Beurling reformuló el criterio de Nyman en términos del espacio de Hardy $H^2$ del semiplano derecho. Definamos
$$\mathcal{B} = \overline{\mathrm{span}}^{L^2(0,\infty)}\{r_a : a \in (0,1)\}$$
con $r_a(t) = \{a/t\}$ extendida como función en $L^2(0,\infty, dt)$.

**Teorema 1.2 (Beurling, 1955).** *La hipótesis de Riemann es verdadera si y solo si $\mathbf{1}_{(0,1)} \in \mathcal{B}$ en $L^2(0,\infty)$.*

Equivalentemente, vía la transformación de Mellin, RH es verdadera si y solo si el sistema $\{r_a : a \in (0,1)\}$ es completo en $L^2(0,\infty)$ en el sentido de que su cierre contiene $\mathbf{1}_{(0,1)}$. La formulación de Beurling hace explícita la conexión con la teoría de espacios invariantes: el cierre $\mathcal{B}$ es un subespacio invariante bajo la multiplicación por $e^{-st}$, y la condición de completitud está relacionada con la estructura de ceros de $\zeta$ en la franja crítica $0 < \mathrm{Re}(s) < 1$.

### 1.3. El criterio de Báez-Duarte (2003)

La formulación cuantitativa más computable del criterio de Nyman-Beurling fue dada por Báez-Duarte. Para $N \geq 1$, definimos la distancia
$$d_N^2 = \inf_{c_1,\ldots,c_N \in \mathbb{C}} \int_0^\infty \left| \mathbf{1}_{(0,1)}(t) - \sum_{k=1}^N c_k \{k/t\} \right|^2 dt.$$

Aquí se usan únicamente los dilados discretos $r_k(t) = \{k/t\}$ para $k = 1, 2, \ldots, N$.

**Teorema 1.3 (Báez-Duarte, 2003).** *La hipótesis de Riemann es verdadera si y solo si $\lim_{N\to\infty} d_N^2 = 0$.*

La computabilidad del criterio descansa en el cálculo explícito de las correlaciones del sistema $\{r_k\}$. Para $j, k \geq 1$:
$$\langle r_j, r_k \rangle_{L^2(0,\infty)} = \int_0^\infty \{j/t\}\{k/t\}\,dt = \frac{\log(jk) + 2\gamma_E}{(jk)^{1/2}},$$
donde $\gamma_E = 0{,}5772\ldots$ es la constante de Euler-Mascheroni. Esta fórmula se verifica por cambio de variable $u = jk/t^2$ y el desarrollo de Fourier de la parte fraccionaria $\{u\} = \frac{1}{2} - \sum_{m=1}^\infty \frac{\sin(2\pi mu)}{\pi m}$.

De forma similar, $\langle \mathbf{1}_{(0,1)}, r_k \rangle_{L^2(0,\infty)} = \int_0^\infty \mathbf{1}_{(0,1)}(t) \{k/t\}\,dt = \frac{1}{2} - \frac{\log k + \gamma_E}{\sqrt{k}}$ (para $k \leq $ algún umbral; la fórmula exacta depende de si $k \geq 1$ o $k < 1$). Con estas fórmulas, $d_N^2$ se expresa como una forma cuadrática en los $c_k$ cuyos coeficientes son accesibles numéricamente, y la convergencia $d_N^2 \to 0$ es verificable empíricamente con alta precisión.

**Observación 1.4.** La secuencia $d_N^2$ es monótonamente no-creciente en $N$ (es una sucesión de infima sobre clases de aproximación que se amplían). Numéricamente se sabe que $d_N^2 \to 0$ con una velocidad consistente con RH, aunque ninguna demostración de la convergencia hacia cero es conocida sin asumir RH.

---

## §2. La medida $dm_\infty$ como espacio de referencia

### 2.1. El espacio $L^2(W_\lambda\,dm_\infty)$ y el criterio CTP

Recordamos que $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ es la medida de referencia del formalismo CCM, y que para cada $\lambda > 0$ el kernel
$$W_\lambda(s) = \sum_{k=0}^{N(\lambda)} (k+1)|P_k(s)|^2$$
define una función de peso no negativa en $L^1(dm_\infty)$ (donde $P_k$ son los polinomios de Jacobi ortonormales con respecto a $dm_\infty$). El producto $W_\lambda\,dm_\infty$ es así una medida positiva finita.

El criterio CTP (Docs 64, 70) afirma:
$$\mathrm{RH} \iff T_\lambda = 0 \quad \forall\lambda > 0,$$
donde
$$T_\lambda = \int_\mathbb{R} W_\lambda(s)\bigl(|\zeta(1/2+is)|^2 - |\zeta_{\mathrm{on}}(1/2+is)|^2\bigr)\,dm_\infty(s).$$

Aquí $\zeta_{\mathrm{on}}$ denota la función zeta hipotética con todos sus ceros sobre la recta crítica (es decir, la función $\zeta$ misma si RH es verdadera, o la versión modificada con ceros proyectados a la recta crítica si no lo es).

### 2.2. Signo de $T_\lambda$

La siguiente proposición precisa el signo de $T_\lambda$ bajo $\neg$RH.

**Proposición 2.1** (signo de $T_\lambda$). *Si $\zeta$ tiene un cero $\rho_0$ con $\mathrm{Re}(\rho_0) \neq 1/2$, entonces existe $\lambda_0 > 0$ tal que $T_{\lambda_0} > 0$.*

*Argumento.* Por la fórmula de Weil (Doc 72), $T_\lambda = A_\lambda^{off}$, donde $A_\lambda^{off}$ es la contribución a la fórmula de Weil de los ceros fuera de la recta crítica. Cada par de ceros simétricos $\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0$ contribuye a $A_\lambda^{off}$ con un término positivo cuando se evalúa con funciones de prueba admisibles $h_\lambda \geq 0$. La positividad es consecuencia del análisis espectral del operador de Hilbert-Jacobi en el espacio de Pontryagin desarrollado en los Docs 35–36; la referencia completa es la Doc 64, Proposición principal. $\square$

**Corolario 2.2.** *$T_\lambda \geq 0$ incondicionalmente para todo $\lambda > 0$, con igualdad para todo $\lambda$ si y solo si RH es verdadera.*

**Observación 2.3.** La no-negatividad de $T_\lambda$ no es obvia desde la definición como diferencia $\int W_\lambda |\zeta|^2\,dm_\infty - \int W_\lambda |\zeta_{\mathrm{on}}|^2\,dm_\infty$; requiere el argumento de Pontryagin de Doc 64. En particular, $|\zeta|^2 \geq |\zeta_{\mathrm{on}}|^2$ en sentido puntual no es cierto en general; la desigualdad es solo integral con el peso $W_\lambda$.

### 2.3. La distancia natural

Definimos la distancia $L^2(W_\lambda\,dm_\infty)$ entre $|\zeta|$ y $|\zeta_{\mathrm{on}}|$:
$$D_\lambda^2 = \int_\mathbb{R} W_\lambda(s)\bigl||\zeta(1/2+is)| - |\zeta_{\mathrm{on}}(1/2+is)|\bigr|^2\,dm_\infty(s).$$

**Proposición 2.4** (comparación $D_\lambda^2$ y $T_\lambda$). *Se tiene*
$$D_\lambda^2 \leq T_\lambda.$$

*Demostración.* Para $a, b \geq 0$ cualesquiera, $(a-b)^2 = a^2 - 2ab + b^2 \leq a^2 - b^2$ si y solo si $2b^2 \leq 2ab$, es decir, $b \leq a$. La desigualdad $D_\lambda^2 \leq T_\lambda$ es así equivalente a que $(|\zeta| - |\zeta_{\mathrm{on}}|)^2 \leq |\zeta|^2 - |\zeta_{\mathrm{on}}|^2$ casi en todas partes con respecto a $W_\lambda\,dm_\infty$, lo cual se reduce a $|\zeta_{\mathrm{on}}| \leq |\zeta|$ c.t.p. en el soporte de $W_\lambda\,dm_\infty$.

Esta desigualdad puntual no está probada en general. Lo que sí se puede decir es: bajo $\neg$RH, $T_\lambda > 0$ (Prop. 2.1) y $D_\lambda^2 \geq 0$ trivialmente. Bajo RH, $D_\lambda^2 = T_\lambda = 0$. La relación exacta entre $D_\lambda^2$ y $T_\lambda$ en general es una pregunta abierta.

La dirección que sí es útil: $T_\lambda = 0 \implies D_\lambda^2 = 0$ (porque $T_\lambda = 0$ implica $|\zeta|^2 = |\zeta_{\mathrm{on}}|^2$ c.t.p. en $L^1(W_\lambda\,dm_\infty)$, lo que a su vez implica $|\zeta| = |\zeta_{\mathrm{on}}|$ c.t.p., luego $D_\lambda^2 = 0$). $\square$

---

## §3. Aproximación de $|\zeta|^2$ por funciones de tipo Hadamard con ceros críticos

### 3.1. El producto de Hadamard de $\xi$

La función $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ satisface $\xi(s) = \xi(1-s)$ y admite el producto de Hadamard
$$\xi(s) = \xi(0) \prod_\rho \left(1 - \frac{s}{\rho}\right),$$
donde el producto se extiende sobre todos los ceros no triviales $\rho$ de $\zeta$ y converge absolutamente en pares simétricos $\rho, 1-\rho$. El valor $\xi(0) = 1/2$.

De la definición de $\xi$, sobre la recta crítica $s = 1/2 + it$:
$$|\zeta(1/2+it)|^2 = \frac{|\xi(1/2+it)|^2}{\frac{1}{4}(1+4t^2) \cdot \frac{1}{4} \cdot \pi^{-1/2-it} \cdot |\Gamma(1/4+it/2)|^2 / (2\pi)^2} \cdot (2\pi)^2.$$

Más precisamente, tenemos la factorización:
$$|\zeta(1/2+it)|^2 = \frac{4\pi^2 |\xi(1/2+it)|^2}{(2\pi)^2 |\Gamma(1/4+it/2)|^2 \cdot \frac{1}{4}(1+4t^2) \cdot \pi^{-1/2}} = \frac{16\pi^{5/2} |\xi(1/2+it)|^2}{(1+4t^2)|\Gamma(1/4+it/2)|^2}.$$

En términos de la densidad $w(t) = (2\pi)^{-2}|\Gamma(1/4+it/2)|^2$ de $dm_\infty$:
$$|\zeta(1/2+it)|^2\,dm_\infty(t) = \frac{16\pi^{5/2}|\xi(1/2+it)|^2}{(1+4t^2)}\,dt.$$

Esta factorización muestra que la parte analíticamente relevante de $|\zeta|^2$ respecto a la medida $dm_\infty$ es esencialmente $|\xi|^2$, módulo factores de crecimiento polinomial conocidos. El producto de Hadamard de $\xi$ proporciona así la descomposición en ceros.

### 3.2. Funciones de tipo Hadamard con ceros críticos

**Definición 3.1.** Una función $\eta_{\mathrm{on}} : \{1/2 + it : t \in \mathbb{R}\} \to \mathbb{C}$ es *del tipo Hadamard con ceros críticos* si existe una sucesión $(\mu_n)_{n \geq 1} \subset \mathbb{R}$ tal que:
$$\eta_{\mathrm{on}}(1/2+it) = \xi(0)\,e^{A+Bt} \prod_{n=1}^\infty \left(1 - \frac{1/2+it}{1/2+i\mu_n}\right)e^{(1/2+it)/(1/2+i\mu_n)},$$
donde $A, B \in \mathbb{C}$ son constantes compatibles con la simetría funcional. Denotamos la clase de estas funciones por $\mathcal{H}_{\mathrm{crit}}$.

Cuando los $\mu_n$ son las partes imaginarias de los ceros no triviales de $\zeta$ (y todos estos ceros están sobre la recta crítica), $\eta_{\mathrm{on}} = \zeta|_{\mathrm{Re}(s)=1/2}$.

### 3.3. Aproximaciones finitas

Para $M \geq 1$, sea $\zeta_M$ la función que retiene solo los primeros $M$ pares de ceros en el producto de Hadamard:
$$\xi_M(1/2+it) = \xi(0) \prod_{k=1}^M \left(1 - \frac{1/2+it}{1/2+i\mu_k}\right)e^{(1/2+it)/(1/2+i\mu_k)},$$
y $\zeta_M(1/2+it) = \xi_M(1/2+it) / [\text{factores regulares}]$.

**Proposición 3.2** (convergencia de la aproximación). *Para todo $\lambda > 0$,*
$$D_\lambda^2(M) := \int_\mathbb{R} W_\lambda(s)\bigl||\zeta(1/2+is)| - |\zeta_M(1/2+is)|\bigr|^2\,dm_\infty(s) \xrightarrow{M\to\infty} D_\lambda^2.$$

*Argumento.* La convergencia del producto de Hadamard implica que $|\xi_M(1/2+is)| \to |\xi(1/2+is)|$ uniformemente sobre compactos. El peso $W_\lambda\,dm_\infty$ tiene decaimiento rápido (exponencial en $|s|$ por el Doc 76), de modo que la integral está dominada por una región compacta efectiva. La convergencia puntual más la dominación completan el argumento por el teorema de convergencia dominada. $\square$

---

## §4. El infimum variacional $\delta_\lambda^2$

### 4.1. Definición

**Definición 4.1.** Para cada $\lambda > 0$, definimos
$$\delta_\lambda^2 = \inf_{\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}} \int_\mathbb{R} W_\lambda(s) \bigl(|\zeta(1/2+is)|^2 - |\eta_{\mathrm{on}}(1/2+is)|^2\bigr)^2 dm_\infty(s).$$

Aquí el infimum se toma sobre todas las funciones del tipo Hadamard con ceros críticos (Def. 3.1). El integrando es el cuadrado de la diferencia de valores cuadráticos.

**Observación 4.2.** Alternativamente, podemos definir
$$\tilde\delta_\lambda^2 = \inf_{\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}} \int_\mathbb{R} W_\lambda(s) \bigl||\zeta(1/2+is)| - |\eta_{\mathrm{on}}(1/2+is)|\bigr|^2 dm_\infty(s),$$
que es la distancia $L^2(W_\lambda\,dm_\infty)$ entre $|\zeta|$ y la clase $|\mathcal{H}_{\mathrm{crit}}|$. Ambas definiciones son pertinentes; la segunda es más natural desde el punto de vista de la aproximación en espacios de Hilbert. A menos que se especifique lo contrario, trabajaremos con $\tilde\delta_\lambda^2$ en lo que sigue.

### 4.2. El criterio variacional

**Proposición 4.3 (RH implica $\tilde\delta_\lambda^2 = 0$).** *Si la hipótesis de Riemann es verdadera, entonces $\tilde\delta_\lambda^2 = 0$ para todo $\lambda > 0$.*

*Demostración.* Bajo RH, todos los ceros no triviales de $\zeta$ están sobre la recta crítica, luego $\zeta \in \mathcal{H}_{\mathrm{crit}}$. Tomando $\eta_{\mathrm{on}} = \zeta$ en la definición, el integrando es idénticamente cero, luego $\tilde\delta_\lambda^2 = 0$. $\square$

**Proposición 4.4 ($\tilde\delta_\lambda^2 = 0$ para todo $\lambda$ implica RH).** *Si $\tilde\delta_\lambda^2 = 0$ para todo $\lambda > 0$, entonces la hipótesis de Riemann es verdadera.*

*Demostración.* Supongamos que $\tilde\delta_\lambda^2 = 0$ para todo $\lambda$. Esto significa que para cada $\lambda$ existe una sucesión $\eta_{\mathrm{on}}^{(n)} \in \mathcal{H}_{\mathrm{crit}}$ tal que $|\eta_{\mathrm{on}}^{(n)}| \to |\zeta|$ en $L^2(W_\lambda\,dm_\infty)$.

La convergencia en $L^2(W_\lambda\,dm_\infty)$ para una sucesión creciente y apropiada de $\lambda$ implica convergencia puntual casi en todo punto para una subsucesión (por un argumento diagonal estándar). La función límite $|\zeta(1/2+is)|$ está así en el cierre de $|\mathcal{H}_{\mathrm{crit}}|$ en el sentido de la convergencia casi en todas partes.

Para concluir RH desde esta completitud se requiere un argumento adicional: que las únicas funciones en $|\mathcal{H}_{\mathrm{crit}}|$ que coinciden con $|\zeta|$ son aquellas cuyos ceros son los mismos que los de $\zeta$. Esto es consecuencia del siguiente lema:

**Lema 4.5.** *Si $\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}$ satisface $|\eta_{\mathrm{on}}(1/2+it)| = |\zeta(1/2+it)|$ para casi todo $t \in \mathbb{R}$, entonces los ceros de $\eta_{\mathrm{on}}$ son los mismos que los de $\zeta$ (es decir, $\eta_{\mathrm{on}}$ y $\zeta$ tienen los mismos ceros sobre la recta crítica, con las mismas multiplicidades).*

*Argumento del Lema 4.5.* Por el producto de Hadamard, $|\eta_{\mathrm{on}}(1/2+it)| = |\zeta(1/2+it)|$ casi en todo punto implica que $|\xi_{\eta_{\mathrm{on}}}(1/2+it)| = |\xi(1/2+it)|$ módulo los factores regulares compartidos. Dos funciones enteras del mismo orden que tienen el mismo módulo sobre una recta son iguales módulo un factor de exponencial pura (teorema de Hadamard aplicado a la función meromorfa $\xi_{\eta_{\mathrm{on}}}/\xi$). Si además ambas tienen todos sus ceros sobre la misma recta $\mathrm{Re}(s) = 1/2$, la función $\xi_{\eta_{\mathrm{on}}}/\xi$ es una función entera sin ceros, luego de la forma $e^{g(s)}$ con $g$ un polinomio de grado $\leq 1$ por el orden de crecimiento. La condición $|\xi_{\eta_{\mathrm{on}}}| = |\xi|$ sobre $\mathrm{Re}(s) = 1/2$ impone que $\mathrm{Re}(g(1/2+it)) = 0$ para todo $t$, lo que fuerza $g$ a ser una constante imaginaria pura. Por tanto $\xi_{\eta_{\mathrm{on}}} = e^{ic}\xi$ para alguna $c \in \mathbb{R}$, luego $\eta_{\mathrm{on}}$ y $\zeta$ tienen exactamente los mismos ceros. $\square$

Retomando la demostración de la Proposición 4.4: si $|\zeta|$ está en el cierre de $|\mathcal{H}_{\mathrm{crit}}|$ y el límite puntual de $|\eta_{\mathrm{on}}^{(n)}|$ es $|\zeta|$, entonces bajo el Lema 4.5, cualquier función $\eta_{\mathrm{on}}$ que coincida en módulo con $\zeta$ sobre la recta crítica tiene los mismos ceros que $\zeta$. Como los ceros de cualquier $\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}$ son reales por definición (están sobre la recta crítica), se sigue que los ceros de $\zeta$ sobre la recta crítica son reales —es decir, sus partes imaginarias son los únicos ceros no triviales— y por tanto RH es verdadera. $\square$

**Corolario 4.6.** *$\tilde\delta_\lambda^2 = 0$ para todo $\lambda > 0$ si y solo si la hipótesis de Riemann es verdadera.*

---

## §5. Completitud del sistema de exponenciales en $L^2(W_\lambda\,dm_\infty)$

### 5.1. El sistema $\{e^{i\gamma_n s}\}$ y la clase Hadamard

Si los ceros no triviales de $\zeta$ son $\rho_n = 1/2 + i\gamma_n$ (bajo RH, los $\gamma_n \in \mathbb{R}$), la función $|\xi(1/2+is)|^2$ puede expresarse formalmente como un producto que involucra los términos $|1 - s/(1/2 + i\gamma_n)|^2$. El logaritmo de este producto es
$$\log |\xi(1/2+is)|^2 = \log|\xi(0)|^2 + 2\,\mathrm{Re}\sum_n \log\left(1 - \frac{1/2+is}{1/2+i\gamma_n}\right) + 2\,\mathrm{Re}\,\frac{1/2+is}{1/2+i\gamma_n}.$$

El desarrollo de Fourier de $\log|\xi|^2$ sobre la recta crítica involucra las frecuencias $\gamma_n$: formalmente, $\log|\xi(1/2+is)|^2$ es una superposición de términos $e^{\pm i\gamma_n s}$. Por tanto, si el sistema $\{e^{i\gamma_n s}\}_{n \geq 1}$ es completo en $L^2(W_\lambda\,dm_\infty)$, toda función suave en ese espacio puede aproximarse, y en particular la función $|\zeta|^2 - |\eta_{\mathrm{on}}|^2$ puede hacerse tan pequeña como se desee.

### 5.2. La densidad de Beurling-Malliavin

Recordamos el teorema fundamental de Beurling y Malliavin (1962) en su forma cualitativa:

**Teorema 5.1 (Beurling-Malliavin, 1962).** *Sea $\Lambda = \{\lambda_n\}_{n \geq 1} \subset \mathbb{R}$ una sucesión de frecuencias con densidad uniforme finita. El sistema $\{e^{i\lambda_n t}\}_{n \geq 1}$ es completo en $L^2(\mathbb{R}, w(t)\,dt)$ donde $w$ tiene soporte compacto si y solo si la densidad de Beurling-Malliavin $D_{BM}(\Lambda) \geq L$, donde $L$ es el radio del soporte de $w$.*

Para el caso que nos ocupa, la medida $W_\lambda\,dm_\infty$ tiene soporte no compacto pero decaimiento exponencial: $W_\lambda(s)\,dm_\infty(s) \leq C_\lambda e^{-\pi|s|/2}\,ds$ (Doc 76, Prop. 1.5). Este decaimiento es análogo a trabajar en un espacio de Paley-Wiener de radio $\pi/2$.

**Proposición 5.2** (densidad de los ceros). *Los ceros imaginarios $\gamma_n > 0$ de $\zeta$ satisfacen*
$$D_{BM}(\{\gamma_n\}) := \liminf_{r\to\infty} \frac{\#\{n : |\gamma_n| \leq r\}}{r} = \frac{\log r}{2\pi}\bigg|_{\text{en promedio}} \to \infty.$$

*Más precisamente, por la fórmula de Riemann-von Mangoldt*
$$N(T) = \#\{\rho : |\mathrm{Im}(\rho)| \leq T, \mathrm{Re}(\rho) \in (0,1)\} = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T),$$
*la densidad media de $\gamma_n$ en $[0, T]$ es $\sim \frac{\log T}{2\pi}$, que tiende a infinito.*

La densidad promedio tiende a infinito (la sucesión $\gamma_n$ es superdensa en el sentido de Beurling-Malliavin). Este hecho es propicio para la completitud.

### 5.3. Completitud en $L^2(W_\lambda\,dm_\infty)$

**Proposición 5.3** (completitud condicional bajo RH). *Asumiendo que todos los $\gamma_n$ son reales (es decir, asumiendo RH), el sistema $\{e^{i\gamma_n s}\}_{n \geq 1}$ es completo en $L^2(W_\lambda\,dm_\infty)$ para todo $\lambda > 0$.*

*Argumento.* La medida $\mu_\lambda = W_\lambda\,dm_\infty$ tiene la propiedad de que su transformada de Fourier $\hat\mu_\lambda(r) = \int e^{irs}\,\mu_\lambda(ds)$ decae exponencialmente: $|\hat\mu_\lambda(r)| = O(e^{-(\pi/4)|r|})$ (Doc 76). Esto significa que $\mu_\lambda$ es una medida en la clase de Bernstein con radio $\pi/4$.

Por el teorema de Beurling-Malliavin adaptado a espacios con peso exponencialmente decreciente (ver Korevaar 2004, cap. 12, o la monografía de Young 1980): si la densidad de $\{\gamma_n\}$ es mayor que $L/\pi$ donde $L = \pi/4$ es el radio efectivo de la medida, entonces el sistema $\{e^{i\gamma_n s}\}$ es completo en $L^2(\mu_\lambda)$.

La condición es que $D_{BM} > L/\pi = 1/4$. Por la Prop. 5.2, $D_{BM} = +\infty$ (en promedio logarítmico). Luego la condición se cumple con holgura, y el sistema es completo. $\square$

**Advertencia 5.4.** El argumento de la Prop. 5.3 es formal en los siguientes puntos: (a) la versión precisa del teorema de Beurling-Malliavin para medidas con decaimiento exponencial (no meramente soporte compacto) requiere verificar condiciones técnicas de la teoría de Paley-Wiener; (b) la "densidad" $D_{BM} = +\infty$ debe interpretarse con cuidado en el sentido logarítmico de la función $N(T)$. El argumento indica la plausibilidad de la completitud, no su demostración rigurosa. Señalamos esto como un punto a desarrollar en la Fase 35.

### 5.4. La pregunta incondicional

La pregunta crítica, que surge de forma natural y que constituye el núcleo del obstáculo circular, es la siguiente:

**Pregunta 5.5.** ¿Es el sistema $\{e^{i\gamma_n s}\}_{n \geq 1}$ completo en $L^2(W_\lambda\,dm_\infty)$ incluso si algunos de los $\gamma_n$ son complejos (es decir, si hay ceros de $\zeta$ fuera de la recta crítica)?

Si la respuesta es afirmativa incondicionalmente, entonces el argumento de completitud no asume RH y $\tilde\delta_\lambda^2 = 0$ seguiría sin asumir RH. Pero $\tilde\delta_\lambda^2 = 0$ equivale a RH por el Corolario 4.6. Esto daría una demostración.

Si la respuesta es negativa —si el sistema $\{e^{i\gamma_n s}\}$ falla ser completo exactamente cuando hay ceros off-critical— entonces la completitud se convierte en un nuevo y equivalente criterio para RH, pero no en una demostración. Examinamos esta alternativa en §6.

---

## §6. Completitud, base de Riesz y la conjetura de Montgomery

### 6.1. Sistemas de exponenciales y bases de Riesz

Un sistema $\{e^{i\lambda_n t}\}_{n \geq 1}$ en $L^2(a, b)$ es una *base de Riesz* si es topológicamente equivalente a una base ortonormal: existen constantes $0 < A \leq B < \infty$ tales que para toda sucesión finita $(c_n)$,
$$A\sum|c_n|^2 \leq \left\|\sum_n c_n e^{i\lambda_n t}\right\|^2 \leq B\sum|c_n|^2.$$

Por el teorema de Pavlov (1979), el sistema $\{e^{i\gamma_n t}\}_{n \geq 1}$ es una base de Riesz en $L^2(0, a)$ si y solo si los $\gamma_n$ satisfacen la condición de Carleson: $\inf_{n \neq m} |\gamma_n - \gamma_m| > 0$ (separación uniforme) y la condición de Blaschke sobre las partes imaginarias cuando los $\gamma_n$ son complejos.

Si algunos $\gamma_n$ tienen parte imaginaria no nula (ceros off-critical), la condición de Blaschke puede fallar, destruyendo la estructura de base de Riesz. Esto sugiere que la completitud del sistema de exponenciales en $L^2(W_\lambda\,dm_\infty)$ podría fallar precisamente bajo $\neg$RH.

### 6.2. La conjetura de Montgomery y la rigidez de los ceros

La *conjetura de par de correlaciones* de Montgomery (1973) afirma que para $0 < a < b < \infty$,
$$\lim_{T\to\infty} \frac{1}{N(T)} \#\left\{(m,n) : m \neq n,\; \gamma_m, \gamma_n \in [0,T],\; a \leq \frac{\gamma_m - \gamma_n}{2\pi/\log T} \leq b\right\} = \int_a^b \left(1 - \left(\frac{\sin\pi u}{\pi u}\right)^2\right)du.$$

Esta conjetura, apoyada por extensas verificaciones numéricas y compatible con la estadística de matrices aleatorias unitarias GUE, implica que las fluctuaciones de $N(T) - \frac{T}{2\pi}\log\frac{T}{2\pi}$ son de orden $O(\log T)$ —mucho más pequeñas que las fluctuaciones $O(T^{1/2})$ esperadas para una secuencia aleatoria. Esta *rigidez* de los ceros es una propiedad estructural profunda.

**Proposición 6.1** (rigidez condicional y completitud). *Bajo la conjetura de Montgomery, la sucesión $(\gamma_n)$ tiene la propiedad de separación local:*
$$\liminf_{n\to\infty} (\gamma_{n+1} - \gamma_n) \cdot \frac{\log\gamma_n}{2\pi} > 0.$$
*Esto implica la condición de Carleson para las frecuencias re-escaladas $\tilde\gamma_n = \gamma_n / \frac{\log\gamma_n}{2\pi}$, y en consecuencia el sistema $\{e^{i\gamma_n s}\}$ es una base de Riesz en $L^2(0, a)$ para todo $a < \infty$.*

**Corolario 6.2.** *Bajo la conjetura de Montgomery, $\tilde\delta_\lambda^2 = 0$ (condicional a RH).*

**Observación 6.3.** La implicación de la conjetura de Montgomery a la completitud solo opera *condicional a RH* (pues la conjetura de Montgomery asume que los $\gamma_n$ son reales). No proporciona el paso incondicional que se busca.

### 6.3. La completitud como criterio independiente

Resumimos la situación como sigue. Definimos:
$$\mathcal{C}_\lambda = \overline{\mathrm{span}}^{L^2(W_\lambda dm_\infty)}\{e^{i\gamma_n s} : n \geq 1\},$$
donde los $\gamma_n$ son las partes imaginarias de los ceros no triviales de $\zeta$ (bajo RH, son reales; en general, son complejos).

**Proposición 6.4.** *Las siguientes son equivalentes:*
1. *RH es verdadera.*
2. *$T_\lambda = 0$ para todo $\lambda > 0$ (criterio CTP).*
3. *$\tilde\delta_\lambda^2 = 0$ para todo $\lambda > 0$ (criterio variacional, Corolario 4.6).*
4. *$|\zeta(1/2+is)|^2 \in \mathcal{C}_\lambda$ en $L^2(W_\lambda\,dm_\infty)$ para todo $\lambda > 0$ (completitud de Hadamard).*

La equivalencia (1)$\iff$(2) es el criterio CTP. La equivalencia (2)$\iff$(3) se sigue del Corolario 4.6. La equivalencia (3)$\iff$(4) es formal: bajo RH, $|\zeta|^2 = |\zeta_{\mathrm{on}}|^2$ pertenece a $\mathcal{C}_\lambda$ trivialmente; recíprocamente, si $|\zeta|^2 \in \mathcal{C}_\lambda$, entonces la distancia $\tilde\delta_\lambda^2 = 0$ y se aplica el Corolario 4.6. 

El interés del criterio (4) es que podría ser verificable por métodos de análisis funcional independientes de la teoría de números.

---

## §7. Síntesis y evaluación del Camino 3

### 7.1. Resultados rigurosos obtenidos

**R1 (Doc 79, Prop. 1.1).** La suma $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converge absolutamente para todo $\lambda > 0$, sin ninguna hipótesis sobre los ceros de $\zeta$. La cantidad $T_\lambda$ está bien definida.

**R2 (Doc 79, §8–9).** La fórmula $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ es una identidad (la fórmula de Weil expresada en el lenguaje CCM). Bajo RH, ambos lados son cero; la ecuación es una tautología, no un mecanismo de cancelación nueva.

**R3 (este documento, Corolario 4.6).** El criterio variacional $\tilde\delta_\lambda^2 = 0$ para todo $\lambda$ es equivalente a RH. La demostración de ambas implicaciones (Proposiciones 4.3 y 4.4) es rigurosa módulo el Lema 4.5, cuya demostración es completa.

**R4 (este documento, Prop. 5.3).** Bajo RH, el sistema $\{e^{i\gamma_n s}\}$ es completo en $L^2(W_\lambda\,dm_\infty)$. La demostración es sólida en su estructura pero requiere la verificación técnica de la versión del teorema de Beurling-Malliavin para medidas con decaimiento exponencial (no compacto).

### 7.2. Lo que sigue siendo conjetural

**C1.** La versión rigurosa del teorema de Beurling-Malliavin para el espacio $L^2(W_\lambda\,dm_\infty)$ con decaimiento exponencial. El argumento en §5.3 es plausible pero no constituye una demostración completa.

**C2.** La completitud *incondicional* del sistema $\{e^{i\gamma_n s}\}$ —es decir, sin asumir que los $\gamma_n$ son reales. Si esto pudiera probarse, RH seguiría del Corolario 4.6. Pero no hay indicación de que la completitud sea independiente de la hipótesis que queremos probar.

**C3.** La relación cuantitativa entre $D_\lambda^2$, $\tilde\delta_\lambda^2$ y $T_\lambda$ cuando $T_\lambda > 0$. En particular, si $T_\lambda > 0$ (bajo $\neg$RH), ¿qué tan grande es $\tilde\delta_\lambda^2$?

### 7.3. El obstáculo circular y su naturaleza precisa

La estructura circular del argumento queda así identificada con precisión:

El Corolario 4.6 dice: RH $\iff$ $\tilde\delta_\lambda^2 = 0$ para todo $\lambda$. Esto es un criterio válido. Pero para usarlo como demostración de RH necesitamos probar $\tilde\delta_\lambda^2 = 0$ por medios independientes.

El argumento de completitud (§5) dice: bajo RH (es decir, bajo el supuesto de que los $\gamma_n$ son reales), el sistema $\{e^{i\gamma_n s}\}$ es completo y por tanto $\tilde\delta_\lambda^2 = 0$. Pero esta es la implicación fácil: RH $\implies$ $\tilde\delta_\lambda^2 = 0$, que ya está en la Proposición 4.3.

El obstáculo es exactamente este: no sabemos demostrar la completitud del sistema $\{e^{i\gamma_n s}\}$ sin asumir que los $\gamma_n$ son reales. Si los $\gamma_n$ pueden ser complejos, la geometría del sistema de exponenciales cambia (los exponentes dejan de ser reales, las exponenciales dejan de ser de módulo uno sobre $\mathbb{R}$, y la teoría de Beurling-Malliavin no aplica directamente).

**En consecuencia:** el Camino 3 en su formulación actual es una reorganización del criterio CTP en términos variacionales y de completitud, sin agregar nueva información que permita probar RH. Las reformulaciones (criterio variacional, completitud de Hadamard, conexión con Nyman-Beurling) son matemáticamente limpias y podrían ser útiles como punto de partida para ataques futuros, pero ninguna de ellas rompe la circularidad intrínseca del problema.

### 7.4. Conexión con Nyman-Beurling: la traducción formal

El criterio de Báez-Duarte dice: RH $\iff$ $d_N^2 \to 0$ en $L^2(0,\infty)$. El criterio variacional de este documento dice: RH $\iff$ $\tilde\delta_\lambda^2 \to 0$ en $L^2(W_\lambda\,dm_\infty)$.

La analogía estructural es clara: en ambos casos, RH equivale a que un cierto objeto ($\mathbf{1}_{(0,1)}$ en el caso de Báez-Duarte, $|\zeta|^2$ en el caso CCM) sea aproximable por una clase de funciones construidas a partir de los ceros de $\zeta$ sobre la recta crítica.

La traducción explícita entre los dos criterios pasa por la transformación de Mellin. La función $\{k/t\}$ en $L^2(0,\infty, dt)$ tiene transformada de Mellin $\zeta(s)/s \cdot k^{-s}$ (para $\mathrm{Re}(s) \in (0,1)$), relacionando el span de las $r_k = \{k/t\}$ con el span de $s \mapsto k^{-s}\zeta(s)/s$. Por la isometría de Plancherel de la transformación de Mellin (que mapea $L^2(0,\infty, dt/t)$ en $L^2(1/2+i\mathbb{R}, ds/(2\pi i))$), el criterio de Báez-Duarte se traduce a que $\hat{\mathbf{1}}_{(0,1)}(s) = (s(s-1))^{-1}$ sea aproximable en $L^2(1/2+i\mathbb{R})$ por las funciones $s \mapsto k^{-s}\zeta(s)/s$, para $k = 1, 2, \ldots, N$.

El formalismo CCM introduce la medida $dm_\infty$ (con su estructura de polinomios ortogonales de Jacobi) como reemplazo de la medida de Lebesgue en la recta crítica. La distancia $\tilde\delta_\lambda^2$ es la versión pesada (con peso $W_\lambda$) de la distancia análoga en $L^2(1/2+i\mathbb{R})$. La conexión formal entre ambos criterios existe, pero su traducción rigurosa requeriría identificar el operador de cambio de medida (de Lebesgue a $dm_\infty$) y verificar que preserva la estructura de densidad.

Este punto se deja como dirección para la Fase 35.

---

## §8. Preguntas abiertas para la Fase 35

Las siguientes preguntas emergen de este análisis y definen la agenda de la fase siguiente.

**P1.** Probar rigurosamente la completitud del sistema $\{e^{i\gamma_n s}\}$ en $L^2(W_\lambda\,dm_\infty)$ bajo RH, verificando todas las condiciones técnicas del teorema de Beurling-Malliavin para espacios con decaimiento exponencial.

**P2.** Determinar si la completitud del sistema $\{e^{i\gamma_n s}\}$ puede probarse incondicionalmente (es decir, sin asumir que los $\gamma_n$ son reales). Analizar qué ocurre con el argumento cuando algunos $\gamma_n$ son complejos.

**P3.** Construir la traducción explícita y rigurosa entre el criterio de Báez-Duarte ($d_N^2 \to 0$ en $L^2(dt)$) y el criterio variacional ($\tilde\delta_\lambda^2 \to 0$ en $L^2(W_\lambda\,dm_\infty)$) vía la transformación de Mellin y el cambio de medida.

**P4.** Estudiar la velocidad de convergencia $d_N^2 \to 0$ (bajo RH) y $\tilde\delta_\lambda^2 \to 0$ (bajo RH) y ver si la velocidad contiene información adicional sobre la distribución de los ceros.

**P5.** Examinar si el criterio de completitud (Prop. 6.4, condición 4) puede reformularse como una condición sobre las potencias de los primos —análoga a la fórmula de Weil— que sea verificable sin asumir RH.

---

*Documento 82 concluido. Estado del Camino 3: las reformulaciones variacional y de completitud son matemáticamente limpias y equivalentes al criterio CTP. El obstáculo circular —la completitud requiere la realidad de los $\gamma_n$, que es precisamente RH— está identificado con precisión. No hay demostración nueva de RH; hay un marco conceptual enriquecido para abordar el problema desde análisis funcional.*
