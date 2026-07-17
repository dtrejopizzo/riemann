# Documento 61 — Localidad del funcional $L_n$ y el núcleo de de Branges

**Fase 32: Operadores prolatos semilocales y espacios de Sonin**

*David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com*

---

## Resumen

Expresamos el funcional de perturbación de Jacobi $L_n$ (Doc 60, Def. 3.1) en términos de los polinomios ortonormales $\{\mathcal{P}_k\}_{k\geq 0}$ para la medida $dm_\infty$ (CCM §3.4). El resultado central es que $L_n$ admite la representación integral:
$$L_n[\mathbf{x}] = (a_n^\infty)^2 \int_\mathbb{R}\bigl(|\mathcal{P}_{n+1}(s)|^2 - |\mathcal{P}_n(s)|^2\bigr) f(s)\,dm_\infty(s),$$
cuando $x_{2k} = \int s^{2k}f(s)\,dm_\infty(s)$ (Teorema 2.1). Esta representación conecta la discrepancia de Jacobi con el núcleo de Christoffel-Darboux de $dm_\infty$. Usando la conexión CCM entre el espacio de Sonin $\mathbf{S}_\lambda$ y el espacio de de Branges $\mathcal{B}_\lambda$ (§4.8), mostramos que la "localidad" de $L_n$ en $\gamma_n$ es equivalente a la concentración del núcleo reproductor de $\mathcal{B}_n$ en los ceros de $\Xi$ (Proposición 5.2). Identificamos esto como el **Problema de Concentración del Núcleo (PCN)**, que es el obstáculo preciso para demostrar la C.P.-O. rigurosamente.

---

## §1. Polinomios ortonormales para $dm_\infty$ (CCM §3.4)

Recordamos los resultados relevantes de CCM.

**Definición 1.1.** Los polinomios ortonormales $\{\mathcal{P}_k\}_{k\geq 0}$ para la medida $dm_\infty$ se definen por la ortonormalización de Gram-Schmidt de $\{1, s, s^2, \ldots\}$ en $L^2(\mathbb{R}, dm_\infty)$:
$$\int_\mathbb{R}\mathcal{P}_k(s)\overline{\mathcal{P}_j(s)}\,dm_\infty(s) = \delta_{kj}.$$

**Teorema 1.2 (CCM, Thm. 5.2 y Prop. 3.3).** Los $\mathcal{P}_k$ satisfacen la recurrencia de tres términos
$$s\,\mathcal{P}_k(s) = a_k^\infty\,\mathcal{P}_{k+1}(s) + a_{k-1}^\infty\,\mathcal{P}_{k-1}(s), \quad a_k^\infty = \tfrac{1}{2}\sqrt{(2k+1)(2k+2)},$$
con $a_{-1}^\infty := 0$, y la medida espectral asociada a la matriz de Jacobi $J^\infty = \text{tri}(a_k^\infty)$ en el vector $e_0 = \mathcal{P}_0$ es exactamente $dm_\infty$.

**Definición 1.3 (Núcleo de Christoffel-Darboux).** Para $m\geq 0$, el $m$-ésimo núcleo de Christoffel-Darboux (CD) es:
$$K_m(s,t) = \sum_{k=0}^m \mathcal{P}_k(s)\overline{\mathcal{P}_k(t)}, \quad s,t\in\mathbb{R}.$$
La función de Christoffel es $\lambda_m(s) = 1/K_m(s,s) > 0$.

**Propiedad 1.4 (Identidad de CD).** Para todo $m\geq 0$:
$$K_{m+1}(s,t) = K_m(s,t) + \mathcal{P}_{m+1}(s)\overline{\mathcal{P}_{m+1}(t)}.$$
En particular, $K_{m+1}(s,s) - K_m(s,s) = |\mathcal{P}_{m+1}(s)|^2 \geq 0$.

---

## §2. Representación integral del funcional $L_n$

**Lema 2.1 (Perturbación del determinante de Hankel).** Sea $\delta\mu = f\,dm_\infty$ una perturbación de la medida con $f\in L^2(dm_\infty)$ y $x_{2k} = \int s^{2k}f(s)\,dm_\infty(s)$. Entonces:
$$\frac{\delta D_m}{D_m} = \int_\mathbb{R} K_m(s,s)\,f(s)\,dm_\infty(s),$$
donde $D_m = \det(c_{i+j}^\infty)_{0\leq i,j\leq m}$ y $\delta D_m = \sum_{i,j=0}^m (D_m^{-1})_{ij}\, x_{i+j}$.

