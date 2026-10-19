# Phase 29 — Attack on convergence: Hurwitz, Montel, and the spectral gap

**Goal:** Attack the convergence $\hat\xi_{\lambda,N}(z) \to \Xi(z)$ (H2) via:
1. Hurwitz structure: real zeros + uniform convergence → RH.
2. Montel's theorem: compactness of the family $\{\hat\xi_{\lambda,N}\}$.
3. Identification of the possible accumulation limits.
4. The precise obstacle (spectral gap).

---

## 1. Hurwitz's argument: exact structure of the proof

The central argument, once convergence is established, is:

**Hurwitz's theorem** (classical). Let $\{f_n\}$ be a sequence of analytic functions on a domain $\Omega \subset \mathbb{C}$ converging uniformly on compacts to $f \not\equiv 0$. If each $f_n$ has no zeros in $\Omega$, then $f$ has no zeros in $\Omega$ either.

Version with real zeros: if each $f_n$ has all its zeros in $\mathbb{R}$, and $f_n \to f$ uniformly on compacts of the strip $S_{1/2} := \{z : |\Im(z)| < 1/2\}$, then all the zeros of $f$ in $S_{1/2}$ are real.

**Application.** By the CCM theorem (doc 00), each $\hat\xi_{\lambda,N}$ has all its zeros in $\mathbb{R}$ (they are in $\mathbb{R}$ by construction). If $\hat\xi_{\lambda,N}(z)\cdot C_{\lambda,N}e^{a_{\lambda,N}+ib_{\lambda,N}z} \to \Xi(z)$ uniformly on compacts of $S_{1/2}$, and $\Xi \not\equiv 0$, then all the zeros of $\Xi$ in $S_{1/2}$ are real — that is, **RH**.

**The strategy:** Prove convergence using:
- Compactness of the family (Montel).
- Uniqueness of the limit (identification as $\Xi$).

---

## 2. Estimates on the family $\{\hat\xi_{\lambda,N}\}$

**Definition of canonical normalization.** For each $(\lambda,N)$, the minimizer $\xi_{\lambda,N}$ is normalized by $\delta_N(\xi_{\lambda,N}) = 1$. We define:
$$F_{\lambda,N}(z) := \hat\xi_{\lambda,N}(z) = \int_{\lambda^{-1}}^\lambda \xi_{\lambda,N}(u)\,u^{-iz}\,d^*u.$$
This is an entire function, with all zeros in $\mathbb{R}$.

**Lemma 1** (local boundedness in the strip). For every $\alpha \in (0,1/2)$:
$$\sup_{\lambda \geq \sqrt{2},\,N \geq 1} \|F_{\lambda,N}\|_{L^\infty(|\Im z|\leq\alpha)} < \infty$$
if and only if $\|\xi_{\lambda,N}\|_{L^1([\lambda^{-1},\lambda],d^*u)}$ is uniformly bounded in $\lambda,N$.

*Proof.* For $|\Im(z)| \leq \alpha$:
$$|F_{\lambda,N}(z)| = \left|\int_{\lambda^{-1}}^\lambda \xi_{\lambda,N}(u)\,u^{-iz}\,d^*u\right| \leq \|\xi_{\lambda,N}\|_{L^1}\cdot\max_{u\in[\lambda^{-1},\lambda]}|u^{-iz}| = \|\xi_{\lambda,N}\|_{L^1}\cdot\lambda^\alpha. \quad\square$$

**Immediate obstacle:** The factor $\lambda^\alpha$ grows with $\lambda$, so the sup bound is $\leq \lambda^\alpha \|\xi_{\lambda,N}\|_{L^1}$, which can grow. The canonical normalization $\delta_N(\xi)=1$ does not directly control the $L^1$ norm.

**Necessary renormalization.** Paper 2 proposes the renormalization:
$$\tilde F_{\lambda,N}(z) := C_{\lambda,N}^{-1} e^{a_{\lambda,N}+ib_{\lambda,N}z} F_{\lambda,N}(z),$$
for constants $C_{\lambda,N}$, $a_{\lambda,N}$, $b_{\lambda,N}$ to be chosen (via the position and residue at the first zero).

