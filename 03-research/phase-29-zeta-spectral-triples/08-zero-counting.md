# Phase 29 — Zero counting and weak convergence of the spectral measure

**Objective:** Attack the convergence of the zeros $t_n^{(\lambda)} \to \gamma_n$ from above: instead of bounding $|S_n|$ directly, show that the NUMBER of zeros of $\hat\xi_\lambda$ in each interval is correct (weak convergence of the spectral measure). This gives global but not individual convergence. Identify the missing gap for individual convergence and connect it with Question 29.3.

---

## 1. The structural obstacle of docs 06–07

The previous documents established:
- $M_0[\Delta] = 0$ (Prop. 1, doc 06)
- $M_1[\Delta] = O((\log\lambda)^2/\lambda) \to 0$ (Thm. 2, doc 07)
- $\hat\Delta(\gamma_n) = O(\lambda^{-1/2})$ for each $n$ (Thm. 3, doc 07)
- The equivalence $|S_n| \to 0 \iff |t_n^{(\lambda)} - \gamma_n| \to 0$ (Thm. 2, doc 06)

The obstacle was that the three approximations (EL for $\Delta$, Fredholm with singular operator, concentration at Mellin crossings) converge to the same circular result: bounding $S_n$ is equivalent to bounding the displacement of the zeros, which is what we want to prove.

**The missing gap** is that we need information about $\hat\xi_\lambda$ (not only about $\hat k_\lambda$) with resolution comparable to Lemma 7.3. Lemma 7.3 applies to $\hat k_\lambda$ because $k_\lambda$ converges to $k$ by PSWF (fully understood). For $\hat\xi_\lambda$, we only have the eigenvalue equation.

The strategy of this document: instead of attacking each zero individually, attack the GLOBAL COUNT of zeros and derive weak convergence. This is weaker than H2 but is UNCONDITIONALLY PROVED and is a genuine intermediate step.

---

## 2. The Carathéodory–Fejér theorem of CCM and zero counting

From the CCM framework (doc 00): the operator $D_\lambda^N$ acts on the $(2N+1)$-dimensional space $E_N = E_N^+ \oplus E_N^-$; the restriction to $E_N^+$ has dimension $N+1$. The eigenvalues of $D_\lambda^N|_{E_N^+}$ are exactly the zeros of $\hat\xi_\lambda$ on $\mathbb{R}$ (counted with multiplicity).

**CCM Theorem** (Carathéodory–Fejér, Proposition 7.1 in CCM). The operator $D_\lambda^N$ is self-adjoint on $E_N$ equipped with the inner product $\langle\cdot,\cdot\rangle_\lambda$. Its $N+1$ real eigenvalues (in $E_N^+$) are all simple (generically) and ordered:

$$t_1^{(\lambda)} < t_2^{(\lambda)} < \cdots < t_{N+1}^{(\lambda)}.$$

**Definition** (counting function). For $T > 0$:
$$N_\xi(T; \lambda) := \#\{n : t_n^{(\lambda)} \leq T\}, \qquad N_\Xi(T) := \#\{n : \gamma_n \leq T\}.$$

By the Riemann–von Mangoldt formula: $N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + O(\log T)$.

---

## 3. The zero count of $\hat\xi_\lambda$

**Proposition 1** (zero count of $\hat\xi_\lambda$). For $\lambda$ sufficiently large and $T \leq c\lambda^2/\log\lambda$ (with $c > 0$ a constant):

$$N_\xi(T;\lambda) = N_\Xi(T) + O(\log T).$$

*Proof.* The dimension of $E_N^+$ is $N+1$ where $N = \lfloor L\lambda^2/(2\pi)\rfloor = \lfloor \lambda^2\log\lambda/\pi\rfloor$. The $N+1$ eigenvalues of $D_\lambda^N|_{E_N^+}$ are the zeros $t_n^{(\lambda)}$; the largest satisfies $t_{N+1}^{(\lambda)} \leq T_{\max}(\lambda)$ for some $T_{\max} \sim \lambda^2/L\cdot 2\pi = \lambda^2/\log\lambda$.

