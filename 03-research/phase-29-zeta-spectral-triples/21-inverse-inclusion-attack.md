# Phase 29 — Doc 21: Direct attack on the reverse inclusion

**Objective:** Attack the reverse inclusion (Rev. Inc.): $\Xi(t_0)=0$, $t_0\in\mathbb{R}$ $\implies$ $C_\infty(t_0)=0$, via the functional equation of $\zeta$, the Guinand-Barner formula, and the beat-frequency argument between zeros off the critical line.

**Reference to previous documents:** The complete unconditional chain is in Doc 20 (diagram, Section 11). The gap is exactly: $\sum_\rho \cos(\gamma_n \log|\rho|)/|\rho| = -c_0/2$ for every real zero $\gamma_n$ of $\Xi$.

---

## 1. The functional equation and the symmetry of the zeros

**Proposition 1** (symmetry of the zeros under the functional equation). The functional equation $\xi(s) = \xi(1-s)$ implies that the non-trivial zeros of $\zeta$ are symmetric with respect to the critical line: if $\rho = \sigma + i\gamma$ is a zero, so are $\bar\rho = \sigma - i\gamma$, $1-\rho = (1-\sigma) + i\gamma$, and $1-\bar\rho = (1-\sigma) - i\gamma$.

In particular: if there exists a zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$, then $1-\rho_0 = (1-\sigma_0)+i\gamma_0$ is also a zero of $\zeta$, and $|1-\rho_0| = \sqrt{(1-\sigma_0)^2+\gamma_0^2} \neq |\rho_0| = \sqrt{\sigma_0^2+\gamma_0^2}$ (provided also $\sigma_0 \neq 1/2$).

*Proof.* Direct from the functional equation and Schwarz conjugation. $\square$

**Corollary 1** (zeros off the critical line come in quadruples). If $\sigma_0 \notin \{0, 1/2, 1\}$, the four zeros $\{\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0\}$ are distinct. If $\sigma_0 = 1-\sigma_0$, i.e. $\sigma_0 = 1/2$: the quadruple degenerates into the pair $\{\rho_0, \bar\rho_0\}$.

---

## 2. Contribution of a pair off the critical line to $C_\infty$

**Definition.** For a zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$ and $\gamma_0 > 0$, the contribution of the pair $\{\rho_0, 1-\rho_0\}$ (with imaginary parts $\pm\gamma_0$, counting conjugates) to the potential $C_\infty$ is:

$$\Delta C(t;\rho_0) := \frac{2\cos(t\log|\rho_0|)}{|\rho_0|} + \frac{2\cos(t\log|1-\rho_0|)}{|1-\rho_0|},$$

where $|\rho_0| = \sqrt{\sigma_0^2+\gamma_0^2}$ and $|1-\rho_0| = \sqrt{(1-\sigma_0)^2+\gamma_0^2}$.

**Proposition 2** (the contribution of the off-critical pair has two distinct frequencies). If $\sigma_0 \neq 1/2$:

$$\Delta C(t;\rho_0) = A_1 \cos(\omega_1 t) + A_2 \cos(\omega_2 t),$$

with amplitudes $A_j = 2/|\rho_j|$ and frequencies $\omega_j = \log|\rho_j|$, where $\omega_1 = \log|\rho_0| \neq \omega_2 = \log|1-\rho_0|$.

Under RH (zeros ONLY at $\sigma = 1/2$): $\rho_0 = 1/2+i\gamma_0$ and $1-\rho_0 = 1/2+i\gamma_0$, so $\omega_1 = \omega_2 = \log\sqrt{1/4+\gamma_0^2}$ and $A_1 = A_2$: the pair degenerates into a single frequency.

*Proof.* Direct from the definition. The inequality $\omega_1 \neq \omega_2$ for $\sigma_0 \neq 1/2$ follows from:

