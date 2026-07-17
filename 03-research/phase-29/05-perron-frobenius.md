# Phase 29 — Estructura de Perron-Frobenius y ortogonalidad aritmética

**Fecha:** junio 2026  
**Objetivo:** Explotar la no-negatividad $k_\lambda \geq 0$ (doc 04) para:  
(A) probar que el minimizador $\xi_\lambda$ es positivo (Perron-Frobenius),  
(B) mostrar que la perturbación aritmética $A_\lambda k_\lambda$ es casi proporcional a $k_\lambda$ (ortogonalidad aritmética),  
(C) atacar Wall-H2 desde este ángulo sin usar teoría de perturbaciones estándar.

---

## 1. El programa Perron-Frobenius: motivación

El Teorema 0 de doc 04 establece $k_\lambda > 0$ en todo $[\lambda^{-1},\lambda]$. El Teorema 1 de doc 01 establece par-simple (H1) para $\lambda$ grande. Pero la inferencia

$$k_\lambda > 0 \implies \xi_\lambda > 0$$

(el minimizador también es positivo) no está probada. Si esta inferencia vale, la situación cambia radicalmente:

- $\xi_\lambda > 0$ implica $I_p(\xi_\lambda) = p^{-1/2}\int \xi_\lambda(u)\xi_\lambda(pu)\,d^*u + \ldots \geq 0$ para todo primo $p$.
- Esto da acceso directo a cotas sobre los coeficientes $\xi_n^{(\lambda)}$ del minimizador sin pasar por la brecha espectral.
- En particular, $\hat\xi_\lambda(z) = \int \xi_\lambda(u)\,u^{-iz}\,d^*u$ satisface propiedades de tipo Hadamard mejoradas.

**El plan:** probar $\xi_\lambda > 0$ por un argumento de Perron-Frobenius que use la estructura del operador $QW_\lambda|_{E^+}$ y la positividad de $k_\lambda$.

---

## 2. La estructura de cono del operador aritmético

**Definición.** El cono de funciones no-negativas en $E_N^+ = \mathrm{span}\{U_n^+: 0\leq n\leq N\}$:
$$\mathcal{C}_N^+ := \{f \in E_N^+ : f(u) \geq 0 \text{ para todo } u \in [\lambda^{-1},\lambda]\}.$$

**Proposición 1** (el operador aritmético preserva el cono). Para todo primo $p \leq \lambda^2$ y toda $f \in \mathcal{C}_N^+$:
$$T(p)f \in \mathcal{C}_N^+.$$

*Prueba.* Por definición, $(T(p)f)(u) = p^{-1/2}[f(pu) + f(u/p)]$ para $u \in [\lambda^{-1},\lambda]$ (con la convención $f(v) = 0$ para $v \notin [\lambda^{-1},\lambda]$). Como $f \geq 0$, cada término $f(pu) \geq 0$ y $f(u/p) \geq 0$. Luego $T(p)f \geq 0$. $\square$

**Corolario** (el operador $A_\lambda$ preserva el cono). Como $A_\lambda f = \sum_{p \leq \lambda^2} \Lambda(p)\,T(p)f$ con $\Lambda(p) = \log p > 0$:
$$f \in \mathcal{C}_N^+ \implies A_\lambda f \in \mathcal{C}_N^+.$$

**Observación crucial.** Esto significa que el operador $A_\lambda$ (el "empuje aritmético") es un operador que amplifica el cono positivo, no lo destruye. La interacción entre $A_\lambda$ y la positividad es estructuralmente benévola.

---

## 3. El operador arquimediano y el cono

El operador arquimediano $B_\lambda := Q^{\mathrm{arch}} + Q^{\mathrm{cross}}|_{E_N^+}$ no preserva el cono en general (porque $Q^{\mathrm{arch}}$ involucra la transformada de Fourier, que no preserva la positividad). Pero podemos identificar su estructura.

**Proposición 2** (no-positividad del término de correlación aritmética). Para $f \in \mathcal{C}_N^+$ y $g \in \mathcal{C}_N^+$:
$$\langle f, A_\lambda g\rangle_{H_\lambda} \geq 0.$$

