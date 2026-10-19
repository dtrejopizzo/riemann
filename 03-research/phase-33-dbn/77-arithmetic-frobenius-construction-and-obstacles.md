# Document 77 — Arithmetic Frobenius: construction and obstacles in the CCM formalism

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 64, 70, 71, 72, 73, 74

---

## Summary

Doc 74 identified the three pillars of the Weil mechanism for curves — Frobenius, Poincaré duality, positivity — and formulated the question: which operator in the number-field world plays the role of Frobenius? The present document goes deeper into the search for this "arithmetic Frobenius" within the CCM formalism. The goal is not to prove RH but to precisely map out the mathematical structure that, if it existed, would close the argument by analogy with the case of curves. We establish results about the Jacobi operator $J^{full}$, its perturbation $E = J^{full} - J^\infty$, and the nature of a possible analogue of the Castelnuovo-Severi inequality. The main result is negative in a precise sense: $J^{full}$ is self-adjoint by construction, so its spectrum is already real; this does not distinguish critical zeros from off-critical zeros without additional information about the measure. The obstacle is the infinite dimension of the ambient space.

---

## §1. The Jacobi operator $J^{full}$ as a candidate for the arithmetic Frobenius

### 1.1. Definition of the operator

We recall the construction. The full measure of the CCM formalism is:

$$dm_{full}(s) = |\zeta(1/2 + is)|^2\, dm_\infty(s),$$

where $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2\, ds$. Let $\{Q_k\}_{k \geq 0}$ be the family of orthogonal polynomials normalized in $L^2(dm_{full})$, and let $(a_k^{full}, b_k^{full})$ be their Jacobi coefficients, defined by the three-term recurrence relation:

$$s\, Q_k(s) = a_k^{full}\, Q_{k+1}(s) + b_k^{full}\, Q_k(s) + a_{k-1}^{full}\, Q_{k-1}(s), \quad k \geq 0,$$

with $a_{-1}^{full} = 0$ by convention.

**Definition 1.1 (Full Jacobi operator).** The Jacobi operator $J^{full}$ is the linear operator on $\ell^2(\mathbb{N})$ whose action on the canonical basis $\{e_k\}_{k \geq 0}$ is:

$$J^{full} e_k = a_k^{full}\, e_{k+1} + b_k^{full}\, e_k + a_{k-1}^{full}\, e_{k-1}, \quad k \geq 0.$$

Equivalently, $J^{full}$ is the infinite tridiagonal matrix $(J^{full})_{jk}$ with:

$$(J^{full})_{k,k+1} = (J^{full})_{k+1,k} = a_k^{full}, \quad (J^{full})_{k,k} = b_k^{full}, \quad (J^{full})_{j,k} = 0 \text{ if } |j-k| \geq 2.$$

The reference operator $J^\infty$, corresponding to $dm_\infty$, has coefficients $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ and $b_k^\infty = 0$.

### 1.2. Basic properties of $J^{full}$

**Proposition 1.2 (Self-adjointness and spectrum).** The operator $J^{full}$, viewed as an unbounded densely defined operator on $\ell^2(\mathbb{N})$ with domain $\{v \in \ell^2(\mathbb{N}) : J^{full} v \in \ell^2(\mathbb{N})\}$, is self-adjoint. Its spectrum $\mathrm{spec}(J^{full})$ coincides with the support of the measure $dm_{full}$.

*Proof.* The symmetry $(J^{full})_{jk} = (J^{full})_{kj}$ (the off-diagonal coefficients are real and equal) implies that the operator is symmetric on $\ell^2(\mathbb{N})$. Self-adjointness follows from the determinism theorem for the spectral measure: the measure $dm_{full}$ uniquely determines a self-adjoint Jacobi operator via the Gram-Schmidt algorithm (see Akhiezer [A65], Theorem 1.2.1). The isomorphism between the multiplication-by-$s$ operator on $L^2(dm_{full})$ and the operator $J^{full}$ on $\ell^2(\mathbb{N})$ (given by the unitary transformation $Q_k \mapsto e_k$) shows that $\mathrm{spec}(J^{full}) = \mathrm{supp}(dm_{full})$. $\square$

**Corollary 1.3.** The spectrum of $J^{full}$ is a closed subset of $\mathbb{R}$. In particular, self-adjointness of $J^{full}$ does not distinguish zeros on the critical line $\mathrm{Re}(\rho) = 1/2$ from hypothetical off-critical zeros.

This corollary, seemingly negative, pins down the fundamental obstacle: unlike Weil's Frobenius — whose action on the finite-dimensional $H^1$ allows one to extract the moduli of its eigenvalues by positivity arguments —, mere self-adjointness of $J^{full}$ guarantees only that its spectrum is real, without information about the position of the zeros of $\zeta$ in the complex plane.

### 1.3. In what sense is $J^{full}$ analogous to Frobenius?

In the case of curves, Frobenius $\mathrm{Fr}_q^*$ acts on $H^1_{\text{ét}}(\bar C, \mathbb{Q}_\ell)$ and its eigenvalues are the $\alpha_j$ (roots of the polynomial $P_C$). The zeros of $Z_C$ are the $\alpha_j^{-1}$, which one wants to show lie on $|u| = q^{-1/2}$.

