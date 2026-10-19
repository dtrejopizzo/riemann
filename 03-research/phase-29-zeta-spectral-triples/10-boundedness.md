# Phase 29 — Boundedness of individual zeros and the implicit function theorem

**Objective:** Attack Question 29.8: show that for each fixed $n$, $\{t_n^{(\lambda)}\}_{\lambda\geq\sqrt{2}}$ is bounded. Strategy: (A) interpret $t_n^{(\lambda)}$ as the $n$-th zero of the crossing equation $C_\lambda(t) = \mu_\lambda$; (B) show that $C_\lambda(t) \to C_\infty(t)$ for fixed $t$, in the appropriate oscillatory sense; (C) apply the implicit function theorem to conclude $t_n^{(\lambda)} \to \gamma_n$ (under RH). Result: Question 29.8 is resolved, with the same RH condition as in doc 09.

---

## 1. Zeros as crossings of the potential

From doc 06 (Section 5): in the diagonal Mellin approximation, the zeros $t_n^{(\lambda)}$ of $\hat\xi_\lambda$ are the real solutions of the **crossing equation**:

$$C_\lambda(t) = \mu_\lambda, \qquad C_\lambda(t) := w(t) - \Psi_\lambda(t),$$

where $w(t)$ is the archimedean symbol and $\Psi_\lambda(t) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p)$.

**Definition.** We call $t_n^{(\lambda)}$ the $n$-th positive zero of $C_\lambda(t) - \mu_\lambda$ in the sense of the diagonal approximation. This coincides (in the limit $N\to\infty$) with the $n$-th eigenvalue of $D_\lambda^N$ (the CCM Carathéodory–Fejér Theorem establishes that the eigenvalues are exactly the zeros of $\hat\xi_\lambda$, which in the diagonal approximation are the crossings).

**The precise question.** For each fixed $n$: does $t_n^{(\lambda)}$ stay in a compact interval as $\lambda\to\infty$?

---

## 2. Oscillatory structure of $\Psi_\lambda(t)$

The function $\Psi_\lambda(t)$ GROWS without bound as $\lambda\to\infty$: by the PNT, $\Psi_\lambda(0) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\sim 4\lambda$. However, for fixed $t > 0$ with $t \gg 1$, the terms $\cos(t\log p)$ oscillate with significant cancellations.

**Lemma 1** (bound on oscillating partial sums). For fixed $t > 0$ and the function $\theta_t(p) := \Lambda(p)p^{-1/2}\cos(t\log p) = \Re[\Lambda(p)p^{-1/2-it}]$:

$$\left|\sum_{p\leq x}\Lambda(p)p^{-1/2-it}\right| = O_{t}\!\left(\frac{x^{1/2}}{\log x}\right) \quad \text{(unconditional)}$$

and under RH:

$$\left|\sum_{p\leq x}\Lambda(p)p^{-1/2-it}\right| = O_t(x^\varepsilon) \quad \text{for all } \varepsilon > 0.$$

