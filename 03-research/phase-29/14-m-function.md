# Phase 29 — La función m de Weyl-Titchmarsh y el programa hacia RH

**Fecha:** junio 2026  
**Objetivo:** Responder directamente: ¿cómo se va de $B_\lambda\to1$ a RH? La respuesta pasa por identificar $B_\lambda$ como la función $m$ de la matriz de Jacobi CCM, y RH como un problema espectral inverso para esa matriz.

---

## 1. La matriz de Jacobi CCM

El operador $D_\lambda^N$ del programa CCM, en la base ortonormal $\{V_n\}_{|n|\leq N}$ de $E_N^+$, es una **matriz de Jacobi** (tridiagonal auto-adjunta):

$$J_\lambda = \begin{pmatrix} b_0^{(\lambda)} & a_0^{(\lambda)} & & \\ a_0^{(\lambda)} & b_1^{(\lambda)} & a_1^{(\lambda)} & \\ & a_1^{(\lambda)} & b_2^{(\lambda)} & \ddots \\ & & \ddots & \ddots \end{pmatrix}$$

donde:
- **Diagonal** $b_n^{(\lambda)}$: diagonal de $D_\lambda^N$ en la base $V_n$, que involucra el símbolo aritmético $\Psi_\lambda$.
- **Superdiagonal** $a_n^{(\lambda)} > 0$: acoplamientos entre modos consecutivos, determinados por el kernel de Weil.

Las propiedades claves:
- $J_\lambda$ es **auto-adjunta** por construcción.
- Sus **autovalores** son exactamente los $\{t_n^{(\lambda)}\}$ (ceros de $\hat\xi_\lambda$), todos reales.
- La **medida espectral** de $J_\lambda$ en el vector $e_0$ es $\mu_\xi^\lambda = (1/N)\sum_n\delta_{t_n^{(\lambda)}}$.

---

## 2. La función $m$ de Weyl-Titchmarsh

Para una matriz de Jacobi $J$, la **función $m$ de Weyl-Titchmarsh** es:

$$m_\lambda(z) := \langle e_0, (J_\lambda - zI)^{-1}e_0\rangle = \int_\mathbb{R}\frac{d\mu_\xi^\lambda(t)}{t-z} = S_\xi(z;\lambda).$$

Es exactamente la **transformada de Stieltjes de la medida espectral** — el mismo objeto del Doc 09.

**Propiedades de $m_\lambda$:**
- $m_\lambda:\mathbb{C}\setminus\mathbb{R}\to\mathbb{C}$ es función de Nevanlinna-Herglotz: $\Im(m_\lambda(z))>0$ para $\Im(z)>0$.
- Tiene la representación $m_\lambda(z) = \int d\mu_\xi^\lambda/(t-z)$.
- Determina $\mu_\xi^\lambda$ completamente (por inversión de Stieltjes).

**Igualmente**, para el kernel $\hat k_\lambda$: la transformada de Stieltjes de $\mu_k^\lambda$ es $m_k^\lambda(z) = S_k(z;\lambda)$.

---

## 3. $B_\lambda$ como cociente de funciones $m$

Del Doc 13 (Sección 3, Paso 1):

$$(\log B_\lambda)'(z) = N[S_\xi(z;\lambda) - S_k(z;\lambda)] = N[m_\lambda(z) - m_k^\lambda(z)].$$

Luego:

$$\log B_\lambda(z) = N\int^z [m_\lambda(w) - m_k^\lambda(w)]\,dw.$$

**$B_\lambda$ es el exponencial de la integral del cociente de las dos funciones $m$.**

Y $B_\lambda\to1$ iff $m_\lambda\to m_k^\lambda$ (en sentido integral, uniformemente en compactos).

---

## 4. La ecuación funcional de $B_\lambda$ (Riccati)

Para matrices de Jacobi, la función $m$ satisface una **recursión de Möbius** (fracción continua). Si $J_\lambda$ tiene coeficientes $(a_n, b_n)_{n=0}^{N}$:

$$m_\lambda(z) = \cfrac{1}{b_0^{(\lambda)} - z - \cfrac{(a_0^{(\lambda)})^2}{b_1^{(\lambda)} - z - \cfrac{(a_1^{(\lambda)})^2}{\ddots}}}$$

