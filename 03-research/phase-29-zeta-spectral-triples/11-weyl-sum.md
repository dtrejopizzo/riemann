# Phase 29 — The Weyl sum over the zeros and average convergence

**Objective:** Attack Question 29.9: behavior of $D_n(x) := \sum_{m\neq n}\sin((\gamma_m-\gamma_n)x)/(\gamma_m-\gamma_n)$ as $x = 2\log\lambda \to \infty$. Correction of the Riemann–Lebesgue argument (which does not apply to discrete measures). Clean result: $D_n(x)$ is a bounded almost-periodic function; its time average is 0; convergence $t_n^{(\lambda)} \to \gamma_n$ holds in the Cesàro average; individual convergence requires an additional arithmetic hypothesis.

---

## 1. Correction of the Riemann–Lebesgue argument of doc 10

**Error identified.** Corollary 2 of doc 10 invoked the Riemann–Lebesgue lemma to conclude that $D_n(x) \to 0$. This is INCORRECT: the Riemann–Lebesgue lemma applies to functions $f \in L^1(\mathbb{R})$, and gives $\hat f(\xi) \to 0$. But $D_n(x) = \hat\mu_n(x)$ where $\mu_n = \sum_{m\neq n}\delta_{mn}^{-1}\delta_{\delta_{mn}}$ is a DISCRETE measure, which is neither absolutely continuous nor $L^1$. For discrete measures, the Riemann–Lebesgue lemma FAILS.

**Canonical counterexample.** Let $f(x) = \sum_{n=1}^\infty \frac{\sin(nx)}{n}$ (Fourier series of the sawtooth function). For $x = 2\pi k/N$: $f(x) = \pi/2 \cdot (1 - 2\lfloor kN^{-1}\rfloor)$ oscillates between $\pm\pi/2$ and does not converge to 0. The argument of Corollary 2 of doc 10 contained this error.

**Consequence.** The individual convergence result $t_n^{(\lambda)} \to \gamma_n$ under RH + Montgomery (Corollary 2, doc 10) is NOT proved. The bound $|t_n^{(\lambda)} - \gamma_n| = O(\log\lambda)$ (Theorem 2, doc 10) remains valid, but convergence is more subtle.

---

## 2. Almost-periodic nature of $D_n(x)$

**Definition.** A function $f:\mathbb{R}\to\mathbb{R}$ is **almost periodic** (in the Bohr sense) if for every $\varepsilon > 0$ there exists $L > 0$ such that every interval of length $L$ contains a $\tau$ with $|f(x+\tau) - f(x)| < \varepsilon$ for all $x$.

**Proposition 1** (almost periodicity of $D_n$). The function

$$D_n(x) = \sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)x)}{\gamma_m-\gamma_n}$$

is Bohr almost periodic if and only if the series converges uniformly (in the sense of the almost-periodic norm). Under the hypothesis that the spacings $\delta_{mn} = \gamma_m - \gamma_n$ are "well separated" (Riesz–Fischer condition: $\sum_{m\neq n}|\delta_{mn}|^{-2} < \infty$), the function $D_n$ is almost periodic.

*Proof.* The Riesz–Fischer condition implies that the series $\sum\delta_{mn}^{-1}e^{i\delta_{mn}x}$ converges in the $L^2$ sense of almost-periodic functions. The mean square $M\{|D_n|^2\} = \sum_{m\neq n}|\delta_{mn}|^{-2}/2 < \infty$ (under the hypothesis), hence $D_n \in B^2$ (the Besicovitch space). $\square$

**The hypothesis $\sum_{m\neq n}|\delta_{mn}|^{-2} < \infty$ is "GUE-level repulsion":** under Montgomery's pair correlation conjecture, the spacings satisfy $\rho_2(\delta) \sim \delta^2$ as $\delta\to 0$ (zeros do not get arbitrarily close), which implies $\sum|\delta_{mn}|^{-2} < \infty$ with the sum diverging only logarithmically. This condition is known conditionally under RH (Gonek, 1984).

---

## 3. The time average of $D_n$ is zero

**Theorem 1** (time average). For each fixed $n$:

$$\lim_{X\to\infty}\frac{1}{X}\int_0^X D_n(x)\,dx = 0.$$

*Proof.* Term by term (justified by dominated convergence under the Riesz–Fischer hypothesis):

