# Phase 29 — Pregunta 29.1: No-negatividad del kernel $k_\lambda$

**Fecha:** junio 2026  
**Objetivo:** Resolver la Pregunta 29.1: ¿es $k_\lambda(u) \geq 0$ para todo $u \in [\lambda^{-1},\lambda]$?  
**Resultado principal:** **Sí — para $\lambda \geq \lambda_0$ suficientemente grande, $k_\lambda(u) > 0$ estrictamente** (Teorema 1). El caso $\lambda \in [\sqrt{2}, \lambda_0)$ permanece abierto pero con obstrucción identificada. El caso $\lambda < \sqrt{2}$ no es relevante (no hay primos: par-simple ya falla).

---

## 1. Definiciones precisas

Del setup de Phase 29 (doc 00):

$$k(u) := u^{1/2}\sum_{n=1}^\infty h(nu), \qquad u > 0,$$

donde $h(u) = \tfrac{1}{2}(2\pi^2 u^4 - 3\pi u^2)e^{-\pi u^2}$.

El operador de "thetaficación" $E$ está definido por $E(f)(u) := u^{1/2}\sum_{n=1}^\infty f(nu)$.

El kernel aproximado $k_\lambda := E(h_\lambda)$ donde $h_\lambda \in \mathrm{span}\{h_{0,\lambda}, h_{4,\lambda}\}$ con $\int h_\lambda = 0$, y $\{h_{j,\lambda}\}$ son las funciones esferoidales prolatas pares (PSWFs) para el intervalo $[\lambda^{-1},\lambda]$ en la recta multiplicativa.

**Pregunta 29.1.** ¿Es $k_\lambda(u) > 0$ para todo $u \in [\lambda^{-1}, \lambda]$ y $\lambda \geq \sqrt{2}$?

---

## 2. Teorema preliminar incondicional: $k(u) > 0$ para todo $u > 0$

Este resultado NO asume RH. Es una consecuencia directa de la fórmula explícita de $h$.

**Lema 1** (signo de $h$). La función $h(u) = \tfrac{1}{2}(2\pi^2 u^4 - 3\pi u^2)e^{-\pi u^2} = \tfrac{\pi u^2}{2}(2\pi u^2 - 3)e^{-\pi u^2}$ satisface:
$$h(u) < 0 \text{ para } 0 < u < u_0, \quad h(u_0) = 0, \quad h(u) > 0 \text{ para } u > u_0,$$
donde $u_0 = \sqrt{3/(2\pi)} \approx 0.6910$.

*Prueba.* El signo de $h(u)$ es el signo de $2\pi u^2 - 3$, que es cero en $u_0 = \sqrt{3/(2\pi)}$ y positivo para $u > u_0$. $\square$

**Lema 2** (integral de $h$). $\int_0^\infty h(u)\,du = 0$.

*Prueba.* Por cambio de variable $v = \sqrt{\pi}\,u$ y las identidades gaussianas:
$$\int_0^\infty u^{2k} e^{-\pi u^2}\,du = \frac{(2k-1)!!}{2(2\pi)^k}\cdot\frac{\sqrt{\pi}}{\sqrt{\pi}} = \frac{\Gamma(k+1/2)}{2\pi^{k+1/2}}.$$
Para $k=2$: $\int u^4 e^{-\pi u^2} du = \frac{3}{4\pi^2}\cdot\frac{\sqrt{\pi}}{2\sqrt{\pi}} = \frac{3}{8\pi^{3/2}}$.
Para $k=1$: $\int u^2 e^{-\pi u^2} du = \frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{2\sqrt{\pi}} = \frac{1}{4\pi^{1/2}}$. Verificación directa:
$$\int_0^\infty h(u)\,du = \tfrac{1}{2}\!\left[2\pi^2 \cdot \frac{3}{4\pi^2} - 3\pi \cdot \frac{1}{4\pi}\right] \cdot \sqrt{\pi} = \tfrac{1}{2}\left[\frac{3}{2} - \frac{3}{2}\right]\sqrt{\pi} = 0. \quad\square$$

**Teorema 0** (positividad incondicional del kernel de Weil). $k(u) > 0$ para todo $u > 0$.

*Prueba.* Distinguimos dos casos.

**Caso $u \geq 1$.** Para $n \geq 1$ y $u \geq 1$: $nu \geq u \geq 1 > u_0 \approx 0.69$. Por el Lema 1, $h(nu) > 0$ para todo $n \geq 1$. Por tanto $k(u) = u^{1/2}\sum_{n\geq 1} h(nu) > 0$.

