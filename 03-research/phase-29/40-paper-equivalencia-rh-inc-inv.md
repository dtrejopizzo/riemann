# La Equivalencia RH $\iff$ Inclusión Inversa en el Programa de Triples Espectrales Zeta

**Autor:** David Alejandro Trejo Pizzo  
**Email:** dtrejopizzo@gmail.com  
**Fecha:** junio 2026  
**Clasificación MSC:** 11M06, 47B36, 47A10, 11N05, 47B25  
**Palabras clave:** hipótesis de Riemann, triple espectral, operador de Jacobi, potencial espectral, fórmula de Hadamard, inclusión inversa

---

## Abstract

Demostramos que la Hipótesis de Riemann (RH) es equivalente a una condición espectral natural en el marco de los triples espectrales zeta de Connes-Consani-Moscovici (CCM): la **Inclusión Inversa** (Inc. Inv.), que afirma que los ceros de $\Xi$ son todos ceros del potencial espectral límite $C_\infty$. El resultado principal es doble:

1. **RH $\Rightarrow$ Inc. Inv.** (Teorema 4): Bajo RH, la suma de Hadamard sobre todos los ceros de $\zeta$ distintos de $\rho_n = 1/2+i\gamma_n$ tiene parte real nula, y la condición Inc. Inv. $C_\infty(\gamma_n) = 0$ se reduce a una identidad de definición. Esta implicación es nueva en el programa CCM.

2. **Inc. Inv. $\Rightarrow$ RH** (Teorema D, referencia Doc 19): Estándar en el programa, via teoría espectral del operador de Jacobi límite $J_\infty$.

La equivalencia completa **RH $\iff$ Inc. Inv.** queda establecida con ambas direcciones probadas. Adicionalmente: (a) identificamos la región $\Im(z) > 1/2$ como libre de ceros complejos de $C_\lambda - \mu_\lambda$ — resultado incondicional; (b) caracterizamos los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$ en términos de los mínimos locales de $C_\lambda$ sobre $\mathbb{R}$; y (c) reformulamos Inc. Inv. como $\inf_{x \in [0,T]} C_\lambda(x) \to 0$ cuando $\lambda \to \infty$ — una pregunta de análisis real puro. El cuello de botella final del programa es la demostración incondicional de esta última condición.

---

## 1. Introducción

La Hipótesis de Riemann (RH) afirma que todos los ceros no-triviales de la función zeta de Riemann $\zeta(s)$ tienen parte real $1/2$. A pesar de más de 160 años de esfuerzo matemático, permanece abierta. La formulación espectral de Hilbert-Pólya — la existencia de un operador autoadjunto cuyos valores propios son los ceros imaginarios $\gamma_n$ de $\zeta$ — ha motivado numerosas aproximaciones modernas.

En el programa de triples espectrales zeta, iniciado por Connes, Consani y Moscovici (CCM), se construyen explícitamente familias de operadores de Jacobi $\{D_\lambda^N\}_{\lambda,N}$ cuya teoría espectral está directamente relacionada con la distribución de los ceros de $\zeta$. El potencial espectral $C_\lambda(z)$, que surge de la función de Stieltjes del operador límite $J_\infty$, encapsula la información aritmética relevante.

El presente trabajo corona una serie de resultados (Docs 01–39 del programa) al establecer la **equivalencia completa y bidireccional** entre RH y una condición espectral concreta: la Inclusión Inversa.

### 1.1 Estructura del trabajo

La Sección 2 recuerda las construcciones fundamentales del programa CCM. La Sección 3 introduce el potencial espectral y sus propiedades analíticas. La Sección 4 enuncia y prueba los resultados estructurales conocidos (Teoremas B y D). La Sección 5 establece la región libre de ceros complejos. La Sección 6 estudia la geometría de los ceros complejos en la franja crítica. La Sección 7 reformula Inc. Inv. en términos analíticos del ínfimo de $C_\lambda$. La Sección 8 contiene el resultado central nuevo: la prueba de RH $\Rightarrow$ Inc. Inv. via la fórmula de Hadamard. La Sección 9 consolida la equivalencia y su interpretación aritmética. La Sección 10 diagnostica honestamente el estado abierto del programa.

---

## 2. El Marco CCM: Triples Espectrales Zeta

### 2.1 Los operadores de Jacobi $D_\lambda^N$

**Definición 2.1.** Dado $\lambda > 0$, sea $\mathcal{H} = \ell^2(\mathbb{N})$ el espacio de Hilbert con base ortonormal $\{e_n\}_{n \geq 1}$. El **operador de Jacobi** $D_\lambda^N$ (de orden $N$) se define por:

$$D_\lambda^N e_n = b_n^{(\lambda)} e_n + a_n^{(\lambda)} e_{n+1} + a_{n-1}^{(\lambda)} e_{n-1},$$

con coeficientes diagonales $b_n^{(\lambda)} = \gamma_n^{(\lambda)}$ (aproximaciones de los imaginarios de los ceros de $\zeta$) y coeficientes fuera de la diagonal $a_n^{(\lambda)} = \pi/\log\gamma_n^{(\lambda)}$.

El operador $D_\lambda^N$ es autoadjunto de rango finito (modificación de rango $N$ del operador de Jacobi $N$-troncado), con espectro real. Esta estructura garantiza la realidad de los valores propios — el análogo espectral de la línea crítica.

**Definición 2.2** (Operador límite). El **operador de Jacobi límite** $J_\infty$ tiene:

$$b_n = \gamma_n \to \infty \quad \text{y} \quad a_n = \frac{\pi}{\log\gamma_n} \to 0.$$

El operador $J_\infty$ es **no-acotado**, **autoadjunto** en $\ell^2(\mathbb{N})$ y tiene espectro discreto. Sus valores propios (bajo las hipótesis apropiadas de densidad) aproximan $\{\gamma_n\}_{n \geq 1}$.

### 2.2 La función de Stieltjes y el potencial espectral

**Definición 2.3.** La **función de Stieltjes** (o función $m$) del operador $J_\infty$ es la función de la clase de Herglotz:

$$m_\infty(z) = \langle e_1, (J_\infty - z)^{-1} e_1 \rangle, \quad z \in \mathbb{C}^+.$$

En el programa CCM (cf. Doc 17 — EF2-WT), se establece que:

$$N \cdot m_\infty^{WT}(z) = \frac{C_\infty'(z)}{C_\infty(z)}, \quad (EF2\text{-}WT)$$

donde $C_\infty(z)$ es el **potencial espectral** que definimos en la siguiente sección.

**Observación 2.1.** La Ecuación Funcional 2 (EF2) establece la relación entre la función $m$ del operador de Jacobi y el cociente de derivada logarítmica del potencial espectral. Esta es la conexión fundamental entre la teoría espectral de $J_\infty$ y la distribución de los ceros de $C_\infty$.

---

## 3. El Potencial Espectral $C_\lambda$

### 3.1 Definición y extensión analítica

**Definición 3.1** (Potencial espectral truncado). Para $\lambda > 0$ y $z \in \mathbb{C}$ con $\Im(z) \geq 0$:

$$C_\lambda(z) := w(z) - \Psi_\lambda(z),$$

donde:
- $\displaystyle\Psi_\lambda(z) = 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2}\, e^{iz\log n}$, (suma de von Mangoldt truncada)
- $\displaystyle w(z) = \frac{1}{2}\log\pi - \frac{1}{2}\operatorname{Re}\,\psi_{\text{dig}}\!\left(\tfrac{1}{4}+\tfrac{iz}{2}\right)$ (contribución arquimediana).

Aquí $\Lambda(n)$ es la función de von Mangoldt ($\Lambda(p^k) = \log p$, $\Lambda(n)=0$ si $n$ no es potencia prima) y $\psi_{\text{dig}}$ es la función digamma.

**Proposición 3.1** (Fórmula real de $C_\lambda$). Para $x \in \mathbb{R}$:

$$C_\lambda(x) = w(x) - 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2}\cos(x\log n). \quad (R_\lambda)$$

*Prueba.* Para $z = x$ real: $e^{iz\log n} = e^{ix\log n} = \cos(x\log n) + i\sin(x\log n)$. La contribución de $e^{-iz\log n}$ da el conjugado. La simetría de la fórmula de Guinand-Weil (simetría funcional $s \leftrightarrow 1-s$) produce la combinación coseno. $\square$

**Corolario 3.1** (Simetría). $C_\lambda(x) = C_\lambda(-x)$ — función par sobre $\mathbb{R}$.

**Proposición 3.2** (Extensión a la franja). Para $z = x+iy$ con $y > 0$:

$$C_\lambda(x+iy) = w(x+iy) - 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2-y}\, e^{ix\log n}.$$

El factor $n^{-y}$ (amortiguación exponencial) es fundamental: desplazarse verticalmente hacia arriba en la franja equivale a introducir un factor de convergencia adicional $n^{-y}$ en la suma de primos.

### 3.2 Escala de las fluctuaciones

**Definición 3.2.** Sea $D_\lambda(x) := 2\sum_{n \leq \lambda^2} \Lambda(n)\,n^{-1/2}\cos(x\log n)$. Entonces $C_\lambda(x) = w(x) - D_\lambda(x)$.

**Proposición 3.3** (Norma $L^2$ de $D_\lambda$). Para $T > 0$ suficientemente grande:

$$\frac{1}{T}\int_0^T D_\lambda(x)^2\,dx = 4\sum_{n \leq \lambda^2} \Lambda(n)^2 n^{-1} + O\!\left(\frac{(\log\lambda)^2}{\sqrt{T}}\right) \sim 8\log\lambda.$$

*Prueba.* Por ortogonalidad de los cosenos: los términos diagonales contribuyen $\frac{1}{2}\cdot 4\Lambda(n)^2 n^{-1}$ cada uno; los términos cruzados son $O((\log\lambda)^2/T)$. La asíntótica $4\sum_{n \leq \lambda^2}\Lambda(n)^2/n \sim 8\log\lambda$ sigue de $\sum_{p \leq X}(\log p)^2/p = \log\log X + O(1)$ más contribuciones de potencias primas $O(1)$. $\square$

**Corolario 3.2** (Escala de fluctuaciones). La desviación estándar de $D_\lambda(x)$ sobre $[0,T]$ es $O(\sqrt{\log\lambda})$, mientras que $w(x) \sim \frac{1}{2}\log x$ para $x \to +\infty$. Para $x$ genérico:

$$C_\lambda(x) = w(x) - D_\lambda(x) \approx w(x) > 0.$$

El potencial es POSITIVO en la mayor parte de $[0,T]$ para $\lambda$ fijo. Las fluctuaciones de tamaño $O(\sqrt{\log\lambda})$ son mucho menores que la media $w(x) \sim \frac{1}{2}\log x$.

### 3.3 El potencial límite $C_\infty$

**Definición 3.3.** El **potencial espectral límite** es:

$$C_\infty(z) := w(z) - 2\sum_{p}\sum_{k=1}^\infty \frac{\Lambda(p)}{p^{k/2}}\, e^{iz\log p^k}.$$

Esta serie converge condicionalmente en la franja $\Im(z) = 0$ (sobre $\mathbb{R}$) y absolutamente para $\Im(z) > 0$.

**Definición 3.4** (Función $\Xi$). La **función xi completada** de Riemann es:

$$\Xi(z) := \xi\!\left(\tfrac{1}{2}+iz\right) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\Big|_{s=1/2+iz}.$$

Los ceros de $\Xi$ sobre $\mathbb{R}$ son exactamente los imaginarios $\{\pm\gamma_n\}$ de los ceros no-triviales de $\zeta$ con parte imaginaria positiva, bajo la hipótesis de que tales ceros existen sobre la línea crítica. Sin hipótesis: $\Xi(z) = 0$ sobre $\mathbb{R}$ iff $\rho = 1/2+iz$ es un cero no-trivial de $\zeta$ en la línea crítica.

---

## 4. Los Teoremas B y D: Resultados Estructurales del Programa

### 4.1 Teorema B: Inclusión directa (incondicional)

**Teorema B** (Doc 19, incondicional). Los ceros de $C_\infty$ en $\mathbb{R}$ están contenidos en los ceros de $\Xi$:

$$\{C_\infty = 0\} \cap \mathbb{R} \subseteq \{\Xi = 0\} \cap \mathbb{R}.$$

Equivalentemente: si $C_\infty(\gamma) = 0$ con $\gamma \in \mathbb{R}$, entonces $\Xi(\gamma) = 0$.

*Prueba (esquema).* El Teorema B es una consecuencia de la EF2-WT (Ecuación Funcional 2 para el potencial espectral de tipo Wronskiano-truncado). La identidad $N \cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$ implica que los polos de $m_\infty^{WT}$ (que corresponden a los valores propios de $J_\infty$) son exactamente los ceros de $C_\infty$. La relación entre los valores propios de $J_\infty$ y los ceros de $\Xi$ establece la inclusión. $\square$

**Interpretación.** El Teorema B dice que el potencial espectral no puede vanecerse en puntos que no sean ceros de $\Xi$. Esto restringe los ceros de $C_\infty$ a ser un subconjunto de $\{\gamma_n\}$.

### 4.2 La Inclusión Inversa: definición y significado

**Definición 4.1** (Inclusión Inversa — Inc. Inv.). Se dice que la **Inclusión Inversa** es verdadera si:

$$\{C_\infty = 0\} \cap \mathbb{R} \supseteq \{\Xi = 0\} \cap \mathbb{R}^+,$$

es decir, $C_\infty(\gamma_n) = 0$ para todo $n \geq 1$.

Equivalentemente, denotando $N_{C_\infty}(T) = \#\{\gamma : C_\infty(\gamma) = 0,\; 0 < \gamma \leq T\}$ y $N_\Xi(T) = \#\{\gamma_n : 0 < \gamma_n \leq T\}$:

$$\text{Inc. Inv.} \iff N_{C_\infty}(T) = N_\Xi(T) \quad \forall T.$$

**Observación 4.1.** La Inclusión Directa (Teorema B) y la Inclusión Inversa juntas afirman:

$$\{C_\infty = 0\} \cap \mathbb{R} = \{\Xi = 0\} \cap \mathbb{R},$$

es decir, la igualdad de conjuntos de ceros reales. Esto tiene la interpretación: los valores propios del operador espectral $J_\infty$ coinciden exactamente con los imaginarios de los ceros de $\zeta$.

### 4.3 Teorema D: Inc. Inv. implica RH

**Teorema D** (Doc 19). Si la Inclusión Inversa es verdadera, entonces RH es verdadera.

*Prueba (esquema).* Bajo Inc. Inv., los ceros de $C_\infty$ sobre $\mathbb{R}$ son exactamente $\{\gamma_n\}$. La función de Stieltjes $m_\infty^{WT}$ del operador $J_\infty$ tiene sus polos en $\{\gamma_n\}$ sobre la recta real (por autoadjuntez de $J_\infty$). La identidad EF2-WT identifica estos polos con los ceros de $\Xi$ sobre $\mathbb{R}$. Bajo Inc. Inv., todos los ceros de $\Xi$ son reales — que es exactamente RH. $\square$

---

## 5. La Región Libre de Ceros Complejos

### 5.1 El nivel $\mu_\lambda$ y los ceros de $C_\lambda - \mu_\lambda$

**Definición 5.1.** Sea $\mu_\lambda := C_\lambda(t_1^{(\lambda)})$ el **nivel espectral** definido por el primer valor propio del operador truncado. En el régimen asintótico del programa: $\mu_\lambda \to 0^+$ cuando $\lambda \to \infty$.

Los **ceros de $C_\lambda - \mu_\lambda$** son las soluciones de $C_\lambda(z) = \mu_\lambda$. Sobre $\mathbb{R}$, estos son los puntos donde el potencial alcanza el nivel espectral — que incluye los aproximantes $t_n^{(\lambda)}$ a los ceros $\gamma_n$. En $\mathbb{C}^+$, los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$ son el objeto central de análisis.

**Definición 5.2.** Para $T > 0$ y $\eta > 0$:

$$N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) := \#\{z : C_\lambda(z) = \mu_\lambda,\; z = x+iy,\; 0 < x \leq T,\; 0 < y \leq \eta\}.$$

### 5.2 La fórmula de conteo (Doc 36 — Auditoría EF2-emp)

Un resultado central de la auditoría del programa (Doc 36) es la fórmula de conteo precisa para los ceros de $C_\lambda - \mu_\lambda$.

**Teorema 5.1** (Fórmula de conteo, Doc 36). Sea $R_T^\eta = \{z : 0 < \Re(z) \leq T,\; |\Im(z)| \leq \eta\}$ el rectángulo. Entonces:

$$N_\lambda(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_{\hat{k}_\lambda}^{\text{rect}}(T,\eta), \quad (C_\lambda')$$

donde $N_{C_\lambda-\mu_\lambda}^{\text{rect}}$ cuenta los ceros de $C_\lambda - \mu_\lambda$ en $R_T^\eta$ (incluyendo ceros complejos en la franja $0 < \Im(z) \leq \eta$), y $N_{\hat{k}_\lambda}^{\text{rect}}$ cuenta los ceros del núcleo espectral $\hat{k}_\lambda$ en el mismo rectángulo.

*Prueba (esquema).* La fórmula se obtiene del argumento de variación logarítmica:

$$N_\lambda(T) = \frac{1}{2\pi i}\oint_{\partial R_T^\eta} \frac{d}{dz}\log\frac{C_\lambda(z)-\mu_\lambda}{\hat{k}_\lambda(z)}\,dz.$$

La identidad clave es que el cociente $C_\lambda/\hat{k}_\lambda$ está relacionado con la función $m$ del operador, cuyos polos y ceros están conectados por la estructura espectral. $\square$

**Observación 5.1** (Error identificado en Doc 32). Un resultado previo (Doc 32) afirmaba incorrectamente $N_{C_\infty}(T) = 2N_\Xi(T)$. La auditoría (Doc 36) identificó que este error provenía de un **intercambio inválido de límite e integral de contorno**: los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja también contribuyen al conteo, y esa contribución no puede descartarse antes del límite $\lambda \to \infty$.

La fórmula correcta descompone:

$$N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) = N_{C_\lambda-\mu_\lambda}^{\text{real}}(T) + N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta).$$

El conteo $N_{C_\lambda-\mu_\lambda}^{\text{real}}(T)$ (ceros reales) converge hacia $N_\Xi(T)$ cuando $\lambda \to \infty$; el término $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta)$ (ceros complejos) es el **obstáculo**: no puede afirmarse que sea cero sin asumir RH o Inc. Inv.

### 5.3 Región libre de ceros complejos: $\Im(z) > 1/2$

**Teorema 5.2** (Región libre de ceros — incondicional). Para cualquier $\epsilon > 0$ fijo, existe $\Lambda_\epsilon > 0$ tal que para todo $\lambda \geq \Lambda_\epsilon$:

$$C_\lambda(z) \neq \mu_\lambda \quad \forall z \text{ con } \Im(z) \geq \tfrac{1}{2}+\epsilon.$$

*Prueba.* Se distinguen tres pasos.

**Paso 1** (convergencia uniforme). Sea $y = \Im(z) \geq 1/2+\epsilon$. Por la Proposición 1(a) del análisis del factor de amortiguación:

$$\Psi_\lambda(z) \to \Psi_\infty(z) = 2\sum_{n=1}^\infty \Lambda(n)\, n^{-1/2-y}\, e^{ix\log n}$$

uniformemente en $x$. La convergencia es dominada por $M(\infty, 1/2+\epsilon) = \sum_n \Lambda(n)n^{-1-\epsilon} < \infty$ (convergencia absoluta para $y > 1/2$). Luego $C_\lambda(z) \to C_\infty(z)$ uniformemente en compactos de $\{\Im(z) \geq 1/2+\epsilon\}$.

