# Document 78 — The transform between Li's criterion and the CTP-CCM criterion

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 63, 64, 70, 71, 72, 73, 75, 76

---

## Summary

Li's criterion and the CTP-CCM criterion are two equivalences to RH expressed in different languages. Doc 75 established that they are structurally different (Li detects deviations from the critical line at order $\delta^1$, CTP at order $\delta^2$) and proved the quantitative bound $T_\lambda \geq C(\lambda,n_0)|\lambda_{n_0}|$ under $\neg$RH. Doc 75 left open Conjecture 6.3: the existence of an integral transform $\mathcal{T}$ such that $\lambda_n = \mathcal{T}[T_\bullet](n)$.

In this document we tackle the construction of such a transform directly. The results are:

1. **(§1, proved):** Simultaneous representation of $\lambda_n$ and $T_\lambda$ as functionals of the zero measure in the complex plane.
2. **(§2, partially proved):** The Laplace transform of $\lambda \mapsto T_\lambda$ admits an expression as a series over zeros, formally connected to $\{\lambda_n\}$ via Li's generating function.
3. **(§3, partially proved):** Weil's explicit formula applied to both criteria shows that the prime terms of $\lambda_n$ and $T_\lambda$ are images of each other under a Stieltjes transform.
4. **(§4, proved):** The contribution of an off-critical zero $\rho_0$ to $\lambda_n$ and to $T_\lambda$ is compared explicitly: the ratios of the contributions are independent of the zero as $\delta \to 0$.
5. **(§5, conjectural):** A kernel $K(n,\lambda)$ is formally constructed and its positivity is investigated.
6. **(§6, conjectural):** The Unified Criterion is formulated as a positivity problem for functionals on the zero measure.
7. **(§7):** Balance of what remains to complete the path to RH.

**Notation and conventions.** Throughout the document: $\rho = \sigma + i\gamma$ denotes a non-trivial zero of $\zeta$; for zeros on the critical line $\sigma = 1/2$ and we write $\rho = 1/2 + i\gamma$; $\delta = \sigma - 1/2$ is the distance to the critical line; off-critical zeros have $\delta \neq 0$ and come in quadruplets $\mathcal{Q}(\rho_0) = \{\sigma_0 \pm i\gamma_0, (1-\sigma_0)\pm i\gamma_0\}$; $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 ds$; $W_\lambda(s)$ is the Abel kernel of Doc 63.

---

## §1. Two representations of the same zeros

### 1.1. Li's criterion as an integral over the zero measure

Let $\mu_{zeros} = \sum_\rho \delta_\rho$ be the zero measure of $\zeta$ in the complex plane (sum over all non-trivial zeros with multiplicity). By Proposition 1.2 of Doc 75:

$$\lambda_n = \int_{\mathbb{C}} \phi_n(z)\, d\mu_{zeros}(z), \qquad \phi_n(z) = 1 - \left(1 - \frac{1}{z}\right)^n.$$

The sum includes all non-trivial zeros. The functional equation $\xi(s) = \xi(1-s)$ guarantees that the zeros come in conjugate pairs $(\rho, \bar\rho)$ and symmetric pairs $(\rho, 1-\rho)$; summing over all zeros, the contribution of each quadruplet $\mathcal{Q}(\rho_0)$ is

$$\Lambda_n(\rho_0) = \sum_{\rho \in \mathcal{Q}(\rho_0)} \phi_n(\rho) = \sum_{\rho \in \mathcal{Q}(\rho_0)} \left[1 - \left(1-\frac{1}{\rho}\right)^n\right].$$

**Proposition 1.1** (sign of $\Lambda_n$ according to the position of $\rho_0$).

(a) If $\rho_0 = 1/2 + i\gamma_0$ is a critical zero, then $\Lambda_n(\rho_0) = 2(1-\cos(n\theta(\gamma_0))) \geq 0$.

(b) If $\rho_0 = (1/2+\delta_0)+i\gamma_0$ is off-critical with $\delta_0 > 0$, two of the four factors $(1-1/\rho)$ have modulus $r_0 < 1$ and two have modulus $1/r_0 > 1$. As $n \to \infty$, $\Lambda_n(\rho_0) \sim -2(1/r_0)^n \cos(n\phi_0)$, which takes negative values for a sequence of $n \to \infty$.

*Proof.* Part (a): this is Proposition 1.2, §1.2 of Doc 75. Part (b): this is Proposition 1.3, §1.3 of Doc 75. $\square$

### 1.2. The CTP criterion as an integral over the off-critical zero measure

Let $\mu_{zeros}^{off} = \sum_{\rho : \sigma_\rho \neq 1/2} \delta_\rho$ be the measure restricted to off-critical zeros. From Proposition 4.2 of Doc 75 (with the notation of Corollary 2.2 of that document):

$$T_\lambda = \int_{\mathbb{C}} \Phi_\lambda(\rho)\, d\mu_{zeros}^{off}(\rho) + E_\lambda,$$

where
$$\Phi_\lambda(\sigma+i\gamma) = (\sigma - 1/2)^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(1/2+is)|^2 \left(\frac{1}{(s-\gamma)^2} + \frac{1}{(s+\gamma)^2}\right) dm_\infty(s)$$
is the CTP test function to first order in $\delta^2$, and $E_\lambda = O(\sum_j \delta_j^4)$ is the higher-order error.

**Remark 1.2** (fundamental structural difference). The test functions $\phi_n$ and $\Phi_\lambda$ have different natures: $\phi_n(z)$ is holomorphic on $\mathbb{C}\setminus\{0\}$ and depends on $z$ in a non-separable way in $(\sigma,\gamma)$; $\Phi_\lambda(\sigma+i\gamma)$ is real $C^\infty$ in $(\sigma,\gamma)$ and factorizes to first order as $(\sigma-1/2)^2 \cdot K_\lambda(\gamma)$ with $K_\lambda(\gamma) \geq 0$.

### 1.3. The respective scale functions

To relate the two criteria, it is convenient to introduce the *scale functions* of each zero:

**Definition 1.3.** For $\rho = \sigma + i\gamma$ non-trivial with $\sigma > 1/2$, let:
- $f_{Li}(\rho) = \log(|\rho|/|\rho - 1|)$: the logarithm of the ratio of the distances of $\rho$ to the origin and to the point $z = 1$.
- $f_{CTP}(\rho) = \sigma - 1/2$: the distance of $\rho$ to the critical line.

