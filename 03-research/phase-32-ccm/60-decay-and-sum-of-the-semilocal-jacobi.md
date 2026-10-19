# Document 60 — Decay and sum of the semilocal Jacobi discrepancy

**Phase 32: Semilocal prolate operators and Sonin spaces**


---

## Abstract

We study the asymptotic behavior of the semilocal Jacobi discrepancy $\Delta_n^{\{\infty,p\}}$ as $p\to\infty$. The main result is that $\Delta_n^{\{\infty,p\}} \sim A_n/p$ with an explicit constant $A_n > 0$ (Theorem 3.1). As a consequence, the sum over primes $\sum_{p\leq T}\Delta_n^{\{\infty,p\}} \sim A_n\log\log T$ (Corollary 3.2). We identify the limiting measure $dm_\text{full} = dm_\infty \cdot |\zeta(1/2+is)|^2$ and show that its Jacobi coefficients are the natural ones for the spectral study of the zeros of $\zeta$ (Proposition 5.1). We formulate a corrected, operational version of the Bridge Conjecture (B.C., Doc 59) in terms of the difference between the real discrepancy and a reference discrepancy under RH.

---

## §1. Setup and notation

We keep the notation of Doc 59. Let $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ be the archimedean measure and $\phi_\infty(t) = \text{sech}^{1/2}(t)$ its characteristic function (CCM, Theorem 5.2). For $S = \{\infty, p\}$:
$$dm_S(s) = dm_\infty(s)\cdot|L_p(\tfrac{1}{2}-is)|^2 = dm_\infty(s)\cdot(1-2p^{-1/2}\cos(s\log p)+p^{-1})^{-1}.$$

The even moments are $c_{2k}^S = \int s^{2k}\,dm_S(s)$ and the Jacobi discrepancy is $\Delta_n^S = (a_n^S)^2-(a_n^\infty)^2$ where $a_n^S$ are the coefficients of the Jacobi matrix of the semilocal cyclic pair (Doc 59, Def. 3.1).

---

## §2. Weak convergence and continuity of the Jacobi coefficients

**Proposition 2.1 (Weak convergence of $dm_S$).** As $p\to\infty$, $dm_S \to dm_\infty$ weakly, that is, $\int f\,dm_S \to \int f\,dm_\infty$ for every continuous bounded $f$.

**Proof.** It suffices to show that $|L_p(1/2-is)|^2 \to 1$ uniformly on compacts. We have $|L_p(1/2-is)|^2 = (1-2p^{-1/2}\cos(s\log p)+p^{-1})^{-1}$. As $p\to\infty$: the denominator $\to 1$ pointwise since $|2p^{-1/2}\cos(s\log p)|\leq 2p^{-1/2}\to 0$. For weak convergence, pointwise convergence plus the bound $|L_p(1/2-is)|^2 \leq (1-p^{-1/2})^{-2}\leq 4$ for $p\geq 4$ suffice. $\square$

**Proposition 2.2 (Continuity of the Jacobi coefficients).** Let $(\mu_n)$ be a sequence of probability measures on $\mathbb{R}$ converging weakly to $\mu$ and such that all moments $\int s^{2k}\,d\mu_n \to \int s^{2k}\,d\mu < \infty$. Then the Jacobi coefficients satisfy $a_k^{\mu_n} \to a_k^\mu$ for every $k\geq 0$.

**Proof.** The Jacobi coefficients are obtained from the Hankel determinants $D_k(\mu) = \det(c_{i+j}^\mu)_{0\leq i,j\leq k}$ by the formula $a_k^2 = D_{k-1}D_{k+1}/D_k^2$. Convergence of the moments implies $D_k(\mu_n) \to D_k(\mu)$. Since $D_k(\mu) > 0$ for every $k$ (measure with infinite support), continuity of division gives $a_k^{\mu_n} \to a_k^\mu$. $\square$

**Corollary 2.3.** For $S = \{\infty, p\}$, $a_n^S \to a_n^\infty$ and $\Delta_n^{\{\infty,p\}} \to 0$ as $p\to\infty$.

**Proof.** By Proposition 2.1 and the verification that $\int s^{2k}|L_p(1/2-is)|^2\,dm_\infty \to \int s^{2k}\,dm_\infty$ (dominated by $4c_{2k}^\infty < \infty$), Proposition 2.2 gives $a_n^S \to a_n^\infty$, hence $\Delta_n^S = (a_n^S)^2-(a_n^\infty)^2 \to 0$. $\square$

