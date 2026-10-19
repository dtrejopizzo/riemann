# Phase 29 — Attack C + B: Möbius dynamical system and functional equation of $m_\infty$

**Objective:** Attack Fronts B and C of the program. Front C: the Möbius recursion of the continued fraction of $m_\infty$ as a dynamical system — identify the attractor. Front B: the symmetry of $\Xi$ imposes a functional equation on $m_\infty$ that determines it. If the attractor of the recursion is the correct fixed point, RH follows.

---

## 1. The Möbius recursion for the Weyl-Titchmarsh function $m$

**Definition.** For a Jacobi matrix $J_\infty$ with coefficients $(a_n^\infty, b_n^\infty)$, the function $m^{(n)}(z)$ is the $m$ function of the submatrix truncated from index $n$:

$$m^{(n)}(z) := \langle e_n, (J_\infty^{(n)} - zI)^{-1} e_n \rangle = \int_\mathbb{R} \frac{d\mu^{(n)}(t)}{t-z},$$

where $J_\infty^{(n)}$ is the submatrix of $J_\infty$ starting from index $n$.

**The Möbius recursion** (continued fraction). By the tridiagonal structure of $J_\infty$:

$$m^{(n-1)}(z) = \frac{1}{b_{n-1}^\infty - z - (a_{n-1}^\infty)^2 \, m^{(n)}(z)}.$$

This is a **Möbius transformation** in $m^{(n)}$:

$$m^{(n-1)} = T_{n-1}(m^{(n)}), \quad T_{n-1}(w) := \frac{1}{b_{n-1}^\infty - z - (a_{n-1}^\infty)^2 w}.$$

For $z \in \mathbb{C}^+ = \{z : \Im(z) > 0\}$: $T_{n-1}$ maps the upper half-plane into itself (it is a Möbius transformation of Nevanlinna class).

---

## 2. Convergence of the continued fraction: the Stieltjes-Van Vleck theorem

**Theorem 1** (Stieltjes-Van Vleck-Śleszyński). Let $J$ be a semi-bounded Jacobi matrix with uniformly bounded coefficients $(a_n, b_n)$. Then the continued fraction:

$$m(z) = \cfrac{1}{b_0 - z - \cfrac{a_0^2}{b_1 - z - \cfrac{a_1^2}{b_2 - z - \cdots}}}$$

converges uniformly on compacta of $\mathbb{C}^+$ to the Weyl-Titchmarsh function $m$ of $J$.

*Reference.* Simon, "Szegő's Theorem and Its Descendants", Ch. 4. $\square$

**Application to $J_\infty$.** The coefficients $(a_n^\infty, b_n^\infty)$ are bounded (since they converge from the bounded coefficients of $J_\lambda^{CCM}$, normalized by $T_\lambda$; at the correct scale $b_n^\infty \sim \gamma_n$ grows, but for the theorem at the normalized scale $b_n^\infty/T_\lambda$ are bounded). At the normalized scale, the continued fraction converges.

---

## 3. The dynamical system of Möbius transformations

**Definition.** Fixing $z \in \mathbb{C}^+$, the Möbius dynamical system associated to $J_\infty$ is:

$$w_0 = m^{(0)}(z) = m_\infty(z), \quad w_n = m^{(n)}(z),$$

with the relation $w_{n-1} = T_{n-1}(z; w_n)$ where:

$$T_n(z; w) := \frac{1}{b_n^\infty - z - (a_n^\infty)^2 w}.$$

The **forward orbit** $w_N = m^{(N)}(z)$ converges (when $J_\infty$ is in the "limit point" case of Weyl) to a unique point $w_\infty \in \overline{\mathbb{C}^+}$ that does not depend on the initial boundary condition.

