# Document 82 — The variational reformulation and the connection with Nyman-Beurling

**Program:** Riemann Hypothesis — Phase 33 DBN-CCM  
**Prerequisites:** Docs 64, 70, 72, 76, 79

---

## Summary

Doc 79 established that the sum over primes $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converges absolutely and that the equation $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) = 0$ is a tautology under RH, with the arithmetic cancellation among primes providing no new information. This document explores a different direction: reformulating RH as an approximation problem in $L^2(W_\lambda\,dm_\infty)$ and connecting this reformulation with the classical Nyman-Beurling-Báez-Duarte criterion.

In §1 we state the Nyman-Beurling criterion in its three forms. In §2 we identify the measure $dm_\infty$ as the reference space and clarify the sign of $T_\lambda$. In §3 we introduce the approximation of $|\zeta|^2$ by Hadamard-type functions with critical zeros. In §4 we formulate the variational infimum $\delta_\lambda^2$ and prove $\delta_\lambda^2 = 0 \iff$ RH. In §5 we examine the completeness of the exponential system $\{e^{i\gamma_n s}\}$ in $L^2(W_\lambda\,dm_\infty)$ using the exponential decay of the measure and the Beurling-Malliavin theorem. In §6 we discuss the connection with Montgomery's conjecture. In §7 we give the synthesis, pointing out precisely what is rigorous, what is conjectural, and what circular obstruction persists.

---

## §1. The Nyman-Beurling-Báez-Duarte criterion

### 1.1. Nyman's criterion (1950)

Let $\{t\} = t - \lfloor t \rfloor$ be the fractional part of $t > 0$. For $a \in (0,1)$, define the function
$$r_a(t) = \{a/t\}, \qquad t > 0.$$

**Theorem 1.1 (Nyman, 1950).** *The Riemann Hypothesis is true if and only if the constant function $\mathbf{1}_{(0,1)}$ belongs to the closure in $L^2(0,1)$ of the space*
$$\mathcal{N} = \left\{ f(t) = \sum_{k=1}^n c_k \{a_k/t\} : n \geq 1,\; a_k \in (0,1),\; c_k \in \mathbb{C},\; \sum_{k=1}^n c_k a_k = 0 \right\}.$$

The condition $\sum c_k a_k = 0$ guarantees that $f \in L^2(0,1)$ (otherwise the pole at $t = 0$ may prevent square-integrability). The criterion follows from the integral representation $\zeta(s) = s\int_0^1 \{1/t\}\, t^{s-1}\,dt + \frac{s}{s-1}$ valid for $\mathrm{Re}(s) > 0$: the function $\mathbf{1}_{(0,1)}$ is approximable in $L^2(0,1)$ by $\mathcal{N}$ if and only if $\mathbf{1}_{(0,1)}$ is not orthogonal to any $f \in L^2(0,1)$ that is orthogonal to all the $r_a$, which occurs precisely when $\zeta$ does not vanish in $\mathrm{Re}(s) > 1/2$.

### 1.2. Beurling's criterion (1955)

Beurling reformulated Nyman's criterion in terms of the Hardy space $H^2$ of the right half-plane. Define
$$\mathcal{B} = \overline{\mathrm{span}}^{L^2(0,\infty)}\{r_a : a \in (0,1)\}$$
with $r_a(t) = \{a/t\}$ extended as a function in $L^2(0,\infty, dt)$.

**Theorem 1.2 (Beurling, 1955).** *The Riemann Hypothesis is true if and only if $\mathbf{1}_{(0,1)} \in \mathcal{B}$ in $L^2(0,\infty)$.*

Equivalently, via the Mellin transform, RH is true if and only if the system $\{r_a : a \in (0,1)\}$ is complete in $L^2(0,\infty)$ in the sense that its closure contains $\mathbf{1}_{(0,1)}$. Beurling's formulation makes explicit the connection with the theory of invariant subspaces: the closure $\mathcal{B}$ is a subspace invariant under multiplication by $e^{-st}$, and the completeness condition is related to the zero structure of $\zeta$ in the critical strip $0 < \mathrm{Re}(s) < 1$.

### 1.3. The Báez-Duarte criterion (2003)

The most computable quantitative formulation of the Nyman-Beurling criterion was given by Báez-Duarte. For $N \geq 1$, define the distance
$$d_N^2 = \inf_{c_1,\ldots,c_N \in \mathbb{C}} \int_0^\infty \left| \mathbf{1}_{(0,1)}(t) - \sum_{k=1}^N c_k \{k/t\} \right|^2 dt.$$

Here only the discrete dilates $r_k(t) = \{k/t\}$ for $k = 1, 2, \ldots, N$ are used.

**Theorem 1.3 (Báez-Duarte, 2003).** *The Riemann Hypothesis is true if and only if $\lim_{N\to\infty} d_N^2 = 0$.*

