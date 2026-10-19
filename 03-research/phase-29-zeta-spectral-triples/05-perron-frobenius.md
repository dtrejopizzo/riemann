# Phase 29 — Perron-Frobenius structure and arithmetic orthogonality

**Goal:** Exploit the non-negativity $k_\lambda \geq 0$ (doc 04) to:
(A) prove that the minimizer $\xi_\lambda$ is positive (Perron-Frobenius),
(B) show that the arithmetic perturbation $A_\lambda k_\lambda$ is nearly proportional to $k_\lambda$ (arithmetic orthogonality),
(C) attack Wall-H2 from this angle without using standard perturbation theory.

---

## 1. The Perron-Frobenius program: motivation

Theorem 0 of doc 04 establishes $k_\lambda > 0$ on all of $[\lambda^{-1},\lambda]$. Theorem 1 of doc 01 establishes simple-even (H1) for large $\lambda$. But the inference

$$k_\lambda > 0 \implies \xi_\lambda > 0$$

(the minimizer is also positive) is not proved. If this inference holds, the situation changes radically:

- $\xi_\lambda > 0$ implies $I_p(\xi_\lambda) = p^{-1/2}\int \xi_\lambda(u)\xi_\lambda(pu)\,d^*u + \ldots \geq 0$ for every prime $p$.
- This gives direct access to bounds on the coefficients $\xi_n^{(\lambda)}$ of the minimizer without going through the spectral gap.
- In particular, $\hat\xi_\lambda(z) = \int \xi_\lambda(u)\,u^{-iz}\,d^*u$ satisfies improved Hadamard-type properties.

**The plan:** prove $\xi_\lambda > 0$ by a Perron-Frobenius argument using the structure of the operator $QW_\lambda|_{E^+}$ and the positivity of $k_\lambda$.

---

## 2. The cone structure of the arithmetic operator

**Definition.** The cone of non-negative functions in $E_N^+ = \mathrm{span}\{U_n^+: 0\leq n\leq N\}$:
$$\mathcal{C}_N^+ := \{f \in E_N^+ : f(u) \geq 0 \text{ for every } u \in [\lambda^{-1},\lambda]\}.$$

**Proposition 1** (the arithmetic operator preserves the cone). For every prime $p \leq \lambda^2$ and every $f \in \mathcal{C}_N^+$:
$$T(p)f \in \mathcal{C}_N^+.$$

*Proof.* By definition, $(T(p)f)(u) = p^{-1/2}[f(pu) + f(u/p)]$ for $u \in [\lambda^{-1},\lambda]$ (with the convention $f(v) = 0$ for $v \notin [\lambda^{-1},\lambda]$). Since $f \geq 0$, each term $f(pu) \geq 0$ and $f(u/p) \geq 0$. Hence $T(p)f \geq 0$. $\square$

**Corollary** (the operator $A_\lambda$ preserves the cone). Since $A_\lambda f = \sum_{p \leq \lambda^2} \Lambda(p)\,T(p)f$ with $\Lambda(p) = \log p > 0$:
$$f \in \mathcal{C}_N^+ \implies A_\lambda f \in \mathcal{C}_N^+.$$

**Crucial remark.** This means that the operator $A_\lambda$ (the "arithmetic push") amplifies the positive cone rather than destroying it. The interaction between $A_\lambda$ and positivity is structurally benign.

---

## 3. The archimedean operator and the cone

The archimedean operator $B_\lambda := Q^{\mathrm{arch}} + Q^{\mathrm{cross}}|_{E_N^+}$ does not preserve the cone in general (because $Q^{\mathrm{arch}}$ involves the Fourier transform, which does not preserve positivity). But we can identify its structure.

**Proposition 2** (non-negativity of the arithmetic correlation term). For $f \in \mathcal{C}_N^+$ and $g \in \mathcal{C}_N^+$:
$$\langle f, A_\lambda g\rangle_{H_\lambda} \geq 0.$$

*Proof.* $\langle f, A_\lambda g\rangle = \sum_p \Lambda(p)\,\langle f, T(p)g\rangle$. Since $f \geq 0$ and $T(p)g \geq 0$ (Proposition 1), the integrand is non-negative. $\square$