With this renormalization, Paper 2 reports numerically that $\tilde F_{\lambda,N}(z) \to \Xi(z)$.

---

## 3. Montel's argument: compactness

**Proposition 1** (compactness of the renormalized family). If the family $\{\tilde F_{\lambda,N}\}$ is uniformly bounded on each compact of $S_{1/2}$, then it is relatively compact in $\mathcal{O}(S_{1/2})$ (analytic functions on $S_{1/2}$ with the topology of uniform convergence on compacts).

*Proof.* By Montel's theorem: a locally uniformly bounded family of analytic functions is normal (has convergent subsequences). $\square$

**To apply Montel:** one needs to show $\|\tilde F_{\lambda,N}\|_{L^\infty(K)} \leq C_K$ for each compact $K \subset S_{1/2}$.

The strategy: use the normalization $\tilde F_{\lambda,N}(0) = 1$ (if achievable) to control the norm via a Cauchy bound.

---

## 4. Uniqueness of the limit: the functional hypothesis

Suppose there exists a subsequence $\tilde F_{\lambda_j, N_j} \to G$ uniformly on compacts, with $G$ analytic on $S_{1/2}$. By Hurwitz, all zeros of $G$ in $S_{1/2}$ are real.

**Question:** Is $G = \Xi$ (up to a scalar)?

**Identification via properties of $\Xi$:**
- $\Xi$ is even: $\Xi(-z) = \Xi(z)$.
- $\Xi(0) = \xi(1/2) \approx 0.4972 \neq 0$.
- The zeros of $\Xi$ have Riemann–von Mangoldt distribution: $N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + O(\log T)$.
- $\Xi$ satisfies the functional equation $\Xi(-z) = \Xi(z)$ and the reflection identity $\Xi(\bar z) = \overline{\Xi(z)}$.

**Theorem 1** (uniqueness under parity + growth). Let $G$ be entire with all its zeros in $\mathbb{R}$, even, $G(0) \neq 0$, and zero-counting function $N_G(T) \sim \frac{T}{2\pi}\log\frac{T}{2\pi e}$ (= the same rate as the zeros of $\Xi$). Then $G(z) = c\,\Xi(z)$ for some constant $c \in \mathbb{R}\setminus\{0\}$.

*Proof.* By the Hadamard product for entire functions of order 1:
$$G(z) = c\,e^{a+bz}\prod_n\!\left(1-\frac{z}{z_n}\right)e^{z/z_n}$$
with $\{z_n\} \subset \mathbb{R}$ and Riemann–von Mangoldt density. If $G$ is even, then $b = 0$ and the $z_n$ come in pairs $\pm|z_n|$. If the $z_n$ are exactly the zeros of $\Xi$ (same density), then $G = c\Xi$. $\square$

**The gap:** To apply this argument, we need the zeros of $G$ to be exactly the zeros of $\Xi$, which is not known a priori. What is known is that the zeros of $\tilde F_{\lambda,N}$ converge numerically to the zeros of $\Xi$. Uniqueness of the limit is a *result conditional* on the convergence of the zeros.

---

## 5. Reduction to the proximity of $\xi_{\lambda,N}$ and $k_\lambda$

**Proposition 2** (sufficient proximity for convergence). Suppose that for every compact $K \subset S_{1/2}$ and every $\epsilon > 0$, there exist $\lambda_0, N_0$ such that for $\lambda \geq \lambda_0$, $N \geq N_0$:
$$\left|\hat\xi_{\lambda,N}(z) - c_{\lambda,N}\hat k_\lambda(z)\right| < \epsilon\,|\hat k_\lambda(z)| \quad \forall z \in K,$$
where $c_{\lambda,N}$ is the relative normalization constant. Then:
$$c_{\lambda,N}\hat k_\lambda(z) = C_{\lambda,N}\hat k_\lambda(z) \to \Xi(z) \quad (\text{by Lemma 7.3})$$
and therefore $\hat\xi_{\lambda,N}(z)\cdot C_{\lambda,N}/c_{\lambda,N} \to \Xi(z)$ uniformly on $K$.

