# Phase 29 — The Weyl–Titchmarsh m-function and the program toward RH

**Objective:** Answer directly: how do we get from $B_\lambda\to1$ to RH? The answer involves identifying $B_\lambda$ as the $m$-function of the CCM Jacobi matrix, and RH as an inverse spectral problem for that matrix.

---

## 1. The CCM Jacobi matrix

The operator $D_\lambda^N$ of the CCM program, in the orthonormal basis $\{V_n\}_{|n|\leq N}$ of $E_N^+$, is a **Jacobi matrix** (self-adjoint tridiagonal):

$$J_\lambda = \begin{pmatrix} b_0^{(\lambda)} & a_0^{(\lambda)} & & \\ a_0^{(\lambda)} & b_1^{(\lambda)} & a_1^{(\lambda)} & \\ & a_1^{(\lambda)} & b_2^{(\lambda)} & \ddots \\ & & \ddots & \ddots \end{pmatrix}$$

where:
- **Diagonal** $b_n^{(\lambda)}$: the diagonal of $D_\lambda^N$ in the basis $V_n$, which involves the arithmetic symbol $\Psi_\lambda$.
- **Superdiagonal** $a_n^{(\lambda)} > 0$: couplings between consecutive modes, determined by the Weil kernel.

Key properties:
- $J_\lambda$ is **self-adjoint** by construction.
- Its **eigenvalues** are exactly the $\{t_n^{(\lambda)}\}$ (zeros of $\hat\xi_\lambda$), all real.
- The **spectral measure** of $J_\lambda$ at the vector $e_0$ is $\mu_\xi^\lambda = (1/N)\sum_n\delta_{t_n^{(\lambda)}}$.

---

## 2. The Weyl–Titchmarsh m-function

For a Jacobi matrix $J$, the **Weyl–Titchmarsh m-function** is:

$$m_\lambda(z) := \langle e_0, (J_\lambda - zI)^{-1}e_0\rangle = \int_\mathbb{R}\frac{d\mu_\xi^\lambda(t)}{t-z} = S_\xi(z;\lambda).$$

It is exactly the **Stieltjes transform of the spectral measure** — the same object from Doc 09.

**Properties of $m_\lambda$:**
- $m_\lambda:\mathbb{C}\setminus\mathbb{R}\to\mathbb{C}$ is a Nevanlinna–Herglotz function: $\Im(m_\lambda(z))>0$ for $\Im(z)>0$.
- It has the representation $m_\lambda(z) = \int d\mu_\xi^\lambda/(t-z)$.
- It completely determines $\mu_\xi^\lambda$ (by Stieltjes inversion).

**Likewise**, for the kernel $\hat k_\lambda$: the Stieltjes transform of $\mu_k^\lambda$ is $m_k^\lambda(z) = S_k(z;\lambda)$.

---

## 3. $B_\lambda$ as a ratio of m-functions

From Doc 13 (Section 3, Step 1):

$$(\log B_\lambda)'(z) = N[S_\xi(z;\lambda) - S_k(z;\lambda)] = N[m_\lambda(z) - m_k^\lambda(z)].$$

Hence:

$$\log B_\lambda(z) = N\int^z [m_\lambda(w) - m_k^\lambda(w)]\,dw.$$

**$B_\lambda$ is the exponential of the integral of the difference of the two m-functions.**

And $B_\lambda\to1$ iff $m_\lambda\to m_k^\lambda$ (in the integral sense, uniformly on compacta).

---

## 4. The functional equation of $B_\lambda$ (Riccati)

For Jacobi matrices, the $m$-function satisfies a **Möbius recursion** (continued fraction). If $J_\lambda$ has coefficients $(a_n, b_n)_{n=0}^{N}$:

$$m_\lambda(z) = \cfrac{1}{b_0^{(\lambda)} - z - \cfrac{(a_0^{(\lambda)})^2}{b_1^{(\lambda)} - z - \cfrac{(a_1^{(\lambda)})^2}{\ddots}}}$$