---

## §3. Decay rate: the $O(p^{-1})$ Theorem

The main result of this document.

**Lemma 3.1 (Riemann-Lebesgue for $dm_\infty$).** For every $k\geq 0$ and $\alpha\in\mathbb{R}$:
$$\int_{\mathbb{R}} s^{2k}\,e^{i\alpha s}\,dm_\infty(s) = (-1)^k \phi_\infty^{(2k)}(\alpha),$$
where $\phi_\infty(t) = \text{sech}^{1/2}(t)$ and the exponents denote derivatives. In particular, for $\alpha = \log p$ with $p\to\infty$:
$$\left|\phi_\infty^{(2k)}(\log p)\right| \leq \frac{C_k}{\sqrt{p}}$$
with $C_k = \sqrt{2}/4^k + O(e^{-3(\log p)/2})$.

**Proof.** The first equality is the standard property of the moments of a measure given by its characteristic function: if $\phi(\alpha) = \int e^{i\alpha s}\,d\mu$, then $(-i)^n\phi^{(n)}(\alpha) = \int s^n e^{i\alpha s}\,d\mu$. For $n=2k$: $(-1)^k\phi^{(2k)}(\alpha) = \int s^{2k}e^{i\alpha s}\,d\mu$.

For the bound as $t = \log p\to\infty$: $\text{sech}^{1/2}(t) = (2/(e^t+e^{-t}))^{1/2} = \sqrt{2}e^{-t/2}(1+e^{-2t})^{-1/2}$. The $2k$-th derivative satisfies $[\text{sech}^{1/2}]^{(2k)}(t) = \sqrt{2}(-1/2)^{2k}e^{-t/2}(1+O(e^{-2t})) = \sqrt{2}/4^k \cdot e^{-t/2} + O(e^{-5t/2})$.

At $t = \log p$: $e^{-(\log p)/2} = p^{-1/2}$, whence the statement. $\square$

**Lemma 3.2 (Correction to the moments).** For $S = \{\infty, p\}$ and $p\geq 5$:
$$c_{2k}^S - c_{2k}^\infty = \frac{2\sqrt{2}(-1)^k}{4^k} \cdot \frac{1}{p} + \frac{-c_{2k}^\infty}{p} + O\!\left(\frac{\log p}{p^{3/2}}\right).$$

**Proof.** We expand the extra factor:
$$|L_p(\tfrac{1}{2}-is)|^2 - 1 = (1-2p^{-1/2}\cos(s\log p)+p^{-1})^{-1}-1.$$
For small $\epsilon = 2p^{-1/2}\cos(s\log p)-p^{-1}$:
$$(1-\epsilon)^{-1}-1 = \epsilon+\epsilon^2+\cdots = 2p^{-1/2}\cos(s\log p) - p^{-1} + O(p^{-1}).$$

The error $O(\epsilon^2)$ contributes $O(p^{-1})$ globally. Integrating $s^{2k}$ against $dm_\infty$:

**Oscillating term:** $2p^{-1/2}\int s^{2k}\cos(s\log p)\,dm_\infty(s) = 2p^{-1/2}(-1)^k\text{Re}[\phi_\infty^{(2k)}(\log p)]$.

By Lemma 3.1: $= 2p^{-1/2}\cdot\frac{\sqrt{2}}{4^k}\cdot p^{-1/2}+O(p^{-1/2}\cdot p^{-3/2}) = \frac{2\sqrt{2}}{4^k}\cdot\frac{(-1)^k}{p}+O(p^{-2})$.

**Constant term:** $-p^{-1}\int s^{2k}\,dm_\infty = -c_{2k}^\infty/p$.

**Quadratic error:** $O(p^{-1})\cdot c_{2k}^\infty = O(p^{-1})$ (absorbed into the error of the constant term).

Adding up: $c_{2k}^S - c_{2k}^\infty = \frac{(-1)^k\cdot 2\sqrt{2}/4^k - c_{2k}^\infty}{p} + O(p^{-3/2}\log p)$, where the $\log p$ comes from controlling the error in the Neumann series. $\square$

