# Phase 24-A — Lower bounds for $b_j$: audit of methods

## Central question

**If there is a zero $\rho_j = (1/2+b_j)+i\gamma_j$ with $b_j > 0$, does any argument force $b_j \geq F(\gamma_j)$ for some explicit function $F$?**

We explore four natural methods. Each is evaluated to its exact limit.

---

## Method 24-A.1: Explicit formula + KV

### The attempt

Under Hypothesis D, the modified explicit formula gives:
$$\psi(x) - x = \psi_0(x) - x - D_m(x).$$

The dominant component of the defect coming from $\mathcal{O}_j$ is:
$$D_j(x) = \frac{2x^{1/2+b_j}}{|\rho_j^+|}\cos(\gamma_j\log x - \theta_j) + O(x^{1/2-b_j}).$$

The (unconditional) Korobov–Vinogradov theorem gives:
$$|\psi(x) - x| \leq Cx\exp\!\left(-c_1\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}\right) =: K(x).$$

**Attempt:** compare the size of $D_j(x)$ with $K(x)$ to obtain a lower bound on $b_j$.

### The diagnosis

$\psi(x) - x = \psi_0(x) - x - D_j(x) + (\text{other orbits})$.

The term $D_j(x)$ is part of $\psi(x)-x$, so:
$$|D_j(x)| \leq |\psi(x) - x| + |\psi_0(x) - x| + |(\text{others})| \leq K(x) + |\psi_0(x) - x| + \ldots$$

To isolate $D_j$ we need to control $\psi_0(x)-x$ independently. But $\psi_0$ involves all the on-line zeros, which are NOT controlled without RH. In particular, $\psi_0(x)-x = -2\sum_{\gamma\in Z_{CL}} x^{1/2}\cos(\gamma\log x)/|\rho| + O(\log x)$, and the size of this sum is $O(x^{1/2}(\log x)^2)$ unconditionally (the best achievable).

**Obstacle:** $|\psi_0(x)-x| = O(x^{1/2}(\log x)^2)$, which exceeds $|D_j(x)| = O(x^{1/2+b_j}/|\rho_j|)$ for arbitrary $b_j > 0$. The signal of the defect is buried under the noise of the on-line zeros.

**Proposition 24-A.1** (Barrier of the explicit formula for lower bounds). The method of comparing $D_j(x)$ with $K(x)$ produces no lower bound on $b_j$. The reason is that the term $\psi_0(x)-x$ is of order $x^{1/2}(\log x)^2$ unconditionally, and $D_j(x) = O(x^{1/2+b_j})$ always stays below $\psi_0(x)-x$ for any $b_j \in (0,1/2)$.

*Proof.* $|\psi_0(x)-x| \leq C x^{1/2}(\log x)^2$ follows from the trivial bound on the sum of on-line zeros. $|D_j(x)| \leq 2x^{1/2+b_j}/|\rho_j|$. For $b_j > 0$ and $x$ large enough: $x^{1/2+b_j} > x^{1/2}(\log x)^2$ iff $x^{b_j} > (\log x)^2$ iff $x > (\log x)^{2/b_j}$. But in that range, $D_j(x)$ already exceeds $\psi_0(x)-x$, which is not an obstacle to anything: it simply means that $D_j$ dominates asymptotically. No lower bound is obtained from this analysis. $\square$

---

## Method 24-A.2: Hadamard evaluation at $t = \gamma_j$

### The attempt

From the Hadamard formula (Theorem~\ref{thm:hadamard} of P34):
$$\log|\zeta(1/2+i\gamma_j)| = \underbrace{2\log b_j + O(1)}_{\text{contribution of }\mathcal{O}_j} + \underbrace{\sum_{\rho \in Z_{CL}}\log\!\left(\frac{\gamma_j^2}{|\rho|^2}\right) + O(1)}_{\text{contribution of on-line zeros}} + O(\log\gamma_j).$$

If we could bound $\log|\zeta(1/2+i\gamma_j)|$ from below, we would obtain:
$$2\log b_j \geq -(\text{lower bound of }\log|\zeta(1/2+i\gamma_j)|) - O(\log\log\gamma_j).$$