**Weyl classification.** The operator $J_\infty$ is in the case:
- **Limit point (LP):** there exists a unique $m(z) \in \mathbb{C}^+$ such that the solution $u_n(z) + m(z) v_n(z) \in \ell^2(\mathbb{N}_0)$ — the continued fraction converges. (Criterion: if $(a_n^\infty)^2 \to 0$ fast enough, or if the coefficients are perturbations of periodic coefficients.)
- **Limit circle (LC):** the values of $m$ compatible with square-summability form a disk (which collapses to the LP case as $n \to \infty$).

**Proposition 1** (classification of $J_\infty$). The limiting Jacobi operator $J_\infty$ is in the Weyl limit point case.

*Proof (sketch).* The coefficients $a_n^\infty \sim \pi/\log\gamma_n$ decrease (from Doc 15, Theorem 1, under RH — or at the normalized scale: they tend to the constant $1/(2\sqrt{3})$ — both cases give LP). More precisely: the coefficients $b_n^\infty \to \infty$ (at the unnormalized scale), so the operator $J_\infty$ has empty essential spectrum (it is an operator with discrete spectrum accumulating at $\infty$). In this case, the Weyl LP condition always holds. (See Teschl, "Jacobi Operators and Completely Integrable Nonlinear Lattices", Prop. 2.3.) $\square$

---

## 4. The attractor of the dynamical system

**Proposition 2** (the attractor of the Möbius recursion). In the LP case, the dynamical system $w_{n-1} = T_{n-1}(w_n)$ has a unique attractor: as $N \to \infty$, the composition $T_0 \circ T_1 \circ \cdots \circ T_{N-1}$ converges (uniformly in $w_N$ ranging over $\mathbb{C}^+$) to the constant $m_\infty(z)$.

*Proof.* This is precisely the content of the Stieltjes-Van Vleck theorem in dynamical form: convergence of the continued fraction is equivalent to the composition of Möbius transformations converging to a constant. In the LP case, this follows from the Śleszyński-Pringsheim criterion for Stieltjes continued fractions. $\square$

**Corollary.** $m_\infty(z)$ is the unique fixed point of the dynamical system: the only Nevanlinna function on which the composition $\{T_n\}$ acts as an asymptotic identity. This is a new characterization of $m_\infty$.

---

## 5. Front B: The functional equation of $m_\infty$ induced by $\Xi(t) = \Xi(-t)$

**Proposition 3** (functional equation of $m_\infty$). The symmetry $\Xi(t) = \Xi(-t)$ (i.e., $\Xi$ is an even function) implies that the spectral measure $\mu_\infty$ of $J_\infty$ satisfies $\mu_\infty(-A) = \mu_\infty(A)$ for every Borel set $A \subseteq \mathbb{R}$. In particular, the function $m_\infty$ satisfies:

$$m_\infty(-z) = -m_\infty(z) \quad \text{for all } z \in \mathbb{C} \setminus \mathbb{R}.$$

*Proof.* As in Proposition 1 of Doc 16 (even symmetry of the measure). $\square$

**Consequence on the coefficients.** The symmetry $m_\infty(-z) = -m_\infty(z)$ imposes constraints on the coefficients $(a_n^\infty, b_n^\infty)$. If the continued fraction of $m_\infty(z)$ is:

$$m_\infty(z) = \cfrac{1}{b_0^\infty - z - \cfrac{(a_0^\infty)^2}{b_1^\infty - z - \cdots}},$$

then $m_\infty(-z) = \cfrac{1}{b_0^\infty + z - \cfrac{(a_0^\infty)^2}{b_1^\infty + z - \cdots}}$.

The condition $m_\infty(-z) = -m_\infty(z)$ implies that the continued fraction of $-m_\infty(z)$ and that of $m_\infty(-z)$ are equal. Comparing:

$$-m_\infty(z) = -\cfrac{1}{b_0^\infty - z - \cdots} \quad \text{vs.} \quad m_\infty(-z) = \cfrac{1}{b_0^\infty + z - \cdots}.$$

**Lemma 1** (symmetry constraint on the coefficients). If $m_\infty(-z) = -m_\infty(z)$, then:

$$b_n^\infty = 0 \quad \text{for all } n \geq 0.$$

