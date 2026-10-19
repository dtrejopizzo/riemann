# Phase 29 — Doc 33: Direction A — The Explicit Formula as a Fixed-Point Equation

**Direction:** A (self-reference of the explicit formula)
**Objective:** Investigate whether the Guinand-Weil formula, evaluated at the zeros of $\Xi$, implies $C_\infty(\gamma_n) = 0$ unconditionally — that is, whether the self-referential structure of the explicit formula forces Inc. Inv.

---

## 1. The self-referential structure of the CCM program

**The cycle.** The CCM construction produces the operator $J_\infty$ whose Jacobi coefficients are:

$$b_n^\infty = \gamma_n, \quad a_n^\infty = \frac{\pi}{\log\gamma_n},$$

where $\{\gamma_n\}$ are the imaginary parts of the zeros of $\zeta$ on the critical line. The eigenvalues of $J_\infty$ are the zeros of $C_\infty$, which in turn must be (if Inc. Inv. holds) the same $\{\gamma_n\}$.

This is a **fixed-point equation**: the zeros of $\zeta$ (input of $J_\infty$) = eigenvalues of $J_\infty$ (output).

**Main question.** Is there an argument that forces this fixed-point equation without assuming Inc. Inv. a priori?

---

## 2. The Guinand-Weil formula

**The formula (Barner's form).** For every test function $h: \mathbb{R} \to \mathbb{C}$ in the Schwartz class $\mathcal{S}(\mathbb{R})$:

$$\sum_\rho h\!\left(\frac{\gamma_\rho}{2\pi}\right) = \hat h(0)\log\pi - \frac{1}{2}\hat h(0)\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}\right) + \int_{-\infty}^\infty h(t)\,\frac{d}{dt}\log\!\left|\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right|\,dt$$
$$- \sum_{p \text{ prime}}\sum_{k\geq 1} \frac{\Lambda(p^k)}{p^{k/2}}\!\left[h\!\left(\frac{\log p^k}{2\pi}\right)+h\!\left(-\frac{\log p^k}{2\pi}\right)\right],$$

where the left-hand sum runs over all non-trivial zeros $\rho$ of $\zeta$ (with $\gamma_\rho = \Im(\rho)$), and $\Lambda$ is the von Mangoldt function.

This is an identity between sums over ZEROS and sums over PRIMES.

---

## 3. Evaluation at a zero: attempting the delta function

**Localized test function.** Formally: let $h_\varepsilon(t) = \phi_\varepsilon(t - \gamma_m/(2\pi))$ where $\phi_\varepsilon$ is an approximation to the delta at $t=0$, concentrated as $\varepsilon\to 0$.

In the limit $\varepsilon \to 0$: $h_\varepsilon \to \delta(\cdot - \gamma_m/(2\pi))$, so that:

- Left-hand side: $\sum_\rho h_\varepsilon(\gamma_\rho/(2\pi)) \to \sum_\rho \delta(\gamma_\rho/(2\pi) - \gamma_m/(2\pi)) = \sum_\rho \delta((\gamma_\rho - \gamma_m)/(2\pi))$.

  If the $\gamma_n$ are simple (no repeated zero): the only non-zero term is the one with $\gamma_\rho = \gamma_m$, which gives $2\pi \cdot 1$ (if $\rho_m = 1/2 + i\gamma_m$ is a simple zero) plus its conjugate $\bar\rho_m = 1/2 - i\gamma_m$, which gives another $2\pi$.

  Total left-hand side (under RH): $2 \cdot 2\pi = 4\pi$ (assuming $\gamma_m > 0$; the zero and its conjugate).

- Right-hand side: $[\text{terms from }w] - [\text{prime terms}] = w(\gamma_m) - \Psi(\gamma_m)$.

**The delta identity:** $4\pi = w(\gamma_m) - \Psi(\gamma_m) = C_\infty(\gamma_m) + [\text{normalization terms}]$.

This would give $C_\infty(\gamma_m) = $ a constant $\neq 0$ — NOT zero.

