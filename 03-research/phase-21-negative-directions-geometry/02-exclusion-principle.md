# Phase 21 — Step 2: The Exclusion Principle and the Kreĭn-Langer Audit

**Central question:** Can it be proved that $0 < \kappa < \infty$ is impossible for $\zeta$?
**Type of analysis:** Audit before starting 21-D

---

## Precise statement of the Exclusion Conjecture

**Conjecture EX.** There is no realization of the Weil form associated with $\zeta$ for which $0 < \kappa < \infty$.

In terms of the negative space:

$$\kappa \in \{0\} \cup \{\infty\}.$$

If proved: RH becomes the binary question $\kappa = 0$ or $\kappa = \infty$.

---

## Why this question is new

Conjecture EX is NOT equivalent to any of the identified walls:

| Wall | Equivalent | Does it reduce to it? |
|------|-------------|-----------------|
| W1 (PNT/Weil positivity) | $\psi(x) = x + O(x^{1/2+\varepsilon})$ | No: EX is geometric, not estimative |
| W2 (SURF/de Branges) | Constructing a global cohomology | No: EX constructs nothing, only excludes |
| W3 (pair correlation/GUE) | Universality of gaps | No: EX is about proliferation, not distribution |

EX says: **if any Lorentz block exists, infinitely many must exist**.
This is a statement of forced proliferation, not a statement of positivity or construction.

---

## Rigorous analysis: what does Kreĭn-Langer theory say about $0 < \kappa < \infty$?

### The factorization

If $0 < \kappa = 2m < \infty$, the Kreĭn-Langer theorem applied to $E(z) = \xi(\tfrac{1}{2}+iz)$ gives:
$$E(z) = E_0(z) \cdot B_{2m}(z),$$
where:
- $B_{2m}$ is a Blaschke product (rational function) of degree $2m$ in the upper half-plane, with its $2m$ poles at the images of the off-line zeros with $\Re\rho < \tfrac{1}{2}$.
- $E_0$ is a genuine de Branges function: entire, satisfies $|E_0(\bar z)| < |E_0(z)|$ for $\Im z > 0$, all of its zeros are real or in the lower half-plane.

The de Branges-Pontryagin space $H(E)$ decomposes:
$$H(E) = H(E_0) \oplus^{\perp_Q} \text{Pontryagin correction}_{2m}.$$

The Pontryagin correction has dimension $2m$.

### What this implies

If $\kappa = 2m$, then there exists an entire $E_0$ with:
1. All zeros of $E_0$ on the real axis (in the $z$ coordinate), i.e., all zeros of $\xi(\tfrac{1}{2}+iz)/B_{2m}(z)$ are real.
2. $E_0$ has order 1 (same as $E$, since $B_{2m}$ is rational).
3. $E_0$ satisfies the induced functional equation (since $\xi$ and $B_{2m}$ are both $\iota$-invariant).

**Remark:** $E_0$ is an entire function with all its zeros in $\mathbb{R}$, of order 1, satisfying a functional equation analogous to that of $\xi$. This is consistent with de Branges theory: there is an enormous family of such functions.

**There is no contradiction at the level of functional analysis alone.**

---

## The obstacle to proving EX

Conjecture EX would require showing that:

> The additional restriction coming from the **Euler product** prevents $E_0$ from existing as a finite separation from $E$.

More precisely: if $\xi$ has exactly $4m$ off-line zeros, then $E/B_{2m}$ must be inconsistent with the Euler product of $\zeta$.

### Why might the Euler product help?

The Euler product $\zeta(s) = \prod_p (1-p^{-s})^{-1}$ for $\Re s > 1$ forces the zeros of $\zeta$ to be related to the primes in a very specific way. Not every configuration of zeros can come from an L-function with an arithmetic Euler product.

But: the relation between individual zeros and individual primes is not direct. The Euler product determines the **statistical distribution** of the zeros (via the explicit formula), not the exact location of each zero.

### The real wall behind EX

Conjecture EX, if it could be proved, would require something of the form:

> "If the function $\xi(\cdot)/B_{2m}(\cdot)$ satisfies the functional equation and has order 1, and if $\xi$ comes from an arithmetic Euler product, then $B_{2m}$ must be trivial ($m=0$) or infinitely nontrivial ($m=\infty$)."