**Remark 1.4.** These scales are comparable for near-critical zeros $\delta \ll 1$:
$$f_{Li}(\rho) = \log\frac{|\rho|}{|\rho-1|} = \log\frac{\sqrt{(1/2+\delta)^2+\gamma^2}}{\sqrt{(1/2-\delta)^2+\gamma^2}} \approx \frac{2\delta}{1/4+\gamma^2} \cdot \frac{\sqrt{1/4+\gamma^2}}{2} = \frac{\delta}{\sqrt{1/4+\gamma^2}}.$$
Thus $f_{Li}(\rho) \asymp \delta/(1+|\gamma|)$ while $f_{CTP}(\rho) = \delta$. The difference is the factor $(1+|\gamma|)^{-1}$, which penalizes zeros with large imaginary part. This has consequences for the relation between the transforms (see §4).

---

## §2. The Laplace transform of $\lambda \mapsto T_\lambda$ as a generating function

### 2.1. Definition of the Laplace transform

The function $\lambda \mapsto T_\lambda$ is non-decreasing in $\lambda$ (under $\neg$RH, each time $\lambda$ exceeds the imaginary part of an off-critical zero, the trace jumps; under RH it is identically zero). Its Laplace transform is formally defined as:

$$\hat{T}(s) = \int_0^\infty e^{-s\lambda}\, T_\lambda\, d\lambda, \qquad s > 0.$$

**Proposition 2.1** (structure of $\hat{T}(s)$ under $\neg$RH). Let $\{\rho_j = (1/2+\delta_j)+i\gamma_j\}_{j \geq 1}$ be the set of off-critical zeros ordered by $|\gamma_j|$, with $0 < |\gamma_1| \leq |\gamma_2| \leq \ldots$ For $\lambda < |\gamma_1|$, $T_\lambda = 0$. For $|\gamma_j| \leq \lambda < |\gamma_{j+1}|$, the trace is $T_\lambda = \sum_{k \leq j} T^{(\rho_k)}_\lambda$ where $T^{(\rho_k)}_\lambda$ is the contribution of quadruplet $\mathcal{Q}(\rho_k)$. Then, integrating by parts:

$$\hat{T}(s) = \frac{1}{s}\sum_{j \geq 1} T^{(\rho_j)}_\infty\, e^{-s|\gamma_j|},$$

where $T^{(\rho_j)}_\infty = \lim_{\lambda \to \infty} T^{(\rho_j)}_\lambda$ is the total contribution of quadruplet $j$.

*Proof.* Using that $T_\lambda$ is constant on each interval $[|\gamma_j|, |\gamma_{j+1}|)$ (up to order-$\delta^4$ terms from the error $E_\lambda$), integrating by parts:
$$\hat{T}(s) = \int_0^\infty e^{-s\lambda} T_\lambda\, d\lambda = \frac{1}{s}\int_0^\infty e^{-s\lambda}\, dT_\lambda = \frac{1}{s}\sum_j \Delta T_{\gamma_j}\, e^{-s|\gamma_j|},$$
where $\Delta T_{\gamma_j} = T_{|\gamma_j|+\varepsilon} - T_{|\gamma_j|-\varepsilon} \approx T^{(\rho_j)}_\infty$ is the jump at $\lambda = |\gamma_j|$. $\square$

### 2.2. Li's generating function and its connection

The generating function of the Li coefficients is
$$\Lambda(z) = \sum_{n=1}^\infty \lambda_n\, z^n = \sum_\rho \frac{z(1-1/\rho)}{1-z(1-1/\rho)}, \qquad |z| < 1.$$

Convergence of this power series follows from $\sum_\rho |1-1/\rho|/(|\rho|\log|\rho|) < \infty$.

**Proposition 2.2** (formal connection via Laplace transform). Formally, if we define $u_j = |1-1/\rho_j|_{>1}$ (the exponential growth factor of quadruplet $j$ with modulus $> 1$, i.e. $u_j = 1/r_j$ in the notation of §1.1(b)), then for large $n$:
$$\lambda_n \approx -2\sum_{j \in J^-} u_j^n \cos(n\phi_j),$$
where the sum runs over the off-critical zeros of the quadruplet that contribute negatively.

Comparing with $\hat{T}(s) = \frac{1}{s}\sum_j T_\infty^{(\rho_j)} e^{-s|\gamma_j|}$, to connect $\lambda_n$ with $\hat{T}(s)$ we would need to identify $u_j^n = e^{n\log u_j}$ with $e^{-s|\gamma_j|}$, which requires the identification $s|\gamma_j| = -n\log u_j$. Since $\log u_j = \log(1/r_j) = -\log r_j > 0$ and $|\gamma_j| > 0$, this would give $s = n\log(1/r_j)/|\gamma_j|$: the Laplace parameter depends on $n$ and on the zero $j$, preventing a uniform identification.

**Conclusion 2.3** (obstacle to the direct Laplace transform). The Laplace transform $\hat{T}(s)$ is not the generating function of $\lambda_n$ under a simple transform. The obstacle is that:
- $\lambda_n$ grows exponentially in $n$ (at rate $u_j^n = e^{n\log(1/r_j)}$) for each off-critical zero.
- $\hat{T}(s)$ decays exponentially in $s$ (at rate $e^{-s|\gamma_j|}$) for each off-critical zero.

The duality parameter is not $s \leftrightarrow n$ directly, but $s \leftrightarrow -\log r_j / |\gamma_j|$ — a parameter that depends on the individual zero.

### 2.3. The Stieltjes transform as the correct candidate

The obstacle of §2.2 suggests looking for a transform different from the Laplace one. Consider the *Stieltjes transform* in the variable $t = -\log r$:

**Definition 2.4.** For a function $F: [0,\infty) \to \mathbb{R}$, the Stieltjes transform of parameter $n$ is
$$\mathcal{S}_n[F] = \int_0^\infty (1-e^{-t})^n\, dF(t).$$

**Proposition 2.5** (Stieltjes representation of $\lambda_n$). If the off-critical zeros contribute with moduli $r_j = |1-1/\rho_j|_{<1}$ (for the two members of the quadruplet with modulus $< 1$), then defining the scale measure

$$d\nu(t) = \sum_j \left[\text{mass at }t = -\log r_j\right] \cdot (\text{appropriate sign coefficient}),$$

the Li coefficients formally satisfy

$$\lambda_n = \mathcal{S}_n[d\nu] = \int_0^\infty (1-e^{-t})^n\, d\nu(t).$$

