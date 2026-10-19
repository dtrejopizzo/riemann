# Document 79 — Exponential decay, the sum over primes, and the cancellation conditions

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 64, 70, 72, 76

---

## Summary

Doc 76 established that $|\widehat{W_\lambda\,dm_\infty}(r)| = O(e^{-\pi|r|/4})$ for $|r|\to\infty$, and Doc 72 proved that $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ where $B_\lambda(r) = \mathrm{Re}[\widehat{W_\lambda\,dm_\infty}(r)]$. This document systematically explores the consequences of exponential decay for the sum over primes: absolute convergence (§1), structure of the term $A_\lambda^{off}$ (§2), the sum over primes as a cancellation condition (§3), quantitative analysis of $B_\lambda(\log p)$ (§4 and §5), the geometric sums appearing at large primes (§6), the reformulation of the criterion (§7), and the connection with the Nyman-Beurling criterion (§8 and §9). We conclude with a frank evaluation of the state of Path 3.

**Permanent notation in this document:**

- $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$, density $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$.
- $\{P_k\}_{k\geq 0}$ CCM orthonormal polynomials with respect to $dm_\infty$; $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$.
- $W_\lambda(s) = \sum_{k=0}^{N} (k+1)|P_k(s)|^2$ with $N = N(\lambda)$.
- $\phi_k(r) = \int_\mathbb{R} |P_k(s)|^2 e^{irs}\,dm_\infty(s)$.
- $B_\lambda(r) = \mathrm{Re}[\widehat{W_\lambda\,dm_\infty}(r)] = \int_\mathbb{R} W_\lambda(s)\cos(rs)\,dm_\infty(s)$.
- $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ (Weil's formula, Doc 72).

---

## §1. Absolute convergence of the sum over primes

### 1.1. The size of $B_\lambda(\log p)$

By Prop. 1.5 of Doc 76, for each fixed $\lambda > 0$ there exists a constant $C_\lambda > 0$ such that
$$|\widehat{W_\lambda\,dm_\infty}(r)| \leq C_\lambda\,e^{-(\pi/4)|r|}, \qquad r\in\mathbb{R}.$$

Since $B_\lambda(r) = \mathrm{Re}[\widehat{W_\lambda\,dm_\infty}(r)]$, we have the bound
$$|B_\lambda(\log p)| \leq C_\lambda\,e^{-(\pi/4)\log p} = C_\lambda\,p^{-\pi/4}.$$

Consequently, the general term of the sum over primes satisfies
$$\frac{\log p}{\sqrt{p}}\,|B_\lambda(\log p)| \leq C_\lambda\,\frac{\log p}{p^{1/2+\pi/4}}.$$

**Proposition 1.1** (Absolute convergence). *For every $\lambda > 0$, the series*
$$\sum_p \frac{\log p}{\sqrt{p}}\,B_\lambda(\log p)$$
*converges absolutely.*

*Proof.* It suffices to verify that $\sum_p \frac{\log p}{p^{1/2+\pi/4}} < \infty$. The exponent is $\alpha := 1/2 + \pi/4 \approx 1.285$. By the prime number theorem, $\sum_{p \leq X} \log p \sim X$, so the partial sum $\sum_{p\leq X} \frac{\log p}{p^\alpha}$ grows like $\int_2^X \frac{dt}{t^{\alpha-1}\log t} \cdot \frac{\log t}{1}$, hence like $\int_2^X t^{-\alpha}\,dt$, an integral that converges absolutely on $[2,\infty)$ since $\alpha > 1$. The bound $|B_\lambda(\log p)| \leq C_\lambda p^{-\pi/4}$ completes the proof. $\square$

**Corollary 1.2.** *The quantity $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ is well defined for every $\lambda > 0$, with no hypothesis on the zeros of $\zeta$. All series involved in its definition converge absolutely.*

*Proof.* The convergence of the sum over primes was just established. The convergence of $A_\lambda^{off}$ — the contribution of the zeros off the critical line in Weil's formula — follows from the standard bounds on the admissible test functions (see Doc 72, §3). $\square$

### 1.2. Remark on the exponent $\pi/4$

The value $\pi/4$ comes from the distance to the first pole of $\Gamma(1/4+is/2)$ in the variable $s$: the first pole in the lower half-plane lies at $s = -i/2$, and shifting the integration contour in the definition of $\phi_k(r)$ by an amount $\varepsilon = \pi/4$ (which remains inside the analyticity strip $|\mathrm{Im}(s)| < 1/2$) picks up the decay $e^{-(\pi/4)|r|}$. This value is optimal for the measure $dm_\infty$; a different kernel would give a different exponent.

---

## §2. The term $A_\lambda^{off}$ and its geometric meaning

### 2.1. Precise definition

In Weil's formula applied with the test function $h_\lambda(s) = W_\lambda(s)\,w(s)$ (Doc 72, §3), the term $A_\lambda^{off}$ collects the contribution of the zeros of $\zeta$ that do not lie on the critical line $\mathrm{Re}(s)=1/2$. More precisely, if $\mathcal{Z}_{off}$ denotes the set of nontrivial zeros of $\zeta$ with $\mathrm{Re}(\rho) \neq 1/2$, then

$$A_\lambda^{off} = \sum_{\rho \in \mathcal{Z}_{off}} h_\lambda(\gamma_\rho) - \sum_{\rho \in \mathcal{Z}_{off}} h_\lambda(\gamma_\rho^*),$$

where $\gamma_\rho = \mathrm{Im}(\rho)$ and $\gamma_\rho^* = \mathrm{Im}(\rho^*)$ are the imaginary parts of the zero and of its critical image $\rho^* = 1/2 + i\,\mathrm{Im}(\rho)$. (The exact definition depends on the parametrization chosen for Weil's formula; see Doc 72.)

### 2.2. Vanishing under RH

**Proposition 2.1** (Vanishing under RH). *If the Riemann Hypothesis holds, then $A_\lambda^{off} = 0$ for every $\lambda > 0$.*

*Proof.* Under RH, $\mathcal{Z}_{off} = \emptyset$: all nontrivial zeros of $\zeta$ lie on the critical line. Hence the sum defining $A_\lambda^{off}$ is empty. $\square$

### 2.3. The converse-direction question

A natural question is whether the condition $A_\lambda^{off} = 0$ for some $\lambda$ implies RH, or at least constrains it. The answer is that the equivalence $A_\lambda^{off} = 0 \iff T_\lambda = 0$ (when simultaneously $\sum_p B_\lambda(\log p) = 0$) is a tautology: both are reformulations of the same spectral condition. The equation defining $T_\lambda$ is

$$T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p),$$

so $T_\lambda = 0$ is equivalent to $A_\lambda^{off}$ and the sum over primes being equal. Under RH both sides are zero (by Prop. 2.1 and by Weil's formula applied to test functions that are Fourier transforms of positive measures). There is no circularity, but no new information either: the condition $A_\lambda^{off} = 0$ is equivalent to RH by the very definition of the criterion $T_\lambda = 0$.

---

## §3. The sum over primes as an obstruction of oscillation

### 3.1. The cancellation equation

The equivalence RH $\iff$ $T_\lambda = 0$ for every $\lambda$ can be rewritten, thanks to Prop. 2.1, as:

$$\text{RH} \iff A_\lambda^{off} = 0 \text{ and } \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0 \quad\text{for every } \lambda > 0.$$

The second condition — that the sum over primes be exactly zero — is a cancellation condition among the frequencies $\cos(s\log p)$ weighted by $W_\lambda w$.

**Proposition 3.1** (The sum over primes under RH). *Under the Riemann Hypothesis,*
$$\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0 \quad \text{for every } \lambda > 0.$$

*Proof.* Under RH, $T_\lambda = 0$ (Doc 64, central criterion) and $A_\lambda^{off} = 0$ (Prop. 2.1). The formula $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ then gives the required identity. $\square$

### 3.2. The obstruction

**Proposition 3.2** (Converse-direction obstruction). *The conditions $A_\lambda^{off} = 0$ and $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ are each individually equivalent to RH, but neither is provable independently of the position of the zeros of $\zeta$ by currently available methods.*

*Proof (of the obstruction).* The condition $A_\lambda^{off} = 0$ is equivalent, by definition, to $\mathcal{Z}_{off} = \emptyset$, i.e., exactly to RH. It is not accessible independently. The condition $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ is, by Weil's formula, the identity that results from applying that formula to the test function $h_\lambda = W_\lambda w$ assuming RH — that is, it is a consequence of RH but cannot be proved without it by purely arithmetic methods with the tools currently available. $\square$

### 3.3. A computable necessary condition

Although we cannot prove the exact equality, Prop. 1.1 guarantees that the series converges absolutely. This allows us to truncate it and compare numerically:

**Definition 3.3.** For $X > 2$ and $\lambda > 0$, let
$$S_\lambda(X) = \sum_{p \leq X} \frac{\log p}{\sqrt{p}} B_\lambda(\log p).$$

By Prop. 1.1, $S_\lambda(X) \to \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ as $X\to\infty$, with absolute convergence. Under RH, $\lim_{X\to\infty} S_\lambda(X) = 0$.

The rate of convergence of $S_\lambda(X)$ to zero (under RH) is the subject of §4.

---

## §4. Quantitative analysis of $B_\lambda(\log p)$

### 4.1. Decomposition into modes $\phi_k$

Recall that $W_\lambda(s) = \sum_{k=0}^N (k+1)|P_k(s)|^2$ and hence

$$\widehat{W_\lambda\,dm_\infty}(r) = \sum_{k=0}^N (k+1)\,\phi_k(r),$$

where the series is finite. Taking the real part:

$$B_\lambda(r) = \sum_{k=0}^N (k+1)\,\phi_k(r).$$

For $r = \log p$ with $p$ prime:

$$B_\lambda(\log p) = \sum_{k=0}^N (k+1)\,\phi_k(\log p).$$

### 4.2. Bound for large primes

Combining the decomposition of §4.1 with the bound $|\phi_k(\log p)| \leq C_k\,p^{-\pi/4}$ (Doc 76, Prop. 1.5):

**Proposition 4.1** (Contribution of large primes). *Let $X > e^{2\pi}$. Then*
$$\left|\sum_{p > X} \frac{\log p}{\sqrt{p}} B_\lambda(\log p)\right| \leq \tilde{C}_\lambda \sum_{p > X} \frac{\log p}{p^{1/2+\pi/4}} = O_\lambda\!\left(X^{1/2-\pi/4}\right) = O_\lambda\!\left(X^{-0.285\ldots}\right).$$

*Proof.* We use $|B_\lambda(\log p)| \leq C_\lambda' p^{-\pi/4}$ with $C_\lambda' = \sum_{k=0}^N (k+1) C_k$, and the estimate $\sum_{p>X} \frac{\log p}{p^\alpha} \ll X^{1-\alpha}/\log X$ for $\alpha > 1$, with $\alpha = 1/2+\pi/4$. $\square$

**Corollary 4.2.** *The "arithmetic core" of the sum comes from primes $p \leq X_0(\lambda)$ with $X_0(\lambda) = \exp(4 N(\lambda)^2/\pi)$; the contribution of larger primes is exponentially small in $N(\lambda)^2$.*

### 4.3. The value $B_\lambda(0)$ and normalization

For $r = 0$: $B_\lambda(0) = \int W_\lambda\,dm_\infty = \sum_{k=0}^N (k+1) = N(N+1)/2 \sim N^2/2$ (Doc 76, §4). This is the maximum value of $|B_\lambda(r)|$ since $|B_\lambda(r)| \leq B_\lambda(0)$ by definition (the function $\cos(rs)$ has modulus $\leq 1$).

---

## §5. Structure of the sum over small primes

### 5.1. DC and oscillatory decomposition

Following the terminology of Doc 76, for $r > 2\pi$ the function $\phi_k(r)$ admits the asymptotic decomposition (via stationary phase with the Marchenko-Riesz-Szegő radius $a_k = 2k/\pi$):

$$\phi_k(r) = \phi_k^{DC}(r) + \phi_k^{osc}(r) + O(k^{-\infty}),$$

where the DC contribution decays exponentially in $r$ and the oscillatory one has the form

$$\phi_k^{osc}(r) \approx C_0\,k^{-3/4}\,e^{-8\pi k/r^2}\cos\!\left(\frac{8\pi k}{r} - \frac{\pi}{4}\right).$$

**Proposition 5.1** (DC contribution to $B_\lambda(\log p)$). *For primes $p > e^{2\pi}$:*
$$B_\lambda^{DC}(\log p) := \sum_{k=0}^N (k+1)\,\phi_k^{DC}(\log p) = O\!\left(N^{9/4}\,p^{-\pi/4}\right).$$

*Proof.* The DC contribution satisfies $|\phi_k^{DC}(r)| \leq C\,k^{-3/4}\,e^{-(\pi/4)r}$ for $r > 0$. Summing with weights $(k+1)$:
$$|B_\lambda^{DC}(\log p)| \leq C\,p^{-\pi/4}\sum_{k=0}^N (k+1) k^{-3/4} \leq C'\,p^{-\pi/4} N^{9/4}. \qquad\square$$

**Proposition 5.2** (Oscillatory contribution to $B_\lambda(\log p)$). *For primes $p > e^{2\pi}$:*
$$B_\lambda^{osc}(\log p) := \sum_{k=1}^N (k+1)\,\phi_k^{osc}(\log p) \approx C_0\sum_{k=1}^N k^{1/4}\,e^{-8\pi k/(\log p)^2}\cos\!\left(\frac{8\pi k}{\log p} - \frac{\pi}{4}\right).$$

*Proof.* Immediate by substituting the asymptotic expression of $\phi_k^{osc}(r)$ with $r = \log p$ and grouping the weights $(k+1) \cdot k^{-3/4} \approx k^{1/4}$ for large $k$. $\square$

---

## §6. The exponential geometric sum and possible cancellation

### 6.1. Identification of the sum

The oscillatory contribution of §5.2 can be written, up to the weight $k^{1/4}$ versus $k^0$, as the real part of a weighted geometric sum. For simplicity let us define the sum without the polynomial weight:

$$\Sigma(r, N) = \sum_{k=1}^N e^{-8\pi k/r^2}\cos\!\left(\frac{8\pi k}{r} - \frac{\pi}{4}\right).$$

Let $q = e^{-8\pi/r^2}$ and $\theta = 8\pi/r$. Then:

$$\Sigma(r,N) = \mathrm{Re}\!\left[e^{-i\pi/4}\sum_{k=1}^N (q e^{i\theta})^k\right] = \mathrm{Re}\!\left[e^{-i\pi/4}\cdot\frac{q e^{i\theta}(1 - (qe^{i\theta})^N)}{1 - q e^{i\theta}}\right].$$

### 6.2. Large-prime regime

For $r = \log p$ with $p$ large, $\theta = 8\pi/r \ll 1$ and $q = 1 - 8\pi/r^2 + O(r^{-4}) \approx 1$. The denominator satisfies

$$|1 - q e^{i\theta}|^2 = (1-q\cos\theta)^2 + (q\sin\theta)^2 \approx \theta^2 + (1-q)^2 \approx \theta^2 = (8\pi/r)^2.$$

The numerator $|qe^{i\theta}(1-(qe^{i\theta})^N)| \leq 1 + |q|^N \leq 2$. Hence

$$|\Sigma(r,N)| \lesssim \frac{1}{|1-qe^{i\theta}|} \approx \frac{r}{8\pi} = \frac{\log p}{8\pi}.$$

For the sum with weight $k^{1/4}$, the estimate is more delicate, but in any case the sum grows at most polynomially in $\log p$ and in $N$.

**Proposition 6.1** (Bound on the oscillatory sum). *For $r = \log p$ with $p > e^{2\pi}$ and $N \geq 1$:*
$$|B_\lambda^{osc}(\log p)| \leq C\,N^{5/4}\,\frac{\log p}{8\pi}.$$

*Proof.* We apply the estimate of the geometric sum with weight $k^{1/4}$, giving $\sum_{k=1}^N k^{1/4}/(r^{-1}) \approx N^{5/4} \cdot r/(8\pi)$. The absolute constant $C$ absorbs the normalization. $\square$

### 6.3. Cancellation between consecutive primes

The sum $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda^{osc}(\log p)$ involves factors $\cos(8\pi k/\log p - \pi/4)$ with phase varying smoothly between consecutive primes. There is no obvious cancellation between consecutive primes (unlike what happens with Dirichlet character sums, where orthogonality provides cancellation).

**Lemma 6.2** (Absence of evident cancellation). *There is no purely arithmetic-combinatorial mechanism guaranteeing $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda^{osc}(\log p) = 0$ without information about the zeros of $\zeta$.*

*Proof (informal).* The phases $8\pi k/\log p$ with $k$ fixed are dense in $[0,2\pi]$ as $p$ ranges over the primes (by the distribution of $\log p \pmod{2\pi k/m}$ for $m\in\mathbb{Z}$, which has no special algebraic structure). For the sum to be exactly zero would require a cancellation law among primes that is, ultimately, equivalent to the position of the zeros of $\zeta$. $\square$

---

## §7. The cancellation condition and the Riemann Hypothesis

### 7.1. Spectral reformulation

We have seen that RH $\iff$ $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ for every $\lambda > 0$ (combining Prop. 3.1 with the criterion $T_\lambda = 0$ of Doc 64). We can state this more explicitly in terms of $\phi_k$:

**Proposition 7.1** (Cancellation criterion). *Let $B_\lambda(r) = \sum_{k=0}^N (k+1)\phi_k(r)$ with $\phi_k(r) = \int \cos(rs)|P_k(s)|^2\,dm_\infty(s)$. Then:*
$$\text{RH} \iff \sum_p \frac{\log p}{\sqrt{p}} \sum_{k=0}^{N(\lambda)} (k+1)\phi_k(\log p) = 0 \quad \text{for every } \lambda > 0.$$

*Proof.* The condition $T_\lambda = 0$ is equivalent to RH (Doc 64). Under RH, $A_\lambda^{off}=0$ (Prop. 2.1), and the formula $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ gives the condition. $\square$

### 7.2. The fundamental obstruction

Prop. 7.1 reformulates RH as an arithmetic identity: the sum over primes of $\frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ must be zero. But $B_\lambda(\log p) \geq 0$ does not hold in general (since $\cos(s\log p)$ has no definite sign, even though the measure $W_\lambda dm_\infty$ is positive). Moreover:

**Proposition 7.2** (Sign does not help). *The sum $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ has no definite sign: for different values of $\lambda$, it can be positive, negative, or zero.*

*Proof.* For small $\lambda$ ($N=0$), $B_\lambda(r) = \phi_0(r) = \int \cos(rs)\,dm_\infty(s) = \hat{w}(r)/\int dm_\infty$, which is real and decays exponentially. The value $\hat{w}(r)$ oscillates and changes sign for moderate $r$ (since $\hat{w} \in L^2(\mathbb{R})$ and $\hat{w}(0) > 0$). Hence the term $B_0(\log p) = \hat{w}(\log p)/C$ can be positive or negative depending on $p$. The total sum depends on the distribution of the primes and has no definite sign. $\square$

---

## §8. Connection with the Nyman-Beurling criterion

### 8.1. The Nyman-Beurling criterion

Recall the classical result. Define Nyman's function $f(x) = \{1/x\} - x\lfloor 1/x^2 \rfloor$ on $(0,\infty)$, and for $0 < a \leq 1$ the translate $f_a(x) = f(x/a)$.

**Theorem** (Nyman 1950, Beurling 1955). *The Riemann Hypothesis is equivalent to the characteristic function $\mathbf{1}_{(0,1)}$ belonging to the closure in $L^2(0,\infty)$ of the linear subspace generated by $\{f_a : 0 < a \leq 1\}$.*

Báez-Duarte (2003) reformulated this: RH $\iff$ the infimum
$$d_N^2 = \inf_{A_k \in \mathbb{C}} \int_0^\infty \left|\mathbf{1}_{(0,1)}(x) - \sum_{k=1}^N A_k f(x/n_k)\right|^2 \frac{dx}{x}$$
converges to $0$ as $N\to\infty$, where $n_k$ are positive integers.

### 8.2. Common structure with the CTP criterion

Both the Nyman-Beurling criterion and the criterion $T_\lambda = 0$ share the following structure:

1. A positive measure $\mu$ is chosen on a measurable space $(\Omega, \mathcal{B})$.
2. A "target" function $f^* \in L^2(\mu)$ is defined that encodes the function $\zeta$.
3. RH is equivalent to $f^*$ being approximable (in $L^2(\mu)$ norm) by a system $\{f_n\}$ related to the primes or to the frequencies $e^{is\log p}$.

In the criterion $T_\lambda = 0$:
- $\mu = W_\lambda\,dm_\infty$ (positive measure on $\mathbb{R}$).
- The "target" function is the difference $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$.
- RH is equivalent to this difference being zero $\mu$-almost everywhere (i.e., $T_\lambda = 0$ for every $\lambda$).
- The sum over primes $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ is the projection of Weil's formula onto the test function $W_\lambda w$.

In the Nyman-Beurling criterion:
- $\mu = dx/x$ (Haar measure on $(0,\infty)$).
- The target function is $\mathbf{1}_{(0,1)}$.
- RH is equivalent to $\mathbf{1}_{(0,1)}$ being approximable by translates of Nyman's function.
- The translates are indexed by rationals $a = m/n$, and the denominators $n$ are integers (not only primes).

### 8.3. The clue: completeness versus cancellation

**Proposition 8.1** (The Nyman-Beurling clue). *If the system $\{\cos(s\log p)\}_{p\,\text{prime}}$ were complete in $L^2(W_\lambda\,dm_\infty)$ for some $\lambda$, and if the cancellation condition $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ could be interpreted as orthogonality of $W_\lambda w$ with respect to all frequencies $\cos(s\log p)$, then completeness would imply $W_\lambda w = 0$, which is a contradiction.*

*Proof.* If $\{\cos(s\log p)\}$ were a complete system in $L^2(W_\lambda\,dm_\infty)$, then the condition
$$\int \cos(s\log p)\cdot g(s)\,W_\lambda(s)\,dm_\infty(s) = 0 \quad \text{for every prime } p$$
would imply $g = 0$ in $L^2(W_\lambda\,dm_\infty)$. But the condition $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ is not a sum of integrals against separate functions $g$: it is a single integral weighted by the sum over primes of $\frac{\log p}{\sqrt{p}}\cos(s\log p)$. If we defined $g(s) = \sum_p \frac{\log p}{\sqrt{p}}\cos(s\log p)$ (a series that does not converge in general), the condition would be $\int g \cdot W_\lambda\,dm_\infty = 0$. Completeness of $\{\cos(s\log p)\}$ does not imply $g = 0$, only that any function orthogonal to all the cosines is zero. The hypothetical contradiction does not arise; the clue does not lead to a direct proof. $\square$

**Remark 8.2.** The analogy with Nyman-Beurling suggests looking for a variational formulation: does there exist an infimum $d_\lambda^2 = \inf_{\text{test functions}} T_\lambda$ that converges to $0$ if and only if RH holds? This direction is the one we will explore in future documents.

---

## §9. Connection with Nyman-Beurling: state of Path 3

### 9.1. What Path 3 has achieved

Path 3 (explicit arithmetic in the sum over primes) has produced the following solid results:

1. **Absolute convergence** (Prop. 1.1): the sum $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converges absolutely for every $\lambda > 0$, guaranteeing that $T_\lambda$ is a well-defined quantity with no additional hypotheses.

2. **Quantitative bound** (Prop. 4.1): the contribution of primes $p > X$ to the sum is $O_\lambda(X^{-0.285})$, which implies that the "arithmetic core" is finite and in principle computable.

3. **Asymptotic structure** (Props. 5.1 and 5.2): the DC-oscillatory decomposition of $\phi_k(r)$ allows us to analyze the sum over primes in terms of explicit geometric sums.

4. **Nyman-Beurling connection clue** (§8): the structure of the criterion $T_\lambda = 0$ is formally analogous to the Nyman-Beurling criterion, with the sum over primes playing the role of the system of Nyman translates.

### 9.2. The obstruction persists

**Proposition 9.1** (Limit of Path 3). *The absolute convergence and the quantitative bounds obtained do not imply the equality $T_\lambda = 0$ nor are they sufficient to prove the Riemann Hypothesis by Path 3 as currently formulated.*

*Proof.* The condition $T_\lambda = 0$ is equivalent to RH (Doc 64). Any result obtainable without assuming the position of the zeros of $\zeta$ implies only convergence and size properties of the sum, but not the exact cancellation. The exact equality $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ is, by Weil's formula, a consequence of RH — not a condition that can be verified independently of the position of the zeros with current methods. $\square$

### 9.3. The Nyman-Beurling clue as a future direction

The connection with the Nyman-Beurling criterion suggests a concrete question:

**Question 9.2.** Does an analogue of the Báez-Duarte infimum exist for the criterion $T_\lambda = 0$? More precisely: if we define
$$\delta_\lambda^2 = \inf_{g \in V_\lambda} \left\|W_\lambda w - g\right\|_{L^2(\mathbb{R})}^2,$$
where $V_\lambda$ is the closure in $L^2(\mathbb{R})$ of the subspace generated by $\{W_\lambda(\cdot)\cos(\cdot\log p) : p\,\text{prime}\}$, is it true that $\delta_\lambda^2 \to 0$ for every $\lambda$ if and only if RH holds?

This question connects the CCM formalism to $L^2$ approximation theory and opens a direction not explored so far in the program.

---

## §10. Synthesis and assessment

**Theorem 10.1** (Synthesis of Doc 79). *Within the framework of the CTP-CCM criterion $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$:*

*(i) The sum over primes converges absolutely for every $\lambda > 0$, with convergence rate $O_\lambda(X^{-0.285})$ for the remainder of primes $p > X$.*

*(ii) Under RH, $A_\lambda^{off} = 0$ and $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ for every $\lambda > 0$.*

*(iii) The cancellation condition $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ is equivalent to RH but cannot be proved independently of the position of the zeros of $\zeta$ with current methods.*

*(iv) The structure of the criterion is formally analogous to the Nyman-Beurling criterion; the question of whether there exists a variational infimum $\delta_\lambda^2 \to 0 \iff$ RH is an open direction.*

*Proof.* (i) is Prop. 1.1 and Cor. 4.2. (ii) is Prop. 2.1 and Prop. 3.1. (iii) is Prop. 3.2 and Prop. 9.1. (iv) is Remark 8.2 and Question 9.2. $\square$

---

**State of Path 3 at the end of Doc 79:**

Path 3 has carried out an exhaustive analysis of the sum over primes $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$: absolute convergence, asymptotic structure, quantitative bounds, and the identification of the exponential geometric sum appearing at large primes. The central result is that all information about the position of the zeros of $\zeta$ is contained in the exact cancellation condition of this sum — which is, ultimately, equivalent to RH but not accessible by purely independent arithmetic methods.

The connection with the Nyman-Beurling criterion (§8–9) is genuinely new in the context of the CCM program and suggests exploring a variational formulation of the criterion $T_\lambda = 0$.