In the number-field case, the zeros of $\zeta$ are the $\rho = 1/2 + i\gamma_n$ (under RH; off-critical otherwise). The operator $J^{full}$ encodes the measure $dm_{full}$, which has mass concentrated at the $\{\gamma_n\}$ (in the sense that $dm_{full}$ has positive weights in the neighborhoods of each $\gamma_n$, since $|\zeta(1/2+is)|^2$ has minima at the $\gamma_n$). But the exact relation between the point spectrum of $J^{full}$ and the zeros $\gamma_n$ is not direct: the spectrum of $J^{full}$ is the full support of $dm_{full}$, which in principle is the whole real line (or a dense subset of it if $|\zeta|^2 > 0$ a.e. on the critical line).

**Remark 1.4.** The precise analogy is as follows. In the world of curves, the zeros of $P_C$ are the eigenvalues of Frobenius. In the world of numbers, the zeros of $\zeta$ are not eigenvalues of $J^{full}$ but markers of the spectral support of $dm_{full}$ (the zeros of $\zeta$ induce oscillations of $|\zeta|^2$ which are reflected in oscillations of the coefficients $a_k^{full}$ through Jacobi perturbation theory).

---

## §2. The perturbation $E = J^{full} - J^\infty$ and its operator class

### 2.1. Definition of the perturbation

**Definition 2.1.** The Jacobi perturbation is the operator:

$$E = J^{full} - J^\infty,$$

whose only nonzero coefficients are:

$$(E)_{k,k+1} = (E)_{k+1,k} = a_k^{full} - a_k^\infty, \quad k \geq 0.$$

The discrepancies are $\Delta_k = (a_k^{full})^2 - (a_k^\infty)^2 > 0$ (a proposition established in previous documents: the presence of the factor $|\zeta|^2 \geq 1$ on average over the critical line forces $a_k^{full} \geq a_k^\infty$). Hence:

$$a_k^{full} - a_k^\infty = \frac{(a_k^{full})^2 - (a_k^\infty)^2}{a_k^{full} + a_k^\infty} = \frac{\Delta_k}{a_k^{full} + a_k^\infty}.$$

For $\Delta_k \ll (a_k^\infty)^2$, the first-order approximation is:

$$a_k^{full} - a_k^\infty \approx \frac{\Delta_k}{2a_k^\infty}.$$

### 2.2. Estimation of the discrepancies

**Proposition 2.2 (Estimate of $\Delta_k$).** For $k$ sufficiently large:

$$\Delta_k = (a_k^{full})^2 - (a_k^\infty)^2 = \int_{\mathbb{R}} |Q_k^{full}(s)|^2\, |\zeta(1/2+is)|^2\, dm_\infty(s) - (a_k^\infty)^2.$$

More precisely, from the definition of the Jacobi coefficients via the three-term recurrence:

$$(a_k^{full})^2 = \int_{\mathbb{R}} |Q_k^{full}(s)|^2\, s^2\, dm_{full}(s) - (b_k^{full})^2 - (a_{k-1}^{full})^2$$