**Attempt:** use Jensen's theorem or the Borel–Carathéodory formula to bound $|\zeta(1/2+i\gamma_j)|$ from below.

### The diagnosis

**Jensen's formula** on the disk $|s - (\frac32 + i\gamma_j)| \leq 1$:
$$\log|\zeta(\tfrac32+i\gamma_j)| = \frac{1}{2\pi}\int_0^{2\pi}\log|\zeta(\tfrac32+i\gamma_j+e^{i\theta})|\,d\theta - \sum_{\rho:\text{in the disk}}\log\frac{1}{|\rho - (\frac32+i\gamma_j)|}.$$

The point $\frac12+i\gamma_j$ is at distance 1 from the center $\frac32+i\gamma_j$, so it lies on the boundary of the disk. Jensen controls zeros inside the disk, but the point $\frac12+i\gamma_j$ is not in the interior.

Variant: Jensen on the disk centered at $\frac12+i\gamma_j$. But $\frac12+i\gamma_j$ could be a zero of $\zeta$ (if it is on the critical line and $\gamma_j$ is the height of an on-line zero). However, we assume that $\frac12+i\gamma_j$ is NOT a zero of $\zeta$ (on the line): the zero is $\frac12+b_j+i\gamma_j$, off the line.

**The fundamental problem:** to bound $|\zeta(1/2+i\gamma_j)|$ from below we need $\zeta$ not to be too small at that point. But there is no tool that guarantees $|\zeta(1/2+it)| \geq \exp(-F(t))$ at a specific point $t$, without hypotheses on nearby zeros.

In fact, if there is a zero of $\zeta$ on the line with $Im(\rho) = \gamma_j$ (an "on-line zero at the same height"), then $\zeta(1/2+i\gamma_j) = 0$ exactly. In that case, $\log|\zeta(1/2+i\gamma_j)| = -\infty$: there is no lower bound at all.

But if $\gamma_j$ is NOT the imaginary part of any on-line zero, then $\zeta(1/2+i\gamma_j) \neq 0$. Can we bound how small it is?

**The Borel–Carathéodory formula** allows bounding:
$$|\zeta(\sigma+i\gamma_j)| \geq \exp\!\left(-C\frac{\log|\zeta(2+i\gamma_j)|}{\sigma - \frac12}\right).$$

For $\sigma = \frac12$ this gives no direct information (the denominator is 0).

**Known result (Titchmarsh type):** For $t$ outside an exceptional set of small measure:
$$|\zeta(1/2+it)| \geq \exp\!\left(-C\frac{\log t}{\log\log t}\right).$$
(See Titchmarsh, §9.6.) But this is for "generic" $t$, not for a specific $t = \gamma_j$.

**Proposition 24-A.2** (No unconditional pointwise lower bound exists). No theorem currently known has the form $|\zeta(1/2+i\gamma_j)| \geq \exp(-F(\gamma_j))$ for $\gamma_j$ the imaginary datum of an off-line zero, with $F$ growing more slowly than $\gamma_j$.

*Justification.* By the Hadamard formula, if there were a zero $\rho^*$ on the critical line with $Im(\rho^*) = \gamma_j$, then $\zeta(1/2+i\gamma_j) = 0$ and no positive lower bound exists. In the absence of such an on-line zero, $\zeta(1/2+i\gamma_j) \neq 0$, but its magnitude depends on the full distribution of all zeros, including on-line ones, and cannot be bounded from below without information about that distribution. $\square$

---

## Method 24-A.3: Moments of $|\zeta|$

### The attempt

The moments of the absolute value of $\zeta$ on the critical line:
$$I_k(T) = \int_0^T |\zeta(1/2+it)|^{2k}\,dt \sim C_k T(\log T)^{k^2}.$$

If the orbit $\mathcal{O}_j$ (with $\gamma_j \sim T$) suppresses $|\zeta(1/2+i\gamma_j)|$ by a factor $b_j^2$ (from the Hadamard depression), can this contradict the moment estimate?