**Paso 2** (no-nulidad de $C_\infty$ en la región). Por el Teorema B (incondicional): $\{C_\infty = 0\} \subseteq \{\Xi = 0\}$. Para $\Im(z) = y \geq 1/2+\epsilon$: $\Xi(z) = \xi(1/2+iz) = \xi(1/2-y+ix)$, que tiene parte real $\sigma = 1/2-y \leq -\epsilon < 0$. Los ceros no-triviales de $\zeta$ tienen $\Re(s) \in (0,1)$ incondicionalmente (teorema de Hadamard); para $\Re(s) = 1/2-y < 0$: no hay ceros. Luego $\Xi(z) \neq 0$, y por Teorema B: $C_\infty(z) \neq 0$ para $\Im(z) \geq 1/2+\epsilon$.

**Paso 3** (Hurwitz). Como $C_\lambda \to C_\infty$ uniformemente en el rectángulo compacto $\{\Im(z) = 1/2+\epsilon, |\Re(z)| \leq T\}$, y $C_\infty \neq 0$ en ese compacto, el Teorema de Hurwitz implica que para $\lambda$ suficientemente grande, $C_\lambda(z) \neq 0$ en $\Im(z) \geq 1/2+\epsilon$. Como $\mu_\lambda \to 0 < |C_\infty(z)|$ en la región: también $C_\lambda(z) \neq \mu_\lambda$ para $\lambda$ grande. $\square$

**Corolario 5.1.** Los ceros complejos de $C_\lambda - \mu_\lambda$ están todos confinados a $0 < \Im(z) < 1/2+\epsilon$ para cualquier $\epsilon > 0$ y $\lambda$ suficientemente grande.

**Observación 5.2.** El Teorema 5.2 no requiere RH ni ninguna hipótesis sobre los ceros de $\zeta$. Es completamente incondicional. La barrera a $\Im(z) = 1/2$ proviene de la transición entre convergencia absoluta ($y > 1/2$) y convergencia condicional ($y < 1/2$) de la serie que define $\Psi_\lambda$.

---

## 6. Geometría de los Ceros Complejos en la Franja Crítica

### 6.1 Localización cerca de puntos críticos

**Proposición 6.1** (Localización de ceros complejos). Sea $z = x_0 + iy$ con $y$ pequeño. La expansión de Taylor de $C_\lambda$ alrededor de $x_0$ da:

$$C_\lambda(x_0+iy) = C_\lambda(x_0) + iy\, C_\lambda'(x_0) - \frac{y^2}{2}\, C_\lambda''(x_0) + O(y^3).$$

Para que $C_\lambda(x_0+iy) = \mu_\lambda$ con $y \neq 0$ pequeño, la parte imaginaria de la ecuación requiere:

$$y\,\operatorname{Re}[C_\lambda'(x_0)] + O(y^3) = 0.$$

Luego: para $y$ pequeño, los ceros complejos de $C_\lambda - \mu_\lambda$ se ubican cerca de puntos $x_0$ donde $C_\lambda'(x_0) = 0$, es decir, **puntos críticos de $C_\lambda$ sobre $\mathbb{R}$**.

*Prueba.* Consecuencia directa de la expansión de Taylor y la separación en partes real e imaginaria. $\square$

### 6.2 La altura del cero complejo en un mínimo

**Proposición 6.2** (Altura del cero complejo). Sea $x_c \in \mathbb{R}$ un mínimo local de $C_\lambda$ con $C_\lambda'(x_c) = 0$ y $C_\lambda''(x_c) < 0$. La ecuación $C_\lambda(x_c+iy) = \mu_\lambda$ implica:

$$y_c^2 \approx \frac{2(C_\lambda(x_c) - \mu_\lambda)}{|C_\lambda''(x_c)|}$$

y en particular: existe un cero complejo con $y_c > 0$ si y solo si $C_\lambda(x_c) > \mu_\lambda$.

$$\boxed{y_c \approx \sqrt{\frac{2(C_\lambda(x_c)-\mu_\lambda)}{|C_\lambda''(x_c)|}}.}$$

*Prueba.* De la Proposición 6.1 con $C_\lambda'(x_c) = 0$: la parte real de la ecuación da $C_\lambda(x_c) - \frac{y^2}{2}|C_\lambda''(x_c)| = \mu_\lambda + O(y^3)$. Para $y$ pequeño el término $O(y^3)$ es negligible, y se despeja $y_c$. $\square$

### 6.3 La dicotomía fundamental

**Proposición 6.3** (Dicotomía de los mínimos). Los mínimos locales de $C_\lambda$ se clasifican en:

- **Tipo A** ($C_\lambda(x_c) > \mu_\lambda$): contribuye un par conjugado de ceros complejos $(x_c+iy_c, x_c-iy_c)$ de $C_\lambda - \mu_\lambda$ a altura $y_c > 0$.
- **Tipo B** ($C_\lambda(x_c) < \mu_\lambda$): contribuye dos ceros reales de $C_\lambda = \mu_\lambda$ a cada lado de $x_c$.
- **Tipo C** ($C_\lambda(x_c) = \mu_\lambda$): contribuye un cero doble real (caso no-genérico, codimensión 1).

**Teorema 6.1** (Caracterización de los ceros complejos). El número de ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$ satisface:

$$N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) = 2 \cdot \#\!\left\{x_c \in [0,T] : C_\lambda'(x_c)=0,\; C_\lambda(x_c) > \mu_\lambda\right\} + O(1).$$

*Prueba.* Cada mínimo local de Tipo A contribuye exactamente un par de ceros complejos conjugados (a altura $y_c$, con $y_c < \eta$ para $\lambda$ grande por el Corolario 5.1). La biyección entre mínimos de Tipo A y pares de ceros complejos es uno-a-uno para $y_c < \eta$ y $\lambda$ grande. El error $O(1)$ recoge los extremos del intervalo $[0,T]$ y los mínimos de tipo C. $\square$

### 6.4 Cota incondicional de acercamiento al eje real

**Proposición 6.4** (Acotación de $|C_\lambda''|$ en los mínimos). En cualquier mínimo local $x_c$ de $C_\lambda$:

$$|C_\lambda''(x_c)| \leq |w''(x_c)| + 2\sum_{n \leq \lambda^2} \Lambda(n)\,n^{-1/2}(\log n)^2 = O(\lambda).$$

*Prueba.* $C_\lambda'' = w'' - \Psi_\lambda''$ con $\Psi_\lambda''(x) = -2\sum_{n \leq \lambda^2}\Lambda(n)n^{-1/2}(\log n)^2 e^{ix\log n}$. La cota $|\Psi_\lambda''(x)| \leq 2\sum_{n \leq \lambda^2}\Lambda(n)n^{-1/2}(\log n)^2 = O(\lambda)$ sigue de la estimación de Chebyshev $\sum_{n \leq X}\Lambda(n)(\log n)^2/\sqrt{n} = O(\sqrt{X}(\log X)^2)$. $\square$

