# 107.152 -- No-go for the naive abelian linearization of the 2026 stalks

## 1. Result

Connes--Consani's 2026 absolute structure sheaf has closed stalk

\[
 \mathcal F_p=\mathbb F_1[T^{M_p}],
 \qquad M_p=\mathbb Z[1/p]_+.
\]

The canonical ordinary additive linearization sends a monoid algebra to
the free abelian monoid ring

\[
 \mathbb F_1[T^{M_p}]
 \longmapsto
 \mathbb Z[T^{M_p}].
\]

Equipping this group with the coefficient \(\ell^1\) mass inherited from
the 2022 integer-dimension construction gives infinite
\(\mathbb S[\pm1]\)-dimension for every positive radius.  The same is
true, a fortiori, for the square stalk

\[
 \mathbb Z[T^{M_p\oplus M_p}].
\]

Therefore direct base extension of the full 2026 stalk cannot provide
the bounded Eilenberg--MacLane Cech terms required by 107_151.

## 2. Primitive-ray lemma

Let \(I\) be any set and let

\[
 L_I=\bigoplus_{i\in I}\mathbb Z e_i,
 \qquad
 \left\|\sum_i a_i e_i\right\|_1=\sum_i|a_i|.
\]

Let \(B_I(n)=\{x\in L_I:\|x\|_1\le n\}\), and define linear generation
with coefficients in \(\{0,\pm1\}\) and the same mass budget as in
Connes--Consani.

**Lemma.** If \(n\ge1\), every generating family for \(B_I(n)\) has
cardinality at least \(|I|\).

**Proof.**  Since \(n\ge1\), every basis vector \(e_i\) belongs to
\(B_I(n)\).  Hence the integral span of any linearly generating family
contains every \(e_i\), and therefore equals \(L_I\).  The free abelian
group \(L_I\) has rank \(|I|\), so a generating family has cardinality
at least \(|I|\).  For \(n=1\), the stronger primitive-ray statement
also holds: the mass budget forces the unique nonzero summand
\(\pm e_i\). \(\square\)

Since \(M_p\) is countably infinite, the integer dimension of the
radius-one ball in \(\mathbb Z[T^{M_p}]\) is already infinite.  Since
\(M_p\oplus M_p\) is also countably infinite, passing to the square does
not repair the problem.

## 3. Consequence for the Cech lift

107_151 shows that middle tolerance cohomology is available after the
Cech terms are embedded in bounded Eilenberg--MacLane modules.  The
most direct candidate was to linearize the newly published absolute
stalks.  The theorem above rejects that candidate before any quotient
or \(H^1\) calculation:

\[
 \dim_{\mathbb S[\pm1]}
 \bigl\|\mathbb Z[T^{M_p\oplus M_p}]\bigr\|_n
 =\infty
 \qquad(n\ge1).
\]

A viable lift must therefore impose a geometrically defined compact
support, quotient, completion with a different dimension theory, or a
non-free additive realization.  The cutoff must come from the divisor
or topology before dimension is computed; it cannot be chosen after
examining the desired Riemann--Roch value.

## 4. Scope

This is a no-go for the canonical free abelian linearization with CC's
published mass.  It does not rule out the original spherical stalk, a
derived completion, or a divisor-dependent coherent submodule.  It
does prove that the phrase "extend scalars to \(\mathbb Z\) and apply
107_151" is not a construction of the square cohomology.