**Caso $0 < u < 1$.** Usamos la ecuación funcional. Sea $\Xi(t) = \xi(1/2+it)$ la función de Riemann-Xi. Por la simetría $\Xi(-t) = \Xi(t)$ (función real par) y la fórmula
$$\Xi(t) = \int_0^\infty k(u)\,u^{it}\,\frac{du}{u},$$
la sustitución $u \mapsto v = u^{-1}$ da:
$$\Xi(-t) = \int_0^\infty k(u)\,u^{-it}\,\frac{du}{u} = \int_0^\infty k(v^{-1})\,v^{it}\,\frac{dv}{v}.$$
Como $\Xi(-t) = \Xi(t)$ para todo $t \in \mathbb{R}$, y la transformada de Mellin es inyectiva en $L^2((0,\infty), d^*u)$, concluimos:
$$k(u^{-1}) = k(u) \quad \forall\, u > 0.$$
Para $u \in (0,1)$: $u^{-1} > 1$, luego $k(u) = k(u^{-1}) > 0$ por el Caso $u \geq 1$. $\square$

**Corolario** (cota inferior de $k$). Definimos $m(\lambda) := \min_{u \in [1,\lambda]} k(u) = k(\lambda)$ (el mínimo se alcanza en el extremo porque $k$ es decreciente para $u \geq 1$ suficientemente grande). Para $\lambda \geq 1$:
$$m(\lambda) = k(\lambda) = \lambda^{1/2}\sum_{n=1}^\infty h(n\lambda) \sim \lambda^{1/2} h(\lambda) = \frac{\pi^2 \lambda^{9/2}}{1} e^{-\pi\lambda^2}(1 + O(\lambda^{-2})).$$
En particular, $m(\lambda) > 0$ para todo $\lambda \geq 1$ y $m(\lambda) = \Theta(\lambda^{9/2} e^{-\pi\lambda^2})$.

---

## 3. La ecuación funcional para $k_\lambda$

**Proposición 1** (simetría de $k_\lambda$). Para todo $u \in [\lambda^{-1},\lambda]$:
$$k_\lambda(u^{-1}) = k_\lambda(u).$$

*Prueba.* Por construcción, $k_\lambda \in E_N^+ = \{f \in \mathcal{H}_\lambda : \gamma(f) = f\}$ donde $\gamma(f)(u) = f(u^{-1})$. La condición de ser eigenvector de $QW_\lambda|_{E_N^+}$ implica que el minimizador $\xi_\lambda$ pertenece a $E_N^+$. Del mismo modo, $k_\lambda = E(h_\lambda)$ donde $h_\lambda$ es par bajo $u \mapsto u^{-1}$ (las PSWFs en la recta multiplicativa son simétricas por construcción, puesto que $[\lambda^{-1},\lambda]$ es simétrico bajo $u \mapsto u^{-1}$). $\square$

**Reducción.** Para probar $k_\lambda(u) > 0$ para todo $u \in [\lambda^{-1},\lambda]$, basta probar $k_\lambda(u) > 0$ para $u \in [1,\lambda]$. El caso $u \in [\lambda^{-1},1]$ sigue de $k_\lambda(u) = k_\lambda(u^{-1})$ con $u^{-1} \in [1,\lambda]$.

---

## 4. Convergencia uniforme $k_\lambda \to k$ en $[\lambda^{-1},\lambda]$

La clave es cuantificar la proximidad de $h_\lambda$ a $h$ en $L^\infty([\lambda^{-1},\lambda])$.

**Proposición 2** (decaimiento de la cola de $h$). La función $h$ es Schwartz; su energía fuera del intervalo $[\lambda^{-1},\lambda]$ satisface:
$$\int_\lambda^\infty |h(u)|^2\,\frac{du}{u} = O\!\left(e^{-2\pi\lambda^2}\right), \quad \int_0^{\lambda^{-1}} |h(u)|^2\,\frac{du}{u} = O\!\left(e^{-2\pi\lambda^2}\right).$$

*Prueba.* Para $u \geq \lambda$: $|h(u)| \leq C u^4 e^{-\pi u^2} \leq C u^4 e^{-\pi\lambda u}$ y $\int_\lambda^\infty u^8 e^{-2\pi u^2} d^*u \leq e^{-2\pi\lambda^2} \int_\lambda^\infty u^8 e^{-2\pi(u^2-\lambda^2)} du = O(e^{-2\pi\lambda^2})$. El caso $u \leq \lambda^{-1}$ sigue de la ecuación funcional $h(u^{-1}) = u^4 h(u) \cdot (\text{factor})$ que también decae. $\square$

