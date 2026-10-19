# Phase 29 — Zeta Spectral Triples: precise setup

**Based on:** Connes–Consani–Moscovici arXiv:2511.22755 (2025); Connes arXiv:2602.04022 (2026); Connes–Moscovici arXiv:2112.05500 (PNAS 2022).
**Fundamental difference from all previous approaches:** the operators are self-adjoint BY CONSTRUCTION (via Carathéodory–Fejér). There is no need to prove positivity of a quadratic form. The only obstacle is operator convergence.

---

## 1. The exact problem to solve

Let $\Xi(t) = \xi(1/2+it)$ be Riemann's real entire function, with
$$\Xi(t) = \int_0^\infty k(u)\, u^{it}\, d^*u, \quad k(u) = u^{1/2}\sum_{n=1}^\infty h(nu),$$
where $h(u) = \frac{1}{2}(2\pi^2 u^4 - 3\pi u^2)e^{-\pi u^2}$ and $d^*u = du/u$.

The Riemann Hypothesis is equivalent to all zeros of $\Xi$ being real.

Connes–Consani–Moscovici (2025) construct a family of entire functions $\hat\xi_{\lambda,N}(z)$, **all of whose zeros are real by construction**, and conjecture that
$$\hat\xi_{\lambda,N}(z)\cdot C_{\lambda,N} e^{a_{\lambda,N} + ib_{\lambda,N} z} \longrightarrow \Xi(z)$$
uniformly on compacts of the strip $|\Im(z)| < 1/2$, as $N,\lambda \to \infty$.

By **Hurwitz's theorem**: if the convergence holds, $\Xi$ has all its zeros in $\mathbb{R}$, i.e., RH.

---

## 2. The semilocal Weil quadratic form

**Definition 1.** For $\lambda > 1$, the Hilbert space is $\mathcal{H}_\lambda := L^2([\lambda^{-1},\lambda], d^*u)$ with orthonormal basis
$$V_n(u) := L^{-1/2}\exp\!\left(\frac{2\pi i n \log(\lambda u)}{L}\right), \quad L := 2\log\lambda, \quad n \in \mathbb{Z}.$$

The **multiplicative Fourier transform** is:
$$\hat f(z) := \int_{\lambda^{-1}}^\lambda f(u)\, u^{-iz}\, d^*u = L^{-1/2}\sum_n \hat f_n \cdot \frac{\sin((z-2\pi n/L)\cdot L/2)}{z - 2\pi n/L}$$
for $f = \sum_n f_n V_n$.

**Definition 2** (Semilocal Weil form). The semilocal Weil quadratic form is:
$$QW_\lambda(f,f) := \underbrace{\int_{\mathbb{R}} |\hat f(t)|^2 \frac{2\partial_t\theta(t)}{2\pi}\,dt}_{=:\, Q^{\mathrm{arch}}(f)} + \underbrace{2\hat f\!\left(\tfrac{i}{2}\right)\hat f\!\left(-\tfrac{i}{2}\right)}_{=:\, Q^{\mathrm{cross}}(f)} - \underbrace{\sum_{1 < n \leq \lambda^2} \Lambda(n)\,\langle f \mid T(n)f\rangle}_{=:\, Q^{\mathrm{arith}}(f,\lambda)},$$
where:
- $\theta(t) = \Im\log\Gamma(1/4+it/2) - (t/2)\log\pi$ is the Riemann–Siegel angular function, with $\partial_t\theta(t) \sim \frac{1}{2}\log(t/2\pi)$ for $t \gg 1$.
- $\Lambda(n)$ is the von Mangoldt function.
- $T(n)$ is the bounded self-adjoint operator on $\mathcal{H}_\lambda$ with
$$\langle f \mid T(n) f\rangle = n^{-1/2}\left[(f^* * f)(n) + (f^* * f)(n^{-1})\right],$$
with multiplicative convolution $(f^* * g)(n) = \int f(u^{-1})g(nu)\,d^*u$.

**Proposition 1** (matrix structure). In the basis $\{V_n\}_{|n|\leq N}$, the matrix of $QW_\lambda^N$ (the restriction to $E_N = \mathrm{span}\,\{V_n : |n|\leq N\}$) has the form:
$$\tau_{n,n} = a_n \in \mathbb{R}, \quad \tau_{n,m} = \frac{b_n - b_m}{n-m} \text{ for } n\neq m,$$
with $a_{-n} = a_n$ and $b_{-n} = -b_n$ (i.e., $\{a_n\}$ is even and $\{b_n\}$ is odd). This is the **Cauchy–Toeplitz** structure key to the Carathéodory–Fejér theorem.