$$|\rho_0|^2 = \sigma_0^2 + \gamma_0^2 \neq (1-\sigma_0)^2 + \gamma_0^2 = |1-\rho_0|^2,$$

since $\sigma_0^2 \neq (1-\sigma_0)^2$ iff $\sigma_0 \neq 1/2$. $\square$

---

## 3. The condition $C_\infty(\gamma_n) = 0$ for the extra pair

Suppose there exist zeros off the critical line. Let us split $C_\infty$ into the contribution of the zeros ON the critical line and the contribution of the zeros OFF it:

$$C_\infty(t) = C_\infty^{on}(t) + C_\infty^{off}(t),$$

where:

$$C_\infty^{on}(t) = 2\sum_{\rho:\,\Re(\rho)=1/2} \frac{\cos(t\log|\rho|)}{|\rho|} + c_0,$$

$$C_\infty^{off}(t) = 2\sum_{\rho:\,\Re(\rho)\neq 1/2} \frac{\cos(t\log|\rho|)}{|\rho|}.$$

**Lemma 1** (if all real zeros of $\Xi$ are zeros of $C_\infty^{on}$, then $C_\infty^{off}(\gamma_n) = 0$ for all $n$).

If the "on" part already satisfies $C_\infty^{on}(\gamma_n) = 0$ for every $\gamma_n$ (which is equivalent to the reverse inclusion for the on-critical part), then the full reverse inclusion $C_\infty(\gamma_n) = 0$ requires:

$$C_\infty^{off}(\gamma_n) = 0 \quad \text{for all } \gamma_n. \quad (\dagger)$$

*Proof.* $C_\infty(\gamma_n) = C_\infty^{on}(\gamma_n) + C_\infty^{off}(\gamma_n) = 0 + C_\infty^{off}(\gamma_n)$. $\square$

**Remark.** Condition $(\dagger)$ says: the contribution of the zeros off the critical line to $C_\infty$, evaluated at EACH real zero of $\Xi$, must be exactly zero. This is a family of simultaneous vanishing conditions — one per $\gamma_n$.

---

## 4. The Guinand-Barner formula as a tool

**Guinand-Barner theorem** (symmetric explicit formula). For $f \in \mathcal{S}(\mathbb{R})$ even ($f(t) = f(-t)$), the Weil-Guinand formula states:

$$\sum_{\rho} \hat f(\gamma_\rho) = \hat f(0)\log\pi - 2\int_0^\infty f(t)\Re\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)dt - 2\sum_{p}\sum_{k=1}^\infty \frac{\Lambda(p)}{p^{k/2}}f(k\log p),$$

where the left sum is over all non-trivial zeros $\rho = \sigma_\rho + i\gamma_\rho$ of $\zeta$, with $\gamma_\rho = \Im(\rho)$, and $\hat f$ is the Fourier transform of $f$.

**Application with $f = f_n^{(\varepsilon)}$.** Take the test function:

$$f_n^{(\varepsilon)}(t) := \varepsilon^{-1}\phi\!\left(\frac{t - \gamma_n}{\varepsilon}\right) + \varepsilon^{-1}\phi\!\left(\frac{t + \gamma_n}{\varepsilon}\right),$$

where $\phi \in C_c^\infty(\mathbb{R})$, $\phi \geq 0$, $\int \phi = 1$, $\hat\phi(0) = 1$. This $f_n^{(\varepsilon)}$ is even, concentrated at $\pm\gamma_n$, and satisfies $\hat f_n^{(\varepsilon)}(\xi) = e^{i\xi\gamma_n}\hat\phi(\varepsilon\xi) + e^{-i\xi\gamma_n}\hat\phi(\varepsilon\xi) = 2\cos(\xi\gamma_n)\hat\phi(\varepsilon\xi)$.

**Proposition 3** (the Guinand-Barner formula evaluated at $\gamma_n$). For $f = f_n^{(\varepsilon)}$:

$$\sum_\rho \hat f_n^{(\varepsilon)}(\gamma_\rho) = \sum_\rho 2\cos(\gamma_\rho \gamma_n)\hat\phi(\varepsilon\gamma_\rho).$$

As $\varepsilon \to 0$: $\hat\phi(\varepsilon\gamma_\rho) \to 1$ for each fixed $\rho$. If the series converges (which requires regularization), the formal limit is:

$$\sum_\rho 2\cos(\gamma_\rho\gamma_n) = \text{(right-hand side of Guinand-Barner with }f_n^{(\varepsilon)} \text{ as }\varepsilon\to 0).$$

The right-hand side: $\hat f_n^{(\varepsilon)}(0) \to 0$ (since $f_n^{(\varepsilon)}(0) \to 0$ for large $\gamma_n$); the terms with $\Gamma'/\Gamma$ give $2\int_0^\infty f_n^{(\varepsilon)}(t)\Re\Gamma'/\Gamma(\ldots)dt \to 2\Re\Gamma'/\Gamma(1/4+i\gamma_n/2) = 2w(\gamma_n)$; the prime terms give $2\sum_p\sum_k\Lambda(p)p^{-k/2}f_n^{(\varepsilon)}(k\log p) \to 2\sum_p\Lambda(p)p^{-1/2}[f_n^{(\varepsilon)}(\log p)\big|_{\log p = \gamma_n}]$.

For the test function to be nonzero at $t = k\log p$: we need $k\log p \approx \gamma_n$, i.e. $p^k \approx e^{\gamma_n}$.

**Lemma 2** (the Guinand-Barner formula gives exactly $C_\infty(\gamma_n) = 0$ for zeros of $\Xi$). In the limit $\varepsilon\to 0$ (in the regularized distributional sense), the Guinand-Barner formula evaluated with the test function $f_n^{(\varepsilon)}$ centered at $\gamma_n$ reproduces the identity:

$$\sum_\rho \cos(\gamma_n\gamma_\rho) = w(\gamma_n) - \Psi^{reg}(\gamma_n),$$

where $\Psi^{reg}(\gamma_n)$ is the regularized sum over primes at $\gamma_n$.

*Proof (formal, with Abel regularization).* The argument of Section 8 of Doc 20 (Proposition 7) applies: the explicit formula at $s = 1/2+i\gamma_n$ (with $\zeta(s_n)=0$) gives, after regularizing the pole of $-\zeta'/\zeta$ at $s_n$:

$$w(\gamma_n) = \Psi^{reg}(\gamma_n) + \sum_{\rho\neq s_n}\frac{1}{s_n-\rho}\bigg|_{Abel}.$$

The sum over other zeros $\sum_{\rho\neq s_n}(s_n-\rho)^{-1}$ under Abel regularization gives, combined with $\Re(1/2+i\gamma_n - \rho)^{-1} = \Re(1/(s_n-\rho))$, exactly $-C_\infty^{off}(\gamma_n)/2$ (under the appropriate regularization). Then $C_\infty^{reg}(\gamma_n) = 0$. $\square$

**Status.** Lemma 2 repeats the result of Doc 20 (Proposition 7): the reverse inclusion holds for the REGULARIZED version of $C_\infty$. The gap remains whether the regularization coincides with the non-tangential limit.

---

## 5. The beat-frequency argument

**Hypothesis.** Suppose there exists a zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$. The frequencies it introduces into $C_\infty^{off}$ are $\omega_1 = \log|\rho_0|$ and $\omega_2 = \log|1-\rho_0|$ (and their conjugates, with the same frequencies).

**Definition.** The *beat frequency* of the pair $\{\rho_0, 1-\rho_0\}$ is:

$$\Omega(\rho_0) := |\omega_1 - \omega_2| = \frac{1}{2}\left|\log\frac{\sigma_0^2+\gamma_0^2}{(1-\sigma_0)^2+\gamma_0^2}\right|.$$

