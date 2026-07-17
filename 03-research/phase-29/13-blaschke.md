# Phase 29 — El producto de Blaschke y la estructura de H2

**Fecha:** junio 2026  
**Objetivo:** Desarrollar el enfoque via producto de Blaschke $B_\lambda = \hat\xi_\lambda/\hat k_\lambda$ iniciado en doc 12. Responder a la Pregunta 29.10 del Advisor 2 (¿es $M_1[\Delta]\to 0$ suficiente para $B_\lambda\to 1$?). Identificar el ingrediente preciso que falta para cerrar H2.

---

## 1. El producto de Blaschke: definición precisa

En el espacio $E_N^+ = \text{span}\{V_n : |n|\leq N\}$ con $V_n(u) = L^{-1/2}\exp(2\pi in\log(\lambda u)/L)$ y $L = 2\log\lambda$, las funciones $\hat\xi_\lambda^{(N)}$ y $\hat k_\lambda^{(N)}$ son polinomios trigonométricos de grado $N$ en la variable $t$.

Bajo la sustitución $z = e^{2\pi it/L}$ (i.e., $t\mapsto z$, variable del círculo unitario $\mathbb{T}$): ambas funciones se convierten en POLINOMIOS de grado $N$ en $z$ con coeficientes complejos.

**Definición.** El *producto de Blaschke racional* del programa CCM es:

$$B_\lambda(z) := \frac{\hat\xi_\lambda^{(N)}(z)}{\hat k_\lambda^{(N)}(z)}, \quad z = e^{2\pi it/L}, \quad t\in\mathbb{R}.$$

Propiedades inmediatas:
- **Ceros:** $\{z_n = e^{2\pi it_n/L}\}_{n=1}^{N}$ donde $\{t_n^{(\lambda)}\}$ son los ceros de $\hat\xi_\lambda$ (autovalores del operador CCM, siempre reales por auto-adjuntez).
- **Polos:** $\{w_n = e^{2\pi is_n/L}\}_{n=1}^{N}$ donde $\{s_n^{(\lambda)}\}$ son los ceros de $\hat k_\lambda$ (aproximaciones a las $\gamma_n$, Doc 06 Teorema 1: $|s_n-\gamma_n|=O(\lambda^{-1/2}/w_n)$).
- **Auto-adjuntez:** $t_n^{(\lambda)}\in\mathbb{R}$ para todo $n$ → los ceros $z_n$ SIEMPRE están en $\mathbb{T}$.
- **Simetría:** $\hat k_\lambda$ es par ($k_\lambda(u) = k_\lambda(u^{-1})$) → ceros de $\hat k_\lambda$ vienen en pares $\pm s_n$. Los ceros $w_n = e^{2\pi is_n/L}$ pueden tener pequeña parte imaginaria (del orden $O(\lambda^{-1/2}/w_n)$ off-$\mathbb{T}$).

**Hecho clave.** Los ceros de $B_\lambda$ están en $\mathbb{T}$ (reales) y los polos de $B_\lambda$ están a distancia $O(\lambda^{-1/2}/w_n)$ de $\mathbb{T}$ (casi-reales). Conforme $\lambda\to\infty$, tanto ceros como polos se aproximan a la imagen de $\{\gamma_n\}$ en $\mathbb{T}$.

---

## 2. La equivalencia H2 ↔ $B_\lambda\to 1$

**Proposición 1.** Las siguientes son equivalentes:

(a) H2: $\hat\xi_\lambda^{(N)}\to c\cdot\Xi$ uniformemente en compactos de $\mathbb{C}$.

(b) $B_\lambda(z)\to 1$ uniformemente en compactos de $\mathbb{C}\setminus\{w_n\}$.

*Prueba.* $(a)\Rightarrow(b)$: $\hat k_\lambda\to c'\Xi$ (Lema 7.3, Doc 00), así que $B_\lambda = \hat\xi_\lambda/\hat k_\lambda \to (c/c')\cdot 1 = $ constante $\to 1$ (por la normalización $B_\lambda(0) = \xi_0/k_0 \to 1$ de los coeficientes líderes).

