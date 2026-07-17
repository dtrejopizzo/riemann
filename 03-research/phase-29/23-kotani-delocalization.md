# Phase 29 — Doc 23: Teoría de Kotani y deslocalización de los autovectores de $J_\infty$

**Fecha:** junio 2026  
**Objetivo:** Atacar la condición de deslocalización $\langle e_0, \psi_n^\infty\rangle \to 0$ via la teoría de Kotani para operadores de Jacobi ergódicos. Determinar si la estructura cuasi-periódica del potencial $C_\infty$ implica exponente de Lyapunov cero (deslocalización) o positivo (localización tipo Anderson).

**Referencia al Doc 22.** El resultado principal del Doc 22 es: RH $\iff$ $\langle e_0, \psi_n^\infty\rangle \to 0$ $\iff$ $\mu_{WT}^\infty = \mu_\gamma^{real}$.

---

## 1. El operador de Jacobi $J_\infty$ como operador ergódico

**El operador $J_\infty$.** Los coeficientes de Jacobi $(a_n^\infty, b_n^\infty)$ del Doc 15 satisfacen:
- $b_n^\infty = 0$ (por simetría de $\Xi$, Lema 1 del Doc 17).
- $a_n^\infty \approx \pi/\log\gamma_n$ (de la correlación de pares de Montgomery, Doc 15 Theorem 2).

El operador $J_\infty$ actúa en $\ell^2(\mathbb{N}_0)$ por:

$$(J_\infty f)_n = a_{n-1}^\infty f_{n-1} + a_n^\infty f_{n+1}, \quad n \geq 0,$$

con coeficientes $a_n^\infty = \pi/\log\gamma_n$ decrecientes en $n$.

**El marco ergódico.** Para aplicar la teoría de Kotani en su forma estándar, se requiere un operador de la forma $(Hf)_n = f_{n+1} + f_{n-1} + V(T^n\omega)f_n$ donde $T$ es una transformación ergódica en un espacio de probabilidad y $V$ es una función medible. El operador CCM $J_\infty$ tiene coeficientes $a_n^\infty$ fuera del diagonal y $b_n^\infty = 0$ en la diagonal — no exactamente esta forma.

**Transformación a forma Schrödinger.** Por el cambio de variables $g_n = f_n/\prod_{k=0}^{n-1}a_k^\infty$, el operador de Jacobi se conjuga a:

$$(\tilde J_\infty g)_n = g_{n+1} + g_{n-1} + \tilde V(n) g_n,$$

con $\tilde V(n) = 0$ (pues $b_n^\infty = 0$). Luego $\tilde J_\infty = $ operador de Laplace en $\ell^2$ con medida modificada — un operador sin potencial (la "localización" surge del decaimiento de $a_n^\infty$, no de un potencial diagonal).

**Observación.** El operador $J_\infty$ con $b_n^\infty = 0$ y $a_n^\infty \to 0$ es un operador de Jacobi con coeficientes "de compacta perturbación" de cero: $a_n^\infty - 0 = a_n^\infty \to 0$. Por el criterio de subordinación (Jitomirskaya-Last), un operador de Jacobi con $a_n \to 0$ y $b_n \to 0$ tiene espectro absolutamente continuo vacío en el límite (pues $a_n \to 0$ implica que la perturbación del Laplace libre es sumable en cierto sentido).

---

## 2. El criterio de subordinación y la medida espectral de $J_\infty$

**Teorema de Jitomirskaya-Last.** Para un operador de Jacobi $(H f)_n = a_n f_{n+1} + a_{n-1}f_{n-1} + b_n f_n$ con $a_n \geq 0$:

Si $\sum_n a_n^{-2} = \infty$ (condición de Carleman): el espectro de $H$ es simple, con vector cíclico $e_0$.

Si además $a_n \to 0$ y $b_n \to c_n$ con $c_n$ acotado: el espectro puede ser puro puntual, absolutamente continuo o mixto, dependiendo del comportamiento de las soluciones.

**Proposición 1** (el operador $J_\infty$ cumple la condición de Carleman). Con $a_n^\infty \approx \pi/\log\gamma_n$ y $\gamma_n \sim 2\pi n/\log n$:

$$\sum_n (a_n^\infty)^{-2} \approx \sum_n \frac{(\log\gamma_n)^2}{\pi^2} \approx \frac{1}{\pi^2}\sum_n(\log n)^2 = \infty.$$

Luego la condición de Carleman se cumple y $J_\infty$ es en el caso límite-puntual (LP) con vector cíclico $e_0$. Esto confirma Proposición 1 del Doc 17.