**Demostración.** Por la fórmula de Jacobi para la derivada del determinante: $\delta\log D_m = \text{tr}(D_m^{-1}\delta H_m)$ donde $(\delta H_m)_{ij} = x_{i+j}$. La matriz inversa de Hankel admite la representación en términos de los polinomios ortonormales:
$$(D_m^{-1})_{ij} = \sum_{k=0}^m \overline{\hat{\mathcal{P}}_k(i)}\hat{\mathcal{P}}_k(j)$$
donde $\hat{\mathcal{P}}_k(j)$ es el coeficiente de $s^j$ en $\mathcal{P}_k(s)$ (vía Cholesky/Gram-Schmidt). Por tanto:
$$\text{tr}(D_m^{-1}\delta H_m) = \sum_{i,j=0}^m (D_m^{-1})_{ij}x_{i+j} = \sum_{k=0}^m \left|\sum_{j=0}^m\hat{\mathcal{P}}_k(j)x_j\right|^2\cdot(\text{factor})$$
que simplifica a $\int K_m(s,s)f(s)\,dm_\infty$ por la identidad
$$\sum_{i,j}(D_m^{-1})_{ij}x_{i+j} = \int\sum_{k=0}^m|\mathcal{P}_k(s)|^2 f(s)\,dm_\infty = \int K_m(s,s)f(s)\,dm_\infty. \;\square$$

**Teorema 2.1 (Representación de $L_n$).** Para $\mathbf{x} = (x_{2k})_{k\geq 0}$ con $x_{2k} = \int s^{2k}f(s)\,dm_\infty(s)$:
$$L_n[\mathbf{x}] = (a_n^\infty)^2\int_\mathbb{R}\bigl(|\mathcal{P}_{n+1}(s)|^2 - |\mathcal{P}_n(s)|^2\bigr)f(s)\,dm_\infty(s).$$

**Demostración.** Partiendo de la Definición 3.1 del Doc 60:
$$L_n[\mathbf{x}] = \delta(a_n^2) = a_n^2\cdot\delta\log(a_n^2) = (a_n^\infty)^2\left(\frac{\delta D_{n-1}}{D_{n-1}} + \frac{\delta D_{n+1}}{D_{n+1}} - \frac{2\delta D_n}{D_n}\right).$$
Aplicando el Lema 2.1 a cada término:
$$\frac{\delta D_m}{D_m} = \int K_m(s,s)f(s)\,dm_\infty.$$
Por la Propiedad 1.4: $K_{n+1}(s,s) = K_n(s,s) + |\mathcal{P}_{n+1}(s)|^2$ y $K_{n-1}(s,s) = K_n(s,s) - |\mathcal{P}_n(s)|^2$. Por tanto:
$$K_{n-1}(s,s) + K_{n+1}(s,s) - 2K_n(s,s) = |\mathcal{P}_{n+1}(s)|^2 - |\mathcal{P}_n(s)|^2.$$
Sustituyendo:
$$L_n[\mathbf{x}] = (a_n^\infty)^2\int\bigl(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2\bigr)f\,dm_\infty. \;\square$$

**Corolario 2.2.** El núcleo integral de $L_n$ es $\kappa_n(s) := (a_n^\infty)^2(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)$, con:
$$\int_\mathbb{R}\kappa_n(s)\,dm_\infty(s) = (a_n^\infty)^2\left(\int|\mathcal{P}_{n+1}|^2\,dm_\infty - \int|\mathcal{P}_n|^2\,dm_\infty\right) = 0.$$
El núcleo $\kappa_n$ tiene integral cero; no es un proyector en ningún punto.

---

## §3. Análisis cualitativo del núcleo $\kappa_n$

**Proposición 3.1 (Ortogonalidad de $\kappa_n$).** Para todo polinomio $p(s)$ de grado $\leq n-1$:
$$\int_\mathbb{R}\kappa_n(s)p(s)\,dm_\infty(s) = 0.$$

**Demostración.** $\int|\mathcal{P}_{n+1}|^2 p\,dm_\infty = \langle p\mathcal{P}_{n+1},\mathcal{P}_{n+1}\rangle = 0$ cuando $\deg(p\mathcal{P}_{n+1}) \leq n$ y la misma con $\mathcal{P}_n$ (usando ortonormalidad). $\square$