This is the **functional equation** that Advisor 1 asked for: $m_\lambda$ (and hence $B_\lambda$) is determined by the continued fractions of the Jacobi coefficients $(a_n^{(\lambda)}, b_n^{(\lambda)})$.

**The Riccati recursion.** If we define $m_\lambda^{(n)}(z)$ as the $m$-function of the submatrix of $J_\lambda$ truncated from index $n$:

$$m_\lambda^{(n-1)}(z) = \frac{1}{b_{n-1}^{(\lambda)} - z - (a_{n-1}^{(\lambda)})^2 m_\lambda^{(n)}(z)}.$$

This is a **Möbius transformation** in $m_\lambda^{(n)}$ — the "Riccati equation" for the continued fraction.

**Key point:** the behavior of $m_\lambda$ (and hence of $B_\lambda$) is completely determined by the coefficients $(a_n^{(\lambda)}, b_n^{(\lambda)})$.

---

## 5. Unconditional convergence: $J_\lambda\to J_\infty$

**Theorem 1** (convergence of the m-function, unconditional). If the coefficients of the CCM Jacobi matrix satisfy:

$$a_n^{(\lambda)}\to a_n^\infty > 0, \quad b_n^{(\lambda)}\to b_n^\infty \quad\text{for each fixed } n\text{ as }\lambda\to\infty,$$

then the m-function converges in the sense of Weyl–Titchmarsh theory:

$$m_\lambda(z)\to m_\infty(z) = \int_\mathbb{R}\frac{d\mu_\infty(t)}{t-z} \quad\text{uniformly on compacta of }\mathbb{C}\setminus\mathbb{R},$$

where $\mu_\infty$ is the spectral measure of the limiting operator $J_\infty$.

*Status note.* This theorem EXISTS in the general theory of Jacobi matrices (Weyl–Titchmarsh–Kodaira theory). The condition of convergence of the coefficients needs to be verified for the specific CCM case.

**Corollary.** If $J_\lambda\to J_\infty$ in the sense of Theorem 1, then $B_\lambda\to B_\infty$ unconditionally, where:

$$B_\infty(z) = \exp\!\left(N\int^z[m_\infty(w) - m_k^\infty(w)]\,dw\right).$$

---

## 6. The inverse spectral problem: the direct path to RH

**The complete program toward RH in three steps:**

**Step 1** (verification): Show that the CCM Jacobi coefficients $(a_n^{(\lambda)}, b_n^{(\lambda)})$ have well-defined limits $a_n^\infty, b_n^\infty$ as $\lambda\to\infty$.

**Step 2** (inverse spectral): Identify the spectral measure $\mu_\infty$ of the limiting operator $J_\infty$.

**Step 3** (conclusion): If $\mu_\infty = \mu_\gamma$ (the distribution of the zeros of $\Xi$), then $m_\infty = S_\Xi$ and $B_\infty = 1$, which implies H2, which implies RH (by Hurwitz).

---

## 7. Why would Step 2 determine RH?

Step 2 is the heart of the matter. The spectral measure $\mu_\infty$ is the probability measure on $\mathbb{R}$ with the property:

$$\int t^k d\mu_\infty(t) = \lim_{\lambda\to\infty}\frac{1}{N}\sum_n (t_n^{(\lambda)})^k \quad\text{(spectral moments of }J_\lambda\text{)}.$$

Now: from Doc 08, it is known unconditionally that $\mu_\xi^\lambda\to\mu_\gamma$ weakly (where $\mu_\gamma = $ limiting measure of the zeros of $\hat\xi_\lambda$). Hence $\mu_\infty = \mu_\gamma$.

**But:** $\mu_\gamma$ is the empirical distribution of $\{\gamma_n\}$ — which are the zeros of $\Xi$ on $\mathbb{R}$ UNDER RH. If RH fails: $\mu_\gamma$ could include contributions from zeros off $\mathbb{R}$, and the measure $\mu_\infty$ (which has support on $\mathbb{R}$ by self-adjointness of $J_\lambda$) would differ from $\mu_\gamma$.