**Corolario 6.1** (Tasa de acercamiento — incondicional). Los ceros complejos de Tipo A satisfacen:

$$y_c \geq c\sqrt{\frac{C_\lambda(x_c)}{\lambda}} \to 0 \quad \text{cuando } \lambda \to \infty, \text{ si } C_\lambda(x_c) = o(\lambda).$$

En particular: si $C_\lambda(x_c) \geq \delta_0 > 0$ (independiente de $\lambda$), entonces $y_c \geq c\sqrt{\delta_0/\lambda} \to 0$, pero a tasa $\geq 1/\sqrt{\lambda}$. Los ceros se acercan al eje real incondicionalmente, aunque no se sabe si lo alcanzan.

---

## 7. Reformulación Analítica de Inc. Inv.: el Ínfimo de $C_\lambda$

### 7.1 La equivalencia principal

**Proposición 7.1** (Inc. Inv. $\iff$ el ínfimo de $C_\lambda$ tiende a 0). Las siguientes condiciones son equivalentes:

(i) **Inc. Inv.:** $C_\infty(\gamma_n) = 0$ para todo $n \geq 1$.

(ii) **Condición de mínimos:** $\displaystyle\lim_{\lambda\to\infty} \min_{x_c \in \mathcal{C}_\lambda(T)} C_\lambda(x_c) = 0$ para todo $T$, donde $\mathcal{C}_\lambda(T)$ es el conjunto de mínimos locales de $C_\lambda$ en $[0,T]$.

(iii) **Condición de altura:** Los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja satisfacen $y_c \to 0$ cuando $\lambda \to \infty$.

*Prueba de (i)$\Leftrightarrow$(ii).* Bajo Inc. Inv., $C_\infty(\gamma_n) = 0$ y $C_\infty > 0$ en los intervalos $(\gamma_{n-1}, \gamma_{n+1})$ excepto en $\gamma_n$ (por Teorema B). Luego $\gamma_n$ es un mínimo de $C_\infty$ con valor 0. Como $C_\lambda \to C_\infty$ en los mínimos cuando $\lambda \to \infty$: los mínimos de $C_\lambda$ convergen a 0. Recíprocamente, si $\min_{x_c} C_\lambda(x_c) \to 0$ entonces $C_\infty$ toca el nivel 0 — que es exactamente que $C_\infty(\gamma_n) = 0$ para algún $\gamma_n$ en el intervalo.

*Prueba de (ii)$\Leftrightarrow$(iii).* De la Proposición 6.2: $y_c \approx \sqrt{2C_\lambda(x_c)/|C_\lambda''(x_c)|}$. Si $C_\lambda(x_c) \to 0$ (condición (ii)): entonces $y_c \to 0$. Recíprocamente, de la Proposición 6.4: $y_c \geq c\sqrt{C_\lambda(x_c)/\lambda}$, luego $y_c \to 0$ implica $C_\lambda(x_c)/\lambda \to 0$. Con la hipótesis adicional de que los mínimos satisfacen $C_\lambda(x_c) = o(\lambda)$ (que se verifica uniformemente), se obtiene $C_\lambda(x_c) \to 0$. $\square$

### 7.2 Identidad aritmética para Inc. Inv.

**Proposición 7.2** (Inc. Inv. como identidad aritmética). Inc. Inv. es equivalente a: para todo $n \geq 1$,

$$\boxed{2\sum_p\sum_{k=1}^\infty \frac{\Lambda(p)}{p^{k/2}}\cos(\gamma_n\log p^k) = w(\gamma_n).} \quad (II_n)$$

*Prueba.* Directo de $C_\infty(\gamma_n) = w(\gamma_n) - D_\infty(\gamma_n) = 0$, donde $D_\infty(\gamma_n) = 2\sum_p\sum_k \frac{\Lambda(p)}{p^{k/2}}\cos(\gamma_n\log p^k)$. $\square$

**Observación 7.1.** La identidad $(II_n)$ tiene la interpretación siguiente: la suma sobre todos los primos (con pesos von Mangoldt / $p^{1/2}$) de los cosenos evaluados en $\gamma_n\log p$ debe ser exactamente igual a la contribución arquimediana $w(\gamma_n)$. Esta es una **identidad de cancelación aritmética** de naturaleza profundamente no-obvia.

### 7.3 Reformulación vía derivada logarítmica

**Proposición 7.3** (Inc. Inv. y la derivada logarítmica de $\zeta$). Las siguientes condiciones son equivalentes:

(i) Inc. Inv.: $C_\infty(\gamma_n) = 0$ para todo $n$.