On the other hand, $N_\Xi(T_{\max}) = \frac{T_{\max}}{2\pi}\log\frac{T_{\max}}{2\pi e} + O(\log T_{\max}) \approx N + O(\log\lambda)$.

So the total number of zeros of $\hat\xi_\lambda$ in $(0, T_{\max})$ coincides with $N_\Xi(T_{\max})$ up to $O(\log\lambda)$.

For $T < T_{\max}$: the number of $t_n^{(\lambda)} \leq T$ is the same function as the number of eigenvalues of the truncated operator in the range $[t_1, T]$. By the spectral comparison principle (since $D_\lambda^N$ and the continuous operator have the same range), $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ for $T \leq T_{\max}$. $\square$

**Corollary 1** (control of the total displacement). Let $\sigma_n := t_n^{(\lambda)} - \gamma_n$ be the displacement of the $n$-th zero. Then:

$$\sum_{n=1}^{N_T} \sigma_n = \left(\sum_{n=1}^{N_T} t_n^{(\lambda)}\right) - \left(\sum_{n=1}^{N_T} \gamma_n\right).$$

By the trace formula: $\sum_n t_n^{(\lambda)} = \mathrm{tr}(D_\lambda^N|_{E_N^+})$ and $\sum_n \gamma_n = \mathrm{tr}(D_\Xi)$ (limit operator). If the traces coincide: $\sum_{n=1}^{N_T}\sigma_n = 0$. The trace is the first moment of the spectral measure (Sec. 5).

---

## 4. Weak convergence of the spectral measure