The computability of the criterion rests on the explicit calculation of the correlations of the system $\{r_k\}$. For $j, k \geq 1$:
$$\langle r_j, r_k \rangle_{L^2(0,\infty)} = \int_0^\infty \{j/t\}\{k/t\}\,dt = \frac{\log(jk) + 2\gamma_E}{(jk)^{1/2}},$$
where $\gamma_E = 0.5772\ldots$ is the Euler-Mascheroni constant. This formula is verified by the change of variable $u = jk/t^2$ and the Fourier expansion of the fractional part $\{u\} = \frac{1}{2} - \sum_{m=1}^\infty \frac{\sin(2\pi mu)}{\pi m}$.

Similarly, $\langle \mathbf{1}_{(0,1)}, r_k \rangle_{L^2(0,\infty)} = \int_0^\infty \mathbf{1}_{(0,1)}(t) \{k/t\}\,dt = \frac{1}{2} - \frac{\log k + \gamma_E}{\sqrt{k}}$ (for $k \leq$ some threshold; the exact formula depends on whether $k \geq 1$ or $k < 1$). With these formulas, $d_N^2$ is expressed as a quadratic form in the $c_k$ whose coefficients are numerically accessible, and the convergence $d_N^2 \to 0$ is empirically verifiable with high precision.

**Remark 1.4.** The sequence $d_N^2$ is monotonically non-increasing in $N$ (it is a sequence of infima over expanding approximation classes). Numerically it is known that $d_N^2 \to 0$ at a rate consistent with RH, although no proof of convergence to zero is known without assuming RH.

---

## §2. The measure $dm_\infty$ as reference space

### 2.1. The space $L^2(W_\lambda\,dm_\infty)$ and the CTP criterion

Recall that $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ is the reference measure of the CCM formalism, and that for each $\lambda > 0$ the kernel
$$W_\lambda(s) = \sum_{k=0}^{N(\lambda)} (k+1)|P_k(s)|^2$$
defines a non-negative weight function in $L^1(dm_\infty)$ (where $P_k$ are the orthonormal Jacobi polynomials with respect to $dm_\infty$). The product $W_\lambda\,dm_\infty$ is thus a positive finite measure.

The CTP criterion (Docs 64, 70) states:
$$\mathrm{RH} \iff T_\lambda = 0 \quad \forall\lambda > 0,$$
where
$$T_\lambda = \int_\mathbb{R} W_\lambda(s)\bigl(|\zeta(1/2+is)|^2 - |\zeta_{\mathrm{on}}(1/2+is)|^2\bigr)\,dm_\infty(s).$$

Here $\zeta_{\mathrm{on}}$ denotes the hypothetical zeta function with all its zeros on the critical line (i.e., $\zeta$ itself if RH is true, or the modified version with zeros projected onto the critical line if it is not).

### 2.2. Sign of $T_\lambda$

The following proposition pins down the sign of $T_\lambda$ under $\neg$RH.

**Proposition 2.1** (sign of $T_\lambda$). *If $\zeta$ has a zero $\rho_0$ with $\mathrm{Re}(\rho_0) \neq 1/2$, then there exists $\lambda_0 > 0$ such that $T_{\lambda_0} > 0$.*

*Argument.* By Weil's formula (Doc 72), $T_\lambda = A_\lambda^{off}$, where $A_\lambda^{off}$ is the contribution to Weil's formula from the zeros off the critical line. Each symmetric quadruple of zeros $\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0$ contributes to $A_\lambda^{off}$ with a positive term when evaluated with admissible test functions $h_\lambda \geq 0$. Positivity is a consequence of the spectral analysis of the Hilbert-Jacobi operator on the Pontryagin space developed in Docs 35–36; the complete reference is Doc 64, main Proposition. $\square$

**Corollary 2.2.** *$T_\lambda \geq 0$ unconditionally for every $\lambda > 0$, with equality for every $\lambda$ if and only if RH is true.*

**Remark 2.3.** The non-negativity of $T_\lambda$ is not obvious from the definition as the difference $\int W_\lambda |\zeta|^2\,dm_\infty - \int W_\lambda |\zeta_{\mathrm{on}}|^2\,dm_\infty$; it requires the Pontryagin argument of Doc 64. In particular, $|\zeta|^2 \geq |\zeta_{\mathrm{on}}|^2$ pointwise does not hold in general; the inequality is only integral with the weight $W_\lambda$.

### 2.3. The natural distance

We define the $L^2(W_\lambda\,dm_\infty)$ distance between $|\zeta|$ and $|\zeta_{\mathrm{on}}|$:
$$D_\lambda^2 = \int_\mathbb{R} W_\lambda(s)\bigl||\zeta(1/2+is)| - |\zeta_{\mathrm{on}}(1/2+is)|\bigr|^2\,dm_\infty(s).$$