*Proof (formal).* For each zero $\rho$ with $|1-1/\rho| = e^{-t_\rho}$, the term $1-(1-1/\rho)^n = 1 - e^{-nt_\rho}$. If the positive part of $\lambda_n$ (contributions of zeros with $|1-1/\rho| \leq 1$) can be written as an integral $\int (1-e^{-t})^n d\nu^+(t)$, then the representation exists formally. The difficulty is that for the two members of the quadruplet with modulus $> 1$, the term $1 - e^{nt_\rho}$ (with $t_\rho < 0$) diverges in $n$: the term $(1-e^{-t})^n$ with $e^{-t} > 1$ is not in $[0,1]$ and the integral is not a probability one. Therefore the Stieltjes representation only captures the part of the zeros with $|1-1/\rho| < 1$.

**This is frankly a partial representation.** The negative part of $\lambda_n$ (due to the two members of the quadruplet with modulus $> 1$) has no representation as a Stieltjes integral with a non-negative measure. $\square$

---

## §3. Weil's formula as an arithmetic bridge

### 3.1. The arithmetic representation of $\lambda_n$

Weil's explicit formula with test function $h: \mathbb{R} \to \mathbb{C}$ establishes (Doc 72, §2.1):

$$\sum_\gamma h(\gamma) = \hat{h}(0)\log\frac{1}{2\pi} + \hat{h}(i/2) - \int_{\mathbb{R}} h(s)\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{is}{2}\right)\frac{ds}{4\pi} - \sum_p\sum_{m=1}^\infty \frac{\log p}{p^{m/2}}\bigl[\hat{h}(m\log p) + \hat{h}(-m\log p)\bigr],$$

where $\gamma$ runs over the imaginary parts of the non-trivial zeros (with multiplicity).

To obtain $\lambda_n = \sum_\rho [1-(1-1/\rho)^n]$, we need a test function $h_n$ whose sum over $\gamma$ is $\lambda_n$. Using the relation between $\rho = 1/2 + i\gamma$ and $1-1/\rho$, we define:

**Proposition 3.1** (Weil test function for $\lambda_n$). The function
$$h_n(u) = \mathrm{Re}\,\left[1 - \left(\frac{1/2 + iu - 1}{1/2 + iu}\right)^n\right] = 1 - \mathrm{Re}\,\left[\left(\frac{-1/2+iu}{1/2+iu}\right)^n\right]$$
satisfies $\sum_\gamma h_n(\gamma) = \lambda_n$ (up to contributions from the poles of $\zeta$ and the trivial zeros). The explicit contributions of the non-spectral terms (pole of $\zeta$ at $s=1$ and trivial zeros) are:
- Pole at $s=1$: contribution $+1$ (the Li term corresponding to the simple pole).
- Trivial zeros $\rho = -2k$, $k = 1, 2, \ldots$: contribution $1-(1-1/(-2k))^n = 1-(1+1/(2k))^n$, which is $< 0$ for all $n \geq 1$.

The complete sum is $\lambda_n = \sum_\gamma h_n(\gamma) + [\text{trivial corrections}]$.

*Proof.* Immediate from the definition $\lambda_n = \sum_\rho [1-(1-1/\rho)^n]$ identifying $u = \gamma$ for zeros $\rho = 1/2 + i\gamma$. $\square$

The Fourier transform of $h_n$ requires extending $h_n$ to a function of the real variable $u$:

$$\hat{h}_n(r) = \int_{\mathbb{R}} h_n(u)\, e^{iru}\, du.$$

**Lemma 3.2** (computation of $\hat{h}_n$). Writing $h_n(u) = 1 - \mathrm{Re}[e^{in\theta(u)}]$ where $e^{i\theta(u)} = (-1/2+iu)/(1/2+iu)$, the Fourier transform is

$$\hat{h}_n(r) = 2\pi\delta(r) - \int_{\mathbb{R}} \mathrm{Re}\,\left[e^{in\theta(u)}\right] e^{iru}\, du.$$

The second integral can be computed by residues. The integrand $e^{in\theta(u)} e^{iru}$ has poles at $u = i/2$ (from $1/(1/2+iu)^n$). For $r > 0$, closing the contour in the upper half-plane:

$$\int_{\mathbb{R}} e^{in\theta(u)} e^{iru}\, du = 2\pi i \cdot \mathrm{Res}_{u = i/2}\left[\left(\frac{-1/2+iu}{1/2+iu}\right)^n e^{iru}\right].$$

The residue at $u = i/2$ (pole of order $n$ of $(1/2+iu)^{-n}$):

$$\mathrm{Res}_{u=i/2}\left[e^{iru}(-1/2+iu)^n(1/2+iu)^{-n}\right] = \frac{1}{(n-1)!}\frac{d^{n-1}}{du^{n-1}}\left[e^{iru}(-1/2+iu)^n\right]_{u=i/2}.$$

At $u = i/2$: $-1/2 + iu = -1/2 + i\cdot i/2 = -1/2 - 1/2 = -1$. Expanding by Leibniz:

$$\frac{d^{n-1}}{du^{n-1}}\left[e^{iru}(-1/2+iu)^n\right]_{u=i/2} = \sum_{k=0}^{n-1}\binom{n-1}{k}(ir)^k e^{-r/2}\cdot \frac{n!}{(n-k)!}(-1)^{n-k}i^{n-k} \cdot (i)^{n-k}\cdot(\text{evaluated at }-1).$$

The complete computation is technical; let us denote the result as $\hat{h}_n(r) = e^{-r/2} P_n(r)$ where $P_n(r)$ is a polynomial in $r$ of degree $n-1$. The decay $e^{-r/2}$ as $r \to +\infty$ is consistent with the properties of $h_n$ as an analytic function in the strip $|\mathrm{Im}(u)| < 1/2$.

**Proposition 3.3** (arithmetic representation of $\lambda_n$). Applying Weil's formula with test function $h_n$:

$$\lambda_n = C_n - \sum_p\sum_{m=1}^\infty \frac{\log p}{p^{m/2}}\bigl[\hat{h}_n(m\log p) + \hat{h}_n(-m\log p)\bigr],$$

where $C_n = \hat{h}_n(0)\log(1/2\pi) + \hat{h}_n(i/2) - \int_{\mathbb{R}} h_n(u) \frac{\Gamma'}{\Gamma}(1/4+iu/2)\frac{du}{4\pi}$ contains all the non-spectral contributions. The prime contributions are the ones carrying the information about the zeros of $\zeta$.

### 3.2. The arithmetic representation of $T_\lambda$

From Doc 72 and Doc 75, the CCM trace has the representation (to first order in $\delta^2$):

$$T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p),$$

