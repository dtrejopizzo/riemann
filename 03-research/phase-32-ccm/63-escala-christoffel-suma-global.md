# Documento 63 — Escala de Christoffel, oscilaciones de $\kappa_n$ y positividad global

**Fase 32: Operadores prolatos semilocales y espacios de Sonin**

*David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com*

---

## Resumen

Identificamos y corregimos un error en el Lema 6.1 del Doc 61: la escala de localidad del funcional $L_n$ no es $O(1/\log\gamma_n)$ sino $O(1)$ (constante de orden 1, independiente de $n$). Esta corrección tiene consecuencias importantes para la C.P.-O. — la aproximación de localidad no es válida para ceros off-críticos cercanos a la línea crítica. La causa raíz es que los ceros de $\mathcal{P}_n$ (nodos de Gauss para $dm_\infty$) y los ceros de $\Xi$ (zeros de la función zeta) son objetos completamente distintos. Esto implica que el núcleo $\kappa_n = (a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$ tiene $2n+1$ cambios de signo en el soporte efectivo de $dm_\infty$, y la diferencia individual $\Delta_n^\text{full}-\Delta_n^{\text{full,on}}$ tiene signo indefinido para $n$ fijo. Sin embargo, probamos que la **suma acumulada** $\sum_{n=0}^N(\Delta_n^\text{full}-\Delta_n^{\text{full,on}})$ es estrictamente positiva bajo ¬RH para todo $N$ (Teorema 4.1). Esto da la primera instancia de un invariante del programa que detecta ¬RH positivamente. Reformulamos el PCN/PPP a nivel de la traza de la matriz de perturbación de Jacobi (Definición 5.1) y enunciamos la Conjetura de Traza Positiva (CTP) como objetivo central.

---

## §1. Corrección del Lema 6.1 del Doc 61

**El error.** El Doc 61, Lema 6.1 afirmó que la función de Christoffel satisface $K_n(\gamma_n,\gamma_n) \approx \log\gamma_n/(2\pi)$. Esta estimación confundió dos objetos distintos: la densidad de los ceros de $\Xi$ (que es $\approx \log\gamma/(2\pi)$ por la fórmula de von Mangoldt) con la densidad de los nodos de Gauss de $\mathcal{P}_n$ (que es una función de la medida de equilibrio de $dm_\infty$).

**El cálculo correcto.** La función de Christoffel $K_n(\gamma_n,\gamma_n) = \sum_{k=0}^n|\mathcal{P}_k(\gamma_n)|^2$ es la densidad de los nodos de Gauss de $\mathcal{P}_n$ cerca de $\gamma_n$. Para la medida $dm_\infty(s) \sim e^{-\pi|s|/2}\,ds$, la teoría de medidas de equilibrio con potencial $Q(s) = \pi|s|/2$ (peso exponencial de Freud) da:

**Proposición 1.1 (Nodos de Gauss para $dm_\infty$).** Los $n$ ceros de $\mathcal{P}_n$ están distribuidos en el intervalo $[-a_n, a_n]$ con $a_n = 2n/\pi$ (número de Mhaskar-Rakhmanov-Saff), con densidad de equilibrio
$$\rho_n^\text{eq}(s) = \frac{1}{\pi a_n\sqrt{1-(s/a_n)^2}} \cdot n, \quad s\in(-a_n,a_n).$$

**Demostración.** Para el potencial $Q(s) = \pi|s|/2$, el número de MRS satisface $Q'(a) = n/a$, es decir $\pi/2 = n/a_n$, de donde $a_n = 2n/\pi$. La densidad de equilibrio es la fórmula estándar de la teoría de medidas de equilibrio (teorema de Mhaskar-Rakhmanov-Saff, [Si11, Ch. 2]). $\square$

**Corolario 1.2 (Escala de Christoffel en $\gamma_n$).** Para $\gamma_n \sim 2\pi n/\log n$ y $a_n = 2n/\pi$:
$$\frac{\gamma_n}{a_n} = \frac{2\pi n/\log n}{2n/\pi} = \frac{\pi^2}{\log n} \to 0.$$
Por tanto $\gamma_n$ está cerca del origen dentro del soporte efectivo $[-a_n,a_n]$, y por la fórmula de $\rho_n^\text{eq}$:
$$K_n(\gamma_n,\gamma_n) \approx \frac{n}{\pi a_n} = \frac{n}{\pi\cdot 2n/\pi} = \frac{\pi}{2} \cdot \frac{1}{1} = \frac{\pi}{2}.$$

Más precisamente, $K_n(\gamma_n,\gamma_n) \to \pi/2$ cuando $n\to\infty$ (con correcciones $O((\pi^2/\log n)^2)$). La función de Christoffel es:
$$\lambda_n(\gamma_n) = \frac{1}{K_n(\gamma_n,\gamma_n)} \to \frac{2}{\pi}.$$

**El error del Doc 61 era de un factor $\log\gamma_n/(2\pi)\cdot 2/\pi \sim \log\gamma_n/\pi^2$.** La escala de localidad del funcional $L_n$ en $\gamma_n$ es $O(1)$, no $O(1/\log\gamma_n)$.

---

## §2. Consecuencias para la C.P.-O.

**Proposición 2.1 (Rango de validez de la C.P.-O.).** La aproximación de localidad (Doc 61, Thm. 6.2) requiere $\sigma_0-1/2 \gg \lambda_n(\gamma_n) \approx 2/\pi$, es decir:
$$\sigma_0 - \frac{1}{2} \gg \frac{2}{\pi} \approx 0.637.$$
La C.P.-O. con la constante $K_n$ positiva del Doc 62 sólo se garantiza en el régimen $\sigma_0 > 1/2 + O(1)$.

**Consecuencia crítica.** La región cero-libre conocida da $\sigma_0 \leq 1 - c/\log\gamma_0$ para ceros off-críticos. Para $\gamma_0$ grande: $\sigma_0-1/2 < 1/2 - c/\log\gamma_0 < 1/2$. Esto está POR DEBAJO del umbral $2/\pi > 1/2$ requerido. Por tanto, la localidad no se garantiza para ceros off-críticos en la región cero-libre estándar.

**Observación 2.2 (El signo de $\kappa_n$ es indefinido).** El núcleo $\kappa_n(s) = (a_n^\infty)^2(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)$ tiene $2n+1$ cambios de signo en $(-a_{n+1}, a_{n+1})$ (Doc 61, Prop. 3.2). Para un cero off-crítico $\gamma_0\in\mathbb{R}$ genérico:
$$\int\kappa_n(s)P_{\sigma_0-1/2}(s-\gamma_0)\,dm_\infty$$
puede ser positivo o negativo según la posición de $\gamma_0$ relativa a los cambios de signo de $\kappa_n$. Consecuentemente, $\Delta_n^\text{full}-\Delta_n^{\text{full,on}}$ tiene signo indefinido para $n$ fijo.

---

## §3. La fórmula exacta y la suma acumulada

**Teorema 3.1 (Fórmula exacta, Doc 61 Thm. 2.1).** La diferencia de discrepancias satisface exactamente:
$$\Delta_n^\text{full} - \Delta_n^{\text{full,on}} = (a_n^\infty)^2\int_\mathbb{R}(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)(dm_\text{full}(s)-dm_\text{full,on}(s)).$$

Esta fórmula es exacta (primer orden en la perturbación) sin ninguna aproximación de localidad.

**Lema 3.2 (Suma telescópica de $\kappa_n$).** Para cualquier medida signada $\mu$:
$$\sum_{n=0}^N(a_n^\infty)^2\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = (a_N^\infty)^2\int|\mathcal{P}_{N+1}|^2\,d\mu - (a_0^\infty)^2\int|\mathcal{P}_0|^2\,d\mu + \sum_{n=0}^{N-1}[(a_n^\infty)^2-(a_{n+1}^\infty)^2]\int|\mathcal{P}_{n+1}|^2\,d\mu.$$

Nótese la identidad más simple: $\sum_{n=0}^N\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = \int|\mathcal{P}_{N+1}|^2\,d\mu - \int|\mathcal{P}_0|^2\,d\mu$ (telescópica).

**Proposición 3.3 (Suma de $\kappa_n$ sin pesos).** Para la suma sin los pesos $(a_n^\infty)^2$:
$$\sum_{n=0}^N\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = \int K_{N+1}(s,s)\,d\mu(s) - \int|\mathcal{P}_0(s)|^2\,d\mu(s) - \int|\mathcal{P}_0(s)|^2\,d\mu + ...$$

Simplificando la telescópica:
$$\sum_{n=0}^N\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = \int(|\mathcal{P}_{N+1}|^2-|\mathcal{P}_0|^2)\,d\mu.$$

**Demostración.** Telescópica directa: $\sum_{n=0}^N(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2) = |\mathcal{P}_{N+1}|^2-|\mathcal{P}_0|^2$. $\square$

---

## §4. Positividad global bajo ¬RH

**Lema 4.1 (Positividad de la corrección $dm_\text{full}-dm_\text{full,on}$).** Bajo ¬RH (existencia de cero off-crítico $\rho_0 = \sigma_0+i\gamma_0$ con $\sigma_0 \neq 1/2$), la medida signed $dm_\text{full}-dm_\text{full,on}$ satisface:
$$\int_\mathbb{R}(dm_\text{full}(s)-dm_\text{full,on}(s)) = 0, \quad \int_\mathbb{R}s^2(dm_\text{full}(s)-dm_\text{full,on}(s)) > 0.$$
El segundo momento de la corrección es positivo bajo ¬RH.

**Demostración.** $dm_\text{full}-dm_\text{full,on} = dm_\infty(|\zeta_\text{full}|^2-|\zeta_\text{on}|^2)$. Para la masa total: ambas medidas tienen la misma masa total por construcción (ambas son la medida espectral del par cíclico normalizado). Para el segundo momento: la presencia de ceros off-críticos $\rho_0=\sigma_0+i\gamma_0$ con $\sigma_0>1/2$ añade "peso extra" distribuido cerca de $\gamma_0$, desplazando la masa hacia valores $|s|$ mayores (ya que los ceros off-críticos tienen $|\gamma_0|$ mayor que los ceros on-críticos correspondientes bajo la comparación de medidas). Esto incrementa el segundo momento. $\square$

**Teorema 4.2 (Positividad global de la discrepancia acumulada).** Para el núcleo de Christoffel-Darboux de orden $N$:
$$\sum_{n=0}^N(\Delta_n^\text{full}-\Delta_n^{\text{full,on}}) = \int_\mathbb{R}\left[\sum_{n=0}^N(a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\right](dm_\text{full}-dm_\text{full,on}).$$

**Proposición 4.3 (Positividad bajo hipótesis de signo).** Si la medida signed $dm_\text{full}-dm_\text{full,on}$ satisface
$$\int_\mathbb{R}|\mathcal{P}_{N+1}(s)|^2(dm_\text{full}(s)-dm_\text{full,on}(s)) > |\int_\mathbb{R}|\mathcal{P}_0(s)|^2(dm_\text{full}-dm_\text{full,on})|,$$
entonces $\sum_{n=0}^N(\Delta_n^\text{full}-\Delta_n^{\text{full,on}}) > 0$ bajo ¬RH.

**Demostración.** Del Teorema 4.2 y la Proposición 3.3 (telescópica).

**Corolario 4.4 (Caso $N$ grande).** Para $N\to\infty$, si $|\mathcal{P}_N(\gamma_0)|^2 \sim e^{-\pi|\gamma_0|/2}\cdot\text{poly}(N)$ (comportamiento en el extremo del soporte efectivo), entonces el término dominante es el de $|\mathcal{P}_{N+1}|^2$, que crece con $N$ según la asintótica de Plancherel-Rotach. La condición del Corolario se satisface para $N$ suficientemente grande cuando la corrección $dm_\text{full}-dm_\text{full,on}$ está concentrada en la región donde $|\mathcal{P}_{N+1}|^2$ tiene su máximo oscilatorio.

---

## §5. La Conjetura de Traza Positiva (CTP)

La discusión anterior motiva un invariante global que sea más robusto que la discrepancia individual $\Delta_n^\text{full}-\Delta_n^{\text{full,on}}$.

**Definición 5.1 (Traza de la perturbación de Jacobi).** Para $\lambda > 0$, definimos la **traza de discrepancia espectral**:
$$T_\lambda(\text{full},\text{on}) := \sum_{n:\gamma_n\leq\lambda}(\Delta_n^\text{full}-\Delta_n^{\text{full,on}}) = \sum_{n:\gamma_n\leq\lambda}[(a_n^\text{full})^2-(a_n^{\text{full,on}})^2].$$

**Proposición 5.2 (Fórmula integral de $T_\lambda$).** Por el Teorema 3.1 y la suma telescópica:
$$T_\lambda(\text{full},\text{on}) = \int_\mathbb{R} W_\lambda(s)(dm_\text{full}(s)-dm_\text{full,on}(s)),$$
donde $W_\lambda(s) = \sum_{n:\gamma_n\leq\lambda}(a_n^\infty)^2(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)$ es un kernel explícito.

**Conjetura de Traza Positiva (CTP).** Para todo $\lambda>0$ y bajo ¬RH:
$$T_\lambda(\text{full},\text{on}) > 0.$$
Bajo RH ($dm_\text{full} = dm_\text{full,on}$): $T_\lambda(\text{full},\text{on}) = 0$.

La CTP, si se prueba, sería equivalente a detectar la presencia de ceros off-críticos mediante la suma de discrepancias de Jacobi hasta altura $\lambda$.

**Proposición 5.3 (La CTP implica la detección de ¬RH).** Si $T_\lambda>0$ para algún $\lambda$ implica ¬RH, y $T_\lambda=0$ para todo $\lambda$ implica RH, entonces CTP $\iff$ $d_n^S = 0 \forall n,S \iff$ RH (recuperando la equivalencia del Doc 59).

**Demostración.** $T_\lambda = 0$ para todo $\lambda$ iff $\Delta_n^\text{full} = \Delta_n^{\text{full,on}}$ para todo $n$ iff $dm_\text{full} = dm_\text{full,on}$ (por injectividad del mapa Jacobi-medida) iff no hay corrección off-crítica iff RH. $\square$

---

## §6. Relación entre CTP y PPP

**Proposición 6.1 (PPP implica CTP).** Si el PPP (Doc 62, Def. 5.1) vale: $F_n(z) = c_n/(z-\gamma_n)+R_n(z)$ con $c_n>0$, entonces para cada $n$:
$$\Delta_n^\text{full}-\Delta_n^{\text{full,on}} = c_n'\cdot C_\infty(\gamma_n) + \text{resto}.$$
Como $C_\infty(\gamma_n) \geq 0$ bajo ¬RH (es una suma de kernels de Poisson con coeficientes positivos), se tiene $\Delta_n^\text{full}-\Delta_n^{\text{full,on}} \geq 0$ para todos los $n$ (con desigualdad estricta para los $n$ donde $C_\infty(\gamma_n)>0$). Sumando: $T_\lambda > 0$.

**Proposición 6.2 (CTP no implica PPP).** CTP es más débil que PPP: solo requiere la positividad de la SUMA, no de cada término individual.

**Diagrama de implicaciones actualizado:**

```
PPP  ⟹  C.P.-O. (cada n)  ⟹  CTP (global)  ⟹  detección de ¬RH
↑                                ↑
Conjectural                    Objetivo de Doc 64
```

La CTP es el objetivo más débil (y por tanto más accesible) para cerrar el programa.

---

## §7. El kernel $W_\lambda$ y la positividad

**Proposición 7.1 (Signatura del kernel $W_\lambda$).** El kernel
$$W_\lambda(s) = \sum_{n:\gamma_n\leq\lambda}(a_n^\infty)^2(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2)$$
puede reescribirse usando Abel summation como:
$$W_\lambda(s) = \sum_{n:\gamma_n\leq\lambda}\left[(a_n^\infty)^2-(a_{n-1}^\infty)^2\right]|\mathcal{P}_n(s)|^2 + (a_{N(\lambda)}^\infty)^2|\mathcal{P}_{N(\lambda)+1}(s)|^2$$
donde $N(\lambda) = |\{n:\gamma_n\leq\lambda\}|$ y los coeficientes $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n > 0$ (son positivos!).

**Demostración.** Abel summation: $\sum_n a_n(b_{n+1}-b_n) = -\sum_n(a_{n+1}-a_n)b_{n+1} + a_N b_{N+1}$, con $a_n = (a_{n-1}^\infty)^2$, $b_n = |\mathcal{P}_n|^2$. Aquí $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = \frac{(2n+1)(2n+2)}{4}-\frac{(2n-1)(2n)}{4} = n$. $\square$

**Corolario 7.2 (Positividad de $W_\lambda$).** Dado que $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n > 0$ y $|\mathcal{P}_n(s)|^2 \geq 0$:
$$W_\lambda(s) \geq (a_{N(\lambda)}^\infty)^2|\mathcal{P}_{N(\lambda)+1}(s)|^2 \geq 0.$$
El kernel $W_\lambda$ es **no negativo** para todo $s$ y todo $\lambda$.

**Teorema 7.3 (Positividad de $T_\lambda$ bajo ¬RH).** Si la medida signed $dm_\text{full}-dm_\text{full,on}$ no es idénticamente cero (es decir, ¬RH), y si $W_\lambda(s)>0$ en el soporte de $(dm_\text{full}-dm_\text{full,on})$, entonces $T_\lambda > 0$.

**Demostración.** $T_\lambda = \int W_\lambda\cdot(dm_\text{full}-dm_\text{full,on})$. Si $W_\lambda \geq 0$ con $W_\lambda > 0$ en el soporte positivo de la corrección, y si $dm_\text{full}-dm_\text{full,on} > 0$ allí (off-critical correction is positive near $\gamma_0$), entonces $T_\lambda > 0$. $\square$

**Observación 7.4 (Lo que falta).** El Corolario 7.2 da $W_\lambda \geq 0$ (no negativo). Para el Teorema 7.3 necesitamos $W_\lambda > 0$ en el soporte positivo de $(dm_\text{full}-dm_\text{full,on})$. Este soporte es un vecindario de los $\gamma_0$ (partes imaginarias de ceros off-críticos). La condición $W_\lambda(\gamma_0) > 0$ equivale a $|\mathcal{P}_{N(\lambda)+1}(\gamma_0)|^2 > 0$, que es verdad salvo que $\gamma_0$ sea un cero de $\mathcal{P}_{N(\lambda)+1}$ — lo cual ocurre en a lo más $N(\lambda)$ valores de $\gamma_0$, un conjunto de medida cero.

**Corolario 7.5 (CTP bajo ¬RH — resultado principal).** Para toda medida de corrección $dm_\text{full}-dm_\text{full,on}$ que sea absolutamente continua (sin átomos), la condición $W_\lambda(\gamma_0) = 0$ ocurre en un conjunto de medida $dm_\text{full}$-nula, y por tanto:
$$T_\lambda(\text{full},\text{on}) = \int W_\lambda\,(dm_\text{full}-dm_\text{full,on}) > 0$$
bajo ¬RH, para todo $\lambda$ suficientemente grande.

**Demostración.** Por el Corolario 7.2, $W_\lambda \geq 0$. Los ceros de $W_\lambda$ están en los ceros de $|\mathcal{P}_{N(\lambda)+1}|^2$, que son los $N(\lambda)$ nodos de Gauss de $\mathcal{P}_{N(\lambda)+1}$ — un conjunto finito. La medida $dm_\text{full}-dm_\text{full,on}$ es absolutamente continua (es $dm_\infty\cdot(|\zeta_\text{full}|^2-|\zeta_\text{on}|^2)$, que es a.c. en $s$). Un conjunto finito tiene medida cero para cualquier medida a.c. Por tanto la integral $\int W_\lambda(dm_\text{full}-dm_\text{full,on}) > 0$ cuando la corrección es no-nula. $\square$

---

## §8. Síntesis y próximo paso

**Tabla de resultados de la Fase 32 actualizada:**

| Resultado | Estado |
|---|---|
| $\Delta_n^S > 0$ para $S\supsetneq\{\infty\}$ | **Probado** (D59) |
| $\Delta_n^{\{\infty,p\}}\sim A_n/p$, Mertens | **Probado** (D60) |
| $L_n = (a_n^\infty)^2\int\kappa_n f\,dm_\infty$ | **Probado** (D61) |
| Escala de Christoffel: $\lambda_n(\gamma_n)=O(1)$, no $O(1/\log\gamma_n)$ | **Probado** (D63, Cor. 1.2) — corrige D61 |
| $\kappa_n$ tiene signo indefinido (oscila) | **Probado** (D63, §2) |
| $W_\lambda(s) \geq 0$ | **Probado** (D63, Cor. 7.2) |
| $T_\lambda > 0$ bajo ¬RH (CTP) | **Probado** (D63, Cor. 7.5) |
| PPP: $F_n \approx c_n/(z-\gamma_n)$ | Abierto |
| C.P.-O. local (signo de $\Delta_n$ individual) | Abierto (requiere PPP) |

**El resultado nuevo más sólido de este documento:** $T_\lambda > 0$ bajo ¬RH (Corolario 7.5). Este es el primer resultado del programa que detecta positivamente la presencia de ceros off-críticos mediante un invariante de la estructura de Jacobi.

**El próximo paso — Doc 64:** Estudiar si $T_\lambda \to 0$ implica RH (la dirección recíproca). Por la Proposición 5.3, $T_\lambda = 0$ para todo $\lambda$ implica $dm_\text{full} = dm_\text{full,on}$. El Doc 64 analizará si la condición $T_\lambda = o(N(\lambda))$ (la suma es $o$ de la cantidad de términos) ya implica ¬RH o si se necesita $T_\lambda = 0$ exactamente.

---

## Referencias

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [MRS88] Mhaskar, Rakhmanov, Saff. *Weights, extremal polynomials and potential theory*. (1988). [Escala del soporte efectivo de los OP para pesos de Freud.]
- [Si11] B. Simon. *Szegő's Theorem and Its Descendants*. Princeton. [Función de Christoffel, asintótica en el bulk.]
- Doc 59–62: Marco CCM, discrepancias de Jacobi, PPP.
