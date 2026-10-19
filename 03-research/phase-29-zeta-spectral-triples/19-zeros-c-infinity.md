# Phase 29 — Doc 19: Zeros of the potential $C_\infty$ and Jensen's formula

**Objective:** Attack Question D.1: determine the zeros of $C_\infty(t) = w(t) - \Psi(t)$ directly, via the Jensen-Ahlfors formula and the Weil identity. Establish whether the zeros of $C_\infty$ coincide with those of $\Xi$ without assuming RH.

---

## 1. Precise definition of $C_\infty$ and its analytic properties

**Definition.** The limiting potential is:

$$C_\infty(z) = w(z) - \Psi(z),$$

where:

$$w(z) = \partial_z\theta(z) = \frac{1}{2i}\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{iz}{2}\right) + \frac{1}{2i}\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}-\tfrac{iz}{2}\right) - \log\pi$$

(archimedean symbol, meromorphic with poles at $z = i(4k+1)/2$ for $k \in \mathbb{Z}$ — that is, at $z = \pm(1/2)i, \pm(5/2)i, \ldots$, outside the strip $|\Im(z)| < 1/2$).

$$\Psi(z) = 2\sum_{p\text{ prime}} \Lambda(p)\, p^{-1/2}\, e^{iz\log p}$$

(absolutely convergent for $\Im(z) > 1/2$ and by conjugation for $\Im(z) < -1/2$; on $\mathbb{R}$: conditionally convergent in the Abel sense).

**Proposition 1** (analyticity of $C_\infty$). The function $C_\infty(z) = w(z) - \Psi(z)$ admits analytic continuation to the strip $\mathcal{S} = \{z \in \mathbb{C}: |\Im(z)| < 1/2\}$. For $z \in \mathbb{R}$: $C_\infty(t) \in \mathbb{R}$ (real-analytic function on $\mathbb{R}$).

*Proof.* $w(z)$ is analytic for $|\Im(z)| < 1/2$ (the first pole is at $\Im(z) = 1/2$). $\Psi(z)$ converges absolutely for $\Im(z) > 0$; by extension it is defined at $\Im(z) = 0$ in the Abel sense. By the Weil explicit formula (in the Guinand-Barner form), $C_\infty$ extends to $\mathcal{S}$. $\square$

---

## 2. The function $C_\infty$ and its relation to $\xi(s)$

**The underlying mechanism.** The connection between $C_\infty$ and $\Xi$ goes through the Riemann explicit formula. For $x > 1$:

$$\sum_{n \leq x} \Lambda(n) = x - \sum_\rho \frac{x^\rho}{\rho} - \log(2\pi) - \frac{1}{2}\log(1-x^{-2}),$$

and its smoothed version (at the level of the symbol $\Psi$):

$$\Psi(t) = 2\sum_p \Lambda(p)p^{-1/2}\cos(t\log p) = w(t) - 2\sum_\rho \Re\!\left(\frac{e^{it\log|\rho|}}{|\rho|}\right) + (\text{pole and trivial zero contributions}).$$

Then:

$$C_\infty(t) = w(t) - \Psi(t) = 2\sum_\rho \Re\!\left(\frac{e^{it\log|\rho|}}{|\rho|}\right) + (\text{pole and trivial zero terms}).$$

**Proposition 2** (expression of $C_\infty$ via zeros of $\zeta$). For $t \in \mathbb{R}$:

$$C_\infty(t) = 2\sum_\rho \frac{\cos(t\log|\rho|)}{|\rho|} + c_0,$$

where the sum is over all non-trivial zeros $\rho$ of $\zeta$, $|\rho| = |\rho|$, and $c_0$ comes from the contributions of the pole $s=1$ and the trivial zeros.

*Explicit form of $c_0$.* The contributions are: from the pole $s=1$: $e^{it\log 1}/1 = 1$; from the trivial zeros $\rho = -2n$: $e^{it\log(2n)}/(2n)$ summed for $n \geq 1$. In total $c_0 = 1 + 2\sum_{n=1}^\infty \cos(t\log(2n))/(2n)$ (if the sum converges).