This connects with:

1. **Uniqueness of the Euler product**: the function $\zeta$ is the unique element of the Selberg class with conductor 1. Does the conductor force the structure of off-line zeros?

2. **Spectral rigidity**: in random matrix theory, spectral rigidity says that eigenvalue positions are highly rigid ($O(1)$ fluctuations). If something analogous holds for the zeros of $\zeta$, it could prevent the existence of a finite number of off-line zeros.

3. **The linear independence hypothesis (LI)**: the $\gamma_\rho$ are linearly independent over $\mathbb{Q}$. This prevents certain kinds of "resonances" between zeros. Could it imply that one off-line zero forces an infinite chain?

**None of these approaches currently leads to a theorem.**

---

## What can actually be proved in 21-D

### Theorem 21-D.1 (Formal structure of the Pontryagin regime)

**Statement.** Assume $0 < \kappa = 2m < \infty$. Then there exists an entire function $E_0 = \xi(\tfrac{1}{2}+iz)/B_{2m}(z)$ of order 1 such that:
1. All zeros of $E_0$ are real (in the $z$ coordinate), equivalently all zeros of the corresponding entire function lie on the critical line.
2. $E_0$ is a de Branges function (Hermite-Biehler): $|E_0(\bar z)| < |E_0(z)|$ for $\Im z > 0$.
3. The Hilbert space $H(E_0)$ (de Branges) has zero negative index: the Weil form restricted to $H(E_0)$ is positive-semidefinite.
4. In the functional sense: "RH holds on $H(E_0)$".

This is a direct consequence of the Kreĭn-Langer theorem and Proposition~\ref{prop:restricted} of P32.

### Corollary 21-D.2 (Partial RH under $\kappa < \infty$)

If $\kappa = 2m < \infty$, then there exists an entire function $\xi_0$ satisfying the functional equation with all zeros on the critical line, related to $\xi$ by:
$$\xi(s) = \xi_0(s) \cdot P_{4m}(s),$$
where $P_{4m}$ is a polynomial of degree $4m$ with roots exactly at the $4m$ off-line zeros of $\xi$.

**Proof.** $\xi_0(s) = \xi(\tfrac{1}{2}+i(\cdot)) / B_{2m}(\cdot)$ under the appropriate change of variables. $P_{4m}$ is the polynomial whose zeros are the $4m$ images of the off-line zeros. $\square$

**Remark.** This result is neither circular nor does it assume RH: it is a conditional statement. It says that IF $\kappa = 2m < \infty$, THEN there exists $\xi_0$ with RH. But it does not say that $\xi_0 = \xi$ (if $\xi_0 = \xi$ then $P_{4m} = 1$ and $\kappa = 0$, which is RH).

---

## Identification of the new obstacle (not W1/W2/W3)

**Proposition 21-D.3 (New territory).** The Exclusion Conjecture, if it could be proved, would constitute a result of a new kind: it does not reduce to W1, W2, or W3.

**Argument:**

- **It is not W1**: W1 says that proving $\kappa = 0$ requires estimating the PNT error. EX does not say $\kappa = 0$; it says $\kappa \notin (0,\infty)$. It does not directly imply $\kappa = 0$.

- **It is not W2**: W2 requires constructing SURF. EX is a statement of impossibility (it constructs nothing); it is formally a nonexistence theorem.

- **It is not W3**: W3 is GUE universality. EX does not speak about the distribution of gaps, but about whether the count $m$ can be finite and positive.

**Proving EX would instead require**:

> A theorem of the form: "the spectral rigidity of the Euler product does not allow $\xi$ to factor as $\xi_0 \cdot P_{4m}$ with $\xi_0$ entire with all zeros on the critical line and $1 \leq m < \infty$."

This is a statement of arithmetic rigidity: the Euler product forces the zeros of $\zeta$ to be "all on-line" or "infinitely off-line", with no intermediate state.

This is genuinely new because it is not:
- An estimate (W1)
- A construction (W2)
- A statistic (W3)
- A positivity (N1: capstone)

It is an **arithmetic-geometric impossibility statement**.

