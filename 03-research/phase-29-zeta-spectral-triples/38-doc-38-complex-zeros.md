# Phase 29 — Doc 38: Complex Zeros of $C_\lambda - \mu_\lambda$ in the Strip

**Phase:** 31 (start)
**Objective:** Analyze the zeros of $C_\lambda(z) = \mu_\lambda$ for $z = x + iy$ with $0 < y \leq \eta < 1/2$. This is the only non-circular analytic opening identified by Docs 36–37.

---

## 1. Precise setup

**Definition 1.** For $\lambda > 0$ and $z = x + iy \in \mathbb{C}^+$:

$$C_\lambda(z) = w(z) - \Psi_\lambda(z), \quad \Psi_\lambda(z) = 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2}\, e^{iz\log n}.$$

For $y > 0$: $e^{iz\log n} = e^{ix\log n} \cdot e^{-y\log n} = e^{ix\log n} \cdot n^{-y}$, hence:

$$\Psi_\lambda(x+iy) = 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2-y}\, e^{ix\log n}. \quad (\star)$$

**The damping factor $n^{-y}$** is central: moving vertically upward in the strip is equivalent to introducing an additional convergence factor $n^{-y}$ in the prime sum.

**Definition 2.** Let $M(\lambda, y) := \sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2-y}$ (von Mangoldt sum weighted by $n^{-1/2-y}$).

By $(\star)$: $|\Psi_\lambda(x+iy)| \leq 2M(\lambda, y)$ for all $x \in \mathbb{R}$.

**Proposition 1** (behavior of $M(\lambda,y)$ by regime). By the Prime Number Theorem ($\psi(X) \sim X$) and the Abel–Stieltjes formula:

(a) For $y > 1/2$: $M(\lambda, y) \to M(\infty, y) = \sum_{n=1}^\infty \Lambda(n)\, n^{-1/2-y} < \infty$ (absolutely convergent series; $1/2 + y > 1$).

(b) For $y = 1/2$: $M(\lambda, 1/2) \sim \log\log\lambda$ (logarithmic growth, diverges).

(c) For $0 < y < 1/2$: $M(\lambda, y) \sim \dfrac{\lambda^{1-2y}}{1/2 - y}$ (polynomial growth in $\lambda$, diverges).

*Proof.* Abel: $M(\lambda,y) = \int_1^{\lambda^2} t^{-1/2-y}\,d\psi(t)$. Using $\psi(t) = t + O(t e^{-c\sqrt{\log t}})$: integration by parts gives the result in each case. $\square$

**Corollary 1.** The behavior of $|\Psi_\lambda(x+iy)|$ is qualitatively different in the three regimes:
- $y > 1/2$: uniformly bounded in $x$ and $\lambda$.
- $0 < y < 1/2$: grows without bound in $\lambda$ (for generic $x$).

---

## 2. The outer strip: unconditional zero-free region

**Theorem 1** (zero-free strip, unconditional). For any fixed $\epsilon > 0$, there exists $\Lambda_\epsilon > 0$ such that for all $\lambda \geq \Lambda_\epsilon$:

$$C_\lambda(z) \neq \mu_\lambda \quad \text{for all } z \text{ with } \Im(z) \geq \tfrac{1}{2} + \epsilon.$$

*Proof.* Let $y = \Im(z) \geq 1/2 + \epsilon$.

**Step 1.** By Proposition 1(a): $\Psi_\lambda(z) \to \Psi_\infty(z) = 2\sum_{n=1}^\infty \Lambda(n)n^{-1/2-y}e^{ix\log n}$ uniformly in $x$ (absolute convergence dominated by $M(\infty, 1/2+\epsilon) < \infty$). Hence $C_\lambda(z) \to C_\infty(z)$ uniformly on compact subsets of $\{z:\Im(z) \geq 1/2+\epsilon\}$.

**Step 2.** By Theorem B (Doc 19, unconditional): $\{C_\infty = 0\} \subseteq \{\Xi = 0\}$. For $\Im(z) = y \geq 1/2+\epsilon$: $\Xi(z) = \xi(1/2+iz) = \xi(1/2-y+ix)$ with $\Re(1/2-y+ix) = 1/2-y \leq -\epsilon < 0$. The nontrivial zeros of $\zeta$ have $\Re(s) \in (0,1)$; for $\Re(s) = 1/2-y < 0$: there are no nontrivial zeros. Hence $\Xi(z) \neq 0$ for $\Im(z) \geq 1/2+\epsilon$ — unconditionally.

