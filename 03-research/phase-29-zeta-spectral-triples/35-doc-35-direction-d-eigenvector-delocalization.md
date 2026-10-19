# Phase 29 — Doc 35: Direction D — Eigenvector Delocalization and the Szegő Theorem

**Direction:** D (eigenvector delocalization via orthogonal polynomial theory and Szegő)
**Objective:** Inc. Inv. is equivalent to uniform delocalization of the eigenvectors of $J_\infty$ (Doc 22): $|c_n|^2 = 1/N$ for all $n$. Investigate whether Szegő theory for Jacobi operators implies this delocalization for the CCM operator $J_\infty = D + P$.

---

## 1. Delocalization as a reformulation of Inc. Inv.

**Reminder (Doc 22, Proposition 8).** Let $\{\psi_n\}_{n\geq 1}$ be the eigenvectors of $J_\infty$ corresponding to the eigenvalues $\{\tilde\gamma_n\}$, normalized. The delocalization weights are $c_n := \langle e_0, \psi_n\rangle$ (component along the cyclic vector $e_0$).

**Proposition 1** (delocalization—Inc. Inv. equivalence, Doc 22). The following are equivalent:

(i) $|c_n|^2 = 1/N$ for all $n = 1, \ldots, N$ (uniform delocalization).

(ii) $m_\infty^{WT}(z) = m_\infty^{emp}(z)$ (the WT and empirical functions coincide).

(iii) Inc. Inv.: $\tilde\gamma_n = \gamma_n$ for all $n$ AND the weights are equal.

*Proof.* $m^{WT}(z) = \sum_n |c_n|^2/(z-\tilde\gamma_n)$ and $m^{emp}(z) = (1/N)\sum_n 1/(z-\gamma_n)$. If $\tilde\gamma_n = \gamma_n$ and $|c_n|^2 = 1/N$: the two functions coincide. The reverse direction: by uniqueness of the Stieltjes representation. $\square$

**Simplification.** If we already know (from Doc 31, Theorem 2) that $\tilde\gamma_n = \gamma_n + O(1/(n\log^2 n))$ (small perturbation), the delocalization question reduces to: do the weights satisfy $|c_n|^2 = 1/N$ when the eigenvalues are exponentially close to the $\gamma_n$?

---

## 2. Orthogonal polynomials and their norms

**Definition.** Let $\{P_n\}_{n\geq 0}$ be the orthogonal polynomials with respect to the spectral measure $\mu_\infty^{WT}$ of $J_\infty$:

$$\int P_n(t) P_m(t) \, d\mu_\infty^{WT}(t) = \delta_{nm}, \quad P_n(t) = k_n t^n + \ldots, \; k_n > 0.$$

The Jacobi coefficients of $J_\infty$ are related by:

$$b_n = \frac{\langle t P_n, P_n\rangle}{1} = \int t P_n(t)^2 \, d\mu_\infty^{WT}(t), \quad a_n^2 = \frac{k_n}{k_{n+1}} \cdot \frac{1}{\|P_n\|^2}.$$

**The delocalization weight.** The component $c_n$ of the eigenvector $\psi_n$ along $e_0$ satisfies:

$$|c_n|^2 = \mu_\infty^{WT}(\{\tilde\gamma_n\}) = \frac{1}{k_{n_0}^2 \|P_{n_0}\|^{-2}} = \frac{1}{|P_{n_0}'(\tilde\gamma_n)|^2 \|P_{n_0}\|^2},$$

where the first expression uses the standard relation between the spectral measure and the orthogonal polynomials.

In more concrete terms: $|c_n|^2 = 1/\sum_k P_k(\tilde\gamma_n)^2$ (by the resolution of the identity).

**Uniform delocalization.** $|c_n|^2 = 1/N$ iff $\sum_k P_k(\tilde\gamma_n)^2 = N$ for all $n$. As $N \to \infty$: this says that the orthogonal polynomials evaluated at the eigenvalues have equal norms — an "equidistribution" condition of the $P_k$ at the points $\tilde\gamma_n$.

---

## 3. The Szegő theorem for measures on the real line

**The classical Szegő theorem (1920).** Let $\mu$ be a measure on $[-1,1]$, absolutely continuous with density $w(x) = d\mu/dx > 0$ almost everywhere. Let $k_n$ be the leading coefficient of the $n$-th orthogonal polynomial. Then:

$$\lim_{n\to\infty} k_n^{-2} = \exp\!\left\{\frac{1}{2\pi}\int_{-1}^1 \frac{\log w(x)}{\sqrt{1-x^2}}\,dx\right\} > 0,$$

if and only if the Szegő condition $\int \log w(x)/\sqrt{1-x^2}\,dx > -\infty$ holds. If the condition fails: $k_n^{-2} \to 0$, that is, $k_n \to \infty$ ("the polynomials are large").

**Version for the real line (Krein, 1945).** For measures $\mu$ on $\mathbb{R}$ with unbounded support: the generalized Szegő condition takes the form of the decay of the coefficients of the Blaschke product on the upper half-plane.

**The Szegő condition for $\mu_\infty^{WT}$.** The measure $\mu_\infty^{WT}$ of $J_\infty$ is the spectral measure of the Jacobi operator with coefficients $(b_n, a_n) = (\gamma_n, \pi/\log\gamma_n)$.

For a Jacobi operator with coefficients $(b_n, a_n)$: Szegő theory (in the Simon-Steklov version) relates the asymptotic properties of the polynomials to the asymptotic properties of the coefficients. Specifically (Simon, 2004):

$$\text{Szegő} \iff \sum_n (b_n - b_n^{(0)})^2 + (a_n - a_n^{(0)})^2 < \infty,$$

where $(b_n^{(0)}, a_n^{(0)})$ are the coefficients of a "free" reference operator.

---

## 4. The reference operator for $J_\infty$

**The natural free operator.** The operator $J_\infty = D + P$ has diagonal coefficients $b_n = \gamma_n$ (free part) and perturbation $P$ with coefficients $a_n = \pi/\log\gamma_n$. The natural reference operator is the diagonal operator $D = \text{diag}(\gamma_n)$.

**The diagonal operator $D$.** For the PURELY DIAGONAL operator $D = \text{diag}(\gamma_n)$: the eigenvalues are exactly $\gamma_n$ and the eigenvectors are $\{e_n\}$ (the canonical basis). In this case: $\langle e_0, e_n\rangle = \delta_{n0}$ — the eigenvector $e_0$ has component $c_0 = 1$ in the eigenvector $e_0$ (eigenvalue $\gamma_0$) and $c_n = 0$ for $n \geq 1$. That is, $D$ is MAXIMALLY LOCALIZED at $e_0$.

This is the opposite of delocalization: in the free operator $D$, all the weight is at $n=0$, not distributed uniformly.

**The role of the perturbation $P$.** The perturbation $P$ (with coefficients $a_n = \pi/\log\gamma_n$) is what "mixes" the eigenvalues and produces delocalization. The strength of the delocalization depends on the size of $P$: $\|P\|_{op} \leq 2\pi/\log\gamma_0 \approx 2.36$.

**Proposition 2** (the Szegő condition for $J_\infty$ vs $D$). The deviation of the coefficients of $J_\infty$ from the reference operator $D$ is:

$$\sum_n (b_n - b_n^{(D)})^2 + (a_n - a_n^{(D)})^2 = \sum_n 0^2 + \left(\frac{\pi}{\log\gamma_n}\right)^2 = \pi^2\sum_n \frac{1}{(\log\gamma_n)^2}.$$

This series DIVERGES (since $\log\gamma_n \sim \log n + \log\log n$ and $\sum 1/(\log n)^2$ diverges).

**Conclusion.** The Szegő condition (finiteness of the sum of squares) is NOT satisfied for $J_\infty$ relative to the diagonal operator $D$. The Szegő theorem (in the finite-perturbation form) does not apply directly.

---

## 5. Szegő theory "at logarithmic scale"

**Modified reference operator.** Instead of comparing with $D$, we compare with a quasi-free Jacobi operator $D^{(0)}$ with:

$$b_n^{(0)} = \gamma_n, \quad a_n^{(0)} = \frac{\pi}{\log\gamma_n}.$$

This is the operator $J_\infty$ itself. Trivially: $J_\infty = D^{(0)}$, and the "perturbation" is zero.

The Szegő theorem in this context would say something about the norms of the orthogonal polynomials with respect to $\mu_\infty^{WT}$ compared to the orthogonal polynomials of $D^{(0)}$.

**The problem.** The operator $D^{(0)} = J_\infty$ has a known spectrum (the eigenvalues $\tilde\gamma_n$), but the WEIGHTS $|c_n|^2$ are what we want to determine. The Szegő theorem does not apply to itself: we need ANOTHER operator as a reference.

---

## 6. The Szegő theorem for Jacobi operators with growing coefficients

**OPRL theory with unbounded coefficients.** For Jacobi operators with $b_n \to \infty$ (as $J_\infty$ with $b_n = \gamma_n \to \infty$): classical Szegő theory does not apply (it is designed for bounded coefficients). One needs the theory of "varying-weight orthogonal polynomials" or Szegő theory for growing Jacobi operators.

**Generalized Szegő theorem (Lubinsky-Saff, 1988; Levin-Lubinsky, 2008).** For measures $\mu$ with density decaying like $w(x) \sim e^{-Q(x)}$ for a function $Q(x) \to \infty$: the orthogonal polynomials satisfy:

$$k_n(a_n^{(Q)})^n \to 1,$$

where $a_n^{(Q)}$ is the "external equilibrium" radius of the function $Q$. This result controls the NORMS of the polynomials but not their VALUES at individual points.

**Tentative application to $\mu_\infty^{WT}$.** The measure $\mu_\infty^{WT}$ has discrete support $\{\tilde\gamma_n\}$ — it is not absolutely continuous. For DISCRETE measures: the orthogonal polynomials satisfy the three-term recurrence, but generalized Szegő theory does not apply directly to discrete measures with unbounded support.

---

## 7. The Weyl equidistribution argument

**The observation.** The coefficients of the operator $J_\infty$ satisfy $a_n = \pi/\log\gamma_n$ and $b_n = \gamma_n$. The perturbation $P$ has entries:

$$P_{n,n+1} = P_{n+1,n} = a_n = \frac{\pi}{\log\gamma_n}.$$

For delocalization, we need the eigenvectors of $J_\infty = D + P$ to "mix" the components of $D$.

**Weyl equidistribution.** By Weyl's equidistribution theorem: if $\{\log\gamma_n \cdot t \mod 2\pi\}$ is equidistributed on $[0,2\pi]$ for every irrational $t$, then the sums $\sum_n f(\gamma_n)\cos(t\log\gamma_n)$ average to zero — a form of "incoherence" between the modes of the eigenvector.

**Incoherence and delocalization.** A delocalized eigenvector $\psi_n$ of $J_\infty = D + P$ satisfies:

$$\psi_n = e_n + \sum_{k \neq n} \frac{P_{kn}}{\gamma_n - \gamma_k} e_k + O(\|P\|^2).$$

The first-order perturbation coefficients:

$$\langle e_0, \psi_n\rangle = \frac{P_{0n}}{\gamma_n - \gamma_0} + O(\|P\|^2) = \frac{a_0}{\gamma_n - \gamma_0} + O(\|P\|^2).$$

For large $n$: $|c_n|^2 \approx a_0^2/(\gamma_n-\gamma_0)^2 = (\pi/\log\gamma_0)^2/\gamma_n^2 \to 0$.

This is NOT $1/N$: the weights decay to 0 for large $n$ at first order in perturbation theory.

**The problem with the standard perturbation.** At first order, the weights $|c_n|^2 \sim \pi^2/(\gamma_n^2\log^2\gamma_0)$ decay to zero with $n$. For $|c_n|^2 = 1/N$ (uniformly): the higher orders of the perturbation must CANCEL the first-order decay and produce a uniform weight.

This cancellation is the SAME problem as Inc. Inv.: it requires exactness at all orders of the perturbation.

---

## 8. An alternative approach: the resolvent matrix and the correlation function

**The projection operator.** Let $P^{>T} = \sum_{n: \gamma_n > T} |e_n\rangle\langle e_n|$ be the projector onto the complement of the first $N = N_\Xi(T)$ eigenvalues. Uniform delocalization is equivalent to:

$$\langle e_0, P^{>T} e_0\rangle = \sum_{n: \gamma_n > T} |c_n|^2 = 1 - \frac{N_\Xi(T)}{N}$$

for any truncation $T$.

**Parseval's identity.** $\sum_{n=0}^\infty |c_n|^2 = 1$ (orthogonality). Uniform delocalization requires:

$$\sum_{n=0}^{N_\Xi(T)-1} |c_n|^2 = \frac{N_\Xi(T)}{N} \quad \text{for all } T.$$

This says that the weights are "proportional to the count" — an equidistribution condition on the weights.

**The weight-counting function.** Define $W(T) := \sum_{n: \tilde\gamma_n \leq T} |c_n|^2 = \mu_\infty^{WT}([0,T])$. Uniform delocalization is equivalent to:

$$W(T) = \frac{N_{C_\infty}(T)}{N} \cdot 1 = \frac{N_\Xi(T)}{N}$$

(using that the eigenvalues of $J_\infty$ are the zeros of $C_\infty$, and assuming $N_{C_\infty}(T) = N_\Xi(T)$, which is Inc. Inv.).

Again: uniform delocalization is directly tied to Inc. Inv. — there is no independent path.

---

## 9. Simon's result on delocalization for Jacobi operators

**Simon's theorem (2003) on free-type orthogonal polynomials.** For Jacobi operators with $a_n \to 0$ and $b_n \to \infty$ (the regime of $J_\infty$ = "Freud" case): the eigenvectors satisfy a LOCALIZATION law, not delocalization. Specifically:

If $b_n \to \infty$ and $a_n/b_n \to 0$ (the case of our $J_\infty$ with $b_n = \gamma_n$ and $a_n = \pi/\log\gamma_n$): the eigenvectors concentrate LOCALLY near each eigenvalue, with $|c_n|^2 \to 0$ as $n \to \infty$.

*This is the OPPOSITE law to uniform delocalization.*

**Proposition 3** (localization of $J_\infty$, tentative). For the operator $J_\infty$ with $b_n = \gamma_n \to \infty$ and $a_n = \pi/\log\gamma_n \to 0$: in the regime $n \to \infty$, the eigenvectors satisfy:

$$|c_n|^2 = |\langle e_0, \psi_n\rangle|^2 \to 0.$$

*Tentative proof.* From the perturbative calculation (§7): at first order, $|c_n|^2 \approx a_0^2/\gamma_n^2 \to 0$. Higher-order corrections do not change the fact that $|c_n|^2 \to 0$ as $n \to \infty$. $\square$ (pending rigorous verification.)

**The tension with Inc. Inv.** If $|c_n|^2 \to 0$: uniform delocalization FAILS (since the weights are not constant). But Inc. Inv. is equivalent to uniform delocalization (Proposition 1). Does this refute Inc. Inv.?

---

## 10. Resolving the tension: the role of the factor $N$

**The subtle point.** "Uniform delocalization" $|c_n|^2 = 1/N$ involves the factor $N$ (the total number of eigenvalues). As $N \to \infty$: $1/N \to 0$. So $|c_n|^2 = 1/N \to 0$ is CONSISTENT with $|c_n|^2 \to 0$.

Delocalization says: all the $|c_n|^2$ are EQUAL (each equal to $1/N$). Localization says: the $|c_n|^2$ decay to 0 with $n$ (some are much smaller than the mean $1/N$).

**The precise condition.** For $n$ in the range $[0, N-1]$ (the first $N$ eigenvalues): delocalization requires $|c_n|^2 \approx 1/N$ uniformly. Localization says that for $n \sim N$: $|c_n|^2 \ll 1/N$.

**Proposition 4** (incompatibility with unbounded operator theory). For Jacobi operators with $b_n \to \infty$ and the structure of $J_\infty$: unbounded operator theory (Atkinson, 1964; Janas-Naboko, 1999) shows that the eigenvectors satisfy $|c_n|^2 \sim C/\gamma_n^\alpha$ for some $\alpha > 0$. This is $|c_n|^2 \sim 1/n^{(1+\alpha)\beta}$ with $\gamma_n \sim n\log n$ (by the von Mangoldt formula).

The mean: $\frac{1}{N}\sum_{n=0}^{N-1}|c_n|^2 = \frac{1}{N}\sum_{n=0}^{N-1}\frac{C}{\gamma_n^\alpha} \approx \frac{C}{N}\sum_{n=0}^N\frac{1}{(n\log n)^\alpha} \approx \frac{C}{N}\cdot\frac{N^{1-\alpha}}{(\log N)^\alpha}$.

For the mean to be $\approx 1/N$: one needs $C\cdot N^{1-\alpha}/(\log N)^\alpha \approx 1$, that is, $N^\alpha \approx C(\log N)^\alpha$, which fails for $\alpha > 0$.

**Tentative conclusion.** For Jacobi operators with the asymptotic behavior of $J_\infty$ ($b_n \sim n\log n$, $a_n \sim \pi/\log n$): the weight distribution is NOT uniform — the weights decay with $n$. This suggests that uniform delocalization ($|c_n|^2 = 1/N$) does NOT hold in general for $J_\infty$.

If this is correct: Inc. Inv. (= uniform delocalization) would NOT follow from the eigenvector behavior of a Jacobi operator with these coefficients. It would be a NEW OBSTACLE.

---

## 11. Candor: Direction D as an obstacle rather than a tool

**The surprising (and candid) result.** The delocalization analysis suggests that the operator $J_\infty$, with its specific coefficients $b_n = \gamma_n$ and $a_n = \pi/\log\gamma_n$, does NOT exhibit uniform delocalization in general. The eigenvectors of unbounded Jacobi operators are generally LOCALIZED (weights decaying with the index).

**The resolution (if one exists).** Inc. Inv. would hold ONLY IF the weights $|c_n|^2$ of $J_\infty$ are exactly $1/N$ — a SPECIAL condition that runs against the generic behavior of unbounded Jacobi operators. This could only happen if there is a deep structural reason (arithmetic or spectral) that FORCES the uniformity of the weights.

This structural reason, if it exists, would be connected to the ARITHMETIC of the zeros of $\zeta$ and not to generic properties of Jacobi operators.

**Corollary 4** (deeper reformulation of the wall). The analysis of Direction D suggests that Inc. Inv. is equivalent to a deep ARITHMETIC condition: the weights $|c_n|^2$ of the eigenvectors of $J_\infty$ are uniform iff the distribution of the zeros of $\zeta$ has an "equidistribution property" going beyond the simple von Mangoldt density.

This observation connects Inc. Inv. with Montgomery's conjectures on the pair correlation of zeros (Random Matrix Theory), where uniformity of the weights would be a consequence of the GUE structure of the zeros.

---

## 12. Conclusion of Direction D

**Positive result.** The formulation of Inc. Inv. as delocalization $|c_n|^2 = 1/N$ is correct and explicit. The condition has a clear interpretation in terms of the Weyl-Titchmarsh function.

**Negative result.** Szegő theory for unbounded Jacobi operators (the regime of $J_\infty$) predicts LOCALIZATION, not delocalization. This suggests that uniform delocalization is a SPECIAL condition, not a generic one.

**The deepened wall.** Inc. Inv. requires the eigenvectors of $J_\infty$ to be uniformly delocalized — a condition that would be violated in the generic regime of unbounded Jacobi operators. The only reason it could hold is the specific ARITHMETIC STRUCTURE of the coefficients $b_n = \gamma_n$ (zeros of $\zeta$) and $a_n = \pi/\log\gamma_n$ (spacings of the zeros).

**Connection with RMT.** If the zeros of $\zeta$ have the correlations predicted by GUE (Montgomery's conjecture), then the eigenvalues of $J_\infty$ have the spectral structure of a random unitary matrix — and in that regime, the eigenvectors ARE uniformly delocalized (eigenvector delocalization conjecture for random matrices). Proving Inc. Inv. from this perspective would require going through Montgomery's conjecture, which is open.

---

*End of the Phase 30 documents. Summary in Doc 36.*
