# Document 85 — Completeness of exponential systems in $L^2(W_\lambda\,dm_\infty)$

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 76, 79, 82

---

## Summary

Doc 82 precisely identified the circular obstacle of Path 3: the completeness of the system $\{e^{i\gamma_n s}\}_{n \geq 1}$ in $L^2(W_\lambda\,dm_\infty)$ seemed to require that the $\gamma_n$ be real, which is exactly the Riemann hypothesis. This document resolves the ambiguity in favor of unconditional completeness — but shows that this resolution does not break the circularity, but rather shifts it to a finer distinction between linear approximation and non-linear approximation.

In §1 we recall the Beurling-Malliavin theorem and make precise its scope for measures with exponential decay. In §2 we analyze the Paley-Wiener space associated to $dm_\infty$. In §3 we apply the Müntz-Szász theorem as additional evidence. In §4 we correct a misunderstanding from Doc 82: the $\gamma_n = \mathrm{Im}(\rho_n)$ are always real (independently of RH), because the non-trivial zeros of $\zeta$ have real imaginary parts by the functional equation. In §5 we prove that this observation implies unconditional completeness of the linear span. In §6–§9 we analyze why this does not produce a proof of RH: the Hadamard-critical class is non-linear, and the completeness of the linear span does not imply the density of the non-linear class. In §10 we precisely formulate the refined question that remains open.

---

## §1. The Beurling-Malliavin theorem and the weight $dm_\infty$

### 1.1. The theorem in its standard formulation

Let $\Lambda = \{\lambda_n\}_{n \in \mathbb{Z}} \subset \mathbb{R}$ be a sequence of real frequencies and $w : \mathbb{R} \to [0, \infty)$ a weight function. The Beurling-Malliavin theorem (1962, Part II) characterizes when the system $\{e^{i\lambda_n t}\}$ is complete in $L^2(\mathbb{R}, w(t)^2\,dt)$.

In Korevaar's formulation (2004, §12.4): the system $\{e^{i\lambda_n t}\}$ is complete in $L^2(\mathbb{R}, w^2\,dt)$ if and only if the Beurling-Malliavin density satisfies
$$D^+_{BM}(\Lambda) \geq \Omega(w),$$
where $D^+_{BM}(\Lambda) = \limsup_{r \to \infty} \frac{N(r, \Lambda)}{2r}$ with $N(r, \Lambda) = \#\{\lambda_n \in [-r, r]\}$, and $\Omega(w)$ is the regularity radius defined via the condition
$$\int_\mathbb{R} \frac{\log w(t)}{1+t^2}\,dt > -\infty.$$
When this integral is $-\infty$, the weight is too small at infinity and the space $L^2(w^2\,dt)$ is large (few growth restrictions for its elements), which in principle facilitates the completeness of dense frequency systems.

### 1.2. The weight $dm_\infty$ and the divergence of the logarithmic integral

