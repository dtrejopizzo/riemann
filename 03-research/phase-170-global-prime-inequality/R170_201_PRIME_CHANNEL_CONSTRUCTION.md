# R170_201 — Construction of prime channels and the exact cost of positivity

**Construction and obstruction proved; D remains OPEN.**

Requested work: attempt to construct a positive structure from the
integers, without a literature search. This works with the local corpus and
explicit algebra. No scientific priority or absolute novelty is claimed.

## 1. What is being repaired

The square of a sum of prime translations produces ratios p^k/q^l.
R166_502 proves that Möbius/Selberg does not remove them. Instead of
repeating that connection, we build a space with one channel per prime and
a factorization that preserves **the whole tower p^k**. We also compute
the minimal price of replacing the archimedean term by a constant.

The goal of this essay is twofold: remove the ratios between primes
without losing the linear current, and check whether the remaining cost
can be absorbed into the archimedean and polar terms.

## 2. A complete prime tower has an explicit root

In H=L²(ℝ), let U_pF(t)=F(t−log p), unitary. Set

$$r_p=p^{-1/2},\quad \ell_p=\log p,\qquad
V_p=\ell_p r_pU_p(I-r_pU_p)^{-1}
=\sum_{k\ge1}\ell_p r_p^k U_p^k.$$

The series converges in norm because r_p<1. Define

$$C_p=\frac{2\ell_p r_p}{1-r_p},\qquad
b_p=\frac{\ell_p r_p(1+r_p)}{1-r_p},\qquad
D_p=\sqrt{b_p}(I-U_p)(I-r_pU_p)^{-1}.$$

**Proposition 1.** Exactly,

$$D_p^*D_p=C_pI-(V_p+V_p^*).\tag{1}$$

**Proof.** All factors are commuting functions of the unitary U_p.
Multiplying by (I-r_pU_p)^*(I-r_pU_p), the right-hand numerator is

$$C_p(1+r_p^2-r_p(U_p+U_p^*))
-\ell_p[r_p(U_p+U_p^*)-2r_p^2].$$

Its coefficients are 2b_p on I and −b_p on U_p,U_p^*. This is precisely
b_p(I-U_p)^*(I-U_p). The denominator is invertible. ∎

This yields a positive root with no zeros of ζ introduced and no
assumption on the sign of W. The current's coefficients are exactly
Λ(p^k)/√(p^k).

## 3. Assembly with no ratios between primes

For a finite set P of primes, build

$$\mathcal H_P=\bigoplus_{p\in P}H,\qquad
\mathcal D_PF=(D_pF)_{p\in P},\qquad C_P=\sum_{p\in P}C_p.$$

By (1),

$$\|\mathcal D_PF\|^2
=C_P\|F\|^2-2\sum_{p\in P}\sum_{k\ge1}
\frac{\log p}{p^{k/2}}\Re c_F(k\log p).\tag{2}$$

No ratios p^k/q^l for p≠q appear. No supertrace, no norm subtraction,
no cohomology is used: the cancellation is obtained by separating channels
before taking the norm. The linear prime current survives intact.

For F supported in (−T,T), it suffices that P contain every prime less
than e^{2T}. The terms of each tower with k log p≥2T vanish, and (2) gives
the exact identity

$$W_T(F)=\|\mathcal D_PF\|^2+
\underbrace{\left[\mathfrak a_\infty(F)
+2\Re(A(F)\overline{B(F)})-C_P\|F\|^2\right]}_{R_P(F)},\tag{3}$$

where 𝔞_∞ is just the archimedean integral, with no prime comb.

**Constructive result:** there is an explicit Hilbert space and operator
that remove the contamination by ratios. **Limit:** the resulting equality
is (3), not W_T=‖𝒟_PF‖². The sign of the remainder is missing.

## 4. The constant cost is optimal, even with other channels

**Theorem 2.** For P finite, if

$$CI-\sum_{p\in P}(V_p+V_p^*)\ge0\quad\text{on }L^2(\mathbb R),$$

