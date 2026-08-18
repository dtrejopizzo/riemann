# 106.209 — The cross-root intersection falsifier

## 1. Purpose

The diagonal finite-root calculation gives

\[
 \Gamma_n^2=n,
 \qquad
 (\Gamma_n-nF_{\mathrm v}-F_{\mathrm h})^2=-n.
 \tag{1}
\]

This does not determine the sign of finite linear combinations.  The
precommitted next test is to construct the cross-intersection from a
common finite refinement and inspect the primitive two-row Gram matrix.

The common-refinement count is canonical and equals \(\gcd(m,n)\).  It
fails the primitive Hodge sign for every pair \(m\ne n\).  In particular,
the first pair \((m,n)=(2,3)\) already produces one positive primitive
direction.  According to the stop rule, the unmodified finite-root
overlap pairing cannot be the required arithmetic intersection form.

## 2. Common-refinement root strata

Fix \(M,m,n\geq1\), and put

\[
 L=\operatorname{lcm}(m,n).
 \tag{2}
\]

Inside the cyclic common refinement

\[
 R_{ML}=\mathbb Z/(ML)\mathbb Z,
 \tag{3}
\]

there is a unique subgroup \(S_m\) of order \(Mm\) and a unique subgroup
\(S_n\) of order \(Mn\).  Explicitly,

\[
 S_m=\frac{L}{m}R_{Mm},
 \qquad
 S_n=\frac{L}{n}R_{Mn}.
 \tag{4}
\]

These are the two root strata obtained by pulling the levels \(Mm\) and
\(Mn\) into the same finite root set.

### Definition 2.1 — Cross-root incidence pairing

Use the same base-cardinality normalization that gave the diagonal row:

\[
 I_M(\Gamma_m,\Gamma_n)
 :=\frac1M|S_m\cap S_n|.
 \tag{5}
\]

For \(m=n\), this reduces to

\[
 I_M(\Gamma_n,\Gamma_n)=\frac1M|S_n|=n,
 \tag{6}
\]

so (5) is a bilinear common-refinement extension of the previously
verified self-pairing, not a new diagonal normalization.

### Theorem 2.2 — Exact cross intersection

For all \(M,m,n\geq1\),

\[
 \boxed{I_M(\Gamma_m,\Gamma_n)=\gcd(m,n).}
 \tag{7}
\]

#### Proof

A finite cyclic group has exactly one subgroup of each order dividing its
cardinality, and the intersection of its subgroups of orders \(a\) and
\(b\) has order \(\gcd(a,b)\).  Therefore

\[
 |S_m\cap S_n|
 =\gcd(Mm,Mn)
 =M\gcd(m,n).
\]

Division by \(M\) gives (7). \(\square\)

The result is independent of the auxiliary level and uses no asymptotic
limit.

## 3. The primitive two-row criterion

Write

\[
 \Gamma_m^0=\Gamma_m-mF_{\mathrm v}-F_{\mathrm h},
 \qquad
 \Gamma_n^0=\Gamma_n-nF_{\mathrm v}-F_{\mathrm h}.
 \tag{8}
\]

Using

\[
 \Gamma_rF_{\mathrm v}=1,
 \qquad
 \Gamma_rF_{\mathrm h}=r,
 \qquad
 F_{\mathrm v}F_{\mathrm h}=1,
 \tag{9}
\]

one obtains

\[
 \Gamma_m^0\Gamma_n^0
 =I_M(\Gamma_m,\Gamma_n)-(m+n).
 \tag{10}
\]

Hence the primitive Gram matrix is

\[
 G_{m,n}^{0}
 =\begin{pmatrix}
 -m & \gcd(m,n)-(m+n)\\
 \gcd(m,n)-(m+n) & -n
 \end{pmatrix}.
 \tag{11}
\]

A symmetric matrix with negative diagonal entries is negative
semidefinite precisely when its determinant is nonnegative.  Thus the
required two-row Hodge condition is

\[
 \left|I_M(\Gamma_m,\Gamma_n)-(m+n)\right|
 \leq\sqrt{mn}.
 \tag{12}
\]

This is the finite-root analogue of a Weil square-root bound.

### Theorem 3.1 — Universal cross-row failure

If \(m\ne n\), then

\[
 \boxed{
 \left|\gcd(m,n)-(m+n)\right|>\sqrt{mn},}
 \tag{13}
\]