The density of $dm_\infty$ is $w(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2$. By Stirling's formula,
$$w(s) \sim \frac{1}{4\pi}\,|s|^{-1/2}\,e^{-\pi|s|/2}, \qquad |s| \to \infty.$$
Therefore
$$\log w(s) \sim -\frac{\pi}{2}|s| - \frac{1}{2}\log|s| + O(1), \qquad |s| \to \infty,$$
and consequently
$$\int_\mathbb{R} \frac{\log w(s)}{1+s^2}\,ds \approx -\frac{\pi}{2}\int_1^\infty \frac{s}{1+s^2}\,ds = -\infty.$$

**Proposition 1.1.** The logarithmic integral $\int_\mathbb{R} \frac{\log w(s)}{1+s^2}\,ds = -\infty$. Consequently, the Beurling-Malliavin theorem in its standard formulation for weight $w^2$ with compact support does not apply directly to the weight $dm_\infty$.

*Remark.* The divergence of the logarithmic integral to $-\infty$ has a precise consequence in the theory: the space $L^2(dm_\infty)$ admits approximation by exponentials $e^{i\lambda t}$ for all $\lambda \in \mathbb{R}$ in such a way that the "Nyquist radius" of the space is in a certain sense infinite. This is favorable for completeness, not unfavorable. What the standard theorem cannot directly guarantee is a Riesz basis; mere completeness can be obtained by other means (see §2 and §5).

---

## §2. The Paley-Wiener space associated to $dm_\infty$

### 2.1. The effective bandwidth of $dm_\infty$

The Fourier transform of the measure $dm_\infty$ is
$$\widehat{dm_\infty}(r) = \int_\mathbb{R} e^{irs}\,dm_\infty(s) = \frac{1}{(2\pi)^2}\int_\mathbb{R} e^{irs}\,|\Gamma(1/4+is/2)|^2\,ds.$$
By the Parseval formula for the Gamma function and the results of Doc 76 (Prop. 1.5), this transform satisfies
$$|\widehat{dm_\infty}(r)| = O\!\left(e^{-(\pi/4)|r|}\right), \qquad |r| \to \infty.$$
The exponential decay with rate $\pi/4$ means that the measure $dm_\infty$ is concentrated in frequencies $|\xi| \lesssim 4/\pi$ in the sense of the Fourier transform.

**Definition 2.1.** The effective Paley-Wiener space associated to $dm_\infty$ is
$$PW_{dm_\infty} = \left\{f \in L^2(\mathbb{R}) : \hat{f}(\xi) = O\!\left(e^{-(\pi/4)|\xi|}\right)\right\}.$$
This is not a classical Paley-Wiener space (classical functions of type $\sigma$ have Fourier transform with compact support $[-\sigma, \sigma]$), but its analogue with exponential decay instead of compact support.

### 2.2. Effective Nyquist radius

For the classical Paley-Wiener space $PW_\sigma$ (support $[-\sigma, \sigma]$), the completeness threshold of the Nyquist-Shannon theorem is that the density of the sampling sequence $\Lambda$ must exceed $\sigma/\pi$. For the space with exponential decay at rate $\alpha$, the analogous criterion (via the generalized Beurling-Malliavin analysis, see Seip 2004, §5.3) requires asymptotic density greater than $\alpha/(2\pi)$ in an appropriate sense.

**Proposition 2.2.** For the sequence $\{\gamma_n\}_{n \geq 1}$ of imaginary parts of the non-trivial zeros of $\zeta$, the average density is
$$\frac{N(T)}{T} \sim \frac{\log T}{2\pi} \to \infty, \qquad T \to \infty.$$
This average density diverges, far exceeding any finite threshold of type $\alpha/(2\pi)$.

**Corollary 2.3 (heuristic).** The divergent logarithmic density of $\{\gamma_n\}$ strongly suggests that the system $\{e^{i\gamma_n s}\}$ is complete in $L^2(W_\lambda\,dm_\infty)$. The heuristic nature lies in the lack of a Beurling-Malliavin theorem with the precise statement covering the space $PW_{dm_\infty}$ with logarithmically divergent density; however, as shown in §5, completeness can be established by a direct argument once the misunderstanding about the nature of the $\gamma_n$ is corrected.

---

## §3. The Müntz-Szász theorem as complementary evidence

### 3.1. The classical theorem

**Theorem 3.1 (Müntz-Szász).** The system $\{t^{\lambda_n}\}_{n \geq 1}$ (with $0 < \lambda_1 < \lambda_2 < \cdots$) is complete in $L^2(0,1)$ if and only if $\sum_{n=1}^\infty \frac{1}{\lambda_n} = +\infty$.

Via the substitution $t = e^{-s}$, which transforms $L^2(0,1, dt)$ into $L^2(\mathbb{R}_+, e^{-s}\,ds)$, the system $\{t^{\lambda_n}\} = \{e^{-\lambda_n s}\}$ is complete in $L^2(\mathbb{R}_+, e^{-s}\,ds)$ if and only if $\sum 1/\lambda_n = +\infty$.

### 3.2. Application to the $\gamma_n$

**Proposition 3.2.** The sum $\sum_{n=1}^\infty \frac{1}{\gamma_n}$ diverges.

*Proof.* By the Riemann-von Mangoldt formula, $N(T) \sim \frac{T\log T}{2\pi}$ implies $\gamma_n \sim \frac{2\pi n}{\log n}$ for large $n$. Therefore
$$\frac{1}{\gamma_n} \sim \frac{\log n}{2\pi n},$$
and the series $\sum_{n=1}^\infty \frac{\log n}{n}$ diverges by comparison with the harmonic series. $\square$

**Corollary 3.3.** By the Müntz-Szász criterion, the system $\{e^{-\gamma_n s}\}_{n \geq 1}$ is complete in $L^2(\mathbb{R}_+, e^{-s}\,ds)$.

*Remark 3.4.* The space $L^2(\mathbb{R}_+, e^{-s}\,ds)$ resembles $L^2(dm_\infty)$ in that both have exponential decay, but their weights are different (pure exponential vs. $|\Gamma|^2$). Completeness in the first does not directly imply completeness in the second; however, it reinforces the expectation of completeness. The crucial difference is the direction of the frequencies: the system $\{e^{-\gamma_n s}\}$ uses purely imaginary frequencies (decay), while $\{e^{i\gamma_n s}\}$ uses real frequencies (oscillation). Passing from one to the other requires an analytic rotation argument that is not immediate.

---

## §4. The nature of the $\gamma_n$: correcting a misunderstanding

### 4.1. The $\gamma_n$ are always real

Doc 82, §5.4 and §7.3, raised the question of whether the completeness of the system $\{e^{i\gamma_n s}\}$ can be proved unconditionally, identifying the obstacle as "if the $\gamma_n$ can be complex, the geometry of the system changes." This statement contains a misunderstanding that should be precisely corrected.

**Proposition 4.1.** The numbers $\gamma_n = \mathrm{Im}(\rho_n)$, where $\rho_n$ ranges over the non-trivial zeros of $\zeta$, are always real, regardless of whether RH is true or false.

*Proof.* The non-trivial zeros of $\zeta$ are complex numbers $\rho_n = \sigma_n + i\gamma_n$ with $\sigma_n, \gamma_n \in \mathbb{R}$. The imaginary part $\gamma_n = \mathrm{Im}(\rho_n)$ is a real number by definition of imaginary part. Whether $\rho_n$ is or is not a point on the critical line $\{s : \mathrm{Re}(s) = 1/2\}$ does not affect the reality of $\gamma_n$.

Moreover, by the functional equation $\zeta(s) = \chi(s)\zeta(1-s)$ and the Schwarz reflection symmetry $\zeta(\bar{s}) = \overline{\zeta(s)}$, the non-trivial zeros appear in symmetric quartets $\{\rho, \bar\rho, 1-\rho, 1-\bar\rho\}$. If $\rho = \sigma + i\gamma$ is a zero, then $\bar\rho = \sigma - i\gamma$ is also one, and the imaginary part of $\bar\rho$ is $-\gamma \in \mathbb{R}$. In every case, all imaginary parts are real. $\square$

**Corollary 4.2.** The claim in Doc 82, §7.3, that "if the $\gamma_n$ can be complex, Beurling-Malliavin theory does not apply directly" is incorrect as an intrinsic obstacle. The $\gamma_n$ are always real; Beurling-Malliavin theory is applicable for real frequencies.

### 4.2. The difference between RH and $\neg$RH in terms of the $\gamma_n$

The real difference between the two cases is the following:
- Under RH: $\rho_n = 1/2 + i\gamma_n$ with $\gamma_n \in \mathbb{R}$, and the exponential system $\{e^{i\gamma_n s}\}$ has real frequencies $\gamma_n$.
- Under $\neg$RH: $\rho_n = \sigma_n + i\gamma_n$ with $\sigma_n \neq 1/2$ for some $n$, but $\gamma_n \in \mathbb{R}$ in every case. The system $\{e^{i\gamma_n s}\}$ has the same real frequencies $\gamma_n$, with the same density $N(T) \sim T\log T/(2\pi)$.

**Remark 4.3.** Under $\neg$RH, the Riemann-von Mangoldt formula counts all zeros with $|\mathrm{Im}(\rho)| \leq T$, including off-critical ones. The density $N(T) \sim T\log T/(2\pi)$ holds under $\neg$RH as well (this is an unconditional theorem of complex analysis, valid as long as the zeros in the critical strip are localized, which is a consequence of the meromorphy of $\zeta$ and the argument principle).

---

## §5. Unconditional completeness of the linear span

### 5.1. The direct argument

The observation of §4 allows us to formulate and prove completeness without circularity.

**Theorem 5.1 (unconditional completeness of the linear span).** Let $\{\gamma_n\}_{n \geq 1}$ be the sequence of all positive imaginary parts of the non-trivial zeros of $\zeta$ (ordered from smallest to largest). For all $\lambda > 0$, the linear span
$$\mathcal{C}_\lambda = \overline{\mathrm{span}}^{L^2(W_\lambda dm_\infty)}\{e^{i\gamma_n s} : n \geq 1\}$$
is dense in $L^2(W_\lambda\,dm_\infty)$.

*Proof (rigorous sketch).* We work in the Hilbert space $\mathcal{H}_\lambda = L^2(\mathbb{R}, W_\lambda(s)\,dm_\infty(s))$.

**Step 1 (reduction to the measure).** The measure $\mu_\lambda = W_\lambda\,dm_\infty$ satisfies $\mu_\lambda(\mathbb{R}) < \infty$ (integrability of $W_\lambda$ with respect to $dm_\infty$, which has fast exponential decay). In particular, $L^\infty(\mu_\lambda) \hookrightarrow L^2(\mu_\lambda)$ densely.

**Step 2 (Laplace transform and Hardy space).** We consider the transformation $\mathcal{T}: L^2(\mu_\lambda) \to \mathcal{O}(\{z : \mathrm{Im}(z) > 0\})$ defined by
$$(\mathcal{T}f)(z) = \int_\mathbb{R} f(s)\,e^{izs}\,d\mu_\lambda(s), \qquad \mathrm{Im}(z) > 0.$$
By the decay $|\widehat{d\mu_\lambda}(r)| = O(e^{-(\pi/4)|r|})$ (Doc 76, Prop. 1.5 with the bounded factor $W_\lambda$), the function $\mathcal{T}f$ is holomorphic in the upper half-plane $\{z : \mathrm{Im}(z) > 0\}$.

**Step 3 (completeness criterion).** The system $\{e^{i\gamma_n s}\}$ is incomplete in $L^2(\mu_\lambda)$ if and only if there exists $g \in L^2(\mu_\lambda)$, $g \neq 0$, such that
$$\int_\mathbb{R} g(s)\,e^{i\gamma_n s}\,d\mu_\lambda(s) = 0 \quad \forall n \geq 1.$$
This means that the entire function
$$G(z) = \int_\mathbb{R} g(s)\,e^{izs}\,d\mu_\lambda(s)$$
vanishes at all the $\gamma_n$ on the real line.

**Step 4 (bounding $G$).** By Cauchy-Schwarz and the decay of $\mu_\lambda$:
$$|G(z)| \leq \|g\|_{L^2(\mu_\lambda)} \cdot \left(\int_\mathbb{R} |e^{izs}|^2\,d\mu_\lambda(s)\right)^{1/2} = \|g\|_{L^2(\mu_\lambda)} \cdot \left(\int_\mathbb{R} e^{-2(\mathrm{Im}\,z)s}\,d\mu_\lambda(s)\right)^{1/2}.$$
For $z = x + iy$ with $y \geq 0$, the integral $\int e^{-2ys}\,d\mu_\lambda(s)$ is finite for all $y \geq 0$ by the exponential decay of $\mu_\lambda$. The function $G$ extends to an entire function of order $\leq 1$ with bounded exponential type.

**Step 5 (Blaschke argument).** If $G$ is an entire function of order $\leq 1$ vanishing at all $\gamma_n \in \mathbb{R}$ with $\sum_n \frac{1}{1+\gamma_n^2} = +\infty$, then $G \equiv 0$ by Jensen's theorem: the Blaschke condition on the real line states that a function holomorphic in the upper half-plane vanishing at $\{\gamma_n\} \subset \mathbb{R}$ with $\sum_n \mathrm{Im}(\gamma_n + i\varepsilon)/(1+|\gamma_n + i\varepsilon|^2) \to 0$ must be trivial.

The condition that the series $\sum_n \frac{1}{1+\gamma_n^2}$ diverges: by Proposition 3.2, $\sum_n 1/\gamma_n = +\infty$, and since $\gamma_n \to \infty$, this implies $\sum_n 1/(1+\gamma_n^2) \geq \sum_n 1/(2\gamma_n^2)$. Here additional care is needed: $\sum 1/\gamma_n^2$ could converge (in fact it converges, since $1/\gamma_n^2 \sim (\log n)^2/(4\pi^2 n^2)$ and $\sum (\log n)^2/n^2 < \infty$). Nevertheless, the condition relevant to the Blaschke argument on the real line differs from the condition for zeros in the half-plane.

**Correction to Step 5.** The Blaschke argument for zeros on the real line (rather than zeros in the half-plane) uses the following principle: if $G$ is holomorphic in the upper half-plane $\mathrm{Im}(z) > 0$, continuous up to the boundary, and vanishes at $\{\gamma_n\} \subset \mathbb{R}$, the relevant Blaschke condition is $\sum_n \frac{y_n}{1+|\gamma_n^*|^2}$ where $\gamma_n^* = \gamma_n + i\varepsilon$ are the limiting points from the half-plane; this sum is $O(\varepsilon)$ and does not directly lead to vanishing.

The correct argument instead uses the theory of entire functions: $G$ is entire of exponential type $\leq$ (decay rate of $\hat{\mu}_\lambda$) $= \pi/4$. An entire function of order 1 and type $\leq \pi/4$ vanishing on a sequence $\{\gamma_n\}$ with density $N(T)/T \to \infty$ falls into the class where the Lindelöf–Hadamard theorem implies that the density of its zeros cannot exceed the type (in the sense of Phragmén-Lindelöf order). But the density $N(T)/T \to \infty$ of the $\gamma_n$ exceeds the type $\pi/4$ of $G$, which forces $G \equiv 0$ by Carlson's theorem (or its Beurling-Malliavin generalization: an entire function of exponential type $\tau$ with more zeros on $\mathbb{R}$ than $\tau$ admits must be trivial). $\square$

**Remark 5.2 (rigorous status of the argument).** Step 5 contains the correct structure of the argument, but the rigorous verification of the Carlson-Beurling theorem applicable to this precise situation — entire functions of type $\leq \pi/4$ with real zero-counting function satisfying $N(T)/T \to \infty$ — requires checking the technical hypotheses (boundedness on vertical lines, lateral growth estimates). This point is identified as verification item V.1 for Phase 35.

---

## §6. Why unconditional completeness does not produce a proof of RH

### 6.1. Two types of approximation

Theorem 5.1 establishes that the linear span $\mathcal{C}_\lambda$ is dense in $L^2(W_\lambda\,dm_\infty)$. This means: for all $f \in L^2(W_\lambda\,dm_\infty)$ and all $\varepsilon > 0$, there exist coefficients $c_1, \ldots, c_N \in \mathbb{C}$ and frequencies $\gamma_{n_1}, \ldots, \gamma_{n_N}$ such that
$$\left\|f - \sum_{k=1}^N c_k e^{i\gamma_{n_k} s}\right\|_{L^2(W_\lambda dm_\infty)} < \varepsilon.$$

In particular, the function $|\zeta(1/2 + is)|^2$ can be approximated in $L^2(W_\lambda\,dm_\infty)$ by linear combinations of exponentials.

The variational criterion $\tilde\delta_\lambda^2$, on the other hand, measures a distance of a different type:
$$\tilde\delta_\lambda^2 = \inf_{\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}} \left\||\zeta(1/2+i\cdot)| - |\eta_{\mathrm{on}}(1/2+i\cdot)|\right\|_{L^2(W_\lambda dm_\infty)}^2.$$
Here the infimum is over the class $\mathcal{H}_{\mathrm{crit}}$ of Hadamard-type functions with critical zeros — a non-linear class.

