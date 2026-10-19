# Doc 90 — Direction A: External arithmetic information via the explicit formula

**Program:** Riemann Hypothesis — Phase 34 (new directions)
**Prerequisites:** Docs 70, 71, 72, 83, 89

---

## Summary

The arithmetic formula $T_\lambda = A_\lambda^{\mathrm{off}} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ (Doc 72) expresses the CCM trace in purely arithmetic terms. Under $\neg$RH, Path I of the program (Doc 70) imposes the lower bound $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j) > 0$. Direction A asks whether the distribution of prime numbers, via the Weil-Guinand formula, can impose an upper bound on the prime sum $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ that contradicts that lower bound, thereby forcing $\neg$RH to be false. This document analyzes that possibility rigorously and concludes that, although the conceptual framework is correct and the tension is real, the argument does not close with the tools currently available. The obstacles are identified precisely and the lemmas that would be sufficient to close the direction are formulated.

---

## §1. The Direction A scenario

### 1.1. The two quantities in tension

The program's framework produces two expressions for the same quantity $T_\lambda$:

**From the zeros (Path I):** under the hypothesis $\neg$RH — that is, assuming there exist zeros $\rho_j = (1/2 + \delta_j) + i\gamma_j$ with $\delta_j > 0$ — the formula of Doc 70 gives
$$T_\lambda \geq 2\sum_j \delta_j^2 \, K_\lambda(\gamma_j),$$
where $K_\lambda(\gamma) = \int W_\lambda(s)(s - \gamma)^{-2}\, dm_{full,on}(s) > 0$ is an explicit positive quantity.

**From arithmetic (Doc 72):** Weil's explicit formula applied to $W_\lambda$ expresses
$$T_\lambda = A_\lambda^{\mathrm{off}} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) + R_\lambda^{\mathrm{arch}},$$
where $A_\lambda^{\mathrm{off}}$ depends on the off-critical zeros, $B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\, dm_\infty(s)$, and $R_\lambda^{\mathrm{arch}}$ is an archimedean term.

Direction A proposes exploiting this duality. If under $\neg$RH the left-hand side is large (positive lower bound), then the right-hand side must also be large. Can the prime sum be that large? Or is there a bound on the prime sum that leads to a contradiction?

### 1.2. Why the direction is conceptually natural

The Weil-Guinand explicit formula is the most precise known instance of the prime-zero duality. It is natural to try to use the regularity of the primes (which is considerable: the Prime Number Theorem, the zero-free region, etc.) to restrict what the prime sum can do. If the distribution of primes were "too regular" for $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ to grow as much as the lower bound requires under $\neg$RH, there would be a contradiction.

### 1.3. The Hadamard barrier and why the direction is not trivially circular

Doc 89 established the Hadamard barrier: no verifiable property of $\zeta$ that does not depend on knowing the position of the zeros can imply $d\nu = 0$. Apparently Direction A falls under this barrier. However, there is a structural difference: Direction A does not attempt to verify that $T_\lambda = 0$ directly, but to obtain an **arithmetic contradiction** under $\neg$RH. The question is not "can arithmetic prove that $d\nu = 0$?" but "can arithmetic prove that $d\nu > 0$ is impossible at the same time that the prime sum satisfies its known properties?". This is a subtle point that will be analyzed in §7.

---

## §2. The Weil-Guinand formula: precise form

### 2.1. The Guinand-Weil formula

Let $h: \mathbb{C} \to \mathbb{C}$ be a test function satisfying the following conditions (admissibility conditions):

**(W1)** $h$ is even: $h(-s) = h(s)$.

**(W2)** $h$ is holomorphic in the strip $\{s \in \mathbb{C} : |\mathrm{Im}(s)| < 1/2 + \varepsilon\}$ for some $\varepsilon > 0$.

**(W3)** $h$ satisfies the bound $|h(s)| \leq C(1 + |s|)^{-2-\varepsilon}$ in that strip.

We denote by $\hat{h}(r) = \int_{-\infty}^\infty h(s) e^{irs} ds$ the Fourier transform of $h$ (defined for real $r$).

**Theorem 2.1 (Guinand-Weil explicit formula).** *Under conditions (W1)–(W3):*
$$\sum_\rho h(\gamma_\rho) = 2h(i/2) + \hat{h}(0)\log\frac{1}{2\pi} - \int_{-\infty}^\infty h(s)\frac{\Gamma'}{\Gamma}\!\left(\frac{1}{4} + \frac{is}{2}\right)\frac{ds}{4\pi} - 2\sum_p \sum_{m=1}^\infty \frac{\log p}{p^{m/2}}\,\hat{h}(m\log p),$$
*where the sum on the left-hand side runs over all non-trivial zeros $\rho = 1/2 + i\gamma_\rho$ of $\zeta$ (with multiplicity, counting $\gamma$ and $-\gamma$ separately if $\rho$ and $\bar{\rho}$ are distinct zeros).*

**Frank note on Theorem 2.1:** The formula is classical (Guinand 1948, Weil 1952). The form stated here is the standard version that appears, for example, in Iwaniec-Kowalski, Analytic Number Theory, ch. 5. RH is not assumed in the statement; the sum on the left-hand side runs over all non-trivial zeros with their real imaginary parts (under RH all the $\gamma_\rho$ are real; without RH the sum must be understood as $\sum_\rho h(\mathrm{Im}(\rho))$, where convergence is guaranteed under (W3) by the density of zeros $N(T) = (T/2\pi)\log(T/2\pi e) + O(\log T)$).

### 2.2. The archimedean term

The term involving $\Gamma'/\Gamma$ can also be written as
$$\int_{-\infty}^\infty h(s)\,\frac{\Gamma'}{\Gamma}\!\left(\frac{1}{4} + \frac{is}{2}\right)\frac{ds}{4\pi} = \int_{-\infty}^\infty h(s)\left(\log\frac{1}{4\pi} + \mathrm{Re}\,\psi\!\left(\frac{1}{4}+\frac{is}{2}\right)\right)\frac{ds}{2\pi},$$
where $\psi = \Gamma'/\Gamma$ is the digamma function. We define the **full archimedean term**
$$\mathcal{A}[h] := 2h(i/2) + \hat{h}(0)\log\frac{1}{2\pi} - \int_{-\infty}^\infty h(s)\,\frac{\Gamma'}{\Gamma}\!\left(\frac{1}{4}+\frac{is}{2}\right)\frac{ds}{4\pi},$$
so that the Weil-Guinand formula takes the compact form
$$\sum_\rho h(\gamma_\rho) = \mathcal{A}[h] - 2\sum_p\sum_{m=1}^\infty \frac{\log p}{p^{m/2}}\,\hat{h}(m\log p).$$

### 2.3. The CCM framework's test function $h_\lambda$

To connect with the trace $T_\lambda$ we need to choose $h$ so that the sum over zeros $\sum_\rho h(\gamma_\rho)$ relates to $T_\lambda$. The natural function of the CCM framework is
$$h_\lambda(s) := W_\lambda(s)\,\frac{dm_\infty}{ds}(s) = W_\lambda(s)\,(2\pi)^{-2}|\Gamma(1/4+is/2)|^2.$$

**Lemma 2.2.** *The function $h_\lambda$ satisfies conditions (W1)–(W3) if $W_\lambda$ is a polynomial of fixed degree in $s^2$ (the case $N(\lambda) < \infty$) or a finite combination of $|P_k(s)|^2$. In particular, for any fixed $\lambda > 0$, $h_\lambda$ is admissible.*

**Proof.** $W_\lambda$ is a finite sum $\sum_{k \leq N(\lambda)} k|P_k(s)|^2 + \ldots$ where $|P_k(s)|^2$ is a polynomial of degree $2k$ in $s$. The evenness of $h_\lambda$ follows from the evenness of $W_\lambda$ and from $|\Gamma(1/4+is/2)|^2 = |\Gamma(1/4-is/2)|^2$ (using reflection). Holomorphy in the strip $|\mathrm{Im}(s)| < 1/2 + \varepsilon$ follows from that of $\Gamma$, which has no poles in that strip (the first pole of $\Gamma(1/4+is/2)$ occurs at $1/4 + is/2 = 0$, i.e., $s = -i/2$; the first pole of $\Gamma(1/4+is/2)$ in the strip $|\mathrm{Im}(s)| < 1/2 + \varepsilon$ requires $|\mathrm{Im}(s)|$ close to $1/2$, outside the closed strip if $\varepsilon < 1/4$). The decay bound follows from the exponential decay of $|\Gamma(1/4+is/2)|^2 \sim 2^{3/2}\pi|s|^{-1/2}e^{-\pi|s|/2}$ for $|s| \to \infty$ on the real line, which compensates for any polynomial growth of $W_\lambda$. $\square$

---

## §3. The term $A_\lambda^{\mathrm{off}}$ and its structure

### 3.1. Precise definition

The term $A_\lambda^{\mathrm{off}}$ of the formula $T_\lambda = A_\lambda^{\mathrm{off}} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) + R_\lambda^{\mathrm{arch}}$ comes from the contribution of the off-critical zeros to the difference $d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$.

**Definition 3.1.** For off-critical zeros $\rho_j = (1/2+\delta_j)+i\gamma_j$ with $\delta_j > 0$ (and their symmetric conjugates), we define
$$A_\lambda^{\mathrm{off}} := \int W_\lambda(s)\, d\nu(s) - \text{(normalization corrections)}.$$
More precisely, from Proposition 3.1 of Doc 83:
$$d\nu(s) = (R(s)-1)\,dm_{\mathrm{full,on}}(s), \qquad R(s) = \prod_j \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2\prod_j\left(1+\frac{\delta_j^2}{(s+\gamma_j)^2}\right)^2,$$
and
$$A_\lambda^{\mathrm{off}} = \int W_\lambda(s)(R(s)-1)\,dm_{\mathrm{full,on}}(s) = T_\lambda.$$

**Remark 3.2.** The identity $A_\lambda^{\mathrm{off}} = T_\lambda$ is not circular: it says that the "off-critical" term in the Weil formula coincides with the trace $T_\lambda$ when the formula is expanded on the zero side. The full Weil formula imposes the relation
$$A_\lambda^{\mathrm{off}} = \mathcal{A}[h_\lambda] - 2\sum_p\sum_{m\geq 1}\frac{\log p}{p^{m/2}}\hat{h}_\lambda(m\log p) - \sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}}),$$
where the sum $\sum_{\rho_{\mathrm{on}}}$ runs over the zeros on the critical line. It is the difference between the zeros of $\zeta$ and those of $\zeta_{\mathrm{on}}$ that produces $A_\lambda^{\mathrm{off}}$.

