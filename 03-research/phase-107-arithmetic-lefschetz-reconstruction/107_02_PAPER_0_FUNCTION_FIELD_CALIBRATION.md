# 107.02 -- Paper 0: function-field calibration on the fixed elliptic control

## 1. Purpose

This paper executes the stop rule of 107.00 for the fixed control curve

\[
 E/\mathbb F_5:\qquad y^2=x^3+x+1.
 \tag{1.1}
\]

The goal is to recover, by explicit geometric operations on
\(S=E\times E\), the full chain

\[
 \text{Frobenius graphs}
 \longrightarrow
 \text{Lefschetz intersections}
 \longrightarrow
 \text{connected Euler extraction}
 \longrightarrow
 \text{critical balancing}
 \longrightarrow
 \text{primitive Hodge sign}.
 \tag{1.2}
\]

No truncation by closed-point degree is introduced.  The calibration is
entirely internal to the proper smooth surface \(E\times E\).

This paper proves the fixed positive elliptic control only.  After the
genus-2 audit of `107_28`, it should not be read as if it already
proved a genus-uniform source derivation of the primitive diagonal
entries.

## 2. Fixed curve and exact arithmetic anchors

Let \(O\in E(\mathbb F_5)\) be the origin of the elliptic curve.  The
projective model is smooth because the cubic \(x^3+x+1\) has nonzero
discriminant modulo \(5\).

Direct counting on the affine chart gives:

* \(x=0\): \(y^2=1\), hence two solutions.
* \(x=1\): \(y^2=3\), hence no solution.
* \(x=2\): \(y^2=1\), hence two solutions.
* \(x=3\): \(y^2=1\), hence two solutions.
* \(x=4\): \(y^2=4\), hence two solutions.

Adding the point at infinity yields

\[
 \#E(\mathbb F_5)=9,
 \qquad
 a_1=5+1-9=-3.
 \tag{2.1}
\]

Let \(F:E\to E\) be geometric Frobenius.  Its characteristic polynomial
on \(H^1_{\mathrm{et}}(E_{\overline{\mathbb F}_5},\mathbf Q_\ell)\) is

\[
 P_E(T)=T^2+3T+5.
 \tag{2.2}
\]

Write \(\alpha,\beta\) for its roots.  Then

\[
 a_n=\alpha^n+\beta^n,
 \qquad
 N_n=\#E(\mathbb F_{5^n})=5^n+1-a_n,
 \tag{2.3}
\]

and the sequence satisfies

\[
 a_0=2,\qquad a_1=-3,\qquad a_n=-3a_{n-1}-5a_{n-2}\quad(n\ge2).
 \tag{2.4}
\]

The exact values

\[
 (a_1,N_1)=(-3,9),\qquad (a_2,N_2)=(-1,27),\qquad (a_3,N_3)=(18,108)
 \tag{2.5}
\]

are used only as arithmetic cross-checks after the geometry is built.

## 3. The geometric correspondence package

Set

\[
 S=E\times E,
 \qquad
 F_{\mathrm v}=\{O\}\times E,
 \qquad
 F_{\mathrm h}=E\times\{O\},
 \qquad
 \Delta=\{(P,P):P\in E\}.
 \tag{3.1}
\]

For \(n\ge0\), define the Frobenius graph

\[
 \Gamma_n=\Gamma_{F^n}=\{(P,F^n(P)):P\in E\}\subset S.
 \tag{3.2}
\]

The first projection identifies \(\Gamma_n\) with \(E\), while the
second projection identifies \(\Gamma_n\) with \(E\) via \(F^n\).

### Proposition 3.1: graph composition

For all \(m,n\ge0\),

\[
 \Gamma_m\circ\Gamma_n=\Gamma_{m+n}.
 \tag{3.3}
\]