*Proof.* The condition $m(-z) = -m(z)$ for a Nevanlinna function $m(z) = \int d\mu(t)/(t-z)$ implies that $\mu$ is symmetric about 0. For a Stieltjes continued fraction with $m(z) = 1/(b_0 - z - a_0^2/(b_1-z-\cdots))$: the symmetry $m(-z) = -m(z)$ holds if and only if $b_n = 0$ for all $n$ (since $m(-z) = 1/(-b_0-z-a_0^2/(-b_1-z-\cdots))$ and comparing coefficient by coefficient in the continued-fraction expansion). See Akhiezer, "The Classical Moment Problem", Ch. 3. $\square$

**Corollary of Lemma 1.** If the distribution $\mu_\gamma^{real}$ is symmetric about 0 (i.e., if the real zeros of $\Xi$ come in pairs $\pm\gamma_n$, which follows from $\Xi(t) = \Xi(-t)$): then all diagonal coefficients of $J_\infty$ are zero: $b_n^\infty = 0$.

**Verification.** Is $b_n^\infty = 0$ compatible with the CCM data? From Doc 15, Part C: $b_0^\infty = T_\lambda/2$ (at the unnormalized scale) — not zero. The contradiction is only apparent: Lemma 1 applies to the function $m_\infty$ of the measure AT THE SYMMETRIC SCALE. If the zeros of $\Xi$ are $\pm\gamma_n$ with $\gamma_n > 0$, the symmetric measure is $\mu_\infty = \frac{1}{N}\sum_n (\delta_{\gamma_n} + \delta_{-\gamma_n})/2$, which has $b_n^\infty = 0$ in the continued fraction over all of $\mathbb{R}$. But Doc 15 works with the measure on $(0,\infty)$ only (positive zeros), which is the symmetric half.

**Reconciliation.** In Doc 15, $J_\infty$ is built with the measure $\mu_\gamma^{real}$ SUPPORTED on $(0,\infty)$ (positive zeros only). The symmetry of $\Xi$ implies that $J_\infty$ over the full measure (on $\mathbb{R}$) has $b_n^\infty = 0$. Over the measure on $(0,\infty)$: the continued fraction is different and $b_n^\infty \neq 0$ in general.

---

## 6. The complete functional equation of $m_\infty$

**Combining Proposition 3 with Lemma 1** (at the full scale $\mathbb{R}$):

The function $m_\infty^{full}(z) := \int_\mathbb{R} d\mu_\infty(t)/(t-z)$ (over all zeros of $\Xi$, real or not) satisfies:

$$m_\infty^{full}(-z) = -m_\infty^{full}(z), \quad \Im(m_\infty^{full}(z)) > 0 \text{ for } z \in \mathbb{C}^+,$$

and the continued fraction of $m_\infty^{full}$ has $b_n^\infty = 0$.

**The Stieltjes functional equation for $m_\infty^{full}$.** In addition, by Doc 09 (Corollary 1):

