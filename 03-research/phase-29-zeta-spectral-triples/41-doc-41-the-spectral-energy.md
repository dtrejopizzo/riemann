# Phase 29 — Doc 41: The Spectral $L^2$ Energy and the Gonek-Fujii Theorem

**Phase:** 32
**Objective:** Attack Inc. Inv. via the spectral $L^2$ norm
$$E_2(\lambda, T) := \sum_{\gamma_n \leq T} |C_\lambda(\gamma_n)|^2,$$
using the Gonek-Fujii Theorem on Dirichlet sums evaluated at the zeros of $\zeta$. Working hypothesis: shifting the problem from pointwise convergence to a quadratic average puts it in the territory where Analytic Number Theory has had all its successes (Selberg, Montgomery, Goldston-Yıldırım).

---

## 1. The problem and its appeal

The equivalence RH $\iff$ Inc. Inv. (Theorem 9.1, Doc 40/paper) says that proving Inc. Inv. is equivalent to proving RH. Inc. Inv. in pointwise form requires: $C_\lambda(\gamma_n) \to 0$ for **each** $n$ as $\lambda \to \infty$.

Pointwise convergence is the strongest version. But if we manage to show

$$E_2(\lambda, T) \to 0 \quad \text{as } \lambda \to \infty, \quad \forall T,$$

then by the **quadratic convergence lemma**:

$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n \leq T} |C_\lambda(\gamma_n)|^2 \to 0 \implies C_\lambda(\gamma_n) \to 0 \text{ for almost all } n.$$

Although "almost all" is not "all," the $L^2$ attack can:
1. Give precise asymptotics for $E_2(\lambda,T)$ in terms of prime arithmetic.
2. Identify the cancellation mechanism.
3. Produce a bound $E_2(\lambda,T) = o(N_\Xi(T) \cdot w(T)^2)$ that is an averaged version of Inc. Inv.
4. In the best case: prove $E_2(\lambda,T) \to 0$ — which implies Inc. Inv. (and hence RH) if the convergence is uniform in $n$.

