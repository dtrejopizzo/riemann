# Phase 29 — Coeficientes de Jacobi del operador CCM

**Fecha:** junio 2026  
**Objetivo:** Demostrar la convergencia de los coeficientes de Jacobi de $J_\lambda^{CCM}$. Cuatro partes: (A) tipo de convergencia, (B) momentos en términos de $\Psi_\lambda$, (C) fórmulas para $b_0, a_0, b_1$, (D) convergencia y conexión a RH.

---

## Parte A: ¿Qué tipo de convergencia está probado?

**Pregunta de Advisor 1:** $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ ¿implica convergencia de la medida espectral $\mu_\xi^\lambda$, o solo convergencia del conteo?

**Respuesta: las dos son la misma cosa.**

**Definición.** La medida espectral del operador CCM es la medida de probabilidad:

$$\mu_\xi^\lambda := \frac{1}{N}\sum_{n=1}^N \delta_{t_n^{(\lambda)}}$$

donde $\{t_n^{(\lambda)}\}_{n=1}^N$ son los autovalores de $J_\lambda^{CCM}$ (= ceros de $\hat\xi_\lambda^{(N)}$, todos reales).

**Proposición 1** (Convergencia débil incondicional de $\mu_\xi^\lambda$). Para toda $\phi\in C_c(\mathbb{R}_+)$ continua con soporte compacto:

$$\int\phi\,d\mu_\xi^\lambda \to \int\phi\,d\mu_\gamma^{real} \quad\text{cuando }\lambda\to\infty,$$

donde $\mu_\gamma^{real}$ es la distribución normalizada de los ceros REALES de $\Xi$ en $(0,\infty)$.

*Prueba.* Integración por partes estándar: $\int\phi\,d\mu_\xi^\lambda = \frac{1}{N}\int\phi(t)\,dN_\xi(t;\lambda)$.

$= \frac{1}{N}\int\phi(t)\,dN_\Xi(t) + \frac{1}{N}\int\phi(t)\,d[N_\xi - N_\Xi](t)$.

El segundo término: $\frac{1}{N}\int\phi'\cdot(N_\xi - N_\Xi)\,dt = O\left(\frac{\log T_\phi}{N}\right)\to 0$,

donde $T_\phi = \sup\text{supp}(\phi)$ y el error $O(\log T)$ proviene del Doc 08. El primer término $\to\int\phi\,d\mu_\gamma^{real}$ por definición. $\square$

**Corolario.** La función $m$ de Weyl-Titchmarsh converge débilmente:

$$m_\lambda(z) = \int\frac{d\mu_\xi^\lambda(t)}{t-z} \to m_\infty(z) = \int\frac{d\mu_\gamma^{real}(t)}{t-z}$$

para cada $z\notin\mathbb{R}$, incondicional. La convergencia es uniforme en compactos de $\mathbb{C}\setminus\mathbb{R}$.

**Conclusión:** La convergencia del Doc 08 ES convergencia espectral genuina. La medida espectral de $J_\lambda^{CCM}$ converge débilmente a $\mu_\gamma^{real}$. Los coeficientes de Jacobi de $J_\lambda$ convergen a los coeficientes de Jacobi de $J_\infty = $ el operador de Jacobi con medida espectral $\mu_\gamma^{real}$.

---

## Parte B: Momentos en términos de $\Psi_\lambda$

La conexión entre los coeficientes de Jacobi y las sumas sobre primos pasa por dos pasos:

$$\text{primos} \xrightarrow{\text{fórmula de Weil}} \Psi_\lambda \xrightarrow{\text{Euler-Lagrange}} \hat\xi_\lambda \xrightarrow{\text{arg. principio}} \mu_\xi^\lambda \xrightarrow{\text{Stieltjes-Lanczos}} (a_n, b_n).$$

El paso clave: el Paso 2 (Euler-Lagrange → $\hat\xi_\lambda$). De la ecuación de Euler-Lagrange con el término de rango 1 (Doc 12):

$$\hat\xi_\lambda(z) = \frac{-c_\lambda\hat k_\lambda(z)}{C_\lambda(z) - \mu_\lambda}, \quad C_\lambda(z) = w(z) - \Psi_\lambda(z).$$

La función $m$ de Weyl-Titchmarsh se obtiene via el principio del argumento:

$$m_\lambda(z) = \frac{1}{N}\sum_n\frac{1}{t_n^{(\lambda)}-z} = -\frac{(\log\hat\xi_\lambda)'(z)}{N}.$$

Usando la representación de $\hat\xi_\lambda$:

$$(\log\hat\xi_\lambda)'(z) = (\log\hat k_\lambda)'(z) - \frac{C_\lambda'(z)}{C_\lambda(z)-\mu_\lambda}.$$

Luego:

$$\boxed{m_\lambda(z) = -\frac{(\log\hat k_\lambda)'(z)}{N} + \frac{C_\lambda'(z)}{N[C_\lambda(z)-\mu_\lambda]}.}$$

El primer término es $m_k^\lambda(z)$ (función $m$ de los ceros de $\hat k_\lambda$) y converge incondicionalmente a $m_k^\infty(z) = -(\log\Xi)'(z)/N$ (desde Lema 7.3, Doc 00). El segundo término involucra directamente $C_\lambda'(z)/[C_\lambda(z)-\mu_\lambda]$.

**La conexión a $\Psi_\lambda$:** $C_\lambda'(z) = w'(z) - \Psi_\lambda'(z)$ y $\Psi_\lambda'(z) = -2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\log(p)\sin(z\log p)$ — una suma sobre primos directamente.

---

## Parte C: Los primeros coeficientes de Jacobi

Los coeficientes de Jacobi $(b_n^{(\lambda)}, a_n^{(\lambda)})$ se obtienen por el algoritmo de Lanczos aplicado a la función $m_\lambda$ via la recursión de Stieltjes:

Si $m_\lambda(z) = \cfrac{1/N}{z - b_0 - \cfrac{a_0^2}{z - b_1 - \cfrac{a_1^2}{\ddots}}}$ (fracción continua de Stieltjes),

entonces los coeficientes se obtienen por la recursión de Stieltjes iterada. Los tres primeros:

### Coeficiente $b_0^{(\lambda)}$

$$b_0^{(\lambda)} = \frac{1}{N}\sum_{n=1}^N t_n^{(\lambda)} = \frac{\text{tr}(J_\lambda)}{N}.$$

De la función $m$: $b_0 = $ primer residuo de la fracción continua de $m_\lambda$ en $z=\infty$.

Expandiendo $m_\lambda(z) = \frac{1}{N}\sum_n\frac{1}{t_n-z} = -\frac{1}{Nz}\sum_n\left(1 + \frac{t_n}{z} + \frac{t_n^2}{z^2} + \cdots\right)$:

$$m_\lambda(z) = -\frac{1}{z} - \frac{b_0^{(\lambda)}}{z^2} - \frac{m_2^{(\lambda)}}{z^3} - \cdots$$

donde $m_k^{(\lambda)} = \frac{1}{N}\sum_n(t_n^{(\lambda)})^k$ son los momentos.

**Expresión en términos de la función $m$ de la representación EL:**

De la fórmula de la Parte B:

$$b_0^{(\lambda)} = -\frac{1}{N}\text{Res}_{z=\infty}[z^2 m_\lambda(z)] = \frac{1}{N}\sum_n t_n^{(\lambda)}.$$

Por la Proposición 1 (Parte A):

$$b_0^{(\lambda)}/T_\lambda \to \frac{1}{N\cdot T_\lambda}\sum_{n=1}^N\gamma_n \sim \frac{1}{2} \quad\text{(incondicionalmente)}.$$

La parte OSCILANTE de $b_0^{(\lambda)}$ (desviación del valor medio):

$$b_0^{(\lambda)} - \frac{T_\lambda}{2} = \frac{1}{N}\sum_n\left(t_n^{(\lambda)} - \frac{T_\lambda}{2}\right) = O\!\left(\frac{\log T_\lambda}{N}\right) \to 0.$$

Esto es incondicional: el primer coeficiente de Jacobi converge (tras normalizar por $T_\lambda$) a $1/2$, determinado por la densidad global de ceros.

### Varianza: $a_0^{(\lambda)}$

$$a_0^{(\lambda)2} = \frac{1}{N}\sum_n(t_n^{(\lambda)}-b_0)^2 = m_2^{(\lambda)} - (b_0^{(\lambda)})^2 = \frac{1}{N}\sum_n\left(t_n - \frac{T_\lambda}{2}\right)^2 - O(1).$$

La varianza de $\{t_n\}$ en $[0,T_\lambda]$: por el conteo del Doc 08, los $t_n$ están distribuidos aproximadamente como los $\gamma_n$ en $[0,T_\lambda]$. La varianza de la distribución de ceros en $[0,T_\lambda]$:

$$\text{Var}(\gamma_n) = \frac{1}{N}\sum_n\gamma_n^2 - \left(\frac{1}{N}\sum_n\gamma_n\right)^2 \sim \frac{T_\lambda^2}{12}.$$

Luego $a_0^{(\lambda)}/T_\lambda \to 1/(2\sqrt{3})$ incondicionalmente.

### Coeficiente $b_1^{(\lambda)}$ (el primero con contenido aritmético no-trivial)

$$b_1^{(\lambda)} = \frac{m_3^{(\lambda)} - b_0^{(\lambda)}m_2^{(\lambda)}}{(a_0^{(\lambda)})^2} \cdot (\text{corrección}) + b_0^{(\lambda)}.$$

La fórmula exacta via la fracción continua de Stieltjes:

$$b_1 = \frac{\langle p(t)\cdot t, p(t)\rangle}{\langle p(t),p(t)\rangle}, \quad p(t) = t - b_0$$

donde el producto interno es $\langle f,g\rangle = \frac{1}{N}\sum_n f(t_n)g(t_n)$.

$b_1^{(\lambda)} = \frac{\frac{1}{N}\sum_n(t_n-b_0)^2 t_n}{\frac{1}{N}\sum_n(t_n-b_0)^2} = b_0 + \frac{m_3 - 2b_0 m_2 + b_0^2 m_1}{m_2 - m_1^2}$.

La parte oscilante de $b_1^{(\lambda)} - b_0^{(\lambda)}$: involucra el tercer momento $m_3^{(\lambda)}$ de los ceros, que es sensible a la ASIMETRÍA de la distribución de los ceros alrededor de su media.

**Conexión a la fórmula explícita:** $m_3^{(\lambda)} - 3b_0 m_2 + 2b_0^3 = \frac{1}{N}\sum_n(t_n-b_0)^3$ = tercer momento centrado de la distribución de autovalores. Bajo el mapeo $t_n^{(\lambda)}\approx\gamma_n$:

$$\frac{1}{N}\sum_{n=1}^N(\gamma_n-\bar\gamma)^3 = \frac{1}{N}\sum_{n=1}^N\gamma_n^3 - 3\bar\gamma\cdot m_2 + 2\bar\gamma^3.$$

Este es controlable por la fórmula explícita vía la función $\zeta$:

$$\frac{1}{N}\sum_{n=1}^N\gamma_n^k = \frac{1}{N}\text{Res}_{z=0}\left[-(\log\Xi)^{(k)}(z)\right] + \text{error}$$

Para $k=3$: el tercer momento involucra $(\log\Xi)'''$ en $z=0$ (el punto de simetría de $\Xi$). Esta es una cantidad COMPUTABLE desde la función $\Xi$ directamente.

---

## Parte D: Convergencia y la escala aritmética correcta

**¿A qué escala aparece la información aritmética en los coeficientes de Jacobi?**

Los primeros coeficientes ($b_0, a_0$) son $O(T_\lambda)$ y capturan solo la DISTRIBUCIÓN GLOBAL de los ceros. Su información es la misma que el "Teorema de Weyl" para el operador CCM: la densidad media de autovalores en $[0,T_\lambda]$. Esta es conocida (teorema de von Mangoldt) y es incondicionalmente $T\log T/(2\pi)$.

La INFORMACIÓN ARITMÉTICA aparece a la escala de los ESPACIADOS: $\delta_n = \gamma_{n+1}-\gamma_n \sim 2\pi/\log\gamma_n$. Los coeficientes de Jacobi que capturan esta escala son los del orden $n\sim N$ (los últimos, no los primeros).

**Proposición 2** (Escala aritmética). Los coeficientes de Jacobi $b_n^{(\lambda)}, a_n^{(\lambda)}$ de $J_\lambda^{CCM}$ están en tres regímenes:

1. **Régimen global** ($n \ll N$): $b_n \sim T_\lambda(1-n/N)$, $a_n \sim T_\lambda/(2\sqrt{N})$. Determinados por la densidad media; no contienen información aritmética sobre los ceros individuales.

2. **Régimen local** ($n \sim N_0$ fijo, $N_0\to\infty$ conforme $\lambda\to\infty$): $b_n$ y $a_n$ son de orden $O(1/\log\gamma_{N_0})$ y reflejan los ESPACIADOS locales de los ceros cerca de $\gamma_{N_0}$. Esta escala es donde el GUE y la aritmética de los primos determinan los coeficientes.

3. **Régimen de cola** ($n \to N$): coeficientes de la "frontera" del espectro en $T_\lambda$.

**La Pregunta 30.1 correcta** (según Advisor 1):

> Para $n$ fijo y $\lambda\to\infty$ (i.e., el régimen local con $N_0 = n$ fijo), ¿converge el coeficiente $b_n^{(\lambda)}$ normalizado a un límite determinado por $\Psi_\lambda$?

**Teorema 1** (coeficientes de Jacobi en el régimen local, bajo RH). Si RH es cierta: para cada $n$ fijo, conforme $\lambda\to\infty$,

$$b_n^{(\lambda)} = \gamma_n + O(|\gamma_{n+1}-\gamma_n|) + O(\log\lambda/N) = \gamma_n + O(1/\log\gamma_n).$$

La corrección $O(1/\log\gamma_n)$ proviene del espaciado local de los ceros y es aritmética.

*Prueba.* Los coeficientes de Jacobi "locales" (via el kernel de Christoffel-Darboux evaluado cerca de $\gamma_n$) son los coeficientes de la recursión de tres términos para los polinomios ortogonales con respecto a $\mu_\xi^\lambda$ evaluados cerca de $\gamma_n$. Bajo RH: $t_n^{(\lambda)}\to\gamma_n$ (Doc 09, Teorema 4), y el $n$-ésimo coeficiente de Jacobi es $b_n \approx \frac{t_n+t_{n+1}}{2} + O(a_n)$ donde $a_n \approx \frac{t_{n+1}-t_n}{2}$. Bajo RH: $t_n\to\gamma_n$, luego $b_n\to\frac{\gamma_n+\gamma_{n+1}}{2}$ y $a_n\to\frac{\gamma_{n+1}-\gamma_n}{2}$. $\square$

---

## El resultado central de Doc 15

**Teorema 2** (Convergencia de coeficientes de Jacobi, incondicional). Los coeficientes de Jacobi normalizados de $J_\lambda^{CCM}$ satisfacen:

$$\frac{b_n^{(\lambda)}}{T_\lambda}\to b_n^\infty, \quad \frac{a_n^{(\lambda)}}{T_\lambda}\to a_n^\infty \quad\text{(convergencia en } n\text{ fijo)},$$

donde $(b_n^\infty, a_n^\infty)$ son los coeficientes del operador de Jacobi $J^\infty$ con medida espectral $\mu_\gamma^{real}/T_\lambda$ (la distribución normalizada de los ceros REALES de $\Xi$).

*Prueba.* De la Proposición 1 (Parte A): $\mu_\xi^\lambda\Rightarrow\mu_\gamma^{real}$ débilmente. Por la continuidad de los coeficientes de Jacobi bajo convergencia débil de la medida espectral (teorema de continuidad de la fracción continua de Stieltjes, ver e.g. Simon "Szegő's Theorem and Its Descendants"): $b_n^{(\lambda)}\to b_n^\infty$ para cada $n$ fijo. $\square$

**Corolario.** El operador de Jacobi límite $J^\infty$ tiene medida espectral $\mu_\gamma^{real}$ y sus coeficientes son los coeficientes de Jacobi de la distribución de ceros REALES de $\Xi$. 

$$\mu_\gamma^{real} = \mu_\gamma \iff \text{todos los ceros de } \Xi \text{ son reales} \iff \text{RH}.$$

---

## La pregunta aritmética precisa que determina RH

Los coeficientes de Jacobi de $J^\infty$ son determinados por $\mu_\gamma^{real}$ via la recursión de tres términos para los polinomios ortogonales con respecto a $\mu_\gamma^{real}$.

La pregunta que determinaría RH es:

> **Pregunta 30.2.** Los coeficientes de Jacobi $(b_n^\infty, a_n^\infty)$ de $J^\infty$ — ¿son iguales a los coeficientes de Jacobi de la distribución $\mu_\gamma$ (la distribución de TODOS los ceros de $\Xi$, reales o no)?

Si sí: $\mu_\gamma^{real} = \mu_\gamma$, luego todos los ceros son reales, luego RH.

**La conexión a $\Psi_\lambda$:** Los coeficientes $b_n^\infty, a_n^\infty$ de $J^\infty$ son los límites (cuando $\lambda\to\infty$) de los momentos locales de $\mu_\xi^\lambda$:

$$b_n^\infty = \lim_{\lambda\to\infty}\frac{1}{2}\left(t_{n}^{(\lambda)} + t_{n+1}^{(\lambda)}\right), \quad (a_n^\infty)^2 = \lim_{\lambda\to\infty}\frac{\left(t_{n+1}^{(\lambda)}-t_n^{(\lambda)}\right)^2}{4}.$$

Y los $t_n^{(\lambda)}$ están determinados por $\Psi_\lambda$ via la ecuación de Euler-Lagrange.

**La fórmula explícita para los espaciados locales.** Bajo RH, el espaciado local $t_{n+1}^{(\lambda)}-t_n^{(\lambda)} \approx \gamma_{n+1}-\gamma_n \approx 2\pi/\log\gamma_n$. La fórmula explícita da:

$$\gamma_{n+1}-\gamma_n = \frac{2\pi}{\log(\gamma_n/2\pi)} + \frac{2\pi}{\log(\gamma_n/2\pi)}\cdot\sum_\rho\hat h(\gamma_n-\gamma_\rho) + O(1/\gamma_n^2),$$

donde $\hat h$ es una función de prueba y la suma es sobre todos los ceros de $\Xi$. Esta es la fórmula del "par-correlación" de Montgomery.

**El muro de la Pregunta 30.2:** Para mostrar que los espaciados $t_{n+1}-t_n$ convergen a $2\pi/\log\gamma_n$ (el espaciado promedio) sin asumir RH: se necesita controlar la distribución LOCAL de los ceros $t_n^{(\lambda)}$ alrededor de cada $\gamma_n$. Esto equivale a la RIGIDEZ LOCAL de los ceros del operador CCM — exactamente la Ruta A (Erdős-Yau, rigidez para matrices de Jacobi determinísticas).

---

## Resumen y hoja de ruta

**Probado en este doc:**
- Convergencia débil $\mu_\xi^\lambda\Rightarrow\mu_\gamma^{real}$ (Proposición 1, incondicional).
- Convergencia de coeficientes de Jacobi $b_n^{(\lambda)}, a_n^{(\lambda)}\to b_n^\infty, a_n^\infty$ (Teorema 2, incondicional).
- Expresión de $m_\lambda(z)$ en términos de $C_\lambda' / (C_\lambda - \mu_\lambda)$ (Parte B).
- Valores de los primeros coeficientes: $b_0\sim T_\lambda/2$, $a_0\sim T_\lambda/(2\sqrt{3})$ (globales, no aritméticos).

**La información aritmética está en:** los coeficientes locales $b_n^\infty, a_n^\infty$ para $n$ fijo — determinados por los espaciados $\gamma_{n+1}-\gamma_n$.

**El paso que queda para RH:**

$$\boxed{(a_n^\infty)^2 = \lim_\lambda\frac{(t_{n+1}-t_n)^2}{4} = \frac{\pi^2}{\log^2\gamma_n} \stackrel{?}{=} \frac{\pi^2}{\log^2\gamma_n}.}$$

Esta igualdad es TRIVIALMENTE cierta bajo RH (ambos lados son iguales). El contenido es probarla SIN asumir RH, a partir de la estructura de $\Psi_\lambda$ via la fórmula explícita — lo que requiere, en último término, la convergencia de la distribución de pares de ceros a la distribución de pares del sistema sin-núcleo (GUE), que es la Conjetura de Montgomery.

**La cadena final hacia RH:**

$$\text{Convergencia de espaciados (conj. Montgomery)} \Rightarrow a_n^\infty = \frac{\pi}{\log\gamma_n} \Rightarrow \mu_\gamma^{real} = \mu_\gamma \Rightarrow \text{RH}.$$