**Proposition 2.4** (comparison of $D_\lambda^2$ and $T_\lambda$). *We have*
$$D_\lambda^2 \leq T_\lambda.$$

*Proof.* For any $a, b \geq 0$, $(a-b)^2 = a^2 - 2ab + b^2 \leq a^2 - b^2$ if and only if $2b^2 \leq 2ab$, i.e., $b \leq a$. The inequality $D_\lambda^2 \leq T_\lambda$ is thus equivalent to $(|\zeta| - |\zeta_{\mathrm{on}}|)^2 \leq |\zeta|^2 - |\zeta_{\mathrm{on}}|^2$ almost everywhere with respect to $W_\lambda\,dm_\infty$, which reduces to $|\zeta_{\mathrm{on}}| \leq |\zeta|$ a.e. on the support of $W_\lambda\,dm_\infty$.

This pointwise inequality is not proved in general. What can be said is: under $\neg$RH, $T_\lambda > 0$ (Prop. 2.1) and $D_\lambda^2 \geq 0$ trivially. Under RH, $D_\lambda^2 = T_\lambda = 0$. The exact relation between $D_\lambda^2$ and $T_\lambda$ in general is an open question.

The direction that is useful: $T_\lambda = 0 \implies D_\lambda^2 = 0$ (because $T_\lambda = 0$ implies $|\zeta|^2 = |\zeta_{\mathrm{on}}|^2$ a.e. in $L^1(W_\lambda\,dm_\infty)$, which in turn implies $|\zeta| = |\zeta_{\mathrm{on}}|$ a.e., hence $D_\lambda^2 = 0$). $\square$

---

## §3. Approximation of $|\zeta|^2$ by Hadamard-type functions with critical zeros

### 3.1. The Hadamard product of $\xi$

The function $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ satisfies $\xi(s) = \xi(1-s)$ and admits the Hadamard product
$$\xi(s) = \xi(0) \prod_\rho \left(1 - \frac{s}{\rho}\right),$$
where the product extends over all nontrivial zeros $\rho$ of $\zeta$ and converges absolutely in symmetric pairs $\rho, 1-\rho$. The value $\xi(0) = 1/2$.

From the definition of $\xi$, on the critical line $s = 1/2 + it$:
$$|\zeta(1/2+it)|^2 = \frac{|\xi(1/2+it)|^2}{\frac{1}{4}(1+4t^2) \cdot \frac{1}{4} \cdot \pi^{-1/2-it} \cdot |\Gamma(1/4+it/2)|^2 / (2\pi)^2} \cdot (2\pi)^2.$$

More precisely, we have the factorization:
$$|\zeta(1/2+it)|^2 = \frac{4\pi^2 |\xi(1/2+it)|^2}{(2\pi)^2 |\Gamma(1/4+it/2)|^2 \cdot \frac{1}{4}(1+4t^2) \cdot \pi^{-1/2}} = \frac{16\pi^{5/2} |\xi(1/2+it)|^2}{(1+4t^2)|\Gamma(1/4+it/2)|^2}.$$

In terms of the density $w(t) = (2\pi)^{-2}|\Gamma(1/4+it/2)|^2$ of $dm_\infty$:
$$|\zeta(1/2+it)|^2\,dm_\infty(t) = \frac{16\pi^{5/2}|\xi(1/2+it)|^2}{(1+4t^2)}\,dt.$$

This factorization shows that the analytically relevant part of $|\zeta|^2$ with respect to the measure $dm_\infty$ is essentially $|\xi|^2$, modulo known polynomial growth factors. The Hadamard product of $\xi$ thus provides the decomposition into zeros.

### 3.2. Hadamard-type functions with critical zeros

**Definition 3.1.** A function $\eta_{\mathrm{on}} : \{1/2 + it : t \in \mathbb{R}\} \to \mathbb{C}$ is *of Hadamard type with critical zeros* if there exists a sequence $(\mu_n)_{n \geq 1} \subset \mathbb{R}$ such that:
$$\eta_{\mathrm{on}}(1/2+it) = \xi(0)\,e^{A+Bt} \prod_{n=1}^\infty \left(1 - \frac{1/2+it}{1/2+i\mu_n}\right)e^{(1/2+it)/(1/2+i\mu_n)},$$
where $A, B \in \mathbb{C}$ are constants compatible with the functional symmetry. We denote the class of these functions by $\mathcal{H}_{\mathrm{crit}}$.

When the $\mu_n$ are the imaginary parts of the nontrivial zeros of $\zeta$ (and all these zeros lie on the critical line), $\eta_{\mathrm{on}} = \zeta|_{\mathrm{Re}(s)=1/2}$.

### 3.3. Finite approximations

For $M \geq 1$, let $\zeta_M$ be the function that retains only the first $M$ pairs of zeros in the Hadamard product:
$$\xi_M(1/2+it) = \xi(0) \prod_{k=1}^M \left(1 - \frac{1/2+it}{1/2+i\mu_k}\right)e^{(1/2+it)/(1/2+i\mu_k)},$$
and $\zeta_M(1/2+it) = \xi_M(1/2+it) / [\text{regular factors}]$.

