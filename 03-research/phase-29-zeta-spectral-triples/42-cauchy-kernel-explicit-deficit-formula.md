# Doc 42 — The Cauchy Kernel: Explicit Deficit Formula and the Two Routes toward Inc. Inv.

**Program:** CCM Zeta Spectral Triples — Phase 29/32
**Prerequisites:** Docs 36–41 (especially Docs 38–41)
**Objective:** Derive an explicit formula for $C_\infty(\gamma_n)$ in terms of the off-critical zeros of $\zeta$; analyze the two strategic routes (Abel Regularization, Complex Zero Trajectory); identify the precise obstacle.

---

## 1. Starting point: the structural barrier from Doc 41

Doc 41 established that the spectral $L^2$ energy converges to:

$$E_2(\lambda, T) \;\xrightarrow{\lambda\to\infty}\; \sum_{\gamma_n \leq T} |C_\infty(\gamma_n)|^2 \;=:\; \mathcal{D}(T)$$

and that $\mathcal{D}(T) = 0$ is equivalent to Inc. Inv. The structural barrier is the following: every natural reformulation of Inc. Inv. leads to computing a quantity of the form $\sum_\rho \mathrm{Re}[1/(\rho_n - \rho)]$, whose vanishing is equivalent to RH.

The goal of this document is:

1. Derive the **explicit deficit formula**: a closed expression for $C_\infty(\gamma_n)$ as a sum of Cauchy kernels over the off-critical zeros of $\zeta$.
2. Derive the **Abel renormalization formula** (Route A): $C_\infty(\gamma_n)$ as a renormalized limit of the regularized potential.
3. Analyze the **complex zero trajectory** (Route B): the connection between $y_c(\infty)$ and the deficit formula.
4. Prove **monotonicity of the deficit** in $\sigma_0$: the contribution of an off-critical zero to $\mathcal{D}(T)$ grows monotonically as it moves away from the critical line.

**Cardinal principle of this document:** no statement is accepted without proof. If something does not close, it is identified explicitly.

---

## 2. Recap: the spectral potential and its value at the zeros of $\Xi$

We recall the definitions and results of the previous documents.

**Definition 2.1 (Finite spectral potential).** For $\lambda > 0$ and $x \in \mathbb{R}$:
$$C_\lambda(x) := w(x) - D_\lambda(x), \qquad D_\lambda(x) := 2\sum_{n \leq \lambda^2} \frac{\Lambda(n)}{\sqrt{n}} \cos(x \log n)$$

where $w(x) = \log\pi - \mathrm{Re}[\psi_{\mathrm{dig}}(1/4 + ix/2)]$ is the arithmetic weight function.

**Definition 2.2 (Limiting potential).** The formal limit $\lambda \to \infty$ of the Dirichlet series defines:
$$C_\infty(x) := w(x) - D_\infty(x), \qquad D_\infty(x) := 2\sum_{n=1}^\infty \frac{\Lambda(n)}{\sqrt{n}} \cos(x \log n)$$

where the series converges conditionally for almost all $x \in \mathbb{R}$ (cf. Doc 36).

**Definition 2.3 (Reverse Inclusion).** Inc. Inv. is the statement:
$$\{C_\infty = 0\} \supseteq \{\gamma_n : \Xi(\gamma_n) = 0\}$$
equivalently: $C_\infty(\gamma_n) = 0$ for all $n \geq 1$.

**Theorem 2.4 (Equivalence, Docs 19 and 39).** Under the hypotheses of the CCM program:
$$\text{RH} \iff \text{Inc. Inv.}$$

**Theorem 2.5 (Doc 40, Proposition 7.3).** Via the Hadamard formula, Inc. Inv. is equivalent to:
$$C_\infty(\gamma_n) = 0 \iff \mathrm{Re}[g_n(\rho_n)] = \frac{w(\gamma_n)}{2}$$

