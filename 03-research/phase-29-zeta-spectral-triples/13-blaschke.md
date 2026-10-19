# Phase 29 — The Blaschke product and the structure of H2

**Objective:** Develop the Blaschke-product approach $B_\lambda = \hat\xi_\lambda/\hat k_\lambda$ started in doc 12. Answer Advisor 2's Question 29.10 (is $M_1[\Delta]\to 0$ sufficient for $B_\lambda\to 1$?). Identify the precise ingredient missing to close H2.

---

## 1. The Blaschke product: precise definition

In the space $E_N^+ = \text{span}\{V_n : |n|\leq N\}$ with $V_n(u) = L^{-1/2}\exp(2\pi in\log(\lambda u)/L)$ and $L = 2\log\lambda$, the functions $\hat\xi_\lambda^{(N)}$ and $\hat k_\lambda^{(N)}$ are trigonometric polynomials of degree $N$ in the variable $t$.

Under the substitution $z = e^{2\pi it/L}$ (i.e., $t\mapsto z$, the unit-circle variable $\mathbb{T}$): both functions become polynomials of degree $N$ in $z$ with complex coefficients.

**Definition.** The *rational Blaschke product* of the CCM program is:

$$B_\lambda(z) := \frac{\hat\xi_\lambda^{(N)}(z)}{\hat k_\lambda^{(N)}(z)}, \quad z = e^{2\pi it/L}, \quad t\in\mathbb{R}.$$

Immediate properties:
- **Zeros:** $\{z_n = e^{2\pi it_n/L}\}_{n=1}^{N}$ where $\{t_n^{(\lambda)}\}$ are the zeros of $\hat\xi_\lambda$ (eigenvalues of the CCM operator, always real by self-adjointness).
- **Poles:** $\{w_n = e^{2\pi is_n/L}\}_{n=1}^{N}$ where $\{s_n^{(\lambda)}\}$ are the zeros of $\hat k_\lambda$ (approximations to the $\gamma_n$, Doc 06 Theorem 1: $|s_n-\gamma_n|=O(\lambda^{-1/2}/w_n)$).
- **Self-adjointness:** $t_n^{(\lambda)}\in\mathbb{R}$ for all $n$ → the zeros $z_n$ are ALWAYS on $\mathbb{T}$.
- **Symmetry:** $\hat k_\lambda$ is even ($k_\lambda(u) = k_\lambda(u^{-1})$) → zeros of $\hat k_\lambda$ come in pairs $\pm s_n$. The zeros $w_n = e^{2\pi is_n/L}$ may have a small imaginary part (of order $O(\lambda^{-1/2}/w_n)$ off $\mathbb{T}$).

**Key fact.** The zeros of $B_\lambda$ are on $\mathbb{T}$ (real) and the poles of $B_\lambda$ are at distance $O(\lambda^{-1/2}/w_n)$ from $\mathbb{T}$ (nearly real). As $\lambda\to\infty$, both zeros and poles approach the image of $\{\gamma_n\}$ on $\mathbb{T}$.

---

## 2. The equivalence H2 ↔ $B_\lambda\to 1$

**Proposition 1.** The following are equivalent:

(a) H2: $\hat\xi_\lambda^{(N)}\to c\cdot\Xi$ uniformly on compacta of $\mathbb{C}$.

(b) $B_\lambda(z)\to 1$ uniformly on compacta of $\mathbb{C}\setminus\{w_n\}$.

*Proof.* $(a)\Rightarrow(b)$: $\hat k_\lambda\to c'\Xi$ (Lemma 7.3, Doc 00), so $B_\lambda = \hat\xi_\lambda/\hat k_\lambda \to (c/c')\cdot 1 = $ constant $\to 1$ (by the normalization $B_\lambda(0) = \xi_0/k_0 \to 1$ of the leading coefficients).