and consequently

\[
 \boxed{\det G_{m,n}^{0}<0.}
 \tag{14}
\]

The primitive span of \(\Gamma_m^0,\Gamma_n^0\) has signature \((1,1)\).

#### Proof

Assume without loss of generality that \(m<n\), and put
\(g=\gcd(m,n)\).  Since \(g\leq m\),

\[
 m+n-g\geq n>\sqrt{mn}.
\]

This is (13).  Therefore

\[
 \det G_{m,n}^{0}
 =mn-(m+n-g)^2<0.
\]

A real symmetric two-by-two matrix with negative determinant has one
positive and one negative eigenvalue. \(\square\)

Thus the failure is not exceptional and cannot be repaired by increasing
the finite level \(M\).

## 4. The first falsifying pair

For \(m=2\) and \(n=3\), the common-refinement intersection is

\[
 I_M(\Gamma_2,\Gamma_3)=1.
 \tag{15}
\]

The primitive matrix is

\[
 G_{2,3}^{0}
 =\begin{pmatrix}-2&-4\\-4&-3\end{pmatrix},
 \qquad
 \det G_{2,3}^{0}=6-16=-10.
 \tag{16}
\]

Its eigenvalues are

\[
 \frac{-5\pm\sqrt{65}}2,
 \tag{17}
\]

one of which is positive.  The route is therefore falsified by a single
finite calculation, before Gamma or a cofinal completion is introduced.

Balancing each row does not change the inertia.  After replacing
\(\Gamma_r\) by \(r^{-1/2}\Gamma_r\), the diagonal entries become \(-1\)
and the off-diagonal entry becomes

\[
 \frac{\gcd(m,n)-(m+n)}{\sqrt{mn}},
 \tag{18}
\]

whose modulus is greater than one whenever \(m\ne n\).

## 5. Connected extraction does not repair the sign

For distinct prime towers the Eulerian projector removes the disconnected
orbit product from the cyclic trace.  If one were to replace the
cross-incidence value in (10) by zero, the primitive cross term would
become \(-(m+n)\), which has even larger modulus.  Thus connected
extraction cannot repair (13).

More importantly, such a replacement would mix two different products:
the Rosati pairing uses categorical composition and transpose, whereas
the Eulerian idempotent acts on the disjoint-union Hopf product.  The
projector is not multiplicative and therefore cannot be inserted into
the Rosati product to alter the cross-intersection.

## 6. Consequence of the stop rule

The calculation separates the valid pieces from the failed extension.

The following remain correct source constructions:

* genuine CRT fiber products of distinct root towers;
* multiplicative covering degree;
* the diagonal incidence identity \(\Gamma_n^2=n\);
* the balanced coefficient \(n^{-1/2}\);
* relative torsion \(\log p\) and the local von Mangoldt mass;
* the polar hyperbolic plane;
* connected Euler extraction at the cyclic trace.

What fails is the proposed promotion of normalized subgroup overlap to a
global arithmetic intersection pairing.  Its diagonal rows have the
correct sign, but its first off-diagonal block already has an additional
positive primitive direction.

According to the precommitted rule, no Gamma correction or limiting
completion is added to rescue this pairing.  Any future geometric route
must supply a genuinely different cross-intersection operation before
the finite-root rows are assembled.  In particular, it must contain
nonlocal factorization or correspondence data capable of replacing the
\(\gcd(m,n)\) overlap by a value in the interval

\[
 m+n-\sqrt{mn}
 \leq I(\Gamma_m,\Gamma_n)
 \leq m+n+\sqrt{mn}.
 \tag{19}
\]

That requirement is not met by root-subgroup incidence counting.

## 7. Status

Proved unconditionally and finitely:

* the exact common-refinement formula
  \(I(\Gamma_m,\Gamma_n)=\gcd(m,n)\);
* the exact two-row Hodge criterion (12);
* failure of that criterion for every distinct pair \(m,n\);
* the explicit first counterexample \((2,3)\), with determinant \(-10\);
* invariance of the failure under balanced normalization;
* impossibility of repairing it by Eulerian compression.

Verdict:

> The normalized finite-root overlap pairing is not the arithmetic
> intersection product required by the Weil--Hodge route.  The route in
> this specific form stops at the cross-intersection test.