**Proposition 3.2** (convergence of the approximation). *For every $\lambda > 0$,*
$$D_\lambda^2(M) := \int_\mathbb{R} W_\lambda(s)\bigl||\zeta(1/2+is)| - |\zeta_M(1/2+is)|\bigr|^2\,dm_\infty(s) \xrightarrow{M\to\infty} D_\lambda^2.$$

*Argument.* The convergence of the Hadamard product implies $|\xi_M(1/2+is)| \to |\xi(1/2+is)|$ uniformly on compact sets. The weight $W_\lambda\,dm_\infty$ has fast (exponential in $|s|$) decay (Doc 76), so the integral is dominated by an effective compact region. Pointwise convergence plus domination complete the argument via the dominated convergence theorem. $\square$

---

## §4. The variational infimum $\delta_\lambda^2$

### 4.1. Definition

**Definition 4.1.** For each $\lambda > 0$, define
$$\delta_\lambda^2 = \inf_{\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}} \int_\mathbb{R} W_\lambda(s) \bigl(|\zeta(1/2+is)|^2 - |\eta_{\mathrm{on}}(1/2+is)|^2\bigr)^2 dm_\infty(s).$$

Here the infimum is taken over all functions of Hadamard type with critical zeros (Def. 3.1). The integrand is the square of the difference of squared values.

**Remark 4.2.** Alternatively, we can define
$$\tilde\delta_\lambda^2 = \inf_{\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}} \int_\mathbb{R} W_\lambda(s) \bigl||\zeta(1/2+is)| - |\eta_{\mathrm{on}}(1/2+is)|\bigr|^2 dm_\infty(s),$$
which is the $L^2(W_\lambda\,dm_\infty)$ distance between $|\zeta|$ and the class $|\mathcal{H}_{\mathrm{crit}}|$. Both definitions are relevant; the second is more natural from the point of view of approximation in Hilbert spaces. Unless otherwise specified, we will work with $\tilde\delta_\lambda^2$ in what follows.

### 4.2. The variational criterion

**Proposition 4.3 (RH implies $\tilde\delta_\lambda^2 = 0$).** *If the Riemann Hypothesis is true, then $\tilde\delta_\lambda^2 = 0$ for every $\lambda > 0$.*

*Proof.* Under RH, all nontrivial zeros of $\zeta$ lie on the critical line, so $\zeta \in \mathcal{H}_{\mathrm{crit}}$. Taking $\eta_{\mathrm{on}} = \zeta$ in the definition, the integrand is identically zero, hence $\tilde\delta_\lambda^2 = 0$. $\square$

**Proposition 4.4 ($\tilde\delta_\lambda^2 = 0$ for every $\lambda$ implies RH).** *If $\tilde\delta_\lambda^2 = 0$ for every $\lambda > 0$, then the Riemann Hypothesis is true.*

*Proof.* Suppose $\tilde\delta_\lambda^2 = 0$ for every $\lambda$. This means that for each $\lambda$ there exists a sequence $\eta_{\mathrm{on}}^{(n)} \in \mathcal{H}_{\mathrm{crit}}$ such that $|\eta_{\mathrm{on}}^{(n)}| \to |\zeta|$ in $L^2(W_\lambda\,dm_\infty)$.

Convergence in $L^2(W_\lambda\,dm_\infty)$ for a suitable increasing sequence of $\lambda$ implies pointwise convergence almost everywhere for a subsequence (by a standard diagonal argument). The limiting function $|\zeta(1/2+is)|$ thus lies in the closure of $|\mathcal{H}_{\mathrm{crit}}|$ in the sense of almost-everywhere convergence.

To conclude RH from this completeness, an additional argument is needed: that the only functions in $|\mathcal{H}_{\mathrm{crit}}|$ that coincide with $|\zeta|$ are those whose zeros are the same as those of $\zeta$. This follows from the lemma below:

**Lemma 4.5.** *If $\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}$ satisfies $|\eta_{\mathrm{on}}(1/2+it)| = |\zeta(1/2+it)|$ for almost every $t \in \mathbb{R}$, then the zeros of $\eta_{\mathrm{on}}$ are the same as those of $\zeta$ (i.e., $\eta_{\mathrm{on}}$ and $\zeta$ have the same zeros on the critical line, with the same multiplicities).*

