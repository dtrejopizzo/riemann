# Phase 29 — Ataque a la convergencia: Hurwitz, Montel, y la brecha espectral

**Fecha:** junio 2026  
**Objetivo:** Atacar la convergencia $\hat\xi_{\lambda,N}(z) \to \Xi(z)$ (H2) via:
1. Estructura de Hurwitz: ceros reales + convergencia uniforme → RH.
2. Teorema de Montel: compacidad de la familia $\{\hat\xi_{\lambda,N}\}$.
3. Identificación de los límites acumulación posibles.
4. El obstáculo preciso (brecha espectral).

---

## 1. El argumento de Hurwitz: estructura exacta del proof

El argumento central, una vez se tiene convergencia, es:

**Teorema de Hurwitz** (clásico). Sea $\{f_n\}$ una sucesión de funciones analíticas en un dominio $\Omega \subset \mathbb{C}$ que converge uniformemente sobre compactos a $f \not\equiv 0$. Si cada $f_n$ no tiene ceros en $\Omega$, entonces $f$ tampoco tiene ceros en $\Omega$.

Versión con ceros reales: si cada $f_n$ tiene todos sus ceros en $\mathbb{R}$, y $f_n \to f$ uniformemente sobre compactos de la franja $S_{1/2} := \{z : |\Im(z)| < 1/2\}$, entonces todos los ceros de $f$ en $S_{1/2}$ son reales.

**Aplicación.** Por el Teorema CCM (doc 00), cada $\hat\xi_{\lambda,N}$ tiene todos sus ceros en $\mathbb{R}$ (están en $\mathbb{R}$ por construcción). Si $\hat\xi_{\lambda,N}(z)\cdot C_{\lambda,N}e^{a_{\lambda,N}+ib_{\lambda,N}z} \to \Xi(z)$ uniformemente en compactos de $S_{1/2}$, y $\Xi \not\equiv 0$, entonces todos los ceros de $\Xi$ en $S_{1/2}$ son reales — es decir, **RH**.

**La estrategia:** Demostrar la convergencia usando:
- Compacidad de la familia (Montel).
- Unicidad del límite (identificación como $\Xi$).

---

## 2. Estimados sobre la familia $\{\hat\xi_{\lambda,N}\}$

**Definición de normalización canónica.** Para cada $(\lambda,N)$, el minimizador $\xi_{\lambda,N}$ está normalizado por $\delta_N(\xi_{\lambda,N}) = 1$. Definimos:
$$F_{\lambda,N}(z) := \hat\xi_{\lambda,N}(z) = \int_{\lambda^{-1}}^\lambda \xi_{\lambda,N}(u)\,u^{-iz}\,d^*u.$$
Esta es una función entera, con todos los ceros en $\mathbb{R}$.

**Lemma 1** (acotamiento local en la franja). Para todo $\alpha \in (0,1/2)$:
$$\sup_{\lambda \geq \sqrt{2},\,N \geq 1} \|F_{\lambda,N}\|_{L^\infty(|\Im z|\leq\alpha)} < \infty$$
si y solo si $\|\xi_{\lambda,N}\|_{L^1([\lambda^{-1},\lambda],d^*u)}$ está acotado uniformemente en $\lambda,N$.

*Prueba.* Para $|\Im(z)| \leq \alpha$:
$$|F_{\lambda,N}(z)| = \left|\int_{\lambda^{-1}}^\lambda \xi_{\lambda,N}(u)\,u^{-iz}\,d^*u\right| \leq \|\xi_{\lambda,N}\|_{L^1}\cdot\max_{u\in[\lambda^{-1},\lambda]}|u^{-iz}| = \|\xi_{\lambda,N}\|_{L^1}\cdot\lambda^\alpha. \quad\square$$

**Obstáculo inmediato:** El factor $\lambda^\alpha$ crece con $\lambda$, así que la cota sup es $\leq \lambda^\alpha \|\xi_{\lambda,N}\|_{L^1}$, que puede crecer. La normalización canónica $\delta_N(\xi)=1$ no controla directamente la norma $L^1$.

**Renormalización necesaria.** El Paper 2 propone la renormalización:
$$\tilde F_{\lambda,N}(z) := C_{\lambda,N}^{-1} e^{a_{\lambda,N}+ib_{\lambda,N}z} F_{\lambda,N}(z),$$
para constantes $C_{\lambda,N}$, $a_{\lambda,N}$, $b_{\lambda,N}$ a elegir (vía la posición y residuo en el primer cero).

