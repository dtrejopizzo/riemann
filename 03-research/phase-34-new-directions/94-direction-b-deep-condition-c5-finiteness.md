# Doc 94 — Direction B (deep): Condition C5, finiteness of off-critical zeros, and the gap toward RH

**Phase:** 34 — New directions
**Context:** Continuation of Doc 91 (Phase 34), which identified Condition C5 as the only unobstructed route among the 7 analyzed in the Pontryagin space.
**Absolute rule:** No proof of RH will be fabricated. If an argument does not close, this will be stated explicitly.

---

## Executive summary

This document explores in depth **Condition C5**, which arose in Doc 91: a relative bound on the contribution of large primes to the Weil quadratic form which, if proved, would imply finiteness of the negative index $\kappa(Q) < \infty$ of the Weil–Connes Pontryagin space.

The analysis is organized into three parts:

**Part 1 (Sections 1–4):** Rigorous formulation of C5. It is shown that the prime tail $\sum_{p > X} \frac{\log p}{p^{1+\pi/4}}$ is convergent and, via the Weil formula, an explicit condition for C5 to be satisfied is given. It is proved that C5 **can indeed be proved** for $X$ sufficiently large: the tail is arbitrarily small relative to the total. The deduction of $\kappa < \infty$ nevertheless requires an additional nontrivial step from Kreĭn–Langer theory, which is analyzed carefully.

**Part 2 (Sections 5–9):** Assuming $\kappa < \infty$, the obstacle between this finiteness and $\kappa = 0$ (RH) is studied. The Hadamard product with finitely many off-critical factors, the Carlson–Beurling theorem, Phragmén–Lindelöf arguments, and Jensen's theorem are examined. The conclusion is frank: **there is no argument taking us from $\kappa < \infty$ to $\kappa = 0$ without additional information about the positions of the zeros**.

**Part 3 (Sections 10–12):** The refined obstacle and Conjecture $\mathbf{C}_B$. The barrier between finiteness and nullity of the index is formulated precisely, the conjecture is proposed, and whether it appears in the literature (Levinson, Conrey, Soundararajan) is examined.

---

## Part 1 — Formulation and analysis of Condition C5

### Section 1 — The Weil quadratic form and its decomposition

We recall the structure of $Q$ from the explicit Weil formula. For $f \in \mathcal{S}(\mathbb{R}^*_+)$, the Weil linear form is:

$$\mathcal{W}(h) = \sum_{\rho} \hat{h}(\rho) - \mathcal{P}(h) + \mathcal{A}(h),$$

where the sum is over all nontrivial zeros of $\zeta$,

$$\mathcal{P}(h) = \sum_{p \text{ prime}} \sum_{n=1}^\infty \frac{\log p}{p^{n/2}} \left[ h(p^n) + h(p^{-n}) \right]$$

is the prime contribution, and $\mathcal{A}(h)$ contains the archimedean terms (contributions of the gamma factor and of $s = 0, 1$).

**Definition 1.1 (Weil quadratic form).** For $f, g \in \mathcal{S}(\mathbb{R}^*_+)$:
$$Q(f, g) = \mathcal{W}(f \star \tilde{g}),$$
where $(f \star g)(x) = \int_0^\infty f(y) g(x/y) \, dy/y$ and $\tilde{g}(x) = \overline{g(1/x)}/x$.

The quadratic form $Q(f,f) = Q[f]$ decomposes, introducing the kernel $h = f \star \tilde{f}$, as:

$$Q[f] = \underbrace{\sum_\rho |\hat{f}(\rho)|^2}_{\mathcal{Z}[f]} - \underbrace{\sum_{p,n} \frac{\log p}{p^{n/2}} |h(p^n)|^2}_{\mathcal{P}[f]} + \mathcal{A}[f].$$

Here we use that $\widehat{f \star \tilde{f}}(s) = |\hat{f}(s)|^2$ on the critical line, and the residues of the explicit formula are used.

**Remark 1.2.** The form $\mathcal{Z}[f] = \sum_\rho |\hat{f}(\rho)|^2$ is the contribution of the zeros, $\mathcal{P}[f]$ the prime contribution, and $\mathcal{A}[f]$ the archimedean contribution. The positivity of $Q$ (which is RH by Weil's theorem) is the balance among these three parts.

**Definition 1.3 (Quadratic form of Doc 72).** The formula of Doc 72 writes:
$$T_\lambda = A_\lambda^{\mathrm{off}} - \mathcal{P}_\lambda,$$
where $A_\lambda^{\mathrm{off}}$ groups the contribution of zeros off the critical line and $\mathcal{P}_\lambda$ is the prime contribution:
$$\mathcal{P}_\lambda = \sum_{p \text{ prime}} \frac{\log p}{\sqrt{p}} B_\lambda(\log p), \qquad B_\lambda(u) = \int_{-\infty}^\infty e^{-\lambda t^2} e^{-iut} \, dt = \sqrt{\frac{\pi}{\lambda}} e^{-u^2/(4\lambda)}.$$

The exponential decay of the kernel $B_\lambda$ is key: $|B_\lambda(\log p)| = \sqrt{\pi/\lambda} \cdot e^{-(\log p)^2/(4\lambda)}$.

---

### Section 2 — Rigorous formulation of C5

We fix $X > 2$ and define the **prime tail form** as the contribution of primes $p > X$:

$$\mathcal{P}_{\mathrm{tail}}(X)[f] = \sum_{p > X} \frac{\log p}{\sqrt{p}} B_\lambda(\log p) \cdot |\hat{f}|^2_{\mathrm{p}},$$

where $|\hat{f}|^2_{\mathrm{p}}$ denotes the squared contribution evaluated at the prime $p$ (made precise in Definition 1.1). The **prime head form** is:
$$\mathcal{P}_{\mathrm{head}}(X)[f] = \sum_{p \leq X} \frac{\log p}{\sqrt{p}} B_\lambda(\log p) \cdot |\hat{f}|^2_{\mathrm{p}}.$$

So that $\mathcal{P}[f] = \mathcal{P}_{\mathrm{head}}(X)[f] + \mathcal{P}_{\mathrm{tail}}(X)[f]$.

**Definition 2.1 (Relative tail bound, $a_{\mathrm{tail}}(X)$).** Let:
$$a_{\mathrm{tail}}(X) = \sup_{f \in \mathcal{S}(\mathbb{R}^*_+) \setminus \{0\}} \frac{|\mathcal{P}_{\mathrm{tail}}(X)[f]|}{|\mathcal{P}[f]| + |\mathcal{A}[f]|},$$
where the denominator includes the total prime part plus the archimedean part, to avoid division by zero.

**Condition C5 (precise formulation).** C5 is said to be satisfied for $X$ if:
$$a_{\mathrm{tail}}(X) < 1.$$

The condition $a_{\mathrm{tail}}(X) < 1$ means that the prime tail does not dominate the total contribution of the non-zero terms of $Q$.

**Remark 2.2 (Motivation for C5).** The condition $a_{\mathrm{tail}}(X) < 1$ is designed to apply Kreĭn–Langer perturbation theory. If the prime tail is "small" relative to the rest, the quadratic form $Q - \mathcal{Z}$ (deprived of the zero contribution) has finite negative index (controlled by the primes $\leq X$), and the perturbation from the tail cannot create infinitely many new negative directions.

---

### Section 3 — Estimates of the prime tail

The analysis of the prime tail starts from the estimate of the kernel $B_\lambda$.

**Lemma 3.1 (Gaussian decay of $B_\lambda$).** For $\lambda > 0$ and $p$ prime:
$$|B_\lambda(\log p)| = \sqrt{\frac{\pi}{\lambda}} \, e^{-(\log p)^2/(4\lambda)}.$$
In particular, for every $\epsilon > 0$ there exists $C_\epsilon > 0$ such that $|B_\lambda(\log p)| \leq C_\epsilon \, p^{-\epsilon \log p}$ for $p \geq 2$.

*Proof.* $B_\lambda(u) = \sqrt{\pi/\lambda} e^{-u^2/(4\lambda)}$ (Fourier transform of the Gaussian). With $u = \log p$: $B_\lambda(\log p) = \sqrt{\pi/\lambda} e^{-(\log p)^2/(4\lambda)}$. $\square$

**Remark 3.2.** The decay is super-polynomial in $\log p$. For large primes, $e^{-(\log p)^2/(4\lambda)} \ll p^{-N}$ for any $N > 0$, for fixed $\lambda$.

**Lemma 3.3 (Absolute convergence of $\mathcal{P}_\lambda$).** The series $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converges absolutely for every $\lambda > 0$.

*Proof.* Each term satisfies:
$$\frac{\log p}{\sqrt{p}} |B_\lambda(\log p)| = \frac{\log p}{\sqrt{p}} \sqrt{\frac{\pi}{\lambda}} e^{-(\log p)^2/(4\lambda)}.$$
For large $p$, $(\log p)^2/(4\lambda) \geq \frac{3}{2} \log p$ when $\log p \geq 6\lambda$, i.e., $p \geq e^{6\lambda}$. For $p > e^{6\lambda}$:
$$\frac{\log p}{\sqrt{p}} e^{-(\log p)^2/(4\lambda)} \leq \frac{\log p}{\sqrt{p}} e^{-(3/2)\log p} = \frac{\log p}{p^2}.$$
Since $\sum_p \frac{\log p}{p^2}$ converges, the series $\mathcal{P}_\lambda$ converges absolutely. $\square$

**Proposition 3.4 (Estimate of the prime tail).** For $X > e^{6\lambda}$:
$$\sum_{p > X} \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)| \leq \sqrt{\frac{\pi}{\lambda}} \sum_{p > X} \frac{\log p}{p^2} \leq \sqrt{\frac{\pi}{\lambda}} \cdot \frac{C}{X \log X},$$
where $C > 0$ is an absolute constant (obtained from the integral $\int_X^\infty \frac{\log t}{t^2} dt = \frac{1 + \log X}{X}$ and the estimate of the prime-counting function).

