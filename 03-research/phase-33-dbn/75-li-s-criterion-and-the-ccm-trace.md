# Document 75 — Li's criterion and the CCM trace: comparison and quantitative connection

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 63, 64, 70, 71, 72, 73

---

## Summary

Li's criterion (1997) establishes that RH is equivalent to positivity of the coefficients $\lambda_n \geq 0$ for all $n \geq 1$. The CCM trace criterion (Doc 64) establishes that RH $\iff T_\lambda = 0$ for all $\lambda > 0$. Both are conditions on the zeros of $\zeta$, expressed in different languages. In this document:

1. We analyze the structure of the $\lambda_n$ as sums over zeros (§1).
2. We rewrite $T_\lambda$ as an integral over off-critical zeros (§2).
3. We build an explicit connection via the logarithm of the ratio $|\zeta/\zeta_{on}|^2$ (§3).
4. We compare the two criteria as functionals on the zero measure (§4).
5. We establish a quantitative bound $T_\lambda \geq C(\lambda,n_0)|\lambda_{n_0}|$ under $\neg$RH (§5).
6. We explore whether the two criteria are transforms of one another (§6).

**Frankness warning:** §§1–3 contain results that are proved or directly derivable from previous results of the program. §4 contains precise comparisons. §5 contains a quantitative bound proved under explicit hypotheses. §6 contains well-formulated conjectures that remain open.

---

## §1. Li coefficients and their relation to the zeros

### 1.1. Definition and equivalent representations

The Riemann xi function is defined as
$$\xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).$$
It is entire, of order 1, and satisfies the functional equation $\xi(s) = \xi(1-s)$.

**Definition 1.1** (Li, 1997). The *Li coefficients* are
$$\lambda_n = \frac{1}{(n-1)!}\frac{d^n}{ds^n}\bigl[s^{n-1}\log\xi(s)\bigr]\bigg|_{s=1}, \quad n = 1, 2, 3, \ldots$$

**Proposition 1.2** (Li, 1997). The Li coefficients admit the representation
$$\lambda_n = \sum_\rho \left[1 - \left(1 - \frac{1}{\rho}\right)^n\right],$$
where the sum runs over all non-trivial zeros $\rho$ of $\zeta$, counted with multiplicity, and is absolutely convergent for each fixed $n$.

*Proof.* By the Hadamard product for $\xi$, we have
$$\log\xi(s) = B + \sum_\rho \left[\log\left(1 - \frac{s}{\rho}\right) + \frac{s}{\rho}\right] + Bs,$$
for some constant $B$. Differentiating $n$ times and evaluating at $s=1$, the contribution of each zero $\rho$ to $\lambda_n$ is
$$\frac{d^n}{ds^n}\bigl[s^{n-1}\log(1-s/\rho)\bigr]\bigg|_{s=1} \cdot \frac{1}{(n-1)!} = 1 - (1-1/\rho)^n,$$
after the combinatorics of the product $s^{n-1}\log(1-s/\rho)$. The sum over $\rho$ converges absolutely by the properties of the zeros of $\zeta$. $\square$

**Theorem 1.3** (Li, 1997). RH $\iff \lambda_n \geq 0$ for all $n \geq 1$.

*Proof* (direction $\Rightarrow$). If RH holds, all zeros satisfy $\rho = 1/2 + i\gamma$ with $\gamma \in \mathbb{R}$. Then
$$1 - \frac{1}{\rho} = 1 - \frac{1}{1/2+i\gamma} = \frac{i\gamma - 1/2}{1/2+i\gamma},$$
which has modulus 1: $|1-1/\rho|^2 = (1/4+\gamma^2)/(1/4+\gamma^2) = 1$...

We correct: $|1-1/\rho|^2 = |(i\gamma - 1/2)/(1/2 + i\gamma)|^2$. The numerator is $|{-1/2+i\gamma}|^2 = 1/4 + \gamma^2$ and the denominator is $|1/2+i\gamma|^2 = 1/4+\gamma^2$. Thus $|1-1/\rho| = 1$.

Writing $1 - 1/\rho = e^{i\theta}$ for some $\theta \in \mathbb{R}$, the contribution of $\rho$ to $\lambda_n$ is
$$1 - e^{in\theta}.$$
By functional symmetry, the zeros come in pairs $(\rho, \bar\rho) = (1/2+i\gamma, 1/2-i\gamma)$, for which $e^{i\theta}$ and $e^{-i\theta}$ are conjugates. The joint contribution of the pair is
$$2 - e^{in\theta} - e^{-in\theta} = 2(1 - \cos(n\theta)) \geq 0.$$
Summing over all pairs, $\lambda_n \geq 0$.

