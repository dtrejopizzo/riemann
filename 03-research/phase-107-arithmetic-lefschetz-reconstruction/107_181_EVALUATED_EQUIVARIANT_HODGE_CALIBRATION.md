# 107.181 -- Evaluated inverse-Euler weights preserve the Hodge sign

## 1. A genuine surface over the arithmetic base

Let

\[
 \mathcal S=mathbb P^1_{\mathbb Z}\times_{\mathbb Z}
 \mathbb P^1_{\mathbb Z}.
\]

Every geometric fibre is the smooth projective surface
\(S=\mathbb P^1\times\mathbb P^1\).  Let \(A,B\) be the two ruling
classes.  Their intersection ring satisfies

\[
 A^2=B^2=0,qquad A\cdot B=1.
 \tag{1.1}
\]

Choose

\[
 H=A+B,qquad D=A-B.
\]

Then

\[
 H^2=2,qquad D\cdot H=0,qquad D^2=-2.
 \tag{1.2}
\]

Thus \(D\) spans the primitive Neron--Severi direction and realizes the
strict Hodge sign.

## 2. Numerical evaluation of the localized class

For a local scaling parameter \(u\neq1\), `107_178` constructs the
localized coefficient \((1-u)^{-1}\).  Although `107_179` proves that
there is no universal ring-valued forgetful map at \(t=1\), evaluation
at a fixed local parameter followed by normalized absolute value is a
well-defined positive real number

\[
 w_v(u)={1\over|1-u|_v}>0.
\]

Define the evaluated primitive class

\[
 M_{v,u}=w_v(u)D.
\]

Using (1.2),

\[
 M_{v,u}\cdot H=0,
 \qquad
 M_{v,u}^2=-2w_v(u)^2<0.
 \tag{2.1}
\]

For \(u=1+p^k\), this becomes

\[
 M_{p,u}^2=-2p^{2k}.
\]

Hence the inverse-Euler localization weight itself does not obstruct
Hodge negativity.  Once a localized boundary class is realized as a
real multiple of a genuine primitive divisor direction, the ordinary
Hodge sign survives exactly.

## 3. Finite combinations

For any finite family of local parameters evaluated in the same
primitive direction,

\[
 M=\left(\sum_j c_jw_{v_j}(u_j)\right)D,
\]

one has

\[
 M\cdot H=0,
 \qquad
 M^2=-2\left(\sum_jc_jw_{v_j}(u_j)\right)^2\le0.
 \tag{3.1}
\]

Equality holds exactly when the evaluated coefficient vanishes.  This
is the correct radical pattern in the rank-one calibration.

## 4. Result and missing theorem

This closes a possible sign obstruction between `107_178` and row (d):
positive normalized evaluations of inverse Euler classes are compatible
with the Hodge cone on an actual surface over \(\mathbb Z\).

It does **not** construct the Phase-107 global divisor.  In particular,
it does not prove that the placewise boundary classes all map to one
primitive direction, that their infinite Green variation converges, or
that the source radical is exactly the equality locus.  The missing
theorem is now sharper:

\[
 \boxed{
 \text{construct a global real evaluation map from the renormalized
 boundary class to a primitive adelic divisor class}.}
\]

If such a map lands in an existing adelic intersection theory, Hodge
negativity need not be reproved; (2.1) shows the local weights preserve
it.  If it remains only in localized equivariant arithmetic Chow, a
corresponding global index theorem is still required.

## 5. Falsifier

The verifier constructs Sage's actual toric
\(\mathbb P^1\times\mathbb P^1\), checks its cohomology relations, and
tests (2.1)--(3.1) for p-adic and archimedean inverse-Euler weights and
signed finite combinations.  Any positive primitive square returns
`VERDICT: NO`.
