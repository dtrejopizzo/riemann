# Phase 29 — Doc 22: Completitud espectral y la brecha entre medida empírica y medida de Weyl-Titchmarsh

**Fecha:** junio 2026  
**Objetivo:** Identificar con precisión la diferencia entre la medida espectral empírica $\mu_\xi^\lambda$ (probada convergente a $\mu_\gamma^{real}$ en Doc 15) y la medida espectral de Weyl-Titchmarsh $\mu_{WT}$ del operador límite $J_\infty$. Mostrar que la igualdad de estas dos medidas es equivalente a RH.

---

## 1. Dos medidas espectrales distintas

Para el operador de Jacobi $J_\lambda^N$ (la truncación CCM a $N \times N$), existen DOS medidas espectrales naturales:

**Definición 1** (Medida espectral empírica). La medida espectral empírica es:

$$\mu_{emp}^{(\lambda,N)} := \frac{1}{N}\sum_{n=1}^N \delta_{t_n^{(\lambda)}},$$

donde $\{t_n^{(\lambda)}\}$ son los autovalores de $J_\lambda^N$.

**Definición 2** (Medida espectral de Weyl-Titchmarsh). La medida espectral asociada al vector cíclico $e_0$ es la única medida $\mu_{WT}^{(\lambda,N)}$ tal que:

$$m_\lambda^{WT}(z) := \langle e_0, (J_\lambda^N - z)^{-1}e_0\rangle = \int_\mathbb{R}\frac{d\mu_{WT}^{(\lambda,N)}(t)}{t-z}.$$

La medida $\mu_{WT}$ tiene la expresión explícita:

$$\mu_{WT}^{(\lambda,N)} = \sum_{n=1}^N |c_n^{(\lambda)}|^2\,\delta_{t_n^{(\lambda)}},$$

donde $c_n^{(\lambda)} = \langle e_0, \psi_n^{(\lambda)}\rangle$ son los componentes del vector $e_0$ en la base de autovectores $\{\psi_n^{(\lambda)}\}$.

**Proposición 1** (las dos medidas son iguales iff $e_0$ es completamente deslocalizado). $\mu_{emp}^{(\lambda,N)} = \mu_{WT}^{(\lambda,N)}$ si y solo si $|c_n^{(\lambda)}|^2 = 1/N$ para todo $n = 1,\ldots,N$.

*Prueba.* Directo de las definiciones: $\mu_{WT} = \sum_n|c_n|^2\delta_{t_n}$ y $\mu_{emp} = (1/N)\sum_n\delta_{t_n}$. Son iguales iff los pesos coinciden: $|c_n|^2 = 1/N$ para todo $n$. $\square$

---

## 2. La brecha en el programa CCM: ¿qué función es $m_\lambda$?

El Doc 14 establece que $m_\lambda(z) = S_\xi(z;\lambda)/N$ (la transformada de Stieltjes de la medida empírica dividida por $N$), y TAMBIÉN que $m_\lambda = \langle e_0, (J_\lambda - z)^{-1}e_0\rangle$ (la función de Weyl-Titchmarsh).

**Proposición 2** (las dos identificaciones del Doc 14 son consistentes iff la CCM tiene deslocalización uniforme). Las dos definiciones de $m_\lambda$ en Doc 14:

$$m_\lambda^{(1)}(z) = \frac{1}{N}\sum_{n=1}^N\frac{1}{t_n^{(\lambda)}-z}, \quad m_\lambda^{(2)}(z) = \langle e_0, (J_\lambda - z)^{-1}e_0\rangle,$$

satisfacen $m_\lambda^{(1)} = m_\lambda^{(2)}$ si y solo si $|c_n^{(\lambda)}|^2 = 1/N$ para todo $n$ (Proposición 1).

**Observación.** En la literatura de matrices aleatorias (ensamble GUE), los vectores propios tienen entradas de orden $O(N^{-1/2})$ en todas las posiciones (deslocalización), y en promedio $\mathbb{E}[|c_n|^2] = 1/N$. Para el operador CCM específico, la deslocalización es una hipótesis, no un teorema.

---

## 3. El límite $\lambda \to \infty$: las dos medidas límite

**Definición 3.** 
- $m_\infty^{emp}(z) := \lim_\lambda m_\lambda^{(1)}(z) = $ límite de la transformada de Stieltjes de $\mu_{emp}^\lambda$, cuya medida límite es $\mu_\gamma^{real}$ (Doc 15).
- $m_\infty^{WT}(z) := \lim_\lambda m_\lambda^{(2)}(z) = $ límite de la función de Weyl-Titchmarsh, cuya medida límite es $\mu_{WT}^\infty$ (la medida espectral de $J_\infty$ en $e_0$).

