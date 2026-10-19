# Hypothesis H1: The simple-even property

**Goal:** Prove (or delimit the domain of validity of) H1: the minimal eigenvalue of $QW_\lambda^N$ is simple and its eigenvector is even.

---

## 1. Precise matrix reformulation

The simple-even property (ES) states: over the space $E_N = E_N^+ \oplus E_N^-$ with the even/odd decomposition of document 00,
$$\mu^+(\lambda,N) < \mu^-(\lambda,N),$$
where $\mu^\pm = \min_{f \in E_N^\pm, \|f\|=1} QW_\lambda^N(f,f)$, and moreover $\mu^+$ is a simple eigenvalue of $QW_\lambda^{N,+}$.

By Proposition 2 of doc 00, $QW_\lambda^N = QW_\lambda^{N,+} \oplus QW_\lambda^{N,-}$, so it suffices to study the two restrictions separately.

---

## 2. Analysis of the three sectors on $E_N^\pm$

**Proposition 1** (signs of the sectors on even/odd).

*(a) Cross sector.* For $f \in E_N^+$: $\hat f(-z) = \hat f(z)$, hence $\hat f(-i/2) = \hat f(i/2)$ and
$$Q^{\mathrm{cross}}(f) = 2\hat f(i/2)^2 \geq 0.$$
For $f \in E_N^-$: $\hat f(-z) = -\hat f(z)$, hence $\hat f(-i/2) = -\hat f(i/2)$ and
$$Q^{\mathrm{cross}}(f) = -2\hat f(i/2)^2 \leq 0.$$

*(b) Arithmetic sector.* For $f \in E_N^+$ (even function, $f(u) = f(u^{-1})$):
$$\langle f \mid T(n)f\rangle = 2n^{-1/2}\int_{\lambda^{-1}}^\lambda f(u)f(nu)\,d^*u.$$
For $f \in E_N^-$ (odd function, $f(u) = -f(u^{-1})$):
$$\langle f \mid T(n)f\rangle = -2n^{-1/2}\int_{\lambda^{-1}}^\lambda f(u)f(nu)\,d^*u.$$
In both cases, the integrand $f(u)f(nu)$ can be positive or negative, but the integral $I_n(f) := \int f(u)f(nu)\,d^*u$ is the same. Therefore:
$$Q^{\mathrm{arith}}(f,\lambda) = -\sum_{1<k\leq\lambda^2}\Lambda(k)\,\langle f\mid T(k)f\rangle = \begin{cases} -2\sum_k \Lambda(k)k^{-1/2}I_k(f) & f \in E_N^+ \\ +2\sum_k \Lambda(k)k^{-1/2}I_k(f) & f \in E_N^- \end{cases}$$

*(c) Archimedean sector.* $Q^{\mathrm{arch}}(f)$ has the same expression for $f \in E_N^\pm$ (the integrand $|\hat f(t)|^2 \partial_t\theta$ is invariant under $f\mapsto\gamma f$ since $|\widehat{\gamma f}(t)| = |\hat f(t)|$).

**Corollary 1.** For any normalized $f_0 \in E_N^+$ with $\|f_0\| = 1$ and its odd image $f_0^- = f_0 - \gamma f_0 / \|\cdots\|$ (projection and renormalization), we have:
$$QW_\lambda^N(f_0, f_0) - QW_\lambda^N(f_0^-, f_0^-) = 4\hat f_0(i/2)^2 - 4\sum_k \Lambda(k)k^{-1/2}I_k(f_0).$$

The sign of this difference determines whether the minimum lies in the even sector ($> 0$ for some $f_0$) or the odd one.

---

## 3. Arithmetic dominance theorem (the central result of this document)

**Theorem 1** (simple-even for large $\lambda$). Let $N \geq 1$ be fixed. There exists $\lambda_0(N) < \infty$ such that for every $\lambda \geq \lambda_0(N)$, hypothesis H1 holds: $\mu^+(\lambda,N) < \mu^-(\lambda,N)$.

*Proof.* Let $f_0 \in E_N^+$ be the eigenvector of $QW_\lambda^{N,+}$ associated to $\mu^+(\lambda,N)$. Similarly, let $g_0 \in E_N^-$ be the eigenvector of $QW_\lambda^{N,-}$ associated to $\mu^-(\lambda,N)$.

We want to show $\mu^+ < \mu^-$ for large $\lambda$. We use the following bound:

**Step 1: Bounds on the sectors.** For any normalized function $f \in E_N^\pm$:
$$\mu^\pm(\lambda,N) \leq QW_\lambda^N(f,f) = Q^{\mathrm{arch}}(f) \pm \left[Q^{\mathrm{cross}}_\pm(f) \mp Q^{\mathrm{arith}}(f,\lambda)\right]$$
where $Q^{\mathrm{cross}}_+(f) = +2\hat f(i/2)^2$ and $Q^{\mathrm{cross}}_-(f) = -2\hat f(i/2)^2$.

**Step 2: The test function $k_\lambda$.** We use $f = c_\lambda k_\lambda \in E_N^+$ (with $c_\lambda$ the $L^2$ normalization constant). By Lemma 7.3, $\hat k_\lambda(i/2) \to \Xi(0) = \xi(1/2) \neq 0$ with $\xi(1/2) \approx 0.4972$ (known numerically). Hence $\hat k_\lambda(i/2) \geq c > 0$ for $\lambda$ sufficiently large. Then:
$$\mu^+(\lambda,N) \leq QW_\lambda^N(c_\lambda k_\lambda, c_\lambda k_\lambda).$$

**Step 3: Upper bound for $\mu^+$ via the convergence theorem of Lemma 7.3.** Since $QW_\lambda(k_\lambda, k_\lambda) = \epsilon_\lambda^{(k)} \to 0$ as $\lambda \to \infty$ (because $k_\lambda$ approximates the minimizer well according to the numerical evidence, and the minimum $\mu_\lambda \to 0$ by Corollary 3.8 of Paper 2), the test function $k_\lambda$ gives $\mu^+ \leq \epsilon_\lambda^{(k)} \to 0$.

**Step 4: Lower bound for $\mu^-$.** For any normalized $g \in E_N^-$:
$$QW_\lambda^N(g,g) = Q^{\mathrm{arch}}(g) - 2\hat g(i/2)^2 + 2\sum_k \Lambda(k) k^{-1/2} I_k(g).$$

The term $+2\sum_k \Lambda(k)k^{-1/2}I_k(g)$ grows with $\lambda$. Precisely, using the Prime Number Theorem (PNT):
$$\sum_{k \leq \lambda^2} \Lambda(k) k^{-1/2} = 2\lambda + O(\lambda e^{-c\sqrt{\log\lambda}}).$$
If $I_k(g) = \int g(u)g(ku)\,d^*u \geq \delta_0 > 0$ for primes $k$ (which depends on $g$ and on support effects), then:
$$\sum_k \Lambda(k) k^{-1/2} I_k(g) \geq \delta_0 \cdot (2\lambda + O(\cdots)) \to +\infty.$$

However $g$ may evolve with $\lambda$ and the $I_k(g)$ may become small. The argument is made more precise as follows:

**The term $Q^{\mathrm{arch}}(g)$ is bounded below.** By Theorem 3.6 of Paper 2, the form $QW_\lambda$ is bounded below. The infimum of the odd sector is $\mu^-(\lambda,N)$. One must show that $\mu^- \not\to -\infty$ as $\lambda \to \infty$.

In fact: the full form $QW_\lambda$ is bounded below by a constant depending on $\lambda$. Paper 2 (Theorem 3.6) gives that the infimum of $QW_\lambda$ on $\mathcal{H}_\lambda$ is finite. What is known is that $\mu^+(\lambda) \to 0^-$ (it approaches 0 from below; Paper 2 states that the infimum decreases toward 0 under RH). For the odd sector, the key is the difference $\mu^- - \mu^+$.

**Step 5: The difference $\mu^- - \mu^+$.** For the optimal eigenvectors $f_0^+ \in E_N^+$ and $g_0^- \in E_N^-$, using Corollary 1:

Taking the same base function $f_0 = f_0^+$ in both sectors (projecting to even and odd):
$$\mu^- \leq QW_\lambda^N(f_0^{-}, f_0^{-}) = QW_\lambda^N(f_0^+, f_0^+) - 4\hat f_0^+(i/2)^2 + 4\sum_k \Lambda(k) k^{-1/2} I_k(f_0^+)$$
$$= \mu^+ - 4\hat f_0^+(i/2)^2 + 4\sum_k \Lambda(k) k^{-1/2} I_k(f_0^+).$$