**Interpretation:** In the quadratic form $QW_\lambda(f,f) = B_\lambda(f,f) - A_\lambda(f,f)$, the arithmetic term $A_\lambda(f,f) = \langle f, A_\lambda f\rangle \geq 0$ for $f \geq 0$. Hence, minimizing $QW_\lambda$ over the cone $\mathcal{C}_N^+$ is dominated by: maximizing $A_\lambda(f,f)$ subject to minimizing $B_\lambda(f,f)$.

---

## 4. The node argument: why the minimizer is positive

We seek to prove that the minimizer $\xi_\lambda$ of $QW_\lambda|_{E_N^+}$ over $\{\|f\| = 1\}$ satisfies $\xi_\lambda \geq 0$.

**Lemma 4** (improvement upon taking absolute value). Let $f \in E_N^+$, $\|f\|_{H_\lambda} = 1$. Then:
$$QW_\lambda(|f|, |f|) \leq QW_\lambda(f, f)$$
if the following two conditions hold:
$$\text{(C1)} \quad Q^{\mathrm{arch}}(|f|) \leq Q^{\mathrm{arch}}(f), \qquad \text{(C2)} \quad A_\lambda(|f|,|f|) \geq A_\lambda(f,f).$$

*Proof.* $QW_\lambda(|f|) = Q^{\mathrm{arch}}(|f|) + Q^{\mathrm{cross}}(|f|) - A_\lambda(|f|)$. For $Q^{\mathrm{cross}}$:
$$Q^{\mathrm{cross}}(|f|) = 2\hat{|f|}(i/2)^2 = 2\!\left(\int_{\lambda^{-1}}^\lambda |f(u)|\,u^{-1/2}\,d^*u\right)^{\!2} \geq 2\!\left(\int_{\lambda^{-1}}^\lambda f(u)\,u^{-1/2}\,d^*u\right)^{\!2} = Q^{\mathrm{cross}}(f).$$
Under (C1) and (C2): $QW_\lambda(|f|) \leq Q^{\mathrm{arch}}(f) + Q^{\mathrm{cross}}(f) - A_\lambda(f,f) = QW_\lambda(f)$. $\square$

**Condition (C2): the arithmetic term.** For $A_\lambda(f) = \sum_p \Lambda(p)\langle f, T(p)f\rangle$:
$$\langle f, T(p)f\rangle = p^{-1/2}\!\int f(u)[f(pu)+f(u/p)]\,d^*u$$

and $\langle |f|, T(p)|f|\rangle = p^{-1/2}\!\int |f(u)|[|f(pu)|+|f(u/p)|]\,d^*u$. Since $f(u)[f(pu)+f(u/p)] \leq |f(u)|[|f(pu)|+|f(u/p)|]$ (pointwise), we get $\langle f, T(p)f\rangle \leq \langle |f|, T(p)|f|\rangle$. Hence (C2) holds **unconditionally** for every $f$. $\square$

**Condition (C1): the archimedean term.** $Q^{\mathrm{arch}}(f) = \int_\mathbb{R} |\hat f(t)|^2 \frac{2\partial_t\theta(t)}{2\pi}\,dt$ where the measure $\mu(dt) = \frac{2\partial_t\theta(t)}{2\pi}dt > 0$ for $t \gg 1$. The question is whether $|\widehat{|f|}(t)| \leq |\hat f(t)|$ for almost every $t$. This is generally FALSE: the Mellin transform of $|f|$ does not dominate that of $f$ in modulus for every $t$ simultaneously.

**Obstacle:** Condition (C1) fails in general because the Mellin transform is not monotone under absolute value. This is the structural wall that prevents the direct proof of the node argument.

**Hypothesis AC** (arithmetic continuity of the cone). For the minimizer $\xi_\lambda$ of $QW_\lambda|_{E_N^+}$: $\xi_\lambda \in \mathcal{C}_N^+$ (the minimizer is non-negative).

This hypothesis does not follow from the classical node argument because of the obstacle in (C1). But there is an alternative route.

---

## 5. Alternative route: Perron-Frobenius via comparison with $k_\lambda$

**Theorem 2** (positivity of the minimizer by comparison). Suppose that:
$$QW_\lambda(k_\lambda, k_\lambda) < QW_\lambda(f, f)$$
for every $f \in E_N^+$ with $\|f\| = 1$ and $f \not\geq 0$. Then $\xi_\lambda > 0$.

*Proof.* The minimizer is unique (by simple-even, H1). If $QW_\lambda(k_\lambda) < QW_\lambda(f)$ for every $f$ that changes sign, the minimum cannot be attained at such an $f$. Hence the minimizer $\xi_\lambda$ satisfies $\xi_\lambda \geq 0$. $\square$