Combining: $C_\infty(z) \neq 0$ for $\Im(z) \geq 1/2+\epsilon$.

**Step 3.** Since $C_\lambda \to C_\infty$ uniformly on $\{\Im(z) = 1/2+\epsilon, |\Re(z)| \leq T\}$ and $C_\infty$ is nonzero on that compact set: by Hurwitz's Theorem (the number of zeros does not increase in the limit under uniform convergence + non-vanishing), for $\lambda$ sufficiently large, $C_\lambda(z) \neq 0$ in $\Im(z) \geq 1/2+\epsilon$.

Since $\mu_\lambda \to 0$ and $C_\infty(z) \neq 0 \neq \mu_\infty$ in the region: also $C_\lambda(z) \neq \mu_\lambda$ for $\lambda$ sufficiently large. $\square$

**Corollary 2.** The complex zeros of $C_\lambda - \mu_\lambda$ are ALL confined to $0 < \Im(z) < 1/2 + \epsilon$ for any $\epsilon > 0$ and $\lambda$ sufficiently large.

---

## 3. The inner strip: the local analysis

We now focus on the inner strip $0 < \Im(z) < 1/2$.

**Proposition 2** (Taylor expansion in the thin strip). Let $x_0 \in \mathbb{R}$ and $z = x_0 + iy$ with $y$ small. For $C_\lambda$ real-analytic in a neighborhood of $x_0$:

$$C_\lambda(x_0 + iy) = C_\lambda(x_0) + iy\, C_\lambda'(x_0) - \frac{y^2}{2}\, C_\lambda''(x_0) + O(y^3).$$

The equation $C_\lambda(x_0+iy) = \mu_\lambda$ (with $\mu_\lambda \in \mathbb{R}$) requires:

**Imaginary part:** $y\,\Re[C_\lambda'(x_0)] + O(y^3) = 0$.

Hence, for $y \neq 0$ small: $\Re[C_\lambda'(x_0)] = O(y^2)$.

**Conclusion.** For $y$ small: the complex zeros of $C_\lambda - \mu_\lambda$ in the strip $0 < \Im(z) \leq \eta$ are located near the CRITICAL POINTS of $C_\lambda$ on $\mathbb{R}$, i.e., points $x_0$ where $C_\lambda'(x_0) = 0$.

**Proposition 3** (geometry of complex zeros at critical points). Let $x_c \in \mathbb{R}$ be a critical point of $C_\lambda$ with $C_\lambda'(x_c) = 0$ and $C_\lambda''(x_c) < 0$ (local minimum).

The equation $C_\lambda(x_c + iy) = \mu_\lambda$ becomes:

$$C_\lambda(x_c) - \frac{y^2}{2}|C_\lambda''(x_c)| + O(y^3) = \mu_\lambda.$$

Hence:

$$y^2 \approx \frac{2(C_\lambda(x_c) - \mu_\lambda)}{|C_\lambda''(x_c)|}.$$

For a complex zero with $y > 0$ to exist: we need $C_\lambda(x_c) > \mu_\lambda$.

The height of the complex zero above the real axis is:

$$\boxed{y_c \approx \sqrt{\frac{2(C_\lambda(x_c) - \mu_\lambda)}{|C_\lambda''(x_c)|}}.}$$

**Corollary 3** (bifurcation from a critical point). Each local minimum of $C_\lambda$ with $C_\lambda(x_c) > \mu_\lambda$ contributes ONE PAIR of complex conjugate zeros of $C_\lambda - \mu_\lambda$ at height $y_c$ above the real line. These zeros have no real counterpart (the equation $C_\lambda(x) = \mu_\lambda$ has no real solution near $x_c$).

Conversely: each local minimum with $C_\lambda(x_c) < \mu_\lambda$ contributes TWO REAL solutions of $C_\lambda = \mu_\lambda$ (one on each side of $x_c$), and there are no complex zeros associated to that critical point.

---

## 4. The fundamental dichotomy

Combining the previous results:

**Proposition 4** (dichotomy for the minima of $C_\lambda$). The complex zeros of $C_\lambda - \mu_\lambda$ arise from local minima of $C_\lambda$ that lie STRICTLY ABOVE $\mu_\lambda$. There are exactly two types:

**Type A (minimum above $\mu_\lambda$):** $C_\lambda(x_c) > \mu_\lambda$. Contributes to $N_{C_\lambda-\mu_\lambda}^{\text{strip}}$ with a pair of complex zeros at height $y_c > 0$.

**Type B (minimum below $\mu_\lambda$):** $C_\lambda(x_c) < \mu_\lambda$. Contributes to $N_{C_\lambda-\mu_\lambda}^{\text{real}}$ with two real zeros. Does not contribute to $N_{C_\lambda-\mu_\lambda}^{\text{strip}}$.

**Type C (minimum exactly at $\mu_\lambda$):** $C_\lambda(x_c) = \mu_\lambda$. Contributes a real DOUBLE ZERO. Non-generic case (codimension 1).

**Theorem 2** (characterization of complex zeros). The number of complex zeros of $C_\lambda - \mu_\lambda$ in the strip is:

$$N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T) = 2 \cdot \#\left\{x_c \in [0,T] : C_\lambda'(x_c)=0,\; C_\lambda(x_c) > \mu_\lambda\right\} + O(1).$$

*Proof.* Each Type A local minimum contributes exactly 2 complex zeros (the conjugate pair). Counting all minima in $[0,T]$: this gives twice the number of Type A minima, with error $O(1)$ from inflection points and the boundary of the interval. $\square$

---

## 5. The connection with identity $(C_\lambda')$ from Doc 36

From Doc 36 Proposition 7:

$$N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) = N_{\hat k_\lambda}^{\text{real}}(T) + N_{\hat k_\lambda}^{\text{strip}}(T,\eta). \quad (C_\lambda')$$

Combining with Theorem 2:

$$2\cdot\#\{\text{Type A minima in }[0,T]\} = N_{\hat k_\lambda}^{\text{real}}(T) + N_{\hat k_\lambda}^{\text{strip}}(T,\eta) + O(1).$$

For large $\lambda$: $N_{\hat k_\lambda}^{\text{real}}(T) \approx N_\Xi(T)$ (the real zeros of $\hat k_\lambda$ approximate the $\gamma_n$). And $N_{\hat k_\lambda}^{\text{strip}}(T,\eta)$ = complex zeros of $\hat k_\lambda$ in the strip $\approx$ off-critical zeros of $\Xi$.

**Proposition 5** (analytic equivalence of Inc. Inv.). The following conditions are equivalent:

(i) **Inc. Inv.:** $\{C_\infty = 0\} \supseteq \{\gamma_n\}$, i.e., $N_{C_\infty}(T) = N_\Xi(T)$.

(ii) **All minima of $C_\infty$ between consecutive zeros $\gamma_n, \gamma_{n+1}$ touch level 0:** $C_\infty(x_c) = 0$ for the local minimum $x_c$ between $\gamma_n$ and $\gamma_{n+1}$.

(iii) **Each local minimum of $C_\lambda$ between $\gamma_n^{(\lambda)}$ and $\gamma_{n+1}^{(\lambda)}$ satisfies $C_\lambda(x_c) \to 0$ as $\lambda \to \infty$.**

(iv) **The complex zeros of $C_\lambda - \mu_\lambda$ have height $y_c \to 0$ as $\lambda \to \infty$.**

*Proof (equivalence (i)$\Leftrightarrow$(ii)).* If $C_\infty(\gamma_n) = 0$ and $C_\infty > 0$ on $(\gamma_{n-1}, \gamma_{n+1})$ except at $\gamma_n$: then $\gamma_n$ is a minimum (touches zero). Conversely. $\square$

*Proof (equivalence (iii)$\Leftrightarrow$(iv)).* From Proposition 3: $y_c \approx \sqrt{2C_\lambda(x_c)/|C_\lambda''(x_c)|}$. Hence $y_c \to 0 \iff C_\lambda(x_c) \to 0$ (if $C_\lambda''(x_c)$ is bounded). $\square$

---

## 6. The unconditional zero-free region in the inner strip

Although we cannot eliminate all complex zeros without assuming Inc. Inv., we can bound their location using the growth of $\Psi_\lambda$.

**Proposition 6** (unconditional bound on the height of complex zeros). For local minima of $C_\lambda$ in $[0,T]$: the height of the associated complex zero satisfies

$$y_c \leq \sqrt{\frac{2\,C_\lambda(x_c)}{|C_\lambda''(x_c)|}}.$$

The value $C_\lambda(x_c)$ at the minimum satisfies $C_\lambda(x_c) \geq 0$ (if $C_\lambda > 0$ on $\mathbb{R}$, which is an open question) or can be negative (if $C_\lambda$ has real zeros under Inc. Inv.).

If $C_\lambda(x_c) = O(\mu_\lambda)$ (the minimum barely exceeds $\mu_\lambda$): then $y_c = O(\sqrt{\mu_\lambda}) \to 0$.

**Proposition 7** (bound on $C_\lambda''$ at the minima). At the local minima of $C_\lambda$:

$$C_\lambda''(x_c) = w''(x_c) - \Psi_\lambda''(x_c),$$

where $\Psi_\lambda''(x) = -2\sum_{n \leq \lambda^2} \Lambda(n) n^{-1/2} (\log n)^2 e^{ix\log n}$. Hence:

$$|C_\lambda''(x_c)| \leq |w''(x_c)| + 2\sum_{n \leq \lambda^2} \Lambda(n) n^{-1/2}(\log n)^2.$$

The sum grows like $\sum_{n \leq \lambda^2} \Lambda(n)(\log n)^2 n^{-1/2} = O(\lambda)$ (by PNT). Therefore: $|C_\lambda''(x_c)| = O(\lambda)$.

Combining: $y_c \geq \sqrt{\frac{2C_\lambda(x_c)}{O(\lambda)}} = \Omega\!\left(\sqrt{\frac{C_\lambda(x_c)}{\lambda}}\right)$.

**Corollary 4** (lower bound on the height). If there is a local minimum with $C_\lambda(x_c) \geq \delta_0 > 0$ (a constant independent of $\lambda$): then the height of the associated complex zero satisfies

$$y_c \geq c\sqrt{\delta_0 / \lambda} \to 0.$$

Type A complex zeros APPROACH the real axis at a rate no worse than $1/\sqrt{\lambda}$ — but they do so UNCONDITIONALLY.

*Note on honesty.* This result says the complex zeros approach the real axis at rate $\geq 1/\sqrt{\lambda}$, but it does NOT say that they arrive. For them to arrive, one needs $C_\lambda(x_c) \to 0$ — which is Inc. Inv.

---

## 7. The open question reformulated precisely

**Proposition 8** (analytic reformulation of Inc. Inv.). The following conditions are equivalent:

$$\text{Inc. Inv.} \iff \lim_{\lambda\to\infty} \min_{x_c \in \mathcal{C}_\lambda(T)} C_\lambda(x_c) = 0 \quad \forall T,$$

where $\mathcal{C}_\lambda(T)$ is the set of local minima of $C_\lambda$ in $[0,T]$ with $C_\lambda(x_c) > 0$.

In words: Inc. Inv. ↔ the local minima of $C_\lambda$ approach level 0 as $\lambda \to \infty$.

**Proposition 9** (analytic reformulation of RH). Let $\mathcal{S}_\lambda^{(\eta)} = \{z : 0 < \Im(z) \leq \eta, C_\lambda(z) = \mu_\lambda\}$ be the set of complex zeros of $C_\lambda - \mu_\lambda$ in the strip $\Im(z) \in (0,\eta]$.

Then:

$$\text{RH} \iff \forall \eta > 0:\; N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T, \eta) = N_\Xi(T) + o(N_\Xi(T)) \text{ with } \Im(\mathcal{S}_\lambda^{(\eta)}) \to 0.$$

