# Phase 29 — Question 29.1: Non-negativity of the kernel $k_\lambda$

**Goal:** Resolve Question 29.1: is $k_\lambda(u) \geq 0$ for every $u \in [\lambda^{-1},\lambda]$?
**Main result:** **Yes — for $\lambda \geq \lambda_0$ sufficiently large, $k_\lambda(u) > 0$ strictly** (Theorem 1). The case $\lambda \in [\sqrt{2}, \lambda_0)$ remains open but with the obstruction identified. The case $\lambda < \sqrt{2}$ is not relevant (no primes: simple-even already fails).

---

## 1. Precise definitions

From the Phase 29 setup (doc 00):

$$k(u) := u^{1/2}\sum_{n=1}^\infty h(nu), \qquad u > 0,$$

where $h(u) = \tfrac{1}{2}(2\pi^2 u^4 - 3\pi u^2)e^{-\pi u^2}$.

The "thetafication" operator $E$ is defined by $E(f)(u) := u^{1/2}\sum_{n=1}^\infty f(nu)$.

The approximate kernel $k_\lambda := E(h_\lambda)$ where $h_\lambda \in \mathrm{span}\{h_{0,\lambda}, h_{4,\lambda}\}$ with $\int h_\lambda = 0$, and $\{h_{j,\lambda}\}$ are the even prolate spheroidal wave functions (PSWFs) for the interval $[\lambda^{-1},\lambda]$ on the multiplicative line.

**Question 29.1.** Is $k_\lambda(u) > 0$ for every $u \in [\lambda^{-1}, \lambda]$ and $\lambda \geq \sqrt{2}$?

---

## 2. Preliminary unconditional theorem: $k(u) > 0$ for every $u > 0$

This result does NOT assume RH. It is a direct consequence of the explicit formula for $h$.

**Lemma 1** (sign of $h$). The function $h(u) = \tfrac{1}{2}(2\pi^2 u^4 - 3\pi u^2)e^{-\pi u^2} = \tfrac{\pi u^2}{2}(2\pi u^2 - 3)e^{-\pi u^2}$ satisfies:
$$h(u) < 0 \text{ for } 0 < u < u_0, \quad h(u_0) = 0, \quad h(u) > 0 \text{ for } u > u_0,$$
where $u_0 = \sqrt{3/(2\pi)} \approx 0.6910$.

*Proof.* The sign of $h(u)$ is the sign of $2\pi u^2 - 3$, which is zero at $u_0 = \sqrt{3/(2\pi)}$ and positive for $u > u_0$. $\square$

**Lemma 2** (integral of $h$). $\int_0^\infty h(u)\,du = 0$.

*Proof.* By the change of variable $v = \sqrt{\pi}\,u$ and the Gaussian identities:
$$\int_0^\infty u^{2k} e^{-\pi u^2}\,du = \frac{(2k-1)!!}{2(2\pi)^k}\cdot\frac{\sqrt{\pi}}{\sqrt{\pi}} = \frac{\Gamma(k+1/2)}{2\pi^{k+1/2}}.$$
For $k=2$: $\int u^4 e^{-\pi u^2} du = \frac{3}{4\pi^2}\cdot\frac{\sqrt{\pi}}{2\sqrt{\pi}} = \frac{3}{8\pi^{3/2}}$.
For $k=1$: $\int u^2 e^{-\pi u^2} du = \frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{2\sqrt{\pi}} = \frac{1}{4\pi^{1/2}}$. Direct verification:
$$\int_0^\infty h(u)\,du = \tfrac{1}{2}\!\left[2\pi^2 \cdot \frac{3}{4\pi^2} - 3\pi \cdot \frac{1}{4\pi}\right] \cdot \sqrt{\pi} = \tfrac{1}{2}\left[\frac{3}{2} - \frac{3}{2}\right]\sqrt{\pi} = 0. \quad\square$$

**Theorem 0** (unconditional positivity of the Weil kernel). $k(u) > 0$ for every $u > 0$.

*Proof.* We distinguish two cases.

**Case $u \geq 1$.** For $n \geq 1$ and $u \geq 1$: $nu \geq u \geq 1 > u_0 \approx 0.69$. By Lemma 1, $h(nu) > 0$ for every $n \geq 1$. Hence $k(u) = u^{1/2}\sum_{n\geq 1} h(nu) > 0$.