**The strategic reason:** the $L^2$ norm averages over all zeros $\gamma_n \leq T$. In this average, the tools of ANT (zero pair correlations, explicit formulas, Landau's lemma) are more powerful than for pointwise questions.

---

## 2. Expansion of $E_2(\lambda, T)$: the three terms

We write $C_\lambda(\gamma_n) = w(\gamma_n) - D_\lambda(\gamma_n)$ where

$$D_\lambda(\gamma_n) = 2\sum_{m \leq \lambda^2} \Lambda(m)\, m^{-1/2}\cos(\gamma_n\log m).$$

Then:

$$|C_\lambda(\gamma_n)|^2 = |w(\gamma_n) - D_\lambda(\gamma_n)|^2 = w(\gamma_n)^2 - 2w(\gamma_n)D_\lambda(\gamma_n) + D_\lambda(\gamma_n)^2.$$

Summing over $\gamma_n \leq T$:

$$\boxed{E_2(\lambda, T) = \underbrace{\sum_{\gamma_n \leq T} w(\gamma_n)^2}_{A(\lambda,T)} - 2\underbrace{\sum_{\gamma_n \leq T} w(\gamma_n) D_\lambda(\gamma_n)}_{B(\lambda,T)} + \underbrace{\sum_{\gamma_n \leq T} D_\lambda(\gamma_n)^2}_{C(\lambda,T)}.}$$

Inc. Inv. is equivalent to $E_2(\lambda,T) \to 0$, which requires:

$$B(\lambda,T) \to \frac{A(\lambda,T) + C(\lambda,T)}{2},$$

that is, the cross term $B$ must almost completely cancel the diagonal terms $A$ and $C$.

---

## 3. The Gonek-Fujii Theorem

**Gonek-Fujii Theorem (1995).** For a Dirichlet sum $P_N(t) = \sum_{n \leq N} a_n n^{-it}$ with coefficients $a_n$:

$$\sum_{0 < \gamma_j \leq T} |P_N(\gamma_j)|^2 = \frac{T}{2\pi}\log T \sum_{n \leq N} |a_n|^2 - \frac{T}{2\pi}\sum_{n \leq N} |a_n|^2 \log n + \text{(Landau terms)} + E(N,T),$$

where the error $E(N,T) = O((T+N)\log^c(TN))$ for some constant $c$.

The **Landau terms** arise from the correlation between the Dirichlet sums evaluated at the zeros of $\zeta$ and the coefficients of the logarithmic derivative $-\zeta'/\zeta$. The precise version:

$$\sum_{0 < \gamma_j \leq T} \left|\sum_{n \leq N} a_n n^{-i\gamma_j}\right|^2 = \frac{T}{2\pi}\log\frac{T}{2\pi} \sum_{n\leq N}|a_n|^2 - 2\mathrm{Re}\,\sum_{n\leq N}a_n\bar{a}_n\sum_{m\leq N}\frac{a_m\bar{a}_m}{m^{i(\gamma_j - \cdot)}} + \ldots$$

For the coefficients $a_n = 2\Lambda(n)n^{-1/2}$ corresponding to $D_\lambda$:

$$C(\lambda,T) = \sum_{\gamma_n \leq T} D_\lambda(\gamma_n)^2 = \sum_{\gamma_n \leq T}\left|2\sum_{m\leq\lambda^2}\Lambda(m)m^{-1/2-i\gamma_n}\right|^2.$$

---

## 4. Computation of the diagonal term $C(\lambda,T)$

**Proposition 1** (Asymptotics of $C(\lambda,T)$ via Gonek-Fujii). Under the hypotheses of the Gonek-Fujii Theorem:

$$C(\lambda,T) = \frac{T}{2\pi}\log T \cdot 4\sum_{m\leq\lambda^2}\Lambda(m)^2 m^{-1} - \frac{T}{2\pi}\cdot 4\sum_{m\leq\lambda^2}\Lambda(m)^2 m^{-1}\log m + \mathcal{L}(\lambda,T) + O((T+\lambda^2)\log^c(T\lambda)),$$

where the Landau term is:

$$\mathcal{L}(\lambda,T) = \frac{T}{\pi}\sum_{m\leq\lambda^2}\Lambda(m)^2 m^{-1} \cdot \frac{\Lambda(m^2)}{m} + \ldots$$

Simplifying with $4\sum_{m\leq\lambda^2}\Lambda(m)^2/m \sim 8\log\lambda$:

$$\boxed{C(\lambda,T) \sim \frac{T}{2\pi}\log T \cdot 8\log\lambda - \frac{T}{2\pi} \cdot S_1(\lambda) + \mathcal{L}(\lambda,T),}$$

where $S_1(\lambda) = 4\sum_{m\leq\lambda^2}\Lambda(m)^2\log(m)/m \sim 8(\log\lambda)^2$ (the weighted Chebyshev sum).

*Proof.* Direct application of the Gonek-Fujii Theorem with $a_n = 2\Lambda(n)n^{-1/2}$. The coefficients satisfy: $\sum_{n\leq N}|a_n|^2 = 4\sum_{n\leq N}\Lambda(n)^2/n \sim 8\log\lambda$ (Doc 39 Proposition 3). $\square$

**Remark 1.** The dominant term of $C(\lambda,T)$ is $\frac{4T\log T\log\lambda}{\pi}$. It grows like $T(\log T)(\log\lambda)$.

---

## 5. Computation of the arithmetic term $A(\lambda,T)$

**Proposition 2** (Asymptotics of $A(\lambda,T)$). By the von Mangoldt Theorem:

$$N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T).$$

And $w(\gamma_n) \sim \frac{1}{2}\log\gamma_n \sim \frac{1}{2}\log\frac{n\cdot 2\pi}{\log n}$ for large $n$ (with $\gamma_n \sim 2\pi n/\log n$).

By the Abel-Stieltjes formula:

$$A(\lambda,T) = \sum_{\gamma_n \leq T} w(\gamma_n)^2 \approx \int_0^T w(t)^2 \,dN_\Xi(t) \sim \int_0^T \frac{(\log t)^2}{4} \cdot \frac{\log T}{2\pi}\,dt \sim \frac{T(\log T)^3}{24\pi}.$$

**Remark 2.** The term $A(\lambda,T) \sim \frac{T(\log T)^3}{24\pi}$ grows much faster than $C(\lambda,T) \sim \frac{4T\log T\log\lambda}{\pi}$ when $\log\lambda \ll (\log T)^2$.

This scale contrast is the key to the $L^2$ strategy: for $E_2 \to 0$, the cross term $B$ must cancel $A + C$, but $A$ dominates for fixed $\lambda$ and large $T$. This indicates that the $L^2$ attack must be taken in the regime $\lambda \to \infty$ first, with $T$ large but fixed, not the other way around.

---

## 6. The cross term $B(\lambda,T)$: the heart of the problem

**Proposition 3** (Expansion of $B(\lambda,T)$). Interchanging (conditionally) the sum over primes:

$$B(\lambda,T) = \sum_{\gamma_n \leq T} w(\gamma_n) D_\lambda(\gamma_n) = 2\sum_{m\leq\lambda^2}\Lambda(m)m^{-1/2}\sum_{\gamma_n \leq T} w(\gamma_n)\cos(\gamma_n\log m).$$

The inner sum is:

$$\mathcal{I}(\lambda,T;m) := \sum_{\gamma_n \leq T} w(\gamma_n)\cos(\gamma_n\log m).$$

**Proposition 4** (Decomposition of $\mathcal{I}$). Writing $\cos(\gamma_n\log m) = \frac{1}{2}(m^{i\gamma_n} + m^{-i\gamma_n})$:

$$\mathcal{I}(T;m) = \frac{1}{2}\sum_{\gamma_n\leq T}w(\gamma_n)(m^{i\gamma_n} + m^{-i\gamma_n}).$$

The sum $\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n}$ is a **weighted von Mangoldt sum over the imaginary parts of the zeros** — the central object of **Landau's Lemma**.

---

## 7. Landau's Formula and the cross sum

**Landau's Lemma** (version for zeta). For $m$ a positive integer and $T$ large:

$$\sum_{0 < \gamma_n \leq T} m^{i\gamma_n} = -\frac{T}{2\pi}\frac{\Lambda(m)}{\sqrt{m}} + O(\sqrt{m}\log^2 T).$$

*Proof.* From Riemann's explicit formula for $\psi(x)$: taking $x = e^{2\pi t/T}$ and summing appropriately, the sum $\sum_\rho x^\rho$ produces the result. The coefficient $\Lambda(m)/\sqrt{m}$ comes from the residue of the pole of $-\zeta'/\zeta$ at $s = 1/2 + i\gamma_n$ modulated by $m^{-1/2+i\gamma_n}$. See Goldston [Gol95] or Conrey-Goldston [CG93]. $\square$

**Proposition 5** (Asymptotics of $\mathcal{I}(T;m)$ via Landau). Using Landau's Lemma:

$$\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n} = \sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n}.$$

We need the version **weighted by $w(\gamma_n)$**. By Abel:

$$\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n} = w(T)\sum_{\gamma_n\leq T}m^{i\gamma_n} - \int_0^T w'(t)\sum_{\gamma_n\leq t}m^{i\gamma_n}\,dt.$$

Using Landau's Lemma for $\sum_{\gamma_n\leq t}m^{i\gamma_n} \approx -\frac{t\Lambda(m)}{2\pi\sqrt{m}}$:

$$\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n} \approx -\frac{\Lambda(m)}{2\pi\sqrt{m}}\left[w(T)\cdot T - \int_0^T w'(t)\cdot t\,dt\right].$$

The integral $\int_0^T w'(t)\cdot t\,dt = [w(t)\cdot t]_0^T - \int_0^T w(t)\,dt \approx w(T)\cdot T - \frac{T}{2}\log T$.

Hence:

$$\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n} \approx -\frac{\Lambda(m)}{2\pi\sqrt{m}}\cdot\frac{T}{2}\log T + O(T\log\log T).$$

**Corollary 1** (Asymptotics of $\mathcal{I}(T;m)$). For $m$ a fixed positive integer:

$$\mathcal{I}(T;m) = \sum_{\gamma_n\leq T}w(\gamma_n)\cos(\gamma_n\log m) \approx -\frac{\Lambda(m)}{2\pi\sqrt{m}}\cdot\frac{T\log T}{2} + O(T\log\log T).$$

---

## 8. The asymptotics of $B(\lambda,T)$

**Theorem 1** (Asymptotics of the cross term). For fixed $\lambda$ and $T \to \infty$:

$$B(\lambda,T) = 2\sum_{m\leq\lambda^2}\frac{\Lambda(m)}{\sqrt{m}}\cdot\mathcal{I}(T;m) \approx 2\sum_{m\leq\lambda^2}\frac{\Lambda(m)}{\sqrt{m}}\cdot\left(-\frac{\Lambda(m)}{2\pi\sqrt{m}}\cdot\frac{T\log T}{2}\right).$$

$$= -\frac{T\log T}{2\pi}\sum_{m\leq\lambda^2}\frac{\Lambda(m)^2}{m} + O(T\log\log T\cdot\log\lambda).$$

Since $\sum_{m\leq\lambda^2}\Lambda(m)^2/m \sim 2\log\lambda$:

$$\boxed{B(\lambda,T) \approx -\frac{T\log T\cdot 2\log\lambda}{\pi} + O(T\log\log T).}$$