### 3.2. Expression via the kernel $K_\lambda$

To first order in $\delta_j$, expanding $R(s) - 1 \approx \sum_j 4\delta_j^2 [(s-\gamma_j)^{-2} + (s+\gamma_j)^{-2}]$:

**Lemma 3.3** (First-order expression of $A_\lambda^{\mathrm{off}}$).
$$A_\lambda^{\mathrm{off}} = 4\sum_j \delta_j^2 \left[K_\lambda(\gamma_j) + K_\lambda(-\gamma_j)\right] + O\!\left(\sum_j \delta_j^4\right),$$
where
$$K_\lambda(\gamma) := \int \frac{W_\lambda(s)}{(s-\gamma)^2}\, dm_{\mathrm{full,on}}(s).$$

**Proof.** Insert $R(s) - 1 = \sum_j 4\delta_j^2[(s-\gamma_j)^{-2}+(s+\gamma_j)^{-2}] + O(\delta_j^4)$ into $A_\lambda^{\mathrm{off}} = \int W_\lambda\,(R-1)\,dm_{\mathrm{full,on}}$. The exchange of sum and integral is legitimate by the absolute convergence of the Hadamard product (Doc 83) for bounded $W_\lambda$. $\square$

**Note:** Doc 70 uses the bound $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j)$; the different factor ($4$ vs. $2$) comes from counting the pair $(\gamma_j, -\gamma_j)$ of zeros. If $\gamma_j > 0$, both $\gamma_j$ and $-\gamma_j$ contribute, and $K_\lambda(\gamma_j) \approx K_\lambda(-\gamma_j)$ by symmetry of $dm_{\mathrm{full,on}}$, giving $4\delta_j^2 K_\lambda(\gamma_j)$; the bound of Doc 70 is then $T_\lambda \geq 4\sum_j \delta_j^2 K_\lambda(\gamma_j)$ (or $2\sum_j \delta_j^2 K_\lambda(\gamma_j)$ if the sum already counts pairs). The difference is a convention in counting zeros and does not affect the argument.

### 3.3. The archimedean term $R_\lambda^{\mathrm{arch}}$

The term $R_\lambda^{\mathrm{arch}}$ in the formula of Doc 72 is the term $\mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}})$: the part of the Weil formula involving $\Gamma$ and the zeros on the critical line (which are present both under RH and under $\neg$RH). Under RH this part cancels exactly with the prime sum (making $T_\lambda = 0$); under $\neg$RH, the difference is exactly $A_\lambda^{\mathrm{off}} > 0$.

For the purposes of Direction A, we can rewrite the arithmetic formula as
$$T_\lambda = A_\lambda^{\mathrm{off}} = \mathcal{A}[h_\lambda] - \sum_{\rho:\, \gamma_\rho \in \mathbb{R}} h_\lambda(\gamma_\rho) - 2\sum_p\sum_{m\geq 1}\frac{\log p}{p^{m/2}}\hat{h}_\lambda(m\log p),$$
where $\sum_{\rho:\, \gamma_\rho \in \mathbb{R}}$ is the sum over the zeros on the critical line and the right-hand side is the Weil formula applied to the off-critical zeros.

---

## §4. The prime sum $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$

### 4.1. Definition and basic properties

**Definition 4.1.** For fixed $\lambda > 0$, we define
$$\mathcal{P}_\lambda := \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p), \qquad B_\lambda(r) := \int W_\lambda(s)\cos(rs)\, dm_\infty(s).$$

The function $B_\lambda: \mathbb{R}^+ \to \mathbb{R}$ is the Fourier-cosine transform of the kernel $W_\lambda$ with respect to the measure $dm_\infty$.

**Lemma 4.2** (Properties of $B_\lambda$). *For all $\lambda > 0$:*

*(i) $B_\lambda(r)$ is real and even in $r$.*

*(ii) $B_\lambda(0) = \int W_\lambda(s)\, dm_\infty(s)$, which is finite and positive.*

*(iii) $|B_\lambda(r)| \leq B_\lambda(0)$ for all $r$.*

*(iv) As $r \to \infty$: $B_\lambda(r) = O(e^{-\pi r/4})$, with exponential decay coming from the decay of $dm_\infty = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 ds \sim e^{-\pi|s|/2}$.*

**Proof.** Points (i)–(iii) are elementary. For (iv): $|B_\lambda(r)| \leq \int W_\lambda(s)|\cos(rs)|\,dm_\infty(s) \leq \int W_\lambda(s)\,dm_\infty(s) = B_\lambda(0)$, but the decay does not come from this bound. The exponential decay of $B_\lambda(r)$ for large $r$ is a consequence of the Paley-Wiener theorem applied to the function $f(s) = W_\lambda(s)|\Gamma(1/4+is/2)|^2$: since $|\Gamma(1/4+is/2)|^2$ decays as $e^{-\pi|s|/2}$ on the real line, $f \in L^1(\mathbb{R})$ with good decay properties, and its Fourier transform decays exponentially. $\square$

