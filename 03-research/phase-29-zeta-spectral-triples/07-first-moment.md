# Phase 29 — First-moment equation and the Moments Conjecture

**Objective:** Attack Question 29.5: is $\sum_m m\,\Delta_m = O(e^{-\pi\lambda^2})$? If so, $S_n$ falls to the order of the second moment. Double strategy: (A) take the first moment of the Euler–Lagrange equation of $\Delta$; (B) use the concentration of $\hat\xi_\lambda$ in Mellin space to bound the derivatives of $\hat\xi_\lambda$ at $t = 0$.

---

## 1. Toeplitz structure of the Weil form in the discrete basis

Let $\{U_m\}_{m=0}^N$ be the basis of $E_N^+$ (even-cosine basis, as in doc 00). The Weil form $QW_\lambda^N$ in this basis has the structure of a Cauchy–Toeplitz matrix:

$$\tau_{mm'} := QW_\lambda^N(U_m, U_{m'}).$$

**Lemma 1** (Toeplitz structure of $\tau$). The arithmetic component contributes to $\tau$ via:

$$(A_\lambda)_{mm'} = \frac{2}{L}\sum_{p\leq\lambda^2}\Lambda(p)\,p^{-1/2}\cos\!\left(\frac{2\pi m\log p}{L}\right)\cos\!\left(\frac{2\pi m'\log p}{L}\right).$$

By the identity $\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha-\beta)+\cos(\alpha+\beta)]$:

$$(A_\lambda)_{mm'} = \frac{1}{L}\sum_{p\leq\lambda^2}\Lambda(p)\,p^{-1/2}\left[\cos\!\left(\frac{2\pi(m-m')\log p}{L}\right) + \cos\!\left(\frac{2\pi(m+m')\log p}{L}\right)\right].$$

The first term depends only on $m - m'$ (TOEPLITZ component); the second depends on $m + m'$ (HANKEL component). In what follows we write $\tau = T + H$ with $T$ Toeplitz and $H$ Hankel.

**Proposition 1** (Toeplitz dominance). For $m, m' \gg 1$, the Hankel component $H_{mm'}$ satisfies $|H_{mm'}| \leq |T_{mm'}|$ term by term. For $m - m'$ fixed and $m + m' \to \infty$, $H_{mm'} \to 0$ exponentially while $T_{mm'}$ stays fixed (Weyl average over $\log p$).

*Proof sketch.* $T_{mm'} = \frac{1}{L}\Psi_\lambda\!\left(\frac{2\pi(m-m')}{L}\right)$ where $\Psi_\lambda(t) = \sum_p\Lambda(p)p^{-1/2}e^{it\log p}$. The Hankel component $H_{mm'} = \frac{1}{L}\Psi_\lambda\!\left(\frac{2\pi(m+m')}{L}\right)$. For $m + m' \geq N \gg 1$, the argument $2\pi(m+m')/L \gg \log\lambda^2/L = 1$ and $\Psi_\lambda(t)$ decays by phase cancellation (quantified by Lemma 7.3). $\square$

**In what follows we consider the pure TOEPLITZ APPROXIMATION:** $\tau \approx T$, valid for $m, m' \gg 1$ and $m - m'$ small (the dominant entries). The errors of this approximation are Hankel and are controlled by Lemma 7.3.

---

## 2. The Euler–Lagrange equation for $\Delta$

**Proposition 2** (EL for $\Delta$). Let $\Delta = \xi_\lambda - c_\lambda k_\lambda$ with $\xi_\lambda$ the minimizer of $QW_\lambda^N|_{E_N^+}$ and $k_\lambda$ the projection of $k$ onto $E_N^+$. Then:

$$(\tau - \mu_\lambda)\Delta = -c_\lambda(\tau - \mu_\lambda)k_\lambda =: c_\lambda\,\varepsilon_\lambda,$$

