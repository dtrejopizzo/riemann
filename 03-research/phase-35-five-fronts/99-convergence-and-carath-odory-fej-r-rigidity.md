# Document 99 — Convergence $H_x \to H_\infty$ and Carathéodory–Fejér rigidity in the CCM spectral triples

**Program:** Riemann Hypothesis — Phase 35 (five fronts)
**Prerequisites:** Docs 64, 68, 69, 83, 89, 92, 96; P39, P40; meta-docs/NOVEL-STRUCTURE-SEARCH-survivors.md
**Verified external sources:** arXiv:2511.22755 (Connes–Consani–Moscovici, *Zeta Spectral Triples*, Nov. 2025 — full text verified); arXiv:2511.23257 = Commun. Math. Phys. **406**:312 (2025) (Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* — abstract and main statements verified); arXiv:2602.04022 (Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, Feb. 2026 — abstract and structure verified); arXiv:2605.20224 (Groskin — abstract only verified, purely numerical paper, cited only as literature evidence).

---

## 1. Purpose of this document

Recent work by Connes–Consani–Moscovici (hereafter **CCM-ZST**, arXiv:2511.22755) constructs, for each $\lambda > 1$ and $N \in \mathbb{N}$, a self-adjoint operator
$$H_x := D_{\log}^{(\lambda,N)}, \qquad x = \lambda^2,$$
whose spectrum is **unconditionally real** and which, according to the paper's own numerical evidence, approximates the low zeros of $\zeta(\tfrac12 + is)$ with extraordinary precision: using only the primes $\leq 13$ (six primes), the first 50 zeros are reproduced with errors ranging from $2.5 \times 10^{-55}$ (first zero) to $\approx 10^{-3}$ (zero 50) [CCM-ZST, §1; Connes 2602.04022 reports the same experiment]. The structural ingredient guaranteeing the reality of the spectrum is a generalization, proved by Connes–van Suijlekom (hereafter **CvS**), of the Carathéodory–Fejér (1911) structure theorem for Toeplitz matrices.

This document answers six questions:

(i) what exactly CF rigidity is and how it enters the construction of $H_x$;
(ii) **discriminating question**: is CF rigidity disguised positivity (a Kurasov–Sarnak → Lee–Yang → CAP collapse), or a genuinely distinct mechanism?;
(iii) what precisely is the obstruction to convergence $H_x \to H_\infty$, formulated mathematically;
(iv) whether the program's own tools (exact Wronskian, sum rule, HS perturbation) give control over that convergence;
(v) which non-circular intermediate statements are provable;
(vi) verdict.

**Convention.** "OPEN GAP" marks unproved steps. Everything not verified against sources carries [NOT VERIFIED].

---

## 2. The CCM-ZST construction of $H_x$ (exact, verified summary)

### 2.1. The semilocal Weil form $QW_\lambda$

Let $W(\mathbb{R}^*_+)$ be the Weil class of test functions. The explicit Weil formula, in the normalization of CCM-ZST §3, defines the functional
$$\Psi(F) := W_{0,2}(F) - W_{\mathbb{R}}(F) - \sum_p W_p(F),$$
where $W_{0,2}(F) = \widehat{F}(i/2) + \widehat{F}(-i/2)$ is the (positive, rank-2 after truncation) contribution of the poles of $\zeta$,
$$W_p(F) = (\log p)\sum_{m=1}^{\infty} p^{-m/2}\bigl(F(p^m) + F(p^{-m})\bigr)$$
is the local distribution at $p$, and $W_{\mathbb{R}}$ is the archimedean contribution, given in Fourier by the multiplier $2\,\partial_t\theta(t)/2\pi$ with $\theta$ the Riemann–Siegel angle function. The **Weil quadratic form** is $QW(f,g) = \Psi(f^* \!*\! g)$ (convolution on $\mathbb{R}^*_+$).

The **semilocal** form $QW_\lambda$ is the restriction to $L^2([\lambda^{-1},\lambda], d^*u)$ (functions extended by $0$ outside the interval). Decisive structural point:

> **Automatic locality.** If $f, g$ are supported in $[\lambda^{-1},\lambda]$, then $f^*\!*\!g$ is supported in $[\lambda^{-2},\lambda^2]$, so that $W_p(f^*\!*\!g) = 0$ for every $p^m > \lambda^2$. The "finite Euler product over $p \leq x = \lambda^2$" **is not a truncation imposed by hand**: it is an exact consequence of the support. [CCM-ZST, abstract and §3 — verified.]

### 2.2. Discrete spectrum and the quantity $\mu_\lambda$

CCM-ZST prove (Prop. 3.3, Thm. 3.6, using the theory of forms of Schmüdgen, GTM 265):

- $QW_\lambda$ is bounded below and lower semicontinuous; it defines a self-adjoint operator $A_\lambda$ with **discrete spectrum bounded below** (the compactness comes from the growth $\partial_t\theta(t) \sim \tfrac12\log|t|$ of the archimedean multiplier).
- Let $\mu_\lambda := \inf \mathrm{spec}(A_\lambda)$. Then $\mu_\lambda$ is **decreasing in $\lambda$** (eq. (3.27)).
- **Corollary 3.8 (CCM-ZST):** if $\lim_{\lambda\to\infty}\mu_\lambda = 0$, then RH.

Conversely, by Weil's criterion (positivity of $QW$ on $C_c^\infty(\mathbb{R}^*_+)$ $\iff$ RH), one has RH $\Rightarrow \mu_\lambda \geq 0$ for all $\lambda$, hence $\lim \mu_\lambda \geq 0$. That is:
$$\boxed{\;\lim_{\lambda\to\infty}\mu_\lambda \geq 0 \iff \text{RH}\;}$$
(the $\Leftarrow$ direction is Weil; the $\Rightarrow$ direction is Cor. 3.8 plus the observation that under $\neg$RH there exists a compactly supported $f$ with $QW(f,f) < 0$). Whether the limit is exactly $0$ and not strictly positive under RH is plausible (the zeros of $\Xi$ force an asymptotic radical) but we do not need it: **the RH content of the family $\{\mu_\lambda\}$ is the sign of the limit**. This is MW-1 in semilocal form and MW-6 (uniform spectral gap) in literal form.

### 2.3. Truncation $E_N$ and the matrix structure

Let $V_n = \kappa(U_n)$ be the Fourier basis transported to $[\lambda^{-1},\lambda]$, $E_N = \mathrm{span}\,\{V_n : |n| \leq N\}$ (the $2N+1$ eigenvectors of the scaling operator $D_{\log}^{(\lambda)} = -iu\,\partial_u$ with periodic conditions, of minimal eigenvalue). The matrix $\tau = QW_\lambda^N$ in this basis has the **special structure** (CCM-ZST, Lemma 5.1):
$$\tau_{ii} = a_i, \qquad \tau_{ij} = \frac{b_i - b_j}{i-j} \ (i \neq j), \qquad a_{-j} = a_j,\ b_{-j} = -b_j,$$
equivalently (Lemma 5.2): with $D = \mathrm{diag}(n)$ and the grading $\gamma(V_j) = V_{-j}$,
$$[D, \tau] = |\beta\rangle\langle\eta| - |\eta\rangle\langle\beta|, \qquad \tau\gamma = \gamma\tau,$$
i.e., **the commutator with $D$ has rank $\leq 2$**. This is the class of matrices to which the CvS theorem applies (§3 below). Note: it is the exact analogue, for the pair (Loewner, differentiation), of the characterization of Toeplitz matrices by $[S,T]$ of rank $\leq 2$ with $S$ the shift.

### 2.4. The operator $H_x = D_{\log}^{(\lambda,N)}$ and Theorem 5.10