**Corollary 4.3.** The series $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converges absolutely for every $\lambda > 0$. In fact, by (iv):
$$|\mathcal{P}_\lambda| \leq B_\lambda(0) \sum_p \frac{\log p}{\sqrt{p}} e^{-\pi\log p/4} = B_\lambda(0)\sum_p \frac{\log p}{\sqrt{p}\cdot p^{\pi/4}} = B_\lambda(0)\sum_p \frac{\log p}{p^{1/2+\pi/4}},$$
and the series $\sum_p \frac{\log p}{p^{1/2+\pi/4}}$ converges absolutely since $1/2 + \pi/4 > 1$ (because $\pi/4 > 1/2$).

### 4.2. Interpretation of $\mathcal{P}_\lambda$ as a von Mangoldt sum

The series $\mathcal{P}_\lambda$ is a smoothed version of the weighted Chebyshev sum. Let us compare it with the von Mangoldt function:
$$\psi(x) = \sum_{p^m \leq x} \log p = \sum_p \log p \cdot \lfloor \log x / \log p\rfloor.$$

The difference is that only $m=1$ appears in $\mathcal{P}_\lambda$ (the first term $\hat{h}_\lambda(\log p)$ with $m=1$) with weight $p^{-1/2}$, while the Weil formula sums over all $m \geq 1$. Let us separate the (dominant) term $m=1$ from the (subdominant) terms $m \geq 2$.

**Lemma 4.4** (Separation of prime powers).
$$2\sum_p\sum_{m\geq 1}\frac{\log p}{p^{m/2}}\hat{h}_\lambda(m\log p) = 2\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) + 2\sum_p\sum_{m\geq 2}\frac{\log p}{p^{m/2}} B_\lambda(m\log p).$$

The second term is $O\!\left(\sum_p \frac{\log p}{p}\right) = O(\log x)$ for primes $p \leq x$, and the full series over all primes converges to a constant:
$$\sum_p\sum_{m\geq 2}\frac{\log p}{p^{m/2}} B_\lambda(m\log p) \leq B_\lambda(0)\sum_p\sum_{m\geq 2}\frac{\log p}{p^{m/2}} e^{-m\pi\log p/4} \leq B_\lambda(0)\sum_p\frac{\log p}{p - p^{\pi/4}} < \infty.$$

**Definition 4.5.** We define the **main prime sum** as
$$\mathcal{P}_\lambda^{(1)} := 2\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$$
and the **higher-power residue** as $\mathcal{P}_\lambda^{(\geq 2)} := 2\sum_p\sum_{m\geq 2}\frac{\log p}{p^{m/2}}B_\lambda(m\log p)$. Both series converge absolutely.

### 4.3. Asymptotic behavior in $\lambda$

As $\lambda \to \infty$, $N(\lambda) \to \infty$ and $W_\lambda(s)$ grows (it incorporates more terms of the Jacobi basis). The behavior of $B_\lambda(r)$ under this limit is crucial.

**Proposition 4.6** (Growth of $B_\lambda$). *For fixed $r > 0$:*
$$B_\lambda(r) = \int W_\lambda(s)\cos(rs)\,dm_\infty(s) \to \sum_{k=0}^\infty k \int |P_k(s)|^2\cos(rs)\,dm_\infty(s) \quad (\lambda \to \infty),$$
*if the series on the right-hand side converges. This convergence is not guaranteed in general; it depends on the decay of the Fourier coefficients of $|P_k|^2 dm_\infty$.*

**Frank note on 4.6:** It is not known whether the series $\sum_k k \widehat{|P_k|^2 dm_\infty}(r)$ converges for the orthogonal polynomials $P_k$ of $L^2(dm_{\mathrm{full,on}})$. This point is a technical (not fundamental) obstacle for the asymptotic analysis in $\lambda$.

---

## §5. The lower bound under $\neg$RH

### 5.1. Path I of Doc 70

Under $\neg$RH, suppose there exist zeros $\rho_j = (1/2+\delta_j)+i\gamma_j$ with $\delta_j > 0$, $j \in J$ (possibly infinite set). From the definition and positivity of $d\nu$:

**Proposition 5.1** (Path I lower bound). *Under $\neg$RH:*
$$T_\lambda \geq 4\sum_{j \in J} \delta_j^2 \left[\frac{1}{2}K_\lambda(\gamma_j) + \frac{1}{2}K_\lambda(-\gamma_j)\right] \geq 4\delta_0^2 K_\lambda(\gamma_0),$$
*where $\rho_0 = (1/2+\delta_0)+i\gamma_0$ is any chosen off-critical zero, and*
$$K_\lambda(\gamma) := \int \frac{W_\lambda(s)}{(s-\gamma)^2}\,dm_{\mathrm{full,on}}(s) > 0.$$

**Proof.** From $d\nu = (R-1)dm_{\mathrm{full,on}} \geq 0$ and $R - 1 \geq 4\delta_j^2(s-\gamma_j)^{-2}$ (taking only term $j$ of the product), we integrate against $W_\lambda \geq 0$. $\square$

### 5.2. Behavior of $K_\lambda(\gamma)$ in $\lambda$

To understand the tension with the prime sum, we need to understand how $K_\lambda(\gamma)$ grows in $\lambda$.

**Lemma 5.2** (Growth of $K_\lambda(\gamma)$). *For fixed $\gamma \in \mathbb{R}$:*
$$K_\lambda(\gamma) = \int \frac{W_\lambda(s)}{(s-\gamma)^2}\,dm_{\mathrm{full,on}}(s)$$
*is increasing in $\lambda$ (since $W_\lambda$ grows with $\lambda$ term by term). More precisely, $K_\lambda(\gamma) \to K_\infty(\gamma) = \int (s-\gamma)^{-2}\,dm_{\mathrm{full,on}}(s)$, which is finite if $dm_{\mathrm{full,on}}$ has no mass at $\gamma$ (which is true if $\zeta_{\mathrm{on}}(1/2+i\gamma) \neq 0$, a condition satisfied except for finitely many $\gamma$ under general conditions on the zeros).*

**Proof.** $W_\lambda = \sum_{k \leq N(\lambda)} k|P_k|^2 + \ldots$ is increasing in $\lambda$ term by term. The integral $K_\lambda(\gamma) = \sum_{k \leq N(\lambda)} k \int |P_k(s)|^2(s-\gamma)^{-2} dm_{\mathrm{full,on}}(s)$ grows with $\lambda$. Convergence $K_\lambda \to K_\infty$ follows from the Monotone Convergence Theorem if all the summands are positive, which requires $(s-\gamma)^{-2}$ to be integrable with respect to $|P_k|^2 dm_{\mathrm{full,on}}$; this holds if $\gamma$ is not an atom of $dm_{\mathrm{full,on}}$. $\square$

**Corollary 5.3.** *Under $\neg$RH, for any off-critical zero $\rho_0$, $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0)$ and this lower bound grows with $\lambda$.*

### 5.3. The asymmetry in growth rates

The lower bound under $\neg$RH grows as $K_\lambda(\gamma_0) \sim \lambda^\alpha$ for some exponent $\alpha > 0$ depending on the Jacobi basis. The prime sum $\mathcal{P}_\lambda$ also grows with $\lambda$ (as $B_\lambda(\log p)$ grows by incorporating more Jacobi terms). The question is whether the growth rates are comparable or whether there is an exploitable asymmetry.

**Remark 5.4** (On the asymmetry). The lower bound involves $(s-\gamma_0)^{-2}$, which has a singularity at $s = \gamma_0$. This singularity makes $K_\lambda(\gamma_0)$ grow rapidly with $\lambda$ if the Jacobi polynomials have spectral mass concentrated near $\gamma_0$. In contrast, $B_\lambda(\log p) = \int W_\lambda\cos(s\log p)\,dm_\infty$ involves the Fourier transform of $W_\lambda dm_\infty$: this functional is oscillatory and may have cancellations. The question is whether these cancellations are sufficient.