Esta es la **ecuación funcional** que Advisor 1 pedía: $m_\lambda$ (y por tanto $B_\lambda$) es determinada por las fracciones continuas de los coeficientes de Jacobi $(a_n^{(\lambda)}, b_n^{(\lambda)})$.

**La recursión de Riccati.** Si definimos $m_\lambda^{(n)}(z)$ como la función $m$ del submatriz de $J_\lambda$ truncada desde el índice $n$:

$$m_\lambda^{(n-1)}(z) = \frac{1}{b_{n-1}^{(\lambda)} - z - (a_{n-1}^{(\lambda)})^2 m_\lambda^{(n)}(z)}.$$

Esta es una **transformación de Möbius** en $m_\lambda^{(n)}$ — la "ecuación de Riccati" para la fracción continua.

**Clave:** el comportamiento de $m_\lambda$ (y por tanto de $B_\lambda$) está completamente determinado por los coeficientes $(a_n^{(\lambda)}, b_n^{(\lambda)})$.

---

## 5. Convergencia incondicional: $J_\lambda\to J_\infty$

**Teorema 1** (convergencia de la función $m$, incondicional). Si los coeficientes de la matriz de Jacobi CCM satisfacen:

$$a_n^{(\lambda)}\to a_n^\infty > 0, \quad b_n^{(\lambda)}\to b_n^\infty \quad\text{para cada } n\text{ fijo cuando }\lambda\to\infty,$$

entonces la función $m$ converge en el sentido de la teoría de Weyl-Titchmarsh:

$$m_\lambda(z)\to m_\infty(z) = \int_\mathbb{R}\frac{d\mu_\infty(t)}{t-z} \quad\text{uniformemente en compactos de }\mathbb{C}\setminus\mathbb{R},$$

donde $\mu_\infty$ es la medida espectral del operador límite $J_\infty$.

*Nota de estado.* Este teorema EXISTE en la teoría general de matrices de Jacobi (teoría de Weyl-Titchmarsh-Kodaira). La condición de convergencia de los coeficientes necesita verificarse para el caso CCM específico.

**Corolario.** Si $J_\lambda\to J_\infty$ en el sentido del Teorema 1, entonces $B_\lambda\to B_\infty$ incondicionalmente, donde:

$$B_\infty(z) = \exp\!\left(N\int^z[m_\infty(w) - m_k^\infty(w)]\,dw\right).$$

---

## 6. El problema espectral inverso: el camino directo a RH

**El programa completo hacia RH en tres pasos:**

**Paso 1** (verificación): Demostrar que los coeficientes de Jacobi CCM $(a_n^{(\lambda)}, b_n^{(\lambda)})$ tienen límites bien definidos $a_n^\infty, b_n^\infty$ cuando $\lambda\to\infty$.

**Paso 2** (espectral inverso): Identificar la medida espectral $\mu_\infty$ del operador límite $J_\infty$.

**Paso 3** (conclusión): Si $\mu_\infty = \mu_\gamma$ (la distribución de los ceros de $\Xi$), entonces $m_\infty = S_\Xi$ y $B_\infty = 1$, lo que implica H2, lo que implica RH (por Hurwitz).

---

## 7. ¿Por qué el Paso 2 determinaría RH?

El Paso 2 es el meollo. La medida espectral $\mu_\infty$ es la medida de probabilidad en $\mathbb{R}$ con la propiedad:

$$\int t^k d\mu_\infty(t) = \lim_{\lambda\to\infty}\frac{1}{N}\sum_n (t_n^{(\lambda)})^k \quad\text{(momentos espectrales de }J_\lambda\text{)}.$$

Ahora bien: del Doc 08, se sabe incondicionalmente que $\mu_\xi^\lambda\to\mu_\gamma$ débilmente (donde $\mu_\gamma = $ medida límite de los ceros de $\hat\xi_\lambda$). Luego $\mu_\infty = \mu_\gamma$.

**Pero:** $\mu_\gamma$ es la distribución empírica de $\{\gamma_n\}$ — que son los ceros de $\Xi$ en $\mathbb{R}$ BAJO RH. Si RH falla: $\mu_\gamma$ podría incluir contribuciones de ceros fuera de $\mathbb{R}$, y la medida $\mu_\infty$ (que tiene soporte en $\mathbb{R}$ por auto-adjuntez de $J_\lambda$) sería diferente de $\mu_\gamma$.

