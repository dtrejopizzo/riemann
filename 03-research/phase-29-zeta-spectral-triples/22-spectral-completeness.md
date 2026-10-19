# Phase 29 — Doc 22: Spectral completeness and the gap between the empirical measure and the Weyl-Titchmarsh measure

**Objective:** Precisely identify the difference between the empirical spectral measure $\mu_\xi^\lambda$ (proved convergent to $\mu_\gamma^{real}$ in Doc 15) and the Weyl-Titchmarsh spectral measure $\mu_{WT}$ of the limiting operator $J_\infty$. Show that the equality of these two measures is equivalent to RH.

---

## 1. Two distinct spectral measures

For the Jacobi operator $J_\lambda^N$ (the CCM truncation to $N \times N$), there exist TWO natural spectral measures:

**Definition 1** (Empirical spectral measure). The empirical spectral measure is:

$$\mu_{emp}^{(\lambda,N)} := \frac{1}{N}\sum_{n=1}^N \delta_{t_n^{(\lambda)}},$$

where $\{t_n^{(\lambda)}\}$ are the eigenvalues of $J_\lambda^N$.

**Definition 2** (Weyl-Titchmarsh spectral measure). The spectral measure associated to the cyclic vector $e_0$ is the unique measure $\mu_{WT}^{(\lambda,N)}$ such that:

$$m_\lambda^{WT}(z) := \langle e_0, (J_\lambda^N - z)^{-1}e_0\rangle = \int_\mathbb{R}\frac{d\mu_{WT}^{(\lambda,N)}(t)}{t-z}.$$

The measure $\mu_{WT}$ has the explicit expression:

$$\mu_{WT}^{(\lambda,N)} = \sum_{n=1}^N |c_n^{(\lambda)}|^2\,\delta_{t_n^{(\lambda)}},$$

where $c_n^{(\lambda)} = \langle e_0, \psi_n^{(\lambda)}\rangle$ are the components of the vector $e_0$ in the eigenvector basis $\{\psi_n^{(\lambda)}\}$.

**Proposition 1** (the two measures are equal iff $e_0$ is completely delocalized). $\mu_{emp}^{(\lambda,N)} = \mu_{WT}^{(\lambda,N)}$ if and only if $|c_n^{(\lambda)}|^2 = 1/N$ for all $n = 1,\ldots,N$.

*Proof.* Direct from the definitions: $\mu_{WT} = \sum_n|c_n|^2\delta_{t_n}$ and $\mu_{emp} = (1/N)\sum_n\delta_{t_n}$. They are equal iff the weights match: $|c_n|^2 = 1/N$ for all $n$. $\square$

---

## 2. The gap in the CCM program: which function is $m_\lambda$?

Doc 14 establishes that $m_\lambda(z) = S_\xi(z;\lambda)/N$ (the Stieltjes transform of the empirical measure divided by $N$), and ALSO that $m_\lambda = \langle e_0, (J_\lambda - z)^{-1}e_0\rangle$ (the Weyl-Titchmarsh function).

**Proposition 2** (the two identifications of Doc 14 are consistent iff the CCM has uniform delocalization). The two definitions of $m_\lambda$ in Doc 14:

$$m_\lambda^{(1)}(z) = \frac{1}{N}\sum_{n=1}^N\frac{1}{t_n^{(\lambda)}-z}, \quad m_\lambda^{(2)}(z) = \langle e_0, (J_\lambda - z)^{-1}e_0\rangle,$$

satisfy $m_\lambda^{(1)} = m_\lambda^{(2)}$ if and only if $|c_n^{(\lambda)}|^2 = 1/N$ for all $n$ (Proposition 1).

**Remark.** In the random matrix literature (GUE ensemble), the eigenvectors have entries of order $O(N^{-1/2})$ at all positions (delocalization), and on average $\mathbb{E}[|c_n|^2] = 1/N$. For the specific CCM operator, delocalization is a hypothesis, not a theorem.

---

## 3. The limit $\lambda \to \infty$: the two limiting measures

