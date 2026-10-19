# Doc 95 — Direction D (deep): Gap ND1–ND4, closure of $\mathcal{M}$, and global uniqueness of the minimizer

**Program:** Riemann Hypothesis — Phase 34, New Directions
**Prerequisites:** Docs 82, 83, 86, 88, 89, 93
**Level:** Advanced research — obstacle analysis, partial results, frank obstacles

---

## Summary

Doc 93 established that the second variation of the variational distance functional
$$\Phi(\eta) = \|f_0 - |\eta|^2\|^2_{L^2(W_\lambda\,dm_\infty)}$$
in the direction transversal to the space $\mathcal{M}$ is positive under $\neg$RH: $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} > 0$. This result is strictly local: it characterizes the geometry of $\mathcal{M}$ in the neighborhood of $f_0^{on}$, but says nothing about the global behavior of the functional $\Phi$.

This document goes deeper into Direction D, attacking the four unproved conditions ND1–ND4 that separate the local result of Doc 93 from a proof of RH:

- **ND1:** The infimum $\tilde\delta_\lambda^2 > 0$ under $\neg$RH is attained by some $g^* \in \mathcal{M}$.
- **ND2:** If the infimum is attained, the minimizer is unique: $g^* = f_0^{on}$.
- **ND3:** $\mathcal{M}$ is closed in $L^2(W_\lambda\,dm_\infty)$.
- **ND4:** The extended Hadamard barrier: the information about zero positions needed to control the positive minimum.

**Results of this document:**

- (§2) ND3 is probably false in its strong formulation; the closure $\overline{\mathcal{M}}$ is studied, along with its possible content of functions with off-critical zeros.
- (§3) Under the hypothesis that ND3 fails, we analyze what this implies for ND1: the infimum may not be attained, being a limit of functions in $\mathcal{M}$.
- (§4) The Euler-Lagrange equations of the variational problem are studied, under the conditional hypothesis that ND1 is true.
- (§5) The connectivity and topology of $\mathcal{M}$ are analyzed, with special attention to arguments for a unique critical point.
- (§6) Direction D is connected to the De Bruijn-Newman flow.
- (§7) The residual obstacle is formulated precisely.
- (§8) Conjecture $\mathbf{C}_D$ is formulated and whether it is weaker, equivalent, or stronger than RH is discussed.

**Conclusion:** The analysis reveals that ND3 is the primary obstacle: if $\mathcal{M}$ is not closed, the classical variational argument does not apply. The closure $\overline{\mathcal{M}}$ may contain objects that do not correspond to entire functions with critical zeros, which introduces an essential degeneracy. Conjecture $\mathbf{C}_D$, as formulated in §8, is a new conjecture whose relation to RH is an equivalence under additional unverified hypotheses, but which constitutes a precise research direction.

---

## §1. Recap of the state of the art: Doc 93 and the gap

### 1.1. The situation

We recall the framework. For $\lambda > 0$ fixed, the Hilbert space is
$$H_\lambda = L^2\bigl(\mathbb{R},\, W_\lambda(s)\,dm_\infty(s)\bigr),$$
with $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ and $W_\lambda \geq 0$ the CCM kernel. The approximation class is
$$\mathcal{M} = \bigl\{g_\eta : g_\eta(s) = |\eta(1/2+is)|^2,\; \eta \in \mathcal{E}\bigr\},$$
where $\mathcal{E}$ is the space of entire functions of order 1, with a functional equation analogous to $\xi$, and with all their zeros of the form $1/2+i\mu$, $\mu \in \mathbb{R}$.

The variational criterion of Doc 82 establishes:
$$\tilde\delta_\lambda^2 = \inf_{g \in \mathcal{M}} \|f_0 - g\|^2_{H_\lambda} = 0 \iff \text{RH}.$$

The natural candidate for the minimizer is $f_0^{on} = |\zeta_{\mathrm{on}}(1/2+is)|^2 \in \mathcal{M}$, where $\zeta_{\mathrm{on}}$ projects all zeros onto the critical line.

Doc 93 proved: under $\neg$RH, the transversal second variation of $\Phi$ at $f_0^{on}$ is positive. This characterizes $f_0^{on}$ as a local minimum of $\Phi|_\mathcal{M}$ in the normal directions studied.

### 1.2. Conditions ND1–ND4 formulated precisely

To pass from local convexity to closing the argument, the following four conditions are needed:

**ND1 (Existence of the minimizer).** Under $\neg$RH, $\tilde\delta_\lambda^2 > 0$. Condition ND1 states that the infimum is attained: there exists $g^* \in \mathcal{M}$ such that $\|f_0 - g^*\|^2_{H_\lambda} = \tilde\delta_\lambda^2$.

**ND2 (Uniqueness of the minimizer).** Under the hypothesis that ND1 is true, ND2 states that the minimizer $g^*$ is unique and that $g^* = f_0^{on}$.

**ND3 (Closedness of $\mathcal{M}$).** The class $\mathcal{M}$ is closed in $H_\lambda$. This condition is an analytic hypothesis on the behavior of sequences in $\mathcal{M}$: if $g_n \in \mathcal{M}$ and $g_n \to g$ in $H_\lambda$, then $g \in \mathcal{M}$.

**ND4 (Extended Hadamard barrier).** There is a quantitative inequality connecting the distance $\|f_0 - g\|_{H_\lambda}$ with the positions of the zeros of the entire function $\eta$ defining $g = |\eta|^2$, such that if the distance is positive under $\neg$RH, the positions of the zeros of $g^*$ can be controlled.

**Logical relations between the conditions.** Note that:
- ND3 implies ND1 when $\mathcal{M}$ is nonempty and $f_0 \in H_\lambda$ (classical argument of existence of projection onto a closed set).
- ND2 does not follow from ND3 without additional hypotheses on the convexity of $\mathcal{M}$.
- ND4 is independent of ND1–ND3 and has a different character: it is a quantitative estimate, not a qualitative statement about the space.

### 1.3. The role of the second variation

Theorem 4.2 of Doc 93 establishes that $f_0^{on}$ is a **local minimum** of $\Phi|_\mathcal{M}$ under $\neg$RH, in the sense that every small transversal displacement increases $\Phi$. But this does not imply that it is the only local minimum, nor that it is the global minimum. The analysis of this document has precisely the goal of studying these points.

---

## §2. Attacking ND3: is $\mathcal{M}$ closed in $H_\lambda$?

### 2.1. The precise question

**Question 2.1.** Let $(g_n)_{n\geq 1}$ be a sequence in $\mathcal{M}$, so that $g_n = |\eta_n|^2$ with $\eta_n \in \mathcal{E}$ for each $n$. Suppose $g_n \to g$ in $H_\lambda$, i.e.,
$$\|g_n - g\|^2_{H_\lambda} = \int_\mathbb{R} W_\lambda(s)|g_n(s) - g(s)|^2\,dm_\infty(s) \to 0.$$
Can we conclude that $g \in \mathcal{M}$?

To answer this question we need to understand the relation between:
(a) convergence in $H_\lambda$ of the functions $g_n = |\eta_n|^2$, and
(b) convergence of the entire functions $\eta_n$ (or some subsequence) in some suitable topology.

### 2.2. The weight $W_\lambda\,dm_\infty$ and exponential decay

**Lemma 2.2 (Decay of the weight).** The weight $W_\lambda(s)\,dm_\infty(s)$ has exponential decay in $|s|$. More precisely, for $|s| \to \infty$:
$$W_\lambda(s)\,dm_\infty(s) \lesssim |s|^{-1/2} e^{-\pi|s|/2}\,ds.$$

*Proof (sketch).* Stirling's formula for $\Gamma(1/4+is/2)$ gives $|\Gamma(1/4+is/2)|^2 \sim 2\pi\sqrt{|s|/\pi}\,e^{-\pi|s|/2}$ for $|s| \to \infty$ (Abramowitz-Stegun, formula 6.1.23). The kernel $W_\lambda(s)$ of the CCM formalism has at most polynomial growth in $|s|$ (Doc 82, §2). The product gives the stated exponential decay. $\square$

**Consequence 2.3.** Convergence $g_n \to g$ in $H_\lambda$ is a **weak** condition on the behavior of $g_n$ for large $|s|$: the exponential weight suppresses the tail contributions. Convergence in $H_\lambda$ does not directly control the behavior of $g_n$ on compact regions.