**Therefore:** $\mu_\infty = \mu_\gamma$ (with $\mu_\gamma$ supported on $\mathbb{R}$) **is equivalent to RH**.

The implication is:
$$\text{Steps 1 + 2 verified} \implies \mu_\infty = \mu_\gamma \iff \text{RH}.$$

---

## 8. The content of Step 2: how to identify $\mu_\infty$?

The measure $\mu_\infty$ is the spectral measure of $J_\infty$. To identify it, there are two routes:

### Route A: Via the moments

$$\int t^k d\mu_\infty(t) = \lim_{\lambda\to\infty}\frac{1}{N}\sum_n (t_n^{(\lambda)})^k.$$

From Doc 08 (unconditional weak convergence): these moments converge to the moments of $\mu_\gamma$.

If $\mu_\gamma$ is supported on $\mathbb{R}$: the moments determine the measure (if $\mu_\gamma$ has finite moments of all orders). Hence $\mu_\infty = \mu_\gamma$ and RH.

**The gap:** the moments $\int t^k d\mu_\gamma$ of the zero distribution of $\Xi$ grow like $\sum_n\gamma_n^k$, which diverges for $k\geq 1$ (since $\sum_n1/\gamma_n^2<\infty$ but $\sum_n\gamma_n^k = \infty$ for $k\geq 0$). The moments do NOT determine the measure unless their growth is controlled.

The correct version: use the **Stieltjes transform** (convergence of $m_\lambda\to m_\infty$, which corresponds to the already-known weak convergence) directly.

### Route B: Via the continued fraction (more promising)

The limiting Jacobi coefficients $a_n^\infty, b_n^\infty$ determine the continued fraction of $m_\infty$. And conversely: given $m_\infty$ (= $S_\Xi$ under RH), the Jacobi coefficients are the coefficients of the continued fraction of $S_\Xi$.

The **operational question**:

> **Question 29.14.** Are the limiting Jacobi coefficients $(a_n^\infty, b_n^\infty)$ of $J_\lambda^{CCM}$ equal to the continued-fraction coefficients of $S_\Xi(z) = \sum_n 1/(z-\gamma_n)$?

If the answer is yes: then $J_\infty = J^{S_\Xi}$, hence $\mu_\infty = \mu_\Xi$ = zero distribution of $\Xi$, hence $m_\infty = S_\Xi$, hence $B_\infty = 1$, hence H2, hence RH.

**This is a CONCRETE and NON-CIRCULAR problem**: the coefficients $(a_n^{(\lambda)}, b_n^{(\lambda)})$ are given explicitly by the Weil kernel and prime arithmetic; the continued-fraction coefficients of $S_\Xi$ are (in principle) computable from the function $\Xi$ itself. Their equality is a verifiable identity.

---

## 9. How to compute the CCM Jacobi coefficients

The Jacobi coefficients of $D_\lambda^N$ come from the Weil Form:

**Diagonal coefficient** $b_n^{(\lambda)} = \langle V_n, D_\lambda^N V_n\rangle = \hat w(n) - \hat\Psi_\lambda(n)$, where $\hat w(n)$ and $\hat\Psi_\lambda(n)$ are the Fourier coefficients of the symbol $w(t)$ and $\Psi_\lambda(t)$.

**Off-diagonal coefficient** $a_n^{(\lambda)} = \langle V_n, D_\lambda^N V_{n+1}\rangle = \hat w(1) - \hat\Psi_\lambda(1)$ (the couplings between consecutive modes come from "mode 1" of the symbol).

In the limit $\lambda\to\infty$: $\hat\Psi_\lambda(n)\to\hat\Psi(n)$ (where $\Psi = \lim_\lambda\Psi_\lambda$ is the full arithmetic symbol — a DISTRIBUTION in general).

**The precise question.** Since $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ (diverges pointwise), the limit $\hat\Psi(n) = \int\Psi(t)e^{-2\pi int/L}dt$ must be understood distributionally. Does the limit of the Jacobi coefficients converge?