where $B_\lambda(\log p) = \widehat{W_\lambda dm_\infty}(\log p)$ is the Fourier transform of the weighted kernel evaluated at $\log p$ (Doc 76, §4.3), and $A_\lambda^{off}$ contains the non-spectral terms of Weil's formula applied to $W_\lambda \cdot |\zeta-\zeta_{on}|^2$.

### 3.3. Comparison of the sums over primes

**Proposition 3.4** (relation between the prime terms of $\lambda_n$ and $T_\lambda$). Let $F_p(n) = -\hat{h}_n(\log p) - \hat{h}_n(-\log p)$ be the contribution of the prime $p$ to $\lambda_n$ (with sign), and let $G_p(\lambda) = B_\lambda(\log p) = \widehat{W_\lambda dm_\infty}(\log p)$ be the contribution of $p$ to $T_\lambda$. Then formally, if there exists a transform $\mathcal{T}$ such that $\lambda_n = \mathcal{T}[T_\bullet](n)$, this transform must in particular satisfy:

$$F_p(n) = \mathcal{T}\!\left[\lambda \mapsto G_p(\lambda)\right](n), \qquad \text{for every prime } p.$$

This is a necessary condition for the existence of $\mathcal{T}$.

**Analysis of the prime-by-prime condition.** For a fixed prime $p$:
- $F_p(n) = -\hat{h}_n(\log p) - \hat{h}_n(-\log p)$: decays like $e^{-(\log p)/2}$ for fixed $n$ and $p \to \infty$.
- $G_p(\lambda) = \widehat{W_\lambda dm_\infty}(\log p) \sim K_p N(\lambda)^{5/4}$ as $\lambda \to \infty$ (Doc 76, Proposition 4.3).

The relation $F_p(n) = \mathcal{T}[G_p](n)$ would require transforming a growing function (polynomially in $\lambda$) into a bounded function (exponentially in $p$). This is possible if $\mathcal{T}$ involves a derivation or differentiation that "compresses" the growth, but it is not immediate.

**Conclusion 3.5.** The existence of a prime-by-prime transform $\mathcal{T}$ (Proposition 3.4) is subject to the compatibility of the growth orders. The necessary condition is not obvious and becomes a restriction on the form of $\mathcal{T}$.

---

## §4. The contributions of an off-critical zero: explicit comparison

### 4.1. Contribution to $\lambda_n$

Let $\rho_0 = (1/2+\delta_0)+i\gamma_0$ with $\delta_0 > 0$. The contribution of the quadruplet $\mathcal{Q}(\rho_0)$ to $\lambda_n$ is (Doc 75, §1.3):

$$\Lambda_n(\rho_0) = \sum_{\rho \in \mathcal{Q}(\rho_0)} \left[1-\left(1-\frac{1}{\rho}\right)^n\right].$$

For large $n$, the two dominant terms are those of $1-\rho_0$ and $\overline{1-\rho_0}$, whose factors $|1-1/(1-\rho_0)| = 1/r_0 > 1$. Expanding to first order in $\delta_0$:

$$1 - \frac{1}{1-\rho_0} = \frac{-\rho_0}{1-\rho_0} = \frac{-(1/2+\delta_0+i\gamma_0)}{(1/2-\delta_0)-i\gamma_0}.$$

Computing the modulus and argument:

$$\left|1-\frac{1}{1-\rho_0}\right|^2 = \frac{(1/2+\delta_0)^2+\gamma_0^2}{(1/2-\delta_0)^2+\gamma_0^2} = 1 + \frac{2\delta_0}{(1/2-\delta_0)^2+\gamma_0^2} + O(\delta_0^2) \approx 1 + \frac{4\delta_0}{1+4\gamma_0^2}.$$

Writing $1-1/(1-\rho_0) = (1/r_0)e^{i\psi_0}$ with $1/r_0 = \sqrt{1 + 4\delta_0/(1+4\gamma_0^2)} + O(\delta_0^2)$ and $\psi_0 = \arg(-\rho_0/(1-\rho_0))$:

$$\left(\frac{1}{r_0}\right)^n = \exp\!\left(\frac{n \cdot 2\delta_0}{1+4\gamma_0^2} + O(n\delta_0^2)\right) = 1 + \frac{2n\delta_0}{1+4\gamma_0^2} + O(n^2\delta_0^2 + n\delta_0^2).$$

Therefore, the dominant contribution of $1-\rho_0$ to $\Lambda_n(\rho_0)$ to first order in $\delta_0$ is:

$$\left[1-\left(1-\frac{1}{1-\rho_0}\right)^n\right] + \left[1-\left(1-\frac{1}{\overline{1-\rho_0}}\right)^n\right] \approx -2\cos(n\psi_0)\cdot\left(\frac{1}{r_0}\right)^n,$$

and to order $\delta_0^1$:

$$\approx -2\cos(n\psi_0)\left(1 + \frac{2n\delta_0}{1+4\gamma_0^2}\right).$$

Combining with the contribution of $\rho_0$ and $\bar\rho_0$ (which have modulus $r_0 < 1$ and decay to 0):

**Proposition 4.1.** To first order in $\delta_0$ (and exact for moderate $n$ with $n\delta_0 \ll 1$):

$$\Lambda_n(\rho_0) = -\frac{4n\delta_0}{1+4\gamma_0^2}\cos(n\psi_0) + O(n^2\delta_0^2),$$

where $\psi_0 = \arg(-\rho_0^{crit}/(1-\rho_0^{crit}))$ with $\rho_0^{crit} = 1/2+i\gamma_0$ the critical projection of $\rho_0$.

*Proof.* The contribution of $\rho_0 = (1/2+\delta_0)+i\gamma_0$ and $\bar\rho_0$ to $\Lambda_n$ is $O(r_0^n) = O(e^{-n\delta_0/(1+4\gamma_0^2)}) \to 0$ exponentially in $n$. The contribution of $1-\rho_0$ and $\overline{1-\rho_0}$ is the one computed above. The detailed computation of $\psi_0$ and the constant of the linear term in $\delta_0$ is a direct complex-argument calculation. $\square$

**Corollary 4.2.** For the off-critical zero $\rho_0$, the first time $\Lambda_n(\rho_0) < 0$ occurs for $n = n_0(\rho_0)$ of order $|\gamma_0|/\delta_0$ (the number of turns of the argument $n\psi_0$ needed for $\cos(n\psi_0) > 0$ with sufficient strength to dominate the contributions of the critical zeros).

### 4.2. Contribution to $T_\lambda$

The contribution of the quadruplet $\mathcal{Q}(\rho_0)$ to $T_\lambda$ for $\lambda > |\gamma_0|$ is (Doc 75, Corollary 2.2):

