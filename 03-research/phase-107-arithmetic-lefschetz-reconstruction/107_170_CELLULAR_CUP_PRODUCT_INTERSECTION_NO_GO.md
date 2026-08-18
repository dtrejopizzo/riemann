# 107.170 -- The rooted cellular cup product cannot be the intersection theory

## 1. Distinction forced by 107_169

The rooted cellular complex of 107_169 has the correct three-term
cohomological shape

\[
 H^0\cong\mathbb Z,qquad H^1\cong\mathbb Z^2,qquad
 H^2\cong\mathbb Z.
\]

This is useful for constructing middle cohomology.  It is not the
cohomology ring required to intersect divisors on a complex surface.

## 2. No-go

Let \(u,v\) be the two degree-one generators of the torus.  Its
cohomology ring is

\[
 H^\bullet(T^2;\mathbb Z)=\bigwedge^\bullet\langle u,v\rangle.
\]

Every degree-two class is a multiple of \(u\wedge v\), and

\[
 (u\wedge v)\smile(u\wedge v)=0
\]

because \(H^4(T^2;\mathbb Z)=0\).

**Theorem.**  No assignment of divisor first Chern classes to
\(H^2\) of the rooted cellular torus can recover a nonzero bilinear
intersection pairing by ordinary cup product.

**Proof.**  For any divisor classes \(c_1(D),c_1(E)\in H^2\), their cup
product lies in \(H^4=0\).  Hence every proposed intersection is zero.
\(\square\)

This is not merely a self-intersection problem: distinct divisor
classes also pair to zero.

## 3. Real contradiction with the Weil calibration

For the fixed control curve

\[
 E/\mathbb F_5:\quad y^2=x^3+x+1,
\]

direct counting gives \(N_1=9\).  The geometric calibration of Paper 0
has

\[
 \Gamma_1\cdot\Delta=N_1=9.
\]

The ordinary cellular cup product would give zero.  Therefore it cannot
be the intersection realization even on the already proved
function-field control.

## 4. Consequence

The roles of the current objects must remain separated:

1. `107_169` supplies an integral, mass-controlled three-term complex
   for additive/tolerance cohomology.
2. It supplies no divisor intersection theory.
3. The required intersection must use extra transverse or relative
   geometry not retained by the de Rham retraction to \(T^2\).

This agrees with the 2018 strategy, which identifies the desired
self-intersection as a **relative trace** on the difference between the
adele class space and the ideles.  A successful route must construct
either:

1. a genuine real-four-dimensional/complex-two-dimensional
   compactification with a nonzero top class; or
2. a relative cyclic/Fredholm fundamental class whose pairing replaces
   ordinary \(H^4\).

The additive cellular complex may still be a coefficient resolution in
either route.  It cannot be promoted to rows (c) or (d) by itself.

## 5. Falsifier

The verifier computes the exterior cohomology ring symbolically and
independently counts the points of the fixed elliptic control over
\(\mathbb F_5\).  `VERDICT: YES` requires the cellular intersection to
be zero and the real geometric intersection to be nonzero.