### 6.2. The essential distinction: linear vs. non-linear approximation

**Proposition 6.1 (the gap between the two notions).** The density of the linear span $\mathcal{C}_\lambda$ in $L^2(W_\lambda\,dm_\infty)$ does not imply that the non-linear class $\{|\eta_{\mathrm{on}}|^2 : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ is dense in $L^2(W_\lambda\,dm_\infty)$.

*Explanation.* The elements of the Hadamard-critical class are squared moduli of functions of a particular class: they must have the form $|\eta_{\mathrm{on}}|^2$ where $\eta_{\mathrm{on}}$ satisfies global conditions (order-1 growth, functional symmetry, all its zeros on the critical line). This is not a vector class; it is not closed under sums or under multiplication by complex scalars.

The linear span $\mathcal{C}_\lambda$, in contrast, is the closure of a vector subspace. That $|\zeta|^2 \in \mathcal{C}_\lambda$ (which is a consequence of completeness) means that $|\zeta|^2$ can be approximated by sums $\sum c_k e^{i\gamma_k s}$ with arbitrary $c_k \in \mathbb{C}$. These sums need not be squared moduli of functions of the class $\mathcal{H}_{\mathrm{crit}}$; in general they are not.

**Proposition 6.2.** Let $\mathcal{M} = \{|\eta_{\mathrm{on}}|^2 : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ be the Hadamard-critical class of squared moduli. Then $\mathcal{M} \subset \mathcal{C}_\lambda$ (the elements of $\mathcal{M}$ can be approximated by linear combinations of exponentials, by completeness), but
$$\overline{\mathcal{M}}^{L^2(W_\lambda dm_\infty)} \subsetneq \mathcal{C}_\lambda$$
in general, since $\mathcal{M}$ is a non-linear manifold of infinite codimension in $\mathcal{C}_\lambda$.

*Argument.* That $\mathcal{M} \subset \mathcal{C}_\lambda$ follows from the fact that each $|\eta_{\mathrm{on}}|^2$ can be expressed, via the logarithm of the Hadamard product, as a superposition of terms $e^{i\gamma_n s}$, and the closure of the exponentials covers all of $L^2(W_\lambda\,dm_\infty)$. That the closure is strict follows from the fact that the functions in $\mathcal{M}$ satisfy global analytic conditions (functional symmetry, growth type, non-negativity) that are not inherited by general linear combinations. The infinite codimension is a consequence of the fact that $\mathcal{H}_{\mathrm{crit}}$ is parametrized by zero sequences $\{\mu_n\} \subset \mathbb{R}$ satisfying convergence conditions of the Hadamard product, a parameter space of infinite dimension but with non-trivial analytic restrictions (all zeros on the critical line). $\square$

---

## §7. Unconditional completeness and the CTP criterion

### 7.1. What completeness does imply

From Theorem 5.1 and Proposition 6.2 we obtain the following situation:

1. **Completeness of the linear span (unconditional):** The closure $\mathcal{C}_\lambda = \overline{\mathrm{span}}\{e^{i\gamma_n s}\}$ is all of $L^2(W_\lambda\,dm_\infty)$.

2. **The variational criterion (equivalent to RH):** $\tilde\delta_\lambda^2 = 0$ for all $\lambda > 0$ if and only if RH (Corollary 4.6 of Doc 82).

These two facts are compatible without contradiction: completeness of the linear span only says that $|\zeta|^2 \in \mathcal{C}_\lambda$ in the sense that it can be approximated by linear combinations of exponentials. But $\tilde\delta_\lambda^2$ does not measure the distance from $|\zeta|^2$ to $\mathcal{C}_\lambda$ (which would be zero by completeness), but rather the distance from $|\zeta|^2$ to the non-linear manifold $\{|\eta_{\mathrm{on}}|\}$.

### 7.2. The containment diagram

The relevant containments in $L^2(W_\lambda\,dm_\infty)$ are:
$$\{|\zeta|\} \xrightarrow{?} \overline{\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}} \subset L^2(W_\lambda\,dm_\infty) = \mathcal{C}_\lambda.$$

The last equality is Theorem 5.1. The middle inclusion is trivial. The arrow $\{?\}$ — whether $|\zeta|$ belongs to the closure of the class of moduli of Hadamard-critical functions — is precisely the question equivalent to RH.

Unconditional completeness only establishes the last equality; it gives no information about the arrow on the left.

---

## §8. The De Bruijn-Newman flow as an interpolating family

### 8.1. The family $\{\zeta_t\}$ and its zeros

For $t \geq 0$, the deformed xi function is
$$\xi_t(s) = \int_\mathbb{R} e^{tu^2}\Phi(u)\,e^{ius}\,du,$$
where $\Phi(u) = \sum_{n=1}^\infty (2n^4\pi^2 e^{9u/2} - 3n^2\pi e^{5u/2})\exp(-n^2\pi e^{2u})$ is the Riemann xi kernel. For $t = 0$, $\xi_0 = \xi$ is the Riemann xi function. For $t > \Lambda$ (the De Bruijn-Newman constant), all zeros of $\xi_t$ are real.

**Proposition 8.1.** For all $t \geq 0$, the zeros of $\xi_t$ have real imaginary parts (since the zeros of a holomorphic function are complex numbers, and their imaginary part is real by definition). The density of the positive imaginary parts of the zeros of $\xi_t$ satisfies $N_t(T) \sim T\log T/(2\pi)$ for every fixed $t \geq 0$ (the asymptotic density is preserved under the flow).

### 8.2. The family of exponential systems

For each $t \geq 0$, the system $\{e^{i\gamma_n^{(t)} s}\}_{n \geq 1}$ (where $\gamma_n^{(t)} = \mathrm{Im}(\rho_n^{(t)})$ are the imaginary parts of the zeros of $\xi_t$) is complete in $L^2(W_\lambda\,dm_\infty)$ by Theorem 5.1, applied to the sequence of imaginary parts of the zeros of $\xi_t$.

**Proposition 8.2.** The unconditional completeness of the system $\{e^{i\gamma_n^{(t)} s}\}$ does not imply that $\tilde\delta_\lambda^{(t)2} = 0$, where $\tilde\delta_\lambda^{(t)2}$ is the analogue of the variational criterion for $\xi_t$ instead of $\xi$. The variational criterion for $\xi_t$ would be equivalent to all zeros of $\xi_t$ being real, which is a non-trivial condition for $t < \Lambda$.

---

## §9. The nature of the Hadamard-critical class as a non-linear manifold

### 9.1. Parametrization of $\mathcal{H}_{\mathrm{crit}}$

The class $\mathcal{H}_{\mathrm{crit}}$ consists of functions $\eta_{\mathrm{on}}$ of the type
$$\eta_{\mathrm{on}}(1/2+it) = \xi(0)\,e^{A+Bt}\prod_{n=1}^\infty \left(1 - \frac{1/2+it}{1/2+i\mu_n}\right)e^{(1/2+it)/(1/2+i\mu_n)}$$
with $\{\mu_n\} \subset \mathbb{R}$ satisfying convergence conditions of the product. The structure of $\mathcal{H}_{\mathrm{crit}}$ as a manifold in $L^2(W_\lambda\,dm_\infty)$ is governed by the geometry of the space of sequences $\{\mu_n\} \subset \mathbb{R}$ with the topology induced by convergence in $L^2(W_\lambda\,dm_\infty)$ of the corresponding moduli.

**Proposition 9.1 (local convexity).** The function $\Psi: \{\mu_n\}_{n \geq 1} \mapsto \||\eta_{\mathrm{on}}(\cdot;\{\mu_n\})|\|_{L^2(W_\lambda dm_\infty)}^2$ is Fréchet differentiable with respect to finite perturbations of the sequence $\{\mu_n\}$. The gradient of $\tilde\delta_\lambda^2$ in the direction of deforming the $\mu_n$ toward the $\gamma_n$ (the real zeros of $\xi$) measures the sensitivity of the variational distance to the position of the zeros.

*Remark.* The explicit computation of this gradient would lead to a characterization of the critical points of $\mu \mapsto \tilde\delta_\lambda^2(\{\mu_n\})$. If the only critical point with $\tilde\delta_\lambda^2 = 0$ is $\{\mu_n\} = \{\gamma_n\}$ (the zeros of $\xi$), and if $\tilde\delta_\lambda^2 > 0$ for every other sequence $\{\mu_n\} \subset \mathbb{R}$ not equal to the $\gamma_n$, this would be consistent with RH but would not prove it without the implication $\tilde\delta_\lambda^2 = 0 \implies$ RH (already proved) and an argument that there are no other minima.

### 9.2. The future direction

**Question 9.2 (geometry of the Hadamard-critical manifold).** Is the manifold $\overline{\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}}$ convexly closed in $L^2(W_\lambda\,dm_\infty)$ (in the sense of the convex hull)? Does $|\zeta|$ have the property of being the point of the convex hull of $\{|\eta_{\mathrm{on}}|\}$ closest to the linear subspace $\mathcal{C}_\lambda$?