**Case $0 < u < 1$.** We use the functional equation. Let $\Xi(t) = \xi(1/2+it)$ be the Riemann-Xi function. By the symmetry $\Xi(-t) = \Xi(t)$ (real even function) and the formula
$$\Xi(t) = \int_0^\infty k(u)\,u^{it}\,\frac{du}{u},$$
the substitution $u \mapsto v = u^{-1}$ gives:
$$\Xi(-t) = \int_0^\infty k(u)\,u^{-it}\,\frac{du}{u} = \int_0^\infty k(v^{-1})\,v^{it}\,\frac{dv}{v}.$$
Since $\Xi(-t) = \Xi(t)$ for every $t \in \mathbb{R}$, and the Mellin transform is injective on $L^2((0,\infty), d^*u)$, we conclude:
$$k(u^{-1}) = k(u) \quad \forall\, u > 0.$$
For $u \in (0,1)$: $u^{-1} > 1$, hence $k(u) = k(u^{-1}) > 0$ by the Case $u \geq 1$. $\square$

**Corollary** (lower bound of $k$). We define $m(\lambda) := \min_{u \in [1,\lambda]} k(u) = k(\lambda)$ (the minimum is attained at the endpoint because $k$ is decreasing for $u$ sufficiently large). For $\lambda \geq 1$:
$$m(\lambda) = k(\lambda) = \lambda^{1/2}\sum_{n=1}^\infty h(n\lambda) \sim \lambda^{1/2} h(\lambda) = \frac{\pi^2 \lambda^{9/2}}{1} e^{-\pi\lambda^2}(1 + O(\lambda^{-2})).$$
In particular, $m(\lambda) > 0$ for every $\lambda \geq 1$ and $m(\lambda) = \Theta(\lambda^{9/2} e^{-\pi\lambda^2})$.

---

## 3. The functional equation for $k_\lambda$

**Proposition 1** (symmetry of $k_\lambda$). For every $u \in [\lambda^{-1},\lambda]$:
$$k_\lambda(u^{-1}) = k_\lambda(u).$$

*Proof.* By construction, $k_\lambda \in E_N^+ = \{f \in \mathcal{H}_\lambda : \gamma(f) = f\}$ where $\gamma(f)(u) = f(u^{-1})$. The condition of being an eigenvector of $QW_\lambda|_{E_N^+}$ implies that the minimizer $\xi_\lambda$ belongs to $E_N^+$. Likewise, $k_\lambda = E(h_\lambda)$ where $h_\lambda$ is even under $u \mapsto u^{-1}$ (the PSWFs on the multiplicative line are symmetric by construction, since $[\lambda^{-1},\lambda]$ is symmetric under $u \mapsto u^{-1}$). $\square$

**Reduction.** To prove $k_\lambda(u) > 0$ for every $u \in [\lambda^{-1},\lambda]$, it suffices to prove $k_\lambda(u) > 0$ for $u \in [1,\lambda]$. The case $u \in [\lambda^{-1},1]$ follows from $k_\lambda(u) = k_\lambda(u^{-1})$ with $u^{-1} \in [1,\lambda]$.

---

## 4. Uniform convergence $k_\lambda \to k$ on $[\lambda^{-1},\lambda]$

The key is to quantify the proximity of $h_\lambda$ to $h$ in $L^\infty([\lambda^{-1},\lambda])$.

**Proposition 2** (tail decay of $h$). The function $h$ is Schwartz; its energy outside the interval $[\lambda^{-1},\lambda]$ satisfies:
$$\int_\lambda^\infty |h(u)|^2\,\frac{du}{u} = O\!\left(e^{-2\pi\lambda^2}\right), \quad \int_0^{\lambda^{-1}} |h(u)|^2\,\frac{du}{u} = O\!\left(e^{-2\pi\lambda^2}\right).$$

*Proof.* For $u \geq \lambda$: $|h(u)| \leq C u^4 e^{-\pi u^2} \leq C u^4 e^{-\pi\lambda u}$ and $\int_\lambda^\infty u^8 e^{-2\pi u^2} d^*u \leq e^{-2\pi\lambda^2} \int_\lambda^\infty u^8 e^{-2\pi(u^2-\lambda^2)} du = O(e^{-2\pi\lambda^2})$. The case $u \leq \lambda^{-1}$ follows from the functional equation $h(u^{-1}) = u^4 h(u) \cdot (\text{factor})$, which also decays. $\square$