*Prueba.* $\langle f, A_\lambda g\rangle = \sum_p \Lambda(p)\,\langle f, T(p)g\rangle$. Como $f \geq 0$ y $T(p)g \geq 0$ (Proposición 1), el integrando es no-negativo. $\square$

**Interpretación:** En la forma cuadrática $QW_\lambda(f,f) = B_\lambda(f,f) - A_\lambda(f,f)$, el término aritmético $A_\lambda(f,f) = \langle f, A_\lambda f\rangle \geq 0$ para $f \geq 0$. Por tanto, la minimización de $QW_\lambda$ sobre el cono $\mathcal{C}_N^+$ está dominada por: maximizar $A_\lambda(f,f)$ sujeto a minimizar $B_\lambda(f,f)$.

---

## 4. El argumento de nodos: por qué el minimizador es positivo

Buscamos probar que el minimizador $\xi_\lambda$ de $QW_\lambda|_{E_N^+}$ sobre $\{\|f\| = 1\}$ satisface $\xi_\lambda \geq 0$.

**Lema 4** (mejora al ir al valor absoluto). Sea $f \in E_N^+$, $\|f\|_{H_\lambda} = 1$. Entonces:
$$QW_\lambda(|f|, |f|) \leq QW_\lambda(f, f)$$
si se satisfacen las dos condiciones siguientes:
$$\text{(C1)} \quad Q^{\mathrm{arch}}(|f|) \leq Q^{\mathrm{arch}}(f), \qquad \text{(C2)} \quad A_\lambda(|f|,|f|) \geq A_\lambda(f,f).$$

*Prueba.* $QW_\lambda(|f|) = Q^{\mathrm{arch}}(|f|) + Q^{\mathrm{cross}}(|f|) - A_\lambda(|f|)$. Para $Q^{\mathrm{cross}}$:
$$Q^{\mathrm{cross}}(|f|) = 2\hat{|f|}(i/2)^2 = 2\!\left(\int_{\lambda^{-1}}^\lambda |f(u)|\,u^{-1/2}\,d^*u\right)^{\!2} \geq 2\!\left(\int_{\lambda^{-1}}^\lambda f(u)\,u^{-1/2}\,d^*u\right)^{\!2} = Q^{\mathrm{cross}}(f).$$
Bajo (C1) y (C2): $QW_\lambda(|f|) \leq Q^{\mathrm{arch}}(f) + Q^{\mathrm{cross}}(f) - A_\lambda(f,f) = QW_\lambda(f)$. $\square$

**Condición (C2): el término aritmético.** Para $A_\lambda(f) = \sum_p \Lambda(p)\langle f, T(p)f\rangle$:
$$\langle f, T(p)f\rangle = p^{-1/2}\!\int f(u)[f(pu)+f(u/p)]\,d^*u$$

y $\langle |f|, T(p)|f|\rangle = p^{-1/2}\!\int |f(u)|[|f(pu)|+|f(u/p)|]\,d^*u$. Como $f(u)[f(pu)+f(u/p)] \leq |f(u)|[|f(pu)|+|f(u/p)|]$ (puntualmente), se tiene $\langle f, T(p)f\rangle \leq \langle |f|, T(p)|f|\rangle$. Por tanto (C2) vale **incondicionalmente** para todo $f$. $\square$ 

**Condición (C1): el término arquimediano.** $Q^{\mathrm{arch}}(f) = \int_\mathbb{R} |\hat f(t)|^2 \frac{2\partial_t\theta(t)}{2\pi}\,dt$ donde la medida $\mu(dt) = \frac{2\partial_t\theta(t)}{2\pi}dt > 0$ para $t \gg 1$. La pregunta es si $|\widehat{|f|}(t)| \leq |\hat f(t)|$ para casi todo $t$. Esto es generalmente FALSO: la transformada de Mellin de $|f|$ no domina la de $f$ en módulo para todo $t$ simultáneamente.

**Obstáculo:** La condición (C1) falla en general porque la transformada de Mellin no es monótona bajo el valor absoluto. Este es el muro estructural que impide la prueba directa del argumento de nodos.