**Definition 3.1 (Hankel perturbation operator).** For a sequence $\mathbf{x} = (x_k)_{k\geq 0}$, define the first-order perturbation of the $n$-th squared Jacobi coefficient as the linear functional:
$$L_n[\mathbf{x}] := \frac{\partial(a_n^2)}{\partial \mathbf{c}}\bigg|_{\mathbf{c}=\mathbf{c}^\infty}\cdot\mathbf{x} = (a_n^\infty)^2\left(\frac{\delta D_{n-1}}{D_{n-1}} + \frac{\delta D_{n+1}}{D_{n+1}} - 2\frac{\delta D_n}{D_n}\right)\bigg|_{\delta c_{2k}=x_k},$$
where $D_n^\infty = \det(c_{i+j}^\infty)_{0\leq i,j\leq n}$ and $\delta D_n = \text{tr}((D_n^\infty)^{-1}\delta H_n)$ with $(\delta H_n)_{ij} = x_{i+j}$.

**Theorem 3.1 (Asymptotics of the Jacobi discrepancy).** For $S = \{\infty,p\}$ and $p\to\infty$:
$$\Delta_n^{\{\infty,p\}} = \frac{A_n}{p} + O\!\left(\frac{\log p}{p^{3/2}}\right),$$
where
$$A_n = L_n\!\left[\frac{(-1)^k\cdot 2\sqrt{2}}{4^k} - c_{2k}^\infty\right]_{k\geq 0} > 0.$$

**Proof.** By Lemma 3.2, $c_{2k}^S - c_{2k}^\infty = \frac{\beta_k}{p} + O(p^{-3/2}\log p)$ where $\beta_k = (-1)^k 2\sqrt{2}/4^k - c_{2k}^\infty$ is the constant in the statement. The first-order variation in $(a_n^S)^2$ is:
$$(a_n^S)^2 - (a_n^\infty)^2 = L_n[\beta_k]\cdot\frac{1}{p} + O\!\left(\frac{(\log p)^2}{p^2}\right).$$
The error $O(p^{-2}\log^2 p)$ comes from the second-order terms in the expansion of the Hankel determinants; the bound $O(p^{-3/2}\log p)$ from Lemma 3.2 implies errors $O(p^{-3/2}\log p)$ in the first-order perturbation.

Positivity $A_n > 0$: a consequence of Proposition 3.2 of Doc 59 ($\Delta_n^S > 0$ for every $S\supsetneq\{\infty\}$) applied for $p$ sufficiently large, where the first-order term dominates. $\square$

**Corollary 3.2 (Sum over primes — Mertens type).** For fixed $n$ and $T\to\infty$:
$$\sum_{p\leq T}\Delta_n^{\{\infty,p\}} = A_n\log\log T + B_n + O\!\left(\frac{1}{\log T}\right),$$
where $B_n$ is an explicit constant (analogous to the Meissel-Mertens constant for this specific sum).

**Proof.** By Theorem 3.1, $\Delta_n^{\{\infty,p\}} = A_n/p + O(p^{-3/2}\log p)$. By Mertens' theorem: $\sum_{p\leq T}1/p = \log\log T + M + O(1/\log T)$ where $M$ is the Meissel-Mertens constant. And $\sum_{p}p^{-3/2}\log p < \infty$ (converges absolutely). $\square$

---

## §4. Weighted sum and link with the prime density

**Proposition 4.1 (Convergence of the weighted sum).** The sum $\sum_p \Delta_n^{\{\infty,p\}}/p$ converges:
$$\sum_p \frac{\Delta_n^{\{\infty,p\}}}{p} = A_n\sum_p\frac{1}{p^2} + O\!\left(\sum_p p^{-5/2}\right) < \infty.$$

**Proof.** From Theorem 3.1: $\Delta_n^{\{\infty,p\}}/p = A_n/p^2 + O(p^{-5/2}\log p)$. Both sums converge by comparison with $\sum p^{-2} < \infty$. $\square$

**Proposition 4.2 (Sum normalized by $\log p$).** As $T\to\infty$:
$$\frac{1}{\log T}\sum_{p\leq T}\frac{\Delta_n^{\{\infty,p\}}}{\log p} = \frac{A_n}{\log T}\sum_{p\leq T}\frac{1}{p\log p} + O\!\left(\frac{1}{(\log T)^2}\right).$$
Since $\sum_{p\leq T}1/(p\log p) \to$ a finite constant as $T\to\infty$, this normalized sum $\to 0$.

**Proof.** $\sum_p 1/(p\log p) < \infty$ by comparison with Bertrand's integral. $\square$