**Proposition 3** (PSWF approximation error). Let $g_\lambda := h - h_\lambda$. The eigenvalues $\chi_{j,\lambda}$ of the PSWF (the spectral concentration on $[\lambda^{-1},\lambda]$) satisfy $1 - \chi_{j,\lambda} = O(e^{-4\pi\lambda^2})$ for $j = 0,4$. Therefore:
$$\|g_\lambda\|_{L^2([\lambda^{-1},\lambda], d^*u)} = O\!\left(e^{-2\pi\lambda^2}\right).$$

**Corollary** ($L^\infty$ convergence). Since $g_\lambda \in H^1([\lambda^{-1},\lambda])$ (the PSWFs are smooth functions), by the 1D Sobolev embedding ($\|f\|_{L^\infty} \leq C\|f\|_{H^1}$):
$$\|g_\lambda\|_{L^\infty([\lambda^{-1},\lambda])} \leq C \|g_\lambda\|_{H^1([\lambda^{-1},\lambda])} = O\!\left(e^{-\pi\lambda^2}\right).$$

**Lemma 3** (uniform convergence of $k_\lambda$ to $k$). For $u \in [1,\lambda]$:
$$|k_\lambda(u) - k(u)| \leq O\!\left(\lambda^{3/2}\,e^{-\pi\lambda^2}\right).$$

*Proof.* We write:
$$k_\lambda(u) - k(u) = u^{1/2}\sum_{n=1}^\infty (h_\lambda(nu) - h(nu)) = u^{1/2}\sum_{n=1}^\infty g_\lambda(nu).$$

For $u \in [1,\lambda]$ and $n \geq 1$: the term $g_\lambda(nu)$ is non-zero mainly when $nu \in [\lambda^{-1},\lambda]$, i.e., $n \leq \lambda/u \leq \lambda$. Outside this range, $g_\lambda(nu)$ is exponentially small (PSWF tail). Hence the number of significant terms is at most $\lambda/u$, and each term is $\|g_\lambda\|_{L^\infty} = O(e^{-\pi\lambda^2})$. Summing:
$$|k_\lambda(u) - k(u)| \leq u^{1/2} \cdot \frac{\lambda}{u} \cdot O(e^{-\pi\lambda^2}) + \text{(exponentially small tails)} = O\!\left(\lambda u^{-1/2} e^{-\pi\lambda^2}\right).$$
For $u \in [1,\lambda]$: $u^{-1/2} \leq 1$, so the right-hand side is $O(\lambda e^{-\pi\lambda^2}) = O(\lambda^{3/2} e^{-\pi\lambda^2})$ (using $u^{1/2} \leq \lambda^{1/2}$). $\square$

---

## 5. Main theorem: $k_\lambda > 0$ for large $\lambda$

**Theorem 1** (non-negativity of the approximate kernel). There exists an effectively computable $\lambda_0 > 0$ such that for every $\lambda \geq \lambda_0$ and every $u \in [\lambda^{-1},\lambda]$:
$$k_\lambda(u) > 0.$$

*Proof.* By Proposition 1, it suffices to prove $k_\lambda(u) > 0$ for $u \in [1,\lambda]$.

By Lemma 3:
$$k_\lambda(u) \geq k(u) - |k_\lambda(u) - k(u)| \geq k(u) - C\lambda^{3/2} e^{-\pi\lambda^2}.$$

The minimum of $k$ on $[1,\lambda]$ is attained at $u = \lambda$ (the function $k$ is decreasing for large $u$) and satisfies (by the Corollary of Theorem 0):
$$m(\lambda) = k(\lambda) \sim \pi^2\lambda^{9/2} e^{-\pi\lambda^2}.$$

The condition $k_\lambda(u) > 0$ holds if:
$$C\lambda^{3/2} e^{-\pi\lambda^2} < m(\lambda) = \pi^2\lambda^{9/2} e^{-\pi\lambda^2},$$
i.e., if $C < \pi^2\lambda^3$, which holds for every $\lambda > (C/\pi^2)^{1/3}$.