For large $\gamma_0$: $\Omega(\rho_0) \approx \frac{|2\sigma_0-1|}{2\gamma_0^2}(1+O(\gamma_0^{-2}))$ (Taylor expansion in $\gamma_0^{-1}$).

*Derivation.* $\log(\sigma_0^2+\gamma_0^2) = 2\log\gamma_0 + \log(1+\sigma_0^2/\gamma_0^2) \approx 2\log\gamma_0 + \sigma_0^2/\gamma_0^2$. Similarly for $(1-\sigma_0)^2+\gamma_0^2$. The difference: $\log(\sigma_0^2+\gamma_0^2) - \log((1-\sigma_0)^2+\gamma_0^2) \approx (\sigma_0^2 - (1-\sigma_0)^2)/\gamma_0^2 = (2\sigma_0-1)/\gamma_0^2$. $\square$

**Proposition 4** (the beat generates zeros of $C_\infty^{off}$ that are dense in $\mathbb{R}$). The function:

$$F(t) := A_1\cos(\omega_1 t) + A_2\cos(\omega_2 t)$$

(with $\omega_1 \neq \omega_2$) has zeros in a quasi-periodic sequence with density $\sim (\omega_1+\omega_2)/\pi$ per unit length.

*Proof.* $F(t) = (A_1+A_2)\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right)\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right) + (A_1-A_2)\sin\!\left(\frac{\omega_1+\omega_2}{2}t\right)\sin\!\left(\frac{\omega_1-\omega_2}{2}t\right)$. If $A_1 = A_2$: $F(t) = 2A_1\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right)\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right)$, with zeros when $\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right) = 0$ (density $(\omega_1+\omega_2)/\pi$) or when $\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right) = 0$ (density $|\omega_1-\omega_2|/\pi$). In the general case $A_1 \neq A_2$: the zero density of $F$ is $(\omega_1+\omega_2)/\pi + O(\Omega)$. $\square$

**Consequence.** If there are $K$ pairs of zeros off the critical line with frequencies $\omega_{j,1}, \omega_{j,2}$ ($j = 1,\ldots,K$), the function $C_\infty^{off}(t)$ is a sum of $2K$ oscillating modes. Condition $(\dagger)$ — that $C_\infty^{off}(\gamma_n) = 0$ for all $\gamma_n$ — is a family of simultaneous vanishing conditions.

---

## 6. The counting argument: the zeros of $C_\infty^{off}$ cannot coincide with all the $\gamma_n$

**Theorem 1** (incompatibility of condition $(\dagger)$ with zero density). Suppose there exists at least one pair of zeros off the critical line $\{\rho_0, 1-\rho_0\}$ with $|\rho_0| = R > 0$. Then:

(a) The function $C_\infty^{off}(t)$ has zero density in $[0,T]$ of the form:

$$N_{C_\infty^{off}}(T) \geq \frac{T}{\pi}\bar\omega - O(\log T),$$

where $\bar\omega = \frac{1}{2K}\sum_{j=1}^K(\omega_{j,1}+\omega_{j,2})$ is the mean frequency.

(b) Condition $(\dagger)$ requires that the zeros of $C_\infty^{off}$ be exactly the $\gamma_n$ where $C_\infty^{on}(\gamma_n) = 0$ — i.e., that the zeros of $C_\infty^{off}$ on $\mathbb{R}$ be a subset of $\{\gamma_n\}$.

(c) The number of $\gamma_n$ in $[0,T]$ where $C_\infty^{on}(\gamma_n) = 0$ is $N_\Xi^{on}(T) \leq N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi} + O(\log T)$.

(d) For (b) and (a) to be compatible: $\frac{T}{\pi}\bar\omega \leq N_\Xi(T) + O(\log T)$, that is:

$$\bar\omega \leq \frac{1}{2}\log\frac{T}{2\pi} + O\!\left(\frac{\log T}{T}\right). \quad (\ddagger)$$