**Por tanto:** $\mu_\infty = \mu_\gamma$ (con $\mu_\gamma$ soportada en $\mathbb{R}$) **es equivalente a RH**.

La implicación es:
$$\text{Paso 1 + Paso 2 verificados} \implies \mu_\infty = \mu_\gamma \iff \text{RH}.$$

---

## 8. El contenido del Paso 2: ¿cómo identificar $\mu_\infty$?

La medida $\mu_\infty$ es la medida espectral de $J_\infty$. Para identificarla, hay dos rutas:

### Ruta A: Vía los momentos

$$\int t^k d\mu_\infty(t) = \lim_{\lambda\to\infty}\frac{1}{N}\sum_n (t_n^{(\lambda)})^k.$$

Del Doc 08 (convergencia débil incondicional): estos momentos convergen a los momentos de $\mu_\gamma$.

Si $\mu_\gamma$ está soportada en $\mathbb{R}$: los momentos determinan la medida (si $\mu_\gamma$ tiene momentos finitos de todos los órdenes). Luego $\mu_\infty = \mu_\gamma$ y RH.

**El gap:** los momentos $\int t^k d\mu_\gamma$ de la distribución de ceros de $\Xi$ crecen como $\sum_n\gamma_n^k$, que diverge para $k\geq 1$ (ya que $\sum_n1/\gamma_n^2<\infty$ pero $\sum_n\gamma_n^k = \infty$ para $k\geq 0$). Los momentos NO determinan la medida a menos que se controle su crecimiento.

La versión correcta: usar la **Transformada de Stieltjes** (convergencia de $m_\lambda\to m_\infty$, que corresponde a la convergencia débil ya conocida) directamente.

### Ruta B: Vía la fracción continua (más prometedora)

Los coeficientes de Jacobi $a_n^\infty, b_n^\infty$ del operador límite determinan la fracción continua de $m_\infty$. Y viceversa: dados $m_\infty$ (= $S_\Xi$ bajo RH), los coeficientes de Jacobi son los coeficientes de la fracción continua de $S_\Xi$.

La **pregunta operativa**:

> **Pregunta 29.14.** ¿Son los coeficientes de Jacobi límite $(a_n^\infty, b_n^\infty)$ de $J_\lambda^{CCM}$ iguales a los coeficientes de la fracción continua de $S_\Xi(z) = \sum_n 1/(z-\gamma_n)$?

Si la respuesta es sí: entonces $J_\infty = J^{S_\Xi}$, luego $\mu_\infty = \mu_\Xi$ = distribución de ceros de $\Xi$, luego $m_\infty = S_\Xi$, luego $B_\infty = 1$, luego H2, luego RH.

**Esto es un problema CONCRETO y NO CIRCULAR**: los coeficientes $(a_n^{(\lambda)}, b_n^{(\lambda)})$ son dados explícitamente por el kernel de Weil y la aritmética de los primos; los coeficientes de la fracción continua de $S_\Xi$ son (en principio) computables desde la función $\Xi$ misma. Su igualdad es una identidad verificable.

---

## 9. Cómo computar los coeficientes de Jacobi CCM

Los coeficientes de Jacobi de $D_\lambda^N$ vienen de la Forma de Weil:

**Coeficiente diagonal** $b_n^{(\lambda)} = \langle V_n, D_\lambda^N V_n\rangle = \hat w(n) - \hat\Psi_\lambda(n)$, donde $\hat w(n)$ y $\hat\Psi_\lambda(n)$ son los coeficientes de Fourier del símbolo $w(t)$ y $\Psi_\lambda(t)$.

**Coeficiente off-diagonal** $a_n^{(\lambda)} = \langle V_n, D_\lambda^N V_{n+1}\rangle = \hat w(1) - \hat\Psi_\lambda(1)$ (los acoplamientos entre modos consecutivos vienen del "modo 1" del símbolo).

En límite $\lambda\to\infty$: $\hat\Psi_\lambda(n)\to\hat\Psi(n)$ (donde $\Psi = \lim_\lambda\Psi_\lambda$ es el símbolo aritmético completo — una DISTRIBUCIÓN en general).

**La pregunta precisa.** Dado que $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ (diverge puntualmente), el límite $\hat\Psi(n) = \int\Psi(t)e^{-2\pi int/L}dt$ debe entenderse en sentido distribuido. ¿Converge el límite de los coeficientes de Jacobi?