---

## §6. Bounds on the prime sum: what can be proved

### 6.1. The Prime Number Theorem and its implication

The PNT says that $\psi(x) = \sum_{p^m \leq x} \log p \sim x$. In terms of the Chebyshev sum:
$$\sum_p \log p \cdot \mathbf{1}_{p \leq x} = \psi(x) + O(x^{1/2+\varepsilon}) = x + O(x^{1/2+\varepsilon}),$$
where the error is conditional on the best known zero-free region. The PNT implies the convergence of the Dirichlet series $\sum_p \frac{\log p}{p^s}$ for $\mathrm{Re}(s) > 1$ and its behavior at $s = 1$ (logarithmic pole).

For our sum $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$, the PNT gives:

**Proposition 6.1** (PNT bound). *For every fixed $\lambda > 0$:*
$$\left|\mathcal{P}_\lambda\right| \leq 2B_\lambda(0)\sum_p \frac{\log p}{\sqrt{p}\,p^{\pi/4-1/2}} = 2B_\lambda(0)\sum_p \frac{\log p}{p^{\pi/4}} < \infty.$$

This is only an absolute-convergence bound, not a non-trivial upper bound. The PNT per se gives no information about the sign or the precise magnitude of $\mathcal{P}_\lambda$.

### 6.2. The zero-free region and the Vinogradov estimate

The best known zero-free region has the form $\sigma > 1 - c(\log t)^{-2/3}(\log\log t)^{-1/3}$ for $t \geq t_0$ (Vinogradov 1958, Korobov 1958). This implies an estimate for the error in the PNT:
$$\psi(x) = x + O\!\left(x\exp\!\left(-c(\log x)^{3/5}(\log\log x)^{-1/5}\right)\right).$$

For the sum $\mathcal{P}_\lambda$ with fixed test functions (dependent on $\lambda$), the zero-free region only gives information about the zeros of $\zeta$ itself. It says nothing about possible off-critical zeros $\rho_j$.

**Remark 6.2** (Limitation of the zero-free region). The known zero-free region excludes zeros in a region of the form $\sigma > 1 - f(t)$ for some function $f(t) \to 0$, but **does not exclude** zeros with $\sigma \leq 1 - f(\gamma)$. In particular, it does not exclude off-critical zeros in the strip $1/2 < \sigma \leq 1 - f(\gamma)$, which includes the whole critical strip for $\gamma$ sufficiently large. The hypothetical zeros $\rho_j$ under $\neg$RH could be at $\sigma_j = 1/2 + \delta_j$ with $\delta_j$ arbitrarily small.

### 6.3. Lindelöf-type bounds and zero density

The **zero density theorem** (Ingham 1940 and refinements) states that for $1/2 < \sigma < 1$:
$$N(\sigma, T) = \#\{\rho : \mathrm{Re}(\rho) \geq \sigma,\; |\mathrm{Im}(\rho)| \leq T\} \ll T^{A(1-\sigma)}\log^B T$$
for explicit constants $A, B$. This limits how many zeros can exist off the critical line at height $T$. The best known bound (Huxley 1972) gives $A = 12/5$.

Under $\neg$RH, there could be $N(\sigma, T) \gg 1$ off-critical zeros. Each one contributes $4\delta_j^2 K_\lambda(\gamma_j)$ to the lower bound of $T_\lambda$. If these zeros are "dense" (in the sense of $N(\sigma, T) \sim T^{A(1-\sigma)}$), the lower bound grows rapidly with the height of the zeros.

**Proposition 6.3** (Accumulated lower bound under maximum density). *Suppose that under $\neg$RH there exist zeros $\rho_j$ with $\delta_j \geq \delta_0 > 0$ and $\gamma_j \in [T, 2T]$, with $N(\sigma_0, T) \gtrsim T^{c}$ for some $c > 0$ and $\sigma_0 = 1/2+\delta_0$. Then:*
$$T_\lambda \geq 4\delta_0^2 \sum_{j:\, \gamma_j \in [T,2T]} K_\lambda(\gamma_j).$$

*If in addition $K_\lambda(\gamma_j) \geq K_{\min}(\lambda, T) > 0$ uniformly in $j$, then*
$$T_\lambda \geq 4\delta_0^2 K_{\min}(\lambda, T) \cdot T^c.$$

**Frank note:** This proposition is valid but unusable directly: under $\neg$RH we do not know how the zeros are distributed (that is why $\neg$RH remains open). It is a conditional proposition.

### 6.4. Can $\mathcal{P}_\lambda$ grow that fast?

The prime sum $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ is a series that depends on $\lambda$ only through $B_\lambda$. For large $\lambda$, $B_\lambda(\log p) \to B_\infty(\log p) = \int W_\infty(s)\cos(s\log p)\,dm_\infty(s)$ (if the limit exists). The limiting sum would be
$$\mathcal{P}_\infty = \sum_p \frac{\log p}{\sqrt{p}} B_\infty(\log p),$$
which is a series over all primes with weights $\frac{\log p}{\sqrt{p}} B_\infty(\log p)$.

The natural upper bound on $|\mathcal{P}_\lambda|$ is the one given by Proposition 6.1, which does not grow with $\lambda$ faster than $B_\lambda(0)$. But $B_\lambda(0) = \int W_\lambda\,dm_\infty$, which grows without bound with $\lambda$ (since $W_\lambda \to \infty$ pointwise). Hence there is no uniform-in-$\lambda$ upper bound on $\mathcal{P}_\lambda$.

**Conclusion 6.4** (Limitation of Direction A so far). *No non-trivial upper bound on $\mathcal{P}_\lambda$ is known — neither from the PNT, nor from the zero-free region, nor from the density theorems — that is comparable to the lower bound $4\delta_0^2 K_\lambda(\gamma_0)$ under $\neg$RH. Both quantities grow with $\lambda$, and the relation between their growth rates is the key to the problem.*

---

## §7. The tension between the lower bound and the prime sum

### 7.1. Reformulation of the tension

From the arithmetic formula for the trace (Doc 72, Thm. 4.1):
$$T_\lambda = \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}}) - 2\sum_p\sum_{m\geq 1}\frac{\log p}{p^{m/2}}\hat{h}_\lambda(m\log p),$$
where the right-hand side involves **only** the zeros on the critical line (not the off-critical ones) and the prime sum.

Under $\neg$RH, the left-hand side satisfies $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0) > 0$. So the identity says:
$$4\delta_0^2 K_\lambda(\gamma_0) \leq \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}}) - 2\mathcal{P}_\lambda^{(1)} - 2\mathcal{P}_\lambda^{(\geq 2)}.$$

**Definition 7.1.** We call the **archimedean-spectral residue**:
$$\mathcal{R}_\lambda := \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}}).$$

This term is computable, in principle, from knowledge of the zeros of $\zeta$ on the critical line and the function $\Gamma$. It is the "already known part" of the problem.

The tension takes the form: under $\neg$RH,
$$4\delta_0^2 K_\lambda(\gamma_0) \leq \mathcal{R}_\lambda - 2\mathcal{P}_\lambda,$$
which means that $\mathcal{P}_\lambda$ must satisfy
$$\mathcal{P}_\lambda \leq \frac{\mathcal{R}_\lambda}{2} - 2\delta_0^2 K_\lambda(\gamma_0).$$

For this to imply a contradiction, we would need to know that $\mathcal{P}_\lambda$ cannot be that small (or negative) when $K_\lambda(\gamma_0)$ is large. This is what Direction A seeks.

### 7.2. The obstacle: sign of $\mathcal{P}_\lambda$

The sum $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ has terms of variable sign:

- For small $p$ with $B_\lambda(\log p)$ positive: positive contribution.
- For large $p$ (with large $\log p$): $B_\lambda(\log p)$ can be negative due to cosine oscillations.

In particular, $B_\lambda(r) = \int W_\lambda(s)\cos(rs)\,dm_\infty(s)$ is negative for $r$ such that the function $W_\lambda dm_\infty$ has more mass where $\cos(rs) < 0$ than where $\cos(rs) > 0$.

**Remark 7.2.** If $\mathcal{P}_\lambda$ could be arbitrarily negative, the inequality $\mathcal{P}_\lambda \leq \mathcal{R}_\lambda/2 - 2\delta_0^2 K_\lambda(\gamma_0)$ would be trivially satisfied (always compatible) and there would be no contradiction. For a contradiction, we need a **lower bound** on $\mathcal{P}_\lambda$.

**Proposition 7.3** (Trivial lower bound on $\mathcal{P}_\lambda$).
$$\mathcal{P}_\lambda \geq -2B_\lambda(0)\sum_p \frac{\log p}{\sqrt{p}\,p^{\pi/4-1/2}}.$$
This bound is finite but does not give the non-trivial lower bound that is needed.

### 7.3. The cancellation structure in the Weil formula

A crucial point: the Weil formula under RH gives $T_\lambda = 0$, which means the prime sum and the archimedean term cancel exactly. Under $\neg$RH, this cancellation is imperfect: there is an excess of $T_\lambda > 0$.

**Question 7.4** (The central question of Direction A). *Is there a non-trivial lower bound on $\mathcal{P}_\lambda$ that shows $\mathcal{P}_\lambda$ cannot be small enough to accommodate $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0)$ simultaneously with the Weil formula?*

The negative answer to the direct attempt: the prime sum $\mathcal{P}_\lambda$ can, in principle, be any value in $[-B_\lambda(0)C_\lambda, B_\lambda(0)C_\lambda]$ (where $C_\lambda = \sum_p \frac{\log p}{\sqrt{p}p^{\pi/4}}$). The distribution of primes does not appear to impose restrictions on the value of $\mathcal{P}_\lambda$ with sufficient precision.

---

## §8. Candidates to close the argument

### 8.1. Candidate 1: Positivity of $B_\lambda(\log p)$ for small primes

If it could be proved that $B_\lambda(\log p) > 0$ for all primes $p$ (or at least for the small primes that dominate the sum), then $\mathcal{P}_\lambda > 0$, and the inequality under $\neg$RH would say
$$4\delta_0^2 K_\lambda(\gamma_0) \leq \mathcal{R}_\lambda - 2\mathcal{P}_\lambda < \mathcal{R}_\lambda.$$

This would mean that $K_\lambda(\gamma_0)$ is bounded by $\mathcal{R}_\lambda/(4\delta_0^2)$, independent of the prime sum. But this does not close the argument: $\mathcal{R}_\lambda$ also grows with $\lambda$, and the inequality would give no contradiction.

**Note:** Even if $B_\lambda(\log p) > 0$ (positivity), the consequence would be $\mathcal{P}_\lambda > 0$, not a lower bound growing as fast as $K_\lambda(\gamma_0)$.

### 8.2. Candidate 2: Relation between $\mathcal{P}_\lambda$ and $K_\lambda(\gamma_0)$ via the Weil formula

If under $\neg$RH the Weil formula directly connected $\mathcal{P}_\lambda$ with $K_\lambda(\gamma_0)$, there could be tension. The connection would be: the prime sum "feels" the off-critical zeros because the Weil formula relates primes to all zeros. Formally, if the test function $h_\lambda$ has significant correlation with the frequency $\gamma_0$ of the off-critical zeros, then the prime sum would reflect that zero.

This is precisely what the Weil formula does: **the zeros of $\zeta$ (including off-critical ones) are encoded in the distribution of primes**. If there were an off-critical zero at $\gamma_0$, the distribution of primes would have an irregularity at scale $\gamma_0$. This irregularity could be detected in $B_\lambda(\log p)$ if the test function $h_\lambda$ is sensitive to that frequency.

**Lemma 8.1** (The Weil formula encodes off-critical zeros in the primes). *If $\rho_0 = (1/2+\delta_0)+i\gamma_0$ is a zero of $\zeta$ with $\delta_0 > 0$, then the distribution of primes satisfies, for any admissible test function $h$:*
$$\sum_p \frac{\log p}{\sqrt{p}}\hat{h}(\log p) = \frac{\mathcal{A}[h] - \sum_{\rho}h(\gamma_\rho)}{2},$$
*where the sum $\sum_\rho h(\gamma_\rho)$ includes the off-critical zero $\rho_0$.*

**Proof.** This is the Weil-Guinand formula (Theorem 2.1) rewritten. $\square$

Lemma 8.1 does not help directly: it says that if there is an off-critical zero, the prime sum changes value (relative to the case without that zero), but it does not say whether that change makes the sum larger or smaller.

### 8.3. Candidate 3: Analysis of the optimal test function

The most promising argument would be to choose $h_\lambda$ so as to maximize the tension: to make $h_\lambda$ large at the off-critical zeros (maximizing the lower bound) and small where the prime sum can compensate. This is an optimization problem in the space of admissible test functions.

**Problem 8.2** (Optimization of the test function). *Does there exist an admissible test function $h^*$ such that:*
$$\sum_\rho h^*(\gamma_\rho^{\mathrm{off}}) > \mathcal{A}[h^*] - 2\mathcal{P}^* - \sum_{\rho_{\mathrm{on}}} h^*(\gamma_j^{\mathrm{on}})$$
*is impossible for every pair (distribution of off-critical zeros, distribution of primes) compatible with the known properties of $\zeta$?*

This is the heart of the Weil method for RH (explored by Bombieri 2000 and others). The known answer is: **no**, no such $h^*$ has been found, and there are technical reasons to believe that the Weil method alone cannot prove RH (reason: the only information used is that of the Weil formula, which is a reformulation of RH, not an independent proof).

---

## §9. The precise obstacle: exact formulation

### 9.1. What would be needed to close the argument

We summarize the gap that Direction A cannot fill:

**Statement of the obstacle 9.1.** *For Direction A to close the RH argument via the explicit formula, it would be necessary to prove (at least) one of the following statements:*

**(O1)** *There exists a function $\Phi_\lambda: \mathbb{R}_{>0} \to \mathbb{R}$ such that $\mathcal{P}_\lambda \geq \Phi_\lambda$ and $\mathcal{R}_\lambda - 2\Phi_\lambda < 4\delta_0^2 K_\lambda(\gamma_0)$ for $\lambda$ sufficiently large.*

**(O2)** *The sum $\mathcal{P}_\lambda$ grows with $\lambda$ at a rate $f(\lambda)$, while $K_\lambda(\gamma_0)$ grows at a rate $g(\lambda)$ with $g(\lambda)/f(\lambda) \to \infty$, so that the lower bound eventually exceeds any upper bound.*

**(O3)** *The hypothetical off-critical zeros $\rho_j$ impose, via the Weil formula, explicit bounds on $\mathcal{P}_\lambda$ that contradict the known analytic properties of $\zeta$ (the functional equation, the zero-free region).*

**Proposition 9.2** (Current status of the obstacles).

*(a) O1 is unknown. No non-trivial lower bound on $\mathcal{P}_\lambda$ is known that comes only from the distribution of primes.*

*(b) O2 is unknown. The relation between the growth rate of $B_\lambda(\log p)$ and that of $K_\lambda(\gamma_0)$ in $\lambda$ has not been analyzed.*

*(c) O3 is the formulation closest to known attempts (the Weil method, the Beurling method, the Bateman-Chowla function). All these methods have run into the same barrier: the Weil formula is a tautology with respect to the position of the zeros, and cannot be used to prove anything new about that position.*