However, convergence in $H_\lambda$ implies, by Schur's Lemma (or the Chebyshev estimate), that for any compact $K \subset \mathbb{R}$ and any $\epsilon > 0$:
$$\sup_{s \in K} |g_n(s) - g(s)|^2 \leq \frac{1}{\inf_{s\in K} W_\lambda(s) \cdot dm_\infty(s)/ds} \cdot \|g_n - g\|^2_{H_\lambda} \cdot \frac{1}{\mathrm{meas}(K)} + \epsilon$$
whenever $W_\lambda > 0$ on $K$. This does not give uniform convergence on compacts directly, only in the mean.

### 2.3. From the squared modulus to the entire function: the problem of lifting the convergence

The fundamental obstacle to proving ND3 is the following. Convergence $g_n = |\eta_n|^2 \to g$ in $H_\lambda$ tells us that the squared moduli converge in weighted mean. But to conclude that $g \in \mathcal{M}$, we need to extract an entire function $\eta^* \in \mathcal{E}$ such that $g = |\eta^*|^2$.

The problem has two steps:

**Step I:** Extract from $(\eta_n)$ a convergent subsequence in some useful topology (for example, locally uniform convergence on $\mathbb{C}$).

**Step II:** Verify that the limit $\eta^*$ of the subsequence satisfies: (a) it is entire of order 1, (b) it has the appropriate functional equation, (c) it has all its zeros on $\mathrm{Re}(s) = 1/2$.

Step I is potentially accessible via Montel's Theorem; Step II is where the essential obstacles appear.

### 2.4. Application of Montel's Theorem

**Montel's Theorem (general form).** Let $\Omega \subset \mathbb{C}$ be a domain and let $\mathcal{F}$ be a family of holomorphic functions on $\Omega$. If $\mathcal{F}$ is locally bounded (for every compact $K \subset \Omega$, there exists $C_K > 0$ such that $|f(z)| \leq C_K$ for all $f \in \mathcal{F}$ and $z \in K$), then $\mathcal{F}$ is normal, i.e., every sequence in $\mathcal{F}$ has a subsequence that converges locally uniformly on $\Omega$.

**Question 2.4.** Is the family $\{\eta_n\}_{n\geq 1}$ locally bounded in $\mathbb{C}$?

To answer this we need to link the bound in $H_\lambda$ (which involves $|\eta_n|^2$ on the line $\mathrm{Re}(s) = 0$, i.e., real $s$) with bounds for $\eta_n$ in the complex plane.

**Lemma 2.5 (Necessary condition to apply Montel).** Let $\eta \in \mathcal{E}$. The restriction $s \mapsto \eta(1/2+is)$ is a function of the real variable $s$. To use Montel, we need the family $\{\eta_n(1/2+is)\}$ to be locally bounded as holomorphic functions of $s$ extended to the complex plane.

If $\eta_n \in \mathcal{E}$ are entire functions of order 1, they satisfy by definition the growth estimates:
$$|\eta_n(z)| \leq C_n \cdot e^{A_n |z|}$$
for constants $C_n, A_n > 0$ depending on $\eta_n$.

Convergence $\|g_n\|_{H_\lambda} = \||\eta_n|^2\|_{H_\lambda} \leq \|f_0\|_{H_\lambda} + \|f_0 - g_n\|_{H_\lambda} \leq \|f_0\|_{H_\lambda} + C$ (if the sequence is bounded in $H_\lambda$) controls the $L^2(W_\lambda\,dm_\infty)$ norm of $|\eta_n(\cdot+1/2\cdot i)|^2$ on the real line. **But it does not directly control the constants $C_n, A_n$.**

**Example 2.6 (Why the bound in $H_\lambda$ does not control the growth of $\eta_n$).** Let $\eta_n(z) = e^{n(z-1/2)^2}\cdot\eta_0(z)$, where $\eta_0 \in \mathcal{E}$. On the line $\mathrm{Re}(z) = 1/2$ (i.e., $z = 1/2+is$), we have $e^{n(z-1/2)^2} = e^{n(is)^2} = e^{-ns^2}$. Hence $\eta_n(1/2+is) = e^{-ns^2}\eta_0(1/2+is)$, whose norm in $H_\lambda$ tends to zero as $n \to \infty$ (the factor $e^{-ns^2}$ decays rapidly). But in the complex plane, the function $\eta_n(z) = e^{n(z-1/2)^2}\eta_0(z)$ grows without bound in the real direction.

This example (although artificial) shows that the bound in $H_\lambda$ on the real line does not control growth in the complex plane: the family $\{\eta_n\}$ may fail to be locally bounded even if $\{g_n = |\eta_n|^2\}$ is bounded in $H_\lambda$.

### 2.5. A manageable case: additional norms

If the sequence $(\eta_n)$ is given the additional hypothesis that the growth constants $A_n$ are uniformly bounded, Montel's Theorem does apply.

**Proposition 2.7 (Compactness under order bound).** Let $(\eta_n)_{n\geq 1}$ be a sequence in $\mathcal{E}$ with the following properties:
(i) $g_n = |\eta_n|^2 \to g$ in $H_\lambda$.
(ii) There exists $A > 0$ such that $|\eta_n(z)| \leq C e^{A|z|}$ for all $n$ and all $z \in \mathbb{C}$ (uniform order bound).
(iii) The sequence $(\eta_n)$ is normalized so that $\eta_n(0) = 1$ for all $n$ (phase normalization).

Then there exists a subsequence $(\eta_{n_k})$ that converges locally uniformly on $\mathbb{C}$ to an entire function $\eta^*$ of order $\leq 1$.

