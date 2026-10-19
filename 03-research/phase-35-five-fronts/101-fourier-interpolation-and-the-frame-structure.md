# Document 101 — Fourier interpolation and the frame structure of $\{e^{i\gamma_n s}\}$

**Program:** Riemann Hypothesis — Phase 35 (five fronts)
**Prerequisites:** Docs 70, 71, 72, 76, 82, 83, 85, 89; P39; meta-docs DISCRIMINATOR-hardening-phase-A, NOVEL-STRUCTURE-SEARCH-survivors

---

## Summary

This document audits the **Fourier interpolation** front (Radchenko–Viazovska, Bondarenko–Radchenko–Seip, Kulikov–Nazarov–Sodin), identified in NOVEL-STRUCTURE-SEARCH-survivors as the theory **dual** to quasicrystal rigidity (Kurasov–Sarnak) and not audited until now. Six questions are answered: (i) the exact structure of the system $\{e^{i\gamma_n s}\}$ in $L^2(W_\lambda\,dm_\infty)$ — it is proved, unconditionally, that the system is complete but **is not Bessel, is not a frame, is not a Riesz sequence, is not minimal, and is not an interpolation sequence**; (ii) the translation of each level of the hierarchy into statements about $d\nu$, including a **new condition equivalent to RH** (Condition 9: vanishing of $(W_\lambda d\nu)^\wedge$ at the $\gamma_n$ themselves); (iii) the analysis of the modular input of the RV/BRS machinery against walls MW-2 and MW-7 — the conclusion is that the modularity of $\theta$ **is** the functional equation of $\zeta$ in automorphic clothing and **does not** inject arithmetic information that evades MW-2; (iv) the Heisenberg-type uniqueness problem for $d\nu$, with explicit detection of circularity (the explicit formula applied to $d\nu$ reproduces the decomposition of Doc 72); (v) passage through the program's discriminator: **FAIL I2b**, Connes's exact profile; (vi) verdict: **ROUTE CLOSED** as a lever toward RH, with two unconditional byproducts incorporated into the program.

---

## §0. Notation and framework

We fix the program's notation (Docs 70, 83, 89):

- $dm_\infty(s) = (2\pi)^{-2}\,|\Gamma(1/4 + is/2)|^2\,ds$ on $\mathbb{R}$.
- $dm_{full} = |\zeta(1/2+is)|^2\,dm_\infty$; $dm_{full,on} = |\zeta_{on}(1/2+is)|^2\,dm_\infty$, where $\zeta_{on}$ has the zeros of $\zeta$ projected onto the critical line.
- $d\nu = dm_{full} - dm_{full,on} = (R-1)\,dm_{full,on} \geq 0$ unconditionally (Doc 83), with $R = \prod_{j:\delta_j>0}\big(1 + \delta_j^2/(s-\gamma_j)^2\big)^2 \geq 1$.
- $W_\lambda(s) = \sum_{k \leq N(\lambda)} k|P_k(s)|^2 + (a_{N(\lambda)}^\infty)^2|P_{N(\lambda)+1}(s)|^2 \geq 0$ the Abel kernel of the Jacobi basis $\{P_k\}$ of $L^2(dm_{full,on})$ (Doc 70).
- $T_\lambda = \int W_\lambda\,d\nu \geq 0$; **RH $\iff T_\lambda = 0\ \forall\lambda$** (P39; Doc 89, Theorem 10.1).
- $\mu_\lambda := W_\lambda\,dm_\infty$, a finite measure on $\mathbb{R}$ (Doc 85, §5.1, Step 1). We write $e_\gamma(s) := e^{i\gamma s}$ and $\widehat{\mu}(r) := \int e^{irs}\,d\mu(s)$.
- $\{\gamma_n\}_{n\geq 1}$: positive imaginary parts of the non-trivial zeros of $\zeta$, **always real** (Doc 85, Prop. 4.1), with $N(T) = \#\{n : \gamma_n \leq T\} = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T)$ unconditionally (Riemann–von Mangoldt).

**Starting result (Doc 85, Theorem 5.1, modulo item V.1).** The system $\{e_{\gamma_n}\}$ is complete in $L^2(\mu_\lambda)$, unconditionally, via Carlson–Beurling. The technical gap V.1 (verification of the hypotheses of the Carlson argument for entire functions of type $\leq \pi/4$ with logarithmically divergent real zero density) remains open and is **inherited** by every statement in this document that uses completeness.

---

## §1. Verified literature: exact statements and conditionality

All statements in this section were verified against the sources. Where verification is partial this is marked explicitly.

### 1.1. Radchenko–Viazovska (Publ. Math. IHÉS 129, 2019)

**Theorem RV (verified, as cited by BRS, Theorem A and eqs. (1.4)–(1.5)).** There exists a sequence of even Schwartz functions $a_n : \mathbb{R} \to \mathbb{R}$ such that for every even Schwartz $f$:
$$f(x) = \sum_{n=0}^\infty f(\sqrt{n})\,a_n(x) + \sum_{n=0}^\infty \widehat{f}(\sqrt{n})\,\widehat{a_n}(x),$$
with absolute convergence, and with interpolation properties $a_n(\sqrt{m}) = \delta_{nm}$, $\widehat{a_n}(\sqrt{m}) = 0$ for $m \geq 1$, plus the relations at $x=0$: $a_0(0)=\widehat{a_0}(0)=1/2$, $a_{n^2}(0) = -\widehat{a_{n^2}}(0) = -1$, $a_n(0) = -\widehat{a_n}(0) = 0$ in all other cases.

**Construction:** the $a_n$ are obtained from contour integrals of weakly holomorphic modular forms of weight $3/2$ for the theta group $\Gamma_\theta$. **Unconditional.** Verified remark (BRS, p. 4): evaluated at $x = 0$, the RV formula **reduces to the Poisson summation formula** — relations (1.5) are exactly the correction that makes the formula consistent with Poisson.

### 1.2. Bondarenko–Radchenko–Seip (Constr. Approx., 2023; arXiv:2005.02996, verified against the text)

Space: $\mathcal{H}_1$ = functions $f$ analytic in the strip $|\mathrm{Im}\,z| < 1/2 + \varepsilon$ with $\sup_{|y|<1/2+\varepsilon}\int |f(x+iy)|(1+|x|)\,dx < \infty$.

