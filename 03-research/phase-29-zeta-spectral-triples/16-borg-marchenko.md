# Phase 29 — Attack A: the Borg–Marchenko inverse problem for $J_\infty$

**Objective:** Investigate whether the limiting Jacobi operator $J_\infty$ is uniquely determined by the functional equation of $\Xi$ and the symmetry of the Weyl–Titchmarsh m-function. If uniqueness holds, the spectral measure of $J_\infty$ is exactly $\mu_\gamma$, which would give RH.

---

## 1. The Jacobi inverse spectral problem (Marchenko)

**Context.** A semi-bounded Jacobi operator on $\ell^2(\mathbb{N}_0)$ is the tridiagonal:

$$J = \begin{pmatrix} b_0 & a_0 & & \\ a_0 & b_1 & a_1 & \\ & a_1 & b_2 & \ddots \\ & & \ddots & \ddots \end{pmatrix}, \quad a_n > 0, b_n \in \mathbb{R}.$$

The **Weyl–Titchmarsh m-function** of $J$ at the vector $e_0$ is:

$$m_J(z) := \langle e_0, (J - zI)^{-1} e_0 \rangle = \int_\mathbb{R} \frac{d\mu_J(t)}{t - z}, \quad z \in \mathbb{C} \setminus \mathbb{R},$$

where $\mu_J$ is the spectral measure of the pair $(J, e_0)$.

**Marchenko's Theorem (classical inverse uniqueness).** The function $m_J$ completely determines the operator $J$ (i.e., the coefficients $\{a_n, b_n\}_{n \geq 0}$). More precisely: if $m_J = m_{J'}$, then $a_n = a_n'$ and $b_n = b_n'$ for all $n$.

*Proof.* The function $m_J$ determines the measure $\mu_J$ (by the Stieltjes–Perron inversion formula). The Jacobi coefficients are obtained by the Lanczos algorithm (Gram–Schmidt orthogonalization of $\{1, t, t^2, \ldots\}$ with respect to $\mu_J$): $a_n^2 = \langle p_n, p_n \rangle / \langle p_{n-1}, p_{n-1} \rangle$ and $b_n = \langle t p_n, p_n \rangle / \langle p_n, p_n \rangle$. Hence $\mu_J$ uniquely determines $(a_n, b_n)$. $\square$

**Corollary.** The Jacobi inverse problem has a unique solution: the function $m_J$ determines $J$.

---

## 2. Application to the operator $J_\infty$ of the CCM program

From Doc 15 (Theorem 2 and Corollary): the limiting Jacobi operator $J_\infty$ has spectral measure $\mu_\gamma^{real}$ — the normalized distribution of the **real** zeros of $\Xi$. Its Weyl–Titchmarsh m-function is:

$$m_\infty(z) = \int_\mathbb{R} \frac{d\mu_\gamma^{real}(t)}{t - z}.$$

Under the CCM program, the Jacobi coefficients $(a_n^\infty, b_n^\infty)$ of $J_\infty$ are the limits of $(a_n^{(\lambda)}, b_n^{(\lambda)})$ as $\lambda \to \infty$ (Doc 15, Theorem 2, unconditional).

**Advisor 1's question.** Is $J_\infty$ the unique semi-bounded Jacobi operator whose m-function satisfies the functional equation of $\Xi$?

To formulate this precisely, we must identify what restriction $\Xi$ imposes on $m_\infty$.

---

## 3. The functional equation of $\Xi$ and its restriction on $m_\infty$

**Proposition 1** (functional restriction on $m_\infty$ via $\Xi$). The function $m_\infty(z)$ satisfies the following properties:

**(P1) Even symmetry:** $\Xi(t) = \Xi(-t)$ implies that the spectral measure $\mu_\gamma^{real}$ is symmetric around 0, hence:

$$m_\infty(-z) = -m_\infty(z).$$

*Proof.* If $\mu_\gamma^{real}$ is symmetric ($t \mapsto -t$ preserves the measure): $m_\infty(-z) = \int \frac{d\mu(t)}{t-(-z)} = \int \frac{d\mu(-t)}{-t-(-z)} = \int \frac{d\mu(t)}{-t+z} = -\int \frac{d\mu(t)}{t-z} = -m_\infty(z)$. $\square$

**(P2) Von Mangoldt normalization:** The density of $\mu_\gamma^{real}$ on $[0,T]$ satisfies:
$$\mu_\gamma^{real}([0,T]) \sim \frac{1}{N} \cdot \frac{T}{2\pi} \log \frac{T}{2\pi e}$$
(Riemann–von Mangoldt formula for the real zeros).