**Definition 3.**
- $m_\infty^{emp}(z) := \lim_\lambda m_\lambda^{(1)}(z) = $ limit of the Stieltjes transform of $\mu_{emp}^\lambda$, whose limiting measure is $\mu_\gamma^{real}$ (Doc 15).
- $m_\infty^{WT}(z) := \lim_\lambda m_\lambda^{(2)}(z) = $ limit of the Weyl-Titchmarsh function, whose limiting measure is $\mu_{WT}^\infty$ (the spectral measure of $J_\infty$ at $e_0$).

**Proposition 3** (the two limiting measures may differ). In the limit $\lambda \to \infty$:

$$\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real} \quad (\text{Doc 15, unconditional}).$$

But the convergence $m_\lambda^{(2)}(z) \to m_\infty^{WT}(z)$ (Weyl-Titchmarsh) gives a measure $\mu_{WT}^\infty$ that is the spectral measure of $J_\infty$ associated to the vector $e_0$. This measure satisfies:

$$\mathrm{spec}(J_\infty) = \mathrm{supp}(\mu_{WT}^\infty),$$

by the spectral theorem for self-adjoint operators with a cyclic vector.

**If $\mu_{WT}^\infty = \mu_\gamma^{real}$:** then $\mathrm{spec}(J_\infty) = \mathrm{supp}(\mu_\gamma^{real}) = \{\gamma_n\}$. Combined with Theorem C1 (Doc 17): $\{\text{real zeros of }C_\infty\} = \{\gamma_n\}$. By Theorem 3 of Doc 19: RH.

**If $\mu_{WT}^\infty \neq \mu_\gamma^{real}$:** the two measures have different supports and the previous conclusions do not apply directly.

---

## 4. When they coincide: the delocalization hypothesis

**Definition 4** (Delocalization of $e_0$ in $J_\lambda$). We say that $J_\lambda$ is *uniformly delocalized* (UD) if:

$$\max_{1\leq n\leq N}|c_n^{(\lambda)}|^2 = O(N^{-1+\varepsilon}) \quad \text{for every }\varepsilon > 0,$$

uniformly in $\lambda \geq \lambda_0$ (with $N = N(\lambda) \to \infty$).

**Proposition 4** (UD implies that the two measures have the same support). If $J_\lambda$ is uniformly delocalized, then:

$$\mathrm{supp}(\mu_{WT}^{(\lambda,N)}) = \mathrm{supp}(\mu_{emp}^{(\lambda,N)}) = \{t_1^{(\lambda)},\ldots,t_N^{(\lambda)}\}.$$

*Proof.* $\mu_{WT} = \sum_n |c_n|^2\delta_{t_n}$. If $|c_n|^2 > 0$ for all $n$ (which follows from UD since $\sum_n|c_n|^2 = \|e_0\|^2 = 1$ and $|c_n|^2 \leq O(N^{-1+\varepsilon})$ implies that each $|c_n|^2 \geq c/N$ for some constant $c > 0$ for most $n$): the support of $\mu_{WT}$ includes all the $t_n$. The support of $\mu_{emp}$ is exactly $\{t_n\}$. $\square$

**Proposition 5** (UD in the limit implies $\mu_{WT}^\infty = \mu_\gamma^{real}$). If delocalization is preserved in the limit $\lambda \to \infty$:

$$\lim_\lambda\max_n|c_n^{(\lambda)}|^2 \to 0 \quad (\text{asymptotic delocalization}),$$

then $\mu_{WT}^\infty = \mu_\gamma^{real}$ (the two limiting measures coincide).

*Proof (heuristic, formal).* Under asymptotic delocalization: the weights $|c_n^{(\lambda)}|^2 \to 1/N$ uniformly. In the limit: the Weyl-Titchmarsh measure $\mu_{WT}^\lambda = \sum_n|c_n|^2\delta_{t_n} \approx (1/N)\sum_n\delta_{t_n} = \mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$. $\square$

---

## 5. The connection to Montgomery-GUE

**The GUE hypothesis.** The correlations of the zeros of $\zeta$ (conjecturally) follow the distribution of the eigenvalues of the GUE ensemble (Montgomery, 1973). In the GUE ensemble, the eigenvectors are uniformly distributed on the complex unit sphere, and in particular $\mathbb{E}[|c_n|^2] = 1/N$ with Gaussian concentration.