---

## 3. The symmetry involution and the even/odd subspaces

The **functional involution** $\gamma: \mathcal{H}_\lambda \to \mathcal{H}_\lambda$ defined by $\gamma(f)(u) := f(u^{-1})$ satisfies $\gamma^2 = \mathrm{id}$. In the basis: $\gamma(V_n) = V_{-n}$ (since $V_n(u^{-1}) = e^{-2\pi i n\log(\lambda u)/L}\cdot e^{2\cdot 2\pi i n \log\lambda/L}$... more precisely: $V_n(u^{-1}) = L^{-1/2}e^{2\pi in\log(\lambda/u)/L} = L^{-1/2}e^{-2\pi in\log(\lambda u)/L} \cdot e^{4\pi in\log\lambda/L}$. With $L = 2\log\lambda$: $= L^{-1/2}e^{-2\pi in\log(\lambda u)/L} \cdot e^{2\pi in} = V_{-n}(u)$).

Therefore: $\gamma(V_n) = V_{-n}$.

**Subspaces:**
$$E_N^+ := \{f \in E_N : \gamma f = f\} = \mathrm{span}\,\{U_n^+ : 0 \leq n \leq N\}, \quad U_0^+ := V_0,\ U_n^+ := (V_n+V_{-n})/\sqrt{2}\ (n\geq 1)$$
$$E_N^- := \{f \in E_N : \gamma f = -f\} = \mathrm{span}\,\{U_n^- : 1 \leq n \leq N\}, \quad U_n^- := (V_n-V_{-n})/\sqrt{2}$$

**Proposition 2** (the form respects the involution). The form $QW_\lambda^N$ preserves $E_N^\pm$, i.e., $QW_\lambda^N(f^+, f^-) = 0$ for $f^\pm \in E_N^\pm$. Therefore:
$$QW_\lambda^N = QW_\lambda^{N,+}\!\oplus\, QW_\lambda^{N,-}$$
as quadratic forms on $E_N^+ \oplus E_N^-$.

*Proof.* Each component $Q^{\mathrm{arch}}$, $Q^{\mathrm{cross}}$, $Q^{\mathrm{arith}}$ is $\gamma$-invariant. For $Q^{\mathrm{arch}}$: $\hat{\gamma f}(t) = \overline{\hat f(t)}$ for the additive Fourier transform on $\mathbb{R}$; for the multiplicative one: $\widehat{\gamma f}(z) = \hat f(-z)$ (via the substitution $u\mapsto u^{-1}$). For $Q^{\mathrm{cross}}$: it depends on $\hat f(i/2)\hat f(-i/2)$, which is symmetric under $f\mapsto\gamma f$. For $T(n)$: if $f$ is even/odd, $T(n)f$ is too. $\square$

---

## 4. The scaling operator and the rank-one perturbation

**Definition 3** (scaling operator). The scaling operator with periodic boundary conditions:
$$D_{\log}^{(\lambda)} := -iu\frac{\partial}{\partial u}: \mathcal{H}_\lambda \to \mathcal{H}_\lambda$$
with eigenvalues $\mu_n = 2\pi n/L$ ($n \in \mathbb{Z}$) and eigenvectors $V_n$. It is self-adjoint on $\mathcal{H}_\lambda$.

**The evaluation functional** at $u = \lambda$:
$$\delta_N(f) := \langle f, \delta_N\rangle = \frac{1}{\sqrt{L}}\sum_{|n|\leq N} f_n, \quad \|\delta_N\|^2 = \frac{2N+1}{L}.$$

**Simple-even hypothesis** (ES). $QW_\lambda^N$ has its minimal eigenvalue $\epsilon_{\lambda,N}$ in $E_N^+$, with multiplicity 1. The corresponding eigenvector (normalized by $\delta_N(\xi)=1$) is called the **minimizer**.

**Definition 4** (perturbed operator). Under (ES), the minimizer $\xi = \xi_{\lambda,N} \in E_N^+$ defines:
$$D_{\log}^{(\lambda,N)} := D_{\log}^{(\lambda)}\bigg|_{E_N} - \big|D_{\log}^{(\lambda)}\xi\big\rangle\big\langle\delta_N\big|.$$

---