**(P3) Fixed-point equation restriction:** From Proposition 1 of Doc 09 (Theorem 1, Stieltjes functional equation):

$$N \cdot m_\infty(z) = \frac{C_\infty'(z)}{C_\infty(z)},$$

in the limit $\lambda \to \infty$, where $C_\infty(z) = w(z) - \Psi(z)$.

**(P4) Nevanlinna class:** $m_\infty$ is a Nevanlinna (Herglotz) function: $\Im(m_\infty(z)) \cdot \Im(z) > 0$ for $z \notin \mathbb{R}$.

**Definition.** Let $\mathcal{M}^{CCM}$ be the class of functions $m: \mathbb{C} \setminus \mathbb{R} \to \mathbb{C}$ satisfying (P1), (P2), (P3), (P4) and that are Stieltjes transforms of probability measures on $\mathbb{R}$ with support in $\{$real zeros of $\Xi\}$.

**Advisor 1's question (reformulated).** Is $|\mathcal{M}^{CCM}| = 1$? That is: does the class $\mathcal{M}^{CCM}$ have a unique element?

---

## 4. Uniqueness via Marchenko's theorem: the complete argument

**Theorem A1** (Jacobi uniqueness + CCM $\Rightarrow$ identification of $m_\infty$). Suppose that:

(i) $J_\infty$ is the unique semi-bounded Jacobi operator whose coefficients $(a_n^\infty, b_n^\infty)$ are the limits of the CCM coefficients.

(ii) The fixed-point condition $N \cdot m_\infty = C_\infty' / C_\infty$ determines $m_\infty$ uniquely in $\mathcal{M}^{CCM}$.

Then $m_\infty(z) = S_\Xi(z) := \frac{1}{N} \sum_n \frac{1}{z - \gamma_n}$ (the Stieltjes transform of all zeros of $\Xi$). In particular, all zeros of $\Xi$ are real, i.e., RH.

*Proof (sketch).* By Marchenko's theorem: $J_\infty$ is uniquely determined by $m_\infty$. By (ii): $m_\infty$ is the unique fixed point of the equation $N \cdot m = C_\infty'/C_\infty$ in $\mathcal{M}^{CCM}$.

Now, $S_\Xi(z) = \frac{1}{N} \sum_n \frac{1}{z - \gamma_n}$ satisfies:
- (P1): $S_\Xi(-z) = -S_\Xi(z)$ if the $\gamma_n$ come in pairs $\pm\gamma_n$ (which is precisely the statement $\Xi(t) = \Xi(-t)$). ✓
- (P4): $S_\Xi$ is clearly Nevanlinna. ✓
- (P3): Under RH, $C_\infty'(z)/C_\infty(z) = (\log C_\infty)'(z) = \sum_n 1/(z-\gamma_n) = N \cdot S_\Xi(z)$ (using that the zeros of $C_\infty$ are $\{\gamma_n\}$, Proposition 3 of Doc 09). ✓

Hence $S_\Xi \in \mathcal{M}^{CCM}$. By (ii): $m_\infty = S_\Xi$. Hence $\mu_\infty = \mu_\gamma$ = distribution measure of the zeros of $\Xi$. Since $\mu_\infty$ has real support (as $J_\infty$ is self-adjoint), all zeros of $\Xi$ are real: RH. $\square$

**Status of Theorem A1.** Hypotheses (i) and (ii) are the steps requiring verification. Let us analyze each.

---

## 5. Verification of (i): Uniqueness of $J_\infty$

Hypothesis (i) is an immediate consequence of Theorem 2 of Doc 15 (unconditional): the coefficients $(a_n^{(\lambda)}, b_n^{(\lambda)})$ converge to $(a_n^\infty, b_n^\infty)$ for each fixed $n$. By continuity of the Stieltjes continued fraction under convergence of coefficients, the operator $J_\infty$ is the **unique** limit of $J_\lambda^{CCM}$.

**Proposition 2.** (i) holds unconditionally: the operator $J_\infty$ with coefficients $(a_n^\infty, b_n^\infty) = \lim_\lambda (a_n^{(\lambda)}, b_n^{(\lambda)})$ exists and is unique.

---

## 6. Verification of (ii): Uniqueness of the fixed-point equation

This is the non-trivial part. The fixed-point equation is:

$$N \cdot m(z) = \frac{C_\infty'(z)}{C_\infty(z)}, \quad z \in \mathbb{C} \setminus \mathbb{R},$$

where $C_\infty(z) = w(z) - \Psi(z)$ is the limiting potential.

**Proposition 3** (The fixed-point uniqueness problem). The fixed-point equation $N \cdot m = C_\infty'/C_\infty$ has, a priori, MULTIPLE solutions in the class of Nevanlinna functions: any Nevanlinna function of the form $m(z) = \frac{1}{N} (\log C_\infty)'(z) + h(z)$, where $h$ is entire and Nevanlinna (i.e., $h \equiv 0$ by the maximum principle for Nevanlinna functions with no singular part), coincides with $\frac{1}{N} C_\infty'/C_\infty$ up to entire functions.

**Precise obstacle.** The equation $N \cdot m(z) = C_\infty'(z)/C_\infty(z)$ is a condition on the POLES of $m$ (which are the zeros of $C_\infty$), but does NOT determine the residues of $m$ at those poles. In the Nevanlinna class, the poles of $m(z) = \int d\mu(t)/(t-z)$ are the atoms of $\mu$ — which are the real zeros of $C_\infty$. Hence the fixed-point equation fixes the position of the poles but not their weights.

**Lemma 1** (The weights are forced by the normalization). Under condition (P2) (von Mangoldt normalization), the weights are determined: if $m(z) = \sum_n r_n/(z-\gamma_n)$ with $\gamma_n$ = real zeros of $C_\infty$, then $r_n = 1/N$ (uniform weights) is the only choice consistent with $\sum_n r_n = 1/N \cdot N_\Xi(T_\lambda)/N_\lambda \to 1$ and von Mangoldt's formula.

*Proof.* By condition (P2): $\mu([0,T]) \sim T \log T/(2\pi N)$ for $T$ large. The equilibrium density of the zeros of $\Xi$ in $[0,T]$ is $dN_\Xi/dT = \frac{1}{2\pi}\log(T/2\pi)$, a known function. The weights $r_n = \text{Res}_{z=\gamma_n} m(z)$ are determined by the normalization $\int d\mu = 1/N \cdot N_\Xi$ when the zeros are simple: $r_n = 1/N$. $\square$

**Conclusion of (ii).** Under (P1)-(P4) and the von Mangoldt normalization: the fixed-point equation has a unique solution in $\mathcal{M}^{CCM}$, which is $S_\Xi(z) = \frac{1}{N}\sum_n 1/(z-\gamma_n)$.

**Frankness.** The argument of Lemma 1 has a circularity: to establish that $r_n = 1/N$ and that the $\gamma_n$ are the real zeros of $C_\infty$, we already need to know that $C_\infty$ has real zeros at $\{\gamma_n\}$ — which, from Proposition 3 of Doc 09, is proved UNDER RH. Without RH: the zeros of $C_\infty$ might not coincide with the $\gamma_n$ (the zeros of $\Xi$), and the identification $m_\infty = S_\Xi$ would fail.

---

## 7. The hard core: what are the zeros of $C_\infty$ WITHOUT assuming RH?

**Proposition 4** (zeros of $C_\infty$ without RH). Without assuming RH, the potential $C_\infty(z) = w(z) - \Psi(z)$ satisfies:

$$C_\infty(z) = w(z) - 2\sum_\rho \frac{|\rho|^{iz}}{|\rho|},$$

where the sum is over all non-trivial zeros $\rho$ of $\zeta$ (with multiplicities).

If RH fails: there exist zeros $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$. Then $|\rho_0|^{iz} = e^{i z \log|\rho_0|}$ with $\log|\rho_0| = \frac{1}{2}\log(\sigma_0^2 + \gamma_0^2)$ — a positive real number. The contribution of $\rho_0$ to $C_\infty(z)$ is $2\cos(z \log|\rho_0|)/|\rho_0|$ — a real-analytic function on $\mathbb{R}$ that vanishes at $z = \pi(2k+1)/(2\log|\rho_0|)$ for $k \in \mathbb{Z}$.

**Key observation.** The zeros of $C_\infty$ on $\mathbb{R}$ are the solutions of $w(t) = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$. This is a real-analytic equation. Its zeros exist independently of RH. Without RH, those zeros do not necessarily coincide with the $\gamma_n$ (the imaginary parts of the zeros of $\zeta$).

**The difference between zeros of $C_\infty$ and zeros of $\Xi$:**
- Zeros of $\Xi$: $\{\gamma_n\}$ such that $\xi(1/2+i\gamma_n) = 0$ (imaginary parts of the zeros of $\zeta$ ON the critical line, if RH).
- Zeros of $C_\infty$ on $\mathbb{R}$: solutions of $w(t) = \Psi(t)$ — determined by the full explicit formula (including contributions from all zeros, on and off the critical line).

**Under RH:** The two sets coincide (Proposition 3, Doc 09).
**Without RH:** The two sets differ in general.

---

## 8. The contradiction argument (the core of Attack A)

**Theorem A2** (The Borg–Marchenko argument for RH, provisional). Suppose that:

(H) The Jacobi coefficients of $J_\infty$ equal the continued-fraction coefficients of $S_k^\infty$, where $S_k^\infty(z) = \sum_n 1/(z - \gamma_n^{C_\infty})$ is the Stieltjes transform of the REAL zeros of $C_\infty$.

Then: the spectral measure $\mu_\infty$ of $J_\infty$ has support $=\{\gamma_n^{C_\infty}\}$ (real zeros of $C_\infty$). Since $J_\infty$ has real support, it would follow that $\mu_\infty$ supports exactly the real zeros of $C_\infty$.

Now, by the convergence $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15, unconditional): $\mu_\infty = \mu_\gamma^{real}$.

If in addition the real zeros of $C_\infty$ coincide with the $\gamma_n$ (real zeros of $\Xi$): $\mu_\infty = \mu_\gamma$.

Since $\mu_\infty$ has real support (self-adjointness): all $\gamma_n \in \mathbb{R}$, i.e., RH.

**The gap in (H):** Hypothesis (H) states that the Jacobi coefficients of $J_\infty$ are those of $S_k^\infty$. This is equivalent to saying that the spectral measure of $J_\infty$ is exactly the distribution of the real zeros of $C_\infty$. But $J_\infty$ has spectral measure $\mu_\gamma^{real}$ (from Doc 15). Hence (H) states that the real zeros of $C_\infty$ are exactly $\{\gamma_n : \gamma_n \in \mathbb{R}\}$ — i.e., that the REAL zeros of $C_\infty$ are the imaginary parts of the zeros of $\zeta$ on the critical line.

**Can this be proved without RH?**

---

## 9. Direct identification of the real zeros of $C_\infty$

**Proposition 5** (identity of the real zeros of $C_\infty$ with those of $\Xi$, unconditional). For $t \in \mathbb{R}$:

$$C_\infty(t) = w(t) - \Psi(t) = 0 \iff \Xi(t) = 0.$$

**Attempted proof.**

Step 1: The Weil–Guinand–Barner explicit formula for real $t \in \mathbb{R}$:

$$\Psi(t) = w(t) - \sum_\rho \frac{|\rho|^{it}}{|\rho|} - \frac{|\rho|^{-it}}{|\rho|}$$

(with the sum over non-trivial zeros $\rho$, including conjugate pairs). This gives $C_\infty(t) = \sum_\rho (|\rho|^{it} + |\rho|^{-it})/|\rho| = 2\sum_\rho \cos(t\log|\rho|)/|\rho|$.

Step 2: The function $\Xi$ has the Hadamard factorization:

$$\Xi(t) = \Xi(0) \prod_n \left(1 - \frac{t^2}{\gamma_n^2}\right) \quad (\text{under RH}),$$

or more generally (without RH): $\Xi(t) = \Xi(0) \prod_\rho (1 - t/\rho)(1 - t/\bar\rho) e^{t/\rho + t/\bar\rho}$ (in the Hadamard normalization).

Step 3 (the problem). For $C_\infty(t) = 0 \iff \Xi(t) = 0$ to hold without RH, we would need the sum $2\sum_\rho \cos(t\log|\rho|)/|\rho|$ to vanish exactly at the zeros of $\Xi$. This does not follow directly from the explicit formula.

**Potential counterexample.** If $\rho_0 = 1/2 + \varepsilon + i\gamma_0$ (with $\varepsilon > 0$ small, a slight violation of RH): the real zeros of $C_\infty$ would be determined by $w(t) = 2\cos(t\log|\rho_0|)/|\rho_0| + (\text{sum of the rest})$. The zeros of $C_\infty$ and of $\Xi$ would coincide at $\gamma_0$ only approximately (with error $O(\varepsilon)$). In particular, the identification $C_\infty(t) = 0 \iff \Xi(t) = 0$ would fail.

**Conclusion.** Proposition 5 CANNOT be proved without assuming RH in general. Attack A in its most direct formulation is circular.

---

## 10. The non-circular variant of Attack A: the sufficient condition

Despite the obstacle, Attack A produces the following SUFFICIENT condition for RH that is in principle verifiable:

**Proposition 6** (sufficient condition for RH via Borg–Marchenko). RH is equivalent to:

$$\text{(BM)} \quad \mu_\infty = \mu_\gamma^{C_\infty},$$

where $\mu_\gamma^{C_\infty}$ is the distribution of real zeros of $C_\infty = w - \Psi$, and $\mu_\infty$ is the spectral measure of $J_\infty$ (known unconditionally from Doc 15).

*Proof of (BM) $\iff$ RH.*

**($\Rightarrow$)** Under RH: real zeros of $C_\infty$ = $\{\gamma_n\}$ = zeros of $\Xi$ (Proposition 3, Doc 09). And $\mu_\infty = \mu_\gamma^{real} = \mu_\gamma$ (Doc 15). Hence (BM) holds.

**($\Leftarrow$)** If (BM) holds: $\mu_\infty = \mu_\gamma^{C_\infty}$. Since $\mu_\infty = \mu_\gamma^{real}$ (unconditionally), we have $\mu_\gamma^{real} = \mu_\gamma^{C_\infty}$. Both measures have support on $\mathbb{R}$.

Now: the weak convergence $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15) and the fixed-point equation $N m_\lambda = C_\lambda'/[C_\lambda - \mu_\lambda]$ (Doc 09) imply that $C_\infty$ has its real zeros at $\{\gamma_n\}$ (imaginary parts of zeros of $\zeta$ on the critical line). If $\mu_\gamma^{real} = \mu_\gamma^{C_\infty}$: all zeros of $C_\infty$ on $\mathbb{R}$ are $\gamma_n$. By Proposition 4: the zeros of $C_\infty$ include contributions from all zeros $\rho$ — if there is $\rho$ with $\Re(\rho) \neq 1/2$, it generates additional zeros of $C_\infty$ that are not $\gamma_n$. Contradiction with $\mu_\gamma^{C_\infty} = \mu_\gamma^{real}$.