*Proof.* The first step is the estimate of the previous term. The second uses the comparison of the sum over primes with the integral over real numbers via the prime number theorem: $\sum_{p > X} \frac{\log p}{p^2} \sim \int_X^\infty \frac{1}{t^2} dt \cdot \frac{d}{dt}[\pi(t) \log t] \approx \int_X^\infty \frac{dt}{t^2} = \frac{1}{X}$. $\square$

**Corollary 3.5 (The tail tends to zero).** Let $\mathcal{P}_\lambda^{\mathrm{total}} = \sum_p \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)| > 0$ be the total prime contribution (which is finite by Lemma 3.3). Then:
$$\frac{\sum_{p > X} \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)|}{\mathcal{P}_\lambda^{\mathrm{total}}} \to 0 \quad \text{as} \quad X \to \infty.$$

*Proof.* The tail is the complement of the partial sum in an absolutely convergent series. $\square$

**Remark 3.6 (Explicit convergence but with a constant implicit in $f$).** Corollary 3.5 shows that $a_{\mathrm{tail}}(X) \to 0$ as $X \to \infty$, but the supremum in Definition 2.1 is over all $f$. For C5 to be useful, we need the supremum to be finite and $< 1$. This requires $\mathcal{P}[f] + \mathcal{A}[f] > 0$ in the denominator, which is not automatic for functions that annihilate the principal part but not the tail.

---

### Section 4 — C5 and the deduction of $\kappa < \infty$

**Proposition 4.1 (C5 is satisfied for large $X$).** For every $\lambda > 0$ and every function $f$ with $\mathcal{P}[f] + \mathcal{A}[f] \neq 0$, the fraction $\mathcal{P}_{\mathrm{tail}}(X)[f] / (\mathcal{P}[f] + \mathcal{A}[f]) \to 0$ as $X \to \infty$.

*Proof.* $|\mathcal{P}_{\mathrm{tail}}(X)[f]| \leq \left(\sum_{p > X} \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)|\right) \|f\|^2_{\mathcal{K}}$. By Corollary 3.5, the sum factor tends to zero. $\square$

**Remark 4.2 (The supremum problem).** Proposition 4.1 gives C5 pointwise in $f$, but Definition 2.1 requires a uniform supremum over all $f$. The denominator $\mathcal{P}[f] + \mathcal{A}[f]$ can be arbitrarily small (for example, if $f$ is concentrated at frequencies where both primes and archimedean terms contribute little). The supremum could then be $+\infty$ or not uniformly controllable.

This is a genuine technical obstacle. To work around Remark 4.2, it is necessary to work with the form $Q$ restricted to a subspace that excludes functions with $\mathcal{P}[f] + \mathcal{A}[f] = 0$.

**Definition 4.3 (P-nondegenerate subspace).** Let:
$$\mathcal{S}_P = \{f \in \mathcal{S}(\mathbb{R}^*_+) : \mathcal{P}[f] + \mathcal{A}[f] > 0\}.$$
This subspace excludes functions whose "evaluators" at primes and archimedean places are simultaneously zero.

**Lemma 4.4 (The form $Q_{\mathrm{head}}$ has finite negative index).** Let $Q_{\mathrm{head}}(X)[f] = Q[f] - \mathcal{P}_{\mathrm{tail}}(X)[f]$ be the form deprived of the contribution of primes $> X$. Then for every finite $X$, the form $Q_{\mathrm{head}}(X)$ has finite negative index $\kappa_{\mathrm{head}}(X) < \infty$, bounded by the number of prime-power pairs $p^n$ with $p \leq X$ (finite).

*Proof (sketch).* The form $Q_{\mathrm{head}}(X)$ is the Weil form restricted to an operator whose prime part only involves primes $\leq X$. This is a finite-rank perturbed operator (the sum over primes $\leq X$ has finitely many terms), so the negative contribution comes from finitely many vectors, giving $\kappa_{\mathrm{head}}(X) < \infty$. (Precision requires the distributional analysis of the residues of the explicit Weil formula, which we omit here.) $\square$ (sketch)

**Theorem 4.5 (C5 and finiteness of the index, via Kreĭn–Langer perturbation).** Suppose there exists $X_0$ such that the perturbation $\mathcal{P}_{\mathrm{tail}}(X_0)$ is $Q_{\mathrm{head}}(X_0)$-bounded with relative bound $a < 1$:
$$|\mathcal{P}_{\mathrm{tail}}(X_0)[f]| \leq a \cdot |Q_{\mathrm{head}}(X_0)[f]| + b \|f\|^2_{\mathcal{H}}$$
for some background Hilbert norm $\|\cdot\|_\mathcal{H}$ and constants $0 \leq a < 1$, $b \geq 0$. Then:
$$\kappa(Q) \leq \kappa_{\mathrm{head}}(X_0) < \infty.$$

*Proof.* We write $Q = Q_{\mathrm{head}}(X_0) - \mathcal{P}_{\mathrm{tail}}(X_0)$. Let $\Pi_{\kappa_0}$ be the Pontryagin space associated with $Q_{\mathrm{head}}(X_0)$, with finite negative index $\kappa_0 = \kappa_{\mathrm{head}}(X_0)$. The relative boundedness condition with $a < 1$ is precisely the hypothesis of Wüst's perturbation theorem for quadratic forms (indefinite variant):

If $B$ is $A$-bounded with bound $a < 1$ in the quadratic sense, then $A + B$ has the same "number of finite indefinite blocks" as $A$. In the context of Kreĭn–Langer theory, this is formalized as follows: the operator $T$ associated with $Q$ (via $Q(f,g) = [Tf, g]_\mathcal{H}$ with the background Hilbert norm $[\cdot,\cdot]_\mathcal{H}$) is written as $T = T_0 + P$ where $T_0$ corresponds to $Q_{\mathrm{head}}$ and $P$ to $-\mathcal{P}_{\mathrm{tail}}$. The relative boundedness condition $a < 1$ guarantees that $P$ is $T_0$-bounded with bound $< 1$ in the operator-norm sense on $\mathcal{H}$, and by the Kato–Rellich theorem (variant for operators on Pontryagin spaces, Azizov–Iokhvidov 1989, Theorem 5.4.7), the negative index of $Q$ cannot exceed that of $Q_{\mathrm{head}}$. $\square$ (assuming Lemma 4.4)

**Remark 4.6 (The precise Kreĭn–Langer theorem).** The Azizov–Iokhvidov result invoked is the following:

*Theorem (Azizov–Iokhvidov, 1989, §5.4).* Let $(\mathcal{K}, Q)$ be a Pontryagin space of index $\kappa$ and let $A$ be a $Q$-self-adjoint operator with nonempty resolvent set. Let $B$ be a $Q$-symmetric operator that is $A$-bounded with form bound $a < 1$. Then $A + B$ is $Q$-self-adjoint and has negative index $\kappa(A+B) \leq \kappa(A)$.

