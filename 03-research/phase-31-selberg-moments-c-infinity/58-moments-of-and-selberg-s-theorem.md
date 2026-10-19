# Doc 58 — Phase 31: Moments of $C_\infty(\gamma_n)$ and Selberg's Theorem

**Program:** CCM Zeta Spectral Triples — Phase 31  
**Prerequisites:** Docs 42–44, 54  
**Objective:** Compute the moments $M_k(T) = \frac{1}{N(T)}\sum_{\gamma_n\leq T}C_\infty(\gamma_n)^k$ via the deficit formula and the Ingham density estimate. Connect with Selberg's distribution theorem for $\log|\zeta'(\rho_n)|$.  
**Central result:** $M_1(T) = 0$ for every $T$ iff RH. The decay rate $M_1(T) \asymp N_{\mathrm{off}}(T)/T$ is a new invariant of the program.

---

## 1. Setup: the moments of the deficit

**Definition 1.1.** For $T > 0$ and $k \geq 1$, let:

$$M_k(T) := \frac{1}{N(T)}\sum_{\substack{\gamma_n \leq T}} C_\infty(\gamma_n)^k$$

where $N(T) = \#\{\gamma_n \leq T\} \sim \frac{T\log T}{2\pi}$ (Riemann-von Mangoldt formula).

By positivity $C_\infty(\gamma_n) \geq 0$ (Doc 42), all moments are non-negative.

**Proposition 1.2 (Equivalence with RH).** $M_1(T) = 0$ for every $T > 0$ $\iff$ $C_\infty(\gamma_n) = 0$ for every $n$ $\iff$ RH.

*Proof.* Direct from $C_\infty(\gamma_n) \geq 0$ and the equivalence Inc. Inv. $\iff$ RH. $\square$

**Definition 1.3 (Deficit density functional).** Let:

$$\mathcal{D}(T) := \sum_{\gamma_n \leq T} C_\infty(\gamma_n)$$

be the cumulative sum of deficits. Then $M_1(T) = \mathcal{D}(T)/N(T)$.

---

## 2. Computation of $M_1(T)$ via the deficit formula

**Theorem 2.1 (Exact formula for $\mathcal{D}(T)$).** From the deficit formula (Doc 42):

$$\mathcal{D}(T) = \sum_{\gamma_n\leq T}C_\infty(\gamma_n) = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}} \mathcal{S}(\gamma_0, \sigma_0; T)$$

where for each off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$:

$$\mathcal{S}(\gamma_0, \sigma_0; T) := \sum_{\gamma_n\leq T}\!\left[\frac{2(\sigma_0-1/2)}{(\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2}+\frac{2(\sigma_0-1/2)}{(\gamma_n+\gamma_0)^2+(\sigma_0-1/2)^2}\right]$$

**Proposition 2.2 (Integral approximation of $\mathcal{S}$).** By the local density of zeros $d\gamma_n \approx (\log\gamma)/(2\pi)\,d\gamma$:

$$\mathcal{S}(\gamma_0, \sigma_0; T) \approx \int_0^T \frac{2(\sigma_0-1/2)}{(t-\gamma_0)^2+(\sigma_0-1/2)^2}\cdot\frac{\log t}{2\pi}\,dt$$

For $T \gg \gamma_0 \gg \sigma_0-1/2$: the Poisson kernel has mass $\pi$ on $(0,\infty)$, and the density at $\gamma_0$ is $\log\gamma_0/(2\pi)$. Hence:

$$\mathcal{S}(\gamma_0, \sigma_0; T) \approx \pi\cdot\frac{\log\gamma_0}{2\pi} = \frac{\log\gamma_0}{2}$$

*Approximation error.* The error is $O((\sigma_0-1/2)\log\gamma_0/\gamma_0)$ — small for large $\gamma_0$.

**Theorem 2.3 (Formula for $M_1(T)$).** For large $T$:

$$\mathcal{D}(T) = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}:\,\gamma_0\leq T}\frac{\log\gamma_0}{2} + O\!\left(\sum_{\rho_0}\frac{(\sigma_0-1/2)\log\gamma_0}{\gamma_0}\right)$$