**The problem:** To verify the hypothesis of Theorem 2, we need to compare $QW_\lambda(k_\lambda)$ with $QW_\lambda(f)$ for $f$ with zeros. This requires knowing the value of $QW_\lambda(k_\lambda)$.

**Computation of $QW_\lambda(k_\lambda)$:**
$$QW_\lambda(k_\lambda, k_\lambda) = Q^{\mathrm{arch}}(k_\lambda) + Q^{\mathrm{cross}}(k_\lambda) - \sum_p \Lambda(p)\langle k_\lambda, T(p)k_\lambda\rangle.$$

Using $\hat k_\lambda(z) \approx \Xi(z)$:
$$Q^{\mathrm{arch}}(k_\lambda) \approx \int |\Xi(t)|^2 \frac{2\partial_t\theta}{2\pi}\,dt = \langle \Xi, \Xi\rangle_\theta > 0.$$
$$Q^{\mathrm{cross}}(k_\lambda) = 2\hat k_\lambda(i/2)^2 \approx 2\Xi(i/2)^2 = 2\xi(1)^2 > 0.$$
$$\sum_p \Lambda(p)\langle k_\lambda, T(p)k_\lambda\rangle \approx \sum_p \Lambda(p) p^{-1/2} [\hat k_\lambda(z)\hat k_\lambda(-z) \text{ evaluated at the zeros}] = \sum_{p\leq\lambda^2}\Lambda(p)\,p^{-1/2}\int_{\lambda^{-1}}^{\lambda/p} k(u)k(pu)\,d^*u.$$

The value $QW_\lambda(k_\lambda)$ is the "approximate eigenvalue" $\mu_\lambda$ of the Weil form evaluated at $k_\lambda$. Lemma 7.3 (CCM) implies that $\mu_\lambda \to 0$ as $\lambda \to \infty$ (since $k_\lambda \to k$ in norm and $QW_\infty(k,k)$ is related to the first zero of $\Xi$).

---

## 6. Arithmetic orthogonality: the central computation

We return to the question posed by Advisor 1: is the projection of $A_\lambda k_\lambda$ onto the second eigenvector $\psi_2$ small?

**Setup.** Let $\mu_1 < \mu_2 \leq \mu_3 \leq \ldots$ be the eigenvalues of $QW_\lambda|_{E_N^+}$ with eigenvectors $\xi_\lambda = \psi_1, \psi_2, \ldots$ In the notation of the Euler-Lagrange equation:

$$(B_\lambda - \mu_1)\xi_\lambda = A_\lambda\xi_\lambda$$

The resolvent solution (first order in $A_\lambda$) gives:
$$\xi_\lambda = k_\lambda + \sum_{j \geq 2} \frac{\langle \psi_j, A_\lambda k_\lambda\rangle}{\mu_j^{(B)} - \mu_1^{(B)}} \psi_j + O(\|A_\lambda\|^2)$$

where $\mu_j^{(B)}$ are the eigenvalues of $B_\lambda$ and $\mu_j^{(B)} - \mu_1^{(B)} \approx \delta_\lambda \cdot (j-1)^2 \cdot (\text{factor})$ (gap between eigenvalues of $B_\lambda$, which is the "spectral gap" of the archimedean operator).

**The problem with classical perturbation theory:** The denominator $\mu_2^{(B)} - \mu_1^{(B)} = \delta_\lambda = O(e^{-4\pi\lambda^2})$ is exponentially small, while the numerator $\langle \psi_2, A_\lambda k_\lambda\rangle$ could be $O(\lambda)$ (of the order of the norm of $A_\lambda$). This gives a correction of order $O(\lambda e^{4\pi\lambda^2})$ — the blow-up already identified in doc 02.

**The arithmetic orthogonality hypothesis (AO):**
$$|\langle \psi_2, A_\lambda k_\lambda\rangle| = O\!\left(e^{-\pi\lambda^2}\right).$$

If AO holds, the first-order correction would be $O(e^{-\pi\lambda^2}/e^{-4\pi\lambda^2}) = O(e^{3\pi\lambda^2})$ — still large. Even with orthogonality, the spectral gap dominates.

**A more refined estimate.** What actually matters for Wall-H2 is not $\|\xi_\lambda - k_\lambda\|_{L^2}$ but the projection of $\xi_\lambda - k_\lambda$ onto the "direction of the zeros":