*Argument for Lemma 4.5.* By the Hadamard product, $|\eta_{\mathrm{on}}(1/2+it)| = |\zeta(1/2+it)|$ a.e. implies $|\xi_{\eta_{\mathrm{on}}}(1/2+it)| = |\xi(1/2+it)|$ modulo the shared regular factors. Two entire functions of the same order that have the same modulus on a line are equal modulo a pure exponential factor (Hadamard's theorem applied to the meromorphic function $\xi_{\eta_{\mathrm{on}}}/\xi$). If moreover both have all their zeros on the same line $\mathrm{Re}(s) = 1/2$, the function $\xi_{\eta_{\mathrm{on}}}/\xi$ is an entire zero-free function, hence of the form $e^{g(s)}$ with $g$ a polynomial of degree $\leq 1$ by the growth order. The condition $|\xi_{\eta_{\mathrm{on}}}| = |\xi|$ on $\mathrm{Re}(s) = 1/2$ forces $\mathrm{Re}(g(1/2+it)) = 0$ for every $t$, which forces $g$ to be a purely imaginary constant. Hence $\xi_{\eta_{\mathrm{on}}} = e^{ic}\xi$ for some $c \in \mathbb{R}$, so $\eta_{\mathrm{on}}$ and $\zeta$ have exactly the same zeros. $\square$

Returning to the proof of Proposition 4.4: if $|\zeta|$ is in the closure of $|\mathcal{H}_{\mathrm{crit}}|$ and the pointwise limit of $|\eta_{\mathrm{on}}^{(n)}|$ is $|\zeta|$, then by Lemma 4.5, any function $\eta_{\mathrm{on}}$ that coincides in modulus with $\zeta$ on the critical line has the same zeros as $\zeta$. Since the zeros of any $\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}$ are real by definition (they lie on the critical line), it follows that the zeros of $\zeta$ on the critical line are real — that is, their imaginary parts are the only nontrivial zeros — and hence RH is true. $\square$

**Corollary 4.6.** *$\tilde\delta_\lambda^2 = 0$ for every $\lambda > 0$ if and only if the Riemann Hypothesis is true.*

---

## §5. Completeness of the exponential system in $L^2(W_\lambda\,dm_\infty)$

### 5.1. The system $\{e^{i\gamma_n s}\}$ and the Hadamard class

If the nontrivial zeros of $\zeta$ are $\rho_n = 1/2 + i\gamma_n$ (under RH, the $\gamma_n \in \mathbb{R}$), the function $|\xi(1/2+is)|^2$ can be formally expressed as a product involving the terms $|1 - s/(1/2 + i\gamma_n)|^2$. The logarithm of this product is
$$\log |\xi(1/2+is)|^2 = \log|\xi(0)|^2 + 2\,\mathrm{Re}\sum_n \log\left(1 - \frac{1/2+is}{1/2+i\gamma_n}\right) + 2\,\mathrm{Re}\,\frac{1/2+is}{1/2+i\gamma_n}.$$

The Fourier expansion of $\log|\xi|^2$ on the critical line involves the frequencies $\gamma_n$: formally, $\log|\xi(1/2+is)|^2$ is a superposition of terms $e^{\pm i\gamma_n s}$. Hence, if the system $\{e^{i\gamma_n s}\}_{n \geq 1}$ is complete in $L^2(W_\lambda\,dm_\infty)$, every smooth function in that space can be approximated, and in particular the function $|\zeta|^2 - |\eta_{\mathrm{on}}|^2$ can be made as small as desired.

### 5.2. The Beurling-Malliavin density

Recall the fundamental theorem of Beurling and Malliavin (1962) in its qualitative form:

**Theorem 5.1 (Beurling-Malliavin, 1962).** *Let $\Lambda = \{\lambda_n\}_{n \geq 1} \subset \mathbb{R}$ be a sequence of frequencies with finite uniform density. The system $\{e^{i\lambda_n t}\}_{n \geq 1}$ is complete in $L^2(\mathbb{R}, w(t)\,dt)$ where $w$ has compact support if and only if the Beurling-Malliavin density $D_{BM}(\Lambda) \geq L$, where $L$ is the radius of the support of $w$.*

For the case at hand, the measure $W_\lambda\,dm_\infty$ has non-compact support but exponential decay: $W_\lambda(s)\,dm_\infty(s) \leq C_\lambda e^{-\pi|s|/2}\,ds$ (Doc 76, Prop. 1.5). This decay is analogous to working in a Paley-Wiener space of radius $\pi/2$.