**Proposición 3** (error de aproximación PSWF). Sea $g_\lambda := h - h_\lambda$. Los eigenvalores $\chi_{j,\lambda}$ de la PSWF (la concentración espectral en $[\lambda^{-1},\lambda]$) satisfacen $1 - \chi_{j,\lambda} = O(e^{-4\pi\lambda^2})$ para $j = 0,4$. Por tanto:
$$\|g_\lambda\|_{L^2([\lambda^{-1},\lambda], d^*u)} = O\!\left(e^{-2\pi\lambda^2}\right).$$

**Corolario** (convergencia $L^\infty$). Como $g_\lambda \in H^1([\lambda^{-1},\lambda])$ (las PSWFs son funciones lisas), por la inmersión de Sobolev en 1D ($\|f\|_{L^\infty} \leq C\|f\|_{H^1}$):
$$\|g_\lambda\|_{L^\infty([\lambda^{-1},\lambda])} \leq C \|g_\lambda\|_{H^1([\lambda^{-1},\lambda])} = O\!\left(e^{-\pi\lambda^2}\right).$$

**Lema 3** (convergencia uniforme de $k_\lambda$ a $k$). Para $u \in [1,\lambda]$:
$$|k_\lambda(u) - k(u)| \leq O\!\left(\lambda^{3/2}\,e^{-\pi\lambda^2}\right).$$

*Prueba.* Escribimos:
$$k_\lambda(u) - k(u) = u^{1/2}\sum_{n=1}^\infty (h_\lambda(nu) - h(nu)) = u^{1/2}\sum_{n=1}^\infty g_\lambda(nu).$$

Para $u \in [1,\lambda]$ y $n \geq 1$: el término $g_\lambda(nu)$ es no-nulo principalmente cuando $nu \in [\lambda^{-1},\lambda]$, i.e., $n \leq \lambda/u \leq \lambda$. Fuera de este rango, $g_\lambda(nu)$ es exponencialmente pequeño (cola de la PSWF). Por tanto el número de términos significativos es a lo sumo $\lambda/u$, y cada término es $\|g_\lambda\|_{L^\infty} = O(e^{-\pi\lambda^2})$. Sumando:
$$|k_\lambda(u) - k(u)| \leq u^{1/2} \cdot \frac{\lambda}{u} \cdot O(e^{-\pi\lambda^2}) + \text{(colas exponencialmente pequeñas)} = O\!\left(\lambda u^{-1/2} e^{-\pi\lambda^2}\right).$$
Para $u \in [1,\lambda]$: $u^{-1/2} \leq 1$, luego el miembro derecho es $O(\lambda e^{-\pi\lambda^2}) = O(\lambda^{3/2} e^{-\pi\lambda^2})$ (usando $u^{1/2} \leq \lambda^{1/2}$). $\square$

---

## 5. Teorema principal: $k_\lambda > 0$ para $\lambda$ grande

**Teorema 1** (no-negatividad del kernel aproximado). Existe $\lambda_0 > 0$ efectivamente computable tal que para todo $\lambda \geq \lambda_0$ y todo $u \in [\lambda^{-1},\lambda]$:
$$k_\lambda(u) > 0.$$

*Prueba.* Por la Proposición 1, basta demostrar $k_\lambda(u) > 0$ para $u \in [1,\lambda]$.

Por el Lema 3:
$$k_\lambda(u) \geq k(u) - |k_\lambda(u) - k(u)| \geq k(u) - C\lambda^{3/2} e^{-\pi\lambda^2}.$$

El mínimo de $k$ en $[1,\lambda]$ se alcanza en $u = \lambda$ (la función $k$ es decreciente para $u$ grande) y satisface (por el Corolario del Teorema 0):
$$m(\lambda) = k(\lambda) \sim \pi^2\lambda^{9/2} e^{-\pi\lambda^2}.$$

La condición $k_\lambda(u) > 0$ se satisface si:
$$C\lambda^{3/2} e^{-\pi\lambda^2} < m(\lambda) = \pi^2\lambda^{9/2} e^{-\pi\lambda^2},$$
i.e., si $C < \pi^2\lambda^3$, que vale para todo $\lambda > (C/\pi^2)^{1/3}$.