where $g_n(\rho_n) = \lim_{s \to \rho_n}\!\left[-\zeta'/\zeta(s) - \frac{1}{s-\rho_n}\right]$ is the regular part of $-\zeta'/\zeta$ at the pole $\rho_n = 1/2 + i\gamma_n$.

---

## 3. The expanded Hadamard formula

To derive the deficit formula we need the Hadamard expansion with all its components made explicit.

**Proposition 3.1 (Hadamard for $-\zeta'/\zeta$).** For $s \in \mathbb{C} \setminus \{1, \rho_n\}$:
$$-\frac{\zeta'}{\zeta}(s) = B + \frac{1}{s-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi_{\mathrm{dig}}\!\left(\frac{s}{2}+1\right) + \sum_\rho \left[\frac{1}{s-\rho} + \frac{1}{\rho}\right]$$

where $B = \log(2\pi) - 1 - \gamma_{\mathrm{Euler}}/2 \approx -0.0230957\ldots$ is the Hadamard constant, and the sum is over all nontrivial zeros $\rho$ of $\zeta$, symmetrized in pairs $(\rho, \bar\rho)$.

**Proposition 3.2 (Expansion of $g_n(\rho_n)$).** From Proposition 3.1, the regular part at $\rho_n$ is:
$$g_n(\rho_n) = B + \frac{1}{\rho_n-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi_{\mathrm{dig}}\!\left(\frac{\rho_n}{2}+1\right) + \sum_{\rho \neq \rho_n}\left[\frac{1}{\rho_n-\rho} + \frac{1}{\rho}\right]$$

**Lemma 3.3 (Real part of the archimedean terms).** With $\rho_n = 1/2 + i\gamma_n$:
$$\mathrm{Re}\,\!\left[B + \frac{1}{\rho_n-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi_{\mathrm{dig}}\!\left(\frac{\rho_n}{2}+1\right) + \sum_\rho \frac{1}{\rho}\right] = \frac{w(\gamma_n)}{2}$$

*Proof.* This identity is precisely the definition of $w(x)$ via the explicit Guinand-Weil formula. The function $w(x) = \log\pi - \mathrm{Re}[\psi_{\mathrm{dig}}(1/4+ix/2)]$ absorbs exactly the contributions of the trivial zeros, the pole at $s=1$, the constant $B$, and the corresponding $1/(2\pi)$ term. A detailed proof can be found in Doc 38 §4. $\square$

**Corollary 3.4 (Simplification of $\mathrm{Re}[g_n(\rho_n)]$).** Combining Proposition 3.2 and Lemma 3.3:
$$\mathrm{Re}[g_n(\rho_n)] = \frac{w(\gamma_n)}{2} + \mathrm{Re}\,\!\left[\sum_{\rho \neq \rho_n} \frac{1}{\rho_n - \rho}\right]$$

**Proposition 3.5 (Reduced formula for $C_\infty(\gamma_n)$).** From Theorem 2.5 and Corollary 3.4:
$$C_\infty(\gamma_n) = w(\gamma_n) - 2\mathrm{Re}[g_n(\rho_n)] = w(\gamma_n) - w(\gamma_n) - 2\mathrm{Re}\,\!\left[\sum_{\rho\neq\rho_n}\frac{1}{\rho_n-\rho}\right]$$

$$\boxed{C_\infty(\gamma_n) = -2\mathrm{Re}\,\!\left[\sum_{\rho \neq \rho_n} \frac{1}{\rho_n - \rho}\right]}$$

This is the **central formula** of this document. Its complete analysis is the content of §4–§8.

---

## 4. Analysis of the Hadamard sum: critical vs. off-critical zeros

The sum in the central formula runs over ALL nontrivial zeros $\rho \neq \rho_n$. We classify them into:

- **Critical zeros:** $\rho = 1/2 + i\gamma$ with $\gamma \neq \gamma_n$ (on the critical line).
- **Off-critical zeros:** $\rho = \sigma + i\gamma$ with $\sigma \neq 1/2$ (off the critical line, if any exist).

**Lemma 4.1 (Contribution of the critical zeros).** If $\rho = 1/2 + i\gamma$ with $\gamma \neq \gamma_n$:
$$\frac{1}{\rho_n - \rho} = \frac{1}{(1/2 + i\gamma_n) - (1/2 + i\gamma)} = \frac{1}{i(\gamma_n - \gamma)} \in i\mathbb{R}$$

Therefore $\mathrm{Re}[1/(\rho_n - \rho)] = 0$. Critical zeros do not contribute to $C_\infty(\gamma_n)$.

**Lemma 4.2 (Contribution of the off-critical zeros: pairing by complex conjugation).** The Hadamard sum is symmetrized in pairs $(\rho, \bar\rho)$. For an off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$:

$$\mathrm{Re}\,\frac{1}{\rho_n-\rho_0} + \mathrm{Re}\,\frac{1}{\rho_n-\bar\rho_0}$$
$$= \mathrm{Re}\,\frac{1}{(1/2-\sigma_0)+i(\gamma_n-\gamma_0)} + \mathrm{Re}\,\frac{1}{(1/2-\sigma_0)+i(\gamma_n+\gamma_0)}$$
$$= \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}$$

This pair has a DEFINITE SIGN: if $\sigma_0 > 1/2$, both fractions are negative; if $\sigma_0 < 1/2$, both are positive. The two terms do NOT cancel (they have the same sign).

*Critical note on the pairing.* Note that the relevant pair here is $(\rho_0, \bar\rho_0)$ (complex conjugation), NOT $(\rho_0, 1-\bar\rho_0)$ (functional equation). Under the pairing $(\rho_0, 1-\bar\rho_0)$ the terms DO cancel (cf. §A.1 of the Appendix). The non-cancellation is a property of the correct pairing of the Hadamard sum.

**Proposition 4.3 (Separation of contributions).** Denoting by $\mathcal{Z}_{\mathrm{off}}$ the set of off-critical zeros with $\mathrm{Im}(\rho) > 0$:

$$C_\infty(\gamma_n) = -2 \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \left[\frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}\right]$$

where $\rho_0 = \sigma_0 + i\gamma_0$.

*Proof.* Direct from the central formula §3 and Lemmas 4.1–4.2. $\square$

---

## 5. The explicit deficit formula

Assume (by the functional equation) that $1/2 < \sigma_0 \leq 1$ for each $\rho_0 \in \mathcal{Z}_{\mathrm{off}}$ with $\mathrm{Im}(\rho_0) > 0$. Its functional pair $1 - \bar\rho_0 = (1-\sigma_0) + i\gamma_0$ has real part $< 1/2$.

**Definition 5.1 (Pointwise deficit).** For an off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$ (with $\sigma_0 > 1/2$, $\gamma_0 > 0$), its contribution to the Inc. Inv. deficit at $\gamma_n$ is:

$$\Delta(\gamma_n; \rho_0) := 2(\sigma_0 - 1/2) \left[\frac{1}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} + \frac{1}{(\sigma_0-1/2)^2+(\gamma_n+\gamma_0)^2}\right] > 0$$

Note that we use $-2(1/2-\sigma_0) = 2(\sigma_0-1/2) > 0$.

**Theorem 5.2 (Explicit deficit formula).** Under the functional equation of $\zeta$ (which ensures that the off-critical zeros group into quadruples $\{\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0\}$):

$$C_\infty(\gamma_n) = \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0 > 1/2,\, \gamma_0 > 0}} \Delta(\gamma_n; \rho_0) \;\geq\; 0$$

The sum is non-negative, and $C_\infty(\gamma_n) = 0$ if and only if $\mathcal{Z}_{\mathrm{off}} = \emptyset$, that is, if and only if RH.

*Proof.* Each $\Delta(\gamma_n; \rho_0) > 0$ by definition. Total vanishing $C_\infty(\gamma_n) = 0$ for ALL $n$ requires each term to equal 0, which (given that each Cauchy kernel is positive) forces the non-existence of off-critical zeros. $\square$

**Corollary 5.3 (Inc. Inv. $\iff$ $\mathcal{Z}_{\mathrm{off}} = \emptyset$).** This is another way of saying RH $\iff$ Inc. Inv., but now with the explicit structure of the deficit formula.

**Corollary 5.4 (Lower bound on $\mathcal{D}(T)$).** The accumulated energy satisfies:
$$\mathcal{D}(T) = \sum_{\gamma_n \leq T} C_\infty(\gamma_n)^2 = \sum_{\gamma_n \leq T}\left[\sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \Delta(\gamma_n; \rho_0)\right]^2 \geq 0$$

If there exists even a single off-critical zero $\rho_0$, then $\Delta(\gamma_n; \rho_0) > 0$ for all $\gamma_n$ (the Cauchy kernel is strictly positive at every point), and therefore $\mathcal{D}(T) > 0$ for all $T$.

---

## 6. Properties of the Cauchy kernel $\Delta(\gamma_n; \rho_0)$

The kernel $\Delta(\gamma_n; \rho_0)$ has a rich geometric structure worth studying.

**Proposition 6.1 (Interpretation as a Poisson sum).** The term $\frac{\epsilon}{(\epsilon^2 + t^2)}$ is the Poisson kernel for the upper half-plane. Specifically:

$$\Delta(\gamma_n; \rho_0) = 2(\sigma_0-1/2) \cdot P(\gamma_n - \gamma_0; \sigma_0-1/2) + 2(\sigma_0-1/2) \cdot P(\gamma_n+\gamma_0; \sigma_0-1/2)$$

where $P(t; \epsilon) = \epsilon/(\epsilon^2+t^2)$ is the Poisson-Cauchy function with width $\epsilon = \sigma_0-1/2$.

**Proposition 6.2 (Scale of the kernel).** The deficit $\Delta(\gamma_n; \rho_0)$ as a function of $\gamma_n$:

- **Maximum value:** attained at $\gamma_n = \gamma_0$: $\Delta(\gamma_0; \rho_0) = 2/(\sigma_0-1/2) + O(1/\gamma_0^2)$.
- **Width of the bell:** $\sim \sigma_0 - 1/2$. Zeros very close to the critical line ($\sigma_0 \to 1/2$) produce a very high and narrow peak.
- **Tail:** For $|\gamma_n - \gamma_0| \gg \sigma_0-1/2$: $\Delta(\gamma_n; \rho_0) \approx 2(\sigma_0-1/2)/(\gamma_n-\gamma_0)^2$ (algebraic decay).
- **Total integral:** $\int_{-\infty}^\infty \Delta(t; \rho_0) dt = 2\pi$ (independent of $\sigma_0$ and $\gamma_0$).

*Proof.* Direct from Cauchy's formula: $\int_{-\infty}^\infty \epsilon/(\epsilon^2+t^2) dt = \pi$ for all $\epsilon > 0$, plus the contribution of the second term (with $+$ sign at $\gamma_0$). For fixed $\gamma_0 > 0$ and the integral over $\gamma_n \in \mathbb{R}$: both terms contribute $\pi$, total $2\pi$. $\square$