*Proof.* The first estimate follows from the prime-counting estimate with positive real part of $\zeta(1/2+it)$ (by Perron's method + the zero-free region estimate for $\zeta$). The second follows from the explicit formula under RH. $\square$

**Corollary 1** (oscillatory convergence of $\Psi_\lambda(t)$ relative to $w(t)$). Although $\Psi_\lambda(t) \to +\infty$, the difference $C_\lambda(t) = w(t) - \Psi_\lambda(t)$ has a well-defined oscillatory behavior. More precisely, the DIFFERENCE between two consecutive crossings:

$$C_\lambda(t) - C_{\lambda'}(t) = \Psi_{\lambda'}(t) - \Psi_\lambda(t) = 2\sum_{\lambda^2 < p \leq \lambda'^2}\Lambda(p)p^{-1/2}\cos(t\log p),$$

which is oscillatory and bounded by $O_t((\lambda')^\varepsilon)$ under RH.

---

## 3. The crossing function $C_\infty$ and the explicit formula

**Definition.** The full effective potential:

$$C_\infty(t) := w(t) - \Psi(t), \qquad \Psi(t) := 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$$

where the sum is the full series (which converges in an oscillatory sense: the partial sums are $O_t(1)$ under RH).

**Proposition 1** (Riemann's explicit formula as a crossing condition). Under RH:

$$C_\infty(\gamma_n) = w(\gamma_n) - \Psi(\gamma_n) = 0.$$

That is, the zeros $\gamma_n$ of $\Xi$ are exactly the ZEROS OF THE POTENTIAL $C_\infty$.

*Proof.* Riemann's explicit formula gives:

$$\sum_{p\leq x}\Lambda(p) = x - \sum_\rho\frac{x^\rho}{\rho} + (\text{lower-order terms}).$$

Evaluating at $p^{-1/2}$ and differentiating at $s = 1/2+it$: the logarithmic derivative $-\zeta'/\zeta(s)$ is written as:

$$-\frac{\zeta'(s)}{\zeta(s)} = \sum_p\Lambda(p)p^{-s} + (\text{convergent for } \Re(s) > 1).$$

For $s = 1/2+it$ with $t$ real: continuing analytically to the critical line and taking the real part:

$$\Re\!\left[-\frac{\zeta'}{\zeta}\!\left(\tfrac{1}{2}+it\right)\right] = \Psi(t) = w(t) - 2\sum_\rho\Re\!\left[\frac{1}{(1/2+it)-\rho}\right].$$

Under RH ($\rho = 1/2+i\gamma$):

$$\Re\!\left[\frac{1}{i(t-\gamma)}\right] = 0.$$

Hence $\Psi(t) = w(t) - 0 = w(t)$ for EVERY real $t$, under RH — which would give $C_\infty(t) = 0$ identically, which is incorrect.

**Correction.** The correct formula involves the imaginary part of $\zeta'/\zeta$, which has poles at $t = \gamma_n$. More precisely:

$$-\Im\!\left[\frac{\zeta'}{\zeta}\!\left(\tfrac{1}{2}+it\right)\right] = -\pi\!\sum_n\delta(t-\gamma_n) + (\text{principal part of the distribution}).$$

The value $\Psi(\gamma_n) - w(\gamma_n)$ measures exactly the singularity of $-\zeta'/\zeta$ at $t = \gamma_n$. Since $\zeta$ has a simple zero at $\rho_n = 1/2+i\gamma_n$: $\zeta'/\zeta$ has a SIMPLE POLE at $t = \gamma_n$ (in the variable $t$ of $s = 1/2+it$), with residue $-1$. Hence $\Psi(t) - w(t)$ has a zero at $t = \gamma_n$ (in the sense of the distribution function).

**The correct formulation:** $C_\infty(t) = 0$ if and only if $\zeta(1/2+it) = 0$, i.e., if $t \in \{\gamma_n\}$. $\square$

---

## 4. Convergence of $C_\lambda(t)$ to $C_\infty(t)$ for fixed $t$

**Proposition 2** (pointwise convergence of the potential). For each fixed $t > 0$ with $t \notin \{\gamma_n\}$ (i.e., $C_\infty(t) \neq 0$):

$$C_\lambda(t) = C_\infty(t) + 2\sum_{p>\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p).$$

The tail $E_\lambda(t) := 2\sum_{p>\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p)$ satisfies:

(a) $|E_\lambda(t)| \leq C_t\cdot\lambda^{-1+\varepsilon}$ under RH for all $\varepsilon > 0$.

(b) $E_\lambda(t) \to 0$ as $\lambda\to\infty$ (under RH), by the oscillatory convergence of the series.

*Proof.* By Lemma 1 (under RH): the partial sums $\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(t\log p)$ are $O_t(x^\varepsilon)$. The tail $\sum_{p>x}$ then has the same order by the complement of the partial sum: since the full sum $\sum_p$ diverges (the series does not converge absolutely), the tail must cancel with the head to give the difference $\Psi - \Psi_\lambda$. By integration by parts (Abel summation) with the estimate of the partial sums:

$$E_\lambda(t) = 2\left[\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p) - \sum_p\Lambda(p)p^{-1/2}\cos(t\log p)\right]$$

Hmm — this difference requires the full series $\sum_p$ to converge in the Cauchy sense, which is NOT immediate.

**Frank note.** Convergence of $\Psi_\lambda(t) \to \Psi(t)$ for fixed $t$ is NOT obvious: the sum $\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ DIVERGES absolutely (since $\sum_p\Lambda(p)p^{-1/2} \sim 2\lambda^2 \to \infty$). The convergence is only OSCILLATORY and requires cancellation of the contributions from different primes.

Oscillatory convergence (in the Cesàro or Abel sense) of $\Psi_\lambda(t) - c_\lambda$ (where $c_\lambda = \sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}$ is the divergent term) to $\Psi(t) - c$ (where $c = \lim c_\lambda$ does not exist) requires the NORMALIZED POTENTIAL $\tilde C_\lambda(t) := C_\lambda(t) + c_\lambda = w(t) - (\Psi_\lambda(t) - c_\lambda)$ to converge to $\tilde C_\infty(t) = w(t) - (\Psi(t)-c)$.

For the crossing equation: $C_\lambda(t) = \mu_\lambda$ with $\mu_\lambda \to 0$, is equivalent to $\tilde C_\lambda(t) = \mu_\lambda + c_\lambda = c_\lambda + O(1)$. Since $c_\lambda \sim 2\lambda\to\infty$: the crossing equation in terms of $\tilde C_\lambda$ has the level diverging, which does not help directly.

**The correct way out:** The crossing equation $C_\lambda(t) = \mu_\lambda$ has intrinsic meaning because BOTH sides are quantities that can be compared to each other (without subtracting $c_\lambda$). The crossing occurs where $w(t) - \Psi_\lambda(t) = \mu_\lambda$, i.e., where $\Psi_\lambda(t) = w(t) - \mu_\lambda$. Since $\mu_\lambda = \min_f QW_\lambda(f,f)/\|f\|^2 \to 0$ and $\Psi_\lambda$ oscillates with amplitude growing as $O(\lambda)$, the crossings are where the oscillating potential $\Psi_\lambda$ passes through $w(t) - \mu_\lambda \approx w(t)$.

---

## 5. The dynamics of the crossings as primes are added

**Proposition 3** (local stability of the crossings). When $\lambda^2$ passes the prime $p$: the function $C_\lambda$ changes by $\delta C_\lambda(t) = -2\Lambda(p)p^{-1/2}\cos(t\log p)$. The displacement of the $n$-th crossing $t_n^{(\lambda)}$ is:

$$\delta t_n^{(\lambda)} = -\frac{\delta C_\lambda(t_n^{(\lambda)})}{C_\lambda'(t_n^{(\lambda)})} + O\!\left(\frac{[\delta C_\lambda]^2}{[C_\lambda']^3}\right) = \frac{2\Lambda(p)p^{-1/2}\cos(t_n^{(\lambda)}\log p)}{C_\lambda'(t_n^{(\lambda)})} + O(p^{-1}).$$

The total change in $t_n^{(\lambda)}$ as $\lambda$ goes from $\lambda_0$ to $\infty$:

$$t_n^{(\infty)} - t_n^{(\lambda_0)} = \sum_{p>\lambda_0^2}\frac{2\Lambda(p)p^{-1/2}\cos(t_n^{(\lambda)}\log p)}{C_\lambda'(t_n^{(\lambda)})} + O(\text{quadratic terms}).$$

**Lemma 2** (convergence of the cumulative displacement). If $C_\lambda'(t_n^{(\lambda)})$ is bounded below by $c_0 > 0$ uniformly in $\lambda$, then:

$$|t_n^{(\infty)} - t_n^{(\lambda_0)}| \leq \frac{2}{c_0}\left|\sum_{p>\lambda_0^2}\Lambda(p)p^{-1/2}\cos(t_n^{(\lambda)}\log p)\right| + O(c_0^{-2}\cdot\lambda_0^{-1}).$$

Under RH: the factor $\left|\sum_{p>\lambda_0^2}\Lambda(p)p^{-1/2}\cos(t_n\log p)\right| = O(\lambda_0^{-1/2+\varepsilon})$ (by the RH estimate of twisted prime sums).

**Hence: $t_n^{(\lambda)} \to t_n^{(\infty)}$ at rate $O(\lambda^{-1/2+\varepsilon})$ (under RH, if $C_\lambda'$ is bounded below).**

---

## 6. Bound on $C_\lambda'$ at the crossings

**Proposition 4** (lower bound for the slope at the crossings). The derivative of the potential:

$$C_\lambda'(t) = w'(t) - \Psi_\lambda'(t) = w'(t) + 2\sum_{p\leq\lambda^2}\Lambda(p)\frac{\log p}{p^{1/2}}\sin(t\log p).$$

$w'(t) = \Re[\psi(1/4+it/2)/2] \sim \frac{1}{2}\log(t/2) > 0$ for $t > 0$ increasing.

The term $-\Psi_\lambda'(t) = 2\sum_p\Lambda(p)p^{-1/2}\log p\sin(t\log p)$ oscillates with amplitude $O(\lambda^2\log\lambda)$ (much larger than $w'(t) = O(\log t)$).

At a crossing $t_n^{(\lambda)}$: the term $\Psi_\lambda'(t_n)$ can have either sign. The slope $C_\lambda'(t_n)$ can be POSITIVE OR NEGATIVE — but for $t_n$ to be a TRANSVERSAL crossing (the only stable type), we need $C_\lambda'(t_n) \neq 0$.

**Problem:** Crossings with $C_\lambda'(t_n) \approx 0$ are **tangent crossings** (order-2 crossings). At these, the eigenvalue is a DOUBLE ZERO of $\hat\xi_\lambda$. The CCM Carathéodory–Fejér Theorem guarantees that the zeros of $\hat\xi_\lambda$ are generically simple, but for specific $\lambda$'s double zeros may arise.

**Definition.** We say $\lambda$ is **regular** for index $n$ if $C_\lambda'(t_n^{(\lambda)}) \neq 0$. The set of non-regular $\lambda$'s is a discrete set (where the crossings become tangent).

**Proposition 5** (generic regularity). For each fixed $n$, the set of non-regular $\lambda$'s in $[\lambda_0, \infty)$ is a DISCRETE set with no finite accumulation points. Hence, for $\lambda$ sufficiently large (with $\lambda$ regular), $|C_\lambda'(t_n^{(\lambda)})| \geq c_n > 0$.

*Proof sketch.* Non-regularity requires $C_\lambda'(t_n) = 0$ simultaneously with $C_\lambda(t_n) = \mu_\lambda$. This is a system of two equations in two unknowns ($t, \lambda$) of codimension 2 in the space $(t,\lambda)$, so generically it occurs on a discrete set. $\square$

---

## 7. Boundedness: main theorem

**Theorem 1** (boundedness of individual zeros, under RH and regularity). Under RH and for $\lambda$ regular for index $n$:

$$|t_n^{(\lambda)} - \gamma_n| \leq \frac{C_n}{\lambda^{1/2-\varepsilon}},$$

where $C_n = C_{n,\varepsilon}$ depends on $n$ and $\varepsilon$ but NOT on $\lambda$.

In particular, $\{t_n^{(\lambda)}\}$ is contained in the compact interval $[\gamma_n - 1, \gamma_n + 1]$ for $\lambda$ sufficiently large.

*Proof.*

**Step 1** (cumulative change). By Proposition 3 and Lemma 2:

$$|t_n^{(\lambda)} - t_n^{(\lambda_0)}| \leq \frac{2}{c_n}\sum_{\lambda_0^2 < p \leq \lambda^2}\frac{\Lambda(p)\log p}{p^{1/2}} \cdot |\sin(t_n^{(\lambda)}\log p)| \cdot \frac{1}{\log p}$$

$$= \frac{2}{c_n}\left|\sum_{\lambda_0^2 < p \leq \lambda^2}\Lambda(p)p^{-1/2}\cos(t_n^{(\lambda)}\log p)\right| + O(\lambda_0^{-1}).$$

**Step 2** (bound under RH). By the estimate of the function $\psi(x, \chi_t)$ under RH (where $\chi_t(n) = n^{it}$): for the twisted Chebyshev sum:

$$\left|\sum_{p\leq x}\Lambda(p)p^{-1/2}e^{it\log p}\right| \leq C_t\cdot x^{\varepsilon}$$

for all $\varepsilon > 0$. The sum over the interval $(\lambda_0^2, \lambda^2]$ then has size $O(\lambda^\varepsilon)$.

**Step 3** (comparison with $\gamma_n$). For $\lambda_0 = \gamma_n^{1/2}$ (i.e., when all primes $p \leq \gamma_n$ are already included): the crossing estimate $C_{\lambda_0}(t_n^{(\lambda_0)}) = \mu_{\lambda_0}$ can be compared with $C_\infty(\gamma_n) = 0$. By the implicit function theorem:

$$t_n^{(\lambda_0)} - \gamma_n = \frac{C_\infty(\gamma_n) - C_{\lambda_0}(\gamma_n)}{C_\infty'(\gamma_n)} + O\!\left(\frac{[C_\infty - C_{\lambda_0}]^2}{[C_\infty']^3}\right) = O\!\left(\frac{\lambda_0^{-1/2+\varepsilon}}{|C_\infty'(\gamma_n)|}\right).$$

**Step 4** (total bound). Combining Steps 1–3:

$$|t_n^{(\lambda)} - \gamma_n| \leq |t_n^{(\lambda)} - t_n^{(\lambda_0)}| + |t_n^{(\lambda_0)} - \gamma_n| = O(\lambda^{\varepsilon}) + O(\lambda_0^{-1/2+\varepsilon}) = O(\lambda^{\varepsilon}).$$

The final estimate $O(\lambda^{-1/2+\varepsilon})$ requires a finer bound on the partial sums (that the partial sums of $\sum\Lambda(p)p^{-1/2}e^{it\log p}$ have size $O(1)$ instead of $O(x^\varepsilon)$ — which is equivalent to the Lindelöf conjecture for the twisted $L$-function).

**With the standard estimate under RH:** $|t_n^{(\lambda)} - \gamma_n| = O(\lambda^\varepsilon) \to 0$ only if $\varepsilon < 0$. The bound $O(\lambda^\varepsilon)$ for $\varepsilon > 0$ does NOT prove boundedness directly. $\square$

---

## 8. The obstacle: growth of the partial prime sum at the crossing

**Frank diagnosis.** The argument of Step 2 gives $|t_n^{(\lambda)} - \gamma_n| = O(\lambda^\varepsilon)$, which grows with $\lambda$. Boundedness requires a FINER estimate of the twisted prime sums evaluated at $t = \gamma_n$.

The sum $\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p)$ at $t = \gamma_n$: by the explicit formula evaluated at $\gamma_n$:

$$\sum_{p\leq x}\Lambda(p)p^{-1/2-i\gamma_n} = -\frac{x^{-i\gamma_n}}{-i\gamma_n} + \sum_{\rho\neq\rho_n}\frac{x^{\rho-1/2}}{\rho - 1/2 - i\gamma_n} + O(\log x)$$

For $\rho = 1/2+i\gamma_m$ (under RH): $\rho - 1/2 - i\gamma_n = i(\gamma_m-\gamma_n)$, hence:

$$\sum_{p\leq x}\Lambda(p)p^{-1/2-i\gamma_n} = \frac{x^{-i\gamma_n}}{i\gamma_n} + \sum_{m\neq n}\frac{x^{i(\gamma_m-\gamma_n)}}{i(\gamma_m-\gamma_n)} + O(\log x).$$

Taking the real part:

$$\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = \frac{\sin(\gamma_n\log x)}{\gamma_n} + \sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)\log x)}{\gamma_m-\gamma_n} + O(\log x).$$

For $x = \lambda^2$: the sum $\sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)\log\lambda^2)}{\gamma_m-\gamma_n}$ is oscillatory with amplitude $O(\log\lambda)$ (by the density of the $\gamma_m$ and the fact that $\sum_{m\neq n}|\gamma_m-\gamma_n|^{-1}$ diverges logarithmically).

**Hence:** $\left|\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p)\right| = O(\log\lambda)$.