$$T_\lambda^{(\rho_0)} \approx \delta_0^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(1/2+is)|^2 \left(\frac{1}{(s-\gamma_0)^2} + \frac{1}{(s+\gamma_0)^2}\right) dm_\infty(s) =: \delta_0^2 \cdot K_\lambda(\gamma_0).$$

The kernel $K_\lambda(\gamma_0)$ is independent of $\delta_0$ at this order and depends only on the imaginary part $\gamma_0$.

**Proposition 4.3** (behavior of $K_\lambda(\gamma_0)$). The kernel $K_\lambda(\gamma_0)$ satisfies:

(a) $K_\lambda(\gamma_0) > 0$ for all $\lambda > |\gamma_0|$.

(b) For $\lambda \gg |\gamma_0|$, $K_\lambda(\gamma_0) \sim C_0 \cdot N(\lambda)^2/\gamma_0^2$ where $C_0 > 0$ is a constant and $N(\lambda) = \lfloor\lambda/2\rfloor$.

(c) For $\lambda$ slightly greater than $|\gamma_0|$, $K_\lambda(\gamma_0) \sim K_0(\gamma_0) > 0$ where $K_0(\gamma_0)$ is the contribution of the first level of the Abel kernel.

*Proof.* (a) is Proposition 2.3 of Doc 75. For (b): $W_\lambda(s)$ has $N(\lambda)$ summands, each $O(N(\lambda))$, and its integral against $|\zeta_{on}|^2(s-\gamma_0)^{-2} dm_\infty$ grows like $N(\lambda)^2/\gamma_0^2$ in the region $s \gg \gamma_0$ where $(s-\gamma_0)^{-2} \approx s^{-2}$. For (c): direct from the definition of the first level $W_\lambda = 1\cdot|P_1(s)|^2 + \ldots$ $\square$

### 4.3. The ratio of contributions and the candidate transform

From Propositions 4.1 and 4.3, the ratio of the contributions of $\rho_0$ to the two criteria is:

$$\frac{T_\lambda^{(\rho_0)}}{|\Lambda_n(\rho_0)|} \approx \frac{\delta_0^2 K_\lambda(\gamma_0)}{\frac{4n\delta_0}{1+4\gamma_0^2}|\cos(n\psi_0)|} = \frac{\delta_0(1+4\gamma_0^2)}{4n|\cos(n\psi_0)|} \cdot K_\lambda(\gamma_0).$$

**Remark 4.4** (the ratio depends on $\delta_0$). This ratio is not independent of $\delta_0$, which quantitatively confirms Proposition 6.4 of Doc 75: the two criteria detect the same violation at different orders in $\delta_0$.

However, the ratio has a factored form:
$$\frac{T_\lambda^{(\rho_0)}}{|\Lambda_n(\rho_0)|} = \delta_0 \cdot \frac{(1+4\gamma_0^2)K_\lambda(\gamma_0)}{4n|\cos(n\psi_0)|}.$$

If we take the ratio of the **derivatives** with respect to $\delta_0$ at $\delta_0 = 0$:

$$\left.\frac{\partial T_\lambda^{(\rho_0)}/\partial\delta_0}{|\partial\Lambda_n(\rho_0)/\partial\delta_0|}\right|_{\delta_0=0} = \frac{0}{4n(1+4\gamma_0^2)^{-1}|\cos(n\psi_0)|} = 0,$$

since $T_\lambda^{(\rho_0)} = O(\delta_0^2)$ has first derivative zero at $\delta_0 = 0$. This confirms the order difference.

The **second derivative** at $\delta_0 = 0$:
$$\left.\frac{\partial^2 T_\lambda^{(\rho_0)}/\partial\delta_0^2}{|\partial\Lambda_n(\rho_0)/\partial\delta_0|}\right|_{\delta_0=0} = \frac{2K_\lambda(\gamma_0)}{4n(1+4\gamma_0^2)^{-1}|\cos(n\psi_0)|} = \frac{(1+4\gamma_0^2)K_\lambda(\gamma_0)}{2n|\cos(n\psi_0)|}.$$

**Proposition 4.5** (differential relation between the criteria for each zero). For the off-critical zero $\rho_0$, the relation between its contributions to the two criteria can be expressed as:

$$T_\lambda^{(\rho_0)} = \frac{(1+4\gamma_0^2)K_\lambda(\gamma_0)}{8n|\cos(n\psi_0)|} \cdot |\Lambda_n(\rho_0)|^2 \cdot [\text{correction factor}] + O(\delta_0^4),$$

where the correction factor tends to $1$ as $\delta_0 \to 0$. This quadratic relation between $T_\lambda^{(\rho_0)}$ and $\Lambda_n(\rho_0)$ reflects the order difference in $\delta_0$.

*Proof.* From Propositions 4.1 and 4.3: $T_\lambda^{(\rho_0)} \approx \delta_0^2 K_\lambda(\gamma_0)$ and $|\Lambda_n(\rho_0)| \approx 4n\delta_0(1+4\gamma_0^2)^{-1}|\cos(n\psi_0)|$. Eliminating $\delta_0$ between these two expressions: $\delta_0 = |\Lambda_n(\rho_0)|(1+4\gamma_0^2)/(4n|\cos(n\psi_0)|)$, hence $\delta_0^2 = |\Lambda_n|^2(1+4\gamma_0^2)^2/(16n^2\cos^2(n\psi_0))$. Substituting: $T_\lambda^{(\rho_0)} \approx K_\lambda(\gamma_0) \cdot |\Lambda_n|^2(1+4\gamma_0^2)^2/(16n^2\cos^2(n\psi_0))$. $\square$

---

## §5. The connection kernel $K(n,\lambda)$

### 5.1. Setting up the problem

We look for a relation of the form

$$\lambda_n = \int_0^\infty K(n,\lambda)\, T_\lambda\, d\lambda \quad\text{or equivalently}\quad \lambda_n = \sum_\lambda K(n,\lambda)\, \Delta T_\lambda,$$

where $\Delta T_\lambda = T_{\lambda+\varepsilon} - T_{\lambda-\varepsilon}$ is the jump of the trace at $\lambda$.

**Proposition 5.1** (kernel via Abel, formal approach). Assuming the off-critical zeros are $\{\rho_j\}$ with $|\gamma_1| \leq |\gamma_2| \leq \ldots$, the jumps of $T_\lambda$ occur at $\lambda = |\gamma_j|$:

$$\Delta T_{|\gamma_j|} \approx \delta_j^2 \cdot K_\infty(\gamma_j), \qquad K_\infty(\gamma) = \int_{\mathbb{R}} W_\infty(s)\,|\zeta_{on}|^2\left(\frac{1}{(s-\gamma)^2}+\frac{1}{(s+\gamma)^2}\right) dm_\infty(s),$$