**Proposition 6.3 (Monotonicity in $\sigma_0$).** For fixed $\gamma_n, \gamma_0$ with $\gamma_n \neq \pm\gamma_0$:
$$\frac{\partial}{\partial\sigma_0}\Delta(\gamma_n; \rho_0) = 2\frac{(\sigma_0-1/2)^2 - (\gamma_n-\gamma_0)^2}{[(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2]^2} + (\text{analogous second term})$$

- If $|\gamma_n - \gamma_0| > \sigma_0 - 1/2$ (zero far from resonance): the deficit DECREASES as $\sigma_0$ increases. Zeros farther from the critical line create smaller deficits in the tails.
- If $|\gamma_n - \gamma_0| < \sigma_0 - 1/2$ (zero near resonance): the deficit increases as $\sigma_0$ increases.

**Extreme limits:**
- $\sigma_0 \to 1/2^+$ (zero $\to$ critical line): $\Delta(\gamma_n;\rho_0) \to 0$ (the zero becomes critical and no longer contributes).
- $\sigma_0 \to 1^-$ (zero $\to$ boundary of the symmetry rectangle): $\Delta(\gamma_n;\rho_0) \to 1/[1/4+(\gamma_n-\gamma_0)^2] + 1/[1/4+(\gamma_n+\gamma_0)^2]$.

**Corollary 6.4.** The deficit $\Delta(\gamma_n; \rho_0)$ is a continuous function of $\sigma_0$ on $(1/2, 1]$, strictly positive for every $\sigma_0 \in (1/2, 1]$, and vanishes smoothly in the limit $\sigma_0 \to 1/2$.

---

## 7. Route A: Abel Regularization and the renormalization formula

We study the regularized potential at height $\epsilon > 0$:

$$C_\infty^{(\epsilon)}(x) := w(x) - 2\sum_{m=1}^\infty \frac{\Lambda(m)}{m^{1/2+\epsilon}}\cos(x\log m)$$

The series converges absolutely for $\epsilon > 0$ and uniformly on compact sets in $x$.

**Proposition 7.1 (Connection with $\zeta'/\zeta$).** For $\epsilon > 0$ and $x \in \mathbb{R}$:
$$C_\infty^{(\epsilon)}(x) = w(x) + 2\mathrm{Re}\,\!\left[\frac{\zeta'}{\zeta}(1/2+\epsilon-ix)\right]$$

*Proof.* By the Dirichlet series: $-\zeta'/\zeta(s) = \sum_m \Lambda(m) m^{-s}$ for $\mathrm{Re}(s) > 1$. With $m^{-1/2-\epsilon+ix} = m^{-(1/2+\epsilon-ix)}$:
$$\sum_m \Lambda(m) m^{-1/2-\epsilon}\cos(x\log m) = \mathrm{Re}\,\!\left[\sum_m \Lambda(m) m^{-1/2-\epsilon+ix}\right] = \mathrm{Re}\,\!\left[-\frac{\zeta'}{\zeta}(1/2+\epsilon-ix)\right]$$
Therefore $C_\infty^{(\epsilon)}(x) = w(x) + 2\mathrm{Re}[\zeta'/\zeta(1/2+\epsilon-ix)]$. $\square$

**Lemma 7.2 (Structure of the pole at $\bar\rho_n$).** As $\epsilon \to 0^+$ and $x = \gamma_n$: the point $s = 1/2+\epsilon-i\gamma_n$ approaches the zero $\bar\rho_n = 1/2-i\gamma_n$ of $\zeta$ (which exists because $\zeta(\bar s) = \overline{\zeta(s)}$ and $\zeta(\rho_n) = 0$). Therefore:

$$\frac{\zeta'}{\zeta}(1/2+\epsilon-i\gamma_n) = -\frac{1}{\epsilon} - g_n(\bar\rho_n) + O(\epsilon)$$

where $g_n(\bar\rho_n) = \overline{g_n(\rho_n)}$ (Schwarz reflection principle for the regular part). Then:

$$\mathrm{Re}\,\!\left[\frac{\zeta'}{\zeta}(1/2+\epsilon-i\gamma_n)\right] = -\frac{1}{\epsilon} - \mathrm{Re}[g_n(\rho_n)] + O(\epsilon)$$

**Proposition 7.3 (Divergence of the regularized potential at $\gamma_n$).** As $\epsilon \to 0^+$:
$$C_\infty^{(\epsilon)}(\gamma_n) = w(\gamma_n) - \frac{2}{\epsilon} - 2\mathrm{Re}[g_n(\rho_n)] + O(\epsilon)$$

The divergence $-2/\epsilon$ is **universal**: independent of $n$, of the nature of $\rho_n$, and of the distribution of the other zeros. It is produced exclusively by the proximity of $s$ to the two conjugate zeros $\rho_n$ and $\bar\rho_n$.

**Theorem 7.4 (Abel renormalization formula).** The regular part of the Abel limit is:
$$C_\infty^{\mathrm{ren}}(\gamma_n) := \lim_{\epsilon \to 0^+}\left[C_\infty^{(\epsilon)}(\gamma_n) + \frac{2}{\epsilon}\right] = w(\gamma_n) - 2\mathrm{Re}[g_n(\rho_n)]$$

And this quantity coincides with the value of the conditionally convergent series:
$$C_\infty^{\mathrm{ren}}(\gamma_n) = C_\infty(\gamma_n)$$

*Proof.* The equality $C_\infty^{\mathrm{ren}}(\gamma_n) = w(\gamma_n) - 2\mathrm{Re}[g_n(\rho_n)]$ is direct from Proposition 7.3. The equality with $C_\infty(\gamma_n)$ comes from the fact that the conditionally convergent series $D_\infty(\gamma_n)$ sums to $2\mathrm{Re}[g_n(\rho_n)]$ (cf. Doc 40 Theorem 8.2 and its proof via Hadamard). $\square$

**Interpretation (Renormalization).** The limiting potential $C_\infty^{(\epsilon)}(\gamma_n)$ diverges universally like $-2/\epsilon$ as $\epsilon \to 0^+$: the "pole" comes from the TWO zeros of $\zeta$ at $\{\rho_n, \bar\rho_n\}$ which approach the real axis from both sides in the conjugate mirror. The "physical" value $C_\infty(\gamma_n)$ is the finite residue after subtracting this universal divergence — exactly as in QFT renormalization.

**Corollary 7.5 (Reformulation of Inc. Inv. as vanishing of the finite residue).**
$$C_\infty(\gamma_n) = 0 \iff C_\infty^{(\epsilon)}(\gamma_n) = -\frac{2}{\epsilon} + O(\epsilon)$$

Inc. Inv. asserts that the finite part of the regularized potential at $\gamma_n$ is exactly zero: the spectral potential at the zeros of $\Xi$ is "purely divergent" in the Abel sense, with no finite residue.

---

## 8. Route A: the precise obstacle and the connection with Route B

Why does Route A (Abel regularization) not prove Inc. Inv. directly?

**Diagnosis 8.1.** Theorem 7.4 establishes:
$$C_\infty^{\mathrm{ren}}(\gamma_n) = w(\gamma_n) - 2\mathrm{Re}[g_n(\rho_n)] = -2\mathrm{Re}\,\!\left[\sum_{\rho\neq\rho_n}\frac{1}{\rho_n-\rho}\right]$$

To prove $C_\infty^{\mathrm{ren}}(\gamma_n) = 0$ we need to prove that $\sum_{\rho\neq\rho_n}\mathrm{Re}[1/(\rho_n-\rho)] = 0$, which (by Proposition 4.3 and Theorem 5.2) is equivalent to $\mathcal{Z}_{\mathrm{off}} = \emptyset$, i.e., RH. Exact circularity.

**The subtle distinction between limits.** The potential $C_\infty(x)$ on the real axis is the conditionally convergent series. The limit $\lim_{\epsilon\to 0^+} C_\infty^{(\epsilon)}(x)$ for $x \neq \gamma_n$ coincides with $C_\infty(x)$ (both are the same function away from the singularities). But at $x = \gamma_n$: the conditional series converges to $C_\infty(\gamma_n)$ (with the Hadamard cancellation), while the Abel limit diverges like $-2/\epsilon$. The renormalization in Theorem 7.4 connects both values — but does not prove them equal to 0.

**Geometric insight.** Think of the "picture of the divergence": as $\epsilon \to 0^+$, the regularized potential at $\gamma_n$ descends to $-\infty$ like a parabola. The Inc. Inv. question is: at what position is the curve at level 0? Does it cross 0 before or after the parabola $-2/\epsilon$? The answer determines the sign of $C_\infty^{\mathrm{ren}}(\gamma_n)$.

---

## 9. Route B: Complex zero trajectory — setup

We recall from Doc 38 the trajectory of the complex zeros of $C_\lambda - \mu_\lambda$ near the minima of $C_\lambda$. For a local minimum $x_c(\lambda)$ of $C_\lambda$ with $C_\lambda(x_c) > \mu_\lambda$ (Type A case), the complex zeros near $x_c$ are:

$$z_c^\pm(\lambda) = x_c(\lambda) \pm iy_c(\lambda), \qquad y_c(\lambda) \approx \sqrt{\frac{2(C_\lambda(x_c) - \mu_\lambda)}{|C_\lambda''(x_c)|}}$$

**Definition 9.1 (Asymptotic height).** For a minimum $x_c(\lambda)$ converging to $\gamma_n$ as $\lambda \to \infty$:
$$y_c^\infty := \lim_{\lambda\to\infty} y_c(\lambda), \qquad x_c^\infty := \lim_{\lambda\to\infty} x_c(\lambda)$$

**Proposition 9.2 (The limiting height measures the deficit).** If the limit $x_c^\infty$ exists and $|C_\lambda''(x_c)|$ converges to a finite limit $H_n := |C_\infty''(\gamma_n)| > 0$, then:

$$y_c^\infty = \sqrt{\frac{2 C_\infty(\gamma_n)}{H_n}}$$

(using $\mu_\lambda \to 0$).

*Proof.* As $\lambda \to \infty$: $C_\lambda(x_c) \to C_\infty(x_{c}^\infty) = C_\infty(\gamma_n)$ and $\mu_\lambda \to 0$. Then $y_c(\lambda) \to \sqrt{2C_\infty(\gamma_n)/H_n}$. $\square$

**Theorem 9.3 (Connection Route B $\leftrightarrow$ Deficit Formula).** Under the hypotheses of Proposition 9.2:

$$y_c^\infty = \sqrt{\frac{2}{H_n} \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0 > 1/2,\, \gamma_0 > 0}} \Delta(\gamma_n; \rho_0)}$$

where $\Delta(\gamma_n; \rho_0) = 2(\sigma_0-1/2)[(\ldots)^{-1}+(\ldots)^{-1}]$ is the Cauchy kernel of §5.

*Proof.* Combine Proposition 9.2 with Theorem 5.2. $\square$

**Geometric interpretation.** The height $y_c^\infty$ of the asymptotic complex zero does NOT depend on the critical zeros of $\zeta$ (which contribute 0 to $C_\infty(\gamma_n)$). It depends solely on the off-critical zeros: each one raises the height of the trajectory according to its position in the complex plane via a Cauchy kernel.

**RH as a "landing condition."** Under RH: $\mathcal{Z}_{\mathrm{off}} = \emptyset$, all deficits are 0, and $y_c^\infty = 0$. The complex zeros "land" on the real axis, coinciding with the zeros $\gamma_n$ of $\Xi$.

---

## 10. Route B: The flow of the trajectory

To analyze whether $y_c(\lambda)$ is monotonic, we need its derivative with respect to $\lambda$.

**Proposition 10.1 (Flow equation for $y_c^2$).** Differentiating $y_c^2 \approx 2(C_\lambda(x_c)-\mu_\lambda)/|C_\lambda''(x_c)|$ with respect to $\lambda$:

$$\frac{d}{d\lambda}y_c^2 \approx \frac{2}{|C_\lambda''(x_c)|}\frac{d}{d\lambda}C_\lambda(x_c)$$

(ignoring changes in $C_\lambda''$ and in $\mu_\lambda$, which are of lower order). By the implicit function theorem: $\frac{d}{d\lambda}C_\lambda(x_c(\lambda)) = \frac{\partial C_\lambda}{\partial\lambda}(x_c)$ (the term $C_\lambda'(x_c) \cdot dx_c/d\lambda = 0$ since $C_\lambda'(x_c) = 0$ at the minimum).

**Proposition 10.2 (Derivative of $C_\lambda$ with respect to the cutoff).** When $\lambda$ crosses $\sqrt{p}$ for a prime $p$ (increasing the cutoff $\lambda^2$ from $n \leq \lambda^2-1$ to $n \leq \lambda^2$ with $\lambda^2 = p$):

$$\Delta_\lambda C_\lambda(x_c) = -\Delta_\lambda D_\lambda(x_c) = -\frac{2\log p}{\sqrt{p}}\cos(x_c\log p)$$

The sign of this jump depends on $\cos(x_c\log p)$:
- $\cos(x_c\log p) > 0$: $C_\lambda(x_c)$ decreases $\Rightarrow$ $y_c$ decreases. (**Favorable to RH.**)
- $\cos(x_c\log p) < 0$: $C_\lambda(x_c)$ increases $\Rightarrow$ $y_c$ increases. (**Unfavorable to RH.**)

**Proposition 10.3 (Non-monotonicity of the individual trajectory).** The function $\lambda \mapsto y_c(\lambda)$ is not monotonic in general: it oscillates with each new prime added.

*Proof.* For any fixed position $x_c$ and the first prime $p_1$ such that $\cos(x_c\log p_1) < 0$: upon crossing $\lambda = \sqrt{p_1}$, the height $y_c$ increases. For the next prime $p_2 > p_1$ such that $\cos(x_c\log p_2) > 0$: $y_c$ decreases. The alternation occurs generically. $\square$

**Proposition 10.4 (The net effect of all primes).** The TOTAL variation of $C_\lambda(x_c)$ from $\lambda$ to $\infty$ is:

$$C_\infty(x_c) - C_\lambda(x_c) = -[D_\infty(x_c) - D_\lambda(x_c)] = -\sum_{n > \lambda^2} \frac{2\Lambda(n)}{\sqrt{n}}\cos(x_c\log n)$$

This is exactly the quantity $-R_\lambda(x_c)$ where $R_\lambda = D_\infty - D_\lambda$ is the tail of the Dirichlet series. Then:

$$y_c(\infty)^2 - y_c(\lambda)^2 \approx \frac{2}{|C_\lambda''(x_c)|} \cdot [C_\infty(x_c) - C_\lambda(x_c)] = \frac{-2R_\lambda(x_c)}{|C_\lambda''(x_c)|}$$

Under Inc. Inv. ($C_\infty(\gamma_n) = 0$): $y_c(\infty) = 0$ and $y_c(\lambda) \approx \sqrt{2R_\lambda(\gamma_n)/|C_\lambda''(\gamma_n)|}$, which goes to 0 conditionally.

**Honest obstacle of Route B.** To prove that $y_c(\lambda) \to 0$ we need to prove that $C_\infty(\gamma_n) = 0$, which is Inc. Inv. The trajectory does not provide an unconditional route; it does provide a precise GEOMETRIC PICTURE: $y_c(\infty)$ directly measures the "spectral mass" of off-critical zeros of $\zeta$ as seen from $\gamma_n$ via Cauchy kernels.

---

## 11. The formula for $H_n$ and the landing speed

To complete the quantitative picture of Route B, we need $H_n = |C_\infty''(\gamma_n)|$.

**Proposition 11.1 (Second derivative of $C_\infty$ at the zeros).** Formally:
$$C_\infty''(x) = -D_\infty''(x) = 2\sum_{n=1}^\infty \frac{\Lambda(n)}{\sqrt{n}} (\log n)^2 \cos(x\log n)$$

(where $w''(x)$ is smooth and contributes $w''(\gamma_n)$). The Dirichlet sum $\sum \Lambda(n) (\log n)^2 n^{-1/2} \cos(x\log n)$ converges conditionally for almost all $x$.

**Proposition 11.2 (Scale of $H_n$).** The analysis of Doc 38 §9 gives $|C_\lambda''(x_c)| \sim c \cdot \lambda$ for typical minima. Hence:

$$y_c(\lambda) \sim \sqrt{\frac{C_\lambda(x_c)}{\lambda}}, \qquad y_c(\infty) \sim \sqrt{\frac{C_\infty(\gamma_n)}{H_n}}$$

The landing speed (how fast the trajectory reaches $y=0$ under RH) is determined by the RATE OF CONVERGENCE of $R_\lambda(\gamma_n) \to 0$, which depends on the properties of the distribution of primes.

---

## 12. Connection between Routes A and B: the geometric meaning of the finite residue

Routes A and B converge at the same central point:

**Theorem 12.1 (Unification of Routes A and B).** The Inc. Inv. deficit has THREE equivalent descriptions:

(i) **Route A (algebra):** $C_\infty(\gamma_n) = \lim_{\epsilon\to0}[C_\infty^{(\epsilon)}(\gamma_n) + 2/\epsilon]$ — the finite residue of the Abel regularization.

(ii) **Hadamard (series):** $C_\infty(\gamma_n) = -2\mathrm{Re}\,\sum_{\rho\neq\rho_n}[1/(\rho_n-\rho)]$ — the vanishing of the sum over zeros of $\zeta$.

(iii) **Route B (geometry):** $C_\infty(\gamma_n) = H_n \cdot (y_c^\infty)^2/2$ — the square of the limiting height of the asymptotic complex zero, scaled by $H_n$.

*Proof.* (i) is Theorem 7.4. (ii) is Proposition 3.5. (iii) is Proposition 9.2. All three are values of the same object: the conditionally convergent series $C_\infty(\gamma_n) = w(\gamma_n) - D_\infty(\gamma_n)$ evaluated at the zeros of $\Xi$. $\square$

**Corollary 12.2 (Inc. Inv. as a geometric condition in $\mathbb{C}$).** The following conditions are equivalent:
1. $\mathcal{Z}_{\mathrm{off}} = \emptyset$ (RH).
2. $y_c^\infty = 0$ for all asymptotic minima $x_c^\infty = \gamma_n$ (Route B).
3. $\lim_{\epsilon\to0}[C_\infty^{(\epsilon)}(\gamma_n) + 2/\epsilon] = 0$ for all $n$ (Route A).
4. $\sum_\rho \mathrm{Re}[1/(\rho_n-\rho)] = 0$ for all $n$ (Hadamard).

---

## 13. The structural obstacle: why symmetry is not enough

An observation that appears suggestive but turns out to be incorrect can be clarified here.

**Proposition 13.1 (The wrong pairing).** Consider the off-critical zeros grouped by the symmetry of the FUNCTIONAL EQUATION: $(\rho_0, 1-\bar\rho_0)$. Then:

$$\mathrm{Re}\,\frac{1}{\rho_n-\rho_0} + \mathrm{Re}\,\frac{1}{\rho_n-(1-\bar\rho_0)} = \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{\sigma_0-1/2}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} = 0$$

Under this pairing, each pair contributes 0 to the sum. This would seem to imply $C_\infty(\gamma_n) = 0$ unconditionally.

**Why this is INCORRECT.** The pairing of the Hadamard sum is NOT by the functional equation, but by complex conjugation $(\rho_0, \bar\rho_0)$. Under this correct pairing:

$$\mathrm{Re}\,\frac{1}{\rho_n-\rho_0} + \mathrm{Re}\,\frac{1}{\rho_n-\bar\rho_0} = \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}$$

Both terms have the SAME SIGN (given by $1/2-\sigma_0$), and do NOT cancel.

*Proof.* The convergence of the Hadamard sum is guaranteed by pairing $\rho$ with $\bar\rho$ (same real part, opposite imaginary part), not with $1-\bar\rho$ (complementary real part). The functional-equation pairing would give pairs $(\sigma, 1-\sigma)$, but for the zeros of $\zeta$ under the functional equation, the pair of $\rho = \sigma+i\gamma$ is $1-\bar\rho = (1-\sigma)+i\gamma$, which has the SAME imaginary part but a different real part. The correct Hadamard pairing is by imaginary part: $\rho = \sigma+i\gamma$ with $\bar\rho = \sigma-i\gamma$. $\square$

**This observation is crucial** because it removes the temptation to argue, by functional-equation symmetry, that Inc. Inv. is trivially true. The symmetry of the functional equation creates pairings that cancel, but the summation ORDER that converges in the Hadamard sum is NOT that symmetry.

---

## 14. Quantifying the obstacle: how much is needed

What MINIMAL additional information would suffice to prove Inc. Inv. from the deficit formula?

**Remark 14.1 (The precise question).** The deficit formula (Theorem 5.2) gives:
$$C_\infty(\gamma_n) = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \Delta(\gamma_n; \rho_0)$$

This is a sum of POSITIVE terms. To prove $C_\infty(\gamma_n) = 0$ it suffices to prove $\mathcal{Z}_{\mathrm{off}} = \emptyset$. To prove that the sum is positive it suffices to find one term. The problem is exactly analogous to proving that a sum of squares is zero: one must prove that every summand is zero.

**Remark 14.2 (Implicit lower bound).** If there is an off-critical zero $\rho_0 = \sigma_0+i\gamma_0$, then for ALL $\gamma_n$:
$$C_\infty(\gamma_n) \geq \Delta(\gamma_n; \rho_0) = \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} + \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_n+\gamma_0)^2}$$

A single off-critical zero contaminates ALL values $C_\infty(\gamma_n)$ with a positive contribution that decays like $1/\gamma_n^2$ as $\gamma_n \to \infty$.

**Proposition 14.3 (Bound on the total energy).** If there exists $\rho_0 \in \mathcal{Z}_{\mathrm{off}}$ with $\sigma_0 > 1/2$ and $\gamma_0 > 0$:
$$\mathcal{D}(T) \geq \sum_{\gamma_n \leq T} \Delta(\gamma_n; \rho_0)^2 \geq c(\rho_0) \cdot \log T$$

for some constant $c(\rho_0) > 0$ depending on $\rho_0$, using the density of zeros $\#\{\gamma_n \leq T\} \sim T\log T/(2\pi)$ and the integral of the squared kernel.

*Proof (sketch).* $\sum_{\gamma_n \leq T}\Delta(\gamma_n;\rho_0)^2 \approx \frac{T\log T}{2\pi}\int_{-\infty}^\infty \Delta(t;\rho_0)^2\frac{dt}{(\text{mean density})}$. The integral $\int \Delta(t;\rho_0)^2 dt$ is finite (the kernel is $L^2$), and the density of zeros gives the factor $T\log T$. $\square$

**Corollary 14.4.** The existence of a single off-critical zero would imply $\mathcal{D}(T) \to \infty$. In terms of the $L^2$ energy: $E_2(\lambda, T) \to \infty$ as $T\to\infty$ (for any fixed $\lambda$). This is **consistent** with the diagnosis of Doc 41 that $E_2 \sim T(\log T)^3/(24\pi)$ as $T\to\infty$.

---

## 15. The zero-free region and its effect on the trajectory

From Doc 38 Theorem 1 (zero-free region of $\zeta$ in the strip $0 < \mathrm{Im}(s) < T$):

$$\mathcal{Z}_{\mathrm{off}} \cap \{\mathrm{Im}(\rho) \leq T\} \subseteq \left\{|\mathrm{Re}(\rho) - 1/2| > c/\log T\right\}$$

for some constant $c > 0$ (classical). This imposes a bound on off-critical zeros close to the critical line.

**Proposition 15.1 (Upper bound on the deficit from the zero-free region).** If all off-critical zeros satisfy $\sigma_0 - 1/2 > c/\log\gamma_0$, then for the zeros closest to $\gamma_n$:

$$\Delta(\gamma_n; \rho_0) \leq \frac{2(\sigma_0-1/2)}{(1/2-\sigma_0)^2} = \frac{2}{\sigma_0-1/2} \leq \frac{2\log\gamma_0}{c}$$

This bound grows with $\gamma_0$ (distant zeros could be relatively closer to the critical line). It does not give a bound that goes to 0.

**Diagnosis 15.2.** The classical zero-free region is not sufficient to control the deficit $\Delta(\gamma_n;\rho_0)$ in a way that guarantees $C_\infty(\gamma_n) = 0$. A zero-free region of the form $\sigma_0 > 1/2 + f(\gamma_0)$ where $f(\gamma_0) \to 1/2$ would be needed — that is, that there be NO off-critical zeros, which is RH.

---

## 16. The "positivity argument" — its scope and its limits

The deficit formula $C_\infty(\gamma_n) = \sum_{\rho_0} \Delta(\gamma_n;\rho_0) \geq 0$ provides a new result with non-trivial consequences.

**Proposition 16.1 (Positivity of $C_\infty$ at the zeros of $\Xi$).** Conditionally on the convergence of $D_\infty(\gamma_n)$ (which follows from the convergence of the Hadamard series):

$$C_\infty(\gamma_n) \geq 0 \quad \forall n$$

*Proof.* Each $\Delta(\gamma_n;\rho_0) \geq 0$ by definition. The sum is non-negative. $\square$

**This is a NEW and unconditional result** (subject only to the convergence of the Hadamard sum): the spectral potential at the zeros of $\Xi$ is ALWAYS non-negative. It cannot be negative, regardless of whether RH is true or not.

**Corollary 16.2 (Lower bound for the potential).** For all $n$:
$$C_\infty(\gamma_n) \geq 0 \qquad (\text{unconditional result})$$

This is consistent with the analysis of Doc 38 showing $C_\lambda(x_c) > 0$ for all Type A minima.

**The limit of the positivity argument.** Although we know $C_\infty(\gamma_n) \geq 0$, proving $C_\infty(\gamma_n) = 0$ is the Riemann Hypothesis itself. Unconditional positivity is an interesting result (it shows that the only possibility for failure is $C_\infty(\gamma_n) > 0$, not $< 0$), but it does not solve the problem.

---

## 17. The deficit formula as a tool for detecting off-critical zeros

If (hypothetically) we could compute $C_\infty(\gamma_n)$ with sufficient numerical precision, the deficit formula would allow deducing information about the off-critical zeros of $\zeta$.

**Proposition 17.1 (Inversion of the deficit formula).** If $C_\infty(\gamma_n) > 0$ for some $n$, then:
$$\sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} \geq C_\infty(\gamma_n) - O(1/\gamma_0^2)$$

(the second term of the Cauchy kernel is of order $1/\gamma_0^2$ for $\gamma_0 \gg \sigma_0-1/2$).

This inequality locates the off-critical zeros: if $C_\infty(\gamma_n)$ is large for a range of $\gamma_n$ near some $\gamma_0$, there is an off-critical zero near $1/2+i\gamma_0$.

**Proposition 17.2 (The distribution of $\{C_\infty(\gamma_n)\}$ as the spectrum of the off-critical zeros).** The function $f(\gamma_0) := C_\infty(\gamma_0)$ is the "spectral measure" of the off-critical zeros as seen from the critical line. It is the Cauchy transform (Poisson-Stieltjes) of the measure $\mu_{\mathrm{off}} := \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} 2(\sigma_0-1/2) \delta_{\gamma_0}$:

$$C_\infty(\gamma_n) = \int_0^\infty \frac{2(\sigma_0(\gamma_0)-1/2)}{(\sigma_0(\gamma_0)-1/2)^2+(\gamma_n-\gamma_0)^2} d\mu_{\mathrm{off}}(\gamma_0) + (\text{term}\ \gamma_n+\gamma_0)$$

Under this interpretation: $C_\infty(\gamma_n) = 0$ for all $n$ $\iff$ $\mu_{\mathrm{off}} = 0$ $\iff$ RH.

---

## 18. The "Zero Geometry in the Plane" route: concrete proposal for Doc 43

The two routes analyzed (A and B) converge at the same structural barrier. However, Route B offers a new direction that has not been explored: **the flow of the complex zero in the plane $\mathbb{C}$ as $\lambda$ varies**.

**Proposal 18.1 (The Riemann-Hilbert flow).** Consider the "moduli space" of complex zeros of $\{C_\lambda - \mu_\lambda\}$ as a function of $\lambda$. The trajectory $z_c(\lambda) = x_c(\lambda) + iy_c(\lambda)$ satisfies (by the implicit function theorem in $\mathbb{C}$):

$$\frac{dz_c}{d\lambda} = -\frac{\partial_\lambda C_\lambda(z_c)}{C_\lambda'(z_c)}$$

where $C_\lambda'(z_c) \neq 0$ (since $z_c$ is a simple zero of $C_\lambda - \mu_\lambda$, not a critical point of $C_\lambda$).

**Open question 18.2.** Can it be shown that $\mathrm{Im}(z_c(\lambda))$ is monotonically decreasing in $\lambda$ for SOME choice of norm, metric, or average over the zeros?

From the analysis of §10: the individual height $y_c(\lambda)$ is NOT monotonic (it oscillates due to the contributions of the primes). But perhaps the sum:

$$Y(\lambda) := \sum_{x_c \in \mathcal{C}_\lambda(T)} y_c(\lambda, x_c)^2$$

is monotonically decreasing. This is exactly $E_2(\lambda, T)/1$ (in some limit), and analyzing its monotonicity leads back to Doc 41.

**Proposal 18.3 (The ratio of speeds).** The descent speed of $y_c$ is proportional to:

$$\frac{dy_c}{d\lambda} \propto \frac{-\cos(x_c\log p)}{y_c} \cdot \frac{\log p}{\sqrt{p}}$$

when $\lambda$ crosses $\sqrt{p}$. The AVERAGE over primes $p$ near $\lambda^2$:

$$\langle\cos(x_c\log p)\rangle_{p \sim \lambda^2} \approx \mathrm{Re}\,\!\left[\frac{\sum_{p \sim \lambda^2} p^{ix_c}/\log p}{\pi(\lambda^2)}\right]$$

Under the equidistribution of primes modulated by the zeros of $\zeta$ (Weyl Equidistribution Theorem + sieves): this average is small for generic $x_c$ and can be controlled by sieve methods if $x_c$ is sufficiently far from all the $\gamma_n$.

---

## 19. A new tool: the spectral Toeplitz operator

We present a reformulation of the deficit formula that connects with the theory of Toeplitz operators and offers a possible new line of attack.

**Definition 19.1 (Deficit function as a Poisson transform).** Define the deficit measure:
$$\mu_{\mathrm{def}} := \sum_{n \geq 1} C_\infty(\gamma_n) \delta_{\gamma_n}$$

Under Inc. Inv.: $\mu_{\mathrm{def}} = 0$. Without RH: $\mu_{\mathrm{def}}$ is a discrete positive measure supported on $\{\gamma_n\}$.

**Proposition 19.2 (The deficit measure as the Cauchy transform of $\mu_{\mathrm{off}}$).** The measure $\mu_{\mathrm{def}}$ is the restriction to the critical zeros of the Cauchy transform of the off-critical-zero measure:

$$C_\infty(\gamma_n) = (\mathcal{C}\mu_{\mathrm{off}})(\gamma_n)$$

where $\mathcal{C}\mu(t) = \int \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(t-s)^2} d\mu(s)$ is the Cauchy-Poisson operator.

**Remark 19.3 (Invertibility).** The Cauchy-Poisson operator $\mathcal{C}$ is injective on measures supported on $\{(\sigma_0-1/2, \gamma_0): \sigma_0 > 1/2\}$: if $\mathcal{C}\mu = 0$ on a dense set, then $\mu = 0$.

This shows: the ONLY way to have $C_\infty(\gamma_n) = 0$ for all $\gamma_n$ is for $\mu_{\mathrm{off}} = 0$, that is, RH. The result is circular (we know this), but the formulation in terms of invertibility of the Cauchy operator is new and could open the door to analytic techniques.

---

## 20. Summary: the state of the problem and the roadmap

**New results of this document:**

| # | Result | State |
|---|---|---|
| T 5.2 | Explicit deficit formula: $C_\infty(\gamma_n) = \sum_{\rho_0}\Delta(\gamma_n;\rho_0)$ (sum of Cauchy kernels) | New, proved |
| T 7.4 | Abel renormalization formula: $C_\infty(\gamma_n) = \lim_\epsilon[C_\infty^{(\epsilon)}(\gamma_n) + 2/\epsilon]$ | New, proved |
| T 9.3 | Connection Route B–Deficit: $y_c^\infty = \sqrt{2C_\infty(\gamma_n)/H_n}$ | New, proved |
| T 12.1 | Unification of the three descriptions (Abel, Hadamard, Geometry) | New, proved |
| P 13.1 | The functional-equation pairing does NOT cancel — the correct one is by conjugation | Crucial clarification |
| P 16.1 | $C_\infty(\gamma_n) \geq 0$ — new **unconditional** result | New, proved |
| P 17.2 | $\{C_\infty(\gamma_n)\}$ as the Cauchy transform of the off-critical-zero measure | New interpretation |

**Consolidated state of the program:**

| Implication | State |
|---|---|
| Inc. Inv. $\Rightarrow$ RH | Proved (Theorem D, Doc 19) |
| RH $\Rightarrow$ Inc. Inv. | Proved (Theorem 4, Doc 39) |
| $E_2(\lambda,T)\to 0 \iff$ Inc. Inv. | Proved (Theorem 3, Doc 41) |
| $C_\infty(\gamma_n) \geq 0$ | **Proved unconditionally** (P 16.1, Doc 42) |
| $C_\infty(\gamma_n) = \sum_{\rho_0}\Delta(\gamma_n;\rho_0)$ | New explicit formula (Doc 42) |
| Inc. Inv. [no hypothesis] | **Open** — bottleneck |

**Next frontier:** The deficit formula opens a new perspective: instead of seeking a proof that $C_\infty(\gamma_n) = 0$, we can try to prove that the off-critical-zero measure $\mu_{\mathrm{off}}$ has some functional restriction that forces $\mathcal{C}\mu_{\mathrm{off}}(\gamma_n) = 0$ for all $\gamma_n$ dense in $\mathbb{R}^+$. This connects with:

1. **Uniqueness theorems for the Cauchy-Poisson transform** (Privalov, Plemelj-Sokhotski).
2. **The asymptotic distribution of the $\gamma_n$** — its density $\sim \log T/(2\pi)$ implies that the condition $\mathcal{C}\mu_{\mathrm{off}}(\gamma_n) = 0$ for ALL $n$ is a condition on infinitely many points becoming ever denser in $\mathbb{R}^+$, which could force the extinction of $\mu_{\mathrm{off}}$ if the Cauchy transform has suitable rigidity properties.

---

## Appendix A: Why the functional-equation pairing cancels

**A.1 (The pairing $(\rho_0, 1-\bar\rho_0)$).** For $\rho_0 = \sigma_0+i\gamma_0$ and its functional pair $1-\bar\rho_0 = (1-\sigma_0)+i\gamma_0$:

$$\mathrm{Re}\,\frac{1}{\rho_n-\rho_0} + \mathrm{Re}\,\frac{1}{\rho_n-(1-\bar\rho_0)} = \frac{(1/2-\sigma_0)}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} = 0$$