### 9.2. The missing lemma

**Definition 9.3** (Lemma $\mathcal{L}_A$). Let $\mathcal{L}_A$ be the following statement:

> *For every admissible test function $h$ with $h(\gamma_0) > 0$ for some real $\gamma_0$, and for every sequence of primes $\{p_k\}$, the sum $\sum_p \frac{\log p}{\sqrt{p}}\hat{h}(\log p)$ is bounded below by a quantity that grows faster than $(h(\gamma_0))^{-1}$ when $h$ is concentrated at $\gamma_0$.*

This statement, if true, would give a lower bound on $\mathcal{P}_\lambda$ when $h_\lambda$ is concentrated at the off-critical zeros. But $\mathcal{L}_A$ is false in general: for functions $h$ concentrated at $\gamma_0$, the sum $\sum_p \frac{\log p}{\sqrt{p}} \hat{h}(\log p)$ can be small (the primes do not "see" a hypothetical zero at $\gamma_0$ except through the Weil formula).

**Proposition 9.4** (Falsity of $\mathcal{L}_A$ in general). *Let $h_\varepsilon(s) = \varepsilon^{-1}\phi((s-\gamma_0)/\varepsilon)$ where $\phi$ is an admissible test function concentrated at $0$. Then:*

*(i) $h_\varepsilon(\gamma_0) = \varepsilon^{-1}\phi(0) \to \infty$ as $\varepsilon \to 0^+$.*

*(ii) $\hat{h}_\varepsilon(\log p) = \phi(\varepsilon \log p) e^{i\gamma_0 \log p} \to \hat{\phi}(0) e^{i\gamma_0 \log p}$ as $\varepsilon \to 0^+$.*

*(iii) $\sum_p \frac{\log p}{\sqrt{p}}\hat{h}_\varepsilon(\log p) \to \hat{\phi}(0)\sum_p \frac{\log p}{\sqrt{p}} e^{i\gamma_0 \log p}$, which is a series that can be bounded or even small depending on the distribution of primes.*

*In particular, the prime sum does not grow like $h_\varepsilon(\gamma_0)^c$ for any $c > 0$, which falsifies $\mathcal{L}_A$. $\square$*

### 9.3. The Hadamard barrier revisited

Doc 89 established that no verifiable property of $\zeta$ that does not depend on knowing zero positions implies $d\nu = 0$. How does this relate to Direction A?

**Proposition 9.5** (Direction A falls under the Hadamard barrier). *The strategy of Direction A — proving that $\mathcal{P}_\lambda$ cannot satisfy the lower bound under $\neg$RH — is equivalent to proving $T_\lambda = 0$ without knowing the positions of the off-critical zeros. This is exactly what the Hadamard barrier (Doc 89) forbids.*

**Proof.** The identity $T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ expresses $T_\lambda$ in terms of $\mathcal{R}_\lambda$ (which depends on the zeros on the critical line) and $\mathcal{P}_\lambda$ (which depends on the distribution of primes). Proving that $T_\lambda = 0$ using only the distribution of primes and the critical zeros is exactly the kind of argument that the Hadamard barrier forbids: the Weil formula is a reformulation of RH, not a proof.

More precisely: $\mathcal{P}_\lambda$ is determined by the zeros of $\zeta$ via the Weil formula (that is, $\mathcal{P}_\lambda = (\mathcal{R}_\lambda - T_\lambda)/2$). Hence any information about $\mathcal{P}_\lambda$ that is used already implicitly contains information about $T_\lambda$. The argument is circular. $\square$

**Corollary 9.6.** *Direction A, in its current formulation, is blocked by the Hadamard barrier. To overcome this blockage, arithmetic information about the primes is needed that is **independent** of the position of the zeros of $\zeta$ — that is, information that exists unconditionally without assuming any hypothesis about the zeros.*

---

## §10. Analysis of possible openings

### 10.1. Genuinely independent arithmetic information

The only arithmetic information about primes that is genuinely independent of the position of the zeros of $\zeta$ is that which can be obtained without using the Weil formula. The canonical examples are:

1. **Bounds for Ramanujan-Weil sums:** the sum $\sum_{p \leq x} e^{i\gamma\log p}$ for fixed $\gamma$; these can be bounded by elementary sieve methods.

2. **Vinogradov's theorem on the sum of three primes:** proves that every sufficiently large odd integer is the sum of three primes. This gives information about the distribution of primes but in an additive, not multiplicative, sense.

3. **Brun-Titchmarsh bounds on primes in arithmetic progressions:** $\pi(x; q, a) \leq 2x/(\phi(q)\log(x/q))$ for $(a,q)=1$ and $x > q$.

None of these tools gives the information about $\mathcal{P}_\lambda$ that is needed.

### 10.2. Can sieve theory give bounds on $\mathcal{P}_\lambda$?

Sieve theory can, in principle, bound sums of the form $\sum_p f(p)$ for multiplicative functions $f$. In our case $f(p) = \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$, which is a function of $\log p$ (not directly multiplicative). Sieves work with multiplicative functions on the primes, but $B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\,dm_\infty(s)$ is a smooth function of $\log p$ and can be treated as an additive function on the multiplicative semigroup.

**Remark 10.1.** A standard computation (Perron's formula + zero-free region) gives:
$$\sum_{p \leq x} \frac{\log p}{\sqrt{p}} e^{i\gamma\log p} = \sum_{p \leq x} \frac{\log p}{p^{1/2 - i\gamma}} \approx -\frac{x^{1/2+i\gamma}}{1/2-i\gamma + \text{contributions from zeros of $\zeta(s)$ near $1/2+i\gamma$}}.$$

This again involves the zeros of $\zeta$: the sum over primes at frequency $e^{i\gamma}$ is governed by the zero $\rho = 1/2 + i\gamma$ of $\zeta$ (if it exists). This is exactly the circularity of the Hadamard barrier.

### 10.3. A possible opening: information from the residue $\mathcal{R}_\lambda$

The term $\mathcal{R}_\lambda = \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}})$ is computable in principle from:
(a) the archimedean term $\mathcal{A}[h_\lambda]$, which involves only $\Gamma$ and is explicitly computable, and
(b) the sum $\sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}})$ over the known critical zeros of $\zeta$.

If for $\lambda$ sufficiently large $\mathcal{R}_\lambda$ were **negative**, then from $T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ and $T_\lambda \geq 0$, it would follow that $\mathcal{P}_\lambda \leq \mathcal{R}_\lambda/2 < 0$. And from $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0) \geq 0$, it would follow that $0 \leq T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda \leq \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$... but if $\mathcal{R}_\lambda < 0$ and $\mathcal{P}_\lambda < 0$, there is no direct contradiction.

**Proposition 10.2** (Sign of $\mathcal{R}_\lambda$). *The sign of $\mathcal{R}_\lambda = \mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}}h_\lambda(\gamma_j^{\mathrm{on}})$ is not determined a priori. It depends on:*
*(a) the value of the archimedean term $\mathcal{A}[h_\lambda]$ (positive if $h_\lambda$ is positive and large at $s = i/2$),*
*(b) the contribution of the critical zeros $\sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}})$ (which is a sum of values of $h_\lambda$ at the $\gamma_j^{\mathrm{on}}$, with sign depending on $h_\lambda$).*

*It cannot be concluded that $\mathcal{R}_\lambda < 0$ in general.*

### 10.4. The "rate comparison" direction

The most concrete opening that remains open is the comparison of growth rates in $\lambda$ of the two quantities. The working hypothesis would be:

**Working hypothesis 10.3** (Differential rate). *The lower bound $4\delta_0^2 K_\lambda(\gamma_0)$ under $\neg$RH grows as a power of $\lambda$ (say $\lambda^\alpha$ for some $\alpha > 0$ determined by the Jacobi basis), while the prime sum $\mathcal{P}_\lambda$ grows as $\lambda^\beta$ with $\beta < \alpha$.*