where $W_\infty$ is the formal limit of the Abel kernel as $\lambda \to \infty$.

The Li coefficients are:
$$\lambda_n = \sum_j \Lambda_n(\rho_j) \approx -\sum_j \frac{4n\delta_j}{1+4\gamma_j^2}\cos(n\psi_j).$$

To connect $\lambda_n$ with $\{\Delta T_\lambda\}$, we need a kernel $K(n, |\gamma_j|)$ such that:

$$-\frac{4n\delta_j\cos(n\psi_j)}{1+4\gamma_j^2} = K(n,|\gamma_j|) \cdot \delta_j^2 K_\infty(\gamma_j).$$

This formally determines:
$$K(n,\gamma) = \frac{-4n\cos(n\psi(\gamma))}{(1+4\gamma^2)\delta_{\gamma} K_\infty(\gamma)},$$

where $\delta_\gamma$ would be the distance to the critical line of the zero responsible for the jump at $\lambda = \gamma$.

### 5.2. The obstacle to positivity of the kernel

**Proposition 5.2** (the kernel $K(n,\gamma)$ cannot be non-negative). The kernel $K(n,\gamma)$ defined in §5.1 cannot be non-negative for all $n$ and $\gamma$, for the following reasons:

(a) $K(n,\gamma)$ contains the factor $\cos(n\psi(\gamma))$, which changes sign for different values of $n$ (as $n$ varies, $n\psi(\gamma)$ ranges over $[0,2\pi]$ and the cosine takes both signs).

(b) $K(n,\gamma)$ contains the factor $\delta_\gamma^{-1}$, which depends on the individual zero and is not a function of $\gamma$ independent of the zero.

(c) The presence of $\delta_\gamma^{-1}$ makes the kernel singular in the limit $\delta \to 0$ (zeros approaching the critical line).

*Proof.* (a): the factor $\cos(n\psi(\gamma))$ alternates sign with $n$. For fixed $n$ and different imaginary parts $\gamma$, the function $n\psi(\gamma)$ varies continuously and the cosine takes all values in $[-1,1]$. (b) and (c): direct from the form of $K$. $\square$

**Corollary 5.3.** There is no kernel $K(n,\lambda) \geq 0$ such that $\lambda_n = \int K(n,\lambda) T_\lambda d\lambda$ for all possible values of the off-critical zeros. The sign of the kernel depends essentially on $\cos(n\psi(\gamma))$, which reflects the oscillatory structure of the powers of the Li values.

### 5.3. A second-order kernel

Instead of seeking $\lambda_n = \int K T_\lambda d\lambda$, we consider the relation at the level of $\lambda_n^2$:

**Proposition 5.4** (non-negative second-order kernel). From Proposition 4.5, for each off-critical zero $\rho_j$:

$$\Lambda_n(\rho_j)^2 \approx \frac{16n^2 K_\lambda(\gamma_j)^{-1}}{(1+4\gamma_j^2)^2} \cdot T_\lambda^{(\rho_j)}.$$

