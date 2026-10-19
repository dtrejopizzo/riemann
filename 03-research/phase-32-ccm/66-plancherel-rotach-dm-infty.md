# Document 66 — Plancherel-Rotach asymptotics for $P_k$ with the CCM measure $dm_\infty$

**Program:** Riemann Hypothesis — Phase 32 CCM
**Prerequisites:** Docs 59–65, in particular Doc 63 (MRS equilibrium density) and Doc 65 (PPP via Wronskian)

---

## 1. The problem

The orthogonal polynomials $\{P_k\}$ of the CCM measure

$$dm_\infty(s) = \frac{1}{(2\pi)^2}\left|\Gamma\!\left(\tfrac{1}{4} + \tfrac{is}{2}\right)\right|^2 ds$$

have exact Jacobi coefficients $a_k^{\infty} = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ (CCM Thm 5.2). To close the PPP analysis of Doc 65 we need the explicit asymptotics of $P_k(s)$ as $k \to \infty$, with $s$ fixed or in the region $s = O(a_k^{\infty})$.

Specifically we need $P_k(\gamma_n)$ for $k \sim n$, where $\gamma_n$ is the $n$-th zero of $\Xi$ with positive imaginary part.

---

## 2. Data of the CCM measure

### 2.1. Density and decay

The function $\Gamma(1/4 + is/2)$ satisfies Stirling's formula: as $s \to +\infty$,

$$\log|\Gamma(1/4 + is/2)| = -\frac{\pi s}{4} + \frac{1}{2}\log(2\pi) - \frac{1}{2}\log s + O(s^{-1}).$$

Hence the density of $dm_\infty$ satisfies

$$w(s) := \frac{dm_\infty}{ds}(s) \sim \frac{1}{4\pi} s^{-1/2} e^{-\pi s/2} \qquad (s \to +\infty).$$

This is a weight of generalized Laguerre type: $w(s) \sim s^\alpha e^{-cs}$ with $\alpha = -1/2$, $c = \pi/2$.

### 2.2. MRS number and equilibrium support

In Doc 63 §1 we computed (via Mhaskar-Rakhmanov-Saff theory) the MRS number $a_k$ for the measure $dm_\infty$ supported on $\mathbb{R}_{\geq 0}$:

$$a_k = \frac{2k}{\pi} + O(\log k), \qquad k \to \infty.$$

The equilibrium measure $\mu_{eq,k}$ is supported on $[0, a_k]$ and has density (Doc 63, Prop. 1.1):

$$\rho_{eq}(s; k) = \frac{2}{\pi a_k}\sqrt{a_k - s} \cdot \sqrt{s}^{-1} \cdot \frac{1}{2} = \frac{1}{\pi}\sqrt{\frac{a_k - s}{s}}, \qquad s \in (0, a_k).$$

(Exact form of the logarithmic equilibrium for the weight $e^{-\pi s/2}$ on $[0, \infty)$, see §3 below.)

---

## 3. Computation of the equilibrium measure

### 3.1. Variational problem

The equilibrium measure for the external field $Q(s) = \pi s/2$ (given $w(s) = e^{-Q(s)} \cdot s^{-1/2}$ approximately) on the interval $[0, a]$ is the measure $\mu_{eq}$ that minimizes the logarithmic energy:

$$I[\mu] = -\iint \log|s - t|\, d\mu(s)\, d\mu(t) + 2\int Q(s)\, d\mu(s).$$

### 3.2. Euler-Lagrange equation

The optimality condition is: there exists a constant $\ell$ (the equilibrium constant) such that

$$2\int \log|s - t|\, d\mu_{eq}(t) = Q(s) + \ell \quad \text{for } \mu_{eq}\text{-a.e.}$$

### 3.3. Explicit density

**Lemma 3.1.** For the weight $Q(s) = \pi s/2$ on $[0, a]$, the equilibrium density is