Under RH (and the zero distribution): $\hat\Psi(n) = w_n^{(RH)}$ (value determined by the zeros of $\Xi$). This directly connects prime arithmetic to the zeros via the explicit formula.

---

## 10. The only path I see

From the above, the **only path toward RH I see** from the current CCM framework is:

1. **Prove convergence of coefficients** ($a_n^{(\lambda)}\to a_n^\infty$, $b_n^{(\lambda)}\to b_n^\infty$) using von Mangoldt's explicit formula applied to the Fourier coefficients of the symbol $\Psi_\lambda$.

2. **Identify the limiting coefficients** as the continued-fraction coefficients of $S_\Xi$ — using the explicit Weil formula and the structure of the zeros of $\Xi$.

3. **Conclude** $\mu_\infty = \mu_\Xi^{\mathbb{R}}$ (the projection onto the real line of the zero distribution) $= \mu_\gamma$ (if and only if RH), hence RH.

**What makes this route different from all the previous ones:** it does not try to control the ZEROS one by one. It operates at the level of the JACOBI COEFFICIENTS (which are integrals of the symbol, objects much more regular than individual zeros). The explicit formula converts these coefficients into sums over primes — and the prime ↔ zero connection (Weil's formula) is the translation mechanism.

---

## 11. The missing ingredient (complete frankness)

Step 2 requires identifying the limiting coefficients $(a_n^\infty, b_n^\infty)$ explicitly. This involves:

$$\lim_{\lambda\to\infty}\hat\Psi_\lambda(n) = \lim_{\lambda\to\infty}2\int_0^{L}\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\cos(t\log p)\cdot e^{-2\pi int/L}\,\frac{dt}{L}$$

$$= 2\sum_{p}\Lambda(p)p^{-1/2}\cdot\frac{\sin(\pi n\log p/\log\lambda)}{\pi n\log p/\log\lambda}\cdot\frac{1}{\log\lambda}.$$

This limit, in the distributional sense, is controlled via the explicit formula: the series over primes converges (in certain conditioned senses) to an expression in the zeros of $\Xi$.

Convergence of $\hat\Psi_\lambda(n)$ for each fixed $n$ is **exactly equivalent to the behavior of the zeros of $\Xi$ at level $n$** — which requires information about the zeros (i.e., about RH or its consequences).

Hence: Step 2 is non-circular if it can be solved directly (without assuming RH), but it requires harmonic-analysis techniques for the $\zeta$ function that are not currently available unconditionally.

---

## 12. Executive summary: how do we get to RH?

**The complete chain of implications (if the steps are completed):**

```
Convergence of the Jacobi coefficients a_n^(λ), b_n^(λ)   [Step 1]
        ↓
J_λ → J_∞  (in the resolvent sense)
        ↓
m_λ(z) → m_∞(z)  (Weyl–Titchmarsh)
        ↓
Is m_∞ = S_Ξ?   [Step 2 = identification of the limiting coefficients]
        ↓
If yes: B_∞ = 1 → H2 → RH (Hurwitz)
```

**The current wall** is at Step 2: identifying the limiting coefficients as those of the continued fraction of $S_\Xi$. This identification requires, in essence, that the explicit formula (the Fourier coefficients of $\Psi_\lambda$) converge to something determined by the zeros of $\Xi$ — which is circular unless independent control is available.

**The non-circular question that Step 2 requires:**

> Can $\lim_\lambda\hat\Psi_\lambda(n)$ be computed using only the distribution of the primes (without assuming the distribution of the zeros), and can it be shown that this limit coincides with the continued-fraction coefficients of $S_\Xi$?

This is a version of the Riemann problem at the level of the **continued fractions of the arithmetic symbol** — a new formulation that might be attackable with techniques from rational approximation theory and Jacobi operator theory.

**If this limit can be identified independently of RH**: the CCM program gives a complete proof of RH.