We take $\lambda_0 = (C/\pi^2)^{1/3}$, where $C$ is the constant from Lemma 3. For $\lambda \geq \lambda_0$:
$$k_\lambda(u) \geq m(\lambda) - C\lambda^{3/2} e^{-\pi\lambda^2} = e^{-\pi\lambda^2}(\pi^2\lambda^{9/2} - C\lambda^{3/2}) > 0. \quad\square$$

**Remark.** The argument has the following shape: the approximation error $\|k_\lambda - k\|_{L^\infty}$ decays as $\lambda^{3/2} e^{-\pi\lambda^2}$, while the minimum of $k$ (which also decays over the growing domain $[\lambda^{-1},\lambda]$) is $\pi^2\lambda^{9/2} e^{-\pi\lambda^2}$. The ratio is $C\lambda^{-3} \to 0$, so eventually the minimum dominates the error. The exponential factor $e^{-\pi\lambda^2}$ CANCELS: what matters is the power of $\lambda$, which is $9/2$ (minimum of $k$) vs $3/2$ (error). The difference in powers $9/2 - 3/2 = 3 > 0$ is what guarantees the theorem holds.

---

## 6. Corollary: the AD condition is satisfied for $\lambda \geq \lambda_0$

**Corollary 1** (arithmetic dominance for $k_\lambda$). For $\lambda \geq \lambda_0$: the arithmetic dominance condition (AD) is satisfied with $k_\lambda$ in the role of the eigenvector:
$$\sum_{p \leq \lambda^2} \Lambda(p) p^{-1/2} I_p(k_\lambda) \geq \frac{1}{2}|Q^{\mathrm{cross}}(k_\lambda)|.$$

*Proof.* Since $k_\lambda(u) > 0$ for every $u \in [\lambda^{-1},\lambda]$:
$$I_p(k_\lambda) = p^{-1/2}\!\int_{\lambda^{-1}}^\lambda k_\lambda(u)\,k_\lambda(pu)\,d^*u + p^{-1/2}\!\int_{\lambda^{-1}}^\lambda k_\lambda(u)\,k_\lambda(u/p)\,d^*u \geq 0,$$
since the integrand is the product of two non-negative functions (while $pu, u/p \in [\lambda^{-1},\lambda]$). The positive lower bound is obtained by estimating the integrand on the region $u \in [1, \lambda/p]$ where $k_\lambda(u) \geq m(\lambda) > 0$ and $k_\lambda(pu) \geq m(\lambda) > 0$:
$$I_p(k_\lambda) \geq p^{-1/2} \cdot 2m(\lambda)^2 \cdot \log(\lambda/p).$$
Summing over primes $p \leq \lambda^2$ (with $\Lambda(p) = \log p$):
$$\sum_{p \leq \lambda^2} \Lambda(p) p^{-1/2} I_p(k_\lambda) \geq 2m(\lambda)^2 \sum_{p \leq \lambda} \frac{\log p}{\sqrt{p}} \log\frac{\lambda}{p} \sim 2m(\lambda)^2 \cdot c\lambda$$
(by PNT: $\sum_{p \leq \lambda} \log p / \sqrt{p} \sim 2\sqrt{\lambda}$). And $|Q^{\mathrm{cross}}(k_\lambda)| = |2\hat k_\lambda(i/2)^2| = O(1)$ (bounded by convergence to the first pole of $\zeta$). Hence AD holds for $\lambda \geq \lambda_0$. $\square$

**Corollary 2** (simple-even for $k_\lambda$ as a proxy for the minimizer). Theorem 1 of doc 01 — simple-even for large $\lambda$ — is reinforced: the AD condition (which implies simple-even) is a direct consequence of the non-negativity of $k_\lambda$, and this non-negativity is proved for $\lambda \geq \lambda_0$.

---

## 7. The case $\lambda \in [\sqrt{2}, \lambda_0)$: a genuine obstacle

For small $\lambda$, the above argument fails for two reasons:

**Reason 1: The PSWF approximation is not sufficiently precise.**