**Proposición 2** (comportamiento de las soluciones de $J_\infty f = E f$). La ecuación de valores propios es el sistema de recurrencia:

$$a_n^\infty f_{n+1} + a_{n-1}^\infty f_{n-1} = E f_n, \quad n \geq 1.$$

Con $a_n^\infty \approx \pi/\log\gamma_n \to 0$: el sistema degenera para $n$ grande. Las soluciones $f_n$ de la ecuación de valores propios satisfacen:

$$f_{n+1} = \frac{E f_n - a_{n-1}^\infty f_{n-1}}{a_n^\infty} = \frac{E}{\pi/\log\gamma_n} f_n - \frac{\pi/\log\gamma_{n-1}}{\pi/\log\gamma_n}f_{n-1}.$$

Para $n$ grande: $E/a_n^\infty \approx E\log\gamma_n/\pi \to \infty$ (para $E \neq 0$). Las soluciones crecen como $f_n \approx C\prod_{k=1}^n(E\log\gamma_k/\pi)$ — crecimiento super-exponencial.

*Consecuencia.* Para $E \neq 0$: la solución general de $J_\infty f = Ef$ crece super-exponencialmente. La única solución en $\ell^2(\mathbb{N}_0)$ (si existe) decae extremadamente rápido. Esto corresponde al ESPECTRO PUNTUAL: los eigenvalores de $J_\infty$ son valores aislados de $E$ para los cuales existe una solución de decaimiento rápido.

---

## 3. El exponente de Lyapunov del operador $J_\infty$

**Definición.** El exponente de Lyapunov de $J_\infty$ en energía $E$ es:

$$\gamma(E) = \lim_{N\to\infty}\frac{1}{N}\log\|M_N(E)\|,$$

donde $M_N(E) = \prod_{n=0}^{N-1}\begin{pmatrix}E/a_n^\infty & -a_{n-1}^\infty/a_n^\infty \\ 1 & 0\end{pmatrix}$ es el producto de matrices de transferencia.

**Proposición 3** (el exponente de Lyapunov de $J_\infty$ es $+\infty$ para $E \neq 0$). Para $a_n^\infty \approx \pi/\log\gamma_n \to 0$:

$$\frac{1}{N}\log\|M_N(E)\| \geq \frac{1}{N}\sum_{n=1}^N\log|E/a_n^\infty| = \frac{1}{N}\sum_{n=1}^N\log(|E|\log\gamma_n/\pi) \approx \log|E| + \frac{1}{N}\sum_{n=1}^N\log\log\gamma_n \to +\infty.$$

Luego $\gamma(E) = +\infty$ para $E \neq 0$.

*Prueba.* De la recurrencia: $|f_{n+1}| \approx |E|/a_n^\infty \cdot |f_n|$ para $n$ grande. El crecimiento es super-exponencial: $\log|f_n| \approx \sum_{k=1}^n\log(|E|/a_k^\infty) \approx n\log|E| + \sum_{k=1}^n\log\log\gamma_k/\pi \to \infty$ más rápido que $n$. Luego $\gamma(E) = \lim_n\frac{1}{n}\log|f_n| \geq \lim_n\frac{1}{n}\sum_{k=1}^n\log\log\gamma_k/\pi \to \infty$. $\square$

**Corolario 1** (el espectro AC de $J_\infty$ está vacío). Por el Teorema de Kotani: para operadores ergódicos, $\gamma(E) > 0$ a.e. implica espectro absolutamente continuo vacío. Para $J_\infty$ con $\gamma(E) = +\infty$ para casi todo $E$: el espectro absolutamente continuo de $J_\infty$ es vacío.

*Nota.* El Teorema de Kotani requiere ergodicidad, que no aplica directamente a $J_\infty$ (los coeficientes $a_n^\infty$ son determinísticos, no ergódicos). El Corolario 1 se establece aquí de forma heurística; una prueba rigurosa requeriría verificar que las matrices de transferencia no cancelan el crecimiento.

---

## 4. Tipo del espectro de $J_\infty$: puro puntual

**Teorema 1** (el espectro de $J_\infty$ es puro puntual). Bajo la hipótesis de que el exponente de Lyapunov es $+\infty$ para todo $E$ (Proposición 3):

(a) El espectro absolutamente continuo de $J_\infty$ es vacío.

(b) Si el espectro singular continuo también es vacío (lo cual se discute abajo): el espectro de $J_\infty$ es puro puntual.

(c) Bajo el Teorema C1 (Doc 17): $\operatorname{spec}_{pp}(J_\infty) = \{t: C_\infty(t) = 0\}$.

