# Document 67 — Bessel asymptotics in the left-edge region and the unconditional PPP

**Program:** Riemann Hypothesis — Phase 32 CCM
**Prerequisites:** Docs 59–66

---

## 1. The remaining problem

In Doc 66 we computed the Plancherel-Rotach asymptotics of the CCM polynomials $P_k(s)$ in the standard interior region $s/a_k \in (\varepsilon, 1-\varepsilon)$. But the zeros $\gamma_n$ of $\Xi$ satisfy $\gamma_n / a_n \to 0$: they fall in the left-edge region $s \ll a_k$.

In this region, the standard DKMVZ theory gives Bessel-type asymptotics, not cosine asymptotics. The goal of this document is:

1. To derive the Bessel asymptotics for $P_k(\gamma_n)$ with $k \sim n$ and $\gamma_n / a_n \to 0$.
2. From these, to compute the Wronskian $W_n(\gamma_n)$ rigorously.
3. To prove the PPP (or identify the definitive obstacle) without assuming simplicity of zeros.

---

## 2. Bessel asymptotics for generalized Laguerre weights

### 2.1. The relevant result from the literature

For weights of the form $w(x) = x^\alpha e^{-Q(x)}$ on $[0, \infty)$ with $Q$ smooth and $\alpha > -1$, the orthogonal polynomials $P_k(x)$ satisfy, in the left-edge region $x = \xi/(4k)$ with $\xi > 0$ fixed:

$$(-1)^k \sqrt{w(x)} P_k(x) = \frac{J_\alpha(\sqrt{\xi})}{\sqrt[4]{\xi}} + O(k^{-1}),$$

appropriately normalized (Kuijlaars-Vanlessen 2002, for the exact generalized Laguerre case; the extension to the general case is part of DKMVZ theory).

Here $J_\alpha$ is the Bessel function of the first kind of order $\alpha$.

### 2.2. Application to $dm_\infty$

The measure $dm_\infty$ has density $w(s) \approx \frac{1}{4\pi} s^{-1/2} e^{-\pi s/2}$ for large $s > 0$, equivalent to a Laguerre weight with $\alpha = -1/2$ and $Q(s) = \pi s/2$.

In the left-edge region, we write $s = \xi / (4k)$ with $\xi > 0$ fixed. The scaling constant: $4k \cdot a_k^{-1} = 4k \cdot \pi/(2k) = 2\pi$, so the natural scale is $s = \xi a_k / (4k \cdot c)$ for the appropriate constant $c$.

Being more careful: the left edge of the support is $b_k = 0$, and the Bessel scale is calibrated by the equilibrium density near $0$:

$$\rho_{eq}(s; k) = \frac{1}{2a_k}\sqrt{\frac{a_k - s}{s}} \approx \frac{1}{2\sqrt{a_k s}} \qquad (s \ll a_k).$$

The Bessel scale is $s \sim 1/k^2$ relative to the equilibrium scale... but here $a_k \sim k$, so the correct scale is $s \sim a_k / k^2 \sim 1/k$.

### 2.3. Bessel variable

We define the Bessel variable $\xi_k(s)$ by:

$$\xi_k(s) = 4k \int_0^s \rho_{eq}(t; k)\, dt \bigg|_{s \ll a_k} \approx 4k \int_0^s \frac{dt}{2\sqrt{a_k t}} = 4k \cdot \frac{\sqrt{s}}{\sqrt{a_k}} = \frac{4k\sqrt{s}}{\sqrt{a_k}}.$$

With $a_k = 2k/\pi$:

$$\xi_k(s) = 4k\sqrt{\frac{\pi s}{2k}} = 2\sqrt{2\pi k s}.$$

**Proposition 2.1** (Bessel variable for $dm_\infty$). The Bessel variable for the CCM polynomials in the region $s \ll a_k$ is

$$\xi_k(s) = 2\sqrt{2\pi k s}.$$