$$\hat\xi_\lambda(z) - c\hat k_\lambda(z) = \int (\xi_\lambda - ck_\lambda)(u)\,u^{-iz}\,d^*u.$$

For $z$ near a zero $\gamma_n$ of $\Xi$: by the Hadamard product identity, $\hat k_\lambda(z)$ has a simple zero at $z \approx \gamma_n$ with residue $w_n = |\Xi'(\gamma_n)|$. If the difference $\xi_\lambda - ck_\lambda$ is "aligned" with the direction of $k_\lambda$ (i.e., if $\xi_\lambda - ck_\lambda = \alpha\psi_2 + \ldots$ with $\hat\psi_2(\gamma_n) \approx 0$), then $\hat\xi_\lambda(\gamma_n) \approx c\hat k_\lambda(\gamma_n) = 0$, which is exactly what we want for Wall-H2.

**Definition.** The spectral orthogonality hypothesis (SO):
$$\hat\psi_2(\gamma_n) = O(w_n e^{-\pi\lambda^2}) \quad \text{for every } n.$$

If SO holds, then even if $\xi_\lambda - k_\lambda$ has large norm (dominated by $\psi_2$), the difference $\hat\xi_\lambda - c\hat k_\lambda$ will have zeros close to those of $\hat k_\lambda$.

---

## 7. Computation of $\langle \psi_2, A_\lambda k_\lambda\rangle$ via the explicit formula

**Proposition 3** (integral representation of the arithmetic inner product). For large $\lambda$, using $k_\lambda \approx k$ and $\psi_2 \approx h_{4,\lambda}$ (the 4th even PSWF):

$$\langle h_{4,\lambda}, A_\lambda k\rangle_{H_\lambda} = \sum_{p \leq \lambda^2} \Lambda(p)\,p^{-1/2}\!\int_{\lambda^{-1}}^\lambda h_{4,\lambda}(u)\,[k(pu)+k(u/p)]\,d^*u.$$

Using the Weil explicit formula on the space $H_\lambda$ (analogous to the one used in doc 01 for the PNT):