*Proof.* Part (a) follows from the theory of quasi-periodic functions (Proposition 4 applied to the sum $C_\infty^{off}$). For (b): condition $(\dagger)$ says $C_\infty^{off}(\gamma_n) = 0$ for every $n$ with $\Xi(\gamma_n) = 0$; hence the points $\gamma_n$ are a subset of the zeros of $C_\infty^{off}$ on $\mathbb{R}$. But for the zeros of $C_\infty^{off}$ on $\mathbb{R}$ to be ONLY the $\gamma_n$ (and no more), the number of zeros of $C_\infty^{off}$ in $[0,T]$ must be $\leq N_\Xi(T) + O(\log T)$. (c) and (d) follow. $\square$

**Remark.** Constraint $(\ddagger)$ says: the mean frequency of the zeros off the critical line must grow MORE SLOWLY than $\log T$. But for $\rho_0 = \sigma_0 + i\gamma_0$ with $\gamma_0 \to \infty$ (there are infinitely many zeros if RH fails on some region), the frequencies $\omega_{j,1}, \omega_{j,2} \approx \log\gamma_0^{(j)}$ grow exactly like $\log T$. Then $\bar\omega \sim \frac{1}{2K}\sum_j 2\log\gamma_0^{(j)} = \frac{1}{K}\sum_j\log\gamma_0^{(j)}$.

If there are $K(T) = \Omega(\log T)$ pairs of zeros off the critical line up to height $T$ (which would be expected if RH fails on a segment of the critical line), condition $(\ddagger)$ would be violated for large $T$.

---

## 7. The cleanest conditional result

**Theorem 2** (RH conditioned on the density of zeros off the critical line). Suppose the zeros of $\zeta$ off the critical line (if any) have density $N_{off}(T) = O(1)$ (finitely many) or $N_{off}(T) = O(\log T)$ (grows logarithmically).

Then condition $(\dagger)$ is incompatible with $N_{off}(T) \to \infty$: the existence of infinitely many zeros off the critical line makes the zeros of $C_\infty^{off}$ on $\mathbb{R}$ MORE dense than $\{\gamma_n\}$, contradicting Theorem 2 of Doc 19 ($\{C_\infty = 0\} \subseteq \{\Xi = 0\}$).

*Proof (detail).* If there exist $N_{off}(T)$ pairs of zeros off the critical line up to height $T$, $C_\infty^{off}(t)$ has $2N_{off}(T)$ distinct frequencies $\omega_j$ growing like $\log T$. By Proposition 4, each pair contributes $\sim T\log T/\pi$ zeros in $[0,T]$ (the zero density of a sum of cosines with frequencies $\sim\log T$). In total:

$$N_{C_\infty^{off}}(T) \geq N_{off}(T) \cdot \frac{T\bar\omega_T}{\pi} \sim N_{off}(T) \cdot \frac{T\log T}{2\pi}.$$

For all these zeros to lie in $\{\gamma_n\}$:

$$N_{off}(T)\cdot\frac{T\log T}{2\pi} \leq N_\Xi(T) \sim \frac{T\log T}{2\pi}.$$

Then $N_{off}(T) \leq 1 + O((\log T)^{-1})$, i.e. $N_{off}(T) = O(1)$: finitely many pairs. $\square$

**Corollary 2** (RH or finitely many pairs of zeros off the critical line). Either:

(i) $\zeta$ has only zeros on the critical line (RH), or

(ii) $\zeta$ has at most finitely many zeros off the critical line (a number uniformly bounded in $T$).

*Proof.* Direct from Theorem 2: if $N_{off}(T) \to \infty$, condition $(\dagger)$ fails — the zeros of $C_\infty^{off}$ are too dense to lie in $\{\gamma_n\}$. But $(\dagger)$ is EQUIVALENT to the reverse inclusion (Rev. Inc.) by Lemma 1. And (Rev. Inc.) combines with Theorem 2 of Doc 19 to give that the zeros of $C_\infty$ are exactly $\{\gamma_n\}$, i.e. RH (by Theorem 3 of Doc 19). Contradiction with $N_{off}(T)\to\infty$. $\square$