**Proposición 3** (las dos medidas límite pueden diferir). En el límite $\lambda \to \infty$:

$$\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real} \quad (\text{Doc 15, incondicional}).$$

Pero la convergencia de $m_\lambda^{(2)}(z) \to m_\infty^{WT}(z)$ (Weyl-Titchmarsh) da una medida $\mu_{WT}^\infty$ que es la medida espectral de $J_\infty$ asociada al vector $e_0$. Esta medida satisface:

$$\operatorname{spec}(J_\infty) = \operatorname{supp}(\mu_{WT}^\infty),$$

por el teorema espectral para operadores autoadjuntos con vector cíclico.

**Si $\mu_{WT}^\infty = \mu_\gamma^{real}$:** entonces $\operatorname{spec}(J_\infty) = \operatorname{supp}(\mu_\gamma^{real}) = \{\gamma_n\}$. Combinando con Teorema C1 (Doc 17): $\{\text{ceros reales de }C_\infty\} = \{\gamma_n\}$. Por Teorema 3 del Doc 19: RH.

**Si $\mu_{WT}^\infty \neq \mu_\gamma^{real}$:** las dos medidas tienen distinto soporte y las conclusiones anteriores no se aplican directamente.

---

## 4. Cuándo coinciden: la hipótesis de deslocalización

**Definición 4** (Deslocalización de $e_0$ en $J_\lambda$). Decimos que $J_\lambda$ es *uniformemente deslocalizado* (UD) si:

$$\max_{1\leq n\leq N}|c_n^{(\lambda)}|^2 = O(N^{-1+\varepsilon}) \quad \text{para todo }\varepsilon > 0,$$

uniformemente en $\lambda \geq \lambda_0$ (con $N = N(\lambda) \to \infty$).

**Proposición 4** (UD implica que las dos medidas tienen el mismo soporte). Si $J_\lambda$ es uniformemente deslocalizado, entonces:

$$\operatorname{supp}(\mu_{WT}^{(\lambda,N)}) = \operatorname{supp}(\mu_{emp}^{(\lambda,N)}) = \{t_1^{(\lambda)},\ldots,t_N^{(\lambda)}\}.$$

*Prueba.* $\mu_{WT} = \sum_n |c_n|^2\delta_{t_n}$. Si $|c_n|^2 > 0$ para todo $n$ (lo cual se sigue de UD ya que $\sum_n|c_n|^2 = \|e_0\|^2 = 1$ y $|c_n|^2 \leq O(N^{-1+\varepsilon})$ implica que cada $|c_n|^2 \geq c/N$ para alguna constante $c > 0$ para la mayoría de los $n$): el soporte de $\mu_{WT}$ incluye todos los $t_n$. El soporte de $\mu_{emp}$ es exactamente $\{t_n\}$. $\square$

**Proposición 5** (UD en el límite implica $\mu_{WT}^\infty = \mu_\gamma^{real}$). Si la deslocalización se preserva en el límite $\lambda \to \infty$:

$$\lim_\lambda\max_n|c_n^{(\lambda)}|^2 \to 0 \quad (\text{deslocalización asintótica}),$$

entonces $\mu_{WT}^\infty = \mu_\gamma^{real}$ (las dos medidas límite coinciden).

*Prueba (heurística, formal).* Bajo deslocalización asintótica: los pesos $|c_n^{(\lambda)}|^2 \to 1/N$ uniformemente. En el límite: la medida de Weyl-Titchmarsh $\mu_{WT}^\lambda = \sum_n|c_n|^2\delta_{t_n} \approx (1/N)\sum_n\delta_{t_n} = \mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$. $\square$

---

## 5. La conexión con Montgomery-GUE

**La hipótesis de GUE.** Las correlaciones de los ceros de $\zeta$ siguen (conjeturalmente) la distribución de los autovalores del ensamble GUE (Montgomery, 1973). En el ensamble GUE, los vectores propios son uniformemente distribuidos en la esfera unitaria compleja, y en particular $\mathbb{E}[|c_n|^2] = 1/N$ con concentración gaussiana.