If this hypothesis were true, for $\lambda$ sufficiently large the lower bound would exceed the prime sum (plus the archimedean term), giving a contradiction.

**Obstacle to 10.3:** Without explicitly computing the growth rates of $K_\lambda(\gamma_0)$ and $B_\lambda(\log p)$ in the Jacobi basis of $L^2(dm_{\mathrm{full,on}})$ (which is an object that depends on $\zeta$ itself and is hard to analyze), it cannot be verified whether $\alpha > \beta$ or not. The analysis of these rates requires information about the orthogonal polynomials $P_k$ of $L^2(dm_{\mathrm{full,on}})$, which in turn depend on the zeros of $\zeta$.

---

## §11. Formulation of the lemma-conjecture that would close the direction

### 11.1. The sufficient lemma

We summarize what the arithmetic result that would close Direction A would be.

**Conjecture $\mathbf{C}_A$ (Missing lemma of Direction A).** *For the family of test functions $\{h_\lambda\}_{\lambda > 0}$ of the CCM framework, the prime sum satisfies:*
$$\mathcal{P}_\lambda = 2\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p) \leq \mathcal{R}_\lambda - \eta_\lambda,$$
*where $\eta_\lambda > 0$ is a quantity that grows without bound with $\lambda$, and the bound is unconditional (without assuming RH).*

If $\mathbf{C}_A$ were true, and moreover $4\delta_0^2 K_\lambda(\gamma_0) > \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ for large $\lambda$ under $\neg$RH, the sought contradiction would be obtained.

**Critical frank note:** Conjecture $\mathbf{C}_A$ currently has no analytic support. There is no a priori reason to believe that the prime sum should be smaller than $\mathcal{R}_\lambda - \eta_\lambda$: the Weil formula imposes exactly that $\mathcal{P}_\lambda = (\mathcal{R}_\lambda - T_\lambda)/2$, so if $T_\lambda = 0$ (RH) then $\mathcal{P}_\lambda = \mathcal{R}_\lambda/2$, and if $T_\lambda > 0$ ($\neg$RH) then $\mathcal{P}_\lambda < \mathcal{R}_\lambda/2$. Conjecture $\mathbf{C}_A$ says that this second possibility ($\mathcal{P}_\lambda < \mathcal{R}_\lambda/2$) implies something contradictory — but the Weil formula imposes no contradiction here.

### 11.2. Variant: the conjecture on the positivity of $B_\lambda$

A weaker form of the conjecture that might be provable:

**Conjecture $\mathbf{C}_A'$ (Positivity of Fourier coefficients).** *For every $\lambda > 0$ and every prime $p$:*
$$B_\lambda(\log p) = \int W_\lambda(s)\cos(s\log p)\,dm_\infty(s) > 0.$$

If $\mathbf{C}_A'$ were true, then $\mathcal{P}_\lambda > 0$, and the formula $T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ would imply $T_\lambda < \mathcal{R}_\lambda$. This alone does not close the argument, but it could be a first step.

**Remark 11.1.** The positivity of $B_\lambda(\log p)$ seems hard to prove: $W_\lambda(s) \geq 0$ but $\cos(s\log p)$ oscillates. For small $\log p$ (small primes) it is plausible that $B_\lambda(\log p) > 0$ since the cosine oscillates slowly and $W_\lambda dm_\infty$ has mass concentrated near $s = 0$ where $\cos(0) = 1 > 0$. For large primes, the cosine oscillates rapidly and the integral can be positive or negative.

### 11.3. The arithmetic coherence lemma

A third, more conceptual formulation:

**Coherence lemma $\mathbf{L}_{A}^{\mathrm{coh}}$ (Hypothetical).** *If under $\neg$RH the distribution of off-critical zeros produces $T_\lambda \geq \varepsilon > 0$ for every $\lambda > 0$, then the distribution of primes at the frequencies $\{e^{i\gamma_j\log p} : p \text{ prime}, j \in J\}$ (where $\gamma_j$ are the imaginary parts of the off-critical zeros) satisfies a quantifiable irregularity that is incompatible with the known analytic properties of $\zeta$ in $\mathrm{Re}(s) > 1$.*

This lemma would attempt to use the fact that the hypothetical off-critical zeros "perturb" the distribution of primes in a specific way, and that this perturbation is visible in $\mathcal{P}_\lambda$. It is the most direct way to exploit the prime-zero duality.

**Status of $\mathbf{L}_A^{\mathrm{coh}}$:** Currently without proof or direct analytic support. The difficulty is that the perturbation of the distribution of primes introduced by an off-critical zero is (via the Weil formula) exactly the perturbation that makes $T_\lambda > 0$ — that is, the two statements are equivalent and there is no new information.

---

## §12. Relation to other classical approaches

### 12.1. The Weil method (1952)

Weil's original attempt to use the explicit formula for RH consists of finding a test function $h$ such that the sum $\sum_\rho h(\gamma_\rho)$ is negative under $\neg$RH and positive under RH. If such an $h$ existed, the Weil formula would give a contradiction.

Bombieri (2000) showed that this approach reduces to the problem of finding an admissible function $h$ such that the "Weil form" $W_h = \sum_\rho h(\gamma_\rho) - \mathcal{A}[h] + 2\mathcal{P}[h]$ has determined sign. The positivity of this form over all admissible functions $h$ would be equivalent to RH. But proving that positivity is as hard as proving RH directly.

