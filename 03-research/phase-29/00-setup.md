# Phase 29 — Zeta Spectral Triples: Setup preciso

**Fecha:** junio 2026  
**Basado en:** Connes–Consani–Moscovici arXiv:2511.22755 (2025); Connes arXiv:2602.04022 (2026); Connes–Moscovici arXiv:2112.05500 (PNAS 2022).  
**Diferencia fundamental respecto a todos los enfoques previos:** los operadores son auto-adjuntos POR CONSTRUCCIÓN (vía Carathéodory–Fejér). No hay que probar positividad de una forma cuadrática. El único obstáculo es la convergencia de operadores.

---

## 1. El problema exacto a resolver

Sea $\Xi(t) = \xi(1/2+it)$ la función entera real de Riemann, con
$$\Xi(t) = \int_0^\infty k(u)\, u^{it}\, d^*u, \quad k(u) = u^{1/2}\sum_{n=1}^\infty h(nu),$$
donde $h(u) = \frac{1}{2}(2\pi^2 u^4 - 3\pi u^2)e^{-\pi u^2}$ y $d^*u = du/u$.

La Hipótesis de Riemann equivale a que todos los ceros de $\Xi$ son reales.

Connes–Consani–Moscovici (2025) construyen una familia de funciones enteras $\hat\xi_{\lambda,N}(z)$, **todos cuyos ceros son reales por construcción**, y conjeturan que
$$\hat\xi_{\lambda,N}(z)\cdot C_{\lambda,N} e^{a_{\lambda,N} + ib_{\lambda,N} z} \longrightarrow \Xi(z)$$
uniformemente en compactos de la franja $|\Im(z)| < 1/2$, cuando $N,\lambda \to \infty$.

Por el **Teorema de Hurwitz**: si la convergencia vale, $\Xi$ tiene todos sus ceros en $\mathbb{R}$, i.e., RH.

---

## 2. La forma cuadrática de Weil semilocal

**Definición 1.** Para $\lambda > 1$, el espacio de Hilbert es $\mathcal{H}_\lambda := L^2([\lambda^{-1},\lambda], d^*u)$ con la base ortonormal
$$V_n(u) := L^{-1/2}\exp\!\left(\frac{2\pi i n \log(\lambda u)}{L}\right), \quad L := 2\log\lambda, \quad n \in \mathbb{Z}.$$

La **transformada de Fourier multiplicativa** es:
$$\hat f(z) := \int_{\lambda^{-1}}^\lambda f(u)\, u^{-iz}\, d^*u = L^{-1/2}\sum_n \hat f_n \cdot \frac{\sin((z-2\pi n/L)\cdot L/2)}{z - 2\pi n/L}$$
para $f = \sum_n f_n V_n$.

**Definición 2** (Forma de Weil semilocal). La forma cuadrática de Weil semilocal es:
$$QW_\lambda(f,f) := \underbrace{\int_{\mathbb{R}} |\hat f(t)|^2 \frac{2\partial_t\theta(t)}{2\pi}\,dt}_{=:\, Q^{\mathrm{arch}}(f)} + \underbrace{2\hat f\!\left(\tfrac{i}{2}\right)\hat f\!\left(-\tfrac{i}{2}\right)}_{=:\, Q^{\mathrm{cross}}(f)} - \underbrace{\sum_{1 < n \leq \lambda^2} \Lambda(n)\,\langle f \mid T(n)f\rangle}_{=:\, Q^{\mathrm{arith}}(f,\lambda)},$$
donde:
- $\theta(t) = \Im\log\Gamma(1/4+it/2) - (t/2)\log\pi$ es la función angular de Riemann-Siegel, con $\partial_t\theta(t) \sim \frac{1}{2}\log(t/2\pi)$ para $t \gg 1$.
- $\Lambda(n)$ es la función de von Mangoldt.
- $T(n)$ es el operador auto-adjunto acotado en $\mathcal{H}_\lambda$ con
$$\langle f \mid T(n) f\rangle = n^{-1/2}\left[(f^* * f)(n) + (f^* * f)(n^{-1})\right],$$
con convolución multiplicativa $(f^* * g)(n) = \int f(u^{-1})g(nu)\,d^*u$.

**Proposición 1** (estructura matricial). En la base $\{V_n\}_{|n|\leq N}$, la matrix de $QW_\lambda^N$ (la restricción a $E_N = \operatorname{span}\{V_n : |n|\leq N\}$) tiene la forma:
$$\tau_{n,n} = a_n \in \mathbb{R}, \quad \tau_{n,m} = \frac{b_n - b_m}{n-m} \text{ para } n\neq m,$$
con $a_{-n} = a_n$ y $b_{-n} = -b_n$ (i.e., $\{a_n\}$ es par y $\{b_n\}$ es impar). Esta es la estructura de **Cauchy–Toeplitz** clave para el teorema de Carathéodory–Fejér.

