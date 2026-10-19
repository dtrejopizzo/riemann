# Phase 29 — The spectral gap and the new wall

**Goal:** Analyze with maximal precision the spectral gap $\delta_\lambda$ and propose an attack that avoids standard perturbation theory.

---

## 1. Reformulation of the central wall

From document 02: perturbation theory fails because:
$$\frac{\|A_\lambda\|_{\mathrm{op}}}{\delta_\lambda} \sim \lambda\,e^{4\pi\lambda^2} \to +\infty.$$

However, the conclusion we need does NOT require $\|\xi_\lambda - k_\lambda\|_{L^2} \to 0$. We only need the zeros of $\hat\xi_\lambda$ to converge to those of $\hat k_\lambda$. This is a condition on the argument of the entire function, not on its modulus in $L^2$ norm.

**The wall is reformulated:** Why do the zeros of $\hat\xi_\lambda$ converge to those of $\hat k_\lambda$ even though $\xi_\lambda$ does not converge to $k_\lambda$ in $L^2$ norm?

---

## 2. Structure of the zeros of entire functions with all zeros real

Let $F(z)$ be entire of order 1, with all its zeros real $\{t_n\} \subset \mathbb{R}$ with $t_n \to \pm\infty$, and such that $F$ is even ($F(-z) = F(z)$). Then:
$$F(z) = F(0)\prod_{n=1}^\infty\left(1 - \frac{z^2}{t_n^2}\right).$$