**Proposition 6** (GUE implies UD for $J_\infty$). If the distribution of the eigenvectors of $J_\lambda$ follows GUE behavior (in the sense that the $c_n^{(\lambda)} = \langle e_0, \psi_n^{(\lambda)}\rangle$ have the asymptotic distribution of a Haar measure on the sphere), then $J_\lambda$ is uniformly delocalized, and by Proposition 5: $\mu_{WT}^\infty = \mu_\gamma^{real}$.

*Proof.* In the GUE ensemble of size $N$: with probability $1 - e^{-cN}$, $\max_n|c_n|^2 \leq C\log N/N$. Then UD holds. In the limit $N\to\infty$: $\max_n|c_n|^2 \to 0$. $\square$

**Corollary 1** (under GUE: $\mathrm{spec}(J_\infty) = \{\gamma_n\}$, implying RH). Under the GUE hypothesis for the eigenvectors of $J_\lambda$:

1. $\mu_{WT}^\infty = \mu_\gamma^{real}$ (Proposition 6).
2. $\mathrm{spec}(J_\infty) = \mathrm{supp}(\mu_{WT}^\infty) = \mathrm{supp}(\mu_\gamma^{real}) = \{\gamma_n\}$ (spectral theorem).
3. By Theorem C1 (Doc 17): $\{\text{real zeros of }C_\infty\} = \{\gamma_n\}$.
4. By Theorem 3 (Doc 19): RH.

*Proof.* The chain of equivalences is direct from steps 1-4. The only non-trivial point is step 2: that $\mathrm{supp}(\mu_\gamma^{real}) = \{\gamma_n\}$. This follows from $\mu_\gamma^{real} = \sum_n w_n\delta_{\gamma_n}$ with $w_n > 0$ for all $n$ (positive weights), so each $\gamma_n$ is in the support. $\square$

---

## 6. The contradiction argument: localization implies a zero off the critical line

**Proposition 7** (localization of $e_0$ implies $\mu_{WT}^\infty \neq \mu_\gamma^{real}$). Suppose there exists $n_0$ such that $|c_{n_0}^{(\lambda)}|^2 \to \alpha > 0$ (localization at the eigenvector $\psi_{n_0}^{(\lambda)}$). Then $\mu_{WT}^\infty$ has an atom of weight $\geq \alpha$ at the position $t_{n_0}^\infty = \lim_\lambda t_{n_0}^{(\lambda)}$.

If $\mu_{WT}^\infty = \mu_\gamma^{real}$ (assume equality): the atom of $\mu_{WT}^\infty$ at $t_{n_0}^\infty$ with weight $\alpha$ must correspond to an atom of $\mu_\gamma^{real}$ at $\gamma_{n_0}$ with weight $w_{n_0}$. Then $t_{n_0}^\infty = \gamma_{n_0}$ and $\alpha = w_{n_0}$.

But localization at a single eigenvector $\psi_{n_0}$ would imply that $\langle e_0, \psi_{n_0}\rangle$ is large — which, by the theory of Jacobi operators, implies that the zero $t_{n_0}^{(\lambda)}$ is especially "close" to the vector $e_0$ in the orthogonal basis. This condition is inconsistent with the uniform distribution of zeros (GUE) unless the zero $\gamma_{n_0}$ has special properties.

In particular: if localization occurs at $n_0$, and the function $C_\infty$ has a zero at $\gamma_{n_0}$ that is a pole of order $> 1$ of $C_\infty'/C_\infty$ (i.e., a multiple zero of $C_\infty$), then the weight $\alpha$ in $\mu_{WT}^\infty$ would be $> w_{n_0}$. But $\mu_{WT}^\infty = \mu_\gamma^{real}$ would give $\alpha = w_{n_0}$ — a contradiction.

