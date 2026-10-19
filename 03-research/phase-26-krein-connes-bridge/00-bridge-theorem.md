# Phase 26 — The bridge theorem: Kreĭn ↔ Connes

**Sole objective:** formulate with mathematical precision the theorem that identifies the
Kreĭn negative index κ with the non-self-adjointness of the Connes operator.

If the bridge theorem cannot be written precisely, Phase 26 cannot begin.

---

## 0. Bibliographic audit of the bridge

**Connes (1999):** "Trace formula in noncommutative geometry and the zeros of the
Riemann zeta function." Establishes the Weil formula as a trace formula of the
scaling operator on the adèle class space $X = \mathbb{A}_\mathbb{Q}/\mathbb{Q}^*$.

**Connes–Consani (2010, 2014, 2016):** The "scaling site" and the arithmetic geometry
of the adèle class space. Refinements of the trace formula.

**Burnol (2001, 2004):** The explicit formula as a scattering formula. The Connes
operator as a Dirac operator in a functional sense.

**Kreĭn–Langer (1978):** Factorization of $\mathfrak{J}$-nonnegative functions in Pontryagin
spaces. Spectral theorem for $\mathcal{Q}$-self-adjoint operators.

**Does a previous bridge theorem exist?** Not in the literature. There are cross-citations
between the programs, but no precise identification of the type κ(Q) = neg.ind($H_{CW}$).

The closest work: Burnol (2002, "On some symmetric Weil explicit formulas") connects
Weil positivity with spectral properties of Dirac operators, but does not explicitly identify
the Kreĭn index.

**Conclusion:** The bridge theorem does not exist in the literature. Its formulation is new.

---

## 1. The two structures to connect

### Structure A: The Weil quadratic form (Kreĭn side)

Let $\mathcal{S}(\mathbb{R}^*_+)$ be the Schwartz space of test functions on $\mathbb{R}^*_+$.
For $f \in \mathcal{S}(\mathbb{R}^*_+)$, the Weil form is:
$$\mathcal{W}(f) = \sum_\rho \hat{f}(\rho) - \hat{f}(0)\log\pi - \hat{f}(1)\log\pi
+ \sum_{p,n} \frac{\log p}{p^{n/2}} f(p^n) + \sum_{p,n}\frac{\log p}{p^{n/2}}f(p^{-n})
+ f(1)\log\pi,$$
where $\hat{f}$ is the Mellin transform of $f$, the sum $\sum_\rho$ runs over all non-trivial
zeros of $\zeta$, and the sum $\sum_{p,n}$ runs over prime powers.

The **Weil quadratic form** is:
$$Q(f, g) := \mathcal{W}(f * \tilde{g}), \qquad \tilde{g}(x) = \overline{g(1/x)} \cdot x^{-1}.$$

**Proposition 26-A.1** (Weil 1952). $Q(f,f) \geq 0$ for every admissible $f$
if and only if RH is true.

**Definition 26-A.2** (Kreĭn index). The **Kreĭn negative index** κ of $Q$ is the
maximum number of linearly independent vectors $\{f_1,\ldots,f_k\}$ such that the
Gram matrix $(Q(f_i,f_j))_{i,j}$ is negative definite:
$$\kappa := \sup \{k : \exists f_1,\ldots,f_k \in \mathcal{S} \text{ with } \det(Q(f_i,f_j)) < 0\}.$$

Under Hypothesis D with $m$ off-line orbits: $\kappa = 2m$ (Papers P32–P33).

### Structure B: The Connes operator (spectral side)

Let $C_\mathbb{Q} := \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$ be the idèle class group.
Let $H = L^2(C_\mathbb{Q}, d\mu)$ where $d\mu$ is the normalized Haar measure.

The group $\mathbb{R}^*_+$ acts on $C_\mathbb{Q}$ by multiplication:
$$(U_\lambda f)(x) = f(\lambda^{-1} x), \quad \lambda \in \mathbb{R}^*_+, f \in H.$$

The **Connes–Weil operator** is the infinitesimal generator of this representation:
$$H_C := \frac{1}{i}\left.\frac{d}{d\lambda}\right|_{\lambda=1} U_\lambda.$$

Formally: $(H_C f)(x) = -i x \frac{d}{dx} f(x)$ (the Euler operator on $C_\mathbb{Q}$).