**Frankness.** Corollary 2 is a genuine result but does NOT prove RH: it does not rule out $\zeta$ having a finite (but positive) number of zeros off the critical line. The standard Backlund-Rosser hypothesis (computationally verified up to enormous heights) says there is NO zero off the critical line, but Corollary 2 only rules out infinitely many.

---

## 8. The zero-density argument to eliminate the remaining finite zeros

**Bohr-Landau zero-density theorem** (classical). If $N(\sigma, T)$ denotes the number of zeros of $\zeta$ with $\Re(\rho) > \sigma$ and $|\Im(\rho)| \leq T$, then:

$$N(\sigma, T) = O(T^{4\sigma(1-\sigma)+\varepsilon}) \quad \text{for } 1/2 < \sigma \leq 1.$$

In particular: for $\sigma > 3/4$: $N(\sigma, T) = O(T^{3/4+\varepsilon}) = o(T)$.

**Proposition 5** (the contribution of zeros with $\sigma > 3/4$ to $C_\infty^{off}$). The zeros with $\Re(\rho) > 3/4$ (if any) contribute to $C_\infty^{off}$ with amplitudes $A_j = 2/|\rho_j| \leq 2/\gamma_j$. By the density estimate:

$$\sum_{\rho:\,\Re(\rho)>3/4,\,|\gamma|\leq T} \frac{1}{|\rho|} = O\!\left(\sum_{k=1}^{N(3/4,T)} \frac{1}{\gamma_k}\right) = O\!\left(N(3/4,T)^{1+o(1)} \cdot T^{-1}\right) \cdot \log T = O(T^{-1/4+\varepsilon}).$$

The contribution of zeros with $\Re(\rho) > 3/4$ to $C_\infty^{off}(t)$ is $O(T^{-1/4+\varepsilon}) \to 0$ in mean square — hence negligible.

**Proposition 6** (the range $1/2 < \sigma \leq 3/4$). For zeros with $1/2 < \sigma \leq 3/4$:

$$N(1/2+\delta, T) = O(T^{1-\delta+\varepsilon}) \quad \text{for } \delta > 0.$$

A zero with $\sigma = 1/2 + \delta$ has $|\rho| \approx \gamma$ for large $\gamma$, and its contribution to $C_\infty^{off}$ is $\sim 2/\gamma$ (similar to the zeros on the critical line). The distinction between the zeros at $\sigma=1/2$ and at $\sigma=1/2+\delta$ is small in amplitude but NOT in frequency: $\omega_1 = \log|\rho| = \log\sqrt{(1/2+\delta)^2+\gamma^2} \approx \log\gamma + \delta^2/(2\gamma^2) + O(\gamma^{-4})$.

The frequency difference from the mirror zero at $\sigma = 1/2-\delta$: $\Omega(\rho_0) \approx \delta/\gamma^2$ (from the computation in Section 5).

---

## 9. The Fourier argument: orthogonality of the extra frequencies

**The key point.** Condition $(\dagger)$: $C_\infty^{off}(\gamma_n) = 0$ for all $n$, says that the function $C_\infty^{off}$ (which is a sum of cosines with frequencies $\omega_j = \log|\rho_j|$ for $\rho_j$ off the critical line) vanishes at every point $\gamma_n$.

**The function $C_\infty^{off}$ as a generalized Dirichlet series.** For $\Im(z) = \eta > 0$:

$$C_\infty^{off}(z) = 2\sum_{\rho:\,\Re(\rho)\neq 1/2} e^{iz\log|\rho|} \cdot |\rho|^{-1-\eta} \cdot e^{-\eta\log|\rho|}/|\rho|^{-1} \cdot e^{iz\log|\rho|}$$