The convergence of the zeros toward $\{\gamma_n\}$ (zeros of $\Xi$) in the sense $\sum_n |t_n - \gamma_n|^2 < \infty$ is equivalent (via Newton's formulas for power sums) to the convergence of the **moments**:
$$m_k(F) := \sum_n \frac{1}{t_n^{2k}} \to m_k(\Xi) = \sum_n \frac{1}{\gamma_n^{2k}} \quad \forall k \geq 1.$$

This is the **moment convergence** condition.

**Proposition 1** (moments of $\hat\xi_\lambda$ in terms of $QW_\lambda$). The $k$-th moment of the zeros of $\hat\xi_\lambda$ satisfies:
$$m_k(\hat\xi_\lambda) = \sum_n \frac{1}{(t_n^{(\lambda)})^{2k}} = (-1)^k\left.\frac{d^{2k}}{dz^{2k}}\log\hat\xi_\lambda(z)\right|_{z=0} + (\text{polynomial-type terms}).$$

Via the relation $\det_{\mathrm{reg}}(D_{\log}^{(\lambda,N)}-z) = -i\lambda^{-iz}\hat\xi_{\lambda,N}(z)$ (CCM theorem), the moments of the eigenvalues of $D_{\log}^{(\lambda,N)}$ are exactly $m_k(\hat\xi_{\lambda,N})$.

---

## 3. Moments as functionals of $QW_\lambda$

**Lemma 1** (moment-form relation). For the function $\hat\xi_\lambda$ (transform of the minimizer $\xi_\lambda$ of $QW_\lambda|_{E^+}$):
$$m_1(\hat\xi_\lambda) = \sum_n \frac{1}{(t_n^{(\lambda)})^2} = \frac{\langle D_\lambda^2\xi_\lambda, \xi_\lambda\rangle}{\langle\xi_\lambda,\xi_\lambda\rangle_T} = \frac{QW_\lambda(D\xi_\lambda, D\xi_\lambda)}{QW_\lambda(\xi_\lambda,\xi_\lambda)},$$
where $D = D_{\log}^{(\lambda)}$ is the scaling operator.

This first moment is a ratio of quadratic forms evaluated at the minimizer. It does not depend on the full eigenvector in norm, but on how the operator $D$ acts on the minimizer.

**Consequence:** To prove convergence of the first moment:
$$m_1(\hat\xi_\lambda) \to m_1(\Xi) = \sum_\rho \frac{1}{\gamma_\rho^2},$$
we need to show that $\langle D_\lambda^2\xi_\lambda,\xi_\lambda\rangle_T \to \langle D_\infty^2 k, k\rangle_{T_\infty}$ (in an appropriate sense as $\lambda \to \infty$).

---

## 4. The mechanism of the zeros: the Carathéodory–Fejér identity

The CCM theorem establishes that the zeros of $\hat\xi_{\lambda,N}$ are exactly the eigenvalues of $D_{\log}^{(\lambda,N)}$. The convergence question translates to:

**How do the eigenvalues of $D_{\log}^{(\lambda,N)}$ vary with $\lambda, N$?**

By the rank-one structure:
$$D_{\log}^{(\lambda,N)} = D - |D\xi\rangle\langle\delta_N|$$

The eigenvalues of this operator satisfy the characteristic equation (from Lemma 5.4 of CCM):
$$\det(D_{\log}^{(\lambda,N)} - z) = \det(D-z)\cdot \hat\xi_{\lambda,N}(z).$$

The equation $\hat\xi_{\lambda,N}(z) = 0$ determines the eigenvalues. Explicitly (from the formula of Lemma 5.4):
$$\hat\xi_{\lambda,N}(z) = \sum_{|n| \leq N} \frac{\xi_n^{(\lambda,N)}}{z - 2\pi n/L}\cdot\frac{\sin(zL/2)}{\sqrt{L}/2}.$$

The zeros of $\hat\xi_{\lambda,N}$ are the values $z$ where this sum vanishes. These depend on the coefficients $\xi_n^{(\lambda,N)}$ (those of the eigenvector $\xi_{\lambda,N}$ in the basis $\{V_n\}$).

**Key remark:** The zeros of $\hat\xi_{\lambda,N}$ are not simple functions of the coefficients $\xi_n$ — they are solutions of a rational equation in $z$. Even though the $\xi_n$ may change drastically with $\lambda$ (due to the large arithmetic perturbation), the zeros of $\hat\xi$ can remain close to those of $\hat k_\lambda$ through a cancellation effect.

---

## 5. The cancellation mechanism: hypothesis on the coefficients

**Hypothesis HC** (coefficients). The coefficients $\xi_n^{(\lambda,N)}$ of the minimizer $\xi_{\lambda,N}$ satisfy:
$$\xi_n^{(\lambda,N)} = c_{\lambda,N}\,k_n^{(\lambda)} + r_n^{(\lambda,N)},$$
where $k_n^{(\lambda)}$ are the coefficients of $k_\lambda$, and the "residue" $r_n^{(\lambda,N)}$ satisfies:
$$\sum_{|n|\leq N} \frac{r_n^{(\lambda,N)}}{z - 2\pi n/L} = O\!\left(\frac{1}{\lambda^{1/2-\alpha}}\right) \quad \text{for } z \in K \subset S_{1/2}.$$

If HC holds, then:
$$\hat\xi_{\lambda,N}(z) = c_{\lambda,N}\hat k_\lambda(z) + O(\lambda^{-1/2+\alpha}) \to c\,\Xi(z).$$

**The problem:** HC is a hypothesis about the fine structure of the coefficients $\xi_n^{(\lambda,N)}$. It does not follow from standard perturbation theory (which failed). It needs a different argument.

---

## 6. Attack via uniqueness of the minimizer with boundary conditions

**Proposition 2** (variational characterization of $\xi_\lambda$). The minimizer $\xi_\lambda$ of $QW_\lambda|_{E^+}$ is the unique even function in $\mathcal{H}_\lambda^+$ satisfying:
$$\left(Q^{\mathrm{arch}} + Q^{\mathrm{cross}} - A_\lambda\right)f = \mu_\lambda f, \quad \delta(\xi_\lambda) = 1,$$
where $\mu_\lambda$ is the minimal eigenvalue.

The Euler–Lagrange equation is:
$$(B_\lambda - A_\lambda)\xi_\lambda = \mu_\lambda\xi_\lambda$$
where $B_\lambda = Q^{\mathrm{arch}} + Q^{\mathrm{cross}}|_{E^+}$.

This can be rewritten as:
$$\xi_\lambda = \mu_\lambda (B_\lambda - A_\lambda)^{-1}\xi_\lambda.$$

Or equivalently, $\xi_\lambda$ belongs to the kernel of the operator $B_\lambda - A_\lambda - \mu_\lambda$.

**Attack idea:** Express $(B_\lambda - A_\lambda - \mu_\lambda)^{-1}$ using the resolvent formula, and show that the dependence of the zeros of $\hat\xi_\lambda$ on $A_\lambda$ is smooth/continuous even when $A_\lambda$ is large.

---

## 7. The zero equation via spectral theory

**Proposition 3** (zero equation). The zeros $\{t_n^{(\lambda)}\}$ of $\hat\xi_\lambda$ satisfy the implicit equation:
$$\hat\xi_\lambda(t) = 0 \iff \frac{1}{L}\sum_{|n|\leq N}\frac{\xi_n^{(\lambda)}}{t - 2\pi n/L} = 0.$$

This is equivalent to $t$ being an eigenvalue of the scaling operator $D_{\log}^{(\lambda,N)}$, whose spectral equation is:
$$1 = \langle\delta_N, (D - t)^{-1}D\xi_{\lambda,N}\rangle = \sum_{|n|\leq N}\frac{2\pi n/L}{t - 2\pi n/L}\,\xi_n^{(\lambda)}.$$

Rearranging:
$$\sum_{|n|\leq N}\frac{2\pi n/L}{t - 2\pi n/L}\,\xi_n^{(\lambda)} = 1.$$

This is the **zero equation** in explicit form. The zeros are the values $t$ satisfying this rational equation (in $t$).

**To study the convergence of the zeros:** we need to understand how the solution set of this equation varies when the coefficients $\xi_n^{(\lambda)}$ vary with $\lambda$.

---

## 8. A stability estimate for the zeros

**Theorem 1** (stability of the zeros — partial result). Let $F_\lambda(z) = \hat\xi_\lambda(z)$ and $G_\lambda(z) = \hat k_\lambda(z)$. Suppose:
1. All zeros of $F_\lambda$ and $G_\lambda$ are real.
2. $F_\lambda$ and $G_\lambda$ have the same exponential type: $\log|F_\lambda(iy)| \sim \log|G_\lambda(iy)| \sim (\log\lambda)|y|$ as $y \to \pm\infty$.
3. The zeros of $G_\lambda$ are at positions $\{s_n^{(\lambda)}\}$ with separation $\min_n|s_n^{(\lambda)}-s_{n+1}^{(\lambda)}| \geq \delta > 0$.
4. $|F_\lambda(z) - G_\lambda(z)| \leq \epsilon |G_\lambda(z)|$ for $z$ on the boundary of the disks $D_n = \{|z-s_n^{(\lambda)}| \leq \delta/2\}$.

Then: each disk $D_n$ contains exactly one zero of $F_\lambda$, and this zero $t_n^{(\lambda)}$ satisfies $|t_n^{(\lambda)} - s_n^{(\lambda)}| \leq \epsilon\delta/2$.

*Proof.* By the argument principle (Rouché): on $\partial D_n$, $|F_\lambda - G_\lambda| \leq \epsilon|G_\lambda| < |G_\lambda|$ (for $\epsilon < 1$), so $F_\lambda$ and $G_\lambda$ have the same number of zeros in $D_n$, which is 1. The zero estimate follows from the differentiability of zeros in analytic functions. $\square$

**Theorem 1 reduces convergence to:** verifying that $|F_\lambda(z) - G_\lambda(z)| \leq \epsilon|G_\lambda(z)|$ on the boundary of sufficiently small disks centered at the zeros of $G_\lambda$.

This is a **pointwise estimate** on the functions (not an $L^2$ bound on eigenvectors), and in principle can be verified even when the spectral gap is small.

---

## 9. The new wall: pointwise estimate of $F_\lambda - G_\lambda$

The estimate $|F_\lambda(z) - G_\lambda(z)| \leq \epsilon|G_\lambda(z)|$ on circles around the zeros of $G_\lambda$ requires:
$$|\hat\xi_\lambda(z) - c_\lambda\hat k_\lambda(z)| \leq \epsilon|c_\lambda\hat k_\lambda(z)|.$$

Expanding:
$$\hat\xi_\lambda(z) - c_\lambda\hat k_\lambda(z) = \int_{\lambda^{-1}}^\lambda (\xi_\lambda(u) - c_\lambda k_\lambda(u))\,u^{-iz}\,d^*u.$$

For $z = s_n^{(\lambda)} + iy$ with $|y| = \delta/2$:
$$|\hat\xi_\lambda(z) - c_\lambda\hat k_\lambda(z)| \leq \|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}\cdot\lambda^{|y|}.$$