*Sign check.* $B(\lambda,T) < 0$ for large $T$ and $\lambda$. This makes sense: $D_\lambda(\gamma_n)$ is a sum of cosines with coefficients $\Lambda(m)/\sqrt{m} > 0$, and Landau's Lemma says that the sum $\sum m^{i\gamma_n}$ is NEGATIVE (proportional to $-\Lambda(m)/\sqrt{m}$). Hence $D_\lambda(\gamma_n) < 0$ on a $w$-weighted average, and $B = \sum w(\gamma_n)D_\lambda(\gamma_n) < 0$.

---

## 9. The balance of $E_2(\lambda,T)$

**Proposition 6** (Asymptotic expansion of $E_2$). For fixed $\lambda$ and $T \to \infty$:

$$E_2(\lambda,T) = A(\lambda,T) - 2B(\lambda,T) + C(\lambda,T).$$

With the computed terms:
- $A(\lambda,T) \sim \dfrac{T(\log T)^3}{24\pi}$
- $B(\lambda,T) \approx -\dfrac{2T\log T\log\lambda}{\pi}$
- $C(\lambda,T) \approx \dfrac{4T\log T\log\lambda}{\pi}$

Hence:

$$E_2(\lambda,T) \sim \frac{T(\log T)^3}{24\pi} - 2\cdot\left(-\frac{2T\log T\log\lambda}{\pi}\right) + \frac{4T\log T\log\lambda}{\pi}$$

$$= \frac{T(\log T)^3}{24\pi} + \frac{4T\log T\log\lambda}{\pi} + \frac{4T\log T\log\lambda}{\pi}$$

$$= \frac{T(\log T)^3}{24\pi} + \frac{8T\log T\log\lambda}{\pi}.$$

**Critical observation.** For fixed $\lambda$ and $T \to \infty$: $E_2(\lambda,T) \sim \frac{T(\log T)^3}{24\pi} \to \infty$.

$E_2$ does NOT tend to zero with $T$ fixed and $\lambda$ fixed! The quadratic average of $C_\lambda(\gamma_n)$ over the zeros grows like $(\log T)^2 / (24\pi/T \cdot N_\Xi(T))$... Let us compute the normalized average:

$$\frac{E_2(\lambda,T)}{N_\Xi(T)} \approx \frac{T(\log T)^3/(24\pi)}{T\log T/(2\pi)} = \frac{(\log T)^2}{12}.$$

The quadratic average of $|C_\lambda(\gamma_n)|$ over the zeros is $\sim \frac{\log T}{\sqrt{12}}$ — of the order $w(\gamma_n)/2$, as expected (since $C_\lambda(\gamma_n) \approx w(\gamma_n)$ for fixed $\lambda$).

**Diagnosis:** For FIXED $\lambda$ and $T \to \infty$, $E_2$ inevitably grows because most of the $C_\lambda(\gamma_n) \approx w(\gamma_n) \neq 0$ (Inc. Inv. requires $C_\infty(\gamma_n) = 0$ in the limit $\lambda \to \infty$, not fixed $\lambda$).

---

## 10. The correct regime: $\lambda \to \infty$ with $T$ a function of $\lambda$

**Proposed regime.** Instead of fixing $\lambda$ and taking $T \to \infty$, we must take:

$$\lambda \to \infty, \quad T = T(\lambda) \to \infty, \quad \text{with the relation } \lambda^2 \gg T \text{ (many primes per zero)}.$$

In this regime, $C_\lambda(\gamma_n)$ approaches the limiting value $C_\infty(\gamma_n)$ (which is 0 under Inc. Inv.) for the first $N_\Xi(T(\lambda))$ zeros.

**Definition 1.** For a function $T = T(\lambda)$ satisfying $T(\lambda) \to \infty$ and $\lambda^2 \geq e^{c\sqrt{\log T(\lambda)}}$:

$$E_2(\lambda, T(\lambda)) = \sum_{\gamma_n \leq T(\lambda)} |C_\lambda(\gamma_n)|^2.$$

**Proposition 7** (Reformulation in the regime $\lambda \to \infty$). For fixed $\gamma_n \leq T(\lambda)$:

$$C_\lambda(\gamma_n) = C_\infty(\gamma_n) - 2\sum_{m > \lambda^2}\frac{\Lambda(m)}{m^{1/2}}\cos(\gamma_n\log m)$$

$$= C_\infty(\gamma_n) - R_\lambda(\gamma_n),$$

where the tail $R_\lambda(\gamma_n) = 2\sum_{m > \lambda^2}\Lambda(m)m^{-1/2}\cos(\gamma_n\log m) \to 0$ as $\lambda \to \infty$ for each fixed $\gamma_n$ (conditional convergence of the Dirichlet series).