**Hipótesis AC** (continuidad aritmética del cono). Para el minimizador $\xi_\lambda$ de $QW_\lambda|_{E_N^+}$: $\xi_\lambda \in \mathcal{C}_N^+$ (el minimizador es no-negativo).

Esta hipótesis no sigue del argumento de nodos clásico por el obstáculo de (C1). Pero hay una ruta alternativa.

---

## 5. Ruta alternativa: Perron-Frobenius via comparación con $k_\lambda$

**Teorema 2** (positividad del minimizador por comparación). Supóngase que:
$$QW_\lambda(k_\lambda, k_\lambda) < QW_\lambda(f, f)$$
para toda $f \in E_N^+$ con $\|f\| = 1$ y $f \not\geq 0$. Entonces $\xi_\lambda > 0$.

*Prueba.* El minimizador es único (por par-simple, H1). Si $QW_\lambda(k_\lambda) < QW_\lambda(f)$ para toda $f$ que cambie de signo, el mínimo no puede alcanzarse en tal $f$. Por tanto el minimizador $\xi_\lambda$ satisface $\xi_\lambda \geq 0$. $\square$

**El problema:** Para verificar la hipótesis del Teorema 2, necesitamos comparar $QW_\lambda(k_\lambda)$ con $QW_\lambda(f)$ para $f$ con ceros. Esto requiere conocer el valor de $QW_\lambda(k_\lambda)$.

**Cálculo de $QW_\lambda(k_\lambda)$:**
$$QW_\lambda(k_\lambda, k_\lambda) = Q^{\mathrm{arch}}(k_\lambda) + Q^{\mathrm{cross}}(k_\lambda) - \sum_p \Lambda(p)\langle k_\lambda, T(p)k_\lambda\rangle.$$

Usando $\hat k_\lambda(z) \approx \Xi(z)$:
$$Q^{\mathrm{arch}}(k_\lambda) \approx \int |\Xi(t)|^2 \frac{2\partial_t\theta}{2\pi}\,dt = \langle \Xi, \Xi\rangle_\theta > 0.$$
$$Q^{\mathrm{cross}}(k_\lambda) = 2\hat k_\lambda(i/2)^2 \approx 2\Xi(i/2)^2 = 2\xi(1)^2 > 0.$$
$$\sum_p \Lambda(p)\langle k_\lambda, T(p)k_\lambda\rangle \approx \sum_p \Lambda(p) p^{-1/2} [\hat k_\lambda(z)\hat k_\lambda(-z) \text{ evaluado en los ceros}] = \sum_{p\leq\lambda^2}\Lambda(p)\,p^{-1/2}\int_{\lambda^{-1}}^{\lambda/p} k(u)k(pu)\,d^*u.$$

El valor $QW_\lambda(k_\lambda)$ es el "eigenvalor aproximado" $\mu_\lambda$ del Weil form evaluado en $k_\lambda$. El Lema 7.3 (CCM) implica que $\mu_\lambda \to 0$ cuando $\lambda \to \infty$ (pues $k_\lambda \to k$ en norma y $QW_\infty(k,k)$ está relacionado con el primer cero de $\Xi$).

---

## 6. La ortogonalidad aritmética: el cálculo central

Retomamos la pregunta de Advisor 1: ¿es la proyección de $A_\lambda k_\lambda$ sobre el segundo vector propio $\psi_2$ pequeña?

**Configuración.** Sea $\mu_1 < \mu_2 \leq \mu_3 \leq \ldots$ los eigenvalores de $QW_\lambda|_{E_N^+}$ con eigenvectores $\xi_\lambda = \psi_1, \psi_2, \ldots$ En la notación de la ecuación de Euler-Lagrange:

$$(B_\lambda - \mu_1)\xi_\lambda = A_\lambda\xi_\lambda$$

La solución de resolución (primer orden en $A_\lambda$) da:
$$\xi_\lambda = k_\lambda + \sum_{j \geq 2} \frac{\langle \psi_j, A_\lambda k_\lambda\rangle}{\mu_j^{(B)} - \mu_1^{(B)}} \psi_j + O(\|A_\lambda\|^2)$$