**The problem.** The delta function is not in the Schwartz class: the Weil formula requires $h \in \mathcal{S}(\mathbb{R})$ (rapid decay and smoothness). With $h_\varepsilon \to \delta$, the terms on the right-hand side DIVERGE as $\varepsilon \to 0$. In particular:

$$\sum_{p,k} \frac{\Lambda(p^k)}{p^{k/2}} h_\varepsilon\!\left(\frac{\log p^k}{2\pi}\right) \sim \sum_{p,k} \frac{\Lambda(p^k)}{p^{k/2}} \phi_\varepsilon\!\left(\frac{\log p^k}{2\pi} - \frac{\gamma_m}{2\pi}\right) \to \infty,$$

since the number of prime powers $p^k$ with $\log p^k \approx \gamma_m$ (in the window $[0,2\pi]$) grows like $\varepsilon^{-1}$.

**Conclusion (negative).** Evaluation at a delta is not admissible: the Weil formula diverges for non-Schwartz test functions.

---

## 4. Admissible test functions localized at $\gamma_m$

**Class of substitutes.** Instead of $\delta(\cdot - \gamma_m)$, use test functions of width $\varepsilon > 0$:

$$h_\varepsilon(t) = \varepsilon^{-1}\phi\!\left(\frac{t-\gamma_m/(2\pi)}{\varepsilon}\right),$$

with $\phi \in \mathcal{S}(\mathbb{R})$, $\int \phi = 1$, $\mathrm{supp}\,\phi \subset [-1,1]$.

**Proposition 1** (the Weil formula at scale $\varepsilon$). For $h_\varepsilon$ as above:

$$\text{Left-hand side:} \quad \sum_\rho \varepsilon^{-1}\phi\!\left(\frac{\gamma_\rho - \gamma_m}{2\pi\varepsilon}\right) = \varepsilon^{-1}\phi(0) + \sum_{\rho \neq \rho_m} \varepsilon^{-1}\phi\!\left(\frac{\gamma_\rho - \gamma_m}{2\pi\varepsilon}\right).$$

For small $\varepsilon$: only the zero $\rho_m = 1/2+i\gamma_m$ (and its conjugate) contribute significantly. The sum gives $\approx \varepsilon^{-1}[\phi(0) + \phi(0)] = 2\varepsilon^{-1}\phi(0)$.

**Proposition 2** (the right-hand side at scale $\varepsilon$). The right-hand side has two contributions:

1. Archimedean term: $\int h_\varepsilon(t)\frac{d}{dt}\log|\Gamma(\ldots)|\,dt \approx \frac{d}{dt}\log|\Gamma(\tfrac{1}{4}+\tfrac{it}{2})||_{t=\gamma_m} = w(\gamma_m) + O(\varepsilon)$ (by smoothness of $w$).

2. Prime terms: $\sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}}\varepsilon^{-1}\phi\!\left(\frac{\log p^k/(2\pi) - \gamma_m/(2\pi)}{\varepsilon}\right)$.

   This is the sum of $\varepsilon^{-1}\phi((\log p^k - \gamma_m)/(2\pi\varepsilon))$ over all prime powers $p^k$. In the limit $\varepsilon \to 0$: it behaves like a distribution applied to the "prime spectrum" $\{\log p^k\}$.

**The identity in the limit $\varepsilon \to 0$.**

$$2\varepsilon^{-1}\phi(0) \approx w(\gamma_m) - \varepsilon^{-1}\int_{-\infty}^\infty \phi(u)\,d\Psi_\varepsilon(\gamma_m + 2\pi\varepsilon u),$$

where $\Psi_\varepsilon$ is the prime function smoothed at scale $\varepsilon$.

The two terms of order $\varepsilon^{-1}$ must be equated. If the prime part $\varepsilon^{-1}\int\phi(u)\,d\Psi_\varepsilon = 2\varepsilon^{-1}\phi(0) + \Psi_\varepsilon'(\gamma_m) + O(\varepsilon)$, then:

$$0 = w(\gamma_m) - \Psi_\varepsilon'(\gamma_m) + O(\varepsilon).$$

Taking $\varepsilon \to 0$: $C_\infty(\gamma_m) = w(\gamma_m) - \Psi'_0(\gamma_m) = 0$?