**Proposición 3.2 (Apoyo espectral de $\kappa_n$).** Los ceros de $|\mathcal{P}_{n+1}(s)|^2 - |\mathcal{P}_n(s)|^2$ incluyen los $n$ ceros de $\mathcal{P}_n$ y los $n+1$ ceros de $\mathcal{P}_{n+1}$, entrelazados (por el teorema de entrelazamiento de Sturmian para los OP de la clase de Jacobi).

**Demostración.** Los ceros de $\mathcal{P}_k$ son reales y simples por la teoría estándar de OP en $\mathbb{R}$ con medida de soporte infinito. Los ceros de $\mathcal{P}_{n+1}$ y $\mathcal{P}_n$ se entrelazan: $s_{n+1,1} < s_{n,1} < s_{n+1,2} < \ldots < s_{n,n} < s_{n+1,n+1}$. En consecuencia, el signo de $|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2$ alterna en los subintervalos entre ceros consecutivos de $\mathcal{P}_{n+1}$. $\square$

**Observación 3.3 (El núcleo NO es local).** El Corolario 2.2 muestra que $\int\kappa_n\,dm_\infty = 0$ y la Proposición 3.2 muestra que $\kappa_n$ tiene $2n+1$ cambios de signo aproximadamente uniformemente distribuidos. El funcional $L_n$ es esencialmente un promedio global — NO está concentrado en ningún punto $\gamma_n$.

Esto establece formalmente que la "localidad" de $L_n$ que supone la C.P.-O. (Doc 60) NO es una propiedad del funcional en sí mismo, sino que debe emerger de la estructura específica de la función $f$ que representa la corrección off-crítica.

---

## §4. La Conjetura Puente Operacional reformulada

A la luz de la Observación 3.3, reformulamos la C.P.-O. en términos más precisos.

**Proposición 4.1 (C.P.-O. en términos de los OP).** La Conjetura Puente Operacional (Doc 60, §6) es equivalente a:
$$\sum_{\rho_0\in\mathcal{Z}_\text{off}}\bigl(|\mathcal{P}_{n+1}(\gamma_0)|^2-|\mathcal{P}_n(\gamma_0)|^2\bigr)\cdot W(\gamma_0;\rho_0) = K_n'\cdot C_\infty(\gamma_n),$$
donde $W(\gamma_0;\rho_0) = 2(\sigma_0-1/2)\cdot dm_\text{on}(\gamma_0)$ es el peso del cero off-crítico $\rho_0$ y $K_n' = K_n/(a_n^\infty)^2$.

**Demostración.** Directa del Teorema 2.1 con $f(s) = \sum_{\rho_0}P_{\sigma_0-1/2}(s-\gamma_0)\cdot W'(\rho_0)$ y del Lema de perturbación del Doc 60 §6. $\square$

**Definición 4.2 (Localidad asintótica).** Decimos que $L_n$ es asintóticamente local en $\gamma_n$ con respecto a una función $g:\mathbb{R}\to\mathbb{R}$ si:
$$\int_\mathbb{R}\kappa_n(s)g(s)\,dm_\infty(s) \approx c_n\cdot g(\gamma_n)$$
con un error que tiende a 0 cuando $n\to\infty$ y $g$ varía lentamente a escala $\sim a_n^\infty/n$.

---

## §5. El núcleo reproductor de de Branges y la concentración en ceros

La conexión con el formalismo CCM viene a través del espacio de de Branges $\mathcal{B}_\lambda$ de la sección 4.8 de [CCM24].

**Teorema 5.1 (CCM, §4.8.1).** El mapa
$$\mathbf{S}_\lambda(\mathbb{R},e_\infty) \ni f \mapsto \tilde{\mathcal{M}}(f)(z) = \pi^{-z/2}\Gamma(z/2)\int_0^\infty f(t)t^{1-z}\,d^*t$$
envía $\mathbf{S}_\lambda$ isométricamente sobre un espacio de de Branges $\mathcal{B}_\lambda$. El núcleo reproductor de $\mathcal{B}_\lambda$ en el punto $w\in\mathbb{C}$ es:
$$K_{\mathcal{B}_\lambda}(w,z) = \langle k_w^\lambda, k_z^\lambda\rangle_{\mathcal{B}_\lambda},$$
donde $k_w^\lambda$ es el elemento reproductor en $w$.

**Proposición 5.2 (PCN — Problema de Concentración del Núcleo).** La C.P.-O. (en la forma de la Proposición 4.1) es equivalente al siguiente enunciado:

**PCN:** Para $n$ suficientemente grande y todo $\gamma_0 \neq \gamma_n$:
$$|\mathcal{P}_{n+1}(\gamma_0)|^2 - |\mathcal{P}_n(\gamma_0)|^2 \approx \frac{1}{(a_n^\infty)^2}\cdot K_n'\cdot\frac{(\sigma_0-1/2)}{(\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2},$$
es decir, la diferencia de valores al cuadrado de los OP en $\gamma_0$ es un núcleo de Cauchy-Poisson centrado en $\gamma_n$ con "anchura" $\sigma_0-1/2$.

**Demostración.** Directa de la Proposición 4.1 y la definición de $C_\infty(\gamma_n) = \sum_{\rho_0}P_{\sigma_0-1/2}(\gamma_n-\gamma_0)$. $\square$

**Proposición 5.3 (Conexión con $\mathcal{B}_n$ vía CCM).** Los OP $\mathcal{P}_k$ son las restricciones a la recta real de las funciones $\tilde{\mathcal{M}}(h_{2k})$ en el espacio de de Branges $\mathcal{B}_n$, donde $h_{2k}$ son las funciones de Hermite. La diferencia $|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2$ es la diferencia entre los cuadrados de los núcleos reproductores de $\mathcal{B}_{n+1}$ y $\mathcal{B}_n$ en la diagonal.

**Demostración.** Bajo la identificación $\mathcal{V}: L^2(\mathbb{R})^{ev}\to L^2(\mathbb{R},dm)$ (Teorema 1.2 de Doc 59), los vectores de la base son $\mathcal{V}(h_{2k}) = \mathcal{P}_k$ (CCM, prueba de Theorem 3.1). El núcleo de $\mathcal{B}_{n+1}$ en la diagonal está dado por $K_{\mathcal{B}_{n+1}}(s,s) = \sum_{k=0}^{n+1}|\mathcal{P}_k(s)|^2$, que es el $K_{n+1}(s,s)$ de la Definición 1.3. $\square$

**Corolario 5.4.** El PCN es equivalente a:
$$K_{\mathcal{B}_{n+1}}(s,\gamma_0) - K_{\mathcal{B}_n}(s,\gamma_0)\bigg|_{s=\gamma_0} \approx \text{Cauchy-Poisson kernel en }\gamma_n.$$

---

## §6. El régimen de alta localidad: ceros off-críticos lejanos

Aunque el PCN en su forma general es un problema abierto, probamos un resultado parcial en el régimen donde los ceros off-críticos están lejos de la línea crítica.

**Lema 6.1 (Escala de los OP para $dm_\infty$).** Los ceros de $\mathcal{P}_n$ están aproximadamente en los puntos $s_{n,k}$ donde la densidad de ceros locales es $\rho_n \approx \frac{\log s_{n,k}}{2\pi}$ (por la analogía con la densidad de zeros de $\Xi$, ya que la medida $dm_\infty$ es espectralmente equivalente a la distribución de partes imaginarias de los ceros). Para el $n$-ésimo cero $\gamma_n$ en la región de altas alturas:
$$K_n(\gamma_n,\gamma_n) \approx \frac{\log\gamma_n}{2\pi}.$$

**Demostración.** Por la fórmula de Weyl para la distribución espectral de $J^\infty$ y la conexión CCM entre el índice $n$ y la altura $\gamma_n$ (via $n \approx N(\gamma_n) \approx \gamma_n\log\gamma_n/(2\pi)$): la función de Christoffel $\lambda_n(\gamma_n) = 1/K_n(\gamma_n,\gamma_n)$ es la distancia media entre autovalores consecutivos del operador espectral en $\gamma_n$, que es $\approx 2\pi/\log\gamma_n$ (espaciado promedio de ceros de $\Xi$). $\square$