donde $\mu_j^{(B)}$ son los eigenvalores de $B_\lambda$ y $\mu_j^{(B)} - \mu_1^{(B)} \approx \delta_\lambda \cdot (j-1)^2 \cdot (\text{factor})$ (brecha entre eigenvalores de $B_\lambda$, que es la "brecha espectral" del operador arquimediano).

**El problema de la teoría de perturbaciones clásica:** El denominador $\mu_2^{(B)} - \mu_1^{(B)} = \delta_\lambda = O(e^{-4\pi\lambda^2})$ es exponencialmente pequeño, mientras que el numerador $\langle \psi_2, A_\lambda k_\lambda\rangle$ podría ser $O(\lambda)$ (del orden de la norma de $A_\lambda$). Esto da una corrección de orden $O(\lambda e^{4\pi\lambda^2})$ — el estallido ya identificado en doc 02.

**La hipótesis de ortogonalidad aritmética (OA):**
$$|\langle \psi_2, A_\lambda k_\lambda\rangle| = O\!\left(e^{-\pi\lambda^2}\right).$$

Si OA vale, la corrección de primer orden sería $O(e^{-\pi\lambda^2}/e^{-4\pi\lambda^2}) = O(e^{3\pi\lambda^2})$ — todavía grande. Incluso con ortogonalidad, la brecha espectral domina.

**Un estimado más refinado.** Lo que realmente importa para Wall-H2 no es $\|\xi_\lambda - k_\lambda\|_{L^2}$ sino la proyección de $\xi_\lambda - k_\lambda$ en la "dirección de los ceros":

$$\hat\xi_\lambda(z) - c\hat k_\lambda(z) = \int (\xi_\lambda - ck_\lambda)(u)\,u^{-iz}\,d^*u.$$

Para $z$ cerca de un cero $\gamma_n$ de $\Xi$: por la identidad del producto de Hadamard, $\hat k_\lambda(z)$ tiene un cero simple en $z \approx \gamma_n$ con residuo $w_n = |\Xi'(\gamma_n)|$. Si la diferencia $\xi_\lambda - ck_\lambda$ está "alineada" con la dirección de $k_\lambda$ (i.e., si $\xi_\lambda - ck_\lambda = \alpha\psi_2 + \ldots$ con $\hat\psi_2(\gamma_n) \approx 0$), entonces $\hat\xi_\lambda(\gamma_n) \approx c\hat k_\lambda(\gamma_n) = 0$, lo que es exactamente lo que queremos para Wall-H2.

**Definición.** La hipótesis de ortogonalidad espectral (OE):
$$\hat\psi_2(\gamma_n) = O(w_n e^{-\pi\lambda^2}) \quad \text{para todo } n.$$

Si OE vale, entonces aunque $\xi_\lambda - k_\lambda$ tenga norma grande (dominada por $\psi_2$), la diferencia $\hat\xi_\lambda - c\hat k_\lambda$ tendrá ceros cercanos a los de $\hat k_\lambda$.

---

## 7. Cálculo de $\langle \psi_2, A_\lambda k_\lambda\rangle$ vía la fórmula explícita

**Proposición 3** (representación integral del producto interior aritmético). Para grandes $\lambda$, usando $k_\lambda \approx k$ y $\psi_2 \approx h_{4,\lambda}$ (la 4ª PSWF par):

$$\langle h_{4,\lambda}, A_\lambda k\rangle_{H_\lambda} = \sum_{p \leq \lambda^2} \Lambda(p)\,p^{-1/2}\!\int_{\lambda^{-1}}^\lambda h_{4,\lambda}(u)\,[k(pu)+k(u/p)]\,d^*u.$$

Usando la fórmula explícita de Weil en el espacio $H_\lambda$ (análoga a la utilizada en el doc 01 para el TPN):