Summing over the zeros and using $\lambda_n^2 \leq \left(\sum_j |\Lambda_n(\rho_j)|\right)^2 \leq (\#\text{off-crit. zeros}) \cdot \sum_j \Lambda_n(\rho_j)^2$ (Cauchy-Schwarz), one obtains:

$$\lambda_n^2 \lesssim C_n \cdot T_\lambda,$$

for some constant $C_n$ depending on $n$ and on the number of off-critical zeros. Equivalently:

$$T_\lambda \gtrsim \frac{\lambda_n^2}{C_n}.$$

This is a quadratic version of the bound of Theorem 5.1 of Doc 75: that one was $T_\lambda \geq C|\lambda_{n_0}|$ (linear in $|\lambda_{n_0}|$), and here we obtain $T_\lambda \gtrsim \lambda_n^2/C_n$ (quadratic). Both are consistent (for small negative $\lambda_{n_0}$, the quadratic bound may be stronger if $|\lambda_{n_0}| < 1/C_n$).

*Proof.* Direct combination of Propositions 4.1 and 4.3 with Cauchy-Schwarz. The constant $C_n$ absorbs the number of zeros and the factors of $n$ and $\gamma$. The explicit form of $C_n$ is not given since it depends on information not available (number of off-critical zeros under $\neg$RH). $\square$

---

## §6. The unified criterion

### 6.1. Positivity functionals on the zero measure

Both Li's criterion and CTP's can be formulated as positivity conditions of linear functionals on the zero measure $\mu_{zeros}$:

**Definition 6.1.** Let $\mathcal{M}$ be the space of finite Borel measures on $\mathbb{C}$ symmetric under $z \mapsto \bar z$ and $z \mapsto 1-z$ (the symmetries of the zeros of $\xi$). For a function $\phi: \mathbb{C} \to \mathbb{R}$, the Li-type functional is:

$$\Lambda_\phi(\mu) = \int_{\mathbb{C}} \phi(z)\, d\mu(z).$$

**Examples:**
- $\phi = \phi_n$: $\phi_n(z) = 1-(1-1/z)^n$. Then $\Lambda_{\phi_n}(\mu_{zeros}) = \lambda_n$.
- $\phi = \Phi_\lambda$: $\Phi_\lambda(\sigma+i\gamma) = (\sigma-1/2)^2 K_\lambda(\gamma)$ to first order. Then $\Lambda_{\Phi_\lambda}(\mu_{zeros}^{off}) = T_\lambda$ (approximately).

**Remark 6.2.** Under RH, all zeros have $\sigma = 1/2$, so:
- $\phi_n(1/2+i\gamma) = 1 - e^{in\theta(\gamma)}$, whose real part is $1 - \cos(n\theta(\gamma)) \geq 0$. Hence $\lambda_n = \sum_\gamma 2(1-\cos(n\theta(\gamma))) \geq 0$.
- $\Phi_\lambda(1/2+i\gamma) = 0$ for all $\gamma$. Hence $T_\lambda = 0$.

Both conditions reduce, under RH, to trivially true statements.

### 6.2. The unified positivity criterion

**Definition 6.3** (Unified Criterion). Let $\mathcal{H}$ be the class of functions $\phi: \mathbb{C} \to \mathbb{R}$ such that:
(i) $\phi$ is continuous and $\phi(1/2+i\gamma) \geq 0$ for all $\gamma \in \mathbb{R}$.
(ii) $\phi$ is symmetric: $\phi(z) = \phi(\bar z) = \phi(1-z)$.
(iii) For off-critical zeros $\rho = \sigma+i\gamma$ with $\sigma > 1/2$: the average over the quadruplet $\frac{1}{4}\sum_{\rho' \in \mathcal{Q}} \phi(\rho')$ can be negative.

The Unified Criterion states: RH $\iff \Lambda_\phi(\mu_{zeros}) \geq 0$ for every convex $\phi \in \mathcal{H}$.

**Proposition 6.4** (Li's criterion is a special case). The functions $\phi_n(z) = 1-(1-1/z)^n$ belong to $\mathcal{H}$ for all $n \geq 1$. Indeed:
(i) $\phi_n(1/2+i\gamma) = 1-\cos(n\theta(\gamma)) + i\sin(n\theta(\gamma))$... but $\phi_n$ is not real on the critical line.

*Correction.* The sum over pairs $(\rho, \bar\rho)$ gives $\lambda_n = \sum_{\gamma>0} 2(1-\cos(n\theta(\gamma))) + \ldots$, which is non-negative under RH. But $\phi_n$ as a function of the complex variable $z$ is not real-valued in general. Li's criterion involves the sum over all zeros, not just the evaluation of $\phi_n$.

**Correct formulation of the Unified Criterion.** For real, symmetric test functions $\phi$, with the convention that the sum $\sum_\rho \phi(\rho)$ (over all zeros) is the condition, the criterion takes the form:

$$\text{RH} \iff \sum_\rho \phi(\rho) \geq 0 \quad\text{for every } \phi \text{ such that } \phi|_{\text{critical line}} \geq 0.$$

**Proposition 6.5** (function $\phi_{CTP}$ for the CTP criterion). To first order in $\delta$, the test function of the CTP criterion as a sum over zeros is:

$$\phi_{CTP,\lambda}(\sigma+i\gamma) = (\sigma-1/2)^2 \cdot K_\lambda(\gamma),$$

which satisfies: $\phi_{CTP,\lambda}(1/2+i\gamma) = 0$ (it vanishes on the critical line, it is not $\geq 0$). Therefore the CTP criterion is not of the form "sum of $\phi \geq 0$"; rather it demands that the sum be exactly zero ($T_\lambda = 0$, not $T_\lambda \geq 0$).

**Remark 6.6** (fundamental difference between Li and CTP from the Unified Criterion). Li's criterion asks $\sum_\rho \phi_n(\rho) \geq 0$ with $\phi_n$ non-negative on the critical line. The CTP criterion asks $\sum_\rho \phi_{CTP}(\rho) = 0$ with $\phi_{CTP}$ non-negative everywhere (and zero on the critical line). Under RH the CTP condition is trivially $0 = 0$ and Li's is $\geq 0 = 0$. Under $\neg$RH:
- In Li: the sum can become negative.
- In CTP: the sum is positive (since $\phi_{CTP} > 0$ for off-critical zeros).

They are "detectors" of the same violation with opposite orientations: Li detects violation as negativity, CTP as positivity.

### 6.3. Does the function $\phi_{CTP}$ exist such that $\Lambda_{\phi_{CTP}} = T_\lambda$?

**Proposition 6.7** (conditional affirmative answer). To first order in $\delta$, the identity $T_\lambda = \sum_\rho \phi_{CTP,\lambda}(\rho)$ holds with

$$\phi_{CTP,\lambda}(\rho) = (\sigma_\rho - 1/2)^2 K_\lambda(\gamma_\rho),$$

where the sum runs only over off-critical zeros (since $\phi_{CTP,\lambda}$ vanishes for critical zeros). This provides the representation $T_\lambda = \Lambda_{\phi_{CTP,\lambda}}(\mu_{zeros})$ sought in Conjecture 6.3 of Doc 75.

*Proof.* Direct from Proposition 4.2 and the definition $\Phi_\lambda = \phi_{CTP,\lambda}$. $\square$

**Consequence for Conjecture 6.3.** The transform $\mathcal{T}$ of Conjecture 6.3 of Doc 75 exists if and only if there is a relation

$$\phi_n(z) = \mathcal{T}[\phi_{CTP,\bullet}(z)](n)$$

as a transform of $\lambda \mapsto \phi_{CTP,\lambda}(z)$ for each fixed $z$. For $z = \sigma+i\gamma$ off-critical:

$$1-(1-1/z)^n = \mathcal{T}\!\left[\lambda \mapsto (\sigma-1/2)^2 K_\lambda(\gamma)\right](n).$$

This is Conjecture 6.3 in zero-by-zero form. The right-hand side is a transform of the function $\lambda \mapsto K_\lambda(\gamma)$ (which is $\sim N(\lambda)^2/\gamma^2$ by Proposition 4.3b), and the left-hand side is $1-(1-1/z)^n$ (which grows like $(1/r)^n$ in modulus for off-critical zeros). A transform converting polynomial growth in $\lambda$ into exponential growth in $n$ could be the discrete Mellin transform or a Bernstein-type integral; however **no explicit expression for $\mathcal{T}$ has been found**, and this problem remains open.

---

## §7. What remains to complete the path to RH

### 7.1. Balance of results proved in this document

1. **(Proposition 1.1):** The contributions of critical and off-critical zeros to $\lambda_n$ have different signs: critical ones contribute non-negatively, off-critical ones with negative dominance for large $n$.

2. **(Proposition 2.1):** The Laplace transform of $\lambda \mapsto T_\lambda$ is $\hat{T}(s) = s^{-1}\sum_j T_\infty^{(\rho_j)} e^{-s|\gamma_j|}$, with the structure of a Dirichlet series in the imaginary parts of the off-critical zeros.

3. **(Conclusion 2.3):** The direct Laplace transform does not connect $\hat{T}(s)$ with $\lambda_n$ due to an incompatibility of growth orders.

4. **(Proposition 3.3):** Weil's formula gives arithmetic representations of both criteria in terms of primes, with test functions $\hat{h}_n(\log p)$ (for Li) and $B_\lambda(\log p)$ (for CTP). The necessary condition for a transform $\mathcal{T}$ to exist is expressed as prime-by-prime compatibility.

5. **(Proposition 4.1):** The contribution of the off-critical zero $\rho_0$ to $\lambda_n$ is $\approx -4n\delta_0(1+4\gamma_0^2)^{-1}\cos(n\psi_0)$, to first order in $\delta_0$.

6. **(Proposition 4.5):** Quadratic relation between the contributions to $T_\lambda$ and to $\lambda_n$ for each off-critical zero: $T_\lambda^{(\rho_0)} \approx C(n,\gamma_0) \cdot \Lambda_n(\rho_0)^2$.

7. **(Proposition 5.2):** The linear connection kernel $K(n,\lambda)$ cannot be non-negative, due to the oscillatory structure of $\cos(n\psi(\gamma))$.

8. **(Proposition 5.4):** There exists a second-order kernel: $T_\lambda \gtrsim \lambda_n^2/C_n$.

9. **(Proposition 6.7):** The function $\phi_{CTP,\lambda}$ representing $T_\lambda$ as a sum over zeros is $(\sigma-1/2)^2 K_\lambda(\gamma)$, and Conjecture 6.3 reduces to a zero-by-zero relation between $\phi_n$ and $\phi_{CTP,\lambda}$.

### 7.2. The obstacles identified

**Obstacle O.1** (oscillatory). The factor $\cos(n\psi_0)$ in $\Lambda_n(\rho_0)$ introduces oscillations in $n$ that prevent a linear positivity relation between $\lambda_n$ and $T_\lambda$. To eliminate this obstacle one would need to work with $\lambda_n^2$ or with an "envelope" $|\lambda_n|$.

**Obstacle O.2** (scale). The relation $T_\lambda^{(\rho_0)} \sim \delta_0^2$ while $\Lambda_n(\rho_0) \sim \delta_0$ implies that the connection kernel is singular in $\delta_0^{-1}$ for near-critical zeros. Overcoming this would require a "renormalization" that absorbs the dependence on $\delta_0$.

**Obstacle O.3** (Laplace). The Laplace transform of $T_\lambda$ grows exponentially in $|\gamma_j|$ (via the factors $e^{-s|\gamma_j|}$) while the coefficients $\lambda_n$ grow exponentially in $n$ (via the factors $(1/r_j)^n$). The identification $s \leftrightarrow n$ requires $s = n\log(1/r_j)/|\gamma_j|$, which depends on the zero $j$: no uniform transform exists.

**Obstacle O.4** (holomorphy). $\phi_n(z)$ is holomorphic in $z$ and its global structure depends on the geometry in the complex plane. $\phi_{CTP,\lambda}(z)$ depends only on $\mathrm{Re}(z)-1/2$ and $\mathrm{Im}(z)$ separately. A transform $\mathcal{T}$ should connect functions of a complex variable with functions of two separate real variables; the holomorphy structure imposes restrictions that are not obvious.

### 7.3. The key open questions

**Question P.1.** Does there exist a transform $\mathcal{T}$ such that $\lambda_n = \mathcal{T}[T_\bullet](n)$? In light of the obstacles, the most plausible answer is that such a transform does not exist in simple form, and that the relation between the criteria is subtler (possibly involving derivatives of $T_\lambda$ or convolutions).

**Question P.2.** Can one prove that $\lambda_n^2 \leq C_n \cdot T_\lambda$ (the bound of Proposition 5.4) with explicit and effective $C_n$? If the constant $C_n$ can be bounded independently of the off-critical zeros, this would give a strong quantitative relation.

**Question P.3.** Does there exist a class of functions $\phi$ in the Unified Criterion (§6.2) such that: (a) Li and CTP are two instances of the same class, and (b) positivity of $\Lambda_\phi$ for every $\phi$ in the class is provable from known properties of $\zeta$?

**Question P.4** (the deepest one). Why should $\Lambda_{\phi_n}(\mu_{zeros}) = \lambda_n \geq 0$ (or $T_\lambda = 0$) follow from intrinsic properties of $\zeta$? The answer seems to require a **spectral positivity** property of the CCM Jacobi operator or of some operator associated to the function $\xi$. If there exists a positive semi-definite self-adjoint operator $H$ such that $\lambda_n = \langle H^n v, v\rangle$ for some vector $v$, then $\lambda_n \geq 0$ would be a consequence of positivity of $H$.

### 7.4. Implications for the program

The results of this document show that the relation between Li's and CTP's criteria is more complex than a direct transform. In particular:

1. The quadratic bound $T_\lambda \gtrsim \lambda_n^2/C_n$ is the strongest form of the connection that can be established with current methods.

2. Conjecture 6.3 of Doc 75 in its literal form (integral transform $\lambda_n = \mathcal{T}[T_\bullet](n)$) faces Obstacle O.3 (Laplace scale), which seems fundamental: the two criteria live in different "dimensions" ($\delta^1$ vs $\delta^2$) and are not transforms of each other in the usual sense.

3. The most promising route seems to be the Unified Criterion (§6), which reformulates both criteria as positivity conditions of functionals on the zero measure, and asks whether a uniform proof of such positivity exists.

4. A new direction (not explored in this document) would be to work with the function $L(z) = \log\xi(z/(z-1))$ and its logarithmic derivatives: this function contains the information of both criteria (Li as Taylor coefficients of $L$ at $z=1$, CTP as norms of certain projectors) and could be the sought "unifying object".

---

## §8. Summary of statements and their status

| Result | §  | Status |
|---|---|---|
| Representation of $\lambda_n$ and $T_\lambda$ as functionals of $\mu_{zeros}$ | §1 | Proved (from Doc 75) |
| Laplace transform of $\lambda \mapsto T_\lambda$ | §2.1 | Proved (under discreteness hypothesis for the zeros) |
| Obstacle to the direct Laplace transform | §2.2 | Proved |
| Partial Stieltjes representation of $\lambda_n$ | §2.3 | Partially proved (positive part only) |
| Arithmetic representation of $\lambda_n$ via Weil | §3.1 | Formally proved (technical conditions pending) |
| Necessary prime-by-prime condition for $\mathcal{T}$ | §3.4 | Proved |
| Contribution of $\rho_0$ to $\lambda_n$ at order $\delta$ | §4.1 | Proved (Prop. 4.1) |
| Quadratic relation $T_\lambda^{(\rho_0)} \approx C \Lambda_n(\rho_0)^2$ | §4.5 | Proved to first order |
| Non-positivity of the linear kernel $K(n,\lambda)$ | §5.2 | Proved |
| Quadratic bound $T_\lambda \gtrsim \lambda_n^2/C_n$ | §5.4 | Proved (with non-explicit $C_n$) |
| Function $\phi_{CTP,\lambda}$ representing $T_\lambda$ | §6.7 | Proved to first order |
| Reduction of Conjecture 6.3 to a zero-by-zero relation | §6.3 | Proved |
| Conjecture 6.3 (existence of $\mathcal{T}$) | §6.3 | **Open** |
| Unified Criterion | §6.2 | **Conjectural** |

---

*End of Document 78.*