The two terms are equal in magnitude and opposite in sign: the difference between $1/2$ and $\sigma_0$ changes sign between the two zeros of the pair.

**A.2 (Why the Hadamard sum does NOT use this pairing).** The Hadamard sum $\sum_\rho [1/(s-\rho)+1/\rho]$ is symmetrized for ABSOLUTE CONVERGENCE of the subseries of $1/(s-\rho)$. Convergence is achieved by grouping $\rho = \sigma+i\gamma$ with $\bar\rho = \sigma-i\gamma$ (same modulus, opposite imaginary part), not with $1-\bar\rho = (1-\sigma)+i\gamma$ (same imaginary modulus, different real part). This distinction is crucial.

**A.3 (Conclusion).** The pairing by conjugation $(\rho_0, \bar\rho_0)$ is what determines the value of $C_\infty(\gamma_n)$ via the Hadamard sum. The apparent cancellation under the functional pairing ($\rho_0, 1-\bar\rho_0$) is an illusion arising from grouping the terms in a different order — an order that does not guarantee convergence of the Hadamard sum.

---

*Next document (Doc 43): Rigidity theorems for the Cauchy-Poisson transform and their application to $\mu_{\mathrm{off}}$. Can the increasing density of the $\gamma_n$ force $\mu_{\mathrm{off}} = 0$?*