---

## The candidate for W4: Spectral Rigidity of the Pontryagin Regime

Having shown that EX is genuinely new and not reducible to the known walls, we formally identify it:

**Definition (W4-candidate).** The **Spectral Rigidity of the Pontryagin Regime** (RSRP) wall is the conjecture:

> For $\zeta$, there is no configuration of zeros with $0 < m < \infty$ complete off-line orbits that is consistent with the Euler product, the functional equation, and the order-1 growth of $\xi$.

That is: $m = 0$ (RH) or $m = \infty$ (infinitely many off-line zeros).

**Current status:** Conjecture. Neither proved nor refuted.

**Why it is hard:** No tool is known that connects the Euler product with the cardinality of off-line zeros. Kreĭn-Langer theory only speaks of formal structure; it does not speak of arithmetic.

---

## Possible paths (no guarantee)

### Path 1: Siegel-type rigidity

The zeros of $\zeta$ satisfy irrationality relations (under LI). Could it be proved that the existence of $m$ off-line zeros forces the existence of $m+1$ off-line zeros via some irrationality or transcendence argument?

**Obstacle:** The irrationality arguments for the $\gamma_\rho$ do not control the sign of $\Re\rho - \tfrac{1}{2}$.

### Path 2: Critical-density-type rigidity

An off-line zero at height $\gamma_0$ would perturb the local distribution of zeros in $[\gamma_0 - \delta, \gamma_0 + \delta]$. If this perturbation violates a local density invariant, it could force new off-line zeros.

**Obstacle:** The local density of zeros does not distinguish on-line from off-line for $\Re\rho$ close to $\tfrac{1}{2}$.

### Path 3: Global analyticity argument

If $m < \infty$, the function $\xi/P_{4m}$ is entire with all zeros on the critical line. Could it be proved that no function of the type "finite deformation of $\xi$" has all zeros on the critical line, except $\xi$ itself (which would be the case $m=0$)?

**Obstacle:** There is no uniqueness principle for entire functions with all zeros on a line. Infinitely many functions with that property can be constructed.

### Path 4: Automorphy argument

If $\zeta$ comes from an automorphic representation (which it does, as $GL_1$), do the properties of the representation prevent finite positive $m$?

**Obstacle:** The theory of automorphic forms gives the functional equation and the Euler product, but not directly the position of individual zeros. This falls back on W1.

---

## Audit conclusion

The Exclusion Conjecture (EX) is:

1. **Genuinely new** (not reducible to W1/W2/W3). ✓
2. **Well posed mathematically**. ✓
3. **Not provable with current tools**. ✓
4. **A new wall candidate** (W4-RSRP). ✓
5. **No harder than RH** if and only if... its relative difficulty is actually unknown. It is possible that EX is exactly as hard as RH, or harder.

**What is actually resolved in Phase 21:**
- Parity Theorem: $\kappa = 2m$ (Class B, proved). ✓
- Angular Separation: exponential orthogonality (Class B, proved). ✓
- Lorentz Decomposition: $\mathcal{N} \cong \bigoplus_j \mathbb{R}^{1,1}_j$ (Class B, proved). ✓
- Formal Structure of the Pontryagin Regime (Theorem 21-D.1): $E = E_0 B_{2m}$ (Class B, proved). ✓
- Partial RH under $\kappa < \infty$ (Corollary 21-D.2): $\xi = \xi_0 \cdot P_{4m}$ (Class B, proved). ✓

**What remains open:**
- EX (Class A if successful): $m > 0 \Rightarrow m = \infty$. Not proved. Candidate for W4-RSRP.

---

## Update to the wall map

| Wall | Description | Status |
|------|-------------|--------|
| W1 | PNT / Weil positivity / zero error | Confirmed |
| W2 | SURF / de Branges / global completeness | Confirmed |
| W3 | Pair correlation / GUE / gaps | Confirmed |
| W4-RSRP | Spectral rigidity of the Pontryagin regime (EX) | **New candidate** |

W4-RSRP is genuinely distinct from W1/W2/W3. It is not obviously equivalent to RH (it could be an intermediate condition, stronger or weaker). Its precise status with respect to RH is unknown.