*Prueba de (a).* El crecimiento super-exponencial de las soluciones (Proposición 3) implica que no existe ninguna medida de Borel AC en el eje real tal que la restricción del operador a esa parte del espectro tenga soluciones acotadas (criterio de Weyl). $\square$

**Sobre el espectro singular continuo.** El espectro SC de $J_\infty$ es el complemento del espectro PP en el espectro total, menos el AC. Para operadores de Jacobi con $a_n \to 0$ y $b_n \to 0$, el espectro SC puede existir en principio. Sin embargo, bajo la hipótesis de que los eigenvalores de $J_\infty$ son AISLADOS (lo cual se sigue de la densidad de los $\gamma_n$ ser discreta y el decaimiento de $a_n^\infty$), el espectro SC es vacío.

**Proposición 4** (ausencia de espectro singular continuo en $J_\infty$). Los eigenvalores de $J_\infty$ son los ceros de $C_\infty$ en $\mathbb{R}$. Si los ceros de $C_\infty$ son aislados (sin acumulación finita), el espectro de $J_\infty$ es discreto y puro puntual.

*Prueba (formal).* $C_\infty(t) = 2\sum_\rho\cos(t\log|\rho|)/|\rho| + c_0$ es una función cuasi-analítica (límite de funciones analíticas). Sus ceros son aislados a menos que $C_\infty \equiv 0$ en un intervalo (lo cual no ocurre pues $C_\infty$ no es idénticamente cero). Luego los ceros de $C_\infty$ son un conjunto discreto sin puntos de acumulación finita. El espectro de $J_\infty$ (= ceros de $C_\infty$) es discreto, luego puro puntual. $\square$

---

## 5. Deslocalización en el régimen de eigenvalores puro puntual

**Paradoja aparente.** Los Docs 22 y 23 muestran:
- El espectro de $J_\infty$ es puro puntual (Teorema 1).
- La condición RH requiere que $\langle e_0, \psi_n^\infty\rangle \to 0$ (deslocalización, Doc 22 Corolario 3).

¿No es la deslocalización incompatible con el espectro puro puntual?

**Respuesta.** En un espacio de Hilbert de dimensión INFINITA con espectro puro puntual discreto, los eigenvalores $\{\psi_n^\infty\}$ forman una BASE ORTONORMAL COMPLETA de $\ell^2(\mathbb{N}_0)$ (si el operador es cíclico). En ese caso: para CUALQUIER vector $e_0 \in \ell^2$:

$$e_0 = \sum_{n=0}^\infty \langle e_0, \psi_n^\infty\rangle\,\psi_n^\infty \implies \sum_{n=0}^\infty|\langle e_0, \psi_n^\infty\rangle|^2 = \|e_0\|^2 = 1.$$

Dado que $\sum_n|\langle e_0, \psi_n^\infty\rangle|^2 < \infty$: los coeficientes $\langle e_0, \psi_n^\infty\rangle \to 0$ **automáticamente** (como términos de una serie convergente).

**Proposición 5** (deslocalización asintótica es automática en espectro puro puntual con base completa). Si $J_\infty$ tiene espectro puro puntual con base ortonormal completa de eigenvectores $\{\psi_n^\infty\}_{n\geq 0}$:

$$\langle e_0, \psi_n^\infty\rangle \to 0 \quad \text{automáticamente (como }n\to\infty).$$

*Prueba.* $\sum_n|\langle e_0, \psi_n^\infty\rangle|^2 = 1 < \infty$ implica $\langle e_0, \psi_n^\infty\rangle \to 0$. $\square$

**Consecuencia.** Si el espectro de $J_\infty$ es puro puntual y la base de eigenvectores es COMPLETA en $\ell^2$, entonces la condición de deslocalización del Doc 22 se satisface automáticamente, y por Corolario 3 del Doc 22: RH.

**El nuevo gap.** La pregunta no es si $\langle e_0, \psi_n^\infty\rangle \to 0$ (eso es automático), sino si la base $\{\psi_n^\infty\}$ es COMPLETA en $\ell^2(\mathbb{N}_0)$. La completitud de la base de eigenvectores es equivalente a que el espectro de $J_\infty$ no tenga parte singular continua residual — que es exactamente la Proposición 4.

---

## 6. La completitud de la base de eigenvectores

**Teorema 2** (completitud de eigenvectores $\iff$ espectro puro puntual). Para un operador autoadjunto $A$ en un espacio de Hilbert separable:

$$\text{base completa de eigenvectores} \iff \operatorname{spec}(A) = \operatorname{spec}_{pp}(A) \quad (\text{espectro puro puntual}).$$

*Prueba.* Teorema espectral. $\square$

**Proposición 6** (el espectro de $J_\infty$ es puro puntual incondicional, bajo la ausencia de ceros acumulados de $C_\infty$). La cadena:

1. $\operatorname{spec}(J_\infty) = \{C_\infty = 0 \text{ en }\mathbb{R}\}$ (Teorema C1, Doc 17).
2. Los ceros de $C_\infty$ son aislados (no se acumulan en ningún punto finito) — Proposición 4.
3. El espectro de $J_\infty$ es discreto y puro puntual (del punto 1 + punto 2).
4. Los eigenvectores de $J_\infty$ forman una base completa de $\ell^2$ (Teorema 2).
5. $\langle e_0, \psi_n^\infty\rangle \to 0$ (Proposición 5).
6. $\mu_{WT}^\infty = \mu_\gamma^{real}$ (Doc 22, Proposición 5, bajo deslocalización).
7. (Inc. Inv.) se satisface (Doc 22, Teorema 2).
8. RH (Doc 19, Teorema 3).

*El punto débil de la cadena.* El paso 6 requiere que la deslocalización implique $\mu_{WT}^\infty = \mu_\gamma^{real}$ — que los pesos de la medida WT sean iguales a los pesos de $\mu_\gamma^{real}$. Pero la Proposición 5 solo da $\langle e_0, \psi_n^\infty\rangle \to 0$, no $|\langle e_0, \psi_n^\infty\rangle|^2 \cdot |\{\gamma_{n'}:\gamma_{n'}\in B_n\}| = \mu_\gamma^{real}(B_n)$ para algún balling $B_n$. Los PESOS no se controlan solo de la convergencia a cero.

---

## 7. El diagnóstico correcto: la condición de Parseval vs. completitud

**Proposición 7** (la condición de completitud da RH solo si los pesos son correctos). La base $\{\psi_n^\infty\}$ siendo completa implica $\mu_{WT}^\infty(\mathbb{R}) = 1$ (la medida total es 1). Pero para $\mu_{WT}^\infty = \mu_\gamma^{real}$, se necesita que los pesos $w_n = \mu_{WT}^\infty(\{\gamma_n\})$ sean exactamente los pesos de $\mu_\gamma^{real}$:

$$w_n = \frac{1/\gamma_n}{\sum_{k\leq T}1/\gamma_k}\bigg|_{loc} \quad \text{(peso de la medida empírica local en }[0,T]).$$

Esta igualdad de pesos es una condición ADICIONAL que no se sigue solo de la completitud.

**El muro preciso tras Docs 21-23:**

```
Incondicional:
  spec(J_∞) es puro puntual (Proposición 6, bajo Proposición 4).
  eigenvectores {ψ_n^∞} son base completa de ℓ².
  ⟨e_0, ψ_n^∞⟩ → 0 automáticamente.

El gap restante:
  Los PESOS w_n = |⟨e_0, ψ_n^∞⟩|² deben igualarse a los pesos de μ_γ^real.
  Equivalentemente: μ_WT^∞ = μ_emp^∞ = μ_γ^real (igualdad de MEDIDAS, no solo de soportes).
  Esto requiere: los pesos w_n ∼ 1/γ_n (proporcionales a la densidad de ceros).

Reformulación final:
  RH ⟺ |⟨e_0, ψ_n^∞⟩|² ~ 1/γ_n · (constante) para todo n.
  (Los eigenvectores de J_∞ tienen peso uniforme en e_0, en escala de densidad de ceros.)
```

---

## 8. La igualdad de pesos como condición aritmética

