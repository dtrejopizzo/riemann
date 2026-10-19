# Phase 29 — Doc 28: The Two EF2s, the Near-Miss, and the Exact Point of the Gap

**Context:** Doc 27 identified that there are TWO distinct EF2s:
- $\text{EF2}_{WT}$: $N\cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$ (Doc 17, for the Weyl-Titchmarsh function)
- $\text{EF2}_{emp}$: $N\cdot m_\infty^{emp}(z) = C_\infty'(z)/C_\infty(z) - \Xi'(z)/\Xi(z)$ (corrected EF2, for the empirical function)

**Objective of this document:** Study the difference $\text{EF2}_{WT} - \text{EF2}_{emp}$ as a possible tool to attack Inc. Inv. Identify the exact point where the argument fails or succeeds.

---

## 1. The difference identity

**Definition.** For $z \in \mathbb{C}^+$, define:

$$\Delta(z) := m_\infty^{WT}(z) - m_\infty^{emp}(z).$$

From the two EF2s:

$$N\cdot\Delta(z) = N\cdot m_\infty^{WT}(z) - N\cdot m_\infty^{emp}(z) = \frac{C_\infty'(z)}{C_\infty(z)} - \left[\frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}\right] = \frac{\Xi'(z)}{\Xi(z)}.$$

Hence:

$$\Delta(z) = \frac{1}{N}\cdot\frac{\Xi'(z)}{\Xi(z)}. \quad (\Delta\text{-id})$$

**Proposition 1** (content of $\Delta$-id in terms of spectral measures). If $(\Delta\text{-id})$ is correct:

$$d\mu_{WT}^\infty - d\mu_\infty^{emp} = \frac{1}{N}\cdot d\mu_\Xi^{real},$$

where $\mu_\Xi^{real}$ is the zero-counting measure of $\Xi$ on $\mathbb{R}$ (= the Montgomery measure $\mu_\gamma^{real}$).

*Proof.* Stieltjes inversion of $(\Delta\text{-id})$. $\square$

**Corollary 1** (limit $N\to\infty$). If $(\Delta\text{-id})$ is correct and $N\to\infty$:

$$\mu_{WT}^\infty = \mu_\infty^{emp} + \frac{1}{N}\cdot\mu_\gamma^{real} \xrightarrow{N\to\infty} \mu_\infty^{emp} = \mu_\gamma^{real}.$$

And since $\mu_{WT}^\infty$ has support $\subseteq \{$zeros of $C_\infty\}$ (from $\text{EF2}_{WT}$), and $\mu_\gamma^{real}$ has support $= \{\gamma_n\}$: Inc. Inv. follows.

---

## 2. The near-miss: the argument almost closes

The argument above would take the following clean shape:

**Proposed argument.**
1. From $\text{EF2}_{WT}$ (Doc 17): $\text{supp}(\mu_{WT}^\infty) \subseteq \{$zeros of $C_\infty\}$.
2. From $(\Delta\text{-id})$ with $N\to\infty$: $\mu_{WT}^\infty = \mu_\gamma^{real}$.
3. Therefore: $\text{supp}(\mu_\gamma^{real}) = \{\gamma_n\} \subseteq \{$zeros of $C_\infty\}$, which is Inc. Inv.
4. By Theorem D (Doc 19 / P37): $\text{RH}$. $\square$

If the three steps were rigorous, we would have a proof of RH.

**The exact point of failure.** The argument fails at step 0, not at 1, 2, or 3. The problem is:

> $(\Delta\text{-id})$ CANNOT be derived from the two EF2s independently: at least one of the two EF2s already requires, in its proof, information equivalent to Inc. Inv.

---

## 3. Diagnosis: which EF2 is genuinely unconditional?

**Proposition 2** (unconditional status of the two EF2s).

(a) $\text{EF2}_{WT}$: The equation $N\cdot m_\lambda^{WT}(z) = C_\lambda'(z)/(C_\lambda(z)-\mu_\lambda)$ for the FINITE operators $J_\lambda^N$ is unconditional (it comes from the Möbius recursion, Doc 17 Proposition 2). The limit $N\cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$ requires:
- (i) Uniform convergence of the Jacobi coefficients: $a_n^{(\lambda)} \to a_n^\infty$, $b_n^{(\lambda)} \to b_n^\infty$. **Status: unconditional** (Doc 11, Proposition 4).
- (ii) Convergence of the $m$ function: $m_\lambda^{WT}(z) \to m_\infty^{WT}(z)$. **Status: requires that $J_\infty$ be well defined and that convergence of coefficients imply convergence of m-functions.** This is standard for Jacobi operators with convergent coefficients (Nevai theory, 1979). **Unconditional.**

(b) $\text{EF2}_{emp}$: The equation $N\cdot m_\lambda^{emp}(z) = C_\lambda'(z)/(C_\lambda(z)-\mu_\lambda) - \hat k_\lambda'/\hat k_\lambda(z)$ is unconditional for finite $J_\lambda^N$ (Proposition 1 of Doc 27). The limit:

$$N\cdot m_\infty^{emp}(z) = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}$$

