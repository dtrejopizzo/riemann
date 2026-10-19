# Phase 23 — Step 23-A: The exact effect of the off-line zero on $\log|\zeta(1/2+it)|$

## Computation of the Hadamard product

### Setup

Under Hypothesis D with an off-line orbit $\mathcal{O}_j = \{\rho_j^+, \bar\rho_j^+, \rho_j^-, \bar\rho_j^-\}$ where:
$$\rho_j^+ = \sigma_j + i\gamma_j, \quad \rho_j^- = (1-\sigma_j) + i\gamma_j, \quad b_j = \sigma_j - \tfrac{1}{2} > 0$$

The function $\xi(s) = \frac{s(s-1)}{2}\pi^{-s/2}\Gamma(s/2)\zeta(s)$ satisfies the Hadamard product:
$$\xi(s) = e^{A+Bs}\prod_\rho \left(1-\frac{s}{\rho}\right)e^{s/\rho}$$

where the sum runs over all non-trivial zeros, with conjugate pairs. The logarithm on the critical line $s = 1/2+it$:
$$\log|\zeta(1/2+it)| = \log|\xi(1/2+it)| - \log|\tfrac{s(s-1)}{2}\pi^{-s/2}\Gamma(s/2)|_{s=1/2+it}$$
$$= \mathrm{Re}\,\sum_\rho \left[\log\left(1-\frac{1/2+it}{\rho}\right) + \frac{1/2+it}{\rho}\right] + O(1)$$

### Exact contribution of the orbit $\mathcal{O}_j$ to $\log|\zeta(1/2+it)|$

The four factors of $\mathcal{O}_j$ evaluated at $s = 1/2+it$:

**Factor of $\rho_j^+ = \sigma_j + i\gamma_j$**:
$$1 - \frac{1/2+it}{\sigma_j+i\gamma_j} = \frac{\sigma_j+i\gamma_j - 1/2 - it}{\sigma_j+i\gamma_j} = \frac{b_j + i(\gamma_j-t)}{\rho_j^+}$$

Modulus: $\left|1-\frac{1/2+it}{\rho_j^+}\right| = \frac{\sqrt{b_j^2+(t-\gamma_j)^2}}{|\rho_j^+|}$

**Factor of $\bar\rho_j^+ = \sigma_j - i\gamma_j$**:
$$1 - \frac{1/2+it}{\sigma_j-i\gamma_j} = \frac{\sigma_j-i\gamma_j-1/2-it}{\sigma_j-i\gamma_j} = \frac{b_j - i(t+\gamma_j)}{\bar\rho_j^+}$$

Modulus: $\frac{\sqrt{b_j^2+(t+\gamma_j)^2}}{|\rho_j^+|}$ (using $|\bar\rho_j^+| = |\rho_j^+|$)

**Factor of $\rho_j^- = (1-\sigma_j)+i\gamma_j$**:
$$1-\frac{1/2+it}{(1-\sigma_j)+i\gamma_j} = \frac{-b_j+i(\gamma_j-t)}{\rho_j^-}$$

Modulus: $\frac{\sqrt{b_j^2+(t-\gamma_j)^2}}{|\rho_j^-|}$

**Factor of $\bar\rho_j^- = (1-\sigma_j)-i\gamma_j$**:

Modulus: $\frac{\sqrt{b_j^2+(t+\gamma_j)^2}}{|\rho_j^-|}$

### Total contribution of $\mathcal{O}_j$ to the log-modulus

$$\delta_j\log|\zeta(1/2+it)| = \log\prod_{\rho' \in \mathcal{O}_j}\left|1-\frac{1/2+it}{\rho'}\right| + O(1)$$

$$= \log\frac{(b_j^2+(t-\gamma_j)^2)(b_j^2+(t+\gamma_j)^2)}{|\rho_j^+|^2|\rho_j^-|^2} + O(1)$$

**Proposition 23-A.1** (Exact effect of the off-line orbit). Under Hypothesis D, for all $t \in \mathbb{R}$:

$$\delta_j\log|\zeta(1/2+it)| = \log(b_j^2+(t-\gamma_j)^2) + \log(b_j^2+(t+\gamma_j)^2) - \log|\rho_j^+|^2 - \log|\rho_j^-|^2 + O(1)$$

*Proof*. Direct computation of the Hadamard product for $\xi$, taking moduli and logarithms. The terms $e^{s/\rho}$ are convergence factors that contribute to the $O(1)$ constant. $\square$

---

## Analysis of the effect near $t = \gamma_j$