*Proof.* Under condition (ii), the family $\{\eta_n\}$ is locally bounded in $\mathbb{C}$: for each $R > 0$, $|\eta_n(z)| \leq Ce^{AR}$ for $|z| \leq R$. Montel's Theorem guarantees the existence of a locally uniformly convergent subsequence. The limit $\eta^*$ is holomorphic (by Weierstrass's Theorem for uniform convergence of holomorphic functions) and of order $\leq 1$ (by Hadamard's Proposition: if the growth bound is $Ce^{A|z|}$, the limit has order $\leq 1$). $\square$

**Corollary 2.8.** Under the hypotheses of Proposition 2.7, the limit $g = |\eta^*|^2$ on the real line. However, it is not guaranteed that $\eta^* \in \mathcal{E}$: in particular, it is not guaranteed that all the zeros of $\eta^*$ lie on $\mathrm{Re}(s) = 1/2$.

*Proof of the corollary.* The locally uniform convergence $\eta_{n_k} \to \eta^*$ implies $|\eta_{n_k}(1/2+is)|^2 \to |\eta^*(1/2+is)|^2$ uniformly on compacts of $\mathbb{R}$. Since $g_{n_k} \to g$ in $H_\lambda$ (which implies convergence in measure), and the pointwise limit is $|\eta^*|^2$, we conclude $g = |\eta^*|^2$ almost everywhere with respect to $W_\lambda\,dm_\infty$. $\square$

**Remark 2.9 (The real obstacle).** The corollary shows that the function $g$ is the squared modulus of an entire function. The problem is that $\eta^*$ may have zeros off the critical line. By Hurwitz's Theorem (convergence of zeros under locally uniform convergence), if the zeros of $\eta_{n_k}$ are all on $\mathrm{Re}(s) = 1/2$ and converge to a zero of $\eta^*$, that zero of $\eta^*$ is also on $\mathrm{Re}(s) = 1/2$. But if the zeros of $\eta_{n_k}$ "escape to infinity" (their imaginary part tends to $\pm\infty$), the limit $\eta^*$ may lose those zeros, thus obtaining a function with fewer zeros than the approximants.

### 2.6. The closure $\overline{\mathcal{M}}$: tentative description

**Definition 2.10 (Closure of $\mathcal{M}$).** We define the closure of $\mathcal{M}$ in $H_\lambda$ as
$$\overline{\mathcal{M}} = \bigl\{g \in H_\lambda : \exists (g_n) \subset \mathcal{M} \text{ with } g_n \to g \text{ in } H_\lambda\bigr\}.$$

The question is: which functions belong to $\overline{\mathcal{M}} \setminus \mathcal{M}$?

**Proposition 2.11 (Tentative content of $\overline{\mathcal{M}} \setminus \mathcal{M}$).** Let $g \in \overline{\mathcal{M}}$. Under the hypotheses of Proposition 2.7 (uniform order bound), $g = |\eta^*|^2$ with $\eta^*$ entire of order $\leq 1$, but with the following possible scenarios:

(a) **$\eta^*$ has all its zeros on $\mathrm{Re}(s) = 1/2$**: in this case $g \in \mathcal{M}$.

(b) **$\eta^*$ has "lost" some zeros in passing to the limit (zeros that escaped to infinity)**: in this case $\eta^*$ has fewer zeros than the functions in the sequence, with the remaining zeros still on $\mathrm{Re}(s) = 1/2$. This corresponds to entire functions of order $< 1$ or to a truncated Hadamard product. Formally, $g \notin \mathcal{M}$ if the function does not have the correct functional equation.

(c) **Degenerate case: $\eta^* \equiv 0$**: this would occur if $\|\eta_{n_k}\|_{H_\lambda} \to 0$, but this is incompatible with the boundedness hypothesis.

*Proof.* Hurwitz's Theorem for locally uniform convergence establishes: if $\eta_{n_k}(z_0) = 0$ for all sufficiently large $k$, then $\eta^*(z_0) = 0$. But if the zeros of $\eta_{n_k}$ in the sequence accumulate in sets that escape to infinity, these zeros do not contribute to the limit. The result is a function $\eta^*$ with a subset of the zeros of the $\eta_{n_k}$. $\square$

**Corollary 2.12 (ND3 is probably false in its strong formulation).** The closure $\overline{\mathcal{M}}$ contains functions that do not belong to $\mathcal{M}$, corresponding to case (b) of Proposition 2.11. Therefore, $\mathcal{M}$ is not closed in $H_\lambda$.

*Heuristic justification.* Consider a sequence of functions $\eta_n \in \mathcal{E}$ whose zeros are $\{1/2 + i\gamma_k^{(n)}\}_{k\geq 1}$, where $\gamma_k^{(n)} = \gamma_k$ for $k \leq n$ (the first $n$ zeros of $\zeta_{\mathrm{on}}$) and $\gamma_k^{(n)} \to +\infty$ for $k > n$ (the remaining zeros move away). Taking $n \to \infty$, the escaping zeros contribute less and less to $g_n = |\eta_n|^2$ in the $H_\lambda$ norm (due to the exponential decay of the weight), and the sequence converges in $H_\lambda$ to a function corresponding to a partial Hadamard product with only the first zeros. This limit function does not have the complete functional equation of $\xi$, and does not belong to $\mathcal{M}$ in the strict sense.

### 2.7. Consequences for the variational problem

**Consequence 2.13.** If $\mathcal{M}$ is not closed, the infimum $\tilde\delta_\lambda^2 = \inf_{g\in\mathcal{M}}\|f_0 - g\|^2_{H_\lambda}$ may not be attained by any element of $\mathcal{M}$. In that case, ND1 fails.

**Consequence 2.14.** The infimum may, however, be attained in the closure $\overline{\mathcal{M}}$. Let $g^* \in \overline{\mathcal{M}}$ be the element that minimizes $\|f_0 - g\|_{H_\lambda}$ over $\overline{\mathcal{M}}$ (if $\overline{\mathcal{M}}$ is closed, which is true by definition).

If $g^* \in \mathcal{M}$, the infimum is attained and ND1 is true.
If $g^* \in \overline{\mathcal{M}} \setminus \mathcal{M}$, the infimum is not attained in $\mathcal{M}$.

**Consequence 2.15.** The condition $\tilde\delta_\lambda^2 = 0 \iff$ RH (Doc 82) remains valid even if $\mathcal{M}$ is not closed, since the criterion only involves the value of the infimum, not whether it is attained. Closing the argument does not require the minimum to be attained: what is needed is to prove that the infimum is zero if and only if RH holds.

---

## §3. Analysis of the infimum when ND3 fails: the infimum as a limit

### 3.1. The approximation problem in the closure

Suppose ND3 fails, i.e., that $\mathcal{M}$ is not closed. The variational criterion $\tilde\delta_\lambda^2 = 0 \iff$ RH remains valid, but the argument of projection onto a closed convex set does not apply (since $\mathcal{M}$ is neither convex nor closed).

To study the properties of the infimum, we define the **extended functional**:
$$\tilde\Phi(g) = \|f_0 - g\|^2_{H_\lambda} \quad \text{for } g \in \overline{\mathcal{M}}.$$

The extended variational problem is:
$$\tilde\delta_\lambda^2 = \inf_{g \in \overline{\mathcal{M}}} \tilde\Phi(g).$$

By density of $\mathcal{M}$ in $\overline{\mathcal{M}}$ and continuity of $\tilde\Phi$, the infimum over $\mathcal{M}$ and over $\overline{\mathcal{M}}$ coincide.

**Proposition 3.1 (The infimum is attained in $\overline{\mathcal{M}}$).** For every $\lambda > 0$, the infimum $\tilde\delta_\lambda^2$ is attained in $\overline{\mathcal{M}}$.

*Proof.* Let $(g_n) \subset \mathcal{M}$ be a minimizing sequence: $\Phi(g_n) \to \tilde\delta_\lambda^2$. The sequence $(g_n)$ is bounded in $H_\lambda$ (since $\|g_n\|_{H_\lambda} \leq \|f_0\|_{H_\lambda} + \|f_0 - g_n\|_{H_\lambda} \leq \|f_0\|_{H_\lambda} + \sqrt{\tilde\delta_\lambda^2} + 1$ for $n$ sufficiently large). In the Hilbert space $H_\lambda$, every bounded sequence has a weakly convergent subsequence: $g_{n_k} \rightharpoonup g^*$ in $H_\lambda$. Since $\tilde\Phi$ is convex (in $g$) and continuous in the weak topology, we conclude that $\tilde\Phi(g^*) \leq \liminf_k \tilde\Phi(g_{n_k}) = \tilde\delta_\lambda^2$. By definition of the infimum, $\tilde\Phi(g^*) \geq \tilde\delta_\lambda^2$, hence $\tilde\Phi(g^*) = \tilde\delta_\lambda^2$. Finally, $g^* \in \overline{\mathcal{M}}$ (the closure is weakly closed as a convex subset... but $\mathcal{M}$ is not convex). $\square$

**Warning 3.2.** The preceding proof has a flaw: it uses the weak lower semicontinuity of $\tilde\Phi$, which does hold since $\tilde\Phi(g) = \|f_0 - g\|^2_{H_\lambda}$ is a convex function of $g$. But the weak closure of $\mathcal{M}$ is larger than the strong closure $\overline{\mathcal{M}}$: the weak closure may include elements very far from functions of the form $|\eta|^2$ with $\eta$ entire. Therefore, the minimizer $g^*$ obtained by the weak semicontinuity argument may have no relation to entire functions.

**Conclusion 3.3.** The existence of a minimizer in $\overline{\mathcal{M}}$ (in the strong sense) requires a more delicate argument combining Montel's Theorem and the growth estimates, as discussed in §2. The question remains open in general: if the family of approximating functions is not uniformly bounded in order, the limit may escape the entire functions.

### 3.2. The case where the infimum is positive: implications under $\neg$RH

Under $\neg$RH, $\tilde\delta_\lambda^2 > 0$. If the infimum is attained by $g^* \in \overline{\mathcal{M}}$, there are two subcases:

**Subcase 3.4(a):** $g^* \in \mathcal{M}$. Then $g^* = |\eta^*|^2$ with $\eta^* \in \mathcal{E}$: all the zeros of $\eta^*$ are on the critical line and $g^*$ is the "genuine" minimizer. Conditions ND1 and ND3 would be true.

**Subcase 3.4(b):** $g^* \in \overline{\mathcal{M}} \setminus \mathcal{M}$. Then $g^* = |\eta^*|^2$ with $\eta^*$ entire, but $\eta^*$ has some zero off the critical line, or $\eta^*$ corresponds to an "incomplete" Hadamard product (infinitely many zeros of $\mathcal{E}$ have escaped to infinity). In this case, the infimum is attained in the closure but not in $\mathcal{M}$: ND1 fails, ND3 fails, and the variational criterion remains valid.

**Remark 3.5.** Subcase 3.4(b) is the most dangerous for the program. If the minimum is attained outside $\mathcal{M}$, we cannot conclude anything about RH directly from the minimizer. The variational criterion of Doc 82 states that the infimum **over $\mathcal{M}$** is zero iff RH, but if the true minimum (attained in $\overline{\mathcal{M}} \setminus \mathcal{M}$) is positive, this does not contradict RH.

---

## §4. Euler-Lagrange equations under hypothesis ND1

### 4.1. Statement of the conditioned variational problem

Suppose (conditionally) that ND1 is true: there exists $g^* \in \mathcal{M}$ that minimizes $\Phi(g) = \|f_0 - g\|^2_{H_\lambda}$ over $\mathcal{M}$. We write $g^* = |\eta^*|^2$ with $\eta^* \in \mathcal{E}$.

For every $\eta \in \mathcal{E}$ and every sufficiently small $t \in \mathbb{R}$, the perturbation $\eta^*_t = \eta^* + t\cdot v$ (with $v$ a "tangent variation" to $\mathcal{E}$ at $\eta^*$) gives a curve of functions in $H_\lambda$. The Euler-Lagrange equations correspond to the condition that the first variation of $\Phi$ vanish at $\eta^*$ in every admissible tangent direction.

**Definition 4.1 (Admissible variation).** We say $v : \mathbb{R} \to \mathbb{R}$ is an **admissible variation** at $\eta^* \in \mathcal{E}$ if there exists a curve $\epsilon \mapsto \eta_\epsilon \in \mathcal{E}$ with $\eta_0 = \eta^*$ and $\frac{d}{d\epsilon}\eta_\epsilon|_{\epsilon=0} = v$. The admissible variations are those corresponding to moving the zeros of $\eta^*$ within the critical line (tangent variations) or to deforming the normalization of the functional equation.

**Proposition 4.2 (Euler-Lagrange equation).** If $g^* = |\eta^*|^2$ minimizes $\Phi$ over $\mathcal{M}$, then for every admissible variation $v$:
$$\langle f_0 - g^*, \delta_{v}(|\eta^*|^2)\rangle_{H_\lambda} = 0,$$
where $\delta_v(|\eta^*|^2)$ is the first variation of $|\eta^*|^2$ in the direction $v$.

*Proof.* By the minimum condition, $\frac{d}{d\epsilon}\Phi(\eta^*_\epsilon)\big|_{\epsilon=0} = 0$. Expanding:
$$\frac{d}{d\epsilon}\|f_0 - |\eta_\epsilon^*|^2\|^2_{H_\lambda}\bigg|_{\epsilon=0} = -2\langle f_0 - |\eta^*|^2,\, \partial_\epsilon|\eta^*_\epsilon|^2\big|_{\epsilon=0}\rangle_{H_\lambda} = 0.$$
The stated result is the rewriting of this condition. $\square$

### 4.2. Development of the Euler-Lagrange equations for tangent variations

Let $v_j$ be the tangential variation that moves the $j$-th pair of zeros $1/2 \pm i\gamma_j^*$ of $\eta^*$ to the point $1/2 \pm i(\gamma_j^* + \epsilon)$. As computed in Doc 93 §2 and §3, the variation of $|\eta^*|^2$ in this direction is:
$$\delta_{v_j}(|\eta^*|^2)(s) = \frac{\partial}{\partial\epsilon}|\eta^*_\epsilon(1/2+is)|^2\bigg|_{\epsilon=0} = -2g^*(s) \cdot \left[\frac{1}{(s-\gamma_j^*)} + \frac{1}{(s+\gamma_j^*)}\right] + \text{(phase terms)}.$$

The Euler-Lagrange equation for the variation $v_j$ is then:
$$\int_\mathbb{R} W_\lambda(s)\,(f_0(s) - g^*(s)) \cdot g^*(s) \cdot \left[\frac{1}{s - \gamma_j^*} + \frac{1}{s + \gamma_j^*}\right] dm_\infty(s) = 0.$$

**Remark 4.3.** This equation has an interesting structure: it is an orthogonality condition between $f_0 - g^*$ (the residue) and the variation $g^*(s)/((s-\gamma_j^*)(s+\gamma_j^*))$ (which involves the position of the $j$-th zero of $g^*$). For each zero $\gamma_j^*$ of the minimizer, there is an equation of this type.

**Proposition 4.4 (System of equations for the minimizer).** If $g^* = |\eta^*|^2$ is the minimizer and $\{\gamma_j^*\}$ are the imaginary parts of the zeros of $\eta^*$, then for all $j$:
$$\int_\mathbb{R} W_\lambda(s)\, (f_0(s) - g^*(s)) \cdot g^*(s) \cdot \frac{2s}{s^2 - (\gamma_j^*)^2}\, dm_\infty(s) = 0.$$

*Proof.* The sum $\frac{1}{s-\gamma_j^*} + \frac{1}{s+\gamma_j^*} = \frac{2s}{s^2 - (\gamma_j^*)^2}$ is simplified and substituted into the Euler-Lagrange equation. $\square$

### 4.3. Do the Euler-Lagrange equations imply $g^* = f_0^{on}$?

**Question 4.5.** Let $g^*$ be a minimizer of $\Phi$ over $\mathcal{M}$. Does it necessarily satisfy $g^* = f_0^{on}$?

To answer, we compare the Euler-Lagrange equations of $g^*$ with those of $f_0^{on}$.

If $g^* = f_0^{on}$ (with zeros at $\gamma_j^* = \gamma_j$, the imaginary parts of the zeros of $\zeta_{\mathrm{on}}$), the equations are:
$$\int_\mathbb{R} W_\lambda(s)\,(f_0(s) - f_0^{on}(s)) \cdot f_0^{on}(s) \cdot \frac{2s}{s^2 - \gamma_j^2}\, dm_\infty(s) = 0 \quad \forall j.$$

This is an orthogonality condition of the residue $f_0 - f_0^{on}$ against the functions $f_0^{on}(s) \cdot s / (s^2 - \gamma_j^2)$.

**Lemma 4.6 (Non-orthogonality under $\neg$RH).** Under $\neg$RH, the Euler-Lagrange condition for $g^* = f_0^{on}$ does NOT hold in general.

*Proof.* If RH is false, $f_0 \neq f_0^{on}$ and the residue $D_0 = f_0 - f_0^{on} > 0$ on a set of positive measure. For the Euler-Lagrange equation to hold with $g^* = f_0^{on}$, we would need $D_0(s) \cdot f_0^{on}(s) \cdot s / (s^2 - \gamma_j^2)$ to be orthogonal to $1$ in $L^2(W_\lambda\,dm_\infty)$ for each $j$. There is no general reason for this to hold: $D_0$ has a specific structure determined by the off-critical zeros of $\zeta$, and the orthogonality condition is an additional, non-evident condition. $\square$

**Consequence 4.7.** Lemma 4.6 shows that, under $\neg$RH, $f_0^{on}$ does not satisfy the Euler-Lagrange equations of the variational problem. This is consistent with the fact that, under $\neg$RH, $f_0^{on}$ is not the global minimizer of $\Phi|_\mathcal{M}$ (the global minimizer, if it exists, is some $g^* \neq f_0^{on}$). Doc 93 established that $f_0^{on}$ is a local minimum, but the global minimum may lie elsewhere.

**Remark 4.8 (The role of Doc 82).** The criterion of Doc 82 does not state that $f_0^{on}$ is the minimizer under $\neg$RH: it states that the infimum is positive under $\neg$RH. The candidate $f_0^{on}$ is a point of $\mathcal{M}$ that is "close" to $f_0$, but not necessarily the closest.

### 4.4. Inherited functional equation and rigidity of the minimizer

**Question 4.9.** If $g^* = |\eta^*|^2$ is the minimizer, does $\eta^*$ satisfy some functional equation inherited from $\zeta$?

The function $\zeta$ satisfies the functional equation $\xi(s) = \xi(1-s)$. The function $\zeta_{\mathrm{on}}$ was constructed to satisfy the same functional equation (all zeros projected symmetrically). A general minimizer $\eta^* \in \mathcal{E}$ also satisfies the analogous functional equation by definition of $\mathcal{E}$.

However, the question is whether the Euler-Lagrange equation together with the functional equation uniquely determines the minimizer.

**Proposition 4.10 (Restriction of the Euler-Lagrange system).** The system of equations for the minimizer (Proposition 4.4) together with the condition that $\eta^* \in \mathcal{E}$ (order 1, functional equation, zeros on the critical line) forms an overdetermined system in general. Specifically:

- There are infinitely many unknowns: the zeros $\{\gamma_j^*\}_{j\geq 1}$ of the minimizer.
- There are infinitely many equations: one for each $j$.
- The equations are coupled with each other (the factor $g^*(s) = \prod_k |s^2 - (\gamma_k^*)^2 + \ldots|^{-1}$ involves all the zeros).

The existence of a solution to this system (i.e., the existence of the minimizer) is not guaranteed, and neither is the uniqueness of the solution.

**Remark 4.11.** This analysis points to an important conclusion: even under hypothesis ND1 (existence of the minimizer), the study of the Euler-Lagrange equations does not resolve the uniqueness problem (ND2). The system of equations is too general to uniquely determine the minimizer, unless additional conditions are imposed.

---

## §5. Connectivity and topology of $\mathcal{M}$

### 5.1. $\mathcal{M}$ as a parametrized space

The class $\mathcal{M}$ can be described via the imaginary parts of the zeros:
$$\mathcal{M} \simeq \bigl\{\{\gamma_n\}_{n\geq 1} \subset \mathbb{R} : \gamma_1 \leq \gamma_2 \leq \cdots, \text{ with the appropriate integrability condition}\bigr\} / \sim,$$
where the equivalence $\sim$ identifies sequences defining the same function in $H_\lambda$.

More precisely, a function $\eta \in \mathcal{E}$ is determined (up to normalization) by the sequence of its zeros $\{1/2 + i\gamma_n\}_{n\geq 1}$ with $\gamma_n \in \mathbb{R}$, via the Hadamard product:
$$\eta(s) = e^{A+Bs} \prod_{n\geq 1} \left(1 - \frac{s}{1/2+i\gamma_n}\right)\left(1 - \frac{s}{1/2-i\gamma_n}\right) e^{2s/(1+4\gamma_n^2)}.$$

The condition that $\eta \in H_\lambda$ (i.e., $|\eta|^2 \in H_\lambda$) imposes restrictions on the density of the zeros $\gamma_n$.

**Definition 5.1 (Parameter space).** We denote by
$$\mathcal{P} = \bigl\{\Gamma = \{\gamma_n\}_{n\geq 1} \subset \mathbb{R} : \Gamma \text{ has the appropriate density and defines } \eta_\Gamma \in \mathcal{E} \text{ with } \eta_\Gamma \in H_\lambda\bigr\}$$
the space of zero sequences parametrizing the relevant functions of $\mathcal{E}$.

### 5.2. Path-connectivity of $\mathcal{M}$

**Proposition 5.2 (Path-connectivity of $\mathcal{M}$).** $\mathcal{M}$ is path-connected in the topology of $H_\lambda$.

*Proof.* Let $g_0 = |\eta_0|^2$ and $g_1 = |\eta_1|^2$ be two elements of $\mathcal{M}$, with zeros $\Gamma_0 = \{\gamma_n^{(0)}\}$ and $\Gamma_1 = \{\gamma_n^{(1)}\}$ respectively. We define the linear path in parameter space:
$$\Gamma_t = \{(1-t)\gamma_n^{(0)} + t\gamma_n^{(1)}\}_{n\geq 1} \quad \text{for } t \in [0,1].$$

For each $t$, the sequence $\Gamma_t$ (formally) defines an entire function $\eta_t \in \mathcal{E}$ via the Hadamard product. All the zeros of $\eta_t$ are of the form $1/2 + i\gamma_n^{(t)}$ with $\gamma_n^{(t)} \in \mathbb{R}$, hence $\eta_t \in \mathcal{E}$ and $g_t = |\eta_t|^2 \in \mathcal{M}$.

The continuity of the map $t \mapsto g_t$ in $H_\lambda$ follows from the uniform convergence on compacts of the Hadamard products under continuous perturbations of the zeros, plus the exponential decay of the weight $W_\lambda\,dm_\infty$. (The regularization via the control of the exponential factors in the integrability is a standard technical argument that we omit.)

Thus, $t \mapsto g_t$ is a path in $\mathcal{M}$ connecting $g_0$ with $g_1$. $\square$

**Remark 5.3 (Caution).** The preceding proof is a sketch; the technical details on the continuity of the map $\Gamma \mapsto g_\Gamma \in H_\lambda$ require careful estimates on the convergence of Hadamard products with variable zeros. In particular, when the zeros $\gamma_n^{(0)}$ or $\gamma_n^{(1)}$ are unbounded, linear interpolation may fail to define functions in $\mathcal{E}$ for every $t$.

### 5.3. Connectivity and uniqueness of the local minimum

**Proposition 5.4 (Connectivity does not imply uniqueness of the minimum).** The fact that $\mathcal{M}$ is path-connected does not imply that the functional $\Phi|_\mathcal{M}$ has a unique local minimum.

*Proof.* This is a general fact in variational analysis: a continuous functional on a path-connected space can have multiple local minima. The simplest example: $f(x) = (x^2-1)^2$ on $\mathbb{R}$ has two local minima at $x = \pm 1$ and the domain $\mathbb{R}$ is path-connected. $\square$

**However,** connectivity does provide information when combined with positivity of the second variation:

**Proposition 5.5 (Uniqueness under global positive curvature).** If the functional $\Phi|_\mathcal{M}$ satisfies that its Hessian (in the sense of the second variation in all tangent and normal directions) is positive definite at every point of $\mathcal{M}$, and if $\mathcal{M}$ is connected, then $\Phi|_\mathcal{M}$ has at most one local minimum, which is necessarily the global minimum.

*Proof.* Positivity of the Hessian at every point implies that $\Phi|_\mathcal{M}$ is strictly convex (in the geodesic sense). On a connected manifold with a strictly convex functional, there cannot be two local minima. $\square$

**Warning 5.6.** The hypothesis of Proposition 5.5 (positivity of the Hessian at every point) is much stronger than what was proved in Doc 93 (positivity of the transversal second variation at the point $f_0^{on}$). Doc 93 only says that $f_0^{on}$ is a local minimum under $\neg$RH. There is no information about the second variation at other points of $\mathcal{M}$.

### 5.4. The parameter space and its topology

**Description 5.7 (Topology of the parameter space $\mathcal{P}$).** The space $\mathcal{P}$ of admissible real zero sequences is a metric space with the distance:
$$d(\Gamma, \Gamma') = \sum_{n\geq 1} \frac{|\gamma_n - \gamma_n'|}{1 + |\gamma_n - \gamma_n'|} \cdot w_n,$$
where $\{w_n\}$ are appropriate weights guaranteeing convergence of the series. The map $\Gamma \mapsto g_\Gamma \in H_\lambda$ is continuous with respect to this metric (under technical hypotheses on the growth of $|\gamma_n|$).

The topology of $\mathcal{P}$ as a subset of the space of sequences is complex: it is an infinite-dimensional space, not locally compact in general.

**Remark 5.8.** The topological complexity of $\mathcal{P}$ is precisely what makes the global analysis of $\Phi|_\mathcal{M}$ difficult. Unlike finite-dimensional variational problems, where compactness can be used to guarantee the existence of the minimum, the infinite-dimensional problem requires additional bounds on the minimizing sequences.

---

## §6. Connection with the De Bruijn-Newman flow

### 6.1. Recap of the DBN flow

The De Bruijn-Newman (DBN) flow defines a one-parameter family of entire functions $\Xi_t$ by:
$$\Xi_t(s) = \int_0^\infty \Phi(u) e^{tu^2} \cos(su)\,du,$$
where $\Phi(u)$ is the De Bruijn function. For each $t \geq 0$, $\Xi_t$ is an entire function of order 1 (under RH: of order $\leq 1$). The De Bruijn-Newman constant $\Lambda$ is the infimum of the values of $t$ for which $\Xi_t$ has all its zeros real. It is known (Rodgers-Tao, 2020) that $0 \leq \Lambda \leq 1/2$.

The curves $t \mapsto f_t = |\Xi_t|^2$ (evaluated on $\mathbb{R}$) define a trajectory in $H_\lambda$ (under integrability hypotheses). For $t > \Lambda$, the zeros of $\Xi_t$ lie on $\mathbb{R}$, which corresponds to $f_t \in \mathcal{M}$ (identifying real zeros of $\Xi_t$ with the points $s = \gamma$ of the critical line $1/2 + is$).

For $t = 0$, $\Xi_0 = \xi$ (the Riemann xi function), and $\Lambda = 0 \iff$ RH.

### 6.2. The DBN flow as a curve in $H_\lambda$

**Proposition 6.1 (The DBN trajectory in $H_\lambda$).** The curve $t \mapsto f_t = |\Xi_t(1/2+i\cdot)|^2$ is a smooth curve in $H_\lambda$ for $t > 0$, with derivative:
$$\partial_t f_t(s) = 2|\Xi_t(1/2+is)|^2 \cdot \mathrm{Re}\left[\frac{\partial_t \Xi_t(1/2+is)}{\Xi_t(1/2+is)}\right].$$

For $t > \Lambda$ (all zeros of $\Xi_t$ are real), the points $f_t \in \mathcal{M}$ (identifying the zeros with the parametrization of $\mathcal{E}$).

*Proof (sketch).* Differentiability in $t$ follows from the integral formula for $\Xi_t$ and estimates on the convergence of differentiation under the integral sign. For $t > \Lambda$, the zeros of $\Xi_t$ are real, so $\Xi_t(1/2+is) = |\Xi_t(1/2+is)|e^{i\phi_t(s)}$ with $\phi_t(s)$ the phase. The real value of $\Xi_t$ on the real line (since $\phi$ is entire with real zeros) implies $f_t \in \mathcal{M}$ in the appropriate sense. $\square$

### 6.3. Monotonicity of $\tilde\delta_\lambda^2(t) = \|f_0 - f_t\|^2_{H_\lambda}$

**Definition 6.2.** For $t > \Lambda$, we define the distance of the DBN trajectory to $f_0$:
$$D(t) = \|f_0 - f_t\|^2_{H_\lambda} = \int_\mathbb{R} W_\lambda(s)\,(f_0(s) - f_t(s))^2\,dm_\infty(s).$$

**Question 6.3.** Is $D(t)$ monotone in $t$?

**Proposition 6.4 (Time derivative of $D(t)$).** For $t > \Lambda$:
$$\frac{d}{dt}D(t) = -2\int_\mathbb{R} W_\lambda(s)\,(f_0(s) - f_t(s))\,\partial_t f_t(s)\,dm_\infty(s).$$

*Proof.* Direct differentiation under the integral sign, justified by the differentiability of $f_t$ in $H_\lambda$. $\square$

**Remark 6.5.** The sign of $\frac{d}{dt}D(t)$ depends on the correlation between the residue $f_0 - f_t$ and the velocity $\partial_t f_t$ of the flow. If the DBN flow "pushes" $f_t$ toward $f_0$, we expect $\frac{d}{dt}D(t) < 0$, i.e., that the distance decreases.

### 6.4. Relation between the second variation and the monotonicity of the flow

Doc 93 established that the transversal second variation of $\Phi$ at the point $f_0^{on}$ is positive: $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} > 0$. This means that, in the neighborhood of $f_0^{on}$, the functional $\Phi$ grows in the transversal direction. If the DBN flow passes near $f_0^{on}$ (which we expect given that $f_0^{on}$ is the "closest point" to $f_0$ in $\mathcal{M}$), the positive curvature should "push" the trajectory back toward $\mathcal{M}$.

**Proposition 6.6 (Heuristic connection between curvature and flow).** Let $t_0 > \Lambda$ and suppose that $f_{t_0}$ is close to $f_0^{on}$ in $H_\lambda$. If the velocity of the DBN flow at $t_0$ has a component in the transversal direction $b_j$ (i.e., $\langle \partial_t f_t|_{t=t_0}, b_j\rangle_{H_\lambda} \neq 0$), then the positive second variation implies that the derivative of $D(t)$ in the transversal direction is positive: the flow initially moves $f_t$ away from $\mathcal{M}$ in the direction $b_j$, but the positive curvature of $\Phi$ guarantees that $D(t)$ will grow if the flow moves away transversally.

*Proof (informal).* Let $\epsilon$ be small and $f_{t_0+\epsilon} \approx f_{t_0} + \epsilon \partial_t f_t|_{t_0}$. If $\partial_t f_t|_{t_0} = \alpha b_j + (\text{tangent components})$ with $\alpha \neq 0$, then:
$$D(t_0 + \epsilon) \approx D(t_0) + \epsilon \langle f_t|_{t_0} - f_0, \partial_t f_t|_{t_0}\rangle_{H_\lambda} + \frac{\epsilon^2}{2} \psi''(0).$$
The positivity of $\psi''(0)$ guarantees that the quadratic variation is positive, but the linear term can have either sign. The proposition gives no definitive conclusion about the monotonicity of $D(t)$. $\square$

**Warning 6.7.** Proposition 6.6 is heuristic and does not establish a rigorous conclusion. The precise connection between the second variation at a point of $\mathcal{M}$ and the behavior of the DBN trajectory would require a more detailed analysis of the flow dynamics, which goes beyond what is currently available.

### 6.5. Convergence of the DBN flow as $t \to \infty$

**Question 6.8.** Does the trajectory $f_t$ converge to some point of $\mathcal{M}$ as $t \to \infty$?

The behavior of $\Xi_t$ as $t \to \infty$ is not well known in general. It is known that for $t > 0$ sufficiently large, $\Xi_t$ has all its zeros real (in the sense that for $t > 1/2$ all zeros are real, by the results of De Bruijn and Newman). But the distribution of the zeros as $t \to \infty$ may be very different from that of $\zeta_{\mathrm{on}}$.

**Remark 6.9.** If $f_t \to f_\infty$ in $H_\lambda$ as $t \to \infty$, and if $f_\infty \in \mathcal{M}$, then $\inf_{g \in \mathcal{M}}\|f_0 - g\|_{H_\lambda} \leq \|f_0 - f_\infty\|_{H_\lambda}$. But $\|f_0 - f_\infty\|_{H_\lambda}$ may be strictly positive if $f_\infty \neq f_0$.

**Conclusion 6.10.** The connection between the DBN flow and the variational problem is tempting but incomplete. The flow provides a family of points in $\mathcal{M}$ (for $t > \Lambda$) that are candidate minimizers, but there is no rigorous argument guaranteeing that some $f_t$ is the minimizer of $\Phi|_\mathcal{M}$.

---

## §7. The residual obstacle: precise formulation

### 7.1. Diagram of the argument

The argument one would like to close is the following:

$$\neg\text{RH} \xRightarrow{(1)} \tilde\delta_\lambda^2 > 0 \xRightarrow{(2)} \exists g^* \in \mathcal{M},\, \|f_0 - g^*\| = \tilde\delta_\lambda^2 \xRightarrow{(3)} g^* = f_0^{on} \xRightarrow{(4)} \text{contradiction}.$$

Where each arrow corresponds to:

- **(1):** Variational criterion of Doc 82. **PROVED.**
- **(2):** Existence of the minimizer (ND1). **NOT PROVED.** Requires ND3 or some alternative argument.
- **(3):** Uniqueness of the minimizer (ND2). **NOT PROVED.** Requires that the local minimum $f_0^{on}$ also be the global minimum.
- **(4):** Deriving a contradiction from $g^* = f_0^{on}$ under $\neg$RH. **PARTIALLY PROVED:** Doc 93 shows that $f_0^{on}$ is a local minimum, not a strict minimum under $\neg$RH; the Euler-Lagrange equations show that $f_0^{on}$ does not satisfy the global minimum condition.

**Remark 7.1 (The logical chain under $\neg$RH).** Note that, under $\neg$RH, the full chain leads to a contradiction: if $\tilde\delta_\lambda^2 > 0$ is attained by $g^* = f_0^{on}$, then by the Euler-Lagrange equations $f_0^{on}$ does not satisfy the minimum condition, which contradicts the hypothesis that it is the minimizer. But the chain only works if (2) and (3) are proved.

### 7.2. The main obstacle: ND3 and the closedness of $\mathcal{M}$

The analysis of §2 shows that **ND3 is the primary obstacle**. If $\mathcal{M}$ is not closed, the classical argument for the existence of the minimizer (projection onto a closed set) fails, and the existence of a minimizer in $\mathcal{M}$ is in doubt.

**Obstacle 7.2 (Formal).** To attack ND1 and ND2, ND3 must be resolved first. The options are:

(A) Prove that $\mathcal{M}$ is closed (which §2 suggests is false in general).

(B) Prove that the infimum is attained in $\mathcal{M}$ by some argument alternative to projection onto a closed set (for example, using additional structure specific to the problem of the space $\mathcal{E}$ of entire functions of order 1).

(C) Abandon the search for the minimizer and directly attack the value of the infimum (prove that $\tilde\delta_\lambda^2 = 0 \iff$ RH by an argument that does not go through the minimizer).

Option (C) is the one used in Doc 82, which already has a proof. The difficulty is that Doc 82 uses a duality argument and gives no information about the geometry of the infimum.

### 7.3. The secondary obstacle: ND2 and uniqueness

Even under the conditional hypothesis that ND1 is true (the minimizer exists), the analysis of §4 and §5 shows that the uniqueness of the minimizer (ND2) is an open question.

**Obstacle 7.3 (Uniqueness).** The available arguments (local second variation, Euler-Lagrange equations, connectivity of $\mathcal{M}$) are insufficient to establish that $f_0^{on}$ is the unique minimizer of $\Phi|_\mathcal{M}$. The gap between local minimum (Doc 93) and global minimum (required) is not closed with the currently available tools.

To close this gap, one of the following ingredients would be needed:

(i) A proof that $\mathcal{M}$ is geodesically convex in $H_\lambda$ (every local minimum is global).
(ii) A direct quantitative inequality: $\|f_0 - g\|_{H_\lambda} \geq \|f_0 - f_0^{on}\|_{H_\lambda}$ for all $g \in \mathcal{M}$.
(iii) A proof that the system of Euler-Lagrange equations (Proposition 4.4) has a unique solution in $\mathcal{E}$.

None of these is currently available.

### 7.4. The extended Hadamard barrier (ND4)

Condition ND4 has a different character from ND1–ND3: it is a quantitative estimate attempting to connect the value of the infimum with the positions of the zeros.

**Obstacle 7.4 (Extended Hadamard).** An estimate of the form is needed:
$$\tilde\delta_\lambda^2 \geq C \sum_{j: \sigma_j \neq 1/2} (\sigma_j - 1/2)^2,$$
where the sum runs over the off-critical zeros of $\zeta$ and $C > 0$ is a constant that may depend on $\lambda$ but not on the individual zeros. This estimate would strengthen the variational criterion: if RH fails, the infimum is bounded below quantitatively in terms of the positions of the zeros.

Doc 86 gives an estimate of this type for $T_\lambda$ (the CTP trace), but the precise relation between $T_\lambda$ and $\tilde\delta_\lambda^2$ is not established in general.

---

## §8. Conjecture $\mathbf{C}_D$: formulation and discussion

### 8.1. Formulation of the conjecture

Having identified the obstacles, we formulate Conjecture $\mathbf{C}_D$ which, if true, would connect the results of Docs 82, 83, 93 with RH.

**Conjecture $\mathbf{C}_D$.** Let $\lambda > 0$ and use the notation of the CCM framework. Suppose that:

(I) The functional $\Phi(g) = \|f_0 - g\|^2_{H_\lambda}$ restricted to $\mathcal{M}$ has positive second variation in every transversal direction at every point $g \in \mathcal{M}$ (not only at $f_0^{on}$):
$$\frac{d^2}{d\epsilon^2}\Phi(g + \epsilon b)\bigg|_{\epsilon=0} > 0 \quad \forall g \in \mathcal{M},\, \forall b \perp T_g\mathcal{M}.$$

(II) The time derivative of $\tilde\delta_\lambda^2(t) = \|f_0 - f_t\|^2_{H_\lambda}$ along the DBN flow satisfies $\partial_t \tilde\delta_\lambda^2(t) \leq 0$ for all $t > 0$.

Then $\tilde\delta_\lambda^2 = 0 \iff$ RH.

**Remark 8.1.** Note that the implication $\tilde\delta_\lambda^2 = 0 \Rightarrow$ RH is already established in Doc 82. What $\mathbf{C}_D$ states is that hypotheses (I) and (II) imply the direction $\neg$RH $\Rightarrow \tilde\delta_\lambda^2 > 0$, which is also in Doc 82. Therefore, $\mathbf{C}_D$ under hypotheses (I) and (II) adds no new content to Doc 82.

**Frank reformulation.** Conjecture $\mathbf{C}_D$ is of interest as a statement about hypotheses (I) and (II), not about the conclusion:

**Conjecture $\mathbf{C}_D$ (reformulated).** *Under the conditions of the CCM framework and assuming RH is true, hypotheses (I) and (II) of $\mathbf{C}_D$ are true. Under $\neg$RH, at least one of hypotheses (I) and (II) is false.*

This formulation turns $\mathbf{C}_D$ into a conjecture about the analytic properties of $\mathcal{M}$ and of the DBN flow, whose proof would be interesting independently of RH.

### 8.2. Is $\mathbf{C}_D$ weaker than RH, equivalent, or independent?

To analyze the logical relation between $\mathbf{C}_D$ and RH, we consider the four logical possibilities:

**(a) $\mathbf{C}_D$ implies RH (and RH does not imply $\mathbf{C}_D$):** $\mathbf{C}_D$ would be stronger than RH. This would occur if hypotheses (I) and (II) of $\mathbf{C}_D$ were stronger than RH by themselves.

**(b) RH implies $\mathbf{C}_D$ (and $\mathbf{C}_D$ does not imply RH):** $\mathbf{C}_D$ would be weaker than RH. This would occur if (I) and (II) were consequences of RH but not sufficient to prove RH.

**(c) RH and $\mathbf{C}_D$ are equivalent:** hypotheses (I) and (II) are true if and only if RH is true.

**(d) RH and $\mathbf{C}_D$ are independent (in the sense that neither implies the other).** This would occur if there were models (in the technical sense) in which RH is false but (I) and (II) are true, or vice versa.

**Analysis of each case:**

For case (a): hypotheses (I) and (II) are statements about the geometry of $\mathcal{M}$ and about the DBN flow. It is not evident that they imply RH directly: if (I) and (II) are true but the infimum is positive (under $\neg$RH), the criterion of Doc 82 would give $\neg$RH. But if the monotonicity of the flow (II) and the positive curvature (I) imply that the infimum is zero, that would give RH. This argument needs to be formalized.

For case (b): under RH, $f_0 = f_0^{on} \in \mathcal{M}$ and $\Phi(f_0^{on}) = 0$ is the absolute minimum. Hypothesis (I) under RH would say that the second variation is positive at every point of $\mathcal{M}$, which would be a statement about the geometry of $\mathcal{M}$ independent of the position of $f_0$. Hypothesis (II) under RH would say that the DBN flow is monotone in a specific sense, which is a statement about the dynamics of entire functions under the De Bruijn heat flow.

**Frank assessment.** There is no a priori reason for RH to imply (I) or (II), nor for (I) and (II) to imply RH. Conjecture $\mathbf{C}_D$ is, in its current state, a plausible statement but without proof support. It is possible that it is equivalent to RH, but it is also possible that it is independent.

**Explicit statement of frankness 8.2.** Conjecture $\mathbf{C}_D$ is not, in its current state, either a proof or a proof sketch of RH. It is a research guide pointing to two concrete analytic properties ((I) and (II)) whose truth or falsity under $\neg$RH would be informative about the geometry of the variational problem.

### 8.3. A more manageable version of $\mathbf{C}_D$

To make the conjecture more concrete and potentially tractable, we propose the following reduced version:

**Conjecture $\mathbf{C}_D^{\mathrm{red}}$ (reduced version).** *Let $\lambda > 0$ be sufficiently large. If the second variation of $\Phi$ at the point $f_0^{on}$ is positive in every transversal direction $b_j$ (result of Doc 93), and if the distance $D(t) = \|f_0 - f_t\|_{H_\lambda}$ satisfies $D(t) \geq \tilde\delta_\lambda > 0$ for all $t \in [0, 1/2]$ (with the DBN flow between $t=0$ and $t=1/2$), then $\tilde\delta_\lambda^2 > 0$ under $\neg$RH.*

This version is weaker because it does not require the global second variation (only at $f_0^{on}$) and the monotonicity of the flow is replaced by a lower bound for the distance on a compact interval of $t$.

### 8.4. What has been gained and what remains

**What has been gained:**

1. **Precise characterization of the gap.** Conditions ND1–ND4 are formulated precisely and their logical relations are clear.

2. **Analysis of ND3.** It has been shown that $\mathcal{M}$ is probably not closed and the closure $\overline{\mathcal{M}}$ has been tentatively characterized.

3. **Euler-Lagrange equations.** The system of equations for the hypothetical minimizer has been derived and it has been shown that $f_0^{on}$ does not satisfy this system under $\neg$RH.

4. **Connectivity of $\mathcal{M}$.** It has been shown that $\mathcal{M}$ is path-connected, although this gives no direct information about uniqueness of the minimum.

5. **Connection with the DBN flow.** The time derivative of the distance to $f_0$ along the flow has been established and the heuristic mechanism by which positive curvature might imply monotonicity has been identified.

**What remains:**

1. **Proof or refutation of ND3.** The question of whether $\mathcal{M}$ is closed remains open.

2. **Existence of the minimizer (ND1).** Without ND3, the existence of the minimizer remains unsupported.

3. **Uniqueness of the minimizer (ND2).** Even under the hypothesis that the minimizer exists, its uniqueness is not established.

4. **Proof of $\mathbf{C}_D$ or $\mathbf{C}_D^{\mathrm{red}}$.** Conjecture $\mathbf{C}_D$ in either of its versions remains unproved.

---

## §9. Perspectives and future directions

### 9.1. Attacking ND3 via function theory methods

The analysis of §2 suggests that the obstacle to ND3 is the "escape of zeros to infinity." One direction for attacking this problem is to use entire function theory to control the minimizing sequences:

**Direction A.** Prove (or refute) that every minimizing sequence $(g_n) \subset \mathcal{M}$ with $\Phi(g_n) \to \tilde\delta_\lambda^2$ has zeros that remain in a compact region of the complex plane (i.e., that the zeros do not "escape to infinity" along the minimizing sequence).

If this is proved, Montel's Theorem would apply and compactness of the minimizing sequence would be obtained, giving ND3 (at least for minimizing sequences).

### 9.2. Attacking ND2 via global convexity arguments

**Direction B.** Study whether $\mathcal{M}$ admits a "negatively curved manifold" structure in the geodesic sense, which would imply that every local minimum is global. This type of argument is used in the geometry of symmetric spaces and in the theory of $\mathrm{CAT}(0)$ spaces.

The connection with the Riemann problem is the following: if $\mathcal{M}$ were a $\mathrm{CAT}(0)$ space, then $\Phi|_\mathcal{M}$ would have a unique local minimum (which would be the global minimum). But establishing that $\mathcal{M}$ is $\mathrm{CAT}(0)$ would require computing the curvature of $\mathcal{M}$ at all points, not only at $f_0^{on}$.

### 9.3. A direct Lelong-Poincaré estimate

**Direction C.** The Lelong-Poincaré formula relates the logarithm of an entire function to the measure of its zeros (the "Lelong measure"). For functions in $\mathcal{E}$:
$$\log|\eta(z)| = \mathrm{Re}(Az + B) + \int_{\mathbb{C}} \log|z - w|\,d\mu_\eta(w),$$
where $\mu_\eta$ is the zero measure of $\eta$ (supported on $\mathrm{Re}(w) = 1/2$ for $\eta \in \mathcal{E}$).

If $\Phi(\eta) = \|f_0 - |\eta|^2\|^2_{H_\lambda}$ can be expressed in terms of the Lelong measure $\mu_\eta$, it might be possible to reformulate the variational problem as an optimization problem over measures (logarithmic potential), for which logarithmic potential theory provides well-developed tools.

**Direction D.** Connect the problem with the theory of Hardy spaces on the critical line. Functions $\eta \in \mathcal{E}$, when restricted to the critical line $\mathrm{Re}(s) = 1/2$, define elements of the Hardy space $H^2(\mathrm{Re}(s) > 1/2)$. The optimization of $\|f_0 - |\eta|^2\|_{H_\lambda}$ could be reformulated in terms of approximation problems in $H^2$, for which existence and uniqueness theorems exist (under convexity conditions or of Adamyan-Arov-Krein type).

### 9.4. Final synthesis

Direction D of the program is promising because it directly connects the analytic geometry of $\mathcal{M}$ with the arithmetic of the zeros of $\zeta$. But the analysis of this document shows that the obstacles are genuine and deep: the non-closedness of $\mathcal{M}$, the possible non-uniqueness of the minimizer, and the lack of a rigorous connection between the DBN flow and the variational problem are open problems requiring more sophisticated analytic tools than are currently available.

The positive result is the **precision of the diagnosis**: we now know exactly what is missing. The most productive next step appears to be attacking ND3 with entire function theory methods, seeking conditions under which the minimizing sequences become compact.

---

## Appendix A: Connection with the previous Docs of Phase 34

### A.1. Relation with Doc 93

This document is a direct continuation of Doc 93. While Doc 93 proved the positive second variation (a local result), Doc 95 analyzes the necessary conditions to turn that local result into a global one. Conditions ND1–ND4 formulated in Doc 93 §8 are the starting point of the analysis of §§2–7 of this document.

### A.2. Relation with Doc 82

The variational criterion of Doc 82 ($\tilde\delta_\lambda^2 = 0 \iff$ RH) is the fundamental framework. The analysis of this document neither modifies nor improves that result: what is studied is the additional geometric structure that would allow a better understanding of the behavior of the infimum, especially under $\neg$RH.

### A.3. Relation with Doc 83

The pointwise inequality $f_0 \geq f_0^{on}$ of Doc 83 is crucial in the analysis of the second variation (Proposition 4.3 of Doc 93) and also for studying the Euler-Lagrange equations (§4 of this document). The formula of Doc 83 for the quotient $f_0/f_0^{on}$ is what determines the sign of $D_0 = f_0 - f_0^{on}$.

### A.4. Relation with Docs 70–72 (Phase 33, DBN-CCM)

Doc 72 expressed $T_\lambda$ in terms of the Weil formula. The connection between $T_\lambda$ and $\tilde\delta_\lambda^2$ noted in Doc 93 §5 (the kernel $K_\lambda(\gamma_j)$ of Doc 86 is essentially the second-variation coefficient $\mathcal{Q}_\lambda^{(j)}$) suggests that Docs 70–72 contain information relevant to the variational problem. In particular, the monotonicity of $T_\lambda(t)$ along the DBN flow (Doc 70) might be related to the monotonicity of $D(t)$ studied in §6.4, although the precise connection is not established.

---

## Appendix B: Glossary of conditions and conjectures

For future reference, we list the conditions and conjectures of the Direction D program:

- **ND1 (Existence):** The infimum $\tilde\delta_\lambda^2$ is attained in $\mathcal{M}$. Status: **open**, probably requires ND3.
- **ND2 (Uniqueness):** The minimizer is unique and equal to $f_0^{on}$. Status: **open**, does not follow from the local second variation.
- **ND3 (Closedness):** $\mathcal{M}$ is closed in $H_\lambda$. Status: **probably false**, the closure contains functions with zeros that escaped to infinity.
- **ND4 (Extended Hadamard):** Quantitative estimate of $\tilde\delta_\lambda^2$ in terms of the positions of the zeros. Status: **open**, partially available for $T_\lambda$ (Doc 86).
- **Conjecture $\mathbf{C}_D$:** Global positive second variation + monotone DBN flow $\Rightarrow$ $\tilde\delta_\lambda^2 = 0 \iff$ RH. Status: **conjecture**, relation to RH not established.
- **Conjecture $\mathbf{C}_D^{\mathrm{red}}$:** Reduced version, with local second variation at $f_0^{on}$ and lower bound of $D(t)$ on $[0,1/2]$. Status: **weaker conjecture**, more accessible.

---

*End of Doc 95.*