Direction A is an instance of this approach with $h = h_\lambda$ (the CCM framework's test function). The conclusion of the analysis is the same as Bombieri's: the argument is circular.

### 12.2. The Beurling-Nyman method

The Beurling-Nyman criterion says that RH is equivalent to a certain family of functions being dense in $L^2(0,1)$. This criterion has an interpretation via the prime sum (via the function $\rho(x) = \{1/x\}$), but it also gives no new information about the distribution of primes beyond reformulating RH.

### 12.3. The "operator zeta function" and the spectral approach

Connes's spectral approach (1999) interprets RH as the condition that a certain operator has real spectrum. The relation with the distribution of primes passes through the trace of the operator, which satisfies the Weil formula. Again, it is a reformulation.

The difference in the current program (CCM-Jacobi) is that it has a more explicit structure (the polynomials $P_k$, the measure $dm_{\mathrm{full,on}}$, the trace $T_\lambda$) than previous approaches. But the underlying obstacle is the same.

---

## §13. Final status of Direction A

### 13.1. What is proved

**Theorem 13.1** (Established facts about Direction A).

*(i) The arithmetic formula $T_\lambda = \mathcal{R}_\lambda - 2\mathcal{P}_\lambda$ is a corollary of the Weil-Guinand formula applied to $h_\lambda$, formal but with the exact content of Theorem 2.1 and Lemma 2.2.*

*(ii) Under $\neg$RH, $T_\lambda \geq 4\delta_0^2 K_\lambda(\gamma_0) > 0$ (Proposition 5.1).*

*(iii) The series $\mathcal{P}_\lambda$ converges absolutely for every $\lambda > 0$ (Corollary 4.3).*

*(iv) There is no non-trivial upper bound on $\mathcal{P}_\lambda$ coming only from the distribution of primes that is incompatible with the lower bound under $\neg$RH.*

*(v) The strategy of Direction A falls under the Hadamard barrier (Proposition 9.5).*

*(vi) The "missing lemma" that would close the argument (Conjecture $\mathbf{C}_A$) lacks analytic support and its precise formulation reveals that it is equivalent to RH.*

### 13.2. What is not proved (and probably will not be by this route)

- It has not been proved that $B_\lambda(\log p) > 0$ for all primes $p$ (Conjecture $\mathbf{C}_A'$).
- No lower bound on $\mathcal{P}_\lambda$ has been proved that is incompatible with the lower bound under $\neg$RH.
- No argument has been found that uses the distribution of primes in a way genuinely independent of the Weil formula (which is a tautology with respect to the zeros).

### 13.3. Verdict

**Verdict 13.2.** *Direction A does not lead to a proof of RH via the paths examined. The obstacle is the Hadamard barrier: any use of the distribution of primes to bound $T_\lambda$ necessarily passes through the Weil formula, which is a reformulation of RH. There is no way to extract from the PNT, the known zero-free region, or the density theorems, information about $\mathcal{P}_\lambda$ that is independent of the position of the zeros of $\zeta$.*

*However, Direction A contributes to the program in the following ways:*

*1. It provides the precise formulation of $A_\lambda^{\mathrm{off}}$ and its relation to $K_\lambda(\gamma_0)$ (Section 3).*
*2. It identifies $B_\lambda(\log p)$ as the central arithmetic object in the CCM framework (Section 4).*
*3. It clarifies that the obstacle is the Hadamard barrier and not a technical weakness (Section 9).*
*4. It suggests that studying the growth rates of $K_\lambda(\gamma_0)$ vs. $\mathcal{P}_\lambda$ in $\lambda$ could be of independent value for understanding the structure of the Jacobi basis (Section 10.4), although this does not close the RH argument.*

---

## Appendix A: The Weil-Guinand formula: technical details

### A.1. Convergence of the sum over zeros

The sum $\sum_\rho h(\gamma_\rho)$ converges absolutely if $|h(s)| = O(|s|^{-1-\varepsilon})$ (a weaker condition than (W3)). For $h_\lambda(s) = W_\lambda(s)(2\pi)^{-2}|\Gamma(1/4+is/2)|^2$, the decay is exponential $O(e^{-\pi|s|/2})$, which guarantees absolute convergence.

The sum $\sum_{\rho_{\mathrm{on}}} h(\gamma_j^{\mathrm{on}})$ over the critical zeros also converges: the zeros $\gamma_j^{\mathrm{on}} \sim (2\pi j/\log j)$ are dense and $h(\gamma_j^{\mathrm{on}}) = O(e^{-\pi\gamma_j/2})$ decays, so the sum converges.

### A.2. The function $\zeta_{\mathrm{on}}$ and the zeros on the critical line

The function $\zeta_{\mathrm{on}}$ (Doc 83) is defined as the Hadamard product with the same zeros as $\zeta$ but projected onto the critical line: if $\rho = \sigma + i\gamma$ is a zero of $\zeta$, the corresponding zero of $\zeta_{\mathrm{on}}$ is $1/2 + i\gamma$. Under RH, $\zeta = \zeta_{\mathrm{on}}$ (all zeros are already on the critical line). The sum $\sum_{\rho_{\mathrm{on}}} h(\gamma_j^{\mathrm{on}})$ is the Weil sum applied to the zeros of $\zeta_{\mathrm{on}}$.

### A.3. The term $\hat{h}(0)\log(1/(2\pi))$ and normalization

In the standard Weil formula, the factor $\log(1/(2\pi))$ (negative) appears. In some versions of the formula this factor is absorbed into the archimedean term $\mathcal{A}[h]$. In the CCM framework, the measure $dm_\infty = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 ds$ already includes the archimedean normalization, so the factors of $2\pi$ enter naturally into $\mathcal{A}[h_\lambda]$.

---

## Appendix B: Summary of symbols

| Symbol | Definition |
|---------|------------|
| $dm_\infty(s)$ | $(2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ |
| $dm_{\mathrm{full}}(s)$ | $|\zeta(1/2+is)|^2\,dm_\infty(s)$ |
| $dm_{\mathrm{full,on}}(s)$ | $|\zeta_{\mathrm{on}}(1/2+is)|^2\,dm_\infty(s)$ |
| $d\nu$ | $dm_{\mathrm{full}} - dm_{\mathrm{full,on}} \geq 0$ |
| $W_\lambda(s)$ | Abel kernel of the Jacobi basis of $L^2(dm_{\mathrm{full,on}})$ |
| $T_\lambda$ | $\int W_\lambda\,d\nu$ (CCM trace) |
| $h_\lambda(s)$ | $W_\lambda(s)(2\pi)^{-2}|\Gamma(1/4+is/2)|^2$ (test function) |
| $\hat{h}(r)$ | $\int h(s)e^{irs}\,ds$ (Fourier transform) |
| $B_\lambda(r)$ | $\int W_\lambda(s)\cos(rs)\,dm_\infty(s) = \hat{h}_\lambda(r)$ |
| $\mathcal{P}_\lambda$ | $\sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ |
| $\mathcal{R}_\lambda$ | $\mathcal{A}[h_\lambda] - \sum_{\rho_{\mathrm{on}}} h_\lambda(\gamma_j^{\mathrm{on}})$ |
| $A_\lambda^{\mathrm{off}}$ | $\int W_\lambda\,(R-1)\,dm_{\mathrm{full,on}} = T_\lambda$ |
| $K_\lambda(\gamma)$ | $\int W_\lambda(s)(s-\gamma)^{-2}\,dm_{\mathrm{full,on}}(s)$ |
| $\delta_j$ | $\mathrm{Re}(\rho_j) - 1/2 > 0$ (off-critical zero displacement) |
| $\gamma_j$ | $\mathrm{Im}(\rho_j)$ (imaginary part of the off-critical zero) |

---

## Appendix C: The prime-zero duality and why it is not unilaterally exploitable

### C.1. The symmetric nature of the Weil formula

The Weil-Guinand formula is fundamentally symmetric: the zeros of $\zeta$ and the primes appear on opposite sides of an equality, and determine each other. It is not possible, within the framework of the Weil formula, to use the distribution of primes to "discover" something about the zeros that is not already known through the same formula.

More precisely: if all the primes (and all their powers) are known, the Weil formula determines all the zeros of $\zeta$. Conversely, if all the zeros are known, the formula determines the distribution of primes. The relation is bijective (for sufficiently rich test functions); there is no additional information on either side that is not in the other.

### C.2. The case of the zeta function of a curve over a finite field

In the case of the geometric analogue (zeta function of a curve over $\mathbb{F}_q$), the Riemann Hypothesis was proved by Weil (1948). The argument uses the positivity of the intersection of cycles on the surface $C \times C$ (positivity criterion of the Weil form). In that case, the extra information that allows the argument to close is **geometric**: the positivity of the intersection form has an interpretation in terms of the geometry of the curve that is genuinely independent of the zeros of the zeta function.

In the case of $\zeta(s)$ over $\mathbb{Z}$, no arithmetic analogue of this geometric positivity has been found. Direction A attempts to use the distribution of primes to supply that information, but the distribution of primes is equivalent to the distribution of zeros (via Weil) and does not provide the analogue of the geometric positivity.

### C.3. What would be different

If there existed an arithmetic object $X$ such that:
1. $X$ is computable from the primes without using the Weil formula.
2. Under $\neg$RH, $X$ satisfies a bound incompatible with the properties of $\zeta$ in $\mathrm{Re}(s) > 1$.
3. Under RH, $X$ is compatible with all the properties of $\zeta$.

Then Direction A (or a variant) would close the argument. The search for such an object $X$ is, in a certain sense, the search for the arithmetic analogue of Weil's geometric positivity. No candidate is known.

---

*End of Document 90.*

*Synthesis note:* Direction A has been explored rigorously and the verdict is negative in its current formulation. The obstacle is structural (Hadamard barrier) and not technical. The formulas developed (expression of $A_\lambda^{\mathrm{off}}$, properties of $B_\lambda$, formulation of Conjecture $\mathbf{C}_A$) are contributions to the program's framework even though they do not close the argument. Direction B (to be explored in Doc 91) and the other directions of Phase 34 must seek arithmetic information that is genuinely independent of the Weil formula.