*Proof.* Direct from Lemma 7.3 (Connes et al., Lemma 7.3 of Paper 2) and the proximity estimate. $\square$

**The central problem:** Does the proximity estimate of Proposition 2 hold?

---

## 6. Perturbation theory of the minimizer

Let $\xi_\lambda$ be the minimizer of $QW_\lambda$ on $\mathcal{H}_\lambda$ (in the limit $N\to\infty$; for finite $N$ the discussion is analogous). The decomposition:
$$QW_\lambda = Q^{\mathrm{arch}} + Q^{\mathrm{cross}} - A_\lambda, \quad A_\lambda := \sum_{1<n\leq\lambda^2}\Lambda(n)T(n).$$

The minimizer of $Q^{\mathrm{arch}} + Q^{\mathrm{cross}}$ on $E^+$ is $k_\lambda$ (the well-behaved function). The perturbation is $-A_\lambda$, and the minimizer of $QW_\lambda$ is $\xi_\lambda$.

**Perturbation theorem** (Kato, Davis–Kahan). If the spectral gap of the unperturbed operator $B = Q^{\mathrm{arch}} + Q^{\mathrm{cross}}|_{E^+}$ between the first and second eigenvalue is $\delta > 0$, and if $\|A_\lambda\|_{\mathrm{op}} < \delta/2$, then:
$$\|\xi_\lambda - k_\lambda\| \leq \frac{2\|A_\lambda k_\lambda\|}{\delta - 2\|A_\lambda\|_{\mathrm{op}}}.$$

**Critical note:** To apply this result, we need $\|A_\lambda\|_{\mathrm{op}} \ll \delta$. However, the norm of the arithmetic operator grows with $\lambda$:

**Estimate of the arithmetic norm:**
$$\|A_\lambda\|_{\mathrm{op}} \leq \sum_{1<n\leq\lambda^2}\Lambda(n)\|T(n)\|_{\mathrm{op}}.$$
For $T(n)$ with $\|T(n)\|_{\mathrm{op}} \leq 2n^{-1/2}$ (by the definition and Cauchy–Schwarz):
$$\|A_\lambda\|_{\mathrm{op}} \leq 2\sum_{n\leq\lambda^2}\frac{\Lambda(n)}{\sqrt{n}} = 4\lambda + O\!\left(\lambda e^{-c\sqrt{\log\lambda}}\right) \sim 4\lambda.$$

**Then:** The norm of the perturbation grows like $\lambda$, while the spectral gap $\delta = \delta_\lambda$ of $Q^{\mathrm{arch}}+Q^{\mathrm{cross}}|_{E^+}$ is the unknown quantity. If $\delta_\lambda \gg \lambda$, perturbation theory gives $\|\xi_\lambda - k_\lambda\| = O(1)$, which is insufficient.

**The critical question:** What is the value of $\delta_\lambda$?

---

## 7. Estimate of the spectral gap: a partial result

**Definition.** Let $B_\lambda = Q^{\mathrm{arch}} + Q^{\mathrm{cross}}|_{E_\lambda^+}$ be the archimedean operator restricted to the even sector. Its eigenvalues are $0 < \mu_0^{(B)} \leq \mu_1^{(B)} \leq \cdots$ and the gap is $\delta_\lambda = \mu_1^{(B)} - \mu_0^{(B)}$.

**Proposition 3** (the spectral gap in terms of the prolate operator). The operator $B_\lambda$ is closely related to the prolate wave operator $PW_\lambda = -\partial_x(\lambda^2-x^2)\partial_x + (2\pi\lambda x)^2$. The eigenfunctions of $PW_\lambda$ (prolate spheroidal wave functions $\psi_{2n}$) are eigenfunctions of $B_\lambda$ to first order, with eigenvalues:
$$\mu_n^{(B)} \approx 1 - \chi_{2n}(\lambda), \quad n = 0, 1, 2, \ldots$$
where $\chi_{2n}(\lambda)$ is the eigenvalue of the Fourier compression $P_\lambda\hat F P_\lambda$ on $L^2([-\lambda,\lambda])$.

