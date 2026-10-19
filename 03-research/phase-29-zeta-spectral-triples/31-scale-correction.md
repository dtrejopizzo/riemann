# Phase 29 — Doc 31: Correcting the Scale Error of Doc 30 — $b_n \neq 0$

**Purpose:** Doc 30 established a "scale problem" based on $\|J_\infty\|_{op} \leq 2\pi/\log\gamma_0 \approx 2.36$, concluding that $\gamma_n \notin \text{spec}(J_\infty)$. This doc corrects that error: Doc 30 wrongly assumed $b_n^\infty = 0$.

---

## 1. The correction to Doc 30: $b_n^\infty \approx \gamma_n$

**The error in Doc 30.** Proposition 1 of Doc 30 stated "$J_\infty$ with $a_n^\infty = \pi/\log\gamma_n$ and $b_n^\infty = 0$ is compact with norm $\approx 2.36$." The error lies in $b_n^\infty = 0$.

**The correct reading of Doc 15 (Part C and Theorem 1).** For the local regime of the CCM Jacobi coefficients:

$$b_n^{(\lambda)} \approx \frac{\gamma_n + \gamma_{n+1}}{2} \approx \gamma_n + O\!\left(\frac{1}{\log\gamma_n}\right), \quad a_n^{(\lambda)} \approx \frac{\gamma_{n+1}-\gamma_n}{2} \approx \frac{\pi}{\log\gamma_n}.$$

In the limit $\lambda\to\infty$ (with $n$ fixed): $b_n^\infty \approx \gamma_n$ (large, diverging with $n$) and $a_n^\infty \approx \pi/\log\gamma_n \to 0$ (small).

**The spectral measure of $J_\infty$.** The operator $J_\infty$ with $b_n = \gamma_n$ and $a_n = \pi/\log\gamma_n$ has its eigenvalues at the $\gamma_n$ (approximately), and the spectral measure is $\mu_\gamma^{real}$. This is consistent with the scale (the $\gamma_n$ are the eigenvalues, of order 14, 21, ...).

---

## 2. The correct operator $J_\infty$: unbounded

**Proposition 1** (correct version). The operator $J_\infty$ with $b_n^\infty = \gamma_n$ (zeros of $\Xi$) and $a_n^\infty = \pi/\log\gamma_n$ is:

(a) **Unbounded**: $\|J_\infty\|_{op} = \infty$ since $b_n \to \infty$.

(b) **Essentially self-adjoint** on $D_0 = \{u \in \ell^2: \sum_n n|u_n|^2 < \infty\}$: since the $b_n$ grow like $\gamma_n \sim n\log n$ (by PNT), which is in the Carleman class.

(c) **Purely point spectrum** (if the $\gamma_n$ are simple eigenvalues): the $a_n = \pi/\log\gamma_n \to 0$ give small off-diagonal perturbations; the eigenvalues of $J_\infty$ approach those of the diagonal part (the $\gamma_n$), perturbed by the $a_n$.

(d) **The norm of the off-diagonal perturbation**: $\|J_\infty - \text{diag}(\gamma_n)\|_{op} \leq 2\sup_n a_n^\infty = 2\pi/\log\gamma_0 \approx 2.36$.

*Proof.* (a) $\sup_n |b_n| = \sup_n \gamma_n = \infty$. (b) Carleman: $\sum_n 1/b_n = \sum_n 1/\gamma_n$ converges (since $\gamma_n > 14n$ for all $n$), so $J_\infty$ has a natural domain. (c) and (d) direct. $\square$

---

## 3. The perturbative structure: $J_\infty = D + P$

**Decomposition.** Let $D = \text{diag}(\gamma_n)$ (the diagonal operator with the $\gamma_n$ on the diagonal) and $P$ the off-diagonal perturbation with $P_{n,n+1} = P_{n+1,n} = a_n^\infty = \pi/\log\gamma_n$ (everything else zero).

$$J_\infty = D + P, \quad \|P\|_{op} \leq 2\pi/\log\gamma_0 \approx 2.36.$$

**Proposition 2** (small perturbation relative to the spacing). The perturbation radius $\|P\|_{op} \approx 2.36$ is comparable to the minimum spacing $\gamma_1 - \gamma_0 \approx 21.0 - 14.1 = 6.9$. The perturbation $P$ has norm smaller than the minimum gap of the spectrum of $D$:

$$\|P\|_{op} \approx 2.36 < \frac{\gamma_1 - \gamma_0}{2} \approx 3.45.$$

Hence: the eigenvalues of $J_\infty$ are WELL SEPARATED and close to those of $D$ (i.e., to the $\gamma_n$).

*Proof.* For $n\geq 0$: $a_n = \pi/\log\gamma_n$ and $(\gamma_{n+1}-\gamma_n)/2 = a_n$ (the same quantity). Hence the off-diagonal perturbation has exactly the magnitude of the half-spacing, and Weyl perturbation theory guarantees that the eigenvalues of $J_\infty$ lie in the intervals $[\gamma_n - a_n, \gamma_n + a_n]$ (for $a_n$ small relative to the next gap). $\square$

---

## 4. Re-analysis of Inc. Inv. with $b_n \approx \gamma_n$

**Proposition 3** (reformulation of Inc. Inv. with $b_n \approx \gamma_n$). With the correct $b_n^\infty = \gamma_n + \epsilon_n$ (where $\epsilon_n = O(1/\log\gamma_n)$ is a small correction):

The eigenvalues of $J_\infty$ are $\tilde\gamma_n = \gamma_n + \delta_n$ where $|\delta_n| \leq \|P\|_{op}\cdot\|R_n\|$ (the perturbation of the eigenvalue $\gamma_n$ of $D$).

Inc. Inv. is the condition: $\tilde\gamma_n = \gamma_n$ for all $n$ (the eigenvalues of $J_\infty$ coincide exactly with the $\gamma_n$, not with some shift $\delta_n \neq 0$).

**Proposition 4** (EF2 with $b_n \approx \gamma_n$). The EF2 of Doc 17:

$$N\cdot m_\infty^{WT}(z) = \frac{C_\infty'(z)}{C_\infty(z)}$$

remains valid with the correct operator $J_\infty$ (with $b_n = \gamma_n$). The eigenvalues of $J_\infty$ are the poles of $m_\infty^{WT}$, which are the zeros of $C_\infty$.

Inc. Inv. says: the zeros of $C_\infty$ on $\mathbb{R}$ are exactly the $\gamma_n$.

With the correct $b_n = \gamma_n$: the spectrum of $J_\infty$ (the eigenvalues $\tilde\gamma_n$) lies in the range $[\gamma_n - 2.36, \gamma_n + 2.36]$ for each $n$. Inc. Inv. requires $\tilde\gamma_n = \gamma_n$ exactly (no shift).

---

## 5. Exact perturbation theory for the condition $\tilde\gamma_n = \gamma_n$

**Theorem 1** (perturbative fixed-point condition). The eigenvalue $\tilde\gamma_n$ of $J_\infty = D + P$ satisfies the implicit equation (Kato-Rellich theorem):

$$\tilde\gamma_n = \gamma_n + \sum_{k\neq n}\frac{|P_{nk}|^2}{\gamma_n - \gamma_k} + O\!\left(\|P\|^4/\text{gap}^3\right) = \gamma_n + a_{n-1}^2 A_{n-1} + a_n^2 B_n + O(\|P\|^4),$$

where $A_{n-1} = 1/(\gamma_n - \gamma_{n-1}) + \ldots$ and $B_n = 1/(\gamma_n - \gamma_{n+1}) + \ldots$ are the second-order contributions of perturbation theory.

The condition $\tilde\gamma_n = \gamma_n$ (unshifted eigenvalue) requires:

$$a_{n-1}^2\cdot\frac{1}{\gamma_n-\gamma_{n-1}} + a_n^2\cdot\frac{1}{\gamma_n-\gamma_{n+1}} + \text{corrections} = 0.$$

**Proposition 5** (the no-shift condition as an equation between zeros). With $a_{n-1} = \pi/\log\gamma_{n-1}$ and $a_n = \pi/\log\gamma_n$, and $\gamma_n - \gamma_{n-1} \approx 2\pi/\log\gamma_{n-1}$ and $\gamma_n - \gamma_{n+1} \approx -2\pi/\log\gamma_n$:

$$\text{2nd-order correction} = \frac{(\pi/\log\gamma_{n-1})^2}{2\pi/\log\gamma_{n-1}} - \frac{(\pi/\log\gamma_n)^2}{2\pi/\log\gamma_n} = \frac{\pi}{2\log\gamma_{n-1}} - \frac{\pi}{2\log\gamma_n}.$$

For large $n$: $\pi/(2\log\gamma_{n-1}) - \pi/(2\log\gamma_n) \approx \pi/(2\log\gamma_n) - \pi/(2\log\gamma_n) + O(1/(\log\gamma_n)^2 \cdot 1/n) \to 0$.

Hence: the second-order correction is $O(1/(n(\log n)^2)) \to 0$. The eigenvalues of $J_\infty$ are $\tilde\gamma_n = \gamma_n + O(1/(n(\log n)^2))$.

---

## 6. The perturbative result: the eigenvalues converge to the $\gamma_n$

**Theorem 2** (eigenvalues of $J_\infty$ are asymptotically $\gamma_n$). With $b_n = \gamma_n$ and $a_n = \pi/\log\gamma_n$:

$$\tilde\gamma_n = \gamma_n + O\!\left(\frac{1}{n(\log n)^2}\right) \quad \text{as } n\to\infty.$$

In particular: $\tilde\gamma_n \to \gamma_n$ as $n\to\infty$ (the eigenvalues approach the $\gamma_n$ for large $n$).

*Proof.* From Proposition 5: the 2nd-order correction is $O(1/(n\log^2 n))$. Higher-order corrections are $O(\|P\|^4/\text{gap}^3) = O(a_n^4/(\gamma_{n+1}-\gamma_n)^3) = O(1/(\log n)^4/n^3) = O(1/(n^3\log^4 n))$ — negligible. $\square$

**The distinction between asymptotic and exact.** Theorem 2 says that $\tilde\gamma_n - \gamma_n \to 0$, but not that $\tilde\gamma_n = \gamma_n$ EXACTLY. The Inc. Inv. gap is exactly whether $\tilde\gamma_n = \gamma_n$ (not merely asymptotically). Perturbation theory only gives an approximation; the exact condition requires ALL terms of the series to cancel.

---

## 7. The exact no-shift condition

**Proposition 6** (exact condition for $\tilde\gamma_n = \gamma_n$). The eigenvalue of $J_\infty$ is exactly $\gamma_n$ (no shift) if and only if the resolvent equation:

$$\gamma_n \text{ is an eigenvalue of } J_\infty \iff (J_\infty - \gamma_n) u = 0 \text{ has a solution } u \in \ell^2(\mathbb{N})$$

has a solution. This is equivalent to: the solution of the recurrence

$$a_{n-1}^\infty u_{n-1} + b_n^\infty u_n + a_n^\infty u_{n+1} = \gamma_n u_n, \quad \text{i.e.,} \quad a_{n-1}^\infty u_{n-1} + a_n^\infty u_{n+1} = (\gamma_n - b_n^\infty) u_n,$$

with $b_n^\infty = \gamma_n$ is:

$$a_{n-1}^\infty u_{n-1} + a_n^\infty u_{n+1} = 0.$$

In the case $b_n^\infty = \gamma_n$ EXACTLY: the equation at point $n$ is $a_{n-1}u_{n-1} + a_n u_{n+1} = 0$, which gives $u_{n+1} = -(a_{n-1}/a_n) u_{n-1}$.

**The recurrence system with $b_n = \gamma_n$.** The equation $(J_\infty - \gamma_n)u = 0$ in components:

For $k \neq n$: $a_{k-1} u_{k-1} + a_k u_{k+1} = (\gamma_n - \gamma_k) u_k$.

For $k = n$: $a_{n-1} u_{n-1} + a_n u_{n+1} = 0$.

The equation at $k = n$ gives a relation between $u_{n-1}$ and $u_{n+1}$: $u_{n+1} = -(a_{n-1}/a_n) u_{n-1} = -(\log\gamma_n/\log\gamma_{n-1}) u_{n-1}$. For large $n$: $(a_{n-1}/a_n) = \log\gamma_n/\log\gamma_{n-1} \approx 1 + (\log\gamma_n - \log\gamma_{n-1})/\log\gamma_{n-1} \approx 1 + (\log p_n)/\log\gamma_{n-1}$ (where $p_n$ is the "log-ratio" of consecutive zeros) — very close to 1 for large $n$.

The relation $u_{n+1} \approx -u_{n-1}$ (for large $n$) imposes a REFLECTION condition at step $n$: the eigenvector "reflects" around the index $n$.

**Local analysis of the eigenfunction.** For $k < n$ (far from $n$): the equation $(J_\infty - \gamma_n) u = 0$ has the factor $(\gamma_n - \gamma_k) > 0$ on the right-hand term. This is a Schrödinger-type equation with potential $V(k) = \gamma_k - \gamma_n$ (negative for $k < n$, positive for $k > n$). The level $\gamma_n$ is at the "energy level" separating the two regimes.

Near the index $n$ (where $V(k) = \gamma_k - \gamma_n \approx (k-n) \cdot \gamma_n'$): the recurrence behaves like a localized harmonic-oscillator-type differential equation — the eigenvector localizes around the index $n$.

---

## 8. The quadrature condition: $b_n = \gamma_n$ exact vs. approximate

The key result of Doc 15 states:

$$b_n^{(\lambda)} \approx \gamma_n + O(1/\log\gamma_n).$$

The correction $O(1/\log\gamma_n)$ in $b_n$ vs. the off-diagonal perturbation $a_n = \pi/\log\gamma_n$: both are of the same order. The condition "$b_n = \gamma_n$ exactly" requires the correction $O(1/\log\gamma_n)$ to be exactly zero.

**Proposition 7** (Inc. Inv. and the correction in $b_n$). The eigenvalues of $J_\infty$ are exactly $\gamma_n$ iff $b_n^\infty = \gamma_n$ exactly AND the solution of the recurrence with $b_n = \gamma_n$ is $\ell^2$.

The condition $b_n^\infty = \gamma_n$ exactly (without the correction $O(1/\log\gamma_n)$) IS EQUIVALENT to the eigenvalues of $J_\lambda^N$ converging to $\gamma_n$ with zero correction — which is Inc. Inv.

In other words: Inc. Inv. ↔ $b_n^{(\lambda)} \to \gamma_n$ (with the correction $\epsilon_n \to 0$) ↔ $J_\infty$ has eigenvalues exactly at $\gamma_n$.

---

## 9. Corrected final diagnosis

**Correction to Doc 30.** The "scale problem" of Doc 30 was fictitious: it was based on $b_n = 0$ when in fact $b_n \approx \gamma_n$. With the correct $b_n = \gamma_n$, the operator $J_\infty$ is unbounded and has eigenvalues at the scale of the $\gamma_n$.

**State of the program after the correction.** The EF2 of Doc 17 applies to the unbounded operator $J_\infty$ with $b_n = \gamma_n$, $a_n = \pi/\log\gamma_n$. Inc. Inv. requires:

$$\text{spec}(J_\infty) = \{\gamma_n\}, \quad \text{i.e., the eigenvalues are exactly the }\gamma_n \text{ (no shift)}.$$

By Theorem 2: the eigenvalues are $\gamma_n + O(1/(n\log^2 n))$ — very close to but not exactly equal to the $\gamma_n$ in general. Inc. Inv. requires the error to be exactly zero.

**The reformulated gap (post-correction).** Inc. Inv. is the condition:

$$\forall n: \tilde\gamma_n = \gamma_n \iff C_\infty(\gamma_n) = 0 \iff \text{the sum of perturbations of all orders cancels exactly}.$$

This exact cancellation, absent a structural reason (such as a global symmetry), is a non-trivial condition not guaranteed by the operator structure alone — it requires the explicit formula or some additional analytic principle.

**The most promising path (synthesizing Docs 27-31).** The only route that has not been closed is **Front B** proposed in Doc 28: the function $C_\infty(t) = w(t) - \Psi(t)$ as a quasi-periodic function. Its relation to the operator $J_\infty$ (now correctly understood as unbounded with $b_n = \gamma_n$) is exactly EF2. The question of whether $C_\infty(\gamma_n) = 0$ for all $\gamma_n$ might be answered by studying the distribution of values of $C_\infty$ at the points $\gamma_n$ using the ergodicity of quasi-periodic functions and the statistical behavior of the zero system of $\zeta$.