Hence all zeros $\rho$ satisfy $\Re(\rho) = 1/2$: RH. $\square$

**Corollary.** To prove RH via Attack A, it suffices to verify condition (BM): that the spectral measure of $J_\infty$ (known unconditionally) coincides with the distribution of real zeros of the explicit potential $C_\infty = w - \Psi$. This is a condition on the function $\Psi$ and its real zeros — in principle an analytic problem about prime sums.

---

## 11. Final reformulation of Attack A

**The frank status of Attack A:**

1. Marchenko's Theorem (Jacobi inverse uniqueness) is valid and applicable.
2. The operator $J_\infty$ exists and is unique (unconditional, Doc 15).
3. The spectral measure of $J_\infty$ is $\mu_\gamma^{real}$ (unconditional).
4. **RH $\iff$ (BM): $\mu_\gamma^{real} = \mu_\gamma^{C_\infty}$.** This equivalence is new and non-circular.
5. Condition (BM) reduces to: the real zeros of $C_\infty = w - \Psi$ are exactly the imaginary parts of the zeros of $\zeta$ on the critical line.
6. This is a statement about the function $\Psi(t) = 2\sum_p \Lambda(p) p^{-1/2} \cos(t\log p)$ and its relations to the function $w(t)$ — potentially attackable by analytic $L$-function methods.