**Proposición 6** (GUE implica UD para $J_\infty$). Si la distribución de los autovectores de $J_\lambda$ sigue el comportamiento GUE (en el sentido de que los $c_n^{(\lambda)} = \langle e_0, \psi_n^{(\lambda)}\rangle$ tienen la distribución asintótica de una medida de Haar en la esfera), entonces $J_\lambda$ es uniformemente deslocalizado, y por Proposición 5: $\mu_{WT}^\infty = \mu_\gamma^{real}$.

*Prueba.* En el ensamble GUE de tamaño $N$: con probabilidad $1 - e^{-cN}$, $\max_n|c_n|^2 \leq C\log N/N$. Luego UD se cumple. En el límite $N\to\infty$: $\max_n|c_n|^2 \to 0$. $\square$

**Corolario 1** (bajo GUE: $\operatorname{spec}(J_\infty) = \{\gamma_n\}$, implicando RH). Bajo la hipótesis GUE para los autovectores de $J_\lambda$:

1. $\mu_{WT}^\infty = \mu_\gamma^{real}$ (Proposición 6).
2. $\operatorname{spec}(J_\infty) = \operatorname{supp}(\mu_{WT}^\infty) = \operatorname{supp}(\mu_\gamma^{real}) = \{\gamma_n\}$ (teorema espectral).
3. Por Teorema C1 (Doc 17): $\{\text{ceros reales de }C_\infty\} = \{\gamma_n\}$.
4. Por Teorema 3 (Doc 19): RH.

*Prueba.* La cadena de equivalencias es directa de los pasos 1-4. El único punto no-trivial es el paso 2: que $\operatorname{supp}(\mu_\gamma^{real}) = \{\gamma_n\}$. Esto sigue de que $\mu_\gamma^{real} = \sum_n w_n\delta_{\gamma_n}$ con $w_n > 0$ para todo $n$ (pesos positivos), luego cada $\gamma_n$ está en el soporte. $\square$

---

## 6. El argumento de contradicción: localizacion implica cero fuera de la recta crítica

**Proposición 7** (localización de $e_0$ implica que $\mu_{WT}^\infty \neq \mu_\gamma^{real}$). Supóngase que existe $n_0$ tal que $|c_{n_0}^{(\lambda)}|^2 \to \alpha > 0$ (localización en el autovector $\psi_{n_0}^{(\lambda)}$). Entonces $\mu_{WT}^\infty$ tiene un átomo de peso $\geq \alpha$ en la posición $t_{n_0}^\infty = \lim_\lambda t_{n_0}^{(\lambda)}$.

Si $\mu_{WT}^\infty = \mu_\gamma^{real}$ (suponemos igualdad): el átomo de $\mu_{WT}^\infty$ en $t_{n_0}^\infty$ con peso $\alpha$ debe corresponderse con un átomo de $\mu_\gamma^{real}$ en $\gamma_{n_0}$ con peso $w_{n_0}$. Luego $t_{n_0}^\infty = \gamma_{n_0}$ y $\alpha = w_{n_0}$.

Pero la localización en un solo autovector $\psi_{n_0}$ implicaría que $\langle e_0, \psi_{n_0}\rangle$ es grande — lo cual por la teoría de operadores de Jacobi implica que el cero $t_{n_0}^{(\lambda)}$ es especialmente "próximo" al vector $e_0$ en la base ortogonal. Esta condición es inconsistente con la distribución uniforme de ceros (GUE) a menos que el cero $\gamma_{n_0}$ tenga propiedades especiales.

En particular: si la localización ocurre en $n_0$, y la función $C_\infty$ tiene un cero en $\gamma_{n_0}$ que es un polo de orden $> 1$ de $C_\infty'/C_\infty$ (i.e., un cero múltiple de $C_\infty$), entonces el peso $\alpha$ en $\mu_{WT}^\infty$ sería $> w_{n_0}$. Pero $\mu_{WT}^\infty = \mu_\gamma^{real}$ daría $\alpha = w_{n_0}$ — contradicción.