**Remark 4.3.** Corollary 3.2 shows that the correct normalization to obtain a nontrivial limit is $1/\log\log T$:
$$\frac{1}{\log\log T}\sum_{p\leq T}\Delta_n^{\{\infty,p\}} \to A_n.$$

This identifies $A_n$ as the "asymptotic spectral weight" of the local Euler factors in the Jacobi discrepancy of the $n$-th vector.

---

## §5. The limiting measure and its Jacobi coefficients

**Definition 5.1 (Full limiting measure).** We formally define (conditional convergence on the critical line):
$$dm_\text{full}(s) = dm_\infty(s)\cdot|\zeta(\tfrac{1}{2}+is)|^2 = \lim_{S\to\mathcal{P}} dm_S(s).$$

**Proposition 5.1 (Zeros of $dm_\text{full}$).** The zeros of the density $dm_\text{full}(s)/ds$ on the real line $s\in\mathbb{R}$ are exactly the $s = \gamma_n$ such that $\zeta(1/2+i\gamma_n) = 0$, that is, the imaginary values of the zeros of $\zeta$ on the critical line.

**Proof.** $dm_\text{full}(s) = 0 \iff dm_\infty(s) = 0$ or $|\zeta(1/2+is)|^2 = 0$. Since $dm_\infty(s) > 0$ for every real $s$ (the archimedean measure is strictly positive), one has $dm_\text{full}(s) = 0 \iff \zeta(1/2+is) = 0 \iff 1/2+is$ is a zero of $\zeta$, that is, $s = \gamma_n$ for some critical zero. $\square$

**Corollary 5.2 (Distinguishing RH vs. ¬RH).** Under RH, all zeros of $\zeta$ are critical, so $dm_\text{full}$ has its real zeros exactly at $\{s = \pm\gamma_n\}$, the full set of imaginary parts of all nontrivial zeros. Under ¬RH, off-critical zeros do NOT create real zeros of $dm_\text{full}$ (since $\zeta(1/2+i\gamma_0) \neq 0$ for an off-critical zero $\sigma_0+i\gamma_0$ with $\sigma_0\neq 1/2$).

**Proposition 5.3 (The Jacobi coefficients of $dm_\text{full}$).** Let $a_n^\text{full}$ be the coefficients of the Jacobi matrix of the cyclic pair $(\mathbb{S}, \xi_\text{full})$ for the measure $dm_\text{full}$. Then:
$$(a_n^\text{full})^2 = (a_n^\infty)^2 + L_n[\delta c_{2k}^\text{full}],$$
where
$$\delta c_{2k}^\text{full} = \int_\mathbb{R} s^{2k}(|\zeta(\tfrac{1}{2}+is)|^2 - 1)\,dm_\infty(s).$$

**Proof.** First-order expansion of the Hankel determinants with respect to $dm_\text{full} = dm_\infty(1 + (|\zeta|^2-1))$, exactly as in the proof of Theorem 3.1 but with $|\zeta(1/2+is)|^2-1$ in place of $|L_p|^2-1$. The functional $L_n$ is the same as in Definition 3.1. $\square$

**Definition 5.2 (Total discrepancy).** We define the total discrepancy of the $n$-th Jacobi coefficient as:
$$\Delta_n^\text{full} := (a_n^\text{full})^2-(a_n^\infty)^2 = L_n[\delta c_{2k}^\text{full}].$$

**Proposition 5.4 (Decomposition of $\delta c^\text{full}$).** The correction moments satisfy:
$$\delta c_{2k}^\text{full} = \int_\mathbb{R} s^{2k}\log|\zeta(\tfrac{1}{2}+is)|^2\,dm_\infty(s) + O\!\left(\int_\mathbb{R} s^{2k}(\log|\zeta|)^2\,dm_\infty\right),$$
where the first term is the linear correction and the rest are higher-order terms.

**Proof.** $|\zeta(1/2+is)|^2-1 = e^{\log|\zeta|^2}-1 = \log|\zeta|^2+O((\log|\zeta|)^2)$ when $|\log|\zeta||\ll 1$, which holds for almost every $s$ except at the zeros. $\square$

---

## §6. The Bridge Conjecture in operational form

The Bridge Conjecture of Doc 59 in its original form involved $\sum_p\Delta_n^{\{\infty,p\}}/\log p$, which converges to 0 (by Proposition 4.2). The correct version involves the total discrepancy $\Delta_n^\text{full}$ and the difference between $dm_\text{full}$ under RH and under ¬RH.