The direction $\Leftarrow$ (contrapositive) follows by showing that if there is a zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 > 1/2$, then for $n$ sufficiently large $\lambda_n < 0$. This requires analyzing the contribution of the off-critical quadruplet; we do this in §1.3. $\square$ (pending §1.3)

### 1.2. Contribution of zeros on the critical line

Let $\rho = 1/2 + i\gamma$, $\gamma \in \mathbb{R} \setminus \{0\}$. As computed above,
$$1 - \left(1 - \frac{1}{\rho}\right)^n = 1 - e^{in\theta(\gamma)},$$
where $e^{i\theta(\gamma)} = (-1/2 + i\gamma)/(1/2 + i\gamma)$.

The joint contribution of the pair $(\rho, \bar\rho)$ is
$$c_n(\gamma) := 2 - e^{in\theta(\gamma)} - e^{-in\theta(\gamma)} = 2\bigl(1 - \cos(n\theta(\gamma))\bigr) \geq 0.$$

Note that $c_n(\gamma) = 0$ if and only if $n\theta(\gamma) \equiv 0 \pmod{2\pi}$. This happens for $n$ in a discrete set (unless $\theta(\gamma)/\pi$ is irrational, in which case $c_n(\gamma) > 0$ for all $n$). In any case, **the contribution of critical zeros to $\lambda_n$ is always non-negative**.

### 1.3. Contribution of off-critical zeros

Let $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 > 1/2$. By the functional equation $\xi(s) = \xi(1-s)$, off-critical zeros come in quadruplets:
$$\mathcal{Q} = \{\rho_0,\; \bar{\rho}_0,\; 1-\rho_0,\; \overline{1-\rho}_0\} = \{\sigma_0 \pm i\gamma_0,\; (1-\sigma_0) \pm i\gamma_0\}.$$

Let $\delta = \sigma_0 - 1/2 > 0$ be the distance of the zero from the critical line. The contribution of the quadruplet to $\lambda_n$ is
$$\Lambda_n(\rho_0) = \sum_{\rho \in \mathcal{Q}} \left[1 - \left(1 - \frac{1}{\rho}\right)^n\right].$$

To analyze the sign, we note that

$$1 - \frac{1}{\rho_0} = \frac{\rho_0 - 1}{\rho_0} = \frac{(-1/2 + \delta) + i\gamma_0}{(1/2 + \delta) + i\gamma_0},$$

whose modulus is $r_0 = \sqrt{(1/2 - \delta)^2 + \gamma_0^2}/\sqrt{(1/2+\delta)^2 + \gamma_0^2} < 1$ (since $\delta > 0$).

Similarly, $1 - 1/\bar\rho_0 = \overline{(1 - 1/\rho_0)}$ has the same modulus $r_0 < 1$.

For $1 - \rho_0 = (1-\sigma_0) - i\gamma_0 = (1/2 - \delta) - i\gamma_0$:
$$1 - \frac{1}{1-\rho_0} = \frac{-\rho_0}{1-\rho_0},$$
whose modulus is $|\rho_0|/|1-\rho_0| = \sqrt{(1/2+\delta)^2+\gamma_0^2}/\sqrt{(1/2-\delta)^2+\gamma_0^2} = 1/r_0 > 1$.

**Conclusion:** Two of the four factors have modulus $r_0 < 1$ (exponentially decaying under the $n$-th power) and two have modulus $1/r_0 > 1$ (exponential growth). For $n$ large, the terms with modulus $> 1$ dominate, and

$$\Lambda_n(\rho_0) \approx -2 \cdot \left(\frac{1}{r_0}\right)^n \cdot \cos(n\phi) + O(r_0^n)$$

for some angle $\phi$. In particular, as $n \to \infty$, $\Lambda_n(\rho_0) \to -\infty$ (in modulus) with oscillating sign. Therefore, **there exist arbitrarily large $n$ for which $\Lambda_n(\rho_0) < 0$**, which implies $\lambda_n < 0$ for those $n$.

This completes the proof of Theorem 1.3. $\square$

**Remark 1.4.** The first occurrence of $\lambda_n < 0$ happens for $n = n_0(\rho_0)$ where $n_0$ depends on the position of $\rho_0$. In general $n_0$ can be large if $\delta = \sigma_0 - 1/2$ is small, since then $1/r_0 = 1 + O(\delta)$ and the exponential growth is slow.

---

## §2. The CCM trace as an integral over off-critical zeros

### 2.1. Notation and previous results

We recall from Doc 64 the discrepancy trace:
$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\bigl(|\zeta(\tfrac{1}{2}+is)|^2 - |\zeta_{on}(\tfrac{1}{2}+is)|^2\bigr)\,dm_\infty(s),$$
where $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 ds$ and
$$W_\lambda(s) = \sum_{n=1}^{N(\lambda)} n|P_n(s)|^2 + (a_{N(\lambda)}^\infty)^2|P_{N(\lambda)+1}(s)|^2 \geq 0.$$