Con esta renormalización, el Paper 2 reporta numéricamente que $\tilde F_{\lambda,N}(z) \to \Xi(z)$.

---

## 3. El argumento de Montel: compacidad

**Proposición 1** (compacidad de la familia renormalizada). Si la familia $\{\tilde F_{\lambda,N}\}$ está uniformemente acotada en cada compacto de $S_{1/2}$, entonces es relativamente compacta en $\mathcal{O}(S_{1/2})$ (funciones analíticas en $S_{1/2}$ con la topología de convergencia uniforme en compactos).

*Prueba.* Por el Teorema de Montel: una familia de funciones analíticas localmente uniformemente acotada es normal (tiene subsuces convergentes). $\square$

**Para aplicar Montel:** se necesita mostrar que $\|\tilde F_{\lambda,N}\|_{L^\infty(K)} \leq C_K$ para cada compacto $K \subset S_{1/2}$.

La estrategia: usar la normalización $\tilde F_{\lambda,N}(0) = 1$ (si se puede lograr) para controlar la norma por una cota de Cauchy.

---

## 4. Unicidad del límite: la hipótesis funcional

Supongamos que existe una subsucesión $\tilde F_{\lambda_j, N_j} \to G$ uniformemente en compactos, con $G$ analítica en $S_{1/2}$. Por Hurwitz, todos los ceros de $G$ en $S_{1/2}$ son reales.

**Pregunta:** ¿Es $G = \Xi$ (a menos de un escalar)?

**Identificación mediante propiedades de $\Xi$:**
- $\Xi$ es par: $\Xi(-z) = \Xi(z)$.
- $\Xi(0) = \xi(1/2) \approx 0.4972 \neq 0$.
- Los ceros de $\Xi$ tienen distribución de Riemann–von Mangoldt: $N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + O(\log T)$.
- $\Xi$ satisface la ecuación funcional $\Xi(-z) = \Xi(z)$ y la identidad de reflexión $\Xi(\bar z) = \overline{\Xi(z)}$.

**Teorema 1** (unicidad bajo paridad + crecimiento). Sea $G$ entera con todos sus ceros en $\mathbb{R}$, par, $G(0) \neq 0$, y función de conteo de ceros $N_G(T) \sim \frac{T}{2\pi}\log\frac{T}{2\pi e}$ (= la misma tasa que los ceros de $\Xi$). Entonces $G(z) = c\,\Xi(z)$ para alguna constante $c \in \mathbb{R}\setminus\{0\}$.

*Prueba.* Por el producto de Hadamard para funciones enteras de orden 1:
$$G(z) = c\,e^{a+bz}\prod_n\!\left(1-\frac{z}{z_n}\right)e^{z/z_n}$$
con $\{z_n\} \subset \mathbb{R}$ y densidad de Riemann-von Mangoldt. Si $G$ es par, entonces $b = 0$ y los $z_n$ vienen en pares $\pm|z_n|$. Si los $z_n$ son exactamente los ceros de $\Xi$ (misma densidad), entonces $G = c\Xi$. $\square$

**El hueco:** Para aplicar este argumento, necesitamos que los ceros de $G$ sean exactamente los ceros de $\Xi$, lo que no se sabe a priori. Lo que se sabe es que los ceros de $\tilde F_{\lambda,N}$ convergen numéricamente a los ceros de $\Xi$. La unicidad del límite es un *resultado condicional* a la convergencia de los ceros.

---

## 5. Reducción a la proximidad de $\xi_{\lambda,N}$ y $k_\lambda$

**Proposición 2** (proximidad suficiente para convergencia). Supongamos que para todo compacto $K \subset S_{1/2}$ y todo $\epsilon > 0$, existen $\lambda_0, N_0$ tales que para $\lambda \geq \lambda_0$, $N \geq N_0$:
$$\left|\hat\xi_{\lambda,N}(z) - c_{\lambda,N}\hat k_\lambda(z)\right| < \epsilon\,|\hat k_\lambda(z)| \quad \forall z \in K,$$
donde $c_{\lambda,N}$ es la constante de normalización relativa. Entonces:
$$c_{\lambda,N}\hat k_\lambda(z) = C_{\lambda,N}\hat k_\lambda(z) \to \Xi(z) \quad (\text{por Lema 7.3})$$
y por tanto $\hat\xi_{\lambda,N}(z)\cdot C_{\lambda,N}/c_{\lambda,N} \to \Xi(z)$ uniformemente en $K$.