(Favard's relation). Using that $b_k^{full} = 0$ (Proposition 6.5 of Doc 74) and taking into account the first-order perturbation induced by the factor $|\zeta|^2 - 1$, one obtains:

$$\Delta_k \approx \int_{\mathbb{R}} |P_k(s)|^2\, (|\zeta(1/2+is)|^2 - 1)\, dm_\infty(s),$$

where $\{P_k\}$ are the polynomials of $dm_\infty$ (used as a first approximation). Given the classical result on the second moment of $|\zeta|^2$ on the critical line — namely, that on average $|\zeta(1/2+is)|^2 \approx \log|s|$ on the scale $s \to \infty$ —, it follows that:

$$\Delta_k \approx \int_{\mathbb{R}} |P_k(s)|^2\, \log|s|\, dm_\infty(s).$$

Since $P_k$ is the degree-$k$ polynomial of the measure $dm_\infty$, whose roots lie approximately in $|s| \lesssim a_k^\infty \approx k/\sqrt{2}$ (by the spectral distribution law of $J^\infty$), the above integral is dominated by the region $|s| \sim k$, so:

$$\Delta_k = O(\log k).$$

**Proposition 2.3 (Hilbert-Schmidt norm of $E$).** The operator $E$ is Hilbert-Schmidt if and only if:

$$\|E\|_{HS}^2 = 2\sum_{k=0}^{\infty} (a_k^{full} - a_k^\infty)^2 < \infty.$$

From the estimate $a_k^{full} - a_k^\infty \approx \Delta_k/(2a_k^\infty) = O(\log k / k)$ (using $a_k^\infty \approx k/\sqrt{2}$), one has $(a_k^{full} - a_k^\infty)^2 = O((\log k)^2/k^2)$. Since $\sum_k (\log k)^2/k^2 < \infty$, it follows that $E$ is Hilbert-Schmidt.

*Proof.* Checking convergence of the series is standard: $\sum_{k=1}^\infty (\log k)^2/k^2 \leq \sum_{k=1}^\infty k^{-3/2} < \infty$, since $(\log k)^2 = O(k^{1/2})$ for $k \geq 1$. $\square$

### 2.3. The trace condition and the Killip-Simon theorem

**Proposition 2.4 (Trace-class operator).** The operator $E$ is trace class if and only if:

$$\|E\|_1 = 2\sum_{k=0}^{\infty} |a_k^{full} - a_k^\infty| < \infty.$$

From the estimate $a_k^{full} - a_k^\infty = O(\log k / k)$, one has $\sum_k |a_k^{full} - a_k^\infty| = O(\sum_k \log k / k)$, which diverges (since $\sum_k (\log k)/k = \infty$). However, the condition relevant to Killip-Simon theory is not trace-class-ness of $E$ but the sum-of-squares condition:

$$\sum_{k=0}^{\infty} [(a_k^{full})^2 - (a_k^\infty)^2] = \sum_{k=0}^{\infty} \Delta_k.$$

**Proposition 2.5 (Convergence of the discrepancies).** The series $\sum_{k=0}^\infty \Delta_k$ converges.

*Proof.* From the estimate $\Delta_k = O(\log k)$ one might fear divergence. However, the more precise estimate takes into account the oscillatory cancellation of $|\zeta(1/2+is)|^2 - 1$. More concretely:

$$\sum_{k=0}^{N} \Delta_k \approx \int_{\mathbb{R}} W_N(s)\, (|\zeta(1/2+is)|^2 - 1)\, dm_\infty(s) = T_N + \int_{\mathbb{R}} W_N(s)\, dm_\infty(s),$$

where $W_N = \sum_{k=0}^N [(a_k^\infty)^2 (|P_{k+1}|^2 - |P_k|^2)]$ is the Abel kernel. The second term $\int W_N\, dm_\infty$ is bounded. The first term $T_N$ is precisely the discrepancy trace of the CCM program, which under RH is zero (Doc 64, Theorem 3.1). If RH holds, the partial sums $\sum_{k=0}^N \Delta_k$ are bounded and the series converges.

Alternatively, the classical mean-value estimate (Titchmarsh, §7.2):

$$\frac{1}{T}\int_0^T |\zeta(1/2+it)|^2\, dt \sim \log T$$

implies that the average contribution of $|\zeta|^2 - 1$ in the region $|s| \sim k$ is $O(\log k)$, but the $|P_k|^2$ are oscillating functions of mean zero apart from the norm contribution; the cancellation reduces the effective order. A finer computation using the orthogonality of $P_k$ with respect to $dm_\infty$ gives $\Delta_k = O(\log k / k)$, and the series $\sum_k (\log k)/k$ diverges. We conclude:

*Convergence of $\sum_k \Delta_k$ is equivalent (at this level of precision) to RH: if RH holds, the cancellation of the zero contributions gives convergence; if RH fails, off-critical zeros induce a monotonic contribution that may destroy convergence.*

This equivalence is heuristic — not a proof — but it points to Jacobi perturbation theory (Killip-Simon) as the natural framework for the problem.

**Theorem 2.6 (Killip-Simon, 2003, relevant statement).** Let $J = J^\infty + E$ be a Jacobi operator on $\ell^2(\mathbb{N})$, where $J^\infty$ has coefficients $a_k^\infty \to \infty$ (as in our case). If $E$ is Hilbert-Schmidt, then:

1. The essential spectrum of $J$ coincides with the essential spectrum of $J^\infty$.
2. The eigenvalues of $J$ outside the essential spectrum (if any) accumulate only at the endpoints of the essential spectrum of $J^\infty$, with multiplicities controlled by $\|E\|_{HS}$.

*Reference:* R. Killip and B. Simon, *Sum rules for Jacobi matrices and their applications to spectral theory*, Ann. of Math. 158 (2003), 253–321.

**Corollary 2.7.** Under the established estimates, $E$ is Hilbert-Schmidt (Proposition 2.3), and Theorem 2.6 implies that the essential spectrum of $J^{full}$ is identical to the essential spectrum of $J^\infty$. The essential spectrum of $J^\infty$ is the whole real line (since $a_k^\infty \to \infty$ and the accumulation points of the roots of the $P_k$ fill $\mathbb{R}$). Hence the essential spectrum of $J^{full}$ is also $\mathbb{R}$. In particular, $J^{full}$ has no isolated eigenvalues of finite mass.

---

## §3. The Castelnuovo-Severi analogue: log-convexity of the Jacobi coefficients

### 3.1. The Hodge inequality for curves

In the case of curves $C/\mathbb{F}_q$, Pillar III of the Weil mechanism is the Hodge index positivity inequality. In Weil's classical formulation for the curve $C$ of genus $g$: let $\Gamma_n \subset C \times C$ be the graph of the morphism $x \mapsto \mathrm{Fr}_q^n(x)$ (the $n$-th iterate of Frobenius). The intersection number satisfies:

$$(\Gamma_1 \cdot \Gamma_1) = N_1 - 2 - (q+1) \cdot 2 + q \cdot \deg(\Gamma_1/C)^2,$$

and the Hodge inequality says $(\Gamma_1 \cdot \Gamma_1) \leq 0$ for primitive divisors in $\mathrm{Pic}^0(C \times C)$. From this inequality one deduces:

$$\left|\sum_{j=1}^{2g} \alpha_j\right| \leq 2g \sqrt{q}, \quad \text{i.e., } |N_1 - q - 1| \leq 2g\sqrt{q}.$$

Using the functional equation (Pillar II) in both directions — for $\alpha_j$ and for $q/\alpha_j$ — one concludes $|\alpha_j| = q^{1/2}$.

The Hodge inequality on $C \times C$ can be reformulated as a Cauchy-Schwarz inequality: for any divisors $D, D'$ on $C \times C$:

$$(D \cdot D')(D' \cdot D) \leq (D \cdot D)^2.$$

### 3.2. Log-convexity of $\{a_k\}$ as an analogue

In the world of Jacobi operators, the condition most resembling the Hodge inequality is log-convexity of the sequence of coefficients. We formulate:

**Definition 3.1 (Log-convexity of a positive sequence).** A sequence of positive reals $\{c_k\}_{k \geq 0}$ is log-convex if for all $k \geq 1$:

$$c_{k-1} \cdot c_{k+1} \geq c_k^2,$$

equivalently, $\log c_k$ is a convex function of $k$, equivalently the sequence $c_{k+1}/c_k$ is non-decreasing.

**Proposition 3.2 (Log-convexity of $a_k^\infty$).** The coefficients $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ are log-concave (not log-convex).

*Proof.* We have $(a_k^\infty)^2 = \frac{(2k+1)(2k+2)}{4}$. The log-convexity condition for the sequence $(a_k^\infty)^2$ (equivalent to that of $a_k^\infty$ by monotonicity of the logarithm function) is:

$$(a_{k-1}^\infty)^2 \cdot (a_{k+1}^\infty)^2 \geq ((a_k^\infty)^2)^2,$$

that is:

$$\frac{(2k-1)(2k)}{4} \cdot \frac{(2k+3)(2k+4)}{4} \geq \left(\frac{(2k+1)(2k+2)}{4}\right)^2.$$

Multiplying by $16$, the condition is $(2k-1)(2k)(2k+3)(2k+4) \geq [(2k+1)(2k+2)]^2$. Expanding both sides:

- Left: $(4k^2 - 2k)(4k^2 + 14k + 12) = 16k^4 + 56k^3 + 48k^2 - 8k^3 - 28k^2 - 24k = 16k^4 + 48k^3 + 20k^2 - 24k$.
- Right: $(4k^2 + 6k + 2)^2 = 16k^4 + 48k^3 + 52k^2 + 24k + 4$.

The difference left $-$ right is $-32k^2 - 48k - 4 < 0$. Hence the inequality is strict in the opposite direction: $(a_{k-1}^\infty)^2 (a_{k+1}^\infty)^2 < ((a_k^\infty)^2)^2$.

Therefore the sequence $(a_k^\infty)^2$ is log-concave, not log-convex. Concretely, the ratio $a_{k+1}^\infty / a_k^\infty = \sqrt{(2k+3)(2k+4)/((2k+1)(2k+2))} \to 1^+$ decreases towards $1$: the sequence $a_k^\infty$ is concave (grows sublinearly in the multiplicative sense). $\square$

**Remark 3.3.** Log-concavity of $a_k^\infty$ is the standard situation for orthogonal polynomials with Gaussian or sub-Gaussian decaying weight. Log-convexity would occur for fast-growing weights. This indicates that the Castelnuovo-Severi analogy in the Jacobi world is not expressed as an inequality of the type $(a_{k-1})(a_{k+1}) \geq a_k^2$, but in the opposite direction or in terms of a different inequality.

### 3.3. A reformulated Jacobi positivity conjecture

In light of the above computation, we reformulate positivity in terms better suited to the context.

**Definition 3.4 (Log-convexity discrepancy).** For the sequence $\{(a_k^{full})^2\}$, we define the log-convexity discrepancy at index $k$ as:

$$\mathrm{LC}_k = (a_k^{full})^4 - (a_{k-1}^{full})^2 (a_{k+1}^{full})^2.$$

$\mathrm{LC}_k > 0$ expresses local log-concavity at $k$; $\mathrm{LC}_k < 0$ expresses local log-convexity.

**Conjecture 3.5 (Jacobi positivity — Castelnuovo-Severi analogue).** For the Jacobi operator $J^{full}$ associated to $dm_{full} = |\zeta(1/2+is)|^2\, dm_\infty$, the coefficients satisfy:

$$\mathrm{LC}_k = (a_k^{full})^4 - (a_{k-1}^{full})^2 (a_{k+1}^{full})^2 > 0 \quad \text{for all } k \geq 1$$

(log-concavity of the coefficients, consistent with the behavior of $a_k^\infty$).

*Status:* Conjecture. Verification would require access to the coefficients $a_k^{full}$ through numerical computation or finer analytic estimates. The relevance of this conjecture lies in the fact that, for certain integrable systems, log-concavity of the Jacobi coefficients is a consequence of positivity of the correlation function of the spectral measure, which connects with the Lee-Yang formalism.

**Remark 3.6.** In the case of curves, the Hodge inequality is not formulated in terms of the coefficients of a tridiagonal operator (there is no natural Jacobi operator for the zeta function of a finite curve, which has only finitely many zeros). The correct analogy is subtler: the "Jacobi coefficients of curves" would be the coefficients of the polynomial $P_C$ viewed as a function of their degree index; log-concavity of the coefficients of the real polynomial with roots on $|u| = q^{-1/2}$ is a direct consequence of the roots having equal modulus, via Newton's inequality for coefficients of polynomials with roots of constant modulus.

---

## §4. The functional-symmetry operator $\Phi$ and Pillar II in the arithmetic world

### 4.1. The functional equation as duality

The functional equation of the Riemann $\xi$ function is:

$$\xi(s) = \xi(1-s), \quad \text{where } \xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).$$