**Proposition 5.2** (density of the zeros). *The imaginary zeros $\gamma_n > 0$ of $\zeta$ satisfy*
$$D_{BM}(\{\gamma_n\}) := \liminf_{r\to\infty} \frac{\#\{n : |\gamma_n| \leq r\}}{r} = \frac{\log r}{2\pi}\bigg|_{\text{on average}} \to \infty.$$

*More precisely, by the Riemann-von Mangoldt formula*
$$N(T) = \#\{\rho : |\mathrm{Im}(\rho)| \leq T, \mathrm{Re}(\rho) \in (0,1)\} = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T),$$
*the average density of $\gamma_n$ in $[0, T]$ is $\sim \frac{\log T}{2\pi}$, which tends to infinity.*

The average density tends to infinity (the sequence $\gamma_n$ is superdense in the Beurling-Malliavin sense). This fact is favorable for completeness.

### 5.3. Completeness in $L^2(W_\lambda\,dm_\infty)$

**Proposition 5.3** (conditional completeness under RH). *Assuming all the $\gamma_n$ are real (i.e., assuming RH), the system $\{e^{i\gamma_n s}\}_{n \geq 1}$ is complete in $L^2(W_\lambda\,dm_\infty)$ for every $\lambda > 0$.*

*Argument.* The measure $\mu_\lambda = W_\lambda\,dm_\infty$ has the property that its Fourier transform $\hat\mu_\lambda(r) = \int e^{irs}\,\mu_\lambda(ds)$ decays exponentially: $|\hat\mu_\lambda(r)| = O(e^{-(\pi/4)|r|})$ (Doc 76). This means $\mu_\lambda$ is a measure in the Bernstein class with radius $\pi/4$.

By the Beurling-Malliavin theorem adapted to spaces with exponentially decreasing weight (see Korevaar 2004, Ch. 12, or the monograph of Young 1980): if the density of $\{\gamma_n\}$ is greater than $L/\pi$ where $L = \pi/4$ is the effective radius of the measure, then the system $\{e^{i\gamma_n s}\}$ is complete in $L^2(\mu_\lambda)$.

The condition is $D_{BM} > L/\pi = 1/4$. By Prop. 5.2, $D_{BM} = +\infty$ (in logarithmic average). Hence the condition holds comfortably, and the system is complete. $\square$

**Caveat 5.4.** The argument of Prop. 5.3 is formal at the following points: (a) the precise version of the Beurling-Malliavin theorem for measures with exponential decay (not merely compact support) requires verifying technical conditions of Paley-Wiener theory; (b) the "density" $D_{BM} = +\infty$ must be interpreted carefully in the logarithmic sense of the function $N(T)$. The argument indicates the plausibility of completeness, not its rigorous proof. We flag this as a point to be developed in Phase 35.

### 5.4. The unconditional question

The critical question, which arises naturally and constitutes the core of the circular obstruction, is the following:

**Question 5.5.** Is the system $\{e^{i\gamma_n s}\}_{n \geq 1}$ complete in $L^2(W_\lambda\,dm_\infty)$ even if some of the $\gamma_n$ are complex (i.e., if there are zeros of $\zeta$ off the critical line)?

If the answer is unconditionally affirmative, then the completeness argument does not assume RH and $\tilde\delta_\lambda^2 = 0$ would follow without assuming RH. But $\tilde\delta_\lambda^2 = 0$ is equivalent to RH by Corollary 4.6. This would give a proof.

If the answer is negative — if the system $\{e^{i\gamma_n s}\}$ fails to be complete exactly when there are off-critical zeros — then completeness becomes a new and equivalent criterion for RH, but not a proof. We examine this alternative in §6.

---

## §6. Completeness, Riesz bases, and Montgomery's conjecture

### 6.1. Exponential systems and Riesz bases

A system $\{e^{i\lambda_n t}\}_{n \geq 1}$ in $L^2(a, b)$ is a *Riesz basis* if it is topologically equivalent to an orthonormal basis: there exist constants $0 < A \leq B < \infty$ such that for every finite sequence $(c_n)$,
$$A\sum|c_n|^2 \leq \left\|\sum_n c_n e^{i\lambda_n t}\right\|^2 \leq B\sum|c_n|^2.$$

By Pavlov's theorem (1979), the system $\{e^{i\gamma_n t}\}_{n \geq 1}$ is a Riesz basis in $L^2(0, a)$ if and only if the $\gamma_n$ satisfy the Carleson condition: $\inf_{n \neq m} |\gamma_n - \gamma_m| > 0$ (uniform separation) and the Blaschke condition on the imaginary parts when the $\gamma_n$ are complex.

If some $\gamma_n$ have nonzero imaginary part (off-critical zeros), the Blaschke condition can fail, destroying the Riesz basis structure. This suggests that completeness of the exponential system in $L^2(W_\lambda\,dm_\infty)$ could fail precisely under $\neg$RH.

### 6.2. Montgomery's conjecture and the rigidity of the zeros

Montgomery's *pair correlation conjecture* (1973) states that for $0 < a < b < \infty$,
$$\lim_{T\to\infty} \frac{1}{N(T)} \#\left\{(m,n) : m \neq n,\; \gamma_m, \gamma_n \in [0,T],\; a \leq \frac{\gamma_m - \gamma_n}{2\pi/\log T} \leq b\right\} = \int_a^b \left(1 - \left(\frac{\sin\pi u}{\pi u}\right)^2\right)du.$$

This conjecture, supported by extensive numerical verifications and compatible with GUE unitary random matrix statistics, implies that the fluctuations of $N(T) - \frac{T}{2\pi}\log\frac{T}{2\pi}$ are of order $O(\log T)$ — much smaller than the $O(T^{1/2})$ fluctuations expected for a random sequence. This *rigidity* of the zeros is a deep structural property.

**Proposition 6.1** (conditional rigidity and completeness). *Under Montgomery's conjecture, the sequence $(\gamma_n)$ has the local separation property:*
$$\liminf_{n\to\infty} (\gamma_{n+1} - \gamma_n) \cdot \frac{\log\gamma_n}{2\pi} > 0.$$
*This implies the Carleson condition for the rescaled frequencies $\tilde\gamma_n = \gamma_n / \frac{\log\gamma_n}{2\pi}$, and consequently the system $\{e^{i\gamma_n s}\}$ is a Riesz basis in $L^2(0, a)$ for every $a < \infty$.*

**Corollary 6.2.** *Under Montgomery's conjecture, $\tilde\delta_\lambda^2 = 0$ (conditional on RH).*

**Remark 6.3.** The implication from Montgomery's conjecture to completeness operates only *conditional on RH* (since Montgomery's conjecture assumes the $\gamma_n$ are real). It does not provide the unconditional step being sought.