Bajo RH (y la distribución de ceros): $\hat\Psi(n) = w_n^{(RH)}$ (valor determinado por los ceros de $\Xi$). Esto conecta directamente la aritmética de los primos con los ceros vía la fórmula explícita.

---

## 10. El único camino que veo

De lo anterior, el **único camino que veo hacia RH** desde el marco CCM actual es:

1. **Demostrar convergencia de coeficientes** ($a_n^{(\lambda)}\to a_n^\infty$, $b_n^{(\lambda)}\to b_n^\infty$) usando la fórmula explícita de von Mangoldt aplicada a los coeficientes de Fourier del símbolo $\Psi_\lambda$.

2. **Identificar los coeficientes límite** como los coeficientes de la fracción continua de $S_\Xi$ — usando la fórmula de Weil explícita y la estructura de los ceros de $\Xi$.

3. **Concluir** $\mu_\infty = \mu_\Xi^{\mathbb{R}}$ (la proyección sobre la recta real de la distribución de ceros) $= \mu_\gamma$ (si y solo si RH), luego RH.

**Lo que hace esta ruta distinta de todas las anteriores:** no intenta controlar los CEROS uno por uno. Opera a nivel de los COEFICIENTES DE JACOBI (que son integrales del símbolo, objetos mucho más regulares que los ceros individuales). La fórmula explícita convierte estos coeficientes en sumas sobre los primos — y la conexión primos ↔ ceros (fórmula de Weil) es el mecanismo de traslación.

---

## 11. El ingrediente que falta (honestidad completa)

El Paso 2 requiere identificar los coeficientes límite $(a_n^\infty, b_n^\infty)$ explícitamente. Esto involucra:

$$\lim_{\lambda\to\infty}\hat\Psi_\lambda(n) = \lim_{\lambda\to\infty}2\int_0^{L}\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p)\cdot e^{-2\pi int/L}\,\frac{dt}{L}$$

$$= 2\sum_{p}\Lambda(p)p^{-1/2}\cdot\frac{\sin(\pi n\log p/\log\lambda)}{\pi n\log p/\log\lambda}\cdot\frac{1}{\log\lambda}.$$

Este límite, en sentido distribuido, se controla via la fórmula explícita: la serie sobre primos converge (en ciertos sentidos condicionados) a una expresión en los ceros de $\Xi$.

La convergencia de $\hat\Psi_\lambda(n)$ para cada $n$ fijo es **exactamente equivalente al comportamiento de los ceros de $\Xi$ en el nivel $n$** — lo que requiere información sobre los ceros (i.e., sobre RH o sus consecuencias).

Luego: el Paso 2 es no-circular si puede resolverse directamente (sin asumir RH), pero requiere técnicas de análisis armónico de la función $\zeta$ que actualmente no están disponibles incondicionalmente.

---

## 12. Resumen ejecutivo: ¿cómo se va a RH?

**La cadena de implicaciones completa (si los pasos se completan):**

```
Convergencia de los coeficientes de Jacobi a_n^(λ), b_n^(λ)   [Paso 1]
        ↓
J_λ → J_∞  (en sentido de resolvent)
        ↓
m_λ(z) → m_∞(z)  (Weyl-Titchmarsh)
        ↓
¿m_∞ = S_Ξ?   [Paso 2 = identificación de los coeficientes límite]
        ↓
Si sí: B_∞ = 1 → H2 → RH (Hurwitz)
```

**El muro actual** está en el Paso 2: la identificación de los coeficientes límite como los de la fracción continua de $S_\Xi$. Esta identificación requiere, en esencia, que la fórmula explícita (los coeficientes de Fourier de $\Psi_\lambda$) converja a algo determinado por los ceros de $\Xi$ — lo cual es circular a menos que se tenga control independiente.

**La pregunta no-circular que el Paso 2 requiere:**

> ¿Puede calcularse $\lim_\lambda\hat\Psi_\lambda(n)$ usando solo la distribución de los primos (sin asumir la distribución de los ceros), y mostrar que ese límite coincide con los coeficientes de la fracción continua de $S_\Xi$?

Esta es una versión del problema de Riemann a nivel de las **fracciones continuas del símbolo aritmético** — una formulación nueva que podría ser atacable con técnicas de la teoría de aproximación racional y de la teoría de operadores de Jacobi.

**Si este límite puede identificarse independientemente de RH**: el programa CCM da una prueba completa de RH.