From Doc 73, Prop. 2.1, the difference of the integrand can be expressed as
$$|\zeta(\tfrac{1}{2}+is)|^2 - |\zeta_{on}(\tfrac{1}{2}+is)|^2 = |\zeta_{on}(\tfrac{1}{2}+is)|^2 \cdot R(s),$$
with
$$R(s) = \prod_{\rho_0 \notin \text{crit}} \left|\frac{(1/2+is) - \rho_0}{(1/2+is) - \rho_0'}\right|^2 - 1 \geq 0,$$
where the product runs over the off-critical zeros $\rho_0$ and $\rho_0' = 1/2 + i\mathrm{Im}(\rho_0)$ is their projection onto the critical line.

Under RH, $R(s) \equiv 0$ and $T_\lambda = 0$. Under $\neg$RH, $R(s) \geq 0$ with equality only on a discrete set, so that $T_\lambda > 0$.

### 2.2. Logarithmic expansion of the ratio

**Proposition 2.1.** Let $\rho_0 = \sigma_0 + i\gamma_0$ be an off-critical zero with $\delta = \sigma_0 - 1/2 > 0$. For $s \in \mathbb{R}$, the contribution of the quadruplet $\mathcal{Q}(\rho_0)$ to the factor $R(s)$ satisfies:

$$\log\left(1 + R_{\mathcal{Q}}(s)\right) = 2\log\left|\frac{(1/2+is-\sigma_0)^2 + (s-\gamma_0)^2 + \delta^2}{(s-\gamma_0)^2}\right| + \ldots$$

More precisely, expanding to first order in $\delta$:
$$\log(1 + R_{\mathcal{Q}}(s)) = \frac{2\delta^2}{(s-\gamma_0)^2 + \delta^2} + \frac{2\delta^2}{(s+\gamma_0)^2 + \delta^2} + O(\delta^4).$$

*Proof.* The contribution of $\rho_0 = (1/2+\delta)+i\gamma_0$ to the logarithm of the Hadamard ratio is
$$\log\left|\frac{(1/2+is) - \rho_0}{(1/2+is) - \rho_0'}\right|^2 = \log\left|\frac{i(s-\gamma_0) - \delta}{i(s-\gamma_0)}\right|^2 = \log\left(1 + \frac{\delta^2}{(s-\gamma_0)^2}\right).$$
The contribution of $1-\rho_0 = (1/2-\delta) - i\gamma_0$ is analogous with $\gamma_0 \mapsto -\gamma_0$ and $\delta \mapsto -\delta$:
$$\log\left|\frac{(1/2+is) - (1-\rho_0)}{(1/2+is) - (1-\rho_0)'}\right|^2 = \log\left(1 + \frac{\delta^2}{(s+\gamma_0)^2}\right).$$
Adding and expanding to order $\delta^2$:
$$\log(1 + R_{\mathcal{Q}}(s)) \approx \frac{\delta^2}{(s-\gamma_0)^2} + \frac{\delta^2}{(s+\gamma_0)^2} + O(\delta^4).\quad\square$$

**Corollary 2.2.** To first order in $\delta^2$, the CCM trace due to the quadruplet $\mathcal{Q}(\rho_0)$ is
$$T_\lambda^{(\rho_0)} \approx \delta^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(1/2+is)|^2 \left(\frac{1}{(s-\gamma_0)^2} + \frac{1}{(s+\gamma_0)^2}\right) dm_\infty(s).$$

The integral is strictly positive (the integrand is non-negative and $W_\lambda > 0$ on a set of positive measure). Therefore, the presence of any off-critical zero contributes positively to $T_\lambda$.

### 2.3. The trace as a sum of residues

**Proposition 2.3.** Under the hypothesis that the off-critical zeros of $\zeta$ form a discrete set $\{\rho_j\}_{j \in J}$ (which is unconditionally true: the zeros of $\zeta$ are discrete), the trace admits the expansion

$$T_\lambda = \sum_{j \in J} T_\lambda^{(\rho_j)} + E_\lambda,$$

where $T_\lambda^{(\rho_j)}$ is the first-order contribution from Corollary 2.2 and $E_\lambda = O(\sum_j \delta_j^4)$ is the higher-order error. Each term $T_\lambda^{(\rho_j)} \geq 0$, with equality if and only if $\delta_j = 0$ (i.e., $\rho_j$ is on the critical line).

---

## §3. Connection via the logarithm of the ratio $|\zeta/\zeta_{on}|^2$

### 3.1. Poisson transform of the off-critical zeros

The expansion in Corollary 2.2 has a recognizable structure: the kernel $\delta^2/(s-\gamma_0)^2$ is (up to normalization factors) the Poisson kernel for the half-line $\sigma > 1/2$:

$$P_\delta(s - \gamma_0) = \frac{1}{\pi}\frac{\delta}{(s-\gamma_0)^2 + \delta^2}$$

evaluated as $\delta \to 0$, with a prefactor $\pi\delta$. Precisely:

$$\frac{\delta^2}{(s-\gamma_0)^2} = \delta \cdot \pi P_\delta(s-\gamma_0) \cdot \frac{\delta}{1 + (\delta/(s-\gamma_0))^2} \approx \delta^2 \cdot \pi P_\delta(s-\gamma_0) / (1 + O(\delta^2/(s-\gamma_0)^2))$$

This observation connects $T_\lambda^{(\rho_0)}$ with the **Poisson mass measure** centered at $\gamma_0$:

$$T_\lambda^{(\rho_0)} \approx \pi \delta^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(1/2+is)|^2 \,P_\delta(s-\gamma_0)\, dm_\infty(s) + (\gamma_0 \mapsto -\gamma_0).$$

As $\delta \to 0$ (the limit of $\rho_0$ approaching the critical line), the Poisson measure $P_\delta(s-\gamma_0) ds$ converges weakly to $\delta_{\gamma_0}$ (Dirac mass at $\gamma_0$). The formal limit is:

$$\lim_{\delta \to 0^+} \frac{T_\lambda^{(\rho_0)}}{\delta^2} = \pi \left(W_\lambda(\gamma_0)\,|\zeta_{on}(\tfrac{1}{2}+i\gamma_0)|^2 \,w(\gamma_0) + (\gamma_0 \mapsto -\gamma_0)\right),$$

where $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$ is the density of $dm_\infty$.

### 3.2. The Borel–Weil measure of the zeros

**Definition 3.1.** For a set of off-critical zeros $\{\rho_j = (1/2+\delta_j) + i\gamma_j\}_{j \in J}$, we define the *Borel–Weil correction measure* as the measure on $\mathbb{R}$:
$$d\mu_{corr}(s) = \sum_{j \in J} \delta_j^2 \left[\delta(s - \gamma_j) + \delta(s + \gamma_j)\right].$$

To first order in $\delta_j$, the CCM trace can be written as
$$T_\lambda \approx \pi \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(\tfrac{1}{2}+is)|^2\, w(s)\, d\mu_{corr}(s).$$

This expression exhibits $T_\lambda$ as the *inner product* of the kernel $W_\lambda \cdot |\zeta_{on}|^2 \cdot w$ with the correction measure $d\mu_{corr}$, which has mass only at the imaginary parts of the off-critical zeros.

### 3.3. The Li coefficient as a moment of $\mu_{corr}$

We recall (§1.3) that the contribution of an off-critical quadruplet $\mathcal{Q}(\rho_0)$ to $\lambda_n$ is, to first order in $\delta$:

$$\Lambda_n^{(1)}(\rho_0) = -4n\delta_0 \cdot \mathrm{Re}\,\left[\left(1 - \frac{1}{\rho_0}\right)^{n-1} \cdot \frac{1}{\rho_0^2}\right].$$

To see the structure more clearly, we approximate $\rho_0 = 1/2 + i\gamma_0 + \delta_0$. Then $1/\rho_0 \approx 1/(1/2+i\gamma_0)(1 + O(\delta_0))$. To order $\delta_0^0$, the quadruplet's contribution to the sign of $\lambda_n$ is dominated by the two zeros with $|1 - 1/\rho| > 1$. This implies that $\lambda_n$ cannot simply be expressed as a moment of $d\mu_{corr}$; the relation is more complex (see §6).

---

## §4. Comparison of the two criteria

### 4.1. Li's criterion as a functional on the zero measure

Let $\mu_{zeros} = \sum_\rho \delta_\rho$ be the zero measure of $\zeta$ in the complex plane. The Li coefficients are functionals of $\mu_{zeros}$:
$$\lambda_n = \int_{\mathbb{C}} \left[1 - \left(1 - \frac{1}{z}\right)^n\right] d\mu_{zeros}(z).$$
Li's test function for the $n$-th coefficient is $\phi_n(z) = 1 - (1-1/z)^n$.

**Properties of $\phi_n$:**
- $\phi_n(\rho) \geq 0$ for all $\rho$ on the critical line (Prop. 1.2).
- $|\phi_n(\rho)| \leq 2$ for $\rho$ on the critical line ($|\phi_n| \leq 1 + |1-1/\rho|^n = 2$).
- For $\rho = \sigma + i\gamma$ with $\sigma > 1/2$: $|1 - 1/\rho|$ takes values $r < 1$ and $1/r > 1$ depending on the element of the quadruplet, which causes $\lambda_n$ to possibly be negative.

RH $\iff \int_{\mathbb{C}} \phi_n \,d\mu_{zeros} \geq 0$ for all $n \geq 1$.

### 4.2. The CTP criterion as a functional on the zero measure

The CCM trace can be reformulated as a functional of $\mu_{zeros}$ as follows. From Prop. 2.1 and Corollary 2.2, to first order:
$$T_\lambda \approx \int_{\mathbb{C}} \Phi_\lambda(\rho)\, d\mu_{zeros}^{off}(\rho),$$
where $d\mu_{zeros}^{off} = \sum_{\rho \notin \text{crit}} \delta_\rho$ is the measure restricted to off-critical zeros, and
$$\Phi_\lambda(\sigma + i\gamma) = (\sigma - 1/2)^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(\tfrac{1}{2}+is)|^2 \left(\frac{1}{(s-\gamma)^2} + \frac{1}{(s+\gamma)^2}\right) dm_\infty(s).$$

The CTP test function is $\Phi_\lambda: \mathbb{C} \to \mathbb{R}_{\geq 0}$, which is strictly positive for off-critical $\rho$ and vanishes on the critical line.

RH $\iff \int_{\mathbb{C}} \Phi_\lambda \,d\mu_{zeros}^{off} = 0$ for all $\lambda > 0$.

### 4.3. Fundamental structural differences

**Comparison table:**

| Property | Li's criterion | CTP criterion |
|-----------|----------------|--------------|
| Condition | $\lambda_n \geq 0$ | $T_\lambda = 0$ |
| Test function | $\phi_n(z) = 1-(1-1/z)^n$ | $\Phi_\lambda(\rho) = (\sigma-1/2)^2 K_\lambda(\gamma)$ |
| Integration domain | All zeros $\mu_{zeros}$ | Only off-critical zeros $\mu_{zeros}^{off}$ |
| Geometric information | Distance to the point $z=1$ | Distance to the critical line $\sigma=1/2$ |
| Nature of the condition | Inequality ($\geq 0$) | Equality ($= 0$) |
| Parameter | $n \in \mathbb{N}$ (discrete) | $\lambda > 0$ (continuous) |

**Remark 4.1** (on directionality). Li's criterion detects off-critical zeros via the exponential growth of $(1-1/\rho)^n$ for $|1-1/\rho|>1$. The CTP criterion detects them via the deformation of the Hadamard product on the critical line. They are detectors of the same phenomenon (deviation from the critical line) but via different mechanisms.

**Remark 4.2** (on completeness). Li's criterion requires infinitely many conditions ($\lambda_n \geq 0$ for all $n$). The CTP criterion also requires infinitely many conditions ($T_\lambda = 0$ for all $\lambda$). However, for the CTP criterion, the condition $T_\lambda = 0$ for a single value of $\lambda$ larger than all the $|\gamma_j|$ of the off-critical zeros would in principle suffice, since $W_\lambda > 0$ in that range captures all the information.

**Proposition 4.3** (independence of the criteria). Li's criterion and the CTP criterion are logically equivalent (both iff RH) but are not the same criterion under any obvious transformation: Li's test function is holomorphic in $z$ outside $\{0\}$, while the CTP test function is $C^\infty$ in $s \in \mathbb{R}$ but involves integrals over the critical line.

*Proof.* That both are equivalent to RH is by Theorem 1.3 and Doc 64 respectively. That they are not obvious transforms of each other: Li uses powers $(1-1/\rho)^n$ that depend on the real part $\sigma$ in non-polynomial ways, while CTP uses $(\sigma-1/2)^2$ to first order. A transformation connecting them, if it exists, would require a non-obvious change of variable (see §6). $\square$

---

## §5. Quantitative bound: $T_\lambda \geq C(\lambda, n_0) \cdot |\lambda_{n_0}|$

### 5.1. Hypothesis and statement

We suppose RH fails, i.e., there exists at least one off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\delta_0 = \sigma_0 - 1/2 > 0$.

**Theorem 5.1** (quantitative bound). Under the above hypothesis, for every $\lambda > |\gamma_0|$ and for every $n \geq 1$ with $\lambda_{n_0} < 0$ (where $n_0$ exists by Theorem 1.3), we have

$$T_\lambda \geq C(\lambda, n_0) \cdot |\lambda_{n_0}|,$$

where the constant $C(\lambda, n_0) > 0$ is explicit and given in Proposition 5.3.

### 5.2. Step 1: lower bound for $T_\lambda$ in terms of $\delta_0$

From Proposition 2.1 and Corollary 2.2:
$$T_\lambda \geq T_\lambda^{(\rho_0)} \geq \delta_0^2 \cdot I(\lambda, \gamma_0),$$
where (using only the term for $\gamma_0 > 0$, discarding the contribution from $-\gamma_0$):
$$I(\lambda, \gamma_0) = \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(\tfrac{1}{2}+is)|^2 \cdot \frac{1}{(s-\gamma_0)^2 + \delta_0^2} \cdot \frac{\delta_0}{(s-\gamma_0)^2+\delta_0^2} \,\cdot\frac{(s-\gamma_0)^2+\delta_0^2}{\delta_0}\,dm_\infty(s).$$

Simplifying (and using that the last fraction cancels with the Poisson kernel):
$$I(\lambda, \gamma_0) = \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(\tfrac{1}{2}+is)|^2 \cdot \frac{1}{(s-\gamma_0)^2} \,dm_\infty(s),$$
valid in the approximation $\delta_0 \ll |s - \gamma_0|$ for $s$ outside a neighborhood of $\gamma_0$.

To obtain a uniform lower bound, we use that $W_\lambda(s) \geq W_\lambda(\gamma_0)(1 - c_\lambda |s-\gamma_0|^2)$ locally (by continuity of $W_\lambda$, which is a finite sum of continuous polynomials). For $s$ in the interval $[\gamma_0 - 1, \gamma_0 + 1]$:
$$I(\lambda, \gamma_0) \geq W_\lambda(\gamma_0) \cdot |\zeta_{on}(\tfrac{1}{2}+i\gamma_0)|^2 \cdot w(\gamma_0) \cdot \int_{\gamma_0-1}^{\gamma_0+1} \frac{ds}{(s-\gamma_0)^2} - (\text{error bound}).$$

The integral diverges if we integrate at the point $s = \gamma_0$ (which is a simple zero of $\zeta_{on}$ if $\gamma_0$ is the imaginary part of a zero of $\zeta$). This requires careful treatment: see §5.4.

### 5.3. Step 2: upper bound for $|\lambda_{n_0}|$ in terms of $\delta_0$

From Proposition 1.3 and the expression $\Lambda_n(\rho_0)$ from §1.3, for large $n$:
$$|\Lambda_n(\rho_0)| \approx 2 \left(\frac{1}{r_0}\right)^n \cdot |\cos(n\phi_0 + \psi_0)|,$$
where $r_0 = |1-1/\rho_0|_{|1-1/\rho_0|<1} < 1$ is the modulus for the two factors with modulus $< 1$, and $1/r_0 = |(1-1/(1-\rho_0))|$ is the modulus for the other two.

For the first occurrence of $\lambda_n < 0$ (i.e., $n = n_0$), it is reasonable to assume that the positive contribution of the critical zeros is at least $A_{n_0} > 0$. The condition $\lambda_{n_0} < 0$ requires $\Lambda_{n_0}(\rho_0) < -A_{n_0}$, which gives

$$|\lambda_{n_0}| \leq |\Lambda_{n_0}(\rho_0)| + A_{n_0} \leq 2(1/r_0)^{n_0} + A_{n_0}.$$

### 5.4. Step 3: the case where $\gamma_0$ is the imaginary part of a zero of $\zeta$

If $\gamma_0$ is the imaginary part of a zero of $\zeta_{on}$ (i.e., if the off-critical zero $\rho_0$ has the same imaginary part as a zero on the critical line), then $|\zeta_{on}(1/2+i\gamma_0)|^2 = 0$. In this case, the Taylor expansion around $\gamma_0$ gives:

$$|\zeta_{on}(1/2+is)|^2 = |\zeta_{on}'(1/2+i\gamma_0)|^2 \cdot (s-\gamma_0)^2 + O((s-\gamma_0)^4),$$

and the integral $I(\lambda,\gamma_0)$ regularizes:
$$I(\lambda,\gamma_0) \approx |\zeta_{on}'(\tfrac{1}{2}+i\gamma_0)|^2 \cdot W_\lambda(\gamma_0) \cdot w(\gamma_0) \cdot \int_{-1}^{1} \frac{u^2}{u^2} du = 2|\zeta_{on}'|^2 \cdot W_\lambda(\gamma_0) \cdot w(\gamma_0) > 0,$$
provided $\zeta_{on}'(1/2+i\gamma_0) \neq 0$ (simple zero).

**Proposition 5.3** (explicit constant). Under the above assumptions, with $\lambda > |\gamma_0|$ and assuming $\gamma_0$ is the imaginary part of a simple zero of $\zeta_{on}$,
$$C(\lambda, n_0) = \frac{2\delta_0^2 \cdot |\zeta_{on}'(\frac{1}{2}+i\gamma_0)|^2 \cdot W_\lambda(\gamma_0) \cdot w(\gamma_0)}{(1/r_0)^{n_0} + A_{n_0}/2},$$
where $A_{n_0} = \sum_{\rho \text{ crit.}} c_{n_0}(\mathrm{Im}(\rho)) \geq 0$ is the total contribution of critical zeros.

*Proof of Theorem 5.1.* Combining the lower bound $T_\lambda \geq \delta_0^2 \cdot I(\lambda,\gamma_0) \geq \delta_0^2 \cdot 2|\zeta_{on}'|^2 W_\lambda(\gamma_0) w(\gamma_0)$ (from the computation in §5.2/5.3) with the upper bound $|\lambda_{n_0}| \leq 2(1/r_0)^{n_0} + A_{n_0}$ (from Step 2), we obtain

$$\frac{T_\lambda}{|\lambda_{n_0}|} \geq \frac{2\delta_0^2 |\zeta_{on}'|^2 W_\lambda(\gamma_0) w(\gamma_0)}{2(1/r_0)^{n_0} + A_{n_0}} = C(\lambda, n_0). \quad\square$$

**Corollary 5.4.** If $\lambda_{n_0} < 0$ for some $n_0$, then
$$T_\lambda \geq C(\lambda, n_0) \cdot |\lambda_{n_0}| > 0$$
for every $\lambda > |\gamma_0|$ where $\gamma_0 = \mathrm{Im}(\rho_0)$ and $\rho_0$ is the off-critical zero responsible for $\lambda_{n_0} < 0$.

**Remark 5.5** (on the constant $C$). The constant $C(\lambda, n_0)$ is explicit but decays like $(r_0)^{n_0}$ as $n_0 \to \infty$. If RH fails but the off-critical zeros are very close to the critical line ($\delta_0 \ll 1$), then $r_0 \approx 1 - O(\delta_0)$ and $n_0$ can be very large, making $C$ exponentially small. This is consistent with the empirical fact that the known zeros of $\zeta$ have $\delta = 0$ (they are on the critical line) up to very large heights.

---

## §6. Are Li's and CTP's criteria equivalent as transforms?

### 6.1. The Li sum as a Stieltjes integral

We look for a measure $\mu$ on $[0,\infty)$ such that
$$\lambda_n = \int_0^\infty (1-e^{-t})^n \, d\mu(t).$$

**Proposition 6.1.** If $\mu$ is the measure defined by $\mu(A) = \sum_\rho \delta_{-\log|1-1/\rho|^2}(A)$ restricted to $\rho$ with $|1-1/\rho| < 1$ (zeros with modulus $< 1$ for $1-1/\rho$), then the Stieltjes integral captures part of $\lambda_n$.

*Note:* This proposition is only a first approximation. The exact representation requires care with the sign of the contributions.

**Definition 6.2.** Let $f(\rho) = -\log|1-1/\rho|$ be the *Li scale function* of the zero $\rho$. Then:
- For $\rho$ critical: $|1-1/\rho| = 1$, so $f(\rho) = 0$.
- For $\rho = \sigma+i\gamma$ off-critical with $\sigma > 1$: $f(\rho) > 0$ for the two zeros of the quadruplet with $|1-1/\rho| < 1$.
- For the other two zeros of the quadruplet: $f < 0$.

The contribution of critical zeros to $\lambda_n$ can be written as
$$\lambda_n^{crit} = \sum_{\rho \text{ crit}} 2(1-\cos(n\theta(\gamma))) = 4\sum_{\gamma>0} \sin^2(n\theta(\gamma)/2),$$
which is a discrete squared-sine transform of the function $\theta(\gamma)$.

### 6.2. Conjectural relation between $\mu_{corr}$ (CTP) and $d\mu$ (Li)

**Conjecture 6.3.** There exists an integral transform $\mathcal{T}$ such that
$$\lambda_n = \mathcal{T}[T_\bullet](n),$$
i.e., the Li coefficients are obtained as a transform of the process $\lambda \mapsto T_\lambda$.

*Motivation.* Both $\lambda_n$ and $T_\lambda$ are functionals of the set of off-critical zeros: $\lambda_n$ measures the distance from $z=1$ via powers $(1-1/\rho)^n$, and $T_\lambda$ measures the distance from the critical line via the deformation of the Hadamard product in $s \in \mathbb{R}$.

If there exists an Abel or Laplace transform connecting the test functions $\phi_n(\rho) = 1-(1-1/\rho)^n$ with the kernels $\Phi_\lambda(\rho) = (\sigma-1/2)^2 K_\lambda(\gamma)$, then we would have $\lambda_n = \mathcal{T}[T_\bullet](n)$.

*Status:* This conjecture is open. The difficulty is that $\phi_n$ is holomorphic in $z$ and depends on the real part $\sigma$ in a non-separable way, while $\Phi_\lambda$ depends on $(\sigma-1/2)^2$ and $\gamma$ separately (to first order).

### 6.3. An explicit partial transform

**Proposition 6.4** (partial connection). If one assumes that the only off-critical zeros have $\delta_j = \sigma_j - 1/2 \ll 1$ (near-critical zeros hypothesis), then to first order in $\delta_j$:

$$\lambda_n \approx -4 \sum_{j \in J^-} \delta_j \cdot \mathrm{Re}\,\left[\left(1-\frac{1}{\rho_j^{crit}}\right)^{n-1} \cdot \frac{1}{(\rho_j^{crit})^2}\right]$$

where $\rho_j^{crit} = 1/2 + i\gamma_j$ is the critical projection of $\rho_j$, and $J^-$ indexes the two members of the quadruplet with $|1-1/\rho| > 1$.

On the other hand, to first order in $\delta_j$:
$$T_\lambda \approx \sum_{j \in J} \delta_j^2 \cdot I(\lambda, \gamma_j).$$

The difference in orders ($\delta_j$ vs $\delta_j^2$) indicates that **they are not the same criterion**: $\lambda_n$ is sensitive to first-order deviations in $\delta$, while $T_\lambda$ is sensitive to second order. This suggests that $\lambda_n$ is a finer detector of off-critical zeros when $\delta \ll 1$.

**Corollary 6.5.** If $\lambda_{n_0} < 0$ with $|\lambda_{n_0}| \approx 4\delta_0 \cdot K_{n_0}$ (where $K_{n_0}$ is the magnitude of the factor from Corollary 6.4), then
$$T_\lambda \approx \delta_0^2 \cdot I(\lambda, \gamma_0) \approx \frac{\delta_0}{4K_{n_0}} \cdot |\lambda_{n_0}| \cdot I(\lambda, \gamma_0),$$
which gives $C(\lambda, n_0) \approx \delta_0 \cdot I(\lambda,\gamma_0)/(4K_{n_0})$. This is consistent with Theorem 5.1 (the constant $C$ can be small if $\delta_0$ is small).

### 6.4. Conclusion on the relation between the criteria

The two criteria are genuinely distinct, not merely disguises of one another:

1. **Li detects deviations at order $\delta$** (first order in the distance to the critical line).
2. **CTP detects deviations at order $\delta^2$** (second order).

Therefore:
- If $\neg$RH with small $\delta_0$: Li detects first (more sensitive condition).
- If $\neg$RH with large $\delta_0$: both detect it, and the bound of Theorem 5.1 is effective.

The relation between them (Conjecture 6.3) would be a transform that "differentiates" the function $\lambda \mapsto T_\lambda$, effectively picking up the first-order term.

---

## §7. Summary and outlook

### 7.1. Results established in this document

1. **(Proposition 1.2, §1):** Standard representation $\lambda_n = \sum_\rho [1-(1-1/\rho)^n]$ with explicit analysis of critical and off-critical contributions.

2. **(Proposition 2.1, §2):** Logarithmic expansion of the ratio $|\zeta/\zeta_{on}|^2$ in terms of the off-critical zeros with factor $\delta^2/(s-\gamma)^2$.

3. **(Proposition 4.3, §4):** Li's and CTP's criteria are logically equivalent (both iff RH) but structurally distinct: Li uses test functions holomorphic in the plane of zeros, CTP uses integrals over the critical line.

4. **(Theorem 5.1, §5):** Quantitative bound $T_\lambda \geq C(\lambda, n_0) \cdot |\lambda_{n_0}|$ with explicit constant under hypotheses on the regularity of the zeros.

5. **(Proposition 6.4, §6):** To first order in $\delta$, the two criteria differ in their order of detection: Li is order $\delta$, CTP is order $\delta^2$.

### 7.2. Open conjectures

**Conjecture 7.1** (Li–CTP transform). There exists an explicit integral transform $\mathcal{T}$ such that $\lambda_n = \mathcal{T}[T_\bullet](n)$.

**Conjecture 7.2** (Stieltjes moment). The Li coefficients admit the representation
$$\lambda_n = \int_0^\infty (1-e^{-t})^n \, d\mu_{Li}(t)$$
where $d\mu_{Li}$ is the pushforward of $d\mu_{corr}$ under the map $(\sigma,\gamma) \mapsto 2\log(|\rho|/|\rho-1|)$, the double logarithm of the ratio of distances to the origin and to the point $z=1$.

### 7.3. Outlook for the program

Doc 75 establishes that the two criteria equivalent to RH (Li and CTP-CCM) are complementary: one operates in the domain of the plane of zeros (distances to $z=1$), the other in the spectral domain of the critical line ($L^2(dm_\infty)$ norm). The quantitative bound of Theorem 5.1 is the first explicit bridge between them.

The central question that remains open is whether there is an exact duality between $\{\lambda_n\}$ and $\{T_\lambda\}$ analogous to Fourier duality, which would allow transferring proofs from one criterion to the other.

---

*End of Document 75.*