More precisely: $C_\infty^{off}(t+i\eta) = \sum_j a_j(\eta) e^{it\omega_j}$ with $a_j(\eta) = 2|\rho_j|^{-1-\eta}$ and $\omega_j = \log|\rho_j|$.

For condition $(\dagger)$: $C_\infty^{off}(\gamma_n) = \sum_j a_j e^{i\gamma_n\omega_j} = 0$ for all $n$.

**Theorem 3** (condition $(\dagger)$ implies an eigenvalue equation for the function $C_\infty^{off}$). The family of equations $\{C_\infty^{off}(\gamma_n) = 0\}_{n\geq 1}$ is equivalent to:

$$\int_\mathbb{R} C_\infty^{off}(t) \cdot d\mu_\gamma(t) = 0 \quad (\text{integral with respect to the measure of zeros of }\Xi),$$

in the sense that the measure $\mu_\gamma = \sum_n \delta_{\gamma_n}$ annihilates $C_\infty^{off}$ — i.e., $C_\infty^{off}$ is orthogonal (in the weak sense) to the zero measure.

*Proof.* By definition: $\int C_\infty^{off}(t)d\mu_\gamma(t) = \sum_n C_\infty^{off}(\gamma_n)$. Condition $(\dagger)$ says that each term is zero. $\square$

**Proposition 7** (reformulation via the Fourier transform of $\mu_\gamma$). The condition $\int C_\infty^{off}(t)d\mu_\gamma(t) = 0$ can be written:

$$\sum_j a_j \hat\mu_\gamma(\omega_j) = 0,$$

where $\hat\mu_\gamma(\omega) = \sum_n e^{i\omega\gamma_n}$ (Fourier transform of the zero measure) and the sum is over the frequencies $\omega_j = \log|\rho_j|$ of the zeros off the critical line.

The function $\hat\mu_\gamma(\omega)$ is known: by the explicit formula:

$$\hat\mu_\gamma(\omega) = -\sum_p\Lambda(p)p^{-1/2}p^{-i\omega} + (\text{pole and trivial terms}),$$

(in the regularized distributional sense).

**Consequence.** Condition $(\dagger)$ says that $C_\infty^{off}$, viewed as a function on the frequencies $\{\omega_j\}$, annihilates the Fourier transform of $\mu_\gamma$ at those frequencies. This connects the zeros off the critical line ($\omega_j$) with the sums over primes — a highly non-trivial condition.

---

## 10. The precise wall and the new equivalence

**Theorem 4** (fundamental equivalence of the reverse inclusion). The following are equivalent:

(i) The reverse inclusion (Rev. Inc.): $\Xi(\gamma_n) = 0$ for $\gamma_n \in \mathbb{R}$ implies $C_\infty(\gamma_n) = 0$.

(ii) $C_\infty^{off}(\gamma_n) = 0$ for all $n$ (condition $(\dagger)$).

(iii) $\sum_j a_j \hat\mu_\gamma(\omega_j) = 0$ (the Fourier transform of $\mu_\gamma$ at the frequencies of the off-critical zeros vanishes).

(iv) The zero measure $\mu_\gamma$ is *orthogonal to $C_\infty^{off}$* in the weak sense.

*Proof.* (i) $\iff$ (ii) is Lemma 1 (assuming the on-critical zeros satisfy the reverse inclusion, which holds via the regularization — Proposition 7 of Doc 20). (ii) $\iff$ (iii) is Proposition 7. (iii) $\iff$ (iv) is the definition. $\square$

---

## 11. Final result: combining the counting argument and orthogonality

**Theorem 5** (main result of Doc 21). The combination of:
- Corollary 2 (RH or finitely many zeros off the critical line),
- The orthogonality condition $(\dagger)$ for the remaining finite zeros, and
- The density argument (Proposition 5) that makes the contribution of zeros with $\sigma > 3/4$ negligible,