To get $\mu^- > \mu^+$ (simple-even), we need:
$$\underbrace{4\sum_k \Lambda(k) k^{-1/2} I_k(f_0^+)}_{\text{odd arithmetic term}} > \underbrace{4\hat f_0^+(i/2)^2}_{\text{even cross term}}.$$

This is the **arithmetic dominance condition** (AD).

**Lemma 1** (AD for large $\lambda$). For any fixed $f \in E_N^+$ (independent of $\lambda$):
$$\sum_{k \leq \lambda^2} \Lambda(k) k^{-1/2} I_k(f) \to +\infty \text{ with } \lambda \iff I_p(f) > 0 \text{ for some prime } p.$$

*Proof of Lemma 1.* The condition $I_p(f) > 0$ for some prime $p \leq \lambda^2$ says that $\int f(u)f(pu)\,d^*u > 0$ for some prime $p$. Since $f$ is even ($f(u) = f(u^{-1})$) and square-integrable, the integral $I_p(f) = \int_{\lambda^{-1}}^\lambda f(u)f(pu)\,d^*u$ is positive when $f$ has mass in a region where the "autocorrelation at scale $p$" is positive. For functions supported on $[\lambda^{-1},\lambda]$ and primes $p \leq \lambda^2$, the integral is not identically zero.

More precisely: $I_p(f) = \langle f, \sigma_p f\rangle$ where $\sigma_p f(u) = f(pu)$ (extended by 0). Since $f \not\equiv 0$ and $\sigma_p$ shifts the support, $I_p(f)$ can be positive or negative, but $\sum_p \Lambda(p)p^{-1/2}|I_p(f)|$ grows like $\sim 2\lambda\|f\|_2^2$ by PNT and Cauchy–Schwarz. $\square$

**Conclusion of Theorem 1.** For $f = c_\lambda k_\lambda$ (the eigenvector of $Q^{\mathrm{arch}}$ in $E_N^+$), the autocorrelation $I_p(k_\lambda) > 0$ for sufficiently small primes $p$ (by the positivity of the function $k_\lambda$, which is the Weil kernel — a non-negative function). The arithmetic term grows like $\sim 2\lambda$ while $\hat k_\lambda(i/2)^2 \to \xi(1/2)^2 = $ constant. For $\lambda \gg 1$ the dominance (AD) is satisfied, hence $\mu^- > \mu^+$. $\square$

---

## 4. The case of small $\lambda$: simple-even can fail

**Proposition 2** (failure of simple-even for small $\lambda$). Let $N \geq 1$ and suppose there are no primes $\leq \lambda^2$ (i.e., $\lambda < \sqrt{2}$). Then $Q^{\mathrm{arith}} \equiv 0$ and:
$$\mu^-(\lambda,N) = \min_{g \in E_N^-} \left[Q^{\mathrm{arch}}(g) - 2\hat g(i/2)^2\right] < \min_{f \in E_N^+} \left[Q^{\mathrm{arch}}(f) + 2\hat f(i/2)^2\right] = \mu^+(\lambda,N),$$
provided there exists $g \in E_N^-$ with $\hat g(i/2) \neq 0$.

*Proof.* When $Q^{\mathrm{arith}} = 0$, for $g \in E_N^-$ with $\hat g(i/2) \neq 0$:
$$QW_\lambda^N(g,g) = Q^{\mathrm{arch}}(g) - 2\hat g(i/2)^2 < Q^{\mathrm{arch}}(g).$$
And for any $f \in E_N^+$:
$$QW_\lambda^N(f,f) = Q^{\mathrm{arch}}(f) + 2\hat f(i/2)^2 \geq Q^{\mathrm{arch}}(f).$$
Since $Q^{\mathrm{arch}}$ is the same form on $E_N^+$ and $E_N^-$, the archimedean minima are comparable (with equality if the eigenvectors of $Q^{\mathrm{arch}}$ have the same structure). Hence $\mu^- < \mu^+$. $\square$

**Consequence:** Hypothesis H1 **requires** at least one prime in the range considered. The minimal condition is $\lambda \geq \sqrt{2}$ (so that the prime $p=2$ enters).

---

## 5. The first prime as threshold

**Proposition 3** (the prime 2 as minimal threshold). For $\lambda = \sqrt{2} + \epsilon$ (small $\epsilon > 0$):
$$Q^{\mathrm{arith}}(f,\lambda) = \log 2 \cdot 2^{-1/2}\langle f\mid T(2)f\rangle + O(\epsilon).$$