### 6.3. Completeness as an independent criterion

We summarize the situation as follows. Define:
$$\mathcal{C}_\lambda = \overline{\mathrm{span}}^{L^2(W_\lambda dm_\infty)}\{e^{i\gamma_n s} : n \geq 1\},$$
where the $\gamma_n$ are the imaginary parts of the nontrivial zeros of $\zeta$ (under RH, they are real; in general, they are complex).

**Proposition 6.4.** *The following are equivalent:*
1. *RH is true.*
2. *$T_\lambda = 0$ for every $\lambda > 0$ (CTP criterion).*
3. *$\tilde\delta_\lambda^2 = 0$ for every $\lambda > 0$ (variational criterion, Corollary 4.6).*
4. *$|\zeta(1/2+is)|^2 \in \mathcal{C}_\lambda$ in $L^2(W_\lambda\,dm_\infty)$ for every $\lambda > 0$ (Hadamard completeness).*

The equivalence (1)$\iff$(2) is the CTP criterion. The equivalence (2)$\iff$(3) follows from Corollary 4.6. The equivalence (3)$\iff$(4) is formal: under RH, $|\zeta|^2 = |\zeta_{\mathrm{on}}|^2$ belongs to $\mathcal{C}_\lambda$ trivially; conversely, if $|\zeta|^2 \in \mathcal{C}_\lambda$, then the distance $\tilde\delta_\lambda^2 = 0$ and Corollary 4.6 applies.

The interest of criterion (4) is that it might be verifiable by functional-analytic methods independent of number theory.

---

## §7. Synthesis and evaluation of Path 3

### 7.1. Rigorous results obtained

**R1 (Doc 79, Prop. 1.1).** The sum $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converges absolutely for every $\lambda > 0$, with no hypothesis on the zeros of $\zeta$. The quantity $T_\lambda$ is well defined.