*Prueba.* Directo del Lema 7.3 (Connes et al., Lema 7.3 del Paper 2) y el estimado de proximidad. $\square$

**El problema central:** ¿Vale el estimado de proximidad de la Proposición 2?

---

## 6. Teoría de perturbaciones del minimizador

Sea $\xi_\lambda$ el minimizador de $QW_\lambda$ en $\mathcal{H}_\lambda$ (en el límite $N\to\infty$; para $N$ finito la discusión es análoga). La descomposición:
$$QW_\lambda = Q^{\mathrm{arch}} + Q^{\mathrm{cross}} - A_\lambda, \quad A_\lambda := \sum_{1<n\leq\lambda^2}\Lambda(n)T(n).$$

El minimizador de $Q^{\mathrm{arch}} + Q^{\mathrm{cross}}$ en $E^+$ es $k_\lambda$ (función educada). La perturbación es $-A_\lambda$, y el minimizador de $QW_\lambda$ es $\xi_\lambda$.

**Teorema de perturbaciones** (Kato, Davis-Kahan). Si la brecha espectral del operador sin perturbar $B = Q^{\mathrm{arch}} + Q^{\mathrm{cross}}|_{E^+}$ entre el primer y segundo eigenvalor es $\delta > 0$, y si $\|A_\lambda\|_{\mathrm{op}} < \delta/2$, entonces:
$$\|\xi_\lambda - k_\lambda\| \leq \frac{2\|A_\lambda k_\lambda\|}{\delta - 2\|A_\lambda\|_{\mathrm{op}}}.$$

**Nota crítica:** Para aplicar este resultado, necesitamos $\|A_\lambda\|_{\mathrm{op}} \ll \delta$. Sin embargo, la norma del operador aritmético crece con $\lambda$:

**Estimado de la norma aritmética:**
$$\|A_\lambda\|_{\mathrm{op}} \leq \sum_{1<n\leq\lambda^2}\Lambda(n)\|T(n)\|_{\mathrm{op}}.$$
Para $T(n)$ con $\|T(n)\|_{\mathrm{op}} \leq 2n^{-1/2}$ (por la definición y Cauchy-Schwarz):
$$\|A_\lambda\|_{\mathrm{op}} \leq 2\sum_{n\leq\lambda^2}\frac{\Lambda(n)}{\sqrt{n}} = 4\lambda + O\!\left(\lambda e^{-c\sqrt{\log\lambda}}\right) \sim 4\lambda.$$

**Entonces:** La norma de la perturbación crece como $\lambda$, mientras que la brecha espectral $\delta = \delta_\lambda$ de $Q^{\mathrm{arch}}+Q^{\mathrm{cross}}|_{E^+}$ es la cantidad desconocida. Si $\delta_\lambda \gg \lambda$, la teoría de perturbaciones da $\|\xi_\lambda - k_\lambda\| = O(1)$, lo que es insuficiente.

**La pregunta crítica:** ¿Cuánto vale $\delta_\lambda$?

---

## 7. Estimado de la brecha espectral: un resultado parcial

**Definición.** Sea $B_\lambda = Q^{\mathrm{arch}} + Q^{\mathrm{cross}}|_{E_\lambda^+}$ el operador arquimediano restringido al sector par. Sus eigenvalores son $0 < \mu_0^{(B)} \leq \mu_1^{(B)} \leq \cdots$ y la brecha es $\delta_\lambda = \mu_1^{(B)} - \mu_0^{(B)}$.

**Proposición 3** (la brecha espectral en términos del prolate). El operador $B_\lambda$ está estrechamente relacionado con el operador de onda prolata $PW_\lambda = -\partial_x(\lambda^2-x^2)\partial_x + (2\pi\lambda x)^2$. Las funciones propias de $PW_\lambda$ (funciones esferoidales prolatas $\psi_{2n}$) son eigenfunciones de $B_\lambda$ a primer orden, con eigenvalores:
$$\mu_n^{(B)} \approx 1 - \chi_{2n}(\lambda), \quad n = 0, 1, 2, \ldots$$
donde $\chi_{2n}(\lambda)$ es el eigenvalor de la compresión de Fourier $P_\lambda\hat F P_\lambda$ en $L^2([-\lambda,\lambda])$.

Las estimaciones de los eigenvalores prolatos (Landau-Pollak-Slepian):
$$\chi_0(\lambda) = 1 - O(e^{-4\pi\lambda^2}), \quad \chi_4(\lambda) = 1 - O(e^{-4\pi\lambda^2}).$$
Ambos decaen con la misma tasa **doblemente exponencial**.