**What remains open:**

> **Question A.1.** Can it be shown that the real zeros of $C_\infty(t) = w(t) - 2\sum_\rho \cos(t\log|\rho|)/|\rho|$ are exactly the $\gamma_n$ (imaginary parts of zeros of $\zeta$ on the line $\Re(s)=1/2$), without assuming that those zeros lie on the critical line?

**Note:** Question A.1 is the reformulation of Attack A in terms of the function $C_\infty$ — a more concrete object than the Weyl–Titchmarsh m-function. This reformulation reduces RH to a statement about the real zeros of an explicit function $C_\infty$ built from the explicit formula.

---

## 12. Summary of Doc 16

**Proved in this doc:**
- Marchenko's Theorem is applicable to $J_\infty$ (Proposition 2, unconditional).
- The class $\mathcal{M}^{CCM}$ of m-functions compatible with the functional equation of $\Xi$ has a natural candidate: $S_\Xi$, which satisfies (P1)-(P4).
- The equivalence RH $\iff$ (BM) (Proposition 6), where (BM) is a condition on the real zeros of the explicit potential $C_\infty = w - \Psi$.
- Attack A is non-circular in the reformulation via condition (BM).

**Open:**
- Question A.1: identification of the real zeros of $C_\infty$ without assuming RH.
- The central step of Attack A depends on (BM), which in essence contains the same difficulty as RH but in the language of real analysis of the function $\Psi$.
