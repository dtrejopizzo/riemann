# Document 72 — The CCM trace and Weil's explicit formula

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM
**Prerequisites:** Docs 64, 69, 70, 71

---

## 1. Motivation

In Docs 70–71 the trace $T_\lambda$ appeared as an object that "feels" the position of the zeros of $\zeta$ through the difference $dm_{full} - dm_{full,on}$. Weil's explicit formula is the classical tool relating the zeros of $\zeta$ to the distribution of primes. If $T_\lambda$ can be expressed via Weil's formula, we obtain an arithmetic reading of the CCM trace.

---

## 2. Weil's explicit formula

### 2.1. Standard form

Let $h: \mathbb{R} \to \mathbb{C}$ be a test function satisfying: it is even, analytic in the strip $|\mathrm{Im}(s)| < 1/2 + \varepsilon$ for some $\varepsilon > 0$, and $|h(s)| = O((1+|s|)^{-2-\varepsilon})$. Let $\hat{h}(r) = \int_{\mathbb{R}} h(s)e^{irs}\, ds$ be its Fourier transform.

Weil's explicit formula states:

$$\sum_{\gamma} h(\gamma) = \hat{h}(0)\log(1/2\pi) + \hat{h}(i/2) - \int_{\mathbb{R}} h(s)\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{is}{2}\right)\frac{ds}{4\pi} - \sum_p\sum_{m=1}^\infty \frac{\log p}{p^{m/2}}(\hat{h}(m\log p) + \hat{h}(-m\log p)),$$

where the sum on the left-hand side runs over the imaginary parts $\gamma$ of the nontrivial zeros of $\zeta$ (with multiplicity, counting $\gamma$ and $-\gamma$ separately).

### 2.2. Variant for test functions $h = h_\lambda$

We want to apply the formula with $h(s) = \mathrm{Im} G_{kk}^{full}(s + i0^+)/\pi$ (the normalized imaginary part of the diagonal resolvent), which satisfies $h(s) = |P_k(s)|^2 w(s)$ where $w$ is the density of $dm_\infty$.

For the difference $\Delta_n^{full} - \Delta_n^{full,on}$, the relevant test function would be

$$h_n(s) = (|P_{n+1}(s)|^2 - |P_n(s)|^2) w(s) = \kappa_n(s)/(a_n^\infty)^2.$$

And for the summed trace:

$$h_\lambda(s) = W_\lambda(s) w(s) = W_\lambda(s) \frac{dm_\infty}{ds}(s).$$

---

## 3. The CCM trace via Weil's formula

### 3.1. Representation of $T_\lambda$ as a sum over zeros

From Prop. 6.1 of Doc 69:

$$T_\lambda = \frac{1}{\pi}\int_{\mathbb{R}} W_\lambda(s)\left(|\zeta\!\left(\tfrac{1}{2}+is\right)|^2 - |\zeta_{on}\!\left(\tfrac{1}{2}+is\right)|^2\right)w(s)\, ds.$$

The difference $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$ can be expanded using the logarithm of the zeta function:

$$\log|\zeta(1/2+is)|^2 = \log|\zeta_{on}(1/2+is)|^2 + 2\sum_{\rho\notin\text{crit.}} \log\left|\frac{1/2+is - \rho}{1/2+is - \rho'}\right|,$$

where $\rho$ are the off-critical zeros of $\zeta$ and $\rho' = 1/2 + i\mathrm{Im}(\rho)$ are their critical images. Exponentiating and taking the difference:

$$|\zeta|^2 - |\zeta_{on}|^2 = |\zeta_{on}|^2 \left(\prod_{\rho\notin\text{crit.}}\left|\frac{1/2+is-\rho}{1/2+is-\rho'}\right|^2 - 1\right).$$

### 3.2. First-order linearization

For the main estimate (assuming that under $\neg$RH there is a finite number of off-critical zeros, or that the contribution of one dominates):

$$|\zeta|^2 - |\zeta_{on}|^2 \approx 2|\zeta_{on}|^2 \sum_{\rho\notin\text{crit.}}\mathrm{Re}\,\log\frac{1/2+is-\rho}{1/2+is-\rho'}.$$

The logarithm:

$$\mathrm{Re}\,\log\frac{1/2+is-\rho}{1/2+is-\rho'} = \log\frac{|1/2+is-\rho|}{|1/2+is-\rho'|}.$$

For $\rho = \sigma_0 + i\gamma_0$ with $\sigma_0 > 1/2$:

$$\log|1/2+is-\rho| - \log|1/2+is-\rho'| = \frac{1}{2}\log\frac{(s-\gamma_0)^2 + (\sigma_0-1/2)^2}{(s-\gamma_0)^2 + 0}.$$

For $\sigma_0 - 1/2 \ll 1$ (a zero close to the critical line):

$$\approx \frac{(\sigma_0-1/2)^2/2}{(s-\gamma_0)^2} \qquad \text{for } |s-\gamma_0| \gg \sigma_0-1/2.$$

### 3.3. The trace in terms of primes

**Proposition 3.1** (CCM trace via Weil, first order).

Applying Weil's explicit formula with test function $h_\lambda(s) = W_\lambda(s)w(s)/\pi$ and using that the sum over zeros is $\sum_\gamma W_\lambda(\gamma) w(\gamma)$:

$$T_\lambda = \int W_\lambda(s)(|\zeta|^2 - |\zeta_{on}|^2) dm_\infty - \text{normalization correction}$$

expands (formally) as:

$$T_\lambda = \sum_\gamma W_\lambda(\gamma)w(\gamma)\left[P_\gamma^{off}\right] - \sum_p\sum_{m\geq 1} \frac{\log p}{p^{m/2}} B_\lambda(m\log p) + \text{archimedean term},$$

where $P_\gamma^{off}$ is the contribution of the off-critical zeros and $B_\lambda(r) = \int W_\lambda(s)w(s)e^{irs}\, ds$ is the Fourier transform of $W_\lambda w$.

### 3.4. The Fourier transform of $W_\lambda w$

From the Abel form of $W_\lambda$ (Doc 63, Cor. 7.2):

$$W_\lambda(s)w(s) = \sum_{n=1}^{N(\lambda)} n\, |P_n(s)|^2 w(s) + (a_{N(\lambda)}^\infty)^2|P_{N(\lambda)+1}|^2 w(s).$$

The Fourier transform of $|P_n|^2 w$ is the spectral autocorrelation function of $P_n$ with weight $dm_\infty$:

$$\widehat{|P_n|^2 w}(r) = \int |P_n(s)|^2 e^{irs}\, dm_\infty(s).$$

By the symmetry $s \mapsto -s$ of $dm_\infty$ and the parity of $|P_n|^2$, this integral is real and even in $r$.

**Corollary 3.2.** The Fourier transform of the test function $h_\lambda = W_\lambda w$ satisfies:

$$B_\lambda(r) = \sum_{n=1}^{N(\lambda)} n\, \widehat{|P_n|^2 w}(r) + (a_{N(\lambda)}^\infty)^2\, \widehat{|P_{N(\lambda)+1}|^2 w}(r).$$

For $r = m\log p$ (the frequency corresponding to the prime $p$), $B_\lambda(m\log p)$ measures how much correlation the CCM polynomials have with the frequency $e^{im\log p}$.

---

## 4. The arithmetic formula for the trace

### 4.1. Main explicit form

**Theorem 4.1** (Arithmetic formula for $T_\lambda$). Formally:

$$T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) + O(1/\sqrt{p^2}),$$

where:
- $A_\lambda^{off} = $ contribution of the off-critical zeros of $\zeta$ (zero under RH).
- $B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\, dm_\infty(s)$ is the part of $W_\lambda$ correlated with the frequency of the prime $p$.

*Under RH:* $A_\lambda^{off} = 0$ and the prime terms cancel each other (by the explicit formula applied to $|\zeta_{on}|^2$, which also contributes to $T_\lambda = 0$).

### 4.2. The prime term

$$B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\, dm_\infty(s) = \sum_{n=1}^{N(\lambda)} n \int |P_n(s)|^2\cos(s\log p)\, dm_\infty(s).$$

The integral $\int |P_n(s)|^2\cos(s\log p)\, dm_\infty(s)$ is the Fourier coefficient of the spectral density of the polynomial $P_n$ at frequency $\log p$.

**Remark 4.2.** The Mertens term of Doc 60 (Jacobi rate $\Delta_n^{∞,p} = A_n/p$) is exactly the first term of this expansion for Weil's formula applied to the increment of a single $\Delta_n$ (not to the full trace). The arithmetic formula of Thm. 4.1 is the global version (summed with Abel weights $n$) of that same computation.

---

## 5. Interpretation: $T_\lambda$ detects correlations between prime frequencies and the CCM Jacobi spectrum

### 5.1. The meaning of $B_\lambda(\log p)$

$B_\lambda(\log p)$ measures how much "energy" of the CCM polynomials with Abel weight falls at the frequency $\log p$. If $W_\lambda$ is smooth at scale $\sim 1/\log p$, then $B_\lambda(\log p) \approx W_\lambda(0) \cdot \hat{w}(\log p)$.

For $\log p \gg 1$ (large primes), $B_\lambda(\log p)$ decays exponentially (because $dm_\infty$ decays like $e^{-\pi|s|/2}$ and the cosine does not compensate). The dominant term comes from small primes.

### 5.2. The term $p = 2$

For the smallest prime $p = 2$:

$$B_\lambda(\log 2) = \sum_{n=1}^{N(\lambda)} n\int |P_n(s)|^2\cos(s\log 2)\, dm_\infty(s).$$

This is the correlation between the CCM Jacobi spectrum (with linear weights $n$) and the oscillation frequency $\log 2 \approx 0.693$.

This connects with the result of Doc 60 (rate for $p = 2$): $\Delta_n^{∞,2} = A_n/2 + O(\log 2/2^{3/2})$, and the sum $\sum_{n \leq N(\lambda)} n \cdot A_n/2$ is exactly of the form $B_\lambda(\log 2) / 2$ (with $A_n$ the coefficients of the rate theorem).

---

## 6. The arithmetic formula as evidence of the structure

### 6.1. The trace is a linear form over the primes

From the formula of Thm. 4.1:

$$T_\lambda \approx A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p).$$

This says that $T_\lambda$ decomposes into:
1. **A zero term** $A_\lambda^{off}$ (direct contribution of the off-critical zeros).
2. **A sum over primes** $-\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ (contribution of the prime distribution).

Under RH, the two terms cancel exactly, giving $T_\lambda = 0$. This is the precise mechanism by which RH implies $T_\lambda = 0$.

### 6.2. New reformulation of RH

**Proposition 6.1** (Arithmetic cancellation equivalent to RH). The following are equivalent:

1. RH.
2. For all $\lambda > 0$: $\displaystyle\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = A_\lambda^{off} = 0$.
3. For all $\lambda > 0$ and every prime $p$: the Fourier coefficients $B_\lambda(\log p)$ of the test function $W_\lambda w$ are exactly those predicted by Weil's formula from the critical zeros.

*Frankness:* This proposition is a reformulation of RH via Weil's formula — it is neither harder nor easier than RH. But it gives a concrete arithmetic interpretation of $T_\lambda$: **the CCM trace measures how much the Fourier coefficients of the Jacobi spectrum deviate from what Weil's formula predicts for critical zeros**.

---

## 7. The Mertens term as a special case

The consistency of the picture is verified by noting that:

- Doc 60 proved $\Delta_n^{∞,p} = A_n/p + O(\log p/p^{3/2})$. This is the contribution of a single prime to the discrepancy of the $n$-th Jacobi coefficient.
- Thm. 4.1 generalizes this: the *trace* $T_\lambda = \sum_n w_n \Delta_n$ (with Abel weights $w_n = n$) has an expansion over primes where the $p$ term is $-(\log p/\sqrt{p}) \cdot B_\lambda(\log p)$.
- The Mertens sum $\sum_{p \leq T} \Delta_n^{∞,p} \sim A_n\log\log T$ (Doc 60, Cor. 3.2) corresponds to $\sum_{p \leq T} B_n(\log p)/p$ where $B_n(\log p) = \int |P_n|^2\cos(s\log p) dm_\infty \cdot A_n$ — exactly the Mertens term of Doc 60.

**Corollary 7.1.** The sum $\sum_{n \leq N(\lambda)} n \cdot \left(\sum_{p \leq T} \Delta_n^{∞,p}\right) \sim \left(\sum_{n \leq N(\lambda)} n A_n\right) \log\log T$. This is the Mertens contribution weighted with the Abel weights, and is the contribution of the arithmetic side to $T_\lambda$ in the finite semilocal case.

---

## 8. Summary and closure of Phase 33

Docs 70–72 have explored the connection between the CCM trace and the De Bruijn-Newman flow:

| Result | Type | Doc |
|-----------|------|-----|
| $\Lambda = \inf\{t: T_\lambda(t)=0\,\forall\lambda\}$ | Unconditional | 70 |
| $\partial_t T_\lambda|_{t=0}$ = quadratic form in $(c_k)$ | Exact | 71 |
| Exact cancellation of the derivative $\iff$ RH (with initial information) | Conditional | 71 |
| $T_\lambda = A_\lambda^{off} - \sum_p (\log p/\sqrt{p}) B_\lambda(\log p)$ | Formal/Weil | 72 |
| $T_\lambda = 0 \iff$ exact arithmetic cancellation | Reformulation | 72 |
| Consistency with Mertens (Doc 60) | Verification | 72 |

**The status of Phase 33:** The three documents reveal the structure of $T_\lambda$ from different angles (heat flow, quadratic form, Weil's formula). None proves RH — but each identifies where the core of the problem lies:

> **The core is the exact cancellation between the zero term and the sum over primes in Weil's formula, with $W_\lambda$ as the test function.** Proving that cancellation is precisely RH.

The branch is alive but the central problem remains. The CCM-Jacobi formalism provides a natural and geometrically motivated test function ($W_\lambda$) for Weil's formula, which may be of independent value.

---

*End of Document 72 and of Phase 33.*