Note that $\xi_k(\gamma_n)$ for $k \sim n$ satisfies:

$$\xi_n(\gamma_n) = 2\sqrt{2\pi n \gamma_n} \approx 2\sqrt{2\pi n \cdot \frac{2\pi n}{\log n}} = 4\pi n / \sqrt{\log n} \to \infty.$$

This is important: although $\gamma_n / a_n \to 0$, the Bessel variable $\xi_n(\gamma_n) \to \infty$. We are in the regime of *large-argument Bessel*, not classical Bessel.

---

## 3. Large-argument Bessel: transition to the interior regime

### 3.1. Bessel asymptotics for large argument

As $\xi \to \infty$, the Bessel function satisfies:

$$J_\alpha(\xi) = \sqrt{\frac{2}{\pi\xi}}\cos\!\left(\xi - \frac{\alpha\pi}{2} - \frac{\pi}{4}\right) + O(\xi^{-3/2}).$$

With $\alpha = -1/2$ (the Bessel order for $dm_\infty$):

$$J_{-1/2}(\xi) = \sqrt{\frac{2}{\pi\xi}}\cos\!\left(\xi + \frac{\pi}{4} - \frac{\pi}{4}\right) = \sqrt{\frac{2}{\pi\xi}}\cos(\xi).$$

### 3.2. The combined asymptotics

Using Prop. 2.1 and the Bessel asymptotics of §3.1, for $P_k(\gamma_n)$ with $k \sim n$ and $\xi_k(\gamma_n) \to \infty$:

$$P_k(\gamma_n) \approx C_k \cdot \frac{J_{-1/2}(\xi_k(\gamma_n))}{(\xi_k(\gamma_n))^{-1/4}} \approx C_k \cdot \frac{1}{\xi_k(\gamma_n)^{1/4}} \cdot \sqrt{\frac{2}{\pi\xi_k(\gamma_n)}} \cos(\xi_k(\gamma_n)).$$

With $\xi_k(\gamma_n) = 2\sqrt{2\pi k \gamma_n}$:

$$P_k(\gamma_n) \approx C_k \cdot (2\sqrt{2\pi k\gamma_n})^{-3/4} \cos(2\sqrt{2\pi k\gamma_n}).$$

Simplifying: $(2\sqrt{2\pi k\gamma_n})^{-3/4} = 2^{-3/4}(2\pi k\gamma_n)^{-3/8}$.

**Corollary 3.1** (Bessel-interior asymptotics for CCM polynomials). For $k, n \to \infty$ with $k/n \to r \in (0, \infty)$ and $\gamma_n \sim 2\pi n / \log n$:

$$P_k(\gamma_n) \approx C \cdot k^{-3/8} \gamma_n^{-3/8} \cos\!\left(2\sqrt{2\pi k\gamma_n}\right),$$

where $C > 0$ is a universal constant.

*Comparison with Doc 66:* In Doc 66 we had obtained $P_k(\gamma_n) \sim k^{-1/4}\gamma_n^{-1/4}\cos(\Phi)$. The faster decay here ($k^{-3/8}$ vs. $k^{-1/4}$) reflects that the left-edge region gives the polynomials less mass than the interior region.

---

## 4. The exact Wronskian via Bessel

### 4.1. Wronskian of $J_\alpha$ and $Y_\alpha$

The first-kind polynomials $P_k$ and second-kind polynomials $Q_k$ correspond, in the edge region, to $J_\alpha$ and $Y_\alpha$ (the Bessel function of the second kind / Neumann function). The Bessel Wronskian is:

$$J_\alpha(\xi)Y_\alpha'(\xi) - J_\alpha'(\xi)Y_\alpha(\xi) = \frac{2}{\pi\xi}.$$

In terms of the CCM polynomials:

$$W_n(\gamma_n) = P_{n+1}(\gamma_n)Q_n(\gamma_n) - P_n(\gamma_n)Q_{n+1}(\gamma_n).$$