Proof.  The composition correspondence is the image of the fiber product
\(\Gamma_n\times_E\Gamma_m\), where the second projection of
\(\Gamma_n\) is matched with the first projection of \(\Gamma_m\).  A
point of the fiber product is a triple \((P,Q,R)\) with
\(Q=F^n(P)\) and \(R=F^m(Q)\), hence \(R=F^{m+n}(P)\).  Therefore the
image in \(E\times E\) is exactly the graph of \(F^{m+n}\).  \(\square\)

### Proposition 3.2: transpose

The transpose correspondence \(\Gamma_n^t\) is the graph of the
Verschiebung \(V^n\), characterized by

\[
 V^n\circ F^n=F^n\circ V^n=[5^n].
 \tag{3.4}
\]

Proof.  By definition, transposition exchanges the two factors of
\(E\times E\), so \(\Gamma_n^t\) is the image of
\(P\mapsto(F^n(P),P)\).  On an elliptic curve over a finite field, this
is the graph of the dual isogeny to \(F^n\), namely \(V^n\).  \(\square\)

### Proposition 3.3: bidegrees and rulings

For every \(n\ge0\),

\[
 \Gamma_n\cdot F_{\mathrm v}=1,
 \qquad
 \Gamma_n\cdot F_{\mathrm h}=5^n.
 \tag{3.5}
\]

Proof.  Intersecting with \(F_{\mathrm v}\) imposes \(P=O\), hence the
only intersection point is \((O,F^n(O))=(O,O)\).  Since \(\Gamma_n\) is
the graph of a morphism over the first factor, the first projection is
an isomorphism and the local intersection multiplicity is \(1\).

Intersecting with \(F_{\mathrm h}\) imposes \(F^n(P)=O\).  The scheme of
solutions is \(\ker(F^n)\), whose degree is the degree of the purely
inseparable isogeny \(F^n\), namely \(5^n\).  Therefore
\(\Gamma_n\cdot F_{\mathrm h}=5^n\).  \(\square\)

The ordered pair \((\Gamma_n\cdot F_{\mathrm v},\Gamma_n\cdot
F_{\mathrm h})=(1,5^n)\) is the exact bidegree used later in the
critical balancing.

## 4. Lefschetz fixed-point intersections

### Proposition 4.1: diagonal trace

For every \(n\ge1\),

\[
 \Gamma_n\cdot\Delta=N_n=\#E(\mathbb F_{5^n}).
 \tag{4.1}
\]

Proof.  The scheme-theoretic intersection \(\Gamma_n\cap\Delta\) is the
fixed-point scheme of \(F^n\), equivalently the kernel of the isogeny
\(F^n-\mathrm{id}_E\).  Since the differential of \(F^n\) is zero in
characteristic \(5\), the differential of \(F^n-\mathrm{id}\) is
\(-\mathrm{id}\), so the isogeny is separable.  Therefore its degree
equals the number of geometric points in its kernel.