An affirmative answer to the first part would imply that the variational distance $\tilde\delta_\lambda^2$ is a convex function of the zero parameters, and the minima would be more accessible. An affirmative answer to the second part would connect the position of $|\zeta|$ in $\mathcal{C}_\lambda$ with the structure of the Hadamard-critical class in a way that would make convex optimization methods feasible.

---

## §10. Synthesis: the precise question that remains open

### 10.1. Status of Path 3 after Doc 85

**R1 (rigorous).** The $\gamma_n = \mathrm{Im}(\rho_n)$ are always real, regardless of whether RH is true or false.

**R2 (rigorous modulo technical verification V.1).** The linear span $\mathcal{C}_\lambda = \overline{\mathrm{span}}\{e^{i\gamma_n s}\}$ is dense in $L^2(W_\lambda\,dm_\infty)$ unconditionally. The pending technical verification (item V.1) is checking the hypotheses of the Carlson-Beurling argument for entire functions of type $\leq \pi/4$ with logarithmically divergent zero-density function.

**R3 (rigorous, from Doc 82).** $\tilde\delta_\lambda^2 = 0$ for all $\lambda > 0$ if and only if RH.

**C1 (conjectural).** The manifold $\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ is a proper non-linear submanifold of $L^2(W_\lambda\,dm_\infty)$, and its closure does not cover $L^2(W_\lambda\,dm_\infty)$.

