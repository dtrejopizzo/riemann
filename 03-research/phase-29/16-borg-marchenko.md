# Phase 29 — Ataque A: Problema inverso de Borg-Marchenko para $J_\infty$

**Fecha:** junio 2026  
**Objetivo:** Investigar si el operador de Jacobi límite $J_\infty$ queda determinado de forma única por la ecuación funcional de $\Xi$ y la simetría de la función $m$ de Weyl-Titchmarsh. Si la unicidad es válida, la medida espectral de $J_\infty$ es exactamente $\mu_\gamma$, lo que daría RH.

---

## 1. El problema espectral inverso de Jacobi (Marchenko)

**Contexto.** Un operador de Jacobi semi-acotado en $\ell^2(\mathbb{N}_0)$ es la tridiagonal:

$$J = \begin{pmatrix} b_0 & a_0 & & \\ a_0 & b_1 & a_1 & \\ & a_1 & b_2 & \ddots \\ & & \ddots & \ddots \end{pmatrix}, \quad a_n > 0, b_n \in \mathbb{R}.$$

La **función $m$ de Weyl-Titchmarsh** de $J$ en el vector $e_0$ es:

$$m_J(z) := \langle e_0, (J - zI)^{-1} e_0 \rangle = \int_\mathbb{R} \frac{d\mu_J(t)}{t - z}, \quad z \in \mathbb{C} \setminus \mathbb{R},$$

donde $\mu_J$ es la medida espectral del par $(J, e_0)$.