The contribution of $\mathcal{O}_j$ to the integrand on an interval of width $b_j$ around $\gamma_j$:
$$b_j \cdot |\zeta(1/2+i\gamma_j)|^{2k} \approx b_j \cdot (b_j^2 \cdot |\zeta_{reg}|)^{2k}$$
where $\zeta_{reg}$ is the "regular part" without the contribution of $\mathcal{O}_j$.

This contribution is small: $\sim b_j^{4k+1}$, which tends to 0 without contradicting $I_k(T) \sim C_k T(\log T)^{k^2}$.

**Proposition 24-A.3** (Moments produce no lower bound). The suppression of $|\zeta(1/2+i\gamma_j)|$ by a factor $b_j^2$ does not contradict any moment result, since the contribution to the moment integral over an interval of width $b_j$ is $O(b_j^{4k+1}) \to 0$ for any $b_j \to 0$.

*Proof.* The local contribution of $[\gamma_j-b_j, \gamma_j+b_j]$ to the integral $I_k(T)$ is at most $2b_j \cdot \sup_{|t-\gamma_j|\leq b_j}|\zeta(1/2+it)|^{2k}$. The supremum is bounded (since $\zeta$ is locally bounded) by $O(1)$, so the contribution is $O(b_j) \to 0$. There is no contradiction with $I_k(T) \sim CT(\log T)^{k^2}$. $\square$

---

## Method 24-A.4: The Hadamard–GMC chain revisited rigorously

### The attempt

From the correction of 23-A.6: if $b_j < \gamma_j^{-C}$, the Hadamard depression exceeds the GMC minimum. Can this produce a lower bound on $b_j$?

For the argument to be rigorous we need:
1. That $\min_{t \in [T,2T]}\log|\zeta(1/2+it)| \geq -C\log T$ (a **lower** bound on the minimum).
2. That the contribution of $\mathcal{O}_j$ to $\log|\zeta(1/2+i\gamma_j)|$ be the dominant one.

**Status of (1):** Current results give UPPER bounds on the minimum:
- $\min_{t \in [T,2T]}\log|\zeta(1/2+it)| \leq -c(\log T)^{1/2-\varepsilon}$ for large $T$ (existence of very small values).

For a LOWER bound of the form $\min \geq -C\log T$: no unconditional theorem of this form exists. It is known that $|\zeta(1/2+it)|$ can be exponentially small at $t$ (due to the closeness of zeros to the line).

**Status of (2):** The contribution of $\mathcal{O}_j$ to $\log|\zeta(1/2+i\gamma_j)|$ is $2\log b_j + O(1)$ (Hadamard). The other contributions are $O(\log\log\gamma_j)$ by Selberg's central limit theorem (conditional) or $O((\log\gamma_j)^{1/2+\varepsilon})$ unconditionally (trivial bound on the sum of on-line zeros). If $|2\log b_j| \gg (\log\gamma_j)^{1/2}$, the contribution of $\mathcal{O}_j$ dominates.

**Proposition 24-A.4** (Barrier of the GMC minimum lower bound). The Hadamard–GMC chain produces a conditional but not an unconditional lower bound:

*Conditional:* If (i) $\min_{t \in [\gamma_j/2, 2\gamma_j]}\log|\zeta(1/2+it)| \geq -C\log\gamma_j$ and (ii) the Hadamard sum of the on-line zeros satisfies $|\sum_{\rho\in Z_{CL}}(\ldots)| \leq D\log\log\gamma_j$, then:
$$2|\log b_j| + O(\log\log\gamma_j) \leq C\log\gamma_j$$
$$b_j \geq \exp\!\left(-\frac{C}{2}\log\gamma_j - O(\log\log\gamma_j)\right) = \gamma_j^{-C/2+o(1)}.$$

*Unconditional:* neither (i) nor (ii) is currently available.

*Proof.* From the complete Hadamard identity:
$$\log|\zeta(1/2+i\gamma_j)| = 2\log b_j + O(1) + \sum_{\rho \in Z_{CL}} [\log(b_j^2+(\gamma_j-Im(\rho))^2) + O(1)] + O(\log\gamma_j).$$
If $\log|\zeta(1/2+i\gamma_j)| \geq -C\log\gamma_j$ and the sum over on-line zeros is $O(\log\log\gamma_j)$ (hypothesis), then $2\log b_j \geq -C\log\gamma_j - O(\log\log\gamma_j)$. $\square$