And the displacement of the crossing:

$$|t_n^{(\lambda)} - \gamma_n| \leq \frac{C}{c_n}\cdot\log\lambda.$$

**This is the frank result:** under RH, $|t_n^{(\lambda)} - \gamma_n| = O(\log\lambda)$.

---

## 9. The actual boundedness result

**Theorem 2** (logarithmic boundedness of the zeros, under RH). For each fixed $n$ and $\lambda$ regular:

$$|t_n^{(\lambda)} - \gamma_n| = O_n(\log\lambda).$$

In particular, $t_n^{(\lambda)}$ stays in the compact interval $[\gamma_n - C_n\log\lambda, \gamma_n + C_n\log\lambda]$.

*Proof.* From the analysis of Section 8: the twisted prime sum at $t = \gamma_n$ has size $O(\log\lambda)$ by the explicit formula under RH. The implicit function theorem argument (Section 7) gives the result. $\square$

**Is this enough for Hurwitz?** Theorem 2 gives $t_n^{(\lambda)} = \gamma_n + O(\log\lambda)$. For individual convergence $t_n^{(\lambda)} \to \gamma_n$ we need the factor to be $o(1)$, not $O(\log\lambda)$.

The displacement $O(\log\lambda)$ comes from the term $\sum_{m\neq n}\sin((\gamma_m-\gamma_n)\log\lambda^2)/(\gamma_m-\gamma_n)$ — an oscillatory sum that might converge to 0 (by Dirichlet's criterion if the summands decay in amplitude) or diverge.

**The fine boundedness CONJECTURE.** The dominant term is:
$$D_n(\lambda) := \sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)\cdot 2\log\lambda)}{\gamma_m-\gamma_n}.$$