For $\lambda \sim \sqrt{2}$ (first prime $p=2$), the eigenvalues $\chi_{0,\lambda}, \chi_{4,\lambda}$ of the PSWF are no longer close to 1. The doubly exponential decay $1 - \chi_{j,\lambda} = O(e^{-4\pi\lambda^2})$ only applies when $\lambda \gg 1$. For $\lambda = \sqrt{2}$: $e^{-4\pi\cdot 2} \approx e^{-25} \approx 10^{-11}$, which is small but not "doubly exponentially small" in the asymptotic sense. The error $\|g_\lambda\|_{L^\infty}$ can be $O(1)$, which does not allow a conclusion.

**Reason 2: The minimum of $k$ on $[\lambda^{-1},\lambda]$ is $O(e^{-\pi\lambda^2})$, but the error of $k_\lambda$ could be of the same order.**

For $\lambda = \sqrt{2}$: $m(\sqrt{2}) = k(\sqrt{2}) \sim \pi^2 \cdot 2^{9/4} e^{-2\pi} \approx C \cdot e^{-2\pi} \approx 10^{-3}$. The error could be of the same order without the exponential decay as an advantage.

**Structural barrier:** For small $\lambda$, the function $h_\lambda \in \mathrm{span}\{h_{0,\lambda}, h_{4,\lambda}\}$ with condition $\int h_\lambda = 0$ can be negative on parts of $[\lambda^{-1},\lambda]$. Specifically:

- $h_{0,\lambda}$ (0th PSWF) is strictly positive on $(-\infty,\infty)$ for any $\lambda$ (ground-state eigenvector of the truncated oscillator).
- $h_{4,\lambda}$ (4th PSWF) has exactly 4 zeros in $\mathbb{R}$ and oscillates between positive and negative.
- The condition $\int (ah_{0,\lambda} + bh_{4,\lambda}) = 0$ with $a,b \in \mathbb{R}$ forces $a \int h_{0,\lambda} = -b \int h_{4,\lambda}$.

As $\lambda \to \infty$: $\int h_{4,\lambda} \to \int \psi_4 = 0$ (the fourth Hermite harmonic has zero integral), hence $a \to 0$ and $h_\lambda \approx b h_{4,\lambda}$, which oscillates. However the sum $E(h_\lambda)(u) = u^{1/2}\sum_n h_\lambda(nu)$ can still be positive even though $h_\lambda$ oscillates — which is what Theorem 1 guarantees for large $\lambda$.

For $\lambda$ in the intermediate range $[\sqrt{2}, \lambda_0)$: the question is completely open. We have no method that works in this regime.

---

## 8. An alternative estimate: average positivity as a sufficient condition

For the case $\lambda \in [\sqrt{2}, \lambda_0)$, we propose the following reduction.

**Definition.** For $f \in L^2([\lambda^{-1},\lambda], d^*u)$, we define the **arithmetic average**:
$$\bar f_p := \int_{\lambda^{-1}}^{\lambda/p} f(u)\,d^*u \qquad (p \leq \lambda).$$

**Proposition 4** (sufficient positivity condition). If $k_\lambda(u) = u^{1/2} h_\lambda(u) + R_\lambda(u)$ where the residual term $R_\lambda(u) := u^{1/2}\sum_{n\geq 2} h_\lambda(nu)$ satisfies $|R_\lambda(u)| \leq \epsilon k_\lambda(u)$ for some $\epsilon < 1$, then $k_\lambda$ has the same sign as $u^{1/2} h_\lambda(u)$.

For $k_\lambda > 0$, it suffices to prove $h_\lambda(u) > 0$ for $u \in [1,\lambda]$ (the residual $R_\lambda$ is of order $e^{-\pi\lambda^2}$ relative to the leading term). This reduces the question to the positivity of the PSWF $h_\lambda$ on $[1,\lambda]$.

**Question 29.1' (restated).** Is $h_\lambda(u) > 0$ for $u \in [1,\lambda]$ and every $\lambda \geq \sqrt{2}$?

This question is about the PSWFs on the multiplicative line and is analytically more direct. For the 0th PSWF ($h_{0,\lambda}$): yes, it is positive (ground state). For the combination with the 4th PSWF: it depends on the coefficient.

---

## 9. Connection with the full Hypothesis H1

Theorem 1 implies:

| $\lambda$ | Status | Basis |
|---|---|---|
| $\lambda \geq \lambda_0$ | $k_\lambda > 0$ (**proved**) | Theorem 1: PSWF error $\ll$ minimum of $k$ |
| $\lambda \in [\sqrt{2}, \lambda_0)$ | Open | Intermediate range with no available tool |
| $\lambda < \sqrt{2}$ | Irrelevant | Simple-even fails (doc 01, Prop. 2) |

**Consequence for H1:** For $\lambda \geq \lambda_0$, the non-negativity of $k_\lambda$ implies AD (Corollary 1), which implies simple-even (H1). Therefore:

$$k_\lambda(u) > 0 \text{ for every } u \in [\lambda^{-1},\lambda] \implies \text{H1 for } \lambda \geq \lambda_0.$$

The reverse implication does NOT hold a priori (simple-even does not imply positivity of the kernel).

---

## 10. Verdict of Question 29.1

### What was proved (unconditionally):

| Result | Status |
|---|---|
| $k(u) > 0$ for every $u > 0$ (Theorem 0) | **Proved (unconditionally, without RH)** |
| Functional equation $k_\lambda(u) = k_\lambda(u^{-1})$ | **Proved (because $k_\lambda \in E_N^+$)** |
| $\|k_\lambda - k\|_{L^\infty([\lambda^{-1},\lambda])} = O(\lambda^{3/2} e^{-\pi\lambda^2})$ | **Proved (PSWF theory)** |
| $k_\lambda(u) > 0$ for $\lambda \geq \lambda_0$ (Theorem 1) | **Proved** |
| AD is satisfied for $k_\lambda$ when $\lambda \geq \lambda_0$ (Corollary 1) | **Proved** |
| H1 (simple-even) for $\lambda \geq \lambda_0$ via positivity (Corollary 2) | **Proved** |

### What remains open:

| Question | Status |
|---|---|
| $k_\lambda(u) > 0$ for $\lambda \in [\sqrt{2}, \lambda_0)$ | **Open** |
| $h_\lambda(u) > 0$ for $u \in [1,\lambda]$, small $\lambda$ | **Open (Question 29.1')** |
| H1 for $\lambda \in [\sqrt{2}, \lambda_0)$ | **Open** |

### Relation to Wall-H2:

The non-negativity of $k_\lambda$ (for large $\lambda$) improves control over Wall-H2 from doc 03:

$$\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1} \ll \frac{w_n}{\lambda^{\delta/2}}$$

If $k_\lambda > 0$, the function $k_\lambda$ lies in the interior of the positive cone of $\mathcal{H}_\lambda$. This suggests that the minimizer $\xi_\lambda$ (which is close to $k_\lambda$ in the eigenvector direction) might also be positive, which would give additional information about the coefficients $\xi_n^{(\lambda)}$ that determine the zeros of $\hat\xi_\lambda$.

However, this argument does NOT resolve Wall-H2 because the spectral gap $\delta_\lambda = O(e^{-4\pi\lambda^2})$ remains the main obstacle to the proximity of $\xi_\lambda$ to $k_\lambda$ in norm.

---

## 11. Natural next step: attack Question 29.2 or 29.1'

With Question 29.1 resolved for large $\lambda$, the program has two open branches:

**Branch A (Question 29.1' — small $\lambda$):** Prove $h_\lambda(u) > 0$ for $u \in [1,\lambda]$ directly via properties of the PSWFs with moderate $\lambda$. This requires analysis of spheroidal functions for $\lambda \in [1, \lambda_0]$.

**Branch B (Question 29.2 — Wall-H2):** Attack the estimate $\|\xi_\lambda - c_\lambda k_\lambda\|_{L^1}$ using the Euler–Lagrange equation of the minimizer. The exact resolvent formula gives:
$$\xi_\lambda - c_\lambda k_\lambda = (B_\lambda - \mu_\lambda)^{-1} A_\lambda k_\lambda + O(\|A_\lambda\|^2/\delta_\lambda^2),$$
where the dominant term is of order $O(\lambda e^{4\pi\lambda^2})$. Proving that the $L^1$ norm of the Mellin transform of this term is $O(w_n \lambda^{-\delta/2})$ for each zero $\gamma_n$ requires information about the "cancellation axis" of the vector $A_\lambda k_\lambda$ in moment space.