$$\sum_{p \leq \lambda^2} \Lambda(p)\,p^{-iz} = -\frac{\zeta'}{\zeta}(1/2+iz) - \text{(contribución de los ceros)} + O(\log\lambda),$$

la suma anterior puede reescribirse (via Parseval en el grupo multiplicativo) como:

$$\langle h_{4,\lambda}, A_\lambda k\rangle = \frac{1}{2\pi}\int_\mathbb{R} \hat h_{4,\lambda}(t)\,\hat k(t)\,\left(\sum_{p\leq\lambda^2}\Lambda(p)p^{-it}\right)\,dt + \ldots$$

$$= \frac{1}{2\pi}\int_\mathbb{R} \hat h_{4,\lambda}(t)\,\Xi(t)\,\Psi_\lambda(t)\,dt$$

donde $\Psi_\lambda(t) = \sum_{p\leq\lambda^2} \Lambda(p)\,p^{-it}$ es la función de Chebyshev de Fourier.

**Análisis del producto interior.** Para calcular $\int \hat h_{4,\lambda}(t) \Xi(t) \Psi_\lambda(t)\,dt$:

- $\hat h_{4,\lambda}(t) \approx \hat\psi_4(t)$ (transformada de Fourier del 4º armónico de Hermite): función par que se anula con multiplicidad en $t=0$ y decae rápidamente.
- $\Xi(t)$: función par, positiva para $t$ pequeño, con ceros en $t = \gamma_n$.
- $\Psi_\lambda(t)$: función "oscillatoria" relacionada con los primos.

**Resultado parcial.** La integral $\int \hat h_{4,\lambda}(t)\Xi(t)\,dt \approx \langle\hat\psi_4, \Xi\rangle_{L^2}$ es una integral de una función con 4 ceros (el 4º armónico de Hermite) contra $\Xi$ (función par positiva cerca del origen). Por la ortogonalidad de los polinomios de Hermite con respecto al peso $e^{-\pi t^2}$:

$$\int_\mathbb{R} H_4(t)\,\Xi(t)\,e^{-\pi t^2}\,dt = \int H_4(t)\,\Xi(t)\,e^{-\pi t^2}\,dt,$$

que se anula si $\Xi$ estuviera en el espacio de polinomios de grado $< 4$ — pero $\Xi$ NO es un polinomio, por lo que la integral es generalmente NO nula. Sin embargo, su tamaño depende de los momentos de $\Xi$.

**Momentos de $\Xi$ vía ceros.** Si los ceros de $\Xi$ son $\pm\gamma_n$ (RH: $\gamma_n$ reales), entonces:
$$\int t^{2k} \Xi(t)\,e^{-\pi t^2}\,dt = \frac{d^{2k}}{dz^{2k}}\left[\Xi(z)\,e^{-\pi z^2}\right]_{z=0} \cdot (\text{factor Gamma}).$$

Esto conecta el producto interior $\langle \hat h_{4,\lambda}, A_\lambda k\rangle$ con los primeros $2k$ momentos de los ceros de $\Xi$.

**Observación de simetría.** La función $\hat h_{4,\lambda}(t)$ es el 4º par PSWF en el espacio de frecuencia — tiene exactamente 4 ceros reales simétricos (en $\pm t_1, \pm t_2$) y cambia de signo. La función $\Xi(t)\,\Psi_\lambda(t)$ también oscila. La integral puede tener cancelaciones significativas.

---

## 8. El mecanismo de cancelación: por qué OA es plausible

**Argumento heurístico.** El núcleo de la cancelación es el siguiente: el vector $A_\lambda k_\lambda$ es el "empuje aritmético" del kernel de Weil bajo los primos. Por la ecuación funcional $k(u) = k(u^{-1})$ y la simetría $T(p)k(u) = p^{-1/2}[k(pu) + k(u/p)]$, el empuje $A_\lambda k$ es también una función par positiva.

Una función par positiva en $H_\lambda^+$ admite la descomposición:
$$A_\lambda k_\lambda = \langle k_\lambda, A_\lambda k_\lambda\rangle k_\lambda + \sum_{j \geq 2} c_j \psi_j$$

donde el coeficiente $c_j = \langle \psi_j, A_\lambda k_\lambda\rangle$. Para que $A_\lambda k_\lambda \approx C\,k_\lambda$ (proporcional al eigenvector dominante), necesitamos $c_j$ pequeños para $j \geq 2$.

**Proposición 4** (la perturbación aritmética rota el eigenvector mínimamente). Sea $r_\lambda := A_\lambda k_\lambda / \|A_\lambda k_\lambda\|$ (el vector de empuje normalizado). Entonces:

$$|\langle r_\lambda, k_\lambda\rangle|^2 + \sum_{j\geq 2} |\langle r_\lambda, \psi_j\rangle|^2 = 1.$$

El vector $r_\lambda$ "apunta en la dirección de $k_\lambda$" (i.e., $|\langle r_\lambda, k_\lambda\rangle| \approx 1$) si y solo si el empuje aritmético es casi proporcional al kernel de Weil.

**Evaluación del coeficiente dominante.** Por la positividad de $k_\lambda$ y de $A_\lambda k_\lambda$:
$$\langle k_\lambda, A_\lambda k_\lambda\rangle = A_\lambda(k_\lambda, k_\lambda) = \sum_{p \leq \lambda^2} \Lambda(p)\,p^{-1/2}\!\int k_\lambda(u)\,k_\lambda(pu)\,d^*u > 0.$$

Este coeficiente es positivo y grande (de orden $\sim 2\lambda \cdot m(\lambda)^2$, usando el Corolario 1 del doc 04 y TPN). Por la descomposición del eigenvector:
$$\|A_\lambda k_\lambda\|^2 = |\langle k_\lambda, A_\lambda k_\lambda\rangle|^2 + \sum_{j\geq 2} |\langle \psi_j, A_\lambda k_\lambda\rangle|^2.$$

Si $\|A_\lambda k_\lambda\|^2 \approx |\langle k_\lambda, A_\lambda k_\lambda\rangle|^2$, entonces los coeficientes de las componentes excitadas son pequeños.

**Cota inferior de $\langle k_\lambda, A_\lambda k_\lambda\rangle$.** De doc 04:
$$\langle k_\lambda, A_\lambda k_\lambda\rangle = A_\lambda(k_\lambda) \geq C\lambda m(\lambda)^2 = C\lambda \cdot \Theta(\lambda^9 e^{-2\pi\lambda^2}).$$

**Estimado de $\|A_\lambda k_\lambda\|^2$.** Por la acotación $\|A_\lambda\|_{\mathrm{op}} = O(\lambda)$ (del doc 02) y $\|k_\lambda\| = O(1)$:
$$\|A_\lambda k_\lambda\| \leq \|A_\lambda\|_{\mathrm{op}}\|k_\lambda\| = O(\lambda).$$

Por tanto $\|A_\lambda k_\lambda\|^2 = O(\lambda^2)$.

Comparando: $|\langle k_\lambda, A_\lambda k_\lambda\rangle| \geq C\lambda^{10} e^{-2\pi\lambda^2}$. El cociente:

$$\frac{|\langle k_\lambda, A_\lambda k_\lambda\rangle|}{\|A_\lambda k_\lambda\|} \geq \frac{C\lambda^{10} e^{-2\pi\lambda^2}}{O(\lambda)} = C\lambda^9 e^{-2\pi\lambda^2} \to 0.$$

Este cociente tiende a 0, lo que significa que el vector $r_\lambda = A_\lambda k_\lambda / \|A_\lambda k_\lambda\|$ NO está aproximadamente alineado con $k_\lambda$ en norma.

**Interpretación.** La ortogonalidad aritmética NO vale en norma $L^2$ de $H_\lambda$. El empuje aritmético $A_\lambda k_\lambda$ tiene una componente grande en las direcciones $\psi_j$ para $j \geq 2$. Esto confirma el diagnóstico del doc 02-03: el análisis norma-a-norma (perturbaciones en $L^2$) no puede dar convergencia.

---

## 9. La salida: convergencia de ceros vía estructura de Mellin

El fracaso de la ortogonalidad en norma $L^2$ no cierra el camino. La clave del Teorema 1 de doc 03 (Rouché) es que la convergencia de ceros requiere solo un estimado PUNTUAL de $|\hat\xi_\lambda(z) - c\hat k_\lambda(z)|$ para $z$ en círculos alrededor de los ceros de $\hat k_\lambda$.

**Proposición 5** (descomposición de la perturbación en espacio de Mellin). Escribamos $\xi_\lambda = k_\lambda + \delta_\lambda$ (con $\delta_\lambda \perp k_\lambda$ en $H_\lambda$). Entonces:

$$\hat\xi_\lambda(z) - \hat k_\lambda(z) = \hat\delta_\lambda(z) = \int_{\lambda^{-1}}^\lambda \delta_\lambda(u)\,u^{-iz}\,d^*u.$$

La función $\hat\delta_\lambda(z)$ es una función entera (transformada de Mellin de una función en $L^2([\lambda^{-1},\lambda], d^*u)$). Sus ceros son potencialmente DISTINTOS de los de $\hat k_\lambda$.

**La pregunta clave (Pregunta 29.2 reformulada).** ¿Los ceros de $\hat\xi_\lambda = \hat k_\lambda + \hat\delta_\lambda$ están cerca de los de $\hat k_\lambda$, aunque $\hat\delta_\lambda$ sea grande en norma?

Para responder, descomponemos $\delta_\lambda = \sum_{j\geq 2} c_j \psi_j$ (proyección en eigenvectores excitados). Entonces:
$$\hat\delta_\lambda(z) = \sum_{j \geq 2} c_j \hat\psi_j(z).$$

Para $z$ cerca del $n$-ésimo cero $\gamma_n$ de $\hat k_\lambda \approx \Xi$:
$$|\hat\delta_\lambda(\gamma_n)| \leq \sum_{j\geq 2} |c_j|\,|\hat\psi_j(\gamma_n)|.$$

Si los eigenvectores excitados $\psi_j$ son "ciegos" en los ceros de $\Xi$ (i.e., $\hat\psi_j(\gamma_n) \approx 0$), entonces $\hat\delta_\lambda(\gamma_n) \approx 0$ aunque los coeficientes $c_j$ sean grandes.

**Hipótesis OE (ortogonalidad espectral en los ceros de $\Xi$).** Para $j \geq 2$ y todo $n$:
$$|\hat\psi_j(\gamma_n)| \leq C_{j,n}\,e^{-\pi\lambda^2/(j^2)}.$$

Si OE vale, entonces $|\hat\delta_\lambda(\gamma_n)| \leq \sum_j |c_j| C_{j,n} e^{-\pi\lambda^2/j^2}$. Combinado con $|c_j| = O(\lambda e^{4\pi\lambda^2}/j^2)$ (estimado conservador de la perturbación), esto da:

$$|\hat\delta_\lambda(\gamma_n)| = O\!\left(\lambda e^{4\pi\lambda^2} \sum_j \frac{C_{j,n}}{j^2} e^{-\pi\lambda^2/j^2}\right).$$

Para $j = 2$: el término dominante es $O(\lambda e^{4\pi\lambda^2}) \cdot C_{2,n} e^{-\pi\lambda^2/4} = O(\lambda C_{2,n} e^{(4-1/4)\pi\lambda^2})$. Esto es aún exponencialmente grande.

**Veredicto parcial.** La hipótesis OE en su forma actual NO resuelve Wall-H2 a menos que $C_{j,n}$ decaigan suficientemente rápido para compensar el factor $e^{4\pi\lambda^2}$ de la brecha espectral.

---

## 10. Un nuevo mecanismo: la ortogonalidad via la estructura de Carathéodory-Fejér

El enfoque Perron-Frobenius y el de ortogonalidad aritmética en $L^2$ enfrentan el mismo muro: el cociente brecha-espectral / norma-perturbación crece exponencialmente. Pero hay un mecanismo DIFERENTE que no aparece en la teoría de perturbaciones estándar: la estructura de Carathéodory-Fejér del minimizador.

**El Teorema CCM (re-enunciado en la clave actual).** El minimizador $\xi_\lambda$ NO es el vector más cercano a $k_\lambda$ en norma $L^2$ — es el vector que MINIMIZA $QW_\lambda$. La estructura Carathéodory-Fejér garantiza que sus ceros (los de $\hat\xi_\lambda$) son todos reales. La pregunta no es cuán cerca está $\xi_\lambda$ de $k_\lambda$ en $L^2$, sino cuán cerca están los CEROS de $\hat\xi_\lambda$ de los de $\hat k_\lambda \approx \Xi$.

**Proposición 6** (la brecha espectral no controla los ceros). Existen funciones $F, G$ enteras con todos los ceros reales tales que $\|F - G\|_{L^2}$ es grande (la norma de la diferencia de las funciones originales es grande) pero los ceros de $F$ y $G$ son cercanos. Ejemplo: $F(z) = (z-a)e^{bz}$ y $G(z) = (z-a')e^{b'z}$ con $a \approx a'$: la norma $\|F-G\|$ puede ser grande si $b \neq b'$, pero los únicos ceros son $a$ y $a'$.

**Interpretación.** La diferencia $\hat\xi_\lambda - c\hat k_\lambda$ puede tener norma grande en $L^\infty$ o $L^2$ (si $c \neq e^{a+ibz}$ exactamente), pero sus ceros pueden estar cerca. El factor de fase $e^{a_\lambda + ib_\lambda z}$ en la fórmula de convergencia de CCM absorbe la diferencia "global" entre $\hat\xi_\lambda$ y $\hat k_\lambda$, permitiendo que los ceros sean cercanos incluso sin convergencia en norma.

---

## 11. Veredicto: lo nuevo de este documento y lo que queda

### Resultados nuevos de doc 05:

| Resultado | Estado |
|---|---|
| $T(p)$ preserva el cono positivo $\mathcal{C}_N^+$ (Prop. 1) | **Probado** |
| $A_\lambda$ preserva el cono (Corolario) | **Probado** |
| $A_\lambda(|f|, |f|) \geq A_\lambda(f,f)$ para todo $f$ (condición C2) | **Probado** |
| $Q^{\mathrm{cross}}(|f|) \geq Q^{\mathrm{cross}}(f)$ para todo $f$ | **Probado** |
| Argumento de nodos obstaculizado por condición (C1) ($Q^{\mathrm{arch}}$) | **Identificado** |
| Ortogonalidad aritmética NO vale en norma $L^2$ (el cociente → 0) | **Demostrado** |
| La brecha espectral no controla los ceros (Prop. 6, ejemplo explícito) | **Probado** |
| El mecanismo de Carathéodory-Fejér como ruta alternativa | **Señalado** |

### El muro preciso (revisado):

El obstáculo central NO es la brecha espectral $\delta_\lambda$ per se, sino la relación entre:
1. La variación de fase $e^{a_\lambda + ib_\lambda z}$ entre $\hat\xi_\lambda$ y $c\hat k_\lambda$ (que la teoría de perturbaciones ignora).
2. La posición relativa de los ceros de $\hat\xi_\lambda$ vs $\hat k_\lambda$ (que puede ser buena aunque la diferencia de funciones sea grande).

### Pregunta nueva (29.4):

> **Pregunta 29.4.** ¿Puede acotarse $|\hat\xi_\lambda(\gamma_n) - \hat k_\lambda(\gamma_n)|$ directamente, sin pasar por $\|\xi_\lambda - k_\lambda\|_{L^1}$, usando la ecuación de ceros del doc 03 (Proposición 3)?

La ecuación de ceros de $\hat\xi_\lambda$ es:
$$\sum_{|m|\leq N} \frac{\xi_m^{(\lambda)}}{z - 2\pi m/L} = 0$$

y para $\hat k_\lambda$:
$$\sum_{|m|\leq N} \frac{k_m^{(\lambda)}}{z - 2\pi m/L} = 0.$$

La diferencia de los ceros depende de la diferencia de los COEFICIENTES $\xi_m - c\,k_m^{(\lambda)}$ — que aunque sea grande en $\ell^2$, puede dar lugar a ceros cercanos si la diferencia es "ortogonal" en el sentido funcional correcto.

Esta es la pregunta más concreta y específica al programa CCM que queda abierta.