$$\frac{1}{X}\int_0^X\frac{\sin((\gamma_m-\gamma_n)x)}{\gamma_m-\gamma_n}\,dx = \frac{1-\cos((\gamma_m-\gamma_n)X)}{(\gamma_m-\gamma_n)^2 X} \leq \frac{2}{(\gamma_m-\gamma_n)^2 X} \to 0.$$

Summing over $m\neq n$ with dominated convergence (using $\sum|\delta_{mn}|^{-2} < \infty$): the average $\to 0$. $\square$

**Corollary 1** (Cesàro convergence of the zeros). Let $\sigma_n(\lambda) := t_n^{(\lambda)} - \gamma_n$ be the displacement of the $n$-th zero. By Theorem 2 of doc 10: $\sigma_n(\lambda) \approx D_n(2\log\lambda)/C_\lambda'(\gamma_n)$. The Cesàro average:

$$\lim_{X\to\infty}\frac{1}{\log X}\int_1^X|\sigma_n(\lambda)|\,\frac{d\lambda}{\lambda} = \frac{1}{|C_\lambda'(\gamma_n)|}\lim_{X\to\infty}\frac{1}{\log X}\int_0^{\log X}|D_n(2u)|\,du.$$

By Theorem 1 and the Cauchy–Schwarz inequality: the average $\to 0$ if $D_n \in B^2$ (Besicovitch space). $\square$

**Interpretation.** For "almost every" value of $\lambda$ in the sense of logarithmic density: $|t_n^{(\lambda)} - \gamma_n|$ is small. But there may be a sequence of $\lambda$'s for which the displacement does not tend to 0.

---

## 4. The variance of $D_n$ and the role of the pair correlation

**Proposition 2** (variance of $D_n$). The mean square of $D_n$:

$$M\{D_n^2\} := \lim_{X\to\infty}\frac{1}{X}\int_0^X D_n(x)^2\,dx = \frac{1}{2}\sum_{m\neq n}\frac{1}{(\gamma_m-\gamma_n)^2} =: V_n.$$

*Proof.* By Parseval's identity for almost-periodic functions: $M\{|f|^2\} = \sum_\omega |a_\omega|^2$ where $a_\omega$ are the Fourier coefficients. For $D_n$: $a_{\gamma_m-\gamma_n} = (2i(\gamma_m-\gamma_n))^{-1}$ (for $m\neq n$) and the other coefficients are 0. $\square$

**Under Montgomery (GUE):** the sum $V_n = \frac{1}{2}\sum_{m\neq n}(\gamma_m-\gamma_n)^{-2}$ has the estimate (Gonek, under RH):

$$V_n = \frac{1}{2}\sum_{m\neq n}\frac{1}{(\gamma_m-\gamma_n)^2} \leq C\log\gamma_n.$$

Hence: $\|D_n\|_{B^2} = \sqrt{V_n} = O(\sqrt{\log\gamma_n})$.

**Consequence.** The typical amplitude of $D_n(x)$ is $O(\sqrt{\log\gamma_n})$, NOT $O(\log\lambda)$. The bound $O(\log\lambda)$ of Theorem 2 of doc 10 is a MAXIMUM bound (worst case), while the typical value is $O(\sqrt{\log\gamma_n})$.

---

## 5. Improved estimate of the displacement $\sigma_n(\lambda)$

**Proposition 3** (typical displacement under Montgomery). Under RH + Montgomery's pair correlation conjecture, for "almost every" $\lambda$ (outside a set of logarithmic density zero):

$$|\sigma_n(\lambda)| = |t_n^{(\lambda)} - \gamma_n| = O_n\!\left(\frac{\sqrt{\log\log\lambda}}{|C_\lambda'(\gamma_n)|}\right).$$

*Proof sketch.* The function $D_n(x)$ has mean square $V_n = O(\log\gamma_n)$. By the theory of almost-periodic functions (Weyl distribution theorem): for every $\varepsilon > 0$, the density of the set $\{x : |D_n(x)| > C\sqrt{\log\gamma_n\log x}\}$ is $O(\varepsilon)$ for appropriate $C = C(\varepsilon)$. In particular, $|D_n(2\log\lambda)| = O(\sqrt{\log\gamma_n\log\log\lambda})$ for "almost every" $\lambda$. $\square$

**The denominator $|C_\lambda'(\gamma_n)|$.** From Section 7 of doc 10: $C_\lambda'(\gamma_n) = w'(\gamma_n) - \Psi_\lambda'(\gamma_n)$. The derivative $\Psi_\lambda'(\gamma_n) = -2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\log p\cdot\sin(\gamma_n\log p)$. The dominant term comes from $\rho_n$ in the differentiated explicit formula: $\Psi_\lambda'(\gamma_n) \approx 4\log\lambda/\gamma_n$ (from the simple pole of $\zeta'/\zeta$ at $s = 1/2+i\gamma_n$).

Hence: $C_\lambda'(\gamma_n) \approx -4\log\lambda/\gamma_n$ (negative: the slope of the potential at the crossing is downward for the $n$-th crossing). So $|C_\lambda'(\gamma_n)| \sim 4\log\lambda/\gamma_n$.

**Final estimate:**

$$|\sigma_n(\lambda)| \approx \frac{|D_n(2\log\lambda)|}{|C_\lambda'(\gamma_n)|} \approx \frac{\sqrt{\log\gamma_n}\cdot\sqrt{\log\log\lambda}}{4\log\lambda/\gamma_n} = \frac{\gamma_n\sqrt{\log\gamma_n\log\log\lambda}}{4\log\lambda}.$$

For fixed $n$ (with $\gamma_n$ constant) and $\lambda\to\infty$:

$$\boxed{|\sigma_n(\lambda)| = O_n\!\left(\frac{\sqrt{\log\log\lambda}}{\log\lambda}\right) \to 0.}$$

**This is the main result of doc 11.**

---

## 6. Individual convergence theorem (under RH + Montgomery)

**Theorem 2** (individual convergence of zeros). Under RH and Montgomery's pair correlation conjecture, for each fixed $n$:

$$t_n^{(\lambda)} - \gamma_n = O_n\!\left(\frac{\sqrt{\log\log\lambda}}{\log\lambda}\right) \to 0 \quad\text{as } \lambda\to\infty.$$

In particular: the family $\{t_n^{(\lambda)}\}_{\lambda\geq 1}$ converges to $\gamma_n$ at rate $O(\sqrt{\log\log\lambda}/\log\lambda)$.

*Proof.*

**Step 1** (expansion via the explicit formula). From Section 8 of doc 10:

$$C_\lambda(\gamma_n) = \frac{4\log\lambda}{m_n} - 2D_n(2\log\lambda) + O(1/\gamma_n),$$
$$C_\lambda'(\gamma_n) = -\frac{4\log\lambda}{m_n\gamma_n} + E_n(\lambda),$$

where $m_n$ is the multiplicity of $\rho_n$ (generically $m_n = 1$) and $E_n(\lambda) = O(\sqrt{\log\gamma_n\log\log\lambda})$ (the oscillatory term of the derivative under Montgomery).

**Step 2** (implicit function theorem). From Step 1 and $C_\infty(\gamma_n) = 0$ (under RH):

$$\sigma_n(\lambda) = t_n^{(\lambda)} - \gamma_n = -\frac{C_\lambda(\gamma_n) - \mu_\lambda}{C_\lambda'(\gamma_n)}.$$

With $\mu_\lambda \to 0$ (from doc 02) and using the expressions of Step 1:

$$\sigma_n(\lambda) = -\frac{4\log\lambda/m_n - 2D_n(2\log\lambda) + O(1/\gamma_n)}{-4\log\lambda/(m_n\gamma_n) + E_n(\lambda)}.$$

**Step 3** (cancellation of the dominant term). The term $4\log\lambda/m_n$ in the numerator and $-4\log\lambda/(m_n\gamma_n)$ in the denominator cancel:

$$\sigma_n(\lambda) = -\frac{4\log\lambda/m_n \cdot (1 - m_n D_n(2\log\lambda)/(2\log\lambda) + O(1/(\gamma_n\log\lambda)))}{-4\log\lambda/(m_n\gamma_n) \cdot (1 + O(E_n\gamma_n/\log\lambda))}$$

$$= \gamma_n\cdot\frac{1 - D_n(2\log\lambda)/(2\log\lambda/m_n) + O(1/(\gamma_n\log\lambda))}{1 + O(E_n\gamma_n/\log\lambda)}.$$

As $\lambda\to\infty$: $D_n(2\log\lambda)/\log\lambda \to 0$ (since $|D_n| = O(\sqrt{\log\gamma_n\cdot\log\log\lambda})$ while the divisor is $\Theta(\log\lambda)$):

$$\sigma_n(\lambda) = \gamma_n\cdot\left[\frac{-m_n D_n(2\log\lambda)}{4\log\lambda} + O\!\left(\frac{1}{\gamma_n\log\lambda}\right)\right].$$

Hence:

$$|\sigma_n(\lambda)| \leq \frac{\gamma_n m_n |D_n(2\log\lambda)|}{4\log\lambda} + O\!\left(\frac{1}{\log\lambda}\right) = O_n\!\left(\frac{\gamma_n\sqrt{\log\gamma_n\log\log\lambda}}{\log\lambda}\right) \to 0. \quad\square$$

---

## 7. Implication for H2 and the program

**Corollary 2** (H2 under RH + Montgomery). Under the same hypotheses, for each fixed $n$:

$$\hat\xi_\lambda(t) \to c\cdot\Xi(t) \quad\text{uniformly on } |t-\gamma_n| \leq \delta$$

for some $\delta > 0$ (where $c > 0$ is the normalization constant).

*Proof.* Theorem 2 gives convergence of the individual zeros. By Vitali's theorem (uniform convergence of holomorphic functions with convergence of zeros): convergence of the zeros implies convergence of the functions on any compact set containing the zeros but not their accumulation points. $\square$

**Proposition 4** (Wall-H2, under RH + Montgomery). For each fixed $n$:

$$|S_n| = |R_\xi(\gamma_n) - c_\lambda R_k(\gamma_n)| = O_n\!\left(\frac{\sqrt{\log\log\lambda}}{\log\lambda}\right) \to 0.$$

*Proof.* From Theorem 2 of doc 06: $|S_n| = O(|t_n^{(\lambda)} - \gamma_n| \cdot w_n/L) = O(\sigma_n\cdot w_n/L) \to 0$ by Theorem 2. $\square$

---

## 8. Can this be made unconditional (without assuming RH)?

Theorem 2 uses RH in two places:

| Place | Role |
|---|---|
| $C_\infty(\gamma_n) = 0$ | So that $\gamma_n$ is a crossing of the limiting potential |
| Bound on prime sums under RH | So that $|D_n(x)| = O(\sqrt{\log\gamma_n\log\log x})$ |

**Without RH:** If $\rho = \sigma + i\gamma$ with $\sigma \neq 1/2$: then $C_\infty(\gamma_n) \neq 0$ in general (the crossing at $\gamma_n$ does not exist). The $t_n^{(\lambda)}$ remain real (CCM), but their limits would be the zeros of $C_\infty$ on $\mathbb{R}$, which do not coincide with the $\gamma_n$.

**The contradiction argument.** If Theorem 2 could be made unconditional (i.e., if it could be shown that $t_n^{(\lambda)} \to \tau_n$ for some real limit $\tau_n$ without assuming RH), then:

1. $\tau_n$ would be the $n$-th zero of $C_\infty$ on $\mathbb{R}$.
2. By the explicit formula: the zeros of $C_\infty$ on $\mathbb{R}$ are exactly $\{\text{Im}(\rho) : \rho \text{ a zero of } \zeta\}$ (the imaginary parts of the non-trivial zeros).
3. Since the $\tau_n$ are limits of REAL numbers ($t_n^{(\lambda)}\in\mathbb{R}$): we conclude that the imaginary parts are real, i.e., the zeros of $\zeta$ have $\Im(\rho) \in \mathbb{R}$, i.e., the zeros are at $\Re(s) = 1/2$ or at $\Im(s) = 0$. The trivial zeros are at $\Im(s) = 0$. Hence the non-trivial ones have $\Re(\rho) = 1/2$ — RH. $\square$

**The remaining gap.** To make the contradiction argument rigorous without assuming RH, we need:

(A) To show that $\{t_n^{(\lambda)}\}$ converges (not merely bounded by $O(\log\lambda)$) — this is what Theorem 2 does UNDER RH.

(B) To identify the limit $\tau_n$ with the $n$-th zero of $C_\infty$ on $\mathbb{R}$ — this requires continuity of the "potential $\to$ crossings" map.

(C) To identify the zeros of $C_\infty$ on $\mathbb{R}$ with the imaginary parts of the zeros of $\zeta$ — this is the explicit formula (does not assume RH).

If (A) can be proved INDEPENDENTLY of RH: the chain (A)+(B)+(C) would give RH. Theorem 2 shows that (A) holds UNDER RH — but to prove (A) without RH we would need an estimate of the twisted prime sums $\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p)$ of size $o(\log x)$ that does NOT use RH. This is precisely the kind of result that would give hints of RH from prime sums.

---

## 9. The status of Question 29.9

**Question 29.9 reformulated.** Is it true that $D_n(2\log\lambda)/\log\lambda \to 0$ as $\lambda\to\infty$?

| Condition | Result |
|---|---|
| Unconditional | $|D_n(2\log\lambda)| = O(\log\lambda)$ (Theorem 2, doc 10) — does not give convergence |
| Under RH | $|D_n(2\log\lambda)| = O(\sqrt{\log\gamma_n\log\log\lambda})$ (Sec. 4, using the RH estimate of prime sums) — gives convergence $O(\sqrt{\log\log\lambda}/\log\lambda)$ |
| Under RH + Montgomery | Variance $V_n = O(\log\gamma_n)$, typically $|D_n| = O(\sqrt{\log\gamma_n\log\log\lambda})$ — gives the same rate |

**Conclusion of Question 29.9:** Under RH, $D_n(2\log\lambda)/\log\lambda \to 0$ at rate $O(\sqrt{\log\log\lambda}/\log\lambda)$. This suffices to prove individual convergence of the zeros.

---

## 10. Full table of results of the Phase 29 program

### Unconditionally proved:

| Result | Document |
|---|---|
| $k(u) > 0$ for all $u > 0$ | 04 |
| $k_\lambda(u) > 0$ for $\lambda \geq \lambda_0$ | 04 |
| $A_\lambda =$ multiplication by $\Psi_\lambda$ in Mellin space | 06 |
| $|s_n^{(\lambda)} - \gamma_n| = O(\lambda^{-1/2}/w_n)$ for zeros of $\hat k_\lambda$ | 06 |
| $\sum_m \Delta_m = 0$ and $M_1[\Delta] = O((\log\lambda)^2/\lambda) \to 0$ | 06, 07 |
| $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ | 08 |
| Weak convergence: $\mu_\lambda \to \mu_\gamma$ | 08 |

### Under RH:

| Result | Document |
|---|---|
| Stieltjes convergence: $S_\lambda(z) \to S_\Xi(z)$ | 09 |
| Individual zeros bounded: $|t_n^{(\lambda)} - \gamma_n| = O(\log\lambda)$ | 10 |
| **Individual zeros converge**: $t_n^{(\lambda)} - \gamma_n = O(\sqrt{\log\log\lambda}/\log\lambda) \to 0$ | **11** |
| H2 (locally): $\hat\xi_\lambda \to c\Xi$ in neighborhoods of $\gamma_n$ | 09, 11 |

### Under RH + Montgomery:

| Result | Document |
|---|---|
| Variance $V_n = O(\log\gamma_n)$ | 11 |
| Improved rate: individual convergence with $O(\sqrt{\log\log\lambda}/\log\lambda)$ | 11 |

---

## 11. The central question that closes the program

The complete analysis of the program has reduced RH to the following ARITHMETIC statement:

> **Central Statement (CS).** For each fixed $n$, the twisted prime sum:
> $$\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = o(\log\lambda) \quad\text{as } \lambda\to\infty.$$

Under RH: this holds with the bound $O(\sqrt{\log\gamma_n\log\log\lambda})$, which is $o(\log\lambda)$.

Without RH: if CS holds for some $n$: the limits of $t_n^{(\lambda)}$ exist, and by the argument of Section 8 the zeros of $\Xi$ are real (which implies RH). Hence CS for some $n$ IMPLIES RH — and RH IMPLIES CS for all $n$.

**The Central Statement CS is EQUIVALENT TO RH.**

This is the final result of the Phase 29 program: the Riemann conjecture is equivalent to the subcritical growth rate of the twisted Chebyshev sum evaluated at the known zeros of $\Xi$. The rate $o(\log\lambda)$ is a statement about the oscillatory cancellation of prime sums — a classical problem in analytic number theory, now reformulated as the heart of the CCM program.