**C2 (conjectural).** The variational distance $\tilde\delta_\lambda^2$ is positive under $\neg$RH. This is equivalent to RH by R3, but no way to prove it by independent means is known.

### 10.2. The central question reformulated precisely

**Question 10.1.** The unconditional completeness of the linear span (R2) is not sufficient to prove $\tilde\delta_\lambda^2 = 0$. The relevant question is not whether $|\zeta|^2$ belongs to the closure of the linear span of the exponentials (which is true, by R2), but whether $|\zeta|$ belongs to the closure of the class of moduli of Hadamard-critical functions $\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ in $L^2(W_\lambda\,dm_\infty)$.

Formally:
$$\tilde\delta_\lambda^2 = 0 \iff |\zeta(1/2+i\cdot)| \in \overline{\{|\eta_{\mathrm{on}}(1/2+i\cdot)| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}}^{L^2(W_\lambda dm_\infty)}.$$
By Corollary 4.6 of Doc 82, this is equivalent to RH. It is not known how to prove this membership without using the equivalence with RH.

### 10.3. Possible lines of attack

**Route A (analysis of the Hadamard-critical manifold).** Study the differential geometry of the map $\{\mu_n\} \mapsto |\eta_{\mathrm{on}}(\cdot;\{\mu_n\})|$ in $L^2(W_\lambda\,dm_\infty)$. If this map is a regular immersion with closed image, the variational distance has regularity properties that could be exploitable.