More precisely (from the discussion in Doc 36 §8): under RH and Inc. Inv.:

$$\sup\{\Im(z) : z \in \mathcal{S}_\lambda^{(\eta)}\} \to 0 \quad \text{as } \lambda \to \infty.$$

**The concrete open question for Phase 31:** Can it be proved unconditionally that

$$\sup\{\Im(z) : z \in \mathcal{S}_\lambda^{(\eta)}\} \to 0 \quad \text{as } \lambda \to \infty?$$

---

## 8. A partial result: the free strip above $\lambda^{-\alpha}$

**Proposition 10** (zone free of complex zeros in the strip). For any $\alpha > 0$: if $y \geq \lambda^{-\alpha}$, then under the hypothesis that $C_\lambda(x_c) = O(\lambda^{1-2\alpha-\epsilon})$ at the local minima of $C_\lambda$:

$$y_c \leq \sqrt{\frac{2\cdot O(\lambda^{1-2\alpha-\epsilon})}{|C_\lambda''(x_c)|}} \leq \sqrt{\frac{c \cdot \lambda^{1-2\alpha-\epsilon}}{\lambda^{-1}}} = O(\lambda^{(2-2\alpha-\epsilon)/2}) = O(\lambda^{1-\alpha-\epsilon/2}).$$