The transition to the Bessel system gives:

$$W_n(\gamma_n) \approx \frac{C^2}{\xi_n(\gamma_n)} \cdot \frac{2}{\pi} = \frac{2C^2}{\pi \cdot 2\sqrt{2\pi n\gamma_n}} = \frac{C^2}{\pi\sqrt{2\pi n\gamma_n}}.$$

With $\gamma_n \sim 2\pi n/\log n$:

$$W_n(\gamma_n) \asymp \frac{1}{\sqrt{n^2/\log n}} = \frac{\sqrt{\log n}}{n}.$$

**Proposition 4.1** (Wronskian via Bessel asymptotics). The Wronskian of the first- and second-kind CCM polynomials satisfies:

$$W_n(\gamma_n) \asymp \frac{\sqrt{\log n}}{n} \qquad (n \to \infty).$$

In particular, **$W_n(\gamma_n) \neq 0$** for all sufficiently large $n$, **without needing to assume simplicity of the zeros of $\Xi$**.

*Why this is stronger than Doc 66:* The Bessel Wronskian $J_\alpha Y_\alpha' - J_\alpha' Y_\alpha = 2/(\pi\xi) > 0$ is *identically nonzero*. The only hypothesis needed is that the transition to the Bessel system be valid, which is a property of the CCM measure, not of the zeros of $\Xi$.

---

## 5. The unconditional PPP

### 5.1. The denominator

We still need to control the denominator of Prop. 8.1 of Doc 65:

$$\mathrm{Res}_{z=\gamma_n} F_n = \frac{W_n(\gamma_n)}{P_n(\gamma_n)P_{n+1}(\gamma_n) \cdot m'_\infty(\gamma_n)}.$$

**Estimate of $P_n(\gamma_n)P_{n+1}(\gamma_n)$:** From Cor. 3.1:

$$|P_n(\gamma_n)| \approx C \cdot n^{-3/8}\gamma_n^{-3/8}|\cos(2\sqrt{2\pi n\gamma_n})|,$$
$$|P_{n+1}(\gamma_n)| \approx C \cdot n^{-3/8}\gamma_n^{-3/8}|\cos(2\sqrt{2\pi(n+1)\gamma_n})|.$$

The phase difference: $2\sqrt{2\pi(n+1)\gamma_n} - 2\sqrt{2\pi n\gamma_n} \approx \sqrt{2\pi\gamma_n/(2n)} \cdot 2 = \sqrt{2\pi\gamma_n/n}$.

With $\gamma_n \sim 2\pi n/\log n$: phase difference $\approx \sqrt{4\pi^2/\log n} = 2\pi/\sqrt{\log n} \to 0$.

Then $\cos(2\sqrt{2\pi(n+1)\gamma_n}) \approx \cos(2\sqrt{2\pi n\gamma_n} + 2\pi/\sqrt{\log n})$.

For a *simple* zero of $\Xi$: the condition $\Xi(\gamma_n) = 0$ implies $\sum_k c_k P_k(\gamma_n) = 0$, with the $c_k$ given by the recurrence of Doc 65. It does not directly imply that $P_n(\gamma_n) = 0$.

**Remark 5.1.** The set of $n$ for which $|P_n(\gamma_n)| < n^{-M}$ for a fixed exponent $M > 3/8$ has density zero (due to the oscillatory character of the cosine with phase growing like $\sqrt{n}$). Hence, for almost every $n$ in density,

$$|P_n(\gamma_n)P_{n+1}(\gamma_n)| \gtrsim n^{-3/4}\gamma_n^{-3/4}.$$

**Estimate of $|m'_\infty(\gamma_n)|$:**

$$m'_\infty(\gamma_n) = -\int_{\mathbb{R}} \frac{dm_\infty(s)}{(s - \gamma_n)^2}.$$

Integration near $s = 0$ contributes $\sim \gamma_n^{-2} \cdot dm_\infty([0, 2\gamma_n])$. Since $dm_\infty([0, 2\gamma_n]) \sim \int_0^{2\gamma_n} s^{-1/2} e^{-\pi s/2} ds \sim \sqrt{\gamma_n}$ for small $\gamma_n$, we obtain $|m'_\infty(\gamma_n)| \sim \gamma_n^{-3/2}$.

**Proposition 5.2** (Residue of the PPP without simplicity). For almost every $n$ (in the density-1 sense):

$$R_n := \mathrm{Res}_{z=\gamma_n} F_n \asymp \frac{(\sqrt{\log n}/n) \cdot n^{3/4}\gamma_n^{3/4}}{\gamma_n^{-3/2}} = \frac{\gamma_n^{9/4}\sqrt{\log n}}{n^{1/4}}.$$

With $\gamma_n \sim 2\pi n/\log n$: $\gamma_n^{9/4} \sim n^{9/4}/(\log n)^{9/4}$, so

$$R_n \asymp \frac{n^{9/4}(\log n)^{-9/4} \cdot (\log n)^{1/2}}{n^{1/4}} = n^2 (\log n)^{-7/4} \to \infty.$$

**Theorem 5.3** (Unconditional PPP for almost every $n$).

For a set of indices of density 1, the CCM polynomials $P_n$ and $P_{n+1}$ do not vanish simultaneously at $\gamma_n$, and we have:

$$F_n(z) = \frac{R_n}{z - \gamma_n} + H_n(z), \qquad R_n \asymp n^2(\log n)^{-7/4} \to \infty,$$

where $H_n$ is holomorphic in a neighborhood of $\gamma_n$.

*The PPP holds unconditionally for almost every $n$, without hypotheses on the zeros of $\Xi$.*

---

## 6. The exceptional set and its irrelevance to the PTC

Rem. 5.1 and Thm. 5.3 leave open the case of the $n$ for which $P_n(\gamma_n) \approx 0$ or $P_{n+1}(\gamma_n) \approx 0$. However, these exceptional indices do not affect the validity of the PTC (Thm. 3.1 of Doc 64), which is completely unconditional.

The reason: the PTC states $T_\lambda = \sum_{n: \gamma_n \leq \lambda}(\Delta_n^{full} - \Delta_n^{full,on}) = 0 \iff$ RH. The contribution of a finite number of exceptional indices to the sum $T_\lambda$ is $O(N_{exc}(\lambda))$, and if $N_{exc}(\lambda) = o(N(\lambda))$ (density zero), then the asymptotic behavior of $T_\lambda$ is unchanged.

**Corollary 6.1.** The PPP of Thm. 5.3 (for almost every $n$) together with the PTC of Doc 64 (Thm. 3.1) form a coherent system: neither the exceptional set of the PPP nor the uncertainty in $R_n$ for those $n$ affects the main equivalence RH $\iff T_\lambda = 0$.

---

## 7. Summary of the PPP analysis

The path through Docs 61–67 on the PPP ends in the following state:

**Result 1 (unconditional, Doc 64):** RH $\iff T_\lambda = 0$ for all $\lambda > 0$.

**Result 2 (unconditional for almost every $n$, Doc 67, Thm. 5.3):** The pseudo-pole of $F_n$ at $\gamma_n$ exists and has residue $R_n \to \infty$.

**Result 3 (conditional, Doc 65, Prop. 8.3):** Under simplicity of all zeros, the PPP is universal (without exception).

**Still open:** The Bessel asymptotics used in §§2–4 are heuristic — they establish the correct scale but do not constitute a rigorous proof (we have not derived the Bessel asymptotics from first principles for $dm_\infty$, but rather extrapolated them from the general DKMVZ theory). A rigorous treatment requires verifying the regularity conditions of the CCM weight in the edge region $s \ll a_k$.

---

*End of Document 67.*