---

## 3. La involución de simetría y los subespacios par/impar

La **involución funcional** $\gamma: \mathcal{H}_\lambda \to \mathcal{H}_\lambda$ definida por $\gamma(f)(u) := f(u^{-1})$ satisface $\gamma^2 = \operatorname{id}$. En la base: $\gamma(V_n) = V_{-n}$ (ya que $V_n(u^{-1}) = e^{-2\pi i n\log(\lambda u)/L}\cdot e^{2\cdot 2\pi i n \log\lambda/L}$... más precisamente: $V_n(u^{-1}) = L^{-1/2}e^{2\pi in\log(\lambda/u)/L} = L^{-1/2}e^{-2\pi in\log(\lambda u)/L} \cdot e^{4\pi in\log\lambda/L}$. Con $L = 2\log\lambda$: $= L^{-1/2}e^{-2\pi in\log(\lambda u)/L} \cdot e^{2\pi in} = V_{-n}(u)$).

Por tanto: $\gamma(V_n) = V_{-n}$.

**Subespacios:**
$$E_N^+ := \{f \in E_N : \gamma f = f\} = \operatorname{span}\{U_n^+ : 0 \leq n \leq N\}, \quad U_0^+ := V_0,\ U_n^+ := (V_n+V_{-n})/\sqrt{2}\ (n\geq 1)$$
$$E_N^- := \{f \in E_N : \gamma f = -f\} = \operatorname{span}\{U_n^- : 1 \leq n \leq N\}, \quad U_n^- := (V_n-V_{-n})/\sqrt{2}$$

**Proposición 2** (la forma respeta la involución). La forma $QW_\lambda^N$ preserva $E_N^\pm$, i.e., $QW_\lambda^N(f^+, f^-) = 0$ para $f^\pm \in E_N^\pm$. Por tanto:
$$QW_\lambda^N = QW_\lambda^{N,+}\!\oplus\, QW_\lambda^{N,-}$$
como formas cuadráticas en $E_N^+ \oplus E_N^-$.

*Prueba.* Cada componente $Q^{\mathrm{arch}}$, $Q^{\mathrm{cross}}$, $Q^{\mathrm{arith}}$ es $\gamma$-invariante. Para $Q^{\mathrm{arch}}$: $\hat{\gamma f}(t) = \overline{\hat f(t)}$ para la transformada aditiva de Fourier en $\mathbb{R}$; para la multiplicativa: $\widehat{\gamma f}(z) = \hat f(-z)$ (por la sustitución $u\mapsto u^{-1}$). Para $Q^{\mathrm{cross}}$: depende de $\hat f(i/2)\hat f(-i/2)$ que es simétrico bajo $f\mapsto\gamma f$. Para $T(n)$: si $f$ es par/impar, $T(n)f$ también lo es. $\square$

---

## 4. El operador de escalado y la perturbación rango-uno

**Definición 3** (operador de escalado). El operador de escalado con condiciones periódicas de frontera:
$$D_{\log}^{(\lambda)} := -iu\frac{\partial}{\partial u}: \mathcal{H}_\lambda \to \mathcal{H}_\lambda$$
con valores propios $\mu_n = 2\pi n/L$ ($n \in \mathbb{Z}$) y vectores propios $V_n$. Es auto-adjunto en $\mathcal{H}_\lambda$.

**El funcional de evaluación** en $u = \lambda$:
$$\delta_N(f) := \langle f, \delta_N\rangle = \frac{1}{\sqrt{L}}\sum_{|n|\leq N} f_n, \quad \|\delta_N\|^2 = \frac{2N+1}{L}.$$

**Hipótesis par-simple** (ES). $QW_\lambda^N$ tiene su eigenvalor mínimo $\epsilon_{\lambda,N}$ en $E_N^+$, con multiplicidad 1. Se llama el eigenvector correspondiente (normalizado por $\delta_N(\xi)=1$) el **minimizador**.

**Definición 4** (operador perturbado). Bajo (ES), el minimizador $\xi = \xi_{\lambda,N} \in E_N^+$ define:
$$D_{\log}^{(\lambda,N)} := D_{\log}^{(\lambda)}\bigg|_{E_N} - \big|D_{\log}^{(\lambda)}\xi\big\rangle\big\langle\delta_N\big|.$$

---

## 5. El Teorema principal (Connes–Consani–Moscovici)