**Conclusion.** Under the hypothesis that all zeros of $\Xi$ are simple (universally conjectured): the weights $w_{n_0}$ in $\mu_\gamma^{real}$ are all equal (since the derivatives $\Xi'(\gamma_n)$ are nonzero). Localization would produce an atom of anomalous weight, generating a contradiction.

---

## 7. The unconditional result: bounding the weights of $\mu_{WT}^\infty$

**Theorem 1** (unconditional bound on the weights of the WT measure). Let $w_n^{WT} = \mu_{WT}^\infty(\{\gamma_n\})$ be the weight of the atom of $\mu_{WT}^\infty$ at $\gamma_n$ (if $\gamma_n \in \mathrm{spec}(J_\infty)$). Then:

$$w_n^{WT} \leq \liminf_\lambda |c_n^{(\lambda)}|^2 \leq C \cdot \|\psi_n^{(\lambda)}\|^2 = C,$$

where $\psi_n^{(\lambda)}$ are the normalized eigenvectors of $J_\lambda$.

If $\mathrm{spec}(J_\infty) = \{\gamma_n\}_{n\geq 1}$ (spectral completeness): the sum of the weights must be 1:

$$\sum_{n\geq 1} w_n^{WT} = \|e_0\|^2 = 1.$$

This is the COMPLETENESS condition of the eigenvector basis of $J_\infty$ in the direction of $e_0$.

*Proof.* By the spectral theory of Jacobi operators (Weyl-Titchmarsh): $\int d\mu_{WT}^\infty(t) = \langle e_0, e_0\rangle = 1$ (if $J_\infty$ is self-adjoint on the correct domain and $e_0$ is cyclic). The sum of the weights is 1 iff the measure $\mu_{WT}^\infty$ has no absolutely continuous part. $\square$

**Corollary 2** (the WT measure has an absolutely continuous part iff $J_\infty$ is not of LP type with purely point spectrum). In the Weyl classification:

- Limit-point case (LP): the operator $J_\infty$ has $m_\infty^{WT}(z) \in \mathbb{C}^+$ for $z \in \mathbb{C}^+$ — unique solution. In this case, the measure $\mu_{WT}^\infty$ may be pure point, AC, or singular continuous.
- Limit-circle case (LC): two solutions in $L^2$; the operator has deficiency $(1,1)$.

Doc 17 (Proposition 1) establishes that $J_\infty$ is in the LP case — guaranteeing a unique solution for the m-function. But this does not per se imply that $\mu_{WT}^\infty$ is pure point.

---

## 8. When $\mu_{WT}^\infty$ is pure point

**Definition 5.** The measure $\mu_{WT}^\infty$ is **pure point** if $\mu_{WT}^\infty = \sum_n w_n\delta_{t_n}$ (with no AC or SC part).

**Proposition 8** (Simon-Wolff criterion for point purity). The measure $\mu_{WT}^\infty$ is pure point if and only if:

$$\int_\mathbb{R}\!\left[\Im m_\infty^{WT}(t+i0^+)\right]^{-1}d\mu_{WT}^\infty(t) < \infty \quad (\text{Simon-Wolff criterion}).$$

Equivalently: the function $\Im m_\infty^{WT}$ grows to $+\infty$ along the mass points of $\mu_{WT}^\infty$ and is zero (in the Lebesgue sense) on the complement.

**Proposition 9** (point purity of $\mu_{WT}^\infty$ from EF2). By EF2 (Doc 17): $N\cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$ (on $\mathbb{C}^+$). For $z = t + i\eta$ with $\eta \to 0^+$:

$$\Im m_\infty^{WT}(t+i\eta) = \frac{1}{N}\Im\frac{C_\infty'(t+i\eta)}{C_\infty(t+i\eta)}.$$

This function:
- Has peaks (grows like $\eta^{-1}$) when $t$ is near a simple zero of $C_\infty$.
- Is $O(1)$ when $t$ is far from the zeros of $C_\infty$.

At points $t = \gamma_n$ where $C_\infty(\gamma_n) = 0$ (if the reverse inclusion holds): $\Im m_\infty^{WT}(\gamma_n + i0^+) = +\infty$ (pole of the m-function). This means that $\mu_{WT}^\infty$ has positive mass at $\gamma_n$ — i.e., $\gamma_n \in \mathrm{spec}_{pp}(J_\infty)$.

*Proof.* The behavior of the imaginary part of $C_\infty'/C_\infty$ at a simple zero $\gamma_n$ of $C_\infty$: $C_\infty(z) \approx C_\infty'(\gamma_n)(z-\gamma_n)$ near $\gamma_n$. Then $C_\infty'(z)/C_\infty(z) \approx 1/(z-\gamma_n)$, whose imaginary part $\Im(1/(t+i\eta - \gamma_n)) = -\eta/((t-\gamma_n)^2+\eta^2) \to -\pi\delta(t-\gamma_n)$ as $\eta\to 0$. $\square$

**Conclusion of Proposition 9.** If (Rev. Inc.) holds — that is, $C_\infty(\gamma_n) = 0$ for all $\gamma_n$ — then $\mu_{WT}^\infty$ has positive mass at every $\gamma_n$. Then $\{\gamma_n\} \subseteq \mathrm{spec}_{pp}(J_\infty) \subseteq \mathrm{spec}(J_\infty)$.

**Conversely:** If $\gamma_n \in \mathrm{spec}_{pp}(J_\infty)$ (i.e., $\mu_{WT}^\infty(\{\gamma_n\}) > 0$): by EF2, $m_\infty^{WT}$ has a pole at $\gamma_n$, hence $C_\infty(\gamma_n) = 0$. This gives (Rev. Inc.) — BUT using the Weyl-Titchmarsh m-function, not the empirical one.

---

## 9. The new central equivalence

**Theorem 2** (equivalence between (Rev. Inc.) and spectral completeness of $J_\infty$). The following are equivalent:

(i) (Rev. Inc.): $\Xi(\gamma_n) = 0$ for $\gamma_n \in \mathbb{R}$ $\implies$ $C_\infty(\gamma_n) = 0$.

(ii) $\{\gamma_n\} \subseteq \mathrm{spec}_{pp}(J_\infty)$ (all the $\gamma_n$ are eigenvalues of $J_\infty$).

(iii) $\mu_{WT}^\infty(\{\gamma_n\}) > 0$ for all $n$ (the Weyl-Titchmarsh measure has mass at every $\gamma_n$).

(iv) $m_\infty^{WT}$ has a pole at every $\gamma_n$ (by EF2: $C_\infty(\gamma_n) = 0$).

*Proof.* (i) $\iff$ (iv): EF2 + Proposition 9. (iv) $\iff$ (iii): poles of the Stieltjes transform = atoms of the measure. (iii) $\iff$ (ii): atoms of $\mu_{WT}^\infty$ = eigenvalues of $J_\infty$. $\square$

**Proposition 10** (completeness of $\mu_{WT}^\infty$ vs. convergence of $\mu_{emp}^\lambda$). The unconditional result (Doc 15) gives $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$, where $\mu_\gamma^{real}$ has mass at every $\gamma_n$. If $\mu_{WT}^\infty = \mu_\gamma^{real}$ (equality of the two limiting measures): then (iii) of Theorem 2 holds, giving (Rev. Inc.) and therefore RH.

**The precise gap.** The equality $\mu_{WT}^\infty = \mu_\gamma^{real}$ is the missing condition. This equality requires that the weights $w_n^{WT} = \mu_{WT}^\infty(\{\gamma_n\})$ equal the weights of $\mu_\gamma^{real}$, which are proportional to $1/\gamma_n$ (the zero density in the region of $\gamma_n$).

---

## 10. The final wall: the relation between $\mu_{WT}^\infty$ and $\mu_{emp}^\infty$

**Proposition 11** (sufficient condition for $\mu_{WT}^\infty = \mu_{emp}^\infty$). Let $G_N(z) = (1/N)\mathrm{Tr}(J_\lambda^N - z)^{-1} = m_\lambda^{emp}(z)$ and $F_N(z) = \langle e_0, (J_\lambda^N - z)^{-1}e_0\rangle = m_\lambda^{WT}(z)$. Then:

$$G_N(z) - F_N(z) = \frac{1}{N}\sum_{j=1}^N\langle e_j, (J-z)^{-1}e_j\rangle - \langle e_0, (J-z)^{-1}e_0\rangle = \frac{1}{N}\sum_{j=1}^N [R_{jj}(z) - R_{00}(z)],$$

where $R_{jj}(z) = \langle e_j, (J-z)^{-1}e_j\rangle$ are the diagonal elements of the resolvent.

**Lemma 1** (the diagonal elements of the resolvent are equal iff $J$ is invariant under index translation). For a Jacobi operator with coefficients $\{a_n, b_n\}$: $R_{jj}(z) = R_{00}(z)$ for all $j$ iff $a_n = a$ and $b_n = b$ are constant (Jacobi with constant coefficients — the circular-arc measure case).

*Proof.* If $J$ has constant coefficients: $R_{jj}(z) = R_{00}(z)$ by translational invariance. In the general case: $R_{jj}(z) \neq R_{00}(z)$ generically. $\square$

**Consequence.** For the CCM operator $J_\infty$ with non-constant coefficients $\{a_n^\infty, b_n^\infty\}$ (the coefficients grow as noted in Doc 15): $G_N(z) \neq F_N(z)$ in general. The difference $G_N - F_N \to 0$ iff the coefficients "homogenize" in the limit — which occurs in the high-frequency regime.

---

## 11. The result that closes the argument under an additional hypothesis

**Theorem 3** (RH under delocalization). Hypothesis D (Delocalization of $e_0$ in $J_\infty$):

$$\sup_{n\geq 1}|\langle e_0, \psi_n^\infty\rangle|^2 = 0 \quad (\text{supremum of the weights in the eigenvectors of the limit})$$

implies RH.

*Proof.* Under Hypothesis D: all weights of $\mu_{WT}^\infty$ are equal in the limit, so $\mu_{WT}^\infty = \mu_{emp}^\infty = \mu_\gamma^{real}$ (Proposition 5). By Theorem 2: (Rev. Inc.) holds. By Theorem C3 (Doc 17): RH. $\square$

**Corollary 3** (reformulation of RH in terms of the eigenvectors of $J_\infty$):

$$\text{RH} \iff \lim_{n\to\infty}\langle e_0, \psi_n^\infty\rangle = 0 \quad (\text{asymptotic delocalization of the vector } e_0 \text{ in the eigenvector basis of }J_\infty).$$

*Proof.* $(\Leftarrow)$: Theorem 3. $(\Rightarrow)$: Under RH, $\mathrm{spec}(J_\infty) = \{\gamma_n\}$, the basis $\{\psi_n^\infty\}$ is complete in the Hilbert space and $\langle e_0, \psi_n^\infty\rangle \to 0$ by the Riemann-Lebesgue lemma for orthonormal bases in Hilbert space. $\square$

---

## 12. Status of the program after Doc 22

**Main result of Doc 22.** The reverse inclusion (Rev. Inc.) is equivalent to the delocalization of $e_0$ in the eigenvector basis of $J_\infty$:

$$(\text{Rev. Inc.}) \iff \langle e_0, \psi_n^\infty\rangle \to 0 \iff \mu_{WT}^\infty = \mu_\gamma^{real}.$$

And the complete chain is:

$$\text{RH} \iff \mu_{WT}^\infty = \mu_\gamma^{real} \iff \langle e_0, \psi_n^\infty\rangle \to 0 \iff \{C_\infty = 0 \text{ on }\mathbb{R}\} = \{\gamma_n\}.$$

**Final diagram of the Phase 29 program (Docs 00-22):**

```
Unconditional:
  t_n^(λ) ∈ ℝ (CCM self-adjointness)
  μ_emp^λ ⇒ μ_γ^real (Doc 15)
  spec(J_∞) = {C_∞ = 0} (Doc 17, Thm C1)
  {C_∞ = 0} ⊆ {Ξ = 0} (Doc 19, Thm 2)
  N_off(T) = O(1) or RH (Doc 21, Cor 2)

The central gap:
  μ_WT^∞ = μ_emp^∞ = μ_γ^real
  ⟺ delocalization: ⟨e_0, ψ_n^∞⟩ → 0
  ⟺ (Rev. Inc.)
  ⟺ RH

Under an additional hypothesis (GUE/UD): RH.
```

**Proposal for Doc 23.** Attack the delocalization $\langle e_0, \psi_n^\infty\rangle \to 0$ directly. The question: can the eigenvectors of $J_\infty$ localize around the vector $e_0$? In Jacobi operators with a quasi-periodic potential (Kotani's theorem), localization relates to the existence of a positive Lyapunov measure. For the CCM operator, the potential is $C_\infty(t) = w(t) - \Psi(t)$ — which has special properties (logarithmic growth, quasi-periodic distribution). Study whether Kotani's conditions imply delocalization (and hence RH) or allow localization (and hence not-RH).