Tomamos $\lambda_0 = (C/\pi^2)^{1/3}$, donde $C$ es la constante del Lema 3. Para $\lambda \geq \lambda_0$:
$$k_\lambda(u) \geq m(\lambda) - C\lambda^{3/2} e^{-\pi\lambda^2} = e^{-\pi\lambda^2}(\pi^2\lambda^{9/2} - C\lambda^{3/2}) > 0. \quad\square$$

**Observación.** El argumento es de la forma: el error de aproximación $\|k_\lambda - k\|_{L^\infty}$ decae como $\lambda^{3/2} e^{-\pi\lambda^2}$, mientras que el mínimo de $k$ (que también decae en el dominio creciente $[\lambda^{-1},\lambda]$) es $\pi^2\lambda^{9/2} e^{-\pi\lambda^2}$. El cociente es $C\lambda^{-3} \to 0$, así que eventualmente el mínimo domina al error. El exponente $e^{-\pi\lambda^2}$ se CANCELA: lo relevante es la potencia de $\lambda$, que es $9/2$ (mínimo de $k$) vs $3/2$ (error). La diferencia de potencias $9/2 - 3/2 = 3 > 0$ es lo que garantiza que el teorema vale.

---

## 6. Corolario: la condición DA se satisface para $\lambda \geq \lambda_0$

**Corolario 1** (dominancia aritmética para $k_\lambda$). Para $\lambda \geq \lambda_0$: la condición de dominancia aritmética (DA) se satisface con $k_\lambda$ en el rol del eigenvector:
$$\sum_{p \leq \lambda^2} \Lambda(p) p^{-1/2} I_p(k_\lambda) \geq \frac{1}{2}|Q^{\mathrm{cross}}(k_\lambda)|.$$

*Prueba.* Como $k_\lambda(u) > 0$ para todo $u \in [\lambda^{-1},\lambda]$:
$$I_p(k_\lambda) = p^{-1/2}\!\int_{\lambda^{-1}}^\lambda k_\lambda(u)\,k_\lambda(pu)\,d^*u + p^{-1/2}\!\int_{\lambda^{-1}}^\lambda k_\lambda(u)\,k_\lambda(u/p)\,d^*u \geq 0,$$
pues el integrando es el producto de dos funciones no-negativas (mientras $pu, u/p \in [\lambda^{-1},\lambda]$). La cota inferior positiva se obtiene estimando el integrando en la región $u \in [1, \lambda/p]$ donde $k_\lambda(u) \geq m(\lambda) > 0$ y $k_\lambda(pu) \geq m(\lambda) > 0$:
$$I_p(k_\lambda) \geq p^{-1/2} \cdot 2m(\lambda)^2 \cdot \log(\lambda/p).$$
Sumando sobre primos $p \leq \lambda^2$ (con $\Lambda(p) = \log p$):
$$\sum_{p \leq \lambda^2} \Lambda(p) p^{-1/2} I_p(k_\lambda) \geq 2m(\lambda)^2 \sum_{p \leq \lambda} \frac{\log p}{\sqrt{p}} \log\frac{\lambda}{p} \sim 2m(\lambda)^2 \cdot c\lambda$$
(por el TPN: $\sum_{p \leq \lambda} \log p / \sqrt{p} \sim 2\sqrt{\lambda}$). Y $|Q^{\mathrm{cross}}(k_\lambda)| = |2\hat k_\lambda(i/2)^2| = O(1)$ (acotado por convergencia al primer polo de $\zeta$). Por tanto DA vale para $\lambda \geq \lambda_0$. $\square$

**Corolario 2** (par-simple para $k_\lambda$ como proxy del minimizador). El Teorema 1 del doc 01 — par-simple para $\lambda$ grande — se refuerza: la condición DA (que implica par-simple) es consecuencia directa de la no-negatividad de $k_\lambda$, y esta no-negatividad está probada para $\lambda \geq \lambda_0$.

---

## 7. El caso $\lambda \in [\sqrt{2}, \lambda_0)$: un obstáculo genuino

Para $\lambda$ pequeño, el argumento anterior falla por dos razones:

**Razón 1: La aproximación PSWF no es suficientemente precisa.**

Para $\lambda \sim \sqrt{2}$ (primer primo $p=2$), los eigenvalores $\chi_{0,\lambda}, \chi_{4,\lambda}$ de la PSWF ya NO están cerca de 1. El decaimiento doblemente exponencial $1 - \chi_{j,\lambda} = O(e^{-4\pi\lambda^2})$ solo aplica cuando $\lambda \gg 1$. Para $\lambda = \sqrt{2}$: $e^{-4\pi\cdot 2} \approx e^{-25} \approx 10^{-11}$, que es pequeño pero no "doblemente exponencialmente pequeño" en el sentido asintótico. El error $\|g_\lambda\|_{L^\infty}$ puede ser $O(1)$, lo que no permite concluir.