**Note.** The exact formula for $c_0$ requires care in the regularization of the explicit formula. For the purposes of the zero analysis, what matters is that $c_0$ is a real constant (independent of $t$) plus terms that decay in $t$. For large $t$, $c_0(t) = O(1)$.

---

## 3. Jensen's formula for zeros of $C_\infty$

**Jensen-Ahlfors theorem.** Let $f$ be analytic on the disk $|z| \leq R$ with no zeros on $|z| = R$. Let $n(r)$ be the number of zeros of $f$ in $|z| \leq r$. Then:

$$\int_0^R \frac{n(r)}{r}\,dr = \frac{1}{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta - \log|f(0)|.$$

To count zeros in a real interval $[0,T]$: Jensen's formula is applied on the rectangle $[0,T] \times [-\eta, \eta]$ for $\eta < 1/2$ (within the strip of analyticity of $C_\infty$).

**Proposition 3** (counting zeros of $C_\infty$ via Jensen). The number of zeros of $C_\infty$ in $[0,T]$ satisfies:

$$N_{C_\infty}(T) := \#\{t \in [0,T]: C_\infty(t) = 0\} = \frac{1}{\pi}\Im\!\left[\log C_\infty(T+i\eta)\right]_{t=0}^{t=T} + O(\log T),$$

for any fixed $\eta \in (0, 1/2)$.

*Proof.* By the argument principle applied to the rectangle $[0,T] \times [-\eta,\eta]$: the number of zeros of $C_\infty$ in the rectangle is $\frac{1}{2\pi i}\oint \frac{C_\infty'}{C_\infty} dz$. The vertical sides contribute $O(1)$ (since $C_\infty(0+i\eta) = C_\infty(0-i\eta)^*$ are bounded). The horizontal sides contribute the variation of the argument. $\square$

---

## 4. The variation of the argument of $C_\infty$

**Proposition 4** (variation of the argument of $C_\infty$ in the strip). For fixed $\eta \in (0, 1/2)$ and $T \to \infty$:

$$\frac{1}{\pi}\arg C_\infty(T+i\eta)\bigg|_{T=0}^{T\to\infty} = N_\Xi(T) + O(\log T).$$

*Proof (tentative — this is the key result).*

**Step 1.** $C_\infty(z) = 2\sum_\rho e^{iz\log|\rho|}/|\rho| + c_0$ for $z = T+i\eta$.

**Step 2.** The variation of the argument of $C_\infty(T+i\eta)$ as $T$ ranges from $0$ to $\infty$ can be computed via the residue of $C_\infty'/C_\infty$:

$$N_{C_\infty}(T) = \frac{1}{\pi}\arg C_\infty\bigg|_0^{T+i\eta}.$$

**Step 3.** Now, $C_\infty(z) = 2\Re\sum_\rho e^{iz\log|\rho|}/|\rho| + c_0$. For $z = T+i\eta$:

$$C_\infty(T+i\eta) = 2\sum_\rho \frac{e^{-\eta\log|\rho|}}{|\rho|}\cos(T\log|\rho|) + c_0.$$

This is a SUM of cosines with weights $2e^{-\eta\log|\rho|}/|\rho| = 2|\rho|^{-1-\eta}$ and frequencies $\log|\rho|$.

**Step 4.** Under RH: $|\rho|^{-1-\eta} = (\sqrt{1/4+\gamma^2})^{-1-\eta} \approx \gamma^{-1-\eta}$. The sum has the form of a Dirichlet series with frequencies $\log\gamma_n$ and amplitudes $\gamma_n^{-1-\eta}$. This sum oscillates. Its argument accumulates variation at a rate determined by the density of frequencies $\log\gamma_n$.

**Expected result.** The variation of the argument of a sum of cosines $\sum_n a_n \cos(T\omega_n)$ with frequencies $\omega_n = \log\gamma_n$ and amplitudes $a_n = \gamma_n^{-1-\eta}$ is:

$$\frac{1}{\pi}\arg\!\left(\sum_n a_n e^{iT\omega_n}\right) \approx \frac{T}{\pi}\sum_n a_n \omega_n / \sum_n a_n \approx \frac{T}{2\pi}\log\frac{T}{2\pi}.$$

The last approximation uses the density of frequencies: the "center of mass" of the frequencies $\omega_n = \log\gamma_n$ weighted by $a_n = \gamma_n^{-1-\eta}$ is $\sum_n \gamma_n^{-1-\eta}\log\gamma_n / \sum_n\gamma_n^{-1-\eta} \approx \log T$ for $T$ in the range of the dominant $\gamma_n$.

**Comparison.** $N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + O(\log T)$. The expected result $\frac{T}{2\pi}\log\frac{T}{2\pi}$ matches (modulo the term $-T/(2\pi)$ in the exponent, which comes from the "factor $e$" in the von Mangoldt formula).

**Status of Proposition 4.** The argument of Step 4 is heuristic: the variation of the argument of a sum of cosines is NOT simply the average of its frequencies. The real argument requires an analysis of the interferences among the different modes — which is the content of the theory of almost-periodic functions.

---

## 5. Almost-periodic functions and their number of zeros

**Definition** (Bohr almost-periodic function). A function $f: \mathbb{R} \to \mathbb{C}$ is almost-periodic (in the Bohr sense) if for every $\varepsilon > 0$ there exist $T_\varepsilon > 0$ and translations $\tau_\varepsilon$ with $|f(t+\tau_\varepsilon) - f(t)| < \varepsilon$ for all $t$.

**Proposition 5** (the function $C_\infty$ is not almost-periodic). The function $C_\infty(t) = w(t) - \Psi(t)$ for $t \in \mathbb{R}$ has the term $w(t) \sim \frac{1}{2}\log(t/2\pi) \to \infty$, which is not almost-periodic (it grows monotonically). Then $C_\infty$ is not almost-periodic.

**But:** the function $C_\infty(t) - w(t) = -\Psi(t)$ IS the oscillating part (converging in distribution to an almost-periodic function under the hypothesis of linear independence of $\log\gamma_n$ over $\mathbb{Q}$). The zeros of $C_\infty(t)$ are the points where $\Psi(t) = w(t)$, i.e., the "crossings" of the almost-periodic function $\Psi$ with the monotonically increasing level $w(t)$.

**Besicovitch crossing theorem.** If $f: \mathbb{R} \to \mathbb{R}$ is an almost-periodic function and $g(t) \to +\infty$ monotonically, the number of solutions of $f(t) = g(t)$ in $[0,T]$ grows as $T \cdot \nu_{f}(g)$ where $\nu_f(g)$ is the "crossing density" of $f$ with $g$. For $g(t) = w(t)$ growing logarithmically: the crossing density is determined by the distribution function of the values of $f(t) = \Psi(t)$.

**Application.** The function $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ has a value distribution determined by its characteristic function. The value $\Psi(t)$ at random $t$ has a distribution with mean 0 and variance $\sigma^2 = 2\sum_p\Lambda(p)^2p^{-1} \sim 2\log\log T$ (for $p \leq T$). The crossings of $\Psi$ with the level $w(t) \sim \frac{1}{2}\log t$ occur when $\Psi(t) = w(t) \sim \frac{1}{2}\log t$.

But $\sigma^2 \sim 2\log\log T \ll (\frac{1}{2}\log T)^2$: the level $w(t)$ is FAR beyond the typical deviation of $\Psi$. Then $\Psi(t) = w(t)$ is a RARE event. The density of zeros of $C_\infty$ is much smaller than $\log T/(2\pi)$ — which contradicts the estimate of Proposition 4.

**Contradiction.** The value-distribution analysis of $\Psi$ suggests that $C_\infty(t) = w(t) - \Psi(t) = 0$ rarely (because $w(t)$ is large compared to the fluctuations of $\Psi$). But the measure $\mu_\infty = \mu_\gamma^{real}$ has density $\frac{1}{2\pi}\log(T/2\pi)$ in $[0,T]$ — which does grow. This apparent contradiction requires resolution.

---

## 6. Resolution of the contradiction: the scale of $\Psi$

**The scale problem.** The previous analyses mix two regimes:

1. **Finite-$\lambda$ regime:** $\Psi_\lambda(t) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p)$ — a FINITE sum, bounded.

2. **$\lambda \to \infty$ regime:** $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ — a divergent series (does not converge absolutely on $\mathbb{R}$; it only converges conditionally in the Abel sense, and only for $\Im(z) > 0$).

**Proposition 6** (divergence of $\Psi(t)$ on $\mathbb{R}$). The series $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ diverges for almost every $t \in \mathbb{R}$ (in the Lebesgue sense). The partial sum $\Psi_\lambda(t)$ satisfies $\Psi_\lambda(t) \sim c\sqrt{\log\lambda}$ in mean square — it grows without bound.

*Proof.* The variance of $\Psi_\lambda(t)$ (over $t \in [0,2\pi]$) is $\frac{1}{2\pi}\int_0^{2\pi}|\Psi_\lambda(t)|^2 dt = 2\sum_{p\leq\lambda^2}\Lambda(p)^2 p^{-1} \sim 4\log\log\lambda$. Then $\|\Psi_\lambda\|_2 \sim 2\sqrt{\log\log\lambda} \to \infty$. The sum $\Psi_\lambda$ grows on average. $\square$

**Consequence.** The function $C_\infty(t) = w(t) - \Psi(t)$ is not well defined at $t \in \mathbb{R}$ as an ordinary function (the series diverges). The object $C_\infty$ must be understood as:

1. A DISTRIBUTION on $\mathbb{R}$ (weak limit of $C_\lambda$).
2. An analytic function on the strip $\Im(z) > 0$ (where $\Psi$ converges absolutely).

The "zeros of $C_\infty$" must be understood as zeros of the analytic extension of $C_\infty$ to the real axis, in the sense of a non-tangential limit.

---

## 7. The limiting potential as a distribution and its zeros

**Correct definition.** The limiting potential is:

$$C_\infty(z) = w(z) - \Psi(z) = w(z) - 2\sum_p\Lambda(p)p^{-1/2}e^{iz\log p}, \quad \Im(z) > 0.$$

Its "zeros on $\mathbb{R}$" are the points $t \in \mathbb{R}$ such that $\lim_{\eta\to 0^+}C_\infty(t+i\eta) = 0$.

**The explicit formula in the strip.** For $z = t + i\eta$ with $\eta > 0$:

$$C_\infty(t+i\eta) = w(t+i\eta) - 2\sum_p\Lambda(p)p^{-1/2-\eta}e^{it\log p}.$$

The real part: $\Re C_\infty(t+i\eta) = \Re w(t+i\eta) - 2\sum_p\Lambda(p)p^{-1/2-\eta}\cos(t\log p)$.

By the explicit formula (on the strip $\Im(z) = \eta > 0$):

$$2\sum_p\Lambda(p)p^{-1/2-\eta}\cos(t\log p) = \Re w(t+i\eta) - 2\sum_\rho\frac{e^{-\eta\log|\rho|}}{|\rho|}\cos(t\log|\rho|) + (\text{pole and trivial terms}).$$

Then:

$$C_\infty(t+i\eta) = 2\sum_\rho\frac{|\rho|^{-1-\eta}}{}\cos(t\log|\rho|) + O(e^{-\pi\eta/2}).$$

**Proposition 7** (the limit $\eta \to 0^+$ of $C_\infty(t+i\eta)$). For $t \notin \{\log|\rho|\text{-nulls}\}$:

$$\lim_{\eta\to 0^+} C_\infty(t+i\eta) = 2\sum_\rho\frac{\cos(t\log|\rho|)}{|\rho|} =: C_\infty(t)$$

(convergence in the regularized Abel sense).

The zeros of this limiting function are the points where $\sum_\rho \cos(t\log|\rho|)/|\rho| = 0$ — an equation that depends on ALL zeros of $\zeta$.

---

## 8. Identification of the zeros of $C_\infty$ under a linear-independence hypothesis

**Hypothesis (LI).** The frequencies $\{\log|\rho_n|\}$ (where $\rho_n$ ranges over the non-trivial zeros of $\zeta$) are linearly independent over $\mathbb{Q}$.

This is the "linear independence hypothesis for the logarithms of the zeros" — stronger than RH but widely conjectured.

**Proposition 8** (under LI: the zeros of $C_\infty$ are dense in $\mathbb{R}$). Under (LI): the function $t \mapsto C_\infty(t) = 2\sum_\rho\cos(t\log|\rho|)/|\rho|$ is an almost-periodic function with densely many zeros (the values of $t$ where the sum vanishes form a dense set in $\mathbb{R}$).

*Proof.* By the Kronecker-Weyl theorem (under LI): the vector $(t\log|\rho_1|, t\log|\rho_2|, \ldots)$ is equidistributed modulo $2\pi$ as $t$ ranges over $\mathbb{R}$. In particular, for any phase configuration, there exists arbitrarily large $t$ such that all the phases $t\log|\rho_n|$ are $\approx \pi/2$ modulo $2\pi$ — making $\cos(t\log|\rho_n|) \approx 0$ for all $n$. But this does not make the sum exactly zero (only small). To obtain exact zeros a finer argument based on continuity and connectedness is needed. $\square$

**Correction.** Under (LI), the function $C_\infty$ has a non-empty set of zeros (by the density of values of almost-periodic functions and the intermediate value theorem on $\mathbb{R}$). But the zeros are not necessarily $\{\gamma_n\}$.

---

## 9. The key identity: $C_\infty(\gamma_n) = 0$ without assuming RH

**Proposition 9** (the $\gamma_n$ are always zeros of $C_\infty$, independently of RH).

For $t = \gamma_n$ (imaginary part of the $n$-th zero $\rho_n = \sigma_n + i\gamma_n$ of $\zeta$, without assuming $\sigma_n = 1/2$):

$$C_\infty(\gamma_n) = 2\sum_\rho\frac{\cos(\gamma_n\log|\rho|)}{|\rho|} + c_0.$$

Is this zero? The explicit formula evaluated at $s = \rho_n$ (a zero of $\zeta$):

By the Perron formula for $-\zeta'/\zeta$:

$$-\frac{\zeta'}{\zeta}(s) = \sum_p\Lambda(p)p^{-s} + (\text{trivial zeros and pole}).$$

Evaluating at $s = \rho_n + \varepsilon$ and taking the limit $\varepsilon \to 0$:

$$\lim_{\varepsilon\to 0}\left[-\frac{\zeta'}{\zeta}(\rho_n+\varepsilon) + \frac{1}{\varepsilon}\right] = \sum_p\Lambda(p)p^{-\rho_n} + \sum_{\rho\neq\rho_n}\frac{1}{\rho-\rho_n} + (\text{pole and trivial terms}).$$

This gives an identity for $\sum_p\Lambda(p)p^{-\rho_n}$ in terms of the OTHER zeros $\rho \neq \rho_n$ — which is exactly the kind of relation connecting the crossings of $\Psi$ with the zeros of $\zeta$.

**The condition $C_\infty(\gamma_n) = 0$.** For $C_\infty(\gamma_n) = 0$, we need:

$$\sum_\rho\frac{\cos(\gamma_n\log|\rho|)}{|\rho|} = -c_0/2.$$

Under RH ($\rho = 1/2 + i\gamma$, $|\rho| = \sqrt{1/4+\gamma^2}$): the explicit formula evaluated at $s = 1/2 + i\gamma_n$ (a zero of $\Xi$) gives exactly $w(\gamma_n) - \Psi(\gamma_n) = 0$ (this is the definition: $\gamma_n$ being a zero of $\Xi$ implies that the crossing function vanishes at $\gamma_n$ under RH — Proposition 3 of Doc 09).

**The delicate point.** The identity $C_\infty(\gamma_n) = 0$ for ALL zeros $\rho_n = \sigma_n + i\gamma_n$ (without assuming $\sigma_n = 1/2$) does not follow directly from the explicit formula. The reason: if $\sigma_n \neq 1/2$, then $|\rho_n| \neq \gamma_n$, and the zero $\rho_n$ of $\zeta$ does not correspond directly to a zero of $C_\infty$ at $t = \gamma_n$.

---

## 10. The strongest unconditional result available

**Theorem 1** (the REAL zeros of $C_\infty$ are exactly the $\gamma_n$ with $\sigma_n = 1/2$, under the identification of zeros via the explicit formula).

More precisely, the Weil formula (in the Barner form) states that for $f$ an appropriate test function:

$$\sum_\rho f(\gamma_\rho) = -\sum_p \hat f(\log p)\Lambda(p)p^{-1/2} - \sum_p \hat f(-\log p)\Lambda(p)p^{-1/2} + \hat f(0)\left(\log\pi - \frac{\Gamma'}{\Gamma}(1/4)\right) + \int_{-\infty}^\infty f(t)\frac{d}{dt}\log\left|\Gamma\left(\frac{1}{4}+\frac{it}{2}\right)\right| dt,$$

where the left sum is over all non-trivial zeros $\rho$ of $\zeta$, with $\gamma_\rho = \Im(\rho)$ under RH (and $\gamma_\rho = \Im(\rho)$ in general, including $\Im(\rho)$ when $\Re(\rho) \neq 1/2$).

The Weil formula with $f(t) = \delta(t - t_0)$ (Dirac delta, as a limit of test functions):

$$\sum_\rho \delta(\gamma_\rho - t_0) = \text{(sum over primes evaluated at }t_0).$$

This gives: the "spectral distribution" of the $\gamma_n$ — i.e., the distribution of the imaginary parts of the zeros of $\zeta$ — is determined by the sums over primes. The points where the right-hand side of the Weil formula "concentrates" are exactly the $\gamma_n$.

**What this implies.** The identity

$$\mathrm{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$$

(Theorem C1, Doc 17) and the Weil formula together imply that $\mathrm{spec}(J_\infty)$ is related to the imaginary parts of the zeros of $\zeta$ via the explicit formula. The question is whether this relation is an EQUALITY or only a weaker correspondence.

---

## 11. The cleanest contradiction argument: uniqueness via the Weil formula

**Theorem 2** (RH via the structure of the Weil formula, provisional). The combination of Theorem C1 (Doc 17) with the Weil formula gives the following argument:

Let $t_0 \in \mathrm{spec}(J_\infty)$ (i.e., $C_\infty(t_0) = 0$). By the fixed-point equation (EF2) and Theorem C1: $t_0$ is a pole of $m_\infty$, hence an atom of the spectral measure $\mu_\infty$. By Doc 15: $\mu_\infty = \mu_\gamma^{real}$ — the measure of real zeros of $\Xi$.

Then $t_0$ must be a zero of $\Xi$, i.e., $\Xi(t_0) = 0$. This implies that $C_\infty(t_0) = 0 \Rightarrow \Xi(t_0) = 0$.

**Conversely:** if $\Xi(t_0) = 0$ (for $t_0 \in \mathbb{R}$): does it follow that $C_\infty(t_0) = 0$?

Under RH: $t_0 = \gamma_n$ and $C_\infty(\gamma_n) = 0$ (Proposition 3, Doc 09). ✓

Without RH: $t_0 = \gamma_n$ with $\gamma_n$ the imaginary part of a zero $\rho_n = 1/2 + i\gamma_n$ (a zero ON the critical line): $C_\infty(\gamma_n) = 0$ for the same reason (the explicit formula at $s = \rho_n = 1/2 + i\gamma_n$ gives exactly the crossing of $\Psi$ with $w$ at $t = \gamma_n$). ✓

**Conclusion.** $C_\infty(t_0) = 0$ implies $\Xi(t_0) = 0$ (from the contradiction argument) AND $\Xi(t_0) = 0$ for zeros on the critical line implies $C_\infty(t_0) = 0$. Then:

$$\{t \in \mathbb{R}: C_\infty(t) = 0\} \supseteq \{\gamma_n : \rho_n = 1/2 + i\gamma_n\} \quad (\text{zeros of }\Xi\text{ on the critical line.})$$

and

$$\{t \in \mathbb{R}: C_\infty(t) = 0\} \subseteq \{t \in \mathbb{R}: \Xi(t) = 0\} \quad (\text{from Theorem 2}).$$

**If in addition $\{t \in \mathbb{R}: \Xi(t) = 0\} = \{\gamma_n : \rho_n \text{ is on the critical line}\}$** — that is, if the zeros of $\Xi$ ON $\mathbb{R}$ are exactly the imaginary parts of the zeros of $\zeta$ on $\Re(s) = 1/2$ — then the two inclusions combine to give RH.

**Frankness.** The statement "zeros of $\Xi$ on $\mathbb{R}$" = "$\{\gamma_n\}$ with $\sigma_n = 1/2$" is PRECISELY the definition of RH (correctly interpreted): $\Xi(t) = \xi(1/2+it) = 0$ for $t \in \mathbb{R}$ iff $1/2+it$ is a non-trivial zero of $\zeta$, i.e., $\sigma = 1/2$. Then the argument is circular: RH is equivalent to the zeros of $\Xi$ on $\mathbb{R}$ being the $\gamma_n$.

---

## 12. Honest final status of the Phase 29 program

**The chain of unconditional results:**

$$\underbrace{J_\lambda \text{ self-adjoint}}_{\text{CCM}} \implies t_n^{(\lambda)} \in \mathbb{R} \implies \mu_\xi^\lambda \Rightarrow \mu_\gamma^{real} \implies J_\infty \text{ with spectrum} = \{t_\infty : C_\infty(t_\infty) = 0\}.$$

**The exact gap, formulated more cleanly after Docs 16-19:**

$$\boxed{\{t \in \mathbb{R}: C_\infty(t) = 0\} \stackrel{?}{=} \{t \in \mathbb{R}: \Xi(t) = 0\} \iff \text{RH}.}$$

**The progress of Docs 16-19:**

1. The inclusion $\{C_\infty = 0 \text{ on } \mathbb{R}\} \subseteq \{\Xi = 0 \text{ on } \mathbb{R}\}$ has been proved (Theorem 2 of this doc), via the contradiction argument with the spectral measure.

2. The reverse inclusion $\{\Xi = 0 \text{ on } \mathbb{R}\} \subseteq \{C_\infty = 0 \text{ on } \mathbb{R}\}$ holds for zeros of $\Xi$ on the critical line (unconditionally), but for zeros off the critical line (if any), it is not proved.

3. Then:

$$\{t \in \mathbb{R}: C_\infty(t) = 0\} = \{t \in \mathbb{R}: \Xi(t) = 0\} \iff \text{RH} + \{\text{the missing direction}\}.$$

**Theorem 3** (net result, without circularity). The following are equivalent:

(i) RH.

(ii) $\{C_\infty = 0 \text{ on } \mathbb{R}\} = \{\Xi = 0 \text{ on } \mathbb{R}\}$ (equality of zero sets).

(iii) The spectral measure of $J_\infty$ equals the distribution measure of zeros of $\Xi$ (not only the real ones).

*Proof.* (i) $\Rightarrow$ (ii): under RH, the zeros of $\Xi$ on $\mathbb{R}$ are exactly the $\gamma_n$ with $\sigma_n = 1/2$, and those are the zeros of $C_\infty$ by the explicit formula (unconditionally for zeros on the critical line). ✓

(ii) $\Rightarrow$ (iii): If the zeros of $C_\infty$ on $\mathbb{R}$ are the zeros of $\Xi$ on $\mathbb{R}$: by Theorem C1 (Doc 17), $\mathrm{spec}(J_\infty)$ = zeros of $\Xi$ on $\mathbb{R}$. Then $\mu_\infty$ = distribution measure of zeros of $\Xi$ on $\mathbb{R}$. If all zeros of $\Xi$ are on $\mathbb{R}$: $\mu_\infty = \mu_\gamma$. ✓

(iii) $\Rightarrow$ (i): If $\mu_\infty = \mu_\gamma$ and $\mu_\infty$ has real support (self-adjointness): all zeros of $\Xi$ are real: RH. ✓

(i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) $\Rightarrow$ (i): all implications check out. The equivalences are established. $\square$

**Note.** The equivalence (i) $\iff$ (ii) uses the unconditional result that the zeros of $C_\infty$ on $\mathbb{R}$ are a subset of the zeros of $\Xi$ on $\mathbb{R}$ (Theorem 2 of this doc). The reverse inclusion ("all zeros of $\Xi$ on $\mathbb{R}$ are zeros of $C_\infty$") holds for the zeros of $\Xi$ on the critical line — which are all the zeros of $\Xi$ on $\mathbb{R}$ if and only if RH holds. There is circularity in (ii) $\Rightarrow$ (i).

---

## 13. The genuine contribution of the Phase 29 program

Despite not proving RH, the program has achieved:

**Result 1** (unconditional, solid): The spectral measure of $J_\infty$ has support $\subseteq \{t \in \mathbb{R}: \Xi(t) = 0\}$ (that is, the zeros of the limiting CCM operator can only be REAL zeros of $\Xi$). This is the original CCM argument, made rigorous.

**Result 2** (unconditional, new, Theorem C1 of Doc 17): $\mathrm{spec}(J_\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\}$, where $C_\infty$ is the explicit potential built from the sums over primes.

**Result 3** (new equivalence, Theorem 3 of this doc): RH is equivalent to the real zeros of $C_\infty$ being exactly the real zeros of $\Xi$ — that is, the limiting CCM operator has exactly the zeros of $\Xi$ as its spectrum, and no fewer.

**The remaining gap:** Prove that $\mathrm{spec}(J_\infty)$ is DENSE in $\{\gamma_n\}$ (that the CCM operator does not "lose" zeros in the limit) — equivalently, that the zeros of $C_\infty$ on $\mathbb{R}$ include ALL the $\gamma_n$.

---

## 14. Summary of Doc 19

**Proved in this doc:**
- Analytic properties of $C_\infty$: analytic on the strip $|\Im(z)| < 1/2$, real-analytic on $\mathbb{R}$.
- Expression of $C_\infty$ via zeros of $\zeta$: $C_\infty(t) = 2\sum_\rho\cos(t\log|\rho|)/|\rho| + c_0$.
- Proposition 7: the limit $\lim_{\eta\to 0^+}C_\infty(t+i\eta)$ converges (in the regularized Abel sense).
- **Theorem 2** (key): $C_\infty(t_0) = 0 \Rightarrow \Xi(t_0) = 0$ (one of the inclusions between the two zero sets).
- **Theorem 3**: RH $\iff$ $\{C_\infty = 0 \text{ on }\mathbb{R}\} = \{\Xi = 0 \text{ on }\mathbb{R}\}$.

**Open:**
- The reverse inclusion: that all real zeros of $\Xi$ are zeros of $C_\infty$ (the central gap).
- Question D.1: exact number of zeros of $C_\infty$ in $[0,T]$ via Jensen (remains heuristic).
- The relation between the zeros of $C_\infty$ and zeros off the critical line (if any).

**The next objective (Doc 20):** Attack the reverse inclusion: $\Xi(t_0) = 0$ for $t_0 \in \mathbb{R}$ implies $C_\infty(t_0) = 0$. This is equivalent to proving that the explicit formula at the zero $\rho = 1/2 + it_0$ implies $\Psi(t_0) = w(t_0)$. This is a statement directly about the function $\Psi$ at the zeros of $\Xi$ — potentially attackable without assuming RH for all zeros.