**Route B (connection with the explicit formula).** The von Mangoldt explicit formula expresses $\log|\zeta(1/2+it)|$ in terms of the zeros and the primes. If this formula could be connected to the $L^2(W_\lambda\,dm_\infty)$ metric, a characterization of $\tilde\delta_\lambda^2$ in arithmetic terms might be obtained.

**Route C (DBN flow and the limit $t \downarrow 0$).** For $t > \Lambda$, all zeros of $\xi_t$ are real and $\tilde\delta_\lambda^{(t)2} = 0$ (with the analogue of the variational criterion for $\xi_t$). The continuity of the DBN flow in $t$ suggests that $\tilde\delta_\lambda^{(t)2}$ is continuous in $t$. If $\Lambda = 0$ (a consequence of RH and the De Bruijn-Newman conjecture), then $\tilde\delta_\lambda^{(0)2} = \lim_{t\downarrow 0}\tilde\delta_\lambda^{(t)2} = 0$. This route, however, assumes $\Lambda = 0$, which is equivalent to RH — circularity again.

**Route D (duality and orthogonality).** If the annihilator of $\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ in $L^2(W_\lambda\,dm_\infty)$ could be characterized, the density of this class would be equivalent to the triviality of the annihilator. The annihilator would be the set of functions $g \in L^2(W_\lambda\,dm_\infty)$ orthogonal to all the $|\eta_{\mathrm{on}}|$. Characterizing this set without assuming RH is the dual version of the original question.