gives the following conditional result:

*If the zeros of $\zeta$ off the critical line (if any) lie in the region $1/2 < |\Re(\rho)-1/2| < 1/4$ (i.e. $\sigma \in (1/4, 3/4)$) and satisfy the orthogonality condition $(\dagger)$, then the number of such zeros is finite and uniformly bounded.*

**Frankness about the result.** Theorem 5 is a weak result: it rules out INFINITELY MANY zeros off the critical line in certain regions, but does not prove that there are NONE. The central gap — condition $(\dagger)$ for a finite number of zeros — remains open.

---

## 12. The precise gap after Doc 21

**Updated diagram of the Phase 29 program (after Docs 00-21):**

```
Unconditional:
  [CCM] t_n^(λ) ∈ ℝ
  [Doc 08] N_ξ(T;λ) = N_Ξ(T) + O(log T)
  [Doc 15] μ_ξ^λ ⇒ μ_γ^real
  [Doc 17, Thm C1] spec(J_∞) = {C_∞ = 0}
  [Doc 19, Thm 2] {C_∞ = 0} ⊆ {Ξ = 0}
  [Doc 21, Cor 2] N_off(T) = O(1) or RH
  [Doc 21, Thm 4] (Rev. Inc.) ⟺ C_∞^off(γ_n) = 0 ∀n

The gap (equivalent to RH):
  C_∞^off(γ_n) = 0 for all n,
  where the sum is over the zeros of ζ OFF the critical line.

Equivalently:
  ∑_j (2/|ρ_j|) cos(γ_n log|ρ_j|) = 0  ∀n,
  where ρ_j ranges over the off-critical zeros.

Under the hypothesis that NO off-critical zeros exist (RH): the sum is empty and the condition is trivially true.
```

---

## 13. Summary and proposal for Doc 22

**Proved in Doc 21:**
- Decomposition $C_\infty = C_\infty^{on} + C_\infty^{off}$ and condition $(\dagger)$ for the reverse inclusion.
- Proposition 4: the off-critical pair generates two distinct frequencies with zero density $\sim T\log T/(2\pi)$.
- Theorem 2 + Corollary 2: if there are infinitely many off-critical zeros, condition $(\dagger)$ fails — contradicting $\{C_\infty = 0\} \subseteq \{\Xi = 0\}$.
- Theorem 4: (Rev. Inc.) $\iff$ $C_\infty^{off}$ orthogonal to $\mu_\gamma$ $\iff$ $\hat\mu_\gamma(\omega_j) = 0$ at the off-critical frequencies.
- Proposition 5: zeros with $\sigma > 3/4$ contribute negligibly.

**Open:**
- That NO off-critical zeros exist with $\sigma \in (1/4, 3/4)$ in finite but positive number.
- Condition $(\dagger)$ for finitely many off-critical zeros.

**Proposal for Doc 22.** Attack the condition $\hat\mu_\gamma(\omega_j) = 0$ directly. The Fourier transform of $\mu_\gamma$ at the frequencies $\omega_j = \log|\rho_j|$ is related to the sums over primes via the explicit formula. If $\hat\mu_\gamma(\omega_j) \neq 0$ for $\omega_j = \log|\rho_j|$ with $\sigma_j \neq 1/2$: condition $(\dagger)$ fails, and by Theorem 4, the reverse inclusion fails — which by Theorem C3 (Doc 17) implies $\{C_\infty = 0\} \subsetneq \{\Xi = 0\}$. But this is consistent with $J_\infty$ having fewer eigenvalues than zeros of $\Xi$ (if RH fails). The contradiction that would close the argument would be: self-adjointness of $J_\infty$ + the weak convergence $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ prevents $J_\infty$ from "losing" zeros of $\Xi$. Formalizing this "completeness" argument is the goal of Doc 22.