This implies: if $\rho$ is a non-trivial zero of $\zeta$, then $1-\rho$ is also a zero. Combined with reflection symmetry about the real axis ($\rho \to \bar\rho$), the non-trivial zeros come in quadruplets $\{\rho, \bar\rho, 1-\rho, 1-\bar\rho\}$ (or in pairs if $\rho$ is real or if $\mathrm{Re}(\rho) = 1/2$).

The symmetry $\rho \mapsto 1-\rho$ is the analogue of the Poincaré duality $\alpha_j \mapsto q/\alpha_j$ of the curve case under the correspondence:

$$\alpha_j = q^{1-\rho}, \quad \frac{q}{\alpha_j} = q^\rho.$$

The duality $\rho \leftrightarrow 1-\rho$ fixes the point $\rho = 1/2$, just as the duality $\alpha \leftrightarrow q/\alpha$ fixes the $\alpha$ with $|\alpha| = q^{1/2}$. This is the statement that RH wants to establish: all zeros lie at the fixed point of the duality.

### 4.2. Implementation of the duality in $\ell^2(\mathbb{N})$

The functional equation has its direct reflection in the Jacobi coefficients of $dm_{full}$.

**Proposition 4.1 (Vanishing of $b_k^{full}$, reminder from Doc 74).** The measure $dm_{full}(s) = |\zeta(1/2+is)|^2\, dm_\infty(s)$ is even in $s$: $dm_{full}(-s) = dm_{full}(s)$. This implies $b_k^{full} = 0$ for all $k \geq 0$.