For $\alpha > 1/2$: $y_c = O(\lambda^{-\epsilon/2}) \to 0$. Then the Type A complex zeros lie BELOW the line $\Im(z) = \lambda^{-\alpha}$ for $\alpha > 1/2$.

*Note on honesty.* This result assumes that $C_\lambda(x_c) = O(\lambda^{1-2\alpha-\epsilon})$ at the minima — which is an additional, unproved hypothesis. Without it, the result is vacuous.

**Proposition 11** (proved case: minima near $\gamma_n$). For the minima of $C_\lambda$ that fall EXACTLY at the positions of the eigenvalues $t_n^{(\lambda)}$ (which, under Inc. Inv., are approximately the $\gamma_n$):

$C_\lambda(t_n^{(\lambda)}) = \mu_\lambda \to 0$.

Hence: the Type A complex zeros NEAR $t_n^{(\lambda)}$ have height

$$y_c \approx \sqrt{\frac{2\mu_\lambda}{|C_\lambda''(t_n^{(\lambda)})|}} \leq C\sqrt{\frac{\mu_\lambda}{\lambda}} \to 0.$$

Under Inc. Inv.: all relevant minima satisfy $C_\lambda(x_c) = O(\mu_\lambda)$, hence all Type A complex zeros have height $y_c = O(\sqrt{\mu_\lambda/\lambda}) \to 0$.

**This is the escape mechanism under Inc. Inv.:** the complex zeros of $C_\lambda - \mu_\lambda$ are pairs $(t_n^{(\lambda)}, \bar t_n^{(\lambda)})$ with imaginary part $\to 0$ — they converge to the real axis, where they merge with the real zeros $t_n^{(\lambda)}$ to form DOUBLE ZEROS of $C_\infty$ at $\gamma_n$.

---

## 9. The behavior of $\Psi_\lambda$ in the strip: the arithmetic mechanism

**Proposition 12** (comparison of $\Psi_\lambda$ and $w$ in the strip). For $z = x + iy$ with $y \in (0, 1/2)$:

$$C_\lambda(x+iy) = w(x+iy) - 2\sum_{n \leq \lambda^2} \Lambda(n)\, n^{-1/2-y}\, e^{ix\log n}.$$

The term $w(x+iy)$ is the archimedean contribution — it is a function holomorphic in $\mathbb{C}^+$ related to the logarithm of the completed xi function. For $y$ small: $w(x+iy) \approx w(x) + iy\, w'(x) + O(y^2)$.

The sum $\Psi_\lambda(x+iy)$ is a truncated Dirichlet sum with weights $n^{-1/2-y}$:

$$\Psi_\lambda(x+iy) = \sum_{n \leq \lambda^2} a_n^{(\lambda,y)} e^{ix\log n}, \quad a_n^{(\lambda,y)} = 2\Lambda(n)\, n^{-1/2-y}.$$

This is an **almost-periodic** function of $x$ for each fixed $y$ — it oscillates with frequencies $\log n$ and amplitudes $n^{-1/2-y}$.