## 5. The main theorem (Connes–Consani–Moscovici)

**Theorem CCM** (Theorem 5.10 / Theorem 1.1 of arXiv:2511.22755). Under (ES):

**(i) Self-adjointness by construction.** $D_{\log}^{(\lambda,N)}$ is self-adjoint on the Hilbert space $(E_N/\mathbb{C}\xi,\, \langle\cdot|\cdot\rangle_T)$, where the inner product is
$$\langle f,g\rangle_T := (QW_\lambda^N - \epsilon_{\lambda,N}\langle\cdot|\cdot\rangle)(f,g) \quad (f,g \in E_N/\mathbb{C}\xi).$$

**(ii) Regularized determinant.** The regularized determinant (via the spectral zeta function) satisfies:
$$\det_{\mathrm{reg}}\!\left(D_{\log}^{(\lambda,N)} - z\right) = -i\lambda^{-iz}\,\hat\xi_{\lambda,N}(z),$$
where $\hat\xi_{\lambda,N}(z) = \int_{\lambda^{-1}}^\lambda \xi_{\lambda,N}(u)\,u^{-iz}\,d^*u$ is an entire function.

**(iii) Spectrum = real zeros of $\hat\xi$.** The function $\hat\xi_{\lambda,N}(z)$ is entire, all its zeros are real, and the spectrum of $D_{\log}^{(\lambda,N)}$ coincides exactly with the zero set of $\hat\xi_{\lambda,N}$.

**Corollary** (self-adjointness ↔ real zeros). The eigenvalues of $D_{\log}^{(\lambda,N)}$ are all real. Therefore, the "approximate zeros of $\Xi$" produced by this operator **always lie on the critical line**, for every $\lambda, N$.

*Mechanism:* The Cauchy–Toeplitz structure of the matrix $\tau_{n,m}$ implies that $[D, T] = |\beta\rangle\langle\eta| - |\eta\rangle\langle\beta|$ (rank 2). The rank-one perturbation $D' = D - |D\xi\rangle\langle\eta|$ becomes self-adjoint in $(E_N/\ker T, \langle\cdot|\cdot\rangle_T)$ via the Sylvester identity for commutators.

---

## 6. The convergence lemma (proved by Connes et al.)

**Lemma 7.3** (Connes–Consani–Moscovici). Let $k_\lambda = E(h_\lambda)$ where $h_\lambda$ is the unique linear combination of prolate spheroidal wave functions $h_{0,\lambda}, h_{4,\lambda}$ with vanishing integral. Then:
$$\hat k_\lambda(z) \longrightarrow \Xi(z) \quad \text{uniformly on compacts of } |\Im(z)| < \frac{1}{2},$$
with rate:
$$\left|\hat k_\lambda(z) - \Xi(z)\right| \leq C_\alpha \lambda^{-1/2-\alpha}(1-2\alpha)^{-1} \quad \text{for } |\Im(z)| \leq \alpha < \frac{1}{2}.$$

**Global convergence condition (Phase 29, Goal).** Prove:
$$\hat\xi_{\lambda,N}(z)\cdot C_{\lambda,N} e^{a_{\lambda,N}+ib_{\lambda,N}z} \longrightarrow \Xi(z)$$
on compacts of $|\Im(z)| < 1/2$. By Lemma 7.3, this reduces to proving:
$$\hat\xi_{\lambda,N}(z) \sim C\,\hat k_\lambda(z) \text{ (in the sense of local uniform convergence)}.$$

---

## 7. The two open hypotheses and the Phase 29 program

| Hypothesis | Precise statement | Status |
|---|---|---|
| **H1 (simple-even)** | $QW_\lambda^N$ has a simple, even minimal eigenvalue for every $\lambda\geq\sqrt{2}, N\geq 1$ | Open; verified numerically |
| **H2 (convergence)** | $\hat\xi_{\lambda,N} \sim C\hat k_\lambda$ on compacts of $|\Im z|<1/2$ | Open |

**H1 + H2 + Theorem CCM + Lemma 7.3 + Hurwitz $\Rightarrow$ RH.**

The Phase 29 program:
1. **Document 01:** Attack H1 (simple-even) — arithmetic-dominance theorem for large $\lambda$.
2. **Document 02:** Attack H2 (convergence) — perturbation theory of the minimizer.
3. **Document 03:** The new wall — the spectral gap of $QW_\lambda|_{E^+}$ and the convergence obstruction.