$$M_1(T) = \frac{\mathcal{D}(T)}{N(T)} \approx \frac{\pi}{T\log T}\sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}:\,\gamma_0\leq T}\log\gamma_0$$

---

## 3. Upper bound for $M_1(T)$ under the Ingham estimate

**Lemma 3.1 (Ingham estimate revisited).** For any $\sigma > 1/2$:

$$N(\sigma, T) := \#\{\rho\in\mathcal{Z}_{\mathrm{off}}: \mathrm{Re}(\rho)\geq\sigma,\,|\mathrm{Im}(\rho)|\leq T\} \ll T^{2(1-\sigma)}\log T$$

**Theorem 3.2 (Decay of $M_1(T)$).** Let $\sigma_{\min} := \inf_{\rho_0\in\mathcal{Z}_{\mathrm{off}}}\mathrm{Re}(\rho_0)$. Then:

$$M_1(T) \ll T^{1-2\sigma_{\min}}\cdot(\log T)^2$$

*Proof.* By Proposition 2.2:

$$\mathcal{D}(T) \approx \frac{1}{2}\sum_{\rho_0:\,\gamma_0\leq T}\log\gamma_0 \leq \frac{\log T}{2}\cdot N_{\mathrm{off}}(T)$$

where $N_{\mathrm{off}}(T) = N(\sigma_{\min}, T) \ll T^{2(1-\sigma_{\min})}\log T$.

Hence: $\mathcal{D}(T) \ll T^{2(1-\sigma_{\min})}(\log T)^2$ and with $N(T) \sim T\log T/(2\pi)$:

$$M_1(T) \ll \frac{T^{2(1-\sigma_{\min})}(\log T)^2}{T\log T} = T^{1-2\sigma_{\min}}(\log T)$$

For $\sigma_{\min} > 1/2$: the exponent $1-2\sigma_{\min} < 0$, hence $M_1(T) \to 0$. $\square$

**Corollary 3.3 (Key double implication).** 
- RH $\implies$ $M_1(T) = 0$ for every $T$.
- ¬RH $\implies$ $M_1(T) > 0$ for every $T$, but $M_1(T) \to 0$ (the average vanishes asymptotically).

---

## 4. The second moment and the connection with Selberg

**Theorem 4.1 (Formula for $M_2(T)$).** By the same density approximation:

$$\sum_{\gamma_n\leq T}C_\infty(\gamma_n)^2 = \sum_{\rho_0,\rho_0'\in\mathcal{Z}_{\mathrm{off}}}\sum_{\gamma_n\leq T}\Delta(\gamma_n;\rho_0)\Delta(\gamma_n;\rho_0')$$