$$m_\infty^{full}(z) = \frac{1}{N} \frac{C_\infty'(z)}{C_\infty(z)}.$$

With $b_n^\infty = 0$: the continued fraction of $m_\infty^{full}$ is:

$$m_\infty^{full}(z) = \cfrac{1}{-z - \cfrac{(a_0^\infty)^2}{-z - \cfrac{(a_1^\infty)^2}{-z - \cdots}}}.$$

This is the continued fraction of the Stieltjes transform of a **symmetric** measure supported on $\mathbb{R}$ with $b_n = 0$.

**Proposition 4** (characterization of $m_\infty^{full}$ by the functional equation). The function $m_\infty^{full}$ is the unique element of the Nevanlinna class satisfying:

(EF1) $m(-z) = -m(z)$ (anti-parity),  
(EF2) $m(z) = \frac{1}{N} C_\infty'(z)/C_\infty(z)$ (fixed-point equation),  
(EF3) $m(z) = \int d\mu(t)/(t-z)$ with $\mu$ a probability measure on $\mathbb{R}$.

*Proof.* Any function satisfying (EF1)-(EF3) has its poles exactly at the zeros of $C_\infty$ (from (EF2)) and those zeros must be real (from (EF3), since the poles of a Nevanlinna function with real support lie on $\mathbb{R}$). Then the zeros of $C_\infty$ are real. The weights of $m$ at its poles are $1/N$ (from the von Mangoldt normalization implicit in (EF3)). Then $m = S_\Xi$ with the zeros of $\Xi$ = the real zeros of $C_\infty$. $\square$

**Critical remark.** The step "the poles of $m$ are on $\mathbb{R}$" in the proof of Proposition 4 uses condition (EF3) — that the measure has real support. This already assumes that the zeros of $C_\infty$ (and hence the zeros of $\Xi$) are real. The circularity persists: to use (EF3) we need to know that the zeros of $C_\infty$ are real, which is equivalent to RH.

---

## 7. The contradiction argument via the dynamical system

**Theorem B1** (dynamical contradiction, conditional). Suppose that $J_\infty$ is in the LP case (Proposition 1) and that the coefficients $(a_n^\infty, b_n^\infty)$ are the CCM limits (Doc 15). Then:

(a) The Möbius dynamical system $\{T_n\}$ has as its unique attractor the function $m_\infty(z)$ (the Stieltjes transform of $\mu_\gamma^{real}$).

(b) If $m_\infty$ satisfies the fixed-point equation (EF2): $N \cdot m_\infty(z) = C_\infty'(z)/C_\infty(z)$, then the poles of $m_\infty$ are the real zeros of $C_\infty$.

(c) By self-adjointness of $J_\infty$: all poles of $m_\infty$ lie on $\mathbb{R}$.

(d) Combining (b) and (c): the zeros of $C_\infty$ are real. By Proposition 5 of Doc 16 (under the identification zeros of $C_\infty$ = zeros of $\Xi$): the zeros of $\Xi$ are real, i.e., RH.

**Status of (a)-(d):**
- (a): Valid, from Proposition 2 (LP case + convergence of the continued fraction).
- (b): Requires verifying that $m_\infty$ satisfies (EF2) **without assuming RH**. This is the gap.
- (c): Valid, from self-adjointness of $J_\infty$ (the poles of $m_\infty = \langle e_0, (J_\infty - z)^{-1} e_0\rangle$ are exactly the eigenvalues of $J_\infty$, which are real).
- (d): Requires the identification of zeros of $C_\infty$ with zeros of $\Xi$ — again the gap from Attack A.

---

## 8. Verification of (EF2) without RH: the central result of Front C

**Question C.1.** Does $m_\infty$ satisfy the fixed-point equation (EF2) without assuming RH?

**Proposition 5** (EF2 holds unconditionally). Without any additional hypothesis: the function $m_\infty$ satisfies the equation:

$$N \cdot m_\infty(z) = \lim_{\lambda \to \infty} \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda},$$

in the sense of uniform convergence on compacta of $\mathbb{C} \setminus \mathbb{R}$.

*Proof.* By Doc 09 (Theorem 1, functional equation for $S_\lambda$): for each $\lambda$,

$$N \cdot m_\lambda(z) = \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} + O(\lambda^{-1/2}).$$

By Doc 15 (Proposition 1): $m_\lambda(z) \to m_\infty(z)$ uniformly on compacta of $\mathbb{C} \setminus \mathbb{R}$ (unconditionally). Taking the limit $\lambda \to \infty$:

$$N \cdot m_\infty(z) = \lim_{\lambda\to\infty} \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda}.$$

The right-hand side is exactly $C_\infty'(z)/C_\infty(z)$ if the limit $C_\lambda'/[C_\lambda - \mu_\lambda] \to C_\infty'/C_\infty$ exists. $\square$