**Teorema CCM** (Teorema 5.10 / Teorema 1.1 de arXiv:2511.22755). Bajo (ES):

**(i) Auto-adjuntez por construcción.** $D_{\log}^{(\lambda,N)}$ es auto-adjunto en el espacio de Hilbert $(E_N/\mathbb{C}\xi,\, \langle\cdot|\cdot\rangle_T)$, donde el producto interno es
$$\langle f,g\rangle_T := (QW_\lambda^N - \epsilon_{\lambda,N}\langle\cdot|\cdot\rangle)(f,g) \quad (f,g \in E_N/\mathbb{C}\xi).$$

**(ii) Determinante regularizado.** El determinante regularizado (vía función zeta espectral) satisface:
$$\det_{\mathrm{reg}}\!\left(D_{\log}^{(\lambda,N)} - z\right) = -i\lambda^{-iz}\,\hat\xi_{\lambda,N}(z),$$
donde $\hat\xi_{\lambda,N}(z) = \int_{\lambda^{-1}}^\lambda \xi_{\lambda,N}(u)\,u^{-iz}\,d^*u$ es una función entera.

**(iii) Espectro = ceros reales de $\hat\xi$.** La función $\hat\xi_{\lambda,N}(z)$ es entera, todos sus ceros son reales, y el espectro de $D_{\log}^{(\lambda,N)}$ coincide exactamente con el conjunto de ceros de $\hat\xi_{\lambda,N}$.

**Corolario** (auto-adjuntez ↔ ceros reales). Los eigenvalores de $D_{\log}^{(\lambda,N)}$ son todos reales. Por tanto, los "ceros aproximados de $\Xi$" producidos por este operador **siempre están en la recta crítica**, para todo $\lambda, N$.

*Mecanismo:* La estructura de Cauchy–Toeplitz de la matriz $\tau_{n,m}$ implica que $[D, T] = |\beta\rangle\langle\eta| - |\eta\rangle\langle\beta|$ (rango 2). La perturbación rango-uno $D' = D - |D\xi\rangle\langle\eta|$ se auto-adjuntiza en $(E_N/\ker T, \langle\cdot|\cdot\rangle_T)$ por la identidad de Sylvester para conmutadores.

---

## 6. El Lema de convergencia (probado por Connes et al.)

**Lema 7.3** (Connes–Consani–Moscovici). Sea $k_\lambda = E(h_\lambda)$ donde $h_\lambda$ es la única combinación lineal de las funciones de onda esferoidales prolatas $h_{0,\lambda}, h_{4,\lambda}$ con integral nula. Entonces:
$$\hat k_\lambda(z) \longrightarrow \Xi(z) \quad \text{uniformemente en compactos de } |\Im(z)| < \frac{1}{2},$$
con tasa:
$$\left|\hat k_\lambda(z) - \Xi(z)\right| \leq C_\alpha \lambda^{-1/2-\alpha}(1-2\alpha)^{-1} \quad \text{para } |\Im(z)| \leq \alpha < \frac{1}{2}.$$

**Condición de convergencia global (Phase 29, Objetivo).** Probar:
$$\hat\xi_{\lambda,N}(z)\cdot C_{\lambda,N} e^{a_{\lambda,N}+ib_{\lambda,N}z} \longrightarrow \Xi(z)$$
en compactos de $|\Im(z)| < 1/2$. Por el Lema 7.3, esto se reduce a probar:
$$\hat\xi_{\lambda,N}(z) \sim C\,\hat k_\lambda(z) \text{ (en el sentido de la convergencia uniforme local)}.$$

---

## 7. Las dos hipótesis abiertas y el programa de Phase 29

| Hipótesis | Enunciado preciso | Estado |
|---|---|---|
| **H1 (par-simple)** | $QW_\lambda^N$ tiene eigenvalor mínimo simple y par para todo $\lambda\geq\sqrt{2}, N\geq 1$ | Abierto; verificado numéricamente |
| **H2 (convergencia)** | $\hat\xi_{\lambda,N} \sim C\hat k_\lambda$ en compactos de $|\Im z|<1/2$ | Abierto |

**H1 + H2 + Teorema CCM + Lema 7.3 + Hurwitz $\Rightarrow$ RH.**

El programa de Phase 29:
1. **Documento 01:** Atacar H1 (par-simple) — teorema de dominancia aritmética para $\lambda$ grande.
2. **Documento 02:** Atacar H2 (convergencia) — teoría de perturbaciones del minimizador.
3. **Documento 03:** El muro nuevo — la brecha espectral de $QW_\lambda|_{E^+}$ y la obstrucción de convergencia.