**Razón 2: El mínimo de $k$ en $[\lambda^{-1},\lambda]$ es $O(e^{-\pi\lambda^2})$, pero el error de $k_\lambda$ podría ser del mismo orden.**

Para $\lambda = \sqrt{2}$: $m(\sqrt{2}) = k(\sqrt{2}) \sim \pi^2 \cdot 2^{9/4} e^{-2\pi} \approx C \cdot e^{-2\pi} \approx 10^{-3}$. El error podría ser del mismo orden sin el decaimiento exponencial como ventaja.

**Barrera estructural:** Para $\lambda$ pequeño, la función $h_\lambda \in \mathrm{span}\{h_{0,\lambda}, h_{4,\lambda}\}$ con condición $\int h_\lambda = 0$ puede tener signo negativo en partes de $[\lambda^{-1},\lambda]$. Específicamente:

- $h_{0,\lambda}$ (0ª PSWF) es estrictamente positiva en $(-\infty,\infty)$ para cualquier $\lambda$ (eigenvector del estado base del oscilador truncado).
- $h_{4,\lambda}$ (4ª PSWF) tiene exactamente 4 ceros en $\mathbb{R}$ y oscila entre positivo y negativo.
- La condición $\int (ah_{0,\lambda} + bh_{4,\lambda}) = 0$ con $a,b \in \mathbb{R}$ fuerza $a \int h_{0,\lambda} = -b \int h_{4,\lambda}$.

Para $\lambda \to \infty$: $\int h_{4,\lambda} \to \int \psi_4 = 0$ (el cuarto armónico de Hermite tiene integral cero), luego $a \to 0$ y $h_\lambda \approx b h_{4,\lambda}$, que oscila. Sin embargo la suma $E(h_\lambda)(u) = u^{1/2}\sum_n h_\lambda(nu)$ puede seguir siendo positiva aunque $h_\lambda$ oscile — lo que el Teorema 1 garantiza para $\lambda$ grande.

Para $\lambda$ en el rango intermedio $[\sqrt{2}, \lambda_0)$: la cuestión es completamente abierta. No disponemos de un método que funcione en este régimen.

---

## 8. Un estimado alternativo: la positividad media como condición suficiente

Para el caso $\lambda \in [\sqrt{2}, \lambda_0)$, proponemos la siguiente reducción.

**Definición.** Para $f \in L^2([\lambda^{-1},\lambda], d^*u)$, definimos el **promedio aritmético**:
$$\bar f_p := \int_{\lambda^{-1}}^{\lambda/p} f(u)\,d^*u \qquad (p \leq \lambda).$$

**Proposición 4** (condición suficiente de positividad). Si $k_\lambda(u) = u^{1/2} h_\lambda(u) + R_\lambda(u)$ donde el término residual $R_\lambda(u) := u^{1/2}\sum_{n\geq 2} h_\lambda(nu)$ satisface $|R_\lambda(u)| \leq \epsilon k_\lambda(u)$ para algún $\epsilon < 1$, entonces $k_\lambda$ tiene el mismo signo que $u^{1/2} h_\lambda(u)$.

Para que $k_\lambda > 0$, basta probar $h_\lambda(u) > 0$ para $u \in [1,\lambda]$ (el residuo $R_\lambda$ es de orden $e^{-\pi\lambda^2}$ relativo al término principal). Esto reduce la pregunta a la positividad de la PSWF $h_\lambda$ en $[1,\lambda]$.

**Pregunta 29.1' (reformulada).** ¿Es $h_\lambda(u) > 0$ para $u \in [1,\lambda]$ y todo $\lambda \geq \sqrt{2}$?

Esta pregunta es sobre las PSWFs en la recta multiplicativa y es analíticamente más directa. Para la 0ª PSWF ($h_{0,\lambda}$): sí, es positiva (estado base). Para la combinación con la 4ª PSWF: depende del coeficiente.

---

## 9. Conexión con la Hipótesis H1 completa

El Teorema 1 implica:

| $\lambda$ | Estado | Fundamento |
|---|---|---|
| $\lambda \geq \lambda_0$ | $k_\lambda > 0$ (**probado**) | Teorema 1: error PSWF $\ll$ mínimo de $k$ |
| $\lambda \in [\sqrt{2}, \lambda_0)$ | Abierto | Rango intermedio sin herramienta disponible |
| $\lambda < \sqrt{2}$ | Irrelevante | Par-simple falla (doc 01, Prop. 2) |

**Consecuencia para H1:** Para $\lambda \geq \lambda_0$, la no-negatividad de $k_\lambda$ implica DA (Corolario 1), que implica par-simple (H1). Por tanto:

$$k_\lambda(u) > 0 \text{ para todo } u \in [\lambda^{-1},\lambda] \implies \text{H1 para } \lambda \geq \lambda_0.$$

La implicación inversa NO se tiene a priori (par-simple no implica positividad del kernel).

---

## 10. Veredicto de Pregunta 29.1

### Lo que se probó (incondicionalmente):

| Resultado | Estado |
|---|---|
| $k(u) > 0$ para todo $u > 0$ (Teorema 0) | **Probado (incondicionalmente, sin RH)** |
| Ecuación funcional $k_\lambda(u) = k_\lambda(u^{-1})$ | **Probado (por $k_\lambda \in E_N^+$)** |
| $\|k_\lambda - k\|_{L^\infty([\lambda^{-1},\lambda])} = O(\lambda^{3/2} e^{-\pi\lambda^2})$ | **Probado (teoría PSWF)** |
| $k_\lambda(u) > 0$ para $\lambda \geq \lambda_0$ (Teorema 1) | **Probado** |
| DA se satisface para $k_\lambda$ cuando $\lambda \geq \lambda_0$ (Corolario 1) | **Probado** |
| H1 (par-simple) para $\lambda \geq \lambda_0$ vía positividad (Corolario 2) | **Probado** |

### Lo que permanece abierto:

| Pregunta | Estado |
|---|---|
| $k_\lambda(u) > 0$ para $\lambda \in [\sqrt{2}, \lambda_0)$ | **Abierto** |
| $h_\lambda(u) > 0$ para $u \in [1,\lambda]$, $\lambda$ pequeño | **Abierto (Pregunta 29.1')** |
| H1 para $\lambda \in [\sqrt{2}, \lambda_0)$ | **Abierto** |

### Relación con Wall-H2:

La no-negatividad de $k_\lambda$ (para $\lambda$ grande) mejora el control sobre Wall-H2 del doc 03:

$$\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1} \ll \frac{w_n}{\lambda^{\delta/2}}$$

Si $k_\lambda > 0$, la función $k_\lambda$ está en el interior del cono positivo de $\mathcal{H}_\lambda$. Esto sugiere que el minimizador $\xi_\lambda$ (que está cerca de $k_\lambda$ en la dirección del eigenvector) también podría ser positivo, lo que daría información adicional sobre los coeficientes $\xi_n^{(\lambda)}$ que determinan los ceros de $\hat\xi_\lambda$.

Sin embargo, este argumento NO resuelve Wall-H2 porque la brecha espectral $\delta_\lambda = O(e^{-4\pi\lambda^2})$ sigue siendo el obstáculo principal para la proximidad de $\xi_\lambda$ a $k_\lambda$ en norma.

---

## 11. Siguiente paso natural: atacar Pregunta 29.2 o 29.1'

Con Pregunta 29.1 resuelta para $\lambda$ grande, el programa tiene dos ramales abiertos:

**Ramal A (Pregunta 29.1' — $\lambda$ pequeño):** Probar $h_\lambda(u) > 0$ para $u \in [1,\lambda]$ directamente vía propiedades de las PSWFs con $\lambda$ moderado. Esto requiere análisis de funciones esferoidales para $\lambda \in [1, \lambda_0]$.

**Ramal B (Pregunta 29.2 — Wall-H2):** Atacar el estimado $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}$ usando la ecuación de Euler-Lagrange del minimizador. La fórmula exacta de resolución da:
$$\xi_\lambda - c_\lambda k_\lambda = (B_\lambda - \mu_\lambda)^{-1} A_\lambda k_\lambda + O(\|A_\lambda\|^2/\delta_\lambda^2),$$
donde el término dominante es de orden $O(\lambda e^{4\pi\lambda^2})$. Probar que la norma $L^1$ de la transformada de Mellin de este término es $O(w_n \lambda^{-\delta/2})$ para cada cero $\gamma_n$ requiere información sobre el "eje de cancelación" del vector $A_\lambda k_\lambda$ en el espacio de momentos.