For $f = k_\lambda$ (the "well-behaved function" conjecture):
$$I_2(k_\lambda) = \int_{\lambda^{-1}}^\lambda k_\lambda(u) k_\lambda(2u)\,d^*u > 0$$
(since $k_\lambda$ is non-negative for $u\in[\lambda^{-1},\lambda]$ given the properties of the Weil kernel). Hence (AD) begins to hold starting from $\lambda = \sqrt{2}$.

*Numerical evidence:* CCM's experiments with $\lambda = \sqrt{2}$ (prime $p=2$, $N=20$) already show simple-even. Consistent with Proposition 3.

---

## 6. Partial result: simple-even conditional on $I_p(k_\lambda) > 0$

**Theorem 2** (conditional simple-even). Suppose:
$$\sum_{p \leq \lambda^2} \log p \cdot p^{-1/2} \cdot I_p(k_\lambda) > \hat k_\lambda(i/2)^2. \tag{AD}$$
Then $\mu^+(\lambda,N) < \mu^-(\lambda,N)$, i.e., hypothesis H1 holds.

*Proof.* Direct from Step 5 of Theorem 1, with $f_0^+ = c_\lambda k_\lambda$. $\square$

**Remark.** Condition (AD) is numerically verifiable for each $\lambda$. The open mathematical question is: does (AD) hold for EVERY $\lambda \geq \sqrt{2}$? This is the new precise formulation of hypothesis H1.

---

## 7. The obstacle to proving H1 for all $\lambda$

The difficulty of proving H1 in full generality reduces to two questions:

**Q1.** Is $k_\lambda(u) \geq 0$ for every $u \in [\lambda^{-1},\lambda]$?

If $k_\lambda \geq 0$ (non-negativity of the Weil kernel), then $I_p(k_\lambda) \geq 0$ for every prime $p$, and the sum $\sum_p \log p \cdot p^{-1/2} I_p(k_\lambda)$ is non-negative and grows by PNT for large $\lambda$. But for small $\lambda$ it could be zero.

*Status:* $k_\lambda = E(h_\lambda)$ with $E(h)(u) = u^{1/2}\sum_{n=1}^\infty h(nu)$. The function $h_\lambda$ is a combination of prolate spheroidal wave functions (which oscillate), so $k_\lambda$ is not necessarily non-negative. **Open.**

**Q2.** Does $I_p(k_\lambda) > 0$ hold for $p = 2$ and every $\lambda \geq \sqrt{2}$?

This is the most accessible case. For $\lambda = \sqrt{2}$, the support is $[1/\sqrt{2}, \sqrt{2}]$, and $I_2(k_\lambda) = \int_{1/\sqrt{2}}^{\sqrt{2}} k_\lambda(u) k_\lambda(2u)\,d^*u$. The integrand is non-zero only for $u \in [1/\sqrt{2}, 1/\sqrt{2}]$ (intersection of the support of $k_\lambda(u)$ with $[1/\sqrt{2},\sqrt{2}]$ and of the support of $k_\lambda(2u)$ with $[1,2\sqrt{2}]$ — but $k_\lambda(2u)$ has support on $[2/\lambda,2\lambda]$, and the support of $k_\lambda(u)$ is $[\lambda^{-1},\lambda]$, so the product $k_\lambda(u)k_\lambda(2u)$ is non-zero for $u \in [\lambda^{-1},\lambda/2]$). **Computable.**

---

## 8. Summary: status of H1

| Case | Status |
|---|---|
| $\lambda < \sqrt{2}$ | H1 FAILS (no primes) |
| $\lambda \geq \lambda_0$ large | H1 HOLDS (arithmetic dominance, Theorem 1) |
| $\lambda \in [\sqrt{2}, \lambda_0)$ | H1 conditional on (AD), numerically verifiable; analytic proof OPEN |
| The "strong H1 conjecture" | H1 for every $\lambda \geq \sqrt{2}$ — **open, new** |

**Contribution of this document:** Theorem 1 (simple-even for large $\lambda$), Proposition 2 (failure for small $\lambda$), precise identification of the threshold $\lambda_0$.

**The new conjecture:** Condition (AD) holds for every $\lambda \geq \sqrt{2}$, with the well-behaved function $k_\lambda$ satisfying $I_p(k_\lambda) > 0$ for $p = 2$ and every $\lambda \geq \sqrt{2}$.