$$\sum_{p \leq \lambda^2} \Lambda(p)\,p^{-iz} = -\frac{\zeta'}{\zeta}(1/2+iz) - \text{(contribution from the zeros)} + O(\log\lambda),$$

the above sum can be rewritten (via Parseval on the multiplicative group) as:

$$\langle h_{4,\lambda}, A_\lambda k\rangle = \frac{1}{2\pi}\int_\mathbb{R} \hat h_{4,\lambda}(t)\,\hat k(t)\,\left(\sum_{p\leq\lambda^2}\Lambda(p)p^{-it}\right)\,dt + \ldots$$

$$= \frac{1}{2\pi}\int_\mathbb{R} \hat h_{4,\lambda}(t)\,\Xi(t)\,\Psi_\lambda(t)\,dt$$

where $\Psi_\lambda(t) = \sum_{p\leq\lambda^2} \Lambda(p)\,p^{-it}$ is the Chebyshev function in Fourier form.

**Analysis of the inner product.** To compute $\int \hat h_{4,\lambda}(t) \Xi(t) \Psi_\lambda(t)\,dt$:

- $\hat h_{4,\lambda}(t) \approx \hat\psi_4(t)$ (Fourier transform of the 4th Hermite harmonic): an even function that vanishes with multiplicity at $t=0$ and decays rapidly.
- $\Xi(t)$: even function, positive for small $t$, with zeros at $t = \gamma_n$.
- $\Psi_\lambda(t)$: an "oscillatory" function related to the primes.

**Partial result.** The integral $\int \hat h_{4,\lambda}(t)\Xi(t)\,dt \approx \langle\hat\psi_4, \Xi\rangle_{L^2}$ is an integral of a function with 4 zeros (the 4th Hermite harmonic) against $\Xi$ (even function, positive near the origin). By the orthogonality of Hermite polynomials with respect to the weight $e^{-\pi t^2}$:

$$\int_\mathbb{R} H_4(t)\,\Xi(t)\,e^{-\pi t^2}\,dt = \int H_4(t)\,\Xi(t)\,e^{-\pi t^2}\,dt,$$

which would vanish if $\Xi$ were in the space of polynomials of degree $< 4$ — but $\Xi$ is NOT a polynomial, so the integral is generally NOT zero. However, its size depends on the moments of $\Xi$.

**Moments of $\Xi$ via zeros.** If the zeros of $\Xi$ are $\pm\gamma_n$ (RH: $\gamma_n$ real), then:
$$\int t^{2k} \Xi(t)\,e^{-\pi t^2}\,dt = \frac{d^{2k}}{dz^{2k}}\left[\Xi(z)\,e^{-\pi z^2}\right]_{z=0} \cdot (\text{Gamma factor}).$$

This connects the inner product $\langle \hat h_{4,\lambda}, A_\lambda k\rangle$ with the first $2k$ moments of the zeros of $\Xi$.

**Symmetry remark.** The function $\hat h_{4,\lambda}(t)$ is the 4th even PSWF in frequency space — it has exactly 4 symmetric real zeros (at $\pm t_1, \pm t_2$) and changes sign. The function $\Xi(t)\,\Psi_\lambda(t)$ also oscillates. The integral may have significant cancellations.

---

## 8. The cancellation mechanism: why AO is plausible

**Heuristic argument.** The core of the cancellation is the following: the vector $A_\lambda k_\lambda$ is the "arithmetic push" of the Weil kernel under the primes. By the functional equation $k(u) = k(u^{-1})$ and the symmetry $T(p)k(u) = p^{-1/2}[k(pu) + k(u/p)]$, the push $A_\lambda k$ is also an even positive function.

An even positive function in $H_\lambda^+$ admits the decomposition:
$$A_\lambda k_\lambda = \langle k_\lambda, A_\lambda k_\lambda\rangle k_\lambda + \sum_{j \geq 2} c_j \psi_j$$

where the coefficient $c_j = \langle \psi_j, A_\lambda k_\lambda\rangle$. For $A_\lambda k_\lambda \approx C\,k_\lambda$ (proportional to the dominant eigenvector), we need $c_j$ to be small for $j \geq 2$.

**Proposition 4** (the arithmetic perturbation rotates the eigenvector minimally). Let $r_\lambda := A_\lambda k_\lambda / \|A_\lambda k_\lambda\|$ (the normalized push vector). Then:

$$|\langle r_\lambda, k_\lambda\rangle|^2 + \sum_{j\geq 2} |\langle r_\lambda, \psi_j\rangle|^2 = 1.$$

The vector $r_\lambda$ "points in the direction of $k_\lambda$" (i.e., $|\langle r_\lambda, k_\lambda\rangle| \approx 1$) if and only if the arithmetic push is nearly proportional to the Weil kernel.

**Evaluation of the dominant coefficient.** By the positivity of $k_\lambda$ and of $A_\lambda k_\lambda$:
$$\langle k_\lambda, A_\lambda k_\lambda\rangle = A_\lambda(k_\lambda, k_\lambda) = \sum_{p \leq \lambda^2} \Lambda(p)\,p^{-1/2}\!\int k_\lambda(u)\,k_\lambda(pu)\,d^*u > 0.$$

This coefficient is positive and large (of order $\sim 2\lambda \cdot m(\lambda)^2$, using Corollary 1 of doc 04 and the PNT). By the eigenvector decomposition:
$$\|A_\lambda k_\lambda\|^2 = |\langle k_\lambda, A_\lambda k_\lambda\rangle|^2 + \sum_{j\geq 2} |\langle \psi_j, A_\lambda k_\lambda\rangle|^2.$$

If $\|A_\lambda k_\lambda\|^2 \approx |\langle k_\lambda, A_\lambda k_\lambda\rangle|^2$, then the coefficients of the excited components are small.

**Lower bound of $\langle k_\lambda, A_\lambda k_\lambda\rangle$.** From doc 04:
$$\langle k_\lambda, A_\lambda k_\lambda\rangle = A_\lambda(k_\lambda) \geq C\lambda m(\lambda)^2 = C\lambda \cdot \Theta(\lambda^9 e^{-2\pi\lambda^2}).$$

**Estimate of $\|A_\lambda k_\lambda\|^2$.** By the bound $\|A_\lambda\|_{\mathrm{op}} = O(\lambda)$ (from doc 02) and $\|k_\lambda\| = O(1)$:
$$\|A_\lambda k_\lambda\| \leq \|A_\lambda\|_{\mathrm{op}}\|k_\lambda\| = O(\lambda).$$

Hence $\|A_\lambda k_\lambda\|^2 = O(\lambda^2)$.

Comparing: $|\langle k_\lambda, A_\lambda k_\lambda\rangle| \geq C\lambda^{10} e^{-2\pi\lambda^2}$. The ratio:

$$\frac{|\langle k_\lambda, A_\lambda k_\lambda\rangle|}{\|A_\lambda k_\lambda\|} \geq \frac{C\lambda^{10} e^{-2\pi\lambda^2}}{O(\lambda)} = C\lambda^9 e^{-2\pi\lambda^2} \to 0.$$

This ratio tends to 0, which means the vector $r_\lambda = A_\lambda k_\lambda / \|A_\lambda k_\lambda\|$ is NOT approximately aligned with $k_\lambda$ in norm.

**Interpretation.** Arithmetic orthogonality does NOT hold in the $L^2$ norm of $H_\lambda$. The arithmetic push $A_\lambda k_\lambda$ has a large component in the directions $\psi_j$ for $j \geq 2$. This confirms the diagnosis of doc 02-03: norm-to-norm analysis ($L^2$ perturbations) cannot give convergence.

---

## 9. The way out: convergence of zeros via Mellin structure

The failure of orthogonality in $L^2$ norm does not close off the path. The key insight of Theorem 1 of doc 03 (Rouché) is that convergence of zeros requires only a POINTWISE estimate of $|\hat\xi_\lambda(z) - c\hat k_\lambda(z)|$ for $z$ on circles around the zeros of $\hat k_\lambda$.

**Proposition 5** (decomposition of the perturbation in Mellin space). Let us write $\xi_\lambda = k_\lambda + \delta_\lambda$ (with $\delta_\lambda \perp k_\lambda$ in $H_\lambda$). Then:

$$\hat\xi_\lambda(z) - \hat k_\lambda(z) = \hat\delta_\lambda(z) = \int_{\lambda^{-1}}^\lambda \delta_\lambda(u)\,u^{-iz}\,d^*u.$$

The function $\hat\delta_\lambda(z)$ is an entire function (Mellin transform of a function in $L^2([\lambda^{-1},\lambda], d^*u)$). Its zeros are potentially DIFFERENT from those of $\hat k_\lambda$.

**The key question (Question 29.2 restated).** Are the zeros of $\hat\xi_\lambda = \hat k_\lambda + \hat\delta_\lambda$ close to those of $\hat k_\lambda$, even though $\hat\delta_\lambda$ is large in norm?

To answer, we decompose $\delta_\lambda = \sum_{j\geq 2} c_j \psi_j$ (projection onto excited eigenvectors). Then:
$$\hat\delta_\lambda(z) = \sum_{j \geq 2} c_j \hat\psi_j(z).$$

For $z$ near the $n$-th zero $\gamma_n$ of $\hat k_\lambda \approx \Xi$:
$$|\hat\delta_\lambda(\gamma_n)| \leq \sum_{j\geq 2} |c_j|\,|\hat\psi_j(\gamma_n)|.$$

If the excited eigenvectors $\psi_j$ are "blind" at the zeros of $\Xi$ (i.e., $\hat\psi_j(\gamma_n) \approx 0$), then $\hat\delta_\lambda(\gamma_n) \approx 0$ even though the coefficients $c_j$ are large.

**Hypothesis SO (spectral orthogonality at the zeros of $\Xi$).** For $j \geq 2$ and every $n$:
$$|\hat\psi_j(\gamma_n)| \leq C_{j,n}\,e^{-\pi\lambda^2/(j^2)}.$$

If SO holds, then $|\hat\delta_\lambda(\gamma_n)| \leq \sum_j |c_j| C_{j,n} e^{-\pi\lambda^2/j^2}$. Combined with $|c_j| = O(\lambda e^{4\pi\lambda^2}/j^2)$ (conservative estimate of the perturbation), this gives:

$$|\hat\delta_\lambda(\gamma_n)| = O\!\left(\lambda e^{4\pi\lambda^2} \sum_j \frac{C_{j,n}}{j^2} e^{-\pi\lambda^2/j^2}\right).$$

For $j = 2$: the dominant term is $O(\lambda e^{4\pi\lambda^2}) \cdot C_{2,n} e^{-\pi\lambda^2/4} = O(\lambda C_{2,n} e^{(4-1/4)\pi\lambda^2})$. This is still exponentially large.

**Partial verdict.** The SO hypothesis in its current form does NOT resolve Wall-H2 unless $C_{j,n}$ decays fast enough to compensate the $e^{4\pi\lambda^2}$ factor from the spectral gap.

---

## 10. A new mechanism: orthogonality via the Carathéodory-Fejér structure

The Perron-Frobenius approach and the $L^2$ arithmetic orthogonality approach face the same wall: the ratio spectral-gap / perturbation-norm grows exponentially. But there is a DIFFERENT mechanism absent from standard perturbation theory: the Carathéodory-Fejér structure of the minimizer.

**The CCM theorem (restated in the current key).** The minimizer $\xi_\lambda$ is NOT the vector closest to $k_\lambda$ in $L^2$ norm — it is the vector that MINIMIZES $QW_\lambda$. The Carathéodory-Fejér structure guarantees that its zeros (those of $\hat\xi_\lambda$) are all real. The question is not how close $\xi_\lambda$ is to $k_\lambda$ in $L^2$, but how close the ZEROS of $\hat\xi_\lambda$ are to those of $\hat k_\lambda \approx \Xi$.

**Proposition 6** (the spectral gap does not control the zeros). There exist entire functions $F, G$ with all zeros real such that $\|F - G\|_{L^2}$ is large (the norm of the difference of the original functions is large) but the zeros of $F$ and $G$ are close. Example: $F(z) = (z-a)e^{bz}$ and $G(z) = (z-a')e^{b'z}$ with $a \approx a'$: the norm $\|F-G\|$ can be large if $b \neq b'$, but the only zeros are $a$ and $a'$.

**Interpretation.** The difference $\hat\xi_\lambda - c\hat k_\lambda$ can have large norm in $L^\infty$ or $L^2$ (if $c \neq e^{a+ibz}$ exactly), but its zeros can be close. The phase factor $e^{a_\lambda + ib_\lambda z}$ in the CCM convergence formula absorbs the "global" difference between $\hat\xi_\lambda$ and $\hat k_\lambda$, allowing the zeros to be close even without convergence in norm.

---

## 11. Verdict: what is new in this document and what remains

### New results of doc 05:

| Result | Status |
|---|---|
| $T(p)$ preserves the positive cone $\mathcal{C}_N^+$ (Prop. 1) | **Proved** |
| $A_\lambda$ preserves the cone (Corollary) | **Proved** |
| $A_\lambda(|f|, |f|) \geq A_\lambda(f,f)$ for every $f$ (condition C2) | **Proved** |
| $Q^{\mathrm{cross}}(|f|) \geq Q^{\mathrm{cross}}(f)$ for every $f$ | **Proved** |
| Node argument obstructed by condition (C1) ($Q^{\mathrm{arch}}$) | **Identified** |
| Arithmetic orthogonality does NOT hold in $L^2$ norm (ratio → 0) | **Proved** |
| The spectral gap does not control the zeros (Prop. 6, explicit example) | **Proved** |
| The Carathéodory-Fejér mechanism as an alternative route | **Pointed out** |

### The precise wall (revised):

The central obstacle is NOT the spectral gap $\delta_\lambda$ per se, but the relation between:
1. The phase variation $e^{a_\lambda + ib_\lambda z}$ between $\hat\xi_\lambda$ and $c\hat k_\lambda$ (which perturbation theory ignores).
2. The relative position of the zeros of $\hat\xi_\lambda$ vs $\hat k_\lambda$ (which can be good even though the function difference is large).

### New question (29.4):

> **Question 29.4.** Can $|\hat\xi_\lambda(\gamma_n) - \hat k_\lambda(\gamma_n)|$ be bounded directly, without going through $\|\xi_\lambda - k_\lambda\|_{L^1}$, using the zero equation of doc 03 (Proposition 3)?

The zero equation of $\hat\xi_\lambda$ is:
$$\sum_{|m|\leq N} \frac{\xi_m^{(\lambda)}}{z - 2\pi m/L} = 0$$

and for $\hat k_\lambda$:
$$\sum_{|m|\leq N} \frac{k_m^{(\lambda)}}{z - 2\pi m/L} = 0.$$

The difference of the zeros depends on the difference of the COEFFICIENTS $\xi_m - c\,k_m^{(\lambda)}$ — which even if large in $\ell^2$, can lead to close zeros if the difference is "orthogonal" in the correct functional sense.

This is the most concrete and specific question to the CCM program that remains open.