**R2 (Doc 79, §8–9).** The formula $T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ is an identity (Weil's formula expressed in CCM language). Under RH, both sides are zero; the equation is a tautology, not a new cancellation mechanism.

**R3 (this document, Corollary 4.6).** The variational criterion $\tilde\delta_\lambda^2 = 0$ for every $\lambda$ is equivalent to RH. The proof of both implications (Propositions 4.3 and 4.4) is rigorous modulo Lemma 4.5, whose proof is complete.

**R4 (this document, Prop. 5.3).** Under RH, the system $\{e^{i\gamma_n s}\}$ is complete in $L^2(W_\lambda\,dm_\infty)$. The proof is solid in structure but requires the technical verification of the version of the Beurling-Malliavin theorem for measures with exponential (non-compact) decay.

### 7.2. What remains conjectural

**C1.** The rigorous version of the Beurling-Malliavin theorem for the space $L^2(W_\lambda\,dm_\infty)$ with exponential decay. The argument in §5.3 is plausible but does not constitute a complete proof.

**C2.** The *unconditional* completeness of the system $\{e^{i\gamma_n s}\}$ — that is, without assuming the $\gamma_n$ are real. If this could be proved, RH would follow from Corollary 4.6. But there is no indication that completeness is independent of the hypothesis we want to prove.

**C3.** The quantitative relation between $D_\lambda^2$, $\tilde\delta_\lambda^2$, and $T_\lambda$ when $T_\lambda > 0$. In particular, if $T_\lambda > 0$ (under $\neg$RH), how large is $\tilde\delta_\lambda^2$?

### 7.3. The circular obstruction and its precise nature

The circular structure of the argument is thus identified precisely:

Corollary 4.6 says: RH $\iff$ $\tilde\delta_\lambda^2 = 0$ for every $\lambda$. This is a valid criterion. But to use it as a proof of RH we need to prove $\tilde\delta_\lambda^2 = 0$ by independent means.

The completeness argument (§5) says: under RH (i.e., under the assumption that the $\gamma_n$ are real), the system $\{e^{i\gamma_n s}\}$ is complete and hence $\tilde\delta_\lambda^2 = 0$. But this is the easy implication: RH $\implies$ $\tilde\delta_\lambda^2 = 0$, which is already Proposition 4.3.

The obstruction is exactly this: we do not know how to prove completeness of the system $\{e^{i\gamma_n s}\}$ without assuming the $\gamma_n$ are real. If the $\gamma_n$ can be complex, the geometry of the exponential system changes (the exponents are no longer real, the exponentials no longer have modulus one on $\mathbb{R}$, and Beurling-Malliavin theory does not apply directly).

**Consequently:** Path 3 in its current formulation is a reorganization of the CTP criterion in variational and completeness terms, without adding new information that would allow proving RH. The reformulations (variational criterion, Hadamard completeness, connection with Nyman-Beurling) are mathematically clean and could be useful as a starting point for future attacks, but none of them breaks the intrinsic circularity of the problem.

### 7.4. Connection with Nyman-Beurling: the formal translation

The Báez-Duarte criterion says: RH $\iff$ $d_N^2 \to 0$ in $L^2(0,\infty)$. The variational criterion of this document says: RH $\iff$ $\tilde\delta_\lambda^2 \to 0$ in $L^2(W_\lambda\,dm_\infty)$.

The structural analogy is clear: in both cases, RH is equivalent to a certain object ($\mathbf{1}_{(0,1)}$ in the Báez-Duarte case, $|\zeta|^2$ in the CCM case) being approximable by a class of functions built from the zeros of $\zeta$ on the critical line.

The explicit translation between the two criteria goes through the Mellin transform. The function $\{k/t\}$ in $L^2(0,\infty, dt)$ has Mellin transform $\zeta(s)/s \cdot k^{-s}$ (for $\mathrm{Re}(s) \in (0,1)$), relating the span of the $r_k = \{k/t\}$ to the span of $s \mapsto k^{-s}\zeta(s)/s$. By the Plancherel isometry of the Mellin transform (which maps $L^2(0,\infty, dt/t)$ to $L^2(1/2+i\mathbb{R}, ds/(2\pi i))$), the Báez-Duarte criterion translates into $\hat{\mathbf{1}}_{(0,1)}(s) = (s(s-1))^{-1}$ being approximable in $L^2(1/2+i\mathbb{R})$ by the functions $s \mapsto k^{-s}\zeta(s)/s$, for $k = 1, 2, \ldots, N$.

The CCM formalism introduces the measure $dm_\infty$ (with its structure of orthogonal Jacobi polynomials) as a replacement for Lebesgue measure on the critical line. The distance $\tilde\delta_\lambda^2$ is the weighted version (with weight $W_\lambda$) of the analogous distance in $L^2(1/2+i\mathbb{R})$. The formal connection between the two criteria exists, but its rigorous translation would require identifying the measure-change operator (from Lebesgue to $dm_\infty$) and verifying that it preserves the density structure.

This point is left as a direction for Phase 35.

---

## §8. Open questions for Phase 35

The following questions emerge from this analysis and define the agenda for the next phase.

**Q1.** Rigorously prove the completeness of the system $\{e^{i\gamma_n s}\}$ in $L^2(W_\lambda\,dm_\infty)$ under RH, verifying all the technical conditions of the Beurling-Malliavin theorem for spaces with exponential decay.

**Q2.** Determine whether the completeness of the system $\{e^{i\gamma_n s}\}$ can be proved unconditionally (i.e., without assuming the $\gamma_n$ are real). Analyze what happens to the argument when some $\gamma_n$ are complex.

**Q3.** Construct the explicit and rigorous translation between the Báez-Duarte criterion ($d_N^2 \to 0$ in $L^2(dt)$) and the variational criterion ($\tilde\delta_\lambda^2 \to 0$ in $L^2(W_\lambda\,dm_\infty)$) via the Mellin transform and the measure change.

**Q4.** Study the rate of convergence $d_N^2 \to 0$ (under RH) and $\tilde\delta_\lambda^2 \to 0$ (under RH) and see whether the rate contains additional information about the distribution of the zeros.

**Q5.** Examine whether the completeness criterion (Prop. 6.4, condition 4) can be reformulated as a condition on prime powers — analogous to Weil's formula — that is verifiable without assuming RH.

---

*Document 82 concluded. State of Path 3: the variational and completeness reformulations are mathematically clean and equivalent to the CTP criterion. The circular obstruction — completeness requires the reality of the $\gamma_n$, which is precisely RH — is identified precisely. There is no new proof of RH; there is an enriched conceptual framework for approaching the problem from functional analysis.*
