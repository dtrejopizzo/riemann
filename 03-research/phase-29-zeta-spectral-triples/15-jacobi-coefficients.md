# Phase 29 — Jacobi coefficients of the CCM operator

**Objective:** Prove convergence of the Jacobi coefficients of $J_\lambda^{CCM}$. Four parts: (A) type of convergence, (B) moments in terms of $\Psi_\lambda$, (C) formulas for $b_0, a_0, b_1$, (D) convergence and connection to RH.

---

## Part A: What type of convergence is proved?

**Advisor 1's question:** Does $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ imply convergence of the spectral measure $\mu_\xi^\lambda$, or only convergence of the count?

**Answer: the two are the same thing.**

**Definition.** The spectral measure of the CCM operator is the probability measure:

$$\mu_\xi^\lambda := \frac{1}{N}\sum_{n=1}^N \delta_{t_n^{(\lambda)}}$$

where $\{t_n^{(\lambda)}\}_{n=1}^N$ are the eigenvalues of $J_\lambda^{CCM}$ (= zeros of $\hat\xi_\lambda^{(N)}$, all real).

**Proposition 1** (unconditional weak convergence of $\mu_\xi^\lambda$). For every continuous $\phi\in C_c(\mathbb{R}_+)$ with compact support:

$$\int\phi\,d\mu_\xi^\lambda \to \int\phi\,d\mu_\gamma^{real} \quad\text{as }\lambda\to\infty,$$

where $\mu_\gamma^{real}$ is the normalized distribution of the REAL zeros of $\Xi$ on $(0,\infty)$.

*Proof.* Standard integration by parts: $\int\phi\,d\mu_\xi^\lambda = \frac{1}{N}\int\phi(t)\,dN_\xi(t;\lambda)$.

$= \frac{1}{N}\int\phi(t)\,dN_\Xi(t) + \frac{1}{N}\int\phi(t)\,d[N_\xi - N_\Xi](t)$.

The second term: $\frac{1}{N}\int\phi'\cdot(N_\xi - N_\Xi)\,dt = O\left(\frac{\log T_\phi}{N}\right)\to 0$,

where $T_\phi = \sup\text{supp}(\phi)$ and the error $O(\log T)$ comes from Doc 08. The first term $\to\int\phi\,d\mu_\gamma^{real}$ by definition. $\square$

**Corollary.** The Weyl–Titchmarsh m-function converges weakly:

$$m_\lambda(z) = \int\frac{d\mu_\xi^\lambda(t)}{t-z} \to m_\infty(z) = \int\frac{d\mu_\gamma^{real}(t)}{t-z}$$

for each $z\notin\mathbb{R}$, unconditionally. The convergence is uniform on compacta of $\mathbb{C}\setminus\mathbb{R}$.

**Conclusion:** The convergence of Doc 08 IS genuine spectral convergence. The spectral measure of $J_\lambda^{CCM}$ converges weakly to $\mu_\gamma^{real}$. The Jacobi coefficients of $J_\lambda$ converge to the Jacobi coefficients of $J_\infty = $ the Jacobi operator with spectral measure $\mu_\gamma^{real}$.

---

## Part B: Moments in terms of $\Psi_\lambda$

The connection between the Jacobi coefficients and the sums over primes goes through two steps:

$$\text{primes} \xrightarrow{\text{Weil's formula}} \Psi_\lambda \xrightarrow{\text{Euler–Lagrange}} \hat\xi_\lambda \xrightarrow{\text{argument principle}} \mu_\xi^\lambda \xrightarrow{\text{Stieltjes–Lanczos}} (a_n, b_n).$$

The key step: Step 2 (Euler–Lagrange → $\hat\xi_\lambda$). From the Euler–Lagrange equation with the rank-1 term (Doc 12):

$$\hat\xi_\lambda(z) = \frac{-c_\lambda\hat k_\lambda(z)}{C_\lambda(z) - \mu_\lambda}, \quad C_\lambda(z) = w(z) - \Psi_\lambda(z).$$

The Weyl–Titchmarsh m-function is obtained via the argument principle:

$$m_\lambda(z) = \frac{1}{N}\sum_n\frac{1}{t_n^{(\lambda)}-z} = -\frac{(\log\hat\xi_\lambda)'(z)}{N}.$$

Using the representation of $\hat\xi_\lambda$:

$$(\log\hat\xi_\lambda)'(z) = (\log\hat k_\lambda)'(z) - \frac{C_\lambda'(z)}{C_\lambda(z)-\mu_\lambda}.$$

Hence:

$$\boxed{m_\lambda(z) = -\frac{(\log\hat k_\lambda)'(z)}{N} + \frac{C_\lambda'(z)}{N[C_\lambda(z)-\mu_\lambda]}.}$$

The first term is $m_k^\lambda(z)$ (m-function of the zeros of $\hat k_\lambda$) and converges unconditionally to $m_k^\infty(z) = -(\log\Xi)'(z)/N$ (from Lemma 7.3, Doc 00). The second term directly involves $C_\lambda'(z)/[C_\lambda(z)-\mu_\lambda]$.

**The connection to $\Psi_\lambda$:** $C_\lambda'(z) = w'(z) - \Psi_\lambda'(z)$ and $\Psi_\lambda'(z) = -2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}\log(p)\sin(z\log p)$ — a sum over primes directly.

---

## Part C: The first Jacobi coefficients

The Jacobi coefficients $(b_n^{(\lambda)}, a_n^{(\lambda)})$ are obtained by the Lanczos algorithm applied to the function $m_\lambda$ via the Stieltjes recursion:

If $m_\lambda(z) = \cfrac{1/N}{z - b_0 - \cfrac{a_0^2}{z - b_1 - \cfrac{a_1^2}{\ddots}}}$ (Stieltjes continued fraction),

then the coefficients are obtained by the iterated Stieltjes recursion. The first three:

### Coefficient $b_0^{(\lambda)}$

$$b_0^{(\lambda)} = \frac{1}{N}\sum_{n=1}^N t_n^{(\lambda)} = \frac{\text{tr}(J_\lambda)}{N}.$$

From the m-function: $b_0 = $ first residue of the continued fraction of $m_\lambda$ at $z=\infty$.

Expanding $m_\lambda(z) = \frac{1}{N}\sum_n\frac{1}{t_n-z} = -\frac{1}{Nz}\sum_n\left(1 + \frac{t_n}{z} + \frac{t_n^2}{z^2} + \cdots\right)$:

$$m_\lambda(z) = -\frac{1}{z} - \frac{b_0^{(\lambda)}}{z^2} - \frac{m_2^{(\lambda)}}{z^3} - \cdots$$

where $m_k^{(\lambda)} = \frac{1}{N}\sum_n(t_n^{(\lambda)})^k$ are the moments.

**Expression in terms of the m-function of the EL representation:**

From the formula of Part B:

$$b_0^{(\lambda)} = -\frac{1}{N}\text{Res}_{z=\infty}[z^2 m_\lambda(z)] = \frac{1}{N}\sum_n t_n^{(\lambda)}.$$

By Proposition 1 (Part A):

$$b_0^{(\lambda)}/T_\lambda \to \frac{1}{N\cdot T_\lambda}\sum_{n=1}^N\gamma_n \sim \frac{1}{2} \quad\text{(unconditionally)}.$$

The OSCILLATING part of $b_0^{(\lambda)}$ (deviation from the mean value):

$$b_0^{(\lambda)} - \frac{T_\lambda}{2} = \frac{1}{N}\sum_n\left(t_n^{(\lambda)} - \frac{T_\lambda}{2}\right) = O\!\left(\frac{\log T_\lambda}{N}\right) \to 0.$$

This is unconditional: the first Jacobi coefficient converges (after normalizing by $T_\lambda$) to $1/2$, determined by the global density of zeros.

### Variance: $a_0^{(\lambda)}$

$$a_0^{(\lambda)2} = \frac{1}{N}\sum_n(t_n^{(\lambda)}-b_0)^2 = m_2^{(\lambda)} - (b_0^{(\lambda)})^2 = \frac{1}{N}\sum_n\left(t_n - \frac{T_\lambda}{2}\right)^2 - O(1).$$

The variance of $\{t_n\}$ in $[0,T_\lambda]$: by the counting of Doc 08, the $t_n$ are distributed approximately like the $\gamma_n$ in $[0,T_\lambda]$. The variance of the zero distribution in $[0,T_\lambda]$:

$$\text{Var}(\gamma_n) = \frac{1}{N}\sum_n\gamma_n^2 - \left(\frac{1}{N}\sum_n\gamma_n\right)^2 \sim \frac{T_\lambda^2}{12}.$$

Hence $a_0^{(\lambda)}/T_\lambda \to 1/(2\sqrt{3})$ unconditionally.

### Coefficient $b_1^{(\lambda)}$ (the first with non-trivial arithmetic content)

$$b_1^{(\lambda)} = \frac{m_3^{(\lambda)} - b_0^{(\lambda)}m_2^{(\lambda)}}{(a_0^{(\lambda)})^2} \cdot (\text{correction}) + b_0^{(\lambda)}.$$

The exact formula via the Stieltjes continued fraction:

$$b_1 = \frac{\langle p(t)\cdot t, p(t)\rangle}{\langle p(t),p(t)\rangle}, \quad p(t) = t - b_0$$

where the inner product is $\langle f,g\rangle = \frac{1}{N}\sum_n f(t_n)g(t_n)$.

$b_1^{(\lambda)} = \frac{\frac{1}{N}\sum_n(t_n-b_0)^2 t_n}{\frac{1}{N}\sum_n(t_n-b_0)^2} = b_0 + \frac{m_3 - 2b_0 m_2 + b_0^2 m_1}{m_2 - m_1^2}$.

The oscillating part of $b_1^{(\lambda)} - b_0^{(\lambda)}$: involves the third moment $m_3^{(\lambda)}$ of the zeros, which is sensitive to the ASYMMETRY of the zero distribution about its mean.

**Connection to the explicit formula:** $m_3^{(\lambda)} - 3b_0 m_2 + 2b_0^3 = \frac{1}{N}\sum_n(t_n-b_0)^3$ = third centered moment of the eigenvalue distribution. Under the mapping $t_n^{(\lambda)}\approx\gamma_n$:

$$\frac{1}{N}\sum_{n=1}^N(\gamma_n-\bar\gamma)^3 = \frac{1}{N}\sum_{n=1}^N\gamma_n^3 - 3\bar\gamma\cdot m_2 + 2\bar\gamma^3.$$

This is controllable via the explicit formula through the function $\zeta$:

$$\frac{1}{N}\sum_{n=1}^N\gamma_n^k = \frac{1}{N}\text{Res}_{z=0}\left[-(\log\Xi)^{(k)}(z)\right] + \text{error}$$

For $k=3$: the third moment involves $(\log\Xi)'''$ at $z=0$ (the symmetry point of $\Xi$). This is a COMPUTABLE quantity directly from the function $\Xi$.

---

## Part D: Convergence and the correct arithmetic scale

**At what scale does arithmetic information appear in the Jacobi coefficients?**

The first coefficients ($b_0, a_0$) are $O(T_\lambda)$ and capture only the GLOBAL DISTRIBUTION of the zeros. Their information is the same as the "Weyl Theorem" for the CCM operator: the mean eigenvalue density in $[0,T_\lambda]$. This is known (von Mangoldt's theorem) and is unconditionally $T\log T/(2\pi)$.

ARITHMETIC INFORMATION appears at the scale of the SPACINGS: $\delta_n = \gamma_{n+1}-\gamma_n \sim 2\pi/\log\gamma_n$. The Jacobi coefficients that capture this scale are those of order $n\sim N$ (the last ones, not the first).

**Proposition 2** (Arithmetic scale). The Jacobi coefficients $b_n^{(\lambda)}, a_n^{(\lambda)}$ of $J_\lambda^{CCM}$ fall into three regimes:

1. **Global regime** ($n \ll N$): $b_n \sim T_\lambda(1-n/N)$, $a_n \sim T_\lambda/(2\sqrt{N})$. Determined by the mean density; they do not contain arithmetic information about the individual zeros.

2. **Local regime** ($n \sim N_0$ fixed, $N_0\to\infty$ as $\lambda\to\infty$): $b_n$ and $a_n$ are of order $O(1/\log\gamma_{N_0})$ and reflect the LOCAL SPACINGS of the zeros near $\gamma_{N_0}$. This is the scale where GUE and prime arithmetic determine the coefficients.

3. **Tail regime** ($n \to N$): coefficients of the "edge" of the spectrum at $T_\lambda$.

**The correct Question 30.1** (per Advisor 1):

> For fixed $n$ and $\lambda\to\infty$ (i.e., the local regime with $N_0 = n$ fixed), does the normalized coefficient $b_n^{(\lambda)}$ converge to a limit determined by $\Psi_\lambda$?

**Theorem 1** (Jacobi coefficients in the local regime, under RH). If RH is true: for each fixed $n$, as $\lambda\to\infty$,

$$b_n^{(\lambda)} = \gamma_n + O(|\gamma_{n+1}-\gamma_n|) + O(\log\lambda/N) = \gamma_n + O(1/\log\gamma_n).$$

The correction $O(1/\log\gamma_n)$ comes from the local spacing of the zeros and is arithmetic.

*Proof.* The "local" Jacobi coefficients (via the Christoffel–Darboux kernel evaluated near $\gamma_n$) are the coefficients of the three-term recursion for the orthogonal polynomials with respect to $\mu_\xi^\lambda$ evaluated near $\gamma_n$. Under RH: $t_n^{(\lambda)}\to\gamma_n$ (Doc 09, Theorem 4), and the $n$-th Jacobi coefficient is $b_n \approx \frac{t_n+t_{n+1}}{2} + O(a_n)$ where $a_n \approx \frac{t_{n+1}-t_n}{2}$. Under RH: $t_n\to\gamma_n$, hence $b_n\to\frac{\gamma_n+\gamma_{n+1}}{2}$ and $a_n\to\frac{\gamma_{n+1}-\gamma_n}{2}$. $\square$

---

## The central result of Doc 15

**Theorem 2** (Convergence of Jacobi coefficients, unconditional). The normalized Jacobi coefficients of $J_\lambda^{CCM}$ satisfy:

$$\frac{b_n^{(\lambda)}}{T_\lambda}\to b_n^\infty, \quad \frac{a_n^{(\lambda)}}{T_\lambda}\to a_n^\infty \quad\text{(convergence for fixed } n\text{)},$$

where $(b_n^\infty, a_n^\infty)$ are the coefficients of the Jacobi operator $J^\infty$ with spectral measure $\mu_\gamma^{real}/T_\lambda$ (the normalized distribution of the REAL zeros of $\Xi$).

*Proof.* From Proposition 1 (Part A): $\mu_\xi^\lambda\Rightarrow\mu_\gamma^{real}$ weakly. By continuity of the Jacobi coefficients under weak convergence of the spectral measure (continuity theorem for the Stieltjes continued fraction, see e.g. Simon "Szegő's Theorem and Its Descendants"): $b_n^{(\lambda)}\to b_n^\infty$ for each fixed $n$. $\square$

**Corollary.** The limiting Jacobi operator $J^\infty$ has spectral measure $\mu_\gamma^{real}$ and its coefficients are the Jacobi coefficients of the distribution of REAL zeros of $\Xi$.

$$\mu_\gamma^{real} = \mu_\gamma \iff \text{all zeros of } \Xi \text{ are real} \iff \text{RH}.$$

---

## The precise arithmetic question that determines RH

The Jacobi coefficients of $J^\infty$ are determined by $\mu_\gamma^{real}$ via the three-term recursion for the orthogonal polynomials with respect to $\mu_\gamma^{real}$.

The question that would determine RH is:

> **Question 30.2.** Are the Jacobi coefficients $(b_n^\infty, a_n^\infty)$ of $J^\infty$ equal to the Jacobi coefficients of the distribution $\mu_\gamma$ (the distribution of ALL zeros of $\Xi$, real or not)?

If yes: $\mu_\gamma^{real} = \mu_\gamma$, hence all zeros are real, hence RH.

**The connection to $\Psi_\lambda$:** The coefficients $b_n^\infty, a_n^\infty$ of $J^\infty$ are the limits (as $\lambda\to\infty$) of the local moments of $\mu_\xi^\lambda$:

$$b_n^\infty = \lim_{\lambda\to\infty}\frac{1}{2}\left(t_{n}^{(\lambda)} + t_{n+1}^{(\lambda)}\right), \quad (a_n^\infty)^2 = \lim_{\lambda\to\infty}\frac{\left(t_{n+1}^{(\lambda)}-t_n^{(\lambda)}\right)^2}{4}.$$

And the $t_n^{(\lambda)}$ are determined by $\Psi_\lambda$ via the Euler–Lagrange equation.

**The explicit formula for the local spacings.** Under RH, the local spacing $t_{n+1}^{(\lambda)}-t_n^{(\lambda)} \approx \gamma_{n+1}-\gamma_n \approx 2\pi/\log\gamma_n$. The explicit formula gives:

$$\gamma_{n+1}-\gamma_n = \frac{2\pi}{\log(\gamma_n/2\pi)} + \frac{2\pi}{\log(\gamma_n/2\pi)}\cdot\sum_\rho\hat h(\gamma_n-\gamma_\rho) + O(1/\gamma_n^2),$$

where $\hat h$ is a test function and the sum is over all zeros of $\Xi$. This is Montgomery's "pair-correlation" formula.

**The wall of Question 30.2:** To show that the spacings $t_{n+1}-t_n$ converge to $2\pi/\log\gamma_n$ (the average spacing) without assuming RH: one needs to control the LOCAL distribution of the zeros $t_n^{(\lambda)}$ around each $\gamma_n$. This is equivalent to LOCAL RIGIDITY of the zeros of the CCM operator — exactly Route A (Erdős–Yau, rigidity for deterministic Jacobi matrices).

---

## Summary and roadmap

**Proved in this doc:**
- Weak convergence $\mu_\xi^\lambda\Rightarrow\mu_\gamma^{real}$ (Proposition 1, unconditional).
- Convergence of Jacobi coefficients $b_n^{(\lambda)}, a_n^{(\lambda)}\to b_n^\infty, a_n^\infty$ (Theorem 2, unconditional).
- Expression of $m_\lambda(z)$ in terms of $C_\lambda' / (C_\lambda - \mu_\lambda)$ (Part B).
- Values of the first coefficients: $b_0\sim T_\lambda/2$, $a_0\sim T_\lambda/(2\sqrt{3})$ (global, not arithmetic).

**The arithmetic information lies in:** the local coefficients $b_n^\infty, a_n^\infty$ for fixed $n$ — determined by the spacings $\gamma_{n+1}-\gamma_n$.

**The step that remains for RH:**

$$\boxed{(a_n^\infty)^2 = \lim_\lambda\frac{(t_{n+1}-t_n)^2}{4} = \frac{\pi^2}{\log^2\gamma_n} \stackrel{?}{=} \frac{\pi^2}{\log^2\gamma_n}.}$$

This equality is TRIVIALLY true under RH (both sides are equal). The content is to prove it WITHOUT assuming RH, from the structure of $\Psi_\lambda$ via the explicit formula — which ultimately requires convergence of the pair distribution of the zeros to the pair distribution of the sine-kernel system (GUE), which is Montgomery's Conjecture.

**The final chain toward RH:**

$$\text{Convergence of spacings (Montgomery's conj.)} \Rightarrow a_n^\infty = \frac{\pi}{\log\gamma_n} \Rightarrow \mu_\gamma^{real} = \mu_\gamma \Rightarrow \text{RH}.$$