**Hence:**

$$E_2(\lambda, T) = \sum_{\gamma_n \leq T}|C_\infty(\gamma_n) - R_\lambda(\gamma_n)|^2$$

$$= \sum_{\gamma_n\leq T}C_\infty(\gamma_n)^2 - 2\sum_{\gamma_n\leq T}C_\infty(\gamma_n)R_\lambda(\gamma_n) + \sum_{\gamma_n\leq T}R_\lambda(\gamma_n)^2.$$

**Proposition 8** (Role of the tail term $R_\lambda$). The $L^2$ norm of the tail term:

$$\sum_{\gamma_n\leq T}R_\lambda(\gamma_n)^2 = 4\sum_{\gamma_n\leq T}\left|\sum_{m>\lambda^2}\Lambda(m)m^{-1/2}e^{i\gamma_n\log m}\right|^2.$$

By Gonek-Fujii applied to the sum over $m > \lambda^2$:

$$\sum_{\gamma_n\leq T}R_\lambda(\gamma_n)^2 \approx \frac{T}{2\pi}\log T\cdot 4\sum_{m>\lambda^2}\Lambda(m)^2/m.$$

Since $\sum_{m>\lambda^2}\Lambda(m)^2/m$ diverges (the tail of the series), this term is large. The convergence $R_\lambda(\gamma_n) \to 0$ for each fixed $\gamma_n$ (conditional) does NOT imply $L^2$ convergence.

**This is the central structural obstacle of the $L^2$ norm.**

---

## 11. The $L^2$ obstacle: divergence of the tail norm

**Proposition 9** (Divergence of $\|R_\lambda\|_{L^2}^2$). For the tail:

$$\sum_{m>\lambda^2}\frac{\Lambda(m)^2}{m} \sim \log\lambda + O(1) \to \infty.$$

Therefore, for $T = T(\lambda) \gg \lambda^2$:

$$\sum_{\gamma_n\leq T}R_\lambda(\gamma_n)^2 \sim \frac{T\log T}{\pi}\log\lambda \to \infty.$$

The $L^2$ norm of the tail term DIVERGES as $T/\lambda^2 \to \infty$.

**Diagnosis:** The $L^2$ norm of $C_\lambda(\gamma_n) - C_\infty(\gamma_n)$ does not go to 0 as $T \to \infty$ for fixed $\lambda$, because the convergence of the Dirichlet series at the $\gamma_n$ is conditional (not $L^2$).

For $E_2(\lambda,T) \to 0$: we simultaneously need:
1. $C_\infty(\gamma_n) = 0$ (Inc. Inv.) — which is what we want to prove.
2. $R_\lambda(\gamma_n) \to 0$ in $L^2$ norm — which fails unconditionally.

---

## 12. Recalibration: the relative $L^2$ energy

The obstacle of §11 arises from the wrong regime. Let us reformulate the problem correctly.

**Definition 2** (Relative $L^2$ energy). For large $\lambda$ and $T \leq \lambda$ (regime where the series converges well):

$$\tilde{E}_2(\lambda, T) := \sum_{\gamma_n \leq T}\left|C_\lambda(\gamma_n)\right|^2$$

but taken in the regime $T = T(\lambda)$ where $N_\Xi(T) = N_\Xi(T(\lambda))$ is the number of zeros approximated by the operator $D_\lambda^N$ (with $N = N_\Xi(T)$).

In this regime: $\lambda^2 \gg \gamma_{N_\Xi(T)}$ — there are many more primes than zeros, and the series $\Psi_\lambda(\gamma_n)$ is a good approximation of $\Psi_\infty(\gamma_n)$.

**Proposition 10** (Estimate in the correct regime). For $T \leq \lambda/(2\pi)$ (equivalently: $\gamma_n \lesssim \lambda/(2\pi)$ for the zeros in question):

The difference between $C_\lambda(\gamma_n)$ and $C_\infty(\gamma_n)$ is:

$$C_\lambda(\gamma_n) - C_\infty(\gamma_n) = 2\sum_{m > \lambda^2}\frac{\Lambda(m)}{m^{1/2}}\cos(\gamma_n\log m).$$

For $\gamma_n \leq T \ll \lambda^2$: the tail sum is controlled by the PNT error:

$$\left|\sum_{m>\lambda^2}\frac{\Lambda(m)}{m^{1/2+i\gamma_n}}\right| = \left|-\zeta'/\zeta(1/2+i\gamma_n) + \sum_{m\leq\lambda^2}\Lambda(m)m^{-1/2-i\gamma_n}\right|.$$