Let $\epsilon_N$ be the minimal eigenvalue of $QW_\lambda^N$, **assumed simple with even eigenvector $\xi$** ("even-simple"; computationally verifiable for each finite $(\lambda,N)$), normalized by $\delta_N(\xi) = 1$ where $\delta_N$ is the Dirichlet kernel (approximation to boundary evaluation at $u = \lambda$). One defines
$$D_{\log}^{(\lambda,N)} := D_{\log}^{(\lambda)} - |D_{\log}^{(\lambda)}\xi\rangle\langle\delta_N| \qquad \text{(rank-one perturbation).}$$

**Theorem 5.10 (CCM-ZST — proved, verified against the text):**
(i) $D_{\log}^{(\lambda,N)}$ is **self-adjoint** on $E_N' \oplus E_N^{\perp}$, where on $E_N' = E_N/\mathbb{C}\xi$ the inner product is the one given by the form
$$T := QW_\lambda^N - \epsilon_N \cdot \mathrm{id} \;\geq\; 0.$$
(ii) Its regularized determinant is $\det\nolimits_{\mathrm{reg}}(D_{\log}^{(\lambda,N)} - z) = -i\,\lambda^{-iz}\,\widehat{\xi}(z)$, with $\widehat{\xi}$ the Fourier transform of $\xi$ for the duality $\langle \mathbb{R}^*_+ | \mathbb{R}\rangle$.
(iii) $\widehat{\xi}(z)$ is entire and **all of its zeros are real**, and coincide with $\mathrm{spec}(D_{\log}^{(\lambda,N)})$.

We underline the self-adjointness mechanism: the inner product is $T = QW^N_\lambda - \epsilon_N$, which is $\geq 0$ **by construction** (shift by the minimal eigenvalue), with radical exactly $\mathbb{C}\xi$. The shift only changes the diagonal $a_i \mapsto a_i - \epsilon_N$, so it **preserves the structure** of §2.3.

### 2.5. What is proved and what is conjecture in CCM-ZST

| Statement | Status in CCM-ZST |
|---|---|
| Discrete spectrum of $A_\lambda$; $\mu_\lambda$ decreasing | Proved (Thm. 3.6) |
| $\lim\mu_\lambda = 0 \Rightarrow$ RH | Proved (Cor. 3.8) |
| Structure $(a_i, (b_i-b_j)/(i-j))$ of the truncated matrix | Proved (Lemma 5.1) |
| Self-adjointness of $H_x$, reality of the spectrum, $\det_{\mathrm{reg}} = -i\lambda^{-iz}\widehat{\xi}(z)$ | Proved (Thm. 5.10), **conditional on even-simplicity of the truncation** (verifiable case by case) |
| Even-simplicity of $QW_\lambda$ (level $N = \infty$) | **OPEN** (missing step 1, §8 of CCM-ZST) |
| $\xi_\lambda \approx k_\lambda$ (prolate approximation) | **OPEN** — "the main remaining obstacle to our approach to RH" (§7) |
| Convergence of spectra to the zeros of $\zeta$ | **Conjecture** supported numerically; "a rigorous proof of this convergence would establish RH" (abstract) |

Additional literature evidence [Groskin, arXiv:2605.20224, abstract only verified]: an independent implementation reproduces the convergence (the error of the first zero decreases monotonically to $\sim 10^{-168}$ with primes $\leq 67$) and reports that the truncated matrices have **negative eigenvalues** (3 to 11 negative eigenvalues depending on $N$, at $x = 100$). This confirms a structural point used in §4: the truncated form is **not** positive in general; the method does not need it to be.

---

## 3. (i) Carathéodory–Fejér rigidity: precise statement and role in the construction

### 3.1. The classical CF problem and its structure theorem (1911)

Two faces of the same object:

**(CF-a) Carathéodory coefficient problem / positive extension.** Given $c_0, \dots, c_N \in \mathbb{C}$, does there exist a positive measure $\mu$ on the circle $S^1$ with trigonometric moments $\widehat{\mu}(k) = c_k$, $|k| \leq N$? Answer (Carathéodory–Toeplitz): yes $\iff$ the Toeplitz matrix $T_N = (c_{i-j})_{0\le i,j\le N}$ is positive semidefinite. Interior case ($T_N > 0$): infinitely many extensions (Schur/Nevanlinna–Pick parametrization). **Boundary case** ($T_N \geq 0$ singular): the extension is **unique** and the measure is **forced** to be atomic,
$$\mu = \sum_{j=1}^{r} \rho_j\,\delta_{e^{i\theta_j}}, \qquad r = \mathrm{rank} T_N \leq N,$$
and every vector $\xi \in \ker T_N$ has associated polynomial $P_\xi(z) = \sum \xi_j z^j$ with **all its zeros on the unit circle** (the atoms $e^{i\theta_j}$ are among them). This boundary uniqueness is **CF rigidity**.

In expanded form, the corollary that CvS generalize is:

> **CF corollary (form used).** Let $T_N = (c_{i-j})_{0 \leq i,j \leq N}$ be a Hermitian Toeplitz matrix, $T_N \geq 0$, $\mathrm{rank}(T_N) = N$ (corank 1), and let $0 \neq \xi = (\xi_0, \dots, \xi_N) \in \ker T_N$. Then the polynomial $P_\xi(z) = \sum_{j=0}^N \xi_j z^j$ has its $N$ zeros on $S^1 = \{|z| = 1\}$, and the (unique) representing measure $\mu \geq 0$ of the moments $c_k$ is supported on those zeros.

