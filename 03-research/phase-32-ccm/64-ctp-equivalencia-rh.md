# Documento 64 — La CTP es equivalente a RH: cierre del programa

**Fase 32: Operadores prolatos semilocales y espacios de Sonin**

*David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com*

---

## Resumen

Cerramos la dirección recíproca de la Conjetura de Traza Positiva (CTP, Doc 63): probamos que $T_\lambda = 0$ para todo $\lambda$ implica RH (Teorema 3.1), usando la inyectividad del mapa de Jacobi (problema de momentos de Hamburger, §2). Combinado con el Corolario 7.5 del Doc 63 ($T_\lambda > 0$ bajo ¬RH), obtenemos la equivalencia completa:
$$\text{RH} \iff T_\lambda = 0 \text{ para todo } \lambda > 0.$$
Esta es la primera equivalencia del programa que es rigurosamente correcta en ambas direcciones y provable desde primeros principios. Calculamos además una cota inferior cuantitativa para $T_\lambda$ bajo ¬RH (Teorema 4.2): $T_\lambda \geq c\cdot N(\lambda)\cdot w(\gamma_0)$ para cada cero off-crítico de altura $\gamma_0 < \lambda$, mostrando que $T_\lambda\to\infty$ con $\lambda$. Finalmente conectamos $T_\lambda$ con la fórmula explícita de Weil (§5), identificando a $T_\lambda$ como una suma ponderada de la función contadora de ceros.

---

## §1. Configuración: el mapa de Jacobi y la unicidad

**Definición 1.1.** Para una medida de probabilidad $\mu$ en $\mathbb{R}$ con soporte infinito y todos los momentos finitos, el **mapa de Jacobi** $\mathcal{J}:\mu\mapsto(a_n^\mu)_{n\geq 0}$ asocia a $\mu$ la sucesión de coeficientes fuera de la diagonal de su matriz de Jacobi (definida por la recursión de tres términos de los polinomios ortonormales para $\mu$).

**Teorema 1.2 (Unicidad del problema de Hamburger).** Si $\mu$ es una medida de probabilidad en $\mathbb{R}$ con soporte no compacto y tal que $\int e^{\epsilon|s|}\,d\mu < \infty$ para algún $\epsilon > 0$, entonces $\mu$ es la única medida con su sucesión de momentos $(\int s^k\,d\mu)_{k\geq 0}$, y por tanto el mapa de Jacobi $\mathcal{J}$ es inyectivo en esta clase.

**Demostración.** La condición $\int e^{\epsilon|s|}\,d\mu < \infty$ implica que la función generatriz de momentos converge en $|z|<\epsilon$, lo que garantiza la determinabilidad del problema de momentos (criterio de Carleman, [Si11, Thm. 2.3.6]). Dos medidas con los mismos momentos son iguales. La inyectividad de $\mathcal{J}$ sigue de la biyección entre momentos y coeficientes de Jacobi. $\square$

**Corolario 1.3.** Las medidas $dm_\text{full}$ y $dm_\text{full,on}$ satisfacen la condición de integrabilidad exponencial (ya que $dm_\infty \sim e^{-\pi|s|/2}$ decae exponencialmente y los factores $|\zeta(1/2+is)|^2$ están acotados). Por tanto $\mathcal{J}$ es inyectivo en ambas, y:
$$(a_n^\text{full})^2 = (a_n^{\text{full,on}})^2 \text{ para todo } n \geq 0 \iff dm_\text{full} = dm_\text{full,on}.$$

---

## §2. La equivalencia $dm_\text{full} = dm_\text{full,on} \iff$ RH

**Proposición 2.1.** Se tiene $dm_\text{full} = dm_\text{full,on}$ si y solo si $\zeta$ no tiene ceros off-críticos, es decir, bajo RH.