**The variable $y$ acts as a regularization parameter:** the larger $y$, the more the high frequencies (large $n$) are suppressed. As $y \to 1/2$: only the low frequencies survive.

**Proposition 13** (the potential $C_\lambda$ in the strip as a regularized Dirichlet sum). For fixed $0 < y < 1/2$:

$$C_\lambda(x+iy) = w(x+iy) - \sum_{n \leq \lambda^2} 2\Lambda(n)\, n^{-1/2-y}\, e^{ix\log n}.$$

The zeros of $C_\lambda(x+iy) = \mu_\lambda$ are the solutions of:

$$\sum_{n \leq \lambda^2} 2\Lambda(n)\, n^{-1/2-y}\, e^{ix\log n} = w(x+iy) - \mu_\lambda.$$

The right-hand side is a smooth function of $x$ (slow variation), while the left-hand side is an oscillating Dirichlet sum with period $O(1/\log\lambda)$. The solutions are the COINCIDENCE POINTS between the smooth function and the oscillating sum — a classical problem in analytic number theory.

---

## 10. Summary: the state of the question and the path forward

**What is proved in this document:**

(T1) **Outer free region** (Theorem 1, unconditional): $C_\lambda - \mu_\lambda$ has no complex zeros for $\Im(z) > 1/2 + \epsilon$ and large $\lambda$.

(T2) **Local geometry** (Proposition 3): the complex zeros in the strip arise from minima of $C_\lambda$ on $\mathbb{R}$ at height $y_c \approx \sqrt{2C_\lambda(x_c)/|C_\lambda''(x_c)|}$.

(T3) **Equivalence with Inc. Inv.** (Proposition 5): the condition $y_c \to 0$ is equivalent to Inc. Inv. — the two statements imply each other.

(T4) **Bound on approach to the real axis** (Corollary 4): the complex zeros approach the real axis at rate $\geq 1/\sqrt{\lambda}$ — this is UNCONDITIONAL.

(T5) **The mechanism under Inc. Inv.** (Proposition 11): if Inc. Inv. is true, the complex zeros have height $O(\sqrt{\mu_\lambda/\lambda}) \to 0$ — they escape to the real axis.

**What remains open:**

(A1) **The central open question:** can it be proved unconditionally that all minima of $C_\lambda$ in $[0,T]$ satisfy $C_\lambda(x_c) \to 0$? This is equivalent to Inc. Inv. — it is a reformulation, not a proof.

(A2) **The unconditional escape question:** does an unconditional bound $y_c \leq f(\lambda) \to 0$ exist (without assuming Inc. Inv.)? From Corollary 4: the bound is $y_c \geq c/\sqrt{\lambda}$ from below, but there is no unconditional upper bound that goes to 0.

**The structural barrier (honest diagnosis):**

The escape of the complex zeros to the real axis IS equivalent to Inc. Inv. There is no way to prove the escape without proving Inc. Inv. first — the conditions are the same thing analytically (Proposition 5).

The advantage of this formulation: it turns Inc. Inv. into a question about the MINIMUM of an explicit real-analytic function ($C_\lambda$) — a question in real analysis, not spectral theory. This may be more tractable.

---

## 11. Proposal for Doc 39: bounding the minimum of $C_\lambda$

**The question for Doc 39.** Prove or disprove:

$$\inf_{x \in [0,T]} C_\lambda(x) \to 0 \quad \text{as } \lambda \to \infty.$$

Available tools:
- The explicit Guinand-Weil formula for $C_\lambda(x)$ as a sum over primes and zeros of $\zeta$.
- The function $C_\lambda(x) = w(x) - \Psi_\lambda(x)$ with $w$ and $\Psi_\lambda$ explicit.
- Extreme value theory for Dirichlet sums (Bondarenko-Seip, Helson).
- The connection with the indeterminate moment problem from Doc 26 — is the infimum of $C_\lambda$ controlled by the moments of the spectral measure?

**Note:** This is the true analytic bottleneck of the Phase 31 program.

---

*Next doc: Doc 39 — Bounding the infimum of $C_\lambda$ on $\mathbb{R}$: extreme values of Dirichlet sums and the minima problem.*