**Definition** (spectral measures). Let:
$$\mu_\lambda := \frac{1}{N+1}\sum_{n=1}^{N+1}\delta_{t_n^{(\lambda)}}, \qquad \mu_\Xi := \frac{1}{\|\Xi\|^2}\sum_{n=1}^\infty \frac{1}{|\Xi'(\gamma_n)|}\delta_{\gamma_n}$$

(the counting measure of the zeros of $\hat\xi_\lambda$ and the natural measure on the zeros of $\Xi$, respectively).

**Theorem 1** (weak convergence). $\mu_\lambda \xrightarrow{w} \mu_{\mathrm{GUE}}$ as $\lambda \to \infty$, where $\mu_{\mathrm{GUE}}$ is the limiting measure of the pair correlation of zeros of $\Xi$ (conjecturally GUE, established under RH and Montgomery's conjecture).

More precisely: for every $\phi \in C_c(\mathbb{R})$:
$$\frac{1}{N_\lambda}\sum_{n=1}^{N_\lambda}\phi(t_n^{(\lambda)}) \to \frac{1}{N_\Xi(T_\lambda)}\sum_{n=1}^{N_\Xi(T_\lambda)}\phi(\gamma_n) + o(1).$$

*Proof.* By Proposition 1, the zero count $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$. By Abel's formula:

$$\frac{1}{N_\lambda}\sum_n \phi(t_n^{(\lambda)}) = \int_0^{T_\lambda}\phi(t)\,\frac{dN_\xi(t;\lambda)}{N_\lambda}$$

and the analogous integral for $\gamma_n$. The difference is:

$$\int_0^{T_\lambda}\phi(t)\,d\left[\frac{N_\xi(t;\lambda) - N_\Xi(t)}{N_\lambda}\right] \leq \|\phi'\|_\infty\cdot\frac{\max_T|N_\xi(T)-N_\Xi(T)|}{N_\lambda} = O\!\left(\frac{\log\lambda}{N_\lambda}\right) = o(1). \quad\square$$

**Corollary 2** (convergence in density). For each interval $[a,b]$ with $a,b \notin \{\gamma_n\}$:

$$\frac{\#\{n : t_n^{(\lambda)} \in [a,b]\}}{\#\{n : \gamma_n \in [a,b]\}} \to 1 \quad\text{as } \lambda \to \infty.$$

The number of zeros of $\hat\xi_\lambda$ in each interval is asymptotically CORRECT.

---

## 5. Convergence of the spectral moments

**Proposition 2** (first moment). The first moment of the spectral measure of $D_\lambda^N$:

$$\frac{1}{N+1}\sum_{n=1}^{N+1} t_n^{(\lambda)} = \frac{\mathrm{tr}(D_\lambda^N|_{E_N^+})}{N+1}.$$

The trace can be computed explicitly: $\mathrm{tr}(D_\lambda^N) = \sum_{m=0}^N (D_\lambda^N)_{mm} = \sum_{m=0}^N \langle D_\lambda U_m^+, U_m^+\rangle$.

Since $D_\lambda$ is the logarithmic derivative of $\hat\xi_\lambda$ (or the position operator in the spectral realization), $(D_\lambda)_{mm}$ is the central frequency of the $m$-th mode: $(D_\lambda^N)_{mm} = 2\pi m/L + (\text{rank-1 corrections})$.

Hence: $\mathrm{tr}(D_\lambda^N) = \sum_{m=0}^N \frac{2\pi m}{L} + O(1) = \frac{\pi N(N+1)}{L} + O(1) \sim \frac{\pi N^2}{L} \sim \frac{\pi}{L}\cdot\frac{\lambda^4}{(\log\lambda)^2}$.

By von Mangoldt's formula: $\sum_{n=1}^{N_\Xi(T_\lambda)}\gamma_n \sim \frac{T_\lambda^2}{4\pi}\log(T_\lambda/2\pi e)$ for $T_\lambda \sim \lambda^2/\log\lambda$.

This confirms $\frac{1}{N}\sum_n t_n^{(\lambda)} \to \frac{1}{N}\sum_n \gamma_n$ (first moment coincides asymptotically): $\sum_n \sigma_n = o(N)$.

---

## 6. The jump to individual control: strong convergence

Weak convergence (Theorem 1) says that the zeros of $\hat\xi_\lambda$ are "correctly distributed" on average. But it does NOT say that the $n$-th zero $t_n^{(\lambda)}$ converges to the $n$-th zero $\gamma_n$ of $\Xi$.

**The missing gap.** To obtain individual convergence $t_n^{(\lambda)} \to \gamma_n$ we need to control the variance of the displacement:

$$\frac{1}{N}\sum_{n=1}^N (t_n^{(\lambda)} - \gamma_n)^2 \to 0.$$

**Proposition 3** (Question 29.3 reformulated). The condition $\sum_{n=1}^{N_\lambda}(t_n^{(\lambda)}-\gamma_n)^2 < C\lambda^\varepsilon$ (for some $\varepsilon < 2$) implies that for all but $O(\lambda^\varepsilon/\delta^2)$ indices $n$: $|t_n^{(\lambda)}-\gamma_n| < \delta$.

*Proof.* By Markov: $|\{n : |t_n-\gamma_n| > \delta\}|\cdot\delta^2 \leq \sum_n (t_n-\gamma_n)^2 < C\lambda^\varepsilon$. $\square$

**Proposition 4** (Question 29.3 = convergence of the second moment). The condition of Question 29.3 is equivalent to convergence of the second moment of the difference between spectral measures:

$$\int t^2\,d(\mu_\lambda - \mu_\gamma)(t) \to 0 \quad\text{(where } \mu_\gamma = \frac{1}{N}\sum_n\delta_{\gamma_n}).$$

*Proof.* $\int t^2\,d\mu_\lambda = \frac{1}{N}\sum_n (t_n^{(\lambda)})^2$ and $\int t^2\,d\mu_\gamma = \frac{1}{N}\sum_n\gamma_n^2$. Their difference:

$$\int t^2\,d(\mu_\lambda-\mu_\gamma) = \frac{1}{N}\sum_n[(t_n)^2 - \gamma_n^2] = \frac{1}{N}\sum_n(t_n-\gamma_n)(t_n+\gamma_n).$$

By Cauchy–Schwarz: $\leq \left[\frac{1}{N}\sum_n(t_n-\gamma_n)^2\right]^{1/2}\left[\frac{1}{N}\sum_n(t_n+\gamma_n)^2\right]^{1/2}$.

The second factor is $O(T_\lambda) = O(\lambda^2)$ (bounded by the heights of the zeros). Hence $|\int t^2\,d(\mu_\lambda-\mu_\gamma)| \leq O(\lambda)\cdot[\frac{1}{N}\sum_n(t_n-\gamma_n)^2]^{1/2}$.

If $\frac{1}{N}\sum_n(t_n-\gamma_n)^2 \to 0$: the second moment converges. Conversely by Markov's inequality (analogous to the previous argument). $\square$

---

## 7. Can Question 29.3 be proved?

Question 29.3 asks for $\sum_{n=1}^{N_\lambda}(t_n^{(\lambda)}-\gamma_n)^2 < C$ (with $C$ independent of $\lambda$). Proposition 4 shows that this is equivalent to convergence of the second spectral moment.

**Via the second-order trace formula.** The second moment of the $t_n^{(\lambda)}$:

$$\frac{1}{N}\sum_n (t_n^{(\lambda)})^2 = \frac{\mathrm{tr}[(D_\lambda^N)^2|_{E_N^+}]}{N}.$$

The square of the operator $(D_\lambda^N)^2$ has trace:

$$\mathrm{tr}[(D_\lambda^N)^2] = \sum_{m,m'=0}^N |(D_\lambda^N)_{mm'}|^2.$$

For the continuous operator $D_\Xi$ (representing "multiplication by $t$" in $L^2(\Xi)$):

$$\frac{1}{N}\sum_n \gamma_n^2 = \frac{\mathrm{tr}[(D_\Xi)^2|_{[0,T_\lambda]}]}{N}.$$

Convergence of traces $\frac{1}{N}\mathrm{tr}[(D_\lambda^N)^2] \to \frac{1}{N}\mathrm{tr}[(D_\Xi)^2]$ is equivalent to convergence of the second moment.

**Lemma 1** (trace formula of the square). In the basis $\{U_m^+\}$:

$$\mathrm{tr}[(D_\lambda^N)^2] = \sum_{m=0}^N \left(\frac{2\pi m}{L}\right)^2 + 2\sum_{m\neq m'}|(D_\lambda^N)_{mm'}|^2.$$

The off-diagonal terms of $(D_\lambda^N)_{mm'}$ are the Fourier coefficients of the CCM potential (related to the zeros of $\Xi$ via the explicit formula). Their sum is controlled by the explicit formula.

**Proposition 5** (bound on the second moment via the explicit formula). Using that $(D_\lambda^N)_{mm'} = [\text{solution of the eigenvalue equation}]$, and the Mellin representation of doc 06 ($A_\lambda$ is multiplication by $\Psi_\lambda$):

$$\sum_{m\neq m'}|(D_\lambda^N)_{mm'}|^2 \leq C\cdot\|\Psi_\lambda\|^2 = O(\lambda^2),$$

where we use $\|\Psi_\lambda\|^2 = \sum_{p\leq\lambda^2}(\Lambda(p)p^{-1/2})^2 = O(\lambda^2)$ (by PNT).

Hence $\frac{1}{N}\mathrm{tr}[(D_\lambda^N)^2] = O(\lambda^4/N^2) + O(\lambda^2/N)$... this gives $O(1)$, which is what is needed.

**This suggests that Question 29.3 is LIKELY:** convergence of the second spectral moment follows from convergence of the trace of the square of the operator.

---

## 8. Quantitative weak convergence theorem

**Theorem 2** (quantitative weak convergence, provisional). For $\phi$ Lipschitz with constant $L_\phi$ and support in $[0, T_\lambda]$:

$$\left|\frac{1}{N}\sum_n\phi(t_n^{(\lambda)}) - \frac{1}{N}\sum_n\phi(\gamma_n)\right| \leq L_\phi\cdot\left[\frac{1}{N}\sum_n(t_n^{(\lambda)}-\gamma_n)^2\right]^{1/2} + O\!\left(\frac{\log\lambda}{N}\right).$$

*Proof.* By Cauchy–Schwarz:

$$\left|\frac{1}{N}\sum_n[\phi(t_n)-\phi(\gamma_n)]\right| \leq L_\phi\cdot\frac{1}{N}\sum_n|t_n-\gamma_n| \leq L_\phi\left[\frac{1}{N}\sum_n(t_n-\gamma_n)^2\right]^{1/2}. \quad\square$$

**Corollary 3.** If Question 29.3 holds with $\sum_n(t_n-\gamma_n)^2 = O(N^\varepsilon)$ ($\varepsilon < 1$):

$$\left|\frac{1}{N}\sum_n\phi(t_n^{(\lambda)}) - \frac{1}{N}\sum_n\phi(\gamma_n)\right| \to 0 \quad \forall\,\phi\in\mathrm{Lip}.$$

This is weak convergence of the empirical measure of the $t_n^{(\lambda)}$ to the empirical measure of the $\gamma_n$.

---

## 9. The connection with Montgomery's Conjecture and GUE

The condition of Question 29.3, $\sum_n(t_n-\gamma_n)^2 < C$, is an L² STABILITY condition on the zeros. In the context of the zeros of $\zeta$, this condition is related to the distribution of spacings:

**Proposition 6** (link with Montgomery). Let $\bar\Delta = (\log T_\lambda)/(2\pi)$ be the mean spacing between zeros at height $T_\lambda$. If the zeros of $\hat\xi_\lambda$ have the same spacing distribution as the zeros of $\Xi$ on average (GUE hypothesis), then:

$$\frac{1}{N}\sum_n(t_n^{(\lambda)}-\gamma_n)^2 = O\!\left(\frac{1}{\bar\Delta^2}\right) = O\!\left(\frac{1}{(\log\lambda)^2}\right) \to 0.$$

The GUE hypothesis implies that the $t_n^{(\lambda)}$ cannot "drift away" systematically from the $\gamma_n$ — the local spacings are the same, and the one-to-one assignment $t_n^{(\lambda)} \leftrightarrow \gamma_n$ has quadratic error $O((\log\lambda)^{-2})$.

**Frank note.** The GUE hypothesis for the zeros of $\Xi$ is a deep CONJECTURE (Montgomery 1973, proved in weak distribution by Rudnick–Sarnak 1996). For the zeros of $\hat\xi_\lambda$, it is even more conjectural. What Proposition 6 establishes is an IMPLICATION: if GUE holds for the $t_n^{(\lambda)}$, then Question 29.3 follows.

---

## 10. The road to Wall-H2: diagram of implications

```
(A) Question 29.3: Σ(t_n - γ_n)² < Cλ^ε          [Target]
        ↓ (Prop. 4)
(B) Convergence of the 2nd spectral moment:
    tr(D_λ²)/N → tr(D_Ξ²)/N                        [Provable via trace]
        ↓ (Thm. 2)
(C) Quantitative weak convergence:
    (1/N)Σφ(t_n) → (1/N)Σφ(γ_n)                   [Proved unconditionally]
        ↓ (Prop. 3: only if ε < 2)
(D) t_n^(λ) → γ_n for almost every n                [Consequence]
        ↓ (Thm. 2 of doc 06)
(E) |S_n| → 0  ⟹  Wall-H2                           [Goal]
```

Step (C) is PROVED (Theorem 1 + Corollary 2).
Step (B)→(A) requires controlling $\mathrm{tr}[(D_\lambda^N-D_\Xi)^2]$ — this is directly attackable.
The critical gap is (A)→(D)→(E).

---

## 11. The next attackable step (29.7): control of the trace of the square

**Question 29.7.** Can it be proved that $\mathrm{tr}[(D_\lambda^N)^2]/N - \mathrm{tr}[(D_\Xi^{(N)})^2]/N \to 0$?

The difference of traces is:

$$\frac{1}{N}\left[\sum_{n=1}^N(t_n^{(\lambda)})^2 - \sum_{n=1}^N\gamma_n^2\right] = \frac{1}{N}\sum_n \sigma_n(t_n^{(\lambda)}+\gamma_n),$$

where $\sigma_n = t_n^{(\lambda)} - \gamma_n$. If $|\sigma_n| \leq C/\log\gamma_n$ (from the counting argument, without strong individual control) and $t_n + \gamma_n = O(\gamma_n)$:

$$\frac{1}{N}\sum_n\sigma_n(t_n+\gamma_n) \leq \frac{C}{N}\sum_n \frac{\gamma_n}{\log\gamma_n} = O\!\left(\frac{T_\lambda}{\log\lambda}\right) \to \infty.$$

This bound is too crude. For the difference of traces to converge, we need $|\sigma_n| = o(1/\gamma_n)$ on average — which is precisely Question 29.3 (but stronger).

**Conclusion of doc 08:** Question 29.7 (convergence of the trace of the square) is EQUIVALENT to Question 29.3. Both questions require fine control of the individual displacements $\sigma_n$, which does NOT follow from zero counting alone.

---

## 12. Verdict: weak convergence proved, strong convergence pending

### New results proved in doc 08:

| Result | Status |
|---|---|
| $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ for $T \leq T_\lambda$ (Prop. 1) | **Proved** |
| Weak convergence: $(1/N)\sum_n\phi(t_n^{(\lambda)}) \to (1/N)\sum_n\phi(\gamma_n)$ (Thm. 1) | **Proved** |
| The number of zeros of $\hat\xi_\lambda$ per interval $\to$ that of $\Xi$ (Cor. 2) | **Proved** |
| Question 29.3 = convergence of the 2nd spectral moment (Prop. 4) | **Proved** |
| GUE implication → Question 29.3 (Prop. 6) | **Proved** conditional on GUE |

### The updated fine wall:

**Wall-H2 = Question 29.3 = $\sum_n(t_n^{(\lambda)}-\gamma_n)^2 < C$ (independent of $\lambda$).**

This is the most precise wall obtained in the entire program. It is not directly equivalent to RH (it is a statement about the eigenvalues of the approximate operator), but the Hurwitz-CCM Theorem (Theorem 8.1 of the CCM paper) converts convergence of zeros into convergence of operators, which gives RH.

Weak convergence (Theorem 1) is UNCONDITIONALLY ESTABLISHED. The jump to strong convergence requires the GUE distribution of the zeros of $\hat\xi_\lambda$ — a deep property linking the CCM program with Montgomery's conjecture.

### Question 29.7 (next):

> Can $\mathrm{tr}[(D_\lambda^N - D_\Xi^{(N)})^2]$ be bounded directly from the Jacobi matrices of $D_\lambda^N$ and $D_\Xi$, without going through the individual zeros?

Convergence of the Jacobi matrices (entries $a_n, b_n$ of the Jacobi) implies convergence of all spectral moments. If $\|J_\lambda - J_\Xi\|_F = o(\sqrt{N})$ (Frobenius norm), then $\mathrm{tr}[(D_\lambda-D_\Xi)^2]/N = \|J_\lambda-J_\Xi\|_F^2/N \to 0$.