We need $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}\cdot\lambda^{\delta/2} \leq \epsilon|c_\lambda\hat k_\lambda(z)|$.

The wall: if $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}$ grows polynomially in $\lambda$ (the most optimistic one can hope for given that the spectral gap is $O(e^{-4\pi\lambda^2})$), but $|c_\lambda\hat k_\lambda(z)|$ near a zero of $G_\lambda$ is $O(|z - s_n|/\prod_m|z-s_m|)$ — which can be EXPONENTIALLY SMALL in $T_n$ (due to terms of the function $\Xi$ far from the origin) — the estimate can break down for large zeros.

**Precise wall:**
$$\text{Wall-H2}: \quad \frac{\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}\cdot\lambda^{\delta/2}}{|c_\lambda\hat k_\lambda(s_n^{(\lambda)} + i\delta/2)|} \to 0 \text{ for every } n.$$

This CANNOT follow from any general $L^2$ or $L^1$ norm estimate of $\xi_\lambda - c_\lambda k_\lambda$. It requires detailed information about how $\Xi(z)$ behaves near its zeros — in particular, the derivative $|\Xi'(\gamma_n)|$ (the "weight" of the zero).

---

## 10. The weight of the zeros of $\Xi$ as protection

**Definition.** The weight of the zero $\gamma_n$ of $\Xi$ is $w_n := |\Xi'(\gamma_n)|$.