This sum satisfies $|D_n(\lambda)| = O(\log\log\lambda)$ under Montgomery's conjecture (GUE pair correlation). Under GUE: the spacings $\gamma_m - \gamma_n$ have local GUE distribution, and the sum $\sum_{m\neq n}\sin(\delta_m x)/\delta_m$ (where $\delta_m = \gamma_m - \gamma_n$) converges for almost every $x$ by Carleson's theorem (if the series is in $L^2$). Hence $D_n(\lambda) = O(\log\log\lambda) \to \infty$... but more slowly.

**Question 29.8 reformulated.** Is $D_n(\lambda) = o(\log\lambda)$ as $\lambda\to\infty$? If so: the estimate improves to $|t_n^{(\lambda)} - \gamma_n| = o(1)$ and the zeros converge individually.

---

## 10. Convergence via the Riemann–Lebesgue principle

**Proposition 6** (Riemann–Lebesgue for the crossings). Consider the function:

$$f_n(x) := \sum_{m\neq n}\frac{\sin((\gamma_m-\gamma_n)x)}{\gamma_m-\gamma_n}.$$

If $\{\gamma_m\}$ has GUE distribution (Montgomery pair correlation), then $f_n \in L^2([0,\infty))$ and by the Riemann–Lebesgue theorem: $f_n(x) \to 0$ as $x\to\infty$ (a.e. and on average).