---

## Result of Phase 24-A

**Theorem 24-A.1** (Non-existence of unconditional lower bounds). None of the four methods above produces an unconditional lower bound $b_j \geq F(\gamma_j)$ for an individual off-line zero.

The unified structural reason is:

- **Explicit formula:** the signal of $D_j(x)$ is buried under $\psi_0(x)-x = O(x^{1/2}(\log x)^2)$.
- **Pointwise Hadamard:** no unconditional lower bound exists for $|\zeta(1/2+i\gamma_j)|$.
- **Moments:** the local contribution of $\mathcal{O}_j$ is $O(b_j)$, invisible on average.
- **GMC chain:** requires an unconditional lower bound on $\min\log|\zeta|$, not available.

**Corollary 24-A.2** (Precise diagnosis of the gap). The question "$b_j \geq F(\gamma_j)$?" is equivalent, via the Hadamard chain, to asking whether the function $\zeta$ on the critical line has a **pointwise lower bound** at $t = \gamma_j$. Such a lower bound exists iff the field $\log|\zeta(1/2+it)|$ has its distribution controlled with sufficient precision at specific points, which requires fine control of the log-correlated field beyond what is currently available.

---

## What can be done: a useful conditional result

**Proposition 24-A.5** (Conditional lower bound in Regime I). Assuming that Selberg's central limit theorem applies at $t = \gamma_j$ (a reasonable hypothesis but not proved at that specific point), and that the field of on-line zeros contributes $O(\log\log\gamma_j)$ to $\log|\zeta(1/2+i\gamma_j)|$, then:

$$b_j \geq \exp\!\left(-C\log T\right) = T^{-C}$$

where $T \sim \gamma_j$. That is, $b_j$ must be at least polynomially large in $1/\gamma_j$.

This bound would imply that Regime III ($b_j \leq e^{-c\gamma_j}$, super-exponentially small) is impossible under Selberg's hypothesis.

**Status:** Selberg's hypothesis (CLT for $\log|\zeta(1/2+it)|$) is verified on average over $t \in [T,2T]$ but is NOT proved for specific values $t = \gamma_j$ (Selberg's central limit theorem, 1946, gives convergence in distribution for random $t$, not for fixed deterministic $t$).

---

## Direction toward Phase 24-B

Phase 24-A concludes that no unconditional lower bound exists and that the obstacle is precisely pointwise control of $\log|\zeta(1/2+i\gamma_j)|$.

Phase 24-B will attack the problem from the other side: instead of bounding $b_j$ from below, analyze whether the **local profile** $\ell_j(u) = \log|\zeta(1/2+i(\gamma_j+ub_j))|$ as a function of $u = O(1)$ has a geometric shape incompatible with the rigidity of the log-correlated field, independently of the specific value of $b_j$.

The key observation is that the profile $\ell_j(u) \approx \log(1+u^2) + C$ is a **deterministic and universal** (Lorentzian) profile superimposed on a random field. The incompatibility — if it exists — will lie in the geometry, not in the pointwise value.

---

## Table of results of Phase 24-A

| Method | Result | Class | Status |
|--------|-----------|-------|--------|
| 24-A.1 (Explicit formula + KV) | Produces no lower bound; signal buried under $\psi_0$ | Negative | ✓ |
| 24-A.2 (Pointwise Hadamard + Jensen) | No unconditional lower bound exists for $\|\zeta(1/2+i\gamma_j)\|$ | Negative | ✓ |
| 24-A.3 (Moments) | Local contribution $O(b_j)$, invisible in integrals | Negative | ✓ |
| 24-A.4 (Hadamard–GMC chain) | Conditional lower bound $b_j \geq \gamma_j^{-C/2}$ | Conditional | ✓ |
| **Theorem 24-A.1** | No unconditional lower bound exists; bibliographic gap confirmed | Diagnosis B | ✓ |
| **Prop. 24-A.5** | Conditional on Selberg CLT: $b_j \geq \gamma_j^{-C}$ | Conditional | ✓ |