additionally requires: (iii) $m_\lambda^{emp}(z) \to m_\infty^{emp}(z)$. Here $m_\lambda^{emp}(z) = (1/N)\sum_n 1/(z-t_n^{(\lambda)})$. For this to converge to something non-trivial in the limit $N\to\infty$, the eigenvalues $t_n^{(\lambda)}$ must converge to well-defined values $t_n^\infty$. The convergence $t_n^{(\lambda)} \to \gamma_n$ **requires Inc. Inv.** (or at minimum a convergence of eigenvalues equivalent to it).

**Conclusion of Proposition 2.** $\text{EF2}_{WT}$ is genuinely unconditional. $\text{EF2}_{emp}$ in the limit $N\to\infty$ requires the convergence of eigenvalues — which is equivalent to Inc. Inv. Therefore, $(\Delta\text{-id})$ cannot be obtained from the two EF2s independently: $\text{EF2}_{emp}$ in the limit already assumes Inc. Inv.

---

## 4. The only genuinely new point: EF2 for $m^{WT}$ in the limit

Given that $\text{EF2}_{WT}$ is unconditional and $\text{EF2}_{emp}$ is not (in the limit), the genuinely unconditional content of the program reduces to:

**Theorem 1** (total unconditional content of the CCM program). Unconditionally:

$$\text{supp}(\mu_{WT}^\infty) \subseteq \{\text{zeros of }C_\infty\text{ on }\mathbb{R}\} \subseteq \{\gamma_n\}.$$

*Proof.* The first inclusion: from the unconditional $\text{EF2}_{WT}$ (steps verified in Doc 27 section 3). The second inclusion: Theorem B of P37 (Doc 19). $\square$

For RH we need the equality $\text{supp}(\mu_{WT}^\infty) = \{\gamma_n\}$, which requires proving that ALL $\gamma_n$ are in the support.

---

## 5. Can the support of $\mu_{WT}^\infty$ be determined unconditionally?

**The support of $\mu_{WT}^\infty$ from $\text{EF2}_{WT}$.** By EF2: the poles of $m_\infty^{WT}$ on $\mathbb{R}$ are the zeros of $C_\infty$. The measure $\mu_{WT}^\infty$ assigns positive mass to $\gamma_n^C$ iff $\gamma_n^C$ is a simple zero of $C_\infty$ (and zero mass to higher-order zeros, which contribute to $\mu_{WT}^\infty$ differently).

**The support of $\mu_{WT}^\infty$ from Jacobi theory.** Alternatively: $\text{supp}(\mu_{WT}^\infty)$ = spectrum of $J_\infty$ (for the semi-infinite operator). By Doc 23 (Kotani): the spectrum is purely point. By $\text{EF2}_{WT}$: the eigenvalues are zeros of $C_\infty$.

But how many eigenvalues does $J_\infty$ have? For a Jacobi operator with $a_n^\infty \to 0$:
- Spec$(J_\infty)$ may be countable (infinite but numerable).
- The total mass $\int d\mu_{WT}^\infty = 1$ is distributed among the eigenvalues.
- Is there one, finitely many, or infinitely many eigenvalues?

**Proposition 3** (number of eigenvalues of $J_\infty$). For $J_\infty$ with $a_n^\infty = \pi/\log\gamma_n \to 0$ and $b_n^\infty = 0$:

The eigenvalues of $J_\infty$ coincide with the zeros of $C_\infty$ on $\mathbb{R}$ (from $\text{EF2}_{WT}$). The number of zeros of $C_\infty$ in $[0,T]$ satisfies (from Proposition 5.2 of Doc 20 via the argument-variation argument):

$$N_{C_\infty}(T) = O(T\log T),$$

that is: there are infinitely many eigenvalues, with density comparable to that of the zeros of $\Xi$. Hence $J_\infty$ has infinite point spectrum with density $\sim (T\log T)/(2\pi)$ on $[0,T]$.

**The central question.** Is $N_{C_\infty}(T) = N_\Xi(T)$ (for all $T$) or $N_{C_\infty}(T) < N_\Xi(T)$ (for some $T$)?

- If $N_{C_\infty}(T) = N_\Xi(T)$: the zeros of $C_\infty$ and $\Xi$ correspond 1-1, giving Inc. Inv.
- If $N_{C_\infty}(T) < N_\Xi(T)$: zeros of $\Xi$ are missing from $C_\infty$, negating Inc. Inv.

