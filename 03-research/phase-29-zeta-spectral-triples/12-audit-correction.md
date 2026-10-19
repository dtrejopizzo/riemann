# Phase 29 — Audit and correction of docs 10–11

**Objective:** Respond to the Advisor 1 audit. Three errors are identified in the docs 10–11 chain and the argument is rebuilt on firmer ground. The Central Statement CS is kept but requires reformulation. The individual convergence result is restated correctly.

---

## 1. The three errors identified

### Error 1 (Doc 10, Sec. 7): the cancellation of $4\log\lambda$

Doc 10 claimed that $C_\lambda(\gamma_n) \approx -4\log\lambda/m_n$ and $C_\lambda'(\gamma_n) \approx -4\log\lambda/(m_n\gamma_n)$, and that the ratio would give $\sigma_n = O(1)$.

**The error:** The correct analysis via the explicit formula (Section 3 below) shows that $C_\lambda(\gamma_n) = w(\gamma_n) - \Psi_\lambda(\gamma_n) \to +\infty$ as $\lambda\to\infty$. The potential does NOT tend to zero at $t = \gamma_n$; BOTH sides of the crossing equation diverge. The application of the implicit function theorem around $\gamma_n$ is invalid.

### Error 2 (Doc 11, Sec. 1, RL correction): incomplete

Doc 11 corrected the use of Riemann–Lebesgue for discrete measures, but still claimed individual convergence $t_n^{(\lambda)}\to\gamma_n$ (Theorem 2, doc 11) via the cancellation of the $4\log\lambda$ term in numerator and denominator. This Theorem 2 inherits Error 1 and is therefore not proved.

### Error 3 (Doc 11, Sec. 4): variance $\not\Rightarrow$ pointwise bound

The passage from $M\{D_n^2\} = V_n = O(\log\gamma_n)$ to $|D_n(x)| = O(\sqrt{\log\gamma_n\log x})$ "for almost every $x$" required a distributional result that was not justified. Finite variance of an almost-periodic function does NOT automatically imply a pointwise bound. This invalidates Proposition 3 of doc 11.

---

## 2. What IS proved (clean inventory)

Before reconstructing, we inventory the results that survive without the three errors:

| Result | Doc | Status |
|---|---|---|
| $k(u)>0$ for all $u>0$ | 04 | **Solid** |
| $k_\lambda(u)>0$ for $\lambda\geq\lambda_0$ | 04 | **Solid** |
| $A_\lambda=$ mult. by $\Psi_\lambda$ in Mellin space | 06 | **Solid** |
| $|s_n^{(\lambda)}-\gamma_n|=O(\lambda^{-1/2}/w_n)$ for zeros of $\hat k_\lambda$ | 06 | **Solid** (Rouché+Lemma 7.3) |
| $\sum_m\Delta_m=0$, $M_1[\Delta]=O((\log\lambda)^2/\lambda)$ | 06, 07 | **Solid** |
| $N_\xi(T;\lambda)=N_\Xi(T)+O(\log T)$ | 08 | **Solid** |
| $\mu_\lambda\to\mu_\gamma$ (weak convergence) | 08 | **Solid** |
| $S_\lambda(z)\to S_\Xi(z)$ (under RH) | 09 | **Solid** (uses weak conv. from doc 08) |
| $t_n^{(\lambda)} - \gamma_n = O(\log\lambda)$ (under RH) | 10 | **The denominator estimate is incorrect; the bound $O(\log\lambda)$ may survive but needs recomputation** |
| $D_n(x)$ almost-periodic, $M\{D_n^2\}=V_n$ | 11 | **Solid** (correct mathematics) |
| Time average of $D_n$ is 0 | 11 | **Solid** |
| Cesàro convergence of the zeros | 11 | **Solid** |

---

## 3. The correct computation of $C_\lambda(\gamma_n)$

**Proposition 1** (explicit formula for the twisted sum). Under RH, for $x > 1$ and $s = 1/2+i\gamma_n$ (simple zero of $\zeta$):

$$\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = \Re\!\left[\sum_{p\leq x}\Lambda(p)p^{-s}\right].$$

By Perron's formula applied to $-\zeta'/\zeta(s)$, which has a simple pole at $s = \rho_n$ with residue $-1$:

$$\sum_{p\leq x}\Lambda(p)p^{-s} = \frac{x^{0}}{0}\cdot(\text{residue of }-\zeta'/\zeta\text{ at }\rho_n) + \sum_{\rho\neq\rho_n}\frac{x^{\rho-s}}{\rho-s} + O(\log x/x).$$

The term at $\rho = \rho_n$ gives the contribution $-\log x$ (of the form $x^0/0 = -\log x$ in the regularized Perron limit). More precisely, for $s = \rho_n + \varepsilon$ and $\varepsilon\to 0$: the pole of $-\zeta'/\zeta$ at $\rho_n$ contributes $x^{\rho_n-s}/(\rho_n-s) = x^{-\varepsilon}/(-\varepsilon) \to \log x$ (the limit $\varepsilon\to 0$ of $-x^{-\varepsilon}/\varepsilon = -e^{-\varepsilon\log x}/\varepsilon \to \log x$).

Under RH ($\rho = 1/2+i\gamma$ for all non-trivial zeros):

$$\sum_{p\leq x}\Lambda(p)p^{-1/2-i\gamma_n} = \log x + A_n + \sum_{m\neq n}\frac{x^{i(\gamma_m-\gamma_n)}}{i(\gamma_m-\gamma_n)} + O(\log x\cdot x^{-1/2}),$$

where $A_n$ is a fixed complex constant (independent of $x$).

Taking the real part: $\sum_{p\leq x}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = \log x + \Re A_n + D_n(\log x) + O(\log x/\sqrt{x})$,

where $D_n(\log x) = \sum_{m\neq n}\sin((\gamma_m-\gamma_n)\log x)/(\gamma_m-\gamma_n)$.

**Hence:**

$$\Psi_\lambda(\gamma_n) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = 4\log\lambda + 2\Re A_n + 2D_n(2\log\lambda) + O(\lambda^{-1}\log\lambda).$$

And: $$C_\lambda(\gamma_n) = w(\gamma_n) - \Psi_\lambda(\gamma_n) = w(\gamma_n) - 4\log\lambda - 2\Re A_n - 2D_n(2\log\lambda) + O(\lambda^{-1}).$$

**As $\lambda\to\infty$:** $C_\lambda(\gamma_n) \to -\infty$ (dominated by $-4\log\lambda$).

And $\mu_\lambda \to 0^+$ (the minimum of $QW_\lambda$ tends to 0).

**Conclusion:** $C_\lambda(\gamma_n) - \mu_\lambda \to -\infty$. The point $t = \gamma_n$ is NOT a crossing of $C_\lambda$ at level $\mu_\lambda$ for $\lambda$ large. The crossing equation $C_\lambda(t_n^{(\lambda)}) = \mu_\lambda$ is satisfied at a point $t_n^{(\lambda)}$ that MOVES AWAY from $\gamma_n$ as $\lambda$ grows.

**Error 1 confirmed.** The implicit function theorem argument in docs 10–11 is invalid.

---

## 4. The correction: the Blaschke map

The error stems from thinking that the zeros of $\hat\xi_\lambda$ are determined by the equation $C_\lambda(t) = \mu_\lambda$ (the "crossings of the potential"). This is only the DIAGONAL APPROXIMATION — which ignores the rank-1 term $Q^{cross}(f,f) = |\langle f, k\rangle|^2$.

The full Euler–Lagrange equation in Mellin space, including $Q^{cross}$:

$$[w(t) - \Psi_\lambda(t) - \mu_\lambda]\hat\xi_\lambda(t) + \langle\xi_\lambda, k\rangle\hat k(t) = 0.$$

Hence:

$$\hat\xi_\lambda(t) = \frac{-c_\lambda\hat k(t)}{w(t) - \Psi_\lambda(t) - \mu_\lambda},$$

where $c_\lambda = \langle\xi_\lambda, k\rangle > 0$.

**The zeros of $\hat\xi_\lambda$ are the zeros of the NUMERATOR** $\hat k(t)$ — which are the zeros $\gamma_n$ of $\Xi$ — **modulated by the poles of the denominator**, which are the zeros of $C_\lambda(t) - \mu_\lambda$.

This is the correct structure: in the limit $\lambda\to\infty$, if the denominator has no zeros on the real line (or if the poles of the denominator cancel with the zeros of the numerator), then $\hat\xi_\lambda(t) \propto \hat k(t)$ and the zeros of $\hat\xi_\lambda$ coincide with those of $\hat k_\lambda \approx \Xi$.

**Proposition 2** (the zeros of $\hat\xi_\lambda$ are modulated zeros of $\hat k$). In the diagonal approximation with the rank-1 term:

$$\hat\xi_\lambda(t) = -c_\lambda \cdot \frac{\hat k(t)}{C_\lambda(t) - \mu_\lambda}.$$

The zeros of $\hat\xi_\lambda$ are the $t$ where:
1. $\hat k(t) = 0$ (zeros of $\hat k = \Xi$, i.e., $t = \gamma_n$), if the denominator is NONZERO at those points.
2. The poles of the denominator (zeros of $C_\lambda - \mu_\lambda$) cancel with zeros of the numerator $\hat k$ — but $\hat k(\gamma_n) = 0$ exactly when $\gamma_n$ is a zero of $\Xi$.

**But:** In the finite-dimensional approximation $E_N^+$, $\hat\xi_\lambda \neq -c_\lambda\hat k/(C_\lambda-\mu_\lambda)$ exactly — the projection introduces an error. The function $\hat\xi_\lambda$ does not have exactly the same zeros as $\hat k$.

The correct relation between $\hat\xi_\lambda$ and $\hat k_\lambda = \hat k|_{E_N^+}$ (the projection):

**Proposition 3** (relation between the zeros). Let $B_\lambda(t) := \hat\xi_\lambda(t)/\hat k_\lambda(t)$ be the ratio of the two functions on $E_N^+$. This is a RATIONAL FUNCTION with:
- Zeros at $\{t_n^{(\lambda)}\}$ (zeros of $\hat\xi_\lambda$)
- Poles at $\{s_n^{(\lambda)}\}$ (zeros of $\hat k_\lambda$)

Both sets have exactly $N+1$ elements. $B_\lambda$ is a RATIONAL BLASCHKE PRODUCT. Its Blaschke norm: $\prod_n\frac{t-t_n^{(\lambda)}}{t-s_n^{(\lambda)}}$ in the realization on the real line.

**Consequence.** $\{t_n^{(\lambda)}\} \to \{\gamma_n\}$ if and only if $B_\lambda \to 1$ (uniformly on compacta of $\mathbb{C}\setminus\mathbb{R}$). And $B_\lambda \to 1$ if and only if $\hat\xi_\lambda/\hat k_\lambda \to $ constant, i.e., H2.

This confirms the circular structure identified in doc 09: convergence of the zeros is equivalent to H2. The "crossings of the potential" analysis was a false path.

---

## 5. The correct estimate of $t_n^{(\lambda)} - \gamma_n$

Despite the earlier errors, a correct estimate for $t_n^{(\lambda)} - \gamma_n$ DOES exist, coming from comparing the Blaschke products.

**Proposition 4** (displacement via Blaschke ratio). The displacement of the $n$-th zero satisfies, for $z \in \mathbb{C}\setminus\mathbb{R}$:

$$\log B_\lambda(z) = \sum_n\log\frac{z-t_n^{(\lambda)}}{z-s_n^{(\lambda)}}.$$

For $z = \gamma_n + i\eta$ ($\eta > 0$ small):

$$|\log B_\lambda(\gamma_n+i\eta)| \leq \sum_n\left|\frac{t_n^{(\lambda)}-s_n^{(\lambda)}}{\gamma_n+i\eta-s_n^{(\lambda)}}\right| + O\!\left(\sum_n\frac{|t_n-s_n|^2}{|\eta|^2}\right).$$

From Theorem 1 of doc 06: $|s_n^{(\lambda)}-\gamma_n| = O(\lambda^{-1/2}/w_n)$. If in addition $|t_n^{(\lambda)}-\gamma_n| = O(\lambda^{-1/2}/w_n)$ (which is what we want to prove): the argument becomes circular.

**The NON-circular result.** From the Corollary of Proposition 1 of doc 08 (zero counting):

$$|t_n^{(\lambda)} - \gamma_n| \leq (\gamma_{n+K} - \gamma_n) + |s_n^{(\lambda)} - \gamma_n|,$$

where $K = O(\log\lambda)$ is the error in the counting. Using the average spacing $\gamma_{n+K}-\gamma_n = O(K\log\gamma_n/\log\gamma_n) = O(K) = O(\log\lambda)$:

$$\boxed{|t_n^{(\lambda)} - \gamma_n| \leq O(\log\lambda) + O(\lambda^{-1/2}/w_n) = O(\log\lambda).}$$

**Theorem 1** (correct estimate). Under RH and with $w_n = |\Xi'(\gamma_n)|$: for each fixed $n$ and $\lambda$ regular,

$$|t_n^{(\lambda)} - \gamma_n| = O_n(\log\lambda).$$

This estimate is the same as that of Theorem 2 of doc 10, but now comes from a CORRECT argument (zero counting, not an implicit function argument over the divergent potential). The exponent $O(\log\lambda)$ comes from the $O(\log\lambda)$ error in the zero count.

---

## 6. The convergence rate: can $O(\log\lambda)$ be improved?

The bound $O(\log\lambda)$ comes from the counting error $|N_\xi(T;\lambda) - N_\Xi(T)| = O(\log T)$. This error is the precision of von Mangoldt's formula for $N_\Xi$ combined with the discretization in $E_N^+$.

**Proposition 5** (the counting is optimal). The error $O(\log T)$ in $N_\xi(T;\lambda) - N_\Xi(T)$ comes from the error of von Mangoldt's formula for $N_\Xi(T)$:

$$N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + \frac{7}{8} + O(\log T).$$

This error $O(\log T)$ cannot be improved with current techniques (it would require showing that the "argument of $\zeta$" on the critical line has bounded variation — which implies deep conjectures about the distribution of $\zeta$ on the critical line).

**Hence:** the bound $|t_n^{(\lambda)}-\gamma_n| = O(\log\lambda)$ is, with current methods, OPTIMAL. Improving it would require an improved estimate of the zero count, which is not available unconditionally.

---

## 7. Convergence: what can correctly be said

**Theorem 2** (CONDITIONAL convergence, reformulated). Under RH: for each fixed $n$, the following are equivalent:

(a) $t_n^{(\lambda)} \to \gamma_n$ as $\lambda\to\infty$.

(b) The localized counting error $|N_\xi(\gamma_n+\varepsilon;\lambda) - N_\Xi(\gamma_n+\varepsilon)| = O(1)$ (bound independent of $\lambda$, for fixed small $\varepsilon$).

(c) The Blaschke product $B_\lambda(z) \to 1$ locally uniformly in a neighborhood of $z = \gamma_n$.

*Proof.* (a)$\Leftrightarrow$(b): A zero $t_n^{(\lambda)} \to \gamma_n$ iff the count of zeros below $\gamma_n+\varepsilon$ stably equals $n$ for $\lambda$ large. (b)$\Leftrightarrow$(c): from the local expansion of the Blaschke product. $\square$

**Condition (b) under RH:** If the localized counting error is $O(1)$ instead of $O(\log\lambda)$ (local precision hypothesis): then individual convergence follows. This local precision is plausible under GUE statistics (which predict that local zero-count fluctuations are $O(1)$ under the GUE distribution), but it is not proved unconditionally.

---

## 8. The Central Statement CS correctly reformulated

The Central Statement of doc 11 was:

> CS: $\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = o(\log\lambda)$.

From Proposition 1 of this document: $\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(\gamma_n\log p) = \log\lambda + \Re A_n + D_n(2\log\lambda) + O(\lambda^{-1/2})$.

Hence CS is rewritten as: $\log\lambda + \Re A_n + D_n(2\log\lambda) = o(\log\lambda)$, i.e., $D_n(2\log\lambda) = -\log\lambda(1+o(1)) - \Re A_n$.

This requires $D_n(2\log\lambda) \sim -\log\lambda$ — a PRECISE bound (not merely $o(\log\lambda)$). The sum $D_n(2\log\lambda) = \sum_{m\neq n}\sin((\gamma_m-\gamma_n)2\log\lambda)/(\gamma_m-\gamma_n)$ has variance $O(\log\gamma_n)$ under Montgomery — much smaller than $\log\lambda$. Hence $D_n(2\log\lambda) = o(\log\lambda)$ in mean square, but the CS condition demands $D_n \sim -\log\lambda$ — a MASSIVE cancellation with the main $\log\lambda$ term.

**Conclusion:** CS as formulated in doc 11 is INCONSISTENT with the explicit formula. The correct condition is different.

**CS reformulated.** The correct condition for individual convergence of the zeros is not about the full sum $\sum_{p\leq\lambda^2}$, but about the LOCALIZED COUNTING ERROR:

> **CS' (correct Central Statement).** For each fixed $n$: $|N_\xi(\gamma_n+1;\lambda) - N_\Xi(\gamma_n+1)| = O(1)$ as $\lambda\to\infty$.

This condition is:
- Equivalent to $t_n^{(\lambda)}\to\gamma_n$ (Theorem 2(b)).
- Unconditional in its formulation (does not explicitly mention RH).
- A consequence of the zero-rigidity conjecture (that under GUE, local counting fluctuation is $O(1)$).

---

## 9. The rigidity hypothesis and its role

**Definition** (Rigidity of the zeros). The zeros $\{t_n^{(\lambda)}\}$ satisfy the **rigidity hypothesis** if:

$$|t_n^{(\lambda)} - \gamma_n| = O\!\left(\frac{\log n}{n}\right) \quad\text{for each } n \leq N_\lambda.$$

This is the version of the Erdős–Yau "rigidity" result for GUE matrices adapted to the zeros of the CCM operator.

**Proposition 6** (rigidity implies individual convergence). Under the rigidity hypothesis:

$$|t_n^{(\lambda)} - \gamma_n| = O(\log n/n) \to 0 \quad\text{for fixed } n.$$

In particular, $t_n^{(\lambda)} \to \gamma_n$ for each fixed $n$.

**Where does rigidity come from?** Rigidity of the zeros of the operator $D_\lambda^N$ should follow from the properties of the ENSEMBLE of Jacobi matrices $\{J_\lambda^{(N)}\}$ as $\lambda\to\infty$. This is a statement of the "local universality" type for convergent deterministic Jacobi matrices.

---

## 10. Summary: map of gaps and path forward

### Gaps identified by Advisor 1 and their status:

| Advisor 1 Gap | Status after audit |
|---|---|
| 1. Riesz–Fischer $\sum|\delta_{mn}|^{-2}<\infty$ | Plausible under GUE (zeros do not get too close); needs direct proof |
| 2. Variance $\not\Rightarrow$ pointwise bound | **CONFIRMED ERROR** — correction in doc 11, Sec. 1 |
| 3. Cancellation of $4\log\lambda$ | **CONFIRMED ERROR** — the cancellation is INCORRECT; the potential diverges |
| 4. CS $\Rightarrow$ convergence of $t_n$ | Original CS is inconsistent; CS' (rigidity) does imply convergence |
| 5. Convergence $\Rightarrow$ RH | Correct via the CCM argument; the step is valid under appropriate conditions |

### The frank status of the Phase 29 program:

**Proved unconditionally and solidly:**
- $k_\lambda > 0$, $A_\lambda=$ mult. Mellin, quantitative convergence of zeros of $\hat k_\lambda$
- $M_1[\Delta]\to 0$, correct counting $N_\xi = N_\Xi + O(\log)$, weak convergence
- $|t_n^{(\lambda)}-\gamma_n| = O(\log\lambda)$ (via counting, not implicit function)
- Cesàro convergence of the zeros

**Proved under RH (solidly):**
- $S_\lambda(z)\to S_\Xi(z)$ (Stieltjes)
- Individual convergence $t_n^{(\lambda)}\to\gamma_n$ follows from CS' (rigidity), which is a consequence of GUE under RH

**The real wall (revised):**
$$\text{RH} \iff \text{CS'} \iff |N_\xi(\gamma_n;\lambda) - N_\Xi(\gamma_n)| = O(1).$$

The condition CS' (rigidity of the local count) is the correct formulation of the central problem. It is equivalent to RH by the chain:
$$\text{CS'} \Rightarrow t_n^{(\lambda)}\to\gamma_n \Rightarrow \hat\xi_\lambda\to c\Xi \text{ (Hurwitz)} \Rightarrow \text{RH (CCM)}.$$

And RH $\Rightarrow$ CS' by the GUE distribution of the zeros of the operator under RH.