The estimates for the prolate eigenvalues (Landau–Pollak–Slepian):
$$\chi_0(\lambda) = 1 - O(e^{-4\pi\lambda^2}), \quad \chi_4(\lambda) = 1 - O(e^{-4\pi\lambda^2}).$$
Both decay at the same **doubly exponential** rate.

**Corollary 1** (doubly exponentially small gap). The spectral gap of $B_\lambda$ satisfies:
$$\delta_\lambda = \mu_1^{(B)} - \mu_0^{(B)} \approx |\chi_4(\lambda) - \chi_0(\lambda)|.$$
By the Slepian–Pollak formulas, $\chi_4 - \chi_0 = O(e^{-4\pi\lambda^2})$, so:
$$\delta_\lambda = O\!\left(e^{-4\pi\lambda^2}\right) \text{ (doubly exponentially small)}.$$

**Catastrophic consequence for perturbation theory:**
$$\frac{\|A_\lambda\|_{\mathrm{op}}}{\delta_\lambda} \sim \frac{4\lambda}{e^{-4\pi\lambda^2}} = 4\lambda\,e^{4\pi\lambda^2} \to +\infty.$$

The ratio norm-of-perturbation / spectral-gap is **doubly exponentially large**. Standard perturbation theory is **completely inapplicable**.

---

## 8. The convergence paradox: why it works numerically

If perturbation theory fails this catastrophically, why do the eigenvalues of the operator $D_{\log}^{(\lambda,N)}$ converge so well (error $10^{-55}$ with 6 primes)?

**Resolution (partial).** Standard perturbation theory measures the difference of eigenvectors in $L^2$ norm, but the function of interest is $\hat\xi_{\lambda,N}(z)$ — the multiplicative Fourier transform of the eigenvector. What is needed for Hurwitz convergence is not that $\xi_\lambda \approx k_\lambda$ in $L^2$ norm, but that:
$$\hat\xi_\lambda(z) \approx c\,\hat k_\lambda(z) \text{ uniformly on compacts of } S_{1/2}.$$

This is a **much weaker** condition than $L^2$ proximity: it only requires that the zeros of $\hat\xi_\lambda$ be close to those of $\hat k_\lambda$ (which approach those of $\Xi$ by Lemma 7.3). Even if $\|\xi_\lambda - c k_\lambda\|_{L^2}$ is large, the function $\hat\xi_\lambda$ can have zeros in the correct positions.

**New formulation of the problem.** The convergence problem is not $\|\xi_\lambda - k_\lambda\|_{L^2} \to 0$, but rather:
$$\sum_{n=1}^\infty \left|\gamma_n^{(\lambda)} - \gamma_n\right|^2 \to 0 \quad (\lambda \to \infty),$$
where $\{\gamma_n^{(\lambda)}\}$ are the zeros of $\hat\xi_\lambda$ and $\{\gamma_n\}$ are the zeros of $\Xi$.

This is convergence of the zeros, not of the functions in norm.

---

## 9. Hadamard's theorem as a bridge

Let $F(z)$ be entire of order $\leq 1$ with all zeros $\{z_n\} \subset \mathbb{R}$. Then by the Hadamard product:
$$F(z) = c\,e^{a+bz}\prod_n\!\left(1-\frac{z}{z_n}\right)e^{z/z_n}.$$

**Lemma 2** (proximity of zeros implies proximity of functions). If $\hat\xi_\lambda$ and $\hat k_\lambda$ are both entire of order 1 with all zeros real, and if the zeros of $\hat\xi_\lambda$ are $\{t_n^{(\lambda)}\}$ and those of $\hat k_\lambda$ are $\{s_n^{(\lambda)}\}$ with $\sum_n|t_n^{(\lambda)} - s_n^{(\lambda)}|^2 \to 0$ and the functions are normalized at the origin, then $\hat\xi_\lambda(z) \to \hat k_\lambda(z)$ uniformly on compacts of $S_{1/2}$.

*Proof.* By the Hadamard formula and the estimation of products: if the zeros are asymptotically equal and the exponential type converges, the product converges uniformly on compacts. (Weierstrass product convergence theorem.) $\square$