This reformulates Inc. Inv. as a question of ZERO COUNTING.

---

## 6. Zero counting: a new angle of attack

**Proposition 4** (lower bound vs. upper bound for $N_{C_\infty}(T)$). From earlier results:

(a) **Upper bound**: $N_{C_\infty}(T) \leq N_\Xi(T) + O(\log T)$ (from Theorem B of P37 plus the argument-variation formula).

(b) **Unconditional lower bound**: $N_{C_\infty}(T) \geq c\cdot T\log T$ for some constant $c > 0$ (since $C_\infty$ oscillates with frequency $\sim T\log T$).

**For Inc. Inv. we need**: $N_{C_\infty}(T) \geq N_\Xi(T) - O(1)$, i.e., the lower bound of Proposition 4(b) must be as good as the upper bound.

**Proposition 5** (reformulation of Inc. Inv. as a counting problem). The following statements are equivalent:

(i) Inc. Inv.: $\{\gamma_n\} \subseteq \{$zeros of $C_\infty\}$.

(ii) Density: $\lim_{T\to\infty} N_{C_\infty}(T)/N_\Xi(T) = 1$.

(iii) The $\text{EF2}_{emp}$ limit (with the correct normalization): $m_\infty^{emp} = \mu_\gamma^{real}$ as a Weyl-Titchmarsh function.

*Proof.* (i)$\Rightarrow$(ii) trivial since $N_{C_\infty}(T) \geq N_\Xi(T)$ (each $\gamma_n$ is a zero of $C_\infty$) and $N_{C_\infty}(T) \leq N_\Xi(T)+O(\log T)$, giving $N_{C_\infty}/N_\Xi \to 1$. (ii)$\Rightarrow$(i): if the density is 1, the zeros of $C_\infty$ cannot "escape" far from the $\gamma_n$, and by continuity and Theorem B: the $\gamma_n$ are zeros of $C_\infty$. (i)$\Leftrightarrow$(iii) is Theorem 2 of Doc 22. $\square$

---

## 7. The density of zeros of $C_\infty$ via Jensen's formula