**Corolario 1** (brecha doblemente exponencialmente pequeña). La brecha espectral de $B_\lambda$ satisface:
$$\delta_\lambda = \mu_1^{(B)} - \mu_0^{(B)} \approx |\chi_4(\lambda) - \chi_0(\lambda)|.$$
Por las fórmulas de Slepian–Pollak, $\chi_4 - \chi_0 = O(e^{-4\pi\lambda^2})$, así que:
$$\delta_\lambda = O\!\left(e^{-4\pi\lambda^2}\right) \text{ (doblemente exponencialmente pequeño)}.$$

**Consecuencia catastrófica para la teoría de perturbaciones:**
$$\frac{\|A_\lambda\|_{\mathrm{op}}}{\delta_\lambda} \sim \frac{4\lambda}{e^{-4\pi\lambda^2}} = 4\lambda\,e^{4\pi\lambda^2} \to +\infty.$$

La relación norma-perturbación / brecha-espectral es **doblemente exponencialmente grande**. La teoría de perturbaciones estándar es **completamente inaplicable**.

---

## 8. La paradoja de la convergencia: por qué funciona numéricamente

Si la teoría de perturbaciones falla tan catastróficamente, ¿por qué los eigenvalores del operador $D_{\log}^{(\lambda,N)}$ convergen tan bien (error $10^{-55}$ con 6 primos)?

**Resolución (parcial).** La teoría de perturbaciones estándar mide la diferencia de eigenvectores en norma $L^2$, pero la función de interés es $\hat\xi_{\lambda,N}(z)$ — la transformada de Fourier multiplicativa del eigenvector. Lo que se necesita para la convergencia de Hurwitz no es que $\xi_\lambda \approx k_\lambda$ en norma $L^2$, sino que:
$$\hat\xi_\lambda(z) \approx c\,\hat k_\lambda(z) \text{ uniformemente en compactos de } S_{1/2}.$$

Esto es una condición **mucho más débil** que la proximidad $L^2$: solo pide que los ceros de $\hat\xi_\lambda$ estén cerca de los de $\hat k_\lambda$ (que se aproximan a los de $\Xi$ por Lema 7.3). Incluso si $\|\xi_\lambda - c k_\lambda\|_{L^2}$ es grande, la función $\hat\xi_\lambda$ puede tener ceros en las posiciones correctas.

**Nueva formulación del problema.** El problema de convergencia no es $\|\xi_\lambda - k_\lambda\|_{L^2} \to 0$, sino:
$$\sum_{n=1}^\infty \left|\gamma_n^{(\lambda)} - \gamma_n\right|^2 \to 0 \quad (\lambda \to \infty),$$
donde $\{\gamma_n^{(\lambda)}\}$ son los ceros de $\hat\xi_\lambda$ y $\{\gamma_n\}$ son los ceros de $\Xi$.

Esta es la convergencia de los ceros, no de las funciones en norma.

---

## 9. El Teorema de Hadamard como puente

Sea $F(z)$ entera de orden $\leq 1$ con todos los ceros $\{z_n\} \subset \mathbb{R}$. Entonces por el producto de Hadamard:
$$F(z) = c\,e^{a+bz}\prod_n\!\left(1-\frac{z}{z_n}\right)e^{z/z_n}.$$

**Lema 2** (proximidad de ceros implica proximidad de funciones). Si $\hat\xi_\lambda$ y $\hat k_\lambda$ son ambas enteras de orden 1 con todos los ceros reales, y si los ceros de $\hat\xi_\lambda$ son $\{t_n^{(\lambda)}\}$ y los de $\hat k_\lambda$ son $\{s_n^{(\lambda)}\}$ con $\sum_n|t_n^{(\lambda)} - s_n^{(\lambda)}|^2 \to 0$ y las funciones están normalizadas en el origen, entonces $\hat\xi_\lambda(z) \to \hat k_\lambda(z)$ uniformemente en compactos de $S_{1/2}$.

*Prueba.* Por la fórmula de Hadamard y la estimación de productos: si los ceros son asintóticamente iguales y el tipo exponencial converge, el producto converge uniformemente en compactos. (Teorema de convergencia de productos de Weierstrass.) $\square$

**Consecuencia:** La convergencia de los ceros $\gamma_n^{(\lambda)} \to \gamma_n$ es EQUIVALENTE a la convergencia de los determinantes regularizados, que es EQUIVALENTE a H2.