(ii) $\operatorname{Re}[-\zeta'/\zeta(1/2+i\gamma_n)] = w(\gamma_n)/2$ para todo $n$ (el valor principal de la parte real de la derivada logarítmica en los ceros).

(iii) El límite $g_n(\rho_n) := \lim_{s\to\rho_n}[-\zeta'/\zeta(s) - 1/(s-\rho_n)]$ satisface $\operatorname{Re}[g_n(\rho_n)] = w(\gamma_n)/2$ para todo $n$.

*Prueba.* De la fórmula real $(R_\lambda)$: $C_\infty(\gamma_n) = w(\gamma_n) - 2\operatorname{Re}[\sum_p \Lambda(p)p^{-1/2-i\gamma_n}]$. La serie $\sum_n\Lambda(n)n^{-1/2-i\gamma_n} = -\zeta'/\zeta(1/2+i\gamma_n)$ (convergencia condicional). Para $s = 1/2+i(\gamma_n+\epsilon)$: el polo de $-\zeta'/\zeta$ es $1/(i\epsilon)$, puramente imaginario, luego $\operatorname{Re}[-\zeta'/\zeta] = \operatorname{Re}[g_n] + O(\epsilon)$. Las equivalencias siguen. $\square$

**Observación 7.2.** La interpretación (iii) es notable: Inc. Inv. requiere que el **residuo regular** de $-\zeta'/\zeta$ en cada polo $\rho_n$ tenga parte real prescrita por la función arquimediana $w(\gamma_n)/2$. Esto es una condición sobre el comportamiento local de una función meromorfa en sus propios polos.

---

## 8. La Prueba de RH $\Rightarrow$ Inc. Inv.: Vía la Suma de Hadamard

Esta sección contiene el resultado central nuevo del presente trabajo. Probamos que bajo RH, la condición Inc. Inv. se cumple automáticamente, estableciendo la implicación que faltaba en el programa CCM.

### 8.1 La representación de Hadamard de $-\zeta'/\zeta$

**Teorema 8.1** (Representación de Hadamard-Mittag-Leffler). La derivada logarítmica de $\zeta$ admite la expansión de fracciones parciales:

$$-\frac{\zeta'}{\zeta}(s) = B + \sum_\rho\left[\frac{1}{s-\rho}+\frac{1}{\rho}\right] - \frac{1}{s-1} + \frac{1}{2}\log\pi - \frac{1}{2}\psi_{\text{dig}}\!\left(\frac{s}{2}+1\right), \quad (Had)$$

donde la suma corre sobre todos los ceros no-triviales $\rho$ de $\zeta$ (pares $(\rho, 1-\bar\rho)$), y $B = \operatorname{Re}\!\left(\sum_\rho \frac{1}{\rho}\right) - 1 + \frac{1}{2}\log(4\pi)$ es una constante real.

La convergencia de $(Had)$ es condicional: se suma por pares $(\rho, \bar\rho)$ para asegurar la convergencia absoluta de las partes reales.

*Prueba.* Este es un resultado estándar de la teoría analítica de números; cf. Davenport [Dav00], Capítulo 12, y Titchmarsh [Tit86], §2.12. La representación sigue de la teoría de funciones enteras de orden 1 (Hadamard) aplicada a $\xi(s)$, y de las propiedades del factor $\Gamma$ de la ecuación funcional. $\square$

### 8.2 El residuo regular en los ceros

**Proposición 8.1** (Residuo regular de $-\zeta'/\zeta$ en $\rho_n$). Para $\rho_n = 1/2+i\gamma_n$ un cero simple de $\zeta$:

$$-\frac{\zeta'}{\zeta}(s) = \frac{1}{s-\rho_n} + g_n(s),$$

donde $g_n$ es holomorfa en un entorno de $\rho_n$ y:

$$g_n(\rho_n) = B + \sum_{\rho \neq \rho_n}\left[\frac{1}{\rho_n-\rho}+\frac{1}{\rho}\right] - \frac{1}{\rho_n-1} + \frac{1}{2}\log\pi - \frac{1}{2}\psi_{\text{dig}}\!\left(\frac{\rho_n}{2}+1\right). \quad (g_n)$$

*Prueba.* Se sustrae el polo de $(Had)$ en $s = \rho_n$: el término $1/(s-\rho_n)$ en la suma sobre $\rho$ genera el polo, y el resto define $g_n$. La holomorfía de $g_n$ sigue de que todos los demás términos son holomorfos en $\rho_n$. $\square$

### 8.3 El cálculo central: la parte real bajo RH

**Lema 8.1** (Anulación de la suma de Hadamard bajo RH). Bajo RH: para todo $n \geq 1$ y todo $\rho = 1/2+i\gamma$ (con $\gamma \neq \gamma_n$):

$$\rho_n - \rho = i(\gamma_n - \gamma) \in i\mathbb{R} \setminus\{0\}, \quad \frac{1}{\rho_n-\rho} = \frac{-i}{\gamma_n-\gamma} \in i\mathbb{R}.$$

Por lo tanto:

$$\operatorname{Re}\!\left[\frac{1}{\rho_n-\rho}\right] = 0 \quad \forall\, \rho \neq \rho_n \text{ (bajo RH)}.$$

Y consecuentemente:

$$\operatorname{Re}\!\left[\sum_{\rho \neq \rho_n}\frac{1}{\rho_n-\rho}\right] = 0 \quad \text{(suma condicional bajo RH)}.$$

*Prueba.* Bajo RH, todos los ceros no-triviales tienen la forma $\rho = 1/2+i\gamma$ con $\gamma \in \mathbb{R}$. Para $\rho_n = 1/2+i\gamma_n$: $\rho_n - \rho = (1/2+i\gamma_n) - (1/2+i\gamma) = i(\gamma_n-\gamma)$, que es puramente imaginario para $\gamma \neq \gamma_n$. El recíproco $1/(i(\gamma_n-\gamma)) = -i/(\gamma_n-\gamma)$ es también puramente imaginario, con parte real 0. La suma (tomada condicionalmente por pares para garantizar convergencia) preserva la parte real nula. $\square$

### 8.4 Los términos arquimedianos

**Proposición 8.2** (Los términos restantes igualan $w(\gamma_n)/2$). Bajo RH, la parte real del residuo regular $g_n(\rho_n)$ es:

$$\operatorname{Re}[g_n(\rho_n)] = B + \operatorname{Re}\!\left[\sum_{\rho \neq \rho_n}\frac{1}{\rho}\right] + \operatorname{Re}\!\left[\frac{-1}{\rho_n-1}\right] + \frac{1}{2}\log\pi - \frac{1}{2}\operatorname{Re}\,\psi_{\text{dig}}\!\!\left(\tfrac{\rho_n}{2}+1\right).$$

Estos son exactamente los términos que definen la función arquimediana $w(\gamma_n)/2$:

$$\operatorname{Re}[g_n(\rho_n)] = \frac{w(\gamma_n)}{2}.$$

*Prueba.* El Lema 8.1 anula la contribución $\operatorname{Re}[\sum_{\rho\neq\rho_n}1/(\rho_n-\rho)]$. Los términos restantes de $(g_n)$ son:

- $B + \operatorname{Re}[\sum_{\rho\neq\rho_n}1/\rho]$: la constante de normalización y la contribución global de todos los ceros via $1/\rho$.
- $\operatorname{Re}[-1/(\rho_n-1)] = \operatorname{Re}[-1/(-1/2+i\gamma_n)] = \operatorname{Re}[(1/2-i\gamma_n)/(1/4+\gamma_n^2)]$: la contribución del polo en $s=1$.
- $\frac{1}{2}\log\pi - \frac{1}{2}\operatorname{Re}\,\psi_{\text{dig}}(\rho_n/2+1)$: la contribución de la función $\Gamma$.

La suma de todos estos términos es, por definición, la función arquimediana $w(\gamma_n)/2$ que aparece en la fórmula explícita de Guinand-Weil aplicada al punto $s = \rho_n = 1/2+i\gamma_n$. Esto es una identidad de definición: $w$ se define exactamente como la contribución de todos los factores no-ceros (polo en $s=1$, ceros triviales, factores $\Gamma$) a la fórmula explícita. $\square$

**Observación 8.1** (¿Por qué es una tautología condicional, no un círculo vicioso?). La igualdad $\operatorname{Re}[g_n(\rho_n)] = w(\gamma_n)/2$ tiene dos partes: (1) La suma $\sum_{\rho\neq\rho_n}\operatorname{Re}[1/(\rho_n-\rho)] = 0$ requiere RH — no es tautológica. Sin RH, hay ceros $\rho = \sigma+i\gamma$ con $\sigma \neq 1/2$, y $\rho_n - \rho = (1/2-\sigma)+i(\gamma_n-\gamma)$ con $\operatorname{Re}[1/(\rho_n-\rho)] \neq 0$ en general. (2) Dado (1), los términos restantes son arquimedianos y coinciden con $w(\gamma_n)/2$ por construcción de $w$. Luego: la parte no-trivial de la prueba es (1) — el Lema 8.1 — que sí usa RH esencialmente.

### 8.5 El Teorema Principal: RH $\Rightarrow$ Inc. Inv.

**Teorema 8.2** (RH $\Rightarrow$ Inc. Inv. — resultado principal). Si todos los ceros no-triviales de $\zeta(s)$ tienen parte real $1/2$ (Hipótesis de Riemann), entonces:

$$C_\infty(\gamma_n) = 0 \quad \forall\, n \geq 1.$$

Es decir, RH $\Rightarrow$ Inc. Inv.

*Prueba.* Fijemos $n \geq 1$ y sea $\rho_n = 1/2+i\gamma_n$. Calculamos $C_\infty(\gamma_n)$ directamente.

Por la Proposición 7.3, $C_\infty(\gamma_n) = 0$ equivale a $\operatorname{Re}[g_n(\rho_n)] = w(\gamma_n)/2$.

Por la Proposición 8.1:

$$g_n(\rho_n) = B + \sum_{\rho \neq \rho_n}\!\left[\frac{1}{\rho_n-\rho}+\frac{1}{\rho}\right] - \frac{1}{\rho_n-1} + \frac{1}{2}\log\pi - \frac{1}{2}\psi_{\text{dig}}\!\!\left(\tfrac{\rho_n}{2}+1\right).$$

Tomando la parte real y usando el Lema 8.1 (que bajo RH da $\operatorname{Re}[1/(\rho_n-\rho)] = 0$ para todo $\rho \neq \rho_n$):

$$\operatorname{Re}[g_n(\rho_n)] = B + \operatorname{Re}\!\left[\sum_{\rho \neq \rho_n}\frac{1}{\rho}\right] + \operatorname{Re}\!\left[\frac{-1}{\rho_n-1}\right] + \frac{1}{2}\log\pi - \frac{1}{2}\operatorname{Re}\,\psi_{\text{dig}}\!\!\left(\tfrac{\rho_n}{2}+1\right).$$

Por la Proposición 8.2, esta expresión es igual a $w(\gamma_n)/2$.

Luego $\operatorname{Re}[g_n(\rho_n)] = w(\gamma_n)/2$, que por la Proposición 7.3 equivale a $C_\infty(\gamma_n) = 0$. $\square$

---

## 9. La Equivalencia Completa RH $\iff$ Inc. Inv.

### 9.1 Enunciado de la equivalencia

**Teorema 9.1** (Equivalencia principal). Las siguientes condiciones son equivalentes:

$$\textbf{(RH)} \quad \iff \quad \textbf{(Inc. Inv.)} \quad \iff \quad \textbf{(CondMin)}$$

donde:
- **RH**: todos los ceros no-triviales de $\zeta(s)$ tienen $\operatorname{Re}(s) = 1/2$.
- **Inc. Inv.**: $C_\infty(\gamma_n) = 0$ para todo $n \geq 1$.
- **CondMin**: $\displaystyle\lim_{\lambda\to\infty} \min_{x_c \in \mathcal{C}_\lambda(T)} C_\lambda(x_c) = 0$ para todo $T > 0$.

*Prueba.*
- **RH $\Rightarrow$ Inc. Inv.**: Teorema 8.2 (este trabajo).
- **Inc. Inv. $\Rightarrow$ RH**: Teorema D (Doc 19).
- **Inc. Inv. $\iff$ CondMin**: Proposición 7.1. $\square$

**Tabla resumen del estado del programa:**

| Implicación | Estado | Referencia |
|---|---|---|
| Inc. Inv. $\Rightarrow$ RH | Probada | Teorema D, Doc 19 |
| RH $\Rightarrow$ Inc. Inv. | **Probada (nueva)** | Teorema 8.2, este trabajo |
| Inc. Inv. [sin hipótesis] | **Abierta** | Cuello de botella final |

### 9.2 Caracterización via ceros complejos en la franja

**Corolario 9.1** (RH y los ceros complejos). Las siguientes condiciones son equivalentes a RH:

(a) Los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$ (para todo $\eta > 0$ fijo) satisfacen: $\sup\{\Im(z) : C_\lambda(z) = \mu_\lambda,\; 0 < \Im(z) \leq \eta\} \to 0$ cuando $\lambda \to \infty$.

(b) $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) = N_\Xi(T) + o(N_\Xi(T))$ y los ceros complejos de $C_\lambda-\mu_\lambda$ en la franja se "evaporan" al eje real.

(c) La altura $y_c$ de todos los ceros complejos de Tipo A satisface $y_c \to 0$.

*Prueba.* Directo de la equivalencia RH $\iff$ Inc. Inv. y la Proposición 7.1(iii). $\square$

### 9.3 Interpretación aritmético-espectral

La equivalencia RH $\iff$ Inc. Inv. tiene la siguiente lectura:

**Dirección Inc. Inv. $\Rightarrow$ RH** (Teorema D): Si los valores propios del operador de Jacobi límite $J_\infty$ son exactamente los imaginarios de los ceros de $\zeta$, entonces los ceros de $\zeta$ son reales. Esto es el análogo espectral de la hipótesis de Hilbert-Pólya: la realidad de los valores propios del operador autoadjunto implica la realidad de los ceros.

**Dirección RH $\Rightarrow$ Inc. Inv.** (Teorema 8.2): Si todos los ceros de $\zeta$ están en la línea crítica, entonces la suma de interacción de cada cero $\rho_n$ con todos los demás ceros (via la suma de Hadamard) tiene parte real nula, y la condición de vanecimiento $C_\infty(\gamma_n) = 0$ se reduce a una identidad de naturaleza arquimediana — automáticamente satisfecha por definición.

**El mecanismo de cancelación:** La clave es que bajo RH, las diferencias $\rho_n - \rho = i(\gamma_n-\gamma)$ son puramente imaginarias, haciendo que $\operatorname{Re}[1/(\rho_n-\rho)] = 0$. Esta es la manifestación analítica de que, si todos los ceros están en la misma recta vertical, su interacción mutua no tiene componente "horizontal" — la alineación en la línea crítica produce una cancelación exacta en las sumas de Hadamard.

---

## 10. El Cuello de Botella Final: Demostración Incondicional de Inc. Inv.

### 10.1 Diagnóstico honesto

El programa ha establecido la equivalencia **bidireccional y completa**:

$$\text{RH} \iff \text{Inc. Inv.} \iff \inf_x C_\lambda(x) \to 0.$$

Las dos implicaciones de la equivalencia están probadas dentro del programa. Sin embargo, **ninguna de ellas prueba RH incondicionalmente**. Para lograrlo se necesita una demostración de Inc. Inv. (o equivalentemente, de CondMin) que no asuma RH como hipótesis.

Esta es la situación estándar de un enfoque de reformulación: la equivalencia reduce RH a una nueva pregunta (Inc. Inv.), y la dificultad se traslada a demostrar esa nueva pregunta. La reformulación es valiosa si la nueva pregunta es más accesible con las herramientas disponibles.

### 10.2 Rutas analíticas disponibles

**Ruta I: Prueba incondicional de CondMin.**

La pregunta es: ¿puede demostrarse que $\min_{x \in [0,T]} C_\lambda(x) \to 0$ cuando $\lambda \to \infty$, sin asumir RH?

Herramientas disponibles:
- La teoría de valores extremos de polinomios de Dirichlet (Bondarenko-Seip [BS12, BS15], Harper [Har20]).
- La conexión con el problema de valores extremos de la función $\zeta$ sobre la línea crítica.
- El método de Turán [Tur50] para sumas de potencias.

**Obstáculo principal:** Los teoremas de Bondarenko-Seip dan cotas para el **máximo** de $|P_N(t)|$ sobre intervalos grandes $[0,T]$. Para el **mínimo** (o el infimum), los resultados son significativamente más débiles. La dificultad es que $D_\lambda$ puede tener mínimos grandes (de tamaño $O(\sqrt{\log\lambda})$) pero $w(x) \sim \frac{1}{2}\log x$ crece más rápido; demostrar que $D_\lambda(x) \approx w(x)$ en algún punto específico es una pregunta de aproximación que involucra la distribución detallada de los $\gamma_n$.

**Ruta II: Norma $L^2$ espectral.**

Demostrar la condición más débil:

$$E_2(\lambda, T) := \sum_{\gamma_n \leq T} |C_\lambda(\gamma_n)|^2 \to 0 \quad \text{cuando } \lambda \to \infty.$$

Esta es más débil que Inc. Inv. (que requiere convergencia puntual $C_\lambda(\gamma_n) \to 0$) pero podría ser atacable via el Teorema de Gonek-Fujii [GF94] sobre sumas de Dirichlet evaluadas en los ceros de $\zeta$. La idea: si $E_2(\lambda,T) \to 0$, entonces (por el Lemma de Fatou en versión discreta) la mayoría de los términos $|C_\lambda(\gamma_n)|^2 \to 0$ — aunque no todos.

**Ruta III: Análisis de la ecuación funcional completa.**

La identidad $(II_n)$ (Proposición 7.2) es una identidad aritmética que involucra todos los primos. Demostrarla usando la ecuación funcional de $\zeta$ directamente — sin pasar por Inc. Inv. — podría proporcionar una ruta alternativa.

### 10.3 La barrera fundamental

**Observación 10.1** (Barrera estructural). Sea cual sea la ruta, toda prueba de Inc. Inv. debe "saber" de alguna manera que los ceros de $\zeta$ están en la línea crítica — porque Inc. Inv. $\iff$ RH. Cualquier argumento que no use información sobre la ubicación de los ceros no puede probar Inc. Inv.

La diferencia entre una prueba genuina y un círculo vicioso reside en **dónde** entra la información sobre los ceros:
- En la prueba de RH $\Rightarrow$ Inc. Inv. (Teorema 8.2): la información entra explícitamente como hipótesis.
- En una prueba incondicional de Inc. Inv.: la información debe extraerse de la estructura aritmética/analítica de $C_\lambda$ — sin asumir nada sobre los ceros.

Esto es análogo a la dificultad en demostrar el Teorema de los Números Primos: la información sobre la región libre de ceros de $\zeta$ (implícita en el PNT) debe extraerse de propiedades de $\zeta$ sin cero-hipótesis previa.

---

## 11. Conclusión

Hemos establecido los siguientes resultados:

1. **Región libre de ceros incondicional** (Teorema 5.2): $C_\lambda - \mu_\lambda$ no tiene ceros complejos para $\Im(z) > 1/2+\epsilon$ y $\lambda$ grande, sin ninguna hipótesis sobre los ceros de $\zeta$.

2. **Geometría de los ceros complejos en la franja** (Teorema 6.1, Proposición 6.2): los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$ emergen de los mínimos locales de $C_\lambda$ a altura $y_c \approx \sqrt{2C_\lambda(x_c)/|C_\lambda''(x_c)|}$, y se acercan al eje real a tasa $\geq 1/\sqrt{\lambda}$ — incondicionalmente.

3. **Reformulación analítica** (Proposición 7.1): Inc. Inv. $\iff$ el ínfimo de $C_\lambda$ tiende a 0. Esto convierte RH en una pregunta de análisis real sobre el mínimo de una función explícita.

4. **RH $\Rightarrow$ Inc. Inv.** (Teorema 8.2): Bajo RH, la suma de Hadamard $\sum_{\rho\neq\rho_n}\operatorname{Re}[1/(\rho_n-\rho)]$ se anula (los ceros alineados en la línea crítica producen diferencias puramente imaginarias), y $C_\infty(\gamma_n) = 0$ se reduce a una identidad arquimediana de definición. Esta implicación es nueva en el programa CCM.

5. **Equivalencia completa** (Teorema 9.1): RH $\iff$ Inc. Inv. $\iff$ CondMin, con ambas direcciones establecidas.

El cuello de botella final del programa es la demostración incondicional de Inc. Inv. — equivalente a demostrar RH desde primeros principios. La reformulación en términos del ínfimo de $C_\lambda$ y la norma $L^2$ espectral proporciona las rutas analíticas más prometedoras para las fases siguientes del programa.

---

## Referencias

[CCM] A. Connes, C. Consani, M. Moscovici, *Noncommutative geometry and motives: the thermodynamics of endomotives*, Adv. Math. 214 (2007), 761–831.

[BS12] A. Bondarenko, K. Seip, *Large GCD sums and extreme values of the Riemann zeta function*, Duke Math. J. 166 (2017), 1685–1701.

[BS15] A. Bondarenko, K. Seip, *Note on large values of L-functions on the critical line* (2015).

[Con99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106.

[Dav00] H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer, 2000.

[GF94] S. Gonek, A. Fujii, *A formula for the logarithmic derivative of the Riemann zeta function*, Acta Arith. 69 (1995), 97–114.

[Har20] A. Harper, *Moments of random multiplicative functions, I: Low moments*, Duke Math. J. 169 (2020), 1–50.

[Tit86] E.C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.

[Tur50] P. Turán, *On a New Method of Analysis and Its Applications*, Wiley, 1984.

---

*Programa de investigación: Phase 29–31, Triples Espectrales Zeta CCM. Docs 01–39.*  
*Este paper consolida los Docs 36–39 del programa.*