The fixed points of \(F^n\) are exactly the \(\mathbb F_{5^n}\)-rational
points of \(E\).  Hence the degree of the fixed-point scheme is
\(\#E(\mathbb F_{5^n})=N_n\).  \(\square\)

### Proposition 4.2: graph-versus-graph cross-check

For \(m>n\),

\[
 \Gamma_m\cdot\Gamma_n=5^nN_{m-n}.
 \tag{4.2}
\]

Proof.  A point lies in \(\Gamma_m\cap\Gamma_n\) exactly when
\(F^m(P)=F^n(P)\), or equivalently when
\(F^n(F^{m-n}(P)-P)=0\).  Thus the intersection scheme is the kernel of
the composite isogeny

\[
 E\xrightarrow{F^{m-n}-\mathrm{id}}E\xrightarrow{F^n}E.
 \tag{4.3}
\]

The first factor is separable of degree \(N_{m-n}\) by Proposition 4.1,
and the second factor is purely inseparable of degree \(5^n\).  Degrees
multiply under composition, so the intersection degree is
\(5^nN_{m-n}\).  \(\square\)

This identity is the internal consistency check demanded by the
specification: the same graph package controls both composition and
intersection multiplicity.

## 5. Connected Euler extraction

Let \(B_d\) denote the number of closed points of \(E\) of degree \(d\).
Every degree-\(d\) closed point contributes exactly \(d\) geometric
points to \(E(\mathbb F_{5^n})\) when \(d\mid n\), and contributes
nothing otherwise.  Therefore

\[
 N_n=\sum_{d\mid n} dB_d.
 \tag{5.1}
\]

M\"obius inversion gives

\[
 B_n=\frac1n\left(N_n-\sum_{\substack{d\mid n\\ d<n}} dB_d\right).
 \tag{5.2}
\]

### Proposition 5.1: connected/primitive Euler decomposition

The zeta function of \(E\) is recovered from the fixed-point counts by

\[
 Z_E(u)=\exp\left(\sum_{n\ge1}\frac{N_n}{n}u^n\right)
       =\prod_{d\ge1}(1-u^d)^{-B_d}.
 \tag{5.3}
\]

Proof.  Starting from the right-hand side,

\[
 \log\prod_{d\ge1}(1-u^d)^{-B_d}
 =\sum_{d\ge1}B_d\sum_{k\ge1}\frac{u^{kd}}{k}
 =\sum_{n\ge1}\frac1n\left(\sum_{d\mid n}dB_d\right)u^n
 =\sum_{n\ge1}\frac{N_n}{n}u^n,
 \tag{5.4}
\]

which proves the claim.  \(\square\)

For the fixed curve one obtains

\[
 B_1=9,\qquad B_2=9,\qquad B_3=33,
 \tag{5.5}
\]

matching the exact preflight script.

The categorical point is that \(N_n\) is a total trace over \(n\)-step
returns, while \(B_d\) is the connected contribution of primitive closed
orbits of degree \(d\).  The logarithm of the Euler product is precisely
the connected projector.

## 6. Critical balancing from bidegree

The graph \(\Gamma_{kd}\) has bidegree \((1,5^{kd})\).  The symmetric
half-density normalization attached to a correspondence of bidegree
\((a,b)\) is

\[
 (ab)^{-1/2}.
 \tag{6.1}
\]

Applied to \(\Gamma_{kd}\), this yields

\[
 (1\cdot 5^{kd})^{-1/2}=5^{-kd/2}.
 \tag{6.2}
\]

Therefore a primitive closed orbit of degree \(d\), iterated \(k\)
times, acquires exactly the critical weight

\[
 5^{-kd/2}.
 \tag{6.3}
\]

This is not inserted by hand.  It is forced by the geometric bidegree
already established in Proposition 3.3.  In the arithmetic target of
107.00 the analogous normalization is required to produce \(p^{-k/2}\)
from a source correspondence of logarithmic length \(k\log p\).

## 7. Primitive projection and direct intersection algebra

Because \(S=E\times E\) is an abelian surface, its canonical divisor is
trivial.  Any embedded translate of \(E\) in \(S\) therefore has
self-intersection \(0\) by the adjunction formula.  In particular,

\[
 F_{\mathrm v}^2=F_{\mathrm h}^2=\Delta^2=\Gamma_n^2=0.
 \tag{7.1}
\]

Also,

\[
 F_{\mathrm v}\cdot F_{\mathrm h}=1,
 \qquad
 \Delta\cdot F_{\mathrm v}=1,
 \qquad
 \Delta\cdot F_{\mathrm h}=1,
 \tag{7.2}
\]

and by Proposition 3.3,

\[
 \Gamma_n\cdot F_{\mathrm v}=1,
 \qquad
 \Gamma_n\cdot F_{\mathrm h}=5^n.
 \tag{7.3}
\]

Define the primitive classes by subtracting their ruling components:

\[
 \Delta^0=\Delta-F_{\mathrm v}-F_{\mathrm h},
 \qquad
 \Gamma_n^0=\Gamma_n-5^nF_{\mathrm v}-F_{\mathrm h}.
 \tag{7.4}
\]

### Proposition 7.1: primitive self-intersections

For every \(n\ge1\),

\[
 (\Delta^0)^2=-2,
 \qquad
 (\Gamma_n^0)^2=-2\cdot 5^n.
 \tag{7.5}
\]

These identities are exactly right for the present elliptic control
\(g=1\).  They do **not** by themselves show that the same source route
would produce \(-2g\) and \(-2gq^n\) for general genus \(g\); that
separate portability question is now isolated by `107_28`.

Proof.  Expanding \((\Delta-F_{\mathrm v}-F_{\mathrm h})^2\) and using
\(F_{\mathrm v}^2=F_{\mathrm h}^2=\Delta^2=0\) together with
\(\Delta\cdot F_{\mathrm v}=\Delta\cdot F_{\mathrm h}
=F_{\mathrm v}\cdot F_{\mathrm h}=1\), we obtain

\[
 (\Delta^0)^2=0-2-2+2=-2.
 \tag{7.6}
\]

Similarly,

\[
 (\Gamma_n^0)^2
 =\Gamma_n^2
 -2\cdot5^n(\Gamma_n\cdot F_{\mathrm v})
 -2(\Gamma_n\cdot F_{\mathrm h})
 +2\cdot5^n(F_{\mathrm v}\cdot F_{\mathrm h}),
 \tag{7.7}
\]

which becomes

\[
 (\Gamma_n^0)^2=0-2\cdot5^n-2\cdot5^n+2\cdot5^n=-2\cdot5^n.
 \tag{7.8}
\]

\(\square\)

### Proposition 7.2: primitive cross term

For every \(n\ge1\),

\[
 \Gamma_n^0\cdot\Delta^0=-a_n.
 \tag{7.9}
\]

Proof.  Expand the product:

\[
 \Gamma_n^0\cdot\Delta^0
 =\Gamma_n\cdot\Delta
 -\Gamma_n\cdot F_{\mathrm v}
 -\Gamma_n\cdot F_{\mathrm h}
 -5^n(F_{\mathrm v}\cdot\Delta)
 +5^n(F_{\mathrm v}\cdot F_{\mathrm h})
 -F_{\mathrm h}\cdot\Delta
 +F_{\mathrm h}\cdot F_{\mathrm v}.
 \tag{7.10}
\]

Substituting
\(\Gamma_n\cdot\Delta=N_n\),
\(\Gamma_n\cdot F_{\mathrm v}=1\),
\(\Gamma_n\cdot F_{\mathrm h}=5^n\),
\(F_{\mathrm v}\cdot\Delta=F_{\mathrm h}\cdot\Delta
=F_{\mathrm v}\cdot F_{\mathrm h}=1\),
we get

\[
 \Gamma_n^0\cdot\Delta^0=N_n-1-5^n-5^n+5^n-1+1=N_n-5^n-1.
 \tag{7.11}
\]

Using \(N_n=5^n+1-a_n\), this equals \(-a_n\).  \(\square\)

Hence the primitive Gram matrix is

\[
 G_n^0=
 \begin{pmatrix}
 -2&-a_n\\
 -a_n&-2\cdot5^n
 \end{pmatrix}.
 \tag{7.12}
\]

## 8. Hodge index and the Weil bound

The divisor \(H=F_{\mathrm v}+F_{\mathrm h}\) is ample on \(E\times E\).
Its orthogonal complement in \(\mathrm{NS}(S)_{\mathbf R}\) is negative
semidefinite by the Hodge-index theorem.  By construction,

\[
 \Delta^0\cdot H=0,
 \qquad
 \Gamma_n^0\cdot H=0,
 \tag{8.1}
\]

so both primitive classes lie in that negative subspace.

### Theorem 8.1: calibrated Weil estimate

For every \(n\ge1\),

\[
 \det G_n^0=4\cdot5^n-a_n^2\ge0,
 \qquad
 |a_n|\le2\cdot5^{n/2}.
 \tag{8.2}
\]

Proof.  Since the restriction of the intersection form to
\(\mathbf R\Delta^0+\mathbf R\Gamma_n^0\) is negative semidefinite, its
Gram determinant is nonnegative:

\[
 \det G_n^0
 =(-2)(-2\cdot5^n)-(-a_n)^2
 =4\cdot5^n-a_n^2
 \ge0.
 \tag{8.3}
\]

Rearranging gives
\(|a_n|\le2\cdot5^{n/2}\).  Because \(N_n=5^n+1-a_n\), this is
equivalent to the classical Weil estimate

\[
 \bigl|5^n+1-\#E(\mathbb F_{5^n})\bigr|
 \le 2\cdot5^{n/2}.
 \tag{8.4}
\]

\(\square\)

For the control curve \(g(E)=1\), so (8.4) is exactly the genus-one case
of the function-field Riemann hypothesis.

## 9. Equality and radical calibration

Equality in (8.2) occurs exactly when the primitive plane generated by
\(\Delta^0\) and \(\Gamma_n^0\) contains a nonzero isotropic class.
Equivalently,

\[
 a_n^2=4\cdot5^n
 \quad\Longleftrightarrow\quad
 \Gamma_n^0 \text{ and } \Delta^0 \text{ become linearly dependent in }
 \mathrm{NS}(S)_{\mathbf R}/\mathrm{rad}.
 \tag{9.1}
\]

This is the correct geometric equality mechanism to compare later with
the arithmetic radical audit of 107.00.  In the present control, \(E\) is
ordinary because \(a_1=-3\) is not divisible by \(5\).  For an ordinary
elliptic curve, the ratio \(\alpha/\beta\) is not a root of unity, so the
strict inequality

\[
 a_n^2<4\cdot5^n
 \tag{9.2}
\]

holds for all \(n\ge1\).  Thus the primitive plane is actually negative
definite for the chosen control curve.

## 10. Calibration ledger

The fixed control curve \(E/\mathbb F_5\) now realizes every interface
required by 107.01:

1. Frobenius graphs compose by genuine fiber products:
   \(\Gamma_m\circ\Gamma_n=\Gamma_{m+n}\).
2. The diagonal trace is scheme-theoretic:
   \(\Gamma_n\cdot\Delta=N_n\).
3. Primitive closed orbits are extracted from total return counts by the
   connected Euler projector:
   \(N_n=\sum_{d\mid n}dB_d\).
4. Critical balancing is forced by bidegree:
   \((1,5^{kd})\mapsto5^{-kd/2}\).
5. Primitive correction is fixed before the Hodge step:
   \(\Delta^0=\Delta-F_{\mathrm v}-F_{\mathrm h}\) and
   \(\Gamma_n^0=\Gamma_n-5^nF_{\mathrm v}-F_{\mathrm h}\).
6. Only after the previous steps are established does the Hodge index
   yield the Weil bound.

This completes Paper 0 in the sense of the stop rule of Phase 107: the
source correspondence package specializes to the proved Frobenius--
Lefschetz--Hodge mechanism on the fixed function-field control without
retrofitting any step from the zeta function or from a presupposed sign.

Residual scope limit:
this closes the fixed \(g=1\) control, not yet a genus-uniform
source-construction theorem for the primitive diagonal package.  That
separate gate is now isolated by `107_28`.

## 11. Recalibration after the genus audit

The correct post-`107_28` reading of Paper 0 is:

1. `107_02` proves the fixed elliptic control exactly as intended;
2. `107_28` shows that genus-sensitive portability of the primitive
   diagonal entries cannot be treated as automatic;
3. no later paper should silently use the elliptic diagonal values
   \(-2,-2q^n\) as if they already came from a genus-uniform source
   construction.

This is a recalibration of scope, not a retraction of the elliptic
proof.