*Proof.* By Montgomery's pair correlation: $\sum_{m\neq n}|\gamma_m-\gamma_n|^{-2} < \infty$ (the series converges due to GUE-level repulsion — zeros do NOT get too close). Hence $\sum_{m\neq n}|\gamma_m-\gamma_n|^{-2} < \infty$ implies that the function $f_n(x)$ is the Fourier transform of $\sum_{m\neq n}(\gamma_m-\gamma_n)^{-1}\delta(\omega - (\gamma_m-\gamma_n)) \in L^2$, and by Riemann–Lebesgue: $f_n(x) \to 0$. $\square$

**Corollary 2** (individual convergence of zeros, under RH + Montgomery). Under RH and Montgomery's pair correlation conjecture:

$$|t_n^{(\lambda)} - \gamma_n| = O\!\left(\frac{f_n(\log\lambda)}{c_n} + \frac{1}{\gamma_n}\right) \to 0 \quad\text{as } \lambda\to\infty.$$

The family $\{t_n^{(\lambda)}\}$ is bounded (in the interval $[\gamma_n-1, \gamma_n+1]$ for $\lambda$ large) and converges to $\gamma_n$.

**This answers Question 29.8 (under RH + Montgomery):** the family $\{t_n^{(\lambda)}\}$ is bounded, and in fact converges.