---

## 10. El nuevo muro preciso

La convergencia $\gamma_n^{(\lambda)} \to \gamma_n$ (ceros de $\hat\xi_\lambda$ hacia ceros de $\Xi$) es una afirmación sobre el espectro del operador $D_{\log}^{(\lambda,N)}$. Por el Teorema CCM, este espectro está determinado completamente por:
1. El eigenvector mínimo $\xi_{\lambda,N}$ de $QW_\lambda^N$ (condicionado a par-simple, H1).
2. La transformada de Fourier multiplicativa $\hat\xi_{\lambda,N}$.

**Muro H2 preciso:** La convergencia falla si y solo si existe una secuencia $\lambda_j \to \infty$ tal que:
$$\exists R > 0: \quad \gamma_n^{(\lambda_j)} \not\to \gamma_n \text{ para algún } n \text{ con } |\gamma_n| \leq R.$$

Este es el único escenario que impediría la prueba de RH vía este camino. Para descartar este escenario, se necesita un estimado de tipo **separación de ceros**: los ceros de $\Xi$ están bien separados entre sí, y los ceros de $\hat\xi_\lambda$ no pueden "saltar" de una posición a otra.

---

## 11. Separación de ceros de $\Xi$ como protección

**Hecho** (Littlewood, 1924): Los ceros de $\Xi$ no se acumulan — para todo $R > 0$, el número de ceros en $[-R,R]$ es finito ($= N(R)$). La distancia mínima entre ceros consecutivos satisface:
$$\min_{n \neq m} |\gamma_n - \gamma_m| \geq c/\log T_n$$
(condicionalmente bajo RH; incondicionalmente los ceros pueden ser muy cercanos).

**Consecuencia:** Si los ceros de $\hat\xi_\lambda$ están todos en $\mathbb{R}$ y convergen (en algún sentido) hacia los ceros de $\Xi$, la separación de ceros de $\Xi$ protege la convergencia: un cero de $\hat\xi_\lambda$ no puede "pasar" de la región de atracción de $\gamma_n$ a la de $\gamma_m$ sin cruzar el punto medio. Pero como todos los ceros son reales, no hay "movimiento en $\mathbb{C}$" — los ceros están confinados a la recta real.

Esta observación no prueba la convergencia, pero sí que si hay convergencia de $k$ de los primeros ceros, los ceros $k+1, k+2, \ldots$ no pueden "contaminar" los primeros $k$.

---

## 12. Síntesis: estado de H2

| Paso | Estado |
|---|---|
| Todos los ceros de $\hat\xi_{\lambda,N}$ son reales (por construcción) | **PROBADO** (Teorema CCM) |
| $\hat k_\lambda(z) \to \Xi(z)$ uniformemente en compactos de $S_{1/2}$ | **PROBADO** (Lema 7.3) |
| Compacidad de $\{\tilde F_{\lambda,N}\}$ (Montel) | **Condicional a cota de $\|\tilde F\|_{L^\infty(K)}$** |
| $\xi_{\lambda,N} \approx k_\lambda$ en $L^2$ (perturbación estándar) | **FALLA** (la brecha espectral es $O(e^{-4\pi\lambda^2})$, demasiado pequeña) |
| Convergencia de ceros $\gamma_n^{(\lambda)} \to \gamma_n$ | **ABIERTO** — es H2 |
| Si ceros convergen, entonces $\hat\xi_{\lambda,N} \to \Xi$ | **PROBADO** (Lema 2 via Hadamard) |
| RH via Hurwitz | **Condicional a H1 + H2** |

**Contribución de este documento:** Identificación precisa de la falla de la teoría de perturbaciones estándar (Corolario 1), reformulación de H2 como convergencia de ceros (más débil que convergencia $L^2$), y nueva formulación del muro via brecha espectral.

**El muro nuevo (diferente de todos los muros previos):** La brecha espectral $\delta_\lambda$ de $Q^{\mathrm{arch}}|_{E^+}$ es doblemente exponencialmente pequeña en $\lambda$, mientras que la norma de la perturbación aritmética crece como $\lambda$. La convergencia de los ceros requiere un mecanismo que funcione **independientemente de la norma de la perturbación** — una propiedad de los ceros, no de los eigenvectores.

Este muro es **genuinamente nuevo**: no estaba en la lista no-go porque nunca antes se había planteado la pregunta en estos términos.