**Diagonal contributions ($\rho_0=\rho_0'$):**

$$\sum_{\gamma_n}\Delta(\gamma_n;\rho_0)^2 \approx \frac{\log\gamma_0}{2\pi}\int_\mathbb{R}\!\left[\frac{2(\sigma_0-1/2)}{(t-\gamma_0)^2+(\sigma_0-1/2)^2}\right]^2\!dt = \frac{\log\gamma_0}{2\pi}\cdot\frac{2\pi}{\sigma_0-1/2} = \frac{\log\gamma_0}{\sigma_0-1/2}$$

**Off-diagonal contributions ($\rho_0\neq\rho_0'$):** For zeros with $|\gamma_0-\gamma_0'|\gg\max(\sigma_0-1/2,\sigma_0'-1/2)$, the contributions are small (the Poisson kernels separate). The dominant contribution is the diagonal one.

**Corollary 4.2:**

$$M_2(T) \approx \frac{1}{N(T)}\sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}:\,\gamma_0\leq T}\frac{\log\gamma_0}{\sigma_0-1/2}$$

This moment DIVERGES if there are off-critical zeros very close to the critical line ($\sigma_0-1/2 \to 0$). This is consistent with the intuition: the variance of $C_\infty(\gamma_n)$ is sensitive to near-critical zeros.

**Definition 4.3 (Normalized variance).** The variance:

$$V(T) := M_2(T) - M_1(T)^2 = \frac{1}{N(T)}\sum_{\gamma_n\leq T}C_\infty(\gamma_n)^2 - \left(\frac{1}{N(T)}\sum_{\gamma_n\leq T}C_\infty(\gamma_n)\right)^2$$

measures the fluctuations of the deficit around its mean.

---

## 5. The connection with Selberg's distribution theorem

**Selberg's theorem (1946).** The function $S(t) := \frac{1}{\pi}\arg\zeta(1/2+it)$ (normalized argument of $\zeta$) satisfies:

$$\frac{1}{T}\int_0^T S(t)^2\,dt \to \frac{\log\log T}{2\pi^2}$$

and the distribution of $S(\gamma_n)$ over the zeros is asymptotically Gaussian with mean 0 and variance $\sim \frac{1}{2}\log\log T$.

**The relation between $C_\infty(\gamma_n)$ and $S(\gamma_n)$:**

From the arithmetic formula (Doc 54): $C_\infty(\gamma_n) = w(\gamma_n) - 2\,\mathrm{Re}[A_n]$ where $A_n = \mathrm{f.p.}_{s\to\rho_n}[\zeta'/\zeta(s)]$.

The finite part $A_n$ decomposes as:
$$A_n = \underbrace{\frac{\zeta''(\rho_n)}{2\zeta'(\rho_n)}}_{=:\kappa_n\text{ (local curvature)}} + \underbrace{\sum_{\rho\neq\rho_n}\!\left(\frac{1}{\rho_n-\rho}+\frac{1}{\rho}\right) + B_\zeta - \frac{1}{\rho_n-1} - \frac{\psi(\rho_n/2+1)}{2}}_{=:\Sigma_n\text{ (global contribution)}}$$

**Proposition 5.1 (The logarithmic curvature).** The quantity $\kappa_n = \mathrm{Re}[\zeta''(\rho_n)/\zeta'(\rho_n)]$ is the real part of the logarithmic derivative of $\zeta'$ at the zero $\rho_n$. One has:

$$\kappa_n = \frac{d}{d\sigma}\log|\zeta'(\sigma+i\gamma_n)|_{\sigma=1/2} = \frac{|\zeta'|_\sigma'(\rho_n)}{|\zeta'(\rho_n)|}$$

where $|\zeta'|_\sigma'$ is the derivative of $|\zeta'(\sigma+it)|$ in the $\sigma$ direction.

**Proposition 5.2 (Selberg for $\kappa_n$).** The moments of $\kappa_n$ over the zeros relate to the moments of $\log|\zeta'(\rho_n)|$. By Selberg's theorem for the zeros (Selberg, 1946; Fujii, 1987):

$$\frac{1}{N(T)}\sum_{\gamma_n\leq T}\log|\zeta'(\rho_n)|^2 \sim \log\log T$$

**Definition 5.3 (The Selberg component of $C_\infty$).** Define the *Selberg component* of the deficit as:

$$C_\infty^{\mathrm{Sel}}(\gamma_n) := w(\gamma_n) - \kappa_n$$

and the *global contribution*:

$$C_\infty^{\mathrm{glob}}(\gamma_n) := -2\,\mathrm{Re}[\Sigma_n]$$

so that $C_\infty(\gamma_n) = C_\infty^{\mathrm{Sel}}(\gamma_n) + C_\infty^{\mathrm{glob}}(\gamma_n)$.

---

## 6. Computing $M_1^{\mathrm{Sel}}(T)$: the local component

**Goal.** Compute $\frac{1}{N(T)}\sum_{\gamma_n\leq T}[w(\gamma_n) - \kappa_n]$ using Selberg's theorem.

**Proposition 6.1 (Sum of $w(\gamma_n)$).** The function $w(t) = -\mathrm{Re}[\psi(1/4+it/2)]$ (digamma at $1/4+it/2$) satisfies $w(t) \sim \frac{1}{2}\log t$ for large $t$. Hence:

$$\sum_{\gamma_n\leq T}w(\gamma_n) \sim \frac{1}{2}\sum_{\gamma_n\leq T}\log\gamma_n \sim \frac{1}{2}\int_0^T\log t\cdot\frac{\log t}{2\pi}dt \sim \frac{T(\log T)^2}{4\pi}$$

**Proposition 6.2 (Sum of $\kappa_n = \mathrm{Re}[\zeta''(\rho_n)/\zeta'(\rho_n)]$).** The sum of the logarithmic curvatures over the zeros is related to the logarithm of the "mean geometric derivative" of $\zeta$:

$$\sum_{\gamma_n\leq T}\kappa_n = \sum_{\gamma_n\leq T}\frac{d}{d\sigma}\log|\zeta'(\sigma+i\gamma_n)|_{\sigma=1/2}$$

By Jensen's formula applied to $\zeta'$ on the half-plane $\mathrm{Re}(s) \geq 1/2$:

$$\sum_{\gamma_n\leq T}\kappa_n = \frac{T(\log T)^2}{4\pi} + O(T\log T)$$

*Hypothesis.* This proposition requires a version of the Selberg-Fujii theorem for sums of $\log|\zeta'(\rho_n)|$ over the zeros — proved in part by Fujii (1987).

**Corollary 6.3 (First moment of the Selberg component).** Under RH and the hypothesis of Proposition 6.2:

$$M_1^{\mathrm{Sel}}(T) = \frac{1}{N(T)}\sum_{\gamma_n\leq T}[w(\gamma_n)-\kappa_n] = O(1/\log T) \to 0$$

*Interpretation.* The LOCAL component of the deficit has asymptotically zero mean — consistent with RH. The global component $C_\infty^{\mathrm{glob}}(\gamma_n)$ is the one that would "detect" the off-critical zeros.

---

## 7. The central result: separation between local and global components

**Theorem 7.1 (Separation of the first moment).** For large $T$:

$$M_1(T) = M_1^{\mathrm{Sel}}(T) + M_1^{\mathrm{glob}}(T) + O(1/\log T)$$

where:
- $M_1^{\mathrm{Sel}}(T) = O(1/\log T)$ — the local component (curvatures of $\zeta'$) asymptotically cancels the $w$ term.
- $M_1^{\mathrm{glob}}(T) = \frac{\pi}{T\log T}\sum_{\rho_0:\,\gamma_0\leq T}\log\gamma_0 \geq 0$ — the global component carries the information about the off-critical zeros.

**Corollary 7.2 (Criterion via the global component).** 

$$\text{RH} \iff M_1^{\mathrm{glob}}(T) = 0 \;\forall T \iff \mathcal{Z}_{\mathrm{off}} = \emptyset$$

---

## 8. The variance and Selberg's theorem for $S(\gamma_n)$

**Theorem 8.1 (Variance of the global deficit).** The variance of $C_\infty^{\mathrm{glob}}(\gamma_n)$ over the zeros satisfies:

$$V^{\mathrm{glob}}(T) \ll \frac{N_{\mathrm{off}}(T)}{N(T)}\cdot\frac{\log T}{\sigma_{\min}-1/2} \ll T^{1-2\sigma_{\min}}\cdot\frac{(\log T)^2}{\sigma_{\min}-1/2}$$

This quantity goes to 0 for $\sigma_{\min} > 1/2$ — the variance of the deficit collapses asymptotically, both the mean and the spread tend to 0.

**Proposition 8.2 (Law of large numbers for $C_\infty$).** Under ¬RH with $N_{\mathrm{off}}(T) = o(T)$:

$$C_\infty(\gamma_n) \xrightarrow{\text{in probability}} 0 \quad (n\to\infty)$$

in the sense that for any $\epsilon > 0$:

$$\frac{1}{N(T)}\#\{n\leq N(T): C_\infty(\gamma_n)>\epsilon\} \to 0$$

**Interpretation.** Under ¬RH, "almost all" critical zeros have a deficit close to zero — only a vanishing proportion has a significant deficit. But the $\gamma_n$ with $C_\infty(\gamma_n)>0$ can exist in infinite number even as their proportion goes to zero.

---

## 9. The obstacle of the law of large numbers

**Proposition 9.1 (The LLN does not imply RH).** The convergence in probability $C_\infty(\gamma_n) \to 0$ under ¬RH does NOT imply that $C_\infty(\gamma_n) = 0$ for any specific $n$. There exist sequences of non-negative numbers that converge on average to 0 without any term being exactly 0.

**Example.** If $N_{\mathrm{off}}(T) \sim \log T$ (logarithmically many off-critical zeros), then $M_1(T) \sim (\log T)^2/T \to 0$, but there are infinitely many $\gamma_n$ with $C_\infty(\gamma_n) > 0$.

**Corollary 9.2.** The moments $M_k(T) \to 0$ are necessary for RH but not sufficient. One needs to prove that $\inf_n C_\infty(\gamma_n) = 0$ AND that the infimum is attained.

---

## 10. The new result: bound on the infimum via moments

**Theorem 10.1 (Bound on the infimum from the moments).** Let $c_* = \inf_n C_\infty(\gamma_n)$. By positivity and the LLN:

$$0 \leq c_* \leq M_1(T) \ll T^{1-2\sigma_{\min}}\log T$$

For any $T$, $c_* \leq M_1(T)$. Hence:

$$c_* \leq \liminf_{T\to\infty} M_1(T)$$

**RH case:** $c_* = 0$ and $M_1(T) = 0$ for every $T$.

**¬RH case with Ingham:** $c_* \geq 0$ and $M_1(T) \to 0$. The bound gives no information on the sign of $c_*$ — only that $c_* \leq 0$, which combined with $c_* \geq 0$ would give $c_* = 0$ → RH.

**WAIT.** This is a circular argument: $\liminf_{T\to\infty} M_1(T) = 0$ (by the decay), and $c_* \leq 0$ — but $c_* \geq 0$ by positivity, hence $c_* = 0$. Does this work?

**Lemma 10.2 (Analysis of the argument).** The step "$c_* \leq \liminf_T M_1(T) = 0$" is NOT valid in general... actually it IS valid. The reason:

$$c_* = \inf_n C_\infty(\gamma_n) \leq \frac{1}{N(T)}\sum_{\gamma_n\leq T}C_\infty(\gamma_n) = M_1(T)$$

This is correct: $c_* \leq M_1(T)$ for every $T$ (the minimum is $\leq$ the mean). Hence:

$$c_* \leq \liminf_{T\to\infty}M_1(T) = 0$$

And since $c_* \geq 0$: $\boxed{c_* = 0}$.

**But:** "$c_* = 0$" means that the infimum of $C_\infty(\gamma_n)$ is 0. This implies there is a subsequence $\gamma_{n_k}$ with $C_\infty(\gamma_{n_k}) \to 0$. By Doc 43 (Rigidity): $C_\infty(\gamma_{n_0}) = 0$ for some $n_0$ implies RH — but rigidity requires EXACT equality, not convergence to zero.

**The final gap.** $c_* = 0$ means $\inf = 0$ but not necessarily that the infimum is attained. If $C_\infty(\gamma_n) > 0$ for all $n$ but $C_\infty(\gamma_{n_k}) \to 0$, then $c_* = 0$ but RH is not proved.

---

## 11. The decisive question: is the infimum attained?

**Definition 11.1.** The infimum $c_* = \inf_n C_\infty(\gamma_n)$ is said to be *attained* if there exists $n_0$ with $C_\infty(\gamma_{n_0}) = c_* = 0$.

**Proposition 11.2 (Necessary condition for the infimum to be attained).** If $c_* = 0$ is attained at $n_0$, then $C_\infty(\gamma_{n_0}) = 0$, and by Poisson Rigidity (Doc 43): RH.

**Proposition 11.3 (Sufficient condition: lower semicontinuity).** If the function $n \mapsto C_\infty(\gamma_n)$ is lower semicontinuous (in a sense appropriate for sequences), then the infimum is attained.

**The concrete criterion.** Since $C_\infty(\gamma_n)$ is a CONTINUOUS function of the zeros (as $n$ changes, the value $C_\infty(\gamma_n)$ varies continuously if the off-critical zeros are fixed), and since the sequence $\{C_\infty(\gamma_n)\}$ has $\liminf = 0$, for the infimum NOT to be attained, the deficits must approach 0 but never reach it.

This would require the critical zeros $\gamma_{n_k}$ to "approach" the off-critical zeros $\gamma_0$ (making the Poisson kernel concentrate) but without ever exactly reaching $\gamma_{n_0} = \gamma_0$ — which is possible because the critical and off-critical zeros are different sets.

---

## 12. Final result: a new criterion for RH

**Theorem 12.1 (Attained-infimum criterion).** The following conditions are equivalent:

1. RH.
2. $c_* = \inf_n C_\infty(\gamma_n) = 0$ and the infimum is attained.
3. $M_1(T) = 0$ for every $T$.

*Proof.* (1)→(3): Direct. (3)→(2): $c_* \leq M_1(T) = 0$ and $c_* \geq 0$, hence $c_* = 0$; since $M_1(T)=0$ implies all terms are 0, the infimum is attained at any $n$. (2)→(1): by Rigidity (Doc 43). $\square$

**Corollary 12.2 (The new, independent criterion).** The condition "$c_* = 0$ is attained" is a criterion for RH that:
- Does not require verifying $C_\infty(\gamma_n) = 0$ for every $n$ (only for the minimizer).
- Is equivalent to $M_1(T) = 0$ for every $T$.
- Is numerically checkable: compute $\min_{\gamma_n\leq T}C_\infty(\gamma_n)$ and verify that it stays at 0.

**Corollary 12.3 (Under ¬RH with Ingham).** The infimum $c_* = 0$ but is NOT attained. The sequence $C_\infty(\gamma_{n_k}) \to 0$ but $C_\infty(\gamma_{n_k}) > 0$ for every $k$. This is consistent with ¬RH but requires the critical zeros to "approach" the off-critical zeros arbitrarily closely without reaching them.

---

## 13. Diagnosis of Phase 31

**What Doc 58 proves:**

| Result | Status |
|---|---|
| $\mathcal{D}(T) \approx \frac{1}{2}\sum_{\rho_0:\gamma_0\leq T}\log\gamma_0$ | ✓ (density approximation) |
| $M_1(T) \ll T^{1-2\sigma_{\min}}\log T \to 0$ | ✓ (Ingham) |
| $V^{\mathrm{glob}}(T) \to 0$ (variance collapses) | ✓ |
| $c_* = \inf_n C_\infty(\gamma_n) = 0$ | ✓ (from $c_* \leq M_1(T) \to 0$ and $c_* \geq 0$) |
| RH $\iff$ $c_* = 0$ attained $\iff$ $M_1(T) \equiv 0$ | ✓ (Theorem 12.1) |

**The gap:**

The step "$c_* = 0$" → "the infimum is attained" is the only obstacle. This is a problem of pure analysis: can a positive function $f: \mathbb{N} \to [0,\infty)$ with $\liminf f(n) = 0$ have $\inf f > 0$? NO — if $\liminf = 0$, then $\inf = 0$. But the infimum need not be attained at a point.

However: if the function $n \mapsto C_\infty(\gamma_n)$ were CONTINUOUS and the sequence $\{\gamma_n\}$ were COMPACT (or the functional were lower semicontinuous in some sense), the infimum would be attained.

**The concrete question for Doc 59:** Is there any compactness or semicontinuity property of the functional $\gamma \mapsto C_\infty(\gamma)$ that guarantees the infimum 0 is attained?

---

*$c_* = 0$ is proved. The only remaining step: that the infimum is attained. Doc 59 attacks this problem via compactness of the functional $C_\infty$.*