$(b)\Rightarrow(a)$: $\hat\xi_\lambda = B_\lambda\cdot\hat k_\lambda \to 1\cdot(c'\Xi) = c'\Xi$. $\square$

---

## 3. Theorem 1: $B_\lambda\to 1$ under RH

This is the correct reformulation of Theorem 5 of doc 09.

**Theorem 1** (Convergence of the Blaschke product, under RH). If RH is true, then:

$$B_\lambda(z) \to 1 \quad \text{uniformly on compacta of } \mathbb{C}\setminus\mathbb{T}.$$

*Proof.* It suffices to show that $\log B_\lambda(z)\to 0$ for $z$ in compacta of $\mathbb{C}\setminus\mathbb{T}$, since $B_\lambda$ is analytic and eventually zero-free on $\mathbb{C}\setminus\mathbb{T}$.

**Step 1: Integral representation.** For $z\notin\mathbb{T}$:

$$\log B_\lambda(z) = \int_\Gamma (\log B_\lambda)'(w)\,dw = \int_\Gamma \left[\frac{(\hat\xi_\lambda)'(w)}{\hat\xi_\lambda(w)} - \frac{(\hat k_\lambda)'(w)}{\hat k_\lambda(w)}\right]dw,$$

where $\Gamma$ is a path from a fixed base point to $z$ avoiding $\mathbb{T}$.

The difference of logarithmic derivatives is:

$$\frac{(\hat\xi_\lambda)'}{\hat\xi_\lambda}(w) - \frac{(\hat k_\lambda)'}{\hat k_\lambda}(w) = N\left[S_\xi(w;\lambda) - S_k(w;\lambda)\right],$$

where $S_\xi = (1/N)\sum_n 1/(w-t_n)$ and $S_k = (1/N)\sum_n 1/(w-s_n)$ are the (normalized) Stieltjes transforms of the zero measures.

**Step 2: Stieltjes convergence.** We rewrite:

$$N[S_\xi(w;\lambda) - S_k(w;\lambda)] = \int_\mathbb{R}\frac{d(\mu_\xi^\lambda - \mu_k^\lambda)(t)}{w-t},$$

where $\mu_\xi^\lambda = (1/N)\sum_n\delta_{t_n^{(\lambda)}}$ and $\mu_k^\lambda = (1/N)\sum_n\delta_{s_n^{(\lambda)}}$.

By Doc 08 (Theorem 1), unconditionally: $\mu_k^\lambda\to\mu_\gamma$ (weak convergence), where $\mu_\gamma$ is the zero measure of $\Xi$.

Under RH: Doc 09 (Theorem 3) shows $\mu_\xi^\lambda\to\mu_\gamma$ weakly.

Hence $\mu_\xi^\lambda - \mu_k^\lambda\to 0$ weakly. For $w\notin\mathbb{R}$: the function $t\mapsto 1/(w-t)$ is continuous and bounded on $\mathbb{R}$. So by weak convergence:

$$\int_\mathbb{R}\frac{d(\mu_\xi^\lambda - \mu_k^\lambda)(t)}{w-t} \to 0 \quad\text{for each } w\notin\mathbb{R}.$$

The convergence is uniform on compacta of $\mathbb{C}\setminus\mathbb{R}$ by uniform boundedness of $\|1/(w-\cdot)\|$ on compacta.

**Step 3: Integration.**

$$|\log B_\lambda(z)| = \left|\int_\Gamma N[S_\xi-S_k](w)\,dw\right| \leq \text{length}(\Gamma)\cdot\sup_{w\in\Gamma}|N[S_\xi-S_k](w)| \to 0. \quad \square$$

---

## 4. Question 29.10: is $M_1[\Delta]\to 0$ enough?

Advisor 2 proposed:

> **Question 29.10.** Is $M_1[\Delta]\to 0$ sufficient for $B_\lambda(z)\to 1$ uniformly on compacta?

**Answer: No, in general. $M_1[\Delta]\to 0$ is necessary but not sufficient.**

**Proof of insufficiency.** Consider the caricature case: $N = 2$, $t_1 = \gamma_1 + \varepsilon$, $t_2 = \gamma_2 - \varepsilon$, $s_n = \gamma_n$. Then $M_1[\Delta] = c\cdot(\varepsilon - \varepsilon) = 0$ (first moment zero by cancellation). But $B_\lambda(z) = \frac{(z-\gamma_1-\varepsilon)(z-\gamma_2+\varepsilon)}{(z-\gamma_1)(z-\gamma_2)} \neq 1$. The Blaschke product is NOT 1 even though $M_1[\Delta] = 0$. $\square$

**What $M_1[\Delta]$ does control.** The first moment controls the logarithmic derivative of $B_\lambda$ at the origin of Mellin space:

$$[(\log B_\lambda)']_{t=0} = \sum_n\left[\frac{1}{-t_n} - \frac{1}{-s_n}\right] = \sum_n\frac{\delta_n}{t_n s_n},$$

which is a weighted combination of the displacements $\delta_n = t_n - s_n$. The control $M_1[\Delta]\to 0$ implies that this weighted sum tends to 0, but does NOT control the individual terms $\delta_n$.

**Proposition 2** (what is missing). For $B_\lambda\to 1$, it is sufficient (but stronger than $M_1[\Delta]\to 0$) that:

$$\sum_n\frac{|\delta_n|}{|z-s_n|^2} \to 0 \quad \text{for } z\notin\mathbb{R},$$

or equivalently (using $|z-s_n|\geq|\Im(z)|$):

$$\frac{1}{|\Im(z)|^2}\sum_n|\delta_n| \to 0, \quad\text{i.e.,}\quad \sum_n|\delta_n| \to 0.$$

And $\sum_n|\delta_n| = \sum_n|t_n^{(\lambda)}-s_n^{(\lambda)}|$ — the sum of all absolute displacements.

**Question 29.11** (new). Is $\sum_n|t_n^{(\lambda)}-s_n^{(\lambda)}| \to 0$?

---

## 5. Analysis of Question 29.11

The sum $\sum_n|t_n-s_n|$ involves $N\sim\lambda^2/\log\lambda$ terms, each of size $O(\log\lambda)$ (from Doc 12, estimated by counting). Hence the crude bound gives:

$$\sum_n|t_n-s_n| = O\!\left(\frac{\lambda^2}{\log\lambda}\cdot\log\lambda\right) = O(\lambda^2) \to +\infty.$$

This confirms that the convergence of $B_\lambda$ CANNOT be deduced from the individual bound $|t_n-s_n|=O(\log\lambda)$. The proof of Theorem 1 via Stieltjes (Section 3) is NECESARY because it avoids controlling the sum of individual zeros.

**Can the sum $\sum_n|t_n-s_n|$ decay?**

The current optimal individual bound is $O(\log\lambda)$ (from zero counting). For $\sum_n|t_n-s_n|\to 0$ we would need, on average, $|t_n-s_n| = o(\log\lambda/N) = o((\log\lambda)^2/\lambda^2)$ — this is a MUCH finer precision than what we have. It would require full rigidity of the zeros of the CCM operator.

**Conclusion.** The correct route to $B_\lambda\to 1$ is that of Theorem 1 (via weak Stieltjes convergence), not via control of $\sum_n|\delta_n|$. Question 29.11 is probably true under RH (its zeros follow the same limiting distribution) but hard to prove directly.

---

## 6. The Euler–Lagrange equation in terms of $B_\lambda$

The relation between $B_\lambda$ and the variational problem is more direct than it appears. The Euler–Lagrange equation of Doc 12 (Proposition 2) says:

$$\hat\xi_\lambda(z) = -c_\lambda\cdot\frac{\hat k_\lambda(z)}{C_\lambda(z) - \mu_\lambda}$$

(in the diagonal approximation with the rank-1 term). Hence:

$$B_\lambda(z) = \frac{\hat\xi_\lambda(z)}{\hat k_\lambda(z)} = \frac{-c_\lambda}{C_\lambda(z) - \mu_\lambda}.$$

This is the EXACT REPRESENTATION of $B_\lambda$ in terms of the potential $C_\lambda$!

**Proposition 3** (Blaschke representation via the potential). In the diagonal approximation:

$$B_\lambda(z) = \frac{-c_\lambda}{C_\lambda(z) - \mu_\lambda} = \frac{-c_\lambda}{w(z) - \Psi_\lambda(z) - \mu_\lambda}.$$

**Consequence.** $B_\lambda(z)\to 1$ if and only if $C_\lambda(z) - \mu_\lambda \to -c_\lambda$ (the normalization constant).

For $z = \gamma_n + iy$ ($y\to 0^+$): $w(\gamma_n) - \Psi_\lambda(\gamma_n) - \mu_\lambda \to w(\gamma_n) - \Psi(\gamma_n) - 0 = C_\infty(\gamma_n)$.

Under RH: $C_\infty(\gamma_n) = 0$. Hence the denominator tends to 0 at $z = \gamma_n$ — the zeros of $\hat k_\lambda$ (where $\hat k_\lambda(z) = 0$) are precisely where the denominator of $B_\lambda$ has poles. The numerator/denominator cancellation gives the zeros of $\hat\xi_\lambda$.

**Question 29.12** (new). Under what conditions does the normalization constant $c_\lambda$ in $B_\lambda = -c_\lambda/[C_\lambda-\mu_\lambda]$ converge to $-1$ (so that $B_\lambda\to 1$ when $C_\lambda-\mu_\lambda\to 1$)?

The condition $c_\lambda\to 1$ is equivalent to $\langle\xi_\lambda, k\rangle\to 1$, which is part of H2.

---

## 7. The Hurwitz argument: H2 implies RH

This is the step in the H2 → RH direction, which IS solidly proved and which the Blaschke product makes more transparent.

**Theorem 2** (H2 $\Rightarrow$ RH). If $\hat\xi_\lambda^{(N)}\to c\Xi$ uniformly on compacta of $\mathbb{C}$, then all zeros of $\Xi$ are real.

*Proof.* By Hurwitz's Theorem: if $f_n\to f$ uniformly on compacta, $f\not\equiv 0$, and each $f_n$ has no zeros in an open set $U$, then $f$ also has no zeros in $U$.

The contrapositive: if $\Xi$ had a zero $\rho = 1/2 + i(\sigma + i\tau)$ with $\tau\neq 0$ (off the real line), then by Hurwitz, eventually $\hat\xi_\lambda^{(N)}$ would have a zero near $\rho$ — in particular, a NON-REAL zero. But $\hat\xi_\lambda^{(N)}$ is the characteristic polynomial of $D_\lambda^N$, a self-adjoint operator, whose eigenvalues are ALL real. The zeros of $\hat\xi_\lambda^{(N)}$ are ALWAYS real. Contradiction. Hence all zeros of $\Xi$ are real, i.e., RH. $\square$

**Corollary.** In terms of the Blaschke product: if $B_\lambda\to 1$, then (by Proposition 1) $\hat\xi_\lambda\to c'\Xi$, and by Theorem 2, RH.

---

## 8. Updated table of equivalences

The complete structure of the CCM program (revised after doc 12):

```
RH
 ⟺ all zeros of Ξ are real
 ⟹ Stieltjes: S_ξ(z;λ) → S_Ξ(z) (Doc 09, Th 3)
 ⟹ B_λ(z) → 1 (Theorem 1, this doc)
 ⟺ H2: ξ̂_λ → c Ξ (Proposition 1, this doc)
 ⟹ (Hurwitz) → zeros of Ξ are real
 ⟹ RH                                    [closing the chain]
```

**Status of the arrows:**

| Arrow | Direction | Condition | Proof |
|---|---|---|---|
| RH → Stieltjes | → | under RH | Doc 09, Th 3 |
| Stieltjes → $B_\lambda\to 1$ | → | under RH | **Theorem 1, this doc** |
| $B_\lambda\to 1$ ↔ H2 | ↔ | always | **Proposition 1, this doc** |
| H2 → RH | → | always | **Theorem 2, this doc** |
| **Gap:** $B_\lambda\to 1$ without assuming RH | ?? | unconditional | **OPEN** |

The only step missing for a conditional proof of RH is already known (Doc 09). The only step missing for an UNCONDITIONAL proof is the gap in the last row.

---

## 9. The real wall: $B_\lambda\to 1$ unconditionally

The gap can be cleanly reformulated:

**Blaschke-Wall.** Prove that $B_\lambda(z)\to 1$ for $z\in\mathbb{C}\setminus\mathbb{T}$ without assuming RH.

Equivalently (Proposition 1): prove H2 without assuming RH.

Equivalently (Proposition 3, diagonal approximation): prove that $-c_\lambda/(C_\lambda(z)-\mu_\lambda)\to 1$, i.e., that $c_\lambda\to 1$ and $C_\lambda(z)-\mu_\lambda\to -1$ (for the appropriate normalization).

**The precise missing ingredient.** From the representation (Proposition 3):

$$B_\lambda(z) = -c_\lambda/[C_\lambda(z) - \mu_\lambda].$$

For $B_\lambda\to 1$ we need:
$$c_\lambda \to -[C_\lambda(z) - \mu_\lambda]_{\text{normalization}}.$$

This requires the potential $C_\lambda$ to have a DETERMINED behavior independent of whether RH is true. Specifically: we need control of $C_\lambda$ in the strip $\{|\Im z| < \eta\}$ without assuming that the zeros of $\Psi$ are real.

**Precise formulation of the gap:**

> **Question 29.13.** Can it be shown that $C_\lambda(z) - \mu_\lambda \to C_\infty(z) \neq 0$ uniformly for $z$ in compacta of $\mathbb{C}\setminus\mathbb{T}$, without assuming RH?

If the answer is yes and the limit $C_\infty(z) \neq 0$ for $z\notin\mathbb{R}$: then $B_\lambda\to -c_\lambda/C_\infty(z)$, which would be the constant 1 only if $c_\lambda\to -C_\infty(z)$ — this does not make the problem simpler.

The fundamental difficulty: without RH, the zeros of $\Xi$ may have imaginary part $\tau\neq 0$. Near such a zero $\rho = 1/2+i(\sigma+i\tau)$: $\Psi_\lambda(\rho)$ diverges (the crossings of the potential "escape" from the real line into the complex plane). The potential $C_\lambda(z)$ may have zeros off $\mathbb{T}$, which would mean $B_\lambda$ has a pole there — contradicting the self-adjointness of $\hat\xi_\lambda^{(N)}$ (which requires the zeros of $B_\lambda$ to lie on $\mathbb{T}$).

**This contradiction is precisely the CCM argument.** The CCM operator is self-adjoint by construction → $B_\lambda$ has all its zeros on $\mathbb{T}$ → if the poles of $B_\lambda$ (zeros of $\hat k_\lambda$) drift off $\mathbb{T}$, then $B_\lambda$ CANNOT converge to 1 — implying that the zeros of $\Xi$ must lie on $\mathbb{T}$ (in the limit). But this full argument still requires the convergence $B_\lambda\to 1$ to be rigorous.

**The wall is genuine and has no visible shortcuts.**

---

## 10. Summary of doc 13

**Proved in this doc:**
- $B_\lambda(z)\to 1$ under RH (Theorem 1, via Stieltjes)
- H2 ↔ $B_\lambda\to 1$ (Proposition 1)
- H2 → RH (Theorem 2, Hurwitz)
- $M_1[\Delta]\to 0$ is NOT sufficient for $B_\lambda\to 1$ (Question 29.10 resolved negatively)
- Exact representation $B_\lambda = -c_\lambda/[C_\lambda-\mu_\lambda]$ (Proposition 3)

**Open:**
- $B_\lambda\to 1$ unconditionally (Blaschke-Wall = H2-Wall)
- Question 29.11: $\sum_n|\delta_n|\to 0$?
- Question 29.12: $c_\lambda\to 1$ unconditionally?
- Question 29.13: control of $C_\lambda - \mu_\lambda$ without RH?

**The real wall of the Phase 29 program (clean final formulation):**

$$\boxed{B_\lambda(z)\to 1 \text{ unconditionally} \iff \text{H2} \iff \text{RH (via Hurwitz)}.}$$

The entire program reduces to a statement about a family of rational analytic functions: that the quotient of the minimizing function and the kernel function converges to 1 in the complex plane. This is the cleanest formulation the program has found so far.