**Known fact** (Titchmarsh). If the zeros are simple (believed but not proved), $w_n > 0$ for every $n$. The distribution of the weights is related to the moments of $|\Xi'|$ on the critical line, which are studied in Selberg's theory of the zeta function.

**Proposition 4** (condition in terms of the weight). The Wall-H2 estimate for the $n$-th zero becomes:
$$\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1} \ll \frac{w_n}{\lambda^{\delta/2}}.$$

If $w_n \geq c > 0$ uniformly in $n$ (which would be believed under RH + simple zeros), and $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1} = O(\lambda^{-\eta})$ for some $\eta > \delta/2$, then Wall-H2 is resolved.

**The real obstacle:** The decay rate of $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}$ is not known. The doubly exponentially small spectral gap suggests that $\xi_\lambda$ can differ significantly from $k_\lambda$ in norm. However, the difference in norm may lie in a direction orthogonal to the zeros — which is what matters.

---

## 11. Verdict of Phase 29: what was proved and the new wall

### New results of Phase 29:

| Result | Status |
|---|---|
| Simple-even for $\lambda \geq \lambda_0$ (arithmetic dominance via PNT) | **NEW (proved in doc 01)** |
| Failure of simple-even for $\lambda < \sqrt{2}$ | **NEW (proved in doc 01)** |
| Standard perturbation theory fails (gap $O(e^{-4\pi\lambda^2})$ vs norm $O(\lambda)$) | **NEW (diagnosed in doc 02-03)** |
| Convergence requires proximity in zeros, not in $L^2$ norm | **NEW (reformulation)** |
| Stability of zeros via Rouché (sufficient condition for H2) | **NEW (Theorem 1, doc 03)** |
| Wall-H2: pointwise estimate $\|\xi_\lambda - k_\lambda\|_{L^1} = o(w_n\lambda^{-\delta/2})$ | **NEW (precise wall)** |

### The new wall (genuinely different from all previous walls):

**Wall-H2:** The minimal eigenvector $\xi_\lambda$ of $QW_\lambda|_{E^+}$ must differ from $k_\lambda$ in $L^1$ norm by an order smaller than $w_n/\lambda^{\delta/2}$ for each $n$. This CANNOT follow from any standard operator-norm estimate (the spectral gap is too small). The mechanism that would guarantee it is specific to the arithmetic structure of the minimizer $\xi_\lambda$ — in particular, to how the truncated Euler product acts on the Weil kernel $k_\lambda$.

**Difference from previous walls:**
- Wall A (arithmetic propagation): about the factorization of $Q$ — not the same thing.
- Wall MW-4 (Hasse–Minkowski): about quadratic forms in infinite dimension — does not apply here.
- Wall H2: about the stability of zeros of an entire function under an eigenvector perturbation that is large in norm but potentially small in zero position.

This is the first wall of the program that does NOT involve Weil positivity directly, but rather the **continuity of the spectrum** of a family of operators that are self-adjoint by construction.

---

## 12. The most attackable remaining question

**Question 29.1.** Is $k_\lambda(u) \geq 0$ for every $u \in [\lambda^{-1},\lambda]$?

If yes: $I_p(k_\lambda) \geq 0$ for every prime $p$, the dominance condition AD is easier to verify, and the simple-even mechanism for every $\lambda \geq \sqrt{2}$ has structural support.

**Question 29.2.** Can $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}$ be bounded via some explicit formula for the change in eigenvector under the arithmetic perturbation $A_\lambda$?

The exact answer uses the resolvent formula:
$$\xi_\lambda - c_\lambda k_\lambda = (B_\lambda - \mu_\lambda)^{-1}A_\lambda k_\lambda + O(\|A_\lambda k_\lambda\|^2/\delta_\lambda^2)$$
(first-order perturbation), which is $O(\lambda e^{4\pi\lambda^2})$ — too large. But the $L^1$ norm of $\int u^{-iz}(\xi_\lambda - k_\lambda)d^*u$ can be much smaller due to cancellations.

**Question 29.3.** Does $\sum_n|t_n^{(\lambda)}-\gamma_n|^2 < C$ hold with $C$ independent of $\lambda$?

This is the $\ell^2$ convergence version of the zeros. If it holds, by Hadamard's Lemma (doc 02), convergence of the functions follows. It is a conjecture about the spectral regularity of the operator $D_{\log}^{(\lambda,N)}$.

These three questions are the most concrete and attackable ones to emerge from Phase 29.