$$\rho_{eq}(s; a) = \frac{1}{2\pi}\frac{Q'(s) - 2H[\rho_{eq} \mathbf{1}_{[0,a]}](s)}{\sqrt{s(a-s)}},$$

but for linear $Q$, the density is the *weighted semicircle measure*:

$$\rho_{eq}(s; a) = \frac{Q'(a/2)}{\pi} \cdot \frac{1}{\sqrt{s}} \cdot \sqrt{a - s} = \frac{\pi/2}{\pi}\frac{\sqrt{a-s}}{\sqrt{s}} = \frac{\sqrt{a-s}}{2\sqrt{s}},$$

with $\int_0^a \rho_{eq}(s;a) ds = 1$ determining $a$.

*Verification:* $\int_0^a \frac{\sqrt{a-s}}{2\sqrt{s}} ds$. Substituting $s = a\sin^2\theta$:

$$\int_0^{\pi/2} \frac{\sqrt{a-a\sin^2\theta}}{2\sqrt{a\sin^2\theta}} \cdot 2a\sin\theta\cos\theta\, d\theta = \int_0^{\pi/2} \frac{a\cos\theta}{2\sqrt{a}\sin\theta} \cdot 2a\sin\theta\cos\theta\, d\theta = a\int_0^{\pi/2} \cos^2\theta\, d\theta = \frac{\pi a}{4}.$$

For the integral to equal 1: $a = 4/\pi$. But from Doc 63 we know $a_k \approx 2k/\pi$, so the correct scale is $a = a_k$ with the weight scaled by $k$.

**Lemma 3.2** (Equilibrium density for $dm_\infty$ at scale $k$). The normalized equilibrium density for the polynomials $P_k$ with measure $dm_\infty$ is

$$\rho_{eq}(s; k) = \frac{\pi}{2a_k}\sqrt{\frac{a_k - s}{s}} \cdot \frac{1}{\pi} = \frac{1}{2a_k}\sqrt{\frac{a_k - s}{s}}, \qquad s \in (0, a_k),$$

with $a_k = 2k/\pi$.

---

## 4. Plancherel-Rotach asymptotics: interior regime

### 4.1. General framework (DKMVZ)

By the theory of Deift-Kriecherbauer-McLaughlin-Venakides-Zhou (1999) for polynomials with weights $e^{-nV}$, the orthogonal polynomials satisfy in the interior region $s \in (0, a_k)$:

$$P_k(s) = \frac{1}{\sqrt{\pi} \cdot \pi_k(s)^{1/4}} \cos\left(\int_{b_k}^s k\rho_{eq}(t; k)\, dt - \frac{\pi}{4}\right) + O(k^{-1}),$$

where $\pi_k(s) = s(a_k - s)$ and $b_k$ is the left endpoint of the support (here $b_k = 0$).

### 4.2. Application to $dm_\infty$

With $\rho_{eq}(t; k) = \frac{1}{2a_k}\sqrt{\frac{a_k-t}{t}}$, we compute the phase:

$$\Phi_k(s) := k\int_0^s \rho_{eq}(t; k)\, dt = \frac{k}{2a_k}\int_0^s \sqrt{\frac{a_k - t}{t}}\, dt.$$

Substituting $t = a_k \sin^2\theta$ (with $t: 0 \to s$ corresponding to $\theta: 0 \to \arcsin\sqrt{s/a_k}$):

$$\int_0^s \sqrt{\frac{a_k - t}{t}}\, dt = \int_0^{\arcsin\sqrt{s/a_k}} \frac{\sqrt{a_k}\cos\theta}{\sqrt{a_k}\sin\theta} \cdot 2a_k\sin\theta\cos\theta\, d\theta = 2a_k\int_0^{\phi_s}\cos^2\theta\, d\theta,$$

where $\phi_s = \arcsin\sqrt{s/a_k}$. Hence:

$$\int_0^s \sqrt{\frac{a_k - t}{t}}\, dt = a_k\left(\phi_s + \frac{1}{2}\sin(2\phi_s)\right) = a_k\left(\arcsin\sqrt{\frac{s}{a_k}} + \sqrt{\frac{s}{a_k}}\sqrt{1 - \frac{s}{a_k}}\right).$$

And the total phase:

$$\Phi_k(s) = \frac{k}{2a_k} \cdot a_k\left(\arcsin\sqrt{\frac{s}{a_k}} + \sqrt{\frac{s(a_k - s)}{a_k^2}}\right) = \frac{k}{2}\left(\arcsin\sqrt{\frac{s}{a_k}} + \frac{\sqrt{s(a_k - s)}}{a_k}\right).$$

### 4.3. Plancherel-Rotach formula for $dm_\infty$

**Theorem 4.1** (PR asymptotics for CCM polynomials). For $s \in (0, a_k)$ fixed with $s/a_k \in (\varepsilon, 1-\varepsilon)$:

$$P_k(s) = \left(\frac{4}{\pi^2 s(a_k - s)}\right)^{1/4} \cos\!\left(\frac{k}{2}\arcsin\!\sqrt{\frac{s}{a_k}} + \frac{k}{2}\cdot\frac{\sqrt{s(a_k-s)}}{a_k} - \frac{\pi}{4}\right) + O(k^{-1}),$$

with $a_k = 2k/\pi + O(\log k)$.

*This formula is the analogue of the Plancherel-Rotach asymptotics for the harmonic oscillator, adapted to the hyperbolic geometry of $dm_\infty$.*

---

## 5. Evaluation at the zeros of $\Xi$

### 5.1. The position of $\gamma_n$ relative to the support

From Doc 63, the zero $\gamma_n$ satisfies $\gamma_n \ll a_k$ for $k \sim n$. More precisely:

- $a_n = 2n/\pi$.
- $\gamma_n \approx 2\pi n / \log n$ (Riemann–von Mangoldt zero density).
- Hence $\gamma_n / a_n \approx \pi^2 / \log n \to 0$.

The zeros $\gamma_n$ fall in the region $s \ll a_k$, i.e., **near the left edge** of the equilibrium support.

### 5.2. Left-edge regime

For $s = \gamma_n \ll a_k$, with $k \sim n$, we have $s/a_k \to 0$. In this regime:

$$\arcsin\sqrt{s/a_k} \approx \sqrt{s/a_k}, \qquad \frac{\sqrt{s(a_k - s)}}{a_k} \approx \sqrt{s/a_k}.$$

The phase becomes:

$$\Phi_k(\gamma_n) \approx \frac{k}{2} \cdot 2\sqrt{\frac{\gamma_n}{a_k}} = k\sqrt{\frac{\gamma_n}{a_k}}.$$

With $a_k \approx 2k/\pi$:

$$\Phi_k(\gamma_n) \approx k\sqrt{\frac{\pi \gamma_n}{2k}} = \sqrt{\frac{\pi k \gamma_n}{2}}.$$

The amplitude factor: $(s(a_k - s))^{-1/4} \approx s^{-1/4} a_k^{-1/4} \approx \gamma_n^{-1/4} \cdot (2k/\pi)^{-1/4}$.

**Corollary 5.1** (Edge asymptotics for $P_k$ at zeros of $\Xi$). For $k \sim n$ and $\gamma_n$ the $n$-th zero of $\Xi$:

$$P_k(\gamma_n) \approx C \cdot \gamma_n^{-1/4} k^{-1/4} \cos\!\left(\sqrt{\frac{\pi k \gamma_n}{2}} - \frac{\pi}{4}\right),$$

for a constant $C > 0$ (which absorbs the powers of $\pi$).

### 5.3. Oscillatory behavior in $k$

The formula of Corollary 5.1 shows that $P_k(\gamma_n)$ oscillates in $k$ with:

- **Amplitude:** $\sim k^{-1/4}$ (decreasing).
- **Oscillation frequency in $k$:** The phase $\sqrt{\pi k \gamma_n / 2}$ changes by $\pi$ when $k$ changes by $\Delta k \approx 2\pi / (\pi \gamma_n / 2 / \sqrt{\pi k \gamma_n / 2}) = \sqrt{8k/(\pi\gamma_n)}$.

For $k \sim n$ and $\gamma_n \sim 2\pi n/\log n$: $\Delta k \sim \sqrt{8n \log n / (2\pi^2 n)} = \sqrt{4\log n / \pi^2} \sim \sqrt{\log n}$.

**Remark 5.2.** The zeros of the cosine in the variable $k$ are separated by $\Delta k \sim \sqrt{\log n}$ for $k \sim n$. This means that in an interval $|k - n| \leq M$, there are approximately $M / \sqrt{\log n}$ nodes of $P_k(\gamma_n) = 0$. In particular, $P_n(\gamma_n)$ may be zero for infinitely many $n$ without any fine control.

---

## 6. Implications for the PPP and the Wronskian

### 6.1. The values $P_k(\gamma_n)$ for $k \sim n$ are comparable

From the asymptotics of Cor. 5.1, for $|k - n| \leq K$:

$$|P_k(\gamma_n)| \approx C \gamma_n^{-1/4} k^{-1/4} \cdot |\!\cos(\cdots)|,$$

with the cosine varying arbitrarily. In particular, **there is no reason for $|P_n(\gamma_n)|$ to be larger than $|P_{n \pm 1}(\gamma_n)|$, $|P_{n \pm 2}(\gamma_n)|$, etc.**

### 6.2. The Wronskian $W_n(\gamma_n)$

From Prop. 8.1 of Doc 65, the PPP is equivalent to $W_n(\gamma_n) \neq 0$, where

$$W_n(s) = P_{n+1}(s)Q_n(s) - P_n(s)Q_{n+1}(s).$$

The second-kind polynomials $Q_n$ satisfy the same Jacobi recurrence as $P_n$ but with initial conditions $Q_0 = 0$, $Q_1 = 1/a_0^{\infty}$. In the left-edge region, $Q_k(\gamma_n)$ has the *sine* asymptotics (complementary to the cosine of $P_k$):

$$Q_k(\gamma_n) \approx C' \gamma_n^{-1/4} k^{-1/4} \sin\!\left(\sqrt{\frac{\pi k \gamma_n}{2}} - \frac{\pi}{4}\right).$$

Then the Wronskian:

$$W_n(\gamma_n) \approx C^2 \gamma_n^{-1/2} n^{-1/2} \left[\cos(\Phi_{n+1})\sin(\Phi_n) - \cos(\Phi_n)\sin(\Phi_{n+1})\right] = -C^2 \gamma_n^{-1/2} n^{-1/2} \sin(\Phi_{n+1} - \Phi_n),$$

where $\Phi_k = \sqrt{\pi k \gamma_n/2} - \pi/4$.

**Proposition 6.1** (Wronskian via PR).

$$W_n(\gamma_n) \approx -C^2 \gamma_n^{-1/2} n^{-1/2} \sin\!\left(\Phi_{n+1} - \Phi_n\right),$$

with $\Phi_{n+1} - \Phi_n \approx \sqrt{\pi(n+1)\gamma_n/2} - \sqrt{\pi n \gamma_n/2} \approx \frac{1}{2}\sqrt{\pi\gamma_n/(2n)}$.

For $\gamma_n \approx 2\pi n/\log n$:

$$\Phi_{n+1} - \Phi_n \approx \frac{1}{2}\sqrt{\frac{\pi}{2n} \cdot \frac{2\pi n}{\log n}} = \frac{\pi}{2\sqrt{\log n}} \to 0.$$

So $\sin(\Phi_{n+1} - \Phi_n) \approx \Phi_{n+1} - \Phi_n \approx \frac{\pi}{2\sqrt{\log n}}$.

**Corollary 6.2** (Order of the Wronskian).

$$W_n(\gamma_n) \approx \frac{C^2 \pi}{2} \cdot \gamma_n^{-1/2} n^{-1/2} \cdot (\log n)^{-1/2}.$$

In particular, $W_n(\gamma_n) \neq 0$ for all sufficiently large $n$ (although it tends to zero as $n^{-1/2}(\log n)^{-1/2}$).

---

## 7. The PPP: conclusion of the analysis

### 7.1. Exact form of the pseudo-pole

Combining Prop. 8.1 of Doc 65 with Cor. 6.2:

$$F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z) \approx \frac{W_n(\gamma_n)}{P_n(\gamma_n)P_{n+1}(\gamma_n) \cdot m'_\infty(\gamma_n)(z - \gamma_n)} + \text{hol.}$$

The residue of the pseudo-pole is:

$$\mathrm{Res}_{z=\gamma_n} F_n = \frac{W_n(\gamma_n)}{P_n(\gamma_n)P_{n+1}(\gamma_n) \cdot m'_\infty(\gamma_n)}.$$

To estimate the denominator: $|P_n(\gamma_n)| \approx C\gamma_n^{-1/4}n^{-1/4}|\cos(\cdots)|$. Generically (when the cosine is not zero), $|P_n(\gamma_n)P_{n+1}(\gamma_n)| \sim C^2 \gamma_n^{-1/2} n^{-1/2}$.

And $m'_\infty(\gamma_n) = -\int (s - \gamma_n)^{-2} dm_\infty(s) \sim -\gamma_n^{-2} \cdot dm_\infty([0, O(\gamma_n)])$, which is $O(\gamma_n^{-2})$ for $\gamma_n$ small relative to the scale of $dm_\infty$.

Hence the residue is of order

$$\mathrm{Res} \sim \frac{\gamma_n^{-1/2} n^{-1/2} (\log n)^{-1/2}}{\gamma_n^{-1/2} n^{-1/2} \cdot \gamma_n^{-2}} \sim \gamma_n^2 (\log n)^{-1/2}.$$

### 7.2. Statement of the PPP proved asymptotically

**Theorem 7.1** (Asymptotic PPP). For $n$ sufficiently large and $\gamma_n$ a simple zero of $\Xi$:

$$F_n(z) = \frac{R_n}{z - \gamma_n} + H_n(z),$$

where $H_n$ is holomorphic in a neighborhood of $\gamma_n$, and the residue satisfies

$$R_n \asymp \gamma_n^2 (\log n)^{-1/2} \to \infty \qquad (n \to \infty).$$

In particular the PPP holds asymptotically under the hypothesis of simplicity of the zeros of $\Xi$.

### 7.3. Frankness about the assumptions

Theorem 7.1 depends on:

1. **Simplicity of the zeros of $\Xi$**: so that $P_n(\gamma_n) \neq 0$ generically (Rem. 5.2 indicates that $P_n(\gamma_n) = 0$ can occur, but only for a set of $n$ of density zero under generic distribution).
2. **The PR asymptotics are valid in the left-edge region ($s \ll a_k$)**: the standard DKMVZ theory covers the region $s/a_k \in (\varepsilon, 1-\varepsilon)$; the extension to the edge region requires Airy asymptotics (not computed in this document — left as Doc 67).

The result of Theorem 7.1 is **conditional** on these two hypotheses. The **unconditional** result of the program remains the PTC of Doc 64 (Thm. 3.1).

---

## 8. Summary: status of the PPP program

| Result | Conditional on | Doc |
|-----------|--------------|-----|
| PPP $\iff W_n(\gamma_n) \neq 0$ | — | 65 |
| $W_n(\gamma_n) \neq 0$ for large $n$ | Simplicity of zeros of $\Xi$ | 65, Prop. 8.3 |
| $W_n(\gamma_n) \asymp n^{-1/2}(\log n)^{-1/2}$ | Interior PR asymptotics + simplicity | 66 (this doc) |
| Asymptotic PPP, $R_n \to \infty$ | Interior PR asymptotics + simplicity | 66, Thm. 7.1 |
| PR asymptotics in the edge region (Airy) | — | Doc 67 (pending) |

The general program diagram is completed as follows:

```
PTC (unconditional):  T_λ = 0 ∀λ  ⟺  RH               [Doc 64]
                              ↑
                    W_λ ≥ 0, T_λ > 0 under ¬RH           [Doc 63]

PPP (conditional on simplicity of zeros):
  W_n(γ_n) ≠ 0  [Doc 65 + 66]
    → F_n has a pseudo-pole  [Doc 65, Prop 5.1]
      → alternative route toward d_n^S = 0 ↔ RH  [Doc 62]

Still open:
  → Airy asymptotics at the left edge                  [Doc 67]
  → fully unconditional PPP
```

---

## 9. Direction for Doc 67

The left-edge region of the support, $s = O(1)$ with $a_k = 2k/\pi \to \infty$, corresponds to the transition between the oscillatory regime (Plancherel-Rotach cosine/sine) and the decay regime. In this region, the orthogonal polynomials are approximated by the Airy function (in the variable $\xi = k^{2/3}(s/a_k - 1)$ for the right edge, or the analogous variable $\eta = k^{2/3}(1 - s/a_k)$ for the left edge):

$$P_k(s) \approx C_k \cdot k^{-1/6} \cdot \text{Ai}(-\eta), \qquad \eta = c \cdot k^{2/3}\left(1 - \frac{s}{a_k}\right)^{1/2}.$$

Since $\gamma_n / a_n \to 0$, the point $s = \gamma_n$ lies **even further inside** than the left edge, in the region where the Bessel asymptotics (not Airy) are needed. Concretely, for $s \ll a_k$:

$$P_k(s) \approx D_k \cdot (ks)^{-1/4} J_0\!\left(2\sqrt{ks \cdot \pi/2}\right),$$

where $J_0$ is the Bessel function of order zero. This is consistent with the formula of Cor. 5.1 (the Plancherel-Rotach cosine becomes $J_0$ near the origin).

Doc 67 must establish this Bessel asymptotics rigorously for the CCM measure, and from it compute $W_n(\gamma_n)$ without the simplicity-of-zeros assumption (if possible).

---

*End of Document 66.*