**Theorem BRS 1.1 (UNCONDITIONAL; verified).** There exist even entire functions of rapid decay $U_n(z)$ ($n \geq 1$) and $V_{\rho,j}(z)$ ($0 \leq j < m(\rho)$, $\rho$ ranging over the non-trivial zeros of $\zeta$ with positive imaginary part, $m(\rho)$ = multiplicity) such that for every even $f \in \mathcal{H}_1$ and every $z$ with $|\mathrm{Im}\,z| < 1/2$:
$$f(z) = \sum_{n=1}^\infty \widehat{f}\Big(\frac{\log n}{4\pi}\Big)\,U_n(z) + \lim_{k\to\infty}\sum_{0<\gamma\leq T_k}\sum_{j=0}^{m(\rho)-1} f^{(j)}\Big(\frac{\rho - 1/2}{i}\Big)\,V_{\rho,j}(z),$$
with dual interpolation properties (1.3): $\widehat{U_n}(\frac{\log n'}{4\pi}) = \delta_{nn'}$, $U_n^{(j)}(\frac{\rho-1/2}{i}) = 0$, $V_{\rho,j}^{(j')}(\frac{\rho'-1/2}{i}) = \delta_{(\rho,j),(\rho',j')}$, $\widehat{V_{\rho,j}}(\frac{\log n}{4\pi}) = 0$.

**Critical conditionality point (verified).** The theorem is **unconditional**: it assumes neither RH nor simplicity. The nodes are $\frac{\rho-1/2}{i} = \gamma - i(\beta - 1/2)$ for $\rho = \beta + i\gamma$: they are **real if and only if $\beta = 1/2$**. Under $\neg$RH the formula still holds, with complex nodes inside the strip. The reading of BRS as "non-redundant sampling of $f$ and $\widehat{f}$ along two real sequences" (the answer to the Shannon-type question) **is indeed conditional on RH + simplicity of zeros** — the authors state this verbatim ("Assuming for a moment the truth of the Riemann hypothesis and that all the zeta zeros are simple…").

**Corollary BRS 1.1 (unconditional; verified).** (i) If an even $f \in \mathcal{H}_1$ satisfies $\widehat{f}(\frac{\log n}{4\pi}) = 0$ for every $n \geq 1$ and $f^{(j)}(\frac{\rho-1/2}{i}) = 0$ for all $\rho, j$, then $f \equiv 0$. (ii) An even $f \in \mathcal{H}_1$ divisible by $\zeta(1/2+is)$ is determined by the values $\widehat{f}(\frac{\log n}{4\pi})$.

**Non-redundancy (verified):** the theorem and the corollary "break down if a single point" of $\{\frac{\log n}{4\pi}\}$ or of the multiset of zeros is removed. The BRS system is **exactly critical**.

**Mechanism (verified, §1 and §4 of BRS):** the kernel is $H(w,s) = \frac{\zeta(s)}{\zeta(w)}\,D(w,s)$, with $D(w,s) = \sum_n \beta_n(s)n^{-w/2}$ a Dirichlet series whose coefficients come from **modular integrals for the theta group** (a reinforced Knopp abundance principle). The zeros of $\zeta$ enter as **poles of $1/\zeta(w)$**: the position of the nodes is an output of the kernel, not an input of the modular machinery.

**Relation to the Riemann–Weil formula (verified, BRS pp. 3–4 and §4.4).** Literal quotation: *"the derivation of the Riemann–Weil formula starts from the Euler product representation of $\zeta(s)$, while formula (1.2) is tied to the Dirichlet series representation of $\zeta(s)$. We may think of the two formulas as respectively expressing a multiplicative and an additive duality relation between the zeros of zeta and a distinguished sequence of integers."* And further: *"the left-hand side of (1.1) defines a linear functional on $\mathcal{H}_1$, while the right-hand side gives the representation of this functional with respect to the basis functions of Theorem 1.1."* That is: **the explicit Weil formula IS a linear functional represented in the BRS basis**. This will be central in §5 and §6.

### 1.3. Kulikov; Kulikov–Nazarov–Sodin

- **Kulikov** (arXiv:2005.12836): uncertainty principle / density bound for Fourier interpolation bases. BRS state (p. 5, verified): *"there is a precise correspondence between Kulikov's density condition and the Riemann–von Mangoldt formula for the density of the non-trivial zeros of zeta and of $L$-functions."* The exact constant of the density inequality was not re-verified here [the precise numerical value is NOT VERIFIED; the qualitative statement is].
- **Kulikov–Nazarov–Sodin** (J. Math. Phys. Anal. Geom., 2023; arXiv:2306.14013, verified at the abstract level): for pairs of non-decreasing **$(p,q)$-supercritical** sequences ($1/p + 1/q = 1$, $p,q>1$, with density conditions), the pair has **Fourier uniqueness** and even strong interpolation; for **subcritical** pairs there exists a nonzero Schwartz function vanishing on both sets (non-uniqueness). The super/subcritical dichotomy is the quantitative version of the RV phenomenon.

### 1.4. Additional context

Cohn–Kumar–Miller–Radchenko–Viazovska (Ann. of Math. 196, 2022, "Universal optimality"): interpolation formulas with nodes $\sqrt{2n}$ in dimensions 8 and 24, also via modular forms [standard statement, not re-verified in detail]. BRS §2.5 (verified): Fourier interpolation bases generate families of **crystalline measures**, a topic connecting to Guinand, Meyer, Lev–Olevskii and Kurasov–Sarnak — exactly the theory destroyed in the previous audit (NOVEL-STRUCTURE-SEARCH, Candidate A). The dual connection is examined in §8.

---

## §2. The weight $\mu_\lambda = W_\lambda\,dm_\infty$ and the geometry of the frequencies $\{\gamma_n\}$

### 2.1. Asymptotics of the weight (computation)

By Stirling, $|\Gamma(\sigma + i\tau)| = \sqrt{2\pi}\,|\tau|^{\sigma - 1/2}e^{-\pi|\tau|/2}\,(1 + O(1/|\tau|))$. With $\sigma = 1/4$, $\tau = s/2$:
$$|\Gamma(1/4 + is/2)|^2 = 2\pi\,\Big(\frac{|s|}{2}\Big)^{-1/2}e^{-\pi|s|/2}\,(1 + O(1/|s|)),$$
whence the density of $dm_\infty$ is
$$w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 = \frac{\sqrt{2}}{2\pi}\,|s|^{-1/2}\,e^{-\pi|s|/2}\,(1 + O(1/|s|)).$$
*(Consistency note: Doc 85, §1.2, writes the constant as $1/(4\pi)$; the rate $e^{-\pi|s|/2}$ and the power $|s|^{-1/2}$ agree, the correct constant is $\sqrt{2}/(2\pi)$. The discrepancy is harmless: no argument in the program uses the constant.)*

Since $W_\lambda$ is a finite sum of squares of polynomials, $\mu_\lambda$ has density $W_\lambda(s)w(s) \asymp |s|^{d_\lambda - 1/2}e^{-\pi|s|/2}$ with $d_\lambda = 2\deg$ effective: **exponential decay of rate $\pi/2$, polynomially modulated**. Consequently (Doc 76, Prop. 1.5):
$$|\widehat{\mu_\lambda}(r)| = O(e^{-(\pi/4)|r|}), \qquad \widehat{\mu_\lambda} \ \text{analytic for } |\mathrm{Im}\,r| < \pi/2 \ \text{and uniformly continuous on } \mathbb{R}, \quad \widehat{\mu_\lambda}(0) = \mu_\lambda(\mathbb{R}) > 0.$$

**Lemma 2.1 (near-everywhere positivity of the kernel).** $W_\lambda(s) > 0$ for every $s \in \mathbb{R}$, whenever $N(\lambda) \geq 1$.

*Proof.* $W_\lambda$ is a sum of non-negative terms including $k|P_k|^2$ and $(a^\infty_{N})^2|P_{N+1}|^2$ for two consecutive indices $k = N, N+1$ (with $N = N(\lambda)$). $W_\lambda(s_0) = 0$ would require $P_N(s_0) = P_{N+1}(s_0) = 0$; but two consecutive orthogonal polynomials with respect to a measure with infinite support have no common zeros (standard interlacing property, a consequence of the three-term recurrence). $\square$

### 2.2. Geometry of $\{\gamma_n\}$: divergent density, vanishing separation, logarithmic clusters

The following three facts are **unconditional** (they only use Riemann–von Mangoldt and pigeonhole):

**(D1) Divergent mean density.** $N(T)/T \sim \frac{1}{2\pi}\log\frac{T}{2\pi} \to \infty$.

**(D2) Gaps tending to zero.** In $[T, 2T]$ there are $\gtrsim \frac{T}{2\pi}\log T$ zeros distributed over length $T$; by pigeonhole, there exist infinitely many $n$ with
$$\gamma_{n+1} - \gamma_n \;\leq\; \frac{2\pi}{\log(\gamma_n/2\pi)} \;\longrightarrow\; 0.$$
(If there are multiple zeros, there are even exactly vanishing gaps; we do not need this.)

**(D3) Logarithmic clusters.** For every $\eta > 0$ and every large $T$ there exists $m$ with $\gamma_m \in [T, 2T]$ such that
$$\#\{n : |\gamma_n - \gamma_m| \leq \eta\} \;\geq\; c\,\eta\,\log T$$
with $c > 0$ absolute. *Proof:* divide $[T,2T]$ into $\lceil T/\eta \rceil$ windows of length $\eta$; some window contains at least the average $\gtrsim \frac{\eta}{2\pi}\log T$ zeros; take $\gamma_m$ in that window. $\square$

The structural tension is exactly as anticipated: the density of the frequencies **grows without bound** ($\sim \frac{1}{2\pi}\log T$), while the weight, however strong its decay ($e^{-\pi|s|/2}$), is **fixed**. The decay of the weight controls the *exponential type* of the transforms (which gives completeness, Doc 85), but cannot absorb a *divergent* density in the quadratic frame inequalities, as is shown next.

### 2.3. The Beurling–Malliavin balance, made quantitative

To fix ideas with the heuristic of Doc 85, §2.2, in terms of a "Nyquist radius": the space of transforms $\{G(z) = \int g\,e^{izs}d\mu_\lambda : g \in L^2(\mu_\lambda)\}$ lives in the class of entire functions of exponential type $\leq \pi/4$ (Doc 76, Prop. 1.5). For that class, the *uniqueness* threshold (how many real zeros a $G \neq 0$ can have) is a finite linear density $\sim \frac{\pi/4}{\pi} = \frac{1}{4}$ per unit length; the $\gamma_n$ contribute local density $\frac{1}{2\pi}\log\frac{T}{2\pi}$, which exceeds the threshold by a factor $\to \infty$. This excess is what gives completeness with infinite margin (and the overcompleteness of Theorem 3.3). But the same computation shows the cost: for a **frame/Riesz** structure the requirement is not to exceed a threshold but to *match* it — density comparable to the bandwidth, plus uniform separation (Seip's theory for sampling/interpolation in Paley–Wiener and Bargmann–Fock spaces). Here the density/bandwidth ratio diverges logarithmically: the system is infinitely far from the frame regime, in the direction of absolute oversampling. **The decay of the weight plays no role in this ratio**: it only fixes the bandwidth $\pi/4$; no weight with continuous $\widehat{\mu}$ (that is, none) changes the conclusion (Corollary 3.5).

---

## §3. Question (i): the complete hierarchy — what $\{e^{i\gamma_n s}\}$ is and is not in $L^2(\mu_\lambda)$

Notation: $e_n := e_{\gamma_n}$, $\mathcal{H} = L^2(\mu_\lambda)$, $\lambda > 0$ fixed with $N(\lambda) \geq 1$. Note that $\|e_n\|^2_{\mathcal{H}} = \mu_\lambda(\mathbb{R})$ for every $n$ (the frequencies are real: $|e^{i\gamma_n s}| = 1$), and
$$\langle e_m, e_n\rangle_{\mathcal{H}} = \int e^{i(\gamma_m - \gamma_n)s}\,d\mu_\lambda(s) = \widehat{\mu_\lambda}(\gamma_m - \gamma_n).$$
The Gram matrix of the system is $G_{mn} = \widehat{\mu_\lambda}(\gamma_m - \gamma_n)$, with constant diagonal $\mu_\lambda(\mathbb{R})$.

### 3.1. There is no frame upper bound (not a Bessel system)

**Theorem 3.1 (unconditional).** There is no $B < \infty$ such that $\sum_n |\langle f, e_n\rangle|^2 \leq B\|f\|^2$ for every $f \in \mathcal{H}$. In particular $\{e_n\}$ **is not a frame** for $L^2(\mu_\lambda)$.

*Proof.* By continuity of $\widehat{\mu_\lambda}$ at $0$ and $\widehat{\mu_\lambda}(0) = \mu_\lambda(\mathbb{R}) > 0$, there exists $\eta > 0$ with $|\widehat{\mu_\lambda}(r)| \geq \mu_\lambda(\mathbb{R})/2$ for $|r| \leq \eta$. By (D3), for each large $T$ there exists $m = m(T)$ with $\gamma_m \in [T,2T]$ and $\#\{n : |\gamma_n - \gamma_m| \leq \eta\} \geq c\eta\log T$. Take $f = e_m$ (which lies in the system, $\|f\|^2 = \mu_\lambda(\mathbb{R})$):
$$\sum_n |\langle e_m, e_n\rangle|^2 \;\geq\; \sum_{n:\,|\gamma_n - \gamma_m|\leq\eta} |\widehat{\mu_\lambda}(\gamma_m - \gamma_n)|^2 \;\geq\; c\,\eta\,\log T \cdot \frac{\mu_\lambda(\mathbb{R})^2}{4}.$$
Then any Bessel constant satisfies $B \geq \frac{c\eta}{4}\mu_\lambda(\mathbb{R})\log T \to \infty$. $\square$

### 3.2. Not a Riesz sequence

**Theorem 3.2 (unconditional).** There is no $A > 0$ such that $\big\|\sum_k c_k e_{n_k}\big\|^2 \geq A\sum_k |c_k|^2$ for every finite combination. In particular $\{e_n\}$ **is not a Riesz basis** nor a Riesz sequence, not even after normalizing.

*Proof.* By (D2) there exist pairs $n, n+1$ with $\delta_n := \gamma_{n+1} - \gamma_n \to 0$. With $c = (1, -1)$:
$$\|e_n - e_{n+1}\|^2 = 2\big(\mu_\lambda(\mathbb{R}) - \mathrm{Re}\,\widehat{\mu_\lambda}(\delta_n)\big) \longrightarrow 0$$
by continuity of $\widehat{\mu_\lambda}$ at $0$. A Riesz lower bound would require $\|e_n - e_{n+1}\|^2 \geq 2A > 0$ for all such pairs. Contradiction. $\square$

### 3.3. Not minimal: total overcompleteness

**Theorem 3.3 (unconditional, modulo V.1).** For every $k$, the system $\{e_n\}_{n \neq k}$ remains complete in $L^2(\mu_\lambda)$. Consequently $\{e_n\}$ is not minimal: **no element is necessary**, and the system is not a Schauder basis of any kind.

*Proof.* The completeness argument of Doc 85 (Theorem 5.1) only uses the fact that the density of the frequency sequence is divergent relative to the exponential type $\pi/4$ of the transforms $G(z) = \int g\,e^{izs}d\mu_\lambda$. Removing one element (or any subset of density zero) does not alter $N(T)/T \to \infty$. Hence the same argument gives $G \equiv 0$. (Inherits the gap V.1 from Doc 85.) $\square$

### 3.4. Not an interpolation sequence

**Theorem 3.4 (unconditional).** $\{\gamma_n\}$ is not an interpolation sequence for $\mathcal{H}$: there exists $(c_n) \in \ell^\infty$ (in fact with only two values) such that no $f \in \mathcal{H}$ satisfies $\langle f, e_n\rangle = c_n$ for every $n$.

*Proof.* For a close pair $(n, n+1)$ as in 3.2, every $f \in \mathcal{H}$ satisfies
$$|\langle f, e_n\rangle - \langle f, e_{n+1}\rangle| \leq \|f\|\cdot\|e_n - e_{n+1}\| \to 0 .$$
Prescribing $c_n = 1$, $c_{n+1} = -1$ along a sequence of pairs with $\delta_n \to 0$ would require $\|f\| \geq 2/\|e_n - e_{n+1}\| \to \infty$. $\square$

### 3.5. Robustness: the refutation is independent of the weight

Theorems 3.1–3.4 use exactly two properties of $\mu_\lambda$: $\mu_\lambda(\mathbb{R}) < \infty$ and $\widehat{\mu_\lambda}$ continuous at $0$. But the second is automatic for any finite measure. Hence:

**Corollary 3.5 (no reweighting can repair the structure).** Let $\mu$ be **any** finite positive measure on $\mathbb{R}$ with $\mu \neq 0$. Then the system $\{e^{i\gamma_n s}\}$ in $L^2(\mu)$ is not Bessel, is not a Riesz sequence, and is not an interpolation sequence. In particular, no choice of $\lambda$, no modification of $W_\lambda$ within the class of positive integrable kernels, and no replacement of $dm_\infty$ by another finite measure can restore frame structure.

*Proof.* Identical to 3.1, 3.2, 3.4: only $\widehat{\mu}(0) = \mu(\mathbb{R}) > 0$, the uniform continuity of $\widehat{\mu}$ (automatic: $\mu$ finite), (D2) and (D3) were used. $\square$

**Remark 3.6 (the only formal way out is blocked).** For the refutations to fail one would need $\widehat{\mu}$ discontinuous at $0$ or non-decaying mass — that is, $\mu(\mathbb{R}) = \infty$. But with infinite $\mu$ the exponentials $e^{i\gamma s}$ cease to belong to $L^2(\mu)$ (their modulus is 1) and the system is not even defined. Remaining alternative: abandon pure exponentials for normalizable wavelet/Gabor-type elements over the $\gamma_n$ — this changes the mechanism (it ceases to be the system of Doc 85) and is not evaluated here; any future attempt must first pass Dichotomy 8.1.

**Remark 3.7 (why BRS does obtain interpolation with the same $\gamma_n$).** There is no contradiction between Theorems 3.1–3.4 and Theorem BRS 1.1. BRS does not work in the $L^2$ of a measure with a single sampling side: its space $\mathcal{H}_1$ is a much smaller **analytic-in-a-strip** class, and its node system is **two-sided** — values of $f$ at the zeros **and** values of $\widehat{f}$ at $\{\frac{\log n}{4\pi}\}$. Exact criticality (non-redundancy) lives in that two-sided time-frequency geometry. The program's system uses a single side (frequencies $\gamma_n$ against a fixed measure), and with a single side the divergent density is incurably excessive. Structural lesson: *the natural geometry of the zeros as nodes is not that of a basis in a weighted $L^2$, but that of one half of a critical time-frequency pair* — and the other half is the logarithms of the integers.

### 3.8. Synthesis of (i)

| Property | Holds? | Status |
|---|---|---|
| Completeness | **YES** | Unconditional (Doc 85, modulo V.1) |
| Overcompleteness (non-minimality) | **YES** | Theorem 3.3, unconditional (modulo V.1) |
| Frame upper bound (Bessel) | **No** | Theorem 3.1, unconditional |
| Frame | **No** | Corollary of 3.1 |
| Riesz sequence / basis | **No** | Theorem 3.2, unconditional |
| Interpolation sequence | **No** | Theorem 3.4, unconditional |
| Isolated frame lower bound | Open | Irrelevant: without an upper bound there is no bounded analysis operator or stable reconstruction |

**Conclusion of (i).** The answer is definitive and negative at every quantitative level: the system is *only* complete. The divergent density $\frac{1}{2\pi}\log T$ is simultaneously the source of completeness (there is excess density for the Carlson argument) and the poison of every frame structure (logarithmic clusters break Bessel; vanishing gaps break Riesz and interpolation). The exponential decay of the weight **does not compensate**: it fixes the exponential type $\pi/4$ of the transforms, but the frame inequalities are insensitive to the type and sensitive to the local density, which diverges. This is not a gap: it is a theorem against.

---

## §4. Question (ii): what each level would say about $d\nu$ — and what the level we have says

### 4.0. Preliminary remark: where the $\gamma_n$ "live" relative to $d\nu$

It is worth fixing the exact geometric relation, because it is the source of the self-reference detected in §6. The measure $d\nu = (R-1)\,dm_{full,on}$ has density $\propto \sum_{j:\delta_j>0} \delta_j^2/(s-\gamma_j)^2 + O(\delta^4)$ to first order (Doc 89, §2.1): it is **concentrated around the ordinates $\gamma_j$ of the off-critical zeros**. The frequencies of the system $\{e^{i\gamma_n s}\}$ are **all** the ordinates (on and off). That is: the $\gamma_n$ enter the mechanism twice — as the approximate support of the object to be annihilated and as the frequencies of the system that tests it. Any identity we produce will link zeros to themselves through the primes; arithmetic content enters only through the global rigidity of $\zeta$ (via $dm_{full}$), never through the system of exponentials.

### 4.1. The exact bridge between the system and $d\nu$

**Lemma 4.1 (unconditional).** Let $h := \dfrac{d\nu}{dm_\infty} = \big(|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2\big) \geq 0$. Then $h \in L^2(\mu_\lambda)$ and
$$T_\lambda = \langle h, \mathbf{1}\rangle_{L^2(\mu_\lambda)}, \qquad \langle h, e_n\rangle_{L^2(\mu_\lambda)} = \int e^{-i\gamma_n s}\,W_\lambda(s)\,d\nu(s) = \big(W_\lambda\,d\nu\big)^{\wedge}(-\gamma_n) =: \widehat{\nu_\lambda}(-\gamma_n).$$

*Proof.* $0 \leq h \leq |\zeta(1/2+is)|^2$ pointwise (since $R \geq 1 \Rightarrow |\zeta_{on}| \leq |\zeta|$). By the unconditional convexity bound $|\zeta(1/2+it)| \ll (1+|t|)^{1/4+\varepsilon}$,
$$\int h^2\,d\mu_\lambda \leq \int |\zeta(1/2+is)|^4\,W_\lambda(s)\,w(s)\,ds \ll \int (1+|s|)^{1+\varepsilon}\,|s|^{d_\lambda - 1/2}e^{-\pi|s|/2}\,ds < \infty.$$
The two identities are direct rewritings of $T_\lambda = \int W_\lambda\,d\nu$ and of the definition of the inner product. $\square$

### 4.2. The ladder of implications (exact statements)

**(The "complete" level — the one we HAVE).**

**Proposition 4.2 (new equivalent condition; "Condition 9" for the table of Doc 89).** *Unconditionally (modulo V.1), for any fixed $\lambda$ with $N(\lambda) \geq 1$:*
$$\mathrm{RH} \iff \big(W_\lambda\,d\nu\big)^{\wedge}(\gamma_n) = 0 \quad \text{for every } n \geq 1.$$

*Proof.* ($\Rightarrow$) RH $\Rightarrow d\nu = 0 \Rightarrow$ trivial. ($\Leftarrow$) By Lemma 4.1, the hypotheses say $\langle h, e_n\rangle = 0$ for every $n$ ($d\nu$ is even, Prop. 8.1 of Doc 89, so vanishing at $\gamma_n$ is equivalent to vanishing at $-\gamma_n$). By completeness (Doc 85, Theorem 5.1), $h = 0$ in $L^2(\mu_\lambda)$, that is $h\,W_\lambda\,w = 0$ a.e.; by Lemma 2.1 ($W_\lambda > 0$) and $w > 0$, $h = 0$ a.e., hence $d\nu = 0$, hence RH (Doc 89, Theorem 10.1, (1)$\iff$(2)). $\square$

This is the first condition in the program that tests $d\nu$ **only at the frequencies $\gamma_n$** (countable, with no supremum over $\lambda$ nor over $z \in \mathbb{H}$). Its honesty is audited in §6.3: it is a CAP-style condition, not verifiable without the zeros.

**(The "frame" level — the one we do NOT have, refuted).** If $\{e_n\}$ were a frame with bounds $A, B$, we would have
$$A\,\|h\|^2_{L^2(\mu_\lambda)} \;\leq\; \sum_n \big|\widehat{\nu_\lambda}(\gamma_n)\big|^2 \;\leq\; B\,\|h\|^2_{L^2(\mu_\lambda)},$$
and with Cauchy–Schwarz $T_\lambda = \langle h, \mathbf{1}\rangle \leq \mu_\lambda(\mathbb{R})^{1/2}\|h\|$ one would obtain the **quantitative bound**
$$T_\lambda^2 \;\leq\; \frac{\mu_\lambda(\mathbb{R})}{A}\,\sum_n \big|\widehat{\nu_\lambda}(\gamma_n)\big|^2.$$
That is: *numerical control of the samples of $\widehat{\nu_\lambda}$ at the zeros would control $T_\lambda$, with stability against errors*. This would have been a mechanism for "effective RH by sampling". **Theorem 3.1 shows that the right-hand inequality is false ($B = \infty$) and hence the quantitative mechanism does not exist.** The isolated left-hand inequality remains open but without the right one there is no stable reconstruction.

**(The "Riesz/interpolation" level — refuted).** A Riesz basis would additionally give uniqueness of coefficients and an isomorphism $\mathcal{H} \simeq \ell^2$ turning $T_\lambda$ into an explicit quadratic form in the samples $\{\widehat{\nu_\lambda}(\gamma_n)\}$ with two-sided bounds — the full quantitative dream. False by Theorem 3.2.

### 4.2bis. On coefficient functionals (why there is no dual system either)

To complete the picture: even without a frame, a complete system can sometimes admit a **dual system** $\{g_n\} \subset \mathcal{H}$ with $\langle g_m, e_n\rangle = \delta_{mn}$ (biorthogonality), which would allow $T_\lambda$ to be written as a series of coefficients. Theorem 3.3 (overcompleteness: every cofinite subsystem remains complete) excludes this: if a biorthogonal $g_m$ existed, $g_m$ would be orthogonal to $\overline{\mathrm{span}}\{e_n : n \neq m\} = \mathcal{H}$, hence $g_m = 0$, contradicting $\langle g_m, e_m\rangle = 1$. **No system of coefficient functionals exists**: the expansion of $h$ (the density of $d\nu$ with respect to $dm_\infty$) in the exponentials of the zeros exists as an approximation (completeness) but its coefficients are neither unique nor continuous. This retrospectively explains why Doc 82 could not extract a coefficient-by-coefficient criterion from Path 3, and why BRS need to leave $L^2$ for $\mathcal{H}_1$ and add the second family of nodes to have biorthogonality (their relations (1.3) are exactly the biorthogonality that is impossible here).

### 4.3. Conclusion of (ii)

The hierarchy collapses informatively: **completeness alone already delivers all the qualitative content that a frame would deliver** (the equivalence of Proposition 4.2: $d\nu$ is determined by its samples at the $\gamma_n$); what the frame would add is exclusively **quantitative stability** (bounds $A, B$), and that is exactly what Theorems 3.1–3.2 refute unconditionally. There is no quantitatively stable version of sampling $d\nu$ at the zeros within $L^2(\mu_\lambda)$.

---

## §5. Question (iii): does the modular machinery inject external arithmetic that evades MW-2/MW-7?

This is the central discriminating question. The answer requires three steps: identify what arithmetic input RV/BRS use, see through which channel it touches $\zeta$, and see whether that channel is sensitive to $\mathrm{Re}(\rho)$.

### 5.1. What the modular input really is

- **RV:** weakly holomorphic modular forms of weight $3/2$ for $\Gamma_\theta$. The generator of the whole structure is the theta function $\theta(\tau) = \sum_{n\in\mathbb{Z}} e^{\pi i n^2\tau}$ and its transformation law $\theta(-1/\tau) = \sqrt{\tau/i}\,\theta(\tau)$. The verified fact that the RV formula evaluated at $x = 0$ **reduces to Poisson summation** (§1.1) reveals the content: the RV formula is an *interpolatory unfolding* of the modularity of $\theta$, which is in turn equivalent to Poisson summation over $\mathbb{Z}$.
- **BRS:** modular integrals for $\Gamma_\theta$ (Eichler cohomology / Knopp's principle) build $D(w,s)$; the kernel that produces the nodes is $H(w,s) = \frac{\zeta(s)}{\zeta(w)}D(w,s)$, and its functional equations $H(1-w,s) = -H(w,s)$, $H(w,1-s) = H(w,s)$ rest on the **functional equation of $\zeta$**.

**Remark 5.1 (the channel is the functional equation).** By Riemann's classical argument (1859) and Hecke's converse theorem, the modularity of $\theta$ under $\tau \mapsto -1/\tau$ and the functional equation $\pi^{-s/2}\Gamma(s/2)\zeta(s) = \pi^{-(1-s)/2}\Gamma((1-s)/2)\zeta(1-s)$ are **equivalent** via the Mellin transform. Hence the "external arithmetic input" of the RV/BRS machinery, *insofar as it touches $\zeta$*, is exactly the functional equation — a datum the program (and every program: Weil, de Branges, Connes) already has and already exploits. No new arithmetic enters through that channel.

### 5.2. What is genuinely new in BRS — and why it is not the lever

One must be precise and fair: BRS prove something that is **not** the explicit Weil formula. The verified comparison (§1.2):

| | Weil formula (1.1 in BRS) | BRS formula (1.2) |
|---|---|---|
| Analytic input | **Euler product** + functional equation | **Dirichlet series** + functional equation |
| Sequence of integers | prime powers $n = p^k$, weights $\Lambda(n)/\sqrt{n}$, nodes $\frac{\log n}{2\pi}$ | **all** integers, nodes $\frac{\log n}{4\pi}$ |
| Nature of the duality | multiplicative | **additive** |
| Structure | identity (one linear functional) | **interpolation basis** (complete system of functionals) |

The additive duality (zeros $\leftrightarrow$ all integers) is structurally distinct information from the explicit formula: BRS underline this, and the fact that the Weil formula is *one* functional represented in the BRS basis (quote in §1.2) shows that (1.2) is finer than (1.1). **Answer to the sub-question: the BRS dual formula is NOT exactly the explicit Weil formula; it is strictly finer (Weil = one functional; BRS = the entire basis), and it comes from the Dirichlet series, not from the Euler product.**

But here is the decisive point for MW-2: precisely because BRS avoids the Euler product, its input is (global Dirichlet series) + (functional equation) — and the Dirichlet series $\sum n^{-s}$ of $\zeta$ **does not contain the multiplicative information** that MW-2 declares confined to $\mathrm{Re}(s) > 1$. BRS does not break MW-2: it **sidesteps it by giving up the arithmetic of the primes**. The theorem works equally well for any Dirichlet series with a functional equation of the appropriate type (BRS §5 does this for Dirichlet characters and "other Dirichlet series" — including, note, the class where counterexamples of Davenport–Heilbronn type with off-line zeros live). A machinery that applies indiscriminately to $\zeta$ and to functions with documented off-line zeros cannot, by itself, feel $\mathrm{Re}(\rho) = 1/2$.

### 5.3. The proof of insensitivity to $\mathrm{Re}(\rho)$ (the I2b test in action)

Three independent verifications that the whole theory is **blind to $\beta_j = \mathrm{Re}(\rho_j)$**:

1. **The nodes.** Theorem BRS 1.1 is unconditional with nodes $\frac{\rho - 1/2}{i} = \gamma - i(\beta - 1/2)$: if a zero leaves the line, the node **leaves $\mathbb{R}$ and the formula still holds, intact**, in the strip. The modular machinery exerts no pressure pushing the nodes toward $\mathbb{R}$. The reality of the nodes is not an output: it is a *reformulation* of RH (see §8: it is the interpolatory avatar of Lee–Yang).
2. **The densities.** All the quantitative content of uniqueness/interpolation theory (Kulikov; KNS super/subcritical; BRS's exact criticality) depends on **counting functions**: and $N(T)$ is the same under RH and under $\neg$RH (Riemann–von Mangoldt counts zeros in the strip, not on the line; Doc 85, Remark 4.3). The "precise correspondence between Kulikov's density condition and Riemann–von Mangoldt" (§1.3) is beautiful, but it is a correspondence with a $\beta$-blind invariant. The parallel with RV is exact: there the nodes $\sqrt{n}$ have counting function $N(r) = r^2$, which is precisely the KNS criticality for the pair $(\sqrt{n}, \sqrt{n})$; the arithmetic of the nodes enters only through its count and the modularity of $\theta$ — at no point in the theory does a theorem turn a count into a position.
3. **The only $\beta$-sensitive statement is conditional.** The reading "non-redundant sampling over two real sequences" — the only statement in the corpus requiring real nodes — **assumes RH and simplicity** (verified, §1.2). That is: within the literature itself, sensitivity to $\mathrm{Re}(\rho)$ only ever appears as a hypothesis, never as a conclusion.

### 5.3bis. The Davenport–Heilbronn witness

The hardest test of $\beta$-blindness is an explicit counterexample. The Davenport–Heilbronn function $L_{DH}$ (a combination of Dirichlet $L$-functions mod 5) satisfies a functional equation of Riemann type and **has zeros off the critical line**, proved. BRS, §5.3, extend their construction to "zeros of other Dirichlet series" with a functional equation of the form $Q^{-s}\Gamma(s/2)F(s) = Q^{-(1-s)}\Gamma((1-s)/2)\overline{F(1-\bar{s})}$ (verified on p. 5 of the PDF: the remark that it suffices to replace $\zeta(s)/\zeta(w)$ by $F(s)/F(w)$). Whether $L_{DH}$ is literally covered by the exact hypotheses of BRS §5.3 remains [NOT VERIFIED in detail]; what is verified is the principle: **the machinery only consumes Dirichlet series + functional equation, and that pair is satisfied by functions with off-line zeros**. A machinery whose natural domain contains counterexamples to "local RH" cannot, without additional input, contain the theorem that would prove it for $\zeta$. This is the same pattern the program documented for the DBN flow (FAIL I4, arithmetic blindness) — here the blindness is not to the primes but to the $\beta$-position of the zeros, with an identical discriminating effect.

### 5.4. Verdict on (iii)

**The modular input does NOT evade MW-2/MW-7.** To be precise:

- It does not evade it because it carries no Euler product: the modularity of $\theta$ = the functional equation (Remark 5.1), and the genuinely new part (additive duality, Knopp cohomology) operates at the level of general Dirichlet series, where RH is false in general.
- The structural point registered in favor in NOVEL-STRUCTURE-SEARCH ("the formulas are built with modular forms — external input not derived from the Euler product, possibly not blocked by MW-2") is **resolved negatively**: the input is indeed external to the Euler product — but for that very reason it is *even weaker* than the Euler product with respect to the critical strip. MW-2 blocks the propagation of multiplicative arithmetic; the modular machinery does not even carry it.
- What would have been an evasion: a theorem on the modular side that **forces** the reality of the nodes (the analogue of the Hodge index in the function-field case). None exists in RV/BRS/KNS, and item 1 of §5.3 shows that the structure of the theorems points in the opposite direction (unconditional validity with complex nodes = no force toward $\mathbb{R}$).

---

## §6. Question (iv): Heisenberg-type uniqueness for $d\nu$

### 6.1. Properties of $d\nu$ verifiable without knowing the zeros (the "data" side)

Unconditional, without zero positions (Docs 83, 89 + new computation):

- (V-a) $d\nu \geq 0$.
- (V-b) $d\nu(-s) = d\nu(s)$ (parity).
- (V-c) $\|d\nu\| < \infty$ and more finely: $d\nu \leq dm_{full}$, whose density is verifiable from $\zeta$ and decays like $|s|^{1/2+\varepsilon}e^{-\pi|s|/2}$.
- (V-d) **(new, computation)** $\widehat{\nu}(z) = \int e^{izs}d\nu(s)$ is analytic in the strip $|\mathrm{Im}\,z| < \pi/2$ and bounded on substrips, because the tails of $d\nu$ are dominated by $e^{-\pi|s|/2}$ by (V-c). Likewise the density $h$ of $d\nu$ with respect to $ds$ extends analytically to $|\mathrm{Im}\,s| < 1/2$ (the only singularities of $\zeta(1/2+is)\zeta(1/2-is)$ are $s = \pm i/2$, and the "on" piece has the same structure).

### 6.2. Forcing pairs (the "theorems" side): which combinations force $d\nu = 0$

**(P1) Analyticity + vanishing on a set with accumulation.** By (V-d), if $\widehat{\nu} = 0$ on any interval $(-\delta,\delta)$ (or on a set with an accumulation point in the strip), then $\widehat{\nu} \equiv 0$ and $d\nu = 0$. — *Forcing; but the condition is not verifiable:* $\widehat{\nu} = \widehat{dm_{full}} - \widehat{dm_{full,on}}$, and the second term requires $\zeta_{on}$, that is, **all** the positions $\beta_j$. (The first term, $\widehat{dm_{full}}$, is in principle computable from $\zeta$ — it is a second-moment / Motohashi-type object — but that does not rescue anything without its partner.)

**(P2) Analyticity + sampling at the $\gamma_n$ (divergent density).** Measure version of Proposition 4.2: $\widehat{\nu}$ is analytic and bounded on substrips; if $\widehat{\nu}(\gamma_n) = 0$ for every $n$, with $N(T)/T \to \infty$, a Carlson/Levinson-type argument in the strip forces $\widehat{\nu} \equiv 0$. — *Forcing (modulo the same technical verification V.1); the condition is not verifiable and doubly self-referential: the nodes are the zeros and the object is built from the zeros.*

**(P3) KNS supercritical uniqueness pairs.** If one takes $F$ = (a Schwartz-class regularization of $\widehat{\nu}$, gap declared below) and a supercritical KNS pair $(\Lambda_1, \Lambda_2)$ **not involving zeros** (e.g. powers $n^a$): $F|_{\Lambda_1} = 0$ and $\widehat{F}|_{\Lambda_2} = 0 \Rightarrow F = 0$. — *Forcing; but the conditions $F|_{\Lambda_1} = 0$ are evaluations of $\widehat{\nu}$, again inaccessible without $\zeta_{on}$.* **Declared gap:** KNS is stated for Schwartz functions; $\widehat{\nu}$ lies in an analytic-in-a-strip class whose decay must be verified (the density $h$ oscillates with frequencies $\sim \log$; the decay of $\widehat{\nu}$ on horizontal lines follows from the analyticity of $h$ in $|\mathrm{Im}\,s|<1/2$, giving $\widehat{\nu}(x) \ll e^{-(1/2-\varepsilon)|x|}$, sufficient; exact membership in $\mathcal{H}_1$ or in Schwartz is not verified here — **technical gap G.101.1**).

**(P4) The BRS pair applied to $F = \widehat{\nu}$ (if $F \in \mathcal{H}_1$, gap G.101.1).** Corollary BRS 1.1(i): $\widehat{F}\big(\frac{\log n}{4\pi}\big) = 0\ \forall n$ **and** $F^{(j)}\big(\frac{\rho-1/2}{i}\big) = 0\ \forall \rho,j \Rightarrow F \equiv 0 \Rightarrow d\nu = 0 \Rightarrow$ RH. Note what each family means: $\widehat{F}$ recovers the density $h$ of $d\nu$ (pointwise vanishing of $h$ at points $\asymp \log n$), and the second family samples $\widehat{\nu}$ **at the zeros themselves**, with multiplicities and with complex nodes if $\neg$RH. — *Forcing, unconditional, and the strongest uniqueness theorem available in the literature; but one of the two node families IS the multiset of zeros: unavoidable self-reference.*

### 6.3. Detecting circularity (explicitly)

**Proposition 6.1 (the explicit formula applied to $d\nu$ reproduces $T_\lambda$).** Every evaluation of the functionals in (P1)–(P4) via the explicit formula reproduces objects the program already has. Concretely: Doc 72 proved
$$T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}}\,B_\lambda(\log p),$$
that is, the Riemann–Weil evaluation of the functional $\int W_\lambda\,d\nu$ is exactly the zeros/primes decomposition of Doc 72. And the verified BRS remark (§1.2) — *the Weil formula is the linear functional $\mathcal{H}_1 \to \mathbb{C}$ represented in the BRS basis* — implies that representing the functionals of $d\nu$ in the BRS basis is a change of basis of the same datum, not new data. In symbols: if $\Phi_{Weil}(f) = \sum_\rho f\big(\frac{\rho-1/2}{i}\big) - (\text{prime side})$, then the coefficients of $\Phi_{Weil}$ in the basis $\{U_n, V_{\rho,j}\}$ are computed by evaluating at the nodes — the zeros again. **There is no free lunch: the BRS basis re-expands the information of the zeros over the zeros.** $\square$

### 6.2bis. The data × theorems matrix (the full picture of the uniqueness problem)

Heisenberg-type formulation: which pairs (condition on $d\nu$, condition on transforms of $d\nu$) force $d\nu = 0$, and which of their ingredients are verifiable without zero positions?

| Ingredient | Forcing (in a suitable pair)? | Verifiable without zero positions? |
|---|---|---|
| $d\nu \geq 0$ (V-a) | Not by itself (Doc 89, Prop. 11.1) | **YES** (Doc 83) |
| parity (V-b) | No | **YES** |
| $d\nu \leq dm_{full}$, tails $e^{-\pi\vert s\vert/2}$ (V-c) | No | **YES** |
| $\widehat{\nu}$ analytic for $\vert\mathrm{Im}\,z\vert < \pi/2$ (V-d) | Only combined | **YES** (consequence of V-c) |
| $\widehat{\nu} = 0$ on an interval (P1) | **YES** (with V-d) | No — requires $\widehat{dm_{full,on}}$ |
| $\widehat{\nu}(\gamma_n) = 0\ \forall n$ (P2 / Cond. 9) | **YES** (with V-d, modulo V.1) | No — doubly self-referential |
| $\widehat{\nu}$ vanishing on $\Lambda_1$ and $h$ vanishing on $\Lambda_2$, KNS supercritical pair (P3) | **YES** (modulo G.101.1) | No — same inaccessible evaluations |
| BRS pair: $h$ at $\asymp\log n$ and $\widehat{\nu}^{(j)}$ at $\frac{\rho-1/2}{i}$ (P4) | **YES**, unconditional (modulo G.101.1) | No — one node family IS the multiset of zeros |

The structure is exact: **the "verifiable" column and the "forcing" column have empty intersection**. The four verifiable properties (positivity, parity, majorant, analyticity in a strip) are compatible with $d\nu \neq 0$ — indeed any even positive measure with tails $O(e^{-\pi|s|/2})$ satisfies them, and the class of such measures is infinite-dimensional. The four forcing theorems consume pointwise evaluations of $\widehat{\nu}$ or of $h$, all with epistemic cost = knowing $\{\beta_j\}$. Interpolation theory shifts the frontier of the theorems (finer, countable, critical) without moving the frontier of the data by a hair.

**Synthesis of (iv) — the Hadamard wall, interpolatory version.** Interpolation/uniqueness theory **genuinely enlarges the catalog of forcing conditions** (P1–P4 are finer than those of Doc 89: countable samplings, non-redundant critical pairs) but **does not add a single verifiable condition**: in every (data, theorem) pair, the data side requires $\widehat{\nu}$ or $h$, and both require $dm_{full,on}$, that is, the positions $\{\beta_j\}$. The MW-7 wall is not in the test sets (which interpolation lets one choose with enormous freedom): it is in the **object** $d\nu$, whose very definition consumes the positions of the zeros. Changing the nodes does not change the object. This is the sharpest formulation of MW-7 achieved so far: *the epistemic inaccessibility of $d\nu$ is invariant under Fourier duality and under change of interpolation basis.*

---

## §7. Question (v): the discriminator (I1, I2a, I2b, I3, I4)

Mechanism evaluated: **"Fourier interpolation / frame structure over the zeros as a lever for $d\nu = 0$"**, in its two variants: (a) quantitative frame in $L^2(\mu_\lambda)$; (b) modular RV/BRS machinery.

| Criterion | Variant (a): frames | Variant (b): modular RV/BRS |
|---|---|---|
| **I1** (encodes all the primes) | checked — via $dm_{full}$ and the $\gamma_n$ | checked — kernel $\zeta(s)/\zeta(w)$; nodes $\frac{\log n}{4\pi}$ |
| **I2a** (independent input exists) | failed — the space $L^2(W_\lambda dm_\infty)$ and the frequencies are $\zeta$ re-encoded (same diagnosis as de Branges in the Phase A table) | partial/checked — Eichler–Knopp cohomology and the weight-$3/2$ forms for $\Gamma_\theta$ are genuinely external structure; but the channel through which they touch $\zeta$ is only the functional equation (Remark 5.1) |
| **I2b** (decisive theorem supplying the restriction) | failed — worse than absent: the desired quantitative restriction (frame bounds) is **false by theorem** (3.1–3.2) | failed — no theorem in the corpus forces real nodes; unconditional validity with complex nodes (§5.3, item 1) shows the machinery exerts no pressure on $\mathrm{Re}(\rho)$ whatsoever; every quantitative invariant (densities) is $\beta$-blind |
| **I3** (localizes individual zeros) | checked — one frequency per zero | checked — one basis function $V_{\rho,j}$ per zero (with multiplicity) |
| **I4** (genuinely arithmetic) | checked | checked |

**Verdict:** variant (a) fails I2a and I2b (with I2b constructively refuted — the strongest failure case recorded in the program: not "the theorem is missing" but "the anti-theorem exists"). Variant (b) has the **exact Connes profile from the Phase A table**: I1 checked, I2a checked/partial, I2b failed, I3 checked, I4 checked → **FAIL I2b**. The modular input exists and is external, but comes without a theorem that does the work (the analogue of the Hodge index / Stepanov is absent). Under Phase A's hardened criterion, FAIL I2b = a program stalled at the same point as Connes/Deninger/Connes–Consani.

Fine note on the FAIL: it is not FAIL I2a (the mechanism is not *literally* CAP positivity — its theorems are unconditional and $\beta$-blind); the failure mode is that of the **dichotomy** formulated in §8.

---

## §8. The structural dichotomy: interpolation and quasicrystals are the same wall seen from two sides

The previous audit destroyed quasicrystal rigidity: Kurasov–Sarnak ⟹ every $\mathbb{N}$-valued 1-D crystalline measure is the toral zero set of a Lee–Yang polynomial, and "reality of the support" = Lee–Yang property = Hermite positivity = CAP. Fourier interpolation is the dual theory (BRS §2.5: interpolation bases *generate* crystalline measures; Guinand, Meyer, Lev–Olevskii). The present audit closes the other side and reveals the symmetry:

**Dichotomy 8.1.** Every statement in interpolation/uniqueness/crystallinity theory relative to the zeros of $\zeta$ falls into exactly one of two classes:
1. **$\beta$-blind and unconditional** (Theorem BRS 1.1 with complex nodes; Corollary 1.1; Kulikov/KNS densities; Riemann–von Mangoldt; our completeness Doc 85 and Theorems 3.1–3.4): holds equally under RH and under $\neg$RH, hence **cannot be a lever**.
2. **$\beta$-sensitive and RH-equivalent or RH-conditional** (real nodes / non-redundant sampling over real sequences; crystallinity of $\sum_\rho \delta_\gamma$; Lee–Yang): here sensitivity to $\mathrm{Re}(\rho)$ is present, but the statement **is** RH (or assumes it), hence it is CAP under another name.

The quasicrystal side collapses via branch 2 (Lee–Yang = CAP); the interpolation side collapses via branch 1 (unconditional = no edge). Fourier duality exchanges the two branches but **maps the wall onto itself**. There is no $\beta$-sensitive, non-RH-equivalent statement anywhere in the RV/BRS/KNS/KS corpus: that statement would be precisely the missing I2b.

---

## §9. Byproducts incorporated into the program

Although the route is closed, the audit leaves two results and two new gaps. For incorporation into the corpus they are stated in citable form:

1. **Theorem 101.A (non-structure; unconditional).** *Let $\mu$ be any nonzero finite positive measure on $\mathbb{R}$ and $\{\gamma_n\}$ the ordinates of the non-trivial zeros of $\zeta$. The system $\{e^{i\gamma_n s}\}$ in $L^2(\mu)$ admits no frame upper bound, is not a Riesz sequence, and is not an interpolation sequence; for $\mu = W_\lambda dm_\infty$ it is moreover complete and overcomplete (every cofinite subsystem is complete, modulo V.1).* — This definitively closes the question Doc 85 left implicit ("what the standard theorem cannot directly guarantee is the Riesz basis", Doc 85 §1.2, Remark): the Riesz basis is not unguaranteed, it is **false**. Ingredients: Riemann–von Mangoldt + pigeonhole + continuity of $\widehat{\mu}$; nothing more.

2. **Proposition 101.B (Condition 9; unconditional modulo V.1).** *For any fixed $\lambda$ with $N(\lambda)\geq 1$: RH $\iff (W_\lambda\,d\nu)^\wedge(\gamma_n) = 0$ for every $n$.* Added to the table of Doc 89 §6 with the honest annotation: CAP-style, not verifiable without zero positions (MW-7); its interest lies in minimal cardinality (countable, with no supremum over $\lambda$ nor over $z \in \mathbb{H}$) and in form (it is the first condition in the catalog whose test points are the $\gamma_n$ themselves).

3. **Dichotomy 101.C (= 8.1, taxonomic):** every statement in the interpolation/uniqueness/crystallinity corpus about zeros of $\zeta$ is either $\beta$-blind and unconditional (no edge), or $\beta$-sensitive and RH-equivalent/conditional (CAP renamed). Admission test for any future candidate in this family: first exhibit a $\beta$-sensitive, non-RH-equivalent statement.

4. **Gap G.101.1:** membership of $\widehat{\nu}$ in $\mathcal{H}_1$ (or in Schwartz after regularization) — needed to formally activate (P3)/(P4) of §6.2. Declared, not resolved; of only taxonomic interest given the verdict.

5. **Item V.1 (inherited, Doc 85):** the Carlson–Beurling verification remains pending and conditions Proposition 101.B and the completeness part of Theorem 101.A. The refutations (non-Bessel, non-Riesz, non-interpolation) **do not** depend on V.1.

---

## §10. VERDICT

**ROUTE CLOSED.**

**Precise reason, in three cuts:**

1. **The frame mechanism is false by theorem, not by gap.** The logarithmically divergent density of the $\gamma_n$ (clusters of size $\log T$, gaps $\to 0$ — all unconditional, Riemann–von Mangoldt) destroys the frame upper bound, the Riesz lower bound, minimality, and the interpolation property in $L^2(W_\lambda dm_\infty)$, for every $\lambda$ (Theorems 3.1–3.4). The exponential decay $e^{-\pi|s|/2}$ of the weight fixes the type of the transforms (hence completeness) but is structurally unable to buy quadratic stability against a divergent density. No quantitative version of sampling $d\nu$ at the zeros remains that could become an effective criterion.

2. **The modular input does not evade MW-2/MW-7.** The channel through which the modular forms of $\Gamma_\theta$ touch $\zeta$ is the modularity of $\theta$, which is the functional equation of $\zeta$ via Mellin (Riemann/Hecke) — a datum already possessed and already inert against the critical strip. The genuinely new part of BRS (**additive** duality zeros↔integers, strictly finer than the Weil formula, which turns out to be *one* functional represented in its basis) comes from the Dirichlet series, not from the Euler product: it sidesteps MW-2 by giving up multiplicative arithmetic, and that is why it applies equally to series with off-line zeros. The whole theory is $\beta$-blind where it is unconditional and RH-equivalent/conditional where it is $\beta$-sensitive (Dichotomy 8.1). The discriminator gives **FAIL I2b** — the Connes profile: genuine external structure, with no decisive theorem forcing the nodes onto $\mathbb{R}$.

3. **Heisenberg-type uniqueness enlarges the forcing theorems but not the verifiable data.** Pairs (P1)–(P4) — including the strongest available in the literature, the unconditional Corollary BRS 1.1 — force $d\nu = 0$ from conditions that require $\widehat{\nu}$ or $h$, and hence $\zeta_{on}$, and hence the positions of all the zeros; moreover one family of BRS nodes *is* the multiset of zeros, and the evaluation via the explicit formula reproduces exactly the decomposition $T_\lambda = A^{off}_\lambda - \sum_p(\log p/\sqrt{p})B_\lambda(\log p)$ of Doc 72 (Proposition 6.1). The MW-7 wall turns out to be invariant under Fourier duality and under change of interpolation basis: it lies in the object $d\nu$, not in the test sets.

**Incorporated into the program** are the byproducts of §9 (non-structure theorem; Condition 9; gaps G.101.1 and inherited V.1). **Not recommended**: continuing the interpolation front as a lever toward RH; its only legitimate future use is taxonomic (Dichotomy 8.1 as a quick test: any future candidate in this family must exhibit, before anything else, a $\beta$-sensitive, non-RH-equivalent statement — the missing I2b).

---

## Appendix — Honesty checklist

| Claim | Status |
|---|---|
| Theorems 3.1, 3.2, 3.4 and Corollary 3.5 (non-Bessel, non-Riesz, non-interpolation, robustness) | **Proved here**, unconditional, self-contained (Riemann–von Mangoldt + pigeonhole + continuity of $\widehat{\mu}$) |
| Theorem 3.3 (overcompleteness) and the starting completeness | Unconditional **modulo V.1** (gap inherited from Doc 85, declared) |
| Lemma 4.1 ($h \in L^2(\mu_\lambda)$) | Proved here, unconditional (uses only the convexity bound $\zeta(1/2+it) \ll t^{1/4+\varepsilon}$) |
| Proposition 4.2 / 101.B (Condition 9) | Unconditional modulo V.1; **CAP-style**, not a lever |
| RV and BRS statements (§1) | Verified against sources; conditionality precisely delimited (BRS Thm 1.1 unconditional; "non-redundant real nodes" reading conditional on RH + simplicity) |
| Kulikov's density constant; exact coverage of $L_{DH}$ by BRS §5.3 | [NOT VERIFIED], marked in the text; no conclusion depends on it |
| Dichotomy 8.1 / 101.C | Argued synthesis over the cited corpus; not a formal theorem — it is a pattern with no known counterexample in RV/BRS/KNS/KS |
| Gap G.101.1 ($\widehat{\nu} \in \mathcal{H}_1$) | Declared, not resolved |
| No proof of RH, no progress on $d\nu = 0$ | Correct: the document closes a route, it does not open one |

## References

**Literature (verified, except as marked):**
- D. Radchenko, M. Viazovska, *Fourier interpolation on the real line*, Publ. Math. IHÉS **129** (2019), 51–81. [Statement verified via the BRS text and numdam.]
- A. Bondarenko, D. Radchenko, K. Seip, *Fourier interpolation with zeros of zeta and L-functions*, Constr. Approx. (2023); arXiv:2005.02996v3. [Theorem 1.1, Corollary 1.1, eqs. (1.1)–(1.7), §4.4: verified directly against the PDF.]
- A. Kulikov, *Fourier interpolation and time-frequency localization*, arXiv:2005.12836. [Qualitative content verified via BRS; exact constant NOT VERIFIED.]
- A. Kulikov, F. Nazarov, M. Sodin, *Fourier uniqueness and non-uniqueness pairs*, J. Math. Phys. Anal. Geom. (2023); arXiv:2306.14013. [Super/subcritical dichotomy verified at the abstract level.]
- H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, *Universal optimality of the E8 and Leech lattices and interpolation formulas*, Ann. of Math. **196** (2022). [Context; not re-verified in detail.]
- P. Kurasov, P. Sarnak, *The arithmetic of Lee–Yang/Fourier quasicrystals*, arXiv:2307.13498. [Via NOVEL-STRUCTURE-SEARCH.]
- Beurling–Malliavin (1962); Korevaar (2004); Seip (2004): classical completeness/density theory, cited as in Doc 85.

**Program:** Docs 70, 71, 72, 76, 82, 83, 85, 89; P39; meta-docs DISCRIMINATOR-hardening-phase-A (criteria I1/I2a/I2b/I3/I4), NOVEL-STRUCTURE-SEARCH-survivors (destruction of Kurasov–Sarnak; open point on interpolation, resolved here).

---

*End of Document 101. The dual theory of quasicrystals has been audited: the wall is the same and duality leaves it invariant. ROUTE CLOSED, with two unconditional byproducts and two declared gaps.*