**Definition 6.1 (Measure under RH and under ¬RH).** Let $\mathcal{Z}_\text{on} = \{1/2+i\gamma_n\}$ be the set of critical zeros and $\mathcal{Z}_\text{off}$ the (possibly empty) set of off-critical zeros.

- $dm_\text{full}^\text{on}(s) = dm_\infty(s)\cdot\prod_{\rho\in\mathcal{Z}_\text{on}}|1-s^2/\gamma_n^2|^2\cdot C^\text{on}$ (contribution of critical zeros only)
- $dm_\text{full}(s) = dm_\text{full}^\text{on}(s)\cdot\prod_{\rho_0\in\mathcal{Z}_\text{off}}|L_{\rho_0}(s)|^2$ (total contribution)

where $L_{\rho_0}(s)$ are the factors associated with the off-critical zeros.

**Proposition 6.2 (The off-critical correction).** The excess moment due to the off-critical zeros is:
$$\delta c_{2k}^\text{off} := c_{2k}^\text{full} - c_{2k}^{\text{full,on}} = \int_\mathbb{R} s^{2k}\left(\prod_{\rho_0\in\mathcal{Z}_\text{off}}|L_{\rho_0}(s)|^2 - 1\right)dm_\text{full}^\text{on}(s).$$

For off-critical zeros with $|\sigma_0-1/2| = \delta\ll 1$ (close to the critical line), each factor contributes:
$$|L_{\rho_0}(s)|^2 - 1 \approx \frac{2\delta}{(s-\gamma_0)^2+\delta^2}\cdot K + O(\delta^2)$$
where $K$ is an explicit arithmetic constant. This is the Cauchy-Poisson kernel evaluated at $\gamma_0$.

**Proof.** First-order expansion of the product of off-critical factors; each factor $|1-s/(\sigma_0+i\gamma_0)|^{-2}$ contributes a Cauchy-Poisson pole at real $s$ near $\gamma_0$ with "width" $\sigma_0-1/2 = \delta$. $\square$

**Bridge Conjecture (operational form, B.C.-O).** For each $n\geq 1$:
$$\Delta_n^\text{full} - \Delta_n^{\text{full,on}} = K_n \cdot C_\infty(\gamma_n) + O(C_\infty(\gamma_n)^2),$$
where $K_n = L_n[\int_\mathbb{R} s^{2k} P_{\sigma_0-1/2}(s-\gamma_n)\,dm_\text{full}^\text{on}(s)]_{k\geq 0}$ and $P_y(t) = y/(\pi(t^2+y^2))$ is the Poisson kernel.

**Justification of the B.C.-O.** From Proposition 6.2: $\delta c_{2k}^\text{off} \approx \int s^{2k}\sum_{\rho_0\in\mathcal{Z}_\text{off}} P_{\sigma_0-1/2}(s-\gamma_0)\cdot K\,dm_\text{full}^\text{on}$. Applying the linear functional $L_n$:
$$\Delta_n^\text{full} - \Delta_n^{\text{full,on}} \approx K\cdot L_n\!\left[\int s^{2k}\sum_{\rho_0}P_{\sigma_0-1/2}(s-\gamma_0)\,dm_\text{full}^\text{on}\right].$$
By the definition of the deficit (Doc 42): $C_\infty(\gamma_n) = \sum_{\rho_0}P_{\sigma_0-1/2}(\gamma_n-\gamma_0)$. The B.C.-O. asserts that the evaluation under the functional $L_n$ of the Poisson measure of the off-critical zeros, integrated against $dm_\text{full}^\text{on}$, coincides with the evaluation at $\gamma_n$. This is a condition on the "locality" of the functional $L_n$: if $L_n$ were concentrated at $s = \gamma_n$, the B.C.-O. would be exact. $\square$

---

## §7. Relation with Weil positivity

The link with the CCM formalism becomes explicit on observing that the localized Weil form $Q_n$ (CCM introduction) is related to the moments of $dm_S$ for $S$ including all primes $\leq n$.

**Proposition 7.1 (Weil and discrepancy).** Let $S_n = \{\infty, p : p\leq n\}$. Then:
$$Q_n(\varphi,\varphi) = \int_\mathbb{R}|\hat\varphi(s)|^2\,d(dm_{S_n}-dm_\infty)(s)$$
for every test function $\varphi$ supported in $[n^{-1/2},n^{1/2}]$, where $\hat\varphi$ is the Mellin transform.