then C≥C_P. Conversely C=C_P works, by (2).

**Proof.** The continuous symbol of the sum is

$$q_P(\tau)=2\Re\sum_{p\in P}
\frac{\ell_pr_pe^{i\tau\log p}}{1-r_pe^{i\tau\log p}}.$$

At τ=0 it equals q_P(0)=C_P. If C<C_P, by continuity C−q_P is negative
on an open interval. A nonzero function whose transform is supported
there contradicts positivity. Sufficiency was already proved. ∎

The argument covers any Hilbert factorization of the **same operator
with constant compensation**, not only the chosen direct sum. It does
not cover τ-dependent compensations nor factorizations compressed into
a window. Its necessity tests have no compactly supported time window.

For the truncated current V_N=Σ_{2≤n≤N}Λ(n)n⁻¹ᐟ²U_n, the exact version is

$$C_N^{\min}=2\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n},\qquad
C_N^{\min}\|F\|^2-2\Re\langle V_NF,F\rangle
=\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}\|F-U_nF\|^2.\tag{4}$$

The necessary bound is again proved at frequency zero. Hence truncating
the towers reduces the cost but does not remove this obstruction.

## 5. The remainder cannot be another independent positive form

Let F≠0 be fixed, smooth and compactly supported. As P grows to include
all primes,

$$R_P(F)\longrightarrow-\infty.\tag{5}$$

Indeed the first two terms of R_P(F) are finite constants, while C_P
diverges. This last fact does not need the PNT: C_p≥2(log 2)/p and
Σ_p1/p diverges. To recall the elementary proof, if that sum converged,
the finite products ∏_{p≤x}(1−1/p)⁻¹ would be bounded; expanding them
contains Σ_{n≤x}1/n, a contradiction.

The same obstruction appears when taking growing windows that contain
the fixed support of F and using, in each window, its active primes.
Once the support of c_F is covered, each additional prime increases
‖𝒟_PF‖² by C_p‖F‖² and decreases R_P(F) by exactly the same amount.
The sum is preserved, but neither piece separately has a useful positive
limit.

Hence (3) is **not** a proof. Nor can it be claimed that renormalization
preserves positivity: subtracting C_P‖F‖² from a positive norm is
precisely the step that loses the sign guarantee.

## 6. What arithmetic information it actually uses

The construction preserves the exact values of Λ and all prime powers,
but its proof works for any set of dilations a_j>1 and positive weights
ℓ_j, taking r_j=a_j⁻¹ᐟ². It does not use the fact that composite integers
from different towers are identified through multiplication.

In terms of the request, we have built the Hilbert-space part but not yet
the specific mechanism of ℤ. Orthogonalization removes the ratios at the
price of also removing the interaction between primes that could carry
that information. The explicit use of log p is not enough to claim that
unique factorization enters the sign step.

## 7. Check against the corpus and scope of the contribution

- R166_502: the obstruction from ratios in V*V is the starting point.
- Phase 104, `104_15_EULER_GAMMA_COMPLEX_GATE`: the Koszul complex already
  removes ratios, but it also kills generators in cohomology. Here no
  cohomology is taken and the current survives; the diagonal cost fails.
- Phase 106, `106_104_THETA_DIVISOR_CURRENT_NORMAL_FORM`: orthogonal
  decompositions and divisorial dispersion already exist there. It is not
  claimed that introducing per-prime orthogonality is a new idea.
- R170_202 examines the alternative of introducing hidden vertices in a
  scalar network to cheapen that cost.

What this note contributes is a fully computed candidate with complete
towers, its optimal constant budget, and a proven diagnosis of why it
does not close. It is not a new proof of RH nor an exclusion of every
possible Hilbert-space construction.

**Object that is still missing:** a coupling between channels and the
archimedean/polar sector that preserves the arithmetic interactions and
jointly controls the remainder of (3). Demanding that control without
building it would amount to postulating W_T≥0 again. It is not presented
as an already-solved lemma.
</content>