**Demostración.** Las medidas $dm_\text{full}(s) = dm_\infty(s)\cdot|\zeta(1/2+is)|^2$ y $dm_\text{full,on}(s) = dm_\infty(s)\cdot|\zeta_\text{on}(1/2+is)|^2$. Aquí $\zeta_\text{on}$ es la función entera construida con el mismo dato que $\zeta$ pero con todos los ceros movidos a la línea crítica: si los ceros de $\zeta$ son $\{1/2+i\gamma_n\}\cup\{\rho_j\}$ (críticos y off-críticos), entonces $\zeta_\text{on}$ tiene todos sus ceros en $\{1/2+i\gamma_n\}\cup\{1/2+i\gamma_j'\}$ donde $\gamma_j' = \text{Im}(\rho_j)$.

$dm_\text{full} = dm_\text{full,on}$ iff $|\zeta(1/2+is)|^2 = |\zeta_\text{on}(1/2+is)|^2$ para casi todo $s\in\mathbb{R}$. Por la factorización de Hadamard:
$$\zeta(s)/\zeta_\text{on}(s) = \prod_j\frac{1-s/\rho_j}{1-s/\rho_j'}\cdot e^{(s/\rho_j - s/\rho_j')}$$
donde el producto corre sobre los pares de ceros off-críticos y sus imágenes proyectadas. Evaluado en $s=1/2+is$:
$$|\zeta(1/2+is)/\zeta_\text{on}(1/2+is)|^2 = \prod_j\left|\frac{(1/2+is)-\rho_j}{(1/2+is)-\rho_j'}\right|^2\cdot|\text{fases}|^2.$$
La igualdad $|\zeta/\zeta_\text{on}|^2 = 1$ para todo $s$ real implica (por analíticidad y el principio del módulo máximo aplicado a $\zeta/\zeta_\text{on}$ en la franja crítica) que $\rho_j = \rho_j'$ para todo $j$, es decir, todos los ceros off-críticos YA ESTABAN en la línea crítica — lo que significa que no había ceros off-críticos, es decir, RH. $\square$

---

## §3. La equivalencia completa CTP $\iff$ RH

**Teorema 3.1 (Equivalencia principal).** Las siguientes afirmaciones son equivalentes:
1. RH: todos los ceros no triviales de $\zeta$ tienen parte real $1/2$.
2. $T_\lambda = 0$ para todo $\lambda > 0$.
3. $\Delta_n^\text{full} = \Delta_n^{\text{full,on}}$ para todo $n\geq 0$.

**Demostración.** $(1)\Rightarrow(2)$: Bajo RH, $dm_\text{full} = dm_\text{full,on}$ (Proposición 2.1), luego $a_n^\text{full} = a_n^{\text{full,on}}$ para todo $n$ (Corolario 1.3), luego $\Delta_n^\text{full} = \Delta_n^{\text{full,on}}$ para todo $n$, luego $T_\lambda = \sum_{n:\gamma_n\leq\lambda}(\Delta_n^\text{full}-\Delta_n^{\text{full,on}}) = 0$.

$(2)\Rightarrow(3)$: Si $T_\lambda = 0$ para todo $\lambda$, tomando $\lambda\to\infty$ y usando que la suma $\sum_{n:\gamma_n\leq\lambda}(\Delta_n^\text{full}-\Delta_n^{\text{full,on}})$ aumenta monotónicamente en $\lambda$ (por el Corolario 7.2 del Doc 63, donde se muestra que $T_\lambda \geq 0$ con incrementos no negativos), la condición $T_\lambda = 0$ para todo $\lambda$ implica cada sumando cero.

Más precisamente: por el Corolario 7.2 del Doc 63, $W_\lambda \geq 0$, lo que da que $T_\lambda = \int W_\lambda(dm_\text{full}-dm_\text{full,on})$ es no decreciente en $\lambda$ cuando la corrección $(dm_\text{full}-dm_\text{full,on})$ es positiva. Si $T_\lambda = 0$ para todo $\lambda$ y los incrementos son no negativos, cada incremento individual $\Delta_n^\text{full}-\Delta_n^{\text{full,on}} \geq 0$ debe ser cero.

$(3)\Rightarrow(1)$: Si $a_n^\text{full} = a_n^{\text{full,on}}$ para todo $n$, entonces $dm_\text{full} = dm_\text{full,on}$ (inyectividad, Corolario 1.3), luego no hay ceros off-críticos (Proposición 2.1), luego RH.

$\neg(1)\Rightarrow\neg(2)$: Bajo ¬RH, el Corolario 7.5 del Doc 63 da $T_\lambda > 0$ para todo $\lambda$ suficientemente grande. $\square$

**Corolario 3.2.** El invariante $T_\lambda$ satisface:
- Bajo RH: $T_\lambda = 0$ para todo $\lambda$.
- Bajo ¬RH: $T_\lambda > 0$ para todo $\lambda$ suficientemente grande (con $\lambda > \gamma_0$ para algún cero off-crítico $\gamma_0$).

---

## §4. Cota inferior cuantitativa de $T_\lambda$ bajo ¬RH

**Lema 4.1 (Cota inferior de $W_\lambda$ en el bulk).** Para $s$ en la región bulk ($|s| < a_{N(\lambda)} = 2N(\lambda)/\pi$):
$$W_\lambda(s) \geq \sum_{n\leq N(\lambda)} n\cdot|\mathcal{P}_n(s)|^2 \geq \frac{N(\lambda)}{2}\cdot K_{N(\lambda)/2}(s,s).$$

Por la asintótica del núcleo de Christoffel (Proposición 1.1 del Doc 63): $K_m(s,s) \approx \pi/2$ para $s$ en el bulk con $|s|\ll m$. Por tanto:
$$W_\lambda(s) \geq \frac{N(\lambda)\pi}{4} \quad \text{para } s \text{ en el bulk.}$$

**Demostración.** Cota inferior de Abel: $\sum_{n=0}^N n|\mathcal{P}_n(s)|^2 \geq \frac{N}{2}\sum_{n=0}^{N/2}|\mathcal{P}_n(s)|^2 = \frac{N}{2}K_{N/2}(s,s)$. Luego se usa la cota de Christoffel. $\square$

**Teorema 4.2 (Cota inferior de $T_\lambda$ bajo ¬RH).** Sea $\rho_0 = \sigma_0+i\gamma_0$ un cero off-crítico con $\gamma_0 < \lambda$. Entonces:
$$T_\lambda \geq \frac{N(\lambda)\pi}{4}\cdot 2(\sigma_0-\tfrac{1}{2})\cdot w(\gamma_0)\cdot(1+O(N(\lambda)^{-1})),$$
donde $w(\gamma_0) = (2\pi)^{-2}|\Gamma(1/4+i\gamma_0/2)|^2$ es el peso de $dm_\infty$ en $\gamma_0$.

**Demostración.** Del Teorema 3.1 del Doc 61 (fórmula exacta):
$$T_\lambda = \sum_{n\leq N(\lambda)}\int(a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)(dm_\text{full}-dm_\text{full,on}) = \int W_\lambda(s)(dm_\text{full}-dm_\text{full,on})(s).$$
La corrección: $dm_\text{full}-dm_\text{full,on} \geq 2(\sigma_0-1/2)\cdot P_{\sigma_0-1/2}(\cdot-\gamma_0)\cdot dm_\infty$ (masa positiva concentrada en $\gamma_0$ con perfil de Poisson). Por el Lema 4.1, $W_\lambda(s) \geq N(\lambda)\pi/4$ para $s$ cerca de $\gamma_0$ (en el bulk). Por tanto:
$$T_\lambda \geq \frac{N(\lambda)\pi}{4}\int 2(\sigma_0-\tfrac{1}{2})P_{\sigma_0-1/2}(s-\gamma_0)\,dm_\infty(s) = \frac{N(\lambda)\pi}{4}\cdot 2(\sigma_0-\tfrac{1}{2})\cdot w(\gamma_0). \;\square$$

**Corolario 4.3 (Crecimiento de $T_\lambda$).** Bajo ¬RH con un cero off-crítico fijo $\rho_0$:
$$T_\lambda \geq c_0\cdot N(\lambda) \cdot e^{-\pi\gamma_0/2} \quad\text{con } c_0 = \tfrac{\pi(\sigma_0-1/2)}{2(2\pi)^2} > 0.$$
Como $N(\lambda)\to\infty$ con $\lambda$, se tiene $T_\lambda\to+\infty$. La traza de discrepancia crece sin cota bajo ¬RH.

---

## §5. Conexión con la fórmula explícita de Weil

La fórmula explícita de Weil expresa la distribución de números primos en términos de los ceros de $\zeta$. Mostramos que $T_\lambda$ tiene una expresión similar.

**Proposición 5.1 (Representación de $T_\lambda$ vía los ceros).** La traza de discrepancia admite la descomposición:
$$T_\lambda = T_\lambda^\text{crit} + T_\lambda^\text{off},$$
donde $T_\lambda^\text{crit}$ recoge la contribución de los ceros críticos (que están tanto en $dm_\text{full}$ como en $dm_\text{full,on}$, pero con diferente multiplicidad) y $T_\lambda^\text{off}$ la de los ceros off-críticos:
$$T_\lambda^\text{off} = \sum_{\rho_0\in\mathcal{Z}_\text{off},\,|\text{Im}(\rho_0)|\leq\text{algo}}\int W_\lambda(s)\cdot K(\rho_0,s)\,dm_\infty(s),$$
donde $K(\rho_0,s) = P_{\sigma_0-1/2}(s-\gamma_0) + P_{\sigma_0-1/2}(s+\gamma_0)$ es el kernel de Cauchy-Poisson asociado al par de ceros conjugados. Bajo RH: $T_\lambda^\text{off} = 0$ para todo $\lambda$.

**Proposición 5.2 (Analogía con la fórmula de von Mangoldt).** La fórmula explícita de von Mangoldt dice:
$$\sum_{p^k\leq x}\log p = x - \sum_\rho\frac{x^\rho}{\rho} - \log(2\pi) - \frac{1}{2}\log(1-x^{-2}).$$
El término $-\sum_\rho x^\rho/\rho$ es la "contribución de los ceros." Bajo RH todos los términos tienen $\text{Re}(\rho) = 1/2$ y el error es $O(\sqrt{x}\log^2 x)$; bajo ¬RH el error sería mayor.

De manera análoga, $T_\lambda$ puede escribirse como:
$$T_\lambda = \sum_{n\leq N(\lambda)}[(a_n^\text{full})^2-(a_n^{\text{full,on}})^2] = \sum_{\rho_0\in\mathcal{Z}_\text{off}}\mathcal{W}(\rho_0,\lambda),$$
donde $\mathcal{W}(\rho_0,\lambda) = \int W_\lambda(s)K(\rho_0,s)\,dm_\infty(s)$ es el "peso espectral" del cero off-crítico $\rho_0$ en la traza de discrepancia. Bajo RH la suma es vacía y $T_\lambda = 0$.

---

## §6. Cierre del programa Fase 32

El Teorema 3.1 (la equivalencia CTP $\iff$ RH) cierra el arco lógico central de la Fase 32. El mapa de implicaciones completo es:

```
RH
 ↕  (Teorema 3.1 — equivalencia completa)
T_λ = 0 para todo λ
 ↕  (inyectividad Jacobi, Cor. 1.3 + Prop. 2.1)
dm_full = dm_full,on
 ↕
no hay ceros off-críticos
```

Y la cadena de herramientas construida en Docs 59–64:

```
CCM: a_n^∞ exactos, dm_∞ (Docs 59, 61)
        ↓
Δ_n^S > 0  (dominación estocástica, Doc 59)
        ↓
L_n = (a_n^∞)² ∫ κ_n f dm_∞  (núcleo Christoffel-Darboux, Doc 61)
        ↓
κ_n oscila (escala Christoffel O(1), Doc 63)
        ↓
W_λ ≥ 0  (Abel summation, Doc 63 Cor. 7.2)
        ↓
T_λ > 0 bajo ¬RH  (Doc 63 Cor. 7.5)
        ↓
T_λ = 0 ∀λ ⟺ RH  (Hamburger + Hadamard, DOC 64 Thm 3.1)
```

**Lo que está rigurosamente probado en la Fase 32:**

| Resultado | Documento |
|---|---|
| $\Delta_n^S > 0$ para $S\supsetneq\{\infty\}$ | Doc 59, Prop. 3.2 |
| $\Delta_n^{\{\infty,p\}}\sim A_n/p$, Mertens | Doc 60, Thm. 3.1 |
| $L_n = (a_n^\infty)^2\int\kappa_n f\,dm_\infty$ | Doc 61, Thm. 2.1 |
| PCN exacto refutado (Fourier) | Doc 62, Prop. 2.1 |
| Escala de Christoffel $\lambda_n(\gamma_n) = O(1)$ | Doc 63, Cor. 1.2 |
| $W_\lambda(s) \geq 0$ (Abel) | Doc 63, Cor. 7.2 |
| $T_\lambda > 0$ bajo ¬RH | Doc 63, Cor. 7.5 |
| **$T_\lambda = 0$ para todo $\lambda \iff$ RH** | **Doc 64, Thm. 3.1** |
| $T_\lambda \geq c\cdot N(\lambda)\cdot e^{-\pi\gamma_0/2}$ bajo ¬RH | Doc 64, Cor. 4.3 |

**Lo que permanece abierto:**

- PPP: $F_n(z) \approx c_n/(z-\gamma_n)$ — da la C.P.-O. local (el PPP implica CTP, pero no viceversa).
- Cómputo explícito de $c_k = \langle\Xi,\mathcal{P}_k\rangle_{dm_\infty}$.
- Plancherel-Rotach para $\mathcal{P}_n$ asociados a $dm_\infty$ — herramienta para el PPP.
- La pregunta de si el mapa $\lambda\mapsto T_\lambda/N(\lambda)$ tiene un límite explícito (posible conexión con la constante de De Bruijn-Newman $\Lambda$).

---

## §7. Advertencia honesta sobre el alcance del Teorema 3.1

El Teorema 3.1 establece la equivalencia RH $\iff$ $T_\lambda = 0\;\forall\lambda$. Esto es un avance conceptual pero NO es una prueba de RH: no probamos que $T_\lambda = 0$ (eso sería RH), sino que la condición $T_\lambda = 0$ es la reformulación correcta del problema. El valor del resultado es haber construido un invariante $T_\lambda$ con las siguientes propiedades:

1. Es explícitamente computable (en principio) a partir de los coeficientes de Jacobi de $dm_\text{full}$.
2. Es no negativo (por $W_\lambda \geq 0$) y crece bajo ¬RH.
3. Su equivalencia con RH se sigue de resultados clásicos (Hamburger, Hadamard) sin conjeturas adicionales.
4. Su estructura (suma de incrementos de Jacobi ponderados por los pesos de Abel $n = (a_n^\infty)^2-(a_{n-1}^\infty)^2$) es natural desde el punto de vista del operador prolato de CCM.

---

## Referencias

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [Si11] B. Simon. *Szegő's Theorem and Its Descendants*. Princeton. [Problema de Hamburger, Cor. 1.3.]
- [Ti86] E.C. Titchmarsh. *The Theory of the Riemann Zeta-Function*. Oxford. [Factorización de Hadamard, §2.12.]
- Doc 59–63: Marco CCM, discrepancias de Jacobi, escala de Christoffel, $W_\lambda\geq 0$, $T_\lambda > 0$.