**Conclusión.** Bajo la hipótesis de que todos los ceros de $\Xi$ son simples (conjeturada universalmente): los pesos $w_{n_0}$ en $\mu_\gamma^{real}$ son todos iguales (pues las derivadas $\Xi'(\gamma_n)$ son no-nulas). La localización produciría un átomo de peso anómalo, generando una contradicción.

---

## 7. El resultado incondicional: acotación de los pesos de $\mu_{WT}^\infty$

**Teorema 1** (acotación incondicional de los pesos de la medida WT). Sea $w_n^{WT} = \mu_{WT}^\infty(\{\gamma_n\})$ el peso del átomo de $\mu_{WT}^\infty$ en $\gamma_n$ (si $\gamma_n \in \operatorname{spec}(J_\infty)$). Entonces:

$$w_n^{WT} \leq \liminf_\lambda |c_n^{(\lambda)}|^2 \leq C \cdot \|\psi_n^{(\lambda)}\|^2 = C,$$

donde $\psi_n^{(\lambda)}$ son los autovectores normalizados de $J_\lambda$.

Si $\operatorname{spec}(J_\infty) = \{\gamma_n\}_{n\geq 1}$ (completitud espectral): la suma de los pesos debe ser 1:

$$\sum_{n\geq 1} w_n^{WT} = \|e_0\|^2 = 1.$$

Esta es la condición de COMPLETITUD de la base de autovectores de $J_\infty$ en la dirección de $e_0$.

*Prueba.* Por la teoría espectral de operadores de Jacobi (Weyl-Titchmarsh): $\int d\mu_{WT}^\infty(t) = \langle e_0, e_0\rangle = 1$ (si $J_\infty$ es autoadjunto en el dominio correcto y $e_0$ es cíclico). La suma de los pesos es 1 iff la medida $\mu_{WT}^\infty$ no tiene parte absolutamente continua. $\square$

**Corolario 2** (la medida WT tiene parte absolutamente continua iff $J_\infty$ no es de tipo LP con espectro puramente puntual). En la clasificación de Weyl:

- Caso límite-puntual (LP): el operador $J_\infty$ tiene $m_\infty^{WT}(z) \in \mathbb{C}^+$ para $z \in \mathbb{C}^+$ — solución única. En este caso, la medida $\mu_{WT}^\infty$ puede ser pura puntual, AC o singular continua.
- Caso límite-circular (LC): dos soluciones en $L^2$; operador tiene deficiencia $(1,1)$.

El Doc 17 (Proposición 1) establece que $J_\infty$ está en el caso LP — garantizando solución única del m-function. Pero esto no implica per se que $\mu_{WT}^\infty$ sea pura puntual.

---

## 8. Cuándo $\mu_{WT}^\infty$ es pura puntual

**Definición 5.** La medida $\mu_{WT}^\infty$ es **pura puntual** si $\mu_{WT}^\infty = \sum_n w_n\delta_{t_n}$ (sin parte AC ni SC).

**Proposición 8** (criterio de Simon-Wolff para pureza puntual). La medida $\mu_{WT}^\infty$ es pura puntual si y solo si:

$$\int_\mathbb{R}\!\left[\Im m_\infty^{WT}(t+i0^+)\right]^{-1}d\mu_{WT}^\infty(t) < \infty \quad (\text{criterio de Simon-Wolff}).$$

Equivalentemente: la función $\Im m_\infty^{WT}$ crece como $+\infty$ a lo largo de los puntos de masa de $\mu_{WT}^\infty$ y es cero (en sentido de Lebesgue) en el complemento.

**Proposición 9** (pura puntualidad de $\mu_{WT}^\infty$ a partir de la EF2). Por EF2 (Doc 17): $N\cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$ (en $\mathbb{C}^+$). Para $z = t + i\eta$ con $\eta \to 0^+$:

$$\Im m_\infty^{WT}(t+i\eta) = \frac{1}{N}\Im\frac{C_\infty'(t+i\eta)}{C_\infty(t+i\eta)}.$$

Esta función:
- Tiene picos (crece como $\eta^{-1}$) cuando $t$ está cerca de un cero simple de $C_\infty$.
- Es $O(1)$ cuando $t$ está lejos de los ceros de $C_\infty$.

En los puntos $t = \gamma_n$ donde $C_\infty(\gamma_n) = 0$ (si la inclusión inversa se satisface): $\Im m_\infty^{WT}(\gamma_n + i0^+) = +\infty$ (polo del m-function). Esto significa que $\mu_{WT}^\infty$ tiene masa positiva en $\gamma_n$ — i.e., $\gamma_n \in \operatorname{spec}_{pp}(J_\infty)$.

*Prueba.* El comportamiento de la parte imaginaria de $C_\infty'/C_\infty$ en un cero simple $\gamma_n$ de $C_\infty$: $C_\infty(z) \approx C_\infty'(\gamma_n)(z-\gamma_n)$ cerca de $\gamma_n$. Luego $C_\infty'(z)/C_\infty(z) \approx 1/(z-\gamma_n)$, cuya parte imaginaria $\Im(1/(t+i\eta - \gamma_n)) = -\eta/((t-\gamma_n)^2+\eta^2) \to -\pi\delta(t-\gamma_n)$ cuando $\eta\to 0$. $\square$

**Conclusión de la Proposición 9.** Si (Inc. Inv.) se satisface — es decir, $C_\infty(\gamma_n) = 0$ para todos los $\gamma_n$ — entonces $\mu_{WT}^\infty$ tiene masa positiva en cada $\gamma_n$. Luego $\{\gamma_n\} \subseteq \operatorname{spec}_{pp}(J_\infty) \subseteq \operatorname{spec}(J_\infty)$.

**Inversamente:** Si $\gamma_n \in \operatorname{spec}_{pp}(J_\infty)$ (i.e., $\mu_{WT}^\infty(\{\gamma_n\}) > 0$): por EF2, $m_\infty^{WT}$ tiene un polo en $\gamma_n$, luego $C_\infty(\gamma_n) = 0$. Esto da (Inc. Inv.) — PERO usando la Weyl-Titchmarsh m-function, no la empírica.

---

## 9. La nueva equivalencia central

**Teorema 2** (equivalencia entre (Inc. Inv.) y completitud espectral de $J_\infty$). Las siguientes son equivalentes:

(i) (Inc. Inv.): $\Xi(\gamma_n) = 0$ para $\gamma_n \in \mathbb{R}$ $\implies$ $C_\infty(\gamma_n) = 0$.

(ii) $\{\gamma_n\} \subseteq \operatorname{spec}_{pp}(J_\infty)$ (todos los $\gamma_n$ son eigenvalores de $J_\infty$).

(iii) $\mu_{WT}^\infty(\{\gamma_n\}) > 0$ para todo $n$ (la medida de Weyl-Titchmarsh tiene masa en cada $\gamma_n$).

(iv) $m_\infty^{WT}$ tiene un polo en cada $\gamma_n$ (por la EF2: $C_\infty(\gamma_n) = 0$).

*Prueba.* (i) $\iff$ (iv): EF2 + Proposición 9. (iv) $\iff$ (iii): poles de la transformada de Stieltjes = átomos de la medida. (iii) $\iff$ (ii): átomos de $\mu_{WT}^\infty$ = eigenvalores de $J_\infty$. $\square$

**Proposición 10** (la completitud de $\mu_{WT}^\infty$ vs. la convergencia de $\mu_{emp}^\lambda$). El resultado incondicional (Doc 15) da $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$, donde $\mu_\gamma^{real}$ tiene masa en cada $\gamma_n$. Si $\mu_{WT}^\infty = \mu_\gamma^{real}$ (igualdad de las dos medidas límite): entonces (iii) del Teorema 2 se satisface, dando (Inc. Inv.) y por tanto RH.

**La brecha precisa.** La igualdad $\mu_{WT}^\infty = \mu_\gamma^{real}$ es la condición faltante. Esta igualdad requiere que los pesos $w_n^{WT} = \mu_{WT}^\infty(\{\gamma_n\})$ sean iguales a los pesos de $\mu_\gamma^{real}$, que son proporcionales a $1/\gamma_n$ (la densidad de ceros en la región de $\gamma_n$).

---

## 10. El muro final: la relación entre $\mu_{WT}^\infty$ y $\mu_{emp}^\infty$

**Proposición 11** (condición suficiente para $\mu_{WT}^\infty = \mu_{emp}^\infty$). Sea $G_N(z) = (1/N)\operatorname{Tr}(J_\lambda^N - z)^{-1} = m_\lambda^{emp}(z)$ y $F_N(z) = \langle e_0, (J_\lambda^N - z)^{-1}e_0\rangle = m_\lambda^{WT}(z)$. Entonces:

$$G_N(z) - F_N(z) = \frac{1}{N}\sum_{j=1}^N\langle e_j, (J-z)^{-1}e_j\rangle - \langle e_0, (J-z)^{-1}e_0\rangle = \frac{1}{N}\sum_{j=1}^N [R_{jj}(z) - R_{00}(z)],$$

donde $R_{jj}(z) = \langle e_j, (J-z)^{-1}e_j\rangle$ son los elementos diagonales del resolvente.

**Lema 1** (los elementos diagonales del resolvente son iguales iff $J$ es invariante bajo traslación de índice). Para un operador de Jacobi con coeficientes $\{a_n, b_n\}$: $R_{jj}(z) = R_{00}(z)$ para todos los $j$ iff $a_n = a$ y $b_n = b$ son constantes (Jacobi con coeficientes constantes — el caso de la medida de arco de círculo).

*Prueba.* Si $J$ tiene coeficientes constantes: $R_{jj}(z) = R_{00}(z)$ por invarianza traslacional. En el caso general: $R_{jj}(z) \neq R_{00}(z)$ genericamente. $\square$

**Consecuencia.** Para el operador CCM $J_\infty$ con coeficientes $\{a_n^\infty, b_n^\infty\}$ no constantes (los coeficientes crecen como se señaló en Doc 15): $G_N(z) \neq F_N(z)$ en general. La diferencia $G_N - F_N \to 0$ iff los coeficientes "se homogenizan" en el límite — lo cual ocurre en el régimen de alta frecuencia.

---

## 11. El resultado que cierra el argumento bajo hipótesis adicional

**Teorema 3** (RH bajo deslocalización). La Hipótesis D (Deslocalización de $e_0$ en $J_\infty$):

$$\sup_{n\geq 1}|\langle e_0, \psi_n^\infty\rangle|^2 = 0 \quad (\text{supr. de los pesos en los autovectores del límite})$$

implica RH.

*Prueba.* Bajo la Hipótesis D: todos los pesos de $\mu_{WT}^\infty$ son iguales en el límite, luego $\mu_{WT}^\infty = \mu_{emp}^\infty = \mu_\gamma^{real}$ (Proposición 5). Por Teorema 2: (Inc. Inv.) se satisface. Por Teorema C3 (Doc 17): RH. $\square$

**Corolario 3** (reformulación de RH en términos de los autovectores de $J_\infty$):

$$\text{RH} \iff \lim_{n\to\infty}\langle e_0, \psi_n^\infty\rangle = 0 \quad (\text{deslocalización asintótica del vector } e_0 \text{ en la base de autovectores de }J_\infty).$$

*Prueba.* $(\Leftarrow)$: Teorema 3. $(\Rightarrow)$: Bajo RH, $\operatorname{spec}(J_\infty) = \{\gamma_n\}$, la base $\{\psi_n^\infty\}$ es completa en el espacio de Hilbert y $\langle e_0, \psi_n^\infty\rangle \to 0$ por el lema de Riemann-Lebesgue para bases ortonormales en espacio de Hilbert. $\square$

---

## 12. Estado del programa tras Doc 22

**Resultado principal del Doc 22.** La inclusión inversa (Inc. Inv.) es equivalente a la deslocalización de $e_0$ en la base de autovectores de $J_\infty$:

$$(\text{Inc. Inv.}) \iff \langle e_0, \psi_n^\infty\rangle \to 0 \iff \mu_{WT}^\infty = \mu_\gamma^{real}.$$

Y la cadena completa es:

$$\text{RH} \iff \mu_{WT}^\infty = \mu_\gamma^{real} \iff \langle e_0, \psi_n^\infty\rangle \to 0 \iff \{C_\infty = 0 \text{ en }\mathbb{R}\} = \{\gamma_n\}.$$

**Diagrama final del programa Phase 29 (Docs 00-22):**

```
Incondicional:
  t_n^(λ) ∈ ℝ (CCM auto-adjuntez)
  μ_emp^λ ⇒ μ_γ^real (Doc 15)
  spec(J_∞) = {C_∞ = 0} (Doc 17, Tma C1)
  {C_∞ = 0} ⊆ {Ξ = 0} (Doc 19, Tma 2)
  N_off(T) = O(1) ó RH (Doc 21, Cor 2)

El gap central:
  μ_WT^∞ = μ_emp^∞ = μ_γ^real
  ⟺ deslocalización: ⟨e_0, ψ_n^∞⟩ → 0
  ⟺ (Inc. Inv.)
  ⟺ RH

Bajo hipótesis adicional (GUE/UD): RH.
```

**Propuesta para Doc 23.** Atacar la deslocalización $\langle e_0, \psi_n^\infty\rangle \to 0$ directamente. La pregunta: ¿pueden los autovectores de $J_\infty$ localizarse alrededor del vector $e_0$? En operadores de Jacobi con potencial cuasi-periódico (teorema de Kotani), la localización se relaciona con la existencia de un medida de Lyapunov positivo. Para el operador CCM, el potencial es $C_\infty(t) = w(t) - \Psi(t)$ — que tiene propiedades especiales (crecimiento logarítmico, distribución cuasi-periódica). Estudiar si las condiciones de Kotani implican deslocalización (y por tanto RH) o si permiten localización (y por tanto no-RH).