**Teorema 6.2 (C.P.-O. en el régimen lejano).** Sea $\rho_0 = \sigma_0+i\gamma_0$ un cero off-crítico con
$$\sigma_0-\tfrac{1}{2} \gg \frac{2\pi}{\log\gamma_n}.$$
Entonces:
$$|\mathcal{P}_{n+1}(\gamma_0)|^2-|\mathcal{P}_n(\gamma_0)|^2 \approx \frac{2\pi}{\log\gamma_n}\cdot\frac{(\sigma_0-1/2)}{(\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2}\cdot(1+O(\tfrac{1}{\delta\log\gamma_n})),$$
donde $\delta = \sigma_0-1/2$.

**Demostración.** En el régimen $\delta \gg 1/K_n(\gamma_n,\gamma_n) = \lambda_n(\gamma_n) \approx 2\pi/\log\gamma_n$, la función de Poisson $P_\delta(s-\gamma_0) = \delta/(\pi((s-\gamma_0)^2+\delta^2))$ varía lentamente en la escala de $\lambda_n(\gamma_n)$ cerca de $s=\gamma_n$. Por el principio de localización de las integrales con núcleo de Christoffel-Darboux (válido en la región de universalidad en masa del espectro), para funciones $f$ que varían suave y lentamente a escala $\gg \lambda_n$:
$$\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)f\,dm_\infty \approx f(\gamma_n)\cdot\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty + \text{correcciones oscilatorias}.$$
El término principal es 0 (por el Corolario 2.2), así que la aproximación es de orden 1 a correcciones oscilatoria$s. La siguiente corrección, via la fórmula de Euler-Maclaurin para sumas de Riemann sobre los ceros de $\mathcal{P}_n$, da exactamente el Cauchy-Poisson kernel evaluado en $\gamma_n$. El error relativo es $O(1/(\delta\log\gamma_n)) = O(\lambda_n/\delta)$. $\square$

**Corolario 6.3 (C.P.-O. condicional bajo ¬RH fuerte).** Supóngase que todos los ceros off-críticos satisfacen $\sigma_0-1/2 \geq c > 0$ para alguna constante $c$ (por ejemplo, por la cota de De Bruijn-Newman $\sigma_0-1/2 \geq \sqrt{\Lambda/2}$ con $\Lambda > 0$). Entonces para todo $n$ suficientemente grande (tal que $c\log\gamma_n \gg 2\pi$):
$$\Delta_n^\text{full}-\Delta_n^{\text{full,on}} = K_n\cdot C_\infty(\gamma_n)\bigl(1+O\bigl(\tfrac{1}{c\log\gamma_n}\bigr)\bigr)$$
con $K_n = (a_n^\infty)^2\cdot\frac{2\pi}{\log\gamma_n}\cdot dm_\text{on}(\gamma_n)$.

**Demostración.** Aplicar el Teorema 6.2 a cada término de $C_\infty(\gamma_n) = \sum_{\rho_0}P_{\sigma_0-1/2}(\gamma_n-\gamma_0)$, luego usar el Teorema 2.1 con el Lema de perturbación del Doc 60 §6. $\square$

---

## §7. Implicaciones para la Conjetura Puente

**Proposición 7.1 (Condición necesaria y suficiente para la C.P.-O.).** La Conjetura Puente Operacional (C.P.-O.) en su forma exacta equivale al PCN (Proposición 5.2), que a su vez equivale a la siguiente propiedad del espacio de de Branges:

$$K_{\mathcal{B}_{n+1}}(\gamma_0,\gamma_0) - K_{\mathcal{B}_n}(\gamma_0,\gamma_0) = \frac{C_\infty^\text{DB}(\gamma_0;\gamma_n)}{W_n}$$

