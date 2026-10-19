# Document 73 — Proof attempt: three attacks on $T_\lambda = 0$ and the fundamental obstacle

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 64, 70, 71, 72

---

## 1. The problem in its cleanest form

We have (Doc 64, Thm. 3.1):

$$\text{RH} \iff T_\lambda = 0 \;\text{ for all } \lambda > 0,$$

with

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\bigl(|\zeta(\tfrac{1}{2}+is)|^2 - |\zeta_{on}(\tfrac{1}{2}+is)|^2\bigr)\,dm_\infty(s).$$

To prove RH it suffices to prove $T_\lambda = 0$ for all $\lambda$.

We have: $W_\lambda \geq 0$ (Doc 63), $|\zeta|^2 - |\zeta_{on}|^2 \geq 0$ pointwise under $\neg$RH (from the Hadamard product, see §2 below), and $T_\lambda > 0$ under $\neg$RH. To prove RH we need an argument establishing $T_\lambda \leq 0$, or establishing $|\zeta|^2 = |\zeta_{on}|^2$, or any other route forcing $T_\lambda = 0$.

We present three attacks.

---

## 2. Verification: $|\zeta(1/2+is)|^2 \geq |\zeta_{on}(1/2+is)|^2$ pointwise

Before attacking, we establish the pointwise inequality that makes the problem hard.

Under $\neg$RH there exists at least one zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 > 1/2$. By the functional equation, off-critical zeros come in quadruplets $\{\sigma_0 \pm i\gamma_0,\, (1-\sigma_0) \pm i\gamma_0\}$. The construction of $\zeta_{on}$ replaces this quadruplet by the critical pair $\{1/2 \pm i\gamma_0\}$ (double multiplicity or simple pair, depending on convention).

The contribution of the off-critical quadruplet to the Hadamard ratio:

$$\frac{|\zeta(1/2+is)|^2}{|\zeta_{on}(1/2+is)|^2}\bigg|_{\text{quadruplet}} = \frac{|(1/2-\sigma_0)^2 + (s-\gamma_0)^2|}{(s-\gamma_0)^2} \cdot \frac{|(1/2-\sigma_0)^2 + (s+\gamma_0)^2|}{(s+\gamma_0)^2} \geq 1$$

for $s \notin \{-\gamma_0, \gamma_0\}$, with equality only when $\sigma_0 = 1/2$ (RH).

**Conclusion:** $|\zeta(1/2+is)|^2 \geq |\zeta_{on}(1/2+is)|^2$ pointwise, with equality a.e. iff RH.

This confirms that the integrand of $T_\lambda$ is non-negative. To prove $T_\lambda = 0$ we need an argument that goes *against* this integrand — an upper bound that cancels it.

---

## 3. Attack 1: Weil's formula as a constraint on $\int W_\lambda |\zeta|^2 dm_\infty$

### 3.1. What Weil's formula says

The Weil explicit formula (applied to the logarithm of $\zeta$, not to $|\zeta|^2$) establishes: for any test function $h$ analytic and with appropriate decay,

$$\sum_n h(\gamma_n) = -\sum_p \sum_{m \geq 1} \frac{\log p}{p^{m/2}} \hat{h}(m\log p) + C[h],$$

where the left-hand sum is over the imaginary parts $\gamma_n$ of all zeros of $\zeta$ and $C[h]$ are the archimedean terms (gamma and pole). The right-hand side depends only on the test function $h$ and on the primes — not on the exact position of the zeros.

### 3.2. The connection with $T_\lambda$

The integral $T_\lambda = \int W_\lambda (|\zeta|^2 - |\zeta_{on}|^2) dm_\infty$ involves $|\zeta|^2$, not the zeros directly. The relation between $|\zeta(1/2+is)|^2$ and the zeros is:

$$\log|\zeta(1/2+is)|^2 = 2\sum_n \log\left|1 - \frac{s}{\gamma_n}\right| + \text{smooth}.$$

(The sum is over the imaginary parts of the zeros, with absolute convergence after the Weierstrass convergence factor.)

Weil's formula speaks of $\frac{d}{ds}\log|\zeta|$ (the logarithmic derivative), not of $\log|\zeta|$ itself.

### 3.3. The obstacle: log vs. square