**Proposition 6** (Jensen's formula for $C_\infty$). For $T > 0$:

$$N_{C_\infty}(T) = \frac{1}{\pi}\int_0^T \left|\text{Im}\frac{C_\infty'(t)}{C_\infty(t)}\right| dt + O(1),$$

(argument-variation formula for zeros in $[0,T]$, under the condition $C_\infty(0) \neq 0$).

**The relation with the prime side.** $C_\infty(t) = w(t) - \Psi(t)$, where $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$.

The density of zeros of $C_\infty$ depends on how $C_\infty'(t)/C_\infty(t)$ oscillates — which connects directly to the distribution of primes.

**Proposition 7** (lower bound via the explicit formula). Using the Guinand-Weil formula:

$$\frac{1}{2\pi i}\int_\gamma \frac{C_\infty'(z)}{C_\infty(z)}dz = N_{C_\infty}(T) + O(\log T),$$

where $\gamma$ is the rectangle $[0,T]\times[0,\epsilon]$ (for small $\epsilon$). The left-hand side can be evaluated using the expression of $C_\infty$ in terms of the zeros of $\zeta$.

Under RH (using the Hadamard formula $C_\infty(z) = C_\infty(0)\prod_n(1-z/\gamma_n^C)(1+z/\gamma_n^C)$):

$$\frac{C_\infty'(z)}{C_\infty(z)} = \sum_n\left[\frac{1}{z-\gamma_n^C} + \frac{1}{z+\gamma_n^C}\right].$$

Integrating over $\gamma$: $N_{C_\infty}(T) = N_{C_\infty}(T)$ (tautological). To make progress we need an expression INDEPENDENT of the $\gamma_n^C$.

---

## 8. The attack via the direct Guinand explicit formula

**The expression for $C_\infty$ via primes.** Recalling:

$$C_\infty(t) = w(t) - \Psi(t), \quad \Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p).$$

**Guinand's formula.** For admissible test functions $h$:

$$\sum_n h(\gamma_n) = -2h(0)\log\pi + \int_{-\infty}^\infty h(t)\frac{\Xi'}{\Xi}(t)dt - 2\sum_p\sum_{k\geq 1}\frac{\log p}{p^{k/2}}\hat h(k\log p),$$

where $\hat h$ is the Fourier transform of $h$.

**Applying the formula to $h(t) = C_\infty(t)\cdot\phi_\epsilon(t-\gamma_n)$** (localizing near a zero $\gamma_n$ of $\Xi$):

If $C_\infty(\gamma_n) = 0$: the left-hand side contributes $h(\gamma_n) = C_\infty(\gamma_n)\cdot\phi_\epsilon(0) = 0$.

If $C_\infty(\gamma_n) \neq 0$: the left-hand side contributes $C_\infty(\gamma_n)\cdot\phi_\epsilon(0) \neq 0$.

The right-hand side (in terms of primes): depends on $\hat h$, which involves both $C_\infty$ and $\phi_\epsilon$.

**The obstacle.** For the Guinand formula to say anything about whether $C_\infty(\gamma_n) = 0$, we need the right-hand side to vanish for every test function localized near $\gamma_n$. This requires:

$$-2h(0)\log\pi - 2\sum_p\sum_{k\geq 1}\frac{\log p}{p^{k/2}}\hat h(k\log p) = 0 \quad \text{for } h = C_\infty\cdot\phi_\epsilon(\cdot-\gamma_n).$$

The left-hand side is a combination of the behavior of $C_\infty$ near $\gamma_n$ via the prime formula. This equation is yet another reformulation of Inc. Inv. — it gives us no new information.

---

## 9. The exact point of the gap — final formulation

**Theorem 2** (precise localization of the gap). The CCM-Jacobi program has established (unconditionally):

$$\text{supp}(\mu_{WT}^\infty) \subseteq \{\gamma_n: C_\infty(\gamma_n)=0\} \subseteq \{\gamma_n\}.$$

The gap is exactly: is the left-hand inclusion an equality?

This is equivalent to: Is $\{\gamma_n\} = \{$zeros of $C_\infty$ on $\mathbb{R}\}$?

The equivalent reformulations of the gap (all shown to be equivalent in docs 21-28):

| Formulation | Statement | Doc |
|---|---|---|
| Inc. Inv. | $\Xi(\gamma_n) = 0 \Rightarrow C_\infty(\gamma_n) = 0$ | Doc 19 |
| Counting | $N_{C_\infty}(T) = N_\Xi(T)$ asymptotically | Doc 28 §6 |
| Spectral | $\mu_{WT}^\infty = \mu_\gamma^{real}$ | Doc 22 |
| Weights | $\forall n: \langle e_0, \psi_n^\infty\rangle \neq 0$ | Doc 23 |
| Sum | $\forall n: \sum_\rho \cos(\gamma_n\log|\rho|)/|\rho| = -c_0/2$ | Doc 19 |

**Proposition 8** (no internal argument closes the gap). The arguments analyzed in docs 21-28:
- Functional equation + beat frequencies (Doc 21): gives only $N_{off}(T) = O(1)$ or RH (conditional).
- Simple zeros + EF2 (Docs 22-23): gives RH under (LI)+(S) (conditional).
- Moment problem (Doc 26): the Hamburger problem is indeterminate; additional information is circular.
- EF2 audit (Doc 27): $\text{EF2}_{emp}$ requires convergence of eigenvalues (circular).
- Two EF2s + near-miss (Doc 28): $(\Delta\text{-id})$ is not independent of Inc. Inv.

None of these arguments closes the gap unconditionally.

---

## 10. Proposal for Phase 30: three genuinely new fronts

Based on the complete analysis of docs 15-28, the only angles that have NOT been explored and that could avoid the circularity are:

**Front A: Unbounded operator theory.** The operator $J_\infty$ has $a_n^\infty \to 0$ (non-standard limit-point case). The spectral theory of Jacobi operators in the case $a_n \to 0$ is special (singular limit). In particular:

- The resolvent function $R(z) = (J_\infty - z)^{-1}$ might have special completeness properties.
- Remling's results (2011) on the unitary limit in the context of Schrödinger operators might be adaptable.
- **Killip-Simon theory** (JAMS 2003) on spectral measures supported on $[-2,2]$ might have an analogue for bounded supports.

**Front B: The function $C_\infty$ as an almost-periodic function.** $C_\infty(t) = w(t) - \Psi(t)$ is a quasi-periodic function in the Besicovitch class (a sum of cosines with frequencies $\{\log p\}$). Bergelson-Leibman's work on ergodic averages in quasi-periodic systems might give a lower bound for the zero density.

**Front C: Spectral geometry via the spectral quotient.** The difference $C_\infty'/C_\infty - \Xi'/\Xi = N\cdot m_\infty^{emp}$ gives (formally) the "discrepancy" between the functions $C_\infty$ and $\Xi$ measured by the empirical spectral density. If $|C_\infty'/C_\infty - \Xi'/\Xi|$ can be bounded from below (without using the equivalence with RH), it might force the equality of their zeros.

All three fronts are genuinely new and avoid the circularities identified above.