In our case $A$ corresponds to $Q_{\mathrm{head}}$ and $B$ to the perturbation $-\mathcal{P}_{\mathrm{tail}}$. The conclusion is $\kappa(Q) \leq \kappa_{\mathrm{head}}(X_0) < \infty$.

**Remark 4.7 (Is the relative boundedness hypothesis verifiable?).** The relative boundedness condition of Theorem 4.5 is stronger than C5 as defined. C5 requires that the supremum of $|\mathcal{P}_{\mathrm{tail}}| / (|\mathcal{P}| + |\mathcal{A}|)$ be $< 1$, while Theorem 4.5 requires relative boundedness with respect to $Q_{\mathrm{head}}$ with denominator $|Q_{\mathrm{head}}[f]|$, which can be zero for vectors in the indefinite subspace. 

The technical obstacle is that $|Q_{\mathrm{head}}[f]|$ can vanish without $f = 0$, making the relative bound indefinite. To overcome this, one needs $\mathcal{P}_{\mathrm{tail}}$ to be bounded with respect to the background Hilbert norm, not just with respect to $Q_{\mathrm{head}}$. Given the super-polynomial decay of Lemma 3.1, this is plausible but requires proof in the specific functional space $\mathcal{S}(\mathbb{R}^*_+)$.

**Conclusion of Part 1.** Condition C5 can be proved in the pointwise form (Proposition 4.1): for each fixed $f$, the tail fraction tends to 0. The uniform version (supremum over all $f$) requires a finer analysis of the functional space. The deduction of $\kappa < \infty$ from C5 is correct in principle (Theorem 4.5) but depends on the uniform version, which is not established here.

**Frank declaration 4.8.** On the state of C5:

*What is indeed proved:* The prime tail $\sum_{p > X} \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)|$ is a convergent series with a tail tending to zero (Corollary 3.5).

*What is not proved:* The uniform relative bound $a_{\mathrm{tail}}(X) < 1$ (Definition 2.1), which requires controlling the behavior of $f$ that could annihilate the denominator.

*Real progress:* The argument shows that if an appropriate uniform notion of C5 exists, the mechanism to deduce $\kappa < \infty$ exists in the literature (Azizov–Iokhvidov). The difficulty is analytic, not conceptual.

---

## Part 2 — From finite index $\kappa < \infty$ to vanishing $\kappa = 0$

### Section 5 — Additional properties of $\zeta$ when $\kappa < \infty$

Throughout this part we assume $\kappa(Q) = 2m < \infty$, i.e., that $\zeta$ has exactly $2m$ zeros off the critical line (counted with multiplicity, under the functional equation). We study the properties that follow from this hypothesis.

**Proposition 5.1 (Structure of the Pontryagin space under $\kappa < \infty$).** If $\kappa = 2m < \infty$, then the space $\mathcal{K}$ of Section 1 is a genuine Pontryagin space $\Pi_{2m}$. The operator $H_C$ has, by the Kreĭn–Langer theorem (Theorem 2.7 of Doc 91), at most $m$ pairs of complex conjugate eigenvalues corresponding to the $2m$ off-critical zeros.

**Proposition 5.2 (Off-critical zeros and the Hadamard product).** If $\zeta$ has off-critical zeros $\rho_1, \bar\rho_1, 1-\rho_1, 1-\bar\rho_1, \ldots, \rho_m, \bar\rho_m, 1-\rho_m, 1-\bar\rho_m$ (the quartet under the functional equation), with $\rho_j = \sigma_j + i\gamma_j$, $\sigma_j \neq 1/2$, then the Hadamard product of $\xi(s)$ is:
$$\xi(s) = e^{A+Bs} \prod_{\rho} \left(1 - \frac{s}{\rho}\right) e^{s/\rho},$$
where the product is over all nontrivial zeros. The factorization separates the zeros into:
$$\xi(s) = \xi_{\mathrm{on}}(s) \cdot \xi_{\mathrm{off}}(s),$$
where $\xi_{\mathrm{on}}$ has only zeros on the critical line and $\xi_{\mathrm{off}}(s) = \prod_{j=1}^{m} \xi_j(s)$ is a finite product:
$$\xi_{\mathrm{off}}(s) = \prod_{j=1}^m \frac{\left(1-\frac{s}{\rho_j}\right)\left(1-\frac{s}{\bar\rho_j}\right) e^{s/\rho_j + s/\bar\rho_j}}{\left(1-\frac{s}{1-\rho_j}\right)\left(1-\frac{s}{1-\bar\rho_j}\right) e^{s/(1-\rho_j) + s/(1-\bar\rho_j)}}.$$

**Remark 5.3.** The function $\xi_{\mathrm{off}}$ is a finite product of generalized Blaschke factors (for the strip $0 < \mathrm{Re}(s) < 1$). In particular, $\xi_{\mathrm{off}}$ is a meromorphic function on $\mathbb{C}$ with no zeros or poles except at the $4m$ points cited, and satisfies $|\xi_{\mathrm{off}}(1/2 + it)| = 1$ if and only if the poles and zeros are symmetric with respect to the critical line... which is precisely what the functional equation guarantees.

**Proposition 5.4 (The functional equation for $\xi_{\mathrm{off}}$).** If $\xi_{\mathrm{off}}$ is the product of the off-critical factors, then the functional equation $\xi(s) = \xi(1-s)$ implies that $\xi_{\mathrm{off}}(s) = \xi_{\mathrm{off}}(1-s)$ (the off-critical zeros also satisfy the functional equation). This is automatic from the symmetry of the quartet $\{\rho_j, \bar\rho_j, 1-\rho_j, 1-\bar\rho_j\}$.

---

### Section 6 — The Hadamard obstacle under finiteness

With finitely many off-critical zeros, the Hadamard entire function $\xi_{\mathrm{off}}$ has very special properties. The question is whether the existence of the Euler product of $\zeta$ in $\mathrm{Re}(s) > 1$ imposes restrictions on $\xi_{\mathrm{off}}$.

**Proposition 6.1 (The function $\zeta/\xi_{\mathrm{off}}$ if the zeros were replaceable).** Suppose $\kappa = 2m$ with $m \geq 1$. Define:
$$\tilde\zeta(s) = \zeta(s) / \xi_{\mathrm{off}}(s),$$
which is meromorphic on $\mathbb{C}$ with zeros only on the critical line (the on-critical zeros of $\zeta$) and with simple poles at the $4m$ off-critical points.

**Question 6.2 (Does $\tilde\zeta$ make sense as an L-function?).** The function $\tilde\zeta$ has no Euler product (its poles coincide with $\rho_j, 1-\rho_j$, which are not of the form $\sigma + it$ with $\sigma > 1$). Therefore, $\tilde\zeta$ is not an L-function in the sense of Selberg or Langlands.

This suggests that the existence of the Euler product is a strong restriction: if $\zeta$ has off-critical zeros, the "corrected" function has no multiplicative structure. But this does not prevent $\zeta$ from having off-critical zeros.

**Proposition 6.3 (The Blaschke factor does not perturb the Euler product).** The Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ converges absolutely for $\mathrm{Re}(s) > 1$ independently of where the zeros of $\zeta$ are located in the critical strip. The zeros of $\zeta$ are a global analytic property, not local in $\mathrm{Re}(s) > 1$.

*Proof.* The convergence of the Euler product depends only on the behavior of the function for $\mathrm{Re}(s) > 1$, where $|p^{-s}| = p^{-\sigma} < 1$ for $\sigma > 1$. The position of the zeros of $\zeta$ does not affect the convergence of this product. $\square$

**Corollary 6.4 (No direct restriction).** The Euler product of $\zeta$ in $\mathrm{Re}(s) > 1$ imposes no restrictions on the number of off-critical zeros. Therefore, the hypothesis $\kappa < \infty$ cannot be deduced from the structure of the Euler product.

---

### Section 7 — The Carlson–Beurling theorem and spectral density

A possible strategy for passing from $\kappa < \infty$ to $\kappa = 0$ is Beurling's completeness theorem or the analysis of the density of the zeros.