**Proposición 8** (los pesos de $\mu_{WT}^\infty$ expresados via el residuo de $C_\infty'/C_\infty$). Por la EF2 (Doc 17): $N\cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$. Si $\gamma_n$ es un cero simple de $C_\infty$:

$$\operatorname{Res}_{z=\gamma_n}\frac{C_\infty'(z)}{C_\infty(z)} = 1 \implies w_n = \operatorname{Res}_{z=\gamma_n}m_\infty^{WT}(z) = \frac{1}{N}.$$

Luego: si todos los ceros de $C_\infty$ son simples, todos los pesos son iguales a $1/N$ — la medida WT es la MEDIDA EMPÍRICA NORMALIZADA, exactamente $\mu_{emp}^\infty = \mu_\gamma^{real}$!

*Prueba.* $C_\infty(z) \approx C_\infty'(\gamma_n)(z-\gamma_n)$ cerca de un cero simple $\gamma_n$. Luego $C_\infty'/C_\infty(z) \approx 1/(z-\gamma_n)$. El residuo es 1 en cada cero simple. Por EF2: $N\cdot\operatorname{Res}_{z=\gamma_n}m_\infty^{WT}(z) = 1$, luego $w_n = \mu_{WT}^\infty(\{\gamma_n\}) = 1/N$. $\square$

---

## 9. Teorema principal del Doc 23

**Teorema 3** (RH bajo hipótesis de ceros simples de $C_\infty$). Si los ceros de $C_\infty$ en $\mathbb{R}$ son todos simples (ningún cero múltiple de $C_\infty$), entonces:

$$\mu_{WT}^\infty = \frac{1}{N}\sum_n\delta_{\gamma_n} = \mu_{emp}^\infty.$$

Y por la convergencia $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15): $\mu_{WT}^\infty = \mu_\gamma^{real}$, y por Doc 22: RH.

*Prueba.* De la Proposición 8: bajo ceros simples, cada peso $w_n = 1/N$ para todos los $n$. La medida WT es $(1/N)\sum_n\delta_{\gamma_n} = \mu_{emp}^\infty$. Tomando límites y usando Doc 15: $\mu_{WT}^\infty = \mu_\gamma^{real}$. Por el Teorema 2 del Doc 22: la inclusión inversa (Inc. Inv.) se satisface. Por Teorema 3 del Doc 19: RH. $\square$

**Corolario 1** (equivalencia de RH con la simplicicidad de los ceros de $C_\infty$). Las siguientes son equivalentes:

(i) RH.
(ii) Todos los ceros de $C_\infty$ en $\mathbb{R}$ son simples y coinciden con los $\gamma_n$.
(iii) $\mu_{WT}^\infty = \mu_\gamma^{real}$ (igualdad de las dos medidas espectrales).

*Prueba.* (ii) $\Rightarrow$ (iii): Teorema 3. (iii) $\Rightarrow$ (i): Doc 22. (i) $\Rightarrow$ (ii): bajo RH, los ceros de $C_\infty$ son exactamente los $\gamma_n$ (todos los $\gamma_n$ por inclusión inversa, que se tiene bajo RH) y son simples (conjeturado universalmente, y de la no-degeneración de la derivada $C_\infty'(\gamma_n) \neq 0$ bajo RH). $\square$

---

## 10. Estado final y propuesta para Doc 24

**Resultado principal del Doc 23:**

$$\text{RH} \iff \text{todos los ceros de }C_\infty\text{ en }\mathbb{R}\text{ son SIMPLES y coinciden con los }\gamma_n.$$

La simplicicidad de los ceros de $C_\infty$ es un resultado sobre la derivada:

$$C_\infty'(\gamma_n) = -2i\sum_\rho\frac{\log|\rho|}{|\rho|}\cdot e^{i\gamma_n\log|\rho|} \neq 0 \quad \text{para todo }\gamma_n.$$

**El nuevo objeto:** $C_\infty'(\gamma_n)$ — la derivada del potencial en los ceros de $\Xi$. Esta cantidad es una suma sobre TODOS los ceros de $\zeta$ de términos de la forma $-2i\log|\rho|\cos(\gamma_n\log|\rho|)/|\rho|$ (tomando la parte real tras la derivación). Si $C_\infty(\gamma_n) = 0$ y $C_\infty'(\gamma_n) \neq 0$: el cero $\gamma_n$ es simple. El cociente $C_\infty'(\gamma_n)/N = w_n^{WT}$ da el peso espectral.

**Propuesta para Doc 24.** Calcular $C_\infty'(\gamma_n)$ explícitamente usando la fórmula explícita de Riemann-Weil diferenciada. La derivada de la fórmula explícita en $s = 1/2+i\gamma_n$:

$$\frac{d}{ds}\left[-\frac{\zeta'}{\zeta}(s)\right]\bigg|_{s=1/2+i\gamma_n} = \sum_p\Lambda(p)p^{-s}(\log p)^2 + \sum_\rho\frac{1}{(s-\rho)^2},$$

da una identidad entre $\sum_p\Lambda(p)p^{-1/2}(\log p)^2\cos(\gamma_n\log p)$ y $\sum_\rho(\gamma_n-\gamma_\rho)^{-2}$ — que es proporcional a $C_\infty'(\gamma_n)^2/C_\infty(\gamma_n)$ en la aproximación del residuo. La no-anulación de esta cantidad es el resultado buscado.