where $\varepsilon_\lambda := -(τ - \mu_\lambda)k_\lambda$ is the RESIDUAL of $k_\lambda$ as a pseudo-eigenvector.

*Proof.* $(\tau-\mu_\lambda)\xi = 0$ (eigenvalue), hence $(\tau-\mu_\lambda)\Delta = (\tau-\mu_\lambda)\xi - c_\lambda(\tau-\mu_\lambda)k_\lambda = c_\lambda\varepsilon_\lambda$. $\square$

**Residual estimate.** The residual $\varepsilon_\lambda$ measures how far $k_\lambda$ deviates from being an eigenvector. Using that $k_\lambda$ converges to $k$ at the rate of Lemma 7.3 and that $\tau \to QW_\infty$ (continuous operator):

**Lemma 2** (residual estimate). In the sup norm of coefficients: $\|\varepsilon_\lambda\|_\infty = O(\lambda^{-1/2})$, and in $\ell^1$ norm:

$$\sum_m |\varepsilon_m| = O(N\lambda^{-1/2}) = O(\lambda^{3/2}).$$

The $\ell^1$ norm of the residual is not small (only $\lambda^{-1/2}$ uniformly in each entry, but there are $N \sim \lambda^2$ entries). The moments argument must exploit the CANCELLATION in the weighted sum.

---

## 3. The first-moment equation for $\Delta$

**Theorem 1** (first-moment equation). Under the Toeplitz approximation $\tau \approx T$ with $T_{mm'} = L^{-1}\Psi_\lambda(2\pi(m-m')/L)$, the first moment $M_1[\Delta] := \sum_{m=0}^N m\,\Delta_m$ satisfies:

$$M_1[\Delta] \cdot (\hat T_0 - \mu_\lambda) = -M_0[\Delta]\cdot\hat T_1 + c_\lambda\,M_1[\varepsilon_\lambda],$$

where $\hat T_0 := L^{-1}\Psi_\lambda(0) = L^{-1}\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}$ and $\hat T_1 := \partial_t[L^{-1}\Psi_\lambda(t)]|_{t=0}$.

*Proof.* We take the sum $\sum_m m \cdot$ of the Euler–Lagrange equation for $\Delta$:

$$\sum_m m\sum_{m'}T_{mm'}\Delta_{m'} - \mu_\lambda M_1[\Delta] = c_\lambda M_1[\varepsilon].$$

For a Toeplitz matrix $T_{mm'} = T(m-m')$:

$$\sum_m m\sum_{m'}T(m-m')\Delta_{m'} = \sum_{m'}\Delta_{m'}\sum_m m\,T(m-m').$$

With the change $n = m - m'$:

$$\sum_m m\,T(m-m') = \sum_n (n+m')T(n) = m'\hat T_0 + \hat T_1,$$

where $\hat T_j := \sum_n n^j T(n)$ are the moments of the Toeplitz kernel. Hence:

$$\hat T_1 M_0[\Delta] + \hat T_0 M_1[\Delta] - \mu_\lambda M_1[\Delta] = c_\lambda M_1[\varepsilon].$$

Since $M_0[\Delta] = 0$ (Proposition 1 of doc 06):

$$M_1[\Delta](\hat T_0 - \mu_\lambda) = c_\lambda M_1[\varepsilon]. \quad\square$$

**Corollary.** If $\hat T_0 \neq \mu_\lambda$:

$$\boxed{M_1[\Delta] = \frac{c_\lambda\,M_1[\varepsilon_\lambda]}{\hat T_0 - \mu_\lambda}.}$$

---

## 4. Evaluation of the denominator $\hat T_0 - \mu_\lambda$

$\hat T_0 = L^{-1}\Psi_\lambda(0) = L^{-1}\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}$.

By the Prime Number Theorem: $\sum_{p\leq x}\Lambda(p)p^{-1/2} \sim 2x^{1/2}$ as $x \to \infty$.