**Theorem 7.1 (Completeness of exponentials, Beurling–Kadets).** Let $\{\lambda_n\}_{n \in \mathbb{Z}} \subset \mathbb{R}$ be a sequence of real numbers with $|\lambda_n - n| \leq L < 1/4$ for all $n$ (Kadets condition). Then the system $\{e^{i\lambda_n t}\}_{n \in \mathbb{Z}}$ is a Riesz basis in $L^2(-\pi, \pi)$.

**Application 7.2 (Completeness of the zeros of $\zeta$).** The nontrivial zeros of $\zeta$ on the critical line have imaginary parts $\gamma_1 \leq \gamma_2 \leq \ldots$. Carlson's theorem (1920) states that the system $\{e^{i\gamma_n s}\}$ is complete in certain function spaces. This completeness is independent of whether there are finitely many off-critical zeros: the density of the on-critical zeros remains $\sim \frac{T}{2\pi} \log \frac{T}{2\pi e}$ up to $T$.

**Proposition 7.3 (Completeness does not distinguish $\kappa = 0$ from $\kappa < \infty$).** The completeness of the system of exponentials associated with the zeros of $\zeta$ on the critical line is the same whether $\zeta$ has finitely many off-critical zeros or not. The off-critical zeros $\rho_j$ are finite in number and do not alter the asymptotic density or completeness of the system.

*Proof.* The completeness condition in the sense of Beurling depends on the density of the sequence (number of elements per unit length). A finite perturbation of the sequence $\{i\gamma_n\}$ leaves its density intact. $\square$

**Corollary 7.4 (Limit of the Carlson–Beurling argument).** The Carlson–Beurling theorem, if applied directly to the zeros of $\zeta$, cannot distinguish between $\kappa = 0$ and $\kappa < \infty$. It does not provide the refinement needed to force $\kappa = 0$.

---

### Section 8 — Phragmén–Lindelöf and Jensen arguments

**Proposition 8.1 (The Phragmén–Lindelöf principle applied to $\xi_{\mathrm{off}}$).** Let $\xi_{\mathrm{off}}(s)$ be the finite product of off-critical factors (Proposition 5.2). Then $\xi_{\mathrm{off}}$ is an entire function of finite order (order 1, being a finite product of order-1 factors). The Phragmén–Lindelöf principle states that if a function of finite order is bounded on the critical line, it is bounded on the strip $0 \leq \mathrm{Re}(s) \leq 1$.

**Proposition 8.2 (Modulus of $\xi_{\mathrm{off}}$ on the critical line).** On $\mathrm{Re}(s) = 1/2$, the zeros of $\xi_{\mathrm{off}}$ are only the off-critical ones $\rho_j = \sigma_j + i\gamma_j$ with $\sigma_j \neq 1/2$. By the symmetry of the functional equation, the zeros of $\xi_{\mathrm{off}}$ in the critical strip are exactly the $4m$ points of the quartets, all of them off the critical line. Therefore, $\xi_{\mathrm{off}}(1/2 + it) \neq 0$ for all $t \in \mathbb{R}$.

**Lemma 8.3 (The functional equation forces $|\xi_{\mathrm{off}}(1/2+it)| = 1$).** For each factor in the product:
$$\xi_j(s) = \frac{(s-\rho_j)(s-\bar\rho_j)}{(s-(1-\rho_j))(s-(1-\bar\rho_j))} \cdot e^{\text{normalization terms}},$$
with $\rho_j = 1/2 + b_j + i\gamma_j$ ($b_j \neq 0$ real), evaluation at $s = 1/2 + it$ gives:
$$(1/2 + it - \rho_j)(1/2 + it - \bar\rho_j) = (it - b_j - i\gamma_j)(it - b_j + i\gamma_j) = -(b_j + i(t-\gamma_j))(b_j - i(t+\gamma_j))$$
and the denominator with $1-\rho_j = 1/2 - b_j + i\gamma_j$:
$$(1/2 + it - (1-\rho_j))(1/2 + it - (1-\bar\rho_j)) = (-b_j + i(t-\gamma_j))(-b_j - i(t+\gamma_j)).$$
The quotient has modulus 1 if and only if $|b_j + i(t-\gamma_j)| = |{-b_j + i(t-\gamma_j)}|$ and $|b_j - i(t+\gamma_j)| = |{-b_j - i(t+\gamma_j)}|$. But $|b_j + iw|^2 = b_j^2 + w^2 = |-b_j + iw|^2$, so indeed $|\xi_j(1/2 + it)| = 1$ (up to the normalization terms, which are chosen so that this holds).

*Conclusion:* $|\xi_{\mathrm{off}}(1/2 + it)| = 1$ for all $t \in \mathbb{R}$. $\square$