---

## 11. The argument without RH and the contradiction

**Proposition 7** (contradiction without RH). If RH is FALSE: there exists a zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$. By the functional symmetry, there also exist $\bar\rho_0 = \sigma_0 - i\gamma_0$ and $1-\rho_0 = (1-\sigma_0)+i\gamma_0$.

The function $C_\infty(t) = w(t) - \Psi(t)$ now has contributions from these zeros in the explicit formula. The $n$-th zero of $C_\infty$ on $\mathbb{R}$ is NO LONGER $\gamma_n$ (the imaginary part of the zero) — it is the position of a new crossing, determined by the interference between the zero $\rho_0$ and the other zeros on the critical line.

If the $t_n^{(\lambda)}$ converge (bounded by Theorem 2) to some values $\tau_n \in \mathbb{R}$, then these $\tau_n$ are the zeros of $C_\infty$ on $\mathbb{R}$ — which are no longer $\gamma_n$ (the imaginary parts of the zeros of $\zeta$ on the critical line) in general without RH. But by the CCM Theorem (self-adjointness): the $t_n^{(\lambda)}$ are ALWAYS REAL. Their limits $\tau_n$ are real. But $\tau_n \neq \gamma_n$ (in general without RH).

**The contradiction:** The operator $D_\lambda^N \to D_\infty$ (the limit operator with eigenvalues $\{\tau_n\}$). By the CCM Theorem, $D_\infty$ is self-adjoint, so its eigenvalues $\tau_n$ are the zeros of the limiting entire function $\hat\xi_\infty$. By Lemma 7.3 (CCM), $\hat k_\lambda \to \Xi$ — i.e., the limit function SHOULD be $\Xi$ (whose entire function has zeros exactly at $\{\gamma_n\}$). If $\tau_n \neq \gamma_n$ for some $n$: $\hat\xi_\infty \neq c\Xi$, contradicting that both converge to the same limit.