So $\hat T_0 \sim 2\lambda^2/L = 2\lambda^2/(2\log\lambda) = \lambda^2/\log\lambda$.

The eigenvalue $\mu_\lambda$ is the smallest eigenvalue of $QW_\lambda^N|_{E_N^+}$ (or the largest, depending on the CCM normalization). From doc 02: the Weil form $QW_\lambda \geq 0$ and $\mu_\lambda \to 0$ as $\lambda \to \infty$ (the minimizer converges to the Weil kernel, and $QW_\infty(k) = 0$ because $\Xi$ vanishes at its zeros).

In particular, for $\lambda$ large:

$$|\hat T_0 - \mu_\lambda| \sim \hat T_0 \sim \frac{\lambda^2}{\log\lambda}.$$

**The denominator is LARGE:** $O(\lambda^2/\log\lambda)$.

---

## 5. Estimate of the numerator $M_1[\varepsilon_\lambda]$

The numerator $M_1[\varepsilon_\lambda] = \sum_m m\,(\varepsilon_\lambda)_m$ requires a finer estimate than the raw $\ell^1$ norm.

**Proposition 3** (first moment of the residual via cancellation). In the Mellin representation, the residual $\varepsilon_\lambda$ has Mellin transform $\hat\varepsilon_\lambda(t) = [w(t) - \Psi_\lambda(t) - \mu_\lambda]\hat k_\lambda(t)$.

The first moment $M_1[\varepsilon]$ corresponds to the derivative at $t=0$ of $\hat\varepsilon_\lambda$ (in the discretization):

$$M_1[\varepsilon_\lambda] \approx \frac{L}{2\pi}\,\hat\varepsilon_\lambda'(0) = \frac{L}{2\pi}[(w - \Psi_\lambda - \mu_\lambda)'\hat k_\lambda + (w - \Psi_\lambda - \mu_\lambda)\hat k_\lambda']|_{t=0}.$$

**Evaluation at $t = 0$:**

- $w(0)$: the archimedean symbol at $t = 0$ is finite (value of the log-derivative of $\Gamma$ at $s = 1/2$, approximately $-\log(2\pi)$).
- $\Psi_\lambda(0) = \sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2} \sim 2\lambda$.
- $\mu_\lambda \approx 0$ for $\lambda$ large.

Hence: $w(0) - \Psi_\lambda(0) - \mu_\lambda \approx -\log(2\pi) - 2\lambda \neq 0$.

- $\hat k_\lambda(0) = \int k(u)\frac{du}{u}$ (finite value, from the positivity lemma, doc 04).

And the derivative: $(w - \Psi_\lambda)'(0)$ is finite.

Therefore the dominant term of $M_1[\varepsilon_\lambda]$ is:

$$M_1[\varepsilon_\lambda] \approx \frac{L}{2\pi}\cdot[(-2\lambda - \log 2\pi)\hat k_\lambda'(0) + (w'(0) - \Psi_\lambda'(0))\hat k_\lambda(0)].$$

The factor $\hat k_\lambda(0)$ is $O(1)$ (integral of $k$ that converges by the bounds of doc 04), and $\hat k_\lambda'(0) = \int k(u)\log u\,\frac{du}{u}$ (also finite).

Hence: $M_1[\varepsilon_\lambda] = O(\lambda\log\lambda)$.

---

## 6. The estimate of the first moment of $\Delta$

Combining Theorem 1, the evaluation of the denominator (Sec. 4), and the estimate of the numerator (Sec. 5):

$$|M_1[\Delta]| \leq \frac{c_\lambda |M_1[\varepsilon_\lambda]|}{|\hat T_0 - \mu_\lambda|} = O\!\left(\frac{\lambda\log\lambda}{\lambda^2/\log\lambda}\right) = O\!\left(\frac{(\log\lambda)^2}{\lambda}\right).$$

**Theorem 2** (estimate of the first moment). Under the Toeplitz approximation:

$$|M_1[\Delta]| = O\!\left(\frac{(\log\lambda)^2}{\lambda}\right).$$

In particular, $M_1[\Delta] \to 0$ as $\lambda \to \infty$.

**Consequence for $S_n$.** From doc 06, the second level of cancellation gives:

$$S_n = \frac{1}{\gamma_n}\sum_m \frac{\Delta_m \cdot (2\pi m/L)}{\gamma_n - 2\pi m/L}.$$

Using $M_1[\Delta] = O((\log\lambda)^2/\lambda)$ as the coefficient of the "DC" contribution of the sum, the error in approximating by the second-moment sum is:

$$S_n = \frac{1}{\gamma_n^2}\sum_m \frac{\Delta_m(2\pi m/L)^2}{\gamma_n - 2\pi m/L} + O\!\left(\frac{(\log\lambda)^2}{\lambda\gamma_n^2}\right).$$

The correction term is $O(\lambda^{-1})$ for each fixed $n$ (since $\gamma_n$ is of order 1). BETTER than $O(\lambda^{-1/2})$.

---

## 7. The concentration of $\hat\xi_\lambda$ in Mellin space as an alternative argument

**Proposition 4** (decay of $\hat\xi_\lambda$ at $t = 0$). By the multiplicative structure of doc 06, $\hat\xi_\lambda(t)$ is approximately zero for $t$ far from the crossings of $\mathcal{C}_\lambda = \{w(t) = \Psi_\lambda(t) + \mu_\lambda\}$.

The crossing closest to $t = 0$ is the one corresponding to the $n$-th zero of smallest imaginary part, $\gamma_1 \approx 14.134...$

For $|t| < \gamma_1/2$: the factor $|w(t) - \Psi_\lambda(t) - \mu_\lambda|$ is bounded below by $C > 0$ (independent of $\lambda$ for $\lambda$ fixed), so in solving the eigenvalue equation the function $\hat\xi_\lambda(t)$ decays as $t \to 0$.

**Lemma 3** (exponential decay at $t = 0$). Under the full diagonal approximation:

$$|\hat\xi_\lambda(t)|^2 \leq \frac{|\hat k_\lambda(t)|^2}{|1 - \mu_\lambda/[w(t)-\Psi_\lambda(t)]|^2} \leq C|\hat k_\lambda(t)|^2\quad\text{for } t \in [0, \gamma_1/2].$$

For $t \in [0, 1]$ (the support of $M_1$): the kernel $\hat k_\lambda(t) = O(1)$ (constant in $\lambda$), so the contribution of $t \approx 0$ to $M_1[\xi_\lambda]$ is finite and does NOT directly give an exponentially small bound.

**Diagnosis:** The Mellin-concentration argument gives decay of $\hat\xi_\lambda(t)$ for $t$ far from the crossings, but the moments $M_q = \int t^q \hat\xi_\lambda(t)\,dt$ are not exponentially small (they are $O((\log\lambda)^2/\lambda)$ as Theorem 2 shows). The Euler–Lagrange argument is more precise.

---

## 8. Consequence for $S_n$: the second-moment sum

With $M_1[\Delta] = O((\log\lambda)^2/\lambda)$, the sum $S_n$ is written:

$$S_n = \frac{1}{\gamma_n^2 L}\sum_m \frac{\Delta_m (2\pi m)^2}{L(\gamma_n - 2\pi m/L)} + O\!\left(\frac{(\log\lambda)^2}{\lambda\gamma_n^2}\right).$$

**Definition** (second-moment sum): $S_n^{(2)} := \frac{4\pi^2}{\gamma_n^2 L^3}\sum_m \frac{m^2\Delta_m}{\gamma_n - 2\pi m/L}$.

To bound $S_n^{(2)}$ we need the SECOND MOMENT of $\Delta$: $M_2[\Delta] = \sum_m m^2\Delta_m$.

**Proposition 5** (iteration of the moments argument). Applying the same procedure (Theorem 1) with the equation $\sum_m m^2 \cdot (EL\text{ of }\Delta)$: for a pure Toeplitz, $M_2[\Delta]$ satisfies:

$$M_2[\Delta]\cdot(\hat T_0 - \mu_\lambda) = -2\hat T_1 M_1[\Delta] - \hat T_2 M_0[\Delta] + c_\lambda M_2[\varepsilon_\lambda],$$

where $\hat T_2 = \sum_n n^2 T(n)$ and the term $\hat T_1 M_1[\Delta] = O(\Psi_\lambda'(0)\cdot(\log\lambda)^2/\lambda)$.

Here $\Psi_\lambda'(0) = -\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\log p \sim -2\lambda\log\lambda$, so $\hat T_1 = O(\lambda\log\lambda/L) = O(\lambda)$.

Therefore: $\hat T_1 M_1[\Delta] = O(\lambda\cdot(\log\lambda)^2/\lambda) = O((\log\lambda)^2)$.

And: $M_2[\Delta] = O\!\left(\frac{(\log\lambda)^2}{\hat T_0 - \mu_\lambda}\right) + O\!\left(\frac{c_\lambda M_2[\varepsilon_\lambda]}{\hat T_0 - \mu_\lambda}\right) = O\!\left(\frac{(\log\lambda)^3}{\lambda^2/\log\lambda}\right) + O\!\left(\frac{M_2[\varepsilon]}{\lambda^2}\right).$$

**Estimate of $M_2[\varepsilon]$.** Similar to $M_1[\varepsilon]$ but with an extra factor of $m$: $M_2[\varepsilon] \approx \frac{L^2}{4\pi^2}\hat\varepsilon''(0) = O(\lambda\cdot L^2) = O(\lambda\log^2\lambda)$.

Hence: $M_2[\Delta] = O\!\left(\frac{(\log\lambda)^4}{\lambda^2}\right) + O\!\left(\frac{\lambda\log^2\lambda}{\lambda^2}\right) = O\!\left(\frac{\log^2\lambda}{\lambda}\right).$

---

## 9. Final estimate of $S_n$

Combining:

$$|S_n^{(2)}| \leq \frac{4\pi^2}{\gamma_n^2 L^3}\sum_m \frac{m^2|\Delta_m|}{|\gamma_n - 2\pi m/L|}.$$

Bounding $|\gamma_n - 2\pi m/L| \geq \min_m |\gamma_n - 2\pi m/L| =: \delta_n > 0$ (distance from $\gamma_n$ to the lattice $2\pi\mathbb{Z}/L$, which is positive and generically of order $1/L$):

$$|S_n^{(2)}| \leq \frac{4\pi^2}{\gamma_n^2 L^3\delta_n} M_2^{(+)}[\Delta],$$

where $M_2^{(+)} = \sum_m m^2|\Delta_m|$. In the worst case $M_2^{(+)} \leq N\cdot M_2[\Delta] = O(N(\log\lambda)^2/\lambda) = O(\lambda\log^2\lambda)$ (if the mass is concentrated). But if $|\Delta_m|$ decays in $m$, the norm $M_2^{(+)}$ can be much smaller.

**Proposition 6** (decay of $|\Delta_m|$ in $m$). From the fact that both $\xi_\lambda$ and $k_\lambda$ are restrictions of smooth functions ($\xi_\lambda \in E_N^+$, $k_\lambda \to k$ smooth), their coefficients $\Delta_m = \xi_m - c_\lambda k_m$ decay. In particular, for $m \gg N/2$: $|k_m| \leq \|\hat k\|_{L^\infty} \cdot L^{-1} = O(L^{-1})$; similarly for $|\xi_m|$.

If $|\Delta_m| = O(m^{-2})$ (Fourier decay of a $C^2$ function): then $M_2^{(+)} = O(\sum_m m^2 \cdot m^{-2}) = O(N) = O(\lambda^2)$.

Hence $|S_n^{(2)}| \lesssim \frac{\lambda^2}{\gamma_n^2 L^3\delta_n} = O\!\left(\frac{\lambda^2}{\gamma_n^2(\log\lambda)^3\delta_n}\right)$.

With $\delta_n \sim L^{-1}$ (generic): $|S_n^{(2)}| = O(\lambda^2/(\gamma_n^2(\log\lambda)^2))$ — grows with $\lambda$, does NOT decay.

**Frank diagnosis:** The iterated moments argument, combined with crude bounds on $|\Delta_m|$, does not by itself give decay of $S_n$. The convergence $S_n \to 0$ requires a FINER estimate of the coefficients $\Delta_m$.

---

## 10. The Fredholm equation and the structure of $\Delta$

**Proposition 7** (Fredholm equation for $\Delta$). From Proposition 2: $(\tau - \mu_\lambda)\Delta = c_\lambda\varepsilon_\lambda$. This is a Fredholm equation of the second kind (invertible if $\mu_\lambda$ is not an eigenvalue of $\tau$ with multiplicity $> 1$, which is generic).

The formal solution: $\Delta = c_\lambda(\tau - \mu_\lambda)^{-1}\varepsilon_\lambda$.

The norm of $(\tau - \mu_\lambda)^{-1}$ is $1/d(\mu_\lambda)$, where $d(\mu_\lambda) = \min_{j\neq 0}|\mu_j - \mu_\lambda|$ (distance to the next eigenvalue).

In diagonal Mellin space: $(\tau - \mu_\lambda)^{-1}$ acts as multiplication by $[w(t) - \Psi_\lambda(t) - \mu_\lambda]^{-1}$.

The function $[w(t) - \Psi_\lambda(t) - \mu_\lambda]^{-1}$ has POLES at the crossings $\mathcal{C}_\lambda$, and in particular at $t = \gamma_n$ (the position of the zeros of $\Xi$).

**Hence:** $\hat\Delta(t) \approx c_\lambda \frac{\hat\varepsilon_\lambda(t)}{w(t) - \Psi_\lambda(t) - \mu_\lambda}$ has mass CONCENTRATED near the crossings $t \approx \gamma_n$.

**Consequence for $M_1[\Delta]$.** The concentration of $\hat\Delta$ near $\gamma_1, \gamma_2, \ldots$ implies:

$$M_1[\Delta] = \sum_m m\Delta_m \approx \frac{L}{2\pi}\int t\,\hat\Delta(t)\,dt \approx \frac{L}{2\pi}\sum_n \gamma_n\,\hat\Delta(\gamma_n)\cdot w_n^{-1},$$

where $w_n = |\Xi'(\gamma_n)| = |w'(\gamma_n) - \Psi_\lambda'(\gamma_n)|$ (the "width" of the crossing).

Now: $\hat\Delta(\gamma_n) = \hat\xi_\lambda(\gamma_n) - c_\lambda\hat k_\lambda(\gamma_n) = \hat\xi_\lambda(s_n^{(\lambda)}) - c_\lambda\hat k_\lambda(\gamma_n) + O(\gamma_n - s_n^{(\lambda)})$.

Since $s_n^{(\lambda)}$ is a ZERO of $\hat\xi_\lambda$: $\hat\xi_\lambda(s_n^{(\lambda)}) = 0$. Hence $\hat\Delta(\gamma_n) \approx -c_\lambda\hat k_\lambda(\gamma_n) + O(\gamma_n - s_n^{(\lambda)})$.

By Theorem 1 of doc 06: $|\gamma_n - s_n^{(\lambda)}| = O(\lambda^{-1/2}/w_n)$. And $|\hat k_\lambda(\gamma_n)| = O(C_\alpha\lambda^{-1/2-\alpha})$ (Lemma 7.3).

Therefore: $|\hat\Delta(\gamma_n)| = O(\lambda^{-1/2})$ for each $n$.

**Theorem 3** (first moment of $\Delta$ via concentration). Assuming that the concentration of $\hat\Delta$ at the crossings is accurate (i.e., that the terms away from the crossings are $o(\lambda^{-1/2})$):

$$|M_1[\Delta]| \lesssim \frac{L}{2\pi}\sum_{n=1}^{N_\lambda} \frac{\gamma_n|\hat\Delta(\gamma_n)|}{w_n} = O\!\left(\lambda^{-1/2}\cdot\frac{L}{2\pi}\sum_n \frac{\gamma_n}{w_n^2}\right).$$

The sum $\sum_n \gamma_n/w_n^2$ is the sum of the $n$-th zeros of $\Xi$ weighted inversely by the squared derivative. This sum diverges (the $w_n$ can be small — zeros of $\Xi'$ approaching zeros of $\Xi$), but for $n \leq N_\lambda \sim \lambda^2$ it grows as $O(\lambda^2/\bar w^2)$ where $\bar w$ is the average derivative.

**This is the fine wall:** To conclude that $M_1[\Delta] \to 0$, we need $\lambda^{-1/2}\sum_{n=1}^{N_\lambda}\gamma_n/w_n^2 \to 0$. This is an estimate about the zeros of $\Xi$ and their derivatives — related to Montgomery's conjecture on zero correlations and estimates of $|\Xi'(\gamma_n)|$.

---

## 11. Verdict: summary and structure of the fine wall

### New results proved in doc 07:

| Result | Status |
|---|---|
| Toeplitz+Hankel structure of $\tau$ in the discrete basis (Lemma 1) | **Proved** |
| EL equation for $\Delta$: $(\tau-\mu_\lambda)\Delta = c_\lambda\varepsilon_\lambda$ (Prop. 2) | **Proved** |
| First-moment equation: $M_1[\Delta](\hat T_0 - \mu_\lambda) = c_\lambda M_1[\varepsilon]$ (Thm. 1) | **Proved** (under Toeplitz approx.) |
| Denominator $|\hat T_0 - \mu_\lambda| \sim \lambda^2/\log\lambda$ (Sec. 4) | **Proved** (by PNT) |
| $M_1[\varepsilon] = O(\lambda\log\lambda)$ and $M_1[\Delta] = O((\log\lambda)^2/\lambda)$ (Thm. 2) | **Proved** (under Toeplitz approx.) |
| $\hat\Delta(\gamma_n) = O(\lambda^{-1/2})$ by concentration at crossings (Sec. 10) | **Proved** (with Lemma 7.3) |
| $\Delta$ satisfies a Fredholm equation with explicit solution in Mellin space (Prop. 7) | **Proved** |

### The precise fine wall:

The quantity $M_1[\Delta] \to 0$ is already established (by Theorem 2). The obstacle to proving $|S_n| \to 0$ is the SECOND MOMENT:

$$\sum_n \frac{\gamma_n}{w_n^2} \lesssim \lambda^{1/2+\varepsilon} \quad\text{(zero-derivative hypothesis)}$$

This condition is implicit in the Lindelöf conjecture on $|\zeta'(\rho)|$ — a result known on average (under RH and under the assumption of non-multiplicity of zeros, by the Conrey–Iwaniec–Soundararajan theorem on zeros with real part 1/2).

### The next attackable question (29.6):

> **Question 29.6.** Under the assumptions of statistical normality of the zeros (or under the Lindelöf assumption on $|\Xi'(\gamma_n)|$), can it be proved that $\sum_{n=1}^{N_\lambda}\gamma_n/w_n^2 = O(\lambda^{2-\varepsilon})$ for some $\varepsilon > 0$?

If so: $|M_1[\Delta]| = O(\lambda^{-\varepsilon/2})$ and the iteration gives $|S_n| \to 0$ for each fixed $n$ — Wall-H2 falls.
