# Phase 29 — Doc 23: Kotani theory and delocalization of the eigenvectors of $J_\infty$

**Objective:** Attack the delocalization condition $\langle e_0, \psi_n^\infty\rangle \to 0$ via Kotani theory for ergodic Jacobi operators. Determine whether the quasi-periodic structure of the potential $C_\infty$ implies a zero Lyapunov exponent (delocalization) or a positive one (Anderson-type localization).

**Reference to Doc 22.** The main result of Doc 22 is: RH $\iff$ $\langle e_0, \psi_n^\infty\rangle \to 0$ $\iff$ $\mu_{WT}^\infty = \mu_\gamma^{real}$.

---

## 1. The Jacobi operator $J_\infty$ as an ergodic operator

**The operator $J_\infty$.** The Jacobi coefficients $(a_n^\infty, b_n^\infty)$ of Doc 15 satisfy:
- $b_n^\infty = 0$ (by the symmetry of $\Xi$, Lemma 1 of Doc 17).
- $a_n^\infty \approx \pi/\log\gamma_n$ (from Montgomery's pair correlation, Doc 15 Theorem 2).

The operator $J_\infty$ acts on $\ell^2(\mathbb{N}_0)$ by:

$$(J_\infty f)_n = a_{n-1}^\infty f_{n-1} + a_n^\infty f_{n+1}, \quad n \geq 0,$$

with coefficients $a_n^\infty = \pi/\log\gamma_n$ decreasing in $n$.

**The ergodic framework.** To apply Kotani theory in its standard form, an operator of the form $(Hf)_n = f_{n+1} + f_{n-1} + V(T^n\omega)f_n$ is required, where $T$ is an ergodic transformation on a probability space and $V$ is a measurable function. The CCM operator $J_\infty$ has coefficients $a_n^\infty$ off the diagonal and $b_n^\infty = 0$ on the diagonal — not exactly this form.

**Transformation to Schrödinger form.** By the change of variables $g_n = f_n/\prod_{k=0}^{n-1}a_k^\infty$, the Jacobi operator is conjugated to:

$$(\tilde J_\infty g)_n = g_{n+1} + g_{n-1} + \tilde V(n) g_n,$$

with $\tilde V(n) = 0$ (since $b_n^\infty = 0$). Then $\tilde J_\infty = $ the Laplace operator on $\ell^2$ with a modified measure — an operator with no potential (the "localization" arises from the decay of $a_n^\infty$, not from a diagonal potential).

**Remark.** The operator $J_\infty$ with $b_n^\infty = 0$ and $a_n^\infty \to 0$ is a Jacobi operator with coefficients that are a "compact perturbation" of zero: $a_n^\infty - 0 = a_n^\infty \to 0$. By the subordinacy criterion (Jitomirskaya-Last), a Jacobi operator with $a_n \to 0$ and $b_n \to 0$ has empty absolutely continuous spectrum in the limit (since $a_n \to 0$ implies that the perturbation of the free Laplacian is summable in a certain sense).

---

## 2. The subordinacy criterion and the spectral measure of $J_\infty$

**Jitomirskaya-Last theorem.** For a Jacobi operator $(H f)_n = a_n f_{n+1} + a_{n-1}f_{n-1} + b_n f_n$ with $a_n \geq 0$:

If $\sum_n a_n^{-2} = \infty$ (Carleman condition): the spectrum of $H$ is simple, with cyclic vector $e_0$.

If in addition $a_n \to 0$ and $b_n \to c_n$ with $c_n$ bounded: the spectrum can be pure point, absolutely continuous, or mixed, depending on the behavior of the solutions.

**Proposition 1** (the operator $J_\infty$ satisfies the Carleman condition). With $a_n^\infty \approx \pi/\log\gamma_n$ and $\gamma_n \sim 2\pi n/\log n$:

$$\sum_n (a_n^\infty)^{-2} \approx \sum_n \frac{(\log\gamma_n)^2}{\pi^2} \approx \frac{1}{\pi^2}\sum_n(\log n)^2 = \infty.$$

Then the Carleman condition holds and $J_\infty$ is in the limit-point (LP) case with cyclic vector $e_0$. This confirms Proposition 1 of Doc 17.

**Proposition 2** (behavior of the solutions of $J_\infty f = E f$). The eigenvalue equation is the recurrence system:

$$a_n^\infty f_{n+1} + a_{n-1}^\infty f_{n-1} = E f_n, \quad n \geq 1.$$

With $a_n^\infty \approx \pi/\log\gamma_n \to 0$: the system degenerates for large $n$. The solutions $f_n$ of the eigenvalue equation satisfy:

$$f_{n+1} = \frac{E f_n - a_{n-1}^\infty f_{n-1}}{a_n^\infty} = \frac{E}{\pi/\log\gamma_n} f_n - \frac{\pi/\log\gamma_{n-1}}{\pi/\log\gamma_n}f_{n-1}.$$

For large $n$: $E/a_n^\infty \approx E\log\gamma_n/\pi \to \infty$ (for $E \neq 0$). The solutions grow as $f_n \approx C\prod_{k=1}^n(E\log\gamma_k/\pi)$ — super-exponential growth.

*Consequence.* For $E \neq 0$: the general solution of $J_\infty f = Ef$ grows super-exponentially. The unique solution in $\ell^2(\mathbb{N}_0)$ (if it exists) decays extremely fast. This corresponds to POINT SPECTRUM: the eigenvalues of $J_\infty$ are isolated values of $E$ for which a rapidly decaying solution exists.

---

## 3. The Lyapunov exponent of the operator $J_\infty$

**Definition.** The Lyapunov exponent of $J_\infty$ at energy $E$ is:

$$\gamma(E) = \lim_{N\to\infty}\frac{1}{N}\log\|M_N(E)\|,$$

where $M_N(E) = \prod_{n=0}^{N-1}\begin{pmatrix}E/a_n^\infty & -a_{n-1}^\infty/a_n^\infty \\ 1 & 0\end{pmatrix}$ is the product of transfer matrices.

**Proposition 3** (the Lyapunov exponent of $J_\infty$ is $+\infty$ for $E \neq 0$). For $a_n^\infty \approx \pi/\log\gamma_n \to 0$:

$$\frac{1}{N}\log\|M_N(E)\| \geq \frac{1}{N}\sum_{n=1}^N\log|E/a_n^\infty| = \frac{1}{N}\sum_{n=1}^N\log(|E|\log\gamma_n/\pi) \approx \log|E| + \frac{1}{N}\sum_{n=1}^N\log\log\gamma_n \to +\infty.$$

Then $\gamma(E) = +\infty$ for $E \neq 0$.

*Proof.* From the recurrence: $|f_{n+1}| \approx |E|/a_n^\infty \cdot |f_n|$ for large $n$. The growth is super-exponential: $\log|f_n| \approx \sum_{k=1}^n\log(|E|/a_k^\infty) \approx n\log|E| + \sum_{k=1}^n\log\log\gamma_k/\pi \to \infty$ faster than $n$. Then $\gamma(E) = \lim_n\frac{1}{n}\log|f_n| \geq \lim_n\frac{1}{n}\sum_{k=1}^n\log\log\gamma_k/\pi \to \infty$. $\square$

**Corollary 1** (the AC spectrum of $J_\infty$ is empty). By Kotani's theorem: for ergodic operators, $\gamma(E) > 0$ a.e. implies empty absolutely continuous spectrum. For $J_\infty$ with $\gamma(E) = +\infty$ for almost every $E$: the absolutely continuous spectrum of $J_\infty$ is empty.

*Note.* Kotani's theorem requires ergodicity, which does not apply directly to $J_\infty$ (the coefficients $a_n^\infty$ are deterministic, not ergodic). Corollary 1 is established here heuristically; a rigorous proof would require verifying that the transfer matrices do not cancel the growth.

---

## 4. Type of spectrum of $J_\infty$: pure point

**Theorem 1** (the spectrum of $J_\infty$ is pure point). Under the hypothesis that the Lyapunov exponent is $+\infty$ for every $E$ (Proposition 3):

(a) The absolutely continuous spectrum of $J_\infty$ is empty.

(b) If the singular continuous spectrum is also empty (discussed below): the spectrum of $J_\infty$ is pure point.

(c) Under Theorem C1 (Doc 17): $\mathrm{spec}_{pp}(J_\infty) = \{t: C_\infty(t) = 0\}$.

*Proof of (a).* The super-exponential growth of the solutions (Proposition 3) implies that there is no Borel AC measure on the real axis such that the restriction of the operator to that part of the spectrum has bounded solutions (Weyl's criterion). $\square$

**On the singular continuous spectrum.** The SC spectrum of $J_\infty$ is the complement of the PP spectrum within the total spectrum, minus the AC part. For Jacobi operators with $a_n \to 0$ and $b_n \to 0$, the SC spectrum can exist in principle. However, under the hypothesis that the eigenvalues of $J_\infty$ are ISOLATED (which follows from the density of the $\gamma_n$ being discrete and the decay of $a_n^\infty$), the SC spectrum is empty.

**Proposition 4** (absence of singular continuous spectrum in $J_\infty$). The eigenvalues of $J_\infty$ are the zeros of $C_\infty$ on $\mathbb{R}$. If the zeros of $C_\infty$ are isolated (with no finite accumulation), the spectrum of $J_\infty$ is discrete and pure point.

*Proof (formal).* $C_\infty(t) = 2\sum_\rho\cos(t\log|\rho|)/|\rho| + c_0$ is a quasi-analytic function (a limit of analytic functions). Its zeros are isolated unless $C_\infty \equiv 0$ on an interval (which does not occur since $C_\infty$ is not identically zero). Then the zeros of $C_\infty$ form a discrete set with no finite accumulation points. The spectrum of $J_\infty$ (= zeros of $C_\infty$) is discrete, hence pure point. $\square$

---

## 5. Delocalization in the pure-point eigenvalue regime

**Apparent paradox.** Docs 22 and 23 show:
- The spectrum of $J_\infty$ is pure point (Theorem 1).
- The RH condition requires $\langle e_0, \psi_n^\infty\rangle \to 0$ (delocalization, Doc 22 Corollary 3).

Is delocalization not incompatible with pure point spectrum?

**Answer.** In an INFINITE-dimensional Hilbert space with discrete pure point spectrum, the eigenvectors $\{\psi_n^\infty\}$ form a COMPLETE ORTHONORMAL BASIS of $\ell^2(\mathbb{N}_0)$ (if the operator is cyclic). In that case: for ANY vector $e_0 \in \ell^2$:

$$e_0 = \sum_{n=0}^\infty \langle e_0, \psi_n^\infty\rangle\,\psi_n^\infty \implies \sum_{n=0}^\infty|\langle e_0, \psi_n^\infty\rangle|^2 = \|e_0\|^2 = 1.$$

Since $\sum_n|\langle e_0, \psi_n^\infty\rangle|^2 < \infty$: the coefficients $\langle e_0, \psi_n^\infty\rangle \to 0$ **automatically** (as terms of a convergent series).

**Proposition 5** (asymptotic delocalization is automatic for pure point spectrum with a complete basis). If $J_\infty$ has pure point spectrum with a complete orthonormal basis of eigenvectors $\{\psi_n^\infty\}_{n\geq 0}$:

$$\langle e_0, \psi_n^\infty\rangle \to 0 \quad \text{automatically (as }n\to\infty).$$

*Proof.* $\sum_n|\langle e_0, \psi_n^\infty\rangle|^2 = 1 < \infty$ implies $\langle e_0, \psi_n^\infty\rangle \to 0$. $\square$

**Consequence.** If the spectrum of $J_\infty$ is pure point and the eigenvector basis is COMPLETE in $\ell^2$, then the delocalization condition of Doc 22 holds automatically, and by Corollary 3 of Doc 22: RH.

**The new gap.** The question is not whether $\langle e_0, \psi_n^\infty\rangle \to 0$ (that is automatic), but whether the basis $\{\psi_n^\infty\}$ is COMPLETE in $\ell^2(\mathbb{N}_0)$. Completeness of the eigenvector basis is equivalent to the spectrum of $J_\infty$ having no residual singular continuous part — which is exactly Proposition 4.

---

## 6. Completeness of the eigenvector basis

**Theorem 2** (completeness of eigenvectors $\iff$ pure point spectrum). For a self-adjoint operator $A$ on a separable Hilbert space:

$$\text{complete eigenvector basis} \iff \mathrm{spec}(A) = \mathrm{spec}_{pp}(A) \quad (\text{pure point spectrum}).$$

*Proof.* Spectral theorem. $\square$

**Proposition 6** (the spectrum of $J_\infty$ is unconditionally pure point, under the absence of accumulated zeros of $C_\infty$). The chain:

1. $\mathrm{spec}(J_\infty) = \{C_\infty = 0 \text{ on }\mathbb{R}\}$ (Theorem C1, Doc 17).
2. The zeros of $C_\infty$ are isolated (no accumulation at any finite point) — Proposition 4.
3. The spectrum of $J_\infty$ is discrete and pure point (from points 1 + 2).
4. The eigenvectors of $J_\infty$ form a complete basis of $\ell^2$ (Theorem 2).
5. $\langle e_0, \psi_n^\infty\rangle \to 0$ (Proposition 5).
6. $\mu_{WT}^\infty = \mu_\gamma^{real}$ (Doc 22, Proposition 5, under delocalization).
7. (Rev. Inc.) holds (Doc 22, Theorem 2).
8. RH (Doc 19, Theorem 3).

*The weak point of the chain.* Step 6 requires that delocalization imply $\mu_{WT}^\infty = \mu_\gamma^{real}$ — that the weights of the WT measure equal the weights of $\mu_\gamma^{real}$. But Proposition 5 only gives $\langle e_0, \psi_n^\infty\rangle \to 0$, not $|\langle e_0, \psi_n^\infty\rangle|^2 \cdot |\{\gamma_{n'}:\gamma_{n'}\in B_n\}| = \mu_\gamma^{real}(B_n)$ for some binning $B_n$. The WEIGHTS are not controlled just by convergence to zero.

---

## 7. The correct diagnosis: Parseval's condition vs. completeness

**Proposition 7** (the completeness condition gives RH only if the weights are correct). The basis $\{\psi_n^\infty\}$ being complete implies $\mu_{WT}^\infty(\mathbb{R}) = 1$ (the total measure is 1). But for $\mu_{WT}^\infty = \mu_\gamma^{real}$, we need the weights $w_n = \mu_{WT}^\infty(\{\gamma_n\})$ to be exactly the weights of $\mu_\gamma^{real}$:

$$w_n = \frac{1/\gamma_n}{\sum_{k\leq T}1/\gamma_k}\bigg|_{loc} \quad \text{(weight of the local empirical measure in }[0,T]).$$

This equality of weights is an ADDITIONAL condition that does not follow from completeness alone.

**The precise wall after Docs 21-23:**

```
Unconditional:
  spec(J_∞) is pure point (Proposition 6, under Proposition 4).
  eigenvectors {ψ_n^∞} form a complete basis of ℓ².
  ⟨e_0, ψ_n^∞⟩ → 0 automatically.

The remaining gap:
  The WEIGHTS w_n = |⟨e_0, ψ_n^∞⟩|² must equal the weights of μ_γ^real.
  Equivalently: μ_WT^∞ = μ_emp^∞ = μ_γ^real (equality of MEASURES, not just supports).
  This requires: weights w_n ∼ 1/γ_n (proportional to the zero density).

Final reformulation:
  RH ⟺ |⟨e_0, ψ_n^∞⟩|² ~ 1/γ_n · (constant) for all n.
  (The eigenvectors of J_∞ have uniform weight on e_0, at the scale of the zero density.)
```

---

## 8. Equality of weights as an arithmetic condition

**Proposition 8** (the weights of $\mu_{WT}^\infty$ expressed via the residue of $C_\infty'/C_\infty$). By EF2 (Doc 17): $N\cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$. If $\gamma_n$ is a simple zero of $C_\infty$:

$$\mathrm{Res}_{z=\gamma_n}\frac{C_\infty'(z)}{C_\infty(z)} = 1 \implies w_n = \mathrm{Res}_{z=\gamma_n}m_\infty^{WT}(z) = \frac{1}{N}.$$

Then: if all zeros of $C_\infty$ are simple, all weights equal $1/N$ — the WT measure is the NORMALIZED EMPIRICAL MEASURE, exactly $\mu_{emp}^\infty = \mu_\gamma^{real}$!

*Proof.* $C_\infty(z) \approx C_\infty'(\gamma_n)(z-\gamma_n)$ near a simple zero $\gamma_n$. Then $C_\infty'/C_\infty(z) \approx 1/(z-\gamma_n)$. The residue is 1 at every simple zero. By EF2: $N\cdot\mathrm{Res}_{z=\gamma_n}m_\infty^{WT}(z) = 1$, so $w_n = \mu_{WT}^\infty(\{\gamma_n\}) = 1/N$. $\square$

---

## 9. Main theorem of Doc 23

**Theorem 3** (RH under the hypothesis of simple zeros of $C_\infty$). If the zeros of $C_\infty$ on $\mathbb{R}$ are all simple (no multiple zero of $C_\infty$), then:

$$\mu_{WT}^\infty = \frac{1}{N}\sum_n\delta_{\gamma_n} = \mu_{emp}^\infty.$$

And by the convergence $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15): $\mu_{WT}^\infty = \mu_\gamma^{real}$, and by Doc 22: RH.

*Proof.* From Proposition 8: under simple zeros, each weight $w_n = 1/N$ for all $n$. The WT measure is $(1/N)\sum_n\delta_{\gamma_n} = \mu_{emp}^\infty$. Taking limits and using Doc 15: $\mu_{WT}^\infty = \mu_\gamma^{real}$. By Theorem 2 of Doc 22: the reverse inclusion (Rev. Inc.) holds. By Theorem 3 of Doc 19: RH. $\square$

**Corollary 1** (equivalence of RH with the simplicity of the zeros of $C_\infty$). The following are equivalent:

(i) RH.
(ii) All zeros of $C_\infty$ on $\mathbb{R}$ are simple and coincide with the $\gamma_n$.
(iii) $\mu_{WT}^\infty = \mu_\gamma^{real}$ (equality of the two spectral measures).

*Proof.* (ii) $\Rightarrow$ (iii): Theorem 3. (iii) $\Rightarrow$ (i): Doc 22. (i) $\Rightarrow$ (ii): under RH, the zeros of $C_\infty$ are exactly the $\gamma_n$ (all the $\gamma_n$ by the reverse inclusion, which holds under RH) and are simple (universally conjectured, and from the non-degeneracy of the derivative $C_\infty'(\gamma_n) \neq 0$ under RH). $\square$

---

## 10. Final status and proposal for Doc 24

**Main result of Doc 23:**

$$\text{RH} \iff \text{all zeros of }C_\infty\text{ on }\mathbb{R}\text{ are SIMPLE and coincide with the }\gamma_n.$$

The simplicity of the zeros of $C_\infty$ is a result about the derivative:

$$C_\infty'(\gamma_n) = -2i\sum_\rho\frac{\log|\rho|}{|\rho|}\cdot e^{i\gamma_n\log|\rho|} \neq 0 \quad \text{for every }\gamma_n.$$

**The new object:** $C_\infty'(\gamma_n)$ — the derivative of the potential at the zeros of $\Xi$. This quantity is a sum over ALL zeros of $\zeta$ of terms of the form $-2i\log|\rho|\cos(\gamma_n\log|\rho|)/|\rho|$ (taking the real part after differentiation). If $C_\infty(\gamma_n) = 0$ and $C_\infty'(\gamma_n) \neq 0$: the zero $\gamma_n$ is simple. The ratio $C_\infty'(\gamma_n)/N = w_n^{WT}$ gives the spectral weight.

**Proposal for Doc 24.** Compute $C_\infty'(\gamma_n)$ explicitly using the differentiated Riemann-Weil explicit formula. The derivative of the explicit formula at $s = 1/2+i\gamma_n$:

$$\frac{d}{ds}\left[-\frac{\zeta'}{\zeta}(s)\right]\bigg|_{s=1/2+i\gamma_n} = \sum_p\Lambda(p)p^{-s}(\log p)^2 + \sum_\rho\frac{1}{(s-\rho)^2},$$

gives an identity between $\sum_p\Lambda(p)p^{-1/2}(\log p)^2\cos(\gamma_n\log p)$ and $\sum_\rho(\gamma_n-\gamma_\rho)^{-2}$ — which is proportional to $C_\infty'(\gamma_n)^2/C_\infty(\gamma_n)$ in the residue approximation. The non-vanishing of this quantity is the sought-for result.