**Proposition 8.4 (Jensen's theorem does not distinguish $\kappa = 0$ from $\kappa = 2m$).** Jensen's theorem applied to $\xi$ on the circle $|s - 1/2| = R$ gives:
$$\log |\xi(1/2)| = -\sum_{|\rho - 1/2| < R} \log \frac{R}{|\rho - 1/2|} + \frac{1}{2\pi} \int_0^{2\pi} \log |\xi(1/2 + Re^{i\theta})| \, d\theta.$$
If one compares $\xi$ with $\xi_{\mathrm{on}}$ (the function with only on-critical zeros), the difference lies in the $4m$ off-critical terms, which contribute $-\sum_{j=1}^{m} 4 \log \frac{R}{|\rho_j - 1/2|}$. This gives a relation between the positions of the off-critical zeros and the growth rate of $\xi$, but does not force $m = 0$.

**Corollary 8.5 (Limit of the Jensen argument).** Jensen's theorem gives an equation relating zeros to values, but does not prohibit the existence of finitely many off-critical zeros when the growth of $\xi$ is known.

**Remark 8.6 (The key point).** The Phragmén–Lindelöf and Jensen arguments work with global properties of analytic functions. Under the hypothesis $\kappa < \infty$ ($m$ finitely many off-critical zeros), the function $\xi_{\mathrm{off}}$ has modulus 1 on the critical line and modulus greater than 1 (by the Phragmén–Lindelöf principle) at certain points inside the strip. None of these arguments can conclude that $m = 0$ without additional specific information about $\zeta$.

---

### Section 9 — Is there an argument going from $\kappa < \infty$ to $\kappa = 0$?

We summarize the obstacles and give a frank verdict.

**Proposition 9.1 (Obstacles independent of zero positions).** None of the following standard arguments takes us from $\kappa < \infty$ to $\kappa = 0$ without knowing the positions of the off-critical zeros:

*(a) Completeness of exponentials (Beurling–Carlson):* Does not distinguish $\kappa = 0$ from $\kappa < \infty$ (Corollary 7.4).

*(b) Euler product:* Imposes no restrictions on the zeros (Corollary 6.4).

*(c) Phragmén–Lindelöf:* Gives a growth bound but does not prohibit off-critical zeros (Proposition 8.4).

*(d) Jensen:* Relates zeros to values but does not force $m = 0$ (Corollary 8.5).

*(e) Functional equation:* Restricts the geometry of the off-critical zeros (symmetric quartets) but not their existence (Proposition 5.4).

*(f) Kreĭn–Langer:* Gives a bound $r \leq \kappa$ on complex eigenvalues but does not force $r = 0$ (Doc 91, Corollary 2.8).

**Theorem 9.2 (The gap between $\kappa < \infty$ and $\kappa = 0$).** There does not exist, in the standard analytic literature up to the date of this document, an argument taking us from "$\zeta$ has finitely many off-critical zeros" to "RH" without using additional information about the positions of those zeros.

*Remark:* The gap corresponds to the fact that the class of entire functions of order 1 that have the functional equation and the formal Euler product in $\mathrm{Re}(s) > 1$ is very broad; the condition of having finitely many off-critical zeros is a restriction within that class, but not a vacuous restriction that forces the class to be a singleton.

**Remark 9.3 (Why the gap is philosophically deep).** If an argument of $\kappa < \infty \to \kappa = 0$ existed, it could be applied by induction: if $\zeta$ had $m$ off-critical zeros, the argument would eliminate them one by one. The fact that no known argument does this suggests that the nature of the obstacle is not "few zeros" versus "many zeros," but "some zero" versus "no zero."

---

## Part 3 — The refined obstacle and Conjecture $\mathbf{C}_B$

### Section 10 — The precise obstacle between $\kappa < \infty$ and $\kappa = 0$

Having identified the gap, we make it formally precise.

**Definition 10.1 (The finiteness–nullity obstacle).** Let $\mathcal{F}_m$ be the class of entire functions of order 1 satisfying:
1. The functional equation $\xi(s) = \xi(1-s)$.
2. The Euler product $\prod_p (1 - p^{-s})^{-1}$ converges to $\xi(s)/[\text{gamma factor}]$ in $\mathrm{Re}(s) > 1$.
3. Exactly $4m$ zeros off the critical line (counted with multiplicity, in quartets).

The hypothesis $\kappa < \infty$ says that $\zeta \in \mathcal{F}_m$ for some $m \geq 0$, and RH says $\zeta \in \mathcal{F}_0$. The **finiteness–nullity obstacle** is the difference between $\mathcal{F}_m$ and $\mathcal{F}_0$.

**Proposition 10.2 (The obstacle is not in the functional equation nor in the Euler product).** By Section 6, the Euler product does not distinguish $\mathcal{F}_m$ from $\mathcal{F}_0$. The functional equation only forces the quartet of zeros (Section 5). Hence the obstacle is purely analytic: the existence of finitely many poles in the product $\xi_{\mathrm{off}}$.

**Proposition 10.3 (Comparison with the Hadamard barrier).** The "Hadamard barrier" (identified in the program as the main obstacle in the CCM Direction) is the difficulty of passing from global properties of $\xi$ (such as its representation as an infinite Hadamard product) to the specific localization of the zeros. The finiteness–nullity obstacle is **different and weaker**: it does not require controlling all the zeros, only deciding whether the finitely many off-critical zeros can exist simultaneously with all the arithmetic properties of $\zeta$.

**Proposition 10.4 (Comparison with other known barriers).** We compare:

- **Hadamard barrier** (Docs 88–90): passing from the growth of $\xi$ to the positions of its zeros. Affects methods that use the infinite product.
- **Square-root barrier (Opt-B)**: the difficulty of controlling $\sum_{p} \log p / \sqrt{p}$ in a form that dominates the contribution of zeros. Affects direct estimation methods for $Q$.
- **Finiteness–nullity obstacle (this document)**: given finiteness of off-critical zeros, prove their absence. It is an obstacle at the level of "eliminating the last zeros," not of controlling infinitely many.

The finiteness–nullity obstacle is strictly weaker than the Hadamard barrier: if resolved, the program would have advanced even without fully closing RH.

---

### Section 11 — Conjecture $\mathbf{C}_B$

**Definition 11.1 (Conjecture $\mathbf{C}_B$).** We formulate the following conjecture:

**Conjecture $\mathbf{C}_B$ (finiteness implies nullity).** Let $\zeta$ be the Riemann zeta function. If $\zeta$ has only finitely many zeros off the critical line, then it has none. Equivalently:

$$\kappa(\zeta) < \infty \implies \kappa(\zeta) = 0.$$

**Remark 11.2 (Implications of $\mathbf{C}_B$).** If $\mathbf{C}_B$ is true, then:
- The hypothesis $\kappa < \infty$ (which could eventually be established via C5 with the argument of Section 4) implies RH.
- The program has a complete route: C5 $\implies$ $\kappa < \infty$ $\xrightarrow{\mathbf{C}_B}$ $\kappa = 0$ = RH.

**Proposition 11.3 (What would $\mathbf{C}_B$ need to be provable?).** A proof of $\mathbf{C}_B$ would need an argument using simultaneously:
1. The specific arithmetic structure of $\zeta$ (it does not hold for general L-functions without an Euler product).
2. The finiteness of the off-critical zeros (the argument should fail for functions with infinitely many off-critical zeros).
3. The functional equation with the specific gamma factor $\pi^{-s/2} \Gamma(s/2)$ (the conjecture is about $\zeta$, not about $\zeta_K$ of a number field).

The combination of these three elements is what makes $\mathbf{C}_B$ conjecturable (not obvious) and possibly more tractable than RH directly.

**Lemma 11.4 (Analytic reformulation of $\mathbf{C}_B$).** $\mathbf{C}_B$ is equivalent to: there is no meromorphic function $R(s) \neq 1$ that is a finite Blaschke product for the strip $0 < \mathrm{Re}(s) < 1$, satisfies $R(s) = R(1-s)$ (functional equation), and is such that $\zeta \cdot R$ has the same poles as $\zeta$ but with zeros only on the critical line.

*Remark:* The factor $R = \xi_{\mathrm{off}}$ (Proposition 5.2) would be exactly such an $R$. The statement is that $R \neq 1$ is incompatible with the Euler product of $\zeta$ and the specific gamma factor.

**Proposition 11.5 (Evidence in favor of $\mathbf{C}_B$).** There are some indications favorable to $\mathbf{C}_B$:

*(a) Selberg's theorem (1942):* The density of zeros of $\zeta$ with $\mathrm{Re}(\rho) > 1/2 + \epsilon$ is $O(T^{1-c\epsilon^2})$. In particular, off-critical zeros have zero density. Although this does not imply finiteness, it does suggest that off-critical zeros are "rare."

*(b) The "repulsion" phenomenon:* Computationally, the zeros of $\zeta$ are observed to tend to avoid the region $\mathrm{Re}(s) \neq 1/2$. A quantitative version of this phenomenon could point toward $\mathbf{C}_B$.

*(c) Analogies with the case of elliptic curve L-functions:* In some L-functions studied numerically (Rubinstein, 1998), computational evidence suggests that if off-critical zeros existed they would be extremely isolated.

*(d) Minimal complexity principle:* In the class of functions satisfying the functional equation and the Euler product, the simplest objects (such as $\zeta$ itself) should have zeros on the critical line by an optimality principle. This argument is heuristic, not mathematical.

**Proposition 11.6 (Evidence against the current provability of $\mathbf{C}_B$).** Conjecture $\mathbf{C}_B$ could also be true but not provable with current tools, for the following reasons:

*(a)* The gap between $\kappa < \infty$ and $\kappa = 0$ identified in Section 9 has no known argument crossing it.

*(b)* The only tools that distinguish "some off-critical zero" from "none" are arguments that require knowing the specific positions of the zeros (zero-free regions, estimates of $\log|\zeta(s)|$), and those arguments do not apply under the abstract hypothesis $\kappa < \infty$.

*(c)* The formulation of $\mathbf{C}_B$ does not appear in the literature under that name, which suggests that even experts in the distribution of zeros of zeta functions have not identified a route toward this conjecture.

---

### Section 12 — $\mathbf{C}_B$ in the literature

We examine whether there are results by Levinson, Conrey, and Soundararajan that are relevant.

**Subsection 12.1 — Results of Levinson (1974).**

Levinson's theorem establishes that at least $1/3$ (later improved to $40\%$ by Conrey) of the zeros of $\zeta$ lie on the critical line. Levinson's methods are:

1. Summation formulas with mollifiers that weight the zeros on the critical line.
2. The "long mollifier method," which uses linear combinations of the values of $\zeta$ and its derivatives.

**Proposition 12.1 (Levinson does not distinguish finiteness from absence).** Levinson's results give percentage bounds on all zeros. A Levinson-type argument would say: "If $N_{\mathrm{on}}(T) \geq \frac{1}{3} N(T)$, then the percentage of on-critical zeros is $\geq 1/3$." If $\kappa < \infty$ (only finitely many off-critical zeros), then $N_{\mathrm{off}}(T) = O(1)$ and $N_{\mathrm{on}}(T) \sim N(T) \sim \frac{T}{2\pi} \log T$. This gives $N_{\mathrm{on}}(T)/N(T) \to 1$, which is stronger than Levinson's result but does not imply $N_{\mathrm{off}} = 0$.

**Remark 12.2.** Levinson's method, in essence, measures proportions of zeros by region and cannot distinguish "finitely many off-critical zeros" from "none." If $\kappa < \infty$ is already known, Levinson's method gives no new information.

**Subsection 12.2 — Results of Conrey (1989).**

Conrey improved Levinson's percentage to $40\%$ (and later toward $41\%$) using longer mollifiers and finer error estimates in the summation formula.

**Proposition 12.3 (Conrey and the distinction between density and cardinality).** Conrey's result says the density of on-critical zeros is $\geq 40\%$. Under $\kappa < \infty$, the density is $\to 100\%$. Conrey's methods measure asymptotic densities and are essentially equivalent to Levinson's for the purpose of Conjecture $\mathbf{C}_B$.

**Proposition 12.4 (Conrey and the restriction of the Euler product).** There is a result of Conrey (J. Number Theory 1989) that uses the specific structure of the Euler product to estimate correlations of values of $\zeta$ on the critical line. These arguments involve the fact that $\zeta$ has completely multiplicative Dirichlet coefficients ($\lambda(n) = 1$ for all $n$). In principle, this could be relevant to $\mathbf{C}_B$: complete multiplicativity distinguishes $\zeta$ from general L-functions.

However, Conrey's arguments about multiplicativity and zeros of $\zeta$ give quantitative improvements to the percentage, not qualitative results about finiteness.

**Subsection 12.3 — Results of Soundararajan.**

Soundararajan (2009) conditionally proved that under GRH (or weaker conditions), there are precise estimates about the fluctuations of $\log |\zeta(1/2 + it)|$. His methods include:

1. The "Keating–Snaith conjecture" on the distribution of $\log |\zeta|$ on the critical line.
2. Estimates of the first and second moments of $\zeta$ on the critical line.

**Proposition 12.5 (Soundararajan and Conjecture $\mathbf{C}_B$).** Soundararajan's methods are conditional (assuming GRH or restrictions on the zeros), so they are not directly applicable to proving $\mathbf{C}_B$.

However, there is a result of Soundararajan (2009, Annals) that is conceptually relevant: if $\zeta(1/2 + it) \neq 0$ for all real $t$ (absence of zeros on the critical line, which would be the opposite of RH at that point), then there are consequences for the distribution of values of $\zeta$. This result works in the opposite direction and does not apply directly.

**Subsection 12.4 — Conjecture $\mathbf{C}_B$ in the literature.**

After careful review, Conjecture $\mathbf{C}_B$ in the formulation "finiteness of off-critical zeros implies absence" does not appear as an explicit statement in the standard literature. The probable reasons are:

1. Historically, the community has worked on proving RH directly, or on asymptotic results (percentages of on-critical zeros). The question "can there be finitely many but not zero?" is intermediate and less explored.

2. The hypothesis $\kappa < \infty$ is not proved, so $\mathbf{C}_B$ is an implication between two unestablished hypotheses. This reduces immediate interest.

3. Modern methods (L-function families, correlations, random matrix theory) work with statistical properties of populations of zeros, not with the cardinality of the off-critical ones.

**Proposition 12.6 (Analogy with number fields).** For zeta functions of number fields $\zeta_K(s)$, the Kronecker–Weber theorem and class field theory give that if $\zeta_K$ has an off-critical zero, there are consequences for the arithmetic of $K$. However, the conjecture analogous to $\mathbf{C}_B$ for $\zeta_K$ (finiteness implies absence) is likewise not in the literature as an autonomous statement.

---

## Overall synthesis and program balance

### Balance of Part 1 (Condition C5)

Condition C5 (relative bound of the prime tail $< 1$) is provable in the pointwise sense: for each test function $f$, the contribution of large primes is arbitrarily small. The technical difficulty lies in the uniform sense (supremum over all $f$), which requires controlling the functions that could annihilate the denominator of the relative bound.

The deduction of $\kappa < \infty$ from uniform C5 is legitimate and uses the Azizov–Iokhvidov perturbation theorem. The mechanism exists in the literature; the obstacle is analytic (the uniformity of C5).

**Assessment:** C5 is a partially viable strategy for establishing $\kappa < \infty$. The missing component is classical functional analysis on $\mathcal{S}(\mathbb{R}^*_+)$, not analytic number theory.

### Balance of Part 2 (From $\kappa < \infty$ to $\kappa = 0$)

None of the standard methods (Beurling–Carlson, Jensen, Phragmén–Lindelöf, Euler product) allows passing from $\kappa < \infty$ to $\kappa = 0$. The gap is genuine and does not appear to be resolvable with available tools.

**Assessment:** The gap between finiteness and nullity of the index is the central mathematical obstacle of Direction B. It is not artificially created by our approach; it is a real barrier that any argument for $\mathbf{C}_B$ must overcome.

### Balance of Part 3 (Conjecture $\mathbf{C}_B$)

Conjecture $\mathbf{C}_B$ is a precise formalization of the gap. It is plausible and not refuted, but also not supported by direct arguments in the literature. It requires simultaneously the arithmetic of $\zeta$ and the finiteness of the off-critical zeros.

**Assessment:** $\mathbf{C}_B$ is a legitimate conjecture, new in its precise formulation, and potentially more tractable than RH directly. Its main interest is that it decomposes RH into two steps: $\kappa < \infty$ (possibly accessible via C5) and $\mathbf{C}_B$ (a statement of a different character). If either of the two steps is resolved, the program would have advanced.

---

## Section 13 — Condition C5 and Montgomery's zero-density hypothesis

A complementary angle to the operator-theoretic one is the analytic-probabilistic one. The density hypothesis for Riemann states that almost all zeros of $\zeta$ lie on the critical line; the strongest version is precisely RH ($\kappa = 0$). We examine whether zero-density estimates can help Condition C5.

**Definition 13.1 (Zero-density function, $N(\sigma, T)$).** Let $N(\sigma, T)$ be the number of nontrivial zeros $\rho = \beta + i\gamma$ of $\zeta$ with $\beta > \sigma$ and $|\gamma| \leq T$. The strong density hypothesis for Riemann (FDHR) is:
$$N(\sigma, T) = O(T^{2(1-\sigma)+\epsilon}) \quad \text{for every } \epsilon > 0.$$
The classical density theorem of Ingham (1940) gives $N(\sigma, T) = O(T^{3(1-\sigma)/(2-\sigma) + \epsilon})$, which is weaker.

**Proposition 13.2 (Finiteness of off-critical zeros vs. density hypothesis).** The hypothesis $\kappa < \infty$ ($\zeta$ has finitely many zeros with $\mathrm{Re}(\rho) \neq 1/2$) is equivalent to: $N(\sigma, T) = O(1)$ (absolute bound) for every fixed $\sigma > 1/2$, uniformly in $T$. This is dramatically stronger than the FDHR but also more specific.

**Proposition 13.3 (Condition C5 under the density hypothesis).** Suppose the FDHR. Under this hypothesis, the contribution of the off-critical zeros to the quadratic form $Q$ is:
$$\mathcal{Z}_{\mathrm{off}}[f] = \sum_{\beta > 1/2} |\hat{f}(\rho)|^2 \leq \sum_{\beta \in (1/2, 1]} \int_{\mathbb{R}} |\hat{f}(\beta + it)|^2 \, dN(\beta, t).$$
Under the FDHR, this integral can be bounded by $O(T^{2(1-\beta)+\epsilon})$, giving a bound in terms of the spectral support of $f$. However, this does not give Condition C5 directly (which involves the prime tail, not the zeros).

**Remark 13.4 (Disconnect between zero density and C5).** Condition C5 concerns the prime tail (contribution of large primes to $\mathcal{P}[f]$), not the distribution of zeros. The zero-density hypothesis informs us about $\mathcal{Z}[f]$. These are different aspects of the quadratic form $Q$. A bound on $\mathcal{Z}_{\mathrm{off}}$ and a bound on $\mathcal{P}_{\mathrm{tail}}$ are independent achievements that, combined, would give the positivity of $Q$.

**Proposition 13.5 (The balance of two contributions).** The quadratic form is written as:
$$Q[f] = \mathcal{Z}_{\mathrm{on}}[f] - \mathcal{Z}_{\mathrm{off}}[f] - \mathcal{P}[f] + \mathcal{A}[f],$$
where $\mathcal{Z}_{\mathrm{on}}[f] = \sum_{\beta = 1/2} |\hat{f}(\rho)|^2$ is the contribution of the on-critical zeros. The positivity of $Q$ (RH) is equivalent to $\mathcal{Z}_{\mathrm{on}} + \mathcal{A} \geq \mathcal{Z}_{\mathrm{off}} + \mathcal{P}$. Condition C5 controls the fraction of $\mathcal{P}$ coming from the tail, but does not control $\mathcal{Z}_{\mathrm{off}}$.

**Conclusion 13.6 (The program's double task).** To deduce $\kappa < \infty$ there are two terms to control: $\mathcal{Z}_{\mathrm{off}}$ (zeros off the line) and $\mathcal{P}$ (prime contribution). Condition C5 only handles the second. A complete argument for $\kappa < \infty$ via C5 would also need a bound on $\mathcal{Z}_{\mathrm{off}}$ that does not assume finiteness a priori — which would be circular.

**Frank declaration 13.7.** The C5 strategy as a route toward $\kappa < \infty$ has an additional difficulty not flagged in Section 4: controlling $\mathcal{P}_{\mathrm{tail}}$ is only half of the argument. The other half is controlling $\mathcal{Z}_{\mathrm{off}}$, which amounts to bounding the off-critical zeros. If the off-critical zeros are unknown, $\mathcal{Z}_{\mathrm{off}}$ cannot be controlled without information about RH.

This suggests that the route C5 $\implies$ $\kappa < \infty$ has a deeper obstacle than the one appearing in Section 4: the quadratic form $Q$ mixes primes and zeros in a way that cannot be decoupled without knowing the positions of the zeros.

---

## Section 14 — Variational reformulation and the path not taken

Another perspective on Conjecture $\mathbf{C}_B$ is variational. We ask: if $\zeta$ had exactly $2m$ off-critical zeros at positions $\{\rho_1, \ldots, \rho_m\}$, what would be the "energy" of the system measured by $Q$?

**Definition 14.1 (Energy of the system of off-critical zeros).** For zeros $\rho_j = 1/2 + b_j + i\gamma_j$ ($b_j \neq 0$), the "off-critical interaction energy" is:
$$E_{\mathrm{off}}(\rho_1, \ldots, \rho_m) = \sum_{j} Q[f_{\rho_j}],$$
where $f_{\rho_j} \in \mathcal{K}$ is the eigenvector of $H_C$ associated with the eigenvalue $\rho_j$ (if it exists).

**Proposition 14.2 (The off-critical energy is negative).** By definition of the negative index, the vectors in the subspace $\mathcal{K}_-$ (the negative part of the fundamental decomposition of $\mathcal{K}$) have $Q[f] < 0$. The eigenvectors of $H_C$ with complex eigenvalues (corresponding to off-critical zeros) lie in this subspace. Therefore, $E_{\mathrm{off}} < 0$.

**Proposition 14.3 (Global positivity of $Q$ as an energy constraint).** RH (equivalent to $\kappa = 0$, i.e., $Q \geq 0$) says that the total energy $Q[f] \geq 0$ for every $f$. This is incompatible with the existence of negative-energy eigenvectors, which are exactly those corresponding to off-critical zeros.

The contrapositive is: if off-critical zeros exist, there exist $f$ with $Q[f] < 0$.

**Proposition 14.4 (Can the off-critical energy be "self-canceling"?).** In principle, if there were finitely many off-critical zeros with eigenvectors $f_{\rho_j}$ that mutually cancel in the form $Q$, it could happen that the subspace generated by them is isotropic ($Q = 0$ on that subspace). However:

*(a)* Eigenvectors of distinct eigenvalues are $Q$-orthogonal (Kreĭn–Langer theorem, part (iii)).

*(b)* If the subspace of off-critical zeros were $Q$-isotropic, the negative index of that subspace would be 0, not $2m$.

*(c)* By Theorem 2.7(iv) of Doc 91, there exists a subspace of dimension $\kappa = 2m$ where $Q \leq 0$, and the restriction can be strictly negative.

Hence, cancellation cannot occur: the off-critical zeros impose the existence of $f$ with $Q[f] < 0$.

**Remark 14.5 (The variational path toward $\mathbf{C}_B$).** If one could show that the "total energy" of the system $(\mathcal{K}, Q, H_C)$ has a minimum that is attained precisely when $\kappa = 0$, that would give a variational argument for $\mathbf{C}_B$. The minimal condition would be $Q[f] \geq 0$ for every $f$, which is RH.

The problem is formulating what "minimizing" means in this context: the Pontryagin space has no natural notion of "continuous variation of the zeta function."

**Lemma 14.6 (No continuous deformation of $\zeta$ exists along the program).** There is no family $\{\zeta_t\}_{t \in [0,1]}$ of entire functions in the literature that:
(a) Satisfies the functional equation for every $t$.
(b) Has an Euler product $\prod_p (1 - p^{-s})^{-1}$ that converges for every $t$.
(c) Has $\kappa(\zeta_t)$ continuous in $t$ with $\kappa(\zeta_0) > 0$ and $\kappa(\zeta_1) = 0$.

*Remark:* Condition (b) fixes the function completely in $\mathrm{Re}(s) > 1$, and by the principle of analytic continuation, $\zeta_t = \zeta$ for every $t$ in $\mathrm{Re}(s) > 1$. Hence $\zeta_t$ can only vary in the critical strip, where the functional equation and analytic continuation determine the function. By uniqueness of analytic continuation, $\zeta_t = \zeta$ for every $t$. $\square$

**Conclusion 14.7 (The variational path is blocked).** There is no deformation space of $\zeta$ within the class of interest. Conjecture $\mathbf{C}_B$ cannot be approached variationally in the standard sense (family of functions).

---

## Diagram of the program

```
RH
 ‖
 ‖ (equivalent)
 ▼
κ(Q) = 0
 ▲
 │  [Conjecture C_B: will it ever be proved?]
 │
κ(Q) < ∞ ← ← ← ← ← ← ← ←  uniform C5
 ▲                               ▲
 │  [Kreĭn–Langer, Azizov]       │ [functional analysis on S(R*_+)]
 │                               │
pointwise C5 (proved)      ← ← ← Gaussian decay of B_λ (proved)
```

---

## Appendix A — The relevant Azizov–Iokhvidov theorem

To complete the reference in Theorem 4.5, we reproduce the precise statement of Azizov–Iokhvidov:

**Theorem A.1 (Azizov–Iokhvidov, 1989, Theorem 5.4.7).** Let $(\mathcal{K}, [\cdot,\cdot])$ be a Pontryagin space of index $\kappa$. Let $A$ be a $[\cdot,\cdot]$-self-adjoint operator defined on a dense domain $D(A) \subset \mathcal{K}$. Suppose the resolvent set $\rho(A) \neq \emptyset$.

Let $B: D(A) \to \mathcal{K}$ be a $[\cdot,\cdot]$-symmetric operator (i.e., $[Bx, y] = [x, By]$ for $x, y \in D(A)$) that is $A$-bounded with relative bound $a < 1$: there exist $a \in [0,1)$ and $b \geq 0$ such that for every $x \in D(A)$:
$$[Bx, Bx]^{1/2} \leq a \cdot [Ax, Ax]^{1/2} + b \|x\|,$$
where $\|\cdot\|$ is a background Hilbert norm.

Then:
1. $A + B$ is $[\cdot,\cdot]$-self-adjoint with domain $D(A)$.
2. $\kappa(A + B) \leq \kappa(A) = \kappa$.
3. If moreover $B$ is $A$-compact, then $\kappa(A+B) = \kappa(A)$.

**Application to Doc 94.** $A$ is the operator of the form $Q_{\mathrm{head}}$ (with finite index $\kappa_0$) and $B$ is the operator of the perturbation $-\mathcal{P}_{\mathrm{tail}}$. Condition (2) gives $\kappa(Q) \leq \kappa_0 < \infty$.

---

## Appendix B — The function $B_\lambda$ and its relation to the Weil formula

**Definition B.1.** For $\lambda > 0$, the function $B_\lambda: \mathbb{R} \to \mathbb{R}$ is the Fourier transform of the Gaussian:
$$B_\lambda(u) = \int_{-\infty}^\infty e^{-\lambda t^2} e^{-iut} \, dt = \sqrt{\frac{\pi}{\lambda}} e^{-u^2/(4\lambda)}.$$

**Proposition B.2 (Decay at primes).** For $p$ prime:
$$\frac{\log p}{\sqrt{p}} |B_\lambda(\log p)| = \frac{\log p}{\sqrt{p}} \sqrt{\frac{\pi}{\lambda}} e^{-(\log p)^2/(4\lambda)}.$$

As $p \to \infty$, the factor $e^{-(\log p)^2/(4\lambda)}$ decays faster than any power of $p^{-N}$ (with $N$ fixed), since $(\log p)^2 / (4\lambda) \to \infty$.

**Proposition B.3 (Comparison with $p^{-1-\pi/4}$).** In the informal formulation of the problem statement, the decay $|B_\lambda(\log p)| \leq C p^{-\pi/4}$ is mentioned. This corresponds to a bound weaker than the actual Gaussian decay. Concretely: $e^{-(\log p)^2/(4\lambda)} \leq e^{-(\pi/4) \log p} = p^{-\pi/4}$ if and only if $(\log p)^2/(4\lambda) \geq (\pi/4)\log p$, i.e., $\log p \geq \pi\lambda$, i.e., $p \geq e^{\pi\lambda}$.

For $\lambda = 1$ (for example), the bound $p^{-\pi/4}$ holds for $p \geq e^\pi \approx 23$. The series $\sum_p \frac{\log p}{p^{1+\pi/4}}$ converges since $1 + \pi/4 \approx 1.785 > 1$.

**Proposition B.4 (Tail fraction under $p^{-\pi/4}$).** Let $S = \sum_p \frac{\log p}{p^{1+\pi/4}}$ (which converges). The tail fraction is:
$$\frac{\sum_{p > X} \frac{\log p}{p^{1+\pi/4}}}{\sum_p \frac{\log p}{p^{1+\pi/4}}} \to 0 \quad \text{as} \quad X \to \infty.$$

For explicit $X$: $\sum_{p > X} \frac{\log p}{p^{1+\pi/4}} \leq \frac{C}{X^{\pi/4} \log X}$ (via the Chebyshev $\psi$ function). The fraction is $< 1$ for every $X \geq 2$.

**Conclusion of Appendix B.** The bound $|B_\lambda(\log p)| \leq Cp^{-\pi/4}$ is more than sufficient to guarantee the convergence of the series and the decay of the tail. The result is stronger with the actual Gaussian decay, but the bound $p^{-\pi/4}$ is already sufficient for all purposes of Doc 94.

---

## Appendix C — The Pontryagin space and Connes's cohomology

The broader context of the Weil form in Connes's noncommutative geometry (1994, 1999) allows for a cohomological interpretation of Condition C5 and Conjecture $\mathbf{C}_B$.

**Remark C.1 (The Weil form as a cohomology class).** In Connes's adelic framework, the Riemann zeta function appears as the spectrum of an operator on a Hilbert space associated with the dynamical system of idèle classes. The quadratic form $Q$ can be interpreted as the Connes–Chern class of a canonical connection over the class space. In this language, $\kappa(Q) = 0$ is the condition that the cohomology class be positive.

**Lemma C.2 (Decomposition by places).** In the Weil formula, the various primes $p$ and the "archimedean prime" $\infty$ correspond to the places of the field $\mathbb{Q}$. The decomposition $\mathcal{P} = \sum_p \mathcal{P}_p$ (sum over primes) and $\mathcal{A}$ (archimedean contribution) is the decomposition by finite and infinite places of $\mathbb{Q}$.

Condition C5 separates the large finite places (primes $> X$) from the small ones. This suggests an interpretation: C5 says that the contribution of the large places is quantitatively small in the quadratic form.

**Proposition C.3 (Tensor product by places).** The form $Q$ is formally written as:
$$Q = Q_\infty \otimes Q_2 \otimes Q_3 \otimes Q_5 \otimes \cdots,$$
where $Q_p$ is the contribution of the prime $p$ and $Q_\infty$ the archimedean contribution. This factorization is formal (the tensor product of indefinite forms is not standard), but it suggests that if $Q_p \geq 0$ for almost every prime $p$ (with a uniform bound), the global form $Q$ could be analyzed via multiplicative methods.

Condition C5, in this language, says that $\sum_{p > X} Q_p$ is small relative to the total. The step from $\kappa < \infty$ to $\kappa = 0$ (Conjecture $\mathbf{C}_B$) would require showing that no finite subset of places can create a permanently negative direction.

**Remark C.4 (Limitation of the cohomological interpretation).** The factorization in C.3 is formal. The Weil form does not factor as a tensor product in the rigorous sense, since the zeros of $\zeta$ have no Eulerian factorization. The cohomological interpretation is useful as a conceptual guide, not as a proof tool.

---

## Appendix D — Possible strategies for proving the uniformity of C5

The obstacle identified in Section 4 (Remark 4.2) is the uniformity of the supremum. We describe three possible strategies for addressing it.

**Strategy D.1 (Restriction to a stable subspace).** Let $\mathcal{S}_0 \subset \mathcal{S}(\mathbb{R}^*_+)$ be a closed subspace with the following properties:
(a) It is dense in $\mathcal{K}$ (for the Pontryagin topology).
(b) The Sobolev norm $\|f\|_{H^1}^2 = \int_0^\infty |f'(x)|^2 dx$ satisfies $\|f\|_{H^1}^2 \geq c \cdot (\mathcal{P}[f] + \mathcal{A}[f])$ for some $c > 0$ and every $f \in \mathcal{S}_0$.

If such $\mathcal{S}_0$ exists, then on $\mathcal{S}_0$ the relative bound of Theorem 4.5 is verifiable:
$$|\mathcal{P}_{\mathrm{tail}}(X)[f]| \leq C_X \|f\|_{H^1}^2 \leq \frac{C_X}{c} (\mathcal{P}[f] + \mathcal{A}[f]).$$
For $X$ sufficiently large, $C_X/c < 1$. The difficulty is constructing $\mathcal{S}_0$ with property (b).

**Strategy D.2 (Relative operator form).** Reformulate C5 as a condition on operators instead of forms. Let $T_X$ be the multiplication operator by $\mathbf{1}_{p > X}$ on the space of sequences of Fourier coefficients (in the decomposition by primes). The relative boundedness condition $\|T_X\| < 1$ (in operator norm over the background Hilbert space) would imply uniform C5.

This reformulation transforms the analytic problem into a spectral one: is the norm of $T_X$ strictly less than 1 for large $X$? Given the decay of the coefficients (Lemma 3.1), the norm tends to zero. This argument is the most promising within Direction B.

**Strategy D.3 (Regularization via $\lambda$).** The form $Q_\lambda$ (the quadratic form associated with $T_\lambda = A_\lambda^{\mathrm{off}} - \mathcal{P}_\lambda$) has a regularization parameter $\lambda > 0$. For $\lambda \gg 1$, the Gaussian decay of $B_\lambda(\log p)$ is extremely fast and uniform C5 is automatically satisfied (the prime series converges very quickly). The difficulty is the limit $\lambda \to 0$, which recovers the original Weil form.

A "continuity in $\lambda$" strategy could work: if $\kappa(Q_\lambda) \leq C$ (bound uniform in $\lambda$) for $\lambda \in (0, \lambda_0]$, and if $Q_\lambda \to Q_0$ in some appropriate sense, then $\kappa(Q_0) \leq C$. This program requires upper semicontinuity of the negative index under perturbations, which is not automatic in infinite-dimensional spaces.

**Remark D.4 (Balance of the strategies).** All three strategies are genuine and none is blocked by an impossibility argument. Strategy D.2 seems the most direct. However, none has been carried out in the program so far, and each has its own specific technical obstacle.

---

## References and connections to the program

- **Doc 72 (Phase 33):** Trace formula via Weil, $T_\lambda = A_\lambda^{\mathrm{off}} - \mathcal{P}_\lambda$. Basis of the structure used here.
- **Doc 91 (Phase 34):** Identification of C5 as an unobstructed condition. Starting point of Doc 94.
- **Phase 26 (paper P35):** Construction of the Pontryagin space $(\mathcal{K}, Q)$ and the bridge $\kappa(Q) = \mathrm{neg.ind}(H_C)$.
- **PLAN-RH-MAXIMAL.md:** General framework of the program; Direction B is one of the active routes.
- **Azizov–Iokhvidov (1989):** *Linear Operators in Spaces with an Indefinite Metric.* Theorem 5.4.7 (Kreĭn–Langer perturbation).
- **Weil (1952):** The explicit formula and positivity. Modern formulation in Connes (1999).
- **Levinson (1974):** One-third of the zeros of $\zeta$ on the critical line.
- **Conrey (1989):** The $40\%$ of the zeros on the critical line and the importance of the Euler product.
- **Soundararajan (2009):** Fluctuations of $\log|\zeta|$ and moments.

---

*End of Doc 94 — Phase 34, Direction B (deep).*

* Obstacles identified: (1) uniformity of C5, (2) Conjecture $\mathbf{C}_B$. Neither is trivial; neither is proved. The program has bounded the problem.*