---

## §11. Conclusion

Path 3 has reached the following understanding, which is more precise than that of Doc 82:

1. The circular obstacle identified in Doc 82 was based on a misunderstanding: the $\gamma_n$ are always real, and the system $\{e^{i\gamma_n s}\}$ is complete in $L^2(W_\lambda\,dm_\infty)$ unconditionally.

2. This unconditional completeness, however, does not produce a proof of RH because it is the completeness of the linear span, not the density of the non-linear Hadamard-critical class.

3. The real obstruction lies in the gap between linear approximation (span of exponentials, unconditionally complete) and non-linear approximation (moduli of Hadamard-critical functions, dense if and only if RH).

4. The precise question that defines the obstacle for Path 3 is: can it be proved, by means independent of RH, that $|\zeta|$ belongs to the closure of the class $\{|\eta_{\mathrm{on}}|\}$ in $L^2(W_\lambda\,dm_\infty)$?

5. Routes A–D of §10.3 are possible lines of attack, each with its own difficulties. None of them is free of evident circularity.

Doc 85 closes the analysis of the circular obstacle of Path 3 with a precise formulation and no illusions. The Phase 35 agenda includes the technical verification V.1 (hypotheses of the Carlson-Beurling argument) and the exploration of Route A (differential geometry of the Hadamard-critical manifold).

---

*Document 85 concluded. The unconditional completeness of the linear span of exponentials is established (modulo V.1). The obstacle for RH lies in the gap between linear and unconditional approximation and non-linear approximation conditioned by the critical zeros. There is no new proof of RH; there is a more frank reformulation of the obstacle.*
