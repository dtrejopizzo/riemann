# 107.192 -- The Green channel is a flat connection, not a Chern class

## 1. Logarithmic connection from the source

On

\[
 \mathcal H=\{s\in\mathbb C:\Re(s)>1\},
\]

the Euler construction of `107_182--187` gives a holomorphic,
nowhere-zero determinant \(\xi(s)\), without using its zeros as input.
Equip the trivialized determinant line with the logarithmic connection

\[
 \nabla=d+A,\qquad A=-d\log\xi(s).
 \tag{1.1}
\]

Its coefficient is exactly the completed Green channel:

\[
 A=-{\xi'(s)\over\xi(s)}\,ds.
 \tag{1.2}
\]

At a finite prime,

\[
 -d\log(1-p^{-s})^{-1}
 =\log p\,{p^{-s}\over1-p^{-s}}\,ds.
\]

Thus the orbit return kernel of `107_185`, multiplied by its orbit
length, is the local logarithmic connection coefficient.

## 2. Exact flatness

Because (1.1) is a scalar logarithmic differential,

\[
 F_\nabla=dA+A\wedge A
 =-d^2\log\xi+0=0.
 \tag{2.1}
\]

Equivalently, for the Hermitian norm induced by the determinant,

\[
 \|1\|^2=|\xi(s)|^{-2},
\]

the Chern curvature is

\[
 -\partial\bar\partial\log\|1\|^2
 =2\partial\bar\partial\log|\xi(s)|=0
 \qquad(s\in\mathcal H).
 \tag{2.2}
\]

This is the elementary Poincare--Lelong statement away from the divisor:
the logarithm of the modulus of a nowhere-zero holomorphic function is
harmonic.

## 3. No-go theorem

**Theorem.**  On \(\mathcal H\), the completed prime--Gamma--pole
channel of `107_183` is realized by a flat logarithmic connection, but
it cannot be realized as the ordinary Chern curvature of the determinant
metric \(|\xi|^{-2}\).  Consequently no intersection construction
depending only on that smooth curvature can recover the explicit-formula
distribution.

**Proof.**  Equation (1.2) gives the Green channel exactly.  Equations
(2.1)--(2.2) show that both its connection curvature and the associated
\((1,1)\)-form vanish identically.  The Green channel is generally
nonzero, so it lives in the connection/transgression datum rather than
in its ordinary Chern class. \(\square\)

## 4. Where a nonzero current can occur

There are only three surviving mechanisms in this architecture:

1. extend meromorphically and use the divisor current in
   \(dd^c\log|\xi|\);
2. retain a boundary/relative term rather than passing to absolute
   curvature;
3. use analytic torsion or a Bott--Chern/Bismut--Goette secondary class.

The first mechanism is admissible only if the extension and its divisor
are derived from the prime/Gamma determinant, never inserted from a zero
table.  The second and third mechanisms require geometry beyond the
product semilocal line.  Koehler--Roessler's arithmetic residue formula
exhibits precisely such an analytic-torsion/current term, but its
hypotheses require a torus-projective arithmetic variety, flat fixed
scheme, compact complex manifold, normal bundle, and invariant Kahler
metric.  None of those structures is supplied by `107_190`.

## 5. Exact scope

This does not say that the determinant connection is useless: it is the
first geometric carrier constructed here whose one-form is exactly the
completed Green channel.  It says that taking its ordinary curvature
forgets that information.

Nor does it rule out singular Hermitian metrics, relative differential
characters, Quillen metrics, analytic torsion, or equivariant
Bott--Chern currents.  It closes only the route

\[
 \text{holomorphic determinant on }\mathcal H
 \longrightarrow |\det|\text{ smooth metric}
 \longrightarrow c_1
 \longrightarrow\text{row (c)}.
\]

## 6. Falsifier

The verifier independently evaluates the completed logarithmic
derivative from \(\xi\) and from the prime--Gamma--pole decomposition.
It checks vanishing of the complex Laplacian of \(\log|\xi|\) at a
fixed real/complex atlas by independent high-precision partial
derivatives.  As a control, multiplication of the metric by
\(e^{|s|^2}\) must produce
nonzero curvature; failure to distinguish that mutation returns
`VERDICT: NO`.