The intuition of the proof (in CvS's C*-algebraic version): $T_N \geq 0$ singular means that the sesquilinear form "touches zero" at $\xi$; the Toeplitz structure ($[S, T]$ of rank $\leq 2$, $S$ = shift) turns the null vector into an approximate eigenvector of the unitary shift in the GNS representation, and the eigenvalues of a unitary live on $S^1$.

**(CF-b) Carathéodory–Fejér extremal problem / minimal-norm Pick–Nevanlinna.** Given a polynomial $p(z) = c_0 + \dots + c_N z^N$, minimize $\|f\|_{H^\infty}$ among the $f$ holomorphic on the disk with the same first coefficients. The 1911 theorem identifies the unique extremal as a scalar multiple of a Blaschke product (constant modulus on the boundary); the minimal norm is the norm of the associated Hankel/Toeplitz matrix. The rigidity is the same as in (CF-a) read in the equality case: **when the quadratic form touches its bound, the representing object becomes rigid and its zeros fall on the boundary** ($S^1$).

What matters for what follows: CF rigidity is a theorem of the form

> *semidefinite positivity + singularity (touching zero) $\Rightarrow$ zero localization on the boundary.*

The input is a positivity; the output is real-rootedness (in the appropriate chart: circle $\leftrightarrow$ real line).

### 3.2. The generalization by Connes–van Suijlekom (CMP 406:312, 2025)

CvS prove [verified at the level of abstract and statements; the full proof of the paper was not inspected line by line — the statements match the use CCM-ZST makes of them]:

**Theorem (CvS, matrix version).** Let $\tau$ be real symmetric of size $(2N+1)$ with the structure $\tau_{ii} = a_i$, $\tau_{ij} = (b_i - b_j)/(i-j)$, commuting with the grading $\gamma$. If $\tau \geq 0$ and $\xi \in \ker\tau$ is even, then the entire function $\widehat{\xi}(z) = \sum_j \xi_j\,\widehat{V_j}(z)$ (Fourier transform of the corresponding combination on the interval) has **all its zeros real**.

**Theorem (CvS, continuous version).** Let $D$ be a real distribution on an interval whose associated quadratic form defines a self-adjoint, bounded-below operator with minimal eigenvalue **simple and isolated** and **even** eigenfunction $\xi$. Then all zeros of $\widehat{\xi}$ lie on the real line.

The proof proceeds in five steps (per the CvS abstract): a C*-algebraic proof of the classical CF corollary; the continuous analogue (Toeplitz $\to$ convolution operator); truncations; the structured analogue; and Hurwitz's theorem on zeros of uniform limits of holomorphic functions. The circle-to-line translation is the expected one: the role of the unit circle is taken by $\mathbb{R}$, that of the shift by the scaling generator $D$, and that of "Toeplitz" by "$[D,\tau]$ of rank $\leq 2$".

### 3.3. How it enters $H_x$: the exact point

CF rigidity **does not apply to $QW_\lambda^N$** (which in general is not $\geq 0$: it has negative eigenvalues, see §2.5). It applies to
$$T = QW_\lambda^N - \epsilon_N\cdot\mathrm{id},$$
which is $\geq 0$ **tautologically** and singular **tautologically** (its kernel is the minimal eigenspace). The remaining non-trivial hypothesis is even-simplicity ($\dim\ker T = 1$, $\gamma\xi = \xi$), which at the finite level is a non-degeneracy check, not a positivity.

The full logical chain of CCM-ZST is then:

```
spectral shift (tautological)          even-simplicity (verifiable at finite level)
        |                                       |
        v                                       v
   T ≥ 0 singular  --------- CF rigidity -----> zeros of ξ̂ real   [UNCONDITIONAL]
                                                |
                                                v
                          spectrum of H_x real = zeros of ξ̂       [UNCONDITIONAL]
                                                |
              det_reg(H_x − z) → Ξ(z)?  (limits N→∞, λ→∞)         [OPEN]
                                                |
                                                v  (Hurwitz)
                                              RH
```

The first three steps are theorems. **All the unproved arithmetic content lives in the fourth.**

---

## 4. (ii) Discriminating question: disguised positivity?

### 4.1. The precedent to be surpassed: Kurasov–Sarnak

Recall the collapse documented in NOVEL-STRUCTURE-SEARCH-survivors.md (Candidate A): "quasicrystalline rigidity" looked like a discreteness/rigidity mechanism capable of forcing zeros onto a line without positivity. Kurasov–Sarnak [arXiv:2307.13498] proved that every 1-D Fourier quasicrystal with values in $\mathbb{N}$ is the toral zero set of a **Lee–Yang** (stable) polynomial. But stability = real-rootedness = positivity of Hermite forms = CAP. That is: **the structural hypothesis was, unknowingly, equivalent to the positivity whose instance for $\zeta$ is RH.** Using it for RH is circular: FAIL I2a.

The question is whether CF rigidity repeats this pattern. The shape of the KS pattern is:

> (KS) *To conclude "the zeros of the limiting arithmetic object are real" one assumes a structural property of the limiting object that is equivalent to an RH-equivalent positivity.*

### 4.2. Fine analysis: two positivities that must not be confused

In the CCM-ZST construction, two positivities of completely different logical nature coexist:

**(P-in) — input positivity.** $T = QW_\lambda^N - \epsilon_N \geq 0$. It is **tautological**: it holds for any symmetric matrix in the world, with no arithmetic content whatsoever. It is also **verifiable**: $\epsilon_N$ is computed by diagonalizing a finite matrix whose entries involve only the primes $p \leq \lambda^2$, the poles of $\zeta$, and the archimedean phase — never the zeros. Crucially, the positivity of $QW^N_\lambda$ itself **is neither assumed nor needed nor true in general** (negative eigenvalues observed, §2.5). The method works identically if $\epsilon_N < 0$.

**(P-out) — output positivity.** $\mu_\lambda \geq 0\ \forall\lambda$, equivalently $\lim\mu_\lambda \geq 0$. This **is** RH-equivalent (§2.2): it is the semilocal Weil positivity, MW-1.

CF rigidity consumes **only (P-in)** and produces an unconditional conclusion: the zeros of the **approximant** $\widehat{\xi}_\lambda^N$ are real. It does not touch (P-out). Comparison with KS:

| | Kurasov–Sarnak (Candidate A) | CF rigidity in CCM-ZST |
|---|---|---|
| Object to which rigidity applies | the limiting arithmetic object (the zero measure of $\zeta$) | the finite truncation $T = QW^N_\lambda - \epsilon_N$ |
| Rigidity hypothesis | quasicrystal $\equiv$ Lee–Yang $\equiv$ Hermite positivity | $T \geq 0$ **by spectral shift** + even-simplicity |
| Is the hypothesis RH-equivalent? | **Yes** (disguised CAP) | **No** (tautological + non-degeneracy) |
| Conclusion obtained | (if applicable) reality of the zeros of $\zeta$ | reality of the zeros of the **approximant** |
| Where does RH end up? | inside the hypothesis (circular) | shifted **entirely to the limit** $\lambda \to \infty$ |

**Discriminator conclusion, mechanism level:** CF rigidity is **NOT disguised RH-equivalent positivity**. Filter I2a lets it through: its input positivity is verifiable and unconditional (indeed trivial), and its conclusion at the finite level is an unconditional theorem. It is structurally distinct from the KS collapse, and the difference is precise: **CF weakens the conclusion** (reality of the zeros of the approximant, not of $\Xi$) **in exchange for eliminating the circularity of the hypothesis**.

### 4.3. But the circularity does not disappear: it is displaced and renamed

The price of that exchange is exact. For the real zeros of the approximant to say anything about $\Xi$, one needs the convergence $\det_{\mathrm{reg}}(H_x - z) \to \Xi(z)$ (after normalization), and then Hurwitz gives RH. But (§5) the quantitative content of that convergence includes the behavior $\mu_\lambda \to 0$, which **is** (P-out) **is** MW-1 **is** MW-6. In the program's language:

> The CF construction realizes the transmutation *"hypothesis circularity" $\longrightarrow$ "non-uniformity of the limit"*. The wall is not crossed: it is relocated to the passage to the limit, where it reappears under its usual name (uniform spectral gap of truncations, MW-6, equivalent to Weil positivity, MW-1).

**Two-level verdict of the filter:**
- **Finite mechanism (CF rigidity as such): PASSES I2a.** It is not CAP. It is the first post-survivors structure that unconditionally produces families of entire functions with real zeros *anchored to the verifiable arithmetic data of $\zeta$* (primes + poles + phase $\theta$).
- **Full strategy (CF + limit): FAILS I2a at the final step.** The statement "the spectra converge to the zeros" implies RH, and its quantitative core ($\lim\mu_\lambda \ge 0$, determinant normalizations) is Weil positivity.

### 4.4. On the meaning of the $10^{-55}$ and the Hadamard barrier

Two candid observations:

1. The precision $10^{-55}$ with 6 primes **is not evidence of non-circularity**; it is evidence that the arithmetic cancellation controlling $\mu_\lambda$ (and the closeness $\xi_\lambda \approx$ prolate function) is already extraordinarily deep at $x = 13$. CCM estimate the probability of coincidental match at $\sim 10^{-1235}$: there is real structure. But the *magnitude* of that cancellation is exactly what no one knows how to bound — see §6.1 (vanishing-gap obstruction).

2. Does Corollary 3.8 violate the Hadamard barrier (MW-7: "no property of $\zeta$ verifiable without knowing zero positions implies $d\nu = 0$")? No, and the reason refines the statement of MW-7: each individual $\mu_\lambda$ is verifiable (computable without zeros), but the RH-sufficient statement is the **infinite conjunction** $\lim\mu_\lambda = 0$, which is not verifiable in finite terms. It is the same logical form as Li's criterion ($\lambda_n \geq 0\ \forall n$, each $\lambda_n$ computable): a sequence of verifiable instances whose totality is CAP. MW-7 should be read thus: *verifiable = decidable with finite information*; the CF family does not escape that reading.

---

## 5. (iii) The $H_x \to H_\infty$ convergence obstruction: precise formulation

### 5.1. The right topology is not that of resolvents

The operators $D^{(\lambda,N)}_{\log}$ live in **different** Hilbert spaces for each $(\lambda,N)$: the inner product on $E_N'$ is the form $QW^N_\lambda - \epsilon_N$, which changes with the parameters and whose "size" collapses with the spectral gaps (§6.1). There is no natural fixed ambient space in which to pose resolvent-norm convergence; a forced embedding into $L^2(\mathbb{R}^*_+)$ degenerates because the metric $T$ has eigenvalues that tend to $0$ super-exponentially [literature numerical evidence; NOT VERIFIED as an asymptotic statement]. The object stable under change of metric is the **regularized determinant**: $\det_{\mathrm{reg}}(D^{(\lambda,N)}_{\log} - z) = -i\lambda^{-iz}\widehat{\xi}(z)$ depends only on the spectrum, and the spectrum depends only on $(\xi, \delta_N, D_{\log}^{(\lambda)})$, not on the chosen inner product. The correct formulation is therefore **uniform convergence on compacta of entire functions** (compact-open topology; Montel + Hurwitz as the machinery for passing to the limit of zeros). This is exactly the choice of CCM-ZST §7. From it one deduces local spectral convergence (convergence of zero sets in local Hausdorff metric over compacta), which is the surviving operator-theoretic notion.

### 5.2. The two limits, as mathematical statements

**(C1) Inner limit, $N \to \infty$ with $\lambda$ fixed.**
*Statement:* Suppose $A_\lambda$ is even-simple (minimal eigenvalue $\mu_\lambda$ simple, even eigenfunction $\xi_\lambda$). Then $\epsilon_N \to \mu_\lambda$, $\xi_N \to \xi_\lambda$ in $L^2([\lambda^{-1},\lambda], d^*u)$ with the normalization $\delta_N(\xi_N)=1 \to \xi_\lambda(\lambda) = 1$, and
$$\det\nolimits_{\mathrm{reg}}\bigl(D^{(\lambda,N)}_{\log} - z\bigr) \longrightarrow -i\,\lambda^{-iz}\,\widehat{\xi_\lambda}(z)$$
uniformly on compacta of $\mathbb{C}$.
*Status:* the convergence $\epsilon_N \to \mu_\lambda$ is Prop. 3.4 of CCM-ZST (proved: $E$ is a core of the form). The convergence of the eigenvector and the determinant is plausible given the compactness of Thm. 3.6, **modulo even-simplicity of $A_\lambda$** — OPEN GAP E1 (§7), plus a limit-exchange in the regularized determinant — declared technical gap, presumably tractable.

**(C2) Outer limit, $\lambda \to \infty$ — the statement that would imply RH.**
*Statement:* There exist constants $a_\lambda, b_\lambda \in \mathbb{R}$ such that
$$e^{a_\lambda + b_\lambda z}\cdot\bigl(-i\,\lambda^{-iz}\,\widehat{\xi_\lambda}(z)\bigr) \longrightarrow \Xi(z) := \xi_{\mathrm{Riemann}}\bigl(\tfrac12 + iz\bigr)$$
uniformly on compacta of the strip $|\Im(z)| < \tfrac12$.
**Proposition 5.3 (C2 $\Rightarrow$ RH; the Hurwitz argument, written in detail).** Assume C1 (for a sequence $N_k \to \infty$ at each $\lambda$, modulo E1) and C2. Then all zeros of $\Xi$ in the strip $|\Im(z)| < \tfrac12$ are real, i.e., RH.

*Proof.* Let $G_\lambda(z) := e^{a_\lambda + b_\lambda z}\bigl(-i\lambda^{-iz}\widehat{\xi_\lambda}(z)\bigr)$. Step 1: the zeros of $G_\lambda$ are those of $\widehat{\xi_\lambda}$ (the exponential factor never vanishes). Step 2: the zeros of $\widehat{\xi_\lambda}$ are real. Indeed, by C1, $\widehat{\xi_{N}} \to \widehat{\xi_\lambda}$ uniformly on compacta, the zeros of each $\widehat{\xi_N}$ are real (Thm. 5.10(iii), unconditional given even-simplicity of the truncation), and $\widehat{\xi_\lambda} \not\equiv 0$; by Hurwitz, every zero of $\widehat{\xi_\lambda}$ is a limit of zeros of the $\widehat{\xi_N}$, and $\mathbb{R}$ is closed in $\mathbb{C}$. (Alternatively, the continuous version of the CvS theorem applied to $A_\lambda$ gives Step 2 directly, again modulo E1.) Step 3: let $\rho = \tfrac12 + i z_0$ be a nontrivial zero of $\zeta$, so that $\Xi(z_0) = 0$ with $|\Im(z_0)| < \tfrac12$. Take a closed disk $\overline{D}(z_0, r)$ inside the strip in which $\Xi$ has no other zeros and does not vanish on the boundary. By C2, $G_\lambda \to \Xi$ uniformly on $\overline{D}(z_0,r)$ and $\Xi \not\equiv 0$; by Hurwitz, for $\lambda$ large $G_\lambda$ has zeros in $D(z_0,r)$, all real by Steps 1–2, and these zeros converge to $z_0$ (shrinking $r$). A limit of real numbers is real: $z_0 \in \mathbb{R}$, i.e., $\Re(\rho) = \tfrac12$. $\square$

Note what enters each step: Step 2 is CF rigidity (unconditional modulo E1); **all the arithmetic weight is in Step 3, i.e., in C2.**

*Converse:* RH $\Rightarrow$ C2 **is not proved** (it is not even stated as a theorem in CCM-ZST; it is the "plausible" direction). C2 is a priori stronger than or equal to RH; in particular C2 requires not only the sign of $\lim\mu_\lambda$ but the convergence of the normalized minimal eigenvector, which is strictly finer information. OPEN GAP.

### 5.3. Is this MW-2 in disguise? Answer: the wall is MW-6/MW-1, and MW-2 reappears as quantitative divergence of the prime tail

First, what it is **not**: the finite Euler product of CCM-ZST is not the truncation of $\zeta$ in $\mathrm{Re}(s) > 1$ extrapolated to the strip. Prime information reaches the critical line through the **only channel MW-2 allows**: the explicit formula, where the compact support on the multiplicative side ($[\lambda^{-1},\lambda]$) cuts off exactly the primes $p \leq \lambda^2$ with no divergence at all. In this precise sense, the construction is a spectral realization of the lesson of MW-2, not a violation or disguise of it.

But MW-2 reappears in the *quantitative* control of the finite $\to$ full limit. We prove:

**Lemma 5.1 (divergence of the prime part).** Let $\tau^{(P)}_{00}(\lambda) := \sum_{p}W_p(V_0, V_0)$ be the prime contribution to the diagonal $(0,0)$ entry of $QW_\lambda$ (which, by support, involves only $p^m \leq \lambda^2$). Then, with $L = 2\log\lambda$,
$$\tau^{(P)}_{00}(\lambda) = 2\sum_{p^m \leq \lambda^2} (\log p)\, p^{-m/2}\Bigl(1 - \frac{m\log p}{L}\Bigr) \;\geq\; \sum_{p \leq \lambda} \frac{\log p}{\sqrt{p}} \;\geq\; c\,\sqrt{\lambda}$$
for an absolute constant $c > 0$ and all sufficiently large $\lambda$. In particular $\tau^{(P)}_{00}(\lambda) \to \infty$: **the family of forms $\{\sum_p W_p\}_\lambda$ does not converge, nor does it stay bounded, in any topology of forms over the growing spaces.**

*Proof.* The diagonal entry is the prime component of $\Psi$ applied to $F(u) = q(U_0,U_0)(\log u) = 2(1 - |\log u|/L)$ (tent function; CCM-ZST eq. (2.8) and context Lemma 4.1). By (3.16), $W_p^{\#}(F) = (\log p)\sum_m p^{-m/2} F(p^m)$, and $F(p^m) = 2(1 - m\log p/L)_+$. For $m = 1$ and $p \leq \lambda$ one has $1 - \log p/L \geq 1 - \tfrac{\log\lambda}{2\log\lambda} = \tfrac12$. Hence $\tau^{(P)}_{00} \geq \sum_{p\leq\lambda}(\log p)p^{-1/2}$. By Chebyshev ($\theta(t) \geq c_0 t$ for $t \geq 2$) and partial summation, $\sum_{p\leq\lambda}(\log p)p^{-1/2} \geq \theta(\lambda)\lambda^{-1/2} \geq c_0\sqrt{\lambda}$. $\square$

**Proposition 5.2 (PNT-level cancellation in the diagonal).** With CCM-ZST's normalization:
(a) the pole contribution is $W_{0,2}(V_0,V_0) = \dfrac{32\sinh^2(L/4)}{L} = \dfrac{4\lambda}{\log\lambda}\,\bigl(1 + O(\lambda^{-1})\bigr)$;
(b) the archimedean contribution is $W_{\mathbb{R}}(V_0,V_0) = O(1)$ uniformly in $\lambda$;
(c) the prime contribution satisfies, by the Prime Number Theorem,
$$\tau^{(P)}_{00}(\lambda) = \frac{4\lambda}{\log\lambda}\,\bigl(1 + o(1)\bigr).$$
Consequently, $\tau_{00}(\lambda) = W_{0,2} - W_{\mathbb{R}} - \tau^{(P)}_{00} = o(\lambda/\log\lambda)$: **each of the two dominant terms diverges as $4\lambda/\log\lambda$, and the diagonal entry of $QW_\lambda$ survives only through their mutual cancellation, which is exactly the PNT.**

*Proof.* (a) By Lemma 4.1 of CCM-ZST with $m = n = 0$: $W_{0,2}(V_0,V_0) = 32L\sinh^2(L/4)\cdot L^2/L^4 = 32\sinh^2(L/4)/L$; and since $L = 2\log\lambda$ gives $e^{L/2} = \lambda$, one has $\sinh^2(L/4) = \tfrac14(e^{L/2} - 2 + e^{-L/2}) = \tfrac{\lambda}{4}(1 + O(\lambda^{-1}))$. Hence $32\cdot\tfrac{\lambda}{4}/(2\log\lambda) = 4\lambda/\log\lambda \cdot (1 + O(\lambda^{-1}))$. (b) By (3.15), $W_{\mathbb{R}}^{\#}(F) = (\log 4\pi + \gamma)F(1) + \tfrac12\int_1^\infty \tfrac{x^{1/2}(F(x) - F(1))}{x - x^{-1}}\,d^*x$ with $F$ the tent function: $F(1) = 2$ and $F(x) - F(1) = -2\log x/L$ on the support; with $x = e^u$ the integrand is $-\tfrac{2u}{L}\cdot\tfrac{e^{u/2}}{2\sinh u}$, which is $O(1)$ for $u \in (0,1]$ and $O\bigl(\tfrac{u}{L}e^{-u/2}\bigr)$ for $u \geq 1$; the total integral is $O(1/L)\cdot O(1) + O(1) = O(1)$. (c) The $m \geq 2$ terms contribute $O(\sum_{p \leq \lambda}\log p/p) = O(\log\lambda)$ (Mertens). For $m = 1$, by partial summation against $\theta(t)$ and the PNT ($\theta(t) = t(1 + o(1))$):
$$2\sum_{p \leq \lambda^2}\frac{\log p}{\sqrt p}\Bigl(1 - \frac{\log p}{L}\Bigr) = 2\int_{2^-}^{\lambda^2}\Bigl(1 - \frac{\log t}{L}\Bigr)t^{-1/2}\,d\theta(t) = 2\int_0^{L}\Bigl(1 - \frac{u}{L}\Bigr)e^{u/2}\,du\;(1 + o(1)),$$
and $\int_0^L(1 - u/L)e^{u/2}du = \tfrac{4e^{L/2}}{L} + O(1) = \tfrac{4\lambda}{2\log\lambda} + O(1)$, giving $2 \cdot \tfrac{2\lambda}{\log\lambda}(1+o(1)) = \tfrac{4\lambda}{\log\lambda}(1+o(1))$. $\square$

*Comment (the hierarchy of cancellations).* Proposition 5.2 quantifies where each level of arithmetic information lives in the family $QW_\lambda$:
- that $\tau_{00} = o(\lambda/\log\lambda)$ is the **PNT**;
- that $\tau_{00}$ (and the other entries) end up of size $O(\lambda^{1/2 + \epsilon})$ is the size of the error term $\psi(x) - x$, i.e., **equivalent to RH at the level of entries** (we do not use it; we flag it);
- that the **bottom of the spectrum** $\mu_\lambda$ of the full form stays $\geq -o(1)$ is semilocal Weil positivity, i.e., **RH at the spectral level** — a deeper floor than the entries, because it involves the coherent cancellation of the whole matrix.

**Answer to (iii).** The obstruction to the convergence $H_x \to H_\infty$ is **not** a compactness problem (compactness is there: Thm. 3.6 gives discrete spectrum for each $\lambda$, and C1 is a controllable inner limit). It is a problem of **stability of the bottom of the spectrum under the limit of the truncations**, i.e., MW-6 in literal form, rooted in MW-1; and Lemma 5.1 shows that MW-2 reappears as the quantitative fact that the prime tail diverges as $\sqrt{x}$ (indeed as $4\lambda/\log\lambda$ with the tent function), so that **no perturbative "finite product $\to$ full" argument can work**: the convergence, if it occurs, occurs only through cancellation among the three divergent blocks, and controlling that cancellation at the level of the spectral infimum is CAP.

---

## 6. (iv) Do the program's own tools control this convergence?

### 6.1. Stability of CF rigidity under bounded perturbation (new result, with proof) and the vanishing-gap obstruction

**Lemma 6.1 (CF stability).** Let $Q$ be real symmetric of size $2N+1$, with the structure of §2.3, commuting with $\gamma$, even-simple, with minimal eigenvalue $\epsilon_1$ and spectral gap $g := \epsilon_2 - \epsilon_1 > 0$. Let $E$ be real symmetric with the same structure, commuting with $\gamma$, with $\|E\| < g/2$. Then:
(i) $\widetilde{Q} = Q + E$ is even-simple;
(ii) its normalized minimal eigenvectors satisfy $\|\widetilde{\xi} - \xi\| \leq \dfrac{2\|E\|}{g - 2\|E\|}$;
(iii) $\widehat{\widetilde{\xi}}$ has all its zeros real, and on any compact $K \subset \mathbb{C}$ the zeros of $\widehat{\widetilde{\xi}}$ converge to those of $\widehat{\xi}$ as $\|E\| \to 0$.

*Proof.* (i) By Weyl, $|\epsilon_k(\widetilde Q) - \epsilon_k(Q)| \leq \|E\|$ for all $k$; since $\|E\| < g/2$, the minimal eigenvalue of $\widetilde Q$ remains separated from the rest by at least $g - 2\|E\| > 0$, hence is simple. Since $E$ commutes with $\gamma$, the even/odd sectors are invariant for $\widetilde Q$; the minimal eigenvector of $Q$ is even and the spectral separation prevents the minimal eigenvector of $\widetilde Q$ from crossing sectors (the interpolation path $Q + tE$ keeps the minimal eigenvalue simple for $t \in [0,1]$, and the parity of the eigenvector, locally constant along the path by simplicity, is preserved). (ii) Davis–Kahan $\sin\theta$ theorem applied to the pair $(Q, \widetilde Q)$ with effective separation $g - 2\|E\|$... [standard form: $\|\sin\theta\| \le \|E\|/(g - \|E\|)$; we use the looser bound stated]. (iii) $\widetilde Q - \epsilon_1(\widetilde Q)\,\mathrm{id} \geq 0$ is singular, even-simple, with the structure preserved (the shift only moves the diagonal): the CvS theorem applies verbatim and gives real zeros. Convergence of zeros on compacta follows from $\widehat{\widetilde\xi} \to \widehat\xi$ uniformly on compacta (the transform is linear and continuous in the coefficients, finite dimension) plus Hurwitz. $\square$

**Positive consequence.** CF rigidity is **robust**: it survives any structured bounded perturbation — in particular Hilbert–Schmidt-type perturbations, which are bounded. The first half of the intermediate statement suggested in the task ("stability of CF rigidity under HS perturbation") **is thereby proved** (Lemma 6.1). The reality of the approximant's zeros is not a fragile phenomenon.

**Vanishing-gap obstruction (the negative side, new and precise).** The constants of Lemma 6.1 are $O(\|E\|/g)$. But in the CCM-ZST family, the relevant gaps at the bottom of the spectrum of $QW_\lambda^N$ are — per CCM-ZST's own discussion in §8 about the "extremely small numbers $\epsilon_\lambda$" and literature numerical evidence — super-exponentially small in $\lambda$ (scale $10^{-55}$ already at $x = 13$) [asymptotic magnitude: NOT VERIFIED as a theorem; it is a reported numerical fact]. Therefore:

> The **very smallness** that produces the spectacular precision of the spectra of $H_x$ (the minimal eigenvalues almost touch $0$, a sign of deep arithmetic cancellation) **destroys all quantitative perturbative control**: any argument "transfer even-simplicity / transfer the eigenvector from a nearby model" pays a factor $1/g$ that grows faster than any available bound on $\|E\|$. The $10^{-55}$ precision and the perturbative fragility are two faces of the same coin.

This explains exactly why the "main remaining obstacle" of CCM-ZST (justifying $\xi_\lambda \approx k_\lambda$ with $k_\lambda$ the prolate approximation) is not a technical detail: the admissible error must compete with vanishing gaps.

### 6.2. The exact Wronskian and the closed formula for $F_n$ (Doc 68/69): a candid diagnosis

The exact Wronskian $W_k = -1/a_k^\infty$ and the formula $F_n = -1/(a_n^\infty P_n P_{n+1} m_\infty)$ live in the **Jacobi representation** of the measures $dm_\infty$ and $dm_{\mathrm{full}} = |\zeta(\tfrac12+is)|^2\,dm_\infty$: they are identities of the **limiting** object $\lambda = \infty$, with the Euler product **already summed** inside $|\zeta|^2$. The $H_x$ family interpolates precisely **in $x$**, before that limit. The two families of truncations are distinct filtrations of the same object:

- **Arithmetic filtration (CCM-ZST):** by primes $p \leq x = \lambda^2$, induced by the multiplicative support $[\lambda^{-1},\lambda]$; the cutoff parameter lives on the **prime** side.
- **Spectral filtration (program, P39/P40):** by polynomial degree $n$ (sections $J_n$ of the Jacobi matrix); the cutoff parameter lives on the **zeros/spectrum** side.

**OPEN GAP 6.2 (filtration dictionary).** There is today no dictionary relating the truncations $QW^N_\lambda$ to the Jacobi sections $J_n$ with uniform control. The natural candidate is the pair of reproducing kernels: the **Christoffel–Darboux** kernel $\sum_{k<n}P_k(z)P_k(w)$ (Jacobi side, Doc 69 §2.3) versus the **Dirichlet** kernel $\delta_N$ (CCM-ZST side, §2.4). Both implement "approximate evaluation" in their respective geometries. Formulating and proving an asymptotic equivalence between the two kernels is a well-posed, non-circular question, but **it has not been done**; without it, the exact Wronskian does not transport to the $H_x$ family.

What the Wronskian **does** contribute, indirectly: the formula $G_{nn} = m_\infty + m_\infty^{-1}\sum_{k<n}(a_k^\infty P_k P_{k+1})^{-1}$ (Doc 69 §4.1) gives the exact diagonal resolvents on the archimedean side $J^\infty$, which is the Jacobi analogue of the scaling operator $D^{(\lambda)}_{\log}$ (both are the "background without arithmetic"). If the dictionary of GAP 6.2 existed, these exact formulas would give the free comparison term for a perturbative theory of $H_x$. Today it is potential, not control.

### 6.2-bis. Clarification to prevent a mistaken identification: $dm_\infty$ is not the archimedean symbol of $QW_\lambda$

It is tempting to identify the "archimedean background" of both frameworks, since both involve the phase $\Gamma(\tfrac14 + \tfrac{is}{2})$. But they are distinct objects and the difference matters:

- In the CCM-ZST family, the archimedean part of $A_\lambda$ is, in Fourier, the **multiplier** $\tfrac{1}{\pi}\partial_t\theta(t) \sim \tfrac{1}{2\pi}\log|t|$ — a function of **logarithmic growth** (this is what gives the compact resolvent, Thm. 3.6).
- In the P39/P40 framework, $dm_\infty(s) = (2\pi)^{-2}\bigl|\Gamma(\tfrac14 + \tfrac{is}{2})\bigr|^2\,ds$ is the **spectral measure** of the Jacobi operator $J^\infty$, with **exponentially decaying** weight $\sim e^{-\pi|s|/2}$ (Stirling) — this is what makes the sum rule of Doc 92 finite.

Both come from the same datum (the $\Gamma_{\mathbb{R}}$ factor of the functional equation), but one is the *phase derivative* ($\theta' = \Im\,\partial_s\log\Gamma$, real, increasing) and the other is the *squared modulus* ($|\Gamma|^2$, decreasing). Any attempt to "translate" results between the two frameworks that identifies them produces errors of exponential order. The correct dictionary, if it exists, must go through GAP 6.2 (reproducing kernels), not through symbol identification. We record this because it is the most likely error in future attempts to merge the two frameworks.

### 6.3. Sum rule and HS perturbation (Doc 92, P40): a transportable lemma and where the chain breaks

**Lemma 6.4 (finite sum rule — provable).** For $x \geq 2$ let $\zeta_x(s) := \prod_{p\leq x}(1 - p^{-s})^{-1}$ be the finite product and $dm_x := |\zeta_x(\tfrac12+is)|^2\,dm_\infty$. Then $\log|\zeta_x(\tfrac12+is)|^2$ is continuous and of polynomial growth in $s$ (it is a finite sum of smooth bounded functions), hence integrable against $dm_\infty$ (weight with exponential decay $|\Gamma(\tfrac14+\tfrac{is}2)|^2$), and the Jacobi coefficients $a_k(x) = a_k^\infty + e_k(x)$ of $dm_x$ satisfy the sum rule
$$\sum_k e_k(x)^2 \;=\; \int \log|\zeta_x(\tfrac12+is)|^2\,dm_\infty \;<\; \infty,$$
with $b_k(x) = 0$ by the symmetry $s \mapsto -s$ of $|\zeta_x(\tfrac12+is)|^2$ (which follows from $\overline{\zeta_x(\tfrac12+is)} = \zeta_x(\tfrac12-is)$ for real $s$).
*Proof.* Identical to that of Doc 92 (Szegő–Killip–Simon-type sum rule for perturbation of the weight by a log-integrable, symmetric factor); no property of the full $\zeta$ is used, only log-integrability of the factor, which here is elementary. $\square$

This gives a **well-defined convergence metric** for the family of finite measures: $d(x)^2 := \sum_k\bigl(e_k(x) - e_k\bigr)^2$, with $e_k$ the full coefficients (P40). And here the chain breaks at the first link, exactly where MW-2 says it must break:

**OPEN GAP 6.5 (no pointwise convergence of the finite product on the line).** For fixed real $s$, $\zeta_x(\tfrac12+is) \not\to$ a limit as $x \to \infty$: the Euler product **does not converge on** $\mathrm{Re}(s) = \tfrac12$ — not even under RH (under RH there is conditional convergence of the product on $\mathrm{Re}(s) > \tfrac12$, not on the line). Hence $dm_x \not\to dm_{\mathrm{full}}$ in any pointwise sense of the integrand, and if there is weak convergence of $dm_x$ (after averaging) to $dm_{\mathrm{full}}$, proving it would be a strong Tauberian theorem whose status we do not know — we declare it an OPEN GAP, noting that it is the natural candidate for an intermediate statement on the Jacobi side (E6, §7).

**The structural lesson (important).** Compare GAP 6.5 with the automatic locality of §2.1: the **only** known way to make "finite product $\to$ full" converge with data on the critical line is to pass to the dual side of the explicit formula and cut by **compact support** (Weil/CCM-ZST), not by pointwise product (Jacobi/Doc 92). The numerical success of CCM-ZST is the spectral manifestation of this asymmetry. The program's Jacobi tools are on the wrong side of the cut: they see the limit, not the family.

**Summary of (iv):** the program's own tools give (a) Lemma 6.1 — qualitative stability of CF rigidity, new and proved here; (b) Lemma 6.4 — finite sum rule, proved by direct transport from Doc 92; (c) **no control of the limit $\lambda \to \infty$**, because that control is (P-out) = MW-1, and moreover GAPs 6.2 and 6.5 block the two natural bridges between the program's Jacobi framework and the $H_x$ family.

---

## 7. (v) Non-circular intermediate statements: what would be provable

We classify by status with respect to the circularity filter.

**E1 (even-simplicity of $A_\lambda$, for every $\lambda > 1$).** CCM-ZST's missing step 1. It is a statement of **spectral non-degeneracy**, not of positivity: on its face it is not RH-equivalent (a degeneracy of the minimal eigenvalue, or an odd minimal eigenvector, does not evidently produce or destroy off-line zeros). Favorable sign (CCM-ZST §8): the property holds for the prolate operator $PW_\lambda$ for every $\lambda$. Non-perturbative line of attack: oscillation/Sturm theory on the even sector of the eigenvalue problem for $A_\lambda$ (the perturbative route from $PW_\lambda$ is quantitatively blocked by the vanishing gap, §6.1). **Cleanest candidate on this front. Non-circular. OPEN GAP.**

**E2 (inner limit C1, modulo E1).** Convergence $\epsilon_N \to \mu_\lambda$, $\xi_N \to \xi_\lambda$, and of the regularized determinants, at fixed $\lambda$. Available ingredients: Prop. 3.4 (core of the form), Thm. 3.6 (compact resolvent), Lemma 5.5 (Dirichlet kernel on $\mathrm{Dom}\,D$). The non-trivial part: the convergence of $\widehat{\xi_N} \to \widehat{\xi_\lambda}$ uniform on compacta with the boundary normalization (the functional $\delta_N$ is not continuous in $L^2$; one must pass through the norm of the form). **Plausibly provable; non-circular; declared technical gap.**

**E3 (stability of CF under structured perturbation).** **Proved** (Lemma 6.1). Closed, positively.

**E4 (rate of spectral convergence as a function of the Euler product tail).** **CIRCULAR — ruled out precisely.** Any bound of the form $\mathrm{dist}\bigl(\mathrm{spec}(H_x)\cap K,\ \{\gamma_n\}\cap K\bigr) \leq \omega(x)$ with $\omega(x) \to 0$ uniform on compacta would imply (via the quantitative Hurwitz argument) an effective version of C2, hence effective RH. And Lemma 5.1 shows that the "tail of the Euler product on $\mathrm{Re}(s) = \tfrac12$" is not small: it diverges as $\sqrt{x}$ in form norm. Any rate must arise from cancellation among divergent blocks = Weil positivity = MW-1. As anticipated by the task: the Euler tail on the line **is** MW-2.

**E5 (finiteness and structure of the negative package of $QW^N_\lambda$).** Question: is the number $\kappa_\lambda(N)$ of negative eigenvalues of $QW^N_\lambda$ uniformly bounded in $N$ (i.e., $\kappa_\lambda := \sup_N \kappa_\lambda(N) < \infty$ for each $\lambda$), and how does $\kappa_\lambda$ grow with $\lambda$? Direct connection to the program: it is the semilocal analogue of the negative index $\kappa(Q) = \mathrm{neg.ind}(H_C)$ (P35) and of Theorem 8.1 of Doc 96 (negative index localized in $\mathcal{K}_{\mathrm{off}}$); literature numerical evidence ($\kappa$ growing with $N$ at fixed $x$: 3, 5, 8, 11 — [Groskin, NOT VERIFIED]) suggests the truncated version does **not** stabilize trivially, which would make $\kappa_\lambda(N)$ an object with content. Under RH, $\mu_\lambda \geq 0$ forces $\kappa_\lambda(N) = 0$ asymptotically in the limit of the form — so take care: an unconditional, growing lower bound on $\kappa_\lambda(N)$ that survives $N \to \infty$ would **refute** RH, and an upper bound $\to 0$ would prove it; the "fine structure" version (parity, localization of the negative eigenvectors), by contrast, is studiable without touching that edge. **Partially non-circular; well posed; not started.**

**E6 (Tauberian for measures: $dm_x \to dm_{\mathrm{full}}$ in averaged weak sense).** GAP 6.5 as a positive question. If true with logarithmic averaging in $x$, it would give the bridge between the arithmetic and spectral filtrations (GAP 6.2) at the level of measures, without passing through zeros. Status with respect to the filter: unknown — it could collapse to a statement of the type "moments of $|\zeta_x|^2$ against a smooth weight", which is classical mean-value theory of Dirichlet polynomials; if it collapses there, it is provable but probably insufficient for C2 (mean values do not see the bottom of the spectrum). **Open, exploratory.**

---

## 8. Synthesis

1. **(i)** CF rigidity is boundary uniqueness in the Carathéodory–Toeplitz positive extension problem (and in the CF/Pick–Nevanlinna extremal problem): form $\geq 0$ singular $\Rightarrow$ kernel vector's zeros on the boundary. CvS generalize it to matrices with $[D,\tau]$ of rank $\leq 2$ (Loewner structure), circle $\to$ line. In CCM-ZST it is applied to the **shifted** truncation $QW^N_\lambda - \epsilon_N \geq 0$ (tautological positivity) and unconditionally produces self-adjoint operators $H_x$ with $\det_{\mathrm{reg}}(H_x - z) = -i\lambda^{-iz}\widehat{\xi}(z)$ having real zeros.

2. **(ii)** **CF rigidity does NOT collapse to RH-equivalent positivity.** Unlike Kurasov–Sarnak (where the structural hypothesis was disguised CAP), here the positivity consumed is a spectral shift with no arithmetic content, verifiable, and the finite-level conclusion is a theorem. The mechanism passes filter I2a. **But** the circularity is not eliminated: it is transmuted into non-uniformity of the limit. The only step that would give RH (C2) implies RH via Hurwitz, and its quantitative core ($\lim\mu_\lambda \geq 0$, Cor. 3.8 and the converse of Weil) **is** MW-1 in the form MW-6.

3. **(iii)** The obstruction to $H_x \to H_\infty$ is neither compactness nor naive MW-2-style non-convergence of the Euler product (support-based locality avoids that exactly): it is the **stability of the bottom of the spectrum of the truncations**, with MW-2 reappearing quantitatively as $\sim 4\lambda/\log\lambda$ divergence of the prime tail (Lemma 5.1, Prop. 5.2), which forces any convergence to come from PNT→RH cancellation among divergent blocks. Correct topology: compact-open topology of regularized determinants (entire functions), not resolvents.

4. **(iv)** Own tools: Lemma 6.1 (CF stability, new) and Lemma 6.4 (finite sum rule, transported from Doc 92) are provable and proved/sketched here; the exact Wronskian does not transport without the filtration dictionary (GAP 6.2); the finite-to-full Jacobi chain breaks at the non-convergence of the product on the line (GAP 6.5). New obstruction, named: **vanishing gap** — the $10^{-55}$ precision and the uselessness of any quantitative perturbation are the same phenomenon.

5. **(v)** Provable and non-circular: E1 (even-simplicity of $A_\lambda$ — the central candidate), E2 (inner limit C1), E3 (fact), E5/E6 (exploratory). Precisely circular: E4 (any uniform finite-to-full rate is effective RH).

---

## VERDICT: **PARTIAL**

**Precise reason.** Carathéodory–Fejér rigidity is the first mechanism examined by the program since the survivors meta-doc that **passes the circularity filter at the mechanism level**: it is not disguised RH-equivalent positivity (the Kurasov–Sarnak → Lee–Yang → CAP collapse **does not** reproduce), because its positivity input is a tautological, verifiable spectral shift, and its output — real spectra of the approximants $H_x$ anchored to computable arithmetic data — is an unconditional theorem. In that sense the route is **alive** and genuinely new.

However, the route **is not a path to RH with existing tools**: the only link between the real spectra of $H_x$ and the zeros of $\zeta$ is the convergence C2, whose quantitative content ($\lim_{\lambda\to\infty}\mu_\lambda \geq 0$) is exactly semilocal Weil positivity — MW-1 under the MW-6 disguise —, with MW-2 reappearing as the $\sim \lambda/\log\lambda$ divergence of the prime tail that forbids any perturbative treatment of the finite-to-full limit (Lemma 5.1, Prop. 5.2). The program's own tools control the **stability** of the mechanism (Lemma 6.1) but not its **limit**, and the two bridges to the program's Jacobi framework are blocked by precise gaps (6.2, 6.5).

What remains alive, concretely, is the non-circular sub-route: **E1 (even-simplicity of $QW_\lambda$) + E2 (inner limit)**, which would close the entire diagram of §3.3 except for the last step, plus the exploratory objects E5/E6. The last step is, once again, the program's single wall under another name.

---

## Appendix A — Source verification (candor protocol)

| Source | What was verified | How |
|---|---|---|
| arXiv:2511.22755 (CCM, *Zeta Spectral Triples*, 27-Nov-2025, 34 pp.) | Full text: abstract, §§1–8, Thm. 1.1/5.10, Prop. 3.3–3.4, Thm. 3.6, Cor. 3.7–3.8, eq. (3.27), Lemmas 5.1–5.5, Prop. 5.7, §7 (strategy, prolate, Lemmas 7.1–7.2), §8 (missing steps), bibliography | PDF downloaded and extracted; all citations in this doc checked against the text |
| arXiv:2511.23257 = Commun. Math. Phys. **406**:312 (2025) (Connes–van Suijlekom) | Abstract; statements of the three theorems (Toeplitz/corank, structured matrices, continuous version); 5-step proof structure | Abstract and statement summary via web; **the internal proof was not inspected line by line** — but CCM-ZST's use of the results was verified in the CCM-ZST text |
| arXiv:2602.04022 (Connes, *The RH: Past, Present and a Letter Through Time*, 3-Feb-2026, 42 pp.) | Abstract and structure: quadratic-form extremization with primes $< 13$, 50 zeros, precisions $2.6\times10^{-55}$ to $10^{-3}$, "approximating values lie exactly on the critical line", "convergence of zeros from finite to infinite Euler products" strategy | Abstract page via web; full text not extracted |
| arXiv:2605.20224 (Groskin, 13-May-2026) | Abstract only: independent numerical implementation, convergence down to $\sim 10^{-168}$ with $c = 67$, negative eigenvalues in truncations (3–11 depending on $N$) | Abstract via web; **[NOT VERIFIED]** beyond the abstract; used only as literature evidence, never as a proof premise |
| Carathéodory–Fejér 1911, Weil 1952, Schmüdgen GTM 265, Connes–Consani Enseign. Math. 69 (2023) | Existence and role as references [2], [16], [12], [4] of CCM-ZST | Checked in the PDF bibliography; content cited only through CCM-ZST's use of them |
| Kurasov–Sarnak arXiv:2307.13498 | Statement "every $\mathbb{N}$-valued 1-D FQ is the toral zero set of a Lee–Yang polynomial" | Already verified in meta-docs/NOVEL-STRUCTURE-SEARCH-survivors.md; not re-verified here |

Results **new to this document** (not present in the sources): Lemma 5.1, Proposition 5.2 (PNT cancellation in the diagonal of $QW_\lambda$), Proposition 5.3 (detailed writeup of the Hurwitz argument), Lemma 6.1 (CF stability), Lemma 6.4 (finite sum rule, transported from Doc 92), the formulation of GAPs 6.2/6.5, the "vanishing-gap obstruction" (§6.1), and the E1–E6 classification (§7). The proofs given are complete at the declared level of detail; unproved points are marked OPEN GAP or [NOT VERIFIED].

---

## Appendix B — Position of Doc 99 in the program's map

```
MW-1 (Weil positivity ⟺ RH)
  ║
  ╠═ MW-6 (uniform gap of truncations)  ⟵━━  C2 / lim μ_λ ≥ 0   [§5: this route's wall]
  ║                                                  ▲
  ║                                                  │ transmutation (§4.3)
  ║                                       CF rigidity at finite level
  ║                                       [PASSES filter I2a — §4.2]
  ║                                                  ▲
  ╠═ MW-2 (arithmetic propagation)  ⟵━━  Lemma 5.1: prime tail diverges ~ λ/log λ
  ║                                       (no finite→full perturbative route)
  ║
  ╚═ MW-7 (Hadamard barrier)  ⟵━━  §4.4: {μ_λ} computable, but RH = infinite
                                        conjunction (Li's logical form) — the barrier
                                        is refined, not broken

Routes alive after this doc:  E1 (even-simplicity of A_λ) ─ E2 (inner limit C1)
                            E5 (negative package κ_λ(N) ↔ Doc 96 Thm 8.1, P32)
                            E6 (Tauberian dm_x → dm_full, Jacobi side)
Precisely closed:      E4 (uniform finite→full rates ≡ effective RH)
Proved here:             E3 (CF stability, Lemma 6.1)
```

---

*End of Document 99.*