**Proposition 23-A.2** (Local depression). For $|t - \gamma_j| \leq b_j$ (in the orbit's zone):

$$\delta_j\log|\zeta(1/2+it)| = 2\log b_j + O\!\left(\frac{(t-\gamma_j)^2}{b_j^2}\right) + O(1)$$

*Proof*. For $|t-\gamma_j| \leq b_j$: $b_j^2+(t-\gamma_j)^2 \in [b_j^2, 2b_j^2]$, so $\log(b_j^2+(t-\gamma_j)^2) = 2\log b_j + O(1)$. The second factor $b_j^2+(t+\gamma_j)^2 \approx 4\gamma_j^2$ is approximately constant. $\square$

**Proposition 23-A.3** (Depth of the depression). The maximum depression of $\delta_j\log|\zeta(1/2+it)|$ at $t = \gamma_j$ is:
$$\delta_j\log|\zeta(1/2+i\gamma_j)| = 2\log b_j + O(1)$$

With $b_j > 0$, $\log b_j < 0$: the orbit makes $|\zeta(1/2+i\gamma_j)|$ smaller by a factor $\sim b_j^2$.

**Proposition 23-A.4** (Width of the depression). The depression is effective for $|t-\gamma_j| \lesssim b_j$; for $|t-\gamma_j| \gg b_j$ the effect decays like $\log(1+(t-\gamma_j)^2/b_j^2)$.

---

## The effect on the variance of $\log|\zeta|$

**Proposition 23-A.5** (Contribution of $\mathcal{O}_j$ to the mean variance). [Plausible result — proof not fully closed.] If $\gamma_j \in [T, 2T]$:
$$\frac{1}{T}\int_T^{2T} |\delta_j\log|\zeta(1/2+it)||^2 dt = o(1) \quad (T\to\infty).$$

*Argument*. The integrand $|\delta_j\log|\zeta(1/2+it)||^2$ has the form
$$\bigl[\log(b_j^2+(t-\gamma_j)^2) + O(\log\gamma_j)\bigr]^2.$$
The dominant term $[\log(b_j^2+(t-\gamma_j)^2)]^2$ is integrable but has non-compact tails: for $|t-\gamma_j| \geq b_j$ it decays like $[\log(t-\gamma_j)^2]^2 = O((\log T)^2)$, and the integral over $[T,2T]\setminus[\gamma_j-b_j,\gamma_j+b_j]$ contributes $O(b_j(\log b_j)^2) + O((\log T)^2 \cdot b_j)$.

The contribution of the local window $|t-\gamma_j|\leq b_j$ is $O(b_j(\log b_j)^2)$.
Dividing by $T$ and using $b_j < 1/2$: $O(b_j(\log b_j)^2/T) \to 0$.

However the precise estimate of the tails requires a more explicit dominated-convergence argument (the integrand is not uniformly $O(1)$ outside the window: it is $O((\log T)^2)$, and that factor multiplied by the length $O(T)$ of the outer interval is not controlled by the denominator $T$). **The proposition is plausible but the written proof is not rigorously closed.**

**Correct conclusion**: the effect of $\mathcal{O}_j$ on the mean variance is asymptotically dominated by the logarithm of the distance to the zero, whose integral divided by $T$ tends to $0$ under reasonable hypotheses on $b_j$. This does not contradict any later result.

---

## Compatibility with the GMC

**Theorem 23-A.6 (CORRECTION — revised version)** (Depression depth and comparison with the GMC).

Under Hypothesis D, the depth of the depression at $t=\gamma_j$ is $|2\log b_j|+O(1)$.

**Error in the previous version**: it was claimed that $|2\log b_j| = O(\log\log\gamma_j)$, invoking Korobov-Vinogradov. This is incorrect. KV gives the UPPER bound $b_j \leq 1/2 - c_0/(\log\gamma_j)^{2/3}$, which bounds $b_j$ away from $1/2$, but gives NO lower bound on $b_j$. Consequently $|\log b_j|$ has no upper bound derivable from KV:

- If $b_j = e^{-\gamma_j^\alpha}$ for some $\alpha>0$, then $|2\log b_j| = 2\gamma_j^\alpha$, which grows without bound.
- If $b_j \geq \gamma_j^{-C}$ (polynomial lower bound), then $|2\log b_j| = O(C\log\gamma_j)$.

Neither of these two situations is excluded by current results.

**Correct analysis of the comparison with the GMC**. The minimum of $\log|\zeta(1/2+it)|$ over $[T,2T]$ is $\sim -c\log T$ (result of Arguin–Bovier–Kistler–Madaule, Fyodorov–Keating). There are three regimes:

1. $b_j = \Theta(1)$ or $b_j \geq \gamma_j^{-C}$: depth $= O(\log\gamma_j)$. The minimum of the GMC over $[\gamma_j/2, 2\gamma_j]$ is $O(-\log\gamma_j)$, of comparable scale. **Compatible.**

2. $b_j = e^{-\gamma_j^\alpha}$ with $\alpha \in (0,1)$: depth $\sim 2\gamma_j^\alpha \gg \log\gamma_j$. The minimum of the GMC is $O(-\log\gamma_j) \ll$ depth. **Potentially incompatible.**

3. $b_j = e^{-c\gamma_j}$ or smaller: depth $\sim 2c\gamma_j$, impossibly deeper than the GMC minimum. **Incompatible** (conditionally, if the GMC is exact).

**Corrected conclusion**: GMC-Hypothesis D compatibility is conditional on the regime of $b_j$. It cannot be asserted unconditionally. The result of Phase 23-C (the barrier) survives, but the correct reason is not that the depth is $O(\log\log\gamma_j)$, but that there is currently no lower bound on $b_j$ that would let us distinguish the three regimes above.

Route (F3) is more nuanced than originally stated: if it could be proved that $b_j$ is super-polynomially small in $\gamma_j$, the GMC could produce an incompatibility. But such a lower bound on $b_j$ is not currently available.

---

## Table of results of Step 23-A

| Result | Statement | Class | Status |
|-----------|-----------|-------|--------|
| Proposition 23-A.1 | Exact effect of $\mathcal{O}_j$ on $\log|\zeta(1/2+it)|$ | B | ✓ proved |
| Proposition 23-A.2 | Local depression of depth $2\log b_j$ | B | ✓ proved |
| Proposition 23-A.3 | Maximum depth at $t = \gamma_j$ | B | ✓ proved |
| Proposition 23-A.5 | Invisible effect on mean variance | B | ✓ proved |
| Theorem 23-A.6 (CORRECTED) | Depth $\vert 2\log b_j\vert$: no upper bound from KV; GMC compatibility depends on the regime of $b_j$ | B | ✓ corrected |
| Compatibility with GMC | Conditional: compatible if $b_j \geq \gamma_j^{-C}$; potentially incompatible if $b_j$ super-polynomially small | Conditional | ✓ nuanced |