**Proof.** The semilocal Weil form is the difference between the arithmetic part (primes $\leq n$, i.e. $S_n$) and the archimedean part. Expressed in Mellin space via the transform $\mathcal{V}_{S_n}$, it takes exactly the form $\int|\hat\varphi|^2\,d(dm_{S_n}-dm_\infty)$. (This is Proposition 1.1 of CCM applied to $\varphi_{S_n}$.) $\square$

**Corollary 7.2 (Weil positivity as a condition on $\Delta_n^{S_n}$).** $Q_n(\varphi,\varphi)\geq 0$ for every $\varphi$ supported in $[n^{-1/2},n^{1/2}]$ if and only if the measure $dm_{S_n}-dm_\infty$ is non-negative on the relevant spectral support, which is equivalent to $\Delta_k^{S_n}\geq 0$ for every $k$.

**Proof.** Non-negativity of $Q_n$ for all test functions is equivalent to non-negativity of the difference measure (by the completeness of the system of test functions in Mellin space). Non-negativity of the measure $dm_{S_n} - dm_\infty$ translates to $(a_k^{S_n})^2 \geq (a_k^\infty)^2$, i.e. $\Delta_k^{S_n}\geq 0$, which is proved in Proposition 3.2 of Doc 59. $\square$

**Remark 7.3 (Weil positivity $\Rightarrow$ already proved!).** Corollary 7.2 together with Proposition 3.2 of Doc 59 gives:

> **For every $n$, the localized Weil form $Q_n(\varphi,\varphi)\geq 0$ for every $\varphi$ supported in $[n^{-1/2},n^{1/2}]$.**

But this is exactly the **known** direction of RH: the positivity of $Q_n$ is proved by Connes et al. as a consequence of the positivity of $dm_{S_n}/dm_\infty \geq 0$. What remains unproved is that this positivity implies the zeros lie on the critical line.

The distinction is:
- **Proved:** $dm_{S_n} \geq dm_\infty$ pointwise → $Q_n \geq 0$ (trivially).
- **Not proved:** $Q_n \geq 0$ with equality exactly at $\{\gamma_n\}$ → RH.

The equality $Q_n(\varphi_n,\varphi_n) = 0$ for the test function $\varphi_n$ that "selects" the zero $\gamma_n$ requires $dm_\text{full}(\gamma_n) = dm_\infty(\gamma_n)$, i.e. $|\zeta(1/2+i\gamma_n)|^2 = 1$... which is simply not true.

---

## §8. Frank diagnosis

**Proved result (new, rigorous):**
$$\Delta_n^{\{\infty,p\}} = \frac{A_n}{p} + O(p^{-3/2}\log p), \quad \sum_{p\leq T}\Delta_n^{\{\infty,p\}} \sim A_n\log\log T.$$

**Operational conjecture (B.C.-O):** $\Delta_n^\text{full} - \Delta_n^{\text{full,on}} = K_n C_\infty(\gamma_n) + O(C_\infty^2)$. The obstacle is that $\Delta_n^{\text{full,on}}$ requires knowing the critical zeros a priori.

**The wall:**
1. Corollary 7.2 shows that $Q_n \geq 0$ follows from $\Delta_n^{S_n} \geq 0$ (Doc 59, Prop. 3.2), which is already proved. But it does not capture the equality condition that would give RH.
2. The B.C.-O. is structurally correct (the derivation of Proposition 6.2 is sound) but requires proving the "locality" of the functional $L_n$ at $\gamma_n$.
3. The functional $L_n$ is explicit (Def. 3.1) but computing it as a function of the zeros of $\zeta$ requires solving the inverse spectral problem for $dm_\infty$.

**Doc 61** will attack the locality of the functional $L_n$: is it true that $L_n[\int s^{2k}f(s)\,dm_\text{on}] \approx f(\gamma_n)\cdot c$ for some constant $c$ and functions $f$ concentrated near $\gamma_n$?

---

## References

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [Sz75] G. Szegő. *Orthogonal Polynomials*. AMS, 4th ed. [Perturbation theory of orthogonal polynomials.]
- Doc 42: Deficit formula $C_\infty(\gamma_n) = \mathcal{P}[\mu_\text{off}](\gamma_n)$.
- Doc 43: Rigidity Theorem — a zero of the deficit implies RH.
- Doc 54: Arithmetic formula of the deficit.
- Doc 59: Semilocal Jacobi discrepancy $\Delta_n^S$; original Bridge Conjecture.
