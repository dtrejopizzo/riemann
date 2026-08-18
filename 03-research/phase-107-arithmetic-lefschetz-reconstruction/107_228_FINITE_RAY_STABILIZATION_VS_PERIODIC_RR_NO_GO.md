# 107.228 -- Finite-ray stabilization is incompatible with periodic RR

## 1. Published input

For the periodic orbit

\[
 C_p=\mathbb R_+^*/p^{\mathbb Z},
\]

Connes--Consani define, for every divisor \(D\),

\[
 H^0(D)^\rho
 =\{f\in H^0(D):\|f\|_p\leq\rho\}
\]

and the continuous dimension

\[
 \mathrm{cdim}\,H^0(D)
 =\lim_{n\to\infty}
 p^{-n}\mathrm{tdim}\,H^0(D)^{p^n}.
 \tag{1.1}
\]

Their periodic Riemann--Roch theorem states that

\[
 \mathrm{cdim}\,H^0(D)=\deg D
 \qquad(\deg D\geq0).
 \tag{1.2}
\]

These are Definition 5.3 and Theorem 5.4 of *The Scaling Site*,
arXiv:1507.05818v2. The verifier reads those statements from the local
source file rather than installing them as Phase 107 assumptions.

## 2. No-go theorem

### Theorem 2.1

Let \(D\) be a divisor on \(C_p\) with \(\deg D>0\), and put

\[
 d_n=\mathrm{tdim}\,H^0(D)^{p^n}.
\]

Then \((d_n)\) is unbounded. In particular, neither the filtered
modules nor their topological dimensions can stabilize at a finite
Frobenius depth.

### Proof

If \(d_n\) were bounded by \(M\), then

\[
 0\leq p^{-n}d_n\leq Mp^{-n}\longrightarrow0.
\]

Equations (1.1)--(1.2) instead give

\[
 p^{-n}d_n\longrightarrow\deg D>0,
\]

a contradiction. \(\square\)

### Corollary 2.2

The requirement in 107_155 Section 4 that **every** finite-support
divisor admit only finitely many monomial rays cannot hold for a
realization of the full published periodic \(H^0(D)\) which preserves
its filtration and topological dimension.

Indeed 107_155 proves that finite-ray support is equivalent to eventual
stabilization in its coefficient-mass linearization, while Theorem 2.1
proves that stabilization is impossible for every positive-degree
periodic divisor.

## 3. Correction of the Phase 107 gate

Two distinct Riemann--Roch theories had been conflated:

1. On \(\overline{\mathrm{Spec}\,\mathbb Z}\), the 2022
   \(H^0(a\{\infty\})\) is the bounded integer interval
   \([-e^a,e^a]\cap\mathbb Z\), with finite integer dimension.
2. On \(C_p\), slopes lie in the dense group
   \(H_p=\mathbb Z[1/p]\); denominator depth is unbounded and RR uses
   the normalized continuous limit (1.1).

The square sought by the 2018 strategy is the square of the Scaling
Site. Consequently, finite stages are legitimate computational models,
but eventual finite stabilization is not a legitimate existence
condition for its full divisor cohomology.

The corrected local requirement is:

\[
 \boxed{
 \text{construct a compatible pro-filtration and prove existence of a
 renormalized dimension limit.}}
 \tag{3.1}
\]

The rooted sector of 107_158 may still stabilize because it records a
finite discrete label. It cannot replace the nonstabilizing slope
sector which carries the positive continuous dimension.

## 4. Scope

This closes the finite-ray-stabilization route as a model of the full
periodic \(H^0\). It does not close row (a), construct the square, or
prove a two-dimensional RR formula.

For degree-zero divisors alone, (1.2) does not force unboundedness.
However, a surface RR theory must be defined on positive twists as
well; restricting the entire sheaf theory to degree zero cannot evade
the obstruction.

The surviving construction problem is now narrower: extend the
one-orbit normalized filtration to the two-ruling square and construct
its middle tolerant cohomology before taking a normalized limit. No
new finite-depth cutoff is admissible as a substitute.

## 5. Exact falsifier

107_228_finite_ray_stabilization_vs_periodic_rr_no_go.py reads the
published TeX source, checks the filtration, limit, and positive-degree
theorem, and tests bounded versus correctly scaled dimension sequences
at the fixed primes \(2,3,5,7,11\). It returns NO if the source
statements are absent, if a bounded sequence retains positive normalized
dimension, or if the growing negative control is rejected.