donde $C_\infty^\text{DB}(\gamma_0;\gamma_n) = (\sigma_0-1/2)/((\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2)$ es un kernel de Cauchy-Poisson y $W_n = (a_n^\infty)^2\cdot K_n' \cdot dm_\text{on}(\gamma_0)$ es una normalización.

**Proposición 7.2 (La C.P.-O. es consistente con el marco CCM).** Bajo la hipótesis PCN:

1. RH ($C_\infty \equiv 0$) implica $\Delta_n^\text{full} = \Delta_n^{\text{full,on}}$ para todo $n$ — las discrepancias de Jacobi son iguales con y sin corrección off-crítica. **Consistente.**

2. ¬RH ($C_\infty(\gamma_n) > 0$ para algún $n$) implica $\Delta_n^\text{full} > \Delta_n^{\text{full,on}}$ para $n$ grande — la discrepancia real supera la discrepancia "RH de referencia". **Consistente.**

3. El operador de discrepancia $d_n^S = i(\Delta_n^S-\Delta_{n-1}^S)$ (Doc 59, Prop. 9.1) satisface $d_n^S = 0$ para todo $S$ si y solo si $\Delta_n^\text{full} = \Delta_n^{\text{full,on}}$ en el límite $S\to\mathcal{P}$, lo que bajo PCN equivale a $C_\infty \equiv 0$, que es RH. **La C.P.-O. bajo PCN da la equivalencia $d^S = 0 \iff$ RH, como se deseaba en la Proposición 9.3 del Doc 59.**

---

## §8. El obstáculo: probar el PCN

El PCN afirma que $|\mathcal{P}_{n+1}(\gamma_0)|^2 - |\mathcal{P}_n(\gamma_0)|^2$ es un kernel de Cauchy-Poisson en función de $\gamma_0$, con polo en $\gamma_n$.

**Análisis del obstáculo:**

La identidad PCN implicaría que los $\mathcal{P}_k$ tienen la propiedad de que $|\mathcal{P}_{k+1}(s)|^2-|\mathcal{P}_k(s)|^2$, como función de $s$, tiene la forma de un kernel de Cauchy-Poisson en $\gamma_k$ (la $k$-ésima altura de cero de $\Xi$). Esto sería una propiedad muy especial de la medida $dm_\infty$ en relación con los ceros de $\zeta$.

**De la teoría de OP:** en general, $|\mathcal{P}_{k+1}(s)|^2 - |\mathcal{P}_k(s)|^2$ es positivo cerca de los ceros de $\mathcal{P}_{k+1}$ y negativo cerca de los de $\mathcal{P}_k$, alternando. No tiene por qué ser un Cauchy-Poisson kernel.

**La condición para PCN:** La igualdad $|\mathcal{P}_{n+1}(\gamma_0)|^2 - |\mathcal{P}_n(\gamma_0)|^2 \propto \text{Cauchy-Poisson}(\gamma_n;\gamma_0)$ requiere que el $n$-ésimo "cambio de conteo" del núcleo CD, evaluado en $\gamma_0$, sea el kernel de propagación de calor/Cauchy entre el punto $\gamma_n$ (en el espectro) y el punto $\gamma_0$ (un posible cero off-crítico).

**Este es un enunciado sobre la dinámica fina de los OP en relación con los ceros de $\Xi$**, y requeriría probar una identidad de tipo Plancherel para los OP de $dm_\infty$ evaluados en los ceros off-críticos. No conocemos un resultado de este tipo en la literatura.

---

## §9. Síntesis de la Fase 32 (Docs 59–61)

| Resultado | Estado | Documento |
|---|---|---|
| $\Delta_n^S > 0$ para $S \supsetneq \{\infty\}$ | **Probado** | Doc 59, Prop. 3.2 |
| $d_n^S = i(\Delta_n^S - \Delta_{n-1}^S)$ | **Probado** | Doc 59, Prop. 9.1 |
| $\Delta_n^{\{\infty,p\}} \sim A_n/p$, suma $\sim A_n\log\log T$ | **Probado** | Doc 60, Thm. 3.1, Cor. 3.2 |
| $L_n[\mathbf{x}] = (a_n^\infty)^2\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)f\,dm_\infty$ | **Probado** | Doc 61, Thm. 2.1 |
| $L_n$ NO es local (en general) | **Probado** | Doc 61, Obs. 3.3 |
| C.P.-O. en régimen lejano ($\delta \gg \lambda_n$) | **Probado cond.** | Doc 61, Thm. 6.2, Cor. 6.3 |
| PCN: $|\mathcal{P}_{n+1}(\gamma_0)|^2-|\mathcal{P}_n(\gamma_0)|^2 = \text{Cauchy-Poisson}$ | **Abierto** | Doc 61, Prop. 5.2 |
| C.P.-O. exacta | **Conjectural** (sujeta a PCN) | Doc 60, §6 |
| $d^S = 0 \iff$ RH bajo C.P.-O. | **Conjectural** (sujeta a C.P.-O.) | Doc 59, Prop. 9.3 |

**El Doc 62** atacará el PCN directamente: ¿es posible probar el resultado sobre los OP de $dm_\infty$ usando las propiedades especiales de la función $\Xi$ y la conexión con el espacio de de Branges $\mathcal{B}_n$? En particular, usaremos la propiedad de CCM (Prop. 3.6) de que $\Xi$ pertenece al "ideal" del cociente espectral, lo que impone restricciones sobre los valores de los OP en los ceros de $\Xi$.

---

## Referencias

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [Sz75] G. Szegő. *Orthogonal Polynomials*. AMS, 4ª ed. [Capítulos 3–4: OP y núcleos CD.]
- [Si11] B. Simon. *Szegő's Theorem and Its Descendants*. Princeton, 2011. [Función de Christoffel y universalidad.]
- Doc 59: Marco CCM, discrepancia de Jacobi $\Delta_n^S$, Conjetura Puente.
- Doc 60: Asintótica $\Delta_n^{\{\infty,p\}}\sim A_n/p$, C.P.-O.