---

## 5. The obstacle: the distributional derivative of $\Psi$

**Definition.** For $\varepsilon > 0$:

$$\Psi_\varepsilon'(t) := \frac{d}{d t}\!\left[\sum_{p,k} \frac{\Lambda(p^k)}{p^{k/2}} \varepsilon^{-1}\hat\phi\!\left(\frac{(t-\log p^k)}{2\pi\varepsilon}\right)\right] = \sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}}\cdot\frac{-1}{2\pi\varepsilon^2}\phi'\!\left(\frac{t-\log p^k}{2\pi\varepsilon}\right).$$

As $\varepsilon \to 0$: $\Psi_\varepsilon'(t) \to \frac{d}{dt}[$ a distribution $]$.

**Proposition 3** (the derivative of $\Psi$ as a distribution). The distributional derivative of $\Psi(t) = 2\sum_{p,k}\Lambda(p^k)p^{-k/2}\cos(t\log p^k)$ is:

$$\Psi'(t) = -2\sum_{p,k}\Lambda(p^k)p^{-k/2}\log(p^k)\sin(t\log p^k).$$

This series ALSO diverges (the terms are $\Lambda(p^k)\log(p^k)p^{-k/2} = (\log p^k)^2 p^{-k/2}$, which is not absolutely summable).

**The negative result.** The condition $w(\gamma_m) - \Psi_\varepsilon'(\gamma_m) = 0$ in the limit $\varepsilon \to 0$ involves the distributional derivative of $\Psi$, which is not well defined as a function. The limit $\varepsilon \to 0$ cannot be taken directly.

---

## 6. The Weil formula as an identity between distributions

**Reinterpretation.** The Weil formula does not say that $C_\infty(\gamma_m) = 0$ for a specific $\gamma_m$. It says that the DISTRIBUTION $\sum_\rho \delta(\gamma - \gamma_\rho)$ (spectral measure of the zeros of $\zeta$) equals a distribution expressed in terms of primes.

The condition $C_\infty(\gamma_m) = 0$ is a POINTWISE statement about $C_\infty$, while the Weil formula is an identity between integral distributions.

**Theorem 1** (what the Weil formula actually gives). The Weil formula establishes:

$$\sum_\rho \langle f, \delta_{\gamma_\rho}\rangle = \langle f, w'\rangle - \sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}}\left[f(\log p^k) + f(-\log p^k)\right]$$

for every $f \in \mathcal{S}(\mathbb{R})$. That is:

$$\mu_\gamma = w' - d\Psi \quad \text{in the distributional sense},$$

where $\mu_\gamma = \sum_\rho \delta_{\gamma_\rho}$ and $d\Psi = \sum_{p,k}\Lambda(p^k)p^{-k/2}[\delta_{\log p^k} + \delta_{-\log p^k}]$ (Dirac measure on the logarithms of prime powers).

**What it does NOT say.** The Weil formula establishes $d\mu_\gamma = w' - d\Psi$ distributionally, but it does NOT say that $w(\gamma_m) - \Psi(\gamma_m) = 0$ for each individual $\gamma_m$. These are objects of a different nature: $w'$ is the derivative of a smooth function, $d\Psi$ is a discrete measure, and the difference is a distribution.

---

## 7. The fixed point from a functional perspective

**Definition of the iteration operator.** Let $\mathcal{F}: \{\text{subsets of } \mathbb{R}\} \to \{\text{subsets of } \mathbb{R}\}$ be the operator:

$$\mathcal{F}(\mathcal{Z}) := \{t \in \mathbb{R}: C_\infty^{\mathcal{Z}}(t) = 0\},$$

where $C_\infty^{\mathcal{Z}}(t) = w(t) - 2\sum_\rho \cos(t\log|\rho|)/|\rho|$ and the sum is over the zeros $\rho$ of $\zeta$ whose imaginary parts are $\mathcal{Z}$.

A fixed point of $\mathcal{F}$ is a set $\mathcal{Z}^*$ such that $\mathcal{F}(\mathcal{Z}^*) = \mathcal{Z}^*$.