The relation between what Weil's formula gives ($\frac{d}{ds}\log|\zeta|$, or equivalently $-\text{Re}\frac{\zeta'}{\zeta}(1/2+is)$) and what we need for $T_\lambda$ ($|\zeta(1/2+is)|^2$) requires:

$$|\zeta(1/2+is)|^2 = \exp\!\left(2\int_{-\infty}^s \left(-\text{Im}\frac{\zeta'}{\zeta}(1/2+it)\right) dt\right) \cdot |\zeta(1/2-i\infty)|^2.$$

The bound $|\zeta(1/2 - i\infty)|^2$ is the "value at infinity" — and the function $\zeta$ cannot be evaluated at $-i\infty$ directly. This integration introduces an integration constant that depends on the zeros globally.

**Result of Attack 1:** Weil's formula does not directly give information about $T_\lambda$. It relates $\frac{d}{ds}\log|\zeta|$ to primes, but the connection with $|\zeta|^2$ requires integration with boundary conditions that are exactly equivalent to RH.

---

## 4. Attack 2: Jensen's inequality and logarithmic convexity

### 4.1. Jensen applied to $W_\lambda dm_\infty$

The function $W_\lambda dm_\infty$ is a positive finite measure (not a probability measure, but we can normalize). Let $\mu_\lambda = W_\lambda dm_\infty / \|W_\lambda\|_{L^1(dm_\infty)}$.

Jensen's inequality for the convex function $e^x$:

$$\int e^{2u} d\mu_\lambda \geq \exp\!\left(2\int u\, d\mu_\lambda\right),$$

with $u = \log|\zeta(1/2+is)|$ and $u_{on} = \log|\zeta_{on}(1/2+is)|$.

This gives: $\int W_\lambda |\zeta|^2 dm_\infty \geq \exp(2\int W_\lambda \log|\zeta| dm_\infty / \|W_\lambda\|_1) \cdot \|W_\lambda\|_1$.

### 4.2. The bound we would need

To prove $T_\lambda = \int W_\lambda(|\zeta|^2 - |\zeta_{on}|^2) dm_\infty \leq 0$ we would need an upper bound:

$$\int W_\lambda |\zeta|^2 dm_\infty \leq \int W_\lambda |\zeta_{on}|^2 dm_\infty.$$

Jensen only gives lower bounds (not upper bounds) for $\int e^{2u}$. To obtain an upper bound we would need the opposite inequality — i.e. that $e^x$ be concave, which is false.

**Result of Attack 2:** The convexity of $e^x$ works in the wrong direction. Jensen gives lower bounds for $\int |\zeta|^2 dm_\infty$, not upper bounds. This attack not only fails — it fails in the direction opposite to what we need.

---

## 5. Attack 3: using the functional equation of $\zeta$

### 5.1. The functional equation on the critical line

The functional equation $\xi(s) = \xi(1-s)$ implies $\Xi(-t) = \Xi(t)$ (parity). On the critical line $s = 1/2 + it$:

$$|\zeta(1/2+it)|^2 = |\chi(1/2+it)|^{-1} \cdot |\zeta(1/2+it)|^2,$$

where $|\chi(1/2+it)| = 1$. This is a tautology — the functional equation gives no new information about the modulus on the critical line.

### 5.2. The Bohr–Landau–von Mangoldt constraint

The mean square of $|\zeta(1/2+is)|$ over intervals $[T, 2T]$ is known:

$$\frac{1}{T}\int_T^{2T} |\zeta(1/2+it)|^2 dt \sim \log T.$$

And for $|\zeta_{on}|$: the same formula holds because $\zeta_{on}$ has the same zero distribution on average (same asymptotic count $N(T) \sim \frac{T}{2\pi}\log T$).

So:
$$\frac{1}{T}\int_T^{2T} W_\lambda(t)(|\zeta|^2 - |\zeta_{on}|^2) dt \to 0 \quad (T \to \infty)?$$

Not necessarily: $W_\lambda$ is fixed and the integral is over large $t$, not over the relevant region.

### 5.3. The Lindelöf constraint

The Lindelöf hypothesis (a consequence of RH, but not equivalent to it) would say $|\zeta(1/2+it)| = O(t^\varepsilon)$. This would give a bound on $T_\lambda$ for large $\lambda$, but not that $T_\lambda = 0$.

**Result of Attack 3:** The functional equation and the mean squares do not give $T_\lambda = 0$ without additional hypotheses equivalent to RH.

---

## 6. The fundamental obstacle: named with precision

All three attacks fail at the same point. The obstacle can be stated precisely:

**Proposition 6.1** (The obstacle).

The following are equivalent:

1. $T_\lambda = 0$ for all $\lambda > 0$.
2. $\int W_\lambda(s)(|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2) dm_\infty(s) = 0$ for all $\lambda$.
3. $|\zeta(1/2+is)|^2 = |\zeta_{on}(1/2+is)|^2$ for $dm_\infty$-almost every $s$.
4. RH.

*Proof.* (1)$\iff$(2): by definition. (2)$\iff$(3): because $\{W_\lambda\}_{\lambda>0}$ is a separating family in $L^1(dm_\infty)$ (as $\lambda \to \infty$, $W_\lambda$ converges to $\sum_{n=0}^\infty n|P_n|^2$, which is dense by completeness of $\{P_n\}$). (3)$\iff$(4): by the Hadamard argument of Doc 64. $\square$

**The obstacle is exactly that (3) is RH.** There is no additional information in the CCM formalism distinguishing $|\zeta|^2$ from $|\zeta_{on}|^2$ without already knowing they are equal.

---

## 7. A new observation: the Euler product constraint

### 7.1. What is new

There is a fact that Docs 70-72 did not fully use: the function $\zeta$ has an Euler product $\zeta(s) = \prod_p (1-p^{-s})^{-1}$, and $\zeta_{on}$ does NOT have this Euler product.

This is a fundamental constraint: $dm_{full} = dm_\infty \cdot |\zeta(1/2+is)|^2$ is given by ONE SPECIFIC FUNCTION — the Riemann zeta function — which satisfies the Euler product. The function $dm_{full,on} = dm_\infty \cdot |\zeta_{on}(1/2+is)|^2$ is given by an arbitrary function constructed only from its zero distribution.

### 7.2. Reformulating the problem

The question $T_\lambda = 0$ is equivalent to: is the modulus $|\zeta(1/2+is)|$ on the critical line the same as the modulus of the function $\zeta_{on}$ built from its critical zeros?

The answer would be positive if: the zero distribution of $\zeta$ on the critical line *fully determines* the modulus $|\zeta(1/2+is)|$, with the Euler product forcing that there can be no "excess" modulus.

**Conjecture 7.1** (The RH complement).

The modulus $|\zeta(1/2+is)|^2$ on the critical line is the *minimum* possible among all entire functions with the same Euler product and the same distribution of real zeros (zeros with $\beta = 1/2$), subject to the functional equation.

If Conj. 7.1 is true, then $|\zeta|^2 \leq |\zeta_{on}|^2$ pointwise, which combined with $|\zeta|^2 \geq |\zeta_{on}|^2$ (§2) gives $|\zeta|^2 = |\zeta_{on}|^2$, i.e. RH.

### 7.3. Analysis of Conjecture 7.1

Conj. 7.1 says that the Euler product *forces* the absence of off-critical zeros. This is precisely the strength of the Euler product — the singularities of $\log\zeta$ in the half-plane $\text{Re}(s) > 1$ are completely determined by the primes, and the analytic continuation to $\text{Re}(s) = 1/2$ should be "minimal" in some sense.

To formalize: if $\zeta$ had an off-critical zero $\sigma_0 + i\gamma_0$ with $\sigma_0 > 1/2$, the ratio $|\zeta(1/2+is)|^2 / |\zeta_{on}(1/2+is)|^2 > 1$ over most of the critical line (§2). This would mean $\int |\zeta|^2 dm_\infty > \int |\zeta_{on}|^2 dm_\infty$.

But the Euler product gives:

$$\int_{\mathbb{R}} |\zeta(1/2+is)|^2 dm_\infty(s) = \sum_{n=1}^\infty \frac{d(n)^2}{n} \cdot \hat{w}(\log n),$$

where $d(n)$ is the number of divisors of $n$ and $\hat{w}$ is the Fourier transform of the density $w = dm_\infty/ds$. This is a fixed number, fully determined by the primes — independent of whether RH is true or not.

And for $\zeta_{on}$:

$$\int_{\mathbb{R}} |\zeta_{on}(1/2+is)|^2 dm_\infty(s) = ?$$

Here is the problem: $\zeta_{on}$ does NOT have an Euler product, so we cannot compute $\int |\zeta_{on}|^2 dm_\infty$ in the same way.

---

## 8. The real heart of the problem

**Proposition 8.1** (The heart of the obstacle).

The following are equivalent:

1. RH.
2. $\int |\zeta_{on}(1/2+is)|^2 dm_\infty(s) = \int |\zeta(1/2+is)|^2 dm_\infty(s) = \sum_n d(n)^2 \hat{w}(\log n)/n$.
3. The function $\zeta_{on}$ satisfies the same mean-square formula over $dm_\infty$ as the zeta function.

*Proof.* (1)$\Rightarrow$(2): under RH, $|\zeta| = |\zeta_{on}|$ on the critical line, so the integrals are equal, and that of $|\zeta|^2$ is computed via the Euler product. (2)$\Rightarrow$(1): if the mean squares are equal and $|\zeta| \geq |\zeta_{on}|$ pointwise (§2), then $|\zeta| = |\zeta_{on}|$ a.e., which is RH. $\square$

**Remark 8.2.** The equality of the number $\sum_n d(n)^2 \hat{w}(\log n)/n$ with $\int |\zeta_{on}|^2 dm_\infty$ requires that $\zeta_{on}$, although it has no Euler product, have the same $L^2(dm_\infty)$ norm as the function $\zeta$. This is equivalent to RH — a tautology.

---

## 9. Is there any new angle?

### 9.1. The Euler product as a constraint on the test function

A genuinely new idea: instead of treating $|\zeta|^2$ as an arbitrary function, explicitly use that $|\zeta(1/2+is)|^2 = \prod_p |1-p^{-1/2-is}|^{-2}$.

The integral:

$$\int W_\lambda(s) |\zeta(1/2+is)|^2 dm_\infty(s) = \int W_\lambda(s) \prod_p |1-p^{-1/2-is}|^{-2} dm_\infty(s).$$

Expanding the product (formally):

$$= \int W_\lambda(s) \sum_{n \geq 1} d(n) n^{-1/2-is} \sum_{m \geq 1} d(m) m^{-1/2+is} dm_\infty(s)$$
$$= \sum_{n,m \geq 1} \frac{d(n)d(m)}{\sqrt{nm}} \int W_\lambda(s) (n/m)^{is} dm_\infty(s).$$

The inner integral is the Fourier transform of $W_\lambda dm_\infty$ evaluated at $\log(m/n)$:

$$\int W_\lambda(s) (n/m)^{is} dm_\infty(s) = \widehat{W_\lambda dm_\infty}(\log(n/m)).$$

Therefore:

$$\int W_\lambda |\zeta|^2 dm_\infty = \sum_{n,m \geq 1} \frac{d(n)d(m)}{\sqrt{nm}} \widehat{W_\lambda dm_\infty}(\log(n/m)).$$

This is the *exact arithmetic representation* of $\int W_\lambda |\zeta|^2 dm_\infty$ in terms of the Euler product.

### 9.2. The Fourier transform of $W_\lambda dm_\infty$

From the Abel form of $W_\lambda$:

$$W_\lambda(s) = \sum_{k=1}^{N(\lambda)} k\, |P_k(s)|^2 + (a_{N(\lambda)}^\infty)^2 |P_{N(\lambda)+1}|^2,$$

its Fourier transform with respect to $dm_\infty$:

$$\widehat{W_\lambda dm_\infty}(r) = \sum_{k=1}^{N(\lambda)} k \underbrace{\int |P_k(s)|^2 e^{irs} dm_\infty(s)}_{\phi_k(r)} + (a_{N(\lambda)}^\infty)^2 \phi_{N(\lambda)+1}(r),$$

where $\phi_k(r) = \int |P_k(s)|^2 e^{irs} dm_\infty$ is the characteristic function of the spectral measure $|P_k|^2 dm_\infty$.

**Proposition 9.1** (Arithmetic representation of $T_\lambda$).

$$T_\lambda = \sum_{n,m} \frac{d(n)d(m)}{\sqrt{nm}} \widehat{W_\lambda dm_\infty}(\log(n/m)) - \int W_\lambda |\zeta_{on}|^2 dm_\infty.$$

The first term is explicit in terms of primes and the CCM polynomials. The second term requires knowing $\zeta_{on}$.

### 9.3. Why this angle is promising

The first term $\sum_{n,m} d(n)d(m)/\sqrt{nm} \cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ is completely explicit and computable. It is a function of $\lambda$ depending only on the CCM structure.

If we could show that this first term *equals* $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ independently of the position of the zeros — i.e. that the arithmetic sum already forces the equality — we would have RH.

The precise question: is the identity

$$\sum_{n,m} \frac{d(n)d(m)}{\sqrt{nm}} \widehat{W_\lambda dm_\infty}(\log(n/m)) = \int W_\lambda |\zeta_{on}|^2 dm_\infty$$

verifiable *without* assuming RH?

The answer is: only if $\int W_\lambda |\zeta_{on}|^2 dm_\infty = \int W_\lambda |\zeta|^2 dm_\infty$, which is RH. We have closed another circle.

---

## 10. Final diagnosis: the nature of the obstacle

All the attacks converge on the same obstacle:

> **The function $|\zeta_{on}(1/2+is)|^2$ cannot be computed explicitly without already knowing the exact position of all zeros of $\zeta$ (which is the information we want to prove).**

More precisely:

- $|\zeta(1/2+is)|^2$ has an explicit arithmetic representation via the Euler product (Prop. 9.1).
- $|\zeta_{on}(1/2+is)|^2$ does not have this representation — it is a function built purely from its zeros.
- The difference $|\zeta|^2 - |\zeta_{on}|^2$ cannot be simplified without explicitly knowing the position of the zeros.

The CCM formalism gives an optimal test function ($W_\lambda$, with positivity, representation-theoretic motivation, and arithmetic connection via Weil), but not a new source of information about the position of the zeros.

---

## 11. The next door: can $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ be computed?

**Remark 11.1.** The function $|\zeta_{on}(1/2+is)|^2$ satisfies:

$$|\zeta_{on}(1/2+is)|^2 = \prod_n \frac{s^2 + \gamma_n^2}{\gamma_n^2} \cdot C$$

(Hadamard product, critical zeros only, with normalization constant $C$). This gives:

$$\log|\zeta_{on}(1/2+is)|^2 = \sum_n \log\!\left(1 + \frac{s^2}{\gamma_n^2}\right) + \log C.$$

The integral $\int W_\lambda(s) \log|\zeta_{on}(1/2+is)|^2 dm_\infty(s)$ can be computed if we know $\phi_k(r) = \int |P_k|^2 e^{irs} dm_\infty$ explicitly (i.e. if we have the full Plancherel–Rotach asymptotics).

This is the connection with Doc 66: the PR asymptotics for $P_k$ evaluated at $\gamma_n$ (the critical zeros) would give $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ explicitly. And comparing with $\sum_{n,m} d(n)d(m)/\sqrt{nm} \cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ would give the identity equivalent to RH.

**The new door that opens:** Compute $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ explicitly via the Plancherel–Rotach asymptotics and compare with the arithmetic representation of $\int W_\lambda |\zeta|^2 dm_\infty$. If the two are equal, RH is true. If not, $\neg$RH.

This is not a proof — it is a quantitative calculation that *would verify* RH (or refute RH) if it could be carried out. The difficulty is that the calculation requires knowing the $\gamma_n$ explicitly (the zeros of $\zeta$ on the critical line), which are infinite in number and not known in closed form.

---

## 12. Frank conclusion

**We have not proved RH.** But we have identified with surgical precision where the obstacle lies:

> It is the impossibility of computing $\int W_\lambda |\zeta_{on}|^2 dm_\infty$ without knowing the $\gamma_n$ (critical zeros of $\zeta$), and the impossibility of comparing this with $\int W_\lambda |\zeta|^2 dm_\infty = \sum_{n,m} d(n)d(m)/\sqrt{nm} \cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ without assuming RH.

The CCM formalism has reduced RH to an identity between:
1. An explicit arithmetic sum (divisors, primes, Fourier transform of $W_\lambda dm_\infty$).
2. A Hadamard product over the critical zeros of $\zeta$.

These two quantities are equal if and only if RH is true.

---

*End of Document 73.*