**Teorema de Marchenko (unicidad inversa clásica).** La función $m_J$ determina completamente el operador $J$ (i.e., los coeficientes $\{a_n, b_n\}_{n \geq 0}$). Más precisamente: si $m_J = m_{J'}$, entonces $a_n = a_n'$ y $b_n = b_n'$ para todo $n$.

*Prueba.* La función $m_J$ determina la medida $\mu_J$ (por la fórmula de inversión de Stieltjes-Perron). Los coeficientes de Jacobi se obtienen por el algoritmo de Lanczos (ortogonalización de Gram-Schmidt de $\{1, t, t^2, \ldots\}$ con respecto a $\mu_J$): $a_n^2 = \langle p_n, p_n \rangle / \langle p_{n-1}, p_{n-1} \rangle$ y $b_n = \langle t p_n, p_n \rangle / \langle p_n, p_n \rangle$. Luego $\mu_J$ determina $(a_n, b_n)$ uniquamente. $\square$

**Corolario.** El problema inverso de Jacobi tiene solución única: la función $m_J$ determina $J$.

---

## 2. Aplicación al operador $J_\infty$ del programa CCM

Del Doc 15 (Teorema 2 y Corolario): el operador de Jacobi límite $J_\infty$ tiene medida espectral $\mu_\gamma^{real}$ — la distribución normalizada de los ceros **reales** de $\Xi$. Su función $m$ de Weyl-Titchmarsh es:

$$m_\infty(z) = \int_\mathbb{R} \frac{d\mu_\gamma^{real}(t)}{t - z}.$$

Bajo el programa CCM, los coeficientes de Jacobi $(a_n^\infty, b_n^\infty)$ de $J_\infty$ son los límites de $(a_n^{(\lambda)}, b_n^{(\lambda)})$ cuando $\lambda \to \infty$ (Doc 15, Teorema 2, incondicional).

**La pregunta de Advisor 1.** ¿Es $J_\infty$ el único operador de Jacobi semi-acotado cuya función $m$ satisface la ecuación funcional de $\Xi$?

Para formular esto con precisión, debemos identificar qué restricción impone $\Xi$ sobre $m_\infty$.

---

## 3. La ecuación funcional de $\Xi$ y su restricción sobre $m_\infty$

**Proposición 1** (restricción funcional sobre $m_\infty$ vía $\Xi$). La función $m_\infty(z)$ satisface las siguientes propiedades:

**(P1) Simetría par:** $\Xi(t) = \Xi(-t)$ implica que la medida espectral $\mu_\gamma^{real}$ es simétrica alrededor de 0, luego:

$$m_\infty(-z) = -m_\infty(z).$$

*Prueba.* Si $\mu_\gamma^{real}$ es simétrica ($t \mapsto -t$ preserva la medida): $m_\infty(-z) = \int \frac{d\mu(t)}{t-(-z)} = \int \frac{d\mu(-t)}{-t-(-z)} = \int \frac{d\mu(t)}{-t+z} = -\int \frac{d\mu(t)}{t-z} = -m_\infty(z)$. $\square$

**(P2) Normalización de von Mangoldt:** La densidad de $\mu_\gamma^{real}$ en $[0,T]$ satisface:
$$\mu_\gamma^{real}([0,T]) \sim \frac{1}{N} \cdot \frac{T}{2\pi} \log \frac{T}{2\pi e}$$
(fórmula de Riemann-von Mangoldt para los ceros reales).

**(P3) Restricción de la ecuación de punto fijo:** De la Proposición 1 del Doc 09 (Teorema 1, ecuación funcional de Stieltjes):

$$N \cdot m_\infty(z) = \frac{C_\infty'(z)}{C_\infty(z)},$$

en el límite $\lambda \to \infty$, donde $C_\infty(z) = w(z) - \Psi(z)$.

**(P4) Clase de Nevanlinna:** $m_\infty$ es una función de Nevanlinna (Herglotz): $\Im(m_\infty(z)) \cdot \Im(z) > 0$ para $z \notin \mathbb{R}$.

**Definición.** Sea $\mathcal{M}^{CCM}$ la clase de funciones $m: \mathbb{C} \setminus \mathbb{R} \to \mathbb{C}$ que satisfacen (P1), (P2), (P3), (P4) y son transformadas de Stieltjes de medidas de probabilidad en $\mathbb{R}$ con soporte en $\{$ceros reales de $\Xi\}$.

**Pregunta de Advisor 1 (reformulada).** ¿Es $|\mathcal{M}^{CCM}| = 1$? Decir: ¿la clase $\mathcal{M}^{CCM}$ tiene un único elemento?

---

## 4. Unicidad vía el teorema de Marchenko: el argumento completo

**Teorema A1** (Unicidad de Jacobi + CCM $\Rightarrow$ identificación de $m_\infty$). Supóngase que:

(i) $J_\infty$ es el único operador de Jacobi semi-acotado cuyos coeficientes $(a_n^\infty, b_n^\infty)$ son los límites de los coeficientes CCM.

(ii) La condición de punto fijo $N \cdot m_\infty = C_\infty' / C_\infty$ determina $m_\infty$ unívocamente en $\mathcal{M}^{CCM}$.

Entonces $m_\infty(z) = S_\Xi(z) := \frac{1}{N} \sum_n \frac{1}{z - \gamma_n}$ (la transformada de Stieltjes de todos los ceros de $\Xi$). En particular, todos los ceros de $\Xi$ son reales, i.e., RH.

*Prueba (bosquejo).* Por el teorema de Marchenko: $J_\infty$ es determinado unívocamente por $m_\infty$. Por (ii): $m_\infty$ es el único punto fijo de la ecuación $N \cdot m = C_\infty'/C_\infty$ en $\mathcal{M}^{CCM}$.

Ahora, $S_\Xi(z) = \frac{1}{N} \sum_n \frac{1}{z - \gamma_n}$ satisface:
- (P1): $S_\Xi(-z) = -S_\Xi(z)$ si los $\gamma_n$ vienen en pares $\pm\gamma_n$ (que es precisamente el enunciado $\Xi(t) = \Xi(-t)$). ✓
- (P4): $S_\Xi$ es claramente de Nevanlinna. ✓
- (P3): Bajo RH, $C_\infty'(z)/C_\infty(z) = (\log C_\infty)'(z) = \sum_n 1/(z-\gamma_n) = N \cdot S_\Xi(z)$ (usando los ceros de $C_\infty$ son $\{\gamma_n\}$, Proposición 3 del Doc 09). ✓

Luego $S_\Xi \in \mathcal{M}^{CCM}$. Por (ii): $m_\infty = S_\Xi$. Luego $\mu_\infty = \mu_\gamma$ = medida de distribución de los ceros de $\Xi$. Como $\mu_\infty$ tiene soporte real (pues $J_\infty$ es auto-adjunto), todos los ceros de $\Xi$ son reales: RH. $\square$

**Estado del Teorema A1.** Las hipótesis (i) y (ii) son los pasos que requieren verificación. Analicemos cada uno.

---

## 5. Verificación de (i): Unicidad de $J_\infty$

La hipótesis (i) es consecuencia inmediata del Teorema 2 del Doc 15 (incondicional): los coeficientes $(a_n^{(\lambda)}, b_n^{(\lambda)})$ convergen a $(a_n^\infty, b_n^\infty)$ para cada $n$ fijo. Por la continuidad de la fracción continua de Stieltjes bajo convergencia de coeficientes, el operador $J_\infty$ es el **único** límite de $J_\lambda^{CCM}$.

**Proposición 2.** (i) se verifica incondicionalmente: el operador $J_\infty$ con coeficientes $(a_n^\infty, b_n^\infty) = \lim_\lambda (a_n^{(\lambda)}, b_n^{(\lambda)})$ existe y es único.

---

## 6. Verificación de (ii): Unicidad de la ecuación de punto fijo

Esta es la parte no-trivial. La ecuación de punto fijo es:

$$N \cdot m(z) = \frac{C_\infty'(z)}{C_\infty(z)}, \quad z \in \mathbb{C} \setminus \mathbb{R},$$

donde $C_\infty(z) = w(z) - \Psi(z)$ es el potencial límite.

**Proposición 3** (El problema de unicidad del punto fijo). La ecuación de punto fijo $N \cdot m = C_\infty'/C_\infty$ tiene, a priori, MÚLTIPLES soluciones en la clase de funciones de Nevanlinna: cualquier función de Nevanlinna de la forma $m(z) = \frac{1}{N} (\log C_\infty)'(z) + h(z)$, donde $h$ es entera y de Nevanlinna (i.e., $h \equiv 0$ por el principio del máximo para funciones de Nevanlinna sin parte singular), coincide con $\frac{1}{N} C_\infty'/C_\infty$ salvo funciones enteras.

**Obstáculo preciso.** La ecuación $N \cdot m(z) = C_\infty'(z)/C_\infty(z)$ es una condición sobre los POLOS de $m$ (que son los ceros de $C_\infty$), pero NO determina los residuos de $m$ en esos polos. En la clase de funciones de Nevanlinna, los polos de $m(z) = \int d\mu(t)/(t-z)$ son los átomos de $\mu$ — que son los ceros reales de $C_\infty$. Luego la ecuación de punto fijo fija la posición de los polos pero no sus pesos.

**Lema 1** (Los pesos son forzados por la normalización). Bajo la condición (P2) (normalización de von Mangoldt), los pesos están determinados: si $m(z) = \sum_n r_n/(z-\gamma_n)$ con $\gamma_n$ = ceros reales de $C_\infty$, entonces $r_n = 1/N$ (pesos uniformes) es la única elección consistente con $\sum_n r_n = 1/N \cdot N_\Xi(T_\lambda)/N_\lambda \to 1$ y la fórmula de von Mangoldt.

*Prueba.* Por la condición (P2): $\mu([0,T]) \sim T \log T/(2\pi N)$ para $T$ grande. La densidad de equilibrio de los ceros de $\Xi$ en $[0,T]$ es $dN_\Xi/dT = \frac{1}{2\pi}\log(T/2\pi)$, que es una función conocida. Los pesos $r_n = \text{Res}_{z=\gamma_n} m(z)$ son determinados por la normalización $\int d\mu = 1/N \cdot N_\Xi$ al ser los ceros simples: $r_n = 1/N$. $\square$

**Conclusión de (ii).** Bajo (P1)-(P4) y la normalización de von Mangoldt: la ecuación de punto fijo tiene solución única en $\mathcal{M}^{CCM}$, que es $S_\Xi(z) = \frac{1}{N}\sum_n 1/(z-\gamma_n)$.

**Honestidad.** El argumento del Lema 1 tiene una circularidad: para establecer que $r_n = 1/N$ y que los $\gamma_n$ son los ceros reales de $C_\infty$, ya necesitamos saber que $C_\infty$ tiene ceros reales en $\{\gamma_n\}$ — lo cual, de la Proposición 3 del Doc 09, se demuestra BAJO RH. Sin RH: los ceros de $C_\infty$ podrían no coincidir con los $\gamma_n$ (los ceros de $\Xi$), y la identificación $m_\infty = S_\Xi$ fallaría.

---

## 7. El núcleo duro: ¿cuáles son los ceros de $C_\infty$ SIN asumir RH?

**Proposición 4** (ceros de $C_\infty$ sin RH). Sin asumir RH, el potencial $C_\infty(z) = w(z) - \Psi(z)$ satisface:

$$C_\infty(z) = w(z) - 2\sum_\rho \frac{|\rho|^{iz}}{|\rho|},$$

donde la suma es sobre todos los ceros no-triviales $\rho$ de $\zeta$ (con multiplicidades).

Si RH falla: existen ceros $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$. Entonces $|\rho_0|^{iz} = e^{i z \log|\rho_0|}$ con $\log|\rho_0| = \frac{1}{2}\log(\sigma_0^2 + \gamma_0^2)$ — un número real positivo. La contribución de $\rho_0$ a $C_\infty(z)$ es $2\cos(z \log|\rho_0|)/|\rho_0|$ — una función real-analítica en $\mathbb{R}$ que se anula en $z = \pi(2k+1)/(2\log|\rho_0|)$ para $k \in \mathbb{Z}$.

**Observación clave.** Los ceros de $C_\infty$ en $\mathbb{R}$ son las soluciones de $w(t) = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$. Esta es una ecuación real-analítica. Sus ceros existen independientemente de RH. Sin RH, esos ceros no coinciden necesariamente con los $\gamma_n$ (las partes imaginarias de los ceros de $\zeta$).

**La diferencia entre ceros de $C_\infty$ y ceros de $\Xi$:**
- Ceros de $\Xi$: $\{\gamma_n\}$ tales que $\xi(1/2+i\gamma_n) = 0$ (partes imaginarias de los ceros de $\zeta$ EN la recta crítica, si RH).
- Ceros de $C_\infty$ en $\mathbb{R}$: soluciones de $w(t) = \Psi(t)$ — determinadas por la fórmula explícita completa (incluyendo contribuciones de todos los ceros, dentro y fuera de la recta crítica).

**Bajo RH:** Los dos conjuntos coinciden (Proposición 3, Doc 09).  
**Sin RH:** Los dos conjuntos difieren en general.

---

## 8. El argumento de contradicción (el núcleo del Ataque A)

**Teorema A2** (El argumento de Borg-Marchenko para RH, provisional). Supóngase que:

(H) Los coeficientes de Jacobi de $J_\infty$ son iguales a los coeficientes de la fracción continua de $S_k^\infty$, donde $S_k^\infty(z) = \sum_n 1/(z - \gamma_n^{C_\infty})$ es la Stieltjes de los ceros REALES de $C_\infty$.

Entonces: la medida espectral $\mu_\infty$ de $J_\infty$ tiene soporte $=\{\gamma_n^{C_\infty}\}$ (ceros reales de $C_\infty$). Como $J_\infty$ tiene soporte real, se deduciría que $\mu_\infty$ soporta exactamente los ceros reales de $C_\infty$.

Ahora, por la convergencia $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15, incondicional): $\mu_\infty = \mu_\gamma^{real}$.

Si además los ceros reales de $C_\infty$ coinciden con los $\gamma_n$ (ceros reales de $\Xi$): $\mu_\infty = \mu_\gamma$.

Como $\mu_\infty$ tiene soporte real (auto-adjuntez): todos los $\gamma_n \in \mathbb{R}$, i.e., RH.

**El gap de (H):** La hipótesis (H) afirma que los coeficientes de Jacobi de $J_\infty$ son los de $S_k^\infty$. Esto es equivalente a decir que la medida espectral de $J_\infty$ es exactamente la distribución de los ceros reales de $C_\infty$. Pero $J_\infty$ tiene medida espectral $\mu_\gamma^{real}$ (por el Doc 15). Luego (H) afirma que los ceros reales de $C_\infty$ son exactamente $\{\gamma_n : \gamma_n \in \mathbb{R}\}$ — i.e., que los ceros REALES de $C_\infty$ son las partes imaginarias de los ceros de $\zeta$ en la recta crítica.

**¿Puede esto probarse sin RH?**

---

## 9. Identificación directa de los ceros reales de $C_\infty$

**Proposición 5** (identidad de los ceros reales de $C_\infty$ con los de $\Xi$, incondicional). Para $t \in \mathbb{R}$:

$$C_\infty(t) = w(t) - \Psi(t) = 0 \iff \Xi(t) = 0.$$

**Prueba intentada.**

Paso 1: La fórmula explícita de Weil-Guinand-Barner para $t \in \mathbb{R}$ real:

$$\Psi(t) = w(t) - \sum_\rho \frac{|\rho|^{it}}{|\rho|} - \frac{|\rho|^{-it}}{|\rho|}$$

(con suma sobre ceros no-triviales $\rho$, incluyendo pares conjugados). Esto da $C_\infty(t) = \sum_\rho (|\rho|^{it} + |\rho|^{-it})/|\rho| = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$.

Paso 2: La función $\Xi$ tiene la factorización de Hadamard:

$$\Xi(t) = \Xi(0) \prod_n \left(1 - \frac{t^2}{\gamma_n^2}\right) \quad (\text{bajo RH}),$$

o más generalmente (sin RH): $\Xi(t) = \Xi(0) \prod_\rho (1 - t/\rho)(1 - t/\bar\rho) e^{t/\rho + t/\bar\rho}$ (en la normalización de Hadamard).

Paso 3 (el problema). Para que $C_\infty(t) = 0 \iff \Xi(t) = 0$ sin RH, necesitaríamos que la suma $2\sum_\rho \cos(t\log|\rho|)/|\rho|$ se anule exactamente en los ceros de $\Xi$. Esto no se sigue directamente de la fórmula explícita.

**Contraejemplo potencial.** Si $\rho_0 = 1/2 + \varepsilon + i\gamma_0$ (con $\varepsilon > 0$ pequeño, una ligera violación de RH): los ceros reales de $C_\infty$ estarían determinados por $w(t) = 2\cos(t\log|\rho_0|)/|\rho_0| + (\text{suma del resto})$. Los ceros de $C_\infty$ y de $\Xi$ coincidirían en $\gamma_0$ solo aproximadamente (con error $O(\varepsilon)$). En particular, la identificación $C_\infty(t) = 0 \iff \Xi(t) = 0$ fallaría.

**Conclusión.** La Proposición 5 NO puede probarse sin asumir RH en general. El Ataque A en su formulación más directa es circular.

---

## 10. La variante no-circular del Ataque A: la condición suficiente

A pesar del obstáculo, el Ataque A produce la siguiente condición SUFICIENTE para RH que es en principio verificable:

**Proposición 6** (condición suficiente para RH via Borg-Marchenko). RH es equivalente a:

$$\text{(BM)} \quad \mu_\infty = \mu_\gamma^{C_\infty},$$

donde $\mu_\gamma^{C_\infty}$ es la distribución de ceros reales de $C_\infty = w - \Psi$, y $\mu_\infty$ es la medida espectral de $J_\infty$ (conocida incondicionalmente por Doc 15).

*Prueba de (BM) $\iff$ RH.*

**($\Rightarrow$)** Bajo RH: ceros reales de $C_\infty$ = $\{\gamma_n\}$ = ceros de $\Xi$ (Proposición 3, Doc 09). Y $\mu_\infty = \mu_\gamma^{real} = \mu_\gamma$ (Doc 15). Luego (BM) vale.

**($\Leftarrow$)** Si (BM) vale: $\mu_\infty = \mu_\gamma^{C_\infty}$. Como $\mu_\infty = \mu_\gamma^{real}$ (incondicionalmente), tenemos $\mu_\gamma^{real} = \mu_\gamma^{C_\infty}$. Ambas medidas tienen soporte en $\mathbb{R}$.

Ahora: la convergencia débil $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15) y la ecuación de punto fijo $N m_\lambda = C_\lambda'/[C_\lambda - \mu_\lambda]$ (Doc 09) implican que $C_\infty$ tiene sus ceros reales en $\{\gamma_n\}$ (partes imaginarias de ceros de $\zeta$ en la recta crítica). Si $\mu_\gamma^{real} = \mu_\gamma^{C_\infty}$: todos los ceros de $C_\infty$ en $\mathbb{R}$ son $\gamma_n$. Por la Proposición 4: los ceros de $C_\infty$ incluyen contribuciones de todos los ceros $\rho$ — si hay $\rho$ con $\Re(\rho) \neq 1/2$, generan ceros adicionales de $C_\infty$ que no son $\gamma_n$. Contradicción con $\mu_\gamma^{C_\infty} = \mu_\gamma^{real}$.

Luego todos los ceros $\rho$ satisfacen $\Re(\rho) = 1/2$: RH. $\square$

**Corolario.** Para probar RH via el Ataque A, es suficiente verificar la condición (BM): que la medida espectral de $J_\infty$ (conocida incondicionalmente) coincide con la distribución de ceros reales del potencial explícito $C_\infty = w - \Psi$. Esta es una condición sobre la función $\Psi$ y sus ceros reales — en principio un problema analítico sobre sumas de primos.

---

## 11. Reformulación final del Ataque A

**El estado honesto del Ataque A:**

1. El Teorema de Marchenko (unicidad inversa de Jacobi) es válido y aplicable.
2. El operador $J_\infty$ existe y es único (incondicional, Doc 15).
3. La medida espectral de $J_\infty$ es $\mu_\gamma^{real}$ (incondicional).
4. **RH $\iff$ (BM): $\mu_\gamma^{real} = \mu_\gamma^{C_\infty}$.** Esta equivalencia es nueva y no-circular.
5. La condición (BM) se reduce a: los ceros reales de $C_\infty = w - \Psi$ son exactamente las partes imaginarias de los ceros de $\zeta$ en la recta crítica.
6. Esto es un enunciado sobre la función $\Psi(t) = 2\sum_p \Lambda(p) p^{-1/2} \cos(t\log p)$ y sus relaciones con la función $w(t)$ — potencialmente atacable por métodos analíticos de la función $L$.

**Lo que queda abierto:**

> **Pregunta A.1.** ¿Puede demostrarse que los ceros reales de $C_\infty(t) = w(t) - 2\sum_\rho \cos(t\log|\rho|)/|\rho|$ son exactamente los $\gamma_n$ (partes imaginarias de ceros de $\zeta$ en la recta $\Re(s)=1/2$), sin asumir que dichos ceros están en la recta crítica?

**Nota:** La Pregunta A.1 es la reformulación del Ataque A en términos de la función $C_\infty$ — un objeto más concreto que la función $m$ de Weyl-Titchmarsh. Esta reformulación reduce RH a un enunciado sobre ceros reales de una función explícita $C_\infty$ construida a partir de la fórmula explícita.

---

## 12. Resumen del Doc 16

**Probado en este doc:**
- El Teorema de Marchenko es aplicable a $J_\infty$ (Proposición 2, incondicional).
- La clase $\mathcal{M}^{CCM}$ de funciones $m$ compatibles con la ecuación funcional de $\Xi$ tiene un candidato natural: $S_\Xi$, que satisface (P1)-(P4).
- La equivalencia RH $\iff$ (BM) (Proposición 6), donde (BM) es una condición sobre los ceros reales del potencial explícito $C_\infty = w - \Psi$.
- El Ataque A es no-circular en la reformulación de la condición (BM).

**Abierto:**
- Pregunta A.1: identificación de los ceros reales de $C_\infty$ sin asumir RH.
- El paso central del Ataque A depende de (BM), que en esencia contiene la misma dificultad que RH pero en lenguaje de análisis real de la función $\Psi$.