**The explicit fixed-point equation.** $\mathcal{Z}^* = \{\gamma_n\}$ if and only if: for each $n$,

$$C_\infty^{\{\gamma_n\}}(\gamma_n) = w(\gamma_n) - 2\sum_m \frac{\cos(\gamma_n\log|\rho_m|)}{|\rho_m|} = 0,$$

where $\rho_m = 1/2 + i\gamma_m$ (under RH) or $\rho_m = \sigma_m + i\gamma_m$ (in general).

**Proposition 4** (the fixed-point equation is Inc. Inv.). The set $\{\gamma_n\}$ is a fixed point of $\mathcal{F}$ if and only if Inc. Inv. holds.

*Proof.* Direct from the definition: $\mathcal{F}(\{\gamma_n\}) = \{\gamma_n\}$ iff each $\gamma_n$ is a zero of $C_\infty^{\{\gamma_n\}} = C_\infty$. But $\{C_\infty=0\} \subseteq \{\gamma_n\}$ (Theorem B, Doc 19), so equality of the sets requires each $\gamma_n$ to be a zero of $C_\infty$, which is exactly Inc. Inv. $\square$

---

## 8. Existence and uniqueness of the fixed point

**Proposition 5** (trivial existence). The empty set $\mathcal{Z}^* = \emptyset$ is a trivial fixed point of $\mathcal{F}$ (vacuously: no $\gamma_n$ satisfying the zero condition). The interesting fixed point is $\mathcal{Z}^* = \{\gamma_n\}$ — the set of zeros of $\Xi$.

**Proposition 6** (uniqueness as a line of attack). If $\mathcal{F}$ has a UNIQUE non-empty fixed point: and if the Weil formula implies that the imaginary parts of the zeros of $\zeta$ form a fixed point of $\mathcal{F}$, then that fixed point is $\{\gamma_n\}$.

**The obstacle for uniqueness.** To show uniqueness of the fixed point of $\mathcal{F}$, one needs:

(a) $\mathcal{F}$ is a contraction (in some suitable metric on discrete subsets of $\mathbb{R}$).

(b) Or: $\mathcal{F}$ has a monotone structure (preserves set order) and has a supremum/infimum fixed point.

Neither of these properties is obvious for $\mathcal{F}$ as defined.

---

## 9. The Weil formula and the self-consistency equation

**Proposition 7** (self-consistency of the Weil formula). The Weil formula, when specialized to $h(t) = e^{ist}$ (exponential function in the "variable $t$"), gives:

$$\sum_\rho e^{is\gamma_\rho} = \hat w(s) - \sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}}\left[e^{is\log p^k} + e^{-is\log p^k}\right] \cdot(\text{scale factor}).$$

The condition $C_\infty(\gamma_m) = 0$ would be written as:

$$w(\gamma_m) = \sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}} \cdot 2\cos(\gamma_m\log p^k).$$

But by the explicit formula (valid for $s = 1/2+i\gamma_m$ a zero of $\zeta$):

$$\sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2+i\gamma_m}} = \sum_\rho \frac{1}{\gamma_m - \gamma_\rho + [\text{pole/trivial terms}]}.$$

This relates the prime side at $t=\gamma_m$ to a sum over ALL zeros $\rho$ (a global "coupling").

**Theorem 2** (what can actually be proved). Under the hypothesis that the zeros of $\zeta$ are SIMPLE and that the prime part of the explicit formula converges absolutely at $s = 1/2 + i\gamma_m$:

$$C_\infty(\gamma_m) = \text{Res}_{s=\rho_m}\!\left(-\frac{\zeta'}{\zeta}(s)\right) \cdot f(\gamma_m) = 1 \cdot f(\gamma_m),$$

where $f(\gamma_m)$ is a factor depending on the normalization. If $f(\gamma_m) = 0$: then $C_\infty(\gamma_m) = 0$ — Inc. Inv. would follow.

**The problem.** The residue $\text{Res}_{s=\rho_m}(-\zeta'/\zeta(s)) = 1$ (for a simple zero of $\zeta$), which is NOT zero. The factor $f(\gamma_m)$ measures whether the residue's contribution CANCELS some other term. Without information about $f$, no conclusion can be drawn.

---

## 10. Attempt via the Hadamard formula for $\Xi$

**The Hadamard factorization of $\Xi$.** The entire function $\Xi(z) = \Xi(0)\prod_n(1-z/\gamma_n)(1+z/\gamma_n)$ (simple zeros on $\mathbb{R}$ under RH). Its logarithmic derivative:

$$\frac{\Xi'(z)}{\Xi(z)} = \sum_n\left(\frac{1}{z-\gamma_n} + \frac{1}{z+\gamma_n}\right).$$

**The Hadamard factorization of $C_\infty$.** By Theorem B (Doc 19): $\{C_\infty=0\} \subseteq \{\Xi=0\} = \{\pm\gamma_n\}$. If we denote by $\{\pm\alpha_j\}$ the zeros of $C_\infty$ (a subset of $\{\pm\gamma_n\}$), then:

$$C_\infty(z) = C_\infty(0)\prod_j\left(1-\frac{z}{\alpha_j}\right)\!\left(1+\frac{z}{\alpha_j}\right) \cdot e^{Q(z)},$$

where $Q(z)$ is an entire function of order $\leq 1$ (the Hadamard exponential factor).

**Inc. Inv. $\Leftrightarrow$ $\{\alpha_j\} = \{\gamma_n\}$ (all zeros of $\Xi$).**

**Proposition 8** (the ratio $C_\infty/\Xi^{2q}$). If $C_\infty(z) = K\cdot\Xi(z)^{2q}\cdot e^{Q(z)}$ for some integer $q \geq 1$: the zeros of $C_\infty$ are the same as those of $\Xi$ (with multiplicity $2q$), and the direct inclusion $\{C_\infty=0\} \subseteq \{\Xi=0\}$ holds with equality. This would give Inc. Inv. if $q \geq 1$.

**The obstacle.** Proving that $C_\infty/\Xi^{2q}$ is entire (or has the form $Ke^{Q}$) without assuming Inc. Inv. requires information about the GROWTH of $C_\infty$ in the complex plane, which in turn requires information about the zeros of $\Xi$ (circular).

---

## 11. Conclusion of Direction A

**Positive result.** The fixed-point structure is identified: Inc. Inv. $\Leftrightarrow$ $\{\gamma_n\}$ is a fixed point of $\mathcal{F}$ (Proposition 4).

**Negative result.** The Weil formula CANNOT be evaluated pointwise at $t = \gamma_m$ (it diverges). The formula gives INTEGRAL information about the distribution of the $\gamma_n$, not pointwise information.

**The central obstacle.** The Weil formula says that the DISTRIBUTION of the zeros $\gamma_n$ is consistent with the distribution of the primes. But it does not say that each individual $\gamma_n$ is a zero of $C_\infty$. Integral (global) information does not imply pointwise (local) information.

**Clarifying analogy.** The law of large numbers says that the average of $n$ random variables converges to the mean. But it says nothing about the value of each individual variable. The Weil formula is analogous: it relates the MEAN of the $\gamma_n$ (in some spectral sense) to the MEAN of the primes, but says nothing about each $\gamma_n$ individually.

**The most promising path from A.** To recover pointwise information from the distributional formula: one needs a "separation principle" stating that if the distribution of the $\gamma_n$ coincides exactly with the distribution of the zeros of $C_\infty$, then the sets are equal. This requires the spectral measures (of $J_\infty$) and that of $\Xi$ to be the SAME measure (not merely to have the same moments). This is precisely the content of the determinacy hypothesis of Doc 26, which turned out to be INDETERMINATE for $\mu_\gamma^{real}$.

**Connection with Doc 26.** The moment problem for $\mu_\gamma^{real}$ is indeterminate (Doc 26), which means that integral information (moments) does NOT determine the measure pointwise. This explains why the path "Weil formula $\Rightarrow$ fixed point $\Rightarrow$ Inc. Inv." cannot be completed: more than moments is needed.

---

*Next doc: Doc 34 — Direction C: Phragmén-Lindelöf for the Quotient $Q$.*