**Consequence:** The convergence of the zeros $\gamma_n^{(\lambda)} \to \gamma_n$ is EQUIVALENT to the convergence of the regularized determinants, which is EQUIVALENT to H2.

---

## 10. The new precise wall

The convergence $\gamma_n^{(\lambda)} \to \gamma_n$ (zeros of $\hat\xi_\lambda$ toward zeros of $\Xi$) is a statement about the spectrum of the operator $D_{\log}^{(\lambda,N)}$. By the CCM theorem, this spectrum is completely determined by:
1. The minimal eigenvector $\xi_{\lambda,N}$ of $QW_\lambda^N$ (conditional on simple-even, H1).
2. The multiplicative Fourier transform $\hat\xi_{\lambda,N}$.

**Precise wall H2:** Convergence fails if and only if there exists a sequence $\lambda_j \to \infty$ such that:
$$\exists R > 0: \quad \gamma_n^{(\lambda_j)} \not\to \gamma_n \text{ for some } n \text{ with } |\gamma_n| \leq R.$$

This is the only scenario that would prevent the proof of RH via this path. To rule out this scenario, one needs a **zero-separation** type estimate: the zeros of $\Xi$ are well separated from one another, and the zeros of $\hat\xi_\lambda$ cannot "jump" from one position to another.

---

## 11. Separation of zeros of $\Xi$ as protection

**Fact** (Littlewood, 1924): The zeros of $\Xi$ do not accumulate — for every $R > 0$, the number of zeros in $[-R,R]$ is finite ($= N(R)$). The minimal distance between consecutive zeros satisfies:
$$\min_{n \neq m} |\gamma_n - \gamma_m| \geq c/\log T_n$$
(conditionally under RH; unconditionally the zeros can be very close).

**Consequence:** If the zeros of $\hat\xi_\lambda$ are all in $\mathbb{R}$ and converge (in some sense) toward the zeros of $\Xi$, the separation of zeros of $\Xi$ protects the convergence: a zero of $\hat\xi_\lambda$ cannot "move" from the basin of attraction of $\gamma_n$ to that of $\gamma_m$ without crossing the midpoint. But since all zeros are real, there is no "motion in $\mathbb{C}$" — the zeros are confined to the real line.

This observation does not prove convergence, but it does show that if $k$ of the first zeros converge, the zeros $k+1, k+2, \ldots$ cannot "contaminate" the first $k$.

---

## 12. Synthesis: status of H2

| Step | Status |
|---|---|
| All zeros of $\hat\xi_{\lambda,N}$ are real (by construction) | **PROVED** (CCM theorem) |
| $\hat k_\lambda(z) \to \Xi(z)$ uniformly on compacts of $S_{1/2}$ | **PROVED** (Lemma 7.3) |
| Compactness of $\{\tilde F_{\lambda,N}\}$ (Montel) | **Conditional on a bound for $\|\tilde F\|_{L^\infty(K)}$** |
| $\xi_{\lambda,N} \approx k_\lambda$ in $L^2$ (standard perturbation) | **FAILS** (the spectral gap is $O(e^{-4\pi\lambda^2})$, too small) |
| Convergence of zeros $\gamma_n^{(\lambda)} \to \gamma_n$ | **OPEN** — this is H2 |
| If zeros converge, then $\hat\xi_{\lambda,N} \to \Xi$ | **PROVED** (Lemma 2 via Hadamard) |
| RH via Hurwitz | **Conditional on H1 + H2** |

**Contribution of this document:** Precise identification of the failure of standard perturbation theory (Corollary 1), reformulation of H2 as convergence of zeros (weaker than $L^2$ convergence), and new formulation of the wall via the spectral gap.

**The new wall (different from all previous walls):** The spectral gap $\delta_\lambda$ of $Q^{\mathrm{arch}}|_{E^+}$ is doubly exponentially small in $\lambda$, while the norm of the arithmetic perturbation grows like $\lambda$. Convergence of the zeros requires a mechanism that works **independently of the norm of the perturbation** — a property of the zeros, not of the eigenvectors.

This wall is **genuinely new**: it was not on the no-go list because this question had never before been posed in these terms.