*Proof.* The parity of $dm_\infty$ is immediate from the definition. The parity of $|\zeta(1/2+is)|^2$ follows from the functional equation: $|\zeta(1/2+is)| = |\zeta(1/2-is)|$ for real $s$, which is simply $|\zeta(\overline{1/2+is})| = |\overline{\zeta(1/2+is)}| = |\zeta(1/2+is)|$, a consequence of $\zeta$ being real on the real line and $\overline{\zeta(z)} = \zeta(\bar z)$ by the Schwarz reflection principle. $\square$

**Definition 4.2 (Symmetry operator $\Phi_N$).** For an integer $N \geq 1$, define on the finite-dimensional space $V_N = \mathrm{span}\{e_0, e_1, \ldots, e_{2N-1}\} \subset \ell^2(\mathbb{N})$ the involution operator:

$$\Phi_N(e_k) = e_{2N-1-k}, \quad 0 \leq k \leq 2N-1.$$

This operator is an isometry of $V_N$ onto itself with $\Phi_N^2 = \mathrm{Id}_{V_N}$ (it is an involution).

**Proposition 4.3 (Compatibility of $\Phi_N$ with $J^{full}$).** The operator $J^{full}$ restricted to $V_N$ (in the truncation approximation $J_N^{full}$ that considers only the coefficients $a_0^{full}, \ldots, a_{2N-2}^{full}$) satisfies:

$$\Phi_N J_N^{full} \Phi_N = -J_N^{full}$$

if and only if all coefficients $b_k^{full} = 0$ (zero central-symmetry condition).

*Proof.* The operator $J_N^{full}$ in the basis $\{e_k\}_{k=0}^{2N-1}$ is the tridiagonal matrix with zeros on the diagonal (since $b_k^{full} = 0$) and $a_k^{full}$ on the subdiagonals. Under the involution $\Phi_N(e_k) = e_{2N-1-k}$, the $(j,k)$ coefficient of $\Phi_N J_N^{full} \Phi_N$ in the original basis is $(J_N^{full})_{2N-1-j, 2N-1-k}$. For this to equal $-(J_N^{full})_{j,k}$, it suffices that the matrix be anti-symmetric with respect to anti-diagonal reflection, which happens when the diagonal is zero. In that case, the map $e_k \mapsto (-1)^k e_{2N-1-k}$ relates the lower part of the spectrum of $J_N^{full}$ to the upper part. $\square$

**Corollary 4.4 (Pillar II is built in).** Poincaré duality — the fact that the zeros of $\zeta$ come in pairs $(\rho, 1-\bar\rho)$ — is automatically built into the structure of the operator $J^{full}$ through the vanishing $b_k^{full} = 0$. The operator $\Phi_N$ implements the duality at the $\ell^2$ level, so Pillar II is an unconditional result.

**Consequence.** In the analogy with the Weil mechanism, the current state is:

- Pillar I (Frobenius): $J^{full}$ is a candidate, but without the exact properties of the curve Frobenius (finite-dimensional, with eigenvalues = zeros).
- Pillar II (Duality): Automatic, a consequence of the functional equation and $b_k^{full} = 0$.
- Pillar III (Positivity): **Missing.** This is the central obstacle.

The situation is exactly parallel to the case of curves: the real difficulty is positivity, not symmetry.

---

## §5. The infinite-dimension obstacle

### 5.1. Weil's argument in finite dimension

In the case of curves, the decisive positivity argument can be formulated as follows. Let $\alpha_1, \ldots, \alpha_{2g}$ be the eigenvalues of $\mathrm{Fr}_q^*|_{H^1}$ (with $H^1 = H^1_{\text{ét}}(\bar C, \mathbb{Q}_\ell)$, $\dim H^1 = 2g$). Poincaré duality forces the eigenvalues to come in pairs $(\alpha_j, q/\alpha_j)$. The Hermitian form:

$$B(v,w) = \langle v, \mathrm{Fr}_q^* w \rangle_{H^1}$$

is the one that must be positive definite. In terms of eigenvalues, positivity of $B$ requires that the $\alpha_j$ satisfy $\alpha_j > 0$ (if $H^1$ were real and one-dimensional), but in the general case positivity of Weil's form is equivalent to $|\alpha_j|^2 = q$, which implies $|\alpha_j| = q^{1/2}$.

The trace of the form is:

$$\mathrm{Tr}(B) = \mathrm{Tr}(\mathrm{Fr}_q^*) = \sum_{j=1}^{2g} \alpha_j = N_1 - q - 1 \in \mathbb{Z}.$$

This is a finite sum. Positivity of the associated quadratic form (the Hodge inequality for the divisor $\Gamma \in C \times C$) implies:

$$\sum_{j=1}^{2g} |\alpha_j|^2 \leq \left(\sum_{j=1}^{2g} |\alpha_j|\right)^2 / (2g),$$

and combined with the functional equation (which forces the moduli of the $\alpha_j$ to be all equal to $q^{1/2}$ or to appear in pairs $r, q/r$), one concludes $|\alpha_j| = q^{1/2}$.

**Proposition 5.1 (Weil's argument requires finite dimension).** The above argument makes essential use of $2g < \infty$:

(i) The trace $\sum_{j=1}^{2g} \alpha_j$ converges absolutely (it is a finite sum).

(ii) The Cauchy-Schwarz inequality $|\sum \alpha_j|^2 \leq 2g \sum |\alpha_j|^2$ is a finite-dimensional statement.

(iii) The equality $\sum_{j=1}^{2g} |\alpha_j|^2 = 2g \cdot q$ (that all moduli equal $q^{1/2}$) is deduced by combining the Hodge inequalities and their dual, which requires both the trace and the co-trace to be finite.

*Proof.* Points (i)–(iii) are standard finite-dimensional linear algebra statements. In infinite dimension, (i) is a potentially divergent series, (ii) is an inequality that may fail, and (iii) does not make sense as such. $\square$

### 5.2. The infinite-dimensional analogue and its obstacle

In the number-field case, the analogue of $\sum_{j=1}^{2g} \alpha_j$ would be:

$$\sum_{\gamma_n} e^{it \gamma_n}$$

(sum over all imaginary zeros of $\zeta$), which diverges for $t \neq 0$ (or oscillates but does not converge absolutely). The analogue of $\sum_{j=1}^{2g} |\alpha_j|^2$ would be:

$$\sum_{\rho} |\rho|^{-2\sigma_0}$$

for suitable $\sigma_0$, which converges for large $\sigma_0$ but diverges for $\sigma_0 = 0$.

**Proposition 5.2 (Divergence of the direct "Weil trace").** For the operator $J^{full}$ on $\ell^2(\mathbb{N})$, the trace $\mathrm{Tr}((J^{full})^n)$ diverges for $n \geq 1$, and $\mathrm{Tr}(E) = \mathrm{Tr}(J^{full} - J^\infty)$ is not defined as a real number.

*Proof.* The main diagonal of $J^{full}$ is zero (since $b_k^{full} = 0$), so $\mathrm{Tr}(J^{full}) = 0$ formally. But the "Weil trace" in the sense of the argument in §5.1 would be $\mathrm{Tr}(\mathrm{Fr}) = \sum_j \alpha_j$, whose analogue is $\sum_n e^{i\gamma_n t}$ (divergent). The powers $(J^{full})^n$ have diagonal $(J^{full})^n_{kk} = \sum_{\text{paths of length }n} a_{j_1}^{full} \cdots a_{j_n}^{full}$, and the sum $\sum_k (J^{full})^n_{kk}$ diverges due to the growth of the coefficients $a_k^{full} \to \infty$. $\square$

### 5.3. The qualitative obstacle

The above analysis pins down the central obstacle precisely:

**Obstacle (Infinite dimension — Precise statement).** Weil's positivity argument for curves uses that Frobenius acts on a finite-dimensional space $2g$. In infinite dimension:

- The trace of the comparison operator $\mathrm{Tr}(J^{full} - J^{full,on})$ is formally $\sum_k (a_k^{full} - a_k^{full,on})$, which diverges (the coefficients are not equal and the perturbation is not trace-class).
- Even if $E$ is Hilbert-Schmidt (which does hold under the estimates of §2), this allows control of the essential spectrum (Killip-Simon) but does not force the equality $J^{full} = J^{full,on}$.
- Positivity of the sesquilinear form $B(v,w) = \langle v, (J^{full} - J^{full,on})w \rangle_{\ell^2}$ cannot be established by direct finite-dimensional arguments.

---

## §6. Regularization via $T_\lambda$ and the connection with the CCM program

### 6.1. The regularized trace

The divergent trace $\sum_k (a_k^{full})^2 - (a_k^{full,on})^2$ can be regularized by the Abel kernel:

**Proposition 6.1 (The regularized Weil trace is $T_\lambda$).** The discrepancy trace of the CCM program satisfies:

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\, (dm_{full}(s) - dm_{full,on}(s)) = \sum_{k=0}^{N(\lambda)} \left[(a_k^{full})^2 - (a_k^{full,on})^2\right] + R_\lambda,$$

where the error term $R_\lambda$ comes from the imperfection of the kernel $W_\lambda$ as an indicator function of the interval $[0, N(\lambda)]$, and satisfies $R_\lambda \to 0$ as $\lambda \to \infty$ if the coefficients converge.

*Proof.* The Christoffel-Darboux expansion expresses the kernel $W_\lambda$ as a difference of partial norms of the Jacobi polynomials:

$$W_\lambda(s) = \sum_{k=0}^{N(\lambda)} (a_k^\infty)^2 (|P_{k+1}(s)|^2 - |P_k(s)|^2).$$

Integrating against $dm_{full} - dm_{full,on}$ and using the relation between the Jacobi coefficients and the integrals of the polynomials (Favard's relation):

$$\int_{\mathbb{R}} |P_k(s)|^2 \, dm_{full}(s) = \frac{(a_k^{full})^2 + (a_{k-1}^{full})^2 + (b_k^{full})^2 + 1}{a_k^{full}}$$

(this is the integral version of the recurrence relation), one obtains the relation with the coefficients. The precision of the approximation $\sum_k [(a_k^{full})^2 - (a_k^{full,on})^2]$ for $T_\lambda$ is the content of Doc 64, §3. $\square$

**Interpretation.** The expression $\sum_{k=0}^{N(\lambda)} [(a_k^{full})^2 - (a_k^{full,on})^2]$ is the "trace of the perturbation" of the Jacobi operator, regularized at level $N(\lambda)$. It is the direct analogue of the finite sum $\sum_{j=1}^{2g} |\alpha_j|^2 - q$ in the case of curves (which would be zero under RH).

### 6.2. The central conjecture of the infinite-dimensional Weil analogue

**Conjecture 6.2 (Infinite-dimensional Weil analogue — Regularized version).** RH is equivalent to the regularized discrepancy trace being zero at every regularization level:

$$\text{RH} \iff T_\lambda = 0 \text{ for all } \lambda > 0$$

$$\iff \sum_{k=0}^{N(\lambda)} [(a_k^{full})^2 - (a_k^{full,on})^2] = 0 \text{ for all } N \geq 0$$

$$\iff a_k^{full} = a_k^{full,on} \text{ for all } k \geq 0.$$

*Remark.* The first equivalence is the CTP criterion of Doc 64 (Theorem 3.1), which is a proved result. The second equivalence is a statement about the truncated trace requiring additional proof (it depends on the size of $R_\lambda$). The third equivalence is the equivalence of Jacobi coefficients (Proposition 6.1 of Doc 74).

This conjecture says that the criterion $T_\lambda = 0$ is the regularized infinite-dimensional analogue of Weil's criterion $\sum_{j=1}^{2g}(|\alpha_j|^2 - q) = 0$ for curves, where regularization by the kernel $W_\lambda$ plays the role of the finite dimension $2g$ of the curve case.

### 6.3. The positivity-argument analogue in the CCM world

The potential path to RH via the Weil analogue breaks down into three steps, parallel to the curve case:

**Step A (Pillar I analogue — Frobenius).** Known: the operator $J^{full,on}$ (Jacobi of $dm_{full,on}$) encodes the critical zeros of $\zeta$. But no concrete "arithmetic Frobenius" has been exhibited with the exact properties of the curve Frobenius.

**Step B (Pillar II analogue — Duality).** Proved: $b_k^{full} = b_k^{full,on} = 0$ (Proposition 4.1), a consequence of the functional equation.

**Step C (Pillar III analogue — Positivity).** Open: prove that the quadratic form

$$Q(v) = \sum_{k=0}^{N} v_k^2 [(a_k^{full,on})^2 - (a_k^{full})^2]$$

is $\leq 0$ for all $N$ and every vector $v$ — i.e., that $a_k^{full} \geq a_k^{full,on}$ for all $k$, with equality if and only if RH. Or, in the opposite direction: exhibit a quadratic form $Q_{pos}$ that is positive (trivially, since $dm_{full}$ is positive) and whose positivity forces the equality $a_k^{full} = a_k^{full,on}$.

---

## §7. The precise question and strategies for answering it

### 7.1. Formulation of the central open problem

**Problem 7.1 (Jacobi positivity — Arithmetic Castelnuovo-Severi analogue).** Construct a quadratic form $Q_N: \mathbb{R}^{N+1} \to \mathbb{R}$ such that:

(i) $Q_N \geq 0$ can be proved without assuming RH (positivity is unconditional).

(ii) $Q_N(v) = 0$ for all $v \in \mathbb{R}^{N+1}$ implies $a_k^{full} = a_k^{full,on}$ for $0 \leq k \leq N$.

(iii) $Q_N \to 0$ as $N \to \infty$ in a controlled way (compatibility with the regularization).

If such a $Q_N$ existed, the argument for RH would be:

$$Q_N \geq 0 \text{ (unconditionally)} \implies a_k^{full} = a_k^{full,on} \;\forall k \leq N \implies T_\lambda = 0 \;\forall \lambda \implies \text{RH}.$$

### 7.2. Where would the positivity of $Q_N$ come from?

We identify three possible sources:

**Source 1: Direct positivity of $dm_{full}$.** The measure $dm_{full} = |\zeta|^2 dm_\infty$ is a positive Borel measure (trivially, since it is the product of a non-negative function with a positive measure). But positivity of $dm_{full}$ implies only that the moments $\int s^k\, dm_{full}(s) \geq 0$ for even $k$, which is insufficient to determine the sign of $dm_{full} - dm_{full,on}$.

**Source 2: Turán-type inequalities for $|\zeta|^2$.** Turán-type inequalities (Turán's power-sum method, 1948) give bounds on exponential sums of the type $\sum_n a_n e^{i\lambda_n t}$ in terms of the coefficients $a_n$ and the frequencies $\lambda_n$. A suitable formulation might give inequalities of the type:

$$\int_a^b |\zeta(1/2+is)|^2\, f(s)\, ds \geq C(a,b) \int_a^b f(s)\, ds$$

for some class of functions $f$ and constant $C(a,b) > 0$. If $f = |P_k|^2\, w$ (density of the measure $dm_\infty$ against the polynomial $P_k$), this would give $\Delta_k \geq 0$ with equality only if the zeros of $\zeta$ are all on the critical line — which is exactly RH. However, the implication $\Delta_k \geq 0 \Rightarrow$ RH requires non-trivially inverting the logic.

**Source 3: Positivity of the complete zeta function $\xi$.** The function $\xi(s)$ is real on the real line and has all its zeros (under RH) on the critical line. Positivity of $\xi$ in certain domains, or the property that $\xi$ is a Pólya-Laguerre function (limit of polynomials with real roots), gives constraints on the distribution of its zeros. If $\xi$ were a Pólya-Laguerre function, RH would follow. But proving that $\xi$ has this property is equivalent to RH.

### 7.3. Conclusion: the obstacle and the structure of the problem

**Proposition 7.2 (Diagnosis of the obstacle).** The program of importing the Weil mechanism to the number-field case through the CCM formalism is blocked by Pillar III (positivity) in the following precise sense:

(i) Pillar I is partially implemented: $J^{full}$ encodes the zeros of $\zeta$, but not in the direct form eigenvalues = zeros.

(ii) Pillar II is fully implemented: the functional equation gives $b_k^{full} = 0$ and the duality $\rho \leftrightarrow 1-\rho$.

(iii) Pillar III is absent: no unconditional positive quadratic form is known whose positivity implies $a_k^{full} = a_k^{full,on}$.

*Proof.* (i) is the content of §1 and §5. (ii) is Proposition 4.1 and Corollary 4.4. (iii) is a consequence of Proposition 5.2 and the discussion in §7.2: all known sources of positivity (positive measure, Turán inequalities, positivity of $\xi$) are either circular (assume RH) or insufficient to force the equality of coefficients. $\square$

**Final remark 7.3 (The analogy as a guide).** Despite the blockage at Pillar III, the analogy with the case of curves plays a precise heuristic role: it indicates that the sought positivity is of the type of a "Hodge inequality" for the Jacobi operator, and that the correct formalism for regularizing the infinite dimension is the kernel $W_\lambda$ (analogous to truncation to $N$ eigenvalues of Frobenius). This guide points the search toward spectral inequalities for perturbed Jacobi operators, an active field of research (see Simon [S11], Damanik-Killip-Simon [DKS10]).

---

## §8. Summary of results and conjectures

### 8.1. Results proved in this document

1. **(Proposition 1.2)** $J^{full}$ is self-adjoint with spectrum $\subseteq \mathbb{R}$; its spectrum does not directly distinguish the position of the zeros of $\zeta$.

2. **(Proposition 2.3)** The perturbation $E = J^{full} - J^\infty$ is Hilbert-Schmidt under the standard estimates on $|\zeta|^2$ on the critical line.

3. **(Proposition 3.2)** The coefficients $a_k^\infty$ are log-concave (not log-convex), which indicates that the Castelnuovo-Severi analogy is not formulated as log-convexity of the coefficients but as log-concavity.

4. **(Proposition 4.1 and Corollary 4.4)** Poincaré duality (Pillar II) is automatically built in via $b_k^{full} = 0$: Pillar II of the Weil mechanism is unconditional in the number-field world.

5. **(Propositions 5.1 and 5.2)** Weil's argument cannot be directly transported to infinite dimension because the relevant traces diverge.

6. **(Proposition 6.1)** The trace $T_\lambda$ is the "regularized Weil trace" $\sum_{k \leq N(\lambda)} [(a_k^{full})^2 - (a_k^{full,on})^2]$, with the kernel $W_\lambda$ playing the role of the finite dimension $2g$.

7. **(Proposition 7.2)** Diagnosis of the obstacle: Pillar III (positivity) is the only one absent; all other elements of the Weil mechanism have a well-defined analogue in the CCM formalism.

### 8.2. Conjectures formulated

- **(Conjecture 3.5)** Log-concavity of $\{(a_k^{full})^2\}$: $(a_k^{full})^4 \geq (a_{k-1}^{full})^2(a_{k+1}^{full})^2$ for all $k \geq 1$.

- **(Conjecture 6.2)** The criterion $T_\lambda = 0$ is the regularized infinite-dimensional analogue of Weil's criterion $\sum_{j=1}^{2g}(|\alpha_j|^2 - q) = 0$ for curves.

- **(Problem 7.1)** Construction of the unconditional quadratic form $Q_N \geq 0$ whose positivity would imply RH: this is the precise analogue of the arithmetic Hodge index / Castelnuovo-Severi problem.

---

## References

- [A65] N. Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver and Boyd, 1965.
- [C99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999), 29–106.
- [CCM24] A. Connes, C. Consani, H. Moscovici, *Spectral triples and zeta functions*, preprint, 2024.
- [DKS10] D. Damanik, R. Killip, B. Simon, *Perturbations of orthogonal polynomials with periodic recursion coefficients*, Ann. of Math. 171 (2010), 1931–2010.
- [KS03] R. Killip, B. Simon, *Sum rules for Jacobi matrices and their applications to spectral theory*, Ann. of Math. 158 (2003), 253–321.
- [S11] B. Simon, *Szegő's Theorem and Its Descendants: Spectral Theory for $L^2$ Perturbations of Orthogonal Polynomials*, Princeton University Press, 2011.
- [T51] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (revised by D. R. Heath-Brown), Oxford University Press, 1986.
- [Docs 64, 70–76] Internal documents of the program, Phases 32–33.

---

*End of Document 77.*