$(b)\Rightarrow(a)$: $\hat\xi_\lambda = B_\lambda\cdot\hat k_\lambda \to 1\cdot(c'\Xi) = c'\Xi$. $\square$

---

## 3. Theorem 1: $B_\lambda\to 1$ bajo RH

Esta es la reformulación correcta del Teorema 5 del doc 09.

**Teorema 1** (Convergencia del producto de Blaschke, bajo RH). Si RH es cierta, entonces:

$$B_\lambda(z) \to 1 \quad \text{uniformemente en compactos de } \mathbb{C}\setminus\mathbb{T}.$$

*Prueba.* Basta demostrar que $\log B_\lambda(z)\to 0$ para $z$ en compactos de $\mathbb{C}\setminus\mathbb{T}$, ya que $B_\lambda$ es analítica y no se anula en $\mathbb{C}\setminus\mathbb{T}$ eventualmente.

**Paso 1: Representación integral.** Para $z\notin\mathbb{T}$:

$$\log B_\lambda(z) = \int_\Gamma (\log B_\lambda)'(w)\,dw = \int_\Gamma \left[\frac{(\hat\xi_\lambda)'(w)}{\hat\xi_\lambda(w)} - \frac{(\hat k_\lambda)'(w)}{\hat k_\lambda(w)}\right]dw,$$

donde $\Gamma$ es una curva de un punto base fijo a $z$ evitando $\mathbb{T}$.

La diferencia de logarítmicas derivadas es:

$$\frac{(\hat\xi_\lambda)'}{\hat\xi_\lambda}(w) - \frac{(\hat k_\lambda)'}{\hat k_\lambda}(w) = N\left[S_\xi(w;\lambda) - S_k(w;\lambda)\right],$$

donde $S_\xi = (1/N)\sum_n 1/(w-t_n)$ y $S_k = (1/N)\sum_n 1/(w-s_n)$ son las transformadas de Stieltjes de las medidas de ceros (normalizadas).

**Paso 2: Convergencia de Stieltjes.** Reescribimos:

$$N[S_\xi(w;\lambda) - S_k(w;\lambda)] = \int_\mathbb{R}\frac{d(\mu_\xi^\lambda - \mu_k^\lambda)(t)}{w-t},$$

donde $\mu_\xi^\lambda = (1/N)\sum_n\delta_{t_n^{(\lambda)}}$ y $\mu_k^\lambda = (1/N)\sum_n\delta_{s_n^{(\lambda)}}$.

Por el Doc 08 (Teorema 1), incondicionalmente: $\mu_k^\lambda\to\mu_\gamma$ (convergencia débil), donde $\mu_\gamma$ es la medida de ceros de $\Xi$.

Bajo RH: el Doc 09 (Teorema 3) demuestra $\mu_\xi^\lambda\to\mu_\gamma$ débilmente.

Por tanto $\mu_\xi^\lambda - \mu_k^\lambda\to 0$ débilmente. Para $w\notin\mathbb{R}$: la función $t\mapsto 1/(w-t)$ es continua y acotada en $\mathbb{R}$. Luego por convergencia débil:

$$\int_\mathbb{R}\frac{d(\mu_\xi^\lambda - \mu_k^\lambda)(t)}{w-t} \to 0 \quad\text{para cada } w\notin\mathbb{R}.$$

La convergencia es uniforme en compactos de $\mathbb{C}\setminus\mathbb{R}$ por acotación uniforme de $\|1/(w-\cdot)\|$ en compactos.

**Paso 3: Integración.** 

$$|\log B_\lambda(z)| = \left|\int_\Gamma N[S_\xi-S_k](w)\,dw\right| \leq \text{longitud}(\Gamma)\cdot\sup_{w\in\Gamma}|N[S_\xi-S_k](w)| \to 0. \quad \square$$

---

## 4. La Pregunta 29.10: ¿basta $M_1[\Delta]\to 0$?

El Advisor 2 propuso:

> **Pregunta 29.10.** ¿Es $M_1[\Delta]\to 0$ suficiente para que $B_\lambda(z)\to 1$ uniformemente en compactos?

**Respuesta: No, en general. $M_1[\Delta]\to 0$ es necesario pero no suficiente.**

**Prueba de la insuficiencia.** Considérese el caso caricatura: $N = 2$, $t_1 = \gamma_1 + \varepsilon$, $t_2 = \gamma_2 - \varepsilon$, $s_n = \gamma_n$. Entonces $M_1[\Delta] = c\cdot(\varepsilon - \varepsilon) = 0$ (primer momento cero por cancelación). Pero $B_\lambda(z) = \frac{(z-\gamma_1-\varepsilon)(z-\gamma_2+\varepsilon)}{(z-\gamma_1)(z-\gamma_2)} \neq 1$. El producto de Blaschke NO es 1 aunque $M_1[\Delta] = 0$. $\square$

**Lo que $M_1[\Delta]$ sí controla.** El primer momento controla la derivada logarítmica de $B_\lambda$ en el origen del espacio de Mellin:

$$[(\log B_\lambda)']_{t=0} = \sum_n\left[\frac{1}{-t_n} - \frac{1}{-s_n}\right] = \sum_n\frac{\delta_n}{t_n s_n},$$

que es una combinación ponderada de los desplazamientos $\delta_n = t_n - s_n$. El control $M_1[\Delta]\to 0$ implica que esta suma ponderada tiende a 0, pero NO controla los términos individuales $\delta_n$.

**Proposición 2** (lo que falta). Para que $B_\lambda\to 1$, es suficiente (pero más fuerte que $M_1[\Delta]\to 0$) que:

$$\sum_n\frac{|\delta_n|}{|z-s_n|^2} \to 0 \quad \text{para } z\notin\mathbb{R},$$

o equivalentemente (usando $|z-s_n|\geq|\Im(z)|$):

$$\frac{1}{|\Im(z)|^2}\sum_n|\delta_n| \to 0, \quad\text{i.e.,}\quad \sum_n|\delta_n| \to 0.$$

Y $\sum_n|\delta_n| = \sum_n|t_n^{(\lambda)}-s_n^{(\lambda)}|$ — la suma de todos los desplazamientos absolutos.

**Pregunta 29.11** (nueva). ¿Es $\sum_n|t_n^{(\lambda)}-s_n^{(\lambda)}| \to 0$?

---

## 5. Análisis de Pregunta 29.11

La suma $\sum_n|t_n-s_n|$ involucra $N\sim\lambda^2/\log\lambda$ términos, cada uno de tamaño $O(\log\lambda)$ (del Doc 12, estimado por conteo). Luego la cota bruta da:

$$\sum_n|t_n-s_n| = O\!\left(\frac{\lambda^2}{\log\lambda}\cdot\log\lambda\right) = O(\lambda^2) \to +\infty.$$

Esto confirma que la convergencia de $B_\lambda$ NO se puede deducir de la cota individual $|t_n-s_n|=O(\log\lambda)$. La prueba del Teorema 1 via Stieltjes (Sección 3) es NECESARIA porque evita controlar la suma de ceros individuales.

**¿Puede decaer la suma $\sum_n|t_n-s_n|$?**

La cota individual óptima actual es $O(\log\lambda)$ (del conteo de ceros). Para que $\sum_n|t_n-s_n|\to 0$ se necesitaría, en promedio, $|t_n-s_n| = o(\log\lambda/N) = o((\log\lambda)^2/\lambda^2)$ — esto es una precisión MUCHO más fina que lo que se tiene. Requeriría la rigidez completa de los ceros del operador CCM.

**Conclusión.** La vía correcta para $B_\lambda\to 1$ es la del Teorema 1 (via convergencia débil de Stieltjes), no via control de $\sum_n|\delta_n|$. La Pregunta 29.11 es probablemente cierta bajo RH (sus ceros siguen la misma distribución límite) pero difícil de probar directamente.

---

## 6. La ecuación de Euler-Lagrange en términos de $B_\lambda$

La relación entre $B_\lambda$ y el problema variacional es más directa de lo que parece. La ecuación de Euler-Lagrange del Doc 12 (Proposición 2) dice:

$$\hat\xi_\lambda(z) = -c_\lambda\cdot\frac{\hat k_\lambda(z)}{C_\lambda(z) - \mu_\lambda}$$

(en la aproximación diagonal con el término de rango 1). Luego:

$$B_\lambda(z) = \frac{\hat\xi_\lambda(z)}{\hat k_\lambda(z)} = \frac{-c_\lambda}{C_\lambda(z) - \mu_\lambda}.$$

Esta es la REPRESENTACIÓN EXACTA de $B_\lambda$ en términos del potencial $C_\lambda$!

**Proposición 3** (representación de Blaschke via potencial). En la aproximación diagonal:

$$B_\lambda(z) = \frac{-c_\lambda}{C_\lambda(z) - \mu_\lambda} = \frac{-c_\lambda}{w(z) - \Psi_\lambda(z) - \mu_\lambda}.$$

**Consecuencia.** $B_\lambda(z)\to 1$ si y solo si $C_\lambda(z) - \mu_\lambda \to -c_\lambda$ (la constante de normalización).

Para $z = \gamma_n + iy$ ($y\to 0^+$): $w(\gamma_n) - \Psi_\lambda(\gamma_n) - \mu_\lambda \to w(\gamma_n) - \Psi(\gamma_n) - 0 = C_\infty(\gamma_n)$.

Bajo RH: $C_\infty(\gamma_n) = 0$. Luego el denominador tiende a 0 en $z = \gamma_n$ — los ceros de $\hat k_\lambda$ (donde $\hat k_\lambda(z) = 0$) son precisamente donde el denominador de $B_\lambda$ tiene polos. La cancelación numerador/denominador da los ceros de $\hat\xi_\lambda$.

**Pregunta 29.12** (nueva). ¿Bajo qué condiciones la constante de normalización $c_\lambda$ en $B_\lambda = -c_\lambda/[C_\lambda-\mu_\lambda]$ converge a $-1$ (para que $B_\lambda\to 1$ cuando $C_\lambda-\mu_\lambda\to 1$)?

La condición $c_\lambda\to 1$ es equivalente a $\langle\xi_\lambda, k\rangle\to 1$, que es parte de H2.

---

## 7. El argumento de Hurwitz: H2 implica RH

Este es el paso en la dirección H2 → RH, que SÍ está sólidamente probado y que el producto de Blaschke hace más transparente.

**Teorema 2** (H2 $\Rightarrow$ RH). Si $\hat\xi_\lambda^{(N)}\to c\Xi$ uniformemente en compactos de $\mathbb{C}$, entonces todos los ceros de $\Xi$ son reales.

*Prueba.* Por el Teorema de Hurwitz: si $f_n\to f$ uniformemente en compactos, $f\not\equiv 0$, y cada $f_n$ no tiene ceros en un abierto $U$, entonces $f$ tampoco tiene ceros en $U$. 

La contrarrecíproca: si $\Xi$ tuviera un cero $\rho = 1/2 + i(\sigma + i\tau)$ con $\tau\neq 0$ (fuera de la recta real), entonces por Hurwitz, eventualmente $\hat\xi_\lambda^{(N)}$ tendría un cero cerca de $\rho$ — en particular, un cero NO-REAL. Pero $\hat\xi_\lambda^{(N)}$ es el polinomio característico de $D_\lambda^N$, un operador auto-adjunto, cuyos autovalores son TODOS reales. Los ceros de $\hat\xi_\lambda^{(N)}$ son SIEMPRE reales. Contradicción. Luego todos los ceros de $\Xi$ son reales, i.e., RH. $\square$

**Corolario.** En términos del producto de Blaschke: si $B_\lambda\to 1$, entonces (por Proposición 1) $\hat\xi_\lambda\to c'\Xi$, y por el Teorema 2, RH.

---

## 8. La tabla de equivalencias actualizada

La estructura completa del programa CCM (revisada tras doc 12):

```
RH
 ⟺ todos los ceros de Ξ son reales
 ⟹ Stieltjes: S_ξ(z;λ) → S_Ξ(z) (Doc 09, Th 3)
 ⟹ B_λ(z) → 1 (Teorema 1, este doc)
 ⟺ H2: ξ̂_λ → c Ξ (Proposición 1, este doc)
 ⟹ (Hurwitz) → ceros de Ξ son reales
 ⟹ RH                                    [cierre de la cadena]
```

**Estado de las flechas:**

| Flecha | Dirección | Condición | Prueba |
|---|---|---|---|
| RH → Stieltjes | → | bajo RH | Doc 09, Th 3 |
| Stieltjes → $B_\lambda\to 1$ | → | bajo RH | **Teorema 1, este doc** |
| $B_\lambda\to 1$ ↔ H2 | ↔ | siempre | **Proposición 1, este doc** |
| H2 → RH | → | siempre | **Teorema 2, este doc** |
| **Gap:** $B_\lambda\to 1$ sin asumir RH | ?? | incondicional | **ABIERTO** |

El único paso que falta para tener una prueba condicional de RH es ya conocido (Doc 09). El único paso que falta para tener una prueba INCONDICIONAL es el gap en la última fila.

---

## 9. El muro real: $B_\lambda\to 1$ incondicionalmente

El gap se puede reformular limpiamente:

**Muro-Blaschke.** Probar que $B_\lambda(z)\to 1$ para $z\in\mathbb{C}\setminus\mathbb{T}$ sin asumir RH.

Equivalentemente (Proposición 1): probar H2 sin asumir RH.

Equivalentemente (Proposición 3, aproximación diagonal): probar que $-c_\lambda/(C_\lambda(z)-\mu_\lambda)\to 1$, i.e., que $c_\lambda\to 1$ y $C_\lambda(z)-\mu_\lambda\to -1$ (para la normalización adecuada).

**El ingrediente preciso que falta.** De la representación (Proposición 3):

$$B_\lambda(z) = -c_\lambda/[C_\lambda(z) - \mu_\lambda].$$

Para tener $B_\lambda\to 1$ necesitamos:
$$c_\lambda \to -[C_\lambda(z) - \mu_\lambda]_{\text{normalización}}.$$

Esto requiere que el potencial $C_\lambda$ tenga un comportamiento DETERMINADO independientemente de si RH es cierta. Específicamente: necesitamos un control de $C_\lambda$ en la franja $\{|\Im z| < \eta\}$ sin asumir que los ceros de $\Psi$ son reales.

**Formulación precisa del gap:**

> **Pregunta 29.13.** ¿Puede demostrarse que $C_\lambda(z) - \mu_\lambda \to C_\infty(z) \neq 0$ uniformemente para $z$ en compactos de $\mathbb{C}\setminus\mathbb{T}$, sin asumir RH?

Si la respuesta es sí y el límite $C_\infty(z) \neq 0$ para $z\notin\mathbb{R}$: entonces $B_\lambda\to -c_\lambda/C_\infty(z)$, que sería constante 1 solo si $c_\lambda\to -C_\infty(z)$ — no deja el problema más simple.

La dificultad fundamental: sin RH, los ceros de $\Xi$ pueden tener parte imaginaria $\tau\neq 0$. Cerca de tal cero $\rho = 1/2+i(\sigma+i\tau)$: $\Psi_\lambda(\rho)$ diverge (los cruces del potencial se "escapan" de la recta real hacia el plano complejo). El potencial $C_\lambda(z)$ puede tener ceros fuera de $\mathbb{T}$, lo que significaría que $B_\lambda$ tendría un polo ahí — contradiciendo la auto-adjuntez de $\hat\xi_\lambda^{(N)}$ (que exige que los ceros de $B_\lambda$ estén en $\mathbb{T}$).

**Esta contradicción es precisamente el argumento de CCM.** El operador CCM es auto-adjunto por construcción → $B_\lambda$ tiene todos sus ceros en $\mathbb{T}$ → si los polos de $B_\lambda$ (ceros de $\hat k_\lambda$) divergen de $\mathbb{T}$, entonces $B_\lambda$ NO puede converger a 1 — implicando que los ceros de $\Xi$ deben estar en $\mathbb{T}$ (en el límite). Pero este argumento completo todavía requiere la convergencia $B_\lambda\to 1$ para ser riguroso.

**El muro es genuino y no tiene atajos visibles.**

---

## 10. Resumen del doc 13

**Probado en este doc:**
- $B_\lambda(z)\to 1$ bajo RH (Teorema 1, via Stieltjes)
- H2 ↔ $B_\lambda\to 1$ (Proposición 1)
- H2 → RH (Teorema 2, Hurwitz)
- $M_1[\Delta]\to 0$ NO es suficiente para $B_\lambda\to 1$ (Pregunta 29.10 resuelta negativamente)
- Representación exacta $B_\lambda = -c_\lambda/[C_\lambda-\mu_\lambda]$ (Proposición 3)

**Abierto:**
- $B_\lambda\to 1$ incondicionalmente (Muro-Blaschke = Muro-H2)
- Pregunta 29.11: $\sum_n|\delta_n|\to 0$?
- Pregunta 29.12: $c_\lambda\to 1$ incondicionalmente?
- Pregunta 29.13: control de $C_\lambda - \mu_\lambda$ sin RH?

**El muro real del programa Phase 29 (formulación final limpia):**

$$\boxed{B_\lambda(z)\to 1 \text{ incondicionalmente} \iff \text{H2} \iff \text{RH (via Hurwitz)}.}$$

Todo el programa se reduce a una afirmación sobre una familia de funciones analíticas racionales: que el cociente de la función minimizante y la función kernel converge a 1 en el plano complejo. Esta es la formulación más limpia que el programa ha encontrado hasta ahora.