**Known status:** $H_C$ is formally symmetric on test functions. Its self-adjoint extension
on $L^2(C_\mathbb{Q})$ is related to the distribution of the zeros of $\zeta$.
RH ↔ $H_C$ admits a self-adjoint extension with spectrum contained in $i\mathbb{R}$ (the imaginary axis
in Connes's parametrization where zeros appear as $s - 1/2 = i\gamma$).

---

## 2. The Weil quadratic form as an inner product on $H$

**Proposition 26-B.1** (Identification of Q with an inner product). For $f, g \in H$, the
**Weil–Connes inner product** is:
$$\langle f, g \rangle_Q := Q(f, g) = \mathcal{W}(f * \tilde{g}).$$

This defines a Hermitian form on $H$. By Proposition 26-A.1:
- If RH: $\langle f,f\rangle_Q \geq 0$ — positive semidefinite inner product.
- If Hypothesis D (κ=2m): $\langle f,f\rangle_Q$ has exactly 2m "negative directions" —
  indefinite inner product with negative index κ = 2m.

The space $(H, \langle\cdot,\cdot\rangle_Q)$ is formally:
- A **Hilbert space** if RH holds (positive structure).
- A space with an indefinite form of negative index κ = 2m if Hypothesis D holds.

**Warning:** that this second space is actually a **Pontryagin space** is not
proved. It requires verifying, beyond κ < ∞: (a) non-degeneracy (ker$Q$ of
finite or null dimension); (b) completeness of the quotient space $H/\ker Q$; (c) existence
of a fundamental decomposition $H = H_+ \oplus H_-$ with $H_-$ of dimension κ.
These properties are part of what Phase 26 must establish.

**Definition 26-B.2** (The Kreĭn-Connes space — conditional). If $Q$ admits a
Pontryagin completion of index κ, it is denoted $\mathcal{K}$. The existence of $\mathcal{K}$
is a goal of Phase 26, not a starting point.

**The Connes operator $H_C$ on $\mathcal{K}$**: $H_C$ is $Q$-symmetric if $Q(H_C f, g) = Q(f, H_C g)$
for all $f,g$ in the domain. Does this symmetry hold?

**Objective 26-B.3** ($Q$-invariance of the scaling — result to be proved). The condition
that would make $H_C$ a $Q$-symmetric operator is:
$$Q(U_\lambda f, U_\lambda g) = Q(f, g) \quad \forall f, g \in \mathcal{S}, \; \lambda \in \mathbb{R}^*_+.$$

If this holds, the infinitesimal generator $H_C$ of the representation $(U_\lambda)$ is
automatically $Q$-symmetric (standard argument: differentiate at $\lambda = 1$).

**Why it is not immediate.** The form $Q(f,g) = \mathcal{W}(f*\tilde{g})$ contains three types
of terms:
- A spectral term: $\sum_\rho \widehat{f*\tilde{g}}(\rho)$.
- Archimedean terms: $-\widehat{f*\tilde{g}}(0)\log\pi - \widehat{f*\tilde{g}}(1)\log\pi + \ldots$
- Arithmetic-prime terms: $\sum_{p,n} \frac{\log p}{p^{n/2}} (f*\tilde{g})(p^n) + \ldots$

Invariance $Q(U_\lambda f, U_\lambda g) = Q(f,g)$ under $(U_\lambda f)(x) = f(\lambda^{-1}x)$
requires that each of these terms be invariant separately, or that the variations
cancel each other. The arithmetic term transforms as:
$$(f*\tilde{g})(p^n) \mapsto (U_\lambda f * \widetilde{U_\lambda g})(p^n) = (f*\tilde{g})(\lambda^{-1} p^n),$$
which modifies the evaluation argument at the primes. Global invariance is not obvious.

**Status:** Pending proof. It constitutes a central result independent of
Phase 26, not a corollary of the other parts. Its proof requires the transformation
property of $\mathcal{W}$ under multiplicative change of variable, which relates
to the Weil formula in Tate (adelic) version.

---

## 3. The bridge theorem: precise formulation

**Definition 26-C.1** (Non-real spectrum in a Pontryagin space). Let $T$ be a
$Q$-self-adjoint operator in a Pontryagin space $(\mathcal{K}, Q)$ with negative index κ < ∞.
The Kreĭn–Langer spectral theorem (1963, 1978; cf. Azizov–Iokhvidov 1989, §2.3) establishes:

$T$ has **at most** $\kappa$ pairs of non-real eigenvalues $\{\lambda_j, \bar\lambda_j\}$
with $\text{Im}(\lambda_j) \neq 0$, and its essential spectrum lies in $\mathbb{R}$.

**Note on "at most" vs. "exactly":** The bound is $\leq \kappa$, not $= \kappa$.
Equality requires the operator to be "maximal" in some sense, or that the
construction of the space itself guarantees that each negative direction of $Q$ produces a
complex eigenvalue. This is precisely the non-trivial claim of V.2.

**Theorem 26-C.2** (The Bridge Theorem — Working Conjecture). Under Hypothesis D with κ = 2m:

The operator $H_C$ on the Pontryagin space $(\mathcal{K}, Q)$ is $Q$-symmetric and satisfies:

**(i)** The essential spectrum of $H_C$ in $\mathcal{K}$ is $i\mathbb{R}$ (the imaginary axis), corresponding
to the zeros of $\zeta$ on the critical line.

**(ii)** The operator $H_C$ has exactly κ = 2m "complex" eigenvalues in $\mathcal{K}$
(in the sense of the Kreĭn–Langer spectral theorem), given by:
$$\text{Complex eigenvalues of }H_C = \{b_j + i\gamma_j : j=1,\ldots,m\} \cup \{-b_j + i\gamma_j\}$$
where $\rho_j = (1/2+b_j)+i\gamma_j$ are the off-line zeros.

**(iii)** The multiplicity of each complex eigenvalue is 1 (simple zeros of $\zeta$, if they are simple).

**(iv)** The Kreĭn negative index of the operator $H_C$ on $\mathcal{K}$ coincides with the negative
index of the form $Q$: $\text{neg.ind}_Q(H_C) = \kappa = 2m$.

**Corollary 26-C.3.** The Bridge Theorem implies:
$$\kappa = 0 \iff H_C \text{ is } Q\text{-self-adjoint with spectrum in } i\mathbb{R} \iff \text{RH.}$$

*Direct equivalence:* RH ↔ κ = 0 (Papers P31–P33) ↔ Q is positive semidefinite (Weil 1952)
↔ the Kreĭn space $\mathcal{K}$ is a Hilbert space ↔ $H_C$ has no complex eigenvalues
↔ $H_C$ is genuinely self-adjoint on $H$.

---

## 4. Status of each part of the bridge theorem

| Part | Content | Status |
|-------|-----------|--------|
| (i): Essential spectrum = $i\mathbb{R}$ | On-line zeros ↔ essential spectrum of $H_C$ | Plausible, not rigorous (depends on the realization of $H_C$) |
| (ii): 2m complex eigenvalues | Off-line zeros ↔ Kreĭn eigenvalues | **Not proved. This is the central claim.** |
| (iii): Multiplicity 1 | Simple zeros of $\zeta$ | Implicit, conditional |
| (iv): neg.ind$_Q(H_C)$ = κ | Kreĭn-Pontryagin compatibility | Formal but not rigorous |

---

## 5. The central technical obstacle

**The operator $H_C$ in $L^2(C_\mathbb{Q})$ versus in $\mathcal{K}$.**

In $L^2(C_\mathbb{Q})$ (positive inner product), $H_C$ is formally symmetric but its
self-adjoint extension is problematic: the space $C_\mathbb{Q}$ is not compact, and the trace
formula has logarithmic divergences that must be regularized.

In $\mathcal{K}$ (inner product $Q$), the problem transforms: $Q$ already incorporates the Weil formula
(which regularizes the divergences) and $H_C$ may be better behaved as a $Q$-symmetric operator.

**The precise technical problem:**

Define $\mathcal{K}$ as the completion of $\mathcal{S}(\mathbb{R}^*_+)$ with respect to the norm:
$$\|f\|_{\mathcal{K}}^2 = |Q(f,f)| = |\mathcal{W}(f * \tilde{f})|.$$

**Obstacle:** If $Q(f,f) = 0$ for $f \neq 0$ (isotropic vectors), the norm degenerates.
In a Pontryagin space, isotropic vectors are $Q$-perpendicular to themselves
but not necessarily null. The quotient $\mathcal{K}/\text{ker}(Q)$ may be the correct space.

**Proposition 26-D.1** (Existence of the Pontryagin space). If the form $Q$ has finite
degeneracy rank (i.e., ker$(Q)$ is finite dimensional) and finite negative index κ = 2m,
then $\mathcal{K}$ is a Pontryagin space of index κ in which $H_C$ can be defined
as a densely defined operator.

*Status:* Requires verifying that ker$(Q)$ is finite dimensional and that $H_C$ preserves the domain
of $Q$. This is part of the technical work of Phase 26.

---

## 6. The structure of Phase 26 — correction of priorities

**Post-audit correction:** The four items are not equivalent. V.2 is the
main objective of Phase 26, not a subsidiary verification item.

The correct classification:

| Item | Real classification | Dependency |
|---|---|---|
| V.1 ($Q$-symmetry of $H_C$) | Independent central result | — |
| **V.2** (zeros ↔ complex eigenvalues) | **Main objective of Phase 26** | The entire bridge rests here |
| V.3 (neg.ind($H_C$) = κ) | Consequence | Depends on V.2 + Kreĭn–Langer |
| V.4 (dimension of the eigenspace) | Algebraic consequence | Depends on V.2 and V.3 |

V.2 is not a "technical calculation". It contains the main obstacle: the candidate
eigenvectors ($f_j = x^{b_j+i\gamma_j}$) are not in $L^2(C_\mathbb{Q})$, and the form $Q$ is not
well defined on them. It requires a distributional extension of $Q$ or a localization. See `phase-26-krein-connes-bridge/01-attack-V2.md`.

For the Bridge Theorem to be a concrete mathematical goal (not just an idea), we need
to verify the following four items — with the caveat that V.2 is the central one:

### Item 26-V.1: Is $H_C$ $Q$-symmetric?

Condition: $Q(H_C f, g) = Q(f, H_C g)$ for $f,g$ in a dense domain.

*Reduction.* By definition $Q(f,g) = \mathcal{W}(f*\tilde{g})$. Then:
$$Q(H_C f, g) = \mathcal{W}((H_C f)*\tilde{g}) \stackrel{?}{=} \mathcal{W}(f*(H_C g)^{\sim}).$$

If $H_C$ acts as $(H_C f)(x) = -ix\partial_x f(x)$, then $(H_C f)*\tilde{g}(y)$:

By Mellin convolution: $\widehat{H_C f * \tilde{g}}(s) = \hat{H_C f}(s) \cdot \hat{\tilde{g}}(s)$.
And $\hat{H_C f}(s) = (1/2-s)\hat{f}(s)$ (the Euler operator in Mellin changes s to s-1/2 ... ).

This needs to be computed explicitly. The $Q$-symmetry depends on the functional identity:
$$\sum_\rho [(s-\rho)\hat{f}(s)]|_{s=\rho} \hat{\tilde{g}}(\rho) = \sum_\rho \hat{f}(\rho)[(1-\rho)\hat{\tilde{g}}(1-\rho)]|$$

This requires careful computation. **Pending verification.**

### Item 26-V.2: Do the complex eigenvalues of $H_C$ on $\mathcal{K}$ correspond to the off-line zeros?

If $\rho_j = (1/2+b_j)+i\gamma_j$ is a zero of $\zeta$ off the line, then $b_j + i\gamma_j$
should be an eigenvalue of $H_C$ on $\mathcal{K}$.

*Direct verification:* We need to find $f_j \in \mathcal{K}$ such that $H_C f_j = (b_j+i\gamma_j) f_j$.
The natural candidate is $f_j(x) = x^{b_j+i\gamma_j}$ (a character of $\mathbb{R}^*_+$). Then:
$(H_C f_j)(x) = -ix\partial_x(x^{b_j+i\gamma_j}) = -i(b_j+i\gamma_j)x^{b_j+i\gamma_j} = (b_j+i\gamma_j)(-i)f_j$.

There is a factor $(-i)$ of difference (depends on conventions: whether $H_C = x\partial_x$ vs $-ix\partial_x$).
With the convention $H_C = -ix\partial_x$: eigenvalue = $-i(b_j+i\gamma_j) = \gamma_j - ib_j$... which has
$\text{Im}(\gamma_j-ib_j) = -b_j \neq 0$ (not in the real spectrum), consistent.

**The verification also requires:** that $f_j = x^{b_j+i\gamma_j}$ be in $\mathcal{K}$,
i.e., that $Q(f_j, f_j)$ be defined and finite. This involves:
$$Q(f_j, f_j) = \mathcal{W}(f_j * \tilde{f}_j).$$

The convolution $f_j * \tilde{f}_j$ is related to the values of $|\zeta|$ at $\rho_j$, which
is 0 (since $\rho_j$ is a zero). This suggests that $Q(f_j,f_j) = 0$, i.e., $f_j$ is an
isotropic vector. This is a delicate technical point.

**Status: pending, with a concrete calculation to be carried out.**

### Item 26-V.3: Is the negative index of $H_C$ on $\mathcal{K}$ equal to κ?

By the Kreĭn–Langer theorem for operators on Pontryagin spaces: if $H_C$ is
$Q$-self-adjoint on $\mathcal{K}$ with negative index κ, then it has exactly κ complex
eigenvalues (in the complex plane, off the real axis, counted with multiplicity).

The identification neg.ind$(H_C)$ = κ = neg.ind$(Q)$ = 2m would be the heart of the bridge theorem.

**Status: needs (i) making $H_C$ rigorous as an operator on $\mathcal{K}$, (ii) applying the Kreĭn–Langer spectral theorem.**

### Item 26-V.4: Does Item 26-V.2 produce an eigenspace of the correct dimension?

For m = 1 (a single orbit): 4 off-line zeros {ρ₁⁺, ρ̄₁⁺, ρ₁⁻, ρ̄₁⁻}. In the
parametrization by $t$ (where $t = -i(s-1/2)$): 4 complex zeros of $H_0$. In $\mathcal{K}$:
2 complex eigenvalues of $H_C$ (by the symmetry $s ↔ 1-s$ of $\xi$, which halves the count).

Dimension of the eigenspace: 2 (the 2 complex eigenvalues irreducible under the functional symmetry).

---

## 7. Result of the analysis: can the bridge theorem be written?

**Answer: the Bridge Theorem is a coherent mathematical conjecture, not yet a
verifiable goal.**

Theorem 26-C.2 is formulated as a working conjecture, with the claims correctly
identified. But the program reduces to a single central problem:

> **Rigorously construct the space $\mathcal{K}$ and prove the spectral correspondence of V.2.**

Everything else (V.1, V.3, V.4, the adelic factorization of 26-B) depends on that.

**Frank status of each component before starting 26-A:**

| Component | Real status |
|---|---|
| $\mathcal{K}$ as a Pontryagin space | **Not constructed.** Conditional on (a) finite ker$Q$, (b) completeness, (c) decomposition. |
| $Q(U_\lambda f, U_\lambda g) = Q(f,g)$ | **Not proved.** Independent central result (extended V.1). |
| Complex eigenvalues = off-line zeros | **Not proved.** This is V.2; requires $f_j \in \mathcal{K}^+$ (distributional extension). |
| "Exactly κ" complex eigenvalues | Consequence of V.2; Kreĭn–Langer gives "at most κ" for free. |

**90% of Phase 26's effort must go to V.2.** We do not advance to 26-B or the adelic
part until V.2 survives a complete functional audit. See `phase-26-krein-connes-bridge/01-attack-V2.md`.

---

## 8. What the bridge theorem gives the program

If Theorem 26-C.2 is proved:

**Before the bridge:** RH ↔ κ = 0 (Kreĭn) and RH ↔ $H_C$ is self-adjoint (Connes) are two
reformulations of RH, but in different spaces and languages, with no direct connection.

**After the bridge:** RH ↔ κ(Q) = 0 ↔ neg.ind$(H_C)$ = 0 are the SAME reformulation
in two languages, with an explicit dictionary. This allows using tools of one program
in the other:
- Kreĭn tools (factorization, indefinite spectrum) → to study $H_C$.
- Adelic tools (Connes) → to try to prove κ = 0.

**The working hypothesis for Phase 26:**

> The adelic space $C_\mathbb{Q} = \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$ has enough arithmetic structure to
> force neg.ind$(H_C) = 0$, i.e., to make $H_C$ genuinely self-adjoint.
>
> This structure comes from the **local-global factorization** of the group $C_\mathbb{Q}$:
> $C_\mathbb{Q} \cong \prod_p \mathbb{Z}_p^* \times \mathbb{R}^*_+$
> and from the product formula of the function $\zeta$ that decomposes $Q$ into local factors.

---

## 9. Phase 26 — Work structure

Given that the bridge theorem is formulated, Phase 26 proceeds as follows:

**26-A:** Verification of Items V.1–V.4 (technical calculations, weeks of work).

**26-B:** If the items are verified: look for adelic tools that imply neg.ind = 0.
   - Local/global class field theorem and its action on $\mathcal{K}$.
   - The Euler-local factorization of $Q = \prod_p Q_p$ (if it exists).

**26-C:** If the items are not verified: precise diagnosis of why the bridge fails, and
   correct reformulation.

**Success criterion of Phase 26:**
> Either: Theorem 26-C.2 is proved and the path toward RH via adelic tools
> is clear.
>
> Or: it is proved that the bridge cannot be built in this form, with a precise reason,
> and the necessary correction is identified.

**Neither of the two is a failure:** the first opens the door, the second refines the question.