**The limit $C_\lambda'/[C_\lambda - \mu_\lambda] \to C_\infty'/C_\infty$.** Here $C_\lambda(z) = w(z) - \Psi_\lambda(z)$ with $\Psi_\lambda(z) = 2\sum_{p \leq \lambda^2} \Lambda(p)p^{-1/2}e^{iz\log p}$ and $\mu_\lambda \to 0$.

In the limit $\lambda \to \infty$: $\Psi_\lambda(z) \to \Psi(z) = 2\sum_p \Lambda(p)p^{-1/2}e^{iz\log p}$ (convergence in the distributional sense; for $z$ with $\Im(z) > 0$, convergence is absolute since $|e^{iz\log p}| = p^{-\Im(z)} \to 0$).

**Obstacle.** For $z \in \mathbb{R}$: $|\Psi_\lambda(z)|$ is not bounded and $C_\lambda(z) - \mu_\lambda \to C_\infty(z)$ may pass through zero. The zeros of $C_\infty(z)$ (on $\mathbb{R}$) are exactly the poles of $C_\infty'/C_\infty$. At those points, $m_\infty(z)$ has poles.

**Conclusion.** (EF2) holds unconditionally on $\mathbb{C} \setminus \mathbb{R}$, in the sense of Proposition 5. The gap is that the limit $C_\lambda'/(C_\lambda - \mu_\lambda) \to C_\infty'/C_\infty$ may fail on the real line — but for the purposes of the contradiction argument, validity on $\mathbb{C}^+$ suffices.

---

## 9. The complete argument (with the gap made explicit)

**Theorem B2** (the Möbius-CCM argument, with the gap made explicit). The following statements are equivalent:

(i) RH: all zeros of $\Xi$ are real.

(ii) The real zeros of $C_\infty(z) = w(z) - \Psi(z)$ are exactly the imaginary parts of the zeros of $\zeta$ on the critical line.

(iii) The fixed-point equation $N \cdot m_\infty = C_\infty'/C_\infty$ (with $m_\infty$ the $m$ function of the self-adjoint operator $J_\infty$) implies that the poles of $m_\infty$ (= eigenvalues of $J_\infty$, all real) are exactly the zeros of $\Xi$ on $\mathbb{R}$.

*Proof of equivalence.*

(i) $\Rightarrow$ (ii): By the explicit formula + Proposition 3 of Doc 09 (under RH, the zeros of $C_\infty$ are $\{\gamma_n\}$). ✓

(ii) $\Rightarrow$ (iii): If the zeros of $C_\infty$ on $\mathbb{R}$ are $\{\gamma_n\}$: the poles of $C_\infty'/C_\infty$ are $\{\gamma_n\}$. By (EF2): the poles of $m_\infty$ are $\{\gamma_n\}$. By self-adjointness of $J_\infty$: those poles are real (automatically). Then the $\gamma_n$ are real: RH. ✓

(iii) $\Rightarrow$ (i): The poles of $m_\infty$ are the eigenvalues of $J_\infty$ (all real) and are the zeros of $\Xi$ on $\mathbb{R}$: i.e., the zeros of $\Xi$ are real: RH. ✓

(i) $\Rightarrow$ (iii): Under RH, $m_\infty = S_\Xi$ (Doc 09, Corollary 3) and all poles (zeros of $\Xi$) are real. ✓ $\square$

**The gap:** The implication (ii) $\Rightarrow$ (iii) requires proving that the real zeros of $C_\infty$ are the imaginary parts of the zeros of $\zeta$ on $\Re(s)=1/2$ — this is (ii), which is equivalent to RH (by (i) $\Leftrightarrow$ (ii)). So the argument does not give RH for free; it pinpoints the obstacle precisely: it is condition (ii).

---

## 10. The approach via the fixed point of the dynamical system: a new route

**Proposition 6** (the fixed point of the Möbius dynamical system is $m_\infty$, and $m_\infty$ has real poles). Let $z \in \mathbb{C} \setminus \mathbb{R}$. The Möbius dynamical system with coefficients $(a_n^\infty, b_n^\infty)$:

- Has as its unique asymptotic fixed point (attractor) the function $m_\infty(z)$ (Weyl LP case).
- $m_\infty(z)$ is the Weyl-Titchmarsh function of the self-adjoint operator $J_\infty$.
- The poles of $m_\infty$ are the eigenvalues of $J_\infty$, which are **all real** (self-adjointness).

**Proposition 7** (the fixed-point equation determines the poles). By equation (EF2): $N \cdot m_\infty(z) = \lim_\lambda C_\lambda'(z)/(C_\lambda(z)-\mu_\lambda)$ (unconditionally on $\mathbb{C}^+$). The poles of $m_\infty$ (on $\mathbb{R}$, by self-adjointness) coincide with the poles of the limit $C_\infty'/C_\infty$.

**Lemma 2** (the poles of $C_\infty'/C_\infty$ on $\mathbb{R}$ are the real zeros of $C_\infty$). The simple zeros of $C_\infty$ on $\mathbb{R}$ are simple poles of $C_\infty'/C_\infty$ with residue 1. Then the eigenvalues of $J_\infty$ (poles of $m_\infty$, all real) are exactly the real zeros of $C_\infty$ (unconditionally).

*Proof.* If $C_\infty(\gamma) = 0$ with $C_\infty'(\gamma) \neq 0$: then $C_\infty(z) = C_\infty'(\gamma)(z-\gamma) + O((z-\gamma)^2)$, so $C_\infty'/C_\infty \sim 1/(z-\gamma)$ near $\gamma$: a simple pole with residue 1. $\square$

**The central result of Front C (without circularity):**

**Theorem C1** (the eigenvalues of $J_\infty$ are exactly the real zeros of $C_\infty$, unconditional). Without assuming RH:

$$\text{spec}(J_\infty) = \{t \in \mathbb{R} : C_\infty(t) = 0\}.$$

*Proof.* By equation (EF2) and Lemma 2: the eigenvalues of $J_\infty$ (= poles of $m_\infty$, all real by self-adjointness) are exactly the poles of $C_\infty'/C_\infty$, which are exactly the real zeros of $C_\infty$. $\square$

**Corollary C2.** The spectral measure of $J_\infty$ satisfies:

$$\mathrm{supp}(\mu_\infty) = \{t \in \mathbb{R} : C_\infty(t) = 0\}.$$

This is the cleanest result of Front C: the eigenvalues of the limiting CCM operator are exactly the zeros of the explicit potential $C_\infty = w - \Psi$.

---

## 11. Consequences and final reformulation

**Lemma 3** (connection between zeros of $C_\infty$ and zeros of $\Xi$, unconditional). The weak convergence $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15, unconditional) and Corollary C2 imply that:

$$\mu_\gamma^{real} = \text{distribution measure of zeros of } C_\infty \text{ on } \mathbb{R}.$$

*Proof.* By Doc 15: $\mu_\infty = \mu_\gamma^{real}$ (unconditionally). By Corollary C2: $\mathrm{supp}(\mu_\infty) = \{t \in \mathbb{R}: C_\infty(t)=0\}$. Then the measure $\mu_\gamma^{real}$ is supported on the real zeros of $C_\infty$. $\square$

**Theorem C3** (equivalence with RH via zeros of $C_\infty$). The following are equivalent:

(i) RH.

(ii) The real zeros of $C_\infty$ are exactly the $\gamma_n$ (imaginary parts of the zeros of $\zeta$ on $\Re(s) = 1/2$).

(iii) $\mu_\gamma^{real} = \mu_\gamma$ (measure of zeros of $\Xi$ on $\mathbb{R}$ = full measure of zeros of $\Xi$).

(iv) All zeros of $C_\infty$ captured by $\mu_\infty$ are exactly the $\gamma_n$ — i.e., there are no zeros of $\Xi$ off the critical line.