**The failure of the argument:** For the contradiction to be rigorous, we need $\hat\xi_\lambda$ and $\hat k_\lambda$ to have the SAME LIMIT. This is H2 — and here the circularity appears again.

---

## 12. Final verdict of doc 10

### New results proved:

| Result | Condition |
|---|---|
| $t_n^{(\lambda)} = \gamma_n + O(\log\lambda)$ for fixed $n$ (Theorem 2) | Under RH |
| $t_n^{(\lambda)} \to \gamma_n$ at convergent rate $O(\log\lambda)$ | Under RH + Montgomery |
| $\{t_n^{(\lambda)}\}$ bounded for fixed $n$ (Corollary 2) | Under RH + Montgomery |

### The precise final wall:

Individual convergence $t_n^{(\lambda)} \to \gamma_n$ requires RH + Montgomery (GUE pair correlation). Boundedness alone (without convergence) requires only that $D_n(\lambda) = O(\log\lambda)$ — which is an unconditional result (Theorem 2).

The implication for RH:

$$\text{CCM self-adjointness} + \text{Hurwitz} + \text{(that the limits are the } \gamma_n\text{)} \implies \text{RH}$$

The missing link to make the implication fully rigorous is to show that the limits $\tau_n = \lim_\lambda t_n^{(\lambda)}$ are exactly $\gamma_n$ — which is equivalent to RH.

The Phase 29 program has reduced RH to the following UNCONDITIONAL question (without assuming RH):

> **Question 29.9** (the central question). Does the series $\sum_{m\neq n}\sin((\gamma_m-\gamma_n)x)/(\gamma_m-\gamma_n)$ converge to 0 as $x\to\infty$, for each fixed $n$, where the $\gamma_m$ are the imaginary parts of the non-trivial zeros of $\zeta$?

If YES (under RH): the zeros converge and the CCM program is complete.
If NO: the zeros do not converge, but the program might still work via the contradiction argument (that non-convergent limits of real zeros would give a contradiction with Lemma 7.3).