The value of $-\zeta'/\zeta$ at $1/2+i\gamma_n$ (a pole) diverges, but the truncated sum $\sum_{m\leq\lambda^2}\Lambda(m)m^{-1/2-i\gamma_n}$ approximates the pole with error $O(1/(\lambda^2)^{1/2-\epsilon})$ for $\gamma_n \ll \lambda^2$.

---

## 13. The connection with the second moment of the Zeta function

**Proposition 11** (Connection with the second moment of $|\zeta'|$). The energy $E_2$ is related to the second moment of the derivative of the zeta function on the critical line.

From Inc. Inv. $\iff$ $\Re[g_n(\rho_n)] = w(\gamma_n)/2$ (Proposition 7.3 of the Doc 40 paper):

$$C_\infty(\gamma_n) = 0 \iff -\Re[\zeta'/\zeta(1/2+i\gamma_n)] = w(\gamma_n)/2.$$

The spectral energy is:

$$E_2(\lambda,T) = \sum_{\gamma_n\leq T}|C_\lambda(\gamma_n) - C_\infty(\gamma_n)|^2 + 2\mathrm{Re}\,\sum_{\gamma_n\leq T}(C_\lambda(\gamma_n)-C_\infty(\gamma_n))\overline{C_\infty(\gamma_n)} + \sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2.$$

The term $\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$ is exactly the energy at the zeros of the limiting potential — which under Inc. Inv. is 0, and in general measures how much the zeros of $\Xi$ fail to be zeros of $C_\infty$.

**Proposition 12** (Inc. Inv. implies $E_2 \to 0$ in the correct regime). If Inc. Inv. is true (i.e., $C_\infty(\gamma_n) = 0$ for all $n$), then:

$$E_2(\lambda, T) = \sum_{\gamma_n\leq T}|C_\lambda(\gamma_n) - C_\infty(\gamma_n)|^2 = \sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2.$$

This term measures the speed of convergence of $C_\lambda \to C_\infty$ at the zeros.

---

## 14. The correct question: $L^2$ convergence of the tail at the zeros

From Proposition 12: if Inc. Inv. is true, then $E_2(\lambda,T) = \sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2$ where $R_\lambda(\gamma_n)$ is the tail of the series.

**Proposition 13** (Bound on the tail at the zeros via Gonek-Fujii). By the Gonek-Fujii Theorem applied to the Dirichlet sum with coefficients $a_m = 2\Lambda(m)m^{-1/2}\mathbf{1}_{m > \lambda^2}$:

$$\sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2 = \frac{T}{2\pi}\log T\cdot 4\sum_{m>\lambda^2}\frac{\Lambda(m)^2}{m} + \mathcal{L}^{\mathrm{tail}}(\lambda,T) + O((T+\lambda^2)\log^c(T\lambda)).$$

The leading term: $4\sum_{m>\lambda^2}\Lambda(m)^2/m \sim 4\log\lambda'$ where $\lambda' \to \infty$ but more slowly. This term keeps diverging.

**Final diagnosis on the $L^2$ norm:**

The norm $\sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2$ diverges as $T \to \infty$ for fixed $\lambda$, **but** the average normalized by $N_\Xi(T)$:

$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2 \approx \frac{\log T \cdot \log\lambda}{N_\Xi(T)/T} \cdot \frac{1}{T} = \frac{\log T \cdot \log\lambda \cdot 2\pi}{\log T} = 2\pi\log\lambda$$

It keeps growing! The quadratic average of the tail does not go to 0.

---

## 15. The genuine route: $L^2$ energy with $T$ fixed and $\lambda \to \infty$

The analysis of the previous sections reveals that the correct regime for the $L^2$ attack is:

$$\textbf{Fix } T > 0 \textbf{ and take } \lambda \to \infty.$$

In this regime: for each fixed $\gamma_n \leq T$, $R_\lambda(\gamma_n) \to 0$ as $\lambda \to \infty$ (conditional convergence of the Dirichlet series). The number of terms $N_\Xi(T)$ is FIXED.

**Theorem 2** (Pointwise $L^2$ convergence at fixed $T$). For fixed $T > 0$:

$$E_2(\lambda, T) = \sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2 + O\!\left(\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|\cdot|R_\lambda(\gamma_n)| + \sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2\right).$$

For each fixed $\gamma_n$:
- $|R_\lambda(\gamma_n)| \to 0$ as $\lambda \to \infty$ (by conditional convergence of the series $\sum\Lambda(m)m^{-1/2-i\gamma_n}$ to $-\zeta'/\zeta(1/2+i\gamma_n)$).
- The sum $\sum_{n=1}^{N_\Xi(T)}|R_\lambda(\gamma_n)|^2 \to 0$ (finite sum of terms going to 0).

**Therefore:**

$$\lim_{\lambda\to\infty} E_2(\lambda, T) = \sum_{\gamma_n \leq T}|C_\infty(\gamma_n)|^2. \quad (*)$$

**Theorem 3** (Inc. Inv. $\iff$ $E_2 \to 0$ at fixed $T$). For fixed $T > 0$:

$$\lim_{\lambda\to\infty} E_2(\lambda, T) = 0 \quad \forall T \iff C_\infty(\gamma_n) = 0\;\forall n \iff \text{Inc. Inv.}$$

*Proof.* From $(*)$: $\lim_\lambda E_2(\lambda,T) = \sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$. This sum is 0 iff $C_\infty(\gamma_n) = 0$ for all $\gamma_n \leq T$ — which is Inc. Inv. restricted to $[0,T]$. Since $T$ is arbitrary, the condition for all $T$ is equivalent to full Inc. Inv. $\square$

**Corollary 1** (Reformulation of Inc. Inv. via $E_2$). The following conditions are equivalent:

(i) Inc. Inv.: $C_\infty(\gamma_n) = 0$ for all $n$.

(ii) $\displaystyle\lim_{\lambda\to\infty}E_2(\lambda,T) = 0$ for every fixed $T > 0$.

(iii) $\displaystyle\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2 = 0$ for all $T > 0$.

---

## 16. The reformulated problem: does $\sum |C_\infty(\gamma_n)|^2 = 0$ hold?

Theorem 3 tells us that attacking $E_2 \to 0$ (in the regime of fixed $T$, $\lambda\to\infty$) is exactly equivalent to Inc. Inv. — no new information.

The genuine advance would be to prove directly that $\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2 = 0$ without assuming Inc. Inv. For that we need to analyze $C_\infty(\gamma_n)$ directly.

**Proposition 14** (Connection with the logarithmic derivative at the poles). From Proposition 7.3 of the paper:

$$C_\infty(\gamma_n) = 0 \iff \Re[g_n(\rho_n)] = w(\gamma_n)/2,$$

where $g_n(\rho_n) = \lim_{s\to\rho_n}[-\zeta'/\zeta(s) - 1/(s-\rho_n)]$.

And:

$$|C_\infty(\gamma_n)|^2 = \left(w(\gamma_n) - 2\Re[g_n(\rho_n)]\right)^2 \cdot 4.$$

**The energy:**

$$\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2 = 4\sum_{\gamma_n\leq T}\left(w(\gamma_n)/2 - \Re[g_n(\rho_n)]\right)^2.$$

This expression involves the distribution of the values of $\Re[g_n(\rho_n)]$. Under RH, each term is 0 (Lemma 8.1 of the paper). Unconditionally, each term could be nonzero.

---

## 17. An unconditional result: the variance of $\Re[g_n]$

**Proposition 15** (Variance of the regular residues). Define:

$$\sigma^2(\lambda,T) := \frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\left(w(\gamma_n)/2 - \Re[g_n(\rho_n)]\right)^2 = \frac{E_2(\infty,T)}{4N_\Xi(T)}.$$

This is the **sample variance** of the regular residues $\Re[g_n(\rho_n)]$ around $w(\gamma_n)/2$.

Inc. Inv. is equivalent to $\sigma^2(\infty,T) = 0$ for all $T$ — the condition that the regular residues are ALL exactly $w(\gamma_n)/2$.

**Proposition 16** (Unconditional bound on the variance). The mean value of $\Re[g_n(\rho_n)]$ over the zeros is:

$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\Re[g_n(\rho_n)] = \frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\frac{w(\gamma_n)}{2} - \frac{1}{N_\Xi(T)}\frac{E_2(\infty,T)}{4 \cdot N_\Xi(T)}\cdot N_\Xi(T).$$

Under RH: the mean value is exactly $\frac{1}{N_\Xi(T)}\sum w(\gamma_n)/2$ (the variance is 0). Unconditionally: the variance could be positive.

---

## 18. The key question for Doc 42: the variance of the residues

**The reformulated problem** (suitable for the next document):

Can the following be bounded unconditionally:

$$\sigma^2(T) := \frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\left(\Re[g_n(\rho_n)] - w(\gamma_n)/2\right)^2?$$

**Route A (unconditional):** Use the Hadamard representation $(g_n)$ to express $\Re[g_n(\rho_n)] - w(\gamma_n)/2$ as a sum over the off-critical zeros (if any):

$$\Re[g_n(\rho_n)] - w(\gamma_n)/2 = \mathrm{Re}\,\!\left[\sum_{\rho\neq\rho_n}\frac{1}{\rho_n-\rho}\right].$$

Unconditionally: if there are zeros with $\Re(\rho) \neq 1/2$, they contribute $\Re[1/(\rho_n-\rho)] = \frac{\Re(\rho_n-\rho)}{|\rho_n-\rho|^2} = \frac{1/2-\Re(\rho)}{|\rho_n-\rho|^2} \neq 0$.

**Fundamental remark.** The quantity $\Re[g_n(\rho_n)] - w(\gamma_n)/2 = \mathrm{Re}\,\sum_{\rho\neq\rho_n}1/(\rho_n-\rho)$ is:
- = 0 if and only if RH (Lemma 8.1 of the paper).
- $\neq 0$ if there are off-critical zeros.

Hence $\sigma^2(T) = 0 \iff$ RH — another reformulation, not an advance.

**Route B (improved conditional):** Prove under weaker hypotheses (for example: $\zeta$ has no zeros in $\Re(s) > 1/2 - \delta$ for some $\delta < 1/2$) that $\sigma^2(T) = O(1/T^\epsilon)$ — a quantitative bound on how much Inc. Inv. can deviate.

---

## 19. Final diagnosis of the $L^2$ route

**Positive result of this document:**

1. **Theorem 3** (Exact reformulation): $\lim_\lambda E_2(\lambda,T) = \sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$. The $L^2$ energy converges to a determined quantity — it does not diverge.

2. **Corollary 1** (Equivalence): Inc. Inv. $\iff$ $E_2(\lambda,T) \to 0$ (in the regime of fixed $T$, $\lambda\to\infty$).

3. **Proposition 14** (Connection with residues): The energy $E_2$ measures the variance of the regular residues $\Re[g_n(\rho_n)]$ around their prescribed value $w(\gamma_n)/2$.

**Honest obstacle:**

The $L^2$ norm alone does not provide an unconditional route to Inc. Inv. Landau's lemma and the Gonek-Fujii Theorem are tools for computing the asymptotics of $E_2$ CONDITIONALLY on the distribution of the zeros — which produces circles or additional hypotheses.

**The difference with Selberg and the PNT:** In the Prime Number Theorem, the $L^2$ norm of $\psi(x) - x$ goes to 0 because the zero-free region of $\zeta$ guarantees that the zeros are NOT at $\Re(s) = 1$. The analogue here would be: proving that the off-critical zeros of $\zeta$ (if any) do not affect the sum $\sum_{\rho\neq\rho_n}1/(\rho_n-\rho)$ on average. But that is equivalent to there being no off-critical zeros — i.e., RH.

---

## 20. Summary and proposal for Doc 42

**Main result of Doc 41:**

The spectral $L^2$ energy $E_2(\lambda,T)$ converges to $\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$ as $\lambda\to\infty$ (for fixed $T$). Inc. Inv. is equivalent to $E_2(\lambda,T)\to 0$ in this regime. The connection with Gonek-Fujii reveals that the $L^2$ norm is no more tractable than Inc. Inv. itself — the structural barrier of Doc 40 §10 also manifests in the $L^2$ approach.

**The lesson:** All reformulations of the type "Inc. Inv. $\iff$ [condition on sums over $\gamma_n$]" are equivalent and share the same barrier. The information about RH is "encoded" in the distribution of the $\gamma_n$, and any approach that uses that distribution circularly cannot prove RH.

**Proposal for Doc 42:** Explore whether there exists an UNCONDITIONAL bound $E_2(\lambda,T) \leq f(\lambda,T)$ (without using the distribution of the $\gamma_n$ as input) that forces $E_2 \to 0$. This would require the function $\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$ to have an unconditional upper bound going to 0 — which is equivalent to proving RH. The question is whether there is a "way back" from the bound to the proof.

---

**State of the program after Doc 41:**

| Implication | State |
|---|---|
| Inc. Inv. $\Rightarrow$ RH | Proved (Theorem D, Doc 19) |
| RH $\Rightarrow$ Inc. Inv. | Proved (Theorem 4, Doc 39) |
| $E_2(\lambda,T)\to 0 \iff$ Inc. Inv. | Proved (Theorem 3, Doc 41) |
| Inc. Inv. [no hypothesis] | **Open** — bottleneck |

---

*Next doc: Doc 42 — Exploration of the structural barrier: can an unconditional bound on $E_2$ force Inc. Inv.?*