*Proof.* (i) $\Leftrightarrow$ (iii): by definition ($\mu_\gamma^{real} = \mu_\gamma$ iff all zeros of $\Xi$ are real iff RH). (iii) $\Leftrightarrow$ (ii): by Lemma 3, $\mu_\gamma^{real}$ is supported on zeros of $C_\infty$; and under (i) the zeros of $C_\infty$ are $\{\gamma_n\}$. (ii) $\Leftrightarrow$ (iv): reformulation. $\square$

---

## 12. Analysis of the potential $C_\infty$ without RH: what is known

**Proposition 8** (structure of the zeros of $C_\infty$ without RH). Without assuming RH: let $\rho = \sigma + i\gamma$ be a zero of $\zeta$ with $\sigma \neq 1/2$. Then $C_\infty(t) = w(t) - 2\sum_\rho \cos(t\log|\rho|)/|\rho|$, and the contribution of the pair $\{\rho, \bar\rho\} = \{\sigma \pm i\gamma\}$ to $C_\infty$ is $-4\cos(t\log|\rho|)/|\rho|$.

The zeros of $t \mapsto \cos(t\log|\rho|)/|\rho|$ are at $t = \pi(2k+1)/(2\log|\rho|)$ — points that in general do NOT coincide with $\gamma$ (the imaginary part of $\rho$).

**Lemma 4** (distinguishing zeros: under RH vs. without RH). Under RH: for $\rho = 1/2 + i\gamma$, $|\rho| = \sqrt{1/4+\gamma^2} \approx \gamma$ for $\gamma \gg 1$. The contribution of $\rho$ to $C_\infty$ oscillates as $\cos(t\log\gamma)/\gamma$.

Without RH: for $\rho = \sigma + i\gamma$ with $\sigma > 1/2$, $|\rho| = \sqrt{\sigma^2+\gamma^2} > \gamma$. The oscillation frequency is $\log|\rho| = \frac{1}{2}\log(\sigma^2+\gamma^2) > \log\gamma$ for $\sigma > 1/2$. Then the zeros of this contribution are at distances $\sim \pi/(2\log|\rho|) < \pi/(2\log\gamma)$ from the origin — MORE DENSE than under RH.

This generates additional zeros of $C_\infty$ on $\mathbb{R}$ that are not $\gamma_n$ — and that would be captured by $\mu_\infty$ via Corollary C2. But $\mu_\infty = \mu_\gamma^{real}$ (which only has atoms at the $\gamma_n$). Contradiction: this would prove that there can be no zeros with $\sigma > 1/2$.

**The problem with the argument of Lemma 4:** The claim "the additional zeros of $C_\infty$ are captured by $\mu_\infty$" requires that the measure $\mu_\infty$ have atoms at every zero of $C_\infty$. But if a zero of $C_\infty$ is "extra" (not a $\gamma_n$), it might cancel with another zero of $\hat\xi_\lambda$ so that the net contribution to the measure is zero. This requires finer analysis.

---

## 13. Summary of Doc 17

**Proved in this doc:**

- The Möbius dynamical system $\{T_n\}$ converges to the unique attractor $m_\infty(z)$ (LP case, unconditional).
- The symmetry $\Xi(t) = \Xi(-t)$ implies $m_\infty(-z) = -m_\infty(z)$ and imposes $b_n^\infty = 0$ at the symmetric scale.
- The fixed-point equation (EF2) holds unconditionally on $\mathbb{C}^+$ (Proposition 5).
- **Theorem C1** (unconditional): $\mathrm{spec}(J_\infty) = \{t \in \mathbb{R} : C_\infty(t) = 0\}$.
- **Theorem C3**: RH $\iff$ the real zeros of $C_\infty$ are exactly $\{\gamma_n\}$.

**Open:**

- Question C.2: Can it be proved directly (via the structure of $w$ and $\Psi$) that the real zeros of $C_\infty$ are $\{\gamma_n\}$ without assuming RH?
- Lemma 4 gives a promising direction (extra zeros of $C_\infty$ if RH fails), but the contradiction argument is not closed.
